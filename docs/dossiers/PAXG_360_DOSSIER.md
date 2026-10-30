# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 14:29:40 IST` (`2026-10-30 08:59:40 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3996.09` | **Live Ask Quote**: `3996.18` | **Mid Price**: `3996.14`
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
  * Session VWAP: `3996.98` | VWAP Z-Score: `-0.80` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `8.32` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `46.79` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4027.25` | Lower -3.00σ Band: `3966.71`
  * Upper +2.51σ Band: `4022.30` | Lower -2.51σ Band: `3971.65`
  * Upper +2.01σ Band: `4017.26` | Lower -2.01σ Band: `3976.70`
  * Upper +2.00σ Band: `4017.16` | Lower -2.00σ Band: `3976.80`
  * Upper +1.28σ Band: `4009.89` | Lower -1.28σ Band: `3984.06`
  * Upper +1.00σ Band: `4007.07` | Lower -1.00σ Band: `3986.89`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3985.68` | EMA-20=`3989.86` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`3999.84` (Slope: `+0.0000`) | EMA-100=`4010.67`
  * Institutional Anchors: EMA-144=`4016.35` | EMA-200=`4020.73` (Slope: `-0.1117`) | EMA-233=`4023.54`
- **Range Boundaries**: 24H High=`4039.31` | 24H Low=`3965.22` | Weekly High=`4082.75` | Weekly Low=`3965.22`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4013.45` (Distance: `-0.40%`)
  * Point of Control (POC) = `4007.08` (Distance: `-0.24%`)
  * Value Area Low (VAL) = `3988.38` (Distance: `+0.23%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4052.58` | Weekly POC=`4017.32` | Weekly VAL=`4004.00`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4011.55` | Low=`3965.22`
  * New York Session (13:00-21:00 UTC): High=`4020.11` | Low=`3972.16`
  * Initial Balance (First Hour): IB High=`4011.55` | IB Low=`3988.18`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3980.15` - `4012.12`
  * Optimal Trade Entry (OTE 0.705): `4004.13`
  * Structural Invalidation Anchor (0.786): `4028.10`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `3991.23` | `3993.79` | `3990.46` | `3992.67` | `127` | 506,506.21 USD | 61,654.30 USD | `+12.17%` | -554,375.38 USD | `+0.52` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `3992.67` | `3992.67` | `3990.68` | `3991.08` | `56` | 221,801.97 USD | 3,569.44 USD | `+1.61%` | -550,805.95 USD | `+0.24` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `3991.08` | `3991.08` | `3990.47` | `3990.95` | `10` | 41,886.76 USD | 18,244.54 USD | `+43.56%` | -532,561.41 USD | `+0.30` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `3981.68` | `3991.15` | `3979.22` | `3989.06` | `520` | 2,072,644.26 USD | 167,881.86 USD | `+8.10%` | -499,236.63 USD | `+0.57` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `3989.06` | `3994.73` | `3988.88` | `3991.23` | `356` | 1,419,588.63 USD | -116,793.05 USD | `-8.23%` | -616,029.68 USD | `-0.27` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `3991.23` | `3993.79` | `3990.46` | `3990.95` | `193` | 769,975.44 USD | 83,288.68 USD | `+10.82%` | -532,741.00 USD | `+0.36` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `3999.19` | `4001.59` | `3987.00` | `3992.27` | `1,465` | 5,850,978.09 USD | -383,638.83 USD | `-6.56%` | 522,438.31 USD | `-0.92` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `3992.27` | `3994.60` | `3973.63` | `3981.69` | `1,798` | 7,168,194.57 USD | -1,074,302.54 USD | `-14.99%` | -551,864.23 USD | `-2.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `3981.68` | `3994.73` | `3979.22` | `3990.95` | `1,068` | 4,262,208.33 USD | 134,377.49 USD | `+3.15%` | -417,486.74 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `3994.73` | `3979.22` | `3990.95` | `1,068` | 4,262,208.33 USD | 134,377.49 USD | `+3.15%` | -444,588.74 USD | `+0.26` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,524,929.80 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,542,786.16 USD | `-1.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `3994.73` | `3979.22` | `3990.95` | `1,068` | 4,262,208.33 USD | 134,377.49 USD | `+3.15%` | -444,588.74 USD | `+0.26` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `BID` | `3996.80` | `4.9650` | 19,844.11 USD | 1,521,013.26 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `3996.90` | `11.3019` | 45,172.56 USD | 1,501,169.14 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3997.00` | `4.1954` | 16,769.01 USD | 1,455,996.58 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `3997.10` | `7.5045` | 29,996.24 USD | 1,439,227.57 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `3997.20` | `7.8152` | 31,238.92 USD | 1,409,231.33 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3997.30` | `18.6669` | 74,617.20 USD | 1,377,992.41 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `3997.40` | `0.4501` | 1,799.23 USD | 1,303,375.21 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `3997.50` | `18.7602` | 74,993.90 USD | 1,301,575.98 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3997.60` | `87.7699` | 350,868.95 USD | 1,226,582.08 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `3997.70` | `7.5471` | 30,171.04 USD | 875,713.13 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `3997.80` | `5.4119` | 21,635.69 USD | 845,542.09 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3997.90` | `7.5029` | 29,995.84 USD | 823,906.39 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3998.00` | `13.7510` | 54,976.50 USD | 793,910.55 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3998.10` | `35.5932` | 142,305.17 USD | 738,934.05 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `3998.20` | `50.2674` | 200,979.12 USD | 596,628.88 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `3998.30` | `10.5020` | 41,990.15 USD | 395,649.76 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `3998.40` | `8.1111` | 32,431.42 USD | 353,659.61 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `3998.50` | `21.7563` | 86,992.57 USD | 321,228.19 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `3998.60` | `2.2172` | 8,865.70 USD | 234,235.63 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `3998.70` | `56.3608` | 225,369.93 USD | 225,369.93 USD | `18 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `3998.75` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 3,998.75` | `0.00%` | `-` |
| `ASK` | `3998.80` | `0.0174` | 69.58 USD | 69.58 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `3999.00` | `0.5198` | 2,078.68 USD | 2,148.26 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `3999.30` | `7.5023` | 30,003.95 USD | 32,152.21 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `3999.40` | `15.2546` | 61,009.25 USD | 93,161.45 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `3999.50` | `3.8070` | 15,226.10 USD | 108,387.55 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `3999.60` | `4.3273` | 17,307.47 USD | 125,695.02 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `3999.70` | `7.8586` | 31,432.04 USD | 157,127.06 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `3999.80` | `11.7191` | 46,874.06 USD | 204,001.12 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `3999.90` | `0.3750` | 1,499.96 USD | 205,501.08 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4000.00` | `56.8485` | 227,394.00 USD | 432,895.08 USD | `9 orders` | `+0.03%` | `-` |
| `ASK` | `4000.10` | `10.1070` | 40,429.01 USD | 473,324.09 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4000.20` | `0.4687` | 1,874.89 USD | 475,198.99 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `4000.30` | `29.1642` | 116,665.55 USD | 591,864.54 USD | `9 orders` | `+0.04%` | `-` |
| `ASK` | `4000.40` | `33.4235` | 133,707.37 USD | 725,571.90 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4000.50` | `3.9627` | 15,852.78 USD | 741,424.69 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4000.60` | `4.6635` | 18,656.80 USD | 760,081.48 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4000.70` | `10.7049` | 42,827.09 USD | 802,908.58 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `4000.80` | `12.6198` | 50,489.30 USD | 853,397.87 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `4000.90` | `28.7641` | 115,082.29 USD | 968,480.16 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `4001.00` | `79.9613` | 319,925.16 USD | 1,288,405.32 USD | `5 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:22:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `47` | `0x5b5d...c060` | `SHORT` | 25,950,859.23 USD | `6,489.82` | `4185.46` | `3999.60` | `29020.53` | 1,212,091.78 USD | `+4.67%` | `4X Cross` |
| `48` | `0x4692...164f` | `SHORT` | 25,292,531.65 USD | `6,325.19` | `4127.45` | `3999.60` | `14069.78` | 814,390.88 USD | `+3.22%` | `5X Cross` |
| `62` | `0xb83d...6e36` | `SHORT` | 23,471,966.73 USD | `5,869.90` | `4228.86` | `3999.60` | `26577.46` | 1,351,055.20 USD | `+5.76%` | `5X Cross` |
| `97` | `0xec0b...b078` | `LONG` | 19,306,935.57 USD | `4,828.91` | `4157.43` | `3999.60` | `2294.57` | -768,946.75 USD | `-3.98%` | `25X Cross` |
| `142` | `0x645b...87b8` | `LONG` | 14,189,454.75 USD | `3,548.61` | `4127.81` | `3999.60` | `636.25` | -458,544.03 USD | `-3.23%` | `3X Cross` |
| `157` | `0x7a6d...f79c` | `SHORT` | 13,068,604.12 USD | `3,268.21` | `4228.94` | `3999.60` | `4377.49` | 752,475.01 USD | `+5.76%` | `25X Cross` |
| `182` | `0xa742...e390` | `SHORT` | 11,196,168.77 USD | `2,800.02` | `4364.62` | `3999.60` | `4212.74` | 1,024,875.37 USD | `+9.15%` | `20X Cross` |
| `262` | `0x3678...b209` | `LONG` | 8,797,140.00 USD | `2,200.00` | `4176.09` | `3999.60` | `2672.28` | -390,279.30 USD | `-4.44%` | `25X Cross` |
| `263` | `0x41e5...0825` | `SHORT` | 8,797,140.00 USD | `2,200.00` | `4112.20` | `3999.60` | `4287.08` | 249,714.59 USD | `+2.84%` | `20X Cross` |
| `304` | `0xacb6...efbd` | `SHORT` | 7,898,710.88 USD | `1,975.37` | `4048.55` | `3999.60` | `6635.23` | 98,680.83 USD | `+1.25%` | `6X Cross` |
| `367` | `0xc26c...b8f4` | `LONG` | 6,317,753.26 USD | `1,579.95` | `4075.62` | `3999.60` | `0.000000` | -121,543.71 USD | `-1.92%` | `1X Cross` |
| `567` | `0x63da...8add` | `LONG` | 3,998,700.00 USD | `1,000.00` | `4021.46` | `3999.60` | `3564.63` | -22,760.96 USD | `-0.57%` | `25X Cross` |
| `578` | `0xf3dc...1672` | `LONG` | 3,935,803.25 USD | `984.27` | `4018.39` | `3999.60` | `2835.06` | -19,383.45 USD | `-0.49%` | `20X Cross` |
| `595` | `0x9aa5...58af` | `LONG` | 3,885,304.87 USD | `971.64` | `4279.98` | `3999.60` | `0.000000` | -273,304.22 USD | `-7.03%` | `20X Cross` |
| `674` | `0x4a20...3c26` | `LONG` | 3,348,510.18 USD | `837.40` | `4599.73` | `3999.60` | `0.000000` | -503,310.20 USD | `-15.03%` | `20X Cross` |
| `794` | `0x9c06...0560` | `LONG` | 2,906,862.16 USD | `726.95` | `4002.36` | `3999.60` | `0.000000` | -2,667.09 USD | `-0.09%` | `25X Cross` |
| `834` | `0x0fac...7a0a` | `LONG` | 2,744,978.92 USD | `686.49` | `4290.34` | `3999.60` | `1410.08` | -200,279.78 USD | `-7.30%` | `25X Cross` |
| `896` | `0x354b...6425` | `LONG` | 2,526,790.53 USD | `631.90` | `4004.93` | `3999.60` | `0.000000` | -3,939.85 USD | `-0.16%` | `10X Cross` |
| `910` | `0x625e...a354` | `SHORT` | 2,479,194.00 USD | `620.00` | `4122.81` | `3999.60` | `4279.49` | 76,953.03 USD | `+3.10%` | `20X Cross` |
| `937` | `0xeae3...e8ad` | `SHORT` | 2,399,280.00 USD | `600.00` | `4104.77` | `3999.60` | `4268.58` | 63,585.11 USD | `+2.65%` | `20X Cross` |
| `940` | `0xf285...fa82` | `LONG` | 2,391,646.06 USD | `598.11` | `4146.45` | `3999.60` | `3891.76` | -88,373.49 USD | `-3.70%` | `25X Cross` |
| `945` | `0xd8c5...99b0` | `SHORT` | 2,376,646.94 USD | `594.35` | `4175.35` | `3999.60` | `35442.36` | 104,997.09 USD | `+4.42%` | `4X Cross` |
| `952` | `0x12f7...8750` | `LONG` | 2,341,681.51 USD | `585.61` | `4082.77` | `3999.60` | `2701.23` | -49,235.47 USD | `-2.10%` | `10X Cross` |
| `997` | `0x413c...886c` | `LONG` | 2,237,210.24 USD | `559.47` | `4007.05` | `3999.60` | `0.000000` | -4,616.97 USD | `-0.21%` | `2X Cross` |
| `1108` | `0x61ce...a62b` | `SHORT` | 1,989,417.00 USD | `497.50` | `4071.66` | `3999.60` | `4723.82` | 36,251.80 USD | `+1.82%` | `20X Cross` |
| `1185` | `0x2edd...8179` | `LONG` | 1,877,125.85 USD | `469.26` | `4164.68` | `4000.45` | `0.000000` | -77,182.92 USD | `-4.11%` | `10X Cross` |
| `1231` | `0xead5...69f2` | `LONG` | 1,814,545.68 USD | `453.78` | `4220.88` | `3999.60` | `3539.46` | -100,822.38 USD | `-5.56%` | `5X Isolated` |
| `1292` | `0x7a6d...f79c` | `SHORT` | 1,713,629.52 USD | `428.38` | `4136.09` | `4000.45` | `5417.71` | 58,185.49 USD | `+3.40%` | `10X Cross` |
| `1309` | `0x46fc...1195` | `LONG` | 1,671,403.82 USD | `417.99` | `4052.43` | `3999.60` | `2178.80` | -22,461.43 USD | `-1.34%` | `20X Cross` |
| `1357` | `0x6d15...d374` | `LONG` | 1,599,480.00 USD | `400.00` | `4068.25` | `3999.60` | `3842.33` | -27,820.00 USD | `-1.74%` | `25X Cross` |
| `1358` | `0xee02...309d` | `SHORT` | 1,599,440.00 USD | `400.00` | `4438.84` | `3999.60` | `4202.87` | 176,098.60 USD | `+11.01%` | `25X Isolated` |
| `1380` | `0x51f6...2b39` | `LONG` | 1,565,880.85 USD | `391.48` | `4228.25` | `4000.45` | `544.54` | -89,394.84 USD | `-5.71%` | `10X Cross` |
| `1388` | `0x02a7...fe9f` | `SHORT` | 1,559,493.00 USD | `390.00` | `4055.02` | `3999.60` | `4307.20` | 21,966.25 USD | `+1.41%` | `25X Cross` |
| `1440` | `0x7e77...b8d2` | `SHORT` | 1,519,506.00 USD | `380.00` | `4131.92` | `3999.60` | `4294.01` | 50,623.64 USD | `+3.33%` | `20X Cross` |
| `1468` | `0x72c2...9b37` | `LONG` | 1,492,077.44 USD | `373.13` | `4000.98` | `3999.60` | `3778.56` | -816.07 USD | `-0.05%` | `13X Isolated` |
| `1483` | `0x781e...96b7` | `SHORT` | 1,463,339.42 USD | `365.84` | `4358.71` | `4000.45` | `12865.90` | 131,268.23 USD | `+8.97%` | `10X Cross` |
| `1502` | `0xaa44...b844` | `LONG` | 1,439,532.00 USD | `360.00` | `4043.10` | `3999.60` | `2816.75` | -15,985.63 USD | `-1.11%` | `4X Cross` |
| `1623` | `0xa41f...d50a` | `LONG` | 1,315,420.75 USD | `328.96` | `4468.89` | `3999.60` | `3802.69` | -154,677.10 USD | `-11.76%` | `15X Cross` |
| `1673` | `0xbf5a...88ba` | `SHORT` | 1,270,174.88 USD | `317.65` | `4091.80` | `3999.60` | `9955.53` | 29,608.15 USD | `+2.33%` | `20X Cross` |
| `1714` | `0xff31...ff6c` | `SHORT` | 1,239,597.00 USD | `310.00` | `4372.43` | `3999.60` | `4789.68` | 115,858.38 USD | `+9.35%` | `10X Isolated` |
| `1744` | `0xada6...6f88` | `LONG` | 1,213,471.49 USD | `303.47` | `4166.46` | `3999.60` | `1785.33` | -50,910.96 USD | `-4.20%` | `5X Cross` |
| `1897` | `0x50e2...d770` | `LONG` | 1,081,118.12 USD | `270.37` | `4243.58` | `3999.60` | `2562.61` | -66,208.34 USD | `-6.12%` | `20X Cross` |
| `1906` | `0x4c92...4f17` | `SHORT` | 1,066,535.26 USD | `266.72` | `4260.98` | `3999.60` | `6500.47` | 69,956.97 USD | `+6.56%` | `20X Cross` |
| `1971` | `0xd346...c4f3` | `LONG` | 1,020,337.96 USD | `255.17` | `4188.66` | `3999.60` | `3310.94` | -48,498.55 USD | `-4.75%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4096.30` (Vol: 350,100.00 USD, Dist: `+2.56%`) | Long MP=`3937.38` (Vol: 356,200.00 USD, Dist: `--1.42%`)
  * 48H Horizon: Short MP=`4111.27` (Vol: 328,300.00 USD, Dist: `+2.94%`) | Long MP=`3936.60` (Vol: 378,100.00 USD, Dist: `--1.44%`)
  * 3D Horizon: Short MP=`4111.27` (Vol: 367,600.00 USD, Dist: `+2.94%`) | Long MP=`3949.08` (Vol: 404,600.00 USD, Dist: `--1.12%`)
  * 7D Horizon: Short MP=`4086.31` (Vol: 853,900.00 USD, Dist: `+2.31%`) | Long MP=`3927.24` (Vol: 1,100,000.00 USD, Dist: `--1.67%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `Long Liquidation` | `3581.80` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3584.30` | 15,080,000.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3586.00` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3588.70` | 15,070,000.00 USD | 15,070,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3590.20` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3593.10` | 15,050,000.00 USD | 15,050,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3594.40` | 5,470,000.00 USD | 5,470,000.00 USD | 28,070.00 USD | 0.00 USD | 13,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3597.50` | 15,040,000.00 USD | 15,040,000.00 USD | 99,580.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3598.60` | 5,430,000.00 USD | 5,430,000.00 USD | 14,150.00 USD | 0.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3601.90` | 14,920,000.00 USD | 14,920,000.00 USD | 182,840.00 USD | 0.00 USD | 69,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3602.80` | 5,410,000.00 USD | 5,410,000.00 USD | 36,990.00 USD | 0.00 USD | 47,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3606.30` | 14,670,000.00 USD | 14,670,000.00 USD | 152,940.00 USD | 0.00 USD | 52,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3607.00` | 5,320,000.00 USD | 5,320,000.00 USD | 48,270.00 USD | 0.00 USD | 11,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3610.70` | 14,460,000.00 USD | 14,460,000.00 USD | 72,480.00 USD | 0.00 USD | 25,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3611.20` | 5,260,000.00 USD | 5,260,000.00 USD | 25,560.00 USD | 0.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.10` | 14,360,000.00 USD | 14,360,000.00 USD | 76,990.00 USD | 0.00 USD | 15,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3615.40` | 5,230,000.00 USD | 5,230,000.00 USD | 31,290.00 USD | 0.00 USD | 10,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.50` | 14,270,000.00 USD | 14,270,000.00 USD | 45,440.00 USD | 0.00 USD | 15,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3619.60` | 5,190,000.00 USD | 5,190,000.00 USD | 42,080.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.80` | 5,140,000.00 USD | 5,140,000.00 USD | 61,240.00 USD | 0.00 USD | 8,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.90` | 14,210,000.00 USD | 14,210,000.00 USD | 55,480.00 USD | 0.00 USD | 21,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3628.00` | 5,070,000.00 USD | 5,070,000.00 USD | 28,780.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.30` | 14,130,000.00 USD | 14,130,000.00 USD | 78,160.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3632.20` | 5,030,000.00 USD | 5,030,000.00 USD | 10,830.00 USD | 0.00 USD | 3,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.70` | 14,040,000.00 USD | 14,040,000.00 USD | 65,870.00 USD | 0.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3636.40` | 5,020,000.00 USD | 5,020,000.00 USD | 11,520.00 USD | 0.00 USD | 204.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.10` | 13,970,000.00 USD | 13,970,000.00 USD | 25,300.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.50` | 13,940,000.00 USD | 13,940,000.00 USD | 45,790.00 USD | 0.00 USD | 13,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.90` | 13,880,000.00 USD | 13,880,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3650.30` | 13,850,000.00 USD | 13,850,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3654.70` | 13,830,000.00 USD | 13,830,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3659.10` | 13,770,000.00 USD | 13,770,000.00 USD | 6,820.00 USD | 0.00 USD | 4,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3663.50` | 13,760,000.00 USD | 13,760,000.00 USD | 12,530.00 USD | 0.00 USD | 4,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3667.90` | 13,740,000.00 USD | 13,740,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3821.20` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3821.90` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3825.40` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3829.60` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.70` | 13,700,000.00 USD | 13,700,000.00 USD | 0.00 USD | 0.00 USD | 84,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3833.80` | 4,950,000.00 USD | 4,950,000.00 USD | 81,530.00 USD | 0.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3835.10` | 13,620,000.00 USD | 13,620,000.00 USD | 69,040.00 USD | 0.00 USD | 58,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3838.00` | 4,840,000.00 USD | 4,840,000.00 USD | 38,960.00 USD | 0.00 USD | 71,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3839.50` | 13,490,000.00 USD | 13,490,000.00 USD | 396,580.00 USD | 0.00 USD | 91,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3842.20` | 4,730,000.00 USD | 4,730,000.00 USD | 93,750.00 USD | 0.00 USD | 109,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3843.90` | 13,000,000.00 USD | 13,000,000.00 USD | 597,060.00 USD | 0.00 USD | 208,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3846.40` | 4,530,000.00 USD | 4,530,000.00 USD | 180,250.00 USD | 0.00 USD | 87,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3848.30` | 12,200,000.00 USD | 12,200,000.00 USD | 436,120.00 USD | 0.00 USD | 112,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3850.60` | 4,260,000.00 USD | 4,260,000.00 USD | 41,090.00 USD | 0.00 USD | 31,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.70` | 11,650,000.00 USD | 11,650,000.00 USD | 228,280.00 USD | 0.00 USD | 74,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3854.80` | 4,190,000.00 USD | 4,190,000.00 USD | 109,230.00 USD | 0.00 USD | 31,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3857.10` | 11,350,000.00 USD | 11,350,000.00 USD | 233,200.00 USD | 0.00 USD | 38,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3859.00` | 4,050,000.00 USD | 4,050,000.00 USD | 125,320.00 USD | 0.00 USD | 20,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3861.50` | 11,070,000.00 USD | 11,070,000.00 USD | 174,990.00 USD | 0.00 USD | 58,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3863.20` | 3,900,000.00 USD | 3,900,000.00 USD | 136,260.00 USD | 0.00 USD | 32,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3865.90` | 10,840,000.00 USD | 10,840,000.00 USD | 261,040.00 USD | 0.00 USD | 62,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3867.40` | 3,730,000.00 USD | 3,730,000.00 USD | 182,060.00 USD | 0.00 USD | 22,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3870.30` | 10,520,000.00 USD | 10,520,000.00 USD | 226,450.00 USD | 0.00 USD | 32,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3871.60` | 3,530,000.00 USD | 3,530,000.00 USD | 109,480.00 USD | 0.00 USD | 12,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3874.70` | 10,260,000.00 USD | 10,260,000.00 USD | 224,270.00 USD | 0.00 USD | 25,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3875.80` | 3,400,000.00 USD | 3,400,000.00 USD | 28,070.00 USD | 0.00 USD | 5,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3879.10` | 10,010,000.00 USD | 10,010,000.00 USD | 122,020.00 USD | 0.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3880.00` | 3,370,000.00 USD | 3,370,000.00 USD | 30,410.00 USD | 0.00 USD | 813.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3883.50` | 9,870,000.00 USD | 9,870,000.00 USD | 161,950.00 USD | 0.00 USD | 36,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3887.90` | 9,670,000.00 USD | 9,670,000.00 USD | 87,390.00 USD | 0.00 USD | 32,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.30` | 9,550,000.00 USD | 9,550,000.00 USD | 104,620.00 USD | 0.00 USD | 12,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.70` | 9,430,000.00 USD | 9,430,000.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.00` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.10` | 9,310,000.00 USD | 9,310,000.00 USD | 73,850.00 USD | 0.00 USD | 75,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3905.20` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.50` | 9,160,000.00 USD | 9,160,000.00 USD | 55,280.00 USD | 0.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3909.40` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3909.90` | 9,090,000.00 USD | 9,090,000.00 USD | 34,960.00 USD | 0.00 USD | 162,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3913.60` | 3,230,000.00 USD | 3,230,000.00 USD | 163,060.00 USD | 0.00 USD | 61,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3914.30` | 8,890,000.00 USD | 8,890,000.00 USD | 138,080.00 USD | 0.00 USD | 40,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3917.80` | 3,000,000.00 USD | 3,000,000.00 USD | 55,700.00 USD | 0.00 USD | 142,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3918.70` | 8,710,000.00 USD | 8,710,000.00 USD | 763,340.00 USD | 0.00 USD | 199,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3922.00` | 2,810,000.00 USD | 2,810,000.00 USD | 187,870.00 USD | 0.00 USD | 206,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3923.10` | 7,750,000.00 USD | 7,750,000.00 USD | 1,120,000.00 USD | 0.00 USD | 399,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3926.20` | 2,410,000.00 USD | 2,410,000.00 USD | 382,350.00 USD | 0.00 USD | 187,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3927.50` | 6,230,000.00 USD | 6,230,000.00 USD | 844,290.00 USD | 0.00 USD | 266,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3930.40` | 1,840,000.00 USD | 1,840,000.00 USD | 40,700.00 USD | 0.00 USD | 46,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3931.90` | 5,110,000.00 USD | 5,110,000.00 USD | 586,550.00 USD | 0.00 USD | 170,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.60` | 1,750,000.00 USD | 1,750,000.00 USD | 237,090.00 USD | 0.00 USD | 75,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3936.30` | 4,360,000.00 USD | 4,360,000.00 USD | 418,330.00 USD | 0.00 USD | 95,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.80` | 1,440,000.00 USD | 1,440,000.00 USD | 215,190.00 USD | 0.00 USD | 39,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3940.70` | 3,840,000.00 USD | 3,840,000.00 USD | 335,530.00 USD | 0.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3943.00` | 1,190,000.00 USD | 1,190,000.00 USD | 315,460.00 USD | 0.00 USD | 64,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3945.10` | 3,440,000.00 USD | 3,440,000.00 USD | 398,420.00 USD | 0.00 USD | 137,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3947.20` | 807,080.00 USD | 807,080.00 USD | 365,110.00 USD | 0.00 USD | 46,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3949.50` | 2,900,000.00 USD | 2,900,000.00 USD | 549,120.00 USD | 0.00 USD | 68,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3951.40` | 395,840.00 USD | 395,840.00 USD | 195,870.00 USD | 0.00 USD | 25,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3953.90` | 2,280,000.00 USD | 2,280,000.00 USD | 442,240.00 USD | 0.00 USD | 66,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.60` | 174,110.00 USD | 174,110.00 USD | 83,380.00 USD | 0.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3958.30` | 1,770,000.00 USD | 1,770,000.00 USD | 306,330.00 USD | 0.00 USD | 49,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.80` | 73,340.00 USD | 73,340.00 USD | 71,090.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3962.70` | 1,420,000.00 USD | 1,420,000.00 USD | 192,180.00 USD | 0.00 USD | 56,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3964.00` | 606.18 USD | 606.18 USD | 0.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3967.10` | 1,170,000.00 USD | 1,170,000.00 USD | 249,290.00 USD | 0.00 USD | 57,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3971.50` | 863,560.00 USD | 863,560.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3975.90` | 616,600.00 USD | 616,600.00 USD | 255,840.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.30` | 347,370.00 USD | 347,370.00 USD | 232,530.00 USD | 0.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3984.70` | 110,560.00 USD | 110,560.00 USD | 59,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.10` | 50,730.00 USD | 50,730.00 USD | 50,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4060.60` | 19,400.00 USD | 19,400.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4063.90` | 60,950.00 USD | 60,950.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4064.80` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4068.30` | 185,820.00 USD | 185,820.00 USD | 0.00 USD | 0.00 USD | 124,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4069.00` | 109,160.00 USD | 109,160.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4072.70` | 319,810.00 USD | 319,810.00 USD | 57,650.00 USD | 0.00 USD | 76,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4073.20` | 302,430.00 USD | 302,430.00 USD | 131,440.00 USD | 0.00 USD | 61,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.10` | 980,620.00 USD | 980,620.00 USD | 539,520.00 USD | 0.00 USD | 121,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4077.40` | 532,290.00 USD | 532,290.00 USD | 87,320.00 USD | 0.00 USD | 142,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4081.50` | 2,290,000.00 USD | 2,290,000.00 USD | 973,810.00 USD | 0.00 USD | 337,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4081.60` | 903,240.00 USD | 903,240.00 USD | 178,090.00 USD | 0.00 USD | 192,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4085.80` | 1,470,000.00 USD | 1,470,000.00 USD | 362,630.00 USD | 0.00 USD | 201,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.90` | 3,470,000.00 USD | 3,470,000.00 USD | 813,840.00 USD | 0.00 USD | 366,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4090.00` | 1,580,000.00 USD | 1,580,000.00 USD | 70,210.00 USD | 0.00 USD | 42,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.30` | 4,430,000.00 USD | 4,430,000.00 USD | 795,150.00 USD | 0.00 USD | 159,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.20` | 1,840,000.00 USD | 1,840,000.00 USD | 195,060.00 USD | 0.00 USD | 62,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.70` | 4,820,000.00 USD | 4,820,000.00 USD | 274,190.00 USD | 0.00 USD | 118,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.40` | 2,070,000.00 USD | 2,070,000.00 USD | 188,180.00 USD | 0.00 USD | 41,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4099.10` | 5,380,000.00 USD | 5,380,000.00 USD | 528,170.00 USD | 0.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.60` | 2,420,000.00 USD | 2,420,000.00 USD | 281,660.00 USD | 0.00 USD | 73,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4103.50` | 5,870,000.00 USD | 5,870,000.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.80` | 2,870,000.00 USD | 2,870,000.00 USD | 402,520.00 USD | 0.00 USD | 44,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4107.90` | 6,470,000.00 USD | 6,470,000.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4111.00` | 3,120,000.00 USD | 3,120,000.00 USD | 224,660.00 USD | 0.00 USD | 30,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4112.30` | 7,070,000.00 USD | 7,070,000.00 USD | 528,700.00 USD | 0.00 USD | 67,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.20` | 3,260,000.00 USD | 3,260,000.00 USD | 114,110.00 USD | 0.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4116.70` | 7,450,000.00 USD | 7,450,000.00 USD | 338,630.00 USD | 0.00 USD | 42,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.40` | 3,330,000.00 USD | 3,330,000.00 USD | 66,420.00 USD | 0.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4121.10` | 7,710,000.00 USD | 7,710,000.00 USD | 225,210.00 USD | 0.00 USD | 36,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4123.60` | 3,340,000.00 USD | 3,340,000.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4125.50` | 8,110,000.00 USD | 8,110,000.00 USD | 342,730.00 USD | 0.00 USD | 61,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4129.90` | 8,290,000.00 USD | 8,290,000.00 USD | 125,300.00 USD | 0.00 USD | 56,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4134.30` | 8,530,000.00 USD | 8,530,000.00 USD | 195,250.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4138.70` | 8,760,000.00 USD | 8,760,000.00 USD | 219,810.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4140.40` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4143.10` | 9,040,000.00 USD | 9,040,000.00 USD | 232,530.00 USD | 0.00 USD | 47,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4144.60` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4147.50` | 9,190,000.00 USD | 9,190,000.00 USD | 59,830.00 USD | 0.00 USD | 91,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4148.80` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4151.90` | 9,370,000.00 USD | 9,370,000.00 USD | 116,380.00 USD | 0.00 USD | 57,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4153.00` | 3,490,000.00 USD | 3,490,000.00 USD | 65,720.00 USD | 0.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4156.30` | 9,670,000.00 USD | 9,670,000.00 USD | 243,560.00 USD | 0.00 USD | 57,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4157.20` | 3,600,000.00 USD | 3,600,000.00 USD | 36,330.00 USD | 0.00 USD | 71,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4160.70` | 10,120,000.00 USD | 10,120,000.00 USD | 336,690.00 USD | 0.00 USD | 111,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4161.40` | 3,780,000.00 USD | 3,780,000.00 USD | 87,190.00 USD | 0.00 USD | 96,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.10` | 10,920,000.00 USD | 10,920,000.00 USD | 593,240.00 USD | 0.00 USD | 210,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4165.60` | 4,060,000.00 USD | 4,060,000.00 USD | 190,490.00 USD | 0.00 USD | 89,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.50` | 11,400,000.00 USD | 11,400,000.00 USD | 401,230.00 USD | 0.00 USD | 82,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4169.80` | 4,120,000.00 USD | 4,120,000.00 USD | 35,100.00 USD | 0.00 USD | 25,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4173.90` | 11,640,000.00 USD | 11,640,000.00 USD | 156,630.00 USD | 0.00 USD | 77,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4174.00` | 4,250,000.00 USD | 4,250,000.00 USD | 90,290.00 USD | 0.00 USD | 37,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4178.20` | 4,350,000.00 USD | 4,350,000.00 USD | 85,070.00 USD | 0.00 USD | 19,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.30` | 11,900,000.00 USD | 11,900,000.00 USD | 233,200.00 USD | 0.00 USD | 28,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4182.40` | 4,510,000.00 USD | 4,510,000.00 USD | 136,450.00 USD | 0.00 USD | 24,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.70` | 12,090,000.00 USD | 12,090,000.00 USD | 143,730.00 USD | 0.00 USD | 50,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4186.60` | 4,760,000.00 USD | 4,760,000.00 USD | 207,850.00 USD | 0.00 USD | 34,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4187.10` | 12,370,000.00 USD | 12,370,000.00 USD | 219,060.00 USD | 0.00 USD | 54,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4190.80` | 4,870,000.00 USD | 4,870,000.00 USD | 101,180.00 USD | 0.00 USD | 15,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.50` | 12,670,000.00 USD | 12,670,000.00 USD | 271,340.00 USD | 0.00 USD | 33,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4195.00` | 4,960,000.00 USD | 4,960,000.00 USD | 73,130.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.90` | 12,910,000.00 USD | 12,910,000.00 USD | 204,490.00 USD | 0.00 USD | 31,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4199.20` | 4,990,000.00 USD | 4,990,000.00 USD | 30,260.00 USD | 0.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4200.30` | 13,060,000.00 USD | 13,060,000.00 USD | 132,330.00 USD | 0.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4203.40` | 5,010,000.00 USD | 5,010,000.00 USD | 17,360.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.70` | 13,210,000.00 USD | 13,210,000.00 USD | 116,920.00 USD | 0.00 USD | 31,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4209.10` | 13,330,000.00 USD | 13,330,000.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4213.50` | 13,460,000.00 USD | 13,460,000.00 USD | 99,920.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4217.90` | 13,590,000.00 USD | 13,590,000.00 USD | 121,670.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4222.30` | 13,740,000.00 USD | 13,740,000.00 USD | 146,500.00 USD | 0.00 USD | 5,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4226.70` | 13,760,000.00 USD | 13,760,000.00 USD | 0.00 USD | 0.00 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4231.10` | 13,830,000.00 USD | 13,830,000.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4235.50` | 13,860,000.00 USD | 13,860,000.00 USD | 34,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4379.80` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4380.70` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4388.20` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4389.50` | 13,890,000.00 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4392.40` | 5,050,000.00 USD | 5,050,000.00 USD | 18,160.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4393.90` | 13,940,000.00 USD | 13,940,000.00 USD | 27,620.00 USD | 0.00 USD | 16,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4396.60` | 5,090,000.00 USD | 5,090,000.00 USD | 16,880.00 USD | 0.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4398.30` | 14,070,000.00 USD | 14,070,000.00 USD | 117,750.00 USD | 0.00 USD | 17,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4400.80` | 5,140,000.00 USD | 5,140,000.00 USD | 26,650.00 USD | 0.00 USD | 22,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4402.70` | 14,280,000.00 USD | 14,280,000.00 USD | 153,810.00 USD | 0.00 USD | 59,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4405.00` | 5,220,000.00 USD | 5,220,000.00 USD | 51,120.00 USD | 0.00 USD | 34,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4407.10` | 14,440,000.00 USD | 14,440,000.00 USD | 115,090.00 USD | 0.00 USD | 43,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.50` | 14,550,000.00 USD | 14,550,000.00 USD | 78,400.00 USD | 0.00 USD | 24,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4415.90` | 14,600,000.00 USD | 14,600,000.00 USD | 36,920.00 USD | 0.00 USD | 15,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4420.30` | 14,690,000.00 USD | 14,690,000.00 USD | 84,770.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4424.70` | 14,740,000.00 USD | 14,740,000.00 USD | 34,880.00 USD | 0.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4429.10` | 14,790,000.00 USD | 14,790,000.00 USD | 37,690.00 USD | 0.00 USD | 16,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4433.40` | 14,890,000.00 USD | 14,890,000.00 USD | 88,510.00 USD | 0.00 USD | 8,450.00 USD | `Tier 1 CEX` |

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
| `1D` | `3581.80` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `3584.30` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `3586.00` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD |
| `7D` | `3588.70` | 15,070,000.00 USD | 0.00 USD | 15,070,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3590.20` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD |
| `7D` | `3593.10` | 15,050,000.00 USD | 0.00 USD | 15,050,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `3594.40` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 28,070.00 USD | 0.00 USD | 13,740.00 USD |
| `7D` | `3597.50` | 15,040,000.00 USD | 0.00 USD | 15,040,000.00 USD | 99,580.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `3598.60` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 14,150.00 USD | 0.00 USD | 10,820.00 USD |
| `7D` | `3601.90` | 14,920,000.00 USD | 0.00 USD | 14,920,000.00 USD | 182,840.00 USD | 0.00 USD | 69,870.00 USD |
| `1D` | `3602.80` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 36,990.00 USD | 0.00 USD | 47,700.00 USD |
| `7D` | `3606.30` | 14,670,000.00 USD | 0.00 USD | 14,670,000.00 USD | 152,940.00 USD | 0.00 USD | 52,040.00 USD |
| `1D` | `3607.00` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 48,270.00 USD | 0.00 USD | 11,730.00 USD |
| `7D` | `3610.70` | 14,460,000.00 USD | 0.00 USD | 14,460,000.00 USD | 72,480.00 USD | 0.00 USD | 25,660.00 USD |
| `1D` | `3611.20` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 25,560.00 USD | 0.00 USD | 6,310.00 USD |
| `7D` | `3615.10` | 14,360,000.00 USD | 0.00 USD | 14,360,000.00 USD | 76,990.00 USD | 0.00 USD | 15,340.00 USD |
| `1D` | `3615.40` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 31,290.00 USD | 0.00 USD | 10,040.00 USD |
| `7D` | `3619.50` | 14,270,000.00 USD | 0.00 USD | 14,270,000.00 USD | 45,440.00 USD | 0.00 USD | 15,200.00 USD |
| `1D` | `3619.60` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 42,080.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3623.80` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 61,240.00 USD | 0.00 USD | 8,000.00 USD |
| `7D` | `3623.90` | 14,210,000.00 USD | 0.00 USD | 14,210,000.00 USD | 55,480.00 USD | 0.00 USD | 21,610.00 USD |
| `1D` | `3628.00` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 28,780.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `3628.30` | 14,130,000.00 USD | 0.00 USD | 14,130,000.00 USD | 78,160.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3632.20` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 10,830.00 USD | 0.00 USD | 3,800.00 USD |
| `7D` | `3632.70` | 14,040,000.00 USD | 0.00 USD | 14,040,000.00 USD | 65,870.00 USD | 0.00 USD | 7,710.00 USD |
| `1D` | `3636.40` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 11,520.00 USD | 0.00 USD | 204.34 USD |
| `7D` | `3637.10` | 13,970,000.00 USD | 0.00 USD | 13,970,000.00 USD | 25,300.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `3641.50` | 13,940,000.00 USD | 0.00 USD | 13,940,000.00 USD | 45,790.00 USD | 0.00 USD | 13,010.00 USD |
| `7D` | `3645.90` | 13,880,000.00 USD | 0.00 USD | 13,880,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `7D` | `3650.30` | 13,850,000.00 USD | 0.00 USD | 13,850,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD |
| `7D` | `3654.70` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD |
| `7D` | `3659.10` | 13,770,000.00 USD | 0.00 USD | 13,770,000.00 USD | 6,820.00 USD | 0.00 USD | 4,810.00 USD |
| `7D` | `3663.50` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 12,530.00 USD | 0.00 USD | 4,250.00 USD |
| `7D` | `3667.90` | 13,740,000.00 USD | 0.00 USD | 13,740,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3821.20` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD |
| `7D` | `3821.90` | 13,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD |
| `1D` | `3825.40` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD |
| `1D` | `3829.60` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `3830.70` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 0.00 USD | 0.00 USD | 84,860.00 USD |
| `1D` | `3833.80` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 81,530.00 USD | 0.00 USD | 30,910.00 USD |
| `7D` | `3835.10` | 13,620,000.00 USD | 0.00 USD | 13,620,000.00 USD | 69,040.00 USD | 0.00 USD | 58,110.00 USD |
| `1D` | `3838.00` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 38,960.00 USD | 0.00 USD | 71,270.00 USD |
| `7D` | `3839.50` | 13,490,000.00 USD | 0.00 USD | 13,490,000.00 USD | 396,580.00 USD | 0.00 USD | 91,350.00 USD |
| `1D` | `3842.20` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 93,750.00 USD | 0.00 USD | 109,220.00 USD |
| `7D` | `3843.90` | 13,000,000.00 USD | 0.00 USD | 13,000,000.00 USD | 597,060.00 USD | 0.00 USD | 208,140.00 USD |
| `1D` | `3846.40` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 180,250.00 USD | 0.00 USD | 87,750.00 USD |
| `7D` | `3848.30` | 12,200,000.00 USD | 0.00 USD | 12,200,000.00 USD | 436,120.00 USD | 0.00 USD | 112,720.00 USD |
| `1D` | `3850.60` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 41,090.00 USD | 0.00 USD | 31,860.00 USD |
| `7D` | `3852.70` | 11,650,000.00 USD | 0.00 USD | 11,650,000.00 USD | 228,280.00 USD | 0.00 USD | 74,580.00 USD |
| `1D` | `3854.80` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 109,230.00 USD | 0.00 USD | 31,990.00 USD |
| `7D` | `3857.10` | 11,350,000.00 USD | 0.00 USD | 11,350,000.00 USD | 233,200.00 USD | 0.00 USD | 38,880.00 USD |
| `1D` | `3859.00` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 125,320.00 USD | 0.00 USD | 20,940.00 USD |
| `7D` | `3861.50` | 11,070,000.00 USD | 0.00 USD | 11,070,000.00 USD | 174,990.00 USD | 0.00 USD | 58,530.00 USD |
| `1D` | `3863.20` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 136,260.00 USD | 0.00 USD | 32,630.00 USD |
| `7D` | `3865.90` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 261,040.00 USD | 0.00 USD | 62,040.00 USD |
| `1D` | `3867.40` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 182,060.00 USD | 0.00 USD | 22,760.00 USD |
| `7D` | `3870.30` | 10,520,000.00 USD | 0.00 USD | 10,520,000.00 USD | 226,450.00 USD | 0.00 USD | 32,730.00 USD |
| `1D` | `3871.60` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 109,480.00 USD | 0.00 USD | 12,540.00 USD |
| `7D` | `3874.70` | 10,260,000.00 USD | 0.00 USD | 10,260,000.00 USD | 224,270.00 USD | 0.00 USD | 25,440.00 USD |
| `1D` | `3875.80` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 28,070.00 USD | 0.00 USD | 5,810.00 USD |
| `7D` | `3879.10` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 122,020.00 USD | 0.00 USD | 18,000.00 USD |
| `1D` | `3880.00` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 30,410.00 USD | 0.00 USD | 813.93 USD |
| `7D` | `3883.50` | 9,870,000.00 USD | 0.00 USD | 9,870,000.00 USD | 161,950.00 USD | 0.00 USD | 36,870.00 USD |
| `7D` | `3887.90` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 87,390.00 USD | 0.00 USD | 32,570.00 USD |
| `7D` | `3892.30` | 9,550,000.00 USD | 0.00 USD | 9,550,000.00 USD | 104,620.00 USD | 0.00 USD | 12,530.00 USD |
| `7D` | `3896.70` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD |
| `1D` | `3901.00` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `3901.10` | 9,310,000.00 USD | 0.00 USD | 9,310,000.00 USD | 73,850.00 USD | 0.00 USD | 75,240.00 USD |
| `1D` | `3905.20` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD |
| `7D` | `3905.50` | 9,160,000.00 USD | 0.00 USD | 9,160,000.00 USD | 55,280.00 USD | 0.00 USD | 15,640.00 USD |
| `1D` | `3909.40` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD |
| `7D` | `3909.90` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 34,960.00 USD | 0.00 USD | 162,420.00 USD |
| `1D` | `3913.60` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 163,060.00 USD | 0.00 USD | 61,830.00 USD |
| `7D` | `3914.30` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 138,080.00 USD | 0.00 USD | 40,680.00 USD |
| `1D` | `3917.80` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 55,700.00 USD | 0.00 USD | 142,540.00 USD |
| `7D` | `3918.70` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 763,340.00 USD | 0.00 USD | 199,970.00 USD |
| `1D` | `3922.00` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 187,870.00 USD | 0.00 USD | 206,230.00 USD |
| `7D` | `3923.10` | 7,750,000.00 USD | 0.00 USD | 7,750,000.00 USD | 1,120,000.00 USD | 0.00 USD | 399,510.00 USD |
| `1D` | `3926.20` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 382,350.00 USD | 0.00 USD | 187,710.00 USD |
| `7D` | `3927.50` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 844,290.00 USD | 0.00 USD | 266,230.00 USD |
| `1D` | `3930.40` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 40,700.00 USD | 0.00 USD | 46,870.00 USD |
| `7D` | `3931.90` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 586,550.00 USD | 0.00 USD | 170,010.00 USD |
| `1D` | `3934.60` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 237,090.00 USD | 0.00 USD | 75,970.00 USD |
| `7D` | `3936.30` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 418,330.00 USD | 0.00 USD | 95,350.00 USD |
| `1D` | `3938.80` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 215,190.00 USD | 0.00 USD | 39,310.00 USD |
| `7D` | `3940.70` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 335,530.00 USD | 0.00 USD | 70,750.00 USD |
| `1D` | `3943.00` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 315,460.00 USD | 0.00 USD | 64,870.00 USD |
| `7D` | `3945.10` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 398,420.00 USD | 0.00 USD | 137,690.00 USD |
| `1D` | `3947.20` | 807,080.00 USD | 0.00 USD | 807,080.00 USD | 365,110.00 USD | 0.00 USD | 46,140.00 USD |
| `7D` | `3949.50` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 549,120.00 USD | 0.00 USD | 68,930.00 USD |
| `1D` | `3951.40` | 395,840.00 USD | 0.00 USD | 395,840.00 USD | 195,870.00 USD | 0.00 USD | 25,860.00 USD |
| `7D` | `3953.90` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 442,240.00 USD | 0.00 USD | 66,920.00 USD |
| `1D` | `3955.60` | 174,110.00 USD | 0.00 USD | 174,110.00 USD | 83,380.00 USD | 0.00 USD | 17,390.00 USD |
| `7D` | `3958.30` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 306,330.00 USD | 0.00 USD | 49,170.00 USD |
| `1D` | `3959.80` | 73,340.00 USD | 0.00 USD | 73,340.00 USD | 71,090.00 USD | 0.00 USD | 1,650.00 USD |
| `7D` | `3962.70` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 192,180.00 USD | 0.00 USD | 56,430.00 USD |
| `1D` | `3964.00` | 606.18 USD | 0.00 USD | 606.18 USD | 0.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `3967.10` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 249,290.00 USD | 0.00 USD | 57,880.00 USD |
| `7D` | `3971.50` | 863,560.00 USD | 0.00 USD | 863,560.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `3975.90` | 616,600.00 USD | 0.00 USD | 616,600.00 USD | 255,840.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `3980.30` | 347,370.00 USD | 0.00 USD | 347,370.00 USD | 232,530.00 USD | 0.00 USD | 4,280.00 USD |
| `7D` | `3984.70` | 110,560.00 USD | 0.00 USD | 110,560.00 USD | 59,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3989.10` | 50,730.00 USD | 0.00 USD | 50,730.00 USD | 50,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4001.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4001.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4060.60` | 19,400.00 USD | 19,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `4063.90` | 60,950.00 USD | 60,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD |
| `1D` | `4064.80` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD |
| `7D` | `4068.30` | 185,820.00 USD | 185,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 124,870.00 USD |
| `1D` | `4069.00` | 109,160.00 USD | 109,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD |
| `7D` | `4072.70` | 319,810.00 USD | 319,810.00 USD | 0.00 USD | 57,650.00 USD | 0.00 USD | 76,340.00 USD |
| `1D` | `4073.20` | 302,430.00 USD | 302,430.00 USD | 0.00 USD | 131,440.00 USD | 0.00 USD | 61,830.00 USD |
| `7D` | `4077.10` | 980,620.00 USD | 980,620.00 USD | 0.00 USD | 539,520.00 USD | 0.00 USD | 121,290.00 USD |
| `1D` | `4077.40` | 532,290.00 USD | 532,290.00 USD | 0.00 USD | 87,320.00 USD | 0.00 USD | 142,540.00 USD |
| `7D` | `4081.50` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 973,810.00 USD | 0.00 USD | 337,450.00 USD |
| `1D` | `4081.60` | 903,240.00 USD | 903,240.00 USD | 0.00 USD | 178,090.00 USD | 0.00 USD | 192,870.00 USD |
| `1D` | `4085.80` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 362,630.00 USD | 0.00 USD | 201,070.00 USD |
| `7D` | `4085.90` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 813,840.00 USD | 0.00 USD | 366,440.00 USD |
| `1D` | `4090.00` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 70,210.00 USD | 0.00 USD | 42,390.00 USD |
| `7D` | `4090.30` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 795,150.00 USD | 0.00 USD | 159,840.00 USD |
| `1D` | `4094.20` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 195,060.00 USD | 0.00 USD | 62,500.00 USD |
| `7D` | `4094.70` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 274,190.00 USD | 0.00 USD | 118,990.00 USD |
| `1D` | `4098.40` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 188,180.00 USD | 0.00 USD | 41,090.00 USD |
| `7D` | `4099.10` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 528,170.00 USD | 0.00 USD | 31,920.00 USD |
| `1D` | `4102.60` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 281,660.00 USD | 0.00 USD | 73,890.00 USD |
| `7D` | `4103.50` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD |
| `1D` | `4106.80` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 402,520.00 USD | 0.00 USD | 44,220.00 USD |
| `7D` | `4107.90` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD |
| `1D` | `4111.00` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 224,660.00 USD | 0.00 USD | 30,400.00 USD |
| `7D` | `4112.30` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 528,700.00 USD | 0.00 USD | 67,220.00 USD |
| `1D` | `4115.20` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 114,110.00 USD | 0.00 USD | 18,540.00 USD |
| `7D` | `4116.70` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 338,630.00 USD | 0.00 USD | 42,660.00 USD |
| `1D` | `4119.40` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 66,420.00 USD | 0.00 USD | 5,040.00 USD |
| `7D` | `4121.10` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 225,210.00 USD | 0.00 USD | 36,010.00 USD |
| `1D` | `4123.60` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `4125.50` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 342,730.00 USD | 0.00 USD | 61,080.00 USD |
| `7D` | `4129.90` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 125,300.00 USD | 0.00 USD | 56,200.00 USD |
| `7D` | `4134.30` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 195,250.00 USD | 0.00 USD | 39,940.00 USD |
| `7D` | `4138.70` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 219,810.00 USD | 0.00 USD | 13,380.00 USD |
| `1D` | `4140.40` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD |
| `7D` | `4143.10` | 9,040,000.00 USD | 9,040,000.00 USD | 0.00 USD | 232,530.00 USD | 0.00 USD | 47,230.00 USD |
| `1D` | `4144.60` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD |
| `7D` | `4147.50` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 91,570.00 USD |
| `1D` | `4148.80` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `4151.90` | 9,370,000.00 USD | 9,370,000.00 USD | 0.00 USD | 116,380.00 USD | 0.00 USD | 57,380.00 USD |
| `1D` | `4153.00` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 65,720.00 USD | 0.00 USD | 30,910.00 USD |
| `7D` | `4156.30` | 9,670,000.00 USD | 9,670,000.00 USD | 0.00 USD | 243,560.00 USD | 0.00 USD | 57,810.00 USD |
| `1D` | `4157.20` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 36,330.00 USD | 0.00 USD | 71,270.00 USD |
| `7D` | `4160.70` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 336,690.00 USD | 0.00 USD | 111,100.00 USD |
| `1D` | `4161.40` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 87,190.00 USD | 0.00 USD | 96,430.00 USD |
| `7D` | `4165.10` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 593,240.00 USD | 0.00 USD | 210,680.00 USD |
| `1D` | `4165.60` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 190,490.00 USD | 0.00 USD | 89,780.00 USD |
| `7D` | `4169.50` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 401,230.00 USD | 0.00 USD | 82,290.00 USD |
| `1D` | `4169.80` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 35,100.00 USD | 0.00 USD | 25,080.00 USD |
| `7D` | `4173.90` | 11,640,000.00 USD | 11,640,000.00 USD | 0.00 USD | 156,630.00 USD | 0.00 USD | 77,020.00 USD |
| `1D` | `4174.00` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 90,290.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4178.20` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 85,070.00 USD | 0.00 USD | 19,360.00 USD |
| `7D` | `4178.30` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 233,200.00 USD | 0.00 USD | 28,180.00 USD |
| `1D` | `4182.40` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 136,450.00 USD | 0.00 USD | 24,010.00 USD |
| `7D` | `4182.70` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 143,730.00 USD | 0.00 USD | 50,750.00 USD |
| `1D` | `4186.60` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 207,850.00 USD | 0.00 USD | 34,560.00 USD |
| `7D` | `4187.10` | 12,370,000.00 USD | 12,370,000.00 USD | 0.00 USD | 219,060.00 USD | 0.00 USD | 54,620.00 USD |
| `1D` | `4190.80` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 101,180.00 USD | 0.00 USD | 15,740.00 USD |
| `7D` | `4191.50` | 12,670,000.00 USD | 12,670,000.00 USD | 0.00 USD | 271,340.00 USD | 0.00 USD | 33,750.00 USD |
| `1D` | `4195.00` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 73,130.00 USD | 0.00 USD | 8,890.00 USD |
| `7D` | `4195.90` | 12,910,000.00 USD | 12,910,000.00 USD | 0.00 USD | 204,490.00 USD | 0.00 USD | 31,470.00 USD |
| `1D` | `4199.20` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD | 5,050.00 USD |
| `7D` | `4200.30` | 13,060,000.00 USD | 13,060,000.00 USD | 0.00 USD | 132,330.00 USD | 0.00 USD | 19,440.00 USD |
| `1D` | `4203.40` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 17,360.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `4204.70` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 116,920.00 USD | 0.00 USD | 31,390.00 USD |
| `7D` | `4209.10` | 13,330,000.00 USD | 13,330,000.00 USD | 0.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD |
| `7D` | `4213.50` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 99,920.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `4217.90` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 121,670.00 USD | 0.00 USD | 12,340.00 USD |
| `7D` | `4222.30` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 146,500.00 USD | 0.00 USD | 5,460.00 USD |
| `7D` | `4226.70` | 13,760,000.00 USD | 13,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,320.00 USD |
| `7D` | `4231.10` | 13,830,000.00 USD | 13,830,000.00 USD | 0.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD |
| `7D` | `4235.50` | 13,860,000.00 USD | 13,860,000.00 USD | 0.00 USD | 34,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4379.80` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,650.00 USD |
| `7D` | `4380.70` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `4388.20` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD |
| `7D` | `4389.50` | 13,890,000.00 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,120.00 USD |
| `1D` | `4392.40` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 18,160.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `4393.90` | 13,940,000.00 USD | 13,940,000.00 USD | 0.00 USD | 27,620.00 USD | 0.00 USD | 16,570.00 USD |
| `1D` | `4396.60` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 16,880.00 USD | 0.00 USD | 15,860.00 USD |
| `7D` | `4398.30` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 117,750.00 USD | 0.00 USD | 17,130.00 USD |
| `1D` | `4400.80` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 26,650.00 USD | 0.00 USD | 22,410.00 USD |
| `7D` | `4402.70` | 14,280,000.00 USD | 14,280,000.00 USD | 0.00 USD | 153,810.00 USD | 0.00 USD | 59,890.00 USD |
| `1D` | `4405.00` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 51,120.00 USD | 0.00 USD | 34,900.00 USD |
| `7D` | `4407.10` | 14,440,000.00 USD | 14,440,000.00 USD | 0.00 USD | 115,090.00 USD | 0.00 USD | 43,280.00 USD |
| `7D` | `4411.50` | 14,550,000.00 USD | 14,550,000.00 USD | 0.00 USD | 78,400.00 USD | 0.00 USD | 24,920.00 USD |
| `7D` | `4415.90` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 36,920.00 USD | 0.00 USD | 15,620.00 USD |
| `7D` | `4420.30` | 14,690,000.00 USD | 14,690,000.00 USD | 0.00 USD | 84,770.00 USD | 0.00 USD | 3,450.00 USD |
| `7D` | `4424.70` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 34,880.00 USD | 0.00 USD | 18,300.00 USD |
| `7D` | `4429.10` | 14,790,000.00 USD | 14,790,000.00 USD | 0.00 USD | 37,690.00 USD | 0.00 USD | 16,270.00 USD |
| `7D` | `4433.40` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 88,510.00 USD | 0.00 USD | 8,450.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `275.62M` | Total OI Tokens: `68,876.9 PAXG`
  * 1h OI Change: `+0.01%` | 4h OI Change: `-0.21%` | 24h OI Change: `+0.13%`
  * Exchange Breakdown: Binance=`105.43M` | Bybit=`24.16M` | OKX=`-` | Hyperliquid=`24.65M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.81K` | Last 24h: `17.74K` | Last 3d: `85.70K` | Last 7d: `216.77K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0016%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0050%` | **USDT KuCoin** | `0.0050%` |
