# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 17:28:17 IST` (`2026-10-30 11:58:17 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3967.56` | **Live Ask Quote**: `3967.72` | **Mid Price**: `3967.64`
- **Spread Points**: `16.00` | **Spread BPS**: `0.40 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `3994.23` | VWAP Z-Score: `-2.11` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `7.69` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `33.44` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4026.99` | Lower -3.00σ Band: `3961.47`
  * Upper +2.51σ Band: `4021.64` | Lower -2.51σ Band: `3966.82`
  * Upper +2.01σ Band: `4016.18` | Lower -2.01σ Band: `3972.28`
  * Upper +2.00σ Band: `4016.07` | Lower -2.00σ Band: `3972.39`
  * Upper +1.28σ Band: `4008.21` | Lower -1.28σ Band: `3980.25`
  * Upper +1.00σ Band: `4005.15` | Lower -1.00σ Band: `3983.31`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3979.04` | EMA-20=`3983.82` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`3993.31` (Slope: `+0.0000`) | EMA-100=`4004.87`
  * Institutional Anchors: EMA-144=`4011.51` | EMA-200=`4017.36` (Slope: `-0.1073`) | EMA-233=`4020.90`
- **Range Boundaries**: 24H High=`4039.31` | 24H Low=`3965.22` | Weekly High=`4082.75` | Weekly Low=`3965.22`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4007.93` (Distance: `-1.01%`)
  * Point of Control (POC) = `3990.50` (Distance: `-0.58%`)
  * Value Area Low (VAL) = `3979.46` (Distance: `-0.30%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4054.15` | Weekly POC=`4017.32` | Weekly VAL=`4004.00`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4011.55` | Low=`3965.22`
  * New York Session (13:00-21:00 UTC): High=`3991.98` | Low=`3966.28`
  * Initial Balance (First Hour): IB High=`4011.55` | IB Low=`3988.18`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3951.77` - `3983.51`
  * Optimal Trade Entry (OTE 0.705): `3975.58`
  * Structural Invalidation Anchor (0.786): `3999.38`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `3980.35` | `3981.31` | `3975.82` | `3976.28` | `78` | 308,435.05 USD | -62,138.30 USD | `-20.15%` | 224,196.66 USD | `-0.51` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `3976.27` | `3976.68` | `3972.24` | `3973.62` | `145` | 578,000.32 USD | -26,919.36 USD | `-4.66%` | 197,277.30 USD | `-0.27` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `3973.63` | `3974.72` | `3973.24` | `3973.65` | `38` | 151,747.39 USD | 7,742.45 USD | `+5.10%` | 205,019.75 USD | `-0.14` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `3984.30` | `3984.30` | `3975.14` | `3981.73` | `398` | 1,585,134.07 USD | 105,026.29 USD | `+6.63%` | 80,870.80 USD | `+0.65` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `3981.74` | `3985.11` | `3975.82` | `3976.28` | `300` | 1,196,019.00 USD | 201,491.06 USD | `+16.85%` | 282,361.87 USD | `+0.95` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `3976.27` | `3976.68` | `3972.24` | `3973.65` | `184` | 729,767.58 USD | -19,157.05 USD | `-2.63%` | 263,204.82 USD | `-0.03` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4001.22` | `4002.41` | `3991.51` | `3995.66` | `459` | 1,835,738.77 USD | 110,152.21 USD | `+6.00%` | 73,019.48 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `3995.66` | `3995.82` | `3981.27` | `3985.58` | `724` | 2,887,727.74 USD | -259,947.31 USD | `-9.00%` | -186,927.83 USD | `-0.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `3985.59` | `3987.59` | `3972.24` | `3973.65` | `1,194` | 4,751,192.95 USD | 450,132.65 USD | `+9.47%` | 263,204.82 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3972.24` | `3973.65` | `3,918` | 15,625,495.34 USD | 842,171.05 USD | `+5.39%` | 263,204.82 USD | `+0.92` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,524,929.80 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,542,786.16 USD | `-1.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3972.24` | `3973.65` | `3,918` | 15,625,495.34 USD | 842,171.05 USD | `+5.39%` | 263,204.82 USD | `+0.92` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `3968.20` | `1.2292` | 4,877.71 USD | 1,027,000.11 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `3968.30` | `62.8329` | 249,339.80 USD | 1,022,122.39 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `3968.40` | `8.2569` | 32,766.68 USD | 772,782.60 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3968.50` | `5.9712` | 23,696.71 USD | 740,015.91 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `3968.70` | `11.9213` | 47,312.06 USD | 716,319.21 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `3968.80` | `10.7169` | 42,533.23 USD | 669,007.14 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `3968.90` | `10.5435` | 41,846.10 USD | 626,473.91 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3969.00` | `64.0611` | 254,258.51 USD | 584,627.81 USD | `10 orders` | `-0.03%` | `-` |
| `BID` | `3969.10` | `9.9074` | 39,323.46 USD | 330,369.31 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `3969.20` | `14.5678` | 57,822.51 USD | 291,045.85 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `3969.40` | `2.6009` | 10,324.01 USD | 233,223.34 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3969.50` | `7.5576` | 29,999.89 USD | 222,899.32 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3969.60` | `8.3311` | 33,071.13 USD | 192,899.43 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3969.70` | `3.0212` | 11,993.26 USD | 159,828.30 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3969.80` | `0.3778` | 1,499.79 USD | 147,835.04 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3969.90` | `5.1167` | 20,312.79 USD | 146,335.25 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `3970.00` | `4.7855` | 18,998.43 USD | 126,022.46 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `3970.10` | `2.6755` | 10,622.00 USD | 107,024.02 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3970.20` | `16.2629` | 64,566.97 USD | 96,402.02 USD | `5 orders` | `-0.00%` | `-` |
| `BID` | `3970.30` | `8.0183` | 31,835.06 USD | 31,835.06 USD | `4 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `3970.35` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 3,970.35` | `0.00%` | `-` |
| `ASK` | `3970.40` | `14.3508` | 56,978.42 USD | 56,978.42 USD | `10 orders` | `+0.00%` | `-` |
| `ASK` | `3970.50` | `4.8319` | 19,185.06 USD | 76,163.48 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `3970.60` | `11.3340` | 45,002.78 USD | 121,166.26 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `3970.70` | `32.4301` | 128,770.20 USD | 249,936.45 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `3970.80` | `12.6473` | 50,219.90 USD | 300,156.35 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `3970.90` | `59.4408` | 236,033.47 USD | 536,189.83 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `3971.00` | `25.4632` | 101,114.37 USD | 637,304.19 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `3971.10` | `10.6433` | 42,265.61 USD | 679,569.80 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `3971.20` | `16.9202` | 67,193.50 USD | 746,763.30 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `3971.30` | `58.6182` | 232,790.46 USD | 979,553.76 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `3971.40` | `3.7772` | 15,000.77 USD | 994,554.53 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `3971.50` | `10.0120` | 39,762.66 USD | 1,034,317.19 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `3971.60` | `11.7541` | 46,682.58 USD | 1,080,999.77 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `3971.70` | `9.1605` | 36,382.76 USD | 1,117,382.53 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `3971.80` | `15.1964` | 60,357.06 USD | 1,177,739.59 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `3971.90` | `95.0624` | 377,578.35 USD | 1,555,317.94 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `3972.00` | `8.9147` | 35,409.19 USD | 1,590,727.12 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3972.10` | `49.7604` | 197,653.28 USD | 1,788,380.41 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `3972.20` | `28.5012` | 113,212.47 USD | 1,901,592.88 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `3972.30` | `12.4143` | 49,313.32 USD | 1,950,906.20 USD | `2 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 17:23:48 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `47` | `0x5b5d...c060` | `SHORT` | 25,765,899.24 USD | `6,489.82` | `4185.46` | `3969.50` | `28007.30` | 1,397,051.77 USD | `+5.42%` | `4X Cross` |
| `49` | `0x4692...164f` | `SHORT` | 25,057,149.27 USD | `6,311.62` | `4126.90` | `3969.50` | `14313.47` | 990,350.62 USD | `+3.95%` | `5X Cross` |
| `61` | `0xb83d...6e36` | `SHORT` | 23,305,848.58 USD | `5,869.90` | `4228.86` | `3969.50` | `22965.01` | 1,517,173.36 USD | `+6.51%` | `5X Cross` |
| `98` | `0xec0b...b078` | `LONG` | 19,172,691.96 USD | `4,828.91` | `4157.43` | `3969.50` | `2279.52` | -903,190.36 USD | `-4.71%` | `25X Cross` |
| `143` | `0x645b...87b8` | `LONG` | 14,077,181.02 USD | `3,545.71` | `4127.81` | `3969.50` | `691.07` | -558,868.15 USD | `-3.97%` | `3X Cross` |
| `156` | `0x7a6d...f79c` | `SHORT` | 12,975,460.05 USD | `3,268.21` | `4228.94` | `3969.50` | `4386.74` | 845,619.08 USD | `+6.52%` | `25X Cross` |
| `181` | `0xa742...e390` | `SHORT` | 11,116,648.14 USD | `2,800.02` | `4364.62` | `3969.50` | `4212.90` | 1,104,396.00 USD | `+9.93%` | `20X Cross` |
| `263` | `0x41e5...0825` | `SHORT` | 8,734,880.00 USD | `2,200.00` | `4112.20` | `3969.50` | `4287.25` | 311,974.59 USD | `+3.57%` | `20X Cross` |
| `264` | `0x3678...b209` | `LONG` | 8,734,660.00 USD | `2,200.00` | `4176.09` | `3969.50` | `2691.17` | -452,759.30 USD | `-5.18%` | `25X Cross` |
| `303` | `0xacb6...efbd` | `SHORT` | 7,843,005.47 USD | `1,975.37` | `4048.55` | `3969.50` | `6724.01` | 154,386.24 USD | `+1.97%` | `6X Cross` |
| `364` | `0xc26c...b8f4` | `LONG` | 6,272,724.64 USD | `1,579.95` | `4075.62` | `3969.50` | `0.000000` | -166,572.33 USD | `-2.66%` | `1X Cross` |
| `560` | `0x63da...8add` | `LONG` | 3,970,200.00 USD | `1,000.00` | `4021.46` | `3969.50` | `3564.79` | -51,260.96 USD | `-1.29%` | `25X Cross` |
| `571` | `0xf3dc...1672` | `LONG` | 3,907,357.82 USD | `984.27` | `4018.39` | `3969.50` | `2802.25` | -47,828.87 USD | `-1.22%` | `20X Cross` |
| `600` | `0x9aa5...58af` | `LONG` | 3,757,129.79 USD | `946.38` | `4279.98` | `3969.50` | `0.000000` | -293,359.70 USD | `-7.81%` | `20X Cross` |
| `675` | `0x4a20...3c26` | `LONG` | 3,324,728.03 USD | `837.40` | `4599.73` | `3969.50` | `0.000000` | -527,092.35 USD | `-15.85%` | `20X Cross` |
| `768` | `0x9c06...0560` | `LONG` | 2,976,355.32 USD | `749.67` | `4001.53` | `3969.50` | `0.000000` | -23,494.28 USD | `-0.79%` | `25X Cross` |
| `830` | `0x0fac...7a0a` | `LONG` | 2,725,482.75 USD | `686.49` | `4290.34` | `3969.50` | `1399.94` | -219,775.96 USD | `-8.06%` | `25X Cross` |
| `875` | `0x354b...6425` | `LONG` | 2,545,812.52 USD | `641.26` | `4003.27` | `3969.50` | `0.000000` | -21,336.35 USD | `-0.84%` | `10X Cross` |
| `896` | `0x625e...a354` | `SHORT` | 2,461,648.00 USD | `620.00` | `4122.81` | `3969.50` | `4279.66` | 94,499.03 USD | `+3.84%` | `20X Cross` |
| `928` | `0xeae3...e8ad` | `SHORT` | 2,382,180.00 USD | `600.00` | `4104.77` | `3969.50` | `4268.74` | 80,685.11 USD | `+3.39%` | `20X Cross` |
| `930` | `0xf285...fa82` | `LONG` | 2,374,600.04 USD | `598.11` | `4146.45` | `3969.50` | `3891.93` | -105,419.51 USD | `-4.44%` | `25X Cross` |
| `935` | `0xd8c5...99b0` | `SHORT` | 2,359,767.26 USD | `594.35` | `4175.35` | `3969.50` | `35496.21` | 121,876.77 USD | `+5.16%` | `4X Cross` |
| `943` | `0x12f7...8750` | `LONG` | 2,324,991.60 USD | `585.61` | `4082.77` | `3969.50` | `2838.26` | -65,925.38 USD | `-2.84%` | `10X Cross` |
| `994` | `0x413c...886c` | `LONG` | 2,221,321.28 USD | `559.47` | `4007.05` | `3969.50` | `0.000000` | -20,505.93 USD | `-0.92%` | `2X Cross` |
| `1096` | `0x61ce...a62b` | `SHORT` | 1,975,238.15 USD | `497.50` | `4071.66` | `3969.50` | `4721.68` | 50,430.65 USD | `+2.55%` | `20X Cross` |
| `1208` | `0x2edd...8179` | `LONG` | 1,825,136.30 USD | `459.30` | `4164.68` | `3973.00` | `0.000000` | -87,717.25 USD | `-4.81%` | `10X Cross` |
| `1219` | `0xead5...69f2` | `LONG` | 1,801,703.60 USD | `453.78` | `4220.88` | `3969.50` | `3539.63` | -113,664.46 USD | `-6.31%` | `5X Isolated` |
| `1275` | `0x7a6d...f79c` | `SHORT` | 1,702,078.28 USD | `428.38` | `4136.09` | `3973.00` | `5368.29` | 69,736.73 USD | `+4.10%` | `10X Cross` |
| `1295` | `0x46fc...1195` | `LONG` | 1,669,597.05 USD | `420.57` | `4050.13` | `3969.50` | `2306.05` | -33,786.78 USD | `-2.02%` | `20X Cross` |
| `1350` | `0x6d15...d374` | `LONG` | 1,588,160.00 USD | `400.00` | `4068.25` | `3969.50` | `3842.50` | -39,140.00 USD | `-2.46%` | `25X Cross` |
| `1352` | `0xee02...309d` | `SHORT` | 1,588,080.00 USD | `400.00` | `4438.84` | `3969.50` | `4203.04` | 187,458.60 USD | `+11.80%` | `25X Isolated` |
| `1381` | `0x51f6...2b39` | `LONG` | 1,555,506.63 USD | `391.48` | `4228.25` | `3973.00` | `535.53` | -99,769.06 USD | `-6.41%` | `10X Cross` |
| `1384` | `0x02a7...fe9f` | `SHORT` | 1,548,378.00 USD | `390.00` | `4055.02` | `3969.50` | `4307.36` | 33,081.25 USD | `+2.14%` | `25X Cross` |
| `1433` | `0x7e77...b8d2` | `SHORT` | 1,508,752.00 USD | `380.00` | `4131.92` | `3969.50` | `4294.17` | 61,377.64 USD | `+4.07%` | `20X Cross` |
| `1457` | `0x72c2...9b37` | `LONG` | 1,481,443.20 USD | `373.13` | `4000.98` | `3969.50` | `3778.73` | -11,450.32 USD | `-0.77%` | `13X Isolated` |
| `1473` | `0x781e...96b7` | `SHORT` | 1,456,625.50 USD | `366.58` | `4357.94` | `3973.00` | `12884.62` | 140,931.56 USD | `+9.68%` | `10X Cross` |
| `1505` | `0xaa44...b844` | `LONG` | 1,429,128.00 USD | `360.00` | `4043.10` | `3969.50` | `3225.94` | -26,389.63 USD | `-1.85%` | `7X Cross` |
| `1616` | `0xa41f...d50a` | `LONG` | 1,306,111.12 USD | `328.96` | `4468.89` | `3969.50` | `3802.85` | -163,986.73 USD | `-12.56%` | `15X Cross` |
| `1670` | `0xbf5a...88ba` | `SHORT` | 1,261,153.48 USD | `317.65` | `4091.80` | `3969.50` | `9930.77` | 38,629.55 USD | `+3.06%` | `20X Cross` |
| `1701` | `0xff31...ff6c` | `SHORT` | 1,230,793.00 USD | `310.00` | `4372.43` | `3969.50` | `4789.84` | 124,662.38 USD | `+10.13%` | `10X Isolated` |
| `1732` | `0xada6...6f88` | `LONG` | 1,204,670.97 USD | `303.47` | `4166.46` | `3969.50` | `1818.13` | -59,711.49 USD | `-4.96%` | `5X Cross` |
| `1885` | `0x50e2...d770` | `LONG` | 1,073,439.69 USD | `270.37` | `4243.58` | `3969.50` | `2562.78` | -73,886.77 USD | `-6.88%` | `20X Cross` |
| `1902` | `0x4c92...4f17` | `SHORT` | 1,058,933.73 USD | `266.72` | `4260.98` | `3969.50` | `6482.98` | 77,558.51 USD | `+7.32%` | `20X Cross` |
| `1978` | `0xd346...c4f3` | `LONG` | 1,013,091.02 USD | `255.17` | `4188.66` | `3969.50` | `3311.11` | -55,745.49 USD | `-5.50%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4089.00` | 1,227.52 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 1.23K USD at 4089.0000 USD [API] | `2026-10-07 12:28:33` |
| `ANNOUNCEMENT` | `INFO` | `4089.00` | 12,789.57 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 12.79K USD at 4089.0000 USD [API | `2026-10-07 12:28:33` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4096.30` (Vol: 350,100.00 USD, Dist: `+2.84%`) | Long MP=`3937.38` (Vol: 356,200.00 USD, Dist: `--1.15%`)
  * 48H Horizon: Short MP=`4111.27` (Vol: 328,300.00 USD, Dist: `+3.22%`) | Long MP=`3936.60` (Vol: 378,100.00 USD, Dist: `--1.17%`)
  * 3D Horizon: Short MP=`4111.27` (Vol: 367,600.00 USD, Dist: `+3.22%`) | Long MP=`3949.08` (Vol: 404,600.00 USD, Dist: `--0.85%`)
  * 7D Horizon: Short MP=`4086.31` (Vol: 853,900.00 USD, Dist: `+2.59%`) | Long MP=`3927.24` (Vol: 1,100,000.00 USD, Dist: `--1.40%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `Long Liquidation` | `3579.70` | 5,920,000.00 USD | 5,920,000.00 USD | 8,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3583.90` | 5,910,000.00 USD | 5,910,000.00 USD | 1,960.00 USD | 0.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3584.80` | 14,790,000.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3588.10` | 5,890,000.00 USD | 5,890,000.00 USD | 10,740.00 USD | 0.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3589.10` | 14,780,000.00 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3592.30` | 5,870,000.00 USD | 5,870,000.00 USD | 7,110.00 USD | 0.00 USD | 21,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3593.40` | 14,760,000.00 USD | 14,760,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3596.50` | 5,840,000.00 USD | 5,840,000.00 USD | 35,040.00 USD | 0.00 USD | 19,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3597.70` | 14,750,000.00 USD | 14,750,000.00 USD | 108,500.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3600.70` | 5,790,000.00 USD | 5,790,000.00 USD | 26,650.00 USD | 0.00 USD | 28,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3602.00` | 14,620,000.00 USD | 14,620,000.00 USD | 173,930.00 USD | 0.00 USD | 75,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3604.90` | 5,730,000.00 USD | 5,730,000.00 USD | 54,630.00 USD | 0.00 USD | 39,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3606.30` | 14,370,000.00 USD | 14,370,000.00 USD | 152,940.00 USD | 0.00 USD | 43,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3609.10` | 5,640,000.00 USD | 5,640,000.00 USD | 14,040.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3610.60` | 14,170,000.00 USD | 14,170,000.00 USD | 72,480.00 USD | 0.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3613.30` | 5,620,000.00 USD | 5,620,000.00 USD | 33,240.00 USD | 0.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3614.90` | 14,080,000.00 USD | 14,080,000.00 USD | 76,990.00 USD | 0.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3617.50` | 5,570,000.00 USD | 5,570,000.00 USD | 41,740.00 USD | 0.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.20` | 13,990,000.00 USD | 13,990,000.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3621.70` | 5,530,000.00 USD | 5,530,000.00 USD | 37,530.00 USD | 0.00 USD | 10,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.50` | 13,930,000.00 USD | 13,930,000.00 USD | 45,130.00 USD | 0.00 USD | 22,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3625.90` | 5,480,000.00 USD | 5,480,000.00 USD | 51,070.00 USD | 0.00 USD | 7,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3627.80` | 13,860,000.00 USD | 13,860,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3630.10` | 5,420,000.00 USD | 5,420,000.00 USD | 19,470.00 USD | 0.00 USD | 2,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.10` | 13,760,000.00 USD | 13,760,000.00 USD | 60,720.00 USD | 0.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3634.30` | 5,400,000.00 USD | 5,400,000.00 USD | 2,050.00 USD | 0.00 USD | 594.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.40` | 13,690,000.00 USD | 13,690,000.00 USD | 20,410.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 13,670,000.00 USD | 13,670,000.00 USD | 55,830.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.00` | 13,600,000.00 USD | 13,600,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.30` | 13,560,000.00 USD | 13,560,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.60` | 13,540,000.00 USD | 13,540,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.90` | 13,510,000.00 USD | 13,510,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.20` | 13,480,000.00 USD | 13,480,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3666.50` | 13,460,000.00 USD | 13,460,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3819.10` | 5,390,000.00 USD | 5,390,000.00 USD | 27,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3821.30` | 13,450,000.00 USD | 13,450,000.00 USD | 17,080.00 USD | 0.00 USD | 28,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3823.30` | 5,370,000.00 USD | 5,370,000.00 USD | 4,900.00 USD | 0.00 USD | 42,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3825.60` | 13,400,000.00 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3827.50` | 5,320,000.00 USD | 5,320,000.00 USD | 33,040.00 USD | 0.00 USD | 40,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.90` | 13,370,000.00 USD | 13,370,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3831.70` | 5,250,000.00 USD | 5,250,000.00 USD | 21,840.00 USD | 0.00 USD | 80,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3834.20` | 13,290,000.00 USD | 13,290,000.00 USD | 86,270.00 USD | 0.00 USD | 34,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3835.90` | 5,140,000.00 USD | 5,140,000.00 USD | 103,760.00 USD | 0.00 USD | 75,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.50` | 13,170,000.00 USD | 13,170,000.00 USD | 334,470.00 USD | 0.00 USD | 99,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3840.10` | 4,970,000.00 USD | 4,970,000.00 USD | 61,360.00 USD | 0.00 USD | 77,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.80` | 12,740,000.00 USD | 12,740,000.00 USD | 569,120.00 USD | 0.00 USD | 199,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3844.30` | 4,830,000.00 USD | 4,830,000.00 USD | 197,290.00 USD | 0.00 USD | 141,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.10` | 11,970,000.00 USD | 11,970,000.00 USD | 416,440.00 USD | 0.00 USD | 143,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3848.50` | 4,490,000.00 USD | 4,490,000.00 USD | 46,980.00 USD | 0.00 USD | 20,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3851.40` | 11,410,000.00 USD | 11,410,000.00 USD | 257,490.00 USD | 0.00 USD | 74,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.70` | 4,420,000.00 USD | 4,420,000.00 USD | 85,690.00 USD | 0.00 USD | 39,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3855.70` | 11,080,000.00 USD | 11,080,000.00 USD | 221,360.00 USD | 0.00 USD | 47,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.90` | 4,300,000.00 USD | 4,300,000.00 USD | 96,830.00 USD | 0.00 USD | 23,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.00` | 10,810,000.00 USD | 10,810,000.00 USD | 147,250.00 USD | 0.00 USD | 28,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3861.10` | 4,180,000.00 USD | 4,180,000.00 USD | 151,640.00 USD | 0.00 USD | 36,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.30` | 10,630,000.00 USD | 10,630,000.00 USD | 232,560.00 USD | 0.00 USD | 75,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3865.30` | 3,990,000.00 USD | 3,990,000.00 USD | 206,710.00 USD | 0.00 USD | 24,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3868.60` | 10,320,000.00 USD | 10,320,000.00 USD | 285,320.00 USD | 0.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3869.50` | 3,760,000.00 USD | 3,760,000.00 USD | 104,160.00 USD | 0.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3872.90` | 10,010,000.00 USD | 10,010,000.00 USD | 221,120.00 USD | 0.00 USD | 41,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.70` | 3,640,000.00 USD | 3,640,000.00 USD | 24,350.00 USD | 0.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.20` | 9,750,000.00 USD | 9,750,000.00 USD | 153,170.00 USD | 0.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.90` | 3,610,000.00 USD | 3,610,000.00 USD | 11,600.00 USD | 0.00 USD | 313.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3881.50` | 9,570,000.00 USD | 9,570,000.00 USD | 96,090.00 USD | 0.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3885.80` | 9,450,000.00 USD | 9,450,000.00 USD | 124,650.00 USD | 0.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.10` | 9,290,000.00 USD | 9,290,000.00 USD | 85,430.00 USD | 0.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3894.40` | 9,190,000.00 USD | 9,190,000.00 USD | 126,480.00 USD | 0.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3898.70` | 9,050,000.00 USD | 9,050,000.00 USD | 166,900.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3898.90` | 3,600,000.00 USD | 3,600,000.00 USD | 54,040.00 USD | 0.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3903.00` | 8,880,000.00 USD | 8,880,000.00 USD | 17,060.00 USD | 0.00 USD | 130,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3903.10` | 3,520,000.00 USD | 3,520,000.00 USD | 9,800.00 USD | 0.00 USD | 64,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3907.30` | 3,450,000.00 USD | 3,450,000.00 USD | 66,080.00 USD | 0.00 USD | 81,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.30` | 8,730,000.00 USD | 8,730,000.00 USD | 56,630.00 USD | 0.00 USD | 98,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3911.50` | 3,300,000.00 USD | 3,300,000.00 USD | 43,670.00 USD | 0.00 USD | 160,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3911.60` | 8,570,000.00 USD | 8,570,000.00 USD | 51,010.00 USD | 0.00 USD | 81,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3915.70` | 3,100,000.00 USD | 3,100,000.00 USD | 207,520.00 USD | 0.00 USD | 150,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3915.90` | 8,440,000.00 USD | 8,440,000.00 USD | 287,340.00 USD | 0.00 USD | 173,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3919.90` | 2,740,000.00 USD | 2,740,000.00 USD | 122,710.00 USD | 0.00 USD | 138,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3920.20` | 7,980,000.00 USD | 7,980,000.00 USD | 731,980.00 USD | 0.00 USD | 181,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3924.10` | 2,480,000.00 USD | 2,480,000.00 USD | 368,670.00 USD | 0.00 USD | 263,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3924.50` | 7,070,000.00 USD | 7,070,000.00 USD | 1,280,000.00 USD | 0.00 USD | 465,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3928.30` | 1,840,000.00 USD | 1,840,000.00 USD | 119,870.00 USD | 0.00 USD | 69,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3928.80` | 5,320,000.00 USD | 5,320,000.00 USD | 723,280.00 USD | 0.00 USD | 185,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3932.50` | 1,660,000.00 USD | 1,660,000.00 USD | 149,210.00 USD | 0.00 USD | 80,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.10` | 4,410,000.00 USD | 4,410,000.00 USD | 340,890.00 USD | 0.00 USD | 133,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3936.70` | 1,430,000.00 USD | 1,430,000.00 USD | 205,910.00 USD | 0.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3937.40` | 3,940,000.00 USD | 3,940,000.00 USD | 466,400.00 USD | 0.00 USD | 56,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3940.90` | 1,170,000.00 USD | 1,170,000.00 USD | 282,810.00 USD | 0.00 USD | 48,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3941.70` | 3,410,000.00 USD | 3,410,000.00 USD | 312,800.00 USD | 0.00 USD | 114,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3945.10` | 837,820.00 USD | 837,820.00 USD | 415,700.00 USD | 0.00 USD | 69,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.00` | 2,990,000.00 USD | 2,990,000.00 USD | 494,480.00 USD | 0.00 USD | 111,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3949.30` | 353,010.00 USD | 353,010.00 USD | 205,220.00 USD | 0.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.30` | 2,380,000.00 USD | 2,380,000.00 USD | 498,180.00 USD | 0.00 USD | 72,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3953.50` | 122,370.00 USD | 122,370.00 USD | 79,910.00 USD | 0.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3954.60` | 1,810,000.00 USD | 1,810,000.00 USD | 417,480.00 USD | 0.00 USD | 53,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3957.70` | 23,820.00 USD | 23,820.00 USD | 23,200.00 USD | 0.00 USD | 626.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3958.90` | 1,340,000.00 USD | 1,340,000.00 USD | 275,800.00 USD | 0.00 USD | 41,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.20` | 1,020,000.00 USD | 1,020,000.00 USD | 303,170.00 USD | 0.00 USD | 57,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3967.50` | 660,520.00 USD | 660,520.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3971.80` | 483,240.00 USD | 483,240.00 USD | 218,900.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.10` | 218,310.00 USD | 218,310.00 USD | 204,930.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `3980.40` | 4,280.00 USD | 4,280.00 USD | 0.00 USD | 0.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `3984.70` | 64,110.00 USD | 64,110.00 USD | 59,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `3989.00` | 114,840.00 USD | 114,840.00 USD | 50,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4057.80` | 149,010.00 USD | 149,010.00 USD | 34,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4058.50` | 84,160.00 USD | 84,160.00 USD | 54,040.00 USD | 0.00 USD | 30,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4062.10` | 266,130.00 USD | 266,130.00 USD | 0.00 USD | 0.00 USD | 117,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4062.70` | 148,190.00 USD | 148,190.00 USD | 9,800.00 USD | 0.00 USD | 54,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4066.40` | 354,420.00 USD | 354,420.00 USD | 0.00 USD | 0.00 USD | 88,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4066.90` | 308,630.00 USD | 308,630.00 USD | 79,310.00 USD | 0.00 USD | 81,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4070.70` | 468,400.00 USD | 468,400.00 USD | 34,460.00 USD | 0.00 USD | 79,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4071.10` | 499,560.00 USD | 499,560.00 USD | 30,450.00 USD | 0.00 USD | 160,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4075.00` | 750,390.00 USD | 750,390.00 USD | 138,080.00 USD | 0.00 USD | 143,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4075.30` | 855,810.00 USD | 855,810.00 USD | 207,520.00 USD | 0.00 USD | 148,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.30` | 1,720,000.00 USD | 1,720,000.00 USD | 793,160.00 USD | 0.00 USD | 181,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4079.50` | 1,080,000.00 USD | 1,080,000.00 USD | 104,830.00 USD | 0.00 USD | 118,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4083.60` | 3,270,000.00 USD | 3,270,000.00 USD | 1,120,000.00 USD | 0.00 USD | 427,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4083.70` | 1,680,000.00 USD | 1,680,000.00 USD | 344,620.00 USD | 0.00 USD | 258,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4087.90` | 1,940,000.00 USD | 1,940,000.00 USD | 161,800.00 USD | 0.00 USD | 93,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4087.90` | 4,190,000.00 USD | 4,190,000.00 USD | 730,150.00 USD | 0.00 USD | 195,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4092.10` | 2,110,000.00 USD | 2,110,000.00 USD | 108,080.00 USD | 0.00 USD | 66,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4092.20` | 4,880,000.00 USD | 4,880,000.00 USD | 535,480.00 USD | 0.00 USD | 149,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4096.30` | 2,400,000.00 USD | 2,400,000.00 USD | 218,140.00 USD | 0.00 USD | 66,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4096.50` | 5,370,000.00 USD | 5,370,000.00 USD | 394,180.00 USD | 0.00 USD | 95,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4100.50` | 2,640,000.00 USD | 2,640,000.00 USD | 209,150.00 USD | 0.00 USD | 31,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4100.80` | 5,730,000.00 USD | 5,730,000.00 USD | 322,520.00 USD | 0.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4104.70` | 2,960,000.00 USD | 2,960,000.00 USD | 262,090.00 USD | 0.00 USD | 62,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4105.10` | 6,280,000.00 USD | 6,280,000.00 USD | 408,250.00 USD | 0.00 USD | 134,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4108.90` | 3,350,000.00 USD | 3,350,000.00 USD | 343,950.00 USD | 0.00 USD | 43,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4109.40` | 6,860,000.00 USD | 6,860,000.00 USD | 504,830.00 USD | 0.00 USD | 76,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4113.10` | 3,540,000.00 USD | 3,540,000.00 USD | 172,570.00 USD | 0.00 USD | 18,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4113.70` | 7,360,000.00 USD | 7,360,000.00 USD | 437,970.00 USD | 0.00 USD | 63,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4117.30` | 3,590,000.00 USD | 3,590,000.00 USD | 40,960.00 USD | 0.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.00` | 7,700,000.00 USD | 7,700,000.00 USD | 282,440.00 USD | 0.00 USD | 57,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4121.50` | 3,600,000.00 USD | 3,600,000.00 USD | 7,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.30` | 8,020,000.00 USD | 8,020,000.00 USD | 286,850.00 USD | 0.00 USD | 30,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4126.60` | 8,330,000.00 USD | 8,330,000.00 USD | 221,890.00 USD | 0.00 USD | 86,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4130.90` | 8,540,000.00 USD | 8,540,000.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.20` | 8,770,000.00 USD | 8,770,000.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4138.30` | 3,640,000.00 USD | 3,640,000.00 USD | 27,020.00 USD | 0.00 USD | 15,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4139.50` | 9,020,000.00 USD | 9,020,000.00 USD | 206,800.00 USD | 0.00 USD | 45,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4142.50` | 3,680,000.00 USD | 3,680,000.00 USD | 12,450.00 USD | 0.00 USD | 27,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4143.80` | 9,270,000.00 USD | 9,270,000.00 USD | 199,160.00 USD | 0.00 USD | 50,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4146.70` | 3,750,000.00 USD | 3,750,000.00 USD | 32,100.00 USD | 0.00 USD | 40,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.10` | 9,420,000.00 USD | 9,420,000.00 USD | 59,830.00 USD | 0.00 USD | 88,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4150.90` | 3,840,000.00 USD | 3,840,000.00 USD | 15,220.00 USD | 0.00 USD | 69,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4152.40` | 9,620,000.00 USD | 9,620,000.00 USD | 133,610.00 USD | 0.00 USD | 66,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4155.10` | 4,010,000.00 USD | 4,010,000.00 USD | 98,490.00 USD | 0.00 USD | 79,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4156.70` | 9,950,000.00 USD | 9,950,000.00 USD | 268,170.00 USD | 0.00 USD | 57,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4159.30` | 4,120,000.00 USD | 4,120,000.00 USD | 57,680.00 USD | 0.00 USD | 52,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.00` | 10,500,000.00 USD | 10,500,000.00 USD | 420,240.00 USD | 0.00 USD | 134,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4163.50` | 4,400,000.00 USD | 4,400,000.00 USD | 142,390.00 USD | 0.00 USD | 138,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.30` | 11,190,000.00 USD | 11,190,000.00 USD | 485,080.00 USD | 0.00 USD | 204,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4167.70` | 4,560,000.00 USD | 4,560,000.00 USD | 110,820.00 USD | 0.00 USD | 48,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.60` | 11,630,000.00 USD | 11,630,000.00 USD | 356,490.00 USD | 0.00 USD | 75,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4171.90` | 4,640,000.00 USD | 4,640,000.00 USD | 43,850.00 USD | 0.00 USD | 30,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4173.90` | 11,850,000.00 USD | 11,850,000.00 USD | 156,630.00 USD | 0.00 USD | 66,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.10` | 4,760,000.00 USD | 4,760,000.00 USD | 93,280.00 USD | 0.00 USD | 33,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.20` | 12,110,000.00 USD | 12,110,000.00 USD | 233,200.00 USD | 0.00 USD | 28,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.30` | 4,910,000.00 USD | 4,910,000.00 USD | 125,320.00 USD | 0.00 USD | 16,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,290,000.00 USD | 12,290,000.00 USD | 143,730.00 USD | 0.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.50` | 5,070,000.00 USD | 5,070,000.00 USD | 128,570.00 USD | 0.00 USD | 32,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.80` | 12,580,000.00 USD | 12,580,000.00 USD | 219,060.00 USD | 0.00 USD | 65,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.70` | 5,250,000.00 USD | 5,250,000.00 USD | 165,550.00 USD | 0.00 USD | 22,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.10` | 12,860,000.00 USD | 12,860,000.00 USD | 254,710.00 USD | 0.00 USD | 31,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.90` | 5,360,000.00 USD | 5,360,000.00 USD | 92,800.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.40` | 13,100,000.00 USD | 13,100,000.00 USD | 205,140.00 USD | 0.00 USD | 33,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4197.10` | 5,390,000.00 USD | 5,390,000.00 USD | 22,950.00 USD | 0.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.70` | 13,270,000.00 USD | 13,270,000.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.30` | 5,390,000.00 USD | 5,390,000.00 USD | 8,640.00 USD | 0.00 USD | 313.39 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.00` | 13,410,000.00 USD | 13,410,000.00 USD | 116,920.00 USD | 0.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.30` | 13,540,000.00 USD | 13,540,000.00 USD | 92,450.00 USD | 0.00 USD | 32,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4212.60` | 13,640,000.00 USD | 13,640,000.00 USD | 77,790.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.90` | 13,750,000.00 USD | 13,750,000.00 USD | 104,620.00 USD | 0.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.20` | 13,880,000.00 USD | 13,880,000.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4225.50` | 13,960,000.00 USD | 13,960,000.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4229.80` | 14,000,000.00 USD | 14,000,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.10` | 14,060,000.00 USD | 14,060,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4238.40` | 14,070,000.00 USD | 14,070,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4377.70` | 5,410,000.00 USD | 5,410,000.00 USD | 8,720.00 USD | 0.00 USD | 8,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4380.30` | 14,080,000.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4381.90` | 5,430,000.00 USD | 5,430,000.00 USD | 6,870.00 USD | 0.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4386.10` | 5,450,000.00 USD | 5,450,000.00 USD | 8,470.00 USD | 0.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4388.90` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4390.30` | 5,470,000.00 USD | 5,470,000.00 USD | 4,460.00 USD | 0.00 USD | 17,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4393.20` | 14,130,000.00 USD | 14,130,000.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4394.50` | 5,510,000.00 USD | 5,510,000.00 USD | 28,070.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4397.50` | 14,240,000.00 USD | 14,240,000.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4398.10` | 5,540,000.00 USD | 5,540,000.00 USD | 14,150.00 USD | 0.00 USD | 10,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4401.80` | 14,450,000.00 USD | 14,450,000.00 USD | 143,560.00 USD | 0.00 USD | 66,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.10` | 14,620,000.00 USD | 14,620,000.00 USD | 125,560.00 USD | 0.00 USD | 45,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4410.40` | 14,740,000.00 USD | 14,740,000.00 USD | 103,520.00 USD | 0.00 USD | 18,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4414.70` | 14,800,000.00 USD | 14,800,000.00 USD | 36,920.00 USD | 0.00 USD | 17,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.00` | 14,870,000.00 USD | 14,870,000.00 USD | 66,780.00 USD | 0.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.30` | 14,930,000.00 USD | 14,930,000.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4424.00` | 14,940,000.00 USD | 14,940,000.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD | `Tier 1 CEX` |

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
| `1D` | `3579.70` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 8,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3583.90` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 1,960.00 USD | 0.00 USD | 16,110.00 USD |
| `7D` | `3584.80` | 14,790,000.00 USD | 0.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `3588.10` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 10,740.00 USD | 0.00 USD | 10,980.00 USD |
| `7D` | `3589.10` | 14,780,000.00 USD | 0.00 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3592.30` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 7,110.00 USD | 0.00 USD | 21,860.00 USD |
| `7D` | `3593.40` | 14,760,000.00 USD | 0.00 USD | 14,760,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `3596.50` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 35,040.00 USD | 0.00 USD | 19,020.00 USD |
| `7D` | `3597.70` | 14,750,000.00 USD | 0.00 USD | 14,750,000.00 USD | 108,500.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `3600.70` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 26,650.00 USD | 0.00 USD | 28,530.00 USD |
| `7D` | `3602.00` | 14,620,000.00 USD | 0.00 USD | 14,620,000.00 USD | 173,930.00 USD | 0.00 USD | 75,620.00 USD |
| `1D` | `3604.90` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 54,630.00 USD | 0.00 USD | 39,640.00 USD |
| `7D` | `3606.30` | 14,370,000.00 USD | 0.00 USD | 14,370,000.00 USD | 152,940.00 USD | 0.00 USD | 43,450.00 USD |
| `1D` | `3609.10` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 14,040.00 USD | 0.00 USD | 3,810.00 USD |
| `7D` | `3610.60` | 14,170,000.00 USD | 0.00 USD | 14,170,000.00 USD | 72,480.00 USD | 0.00 USD | 20,480.00 USD |
| `1D` | `3613.30` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 33,240.00 USD | 0.00 USD | 12,240.00 USD |
| `7D` | `3614.90` | 14,080,000.00 USD | 0.00 USD | 14,080,000.00 USD | 76,990.00 USD | 0.00 USD | 16,470.00 USD |
| `1D` | `3617.50` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 41,740.00 USD | 0.00 USD | 5,470.00 USD |
| `7D` | `3619.20` | 13,990,000.00 USD | 0.00 USD | 13,990,000.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD |
| `1D` | `3621.70` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 37,530.00 USD | 0.00 USD | 10,010.00 USD |
| `7D` | `3623.50` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 45,130.00 USD | 0.00 USD | 22,740.00 USD |
| `1D` | `3625.90` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 51,070.00 USD | 0.00 USD | 7,660.00 USD |
| `7D` | `3627.80` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD |
| `1D` | `3630.10` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 19,470.00 USD | 0.00 USD | 2,670.00 USD |
| `7D` | `3632.10` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 60,720.00 USD | 0.00 USD | 7,710.00 USD |
| `1D` | `3634.30` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 2,050.00 USD | 0.00 USD | 594.12 USD |
| `7D` | `3636.40` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 20,410.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `3640.70` | 13,670,000.00 USD | 0.00 USD | 13,670,000.00 USD | 55,830.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `3645.00` | 13,600,000.00 USD | 0.00 USD | 13,600,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `7D` | `3649.30` | 13,560,000.00 USD | 0.00 USD | 13,560,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `7D` | `3653.60` | 13,540,000.00 USD | 0.00 USD | 13,540,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3657.90` | 13,510,000.00 USD | 0.00 USD | 13,510,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3662.20` | 13,480,000.00 USD | 0.00 USD | 13,480,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3666.50` | 13,460,000.00 USD | 0.00 USD | 13,460,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3819.10` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 27,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3821.30` | 13,450,000.00 USD | 0.00 USD | 13,450,000.00 USD | 17,080.00 USD | 0.00 USD | 28,090.00 USD |
| `1D` | `3823.30` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 4,900.00 USD | 0.00 USD | 42,180.00 USD |
| `7D` | `3825.60` | 13,400,000.00 USD | 0.00 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD |
| `1D` | `3827.50` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 33,040.00 USD | 0.00 USD | 40,570.00 USD |
| `7D` | `3829.90` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD |
| `1D` | `3831.70` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 21,840.00 USD | 0.00 USD | 80,240.00 USD |
| `7D` | `3834.20` | 13,290,000.00 USD | 0.00 USD | 13,290,000.00 USD | 86,270.00 USD | 0.00 USD | 34,180.00 USD |
| `1D` | `3835.90` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 103,760.00 USD | 0.00 USD | 75,370.00 USD |
| `7D` | `3838.50` | 13,170,000.00 USD | 0.00 USD | 13,170,000.00 USD | 334,470.00 USD | 0.00 USD | 99,980.00 USD |
| `1D` | `3840.10` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 61,360.00 USD | 0.00 USD | 77,280.00 USD |
| `7D` | `3842.80` | 12,740,000.00 USD | 0.00 USD | 12,740,000.00 USD | 569,120.00 USD | 0.00 USD | 199,760.00 USD |
| `1D` | `3844.30` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 197,290.00 USD | 0.00 USD | 141,360.00 USD |
| `7D` | `3847.10` | 11,970,000.00 USD | 0.00 USD | 11,970,000.00 USD | 416,440.00 USD | 0.00 USD | 143,690.00 USD |
| `1D` | `3848.50` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 46,980.00 USD | 0.00 USD | 20,000.00 USD |
| `7D` | `3851.40` | 11,410,000.00 USD | 0.00 USD | 11,410,000.00 USD | 257,490.00 USD | 0.00 USD | 74,890.00 USD |
| `1D` | `3852.70` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 85,690.00 USD | 0.00 USD | 39,480.00 USD |
| `7D` | `3855.70` | 11,080,000.00 USD | 0.00 USD | 11,080,000.00 USD | 221,360.00 USD | 0.00 USD | 47,670.00 USD |
| `1D` | `3856.90` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 96,830.00 USD | 0.00 USD | 23,600.00 USD |
| `7D` | `3860.00` | 10,810,000.00 USD | 0.00 USD | 10,810,000.00 USD | 147,250.00 USD | 0.00 USD | 28,510.00 USD |
| `1D` | `3861.10` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 151,640.00 USD | 0.00 USD | 36,810.00 USD |
| `7D` | `3864.30` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 232,560.00 USD | 0.00 USD | 75,710.00 USD |
| `1D` | `3865.30` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 206,710.00 USD | 0.00 USD | 24,460.00 USD |
| `7D` | `3868.60` | 10,320,000.00 USD | 0.00 USD | 10,320,000.00 USD | 285,320.00 USD | 0.00 USD | 26,240.00 USD |
| `1D` | `3869.50` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 104,160.00 USD | 0.00 USD | 11,550.00 USD |
| `7D` | `3872.90` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 221,120.00 USD | 0.00 USD | 41,690.00 USD |
| `1D` | `3873.70` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 24,350.00 USD | 0.00 USD | 7,780.00 USD |
| `7D` | `3877.20` | 9,750,000.00 USD | 0.00 USD | 9,750,000.00 USD | 153,170.00 USD | 0.00 USD | 23,330.00 USD |
| `1D` | `3877.90` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 11,600.00 USD | 0.00 USD | 313.39 USD |
| `7D` | `3881.50` | 9,570,000.00 USD | 0.00 USD | 9,570,000.00 USD | 96,090.00 USD | 0.00 USD | 27,510.00 USD |
| `7D` | `3885.80` | 9,450,000.00 USD | 0.00 USD | 9,450,000.00 USD | 124,650.00 USD | 0.00 USD | 30,910.00 USD |
| `7D` | `3890.10` | 9,290,000.00 USD | 0.00 USD | 9,290,000.00 USD | 85,430.00 USD | 0.00 USD | 19,460.00 USD |
| `7D` | `3894.40` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 126,480.00 USD | 0.00 USD | 10,240.00 USD |
| `7D` | `3898.70` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 166,900.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `3898.90` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 54,040.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `3903.00` | 8,880,000.00 USD | 0.00 USD | 8,880,000.00 USD | 17,060.00 USD | 0.00 USD | 130,200.00 USD |
| `1D` | `3903.10` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 9,800.00 USD | 0.00 USD | 64,950.00 USD |
| `1D` | `3907.30` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 66,080.00 USD | 0.00 USD | 81,140.00 USD |
| `7D` | `3907.30` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 56,630.00 USD | 0.00 USD | 98,910.00 USD |
| `1D` | `3911.50` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 43,670.00 USD | 0.00 USD | 160,480.00 USD |
| `7D` | `3911.60` | 8,570,000.00 USD | 0.00 USD | 8,570,000.00 USD | 51,010.00 USD | 0.00 USD | 81,430.00 USD |
| `1D` | `3915.70` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 207,520.00 USD | 0.00 USD | 150,730.00 USD |
| `7D` | `3915.90` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 287,340.00 USD | 0.00 USD | 173,650.00 USD |
| `1D` | `3919.90` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 122,710.00 USD | 0.00 USD | 138,860.00 USD |
| `7D` | `3920.20` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 731,980.00 USD | 0.00 USD | 181,350.00 USD |
| `1D` | `3924.10` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 368,670.00 USD | 0.00 USD | 263,330.00 USD |
| `7D` | `3924.50` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 1,280,000.00 USD | 0.00 USD | 465,510.00 USD |
| `1D` | `3928.30` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 119,870.00 USD | 0.00 USD | 69,340.00 USD |
| `7D` | `3928.80` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 723,280.00 USD | 0.00 USD | 185,470.00 USD |
| `1D` | `3932.50` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 149,210.00 USD | 0.00 USD | 80,220.00 USD |
| `7D` | `3933.10` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 340,890.00 USD | 0.00 USD | 133,810.00 USD |
| `1D` | `3936.70` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 205,910.00 USD | 0.00 USD | 51,660.00 USD |
| `7D` | `3937.40` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 466,400.00 USD | 0.00 USD | 56,370.00 USD |
| `1D` | `3940.90` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 282,810.00 USD | 0.00 USD | 48,030.00 USD |
| `7D` | `3941.70` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 312,800.00 USD | 0.00 USD | 114,460.00 USD |
| `1D` | `3945.10` | 837,820.00 USD | 0.00 USD | 837,820.00 USD | 415,700.00 USD | 0.00 USD | 69,110.00 USD |
| `7D` | `3946.00` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 494,480.00 USD | 0.00 USD | 111,080.00 USD |
| `1D` | `3949.30` | 353,010.00 USD | 0.00 USD | 353,010.00 USD | 205,220.00 USD | 0.00 USD | 25,420.00 USD |
| `7D` | `3950.30` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 498,180.00 USD | 0.00 USD | 72,590.00 USD |
| `1D` | `3953.50` | 122,370.00 USD | 0.00 USD | 122,370.00 USD | 79,910.00 USD | 0.00 USD | 18,640.00 USD |
| `7D` | `3954.60` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 417,480.00 USD | 0.00 USD | 53,640.00 USD |
| `1D` | `3957.70` | 23,820.00 USD | 0.00 USD | 23,820.00 USD | 23,200.00 USD | 0.00 USD | 626.79 USD |
| `7D` | `3958.90` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 275,800.00 USD | 0.00 USD | 41,700.00 USD |
| `7D` | `3963.20` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 303,170.00 USD | 0.00 USD | 57,060.00 USD |
| `7D` | `3967.50` | 660,520.00 USD | 0.00 USD | 660,520.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD |
| `7D` | `3971.80` | 483,240.00 USD | 0.00 USD | 483,240.00 USD | 218,900.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `3976.10` | 218,310.00 USD | 0.00 USD | 218,310.00 USD | 204,930.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `3980.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3980.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3980.40` | 4,280.00 USD | 4,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,280.00 USD |
| `7D` | `3984.70` | 64,110.00 USD | 64,110.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3989.00` | 114,840.00 USD | 114,840.00 USD | 0.00 USD | 50,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4057.80` | 149,010.00 USD | 149,010.00 USD | 0.00 USD | 34,170.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4058.50` | 84,160.00 USD | 84,160.00 USD | 0.00 USD | 54,040.00 USD | 0.00 USD | 30,120.00 USD |
| `7D` | `4062.10` | 266,130.00 USD | 266,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 117,120.00 USD |
| `1D` | `4062.70` | 148,190.00 USD | 148,190.00 USD | 0.00 USD | 9,800.00 USD | 0.00 USD | 54,230.00 USD |
| `7D` | `4066.40` | 354,420.00 USD | 354,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 88,290.00 USD |
| `1D` | `4066.90` | 308,630.00 USD | 308,630.00 USD | 0.00 USD | 79,310.00 USD | 0.00 USD | 81,140.00 USD |
| `7D` | `4070.70` | 468,400.00 USD | 468,400.00 USD | 0.00 USD | 34,460.00 USD | 0.00 USD | 79,530.00 USD |
| `1D` | `4071.10` | 499,560.00 USD | 499,560.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 160,480.00 USD |
| `7D` | `4075.00` | 750,390.00 USD | 750,390.00 USD | 0.00 USD | 138,080.00 USD | 0.00 USD | 143,900.00 USD |
| `1D` | `4075.30` | 855,810.00 USD | 855,810.00 USD | 0.00 USD | 207,520.00 USD | 0.00 USD | 148,730.00 USD |
| `7D` | `4079.30` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 793,160.00 USD | 0.00 USD | 181,320.00 USD |
| `1D` | `4079.50` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 104,830.00 USD | 0.00 USD | 118,800.00 USD |
| `7D` | `4083.60` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 427,200.00 USD |
| `1D` | `4083.70` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 344,620.00 USD | 0.00 USD | 258,530.00 USD |
| `1D` | `4087.90` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 161,800.00 USD | 0.00 USD | 93,580.00 USD |
| `7D` | `4087.90` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 730,150.00 USD | 0.00 USD | 195,500.00 USD |
| `1D` | `4092.10` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 108,080.00 USD | 0.00 USD | 66,790.00 USD |
| `7D` | `4092.20` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 535,480.00 USD | 0.00 USD | 149,790.00 USD |
| `1D` | `4096.30` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 218,140.00 USD | 0.00 USD | 66,770.00 USD |
| `7D` | `4096.50` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 394,180.00 USD | 0.00 USD | 95,350.00 USD |
| `1D` | `4100.50` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 209,150.00 USD | 0.00 USD | 31,520.00 USD |
| `7D` | `4100.80` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 322,520.00 USD | 0.00 USD | 42,790.00 USD |
| `1D` | `4104.70` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 262,090.00 USD | 0.00 USD | 62,730.00 USD |
| `7D` | `4105.10` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 408,250.00 USD | 0.00 USD | 134,430.00 USD |
| `1D` | `4108.90` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 343,950.00 USD | 0.00 USD | 43,620.00 USD |
| `7D` | `4109.40` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 504,830.00 USD | 0.00 USD | 76,750.00 USD |
| `1D` | `4113.10` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 172,570.00 USD | 0.00 USD | 18,130.00 USD |
| `7D` | `4113.70` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 437,970.00 USD | 0.00 USD | 63,950.00 USD |
| `1D` | `4117.30` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 40,960.00 USD | 0.00 USD | 6,800.00 USD |
| `7D` | `4118.00` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 282,440.00 USD | 0.00 USD | 57,050.00 USD |
| `1D` | `4121.50` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 7,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4122.30` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 286,850.00 USD | 0.00 USD | 30,750.00 USD |
| `7D` | `4126.60` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 221,890.00 USD | 0.00 USD | 86,130.00 USD |
| `7D` | `4130.90` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD |
| `7D` | `4135.20` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD |
| `1D` | `4138.30` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 27,020.00 USD | 0.00 USD | 15,060.00 USD |
| `7D` | `4139.50` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 206,800.00 USD | 0.00 USD | 45,750.00 USD |
| `1D` | `4142.50` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 12,450.00 USD | 0.00 USD | 27,110.00 USD |
| `7D` | `4143.80` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 199,160.00 USD | 0.00 USD | 50,830.00 USD |
| `1D` | `4146.70` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 32,100.00 USD | 0.00 USD | 40,570.00 USD |
| `7D` | `4148.10` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 88,440.00 USD |
| `1D` | `4150.90` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 15,220.00 USD | 0.00 USD | 69,900.00 USD |
| `7D` | `4152.40` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 133,610.00 USD | 0.00 USD | 66,470.00 USD |
| `1D` | `4155.10` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 98,490.00 USD | 0.00 USD | 79,530.00 USD |
| `7D` | `4156.70` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 268,170.00 USD | 0.00 USD | 57,810.00 USD |
| `1D` | `4159.30` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 57,680.00 USD | 0.00 USD | 52,470.00 USD |
| `7D` | `4161.00` | 10,500,000.00 USD | 10,500,000.00 USD | 0.00 USD | 420,240.00 USD | 0.00 USD | 134,730.00 USD |
| `1D` | `4163.50` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 142,390.00 USD | 0.00 USD | 138,090.00 USD |
| `7D` | `4165.30` | 11,190,000.00 USD | 11,190,000.00 USD | 0.00 USD | 485,080.00 USD | 0.00 USD | 204,730.00 USD |
| `1D` | `4167.70` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 110,820.00 USD | 0.00 USD | 48,030.00 USD |
| `7D` | `4169.60` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 356,490.00 USD | 0.00 USD | 75,190.00 USD |
| `1D` | `4171.90` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 43,850.00 USD | 0.00 USD | 30,380.00 USD |
| `7D` | `4173.90` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 156,630.00 USD | 0.00 USD | 66,900.00 USD |
| `1D` | `4176.10` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 93,280.00 USD | 0.00 USD | 33,360.00 USD |
| `7D` | `4178.20` | 12,110,000.00 USD | 12,110,000.00 USD | 0.00 USD | 233,200.00 USD | 0.00 USD | 28,180.00 USD |
| `1D` | `4180.30` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 125,320.00 USD | 0.00 USD | 16,560.00 USD |
| `7D` | `4182.50` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 143,730.00 USD | 0.00 USD | 40,030.00 USD |
| `1D` | `4184.50` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 128,570.00 USD | 0.00 USD | 32,780.00 USD |
| `7D` | `4186.80` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 219,060.00 USD | 0.00 USD | 65,350.00 USD |
| `1D` | `4188.70` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 165,550.00 USD | 0.00 USD | 22,020.00 USD |
| `7D` | `4191.10` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 254,710.00 USD | 0.00 USD | 31,760.00 USD |
| `1D` | `4192.90` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 92,800.00 USD | 0.00 USD | 7,360.00 USD |
| `7D` | `4195.40` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 205,140.00 USD | 0.00 USD | 33,460.00 USD |
| `1D` | `4197.10` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 22,950.00 USD | 0.00 USD | 7,420.00 USD |
| `7D` | `4199.70` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD |
| `1D` | `4201.30` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 8,640.00 USD | 0.00 USD | 313.39 USD |
| `7D` | `4204.00` | 13,410,000.00 USD | 13,410,000.00 USD | 0.00 USD | 116,920.00 USD | 0.00 USD | 23,560.00 USD |
| `7D` | `4208.30` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 92,450.00 USD | 0.00 USD | 32,380.00 USD |
| `7D` | `4212.60` | 13,640,000.00 USD | 13,640,000.00 USD | 0.00 USD | 77,790.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `4216.90` | 13,750,000.00 USD | 13,750,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 10,670.00 USD |
| `7D` | `4221.20` | 13,880,000.00 USD | 13,880,000.00 USD | 0.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `4225.50` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD |
| `7D` | `4229.80` | 14,000,000.00 USD | 14,000,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD |
| `7D` | `4234.10` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4238.40` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4377.70` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 8,720.00 USD | 0.00 USD | 8,360.00 USD |
| `7D` | `4380.30` | 14,080,000.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `4381.90` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 6,870.00 USD | 0.00 USD | 7,750.00 USD |
| `1D` | `4386.10` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 8,470.00 USD | 0.00 USD | 10,980.00 USD |
| `7D` | `4388.90` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `4390.30` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 4,460.00 USD | 0.00 USD | 17,730.00 USD |
| `7D` | `4393.20` | 14,130,000.00 USD | 14,130,000.00 USD | 0.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `4394.50` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 28,070.00 USD | 0.00 USD | 16,260.00 USD |
| `7D` | `4397.50` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `4398.10` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 14,150.00 USD | 0.00 USD | 10,020.00 USD |
| `7D` | `4401.80` | 14,450,000.00 USD | 14,450,000.00 USD | 0.00 USD | 143,560.00 USD | 0.00 USD | 66,400.00 USD |
| `7D` | `4406.10` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 125,560.00 USD | 0.00 USD | 45,370.00 USD |
| `7D` | `4410.40` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 103,520.00 USD | 0.00 USD | 18,970.00 USD |
| `7D` | `4414.70` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 36,920.00 USD | 0.00 USD | 17,590.00 USD |
| `7D` | `4419.00` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 66,780.00 USD | 0.00 USD | 7,680.00 USD |
| `7D` | `4423.30` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD |
| `7D` | `4424.00` | 14,940,000.00 USD | 14,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `273.84M` | Total OI Tokens: `68,919.1 PAXG`
  * 1h OI Change: `-0.24%` | 4h OI Change: `-0.63%` | 24h OI Change: `-0.42%`
  * Exchange Breakdown: Binance=`104.15M` | Bybit=`25.05M` | OKX=`-` | Hyperliquid=`24.56M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.19K` | Last 24h: `17.74K` | Last 3d: `85.70K` | Last 7d: `216.77K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0001%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0050%` | **USDT KuCoin** | `0.0050%` |
| **USDT MEXC** | `-0.0001%` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0066%` | **USDT Bitget** | `0.0012%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `PAXG` | `48.08%` | `51.92%` | `0.93` | 1,970,000.00 USD |
| `15M` | `Binance` | `46.23%` | `53.77%` | `0.86` | 1,140,000.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `81.36%` | `18.64%` | `4.36` | 120,510.00 USD |
| `15M` | `KuCoin` | `43.49%` | `56.51%` | `0.77` | 96,080.00 USD |
| `15M` | `Gate` | `39.05%` | `60.95%` | `0.64` | 55,030.00 USD |
| `15M` | `Bitget` | `44.5%` | `55.5%` | `0.80` | 98,250.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `33.7%` | `66.3%` | `0.51` | 161,420.00 USD |
| `15M` | `Bitunix` | `47%` | `53%` | `0.89` | 135,230.00 USD |
| `15M` | `Hyperliquid` | `20.72%` | `79.28%` | `0.26` | 32,380.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `73.33%` | `26.67%` | `2.75` | 114,270.00 USD |
| `15M` | `HTX` | `18.7%` | `81.3%` | `0.23` | 1,400.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `100%` | `0%` | `1.00` | 1,560.00 USD |
| `15M` | `Aster` | `10.58%` | `89.42%` | `0.12` | 3,460.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `43.68%` | `56.32%` | `0.78` | 7,620.00 USD |
| `15M` | `Whale Positions` | `46.23%` | `53.77%` | `0.86` | 1,140,000.00 USD |
| `15M` | `Global Accounts` | `48.08%` | `51.92%` | `0.93` | 1,970,000.00 USD |
| `1H` | `PAXG` | `52.83%` | `47.17%` | `1.12` | 19,910,000.00 USD |
| `1H` | `Binance` | `43.74%` | `56.26%` | `0.78` | 2,860,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `43.92%` | `56.08%` | `0.78` | 1,620,000.00 USD |
| `1H` | `KuCoin` | `45.59%` | `54.41%` | `0.84` | 99,430.00 USD |
| `1H` | `Gate` | `44.56%` | `55.44%` | `0.80` | 713,990.00 USD |
| `1H` | `Bitget` | `59.77%` | `40.23%` | `1.49` | 1,220,000.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `57.17%` | `42.83%` | `1.33` | 10,800,000.00 USD |
| `1H` | `Bitunix` | `47.77%` | `52.23%` | `0.91` | 863,440.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.55%` | `52.45%` | `0.91` | 1,040,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `45.85%` | `54.15%` | `0.85` | 397,250.00 USD |
| `1H` | `HTX` | `92.15%` | `7.85%` | `11.74` | 13,170.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `67.16%` | `32.84%` | `2.05` | 273,540.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `43.74%` | `56.26%` | `0.78` | 2,860,000.00 USD |
| `1H` | `Global Accounts` | `52.83%` | `47.17%` | `1.12` | 19,910,000.00 USD |
| `4H` | `PAXG` | `51.05%` | `48.95%` | `1.04` | 40,150,000.00 USD |
| `4H` | `Binance` | `49.71%` | `50.29%` | `0.99` | 14,600,000.00 USD |
| `4H` | `OKX` | `47.55%` | `52.45%` | `0.91` | 5,510,000.00 USD |
| `4H` | `Bybit` | `51.3%` | `48.7%` | `1.05` | 3,840,000.00 USD |
| `4H` | `KuCoin` | `48.42%` | `51.58%` | `0.94` | 805,080.00 USD |
| `4H` | `Gate` | `46.59%` | `53.41%` | `0.87` | 1,410,000.00 USD |
| `4H` | `Bitget` | `49.48%` | `50.52%` | `0.98` | 2,850,000.00 USD |
| `4H` | `BingX` | `42.46%` | `57.54%` | `0.74` | 2,620,000.00 USD |
| `4H` | `MEXC` | `47.03%` | `52.97%` | `0.89` | 3,380,000.00 USD |
| `4H` | `Bitunix` | `51.87%` | `48.13%` | `1.08` | 636,470.00 USD |
| `4H` | `Hyperliquid` | `65.65%` | `34.35%` | `1.91` | 641,860.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.56%` | `50.44%` | `0.98` | 1,270,000.00 USD |
| `4H` | `Crypto.com` | `45.56%` | `54.44%` | `0.84` | 16,870.00 USD |
| `4H` | `WhiteBIT` | `88.48%` | `11.52%` | `7.68` | 2,220,000.00 USD |
| `4H` | `HTX` | `75.33%` | `24.67%` | `3.05` | 18,870.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `47.37%` | `52.63%` | `0.90` | 119,710.00 USD |
| `4H` | `Aster` | `17.58%` | `82.42%` | `0.21` | 30,540.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `35.45%` | `64.55%` | `0.55` | 183,210.00 USD |
| `4H` | `Whale Positions` | `49.71%` | `50.29%` | `0.99` | 14,600,000.00 USD |
| `4H` | `Global Accounts` | `51.05%` | `48.95%` | `1.04` | 40,150,000.00 USD |


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
| `5m` | 11,020.00 USD | 120,690.00 USD | **`ACCUMULATION`** |
| `15m` | -399,340.00 USD | -13,450.00 USD | **`DISTRIBUTION`** |
| `30m` | -181,660.00 USD | 504,820.00 USD | **`ACCUMULATION`** |
| `1h` | -554,920.00 USD | 772,920.00 USD | **`ACCUMULATION`** |
| `2h` | -764,490.00 USD | 423,100.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,570,000.00 USD | 1,780,000.00 USD | **`ACCUMULATION`** |
| `6h` | -2,510,000.00 USD | -134,860.00 USD | **`DISTRIBUTION`** |
| `8h` | -760,580.00 USD | 853,590.00 USD | **`ACCUMULATION`** |
| `12h` | -697,890.00 USD | -96,510.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,920,000.00 USD | 1,040,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,260,000.00 USD | -7,710,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -21,030,000.00 USD | -69,800,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+11.02K` | 15m=`-399.34K` | 1h=`-554.92K` | 24h=`-1.92M`
* Futures Capital Netflows: 5m=`+120.69K` | 15m=`-13.45K` | 1h=`+772.92K` | 24h=`+1.04M`
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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3979.46` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3969.99` (Risk Distance: `9.47` pts)
  * +2.5R Take Profit: `4003.14`
  * Mathematical Lot Sizing: **`1.05 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4007.93` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4017.40` (Risk Distance: `9.47` pts)
  * +2.5R Take Profit: `3984.25`
  * Mathematical Lot Sizing: **`1.05 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`3999.38`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
