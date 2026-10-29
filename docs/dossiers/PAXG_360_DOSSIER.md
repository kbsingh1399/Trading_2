# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 01:02:38 IST` (`2026-10-29 19:32:38 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4012.59` | **Live Ask Quote**: `4012.67` | **Mid Price**: `4012.63`
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
  * Session VWAP: `4012.63` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `10.03` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4040.72` | Lower -3.00σ Band: `3984.54`
  * Upper +2.51σ Band: `4034.70` | Lower -2.51σ Band: `3990.56`
  * Upper +2.01σ Band: `4029.48` | Lower -2.01σ Band: `3995.78`
  * Upper +2.00σ Band: `4028.68` | Lower -2.00σ Band: `3996.58`
  * Upper +1.28σ Band: `4023.87` | Lower -1.28σ Band: `4001.39`
  * Upper +1.00σ Band: `4020.66` | Lower -1.00σ Band: `4004.60`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4012.63` | EMA-20=`4012.63` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4012.63` (Slope: `+0.0000`) | EMA-100=`4012.63`
  * Institutional Anchors: EMA-144=`4012.63` | EMA-200=`4012.63` (Slope: `+0.0000`) | EMA-233=`4012.63`
- **Range Boundaries**: 24H High=`4052.76` | 24H Low=`3972.50` | Weekly High=`4092.88` | Weekly Low=`3932.38`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4041.38` (Distance: `-0.72%`)
  * Point of Control (POC) = `4027.32` (Distance: `-0.37%`)
  * Value Area Low (VAL) = `4017.10` (Distance: `-0.12%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4059.03` | POC=`4041.68` | VAL=`4035.89`
  * Prior Day Extremes: PDH=`4082.75` | PDL=`4024.90` | PDC=`4067.36`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.72` | Weekly POC=`4014.77` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4069.28` | Low=`4035.73`
  * London Session (08:00-16:00 UTC): High=`4046.38` | Low=`4015.80`
  * New York Session (13:00-21:00 UTC): High=`4039.31` | Low=`4010.16`
  * Initial Balance (First Hour): IB High=`4046.38` | IB Low=`4022.15`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3996.58` - `4028.68`
  * Optimal Trade Entry (OTE 0.705): `4020.66`
  * Structural Invalidation Anchor (0.786): `4044.73`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4016.92` | `4016.92` | `4014.71` | `4015.27` | `69` | 275,644.38 USD | -227,662.19 USD | `-82.59%` | 1,089,650.57 USD | `-1.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4015.26` | `4016.76` | `4014.71` | `4016.52` | `12` | 46,642.67 USD | 15,296.36 USD | `+32.79%` | 1,104,946.92 USD | `+0.06` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4016.52` | `4017.75` | `4016.52` | `4017.20` | `10` | 41,556.93 USD | 23,543.33 USD | `+56.65%` | 1,128,490.25 USD | `+0.10` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4014.54` | `4017.97` | `4013.57` | `4017.56` | `132` | 528,554.94 USD | 354,179.10 USD | `+67.01%` | 1,835,616.70 USD | `+1.28` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4017.56` | `4018.64` | `4014.71` | `4015.27` | `224` | 899,445.34 USD | -718,002.67 USD | `-79.83%` | 1,117,614.03 USD | `-2.65` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4015.26` | `4017.75` | `4014.71` | `4017.20` | `22` | 88,199.60 USD | 38,839.69 USD | `+44.04%` | 1,156,453.72 USD | `+0.03` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4023.30` | `4029.00` | `4011.95` | `4011.96` | `549` | 2,206,317.77 USD | -210,291.82 USD | `-9.53%` | 1,017,172.68 USD | `-0.59` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4011.95` | `4017.97` | `4011.01` | `4017.56` | `511` | 2,050,996.96 USD | 1,105,382.66 USD | `+53.89%` | 2,122,555.33 USD | `+1.88` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4017.56` | `4018.64` | `4014.71` | `4017.20` | `246` | 987,644.95 USD | -679,162.98 USD | `-68.77%` | 1,443,392.35 USD | `-1.43` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4017.20` | `2,256` | 9,068,685.04 USD | 1,066,342.07 USD | `+11.76%` | 1,443,392.35 USD | `+1.46` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4053.44` | `4065.63` | `4036.00` | `4038.03` | `3,568` | 14,441,971.44 USD | 632,777.98 USD | `+4.38%` | 855,497.47 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | 197,313.54 USD | `-1.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4017.20` | `2,256` | 9,068,685.04 USD | 1,066,342.07 USD | `+11.76%` | 1,443,392.35 USD | `+1.46` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4011.50` | `5.9678` | 23,939.83 USD | 1,587,112.00 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4011.60` | `9.4528` | 37,920.85 USD | 1,563,172.18 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4011.70` | `0.8869` | 3,557.98 USD | 1,525,251.32 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4011.80` | `21.4692` | 86,130.14 USD | 1,521,693.35 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `4011.90` | `59.6067` | 239,136.12 USD | 1,435,563.21 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `4012.00` | `7.5919` | 30,458.70 USD | 1,196,427.09 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4012.10` | `3.8200` | 15,326.22 USD | 1,165,968.39 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `4012.20` | `4.7621` | 19,106.50 USD | 1,150,642.16 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4012.30` | `85.0436` | 341,220.44 USD | 1,131,535.67 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4012.40` | `21.9845` | 88,210.61 USD | 790,315.23 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4012.50` | `7.4748` | 29,992.64 USD | 702,104.62 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4012.60` | `5.4247` | 21,767.15 USD | 672,111.99 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4012.70` | `57.3165` | 229,993.92 USD | 650,344.84 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4012.80` | `5.5213` | 22,155.87 USD | 420,350.92 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4012.90` | `16.6861` | 66,959.65 USD | 398,195.04 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4013.00` | `10.3404` | 41,496.03 USD | 331,235.39 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4013.10` | `18.1629` | 72,889.53 USD | 289,739.37 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4013.20` | `3.6406` | 14,610.46 USD | 216,849.83 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4013.30` | `22.6836` | 91,036.09 USD | 202,239.38 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `4013.40` | `27.7080` | 111,203.29 USD | 111,203.29 USD | `6 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4013.45` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,013.45` | `0.00%` | `-` |
| `ASK` | `4013.50` | `32.9982` | 132,438.28 USD | 132,438.28 USD | `12 orders` | `+0.00%` | `-` |
| `ASK` | `4013.60` | `11.6604` | 46,800.18 USD | 179,238.46 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `4013.70` | `15.8719` | 63,705.05 USD | 242,943.50 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `4013.80` | `13.2757` | 53,286.00 USD | 296,229.51 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4013.90` | `22.5262` | 90,417.91 USD | 386,647.42 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `4014.00` | `7.4748` | 30,003.85 USD | 416,651.27 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4014.10` | `20.5154` | 82,350.87 USD | 499,002.14 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4014.20` | `10.2744` | 41,243.50 USD | 540,245.63 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4014.30` | `66.0860` | 265,289.03 USD | 805,534.66 USD | `7 orders` | `+0.02%` | `-` |
| `ASK` | `4014.40` | `21.5375` | 86,460.14 USD | 891,994.80 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4014.50` | `2.1419` | 8,598.66 USD | 900,593.46 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4014.60` | `2.1457` | 8,614.13 USD | 909,207.59 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4014.70` | `14.8735` | 59,712.64 USD | 968,920.23 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4014.80` | `7.7754` | 31,216.68 USD | 1,000,136.90 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4014.90` | `35.2288` | 141,440.11 USD | 1,141,577.01 USD | `7 orders` | `+0.04%` | `-` |
| `ASK` | `4015.00` | `0.2507` | 1,006.56 USD | 1,142,583.57 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `4015.10` | `8.4811` | 34,052.46 USD | 1,176,636.04 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4015.20` | `18.1163` | 72,740.57 USD | 1,249,376.60 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4015.30` | `3.6205` | 14,537.39 USD | 1,263,914.00 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `4015.50` | `65.3748` | 262,512.51 USD | 1,526,426.51 USD | `9 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:53:52 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `54` | `0x5b5d...c060` | `SHORT` | 25,592,740.16 USD | `6,373.65` | `4191.43` | `4015.40` | `29303.46` | 1,122,009.04 USD | `+4.38%` | `4X Cross` |
| `56` | `0x4692...164f` | `SHORT` | 25,340,136.16 USD | `6,310.74` | `4133.85` | `4015.40` | `13282.50` | 747,561.70 USD | `+2.95%` | `5X Cross` |
| `73` | `0xb83d...6e36` | `SHORT` | 22,944,846.20 USD | `5,717.06` | `4234.49` | `4015.40` | `27641.34` | 1,264,029.03 USD | `+5.51%` | `5X Cross` |
| `99` | `0xec0b...b078` | `LONG` | 19,380,334.95 USD | `4,828.91` | `4157.43` | `4015.40` | `2092.37` | -695,547.36 USD | `-3.59%` | `25X Cross` |
| `147` | `0x645b...87b8` | `LONG` | 14,129,772.59 USD | `3,518.90` | `4129.56` | `4015.40` | `296.97` | -401,721.99 USD | `-2.84%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,122,856.46 USD | `3,268.21` | `4228.94` | `4015.40` | `4409.42` | 698,222.67 USD | `+5.32%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,638,860.40 USD | `2,900.00` | `4364.92` | `4015.40` | `4235.62` | 1,019,415.93 USD | `+8.76%` | `20X Cross` |
| `276` | `0x3678...b209` | `LONG` | 8,833,660.00 USD | `2,200.00` | `4176.09` | `4015.40` | `2478.97` | -353,759.30 USD | `-4.00%` | `25X Cross` |
| `277` | `0x41e5...0825` | `SHORT` | 8,829,480.00 USD | `2,200.00` | `4112.20` | `4015.40` | `4331.10` | 217,374.59 USD | `+2.46%` | `20X Cross` |
| `308` | `0xfc66...ca06` | `SHORT` | 7,978,156.50 USD | `1,986.89` | `4032.86` | `4015.40` | `25003.01` | 34,709.67 USD | `+0.44%` | `3X Cross` |
| `311` | `0xacb6...efbd` | `SHORT` | 7,927,946.35 USD | `1,975.37` | `4048.55` | `4015.40` | `6499.40` | 69,445.37 USD | `+0.88%` | `6X Cross` |
| `381` | `0xc26c...b8f4` | `LONG` | 6,344,138.46 USD | `1,579.95` | `4075.62` | `4015.40` | `0.000000` | -95,158.51 USD | `-1.50%` | `1X Cross` |
| `419` | `0x12d2...f97f` | `LONG` | 5,626,557.23 USD | `1,401.94` | `4278.91` | `4015.40` | `2523.22` | -372,233.35 USD | `-6.62%` | `20X Cross` |
| `576` | `0x63da...8add` | `LONG` | 4,015,400.00 USD | `1,000.00` | `4021.46` | `4015.40` | `3564.06` | -6,060.96 USD | `-0.15%` | `25X Cross` |
| `597` | `0x9aa5...58af` | `LONG` | 3,899,588.00 USD | `971.64` | `4279.98` | `4015.40` | `0.000000` | -259,021.08 USD | `-6.64%` | `20X Cross` |
| `627` | `0xf3dc...1672` | `LONG` | 3,736,005.21 USD | `930.74` | `4024.62` | `4015.40` | `3337.54` | -9,887.35 USD | `-0.26%` | `20X Cross` |
| `689` | `0x4a20...3c26` | `LONG` | 3,362,411.02 USD | `837.40` | `4599.73` | `4015.40` | `0.000000` | -489,409.37 USD | `-14.56%` | `20X Cross` |
| `705` | `0x354b...6425` | `LONG` | 3,295,479.98 USD | `820.73` | `4033.57` | `4015.40` | `0.000000` | -14,998.89 USD | `-0.46%` | `10X Cross` |
| `844` | `0x0fac...7a0a` | `LONG` | 2,756,443.22 USD | `686.49` | `4290.34` | `4015.40` | `1325.71` | -188,815.48 USD | `-6.85%` | `25X Cross` |
| `886` | `0xd8c5...99b0` | `SHORT` | 2,579,054.92 USD | `642.35` | `4175.35` | `4015.40` | `32030.49` | 103,006.25 USD | `+3.99%` | `4X Cross` |
| `921` | `0x625e...a354` | `SHORT` | 2,488,308.00 USD | `620.00` | `4122.81` | `4015.40` | `4342.20` | 67,839.03 USD | `+2.73%` | `20X Cross` |
| `949` | `0xeae3...e8ad` | `SHORT` | 2,408,880.00 USD | `600.00` | `4104.77` | `4015.40` | `4325.22` | 53,985.11 USD | `+2.24%` | `20X Cross` |
| `952` | `0xf285...fa82` | `LONG` | 2,400,438.22 USD | `598.11` | `4146.45` | `4015.40` | `3891.19` | -79,581.33 USD | `-3.32%` | `25X Cross` |
| `969` | `0x12f7...8750` | `LONG` | 2,351,461.20 USD | `585.61` | `4082.77` | `4015.40` | `2155.18` | -39,455.77 USD | `-1.68%` | `10X Cross` |
| `1133` | `0x413c...886c` | `LONG` | 2,007,000.00 USD | `500.00` | `4010.43` | `4015.40` | `0.000000` | 1,783.77 USD | `+0.09%` | `2X Cross` |
| `1141` | `0x61ce...a62b` | `SHORT` | 1,997,377.05 USD | `497.50` | `4071.66` | `4015.40` | `4692.60` | 28,291.74 USD | `+1.42%` | `20X Cross` |
| `1143` | `0x0593...40f9` | `LONG` | 1,992,150.66 USD | `496.18` | `4024.57` | `4015.40` | `3701.68` | -4,753.17 USD | `-0.24%` | `10X Isolated` |
| `1262` | `0x2edd...8179` | `LONG` | 1,823,271.60 USD | `453.58` | `4169.95` | `4019.70` | `0.000000` | -68,152.51 USD | `-3.74%` | `10X Cross` |
| `1263` | `0xead5...69f2` | `LONG` | 1,821,216.30 USD | `453.78` | `4220.88` | `4015.40` | `3538.89` | -94,151.75 USD | `-5.17%` | `5X Isolated` |
| `1321` | `0x7a6d...f79c` | `SHORT` | 1,720,969.79 USD | `428.38` | `4136.09` | `4019.70` | `5904.25` | 50,845.21 USD | `+2.95%` | `10X Cross` |
| `1388` | `0x46fc...1195` | `LONG` | 1,633,812.40 USD | `407.03` | `4055.53` | `4015.40` | `1929.19` | -16,907.42 USD | `-1.03%` | `20X Cross` |
| `1424` | `0xee02...309d` | `SHORT` | 1,606,160.00 USD | `400.00` | `4438.84` | `4015.40` | `4226.84` | 169,378.60 USD | `+10.55%` | `25X Isolated` |
| `1426` | `0x6d15...d374` | `LONG` | 1,605,360.00 USD | `400.00` | `4068.25` | `4015.40` | `3841.76` | -21,940.00 USD | `-1.37%` | `25X Cross` |
| `1451` | `0x02a7...fe9f` | `SHORT` | 1,566,006.00 USD | `390.00` | `4055.02` | `4015.40` | `4306.66` | 15,453.25 USD | `+0.99%` | `25X Cross` |
| `1486` | `0x51f6...2b39` | `LONG` | 1,529,097.14 USD | `380.49` | `4234.66` | `4019.70` | `0.000000` | -82,130.93 USD | `-5.37%` | `10X Cross` |
| `1490` | `0x7e77...b8d2` | `SHORT` | 1,525,700.00 USD | `380.00` | `4131.92` | `4015.40` | `4293.46` | 44,429.64 USD | `+2.91%` | `20X Cross` |
| `1508` | `0x72c2...9b37` | `LONG` | 1,497,749.04 USD | `373.13` | `4000.98` | `4015.40` | `3777.99` | 4,855.52 USD | `+0.32%` | `13X Isolated` |
| `1546` | `0xaa44...b844` | `LONG` | 1,445,040.00 USD | `360.00` | `4043.10` | `4015.40` | `2803.21` | -10,477.63 USD | `-0.73%` | `4X Cross` |
| `1547` | `0x781e...96b7` | `SHORT` | 1,444,959.54 USD | `359.55` | `4365.03` | `4019.70` | `12655.58` | 124,487.94 USD | `+8.62%` | `10X Cross` |
| `1658` | `0xa41f...d50a` | `LONG` | 1,320,256.49 USD | `328.96` | `4468.89` | `4015.40` | `3833.14` | -149,841.36 USD | `-11.35%` | `15X Cross` |
| `1686` | `0x49e9...e1d0` | `SHORT` | 1,299,179.63 USD | `323.56` | `4025.23` | `4015.40` | `28777.23` | 3,213.07 USD | `+0.25%` | `4X Cross` |
| `1713` | `0xada6...6f88` | `LONG` | 1,281,827.68 USD | `319.28` | `4166.46` | `4015.40` | `1865.89` | -48,422.83 USD | `-3.78%` | `5X Cross` |
| `1721` | `0xbf5a...88ba` | `SHORT` | 1,274,876.18 USD | `317.65` | `4091.80` | `4015.40` | `10490.54` | 24,906.86 USD | `+1.95%` | `20X Cross` |
| `1738` | `0xff31...ff6c` | `SHORT` | 1,244,650.00 USD | `310.00` | `4372.43` | `4015.40` | `4789.13` | 110,805.38 USD | `+8.90%` | `10X Isolated` |
| `1902` | `0x50e2...d770` | `LONG` | 1,085,525.11 USD | `270.37` | `4243.58` | `4015.40` | `2562.05` | -61,801.35 USD | `-5.69%` | `20X Cross` |
| `1915` | `0x4c92...4f17` | `SHORT` | 1,070,962.82 USD | `266.72` | `4260.98` | `4015.40` | `6521.64` | 65,529.41 USD | `+6.12%` | `20X Cross` |
| `1989` | `0xd346...c4f3` | `LONG` | 1,024,114.53 USD | `255.17` | `4188.66` | `4015.40` | `3310.37` | -44,721.98 USD | `-4.37%` | `5X Isolated` |
| `2031` | `0xe47f...758c` | `LONG` | 1,003,500.00 USD | `250.00` | `4020.00` | `4015.40` | `3774.29` | -1,500.00 USD | `-0.15%` | `20X Cross` |
| `2032` | `0x1581...463b` | `LONG` | 1,003,350.00 USD | `250.00` | `4003.77` | `4015.40` | `3504.59` | 2,406.41 USD | `+0.24%` | `15X Cross` |

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
| `7D` | `Long Liquidation` | `3611.20` | 16,640,000.00 USD | 16,640,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3612.60` | 3,620,000.00 USD | 3,620,000.00 USD | 2,900.00 USD | 0.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,560,000.00 USD | 16,560,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3616.80` | 3,610,000.00 USD | 3,610,000.00 USD | 29,730.00 USD | 0.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.80` | 16,420,000.00 USD | 16,420,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3621.00` | 3,580,000.00 USD | 3,580,000.00 USD | 27,050.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3624.10` | 16,360,000.00 USD | 16,360,000.00 USD | 95,230.00 USD | 0.00 USD | 21,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3625.20` | 3,550,000.00 USD | 3,550,000.00 USD | 45,730.00 USD | 0.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.40` | 16,240,000.00 USD | 16,240,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3629.40` | 3,500,000.00 USD | 3,500,000.00 USD | 32,220.00 USD | 0.00 USD | 6,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.70` | 16,050,000.00 USD | 16,050,000.00 USD | 112,500.00 USD | 0.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3633.60` | 3,460,000.00 USD | 3,460,000.00 USD | 24,570.00 USD | 0.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.00` | 15,920,000.00 USD | 15,920,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3637.80` | 3,430,000.00 USD | 3,430,000.00 USD | 45,970.00 USD | 0.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.30` | 15,790,000.00 USD | 15,790,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3642.00` | 3,380,000.00 USD | 3,380,000.00 USD | 10,510.00 USD | 0.00 USD | 4,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.60` | 15,730,000.00 USD | 15,730,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3646.20` | 3,360,000.00 USD | 3,360,000.00 USD | 8,210.00 USD | 0.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.90` | 15,690,000.00 USD | 15,690,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3650.40` | 3,350,000.00 USD | 3,350,000.00 USD | 22,380.00 USD | 0.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3654.20` | 15,670,000.00 USD | 15,670,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3654.60` | 3,330,000.00 USD | 3,330,000.00 USD | 11,860.00 USD | 0.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3658.50` | 15,610,000.00 USD | 15,610,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3658.80` | 3,310,000.00 USD | 3,310,000.00 USD | 8,050.00 USD | 0.00 USD | 759.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.80` | 15,600,000.00 USD | 15,600,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3663.00` | 3,300,000.00 USD | 3,300,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3667.10` | 15,580,000.00 USD | 15,580,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3671.40` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.50` | 15,580,000.00 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3839.10` | 15,570,000.00 USD | 15,570,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3843.40` | 15,150,000.00 USD | 15,150,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.70` | 14,630,000.00 USD | 14,630,000.00 USD | 497,700.00 USD | 0.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.00` | 3,290,000.00 USD | 3,290,000.00 USD | 2,810.00 USD | 0.00 USD | 752.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.00` | 14,070,000.00 USD | 14,070,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.20` | 3,290,000.00 USD | 3,290,000.00 USD | 76,990.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3856.30` | 13,790,000.00 USD | 13,790,000.00 USD | 402,740.00 USD | 0.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.40` | 3,210,000.00 USD | 3,210,000.00 USD | 55,360.00 USD | 0.00 USD | 6,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.60` | 13,360,000.00 USD | 13,360,000.00 USD | 167,120.00 USD | 0.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3864.60` | 3,140,000.00 USD | 3,140,000.00 USD | 150,790.00 USD | 0.00 USD | 14,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.90` | 13,170,000.00 USD | 13,170,000.00 USD | 312,440.00 USD | 0.00 USD | 59,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3868.80` | 2,980,000.00 USD | 2,980,000.00 USD | 104,280.00 USD | 0.00 USD | 20,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3869.20` | 12,800,000.00 USD | 12,800,000.00 USD | 609,640.00 USD | 0.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.00` | 2,850,000.00 USD | 2,850,000.00 USD | 126,290.00 USD | 0.00 USD | 18,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3873.50` | 12,150,000.00 USD | 12,150,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.20` | 2,710,000.00 USD | 2,710,000.00 USD | 99,080.00 USD | 0.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.80` | 11,770,000.00 USD | 11,770,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.40` | 2,600,000.00 USD | 2,600,000.00 USD | 105,320.00 USD | 0.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3882.10` | 11,190,000.00 USD | 11,190,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3885.60` | 2,480,000.00 USD | 2,480,000.00 USD | 22,630.00 USD | 0.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3886.40` | 10,970,000.00 USD | 10,970,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3889.80` | 2,440,000.00 USD | 2,440,000.00 USD | 26,200.00 USD | 0.00 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.70` | 10,880,000.00 USD | 10,880,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3894.00` | 2,410,000.00 USD | 2,410,000.00 USD | 82,900.00 USD | 0.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3895.00` | 10,750,000.00 USD | 10,750,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3898.20` | 2,320,000.00 USD | 2,320,000.00 USD | 32,580.00 USD | 0.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3899.30` | 10,620,000.00 USD | 10,620,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3902.40` | 2,280,000.00 USD | 2,280,000.00 USD | 38,100.00 USD | 0.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3903.60` | 10,500,000.00 USD | 10,500,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3906.60` | 2,240,000.00 USD | 2,240,000.00 USD | 26,240.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.90` | 10,450,000.00 USD | 10,450,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3912.20` | 10,400,000.00 USD | 10,400,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3915.00` | 2,210,000.00 USD | 2,210,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3916.50` | 10,380,000.00 USD | 10,380,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3920.80` | 10,010,000.00 USD | 10,010,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3925.10` | 9,230,000.00 USD | 9,230,000.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3929.40` | 8,190,000.00 USD | 8,190,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.70` | 7,080,000.00 USD | 7,080,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3936.00` | 2,200,000.00 USD | 2,200,000.00 USD | 130,690.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.00` | 6,580,000.00 USD | 6,580,000.00 USD | 711,630.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3940.20` | 2,050,000.00 USD | 2,050,000.00 USD | 94,110.00 USD | 0.00 USD | 11,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3942.30` | 5,840,000.00 USD | 5,840,000.00 USD | 375,470.00 USD | 0.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3944.40` | 1,950,000.00 USD | 1,950,000.00 USD | 268,200.00 USD | 0.00 USD | 16,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.60` | 5,410,000.00 USD | 5,410,000.00 USD | 650,970.00 USD | 0.00 USD | 137,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3948.60` | 1,660,000.00 USD | 1,660,000.00 USD | 227,310.00 USD | 0.00 USD | 48,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.90` | 4,620,000.00 USD | 4,620,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3952.80` | 1,390,000.00 USD | 1,390,000.00 USD | 283,970.00 USD | 0.00 USD | 38,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.20` | 3,450,000.00 USD | 3,450,000.00 USD | 779,760.00 USD | 0.00 USD | 66,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3957.00` | 1,060,000.00 USD | 1,060,000.00 USD | 171,150.00 USD | 0.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.50` | 2,610,000.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3961.20` | 876,740.00 USD | 876,740.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.80` | 1,600,000.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3965.40` | 585,780.00 USD | 585,780.00 USD | 61,120.00 USD | 0.00 USD | 27,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.10` | 1,120,000.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3969.60` | 496,760.00 USD | 496,760.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.40` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3973.80` | 478,380.00 USD | 478,380.00 USD | 156,290.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3978.00` | 315,480.00 USD | 315,480.00 USD | 124,280.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3981.00` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3982.20` | 183,990.00 USD | 183,990.00 USD | 32,780.00 USD | 0.00 USD | 22,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.30` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3986.40` | 128,790.00 USD | 128,790.00 USD | 66,940.00 USD | 0.00 USD | 7,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.60` | 134,160.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3990.60` | 53,970.00 USD | 53,970.00 USD | 31,710.00 USD | 0.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.90` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3999.00` | 20,280.00 USD | 20,280.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4088.50` | 3,010,000.00 USD | 3,010,000.00 USD | 986,980.00 USD | 0.00 USD | 122,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4092.80` | 3,580,000.00 USD | 3,580,000.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4095.60` | 91,610.00 USD | 91,610.00 USD | 78,740.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4097.10` | 4,430,000.00 USD | 4,430,000.00 USD | 805,470.00 USD | 0.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4099.80` | 238,120.00 USD | 238,120.00 USD | 137,710.00 USD | 0.00 USD | 8,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4101.40` | 4,720,000.00 USD | 4,720,000.00 USD | 246,010.00 USD | 0.00 USD | 40,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4104.00` | 400,370.00 USD | 400,370.00 USD | 150,630.00 USD | 0.00 USD | 11,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4105.70` | 5,470,000.00 USD | 5,470,000.00 USD | 651,880.00 USD | 0.00 USD | 104,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4108.20` | 701,730.00 USD | 701,730.00 USD | 260,190.00 USD | 0.00 USD | 41,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4110.00` | 6,560,000.00 USD | 6,560,000.00 USD | 1,020,000.00 USD | 0.00 USD | 68,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4112.40` | 1,010,000.00 USD | 1,010,000.00 USD | 272,530.00 USD | 0.00 USD | 36,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4114.30` | 7,460,000.00 USD | 7,460,000.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4116.60` | 1,210,000.00 USD | 1,210,000.00 USD | 166,650.00 USD | 0.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.60` | 8,340,000.00 USD | 8,340,000.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4120.80` | 1,500,000.00 USD | 1,500,000.00 USD | 275,140.00 USD | 0.00 USD | 14,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.90` | 9,060,000.00 USD | 9,060,000.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4125.00` | 1,650,000.00 USD | 1,650,000.00 USD | 108,590.00 USD | 0.00 USD | 47,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.20` | 9,310,000.00 USD | 9,310,000.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4129.20` | 1,700,000.00 USD | 1,700,000.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4131.50` | 9,510,000.00 USD | 9,510,000.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4133.40` | 1,800,000.00 USD | 1,800,000.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.80` | 9,740,000.00 USD | 9,740,000.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4137.60` | 1,950,000.00 USD | 1,950,000.00 USD | 140,890.00 USD | 0.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.10` | 10,000,000.00 USD | 10,000,000.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4141.80` | 2,030,000.00 USD | 2,030,000.00 USD | 65,150.00 USD | 0.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.40` | 10,160,000.00 USD | 10,160,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4146.00` | 2,100,000.00 USD | 2,100,000.00 USD | 60,190.00 USD | 0.00 USD | 3,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.70` | 10,260,000.00 USD | 10,260,000.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4150.20` | 2,140,000.00 USD | 2,140,000.00 USD | 36,760.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.00` | 10,350,000.00 USD | 10,350,000.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4154.40` | 2,170,000.00 USD | 2,170,000.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,730,000.00 USD | 10,730,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4158.60` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.60` | 11,160,000.00 USD | 11,160,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4162.80` | 2,200,000.00 USD | 2,200,000.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.90` | 11,610,000.00 USD | 11,610,000.00 USD | 378,790.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4170.20` | 12,050,000.00 USD | 12,050,000.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.50` | 12,290,000.00 USD | 12,290,000.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4175.40` | 2,230,000.00 USD | 2,230,000.00 USD | 27,940.00 USD | 0.00 USD | 5,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.80` | 12,640,000.00 USD | 12,640,000.00 USD | 334,860.00 USD | 0.00 USD | 13,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4179.60` | 2,300,000.00 USD | 2,300,000.00 USD | 66,150.00 USD | 0.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4183.10` | 12,810,000.00 USD | 12,810,000.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4183.80` | 2,380,000.00 USD | 2,380,000.00 USD | 72,440.00 USD | 0.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4187.40` | 13,180,000.00 USD | 13,180,000.00 USD | 314,740.00 USD | 0.00 USD | 53,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.00` | 2,520,000.00 USD | 2,520,000.00 USD | 122,010.00 USD | 0.00 USD | 18,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.70` | 13,820,000.00 USD | 13,820,000.00 USD | 594,660.00 USD | 0.00 USD | 45,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.20` | 2,690,000.00 USD | 2,690,000.00 USD | 152,180.00 USD | 0.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4196.00` | 14,160,000.00 USD | 14,160,000.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4196.40` | 2,790,000.00 USD | 2,790,000.00 USD | 86,670.00 USD | 0.00 USD | 15,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4200.30` | 14,670,000.00 USD | 14,670,000.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4200.60` | 2,900,000.00 USD | 2,900,000.00 USD | 105,540.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.60` | 14,920,000.00 USD | 14,920,000.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4204.80` | 3,010,000.00 USD | 3,010,000.00 USD | 87,970.00 USD | 0.00 USD | 22,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.90` | 15,050,000.00 USD | 15,050,000.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4209.00` | 3,040,000.00 USD | 3,040,000.00 USD | 22,630.00 USD | 0.00 USD | 10,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4213.20` | 3,070,000.00 USD | 3,070,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4213.20` | 15,160,000.00 USD | 15,160,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.40` | 3,140,000.00 USD | 3,140,000.00 USD | 60,540.00 USD | 0.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4217.50` | 15,280,000.00 USD | 15,280,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4221.60` | 3,200,000.00 USD | 3,200,000.00 USD | 59,220.00 USD | 0.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.80` | 15,380,000.00 USD | 15,380,000.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4225.80` | 3,220,000.00 USD | 3,220,000.00 USD | 11,300.00 USD | 0.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4226.10` | 15,470,000.00 USD | 15,470,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4230.00` | 3,260,000.00 USD | 3,260,000.00 USD | 33,610.00 USD | 0.00 USD | 3,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4230.40` | 15,520,000.00 USD | 15,520,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4234.20` | 3,280,000.00 USD | 3,280,000.00 USD | 20,800.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.70` | 15,560,000.00 USD | 15,560,000.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4239.00` | 15,580,000.00 USD | 15,580,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4242.60` | 3,290,000.00 USD | 3,290,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4389.50` | 15,580,000.00 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4398.10` | 15,720,000.00 USD | 15,720,000.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4402.40` | 15,850,000.00 USD | 15,850,000.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.70` | 16,000,000.00 USD | 16,000,000.00 USD | 124,220.00 USD | 0.00 USD | 19,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.00` | 16,120,000.00 USD | 16,120,000.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4414.80` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4415.30` | 16,180,000.00 USD | 16,180,000.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4419.00` | 3,320,000.00 USD | 3,320,000.00 USD | 28,900.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.60` | 16,290,000.00 USD | 16,290,000.00 USD | 106,130.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4423.20` | 3,340,000.00 USD | 3,340,000.00 USD | 16,900.00 USD | 0.00 USD | 2,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.90` | 16,330,000.00 USD | 16,330,000.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4427.40` | 3,380,000.00 USD | 3,380,000.00 USD | 37,230.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4428.20` | 16,420,000.00 USD | 16,420,000.00 USD | 74,340.00 USD | 0.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4429.70` | 3,390,000.00 USD | 3,390,000.00 USD | 7,560.00 USD | 0.00 USD | 4,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4432.50` | 16,590,000.00 USD | 16,590,000.00 USD | 152,220.00 USD | 0.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4436.80` | 16,700,000.00 USD | 16,700,000.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4441.10` | 16,830,000.00 USD | 16,830,000.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4445.40` | 16,910,000.00 USD | 16,910,000.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4448.40` | 16,950,000.00 USD | 16,950,000.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.20` | 16,640,000.00 USD | 0.00 USD | 16,640,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `3612.60` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 2,900.00 USD | 0.00 USD | 1,530.00 USD |
| `7D` | `3615.50` | 16,560,000.00 USD | 0.00 USD | 16,560,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3616.80` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 29,730.00 USD | 0.00 USD | 2,100.00 USD |
| `7D` | `3619.80` | 16,420,000.00 USD | 0.00 USD | 16,420,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3621.00` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 27,050.00 USD | 0.00 USD | 2,070.00 USD |
| `7D` | `3624.10` | 16,360,000.00 USD | 0.00 USD | 16,360,000.00 USD | 95,230.00 USD | 0.00 USD | 21,190.00 USD |
| `1D` | `3625.20` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 45,730.00 USD | 0.00 USD | 7,790.00 USD |
| `7D` | `3628.40` | 16,240,000.00 USD | 0.00 USD | 16,240,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD |
| `1D` | `3629.40` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 32,220.00 USD | 0.00 USD | 6,260.00 USD |
| `7D` | `3632.70` | 16,050,000.00 USD | 0.00 USD | 16,050,000.00 USD | 112,500.00 USD | 0.00 USD | 13,730.00 USD |
| `1D` | `3633.60` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 24,570.00 USD | 0.00 USD | 3,680.00 USD |
| `7D` | `3637.00` | 15,920,000.00 USD | 0.00 USD | 15,920,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD |
| `1D` | `3637.80` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 45,970.00 USD | 0.00 USD | 6,310.00 USD |
| `7D` | `3641.30` | 15,790,000.00 USD | 0.00 USD | 15,790,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD |
| `1D` | `3642.00` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 10,510.00 USD | 0.00 USD | 4,910.00 USD |
| `7D` | `3645.60` | 15,730,000.00 USD | 0.00 USD | 15,730,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `3646.20` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 8,210.00 USD | 0.00 USD | 3,310.00 USD |
| `7D` | `3649.90` | 15,690,000.00 USD | 0.00 USD | 15,690,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `3650.40` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 22,380.00 USD | 0.00 USD | 2,300.00 USD |
| `7D` | `3654.20` | 15,670,000.00 USD | 0.00 USD | 15,670,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `3654.60` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 11,860.00 USD | 0.00 USD | 3,340.00 USD |
| `7D` | `3658.50` | 15,610,000.00 USD | 0.00 USD | 15,610,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD |
| `1D` | `3658.80` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 8,050.00 USD | 0.00 USD | 759.64 USD |
| `7D` | `3662.80` | 15,600,000.00 USD | 0.00 USD | 15,600,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD |
| `1D` | `3663.00` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `3667.10` | 15,580,000.00 USD | 0.00 USD | 15,580,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3671.40` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD |
| `7D` | `3830.50` | 15,580,000.00 USD | 0.00 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3839.10` | 15,570,000.00 USD | 0.00 USD | 15,570,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `3843.40` | 15,150,000.00 USD | 0.00 USD | 15,150,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD |
| `7D` | `3847.70` | 14,630,000.00 USD | 0.00 USD | 14,630,000.00 USD | 497,700.00 USD | 0.00 USD | 59,220.00 USD |
| `1D` | `3852.00` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 2,810.00 USD | 0.00 USD | 752.34 USD |
| `7D` | `3852.00` | 14,070,000.00 USD | 0.00 USD | 14,070,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD |
| `1D` | `3856.20` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 76,990.00 USD | 0.00 USD | 6,160.00 USD |
| `7D` | `3856.30` | 13,790,000.00 USD | 0.00 USD | 13,790,000.00 USD | 402,740.00 USD | 0.00 USD | 23,990.00 USD |
| `1D` | `3860.40` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 55,360.00 USD | 0.00 USD | 6,850.00 USD |
| `7D` | `3860.60` | 13,360,000.00 USD | 0.00 USD | 13,360,000.00 USD | 167,120.00 USD | 0.00 USD | 20,440.00 USD |
| `1D` | `3864.60` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 150,790.00 USD | 0.00 USD | 14,900.00 USD |
| `7D` | `3864.90` | 13,170,000.00 USD | 0.00 USD | 13,170,000.00 USD | 312,440.00 USD | 0.00 USD | 59,280.00 USD |
| `1D` | `3868.80` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 104,280.00 USD | 0.00 USD | 20,070.00 USD |
| `7D` | `3869.20` | 12,800,000.00 USD | 0.00 USD | 12,800,000.00 USD | 609,640.00 USD | 0.00 USD | 39,700.00 USD |
| `1D` | `3873.00` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 126,290.00 USD | 0.00 USD | 18,930.00 USD |
| `7D` | `3873.50` | 12,150,000.00 USD | 0.00 USD | 12,150,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD |
| `1D` | `3877.20` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 99,080.00 USD | 0.00 USD | 4,780.00 USD |
| `7D` | `3877.80` | 11,770,000.00 USD | 0.00 USD | 11,770,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD |
| `1D` | `3881.40` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 105,320.00 USD | 0.00 USD | 22,610.00 USD |
| `7D` | `3882.10` | 11,190,000.00 USD | 0.00 USD | 11,190,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD |
| `1D` | `3885.60` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 22,630.00 USD | 0.00 USD | 12,350.00 USD |
| `7D` | `3886.40` | 10,970,000.00 USD | 0.00 USD | 10,970,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD |
| `1D` | `3889.80` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 26,200.00 USD | 0.00 USD | 8,930.00 USD |
| `7D` | `3890.70` | 10,880,000.00 USD | 0.00 USD | 10,880,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD |
| `1D` | `3894.00` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 82,900.00 USD | 0.00 USD | 5,450.00 USD |
| `7D` | `3895.00` | 10,750,000.00 USD | 0.00 USD | 10,750,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD |
| `1D` | `3898.20` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 32,580.00 USD | 0.00 USD | 9,310.00 USD |
| `7D` | `3899.30` | 10,620,000.00 USD | 0.00 USD | 10,620,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `3902.40` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 38,100.00 USD | 0.00 USD | 1,900.00 USD |
| `7D` | `3903.60` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `3906.60` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 26,240.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `3907.90` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3912.20` | 10,400,000.00 USD | 0.00 USD | 10,400,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD |
| `1D` | `3915.00` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `3916.50` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD |
| `7D` | `3920.80` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD |
| `7D` | `3925.10` | 9,230,000.00 USD | 0.00 USD | 9,230,000.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD |
| `7D` | `3929.40` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD |
| `7D` | `3933.70` | 7,080,000.00 USD | 0.00 USD | 7,080,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD |
| `1D` | `3936.00` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 130,690.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `3938.00` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 711,630.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `3940.20` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 94,110.00 USD | 0.00 USD | 11,080.00 USD |
| `7D` | `3942.30` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 375,470.00 USD | 0.00 USD | 56,660.00 USD |
| `1D` | `3944.40` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 268,200.00 USD | 0.00 USD | 16,100.00 USD |
| `7D` | `3946.60` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 650,970.00 USD | 0.00 USD | 137,820.00 USD |
| `1D` | `3948.60` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 227,310.00 USD | 0.00 USD | 48,490.00 USD |
| `7D` | `3950.90` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD |
| `1D` | `3952.80` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 283,970.00 USD | 0.00 USD | 38,080.00 USD |
| `7D` | `3955.20` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 779,760.00 USD | 0.00 USD | 66,110.00 USD |
| `1D` | `3957.00` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 171,150.00 USD | 0.00 USD | 16,410.00 USD |
| `7D` | `3959.50` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD |
| `1D` | `3961.20` | 876,740.00 USD | 0.00 USD | 876,740.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD |
| `7D` | `3963.80` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD |
| `1D` | `3965.40` | 585,780.00 USD | 0.00 USD | 585,780.00 USD | 61,120.00 USD | 0.00 USD | 27,900.00 USD |
| `7D` | `3968.10` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD |
| `1D` | `3969.60` | 496,760.00 USD | 0.00 USD | 496,760.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD |
| `7D` | `3972.40` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3973.80` | 478,380.00 USD | 0.00 USD | 478,380.00 USD | 156,290.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3978.00` | 315,480.00 USD | 0.00 USD | 315,480.00 USD | 124,280.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `3981.00` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3982.20` | 183,990.00 USD | 0.00 USD | 183,990.00 USD | 32,780.00 USD | 0.00 USD | 22,420.00 USD |
| `7D` | `3985.30` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD |
| `1D` | `3986.40` | 128,790.00 USD | 0.00 USD | 128,790.00 USD | 66,940.00 USD | 0.00 USD | 7,890.00 USD |
| `7D` | `3989.60` | 134,160.00 USD | 0.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD |
| `1D` | `3990.60` | 53,970.00 USD | 0.00 USD | 53,970.00 USD | 31,710.00 USD | 0.00 USD | 1,980.00 USD |
| `7D` | `3993.90` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3999.00` | 20,280.00 USD | 0.00 USD | 20,280.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD |
| `1D` | `4020.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4021.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 0.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 0.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD |
| `7D` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD |
| `7D` | `4088.50` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 986,980.00 USD | 0.00 USD | 122,030.00 USD |
| `7D` | `4092.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD |
| `1D` | `4095.60` | 91,610.00 USD | 91,610.00 USD | 0.00 USD | 78,740.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `4097.10` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 805,470.00 USD | 0.00 USD | 47,970.00 USD |
| `1D` | `4099.80` | 238,120.00 USD | 238,120.00 USD | 0.00 USD | 137,710.00 USD | 0.00 USD | 8,800.00 USD |
| `7D` | `4101.40` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 246,010.00 USD | 0.00 USD | 40,870.00 USD |
| `1D` | `4104.00` | 400,370.00 USD | 400,370.00 USD | 0.00 USD | 150,630.00 USD | 0.00 USD | 11,620.00 USD |
| `7D` | `4105.70` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 651,880.00 USD | 0.00 USD | 104,930.00 USD |
| `1D` | `4108.20` | 701,730.00 USD | 701,730.00 USD | 0.00 USD | 260,190.00 USD | 0.00 USD | 41,160.00 USD |
| `7D` | `4110.00` | 6,560,000.00 USD | 6,560,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 68,720.00 USD |
| `1D` | `4112.40` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 272,530.00 USD | 0.00 USD | 36,980.00 USD |
| `7D` | `4114.30` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD |
| `1D` | `4116.60` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 166,650.00 USD | 0.00 USD | 29,460.00 USD |
| `7D` | `4118.60` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD |
| `1D` | `4120.80` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 275,140.00 USD | 0.00 USD | 14,990.00 USD |
| `7D` | `4122.90` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD |
| `1D` | `4125.00` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 108,590.00 USD | 0.00 USD | 47,040.00 USD |
| `7D` | `4127.20` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD |
| `1D` | `4129.20` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD |
| `7D` | `4131.50` | 9,510,000.00 USD | 9,510,000.00 USD | 0.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4133.40` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `4135.80` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD |
| `1D` | `4137.60` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 140,890.00 USD | 0.00 USD | 10,150.00 USD |
| `7D` | `4140.10` | 10,000,000.00 USD | 10,000,000.00 USD | 0.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `4141.80` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 65,150.00 USD | 0.00 USD | 18,620.00 USD |
| `7D` | `4144.40` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4146.00` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 60,190.00 USD | 0.00 USD | 3,800.00 USD |
| `7D` | `4148.70` | 10,260,000.00 USD | 10,260,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD |
| `1D` | `4150.20` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 36,760.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `4153.00` | 10,350,000.00 USD | 10,350,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD |
| `1D` | `4154.40` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4157.30` | 10,730,000.00 USD | 10,730,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `1D` | `4158.60` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4161.60` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `1D` | `4162.80` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4165.90` | 11,610,000.00 USD | 11,610,000.00 USD | 0.00 USD | 378,790.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4170.20` | 12,050,000.00 USD | 12,050,000.00 USD | 0.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD |
| `7D` | `4174.50` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD |
| `1D` | `4175.40` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 27,940.00 USD | 0.00 USD | 5,940.00 USD |
| `7D` | `4178.80` | 12,640,000.00 USD | 12,640,000.00 USD | 0.00 USD | 334,860.00 USD | 0.00 USD | 13,490.00 USD |
| `1D` | `4179.60` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 66,150.00 USD | 0.00 USD | 4,190.00 USD |
| `7D` | `4183.10` | 12,810,000.00 USD | 12,810,000.00 USD | 0.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD |
| `1D` | `4183.80` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 72,440.00 USD | 0.00 USD | 5,150.00 USD |
| `7D` | `4187.40` | 13,180,000.00 USD | 13,180,000.00 USD | 0.00 USD | 314,740.00 USD | 0.00 USD | 53,390.00 USD |
| `1D` | `4188.00` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 122,010.00 USD | 0.00 USD | 18,670.00 USD |
| `7D` | `4191.70` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 594,660.00 USD | 0.00 USD | 45,200.00 USD |
| `1D` | `4192.20` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 152,180.00 USD | 0.00 USD | 19,450.00 USD |
| `7D` | `4196.00` | 14,160,000.00 USD | 14,160,000.00 USD | 0.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD |
| `1D` | `4196.40` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 86,670.00 USD | 0.00 USD | 15,950.00 USD |
| `7D` | `4200.30` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD |
| `1D` | `4200.60` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 105,540.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `4204.60` | 14,920,000.00 USD | 14,920,000.00 USD | 0.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD |
| `1D` | `4204.80` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 87,970.00 USD | 0.00 USD | 22,440.00 USD |
| `7D` | `4208.90` | 15,050,000.00 USD | 15,050,000.00 USD | 0.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD |
| `1D` | `4209.00` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 22,630.00 USD | 0.00 USD | 10,900.00 USD |
| `1D` | `4213.20` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `4213.20` | 15,160,000.00 USD | 15,160,000.00 USD | 0.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `4217.40` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 60,540.00 USD | 0.00 USD | 3,300.00 USD |
| `7D` | `4217.50` | 15,280,000.00 USD | 15,280,000.00 USD | 0.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `4221.60` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 59,220.00 USD | 0.00 USD | 3,600.00 USD |
| `7D` | `4221.80` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `4225.80` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 11,300.00 USD | 0.00 USD | 11,210.00 USD |
| `7D` | `4226.10` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `4230.00` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 33,610.00 USD | 0.00 USD | 3,120.00 USD |
| `7D` | `4230.40` | 15,520,000.00 USD | 15,520,000.00 USD | 0.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `1D` | `4234.20` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 20,800.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `4234.70` | 15,560,000.00 USD | 15,560,000.00 USD | 0.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4239.00` | 15,580,000.00 USD | 15,580,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4242.60` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `4389.50` | 15,580,000.00 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4398.10` | 15,720,000.00 USD | 15,720,000.00 USD | 0.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD |
| `7D` | `4402.40` | 15,850,000.00 USD | 15,850,000.00 USD | 0.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD |
| `7D` | `4406.70` | 16,000,000.00 USD | 16,000,000.00 USD | 0.00 USD | 124,220.00 USD | 0.00 USD | 19,700.00 USD |
| `7D` | `4411.00` | 16,120,000.00 USD | 16,120,000.00 USD | 0.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD |
| `1D` | `4414.80` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD |
| `7D` | `4415.30` | 16,180,000.00 USD | 16,180,000.00 USD | 0.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD |
| `1D` | `4419.00` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 28,900.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `4419.60` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 106,130.00 USD | 0.00 USD | 3,450.00 USD |
| `1D` | `4423.20` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 16,900.00 USD | 0.00 USD | 2,330.00 USD |
| `7D` | `4423.90` | 16,330,000.00 USD | 16,330,000.00 USD | 0.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD |
| `1D` | `4427.40` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 37,230.00 USD | 0.00 USD | 2,250.00 USD |
| `7D` | `4428.20` | 16,420,000.00 USD | 16,420,000.00 USD | 0.00 USD | 74,340.00 USD | 0.00 USD | 18,160.00 USD |
| `1D` | `4429.70` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 7,560.00 USD | 0.00 USD | 4,260.00 USD |
| `7D` | `4432.50` | 16,590,000.00 USD | 16,590,000.00 USD | 0.00 USD | 152,220.00 USD | 0.00 USD | 11,860.00 USD |
| `7D` | `4436.80` | 16,700,000.00 USD | 16,700,000.00 USD | 0.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD |
| `7D` | `4441.10` | 16,830,000.00 USD | 16,830,000.00 USD | 0.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD |
| `7D` | `4445.40` | 16,910,000.00 USD | 16,910,000.00 USD | 0.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `4448.40` | 16,950,000.00 USD | 16,950,000.00 USD | 0.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.57M` | Total OI Tokens: `68,298.1 PAXG`
  * 1h OI Change: `+0.18%` | 4h OI Change: `-0.22%` | 24h OI Change: `+0.24%`
  * Exchange Breakdown: Binance=`107.22M` | Bybit=`19.99M` | OKX=`-` | Hyperliquid=`25.08M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.36K` | Last 24h: `25.27K` | Last 3d: `95.73K` | Last 7d: `222.33K`
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
| `15M` | `PAXG` | `45.93%` | `54.07%` | `0.85` | 1,640,000.00 USD |
| `15M` | `Binance` | `57.99%` | `42.01%` | `1.38` | 541,160.00 USD |
| `15M` | `OKX` | `64.28%` | `35.72%` | `1.80` | 130,420.00 USD |
| `15M` | `Bybit` | `58.33%` | `41.67%` | `1.40` | 72,590.00 USD |
| `15M` | `KuCoin` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Gate` | `58.63%` | `41.37%` | `1.42` | 10,540.00 USD |
| `15M` | `Bitget` | `43.61%` | `56.39%` | `0.77` | 174,990.00 USD |
| `15M` | `BingX` | `7.74%` | `92.26%` | `0.08` | 388,400.00 USD |
| `15M` | `MEXC` | `48.6%` | `51.4%` | `0.95` | 137,020.00 USD |
| `15M` | `Bitunix` | `77.57%` | `22.43%` | `3.46` | 33,280.00 USD |
| `15M` | `Hyperliquid` | `38.56%` | `61.44%` | `0.63` | 9,280.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `52.71%` | `47.29%` | `1.11` | 24,980.00 USD |
| `15M` | `Crypto.com` | `0.47%` | `99.53%` | `0.00` | 498.88 USD |
| `15M` | `WhiteBIT` | `81.6%` | `18.4%` | `4.43` | 109,310.00 USD |
| `15M` | `HTX` | `48.12%` | `51.88%` | `0.93` | 216.86 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `19.82%` | `80.18%` | `0.25` | 2,390.00 USD |
| `15M` | `Aster` | `48.27%` | `51.73%` | `0.93` | 635.03 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `2.47%` | `97.53%` | `0.03` | 1,320.00 USD |
| `15M` | `Whale Positions` | `57.99%` | `42.01%` | `1.38` | 541,160.00 USD |
| `15M` | `Global Accounts` | `45.93%` | `54.07%` | `0.85` | 1,640,000.00 USD |
| `1H` | `PAXG` | `60.10%` | `39.90%` | `1.51` | 8,770,000.00 USD |
| `1H` | `Binance` | `56.94%` | `43.06%` | `1.32` | 3,010,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 1,300,000.00 USD |
| `1H` | `Bybit` | `47.91%` | `52.09%` | `0.92` | 675,160.00 USD |
| `1H` | `KuCoin` | `14.55%` | `85.45%` | `0.17` | 53,500.00 USD |
| `1H` | `Gate` | `60.58%` | `39.42%` | `1.54` | 416,450.00 USD |
| `1H` | `Bitget` | `58.01%` | `41.99%` | `1.38` | 492,900.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 799,880.00 USD |
| `1H` | `MEXC` | `64.58%` | `35.42%` | `1.82` | 931,580.00 USD |
| `1H` | `Bitunix` | `75.76%` | `24.24%` | `3.13` | 128,760.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 105,140.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `55.14%` | `44.86%` | `1.23` | 450,680.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 4,700.00 USD |
| `1H` | `WhiteBIT` | `20.06%` | `79.94%` | `0.25` | 338,640.00 USD |
| `1H` | `HTX` | `36.78%` | `63.22%` | `0.58` | 612.15 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `30.78%` | `69.22%` | `0.44` | 8,580.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 2,630.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 39,330.00 USD |
| `1H` | `Whale Positions` | `56.94%` | `43.06%` | `1.32` | 3,010,000.00 USD |
| `1H` | `Global Accounts` | `60.10%` | `39.90%` | `1.51` | 8,770,000.00 USD |
| `4H` | `PAXG` | `52.39%` | `47.61%` | `1.10` | 53,160,000.00 USD |
| `4H` | `Binance` | `54.23%` | `45.77%` | `1.18` | 4,610,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `51.27%` | `48.73%` | `1.05` | 4,930,000.00 USD |
| `4H` | `KuCoin` | `55.18%` | `44.82%` | `1.23` | 323,510.00 USD |
| `4H` | `Gate` | `53.52%` | `46.48%` | `1.15` | 1,740,000.00 USD |
| `4H` | `Bitget` | `45.8%` | `54.2%` | `0.85` | 1,810,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `54.03%` | `45.97%` | `1.18` | 32,300,000.00 USD |
| `4H` | `Bitunix` | `60.99%` | `39.01%` | `1.56` | 1,670,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.19%` | `49.81%` | `1.01` | 4,200,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `12.87%` | `87.13%` | `0.15` | 1,370,000.00 USD |
| `4H` | `HTX` | `93.57%` | `6.43%` | `14.55` | 71,810.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.83%` | `54.17%` | `0.85` | 122,280.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `54.23%` | `45.77%` | `1.18` | 4,610,000.00 USD |
| `4H` | `Global Accounts` | `52.39%` | `47.61%` | `1.10` | 53,160,000.00 USD |


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
| `5m` | 4,800.00 USD | 43,280.00 USD | **`ACCUMULATION`** |
| `15m` | 7,530.00 USD | -212,020.00 USD | **`DISTRIBUTION`** |
| `30m` | -168,690.00 USD | -651,390.00 USD | **`DISTRIBUTION`** |
| `1h` | -290,000.00 USD | -228,920.00 USD | **`DISTRIBUTION`** |
| `2h` | -584,100.00 USD | 16,030.00 USD | **`DISTRIBUTION`** |
| `4h` | 210,110.00 USD | 1,010,000.00 USD | **`ACCUMULATION`** |
| `6h` | 21,050.00 USD | 630,070.00 USD | **`ACCUMULATION`** |
| `8h` | -231,420.00 USD | 1,350,000.00 USD | **`ACCUMULATION`** |
| `12h` | -310,900.00 USD | 896,130.00 USD | **`ACCUMULATION`** |
| `24h` | -443,940.00 USD | 1,090,000.00 USD | **`ACCUMULATION`** |
| `1w` | -8,490,000.00 USD | -7,590,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,550,000.00 USD | -71,960,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+4.80K` | 15m=`+7.53K` | 1h=`-290.00K` | 24h=`-443.94K`
* Futures Capital Netflows: 5m=`+43.28K` | 15m=`-212.02K` | 1h=`-228.92K` | 24h=`+1.09M`
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
  * `2026-10-30 00:57:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:47:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:16:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `4004.94` (Risk Distance: `12.16` pts)
  * +2.5R Take Profit: `4047.49`
  * Mathematical Lot Sizing: **`0.82 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4041.38` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4053.54` (Risk Distance: `12.16` pts)
  * +2.5R Take Profit: `4010.99`
  * Mathematical Lot Sizing: **`0.82 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4044.73`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