| **USDT MEXC** | `0.0015%` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0177%` | **USDT Bitget** | `0.0045%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `PAXG` | `56.58%` | `43.42%` | `1.30` | 2,640,000.00 USD |
| `15M` | `Binance` | `49.36%` | `50.64%` | `0.97` | 1,010,000.00 USD |
| `15M` | `OKX` | `52.29%` | `47.71%` | `1.10` | 407,910.00 USD |
| `15M` | `Bybit` | `69.17%` | `30.83%` | `2.24` | 340,180.00 USD |
| `15M` | `KuCoin` | `55.08%` | `44.92%` | `1.23` | 53,720.00 USD |
| `15M` | `Gate` | `64.36%` | `35.64%` | `1.81` | 79,740.00 USD |
| `15M` | `Bitget` | `59.23%` | `40.77%` | `1.45` | 323,260.00 USD |
| `15M` | `BingX` | `72.58%` | `27.42%` | `2.65` | 51,960.00 USD |
| `15M` | `MEXC` | `67.71%` | `32.29%` | `2.10` | 141,140.00 USD |
| `15M` | `Bitunix` | `53.53%` | `46.47%` | `1.15` | 37,100.00 USD |
| `15M` | `Hyperliquid` | `41.15%` | `58.85%` | `0.70` | 30,900.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.96%` | `48.04%` | `1.08` | 25,520.00 USD |
| `15M` | `Crypto.com` | `49.27%` | `50.73%` | `0.97` | 950.57 USD |
| `15M` | `WhiteBIT` | `68%` | `32%` | `2.12` | 103,670.00 USD |
| `15M` | `HTX` | `0.91%` | `99.09%` | `0.01` | 359.63 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `71.98%` | `28.02%` | `2.57` | 28,490.00 USD |
| `15M` | `Aster` | `58.59%` | `41.41%` | `1.41` | 608.59 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `97.65%` | `2.35%` | `41.55` | 2,130.00 USD |
| `15M` | `Whale Positions` | `49.36%` | `50.64%` | `0.97` | 1,010,000.00 USD |
| `15M` | `Global Accounts` | `56.58%` | `43.42%` | `1.30` | 2,640,000.00 USD |
| `1H` | `PAXG` | `55.95%` | `44.05%` | `1.27` | 11,040,000.00 USD |
| `1H` | `Binance` | `56.34%` | `43.66%` | `1.29` | 6,440,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `76.84%` | `23.16%` | `3.32` | 1,010,000.00 USD |
| `1H` | `KuCoin` | `45.42%` | `54.58%` | `0.83` | 535,910.00 USD |
| `1H` | `Gate` | `46.04%` | `53.96%` | `0.85` | 455,110.00 USD |
| `1H` | `Bitget` | `56.05%` | `43.95%` | `1.28` | 1,470,000.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `51.44%` | `48.56%` | `1.06` | 41,970.00 USD |
| `1H` | `Bitunix` | `61.22%` | `38.78%` | `1.58` | 219,600.00 USD |
| `1H` | `Hyperliquid` | `51.42%` | `48.58%` | `1.06` | 293,800.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `9.57%` | `90.43%` | `0.11` | 381,140.00 USD |
| `1H` | `HTX` | `50.09%` | `49.91%` | `1.00` | 22,620.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `93.92%` | `6.08%` | `15.45` | 35,370.00 USD |
| `1H` | `Aster` | `71.51%` | `28.49%` | `2.51` | 99,370.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `99.48%` | `0.52%` | `191.31` | 38,180.00 USD |
| `1H` | `Whale Positions` | `56.34%` | `43.66%` | `1.29` | 6,440,000.00 USD |
| `1H` | `Global Accounts` | `55.95%` | `44.05%` | `1.27` | 11,040,000.00 USD |
| `4H` | `PAXG` | `49.33%` | `50.67%` | `0.97` | 39,110,000.00 USD |
| `4H` | `Binance` | `49.83%` | `50.17%` | `0.99` | 22,900,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `57.37%` | `42.63%` | `1.35` | 4,230,000.00 USD |
| `4H` | `KuCoin` | `49.27%` | `50.73%` | `0.97` | 2,150,000.00 USD |
| `4H` | `Gate` | `43.83%` | `56.17%` | `0.78` | 1,600,000.00 USD |
| `4H` | `Bitget` | `49.05%` | `50.95%` | `0.96` | 4,480,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `41.08%` | `58.92%` | `0.70` | 388,390.00 USD |
| `4H` | `Bitunix` | `52.48%` | `47.52%` | `1.10` | 765,180.00 USD |
| `4H` | `Hyperliquid` | `56.2%` | `43.8%` | `1.28` | 968,570.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `12.85%` | `87.15%` | `0.15` | 1,160,000.00 USD |
| `4H` | `HTX` | `27.06%` | `72.94%` | `0.37` | 147,770.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `89.38%` | `10.62%` | `8.42` | 37,170.00 USD |
| `4H` | `Aster` | `50.74%` | `49.26%` | `1.03` | 160,840.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `71.84%` | `28.16%` | `2.55` | 132,060.00 USD |
| `4H` | `Whale Positions` | `49.83%` | `50.17%` | `0.99` | 22,900,000.00 USD |
| `4H` | `Global Accounts` | `49.33%` | `50.67%` | `0.97` | 39,110,000.00 USD |


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
| `5m` | 27,090.00 USD | 8,020.00 USD | **`ACCUMULATION`** |
| `15m` | -33,210.00 USD | 610,100.00 USD | **`ACCUMULATION`** |
| `30m` | -180,280.00 USD | 685,830.00 USD | **`ACCUMULATION`** |
| `1h` | -329,300.00 USD | 1,300,000.00 USD | **`ACCUMULATION`** |
| `2h` | -1,050,000.00 USD | -94,630.00 USD | **`DISTRIBUTION`** |
| `4h` | 559,360.00 USD | 523,000.00 USD | **`ACCUMULATION`** |
| `6h` | 419,670.00 USD | 253,640.00 USD | **`ACCUMULATION`** |
| `8h` | 266,210.00 USD | -642,150.00 USD | **`DISTRIBUTION`** |
| `12h` | -606,130.00 USD | -426,840.00 USD | **`DISTRIBUTION`** |
| `24h` | -777,340.00 USD | 547,020.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,370,000.00 USD | -8,910,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,810,000.00 USD | -71,550,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+27.09K` | 15m=`-33.21K` | 1h=`-329.30K` | 24h=`-777.34K`
* Futures Capital Netflows: 5m=`+8.02K` | 15m=`+610.10K` | 1h=`+1.30M` | 24h=`+547.02K`
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
  * `2026-10-30 14:09:50 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:50:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:31:50 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3988.38` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3978.26` (Risk Distance: `10.12` pts)
  * +2.5R Take Profit: `4013.69`
  * Mathematical Lot Sizing: **`0.98 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4013.45` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4023.57` (Risk Distance: `10.12` pts)
  * +2.5R Take Profit: `3988.14`
  * Mathematical Lot Sizing: **`0.98 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4028.10`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
