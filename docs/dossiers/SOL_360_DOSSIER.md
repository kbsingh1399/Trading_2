# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 11:47:32 IST` (`2026-10-30 06:17:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `97.68` | **Live Ask Quote**: `97.91` | **Mid Price**: `97.80`
- **Spread Points**: `23.00` | **Spread BPS**: `23.52 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `0.01 USD` | Point Value (0.01 Lot): `0.0001 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `95.08` | VWAP Z-Score: `+1.66` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.7600` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `61.93` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `99.75` | Lower -3.00σ Band: `90.42`
  * Upper +2.51σ Band: `98.98` | Lower -2.51σ Band: `91.18`
  * Upper +2.01σ Band: `98.21` | Lower -2.01σ Band: `91.96`
  * Upper +2.00σ Band: `98.19` | Lower -2.00σ Band: `91.98`
  * Upper +1.28σ Band: `97.07` | Lower -1.28σ Band: `93.10`
  * Upper +1.00σ Band: `96.64` | Lower -1.00σ Band: `93.53`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`97.17` | EMA-20=`96.57` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`97.05` (Slope: `+0.0000`) | EMA-100=`98.17`
  * Institutional Anchors: EMA-144=`98.74` | EMA-200=`99.21` (Slope: `-0.2906`) | EMA-233=`99.46`
- **Range Boundaries**: 24H High=`102.93` | 24H Low=`91.86` | Weekly High=`103.63` | Weekly Low=`91.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `97.79` (Distance: `+0.06%`)
  * Point of Control (POC) = `96.85` (Distance: `+1.03%`)
  * Value Area Low (VAL) = `94.53` (Distance: `+3.50%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`101.56` | POC=`99.94` | VAL=`98.94`
  * Prior Day Extremes: PDH=`102.93` | PDL=`94.56` | PDC=`95.94`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`101.94` | Weekly POC=`100.92` | Weekly VAL=`99.51`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`97.84` | Low=`91.86`
  * London Session (08:00-16:00 UTC): High=`98.28` | Low=`96.72`
  * New York Session (13:00-21:00 UTC): High=`98.38` | Low=`97.21`
  * Initial Balance (First Hour): IB High=`98.28` | IB Low=`96.72`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `97.40` - `98.19`
  * Optimal Trade Entry (OTE 0.705): `97.99`
  * Structural Invalidation Anchor (0.786): `98.58`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `97.94` | `98.05` | `97.76` | `97.82` | `90,024` | 8,812,527.45 USD | -353,747.97 USD | `-4.01%` | -205,042,069.55 USD | `+0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `97.82` | `98.00` | `97.74` | `97.91` | `43,214` | 4,228,808.12 USD | -304,080.44 USD | `-7.19%` | -205,346,149.99 USD | `+0.20` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `97.92` | `98.04` | `97.82` | `98.03` | `20,712` | 2,028,746.00 USD | 241,779.89 USD | `+11.92%` | -205,104,370.10 USD | `+0.59` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `98.01` | `98.35` | `97.88` | `98.31` | `192,918` | 18,936,666.93 USD | -1,219,807.57 USD | `-6.44%` | -199,009,561.29 USD | `-0.51` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `98.31` | `98.54` | `97.83` | `97.94` | `230,185` | 22,589,286.35 USD | -5,678,760.28 USD | `-25.14%` | -204,688,321.58 USD | `-2.17` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `97.94` | `98.05` | `97.74` | `98.03` | `153,950` | 15,070,081.56 USD | -416,048.52 USD | `-2.76%` | -205,104,370.10 USD | `-0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `97.20` | `97.61` | `96.72` | `97.23` | `802,986` | 78,022,251.46 USD | -722,046.52 USD | `-0.93%` | -197,232,714.70 USD | `+0.50` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `97.22` | `98.54` | `97.20` | `97.94` | `855,763` | 83,816,641.16 USD | -6,649,350.04 USD | `-7.93%` | -203,882,064.74 USD | `+0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `97.94` | `98.05` | `97.74` | `98.03` | `153,950` | 15,070,081.56 USD | -416,048.52 USD | `-2.76%` | -204,298,113.26 USD | `+0.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `99.78` | `99.90` | `94.81` | `95.62` | `13,887,188` | 1,349,343,315.53 USD | -115,873,425.65 USD | `-8.59%` | -153,967,489.63 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -197,228,736.47 USD | `-0.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.54` | `96.72` | `98.03` | `1,812,780` | 176,916,964.60 USD | -7,779,454.65 USD | `-4.40%` | -205,008,191.12 USD | `+0.67` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -5,851,281.21 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -38,094,063.99 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `95.62` | `13,887,188` | 1,349,343,315.53 USD | -115,873,425.65 USD | `-8.59%` | -153,967,489.63 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -197,228,736.47 USD | `-0.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.54` | `96.72` | `98.03` | `1,812,780` | 176,916,964.60 USD | -7,779,454.65 USD | `-4.40%` | -205,008,191.12 USD | `+0.67` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`97.80`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `97.95` | `313.0600` | 30,665.79 USD | 573,247.07 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `97.95` | `40.8300` | 3,999.46 USD | 577,246.54 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.95` | `40.8300` | 3,999.42 USD | 581,245.96 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.95` | `40.8300` | 3,999.38 USD | 585,245.34 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.95` | `164.6000` | 16,122.73 USD | 601,368.07 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `97.95` | `48.4800` | 4,748.62 USD | 606,116.69 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `97.96` | `40.8300` | 3,999.87 USD | 366,761.52 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.96` | `290.3500` | 28,443.56 USD | 395,205.08 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `97.96` | `116.2500` | 11,388.08 USD | 406,593.16 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `97.96` | `164.6000` | 16,124.38 USD | 422,717.54 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `97.96` | `374.2200` | 36,658.59 USD | 459,376.13 USD | `7 orders` | `-0.01%` | `-` |
| `BID` | `97.96` | `726.9000` | 71,206.40 USD | 530,582.53 USD | `9 orders` | `-0.01%` | `-` |
| `BID` | `97.96` | `40.8300` | 3,999.63 USD | 534,582.15 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.96` | `40.8300` | 3,999.58 USD | 538,581.74 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.96` | `40.8300` | 3,999.54 USD | 542,581.28 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `97.97` | `84.1700` | 8,246.13 USD | 8,246.13 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `97.97` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 97.97` | `0.00%` | `-` |
| `BID` | `97.97` | `3279.8700` | 321,325.58 USD | 321,325.58 USD | `27 orders` | `-0.00%` | `-` |
| `BID` | `97.97` | `220.8200` | 21,633.29 USD | 342,958.88 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `97.97` | `40.8300` | 3,999.99 USD | 346,958.87 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `97.97` | `45.0600` | 4,414.35 USD | 351,373.22 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `97.97` | `116.2500` | 11,388.43 USD | 362,761.65 USD | `2 orders` | `-0.00%` | `-` |
| `ASK` | `97.98` | `165.2200` | 16,188.42 USD | 39,437.25 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.98` | `153.1200` | 15,002.70 USD | 23,248.83 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `97.99` | `123.9100` | 12,142.44 USD | 66,580.98 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `97.99` | `153.0900` | 15,001.29 USD | 54,438.54 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `98.00` | `0.5100` | 49.98 USD | 82,848.91 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `98.00` | `143.8600` | 14,098.28 USD | 82,798.93 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `98.00` | `21.3300` | 2,090.28 USD | 68,700.65 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `98.00` | `0.3000` | 29.40 USD | 66,610.38 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `98.01` | `0.1100` | 10.78 USD | 105,918.01 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `98.01` | `0.2000` | 19.60 USD | 105,907.23 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `98.01` | `111.2900` | 10,907.53 USD | 105,887.63 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `98.01` | `123.7800` | 12,131.18 USD | 94,980.10 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `98.02` | `123.9100` | 12,146.03 USD | 167,090.41 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `98.02` | `63.0100` | 6,176.37 USD | 154,944.38 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `98.02` | `130.9100` | 12,831.80 USD | 148,768.01 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `98.02` | `0.4000` | 39.21 USD | 135,936.21 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `98.02` | `123.6500` | 12,119.68 USD | 135,897.01 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `98.02` | `182.2100` | 17,859.31 USD | 123,777.33 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `98.03` | `0.2000` | 19.61 USD | 167,110.01 USD | `1 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `11` | `0x5b5d...c060` | `SHORT` | 68,205,154.22 USD | `696,120.13` | `94.33` | `97.98` | `327.78` | -2,536,888.00 USD | `-3.72%` | `7X Cross` |
| `20` | `0x9c6a...a4ed` | `LONG` | 53,897,041.78 USD | `550,087.69` | `80.86` | `97.98` | `68.18` | 9,418,055.39 USD | `+17.47%` | `20X Cross` |
| `49` | `0xb83d...6e36` | `SHORT` | 25,425,758.82 USD | `259,338.02` | `91.42` | `97.98` | `607.42` | -1,716,944.78 USD | `-6.75%` | `5X Cross` |
| `80` | `0x3dc9...54b0` | `SHORT` | 21,570,138.63 USD | `220,000.19` | `105.90` | `97.98` | `173.21` | 1,728,968.65 USD | `+8.02%` | `20X Cross` |
| `112` | `0x9c89...600e` | `LONG` | 18,567,357.64 USD | `189,472.50` | `115.21` | `97.98` | `34.97` | -3,261,657.62 USD | `-17.57%` | `20X Cross` |
| `119` | `0x4a20...3c26` | `LONG` | 17,642,160.00 USD | `180,000.00` | `106.43` | `97.98` | `68.94` | -1,516,118.71 USD | `-8.59%` | `20X Cross` |
| `161` | `0xecb6...2b00` | `SHORT` | 12,859,105.58 USD | `131,219.38` | `101.33` | `97.98` | `316.13` | 437,203.06 USD | `+3.40%` | `20X Cross` |
| `224` | `0xc63a...a3cd` | `LONG` | 9,801,200.00 USD | `100,000.00` | `112.22` | `97.98` | `0.000000` | -1,420,908.97 USD | `-14.50%` | `20X Cross` |
| `225` | `0xb581...6f4f` | `LONG` | 9,797,000.00 USD | `100,000.00` | `112.81` | `97.98` | `0.000000` | -1,483,709.14 USD | `-15.14%` | `3X Cross` |
| `290` | `0x645b...87b8` | `SHORT` | 8,121,125.49 USD | `82,879.96` | `103.90` | `97.98` | `354.45` | 490,344.74 USD | `+6.04%` | `20X Cross` |
| `294` | `0xdb3a...cf3b` | `LONG` | 8,025,051.36 USD | `81,851.78` | `106.04` | `97.98` | `44.88` | -654,695.49 USD | `-8.16%` | `4X Cross` |
| `309` | `0xe927...98ef` | `LONG` | 7,647,120.00 USD | `78,000.00` | `96.34` | `97.98` | `38.45` | 132,978.52 USD | `+1.74%` | `3X Cross` |
| `321` | `0xca49...53c8` | `SHORT` | 7,246,975.70 USD | `73,943.45` | `110.70` | `97.98` | `296.70` | 938,646.56 USD | `+12.95%` | `20X Cross` |
| `327` | `0x8ae4...3d60` | `LONG` | 7,073,644.90 USD | `72,180.05` | `111.72` | `97.98` | `10.33` | -990,515.34 USD | `-14.00%` | `10X Cross` |
| `330` | `0xa0b7...6165` | `SHORT` | 6,960,861.23 USD | `71,044.42` | `107.87` | `97.98` | `190.91` | 702,605.97 USD | `+10.09%` | `2X Cross` |
| `345` | `0xf517...c032` | `SHORT` | 6,645,257.86 USD | `67,778.53` | `84.64` | `97.98` | `226.06` | -908,226.70 USD | `-13.67%` | `20X Cross` |
| `363` | `0x7a5a...0394` | `SHORT` | 6,368,476.98 USD | `64,966.56` | `99.29` | `97.98` | `124.19` | 81,797.54 USD | `+1.28%` | `10X Cross` |
| `404` | `0x7fda...17d1` | `SHORT` | 5,522,377.90 USD | `56,347.92` | `100.53` | `97.98` | `759.98` | 142,489.79 USD | `+2.58%` | `20X Cross` |
| `465` | `0x7e23...5a5a` | `LONG` | 4,761,318.03 USD | `48,564.56` | `105.17` | `97.98` | `57.00` | -346,251.13 USD | `-7.27%` | `5X Isolated` |
| `564` | `0xf899...88db` | `SHORT` | 3,990,206.66 USD | `40,716.81` | `88.40` | `97.98` | `117.21` | -390,933.79 USD | `-9.80%` | `20X Cross` |
| `582` | `0x2e2b...2fab` | `LONG` | 3,921,640.00 USD | `40,000.00` | `119.55` | `97.98` | `57.91` | -860,395.64 USD | `-21.94%` | `10X Cross` |
| `610` | `0x9c16...4a6f` | `SHORT` | 3,704,621.70 USD | `37,796.13` | `90.79` | `97.98` | `118.06` | -273,270.97 USD | `-7.38%` | `20X Cross` |
| `638` | `0x27b8...12fc` | `LONG` | 3,536,185.03 USD | `36,085.73` | `110.86` | `97.98` | `22.30` | -464,160.23 USD | `-13.13%` | `10X Cross` |
| `643` | `0x9946...0852` | `SHORT` | 3,488,891.62 USD | `35,590.04` | `111.00` | `97.98` | `140.32` | 461,695.13 USD | `+13.23%` | `20X Cross` |
| `653` | `0x3440...32c5` | `SHORT` | 3,447,741.57 USD | `35,170.27` | `95.02` | `97.98` | `160.54` | -105,818.51 USD | `-3.07%` | `20X Cross` |
| `667` | `0xa61c...66b9` | `LONG` | 3,376,503.45 USD | `34,438.76` | `102.78` | `97.98` | `0.000000` | -162,957.86 USD | `-4.83%` | `5X Cross` |
| `729` | `0x96a7...79df` | `LONG` | 3,137,280.00 USD | `32,000.00` | `74.39` | `97.98` | `0.000000` | 756,874.15 USD | `+24.13%` | `20X Cross` |
| `773` | `0xbe19...8bd1` | `SHORT` | 2,985,087.82 USD | `30,451.69` | `97.62` | `97.98` | `753.55` | -12,541.19 USD | `-0.42%` | `3X Cross` |
| `774` | `0x482b...cae4` | `SHORT` | 2,970,791.75 USD | `30,310.49` | `88.03` | `97.98` | `155.57` | -302,543.46 USD | `-10.18%` | `20X Cross` |
| `777` | `0x023a...2355` | `SHORT` | 2,963,126.48 USD | `30,223.34` | `101.18` | `97.98` | `268.40` | 94,745.66 USD | `+3.20%` | `20X Cross` |
| `785` | `0x610b...b613` | `LONG` | 2,905,508.89 USD | `29,634.14` | `101.23` | `97.98` | `70.39` | -94,490.46 USD | `-3.25%` | `3X Isolated` |
| `794` | `0x45d2...4029` | `SHORT` | 2,863,852.20 USD | `29,220.00` | `93.28` | `97.98` | `1521.19` | -138,076.22 USD | `-4.82%` | `20X Cross` |
| `846` | `0x458d...ab3b` | `LONG` | 2,684,828.34 USD | `27,385.03` | `117.17` | `97.98` | `81.08` | -523,834.18 USD | `-19.51%` | `3X Isolated` |
| `911` | `0x051c...693c` | `LONG` | 2,463,439.20 USD | `25,139.70` | `89.76` | `97.98` | `40.60` | 206,877.87 USD | `+8.40%` | `20X Cross` |
| `929` | `0xfc27...9d9d` | `SHORT` | 2,404,047.16 USD | `24,528.09` | `100.40` | `97.98` | `819.91` | 58,465.98 USD | `+2.43%` | `20X Cross` |
| `946` | `0x638f...f5f0` | `LONG` | 2,352,168.00 USD | `24,000.00` | `136.71` | `97.98` | `49.35` | -928,800.54 USD | `-39.49%` | `20X Cross` |
| `991` | `0x7277...0b98` | `SHORT` | 2,232,147.33 USD | `22,770.74` | `99.32` | `97.98` | `156.64` | 29,456.43 USD | `+1.32%` | `20X Cross` |
| `998` | `0x7178...0854` | `LONG` | 2,209,131.41 USD | `22,545.24` | `110.94` | `97.98` | `38.22` | -292,013.06 USD | `-13.22%` | `10X Cross` |
| `1019` | `0x69cc...14fd` | `SHORT` | 2,127,404.91 USD | `21,701.57` | `99.01` | `97.98` | `463.47` | 21,247.84 USD | `+1.00%` | `20X Cross` |
| `1026` | `0x739c...cfb2` | `LONG` | 2,107,989.00 USD | `21,500.00` | `91.95` | `97.98` | `73.72` | 131,056.85 USD | `+6.22%` | `20X Cross` |
| `1090` | `0x7737...bf66` | `SHORT` | 1,997,364.73 USD | `20,384.06` | `102.94` | `97.98` | `956.88` | 100,977.16 USD | `+5.06%` | `10X Cross` |
| `1126` | `0xea00...a918` | `LONG` | 1,963,144.66 USD | `20,022.69` | `66.09` | `97.98` | `0.000000` | 639,836.06 USD | `+32.59%` | `20X Cross` |
| `1127` | `0x3fc5...c0c1` | `SHORT` | 1,960,920.00 USD | `20,000.00` | `98.28` | `97.98` | `178.21` | 4,639.84 USD | `+0.24%` | `20X Cross` |
| `1128` | `0x251f...6e5d` | `LONG` | 1,960,874.00 USD | `20,000.00` | `101.15` | `97.98` | `65.93` | -62,223.77 USD | `-3.17%` | `20X Cross` |
| `1130` | `0xbfc7...80b4` | `SHORT` | 1,959,732.00 USD | `20,000.00` | `85.98` | `97.98` | `172.37` | -240,197.50 USD | `-12.26%` | `20X Cross` |
| `1149` | `0x936c...bb0f` | `SHORT` | 1,927,213.57 USD | `19,664.04` | `105.57` | `97.98` | `506.66` | 148,748.61 USD | `+7.72%` | `20X Cross` |
| `1161` | `0x7160...d47c` | `LONG` | 1,905,391.07 USD | `19,434.10` | `105.03` | `97.98` | `75.23` | -135,830.22 USD | `-7.13%` | `20X Cross` |
| `1194` | `0xe097...d0fe` | `LONG` | 1,861,885.53 USD | `18,995.75` | `109.71` | `97.98` | `0.000000` | -222,111.36 USD | `-11.93%` | `20X Cross` |
| `1267` | `0xdf95...7d72` | `SHORT` | 1,744,414.29 USD | `17,802.58` | `104.53` | `97.98` | `2248.63` | 116,542.57 USD | `+6.68%` | `20X Cross` |
| `1275` | `0xe98b...8cd5` | `SHORT` | 1,726,673.14 USD | `17,622.89` | `187.95` | `97.98` | `261.88` | 1,585,547.58 USD | `+91.83%` | `20X Cross` |
| `1306` | `0xee2b...d67e` | `LONG` | 1,663,133.91 USD | `16,963.19` | `119.86` | `97.98` | `30.81` | -370,137.73 USD | `-22.26%` | `4X Cross` |
| `1308` | `0x123d...3bff` | `LONG` | 1,658,163.14 USD | `16,920.55` | `89.54` | `97.98` | `0.000000` | 143,169.39 USD | `+8.63%` | `10X Cross` |
| `1406` | `0x73d7...8be1` | `LONG` | 1,535,806.24 USD | `15,668.95` | `106.60` | `97.98` | `47.69` | -134,534.73 USD | `-8.76%` | `20X Cross` |
| `1424` | `0xc74a...ab93` | `LONG` | 1,522,400.17 USD | `15,536.82` | `64.06` | `97.98` | `54.89` | 527,171.33 USD | `+34.63%` | `5X Isolated` |
| `1466` | `0xb322...d51f` | `LONG` | 1,470,637.85 USD | `14,999.82` | `102.98` | `97.98` | `44.48` | -74,089.45 USD | `-5.04%` | `20X Cross` |
| `1467` | `0x5f10...d49d` | `LONG` | 1,470,405.00 USD | `15,000.00` | `96.35` | `97.98` | `70.71` | 25,103.84 USD | `+1.71%` | `20X Cross` |
| `1514` | `0xffb2...5ed6` | `LONG` | 1,420,961.78 USD | `14,504.05` | `117.89` | `97.98` | `85.40` | -288,942.93 USD | `-20.33%` | `20X Cross` |
| `1543` | `0x0d6a...ca57` | `LONG` | 1,392,905.21 USD | `14,206.65` | `110.41` | `97.98` | `91.60` | -175,685.15 USD | `-12.61%` | `5X Isolated` |
| `1738` | `0x5323...b23c` | `LONG` | 1,183,294.08 USD | `12,069.38` | `94.78` | `97.98` | `0.000000` | 39,354.72 USD | `+3.33%` | `5X Cross` |
| `1739` | `0x2814...9b08` | `LONG` | 1,182,239.36 USD | `12,061.71` | `96.37` | `97.98` | `93.93` | 19,900.62 USD | `+1.68%` | `20X Isolated` |
| `1814` | `0x7808...6e70` | `SHORT` | 1,125,838.97 USD | `11,488.27` | `97.15` | `97.98` | `151.16` | -9,776.75 USD | `-0.87%` | `10X Cross` |
| `1838` | `0x2482...0e55` | `LONG` | 1,114,135.96 USD | `11,363.98` | `122.03` | `97.98` | `88.83` | -272,565.96 USD | `-24.46%` | `20X Isolated` |
| `1864` | `0x45db...86eb` | `LONG` | 1,087,899.90 USD | `11,100.00` | `110.69` | `97.98` | `68.85` | -140,782.00 USD | `-12.94%` | `5X Cross` |
| `1891` | `0x1d04...7c43` | `LONG` | 1,059,325.43 USD | `10,811.76` | `111.55` | `97.98` | `16.49` | -146,736.06 USD | `-13.85%` | `6X Cross` |
| `1910` | `0x34e6...8d74` | `LONG` | 1,045,847.40 USD | `10,671.15` | `101.19` | `97.98` | `15.56` | -33,927.24 USD | `-3.24%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `100.96` | 6,720.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 6.72K USD at 100.9600 USD [API] | `2026-10-29 01:38:38` |
| `ANNOUNCEMENT` | `INFO` | `99.59` | 22,830.16 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 22.83K USD at 99.5950 USD [API] | `2026-10-29 03:39:17` |
| `ANNOUNCEMENT` | `INFO` | `66.74` | 98,718.18 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 98.72K USD at 66.7380 USD [API] | `2026-06-04 02:04:51` |
| `ANNOUNCEMENT` | `INFO` | `66.74` | 99,453.95 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 99.45K USD at 66.7400 USD [API] | `2026-06-04 02:04:51` |
| `ANNOUNCEMENT` | `INFO` | `66.74` | 96.11 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.10K USD at 66.7430 USD [API] | `2026-06-04 02:04:51` |
| `ANNOUNCEMENT` | `INFO` | `66.75` | 99,461.40 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 99.46K USD at 66.7450 USD [API] | `2026-06-04 02:04:51` |
| `ANNOUNCEMENT` | `INFO` | `66.75` | 166.87 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.17K USD at 66.7470 USD [API] | `2026-06-04 02:04:51` |
| `ANNOUNCEMENT` | `INFO` | `66.75` | 84,833.31 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 84.83K USD at 66.7490 USD [API] | `2026-06-04 02:04:51` |
| `ANNOUNCEMENT` | `INFO` | `67.08` | 14,650.93 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 14.65K USD at 67.0830 USD [API] | `2026-06-04 02:04:33` |
| `ANNOUNCEMENT` | `INFO` | `67.08` | 663.45 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.66K USD at 67.0830 USD [API] | `2026-06-04 02:04:33` |
| `ANNOUNCEMENT` | `INFO` | `67.08` | 663.46 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.66K USD at 67.0840 USD [API] | `2026-06-04 02:04:33` |
| `ANNOUNCEMENT` | `INFO` | `67.09` | 663.48 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.66K USD at 67.0860 USD [API] | `2026-06-04 02:04:33` |
| `ANNOUNCEMENT` | `INFO` | `67.09` | 663.50 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.66K USD at 67.0880 USD [API] | `2026-06-04 02:04:33` |
| `ANNOUNCEMENT` | `INFO` | `67.10` | 78,887.80 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 78.89K USD at 67.1020 USD [API] | `2026-06-04 02:04:33` |
| `ANNOUNCEMENT` | `INFO` | `67.54` | 2,413.20 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.41K USD at 67.5400 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.54` | 40,031.47 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 40.03K USD at 67.5420 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.54` | 664.62 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.66K USD at 67.5430 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.54` | 664.63 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.66K USD at 67.5440 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.55` | 1,253.64 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.25K USD at 67.5450 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.55` | 664.65 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.66K USD at 67.5460 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.55` | 5,844.43 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 5.84K USD at 67.5500 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.56` | 1,375.42 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.38K USD at 67.5550 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.57` | 262.85 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.26K USD at 67.5710 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.57` | 67,890.61 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 67.89K USD at 67.5710 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.92` | 3,330.26 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.33K USD at 67.9230 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.93` | 180.69 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.18K USD at 67.9270 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.93` | 96,159.56 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 96.16K USD at 67.9280 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.93` | 2,249.94 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.25K USD at 67.9330 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.93` | 49.59 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.05K USD at 67.9330 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.94` | 578.84 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.58K USD at 67.9390 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.94` | 416.49 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.42K USD at 67.9430 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.95` | 299.66 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.30K USD at 67.9500 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.95` | 11.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 67.9500 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.95` | 42.81 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.04K USD at 67.9500 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.95` | 1,161.98 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.16K USD at 67.9520 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.96` | 1,130.17 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.13K USD at 67.9600 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.96` | 19.71 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 67.9600 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.97` | 21.75 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 67.9700 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.97` | 377.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.38K USD at 67.9700 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.97` | 2,011.94 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.01K USD at 67.9710 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.98` | 1,137.24 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.14K USD at 67.9760 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.98` | 67.98 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.07K USD at 67.9800 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.99` | 190.36 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.19K USD at 67.9860 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.99` | 42,760.47 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 42.76K USD at 67.9860 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 3,761.65 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.76K USD at 68.4060 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 119,176.62 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 119.18K USD at 68.4070 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 19,940.93 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 19.94K USD at 68.4080 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 5,615.78 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 5.62K USD at 68.4100 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 15.05 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 68.4110 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 4,623.28 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.62K USD at 68.4120 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 410.48 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.41K USD at 68.4140 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 15.05 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 68.4140 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.42` | 28,938.08 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 28.94K USD at 68.4180 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.42` | 11.63 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 68.4180 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.42` | 5,688.44 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 5.69K USD at 68.4200 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.42` | 3,349.84 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.35K USD at 68.4200 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `99.65` | 27,695.61 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 27.70K USD at 99.6460 USD [API] | `2026-10-29 03:49:50` |
| `ANNOUNCEMENT` | `INFO` | `99.65` | 47,830.08 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 47.83K USD at 99.6460 USD [API] | `2026-10-29 03:49:50` |
| `ANNOUNCEMENT` | `INFO` | `99.56` | 26,848.61 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 26.85K USD at 99.5610 USD [API] | `2026-10-29 03:52:36` |
| `ANNOUNCEMENT` | `INFO` | `99.62` | 23,062.96 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 23.06K USD at 99.6240 USD [API] | `2026-10-29 03:58:36` |
| `ANNOUNCEMENT` | `INFO` | `100.37` | 105,923.47 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 105.92K USD at 100.3700 USD [API] | `2026-10-29 05:05:15` |
| `ANNOUNCEMENT` | `INFO` | `100.51` | 24,346.54 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 24.35K USD at 100.5100 USD [API] | `2026-10-29 05:07:49` |
| `ANNOUNCEMENT` | `INFO` | `138.54` | 7,909.25 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 7.91K USD at 138.5400 USD [API] | `2026-01-18 23:46:32` |
| `ANNOUNCEMENT` | `INFO` | `142.66` | 19,725.60 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 19.73K USD at 142.6600 USD [API] | `2026-01-15 15:25:17` |
| `ANNOUNCEMENT` | `INFO` | `120.55` | 2,728.05 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.73K USD at 120.5500 USD [API] | `2025-12-24 06:07:30` |
| `ANNOUNCEMENT` | `INFO` | `122.53` | 5,992.94 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 5.99K USD at 122.5300 USD [API] | `2025-12-23 14:38:40` |
| `ANNOUNCEMENT` | `INFO` | `128.41` | 8,136.06 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 8.14K USD at 128.4100 USD [API] | `2025-12-14 23:32:44` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 16,030.36 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 16.03K USD at 129.7900 USD [API] | `2025-12-07 14:24:22` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 13,999.15 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 14.00K USD at 129.7900 USD [API] | `2025-12-07 14:24:22` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 9,292.96 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 9.29K USD at 129.7900 USD [API] | `2025-12-07 14:24:22` |
| `ANNOUNCEMENT` | `INFO` | `139.31` | 983.53 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.98K USD at 139.3100 USD [API] | `2025-12-03 14:02:57` |
| `ANNOUNCEMENT` | `INFO` | `132.04` | 2,100.76 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.10K USD at 132.0400 USD [API] | `2025-11-19 17:19:49` |
| `ANNOUNCEMENT` | `INFO` | `136.22` | 934.47 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.93K USD at 136.2200 USD [API] | `2025-11-17 16:02:09` |
| `ANNOUNCEMENT` | `INFO` | `136.22` | 2,351.16 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.35K USD at 136.2200 USD [API] | `2025-11-17 16:02:09` |
| `ANNOUNCEMENT` | `INFO` | `136.23` | 1,219.26 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.22K USD at 136.2300 USD [API] | `2025-11-17 16:02:09` |
| `ANNOUNCEMENT` | `INFO` | `138.52` | 1,171.88 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.17K USD at 138.5200 USD [API] | `2025-11-16 01:01:11` |
| `ANNOUNCEMENT` | `INFO` | `138.52` | 8,254.41 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 8.25K USD at 138.5200 USD [API] | `2025-11-16 01:01:11` |
| `ANNOUNCEMENT` | `INFO` | `140.30` | 21,653.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 21.65K USD at 140.3000 USD [API] | `2025-11-14 04:38:28` |
| `ANNOUNCEMENT` | `INFO` | `158.03` | 8,694.81 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 8.69K USD at 158.0300 USD [API] | `2025-11-08 13:59:22` |
| `ANNOUNCEMENT` | `INFO` | `153.11` | 38,948.12 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 38.95K USD at 153.1100 USD [API] | `2025-11-07 11:10:41` |
| `ANNOUNCEMENT` | `INFO` | `156.71` | 8,258.62 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 8.26K USD at 156.7100 USD [API] | `2025-11-06 15:33:46` |
| `ANNOUNCEMENT` | `INFO` | `156.71` | 23,982.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 23.98K USD at 156.7100 USD [API] | `2025-11-06 15:33:46` |
| `ANNOUNCEMENT` | `INFO` | `156.71` | 52,425.76 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 52.43K USD at 156.7100 USD [API] | `2025-11-06 15:33:46` |
| `ANNOUNCEMENT` | `INFO` | `163.36` | 84,741.37 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 84.74K USD at 163.3600 USD [API] | `2025-11-04 05:18:41` |
| `ANNOUNCEMENT` | `INFO` | `163.38` | 21,187.12 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 21.19K USD at 163.3800 USD [API] | `2025-11-04 05:18:39` |
| `ANNOUNCEMENT` | `INFO` | `171.94` | 59,785.26 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 59.79K USD at 171.9400 USD [API] | `2025-11-03 15:26:55` |
| `ANNOUNCEMENT` | `INFO` | `180.11` | 5,718.49 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 5.72K USD at 180.1100 USD [API] | `2025-10-22 18:19:05` |
| `ANNOUNCEMENT` | `INFO` | `186.23` | 12,684.13 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 12.68K USD at 186.2300 USD [API] | `2025-10-21 23:35:44` |
| `ANNOUNCEMENT` | `INFO` | `183.34` | 4,860.34 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.86K USD at 183.3400 USD [API] | `2025-10-21 04:11:42` |
| `ANNOUNCEMENT` | `INFO` | `183.34` | 1,560.22 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.56K USD at 183.3400 USD [API] | `2025-10-21 04:11:42` |
| `ANNOUNCEMENT` | `INFO` | `183.34` | 269.51 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.27K USD at 183.3400 USD [API] | `2025-10-21 04:11:42` |
| `ANNOUNCEMENT` | `INFO` | `183.34` | 45.84 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.05K USD at 183.3400 USD [API] | `2025-10-21 04:11:42` |
| `ANNOUNCEMENT` | `INFO` | `183.35` | 29.34 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.03K USD at 183.3500 USD [API] | `2025-10-21 04:11:42` |
| `ANNOUNCEMENT` | `INFO` | `183.35` | 1,096.43 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.10K USD at 183.3500 USD [API] | `2025-10-21 04:11:42` |
| `ANNOUNCEMENT` | `INFO` | `183.36` | 4,294.29 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.29K USD at 183.3600 USD [API] | `2025-10-21 04:11:42` |
| `ANNOUNCEMENT` | `INFO` | `186.67` | 8,351.62 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 8.35K USD at 186.6700 USD [API] | `2025-10-20 16:45:40` |
| `ANNOUNCEMENT` | `INFO` | `186.67` | 17,785.92 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 17.79K USD at 186.6700 USD [API] | `2025-10-20 16:45:40` |
| `ANNOUNCEMENT` | `INFO` | `183.69` | 9,028.36 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 9.03K USD at 183.6900 USD [API] | `2025-10-20 00:33:22` |
| `ANNOUNCEMENT` | `INFO` | `183.69` | 21,462.34 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 21.46K USD at 183.6900 USD [API] | `2025-10-20 00:33:22` |
| `ANNOUNCEMENT` | `INFO` | `183.69` | 148.79 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.15K USD at 183.6900 USD [API] | `2025-10-20 00:33:22` |
| `ANNOUNCEMENT` | `INFO` | `183.69` | 2,999.66 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.00K USD at 183.6900 USD [API] | `2025-10-20 00:33:22` |
| `ANNOUNCEMENT` | `INFO` | `183.69` | 21,337.43 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 21.34K USD at 183.6900 USD [API] | `2025-10-20 00:33:22` |
| `ANNOUNCEMENT` | `INFO` | `176.12` | 23,059.39 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 23.06K USD at 176.1200 USD [API] | `2025-10-17 14:35:32` |
| `ANNOUNCEMENT` | `INFO` | `176.12` | 1,000.36 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.00K USD at 176.1200 USD [API] | `2025-10-17 14:35:32` |
| `ANNOUNCEMENT` | `INFO` | `176.13` | 24,640.59 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 24.64K USD at 176.1300 USD [API] | `2025-10-17 14:35:32` |
| `ANNOUNCEMENT` | `INFO` | `176.13` | 17.61 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 176.1300 USD [API] | `2025-10-17 14:35:32` |
| `ANNOUNCEMENT` | `INFO` | `176.13` | 5,787.63 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 5.79K USD at 176.1300 USD [API] | `2025-10-17 14:35:32` |
| `ANNOUNCEMENT` | `INFO` | `179.55` | 16,558.10 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 16.56K USD at 179.5500 USD [API] | `2025-10-11 19:20:00` |
| `ANNOUNCEMENT` | `INFO` | `203.42` | 34,725.83 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 34.73K USD at 203.4200 USD [API] | `2025-10-10 20:54:00` |
| `ANNOUNCEMENT` | `INFO` | `216.03` | 10,764.77 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 10.76K USD at 216.0300 USD [API] | `2025-10-10 15:20:15` |
| `ANNOUNCEMENT` | `INFO` | `216.03` | 987.26 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.99K USD at 216.0300 USD [API] | `2025-10-10 15:20:15` |
| `ANNOUNCEMENT` | `INFO` | `216.04` | 1,641.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.64K USD at 216.0400 USD [API] | `2025-10-10 15:20:15` |
| `ANNOUNCEMENT` | `INFO` | `216.04` | 1,641.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.64K USD at 216.0400 USD [API] | `2025-10-10 15:20:15` |
| `ANNOUNCEMENT` | `INFO` | `216.04` | 1,641.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.64K USD at 216.0400 USD [API] | `2025-10-10 15:20:15` |
| `ANNOUNCEMENT` | `INFO` | `216.04` | 1,641.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.64K USD at 216.0400 USD [API] | `2025-10-10 15:20:15` |
| `ANNOUNCEMENT` | `INFO` | `216.04` | 20,003.14 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 20.00K USD at 216.0400 USD [API] | `2025-10-10 15:20:15` |
| `ANNOUNCEMENT` | `INFO` | `216.05` | 1,641.98 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.64K USD at 216.0500 USD [API] | `2025-10-10 15:20:15` |
| `ANNOUNCEMENT` | `INFO` | `216.05` | 1,641.98 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.64K USD at 216.0500 USD [API] | `2025-10-10 15:20:15` |
| `ANNOUNCEMENT` | `INFO` | `216.05` | 1,641.98 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.64K USD at 216.0500 USD [API] | `2025-10-10 15:20:15` |
| `ANNOUNCEMENT` | `INFO` | `216.05` | 1,641.98 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.64K USD at 216.0500 USD [API] | `2025-10-10 15:20:15` |
| `ANNOUNCEMENT` | `INFO` | `216.07` | 4,628.22 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.63K USD at 216.0700 USD [API] | `2025-10-10 15:20:15` |
| `ANNOUNCEMENT` | `INFO` | `191.18` | 7,909.12 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 7.91K USD at 191.1800 USD [API] | `2025-09-26 11:07:31` |
| `ANNOUNCEMENT` | `INFO` | `205.12` | 4,449.05 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.45K USD at 205.1200 USD [API] | `2025-09-25 04:17:33` |
| `ANNOUNCEMENT` | `INFO` | `205.12` | 1,380.46 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.38K USD at 205.1200 USD [API] | `2025-09-25 04:17:33` |
| `ANNOUNCEMENT` | `INFO` | `205.12` | 3,763.95 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.76K USD at 205.1200 USD [API] | `2025-09-25 04:17:33` |
| `ANNOUNCEMENT` | `INFO` | `205.12` | 416.39 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.42K USD at 205.1200 USD [API] | `2025-09-25 04:17:33` |
| `ANNOUNCEMENT` | `INFO` | `205.12` | 6,553.58 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 6.55K USD at 205.1200 USD [API] | `2025-09-25 04:17:33` |
| `ANNOUNCEMENT` | `INFO` | `210.73` | 7,059.45 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 7.06K USD at 210.7300 USD [API] | `2025-09-24 03:27:51` |
| `ANNOUNCEMENT` | `INFO` | `210.73` | 472.04 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.47K USD at 210.7300 USD [API] | `2025-09-24 03:27:51` |
| `ANNOUNCEMENT` | `INFO` | `210.73` | 389.85 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.39K USD at 210.7300 USD [API] | `2025-09-24 03:27:51` |
| `ANNOUNCEMENT` | `INFO` | `210.73` | 472.04 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.47K USD at 210.7300 USD [API] | `2025-09-24 03:27:51` |
| `ANNOUNCEMENT` | `INFO` | `210.73` | 4,360.00 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.36K USD at 210.7300 USD [API] | `2025-09-24 03:27:51` |
| `ANNOUNCEMENT` | `INFO` | `210.73` | 19,802.30 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 19.80K USD at 210.7300 USD [API] | `2025-09-24 03:27:51` |
| `ANNOUNCEMENT` | `INFO` | `210.73` | 2,090.44 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.09K USD at 210.7300 USD [API] | `2025-09-24 03:27:51` |
| `ANNOUNCEMENT` | `INFO` | `213.40` | 32,020.67 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 32.02K USD at 213.4000 USD [API] | `2025-09-23 20:22:48` |
| `ANNOUNCEMENT` | `INFO` | `213.40` | 9,997.79 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 10.00K USD at 213.4000 USD [API] | `2025-09-23 20:22:48` |
| `ANNOUNCEMENT` | `INFO` | `213.40` | 10,104.49 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 10.10K USD at 213.4000 USD [API] | `2025-09-23 20:22:48` |
| `ANNOUNCEMENT` | `INFO` | `213.40` | 5,996.54 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 6.00K USD at 213.4000 USD [API] | `2025-09-23 20:22:48` |
| `ANNOUNCEMENT` | `INFO` | `213.40` | 1,997.42 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.00K USD at 213.4000 USD [API] | `2025-09-23 20:22:48` |
| `ANNOUNCEMENT` | `INFO` | `213.40` | 9,997.79 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 10.00K USD at 213.4000 USD [API] | `2025-09-23 20:22:48` |
| `ANNOUNCEMENT` | `INFO` | `213.40` | 3,378.12 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.38K USD at 213.4000 USD [API] | `2025-09-23 20:22:48` |
| `ANNOUNCEMENT` | `INFO` | `232.53` | 33,214.59 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 33.21K USD at 232.5300 USD [API] | `2025-09-22 00:32:54` |
| `ANNOUNCEMENT` | `INFO` | `235.00` | 36,716.40 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 36.72K USD at 235.0000 USD [API] | `2025-09-15 08:03:04` |
| `ANNOUNCEMENT` | `INFO` | `235.00` | 14,356.15 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 14.36K USD at 235.0000 USD [API] | `2025-09-15 08:03:04` |
| `ANNOUNCEMENT` | `INFO` | `99.76` | 20,000.68 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 20.00K USD at 99.7590 USD [API] | `2026-10-29 07:47:27` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`101.22` (Vol: 4,800,000.00 USD, Dist: `+3.06%`) | Long MP=`92.18` (Vol: 5,300,000.00 USD, Dist: `--6.15%`)
  * 48H Horizon: Short MP=`101.12` (Vol: 4,700,000.00 USD, Dist: `+2.96%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--6.17%`)
  * 3D Horizon: Short MP=`101.12` (Vol: 4,700,000.00 USD, Dist: `+2.96%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--6.17%`)
  * 7D Horizon: Short MP=`104.03` (Vol: 7,200,000.00 USD, Dist: `+5.92%`) | Long MP=`92.11` (Vol: 5,300,000.00 USD, Dist: `--6.22%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `19.65` | 712.31 USD | 122,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.95` | 9,980.00 USD | 122,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.25` | 207.76 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.35` | 386.65 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.55` | 5,120.00 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.05` | 1,050.00 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.25` | 276.68 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 3,990.00 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 161.73 USD | 122,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.65` | 5,020.00 USD | 122,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.75` | 4,630.00 USD | 122,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.05` | 795,690.00 USD | 122,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.25` | 132.39 USD | 121,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.45` | 111.13 USD | 121,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.75` | 8,390.00 USD | 121,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.95` | 2,300.00 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.05` | 1,150.00 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.15` | 243.31 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.25` | 12,170.00 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.35` | 21,070.00 USD | 121,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.45` | 1,380.00 USD | 121,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.55` | 14,180.00 USD | 121,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.35` | 1,350.00 USD | 121,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.55` | 4,530.00 USD | 121,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.95` | 1,680.00 USD | 121,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.05` | 1,250.00 USD | 121,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.15` | 2,010.00 USD | 121,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.45` | 1,200.00 USD | 121,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.75` | 148,070.00 USD | 121,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.85` | 14,530.00 USD | 121,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 3,090.00 USD | 121,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.05` | 5,910.00 USD | 121,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.25` | 271.69 USD | 121,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.35` | 475.09 USD | 121,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.45` | 856.45 USD | 121,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.65` | 9,090.00 USD | 121,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 40,740.00 USD | 121,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.35` | 3,500.00 USD | 121,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.45` | 686.25 USD | 121,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 2,480.00 USD | 121,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.85` | 412.18 USD | 121,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 84,260.00 USD | 121,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.05` | 17,440.00 USD | 121,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.15` | 62,890.00 USD | 121,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.35` | 6,200.00 USD | 121,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 113.80 USD | 121,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.55` | 2,280.00 USD | 121,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.65` | 16,880.00 USD | 121,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.75` | 254.72 USD | 121,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.85` | 727.60 USD | 121,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.95` | 9,840.00 USD | 121,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.35` | 121.51 USD | 121,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.45` | 10,580.00 USD | 121,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.95` | 239.60 USD | 121,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 3,010.00 USD | 121,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.15` | 50,570.00 USD | 121,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.35` | 4,230.00 USD | 121,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 526,290.00 USD | 121,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 233.86 USD | 120,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.85` | 69,880.00 USD | 120,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.05` | 621.00 USD | 120,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 160.11 USD | 120,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.45` | 278.33 USD | 120,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 789.24 USD | 120,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 19,970.00 USD | 120,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 1,030.00 USD | 120,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.25` | 3,900.00 USD | 120,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 4,420.00 USD | 120,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 5,240.00 USD | 120,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.05` | 274.98 USD | 120,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.25` | 489.11 USD | 120,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.45` | 1,810.00 USD | 120,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.55` | 559.28 USD | 120,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 962.39 USD | 120,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.75` | 40,500.00 USD | 120,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.85` | 958.63 USD | 120,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 395.66 USD | 120,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.35` | 842.61 USD | 120,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.55` | 9,070.00 USD | 120,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 486.14 USD | 120,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.75` | 54,920.00 USD | 120,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.85` | 1,930.00 USD | 120,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 6,620,000.00 USD | 120,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 37,720.00 USD | 113,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.15` | 9,310.00 USD | 113,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.25` | 4,490.00 USD | 113,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.35` | 2,900.00 USD | 113,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.55` | 107.01 USD | 113,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.65` | 5,650.00 USD | 113,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.75` | 4,840.00 USD | 113,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.85` | 1,570.00 USD | 113,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.95` | 1,990.00 USD | 113,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.05` | 6,700.00 USD | 113,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.15` | 15,480.00 USD | 113,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.25` | 619.51 USD | 113,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 4,550.00 USD | 113,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 2,410.00 USD | 113,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.55` | 50,040.00 USD | 113,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.65` | 2,060.00 USD | 113,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 1,740.00 USD | 113,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.95` | 1,660.00 USD | 113,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 302,500.00 USD | 113,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 373.62 USD | 113,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 19,600.00 USD | 113,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 262.85 USD | 113,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.65` | 6,000.00 USD | 113,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 267.27 USD | 113,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 4,380.00 USD | 113,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 858,390.00 USD | 113,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 191,250.00 USD | 112,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 287.63 USD | 112,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 3,000,000.00 USD | 112,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 107,910.00 USD | 109,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 736.64 USD | 109,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.85` | 4,270.00 USD | 109,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 607.62 USD | 109,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 51,130.00 USD | 109,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 54,790.00 USD | 108,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 258.40 USD | 108,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 424.37 USD | 108,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 13,450.00 USD | 108,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 2,890.00 USD | 108,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 1,270.00 USD | 108,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 1,510.00 USD | 108,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.15` | 2,510.00 USD | 108,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.25` | 632.73 USD | 108,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.35` | 120,110.00 USD | 108,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 3,160.00 USD | 108,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 2,030.00 USD | 108,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.75` | 9,610.00 USD | 108,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 1,050,000.00 USD | 108,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 204,890.00 USD | 107,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 4,600.00 USD | 107,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 1,070.00 USD | 107,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 471.49 USD | 107,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.35` | 1,850.00 USD | 107,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 15,430.00 USD | 107,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 770.11 USD | 107,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.75` | 588.26 USD | 107,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 1,020.00 USD | 107,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 48,400.00 USD | 107,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 1,120.00 USD | 107,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 2,790.00 USD | 107,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 146.19 USD | 107,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 198.62 USD | 107,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.45` | 5,920.00 USD | 107,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.55` | 8,210.00 USD | 107,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 5,190.00 USD | 107,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.75` | 315,460.00 USD | 107,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 46,180.00 USD | 107,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 1,080.00 USD | 107,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,420.00 USD | 107,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 440.15 USD | 107,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.55` | 298.75 USD | 107,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 213.01 USD | 107,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 69,410.00 USD | 107,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 1,120.00 USD | 106,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.05` | 11,530.00 USD | 106,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 6,640.00 USD | 106,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 8,950.00 USD | 106,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.45` | 10,180.00 USD | 106,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 686,110.00 USD | 106,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 4,280.00 USD | 106,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 37,670.00 USD | 106,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 3,670,000.00 USD | 106,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 6,960.00 USD | 102,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 19,040.00 USD | 102,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 2,210.00 USD | 102,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 31,340.00 USD | 102,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 9,480.00 USD | 102,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 7,940.00 USD | 102,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 319.09 USD | 102,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 9,450.00 USD | 102,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.85` | 458.50 USD | 102,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 26,070.00 USD | 102,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 435.63 USD | 102,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 3,580.00 USD | 102,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 4,560.00 USD | 102,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 3,190.00 USD | 102,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 11,380.00 USD | 102,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.75` | 537.62 USD | 102,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 592.18 USD | 102,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 2,360.00 USD | 102,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 2,950.00 USD | 102,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 8,650.00 USD | 102,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 743,490.00 USD | 102,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 2,540.00 USD | 101,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.65` | 98,780.00 USD | 101,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 58,290.00 USD | 101,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.95` | 2,260.00 USD | 101,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 13,300.00 USD | 101,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 6,450.00 USD | 101,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 2,430.00 USD | 101,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.35` | 5,840.00 USD | 101,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.45` | 2,930.00 USD | 101,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 97,250.00 USD | 101,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 9,260.00 USD | 101,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 1,860.00 USD | 101,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.85` | 14,260.00 USD | 101,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,490.00 USD | 101,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,190,000.00 USD | 101,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,610.00 USD | 100,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.25` | 21,190.00 USD | 100,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 7,790.00 USD | 100,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 16,830.00 USD | 100,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 889.42 USD | 100,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 9,200.00 USD | 100,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.75` | 1,700.00 USD | 100,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.85` | 41,540.00 USD | 100,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 20,850.00 USD | 100,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 12,350.00 USD | 100,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.15` | 1,500.00 USD | 100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 7,860.00 USD | 100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.35` | 2,410.00 USD | 99,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,110.00 USD | 99,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 2,710.00 USD | 99,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.65` | 843.83 USD | 99,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 12,040.00 USD | 99,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.85` | 19,710.00 USD | 99,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 5,530.00 USD | 99,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.05` | 2,840.00 USD | 99,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.15` | 2,620.00 USD | 99,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.25` | 1,440.00 USD | 99,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.35` | 10,640.00 USD | 99,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.45` | 3,920.00 USD | 99,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.55` | 137,330.00 USD | 99,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.65` | 7,840.00 USD | 99,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.75` | 24,770.00 USD | 99,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.85` | 42,450.00 USD | 99,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.95` | 503,350.00 USD | 99,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.05` | 58,250.00 USD | 99,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.15` | 99,630.00 USD | 99,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.25` | 1,760.00 USD | 99,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.35` | 5,700.00 USD | 99,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.45` | 879.59 USD | 99,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.55` | 11,110.00 USD | 99,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.65` | 3,370.00 USD | 99,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.75` | 3,180.00 USD | 99,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.85` | 9,370.00 USD | 99,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.95` | 3,240.00 USD | 99,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.05` | 38,480.00 USD | 99,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.15` | 2,670.00 USD | 98,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.25` | 24,560.00 USD | 98,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.35` | 15,690.00 USD | 98,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.45` | 38,780.00 USD | 98,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.55` | 43,790.00 USD | 98,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.65` | 230.70 USD | 98,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.75` | 3,870.00 USD | 98,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.85` | 18,220.00 USD | 98,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.95` | 62,860.00 USD | 98,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.05` | 350.78 USD | 98,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.15` | 14,640.00 USD | 98,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.25` | 6,450.00 USD | 98,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.35` | 11,720.00 USD | 98,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.45` | 2,230.00 USD | 98,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.55` | 70,060.00 USD | 98,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.65` | 2,070.00 USD | 98,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.75` | 15,300.00 USD | 98,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.85` | 860,090.00 USD | 98,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.95` | 142,480.00 USD | 97,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.05` | 30,740.00 USD | 97,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.25` | 2,010.00 USD | 97,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.35` | 9,920.00 USD | 97,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.45` | 146,360.00 USD | 97,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.55` | 5,090.00 USD | 97,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.65` | 11,490.00 USD | 97,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.75` | 92,210.00 USD | 97,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.85` | 26,070.00 USD | 97,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.95` | 7,050.00 USD | 97,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.05` | 5,640.00 USD | 97,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.15` | 38,120.00 USD | 97,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.25` | 13,420.00 USD | 97,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.35` | 14,180.00 USD | 97,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.45` | 12,980.00 USD | 97,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.55` | 11,520.00 USD | 97,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.65` | 3,190.00 USD | 97,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.75` | 10,100.00 USD | 97,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.85` | 1,260.00 USD | 97,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.95` | 74,000.00 USD | 97,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.05` | 2,770,000.00 USD | 97,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.15` | 5,570.00 USD | 94,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.25` | 6,500.00 USD | 94,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.35` | 7,120.00 USD | 94,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.45` | 29,660.00 USD | 94,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.55` | 1,390.00 USD | 94,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.65` | 14,530.00 USD | 94,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.75` | 52,640.00 USD | 94,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.85` | 26,170.00 USD | 94,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.95` | 2,320,000.00 USD | 94,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.05` | 11,230.00 USD | 91,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.15` | 138,750.00 USD | 91,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.25` | 9,870.00 USD | 91,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.35` | 4,670.00 USD | 91,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.45` | 463.51 USD | 91,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.55` | 2,970.00 USD | 91,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.65` | 418.17 USD | 91,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.75` | 195.64 USD | 91,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.85` | 6,130.00 USD | 91,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.95` | 488.70 USD | 91,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.05` | 3,780.00 USD | 91,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.15` | 34,330.00 USD | 91,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.25` | 613.24 USD | 91,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.35` | 29,010.00 USD | 91,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.45` | 94,150.00 USD | 91,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.55` | 16,050.00 USD | 91,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.65` | 3,640.00 USD | 91,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.75` | 29,930.00 USD | 91,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.85` | 32,070.00 USD | 91,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.95` | 37,240.00 USD | 91,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.05` | 19,630.00 USD | 91,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.15` | 64,730.00 USD | 91,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.25` | 30,620.00 USD | 91,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.35` | 3,930.00 USD | 91,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.55` | 4,750.00 USD | 91,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.65` | 711.42 USD | 91,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.75` | 5,300.00 USD | 91,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.85` | 28,860.00 USD | 91,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.95` | 55,060.00 USD | 91,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.05` | 4,230.00 USD | 91,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.15` | 5,900.00 USD | 91,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.25` | 35,260.00 USD | 91,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.35` | 10,280.00 USD | 91,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.45` | 20,920.00 USD | 91,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.55` | 33,930.00 USD | 91,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.65` | 32,140.00 USD | 91,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.75` | 16,580.00 USD | 91,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.85` | 6,380.00 USD | 91,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.95` | 13,170.00 USD | 91,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.05` | 9,000.00 USD | 91,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.15` | 44,140.00 USD | 91,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.25` | 1,800.00 USD | 90,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.35` | 16,180.00 USD | 90,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.45` | 21,530.00 USD | 90,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.55` | 133,130.00 USD | 90,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.65` | 2,480.00 USD | 90,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.75` | 20,960.00 USD | 90,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.85` | 31,310.00 USD | 90,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.95` | 6,250.00 USD | 90,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.05` | 21,650.00 USD | 90,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.15` | 104,280.00 USD | 90,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.25` | 31,580.00 USD | 90,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.45` | 11,700.00 USD | 90,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.55` | 49,290.00 USD | 90,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.65` | 416.27 USD | 90,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.75` | 32,540.00 USD | 90,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.85` | 36,960.00 USD | 90,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.95` | 3,910.00 USD | 90,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.05` | 96,080.00 USD | 90,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.25` | 4,450.00 USD | 90,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.35` | 47,540.00 USD | 90,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.45` | 4,310.00 USD | 90,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.55` | 579.66 USD | 90,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.65` | 2,570.00 USD | 90,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.85` | 396.23 USD | 90,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.95` | 209.79 USD | 90,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.05` | 1,560,000.00 USD | 90,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.15` | 20,970.00 USD | 88,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.25` | 42,080.00 USD | 88,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.35` | 38,010.00 USD | 88,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.45` | 3,130.00 USD | 88,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.55` | 10,640.00 USD | 88,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.65` | 65,990.00 USD | 88,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.75` | 11,630.00 USD | 88,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.85` | 11,050.00 USD | 88,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.95` | 60,910.00 USD | 88,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.05` | 4,840.00 USD | 88,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.25` | 14,930.00 USD | 88,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.35` | 1,600.00 USD | 88,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.45` | 10,990.00 USD | 88,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.55` | 64,260.00 USD | 88,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.65` | 19,140.00 USD | 88,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.75` | 47,940.00 USD | 88,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.85` | 1,910.00 USD | 88,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.95` | 937.30 USD | 88,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.05` | 37,700.00 USD | 88,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.15` | 3,370.00 USD | 88,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.25` | 1,930.00 USD | 88,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.35` | 2,640.00 USD | 88,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.45` | 21,630.00 USD | 88,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.55` | 53,160.00 USD | 88,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.65` | 537,120.00 USD | 88,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.75` | 34,900.00 USD | 87,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.85` | 15,250.00 USD | 87,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.05` | 11,080.00 USD | 87,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.15` | 37,510,000.00 USD | 87,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.25` | 13,650.00 USD | 50,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.35` | 5,820.00 USD | 50,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.45` | 18,570.00 USD | 50,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.55` | 17,710.00 USD | 50,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.65` | 6,150.00 USD | 50,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.75` | 12,530,000.00 USD | 50,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.85` | 770,120.00 USD | 37,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.95` | 46,330.00 USD | 36,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.05` | 3,570.00 USD | 36,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.15` | 11,510.00 USD | 36,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.25` | 3,140.00 USD | 36,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.35` | 6,940.00 USD | 36,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.45` | 45,050.00 USD | 36,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.55` | 9,170.00 USD | 36,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.65` | 9,110.00 USD | 36,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.75` | 212,620.00 USD | 36,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.85` | 13,010.00 USD | 36,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.95` | 9,190.00 USD | 36,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.05` | 2,080.00 USD | 36,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.15` | 4,120.00 USD | 36,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.25` | 72,890.00 USD | 36,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.35` | 2,360,000.00 USD | 36,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.45` | 1,170,000.00 USD | 33,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.55` | 4,350.00 USD | 32,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.65` | 48,410.00 USD | 32,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.75` | 10,060.00 USD | 32,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.85` | 11,420.00 USD | 32,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.95` | 8,410.00 USD | 32,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.05` | 37,930.00 USD | 32,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.15` | 69,510.00 USD | 32,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.25` | 2,040.00 USD | 32,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.35` | 47,480.00 USD | 32,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.45` | 31,640.00 USD | 32,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.55` | 41,780.00 USD | 32,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.65` | 1,390.00 USD | 32,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.75` | 32,550.00 USD | 32,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.85` | 2,130.00 USD | 32,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.95` | 20,800.00 USD | 32,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.05` | 9,520.00 USD | 32,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.15` | 135,330.00 USD | 32,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.25` | 258,520.00 USD | 32,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.35` | 28,860.00 USD | 31,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.45` | 1,840.00 USD | 31,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.55` | 18,490.00 USD | 31,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.65` | 33,720.00 USD | 31,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.75` | 8,730.00 USD | 31,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.85` | 186,830.00 USD | 31,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.95` | 26,290.00 USD | 31,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.05` | 7,310.00 USD | 31,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.15` | 16,780.00 USD | 31,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.25` | 27,910.00 USD | 31,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.35` | 16,990.00 USD | 31,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.45` | 5,350.00 USD | 31,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.55` | 14,850.00 USD | 31,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.65` | 37,850.00 USD | 31,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.75` | 84,910.00 USD | 31,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.85` | 1,600,000.00 USD | 31,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.95` | 42,980.00 USD | 29,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.05` | 40,920.00 USD | 29,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.15` | 21,710.00 USD | 29,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.25` | 50,170.00 USD | 29,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.35` | 27,910.00 USD | 29,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.45` | 22,440.00 USD | 29,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.55` | 6,260.00 USD | 29,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.65` | 103,520.00 USD | 29,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.75` | 48,180.00 USD | 29,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.85` | 34,400.00 USD | 29,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.95` | 18,080.00 USD | 29,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.05` | 40,680.00 USD | 29,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.15` | 1,460,000.00 USD | 29,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.25` | 24,900.00 USD | 27,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.35` | 369,030.00 USD | 27,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.45` | 33,560.00 USD | 27,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.55` | 59,620.00 USD | 27,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.65` | 130,250.00 USD | 27,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.75` | 53,250.00 USD | 27,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.85` | 2,630.00 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.95` | 27,920.00 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.05` | 9,680.00 USD | 27,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.15` | 4,370.00 USD | 27,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.25` | 106,660.00 USD | 27,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.35` | 205,010.00 USD | 27,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.45` | 2,180.00 USD | 26,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.55` | 38,390.00 USD | 26,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.65` | 56,310.00 USD | 26,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.75` | 12,180.00 USD | 26,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.85` | 134,060.00 USD | 26,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.95` | 28,980.00 USD | 26,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.05` | 83,450.00 USD | 26,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.15` | 85,390.00 USD | 26,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.25` | 25,020.00 USD | 26,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.35` | 5,340.00 USD | 26,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.45` | 48,500.00 USD | 26,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.55` | 13,740.00 USD | 26,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.75` | 9,870.00 USD | 26,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.85` | 68,400.00 USD | 26,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.95` | 8,370.00 USD | 26,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.05` | 21,520.00 USD | 26,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.15` | 63,710.00 USD | 26,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.25` | 39,070.00 USD | 26,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.35` | 55,590.00 USD | 26,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.45` | 34,460.00 USD | 26,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.55` | 9,470.00 USD | 26,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.65` | 36,820.00 USD | 26,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.75` | 60,790.00 USD | 26,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.85` | 62,880.00 USD | 25,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.95` | 3,950.00 USD | 25,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.05` | 54,310.00 USD | 25,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.15` | 128,590.00 USD | 25,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.25` | 41,700.00 USD | 25,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.35` | 33,050.00 USD | 25,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.45` | 15,960.00 USD | 25,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.55` | 2,220.00 USD | 25,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.65` | 31,850.00 USD | 25,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.75` | 49,110.00 USD | 25,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.85` | 14,850.00 USD | 25,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.95` | 30,400.00 USD | 25,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.05` | 28,670.00 USD | 25,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.15` | 31,900.00 USD | 25,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.25` | 624,910.00 USD | 25,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.35` | 104,890.00 USD | 24,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.45` | 17,250.00 USD | 24,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.55` | 10,500.00 USD | 24,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.65` | 13,740.00 USD | 24,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.75` | 31,310.00 USD | 24,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.85` | 440,070.00 USD | 24,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.95` | 10,620.00 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.05` | 2,230,000.00 USD | 24,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.15` | 128,110.00 USD | 21,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.25` | 22,790.00 USD | 21,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.35` | 418,360.00 USD | 21,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.45` | 60,710.00 USD | 21,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.55` | 102,010.00 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.65` | 15,400.00 USD | 21,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.75` | 18,650.00 USD | 21,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.85` | 760,330.00 USD | 21,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.95` | 31,560.00 USD | 20,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.05` | 117,060.00 USD | 20,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.15` | 807,960.00 USD | 20,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.25` | 24,480.00 USD | 19,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.35` | 159,780.00 USD | 19,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.45` | 235,090.00 USD | 19,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `82.50` | 171,450,000.00 USD | 171,450,000.00 USD | 71,680.00 USD | 3,750.00 USD | 2,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `82.55` | 26,400.00 USD | 19,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.65` | 98,590.00 USD | 19,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `82.70` | 171,370,000.00 USD | 171,370,000.00 USD | 0.00 USD | 54,980.00 USD | 140,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `82.75` | 27,050.00 USD | 18,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.85` | 20,580.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `82.90` | 171,170,000.00 USD | 171,170,000.00 USD | 1,670.00 USD | 2,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `82.95` | 16,630.00 USD | 18,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.05` | 58,320.00 USD | 18,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.10` | 171,170,000.00 USD | 171,170,000.00 USD | 1,690.00 USD | 48,940.00 USD | 642.56 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.15` | 61,560.00 USD | 18,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.25` | 197,080.00 USD | 18,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.30` | 171,120,000.00 USD | 171,120,000.00 USD | 3,730.00 USD | 93,000.00 USD | 56,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.35` | 287,230.00 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.45` | 29,160.00 USD | 18,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.50` | 170,960,000.00 USD | 170,960,000.00 USD | 6,440.00 USD | 791.58 USD | 10,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.55` | 168,680.00 USD | 18,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.65` | 80,730.00 USD | 18,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.70` | 170,950,000.00 USD | 170,950,000.00 USD | 0.00 USD | 68,140.00 USD | 85,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.75` | 87,590.00 USD | 17,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.85` | 12,050.00 USD | 17,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.90` | 170,790,000.00 USD | 170,790,000.00 USD | 2,640.00 USD | 0.00 USD | 70,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.95` | 54,780.00 USD | 17,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.05` | 133,650.00 USD | 17,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.10` | 170,720,000.00 USD | 170,720,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.15` | 65,310.00 USD | 17,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.25` | 47,100.00 USD | 17,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.30` | 170,700,000.00 USD | 170,700,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.35` | 25,180.00 USD | 17,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.45` | 85,770.00 USD | 17,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.55` | 18,030.00 USD | 17,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.65` | 102,150.00 USD | 17,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.75` | 289,740.00 USD | 17,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.85` | 95,230.00 USD | 17,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.95` | 617.59 USD | 16,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.05` | 18,750.00 USD | 16,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.10` | 170,670,000.00 USD | 170,670,000.00 USD | 0.00 USD | 204,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.15` | 5,380.00 USD | 16,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.25` | 609,660.00 USD | 16,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.30` | 170,470,000.00 USD | 170,470,000.00 USD | 0.00 USD | 13,630.00 USD | 186,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.35` | 22,160.00 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.45` | 53,750.00 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.50` | 170,270,000.00 USD | 170,270,000.00 USD | 0.00 USD | 12,950.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.55` | 1,250,000.00 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.65` | 43,310.00 USD | 15,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.70` | 170,250,000.00 USD | 170,250,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.75` | 9,830.00 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.85` | 86,260.00 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.90` | 170,060,000.00 USD | 170,060,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.95` | 363,700.00 USD | 14,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.05` | 256,680.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.10` | 169,800,000.00 USD | 169,800,000.00 USD | 0.00 USD | 0.00 USD | 195,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.15` | 74,860.00 USD | 14,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.25` | 28,470.00 USD | 14,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.30` | 169,600,000.00 USD | 169,600,000.00 USD | 0.00 USD | 323,360.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.35` | 3,870.00 USD | 14,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.45` | 266,720.00 USD | 14,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.50` | 169,270,000.00 USD | 169,270,000.00 USD | 0.00 USD | 0.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.55` | 44,550.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.65` | 193,100.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.70` | 169,270,000.00 USD | 169,270,000.00 USD | 0.00 USD | 11,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.75` | 46,790.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.85` | 78,310.00 USD | 13,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.90` | 169,260,000.00 USD | 169,260,000.00 USD | 263,340.00 USD | 309,680.00 USD | 297,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.95` | 155,770.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.05` | 55,280.00 USD | 13,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.10` | 174,880,000.00 USD | 174,880,000.00 USD | 316,760.00 USD | 428,310.00 USD | 423,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.10` | 168,390,000.00 USD | 168,390,000.00 USD | 0.00 USD | 5,620.00 USD | 6,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.15` | 45,190.00 USD | 13,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.25` | 76,430.00 USD | 13,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.30` | 173,710,000.00 USD | 173,710,000.00 USD | 61,200.00 USD | 207,830.00 USD | 156,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.30` | 168,370,000.00 USD | 168,370,000.00 USD | 0.00 USD | 204,790.00 USD | 288,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.35` | 83,480.00 USD | 13,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.45` | 158,820.00 USD | 13,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.50` | 173,290,000.00 USD | 173,290,000.00 USD | 10,160.00 USD | 72,180.00 USD | 69,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.50` | 167,880,000.00 USD | 167,880,000.00 USD | 24,350.00 USD | 24,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.55` | 203,490.00 USD | 12,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.65` | 113,790.00 USD | 12,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.70` | 173,140,000.00 USD | 173,140,000.00 USD | 8,600.00 USD | 247,780.00 USD | 247,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.70` | 167,830,000.00 USD | 167,830,000.00 USD | 0.00 USD | 290,940.00 USD | 415,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.75` | 25,930.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.85` | 67,120.00 USD | 12,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.90` | 172,630,000.00 USD | 172,630,000.00 USD | 133,480.00 USD | 427,430.00 USD | 925,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.90` | 167,130,000.00 USD | 167,130,000.00 USD | 0.00 USD | 307,460.00 USD | 251,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.95` | 6,600.00 USD | 12,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.05` | 161,010.00 USD | 12,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.10` | 171,140,000.00 USD | 171,140,000.00 USD | 54,110.00 USD | 0.00 USD | 230,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.10` | 166,570,000.00 USD | 166,570,000.00 USD | 0.00 USD | 0.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.15` | 21,240.00 USD | 12,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.25` | 54,000.00 USD | 12,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.30` | 170,860,000.00 USD | 170,860,000.00 USD | 83,370.00 USD | 73,830.00 USD | 136,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.30` | 166,550,000.00 USD | 166,550,000.00 USD | 0.00 USD | 20,610.00 USD | 331,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.35` | 101,240.00 USD | 12,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.45` | 62,140.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.50` | 170,570,000.00 USD | 170,570,000.00 USD | 0.00 USD | 99,900.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.50` | 166,200,000.00 USD | 166,200,000.00 USD | 0.00 USD | 0.00 USD | 3,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.55` | 242,620.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.65` | 97,760.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.70` | 170,470,000.00 USD | 170,470,000.00 USD | 204,330.00 USD | 124,180.00 USD | 415,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.70` | 166,200,000.00 USD | 166,200,000.00 USD | 224,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.75` | 185,570.00 USD | 11,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.85` | 1,140,000.00 USD | 11,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.90` | 169,720,000.00 USD | 169,720,000.00 USD | 143,140.00 USD | 62,660.00 USD | 226,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.90` | 165,970,000.00 USD | 165,970,000.00 USD | 17,470.00 USD | 3,730.00 USD | 3,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.95` | 32,790.00 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.05` | 22,640.00 USD | 10,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.10` | 169,290,000.00 USD | 169,290,000.00 USD | 160,900.00 USD | 83,520.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.10` | 165,950,000.00 USD | 165,950,000.00 USD | 350,210.00 USD | 291,000.00 USD | 601,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.15` | 125,700.00 USD | 10,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.25` | 31,740.00 USD | 10,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.30` | 169,030,000.00 USD | 169,030,000.00 USD | 221,290.00 USD | 284,680.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.30` | 164,710,000.00 USD | 164,710,000.00 USD | 679,190.00 USD | 22,080.00 USD | 27,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.35` | 25,620.00 USD | 10,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.45` | 447,820.00 USD | 10,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.50` | 168,520,000.00 USD | 168,520,000.00 USD | 4,870.00 USD | 50,620.00 USD | 278,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.50` | 163,980,000.00 USD | 163,980,000.00 USD | 184,930.00 USD | 91,380.00 USD | 512,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.55` | 53,100.00 USD | 9,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.65` | 28,830.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.70` | 168,190,000.00 USD | 168,190,000.00 USD | 190,910.00 USD | 107,730.00 USD | 426,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.70` | 163,190,000.00 USD | 163,190,000.00 USD | 780,700.00 USD | 225,300.00 USD | 472,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.75` | 125,510.00 USD | 9,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.85` | 64,900.00 USD | 9,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.90` | 167,460,000.00 USD | 167,460,000.00 USD | 301,540.00 USD | 255,100.00 USD | 381,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.90` | 161,710,000.00 USD | 161,710,000.00 USD | 446,430.00 USD | 563,970.00 USD | 807,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.95` | 83,320.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.05` | 57,350.00 USD | 9,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.10` | 166,530,000.00 USD | 166,530,000.00 USD | 1,210,000.00 USD | 1,030,000.00 USD | 836,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.10` | 159,890,000.00 USD | 159,890,000.00 USD | 967,200.00 USD | 633,920.00 USD | 879,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.15` | 56,590.00 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.25` | 28,100.00 USD | 9,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.30` | 163,450,000.00 USD | 163,450,000.00 USD | 773,740.00 USD | 539,900.00 USD | 443,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.30` | 157,410,000.00 USD | 157,410,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.35` | 78,770.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.45` | 28,650.00 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.50` | 161,690,000.00 USD | 161,690,000.00 USD | 683,680.00 USD | 538,340.00 USD | 928,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.50` | 155,330,000.00 USD | 155,330,000.00 USD | 1,100,000.00 USD | 823,160.00 USD | 860,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.55` | 44,980.00 USD | 9,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.65` | 119,860.00 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.70` | 159,540,000.00 USD | 159,540,000.00 USD | 628,630.00 USD | 803,190.00 USD | 388,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.70` | 152,550,000.00 USD | 152,550,000.00 USD | 742,490.00 USD | 700,720.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.75` | 103,330.00 USD | 8,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.85` | 951,490.00 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.90` | 157,720,000.00 USD | 157,720,000.00 USD | 673,680.00 USD | 420,760.00 USD | 83,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.90` | 149,670,000.00 USD | 149,670,000.00 USD | 1,350,000.00 USD | 997,660.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.95` | 18,840.00 USD | 7,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.05` | 435,550.00 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.10` | 156,540,000.00 USD | 156,540,000.00 USD | 436,270.00 USD | 732,110.00 USD | 474,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.10` | 146,290,000.00 USD | 146,290,000.00 USD | 2,350,000.00 USD | 578,750.00 USD | 895,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.15` | 294,770.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.25` | 33,570.00 USD | 7,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.30` | 154,900,000.00 USD | 154,900,000.00 USD | 150,320.00 USD | 221,290.00 USD | 448,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.30` | 142,470,000.00 USD | 142,470,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.35` | 25,530.00 USD | 7,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.45` | 322,810.00 USD | 7,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.50` | 154,080,000.00 USD | 154,080,000.00 USD | 850,930.00 USD | 781,420.00 USD | 655,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.50` | 139,490,000.00 USD | 139,490,000.00 USD | 705,000.00 USD | 1,710,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.55` | 1,230,000.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.65` | 1,440,000.00 USD | 5,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.70` | 151,790,000.00 USD | 151,790,000.00 USD | 268,750.00 USD | 463,180.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.70` | 135,780,000.00 USD | 135,780,000.00 USD | 538,680.00 USD | 342,840.00 USD | 781,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.75` | 225,950.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.85` | 248,450.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.90` | 149,900,000.00 USD | 149,900,000.00 USD | 1,280,000.00 USD | 813,050.00 USD | 663,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.90` | 134,120,000.00 USD | 134,120,000.00 USD | 1,020,000.00 USD | 838,200.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.95` | 181,560.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.05` | 94,570.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.10` | 147,140,000.00 USD | 147,140,000.00 USD | 2,310,000.00 USD | 2,670,000.00 USD | 565,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.10` | 131,030,000.00 USD | 131,030,000.00 USD | 3,150,000.00 USD | 1,400,000.00 USD | 278,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.15` | 328,620.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.25` | 227,110.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.30` | 141,600,000.00 USD | 141,600,000.00 USD | 720,590.00 USD | 799,660.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.30` | 126,200,000.00 USD | 126,200,000.00 USD | 375,130.00 USD | 487,150.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.35` | 326,740.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.45` | 122,830.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.50` | 138,670,000.00 USD | 138,670,000.00 USD | 1,140,000.00 USD | 703,500.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.50` | 123,810,000.00 USD | 123,810,000.00 USD | 260,510.00 USD | 1,320,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.55` | 315,900.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.65` | 15,290.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.70` | 134,480,000.00 USD | 134,480,000.00 USD | 982,240.00 USD | 1,110,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.70` | 120,460,000.00 USD | 120,460,000.00 USD | 148,000.00 USD | 1,830,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.75` | 62,310.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.85` | 7,990.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.90` | 130,690,000.00 USD | 130,690,000.00 USD | 3,020,000.00 USD | 1,870,000.00 USD | 2,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.90` | 116,880,000.00 USD | 116,880,000.00 USD | 371,030.00 USD | 783,070.00 USD | 954,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.95` | 5,720.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.05` | 67,670.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.10` | 123,330,000.00 USD | 123,330,000.00 USD | 2,030,000.00 USD | 3,210,000.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.10` | 114,770,000.00 USD | 114,770,000.00 USD | 31,020.00 USD | 686,660.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.15` | 2,810.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.25` | 38,840.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.30` | 116,350,000.00 USD | 116,350,000.00 USD | 2,250,000.00 USD | 2,580,000.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.30` | 113,030,000.00 USD | 113,030,000.00 USD | 96,300.00 USD | 0.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.35` | 12,570.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.45` | 7,320.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.50` | 110,270,000.00 USD | 110,270,000.00 USD | 2,930,000.00 USD | 2,280,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.50` | 111,510,000.00 USD | 111,510,000.00 USD | 399,000.00 USD | 2,880,000.00 USD | 3,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.55` | 29,010.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.65` | 9,580.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.70` | 102,800,000.00 USD | 102,800,000.00 USD | 551,230.00 USD | 3,170,000.00 USD | 867,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.70` | 105,190,000.00 USD | 105,190,000.00 USD | 7,450.00 USD | 2,970,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.75` | 9,230.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.90` | 98,210,000.00 USD | 98,210,000.00 USD | 1,590,000.00 USD | 928,170.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.90` | 100,510,000.00 USD | 100,510,000.00 USD | 2,670,000.00 USD | 30,170.00 USD | 3,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.95` | 1,130,000.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.10` | 94,270,000.00 USD | 94,270,000.00 USD | 680,650.00 USD | 851,000.00 USD | 2,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.10` | 94,380,000.00 USD | 94,380,000.00 USD | 175,750.00 USD | 2,120,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.15` | 20,790.00 USD | 664,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.25` | 15,100.00 USD | 643,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.30` | 90,280,000.00 USD | 90,280,000.00 USD | 2,130,000.00 USD | 1,080,000.00 USD | 371,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.30` | 89,850,000.00 USD | 89,850,000.00 USD | 0.00 USD | 159,070.00 USD | 839,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.35` | 2,100.00 USD | 628,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.45` | 152,100.00 USD | 626,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.50` | 86,690,000.00 USD | 86,690,000.00 USD | 795,850.00 USD | 1,250,000.00 USD | 645,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.50` | 88,850,000.00 USD | 88,850,000.00 USD | 183,750.00 USD | 496,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.55` | 584.32 USD | 473,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.65` | 18,060.00 USD | 473,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.70` | 84,000,000.00 USD | 84,000,000.00 USD | 1,360,000.00 USD | 571,830.00 USD | 399,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.70` | 88,170,000.00 USD | 88,170,000.00 USD | 1,600,000.00 USD | 99,300.00 USD | 3,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.75` | 32,450.00 USD | 455,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.85` | 56,320.00 USD | 422,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.90` | 81,670,000.00 USD | 81,670,000.00 USD | 2,720,000.00 USD | 434,700.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.90` | 83,110,000.00 USD | 83,110,000.00 USD | 3,170,000.00 USD | 4,260,000.00 USD | 47,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.95` | 22,400.00 USD | 366,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.05` | 84,340.00 USD | 344,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.10` | 77,300,000.00 USD | 77,300,000.00 USD | 2,150,000.00 USD | 1,390,000.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.10` | 75,630,000.00 USD | 75,630,000.00 USD | 198,380.00 USD | 199,180.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.15` | 25,040.00 USD | 259,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.25` | 66,250.00 USD | 234,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.30` | 73,730,000.00 USD | 73,730,000.00 USD | 87,330.00 USD | 494,560.00 USD | 3,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.30` | 75,210,000.00 USD | 75,210,000.00 USD | 678,330.00 USD | 1,060,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.35` | 22,080.00 USD | 168,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.45` | 14,420.00 USD | 146,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.50` | 69,780,000.00 USD | 69,780,000.00 USD | 291,230.00 USD | 1,570,000.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.50` | 71,790,000.00 USD | 71,790,000.00 USD | 2,000,000.00 USD | 3,870,000.00 USD | 4,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.55` | 23,690.00 USD | 132,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.65` | 57,300.00 USD | 108,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.70` | 66,510,000.00 USD | 66,510,000.00 USD | 1,710,000.00 USD | 2,160,000.00 USD | 5,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.70` | 61,480,000.00 USD | 61,480,000.00 USD | 5,540,000.00 USD | 4,060,000.00 USD | 4,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.75` | 34,210.00 USD | 51,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.85` | 13,180.00 USD | 16,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.90` | 57,180,000.00 USD | 57,180,000.00 USD | 1,270,000.00 USD | 1,210,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.90` | 47,650,000.00 USD | 47,650,000.00 USD | 2,130,000.00 USD | 344,240.00 USD | 689,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `95.95` | 1,900.00 USD | 1,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.10` | 53,010,000.00 USD | 53,010,000.00 USD | 1,770,000.00 USD | 2,040,000.00 USD | 3,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.10` | 44,490,000.00 USD | 44,490,000.00 USD | 3,460,000.00 USD | 811,100.00 USD | 8,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.30` | 45,980,000.00 USD | 45,980,000.00 USD | 4,480,000.00 USD | 5,140,000.00 USD | 848,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.30` | 32,140,000.00 USD | 32,140,000.00 USD | 2,740,000.00 USD | 1,700,000.00 USD | 6,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.50` | 35,510,000.00 USD | 35,510,000.00 USD | 2,840,000.00 USD | 1,260,000.00 USD | 3,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.50` | 21,210,000.00 USD | 21,210,000.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.55` | 3,650.00 USD | 3,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.70` | 27,640,000.00 USD | 27,640,000.00 USD | 1,420,000.00 USD | 2,230,000.00 USD | 956,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.70` | 21,180,000.00 USD | 21,180,000.00 USD | 0.00 USD | 14,450.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.90` | 23,030,000.00 USD | 23,030,000.00 USD | 541,070.00 USD | 1,880,000.00 USD | 4,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.90` | 18,820,000.00 USD | 18,820,000.00 USD | 0.00 USD | 2,310,000.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.10` | 15,700,000.00 USD | 15,700,000.00 USD | 3,190,000.00 USD | 2,570,000.00 USD | 1,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.10` | 15,310,000.00 USD | 15,310,000.00 USD | 0.00 USD | 1,350,000.00 USD | 4,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.30` | 8,010,000.00 USD | 8,010,000.00 USD | 1,030,000.00 USD | 1,270,000.00 USD | 873,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.30` | 9,670,000.00 USD | 9,670,000.00 USD | 0.00 USD | 16,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.50` | 4,840,000.00 USD | 4,840,000.00 USD | 534,370.00 USD | 1,320,000.00 USD | 1,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.50` | 9,650,000.00 USD | 9,650,000.00 USD | 0.00 USD | 110,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.70` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.70` | 9,540,000.00 USD | 9,540,000.00 USD | 3,880,000.00 USD | 1,750,000.00 USD | 3,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.90` | 2,450,000.00 USD | 2,450,000.00 USD | 2,400,000.00 USD | 48,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.90` | 4,900,000.00 USD | 4,900,000.00 USD | 2,400,000.00 USD | 48,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.90` | 13,610,000.00 USD | 13,610,000.00 USD | 11,920,000.00 USD | 1,690,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.90` | 27,210,000.00 USD | 27,210,000.00 USD | 11,920,000.00 USD | 1,690,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.10` | 7,920,000.00 USD | 7,920,000.00 USD | 211,100.00 USD | 0.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.10` | 37,090,000.00 USD | 37,090,000.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.30` | 15,730,000.00 USD | 15,730,000.00 USD | 1,890,000.00 USD | 20,470.00 USD | 5,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.30` | 49,490,000.00 USD | 49,490,000.00 USD | 1,640,000.00 USD | 5,130,000.00 USD | 5,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.50` | 25,900,000.00 USD | 25,900,000.00 USD | 295,480.00 USD | 3,460,000.00 USD | 6,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.50` | 59,620,000.00 USD | 59,620,000.00 USD | 1,320,000.00 USD | 6,930,000.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.55` | 5,930.00 USD | 7,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.65` | 9,740.00 USD | 17,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.70` | 41,560,000.00 USD | 41,560,000.00 USD | 980,300.00 USD | 5,100,000.00 USD | 9,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.70` | 64,610,000.00 USD | 64,610,000.00 USD | 742,060.00 USD | 1,370,000.00 USD | 2,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.85` | 269.86 USD | 17,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.90` | 50,160,000.00 USD | 50,160,000.00 USD | 1,180,000.00 USD | 3,110,000.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.90` | 69,460,000.00 USD | 69,460,000.00 USD | 57,310.00 USD | 1,660,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.95` | 1,020.00 USD | 18,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.05` | 3,610.00 USD | 22,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.10` | 59,740,000.00 USD | 59,740,000.00 USD | 1,710,000.00 USD | 2,910,000.00 USD | 4,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.10` | 75,860,000.00 USD | 75,860,000.00 USD | 179,190.00 USD | 2,070,000.00 USD | 4,150,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.15` | 1,110,000.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.25` | 8,190.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.30` | 68,660,000.00 USD | 68,660,000.00 USD | 3,350,000.00 USD | 3,300,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.30` | 82,610,000.00 USD | 82,610,000.00 USD | 798,000.00 USD | 3,060,000.00 USD | 2,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.35` | 92,570.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.45` | 335.15 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.50` | 73,950,000.00 USD | 73,950,000.00 USD | 1,380,000.00 USD | 3,290,000.00 USD | 619,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.50` | 86,850,000.00 USD | 86,850,000.00 USD | 2,240,000.00 USD | 1,490,000.00 USD | 504,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.55` | 11,890.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.65` | 3,000.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.70` | 96,880,000.00 USD | 96,880,000.00 USD | 4,390,000.00 USD | 7,340,000.00 USD | 11,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.70` | 90,610,000.00 USD | 90,610,000.00 USD | 0.00 USD | 2,490,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.75` | 24,780.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.85` | 410.38 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.90` | 105,430,000.00 USD | 105,430,000.00 USD | 825,740.00 USD | 1,760,000.00 USD | 5,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.90` | 98,740,000.00 USD | 98,740,000.00 USD | 2,860,000.00 USD | 1,420,000.00 USD | 3,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.95` | 10,100.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.05` | 40,190.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.10` | 110,690,000.00 USD | 110,690,000.00 USD | 2,030,000.00 USD | 2,360,000.00 USD | 877,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.10` | 104,530,000.00 USD | 104,530,000.00 USD | 48,160.00 USD | 1,210,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.15` | 51,840.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.25` | 298,790.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.30` | 115,820,000.00 USD | 115,820,000.00 USD | 300,700.00 USD | 2,120,000.00 USD | 2,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.30` | 108,140,000.00 USD | 108,140,000.00 USD | 883,050.00 USD | 1,600,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.35` | 180,560.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.50` | 123,470,000.00 USD | 123,470,000.00 USD | 2,200,000.00 USD | 1,260,000.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.50` | 116,600,000.00 USD | 116,600,000.00 USD | 2,640,000.00 USD | 765,300.00 USD | 5,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.55` | 969.30 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.65` | 99,220.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.70` | 130,790,000.00 USD | 130,790,000.00 USD | 1,940,000.00 USD | 2,250,000.00 USD | 3,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.70` | 119,020,000.00 USD | 119,020,000.00 USD | 504,370.00 USD | 1,900,000.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.75` | 19,020.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.85` | 16,850.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.90` | 136,740,000.00 USD | 136,740,000.00 USD | 1,760,000.00 USD | 2,410,000.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.90` | 132,120,000.00 USD | 132,120,000.00 USD | 3,480,000.00 USD | 3,730,000.00 USD | 5,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.95` | 5,080.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.05` | 765.96 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.10` | 150,610,000.00 USD | 150,610,000.00 USD | 8,660,000.00 USD | 2,680,000.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.10` | 141,890,000.00 USD | 141,890,000.00 USD | 3,020,000.00 USD | 3,990,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.15` | 11,950.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.25` | 769.50 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.30` | 160,810,000.00 USD | 160,810,000.00 USD | 3,460,000.00 USD | 3,950,000.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.30` | 163,270,000.00 USD | 163,270,000.00 USD | 7,710,000.00 USD | 4,690,000.00 USD | 8,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.45` | 118.70 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.50` | 176,960,000.00 USD | 176,960,000.00 USD | 3,050,000.00 USD | 3,960,000.00 USD | 9,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.50` | 178,540,000.00 USD | 178,540,000.00 USD | 2,950,000.00 USD | 738,480.00 USD | 11,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.55` | 2,790.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.65` | 2,640.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.70` | 186,830,000.00 USD | 186,830,000.00 USD | 2,320,000.00 USD | 841,470.00 USD | 6,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.70` | 188,540,000.00 USD | 188,540,000.00 USD | 2,950,000.00 USD | 484,140.00 USD | 6,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.85` | 310.64 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.90` | 192,540,000.00 USD | 192,540,000.00 USD | 2,230,000.00 USD | 823,320.00 USD | 2,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.90` | 197,250,000.00 USD | 197,250,000.00 USD | 3,710,000.00 USD | 867,880.00 USD | 4,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.95` | 1,560.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.05` | 4,930.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.10` | 198,540,000.00 USD | 198,540,000.00 USD | 2,830,000.00 USD | 1,270,000.00 USD | 1,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.10` | 202,900,000.00 USD | 202,900,000.00 USD | 1,470,000.00 USD | 159,070.00 USD | 4,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.25` | 1,170.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.30` | 203,270,000.00 USD | 203,270,000.00 USD | 1,650,000.00 USD | 1,450,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.30` | 208,960,000.00 USD | 208,960,000.00 USD | 2,700,000.00 USD | 807,930.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.45` | 175.19 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.50` | 207,600,000.00 USD | 207,600,000.00 USD | 1,510,000.00 USD | 785,070.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.50` | 212,610,000.00 USD | 212,610,000.00 USD | 1,240,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.65` | 26,740.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.70` | 209,490,000.00 USD | 209,490,000.00 USD | 1,110,000.00 USD | 661,840.00 USD | 121,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.70` | 213,410,000.00 USD | 213,410,000.00 USD | 766,460.00 USD | 14,010.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.75` | 2,120.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.90` | 214,020,000.00 USD | 214,020,000.00 USD | 1,510,000.00 USD | 1,530,000.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.90` | 234,690,000.00 USD | 234,690,000.00 USD | 17,210,000.00 USD | 294,050.00 USD | 3,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.95` | 4,670.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.05` | 692.50 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.10` | 218,980,000.00 USD | 218,980,000.00 USD | 2,380,000.00 USD | 1,360,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.10` | 240,930,000.00 USD | 240,930,000.00 USD | 4,750,000.00 USD | 140,720.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.15` | 11,000.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.25` | 346.92 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.30` | 220,800,000.00 USD | 220,800,000.00 USD | 334,720.00 USD | 717,010.00 USD | 769,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.30` | 256,610,000.00 USD | 256,610,000.00 USD | 15,130,000.00 USD | 133,780.00 USD | 417,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.35` | 385.50 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.45` | 3,300.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.50` | 227,390,000.00 USD | 227,390,000.00 USD | 1,770,000.00 USD | 1,090,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.50` | 279,020,000.00 USD | 279,020,000.00 USD | 13,780,000.00 USD | 1,770,000.00 USD | 6,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.65` | 4,360.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.70` | 232,590,000.00 USD | 232,590,000.00 USD | 1,610,000.00 USD | 971,510.00 USD | 2,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.70` | 291,240,000.00 USD | 291,240,000.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.75` | 261,580.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.85` | 13,560.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.90` | 238,400,000.00 USD | 238,400,000.00 USD | 2,080,000.00 USD | 2,200,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.90` | 309,270,000.00 USD | 309,270,000.00 USD | 9,120,000.00 USD | 2,880,000.00 USD | 6,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.95` | 827.44 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.05` | 1,400.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.10` | 245,500,000.00 USD | 245,500,000.00 USD | 2,840,000.00 USD | 1,270,000.00 USD | 2,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.10` | 338,200,000.00 USD | 338,200,000.00 USD | 11,570,000.00 USD | 8,350,000.00 USD | 9,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.15` | 1,180.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.25` | 722.45 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.30` | 249,190,000.00 USD | 249,190,000.00 USD | 1,350,000.00 USD | 1,350,000.00 USD | 984,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.30` | 359,780,000.00 USD | 359,780,000.00 USD | 7,320,000.00 USD | 6,380,000.00 USD | 7,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.35` | 10,440.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.45` | 12,640.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.50` | 253,200,000.00 USD | 253,200,000.00 USD | 1,430,000.00 USD | 1,220,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.50` | 371,810,000.00 USD | 371,810,000.00 USD | 4,410,000.00 USD | 2,350,000.00 USD | 5,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.55` | 464.20 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.65` | 1,070.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.70` | 258,990,000.00 USD | 258,990,000.00 USD | 1,720,000.00 USD | 982,920.00 USD | 3,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.70` | 392,000,000.00 USD | 392,000,000.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.75` | 199.02 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.90` | 260,470,000.00 USD | 260,470,000.00 USD | 486,940.00 USD | 283,560.00 USD | 706,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.90` | 412,860,000.00 USD | 412,860,000.00 USD | 5,970,000.00 USD | 5,350,000.00 USD | 9,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.95` | 125,660.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.05` | 329.86 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.10` | 262,300,000.00 USD | 262,300,000.00 USD | 299,230.00 USD | 436,680.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.10` | 425,670,000.00 USD | 425,670,000.00 USD | 5,580,000.00 USD | 4,400,000.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.15` | 6,410.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.25` | 1,040.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.30` | 262,490,000.00 USD | 262,490,000.00 USD | 94,380.00 USD | 96,460.00 USD | 1,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.30` | 430,010,000.00 USD | 430,010,000.00 USD | 2,410,000.00 USD | 1,310,000.00 USD | 623,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.35` | 2,710.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.45` | 527,250.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.50` | 263,110,000.00 USD | 263,110,000.00 USD | 245,610.00 USD | 180,000.00 USD | 186,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.50` | 447,780,000.00 USD | 447,780,000.00 USD | 5,600,000.00 USD | 5,850,000.00 USD | 6,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.55` | 4,180.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.65` | 247.22 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.70` | 263,320,000.00 USD | 263,320,000.00 USD | 65,040.00 USD | 150,210.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.70` | 459,530,000.00 USD | 459,530,000.00 USD | 3,430,000.00 USD | 3,740,000.00 USD | 4,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.75` | 750.82 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.85` | 103,700.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.90` | 264,370,000.00 USD | 264,370,000.00 USD | 171,160.00 USD | 683,690.00 USD | 193,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.90` | 468,420,000.00 USD | 468,420,000.00 USD | 3,110,000.00 USD | 1,880,000.00 USD | 3,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.95` | 592.26 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.05` | 33,380.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.10` | 265,760,000.00 USD | 265,760,000.00 USD | 706,860.00 USD | 457,510.00 USD | 226,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.10` | 479,020,000.00 USD | 479,020,000.00 USD | 4,910,000.00 USD | 2,870,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.15` | 4,030.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.30` | 266,920,000.00 USD | 266,920,000.00 USD | 281,270.00 USD | 484,380.00 USD | 391,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.30` | 487,420,000.00 USD | 487,420,000.00 USD | 3,400,000.00 USD | 2,850,000.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.35` | 252,220.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.45` | 32,940.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.50` | 267,610,000.00 USD | 267,610,000.00 USD | 229,790.00 USD | 216,810.00 USD | 239,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.50` | 491,820,000.00 USD | 491,820,000.00 USD | 1,520,000.00 USD | 1,440,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.70` | 269,740,000.00 USD | 269,740,000.00 USD | 565,590.00 USD | 249,950.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.70` | 499,910,000.00 USD | 499,910,000.00 USD | 1,820,000.00 USD | 2,330,000.00 USD | 3,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.85` | 478,970.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.90` | 270,210,000.00 USD | 270,210,000.00 USD | 10,160.00 USD | 156,020.00 USD | 305,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.90` | 504,970,000.00 USD | 504,970,000.00 USD | 789,400.00 USD | 1,150,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.95` | 82,630.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.05` | 17,260.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.10` | 271,250,000.00 USD | 271,250,000.00 USD | 97,170.00 USD | 366,280.00 USD | 580,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.10` | 509,080,000.00 USD | 509,080,000.00 USD | 1,630,000.00 USD | 799,480.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.15` | 3,060.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.25` | 34,950.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.30` | 271,620,000.00 USD | 271,620,000.00 USD | 82,550.00 USD | 174,420.00 USD | 110,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.30` | 509,530,000.00 USD | 509,530,000.00 USD | 0.00 USD | 451,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.35` | 766.48 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.45` | 49,740.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.50` | 272,740,000.00 USD | 272,740,000.00 USD | 50,930.00 USD | 253,000.00 USD | 815,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.50` | 510,780,000.00 USD | 510,780,000.00 USD | 5,920.00 USD | 286,950.00 USD | 954,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.55` | 221.55 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.65` | 1,820.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.70` | 273,020,000.00 USD | 273,020,000.00 USD | 54,110.00 USD | 0.00 USD | 230,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.70` | 511,760,000.00 USD | 511,760,000.00 USD | 523,660.00 USD | 10,400.00 USD | 444,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.75` | 11,710.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.85` | 143,340.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.90` | 273,320,000.00 USD | 273,320,000.00 USD | 83,370.00 USD | 73,830.00 USD | 136,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.90` | 512,280,000.00 USD | 512,280,000.00 USD | 173,590.00 USD | 20,610.00 USD | 331,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.05` | 1,080.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.10` | 273,420,000.00 USD | 273,420,000.00 USD | 0.00 USD | 99,900.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.10` | 512,540,000.00 USD | 512,540,000.00 USD | 5,950.00 USD | 248,110.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.15` | 1,150.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.25` | 116.91 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.30` | 273,450,000.00 USD | 273,450,000.00 USD | 33,880.00 USD | 1,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.30` | 513,670,000.00 USD | 513,670,000.00 USD | 303,300.00 USD | 464,990.00 USD | 359,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.35` | 3,470.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.45` | 108,080.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.50` | 274,150,000.00 USD | 274,150,000.00 USD | 163,220.00 USD | 120,280.00 USD | 413,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.50` | 514,070,000.00 USD | 514,070,000.00 USD | 395,570.00 USD | 3,960.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.55` | 117.23 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.60` | 274,270,000.00 USD | 274,270,000.00 USD | 118,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.65` | 5,050.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.70` | 515,800,000.00 USD | 515,800,000.00 USD | 557,190.00 USD | 529,990.00 USD | 640,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.85` | 3,230.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.90` | 517,240,000.00 USD | 517,240,000.00 USD | 363,550.00 USD | 494,000.00 USD | 580,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.95` | 3,170.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.05` | 163.58 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.10` | 518,070,000.00 USD | 518,070,000.00 USD | 289,830.00 USD | 185,250.00 USD | 354,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.30` | 519,230,000.00 USD | 519,230,000.00 USD | 503,000.00 USD | 91,380.00 USD | 569,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.35` | 407,490.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.45` | 342.58 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.50` | 519,470,000.00 USD | 519,470,000.00 USD | 230,320.00 USD | 4,290.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.55` | 356.04 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.65` | 42,030.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.70` | 520,650,000.00 USD | 520,650,000.00 USD | 550,380.00 USD | 185,990.00 USD | 444,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.85` | 459.17 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.90` | 522,450,000.00 USD | 522,450,000.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.95` | 2,440.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.10` | 524,820,000.00 USD | 524,820,000.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.15` | 194.97 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.25` | 2,750.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.30` | 526,880,000.00 USD | 526,880,000.00 USD | 936,750.00 USD | 321,390.00 USD | 800,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.35` | 14,530.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 143,200.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.55` | 28,380.00 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.65` | 10,470.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.75` | 575.90 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.85` | 1,090.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 4,450.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.05` | 196.56 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.15` | 1,710.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.35` | 390.84 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.45` | 841.45 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.55` | 892.40 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.75` | 169.86 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.85` | 15,880.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.95` | 223.90 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.15` | 291.59 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.35` | 1,910.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.45` | 5,670.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.55` | 844.13 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.65` | 707.44 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.75` | 118,640.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.85` | 108,760.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.05` | 406.98 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.15` | 9,560.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.25` | 1,940.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.35` | 263,390.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.45` | 3,360.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.55` | 102,200.00 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.65` | 3,220.00 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.75` | 303.71 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.85` | 104.74 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.95` | 21,840.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.05` | 31,900.00 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.25` | 2,150.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.35` | 39,970.00 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.45` | 3,310.00 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.65` | 584.72 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.85` | 27,340.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.05` | 569,550.00 USD | 6,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.15` | 1,100.00 USD | 6,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.25` | 17,810.00 USD | 6,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.35` | 878,270.00 USD | 7,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.55` | 43,020.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.75` | 160.89 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.85` | 289.62 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.95` | 441.77 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.05` | 4,450.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.25` | 180.19 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.35` | 4,960.00 USD | 7,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.55` | 2,040.00 USD | 7,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.65` | 113.15 USD | 7,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.05` | 156.85 USD | 7,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.15` | 4,860,000.00 USD | 12,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.35` | 11,610.00 USD | 12,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.55` | 188.08 USD | 12,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.65` | 23,530.00 USD | 12,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.75` | 10,360.00 USD | 12,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.95` | 353.85 USD | 12,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.05` | 4,460,000.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.15` | 4,140.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.45` | 30,080.00 USD | 16,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.55` | 1,110.00 USD | 16,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.75` | 309.94 USD | 16,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.85` | 18,610.00 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.95` | 28,010.00 USD | 16,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.05` | 12,470.00 USD | 16,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.25` | 240.88 USD | 16,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.35` | 57,850.00 USD | 16,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.55` | 8,970.00 USD | 16,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.75` | 1,790.00 USD | 16,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.85` | 96,440.00 USD | 17,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.15` | 2,980.00 USD | 17,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.45` | 619.11 USD | 17,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.55` | 1,190.00 USD | 17,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.95` | 13,290.00 USD | 17,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.15` | 960.72 USD | 17,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.55` | 5,940.00 USD | 17,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.75` | 105.92 USD | 17,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.05` | 935,440.00 USD | 17,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.15` | 500.81 USD | 17,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.25` | 3,920.00 USD | 17,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.35` | 357.26 USD | 17,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.45` | 17,500.00 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.65` | 116.52 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.95` | 1,650.00 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.05` | 525.42 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.25` | 124,110.00 USD | 18,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.35` | 2,330.00 USD | 18,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.45` | 1,960.00 USD | 18,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.65` | 697.39 USD | 18,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.05` | 586.76 USD | 18,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.15` | 121.67 USD | 18,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.25` | 23,360.00 USD | 18,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.35` | 114.40 USD | 18,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.45` | 46,110.00 USD | 18,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.55` | 3,080.00 USD | 18,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.65` | 675.60 USD | 18,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.75` | 8,660,000.00 USD | 26,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.95` | 9,550.00 USD | 26,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.05` | 208.83 USD | 26,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.35` | 5,320.00 USD | 26,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.45` | 590.87 USD | 26,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.55` | 4,610.00 USD | 26,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.65` | 851.91 USD | 26,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.75` | 4,600.00 USD | 26,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.95` | 110.84 USD | 26,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.05` | 810.50 USD | 26,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.15` | 470.54 USD | 26,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.35` | 4,090.00 USD | 26,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.45` | 117.60 USD | 26,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.65` | 30,830.00 USD | 26,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.85` | 3,870.00 USD | 26,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.05` | 2,030.00 USD | 26,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.35` | 16,190.00 USD | 26,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.65` | 4,840.00 USD | 26,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.85` | 388.66 USD | 26,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.95` | 10,510.00 USD | 26,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.05` | 116,190.00 USD | 27,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.35` | 195.09 USD | 27,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.65` | 788.62 USD | 27,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.75` | 18,730.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.85` | 32,440.00 USD | 27,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.05` | 603.95 USD | 27,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.15` | 822,240.00 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.25` | 38,770.00 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.35` | 164.27 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.55` | 910.74 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.65` | 127.06 USD | 27,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.75` | 2,210.00 USD | 27,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.85` | 490.83 USD | 27,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.05` | 13,180.00 USD | 28,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.35` | 145.99 USD | 28,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.65` | 2,210.00 USD | 28,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.85` | 503,820.00 USD | 28,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.95` | 2,070.00 USD | 28,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.05` | 188.71 USD | 28,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.25` | 1,560.00 USD | 28,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.45` | 219.52 USD | 28,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.65` | 3,590.00 USD | 28,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.85` | 3,100.00 USD | 28,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.95` | 106.88 USD | 28,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.05` | 11,940.00 USD | 28,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.15` | 712.29 USD | 28,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.35` | 3,960.00 USD | 28,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.55` | 8,730.00 USD | 28,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.65` | 66,570.00 USD | 28,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.85` | 49,280.00 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.95` | 47,950.00 USD | 28,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.05` | 103.78 USD | 28,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.15` | 8,440.00 USD | 28,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.55` | 30,060.00 USD | 28,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.65` | 156.37 USD | 28,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.75` | 151,200.00 USD | 28,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.85` | 1,600.00 USD | 28,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.95` | 100,970.00 USD | 29,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.05` | 12,620.00 USD | 29,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.25` | 11,590.00 USD | 29,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.35` | 6,400.00 USD | 29,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.85` | 3,250.00 USD | 29,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.95` | 504.37 USD | 29,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.55` | 136.55 USD | 29,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.65` | 1,110.00 USD | 29,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.95` | 48,960.00 USD | 29,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.05` | 1,530.00 USD | 29,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.15` | 2,850.00 USD | 29,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.85` | 2,810.00 USD | 29,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.05` | 9,810.00 USD | 29,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.15` | 41,450.00 USD | 29,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.25` | 45,220.00 USD | 29,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.45` | 7,310.00 USD | 29,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.75` | 2,360.00 USD | 29,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.15` | 552.43 USD | 29,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.35` | 1,670.00 USD | 29,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.45` | 253.80 USD | 29,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.55` | 494.01 USD | 29,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.75` | 4,870.00 USD | 29,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.85` | 41,280.00 USD | 29,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.95` | 394.66 USD | 29,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.05` | 4,980,000.00 USD | 34,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.15` | 13,370.00 USD | 34,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.35` | 158.60 USD | 34,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.45` | 4,870.00 USD | 34,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.55` | 702.75 USD | 34,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.65` | 74,520.00 USD | 34,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.95` | 2,600.00 USD | 34,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.05` | 3,080.00 USD | 34,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.15` | 22,890.00 USD | 34,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.25` | 1,070,000.00 USD | 35,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.35` | 867,610.00 USD | 36,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.45` | 247,540.00 USD | 36,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.55` | 236.39 USD | 36,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.65` | 780.49 USD | 36,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.75` | 4,900.00 USD | 36,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.95` | 112.14 USD | 36,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.15` | 2,430.00 USD | 36,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.45` | 19,240.00 USD | 36,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.65` | 21,940.00 USD | 36,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.75` | 28,420.00 USD | 36,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.85` | 595.68 USD | 36,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.15` | 1,330.00 USD | 36,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.35` | 22,260.00 USD | 36,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.45` | 595,460.00 USD | 37,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.55` | 103.36 USD | 37,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.65` | 104,880.00 USD | 37,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.05` | 3,750.00 USD | 37,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.65` | 1,240.00 USD | 37,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.15` | 1,760.00 USD | 37,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.45` | 29,480.00 USD | 37,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.85` | 5,850.00 USD | 37,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.05` | 88,930.00 USD | 37,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.15` | 88,760.00 USD | 37,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.25` | 2,770.00 USD | 37,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.35` | 7,330.00 USD | 37,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.55` | 3,390.00 USD | 37,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.65` | 587,730.00 USD | 38,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.95` | 3,070.00 USD | 38,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.05` | 166.17 USD | 38,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.15` | 1,730.00 USD | 38,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.35` | 1,580.00 USD | 38,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.45` | 204.96 USD | 38,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.55` | 1,000.00 USD | 38,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.65` | 237.72 USD | 38,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.75` | 2,470.00 USD | 38,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.85` | 522,270.00 USD | 38,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.95` | 517,820.00 USD | 39,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.15` | 102.22 USD | 39,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.35` | 278.90 USD | 39,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.45` | 5,800.00 USD | 39,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.55` | 344,780.00 USD | 39,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.75` | 93,700.00 USD | 39,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.05` | 161,460.00 USD | 39,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.15` | 1,380,000.00 USD | 41,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.55` | 116.65 USD | 41,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.65` | 16,030.00 USD | 41,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.75` | 16,320.00 USD | 41,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.95` | 178.44 USD | 41,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.05` | 2,930.00 USD | 41,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.25` | 123,390.00 USD | 41,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.55` | 346.26 USD | 41,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.65` | 17,300.00 USD | 41,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.75` | 2,370.00 USD | 41,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.05` | 1,740,000.00 USD | 43,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.15` | 3,180.00 USD | 43,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.45` | 38,210.00 USD | 43,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.75` | 1,100,000.00 USD | 44,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.95` | 1,920.00 USD | 44,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.05` | 44,540.00 USD | 44,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.15` | 1,470.00 USD | 44,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.25` | 200.97 USD | 44,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.35` | 286,550.00 USD | 44,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.45` | 3,150.00 USD | 44,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.55` | 423,220.00 USD | 45,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.75` | 1,570.00 USD | 45,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.95` | 44,550.00 USD | 45,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.05` | 479.05 USD | 45,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.15` | 1,060.00 USD | 45,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.25` | 761,340.00 USD | 45,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.35` | 2,300.00 USD | 45,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.65` | 8,340.00 USD | 45,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.05` | 223.37 USD | 45,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.15` | 292.89 USD | 45,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.25` | 2,340.00 USD | 45,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.45` | 4,240.00 USD | 45,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.75` | 363.66 USD | 45,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.95` | 2,180.00 USD | 45,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.05` | 117.84 USD | 45,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.35` | 4,710,000.00 USD | 50,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.55` | 267.55 USD | 50,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.05` | 7,800.00 USD | 50,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.25` | 18,300.00 USD | 50,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.35` | 3,560,000.00 USD | 54,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.45` | 5,220.00 USD | 54,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.65` | 310.17 USD | 54,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.15` | 49,270.00 USD | 54,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.25` | 660,450.00 USD | 54,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.35` | 297.39 USD | 54,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.45` | 100,280.00 USD | 54,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.55` | 189.06 USD | 54,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.65` | 654.25 USD | 54,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.75` | 92,600.00 USD | 55,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.05` | 79,830.00 USD | 55,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.55` | 1,410.00 USD | 55,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.75` | 3,520.00 USD | 55,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.05` | 44,690.00 USD | 55,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.45` | 27,950.00 USD | 55,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.65` | 1,760.00 USD | 55,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.75` | 496.82 USD | 55,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.15` | 683,000.00 USD | 55,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.25` | 5,640,000.00 USD | 61,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.35` | 655.83 USD | 61,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.45` | 320,900.00 USD | 61,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.65` | 85,580.00 USD | 61,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.05` | 2,240.00 USD | 61,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.35` | 1,530.00 USD | 61,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.55` | 114,830.00 USD | 62,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.75` | 142,240.00 USD | 62,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.95` | 144,610.00 USD | 62,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.25` | 16,230.00 USD | 62,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.65` | 107,780.00 USD | 62,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.75` | 608.69 USD | 62,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.95` | 1,060.00 USD | 62,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.75` | 121.17 USD | 62,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.85` | 786.48 USD | 62,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.95` | 206,830.00 USD | 62,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.15` | 198.18 USD | 62,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.85` | 829.25 USD | 62,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.15` | 996.90 USD | 62,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.25` | 14,070.00 USD | 62,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.55` | 6,670.00 USD | 62,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.65` | 68,020.00 USD | 62,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.55` | 3,460.00 USD | 62,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.65` | 115.68 USD | 62,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.75` | 1,890.00 USD | 62,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.05` | 122.68 USD | 62,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.15` | 151.34 USD | 62,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.25` | 440.81 USD | 62,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.35` | 19,740.00 USD | 62,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.65` | 325,850.00 USD | 63,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.65` | 180,130.00 USD | 63,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.75` | 38,210.00 USD | 63,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.05` | 20,360.00 USD | 63,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.45` | 111.44 USD | 63,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.75` | 3,460,000.00 USD | 66,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.95` | 19,590.00 USD | 66,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.05` | 2,520.00 USD | 66,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.45` | 51,940.00 USD | 66,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.65` | 343.57 USD | 66,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.15` | 38,090,000.00 USD | 105,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.45` | 16,540.00 USD | 105,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.85` | 695.40 USD | 105,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.05` | 285.44 USD | 105,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.15` | 104,490.00 USD | 105,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.25` | 245,010.00 USD | 105,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.35` | 205,490.00 USD | 105,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.45` | 1,980.00 USD | 105,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.75` | 146.79 USD | 105,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.05` | 1,200.00 USD | 105,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.15` | 105,090.00 USD | 105,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.35` | 19,830.00 USD | 105,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.45` | 4,020.00 USD | 105,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.65` | 4,390.00 USD | 105,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.75` | 25,680.00 USD | 105,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.25` | 625.69 USD | 105,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.55` | 141,240.00 USD | 105,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.45` | 47,190.00 USD | 105,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.55` | 1,030,000.00 USD | 106,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.65` | 637.76 USD | 106,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.85` | 4,930.00 USD | 106,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.95` | 78,300.00 USD | 107,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.05` | 267,070.00 USD | 107,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.55` | 206,920.00 USD | 107,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.55` | 9,290.00 USD | 107,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.95` | 3,600,000.00 USD | 111,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.15` | 2,030.00 USD | 111,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.25` | 1,360.00 USD | 111,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.55` | 38,150.00 USD | 111,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.05` | 780.33 USD | 111,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.25` | 18,120.00 USD | 111,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.55` | 254.17 USD | 111,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.15` | 3,990.00 USD | 111,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.85` | 52,820.00 USD | 111,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.25` | 1,680.00 USD | 111,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.65` | 7,650.00 USD | 111,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.95` | 176,140.00 USD | 111,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.15` | 1,370,000.00 USD | 112,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.25` | 737.29 USD | 112,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.45` | 2,770.00 USD | 112,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.55` | 1,220.00 USD | 112,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.65` | 137.38 USD | 112,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.15` | 247.58 USD | 112,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.45` | 2,440.00 USD | 112,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.75` | 2,800.00 USD | 112,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.85` | 2,190.00 USD | 112,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.45` | 232.44 USD | 112,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.85` | 1,560.00 USD | 112,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.55` | 231.92 USD | 112,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.65` | 29,110.00 USD | 112,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.75` | 4,070.00 USD | 112,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.95` | 1,450.00 USD | 112,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.25` | 456.09 USD | 112,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.55` | 1,000.00 USD | 112,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.85` | 307.56 USD | 112,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.95` | 284,930.00 USD | 113,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.05` | 385,490.00 USD | 113,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.15` | 148.32 USD | 113,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.45` | 620.87 USD | 113,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.95` | 13,570,000.00 USD | 127,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.15` | 62,720.00 USD | 127,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.95` | 322.48 USD | 127,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.15` | 3,290.00 USD | 127,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.95` | 192.95 USD | 127,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.15` | 2,170.00 USD | 127,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.55` | 114,580.00 USD | 127,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.05` | 543.34 USD | 127,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.35` | 9,380.00 USD | 127,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.55` | 89,060.00 USD | 127,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.75` | 266.81 USD | 127,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.95` | 20,000.00 USD | 127,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.25` | 18,480.00 USD | 127,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.35` | 27,160.00 USD | 127,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.65` | 142,140.00 USD | 127,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `19.65` | 122,450,000.00 USD | 0.00 USD | 712.31 USD | `-79.94%` | `36.25` |
| `Live` | `Long` | `19.95` | 122,450,000.00 USD | 0.00 USD | 9,980.00 USD | `-79.63%` | `500.00` |
| `Live` | `Long` | `20.25` | 122,440,000.00 USD | 0.00 USD | 207.76 USD | `-79.33%` | `10.26` |
| `Live` | `Long` | `20.35` | 122,440,000.00 USD | 0.00 USD | 386.65 USD | `-79.23%` | `19.00` |
| `Live` | `Long` | `20.55` | 122,440,000.00 USD | 0.00 USD | 5,120.00 USD | `-79.02%` | `249.23` |
| `Live` | `Long` | `21.05` | 122,440,000.00 USD | 0.00 USD | 1,050.00 USD | `-78.51%` | `50.00` |
| `Live` | `Long` | `21.25` | 122,440,000.00 USD | 0.00 USD | 276.68 USD | `-78.31%` | `13.02` |
| `Live` | `Long` | `21.35` | 122,440,000.00 USD | 0.00 USD | 3,990.00 USD | `-78.21%` | `186.87` |
| `Live` | `Long` | `21.45` | 122,430,000.00 USD | 0.00 USD | 161.73 USD | `-78.10%` | `7.54` |
| `Live` | `Long` | `21.65` | 122,430,000.00 USD | 0.00 USD | 5,020.00 USD | `-77.90%` | `231.88` |
| `Live` | `Long` | `21.75` | 122,430,000.00 USD | 0.00 USD | 4,630.00 USD | `-77.80%` | `212.70` |
| `Live` | `Long` | `22.05` | 122,420,000.00 USD | 0.00 USD | 795,690.00 USD | `-77.49%` | `36,085.73` |
| `Live` | `Long` | `22.25` | 121,630,000.00 USD | 0.00 USD | 132.39 USD | `-77.29%` | `5.95` |
| `Live` | `Long` | `22.45` | 121,630,000.00 USD | 0.00 USD | 111.13 USD | `-77.08%` | `4.95` |
| `Live` | `Long` | `22.75` | 121,630,000.00 USD | 0.00 USD | 8,390.00 USD | `-76.78%` | `369.00` |
| `Live` | `Long` | `22.95` | 121,620,000.00 USD | 0.00 USD | 2,300.00 USD | `-76.57%` | `100.00` |
| `Live` | `Long` | `23.05` | 121,620,000.00 USD | 0.00 USD | 1,150.00 USD | `-76.47%` | `50.00` |
| `Live` | `Long` | `23.15` | 121,620,000.00 USD | 0.00 USD | 243.31 USD | `-76.37%` | `10.51` |
| `Live` | `Long` | `23.25` | 121,620,000.00 USD | 0.00 USD | 12,170.00 USD | `-76.27%` | `523.23` |
| `Live` | `Long` | `23.35` | 121,600,000.00 USD | 0.00 USD | 21,070.00 USD | `-76.16%` | `902.43` |
| `Live` | `Long` | `23.45` | 121,580,000.00 USD | 0.00 USD | 1,380.00 USD | `-76.06%` | `58.86` |
| `Live` | `Long` | `23.55` | 121,580,000.00 USD | 0.00 USD | 14,180.00 USD | `-75.96%` | `602.03` |
| `Live` | `Long` | `24.35` | 121,570,000.00 USD | 0.00 USD | 1,350.00 USD | `-75.14%` | `55.27` |
| `Live` | `Long` | `24.55` | 121,570,000.00 USD | 0.00 USD | 4,530.00 USD | `-74.94%` | `184.67` |
| `Live` | `Long` | `24.95` | 121,560,000.00 USD | 0.00 USD | 1,680.00 USD | `-74.53%` | `67.33` |
| `Live` | `Long` | `25.05` | 121,560,000.00 USD | 0.00 USD | 1,250.00 USD | `-74.43%` | `50.00` |
| `Live` | `Long` | `25.15` | 121,560,000.00 USD | 0.00 USD | 2,010.00 USD | `-74.33%` | `80.00` |
| `Live` | `Long` | `25.45` | 121,560,000.00 USD | 0.00 USD | 1,200.00 USD | `-74.02%` | `47.25` |
| `Live` | `Long` | `25.75` | 121,550,000.00 USD | 0.00 USD | 148,070.00 USD | `-73.71%` | `5,750.44` |
| `Live` | `Long` | `25.85` | 121,410,000.00 USD | 0.00 USD | 14,530.00 USD | `-73.61%` | `562.26` |
| `Live` | `Long` | `25.95` | 121,390,000.00 USD | 0.00 USD | 3,090.00 USD | `-73.51%` | `119.10` |
| `Live` | `Long` | `26.05` | 121,390,000.00 USD | 0.00 USD | 5,910.00 USD | `-73.41%` | `226.73` |
| `Live` | `Long` | `26.25` | 121,380,000.00 USD | 0.00 USD | 271.69 USD | `-73.20%` | `10.35` |
| `Live` | `Long` | `26.35` | 121,380,000.00 USD | 0.00 USD | 475.09 USD | `-73.10%` | `18.03` |
| `Live` | `Long` | `26.45` | 121,380,000.00 USD | 0.00 USD | 856.45 USD | `-73.00%` | `32.38` |
| `Live` | `Long` | `26.65` | 121,380,000.00 USD | 0.00 USD | 9,090.00 USD | `-72.80%` | `341.04` |
| `Live` | `Long` | `26.95` | 121,370,000.00 USD | 0.00 USD | 40,740.00 USD | `-72.49%` | `1,511.84` |
| `Live` | `Long` | `27.35` | 121,330,000.00 USD | 0.00 USD | 3,500.00 USD | `-72.08%` | `127.82` |
| `Live` | `Long` | `27.45` | 121,330,000.00 USD | 0.00 USD | 686.25 USD | `-71.98%` | `25.00` |
| `Live` | `Long` | `27.55` | 121,330,000.00 USD | 0.00 USD | 2,480.00 USD | `-71.88%` | `90.00` |
| `Live` | `Long` | `27.85` | 121,320,000.00 USD | 0.00 USD | 412.18 USD | `-71.57%` | `14.80` |
| `Live` | `Long` | `27.95` | 121,320,000.00 USD | 0.00 USD | 84,260.00 USD | `-71.47%` | `3,014.66` |
| `Live` | `Long` | `28.05` | 121,240,000.00 USD | 0.00 USD | 17,440.00 USD | `-71.37%` | `621.62` |
| `Live` | `Long` | `28.15` | 121,220,000.00 USD | 0.00 USD | 62,890.00 USD | `-71.26%` | `2,234.01` |
| `Live` | `Long` | `28.35` | 121,160,000.00 USD | 0.00 USD | 6,200.00 USD | `-71.06%` | `218.55` |
| `Live` | `Long` | `28.45` | 121,150,000.00 USD | 0.00 USD | 113.80 USD | `-70.96%` | `4.00` |
| `Live` | `Long` | `28.55` | 121,150,000.00 USD | 0.00 USD | 2,280.00 USD | `-70.86%` | `79.92` |
| `Live` | `Long` | `28.65` | 121,150,000.00 USD | 0.00 USD | 16,880.00 USD | `-70.75%` | `589.18` |
| `Live` | `Long` | `28.75` | 121,130,000.00 USD | 0.00 USD | 254.72 USD | `-70.65%` | `8.86` |
| `Live` | `Long` | `28.85` | 121,130,000.00 USD | 0.00 USD | 727.60 USD | `-70.55%` | `25.22` |
| `Live` | `Long` | `28.95` | 121,130,000.00 USD | 0.00 USD | 9,840.00 USD | `-70.45%` | `340.00` |
| `Live` | `Long` | `29.35` | 121,120,000.00 USD | 0.00 USD | 121.51 USD | `-70.04%` | `4.14` |
| `Live` | `Long` | `29.45` | 121,120,000.00 USD | 0.00 USD | 10,580.00 USD | `-69.94%` | `359.09` |
| `Live` | `Long` | `29.95` | 121,110,000.00 USD | 0.00 USD | 239.60 USD | `-69.43%` | `8.00` |
| `Live` | `Long` | `30.05` | 121,110,000.00 USD | 0.00 USD | 3,010.00 USD | `-69.32%` | `100.04` |
| `Live` | `Long` | `30.15` | 121,110,000.00 USD | 0.00 USD | 50,570.00 USD | `-69.22%` | `1,677.30` |
| `Live` | `Long` | `30.35` | 121,060,000.00 USD | 0.00 USD | 4,230.00 USD | `-69.02%` | `139.36` |
| `Live` | `Long` | `30.55` | 121,050,000.00 USD | 0.00 USD | 526,290.00 USD | `-68.81%` | `17,227.29` |
| `Live` | `Long` | `30.65` | 120,530,000.00 USD | 0.00 USD | 233.86 USD | `-68.71%` | `7.63` |
| `Live` | `Long` | `30.85` | 120,530,000.00 USD | 0.00 USD | 69,880.00 USD | `-68.51%` | `2,265.28` |
| `Live` | `Long` | `31.05` | 120,460,000.00 USD | 0.00 USD | 621.00 USD | `-68.30%` | `20.00` |
| `Live` | `Long` | `31.15` | 120,460,000.00 USD | 0.00 USD | 160.11 USD | `-68.20%` | `5.14` |
| `Live` | `Long` | `31.45` | 120,460,000.00 USD | 0.00 USD | 278.33 USD | `-67.90%` | `8.85` |
| `Live` | `Long` | `31.85` | 120,460,000.00 USD | 0.00 USD | 789.24 USD | `-67.49%` | `24.78` |
| `Live` | `Long` | `31.95` | 120,460,000.00 USD | 0.00 USD | 19,970.00 USD | `-67.38%` | `625.00` |
| `Live` | `Long` | `32.15` | 120,440,000.00 USD | 0.00 USD | 1,030.00 USD | `-67.18%` | `31.94` |
| `Live` | `Long` | `32.25` | 120,440,000.00 USD | 0.00 USD | 3,900.00 USD | `-67.08%` | `120.98` |
| `Live` | `Long` | `32.45` | 120,430,000.00 USD | 0.00 USD | 4,420.00 USD | `-66.87%` | `136.10` |
| `Live` | `Long` | `32.85` | 120,430,000.00 USD | 0.00 USD | 5,240.00 USD | `-66.47%` | `159.61` |
| `Live` | `Long` | `33.05` | 120,420,000.00 USD | 0.00 USD | 274.98 USD | `-66.26%` | `8.32` |
| `Live` | `Long` | `33.25` | 120,420,000.00 USD | 0.00 USD | 489.11 USD | `-66.06%` | `14.71` |
| `Live` | `Long` | `33.45` | 120,420,000.00 USD | 0.00 USD | 1,810.00 USD | `-65.85%` | `54.25` |
| `Live` | `Long` | `33.55` | 120,420,000.00 USD | 0.00 USD | 559.28 USD | `-65.75%` | `16.67` |
| `Live` | `Long` | `33.65` | 120,420,000.00 USD | 0.00 USD | 962.39 USD | `-65.65%` | `28.60` |
| `Live` | `Long` | `33.75` | 120,420,000.00 USD | 0.00 USD | 40,500.00 USD | `-65.55%` | `1,200.00` |
| `Live` | `Long` | `33.85` | 120,380,000.00 USD | 0.00 USD | 958.63 USD | `-65.45%` | `28.32` |
| `Live` | `Long` | `34.05` | 120,380,000.00 USD | 0.00 USD | 395.66 USD | `-65.24%` | `11.62` |
| `Live` | `Long` | `34.35` | 120,380,000.00 USD | 0.00 USD | 842.61 USD | `-64.93%` | `24.53` |
| `Live` | `Long` | `34.55` | 120,380,000.00 USD | 0.00 USD | 9,070.00 USD | `-64.73%` | `262.64` |
| `Live` | `Long` | `34.65` | 120,370,000.00 USD | 0.00 USD | 486.14 USD | `-64.63%` | `14.03` |
| `Live` | `Long` | `34.75` | 120,370,000.00 USD | 0.00 USD | 54,920.00 USD | `-64.53%` | `1,580.51` |
| `Live` | `Long` | `34.85` | 120,310,000.00 USD | 0.00 USD | 1,930.00 USD | `-64.42%` | `55.47` |
| `Live` | `Long` | `34.95` | 120,310,000.00 USD | 0.00 USD | 6,620,000.00 USD | `-64.32%` | `189,537.46` |
| `Live` | `Long` | `35.05` | 113,680,000.00 USD | 0.00 USD | 37,720.00 USD | `-64.22%` | `1,076.17` |
| `Live` | `Long` | `35.15` | 113,650,000.00 USD | 0.00 USD | 9,310.00 USD | `-64.12%` | `264.96` |
| `Live` | `Long` | `35.25` | 113,640,000.00 USD | 0.00 USD | 4,490.00 USD | `-64.02%` | `127.29` |
| `Live` | `Long` | `35.35` | 113,630,000.00 USD | 0.00 USD | 2,900.00 USD | `-63.91%` | `82.13` |
| `Live` | `Long` | `35.55` | 113,630,000.00 USD | 0.00 USD | 107.01 USD | `-63.71%` | `3.01` |
| `Live` | `Long` | `35.65` | 113,630,000.00 USD | 0.00 USD | 5,650.00 USD | `-63.61%` | `158.58` |
| `Live` | `Long` | `35.75` | 113,620,000.00 USD | 0.00 USD | 4,840.00 USD | `-63.51%` | `135.34` |
| `Live` | `Long` | `35.85` | 113,620,000.00 USD | 0.00 USD | 1,570.00 USD | `-63.40%` | `43.67` |
| `Live` | `Long` | `35.95` | 113,620,000.00 USD | 0.00 USD | 1,990.00 USD | `-63.30%` | `55.37` |
| `Live` | `Long` | `36.05` | 113,620,000.00 USD | 0.00 USD | 6,700.00 USD | `-63.20%` | `185.99` |
| `Live` | `Long` | `36.15` | 113,610,000.00 USD | 0.00 USD | 15,480.00 USD | `-63.10%` | `428.23` |
| `Live` | `Long` | `36.25` | 113,590,000.00 USD | 0.00 USD | 619.51 USD | `-63.00%` | `17.09` |
| `Live` | `Long` | `36.35` | 113,590,000.00 USD | 0.00 USD | 4,550.00 USD | `-62.89%` | `125.26` |
| `Live` | `Long` | `36.45` | 113,590,000.00 USD | 0.00 USD | 2,410.00 USD | `-62.79%` | `66.24` |
| `Live` | `Long` | `36.55` | 113,590,000.00 USD | 0.00 USD | 50,040.00 USD | `-62.69%` | `1,368.98` |
| `Live` | `Long` | `36.65` | 113,540,000.00 USD | 0.00 USD | 2,060.00 USD | `-62.59%` | `56.20` |
| `Live` | `Long` | `36.75` | 113,530,000.00 USD | 0.00 USD | 1,740.00 USD | `-62.48%` | `47.31` |
| `Live` | `Long` | `36.95` | 113,530,000.00 USD | 0.00 USD | 1,660.00 USD | `-62.28%` | `45.00` |
| `Live` | `Long` | `37.15` | 113,530,000.00 USD | 0.00 USD | 302,500.00 USD | `-62.08%` | `8,142.56` |
| `Live` | `Long` | `37.25` | 113,230,000.00 USD | 0.00 USD | 373.62 USD | `-61.97%` | `10.03` |
| `Live` | `Long` | `37.35` | 113,230,000.00 USD | 0.00 USD | 19,600.00 USD | `-61.87%` | `524.75` |
| `Live` | `Long` | `37.55` | 113,210,000.00 USD | 0.00 USD | 262.85 USD | `-61.67%` | `7.00` |
| `Live` | `Long` | `37.65` | 113,210,000.00 USD | 0.00 USD | 6,000.00 USD | `-61.57%` | `159.30` |
| `Live` | `Long` | `37.75` | 113,200,000.00 USD | 0.00 USD | 267.27 USD | `-61.46%` | `7.08` |
| `Live` | `Long` | `37.95` | 113,200,000.00 USD | 0.00 USD | 4,380.00 USD | `-61.26%` | `115.44` |
| `Live` | `Long` | `38.05` | 113,200,000.00 USD | 0.00 USD | 858,390.00 USD | `-61.16%` | `22,559.50` |
| `Live` | `Long` | `38.25` | 112,340,000.00 USD | 0.00 USD | 191,250.00 USD | `-60.95%` | `5,000.00` |
| `Live` | `Long` | `38.35` | 112,150,000.00 USD | 0.00 USD | 287.63 USD | `-60.85%` | `7.50` |
| `Live` | `Long` | `38.45` | 112,150,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-60.75%` | `78,015.00` |
| `Live` | `Long` | `38.65` | 109,150,000.00 USD | 0.00 USD | 107,910.00 USD | `-60.55%` | `2,791.94` |
| `Live` | `Long` | `38.75` | 109,040,000.00 USD | 0.00 USD | 736.64 USD | `-60.44%` | `19.01` |
| `Live` | `Long` | `38.85` | 109,040,000.00 USD | 0.00 USD | 4,270.00 USD | `-60.34%` | `109.96` |
| `Live` | `Long` | `38.95` | 109,030,000.00 USD | 0.00 USD | 607.62 USD | `-60.24%` | `15.60` |
| `Live` | `Long` | `39.05` | 109,030,000.00 USD | 0.00 USD | 51,130.00 USD | `-60.14%` | `1,309.35` |
| `Live` | `Long` | `39.35` | 108,980,000.00 USD | 0.00 USD | 54,790.00 USD | `-59.83%` | `1,392.49` |
| `Live` | `Long` | `39.45` | 108,930,000.00 USD | 0.00 USD | 258.40 USD | `-59.73%` | `6.55` |
| `Live` | `Long` | `39.55` | 108,930,000.00 USD | 0.00 USD | 424.37 USD | `-59.63%` | `10.73` |
| `Live` | `Long` | `39.65` | 108,930,000.00 USD | 0.00 USD | 13,450.00 USD | `-59.52%` | `339.31` |
| `Live` | `Long` | `39.75` | 108,910,000.00 USD | 0.00 USD | 2,890.00 USD | `-59.42%` | `72.81` |
| `Live` | `Long` | `39.85` | 108,910,000.00 USD | 0.00 USD | 1,270.00 USD | `-59.32%` | `31.86` |
| `Live` | `Long` | `40.05` | 108,910,000.00 USD | 0.00 USD | 1,510.00 USD | `-59.12%` | `37.77` |
| `Live` | `Long` | `40.15` | 108,910,000.00 USD | 0.00 USD | 2,510.00 USD | `-59.01%` | `62.48` |
| `Live` | `Long` | `40.25` | 108,910,000.00 USD | 0.00 USD | 632.73 USD | `-58.91%` | `15.72` |
| `Live` | `Long` | `40.35` | 108,910,000.00 USD | 0.00 USD | 120,110.00 USD | `-58.81%` | `2,976.73` |
| `Live` | `Long` | `40.55` | 108,790,000.00 USD | 0.00 USD | 3,160.00 USD | `-58.61%` | `77.90` |
| `Live` | `Long` | `40.65` | 108,780,000.00 USD | 0.00 USD | 2,030.00 USD | `-58.50%` | `50.00` |
| `Live` | `Long` | `40.75` | 108,780,000.00 USD | 0.00 USD | 9,610.00 USD | `-58.40%` | `235.71` |
| `Live` | `Long` | `40.85` | 108,770,000.00 USD | 0.00 USD | 1,050,000.00 USD | `-58.30%` | `25,676.48` |
| `Live` | `Long` | `40.95` | 107,720,000.00 USD | 0.00 USD | 204,890.00 USD | `-58.20%` | `5,003.47` |
| `Live` | `Long` | `41.05` | 107,520,000.00 USD | 0.00 USD | 4,600.00 USD | `-58.10%` | `112.05` |
| `Live` | `Long` | `41.15` | 107,510,000.00 USD | 0.00 USD | 1,070.00 USD | `-57.99%` | `26.08` |
| `Live` | `Long` | `41.25` | 107,510,000.00 USD | 0.00 USD | 471.49 USD | `-57.89%` | `11.43` |
| `Live` | `Long` | `41.35` | 107,510,000.00 USD | 0.00 USD | 1,850.00 USD | `-57.79%` | `44.63` |
| `Live` | `Long` | `41.55` | 107,510,000.00 USD | 0.00 USD | 15,430.00 USD | `-57.58%` | `371.31` |
| `Live` | `Long` | `41.65` | 107,490,000.00 USD | 0.00 USD | 770.11 USD | `-57.48%` | `18.49` |
| `Live` | `Long` | `41.75` | 107,490,000.00 USD | 0.00 USD | 588.26 USD | `-57.38%` | `14.09` |
| `Live` | `Long` | `41.85` | 107,490,000.00 USD | 0.00 USD | 1,020.00 USD | `-57.28%` | `24.39` |
| `Live` | `Long` | `41.95` | 107,490,000.00 USD | 0.00 USD | 48,400.00 USD | `-57.18%` | `1,153.84` |
| `Live` | `Long` | `42.05` | 107,440,000.00 USD | 0.00 USD | 1,120.00 USD | `-57.07%` | `26.56` |
| `Live` | `Long` | `42.15` | 107,440,000.00 USD | 0.00 USD | 2,790.00 USD | `-56.97%` | `66.27` |
| `Live` | `Long` | `42.25` | 107,440,000.00 USD | 0.00 USD | 146.19 USD | `-56.87%` | `3.46` |
| `Live` | `Long` | `42.35` | 107,440,000.00 USD | 0.00 USD | 198.62 USD | `-56.77%` | `4.69` |
| `Live` | `Long` | `42.45` | 107,440,000.00 USD | 0.00 USD | 5,920.00 USD | `-56.67%` | `139.56` |
| `Live` | `Long` | `42.55` | 107,430,000.00 USD | 0.00 USD | 8,210.00 USD | `-56.56%` | `193.00` |
| `Live` | `Long` | `42.65` | 107,420,000.00 USD | 0.00 USD | 5,190.00 USD | `-56.46%` | `121.71` |
| `Live` | `Long` | `42.75` | 107,420,000.00 USD | 0.00 USD | 315,460.00 USD | `-56.36%` | `7,379.19` |
| `Live` | `Long` | `42.85` | 107,100,000.00 USD | 0.00 USD | 46,180.00 USD | `-56.26%` | `1,077.62` |
| `Live` | `Long` | `43.25` | 107,060,000.00 USD | 0.00 USD | 1,080.00 USD | `-55.85%` | `25.00` |
| `Live` | `Long` | `43.35` | 107,060,000.00 USD | 0.00 USD | 5,420.00 USD | `-55.75%` | `125.05` |
| `Live` | `Long` | `43.45` | 107,050,000.00 USD | 0.00 USD | 440.15 USD | `-55.65%` | `10.13` |
| `Live` | `Long` | `43.55` | 107,050,000.00 USD | 0.00 USD | 298.75 USD | `-55.54%` | `6.86` |
| `Live` | `Long` | `43.65` | 107,050,000.00 USD | 0.00 USD | 213.01 USD | `-55.44%` | `4.88` |
| `Live` | `Long` | `43.85` | 107,050,000.00 USD | 0.00 USD | 69,410.00 USD | `-55.24%` | `1,582.81` |
| `Live` | `Long` | `43.95` | 106,980,000.00 USD | 0.00 USD | 1,120.00 USD | `-55.13%` | `25.51` |
| `Live` | `Long` | `44.05` | 106,980,000.00 USD | 0.00 USD | 11,530.00 USD | `-55.03%` | `261.82` |
| `Live` | `Long` | `44.25` | 106,970,000.00 USD | 0.00 USD | 6,640.00 USD | `-54.83%` | `150.09` |
| `Live` | `Long` | `44.35` | 106,960,000.00 USD | 0.00 USD | 8,950.00 USD | `-54.73%` | `201.80` |
| `Live` | `Long` | `44.45` | 106,950,000.00 USD | 0.00 USD | 10,180.00 USD | `-54.62%` | `229.02` |
| `Live` | `Long` | `44.55` | 106,940,000.00 USD | 0.00 USD | 686,110.00 USD | `-54.52%` | `15,400.85` |
| `Live` | `Long` | `44.65` | 106,260,000.00 USD | 0.00 USD | 4,280.00 USD | `-54.42%` | `95.95` |
| `Live` | `Long` | `44.75` | 106,250,000.00 USD | 0.00 USD | 37,670.00 USD | `-54.32%` | `841.69` |
| `Live` | `Long` | `44.85` | 106,210,000.00 USD | 0.00 USD | 3,670,000.00 USD | `-54.22%` | `81,862.42` |
| `Live` | `Long` | `44.95` | 102,540,000.00 USD | 0.00 USD | 6,960.00 USD | `-54.11%` | `154.85` |
| `Live` | `Long` | `45.05` | 102,540,000.00 USD | 0.00 USD | 19,040.00 USD | `-54.01%` | `422.54` |
| `Live` | `Long` | `45.15` | 102,520,000.00 USD | 0.00 USD | 2,210.00 USD | `-53.91%` | `49.04` |
| `Live` | `Long` | `45.35` | 102,510,000.00 USD | 0.00 USD | 31,340.00 USD | `-53.71%` | `691.07` |
| `Live` | `Long` | `45.45` | 102,480,000.00 USD | 0.00 USD | 9,480.00 USD | `-53.60%` | `208.64` |
| `Live` | `Long` | `45.55` | 102,470,000.00 USD | 0.00 USD | 7,940.00 USD | `-53.50%` | `174.26` |
| `Live` | `Long` | `45.65` | 102,470,000.00 USD | 0.00 USD | 319.09 USD | `-53.40%` | `6.99` |
| `Live` | `Long` | `45.75` | 102,460,000.00 USD | 0.00 USD | 9,450.00 USD | `-53.30%` | `206.46` |
| `Live` | `Long` | `45.85` | 102,460,000.00 USD | 0.00 USD | 458.50 USD | `-53.20%` | `10.00` |
| `Live` | `Long` | `45.95` | 102,450,000.00 USD | 0.00 USD | 26,070.00 USD | `-53.09%` | `567.34` |
| `Live` | `Long` | `46.05` | 102,430,000.00 USD | 0.00 USD | 435.63 USD | `-52.99%` | `9.46` |
| `Live` | `Long` | `46.25` | 102,430,000.00 USD | 0.00 USD | 3,580.00 USD | `-52.79%` | `77.46` |
| `Live` | `Long` | `46.45` | 102,420,000.00 USD | 0.00 USD | 4,560.00 USD | `-52.58%` | `98.25` |
| `Live` | `Long` | `46.55` | 102,420,000.00 USD | 0.00 USD | 3,190.00 USD | `-52.48%` | `68.63` |
| `Live` | `Long` | `46.65` | 102,420,000.00 USD | 0.00 USD | 11,380.00 USD | `-52.38%` | `243.90` |
| `Live` | `Long` | `46.75` | 102,410,000.00 USD | 0.00 USD | 537.62 USD | `-52.28%` | `11.50` |
| `Live` | `Long` | `46.85` | 102,410,000.00 USD | 0.00 USD | 592.18 USD | `-52.17%` | `12.64` |
| `Live` | `Long` | `46.95` | 102,400,000.00 USD | 0.00 USD | 2,360.00 USD | `-52.07%` | `50.18` |
| `Live` | `Long` | `47.15` | 102,400,000.00 USD | 0.00 USD | 2,950.00 USD | `-51.87%` | `62.62` |
| `Live` | `Long` | `47.25` | 102,400,000.00 USD | 0.00 USD | 8,650.00 USD | `-51.77%` | `183.03` |
| `Live` | `Long` | `47.45` | 102,390,000.00 USD | 0.00 USD | 743,490.00 USD | `-51.56%` | `15,668.95` |
| `Live` | `Long` | `47.55` | 101,650,000.00 USD | 0.00 USD | 2,540.00 USD | `-51.46%` | `53.50` |
| `Live` | `Long` | `47.65` | 101,640,000.00 USD | 0.00 USD | 98,780.00 USD | `-51.36%` | `2,073.02` |
| `Live` | `Long` | `47.75` | 101,550,000.00 USD | 0.00 USD | 58,290.00 USD | `-51.26%` | `1,220.77` |
| `Live` | `Long` | `47.95` | 101,490,000.00 USD | 0.00 USD | 2,260.00 USD | `-51.05%` | `47.05` |
| `Live` | `Long` | `48.05` | 101,490,000.00 USD | 0.00 USD | 13,300.00 USD | `-50.95%` | `276.89` |
| `Live` | `Long` | `48.15` | 101,470,000.00 USD | 0.00 USD | 6,450.00 USD | `-50.85%` | `133.97` |
| `Live` | `Long` | `48.25` | 101,470,000.00 USD | 0.00 USD | 2,430.00 USD | `-50.75%` | `50.45` |
| `Live` | `Long` | `48.35` | 101,460,000.00 USD | 0.00 USD | 5,840.00 USD | `-50.64%` | `120.82` |
| `Live` | `Long` | `48.45` | 101,460,000.00 USD | 0.00 USD | 2,930.00 USD | `-50.54%` | `60.44` |
| `Live` | `Long` | `48.55` | 101,450,000.00 USD | 0.00 USD | 97,250.00 USD | `-50.44%` | `2,003.13` |
| `Live` | `Long` | `48.65` | 101,360,000.00 USD | 0.00 USD | 9,260.00 USD | `-50.34%` | `190.42` |
| `Live` | `Long` | `48.75` | 101,350,000.00 USD | 0.00 USD | 1,860.00 USD | `-50.23%` | `38.17` |
| `Live` | `Long` | `48.85` | 101,350,000.00 USD | 0.00 USD | 14,260.00 USD | `-50.13%` | `291.88` |
| `Live` | `Long` | `48.95` | 101,330,000.00 USD | 0.00 USD | 1,490.00 USD | `-50.03%` | `30.41` |
| `Live` | `Long` | `49.05` | 101,330,000.00 USD | 0.00 USD | 1,190,000.00 USD | `-49.93%` | `24,247.71` |
| `Live` | `Long` | `49.15` | 100,140,000.00 USD | 0.00 USD | 5,610.00 USD | `-49.83%` | `114.10` |
| `Live` | `Long` | `49.25` | 100,140,000.00 USD | 0.00 USD | 21,190.00 USD | `-49.72%` | `430.30` |
| `Live` | `Long` | `49.35` | 100,110,000.00 USD | 0.00 USD | 7,790.00 USD | `-49.62%` | `157.93` |
| `Live` | `Long` | `49.45` | 100,110,000.00 USD | 0.00 USD | 16,830.00 USD | `-49.52%` | `340.38` |
| `Live` | `Long` | `49.55` | 100,090,000.00 USD | 0.00 USD | 889.42 USD | `-49.42%` | `17.95` |
| `Live` | `Long` | `49.65` | 100,090,000.00 USD | 0.00 USD | 9,200.00 USD | `-49.32%` | `185.21` |
| `Live` | `Long` | `49.75` | 100,080,000.00 USD | 0.00 USD | 1,700.00 USD | `-49.21%` | `34.13` |
| `Live` | `Long` | `49.85` | 100,080,000.00 USD | 0.00 USD | 41,540.00 USD | `-49.11%` | `833.28` |
| `Live` | `Long` | `49.95` | 100,040,000.00 USD | 0.00 USD | 20,850.00 USD | `-49.01%` | `417.37` |
| `Live` | `Long` | `50.05` | 100,020,000.00 USD | 0.00 USD | 12,350.00 USD | `-48.91%` | `246.80` |
| `Live` | `Long` | `50.15` | 100,000,000.00 USD | 0.00 USD | 1,500.00 USD | `-48.81%` | `29.82` |
| `Live` | `Long` | `50.25` | 100,000,000.00 USD | 0.00 USD | 7,860.00 USD | `-48.70%` | `156.35` |
| `Live` | `Long` | `50.35` | 99,990,000.00 USD | 0.00 USD | 2,410.00 USD | `-48.60%` | `47.91` |
| `Live` | `Long` | `50.45` | 99,990,000.00 USD | 0.00 USD | 4,110.00 USD | `-48.50%` | `81.52` |
| `Live` | `Long` | `50.55` | 99,990,000.00 USD | 0.00 USD | 2,710.00 USD | `-48.40%` | `53.61` |
| `Live` | `Long` | `50.65` | 99,980,000.00 USD | 0.00 USD | 843.83 USD | `-48.30%` | `16.66` |
| `Live` | `Long` | `50.75` | 99,980,000.00 USD | 0.00 USD | 12,040.00 USD | `-48.19%` | `237.21` |
| `Live` | `Long` | `50.85` | 99,970,000.00 USD | 0.00 USD | 19,710.00 USD | `-48.09%` | `387.64` |
| `Live` | `Long` | `50.95` | 99,950,000.00 USD | 0.00 USD | 5,530.00 USD | `-47.99%` | `108.48` |
| `Live` | `Long` | `51.05` | 99,950,000.00 USD | 0.00 USD | 2,840.00 USD | `-47.89%` | `55.65` |
| `Live` | `Long` | `51.15` | 99,940,000.00 USD | 0.00 USD | 2,620.00 USD | `-47.78%` | `51.22` |
| `Live` | `Long` | `51.25` | 99,940,000.00 USD | 0.00 USD | 1,440.00 USD | `-47.68%` | `28.11` |
| `Live` | `Long` | `51.35` | 99,940,000.00 USD | 0.00 USD | 10,640.00 USD | `-47.58%` | `207.26` |
| `Live` | `Long` | `51.45` | 99,930,000.00 USD | 0.00 USD | 3,920.00 USD | `-47.48%` | `76.22` |
| `Live` | `Long` | `51.55` | 99,920,000.00 USD | 0.00 USD | 137,330.00 USD | `-47.38%` | `2,663.99` |
| `Live` | `Long` | `51.65` | 99,790,000.00 USD | 0.00 USD | 7,840.00 USD | `-47.27%` | `151.77` |
| `Live` | `Long` | `51.75` | 99,780,000.00 USD | 0.00 USD | 24,770.00 USD | `-47.17%` | `478.71` |
| `Live` | `Long` | `51.85` | 99,750,000.00 USD | 0.00 USD | 42,450.00 USD | `-47.07%` | `818.66` |
| `Live` | `Long` | `51.95` | 99,710,000.00 USD | 0.00 USD | 503,350.00 USD | `-46.97%` | `9,689.22` |
| `Live` | `Long` | `52.05` | 99,210,000.00 USD | 0.00 USD | 58,250.00 USD | `-46.87%` | `1,119.13` |
| `Live` | `Long` | `52.15` | 99,150,000.00 USD | 0.00 USD | 99,630.00 USD | `-46.76%` | `1,910.43` |
| `Live` | `Long` | `52.25` | 99,050,000.00 USD | 0.00 USD | 1,760.00 USD | `-46.66%` | `33.59` |
| `Live` | `Long` | `52.35` | 99,050,000.00 USD | 0.00 USD | 5,700.00 USD | `-46.56%` | `108.90` |
| `Live` | `Long` | `52.45` | 99,040,000.00 USD | 0.00 USD | 879.59 USD | `-46.46%` | `16.77` |
| `Live` | `Long` | `52.55` | 99,040,000.00 USD | 0.00 USD | 11,110.00 USD | `-46.36%` | `211.45` |
| `Live` | `Long` | `52.65` | 99,030,000.00 USD | 0.00 USD | 3,370.00 USD | `-46.25%` | `64.08` |
| `Live` | `Long` | `52.75` | 99,030,000.00 USD | 0.00 USD | 3,180.00 USD | `-46.15%` | `60.32` |
| `Live` | `Long` | `52.85` | 99,030,000.00 USD | 0.00 USD | 9,370.00 USD | `-46.05%` | `177.38` |
| `Live` | `Long` | `52.95` | 99,020,000.00 USD | 0.00 USD | 3,240.00 USD | `-45.95%` | `61.25` |
| `Live` | `Long` | `53.05` | 99,010,000.00 USD | 0.00 USD | 38,480.00 USD | `-45.85%` | `725.33` |
| `Live` | `Long` | `53.15` | 98,970,000.00 USD | 0.00 USD | 2,670.00 USD | `-45.74%` | `50.29` |
| `Live` | `Long` | `53.25` | 98,970,000.00 USD | 0.00 USD | 24,560.00 USD | `-45.64%` | `461.23` |
| `Live` | `Long` | `53.35` | 98,950,000.00 USD | 0.00 USD | 15,690.00 USD | `-45.54%` | `294.13` |
| `Live` | `Long` | `53.45` | 98,930,000.00 USD | 0.00 USD | 38,780.00 USD | `-45.44%` | `725.62` |
| `Live` | `Long` | `53.55` | 98,890,000.00 USD | 0.00 USD | 43,790.00 USD | `-45.33%` | `817.76` |
| `Live` | `Long` | `53.65` | 98,850,000.00 USD | 0.00 USD | 230.70 USD | `-45.23%` | `4.30` |
| `Live` | `Long` | `53.75` | 98,850,000.00 USD | 0.00 USD | 3,870.00 USD | `-45.13%` | `71.92` |
| `Live` | `Long` | `53.85` | 98,840,000.00 USD | 0.00 USD | 18,220.00 USD | `-45.03%` | `338.41` |
| `Live` | `Long` | `53.95` | 98,830,000.00 USD | 0.00 USD | 62,860.00 USD | `-44.93%` | `1,165.20` |
| `Live` | `Long` | `54.05` | 98,760,000.00 USD | 0.00 USD | 350.78 USD | `-44.82%` | `6.49` |
| `Live` | `Long` | `54.15` | 98,760,000.00 USD | 0.00 USD | 14,640.00 USD | `-44.72%` | `270.39` |
| `Live` | `Long` | `54.25` | 98,750,000.00 USD | 0.00 USD | 6,450.00 USD | `-44.62%` | `118.83` |
| `Live` | `Long` | `54.35` | 98,740,000.00 USD | 0.00 USD | 11,720.00 USD | `-44.52%` | `215.69` |
| `Live` | `Long` | `54.45` | 98,730,000.00 USD | 0.00 USD | 2,230.00 USD | `-44.42%` | `40.87` |
| `Live` | `Long` | `54.55` | 98,730,000.00 USD | 0.00 USD | 70,060.00 USD | `-44.31%` | `1,284.36` |
| `Live` | `Long` | `54.65` | 98,660,000.00 USD | 0.00 USD | 2,070.00 USD | `-44.21%` | `37.91` |
| `Live` | `Long` | `54.75` | 98,660,000.00 USD | 0.00 USD | 15,300.00 USD | `-44.11%` | `279.38` |
| `Live` | `Long` | `54.85` | 98,640,000.00 USD | 0.00 USD | 860,090.00 USD | `-44.01%` | `15,680.83` |
| `Live` | `Long` | `54.95` | 97,780,000.00 USD | 0.00 USD | 142,480.00 USD | `-43.91%` | `2,592.93` |
| `Live` | `Long` | `55.05` | 97,640,000.00 USD | 0.00 USD | 30,740.00 USD | `-43.80%` | `558.43` |
| `Live` | `Long` | `55.25` | 97,610,000.00 USD | 0.00 USD | 2,010.00 USD | `-43.60%` | `36.31` |
| `Live` | `Long` | `55.35` | 97,610,000.00 USD | 0.00 USD | 9,920.00 USD | `-43.50%` | `179.16` |
| `Live` | `Long` | `55.45` | 97,600,000.00 USD | 0.00 USD | 146,360.00 USD | `-43.40%` | `2,639.58` |
| `Live` | `Long` | `55.55` | 97,450,000.00 USD | 0.00 USD | 5,090.00 USD | `-43.29%` | `91.69` |
| `Live` | `Long` | `55.65` | 97,440,000.00 USD | 0.00 USD | 11,490.00 USD | `-43.19%` | `206.41` |
| `Live` | `Long` | `55.75` | 97,430,000.00 USD | 0.00 USD | 92,210.00 USD | `-43.09%` | `1,653.91` |
| `Live` | `Long` | `55.85` | 97,340,000.00 USD | 0.00 USD | 26,070.00 USD | `-42.99%` | `466.70` |
| `Live` | `Long` | `55.95` | 97,310,000.00 USD | 0.00 USD | 7,050.00 USD | `-42.88%` | `125.95` |
| `Live` | `Long` | `56.05` | 97,310,000.00 USD | 0.00 USD | 5,640.00 USD | `-42.78%` | `100.70` |
| `Live` | `Long` | `56.15` | 97,300,000.00 USD | 0.00 USD | 38,120.00 USD | `-42.68%` | `678.89` |
| `Live` | `Long` | `56.25` | 97,260,000.00 USD | 0.00 USD | 13,420.00 USD | `-42.58%` | `238.59` |
| `Live` | `Long` | `56.35` | 97,250,000.00 USD | 0.00 USD | 14,180.00 USD | `-42.48%` | `251.72` |
| `Live` | `Long` | `56.45` | 97,240,000.00 USD | 0.00 USD | 12,980.00 USD | `-42.37%` | `229.97` |
| `Live` | `Long` | `56.55` | 97,220,000.00 USD | 0.00 USD | 11,520.00 USD | `-42.27%` | `203.63` |
| `Live` | `Long` | `56.65` | 97,210,000.00 USD | 0.00 USD | 3,190.00 USD | `-42.17%` | `56.32` |
| `Live` | `Long` | `56.75` | 97,210,000.00 USD | 0.00 USD | 10,100.00 USD | `-42.07%` | `177.94` |
| `Live` | `Long` | `56.85` | 97,200,000.00 USD | 0.00 USD | 1,260.00 USD | `-41.97%` | `22.16` |
| `Live` | `Long` | `56.95` | 97,200,000.00 USD | 0.00 USD | 74,000.00 USD | `-41.86%` | `1,299.41` |
| `Live` | `Long` | `57.05` | 97,120,000.00 USD | 0.00 USD | 2,770,000.00 USD | `-41.76%` | `48,627.98` |
| `Live` | `Long` | `57.15` | 94,350,000.00 USD | 0.00 USD | 5,570.00 USD | `-41.66%` | `97.44` |
| `Live` | `Long` | `57.25` | 94,340,000.00 USD | 0.00 USD | 6,500.00 USD | `-41.56%` | `113.52` |
| `Live` | `Long` | `57.35` | 94,340,000.00 USD | 0.00 USD | 7,120.00 USD | `-41.46%` | `124.09` |
| `Live` | `Long` | `57.45` | 94,330,000.00 USD | 0.00 USD | 29,660.00 USD | `-41.35%` | `516.19` |
| `Live` | `Long` | `57.55` | 94,300,000.00 USD | 0.00 USD | 1,390.00 USD | `-41.25%` | `24.22` |
| `Live` | `Long` | `57.65` | 94,300,000.00 USD | 0.00 USD | 14,530.00 USD | `-41.15%` | `252.08` |
| `Live` | `Long` | `57.75` | 94,280,000.00 USD | 0.00 USD | 52,640.00 USD | `-41.05%` | `911.47` |
| `Live` | `Long` | `57.85` | 94,230,000.00 USD | 0.00 USD | 26,170.00 USD | `-40.95%` | `452.30` |
| `Live` | `Long` | `57.95` | 94,200,000.00 USD | 0.00 USD | 2,320,000.00 USD | `-40.84%` | `40,009.05` |
| `Live` | `Long` | `58.05` | 91,890,000.00 USD | 0.00 USD | 11,230.00 USD | `-40.74%` | `193.53` |
| `Live` | `Long` | `58.15` | 91,880,000.00 USD | 0.00 USD | 138,750.00 USD | `-40.64%` | `2,386.05` |
| `Live` | `Long` | `58.25` | 91,740,000.00 USD | 0.00 USD | 9,870.00 USD | `-40.54%` | `169.44` |
| `Live` | `Long` | `58.35` | 91,730,000.00 USD | 0.00 USD | 4,670.00 USD | `-40.43%` | `80.09` |
| `Live` | `Long` | `58.45` | 91,720,000.00 USD | 0.00 USD | 463.51 USD | `-40.33%` | `7.93` |
| `Live` | `Long` | `58.55` | 91,720,000.00 USD | 0.00 USD | 2,970.00 USD | `-40.23%` | `50.81` |
| `Live` | `Long` | `58.65` | 91,720,000.00 USD | 0.00 USD | 418.17 USD | `-40.13%` | `7.13` |
| `Live` | `Long` | `58.75` | 91,720,000.00 USD | 0.00 USD | 195.64 USD | `-40.03%` | `3.33` |
| `Live` | `Long` | `58.85` | 91,720,000.00 USD | 0.00 USD | 6,130.00 USD | `-39.92%` | `104.08` |
| `Live` | `Long` | `58.95` | 91,710,000.00 USD | 0.00 USD | 488.70 USD | `-39.82%` | `8.29` |
| `Live` | `Long` | `59.05` | 91,710,000.00 USD | 0.00 USD | 3,780.00 USD | `-39.72%` | `63.97` |
| `Live` | `Long` | `59.15` | 91,710,000.00 USD | 0.00 USD | 34,330.00 USD | `-39.62%` | `580.44` |
| `Live` | `Long` | `59.25` | 91,670,000.00 USD | 0.00 USD | 613.24 USD | `-39.52%` | `10.35` |
| `Live` | `Long` | `59.35` | 91,670,000.00 USD | 0.00 USD | 29,010.00 USD | `-39.41%` | `488.78` |
| `Live` | `Long` | `59.45` | 91,640,000.00 USD | 0.00 USD | 94,150.00 USD | `-39.31%` | `1,583.76` |
| `Live` | `Long` | `59.55` | 91,550,000.00 USD | 0.00 USD | 16,050.00 USD | `-39.21%` | `269.55` |
| `Live` | `Long` | `59.65` | 91,530,000.00 USD | 0.00 USD | 3,640.00 USD | `-39.11%` | `61.07` |
| `Live` | `Long` | `59.75` | 91,530,000.00 USD | 0.00 USD | 29,930.00 USD | `-39.01%` | `500.84` |
| `Live` | `Long` | `59.85` | 91,500,000.00 USD | 0.00 USD | 32,070.00 USD | `-38.90%` | `535.85` |
| `Live` | `Long` | `59.95` | 91,470,000.00 USD | 0.00 USD | 37,240.00 USD | `-38.80%` | `621.17` |
| `Live` | `Long` | `60.05` | 91,430,000.00 USD | 0.00 USD | 19,630.00 USD | `-38.70%` | `326.86` |
| `Live` | `Long` | `60.15` | 91,410,000.00 USD | 0.00 USD | 64,730.00 USD | `-38.60%` | `1,076.14` |
| `Live` | `Long` | `60.25` | 91,350,000.00 USD | 0.00 USD | 30,620.00 USD | `-38.50%` | `508.29` |
| `Live` | `Long` | `60.35` | 91,320,000.00 USD | 0.00 USD | 3,930.00 USD | `-38.39%` | `65.10` |
| `Live` | `Long` | `60.55` | 91,310,000.00 USD | 0.00 USD | 4,750.00 USD | `-38.19%` | `78.51` |
| `Live` | `Long` | `60.65` | 91,310,000.00 USD | 0.00 USD | 711.42 USD | `-38.09%` | `11.73` |
| `Live` | `Long` | `60.75` | 91,310,000.00 USD | 0.00 USD | 5,300.00 USD | `-37.98%` | `87.26` |
| `Live` | `Long` | `60.85` | 91,300,000.00 USD | 0.00 USD | 28,860.00 USD | `-37.88%` | `474.33` |
| `Live` | `Long` | `60.95` | 91,270,000.00 USD | 0.00 USD | 55,060.00 USD | `-37.78%` | `903.35` |
| `Live` | `Long` | `61.05` | 91,220,000.00 USD | 0.00 USD | 4,230.00 USD | `-37.68%` | `69.34` |
| `Live` | `Long` | `61.15` | 91,210,000.00 USD | 0.00 USD | 5,900.00 USD | `-37.58%` | `96.47` |
| `Live` | `Long` | `61.25` | 91,210,000.00 USD | 0.00 USD | 35,260.00 USD | `-37.47%` | `575.67` |
| `Live` | `Long` | `61.35` | 91,170,000.00 USD | 0.00 USD | 10,280.00 USD | `-37.37%` | `167.54` |
| `Live` | `Long` | `61.45` | 91,160,000.00 USD | 0.00 USD | 20,920.00 USD | `-37.27%` | `340.48` |
| `Live` | `Long` | `61.55` | 91,140,000.00 USD | 0.00 USD | 33,930.00 USD | `-37.17%` | `551.24` |
| `Live` | `Long` | `61.65` | 91,110,000.00 USD | 0.00 USD | 32,140.00 USD | `-37.07%` | `521.34` |
| `Live` | `Long` | `61.75` | 91,070,000.00 USD | 0.00 USD | 16,580.00 USD | `-36.96%` | `268.54` |
| `Live` | `Long` | `61.85` | 91,060,000.00 USD | 0.00 USD | 6,380.00 USD | `-36.86%` | `103.10` |
| `Live` | `Long` | `61.95` | 91,050,000.00 USD | 0.00 USD | 13,170.00 USD | `-36.76%` | `212.57` |
| `Live` | `Long` | `62.05` | 91,040,000.00 USD | 0.00 USD | 9,000.00 USD | `-36.66%` | `145.05` |
| `Live` | `Long` | `62.15` | 91,030,000.00 USD | 0.00 USD | 44,140.00 USD | `-36.56%` | `710.25` |
| `Live` | `Long` | `62.25` | 90,980,000.00 USD | 0.00 USD | 1,800.00 USD | `-36.45%` | `28.90` |
| `Live` | `Long` | `62.35` | 90,980,000.00 USD | 0.00 USD | 16,180.00 USD | `-36.35%` | `259.49` |
| `Live` | `Long` | `62.45` | 90,970,000.00 USD | 0.00 USD | 21,530.00 USD | `-36.25%` | `344.79` |
| `Live` | `Long` | `62.55` | 90,950,000.00 USD | 0.00 USD | 133,130.00 USD | `-36.15%` | `2,128.40` |
| `Live` | `Long` | `62.65` | 90,810,000.00 USD | 0.00 USD | 2,480.00 USD | `-36.05%` | `39.62` |
| `Live` | `Long` | `62.75` | 90,810,000.00 USD | 0.00 USD | 20,960.00 USD | `-35.94%` | `334.00` |
| `Live` | `Long` | `62.85` | 90,790,000.00 USD | 0.00 USD | 31,310.00 USD | `-35.84%` | `498.17` |
| `Live` | `Long` | `62.95` | 90,760,000.00 USD | 0.00 USD | 6,250.00 USD | `-35.74%` | `99.35` |
| `Live` | `Long` | `63.05` | 90,750,000.00 USD | 0.00 USD | 21,650.00 USD | `-35.64%` | `343.33` |
| `Live` | `Long` | `63.15` | 90,730,000.00 USD | 0.00 USD | 104,280.00 USD | `-35.53%` | `1,651.25` |
| `Live` | `Long` | `63.25` | 90,630,000.00 USD | 0.00 USD | 31,580.00 USD | `-35.43%` | `499.21` |
| `Live` | `Long` | `63.45` | 90,590,000.00 USD | 0.00 USD | 11,700.00 USD | `-35.23%` | `184.38` |
| `Live` | `Long` | `63.55` | 90,580,000.00 USD | 0.00 USD | 49,290.00 USD | `-35.13%` | `775.56` |
| `Live` | `Long` | `63.65` | 90,530,000.00 USD | 0.00 USD | 416.27 USD | `-35.02%` | `6.54` |
| `Live` | `Long` | `63.75` | 90,530,000.00 USD | 0.00 USD | 32,540.00 USD | `-34.92%` | `510.36` |
| `Live` | `Long` | `63.85` | 90,500,000.00 USD | 0.00 USD | 36,960.00 USD | `-34.82%` | `578.89` |
| `Live` | `Long` | `63.95` | 90,460,000.00 USD | 0.00 USD | 3,910.00 USD | `-34.72%` | `61.07` |
| `Live` | `Long` | `64.05` | 90,460,000.00 USD | 0.00 USD | 96,080.00 USD | `-34.62%` | `1,500.00` |
| `Live` | `Long` | `64.25` | 90,360,000.00 USD | 0.00 USD | 4,450.00 USD | `-34.41%` | `69.19` |
| `Live` | `Long` | `64.35` | 90,360,000.00 USD | 0.00 USD | 47,540.00 USD | `-34.31%` | `738.71` |
| `Live` | `Long` | `64.45` | 90,310,000.00 USD | 0.00 USD | 4,310.00 USD | `-34.21%` | `66.88` |
| `Live` | `Long` | `64.55` | 90,310,000.00 USD | 0.00 USD | 579.66 USD | `-34.11%` | `8.98` |
| `Live` | `Long` | `64.65` | 90,310,000.00 USD | 0.00 USD | 2,570.00 USD | `-34.00%` | `39.78` |
| `Live` | `Long` | `64.85` | 90,300,000.00 USD | 0.00 USD | 396.23 USD | `-33.80%` | `6.11` |
| `Live` | `Long` | `64.95` | 90,300,000.00 USD | 0.00 USD | 209.79 USD | `-33.70%` | `3.23` |
| `Live` | `Long` | `65.05` | 90,300,000.00 USD | 0.00 USD | 1,560,000.00 USD | `-33.60%` | `23,995.03` |
| `Live` | `Long` | `65.15` | 88,740,000.00 USD | 0.00 USD | 20,970.00 USD | `-33.49%` | `321.86` |
| `Live` | `Long` | `65.25` | 88,720,000.00 USD | 0.00 USD | 42,080.00 USD | `-33.39%` | `644.91` |
| `Live` | `Long` | `65.35` | 88,680,000.00 USD | 0.00 USD | 38,010.00 USD | `-33.29%` | `581.67` |
| `Live` | `Long` | `65.45` | 88,640,000.00 USD | 0.00 USD | 3,130.00 USD | `-33.19%` | `47.89` |
| `Live` | `Long` | `65.55` | 88,640,000.00 USD | 0.00 USD | 10,640.00 USD | `-33.08%` | `162.26` |
| `Live` | `Long` | `65.65` | 88,630,000.00 USD | 0.00 USD | 65,990.00 USD | `-32.98%` | `1,005.20` |
| `Live` | `Long` | `65.75` | 88,560,000.00 USD | 0.00 USD | 11,630.00 USD | `-32.88%` | `176.84` |
| `Live` | `Long` | `65.85` | 88,550,000.00 USD | 0.00 USD | 11,050.00 USD | `-32.78%` | `167.82` |
| `Live` | `Long` | `65.95` | 88,540,000.00 USD | 0.00 USD | 60,910.00 USD | `-32.68%` | `923.59` |
| `Live` | `Long` | `66.05` | 88,480,000.00 USD | 0.00 USD | 4,840.00 USD | `-32.57%` | `73.25` |
| `Live` | `Long` | `66.25` | 88,470,000.00 USD | 0.00 USD | 14,930.00 USD | `-32.37%` | `225.38` |
| `Live` | `Long` | `66.35` | 88,460,000.00 USD | 0.00 USD | 1,600.00 USD | `-32.27%` | `24.08` |
| `Live` | `Long` | `66.45` | 88,460,000.00 USD | 0.00 USD | 10,990.00 USD | `-32.17%` | `165.37` |
| `Live` | `Long` | `66.55` | 88,450,000.00 USD | 0.00 USD | 64,260.00 USD | `-32.06%` | `965.60` |
| `Live` | `Long` | `66.65` | 88,380,000.00 USD | 0.00 USD | 19,140.00 USD | `-31.96%` | `287.22` |
| `Live` | `Long` | `66.75` | 88,360,000.00 USD | 0.00 USD | 47,940.00 USD | `-31.86%` | `718.22` |
| `Live` | `Long` | `66.85` | 88,310,000.00 USD | 0.00 USD | 1,910.00 USD | `-31.76%` | `28.53` |
| `Live` | `Long` | `66.95` | 88,310,000.00 USD | 0.00 USD | 937.30 USD | `-31.66%` | `14.00` |
| `Live` | `Long` | `67.05` | 88,310,000.00 USD | 0.00 USD | 37,700.00 USD | `-31.55%` | `562.33` |
| `Live` | `Long` | `67.15` | 88,270,000.00 USD | 0.00 USD | 3,370.00 USD | `-31.45%` | `50.24` |
| `Live` | `Long` | `67.25` | 88,270,000.00 USD | 0.00 USD | 1,930.00 USD | `-31.35%` | `28.70` |
| `Live` | `Long` | `67.35` | 88,270,000.00 USD | 0.00 USD | 2,640.00 USD | `-31.25%` | `39.19` |
| `Live` | `Long` | `67.45` | 88,270,000.00 USD | 0.00 USD | 21,630.00 USD | `-31.15%` | `320.66` |
| `Live` | `Long` | `67.55` | 88,240,000.00 USD | 0.00 USD | 53,160.00 USD | `-31.04%` | `786.93` |
| `Live` | `Long` | `67.65` | 88,190,000.00 USD | 0.00 USD | 537,120.00 USD | `-30.94%` | `7,939.71` |
| `Live` | `Long` | `67.75` | 87,650,000.00 USD | 0.00 USD | 34,900.00 USD | `-30.84%` | `515.15` |
| `Live` | `Long` | `67.85` | 87,620,000.00 USD | 0.00 USD | 15,250.00 USD | `-30.74%` | `224.79` |
| `Live` | `Long` | `68.05` | 87,600,000.00 USD | 0.00 USD | 11,080.00 USD | `-30.53%` | `162.87` |
| `Live` | `Long` | `68.15` | 87,590,000.00 USD | 0.00 USD | 37,510,000.00 USD | `-30.43%` | `550,364.00` |
| `Live` | `Long` | `68.25` | 50,080,000.00 USD | 0.00 USD | 13,650.00 USD | `-30.33%` | `199.93` |
| `Live` | `Long` | `68.35` | 50,070,000.00 USD | 0.00 USD | 5,820.00 USD | `-30.23%` | `85.10` |
| `Live` | `Long` | `68.45` | 50,070,000.00 USD | 0.00 USD | 18,570.00 USD | `-30.12%` | `271.36` |
| `Live` | `Long` | `68.55` | 50,050,000.00 USD | 0.00 USD | 17,710.00 USD | `-30.02%` | `258.31` |
| `Live` | `Long` | `68.65` | 50,030,000.00 USD | 0.00 USD | 6,150.00 USD | `-29.92%` | `89.56` |
| `Live` | `Long` | `68.75` | 50,020,000.00 USD | 0.00 USD | 12,530,000.00 USD | `-29.82%` | `182,195.20` |
| `Live` | `Long` | `68.85` | 37,500,000.00 USD | 0.00 USD | 770,120.00 USD | `-29.72%` | `11,185.54` |
| `Live` | `Long` | `68.95` | 36,730,000.00 USD | 0.00 USD | 46,330.00 USD | `-29.61%` | `671.97` |
| `Live` | `Long` | `69.05` | 36,680,000.00 USD | 0.00 USD | 3,570.00 USD | `-29.51%` | `51.69` |
| `Live` | `Long` | `69.15` | 36,680,000.00 USD | 0.00 USD | 11,510.00 USD | `-29.41%` | `166.47` |
| `Live` | `Long` | `69.25` | 36,670,000.00 USD | 0.00 USD | 3,140.00 USD | `-29.31%` | `45.34` |
| `Live` | `Long` | `69.35` | 36,660,000.00 USD | 0.00 USD | 6,940.00 USD | `-29.21%` | `100.14` |
| `Live` | `Long` | `69.45` | 36,660,000.00 USD | 0.00 USD | 45,050.00 USD | `-29.10%` | `648.63` |
| `Live` | `Long` | `69.55` | 36,610,000.00 USD | 0.00 USD | 9,170.00 USD | `-29.00%` | `131.87` |
| `Live` | `Long` | `69.65` | 36,600,000.00 USD | 0.00 USD | 9,110.00 USD | `-28.90%` | `130.77` |
| `Live` | `Long` | `69.75` | 36,590,000.00 USD | 0.00 USD | 212,620.00 USD | `-28.80%` | `3,048.34` |
| `Live` | `Long` | `69.85` | 36,380,000.00 USD | 0.00 USD | 13,010.00 USD | `-28.70%` | `186.19` |
| `Live` | `Long` | `69.95` | 36,370,000.00 USD | 0.00 USD | 9,190.00 USD | `-28.59%` | `131.44` |
| `Live` | `Long` | `70.05` | 36,360,000.00 USD | 0.00 USD | 2,080.00 USD | `-28.49%` | `29.75` |
| `Live` | `Long` | `70.15` | 36,360,000.00 USD | 0.00 USD | 4,120.00 USD | `-28.39%` | `58.77` |
| `Live` | `Long` | `70.25` | 36,350,000.00 USD | 0.00 USD | 72,890.00 USD | `-28.29%` | `1,037.54` |
| `Live` | `Long` | `70.35` | 36,280,000.00 USD | 0.00 USD | 2,360,000.00 USD | `-28.18%` | `33,572.90` |
| `Live` | `Long` | `70.45` | 33,920,000.00 USD | 0.00 USD | 1,170,000.00 USD | `-28.08%` | `16,614.19` |
| `Live` | `Long` | `70.55` | 32,750,000.00 USD | 0.00 USD | 4,350.00 USD | `-27.98%` | `61.72` |
| `Live` | `Long` | `70.65` | 32,740,000.00 USD | 0.00 USD | 48,410.00 USD | `-27.88%` | `685.22` |
| `Live` | `Long` | `70.75` | 32,690,000.00 USD | 0.00 USD | 10,060.00 USD | `-27.78%` | `142.20` |
| `Live` | `Long` | `70.85` | 32,680,000.00 USD | 0.00 USD | 11,420.00 USD | `-27.67%` | `161.17` |
| `Live` | `Long` | `70.95` | 32,670,000.00 USD | 0.00 USD | 8,410.00 USD | `-27.57%` | `118.55` |
| `Live` | `Long` | `71.05` | 32,660,000.00 USD | 0.00 USD | 37,930.00 USD | `-27.47%` | `533.81` |
| `Live` | `Long` | `71.15` | 32,630,000.00 USD | 0.00 USD | 69,510.00 USD | `-27.37%` | `976.99` |
| `Live` | `Long` | `71.25` | 32,560,000.00 USD | 0.00 USD | 2,040.00 USD | `-27.27%` | `28.61` |
| `Live` | `Long` | `71.35` | 32,550,000.00 USD | 0.00 USD | 47,480.00 USD | `-27.16%` | `665.45` |
| `Live` | `Long` | `71.45` | 32,510,000.00 USD | 0.00 USD | 31,640.00 USD | `-27.06%` | `442.82` |
| `Live` | `Long` | `71.55` | 32,470,000.00 USD | 0.00 USD | 41,780.00 USD | `-26.96%` | `583.97` |
| `Live` | `Long` | `71.65` | 32,430,000.00 USD | 0.00 USD | 1,390.00 USD | `-26.86%` | `19.43` |
| `Live` | `Long` | `71.75` | 32,430,000.00 USD | 0.00 USD | 32,550.00 USD | `-26.76%` | `453.65` |
| `Live` | `Long` | `71.85` | 32,400,000.00 USD | 0.00 USD | 2,130.00 USD | `-26.65%` | `29.71` |
| `Live` | `Long` | `71.95` | 32,400,000.00 USD | 0.00 USD | 20,800.00 USD | `-26.55%` | `289.12` |
| `Live` | `Long` | `72.05` | 32,380,000.00 USD | 0.00 USD | 9,520.00 USD | `-26.45%` | `132.09` |
| `Live` | `Long` | `72.15` | 32,370,000.00 USD | 0.00 USD | 135,330.00 USD | `-26.35%` | `1,875.70` |
| `Live` | `Long` | `72.25` | 32,230,000.00 USD | 0.00 USD | 258,520.00 USD | `-26.25%` | `3,578.20` |
| `Live` | `Long` | `72.35` | 31,970,000.00 USD | 0.00 USD | 28,860.00 USD | `-26.14%` | `398.85` |
| `Live` | `Long` | `72.45` | 31,940,000.00 USD | 0.00 USD | 1,840.00 USD | `-26.04%` | `25.36` |
| `Live` | `Long` | `72.55` | 31,940,000.00 USD | 0.00 USD | 18,490.00 USD | `-25.94%` | `254.79` |
| `Live` | `Long` | `72.65` | 31,920,000.00 USD | 0.00 USD | 33,720.00 USD | `-25.84%` | `464.15` |
| `Live` | `Long` | `72.75` | 31,890,000.00 USD | 0.00 USD | 8,730.00 USD | `-25.73%` | `120.06` |
| `Live` | `Long` | `72.85` | 31,880,000.00 USD | 0.00 USD | 186,830.00 USD | `-25.63%` | `2,564.61` |
| `Live` | `Long` | `72.95` | 31,690,000.00 USD | 0.00 USD | 26,290.00 USD | `-25.53%` | `360.43` |
| `Live` | `Long` | `73.05` | 31,670,000.00 USD | 0.00 USD | 7,310.00 USD | `-25.43%` | `100.09` |
| `Live` | `Long` | `73.15` | 31,660,000.00 USD | 0.00 USD | 16,780.00 USD | `-25.33%` | `229.39` |
| `Live` | `Long` | `73.25` | 31,640,000.00 USD | 0.00 USD | 27,910.00 USD | `-25.22%` | `380.97` |
| `Live` | `Long` | `73.35` | 31,620,000.00 USD | 0.00 USD | 16,990.00 USD | `-25.12%` | `231.57` |
| `Live` | `Long` | `73.45` | 31,600,000.00 USD | 0.00 USD | 5,350.00 USD | `-25.02%` | `72.82` |
| `Live` | `Long` | `73.55` | 31,590,000.00 USD | 0.00 USD | 14,850.00 USD | `-24.92%` | `201.89` |
| `Live` | `Long` | `73.65` | 31,580,000.00 USD | 0.00 USD | 37,850.00 USD | `-24.82%` | `513.85` |
| `Live` | `Long` | `73.75` | 31,540,000.00 USD | 0.00 USD | 84,910.00 USD | `-24.71%` | `1,151.37` |
| `Live` | `Long` | `73.85` | 31,460,000.00 USD | 0.00 USD | 1,600,000.00 USD | `-24.61%` | `21,708.63` |
| `Live` | `Long` | `73.95` | 29,850,000.00 USD | 0.00 USD | 42,980.00 USD | `-24.51%` | `581.21` |
| `Live` | `Long` | `74.05` | 29,810,000.00 USD | 0.00 USD | 40,920.00 USD | `-24.41%` | `552.60` |
| `Live` | `Long` | `74.15` | 29,770,000.00 USD | 0.00 USD | 21,710.00 USD | `-24.31%` | `292.76` |
| `Live` | `Long` | `74.25` | 29,750,000.00 USD | 0.00 USD | 50,170.00 USD | `-24.20%` | `675.67` |
| `Live` | `Long` | `74.35` | 29,700,000.00 USD | 0.00 USD | 27,910.00 USD | `-24.10%` | `375.37` |
| `Live` | `Long` | `74.45` | 29,670,000.00 USD | 0.00 USD | 22,440.00 USD | `-24.00%` | `301.36` |
| `Live` | `Long` | `74.55` | 29,650,000.00 USD | 0.00 USD | 6,260.00 USD | `-23.90%` | `84.00` |
| `Live` | `Long` | `74.65` | 29,640,000.00 USD | 0.00 USD | 103,520.00 USD | `-23.80%` | `1,386.71` |
| `Live` | `Long` | `74.75` | 29,540,000.00 USD | 0.00 USD | 48,180.00 USD | `-23.69%` | `644.53` |
| `Live` | `Long` | `74.85` | 29,490,000.00 USD | 0.00 USD | 34,400.00 USD | `-23.59%` | `459.63` |
| `Live` | `Long` | `74.95` | 29,450,000.00 USD | 0.00 USD | 18,080.00 USD | `-23.49%` | `241.26` |
| `Live` | `Long` | `75.05` | 29,440,000.00 USD | 0.00 USD | 40,680.00 USD | `-23.39%` | `542.00` |
| `Live` | `Long` | `75.15` | 29,400,000.00 USD | 0.00 USD | 1,460,000.00 USD | `-23.29%` | `19,434.10` |
| `Live` | `Long` | `75.25` | 27,930,000.00 USD | 0.00 USD | 24,900.00 USD | `-23.18%` | `330.84` |
| `Live` | `Long` | `75.35` | 27,910,000.00 USD | 0.00 USD | 369,030.00 USD | `-23.08%` | `4,897.55` |
| `Live` | `Long` | `75.45` | 27,540,000.00 USD | 0.00 USD | 33,560.00 USD | `-22.98%` | `444.85` |
| `Live` | `Long` | `75.55` | 27,510,000.00 USD | 0.00 USD | 59,620.00 USD | `-22.88%` | `789.20` |
| `Live` | `Long` | `75.65` | 27,450,000.00 USD | 0.00 USD | 130,250.00 USD | `-22.77%` | `1,721.70` |
| `Live` | `Long` | `75.75` | 27,320,000.00 USD | 0.00 USD | 53,250.00 USD | `-22.67%` | `702.97` |
| `Live` | `Long` | `75.85` | 27,260,000.00 USD | 0.00 USD | 2,630.00 USD | `-22.57%` | `34.67` |
| `Live` | `Long` | `75.95` | 27,260,000.00 USD | 0.00 USD | 27,920.00 USD | `-22.47%` | `367.58` |
| `Live` | `Long` | `76.05` | 27,230,000.00 USD | 0.00 USD | 9,680.00 USD | `-22.37%` | `127.31` |
| `Live` | `Long` | `76.15` | 27,220,000.00 USD | 0.00 USD | 4,370.00 USD | `-22.26%` | `57.43` |
| `Live` | `Long` | `76.25` | 27,220,000.00 USD | 0.00 USD | 106,660.00 USD | `-22.16%` | `1,398.86` |
| `Live` | `Long` | `76.35` | 27,110,000.00 USD | 0.00 USD | 205,010.00 USD | `-22.06%` | `2,685.10` |
| `Live` | `Long` | `76.45` | 26,910,000.00 USD | 0.00 USD | 2,180.00 USD | `-21.96%` | `28.58` |
| `Live` | `Long` | `76.55` | 26,910,000.00 USD | 0.00 USD | 38,390.00 USD | `-21.86%` | `501.50` |
| `Live` | `Long` | `76.65` | 26,870,000.00 USD | 0.00 USD | 56,310.00 USD | `-21.75%` | `734.69` |
| `Live` | `Long` | `76.75` | 26,810,000.00 USD | 0.00 USD | 12,180.00 USD | `-21.65%` | `158.68` |
| `Live` | `Long` | `76.85` | 26,800,000.00 USD | 0.00 USD | 134,060.00 USD | `-21.55%` | `1,744.43` |
| `Live` | `Long` | `76.95` | 26,660,000.00 USD | 0.00 USD | 28,980.00 USD | `-21.45%` | `376.65` |
| `Live` | `Long` | `77.05` | 26,640,000.00 USD | 0.00 USD | 83,450.00 USD | `-21.35%` | `1,083.07` |
| `Live` | `Long` | `77.15` | 26,550,000.00 USD | 0.00 USD | 85,390.00 USD | `-21.24%` | `1,106.85` |
| `Live` | `Long` | `77.25` | 26,470,000.00 USD | 0.00 USD | 25,020.00 USD | `-21.14%` | `323.94` |
| `Live` | `Long` | `77.35` | 26,440,000.00 USD | 0.00 USD | 5,340.00 USD | `-21.04%` | `68.99` |
| `Live` | `Long` | `77.45` | 26,440,000.00 USD | 0.00 USD | 48,500.00 USD | `-20.94%` | `626.25` |
| `Live` | `Long` | `77.55` | 26,390,000.00 USD | 0.00 USD | 13,740.00 USD | `-20.84%` | `177.20` |
| `Live` | `Long` | `77.75` | 26,370,000.00 USD | 0.00 USD | 9,870.00 USD | `-20.63%` | `126.99` |
| `Live` | `Long` | `77.85` | 26,360,000.00 USD | 0.00 USD | 68,400.00 USD | `-20.53%` | `878.61` |
| `Live` | `Long` | `77.95` | 26,300,000.00 USD | 0.00 USD | 8,370.00 USD | `-20.43%` | `107.32` |
| `Live` | `Long` | `78.05` | 26,290,000.00 USD | 0.00 USD | 21,520.00 USD | `-20.32%` | `275.71` |
| `Live` | `Long` | `78.15` | 26,270,000.00 USD | 0.00 USD | 63,710.00 USD | `-20.22%` | `815.26` |
| `Live` | `Long` | `78.25` | 26,200,000.00 USD | 0.00 USD | 39,070.00 USD | `-20.12%` | `499.28` |
| `Live` | `Long` | `78.35` | 26,160,000.00 USD | 0.00 USD | 55,590.00 USD | `-20.02%` | `709.49` |
| `Live` | `Long` | `78.45` | 26,110,000.00 USD | 0.00 USD | 34,460.00 USD | `-19.92%` | `439.21` |
| `Live` | `Long` | `78.55` | 26,070,000.00 USD | 0.00 USD | 9,470.00 USD | `-19.81%` | `120.61` |
| `Live` | `Long` | `78.65` | 26,060,000.00 USD | 0.00 USD | 36,820.00 USD | `-19.71%` | `468.09` |
| `Live` | `Long` | `78.75` | 26,030,000.00 USD | 0.00 USD | 60,790.00 USD | `-19.61%` | `771.88` |
| `Live` | `Long` | `78.85` | 25,970,000.00 USD | 0.00 USD | 62,880.00 USD | `-19.51%` | `797.43` |
| `Live` | `Long` | `78.95` | 25,900,000.00 USD | 0.00 USD | 3,950.00 USD | `-19.41%` | `50.07` |
| `Live` | `Long` | `79.05` | 25,900,000.00 USD | 0.00 USD | 54,310.00 USD | `-19.30%` | `687.06` |
| `Live` | `Long` | `79.15` | 25,850,000.00 USD | 0.00 USD | 128,590.00 USD | `-19.20%` | `1,624.63` |
| `Live` | `Long` | `79.25` | 25,720,000.00 USD | 0.00 USD | 41,700.00 USD | `-19.10%` | `526.15` |
| `Live` | `Long` | `79.35` | 25,670,000.00 USD | 0.00 USD | 33,050.00 USD | `-19.00%` | `416.51` |
| `Live` | `Long` | `79.45` | 25,640,000.00 USD | 0.00 USD | 15,960.00 USD | `-18.90%` | `200.90` |
| `Live` | `Long` | `79.55` | 25,630,000.00 USD | 0.00 USD | 2,220.00 USD | `-18.79%` | `27.86` |
| `Live` | `Long` | `79.65` | 25,620,000.00 USD | 0.00 USD | 31,850.00 USD | `-18.69%` | `399.87` |
| `Live` | `Long` | `79.75` | 25,590,000.00 USD | 0.00 USD | 49,110.00 USD | `-18.59%` | `615.82` |
| `Live` | `Long` | `79.85` | 25,540,000.00 USD | 0.00 USD | 14,850.00 USD | `-18.49%` | `185.99` |
| `Live` | `Long` | `79.95` | 25,530,000.00 USD | 0.00 USD | 30,400.00 USD | `-18.39%` | `380.25` |
| `Live` | `Long` | `80.05` | 25,500,000.00 USD | 0.00 USD | 28,670.00 USD | `-18.28%` | `358.13` |
| `Live` | `Long` | `80.15` | 25,470,000.00 USD | 0.00 USD | 31,900.00 USD | `-18.18%` | `398.06` |
| `Live` | `Long` | `80.25` | 25,440,000.00 USD | 0.00 USD | 624,910.00 USD | `-18.08%` | `7,787.04` |
| `Live` | `Long` | `80.35` | 24,810,000.00 USD | 0.00 USD | 104,890.00 USD | `-17.98%` | `1,305.38` |
| `Live` | `Long` | `80.45` | 24,710,000.00 USD | 0.00 USD | 17,250.00 USD | `-17.87%` | `214.40` |
| `Live` | `Long` | `80.55` | 24,690,000.00 USD | 0.00 USD | 10,500.00 USD | `-17.77%` | `130.37` |
| `Live` | `Long` | `80.65` | 24,680,000.00 USD | 0.00 USD | 13,740.00 USD | `-17.67%` | `170.32` |
| `Live` | `Long` | `80.75` | 24,670,000.00 USD | 0.00 USD | 31,310.00 USD | `-17.57%` | `387.77` |
| `Live` | `Long` | `80.85` | 24,630,000.00 USD | 0.00 USD | 440,070.00 USD | `-17.47%` | `5,443.01` |
| `Live` | `Long` | `80.95` | 24,190,000.00 USD | 0.00 USD | 10,620.00 USD | `-17.36%` | `131.18` |
| `Live` | `Long` | `81.05` | 24,180,000.00 USD | 0.00 USD | 2,230,000.00 USD | `-17.26%` | `27,540.80` |
| `Live` | `Long` | `81.15` | 21,950,000.00 USD | 0.00 USD | 128,110.00 USD | `-17.16%` | `1,578.71` |
| `Live` | `Long` | `81.25` | 21,820,000.00 USD | 0.00 USD | 22,790.00 USD | `-17.06%` | `280.49` |
| `Live` | `Long` | `81.35` | 21,800,000.00 USD | 0.00 USD | 418,360.00 USD | `-16.96%` | `5,142.72` |
| `Live` | `Long` | `81.45` | 21,380,000.00 USD | 0.00 USD | 60,710.00 USD | `-16.85%` | `745.33` |
| `Live` | `Long` | `81.55` | 21,320,000.00 USD | 0.00 USD | 102,010.00 USD | `-16.75%` | `1,250.84` |
| `Live` | `Long` | `81.65` | 21,220,000.00 USD | 0.00 USD | 15,400.00 USD | `-16.65%` | `188.66` |
| `Live` | `Long` | `81.75` | 21,200,000.00 USD | 0.00 USD | 18,650.00 USD | `-16.55%` | `228.11` |
| `Live` | `Long` | `81.85` | 21,190,000.00 USD | 0.00 USD | 760,330.00 USD | `-16.45%` | `9,289.37` |
| `Live` | `Long` | `81.95` | 20,430,000.00 USD | 0.00 USD | 31,560.00 USD | `-16.34%` | `385.12` |
| `Live` | `Long` | `82.05` | 20,390,000.00 USD | 0.00 USD | 117,060.00 USD | `-16.24%` | `1,426.69` |
| `Live` | `Long` | `82.15` | 20,280,000.00 USD | 0.00 USD | 807,960.00 USD | `-16.14%` | `9,835.19` |
| `Live` | `Long` | `82.25` | 19,470,000.00 USD | 0.00 USD | 24,480.00 USD | `-16.04%` | `297.62` |
| `Live` | `Long` | `82.35` | 19,440,000.00 USD | 0.00 USD | 159,780.00 USD | `-15.94%` | `1,940.23` |
| `Live` | `Long` | `82.45` | 19,280,000.00 USD | 0.00 USD | 235,090.00 USD | `-15.83%` | `2,851.33` |
| `Live` | `Long` | `82.55` | 19,050,000.00 USD | 0.00 USD | 26,400.00 USD | `-15.73%` | `319.76` |
| `Live` | `Long` | `82.65` | 19,020,000.00 USD | 0.00 USD | 98,590.00 USD | `-15.63%` | `1,192.87` |
| `Live` | `Long` | `82.75` | 18,920,000.00 USD | 0.00 USD | 27,050.00 USD | `-15.53%` | `326.86` |
| `Live` | `Long` | `82.85` | 18,900,000.00 USD | 0.00 USD | 20,580.00 USD | `-15.42%` | `248.36` |
| `Live` | `Long` | `82.95` | 18,880,000.00 USD | 0.00 USD | 16,630.00 USD | `-15.32%` | `200.48` |
| `Live` | `Long` | `83.05` | 18,860,000.00 USD | 0.00 USD | 58,320.00 USD | `-15.22%` | `702.17` |
| `Live` | `Long` | `83.15` | 18,800,000.00 USD | 0.00 USD | 61,560.00 USD | `-15.12%` | `740.37` |
| `Live` | `Long` | `83.25` | 18,740,000.00 USD | 0.00 USD | 197,080.00 USD | `-15.02%` | `2,367.37` |
| `Live` | `Long` | `83.35` | 18,540,000.00 USD | 0.00 USD | 287,230.00 USD | `-14.91%` | `3,446.04` |
| `Live` | `Long` | `83.45` | 18,260,000.00 USD | 0.00 USD | 29,160.00 USD | `-14.81%` | `349.42` |
| `Live` | `Long` | `83.55` | 18,230,000.00 USD | 0.00 USD | 168,680.00 USD | `-14.71%` | `2,018.86` |
| `Live` | `Long` | `83.65` | 18,060,000.00 USD | 0.00 USD | 80,730.00 USD | `-14.61%` | `965.08` |
| `Live` | `Long` | `83.75` | 17,980,000.00 USD | 0.00 USD | 87,590.00 USD | `-14.51%` | `1,045.88` |
| `Live` | `Long` | `83.85` | 17,890,000.00 USD | 0.00 USD | 12,050.00 USD | `-14.40%` | `143.75` |
| `Live` | `Long` | `83.95` | 17,880,000.00 USD | 0.00 USD | 54,780.00 USD | `-14.30%` | `652.51` |
| `Live` | `Long` | `84.05` | 17,820,000.00 USD | 0.00 USD | 133,650.00 USD | `-14.20%` | `1,590.09` |
| `Live` | `Long` | `84.15` | 17,690,000.00 USD | 0.00 USD | 65,310.00 USD | `-14.10%` | `776.06` |
| `Live` | `Long` | `84.25` | 17,620,000.00 USD | 0.00 USD | 47,100.00 USD | `-14.00%` | `559.03` |
| `Live` | `Long` | `84.35` | 17,580,000.00 USD | 0.00 USD | 25,180.00 USD | `-13.89%` | `298.47` |
| `Live` | `Long` | `84.45` | 17,550,000.00 USD | 0.00 USD | 85,770.00 USD | `-13.79%` | `1,015.66` |
| `Live` | `Long` | `84.55` | 17,470,000.00 USD | 0.00 USD | 18,030.00 USD | `-13.69%` | `213.21` |
| `Live` | `Long` | `84.65` | 17,450,000.00 USD | 0.00 USD | 102,150.00 USD | `-13.59%` | `1,206.79` |
| `Live` | `Long` | `84.75` | 17,350,000.00 USD | 0.00 USD | 289,740.00 USD | `-13.49%` | `3,418.76` |
| `Live` | `Long` | `84.85` | 17,060,000.00 USD | 0.00 USD | 95,230.00 USD | `-13.38%` | `1,122.34` |
| `Live` | `Long` | `84.95` | 16,960,000.00 USD | 0.00 USD | 617.59 USD | `-13.28%` | `7.27` |
| `Live` | `Long` | `85.05` | 16,960,000.00 USD | 0.00 USD | 18,750.00 USD | `-13.18%` | `220.51` |
| `Live` | `Long` | `85.15` | 16,940,000.00 USD | 0.00 USD | 5,380.00 USD | `-13.08%` | `63.15` |
| `Live` | `Long` | `85.25` | 16,940,000.00 USD | 0.00 USD | 609,660.00 USD | `-12.97%` | `7,151.48` |
| `Live` | `Long` | `85.35` | 16,330,000.00 USD | 0.00 USD | 22,160.00 USD | `-12.87%` | `259.69` |
| `Live` | `Long` | `85.45` | 16,300,000.00 USD | 0.00 USD | 53,750.00 USD | `-12.77%` | `629.05` |
| `Live` | `Long` | `85.55` | 16,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | `-12.67%` | `14,616.41` |
| `Live` | `Long` | `85.65` | 15,000,000.00 USD | 0.00 USD | 43,310.00 USD | `-12.57%` | `505.67` |
| `Live` | `Long` | `85.75` | 14,960,000.00 USD | 0.00 USD | 9,830.00 USD | `-12.46%` | `114.66` |
| `Live` | `Long` | `85.85` | 14,950,000.00 USD | 0.00 USD | 86,260.00 USD | `-12.36%` | `1,004.79` |
| `Live` | `Long` | `85.95` | 14,860,000.00 USD | 0.00 USD | 363,700.00 USD | `-12.26%` | `4,231.48` |
| `Live` | `Long` | `86.05` | 14,500,000.00 USD | 0.00 USD | 256,680.00 USD | `-12.16%` | `2,982.96` |
| `Live` | `Long` | `86.15` | 14,240,000.00 USD | 0.00 USD | 74,860.00 USD | `-12.06%` | `868.98` |
| `Live` | `Long` | `86.25` | 14,170,000.00 USD | 0.00 USD | 28,470.00 USD | `-11.95%` | `330.09` |
| `Live` | `Long` | `86.35` | 14,140,000.00 USD | 0.00 USD | 3,870.00 USD | `-11.85%` | `44.87` |
| `Live` | `Long` | `86.45` | 14,130,000.00 USD | 0.00 USD | 266,720.00 USD | `-11.75%` | `3,085.21` |
| `Live` | `Long` | `86.55` | 13,870,000.00 USD | 0.00 USD | 44,550.00 USD | `-11.65%` | `514.77` |
| `Live` | `Long` | `86.65` | 13,820,000.00 USD | 0.00 USD | 193,100.00 USD | `-11.55%` | `2,228.45` |
| `Live` | `Long` | `86.75` | 13,630,000.00 USD | 0.00 USD | 46,790.00 USD | `-11.44%` | `539.35` |
| `Live` | `Long` | `86.85` | 13,580,000.00 USD | 0.00 USD | 78,310.00 USD | `-11.34%` | `901.67` |
| `Live` | `Long` | `86.95` | 13,500,000.00 USD | 0.00 USD | 155,770.00 USD | `-11.24%` | `1,791.48` |
| `Live` | `Long` | `87.05` | 13,350,000.00 USD | 0.00 USD | 55,280.00 USD | `-11.14%` | `635.04` |
| `Live` | `Long` | `87.15` | 13,290,000.00 USD | 0.00 USD | 45,190.00 USD | `-11.04%` | `518.50` |
| `Live` | `Long` | `87.25` | 13,250,000.00 USD | 0.00 USD | 76,430.00 USD | `-10.93%` | `876.01` |
| `Live` | `Long` | `87.35` | 13,170,000.00 USD | 0.00 USD | 83,480.00 USD | `-10.83%` | `955.66` |
| `Live` | `Long` | `87.45` | 13,090,000.00 USD | 0.00 USD | 158,820.00 USD | `-10.73%` | `1,816.08` |
| `Live` | `Long` | `87.55` | 12,930,000.00 USD | 0.00 USD | 203,490.00 USD | `-10.63%` | `2,324.25` |
| `Live` | `Long` | `87.65` | 12,720,000.00 USD | 0.00 USD | 113,790.00 USD | `-10.52%` | `1,298.21` |
| `Live` | `Long` | `87.75` | 12,610,000.00 USD | 0.00 USD | 25,930.00 USD | `-10.42%` | `295.46` |
| `Live` | `Long` | `87.85` | 12,590,000.00 USD | 0.00 USD | 67,120.00 USD | `-10.32%` | `764.00` |
| `Live` | `Long` | `87.95` | 12,520,000.00 USD | 0.00 USD | 6,600.00 USD | `-10.22%` | `75.02` |
| `Live` | `Long` | `88.05` | 12,510,000.00 USD | 0.00 USD | 161,010.00 USD | `-10.12%` | `1,828.61` |
| `Live` | `Long` | `88.15` | 12,350,000.00 USD | 0.00 USD | 21,240.00 USD | `-10.01%` | `240.98` |
| `Live` | `Long` | `88.25` | 12,330,000.00 USD | 0.00 USD | 54,000.00 USD | `-9.91%` | `611.94` |
| `Live` | `Long` | `88.35` | 12,280,000.00 USD | 0.00 USD | 101,240.00 USD | `-9.81%` | `1,145.95` |
| `Live` | `Long` | `88.45` | 12,170,000.00 USD | 0.00 USD | 62,140.00 USD | `-9.71%` | `702.51` |
| `Live` | `Long` | `88.55` | 12,110,000.00 USD | 0.00 USD | 242,620.00 USD | `-9.61%` | `2,739.96` |
| `Live` | `Long` | `88.65` | 11,870,000.00 USD | 0.00 USD | 97,760.00 USD | `-9.50%` | `1,102.79` |
| `Live` | `Long` | `88.75` | 11,770,000.00 USD | 0.00 USD | 185,570.00 USD | `-9.40%` | `2,090.98` |
| `Live` | `Long` | `88.85` | 11,590,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-9.30%` | `12,824.96` |
| `Live` | `Long` | `88.95` | 10,450,000.00 USD | 0.00 USD | 32,790.00 USD | `-9.20%` | `368.66` |
| `Live` | `Long` | `89.05` | 10,410,000.00 USD | 0.00 USD | 22,640.00 USD | `-9.10%` | `254.28` |
| `Live` | `Long` | `89.15` | 10,390,000.00 USD | 0.00 USD | 125,700.00 USD | `-8.99%` | `1,409.95` |
| `Live` | `Long` | `89.25` | 10,270,000.00 USD | 0.00 USD | 31,740.00 USD | `-8.89%` | `355.61` |
| `Live` | `Long` | `89.35` | 10,230,000.00 USD | 0.00 USD | 25,620.00 USD | `-8.79%` | `286.79` |
| `Live` | `Long` | `89.45` | 10,210,000.00 USD | 0.00 USD | 447,820.00 USD | `-8.69%` | `5,006.38` |
| `Live` | `Long` | `89.55` | 9,760,000.00 USD | 0.00 USD | 53,100.00 USD | `-8.59%` | `592.94` |
| `Live` | `Long` | `89.65` | 9,710,000.00 USD | 0.00 USD | 28,830.00 USD | `-8.48%` | `321.62` |
| `Live` | `Long` | `89.75` | 9,680,000.00 USD | 0.00 USD | 125,510.00 USD | `-8.38%` | `1,398.43` |
| `Live` | `Long` | `89.85` | 9,550,000.00 USD | 0.00 USD | 64,900.00 USD | `-8.28%` | `722.27` |
| `Live` | `Long` | `89.95` | 9,490,000.00 USD | 0.00 USD | 83,320.00 USD | `-8.18%` | `926.30` |
| `Live` | `Long` | `90.05` | 9,400,000.00 USD | 0.00 USD | 57,350.00 USD | `-8.07%` | `636.87` |
| `Live` | `Long` | `90.15` | 9,350,000.00 USD | 0.00 USD | 56,590.00 USD | `-7.97%` | `627.73` |
| `Live` | `Long` | `90.25` | 9,290,000.00 USD | 0.00 USD | 28,100.00 USD | `-7.87%` | `311.41` |
| `Live` | `Long` | `90.35` | 9,260,000.00 USD | 0.00 USD | 78,770.00 USD | `-7.77%` | `871.85` |
| `Live` | `Long` | `90.45` | 9,180,000.00 USD | 0.00 USD | 28,650.00 USD | `-7.67%` | `316.80` |
| `Live` | `Long` | `90.55` | 9,150,000.00 USD | 0.00 USD | 44,980.00 USD | `-7.56%` | `496.77` |
| `Live` | `Long` | `90.65` | 9,110,000.00 USD | 0.00 USD | 119,860.00 USD | `-7.46%` | `1,322.18` |
| `Live` | `Long` | `90.75` | 8,990,000.00 USD | 0.00 USD | 103,330.00 USD | `-7.36%` | `1,138.66` |
| `Live` | `Long` | `90.85` | 8,890,000.00 USD | 0.00 USD | 951,490.00 USD | `-7.26%` | `10,473.21` |
| `Live` | `Long` | `90.95` | 7,940,000.00 USD | 0.00 USD | 18,840.00 USD | `-7.16%` | `207.20` |
| `Live` | `Long` | `91.05` | 7,920,000.00 USD | 0.00 USD | 435,550.00 USD | `-7.05%` | `4,783.59` |
| `Live` | `Long` | `91.15` | 7,480,000.00 USD | 0.00 USD | 294,770.00 USD | `-6.95%` | `3,233.86` |
| `Live` | `Long` | `91.25` | 7,190,000.00 USD | 0.00 USD | 33,570.00 USD | `-6.85%` | `367.90` |
| `Live` | `Long` | `91.35` | 7,150,000.00 USD | 0.00 USD | 25,530.00 USD | `-6.75%` | `279.44` |
| `Live` | `Long` | `91.45` | 7,130,000.00 USD | 0.00 USD | 322,810.00 USD | `-6.65%` | `3,529.93` |
| `Live` | `Long` | `91.55` | 6,800,000.00 USD | 0.00 USD | 1,230,000.00 USD | `-6.54%` | `13,404.29` |
| `Live` | `Long` | `91.65` | 5,580,000.00 USD | 0.00 USD | 1,440,000.00 USD | `-6.44%` | `15,699.19` |
| `Live` | `Long` | `91.75` | 4,140,000.00 USD | 0.00 USD | 225,950.00 USD | `-6.34%` | `2,462.71` |
| `Live` | `Long` | `91.85` | 3,910,000.00 USD | 0.00 USD | 248,450.00 USD | `-6.24%` | `2,704.96` |
| `Live` | `Long` | `91.95` | 3,660,000.00 USD | 0.00 USD | 181,560.00 USD | `-6.14%` | `1,974.59` |
| `Live` | `Long` | `92.05` | 3,480,000.00 USD | 0.00 USD | 94,570.00 USD | `-6.03%` | `1,027.34` |
| `Live` | `Long` | `92.15` | 3,390,000.00 USD | 0.00 USD | 328,620.00 USD | `-5.93%` | `3,566.11` |
| `Live` | `Long` | `92.25` | 3,060,000.00 USD | 0.00 USD | 227,110.00 USD | `-5.83%` | `2,461.90` |
| `Live` | `Long` | `92.35` | 2,830,000.00 USD | 0.00 USD | 326,740.00 USD | `-5.73%` | `3,538.03` |
| `Live` | `Long` | `92.45` | 2,510,000.00 USD | 0.00 USD | 122,830.00 USD | `-5.62%` | `1,328.59` |
| `Live` | `Long` | `92.55` | 2,380,000.00 USD | 0.00 USD | 315,900.00 USD | `-5.52%` | `3,413.29` |
| `Live` | `Long` | `92.65` | 2,070,000.00 USD | 0.00 USD | 15,290.00 USD | `-5.42%` | `165.04` |
| `Live` | `Long` | `92.75` | 2,050,000.00 USD | 0.00 USD | 62,310.00 USD | `-5.32%` | `671.80` |
| `Live` | `Long` | `92.85` | 1,990,000.00 USD | 0.00 USD | 7,990.00 USD | `-5.22%` | `86.06` |
| `Live` | `Long` | `92.95` | 1,980,000.00 USD | 0.00 USD | 5,720.00 USD | `-5.11%` | `61.49` |
| `Live` | `Long` | `93.05` | 1,980,000.00 USD | 0.00 USD | 67,670.00 USD | `-5.01%` | `727.19` |
| `Live` | `Long` | `93.15` | 1,910,000.00 USD | 0.00 USD | 2,810.00 USD | `-4.91%` | `30.17` |
| `Live` | `Long` | `93.25` | 1,900,000.00 USD | 0.00 USD | 38,840.00 USD | `-4.81%` | `416.49` |
| `Live` | `Long` | `93.35` | 1,870,000.00 USD | 0.00 USD | 12,570.00 USD | `-4.71%` | `134.70` |
| `Live` | `Long` | `93.45` | 1,850,000.00 USD | 0.00 USD | 7,320.00 USD | `-4.60%` | `78.38` |
| `Live` | `Long` | `93.55` | 1,850,000.00 USD | 0.00 USD | 29,010.00 USD | `-4.50%` | `310.09` |
| `Live` | `Long` | `93.65` | 1,820,000.00 USD | 0.00 USD | 9,580.00 USD | `-4.40%` | `102.34` |
| `Live` | `Long` | `93.75` | 1,810,000.00 USD | 0.00 USD | 9,230.00 USD | `-4.30%` | `98.48` |
| `Live` | `Long` | `93.95` | 1,800,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-4.09%` | `12,071.12` |
| `Live` | `Long` | `94.15` | 664,060.00 USD | 0.00 USD | 20,790.00 USD | `-3.89%` | `220.82` |
| `Live` | `Long` | `94.25` | 643,270.00 USD | 0.00 USD | 15,100.00 USD | `-3.79%` | `160.23` |
| `Live` | `Long` | `94.35` | 628,170.00 USD | 0.00 USD | 2,100.00 USD | `-3.69%` | `22.27` |
| `Live` | `Long` | `94.45` | 626,060.00 USD | 0.00 USD | 152,100.00 USD | `-3.58%` | `1,610.37` |
| `Live` | `Long` | `94.55` | 473,970.00 USD | 0.00 USD | 584.32 USD | `-3.48%` | `6.18` |
| `Live` | `Long` | `94.65` | 473,380.00 USD | 0.00 USD | 18,060.00 USD | `-3.38%` | `190.78` |
| `Live` | `Long` | `94.75` | 455,320.00 USD | 0.00 USD | 32,450.00 USD | `-3.28%` | `342.53` |
| `Live` | `Long` | `94.85` | 422,870.00 USD | 0.00 USD | 56,320.00 USD | `-3.17%` | `593.75` |
| `Live` | `Long` | `94.95` | 366,550.00 USD | 0.00 USD | 22,400.00 USD | `-3.07%` | `235.87` |
| `Live` | `Long` | `95.05` | 344,160.00 USD | 0.00 USD | 84,340.00 USD | `-2.97%` | `887.35` |
| `Live` | `Long` | `95.15` | 259,810.00 USD | 0.00 USD | 25,040.00 USD | `-2.87%` | `263.12` |
| `Live` | `Long` | `95.25` | 234,780.00 USD | 0.00 USD | 66,250.00 USD | `-2.77%` | `695.51` |
| `Live` | `Long` | `95.35` | 168,530.00 USD | 0.00 USD | 22,080.00 USD | `-2.66%` | `231.55` |
| `Live` | `Long` | `95.45` | 146,450.00 USD | 0.00 USD | 14,420.00 USD | `-2.56%` | `151.05` |
| `Live` | `Long` | `95.55` | 132,030.00 USD | 0.00 USD | 23,690.00 USD | `-2.46%` | `247.92` |
| `Live` | `Long` | `95.65` | 108,350.00 USD | 0.00 USD | 57,300.00 USD | `-2.36%` | `599.06` |
| `Live` | `Long` | `95.75` | 51,050.00 USD | 0.00 USD | 34,210.00 USD | `-2.26%` | `357.31` |
| `Live` | `Long` | `95.85` | 16,830.00 USD | 0.00 USD | 13,180.00 USD | `-2.15%` | `137.53` |
| `Live` | `Short` | `95.95` | 1,900.00 USD | 1,900.00 USD | 0.00 USD | `-2.05%` | `19.79` |
| `Live` | `Long` | `96.55` | 3,650.00 USD | 0.00 USD | 3,650.00 USD | `-1.44%` | `37.81` |
| `Live` | `Short` | `98.55` | 7,830.00 USD | 5,930.00 USD | 0.00 USD | `+0.60%` | `60.17` |
| `Live` | `Short` | `98.65` | 17,570.00 USD | 9,740.00 USD | 0.00 USD | `+0.70%` | `98.70` |
| `Live` | `Short` | `98.85` | 17,840.00 USD | 269.86 USD | 0.00 USD | `+0.91%` | `2.73` |
| `Live` | `Short` | `98.95` | 18,850.00 USD | 1,020.00 USD | 0.00 USD | `+1.01%` | `10.28` |
| `Live` | `Short` | `99.05` | 22,460.00 USD | 3,610.00 USD | 0.00 USD | `+1.11%` | `36.45` |
| `Live` | `Short` | `99.15` | 1,140,000.00 USD | 1,110,000.00 USD | 0.00 USD | `+1.21%` | `11,235.53` |
| `Live` | `Short` | `99.25` | 1,140,000.00 USD | 8,190.00 USD | 0.00 USD | `+1.32%` | `82.53` |
| `Live` | `Short` | `99.35` | 1,240,000.00 USD | 92,570.00 USD | 0.00 USD | `+1.42%` | `931.77` |
| `Live` | `Short` | `99.45` | 1,240,000.00 USD | 335.15 USD | 0.00 USD | `+1.52%` | `3.37` |
| `Live` | `Short` | `99.55` | 1,250,000.00 USD | 11,890.00 USD | 0.00 USD | `+1.62%` | `119.45` |
| `Live` | `Short` | `99.65` | 1,250,000.00 USD | 3,000.00 USD | 0.00 USD | `+1.73%` | `30.14` |
| `Live` | `Short` | `99.75` | 1,280,000.00 USD | 24,780.00 USD | 0.00 USD | `+1.83%` | `248.44` |
| `Live` | `Short` | `99.85` | 1,280,000.00 USD | 410.38 USD | 0.00 USD | `+1.93%` | `4.11` |
| `Live` | `Short` | `99.95` | 1,290,000.00 USD | 10,100.00 USD | 0.00 USD | `+2.03%` | `101.09` |
| `Live` | `Short` | `100.05` | 1,330,000.00 USD | 40,190.00 USD | 0.00 USD | `+2.13%` | `401.74` |
| `Live` | `Short` | `100.15` | 1,380,000.00 USD | 51,840.00 USD | 0.00 USD | `+2.24%` | `517.65` |
| `Live` | `Short` | `100.25` | 1,680,000.00 USD | 298,790.00 USD | 0.00 USD | `+2.34%` | `2,980.49` |
| `Live` | `Short` | `100.35` | 1,860,000.00 USD | 180,560.00 USD | 0.00 USD | `+2.44%` | `1,799.33` |
| `Live` | `Short` | `100.55` | 1,860,000.00 USD | 969.30 USD | 0.00 USD | `+2.64%` | `9.64` |
| `Live` | `Short` | `100.65` | 1,960,000.00 USD | 99,220.00 USD | 0.00 USD | `+2.75%` | `985.80` |
| `Live` | `Short` | `100.75` | 1,980,000.00 USD | 19,020.00 USD | 0.00 USD | `+2.85%` | `188.74` |
| `Live` | `Short` | `100.85` | 2,000,000.00 USD | 16,850.00 USD | 0.00 USD | `+2.95%` | `167.08` |
| `Live` | `Short` | `100.95` | 2,000,000.00 USD | 5,080.00 USD | 0.00 USD | `+3.05%` | `50.30` |
| `Live` | `Short` | `101.05` | 2,000,000.00 USD | 765.96 USD | 0.00 USD | `+3.15%` | `7.58` |
| `Live` | `Short` | `101.15` | 2,010,000.00 USD | 11,950.00 USD | 0.00 USD | `+3.26%` | `118.12` |
| `Live` | `Short` | `101.25` | 2,010,000.00 USD | 769.50 USD | 0.00 USD | `+3.36%` | `7.60` |
| `Live` | `Short` | `101.45` | 2,010,000.00 USD | 118.70 USD | 0.00 USD | `+3.56%` | `1.17` |
| `Live` | `Short` | `101.55` | 2,020,000.00 USD | 2,790.00 USD | 0.00 USD | `+3.66%` | `27.47` |
| `Live` | `Short` | `101.65` | 2,020,000.00 USD | 2,640.00 USD | 0.00 USD | `+3.77%` | `26.02` |
| `Live` | `Short` | `101.85` | 2,020,000.00 USD | 310.64 USD | 0.00 USD | `+3.97%` | `3.05` |
| `Live` | `Short` | `101.95` | 2,020,000.00 USD | 1,560.00 USD | 0.00 USD | `+4.07%` | `15.31` |
| `Live` | `Short` | `102.05` | 2,030,000.00 USD | 4,930.00 USD | 0.00 USD | `+4.18%` | `48.30` |
| `Live` | `Short` | `102.25` | 2,030,000.00 USD | 1,170.00 USD | 0.00 USD | `+4.38%` | `11.44` |
| `Live` | `Short` | `102.45` | 2,030,000.00 USD | 175.19 USD | 0.00 USD | `+4.58%` | `1.71` |
| `Live` | `Short` | `102.65` | 2,050,000.00 USD | 26,740.00 USD | 0.00 USD | `+4.79%` | `260.52` |
| `Live` | `Short` | `102.75` | 2,060,000.00 USD | 2,120.00 USD | 0.00 USD | `+4.89%` | `20.66` |
| `Live` | `Short` | `102.95` | 2,060,000.00 USD | 4,670.00 USD | 0.00 USD | `+5.09%` | `45.37` |
| `Live` | `Short` | `103.05` | 2,060,000.00 USD | 692.50 USD | 0.00 USD | `+5.20%` | `6.72` |
| `Live` | `Short` | `103.15` | 2,070,000.00 USD | 11,000.00 USD | 0.00 USD | `+5.30%` | `106.62` |
| `Live` | `Short` | `103.25` | 2,070,000.00 USD | 346.92 USD | 0.00 USD | `+5.40%` | `3.36` |
| `Live` | `Short` | `103.35` | 2,070,000.00 USD | 385.50 USD | 0.00 USD | `+5.50%` | `3.73` |
| `Live` | `Short` | `103.45` | 2,080,000.00 USD | 3,300.00 USD | 0.00 USD | `+5.60%` | `31.94` |
| `Live` | `Short` | `103.65` | 2,080,000.00 USD | 4,360.00 USD | 0.00 USD | `+5.81%` | `42.09` |
| `Live` | `Short` | `103.75` | 2,340,000.00 USD | 261,580.00 USD | 0.00 USD | `+5.91%` | `2,521.25` |
| `Live` | `Short` | `103.85` | 2,360,000.00 USD | 13,560.00 USD | 0.00 USD | `+6.01%` | `130.56` |
| `Live` | `Short` | `103.95` | 2,360,000.00 USD | 827.44 USD | 0.00 USD | `+6.11%` | `7.96` |
| `Live` | `Short` | `104.05` | 2,360,000.00 USD | 1,400.00 USD | 0.00 USD | `+6.22%` | `13.47` |
| `Live` | `Short` | `104.15` | 2,360,000.00 USD | 1,180.00 USD | 0.00 USD | `+6.32%` | `11.34` |
| `Live` | `Short` | `104.25` | 2,360,000.00 USD | 722.45 USD | 0.00 USD | `+6.42%` | `6.93` |
| `Live` | `Short` | `104.35` | 2,370,000.00 USD | 10,440.00 USD | 0.00 USD | `+6.52%` | `100.00` |
| `Live` | `Short` | `104.45` | 2,380,000.00 USD | 12,640.00 USD | 0.00 USD | `+6.63%` | `120.99` |
| `Live` | `Short` | `104.55` | 2,380,000.00 USD | 464.20 USD | 0.00 USD | `+6.73%` | `4.44` |
| `Live` | `Short` | `104.65` | 2,380,000.00 USD | 1,070.00 USD | 0.00 USD | `+6.83%` | `10.20` |
| `Live` | `Short` | `104.75` | 2,390,000.00 USD | 199.02 USD | 0.00 USD | `+6.93%` | `1.90` |
| `Live` | `Short` | `104.95` | 2,510,000.00 USD | 125,660.00 USD | 0.00 USD | `+7.14%` | `1,197.29` |
| `Live` | `Short` | `105.05` | 2,510,000.00 USD | 329.86 USD | 0.00 USD | `+7.24%` | `3.14` |
| `Live` | `Short` | `105.15` | 2,520,000.00 USD | 6,410.00 USD | 0.00 USD | `+7.34%` | `60.95` |
| `Live` | `Short` | `105.25` | 2,520,000.00 USD | 1,040.00 USD | 0.00 USD | `+7.44%` | `9.84` |
| `Live` | `Short` | `105.35` | 2,520,000.00 USD | 2,710.00 USD | 0.00 USD | `+7.54%` | `25.68` |
| `Live` | `Short` | `105.45` | 3,050,000.00 USD | 527,250.00 USD | 0.00 USD | `+7.65%` | `5,000.00` |
| `Live` | `Short` | `105.55` | 3,050,000.00 USD | 4,180.00 USD | 0.00 USD | `+7.75%` | `39.61` |
| `Live` | `Short` | `105.65` | 3,050,000.00 USD | 247.22 USD | 0.00 USD | `+7.85%` | `2.34` |
| `Live` | `Short` | `105.75` | 3,050,000.00 USD | 750.82 USD | 0.00 USD | `+7.95%` | `7.10` |
| `Live` | `Short` | `105.85` | 3,160,000.00 USD | 103,700.00 USD | 0.00 USD | `+8.05%` | `979.69` |
| `Live` | `Short` | `105.95` | 3,160,000.00 USD | 592.26 USD | 0.00 USD | `+8.16%` | `5.59` |
| `Live` | `Short` | `106.05` | 3,190,000.00 USD | 33,380.00 USD | 0.00 USD | `+8.26%` | `314.77` |
| `Live` | `Short` | `106.15` | 3,200,000.00 USD | 4,030.00 USD | 0.00 USD | `+8.36%` | `37.94` |
| `Live` | `Short` | `106.35` | 3,450,000.00 USD | 252,220.00 USD | 0.00 USD | `+8.56%` | `2,371.56` |
| `Live` | `Short` | `106.45` | 3,480,000.00 USD | 32,940.00 USD | 0.00 USD | `+8.67%` | `309.43` |
| `Live` | `Short` | `106.85` | 3,960,000.00 USD | 478,970.00 USD | 0.00 USD | `+9.08%` | `4,482.65` |
| `Live` | `Short` | `106.95` | 4,040,000.00 USD | 82,630.00 USD | 0.00 USD | `+9.18%` | `772.58` |
| `Live` | `Short` | `107.05` | 4,060,000.00 USD | 17,260.00 USD | 0.00 USD | `+9.28%` | `161.19` |
| `Live` | `Short` | `107.15` | 4,060,000.00 USD | 3,060.00 USD | 0.00 USD | `+9.38%` | `28.58` |
| `Live` | `Short` | `107.25` | 4,100,000.00 USD | 34,950.00 USD | 0.00 USD | `+9.48%` | `325.92` |
| `Live` | `Short` | `107.35` | 4,100,000.00 USD | 766.48 USD | 0.00 USD | `+9.59%` | `7.14` |
| `Live` | `Short` | `107.45` | 4,150,000.00 USD | 49,740.00 USD | 0.00 USD | `+9.69%` | `462.93` |
| `Live` | `Short` | `107.55` | 4,150,000.00 USD | 221.55 USD | 0.00 USD | `+9.79%` | `2.06` |
| `Live` | `Short` | `107.65` | 4,150,000.00 USD | 1,820.00 USD | 0.00 USD | `+9.89%` | `16.87` |
| `Live` | `Short` | `107.75` | 4,160,000.00 USD | 11,710.00 USD | 0.00 USD | `+9.99%` | `108.68` |
| `Live` | `Short` | `107.85` | 4,310,000.00 USD | 143,340.00 USD | 0.00 USD | `+10.10%` | `1,329.08` |
| `Live` | `Short` | `108.05` | 4,310,000.00 USD | 1,080.00 USD | 0.00 USD | `+10.30%` | `10.04` |
| `Live` | `Short` | `108.15` | 4,310,000.00 USD | 1,150.00 USD | 0.00 USD | `+10.40%` | `10.66` |
| `Live` | `Short` | `108.25` | 4,310,000.00 USD | 116.91 USD | 0.00 USD | `+10.50%` | `1.08` |
| `Live` | `Short` | `108.35` | 4,310,000.00 USD | 3,470.00 USD | 0.00 USD | `+10.61%` | `32.00` |
| `Live` | `Short` | `108.45` | 4,420,000.00 USD | 108,080.00 USD | 0.00 USD | `+10.71%` | `996.61` |
| `Live` | `Short` | `108.55` | 4,420,000.00 USD | 117.23 USD | 0.00 USD | `+10.81%` | `1.08` |
| `Live` | `Short` | `108.65` | 4,420,000.00 USD | 5,050.00 USD | 0.00 USD | `+10.91%` | `46.45` |
| `Live` | `Short` | `108.85` | 4,430,000.00 USD | 3,230.00 USD | 0.00 USD | `+11.12%` | `29.68` |
| `Live` | `Short` | `108.95` | 4,430,000.00 USD | 3,170.00 USD | 0.00 USD | `+11.22%` | `29.10` |
| `Live` | `Short` | `109.05` | 4,430,000.00 USD | 163.58 USD | 0.00 USD | `+11.32%` | `1.50` |
| `Live` | `Short` | `109.35` | 4,840,000.00 USD | 407,490.00 USD | 0.00 USD | `+11.63%` | `3,726.43` |
| `Live` | `Short` | `109.45` | 4,840,000.00 USD | 342.58 USD | 0.00 USD | `+11.73%` | `3.13` |
| `Live` | `Short` | `109.55` | 4,840,000.00 USD | 356.04 USD | 0.00 USD | `+11.83%` | `3.25` |
| `Live` | `Short` | `109.65` | 4,880,000.00 USD | 42,030.00 USD | 0.00 USD | `+11.93%` | `383.35` |
| `Live` | `Short` | `109.85` | 4,880,000.00 USD | 459.17 USD | 0.00 USD | `+12.14%` | `4.18` |
| `Live` | `Short` | `109.95` | 4,880,000.00 USD | 2,440.00 USD | 0.00 USD | `+12.24%` | `22.20` |
| `Live` | `Short` | `110.15` | 4,880,000.00 USD | 194.97 USD | 0.00 USD | `+12.44%` | `1.77` |
| `Live` | `Short` | `110.25` | 4,890,000.00 USD | 2,750.00 USD | 0.00 USD | `+12.55%` | `24.90` |
| `Live` | `Short` | `110.35` | 4,900,000.00 USD | 14,530.00 USD | 0.00 USD | `+12.65%` | `131.64` |
| `Live` | `Short` | `110.45` | 5,040,000.00 USD | 143,200.00 USD | 0.00 USD | `+12.75%` | `1,296.50` |
| `Live` | `Short` | `110.55` | 5,070,000.00 USD | 28,380.00 USD | 0.00 USD | `+12.85%` | `256.69` |
| `Live` | `Short` | `110.65` | 5,080,000.00 USD | 10,470.00 USD | 0.00 USD | `+12.95%` | `94.65` |
| `Live` | `Short` | `110.75` | 5,080,000.00 USD | 575.90 USD | 0.00 USD | `+13.06%` | `5.20` |
| `Live` | `Short` | `110.85` | 5,080,000.00 USD | 1,090.00 USD | 0.00 USD | `+13.16%` | `9.87` |
| `Live` | `Short` | `110.95` | 5,090,000.00 USD | 4,450.00 USD | 0.00 USD | `+13.26%` | `40.12` |
| `Live` | `Short` | `111.05` | 5,090,000.00 USD | 196.56 USD | 0.00 USD | `+13.36%` | `1.77` |
| `Live` | `Short` | `111.15` | 5,090,000.00 USD | 1,710.00 USD | 0.00 USD | `+13.46%` | `15.37` |
| `Live` | `Short` | `111.35` | 5,090,000.00 USD | 390.84 USD | 0.00 USD | `+13.67%` | `3.51` |
| `Live` | `Short` | `111.45` | 5,090,000.00 USD | 841.45 USD | 0.00 USD | `+13.77%` | `7.55` |
| `Live` | `Short` | `111.55` | 5,090,000.00 USD | 892.40 USD | 0.00 USD | `+13.87%` | `8.00` |
| `Live` | `Short` | `111.75` | 5,090,000.00 USD | 169.86 USD | 0.00 USD | `+14.08%` | `1.52` |
| `Live` | `Short` | `111.85` | 5,110,000.00 USD | 15,880.00 USD | 0.00 USD | `+14.18%` | `141.95` |
| `Live` | `Short` | `111.95` | 5,110,000.00 USD | 223.90 USD | 0.00 USD | `+14.28%` | `2.00` |
| `Live` | `Short` | `112.15` | 5,110,000.00 USD | 291.59 USD | 0.00 USD | `+14.49%` | `2.60` |
| `Live` | `Short` | `112.35` | 5,110,000.00 USD | 1,910.00 USD | 0.00 USD | `+14.69%` | `17.00` |
| `Live` | `Short` | `112.45` | 5,120,000.00 USD | 5,670.00 USD | 0.00 USD | `+14.79%` | `50.42` |
| `Live` | `Short` | `112.55` | 5,120,000.00 USD | 844.13 USD | 0.00 USD | `+14.89%` | `7.50` |
| `Live` | `Short` | `112.65` | 5,120,000.00 USD | 707.44 USD | 0.00 USD | `+15.00%` | `6.28` |
| `Live` | `Short` | `112.75` | 5,240,000.00 USD | 118,640.00 USD | 0.00 USD | `+15.10%` | `1,052.24` |
| `Live` | `Short` | `112.85` | 5,350,000.00 USD | 108,760.00 USD | 0.00 USD | `+15.20%` | `963.76` |
| `Live` | `Short` | `113.05` | 5,350,000.00 USD | 406.98 USD | 0.00 USD | `+15.40%` | `3.60` |
| `Live` | `Short` | `113.15` | 5,360,000.00 USD | 9,560.00 USD | 0.00 USD | `+15.51%` | `84.51` |
| `Live` | `Short` | `113.25` | 5,360,000.00 USD | 1,940.00 USD | 0.00 USD | `+15.61%` | `17.11` |
| `Live` | `Short` | `113.35` | 5,620,000.00 USD | 263,390.00 USD | 0.00 USD | `+15.71%` | `2,323.72` |
| `Live` | `Short` | `113.45` | 5,630,000.00 USD | 3,360.00 USD | 0.00 USD | `+15.81%` | `29.62` |
| `Live` | `Short` | `113.55` | 5,730,000.00 USD | 102,200.00 USD | 0.00 USD | `+15.91%` | `900.00` |
| `Live` | `Short` | `113.65` | 5,730,000.00 USD | 3,220.00 USD | 0.00 USD | `+16.02%` | `28.37` |
| `Live` | `Short` | `113.75` | 5,730,000.00 USD | 303.71 USD | 0.00 USD | `+16.12%` | `2.67` |
| `Live` | `Short` | `113.85` | 5,730,000.00 USD | 104.74 USD | 0.00 USD | `+16.22%` | `0.92` |
| `Live` | `Short` | `113.95` | 5,750,000.00 USD | 21,840.00 USD | 0.00 USD | `+16.32%` | `191.69` |
| `Live` | `Short` | `114.05` | 5,780,000.00 USD | 31,900.00 USD | 0.00 USD | `+16.43%` | `279.66` |
| `Live` | `Short` | `114.25` | 5,790,000.00 USD | 2,150.00 USD | 0.00 USD | `+16.63%` | `18.80` |
| `Live` | `Short` | `114.35` | 5,830,000.00 USD | 39,970.00 USD | 0.00 USD | `+16.73%` | `349.58` |
| `Live` | `Short` | `114.45` | 5,830,000.00 USD | 3,310.00 USD | 0.00 USD | `+16.83%` | `28.93` |
| `Live` | `Short` | `114.65` | 5,830,000.00 USD | 584.72 USD | 0.00 USD | `+17.04%` | `5.10` |
| `Live` | `Short` | `114.85` | 5,860,000.00 USD | 27,340.00 USD | 0.00 USD | `+17.24%` | `238.04` |
| `Live` | `Short` | `115.05` | 6,430,000.00 USD | 569,550.00 USD | 0.00 USD | `+17.45%` | `4,950.49` |
| `Live` | `Short` | `115.15` | 6,430,000.00 USD | 1,100.00 USD | 0.00 USD | `+17.55%` | `9.52` |
| `Live` | `Short` | `115.25` | 6,450,000.00 USD | 17,810.00 USD | 0.00 USD | `+17.65%` | `154.57` |
| `Live` | `Short` | `115.35` | 7,320,000.00 USD | 878,270.00 USD | 0.00 USD | `+17.75%` | `7,614.00` |
| `Live` | `Short` | `115.55` | 7,370,000.00 USD | 43,020.00 USD | 0.00 USD | `+17.96%` | `372.33` |
| `Live` | `Short` | `115.75` | 7,370,000.00 USD | 160.89 USD | 0.00 USD | `+18.16%` | `1.39` |
| `Live` | `Short` | `115.85` | 7,370,000.00 USD | 289.62 USD | 0.00 USD | `+18.26%` | `2.50` |
| `Live` | `Short` | `115.95` | 7,370,000.00 USD | 441.77 USD | 0.00 USD | `+18.36%` | `3.81` |
| `Live` | `Short` | `116.05` | 7,370,000.00 USD | 4,450.00 USD | 0.00 USD | `+18.47%` | `38.34` |
| `Live` | `Short` | `116.25` | 7,370,000.00 USD | 180.19 USD | 0.00 USD | `+18.67%` | `1.55` |
| `Live` | `Short` | `116.35` | 7,380,000.00 USD | 4,960.00 USD | 0.00 USD | `+18.77%` | `42.60` |
| `Live` | `Short` | `116.55` | 7,380,000.00 USD | 2,040.00 USD | 0.00 USD | `+18.98%` | `17.52` |
| `Live` | `Short` | `116.65` | 7,380,000.00 USD | 113.15 USD | 0.00 USD | `+19.08%` | `0.97` |
| `Live` | `Short` | `117.05` | 7,380,000.00 USD | 156.85 USD | 0.00 USD | `+19.49%` | `1.34` |
| `Live` | `Short` | `117.15` | 12,240,000.00 USD | 4,860,000.00 USD | 0.00 USD | `+19.59%` | `41,484.61` |
| `Live` | `Short` | `117.35` | 12,250,000.00 USD | 11,610.00 USD | 0.00 USD | `+19.79%` | `98.95` |
| `Live` | `Short` | `117.55` | 12,250,000.00 USD | 188.08 USD | 0.00 USD | `+20.00%` | `1.60` |
| `Live` | `Short` | `117.65` | 12,280,000.00 USD | 23,530.00 USD | 0.00 USD | `+20.10%` | `200.00` |
| `Live` | `Short` | `117.75` | 12,290,000.00 USD | 10,360.00 USD | 0.00 USD | `+20.20%` | `87.98` |
| `Live` | `Short` | `117.95` | 12,290,000.00 USD | 353.85 USD | 0.00 USD | `+20.41%` | `3.00` |
| `Live` | `Short` | `118.05` | 16,750,000.00 USD | 4,460,000.00 USD | 0.00 USD | `+20.51%` | `37,796.13` |
| `Live` | `Short` | `118.15` | 16,750,000.00 USD | 4,140.00 USD | 0.00 USD | `+20.61%` | `35.00` |
| `Live` | `Short` | `118.45` | 16,780,000.00 USD | 30,080.00 USD | 0.00 USD | `+20.92%` | `253.91` |
| `Live` | `Short` | `118.55` | 16,780,000.00 USD | 1,110.00 USD | 0.00 USD | `+21.02%` | `9.38` |
| `Live` | `Short` | `118.75` | 16,780,000.00 USD | 309.94 USD | 0.00 USD | `+21.22%` | `2.61` |
| `Live` | `Short` | `118.85` | 16,800,000.00 USD | 18,610.00 USD | 0.00 USD | `+21.33%` | `156.58` |
| `Live` | `Short` | `118.95` | 16,830,000.00 USD | 28,010.00 USD | 0.00 USD | `+21.43%` | `235.47` |
| `Live` | `Short` | `119.05` | 16,840,000.00 USD | 12,470.00 USD | 0.00 USD | `+21.53%` | `104.72` |
| `Live` | `Short` | `119.25` | 16,840,000.00 USD | 240.88 USD | 0.00 USD | `+21.73%` | `2.02` |
| `Live` | `Short` | `119.35` | 16,900,000.00 USD | 57,850.00 USD | 0.00 USD | `+21.84%` | `484.72` |
| `Live` | `Short` | `119.55` | 16,910,000.00 USD | 8,970.00 USD | 0.00 USD | `+22.04%` | `75.00` |
| `Live` | `Short` | `119.75` | 16,910,000.00 USD | 1,790.00 USD | 0.00 USD | `+22.24%` | `14.98` |
| `Live` | `Short` | `119.85` | 17,010,000.00 USD | 96,440.00 USD | 0.00 USD | `+22.35%` | `804.65` |
| `Live` | `Short` | `120.15` | 17,010,000.00 USD | 2,980.00 USD | 0.00 USD | `+22.65%` | `24.83` |
| `Live` | `Short` | `120.45` | 17,010,000.00 USD | 619.11 USD | 0.00 USD | `+22.96%` | `5.14` |
| `Live` | `Short` | `120.55` | 17,010,000.00 USD | 1,190.00 USD | 0.00 USD | `+23.06%` | `9.86` |
| `Live` | `Short` | `120.95` | 17,030,000.00 USD | 13,290.00 USD | 0.00 USD | `+23.47%` | `109.91` |
| `Live` | `Short` | `121.15` | 17,030,000.00 USD | 960.72 USD | 0.00 USD | `+23.67%` | `7.93` |
| `Live` | `Short` | `121.55` | 17,030,000.00 USD | 5,940.00 USD | 0.00 USD | `+24.08%` | `48.87` |
| `Live` | `Short` | `121.75` | 17,030,000.00 USD | 105.92 USD | 0.00 USD | `+24.29%` | `0.87` |
| `Live` | `Short` | `122.05` | 17,970,000.00 USD | 935,440.00 USD | 0.00 USD | `+24.59%` | `7,664.41` |
| `Live` | `Short` | `122.15` | 17,970,000.00 USD | 500.81 USD | 0.00 USD | `+24.69%` | `4.10` |
| `Live` | `Short` | `122.25` | 17,970,000.00 USD | 3,920.00 USD | 0.00 USD | `+24.80%` | `32.03` |
| `Live` | `Short` | `122.35` | 17,970,000.00 USD | 357.26 USD | 0.00 USD | `+24.90%` | `2.92` |
| `Live` | `Short` | `122.45` | 17,990,000.00 USD | 17,500.00 USD | 0.00 USD | `+25.00%` | `142.95` |
| `Live` | `Short` | `122.65` | 17,990,000.00 USD | 116.52 USD | 0.00 USD | `+25.20%` | `0.95` |
| `Live` | `Short` | `122.95` | 17,990,000.00 USD | 1,650.00 USD | 0.00 USD | `+25.51%` | `13.39` |
| `Live` | `Short` | `123.05` | 17,990,000.00 USD | 525.42 USD | 0.00 USD | `+25.61%` | `4.27` |
| `Live` | `Short` | `123.25` | 18,120,000.00 USD | 124,110.00 USD | 0.00 USD | `+25.82%` | `1,006.96` |
| `Live` | `Short` | `123.35` | 18,120,000.00 USD | 2,330.00 USD | 0.00 USD | `+25.92%` | `18.92` |
| `Live` | `Short` | `123.45` | 18,120,000.00 USD | 1,960.00 USD | 0.00 USD | `+26.02%` | `15.87` |
| `Live` | `Short` | `123.65` | 18,120,000.00 USD | 697.39 USD | 0.00 USD | `+26.22%` | `5.64` |
| `Live` | `Short` | `124.05` | 18,120,000.00 USD | 586.76 USD | 0.00 USD | `+26.63%` | `4.73` |
| `Live` | `Short` | `124.15` | 18,120,000.00 USD | 121.67 USD | 0.00 USD | `+26.74%` | `0.98` |
| `Live` | `Short` | `124.25` | 18,150,000.00 USD | 23,360.00 USD | 0.00 USD | `+26.84%` | `188.01` |
| `Live` | `Short` | `124.35` | 18,150,000.00 USD | 114.40 USD | 0.00 USD | `+26.94%` | `0.92` |
| `Live` | `Short` | `124.45` | 18,190,000.00 USD | 46,110.00 USD | 0.00 USD | `+27.04%` | `370.50` |
| `Live` | `Short` | `124.55` | 18,200,000.00 USD | 3,080.00 USD | 0.00 USD | `+27.14%` | `24.76` |
| `Live` | `Short` | `124.65` | 18,200,000.00 USD | 675.60 USD | 0.00 USD | `+27.25%` | `5.42` |
| `Live` | `Short` | `124.75` | 26,850,000.00 USD | 8,660,000.00 USD | 0.00 USD | `+27.35%` | `69,396.25` |
| `Live` | `Short` | `124.95` | 26,860,000.00 USD | 9,550.00 USD | 0.00 USD | `+27.55%` | `76.46` |
| `Live` | `Short` | `125.05` | 26,860,000.00 USD | 208.83 USD | 0.00 USD | `+27.65%` | `1.67` |
| `Live` | `Short` | `125.35` | 26,870,000.00 USD | 5,320.00 USD | 0.00 USD | `+27.96%` | `42.44` |
| `Live` | `Short` | `125.45` | 26,870,000.00 USD | 590.87 USD | 0.00 USD | `+28.06%` | `4.71` |
| `Live` | `Short` | `125.55` | 26,870,000.00 USD | 4,610.00 USD | 0.00 USD | `+28.16%` | `36.71` |
| `Live` | `Short` | `125.65` | 26,880,000.00 USD | 851.91 USD | 0.00 USD | `+28.27%` | `6.78` |
| `Live` | `Short` | `125.75` | 26,880,000.00 USD | 4,600.00 USD | 0.00 USD | `+28.37%` | `36.61` |
| `Live` | `Short` | `125.95` | 26,880,000.00 USD | 110.84 USD | 0.00 USD | `+28.57%` | `0.88` |
| `Live` | `Short` | `126.05` | 26,880,000.00 USD | 810.50 USD | 0.00 USD | `+28.67%` | `6.43` |
| `Live` | `Short` | `126.15` | 26,880,000.00 USD | 470.54 USD | 0.00 USD | `+28.78%` | `3.73` |
| `Live` | `Short` | `126.35` | 26,890,000.00 USD | 4,090.00 USD | 0.00 USD | `+28.98%` | `32.36` |
| `Live` | `Short` | `126.45` | 26,890,000.00 USD | 117.60 USD | 0.00 USD | `+29.08%` | `0.93` |
| `Live` | `Short` | `126.65` | 26,920,000.00 USD | 30,830.00 USD | 0.00 USD | `+29.29%` | `243.46` |
| `Live` | `Short` | `126.85` | 26,920,000.00 USD | 3,870.00 USD | 0.00 USD | `+29.49%` | `30.49` |
| `Live` | `Short` | `127.05` | 26,920,000.00 USD | 2,030.00 USD | 0.00 USD | `+29.70%` | `16.01` |
| `Live` | `Short` | `127.35` | 26,940,000.00 USD | 16,190.00 USD | 0.00 USD | `+30.00%` | `127.13` |
| `Live` | `Short` | `127.65` | 26,940,000.00 USD | 4,840.00 USD | 0.00 USD | `+30.31%` | `37.89` |
| `Live` | `Short` | `127.85` | 26,940,000.00 USD | 388.66 USD | 0.00 USD | `+30.51%` | `3.04` |
| `Live` | `Short` | `127.95` | 26,950,000.00 USD | 10,510.00 USD | 0.00 USD | `+30.61%` | `82.13` |
| `Live` | `Short` | `128.05` | 27,070,000.00 USD | 116,190.00 USD | 0.00 USD | `+30.72%` | `907.38` |
| `Live` | `Short` | `128.35` | 27,070,000.00 USD | 195.09 USD | 0.00 USD | `+31.02%` | `1.52` |
| `Live` | `Short` | `128.65` | 27,070,000.00 USD | 788.62 USD | 0.00 USD | `+31.33%` | `6.13` |
| `Live` | `Short` | `128.75` | 27,090,000.00 USD | 18,730.00 USD | 0.00 USD | `+31.43%` | `145.45` |
| `Live` | `Short` | `128.85` | 27,120,000.00 USD | 32,440.00 USD | 0.00 USD | `+31.53%` | `251.77` |
| `Live` | `Short` | `129.05` | 27,120,000.00 USD | 603.95 USD | 0.00 USD | `+31.74%` | `4.68` |
| `Live` | `Short` | `129.15` | 27,950,000.00 USD | 822,240.00 USD | 0.00 USD | `+31.84%` | `6,366.52` |
| `Live` | `Short` | `129.25` | 27,980,000.00 USD | 38,770.00 USD | 0.00 USD | `+31.94%` | `300.00` |
| `Live` | `Short` | `129.35` | 27,980,000.00 USD | 164.27 USD | 0.00 USD | `+32.04%` | `1.27` |
| `Live` | `Short` | `129.55` | 27,980,000.00 USD | 910.74 USD | 0.00 USD | `+32.25%` | `7.03` |
| `Live` | `Short` | `129.65` | 27,990,000.00 USD | 127.06 USD | 0.00 USD | `+32.35%` | `0.98` |
| `Live` | `Short` | `129.75` | 27,990,000.00 USD | 2,210.00 USD | 0.00 USD | `+32.45%` | `17.05` |
| `Live` | `Short` | `129.85` | 27,990,000.00 USD | 490.83 USD | 0.00 USD | `+32.55%` | `3.78` |
| `Live` | `Short` | `130.05` | 28,000,000.00 USD | 13,180.00 USD | 0.00 USD | `+32.76%` | `101.38` |
| `Live` | `Short` | `130.35` | 28,000,000.00 USD | 145.99 USD | 0.00 USD | `+33.06%` | `1.12` |
| `Live` | `Short` | `130.65` | 28,000,000.00 USD | 2,210.00 USD | 0.00 USD | `+33.37%` | `16.89` |
| `Live` | `Short` | `130.85` | 28,510,000.00 USD | 503,820.00 USD | 0.00 USD | `+33.57%` | `3,850.39` |
| `Live` | `Short` | `130.95` | 28,510,000.00 USD | 2,070.00 USD | 0.00 USD | `+33.68%` | `15.84` |
| `Live` | `Short` | `131.05` | 28,510,000.00 USD | 188.71 USD | 0.00 USD | `+33.78%` | `1.44` |
| `Live` | `Short` | `131.25` | 28,510,000.00 USD | 1,560.00 USD | 0.00 USD | `+33.98%` | `11.87` |
| `Live` | `Short` | `131.45` | 28,510,000.00 USD | 219.52 USD | 0.00 USD | `+34.19%` | `1.67` |
| `Live` | `Short` | `131.65` | 28,510,000.00 USD | 3,590.00 USD | 0.00 USD | `+34.39%` | `27.29` |
| `Live` | `Short` | `131.85` | 28,520,000.00 USD | 3,100.00 USD | 0.00 USD | `+34.60%` | `23.54` |
| `Live` | `Short` | `131.95` | 28,520,000.00 USD | 106.88 USD | 0.00 USD | `+34.70%` | `0.81` |
| `Live` | `Short` | `132.05` | 28,530,000.00 USD | 11,940.00 USD | 0.00 USD | `+34.80%` | `90.43` |
| `Live` | `Short` | `132.15` | 28,530,000.00 USD | 712.29 USD | 0.00 USD | `+34.90%` | `5.39` |
| `Live` | `Short` | `132.35` | 28,530,000.00 USD | 3,960.00 USD | 0.00 USD | `+35.11%` | `29.93` |
| `Live` | `Short` | `132.55` | 28,540,000.00 USD | 8,730.00 USD | 0.00 USD | `+35.31%` | `65.85` |
| `Live` | `Short` | `132.65` | 28,610,000.00 USD | 66,570.00 USD | 0.00 USD | `+35.41%` | `501.81` |
| `Live` | `Short` | `132.85` | 28,660,000.00 USD | 49,280.00 USD | 0.00 USD | `+35.62%` | `370.98` |
| `Live` | `Short` | `132.95` | 28,710,000.00 USD | 47,950.00 USD | 0.00 USD | `+35.72%` | `360.65` |
| `Live` | `Short` | `133.05` | 28,710,000.00 USD | 103.78 USD | 0.00 USD | `+35.82%` | `0.78` |
| `Live` | `Short` | `133.15` | 28,720,000.00 USD | 8,440.00 USD | 0.00 USD | `+35.92%` | `63.42` |
| `Live` | `Short` | `133.55` | 28,750,000.00 USD | 30,060.00 USD | 0.00 USD | `+36.33%` | `225.08` |
| `Live` | `Short` | `133.65` | 28,750,000.00 USD | 156.37 USD | 0.00 USD | `+36.43%` | `1.17` |
| `Live` | `Short` | `133.75` | 28,900,000.00 USD | 151,200.00 USD | 0.00 USD | `+36.54%` | `1,130.50` |
| `Live` | `Short` | `133.85` | 28,900,000.00 USD | 1,600.00 USD | 0.00 USD | `+36.64%` | `11.97` |
| `Live` | `Short` | `133.95` | 29,000,000.00 USD | 100,970.00 USD | 0.00 USD | `+36.74%` | `753.76` |
| `Live` | `Short` | `134.05` | 29,010,000.00 USD | 12,620.00 USD | 0.00 USD | `+36.84%` | `94.18` |
| `Live` | `Short` | `134.25` | 29,020,000.00 USD | 11,590.00 USD | 0.00 USD | `+37.05%` | `86.32` |
| `Live` | `Short` | `135.35` | 29,030,000.00 USD | 6,400.00 USD | 0.00 USD | `+38.17%` | `47.30` |
| `Live` | `Short` | `135.85` | 29,030,000.00 USD | 3,250.00 USD | 0.00 USD | `+38.68%` | `23.94` |
| `Live` | `Short` | `135.95` | 29,030,000.00 USD | 504.37 USD | 0.00 USD | `+38.78%` | `3.71` |
| `Live` | `Short` | `136.55` | 29,030,000.00 USD | 136.55 USD | 0.00 USD | `+39.39%` | `1.00` |
| `Live` | `Short` | `136.65` | 29,040,000.00 USD | 1,110.00 USD | 0.00 USD | `+39.50%` | `8.14` |
| `Live` | `Short` | `136.95` | 29,080,000.00 USD | 48,960.00 USD | 0.00 USD | `+39.80%` | `357.50` |
| `Live` | `Short` | `137.05` | 29,090,000.00 USD | 1,530.00 USD | 0.00 USD | `+39.90%` | `11.17` |
| `Live` | `Short` | `137.15` | 29,090,000.00 USD | 2,850.00 USD | 0.00 USD | `+40.01%` | `20.77` |
| `Live` | `Short` | `137.85` | 29,090,000.00 USD | 2,810.00 USD | 0.00 USD | `+40.72%` | `20.42` |
| `Live` | `Short` | `138.05` | 29,100,000.00 USD | 9,810.00 USD | 0.00 USD | `+40.92%` | `71.04` |
| `Live` | `Short` | `138.15` | 29,140,000.00 USD | 41,450.00 USD | 0.00 USD | `+41.03%` | `300.00` |
| `Live` | `Short` | `138.25` | 29,190,000.00 USD | 45,220.00 USD | 0.00 USD | `+41.13%` | `327.11` |
| `Live` | `Short` | `138.45` | 29,200,000.00 USD | 7,310.00 USD | 0.00 USD | `+41.33%` | `52.83` |
| `Live` | `Short` | `138.75` | 29,200,000.00 USD | 2,360.00 USD | 0.00 USD | `+41.64%` | `17.04` |
| `Live` | `Short` | `139.15` | 29,200,000.00 USD | 552.43 USD | 0.00 USD | `+42.05%` | `3.97` |
| `Live` | `Short` | `139.35` | 29,200,000.00 USD | 1,670.00 USD | 0.00 USD | `+42.25%` | `12.02` |
| `Live` | `Short` | `139.45` | 29,200,000.00 USD | 253.80 USD | 0.00 USD | `+42.35%` | `1.82` |
| `Live` | `Short` | `139.55` | 29,200,000.00 USD | 494.01 USD | 0.00 USD | `+42.46%` | `3.54` |
| `Live` | `Short` | `139.75` | 29,210,000.00 USD | 4,870.00 USD | 0.00 USD | `+42.66%` | `34.82` |
| `Live` | `Short` | `139.85` | 29,250,000.00 USD | 41,280.00 USD | 0.00 USD | `+42.76%` | `295.19` |
| `Live` | `Short` | `139.95` | 29,250,000.00 USD | 394.66 USD | 0.00 USD | `+42.86%` | `2.82` |
| `Live` | `Short` | `140.05` | 34,230,000.00 USD | 4,980,000.00 USD | 0.00 USD | `+42.97%` | `35,590.87` |
| `Live` | `Short` | `140.15` | 34,240,000.00 USD | 13,370.00 USD | 0.00 USD | `+43.07%` | `95.37` |
| `Live` | `Short` | `140.35` | 34,250,000.00 USD | 158.60 USD | 0.00 USD | `+43.27%` | `1.13` |
| `Live` | `Short` | `140.45` | 34,250,000.00 USD | 4,870.00 USD | 0.00 USD | `+43.37%` | `34.66` |
| `Live` | `Short` | `140.55` | 34,250,000.00 USD | 702.75 USD | 0.00 USD | `+43.48%` | `5.00` |
| `Live` | `Short` | `140.65` | 34,330,000.00 USD | 74,520.00 USD | 0.00 USD | `+43.58%` | `529.83` |
| `Live` | `Short` | `140.95` | 34,330,000.00 USD | 2,600.00 USD | 0.00 USD | `+43.89%` | `18.43` |
| `Live` | `Short` | `141.05` | 34,330,000.00 USD | 3,080.00 USD | 0.00 USD | `+43.99%` | `21.83` |
| `Live` | `Short` | `141.15` | 34,350,000.00 USD | 22,890.00 USD | 0.00 USD | `+44.09%` | `162.19` |
| `Live` | `Short` | `141.25` | 35,430,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+44.19%` | `7,609.58` |
| `Live` | `Short` | `141.35` | 36,300,000.00 USD | 867,610.00 USD | 0.00 USD | `+44.29%` | `6,138.02` |
| `Live` | `Short` | `141.45` | 36,540,000.00 USD | 247,540.00 USD | 0.00 USD | `+44.40%` | `1,750.00` |
| `Live` | `Short` | `141.55` | 36,540,000.00 USD | 236.39 USD | 0.00 USD | `+44.50%` | `1.67` |
| `Live` | `Short` | `141.65` | 36,540,000.00 USD | 780.49 USD | 0.00 USD | `+44.60%` | `5.51` |
| `Live` | `Short` | `141.75` | 36,550,000.00 USD | 4,900.00 USD | 0.00 USD | `+44.70%` | `34.57` |
| `Live` | `Short` | `141.95` | 36,550,000.00 USD | 112.14 USD | 0.00 USD | `+44.91%` | `0.79` |
| `Live` | `Short` | `142.15` | 36,550,000.00 USD | 2,430.00 USD | 0.00 USD | `+45.11%` | `17.10` |
| `Live` | `Short` | `142.45` | 36,570,000.00 USD | 19,240.00 USD | 0.00 USD | `+45.42%` | `135.07` |
| `Live` | `Short` | `142.65` | 36,590,000.00 USD | 21,940.00 USD | 0.00 USD | `+45.62%` | `153.80` |
| `Live` | `Short` | `142.75` | 36,620,000.00 USD | 28,420.00 USD | 0.00 USD | `+45.72%` | `199.08` |
| `Live` | `Short` | `142.85` | 36,620,000.00 USD | 595.68 USD | 0.00 USD | `+45.82%` | `4.17` |
| `Live` | `Short` | `143.15` | 36,620,000.00 USD | 1,330.00 USD | 0.00 USD | `+46.13%` | `9.31` |
| `Live` | `Short` | `143.35` | 36,650,000.00 USD | 22,260.00 USD | 0.00 USD | `+46.34%` | `155.27` |
| `Live` | `Short` | `143.45` | 37,240,000.00 USD | 595,460.00 USD | 0.00 USD | `+46.44%` | `4,151.00` |
| `Live` | `Short` | `143.55` | 37,240,000.00 USD | 103.36 USD | 0.00 USD | `+46.54%` | `0.72` |
| `Live` | `Short` | `143.65` | 37,350,000.00 USD | 104,880.00 USD | 0.00 USD | `+46.64%` | `730.14` |
| `Live` | `Short` | `144.05` | 37,350,000.00 USD | 3,750.00 USD | 0.00 USD | `+47.05%` | `26.00` |
| `Live` | `Short` | `144.65` | 37,350,000.00 USD | 1,240.00 USD | 0.00 USD | `+47.66%` | `8.60` |
| `Live` | `Short` | `145.15` | 37,350,000.00 USD | 1,760.00 USD | 0.00 USD | `+48.17%` | `12.12` |
| `Live` | `Short` | `145.45` | 37,380,000.00 USD | 29,480.00 USD | 0.00 USD | `+48.48%` | `202.66` |
| `Live` | `Short` | `145.85` | 37,390,000.00 USD | 5,850.00 USD | 0.00 USD | `+48.89%` | `40.09` |
| `Live` | `Short` | `146.05` | 37,480,000.00 USD | 88,930.00 USD | 0.00 USD | `+49.09%` | `608.87` |
| `Live` | `Short` | `146.15` | 37,570,000.00 USD | 88,760.00 USD | 0.00 USD | `+49.19%` | `607.33` |
| `Live` | `Short` | `146.25` | 37,570,000.00 USD | 2,770.00 USD | 0.00 USD | `+49.30%` | `18.95` |
| `Live` | `Short` | `146.35` | 37,580,000.00 USD | 7,330.00 USD | 0.00 USD | `+49.40%` | `50.10` |
| `Live` | `Short` | `146.55` | 37,580,000.00 USD | 3,390.00 USD | 0.00 USD | `+49.60%` | `23.16` |
| `Live` | `Short` | `146.65` | 38,170,000.00 USD | 587,730.00 USD | 0.00 USD | `+49.70%` | `4,007.68` |
| `Live` | `Short` | `146.95` | 38,170,000.00 USD | 3,070.00 USD | 0.00 USD | `+50.01%` | `20.88` |
| `Live` | `Short` | `147.05` | 38,170,000.00 USD | 166.17 USD | 0.00 USD | `+50.11%` | `1.13` |
| `Live` | `Short` | `147.15` | 38,170,000.00 USD | 1,730.00 USD | 0.00 USD | `+50.21%` | `11.75` |
| `Live` | `Short` | `147.35` | 38,170,000.00 USD | 1,580.00 USD | 0.00 USD | `+50.42%` | `10.72` |
| `Live` | `Short` | `147.45` | 38,170,000.00 USD | 204.96 USD | 0.00 USD | `+50.52%` | `1.39` |
| `Live` | `Short` | `147.55` | 38,180,000.00 USD | 1,000.00 USD | 0.00 USD | `+50.62%` | `6.78` |
| `Live` | `Short` | `147.65` | 38,180,000.00 USD | 237.72 USD | 0.00 USD | `+50.72%` | `1.61` |
| `Live` | `Short` | `147.75` | 38,180,000.00 USD | 2,470.00 USD | 0.00 USD | `+50.83%` | `16.72` |
| `Live` | `Short` | `147.85` | 38,700,000.00 USD | 522,270.00 USD | 0.00 USD | `+50.93%` | `3,532.45` |
| `Live` | `Short` | `147.95` | 39,220,000.00 USD | 517,820.00 USD | 0.00 USD | `+51.03%` | `3,500.00` |
| `Live` | `Short` | `148.15` | 39,220,000.00 USD | 102.22 USD | 0.00 USD | `+51.24%` | `0.69` |
| `Live` | `Short` | `148.35` | 39,220,000.00 USD | 278.90 USD | 0.00 USD | `+51.44%` | `1.88` |
| `Live` | `Short` | `148.45` | 39,220,000.00 USD | 5,800.00 USD | 0.00 USD | `+51.54%` | `39.10` |
| `Live` | `Short` | `148.55` | 39,570,000.00 USD | 344,780.00 USD | 0.00 USD | `+51.64%` | `2,321.00` |
| `Live` | `Short` | `148.75` | 39,660,000.00 USD | 93,700.00 USD | 0.00 USD | `+51.85%` | `629.91` |
| `Live` | `Short` | `149.05` | 39,820,000.00 USD | 161,460.00 USD | 0.00 USD | `+52.15%` | `1,083.29` |
| `Live` | `Short` | `149.15` | 41,210,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+52.26%` | `9,282.33` |
| `Live` | `Short` | `149.55` | 41,210,000.00 USD | 116.65 USD | 0.00 USD | `+52.66%` | `0.78` |
| `Live` | `Short` | `149.65` | 41,220,000.00 USD | 16,030.00 USD | 0.00 USD | `+52.77%` | `107.15` |
| `Live` | `Short` | `149.75` | 41,240,000.00 USD | 16,320.00 USD | 0.00 USD | `+52.87%` | `109.00` |
| `Live` | `Short` | `149.95` | 41,240,000.00 USD | 178.44 USD | 0.00 USD | `+53.07%` | `1.19` |
| `Live` | `Short` | `150.05` | 41,240,000.00 USD | 2,930.00 USD | 0.00 USD | `+53.17%` | `19.54` |
| `Live` | `Short` | `150.25` | 41,370,000.00 USD | 123,390.00 USD | 0.00 USD | `+53.38%` | `821.21` |
| `Live` | `Short` | `150.55` | 41,370,000.00 USD | 346.26 USD | 0.00 USD | `+53.69%` | `2.30` |
| `Live` | `Short` | `150.65` | 41,390,000.00 USD | 17,300.00 USD | 0.00 USD | `+53.79%` | `114.86` |
| `Live` | `Short` | `150.75` | 41,390,000.00 USD | 2,370.00 USD | 0.00 USD | `+53.89%` | `15.69` |
| `Live` | `Short` | `151.05` | 43,130,000.00 USD | 1,740,000.00 USD | 0.00 USD | `+54.20%` | `11,506.64` |
| `Live` | `Short` | `151.15` | 43,130,000.00 USD | 3,180.00 USD | 0.00 USD | `+54.30%` | `21.05` |
| `Live` | `Short` | `151.45` | 43,170,000.00 USD | 38,210.00 USD | 0.00 USD | `+54.60%` | `252.32` |
| `Live` | `Short` | `151.75` | 44,270,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+54.91%` | `7,271.63` |
| `Live` | `Short` | `151.95` | 44,270,000.00 USD | 1,920.00 USD | 0.00 USD | `+55.11%` | `12.64` |
| `Live` | `Short` | `152.05` | 44,320,000.00 USD | 44,540.00 USD | 0.00 USD | `+55.22%` | `292.91` |
| `Live` | `Short` | `152.15` | 44,320,000.00 USD | 1,470.00 USD | 0.00 USD | `+55.32%` | `9.68` |
| `Live` | `Short` | `152.25` | 44,320,000.00 USD | 200.97 USD | 0.00 USD | `+55.42%` | `1.32` |
| `Live` | `Short` | `152.35` | 44,610,000.00 USD | 286,550.00 USD | 0.00 USD | `+55.52%` | `1,880.87` |
| `Live` | `Short` | `152.45` | 44,610,000.00 USD | 3,150.00 USD | 0.00 USD | `+55.62%` | `20.65` |
| `Live` | `Short` | `152.55` | 45,030,000.00 USD | 423,220.00 USD | 0.00 USD | `+55.73%` | `2,774.28` |
| `Live` | `Short` | `152.75` | 45,030,000.00 USD | 1,570.00 USD | 0.00 USD | `+55.93%` | `10.30` |
| `Live` | `Short` | `152.95` | 45,080,000.00 USD | 44,550.00 USD | 0.00 USD | `+56.14%` | `291.26` |
| `Live` | `Short` | `153.05` | 45,080,000.00 USD | 479.05 USD | 0.00 USD | `+56.24%` | `3.13` |
| `Live` | `Short` | `153.15` | 45,080,000.00 USD | 1,060.00 USD | 0.00 USD | `+56.34%` | `6.95` |
| `Live` | `Short` | `153.25` | 45,840,000.00 USD | 761,340.00 USD | 0.00 USD | `+56.44%` | `4,967.95` |
| `Live` | `Short` | `153.35` | 45,840,000.00 USD | 2,300.00 USD | 0.00 USD | `+56.54%` | `15.00` |
| `Live` | `Short` | `153.65` | 45,850,000.00 USD | 8,340.00 USD | 0.00 USD | `+56.85%` | `54.29` |
| `Live` | `Short` | `154.05` | 45,850,000.00 USD | 223.37 USD | 0.00 USD | `+57.26%` | `1.45` |
| `Live` | `Short` | `154.15` | 45,850,000.00 USD | 292.89 USD | 0.00 USD | `+57.36%` | `1.90` |
| `Live` | `Short` | `154.25` | 45,850,000.00 USD | 2,340.00 USD | 0.00 USD | `+57.46%` | `15.20` |
| `Live` | `Short` | `154.45` | 45,860,000.00 USD | 4,240.00 USD | 0.00 USD | `+57.67%` | `27.45` |
| `Live` | `Short` | `154.75` | 45,860,000.00 USD | 363.66 USD | 0.00 USD | `+57.97%` | `2.35` |
| `Live` | `Short` | `154.95` | 45,860,000.00 USD | 2,180.00 USD | 0.00 USD | `+58.18%` | `14.05` |
| `Live` | `Short` | `155.05` | 45,860,000.00 USD | 117.84 USD | 0.00 USD | `+58.28%` | `0.76` |
| `Live` | `Short` | `155.35` | 50,570,000.00 USD | 4,710,000.00 USD | 0.00 USD | `+58.59%` | `30,310.49` |
| `Live` | `Short` | `155.55` | 50,570,000.00 USD | 267.55 USD | 0.00 USD | `+58.79%` | `1.72` |
| `Live` | `Short` | `156.05` | 50,580,000.00 USD | 7,800.00 USD | 0.00 USD | `+59.30%` | `50.00` |
| `Live` | `Short` | `156.25` | 50,600,000.00 USD | 18,300.00 USD | 0.00 USD | `+59.50%` | `117.09` |
| `Live` | `Short` | `156.35` | 54,160,000.00 USD | 3,560,000.00 USD | 0.00 USD | `+59.61%` | `22,772.00` |
| `Live` | `Short` | `156.45` | 54,160,000.00 USD | 5,220.00 USD | 0.00 USD | `+59.71%` | `33.38` |
| `Live` | `Short` | `156.65` | 54,160,000.00 USD | 310.17 USD | 0.00 USD | `+59.91%` | `1.98` |
| `Live` | `Short` | `157.15` | 54,210,000.00 USD | 49,270.00 USD | 0.00 USD | `+60.42%` | `313.50` |
| `Live` | `Short` | `157.25` | 54,870,000.00 USD | 660,450.00 USD | 0.00 USD | `+60.52%` | `4,200.00` |
| `Live` | `Short` | `157.35` | 54,870,000.00 USD | 297.39 USD | 0.00 USD | `+60.63%` | `1.89` |
| `Live` | `Short` | `157.45` | 54,970,000.00 USD | 100,280.00 USD | 0.00 USD | `+60.73%` | `636.89` |
| `Live` | `Short` | `157.55` | 54,970,000.00 USD | 189.06 USD | 0.00 USD | `+60.83%` | `1.20` |
| `Live` | `Short` | `157.65` | 54,970,000.00 USD | 654.25 USD | 0.00 USD | `+60.93%` | `4.15` |
| `Live` | `Short` | `157.75` | 55,070,000.00 USD | 92,600.00 USD | 0.00 USD | `+61.04%` | `587.00` |
| `Live` | `Short` | `158.05` | 55,150,000.00 USD | 79,830.00 USD | 0.00 USD | `+61.34%` | `505.07` |
| `Live` | `Short` | `158.55` | 55,150,000.00 USD | 1,410.00 USD | 0.00 USD | `+61.85%` | `8.89` |
| `Live` | `Short` | `158.75` | 55,150,000.00 USD | 3,520.00 USD | 0.00 USD | `+62.06%` | `22.17` |
| `Live` | `Short` | `159.05` | 55,200,000.00 USD | 44,690.00 USD | 0.00 USD | `+62.36%` | `281.00` |
| `Live` | `Short` | `159.45` | 55,220,000.00 USD | 27,950.00 USD | 0.00 USD | `+62.77%` | `175.30` |
| `Live` | `Short` | `159.65` | 55,220,000.00 USD | 1,760.00 USD | 0.00 USD | `+62.97%` | `11.01` |
| `Live` | `Short` | `159.75` | 55,230,000.00 USD | 496.82 USD | 0.00 USD | `+63.08%` | `3.11` |
| `Live` | `Short` | `160.15` | 55,910,000.00 USD | 683,000.00 USD | 0.00 USD | `+63.49%` | `4,264.75` |
| `Live` | `Short` | `160.25` | 61,540,000.00 USD | 5,640,000.00 USD | 0.00 USD | `+63.59%` | `35,170.27` |
| `Live` | `Short` | `160.35` | 61,550,000.00 USD | 655.83 USD | 0.00 USD | `+63.69%` | `4.09` |
| `Live` | `Short` | `160.45` | 61,870,000.00 USD | 320,900.00 USD | 0.00 USD | `+63.79%` | `2,000.00` |
| `Live` | `Short` | `160.65` | 61,950,000.00 USD | 85,580.00 USD | 0.00 USD | `+64.00%` | `532.74` |
| `Live` | `Short` | `161.05` | 61,950,000.00 USD | 2,240.00 USD | 0.00 USD | `+64.40%` | `13.93` |
| `Live` | `Short` | `161.35` | 61,960,000.00 USD | 1,530.00 USD | 0.00 USD | `+64.71%` | `9.51` |
| `Live` | `Short` | `161.55` | 62,070,000.00 USD | 114,830.00 USD | 0.00 USD | `+64.91%` | `710.83` |
| `Live` | `Short` | `161.75` | 62,210,000.00 USD | 142,240.00 USD | 0.00 USD | `+65.12%` | `879.39` |
| `Live` | `Short` | `161.95` | 62,360,000.00 USD | 144,610.00 USD | 0.00 USD | `+65.32%` | `892.95` |
| `Live` | `Short` | `162.25` | 62,370,000.00 USD | 16,230.00 USD | 0.00 USD | `+65.63%` | `100.00` |
| `Live` | `Short` | `162.65` | 62,480,000.00 USD | 107,780.00 USD | 0.00 USD | `+66.04%` | `662.62` |
| `Live` | `Short` | `162.75` | 62,480,000.00 USD | 608.69 USD | 0.00 USD | `+66.14%` | `3.74` |
| `Live` | `Short` | `162.95` | 62,480,000.00 USD | 1,060.00 USD | 0.00 USD | `+66.34%` | `6.49` |
| `Live` | `Short` | `163.75` | 62,480,000.00 USD | 121.17 USD | 0.00 USD | `+67.16%` | `0.74` |
| `Live` | `Short` | `163.85` | 62,480,000.00 USD | 786.48 USD | 0.00 USD | `+67.26%` | `4.80` |
| `Live` | `Short` | `163.95` | 62,690,000.00 USD | 206,830.00 USD | 0.00 USD | `+67.36%` | `1,261.56` |
| `Live` | `Short` | `165.15` | 62,690,000.00 USD | 198.18 USD | 0.00 USD | `+68.59%` | `1.20` |
| `Live` | `Short` | `165.85` | 62,690,000.00 USD | 829.25 USD | 0.00 USD | `+69.30%` | `5.00` |
| `Live` | `Short` | `166.15` | 62,690,000.00 USD | 996.90 USD | 0.00 USD | `+69.61%` | `6.00` |
| `Live` | `Short` | `166.25` | 62,710,000.00 USD | 14,070.00 USD | 0.00 USD | `+69.71%` | `84.61` |
| `Live` | `Short` | `166.55` | 62,710,000.00 USD | 6,670.00 USD | 0.00 USD | `+70.02%` | `40.03` |
| `Live` | `Short` | `166.65` | 62,780,000.00 USD | 68,020.00 USD | 0.00 USD | `+70.12%` | `408.16` |
| `Live` | `Short` | `167.55` | 62,780,000.00 USD | 3,460.00 USD | 0.00 USD | `+71.04%` | `20.63` |
| `Live` | `Short` | `167.65` | 62,780,000.00 USD | 115.68 USD | 0.00 USD | `+71.14%` | `0.69` |
| `Live` | `Short` | `167.75` | 62,790,000.00 USD | 1,890.00 USD | 0.00 USD | `+71.24%` | `11.27` |
| `Live` | `Short` | `168.05` | 62,790,000.00 USD | 122.68 USD | 0.00 USD | `+71.55%` | `0.73` |
| `Live` | `Short` | `168.15` | 62,790,000.00 USD | 151.34 USD | 0.00 USD | `+71.65%` | `0.90` |
| `Live` | `Short` | `168.25` | 62,790,000.00 USD | 440.81 USD | 0.00 USD | `+71.75%` | `2.62` |
| `Live` | `Short` | `168.35` | 62,810,000.00 USD | 19,740.00 USD | 0.00 USD | `+71.86%` | `117.24` |
| `Live` | `Short` | `168.65` | 63,130,000.00 USD | 325,850.00 USD | 0.00 USD | `+72.16%` | `1,932.10` |
| `Live` | `Short` | `169.65` | 63,310,000.00 USD | 180,130.00 USD | 0.00 USD | `+73.18%` | `1,061.79` |
| `Live` | `Short` | `169.75` | 63,350,000.00 USD | 38,210.00 USD | 0.00 USD | `+73.29%` | `225.10` |
| `Live` | `Short` | `171.05` | 63,370,000.00 USD | 20,360.00 USD | 0.00 USD | `+74.61%` | `119.02` |
| `Live` | `Short` | `171.45` | 63,370,000.00 USD | 111.44 USD | 0.00 USD | `+75.02%` | `0.65` |
| `Live` | `Short` | `171.75` | 66,830,000.00 USD | 3,460,000.00 USD | 0.00 USD | `+75.33%` | `20,161.92` |
| `Live` | `Short` | `171.95` | 66,850,000.00 USD | 19,590.00 USD | 0.00 USD | `+75.53%` | `113.92` |
| `Live` | `Short` | `172.05` | 66,860,000.00 USD | 2,520.00 USD | 0.00 USD | `+75.63%` | `14.66` |
| `Live` | `Short` | `172.45` | 66,910,000.00 USD | 51,940.00 USD | 0.00 USD | `+76.04%` | `301.18` |
| `Live` | `Short` | `172.65` | 66,910,000.00 USD | 343.57 USD | 0.00 USD | `+76.25%` | `1.99` |
| `Live` | `Short` | `173.15` | 105,000,000.00 USD | 38,090,000.00 USD | 0.00 USD | `+76.76%` | `220,000.19` |
| `Live` | `Short` | `173.45` | 105,020,000.00 USD | 16,540.00 USD | 0.00 USD | `+77.06%` | `95.36` |
| `Live` | `Short` | `173.85` | 105,020,000.00 USD | 695.40 USD | 0.00 USD | `+77.47%` | `4.00` |
| `Live` | `Short` | `174.05` | 105,020,000.00 USD | 285.44 USD | 0.00 USD | `+77.67%` | `1.64` |
| `Live` | `Short` | `174.15` | 105,120,000.00 USD | 104,490.00 USD | 0.00 USD | `+77.78%` | `600.00` |
| `Live` | `Short` | `174.25` | 105,370,000.00 USD | 245,010.00 USD | 0.00 USD | `+77.88%` | `1,406.07` |
| `Live` | `Short` | `174.35` | 105,570,000.00 USD | 205,490.00 USD | 0.00 USD | `+77.98%` | `1,178.60` |
| `Live` | `Short` | `174.45` | 105,580,000.00 USD | 1,980.00 USD | 0.00 USD | `+78.08%` | `11.37` |
| `Live` | `Short` | `174.75` | 105,580,000.00 USD | 146.79 USD | 0.00 USD | `+78.39%` | `0.84` |
| `Live` | `Short` | `175.05` | 105,580,000.00 USD | 1,200.00 USD | 0.00 USD | `+78.70%` | `6.88` |
| `Live` | `Short` | `175.15` | 105,680,000.00 USD | 105,090.00 USD | 0.00 USD | `+78.80%` | `600.00` |
| `Live` | `Short` | `175.35` | 105,700,000.00 USD | 19,830.00 USD | 0.00 USD | `+79.00%` | `113.07` |
| `Live` | `Short` | `175.45` | 105,710,000.00 USD | 4,020.00 USD | 0.00 USD | `+79.10%` | `22.94` |
| `Live` | `Short` | `175.65` | 105,710,000.00 USD | 4,390.00 USD | 0.00 USD | `+79.31%` | `25.00` |
| `Live` | `Short` | `175.75` | 105,740,000.00 USD | 25,680.00 USD | 0.00 USD | `+79.41%` | `146.10` |
| `Live` | `Short` | `176.25` | 105,740,000.00 USD | 625.69 USD | 0.00 USD | `+79.92%` | `3.55` |
| `Live` | `Short` | `176.55` | 105,880,000.00 USD | 141,240.00 USD | 0.00 USD | `+80.23%` | `800.00` |
| `Live` | `Short` | `177.45` | 105,930,000.00 USD | 47,190.00 USD | 0.00 USD | `+81.15%` | `265.94` |
| `Live` | `Short` | `177.55` | 106,960,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+81.25%` | `5,800.00` |
| `Live` | `Short` | `177.65` | 106,960,000.00 USD | 637.76 USD | 0.00 USD | `+81.35%` | `3.59` |
| `Live` | `Short` | `177.85` | 106,960,000.00 USD | 4,930.00 USD | 0.00 USD | `+81.55%` | `27.73` |
| `Live` | `Short` | `177.95` | 107,040,000.00 USD | 78,300.00 USD | 0.00 USD | `+81.66%` | `440.00` |
| `Live` | `Short` | `178.05` | 107,310,000.00 USD | 267,070.00 USD | 0.00 USD | `+81.76%` | `1,500.00` |
| `Live` | `Short` | `178.55` | 107,510,000.00 USD | 206,920.00 USD | 0.00 USD | `+82.27%` | `1,158.88` |
| `Live` | `Short` | `179.55` | 107,520,000.00 USD | 9,290.00 USD | 0.00 USD | `+83.29%` | `51.72` |
| `Live` | `Short` | `179.95` | 111,120,000.00 USD | 3,600,000.00 USD | 0.00 USD | `+83.70%` | `20,000.00` |
| `Live` | `Short` | `180.15` | 111,120,000.00 USD | 2,030.00 USD | 0.00 USD | `+83.90%` | `11.27` |
| `Live` | `Short` | `180.25` | 111,130,000.00 USD | 1,360.00 USD | 0.00 USD | `+84.00%` | `7.52` |
| `Live` | `Short` | `180.55` | 111,160,000.00 USD | 38,150.00 USD | 0.00 USD | `+84.31%` | `211.32` |
| `Live` | `Short` | `181.05` | 111,160,000.00 USD | 780.33 USD | 0.00 USD | `+84.82%` | `4.31` |
| `Live` | `Short` | `181.25` | 111,180,000.00 USD | 18,120.00 USD | 0.00 USD | `+85.02%` | `100.00` |
| `Live` | `Short` | `181.55` | 111,180,000.00 USD | 254.17 USD | 0.00 USD | `+85.33%` | `1.40` |
| `Live` | `Short` | `182.15` | 111,190,000.00 USD | 3,990.00 USD | 0.00 USD | `+85.94%` | `21.93` |
| `Live` | `Short` | `183.85` | 111,240,000.00 USD | 52,820.00 USD | 0.00 USD | `+87.68%` | `287.30` |
| `Live` | `Short` | `184.25` | 111,240,000.00 USD | 1,680.00 USD | 0.00 USD | `+88.09%` | `9.12` |
| `Live` | `Short` | `184.65` | 111,250,000.00 USD | 7,650.00 USD | 0.00 USD | `+88.50%` | `41.43` |
| `Live` | `Short` | `184.95` | 111,420,000.00 USD | 176,140.00 USD | 0.00 USD | `+88.80%` | `952.35` |
| `Live` | `Short` | `185.15` | 112,800,000.00 USD | 1,370,000.00 USD | 0.00 USD | `+89.01%` | `7,413.68` |
| `Live` | `Short` | `185.25` | 112,800,000.00 USD | 737.29 USD | 0.00 USD | `+89.11%` | `3.98` |
| `Live` | `Short` | `185.45` | 112,800,000.00 USD | 2,770.00 USD | 0.00 USD | `+89.31%` | `14.94` |
| `Live` | `Short` | `185.55` | 112,800,000.00 USD | 1,220.00 USD | 0.00 USD | `+89.41%` | `6.56` |
| `Live` | `Short` | `185.65` | 112,800,000.00 USD | 137.38 USD | 0.00 USD | `+89.52%` | `0.74` |
| `Live` | `Short` | `186.15` | 112,800,000.00 USD | 247.58 USD | 0.00 USD | `+90.03%` | `1.33` |
| `Live` | `Short` | `186.45` | 112,810,000.00 USD | 2,440.00 USD | 0.00 USD | `+90.33%` | `13.11` |
| `Live` | `Short` | `186.75` | 112,810,000.00 USD | 2,800.00 USD | 0.00 USD | `+90.64%` | `15.00` |
| `Live` | `Short` | `186.85` | 112,810,000.00 USD | 2,190.00 USD | 0.00 USD | `+90.74%` | `11.72` |
| `Live` | `Short` | `187.45` | 112,810,000.00 USD | 232.44 USD | 0.00 USD | `+91.35%` | `1.24` |
| `Live` | `Short` | `187.85` | 112,810,000.00 USD | 1,560.00 USD | 0.00 USD | `+91.76%` | `8.32` |
| `Live` | `Short` | `188.55` | 112,810,000.00 USD | 231.92 USD | 0.00 USD | `+92.48%` | `1.23` |
| `Live` | `Short` | `188.65` | 112,840,000.00 USD | 29,110.00 USD | 0.00 USD | `+92.58%` | `154.32` |
| `Live` | `Short` | `188.75` | 112,850,000.00 USD | 4,070.00 USD | 0.00 USD | `+92.68%` | `21.57` |
| `Live` | `Short` | `188.95` | 112,850,000.00 USD | 1,450.00 USD | 0.00 USD | `+92.88%` | `7.69` |
| `Live` | `Short` | `189.25` | 112,850,000.00 USD | 456.09 USD | 0.00 USD | `+93.19%` | `2.41` |
| `Live` | `Short` | `189.55` | 112,850,000.00 USD | 1,000.00 USD | 0.00 USD | `+93.50%` | `5.30` |
| `Live` | `Short` | `189.85` | 112,850,000.00 USD | 307.56 USD | 0.00 USD | `+93.80%` | `1.62` |
| `Live` | `Short` | `189.95` | 113,130,000.00 USD | 284,930.00 USD | 0.00 USD | `+93.91%` | `1,500.00` |
| `Live` | `Short` | `190.05` | 113,520,000.00 USD | 385,490.00 USD | 0.00 USD | `+94.01%` | `2,028.34` |
| `Live` | `Short` | `190.15` | 113,520,000.00 USD | 148.32 USD | 0.00 USD | `+94.11%` | `0.78` |
| `Live` | `Short` | `190.45` | 113,520,000.00 USD | 620.87 USD | 0.00 USD | `+94.42%` | `3.26` |
| `Live` | `Short` | `190.95` | 127,090,000.00 USD | 13,570,000.00 USD | 0.00 USD | `+94.93%` | `71,044.42` |
| `Live` | `Short` | `191.15` | 127,150,000.00 USD | 62,720.00 USD | 0.00 USD | `+95.13%` | `328.11` |
| `Live` | `Short` | `191.95` | 127,150,000.00 USD | 322.48 USD | 0.00 USD | `+95.95%` | `1.68` |
| `Live` | `Short` | `192.15` | 127,150,000.00 USD | 3,290.00 USD | 0.00 USD | `+96.15%` | `17.13` |
| `Live` | `Short` | `192.95` | 127,150,000.00 USD | 192.95 USD | 0.00 USD | `+96.97%` | `1.00` |
| `Live` | `Short` | `193.15` | 127,150,000.00 USD | 2,170.00 USD | 0.00 USD | `+97.17%` | `11.24` |
| `Live` | `Short` | `193.55` | 127,270,000.00 USD | 114,580.00 USD | 0.00 USD | `+97.58%` | `592.00` |
| `Live` | `Short` | `194.05` | 127,270,000.00 USD | 543.34 USD | 0.00 USD | `+98.09%` | `2.80` |
| `Live` | `Short` | `194.35` | 127,280,000.00 USD | 9,380.00 USD | 0.00 USD | `+98.40%` | `48.28` |
| `Live` | `Short` | `194.55` | 127,370,000.00 USD | 89,060.00 USD | 0.00 USD | `+98.60%` | `457.80` |
| `Live` | `Short` | `194.75` | 127,370,000.00 USD | 266.81 USD | 0.00 USD | `+98.81%` | `1.37` |
| `Live` | `Short` | `194.95` | 127,390,000.00 USD | 20,000.00 USD | 0.00 USD | `+99.01%` | `102.58` |
| `Live` | `Short` | `195.25` | 127,410,000.00 USD | 18,480.00 USD | 0.00 USD | `+99.32%` | `94.66` |
| `Live` | `Short` | `195.35` | 127,430,000.00 USD | 27,160.00 USD | 0.00 USD | `+99.42%` | `139.03` |
| `Live` | `Short` | `195.65` | 127,580,000.00 USD | 142,140.00 USD | 0.00 USD | `+99.72%` | `726.51` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.05` | 10,860,000.00 USD | 0.00 USD | 14,030.00 USD | `-76.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.35` | 10,850,000.00 USD | 0.00 USD | 499.56 USD | `-69.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `32.05` | 10,850,000.00 USD | 0.00 USD | 1,230.00 USD | `-67.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.05` | 10,850,000.00 USD | 0.00 USD | 818.32 USD | `-66.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.85` | 10,850,000.00 USD | 0.00 USD | 1,340.00 USD | `-64.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 10,850,000.00 USD | 0.00 USD | 2,160.00 USD | `-63.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.45` | 10,840,000.00 USD | 0.00 USD | 434.85 USD | `-62.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.05` | 10,840,000.00 USD | 0.00 USD | 267.87 USD | `-61.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.55` | 10,840,000.00 USD | 0.00 USD | 3,460.00 USD | `-59.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.75` | 10,840,000.00 USD | 0.00 USD | 157.01 USD | `-59.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 10,840,000.00 USD | 0.00 USD | 1,050.00 USD | `-59.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.75` | 10,840,000.00 USD | 0.00 USD | 120.66 USD | `-57.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.15` | 10,840,000.00 USD | 0.00 USD | 121.81 USD | `-56.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.55` | 10,840,000.00 USD | 0.00 USD | 170,530.00 USD | `-56.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.75` | 10,670,000.00 USD | 0.00 USD | 105.00 USD | `-55.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 10,670,000.00 USD | 0.00 USD | 64,240.00 USD | `-54.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.75` | 10,600,000.00 USD | 0.00 USD | 251.05 USD | `-52.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.75` | 10,600,000.00 USD | 0.00 USD | 143.25 USD | `-51.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.85` | 10,600,000.00 USD | 0.00 USD | 191.40 USD | `-51.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 10,600,000.00 USD | 0.00 USD | 50,240.00 USD | `-50.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.55` | 10,550,000.00 USD | 0.00 USD | 664.65 USD | `-50.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.75` | 10,550,000.00 USD | 0.00 USD | 103.35 USD | `-50.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 10,550,000.00 USD | 0.00 USD | 4,660.00 USD | `-48.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.25` | 10,550,000.00 USD | 0.00 USD | 107.03 USD | `-48.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 10,550,000.00 USD | 0.00 USD | 102.62 USD | `-48.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.25` | 10,550,000.00 USD | 0.00 USD | 134.28 USD | `-47.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 10,550,000.00 USD | 0.00 USD | 3,950.00 USD | `-47.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.15` | 10,540,000.00 USD | 0.00 USD | 102.74 USD | `-46.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 10,540,000.00 USD | 0.00 USD | 126.12 USD | `-46.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 10,540,000.00 USD | 0.00 USD | 200.15 USD | `-45.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 10,540,000.00 USD | 0.00 USD | 24,450.00 USD | `-45.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 10,520,000.00 USD | 0.00 USD | 1,660.00 USD | `-45.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 10,520,000.00 USD | 0.00 USD | 641.57 USD | `-44.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 10,520,000.00 USD | 0.00 USD | 139.87 USD | `-44.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 10,520,000.00 USD | 0.00 USD | 209.19 USD | `-43.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 10,510,000.00 USD | 0.00 USD | 4,350.00 USD | `-42.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 10,510,000.00 USD | 0.00 USD | 894.56 USD | `-42.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 10,510,000.00 USD | 0.00 USD | 4,930.00 USD | `-42.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 10,500,000.00 USD | 0.00 USD | 6,790.00 USD | `-41.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.35` | 10,500,000.00 USD | 0.00 USD | 265.53 USD | `-41.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.95` | 10,500,000.00 USD | 0.00 USD | 268.31 USD | `-40.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.05` | 10,500,000.00 USD | 0.00 USD | 158.48 USD | `-40.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.15` | 10,500,000.00 USD | 0.00 USD | 3,820.00 USD | `-40.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.25` | 10,490,000.00 USD | 0.00 USD | 428.72 USD | `-40.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.05` | 10,490,000.00 USD | 0.00 USD | 295.25 USD | `-39.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.35` | 10,490,000.00 USD | 0.00 USD | 200.01 USD | `-39.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.55` | 10,490,000.00 USD | 0.00 USD | 1,460.00 USD | `-39.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.95` | 10,490,000.00 USD | 0.00 USD | 9,040.00 USD | `-38.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.05` | 10,480,000.00 USD | 0.00 USD | 35,050.00 USD | `-38.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.15` | 10,450,000.00 USD | 0.00 USD | 2,820.00 USD | `-38.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.25` | 10,440,000.00 USD | 0.00 USD | 488.63 USD | `-38.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.35` | 10,440,000.00 USD | 0.00 USD | 258.90 USD | `-38.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.45` | 10,440,000.00 USD | 0.00 USD | 206.13 USD | `-38.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.55` | 10,440,000.00 USD | 0.00 USD | 724.78 USD | `-38.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.05` | 10,440,000.00 USD | 0.00 USD | 14,350.00 USD | `-37.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.35` | 10,430,000.00 USD | 0.00 USD | 142.33 USD | `-37.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.45` | 10,430,000.00 USD | 0.00 USD | 100.78 USD | `-37.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.55` | 10,430,000.00 USD | 0.00 USD | 243.74 USD | `-37.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.05` | 10,430,000.00 USD | 0.00 USD | 6,720.00 USD | `-36.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.55` | 10,420,000.00 USD | 0.00 USD | 136.98 USD | `-36.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.05` | 10,420,000.00 USD | 0.00 USD | 9,990.00 USD | `-35.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.55` | 10,410,000.00 USD | 0.00 USD | 2,980.00 USD | `-35.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.95` | 10,410,000.00 USD | 0.00 USD | 222.55 USD | `-34.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.25` | 10,410,000.00 USD | 0.00 USD | 163.19 USD | `-34.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.85` | 10,410,000.00 USD | 0.00 USD | 129.70 USD | `-33.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.05` | 10,410,000.00 USD | 0.00 USD | 2,440.00 USD | `-33.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.15` | 10,400,000.00 USD | 0.00 USD | 2,190.00 USD | `-33.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.55` | 10,400,000.00 USD | 0.00 USD | 2,200.00 USD | `-33.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.05` | 10,400,000.00 USD | 0.00 USD | 7,100.00 USD | `-32.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.55` | 10,390,000.00 USD | 0.00 USD | 541.72 USD | `-32.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.05` | 10,390,000.00 USD | 0.00 USD | 335.25 USD | `-31.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.15` | 10,390,000.00 USD | 0.00 USD | 268.60 USD | `-31.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.05` | 10,390,000.00 USD | 0.00 USD | 195.30 USD | `-30.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.45` | 10,390,000.00 USD | 0.00 USD | 7,600.00 USD | `-30.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.55` | 10,380,000.00 USD | 0.00 USD | 5,610.00 USD | `-30.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.65` | 10,380,000.00 USD | 0.00 USD | 359.04 USD | `-29.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.75` | 10,380,000.00 USD | 0.00 USD | 1,200.00 USD | `-29.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.05` | 10,380,000.00 USD | 0.00 USD | 11,360.00 USD | `-29.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.15` | 10,370,000.00 USD | 0.00 USD | 172.18 USD | `-29.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.25` | 10,370,000.00 USD | 0.00 USD | 668.96 USD | `-29.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.65` | 10,370,000.00 USD | 0.00 USD | 107.96 USD | `-28.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.75` | 10,360,000.00 USD | 0.00 USD | 42,360.00 USD | `-28.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.85` | 10,320,000.00 USD | 0.00 USD | 365.32 USD | `-28.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.95` | 10,320,000.00 USD | 0.00 USD | 1,510.00 USD | `-28.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.05` | 10,320,000.00 USD | 0.00 USD | 43,920.00 USD | `-28.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.25` | 10,280,000.00 USD | 0.00 USD | 5,270.00 USD | `-28.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.35` | 10,270,000.00 USD | 0.00 USD | 562.80 USD | `-28.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.55` | 10,270,000.00 USD | 0.00 USD | 681.51 USD | `-27.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.65` | 10,270,000.00 USD | 0.00 USD | 4,920.00 USD | `-27.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.75` | 10,270,000.00 USD | 0.00 USD | 2,790.00 USD | `-27.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.05` | 10,260,000.00 USD | 0.00 USD | 265.02 USD | `-27.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.35` | 10,260,000.00 USD | 0.00 USD | 32,450.00 USD | `-27.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.45` | 10,230,000.00 USD | 0.00 USD | 289.37 USD | `-27.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.55` | 10,230,000.00 USD | 0.00 USD | 1,170.00 USD | `-26.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.65` | 10,230,000.00 USD | 0.00 USD | 1,930.00 USD | `-26.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.75` | 10,230,000.00 USD | 0.00 USD | 235.34 USD | `-26.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.05` | 10,230,000.00 USD | 0.00 USD | 20,410.00 USD | `-26.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.55` | 10,210,000.00 USD | 0.00 USD | 19,560.00 USD | `-25.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.65` | 10,190,000.00 USD | 0.00 USD | 14,530.00 USD | `-25.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.95` | 10,170,000.00 USD | 0.00 USD | 66,160.00 USD | `-25.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.05` | 10,110,000.00 USD | 0.00 USD | 7,970.00 USD | `-25.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.35` | 10,100,000.00 USD | 0.00 USD | 733.50 USD | `-25.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.45` | 10,100,000.00 USD | 0.00 USD | 139.56 USD | `-25.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.05` | 10,100,000.00 USD | 0.00 USD | 510.95 USD | `-24.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.25` | 10,100,000.00 USD | 0.00 USD | 414.31 USD | `-24.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.35` | 10,100,000.00 USD | 0.00 USD | 1,660.00 USD | `-24.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.45` | 10,090,000.00 USD | 0.00 USD | 10,730.00 USD | `-24.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.55` | 10,080,000.00 USD | 0.00 USD | 331.00 USD | `-23.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.75` | 10,080,000.00 USD | 0.00 USD | 28,050.00 USD | `-23.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.05` | 10,060,000.00 USD | 0.00 USD | 30,040.00 USD | `-23.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.35` | 10,030,000.00 USD | 0.00 USD | 153.71 USD | `-23.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.45` | 10,020,000.00 USD | 0.00 USD | 163.73 USD | `-22.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.75` | 10,020,000.00 USD | 0.00 USD | 2,220.00 USD | `-22.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.95` | 10,020,000.00 USD | 0.00 USD | 277.98 USD | `-22.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.05` | 10,020,000.00 USD | 0.00 USD | 8,680.00 USD | `-22.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.15` | 10,010,000.00 USD | 0.00 USD | 254.34 USD | `-22.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.25` | 10,010,000.00 USD | 0.00 USD | 486.47 USD | `-22.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.35` | 10,010,000.00 USD | 0.00 USD | 358.84 USD | `-22.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.55` | 10,010,000.00 USD | 0.00 USD | 4,340.00 USD | `-21.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.65` | 10,010,000.00 USD | 0.00 USD | 536.55 USD | `-21.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.75` | 10,010,000.00 USD | 0.00 USD | 251.74 USD | `-21.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.05` | 10,010,000.00 USD | 0.00 USD | 2,160.00 USD | `-21.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.35` | 10,010,000.00 USD | 0.00 USD | 5,690.00 USD | `-21.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.45` | 10,000,000.00 USD | 0.00 USD | 1,020.00 USD | `-20.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.95` | 10,000,000.00 USD | 0.00 USD | 155.12 USD | `-20.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.05` | 10,000,000.00 USD | 0.00 USD | 56,850.00 USD | `-20.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.15` | 9,940,000.00 USD | 0.00 USD | 738.52 USD | `-20.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.55` | 9,940,000.00 USD | 0.00 USD | 18,590.00 USD | `-19.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.65` | 9,920,000.00 USD | 0.00 USD | 116.40 USD | `-19.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.75` | 9,920,000.00 USD | 0.00 USD | 379.58 USD | `-19.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.05` | 9,920,000.00 USD | 0.00 USD | 5,300.00 USD | `-19.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.15` | 9,920,000.00 USD | 0.00 USD | 201.04 USD | `-19.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.25` | 9,920,000.00 USD | 0.00 USD | 2,140.00 USD | `-19.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.45` | 9,910,000.00 USD | 0.00 USD | 5,850.00 USD | `-18.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.65` | 9,910,000.00 USD | 0.00 USD | 238.95 USD | `-18.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.75` | 9,910,000.00 USD | 0.00 USD | 1,330.00 USD | `-18.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.85` | 9,910,000.00 USD | 0.00 USD | 289.06 USD | `-18.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.95` | 9,910,000.00 USD | 0.00 USD | 808.29 USD | `-18.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.05` | 9,910,000.00 USD | 0.00 USD | 39,530.00 USD | `-18.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.15` | 9,870,000.00 USD | 0.00 USD | 8,360.00 USD | `-18.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.35` | 9,860,000.00 USD | 0.00 USD | 359.97 USD | `-17.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.45` | 9,860,000.00 USD | 0.00 USD | 8,770.00 USD | `-17.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.55` | 9,850,000.00 USD | 0.00 USD | 1,280.00 USD | `-17.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.65` | 9,850,000.00 USD | 0.00 USD | 1,280.00 USD | `-17.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.75` | 9,850,000.00 USD | 0.00 USD | 22,780.00 USD | `-17.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.85` | 9,820,000.00 USD | 0.00 USD | 341.19 USD | `-17.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.05` | 9,820,000.00 USD | 0.00 USD | 1,620.00 USD | `-17.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.25` | 9,820,000.00 USD | 0.00 USD | 266.50 USD | `-17.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.45` | 9,820,000.00 USD | 0.00 USD | 5,830.00 USD | `-16.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.55` | 9,820,000.00 USD | 0.00 USD | 572.48 USD | `-16.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.65` | 9,810,000.00 USD | 0.00 USD | 806.70 USD | `-16.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.75` | 9,810,000.00 USD | 0.00 USD | 1,390.00 USD | `-16.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.85` | 9,810,000.00 USD | 0.00 USD | 818.50 USD | `-16.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.95` | 9,810,000.00 USD | 0.00 USD | 70,900.00 USD | `-16.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.05` | 9,740,000.00 USD | 0.00 USD | 3,220.00 USD | `-16.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.15` | 9,740,000.00 USD | 0.00 USD | 684.31 USD | `-16.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.25` | 9,740,000.00 USD | 0.00 USD | 486.92 USD | `-16.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.35` | 9,740,000.00 USD | 0.00 USD | 386.22 USD | `-15.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.45` | 9,740,000.00 USD | 0.00 USD | 1,570.00 USD | `-15.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.65` | 9,730,000.00 USD | 0.00 USD | 267,390.00 USD | `-15.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.75` | 9,470,000.00 USD | 0.00 USD | 1,660.00 USD | `-15.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.85` | 9,470,000.00 USD | 0.00 USD | 3,270.00 USD | `-15.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.95` | 9,460,000.00 USD | 0.00 USD | 945.63 USD | `-15.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.05` | 9,460,000.00 USD | 0.00 USD | 6,420.00 USD | `-15.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.15` | 9,450,000.00 USD | 0.00 USD | 239.47 USD | `-15.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.25` | 9,450,000.00 USD | 0.00 USD | 18,630.00 USD | `-15.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.45` | 9,440,000.00 USD | 0.00 USD | 1,500.00 USD | `-14.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.55` | 9,430,000.00 USD | 0.00 USD | 831,290.00 USD | `-14.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.65` | 8,600,000.00 USD | 0.00 USD | 1,100.00 USD | `-14.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.75` | 8,600,000.00 USD | 0.00 USD | 1,320.00 USD | `-14.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.95` | 8,600,000.00 USD | 0.00 USD | 4,550.00 USD | `-14.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.05` | 8,600,000.00 USD | 0.00 USD | 40,720.00 USD | `-14.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.15` | 8,560,000.00 USD | 0.00 USD | 25,220.00 USD | `-14.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.25` | 8,530,000.00 USD | 0.00 USD | 2,690.00 USD | `-14.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.45` | 8,530,000.00 USD | 0.00 USD | 965.26 USD | `-13.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.55` | 8,530,000.00 USD | 0.00 USD | 169.95 USD | `-13.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.65` | 8,530,000.00 USD | 0.00 USD | 858.35 USD | `-13.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.75` | 8,530,000.00 USD | 0.00 USD | 306.80 USD | `-13.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.95` | 8,520,000.00 USD | 0.00 USD | 137.62 USD | `-13.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.05` | 8,520,000.00 USD | 0.00 USD | 233,610.00 USD | `-13.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.15` | 8,290,000.00 USD | 0.00 USD | 1,290.00 USD | `-13.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.25` | 8,290,000.00 USD | 0.00 USD | 1,320.00 USD | `-12.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.35` | 8,290,000.00 USD | 0.00 USD | 39,110.00 USD | `-12.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.45` | 8,250,000.00 USD | 0.00 USD | 120.48 USD | `-12.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.55` | 8,250,000.00 USD | 0.00 USD | 105.23 USD | `-12.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.65` | 8,250,000.00 USD | 0.00 USD | 310.05 USD | `-12.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.75` | 8,250,000.00 USD | 0.00 USD | 1,410.00 USD | `-12.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.85` | 8,250,000.00 USD | 0.00 USD | 360.57 USD | `-12.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.95` | 8,250,000.00 USD | 0.00 USD | 2,050.00 USD | `-12.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.05` | 8,250,000.00 USD | 0.00 USD | 10,250.00 USD | `-12.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.15` | 8,230,000.00 USD | 0.00 USD | 2,210.00 USD | `-12.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.25` | 8,230,000.00 USD | 0.00 USD | 163.88 USD | `-11.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.35` | 8,230,000.00 USD | 0.00 USD | 4,080.00 USD | `-11.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.45` | 8,230,000.00 USD | 0.00 USD | 2,790.00 USD | `-11.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.55` | 8,230,000.00 USD | 0.00 USD | 417.17 USD | `-11.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.65` | 8,230,000.00 USD | 0.00 USD | 220,550.00 USD | `-11.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.75` | 8,000,000.00 USD | 0.00 USD | 3,060.00 USD | `-11.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.85` | 8,000,000.00 USD | 0.00 USD | 788.60 USD | `-11.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.95` | 8,000,000.00 USD | 0.00 USD | 132.16 USD | `-11.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.05` | 8,000,000.00 USD | 0.00 USD | 280,590.00 USD | `-11.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.15` | 7,720,000.00 USD | 0.00 USD | 23,550.00 USD | `-11.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.25` | 7,700,000.00 USD | 0.00 USD | 8,200.00 USD | `-10.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.35` | 7,690,000.00 USD | 0.00 USD | 102.20 USD | `-10.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.45` | 7,690,000.00 USD | 0.00 USD | 730.21 USD | `-10.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.55` | 7,690,000.00 USD | 0.00 USD | 7,840.00 USD | `-10.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.65` | 7,680,000.00 USD | 0.00 USD | 2,300.00 USD | `-10.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.85` | 7,680,000.00 USD | 0.00 USD | 131.78 USD | `-10.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.95` | 7,680,000.00 USD | 0.00 USD | 177.66 USD | `-10.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.05` | 7,680,000.00 USD | 0.00 USD | 147,990.00 USD | `-10.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.15` | 7,530,000.00 USD | 0.00 USD | 2,470.00 USD | `-10.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.25` | 7,530,000.00 USD | 0.00 USD | 1,870.00 USD | `-9.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.35` | 7,520,000.00 USD | 0.00 USD | 38,020.00 USD | `-9.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.45` | 7,490,000.00 USD | 0.00 USD | 867.69 USD | `-9.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.55` | 7,490,000.00 USD | 0.00 USD | 32,280.00 USD | `-9.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.65` | 7,450,000.00 USD | 0.00 USD | 27,220.00 USD | `-9.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.75` | 7,430,000.00 USD | 0.00 USD | 53,390.00 USD | `-9.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.85` | 7,370,000.00 USD | 0.00 USD | 91,430.00 USD | `-9.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.95` | 7,280,000.00 USD | 0.00 USD | 141.43 USD | `-9.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.05` | 7,280,000.00 USD | 0.00 USD | 16,600.00 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.15` | 7,260,000.00 USD | 0.00 USD | 6,470.00 USD | `-8.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.25` | 7,260,000.00 USD | 0.00 USD | 1,340.00 USD | `-8.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.35` | 7,260,000.00 USD | 0.00 USD | 4,360.00 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.45` | 7,250,000.00 USD | 0.00 USD | 5,280.00 USD | `-8.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.55` | 7,250,000.00 USD | 0.00 USD | 644.76 USD | `-8.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.65` | 7,250,000.00 USD | 0.00 USD | 297.64 USD | `-8.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.75` | 7,250,000.00 USD | 0.00 USD | 105.01 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.85` | 7,250,000.00 USD | 0.00 USD | 17,170.00 USD | `-8.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.95` | 7,230,000.00 USD | 0.00 USD | 87,890.00 USD | `-8.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.05` | 7,140,000.00 USD | 0.00 USD | 2,360,000.00 USD | `-8.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.15` | 4,780,000.00 USD | 0.00 USD | 1,250.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.25` | 4,780,000.00 USD | 0.00 USD | 12,170.00 USD | `-7.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.35` | 4,770,000.00 USD | 0.00 USD | 106,890.00 USD | `-7.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.45` | 4,660,000.00 USD | 0.00 USD | 5,010.00 USD | `-7.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.55` | 4,660,000.00 USD | 0.00 USD | 13,500.00 USD | `-7.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.65` | 4,640,000.00 USD | 0.00 USD | 529,070.00 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.75` | 4,110,000.00 USD | 0.00 USD | 4,980.00 USD | `-7.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.85` | 4,110,000.00 USD | 0.00 USD | 6,580.00 USD | `-7.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.95` | 4,100,000.00 USD | 0.00 USD | 13,150.00 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.05` | 4,090,000.00 USD | 0.00 USD | 660,450.00 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.15` | 3,430,000.00 USD | 0.00 USD | 1,240.00 USD | `-6.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.25` | 3,430,000.00 USD | 0.00 USD | 154,330.00 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.35` | 3,270,000.00 USD | 0.00 USD | 16,770.00 USD | `-6.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.45` | 3,260,000.00 USD | 0.00 USD | 920.90 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.55` | 3,260,000.00 USD | 0.00 USD | 20,410.00 USD | `-6.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.65` | 3,240,000.00 USD | 0.00 USD | 44,680.00 USD | `-6.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.75` | 3,190,000.00 USD | 0.00 USD | 21,870.00 USD | `-6.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.85` | 3,170,000.00 USD | 0.00 USD | 46,310.00 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.95` | 3,120,000.00 USD | 0.00 USD | 33,290.00 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.05` | 3,090,000.00 USD | 0.00 USD | 271,920.00 USD | `-6.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.15` | 2,820,000.00 USD | 0.00 USD | 52,810.00 USD | `-5.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.25` | 2,760,000.00 USD | 0.00 USD | 5,610.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.35` | 2,760,000.00 USD | 0.00 USD | 911,190.00 USD | `-5.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.45` | 1,850,000.00 USD | 0.00 USD | 11,060.00 USD | `-5.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.55` | 1,840,000.00 USD | 0.00 USD | 17,280.00 USD | `-5.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.65` | 1,820,000.00 USD | 0.00 USD | 45,060.00 USD | `-5.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.75` | 1,770,000.00 USD | 0.00 USD | 2,020.00 USD | `-5.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.85` | 1,770,000.00 USD | 0.00 USD | 32,500.00 USD | `-5.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.95` | 1,740,000.00 USD | 0.00 USD | 14,800.00 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.05` | 1,730,000.00 USD | 0.00 USD | 30,900.00 USD | `-5.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.15` | 1,690,000.00 USD | 0.00 USD | 133,950.00 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.25` | 1,560,000.00 USD | 0.00 USD | 3,900.00 USD | `-4.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.35` | 1,560,000.00 USD | 0.00 USD | 385.54 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.45` | 1,560,000.00 USD | 0.00 USD | 1,380.00 USD | `-4.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.55` | 1,550,000.00 USD | 0.00 USD | 1,120.00 USD | `-4.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.65` | 1,550,000.00 USD | 0.00 USD | 4,050.00 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.75` | 1,550,000.00 USD | 0.00 USD | 255.94 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.85` | 1,550,000.00 USD | 0.00 USD | 479.57 USD | `-4.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.95` | 1,550,000.00 USD | 0.00 USD | 3,680.00 USD | `-4.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.05` | 1,550,000.00 USD | 0.00 USD | 27,580.00 USD | `-3.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.15` | 1,520,000.00 USD | 0.00 USD | 15,780.00 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.25` | 1,500,000.00 USD | 0.00 USD | 7,170.00 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.35` | 1,490,000.00 USD | 0.00 USD | 12,280.00 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.45` | 1,480,000.00 USD | 0.00 USD | 251.24 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.55` | 1,480,000.00 USD | 0.00 USD | 91,930.00 USD | `-3.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.65` | 1,390,000.00 USD | 0.00 USD | 16,810.00 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.75` | 1,370,000.00 USD | 0.00 USD | 28,250.00 USD | `-3.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.85` | 1,350,000.00 USD | 0.00 USD | 12,830.00 USD | `-3.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.95` | 1,330,000.00 USD | 0.00 USD | 3,800.00 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.05` | 1,330,000.00 USD | 0.00 USD | 33,630.00 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.15` | 1,290,000.00 USD | 0.00 USD | 62,080.00 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.25` | 1,230,000.00 USD | 0.00 USD | 6,890.00 USD | `-2.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.35` | 1,230,000.00 USD | 0.00 USD | 11,640.00 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.45` | 1,210,000.00 USD | 0.00 USD | 199,040.00 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.55` | 1,020,000.00 USD | 0.00 USD | 158,590.00 USD | `-2.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.65` | 856,720.00 USD | 0.00 USD | 2,460.00 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.75` | 854,260.00 USD | 0.00 USD | 60,600.00 USD | `-2.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.85` | 793,670.00 USD | 0.00 USD | 28,740.00 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.95` | 764,930.00 USD | 0.00 USD | 29,710.00 USD | `-2.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.05` | 735,220.00 USD | 0.00 USD | 24,280.00 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.15` | 710,950.00 USD | 0.00 USD | 18,010.00 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.25` | 692,930.00 USD | 0.00 USD | 13,060.00 USD | `-1.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.35` | 679,870.00 USD | 0.00 USD | 60,470.00 USD | `-1.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.45` | 619,400.00 USD | 0.00 USD | 379.05 USD | `-1.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.55` | 619,020.00 USD | 0.00 USD | 4,670.00 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.65` | 614,360.00 USD | 0.00 USD | 53,050.00 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.75` | 561,310.00 USD | 0.00 USD | 353,520.00 USD | `-1.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.85` | 207,790.00 USD | 0.00 USD | 7,830.00 USD | `-1.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.95` | 199,960.00 USD | 0.00 USD | 21,960.00 USD | `-1.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.05` | 178,000.00 USD | 0.00 USD | 69,000.00 USD | `-0.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.15` | 108,990.00 USD | 0.00 USD | 6,080.00 USD | `-0.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.25` | 102,910.00 USD | 0.00 USD | 12,350.00 USD | `-0.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.35` | 90,560.00 USD | 0.00 USD | 8,150.00 USD | `-0.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.45` | 82,410.00 USD | 0.00 USD | 24,400.00 USD | `-0.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.55` | 58,010.00 USD | 0.00 USD | 12,870.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.65` | 45,140.00 USD | 0.00 USD | 16,770.00 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.75` | 28,370.00 USD | 0.00 USD | 25,360.00 USD | `-0.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.85` | 3,010.00 USD | 0.00 USD | 2,010.00 USD | `-0.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.95` | 996.15 USD | 0.00 USD | 996.15 USD | `-0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 459,820.00 USD | 459,820.00 USD | 0.00 USD | `+0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.15` | 461,080.00 USD | 1,260.00 USD | 0.00 USD | `+0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.25` | 462,170.00 USD | 1,090.00 USD | 0.00 USD | `+0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.35` | 467,090.00 USD | 4,920.00 USD | 0.00 USD | `+0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.45` | 475,980.00 USD | 8,900.00 USD | 0.00 USD | `+0.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.55` | 477,070.00 USD | 1,090.00 USD | 0.00 USD | `+0.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.65` | 624,710.00 USD | 147,640.00 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.75` | 1,000,000.00 USD | 377,830.00 USD | 0.00 USD | `+0.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.85` | 1,010,000.00 USD | 5,190.00 USD | 0.00 USD | `+0.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.95` | 1,010,000.00 USD | 4,980.00 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,040,000.00 USD | 32,280.00 USD | 0.00 USD | `+1.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.15` | 1,100,000.00 USD | 56,030.00 USD | 0.00 USD | `+1.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.25` | 1,100,000.00 USD | 301.72 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.35` | 1,130,000.00 USD | 28,680.00 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.45` | 1,230,000.00 USD | 103,130.00 USD | 0.00 USD | `+1.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.55` | 1,370,000.00 USD | 134,670.00 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.65` | 1,380,000.00 USD | 13,860.00 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.75` | 1,390,000.00 USD | 5,200.00 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.85` | 1,390,000.00 USD | 4,740.00 USD | 0.00 USD | `+1.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.95` | 1,440,000.00 USD | 45,470.00 USD | 0.00 USD | `+2.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 2,700,000.00 USD | 1,260,000.00 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.15` | 2,720,000.00 USD | 15,740.00 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.25` | 2,720,000.00 USD | 5,120.00 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.35` | 2,720,000.00 USD | 144.50 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.45` | 2,730,000.00 USD | 9,100.00 USD | 0.00 USD | `+2.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.55` | 2,730,000.00 USD | 2,490.00 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.65` | 2,780,000.00 USD | 49,870.00 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.75` | 2,780,000.00 USD | 826.15 USD | 0.00 USD | `+2.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.85` | 2,810,000.00 USD | 27,150.00 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.95` | 2,840,000.00 USD | 31,470.00 USD | 0.00 USD | `+3.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.05` | 3,070,000.00 USD | 230,330.00 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.15` | 3,070,000.00 USD | 1,730.00 USD | 0.00 USD | `+3.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.25` | 3,080,000.00 USD | 5,990.00 USD | 0.00 USD | `+3.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.35` | 3,080,000.00 USD | 2,310.00 USD | 0.00 USD | `+3.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.45` | 3,080,000.00 USD | 1,740.00 USD | 0.00 USD | `+3.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.55` | 3,100,000.00 USD | 14,000.00 USD | 0.00 USD | `+3.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.65` | 3,100,000.00 USD | 762.38 USD | 0.00 USD | `+3.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.75` | 3,100,000.00 USD | 870.98 USD | 0.00 USD | `+3.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.85` | 3,100,000.00 USD | 2,210.00 USD | 0.00 USD | `+3.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.95` | 3,110,000.00 USD | 7,640.00 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 3,200,000.00 USD | 88,160.00 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.15` | 3,200,000.00 USD | 2,450.00 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.25` | 3,200,000.00 USD | 2,440.00 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.35` | 3,210,000.00 USD | 4,930.00 USD | 0.00 USD | `+4.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.45` | 3,220,000.00 USD | 7,280.00 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.55` | 3,230,000.00 USD | 15,190.00 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.65` | 3,500,000.00 USD | 264,900.00 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.75` | 3,500,000.00 USD | 1,280.00 USD | 0.00 USD | `+4.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.85` | 3,500,000.00 USD | 3,650.00 USD | 0.00 USD | `+4.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.95` | 3,510,000.00 USD | 5,900.00 USD | 0.00 USD | `+5.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 4,550,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+5.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 4,560,000.00 USD | 3,180.00 USD | 0.00 USD | `+5.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.25` | 4,620,000.00 USD | 64,080.00 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.35` | 4,620,000.00 USD | 4,260.00 USD | 0.00 USD | `+5.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.45` | 4,630,000.00 USD | 3,860.00 USD | 0.00 USD | `+5.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.55` | 4,630,000.00 USD | 6,180.00 USD | 0.00 USD | `+5.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.65` | 4,650,000.00 USD | 17,250.00 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.75` | 4,650,000.00 USD | 980.44 USD | 0.00 USD | `+5.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.85` | 4,880,000.00 USD | 227,770.00 USD | 0.00 USD | `+6.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.95` | 4,940,000.00 USD | 62,400.00 USD | 0.00 USD | `+6.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.05` | 4,950,000.00 USD | 12,270.00 USD | 0.00 USD | `+6.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.15` | 4,960,000.00 USD | 1,720.00 USD | 0.00 USD | `+6.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.25` | 4,960,000.00 USD | 519.17 USD | 0.00 USD | `+6.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.35` | 4,960,000.00 USD | 146.09 USD | 0.00 USD | `+6.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.45` | 5,050,000.00 USD | 95,950.00 USD | 0.00 USD | `+6.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.55` | 5,080,000.00 USD | 26,540.00 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.65` | 5,080,000.00 USD | 230.23 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.75` | 5,080,000.00 USD | 1,900.00 USD | 0.00 USD | `+6.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.85` | 5,090,000.00 USD | 5,900.00 USD | 0.00 USD | `+7.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.95` | 5,110,000.00 USD | 25,930.00 USD | 0.00 USD | `+7.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.05` | 5,240,000.00 USD | 123,260.00 USD | 0.00 USD | `+7.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.15` | 5,270,000.00 USD | 31,990.00 USD | 0.00 USD | `+7.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.25` | 5,270,000.00 USD | 1,010.00 USD | 0.00 USD | `+7.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.35` | 5,270,000.00 USD | 1,090.00 USD | 0.00 USD | `+7.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.45` | 5,270,000.00 USD | 266.79 USD | 0.00 USD | `+7.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.55` | 5,270,000.00 USD | 3,620.00 USD | 0.00 USD | `+7.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.65` | 5,280,000.00 USD | 235.60 USD | 0.00 USD | `+7.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.75` | 5,280,000.00 USD | 549.90 USD | 0.00 USD | `+7.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.85` | 5,290,000.00 USD | 10,600.00 USD | 0.00 USD | `+8.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.95` | 5,290,000.00 USD | 206.60 USD | 0.00 USD | `+8.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.05` | 5,310,000.00 USD | 19,890.00 USD | 0.00 USD | `+8.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.15` | 5,310,000.00 USD | 7,080.00 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.25` | 5,310,000.00 USD | 758.62 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.35` | 5,320,000.00 USD | 7,980.00 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.45` | 5,350,000.00 USD | 26,170.00 USD | 0.00 USD | `+8.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.55` | 5,360,000.00 USD | 6,950.00 USD | 0.00 USD | `+8.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.65` | 5,360,000.00 USD | 355.14 USD | 0.00 USD | `+8.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.75` | 5,470,000.00 USD | 110,530.00 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.85` | 5,470,000.00 USD | 1,400.00 USD | 0.00 USD | `+9.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.95` | 5,500,000.00 USD | 33,170.00 USD | 0.00 USD | `+9.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.05` | 5,640,000.00 USD | 142,930.00 USD | 0.00 USD | `+9.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.15` | 5,640,000.00 USD | 109.29 USD | 0.00 USD | `+9.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.25` | 5,660,000.00 USD | 20,190.00 USD | 0.00 USD | `+9.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.35` | 5,660,000.00 USD | 698.85 USD | 0.00 USD | `+9.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.45` | 5,670,000.00 USD | 8,930.00 USD | 0.00 USD | `+9.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.55` | 5,730,000.00 USD | 52,130.00 USD | 0.00 USD | `+9.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.65` | 5,790,000.00 USD | 65,380.00 USD | 0.00 USD | `+9.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.75` | 5,790,000.00 USD | 536.60 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.85` | 5,800,000.00 USD | 11,800.00 USD | 0.00 USD | `+10.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.95` | 5,810,000.00 USD | 9,120.00 USD | 0.00 USD | `+10.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 5,900,000.00 USD | 87,120.00 USD | 0.00 USD | `+10.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.15` | 5,970,000.00 USD | 68,190.00 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.35` | 5,980,000.00 USD | 7,140.00 USD | 0.00 USD | `+10.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.45` | 5,980,000.00 USD | 2,580.00 USD | 0.00 USD | `+10.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.55` | 5,980,000.00 USD | 5,430.00 USD | 0.00 USD | `+10.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.65` | 5,980,000.00 USD | 666.02 USD | 0.00 USD | `+10.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.75` | 5,980,000.00 USD | 1,030.00 USD | 0.00 USD | `+11.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.85` | 5,990,000.00 USD | 1,430.00 USD | 0.00 USD | `+11.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.95` | 6,030,000.00 USD | 40,920.00 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 6,100,000.00 USD | 72,930.00 USD | 0.00 USD | `+11.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.15` | 6,110,000.00 USD | 7,660.00 USD | 0.00 USD | `+11.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.25` | 10,000,000.00 USD | 3,890,000.00 USD | 0.00 USD | `+11.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.35` | 10,020,000.00 USD | 25,320.00 USD | 0.00 USD | `+11.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.45` | 10,030,000.00 USD | 5,880.00 USD | 0.00 USD | `+11.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.55` | 10,030,000.00 USD | 1,070.00 USD | 0.00 USD | `+11.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.65` | 10,040,000.00 USD | 5,410.00 USD | 0.00 USD | `+11.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.75` | 10,040,000.00 USD | 1,370.00 USD | 0.00 USD | `+12.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.85` | 10,040,000.00 USD | 1,430.00 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.95` | 10,040,000.00 USD | 357.34 USD | 0.00 USD | `+12.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.05` | 10,560,000.00 USD | 519,200.00 USD | 0.00 USD | `+12.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.15` | 10,560,000.00 USD | 1,030.00 USD | 0.00 USD | `+12.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.25` | 10,560,000.00 USD | 3,230.00 USD | 0.00 USD | `+12.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.35` | 10,560,000.00 USD | 1,610.00 USD | 0.00 USD | `+12.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.45` | 10,570,000.00 USD | 1,580.00 USD | 0.00 USD | `+12.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.55` | 10,580,000.00 USD | 10,280.00 USD | 0.00 USD | `+12.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.65` | 10,580,000.00 USD | 3,030.00 USD | 0.00 USD | `+12.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.85` | 10,600,000.00 USD | 17,740.00 USD | 0.00 USD | `+13.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.95` | 10,670,000.00 USD | 74,410.00 USD | 0.00 USD | `+13.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 10,740,000.00 USD | 64,530.00 USD | 0.00 USD | `+13.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.15` | 10,740,000.00 USD | 1,300.00 USD | 0.00 USD | `+13.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.25` | 10,740,000.00 USD | 5,910.00 USD | 0.00 USD | `+13.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.45` | 10,740,000.00 USD | 585.11 USD | 0.00 USD | `+13.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.55` | 10,740,000.00 USD | 852.24 USD | 0.00 USD | `+13.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.65` | 11,330,000.00 USD | 581,160.00 USD | 0.00 USD | `+13.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.75` | 11,330,000.00 USD | 2,420.00 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.85` | 11,330,000.00 USD | 2,330.00 USD | 0.00 USD | `+14.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.05` | 11,350,000.00 USD | 16,120.00 USD | 0.00 USD | `+14.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.15` | 11,400,000.00 USD | 49,680.00 USD | 0.00 USD | `+14.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.25` | 11,400,000.00 USD | 4,960.00 USD | 0.00 USD | `+14.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.35` | 11,410,000.00 USD | 6,270.00 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.45` | 11,410,000.00 USD | 843.38 USD | 0.00 USD | `+14.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.55` | 11,440,000.00 USD | 36,280.00 USD | 0.00 USD | `+14.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.65` | 11,450,000.00 USD | 6,150.00 USD | 0.00 USD | `+15.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.85` | 11,450,000.00 USD | 586.82 USD | 0.00 USD | `+15.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.05` | 11,530,000.00 USD | 78,560.00 USD | 0.00 USD | `+15.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.25` | 11,530,000.00 USD | 473.38 USD | 0.00 USD | `+15.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.35` | 11,570,000.00 USD | 35,070.00 USD | 0.00 USD | `+15.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.45` | 11,570,000.00 USD | 655.74 USD | 0.00 USD | `+15.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.55` | 11,570,000.00 USD | 4,470.00 USD | 0.00 USD | `+15.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.65` | 11,570,000.00 USD | 395.50 USD | 0.00 USD | `+16.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.75` | 11,570,000.00 USD | 257.07 USD | 0.00 USD | `+16.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.85` | 11,580,000.00 USD | 4,540.00 USD | 0.00 USD | `+16.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.05` | 11,580,000.00 USD | 1,970.00 USD | 0.00 USD | `+16.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.15` | 11,590,000.00 USD | 11,410.00 USD | 0.00 USD | `+16.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.25` | 11,590,000.00 USD | 907.14 USD | 0.00 USD | `+16.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.35` | 11,590,000.00 USD | 740.99 USD | 0.00 USD | `+16.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.45` | 11,590,000.00 USD | 343.35 USD | 0.00 USD | `+16.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.55` | 11,590,000.00 USD | 1,640.00 USD | 0.00 USD | `+16.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.65` | 11,590,000.00 USD | 105.48 USD | 0.00 USD | `+17.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.75` | 11,590,000.00 USD | 1,010.00 USD | 0.00 USD | `+17.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.95` | 11,600,000.00 USD | 2,520.00 USD | 0.00 USD | `+17.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.05` | 11,680,000.00 USD | 81,890.00 USD | 0.00 USD | `+17.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.35` | 11,680,000.00 USD | 309.14 USD | 0.00 USD | `+17.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.45` | 11,680,000.00 USD | 346.35 USD | 0.00 USD | `+17.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.55` | 11,680,000.00 USD | 2,440.00 USD | 0.00 USD | `+17.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.75` | 11,680,000.00 USD | 121.54 USD | 0.00 USD | `+18.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.85` | 11,680,000.00 USD | 579.25 USD | 0.00 USD | `+18.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.05` | 11,750,000.00 USD | 65,120.00 USD | 0.00 USD | `+18.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.15` | 11,750,000.00 USD | 1,740.00 USD | 0.00 USD | `+18.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.25` | 11,750,000.00 USD | 1,920.00 USD | 0.00 USD | `+18.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.45` | 11,750,000.00 USD | 2,870.00 USD | 0.00 USD | `+18.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.55` | 11,760,000.00 USD | 10,810.00 USD | 0.00 USD | `+18.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.65` | 11,770,000.00 USD | 6,000.00 USD | 0.00 USD | `+19.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.75` | 11,770,000.00 USD | 3,580.00 USD | 0.00 USD | `+19.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.85` | 11,770,000.00 USD | 234.87 USD | 0.00 USD | `+19.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.95` | 11,790,000.00 USD | 12,860.00 USD | 0.00 USD | `+19.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.05` | 11,790,000.00 USD | 4,200.00 USD | 0.00 USD | `+19.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.15` | 11,790,000.00 USD | 584.58 USD | 0.00 USD | `+19.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.25` | 11,790,000.00 USD | 1,740.00 USD | 0.00 USD | `+19.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.35` | 11,800,000.00 USD | 2,330.00 USD | 0.00 USD | `+19.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.45` | 11,910,000.00 USD | 118,690.00 USD | 0.00 USD | `+19.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.65` | 12,020,000.00 USD | 106,330.00 USD | 0.00 USD | `+20.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.75` | 12,030,000.00 USD | 5,920.00 USD | 0.00 USD | `+20.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.85` | 12,080,000.00 USD | 55,580.00 USD | 0.00 USD | `+20.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.05` | 12,150,000.00 USD | 69,220.00 USD | 0.00 USD | `+20.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.15` | 12,160,000.00 USD | 3,980.00 USD | 0.00 USD | `+20.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.25` | 12,160,000.00 USD | 4,460.00 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.35` | 12,160,000.00 USD | 127.82 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.45` | 12,160,000.00 USD | 707.15 USD | 0.00 USD | `+20.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.55` | 12,160,000.00 USD | 1,260.00 USD | 0.00 USD | `+21.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.65` | 12,170,000.00 USD | 2,970.00 USD | 0.00 USD | `+21.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.75` | 12,170,000.00 USD | 403.75 USD | 0.00 USD | `+21.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.85` | 12,180,000.00 USD | 15,940.00 USD | 0.00 USD | `+21.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.95` | 12,220,000.00 USD | 42,290.00 USD | 0.00 USD | `+21.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.05` | 12,280,000.00 USD | 52,430.00 USD | 0.00 USD | `+21.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.15` | 12,290,000.00 USD | 15,130.00 USD | 0.00 USD | `+21.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.25` | 12,290,000.00 USD | 1,850.00 USD | 0.00 USD | `+21.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.35` | 12,300,000.00 USD | 4,150.00 USD | 0.00 USD | `+21.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.45` | 12,300,000.00 USD | 3,580.00 USD | 0.00 USD | `+21.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.65` | 12,300,000.00 USD | 615.00 USD | 0.00 USD | `+22.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.75` | 12,430,000.00 USD | 125,500.00 USD | 0.00 USD | `+22.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.85` | 12,460,000.00 USD | 37,630.00 USD | 0.00 USD | `+22.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.95` | 12,470,000.00 USD | 458.21 USD | 0.00 USD | `+22.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.05` | 12,650,000.00 USD | 181,190.00 USD | 0.00 USD | `+22.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.15` | 12,650,000.00 USD | 414.52 USD | 0.00 USD | `+22.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.25` | 12,650,000.00 USD | 3,210.00 USD | 0.00 USD | `+22.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.35` | 12,660,000.00 USD | 7,850.00 USD | 0.00 USD | `+22.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.45` | 12,670,000.00 USD | 13,560.00 USD | 0.00 USD | `+22.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.55` | 12,670,000.00 USD | 904.13 USD | 0.00 USD | `+23.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.65` | 12,670,000.00 USD | 191.83 USD | 0.00 USD | `+23.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.75` | 12,670,000.00 USD | 2,150.00 USD | 0.00 USD | `+23.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.85` | 12,680,000.00 USD | 663.47 USD | 0.00 USD | `+23.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.05` | 12,700,000.00 USD | 20,810.00 USD | 0.00 USD | `+23.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.15` | 12,700,000.00 USD | 122.36 USD | 0.00 USD | `+23.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.25` | 12,710,000.00 USD | 11,200.00 USD | 0.00 USD | `+23.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.45` | 12,720,000.00 USD | 11,570.00 USD | 0.00 USD | `+23.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.55` | 12,730,000.00 USD | 7,860.00 USD | 0.00 USD | `+24.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.65` | 12,730,000.00 USD | 2,070.00 USD | 0.00 USD | `+24.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.75` | 12,730,000.00 USD | 2,450.00 USD | 0.00 USD | `+24.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.85` | 12,730,000.00 USD | 1,480.00 USD | 0.00 USD | `+24.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.95` | 12,810,000.00 USD | 80,260.00 USD | 0.00 USD | `+24.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.05` | 13,010,000.00 USD | 199,800.00 USD | 0.00 USD | `+24.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.15` | 13,010,000.00 USD | 1,000.00 USD | 0.00 USD | `+24.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.25` | 13,250,000.00 USD | 234,430.00 USD | 0.00 USD | `+24.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.35` | 13,300,000.00 USD | 52,330.00 USD | 0.00 USD | `+24.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.45` | 13,300,000.00 USD | 3,060.00 USD | 0.00 USD | `+25.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.55` | 13,310,000.00 USD | 7,020.00 USD | 0.00 USD | `+25.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.65` | 13,320,000.00 USD | 11,000.00 USD | 0.00 USD | `+25.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.75` | 13,320,000.00 USD | 235.68 USD | 0.00 USD | `+25.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.85` | 13,330,000.00 USD | 3,850.00 USD | 0.00 USD | `+25.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.95` | 13,340,000.00 USD | 16,430.00 USD | 0.00 USD | `+25.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.05` | 14,350,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+25.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.15` | 14,350,000.00 USD | 252.46 USD | 0.00 USD | `+25.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.25` | 14,360,000.00 USD | 7,710.00 USD | 0.00 USD | `+25.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.35` | 14,370,000.00 USD | 6,790.00 USD | 0.00 USD | `+25.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.45` | 14,370,000.00 USD | 2,670.00 USD | 0.00 USD | `+26.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.55` | 14,370,000.00 USD | 632.58 USD | 0.00 USD | `+26.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.65` | 14,380,000.00 USD | 13,450.00 USD | 0.00 USD | `+26.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.85` | 14,390,000.00 USD | 5,530.00 USD | 0.00 USD | `+26.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.95` | 14,410,000.00 USD | 18,470.00 USD | 0.00 USD | `+26.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.05` | 14,760,000.00 USD | 355,910.00 USD | 0.00 USD | `+26.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.15` | 14,770,000.00 USD | 1,320.00 USD | 0.00 USD | `+26.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.25` | 14,770,000.00 USD | 151.59 USD | 0.00 USD | `+26.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.35` | 14,770,000.00 USD | 4,240.00 USD | 0.00 USD | `+26.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.45` | 14,770,000.00 USD | 1,370.00 USD | 0.00 USD | `+27.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.55` | 14,780,000.00 USD | 7,330.00 USD | 0.00 USD | `+27.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.65` | 14,780,000.00 USD | 6,610.00 USD | 0.00 USD | `+27.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.85` | 14,790,000.00 USD | 596.78 USD | 0.00 USD | `+27.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.95` | 14,800,000.00 USD | 10,310.00 USD | 0.00 USD | `+27.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.05` | 15,350,000.00 USD | 554,250.00 USD | 0.00 USD | `+27.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.15` | 15,350,000.00 USD | 603.22 USD | 0.00 USD | `+27.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.25` | 15,360,000.00 USD | 7,990.00 USD | 0.00 USD | `+27.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.35` | 15,370,000.00 USD | 6,780.00 USD | 0.00 USD | `+27.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.45` | 15,370,000.00 USD | 993.56 USD | 0.00 USD | `+28.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.55` | 15,380,000.00 USD | 16,280.00 USD | 0.00 USD | `+28.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.85` | 15,380,000.00 USD | 471.94 USD | 0.00 USD | `+28.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.95` | 15,380,000.00 USD | 209.08 USD | 0.00 USD | `+28.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.05` | 15,530,000.00 USD | 151,060.00 USD | 0.00 USD | `+28.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.15` | 15,530,000.00 USD | 189.23 USD | 0.00 USD | `+28.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.45` | 15,530,000.00 USD | 187.15 USD | 0.00 USD | `+29.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.65` | 15,540,000.00 USD | 3,550.00 USD | 0.00 USD | `+29.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.75` | 15,550,000.00 USD | 7,460.00 USD | 0.00 USD | `+29.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.05` | 15,740,000.00 USD | 190,580.00 USD | 0.00 USD | `+29.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.35` | 15,740,000.00 USD | 534.87 USD | 0.00 USD | `+30.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.45` | 15,740,000.00 USD | 4,620.00 USD | 0.00 USD | `+30.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.65` | 15,750,000.00 USD | 5,000.00 USD | 0.00 USD | `+30.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.75` | 15,750,000.00 USD | 362.81 USD | 0.00 USD | `+30.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.85` | 15,810,000.00 USD | 60,770.00 USD | 0.00 USD | `+30.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.95` | 15,810,000.00 USD | 482.37 USD | 0.00 USD | `+30.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.05` | 15,810,000.00 USD | 3,700.00 USD | 0.00 USD | `+30.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.15` | 15,810,000.00 USD | 3,010.00 USD | 0.00 USD | `+30.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.25` | 15,810,000.00 USD | 191.09 USD | 0.00 USD | `+30.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.65` | 15,860,000.00 USD | 41,130.00 USD | 0.00 USD | `+31.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.95` | 15,870,000.00 USD | 12,600.00 USD | 0.00 USD | `+31.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.05` | 15,920,000.00 USD | 50,720.00 USD | 0.00 USD | `+31.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.15` | 15,920,000.00 USD | 229.89 USD | 0.00 USD | `+31.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.25` | 15,930,000.00 USD | 15,330.00 USD | 0.00 USD | `+31.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.45` | 15,940,000.00 USD | 401.29 USD | 0.00 USD | `+32.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.55` | 15,940,000.00 USD | 1,320.00 USD | 0.00 USD | `+32.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.65` | 15,940,000.00 USD | 152.99 USD | 0.00 USD | `+32.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.75` | 15,940,000.00 USD | 153.10 USD | 0.00 USD | `+32.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.85` | 15,940,000.00 USD | 116.87 USD | 0.00 USD | `+32.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.05` | 15,990,000.00 USD | 50,760.00 USD | 0.00 USD | `+32.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.35` | 15,990,000.00 USD | 1,760.00 USD | 0.00 USD | `+33.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.45` | 15,990,000.00 USD | 4,090.00 USD | 0.00 USD | `+33.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.65` | 15,990,000.00 USD | 192.06 USD | 0.00 USD | `+33.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.75` | 16,000,000.00 USD | 3,150.00 USD | 0.00 USD | `+33.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.85` | 16,000,000.00 USD | 2,620.00 USD | 0.00 USD | `+33.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.95` | 16,010,000.00 USD | 10,140.00 USD | 0.00 USD | `+33.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.05` | 16,020,000.00 USD | 6,000.00 USD | 0.00 USD | `+33.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.15` | 16,020,000.00 USD | 5,950.00 USD | 0.00 USD | `+33.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.25` | 16,030,000.00 USD | 8,820.00 USD | 0.00 USD | `+33.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.45` | 16,030,000.00 USD | 135.39 USD | 0.00 USD | `+34.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.65` | 16,190,000.00 USD | 160,920.00 USD | 0.00 USD | `+34.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.75` | 16,190,000.00 USD | 144.93 USD | 0.00 USD | `+34.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.05` | 16,200,000.00 USD | 12,390.00 USD | 0.00 USD | `+34.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.65` | 16,200,000.00 USD | 397.95 USD | 0.00 USD | `+35.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.85` | 16,210,000.00 USD | 9,310.00 USD | 0.00 USD | `+35.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.95` | 16,220,000.00 USD | 3,910.00 USD | 0.00 USD | `+35.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.05` | 16,220,000.00 USD | 267.43 USD | 0.00 USD | `+35.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.15` | 16,220,000.00 USD | 509.96 USD | 0.00 USD | `+35.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.25` | 16,220,000.00 USD | 191.88 USD | 0.00 USD | `+36.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.35` | 16,220,000.00 USD | 237.36 USD | 0.00 USD | `+36.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.55` | 16,220,000.00 USD | 1,210.00 USD | 0.00 USD | `+36.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.65` | 16,220,000.00 USD | 192.46 USD | 0.00 USD | `+36.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.75` | 16,220,000.00 USD | 112.35 USD | 0.00 USD | `+36.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.95` | 16,230,000.00 USD | 4,620.00 USD | 0.00 USD | `+36.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.05` | 16,280,000.00 USD | 54,080.00 USD | 0.00 USD | `+36.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.25` | 16,280,000.00 USD | 331.60 USD | 0.00 USD | `+37.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.55` | 16,550,000.00 USD | 270,270.00 USD | 0.00 USD | `+37.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.85` | 16,550,000.00 USD | 625.70 USD | 0.00 USD | `+37.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.05` | 16,670,000.00 USD | 116,220.00 USD | 0.00 USD | `+37.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.55` | 16,670,000.00 USD | 7,560.00 USD | 0.00 USD | `+38.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.05` | 16,680,000.00 USD | 1,890.00 USD | 0.00 USD | `+38.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.35` | 16,680,000.00 USD | 192.25 USD | 0.00 USD | `+39.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.45` | 16,680,000.00 USD | 465.29 USD | 0.00 USD | `+39.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.55` | 16,680,000.00 USD | 389.17 USD | 0.00 USD | `+39.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.85` | 16,680,000.00 USD | 826.57 USD | 0.00 USD | `+39.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.05` | 16,680,000.00 USD | 231.61 USD | 0.00 USD | `+39.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.25` | 16,680,000.00 USD | 2,910.00 USD | 0.00 USD | `+40.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.35` | 16,690,000.00 USD | 3,920.00 USD | 0.00 USD | `+40.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.65` | 16,710,000.00 USD | 26,260.00 USD | 0.00 USD | `+40.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.75` | 16,710,000.00 USD | 133.62 USD | 0.00 USD | `+40.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.05` | 16,730,000.00 USD | 18,910.00 USD | 0.00 USD | `+40.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.45` | 16,730,000.00 USD | 692.25 USD | 0.00 USD | `+41.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.65` | 16,730,000.00 USD | 406.24 USD | 0.00 USD | `+41.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.85` | 23,470,000.00 USD | 6,740,000.00 USD | 0.00 USD | `+41.74%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `138.95` | 23,480,000.00 USD | 826.75 USD | 0.00 USD | `+41.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.05` | 25,670,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+41.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.55` | 25,670,000.00 USD | 5,920.00 USD | 0.00 USD | `+42.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.05` | 25,780,000.00 USD | 110,660.00 USD | 0.00 USD | `+42.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.45` | 25,800,000.00 USD | 12,120.00 USD | 0.00 USD | `+43.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.55` | 25,890,000.00 USD | 98,400.00 USD | 0.00 USD | `+43.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.75` | 25,900,000.00 USD | 990.88 USD | 0.00 USD | `+43.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.05` | 25,910,000.00 USD | 11,640.00 USD | 0.00 USD | `+43.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.25` | 25,910,000.00 USD | 6,190.00 USD | 0.00 USD | `+44.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.65` | 25,910,000.00 USD | 796.07 USD | 0.00 USD | `+44.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.05` | 25,910,000.00 USD | 826.73 USD | 0.00 USD | `+45.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.85` | 25,910,000.00 USD | 278.56 USD | 0.00 USD | `+45.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.95` | 26,240,000.00 USD | 329,100.00 USD | 0.00 USD | `+45.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.05` | 26,320,000.00 USD | 72,610.00 USD | 0.00 USD | `+46.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.15` | 26,330,000.00 USD | 16,980.00 USD | 0.00 USD | `+46.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.35` | 26,330,000.00 USD | 528.96 USD | 0.00 USD | `+46.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.05` | 26,340,000.00 USD | 6,330.00 USD | 0.00 USD | `+47.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.25` | 26,340,000.00 USD | 415.44 USD | 0.00 USD | `+47.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.35` | 26,620,000.00 USD | 282,520.00 USD | 0.00 USD | `+47.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.55` | 26,630,000.00 USD | 7,260.00 USD | 0.00 USD | `+47.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.75` | 26,630,000.00 USD | 791.78 USD | 0.00 USD | `+47.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.05` | 26,670,000.00 USD | 36,040.00 USD | 0.00 USD | `+48.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.25` | 26,670,000.00 USD | 209.16 USD | 0.00 USD | `+48.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.55` | 26,670,000.00 USD | 698.64 USD | 0.00 USD | `+48.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.05` | 26,860,000.00 USD | 190,100.00 USD | 0.00 USD | `+49.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.15` | 26,860,000.00 USD | 3,300.00 USD | 0.00 USD | `+49.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.25` | 26,860,000.00 USD | 1,020.00 USD | 0.00 USD | `+49.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.95` | 26,860,000.00 USD | 1,500.00 USD | 0.00 USD | `+50.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.05` | 26,900,000.00 USD | 37,700.00 USD | 0.00 USD | `+50.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.45` | 26,900,000.00 USD | 844.89 USD | 0.00 USD | `+50.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.85` | 26,910,000.00 USD | 4,610.00 USD | 0.00 USD | `+50.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.95` | 26,910,000.00 USD | 3,100.00 USD | 0.00 USD | `+51.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.05` | 28,250,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+51.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.45` | 28,250,000.00 USD | 1,370.00 USD | 0.00 USD | `+51.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.55` | 28,260,000.00 USD | 4,760.00 USD | 0.00 USD | `+51.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.05` | 28,260,000.00 USD | 549.99 USD | 0.00 USD | `+52.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.15` | 28,770,000.00 USD | 510,120.00 USD | 0.00 USD | `+52.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.05` | 29,020,000.00 USD | 254,780.00 USD | 0.00 USD | `+53.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.25` | 29,020,000.00 USD | 1,200.00 USD | 0.00 USD | `+53.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.35` | 29,020,000.00 USD | 178.92 USD | 0.00 USD | `+53.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.55` | 29,020,000.00 USD | 1,360.00 USD | 0.00 USD | `+53.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.05` | 29,040,000.00 USD | 14,430.00 USD | 0.00 USD | `+54.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.25` | 29,040,000.00 USD | 2,000.00 USD | 0.00 USD | `+54.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.45` | 29,040,000.00 USD | 411.94 USD | 0.00 USD | `+54.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.15` | 29,050,000.00 USD | 10,620.00 USD | 0.00 USD | `+56.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.65` | 29,050,000.00 USD | 1,020.00 USD | 0.00 USD | `+56.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.55` | 29,060,000.00 USD | 12,000.00 USD | 0.00 USD | `+57.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.85` | 29,060,000.00 USD | 113.04 USD | 0.00 USD | `+58.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.05` | 29,070,000.00 USD | 1,830.00 USD | 0.00 USD | `+58.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.35` | 29,090,000.00 USD | 22,680.00 USD | 0.00 USD | `+58.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.85` | 29,110,000.00 USD | 16,970.00 USD | 0.00 USD | `+59.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.05` | 29,110,000.00 USD | 2,230.00 USD | 0.00 USD | `+59.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.05` | 29,110,000.00 USD | 6,640.00 USD | 0.00 USD | `+61.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.75` | 29,130,000.00 USD | 15,880.00 USD | 0.00 USD | `+62.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.15` | 29,130,000.00 USD | 692.30 USD | 0.00 USD | `+62.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.95` | 29,140,000.00 USD | 5,620.00 USD | 0.00 USD | `+63.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.05` | 29,230,000.00 USD | 89,040.00 USD | 0.00 USD | `+63.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.05` | 29,230,000.00 USD | 281.84 USD | 0.00 USD | `+64.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.05` | 29,230,000.00 USD | 4,080.00 USD | 0.00 USD | `+66.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.05` | 29,320,000.00 USD | 89,230.00 USD | 0.00 USD | `+68.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.45` | 29,320,000.00 USD | 823.94 USD | 0.00 USD | `+68.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.45` | 29,320,000.00 USD | 211.39 USD | 0.00 USD | `+69.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.95` | 29,320,000.00 USD | 307.19 USD | 0.00 USD | `+70.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.05` | 29,320,000.00 USD | 593.03 USD | 0.00 USD | `+70.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.75` | 29,320,000.00 USD | 1,440.00 USD | 0.00 USD | `+71.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.05` | 29,330,000.00 USD | 5,720.00 USD | 0.00 USD | `+71.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.55` | 29,330,000.00 USD | 495.09 USD | 0.00 USD | `+73.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.95` | 29,330,000.00 USD | 912.63 USD | 0.00 USD | `+73.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.05` | 29,370,000.00 USD | 43,480.00 USD | 0.00 USD | `+73.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.55` | 29,370,000.00 USD | 686.20 USD | 0.00 USD | `+75.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.05` | 29,410,000.00 USD | 35,280.00 USD | 0.00 USD | `+75.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.45` | 29,410,000.00 USD | 703.60 USD | 0.00 USD | `+76.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.05` | 29,410,000.00 USD | 3,160.00 USD | 0.00 USD | `+76.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `174.85` | 29,410,000.00 USD | 1,430.00 USD | 0.00 USD | `+78.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.05` | 29,470,000.00 USD | 52,520.00 USD | 0.00 USD | `+78.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.25` | 29,490,000.00 USD | 21,960.00 USD | 0.00 USD | `+78.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.85` | 29,490,000.00 USD | 1,450.00 USD | 0.00 USD | `+80.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.05` | 29,490,000.00 USD | 885.25 USD | 0.00 USD | `+80.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.55` | 29,490,000.00 USD | 2,990.00 USD | 0.00 USD | `+82.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.15` | 29,490,000.00 USD | 261.56 USD | 0.00 USD | `+82.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.05` | 29,570,000.00 USD | 80,290.00 USD | 0.00 USD | `+83.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.05` | 29,580,000.00 USD | 2,440.00 USD | 0.00 USD | `+84.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.95` | 29,580,000.00 USD | 349.34 USD | 0.00 USD | `+85.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.45` | 29,600,000.00 USD | 19,620.00 USD | 0.00 USD | `+86.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.45` | 30,150,000.00 USD | 550,350.00 USD | 0.00 USD | `+87.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.05` | 30,180,000.00 USD | 29,610.00 USD | 0.00 USD | `+88.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.05` | 30,340,000.00 USD | 165,580.00 USD | 0.00 USD | `+90.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.05` | 30,480,000.00 USD | 141,190.00 USD | 0.00 USD | `+91.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.05` | 30,520,000.00 USD | 35,880.00 USD | 0.00 USD | `+94.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.35` | 30,520,000.00 USD | 744.27 USD | 0.00 USD | `+94.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.65` | 30,530,000.00 USD | 7,750.00 USD | 0.00 USD | `+94.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `194.05` | 30,530,000.00 USD | 4,270.00 USD | 0.00 USD | `+98.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `195.05` | 30,530,000.00 USD | 1,950.00 USD | 0.00 USD | `+99.11%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `82.50` | 171,450,000.00 USD | 0.00 USD | 171,450,000.00 USD | 71,680.00 USD | 3,750.00 USD | 2,420.00 USD |
| `7D` | `82.70` | 171,370,000.00 USD | 0.00 USD | 171,370,000.00 USD | 0.00 USD | 54,980.00 USD | 140,740.00 USD |
| `7D` | `82.90` | 171,170,000.00 USD | 0.00 USD | 171,170,000.00 USD | 1,670.00 USD | 2,080.00 USD | 0.00 USD |
| `7D` | `83.10` | 171,170,000.00 USD | 0.00 USD | 171,170,000.00 USD | 1,690.00 USD | 48,940.00 USD | 642.56 USD |
| `7D` | `83.30` | 171,120,000.00 USD | 0.00 USD | 171,120,000.00 USD | 3,730.00 USD | 93,000.00 USD | 56,580.00 USD |
| `7D` | `83.50` | 170,960,000.00 USD | 0.00 USD | 170,960,000.00 USD | 6,440.00 USD | 791.58 USD | 10,500.00 USD |
| `7D` | `83.70` | 170,950,000.00 USD | 0.00 USD | 170,950,000.00 USD | 0.00 USD | 68,140.00 USD | 85,660.00 USD |
| `7D` | `83.90` | 170,790,000.00 USD | 0.00 USD | 170,790,000.00 USD | 2,640.00 USD | 0.00 USD | 70,110.00 USD |
| `7D` | `84.10` | 170,720,000.00 USD | 0.00 USD | 170,720,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD |
| `7D` | `84.30` | 170,700,000.00 USD | 0.00 USD | 170,700,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD |
| `7D` | `85.10` | 170,670,000.00 USD | 0.00 USD | 170,670,000.00 USD | 0.00 USD | 204,940.00 USD | 0.00 USD |
| `7D` | `85.30` | 170,470,000.00 USD | 0.00 USD | 170,470,000.00 USD | 0.00 USD | 13,630.00 USD | 186,170.00 USD |
| `7D` | `85.50` | 170,270,000.00 USD | 0.00 USD | 170,270,000.00 USD | 0.00 USD | 12,950.00 USD | 6,140.00 USD |
| `7D` | `85.70` | 170,250,000.00 USD | 0.00 USD | 170,250,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD |
| `7D` | `85.90` | 170,060,000.00 USD | 0.00 USD | 170,060,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD |
| `7D` | `86.10` | 169,800,000.00 USD | 0.00 USD | 169,800,000.00 USD | 0.00 USD | 0.00 USD | 195,220.00 USD |
| `7D` | `86.30` | 169,600,000.00 USD | 0.00 USD | 169,600,000.00 USD | 0.00 USD | 323,360.00 USD | 4,140.00 USD |
| `7D` | `86.50` | 169,270,000.00 USD | 0.00 USD | 169,270,000.00 USD | 0.00 USD | 0.00 USD | 4,340.00 USD |
| `7D` | `86.70` | 169,270,000.00 USD | 0.00 USD | 169,270,000.00 USD | 0.00 USD | 11,140.00 USD | 0.00 USD |
| `7D` | `86.90` | 169,260,000.00 USD | 0.00 USD | 169,260,000.00 USD | 263,340.00 USD | 309,680.00 USD | 297,340.00 USD |
| `1D` | `87.10` | 174,880,000.00 USD | 0.00 USD | 174,880,000.00 USD | 316,760.00 USD | 428,310.00 USD | 423,350.00 USD |
| `7D` | `87.10` | 168,390,000.00 USD | 0.00 USD | 168,390,000.00 USD | 0.00 USD | 5,620.00 USD | 6,820.00 USD |
| `1D` | `87.30` | 173,710,000.00 USD | 0.00 USD | 173,710,000.00 USD | 61,200.00 USD | 207,830.00 USD | 156,230.00 USD |
| `7D` | `87.30` | 168,370,000.00 USD | 0.00 USD | 168,370,000.00 USD | 0.00 USD | 204,790.00 USD | 288,100.00 USD |
| `1D` | `87.50` | 173,290,000.00 USD | 0.00 USD | 173,290,000.00 USD | 10,160.00 USD | 72,180.00 USD | 69,020.00 USD |
| `7D` | `87.50` | 167,880,000.00 USD | 0.00 USD | 167,880,000.00 USD | 24,350.00 USD | 24,850.00 USD | 0.00 USD |
| `1D` | `87.70` | 173,140,000.00 USD | 0.00 USD | 173,140,000.00 USD | 8,600.00 USD | 247,780.00 USD | 247,620.00 USD |
| `7D` | `87.70` | 167,830,000.00 USD | 0.00 USD | 167,830,000.00 USD | 0.00 USD | 290,940.00 USD | 415,730.00 USD |
| `1D` | `87.90` | 172,630,000.00 USD | 0.00 USD | 172,630,000.00 USD | 133,480.00 USD | 427,430.00 USD | 925,920.00 USD |
| `7D` | `87.90` | 167,130,000.00 USD | 0.00 USD | 167,130,000.00 USD | 0.00 USD | 307,460.00 USD | 251,100.00 USD |
| `1D` | `88.10` | 171,140,000.00 USD | 0.00 USD | 171,140,000.00 USD | 54,110.00 USD | 0.00 USD | 230,360.00 USD |
| `7D` | `88.10` | 166,570,000.00 USD | 0.00 USD | 166,570,000.00 USD | 0.00 USD | 0.00 USD | 12,670.00 USD |
| `1D` | `88.30` | 170,860,000.00 USD | 0.00 USD | 170,860,000.00 USD | 83,370.00 USD | 73,830.00 USD | 136,810.00 USD |
| `7D` | `88.30` | 166,550,000.00 USD | 0.00 USD | 166,550,000.00 USD | 0.00 USD | 20,610.00 USD | 331,480.00 USD |
| `1D` | `88.50` | 170,570,000.00 USD | 0.00 USD | 170,570,000.00 USD | 0.00 USD | 99,900.00 USD | 1,320.00 USD |
| `7D` | `88.50` | 166,200,000.00 USD | 0.00 USD | 166,200,000.00 USD | 0.00 USD | 0.00 USD | 3,910.00 USD |
| `1D` | `88.70` | 170,470,000.00 USD | 0.00 USD | 170,470,000.00 USD | 204,330.00 USD | 124,180.00 USD | 415,440.00 USD |
| `7D` | `88.70` | 166,200,000.00 USD | 0.00 USD | 166,200,000.00 USD | 224,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `88.90` | 169,720,000.00 USD | 0.00 USD | 169,720,000.00 USD | 143,140.00 USD | 62,660.00 USD | 226,460.00 USD |
| `7D` | `88.90` | 165,970,000.00 USD | 0.00 USD | 165,970,000.00 USD | 17,470.00 USD | 3,730.00 USD | 3,570.00 USD |
| `1D` | `89.10` | 169,290,000.00 USD | 0.00 USD | 169,290,000.00 USD | 160,900.00 USD | 83,520.00 USD | 11,880.00 USD |
| `7D` | `89.10` | 165,950,000.00 USD | 0.00 USD | 165,950,000.00 USD | 350,210.00 USD | 291,000.00 USD | 601,650.00 USD |
| `1D` | `89.30` | 169,030,000.00 USD | 0.00 USD | 169,030,000.00 USD | 221,290.00 USD | 284,680.00 USD | 5,050.00 USD |
| `7D` | `89.30` | 164,710,000.00 USD | 0.00 USD | 164,710,000.00 USD | 679,190.00 USD | 22,080.00 USD | 27,480.00 USD |
| `1D` | `89.50` | 168,520,000.00 USD | 0.00 USD | 168,520,000.00 USD | 4,870.00 USD | 50,620.00 USD | 278,210.00 USD |
| `7D` | `89.50` | 163,980,000.00 USD | 0.00 USD | 163,980,000.00 USD | 184,930.00 USD | 91,380.00 USD | 512,480.00 USD |
| `1D` | `89.70` | 168,190,000.00 USD | 0.00 USD | 168,190,000.00 USD | 190,910.00 USD | 107,730.00 USD | 426,480.00 USD |
| `7D` | `89.70` | 163,190,000.00 USD | 0.00 USD | 163,190,000.00 USD | 780,700.00 USD | 225,300.00 USD | 472,550.00 USD |
| `1D` | `89.90` | 167,460,000.00 USD | 0.00 USD | 167,460,000.00 USD | 301,540.00 USD | 255,100.00 USD | 381,220.00 USD |
| `7D` | `89.90` | 161,710,000.00 USD | 0.00 USD | 161,710,000.00 USD | 446,430.00 USD | 563,970.00 USD | 807,700.00 USD |
| `1D` | `90.10` | 166,530,000.00 USD | 0.00 USD | 166,530,000.00 USD | 1,210,000.00 USD | 1,030,000.00 USD | 836,530.00 USD |
| `7D` | `90.10` | 159,890,000.00 USD | 0.00 USD | 159,890,000.00 USD | 967,200.00 USD | 633,920.00 USD | 879,080.00 USD |
| `1D` | `90.30` | 163,450,000.00 USD | 0.00 USD | 163,450,000.00 USD | 773,740.00 USD | 539,900.00 USD | 443,720.00 USD |
| `7D` | `90.30` | 157,410,000.00 USD | 0.00 USD | 157,410,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD |
| `1D` | `90.50` | 161,690,000.00 USD | 0.00 USD | 161,690,000.00 USD | 683,680.00 USD | 538,340.00 USD | 928,480.00 USD |
| `7D` | `90.50` | 155,330,000.00 USD | 0.00 USD | 155,330,000.00 USD | 1,100,000.00 USD | 823,160.00 USD | 860,530.00 USD |
| `1D` | `90.70` | 159,540,000.00 USD | 0.00 USD | 159,540,000.00 USD | 628,630.00 USD | 803,190.00 USD | 388,680.00 USD |
| `7D` | `90.70` | 152,550,000.00 USD | 0.00 USD | 152,550,000.00 USD | 742,490.00 USD | 700,720.00 USD | 1,440,000.00 USD |
| `1D` | `90.90` | 157,720,000.00 USD | 0.00 USD | 157,720,000.00 USD | 673,680.00 USD | 420,760.00 USD | 83,650.00 USD |
| `7D` | `90.90` | 149,670,000.00 USD | 0.00 USD | 149,670,000.00 USD | 1,350,000.00 USD | 997,660.00 USD | 1,020,000.00 USD |
| `1D` | `91.10` | 156,540,000.00 USD | 0.00 USD | 156,540,000.00 USD | 436,270.00 USD | 732,110.00 USD | 474,290.00 USD |
| `7D` | `91.10` | 146,290,000.00 USD | 0.00 USD | 146,290,000.00 USD | 2,350,000.00 USD | 578,750.00 USD | 895,510.00 USD |
| `1D` | `91.30` | 154,900,000.00 USD | 0.00 USD | 154,900,000.00 USD | 150,320.00 USD | 221,290.00 USD | 448,730.00 USD |
| `7D` | `91.30` | 142,470,000.00 USD | 0.00 USD | 142,470,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 1,090,000.00 USD |
| `1D` | `91.50` | 154,080,000.00 USD | 0.00 USD | 154,080,000.00 USD | 850,930.00 USD | 781,420.00 USD | 655,960.00 USD |
| `7D` | `91.50` | 139,490,000.00 USD | 0.00 USD | 139,490,000.00 USD | 705,000.00 USD | 1,710,000.00 USD | 1,290,000.00 USD |
| `1D` | `91.70` | 151,790,000.00 USD | 0.00 USD | 151,790,000.00 USD | 268,750.00 USD | 463,180.00 USD | 1,160,000.00 USD |
| `7D` | `91.70` | 135,780,000.00 USD | 0.00 USD | 135,780,000.00 USD | 538,680.00 USD | 342,840.00 USD | 781,330.00 USD |
| `1D` | `91.90` | 149,900,000.00 USD | 0.00 USD | 149,900,000.00 USD | 1,280,000.00 USD | 813,050.00 USD | 663,410.00 USD |
| `7D` | `91.90` | 134,120,000.00 USD | 0.00 USD | 134,120,000.00 USD | 1,020,000.00 USD | 838,200.00 USD | 1,230,000.00 USD |
| `1D` | `92.10` | 147,140,000.00 USD | 0.00 USD | 147,140,000.00 USD | 2,310,000.00 USD | 2,670,000.00 USD | 565,160.00 USD |
| `7D` | `92.10` | 131,030,000.00 USD | 0.00 USD | 131,030,000.00 USD | 3,150,000.00 USD | 1,400,000.00 USD | 278,960.00 USD |
| `1D` | `92.30` | 141,600,000.00 USD | 0.00 USD | 141,600,000.00 USD | 720,590.00 USD | 799,660.00 USD | 1,410,000.00 USD |
| `7D` | `92.30` | 126,200,000.00 USD | 0.00 USD | 126,200,000.00 USD | 375,130.00 USD | 487,150.00 USD | 1,530,000.00 USD |
| `1D` | `92.50` | 138,670,000.00 USD | 0.00 USD | 138,670,000.00 USD | 1,140,000.00 USD | 703,500.00 USD | 2,340,000.00 USD |
| `7D` | `92.50` | 123,810,000.00 USD | 0.00 USD | 123,810,000.00 USD | 260,510.00 USD | 1,320,000.00 USD | 1,770,000.00 USD |
| `1D` | `92.70` | 134,480,000.00 USD | 0.00 USD | 134,480,000.00 USD | 982,240.00 USD | 1,110,000.00 USD | 1,700,000.00 USD |
| `7D` | `92.70` | 120,460,000.00 USD | 0.00 USD | 120,460,000.00 USD | 148,000.00 USD | 1,830,000.00 USD | 1,610,000.00 USD |
| `1D` | `92.90` | 130,690,000.00 USD | 0.00 USD | 130,690,000.00 USD | 3,020,000.00 USD | 1,870,000.00 USD | 2,470,000.00 USD |
| `7D` | `92.90` | 116,880,000.00 USD | 0.00 USD | 116,880,000.00 USD | 371,030.00 USD | 783,070.00 USD | 954,800.00 USD |
| `1D` | `93.10` | 123,330,000.00 USD | 0.00 USD | 123,330,000.00 USD | 2,030,000.00 USD | 3,210,000.00 USD | 1,730,000.00 USD |
| `7D` | `93.10` | 114,770,000.00 USD | 0.00 USD | 114,770,000.00 USD | 31,020.00 USD | 686,660.00 USD | 1,020,000.00 USD |
| `1D` | `93.30` | 116,350,000.00 USD | 0.00 USD | 116,350,000.00 USD | 2,250,000.00 USD | 2,580,000.00 USD | 1,250,000.00 USD |
| `7D` | `93.30` | 113,030,000.00 USD | 0.00 USD | 113,030,000.00 USD | 96,300.00 USD | 0.00 USD | 1,420,000.00 USD |
| `1D` | `93.50` | 110,270,000.00 USD | 0.00 USD | 110,270,000.00 USD | 2,930,000.00 USD | 2,280,000.00 USD | 2,260,000.00 USD |
| `7D` | `93.50` | 111,510,000.00 USD | 0.00 USD | 111,510,000.00 USD | 399,000.00 USD | 2,880,000.00 USD | 3,050,000.00 USD |
| `1D` | `93.70` | 102,800,000.00 USD | 0.00 USD | 102,800,000.00 USD | 551,230.00 USD | 3,170,000.00 USD | 867,680.00 USD |
| `7D` | `93.70` | 105,190,000.00 USD | 0.00 USD | 105,190,000.00 USD | 7,450.00 USD | 2,970,000.00 USD | 1,700,000.00 USD |
| `1D` | `93.90` | 98,210,000.00 USD | 0.00 USD | 98,210,000.00 USD | 1,590,000.00 USD | 928,170.00 USD | 1,420,000.00 USD |
| `7D` | `93.90` | 100,510,000.00 USD | 0.00 USD | 100,510,000.00 USD | 2,670,000.00 USD | 30,170.00 USD | 3,430,000.00 USD |
| `1D` | `94.10` | 94,270,000.00 USD | 0.00 USD | 94,270,000.00 USD | 680,650.00 USD | 851,000.00 USD | 2,460,000.00 USD |
| `7D` | `94.10` | 94,380,000.00 USD | 0.00 USD | 94,380,000.00 USD | 175,750.00 USD | 2,120,000.00 USD | 2,230,000.00 USD |
| `1D` | `94.30` | 90,280,000.00 USD | 0.00 USD | 90,280,000.00 USD | 2,130,000.00 USD | 1,080,000.00 USD | 371,610.00 USD |
| `7D` | `94.30` | 89,850,000.00 USD | 0.00 USD | 89,850,000.00 USD | 0.00 USD | 159,070.00 USD | 839,350.00 USD |
| `1D` | `94.50` | 86,690,000.00 USD | 0.00 USD | 86,690,000.00 USD | 795,850.00 USD | 1,250,000.00 USD | 645,220.00 USD |
| `7D` | `94.50` | 88,850,000.00 USD | 0.00 USD | 88,850,000.00 USD | 183,750.00 USD | 496,790.00 USD | 0.00 USD |
| `1D` | `94.70` | 84,000,000.00 USD | 0.00 USD | 84,000,000.00 USD | 1,360,000.00 USD | 571,830.00 USD | 399,800.00 USD |
| `7D` | `94.70` | 88,170,000.00 USD | 0.00 USD | 88,170,000.00 USD | 1,600,000.00 USD | 99,300.00 USD | 3,360,000.00 USD |
| `1D` | `94.90` | 81,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 2,720,000.00 USD | 434,700.00 USD | 1,220,000.00 USD |
| `7D` | `94.90` | 83,110,000.00 USD | 0.00 USD | 83,110,000.00 USD | 3,170,000.00 USD | 4,260,000.00 USD | 47,940.00 USD |
| `1D` | `95.10` | 77,300,000.00 USD | 0.00 USD | 77,300,000.00 USD | 2,150,000.00 USD | 1,390,000.00 USD | 27,360.00 USD |
| `7D` | `95.10` | 75,630,000.00 USD | 0.00 USD | 75,630,000.00 USD | 198,380.00 USD | 199,180.00 USD | 17,980.00 USD |
| `1D` | `95.30` | 73,730,000.00 USD | 0.00 USD | 73,730,000.00 USD | 87,330.00 USD | 494,560.00 USD | 3,370,000.00 USD |
| `7D` | `95.30` | 75,210,000.00 USD | 0.00 USD | 75,210,000.00 USD | 678,330.00 USD | 1,060,000.00 USD | 1,680,000.00 USD |
| `1D` | `95.50` | 69,780,000.00 USD | 0.00 USD | 69,780,000.00 USD | 291,230.00 USD | 1,570,000.00 USD | 1,410,000.00 USD |
| `7D` | `95.50` | 71,790,000.00 USD | 0.00 USD | 71,790,000.00 USD | 2,000,000.00 USD | 3,870,000.00 USD | 4,440,000.00 USD |
| `1D` | `95.70` | 66,510,000.00 USD | 0.00 USD | 66,510,000.00 USD | 1,710,000.00 USD | 2,160,000.00 USD | 5,460,000.00 USD |
| `7D` | `95.70` | 61,480,000.00 USD | 0.00 USD | 61,480,000.00 USD | 5,540,000.00 USD | 4,060,000.00 USD | 4,230,000.00 USD |
| `1D` | `95.90` | 57,180,000.00 USD | 0.00 USD | 57,180,000.00 USD | 1,270,000.00 USD | 1,210,000.00 USD | 1,690,000.00 USD |
| `7D` | `95.90` | 47,650,000.00 USD | 0.00 USD | 47,650,000.00 USD | 2,130,000.00 USD | 344,240.00 USD | 689,060.00 USD |
| `1D` | `96.10` | 53,010,000.00 USD | 0.00 USD | 53,010,000.00 USD | 1,770,000.00 USD | 2,040,000.00 USD | 3,220,000.00 USD |
| `7D` | `96.10` | 44,490,000.00 USD | 0.00 USD | 44,490,000.00 USD | 3,460,000.00 USD | 811,100.00 USD | 8,080,000.00 USD |
| `1D` | `96.30` | 45,980,000.00 USD | 0.00 USD | 45,980,000.00 USD | 4,480,000.00 USD | 5,140,000.00 USD | 848,070.00 USD |
| `7D` | `96.30` | 32,140,000.00 USD | 0.00 USD | 32,140,000.00 USD | 2,740,000.00 USD | 1,700,000.00 USD | 6,490,000.00 USD |
| `1D` | `96.50` | 35,510,000.00 USD | 0.00 USD | 35,510,000.00 USD | 2,840,000.00 USD | 1,260,000.00 USD | 3,780,000.00 USD |
| `7D` | `96.50` | 21,210,000.00 USD | 0.00 USD | 21,210,000.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD |
| `1D` | `96.70` | 27,640,000.00 USD | 0.00 USD | 27,640,000.00 USD | 1,420,000.00 USD | 2,230,000.00 USD | 956,820.00 USD |
| `7D` | `96.70` | 21,180,000.00 USD | 0.00 USD | 21,180,000.00 USD | 0.00 USD | 14,450.00 USD | 2,350,000.00 USD |
| `1D` | `96.90` | 23,030,000.00 USD | 0.00 USD | 23,030,000.00 USD | 541,070.00 USD | 1,880,000.00 USD | 4,910,000.00 USD |
| `7D` | `96.90` | 18,820,000.00 USD | 0.00 USD | 18,820,000.00 USD | 0.00 USD | 2,310,000.00 USD | 1,210,000.00 USD |
| `1D` | `97.10` | 15,700,000.00 USD | 0.00 USD | 15,700,000.00 USD | 3,190,000.00 USD | 2,570,000.00 USD | 1,930,000.00 USD |
| `7D` | `97.10` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 0.00 USD | 1,350,000.00 USD | 4,290,000.00 USD |
| `1D` | `97.30` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 1,030,000.00 USD | 1,270,000.00 USD | 873,300.00 USD |
| `7D` | `97.30` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 0.00 USD | 16,130.00 USD | 0.00 USD |
| `1D` | `97.50` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 534,370.00 USD | 1,320,000.00 USD | 1,760,000.00 USD |
| `7D` | `97.50` | 9,650,000.00 USD | 0.00 USD | 9,650,000.00 USD | 0.00 USD | 110,360.00 USD | 0.00 USD |
| `1D` | `97.70` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 1,230,000.00 USD |
| `7D` | `97.70` | 9,540,000.00 USD | 0.00 USD | 9,540,000.00 USD | 3,880,000.00 USD | 1,750,000.00 USD | 3,910,000.00 USD |
| `1D` | `97.90` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 2,400,000.00 USD | 48,560.00 USD | 0.00 USD |
| `1D` | `97.90` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 2,400,000.00 USD | 48,560.00 USD | 0.00 USD |
| `7D` | `97.90` | 13,610,000.00 USD | 13,610,000.00 USD | 0.00 USD | 11,920,000.00 USD | 1,690,000.00 USD | 0.00 USD |
| `7D` | `97.90` | 27,210,000.00 USD | 27,210,000.00 USD | 0.00 USD | 11,920,000.00 USD | 1,690,000.00 USD | 0.00 USD |
| `1D` | `98.10` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 211,100.00 USD | 0.00 USD | 2,810,000.00 USD |
| `7D` | `98.10` | 37,090,000.00 USD | 37,090,000.00 USD | 0.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `98.30` | 15,730,000.00 USD | 15,730,000.00 USD | 0.00 USD | 1,890,000.00 USD | 20,470.00 USD | 5,890,000.00 USD |
| `7D` | `98.30` | 49,490,000.00 USD | 49,490,000.00 USD | 0.00 USD | 1,640,000.00 USD | 5,130,000.00 USD | 5,630,000.00 USD |
| `1D` | `98.50` | 25,900,000.00 USD | 25,900,000.00 USD | 0.00 USD | 295,480.00 USD | 3,460,000.00 USD | 6,420,000.00 USD |
| `7D` | `98.50` | 59,620,000.00 USD | 59,620,000.00 USD | 0.00 USD | 1,320,000.00 USD | 6,930,000.00 USD | 1,880,000.00 USD |
| `1D` | `98.70` | 41,560,000.00 USD | 41,560,000.00 USD | 0.00 USD | 980,300.00 USD | 5,100,000.00 USD | 9,580,000.00 USD |
| `7D` | `98.70` | 64,610,000.00 USD | 64,610,000.00 USD | 0.00 USD | 742,060.00 USD | 1,370,000.00 USD | 2,880,000.00 USD |
| `1D` | `98.90` | 50,160,000.00 USD | 50,160,000.00 USD | 0.00 USD | 1,180,000.00 USD | 3,110,000.00 USD | 4,320,000.00 USD |
| `7D` | `98.90` | 69,460,000.00 USD | 69,460,000.00 USD | 0.00 USD | 57,310.00 USD | 1,660,000.00 USD | 3,120,000.00 USD |
| `1D` | `99.10` | 59,740,000.00 USD | 59,740,000.00 USD | 0.00 USD | 1,710,000.00 USD | 2,910,000.00 USD | 4,950,000.00 USD |
| `7D` | `99.10` | 75,860,000.00 USD | 75,860,000.00 USD | 0.00 USD | 179,190.00 USD | 2,070,000.00 USD | 4,150,000.00 USD |
| `1D` | `99.30` | 68,660,000.00 USD | 68,660,000.00 USD | 0.00 USD | 3,350,000.00 USD | 3,300,000.00 USD | 2,270,000.00 USD |
| `7D` | `99.30` | 82,610,000.00 USD | 82,610,000.00 USD | 0.00 USD | 798,000.00 USD | 3,060,000.00 USD | 2,890,000.00 USD |
| `1D` | `99.50` | 73,950,000.00 USD | 73,950,000.00 USD | 0.00 USD | 1,380,000.00 USD | 3,290,000.00 USD | 619,030.00 USD |
| `7D` | `99.50` | 86,850,000.00 USD | 86,850,000.00 USD | 0.00 USD | 2,240,000.00 USD | 1,490,000.00 USD | 504,960.00 USD |
| `1D` | `99.70` | 96,880,000.00 USD | 96,880,000.00 USD | 0.00 USD | 4,390,000.00 USD | 7,340,000.00 USD | 11,210,000.00 USD |
| `7D` | `99.70` | 90,610,000.00 USD | 90,610,000.00 USD | 0.00 USD | 0.00 USD | 2,490,000.00 USD | 1,270,000.00 USD |
| `1D` | `99.90` | 105,430,000.00 USD | 105,430,000.00 USD | 0.00 USD | 825,740.00 USD | 1,760,000.00 USD | 5,960,000.00 USD |
| `7D` | `99.90` | 98,740,000.00 USD | 98,740,000.00 USD | 0.00 USD | 2,860,000.00 USD | 1,420,000.00 USD | 3,850,000.00 USD |
| `1D` | `100.10` | 110,690,000.00 USD | 110,690,000.00 USD | 0.00 USD | 2,030,000.00 USD | 2,360,000.00 USD | 877,830.00 USD |
| `7D` | `100.10` | 104,530,000.00 USD | 104,530,000.00 USD | 0.00 USD | 48,160.00 USD | 1,210,000.00 USD | 4,520,000.00 USD |
| `1D` | `100.30` | 115,820,000.00 USD | 115,820,000.00 USD | 0.00 USD | 300,700.00 USD | 2,120,000.00 USD | 2,710,000.00 USD |
| `7D` | `100.30` | 108,140,000.00 USD | 108,140,000.00 USD | 0.00 USD | 883,050.00 USD | 1,600,000.00 USD | 1,130,000.00 USD |
| `1D` | `100.50` | 123,470,000.00 USD | 123,470,000.00 USD | 0.00 USD | 2,200,000.00 USD | 1,260,000.00 USD | 4,200,000.00 USD |
| `7D` | `100.50` | 116,600,000.00 USD | 116,600,000.00 USD | 0.00 USD | 2,640,000.00 USD | 765,300.00 USD | 5,050,000.00 USD |
| `1D` | `100.70` | 130,790,000.00 USD | 130,790,000.00 USD | 0.00 USD | 1,940,000.00 USD | 2,250,000.00 USD | 3,130,000.00 USD |
| `7D` | `100.70` | 119,020,000.00 USD | 119,020,000.00 USD | 0.00 USD | 504,370.00 USD | 1,900,000.00 USD | 23,970.00 USD |
| `1D` | `100.90` | 136,740,000.00 USD | 136,740,000.00 USD | 0.00 USD | 1,760,000.00 USD | 2,410,000.00 USD | 1,790,000.00 USD |
| `7D` | `100.90` | 132,120,000.00 USD | 132,120,000.00 USD | 0.00 USD | 3,480,000.00 USD | 3,730,000.00 USD | 5,890,000.00 USD |
| `1D` | `101.10` | 150,610,000.00 USD | 150,610,000.00 USD | 0.00 USD | 8,660,000.00 USD | 2,680,000.00 USD | 2,520,000.00 USD |
| `7D` | `101.10` | 141,890,000.00 USD | 141,890,000.00 USD | 0.00 USD | 3,020,000.00 USD | 3,990,000.00 USD | 2,760,000.00 USD |
| `1D` | `101.30` | 160,810,000.00 USD | 160,810,000.00 USD | 0.00 USD | 3,460,000.00 USD | 3,950,000.00 USD | 2,800,000.00 USD |
| `7D` | `101.30` | 163,270,000.00 USD | 163,270,000.00 USD | 0.00 USD | 7,710,000.00 USD | 4,690,000.00 USD | 8,980,000.00 USD |
| `1D` | `101.50` | 176,960,000.00 USD | 176,960,000.00 USD | 0.00 USD | 3,050,000.00 USD | 3,960,000.00 USD | 9,140,000.00 USD |
| `7D` | `101.50` | 178,540,000.00 USD | 178,540,000.00 USD | 0.00 USD | 2,950,000.00 USD | 738,480.00 USD | 11,580,000.00 USD |
| `1D` | `101.70` | 186,830,000.00 USD | 186,830,000.00 USD | 0.00 USD | 2,320,000.00 USD | 841,470.00 USD | 6,710,000.00 USD |
| `7D` | `101.70` | 188,540,000.00 USD | 188,540,000.00 USD | 0.00 USD | 2,950,000.00 USD | 484,140.00 USD | 6,570,000.00 USD |
| `1D` | `101.90` | 192,540,000.00 USD | 192,540,000.00 USD | 0.00 USD | 2,230,000.00 USD | 823,320.00 USD | 2,650,000.00 USD |
| `7D` | `101.90` | 197,250,000.00 USD | 197,250,000.00 USD | 0.00 USD | 3,710,000.00 USD | 867,880.00 USD | 4,120,000.00 USD |
| `1D` | `102.10` | 198,540,000.00 USD | 198,540,000.00 USD | 0.00 USD | 2,830,000.00 USD | 1,270,000.00 USD | 1,900,000.00 USD |
| `7D` | `102.10` | 202,900,000.00 USD | 202,900,000.00 USD | 0.00 USD | 1,470,000.00 USD | 159,070.00 USD | 4,030,000.00 USD |
| `1D` | `102.30` | 203,270,000.00 USD | 203,270,000.00 USD | 0.00 USD | 1,650,000.00 USD | 1,450,000.00 USD | 1,630,000.00 USD |
| `7D` | `102.30` | 208,960,000.00 USD | 208,960,000.00 USD | 0.00 USD | 2,700,000.00 USD | 807,930.00 USD | 2,550,000.00 USD |
| `1D` | `102.50` | 207,600,000.00 USD | 207,600,000.00 USD | 0.00 USD | 1,510,000.00 USD | 785,070.00 USD | 2,030,000.00 USD |
| `7D` | `102.50` | 212,610,000.00 USD | 212,610,000.00 USD | 0.00 USD | 1,240,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD |
| `1D` | `102.70` | 209,490,000.00 USD | 209,490,000.00 USD | 0.00 USD | 1,110,000.00 USD | 661,840.00 USD | 121,020.00 USD |
| `7D` | `102.70` | 213,410,000.00 USD | 213,410,000.00 USD | 0.00 USD | 766,460.00 USD | 14,010.00 USD | 16,660.00 USD |
| `1D` | `102.90` | 214,020,000.00 USD | 214,020,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,530,000.00 USD | 1,490,000.00 USD |
| `7D` | `102.90` | 234,690,000.00 USD | 234,690,000.00 USD | 0.00 USD | 17,210,000.00 USD | 294,050.00 USD | 3,780,000.00 USD |
| `1D` | `103.10` | 218,980,000.00 USD | 218,980,000.00 USD | 0.00 USD | 2,380,000.00 USD | 1,360,000.00 USD | 1,220,000.00 USD |
| `7D` | `103.10` | 240,930,000.00 USD | 240,930,000.00 USD | 0.00 USD | 4,750,000.00 USD | 140,720.00 USD | 1,340,000.00 USD |
| `1D` | `103.30` | 220,800,000.00 USD | 220,800,000.00 USD | 0.00 USD | 334,720.00 USD | 717,010.00 USD | 769,510.00 USD |
| `7D` | `103.30` | 256,610,000.00 USD | 256,610,000.00 USD | 0.00 USD | 15,130,000.00 USD | 133,780.00 USD | 417,110.00 USD |
| `1D` | `103.50` | 227,390,000.00 USD | 227,390,000.00 USD | 0.00 USD | 1,770,000.00 USD | 1,090,000.00 USD | 3,730,000.00 USD |
| `7D` | `103.50` | 279,020,000.00 USD | 279,020,000.00 USD | 0.00 USD | 13,780,000.00 USD | 1,770,000.00 USD | 6,860,000.00 USD |
| `1D` | `103.70` | 232,590,000.00 USD | 232,590,000.00 USD | 0.00 USD | 1,610,000.00 USD | 971,510.00 USD | 2,620,000.00 USD |
| `7D` | `103.70` | 291,240,000.00 USD | 291,240,000.00 USD | 0.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD |
| `1D` | `103.90` | 238,400,000.00 USD | 238,400,000.00 USD | 0.00 USD | 2,080,000.00 USD | 2,200,000.00 USD | 1,530,000.00 USD |
| `7D` | `103.90` | 309,270,000.00 USD | 309,270,000.00 USD | 0.00 USD | 9,120,000.00 USD | 2,880,000.00 USD | 6,040,000.00 USD |
| `1D` | `104.10` | 245,500,000.00 USD | 245,500,000.00 USD | 0.00 USD | 2,840,000.00 USD | 1,270,000.00 USD | 2,990,000.00 USD |
| `7D` | `104.10` | 338,200,000.00 USD | 338,200,000.00 USD | 0.00 USD | 11,570,000.00 USD | 8,350,000.00 USD | 9,010,000.00 USD |
| `1D` | `104.30` | 249,190,000.00 USD | 249,190,000.00 USD | 0.00 USD | 1,350,000.00 USD | 1,350,000.00 USD | 984,790.00 USD |
| `7D` | `104.30` | 359,780,000.00 USD | 359,780,000.00 USD | 0.00 USD | 7,320,000.00 USD | 6,380,000.00 USD | 7,870,000.00 USD |
| `1D` | `104.50` | 253,200,000.00 USD | 253,200,000.00 USD | 0.00 USD | 1,430,000.00 USD | 1,220,000.00 USD | 1,360,000.00 USD |
| `7D` | `104.50` | 371,810,000.00 USD | 371,810,000.00 USD | 0.00 USD | 4,410,000.00 USD | 2,350,000.00 USD | 5,270,000.00 USD |
| `1D` | `104.70` | 258,990,000.00 USD | 258,990,000.00 USD | 0.00 USD | 1,720,000.00 USD | 982,920.00 USD | 3,090,000.00 USD |
| `7D` | `104.70` | 392,000,000.00 USD | 392,000,000.00 USD | 0.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,860,000.00 USD |
| `1D` | `104.90` | 260,470,000.00 USD | 260,470,000.00 USD | 0.00 USD | 486,940.00 USD | 283,560.00 USD | 706,500.00 USD |
| `7D` | `104.90` | 412,860,000.00 USD | 412,860,000.00 USD | 0.00 USD | 5,970,000.00 USD | 5,350,000.00 USD | 9,550,000.00 USD |
| `1D` | `105.10` | 262,300,000.00 USD | 262,300,000.00 USD | 0.00 USD | 299,230.00 USD | 436,680.00 USD | 1,100,000.00 USD |
| `7D` | `105.10` | 425,670,000.00 USD | 425,670,000.00 USD | 0.00 USD | 5,580,000.00 USD | 4,400,000.00 USD | 2,830,000.00 USD |
| `1D` | `105.30` | 262,490,000.00 USD | 262,490,000.00 USD | 0.00 USD | 94,380.00 USD | 96,460.00 USD | 1,240.00 USD |
| `7D` | `105.30` | 430,010,000.00 USD | 430,010,000.00 USD | 0.00 USD | 2,410,000.00 USD | 1,310,000.00 USD | 623,960.00 USD |
| `1D` | `105.50` | 263,110,000.00 USD | 263,110,000.00 USD | 0.00 USD | 245,610.00 USD | 180,000.00 USD | 186,400.00 USD |
| `7D` | `105.50` | 447,780,000.00 USD | 447,780,000.00 USD | 0.00 USD | 5,600,000.00 USD | 5,850,000.00 USD | 6,320,000.00 USD |
| `1D` | `105.70` | 263,320,000.00 USD | 263,320,000.00 USD | 0.00 USD | 65,040.00 USD | 150,210.00 USD | 3,480.00 USD |
| `7D` | `105.70` | 459,530,000.00 USD | 459,530,000.00 USD | 0.00 USD | 3,430,000.00 USD | 3,740,000.00 USD | 4,570,000.00 USD |
| `1D` | `105.90` | 264,370,000.00 USD | 264,370,000.00 USD | 0.00 USD | 171,160.00 USD | 683,690.00 USD | 193,630.00 USD |
| `7D` | `105.90` | 468,420,000.00 USD | 468,420,000.00 USD | 0.00 USD | 3,110,000.00 USD | 1,880,000.00 USD | 3,900,000.00 USD |
| `1D` | `106.10` | 265,760,000.00 USD | 265,760,000.00 USD | 0.00 USD | 706,860.00 USD | 457,510.00 USD | 226,230.00 USD |
| `7D` | `106.10` | 479,020,000.00 USD | 479,020,000.00 USD | 0.00 USD | 4,910,000.00 USD | 2,870,000.00 USD | 2,820,000.00 USD |
| `1D` | `106.30` | 266,920,000.00 USD | 266,920,000.00 USD | 0.00 USD | 281,270.00 USD | 484,380.00 USD | 391,880.00 USD |
| `7D` | `106.30` | 487,420,000.00 USD | 487,420,000.00 USD | 0.00 USD | 3,400,000.00 USD | 2,850,000.00 USD | 2,150,000.00 USD |
| `1D` | `106.50` | 267,610,000.00 USD | 267,610,000.00 USD | 0.00 USD | 229,790.00 USD | 216,810.00 USD | 239,170.00 USD |
| `7D` | `106.50` | 491,820,000.00 USD | 491,820,000.00 USD | 0.00 USD | 1,520,000.00 USD | 1,440,000.00 USD | 1,450,000.00 USD |
| `1D` | `106.70` | 269,740,000.00 USD | 269,740,000.00 USD | 0.00 USD | 565,590.00 USD | 249,950.00 USD | 1,320,000.00 USD |
| `7D` | `106.70` | 499,910,000.00 USD | 499,910,000.00 USD | 0.00 USD | 1,820,000.00 USD | 2,330,000.00 USD | 3,940,000.00 USD |
| `1D` | `106.90` | 270,210,000.00 USD | 270,210,000.00 USD | 0.00 USD | 10,160.00 USD | 156,020.00 USD | 305,180.00 USD |
| `7D` | `106.90` | 504,970,000.00 USD | 504,970,000.00 USD | 0.00 USD | 789,400.00 USD | 1,150,000.00 USD | 3,120,000.00 USD |
| `1D` | `107.10` | 271,250,000.00 USD | 271,250,000.00 USD | 0.00 USD | 97,170.00 USD | 366,280.00 USD | 580,410.00 USD |
| `7D` | `107.10` | 509,080,000.00 USD | 509,080,000.00 USD | 0.00 USD | 1,630,000.00 USD | 799,480.00 USD | 1,680,000.00 USD |
| `1D` | `107.30` | 271,620,000.00 USD | 271,620,000.00 USD | 0.00 USD | 82,550.00 USD | 174,420.00 USD | 110,290.00 USD |
| `7D` | `107.30` | 509,530,000.00 USD | 509,530,000.00 USD | 0.00 USD | 0.00 USD | 451,690.00 USD | 0.00 USD |
| `1D` | `107.50` | 272,740,000.00 USD | 272,740,000.00 USD | 0.00 USD | 50,930.00 USD | 253,000.00 USD | 815,630.00 USD |
| `7D` | `107.50` | 510,780,000.00 USD | 510,780,000.00 USD | 0.00 USD | 5,920.00 USD | 286,950.00 USD | 954,810.00 USD |
| `1D` | `107.70` | 273,020,000.00 USD | 273,020,000.00 USD | 0.00 USD | 54,110.00 USD | 0.00 USD | 230,360.00 USD |
| `7D` | `107.70` | 511,760,000.00 USD | 511,760,000.00 USD | 0.00 USD | 523,660.00 USD | 10,400.00 USD | 444,980.00 USD |
| `1D` | `107.90` | 273,320,000.00 USD | 273,320,000.00 USD | 0.00 USD | 83,370.00 USD | 73,830.00 USD | 136,810.00 USD |
| `7D` | `107.90` | 512,280,000.00 USD | 512,280,000.00 USD | 0.00 USD | 173,590.00 USD | 20,610.00 USD | 331,480.00 USD |
| `1D` | `108.10` | 273,420,000.00 USD | 273,420,000.00 USD | 0.00 USD | 0.00 USD | 99,900.00 USD | 1,320.00 USD |
| `7D` | `108.10` | 512,540,000.00 USD | 512,540,000.00 USD | 0.00 USD | 5,950.00 USD | 248,110.00 USD | 7,130.00 USD |
| `1D` | `108.30` | 273,450,000.00 USD | 273,450,000.00 USD | 0.00 USD | 33,880.00 USD | 1,950.00 USD | 0.00 USD |
| `7D` | `108.30` | 513,670,000.00 USD | 513,670,000.00 USD | 0.00 USD | 303,300.00 USD | 464,990.00 USD | 359,500.00 USD |
| `1D` | `108.50` | 274,150,000.00 USD | 274,150,000.00 USD | 0.00 USD | 163,220.00 USD | 120,280.00 USD | 413,910.00 USD |
| `7D` | `108.50` | 514,070,000.00 USD | 514,070,000.00 USD | 0.00 USD | 395,570.00 USD | 3,960.00 USD | 2,900.00 USD |
| `1D` | `108.60` | 274,270,000.00 USD | 274,270,000.00 USD | 0.00 USD | 118,190.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `108.70` | 515,800,000.00 USD | 515,800,000.00 USD | 0.00 USD | 557,190.00 USD | 529,990.00 USD | 640,060.00 USD |
| `7D` | `108.90` | 517,240,000.00 USD | 517,240,000.00 USD | 0.00 USD | 363,550.00 USD | 494,000.00 USD | 580,220.00 USD |
| `7D` | `109.10` | 518,070,000.00 USD | 518,070,000.00 USD | 0.00 USD | 289,830.00 USD | 185,250.00 USD | 354,460.00 USD |
| `7D` | `109.30` | 519,230,000.00 USD | 519,230,000.00 USD | 0.00 USD | 503,000.00 USD | 91,380.00 USD | 569,620.00 USD |
| `7D` | `109.50` | 519,470,000.00 USD | 519,470,000.00 USD | 0.00 USD | 230,320.00 USD | 4,290.00 USD | 5,670.00 USD |
| `7D` | `109.70` | 520,650,000.00 USD | 520,650,000.00 USD | 0.00 USD | 550,380.00 USD | 185,990.00 USD | 444,420.00 USD |
| `7D` | `109.90` | 522,450,000.00 USD | 522,450,000.00 USD | 0.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD |
| `7D` | `110.10` | 524,820,000.00 USD | 524,820,000.00 USD | 0.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD |
| `7D` | `110.30` | 526,880,000.00 USD | 526,880,000.00 USD | 0.00 USD | 936,750.00 USD | 321,390.00 USD | 800,250.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `5.71B` | Total OI Tokens: `58,263,195.6 SOL`
  * 1h OI Change: `-0.54%` | 4h OI Change: `-1.47%` | 24h OI Change: `-10.83%`
  * Exchange Breakdown: Binance=`984.16M` | Bybit=`631.25M` | OKX=`396.09M` | Hyperliquid=`529.68M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-138.47K` | Last 24h: `286.77K` | Last 3d: `1.17M` | Last 7d: `2.35M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0045%` | **USDT OKX** | `-0.0292%` |
| **USDT Bybit** | `-0.0130%` | **USDT KuCoin** | `-0.0077%` |
| **USDT MEXC** | `0.0046%` | **USDT BingX** | `0.0047%` |
| **USDT Gate** | `-0.0122%` | **USDT Bitget** | `-0.0072%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `55.36%` | `44.64%` | `1.24` | 448,070,000.00 USD |
| `15M` | `Binance` | `58.27%` | `41.73%` | `1.40` | 160,330,000.00 USD |
| `15M` | `OKX` | `54.36%` | `45.64%` | `1.19` | 92,830,000.00 USD |
| `15M` | `Bybit` | `33.66%` | `66.34%` | `0.51` | 30,870,000.00 USD |
| `15M` | `KuCoin` | `51.74%` | `48.26%` | `1.07` | 733,820.00 USD |
| `15M` | `Gate` | `53.87%` | `46.13%` | `1.17` | 73,810,000.00 USD |
| `15M` | `Bitget` | `47.83%` | `52.17%` | `0.92` | 14,200,000.00 USD |
| `15M` | `BingX` | `68.08%` | `31.92%` | `2.13` | 4,640,000.00 USD |
| `15M` | `MEXC` | `59.73%` | `40.27%` | `1.48` | 19,810,000.00 USD |
| `15M` | `Bitunix` | `54.77%` | `45.23%` | `1.21` | 15,630,000.00 USD |
| `15M` | `Hyperliquid` | `91.14%` | `8.86%` | `10.29` | 15,810,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.74%` | `50.26%` | `0.99` | 2,440,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `63.55%` | `36.45%` | `1.74` | 90,210.00 USD |
| `15M` | `HTX` | `64.17%` | `35.83%` | `1.79` | 3,330,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `70.02%` | `29.98%` | `2.34` | 2,160,000.00 USD |
| `15M` | `Bitfinex` | `7.43%` | `92.57%` | `0.08` | 201,550.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `43.94%` | `56.06%` | `0.78` | 2,750,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `32.26%` | `67.74%` | `0.48` | 8,410,000.00 USD |
| `15M` | `Whale Positions` | `58.27%` | `41.73%` | `1.40` | 160,330,000.00 USD |
| `15M` | `Global Accounts` | `55.36%` | `44.64%` | `1.24` | 448,070,000.00 USD |
| `1H` | `SOL` | `48.06%` | `51.94%` | `0.93` | 1,340,000,000.00 USD |
| `1H` | `Binance` | `51.34%` | `48.66%` | `1.06` | 458,410,000.00 USD |
| `1H` | `OKX` | `43.78%` | `56.22%` | `0.78` | 271,900,000.00 USD |
| `1H` | `Bybit` | `39.88%` | `60.12%` | `0.66` | 102,760,000.00 USD |
| `1H` | `KuCoin` | `47.21%` | `52.79%` | `0.89` | 4,390,000.00 USD |
| `1H` | `Gate` | `50.49%` | `49.51%` | `1.02` | 222,180,000.00 USD |
| `1H` | `Bitget` | `40.97%` | `59.03%` | `0.69` | 63,850,000.00 USD |
| `1H` | `BingX` | `40.12%` | `59.88%` | `0.67` | 16,690,000.00 USD |
| `1H` | `MEXC` | `52.19%` | `47.81%` | `1.09` | 45,830,000.00 USD |
| `1H` | `Bitunix` | `51.68%` | `48.32%` | `1.07` | 46,920,000.00 USD |
| `1H` | `Hyperliquid` | `56.35%` | `43.65%` | `1.29` | 36,090,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.34%` | `45.66%` | `1.19` | 6,410,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `1.01%` | `98.99%` | `0.01` | 9,220,000.00 USD |
| `1H` | `HTX` | `72.68%` | `27.32%` | `2.66` | 16,980,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `58.03%` | `41.97%` | `1.38` | 9,100,000.00 USD |
| `1H` | `Bitfinex` | `12.57%` | `87.43%` | `0.14` | 583,050.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `42.57%` | `57.43%` | `0.74` | 9,400,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `40.54%` | `59.46%` | `0.68` | 19,280,000.00 USD |
| `1H` | `Whale Positions` | `51.34%` | `48.66%` | `1.06` | 458,410,000.00 USD |
| `1H` | `Global Accounts` | `48.06%` | `51.94%` | `0.93` | 1,340,000,000.00 USD |
| `4H` | `SOL` | `55.14%` | `44.86%` | `1.23` | 569,990,000.00 USD |
| `4H` | `Binance` | `54.64%` | `45.36%` | `1.20` | 193,840,000.00 USD |
| `4H` | `OKX` | `51.22%` | `48.78%` | `1.05` | 71,320,000.00 USD |
| `4H` | `Bybit` | `56.92%` | `43.08%` | `1.32` | 94,750,000.00 USD |
| `4H` | `KuCoin` | `48.62%` | `51.38%` | `0.95` | 5,670,000.00 USD |
| `4H` | `Gate` | `57.14%` | `42.86%` | `1.33` | 22,310,000.00 USD |
| `4H` | `Bitget` | `54.61%` | `45.39%` | `1.20` | 36,420,000.00 USD |
| `4H` | `BingX` | `43.51%` | `56.49%` | `0.77` | 14,110,000.00 USD |
| `4H` | `MEXC` | `54.74%` | `45.26%` | `1.21` | 79,940,000.00 USD |
| `4H` | `Bitunix` | `53.64%` | `46.36%` | `1.16` | 17,600,000.00 USD |
| `4H` | `Hyperliquid` | `63.6%` | `36.4%` | `1.75` | 18,270,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `63.51%` | `36.49%` | `1.74` | 2,470,000.00 USD |
| `4H` | `Crypto.com` | `55.64%` | `44.36%` | `1.25` | 907,150.00 USD |
| `4H` | `WhiteBIT` | `93.76%` | `6.24%` | `15.03` | 6,800,000.00 USD |
| `4H` | `HTX` | `42.78%` | `57.22%` | `0.75` | 511,920.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `40.45%` | `59.55%` | `0.68` | 20,120.00 USD |
| `4H` | `Aster` | `45.98%` | `54.02%` | `0.85` | 2,910,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `73.46%` | `26.54%` | `2.77` | 2,120,000.00 USD |
| `4H` | `Whale Positions` | `54.64%` | `45.36%` | `1.20` | 193,840,000.00 USD |
| `4H` | `Global Accounts` | `55.14%` | `44.86%` | `1.23` | 569,990,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `97.05` | `97.07` | `97.05` | `97.23` | `96.88` | 23,273,914.74 USD | 12,919,268.61 USD | 10,354,646.13 USD | 2,564,622.48 USD | `+11.02%` | `2B / 3S` |
| `0:00 UTC` | `97.00` | `96.93` | `97.00` | `97.28` | `96.72` | 29,456,364.14 USD | 16,744,830.08 USD | 12,711,534.06 USD | 4,033,296.02 USD | `+13.69%` | `9B / 4S` |
| `5:00 UTC` | `97.16` | `97.32` | `97.16` | `97.62` | `97.06` | 19,813,374.49 USD | 9,462,479.38 USD | 10,350,895.11 USD | -888,415.74 USD | `-4.48%` | `5B / 3S` |
| `0:00 UTC` | `97.27` | `97.32` | `97.27` | `97.50` | `97.16` | 16,828,074.52 USD | 7,221,424.98 USD | 9,606,649.54 USD | -2,385,224.56 USD | `-14.17%` | `3B / 6S` |
| `5:00 UTC` | `97.34` | `97.32` | `97.34` | `97.41` | `97.22` | 11,924,438.31 USD | 5,221,368.03 USD | 6,703,070.27 USD | -1,481,702.24 USD | `-12.43%` | `0B / 0S` |
| `0:00 UTC` | `97.75` | `97.66` | `97.75` | `98.00` | `97.20` | 26,397,725.62 USD | 14,040,862.52 USD | 12,356,863.09 USD | 1,683,999.43 USD | `+6.38%` | `10B / 3S` |
| `5:00 UTC` | `98.00` | `97.90` | `98.00` | `98.06` | `97.68` | 15,892,962.27 USD | 7,229,090.33 USD | 8,663,871.94 USD | -1,434,781.61 USD | `-9.03%` | `2B / 4S` |
| `0:00 UTC` | `98.22` | `98.16` | `98.22` | `98.35` | `97.88` | 18,936,666.93 USD | 8,858,429.68 USD | 10,078,237.25 USD | -1,219,807.57 USD | `-6.44%` | `5B / 6S` |
| `5:00 UTC` | `98.05` | `98.14` | `98.05` | `98.55` | `97.84` | 22,589,286.35 USD | 8,455,263.03 USD | 14,134,023.31 USD | -5,678,760.28 USD | `-25.14%` | `6B / 22S` |
| `0:00 UTC` | `98.00` | `97.89` | `98.00` | `98.06` | `97.75` | 12,986,186.38 USD | 6,179,286.71 USD | 6,806,899.67 USD | -627,612.95 USD | `-4.83%` | `3B / 4S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 18:37` | `Volume 500K SOL` | `Divergence` | **`BULLISH`** | Drop without taker selling | `101.13` | 0.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 500K SOL` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `101.76` | 0.00 USD | 0.00 USD |
| `10-28 15:32` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `102.87` | 99,000.00 USD | 0.00 USD |
| `10-28 13:57` | `Volume 500K SOL` | `Divergence` | **`BULLISH`** | Drop without taker selling | `102.88` | 0.00 USD | 0.00 USD |
| `10-28 13:30` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `102.22` | 103,000.00 USD | 0.00 USD |
| `10-28 10:59` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `101.76` | 110,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 143,110.00 USD | 1,610,000.00 USD | **`ACCUMULATION`** |
| `15m` | -1,350,000.00 USD | -457,800.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,510,000.00 USD | -15,200,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -678,930.00 USD | -17,010,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 2,760,000.00 USD | -13,820,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 6,800,000.00 USD | 37,490,000.00 USD | **`ACCUMULATION`** |
| `6h` | 7,650,000.00 USD | -33,550,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -18,510,000.00 USD | -215,930,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -60,820,000.00 USD | -363,530,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -37,280,000.00 USD | -407,670,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 31,420,000.00 USD | -677,020,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 1,440,000.00 USD | -2,180,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+143.11K` | 15m=`-1.35M` | 1h=`-678.93K` | 24h=`-37.28M`
* Futures Capital Netflows: 5m=`+1.61M` | 15m=`-457.80K` | 1h=`-17.01M` | 24h=`-407.67M`
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
  * Execution Entry: `94.53` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `93.27` (Risk Distance: `1.26` pts)
  * +2.5R Take Profit: `97.67`
  * Mathematical Lot Sizing: **`7.95 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `97.79` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `99.05` (Risk Distance: `1.26` pts)
  * +2.5R Take Profit: `94.65`
  * Mathematical Lot Sizing: **`7.95 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`98.58`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
