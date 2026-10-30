# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 15:42:18 IST` (`2026-10-30 10:12:18 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `96.16` | **Live Ask Quote**: `96.38` | **Mid Price**: `96.27`
- **Spread Points**: `22.00` | **Spread BPS**: `22.85 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `95.72` | VWAP Z-Score: `+0.51` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.5837` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `44.56` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `100.57` | Lower -3.00σ Band: `90.88`
  * Upper +2.51σ Band: `99.78` | Lower -2.51σ Band: `91.67`
  * Upper +2.01σ Band: `98.97` | Lower -2.01σ Band: `92.47`
  * Upper +2.00σ Band: `98.95` | Lower -2.00σ Band: `92.49`
  * Upper +1.28σ Band: `97.79` | Lower -1.28σ Band: `93.65`
  * Upper +1.00σ Band: `97.34` | Lower -1.00σ Band: `94.11`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`96.85` | EMA-20=`96.92` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`97.08` (Slope: `+0.0000`) | EMA-100=`97.89`
  * Institutional Anchors: EMA-144=`98.44` | EMA-200=`98.97` (Slope: `-0.2575`) | EMA-233=`99.19`
- **Range Boundaries**: 24H High=`102.93` | 24H Low=`91.86` | Weekly High=`103.63` | Weekly Low=`91.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `98.09` (Distance: `-1.86%`)
  * Point of Control (POC) = `96.89` (Distance: `-0.64%`)
  * Value Area Low (VAL) = `95.13` (Distance: `+1.19%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`101.56` | POC=`99.94` | VAL=`98.94`
  * Prior Day Extremes: PDH=`102.93` | PDL=`94.56` | PDC=`95.94`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`102.10` | Weekly POC=`100.92` | Weekly VAL=`99.51`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`97.84` | Low=`91.86`
  * London Session (08:00-16:00 UTC): High=`98.28` | Low=`95.96`
  * New York Session (13:00-21:00 UTC): High=`96.67` | Low=`95.96`
  * Initial Balance (First Hour): IB High=`98.28` | IB Low=`96.72`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `95.88` - `96.66`
  * Optimal Trade Entry (OTE 0.705): `96.46`
  * Structural Invalidation Anchor (0.786): `97.04`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `96.98` | `97.01` | `96.77` | `96.95` | `45,495` | 4,408,108.96 USD | 940,591.70 USD | `+21.34%` | -223,893,243.23 USD | `+1.09` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `96.95` | `96.95` | `96.73` | `96.83` | `26,079` | 2,525,030.35 USD | 6,223.45 USD | `+0.25%` | -223,887,019.77 USD | `+0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `96.83` | `96.87` | `96.73` | `96.84` | `30,139` | 2,917,412.41 USD | 211,709.17 USD | `+7.26%` | -223,675,310.61 USD | `+0.46` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `96.91` | `97.15` | `96.68` | `96.99` | `154,066` | 14,931,632.13 USD | 1,124,750.63 USD | `+7.53%` | -224,047,574.27 USD | `+1.20` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `96.98` | `97.01` | `96.73` | `96.83` | `102,000` | 9,878,254.59 USD | 1,145,851.02 USD | `+11.60%` | -222,901,723.25 USD | `+1.10` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `96.84` | `96.84` | `96.30` | `96.42` | `164,310` | 15,850,528.83 USD | -1,125,145.76 USD | `-7.10%` | -224,026,869.01 USD | `+0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `97.28` | `97.55` | `96.84` | `97.33` | `564,307` | 54,855,982.25 USD | -1,256,866.37 USD | `-2.29%` | -217,296,468.21 USD | `+0.46` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `97.34` | `97.44` | `96.68` | `96.83` | `564,041` | 54,709,052.00 USD | -2,626,000.84 USD | `-4.80%` | -219,922,469.04 USD | `+0.40` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `96.84` | `96.84` | `96.30` | `96.42` | `164,310` | 15,850,528.83 USD | -1,125,145.76 USD | `-7.10%` | -221,047,614.81 USD | `+0.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -192,935,382.59 USD | `+0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.54` | `96.72` | `97.28` | `3,030,040` | 295,921,356.18 USD | -16,839,868.63 USD | `-5.69%` | -209,775,251.22 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.28` | `97.55` | `96.68` | `96.84` | `1,127,790` | 109,510,965.18 USD | -3,850,891.22 USD | `-3.52%` | -213,626,142.44 USD | `+0.82` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -33,800,710.11 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `95.62` | `13,887,188` | 1,349,343,315.53 USD | -115,873,425.65 USD | `-8.59%` | -149,674,135.76 USD | `-1.37` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -192,935,382.59 USD | `+0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.54` | `96.72` | `97.28` | `3,030,040` | 295,921,356.18 USD | -16,839,868.63 USD | `-5.69%` | -209,775,251.22 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.28` | `97.55` | `96.30` | `96.43` | `1,292,449` | 125,395,307.17 USD | -4,987,757.06 USD | `-3.98%` | -214,763,008.28 USD | `+0.80` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`96.27`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `96.36` | `2119.3900` | 204,235.02 USD | 456,016.96 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `96.36` | `41.5000` | 3,999.11 USD | 460,016.07 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `96.36` | `1938.0100` | 186,752.46 USD | 646,768.53 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `96.36` | `371.1800` | 35,767.65 USD | 682,536.17 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `96.36` | `456.4900` | 43,987.83 USD | 726,524.01 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `96.37` | `93.1100` | 8,973.29 USD | 103,000.03 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `96.37` | `249.0200` | 23,998.56 USD | 126,998.59 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `96.37` | `41.5000` | 3,999.40 USD | 130,997.98 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `96.37` | `1087.3400` | 104,786.96 USD | 235,784.94 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `96.37` | `41.5000` | 3,999.31 USD | 239,784.25 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `96.37` | `41.5000` | 3,999.27 USD | 243,783.52 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `96.37` | `41.5000` | 3,999.23 USD | 247,782.76 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `96.37` | `41.5000` | 3,999.19 USD | 251,781.94 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `96.38` | `93.1100` | 8,974.13 USD | 25,063.34 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `96.38` | `171.1900` | 16,499.29 USD | 41,562.63 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `96.38` | `451.2600` | 43,490.63 USD | 85,053.27 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `96.38` | `93.1100` | 8,973.48 USD | 94,026.74 USD | `1 orders` | `-0.02%` | `-` |
| `ASK` | `96.39` | `178.3000` | 17,186.69 USD | 40,968.28 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `96.39` | `246.7200` | 23,781.59 USD | 23,781.59 USD | `6 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `96.39` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 96.39` | `0.00%` | `-` |
| `BID` | `96.39` | `125.3100` | 12,078.63 USD | 12,078.63 USD | `5 orders` | `-0.00%` | `-` |
| `BID` | `96.39` | `0.1200` | 11.57 USD | 12,090.20 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `96.39` | `41.4900` | 3,999.01 USD | 16,089.21 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `96.40` | `69.8300` | 6,731.75 USD | 76,231.65 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `96.40` | `200.9000` | 19,366.96 USD | 69,499.90 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `96.40` | `1.9600` | 188.94 USD | 50,132.94 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `96.40` | `93.1100` | 8,975.71 USD | 49,943.99 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `96.41` | `10.0000` | 964.14 USD | 321,374.71 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.41` | `1896.5100` | 182,848.22 USD | 320,410.57 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.41` | `392.6300` | 37,854.24 USD | 137,562.36 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.41` | `23.8100` | 2,295.55 USD | 99,708.11 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.41` | `0.2100` | 20.25 USD | 97,412.57 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.41` | `172.8500` | 16,664.30 USD | 97,392.32 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.41` | `46.6400` | 4,496.38 USD | 80,728.02 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.42` | `92.5800` | 8,926.84 USD | 532,223.64 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `96.42` | `1051.6600` | 101,403.16 USD | 523,296.80 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `96.42` | `0.1100` | 10.61 USD | 421,893.64 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `96.42` | `807.2200` | 77,832.15 USD | 421,883.04 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `96.42` | `93.0200` | 8,968.80 USD | 344,050.88 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `96.42` | `46.6400` | 4,496.84 USD | 335,082.08 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `96.42` | `95.5300` | 9,210.52 USD | 330,585.24 USD | `2 orders` | `+0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:40:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `11` | `0x5b5d...c060` | `SHORT` | 67,408,792.79 USD | `696,120.13` | `94.33` | `96.56` | `312.85` | -1,740,526.57 USD | `-2.58%` | `7X Cross` |
| `19` | `0x9c6a...a4ed` | `LONG` | 53,157,723.92 USD | `550,087.69` | `80.86` | `96.56` | `68.18` | 8,678,737.53 USD | `+16.33%` | `20X Cross` |
| `49` | `0xb83d...6e36` | `SHORT` | 25,063,463.60 USD | `259,338.02` | `91.42` | `96.56` | `551.00` | -1,354,649.56 USD | `-5.40%` | `5X Cross` |
| `79` | `0x3dc9...54b0` | `SHORT` | 21,261,698.36 USD | `220,000.19` | `105.90` | `96.56` | `175.77` | 2,037,408.91 USD | `+9.58%` | `20X Cross` |
| `111` | `0x9c89...600e` | `LONG` | 18,342,264.31 USD | `189,472.50` | `115.21` | `96.56` | `35.01` | -3,486,750.95 USD | `-19.01%` | `20X Cross` |
| `118` | `0x4a20...3c26` | `LONG` | 17,410,500.00 USD | `180,000.00` | `106.43` | `96.56` | `69.96` | -1,747,778.71 USD | `-10.04%` | `20X Cross` |
| `155` | `0xecb6...2b00` | `SHORT` | 13,338,012.40 USD | `138,011.80` | `101.05` | `96.56` | `323.58` | 607,445.70 USD | `+4.55%` | `20X Cross` |
| `223` | `0xc63a...a3cd` | `LONG` | 9,663,500.00 USD | `100,000.00` | `112.22` | `96.56` | `0.000000` | -1,558,608.97 USD | `-16.13%` | `20X Cross` |
| `224` | `0xb581...6f4f` | `LONG` | 9,660,400.00 USD | `100,000.00` | `112.81` | `96.56` | `0.000000` | -1,620,309.14 USD | `-16.77%` | `3X Cross` |
| `292` | `0x645b...87b8` | `SHORT` | 8,009,850.85 USD | `82,879.96` | `103.90` | `96.56` | `362.76` | 601,619.37 USD | `+7.51%` | `20X Cross` |
| `297` | `0xdb3a...cf3b` | `LONG` | 7,910,483.43 USD | `81,851.78` | `106.04` | `96.56` | `47.16` | -769,263.43 USD | `-9.72%` | `4X Cross` |
| `313` | `0xe927...98ef` | `LONG` | 7,537,530.00 USD | `78,000.00` | `96.34` | `96.56` | `38.45` | 23,388.52 USD | `+0.31%` | `3X Cross` |
| `323` | `0xca49...53c8` | `SHORT` | 7,143,750.65 USD | `73,943.45` | `110.70` | `96.56` | `303.86` | 1,041,871.61 USD | `+14.58%` | `20X Cross` |
| `328` | `0x8ae4...3d60` | `LONG` | 6,986,595.76 USD | `72,180.05` | `111.72` | `96.56` | `12.29` | -1,077,564.48 USD | `-15.42%` | `10X Cross` |
| `332` | `0xa0b7...6165` | `SHORT` | 6,863,175.15 USD | `71,044.42` | `107.87` | `96.56` | `190.91` | 800,292.05 USD | `+11.66%` | `2X Cross` |
| `353` | `0xf517...c032` | `SHORT` | 6,548,083.78 USD | `67,778.53` | `84.64` | `96.56` | `219.43` | -811,052.62 USD | `-12.39%` | `20X Cross` |
| `412` | `0x7fda...17d1` | `SHORT` | 5,387,178.53 USD | `55,739.62` | `100.53` | `96.56` | `794.52` | 216,534.47 USD | `+4.02%` | `20X Cross` |
| `469` | `0x7e23...5a5a` | `LONG` | 4,693,716.16 USD | `48,564.56` | `105.17` | `96.56` | `57.00` | -413,853.00 USD | `-8.82%` | `5X Isolated` |
| `563` | `0xf899...88db` | `SHORT` | 3,941,916.53 USD | `40,716.81` | `88.40` | `96.56` | `109.21` | -342,643.66 USD | `-8.69%` | `20X Cross` |
| `581` | `0x2e2b...2fab` | `LONG` | 3,865,960.00 USD | `40,000.00` | `119.55` | `96.56` | `59.93` | -916,075.64 USD | `-23.70%` | `10X Cross` |
| `616` | `0x9c16...4a6f` | `SHORT` | 3,656,435.41 USD | `37,796.13` | `90.79` | `96.56` | `118.57` | -225,084.69 USD | `-6.16%` | `20X Cross` |
| `634` | `0x7a5a...0394` | `SHORT` | 3,532,626.77 USD | `36,565.85` | `99.28` | `96.56` | `123.93` | 97,458.37 USD | `+2.76%` | `10X Cross` |
| `644` | `0x27b8...12fc` | `LONG` | 3,487,144.52 USD | `36,085.73` | `110.86` | `96.56` | `24.92` | -513,200.73 USD | `-14.72%` | `10X Cross` |
| `645` | `0x9946...0852` | `SHORT` | 3,486,461.34 USD | `36,099.58` | `110.82` | `96.56` | `141.29` | 514,125.05 USD | `+14.75%` | `20X Cross` |
| `673` | `0xa61c...66b9` | `LONG` | 3,339,123.65 USD | `34,550.76` | `102.76` | `96.56` | `0.000000` | -211,159.13 USD | `-6.32%` | `5X Cross` |
| `687` | `0x3440...32c5` | `SHORT` | 3,260,010.74 USD | `33,744.03` | `95.02` | `96.56` | `169.44` | -53,610.79 USD | `-1.64%` | `20X Cross` |
| `735` | `0x96a7...79df` | `LONG` | 3,092,608.00 USD | `32,000.00` | `74.39` | `96.56` | `0.000000` | 712,202.15 USD | `+23.03%` | `20X Cross` |
| `771` | `0xbe19...8bd1` | `SHORT` | 2,940,993.77 USD | `30,451.69` | `97.62` | `96.56` | `763.15` | 31,552.86 USD | `+1.07%` | `3X Cross` |
| `776` | `0x482b...cae4` | `SHORT` | 2,927,478.06 USD | `30,310.49` | `88.03` | `96.56` | `151.09` | -259,229.77 USD | `-8.86%` | `20X Cross` |
| `790` | `0x610b...b613` | `LONG` | 2,863,961.83 USD | `29,634.14` | `101.23` | `96.56` | `70.39` | -136,037.52 USD | `-4.75%` | `3X Isolated` |
| `805` | `0x45d2...4029` | `SHORT` | 2,822,768.88 USD | `29,220.00` | `93.28` | `96.56` | `1584.79` | -96,992.90 USD | `-3.44%` | `20X Cross` |
| `847` | `0x458d...ab3b` | `LONG` | 2,646,598.84 USD | `27,385.03` | `117.17` | `96.56` | `81.08` | -562,063.68 USD | `-21.24%` | `3X Isolated` |
| `882` | `0x023a...2355` | `SHORT` | 2,508,506.16 USD | `25,956.15` | `101.16` | `96.56` | `295.17` | 117,123.71 USD | `+4.67%` | `20X Cross` |
| `908` | `0xfc27...9d9d` | `SHORT` | 2,440,738.69 USD | `25,271.94` | `100.29` | `96.56` | `851.32` | 93,778.46 USD | `+3.84%` | `20X Cross` |
| `911` | `0x051c...693c` | `LONG` | 2,429,601.17 USD | `25,139.70` | `89.76` | `96.56` | `44.25` | 173,039.84 USD | `+7.12%` | `20X Cross` |
| `951` | `0x638f...f5f0` | `LONG` | 2,318,664.00 USD | `24,000.00` | `136.71` | `96.56` | `51.90` | -962,304.54 USD | `-41.50%` | `20X Cross` |
| `999` | `0x7277...0b98` | `SHORT` | 2,199,175.30 USD | `22,770.74` | `99.32` | `96.56` | `159.42` | 62,428.46 USD | `+2.84%` | `20X Cross` |
| `1001` | `0x7178...0854` | `LONG` | 2,182,672.32 USD | `22,545.24` | `110.94` | `96.56` | `40.27` | -318,472.15 USD | `-14.59%` | `10X Cross` |
| `1033` | `0x739c...cfb2` | `LONG` | 2,077,846.00 USD | `21,500.00` | `91.95` | `96.56` | `76.68` | 100,913.85 USD | `+4.86%` | `20X Cross` |
| `1100` | `0x7737...bf66` | `SHORT` | 1,973,890.45 USD | `20,384.06` | `102.94` | `96.56` | `993.97` | 124,451.44 USD | `+6.30%` | `10X Cross` |
| `1130` | `0xbfc7...80b4` | `SHORT` | 1,935,900.00 USD | `20,000.00` | `85.98` | `96.56` | `174.32` | -216,365.50 USD | `-11.18%` | `20X Cross` |
| `1132` | `0xea00...a918` | `LONG` | 1,935,072.85 USD | `20,022.69` | `66.09` | `96.56` | `0.000000` | 611,764.25 USD | `+31.61%` | `20X Cross` |
| `1134` | `0x3fc5...c0c1` | `SHORT` | 1,932,880.00 USD | `20,000.00` | `98.28` | `96.56` | `186.87` | 32,679.84 USD | `+1.69%` | `20X Cross` |
| `1135` | `0x251f...6e5d` | `LONG` | 1,932,200.00 USD | `20,000.00` | `101.15` | `96.56` | `71.69` | -90,897.77 USD | `-4.70%` | `20X Cross` |
| `1169` | `0x7160...d47c` | `LONG` | 1,877,528.40 USD | `19,434.10` | `105.03` | `96.56` | `76.21` | -163,692.89 USD | `-8.72%` | `20X Cross` |
| `1191` | `0xe097...d0fe` | `LONG` | 1,835,654.30 USD | `18,995.75` | `109.71` | `96.56` | `0.000000` | -248,342.59 USD | `-13.53%` | `20X Cross` |
| `1193` | `0x936c...bb0f` | `SHORT` | 1,835,259.16 USD | `18,988.91` | `105.57` | `96.56` | `533.09` | 169,428.53 USD | `+9.23%` | `20X Cross` |
| `1270` | `0xdf95...7d72` | `SHORT` | 1,719,800.44 USD | `17,802.58` | `104.53` | `96.56` | `2308.22` | 141,156.41 USD | `+8.21%` | `20X Cross` |
| `1275` | `0xe98b...8cd5` | `SHORT` | 1,706,547.80 USD | `17,622.89` | `187.95` | `96.56` | `262.54` | 1,605,672.92 USD | `+94.09%` | `20X Cross` |
| `1315` | `0xee2b...d67e` | `LONG` | 1,639,390.53 USD | `16,963.19` | `119.86` | `96.56` | `35.12` | -393,881.10 USD | `-24.03%` | `4X Cross` |
| `1324` | `0x123d...3bff` | `LONG` | 1,630,279.95 USD | `16,835.30` | `89.54` | `96.56` | `0.000000` | 122,838.69 USD | `+7.53%` | `10X Cross` |
| `1336` | `0x69cc...14fd` | `SHORT` | 1,613,020.93 USD | `16,701.57` | `99.01` | `96.56` | `586.23` | 40,586.36 USD | `+2.52%` | `20X Cross` |
| `1437` | `0x73d7...8be1` | `LONG` | 1,514,168.98 USD | `15,668.95` | `106.60` | `96.56` | `49.74` | -156,171.98 USD | `-10.31%` | `20X Cross` |
| `1447` | `0xc74a...ab93` | `LONG` | 1,500,918.96 USD | `15,536.82` | `64.06` | `96.56` | `54.89` | 505,690.12 USD | `+33.69%` | `5X Isolated` |
| `1480` | `0xb322...d51f` | `LONG` | 1,449,642.60 USD | `14,999.82` | `102.98` | `96.56` | `44.18` | -95,084.70 USD | `-6.56%` | `20X Cross` |
| `1481` | `0x5f10...d49d` | `LONG` | 1,448,685.00 USD | `15,000.00` | `96.35` | `96.56` | `72.20` | 3,383.84 USD | `+0.23%` | `20X Cross` |
| `1529` | `0xffb2...5ed6` | `LONG` | 1,404,093.57 USD | `14,504.05` | `117.89` | `96.56` | `84.69` | -305,811.14 USD | `-21.78%` | `20X Cross` |
| `1561` | `0x0d6a...ca57` | `LONG` | 1,373,058.52 USD | `14,206.65` | `110.41` | `96.56` | `91.60` | -195,531.84 USD | `-14.24%` | `5X Isolated` |
| `1769` | `0x2814...9b08` | `LONG` | 1,166,861.89 USD | `12,061.71` | `96.37` | `96.56` | `93.93` | 4,523.14 USD | `+0.39%` | `20X Isolated` |
| `1826` | `0x2577...4897` | `LONG` | 1,131,845.24 USD | `11,711.49` | `96.60` | `96.56` | `0.000000` | 485.58 USD | `+0.04%` | `15X Cross` |
| `1851` | `0x7808...6e70` | `SHORT` | 1,109,778.37 USD | `11,488.27` | `97.15` | `96.56` | `152.40` | 6,283.85 USD | `+0.57%` | `10X Cross` |
| `1868` | `0x2482...0e55` | `LONG` | 1,098,305.94 USD | `11,363.98` | `122.03` | `96.56` | `88.83` | -288,395.98 USD | `-26.26%` | `20X Isolated` |
| `1893` | `0x45db...86eb` | `LONG` | 1,072,648.50 USD | `11,100.00` | `110.69` | `96.56` | `69.31` | -156,033.40 USD | `-14.55%` | `5X Cross` |
| `1900` | `0xe863...8bb8` | `SHORT` | 1,060,976.19 USD | `10,978.19` | `97.06` | `96.56` | `259.96` | 4,596.99 USD | `+0.43%` | `20X Cross` |
| `1917` | `0x1d04...7c43` | `LONG` | 1,046,978.40 USD | `10,811.76` | `111.55` | `96.56` | `17.17` | -159,083.09 USD | `-15.19%` | `6X Cross` |
| `1938` | `0x34e6...8d74` | `LONG` | 1,031,206.58 USD | `10,671.15` | `101.19` | `96.56` | `15.56` | -48,568.06 USD | `-4.71%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `100.31` | 34,002.08 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 34.00K USD at 100.3100 USD [API] | `2026-10-29 09:58:06` |
| `ANNOUNCEMENT` | `INFO` | `100.55` | 25,634.22 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 25.63K USD at 100.5500 USD [API] | `2026-10-29 10:48:31` |
| `ANNOUNCEMENT` | `INFO` | `100.53` | 2.01 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.00K USD at 100.5300 USD [API] | `2026-10-29 11:50:52` |
| `ANNOUNCEMENT` | `INFO` | `100.20` | 25,159.22 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 25.16K USD at 100.2000 USD [API] | `2026-10-29 12:11:24` |
| `ANNOUNCEMENT` | `INFO` | `100.30` | 44,051.76 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 44.05K USD at 100.3000 USD [API] | `2026-10-29 12:19:01` |
| `ANNOUNCEMENT` | `INFO` | `100.43` | 20,001.64 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 20.00K USD at 100.4300 USD [API] | `2026-10-29 12:29:43` |
| `ANNOUNCEMENT` | `INFO` | `100.68` | 22,375.12 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 22.38K USD at 100.6800 USD [API] | `2026-10-29 13:05:41` |
| `ANNOUNCEMENT` | `INFO` | `100.75` | 37,574.71 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 37.57K USD at 100.7500 USD [API] | `2026-10-29 13:18:58` |
| `ANNOUNCEMENT` | `INFO` | `100.48` | 36,538.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 36.54K USD at 100.4800 USD [API] | `2026-10-29 13:53:35` |
| `ANNOUNCEMENT` | `INFO` | `101.56` | 22,019.22 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 22.02K USD at 101.5600 USD [API] | `2026-10-29 17:38:34` |
| `ANNOUNCEMENT` | `INFO` | `101.01` | 23,419.17 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 23.42K USD at 101.0100 USD [API] | `2026-10-29 17:57:56` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`101.22` (Vol: 4,800,000.00 USD, Dist: `+4.41%`) | Long MP=`92.18` (Vol: 5,300,000.00 USD, Dist: `--4.92%`)
  * 48H Horizon: Short MP=`101.12` (Vol: 5,400,000.00 USD, Dist: `+4.31%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--4.94%`)
  * 3D Horizon: Short MP=`101.12` (Vol: 5,400,000.00 USD, Dist: `+4.31%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--4.94%`)
  * 7D Horizon: Short MP=`104.03` (Vol: 7,200,000.00 USD, Dist: `+7.30%`) | Long MP=`92.11` (Vol: 5,300,000.00 USD, Dist: `--4.99%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `19.45` | 11,880.00 USD | 123,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.65` | 55,020.00 USD | 123,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.85` | 468.46 USD | 123,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.95` | 379.05 USD | 123,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.25` | 167.26 USD | 123,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.55` | 4,790.00 USD | 123,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.65` | 748.56 USD | 123,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.15` | 994.47 USD | 123,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 3,470.00 USD | 123,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 161.73 USD | 123,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.65` | 631.10 USD | 123,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.75` | 4,630.00 USD | 123,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.95` | 1,800.00 USD | 123,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.05` | 1,080.00 USD | 123,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.35` | 5,040.00 USD | 123,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.45` | 8,570.00 USD | 123,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.95` | 1,150.00 USD | 123,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.05` | 114.10 USD | 123,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.15` | 1,010.00 USD | 123,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.45` | 1,380.00 USD | 123,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.65` | 619.16 USD | 123,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 1,190.00 USD | 123,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.95` | 1,120.00 USD | 123,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.05` | 8,870.00 USD | 123,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.25` | 10,230.00 USD | 122,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.35` | 878,940.00 USD | 122,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.85` | 12,430.00 USD | 122,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.95` | 160.43 USD | 122,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.05` | 2,640.00 USD | 122,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.15` | 2,010.00 USD | 122,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 4,660.00 USD | 122,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.45` | 106.64 USD | 122,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 2,760.00 USD | 122,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.85` | 148,650.00 USD | 122,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 2,930.00 USD | 121,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.05` | 5,210.00 USD | 121,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.15` | 1,620.00 USD | 121,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.25` | 22,600.00 USD | 121,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.55` | 478.70 USD | 121,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.65` | 265.17 USD | 121,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 11,420.00 USD | 121,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.25` | 5,450.00 USD | 121,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.35` | 332.30 USD | 121,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.45` | 982.98 USD | 121,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.85` | 808.21 USD | 121,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 747.10 USD | 121,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.05` | 2,740.00 USD | 121,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.35` | 6,330.00 USD | 121,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 113.80 USD | 121,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.75` | 86,250.00 USD | 121,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.85` | 721.25 USD | 121,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 9,910.00 USD | 121,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.25` | 150.93 USD | 121,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.35` | 15,380.00 USD | 121,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.45` | 18,410.00 USD | 121,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.55` | 2,940.00 USD | 121,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.65` | 44,480.00 USD | 121,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.85` | 10,070.00 USD | 121,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.95` | 1,430.00 USD | 121,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 3,010.00 USD | 121,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.15` | 47,340.00 USD | 121,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.45` | 4,240.00 USD | 121,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 889.01 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 233.86 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.75` | 450.80 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.85` | 157.64 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.05` | 3,380.00 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.25` | 1,340.00 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.35` | 35,160.00 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.45` | 278.33 USD | 121,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.65` | 16,560.00 USD | 121,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.05` | 1,970.00 USD | 121,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.25` | 496.01 USD | 121,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 804.11 USD | 121,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.55` | 3,770.00 USD | 121,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 5,360.00 USD | 121,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 5,240.00 USD | 121,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.95` | 875.15 USD | 121,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.05` | 39,660.00 USD | 121,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.15` | 193.93 USD | 121,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.35` | 12,380.00 USD | 121,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.45` | 6,580.00 USD | 121,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.55` | 302.62 USD | 121,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 494.99 USD | 121,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.75` | 1,830.00 USD | 121,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.95` | 577,150.00 USD | 121,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.25` | 141.79 USD | 120,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 1,710.00 USD | 120,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.85` | 580.95 USD | 120,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 6,640,000.00 USD | 120,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.15` | 734.28 USD | 114,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.75` | 8,590.00 USD | 114,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.85` | 3,360.00 USD | 114,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.95` | 557.94 USD | 114,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.05` | 5,070.00 USD | 114,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.15` | 531.41 USD | 114,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.25` | 78,700.00 USD | 114,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 4,410.00 USD | 114,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 2,410.00 USD | 114,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.55` | 49,130.00 USD | 114,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.65` | 111,820.00 USD | 114,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 500.90 USD | 114,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.85` | 903.93 USD | 114,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.95` | 1,660.00 USD | 114,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 41,180.00 USD | 113,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 1,690.00 USD | 113,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 20,600.00 USD | 113,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.45` | 631.03 USD | 113,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 262.85 USD | 113,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.65` | 23,340.00 USD | 113,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 5,570.00 USD | 113,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 5,430.00 USD | 113,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 542.59 USD | 113,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.15` | 18,020.00 USD | 113,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 759.64 USD | 113,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 287.63 USD | 113,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 3,000,000.00 USD | 113,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 116.04 USD | 110,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 736.64 USD | 110,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.85` | 4,270.00 USD | 110,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 195,360.00 USD | 110,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 50,470.00 USD | 110,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 1,710.00 USD | 110,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 45,040.00 USD | 110,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 4,500.00 USD | 110,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 3,400.00 USD | 110,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 159.00 USD | 110,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 1,870.00 USD | 110,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.95` | 16,520.00 USD | 110,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 905,320.00 USD | 110,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.15` | 3,500.00 USD | 109,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.25` | 12,710.00 USD | 109,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 3,160.00 USD | 109,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 12,400.00 USD | 109,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 142.10 USD | 109,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 6,760.00 USD | 109,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 53,750.00 USD | 109,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 368.36 USD | 109,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.35` | 148.45 USD | 109,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 489.04 USD | 109,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 24,190.00 USD | 109,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.75` | 2,160.00 USD | 109,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 3,060.00 USD | 109,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 48,400.00 USD | 109,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 470.12 USD | 109,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 4,170.00 USD | 109,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 6,500.00 USD | 109,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 198.62 USD | 109,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.45` | 19,900.00 USD | 109,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.55` | 8,210.00 USD | 109,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 44,250.00 USD | 109,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 355.20 USD | 109,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 1,730.00 USD | 109,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 12,030.00 USD | 109,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 440.15 USD | 109,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 740.74 USD | 109,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 725,070.00 USD | 109,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 326.24 USD | 108,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 11,790.00 USD | 108,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.05` | 13,420.00 USD | 108,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 366,420.00 USD | 108,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 8,630.00 USD | 108,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.45` | 10,180.00 USD | 108,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 17,870.00 USD | 108,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 2,240.00 USD | 108,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 1,790.00 USD | 108,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 477.20 USD | 108,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 6,510.00 USD | 108,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 1,140,000.00 USD | 108,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 31,200.00 USD | 107,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 19,810.00 USD | 107,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 7,940.00 USD | 107,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 319.09 USD | 107,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 9,450.00 USD | 107,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.85` | 458.50 USD | 107,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 62,910.00 USD | 107,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 281.83 USD | 106,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 824.95 USD | 106,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 522.76 USD | 106,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 1,190.00 USD | 106,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.75` | 374.00 USD | 106,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 702.75 USD | 106,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 2,490.00 USD | 106,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 3,860,000.00 USD | 106,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 3,220.00 USD | 103,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 324.82 USD | 103,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 449.82 USD | 103,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.65` | 99,760.00 USD | 103,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 66,920.00 USD | 102,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.85` | 125.37 USD | 102,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 13,300.00 USD | 102,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 5,970.00 USD | 102,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 3,980.00 USD | 102,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.35` | 8,060.00 USD | 102,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.45` | 7,790.00 USD | 102,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 97,530.00 USD | 102,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 9,260.00 USD | 102,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 31,020.00 USD | 102,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.85` | 14,260.00 USD | 102,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,490.00 USD | 102,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 11,600.00 USD | 102,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.25` | 21,190.00 USD | 102,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 585.29 USD | 102,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 17,180.00 USD | 102,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 627.80 USD | 102,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 11,440.00 USD | 102,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.75` | 783,640.00 USD | 102,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.85` | 43,150.00 USD | 101,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 23,020.00 USD | 101,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 15,660.00 USD | 101,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.15` | 1,780.00 USD | 101,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 8,060.00 USD | 101,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.35` | 12,490.00 USD | 101,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 11,730.00 USD | 101,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 2,400.00 USD | 101,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.65` | 843.83 USD | 101,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 12,800.00 USD | 101,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.85` | 20,140.00 USD | 101,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 9,430.00 USD | 101,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.05` | 319,690.00 USD | 101,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.15` | 1,230,000.00 USD | 101,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.25` | 10,940.00 USD | 100,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.35` | 360.48 USD | 100,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.45` | 4,170.00 USD | 100,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.55` | 138,060.00 USD | 100,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.65` | 3,280.00 USD | 100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.75` | 24,770.00 USD | 100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.85` | 46,110.00 USD | 99,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.95` | 469,860.00 USD | 99,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.15` | 99,630.00 USD | 99,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.25` | 3,340.00 USD | 99,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.35` | 1,030.00 USD | 99,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.45` | 879.59 USD | 99,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.55` | 39,900.00 USD | 99,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.65` | 2,630.00 USD | 99,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.75` | 3,180.00 USD | 99,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.85` | 9,370.00 USD | 99,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.95` | 6,120.00 USD | 99,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.05` | 5,120.00 USD | 99,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.15` | 3,110.00 USD | 99,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.25` | 35,570.00 USD | 99,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.35` | 13,390.00 USD | 99,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.45` | 35,530.00 USD | 99,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.55` | 54,310.00 USD | 99,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.65` | 11,440.00 USD | 99,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.75` | 3,600.00 USD | 99,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.85` | 19,810.00 USD | 99,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.95` | 59,450.00 USD | 99,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.05` | 18,910.00 USD | 99,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.15` | 14,640.00 USD | 99,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.25` | 5,360.00 USD | 99,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.35` | 11,720.00 USD | 99,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.45` | 2,060.00 USD | 99,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.55` | 64,910.00 USD | 99,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.65` | 3,380.00 USD | 98,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.75` | 37,350.00 USD | 98,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.85` | 861,400.00 USD | 98,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.95` | 142,480.00 USD | 98,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.05` | 552.70 USD | 97,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.15` | 341.93 USD | 97,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.25` | 2,010.00 USD | 97,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.35` | 9,920.00 USD | 97,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.45` | 8,670.00 USD | 97,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.55` | 5,090.00 USD | 97,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.65` | 11,490.00 USD | 97,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.75` | 233,170.00 USD | 97,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.85` | 5,050.00 USD | 97,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.95` | 7,390.00 USD | 97,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.05` | 19,890.00 USD | 97,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.15` | 40,270.00 USD | 97,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.25` | 13,300.00 USD | 97,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.35` | 12,550.00 USD | 97,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.45` | 12,980.00 USD | 97,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.55` | 4,730.00 USD | 97,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.65` | 3,190.00 USD | 97,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.75` | 9,410.00 USD | 97,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.85` | 122.80 USD | 97,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.95` | 2,780,000.00 USD | 97,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.05` | 3,620.00 USD | 94,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.15` | 6,590.00 USD | 94,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.25` | 1,270.00 USD | 94,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.35` | 7,120.00 USD | 94,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.45` | 19,200.00 USD | 94,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.55` | 1,390.00 USD | 94,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.65` | 13,130.00 USD | 94,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.75` | 26,230.00 USD | 94,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.85` | 22,150.00 USD | 94,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.95` | 324.52 USD | 94,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.05` | 9,900.00 USD | 94,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.15` | 130,170.00 USD | 94,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.25` | 6,670.00 USD | 94,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.35` | 46,410.00 USD | 94,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.45` | 463.51 USD | 94,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.55` | 4,680.00 USD | 94,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.65` | 62,850.00 USD | 94,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.75` | 7,250.00 USD | 94,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.85` | 13,980.00 USD | 94,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.95` | 488.70 USD | 94,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.05` | 3,780.00 USD | 94,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.15` | 9,070.00 USD | 94,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.25` | 41,950.00 USD | 94,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.35` | 44,180.00 USD | 94,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.45` | 33,950.00 USD | 94,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.55` | 8,610.00 USD | 94,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.65` | 3,640.00 USD | 94,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.75` | 13,130.00 USD | 94,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.85` | 46,860.00 USD | 94,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.95` | 2,440,000.00 USD | 94,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.05` | 19,790.00 USD | 91,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.15` | 36,590.00 USD | 91,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.25` | 499.47 USD | 91,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.35` | 3,930.00 USD | 91,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.45` | 25,390.00 USD | 91,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.55` | 2,760.00 USD | 91,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.65` | 711.42 USD | 91,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.75` | 5,300.00 USD | 91,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.85` | 28,860.00 USD | 91,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.95` | 98,640.00 USD | 91,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.05` | 4,230.00 USD | 91,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.15` | 10,300.00 USD | 91,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.25` | 41,080.00 USD | 91,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.35` | 10,170.00 USD | 91,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.45` | 20,920.00 USD | 91,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.55` | 320.06 USD | 91,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.65` | 18,880.00 USD | 91,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.75` | 16,580.00 USD | 91,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.85` | 24,050.00 USD | 91,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.95` | 19,750.00 USD | 91,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.05` | 9,000.00 USD | 91,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.15` | 32,930.00 USD | 91,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.25` | 177,610.00 USD | 91,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.35` | 16,720.00 USD | 91,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.45` | 33,530.00 USD | 91,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.55` | 180,290.00 USD | 91,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.65` | 2,480.00 USD | 90,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.75` | 3,140.00 USD | 90,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.85` | 31,310.00 USD | 90,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.95` | 9,610.00 USD | 90,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.05` | 16,430.00 USD | 90,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.15` | 88,070.00 USD | 90,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.25` | 15,410.00 USD | 90,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.45` | 291.24 USD | 90,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.55` | 50,360.00 USD | 90,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.65` | 1,320.00 USD | 90,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.75` | 50,640.00 USD | 90,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.85` | 36,960.00 USD | 90,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.95` | 5,560.00 USD | 90,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.15` | 160.38 USD | 90,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.25` | 23,150.00 USD | 90,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.35` | 3,020.00 USD | 90,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.45` | 101,630.00 USD | 90,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.55` | 18,080.00 USD | 90,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.65` | 2,220.00 USD | 90,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.75` | 1,110.00 USD | 90,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.85` | 396.23 USD | 90,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.95` | 209.79 USD | 90,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.05` | 247,180.00 USD | 90,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.15` | 13,490.00 USD | 90,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.25` | 16,320.00 USD | 90,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.35` | 37,840.00 USD | 90,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.45` | 4,380.00 USD | 90,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.55` | 10,690.00 USD | 90,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.65` | 156,750.00 USD | 90,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.75` | 5,050.00 USD | 89,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.85` | 1,620.00 USD | 89,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.95` | 5,780.00 USD | 89,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.05` | 6,180.00 USD | 89,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.25` | 15,600.00 USD | 89,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.35` | 1,600.00 USD | 89,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.45` | 10,990.00 USD | 89,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.55` | 111,220.00 USD | 89,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.65` | 13,170.00 USD | 89,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.75` | 49,390.00 USD | 89,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.85` | 39,430.00 USD | 89,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.95` | 937.30 USD | 89,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.05` | 40,230.00 USD | 89,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.15` | 24,540.00 USD | 89,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.25` | 248.83 USD | 89,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.35` | 29,330.00 USD | 89,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.45` | 35,570.00 USD | 89,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.55` | 77,840.00 USD | 89,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.65` | 148,910.00 USD | 89,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.75` | 11,310.00 USD | 89,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.85` | 4,670.00 USD | 89,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.05` | 10,180.00 USD | 89,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.15` | 37,490,000.00 USD | 89,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.25` | 13,650.00 USD | 51,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.35` | 2,860.00 USD | 51,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.45` | 20,580.00 USD | 51,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.55` | 3,370.00 USD | 51,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.65` | 6,530.00 USD | 51,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.75` | 365,790.00 USD | 51,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.85` | 3,040.00 USD | 51,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.95` | 46,330.00 USD | 51,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.05` | 145.70 USD | 51,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.15` | 791,690.00 USD | 51,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.25` | 9,630.00 USD | 50,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.45` | 15,870.00 USD | 50,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.55` | 8,880.00 USD | 50,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.65` | 3,590.00 USD | 50,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.75` | 12,770,000.00 USD | 50,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.85` | 9,160.00 USD | 37,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.95` | 12,050.00 USD | 37,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.05` | 542,190.00 USD | 37,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.15` | 4,900.00 USD | 37,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.25` | 82,890.00 USD | 37,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.35` | 2,140,000.00 USD | 37,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.45` | 113,930.00 USD | 34,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.55` | 1,630.00 USD | 34,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.65` | 50,360.00 USD | 34,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.75` | 1,430,000.00 USD | 34,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.85` | 14,360.00 USD | 33,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.95` | 4,430.00 USD | 33,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.05` | 33,380.00 USD | 33,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.15` | 70,650.00 USD | 33,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.25` | 18,270.00 USD | 33,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.35` | 29,280.00 USD | 33,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.45` | 23,900.00 USD | 33,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.55` | 52,920.00 USD | 33,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.65` | 1,280.00 USD | 33,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.75` | 27,710.00 USD | 33,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.85` | 2,670.00 USD | 33,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.95` | 45,220.00 USD | 33,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.05` | 1,090,000.00 USD | 32,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.15` | 130,700.00 USD | 31,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.25` | 260,210.00 USD | 31,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.35` | 29,100.00 USD | 31,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.45` | 1,590.00 USD | 31,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.55` | 17,280.00 USD | 31,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.65` | 35,010.00 USD | 31,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.75` | 3,100.00 USD | 31,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.85` | 186,830.00 USD | 31,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.95` | 5,600.00 USD | 31,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.05` | 32,880.00 USD | 31,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.15` | 17,430.00 USD | 31,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.25` | 41,540.00 USD | 31,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.35` | 10,250.00 USD | 31,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.45` | 5,350.00 USD | 31,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.55` | 15,600.00 USD | 31,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.65` | 37,850.00 USD | 31,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.75` | 70,280.00 USD | 31,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.85` | 11,710.00 USD | 31,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.95` | 40,040.00 USD | 30,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.05` | 24,560.00 USD | 30,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.15` | 21,430.00 USD | 30,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.25` | 27,320.00 USD | 30,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.35` | 39,600.00 USD | 30,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.45` | 27,460.00 USD | 30,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.55` | 6,260.00 USD | 30,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.65` | 10,450.00 USD | 30,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.75` | 123,070.00 USD | 30,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.85` | 134,930.00 USD | 30,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.95` | 18,610.00 USD | 30,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.05` | 40,670.00 USD | 30,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.25` | 287,360.00 USD | 30,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.35` | 21,080.00 USD | 30,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.45` | 33,560.00 USD | 30,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.55` | 1,650,000.00 USD | 30,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.65` | 130,250.00 USD | 28,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.75` | 53,060.00 USD | 28,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.85` | 2,880.00 USD | 28,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.95` | 37,010.00 USD | 28,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.05` | 6,260.00 USD | 28,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.15` | 4,370.00 USD | 28,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.25` | 10,140.00 USD | 28,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.35` | 41,020.00 USD | 28,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.45` | 1,490,000.00 USD | 28,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.55` | 37,610.00 USD | 26,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.65` | 55,910.00 USD | 26,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.75` | 29,450.00 USD | 26,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.85` | 134,000.00 USD | 26,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.95` | 41,940.00 USD | 26,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.05` | 80,610.00 USD | 26,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.15` | 84,180.00 USD | 26,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.25` | 25,020.00 USD | 26,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.35` | 36,280.00 USD | 26,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.45` | 40,590.00 USD | 26,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.55` | 12,900.00 USD | 26,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.75` | 20,230.00 USD | 26,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.85` | 81,170.00 USD | 26,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.95` | 8,370.00 USD | 26,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.05` | 21,520.00 USD | 26,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.15` | 65,600.00 USD | 26,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.25` | 39,440.00 USD | 25,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.35` | 55,060.00 USD | 25,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.45` | 29,370.00 USD | 25,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.55` | 5,740.00 USD | 25,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.65` | 32,860.00 USD | 25,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.75` | 52,670.00 USD | 25,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.85` | 240,940.00 USD | 25,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.95` | 2,270.00 USD | 25,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.05` | 6,490.00 USD | 25,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.15` | 128,420.00 USD | 25,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.25` | 47,570.00 USD | 25,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.35` | 20,900.00 USD | 25,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.45` | 8,800.00 USD | 25,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.55` | 1,900.00 USD | 25,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.65` | 19,960.00 USD | 25,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.75` | 13,190.00 USD | 25,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.85` | 14,710.00 USD | 25,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.95` | 189,340.00 USD | 25,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.05` | 14,790.00 USD | 25,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.15` | 31,900.00 USD | 25,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.25` | 57,660.00 USD | 24,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.35` | 132,270.00 USD | 24,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.45` | 20,100.00 USD | 24,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.55` | 15,600.00 USD | 24,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.65` | 77,670.00 USD | 24,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.75` | 33,470.00 USD | 24,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.85` | 449,860.00 USD | 24,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.95` | 10,620.00 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.05` | 2,250,000.00 USD | 24,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.15` | 101,800.00 USD | 21,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.25` | 22,790.00 USD | 21,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.35` | 56,470.00 USD | 21,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.45` | 59,690.00 USD | 21,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.55` | 190,680.00 USD | 21,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.65` | 15,590.00 USD | 21,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.75` | 19,020.00 USD | 21,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.85` | 36,460.00 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.95` | 22,190.00 USD | 21,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.05` | 117,060.00 USD | 21,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.15` | 808,740.00 USD | 21,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.25` | 50,310.00 USD | 20,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.35` | 166,860.00 USD | 20,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.45` | 214,440.00 USD | 20,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.55` | 27,730.00 USD | 20,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `82.60` | 162,860,000.00 USD | 162,860,000.00 USD | 53,130.00 USD | 56,870.00 USD | 141,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `82.65` | 98,590.00 USD | 20,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.75` | 7,950.00 USD | 19,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `82.80` | 162,600,000.00 USD | 162,600,000.00 USD | 1,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `82.85` | 23,000.00 USD | 19,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.95` | 29,750.00 USD | 19,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.00` | 162,600,000.00 USD | 162,600,000.00 USD | 1,690.00 USD | 2,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.05` | 137,530.00 USD | 19,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.15` | 52,900.00 USD | 19,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.20` | 162,600,000.00 USD | 162,600,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.25` | 153,060.00 USD | 19,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.35` | 637,030.00 USD | 19,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.45` | 55,880.00 USD | 18,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.55` | 65,570.00 USD | 18,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.60` | 162,560,000.00 USD | 162,560,000.00 USD | 0.00 USD | 0.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.65` | 76,120.00 USD | 18,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.75` | 81,510.00 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.80` | 162,550,000.00 USD | 162,550,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.85` | 13,630.00 USD | 18,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.95` | 842,760.00 USD | 18,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.05` | 113,720.00 USD | 17,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.15` | 65,310.00 USD | 17,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.20` | 162,540,000.00 USD | 162,540,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.25` | 46,440.00 USD | 17,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.35` | 25,180.00 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.40` | 162,520,000.00 USD | 162,520,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.45` | 85,770.00 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.55` | 1,230,000.00 USD | 17,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.65` | 261,450.00 USD | 16,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.75` | 289,310.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.85` | 94,510.00 USD | 15,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.95` | 617.59 USD | 15,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.05` | 15,920.00 USD | 15,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.15` | 5,400.00 USD | 15,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.20` | 162,490,000.00 USD | 162,490,000.00 USD | 0.00 USD | 218,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.25` | 609,970.00 USD | 15,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.35` | 21,250.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.40` | 162,270,000.00 USD | 162,270,000.00 USD | 0.00 USD | 12,950.00 USD | 192,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.45` | 52,900.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.55` | 10,360.00 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.60` | 162,070,000.00 USD | 162,070,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.65` | 53,210.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.75` | 23,470.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.80` | 161,880,000.00 USD | 161,880,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.85` | 69,910.00 USD | 14,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.95` | 363,970.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.05` | 276,690.00 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.15` | 68,570.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.20` | 161,610,000.00 USD | 161,610,000.00 USD | 0.00 USD | 12,130.00 USD | 199,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.25` | 52,990.00 USD | 13,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.35` | 5,680.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.40` | 161,400,000.00 USD | 161,400,000.00 USD | 0.00 USD | 311,220.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.45` | 187,940.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.55` | 43,510.00 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.65` | 190,730.00 USD | 13,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.75` | 34,660.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.80` | 166,230,000.00 USD | 166,230,000.00 USD | 27,250.00 USD | 340,470.00 USD | 80,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `86.80` | 161,090,000.00 USD | 161,090,000.00 USD | 0.00 USD | 149,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.85` | 78,950.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.95` | 152,510.00 USD | 13,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.00` | 165,780,000.00 USD | 165,780,000.00 USD | 290,630.00 USD | 405,560.00 USD | 356,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.00` | 160,940,000.00 USD | 160,940,000.00 USD | 271,000.00 USD | 183,160.00 USD | 297,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.05` | 30,820.00 USD | 13,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.15` | 4,410.00 USD | 13,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.20` | 164,730,000.00 USD | 164,730,000.00 USD | 226,040.00 USD | 113,550.00 USD | 364,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.20` | 160,190,000.00 USD | 160,190,000.00 USD | 8,850.00 USD | 6,510.00 USD | 6,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.25` | 92,480.00 USD | 13,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.35` | 72,050.00 USD | 13,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.40` | 164,020,000.00 USD | 164,020,000.00 USD | 123,520.00 USD | 316,080.00 USD | 128,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.40` | 160,160,000.00 USD | 160,160,000.00 USD | 248,310.00 USD | 225,130.00 USD | 288,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.45` | 149,740.00 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.55` | 128,700.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.60` | 163,460,000.00 USD | 163,460,000.00 USD | 105,350.00 USD | 295,330.00 USD | 77,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.60` | 159,400,000.00 USD | 159,400,000.00 USD | 0.00 USD | 275,130.00 USD | 421,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.65` | 105,660.00 USD | 12,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.75` | 90,160.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.80` | 162,980,000.00 USD | 162,980,000.00 USD | 90,150.00 USD | 276,230.00 USD | 716,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.80` | 158,710,000.00 USD | 158,710,000.00 USD | 0.00 USD | 413,150.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.85` | 66,830.00 USD | 12,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.95` | 9,000.00 USD | 12,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.00` | 161,900,000.00 USD | 161,900,000.00 USD | 47,860.00 USD | 202,660.00 USD | 485,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.00` | 158,280,000.00 USD | 158,280,000.00 USD | 0.00 USD | 12,070.00 USD | 251,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.05` | 157,110.00 USD | 12,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.15` | 25,750.00 USD | 12,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.20` | 161,160,000.00 USD | 161,160,000.00 USD | 140,490.00 USD | 168,390.00 USD | 365,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.20` | 158,020,000.00 USD | 158,020,000.00 USD | 9,900.00 USD | 20,610.00 USD | 28,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.25` | 74,760.00 USD | 12,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.35` | 26,970.00 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.40` | 160,480,000.00 USD | 160,480,000.00 USD | 84,680.00 USD | 178,840.00 USD | 65,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.40` | 157,960,000.00 USD | 157,960,000.00 USD | 0.00 USD | 237,870.00 USD | 335,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.45` | 64,640.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.55` | 267,270.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.60` | 160,160,000.00 USD | 160,160,000.00 USD | 68,370.00 USD | 64,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.65` | 95,980.00 USD | 11,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.75` | 236,310.00 USD | 11,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.80` | 160,020,000.00 USD | 160,020,000.00 USD | 304,990.00 USD | 175,710.00 USD | 415,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.80` | 157,390,000.00 USD | 157,390,000.00 USD | 241,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.85` | 1,070,000.00 USD | 11,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.95` | 32,790.00 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.00` | 159,130,000.00 USD | 159,130,000.00 USD | 8,600.00 USD | 11,540.00 USD | 227,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.00` | 157,140,000.00 USD | 157,140,000.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.05` | 29,770.00 USD | 10,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.15` | 160,380.00 USD | 10,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.20` | 158,880,000.00 USD | 158,880,000.00 USD | 377,030.00 USD | 119,090.00 USD | 11,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.20` | 156,210,000.00 USD | 156,210,000.00 USD | 8,180.00 USD | 10,750.00 USD | 315,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.25` | 31,740.00 USD | 10,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.35` | 29,540.00 USD | 10,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.40` | 158,370,000.00 USD | 158,370,000.00 USD | 5,150.00 USD | 292,120.00 USD | 274,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.40` | 155,880,000.00 USD | 155,880,000.00 USD | 697,470.00 USD | 26,220.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.45` | 429,190.00 USD | 10,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.55` | 39,790.00 USD | 9,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.60` | 157,800,000.00 USD | 157,800,000.00 USD | 138,450.00 USD | 5,250.00 USD | 135,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.60` | 154,990,000.00 USD | 154,990,000.00 USD | 684,220.00 USD | 270,260.00 USD | 723,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.65` | 17,750.00 USD | 9,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.75` | 146,450.00 USD | 9,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.80` | 157,520,000.00 USD | 157,520,000.00 USD | 54,220.00 USD | 91,280.00 USD | 440,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.80` | 153,320,000.00 USD | 153,320,000.00 USD | 425,950.00 USD | 318,390.00 USD | 314,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.85` | 59,040.00 USD | 9,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.95` | 136,370.00 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.00` | 156,930,000.00 USD | 156,930,000.00 USD | 686,700.00 USD | 282,770.00 USD | 278,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.00` | 152,260,000.00 USD | 152,260,000.00 USD | 374,600.00 USD | 647,410.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.05` | 73,280.00 USD | 9,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.15` | 60,790.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.20` | 155,690,000.00 USD | 155,690,000.00 USD | 818,880.00 USD | 911,910.00 USD | 363,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.20` | 150,140,000.00 USD | 150,140,000.00 USD | 1,250,000.00 USD | 590,390.00 USD | 735,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.25` | 26,880.00 USD | 9,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.35` | 77,850.00 USD | 9,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.40` | 153,590,000.00 USD | 153,590,000.00 USD | 639,290.00 USD | 495,650.00 USD | 670,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.40` | 147,560,000.00 USD | 147,560,000.00 USD | 796,240.00 USD | 68,740.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.45` | 50,450.00 USD | 9,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.55` | 29,950.00 USD | 9,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.60` | 151,790,000.00 USD | 151,790,000.00 USD | 676,760.00 USD | 653,070.00 USD | 788,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.60` | 146,000,000.00 USD | 146,000,000.00 USD | 1,040,000.00 USD | 1,010,000.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.65` | 131,550.00 USD | 9,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.75` | 107,810.00 USD | 8,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.80` | 149,670,000.00 USD | 149,670,000.00 USD | 404,570.00 USD | 518,670.00 USD | 250,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.80` | 142,390,000.00 USD | 142,390,000.00 USD | 1,210,000.00 USD | 1,200,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.85` | 73,530.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.95` | 16,410.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.00` | 148,490,000.00 USD | 148,490,000.00 USD | 1,020,000.00 USD | 597,650.00 USD | 483,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.00` | 138,500,000.00 USD | 138,500,000.00 USD | 1,190,000.00 USD | 609,900.00 USD | 810,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.05` | 389,480.00 USD | 8,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.15` | 373,670.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.20` | 146,390,000.00 USD | 146,390,000.00 USD | 16,980.00 USD | 493,060.00 USD | 403,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.20` | 135,890,000.00 USD | 135,890,000.00 USD | 2,280,000.00 USD | 868,420.00 USD | 638,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.25` | 29,640.00 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.35` | 14,960.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.40` | 145,470,000.00 USD | 145,470,000.00 USD | 664,720.00 USD | 758,110.00 USD | 111,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.40` | 132,110,000.00 USD | 132,110,000.00 USD | 1,180,000.00 USD | 1,030,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.45` | 331,850.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.55` | 1,210,000.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.60` | 143,940,000.00 USD | 143,940,000.00 USD | 488,750.00 USD | 281,460.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.60` | 128,280,000.00 USD | 128,280,000.00 USD | 500,280.00 USD | 1,020,000.00 USD | 872,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.65` | 1,430,000.00 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.75` | 240,910.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.80` | 142,070,000.00 USD | 142,070,000.00 USD | 526,140.00 USD | 449,000.00 USD | 713,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.80` | 125,890,000.00 USD | 125,890,000.00 USD | 932,400.00 USD | 797,110.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.85` | 43,170.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.95` | 64,120.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.00` | 140,380,000.00 USD | 140,380,000.00 USD | 2,810,000.00 USD | 2,220,000.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.00` | 123,470,000.00 USD | 123,470,000.00 USD | 681,440.00 USD | 656,110.00 USD | 990,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.05` | 168,710.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.15` | 328,530.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.20` | 134,240,000.00 USD | 134,240,000.00 USD | 887,260.00 USD | 1,630,000.00 USD | 465,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.20` | 121,150,000.00 USD | 121,150,000.00 USD | 2,870,000.00 USD | 1,110,000.00 USD | 289,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.25` | 170,110.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.35` | 304,990.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.40` | 131,260,000.00 USD | 131,260,000.00 USD | 731,980.00 USD | 331,330.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.40` | 116,880,000.00 USD | 116,880,000.00 USD | 550,500.00 USD | 833,900.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.45` | 117,820.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.55` | 4,870.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.60` | 128,030,000.00 USD | 128,030,000.00 USD | 1,330,000.00 USD | 1,530,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.60` | 113,960,000.00 USD | 113,960,000.00 USD | 98,670.00 USD | 880,990.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.65` | 15,170.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.75` | 4,920.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.80` | 122,750,000.00 USD | 122,750,000.00 USD | 2,020,000.00 USD | 948,040.00 USD | 977,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.80` | 111,500,000.00 USD | 111,500,000.00 USD | 463,730.00 USD | 2,370,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.85` | 23,420.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.95` | 3,780.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.00` | 118,800,000.00 USD | 118,800,000.00 USD | 3,260,000.00 USD | 3,880,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.00` | 107,060,000.00 USD | 107,060,000.00 USD | 539,240.00 USD | 550,690.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.05` | 29,610.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.15` | 319,790.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.20` | 108,080,000.00 USD | 108,080,000.00 USD | 2,720,000.00 USD | 1,820,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.20` | 103,940,000.00 USD | 103,940,000.00 USD | 1,090,000.00 USD | 670,930.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.25` | 105,430.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.35` | 13,390.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.40` | 101,550,000.00 USD | 101,550,000.00 USD | 3,070,000.00 USD | 3,100,000.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.40` | 100,050,000.00 USD | 100,050,000.00 USD | 611,840.00 USD | 2,660,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.45` | 8,060.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.55` | 19,360.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.60` | 93,030,000.00 USD | 93,030,000.00 USD | 1,950,000.00 USD | 3,880,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.60` | 95,340,000.00 USD | 95,340,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.65` | 937,160.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.75` | 10,870.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.80` | 86,090,000.00 USD | 86,090,000.00 USD | 1,010,000.00 USD | 1,030,000.00 USD | 483,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.80` | 92,400,000.00 USD | 92,400,000.00 USD | 0.00 USD | 2,080,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.85` | 11,870.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.95` | 1,140,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.00` | 83,570,000.00 USD | 83,570,000.00 USD | 759,420.00 USD | 1,060,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.00` | 87,150,000.00 USD | 87,150,000.00 USD | 2,660,000.00 USD | 1,780,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.05` | 4,190.00 USD | 821,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.15` | 29,950.00 USD | 817,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.20` | 79,930,000.00 USD | 79,930,000.00 USD | 1,980,000.00 USD | 1,940,000.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.20` | 80,500,000.00 USD | 80,500,000.00 USD | 24,740.00 USD | 962,410.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.25` | 8,860.00 USD | 787,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.35` | 5,200.00 USD | 778,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.40` | 73,850,000.00 USD | 73,850,000.00 USD | 1,650,000.00 USD | 568,640.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.40` | 76,770,000.00 USD | 76,770,000.00 USD | 0.00 USD | 496,790.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.45` | 146,220.00 USD | 773,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.55` | 60,600.00 USD | 627,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.60` | 70,620,000.00 USD | 70,620,000.00 USD | 142,910.00 USD | 1,380,000.00 USD | 398,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.60` | 76,260,000.00 USD | 76,260,000.00 USD | 560,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `94.65` | 28,740.00 USD | 28,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.75` | 82,810.00 USD | 566,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.80` | 68,700,000.00 USD | 68,700,000.00 USD | 2,970,000.00 USD | 800,730.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.80` | 75,700,000.00 USD | 75,700,000.00 USD | 2,090,000.00 USD | 152,290.00 USD | 3,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.85` | 54,830.00 USD | 483,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.95` | 58,350.00 USD | 428,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.00` | 63,320,000.00 USD | 63,320,000.00 USD | 4,450,000.00 USD | 899,320.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.00` | 70,090,000.00 USD | 70,090,000.00 USD | 3,400,000.00 USD | 4,770,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.05` | 57,060.00 USD | 370,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.15` | 21,470.00 USD | 313,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.20` | 56,840,000.00 USD | 56,840,000.00 USD | 1,720,000.00 USD | 2,190,000.00 USD | 3,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.20` | 60,350,000.00 USD | 60,350,000.00 USD | 2,420,000.00 USD | 317,900.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.25` | 42,730.00 USD | 292,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.35` | 7,550.00 USD | 249,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.40` | 49,800,000.00 USD | 49,800,000.00 USD | 1,120,000.00 USD | 1,820,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.40` | 57,590,000.00 USD | 57,590,000.00 USD | 2,080,000.00 USD | 2,620,000.00 USD | 4,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.45` | 24,230.00 USD | 241,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.55` | 44,760.00 USD | 217,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.60` | 45,590,000.00 USD | 45,590,000.00 USD | 1,850,000.00 USD | 2,410,000.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.60` | 48,300,000.00 USD | 48,300,000.00 USD | 3,820,000.00 USD | 7,040,000.00 USD | 4,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.65` | 92,490.00 USD | 172,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.75` | 49,350.00 USD | 80,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.80` | 40,130,000.00 USD | 40,130,000.00 USD | 2,040,000.00 USD | 1,900,000.00 USD | 7,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.80` | 32,850,000.00 USD | 32,850,000.00 USD | 3,400,000.00 USD | 93,510.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.85` | 30,710.00 USD | 30,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.95` | 231.24 USD | 231.24 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.00` | 28,770,000.00 USD | 28,770,000.00 USD | 4,610,000.00 USD | 2,890,000.00 USD | 6,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.00` | 27,060,000.00 USD | 27,060,000.00 USD | 5,350,000.00 USD | 1,290,000.00 USD | 5,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.20` | 15,180,000.00 USD | 15,180,000.00 USD | 6,210,000.00 USD | 7,360,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.20` | 14,800,000.00 USD | 14,800,000.00 USD | 6,840,000.00 USD | 2,710,000.00 USD | 5,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `96.40` | 11,260,000.00 USD | 11,260,000.00 USD | 4,170,000.00 USD | 2,150,000.00 USD | 4,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `96.40` | 22,510,000.00 USD | 22,510,000.00 USD | 4,170,000.00 USD | 2,150,000.00 USD | 4,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `96.40` | 10,660,000.00 USD | 10,660,000.00 USD | 1,600,000.00 USD | 2,590,000.00 USD | 6,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `96.40` | 21,310,000.00 USD | 21,310,000.00 USD | 1,600,000.00 USD | 2,590,000.00 USD | 6,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `96.60` | 26,120,000.00 USD | 26,120,000.00 USD | 1,300,000.00 USD | 2,010,000.00 USD | 299,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `96.60` | 21,340,000.00 USD | 21,340,000.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `96.80` | 26,130,000.00 USD | 26,130,000.00 USD | 0.00 USD | 8,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `96.80` | 21,400,000.00 USD | 21,400,000.00 USD | 0.00 USD | 64,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.00` | 27,540,000.00 USD | 27,540,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.20` | 24,720,000.00 USD | 24,720,000.00 USD | 0.00 USD | 0.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.40` | 29,370,000.00 USD | 29,370,000.00 USD | 534,370.00 USD | 1,280,000.00 USD | 18,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.40` | 24,820,000.00 USD | 24,820,000.00 USD | 0.00 USD | 101,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.60` | 30,610,000.00 USD | 30,610,000.00 USD | 0.00 USD | 0.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.60` | 28,760,000.00 USD | 28,760,000.00 USD | 0.00 USD | 24,930.00 USD | 3,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.75` | 1,220.00 USD | 29,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.80` | 36,010,000.00 USD | 36,010,000.00 USD | 3,010,000.00 USD | 876,010.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.80` | 40,800,000.00 USD | 40,800,000.00 USD | 7,580,000.00 USD | 3,430,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.00` | 40,860,000.00 USD | 40,860,000.00 USD | 2,320,000.00 USD | 712,280.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.00` | 57,500,000.00 USD | 57,500,000.00 USD | 14,120,000.00 USD | 561,730.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.20` | 47,970,000.00 USD | 47,970,000.00 USD | 3,200,000.00 USD | 2,290,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.20` | 68,410,000.00 USD | 68,410,000.00 USD | 9,790,000.00 USD | 1,120,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.40` | 59,030,000.00 USD | 59,030,000.00 USD | 772,180.00 USD | 311,650.00 USD | 9,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.40` | 79,550,000.00 USD | 79,550,000.00 USD | 1,780,000.00 USD | 3,320,000.00 USD | 6,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.55` | 5,930.00 USD | 35,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.60` | 73,070,000.00 USD | 73,070,000.00 USD | 649,650.00 USD | 5,980,000.00 USD | 7,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.60` | 88,910,000.00 USD | 88,910,000.00 USD | 1,960,000.00 USD | 5,450,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.65` | 9,740.00 USD | 45,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.80` | 87,200,000.00 USD | 87,200,000.00 USD | 2,640,000.00 USD | 4,390,000.00 USD | 7,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.80` | 94,710,000.00 USD | 94,710,000.00 USD | 1,080,000.00 USD | 784,380.00 USD | 3,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.95` | 1,020.00 USD | 46,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.00` | 102,560,000.00 USD | 102,560,000.00 USD | 3,500,000.00 USD | 6,290,000.00 USD | 5,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.00` | 103,540,000.00 USD | 103,540,000.00 USD | 2,170,000.00 USD | 2,700,000.00 USD | 3,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.05` | 3,610.00 USD | 50,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.15` | 1,110,000.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.20` | 113,660,000.00 USD | 113,660,000.00 USD | 2,840,000.00 USD | 4,520,000.00 USD | 3,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.20` | 117,510,000.00 USD | 117,510,000.00 USD | 1,220,000.00 USD | 6,520,000.00 USD | 6,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.25` | 72,450.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.35` | 92,510.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.40` | 119,430,000.00 USD | 119,430,000.00 USD | 2,370,000.00 USD | 1,650,000.00 USD | 1,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.40` | 118,550,000.00 USD | 118,550,000.00 USD | 0.00 USD | 1,010,000.00 USD | 25,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.45` | 19,710.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.55` | 138,120.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.60` | 135,880,000.00 USD | 135,880,000.00 USD | 2,920,000.00 USD | 6,420,000.00 USD | 7,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.60` | 123,980,000.00 USD | 123,980,000.00 USD | 2,240,000.00 USD | 2,640,000.00 USD | 545,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.65` | 9,360.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.75` | 33,470.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.80` | 150,840,000.00 USD | 150,840,000.00 USD | 2,520,000.00 USD | 4,590,000.00 USD | 7,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.80` | 127,310,000.00 USD | 127,310,000.00 USD | 736,270.00 USD | 1,330,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.85` | 883.67 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.95` | 4,010.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.00` | 161,300,000.00 USD | 161,300,000.00 USD | 2,850,000.00 USD | 3,360,000.00 USD | 4,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.00` | 138,640,000.00 USD | 138,640,000.00 USD | 2,220,000.00 USD | 2,310,000.00 USD | 6,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.05` | 36,990.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.15` | 25,710.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.20` | 164,470,000.00 USD | 164,470,000.00 USD | 651,800.00 USD | 2,130,000.00 USD | 388,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.20` | 144,730,000.00 USD | 144,730,000.00 USD | 843,770.00 USD | 2,460,000.00 USD | 2,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.25` | 347,460.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.35` | 391,910.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.40` | 170,220,000.00 USD | 170,220,000.00 USD | 976,110.00 USD | 1,790,000.00 USD | 2,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.40` | 149,210,000.00 USD | 149,210,000.00 USD | 993,830.00 USD | 654,600.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.45` | 26,900.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.55` | 1,510.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.60` | 181,260,000.00 USD | 181,260,000.00 USD | 2,300,000.00 USD | 1,830,000.00 USD | 6,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.60` | 155,050,000.00 USD | 155,050,000.00 USD | 2,150,000.00 USD | 1,480,000.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.65` | 101,930.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.75` | 19,590.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.80` | 188,000,000.00 USD | 188,000,000.00 USD | 2,610,000.00 USD | 1,940,000.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.80` | 158,210,000.00 USD | 158,210,000.00 USD | 994,710.00 USD | 1,380,000.00 USD | 786,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.85` | 62,360.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.95` | 498.69 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.00` | 198,770,000.00 USD | 198,770,000.00 USD | 6,070,000.00 USD | 3,420,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.00` | 177,180,000.00 USD | 177,180,000.00 USD | 4,160,000.00 USD | 7,060,000.00 USD | 7,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.05` | 698.26 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.15` | 12,940.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.20` | 211,010,000.00 USD | 211,010,000.00 USD | 5,270,000.00 USD | 4,010,000.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.20` | 196,590,000.00 USD | 196,590,000.00 USD | 7,240,000.00 USD | 5,320,000.00 USD | 6,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.25` | 769.50 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.40` | 221,710,000.00 USD | 221,710,000.00 USD | 3,860,000.00 USD | 2,700,000.00 USD | 4,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.40` | 213,650,000.00 USD | 213,650,000.00 USD | 4,720,000.00 USD | 1,270,000.00 USD | 11,070,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.45` | 118.70 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.55` | 2,790.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.60` | 236,590,000.00 USD | 236,590,000.00 USD | 2,980,000.00 USD | 2,630,000.00 USD | 9,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.60` | 224,170,000.00 USD | 224,170,000.00 USD | 3,650,000.00 USD | 30,170.00 USD | 6,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.65` | 3,870.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.80` | 242,810,000.00 USD | 242,810,000.00 USD | 646,170.00 USD | 836,200.00 USD | 4,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.80` | 234,100,000.00 USD | 234,100,000.00 USD | 3,050,000.00 USD | 609,510.00 USD | 6,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.95` | 1,760.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.00` | 249,090,000.00 USD | 249,090,000.00 USD | 2,520,000.00 USD | 1,780,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.00` | 240,090,000.00 USD | 240,090,000.00 USD | 1,830,000.00 USD | 1,470,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.05` | 4,280.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.15` | 719.14 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.20` | 255,180,000.00 USD | 255,180,000.00 USD | 3,110,000.00 USD | 1,170,000.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.20` | 246,810,000.00 USD | 246,810,000.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.25` | 1,170.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.40` | 259,600,000.00 USD | 259,600,000.00 USD | 1,560,000.00 USD | 716,320.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.40` | 252,120,000.00 USD | 252,120,000.00 USD | 2,340,000.00 USD | 304,350.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.55` | 6,330.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.60` | 262,240,000.00 USD | 262,240,000.00 USD | 985,660.00 USD | 606,030.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.60` | 254,580,000.00 USD | 254,580,000.00 USD | 1,450,000.00 USD | 979,270.00 USD | 33,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.65` | 1,500.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.75` | 3,240.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.80` | 266,290,000.00 USD | 266,290,000.00 USD | 1,260,000.00 USD | 1,570,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.80` | 262,670,000.00 USD | 262,670,000.00 USD | 7,780,000.00 USD | 23,810.00 USD | 286,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.95` | 4,150.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.00` | 271,340,000.00 USD | 271,340,000.00 USD | 3,120,000.00 USD | 1,440,000.00 USD | 498,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.00` | 279,610,000.00 USD | 279,610,000.00 USD | 12,270,000.00 USD | 394,420.00 USD | 4,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.05` | 692.50 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.15` | 11,000.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.20` | 273,710,000.00 USD | 273,710,000.00 USD | 301,000.00 USD | 853,780.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.20` | 292,280,000.00 USD | 292,280,000.00 USD | 11,620,000.00 USD | 140,550.00 USD | 913,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.25` | 863.17 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.35` | 385.50 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.40` | 276,640,000.00 USD | 276,640,000.00 USD | 867,130.00 USD | 1,180,000.00 USD | 877,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.40` | 306,850,000.00 USD | 306,850,000.00 USD | 11,050,000.00 USD | 233,330.00 USD | 3,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.45` | 3,300.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.60` | 284,270,000.00 USD | 284,270,000.00 USD | 2,430,000.00 USD | 183,360.00 USD | 5,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.60` | 325,240,000.00 USD | 325,240,000.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.65` | 4,360.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.75` | 261,050.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.80` | 287,420,000.00 USD | 287,420,000.00 USD | 481,980.00 USD | 1,320,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.80` | 337,630,000.00 USD | 337,630,000.00 USD | 7,960,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.85` | 13,560.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.95` | 827.44 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.00` | 293,220,000.00 USD | 293,220,000.00 USD | 2,410,000.00 USD | 1,490,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.00` | 364,330,000.00 USD | 364,330,000.00 USD | 10,830,000.00 USD | 7,160,000.00 USD | 8,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.05` | 775.17 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.15` | 4,830.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.20` | 296,390,000.00 USD | 296,390,000.00 USD | 1,290,000.00 USD | 831,810.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.20` | 386,360,000.00 USD | 386,360,000.00 USD | 8,520,000.00 USD | 7,230,000.00 USD | 6,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.25` | 41,100.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.35` | 11,630.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.40` | 300,650,000.00 USD | 300,650,000.00 USD | 1,470,000.00 USD | 1,330,000.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.40` | 403,540,000.00 USD | 403,540,000.00 USD | 5,100,000.00 USD | 3,710,000.00 USD | 8,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.45` | 8,550.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.55` | 575.03 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.60` | 304,660,000.00 USD | 304,660,000.00 USD | 1,030,000.00 USD | 794,070.00 USD | 2,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.60` | 421,290,000.00 USD | 421,290,000.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 7,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.65` | 401.86 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.75` | 3,620.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.80` | 308,670,000.00 USD | 308,670,000.00 USD | 1,250,000.00 USD | 820,470.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.80` | 438,680,000.00 USD | 438,680,000.00 USD | 5,170,000.00 USD | 4,410,000.00 USD | 7,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.95` | 126,400.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.00` | 309,900,000.00 USD | 309,900,000.00 USD | 463,890.00 USD | 350,040.00 USD | 413,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.00` | 454,850,000.00 USD | 454,850,000.00 USD | 5,730,000.00 USD | 4,110,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.05` | 578.83 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.15` | 19,740.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.20` | 310,970,000.00 USD | 310,970,000.00 USD | 111,930.00 USD | 94,030.00 USD | 864,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.20` | 465,510,000.00 USD | 465,510,000.00 USD | 5,340,000.00 USD | 2,800,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.25` | 2,110.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.35` | 6,840.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.40` | 311,450,000.00 USD | 311,450,000.00 USD | 262,490.00 USD | 138,720.00 USD | 78,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.40` | 473,730,000.00 USD | 473,730,000.00 USD | 1,570,000.00 USD | 3,170,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.45` | 531,450.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.55` | 4,180.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.60` | 311,880,000.00 USD | 311,880,000.00 USD | 130,280.00 USD | 187,950.00 USD | 110,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.60` | 482,150,000.00 USD | 482,150,000.00 USD | 3,700,000.00 USD | 2,270,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.65` | 3,540.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.80` | 312,570,000.00 USD | 312,570,000.00 USD | 87,540.00 USD | 526,970.00 USD | 76,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.80` | 490,960,000.00 USD | 490,960,000.00 USD | 2,690,000.00 USD | 2,620,000.00 USD | 3,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.85` | 91,370.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.95` | 840.18 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.00` | 313,720,000.00 USD | 313,720,000.00 USD | 372,000.00 USD | 554,120.00 USD | 226,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.00` | 496,110,000.00 USD | 496,110,000.00 USD | 1,970,000.00 USD | 1,050,000.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.05` | 33,380.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.15` | 5,820.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.20` | 315,140,000.00 USD | 315,140,000.00 USD | 623,340.00 USD | 349,490.00 USD | 440,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.20` | 505,010,000.00 USD | 505,010,000.00 USD | 3,820,000.00 USD | 2,560,000.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.35` | 252,430.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.40` | 315,980,000.00 USD | 315,980,000.00 USD | 191,590.00 USD | 403,460.00 USD | 243,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.40` | 511,080,000.00 USD | 511,080,000.00 USD | 2,430,000.00 USD | 2,180,000.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.45` | 33,200.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.55` | 218.43 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.60` | 317,980,000.00 USD | 317,980,000.00 USD | 547,840.00 USD | 307,440.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.60` | 515,920,000.00 USD | 515,920,000.00 USD | 1,330,000.00 USD | 1,250,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.65` | 6,460.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.80` | 319,550,000.00 USD | 319,550,000.00 USD | 434,130.00 USD | 399,910.00 USD | 737,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.80` | 520,570,000.00 USD | 520,570,000.00 USD | 999,190.00 USD | 927,000.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.85` | 479,570.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.95` | 131.55 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.00` | 320,330,000.00 USD | 320,330,000.00 USD | 193,920.00 USD | 413,830.00 USD | 167,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.00` | 524,710,000.00 USD | 524,710,000.00 USD | 527,980.00 USD | 1,180,000.00 USD | 2,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.05` | 14,820.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.15` | 3,060.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.20` | 320,820,000.00 USD | 320,820,000.00 USD | 0.00 USD | 50,140.00 USD | 436,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.20` | 525,800,000.00 USD | 525,800,000.00 USD | 230,020.00 USD | 507,570.00 USD | 352,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.25` | 46,610.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.35` | 766.48 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.40` | 321,600,000.00 USD | 321,600,000.00 USD | 60,260.00 USD | 201,440.00 USD | 518,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.40` | 527,090,000.00 USD | 527,090,000.00 USD | 0.00 USD | 576,040.00 USD | 709,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.45` | 32,580.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.55` | 221.55 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.60` | 527,720,000.00 USD | 527,720,000.00 USD | 213,520.00 USD | 12,070.00 USD | 406,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.75` | 150,290.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.80` | 528,560,000.00 USD | 528,560,000.00 USD | 499,550.00 USD | 31,020.00 USD | 305,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.85` | 143,860.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.00` | 529,140,000.00 USD | 529,140,000.00 USD | 5,950.00 USD | 237,870.00 USD | 335,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.05` | 1,080.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.15` | 1,150.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.20` | 529,420,000.00 USD | 529,420,000.00 USD | 0.00 USD | 205,080.00 USD | 74,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.25` | 161,430.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.35` | 3,470.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.40` | 529,900,000.00 USD | 529,900,000.00 USD | 487,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.45` | 108,080.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.55` | 261.61 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.60` | 530,090,000.00 USD | 530,090,000.00 USD | 17,470.00 USD | 167,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.65` | 7,980.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.80` | 531,020,000.00 USD | 531,020,000.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.85` | 41,550.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.95` | 3,170.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.00` | 531,320,000.00 USD | 531,320,000.00 USD | 8,180.00 USD | 0.00 USD | 286,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.05` | 163.58 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.15` | 17,440.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.25` | 2,720.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.35` | 247.13 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.45` | 620.58 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.55` | 356.04 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.65` | 447,000.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.75` | 111.95 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.85` | 459.17 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.95` | 4,480.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.05` | 14,790.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.15` | 194.97 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.25` | 226.01 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.35` | 385.12 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 143,580.00 USD | 5,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.55` | 1,820.00 USD | 5,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.85` | 1,090.00 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 4,450.00 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.15` | 29,660.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.35` | 390.84 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.45` | 841.45 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.55` | 892.40 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.65` | 199.85 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.75` | 169.86 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.85` | 15,880.00 USD | 5,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.95` | 223.90 USD | 5,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.15` | 528.23 USD | 5,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.25` | 261,320.00 USD | 6,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.35` | 1,910.00 USD | 6,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.45` | 5,670.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.55` | 1,070.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.65` | 707.44 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.75` | 118,640.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.85` | 108,760.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.05` | 406.98 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.15` | 9,560.00 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.25` | 698.75 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.35` | 4,120.00 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.45` | 5,120.00 USD | 6,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.65` | 105,650.00 USD | 6,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.75` | 5,200.00 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.85` | 461.09 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.95` | 21,840.00 USD | 6,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.05` | 31,740.00 USD | 6,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.25` | 6,230.00 USD | 6,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.45` | 3,830.00 USD | 6,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.65` | 3,430.00 USD | 6,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.95` | 1,260.00 USD | 6,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.05` | 569,550.00 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.15` | 1,100.00 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.35` | 161.49 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.45` | 879,040.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.55` | 167,330.00 USD | 8,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.65` | 14,750.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.75` | 6,060.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.85` | 512.06 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.05` | 4,450.00 USD | 8,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.25` | 180.19 USD | 8,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.35` | 4,960.00 USD | 8,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.55` | 2,040.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.65` | 113.15 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.75` | 6,020.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.85` | 10,520.00 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.05` | 156.85 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.15` | 89,950.00 USD | 8,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.35` | 11,610.00 USD | 8,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.55` | 4,790,000.00 USD | 13,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.75` | 10,360.00 USD | 13,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.95` | 2,310.00 USD | 13,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.25` | 614.90 USD | 13,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.45` | 4,510,000.00 USD | 17,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.55` | 7,700.00 USD | 17,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.75` | 309.94 USD | 17,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.25` | 240.88 USD | 17,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.35` | 57,850.00 USD | 17,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.45` | 1,560.00 USD | 17,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.55` | 8,970.00 USD | 17,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.65` | 470.22 USD | 17,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.75` | 28,230.00 USD | 17,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.85` | 485.39 USD | 17,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.15` | 140,720.00 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.25` | 453.34 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.45` | 145.74 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.55` | 1,190.00 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.75` | 515.60 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.95` | 13,290.00 USD | 18,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.05` | 60,530.00 USD | 18,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.15` | 2,100.00 USD | 18,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.35` | 489,130.00 USD | 18,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.55` | 5,940.00 USD | 18,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.75` | 105.92 USD | 18,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.05` | 56,150.00 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.15` | 169.79 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.25` | 2,330.00 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.35` | 881,450.00 USD | 19,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.45` | 17,500.00 USD | 19,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.65` | 116.52 USD | 19,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.95` | 4,300.00 USD | 19,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.25` | 471,560.00 USD | 19,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.35` | 2,330.00 USD | 20,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.45` | 1,960.00 USD | 20,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.65` | 124,510.00 USD | 20,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.05` | 7,950.00 USD | 20,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.15` | 121.67 USD | 20,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.25` | 23,360.00 USD | 20,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.35` | 29,710.00 USD | 20,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.55` | 3,080.00 USD | 20,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.65` | 675.60 USD | 20,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.75` | 5,330.00 USD | 20,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.95` | 2,800.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.05` | 208.83 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.25` | 690.13 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.35` | 5,320.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.45` | 590.87 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.55` | 51,130.00 USD | 20,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.65` | 1,560.00 USD | 20,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.75` | 1,930.00 USD | 20,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.85` | 5,430,000.00 USD | 25,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.95` | 110.84 USD | 25,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.05` | 810.50 USD | 25,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.15` | 470.54 USD | 25,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.35` | 4,090.00 USD | 25,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.45` | 5,150.00 USD | 25,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.55` | 403.69 USD | 25,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.65` | 30,830.00 USD | 25,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.85` | 3,870.00 USD | 25,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.05` | 2,030.00 USD | 25,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.15` | 389.08 USD | 25,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.35` | 28,940.00 USD | 25,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.45` | 138.92 USD | 25,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.65` | 4,840.00 USD | 25,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.75` | 20,800.00 USD | 25,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.85` | 388.66 USD | 25,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.95` | 10,510.00 USD | 25,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.05` | 116,190.00 USD | 25,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.15` | 221.70 USD | 25,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.25` | 782.32 USD | 25,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.35` | 195.09 USD | 25,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.65` | 788.62 USD | 25,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.75` | 18,730.00 USD | 25,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.85` | 32,440.00 USD | 25,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.15` | 313,870.00 USD | 26,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.25` | 32,310.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.35` | 35,060.00 USD | 26,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.45` | 730.10 USD | 26,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.55` | 701,210.00 USD | 27,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.75` | 2,210.00 USD | 27,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.85` | 490.83 USD | 27,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.25` | 131.55 USD | 27,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.35` | 13,360.00 USD | 27,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.55` | 69,270.00 USD | 27,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.85` | 3,180.00 USD | 27,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.95` | 2,070.00 USD | 27,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.05` | 188.71 USD | 27,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.25` | 1,560.00 USD | 27,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.35` | 855.09 USD | 27,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.45` | 219.52 USD | 27,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.85` | 3,100.00 USD | 27,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.95` | 106.88 USD | 27,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.05` | 13,650.00 USD | 27,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.15` | 3,930.00 USD | 27,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.55` | 8,730.00 USD | 27,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.65` | 30,100.00 USD | 27,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.75` | 136.73 USD | 27,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.85` | 49,280.00 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.05` | 103.78 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.15` | 8,440.00 USD | 27,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.25` | 1,330.00 USD | 27,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.45` | 1,600.00 USD | 27,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.65` | 156.37 USD | 27,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.75` | 151,200.00 USD | 27,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.95` | 503.65 USD | 27,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.05` | 12,620.00 USD | 27,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.25` | 11,980.00 USD | 27,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.65` | 18,040.00 USD | 27,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.25` | 14,540.00 USD | 27,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.65` | 6,420.00 USD | 27,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.75` | 415.39 USD | 27,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.85` | 3,250.00 USD | 27,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.95` | 504.37 USD | 27,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.35` | 49,040.00 USD | 27,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.45` | 8,630.00 USD | 27,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.55` | 136.55 USD | 27,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.65` | 1,110.00 USD | 27,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.95` | 34,240.00 USD | 27,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.05` | 836.00 USD | 27,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.15` | 809.19 USD | 27,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.25` | 68,620.00 USD | 27,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.05` | 1,270.00 USD | 27,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.15` | 50,150.00 USD | 27,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.25` | 48,050.00 USD | 27,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.35` | 2,060.00 USD | 27,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.45` | 7,310.00 USD | 27,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.75` | 2,360.00 USD | 27,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.15` | 4,720.00 USD | 27,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.35` | 4,430.00 USD | 27,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.45` | 12,680.00 USD | 27,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.55` | 494.01 USD | 27,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.75` | 4,870.00 USD | 27,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.95` | 2,080.00 USD | 27,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.05` | 116.24 USD | 27,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.35` | 1,600.00 USD | 27,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.45` | 4,870.00 USD | 27,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.55` | 702.75 USD | 27,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.65` | 7,340.00 USD | 27,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.95` | 1,940.00 USD | 27,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.05` | 70,450.00 USD | 27,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.15` | 5,100,000.00 USD | 32,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.35` | 210.61 USD | 32,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.45` | 289,400.00 USD | 33,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.55` | 236.39 USD | 33,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.75` | 1,950,000.00 USD | 35,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.95` | 2,640.00 USD | 35,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.15` | 23,060.00 USD | 35,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.25` | 3,470.00 USD | 35,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.45` | 151.00 USD | 35,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.75` | 1,150.00 USD | 35,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.95` | 283.04 USD | 35,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.15` | 73,040.00 USD | 35,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.35` | 110,660.00 USD | 35,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.55` | 103.36 USD | 35,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.65` | 2,840.00 USD | 35,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.05` | 3,750.00 USD | 35,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.65` | 1,240.00 USD | 35,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.85` | 601,130.00 USD | 36,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.15` | 3,100.00 USD | 36,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.35` | 15,840.00 USD | 36,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.45` | 28,990.00 USD | 36,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.85` | 7,120.00 USD | 36,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.95` | 106,560.00 USD | 36,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.15` | 89,370.00 USD | 36,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.25` | 2,920.00 USD | 36,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.35` | 8,510.00 USD | 36,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.55` | 103,990.00 USD | 36,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.65` | 587,730.00 USD | 36,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.85` | 2,120.00 USD | 37,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.95` | 78,060.00 USD | 37,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.05` | 166.17 USD | 37,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.15` | 1,730.00 USD | 37,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.35` | 169.45 USD | 37,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.45` | 204.96 USD | 37,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.55` | 1,280.00 USD | 37,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.65` | 443,190.00 USD | 37,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.75` | 28,660.00 USD | 37,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.85` | 510.08 USD | 37,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.15` | 102.22 USD | 37,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.35` | 18,560.00 USD | 37,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.45` | 163.29 USD | 37,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.55` | 344,780.00 USD | 37,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.75` | 178,250.00 USD | 38,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.95` | 521,320.00 USD | 38,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.15` | 1,120.00 USD | 38,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.45` | 1,390,000.00 USD | 40,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.55` | 116.65 USD | 40,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.65` | 16,030.00 USD | 40,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.95` | 234,200.00 USD | 40,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.05` | 2,930.00 USD | 40,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.15` | 123,300.00 USD | 40,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.85` | 4,570,000.00 USD | 44,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.05` | 347.42 USD | 44,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.15` | 5,550.00 USD | 44,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.35` | 22,020.00 USD | 44,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.45` | 8,830.00 USD | 44,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.95` | 1,920.00 USD | 44,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.05` | 1,750,000.00 USD | 46,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.15` | 1,860,000.00 USD | 48,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.25` | 200.97 USD | 48,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.35` | 331,280.00 USD | 48,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.45` | 3,150.00 USD | 48,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.75` | 2,800.00 USD | 48,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.05` | 1,060.00 USD | 48,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.15` | 2,810.00 USD | 48,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.25` | 239.07 USD | 48,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.35` | 46,960.00 USD | 48,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.65` | 8,340.00 USD | 49,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.85` | 995.41 USD | 49,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.15` | 292.89 USD | 49,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.25` | 2,340.00 USD | 49,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.45` | 4,240.00 USD | 49,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.55` | 1,860.00 USD | 49,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.05` | 2,340.00 USD | 49,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.25` | 1,110.00 USD | 49,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.45` | 118.14 USD | 49,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.55` | 1,430.00 USD | 49,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.75` | 4,050.00 USD | 49,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.15` | 8,130.00 USD | 49,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.35` | 197.00 USD | 49,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.45` | 4,900.00 USD | 49,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.85` | 6,280.00 USD | 49,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.15` | 49,270.00 USD | 49,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.65` | 654.25 USD | 49,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.75` | 173,110.00 USD | 49,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.35` | 299.28 USD | 49,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.45` | 237,670.00 USD | 49,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.05` | 45,380.00 USD | 49,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.45` | 27,950.00 USD | 49,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.55` | 655.75 USD | 49,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.65` | 432,810.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.75` | 3,640,000.00 USD | 53,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.05` | 448.14 USD | 53,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.15` | 683,500.00 USD | 54,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.35` | 655.83 USD | 54,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.55` | 102,250.00 USD | 54,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.05` | 2,240.00 USD | 54,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.25` | 85,560.00 USD | 54,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.35` | 21,430.00 USD | 54,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.55` | 410.34 USD | 54,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.75` | 323,500.00 USD | 54,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.85` | 18,950.00 USD | 54,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.95` | 144,610.00 USD | 55,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.15` | 228,980.00 USD | 55,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.45` | 5,980.00 USD | 55,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.55` | 1,060.00 USD | 55,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.85` | 786.48 USD | 55,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.95` | 206,830.00 USD | 55,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.15` | 198.18 USD | 55,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.55` | 1,370.00 USD | 55,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.85` | 681.64 USD | 55,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.15` | 996.90 USD | 55,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.25` | 14,070.00 USD | 55,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.75` | 3,220.00 USD | 55,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.95` | 3,590.00 USD | 55,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.65` | 115.68 USD | 55,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.75` | 2,520.00 USD | 55,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.05` | 46,060.00 USD | 55,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.15` | 5,670,000.00 USD | 61,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.35` | 19,740.00 USD | 61,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.55` | 111,680.00 USD | 61,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.65` | 325,850.00 USD | 61,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.75` | 25,920.00 USD | 61,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.75` | 100.15 USD | 61,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.45` | 446.58 USD | 61,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.35` | 181,940.00 USD | 61,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.45` | 1,570.00 USD | 61,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.05` | 20,480.00 USD | 61,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.45` | 51,730.00 USD | 61,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.05` | 36,010.00 USD | 61,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.15` | 15,580.00 USD | 62,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.35` | 28,070.00 USD | 62,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.45` | 16,540.00 USD | 62,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.85` | 695.40 USD | 62,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.05` | 205.38 USD | 62,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.15` | 104,490.00 USD | 62,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.25` | 245,010.00 USD | 62,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.35` | 205,490.00 USD | 62,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.75` | 146.79 USD | 62,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.95` | 348.15 USD | 62,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.45` | 119.31 USD | 62,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.75` | 263.62 USD | 62,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.85` | 38,690,000.00 USD | 101,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.15` | 19,920.00 USD | 101,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.25` | 625.69 USD | 101,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.35` | 3,530,000.00 USD | 104,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.65` | 105,990.00 USD | 104,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.75` | 204,830.00 USD | 105,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.95` | 265,430.00 USD | 105,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.55` | 25,670.00 USD | 105,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.65` | 637.76 USD | 105,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.95` | 78,300.00 USD | 105,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.35` | 7,280.00 USD | 105,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.45` | 1,320.00 USD | 105,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.05` | 44,780.00 USD | 105,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.25` | 143,400.00 USD | 105,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.45` | 1,040,000.00 USD | 106,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.65` | 718.60 USD | 106,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.75` | 280.41 USD | 106,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.25` | 2,030.00 USD | 106,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.35` | 1,340,000.00 USD | 108,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.55` | 3,970.00 USD | 108,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.05` | 77,440.00 USD | 108,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.15` | 18,120.00 USD | 108,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.55` | 254.17 USD | 108,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.95` | 1,370.00 USD | 108,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.05` | 91,030.00 USD | 108,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.15` | 3,990.00 USD | 108,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.45` | 248.13 USD | 108,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.55` | 9,490.00 USD | 108,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.25` | 1,680.00 USD | 108,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.65` | 2,080.00 USD | 108,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.95` | 165,230.00 USD | 108,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.15` | 10,920.00 USD | 108,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.25` | 737.29 USD | 108,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.45` | 2,770.00 USD | 108,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.65` | 137.38 USD | 108,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.75` | 8,410.00 USD | 108,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.65` | 53,620.00 USD | 108,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.85` | 3,740,000.00 USD | 112,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.95` | 805.75 USD | 112,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.05` | 10,740.00 USD | 112,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.45` | 2,460.00 USD | 112,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.65` | 232.69 USD | 112,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.85` | 1,560.00 USD | 112,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.55` | 231.92 USD | 112,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.65` | 29,110.00 USD | 112,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.95` | 1,450.00 USD | 112,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.05` | 1,000.00 USD | 112,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.25` | 456.09 USD | 112,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.65` | 117.58 USD | 112,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.85` | 189.85 USD | 112,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.95` | 284,930.00 USD | 112,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.15` | 148.32 USD | 112,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.45` | 118.08 USD | 112,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.85` | 118.33 USD | 112,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.95` | 13,570,000.00 USD | 126,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.05` | 278.93 USD | 126,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.55` | 191.55 USD | 126,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.65` | 62,880.00 USD | 126,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.95` | 322.48 USD | 126,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.55` | 5,460.00 USD | 126,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.75` | 385,500.00 USD | 126,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.85` | 19,780.00 USD | 126,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.05` | 9,320.00 USD | 126,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.55` | 114,580.00 USD | 126,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `19.45` | 123,140,000.00 USD | 0.00 USD | 18,100.00 USD | `-79.82%` | `930.46` |
| `Live` | `Long` | `19.85` | 123,120,000.00 USD | 0.00 USD | 18,240.00 USD | `-79.41%` | `919.00` |
| `Live` | `Long` | `19.95` | 123,110,000.00 USD | 0.00 USD | 15,960.00 USD | `-79.30%` | `800.00` |
| `Live` | `Long` | `20.25` | 123,090,000.00 USD | 0.00 USD | 1,720.00 USD | `-78.99%` | `85.17` |
| `Live` | `Long` | `20.55` | 123,090,000.00 USD | 0.00 USD | 4,790.00 USD | `-78.68%` | `233.31` |
| `Live` | `Long` | `20.65` | 123,080,000.00 USD | 0.00 USD | 748.56 USD | `-78.58%` | `36.25` |
| `Live` | `Long` | `21.05` | 123,080,000.00 USD | 0.00 USD | 496.78 USD | `-78.16%` | `23.60` |
| `Live` | `Long` | `21.15` | 123,080,000.00 USD | 0.00 USD | 242.38 USD | `-78.06%` | `11.46` |
| `Live` | `Long` | `21.35` | 123,080,000.00 USD | 0.00 USD | 1,410.00 USD | `-77.85%` | `65.89` |
| `Live` | `Long` | `21.45` | 123,080,000.00 USD | 0.00 USD | 161.73 USD | `-77.75%` | `7.54` |
| `Live` | `Long` | `21.75` | 123,080,000.00 USD | 0.00 USD | 4,630.00 USD | `-77.44%` | `212.70` |
| `Live` | `Long` | `21.95` | 123,080,000.00 USD | 0.00 USD | 1,100.00 USD | `-77.23%` | `50.00` |
| `Live` | `Long` | `22.25` | 123,080,000.00 USD | 0.00 USD | 445.00 USD | `-76.92%` | `20.00` |
| `Live` | `Long` | `22.45` | 123,070,000.00 USD | 0.00 USD | 133.58 USD | `-76.71%` | `5.95` |
| `Live` | `Long` | `22.55` | 123,070,000.00 USD | 0.00 USD | 4,850.00 USD | `-76.61%` | `215.00` |
| `Live` | `Long` | `22.95` | 123,070,000.00 USD | 0.00 USD | 1,260.00 USD | `-76.19%` | `54.95` |
| `Live` | `Long` | `23.05` | 123,070,000.00 USD | 0.00 USD | 1,130.00 USD | `-76.09%` | `49.01` |
| `Live` | `Long` | `23.15` | 123,070,000.00 USD | 0.00 USD | 243.31 USD | `-75.98%` | `10.51` |
| `Live` | `Long` | `23.35` | 123,070,000.00 USD | 0.00 USD | 772.65 USD | `-75.78%` | `33.09` |
| `Live` | `Long` | `23.45` | 123,070,000.00 USD | 0.00 USD | 2,060.00 USD | `-75.67%` | `88.01` |
| `Live` | `Long` | `23.55` | 123,060,000.00 USD | 0.00 USD | 249.63 USD | `-75.57%` | `10.60` |
| `Live` | `Long` | `23.75` | 123,060,000.00 USD | 0.00 USD | 1,560.00 USD | `-75.36%` | `65.63` |
| `Live` | `Long` | `24.15` | 123,060,000.00 USD | 0.00 USD | 18,400.00 USD | `-74.95%` | `762.03` |
| `Live` | `Long` | `24.25` | 123,040,000.00 USD | 0.00 USD | 1,130.00 USD | `-74.84%` | `46.58` |
| `Live` | `Long` | `24.85` | 123,040,000.00 USD | 0.00 USD | 896,730.00 USD | `-74.22%` | `36,085.73` |
| `Live` | `Long` | `25.05` | 122,150,000.00 USD | 0.00 USD | 1,250.00 USD | `-74.01%` | `50.00` |
| `Live` | `Long` | `25.15` | 122,140,000.00 USD | 0.00 USD | 2,010.00 USD | `-73.91%` | `80.00` |
| `Live` | `Long` | `25.25` | 122,140,000.00 USD | 0.00 USD | 5,470.00 USD | `-73.81%` | `216.71` |
| `Live` | `Long` | `25.45` | 122,140,000.00 USD | 0.00 USD | 146,460.00 USD | `-73.60%` | `5,754.63` |
| `Live` | `Long` | `25.65` | 121,990,000.00 USD | 0.00 USD | 9,870.00 USD | `-73.39%` | `384.80` |
| `Live` | `Long` | `25.95` | 121,980,000.00 USD | 0.00 USD | 3,200.00 USD | `-73.08%` | `123.26` |
| `Live` | `Long` | `26.05` | 121,980,000.00 USD | 0.00 USD | 5,210.00 USD | `-72.98%` | `200.00` |
| `Live` | `Long` | `26.25` | 121,970,000.00 USD | 0.00 USD | 136.24 USD | `-72.77%` | `5.19` |
| `Live` | `Long` | `26.35` | 121,970,000.00 USD | 0.00 USD | 217.65 USD | `-72.66%` | `8.26` |
| `Live` | `Long` | `26.55` | 121,970,000.00 USD | 0.00 USD | 13,590.00 USD | `-72.46%` | `512.00` |
| `Live` | `Long` | `26.65` | 121,960,000.00 USD | 0.00 USD | 745.67 USD | `-72.35%` | `27.98` |
| `Live` | `Long` | `26.85` | 121,960,000.00 USD | 0.00 USD | 1,260.00 USD | `-72.15%` | `47.02` |
| `Live` | `Long` | `26.95` | 121,960,000.00 USD | 0.00 USD | 11,460.00 USD | `-72.04%` | `425.19` |
| `Live` | `Long` | `27.15` | 121,950,000.00 USD | 0.00 USD | 25,480.00 USD | `-71.83%` | `938.38` |
| `Live` | `Long` | `27.35` | 121,920,000.00 USD | 0.00 USD | 1,050.00 USD | `-71.63%` | `38.33` |
| `Live` | `Long` | `27.75` | 121,920,000.00 USD | 0.00 USD | 153.18 USD | `-71.21%` | `5.52` |
| `Live` | `Long` | `27.85` | 121,920,000.00 USD | 0.00 USD | 5,980.00 USD | `-71.11%` | `214.80` |
| `Live` | `Long` | `27.95` | 121,910,000.00 USD | 0.00 USD | 747.10 USD | `-71.00%` | `26.73` |
| `Live` | `Long` | `28.05` | 121,910,000.00 USD | 0.00 USD | 2,740.00 USD | `-70.90%` | `97.63` |
| `Live` | `Long` | `28.35` | 121,910,000.00 USD | 0.00 USD | 6,200.00 USD | `-70.59%` | `218.55` |
| `Live` | `Long` | `28.45` | 121,900,000.00 USD | 0.00 USD | 113.80 USD | `-70.49%` | `4.00` |
| `Live` | `Long` | `28.55` | 121,900,000.00 USD | 0.00 USD | 107.06 USD | `-70.38%` | `3.75` |
| `Live` | `Long` | `28.95` | 121,900,000.00 USD | 0.00 USD | 665.85 USD | `-69.97%` | `23.00` |
| `Live` | `Long` | `29.05` | 121,900,000.00 USD | 0.00 USD | 1,770.00 USD | `-69.86%` | `60.81` |
| `Live` | `Long` | `29.15` | 121,900,000.00 USD | 0.00 USD | 87,450.00 USD | `-69.76%` | `3,000.00` |
| `Live` | `Long` | `29.25` | 121,810,000.00 USD | 0.00 USD | 10,680.00 USD | `-69.66%` | `365.00` |
| `Live` | `Long` | `29.35` | 121,800,000.00 USD | 0.00 USD | 843.52 USD | `-69.55%` | `28.74` |
| `Live` | `Long` | `29.45` | 121,800,000.00 USD | 0.00 USD | 59,610.00 USD | `-69.45%` | `2,023.99` |
| `Live` | `Long` | `29.55` | 121,740,000.00 USD | 0.00 USD | 21,130.00 USD | `-69.34%` | `715.00` |
| `Live` | `Long` | `29.65` | 121,720,000.00 USD | 0.00 USD | 131.94 USD | `-69.24%` | `4.45` |
| `Live` | `Long` | `29.95` | 121,720,000.00 USD | 0.00 USD | 239.60 USD | `-68.93%` | `8.00` |
| `Live` | `Long` | `30.05` | 121,720,000.00 USD | 0.00 USD | 3,010.00 USD | `-68.83%` | `100.04` |
| `Live` | `Long` | `30.15` | 121,720,000.00 USD | 0.00 USD | 47,340.00 USD | `-68.72%` | `1,570.00` |
| `Live` | `Long` | `30.45` | 121,670,000.00 USD | 0.00 USD | 4,240.00 USD | `-68.41%` | `139.36` |
| `Live` | `Long` | `30.55` | 121,670,000.00 USD | 0.00 USD | 11,190.00 USD | `-68.31%` | `366.29` |
| `Live` | `Long` | `30.65` | 121,650,000.00 USD | 0.00 USD | 233.86 USD | `-68.20%` | `7.63` |
| `Live` | `Long` | `30.85` | 121,650,000.00 USD | 0.00 USD | 35,990.00 USD | `-68.00%` | `1,166.55` |
| `Live` | `Long` | `31.05` | 121,620,000.00 USD | 0.00 USD | 820.65 USD | `-67.79%` | `26.43` |
| `Live` | `Long` | `31.15` | 121,620,000.00 USD | 0.00 USD | 870.33 USD | `-67.69%` | `27.94` |
| `Live` | `Long` | `31.35` | 121,620,000.00 USD | 0.00 USD | 16,400.00 USD | `-67.48%` | `523.23` |
| `Live` | `Long` | `31.45` | 121,600,000.00 USD | 0.00 USD | 1,020.00 USD | `-67.37%` | `32.37` |
| `Live` | `Long` | `31.95` | 121,600,000.00 USD | 0.00 USD | 2,560.00 USD | `-66.86%` | `80.00` |
| `Live` | `Long` | `32.05` | 121,600,000.00 USD | 0.00 USD | 164.74 USD | `-66.75%` | `5.14` |
| `Live` | `Long` | `32.25` | 121,600,000.00 USD | 0.00 USD | 496.01 USD | `-66.54%` | `15.38` |
| `Live` | `Long` | `32.35` | 121,600,000.00 USD | 0.00 USD | 39,620.00 USD | `-66.44%` | `1,224.78` |
| `Live` | `Long` | `32.45` | 121,560,000.00 USD | 0.00 USD | 1,830.00 USD | `-66.34%` | `56.43` |
| `Live` | `Long` | `32.85` | 121,550,000.00 USD | 0.00 USD | 6,290.00 USD | `-65.92%` | `191.33` |
| `Live` | `Long` | `33.05` | 121,550,000.00 USD | 0.00 USD | 5,410.00 USD | `-65.71%` | `163.78` |
| `Live` | `Long` | `33.55` | 121,540,000.00 USD | 0.00 USD | 4,570.00 USD | `-65.20%` | `136.10` |
| `Live` | `Long` | `33.85` | 121,540,000.00 USD | 0.00 USD | 5,750.00 USD | `-64.88%` | `169.92` |
| `Live` | `Long` | `33.95` | 121,530,000.00 USD | 0.00 USD | 499.40 USD | `-64.78%` | `14.71` |
| `Live` | `Long` | `34.55` | 121,530,000.00 USD | 0.00 USD | 1,490.00 USD | `-64.16%` | `43.14` |
| `Live` | `Long` | `34.65` | 121,530,000.00 USD | 0.00 USD | 486.14 USD | `-64.05%` | `14.03` |
| `Live` | `Long` | `34.75` | 121,530,000.00 USD | 0.00 USD | 8,680.00 USD | `-63.95%` | `249.89` |
| `Live` | `Long` | `34.85` | 121,520,000.00 USD | 0.00 USD | 878.92 USD | `-63.85%` | `25.22` |
| `Live` | `Long` | `35.05` | 121,520,000.00 USD | 0.00 USD | 6,650,000.00 USD | `-63.64%` | `189,675.12` |
| `Live` | `Long` | `35.15` | 114,870,000.00 USD | 0.00 USD | 598,290.00 USD | `-63.54%` | `17,021.03` |
| `Live` | `Long` | `35.65` | 114,270,000.00 USD | 0.00 USD | 99,830.00 USD | `-63.02%` | `2,800.26` |
| `Live` | `Long` | `35.75` | 114,170,000.00 USD | 0.00 USD | 4,990.00 USD | `-62.91%` | `139.48` |
| `Live` | `Long` | `35.95` | 114,170,000.00 USD | 0.00 USD | 557.94 USD | `-62.71%` | `15.52` |
| `Live` | `Long` | `36.05` | 114,170,000.00 USD | 0.00 USD | 5,070.00 USD | `-62.60%` | `140.61` |
| `Live` | `Long` | `36.15` | 114,160,000.00 USD | 0.00 USD | 3,500.00 USD | `-62.50%` | `96.83` |
| `Live` | `Long` | `36.25` | 114,160,000.00 USD | 0.00 USD | 619.51 USD | `-62.39%` | `17.09` |
| `Live` | `Long` | `36.35` | 114,160,000.00 USD | 0.00 USD | 4,410.00 USD | `-62.29%` | `121.32` |
| `Live` | `Long` | `36.45` | 114,150,000.00 USD | 0.00 USD | 2,840.00 USD | `-62.19%` | `77.86` |
| `Live` | `Long` | `36.55` | 114,150,000.00 USD | 0.00 USD | 58,350.00 USD | `-62.08%` | `1,596.58` |
| `Live` | `Long` | `36.75` | 114,090,000.00 USD | 0.00 USD | 748.97 USD | `-61.88%` | `20.38` |
| `Live` | `Long` | `36.85` | 114,090,000.00 USD | 0.00 USD | 546.85 USD | `-61.77%` | `14.84` |
| `Live` | `Long` | `36.95` | 114,090,000.00 USD | 0.00 USD | 1,660.00 USD | `-61.67%` | `45.00` |
| `Live` | `Long` | `37.05` | 114,090,000.00 USD | 0.00 USD | 624.29 USD | `-61.56%` | `16.85` |
| `Live` | `Long` | `37.15` | 114,090,000.00 USD | 0.00 USD | 1,310.00 USD | `-61.46%` | `35.38` |
| `Live` | `Long` | `37.25` | 114,090,000.00 USD | 0.00 USD | 4,280.00 USD | `-61.36%` | `114.97` |
| `Live` | `Long` | `37.35` | 114,080,000.00 USD | 0.00 USD | 19,600.00 USD | `-61.25%` | `524.75` |
| `Live` | `Long` | `37.55` | 114,060,000.00 USD | 0.00 USD | 41,870.00 USD | `-61.05%` | `1,115.13` |
| `Live` | `Long` | `37.65` | 114,020,000.00 USD | 0.00 USD | 2,430.00 USD | `-60.94%` | `64.52` |
| `Live` | `Long` | `37.95` | 114,020,000.00 USD | 0.00 USD | 5,170.00 USD | `-60.63%` | `136.35` |
| `Live` | `Long` | `38.05` | 114,020,000.00 USD | 0.00 USD | 1,630.00 USD | `-60.53%` | `42.73` |
| `Live` | `Long` | `38.15` | 114,010,000.00 USD | 0.00 USD | 2,120.00 USD | `-60.42%` | `55.47` |
| `Live` | `Long` | `38.35` | 114,010,000.00 USD | 0.00 USD | 287.63 USD | `-60.22%` | `7.50` |
| `Live` | `Long` | `38.45` | 114,010,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-60.11%` | `78,000.00` |
| `Live` | `Long` | `38.55` | 111,010,000.00 USD | 0.00 USD | 18,330.00 USD | `-60.01%` | `475.39` |
| `Live` | `Long` | `38.65` | 110,990,000.00 USD | 0.00 USD | 83,250.00 USD | `-59.90%` | `2,154.01` |
| `Live` | `Long` | `38.75` | 110,910,000.00 USD | 0.00 USD | 2,280.00 USD | `-59.80%` | `58.86` |
| `Live` | `Long` | `38.85` | 110,910,000.00 USD | 0.00 USD | 4,270.00 USD | `-59.70%` | `109.96` |
| `Live` | `Long` | `38.95` | 110,900,000.00 USD | 0.00 USD | 2,310.00 USD | `-59.59%` | `59.27` |
| `Live` | `Long` | `39.05` | 110,900,000.00 USD | 0.00 USD | 50,470.00 USD | `-59.49%` | `1,292.50` |
| `Live` | `Long` | `39.15` | 110,850,000.00 USD | 0.00 USD | 195,750.00 USD | `-59.39%` | `5,000.00` |
| `Live` | `Long` | `39.25` | 110,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-59.28%` | `33.68` |
| `Live` | `Long` | `39.35` | 110,650,000.00 USD | 0.00 USD | 7,860.00 USD | `-59.18%` | `199.79` |
| `Live` | `Long` | `39.45` | 110,650,000.00 USD | 0.00 USD | 886.44 USD | `-59.07%` | `22.47` |
| `Live` | `Long` | `39.65` | 110,650,000.00 USD | 0.00 USD | 1,560.00 USD | `-58.87%` | `39.31` |
| `Live` | `Long` | `39.75` | 110,640,000.00 USD | 0.00 USD | 159.00 USD | `-58.76%` | `4.00` |
| `Live` | `Long` | `39.85` | 110,640,000.00 USD | 0.00 USD | 1,270.00 USD | `-58.66%` | `31.86` |
| `Live` | `Long` | `40.05` | 110,640,000.00 USD | 0.00 USD | 1,510.00 USD | `-58.45%` | `37.77` |
| `Live` | `Long` | `40.15` | 110,640,000.00 USD | 0.00 USD | 4,490.00 USD | `-58.35%` | `111.93` |
| `Live` | `Long` | `40.25` | 110,640,000.00 USD | 0.00 USD | 632.73 USD | `-58.24%` | `15.72` |
| `Live` | `Long` | `40.35` | 110,640,000.00 USD | 0.00 USD | 921,810.00 USD | `-58.14%` | `22,845.24` |
| `Live` | `Long` | `40.45` | 109,710,000.00 USD | 0.00 USD | 62,790.00 USD | `-58.04%` | `1,552.17` |
| `Live` | `Long` | `40.55` | 109,650,000.00 USD | 0.00 USD | 9,470.00 USD | `-57.93%` | `233.52` |
| `Live` | `Long` | `40.65` | 109,640,000.00 USD | 0.00 USD | 5,150.00 USD | `-57.83%` | `126.80` |
| `Live` | `Long` | `40.75` | 109,640,000.00 USD | 0.00 USD | 1,070.00 USD | `-57.73%` | `26.36` |
| `Live` | `Long` | `40.85` | 109,640,000.00 USD | 0.00 USD | 3,690.00 USD | `-57.62%` | `90.27` |
| `Live` | `Long` | `40.95` | 109,630,000.00 USD | 0.00 USD | 9,790.00 USD | `-57.52%` | `239.18` |
| `Live` | `Long` | `41.05` | 109,620,000.00 USD | 0.00 USD | 21,580.00 USD | `-57.41%` | `525.58` |
| `Live` | `Long` | `41.15` | 109,600,000.00 USD | 0.00 USD | 2,950.00 USD | `-57.31%` | `71.74` |
| `Live` | `Long` | `41.25` | 109,600,000.00 USD | 0.00 USD | 723.94 USD | `-57.21%` | `17.55` |
| `Live` | `Long` | `41.35` | 109,600,000.00 USD | 0.00 USD | 148.45 USD | `-57.10%` | `3.59` |
| `Live` | `Long` | `41.55` | 109,600,000.00 USD | 0.00 USD | 130.88 USD | `-56.90%` | `3.15` |
| `Live` | `Long` | `41.65` | 109,600,000.00 USD | 0.00 USD | 770.11 USD | `-56.79%` | `18.49` |
| `Live` | `Long` | `41.75` | 109,600,000.00 USD | 0.00 USD | 836.67 USD | `-56.69%` | `20.04` |
| `Live` | `Long` | `41.85` | 109,600,000.00 USD | 0.00 USD | 3,450.00 USD | `-56.58%` | `82.36` |
| `Live` | `Long` | `41.95` | 109,590,000.00 USD | 0.00 USD | 50,440.00 USD | `-56.48%` | `1,202.48` |
| `Live` | `Long` | `42.05` | 109,540,000.00 USD | 0.00 USD | 54,040.00 USD | `-56.38%` | `1,285.08` |
| `Live` | `Long` | `42.15` | 109,490,000.00 USD | 0.00 USD | 8,680.00 USD | `-56.27%` | `205.83` |
| `Live` | `Long` | `42.25` | 109,480,000.00 USD | 0.00 USD | 785.00 USD | `-56.17%` | `18.58` |
| `Live` | `Long` | `42.35` | 109,480,000.00 USD | 0.00 USD | 6,030.00 USD | `-56.07%` | `142.31` |
| `Live` | `Long` | `42.55` | 109,470,000.00 USD | 0.00 USD | 8,210.00 USD | `-55.86%` | `193.00` |
| `Live` | `Long` | `42.85` | 109,460,000.00 USD | 0.00 USD | 44,250.00 USD | `-55.55%` | `1,032.68` |
| `Live` | `Long` | `42.95` | 109,420,000.00 USD | 0.00 USD | 460.85 USD | `-55.44%` | `10.73` |
| `Live` | `Long` | `43.25` | 109,420,000.00 USD | 0.00 USD | 2,150.00 USD | `-55.13%` | `49.79` |
| `Live` | `Long` | `43.35` | 109,420,000.00 USD | 0.00 USD | 25,040.00 USD | `-55.03%` | `577.54` |
| `Live` | `Long` | `43.45` | 109,390,000.00 USD | 0.00 USD | 749.95 USD | `-54.93%` | `17.26` |
| `Live` | `Long` | `43.55` | 109,390,000.00 USD | 0.00 USD | 360.16 USD | `-54.82%` | `8.27` |
| `Live` | `Long` | `43.65` | 109,390,000.00 USD | 0.00 USD | 322.14 USD | `-54.72%` | `7.38` |
| `Live` | `Long` | `43.75` | 109,390,000.00 USD | 0.00 USD | 68,830.00 USD | `-54.61%` | `1,573.15` |
| `Live` | `Long` | `43.85` | 109,320,000.00 USD | 0.00 USD | 764.31 USD | `-54.51%` | `17.43` |
| `Live` | `Long` | `43.95` | 109,320,000.00 USD | 0.00 USD | 242.16 USD | `-54.41%` | `5.51` |
| `Live` | `Long` | `44.05` | 109,320,000.00 USD | 0.00 USD | 671,960.00 USD | `-54.30%` | `15,254.51` |
| `Live` | `Long` | `44.15` | 108,650,000.00 USD | 0.00 USD | 110.82 USD | `-54.20%` | `2.51` |
| `Live` | `Long` | `44.25` | 108,650,000.00 USD | 0.00 USD | 9,160.00 USD | `-54.10%` | `206.90` |
| `Live` | `Long` | `44.35` | 108,640,000.00 USD | 0.00 USD | 4,600.00 USD | `-53.99%` | `103.68` |
| `Live` | `Long` | `44.45` | 108,630,000.00 USD | 0.00 USD | 10,180.00 USD | `-53.89%` | `229.02` |
| `Live` | `Long` | `44.55` | 108,620,000.00 USD | 0.00 USD | 17,870.00 USD | `-53.78%` | `401.03` |
| `Live` | `Long` | `44.65` | 108,610,000.00 USD | 0.00 USD | 410.78 USD | `-53.68%` | `9.20` |
| `Live` | `Long` | `44.75` | 108,610,000.00 USD | 0.00 USD | 1,790.00 USD | `-53.58%` | `39.98` |
| `Live` | `Long` | `44.85` | 108,600,000.00 USD | 0.00 USD | 477.20 USD | `-53.47%` | `10.64` |
| `Live` | `Long` | `44.95` | 108,600,000.00 USD | 0.00 USD | 6,510.00 USD | `-53.37%` | `144.85` |
| `Live` | `Long` | `45.15` | 108,600,000.00 USD | 0.00 USD | 179.70 USD | `-53.16%` | `3.98` |
| `Live` | `Long` | `45.25` | 108,600,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-53.06%` | `25,139.70` |
| `Live` | `Long` | `45.35` | 107,460,000.00 USD | 0.00 USD | 37,590.00 USD | `-52.95%` | `828.95` |
| `Live` | `Long` | `45.45` | 107,420,000.00 USD | 0.00 USD | 9,480.00 USD | `-52.85%` | `208.64` |
| `Live` | `Long` | `45.55` | 107,410,000.00 USD | 0.00 USD | 7,940.00 USD | `-52.75%` | `174.26` |
| `Live` | `Long` | `45.65` | 107,400,000.00 USD | 0.00 USD | 12,760.00 USD | `-52.64%` | `279.53` |
| `Live` | `Long` | `45.75` | 107,390,000.00 USD | 0.00 USD | 9,450.00 USD | `-52.54%` | `206.46` |
| `Live` | `Long` | `45.85` | 107,380,000.00 USD | 0.00 USD | 37,220.00 USD | `-52.44%` | `811.71` |
| `Live` | `Long` | `45.95` | 107,350,000.00 USD | 0.00 USD | 400,220.00 USD | `-52.33%` | `8,709.90` |
| `Live` | `Long` | `46.05` | 106,940,000.00 USD | 0.00 USD | 2,170.00 USD | `-52.23%` | `47.16` |
| `Live` | `Long` | `46.45` | 106,940,000.00 USD | 0.00 USD | 11,610.00 USD | `-51.81%` | `250.00` |
| `Live` | `Long` | `46.55` | 106,930,000.00 USD | 0.00 USD | 2,050.00 USD | `-51.71%` | `43.98` |
| `Live` | `Long` | `46.65` | 106,930,000.00 USD | 0.00 USD | 542.07 USD | `-51.61%` | `11.62` |
| `Live` | `Long` | `46.75` | 106,930,000.00 USD | 0.00 USD | 537.62 USD | `-51.50%` | `11.50` |
| `Live` | `Long` | `46.85` | 106,930,000.00 USD | 0.00 USD | 140.55 USD | `-51.40%` | `3.00` |
| `Live` | `Long` | `46.95` | 106,930,000.00 USD | 0.00 USD | 3,260.00 USD | `-51.29%` | `69.48` |
| `Live` | `Long` | `47.15` | 106,920,000.00 USD | 0.00 USD | 1,570.00 USD | `-51.09%` | `33.22` |
| `Live` | `Long` | `47.25` | 106,920,000.00 USD | 0.00 USD | 3,700.00 USD | `-50.98%` | `78.21` |
| `Live` | `Long` | `47.35` | 106,920,000.00 USD | 0.00 USD | 3,880,000.00 USD | `-50.88%` | `81,851.78` |
| `Live` | `Long` | `47.55` | 103,040,000.00 USD | 0.00 USD | 106.04 USD | `-50.67%` | `2.23` |
| `Live` | `Long` | `47.65` | 103,040,000.00 USD | 0.00 USD | 99,280.00 USD | `-50.57%` | `2,083.61` |
| `Live` | `Long` | `47.75` | 102,940,000.00 USD | 0.00 USD | 56,650.00 USD | `-50.46%` | `1,186.40` |
| `Live` | `Long` | `47.85` | 102,890,000.00 USD | 0.00 USD | 10,290.00 USD | `-50.36%` | `215.05` |
| `Live` | `Long` | `48.05` | 102,880,000.00 USD | 0.00 USD | 14,010.00 USD | `-50.15%` | `291.51` |
| `Live` | `Long` | `48.15` | 102,860,000.00 USD | 0.00 USD | 6,300.00 USD | `-50.05%` | `130.93` |
| `Live` | `Long` | `48.25` | 102,860,000.00 USD | 0.00 USD | 3,980.00 USD | `-49.95%` | `82.45` |
| `Live` | `Long` | `48.35` | 102,850,000.00 USD | 0.00 USD | 5,630.00 USD | `-49.84%` | `116.44` |
| `Live` | `Long` | `48.45` | 102,850,000.00 USD | 0.00 USD | 2,930.00 USD | `-49.74%` | `60.44` |
| `Live` | `Long` | `48.55` | 102,840,000.00 USD | 0.00 USD | 97,530.00 USD | `-49.63%` | `2,008.83` |
| `Live` | `Long` | `48.65` | 102,750,000.00 USD | 0.00 USD | 9,260.00 USD | `-49.53%` | `190.42` |
| `Live` | `Long` | `48.75` | 102,740,000.00 USD | 0.00 USD | 58,330.00 USD | `-49.43%` | `1,196.55` |
| `Live` | `Long` | `48.85` | 102,680,000.00 USD | 0.00 USD | 14,260.00 USD | `-49.32%` | `291.88` |
| `Live` | `Long` | `48.95` | 102,670,000.00 USD | 0.00 USD | 1,250.00 USD | `-49.22%` | `25.51` |
| `Live` | `Long` | `49.05` | 102,660,000.00 USD | 0.00 USD | 5,800.00 USD | `-49.12%` | `118.27` |
| `Live` | `Long` | `49.25` | 102,660,000.00 USD | 0.00 USD | 21,190.00 USD | `-48.91%` | `430.30` |
| `Live` | `Long` | `49.35` | 102,640,000.00 USD | 0.00 USD | 585.29 USD | `-48.80%` | `11.86` |
| `Live` | `Long` | `49.45` | 102,640,000.00 USD | 0.00 USD | 15,560.00 USD | `-48.70%` | `314.65` |
| `Live` | `Long` | `49.55` | 102,620,000.00 USD | 0.00 USD | 777,020.00 USD | `-48.60%` | `15,681.62` |
| `Live` | `Long` | `49.65` | 101,840,000.00 USD | 0.00 USD | 9,200.00 USD | `-48.49%` | `185.21` |
| `Live` | `Long` | `49.75` | 101,830,000.00 USD | 0.00 USD | 12,330.00 USD | `-48.39%` | `247.90` |
| `Live` | `Long` | `49.85` | 101,820,000.00 USD | 0.00 USD | 42,210.00 USD | `-48.29%` | `846.70` |
| `Live` | `Long` | `49.95` | 101,780,000.00 USD | 0.00 USD | 22,720.00 USD | `-48.18%` | `454.83` |
| `Live` | `Long` | `50.05` | 101,760,000.00 USD | 0.00 USD | 9,450.00 USD | `-48.08%` | `188.80` |
| `Live` | `Long` | `50.15` | 101,750,000.00 USD | 0.00 USD | 4,070.00 USD | `-47.97%` | `81.09` |
| `Live` | `Long` | `50.25` | 101,740,000.00 USD | 0.00 USD | 8,170.00 USD | `-47.87%` | `162.55` |
| `Live` | `Long` | `50.35` | 101,740,000.00 USD | 0.00 USD | 7,880.00 USD | `-47.77%` | `156.51` |
| `Live` | `Long` | `50.45` | 101,730,000.00 USD | 0.00 USD | 4,800.00 USD | `-47.66%` | `95.10` |
| `Live` | `Long` | `50.55` | 101,720,000.00 USD | 0.00 USD | 2,400.00 USD | `-47.56%` | `47.47` |
| `Live` | `Long` | `50.65` | 101,720,000.00 USD | 0.00 USD | 843.83 USD | `-47.46%` | `16.66` |
| `Live` | `Long` | `50.75` | 101,720,000.00 USD | 0.00 USD | 12,800.00 USD | `-47.35%` | `252.21` |
| `Live` | `Long` | `50.85` | 101,710,000.00 USD | 0.00 USD | 20,000.00 USD | `-47.25%` | `393.39` |
| `Live` | `Long` | `50.95` | 101,690,000.00 USD | 0.00 USD | 12,540.00 USD | `-47.14%` | `246.18` |
| `Live` | `Long` | `51.05` | 101,670,000.00 USD | 0.00 USD | 13,390.00 USD | `-47.04%` | `262.21` |
| `Live` | `Long` | `51.15` | 101,660,000.00 USD | 0.00 USD | 3,170.00 USD | `-46.94%` | `61.92` |
| `Live` | `Long` | `51.25` | 101,660,000.00 USD | 0.00 USD | 10,390.00 USD | `-46.83%` | `202.74` |
| `Live` | `Long` | `51.35` | 101,650,000.00 USD | 0.00 USD | 5,990.00 USD | `-46.73%` | `116.62` |
| `Live` | `Long` | `51.45` | 101,640,000.00 USD | 0.00 USD | 4,540.00 USD | `-46.63%` | `88.31` |
| `Live` | `Long` | `51.55` | 101,640,000.00 USD | 0.00 USD | 137,150.00 USD | `-46.52%` | `2,660.60` |
| `Live` | `Long` | `51.65` | 101,500,000.00 USD | 0.00 USD | 7,720.00 USD | `-46.42%` | `149.52` |
| `Live` | `Long` | `51.75` | 101,490,000.00 USD | 0.00 USD | 24,770.00 USD | `-46.31%` | `478.71` |
| `Live` | `Long` | `51.85` | 101,470,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-46.21%` | `24,889.34` |
| `Live` | `Long` | `51.95` | 100,180,000.00 USD | 0.00 USD | 469,860.00 USD | `-46.11%` | `9,044.37` |
| `Live` | `Long` | `52.15` | 99,710,000.00 USD | 0.00 USD | 99,630.00 USD | `-45.90%` | `1,910.43` |
| `Live` | `Long` | `52.25` | 99,610,000.00 USD | 0.00 USD | 1,550.00 USD | `-45.80%` | `29.66` |
| `Live` | `Long` | `52.35` | 99,610,000.00 USD | 0.00 USD | 1,030.00 USD | `-45.69%` | `19.66` |
| `Live` | `Long` | `52.45` | 99,600,000.00 USD | 0.00 USD | 4,780.00 USD | `-45.59%` | `91.07` |
| `Live` | `Long` | `52.55` | 99,600,000.00 USD | 0.00 USD | 11,110.00 USD | `-45.48%` | `211.45` |
| `Live` | `Long` | `52.65` | 99,590,000.00 USD | 0.00 USD | 2,630.00 USD | `-45.38%` | `50.00` |
| `Live` | `Long` | `52.75` | 99,590,000.00 USD | 0.00 USD | 30,770.00 USD | `-45.28%` | `583.33` |
| `Live` | `Long` | `52.85` | 99,560,000.00 USD | 0.00 USD | 9,370.00 USD | `-45.17%` | `177.38` |
| `Live` | `Long` | `52.95` | 99,550,000.00 USD | 0.00 USD | 5,320.00 USD | `-45.07%` | `100.41` |
| `Live` | `Long` | `53.05` | 99,540,000.00 USD | 0.00 USD | 5,120.00 USD | `-44.97%` | `96.59` |
| `Live` | `Long` | `53.15` | 99,540,000.00 USD | 0.00 USD | 7,910.00 USD | `-44.86%` | `148.83` |
| `Live` | `Long` | `53.25` | 99,530,000.00 USD | 0.00 USD | 24,120.00 USD | `-44.76%` | `452.99` |
| `Live` | `Long` | `53.35` | 99,500,000.00 USD | 0.00 USD | 2,930.00 USD | `-44.65%` | `54.90` |
| `Live` | `Long` | `53.45` | 99,500,000.00 USD | 0.00 USD | 34,210.00 USD | `-44.55%` | `639.97` |
| `Live` | `Long` | `53.55` | 99,470,000.00 USD | 0.00 USD | 44,230.00 USD | `-44.45%` | `826.05` |
| `Live` | `Long` | `53.65` | 99,420,000.00 USD | 0.00 USD | 334.24 USD | `-44.34%` | `6.23` |
| `Live` | `Long` | `53.75` | 99,420,000.00 USD | 0.00 USD | 3,600.00 USD | `-44.24%` | `67.00` |
| `Live` | `Long` | `53.85` | 99,420,000.00 USD | 0.00 USD | 27,060.00 USD | `-44.14%` | `502.46` |
| `Live` | `Long` | `53.95` | 99,390,000.00 USD | 0.00 USD | 69,370.00 USD | `-44.03%` | `1,285.73` |
| `Live` | `Long` | `54.05` | 99,320,000.00 USD | 0.00 USD | 350.78 USD | `-43.93%` | `6.49` |
| `Live` | `Long` | `54.15` | 99,320,000.00 USD | 0.00 USD | 19,470.00 USD | `-43.82%` | `359.63` |
| `Live` | `Long` | `54.25` | 99,300,000.00 USD | 0.00 USD | 5,360.00 USD | `-43.72%` | `98.83` |
| `Live` | `Long` | `54.35` | 99,300,000.00 USD | 0.00 USD | 30,500.00 USD | `-43.62%` | `561.12` |
| `Live` | `Long` | `54.45` | 99,270,000.00 USD | 0.00 USD | 753.04 USD | `-43.51%` | `13.83` |
| `Live` | `Long` | `54.55` | 99,270,000.00 USD | 0.00 USD | 62,540.00 USD | `-43.41%` | `1,146.45` |
| `Live` | `Long` | `54.65` | 99,200,000.00 USD | 0.00 USD | 3,290.00 USD | `-43.31%` | `60.21` |
| `Live` | `Long` | `54.75` | 99,200,000.00 USD | 0.00 USD | 15,140.00 USD | `-43.20%` | `276.50` |
| `Live` | `Long` | `54.85` | 99,180,000.00 USD | 0.00 USD | 858,930.00 USD | `-43.10%` | `15,659.66` |
| `Live` | `Long` | `54.95` | 98,330,000.00 USD | 0.00 USD | 151,380.00 USD | `-42.99%` | `2,754.84` |
| `Live` | `Long` | `55.05` | 98,170,000.00 USD | 0.00 USD | 722.26 USD | `-42.89%` | `13.12` |
| `Live` | `Long` | `55.15` | 98,170,000.00 USD | 0.00 USD | 1,550.00 USD | `-42.79%` | `28.06` |
| `Live` | `Long` | `55.25` | 98,170,000.00 USD | 0.00 USD | 1,900.00 USD | `-42.68%` | `34.45` |
| `Live` | `Long` | `55.35` | 98,170,000.00 USD | 0.00 USD | 9,920.00 USD | `-42.58%` | `179.16` |
| `Live` | `Long` | `55.45` | 98,160,000.00 USD | 0.00 USD | 8,670.00 USD | `-42.48%` | `156.35` |
| `Live` | `Long` | `55.55` | 98,150,000.00 USD | 0.00 USD | 16,200.00 USD | `-42.37%` | `291.69` |
| `Live` | `Long` | `55.65` | 98,130,000.00 USD | 0.00 USD | 11,490.00 USD | `-42.27%` | `206.41` |
| `Live` | `Long` | `55.75` | 98,120,000.00 USD | 0.00 USD | 232,500.00 USD | `-42.17%` | `4,170.46` |
| `Live` | `Long` | `55.85` | 97,890,000.00 USD | 0.00 USD | 3,530.00 USD | `-42.06%` | `63.22` |
| `Live` | `Long` | `55.95` | 97,890,000.00 USD | 0.00 USD | 7,050.00 USD | `-41.96%` | `125.95` |
| `Live` | `Long` | `56.05` | 97,880,000.00 USD | 0.00 USD | 9,470.00 USD | `-41.85%` | `169.01` |
| `Live` | `Long` | `56.15` | 97,870,000.00 USD | 0.00 USD | 37,740.00 USD | `-41.75%` | `672.10` |
| `Live` | `Long` | `56.25` | 97,830,000.00 USD | 0.00 USD | 17,970.00 USD | `-41.65%` | `319.43` |
| `Live` | `Long` | `56.35` | 97,820,000.00 USD | 0.00 USD | 22,200.00 USD | `-41.54%` | `393.91` |
| `Live` | `Long` | `56.45` | 97,790,000.00 USD | 0.00 USD | 17,880.00 USD | `-41.44%` | `316.72` |
| `Live` | `Long` | `56.55` | 97,780,000.00 USD | 0.00 USD | 355,340.00 USD | `-41.34%` | `6,283.63` |
| `Live` | `Long` | `56.65` | 97,420,000.00 USD | 0.00 USD | 3,700.00 USD | `-41.23%` | `65.40` |
| `Live` | `Long` | `56.75` | 97,420,000.00 USD | 0.00 USD | 9,410.00 USD | `-41.13%` | `165.87` |
| `Live` | `Long` | `56.85` | 97,410,000.00 USD | 0.00 USD | 12,000.00 USD | `-41.02%` | `211.05` |
| `Live` | `Long` | `56.95` | 97,390,000.00 USD | 0.00 USD | 2,780,000.00 USD | `-40.92%` | `48,815.94` |
| `Live` | `Long` | `57.05` | 94,610,000.00 USD | 0.00 USD | 3,620.00 USD | `-40.82%` | `63.42` |
| `Live` | `Long` | `57.15` | 94,610,000.00 USD | 0.00 USD | 5,740.00 USD | `-40.71%` | `100.36` |
| `Live` | `Long` | `57.25` | 94,610,000.00 USD | 0.00 USD | 1,270.00 USD | `-40.61%` | `22.11` |
| `Live` | `Long` | `57.35` | 94,600,000.00 USD | 0.00 USD | 8,840.00 USD | `-40.51%` | `154.09` |
| `Live` | `Long` | `57.45` | 94,600,000.00 USD | 0.00 USD | 19,200.00 USD | `-40.40%` | `334.25` |
| `Live` | `Long` | `57.55` | 94,580,000.00 USD | 0.00 USD | 1,390.00 USD | `-40.30%` | `24.22` |
| `Live` | `Long` | `57.65` | 94,570,000.00 USD | 0.00 USD | 12,790.00 USD | `-40.19%` | `221.85` |
| `Live` | `Long` | `57.75` | 94,560,000.00 USD | 0.00 USD | 3,130.00 USD | `-40.09%` | `54.14` |
| `Live` | `Long` | `57.85` | 94,560,000.00 USD | 0.00 USD | 27,330.00 USD | `-39.99%` | `472.35` |
| `Live` | `Long` | `57.95` | 94,530,000.00 USD | 0.00 USD | 32,460.00 USD | `-39.88%` | `560.10` |
| `Live` | `Long` | `58.05` | 94,500,000.00 USD | 0.00 USD | 4,710.00 USD | `-39.78%` | `81.10` |
| `Live` | `Long` | `58.15` | 94,490,000.00 USD | 0.00 USD | 124,360.00 USD | `-39.68%` | `2,138.54` |
| `Live` | `Long` | `58.25` | 94,370,000.00 USD | 0.00 USD | 6,670.00 USD | `-39.57%` | `114.44` |
| `Live` | `Long` | `58.35` | 94,360,000.00 USD | 0.00 USD | 28,010.00 USD | `-39.47%` | `480.09` |
| `Live` | `Long` | `58.45` | 94,340,000.00 USD | 0.00 USD | 463.51 USD | `-39.36%` | `7.93` |
| `Live` | `Long` | `58.55` | 94,330,000.00 USD | 0.00 USD | 49,380.00 USD | `-39.26%` | `843.30` |
| `Live` | `Long` | `58.65` | 94,290,000.00 USD | 0.00 USD | 11,370.00 USD | `-39.16%` | `193.94` |
| `Live` | `Long` | `58.75` | 94,270,000.00 USD | 0.00 USD | 195.64 USD | `-39.05%` | `3.33` |
| `Live` | `Long` | `58.85` | 94,270,000.00 USD | 0.00 USD | 6,130.00 USD | `-38.95%` | `104.08` |
| `Live` | `Long` | `58.95` | 94,270,000.00 USD | 0.00 USD | 62,270.00 USD | `-38.85%` | `1,056.32` |
| `Live` | `Long` | `59.05` | 94,210,000.00 USD | 0.00 USD | 3,780.00 USD | `-38.74%` | `63.97` |
| `Live` | `Long` | `59.15` | 94,200,000.00 USD | 0.00 USD | 15,720.00 USD | `-38.64%` | `265.70` |
| `Live` | `Long` | `59.25` | 94,190,000.00 USD | 0.00 USD | 46,730.00 USD | `-38.53%` | `788.65` |
| `Live` | `Long` | `59.35` | 94,140,000.00 USD | 0.00 USD | 28,850.00 USD | `-38.43%` | `486.15` |
| `Live` | `Long` | `59.45` | 94,110,000.00 USD | 0.00 USD | 4,230.00 USD | `-38.33%` | `71.12` |
| `Live` | `Long` | `59.55` | 94,110,000.00 USD | 0.00 USD | 14,560.00 USD | `-38.22%` | `244.57` |
| `Live` | `Long` | `59.65` | 94,090,000.00 USD | 0.00 USD | 18,840.00 USD | `-38.12%` | `315.85` |
| `Live` | `Long` | `59.75` | 94,070,000.00 USD | 0.00 USD | 22,540.00 USD | `-38.02%` | `377.28` |
| `Live` | `Long` | `59.85` | 94,050,000.00 USD | 0.00 USD | 28,800.00 USD | `-37.91%` | `481.25` |
| `Live` | `Long` | `59.95` | 94,020,000.00 USD | 0.00 USD | 38,660.00 USD | `-37.81%` | `644.88` |
| `Live` | `Long` | `60.05` | 93,980,000.00 USD | 0.00 USD | 19,630.00 USD | `-37.70%` | `326.86` |
| `Live` | `Long` | `60.15` | 93,960,000.00 USD | 0.00 USD | 2,470,000.00 USD | `-37.60%` | `41,032.55` |
| `Live` | `Long` | `60.25` | 91,490,000.00 USD | 0.00 USD | 745.29 USD | `-37.50%` | `12.37` |
| `Live` | `Long` | `60.35` | 91,490,000.00 USD | 0.00 USD | 3,930.00 USD | `-37.39%` | `65.10` |
| `Live` | `Long` | `60.45` | 91,490,000.00 USD | 0.00 USD | 38,080.00 USD | `-37.29%` | `630.00` |
| `Live` | `Long` | `60.55` | 91,450,000.00 USD | 0.00 USD | 8,210.00 USD | `-37.19%` | `135.51` |
| `Live` | `Long` | `60.65` | 91,440,000.00 USD | 0.00 USD | 711.42 USD | `-37.08%` | `11.73` |
| `Live` | `Long` | `60.75` | 91,440,000.00 USD | 0.00 USD | 6,520.00 USD | `-36.98%` | `107.26` |
| `Live` | `Long` | `60.85` | 91,440,000.00 USD | 0.00 USD | 28,890.00 USD | `-36.87%` | `474.84` |
| `Live` | `Long` | `60.95` | 91,410,000.00 USD | 0.00 USD | 55,160.00 USD | `-36.77%` | `905.08` |
| `Live` | `Long` | `61.05` | 91,350,000.00 USD | 0.00 USD | 4,230.00 USD | `-36.67%` | `69.34` |
| `Live` | `Long` | `61.15` | 91,350,000.00 USD | 0.00 USD | 4,870.00 USD | `-36.56%` | `79.64` |
| `Live` | `Long` | `61.25` | 91,340,000.00 USD | 0.00 USD | 4,630.00 USD | `-36.46%` | `75.67` |
| `Live` | `Long` | `61.35` | 91,340,000.00 USD | 0.00 USD | 10,170.00 USD | `-36.36%` | `165.83` |
| `Live` | `Long` | `61.45` | 91,330,000.00 USD | 0.00 USD | 20,920.00 USD | `-36.25%` | `340.48` |
| `Live` | `Long` | `61.55` | 91,310,000.00 USD | 0.00 USD | 121.87 USD | `-36.15%` | `1.98` |
| `Live` | `Long` | `61.65` | 91,310,000.00 USD | 0.00 USD | 18,880.00 USD | `-36.04%` | `306.22` |
| `Live` | `Long` | `61.75` | 91,290,000.00 USD | 0.00 USD | 21,030.00 USD | `-35.94%` | `340.52` |
| `Live` | `Long` | `61.85` | 91,270,000.00 USD | 0.00 USD | 21,260.00 USD | `-35.84%` | `343.81` |
| `Live` | `Long` | `61.95` | 91,250,000.00 USD | 0.00 USD | 22,840.00 USD | `-35.73%` | `368.75` |
| `Live` | `Long` | `62.05` | 91,220,000.00 USD | 0.00 USD | 9,000.00 USD | `-35.63%` | `145.05` |
| `Live` | `Long` | `62.15` | 91,210,000.00 USD | 0.00 USD | 25,540.00 USD | `-35.53%` | `410.91` |
| `Live` | `Long` | `62.25` | 91,190,000.00 USD | 0.00 USD | 1,800.00 USD | `-35.42%` | `28.90` |
| `Live` | `Long` | `62.35` | 91,190,000.00 USD | 0.00 USD | 20,700.00 USD | `-35.32%` | `331.95` |
| `Live` | `Long` | `62.45` | 91,170,000.00 USD | 0.00 USD | 20,480.00 USD | `-35.21%` | `327.96` |
| `Live` | `Long` | `62.55` | 91,150,000.00 USD | 0.00 USD | 140,760.00 USD | `-35.11%` | `2,250.35` |
| `Live` | `Long` | `62.65` | 91,010,000.00 USD | 0.00 USD | 41,340.00 USD | `-35.01%` | `659.81` |
| `Live` | `Long` | `62.75` | 90,960,000.00 USD | 0.00 USD | 3,140.00 USD | `-34.90%` | `49.97` |
| `Live` | `Long` | `62.85` | 90,960,000.00 USD | 0.00 USD | 31,310.00 USD | `-34.80%` | `498.17` |
| `Live` | `Long` | `62.95` | 90,930,000.00 USD | 0.00 USD | 56,830.00 USD | `-34.70%` | `902.71` |
| `Live` | `Long` | `63.05` | 90,870,000.00 USD | 0.00 USD | 26,110.00 USD | `-34.59%` | `414.11` |
| `Live` | `Long` | `63.15` | 90,850,000.00 USD | 0.00 USD | 82,440.00 USD | `-34.49%` | `1,305.44` |
| `Live` | `Long` | `63.25` | 90,760,000.00 USD | 0.00 USD | 14,770.00 USD | `-34.38%` | `233.52` |
| `Live` | `Long` | `63.45` | 90,750,000.00 USD | 0.00 USD | 1,360.00 USD | `-34.18%` | `21.42` |
| `Live` | `Long` | `63.55` | 90,750,000.00 USD | 0.00 USD | 49,290.00 USD | `-34.07%` | `775.56` |
| `Live` | `Long` | `63.65` | 90,700,000.00 USD | 0.00 USD | 18,490.00 USD | `-33.97%` | `290.57` |
| `Live` | `Long` | `63.75` | 90,680,000.00 USD | 0.00 USD | 32,540.00 USD | `-33.87%` | `510.36` |
| `Live` | `Long` | `63.85` | 90,650,000.00 USD | 0.00 USD | 36,960.00 USD | `-33.76%` | `578.89` |
| `Live` | `Long` | `63.95` | 90,610,000.00 USD | 0.00 USD | 5,480.00 USD | `-33.66%` | `85.70` |
| `Live` | `Long` | `64.15` | 90,610,000.00 USD | 0.00 USD | 160.38 USD | `-33.45%` | `2.50` |
| `Live` | `Long` | `64.25` | 90,610,000.00 USD | 0.00 USD | 5,090.00 USD | `-33.35%` | `79.27` |
| `Live` | `Long` | `64.35` | 90,600,000.00 USD | 0.00 USD | 875.16 USD | `-33.24%` | `13.60` |
| `Live` | `Long` | `64.45` | 90,600,000.00 USD | 0.00 USD | 7,090.00 USD | `-33.14%` | `110.04` |
| `Live` | `Long` | `64.55` | 90,590,000.00 USD | 0.00 USD | 579.66 USD | `-33.04%` | `8.98` |
| `Live` | `Long` | `64.65` | 90,590,000.00 USD | 0.00 USD | 1,740.00 USD | `-32.93%` | `26.99` |
| `Live` | `Long` | `64.75` | 90,590,000.00 USD | 0.00 USD | 18,230.00 USD | `-32.83%` | `281.58` |
| `Live` | `Long` | `64.85` | 90,570,000.00 USD | 0.00 USD | 396.23 USD | `-32.72%` | `6.11` |
| `Live` | `Long` | `64.95` | 90,570,000.00 USD | 0.00 USD | 209.79 USD | `-32.62%` | `3.23` |
| `Live` | `Long` | `65.05` | 90,570,000.00 USD | 0.00 USD | 247,180.00 USD | `-32.52%` | `3,799.85` |
| `Live` | `Long` | `65.15` | 90,320,000.00 USD | 0.00 USD | 12,510.00 USD | `-32.41%` | `192.07` |
| `Live` | `Long` | `65.25` | 90,310,000.00 USD | 0.00 USD | 16,400.00 USD | `-32.31%` | `251.41` |
| `Live` | `Long` | `65.35` | 90,290,000.00 USD | 0.00 USD | 57,020.00 USD | `-32.21%` | `872.59` |
| `Live` | `Long` | `65.45` | 90,240,000.00 USD | 0.00 USD | 102,230.00 USD | `-32.10%` | `1,561.89` |
| `Live` | `Long` | `65.55` | 90,140,000.00 USD | 0.00 USD | 10,470.00 USD | `-32.00%` | `159.76` |
| `Live` | `Long` | `65.65` | 90,130,000.00 USD | 0.00 USD | 60,250.00 USD | `-31.89%` | `917.71` |
| `Live` | `Long` | `65.75` | 90,060,000.00 USD | 0.00 USD | 5,370.00 USD | `-31.79%` | `81.62` |
| `Live` | `Long` | `65.85` | 90,060,000.00 USD | 0.00 USD | 1,300.00 USD | `-31.69%` | `19.81` |
| `Live` | `Long` | `65.95` | 90,060,000.00 USD | 0.00 USD | 108,010.00 USD | `-31.58%` | `1,637.71` |
| `Live` | `Long` | `66.05` | 89,950,000.00 USD | 0.00 USD | 6,280.00 USD | `-31.48%` | `95.15` |
| `Live` | `Long` | `66.25` | 89,940,000.00 USD | 0.00 USD | 15,490.00 USD | `-31.27%` | `233.79` |
| `Live` | `Long` | `66.35` | 89,930,000.00 USD | 0.00 USD | 1,810.00 USD | `-31.17%` | `27.33` |
| `Live` | `Long` | `66.45` | 89,930,000.00 USD | 0.00 USD | 10,990.00 USD | `-31.06%` | `165.37` |
| `Live` | `Long` | `66.55` | 89,920,000.00 USD | 0.00 USD | 56,020.00 USD | `-30.96%` | `841.75` |
| `Live` | `Long` | `66.65` | 89,860,000.00 USD | 0.00 USD | 68,880.00 USD | `-30.86%` | `1,033.44` |
| `Live` | `Long` | `66.75` | 89,790,000.00 USD | 0.00 USD | 12,210.00 USD | `-30.75%` | `182.96` |
| `Live` | `Long` | `66.85` | 89,780,000.00 USD | 0.00 USD | 6,010.00 USD | `-30.65%` | `89.90` |
| `Live` | `Long` | `66.95` | 89,770,000.00 USD | 0.00 USD | 937.30 USD | `-30.55%` | `14.00` |
| `Live` | `Long` | `67.05` | 89,770,000.00 USD | 0.00 USD | 42,080.00 USD | `-30.44%` | `627.62` |
| `Live` | `Long` | `67.15` | 89,730,000.00 USD | 0.00 USD | 46,040.00 USD | `-30.34%` | `685.65` |
| `Live` | `Long` | `67.25` | 89,680,000.00 USD | 0.00 USD | 10,190.00 USD | `-30.23%` | `151.47` |
| `Live` | `Long` | `67.35` | 89,670,000.00 USD | 0.00 USD | 23,070.00 USD | `-30.13%` | `342.55` |
| `Live` | `Long` | `67.45` | 89,650,000.00 USD | 0.00 USD | 22,930.00 USD | `-30.03%` | `339.94` |
| `Live` | `Long` | `67.55` | 89,630,000.00 USD | 0.00 USD | 53,160.00 USD | `-29.92%` | `786.93` |
| `Live` | `Long` | `67.65` | 89,570,000.00 USD | 0.00 USD | 160,750.00 USD | `-29.82%` | `2,376.17` |
| `Live` | `Long` | `67.75` | 89,410,000.00 USD | 0.00 USD | 11,150.00 USD | `-29.72%` | `164.59` |
| `Live` | `Long` | `67.85` | 89,400,000.00 USD | 0.00 USD | 32,710.00 USD | `-29.61%` | `482.02` |
| `Live` | `Long` | `68.05` | 89,370,000.00 USD | 0.00 USD | 259,070.00 USD | `-29.41%` | `3,807.08` |
| `Live` | `Long` | `68.15` | 89,110,000.00 USD | 0.00 USD | 37,490,000.00 USD | `-29.30%` | `550,112.64` |
| `Live` | `Long` | `68.25` | 51,620,000.00 USD | 0.00 USD | 13,820.00 USD | `-29.20%` | `202.43` |
| `Live` | `Long` | `68.35` | 51,610,000.00 USD | 0.00 USD | 2,860.00 USD | `-29.09%` | `41.82` |
| `Live` | `Long` | `68.45` | 51,600,000.00 USD | 0.00 USD | 18,450.00 USD | `-28.99%` | `269.55` |
| `Live` | `Long` | `68.55` | 51,590,000.00 USD | 0.00 USD | 3,260.00 USD | `-28.89%` | `47.60` |
| `Live` | `Long` | `68.65` | 51,580,000.00 USD | 0.00 USD | 6,610.00 USD | `-28.78%` | `96.35` |
| `Live` | `Long` | `68.75` | 51,580,000.00 USD | 0.00 USD | 162,300.00 USD | `-28.68%` | `2,360.72` |
| `Live` | `Long` | `68.85` | 51,410,000.00 USD | 0.00 USD | 3,260.00 USD | `-28.58%` | `47.36` |
| `Live` | `Long` | `68.95` | 51,410,000.00 USD | 0.00 USD | 45,480.00 USD | `-28.47%` | `659.55` |
| `Live` | `Long` | `69.05` | 51,360,000.00 USD | 0.00 USD | 145.70 USD | `-28.37%` | `2.11` |
| `Live` | `Long` | `69.15` | 51,360,000.00 USD | 0.00 USD | 24,130.00 USD | `-28.26%` | `348.94` |
| `Live` | `Long` | `69.25` | 51,340,000.00 USD | 0.00 USD | 3,140.00 USD | `-28.16%` | `45.34` |
| `Live` | `Long` | `69.35` | 51,340,000.00 USD | 0.00 USD | 772,100.00 USD | `-28.06%` | `11,133.44` |
| `Live` | `Long` | `69.45` | 50,560,000.00 USD | 0.00 USD | 14,370.00 USD | `-27.95%` | `206.85` |
| `Live` | `Long` | `69.55` | 50,550,000.00 USD | 0.00 USD | 10,540.00 USD | `-27.85%` | `151.60` |
| `Live` | `Long` | `69.65` | 50,540,000.00 USD | 0.00 USD | 3,660.00 USD | `-27.75%` | `52.48` |
| `Live` | `Long` | `69.75` | 50,540,000.00 USD | 0.00 USD | 214,850.00 USD | `-27.64%` | `3,080.30` |
| `Live` | `Long` | `69.85` | 50,320,000.00 USD | 0.00 USD | 8,470.00 USD | `-27.54%` | `121.19` |
| `Live` | `Long` | `69.95` | 50,310,000.00 USD | 0.00 USD | 8,800.00 USD | `-27.43%` | `125.81` |
| `Live` | `Long` | `70.05` | 50,300,000.00 USD | 0.00 USD | 13,110,000.00 USD | `-27.33%` | `187,140.55` |
| `Live` | `Long` | `70.15` | 37,190,000.00 USD | 0.00 USD | 4,120.00 USD | `-27.23%` | `58.77` |
| `Live` | `Long` | `70.25` | 37,190,000.00 USD | 0.00 USD | 73,790.00 USD | `-27.12%` | `1,050.46` |
| `Live` | `Long` | `70.35` | 37,120,000.00 USD | 0.00 USD | 2,170,000.00 USD | `-27.02%` | `30,814.81` |
| `Live` | `Long` | `70.45` | 34,950,000.00 USD | 0.00 USD | 116,720.00 USD | `-26.92%` | `1,656.76` |
| `Live` | `Long` | `70.65` | 34,830,000.00 USD | 0.00 USD | 45,480.00 USD | `-26.71%` | `643.67` |
| `Live` | `Long` | `70.75` | 34,790,000.00 USD | 0.00 USD | 9,720.00 USD | `-26.60%` | `137.39` |
| `Live` | `Long` | `70.85` | 34,780,000.00 USD | 0.00 USD | 29,230.00 USD | `-26.50%` | `412.53` |
| `Live` | `Long` | `70.95` | 34,750,000.00 USD | 0.00 USD | 4,430.00 USD | `-26.40%` | `62.38` |
| `Live` | `Long` | `71.05` | 34,740,000.00 USD | 0.00 USD | 47,400.00 USD | `-26.29%` | `667.14` |
| `Live` | `Long` | `71.15` | 34,700,000.00 USD | 0.00 USD | 69,870.00 USD | `-26.19%` | `982.07` |
| `Live` | `Long` | `71.25` | 34,630,000.00 USD | 0.00 USD | 6,300.00 USD | `-26.09%` | `88.37` |
| `Live` | `Long` | `71.35` | 34,620,000.00 USD | 0.00 USD | 15,590.00 USD | `-25.98%` | `218.51` |
| `Live` | `Long` | `71.45` | 34,600,000.00 USD | 0.00 USD | 38,820.00 USD | `-25.88%` | `543.37` |
| `Live` | `Long` | `71.55` | 34,570,000.00 USD | 0.00 USD | 43,440.00 USD | `-25.77%` | `607.14` |
| `Live` | `Long` | `71.65` | 34,520,000.00 USD | 0.00 USD | 4,370.00 USD | `-25.67%` | `61.05` |
| `Live` | `Long` | `71.75` | 34,520,000.00 USD | 0.00 USD | 28,720.00 USD | `-25.57%` | `400.33` |
| `Live` | `Long` | `71.85` | 34,490,000.00 USD | 0.00 USD | 2,670.00 USD | `-25.46%` | `37.11` |
| `Live` | `Long` | `71.95` | 34,490,000.00 USD | 0.00 USD | 12,860.00 USD | `-25.36%` | `178.70` |
| `Live` | `Long` | `72.05` | 34,470,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-25.26%` | `15,562.06` |
| `Live` | `Long` | `72.15` | 33,350,000.00 USD | 0.00 USD | 131,520.00 USD | `-25.15%` | `1,822.91` |
| `Live` | `Long` | `72.25` | 33,220,000.00 USD | 0.00 USD | 260,000.00 USD | `-25.05%` | `3,598.60` |
| `Live` | `Long` | `72.35` | 32,960,000.00 USD | 0.00 USD | 1,480,000.00 USD | `-24.94%` | `20,402.20` |
| `Live` | `Long` | `72.45` | 31,480,000.00 USD | 0.00 USD | 5,600.00 USD | `-24.84%` | `77.33` |
| `Live` | `Long` | `72.55` | 31,480,000.00 USD | 0.00 USD | 13,960.00 USD | `-24.74%` | `192.38` |
| `Live` | `Long` | `72.65` | 31,470,000.00 USD | 0.00 USD | 33,720.00 USD | `-24.63%` | `464.15` |
| `Live` | `Long` | `72.75` | 31,430,000.00 USD | 0.00 USD | 3,690.00 USD | `-24.53%` | `50.79` |
| `Live` | `Long` | `72.85` | 31,430,000.00 USD | 0.00 USD | 190,300.00 USD | `-24.43%` | `2,612.27` |
| `Live` | `Long` | `72.95` | 31,240,000.00 USD | 0.00 USD | 5,600.00 USD | `-24.32%` | `76.71` |
| `Live` | `Long` | `73.05` | 31,230,000.00 USD | 0.00 USD | 46,010.00 USD | `-24.22%` | `629.88` |
| `Live` | `Long` | `73.15` | 31,190,000.00 USD | 0.00 USD | 18,520.00 USD | `-24.11%` | `253.14` |
| `Live` | `Long` | `73.25` | 31,170,000.00 USD | 0.00 USD | 26,730.00 USD | `-24.01%` | `364.96` |
| `Live` | `Long` | `73.35` | 31,140,000.00 USD | 0.00 USD | 21,920.00 USD | `-23.91%` | `298.83` |
| `Live` | `Long` | `73.45` | 31,120,000.00 USD | 0.00 USD | 5,350.00 USD | `-23.80%` | `72.82` |
| `Live` | `Long` | `73.55` | 31,110,000.00 USD | 0.00 USD | 14,850.00 USD | `-23.70%` | `201.89` |
| `Live` | `Long` | `73.65` | 31,100,000.00 USD | 0.00 USD | 37,850.00 USD | `-23.60%` | `513.85` |
| `Live` | `Long` | `73.75` | 31,060,000.00 USD | 0.00 USD | 70,280.00 USD | `-23.49%` | `952.95` |
| `Live` | `Long` | `73.85` | 30,990,000.00 USD | 0.00 USD | 12,370.00 USD | `-23.39%` | `167.54` |
| `Live` | `Long` | `73.95` | 30,980,000.00 USD | 0.00 USD | 40,040.00 USD | `-23.28%` | `541.40` |
| `Live` | `Long` | `74.05` | 30,940,000.00 USD | 0.00 USD | 25,190.00 USD | `-23.18%` | `340.24` |
| `Live` | `Long` | `74.15` | 30,910,000.00 USD | 0.00 USD | 21,430.00 USD | `-23.08%` | `289.03` |
| `Live` | `Long` | `74.25` | 30,890,000.00 USD | 0.00 USD | 26,460.00 USD | `-22.97%` | `356.31` |
| `Live` | `Long` | `74.35` | 30,860,000.00 USD | 0.00 USD | 40,040.00 USD | `-22.87%` | `538.50` |
| `Live` | `Long` | `74.45` | 30,820,000.00 USD | 0.00 USD | 22,440.00 USD | `-22.77%` | `301.36` |
| `Live` | `Long` | `74.55` | 30,800,000.00 USD | 0.00 USD | 15,670.00 USD | `-22.66%` | `210.23` |
| `Live` | `Long` | `74.65` | 30,790,000.00 USD | 0.00 USD | 1,030.00 USD | `-22.56%` | `13.82` |
| `Live` | `Long` | `74.75` | 30,790,000.00 USD | 0.00 USD | 123,840.00 USD | `-22.45%` | `1,656.66` |
| `Live` | `Long` | `74.85` | 30,660,000.00 USD | 0.00 USD | 127,450.00 USD | `-22.35%` | `1,702.70` |
| `Live` | `Long` | `74.95` | 30,530,000.00 USD | 0.00 USD | 18,090.00 USD | `-22.25%` | `241.37` |
| `Live` | `Long` | `75.05` | 30,520,000.00 USD | 0.00 USD | 40,670.00 USD | `-22.14%` | `541.85` |
| `Live` | `Long` | `75.25` | 30,480,000.00 USD | 0.00 USD | 287,360.00 USD | `-21.94%` | `3,818.68` |
| `Live` | `Long` | `75.35` | 30,190,000.00 USD | 0.00 USD | 18,360.00 USD | `-21.83%` | `243.67` |
| `Live` | `Long` | `75.45` | 30,170,000.00 USD | 0.00 USD | 38,660.00 USD | `-21.73%` | `512.34` |
| `Live` | `Long` | `75.55` | 30,130,000.00 USD | 0.00 USD | 35,050.00 USD | `-21.62%` | `463.97` |
| `Live` | `Long` | `75.65` | 30,100,000.00 USD | 0.00 USD | 130,250.00 USD | `-21.52%` | `1,721.70` |
| `Live` | `Long` | `75.75` | 29,970,000.00 USD | 0.00 USD | 60,640.00 USD | `-21.42%` | `800.51` |
| `Live` | `Long` | `75.85` | 29,910,000.00 USD | 0.00 USD | 2,880.00 USD | `-21.31%` | `37.95` |
| `Live` | `Long` | `75.95` | 29,900,000.00 USD | 0.00 USD | 29,830.00 USD | `-21.21%` | `392.72` |
| `Live` | `Long` | `76.15` | 29,870,000.00 USD | 0.00 USD | 4,370.00 USD | `-21.00%` | `57.43` |
| `Live` | `Long` | `76.25` | 29,870,000.00 USD | 0.00 USD | 4,340.00 USD | `-20.90%` | `56.96` |
| `Live` | `Long` | `76.35` | 29,860,000.00 USD | 0.00 USD | 45,780.00 USD | `-20.79%` | `599.62` |
| `Live` | `Long` | `76.45` | 29,820,000.00 USD | 0.00 USD | 1,720,000.00 USD | `-20.69%` | `22,507.44` |
| `Live` | `Long` | `76.55` | 28,100,000.00 USD | 0.00 USD | 37,610.00 USD | `-20.59%` | `491.36` |
| `Live` | `Long` | `76.65` | 28,060,000.00 USD | 0.00 USD | 55,910.00 USD | `-20.48%` | `729.36` |
| `Live` | `Long` | `76.75` | 28,000,000.00 USD | 0.00 USD | 5,060.00 USD | `-20.38%` | `65.89` |
| `Live` | `Long` | `76.85` | 28,000,000.00 USD | 0.00 USD | 135,520.00 USD | `-20.28%` | `1,763.49` |
| `Live` | `Long` | `76.95` | 27,860,000.00 USD | 0.00 USD | 33,790.00 USD | `-20.17%` | `439.09` |
| `Live` | `Long` | `77.05` | 27,830,000.00 USD | 0.00 USD | 80,420.00 USD | `-20.07%` | `1,043.70` |
| `Live` | `Long` | `77.15` | 27,750,000.00 USD | 0.00 USD | 1,740,000.00 USD | `-19.96%` | `22,565.63` |
| `Live` | `Long` | `77.25` | 26,010,000.00 USD | 0.00 USD | 25,180.00 USD | `-19.86%` | `325.91` |
| `Live` | `Long` | `77.35` | 25,980,000.00 USD | 0.00 USD | 5,650.00 USD | `-19.76%` | `73.07` |
| `Live` | `Long` | `77.45` | 25,980,000.00 USD | 0.00 USD | 59,150.00 USD | `-19.65%` | `763.68` |
| `Live` | `Long` | `77.55` | 25,920,000.00 USD | 0.00 USD | 18,400.00 USD | `-19.55%` | `237.26` |
| `Live` | `Long` | `77.65` | 25,900,000.00 USD | 0.00 USD | 3,590.00 USD | `-19.45%` | `46.26` |
| `Live` | `Long` | `77.75` | 25,900,000.00 USD | 0.00 USD | 9,870.00 USD | `-19.34%` | `126.99` |
| `Live` | `Long` | `77.85` | 25,890,000.00 USD | 0.00 USD | 83,670.00 USD | `-19.24%` | `1,074.71` |
| `Live` | `Long` | `77.95` | 25,800,000.00 USD | 0.00 USD | 15,390.00 USD | `-19.13%` | `197.48` |
| `Live` | `Long` | `78.05` | 25,790,000.00 USD | 0.00 USD | 21,520.00 USD | `-19.03%` | `275.71` |
| `Live` | `Long` | `78.15` | 25,770,000.00 USD | 0.00 USD | 63,710.00 USD | `-18.93%` | `815.26` |
| `Live` | `Long` | `78.25` | 25,700,000.00 USD | 0.00 USD | 70,740.00 USD | `-18.82%` | `904.08` |
| `Live` | `Long` | `78.35` | 25,630,000.00 USD | 0.00 USD | 55,060.00 USD | `-18.72%` | `702.76` |
| `Live` | `Long` | `78.45` | 25,580,000.00 USD | 0.00 USD | 26,080.00 USD | `-18.62%` | `332.40` |
| `Live` | `Long` | `78.55` | 25,550,000.00 USD | 0.00 USD | 5,740.00 USD | `-18.51%` | `73.09` |
| `Live` | `Long` | `78.65` | 25,540,000.00 USD | 0.00 USD | 32,860.00 USD | `-18.41%` | `417.75` |
| `Live` | `Long` | `78.75` | 25,510,000.00 USD | 0.00 USD | 52,670.00 USD | `-18.30%` | `668.88` |
| `Live` | `Long` | `78.85` | 25,460,000.00 USD | 0.00 USD | 62,050.00 USD | `-18.20%` | `786.91` |
| `Live` | `Long` | `78.95` | 25,400,000.00 USD | 0.00 USD | 1,370.00 USD | `-18.10%` | `17.33` |
| `Live` | `Long` | `79.05` | 25,400,000.00 USD | 0.00 USD | 6,490.00 USD | `-17.99%` | `82.14` |
| `Live` | `Long` | `79.15` | 25,390,000.00 USD | 0.00 USD | 128,420.00 USD | `-17.89%` | `1,622.43` |
| `Live` | `Long` | `79.25` | 25,260,000.00 USD | 0.00 USD | 47,570.00 USD | `-17.79%` | `600.23` |
| `Live` | `Long` | `79.35` | 25,210,000.00 USD | 0.00 USD | 17,490.00 USD | `-17.68%` | `220.45` |
| `Live` | `Long` | `79.45` | 25,200,000.00 USD | 0.00 USD | 7,750.00 USD | `-17.58%` | `97.50` |
| `Live` | `Long` | `79.55` | 25,190,000.00 USD | 0.00 USD | 6,720.00 USD | `-17.47%` | `84.52` |
| `Live` | `Long` | `79.65` | 25,180,000.00 USD | 0.00 USD | 45,420.00 USD | `-17.37%` | `570.30` |
| `Live` | `Long` | `79.75` | 25,140,000.00 USD | 0.00 USD | 194,630.00 USD | `-17.27%` | `2,440.53` |
| `Live` | `Long` | `79.85` | 24,940,000.00 USD | 0.00 USD | 30,690.00 USD | `-17.16%` | `384.36` |
| `Live` | `Long` | `79.95` | 24,910,000.00 USD | 0.00 USD | 34,220.00 USD | `-17.06%` | `428.08` |
| `Live` | `Long` | `80.05` | 24,880,000.00 USD | 0.00 USD | 40,880.00 USD | `-16.96%` | `510.63` |
| `Live` | `Long` | `80.15` | 24,840,000.00 USD | 0.00 USD | 34,810.00 USD | `-16.85%` | `434.26` |
| `Live` | `Long` | `80.25` | 24,800,000.00 USD | 0.00 USD | 79,220.00 USD | `-16.75%` | `987.16` |
| `Live` | `Long` | `80.35` | 24,720,000.00 USD | 0.00 USD | 107,240.00 USD | `-16.65%` | `1,334.64` |
| `Live` | `Long` | `80.45` | 24,610,000.00 USD | 0.00 USD | 11,550.00 USD | `-16.54%` | `143.59` |
| `Live` | `Long` | `80.55` | 24,600,000.00 USD | 0.00 USD | 16,640.00 USD | `-16.44%` | `206.58` |
| `Live` | `Long` | `80.65` | 24,590,000.00 USD | 0.00 USD | 103,370.00 USD | `-16.33%` | `1,281.68` |
| `Live` | `Long` | `80.75` | 24,480,000.00 USD | 0.00 USD | 52,190.00 USD | `-16.23%` | `646.30` |
| `Live` | `Long` | `80.85` | 24,430,000.00 USD | 0.00 USD | 439,180.00 USD | `-16.13%` | `5,432.01` |
| `Live` | `Long` | `80.95` | 23,990,000.00 USD | 0.00 USD | 25,480.00 USD | `-16.02%` | `314.80` |
| `Live` | `Long` | `81.05` | 23,970,000.00 USD | 0.00 USD | 2,230,000.00 USD | `-15.92%` | `27,457.97` |
| `Live` | `Long` | `81.15` | 21,740,000.00 USD | 0.00 USD | 89,300.00 USD | `-15.82%` | `1,100.39` |
| `Live` | `Long` | `81.25` | 21,650,000.00 USD | 0.00 USD | 22,790.00 USD | `-15.71%` | `280.49` |
| `Live` | `Long` | `81.35` | 21,630,000.00 USD | 0.00 USD | 50,550.00 USD | `-15.61%` | `621.37` |
| `Live` | `Long` | `81.45` | 21,580,000.00 USD | 0.00 USD | 68,010.00 USD | `-15.50%` | `834.94` |
| `Live` | `Long` | `81.55` | 21,510,000.00 USD | 0.00 USD | 190,680.00 USD | `-15.40%` | `2,338.18` |
| `Live` | `Long` | `81.65` | 21,320,000.00 USD | 0.00 USD | 20,720.00 USD | `-15.30%` | `253.76` |
| `Live` | `Long` | `81.75` | 21,300,000.00 USD | 0.00 USD | 18,650.00 USD | `-15.19%` | `228.11` |
| `Live` | `Long` | `81.85` | 21,280,000.00 USD | 0.00 USD | 35,560.00 USD | `-15.09%` | `434.40` |
| `Live` | `Long` | `81.95` | 21,240,000.00 USD | 0.00 USD | 153,360.00 USD | `-14.99%` | `1,871.43` |
| `Live` | `Long` | `82.05` | 21,090,000.00 USD | 0.00 USD | 123,570.00 USD | `-14.88%` | `1,506.01` |
| `Live` | `Long` | `82.15` | 20,970,000.00 USD | 0.00 USD | 804,530.00 USD | `-14.78%` | `9,793.43` |
| `Live` | `Long` | `82.25` | 20,160,000.00 USD | 0.00 USD | 43,580.00 USD | `-14.67%` | `529.88` |
| `Live` | `Long` | `82.35` | 20,120,000.00 USD | 0.00 USD | 158,370.00 USD | `-14.57%` | `1,923.09` |
| `Live` | `Long` | `82.45` | 19,960,000.00 USD | 0.00 USD | 218,740.00 USD | `-14.47%` | `2,652.97` |
| `Live` | `Long` | `82.55` | 19,740,000.00 USD | 0.00 USD | 18,190.00 USD | `-14.36%` | `220.40` |
| `Live` | `Long` | `82.65` | 19,720,000.00 USD | 0.00 USD | 184,500.00 USD | `-14.26%` | `2,232.25` |
| `Live` | `Long` | `82.75` | 19,540,000.00 USD | 0.00 USD | 7,950.00 USD | `-14.16%` | `96.13` |
| `Live` | `Long` | `82.85` | 19,530,000.00 USD | 0.00 USD | 58,610.00 USD | `-14.05%` | `707.39` |
| `Live` | `Long` | `82.95` | 19,470,000.00 USD | 0.00 USD | 23,300.00 USD | `-13.95%` | `280.94` |
| `Live` | `Long` | `83.05` | 19,450,000.00 USD | 0.00 USD | 107,130.00 USD | `-13.84%` | `1,289.96` |
| `Live` | `Long` | `83.15` | 19,340,000.00 USD | 0.00 USD | 44,400.00 USD | `-13.74%` | `534.02` |
| `Live` | `Long` | `83.25` | 19,300,000.00 USD | 0.00 USD | 160,260.00 USD | `-13.64%` | `1,925.04` |
| `Live` | `Long` | `83.35` | 19,140,000.00 USD | 0.00 USD | 274,420.00 USD | `-13.53%` | `3,292.33` |
| `Live` | `Long` | `83.45` | 18,860,000.00 USD | 0.00 USD | 54,190.00 USD | `-13.43%` | `649.42` |
| `Live` | `Long` | `83.55` | 18,810,000.00 USD | 0.00 USD | 20,900.00 USD | `-13.33%` | `250.12` |
| `Live` | `Long` | `83.65` | 18,790,000.00 USD | 0.00 USD | 130,030.00 USD | `-13.22%` | `1,554.46` |
| `Live` | `Long` | `83.75` | 18,660,000.00 USD | 0.00 USD | 81,510.00 USD | `-13.12%` | `973.24` |
| `Live` | `Long` | `83.85` | 18,580,000.00 USD | 0.00 USD | 11,040.00 USD | `-13.01%` | `131.62` |
| `Live` | `Long` | `83.95` | 18,570,000.00 USD | 0.00 USD | 98,980.00 USD | `-12.91%` | `1,178.98` |
| `Live` | `Long` | `84.05` | 18,470,000.00 USD | 0.00 USD | 113,380.00 USD | `-12.81%` | `1,348.96` |
| `Live` | `Long` | `84.15` | 18,350,000.00 USD | 0.00 USD | 66,390.00 USD | `-12.70%` | `788.98` |
| `Live` | `Long` | `84.25` | 18,290,000.00 USD | 0.00 USD | 49,770.00 USD | `-12.60%` | `590.78` |
| `Live` | `Long` | `84.35` | 18,240,000.00 USD | 0.00 USD | 397,070.00 USD | `-12.50%` | `4,707.45` |
| `Live` | `Long` | `84.45` | 17,840,000.00 USD | 0.00 USD | 85,770.00 USD | `-12.39%` | `1,015.66` |
| `Live` | `Long` | `84.55` | 17,750,000.00 USD | 0.00 USD | 5,900.00 USD | `-12.29%` | `69.79` |
| `Live` | `Long` | `84.65` | 17,750,000.00 USD | 0.00 USD | 1,330,000.00 USD | `-12.18%` | `15,710.69` |
| `Live` | `Long` | `84.75` | 16,420,000.00 USD | 0.00 USD | 1,040,000.00 USD | `-12.08%` | `12,268.62` |
| `Live` | `Long` | `84.85` | 15,380,000.00 USD | 0.00 USD | 95,670.00 USD | `-11.98%` | `1,127.48` |
| `Live` | `Long` | `84.95` | 15,280,000.00 USD | 0.00 USD | 162,040.00 USD | `-11.87%` | `1,907.46` |
| `Live` | `Long` | `85.05` | 15,120,000.00 USD | 0.00 USD | 15,920.00 USD | `-11.77%` | `187.17` |
| `Live` | `Long` | `85.15` | 15,100,000.00 USD | 0.00 USD | 7,430.00 USD | `-11.67%` | `87.29` |
| `Live` | `Long` | `85.25` | 15,100,000.00 USD | 0.00 USD | 618,490.00 USD | `-11.56%` | `7,255.05` |
| `Live` | `Long` | `85.35` | 14,480,000.00 USD | 0.00 USD | 20,970.00 USD | `-11.46%` | `245.72` |
| `Live` | `Long` | `85.45` | 14,460,000.00 USD | 0.00 USD | 66,690.00 USD | `-11.35%` | `780.41` |
| `Live` | `Long` | `85.55` | 14,390,000.00 USD | 0.00 USD | 11,200.00 USD | `-11.25%` | `130.93` |
| `Live` | `Long` | `85.65` | 14,380,000.00 USD | 0.00 USD | 43,620.00 USD | `-11.15%` | `509.33` |
| `Live` | `Long` | `85.75` | 14,340,000.00 USD | 0.00 USD | 9,640.00 USD | `-11.04%` | `112.40` |
| `Live` | `Long` | `85.85` | 14,330,000.00 USD | 0.00 USD | 73,630.00 USD | `-10.94%` | `857.62` |
| `Live` | `Long` | `85.95` | 14,250,000.00 USD | 0.00 USD | 360,250.00 USD | `-10.84%` | `4,191.38` |
| `Live` | `Long` | `86.05` | 13,890,000.00 USD | 0.00 USD | 138,200.00 USD | `-10.73%` | `1,606.03` |
| `Live` | `Long` | `86.15` | 13,750,000.00 USD | 0.00 USD | 51,580.00 USD | `-10.63%` | `598.73` |
| `Live` | `Long` | `86.25` | 13,700,000.00 USD | 0.00 USD | 52,570.00 USD | `-10.52%` | `609.53` |
| `Live` | `Long` | `86.35` | 13,650,000.00 USD | 0.00 USD | 3,860.00 USD | `-10.42%` | `44.73` |
| `Live` | `Long` | `86.45` | 13,650,000.00 USD | 0.00 USD | 188,400.00 USD | `-10.32%` | `2,179.28` |
| `Live` | `Long` | `86.55` | 13,460,000.00 USD | 0.00 USD | 30,640.00 USD | `-10.21%` | `353.96` |
| `Live` | `Long` | `86.65` | 13,430,000.00 USD | 0.00 USD | 190,730.00 USD | `-10.11%` | `2,201.12` |
| `Live` | `Long` | `86.75` | 13,240,000.00 USD | 0.00 USD | 35,070.00 USD | `-10.01%` | `404.31` |
| `Live` | `Long` | `86.85` | 13,200,000.00 USD | 0.00 USD | 75,910.00 USD | `-9.90%` | `874.00` |
| `Live` | `Long` | `86.95` | 13,130,000.00 USD | 0.00 USD | 152,510.00 USD | `-9.80%` | `1,754.01` |
| `Live` | `Long` | `87.05` | 12,970,000.00 USD | 0.00 USD | 30,500.00 USD | `-9.69%` | `350.43` |
| `Live` | `Long` | `87.15` | 12,940,000.00 USD | 0.00 USD | 20,150.00 USD | `-9.59%` | `231.21` |
| `Live` | `Long` | `87.25` | 12,920,000.00 USD | 0.00 USD | 93,120.00 USD | `-9.49%` | `1,067.25` |
| `Live` | `Long` | `87.35` | 12,830,000.00 USD | 0.00 USD | 72,050.00 USD | `-9.38%` | `824.89` |
| `Live` | `Long` | `87.45` | 12,760,000.00 USD | 0.00 USD | 151,520.00 USD | `-9.28%` | `1,732.68` |
| `Live` | `Long` | `87.55` | 12,610,000.00 USD | 0.00 USD | 128,170.00 USD | `-9.18%` | `1,463.96` |
| `Live` | `Long` | `87.65` | 12,480,000.00 USD | 0.00 USD | 105,970.00 USD | `-9.07%` | `1,208.96` |
| `Live` | `Long` | `87.75` | 12,370,000.00 USD | 0.00 USD | 30,700.00 USD | `-8.97%` | `349.86` |
| `Live` | `Long` | `87.85` | 12,340,000.00 USD | 0.00 USD | 66,830.00 USD | `-8.86%` | `760.69` |
| `Live` | `Long` | `87.95` | 12,270,000.00 USD | 0.00 USD | 162,530.00 USD | `-8.76%` | `1,847.96` |
| `Live` | `Long` | `88.05` | 12,110,000.00 USD | 0.00 USD | 62,640.00 USD | `-8.66%` | `711.44` |
| `Live` | `Long` | `88.15` | 12,050,000.00 USD | 0.00 USD | 21,240.00 USD | `-8.55%` | `240.98` |
| `Live` | `Long` | `88.25` | 12,030,000.00 USD | 0.00 USD | 74,760.00 USD | `-8.45%` | `847.09` |
| `Live` | `Long` | `88.35` | 11,950,000.00 USD | 0.00 USD | 26,970.00 USD | `-8.35%` | `305.29` |
| `Live` | `Long` | `88.45` | 11,930,000.00 USD | 0.00 USD | 129,160.00 USD | `-8.24%` | `1,460.28` |
| `Live` | `Long` | `88.55` | 11,800,000.00 USD | 0.00 USD | 251,040.00 USD | `-8.14%` | `2,834.96` |
| `Live` | `Long` | `88.65` | 11,550,000.00 USD | 0.00 USD | 96,310.00 USD | `-8.03%` | `1,086.46` |
| `Live` | `Long` | `88.75` | 11,450,000.00 USD | 0.00 USD | 168,880.00 USD | `-7.93%` | `1,902.89` |
| `Live` | `Long` | `88.85` | 11,280,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-7.83%` | `11,930.59` |
| `Live` | `Long` | `88.95` | 10,220,000.00 USD | 0.00 USD | 36,710.00 USD | `-7.72%` | `412.71` |
| `Live` | `Long` | `89.05` | 10,180,000.00 USD | 0.00 USD | 40,570.00 USD | `-7.62%` | `455.59` |
| `Live` | `Long` | `89.15` | 10,140,000.00 USD | 0.00 USD | 160,460.00 USD | `-7.52%` | `1,799.88` |
| `Live` | `Long` | `89.25` | 9,980,000.00 USD | 0.00 USD | 31,740.00 USD | `-7.41%` | `355.61` |
| `Live` | `Long` | `89.35` | 9,950,000.00 USD | 0.00 USD | 42,390.00 USD | `-7.31%` | `474.42` |
| `Live` | `Long` | `89.45` | 9,910,000.00 USD | 0.00 USD | 511,650.00 USD | `-7.20%` | `5,719.99` |
| `Live` | `Long` | `89.55` | 9,400,000.00 USD | 0.00 USD | 64,040.00 USD | `-7.10%` | `715.09` |
| `Live` | `Long` | `89.65` | 9,330,000.00 USD | 0.00 USD | 22,300.00 USD | `-7.00%` | `248.69` |
| `Live` | `Long` | `89.75` | 9,310,000.00 USD | 0.00 USD | 134,870.00 USD | `-6.89%` | `1,502.76` |
| `Live` | `Long` | `89.85` | 9,180,000.00 USD | 0.00 USD | 56,560.00 USD | `-6.79%` | `629.54` |
| `Live` | `Long` | `89.95` | 9,120,000.00 USD | 0.00 USD | 77,970.00 USD | `-6.69%` | `866.84` |
| `Live` | `Long` | `90.05` | 9,040,000.00 USD | 0.00 USD | 38,720.00 USD | `-6.58%` | `430.03` |
| `Live` | `Long` | `90.15` | 9,000,000.00 USD | 0.00 USD | 77,700.00 USD | `-6.48%` | `861.87` |
| `Live` | `Long` | `90.25` | 8,920,000.00 USD | 0.00 USD | 44,640.00 USD | `-6.37%` | `494.61` |
| `Live` | `Long` | `90.35` | 8,880,000.00 USD | 0.00 USD | 77,210.00 USD | `-6.27%` | `854.62` |
| `Live` | `Long` | `90.45` | 8,800,000.00 USD | 0.00 USD | 41,960.00 USD | `-6.17%` | `463.95` |
| `Live` | `Long` | `90.55` | 8,760,000.00 USD | 0.00 USD | 85,260.00 USD | `-6.06%` | `941.55` |
| `Live` | `Long` | `90.65` | 8,680,000.00 USD | 0.00 USD | 116,340.00 USD | `-5.96%` | `1,283.37` |
| `Live` | `Long` | `90.75` | 8,560,000.00 USD | 0.00 USD | 84,390.00 USD | `-5.86%` | `929.89` |
| `Live` | `Long` | `90.85` | 8,480,000.00 USD | 0.00 USD | 74,130.00 USD | `-5.75%` | `815.96` |
| `Live` | `Long` | `90.95` | 8,400,000.00 USD | 0.00 USD | 39,770.00 USD | `-5.65%` | `437.23` |
| `Live` | `Long` | `91.05` | 8,360,000.00 USD | 0.00 USD | 413,880.00 USD | `-5.54%` | `4,545.58` |
| `Live` | `Long` | `91.15` | 7,950,000.00 USD | 0.00 USD | 282,790.00 USD | `-5.44%` | `3,102.48` |
| `Live` | `Long` | `91.25` | 7,660,000.00 USD | 0.00 USD | 44,170.00 USD | `-5.34%` | `484.10` |
| `Live` | `Long` | `91.35` | 7,620,000.00 USD | 0.00 USD | 14,960.00 USD | `-5.23%` | `163.74` |
| `Live` | `Long` | `91.45` | 7,610,000.00 USD | 0.00 USD | 347,480.00 USD | `-5.13%` | `3,799.62` |
| `Live` | `Long` | `91.55` | 7,260,000.00 USD | 0.00 USD | 1,210,000.00 USD | `-5.03%` | `13,204.29` |
| `Live` | `Long` | `91.65` | 6,050,000.00 USD | 0.00 USD | 1,430,000.00 USD | `-4.92%` | `15,594.68` |
| `Live` | `Long` | `91.75` | 4,620,000.00 USD | 0.00 USD | 237,560.00 USD | `-4.82%` | `2,589.24` |
| `Live` | `Long` | `91.85` | 4,380,000.00 USD | 0.00 USD | 71,640.00 USD | `-4.71%` | `779.93` |
| `Live` | `Long` | `91.95` | 4,310,000.00 USD | 0.00 USD | 35,980.00 USD | `-4.61%` | `391.35` |
| `Live` | `Long` | `92.05` | 4,270,000.00 USD | 0.00 USD | 168,710.00 USD | `-4.51%` | `1,832.79` |
| `Live` | `Long` | `92.15` | 4,110,000.00 USD | 0.00 USD | 328,990.00 USD | `-4.40%` | `3,570.11` |
| `Live` | `Long` | `92.25` | 3,780,000.00 USD | 0.00 USD | 168,960.00 USD | `-4.30%` | `1,831.52` |
| `Live` | `Long` | `92.35` | 3,610,000.00 USD | 0.00 USD | 369,030.00 USD | `-4.20%` | `3,995.96` |
| `Live` | `Long` | `92.45` | 3,240,000.00 USD | 0.00 USD | 117,820.00 USD | `-4.09%` | `1,274.42` |
| `Live` | `Long` | `92.55` | 3,120,000.00 USD | 0.00 USD | 5,040.00 USD | `-3.99%` | `54.41` |
| `Live` | `Long` | `92.65` | 3,120,000.00 USD | 0.00 USD | 15,170.00 USD | `-3.89%` | `163.78` |
| `Live` | `Long` | `92.75` | 3,100,000.00 USD | 0.00 USD | 2,060.00 USD | `-3.78%` | `22.19` |
| `Live` | `Long` | `92.85` | 3,100,000.00 USD | 0.00 USD | 23,420.00 USD | `-3.68%` | `252.19` |
| `Live` | `Long` | `92.95` | 3,080,000.00 USD | 0.00 USD | 5,840.00 USD | `-3.57%` | `62.86` |
| `Live` | `Long` | `93.05` | 3,070,000.00 USD | 0.00 USD | 31,450.00 USD | `-3.47%` | `338.04` |
| `Live` | `Long` | `93.15` | 3,040,000.00 USD | 0.00 USD | 4,940.00 USD | `-3.37%` | `53.02` |
| `Live` | `Long` | `93.25` | 3,030,000.00 USD | 0.00 USD | 63,970.00 USD | `-3.26%` | `686.00` |
| `Live` | `Long` | `93.35` | 2,970,000.00 USD | 0.00 USD | 11,060.00 USD | `-3.16%` | `118.46` |
| `Live` | `Long` | `93.45` | 2,960,000.00 USD | 0.00 USD | 8,060.00 USD | `-3.06%` | `86.26` |
| `Live` | `Long` | `93.55` | 2,950,000.00 USD | 0.00 USD | 19,360.00 USD | `-2.95%` | `206.98` |
| `Live` | `Long` | `93.65` | 2,930,000.00 USD | 0.00 USD | 939,260.00 USD | `-2.85%` | `10,029.52` |
| `Live` | `Long` | `93.75` | 1,990,000.00 USD | 0.00 USD | 10,870.00 USD | `-2.74%` | `115.91` |
| `Live` | `Long` | `93.85` | 1,980,000.00 USD | 0.00 USD | 11,870.00 USD | `-2.64%` | `126.50` |
| `Live` | `Long` | `93.95` | 1,970,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-2.54%` | `12,126.47` |
| `Live` | `Long` | `94.05` | 829,440.00 USD | 0.00 USD | 4,190.00 USD | `-2.43%` | `44.53` |
| `Live` | `Long` | `94.15` | 825,260.00 USD | 0.00 USD | 29,210.00 USD | `-2.33%` | `310.26` |
| `Live` | `Long` | `94.25` | 796,050.00 USD | 0.00 USD | 8,860.00 USD | `-2.23%` | `93.98` |
| `Live` | `Long` | `94.35` | 787,190.00 USD | 0.00 USD | 7,960.00 USD | `-2.12%` | `84.41` |
| `Live` | `Long` | `94.45` | 779,220.00 USD | 0.00 USD | 155,730.00 USD | `-2.02%` | `1,648.85` |
| `Live` | `Long` | `94.55` | 623,490.00 USD | 0.00 USD | 80,330.00 USD | `-1.91%` | `849.62` |
| `Live` | `Long` | `94.65` | 543,160.00 USD | 0.00 USD | 25,780.00 USD | `-1.81%` | `272.42` |
| `Live` | `Long` | `94.75` | 517,370.00 USD | 0.00 USD | 82,080.00 USD | `-1.71%` | `866.31` |
| `Live` | `Long` | `94.85` | 435,290.00 USD | 0.00 USD | 33,620.00 USD | `-1.60%` | `354.43` |
| `Live` | `Long` | `94.95` | 401,670.00 USD | 0.00 USD | 33,760.00 USD | `-1.50%` | `355.56` |
| `Live` | `Long` | `95.05` | 367,910.00 USD | 0.00 USD | 57,160.00 USD | `-1.40%` | `601.41` |
| `Live` | `Long` | `95.15` | 310,750.00 USD | 0.00 USD | 20,130.00 USD | `-1.29%` | `211.59` |
| `Live` | `Long` | `95.25` | 290,620.00 USD | 0.00 USD | 42,330.00 USD | `-1.19%` | `444.46` |
| `Live` | `Long` | `95.35` | 248,280.00 USD | 0.00 USD | 7,350.00 USD | `-1.08%` | `77.08` |
| `Live` | `Long` | `95.45` | 240,930.00 USD | 0.00 USD | 23,550.00 USD | `-0.98%` | `246.70` |
| `Live` | `Long` | `95.55` | 217,380.00 USD | 0.00 USD | 44,090.00 USD | `-0.88%` | `461.42` |
| `Live` | `Long` | `95.65` | 173,300.00 USD | 0.00 USD | 92,490.00 USD | `-0.77%` | `966.99` |
| `Live` | `Long` | `95.75` | 80,800.00 USD | 0.00 USD | 49,860.00 USD | `-0.67%` | `520.70` |
| `Live` | `Long` | `95.85` | 30,950.00 USD | 0.00 USD | 30,710.00 USD | `-0.57%` | `320.44` |
| `Live` | `Long` | `95.95` | 231.24 USD | 0.00 USD | 231.24 USD | `-0.46%` | `2.41` |
| `Live` | `Short` | `96.75` | 12,160.00 USD | 12,160.00 USD | 0.00 USD | `+0.37%` | `125.72` |
| `Live` | `Short` | `98.55` | 18,090.00 USD | 5,930.00 USD | 0.00 USD | `+2.24%` | `60.17` |
| `Live` | `Short` | `98.85` | 21,390.00 USD | 3,300.00 USD | 0.00 USD | `+2.55%` | `33.40` |
| `Live` | `Short` | `98.95` | 22,410.00 USD | 1,020.00 USD | 0.00 USD | `+2.65%` | `10.28` |
| `Live` | `Short` | `99.05` | 62,210.00 USD | 39,790.00 USD | 0.00 USD | `+2.75%` | `401.76` |
| `Live` | `Short` | `99.15` | 1,210,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+2.86%` | `11,548.97` |
| `Live` | `Short` | `99.25` | 1,230,000.00 USD | 20,260.00 USD | 0.00 USD | `+2.96%` | `204.12` |
| `Live` | `Short` | `99.35` | 1,320,000.00 USD | 96,300.00 USD | 0.00 USD | `+3.07%` | `969.32` |
| `Live` | `Short` | `99.45` | 1,350,000.00 USD | 24,220.00 USD | 0.00 USD | `+3.17%` | `243.54` |
| `Live` | `Short` | `99.55` | 1,360,000.00 USD | 14,200.00 USD | 0.00 USD | `+3.27%` | `142.63` |
| `Live` | `Short` | `99.65` | 1,380,000.00 USD | 15,630.00 USD | 0.00 USD | `+3.38%` | `156.84` |
| `Live` | `Short` | `99.75` | 1,400,000.00 USD | 26,990.00 USD | 0.00 USD | `+3.48%` | `270.61` |
| `Live` | `Short` | `99.85` | 1,410,000.00 USD | 410.38 USD | 0.00 USD | `+3.58%` | `4.11` |
| `Live` | `Short` | `99.95` | 1,410,000.00 USD | 4,010.00 USD | 0.00 USD | `+3.69%` | `40.15` |
| `Live` | `Short` | `100.05` | 1,450,000.00 USD | 36,990.00 USD | 0.00 USD | `+3.79%` | `369.67` |
| `Live` | `Short` | `100.15` | 1,470,000.00 USD | 25,710.00 USD | 0.00 USD | `+3.90%` | `256.74` |
| `Live` | `Short` | `100.25` | 1,820,000.00 USD | 347,460.00 USD | 0.00 USD | `+4.00%` | `3,465.93` |
| `Live` | `Short` | `100.35` | 2,210,000.00 USD | 391,910.00 USD | 0.00 USD | `+4.10%` | `3,905.45` |
| `Live` | `Short` | `100.45` | 2,220,000.00 USD | 6,010.00 USD | 0.00 USD | `+4.21%` | `59.81` |
| `Live` | `Short` | `100.55` | 2,220,000.00 USD | 1,510.00 USD | 0.00 USD | `+4.31%` | `15.00` |
| `Live` | `Short` | `100.65` | 2,320,000.00 USD | 101,930.00 USD | 0.00 USD | `+4.41%` | `1,012.76` |
| `Live` | `Short` | `100.75` | 2,340,000.00 USD | 20,210.00 USD | 0.00 USD | `+4.52%` | `200.63` |
| `Live` | `Short` | `100.85` | 2,400,000.00 USD | 62,360.00 USD | 0.00 USD | `+4.62%` | `618.31` |
| `Live` | `Short` | `100.95` | 2,420,000.00 USD | 18,180.00 USD | 0.00 USD | `+4.73%` | `180.12` |
| `Live` | `Short` | `101.05` | 2,430,000.00 USD | 8,240.00 USD | 0.00 USD | `+4.83%` | `81.52` |
| `Live` | `Short` | `101.15` | 2,440,000.00 USD | 14,160.00 USD | 0.00 USD | `+4.93%` | `140.03` |
| `Live` | `Short` | `101.25` | 2,440,000.00 USD | 769.50 USD | 0.00 USD | `+5.04%` | `7.60` |
| `Live` | `Short` | `101.35` | 2,450,000.00 USD | 922.29 USD | 0.00 USD | `+5.14%` | `9.10` |
| `Live` | `Short` | `101.45` | 2,450,000.00 USD | 118.70 USD | 0.00 USD | `+5.24%` | `1.17` |
| `Live` | `Short` | `101.55` | 2,450,000.00 USD | 2,790.00 USD | 0.00 USD | `+5.35%` | `27.47` |
| `Live` | `Short` | `101.65` | 2,450,000.00 USD | 2,640.00 USD | 0.00 USD | `+5.45%` | `26.02` |
| `Live` | `Short` | `101.95` | 2,450,000.00 USD | 1,560.00 USD | 0.00 USD | `+5.76%` | `15.31` |
| `Live` | `Short` | `102.05` | 2,460,000.00 USD | 4,280.00 USD | 0.00 USD | `+5.87%` | `41.98` |
| `Live` | `Short` | `102.25` | 2,460,000.00 USD | 1,890.00 USD | 0.00 USD | `+6.07%` | `18.48` |
| `Live` | `Short` | `102.65` | 2,460,000.00 USD | 1,070.00 USD | 0.00 USD | `+6.49%` | `10.45` |
| `Live` | `Short` | `102.75` | 2,460,000.00 USD | 3,340.00 USD | 0.00 USD | `+6.59%` | `32.53` |
| `Live` | `Short` | `102.85` | 2,460,000.00 USD | 654.13 USD | 0.00 USD | `+6.70%` | `6.36` |
| `Live` | `Short` | `102.95` | 2,470,000.00 USD | 4,150.00 USD | 0.00 USD | `+6.80%` | `40.32` |
| `Live` | `Short` | `103.05` | 2,470,000.00 USD | 1,060.00 USD | 0.00 USD | `+6.90%` | `10.24` |
| `Live` | `Short` | `103.15` | 2,480,000.00 USD | 14,800.00 USD | 0.00 USD | `+7.01%` | `143.46` |
| `Live` | `Short` | `103.25` | 2,480,000.00 USD | 206.50 USD | 0.00 USD | `+7.11%` | `2.00` |
| `Live` | `Short` | `103.35` | 2,480,000.00 USD | 385.50 USD | 0.00 USD | `+7.22%` | `3.73` |
| `Live` | `Short` | `103.45` | 2,490,000.00 USD | 3,300.00 USD | 0.00 USD | `+7.32%` | `31.94` |
| `Live` | `Short` | `103.65` | 2,490,000.00 USD | 4,360.00 USD | 0.00 USD | `+7.53%` | `42.09` |
| `Live` | `Short` | `103.75` | 2,750,000.00 USD | 261,050.00 USD | 0.00 USD | `+7.63%` | `2,516.13` |
| `Live` | `Short` | `103.85` | 2,770,000.00 USD | 14,630.00 USD | 0.00 USD | `+7.73%` | `140.89` |
| `Live` | `Short` | `103.95` | 2,770,000.00 USD | 827.44 USD | 0.00 USD | `+7.84%` | `7.96` |
| `Live` | `Short` | `104.05` | 2,770,000.00 USD | 1,110.00 USD | 0.00 USD | `+7.94%` | `10.66` |
| `Live` | `Short` | `104.15` | 2,770,000.00 USD | 1,180.00 USD | 0.00 USD | `+8.05%` | `11.34` |
| `Live` | `Short` | `104.25` | 2,810,000.00 USD | 40,840.00 USD | 0.00 USD | `+8.15%` | `391.71` |
| `Live` | `Short` | `104.35` | 2,830,000.00 USD | 14,580.00 USD | 0.00 USD | `+8.25%` | `139.68` |
| `Live` | `Short` | `104.45` | 2,840,000.00 USD | 9,560.00 USD | 0.00 USD | `+8.36%` | `91.52` |
| `Live` | `Short` | `104.55` | 2,840,000.00 USD | 575.03 USD | 0.00 USD | `+8.46%` | `5.50` |
| `Live` | `Short` | `104.65` | 2,840,000.00 USD | 401.86 USD | 0.00 USD | `+8.56%` | `3.84` |
| `Live` | `Short` | `104.75` | 2,840,000.00 USD | 3,620.00 USD | 0.00 USD | `+8.67%` | `34.59` |
| `Live` | `Short` | `104.85` | 2,870,000.00 USD | 31,470.00 USD | 0.00 USD | `+8.77%` | `300.15` |
| `Live` | `Short` | `104.95` | 3,000,000.00 USD | 125,660.00 USD | 0.00 USD | `+8.87%` | `1,197.29` |
| `Live` | `Short` | `105.05` | 3,000,000.00 USD | 578.83 USD | 0.00 USD | `+8.98%` | `5.51` |
| `Live` | `Short` | `105.15` | 3,010,000.00 USD | 13,330.00 USD | 0.00 USD | `+9.08%` | `126.78` |
| `Live` | `Short` | `105.25` | 3,010,000.00 USD | 2,110.00 USD | 0.00 USD | `+9.19%` | `20.07` |
| `Live` | `Short` | `105.35` | 3,020,000.00 USD | 6,840.00 USD | 0.00 USD | `+9.29%` | `64.89` |
| `Live` | `Short` | `105.45` | 3,550,000.00 USD | 531,450.00 USD | 0.00 USD | `+9.39%` | `5,039.81` |
| `Live` | `Short` | `105.55` | 3,560,000.00 USD | 4,180.00 USD | 0.00 USD | `+9.50%` | `39.61` |
| `Live` | `Short` | `105.65` | 3,560,000.00 USD | 1,950.00 USD | 0.00 USD | `+9.60%` | `18.49` |
| `Live` | `Short` | `105.75` | 3,560,000.00 USD | 4,160.00 USD | 0.00 USD | `+9.70%` | `39.37` |
| `Live` | `Short` | `105.85` | 3,650,000.00 USD | 91,370.00 USD | 0.00 USD | `+9.81%` | `863.23` |
| `Live` | `Short` | `105.95` | 3,650,000.00 USD | 592.26 USD | 0.00 USD | `+9.91%` | `5.59` |
| `Live` | `Short` | `106.05` | 3,690,000.00 USD | 33,380.00 USD | 0.00 USD | `+10.02%` | `314.77` |
| `Live` | `Short` | `106.25` | 3,690,000.00 USD | 1,970.00 USD | 0.00 USD | `+10.22%` | `18.57` |
| `Live` | `Short` | `106.35` | 3,950,000.00 USD | 256,690.00 USD | 0.00 USD | `+10.33%` | `2,413.61` |
| `Live` | `Short` | `106.45` | 4,160,000.00 USD | 216,090.00 USD | 0.00 USD | `+10.43%` | `2,029.98` |
| `Live` | `Short` | `106.55` | 4,160,000.00 USD | 219.49 USD | 0.00 USD | `+10.53%` | `2.06` |
| `Live` | `Short` | `106.65` | 4,170,000.00 USD | 6,680.00 USD | 0.00 USD | `+10.64%` | `62.64` |
| `Live` | `Short` | `106.85` | 4,650,000.00 USD | 479,350.00 USD | 0.00 USD | `+10.85%` | `4,486.21` |
| `Live` | `Short` | `106.95` | 4,650,000.00 USD | 131.55 USD | 0.00 USD | `+10.95%` | `1.23` |
| `Live` | `Short` | `107.05` | 4,660,000.00 USD | 14,600.00 USD | 0.00 USD | `+11.05%` | `136.36` |
| `Live` | `Short` | `107.15` | 4,670,000.00 USD | 3,060.00 USD | 0.00 USD | `+11.16%` | `28.58` |
| `Live` | `Short` | `107.25` | 4,700,000.00 USD | 34,950.00 USD | 0.00 USD | `+11.26%` | `325.92` |
| `Live` | `Short` | `107.35` | 4,700,000.00 USD | 766.48 USD | 0.00 USD | `+11.36%` | `7.14` |
| `Live` | `Short` | `107.45` | 4,730,000.00 USD | 32,580.00 USD | 0.00 USD | `+11.47%` | `303.18` |
| `Live` | `Short` | `107.55` | 4,740,000.00 USD | 221.55 USD | 0.00 USD | `+11.57%` | `2.06` |
| `Live` | `Short` | `107.85` | 4,880,000.00 USD | 143,340.00 USD | 0.00 USD | `+11.88%` | `1,329.08` |
| `Live` | `Short` | `107.95` | 4,890,000.00 USD | 8,330.00 USD | 0.00 USD | `+11.99%` | `77.19` |
| `Live` | `Short` | `108.05` | 4,890,000.00 USD | 1,080.00 USD | 0.00 USD | `+12.09%` | `10.04` |
| `Live` | `Short` | `108.15` | 4,890,000.00 USD | 1,150.00 USD | 0.00 USD | `+12.19%` | `10.66` |
| `Live` | `Short` | `108.25` | 5,050,000.00 USD | 162,440.00 USD | 0.00 USD | `+12.30%` | `1,500.57` |
| `Live` | `Short` | `108.35` | 5,050,000.00 USD | 3,470.00 USD | 0.00 USD | `+12.40%` | `32.00` |
| `Live` | `Short` | `108.45` | 5,160,000.00 USD | 108,080.00 USD | 0.00 USD | `+12.51%` | `996.61` |
| `Live` | `Short` | `108.55` | 5,160,000.00 USD | 381.01 USD | 0.00 USD | `+12.61%` | `3.51` |
| `Live` | `Short` | `108.65` | 5,170,000.00 USD | 5,050.00 USD | 0.00 USD | `+12.71%` | `46.45` |
| `Live` | `Short` | `108.85` | 5,170,000.00 USD | 3,980.00 USD | 0.00 USD | `+12.92%` | `36.58` |
| `Live` | `Short` | `108.95` | 5,180,000.00 USD | 3,170.00 USD | 0.00 USD | `+13.02%` | `29.10` |
| `Live` | `Short` | `109.05` | 5,180,000.00 USD | 356.59 USD | 0.00 USD | `+13.13%` | `3.27` |
| `Live` | `Short` | `109.25` | 9,620,000.00 USD | 4,450,000.00 USD | 0.00 USD | `+13.34%` | `40,716.81` |
| `Live` | `Short` | `109.35` | 9,640,000.00 USD | 20,440.00 USD | 0.00 USD | `+13.44%` | `186.91` |
| `Live` | `Short` | `109.45` | 9,650,000.00 USD | 426.86 USD | 0.00 USD | `+13.54%` | `3.90` |
| `Live` | `Short` | `109.55` | 9,650,000.00 USD | 356.04 USD | 0.00 USD | `+13.65%` | `3.25` |
| `Live` | `Short` | `109.65` | 9,680,000.00 USD | 38,750.00 USD | 0.00 USD | `+13.75%` | `353.42` |
| `Live` | `Short` | `109.75` | 10,090,000.00 USD | 408,730.00 USD | 0.00 USD | `+13.85%` | `3,724.17` |
| `Live` | `Short` | `109.85` | 10,090,000.00 USD | 459.17 USD | 0.00 USD | `+13.96%` | `4.18` |
| `Live` | `Short` | `109.95` | 10,090,000.00 USD | 301.26 USD | 0.00 USD | `+14.06%` | `2.74` |
| `Live` | `Short` | `110.05` | 10,110,000.00 USD | 14,790.00 USD | 0.00 USD | `+14.17%` | `134.36` |
| `Live` | `Short` | `110.15` | 10,140,000.00 USD | 33,240.00 USD | 0.00 USD | `+14.27%` | `301.77` |
| `Live` | `Short` | `110.25` | 10,140,000.00 USD | 226.01 USD | 0.00 USD | `+14.37%` | `2.05` |
| `Live` | `Short` | `110.35` | 10,290,000.00 USD | 143,450.00 USD | 0.00 USD | `+14.48%` | `1,299.99` |
| `Live` | `Short` | `110.45` | 10,290,000.00 USD | 376.63 USD | 0.00 USD | `+14.58%` | `3.41` |
| `Live` | `Short` | `110.55` | 10,290,000.00 USD | 203.41 USD | 0.00 USD | `+14.68%` | `1.84` |
| `Live` | `Short` | `110.85` | 10,310,000.00 USD | 28,970.00 USD | 0.00 USD | `+15.00%` | `261.31` |
| `Live` | `Short` | `110.95` | 10,320,000.00 USD | 4,450.00 USD | 0.00 USD | `+15.10%` | `40.12` |
| `Live` | `Short` | `111.15` | 10,320,000.00 USD | 1,710.00 USD | 0.00 USD | `+15.31%` | `15.37` |
| `Live` | `Short` | `111.35` | 10,320,000.00 USD | 390.84 USD | 0.00 USD | `+15.51%` | `3.51` |
| `Live` | `Short` | `111.45` | 10,320,000.00 USD | 841.45 USD | 0.00 USD | `+15.62%` | `7.55` |
| `Live` | `Short` | `111.55` | 10,320,000.00 USD | 892.40 USD | 0.00 USD | `+15.72%` | `8.00` |
| `Live` | `Short` | `111.65` | 10,320,000.00 USD | 199.85 USD | 0.00 USD | `+15.83%` | `1.79` |
| `Live` | `Short` | `111.75` | 10,320,000.00 USD | 169.86 USD | 0.00 USD | `+15.93%` | `1.52` |
| `Live` | `Short` | `111.85` | 10,340,000.00 USD | 15,880.00 USD | 0.00 USD | `+16.03%` | `141.95` |
| `Live` | `Short` | `111.95` | 10,340,000.00 USD | 223.90 USD | 0.00 USD | `+16.14%` | `2.00` |
| `Live` | `Short` | `112.05` | 10,340,000.00 USD | 1,640.00 USD | 0.00 USD | `+16.24%` | `14.66` |
| `Live` | `Short` | `112.15` | 10,340,000.00 USD | 291.59 USD | 0.00 USD | `+16.34%` | `2.60` |
| `Live` | `Short` | `112.35` | 10,600,000.00 USD | 262,980.00 USD | 0.00 USD | `+16.55%` | `2,340.72` |
| `Live` | `Short` | `112.45` | 10,610,000.00 USD | 5,670.00 USD | 0.00 USD | `+16.66%` | `50.42` |
| `Live` | `Short` | `112.55` | 10,610,000.00 USD | 1,070.00 USD | 0.00 USD | `+16.76%` | `9.55` |
| `Live` | `Short` | `112.65` | 10,610,000.00 USD | 707.44 USD | 0.00 USD | `+16.86%` | `6.28` |
| `Live` | `Short` | `112.75` | 10,730,000.00 USD | 118,640.00 USD | 0.00 USD | `+16.97%` | `1,052.24` |
| `Live` | `Short` | `112.85` | 10,840,000.00 USD | 108,760.00 USD | 0.00 USD | `+17.07%` | `963.76` |
| `Live` | `Short` | `113.05` | 10,840,000.00 USD | 406.98 USD | 0.00 USD | `+17.28%` | `3.60` |
| `Live` | `Short` | `113.15` | 10,880,000.00 USD | 37,800.00 USD | 0.00 USD | `+17.38%` | `334.03` |
| `Live` | `Short` | `113.25` | 10,880,000.00 USD | 698.75 USD | 0.00 USD | `+17.49%` | `6.17` |
| `Live` | `Short` | `113.35` | 10,880,000.00 USD | 4,970.00 USD | 0.00 USD | `+17.59%` | `43.83` |
| `Live` | `Short` | `113.45` | 10,890,000.00 USD | 3,360.00 USD | 0.00 USD | `+17.69%` | `29.62` |
| `Live` | `Short` | `113.55` | 10,900,000.00 USD | 17,470.00 USD | 0.00 USD | `+17.80%` | `153.86` |
| `Live` | `Short` | `113.65` | 10,910,000.00 USD | 4,360.00 USD | 0.00 USD | `+17.90%` | `38.38` |
| `Live` | `Short` | `113.75` | 11,020,000.00 USD | 107,800.00 USD | 0.00 USD | `+18.00%` | `947.67` |
| `Live` | `Short` | `113.85` | 11,020,000.00 USD | 2,470.00 USD | 0.00 USD | `+18.11%` | `21.72` |
| `Live` | `Short` | `113.95` | 11,040,000.00 USD | 21,840.00 USD | 0.00 USD | `+18.21%` | `191.69` |
| `Live` | `Short` | `114.05` | 11,070,000.00 USD | 31,740.00 USD | 0.00 USD | `+18.32%` | `278.26` |
| `Live` | `Short` | `114.15` | 11,070,000.00 USD | 253.41 USD | 0.00 USD | `+18.42%` | `2.22` |
| `Live` | `Short` | `114.25` | 11,070,000.00 USD | 2,370.00 USD | 0.00 USD | `+18.52%` | `20.72` |
| `Live` | `Short` | `114.45` | 11,080,000.00 USD | 3,830.00 USD | 0.00 USD | `+18.73%` | `33.46` |
| `Live` | `Short` | `114.65` | 11,080,000.00 USD | 3,430.00 USD | 0.00 USD | `+18.94%` | `29.93` |
| `Live` | `Short` | `115.05` | 11,650,000.00 USD | 569,550.00 USD | 0.00 USD | `+19.35%` | `4,950.49` |
| `Live` | `Short` | `115.15` | 11,650,000.00 USD | 1,100.00 USD | 0.00 USD | `+19.46%` | `9.52` |
| `Live` | `Short` | `115.25` | 11,650,000.00 USD | 1,260.00 USD | 0.00 USD | `+19.56%` | `10.94` |
| `Live` | `Short` | `115.45` | 12,530,000.00 USD | 879,040.00 USD | 0.00 USD | `+19.77%` | `7,614.00` |
| `Live` | `Short` | `115.55` | 12,700,000.00 USD | 167,330.00 USD | 0.00 USD | `+19.87%` | `1,448.12` |
| `Live` | `Short` | `115.65` | 12,710,000.00 USD | 5,970.00 USD | 0.00 USD | `+19.98%` | `51.58` |
| `Live` | `Short` | `115.75` | 12,720,000.00 USD | 14,920.00 USD | 0.00 USD | `+20.08%` | `128.93` |
| `Live` | `Short` | `115.85` | 12,720,000.00 USD | 289.62 USD | 0.00 USD | `+20.18%` | `2.50` |
| `Live` | `Short` | `116.05` | 12,730,000.00 USD | 5,930.00 USD | 0.00 USD | `+20.39%` | `51.14` |
| `Live` | `Short` | `116.25` | 12,730,000.00 USD | 6,270.00 USD | 0.00 USD | `+20.60%` | `53.91` |
| `Live` | `Short` | `116.35` | 12,740,000.00 USD | 4,960.00 USD | 0.00 USD | `+20.70%` | `42.60` |
| `Live` | `Short` | `116.55` | 12,740,000.00 USD | 2,040.00 USD | 0.00 USD | `+20.91%` | `17.52` |
| `Live` | `Short` | `116.65` | 12,740,000.00 USD | 113.15 USD | 0.00 USD | `+21.01%` | `0.97` |
| `Live` | `Short` | `116.85` | 12,750,000.00 USD | 10,520.00 USD | 0.00 USD | `+21.22%` | `90.00` |
| `Live` | `Short` | `117.05` | 12,750,000.00 USD | 156.85 USD | 0.00 USD | `+21.43%` | `1.34` |
| `Live` | `Short` | `117.15` | 12,840,000.00 USD | 89,950.00 USD | 0.00 USD | `+21.53%` | `767.80` |
| `Live` | `Short` | `117.35` | 12,850,000.00 USD | 11,610.00 USD | 0.00 USD | `+21.74%` | `98.95` |
| `Live` | `Short` | `117.55` | 12,850,000.00 USD | 635.95 USD | 0.00 USD | `+21.95%` | `5.41` |
| `Live` | `Short` | `117.75` | 12,860,000.00 USD | 10,360.00 USD | 0.00 USD | `+22.15%` | `87.98` |
| `Live` | `Short` | `117.95` | 12,870,000.00 USD | 1,890.00 USD | 0.00 USD | `+22.36%` | `16.05` |
| `Live` | `Short` | `118.25` | 12,880,000.00 USD | 9,280.00 USD | 0.00 USD | `+22.67%` | `78.51` |
| `Live` | `Short` | `118.45` | 12,910,000.00 USD | 30,080.00 USD | 0.00 USD | `+22.88%` | `253.91` |
| `Live` | `Short` | `118.55` | 12,910,000.00 USD | 7,700.00 USD | 0.00 USD | `+22.98%` | `64.98` |
| `Live` | `Short` | `118.65` | 17,400,000.00 USD | 4,480,000.00 USD | 0.00 USD | `+23.09%` | `37,796.13` |
| `Live` | `Short` | `118.75` | 17,400,000.00 USD | 309.94 USD | 0.00 USD | `+23.19%` | `2.61` |
| `Live` | `Short` | `118.85` | 17,400,000.00 USD | 5,750.00 USD | 0.00 USD | `+23.29%` | `48.34` |
| `Live` | `Short` | `119.25` | 17,400,000.00 USD | 240.88 USD | 0.00 USD | `+23.71%` | `2.02` |
| `Live` | `Short` | `119.35` | 17,460,000.00 USD | 58,320.00 USD | 0.00 USD | `+23.81%` | `488.65` |
| `Live` | `Short` | `119.55` | 17,470,000.00 USD | 8,970.00 USD | 0.00 USD | `+24.02%` | `75.00` |
| `Live` | `Short` | `119.75` | 17,470,000.00 USD | 261.06 USD | 0.00 USD | `+24.23%` | `2.18` |
| `Live` | `Short` | `119.85` | 17,470,000.00 USD | 485.39 USD | 0.00 USD | `+24.33%` | `4.05` |
| `Live` | `Short` | `120.15` | 17,500,000.00 USD | 31,040.00 USD | 0.00 USD | `+24.64%` | `258.38` |
| `Live` | `Short` | `120.25` | 17,600,000.00 USD | 97,590.00 USD | 0.00 USD | `+24.75%` | `811.55` |
| `Live` | `Short` | `120.35` | 17,600,000.00 USD | 145.62 USD | 0.00 USD | `+24.85%` | `1.21` |
| `Live` | `Short` | `120.45` | 17,600,000.00 USD | 968.42 USD | 0.00 USD | `+24.95%` | `8.04` |
| `Live` | `Short` | `120.55` | 17,600,000.00 USD | 1,190.00 USD | 0.00 USD | `+25.06%` | `9.86` |
| `Live` | `Short` | `120.65` | 17,600,000.00 USD | 1,110.00 USD | 0.00 USD | `+25.16%` | `9.19` |
| `Live` | `Short` | `120.85` | 17,600,000.00 USD | 123.27 USD | 0.00 USD | `+25.37%` | `1.02` |
| `Live` | `Short` | `120.95` | 17,620,000.00 USD | 13,290.00 USD | 0.00 USD | `+25.47%` | `109.91` |
| `Live` | `Short` | `121.05` | 17,680,000.00 USD | 60,700.00 USD | 0.00 USD | `+25.58%` | `501.43` |
| `Live` | `Short` | `121.15` | 17,680,000.00 USD | 316.20 USD | 0.00 USD | `+25.68%` | `2.61` |
| `Live` | `Short` | `121.45` | 17,720,000.00 USD | 42,460.00 USD | 0.00 USD | `+25.99%` | `349.58` |
| `Live` | `Short` | `121.55` | 17,730,000.00 USD | 5,940.00 USD | 0.00 USD | `+26.10%` | `48.87` |
| `Live` | `Short` | `121.75` | 17,730,000.00 USD | 105.92 USD | 0.00 USD | `+26.30%` | `0.87` |
| `Live` | `Short` | `122.05` | 17,780,000.00 USD | 56,150.00 USD | 0.00 USD | `+26.61%` | `460.06` |
| `Live` | `Short` | `122.15` | 17,780,000.00 USD | 169.79 USD | 0.00 USD | `+26.72%` | `1.39` |
| `Live` | `Short` | `122.25` | 17,790,000.00 USD | 4,210.00 USD | 0.00 USD | `+26.82%` | `34.46` |
| `Live` | `Short` | `122.45` | 18,690,000.00 USD | 899,680.00 USD | 0.00 USD | `+27.03%` | `7,347.30` |
| `Live` | `Short` | `122.65` | 18,690,000.00 USD | 116.52 USD | 0.00 USD | `+27.24%` | `0.95` |
| `Live` | `Short` | `123.25` | 19,160,000.00 USD | 471,560.00 USD | 0.00 USD | `+27.86%` | `3,826.05` |
| `Live` | `Short` | `123.35` | 19,160,000.00 USD | 2,330.00 USD | 0.00 USD | `+27.96%` | `18.92` |
| `Live` | `Short` | `123.45` | 19,160,000.00 USD | 1,960.00 USD | 0.00 USD | `+28.07%` | `15.87` |
| `Live` | `Short` | `123.75` | 19,290,000.00 USD | 124,610.00 USD | 0.00 USD | `+28.38%` | `1,006.96` |
| `Live` | `Short` | `123.95` | 19,320,000.00 USD | 36,200.00 USD | 0.00 USD | `+28.59%` | `292.09` |
| `Live` | `Short` | `124.05` | 19,320,000.00 USD | 586.76 USD | 0.00 USD | `+28.69%` | `4.73` |
| `Live` | `Short` | `124.15` | 19,320,000.00 USD | 121.67 USD | 0.00 USD | `+28.79%` | `0.98` |
| `Live` | `Short` | `124.25` | 19,350,000.00 USD | 23,360.00 USD | 0.00 USD | `+28.90%` | `188.01` |
| `Live` | `Short` | `124.35` | 19,350,000.00 USD | 775.94 USD | 0.00 USD | `+29.00%` | `6.24` |
| `Live` | `Short` | `124.55` | 24,110,000.00 USD | 4,760,000.00 USD | 0.00 USD | `+29.21%` | `38,235.81` |
| `Live` | `Short` | `124.65` | 24,110,000.00 USD | 675.60 USD | 0.00 USD | `+29.31%` | `5.42` |
| `Live` | `Short` | `124.75` | 24,120,000.00 USD | 5,330.00 USD | 0.00 USD | `+29.42%` | `42.73` |
| `Live` | `Short` | `124.95` | 24,170,000.00 USD | 49,090.00 USD | 0.00 USD | `+29.62%` | `392.91` |
| `Live` | `Short` | `125.05` | 24,170,000.00 USD | 208.83 USD | 0.00 USD | `+29.73%` | `1.67` |
| `Live` | `Short` | `125.15` | 24,170,000.00 USD | 6,260.00 USD | 0.00 USD | `+29.83%` | `50.00` |
| `Live` | `Short` | `125.35` | 24,180,000.00 USD | 5,320.00 USD | 0.00 USD | `+30.04%` | `42.44` |
| `Live` | `Short` | `125.45` | 24,180,000.00 USD | 590.87 USD | 0.00 USD | `+30.14%` | `4.71` |
| `Live` | `Short` | `125.55` | 24,180,000.00 USD | 4,610.00 USD | 0.00 USD | `+30.25%` | `36.71` |
| `Live` | `Short` | `125.65` | 24,180,000.00 USD | 1,560.00 USD | 0.00 USD | `+30.35%` | `12.41` |
| `Live` | `Short` | `125.75` | 24,190,000.00 USD | 1,930.00 USD | 0.00 USD | `+30.45%` | `15.31` |
| `Live` | `Short` | `125.95` | 24,190,000.00 USD | 110.84 USD | 0.00 USD | `+30.66%` | `0.88` |
| `Live` | `Short` | `126.05` | 24,190,000.00 USD | 810.50 USD | 0.00 USD | `+30.76%` | `6.43` |
| `Live` | `Short` | `126.15` | 24,190,000.00 USD | 470.54 USD | 0.00 USD | `+30.87%` | `3.73` |
| `Live` | `Short` | `126.35` | 24,190,000.00 USD | 4,350.00 USD | 0.00 USD | `+31.08%` | `34.43` |
| `Live` | `Short` | `126.45` | 24,200,000.00 USD | 4,880.00 USD | 0.00 USD | `+31.18%` | `38.63` |
| `Live` | `Short` | `126.55` | 24,200,000.00 USD | 403.69 USD | 0.00 USD | `+31.28%` | `3.19` |
| `Live` | `Short` | `126.65` | 24,230,000.00 USD | 30,830.00 USD | 0.00 USD | `+31.39%` | `243.46` |
| `Live` | `Short` | `126.85` | 24,230,000.00 USD | 3,870.00 USD | 0.00 USD | `+31.59%` | `30.49` |
| `Live` | `Short` | `127.05` | 24,230,000.00 USD | 2,030.00 USD | 0.00 USD | `+31.80%` | `16.01` |
| `Live` | `Short` | `127.15` | 24,230,000.00 USD | 389.08 USD | 0.00 USD | `+31.91%` | `3.06` |
| `Live` | `Short` | `127.35` | 24,260,000.00 USD | 29,060.00 USD | 0.00 USD | `+32.11%` | `228.18` |
| `Live` | `Short` | `127.45` | 24,260,000.00 USD | 138.92 USD | 0.00 USD | `+32.22%` | `1.09` |
| `Live` | `Short` | `127.55` | 24,270,000.00 USD | 4,460.00 USD | 0.00 USD | `+32.32%` | `35.00` |
| `Live` | `Short` | `127.65` | 24,270,000.00 USD | 4,840.00 USD | 0.00 USD | `+32.42%` | `37.89` |
| `Live` | `Short` | `127.75` | 24,290,000.00 USD | 20,800.00 USD | 0.00 USD | `+32.53%` | `162.83` |
| `Live` | `Short` | `127.85` | 24,290,000.00 USD | 388.66 USD | 0.00 USD | `+32.63%` | `3.04` |
| `Live` | `Short` | `127.95` | 24,310,000.00 USD | 12,330.00 USD | 0.00 USD | `+32.74%` | `96.34` |
| `Live` | `Short` | `128.05` | 24,420,000.00 USD | 116,190.00 USD | 0.00 USD | `+32.84%` | `907.38` |
| `Live` | `Short` | `128.15` | 24,420,000.00 USD | 1,000.00 USD | 0.00 USD | `+32.94%` | `7.83` |
| `Live` | `Short` | `128.35` | 24,420,000.00 USD | 195.09 USD | 0.00 USD | `+33.15%` | `1.52` |
| `Live` | `Short` | `128.65` | 24,430,000.00 USD | 788.62 USD | 0.00 USD | `+33.46%` | `6.13` |
| `Live` | `Short` | `128.75` | 24,440,000.00 USD | 18,730.00 USD | 0.00 USD | `+33.57%` | `145.45` |
| `Live` | `Short` | `128.85` | 24,480,000.00 USD | 32,440.00 USD | 0.00 USD | `+33.67%` | `251.77` |
| `Live` | `Short` | `129.15` | 24,530,000.00 USD | 55,570.00 USD | 0.00 USD | `+33.98%` | `430.25` |
| `Live` | `Short` | `129.25` | 24,560,000.00 USD | 32,310.00 USD | 0.00 USD | `+34.08%` | `250.00` |
| `Live` | `Short` | `129.35` | 24,600,000.00 USD | 35,060.00 USD | 0.00 USD | `+34.19%` | `271.06` |
| `Live` | `Short` | `129.45` | 24,600,000.00 USD | 730.10 USD | 0.00 USD | `+34.29%` | `5.64` |
| `Live` | `Short` | `129.55` | 24,600,000.00 USD | 910.74 USD | 0.00 USD | `+34.39%` | `7.03` |
| `Live` | `Short` | `129.65` | 25,300,000.00 USD | 700,970.00 USD | 0.00 USD | `+34.50%` | `5,406.67` |
| `Live` | `Short` | `129.75` | 25,300,000.00 USD | 2,210.00 USD | 0.00 USD | `+34.60%` | `17.05` |
| `Live` | `Short` | `129.85` | 25,300,000.00 USD | 490.83 USD | 0.00 USD | `+34.71%` | `3.78` |
| `Live` | `Short` | `130.25` | 25,300,000.00 USD | 145.88 USD | 0.00 USD | `+35.12%` | `1.12` |
| `Live` | `Short` | `130.45` | 25,650,000.00 USD | 343,340.00 USD | 0.00 USD | `+35.33%` | `2,631.99` |
| `Live` | `Short` | `130.85` | 25,650,000.00 USD | 3,180.00 USD | 0.00 USD | `+35.74%` | `24.34` |
| `Live` | `Short` | `130.95` | 25,650,000.00 USD | 2,070.00 USD | 0.00 USD | `+35.85%` | `15.84` |
| `Live` | `Short` | `131.05` | 25,650,000.00 USD | 188.71 USD | 0.00 USD | `+35.95%` | `1.44` |
| `Live` | `Short` | `131.25` | 25,650,000.00 USD | 1,560.00 USD | 0.00 USD | `+36.16%` | `11.87` |
| `Live` | `Short` | `131.35` | 25,670,000.00 USD | 14,210.00 USD | 0.00 USD | `+36.26%` | `108.18` |
| `Live` | `Short` | `131.45` | 25,670,000.00 USD | 219.52 USD | 0.00 USD | `+36.37%` | `1.67` |
| `Live` | `Short` | `131.65` | 25,690,000.00 USD | 17,640.00 USD | 0.00 USD | `+36.57%` | `134.01` |
| `Live` | `Short` | `131.85` | 25,690,000.00 USD | 3,210.00 USD | 0.00 USD | `+36.78%` | `24.35` |
| `Live` | `Short` | `132.05` | 25,690,000.00 USD | 1,710.00 USD | 0.00 USD | `+36.99%` | `12.93` |
| `Live` | `Short` | `132.15` | 25,730,000.00 USD | 33,680.00 USD | 0.00 USD | `+37.09%` | `254.83` |
| `Live` | `Short` | `132.45` | 25,730,000.00 USD | 8,530.00 USD | 0.00 USD | `+37.40%` | `64.37` |
| `Live` | `Short` | `132.55` | 25,730,000.00 USD | 196.17 USD | 0.00 USD | `+37.51%` | `1.48` |
| `Live` | `Short` | `132.65` | 25,730,000.00 USD | 240.10 USD | 0.00 USD | `+37.61%` | `1.81` |
| `Live` | `Short` | `132.75` | 25,730,000.00 USD | 136.73 USD | 0.00 USD | `+37.71%` | `1.03` |
| `Live` | `Short` | `132.85` | 25,780,000.00 USD | 49,280.00 USD | 0.00 USD | `+37.82%` | `370.98` |
| `Live` | `Short` | `133.05` | 25,790,000.00 USD | 1,700.00 USD | 0.00 USD | `+38.03%` | `12.75` |
| `Live` | `Short` | `133.15` | 25,790,000.00 USD | 8,440.00 USD | 0.00 USD | `+38.13%` | `63.42` |
| `Live` | `Short` | `133.25` | 25,800,000.00 USD | 1,330.00 USD | 0.00 USD | `+38.23%` | `9.95` |
| `Live` | `Short` | `133.65` | 25,800,000.00 USD | 156.37 USD | 0.00 USD | `+38.65%` | `1.17` |
| `Live` | `Short` | `133.75` | 25,950,000.00 USD | 151,200.00 USD | 0.00 USD | `+38.75%` | `1,130.50` |
| `Live` | `Short` | `133.95` | 25,950,000.00 USD | 503.65 USD | 0.00 USD | `+38.96%` | `3.76` |
| `Live` | `Short` | `134.05` | 25,960,000.00 USD | 12,620.00 USD | 0.00 USD | `+39.06%` | `94.18` |
| `Live` | `Short` | `134.15` | 25,960,000.00 USD | 2,510.00 USD | 0.00 USD | `+39.17%` | `18.74` |
| `Live` | `Short` | `134.25` | 25,970,000.00 USD | 11,590.00 USD | 0.00 USD | `+39.27%` | `86.32` |
| `Live` | `Short` | `134.95` | 25,970,000.00 USD | 395.40 USD | 0.00 USD | `+40.00%` | `2.93` |
| `Live` | `Short` | `135.45` | 25,990,000.00 USD | 14,560.00 USD | 0.00 USD | `+40.52%` | `107.50` |
| `Live` | `Short` | `135.65` | 25,990,000.00 USD | 415.09 USD | 0.00 USD | `+40.72%` | `3.06` |
| `Live` | `Short` | `135.85` | 26,000,000.00 USD | 9,680.00 USD | 0.00 USD | `+40.93%` | `71.24` |
| `Live` | `Short` | `135.95` | 26,000,000.00 USD | 504.37 USD | 0.00 USD | `+41.03%` | `3.71` |
| `Live` | `Short` | `136.25` | 26,050,000.00 USD | 49,000.00 USD | 0.00 USD | `+41.35%` | `359.64` |
| `Live` | `Short` | `136.45` | 26,050,000.00 USD | 1,500.00 USD | 0.00 USD | `+41.55%` | `11.00` |
| `Live` | `Short` | `136.55` | 26,060,000.00 USD | 8,700.00 USD | 0.00 USD | `+41.66%` | `63.70` |
| `Live` | `Short` | `136.65` | 26,060,000.00 USD | 1,110.00 USD | 0.00 USD | `+41.76%` | `8.14` |
| `Live` | `Short` | `136.95` | 26,090,000.00 USD | 34,240.00 USD | 0.00 USD | `+42.07%` | `250.00` |
| `Live` | `Short` | `137.05` | 26,100,000.00 USD | 836.00 USD | 0.00 USD | `+42.18%` | `6.10` |
| `Live` | `Short` | `137.15` | 26,100,000.00 USD | 809.19 USD | 0.00 USD | `+42.28%` | `5.90` |
| `Live` | `Short` | `137.85` | 26,160,000.00 USD | 68,930.00 USD | 0.00 USD | `+43.01%` | `500.00` |
| `Live` | `Short` | `138.05` | 26,170,000.00 USD | 1,270.00 USD | 0.00 USD | `+43.21%` | `9.20` |
| `Live` | `Short` | `138.15` | 26,210,000.00 USD | 41,450.00 USD | 0.00 USD | `+43.32%` | `300.00` |
| `Live` | `Short` | `138.25` | 26,250,000.00 USD | 45,220.00 USD | 0.00 USD | `+43.42%` | `327.11` |
| `Live` | `Short` | `138.35` | 26,270,000.00 USD | 15,400.00 USD | 0.00 USD | `+43.52%` | `111.33` |
| `Live` | `Short` | `138.45` | 26,280,000.00 USD | 9,370.00 USD | 0.00 USD | `+43.63%` | `67.70` |
| `Live` | `Short` | `138.65` | 26,280,000.00 USD | 4,160.00 USD | 0.00 USD | `+43.84%` | `30.00` |
| `Live` | `Short` | `138.75` | 26,280,000.00 USD | 2,360.00 USD | 0.00 USD | `+43.94%` | `17.04` |
| `Live` | `Short` | `138.85` | 26,290,000.00 USD | 9,290.00 USD | 0.00 USD | `+44.04%` | `66.89` |
| `Live` | `Short` | `139.15` | 26,290,000.00 USD | 552.43 USD | 0.00 USD | `+44.35%` | `3.97` |
| `Live` | `Short` | `139.35` | 26,290,000.00 USD | 253.62 USD | 0.00 USD | `+44.56%` | `1.82` |
| `Live` | `Short` | `139.55` | 26,290,000.00 USD | 494.01 USD | 0.00 USD | `+44.77%` | `3.54` |
| `Live` | `Short` | `139.75` | 26,300,000.00 USD | 4,870.00 USD | 0.00 USD | `+44.98%` | `34.82` |
| `Live` | `Short` | `139.95` | 26,300,000.00 USD | 394.66 USD | 0.00 USD | `+45.18%` | `2.82` |
| `Live` | `Short` | `140.05` | 26,300,000.00 USD | 1,800.00 USD | 0.00 USD | `+45.29%` | `12.85` |
| `Live` | `Short` | `140.35` | 26,300,000.00 USD | 127.72 USD | 0.00 USD | `+45.60%` | `0.91` |
| `Live` | `Short` | `140.45` | 26,310,000.00 USD | 4,870.00 USD | 0.00 USD | `+45.70%` | `34.66` |
| `Live` | `Short` | `140.55` | 26,310,000.00 USD | 8,030.00 USD | 0.00 USD | `+45.81%` | `57.16` |
| `Live` | `Short` | `140.65` | 26,320,000.00 USD | 4,210.00 USD | 0.00 USD | `+45.91%` | `29.93` |
| `Live` | `Short` | `140.95` | 26,320,000.00 USD | 1,940.00 USD | 0.00 USD | `+46.22%` | `13.73` |
| `Live` | `Short` | `141.05` | 26,320,000.00 USD | 3,710.00 USD | 0.00 USD | `+46.33%` | `26.29` |
| `Live` | `Short` | `141.15` | 26,390,000.00 USD | 67,420.00 USD | 0.00 USD | `+46.43%` | `477.67` |
| `Live` | `Short` | `141.35` | 31,490,000.00 USD | 5,100,000.00 USD | 0.00 USD | `+46.64%` | `36,101.07` |
| `Live` | `Short` | `141.45` | 31,740,000.00 USD | 247,540.00 USD | 0.00 USD | `+46.74%` | `1,750.00` |
| `Live` | `Short` | `141.55` | 31,750,000.00 USD | 2,770.00 USD | 0.00 USD | `+46.84%` | `19.56` |
| `Live` | `Short` | `141.65` | 31,750,000.00 USD | 1,220.00 USD | 0.00 USD | `+46.95%` | `8.59` |
| `Live` | `Short` | `141.75` | 31,750,000.00 USD | 2,250.00 USD | 0.00 USD | `+47.05%` | `15.84` |
| `Live` | `Short` | `141.85` | 33,700,000.00 USD | 1,950,000.00 USD | 0.00 USD | `+47.15%` | `13,744.62` |
| `Live` | `Short` | `141.95` | 33,700,000.00 USD | 211.51 USD | 0.00 USD | `+47.26%` | `1.49` |
| `Live` | `Short` | `142.25` | 33,700,000.00 USD | 3,470.00 USD | 0.00 USD | `+47.57%` | `24.41` |
| `Live` | `Short` | `142.35` | 33,770,000.00 USD | 71,180.00 USD | 0.00 USD | `+47.67%` | `500.00` |
| `Live` | `Short` | `142.45` | 33,800,000.00 USD | 23,250.00 USD | 0.00 USD | `+47.78%` | `163.25` |
| `Live` | `Short` | `142.55` | 33,840,000.00 USD | 42,080.00 USD | 0.00 USD | `+47.88%` | `295.19` |
| `Live` | `Short` | `142.65` | 33,930,000.00 USD | 87,970.00 USD | 0.00 USD | `+47.98%` | `616.67` |
| `Live` | `Short` | `142.75` | 33,930,000.00 USD | 368.30 USD | 0.00 USD | `+48.09%` | `2.58` |
| `Live` | `Short` | `143.15` | 33,930,000.00 USD | 1,460.00 USD | 0.00 USD | `+48.50%` | `10.22` |
| `Live` | `Short` | `143.35` | 33,950,000.00 USD | 22,260.00 USD | 0.00 USD | `+48.71%` | `155.27` |
| `Live` | `Short` | `143.45` | 33,950,000.00 USD | 790.41 USD | 0.00 USD | `+48.81%` | `5.51` |
| `Live` | `Short` | `143.55` | 33,950,000.00 USD | 103.36 USD | 0.00 USD | `+48.92%` | `0.72` |
| `Live` | `Short` | `143.65` | 33,950,000.00 USD | 2,840.00 USD | 0.00 USD | `+49.02%` | `19.75` |
| `Live` | `Short` | `143.75` | 33,960,000.00 USD | 1,710.00 USD | 0.00 USD | `+49.13%` | `11.91` |
| `Live` | `Short` | `143.85` | 33,960,000.00 USD | 1,480.00 USD | 0.00 USD | `+49.23%` | `10.26` |
| `Live` | `Short` | `143.95` | 33,960,000.00 USD | 285.02 USD | 0.00 USD | `+49.33%` | `1.98` |
| `Live` | `Short` | `144.05` | 33,960,000.00 USD | 3,750.00 USD | 0.00 USD | `+49.44%` | `26.00` |
| `Live` | `Short` | `144.25` | 34,000,000.00 USD | 34,630.00 USD | 0.00 USD | `+49.64%` | `240.07` |
| `Live` | `Short` | `144.55` | 34,600,000.00 USD | 599,880.00 USD | 0.00 USD | `+49.96%` | `4,150.00` |
| `Live` | `Short` | `144.65` | 34,600,000.00 USD | 1,240.00 USD | 0.00 USD | `+50.06%` | `8.60` |
| `Live` | `Short` | `145.15` | 34,600,000.00 USD | 1,760.00 USD | 0.00 USD | `+50.58%` | `12.12` |
| `Live` | `Short` | `145.25` | 34,600,000.00 USD | 1,090.00 USD | 0.00 USD | `+50.68%` | `7.50` |
| `Live` | `Short` | `145.45` | 34,630,000.00 USD | 28,990.00 USD | 0.00 USD | `+50.89%` | `199.30` |
| `Live` | `Short` | `145.55` | 34,630,000.00 USD | 1,270.00 USD | 0.00 USD | `+50.99%` | `8.75` |
| `Live` | `Short` | `145.75` | 34,630,000.00 USD | 1,340.00 USD | 0.00 USD | `+51.20%` | `9.22` |
| `Live` | `Short` | `145.85` | 34,640,000.00 USD | 5,990.00 USD | 0.00 USD | `+51.30%` | `41.09` |
| `Live` | `Short` | `145.95` | 34,740,000.00 USD | 106,560.00 USD | 0.00 USD | `+51.41%` | `730.14` |
| `Live` | `Short` | `146.15` | 34,830,000.00 USD | 88,760.00 USD | 0.00 USD | `+51.62%` | `607.33` |
| `Live` | `Short` | `146.25` | 34,860,000.00 USD | 22,210.00 USD | 0.00 USD | `+51.72%` | `151.85` |
| `Live` | `Short` | `146.35` | 34,860,000.00 USD | 7,330.00 USD | 0.00 USD | `+51.82%` | `50.10` |
| `Live` | `Short` | `146.45` | 34,860,000.00 USD | 1,400.00 USD | 0.00 USD | `+51.93%` | `9.57` |
| `Live` | `Short` | `146.55` | 34,940,000.00 USD | 74,780.00 USD | 0.00 USD | `+52.03%` | `510.30` |
| `Live` | `Short` | `146.65` | 35,530,000.00 USD | 587,730.00 USD | 0.00 USD | `+52.13%` | `4,007.68` |
| `Live` | `Short` | `146.75` | 35,530,000.00 USD | 493.08 USD | 0.00 USD | `+52.24%` | `3.36` |
| `Live` | `Short` | `146.85` | 35,970,000.00 USD | 442,670.00 USD | 0.00 USD | `+52.34%` | `3,014.41` |
| `Live` | `Short` | `146.95` | 35,970,000.00 USD | 3,340.00 USD | 0.00 USD | `+52.45%` | `22.76` |
| `Live` | `Short` | `147.05` | 35,970,000.00 USD | 166.17 USD | 0.00 USD | `+52.55%` | `1.13` |
| `Live` | `Short` | `147.15` | 36,000,000.00 USD | 30,890.00 USD | 0.00 USD | `+52.65%` | `209.92` |
| `Live` | `Short` | `147.35` | 36,000,000.00 USD | 169.45 USD | 0.00 USD | `+52.86%` | `1.15` |
| `Live` | `Short` | `147.45` | 36,000,000.00 USD | 204.96 USD | 0.00 USD | `+52.96%` | `1.39` |
| `Live` | `Short` | `147.55` | 36,010,000.00 USD | 1,690.00 USD | 0.00 USD | `+53.07%` | `11.48` |
| `Live` | `Short` | `147.65` | 36,010,000.00 USD | 237.72 USD | 0.00 USD | `+53.17%` | `1.61` |
| `Live` | `Short` | `147.85` | 36,010,000.00 USD | 510.08 USD | 0.00 USD | `+53.38%` | `3.45` |
| `Live` | `Short` | `148.15` | 36,010,000.00 USD | 102.22 USD | 0.00 USD | `+53.69%` | `0.69` |
| `Live` | `Short` | `148.45` | 36,010,000.00 USD | 163.29 USD | 0.00 USD | `+54.00%` | `1.10` |
| `Live` | `Short` | `148.55` | 36,350,000.00 USD | 344,780.00 USD | 0.00 USD | `+54.11%` | `2,321.00` |
| `Live` | `Short` | `148.65` | 36,430,000.00 USD | 78,850.00 USD | 0.00 USD | `+54.21%` | `530.42` |
| `Live` | `Short` | `148.75` | 36,530,000.00 USD | 99,350.00 USD | 0.00 USD | `+54.31%` | `667.91` |
| `Live` | `Short` | `148.85` | 37,050,000.00 USD | 520,980.00 USD | 0.00 USD | `+54.42%` | `3,500.00` |
| `Live` | `Short` | `149.55` | 37,050,000.00 USD | 116.65 USD | 0.00 USD | `+55.14%` | `0.78` |
| `Live` | `Short` | `149.65` | 38,460,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+55.25%` | `9,389.48` |
| `Live` | `Short` | `149.85` | 38,580,000.00 USD | 123,060.00 USD | 0.00 USD | `+55.45%` | `821.21` |
| `Live` | `Short` | `149.95` | 38,810,000.00 USD | 234,200.00 USD | 0.00 USD | `+55.56%` | `1,561.87` |
| `Live` | `Short` | `150.05` | 38,820,000.00 USD | 2,930.00 USD | 0.00 USD | `+55.66%` | `19.54` |
| `Live` | `Short` | `150.15` | 38,820,000.00 USD | 642.64 USD | 0.00 USD | `+55.77%` | `4.28` |
| `Live` | `Short` | `150.35` | 38,920,000.00 USD | 105,250.00 USD | 0.00 USD | `+55.97%` | `700.00` |
| `Live` | `Short` | `150.55` | 43,490,000.00 USD | 4,560,000.00 USD | 0.00 USD | `+56.18%` | `30,310.49` |
| `Live` | `Short` | `151.15` | 43,490,000.00 USD | 3,530.00 USD | 0.00 USD | `+56.80%` | `23.35` |
| `Live` | `Short` | `151.25` | 43,490,000.00 USD | 2,370.00 USD | 0.00 USD | `+56.91%` | `15.69` |
| `Live` | `Short` | `151.45` | 43,500,000.00 USD | 8,830.00 USD | 0.00 USD | `+57.11%` | `58.32` |
| `Live` | `Short` | `151.95` | 43,500,000.00 USD | 1,920.00 USD | 0.00 USD | `+57.63%` | `12.64` |
| `Live` | `Short` | `152.25` | 45,370,000.00 USD | 1,860,000.00 USD | 0.00 USD | `+57.94%` | `12,240.90` |
| `Live` | `Short` | `152.35` | 47,400,000.00 USD | 2,040,000.00 USD | 0.00 USD | `+58.05%` | `13,369.14` |
| `Live` | `Short` | `152.45` | 47,450,000.00 USD | 47,900.00 USD | 0.00 USD | `+58.15%` | `314.22` |
| `Live` | `Short` | `152.65` | 47,450,000.00 USD | 615.18 USD | 0.00 USD | `+58.36%` | `4.03` |
| `Live` | `Short` | `152.75` | 47,450,000.00 USD | 1,570.00 USD | 0.00 USD | `+58.46%` | `10.30` |
| `Live` | `Short` | `152.85` | 47,470,000.00 USD | 13,500.00 USD | 0.00 USD | `+58.57%` | `88.35` |
| `Live` | `Short` | `153.05` | 47,470,000.00 USD | 1,060.00 USD | 0.00 USD | `+58.77%` | `6.95` |
| `Live` | `Short` | `153.25` | 47,470,000.00 USD | 239.07 USD | 0.00 USD | `+58.98%` | `1.56` |
| `Live` | `Short` | `153.35` | 47,470,000.00 USD | 2,300.00 USD | 0.00 USD | `+59.09%` | `15.00` |
| `Live` | `Short` | `153.45` | 47,520,000.00 USD | 47,510.00 USD | 0.00 USD | `+59.19%` | `309.63` |
| `Live` | `Short` | `153.65` | 47,530,000.00 USD | 8,340.00 USD | 0.00 USD | `+59.40%` | `54.29` |
| `Live` | `Short` | `153.85` | 47,530,000.00 USD | 995.41 USD | 0.00 USD | `+59.60%` | `6.47` |
| `Live` | `Short` | `154.15` | 47,530,000.00 USD | 292.89 USD | 0.00 USD | `+59.91%` | `1.90` |
| `Live` | `Short` | `154.25` | 47,530,000.00 USD | 2,340.00 USD | 0.00 USD | `+60.02%` | `15.20` |
| `Live` | `Short` | `154.45` | 47,530,000.00 USD | 4,240.00 USD | 0.00 USD | `+60.23%` | `27.45` |
| `Live` | `Short` | `154.75` | 47,530,000.00 USD | 363.66 USD | 0.00 USD | `+60.54%` | `2.35` |
| `Live` | `Short` | `155.05` | 47,540,000.00 USD | 1,500.00 USD | 0.00 USD | `+60.85%` | `9.68` |
| `Live` | `Short` | `155.25` | 47,540,000.00 USD | 3,020.00 USD | 0.00 USD | `+61.06%` | `19.46` |
| `Live` | `Short` | `155.55` | 47,540,000.00 USD | 267.55 USD | 0.00 USD | `+61.37%` | `1.72` |
| `Live` | `Short` | `155.75` | 47,540,000.00 USD | 118.37 USD | 0.00 USD | `+61.57%` | `0.76` |
| `Live` | `Short` | `156.15` | 47,540,000.00 USD | 326.35 USD | 0.00 USD | `+61.99%` | `2.09` |
| `Live` | `Short` | `156.25` | 47,550,000.00 USD | 7,810.00 USD | 0.00 USD | `+62.09%` | `50.00` |
| `Live` | `Short` | `156.35` | 47,550,000.00 USD | 197.00 USD | 0.00 USD | `+62.20%` | `1.26` |
| `Live` | `Short` | `156.45` | 47,550,000.00 USD | 4,900.00 USD | 0.00 USD | `+62.30%` | `31.29` |
| `Live` | `Short` | `156.65` | 47,550,000.00 USD | 1,170.00 USD | 0.00 USD | `+62.51%` | `7.50` |
| `Live` | `Short` | `157.15` | 47,600,000.00 USD | 49,270.00 USD | 0.00 USD | `+63.03%` | `313.50` |
| `Live` | `Short` | `157.65` | 47,600,000.00 USD | 654.25 USD | 0.00 USD | `+63.55%` | `4.15` |
| `Live` | `Short` | `157.75` | 47,700,000.00 USD | 92,600.00 USD | 0.00 USD | `+63.65%` | `587.00` |
| `Live` | `Short` | `158.25` | 47,700,000.00 USD | 299.09 USD | 0.00 USD | `+64.17%` | `1.89` |
| `Live` | `Short` | `158.65` | 47,930,000.00 USD | 237,980.00 USD | 0.00 USD | `+64.58%` | `1,500.00` |
| `Live` | `Short` | `159.05` | 47,980,000.00 USD | 44,690.00 USD | 0.00 USD | `+65.00%` | `281.00` |
| `Live` | `Short` | `159.45` | 47,980,000.00 USD | 2,410.00 USD | 0.00 USD | `+65.41%` | `15.09` |
| `Live` | `Short` | `159.65` | 47,980,000.00 USD | 1,760.00 USD | 0.00 USD | `+65.62%` | `11.01` |
| `Live` | `Short` | `159.75` | 47,980,000.00 USD | 656.57 USD | 0.00 USD | `+65.72%` | `4.11` |
| `Live` | `Short` | `159.85` | 51,620,000.00 USD | 3,640,000.00 USD | 0.00 USD | `+65.83%` | `22,770.74` |
| `Live` | `Short` | `160.15` | 52,310,000.00 USD | 683,000.00 USD | 0.00 USD | `+66.14%` | `4,264.75` |
| `Live` | `Short` | `160.25` | 52,310,000.00 USD | 498.38 USD | 0.00 USD | `+66.24%` | `3.11` |
| `Live` | `Short` | `160.35` | 52,310,000.00 USD | 7,070.00 USD | 0.00 USD | `+66.35%` | `44.12` |
| `Live` | `Short` | `160.55` | 52,310,000.00 USD | 449.54 USD | 0.00 USD | `+66.55%` | `2.80` |
| `Live` | `Short` | `160.75` | 52,750,000.00 USD | 434,020.00 USD | 0.00 USD | `+66.76%` | `2,700.00` |
| `Live` | `Short` | `160.95` | 52,780,000.00 USD | 28,210.00 USD | 0.00 USD | `+66.97%` | `175.30` |
| `Live` | `Short` | `161.05` | 53,030,000.00 USD | 255,020.00 USD | 0.00 USD | `+67.07%` | `1,583.47` |
| `Live` | `Short` | `161.15` | 53,130,000.00 USD | 102,630.00 USD | 0.00 USD | `+67.18%` | `636.89` |
| `Live` | `Short` | `161.25` | 53,140,000.00 USD | 4,120.00 USD | 0.00 USD | `+67.28%` | `25.54` |
| `Live` | `Short` | `161.35` | 53,160,000.00 USD | 21,430.00 USD | 0.00 USD | `+67.38%` | `132.81` |
| `Live` | `Short` | `161.55` | 53,160,000.00 USD | 410.34 USD | 0.00 USD | `+67.59%` | `2.54` |
| `Live` | `Short` | `161.75` | 53,300,000.00 USD | 142,240.00 USD | 0.00 USD | `+67.80%` | `879.39` |
| `Live` | `Short` | `161.95` | 53,450,000.00 USD | 144,610.00 USD | 0.00 USD | `+68.01%` | `892.95` |
| `Live` | `Short` | `162.05` | 53,850,000.00 USD | 405,950.00 USD | 0.00 USD | `+68.11%` | `2,505.07` |
| `Live` | `Short` | `162.15` | 53,860,000.00 USD | 5,970.00 USD | 0.00 USD | `+68.21%` | `36.83` |
| `Live` | `Short` | `162.45` | 53,950,000.00 USD | 86,540.00 USD | 0.00 USD | `+68.53%` | `532.74` |
| `Live` | `Short` | `162.95` | 53,960,000.00 USD | 19,080.00 USD | 0.00 USD | `+69.04%` | `117.09` |
| `Live` | `Short` | `163.85` | 53,970,000.00 USD | 786.48 USD | 0.00 USD | `+69.98%` | `4.80` |
| `Live` | `Short` | `163.95` | 54,170,000.00 USD | 207,900.00 USD | 0.00 USD | `+70.08%` | `1,268.05` |
| `Live` | `Short` | `165.15` | 54,170,000.00 USD | 198.18 USD | 0.00 USD | `+71.33%` | `1.20` |
| `Live` | `Short` | `165.65` | 54,180,000.00 USD | 3,420.00 USD | 0.00 USD | `+71.85%` | `20.63` |
| `Live` | `Short` | `166.05` | 54,180,000.00 USD | 149.45 USD | 0.00 USD | `+72.26%` | `0.90` |
| `Live` | `Short` | `166.15` | 54,180,000.00 USD | 996.90 USD | 0.00 USD | `+72.36%` | `6.00` |
| `Live` | `Short` | `166.25` | 54,190,000.00 USD | 14,070.00 USD | 0.00 USD | `+72.47%` | `84.61` |
| `Live` | `Short` | `166.45` | 54,190,000.00 USD | 1,380.00 USD | 0.00 USD | `+72.67%` | `8.29` |
| `Live` | `Short` | `166.75` | 54,190,000.00 USD | 685.34 USD | 0.00 USD | `+72.99%` | `4.11` |
| `Live` | `Short` | `166.95` | 54,200,000.00 USD | 3,230.00 USD | 0.00 USD | `+73.19%` | `19.33` |
| `Live` | `Short` | `167.65` | 54,200,000.00 USD | 115.68 USD | 0.00 USD | `+73.92%` | `0.69` |
| `Live` | `Short` | `167.75` | 54,200,000.00 USD | 1,890.00 USD | 0.00 USD | `+74.02%` | `11.27` |
| `Live` | `Short` | `168.05` | 54,200,000.00 USD | 122.68 USD | 0.00 USD | `+74.33%` | `0.73` |
| `Live` | `Short` | `168.15` | 54,310,000.00 USD | 111,420.00 USD | 0.00 USD | `+74.44%` | `662.62` |
| `Live` | `Short` | `168.25` | 54,310,000.00 USD | 629.25 USD | 0.00 USD | `+74.54%` | `3.74` |
| `Live` | `Short` | `168.35` | 54,330,000.00 USD | 19,740.00 USD | 0.00 USD | `+74.65%` | `117.24` |
| `Live` | `Short` | `168.65` | 54,660,000.00 USD | 325,850.00 USD | 0.00 USD | `+74.96%` | `1,932.10` |
| `Live` | `Short` | `169.45` | 60,380,000.00 USD | 5,720,000.00 USD | 0.00 USD | `+75.79%` | `33,744.03` |
| `Live` | `Short` | `169.55` | 60,380,000.00 USD | 847.75 USD | 0.00 USD | `+75.89%` | `5.00` |
| `Live` | `Short` | `170.05` | 60,380,000.00 USD | 6,000.00 USD | 0.00 USD | `+76.41%` | `35.27` |
| `Live` | `Short` | `170.75` | 60,380,000.00 USD | 447.37 USD | 0.00 USD | `+77.14%` | `2.62` |
| `Live` | `Short` | `171.45` | 60,380,000.00 USD | 111.44 USD | 0.00 USD | `+77.86%` | `0.65` |
| `Live` | `Short` | `171.75` | 60,570,000.00 USD | 182,360.00 USD | 0.00 USD | `+78.17%` | `1,061.79` |
| `Live` | `Short` | `172.05` | 60,590,000.00 USD | 20,480.00 USD | 0.00 USD | `+78.48%` | `119.02` |
| `Live` | `Short` | `172.45` | 60,640,000.00 USD | 51,730.00 USD | 0.00 USD | `+78.90%` | `300.00` |
| `Live` | `Short` | `172.85` | 60,640,000.00 USD | 1,190.00 USD | 0.00 USD | `+79.31%` | `6.88` |
| `Live` | `Short` | `173.25` | 60,670,000.00 USD | 36,050.00 USD | 0.00 USD | `+79.73%` | `208.07` |
| `Live` | `Short` | `173.35` | 60,670,000.00 USD | 284.29 USD | 0.00 USD | `+79.83%` | `1.64` |
| `Live` | `Short` | `173.45` | 60,690,000.00 USD | 16,540.00 USD | 0.00 USD | `+79.94%` | `95.36` |
| `Live` | `Short` | `173.85` | 60,690,000.00 USD | 695.40 USD | 0.00 USD | `+80.35%` | `4.00` |
| `Live` | `Short` | `173.95` | 60,720,000.00 USD | 25,850.00 USD | 0.00 USD | `+80.46%` | `148.59` |
| `Live` | `Short` | `174.05` | 60,750,000.00 USD | 28,180.00 USD | 0.00 USD | `+80.56%` | `161.92` |
| `Live` | `Short` | `174.15` | 60,850,000.00 USD | 104,490.00 USD | 0.00 USD | `+80.66%` | `600.00` |
| `Live` | `Short` | `174.25` | 61,100,000.00 USD | 245,010.00 USD | 0.00 USD | `+80.77%` | `1,406.07` |
| `Live` | `Short` | `174.35` | 61,300,000.00 USD | 205,490.00 USD | 0.00 USD | `+80.87%` | `1,178.60` |
| `Live` | `Short` | `174.55` | 61,320,000.00 USD | 18,550.00 USD | 0.00 USD | `+81.08%` | `106.26` |
| `Live` | `Short` | `174.75` | 61,320,000.00 USD | 146.79 USD | 0.00 USD | `+81.29%` | `0.84` |
| `Live` | `Short` | `175.35` | 61,320,000.00 USD | 119.24 USD | 0.00 USD | `+81.91%` | `0.68` |
| `Live` | `Short` | `175.75` | 61,320,000.00 USD | 263.62 USD | 0.00 USD | `+82.32%` | `1.50` |
| `Live` | `Short` | `176.05` | 61,320,000.00 USD | 2,960.00 USD | 0.00 USD | `+82.63%` | `16.82` |
| `Live` | `Short` | `176.15` | 61,320,000.00 USD | 350.54 USD | 0.00 USD | `+82.74%` | `1.99` |
| `Live` | `Short` | `176.25` | 61,320,000.00 USD | 625.69 USD | 0.00 USD | `+82.84%` | `3.55` |
| `Live` | `Short` | `176.35` | 61,340,000.00 USD | 19,940.00 USD | 0.00 USD | `+82.95%` | `113.07` |
| `Live` | `Short` | `176.55` | 100,190,000.00 USD | 38,840,000.00 USD | 0.00 USD | `+83.15%` | `220,000.19` |
| `Live` | `Short` | `176.95` | 100,290,000.00 USD | 106,170.00 USD | 0.00 USD | `+83.57%` | `600.00` |
| `Live` | `Short` | `177.05` | 100,760,000.00 USD | 470,750.00 USD | 0.00 USD | `+83.67%` | `2,658.88` |
| `Live` | `Short` | `177.45` | 100,770,000.00 USD | 12,000.00 USD | 0.00 USD | `+84.09%` | `67.60` |
| `Live` | `Short` | `177.65` | 104,330,000.00 USD | 3,550,000.00 USD | 0.00 USD | `+84.29%` | `20,003.59` |
| `Live` | `Short` | `177.95` | 104,410,000.00 USD | 78,300.00 USD | 0.00 USD | `+84.61%` | `440.00` |
| `Live` | `Short` | `178.05` | 104,430,000.00 USD | 25,750.00 USD | 0.00 USD | `+84.71%` | `144.60` |
| `Live` | `Short` | `178.35` | 104,460,000.00 USD | 33,140.00 USD | 0.00 USD | `+85.02%` | `185.84` |
| `Live` | `Short` | `178.45` | 104,470,000.00 USD | 2,440.00 USD | 0.00 USD | `+85.12%` | `13.65` |
| `Live` | `Short` | `178.95` | 104,470,000.00 USD | 2,830.00 USD | 0.00 USD | `+85.64%` | `15.84` |
| `Live` | `Short` | `179.25` | 105,510,000.00 USD | 1,040,000.00 USD | 0.00 USD | `+85.95%` | `5,807.37` |
| `Live` | `Short` | `179.85` | 105,520,000.00 USD | 4,500.00 USD | 0.00 USD | `+86.58%` | `25.00` |
| `Live` | `Short` | `179.95` | 105,520,000.00 USD | 2,030.00 USD | 0.00 USD | `+86.68%` | `11.27` |
| `Live` | `Short` | `180.05` | 105,560,000.00 USD | 45,030.00 USD | 0.00 USD | `+86.78%` | `250.10` |
| `Live` | `Short` | `180.25` | 105,570,000.00 USD | 3,730.00 USD | 0.00 USD | `+86.99%` | `20.70` |
| `Live` | `Short` | `180.35` | 106,910,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+87.09%` | `7,439.01` |
| `Live` | `Short` | `180.55` | 107,060,000.00 USD | 148,410.00 USD | 0.00 USD | `+87.30%` | `822.01` |
| `Live` | `Short` | `180.75` | 107,130,000.00 USD | 72,300.00 USD | 0.00 USD | `+87.51%` | `400.00` |
| `Live` | `Short` | `181.15` | 107,130,000.00 USD | 5,020.00 USD | 0.00 USD | `+87.92%` | `27.73` |
| `Live` | `Short` | `181.25` | 107,150,000.00 USD | 18,120.00 USD | 0.00 USD | `+88.03%` | `100.00` |
| `Live` | `Short` | `181.55` | 107,150,000.00 USD | 254.17 USD | 0.00 USD | `+88.34%` | `1.40` |
| `Live` | `Short` | `181.75` | 107,150,000.00 USD | 727.00 USD | 0.00 USD | `+88.55%` | `4.00` |
| `Live` | `Short` | `182.05` | 107,240,000.00 USD | 91,030.00 USD | 0.00 USD | `+88.86%` | `500.00` |
| `Live` | `Short` | `182.15` | 107,250,000.00 USD | 3,990.00 USD | 0.00 USD | `+88.96%` | `21.93` |
| `Live` | `Short` | `182.75` | 107,250,000.00 USD | 1,370.00 USD | 0.00 USD | `+89.58%` | `7.52` |
| `Live` | `Short` | `184.25` | 107,250,000.00 USD | 1,680.00 USD | 0.00 USD | `+91.14%` | `9.12` |
| `Live` | `Short` | `184.35` | 107,250,000.00 USD | 993.65 USD | 0.00 USD | `+91.24%` | `5.39` |
| `Live` | `Short` | `184.45` | 107,260,000.00 USD | 9,540.00 USD | 0.00 USD | `+91.35%` | `51.72` |
| `Live` | `Short` | `184.95` | 107,430,000.00 USD | 165,230.00 USD | 0.00 USD | `+91.87%` | `893.35` |
| `Live` | `Short` | `185.25` | 107,440,000.00 USD | 13,750.00 USD | 0.00 USD | `+92.18%` | `74.22` |
| `Live` | `Short` | `185.45` | 107,440,000.00 USD | 2,770.00 USD | 0.00 USD | `+92.39%` | `14.94` |
| `Live` | `Short` | `185.65` | 107,450,000.00 USD | 7,830.00 USD | 0.00 USD | `+92.59%` | `42.17` |
| `Live` | `Short` | `186.85` | 107,450,000.00 USD | 2,190.00 USD | 0.00 USD | `+93.84%` | `11.72` |
| `Live` | `Short` | `187.15` | 107,460,000.00 USD | 2,450.00 USD | 0.00 USD | `+94.15%` | `13.11` |
| `Live` | `Short` | `187.65` | 107,460,000.00 USD | 232.69 USD | 0.00 USD | `+94.67%` | `1.24` |
| `Live` | `Short` | `187.85` | 107,460,000.00 USD | 1,560.00 USD | 0.00 USD | `+94.88%` | `8.32` |
| `Live` | `Short` | `188.05` | 111,270,000.00 USD | 3,820,000.00 USD | 0.00 USD | `+95.08%` | `20,287.30` |
| `Live` | `Short` | `188.55` | 111,270,000.00 USD | 231.92 USD | 0.00 USD | `+95.60%` | `1.23` |
| `Live` | `Short` | `188.65` | 111,300,000.00 USD | 29,110.00 USD | 0.00 USD | `+95.71%` | `154.32` |
| `Live` | `Short` | `188.75` | 111,300,000.00 USD | 813.51 USD | 0.00 USD | `+95.81%` | `4.31` |
| `Live` | `Short` | `188.95` | 111,300,000.00 USD | 1,450.00 USD | 0.00 USD | `+96.02%` | `7.69` |
| `Live` | `Short` | `189.15` | 111,300,000.00 USD | 257.24 USD | 0.00 USD | `+96.22%` | `1.36` |
| `Live` | `Short` | `189.25` | 111,300,000.00 USD | 456.09 USD | 0.00 USD | `+96.33%` | `2.41` |
| `Live` | `Short` | `189.55` | 111,310,000.00 USD | 284.33 USD | 0.00 USD | `+96.64%` | `1.50` |
| `Live` | `Short` | `189.65` | 111,310,000.00 USD | 117.58 USD | 0.00 USD | `+96.74%` | `0.62` |
| `Live` | `Short` | `189.75` | 111,310,000.00 USD | 1,010.00 USD | 0.00 USD | `+96.85%` | `5.30` |
| `Live` | `Short` | `189.85` | 111,310,000.00 USD | 189.85 USD | 0.00 USD | `+96.95%` | `1.00` |
| `Live` | `Short` | `189.95` | 111,590,000.00 USD | 284,930.00 USD | 0.00 USD | `+97.05%` | `1,500.00` |
| `Live` | `Short` | `190.15` | 111,590,000.00 USD | 148.32 USD | 0.00 USD | `+97.26%` | `0.78` |
| `Live` | `Short` | `190.45` | 111,590,000.00 USD | 118.08 USD | 0.00 USD | `+97.57%` | `0.62` |
| `Live` | `Short` | `190.65` | 111,590,000.00 USD | 278.35 USD | 0.00 USD | `+97.78%` | `1.46` |
| `Live` | `Short` | `190.95` | 125,160,000.00 USD | 13,570,000.00 USD | 0.00 USD | `+98.09%` | `71,044.42` |
| `Live` | `Short` | `191.15` | 125,160,000.00 USD | 191.15 USD | 0.00 USD | `+98.30%` | `1.00` |
| `Live` | `Short` | `191.25` | 125,160,000.00 USD | 118.58 USD | 0.00 USD | `+98.40%` | `0.62` |
| `Live` | `Short` | `191.55` | 125,220,000.00 USD | 62,850.00 USD | 0.00 USD | `+98.71%` | `328.11` |
| `Live` | `Short` | `191.95` | 125,220,000.00 USD | 322.48 USD | 0.00 USD | `+99.13%` | `1.68` |
| `Live` | `Short` | `192.65` | 125,230,000.00 USD | 9,300.00 USD | 0.00 USD | `+99.85%` | `48.28` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.05` | 10,460,000.00 USD | 0.00 USD | 14,190.00 USD | `-76.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.35` | 10,440,000.00 USD | 0.00 USD | 499.56 USD | `-68.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `32.05` | 10,440,000.00 USD | 0.00 USD | 1,230.00 USD | `-66.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.05` | 10,440,000.00 USD | 0.00 USD | 818.32 USD | `-65.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.85` | 10,440,000.00 USD | 0.00 USD | 1,340.00 USD | `-63.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 10,440,000.00 USD | 0.00 USD | 2,160.00 USD | `-62.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.45` | 10,440,000.00 USD | 0.00 USD | 434.85 USD | `-62.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.05` | 10,440,000.00 USD | 0.00 USD | 267.87 USD | `-60.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.55` | 10,440,000.00 USD | 0.00 USD | 3,460.00 USD | `-58.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.75` | 10,430,000.00 USD | 0.00 USD | 157.01 USD | `-58.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 10,430,000.00 USD | 0.00 USD | 1,050.00 USD | `-58.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.75` | 10,430,000.00 USD | 0.00 USD | 120.66 USD | `-56.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.15` | 10,430,000.00 USD | 0.00 USD | 121.81 USD | `-56.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.55` | 10,430,000.00 USD | 0.00 USD | 170,530.00 USD | `-55.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.75` | 10,260,000.00 USD | 0.00 USD | 105.00 USD | `-54.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 10,260,000.00 USD | 0.00 USD | 64,240.00 USD | `-53.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.75` | 10,200,000.00 USD | 0.00 USD | 251.05 USD | `-51.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.75` | 10,200,000.00 USD | 0.00 USD | 143.25 USD | `-50.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.85` | 10,200,000.00 USD | 0.00 USD | 191.40 USD | `-50.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 10,200,000.00 USD | 0.00 USD | 50,240.00 USD | `-50.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.55` | 10,150,000.00 USD | 0.00 USD | 664.65 USD | `-49.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.75` | 10,150,000.00 USD | 0.00 USD | 103.35 USD | `-49.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 10,150,000.00 USD | 0.00 USD | 4,660.00 USD | `-48.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.25` | 10,140,000.00 USD | 0.00 USD | 107.03 USD | `-47.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 10,140,000.00 USD | 0.00 USD | 102.62 USD | `-47.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.25` | 10,140,000.00 USD | 0.00 USD | 134.28 USD | `-46.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 10,140,000.00 USD | 0.00 USD | 3,950.00 USD | `-46.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.15` | 10,140,000.00 USD | 0.00 USD | 102.74 USD | `-45.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 10,140,000.00 USD | 0.00 USD | 126.12 USD | `-45.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 10,140,000.00 USD | 0.00 USD | 200.15 USD | `-45.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 10,140,000.00 USD | 0.00 USD | 24,450.00 USD | `-44.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 10,110,000.00 USD | 0.00 USD | 1,660.00 USD | `-44.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 10,110,000.00 USD | 0.00 USD | 641.57 USD | `-43.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 10,110,000.00 USD | 0.00 USD | 139.87 USD | `-43.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 10,110,000.00 USD | 0.00 USD | 209.19 USD | `-42.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 10,110,000.00 USD | 0.00 USD | 4,350.00 USD | `-41.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 10,110,000.00 USD | 0.00 USD | 894.56 USD | `-41.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 10,100,000.00 USD | 0.00 USD | 4,930.00 USD | `-41.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 10,100,000.00 USD | 0.00 USD | 6,790.00 USD | `-40.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.35` | 10,090,000.00 USD | 0.00 USD | 265.53 USD | `-40.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.95` | 10,090,000.00 USD | 0.00 USD | 268.31 USD | `-39.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.05` | 10,090,000.00 USD | 0.00 USD | 158.48 USD | `-39.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.15` | 10,090,000.00 USD | 0.00 USD | 3,820.00 USD | `-39.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.25` | 10,090,000.00 USD | 0.00 USD | 428.72 USD | `-39.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.05` | 10,090,000.00 USD | 0.00 USD | 295.25 USD | `-38.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.35` | 10,090,000.00 USD | 0.00 USD | 200.01 USD | `-38.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.55` | 10,090,000.00 USD | 0.00 USD | 1,460.00 USD | `-38.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.95` | 10,090,000.00 USD | 0.00 USD | 9,040.00 USD | `-37.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.05` | 10,080,000.00 USD | 0.00 USD | 35,050.00 USD | `-37.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.15` | 10,040,000.00 USD | 0.00 USD | 2,820.00 USD | `-37.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.25` | 10,040,000.00 USD | 0.00 USD | 488.63 USD | `-37.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.35` | 10,040,000.00 USD | 0.00 USD | 258.90 USD | `-37.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.45` | 10,040,000.00 USD | 0.00 USD | 206.13 USD | `-37.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.55` | 10,040,000.00 USD | 0.00 USD | 724.78 USD | `-37.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.05` | 10,040,000.00 USD | 0.00 USD | 14,350.00 USD | `-36.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.35` | 10,020,000.00 USD | 0.00 USD | 142.33 USD | `-36.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.45` | 10,020,000.00 USD | 0.00 USD | 100.78 USD | `-36.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.55` | 10,020,000.00 USD | 0.00 USD | 243.74 USD | `-36.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.05` | 10,020,000.00 USD | 0.00 USD | 6,720.00 USD | `-35.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.55` | 10,020,000.00 USD | 0.00 USD | 136.98 USD | `-35.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.05` | 10,020,000.00 USD | 0.00 USD | 9,990.00 USD | `-34.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.55` | 10,010,000.00 USD | 0.00 USD | 2,980.00 USD | `-34.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.95` | 10,000,000.00 USD | 0.00 USD | 222.55 USD | `-33.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.25` | 10,000,000.00 USD | 0.00 USD | 163.19 USD | `-33.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.85` | 10,000,000.00 USD | 0.00 USD | 129.70 USD | `-32.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.05` | 10,000,000.00 USD | 0.00 USD | 2,450.00 USD | `-32.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.15` | 10,000,000.00 USD | 0.00 USD | 2,190.00 USD | `-32.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.55` | 10,000,000.00 USD | 0.00 USD | 2,200.00 USD | `-32.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.05` | 9,990,000.00 USD | 0.00 USD | 7,100.00 USD | `-31.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.55` | 9,990,000.00 USD | 0.00 USD | 541.72 USD | `-30.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.05` | 9,990,000.00 USD | 0.00 USD | 335.25 USD | `-30.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.15` | 9,990,000.00 USD | 0.00 USD | 268.60 USD | `-30.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.05` | 9,990,000.00 USD | 0.00 USD | 13,310.00 USD | `-29.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.45` | 9,970,000.00 USD | 0.00 USD | 7,600.00 USD | `-28.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.55` | 9,970,000.00 USD | 0.00 USD | 5,610.00 USD | `-28.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.65` | 9,960,000.00 USD | 0.00 USD | 552.63 USD | `-28.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.75` | 9,960,000.00 USD | 0.00 USD | 1,200.00 USD | `-28.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.05` | 9,960,000.00 USD | 0.00 USD | 11,360.00 USD | `-28.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.15` | 9,950,000.00 USD | 0.00 USD | 172.18 USD | `-28.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.25` | 9,950,000.00 USD | 0.00 USD | 668.96 USD | `-28.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.65` | 9,950,000.00 USD | 0.00 USD | 107.96 USD | `-27.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.75` | 9,950,000.00 USD | 0.00 USD | 42,360.00 USD | `-27.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.85` | 9,900,000.00 USD | 0.00 USD | 365.32 USD | `-27.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.95` | 9,900,000.00 USD | 0.00 USD | 1,510.00 USD | `-27.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.05` | 9,900,000.00 USD | 0.00 USD | 43,920.00 USD | `-27.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.25` | 9,860,000.00 USD | 0.00 USD | 5,270.00 USD | `-27.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.35` | 9,850,000.00 USD | 0.00 USD | 562.80 USD | `-27.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.55` | 9,850,000.00 USD | 0.00 USD | 681.51 USD | `-26.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.65` | 9,850,000.00 USD | 0.00 USD | 4,920.00 USD | `-26.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.75` | 9,850,000.00 USD | 0.00 USD | 2,790.00 USD | `-26.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.05` | 9,840,000.00 USD | 0.00 USD | 265.02 USD | `-26.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.35` | 9,840,000.00 USD | 0.00 USD | 32,450.00 USD | `-25.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.45` | 9,810,000.00 USD | 0.00 USD | 289.37 USD | `-25.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.65` | 9,810,000.00 USD | 0.00 USD | 1,930.00 USD | `-25.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.75` | 9,810,000.00 USD | 0.00 USD | 235.34 USD | `-25.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.05` | 9,810,000.00 USD | 0.00 USD | 20,410.00 USD | `-25.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.55` | 9,790,000.00 USD | 0.00 USD | 19,560.00 USD | `-24.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.65` | 9,770,000.00 USD | 0.00 USD | 14,530.00 USD | `-24.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.95` | 9,750,000.00 USD | 0.00 USD | 66,160.00 USD | `-24.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.05` | 9,690,000.00 USD | 0.00 USD | 7,970.00 USD | `-24.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.35` | 9,680,000.00 USD | 0.00 USD | 733.50 USD | `-23.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.45` | 9,680,000.00 USD | 0.00 USD | 139.56 USD | `-23.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.05` | 9,680,000.00 USD | 0.00 USD | 510.95 USD | `-23.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.25` | 9,680,000.00 USD | 0.00 USD | 621.47 USD | `-22.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.35` | 9,680,000.00 USD | 0.00 USD | 1,660.00 USD | `-22.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.45` | 9,680,000.00 USD | 0.00 USD | 10,730.00 USD | `-22.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.55` | 9,670,000.00 USD | 0.00 USD | 331.00 USD | `-22.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.75` | 9,670,000.00 USD | 0.00 USD | 28,050.00 USD | `-22.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.05` | 9,640,000.00 USD | 0.00 USD | 27,010.00 USD | `-22.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.35` | 9,610,000.00 USD | 0.00 USD | 153.71 USD | `-21.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.45` | 9,610,000.00 USD | 0.00 USD | 163.73 USD | `-21.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.75` | 9,610,000.00 USD | 0.00 USD | 2,220.00 USD | `-21.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.95` | 9,610,000.00 USD | 0.00 USD | 277.98 USD | `-21.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.05` | 9,610,000.00 USD | 0.00 USD | 8,680.00 USD | `-21.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.15` | 9,600,000.00 USD | 0.00 USD | 254.34 USD | `-21.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.25` | 9,600,000.00 USD | 0.00 USD | 486.47 USD | `-20.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.35` | 9,600,000.00 USD | 0.00 USD | 358.84 USD | `-20.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.55` | 9,600,000.00 USD | 0.00 USD | 4,340.00 USD | `-20.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.65` | 9,590,000.00 USD | 0.00 USD | 536.55 USD | `-20.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.75` | 9,590,000.00 USD | 0.00 USD | 251.74 USD | `-20.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.05` | 9,590,000.00 USD | 0.00 USD | 5,000.00 USD | `-20.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.35` | 9,590,000.00 USD | 0.00 USD | 5,690.00 USD | `-19.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.45` | 9,580,000.00 USD | 0.00 USD | 1,020.00 USD | `-19.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.55` | 9,580,000.00 USD | 0.00 USD | 242.73 USD | `-19.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.95` | 9,580,000.00 USD | 0.00 USD | 155.12 USD | `-19.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.05` | 9,580,000.00 USD | 0.00 USD | 60,010.00 USD | `-19.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.15` | 9,520,000.00 USD | 0.00 USD | 532.98 USD | `-18.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.55` | 9,520,000.00 USD | 0.00 USD | 18,590.00 USD | `-18.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.65` | 9,500,000.00 USD | 0.00 USD | 116.40 USD | `-18.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.05` | 9,500,000.00 USD | 0.00 USD | 5,300.00 USD | `-17.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.15` | 9,500,000.00 USD | 0.00 USD | 201.04 USD | `-17.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.25` | 9,500,000.00 USD | 0.00 USD | 2,140.00 USD | `-17.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.45` | 9,490,000.00 USD | 0.00 USD | 5,850.00 USD | `-17.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.65` | 9,490,000.00 USD | 0.00 USD | 238.95 USD | `-17.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.75` | 9,490,000.00 USD | 0.00 USD | 1,330.00 USD | `-17.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.85` | 9,490,000.00 USD | 0.00 USD | 289.06 USD | `-17.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.95` | 9,490,000.00 USD | 0.00 USD | 808.29 USD | `-17.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.05` | 9,480,000.00 USD | 0.00 USD | 40,970.00 USD | `-16.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.15` | 9,440,000.00 USD | 0.00 USD | 8,360.00 USD | `-16.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.35` | 9,440,000.00 USD | 0.00 USD | 359.97 USD | `-16.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.45` | 9,440,000.00 USD | 0.00 USD | 8,770.00 USD | `-16.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.55` | 9,430,000.00 USD | 0.00 USD | 1,280.00 USD | `-16.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.65` | 9,430,000.00 USD | 0.00 USD | 1,280.00 USD | `-16.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.75` | 9,420,000.00 USD | 0.00 USD | 22,780.00 USD | `-16.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.85` | 9,400,000.00 USD | 0.00 USD | 341.19 USD | `-16.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.05` | 9,400,000.00 USD | 0.00 USD | 1,620.00 USD | `-15.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.25` | 9,400,000.00 USD | 0.00 USD | 266.50 USD | `-15.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.45` | 9,400,000.00 USD | 0.00 USD | 6,260.00 USD | `-15.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.55` | 9,390,000.00 USD | 0.00 USD | 572.48 USD | `-15.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.65` | 9,390,000.00 USD | 0.00 USD | 952.86 USD | `-15.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.75` | 9,390,000.00 USD | 0.00 USD | 1,390.00 USD | `-15.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.85` | 9,390,000.00 USD | 0.00 USD | 818.50 USD | `-15.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.95` | 9,390,000.00 USD | 0.00 USD | 70,900.00 USD | `-14.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.05` | 9,320,000.00 USD | 0.00 USD | 6,750.00 USD | `-14.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.15` | 9,310,000.00 USD | 0.00 USD | 684.31 USD | `-14.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.25` | 9,310,000.00 USD | 0.00 USD | 486.92 USD | `-14.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.35` | 9,310,000.00 USD | 0.00 USD | 386.22 USD | `-14.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.45` | 9,310,000.00 USD | 0.00 USD | 1,870.00 USD | `-14.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.55` | 9,310,000.00 USD | 0.00 USD | 1,310.00 USD | `-14.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.65` | 9,310,000.00 USD | 0.00 USD | 267,390.00 USD | `-14.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.75` | 9,040,000.00 USD | 0.00 USD | 1,660.00 USD | `-14.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.85` | 9,040,000.00 USD | 0.00 USD | 3,270.00 USD | `-14.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.95` | 9,030,000.00 USD | 0.00 USD | 945.63 USD | `-13.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.05` | 9,030,000.00 USD | 0.00 USD | 6,040.00 USD | `-13.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.15` | 9,030,000.00 USD | 0.00 USD | 239.47 USD | `-13.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.25` | 9,030,000.00 USD | 0.00 USD | 18,330.00 USD | `-13.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.45` | 9,010,000.00 USD | 0.00 USD | 168.57 USD | `-13.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.55` | 9,010,000.00 USD | 0.00 USD | 421.09 USD | `-13.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.65` | 9,010,000.00 USD | 0.00 USD | 1,100.00 USD | `-13.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.75` | 9,010,000.00 USD | 0.00 USD | 1,320.00 USD | `-13.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.95` | 9,010,000.00 USD | 0.00 USD | 4,550.00 USD | `-12.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.05` | 9,000,000.00 USD | 0.00 USD | 40,720.00 USD | `-12.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.15` | 8,960,000.00 USD | 0.00 USD | 25,220.00 USD | `-12.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.25` | 8,940,000.00 USD | 0.00 USD | 2,690.00 USD | `-12.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.45` | 8,930,000.00 USD | 0.00 USD | 965.26 USD | `-12.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.55` | 8,930,000.00 USD | 0.00 USD | 169.95 USD | `-12.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.65` | 8,930,000.00 USD | 0.00 USD | 858.35 USD | `-12.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.75` | 8,930,000.00 USD | 0.00 USD | 306.80 USD | `-12.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.95` | 8,930,000.00 USD | 0.00 USD | 137.62 USD | `-11.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.05` | 8,930,000.00 USD | 0.00 USD | 239,080.00 USD | `-11.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.15` | 8,690,000.00 USD | 0.00 USD | 437.67 USD | `-11.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.25` | 8,690,000.00 USD | 0.00 USD | 1,320.00 USD | `-11.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.35` | 8,690,000.00 USD | 0.00 USD | 39,110.00 USD | `-11.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.45` | 8,650,000.00 USD | 0.00 USD | 120.48 USD | `-11.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.55` | 8,650,000.00 USD | 0.00 USD | 105.23 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.65` | 8,650,000.00 USD | 0.00 USD | 493,240.00 USD | `-11.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.75` | 8,160,000.00 USD | 0.00 USD | 1,410.00 USD | `-11.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.85` | 8,160,000.00 USD | 0.00 USD | 360.57 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.95` | 8,150,000.00 USD | 0.00 USD | 2,050.00 USD | `-10.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.05` | 8,150,000.00 USD | 0.00 USD | 10,910.00 USD | `-10.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.15` | 8,140,000.00 USD | 0.00 USD | 2,210.00 USD | `-10.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.25` | 8,140,000.00 USD | 0.00 USD | 163.88 USD | `-10.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.35` | 8,140,000.00 USD | 0.00 USD | 5,710.00 USD | `-10.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.45` | 8,130,000.00 USD | 0.00 USD | 2,790.00 USD | `-10.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.55` | 8,130,000.00 USD | 0.00 USD | 417.17 USD | `-10.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.65` | 8,130,000.00 USD | 0.00 USD | 220,550.00 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.75` | 7,910,000.00 USD | 0.00 USD | 3,060.00 USD | `-10.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.85` | 7,910,000.00 USD | 0.00 USD | 788.60 USD | `-9.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.95` | 7,910,000.00 USD | 0.00 USD | 132.16 USD | `-9.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.05` | 7,910,000.00 USD | 0.00 USD | 283,280.00 USD | `-9.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.15` | 7,620,000.00 USD | 0.00 USD | 23,550.00 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.25` | 7,600,000.00 USD | 0.00 USD | 8,200.00 USD | `-9.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.35` | 7,590,000.00 USD | 0.00 USD | 102.20 USD | `-9.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.45` | 7,590,000.00 USD | 0.00 USD | 730.21 USD | `-9.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.55` | 7,590,000.00 USD | 0.00 USD | 1,160.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.65` | 7,590,000.00 USD | 0.00 USD | 2,300.00 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.85` | 7,590,000.00 USD | 0.00 USD | 131.78 USD | `-8.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.95` | 7,590,000.00 USD | 0.00 USD | 1,410.00 USD | `-8.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.05` | 7,590,000.00 USD | 0.00 USD | 132,850.00 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.15` | 7,450,000.00 USD | 0.00 USD | 833.02 USD | `-8.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.25` | 7,450,000.00 USD | 0.00 USD | 1,870.00 USD | `-8.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.35` | 7,450,000.00 USD | 0.00 USD | 38,020.00 USD | `-8.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.45` | 7,410,000.00 USD | 0.00 USD | 867.69 USD | `-8.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.55` | 7,410,000.00 USD | 0.00 USD | 32,280.00 USD | `-8.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.65` | 7,380,000.00 USD | 0.00 USD | 27,220.00 USD | `-8.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.75` | 7,350,000.00 USD | 0.00 USD | 53,390.00 USD | `-7.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.85` | 7,300,000.00 USD | 0.00 USD | 91,430.00 USD | `-7.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.95` | 7,210,000.00 USD | 0.00 USD | 141.43 USD | `-7.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.05` | 7,210,000.00 USD | 0.00 USD | 12,930.00 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.15` | 7,190,000.00 USD | 0.00 USD | 6,470.00 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.25` | 7,190,000.00 USD | 0.00 USD | 1,340.00 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.35` | 7,190,000.00 USD | 0.00 USD | 4,220.00 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.45` | 7,180,000.00 USD | 0.00 USD | 5,280.00 USD | `-7.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.55` | 7,180,000.00 USD | 0.00 USD | 348.35 USD | `-7.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.65` | 7,180,000.00 USD | 0.00 USD | 192.75 USD | `-7.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.75` | 7,180,000.00 USD | 0.00 USD | 105.01 USD | `-6.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.85` | 7,180,000.00 USD | 0.00 USD | 17,800.00 USD | `-6.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.95` | 7,160,000.00 USD | 0.00 USD | 87,020.00 USD | `-6.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.05` | 7,070,000.00 USD | 0.00 USD | 2,350,000.00 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.15` | 4,720,000.00 USD | 0.00 USD | 1,130.00 USD | `-6.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.25` | 4,720,000.00 USD | 0.00 USD | 12,170.00 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.35` | 4,710,000.00 USD | 0.00 USD | 338.81 USD | `-6.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.45` | 4,710,000.00 USD | 0.00 USD | 5,010.00 USD | `-6.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.55` | 4,700,000.00 USD | 0.00 USD | 12,520.00 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.65` | 4,690,000.00 USD | 0.00 USD | 75,820.00 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.75` | 4,610,000.00 USD | 0.00 USD | 4,980.00 USD | `-5.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.85` | 4,610,000.00 USD | 0.00 USD | 6,580.00 USD | `-5.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.95` | 4,600,000.00 USD | 0.00 USD | 7,300.00 USD | `-5.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.05` | 4,590,000.00 USD | 0.00 USD | 626,620.00 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.15` | 3,970,000.00 USD | 0.00 USD | 1,120.00 USD | `-5.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.25` | 3,970,000.00 USD | 0.00 USD | 1,660.00 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.35` | 3,970,000.00 USD | 0.00 USD | 16,980.00 USD | `-5.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.45` | 3,950,000.00 USD | 0.00 USD | 920.90 USD | `-5.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.55` | 3,950,000.00 USD | 0.00 USD | 20,520.00 USD | `-5.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.65` | 3,930,000.00 USD | 0.00 USD | 37,810.00 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.75` | 3,890,000.00 USD | 0.00 USD | 21,870.00 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.85` | 3,870,000.00 USD | 0.00 USD | 41,980.00 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.95` | 3,830,000.00 USD | 0.00 USD | 1,040,000.00 USD | `-4.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.05` | 2,780,000.00 USD | 0.00 USD | 268,660.00 USD | `-4.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.15` | 2,510,000.00 USD | 0.00 USD | 49,850.00 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.25` | 2,460,000.00 USD | 0.00 USD | 6,810.00 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.35` | 2,460,000.00 USD | 0.00 USD | 20,880.00 USD | `-4.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.45` | 2,440,000.00 USD | 0.00 USD | 132.20 USD | `-4.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.55` | 2,440,000.00 USD | 0.00 USD | 937,650.00 USD | `-3.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.65` | 1,500,000.00 USD | 0.00 USD | 59,380.00 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.75` | 1,440,000.00 USD | 0.00 USD | 7,590.00 USD | `-3.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.85` | 1,430,000.00 USD | 0.00 USD | 32,380.00 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.95` | 1,400,000.00 USD | 0.00 USD | 14,800.00 USD | `-3.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.05` | 1,380,000.00 USD | 0.00 USD | 70,600.00 USD | `-3.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.15` | 1,310,000.00 USD | 0.00 USD | 135,720.00 USD | `-3.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.25` | 1,180,000.00 USD | 0.00 USD | 9,220.00 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.35` | 1,170,000.00 USD | 0.00 USD | 23,560.00 USD | `-3.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.45` | 1,150,000.00 USD | 0.00 USD | 7,970.00 USD | `-3.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.55` | 1,140,000.00 USD | 0.00 USD | 12,940.00 USD | `-2.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.65` | 1,120,000.00 USD | 0.00 USD | 3,290.00 USD | `-2.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.75` | 1,120,000.00 USD | 0.00 USD | 4,050.00 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.85` | 1,120,000.00 USD | 0.00 USD | 674.78 USD | `-2.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.95` | 1,120,000.00 USD | 0.00 USD | 454.72 USD | `-2.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.05` | 1,120,000.00 USD | 0.00 USD | 111,780.00 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.15` | 1,000,000.00 USD | 0.00 USD | 528.18 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.25` | 1,000,000.00 USD | 0.00 USD | 1,050.00 USD | `-2.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.35` | 1,000,000.00 USD | 0.00 USD | 6,530.00 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.45` | 996,120.00 USD | 0.00 USD | 69,890.00 USD | `-2.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.55` | 926,240.00 USD | 0.00 USD | 94,340.00 USD | `-1.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.65` | 831,890.00 USD | 0.00 USD | 25,000.00 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.75` | 806,890.00 USD | 0.00 USD | 32,630.00 USD | `-1.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.85` | 774,260.00 USD | 0.00 USD | 15,630.00 USD | `-1.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.95` | 758,630.00 USD | 0.00 USD | 8,370.00 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.05` | 750,260.00 USD | 0.00 USD | 184,930.00 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.15` | 565,340.00 USD | 0.00 USD | 65,810.00 USD | `-1.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.25` | 499,520.00 USD | 0.00 USD | 2,730.00 USD | `-1.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.35` | 496,800.00 USD | 0.00 USD | 11,350.00 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.45` | 485,440.00 USD | 0.00 USD | 80,520.00 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.55` | 404,930.00 USD | 0.00 USD | 159,990.00 USD | `-0.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.65` | 244,940.00 USD | 0.00 USD | 4,850.00 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.75` | 240,090.00 USD | 0.00 USD | 36,220.00 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.85` | 203,870.00 USD | 0.00 USD | 26,550.00 USD | `-0.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.95` | 177,320.00 USD | 0.00 USD | 32,220.00 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.05` | 145,110.00 USD | 0.00 USD | 31,080.00 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.15` | 114,020.00 USD | 0.00 USD | 34,750.00 USD | `-0.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.25` | 79,280.00 USD | 0.00 USD | 14,620.00 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.35` | 64,660.00 USD | 0.00 USD | 64,660.00 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.45` | 979,030.00 USD | 979,030.00 USD | 0.00 USD | `+0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.55` | 1,030,000.00 USD | 54,510.00 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.65` | 1,060,000.00 USD | 26,630.00 USD | 0.00 USD | `+0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.75` | 1,410,000.00 USD | 353,080.00 USD | 0.00 USD | `+0.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.85` | 1,420,000.00 USD | 8,290.00 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.95` | 1,420,000.00 USD | 731.97 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.05` | 1,420,000.00 USD | 379.47 USD | 0.00 USD | `+0.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.15` | 1,460,000.00 USD | 38,340.00 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.25` | 1,490,000.00 USD | 27,460.00 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.35` | 1,500,000.00 USD | 8,150.00 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.45` | 1,500,000.00 USD | 6,380.00 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.55` | 1,520,000.00 USD | 18,390.00 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.65` | 1,530,000.00 USD | 6,780.00 USD | 0.00 USD | `+1.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.75` | 1,530,000.00 USD | 4,770.00 USD | 0.00 USD | `+1.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.85` | 1,580,000.00 USD | 48,470.00 USD | 0.00 USD | `+1.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.95` | 1,580,000.00 USD | 1,770.00 USD | 0.00 USD | `+1.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,610,000.00 USD | 23,860.00 USD | 0.00 USD | `+1.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.15` | 1,610,000.00 USD | 215.93 USD | 0.00 USD | `+1.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.25` | 1,610,000.00 USD | 1,680.00 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.35` | 1,620,000.00 USD | 11,510.00 USD | 0.00 USD | `+2.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.45` | 1,640,000.00 USD | 24,200.00 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.55` | 1,780,000.00 USD | 139,510.00 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.65` | 1,820,000.00 USD | 37,650.00 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.75` | 1,880,000.00 USD | 59,410.00 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.85` | 1,890,000.00 USD | 6,460.00 USD | 0.00 USD | `+2.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.95` | 1,910,000.00 USD | 24,050.00 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,940,000.00 USD | 27,700.00 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.15` | 1,960,000.00 USD | 16,550.00 USD | 0.00 USD | `+2.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.25` | 1,960,000.00 USD | 6,940.00 USD | 0.00 USD | `+2.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.35` | 2,000,000.00 USD | 39,840.00 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.45` | 2,000,000.00 USD | 1,770.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.55` | 2,040,000.00 USD | 34,050.00 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.65` | 2,060,000.00 USD | 17,050.00 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.75` | 2,070,000.00 USD | 9,780.00 USD | 0.00 USD | `+3.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.85` | 2,070,000.00 USD | 3,680.00 USD | 0.00 USD | `+3.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.95` | 2,110,000.00 USD | 42,410.00 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 2,710,000.00 USD | 595,650.00 USD | 0.00 USD | `+3.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.15` | 2,720,000.00 USD | 12,360.00 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.25` | 2,720,000.00 USD | 5,030.00 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.35` | 2,730,000.00 USD | 1,250.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.45` | 2,740,000.00 USD | 12,940.00 USD | 0.00 USD | `+4.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.55` | 2,740,000.00 USD | 2,700.00 USD | 0.00 USD | `+4.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.65` | 2,760,000.00 USD | 22,990.00 USD | 0.00 USD | `+4.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.75` | 2,770,000.00 USD | 1,110.00 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.85` | 2,770,000.00 USD | 2,570.00 USD | 0.00 USD | `+4.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.95` | 2,770,000.00 USD | 2,490.00 USD | 0.00 USD | `+4.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.05` | 2,990,000.00 USD | 223,000.00 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.15` | 4,210,000.00 USD | 1,220,000.00 USD | 0.00 USD | `+4.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.25` | 4,220,000.00 USD | 8,940.00 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.35` | 4,230,000.00 USD | 3,850.00 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.45` | 4,230,000.00 USD | 1,450.00 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.55` | 4,240,000.00 USD | 10,050.00 USD | 0.00 USD | `+5.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.65` | 4,240,000.00 USD | 477.76 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.75` | 4,240,000.00 USD | 648.15 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.85` | 4,240,000.00 USD | 4,720.00 USD | 0.00 USD | `+5.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.95` | 4,240,000.00 USD | 1,080.00 USD | 0.00 USD | `+5.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 4,330,000.00 USD | 83,280.00 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.15` | 4,330,000.00 USD | 231.88 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.25` | 4,330,000.00 USD | 3,080.00 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.35` | 4,340,000.00 USD | 4,280.00 USD | 0.00 USD | `+6.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.45` | 4,340,000.00 USD | 7,280.00 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.55` | 4,510,000.00 USD | 168,820.00 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.65` | 4,780,000.00 USD | 268,070.00 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.75` | 4,780,000.00 USD | 1,280.00 USD | 0.00 USD | `+6.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.85` | 4,780,000.00 USD | 1,780.00 USD | 0.00 USD | `+6.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.95` | 4,790,000.00 USD | 4,280.00 USD | 0.00 USD | `+6.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 4,830,000.00 USD | 42,010.00 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 4,830,000.00 USD | 3,180.00 USD | 0.00 USD | `+7.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.25` | 4,900,000.00 USD | 64,080.00 USD | 0.00 USD | `+7.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.35` | 4,900,000.00 USD | 4,260.00 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.45` | 4,900,000.00 USD | 3,860.00 USD | 0.00 USD | `+7.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.55` | 4,930,000.00 USD | 20,580.00 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.65` | 4,940,000.00 USD | 17,250.00 USD | 0.00 USD | `+7.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.75` | 4,940,000.00 USD | 980.44 USD | 0.00 USD | `+7.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.85` | 5,170,000.00 USD | 227,080.00 USD | 0.00 USD | `+7.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.95` | 5,230,000.00 USD | 62,400.00 USD | 0.00 USD | `+7.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.05` | 5,250,000.00 USD | 13,180.00 USD | 0.00 USD | `+7.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.15` | 5,250,000.00 USD | 1,180.00 USD | 0.00 USD | `+8.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.25` | 5,250,000.00 USD | 519.17 USD | 0.00 USD | `+8.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.35` | 5,250,000.00 USD | 323.49 USD | 0.00 USD | `+8.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.45` | 5,340,000.00 USD | 95,950.00 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.55` | 5,370,000.00 USD | 28,290.00 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.65` | 5,370,000.00 USD | 680.23 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.75` | 5,380,000.00 USD | 2,150.00 USD | 0.00 USD | `+8.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.85` | 5,380,000.00 USD | 5,900.00 USD | 0.00 USD | `+8.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.95` | 5,410,000.00 USD | 25,930.00 USD | 0.00 USD | `+8.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.05` | 5,530,000.00 USD | 126,860.00 USD | 0.00 USD | `+8.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.15` | 5,560,000.00 USD | 28,780.00 USD | 0.00 USD | `+9.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.25` | 5,560,000.00 USD | 1,010.00 USD | 0.00 USD | `+9.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.35` | 5,560,000.00 USD | 1,090.00 USD | 0.00 USD | `+9.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.45` | 5,570,000.00 USD | 266.79 USD | 0.00 USD | `+9.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.55` | 5,570,000.00 USD | 3,620.00 USD | 0.00 USD | `+9.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.65` | 5,570,000.00 USD | 1,970.00 USD | 0.00 USD | `+9.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.75` | 5,570,000.00 USD | 549.90 USD | 0.00 USD | `+9.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.85` | 5,580,000.00 USD | 10,600.00 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.95` | 5,590,000.00 USD | 3,620.00 USD | 0.00 USD | `+9.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.05` | 5,610,000.00 USD | 19,780.00 USD | 0.00 USD | `+10.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.15` | 5,610,000.00 USD | 7,080.00 USD | 0.00 USD | `+10.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.25` | 5,610,000.00 USD | 758.62 USD | 0.00 USD | `+10.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.35` | 5,620,000.00 USD | 7,980.00 USD | 0.00 USD | `+10.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.45` | 5,650,000.00 USD | 26,170.00 USD | 0.00 USD | `+10.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.55` | 5,650,000.00 USD | 7,640.00 USD | 0.00 USD | `+10.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.65` | 5,660,000.00 USD | 355.14 USD | 0.00 USD | `+10.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.75` | 5,770,000.00 USD | 110,390.00 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.85` | 5,770,000.00 USD | 1,730.00 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.95` | 5,770,000.00 USD | 2,990.00 USD | 0.00 USD | `+10.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.05` | 5,910,000.00 USD | 142,930.00 USD | 0.00 USD | `+11.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.15` | 5,910,000.00 USD | 109.29 USD | 0.00 USD | `+11.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.25` | 5,930,000.00 USD | 20,190.00 USD | 0.00 USD | `+11.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.35` | 5,930,000.00 USD | 698.85 USD | 0.00 USD | `+11.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.45` | 5,940,000.00 USD | 8,930.00 USD | 0.00 USD | `+11.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.55` | 6,000,000.00 USD | 52,130.00 USD | 0.00 USD | `+11.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.65` | 6,060,000.00 USD | 65,380.00 USD | 0.00 USD | `+11.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.75` | 6,060,000.00 USD | 536.60 USD | 0.00 USD | `+11.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.85` | 6,070,000.00 USD | 11,350.00 USD | 0.00 USD | `+11.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.95` | 6,080,000.00 USD | 9,120.00 USD | 0.00 USD | `+11.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 6,170,000.00 USD | 87,120.00 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.15` | 6,240,000.00 USD | 68,190.00 USD | 0.00 USD | `+12.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.35` | 6,240,000.00 USD | 7,280.00 USD | 0.00 USD | `+12.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.45` | 6,250,000.00 USD | 2,580.00 USD | 0.00 USD | `+12.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.55` | 6,250,000.00 USD | 5,430.00 USD | 0.00 USD | `+12.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.65` | 6,250,000.00 USD | 666.02 USD | 0.00 USD | `+12.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.75` | 6,250,000.00 USD | 1,010.00 USD | 0.00 USD | `+12.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.85` | 6,260,000.00 USD | 1,430.00 USD | 0.00 USD | `+12.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.95` | 6,300,000.00 USD | 40,920.00 USD | 0.00 USD | `+13.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 6,370,000.00 USD | 73,460.00 USD | 0.00 USD | `+13.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.15` | 6,380,000.00 USD | 7,660.00 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.25` | 10,320,000.00 USD | 3,950,000.00 USD | 0.00 USD | `+13.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.35` | 10,350,000.00 USD | 31,070.00 USD | 0.00 USD | `+13.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.45` | 10,360,000.00 USD | 5,880.00 USD | 0.00 USD | `+13.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.55` | 10,360,000.00 USD | 1,070.00 USD | 0.00 USD | `+13.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.65` | 10,370,000.00 USD | 5,040.00 USD | 0.00 USD | `+13.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.75` | 10,370,000.00 USD | 1,370.00 USD | 0.00 USD | `+13.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.85` | 10,370,000.00 USD | 1,420.00 USD | 0.00 USD | `+13.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.95` | 10,370,000.00 USD | 357.34 USD | 0.00 USD | `+14.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.05` | 10,890,000.00 USD | 522,250.00 USD | 0.00 USD | `+14.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.15` | 10,900,000.00 USD | 4,150.00 USD | 0.00 USD | `+14.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.25` | 10,900,000.00 USD | 102.53 USD | 0.00 USD | `+14.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.35` | 10,900,000.00 USD | 1,610.00 USD | 0.00 USD | `+14.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.45` | 10,900,000.00 USD | 1,580.00 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.55` | 10,910,000.00 USD | 10,280.00 USD | 0.00 USD | `+14.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.65` | 10,910,000.00 USD | 3,030.00 USD | 0.00 USD | `+14.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.85` | 10,930,000.00 USD | 17,520.00 USD | 0.00 USD | `+15.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.95` | 11,000,000.00 USD | 74,620.00 USD | 0.00 USD | `+15.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 11,070,000.00 USD | 64,770.00 USD | 0.00 USD | `+15.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.15` | 11,070,000.00 USD | 1,300.00 USD | 0.00 USD | `+15.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.25` | 11,080,000.00 USD | 5,910.00 USD | 0.00 USD | `+15.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.45` | 11,080,000.00 USD | 585.11 USD | 0.00 USD | `+15.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.55` | 11,080,000.00 USD | 852.24 USD | 0.00 USD | `+15.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.65` | 11,100,000.00 USD | 22,910.00 USD | 0.00 USD | `+15.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.75` | 11,100,000.00 USD | 2,420.00 USD | 0.00 USD | `+15.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.85` | 11,110,000.00 USD | 2,100.00 USD | 0.00 USD | `+16.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.05` | 11,120,000.00 USD | 14,400.00 USD | 0.00 USD | `+16.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.15` | 11,170,000.00 USD | 49,680.00 USD | 0.00 USD | `+16.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.25` | 11,180,000.00 USD | 5,260.00 USD | 0.00 USD | `+16.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.35` | 11,180,000.00 USD | 4,920.00 USD | 0.00 USD | `+16.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.45` | 11,180,000.00 USD | 953.58 USD | 0.00 USD | `+16.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.55` | 11,220,000.00 USD | 36,280.00 USD | 0.00 USD | `+16.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.65` | 11,220,000.00 USD | 6,710.00 USD | 0.00 USD | `+16.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.85` | 11,220,000.00 USD | 586.82 USD | 0.00 USD | `+17.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.05` | 11,310,000.00 USD | 81,560.00 USD | 0.00 USD | `+17.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.25` | 11,310,000.00 USD | 710.08 USD | 0.00 USD | `+17.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.35` | 11,340,000.00 USD | 35,250.00 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.45` | 11,340,000.00 USD | 655.74 USD | 0.00 USD | `+17.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.55` | 11,350,000.00 USD | 4,470.00 USD | 0.00 USD | `+17.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.65` | 11,350,000.00 USD | 230.71 USD | 0.00 USD | `+17.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.75` | 11,350,000.00 USD | 257.07 USD | 0.00 USD | `+18.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.85` | 11,350,000.00 USD | 4,540.00 USD | 0.00 USD | `+18.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.05` | 11,350,000.00 USD | 1,970.00 USD | 0.00 USD | `+18.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.15` | 11,350,000.00 USD | 122.14 USD | 0.00 USD | `+18.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.25` | 11,360,000.00 USD | 907.14 USD | 0.00 USD | `+18.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.35` | 11,360,000.00 USD | 740.99 USD | 0.00 USD | `+18.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.45` | 11,360,000.00 USD | 343.35 USD | 0.00 USD | `+18.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.55` | 11,360,000.00 USD | 1,640.00 USD | 0.00 USD | `+18.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.65` | 11,360,000.00 USD | 105.48 USD | 0.00 USD | `+18.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.75` | 11,360,000.00 USD | 1,010.00 USD | 0.00 USD | `+19.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.95` | 11,360,000.00 USD | 2,520.00 USD | 0.00 USD | `+19.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.05` | 11,440,000.00 USD | 81,890.00 USD | 0.00 USD | `+19.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.35` | 11,440,000.00 USD | 309.14 USD | 0.00 USD | `+19.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.45` | 11,440,000.00 USD | 346.35 USD | 0.00 USD | `+19.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.55` | 11,450,000.00 USD | 4,900.00 USD | 0.00 USD | `+19.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.75` | 11,450,000.00 USD | 121.54 USD | 0.00 USD | `+20.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.85` | 11,450,000.00 USD | 579.25 USD | 0.00 USD | `+20.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.05` | 11,460,000.00 USD | 6,400.00 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.15` | 11,460,000.00 USD | 1,740.00 USD | 0.00 USD | `+20.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.25` | 11,460,000.00 USD | 1,920.00 USD | 0.00 USD | `+20.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.45` | 11,460,000.00 USD | 2,870.00 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.55` | 11,480,000.00 USD | 14,010.00 USD | 0.00 USD | `+20.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.65` | 11,480,000.00 USD | 6,000.00 USD | 0.00 USD | `+21.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.75` | 11,490,000.00 USD | 3,580.00 USD | 0.00 USD | `+21.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.85` | 11,490,000.00 USD | 234.87 USD | 0.00 USD | `+21.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.95` | 11,500,000.00 USD | 12,860.00 USD | 0.00 USD | `+21.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.05` | 11,500,000.00 USD | 4,200.00 USD | 0.00 USD | `+21.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.15` | 11,500,000.00 USD | 584.58 USD | 0.00 USD | `+21.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.25` | 11,510,000.00 USD | 1,740.00 USD | 0.00 USD | `+21.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.35` | 11,510,000.00 USD | 2,330.00 USD | 0.00 USD | `+21.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.45` | 11,630,000.00 USD | 118,690.00 USD | 0.00 USD | `+21.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.65` | 11,730,000.00 USD | 106,330.00 USD | 0.00 USD | `+22.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.75` | 11,740,000.00 USD | 5,920.00 USD | 0.00 USD | `+22.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.85` | 11,790,000.00 USD | 55,580.00 USD | 0.00 USD | `+22.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.05` | 11,860,000.00 USD | 69,220.00 USD | 0.00 USD | `+22.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.15` | 11,870,000.00 USD | 3,980.00 USD | 0.00 USD | `+22.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.25` | 11,870,000.00 USD | 4,460.00 USD | 0.00 USD | `+22.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.35` | 11,870,000.00 USD | 127.82 USD | 0.00 USD | `+22.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.45` | 11,870,000.00 USD | 707.15 USD | 0.00 USD | `+22.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.55` | 11,870,000.00 USD | 1,260.00 USD | 0.00 USD | `+22.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.65` | 11,880,000.00 USD | 2,970.00 USD | 0.00 USD | `+23.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.75` | 11,880,000.00 USD | 403.75 USD | 0.00 USD | `+23.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.85` | 11,890,000.00 USD | 15,940.00 USD | 0.00 USD | `+23.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.95` | 11,940,000.00 USD | 42,290.00 USD | 0.00 USD | `+23.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.05` | 11,990,000.00 USD | 52,430.00 USD | 0.00 USD | `+23.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.15` | 12,000,000.00 USD | 15,130.00 USD | 0.00 USD | `+23.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.25` | 12,010,000.00 USD | 1,850.00 USD | 0.00 USD | `+23.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.35` | 12,010,000.00 USD | 4,150.00 USD | 0.00 USD | `+23.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.45` | 12,010,000.00 USD | 310.57 USD | 0.00 USD | `+23.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.65` | 12,010,000.00 USD | 615.00 USD | 0.00 USD | `+24.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.75` | 12,140,000.00 USD | 125,500.00 USD | 0.00 USD | `+24.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.85` | 12,170,000.00 USD | 37,630.00 USD | 0.00 USD | `+24.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.95` | 12,170,000.00 USD | 458.21 USD | 0.00 USD | `+24.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.05` | 12,360,000.00 USD | 184,950.00 USD | 0.00 USD | `+24.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.15` | 12,360,000.00 USD | 414.52 USD | 0.00 USD | `+24.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.25` | 12,360,000.00 USD | 3,210.00 USD | 0.00 USD | `+24.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.35` | 12,370,000.00 USD | 7,850.00 USD | 0.00 USD | `+24.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.45` | 12,380,000.00 USD | 13,560.00 USD | 0.00 USD | `+24.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.55` | 12,390,000.00 USD | 904.13 USD | 0.00 USD | `+25.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.65` | 12,390,000.00 USD | 191.83 USD | 0.00 USD | `+25.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.85` | 12,390,000.00 USD | 663.47 USD | 0.00 USD | `+25.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.05` | 12,410,000.00 USD | 20,960.00 USD | 0.00 USD | `+25.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.15` | 12,410,000.00 USD | 122.36 USD | 0.00 USD | `+25.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.25` | 12,420,000.00 USD | 11,200.00 USD | 0.00 USD | `+25.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.45` | 12,430,000.00 USD | 11,570.00 USD | 0.00 USD | `+25.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.55` | 12,440,000.00 USD | 7,860.00 USD | 0.00 USD | `+26.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.65` | 12,440,000.00 USD | 4,430.00 USD | 0.00 USD | `+26.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.75` | 12,440,000.00 USD | 2,450.00 USD | 0.00 USD | `+26.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.85` | 12,450,000.00 USD | 1,480.00 USD | 0.00 USD | `+26.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.95` | 12,530,000.00 USD | 80,260.00 USD | 0.00 USD | `+26.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.05` | 12,720,000.00 USD | 192,930.00 USD | 0.00 USD | `+26.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.15` | 12,720,000.00 USD | 1,000.00 USD | 0.00 USD | `+26.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.25` | 12,950,000.00 USD | 234,430.00 USD | 0.00 USD | `+26.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.35` | 13,010,000.00 USD | 52,330.00 USD | 0.00 USD | `+26.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.45` | 13,010,000.00 USD | 3,060.00 USD | 0.00 USD | `+27.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.55` | 13,020,000.00 USD | 7,020.00 USD | 0.00 USD | `+27.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.65` | 13,030,000.00 USD | 11,000.00 USD | 0.00 USD | `+27.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.75` | 13,030,000.00 USD | 368.25 USD | 0.00 USD | `+27.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.85` | 13,030,000.00 USD | 3,850.00 USD | 0.00 USD | `+27.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.95` | 13,050,000.00 USD | 16,430.00 USD | 0.00 USD | `+27.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.05` | 14,060,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+27.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.15` | 14,060,000.00 USD | 252.46 USD | 0.00 USD | `+27.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.25` | 14,070,000.00 USD | 7,710.00 USD | 0.00 USD | `+27.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.35` | 14,070,000.00 USD | 6,790.00 USD | 0.00 USD | `+27.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.45` | 14,080,000.00 USD | 2,670.00 USD | 0.00 USD | `+28.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.55` | 14,080,000.00 USD | 632.58 USD | 0.00 USD | `+28.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.65` | 14,090,000.00 USD | 11,550.00 USD | 0.00 USD | `+28.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.85` | 14,090,000.00 USD | 5,530.00 USD | 0.00 USD | `+28.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.95` | 14,110,000.00 USD | 18,470.00 USD | 0.00 USD | `+28.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.05` | 14,130,000.00 USD | 16,360.00 USD | 0.00 USD | `+28.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.15` | 14,130,000.00 USD | 1,320.00 USD | 0.00 USD | `+28.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.25` | 14,130,000.00 USD | 151.59 USD | 0.00 USD | `+28.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.35` | 14,130,000.00 USD | 4,240.00 USD | 0.00 USD | `+29.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.45` | 14,140,000.00 USD | 1,370.00 USD | 0.00 USD | `+29.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.55` | 14,140,000.00 USD | 7,330.00 USD | 0.00 USD | `+29.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.65` | 14,150,000.00 USD | 6,610.00 USD | 0.00 USD | `+29.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.85` | 14,150,000.00 USD | 596.78 USD | 0.00 USD | `+29.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.95` | 14,160,000.00 USD | 10,310.00 USD | 0.00 USD | `+29.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.05` | 14,710,000.00 USD | 554,250.00 USD | 0.00 USD | `+29.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.15` | 14,720,000.00 USD | 603.22 USD | 0.00 USD | `+29.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.25` | 14,720,000.00 USD | 311.87 USD | 0.00 USD | `+29.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.35` | 14,720,000.00 USD | 6,780.00 USD | 0.00 USD | `+30.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.45` | 14,720,000.00 USD | 993.56 USD | 0.00 USD | `+30.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.55` | 14,740,000.00 USD | 16,280.00 USD | 0.00 USD | `+30.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.85` | 14,740,000.00 USD | 471.94 USD | 0.00 USD | `+30.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.95` | 14,740,000.00 USD | 209.08 USD | 0.00 USD | `+30.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.05` | 14,890,000.00 USD | 151,060.00 USD | 0.00 USD | `+30.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.15` | 14,890,000.00 USD | 189.23 USD | 0.00 USD | `+30.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.45` | 14,890,000.00 USD | 187.15 USD | 0.00 USD | `+31.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.65` | 14,900,000.00 USD | 3,550.00 USD | 0.00 USD | `+31.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.75` | 14,900,000.00 USD | 7,460.00 USD | 0.00 USD | `+31.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.05` | 15,090,000.00 USD | 190,580.00 USD | 0.00 USD | `+31.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.35` | 15,090,000.00 USD | 534.87 USD | 0.00 USD | `+32.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.45` | 15,100,000.00 USD | 4,620.00 USD | 0.00 USD | `+32.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.65` | 15,100,000.00 USD | 5,000.00 USD | 0.00 USD | `+32.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.75` | 15,100,000.00 USD | 362.81 USD | 0.00 USD | `+32.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.85` | 15,160,000.00 USD | 60,770.00 USD | 0.00 USD | `+32.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.95` | 15,170,000.00 USD | 482.37 USD | 0.00 USD | `+32.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.05` | 15,170,000.00 USD | 3,700.00 USD | 0.00 USD | `+32.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.15` | 15,170,000.00 USD | 3,010.00 USD | 0.00 USD | `+32.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.25` | 15,170,000.00 USD | 191.09 USD | 0.00 USD | `+33.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.65` | 15,210,000.00 USD | 41,130.00 USD | 0.00 USD | `+33.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.95` | 15,230,000.00 USD | 12,600.00 USD | 0.00 USD | `+33.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.05` | 15,280,000.00 USD | 50,720.00 USD | 0.00 USD | `+33.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.15` | 15,280,000.00 USD | 229.89 USD | 0.00 USD | `+33.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.25` | 15,290,000.00 USD | 15,330.00 USD | 0.00 USD | `+34.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.45` | 15,290,000.00 USD | 401.29 USD | 0.00 USD | `+34.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.55` | 15,290,000.00 USD | 1,320.00 USD | 0.00 USD | `+34.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.65` | 15,290,000.00 USD | 152.99 USD | 0.00 USD | `+34.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.75` | 15,290,000.00 USD | 153.10 USD | 0.00 USD | `+34.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.85` | 15,290,000.00 USD | 116.87 USD | 0.00 USD | `+34.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.05` | 15,350,000.00 USD | 51,520.00 USD | 0.00 USD | `+34.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.35` | 15,350,000.00 USD | 1,760.00 USD | 0.00 USD | `+35.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.45` | 15,350,000.00 USD | 4,090.00 USD | 0.00 USD | `+35.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.65` | 15,350,000.00 USD | 192.06 USD | 0.00 USD | `+35.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.75` | 15,360,000.00 USD | 3,150.00 USD | 0.00 USD | `+35.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.85` | 15,360,000.00 USD | 2,620.00 USD | 0.00 USD | `+35.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.95` | 15,370,000.00 USD | 10,140.00 USD | 0.00 USD | `+35.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.05` | 15,370,000.00 USD | 6,000.00 USD | 0.00 USD | `+35.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.15` | 15,380,000.00 USD | 5,950.00 USD | 0.00 USD | `+36.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.25` | 15,390,000.00 USD | 8,820.00 USD | 0.00 USD | `+36.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.45` | 15,390,000.00 USD | 135.39 USD | 0.00 USD | `+36.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.65` | 15,550,000.00 USD | 160,920.00 USD | 0.00 USD | `+36.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.75` | 15,550,000.00 USD | 144.93 USD | 0.00 USD | `+36.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.05` | 15,560,000.00 USD | 12,390.00 USD | 0.00 USD | `+36.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.65` | 15,560,000.00 USD | 397.95 USD | 0.00 USD | `+37.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.85` | 15,570,000.00 USD | 9,310.00 USD | 0.00 USD | `+37.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.95` | 15,580,000.00 USD | 3,910.00 USD | 0.00 USD | `+37.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.05` | 15,580,000.00 USD | 267.43 USD | 0.00 USD | `+38.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.15` | 15,580,000.00 USD | 509.96 USD | 0.00 USD | `+38.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.25` | 15,580,000.00 USD | 191.88 USD | 0.00 USD | `+38.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.35` | 15,580,000.00 USD | 237.36 USD | 0.00 USD | `+38.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.55` | 15,580,000.00 USD | 1,210.00 USD | 0.00 USD | `+38.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.65` | 15,580,000.00 USD | 192.46 USD | 0.00 USD | `+38.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.75` | 15,580,000.00 USD | 112.35 USD | 0.00 USD | `+38.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.95` | 15,580,000.00 USD | 4,620.00 USD | 0.00 USD | `+38.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.05` | 15,640,000.00 USD | 54,080.00 USD | 0.00 USD | `+39.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.25` | 15,640,000.00 USD | 331.60 USD | 0.00 USD | `+39.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.55` | 15,910,000.00 USD | 270,270.00 USD | 0.00 USD | `+39.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.85` | 15,910,000.00 USD | 647.28 USD | 0.00 USD | `+39.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.05` | 16,020,000.00 USD | 116,220.00 USD | 0.00 USD | `+40.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.55` | 16,030,000.00 USD | 7,560.00 USD | 0.00 USD | `+40.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.05` | 16,030,000.00 USD | 1,890.00 USD | 0.00 USD | `+41.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.35` | 16,030,000.00 USD | 192.25 USD | 0.00 USD | `+41.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.45` | 16,030,000.00 USD | 465.29 USD | 0.00 USD | `+41.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.55` | 16,040,000.00 USD | 389.17 USD | 0.00 USD | `+41.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.85` | 16,040,000.00 USD | 826.57 USD | 0.00 USD | `+41.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.05` | 16,040,000.00 USD | 231.61 USD | 0.00 USD | `+42.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.25` | 16,040,000.00 USD | 2,910.00 USD | 0.00 USD | `+42.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.35` | 16,040,000.00 USD | 3,920.00 USD | 0.00 USD | `+42.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.65` | 16,070,000.00 USD | 26,260.00 USD | 0.00 USD | `+42.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.75` | 16,070,000.00 USD | 133.62 USD | 0.00 USD | `+42.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.05` | 16,080,000.00 USD | 14,550.00 USD | 0.00 USD | `+43.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.45` | 16,080,000.00 USD | 692.25 USD | 0.00 USD | `+43.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.65` | 16,090,000.00 USD | 447.84 USD | 0.00 USD | `+43.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.85` | 22,830,000.00 USD | 6,740,000.00 USD | 0.00 USD | `+44.04%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `138.95` | 22,830,000.00 USD | 826.75 USD | 0.00 USD | `+44.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.05` | 25,020,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+44.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.55` | 25,030,000.00 USD | 5,920.00 USD | 0.00 USD | `+44.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.05` | 25,140,000.00 USD | 110,660.00 USD | 0.00 USD | `+45.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.45` | 25,150,000.00 USD | 12,120.00 USD | 0.00 USD | `+45.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.55` | 25,250,000.00 USD | 98,400.00 USD | 0.00 USD | `+45.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.75` | 25,250,000.00 USD | 990.88 USD | 0.00 USD | `+46.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.05` | 25,260,000.00 USD | 12,080.00 USD | 0.00 USD | `+46.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.25` | 25,270,000.00 USD | 6,190.00 USD | 0.00 USD | `+46.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.65` | 25,270,000.00 USD | 796.07 USD | 0.00 USD | `+46.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.05` | 25,270,000.00 USD | 826.73 USD | 0.00 USD | `+47.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.85` | 25,270,000.00 USD | 278.56 USD | 0.00 USD | `+48.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.95` | 25,600,000.00 USD | 329,100.00 USD | 0.00 USD | `+48.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.05` | 25,670,000.00 USD | 72,610.00 USD | 0.00 USD | `+48.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.15` | 25,690,000.00 USD | 16,980.00 USD | 0.00 USD | `+48.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.35` | 25,690,000.00 USD | 528.96 USD | 0.00 USD | `+48.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.05` | 25,690,000.00 USD | 6,330.00 USD | 0.00 USD | `+49.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.25` | 25,700,000.00 USD | 415.44 USD | 0.00 USD | `+49.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.35` | 25,980,000.00 USD | 282,520.00 USD | 0.00 USD | `+49.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.55` | 25,980,000.00 USD | 7,260.00 USD | 0.00 USD | `+49.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.75` | 25,990,000.00 USD | 791.78 USD | 0.00 USD | `+50.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.05` | 26,020,000.00 USD | 36,040.00 USD | 0.00 USD | `+50.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.25` | 26,020,000.00 USD | 209.16 USD | 0.00 USD | `+50.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.55` | 26,020,000.00 USD | 698.64 USD | 0.00 USD | `+50.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.05` | 26,210,000.00 USD | 190,100.00 USD | 0.00 USD | `+51.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.15` | 26,220,000.00 USD | 3,300.00 USD | 0.00 USD | `+51.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.25` | 26,220,000.00 USD | 1,020.00 USD | 0.00 USD | `+51.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.95` | 26,220,000.00 USD | 1,500.00 USD | 0.00 USD | `+52.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.05` | 26,260,000.00 USD | 37,700.00 USD | 0.00 USD | `+52.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.45` | 26,260,000.00 USD | 844.89 USD | 0.00 USD | `+52.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.85` | 26,260,000.00 USD | 4,610.00 USD | 0.00 USD | `+53.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.95` | 26,260,000.00 USD | 3,100.00 USD | 0.00 USD | `+53.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.05` | 27,600,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+53.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.45` | 27,600,000.00 USD | 1,370.00 USD | 0.00 USD | `+54.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.55` | 27,610,000.00 USD | 4,760.00 USD | 0.00 USD | `+54.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.05` | 27,610,000.00 USD | 549.99 USD | 0.00 USD | `+54.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.15` | 28,120,000.00 USD | 510,120.00 USD | 0.00 USD | `+54.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.05` | 28,370,000.00 USD | 249,190.00 USD | 0.00 USD | `+55.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.25` | 28,370,000.00 USD | 1,200.00 USD | 0.00 USD | `+55.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.35` | 28,370,000.00 USD | 178.92 USD | 0.00 USD | `+55.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.55` | 28,370,000.00 USD | 1,360.00 USD | 0.00 USD | `+56.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.05` | 28,390,000.00 USD | 14,430.00 USD | 0.00 USD | `+56.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.25` | 28,390,000.00 USD | 2,000.00 USD | 0.00 USD | `+56.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.45` | 28,390,000.00 USD | 411.94 USD | 0.00 USD | `+57.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.15` | 28,400,000.00 USD | 10,620.00 USD | 0.00 USD | `+58.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.65` | 28,400,000.00 USD | 1,020.00 USD | 0.00 USD | `+59.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.55` | 28,410,000.00 USD | 12,000.00 USD | 0.00 USD | `+60.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.85` | 28,410,000.00 USD | 113.04 USD | 0.00 USD | `+60.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.05` | 28,410,000.00 USD | 1,830.00 USD | 0.00 USD | `+60.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.35` | 28,440,000.00 USD | 22,680.00 USD | 0.00 USD | `+61.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.85` | 28,450,000.00 USD | 16,970.00 USD | 0.00 USD | `+61.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.05` | 28,460,000.00 USD | 2,230.00 USD | 0.00 USD | `+61.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.05` | 28,460,000.00 USD | 6,640.00 USD | 0.00 USD | `+63.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.75` | 28,480,000.00 USD | 15,880.00 USD | 0.00 USD | `+64.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.15` | 28,480,000.00 USD | 692.30 USD | 0.00 USD | `+65.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.95` | 28,490,000.00 USD | 5,620.00 USD | 0.00 USD | `+65.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.05` | 28,570,000.00 USD | 89,040.00 USD | 0.00 USD | `+66.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.05` | 28,570,000.00 USD | 281.84 USD | 0.00 USD | `+67.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.05` | 28,580,000.00 USD | 4,080.00 USD | 0.00 USD | `+69.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.05` | 28,670,000.00 USD | 89,230.00 USD | 0.00 USD | `+71.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.45` | 28,670,000.00 USD | 823.94 USD | 0.00 USD | `+71.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.45` | 28,670,000.00 USD | 211.39 USD | 0.00 USD | `+72.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.95` | 28,670,000.00 USD | 307.19 USD | 0.00 USD | `+73.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.05` | 28,670,000.00 USD | 593.03 USD | 0.00 USD | `+73.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.75` | 28,670,000.00 USD | 1,440.00 USD | 0.00 USD | `+74.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.05` | 28,680,000.00 USD | 5,720.00 USD | 0.00 USD | `+74.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.55` | 28,680,000.00 USD | 495.09 USD | 0.00 USD | `+75.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.95` | 28,680,000.00 USD | 912.63 USD | 0.00 USD | `+76.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.05` | 28,720,000.00 USD | 43,480.00 USD | 0.00 USD | `+76.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.55` | 28,720,000.00 USD | 686.20 USD | 0.00 USD | `+77.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.05` | 28,760,000.00 USD | 35,280.00 USD | 0.00 USD | `+78.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.45` | 28,760,000.00 USD | 703.60 USD | 0.00 USD | `+78.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.05` | 28,760,000.00 USD | 3,160.00 USD | 0.00 USD | `+79.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `174.85` | 28,760,000.00 USD | 1,430.00 USD | 0.00 USD | `+81.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.05` | 28,820,000.00 USD | 52,520.00 USD | 0.00 USD | `+81.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.25` | 28,840,000.00 USD | 21,960.00 USD | 0.00 USD | `+81.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.85` | 28,840,000.00 USD | 1,450.00 USD | 0.00 USD | `+83.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.05` | 28,840,000.00 USD | 885.25 USD | 0.00 USD | `+83.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.55` | 28,840,000.00 USD | 2,990.00 USD | 0.00 USD | `+85.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.15` | 28,840,000.00 USD | 261.56 USD | 0.00 USD | `+85.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.05` | 28,920,000.00 USD | 80,290.00 USD | 0.00 USD | `+86.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.05` | 28,930,000.00 USD | 2,440.00 USD | 0.00 USD | `+87.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.95` | 28,930,000.00 USD | 349.34 USD | 0.00 USD | `+88.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.45` | 28,950,000.00 USD | 19,620.00 USD | 0.00 USD | `+89.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.45` | 29,500,000.00 USD | 550,350.00 USD | 0.00 USD | `+90.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.05` | 29,530,000.00 USD | 29,610.00 USD | 0.00 USD | `+91.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.05` | 29,690,000.00 USD | 165,580.00 USD | 0.00 USD | `+94.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.05` | 29,830,000.00 USD | 141,190.00 USD | 0.00 USD | `+95.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `189.05` | 29,850,000.00 USD | 15,340.00 USD | 0.00 USD | `+96.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.05` | 29,880,000.00 USD | 35,880.00 USD | 0.00 USD | `+97.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.35` | 29,880,000.00 USD | 744.27 USD | 0.00 USD | `+97.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.65` | 29,890,000.00 USD | 7,750.00 USD | 0.00 USD | `+97.78%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `82.60` | 162,860,000.00 USD | 0.00 USD | 162,860,000.00 USD | 53,130.00 USD | 56,870.00 USD | 141,300.00 USD |
| `7D` | `82.80` | 162,600,000.00 USD | 0.00 USD | 162,600,000.00 USD | 1,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `83.00` | 162,600,000.00 USD | 0.00 USD | 162,600,000.00 USD | 1,690.00 USD | 2,080.00 USD | 0.00 USD |
| `7D` | `83.20` | 162,600,000.00 USD | 0.00 USD | 162,600,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD |
| `7D` | `83.60` | 162,560,000.00 USD | 0.00 USD | 162,560,000.00 USD | 0.00 USD | 0.00 USD | 9,920.00 USD |
| `7D` | `83.80` | 162,550,000.00 USD | 0.00 USD | 162,550,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD |
| `7D` | `84.20` | 162,540,000.00 USD | 0.00 USD | 162,540,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD |
| `7D` | `84.40` | 162,520,000.00 USD | 0.00 USD | 162,520,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD |
| `7D` | `85.20` | 162,490,000.00 USD | 0.00 USD | 162,490,000.00 USD | 0.00 USD | 218,580.00 USD | 0.00 USD |
| `7D` | `85.40` | 162,270,000.00 USD | 0.00 USD | 162,270,000.00 USD | 0.00 USD | 12,950.00 USD | 192,310.00 USD |
| `7D` | `85.60` | 162,070,000.00 USD | 0.00 USD | 162,070,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD |
| `7D` | `85.80` | 161,880,000.00 USD | 0.00 USD | 161,880,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD |
| `7D` | `86.20` | 161,610,000.00 USD | 0.00 USD | 161,610,000.00 USD | 0.00 USD | 12,130.00 USD | 199,350.00 USD |
| `7D` | `86.40` | 161,400,000.00 USD | 0.00 USD | 161,400,000.00 USD | 0.00 USD | 311,220.00 USD | 4,340.00 USD |
| `1D` | `86.80` | 166,230,000.00 USD | 0.00 USD | 166,230,000.00 USD | 27,250.00 USD | 340,470.00 USD | 80,050.00 USD |
| `7D` | `86.80` | 161,090,000.00 USD | 0.00 USD | 161,090,000.00 USD | 0.00 USD | 149,840.00 USD | 0.00 USD |
| `1D` | `87.00` | 165,780,000.00 USD | 0.00 USD | 165,780,000.00 USD | 290,630.00 USD | 405,560.00 USD | 356,220.00 USD |
| `7D` | `87.00` | 160,940,000.00 USD | 0.00 USD | 160,940,000.00 USD | 271,000.00 USD | 183,160.00 USD | 297,340.00 USD |
| `1D` | `87.20` | 164,730,000.00 USD | 0.00 USD | 164,730,000.00 USD | 226,040.00 USD | 113,550.00 USD | 364,780.00 USD |
| `7D` | `87.20` | 160,190,000.00 USD | 0.00 USD | 160,190,000.00 USD | 8,850.00 USD | 6,510.00 USD | 6,820.00 USD |
| `1D` | `87.40` | 164,020,000.00 USD | 0.00 USD | 164,020,000.00 USD | 123,520.00 USD | 316,080.00 USD | 128,070.00 USD |
| `7D` | `87.40` | 160,160,000.00 USD | 0.00 USD | 160,160,000.00 USD | 248,310.00 USD | 225,130.00 USD | 288,100.00 USD |
| `1D` | `87.60` | 163,460,000.00 USD | 0.00 USD | 163,460,000.00 USD | 105,350.00 USD | 295,330.00 USD | 77,040.00 USD |
| `7D` | `87.60` | 159,400,000.00 USD | 0.00 USD | 159,400,000.00 USD | 0.00 USD | 275,130.00 USD | 421,310.00 USD |
| `1D` | `87.80` | 162,980,000.00 USD | 0.00 USD | 162,980,000.00 USD | 90,150.00 USD | 276,230.00 USD | 716,950.00 USD |
| `7D` | `87.80` | 158,710,000.00 USD | 0.00 USD | 158,710,000.00 USD | 0.00 USD | 413,150.00 USD | 11,130.00 USD |
| `1D` | `88.00` | 161,900,000.00 USD | 0.00 USD | 161,900,000.00 USD | 47,860.00 USD | 202,660.00 USD | 485,910.00 USD |
| `7D` | `88.00` | 158,280,000.00 USD | 0.00 USD | 158,280,000.00 USD | 0.00 USD | 12,070.00 USD | 251,100.00 USD |
| `1D` | `88.20` | 161,160,000.00 USD | 0.00 USD | 161,160,000.00 USD | 140,490.00 USD | 168,390.00 USD | 365,710.00 USD |
| `7D` | `88.20` | 158,020,000.00 USD | 0.00 USD | 158,020,000.00 USD | 9,900.00 USD | 20,610.00 USD | 28,240.00 USD |
| `1D` | `88.40` | 160,480,000.00 USD | 0.00 USD | 160,480,000.00 USD | 84,680.00 USD | 178,840.00 USD | 65,030.00 USD |
| `7D` | `88.40` | 157,960,000.00 USD | 0.00 USD | 157,960,000.00 USD | 0.00 USD | 237,870.00 USD | 335,390.00 USD |
| `1D` | `88.60` | 160,160,000.00 USD | 0.00 USD | 160,160,000.00 USD | 68,370.00 USD | 64,340.00 USD | 0.00 USD |
| `1D` | `88.80` | 160,020,000.00 USD | 0.00 USD | 160,020,000.00 USD | 304,990.00 USD | 175,710.00 USD | 415,440.00 USD |
| `7D` | `88.80` | 157,390,000.00 USD | 0.00 USD | 157,390,000.00 USD | 241,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `89.00` | 159,130,000.00 USD | 0.00 USD | 159,130,000.00 USD | 8,600.00 USD | 11,540.00 USD | 227,790.00 USD |
| `7D` | `89.00` | 157,140,000.00 USD | 0.00 USD | 157,140,000.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD |
| `1D` | `89.20` | 158,880,000.00 USD | 0.00 USD | 158,880,000.00 USD | 377,030.00 USD | 119,090.00 USD | 11,970.00 USD |
| `7D` | `89.20` | 156,210,000.00 USD | 0.00 USD | 156,210,000.00 USD | 8,180.00 USD | 10,750.00 USD | 315,450.00 USD |
| `1D` | `89.40` | 158,370,000.00 USD | 0.00 USD | 158,370,000.00 USD | 5,150.00 USD | 292,120.00 USD | 274,990.00 USD |
| `7D` | `89.40` | 155,880,000.00 USD | 0.00 USD | 155,880,000.00 USD | 697,470.00 USD | 26,220.00 USD | 160,460.00 USD |
| `1D` | `89.60` | 157,800,000.00 USD | 0.00 USD | 157,800,000.00 USD | 138,450.00 USD | 5,250.00 USD | 135,260.00 USD |
| `7D` | `89.60` | 154,990,000.00 USD | 0.00 USD | 154,990,000.00 USD | 684,220.00 USD | 270,260.00 USD | 723,370.00 USD |
| `1D` | `89.80` | 157,520,000.00 USD | 0.00 USD | 157,520,000.00 USD | 54,220.00 USD | 91,280.00 USD | 440,250.00 USD |
| `7D` | `89.80` | 153,320,000.00 USD | 0.00 USD | 153,320,000.00 USD | 425,950.00 USD | 318,390.00 USD | 314,310.00 USD |
| `1D` | `90.00` | 156,930,000.00 USD | 0.00 USD | 156,930,000.00 USD | 686,700.00 USD | 282,770.00 USD | 278,530.00 USD |
| `7D` | `90.00` | 152,260,000.00 USD | 0.00 USD | 152,260,000.00 USD | 374,600.00 USD | 647,410.00 USD | 1,090,000.00 USD |
| `1D` | `90.20` | 155,690,000.00 USD | 0.00 USD | 155,690,000.00 USD | 818,880.00 USD | 911,910.00 USD | 363,360.00 USD |
| `7D` | `90.20` | 150,140,000.00 USD | 0.00 USD | 150,140,000.00 USD | 1,250,000.00 USD | 590,390.00 USD | 735,310.00 USD |
| `1D` | `90.40` | 153,590,000.00 USD | 0.00 USD | 153,590,000.00 USD | 639,290.00 USD | 495,650.00 USD | 670,880.00 USD |
| `7D` | `90.40` | 147,560,000.00 USD | 0.00 USD | 147,560,000.00 USD | 796,240.00 USD | 68,740.00 USD | 694,770.00 USD |
| `1D` | `90.60` | 151,790,000.00 USD | 0.00 USD | 151,790,000.00 USD | 676,760.00 USD | 653,070.00 USD | 788,350.00 USD |
| `7D` | `90.60` | 146,000,000.00 USD | 0.00 USD | 146,000,000.00 USD | 1,040,000.00 USD | 1,010,000.00 USD | 1,560,000.00 USD |
| `1D` | `90.80` | 149,670,000.00 USD | 0.00 USD | 149,670,000.00 USD | 404,570.00 USD | 518,670.00 USD | 250,200.00 USD |
| `7D` | `90.80` | 142,390,000.00 USD | 0.00 USD | 142,390,000.00 USD | 1,210,000.00 USD | 1,200,000.00 USD | 1,480,000.00 USD |
| `1D` | `91.00` | 148,490,000.00 USD | 0.00 USD | 148,490,000.00 USD | 1,020,000.00 USD | 597,650.00 USD | 483,730.00 USD |
| `7D` | `91.00` | 138,500,000.00 USD | 0.00 USD | 138,500,000.00 USD | 1,190,000.00 USD | 609,900.00 USD | 810,620.00 USD |
| `1D` | `91.20` | 146,390,000.00 USD | 0.00 USD | 146,390,000.00 USD | 16,980.00 USD | 493,060.00 USD | 403,810.00 USD |
| `7D` | `91.20` | 135,890,000.00 USD | 0.00 USD | 135,890,000.00 USD | 2,280,000.00 USD | 868,420.00 USD | 638,860.00 USD |
| `1D` | `91.40` | 145,470,000.00 USD | 0.00 USD | 145,470,000.00 USD | 664,720.00 USD | 758,110.00 USD | 111,340.00 USD |
| `7D` | `91.40` | 132,110,000.00 USD | 0.00 USD | 132,110,000.00 USD | 1,180,000.00 USD | 1,030,000.00 USD | 1,620,000.00 USD |
| `1D` | `91.60` | 143,940,000.00 USD | 0.00 USD | 143,940,000.00 USD | 488,750.00 USD | 281,460.00 USD | 1,100,000.00 USD |
| `7D` | `91.60` | 128,280,000.00 USD | 0.00 USD | 128,280,000.00 USD | 500,280.00 USD | 1,020,000.00 USD | 872,760.00 USD |
| `1D` | `91.80` | 142,070,000.00 USD | 0.00 USD | 142,070,000.00 USD | 526,140.00 USD | 449,000.00 USD | 713,610.00 USD |
| `7D` | `91.80` | 125,890,000.00 USD | 0.00 USD | 125,890,000.00 USD | 932,400.00 USD | 797,110.00 USD | 688,730.00 USD |
| `1D` | `92.00` | 140,380,000.00 USD | 0.00 USD | 140,380,000.00 USD | 2,810,000.00 USD | 2,220,000.00 USD | 1,110,000.00 USD |
| `7D` | `92.00` | 123,470,000.00 USD | 0.00 USD | 123,470,000.00 USD | 681,440.00 USD | 656,110.00 USD | 990,500.00 USD |
| `1D` | `92.20` | 134,240,000.00 USD | 0.00 USD | 134,240,000.00 USD | 887,260.00 USD | 1,630,000.00 USD | 465,660.00 USD |
| `7D` | `92.20` | 121,150,000.00 USD | 0.00 USD | 121,150,000.00 USD | 2,870,000.00 USD | 1,110,000.00 USD | 289,060.00 USD |
| `1D` | `92.40` | 131,260,000.00 USD | 0.00 USD | 131,260,000.00 USD | 731,980.00 USD | 331,330.00 USD | 2,170,000.00 USD |
| `7D` | `92.40` | 116,880,000.00 USD | 0.00 USD | 116,880,000.00 USD | 550,500.00 USD | 833,900.00 USD | 1,540,000.00 USD |
| `1D` | `92.60` | 128,030,000.00 USD | 0.00 USD | 128,030,000.00 USD | 1,330,000.00 USD | 1,530,000.00 USD | 2,420,000.00 USD |
| `7D` | `92.60` | 113,960,000.00 USD | 0.00 USD | 113,960,000.00 USD | 98,670.00 USD | 880,990.00 USD | 1,480,000.00 USD |
| `1D` | `92.80` | 122,750,000.00 USD | 0.00 USD | 122,750,000.00 USD | 2,020,000.00 USD | 948,040.00 USD | 977,640.00 USD |
| `7D` | `92.80` | 111,500,000.00 USD | 0.00 USD | 111,500,000.00 USD | 463,730.00 USD | 2,370,000.00 USD | 1,610,000.00 USD |
| `1D` | `93.00` | 118,800,000.00 USD | 0.00 USD | 118,800,000.00 USD | 3,260,000.00 USD | 3,880,000.00 USD | 3,590,000.00 USD |
| `7D` | `93.00` | 107,060,000.00 USD | 0.00 USD | 107,060,000.00 USD | 539,240.00 USD | 550,690.00 USD | 2,030,000.00 USD |
| `1D` | `93.20` | 108,080,000.00 USD | 0.00 USD | 108,080,000.00 USD | 2,720,000.00 USD | 1,820,000.00 USD | 1,990,000.00 USD |
| `7D` | `93.20` | 103,940,000.00 USD | 0.00 USD | 103,940,000.00 USD | 1,090,000.00 USD | 670,930.00 USD | 2,130,000.00 USD |
| `1D` | `93.40` | 101,550,000.00 USD | 0.00 USD | 101,550,000.00 USD | 3,070,000.00 USD | 3,100,000.00 USD | 2,350,000.00 USD |
| `7D` | `93.40` | 100,050,000.00 USD | 0.00 USD | 100,050,000.00 USD | 611,840.00 USD | 2,660,000.00 USD | 1,430,000.00 USD |
| `1D` | `93.60` | 93,030,000.00 USD | 0.00 USD | 93,030,000.00 USD | 1,950,000.00 USD | 3,880,000.00 USD | 1,100,000.00 USD |
| `7D` | `93.60` | 95,340,000.00 USD | 0.00 USD | 95,340,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,640,000.00 USD |
| `1D` | `93.80` | 86,090,000.00 USD | 0.00 USD | 86,090,000.00 USD | 1,010,000.00 USD | 1,030,000.00 USD | 483,140.00 USD |
| `7D` | `93.80` | 92,400,000.00 USD | 0.00 USD | 92,400,000.00 USD | 0.00 USD | 2,080,000.00 USD | 3,170,000.00 USD |
| `1D` | `94.00` | 83,570,000.00 USD | 0.00 USD | 83,570,000.00 USD | 759,420.00 USD | 1,060,000.00 USD | 1,830,000.00 USD |
| `7D` | `94.00` | 87,150,000.00 USD | 0.00 USD | 87,150,000.00 USD | 2,660,000.00 USD | 1,780,000.00 USD | 2,210,000.00 USD |
| `1D` | `94.20` | 79,930,000.00 USD | 0.00 USD | 79,930,000.00 USD | 1,980,000.00 USD | 1,940,000.00 USD | 2,160,000.00 USD |
| `7D` | `94.20` | 80,500,000.00 USD | 0.00 USD | 80,500,000.00 USD | 24,740.00 USD | 962,410.00 USD | 2,750,000.00 USD |
| `1D` | `94.40` | 73,850,000.00 USD | 0.00 USD | 73,850,000.00 USD | 1,650,000.00 USD | 568,640.00 USD | 1,010,000.00 USD |
| `7D` | `94.40` | 76,770,000.00 USD | 0.00 USD | 76,770,000.00 USD | 0.00 USD | 496,790.00 USD | 9,790.00 USD |
| `1D` | `94.60` | 70,620,000.00 USD | 0.00 USD | 70,620,000.00 USD | 142,910.00 USD | 1,380,000.00 USD | 398,720.00 USD |
| `7D` | `94.60` | 76,260,000.00 USD | 0.00 USD | 76,260,000.00 USD | 560,570.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `94.80` | 68,700,000.00 USD | 0.00 USD | 68,700,000.00 USD | 2,970,000.00 USD | 800,730.00 USD | 1,620,000.00 USD |
| `7D` | `94.80` | 75,700,000.00 USD | 0.00 USD | 75,700,000.00 USD | 2,090,000.00 USD | 152,290.00 USD | 3,360,000.00 USD |
| `1D` | `95.00` | 63,320,000.00 USD | 0.00 USD | 63,320,000.00 USD | 4,450,000.00 USD | 899,320.00 USD | 1,130,000.00 USD |
| `7D` | `95.00` | 70,090,000.00 USD | 0.00 USD | 70,090,000.00 USD | 3,400,000.00 USD | 4,770,000.00 USD | 1,570,000.00 USD |
| `1D` | `95.20` | 56,840,000.00 USD | 0.00 USD | 56,840,000.00 USD | 1,720,000.00 USD | 2,190,000.00 USD | 3,130,000.00 USD |
| `7D` | `95.20` | 60,350,000.00 USD | 0.00 USD | 60,350,000.00 USD | 2,420,000.00 USD | 317,900.00 USD | 17,980.00 USD |
| `1D` | `95.40` | 49,800,000.00 USD | 0.00 USD | 49,800,000.00 USD | 1,120,000.00 USD | 1,820,000.00 USD | 1,270,000.00 USD |
| `7D` | `95.40` | 57,590,000.00 USD | 0.00 USD | 57,590,000.00 USD | 2,080,000.00 USD | 2,620,000.00 USD | 4,590,000.00 USD |
| `1D` | `95.60` | 45,590,000.00 USD | 0.00 USD | 45,590,000.00 USD | 1,850,000.00 USD | 2,410,000.00 USD | 1,200,000.00 USD |
| `7D` | `95.60` | 48,300,000.00 USD | 0.00 USD | 48,300,000.00 USD | 3,820,000.00 USD | 7,040,000.00 USD | 4,590,000.00 USD |
| `1D` | `95.80` | 40,130,000.00 USD | 0.00 USD | 40,130,000.00 USD | 2,040,000.00 USD | 1,900,000.00 USD | 7,420,000.00 USD |
| `7D` | `95.80` | 32,850,000.00 USD | 0.00 USD | 32,850,000.00 USD | 3,400,000.00 USD | 93,510.00 USD | 2,300,000.00 USD |
| `1D` | `96.00` | 28,770,000.00 USD | 0.00 USD | 28,770,000.00 USD | 4,610,000.00 USD | 2,890,000.00 USD | 6,080,000.00 USD |
| `7D` | `96.00` | 27,060,000.00 USD | 0.00 USD | 27,060,000.00 USD | 5,350,000.00 USD | 1,290,000.00 USD | 5,620,000.00 USD |
| `1D` | `96.20` | 15,180,000.00 USD | 0.00 USD | 15,180,000.00 USD | 6,210,000.00 USD | 7,360,000.00 USD | 1,610,000.00 USD |
| `7D` | `96.20` | 14,800,000.00 USD | 0.00 USD | 14,800,000.00 USD | 6,840,000.00 USD | 2,710,000.00 USD | 5,250,000.00 USD |
| `1D` | `96.40` | 11,260,000.00 USD | 11,260,000.00 USD | 0.00 USD | 4,170,000.00 USD | 2,150,000.00 USD | 4,940,000.00 USD |
| `1D` | `96.40` | 22,510,000.00 USD | 22,510,000.00 USD | 0.00 USD | 4,170,000.00 USD | 2,150,000.00 USD | 4,940,000.00 USD |
| `7D` | `96.40` | 10,660,000.00 USD | 10,660,000.00 USD | 0.00 USD | 1,600,000.00 USD | 2,590,000.00 USD | 6,470,000.00 USD |
| `7D` | `96.40` | 21,310,000.00 USD | 21,310,000.00 USD | 0.00 USD | 1,600,000.00 USD | 2,590,000.00 USD | 6,470,000.00 USD |
| `1D` | `96.60` | 26,120,000.00 USD | 26,120,000.00 USD | 0.00 USD | 1,300,000.00 USD | 2,010,000.00 USD | 299,180.00 USD |
| `7D` | `96.60` | 21,340,000.00 USD | 21,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD |
| `1D` | `96.80` | 26,130,000.00 USD | 26,130,000.00 USD | 0.00 USD | 0.00 USD | 8,140.00 USD | 0.00 USD |
| `7D` | `96.80` | 21,400,000.00 USD | 21,400,000.00 USD | 0.00 USD | 0.00 USD | 64,730.00 USD | 0.00 USD |
| `1D` | `97.00` | 27,540,000.00 USD | 27,540,000.00 USD | 0.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD |
| `7D` | `97.20` | 24,720,000.00 USD | 24,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,310,000.00 USD |
| `1D` | `97.40` | 29,370,000.00 USD | 29,370,000.00 USD | 0.00 USD | 534,370.00 USD | 1,280,000.00 USD | 18,900.00 USD |
| `7D` | `97.40` | 24,820,000.00 USD | 24,820,000.00 USD | 0.00 USD | 0.00 USD | 101,560.00 USD | 0.00 USD |
| `1D` | `97.60` | 30,610,000.00 USD | 30,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,230,000.00 USD |
| `7D` | `97.60` | 28,760,000.00 USD | 28,760,000.00 USD | 0.00 USD | 0.00 USD | 24,930.00 USD | 3,910,000.00 USD |
| `1D` | `97.80` | 36,010,000.00 USD | 36,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 876,010.00 USD | 1,520,000.00 USD |
| `7D` | `97.80` | 40,800,000.00 USD | 40,800,000.00 USD | 0.00 USD | 7,580,000.00 USD | 3,430,000.00 USD | 1,020,000.00 USD |
| `1D` | `98.00` | 40,860,000.00 USD | 40,860,000.00 USD | 0.00 USD | 2,320,000.00 USD | 712,280.00 USD | 1,820,000.00 USD |
| `7D` | `98.00` | 57,500,000.00 USD | 57,500,000.00 USD | 0.00 USD | 14,120,000.00 USD | 561,730.00 USD | 2,030,000.00 USD |
| `1D` | `98.20` | 47,970,000.00 USD | 47,970,000.00 USD | 0.00 USD | 3,200,000.00 USD | 2,290,000.00 USD | 1,620,000.00 USD |
| `7D` | `98.20` | 68,410,000.00 USD | 68,410,000.00 USD | 0.00 USD | 9,790,000.00 USD | 1,120,000.00 USD | 0.00 USD |
| `1D` | `98.40` | 59,030,000.00 USD | 59,030,000.00 USD | 0.00 USD | 772,180.00 USD | 311,650.00 USD | 9,980,000.00 USD |
| `7D` | `98.40` | 79,550,000.00 USD | 79,550,000.00 USD | 0.00 USD | 1,780,000.00 USD | 3,320,000.00 USD | 6,030,000.00 USD |
| `1D` | `98.60` | 73,070,000.00 USD | 73,070,000.00 USD | 0.00 USD | 649,650.00 USD | 5,980,000.00 USD | 7,410,000.00 USD |
| `7D` | `98.60` | 88,910,000.00 USD | 88,910,000.00 USD | 0.00 USD | 1,960,000.00 USD | 5,450,000.00 USD | 1,950,000.00 USD |
| `1D` | `98.80` | 87,200,000.00 USD | 87,200,000.00 USD | 0.00 USD | 2,640,000.00 USD | 4,390,000.00 USD | 7,100,000.00 USD |
| `7D` | `98.80` | 94,710,000.00 USD | 94,710,000.00 USD | 0.00 USD | 1,080,000.00 USD | 784,380.00 USD | 3,930,000.00 USD |
| `1D` | `99.00` | 102,560,000.00 USD | 102,560,000.00 USD | 0.00 USD | 3,500,000.00 USD | 6,290,000.00 USD | 5,570,000.00 USD |
| `7D` | `99.00` | 103,540,000.00 USD | 103,540,000.00 USD | 0.00 USD | 2,170,000.00 USD | 2,700,000.00 USD | 3,960,000.00 USD |
| `1D` | `99.20` | 113,660,000.00 USD | 113,660,000.00 USD | 0.00 USD | 2,840,000.00 USD | 4,520,000.00 USD | 3,740,000.00 USD |
| `7D` | `99.20` | 117,510,000.00 USD | 117,510,000.00 USD | 0.00 USD | 1,220,000.00 USD | 6,520,000.00 USD | 6,240,000.00 USD |
| `1D` | `99.40` | 119,430,000.00 USD | 119,430,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,650,000.00 USD | 1,740,000.00 USD |
| `7D` | `99.40` | 118,550,000.00 USD | 118,550,000.00 USD | 0.00 USD | 0.00 USD | 1,010,000.00 USD | 25,850.00 USD |
| `1D` | `99.60` | 135,880,000.00 USD | 135,880,000.00 USD | 0.00 USD | 2,920,000.00 USD | 6,420,000.00 USD | 7,120,000.00 USD |
| `7D` | `99.60` | 123,980,000.00 USD | 123,980,000.00 USD | 0.00 USD | 2,240,000.00 USD | 2,640,000.00 USD | 545,090.00 USD |
| `1D` | `99.80` | 150,840,000.00 USD | 150,840,000.00 USD | 0.00 USD | 2,520,000.00 USD | 4,590,000.00 USD | 7,850,000.00 USD |
| `7D` | `99.80` | 127,310,000.00 USD | 127,310,000.00 USD | 0.00 USD | 736,270.00 USD | 1,330,000.00 USD | 1,270,000.00 USD |
| `1D` | `100.00` | 161,300,000.00 USD | 161,300,000.00 USD | 0.00 USD | 2,850,000.00 USD | 3,360,000.00 USD | 4,250,000.00 USD |
| `7D` | `100.00` | 138,640,000.00 USD | 138,640,000.00 USD | 0.00 USD | 2,220,000.00 USD | 2,310,000.00 USD | 6,790,000.00 USD |
| `1D` | `100.20` | 164,470,000.00 USD | 164,470,000.00 USD | 0.00 USD | 651,800.00 USD | 2,130,000.00 USD | 388,240.00 USD |
| `7D` | `100.20` | 144,730,000.00 USD | 144,730,000.00 USD | 0.00 USD | 843,770.00 USD | 2,460,000.00 USD | 2,780,000.00 USD |
| `1D` | `100.40` | 170,220,000.00 USD | 170,220,000.00 USD | 0.00 USD | 976,110.00 USD | 1,790,000.00 USD | 2,990,000.00 USD |
| `7D` | `100.40` | 149,210,000.00 USD | 149,210,000.00 USD | 0.00 USD | 993,830.00 USD | 654,600.00 USD | 2,830,000.00 USD |
| `1D` | `100.60` | 181,260,000.00 USD | 181,260,000.00 USD | 0.00 USD | 2,300,000.00 USD | 1,830,000.00 USD | 6,910,000.00 USD |
| `7D` | `100.60` | 155,050,000.00 USD | 155,050,000.00 USD | 0.00 USD | 2,150,000.00 USD | 1,480,000.00 USD | 2,220,000.00 USD |
| `1D` | `100.80` | 188,000,000.00 USD | 188,000,000.00 USD | 0.00 USD | 2,610,000.00 USD | 1,940,000.00 USD | 2,200,000.00 USD |
| `7D` | `100.80` | 158,210,000.00 USD | 158,210,000.00 USD | 0.00 USD | 994,710.00 USD | 1,380,000.00 USD | 786,390.00 USD |
| `1D` | `101.00` | 198,770,000.00 USD | 198,770,000.00 USD | 0.00 USD | 6,070,000.00 USD | 3,420,000.00 USD | 1,270,000.00 USD |
| `7D` | `101.00` | 177,180,000.00 USD | 177,180,000.00 USD | 0.00 USD | 4,160,000.00 USD | 7,060,000.00 USD | 7,750,000.00 USD |
| `1D` | `101.20` | 211,010,000.00 USD | 211,010,000.00 USD | 0.00 USD | 5,270,000.00 USD | 4,010,000.00 USD | 2,970,000.00 USD |
| `7D` | `101.20` | 196,590,000.00 USD | 196,590,000.00 USD | 0.00 USD | 7,240,000.00 USD | 5,320,000.00 USD | 6,850,000.00 USD |
| `1D` | `101.40` | 221,710,000.00 USD | 221,710,000.00 USD | 0.00 USD | 3,860,000.00 USD | 2,700,000.00 USD | 4,140,000.00 USD |
| `7D` | `101.40` | 213,650,000.00 USD | 213,650,000.00 USD | 0.00 USD | 4,720,000.00 USD | 1,270,000.00 USD | 11,070,000.00 USD |
| `1D` | `101.60` | 236,590,000.00 USD | 236,590,000.00 USD | 0.00 USD | 2,980,000.00 USD | 2,630,000.00 USD | 9,260,000.00 USD |
| `7D` | `101.60` | 224,170,000.00 USD | 224,170,000.00 USD | 0.00 USD | 3,650,000.00 USD | 30,170.00 USD | 6,840,000.00 USD |
| `1D` | `101.80` | 242,810,000.00 USD | 242,810,000.00 USD | 0.00 USD | 646,170.00 USD | 836,200.00 USD | 4,730,000.00 USD |
| `7D` | `101.80` | 234,100,000.00 USD | 234,100,000.00 USD | 0.00 USD | 3,050,000.00 USD | 609,510.00 USD | 6,270,000.00 USD |
| `1D` | `102.00` | 249,090,000.00 USD | 249,090,000.00 USD | 0.00 USD | 2,520,000.00 USD | 1,780,000.00 USD | 1,990,000.00 USD |
| `7D` | `102.00` | 240,090,000.00 USD | 240,090,000.00 USD | 0.00 USD | 1,830,000.00 USD | 1,470,000.00 USD | 2,690,000.00 USD |
| `1D` | `102.20` | 255,180,000.00 USD | 255,180,000.00 USD | 0.00 USD | 3,110,000.00 USD | 1,170,000.00 USD | 1,800,000.00 USD |
| `7D` | `102.20` | 246,810,000.00 USD | 246,810,000.00 USD | 0.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,540,000.00 USD |
| `1D` | `102.40` | 259,600,000.00 USD | 259,600,000.00 USD | 0.00 USD | 1,560,000.00 USD | 716,320.00 USD | 2,150,000.00 USD |
| `7D` | `102.40` | 252,120,000.00 USD | 252,120,000.00 USD | 0.00 USD | 2,340,000.00 USD | 304,350.00 USD | 2,660,000.00 USD |
| `1D` | `102.60` | 262,240,000.00 USD | 262,240,000.00 USD | 0.00 USD | 985,660.00 USD | 606,030.00 USD | 1,040,000.00 USD |
| `7D` | `102.60` | 254,580,000.00 USD | 254,580,000.00 USD | 0.00 USD | 1,450,000.00 USD | 979,270.00 USD | 33,240.00 USD |
| `1D` | `102.80` | 266,290,000.00 USD | 266,290,000.00 USD | 0.00 USD | 1,260,000.00 USD | 1,570,000.00 USD | 1,220,000.00 USD |
| `7D` | `102.80` | 262,670,000.00 USD | 262,670,000.00 USD | 0.00 USD | 7,780,000.00 USD | 23,810.00 USD | 286,910.00 USD |
| `1D` | `103.00` | 271,340,000.00 USD | 271,340,000.00 USD | 0.00 USD | 3,120,000.00 USD | 1,440,000.00 USD | 498,100.00 USD |
| `7D` | `103.00` | 279,610,000.00 USD | 279,610,000.00 USD | 0.00 USD | 12,270,000.00 USD | 394,420.00 USD | 4,270,000.00 USD |
| `1D` | `103.20` | 273,710,000.00 USD | 273,710,000.00 USD | 0.00 USD | 301,000.00 USD | 853,780.00 USD | 1,220,000.00 USD |
| `7D` | `103.20` | 292,280,000.00 USD | 292,280,000.00 USD | 0.00 USD | 11,620,000.00 USD | 140,550.00 USD | 913,680.00 USD |
| `1D` | `103.40` | 276,640,000.00 USD | 276,640,000.00 USD | 0.00 USD | 867,130.00 USD | 1,180,000.00 USD | 877,320.00 USD |
| `7D` | `103.40` | 306,850,000.00 USD | 306,850,000.00 USD | 0.00 USD | 11,050,000.00 USD | 233,330.00 USD | 3,280,000.00 USD |
| `1D` | `103.60` | 284,270,000.00 USD | 284,270,000.00 USD | 0.00 USD | 2,430,000.00 USD | 183,360.00 USD | 5,010,000.00 USD |
| `7D` | `103.60` | 325,240,000.00 USD | 325,240,000.00 USD | 0.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD |
| `1D` | `103.80` | 287,420,000.00 USD | 287,420,000.00 USD | 0.00 USD | 481,980.00 USD | 1,320,000.00 USD | 1,350,000.00 USD |
| `7D` | `103.80` | 337,630,000.00 USD | 337,630,000.00 USD | 0.00 USD | 7,960,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD |
| `1D` | `104.00` | 293,220,000.00 USD | 293,220,000.00 USD | 0.00 USD | 2,410,000.00 USD | 1,490,000.00 USD | 1,910,000.00 USD |
| `7D` | `104.00` | 364,330,000.00 USD | 364,330,000.00 USD | 0.00 USD | 10,830,000.00 USD | 7,160,000.00 USD | 8,710,000.00 USD |
| `1D` | `104.20` | 296,390,000.00 USD | 296,390,000.00 USD | 0.00 USD | 1,290,000.00 USD | 831,810.00 USD | 1,050,000.00 USD |
| `7D` | `104.20` | 386,360,000.00 USD | 386,360,000.00 USD | 0.00 USD | 8,520,000.00 USD | 7,230,000.00 USD | 6,280,000.00 USD |
| `1D` | `104.40` | 300,650,000.00 USD | 300,650,000.00 USD | 0.00 USD | 1,470,000.00 USD | 1,330,000.00 USD | 1,460,000.00 USD |
| `7D` | `104.40` | 403,540,000.00 USD | 403,540,000.00 USD | 0.00 USD | 5,100,000.00 USD | 3,710,000.00 USD | 8,360,000.00 USD |
| `1D` | `104.60` | 304,660,000.00 USD | 304,660,000.00 USD | 0.00 USD | 1,030,000.00 USD | 794,070.00 USD | 2,180,000.00 USD |
| `7D` | `104.60` | 421,290,000.00 USD | 421,290,000.00 USD | 0.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 7,020,000.00 USD |
| `1D` | `104.80` | 308,670,000.00 USD | 308,670,000.00 USD | 0.00 USD | 1,250,000.00 USD | 820,470.00 USD | 1,950,000.00 USD |
| `7D` | `104.80` | 438,680,000.00 USD | 438,680,000.00 USD | 0.00 USD | 5,170,000.00 USD | 4,410,000.00 USD | 7,820,000.00 USD |
| `1D` | `105.00` | 309,900,000.00 USD | 309,900,000.00 USD | 0.00 USD | 463,890.00 USD | 350,040.00 USD | 413,950.00 USD |
| `7D` | `105.00` | 454,850,000.00 USD | 454,850,000.00 USD | 0.00 USD | 5,730,000.00 USD | 4,110,000.00 USD | 6,330,000.00 USD |
| `1D` | `105.20` | 310,970,000.00 USD | 310,970,000.00 USD | 0.00 USD | 111,930.00 USD | 94,030.00 USD | 864,650.00 USD |
| `7D` | `105.20` | 465,510,000.00 USD | 465,510,000.00 USD | 0.00 USD | 5,340,000.00 USD | 2,800,000.00 USD | 2,530,000.00 USD |
| `1D` | `105.40` | 311,450,000.00 USD | 311,450,000.00 USD | 0.00 USD | 262,490.00 USD | 138,720.00 USD | 78,430.00 USD |
| `7D` | `105.40` | 473,730,000.00 USD | 473,730,000.00 USD | 0.00 USD | 1,570,000.00 USD | 3,170,000.00 USD | 3,470,000.00 USD |
| `1D` | `105.60` | 311,880,000.00 USD | 311,880,000.00 USD | 0.00 USD | 130,280.00 USD | 187,950.00 USD | 110,700.00 USD |
| `7D` | `105.60` | 482,150,000.00 USD | 482,150,000.00 USD | 0.00 USD | 3,700,000.00 USD | 2,270,000.00 USD | 2,450,000.00 USD |
| `1D` | `105.80` | 312,570,000.00 USD | 312,570,000.00 USD | 0.00 USD | 87,540.00 USD | 526,970.00 USD | 76,760.00 USD |
| `7D` | `105.80` | 490,960,000.00 USD | 490,960,000.00 USD | 0.00 USD | 2,690,000.00 USD | 2,620,000.00 USD | 3,510,000.00 USD |
| `1D` | `106.00` | 313,720,000.00 USD | 313,720,000.00 USD | 0.00 USD | 372,000.00 USD | 554,120.00 USD | 226,820.00 USD |
| `7D` | `106.00` | 496,110,000.00 USD | 496,110,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,050,000.00 USD | 2,130,000.00 USD |
| `1D` | `106.20` | 315,140,000.00 USD | 315,140,000.00 USD | 0.00 USD | 623,340.00 USD | 349,490.00 USD | 440,280.00 USD |
| `7D` | `106.20` | 505,010,000.00 USD | 505,010,000.00 USD | 0.00 USD | 3,820,000.00 USD | 2,560,000.00 USD | 2,520,000.00 USD |
| `1D` | `106.40` | 315,980,000.00 USD | 315,980,000.00 USD | 0.00 USD | 191,590.00 USD | 403,460.00 USD | 243,530.00 USD |
| `7D` | `106.40` | 511,080,000.00 USD | 511,080,000.00 USD | 0.00 USD | 2,430,000.00 USD | 2,180,000.00 USD | 1,460,000.00 USD |
| `1D` | `106.60` | 317,980,000.00 USD | 317,980,000.00 USD | 0.00 USD | 547,840.00 USD | 307,440.00 USD | 1,150,000.00 USD |
| `7D` | `106.60` | 515,920,000.00 USD | 515,920,000.00 USD | 0.00 USD | 1,330,000.00 USD | 1,250,000.00 USD | 2,260,000.00 USD |
| `1D` | `106.80` | 319,550,000.00 USD | 319,550,000.00 USD | 0.00 USD | 434,130.00 USD | 399,910.00 USD | 737,390.00 USD |
| `7D` | `106.80` | 520,570,000.00 USD | 520,570,000.00 USD | 0.00 USD | 999,190.00 USD | 927,000.00 USD | 2,730,000.00 USD |
| `1D` | `107.00` | 320,330,000.00 USD | 320,330,000.00 USD | 0.00 USD | 193,920.00 USD | 413,830.00 USD | 167,050.00 USD |
| `7D` | `107.00` | 524,710,000.00 USD | 524,710,000.00 USD | 0.00 USD | 527,980.00 USD | 1,180,000.00 USD | 2,430,000.00 USD |
| `1D` | `107.20` | 320,820,000.00 USD | 320,820,000.00 USD | 0.00 USD | 0.00 USD | 50,140.00 USD | 436,040.00 USD |
| `7D` | `107.20` | 525,800,000.00 USD | 525,800,000.00 USD | 0.00 USD | 230,020.00 USD | 507,570.00 USD | 352,500.00 USD |
| `1D` | `107.40` | 321,600,000.00 USD | 321,600,000.00 USD | 0.00 USD | 60,260.00 USD | 201,440.00 USD | 518,350.00 USD |
| `7D` | `107.40` | 527,090,000.00 USD | 527,090,000.00 USD | 0.00 USD | 0.00 USD | 576,040.00 USD | 709,670.00 USD |
| `7D` | `107.60` | 527,720,000.00 USD | 527,720,000.00 USD | 0.00 USD | 213,520.00 USD | 12,070.00 USD | 406,020.00 USD |
| `7D` | `107.80` | 528,560,000.00 USD | 528,560,000.00 USD | 0.00 USD | 499,550.00 USD | 31,020.00 USD | 305,630.00 USD |
| `7D` | `108.00` | 529,140,000.00 USD | 529,140,000.00 USD | 0.00 USD | 5,950.00 USD | 237,870.00 USD | 335,390.00 USD |
| `7D` | `108.20` | 529,420,000.00 USD | 529,420,000.00 USD | 0.00 USD | 0.00 USD | 205,080.00 USD | 74,400.00 USD |
| `7D` | `108.40` | 529,900,000.00 USD | 529,900,000.00 USD | 0.00 USD | 487,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `108.60` | 530,090,000.00 USD | 530,090,000.00 USD | 0.00 USD | 17,470.00 USD | 167,730.00 USD | 0.00 USD |
| `7D` | `108.80` | 531,020,000.00 USD | 531,020,000.00 USD | 0.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD |
| `7D` | `109.00` | 531,320,000.00 USD | 531,320,000.00 USD | 0.00 USD | 8,180.00 USD | 0.00 USD | 286,720.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `5.59B` | Total OI Tokens: `57,888,582.5 SOL`
  * 1h OI Change: `-0.15%` | 4h OI Change: `-1.86%` | 24h OI Change: `-13.58%`
  * Exchange Breakdown: Binance=`967.57M` | Bybit=`609.44M` | OKX=`383.58M` | Hyperliquid=`516.57M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-34.03K` | Last 24h: `177.62K` | Last 3d: `997.77K` | Last 7d: `2.11M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0065%` | **USDT OKX** | `-0.0149%` |
| **USDT Bybit** | `-0.0047%` | **USDT KuCoin** | `-0.0080%` |
| **USDT MEXC** | `0.0063%` | **USDT BingX** | `0.0058%` |
| **USDT Gate** | `-0.0058%` | **USDT Bitget** | `-0.0113%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0007%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `48.48%` | `51.52%` | `0.94` | 254,490,000.00 USD |
| `15M` | `Binance` | `49.51%` | `50.49%` | `0.98` | 84,620,000.00 USD |
| `15M` | `OKX` | `53.37%` | `46.63%` | `1.14` | 44,990,000.00 USD |
| `15M` | `Bybit` | `50.6%` | `49.4%` | `1.02` | 20,120,000.00 USD |
| `15M` | `KuCoin` | `45.41%` | `54.59%` | `0.83` | 1,220,000.00 USD |
| `15M` | `Gate` | `52.95%` | `47.05%` | `1.13` | 39,240,000.00 USD |
| `15M` | `Bitget` | `42.44%` | `57.56%` | `0.74` | 8,840,000.00 USD |
| `15M` | `BingX` | `26.3%` | `73.7%` | `0.36` | 4,710,000.00 USD |
| `15M` | `MEXC` | `56.97%` | `43.03%` | `1.32` | 9,140,000.00 USD |
| `15M` | `Bitunix` | `43.3%` | `56.7%` | `0.76` | 8,940,000.00 USD |
| `15M` | `Hyperliquid` | `55.27%` | `44.73%` | `1.24` | 7,960,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `54.94%` | `45.06%` | `1.22` | 616,870.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `33.14%` | `66.86%` | `0.50` | 2,050,000.00 USD |
| `15M` | `HTX` | `13.19%` | `86.81%` | `0.15` | 11,960,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `51.1%` | `48.9%` | `1.04` | 2,420,000.00 USD |
| `15M` | `Bitfinex` | `50.65%` | `49.35%` | `1.03` | 37,510.00 USD |
| `15M` | `Kraken` | `32.65%` | `67.35%` | `0.48` | 2,480,000.00 USD |
| `15M` | `Aster` | `66.01%` | `33.99%` | `1.94` | 2,410,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `45.5%` | `54.5%` | `0.83` | 2,770,000.00 USD |
| `15M` | `Whale Positions` | `49.51%` | `50.49%` | `0.98` | 84,620,000.00 USD |
| `15M` | `Global Accounts` | `48.48%` | `51.52%` | `0.94` | 254,490,000.00 USD |
| `1H` | `SOL` | `42.47%` | `57.53%` | `0.74` | 1,290,000,000.00 USD |
| `1H` | `Binance` | `47.53%` | `52.47%` | `0.91` | 356,860,000.00 USD |
| `1H` | `OKX` | `39.99%` | `60.01%` | `0.67` | 219,890,000.00 USD |
| `1H` | `Bybit` | `39.53%` | `60.47%` | `0.65` | 70,900,000.00 USD |
| `1H` | `KuCoin` | `49.95%` | `50.05%` | `1.00` | 4,900,000.00 USD |
| `1H` | `Gate` | `53.97%` | `46.03%` | `1.17` | 176,960,000.00 USD |
| `1H` | `Bitget` | `44.5%` | `55.5%` | `0.80` | 36,360,000.00 USD |
| `1H` | `BingX` | `32.69%` | `67.31%` | `0.49` | 18,060,000.00 USD |
| `1H` | `MEXC` | `46.42%` | `53.58%` | `0.87` | 37,360,000.00 USD |
| `1H` | `Bitunix` | `48.84%` | `51.16%` | `0.95` | 38,120,000.00 USD |
| `1H` | `Hyperliquid` | `50.26%` | `49.74%` | `1.01` | 60,160,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.32%` | `50.68%` | `0.97` | 4,080,000.00 USD |
| `1H` | `Crypto.com` | `52.36%` | `47.64%` | `1.10` | 0.00 USD |
| `1H` | `WhiteBIT` | `2.53%` | `97.47%` | `0.03` | 207,710,000.00 USD |
| `1H` | `HTX` | `28.81%` | `71.19%` | `0.40` | 23,060,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 12,520,000.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 382,550.00 USD |
| `1H` | `Kraken` | `56.1%` | `43.9%` | `1.28` | 4,970,000.00 USD |
| `1H` | `Aster` | `47.98%` | `52.02%` | `0.92` | 6,590,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `66.95%` | `33.05%` | `2.03` | 14,410,000.00 USD |
| `1H` | `Whale Positions` | `47.53%` | `52.47%` | `0.91` | 356,860,000.00 USD |
| `1H` | `Global Accounts` | `42.47%` | `57.53%` | `0.74` | 1,290,000,000.00 USD |
| `4H` | `SOL` | `47.01%` | `52.99%` | `0.89` | 6,220,000,000.00 USD |
| `4H` | `Binance` | `48.84%` | `51.16%` | `0.95` | 2,010,000,000.00 USD |
| `4H` | `OKX` | `46.8%` | `53.2%` | `0.88` | 1,090,000,000.00 USD |
| `4H` | `Bybit` | `48.26%` | `51.74%` | `0.93` | 363,820,000.00 USD |
| `4H` | `KuCoin` | `50.7%` | `49.3%` | `1.03` | 19,460,000.00 USD |
| `4H` | `Gate` | `55.93%` | `44.07%` | `1.27` | 918,510,000.00 USD |
| `4H` | `Bitget` | `49.43%` | `50.57%` | `0.98` | 202,940,000.00 USD |
| `4H` | `BingX` | `26.62%` | `73.38%` | `0.36` | 71,590,000.00 USD |
| `4H` | `MEXC` | `49.04%` | `50.96%` | `0.96` | 244,900,000.00 USD |
| `4H` | `Bitunix` | `45.55%` | `54.45%` | `0.84` | 201,030,000.00 USD |
| `4H` | `Hyperliquid` | `62.29%` | `37.71%` | `1.65` | 282,520,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.68%` | `50.32%` | `0.99` | 33,760,000.00 USD |
| `4H` | `Crypto.com` | `48.85%` | `51.15%` | `0.96` | 0.00 USD |
| `4H` | `WhiteBIT` | `4.55%` | `95.45%` | `0.05` | 484,820,000.00 USD |
| `4H` | `HTX` | `46.96%` | `53.04%` | `0.89` | 81,300,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 68,780,000.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 1,680,000.00 USD |
| `4H` | `Kraken` | `40.16%` | `59.84%` | `0.67` | 11,990,000.00 USD |
| `4H` | `Aster` | `35.84%` | `64.16%` | `0.56` | 49,390,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `59.82%` | `40.18%` | `1.49` | 78,740,000.00 USD |
| `4H` | `Whale Positions` | `48.84%` | `51.16%` | `0.95` | 2,010,000,000.00 USD |
| `4H` | `Global Accounts` | `47.01%` | `52.99%` | `0.89` | 6,220,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `97.31` | `97.23` | `97.31` | `97.59` | `96.94` | 34,349,154.70 USD | 16,069,023.45 USD | 18,280,131.25 USD | -2,211,107.80 USD | `-6.44%` | `8B / 12S` |
| `0:00 UTC` | `97.07` | `97.11` | `97.07` | `97.31` | `96.84` | 19,320,776.86 USD | 9,044,516.83 USD | 10,276,260.03 USD | -1,231,743.19 USD | `-6.38%` | `6B / 9S` |
| `5:00 UTC` | `97.31` | `97.36` | `97.31` | `97.56` | `97.18` | 14,539,694.05 USD | 7,744,567.35 USD | 6,795,126.70 USD | 949,440.65 USD | `+6.53%` | `8B / 2S` |
| `0:00 UTC` | `97.15` | `97.19` | `97.15` | `97.37` | `97.05` | 9,961,152.58 USD | 4,407,159.48 USD | 5,553,993.10 USD | -1,146,833.62 USD | `-11.51%` | `1B / 5S` |
| `5:00 UTC` | `97.03` | `97.24` | `97.03` | `97.56` | `97.00` | 11,034,358.76 USD | 5,603,314.27 USD | 5,431,044.48 USD | 172,269.79 USD | `+1.56%` | `15B / 4S` |
| `0:00 UTC` | `97.13` | `97.19` | `97.13` | `97.44` | `97.03` | 17,561,649.50 USD | 7,274,477.25 USD | 10,287,172.25 USD | -3,012,695.00 USD | `-17.15%` | `4B / 13S` |
| `5:00 UTC` | `96.81` | `96.94` | `96.81` | `97.16` | `96.81` | 12,337,515.78 USD | 5,226,804.15 USD | 7,110,711.63 USD | -1,883,907.48 USD | `-15.27%` | `2B / 2S` |
| `0:00 UTC` | `96.81` | `96.92` | `96.81` | `97.16` | `96.69` | 14,931,632.13 USD | 8,028,191.38 USD | 6,903,440.75 USD | 1,124,750.63 USD | `+7.53%` | `9B / 6S` |
| `5:00 UTC` | `96.80` | `96.85` | `96.80` | `97.02` | `96.73` | 9,878,254.59 USD | 5,512,052.81 USD | 4,366,201.79 USD | 1,145,851.02 USD | `+11.60%` | `5B / 5S` |
| `0:00 UTC` | `96.43` | `96.49` | `96.43` | `96.84` | `96.31` | 13,250,461.99 USD | 5,707,031.01 USD | 7,543,430.98 USD | -1,836,399.97 USD | `-13.86%` | `0B / 9S` |

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
| `5m` | -655,790.00 USD | -2,270,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,160,000.00 USD | -9,880,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,180,000.00 USD | -8,130,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,190,000.00 USD | -17,600,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,610,000.00 USD | -23,310,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -3,320,000.00 USD | -36,030,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 1,400,000.00 USD | -41,460,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 3,530,000.00 USD | -14,460,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -22,860,000.00 USD | -102,190,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -50,790,000.00 USD | -450,580,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 32,410,000.00 USD | -704,300,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -11,270,000.00 USD | -2,220,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-655.79K` | 15m=`-1.16M` | 1h=`-2.19M` | 24h=`-50.79M`
* Futures Capital Netflows: 5m=`-2.27M` | 15m=`-9.88M` | 1h=`-17.60M` | 24h=`-450.58M`
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
  * `2026-10-30 15:33:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:19:00 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:00 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:00 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:00 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `95.13` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `94.10` (Risk Distance: `1.03` pts)
  * +2.5R Take Profit: `97.71`
  * Mathematical Lot Sizing: **`9.70 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `98.09` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `99.12` (Risk Distance: `1.03` pts)
  * +2.5R Take Profit: `95.51`
  * Mathematical Lot Sizing: **`9.70 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`97.04`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
