# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 14:32:43 IST` (`2026-10-30 09:02:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `97.00` | **Live Ask Quote**: `97.23` | **Mid Price**: `97.12`
- **Spread Points**: `23.00` | **Spread BPS**: `23.68 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `97.12` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `97.79` | Lower -3.00σ Band: `96.44`
  * Upper +2.51σ Band: `97.65` | Lower -2.51σ Band: `96.58`
  * Upper +2.01σ Band: `97.52` | Lower -2.01σ Band: `96.71`
  * Upper +2.00σ Band: `97.50` | Lower -2.00σ Band: `96.73`
  * Upper +1.28σ Band: `97.39` | Lower -1.28σ Band: `96.84`
  * Upper +1.00σ Band: `97.31` | Lower -1.00σ Band: `96.92`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`97.12` | EMA-20=`97.12` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`97.12` (Slope: `+0.0000`) | EMA-100=`97.12`
  * Institutional Anchors: EMA-144=`97.12` | EMA-200=`97.12` (Slope: `+0.0000`) | EMA-233=`97.12`
- **Range Boundaries**: 24H High=`98.09` | 24H Low=`96.14` | Weekly High=`99.06` | Weekly Low=`95.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `98.09` (Distance: `-0.89%`)
  * Point of Control (POC) = `96.89` (Distance: `+0.34%`)
  * Value Area Low (VAL) = `95.01` (Distance: `+2.33%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`101.56` | POC=`99.94` | VAL=`98.94`
  * Prior Day Extremes: PDH=`102.93` | PDL=`94.56` | PDC=`95.94`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`102.02` | Weekly POC=`100.92` | Weekly VAL=`99.51`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`97.84` | Low=`91.86`
  * London Session (08:00-16:00 UTC): High=`98.28` | Low=`96.52`
  * New York Session (13:00-21:00 UTC): High=`97.70` | Low=`96.53`
  * Initial Balance (First Hour): IB High=`98.28` | IB Low=`96.72`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `96.73` - `97.50`
  * Optimal Trade Entry (OTE 0.705): `97.31`
  * Structural Invalidation Anchor (0.786): `97.89`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `97.10` | `97.55` | `97.05` | `97.53` | `49,118` | 4,778,935.56 USD | 1,704,871.97 USD | `+35.67%` | -219,493,242.90 USD | `+1.82` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `97.53` | `97.53` | `97.26` | `97.33` | `25,357` | 2,469,158.16 USD | -273,575.01 USD | `-11.08%` | -219,766,817.91 USD | `+0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `97.34` | `97.34` | `97.17` | `97.26` | `33,205` | 3,229,496.82 USD | -1,946,556.54 USD | `-60.27%` | -221,713,374.44 USD | `-1.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `97.21` | `97.36` | `97.04` | `97.09` | `102,500` | 9,961,152.58 USD | -1,146,833.62 USD | `-11.51%` | -221,250,291.84 USD | `-0.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `97.10` | `97.55` | `97.00` | `97.33` | `113,486` | 11,034,358.76 USD | 172,269.79 USD | `+1.56%` | -221,078,022.05 USD | `+0.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `97.34` | `97.34` | `97.17` | `97.26` | `33,128` | 3,222,039.84 USD | -1,952,280.34 USD | `-60.59%` | -223,030,302.38 USD | `-0.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `98.26` | `98.28` | `96.93` | `97.28` | `823,584` | 80,361,988.15 USD | -10,205,381.09 USD | `-12.70%` | -219,805,116.69 USD | `+0.02` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `97.28` | `97.55` | `96.84` | `97.33` | `564,307` | 54,855,982.25 USD | -1,256,866.37 USD | `-2.29%` | -221,061,983.07 USD | `+0.46` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `97.34` | `97.34` | `97.17` | `97.29` | `33,472` | 3,255,525.54 USD | -1,920,671.76 USD | `-59.00%` | -222,982,654.83 USD | `+0.43` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -192,935,382.59 USD | `+0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.54` | `96.72` | `97.28` | `3,030,040` | 295,921,356.18 USD | -16,839,868.63 USD | `-5.69%` | -209,775,251.22 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.28` | `97.55` | `96.84` | `97.26` | `597,512` | 58,085,479.07 USD | -3,203,422.91 USD | `-5.52%` | -212,978,674.13 USD | `+0.83` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -33,800,710.11 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `95.62` | `13,887,188` | 1,349,343,315.53 USD | -115,873,425.65 USD | `-8.59%` | -149,674,135.76 USD | `-1.37` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -192,935,382.59 USD | `+0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.54` | `96.72` | `97.28` | `3,030,040` | 295,921,356.18 USD | -16,839,868.63 USD | `-5.69%` | -209,775,251.22 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.28` | `97.55` | `96.84` | `97.26` | `597,512` | 58,085,479.07 USD | -3,203,422.91 USD | `-5.52%` | -212,978,674.13 USD | `+0.83` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`97.12`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `97.25` | `41.1200` | 3,999.08 USD | 508,930.87 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `97.25` | `41.1200` | 3,999.04 USD | 512,929.91 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `97.25` | `377.3500` | 36,698.04 USD | 549,627.95 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `97.25` | `150.1200` | 14,599.32 USD | 564,227.27 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `97.25` | `41.1300` | 3,999.89 USD | 568,227.16 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `97.25` | `41.1300` | 3,999.85 USD | 572,227.02 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `97.25` | `1086.9700` | 105,705.66 USD | 677,932.67 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `97.25` | `1296.1300` | 126,044.75 USD | 803,977.43 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `97.25` | `41.1300` | 3,999.73 USD | 807,977.16 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `97.26` | `10.0000` | 972.64 USD | 160,554.40 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.26` | `251.3200` | 24,444.14 USD | 184,998.53 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.26` | `47.9600` | 4,664.69 USD | 189,663.22 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `97.26` | `2068.8000` | 201,209.42 USD | 390,872.64 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `97.26` | `111.7000` | 10,863.72 USD | 401,736.36 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `97.26` | `1061.0700` | 103,195.42 USD | 504,931.78 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `97.27` | `434.0400` | 42,219.94 USD | 116,582.92 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `97.27` | `79.3000` | 7,713.59 USD | 124,296.52 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.27` | `257.0200` | 25,000.34 USD | 149,296.85 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `97.27` | `105.7400` | 10,284.91 USD | 159,581.76 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `97.28` | `178.7500` | 17,389.34 USD | 19,554.82 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `97.28` | `11.9800` | 1,165.44 USD | 2,165.49 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `97.28` | `10.2800` | 1,000.05 USD | 1,000.05 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `97.28` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 97.28` | `0.00%` | `-` |
| `BID` | `97.28` | `764.4300` | 74,362.99 USD | 74,362.99 USD | `11 orders` | `-0.00%` | `-` |
| `ASK` | `97.29` | `105.7200` | 10,285.60 USD | 37,570.93 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.29` | `0.1600` | 15.57 USD | 27,285.33 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.29` | `79.3000` | 7,714.94 USD | 27,269.76 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.30` | `89.7400` | 8,732.06 USD | 145,023.56 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `97.30` | `80.7000` | 7,852.35 USD | 136,291.50 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `97.30` | `45.1400` | 4,392.17 USD | 128,439.15 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `97.30` | `635.2600` | 61,810.80 USD | 124,046.98 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `97.30` | `232.3800` | 22,610.34 USD | 62,236.19 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `97.30` | `21.1200` | 2,054.91 USD | 39,625.85 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `97.31` | `1995.7000` | 194,205.56 USD | 542,447.34 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `97.31` | `1205.8300` | 117,340.52 USD | 348,241.78 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `97.31` | `80.7000` | 7,852.92 USD | 230,901.26 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `97.31` | `238.0700` | 23,166.35 USD | 223,048.34 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `97.31` | `110.3700` | 10,739.88 USD | 199,881.99 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `97.31` | `80.7000` | 7,852.67 USD | 189,142.11 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `97.31` | `292.0000` | 28,413.35 USD | 181,289.43 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `97.31` | `80.7000` | 7,852.51 USD | 152,876.08 USD | `1 orders` | `+0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:32:27 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `10` | `0x5b5d...c060` | `SHORT` | 67,721,350.73 USD | `696,120.13` | `94.33` | `97.42` | `323.95` | -2,053,084.51 USD | `-3.03%` | `7X Cross` |
| `18` | `0x9c6a...a4ed` | `LONG` | 53,493,277.41 USD | `550,087.69` | `80.86` | `97.42` | `68.18` | 9,014,291.03 USD | `+16.85%` | `20X Cross` |
| `49` | `0xb83d...6e36` | `SHORT` | 25,222,178.47 USD | `259,338.02` | `91.42` | `97.42` | `597.83` | -1,513,364.43 USD | `-6.00%` | `5X Cross` |
| `79` | `0x3dc9...54b0` | `SHORT` | 21,386,812.47 USD | `220,000.19` | `105.90` | `97.42` | `175.44` | 1,912,294.81 USD | `+8.94%` | `20X Cross` |
| `109` | `0x9c89...600e` | `LONG` | 18,395,316.61 USD | `189,472.50` | `115.21` | `97.42` | `35.01` | -3,433,698.65 USD | `-18.67%` | `20X Cross` |
| `117` | `0x4a20...3c26` | `LONG` | 17,493,660.00 USD | `180,000.00` | `106.43` | `97.42` | `69.72` | -1,664,618.71 USD | `-9.52%` | `20X Cross` |
| `160` | `0xecb6...2b00` | `SHORT` | 12,853,123.17 USD | `132,119.60` | `101.25` | `97.42` | `333.55` | 523,917.42 USD | `+4.08%` | `20X Cross` |
| `226` | `0xc63a...a3cd` | `LONG` | 9,717,500.00 USD | `100,000.00` | `112.22` | `97.42` | `0.000000` | -1,504,608.97 USD | `-15.48%` | `20X Cross` |
| `227` | `0xb581...6f4f` | `LONG` | 9,710,700.00 USD | `100,000.00` | `112.81` | `97.42` | `0.000000` | -1,570,009.14 USD | `-16.17%` | `3X Cross` |
| `294` | `0x645b...87b8` | `SHORT` | 8,060,573.39 USD | `82,879.96` | `103.90` | `97.42` | `360.77` | 550,896.83 USD | `+6.83%` | `20X Cross` |
| `300` | `0xdb3a...cf3b` | `LONG` | 7,946,580.06 USD | `81,851.78` | `106.04` | `97.42` | `47.22` | -733,166.80 USD | `-9.23%` | `4X Cross` |
| `318` | `0xe927...98ef` | `LONG` | 7,582,590.60 USD | `78,000.00` | `96.34` | `97.42` | `38.45` | 68,449.12 USD | `+0.90%` | `3X Cross` |
| `325` | `0xca49...53c8` | `SHORT` | 7,186,194.19 USD | `73,943.45` | `110.70` | `97.42` | `302.46` | 999,428.07 USD | `+13.91%` | `20X Cross` |
| `330` | `0x8ae4...3d60` | `LONG` | 7,021,963.98 USD | `72,180.05` | `111.72` | `97.42` | `11.89` | -1,042,196.25 USD | `-14.84%` | `10X Cross` |
| `334` | `0xa0b7...6165` | `SHORT` | 6,907,648.96 USD | `71,044.42` | `107.87` | `97.42` | `190.91` | 755,818.24 USD | `+10.94%` | `2X Cross` |
| `352` | `0xf517...c032` | `SHORT` | 6,587,734.22 USD | `67,778.53` | `84.64` | `97.42` | `220.45` | -850,703.06 USD | `-12.91%` | `20X Cross` |
| `411` | `0x7fda...17d1` | `SHORT` | 5,433,432.03 USD | `55,851.24` | `100.53` | `97.42` | `790.62` | 181,502.55 USD | `+3.34%` | `20X Cross` |
| `468` | `0x7e23...5a5a` | `LONG` | 4,720,280.97 USD | `48,564.56` | `105.17` | `97.42` | `57.00` | -387,288.19 USD | `-8.20%` | `5X Isolated` |
| `540` | `0x7a5a...0394` | `SHORT` | 4,183,404.01 USD | `43,041.35` | `99.29` | `97.42` | `124.03` | 90,002.54 USD | `+2.15%` | `10X Cross` |
| `572` | `0xf899...88db` | `SHORT` | 3,959,954.07 USD | `40,716.81` | `88.40` | `97.42` | `109.13` | -360,681.20 USD | `-9.11%` | `20X Cross` |
| `592` | `0x2e2b...2fab` | `LONG` | 3,887,840.00 USD | `40,000.00` | `119.55` | `97.42` | `59.79` | -894,195.64 USD | `-23.00%` | `10X Cross` |
| `625` | `0x9c16...4a6f` | `SHORT` | 3,672,838.93 USD | `37,796.13` | `90.79` | `97.42` | `118.49` | -241,488.21 USD | `-6.57%` | `20X Cross` |
| `648` | `0x9946...0852` | `SHORT` | 3,508,698.68 USD | `36,099.58` | `110.82` | `97.42` | `141.24` | 491,887.71 USD | `+14.02%` | `20X Cross` |
| `650` | `0x27b8...12fc` | `LONG` | 3,504,158.94 USD | `36,085.73` | `110.86` | `97.42` | `24.43` | -496,186.31 USD | `-14.16%` | `10X Cross` |
| `675` | `0xa61c...66b9` | `LONG` | 3,347,275.28 USD | `34,438.76` | `102.78` | `97.42` | `0.000000` | -192,186.03 USD | `-5.74%` | `5X Cross` |
| `692` | `0x3440...32c5` | `SHORT` | 3,276,680.29 USD | `33,744.03` | `95.02` | `97.42` | `168.30` | -70,280.34 USD | `-2.14%` | `20X Cross` |
| `741` | `0x96a7...79df` | `LONG` | 3,110,806.40 USD | `32,000.00` | `74.39` | `97.42` | `0.000000` | 730,400.55 USD | `+23.48%` | `20X Cross` |
| `783` | `0xbe19...8bd1` | `SHORT` | 2,959,752.01 USD | `30,451.69` | `97.62` | `97.42` | `763.53` | 12,794.62 USD | `+0.43%` | `3X Cross` |
| `786` | `0x482b...cae4` | `SHORT` | 2,945,785.59 USD | `30,310.49` | `88.03` | `97.42` | `151.26` | -277,537.30 USD | `-9.42%` | `20X Cross` |
| `798` | `0x610b...b613` | `LONG` | 2,880,814.76 USD | `29,634.14` | `101.23` | `97.42` | `70.39` | -119,184.59 USD | `-4.14%` | `3X Isolated` |
| `806` | `0x023a...2355` | `SHORT` | 2,864,156.39 USD | `29,462.78` | `101.18` | `97.42` | `273.04` | 116,765.44 USD | `+4.08%` | `20X Cross` |
| `814` | `0x45d2...4029` | `SHORT` | 2,838,021.72 USD | `29,220.00` | `93.28` | `97.42` | `1580.15` | -112,245.74 USD | `-3.96%` | `20X Cross` |
| `863` | `0x458d...ab3b` | `LONG` | 2,662,172.71 USD | `27,385.03` | `117.17` | `97.42` | `81.08` | -546,489.81 USD | `-20.53%` | `3X Isolated` |
| `924` | `0x051c...693c` | `LONG` | 2,443,898.11 USD | `25,139.70` | `89.76` | `97.42` | `44.96` | 187,336.79 USD | `+7.67%` | `20X Cross` |
| `941` | `0xfc27...9d9d` | `SHORT` | 2,386,190.71 USD | `24,528.09` | `100.40` | `97.42` | `855.24` | 76,322.43 USD | `+3.20%` | `20X Cross` |
| `965` | `0x638f...f5f0` | `LONG` | 2,331,480.00 USD | `24,000.00` | `136.71` | `97.42` | `51.19` | -949,488.54 USD | `-40.72%` | `20X Cross` |
| `1010` | `0x7277...0b98` | `SHORT` | 2,213,202.07 USD | `22,770.74` | `99.32` | `97.42` | `159.67` | 48,401.68 USD | `+2.19%` | `20X Cross` |
| `1022` | `0x7178...0854` | `LONG` | 2,189,300.62 USD | `22,545.24` | `110.94` | `97.42` | `40.17` | -311,843.85 USD | `-14.24%` | `10X Cross` |
| `1049` | `0x69cc...14fd` | `SHORT` | 2,109,284.10 USD | `21,701.57` | `99.01` | `97.42` | `472.17` | 39,368.65 USD | `+1.87%` | `20X Cross` |
| `1053` | `0x739c...cfb2` | `LONG` | 2,090,073.05 USD | `21,500.00` | `91.95` | `97.42` | `75.52` | 113,140.90 USD | `+5.41%` | `20X Cross` |
| `1116` | `0x7737...bf66` | `SHORT` | 1,982,247.91 USD | `20,384.06` | `102.94` | `97.42` | `983.11` | 116,093.98 USD | `+5.86%` | `10X Cross` |
| `1144` | `0xbfc7...80b4` | `SHORT` | 1,945,120.00 USD | `20,000.00` | `85.98` | `97.42` | `175.45` | -225,585.50 USD | `-11.60%` | `20X Cross` |
| `1145` | `0x3fc5...c0c1` | `SHORT` | 1,944,254.00 USD | `20,000.00` | `98.28` | `97.42` | `186.47` | 21,305.84 USD | `+1.10%` | `20X Cross` |
| `1146` | `0xea00...a918` | `LONG` | 1,943,942.90 USD | `20,022.69` | `66.09` | `97.42` | `0.000000` | 620,634.31 USD | `+31.93%` | `20X Cross` |
| `1147` | `0x251f...6e5d` | `LONG` | 1,943,900.00 USD | `20,000.00` | `101.15` | `97.42` | `70.82` | -79,197.77 USD | `-4.07%` | `20X Cross` |
| `1181` | `0x7160...d47c` | `LONG` | 1,888,897.35 USD | `19,434.10` | `105.03` | `97.42` | `76.25` | -152,323.94 USD | `-8.06%` | `20X Cross` |
| `1198` | `0x936c...bb0f` | `SHORT` | 1,847,317.12 USD | `18,988.91` | `105.57` | `97.42` | `530.45` | 157,370.57 USD | `+8.52%` | `20X Cross` |
| `1200` | `0xe097...d0fe` | `LONG` | 1,845,912.01 USD | `18,995.75` | `109.71` | `97.42` | `0.000000` | -238,084.88 USD | `-12.90%` | `20X Cross` |
| `1280` | `0xdf95...7d72` | `SHORT` | 1,731,407.72 USD | `17,802.58` | `104.53` | `97.42` | `2295.04` | 129,549.13 USD | `+7.48%` | `20X Cross` |
| `1293` | `0xe98b...8cd5` | `SHORT` | 1,713,473.59 USD | `17,622.89` | `187.95` | `97.42` | `262.47` | 1,598,747.13 USD | `+93.30%` | `20X Cross` |
| `1326` | `0xee2b...d67e` | `LONG` | 1,648,737.25 USD | `16,963.19` | `119.86` | `97.42` | `34.04` | -384,534.39 USD | `-23.32%` | `4X Cross` |
| `1335` | `0x123d...3bff` | `LONG` | 1,636,604.97 USD | `16,835.30` | `89.54` | `97.42` | `0.000000` | 129,163.71 USD | `+7.89%` | `10X Cross` |
| `1436` | `0x73d7...8be1` | `LONG` | 1,522,786.91 USD | `15,668.95` | `106.60` | `97.42` | `49.71` | -147,554.06 USD | `-9.69%` | `20X Cross` |
| `1453` | `0xc74a...ab93` | `LONG` | 1,510,878.06 USD | `15,536.82` | `64.06` | `97.42` | `54.88` | 515,649.23 USD | `+34.13%` | `5X Isolated` |
| `1485` | `0x5f10...d49d` | `LONG` | 1,457,925.00 USD | `15,000.00` | `96.35` | `97.42` | `72.02` | 12,623.84 USD | `+0.87%` | `20X Cross` |
| `1486` | `0xb322...d51f` | `LONG` | 1,457,907.50 USD | `14,999.82` | `102.98` | `97.42` | `43.71` | -86,819.80 USD | `-5.96%` | `20X Cross` |
| `1536` | `0xffb2...5ed6` | `LONG` | 1,408,154.70 USD | `14,504.05` | `117.89` | `97.42` | `84.52` | -301,750.01 USD | `-21.43%` | `20X Cross` |
| `1560` | `0x0d6a...ca57` | `LONG` | 1,380,829.55 USD | `14,206.65` | `110.41` | `97.42` | `91.60` | -187,760.80 USD | `-13.60%` | `5X Isolated` |
| `1778` | `0x2814...9b08` | `LONG` | 1,172,108.73 USD | `12,061.71` | `96.37` | `97.42` | `93.93` | 9,769.99 USD | `+0.83%` | `20X Isolated` |
| `1850` | `0x7808...6e70` | `SHORT` | 1,115,361.67 USD | `11,488.27` | `97.15` | `97.42` | `152.10` | 700.55 USD | `+0.06%` | `10X Cross` |
| `1867` | `0x2482...0e55` | `LONG` | 1,104,533.40 USD | `11,363.98` | `122.03` | `97.42` | `88.83` | -282,168.52 USD | `-25.55%` | `20X Isolated` |
| `1898` | `0x45db...86eb` | `LONG` | 1,078,542.60 USD | `11,100.00` | `110.69` | `97.42` | `69.15` | -150,139.30 USD | `-13.92%` | `5X Cross` |
| `1926` | `0x1d04...7c43` | `LONG` | 1,051,227.42 USD | `10,811.76` | `111.55` | `97.42` | `17.23` | -154,834.07 USD | `-14.73%` | `6X Cross` |
| `1944` | `0x34e6...8d74` | `LONG` | 1,037,075.71 USD | `10,671.15` | `101.19` | `97.42` | `15.56` | -42,698.93 USD | `-4.12%` | `20X Cross` |
| `2004` | `0x2577...4897` | `LONG` | 1,004,367.57 USD | `10,327.05` | `96.54` | `97.42` | `0.000000` | 7,371.13 USD | `+0.73%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `100.72` | 3,101.17 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.10K USD at 100.7200 USD [API] | `2026-10-18 19:41:08` |
| `ANNOUNCEMENT` | `INFO` | `100.72` | 1,874.40 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.87K USD at 100.7200 USD [API] | `2026-10-18 19:41:08` |
| `ANNOUNCEMENT` | `INFO` | `100.72` | 179.28 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.18K USD at 100.7200 USD [API] | `2026-10-18 19:41:08` |
| `ANNOUNCEMENT` | `INFO` | `100.72` | 1,380.87 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.38K USD at 100.7200 USD [API] | `2026-10-18 19:41:08` |
| `ANNOUNCEMENT` | `INFO` | `100.72` | 12.09 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 100.7200 USD [API] | `2026-10-18 19:41:08` |
| `ANNOUNCEMENT` | `INFO` | `100.72` | 1,380.87 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.38K USD at 100.7200 USD [API] | `2026-10-18 19:41:08` |
| `ANNOUNCEMENT` | `INFO` | `100.72` | 2,143.32 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.14K USD at 100.7200 USD [API] | `2026-10-18 19:41:08` |
| `ANNOUNCEMENT` | `INFO` | `100.13` | 59,164.81 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 59.16K USD at 100.1300 USD [API] | `2026-10-29 09:30:31` |
| `ANNOUNCEMENT` | `INFO` | `100.31` | 34,002.08 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 34.00K USD at 100.3100 USD [API] | `2026-10-29 09:58:06` |
| `ANNOUNCEMENT` | `INFO` | `100.55` | 25,634.22 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 25.63K USD at 100.5500 USD [API] | `2026-10-29 10:48:31` |
| `ANNOUNCEMENT` | `INFO` | `100.53` | 2.01 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.00K USD at 100.5300 USD [API] | `2026-10-29 11:50:52` |
| `ANNOUNCEMENT` | `INFO` | `100.20` | 25,159.22 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 25.16K USD at 100.2000 USD [API] | `2026-10-29 12:11:24` |
| `ANNOUNCEMENT` | `INFO` | `100.30` | 44,051.76 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 44.05K USD at 100.3000 USD [API] | `2026-10-29 12:19:01` |
| `ANNOUNCEMENT` | `INFO` | `100.43` | 20,001.64 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 20.00K USD at 100.4300 USD [API] | `2026-10-29 12:29:43` |
| `ANNOUNCEMENT` | `INFO` | `100.68` | 22,375.12 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 22.38K USD at 100.6800 USD [API] | `2026-10-29 13:05:41` |
| `ANNOUNCEMENT` | `INFO` | `100.75` | 37,574.71 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 37.57K USD at 100.7500 USD [API] | `2026-10-29 13:18:58` |
| `ANNOUNCEMENT` | `INFO` | `100.48` | 36,538.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 36.54K USD at 100.4800 USD [API] | `2026-10-29 13:53:35` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`101.22` (Vol: 4,800,000.00 USD, Dist: `+4.28%`) | Long MP=`92.18` (Vol: 5,300,000.00 USD, Dist: `--5.04%`)
  * 48H Horizon: Short MP=`101.12` (Vol: 5,400,000.00 USD, Dist: `+4.18%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--5.05%`)
  * 3D Horizon: Short MP=`101.12` (Vol: 5,400,000.00 USD, Dist: `+4.18%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--5.05%`)
  * 7D Horizon: Short MP=`104.03` (Vol: 7,200,000.00 USD, Dist: `+7.17%`) | Long MP=`92.11` (Vol: 5,300,000.00 USD, Dist: `--5.11%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `19.45` | 3,100.00 USD | 122,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.55` | 449.65 USD | 122,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.65` | 514.44 USD | 122,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.05` | 897.84 USD | 122,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.15` | 730.44 USD | 122,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.55` | 12,190.00 USD | 122,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.85` | 689.93 USD | 122,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.95` | 1,030.00 USD | 122,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 1,410.00 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 407.55 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.75` | 4,630.00 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.95` | 1,100.00 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.05` | 4,740.00 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.35` | 2,040.00 USD | 122,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.65` | 112.12 USD | 122,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.95` | 1,150.00 USD | 122,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.15` | 11,820.00 USD | 122,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.25` | 838,990.00 USD | 122,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.35` | 46,700.00 USD | 121,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.45` | 1,380.00 USD | 121,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.65` | 9,830.00 USD | 121,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 1,570.00 USD | 121,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 9,590.00 USD | 121,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.25` | 248.81 USD | 121,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 882.72 USD | 121,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.75` | 976.88 USD | 121,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.85` | 5,360.00 USD | 121,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.95` | 25,960.00 USD | 121,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.05` | 1,250.00 USD | 121,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.15` | 3,270.00 USD | 121,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.45` | 106.64 USD | 121,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.65` | 147,500.00 USD | 121,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.75` | 309.00 USD | 121,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 3,320.00 USD | 121,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.05` | 5,730.00 USD | 121,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.25` | 136.24 USD | 121,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.35` | 366.79 USD | 121,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.45` | 1,710.00 USD | 121,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.65` | 265.17 USD | 121,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 10,110.00 USD | 121,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.35` | 332.30 USD | 121,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.75` | 1,190.00 USD | 121,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.85` | 14,980.00 USD | 121,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 154.28 USD | 121,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.05` | 2,740.00 USD | 121,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.15` | 271.37 USD | 121,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.25` | 755.12 USD | 121,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.35` | 6,200.00 USD | 121,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 113.80 USD | 121,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.05` | 11,030.00 USD | 121,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 15,270.00 USD | 121,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.25` | 88,480.00 USD | 121,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.35` | 9,900.00 USD | 121,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.45` | 151.96 USD | 121,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 33,370.00 USD | 121,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.95` | 18,960.00 USD | 121,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 5,410.00 USD | 121,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.15` | 50,050.00 USD | 121,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.25` | 47,800.00 USD | 121,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.35` | 4,230.00 USD | 120,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 889.01 USD | 120,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 5,250.00 USD | 120,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.85` | 157.64 USD | 120,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.05` | 621.00 USD | 120,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 178.49 USD | 120,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.35` | 6,120.00 USD | 120,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.45` | 278.33 USD | 120,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 162.17 USD | 120,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.75` | 11,130.00 USD | 120,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 796.68 USD | 120,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.25` | 173.50 USD | 120,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 861.87 USD | 120,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 1,150.00 USD | 120,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 562,480.00 USD | 120,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.95` | 1,160.00 USD | 120,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.05` | 5,420.00 USD | 120,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.25` | 39,900.00 USD | 120,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 1,830.00 USD | 120,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.75` | 72,700.00 USD | 120,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 3,650.00 USD | 120,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 19,990.00 USD | 120,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.25` | 799.05 USD | 120,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.35` | 982.41 USD | 120,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.55` | 17,270.00 USD | 120,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 486.14 USD | 120,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.75` | 143.86 USD | 120,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.85` | 3,660.00 USD | 120,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 6,620,000.00 USD | 120,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.15` | 441.84 USD | 113,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.25` | 1,360.00 USD | 113,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.65` | 3,040.00 USD | 113,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.75` | 4,840.00 USD | 113,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.85` | 9,050.00 USD | 113,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.95` | 557.94 USD | 113,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.05` | 5,070.00 USD | 113,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.15` | 531.41 USD | 113,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.25` | 2,630.00 USD | 113,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 5,630.00 USD | 113,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 42,810.00 USD | 113,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.55` | 50,420.00 USD | 113,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 748.97 USD | 113,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.85` | 1,470.00 USD | 113,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.95` | 1,660.00 USD | 113,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 146.37 USD | 113,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 373.62 USD | 113,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 38,140.00 USD | 113,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 144,730.00 USD | 113,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.65` | 4,610.00 USD | 113,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 636.09 USD | 113,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 819.83 USD | 113,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 5,000.00 USD | 113,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 1,490.00 USD | 113,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 480.42 USD | 113,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 287.63 USD | 113,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 3,000,000.00 USD | 113,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 17,850.00 USD | 110,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 6,130.00 USD | 110,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 194,490.00 USD | 110,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.85` | 4,270.00 USD | 110,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 607.62 USD | 110,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 933,530.00 USD | 110,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 194.18 USD | 109,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 4,930.00 USD | 109,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 258.40 USD | 109,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 11,970.00 USD | 109,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 159.00 USD | 109,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 1,270.00 USD | 109,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 13,530.00 USD | 109,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.15` | 2,510.00 USD | 109,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.25` | 632.73 USD | 109,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.35` | 51,650.00 USD | 109,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,970.00 USD | 109,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 3,160.00 USD | 109,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 12,650.00 USD | 109,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 581.49 USD | 109,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 5,220.00 USD | 109,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 1,070.00 USD | 109,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 368.36 USD | 109,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.35` | 148.45 USD | 109,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 130.88 USD | 109,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 770.11 USD | 109,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.75` | 588.26 USD | 109,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 1,020.00 USD | 109,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 389,980.00 USD | 109,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 20,830.00 USD | 108,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 2,790.00 USD | 108,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 3,050.00 USD | 108,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 6,460.00 USD | 108,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.45` | 106.12 USD | 108,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 8,230.00 USD | 108,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 44,750.00 USD | 108,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 1,620.00 USD | 108,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 1,400.00 USD | 108,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 2,040.00 USD | 108,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 1,080.00 USD | 108,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 4,710.00 USD | 108,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 440.15 USD | 108,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.55` | 2,180.00 USD | 108,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 6,530.00 USD | 108,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 1,170,000.00 USD | 108,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 219,360.00 USD | 107,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 10,340.00 USD | 107,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.05` | 12,870.00 USD | 107,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 662,360.00 USD | 107,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 6,550.00 USD | 106,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 2,380.00 USD | 106,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.45` | 10,180.00 USD | 106,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 20,540.00 USD | 106,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 4,880.00 USD | 106,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 1,790.00 USD | 106,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 477.20 USD | 106,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 3,690,000.00 USD | 106,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 179.70 USD | 102,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 67,560.00 USD | 102,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 9,480.00 USD | 102,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 7,940.00 USD | 102,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 866.89 USD | 102,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 9,780.00 USD | 102,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.85` | 458.50 USD | 102,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 26,070.00 USD | 102,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 9,760.00 USD | 102,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.15` | 714.40 USD | 102,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 824.95 USD | 102,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 685.68 USD | 102,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 542.07 USD | 102,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.75` | 374.00 USD | 102,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 543.93 USD | 102,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 2,090.00 USD | 102,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 1,160.00 USD | 102,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 13,380.00 USD | 102,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 502.50 USD | 102,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 106.04 USD | 102,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.65` | 98,780.00 USD | 102,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 56,650.00 USD | 102,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.85` | 473.72 USD | 102,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.95` | 3,360.00 USD | 102,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 13,580.00 USD | 102,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 16,260.00 USD | 102,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 2,430.00 USD | 102,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.35` | 9,290.00 USD | 102,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.45` | 764,270.00 USD | 102,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 97,400.00 USD | 101,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 10,720.00 USD | 101,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 2,330.00 USD | 101,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.85` | 17,060.00 USD | 101,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,490.00 USD | 101,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,120.00 USD | 101,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.25` | 21,190.00 USD | 101,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 585.29 USD | 101,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 17,090.00 USD | 101,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 627.80 USD | 101,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 8,890.00 USD | 101,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.75` | 2,650.00 USD | 101,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.85` | 41,540.00 USD | 101,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 29,590.00 USD | 101,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 9,750.00 USD | 101,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.15` | 5,850.00 USD | 101,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 1,210,000.00 USD | 101,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.35` | 8,240.00 USD | 100,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,800.00 USD | 100,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 12,940.00 USD | 100,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.65` | 1,270.00 USD | 100,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 13,300.00 USD | 100,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.85` | 20,760.00 USD | 100,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 5,110.00 USD | 100,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.05` | 3,470.00 USD | 100,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.15` | 2,620.00 USD | 100,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.25` | 10,940.00 USD | 100,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.35` | 4,340.00 USD | 100,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.45` | 3,920.00 USD | 100,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.55` | 135,270.00 USD | 100,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.65` | 4,290.00 USD | 99,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.75` | 24,770.00 USD | 99,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.85` | 46,110.00 USD | 99,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.95` | 469,860.00 USD | 99,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.05` | 31,030.00 USD | 99,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.15` | 112,570.00 USD | 99,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.25` | 12,600.00 USD | 99,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.35` | 2,160.00 USD | 99,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.45` | 43,640.00 USD | 99,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.55` | 11,110.00 USD | 99,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.65` | 9,300.00 USD | 99,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.75` | 3,180.00 USD | 99,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.85` | 9,370.00 USD | 99,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.95` | 6,120.00 USD | 99,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.05` | 5,120.00 USD | 99,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.15` | 3,340.00 USD | 99,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.25` | 24,120.00 USD | 99,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.35` | 2,130.00 USD | 99,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.45` | 52,360.00 USD | 99,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.55` | 44,480.00 USD | 99,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.65` | 230.70 USD | 98,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.75` | 3,600.00 USD | 98,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.85` | 19,810.00 USD | 98,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.95` | 58,760.00 USD | 98,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.05` | 350.78 USD | 98,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.15` | 14,640.00 USD | 98,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.25` | 6,660.00 USD | 98,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.35` | 11,720.00 USD | 98,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.45` | 1,410.00 USD | 98,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.55` | 61,670.00 USD | 98,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.65` | 10,920.00 USD | 98,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.75` | 15,140.00 USD | 98,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.85` | 861,080.00 USD | 98,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.95` | 142,480.00 USD | 97,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.05` | 552.70 USD | 97,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.15` | 665.66 USD | 97,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.25` | 2,010.00 USD | 97,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.35` | 9,920.00 USD | 97,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.45` | 5,620.00 USD | 97,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.55` | 145,530.00 USD | 97,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.65` | 11,490.00 USD | 97,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.75` | 91,720.00 USD | 97,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.85` | 18,770.00 USD | 97,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.95` | 7,050.00 USD | 97,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.05` | 5,640.00 USD | 97,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.15` | 38,930.00 USD | 97,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.25` | 13,300.00 USD | 97,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.35` | 12,890.00 USD | 97,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.45` | 13,320.00 USD | 97,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.55` | 4,730.00 USD | 97,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.65` | 3,190.00 USD | 97,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.75` | 9,410.00 USD | 97,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.85` | 28,550.00 USD | 97,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.95` | 14,320.00 USD | 97,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.05` | 2,770,000.00 USD | 97,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.15` | 5,380.00 USD | 94,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.25` | 2,470.00 USD | 94,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.35` | 7,120.00 USD | 94,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.45` | 19,200.00 USD | 94,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.55` | 8,510.00 USD | 94,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.65` | 13,030.00 USD | 94,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.75` | 8,290.00 USD | 94,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.85` | 22,150.00 USD | 94,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.95` | 10,870.00 USD | 94,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.05` | 39,250.00 USD | 94,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.15` | 125,030.00 USD | 94,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.25` | 9,870.00 USD | 94,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.35` | 30,840.00 USD | 94,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.45` | 697.31 USD | 94,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.55` | 4,680.00 USD | 94,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.65` | 4,690.00 USD | 94,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.75` | 14,500.00 USD | 94,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.85` | 13,970.00 USD | 94,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.95` | 31,930.00 USD | 94,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.05` | 65,660.00 USD | 94,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.15` | 2,370,000.00 USD | 94,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.25` | 1,990.00 USD | 91,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.35` | 28,500.00 USD | 91,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.45` | 4,830.00 USD | 91,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.55` | 26,470.00 USD | 91,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.65` | 3,640.00 USD | 91,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.75` | 13,290.00 USD | 91,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.85` | 28,800.00 USD | 91,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.95` | 38,940.00 USD | 91,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.05` | 55,060.00 USD | 91,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.15` | 35,380.00 USD | 91,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.25` | 20,380.00 USD | 91,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.35` | 4,540.00 USD | 91,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.55` | 10,140.00 USD | 91,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.65` | 711.42 USD | 91,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.75` | 5,300.00 USD | 91,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.85` | 33,430.00 USD | 91,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.95` | 57,890.00 USD | 91,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.05` | 4,520.00 USD | 91,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.15` | 5,900.00 USD | 91,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.25` | 4,630.00 USD | 91,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.35` | 11,660.00 USD | 91,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.45` | 20,920.00 USD | 91,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.55` | 651.20 USD | 91,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.65` | 19,270.00 USD | 91,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.75` | 109,820.00 USD | 91,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.85` | 24,050.00 USD | 91,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.95` | 4,680.00 USD | 91,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.05` | 53,350.00 USD | 91,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.15` | 25,350.00 USD | 91,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.25` | 47,880.00 USD | 91,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.35` | 20,220.00 USD | 91,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.45` | 67,320.00 USD | 91,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.55` | 135,200.00 USD | 90,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.65` | 2,630.00 USD | 90,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.75` | 3,140.00 USD | 90,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.85` | 31,310.00 USD | 90,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.95` | 9,610.00 USD | 90,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.05` | 16,070.00 USD | 90,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.15` | 82,790.00 USD | 90,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.25` | 32,790.00 USD | 90,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.35` | 1,200.00 USD | 90,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.45` | 291.24 USD | 90,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.55` | 49,290.00 USD | 90,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.65` | 416.27 USD | 90,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.75` | 32,540.00 USD | 90,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.85` | 37,610.00 USD | 90,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.95` | 19,530.00 USD | 90,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.05` | 796.78 USD | 90,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.15` | 35,280.00 USD | 90,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.25` | 5,090.00 USD | 90,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.35` | 875.16 USD | 90,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.45` | 4,310.00 USD | 90,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.55` | 579.66 USD | 90,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.65` | 2,220.00 USD | 90,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.75` | 16,300.00 USD | 90,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.85` | 396.23 USD | 90,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.95` | 209.79 USD | 90,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.05` | 265,650.00 USD | 90,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.15` | 108,780.00 USD | 90,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.25` | 13,060.00 USD | 90,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.35` | 39,610.00 USD | 90,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.45` | 3,450.00 USD | 90,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.55` | 10,470.00 USD | 89,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.65` | 58,270.00 USD | 89,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.75` | 5,050.00 USD | 89,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.85` | 1,300.00 USD | 89,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.95` | 5,780.00 USD | 89,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.05` | 6,490.00 USD | 89,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.15` | 20,170.00 USD | 89,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.25` | 14,930.00 USD | 89,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.35` | 1,600.00 USD | 89,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.45` | 75,010.00 USD | 89,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.55` | 52,610.00 USD | 89,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.65` | 40,710.00 USD | 89,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.75` | 43,110.00 USD | 89,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.85` | 20,000.00 USD | 89,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.95` | 937.30 USD | 89,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.05` | 46,770.00 USD | 89,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.15` | 3,620.00 USD | 89,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.25` | 248.83 USD | 89,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.35` | 1,880.00 USD | 89,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.45` | 22,250.00 USD | 89,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.55` | 53,380.00 USD | 89,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.65` | 129,430.00 USD | 89,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.75` | 30,820.00 USD | 89,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.85` | 28,740.00 USD | 89,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.05` | 11,140.00 USD | 89,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.15` | 37,490,000.00 USD | 89,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.25` | 17,190.00 USD | 51,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.35` | 2,860.00 USD | 51,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.45` | 18,610.00 USD | 51,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.55` | 1,380,000.00 USD | 51,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.65` | 7,740.00 USD | 50,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.75` | 151,610.00 USD | 50,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.85` | 417,630.00 USD | 50,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.95` | 46,330.00 USD | 49,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.05` | 786,930.00 USD | 49,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.15` | 29,000.00 USD | 48,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.25` | 20,140.00 USD | 48,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.35` | 12,490,000.00 USD | 48,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.45` | 264,310.00 USD | 36,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.55` | 10,170.00 USD | 36,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.65` | 5,280.00 USD | 36,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.75` | 212,170.00 USD | 36,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.85` | 8,590.00 USD | 35,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.95` | 8,800.00 USD | 35,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.05` | 496,560.00 USD | 35,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.15` | 4,120.00 USD | 35,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.25` | 72,890.00 USD | 35,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.35` | 2,140,000.00 USD | 35,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.45` | 113,800.00 USD | 33,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.55` | 458.58 USD | 33,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.65` | 49,010.00 USD | 33,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.75` | 10,240.00 USD | 33,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.85` | 15,430.00 USD | 33,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.95` | 7,010.00 USD | 33,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.05` | 31,630.00 USD | 33,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.15` | 69,160.00 USD | 33,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.25` | 1,080,000.00 USD | 32,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.35` | 15,910.00 USD | 31,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.45` | 31,640.00 USD | 31,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.55` | 41,780.00 USD | 31,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.65` | 894.91 USD | 31,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.75` | 30,200.00 USD | 31,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.85` | 2,130.00 USD | 31,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.95` | 12,860.00 USD | 31,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.05` | 42,610.00 USD | 31,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.15` | 130,700.00 USD | 31,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.25` | 259,270.00 USD | 31,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.35` | 29,390.00 USD | 31,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.45` | 2,240.00 USD | 31,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.55` | 16,450.00 USD | 31,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.65` | 33,720.00 USD | 31,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.75` | 3,100.00 USD | 31,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.85` | 186,830.00 USD | 31,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.95` | 18,610.00 USD | 31,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.05` | 7,310.00 USD | 30,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.15` | 17,140.00 USD | 30,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.25` | 28,470.00 USD | 30,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.35` | 8,280.00 USD | 30,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.45` | 5,350.00 USD | 30,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.55` | 17,060.00 USD | 30,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.65` | 38,360.00 USD | 30,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.75` | 77,660.00 USD | 30,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.85` | 11,710.00 USD | 30,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.95` | 40,040.00 USD | 30,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.05` | 38,460.00 USD | 30,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.15` | 21,430.00 USD | 30,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.25` | 41,310.00 USD | 30,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.35` | 24,920.00 USD | 30,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.45` | 22,920.00 USD | 30,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.55` | 11,550.00 USD | 30,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.65` | 1,030.00 USD | 30,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.75` | 46,150.00 USD | 30,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.85` | 127,450.00 USD | 30,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.95` | 19,860.00 USD | 30,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.05` | 48,410.00 USD | 30,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.15` | 2,430.00 USD | 30,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.25` | 1,910,000.00 USD | 30,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.35` | 18,360.00 USD | 28,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.45` | 33,560.00 USD | 28,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.55` | 29,130.00 USD | 28,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.65` | 130,250.00 USD | 28,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.75` | 1,550,000.00 USD | 28,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.85` | 4,110.00 USD | 26,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.95` | 27,920.00 USD | 26,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.05` | 8,540.00 USD | 26,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.15` | 17,050.00 USD | 26,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.25` | 9,710.00 USD | 26,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.35` | 35,800.00 USD | 26,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.45` | 1,990.00 USD | 26,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.55` | 68,230.00 USD | 26,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.65` | 57,460.00 USD | 26,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.75` | 5,060.00 USD | 26,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.85` | 134,060.00 USD | 26,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.95` | 29,250.00 USD | 26,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.05` | 80,420.00 USD | 26,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.15` | 257,230.00 USD | 26,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.25` | 32,190.00 USD | 25,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.35` | 8,780.00 USD | 25,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.45` | 52,110.00 USD | 25,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.55` | 12,900.00 USD | 25,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.75` | 9,870.00 USD | 25,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.85` | 59,570.00 USD | 25,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.95` | 14,550.00 USD | 25,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.05` | 21,880.00 USD | 25,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.15` | 63,910.00 USD | 25,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.25` | 39,070.00 USD | 25,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.35` | 55,060.00 USD | 25,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.45` | 26,080.00 USD | 25,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.55` | 5,910.00 USD | 25,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.65` | 32,860.00 USD | 25,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.75` | 60,550.00 USD | 25,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.85` | 62,050.00 USD | 25,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.95` | 1,370.00 USD | 25,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.05` | 6,870.00 USD | 25,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.15` | 128,420.00 USD | 25,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.25` | 59,390.00 USD | 25,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.35` | 25,940.00 USD | 25,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.45` | 11,960.00 USD | 25,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.55` | 1,900.00 USD | 25,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.65` | 19,720.00 USD | 25,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.75` | 85,820.00 USD | 25,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.85` | 171,770.00 USD | 25,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.95` | 29,580.00 USD | 24,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.05` | 8,660.00 USD | 24,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.15` | 59,220.00 USD | 24,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.25` | 76,330.00 USD | 24,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.35` | 113,360.00 USD | 24,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.45` | 12,930.00 USD | 24,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.55` | 8,000.00 USD | 24,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.65` | 94,280.00 USD | 24,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.75` | 26,360.00 USD | 24,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.85` | 440,510.00 USD | 24,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.95` | 10,620.00 USD | 24,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.05` | 2,230,000.00 USD | 23,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.15` | 136,780.00 USD | 21,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.25` | 31,500.00 USD | 21,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.35` | 56,470.00 USD | 21,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.45` | 59,690.00 USD | 21,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.55` | 68,180.00 USD | 21,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.65` | 36,930.00 USD | 21,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.75` | 18,650.00 USD | 21,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.85` | 37,600.00 USD | 21,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.95` | 22,190.00 USD | 21,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.05` | 117,060.00 USD | 21,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.15` | 804,530.00 USD | 21,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.25` | 41,530.00 USD | 20,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.35` | 162,250.00 USD | 20,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.45` | 213,390.00 USD | 20,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.55` | 390,360.00 USD | 19,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `82.60` | 171,490,000.00 USD | 171,490,000.00 USD | 53,130.00 USD | 56,870.00 USD | 141,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `82.65` | 106,090.00 USD | 19,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.75` | 41,050.00 USD | 19,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `82.80` | 171,240,000.00 USD | 171,240,000.00 USD | 1,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `82.85` | 20,820.00 USD | 19,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.95` | 24,190.00 USD | 19,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.00` | 171,230,000.00 USD | 171,230,000.00 USD | 1,690.00 USD | 2,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.05` | 99,450.00 USD | 19,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.15` | 758,900.00 USD | 19,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.20` | 171,230,000.00 USD | 171,230,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.25` | 158,960.00 USD | 18,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.35` | 263,640.00 USD | 18,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.40` | 171,190,000.00 USD | 171,190,000.00 USD | 0.00 USD | 0.00 USD | 579.46 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.45` | 54,780.00 USD | 18,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.55` | 65,570.00 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.60` | 171,190,000.00 USD | 171,190,000.00 USD | 0.00 USD | 0.00 USD | 86,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.65` | 79,520.00 USD | 17,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.75` | 89,170.00 USD | 17,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.80` | 171,100,000.00 USD | 171,100,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.85` | 13,820.00 USD | 17,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.95` | 103,880.00 USD | 17,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.05` | 124,350.00 USD | 17,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.15` | 65,530.00 USD | 17,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.20` | 171,090,000.00 USD | 171,090,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.25` | 204,990.00 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.35` | 25,180.00 USD | 17,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.40` | 171,070,000.00 USD | 171,070,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.45` | 86,250.00 USD | 17,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.55` | 2,300.00 USD | 17,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.65` | 101,540.00 USD | 17,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.75` | 289,310.00 USD | 17,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.85` | 94,350.00 USD | 16,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.95` | 1,800.00 USD | 16,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.05` | 15,480.00 USD | 16,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.15` | 1,240,000.00 USD | 16,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.20` | 171,040,000.00 USD | 171,040,000.00 USD | 0.00 USD | 218,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.25` | 609,970.00 USD | 15,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.35` | 21,130.00 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.40` | 170,830,000.00 USD | 170,830,000.00 USD | 0.00 USD | 12,950.00 USD | 192,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.45` | 57,870.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.55` | 63,600.00 USD | 14,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.60` | 170,620,000.00 USD | 170,620,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.65` | 43,310.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.75` | 9,950.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.80` | 170,430,000.00 USD | 170,430,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.85` | 70,970.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.95` | 361,960.00 USD | 14,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.05` | 276,690.00 USD | 14,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.15` | 51,580.00 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.20` | 170,170,000.00 USD | 170,170,000.00 USD | 0.00 USD | 12,130.00 USD | 199,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.25` | 29,040.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.35` | 5,680.00 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.40` | 169,960,000.00 USD | 169,960,000.00 USD | 0.00 USD | 311,220.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.45` | 108,330.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.55` | 60,140.00 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.65` | 190,730.00 USD | 13,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.75` | 34,820.00 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.80` | 169,640,000.00 USD | 169,640,000.00 USD | 0.00 USD | 149,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.85` | 92,320.00 USD | 13,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.95` | 152,510.00 USD | 13,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.00` | 169,490,000.00 USD | 169,490,000.00 USD | 263,340.00 USD | 176,600.00 USD | 297,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.05` | 31,140.00 USD | 13,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.15` | 4,410.00 USD | 13,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.20` | 174,240,000.00 USD | 174,240,000.00 USD | 129,420.00 USD | 138,340.00 USD | 351,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.20` | 168,760,000.00 USD | 168,760,000.00 USD | 8,850.00 USD | 0.00 USD | 6,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.25` | 92,780.00 USD | 13,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.35` | 100,830.00 USD | 13,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.40` | 173,620,000.00 USD | 173,620,000.00 USD | 30,080.00 USD | 232,930.00 USD | 109,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.40` | 168,740,000.00 USD | 168,740,000.00 USD | 248,310.00 USD | 217,060.00 USD | 288,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.45` | 156,920.00 USD | 12,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.55` | 243,070.00 USD | 12,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.60` | 173,250,000.00 USD | 173,250,000.00 USD | 105,350.00 USD | 295,330.00 USD | 57,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.60` | 167,990,000.00 USD | 167,990,000.00 USD | 0.00 USD | 275,130.00 USD | 421,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.65` | 108,400.00 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.75` | 28,570.00 USD | 12,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.80` | 172,790,000.00 USD | 172,790,000.00 USD | 90,150.00 USD | 276,230.00 USD | 716,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.80` | 167,290,000.00 USD | 167,290,000.00 USD | 0.00 USD | 413,150.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.85` | 72,180.00 USD | 12,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.95` | 6,600.00 USD | 12,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.00` | 171,710,000.00 USD | 171,710,000.00 USD | 47,860.00 USD | 202,660.00 USD | 485,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.00` | 166,870,000.00 USD | 166,870,000.00 USD | 0.00 USD | 12,070.00 USD | 251,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.05` | 154,390.00 USD | 12,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.15` | 37,310.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.20` | 170,970,000.00 USD | 170,970,000.00 USD | 140,490.00 USD | 168,390.00 USD | 365,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.20` | 166,600,000.00 USD | 166,600,000.00 USD | 9,900.00 USD | 20,610.00 USD | 28,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.25` | 68,850.00 USD | 12,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.35` | 91,590.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.40` | 170,300,000.00 USD | 170,300,000.00 USD | 84,680.00 USD | 178,840.00 USD | 65,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.40` | 166,540,000.00 USD | 166,540,000.00 USD | 0.00 USD | 237,870.00 USD | 335,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.45` | 69,390.00 USD | 11,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.55` | 242,620.00 USD | 11,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.60` | 169,970,000.00 USD | 169,970,000.00 USD | 68,370.00 USD | 64,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.65` | 95,980.00 USD | 11,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.75` | 167,190.00 USD | 11,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.80` | 169,840,000.00 USD | 169,840,000.00 USD | 304,990.00 USD | 175,710.00 USD | 415,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.80` | 165,970,000.00 USD | 165,970,000.00 USD | 241,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.85` | 1,090,000.00 USD | 11,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.95` | 48,800.00 USD | 10,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.00` | 168,940,000.00 USD | 168,940,000.00 USD | 8,600.00 USD | 11,540.00 USD | 227,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.00` | 165,730,000.00 USD | 165,730,000.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.05` | 24,630.00 USD | 10,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.15` | 119,730.00 USD | 10,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.20` | 168,690,000.00 USD | 168,690,000.00 USD | 377,030.00 USD | 119,090.00 USD | 11,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.20` | 164,800,000.00 USD | 164,800,000.00 USD | 8,180.00 USD | 10,750.00 USD | 315,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.25` | 31,740.00 USD | 10,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.35` | 47,410.00 USD | 10,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.40` | 168,180,000.00 USD | 168,180,000.00 USD | 5,150.00 USD | 292,120.00 USD | 274,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.40` | 164,460,000.00 USD | 164,460,000.00 USD | 697,470.00 USD | 26,220.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.45` | 488,780.00 USD | 10,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.55` | 36,300.00 USD | 9,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.60` | 167,610,000.00 USD | 167,610,000.00 USD | 138,450.00 USD | 5,250.00 USD | 135,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.60` | 163,580,000.00 USD | 163,580,000.00 USD | 684,220.00 USD | 270,260.00 USD | 723,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.65` | 15,430.00 USD | 9,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.75` | 122,670.00 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.80` | 167,330,000.00 USD | 167,330,000.00 USD | 54,220.00 USD | 91,280.00 USD | 440,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.80` | 161,900,000.00 USD | 161,900,000.00 USD | 425,950.00 USD | 318,390.00 USD | 314,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.85` | 71,950.00 USD | 9,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.95` | 81,650.00 USD | 9,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.00` | 166,750,000.00 USD | 166,750,000.00 USD | 686,700.00 USD | 302,220.00 USD | 278,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.00` | 160,840,000.00 USD | 160,840,000.00 USD | 374,600.00 USD | 647,410.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.05` | 30,300.00 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.15` | 60,240.00 USD | 9,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.20` | 165,480,000.00 USD | 165,480,000.00 USD | 822,890.00 USD | 930,230.00 USD | 363,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.20` | 158,720,000.00 USD | 158,720,000.00 USD | 1,250,000.00 USD | 590,390.00 USD | 735,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.25` | 35,780.00 USD | 9,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.35` | 79,990.00 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.40` | 163,360,000.00 USD | 163,360,000.00 USD | 779,410.00 USD | 544,380.00 USD | 671,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.40` | 156,140,000.00 USD | 156,140,000.00 USD | 796,240.00 USD | 68,740.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.45` | 64,160.00 USD | 9,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.55` | 54,910.00 USD | 8,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.60` | 161,370,000.00 USD | 161,370,000.00 USD | 676,760.00 USD | 671,710.00 USD | 840,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.60` | 154,580,000.00 USD | 154,580,000.00 USD | 1,040,000.00 USD | 1,010,000.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.65` | 114,260.00 USD | 8,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.75` | 84,750.00 USD | 8,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.80` | 159,180,000.00 USD | 159,180,000.00 USD | 404,570.00 USD | 518,670.00 USD | 250,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.80` | 150,970,000.00 USD | 150,970,000.00 USD | 1,210,000.00 USD | 1,200,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.85` | 94,780.00 USD | 8,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.95` | 31,540.00 USD | 8,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.00` | 158,010,000.00 USD | 158,010,000.00 USD | 1,020,000.00 USD | 597,650.00 USD | 483,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.00` | 147,080,000.00 USD | 147,080,000.00 USD | 1,190,000.00 USD | 609,900.00 USD | 810,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.05` | 389,480.00 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.15` | 293,530.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.20` | 155,900,000.00 USD | 155,900,000.00 USD | 16,980.00 USD | 493,060.00 USD | 403,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.20` | 144,470,000.00 USD | 144,470,000.00 USD | 2,280,000.00 USD | 868,420.00 USD | 638,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.25` | 30,390.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.35` | 14,960.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.40` | 154,990,000.00 USD | 154,990,000.00 USD | 664,720.00 USD | 758,110.00 USD | 111,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.40` | 140,690,000.00 USD | 140,690,000.00 USD | 1,180,000.00 USD | 1,030,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.45` | 309,360.00 USD | 7,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.55` | 1,210,000.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.60` | 153,450,000.00 USD | 153,450,000.00 USD | 488,750.00 USD | 281,460.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.60` | 136,870,000.00 USD | 136,870,000.00 USD | 500,280.00 USD | 1,020,000.00 USD | 872,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.65` | 1,430,000.00 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.75` | 237,960.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.80` | 151,580,000.00 USD | 151,580,000.00 USD | 526,140.00 USD | 449,000.00 USD | 713,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.80` | 134,480,000.00 USD | 134,480,000.00 USD | 932,400.00 USD | 797,110.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.85` | 46,220.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.95` | 64,120.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.00` | 149,890,000.00 USD | 149,890,000.00 USD | 2,810,000.00 USD | 2,220,000.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.00` | 132,060,000.00 USD | 132,060,000.00 USD | 681,440.00 USD | 656,110.00 USD | 990,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.05` | 192,580.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.15` | 328,220.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.20` | 143,750,000.00 USD | 143,750,000.00 USD | 887,260.00 USD | 1,630,000.00 USD | 465,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.20` | 129,730,000.00 USD | 129,730,000.00 USD | 2,870,000.00 USD | 1,110,000.00 USD | 289,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.25` | 225,070.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.35` | 308,200.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.40` | 140,770,000.00 USD | 140,770,000.00 USD | 731,980.00 USD | 331,330.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.40` | 125,470,000.00 USD | 125,470,000.00 USD | 550,500.00 USD | 833,900.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.45` | 117,820.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.55` | 4,870.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.60` | 137,540,000.00 USD | 137,540,000.00 USD | 1,330,000.00 USD | 1,530,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.60` | 122,540,000.00 USD | 122,540,000.00 USD | 98,670.00 USD | 880,990.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.65` | 14,980.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.75` | 5,120.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.80` | 132,260,000.00 USD | 132,260,000.00 USD | 1,940,000.00 USD | 824,500.00 USD | 775,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.80` | 120,090,000.00 USD | 120,090,000.00 USD | 422,920.00 USD | 2,340,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.85` | 337,230.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.95` | 3,780.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.00` | 128,720,000.00 USD | 128,720,000.00 USD | 2,640,000.00 USD | 3,760,000.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.00` | 115,710,000.00 USD | 115,710,000.00 USD | 35,740.00 USD | 393,980.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.05` | 29,770.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.15` | 2,810.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.20` | 119,280,000.00 USD | 119,280,000.00 USD | 2,380,000.00 USD | 1,620,000.00 USD | 1,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.20` | 114,020,000.00 USD | 114,020,000.00 USD | 921,350.00 USD | 650,760.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.25` | 38,840.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.35` | 12,570.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.40` | 113,350,000.00 USD | 113,350,000.00 USD | 3,070,000.00 USD | 3,100,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.40` | 110,320,000.00 USD | 110,320,000.00 USD | 611,840.00 USD | 2,520,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.45` | 7,320.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.55` | 19,840.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.60` | 104,880,000.00 USD | 104,880,000.00 USD | 1,950,000.00 USD | 3,880,000.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.60` | 105,750,000.00 USD | 105,750,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.65` | 3,240.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.75` | 942,560.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.80` | 97,980,000.00 USD | 97,980,000.00 USD | 1,010,000.00 USD | 1,030,000.00 USD | 483,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.80` | 102,810,000.00 USD | 102,810,000.00 USD | 0.00 USD | 2,080,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.85` | 7,310.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.95` | 1,140,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.00` | 95,460,000.00 USD | 95,460,000.00 USD | 759,420.00 USD | 1,060,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.00` | 97,560,000.00 USD | 97,560,000.00 USD | 2,660,000.00 USD | 1,780,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.15` | 33,550.00 USD | 821,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.20` | 91,820,000.00 USD | 91,820,000.00 USD | 1,980,000.00 USD | 1,940,000.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.20` | 90,910,000.00 USD | 90,910,000.00 USD | 24,740.00 USD | 962,410.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.25` | 8,860.00 USD | 788,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.35` | 5,200.00 USD | 779,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.40` | 85,730,000.00 USD | 85,730,000.00 USD | 1,650,000.00 USD | 568,640.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.40` | 87,170,000.00 USD | 87,170,000.00 USD | 0.00 USD | 496,790.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.45` | 146,220.00 USD | 774,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.55` | 97,340.00 USD | 627,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.60` | 82,510,000.00 USD | 82,510,000.00 USD | 142,910.00 USD | 1,380,000.00 USD | 396,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.60` | 86,660,000.00 USD | 86,660,000.00 USD | 560,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.65` | 2,690.00 USD | 530,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.75` | 33,140.00 USD | 527,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.80` | 80,590,000.00 USD | 80,590,000.00 USD | 2,800,000.00 USD | 553,660.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.80` | 86,100,000.00 USD | 86,100,000.00 USD | 2,010,000.00 USD | 99,300.00 USD | 3,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.85` | 52,310.00 USD | 494,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.95` | 13,860.00 USD | 442,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.00` | 76,020,000.00 USD | 76,020,000.00 USD | 3,210,000.00 USD | 673,040.00 USD | 25,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.00` | 80,630,000.00 USD | 80,630,000.00 USD | 2,400,000.00 USD | 4,460,000.00 USD | 47,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.05` | 77,030.00 USD | 428,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.15` | 25,120.00 USD | 351,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.20` | 72,110,000.00 USD | 72,110,000.00 USD | 1,030,000.00 USD | 1,780,000.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.20` | 73,730,000.00 USD | 73,730,000.00 USD | 2,080,000.00 USD | 277,550.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.25` | 32,200.00 USD | 326,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.35` | 8,070.00 USD | 294,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.40` | 66,270,000.00 USD | 66,270,000.00 USD | 1,120,000.00 USD | 1,820,000.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.40` | 71,350,000.00 USD | 71,350,000.00 USD | 2,080,000.00 USD | 2,340,000.00 USD | 4,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.45` | 23,290.00 USD | 286,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.55` | 48,980.00 USD | 262,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.60` | 62,160,000.00 USD | 62,160,000.00 USD | 1,850,000.00 USD | 2,410,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.60` | 62,340,000.00 USD | 62,340,000.00 USD | 3,820,000.00 USD | 7,040,000.00 USD | 4,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.65` | 93,140.00 USD | 213,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.75` | 84,480.00 USD | 120,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.80` | 56,770,000.00 USD | 56,770,000.00 USD | 571,180.00 USD | 1,020,000.00 USD | 5,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.80` | 46,890,000.00 USD | 46,890,000.00 USD | 3,400,000.00 USD | 93,510.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.85` | 32,540.00 USD | 36,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.95` | 231.24 USD | 3,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.00` | 49,260,000.00 USD | 49,260,000.00 USD | 3,070,000.00 USD | 2,590,000.00 USD | 4,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.00` | 42,130,000.00 USD | 42,130,000.00 USD | 2,670,000.00 USD | 728,410.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.05` | 2,210.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.15` | 345.18 USD | 1,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.20` | 39,020,000.00 USD | 39,020,000.00 USD | 5,210,000.00 USD | 6,860,000.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.20` | 35,140,000.00 USD | 35,140,000.00 USD | 6,840,000.00 USD | 2,140,000.00 USD | 5,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.35` | 964.46 USD | 964.46 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.40` | 25,520,000.00 USD | 25,520,000.00 USD | 4,170,000.00 USD | 2,150,000.00 USD | 4,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.40` | 20,910,000.00 USD | 20,910,000.00 USD | 1,600,000.00 USD | 2,590,000.00 USD | 6,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.60` | 14,580,000.00 USD | 14,580,000.00 USD | 1,410,000.00 USD | 2,010,000.00 USD | 299,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.60` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.80` | 10,860,000.00 USD | 10,860,000.00 USD | 1,350,000.00 USD | 2,230,000.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.80` | 10,230,000.00 USD | 10,230,000.00 USD | 0.00 USD | 79,170.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.00` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 1,410,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.00` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 2,240,000.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.20` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 87,380.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.40` | 2,110,000.00 USD | 2,110,000.00 USD | 534,370.00 USD | 1,280,000.00 USD | 292,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.40` | 4,210,000.00 USD | 4,210,000.00 USD | 534,370.00 USD | 1,280,000.00 USD | 292,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.40` | 101,560.00 USD | 101,560.00 USD | 0.00 USD | 101,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.40` | 203,120.00 USD | 203,120.00 USD | 0.00 USD | 101,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.45` | 331.33 USD | 331.33 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.60` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.60` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 24,930.00 USD | 3,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.80` | 6,990,000.00 USD | 6,990,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.80` | 15,160,000.00 USD | 15,160,000.00 USD | 7,580,000.00 USD | 3,430,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.00` | 8,490,000.00 USD | 8,490,000.00 USD | 773,040.00 USD | 407,460.00 USD | 320,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.00` | 26,590,000.00 USD | 26,590,000.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.20` | 13,930,000.00 USD | 13,930,000.00 USD | 2,200,000.00 USD | 1,790,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.20` | 36,930,000.00 USD | 36,930,000.00 USD | 9,790,000.00 USD | 555,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.40` | 24,730,000.00 USD | 24,730,000.00 USD | 772,180.00 USD | 311,650.00 USD | 9,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.40` | 48,060,000.00 USD | 48,060,000.00 USD | 1,780,000.00 USD | 3,320,000.00 USD | 6,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.55` | 5,930.00 USD | 6,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.60` | 37,960,000.00 USD | 37,960,000.00 USD | 488,190.00 USD | 5,730,000.00 USD | 7,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.60` | 57,290,000.00 USD | 57,290,000.00 USD | 1,880,000.00 USD | 5,400,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.65` | 9,740.00 USD | 16,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.80` | 49,510,000.00 USD | 49,510,000.00 USD | 1,400,000.00 USD | 4,160,000.00 USD | 6,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.80` | 60,250,000.00 USD | 60,250,000.00 USD | 71,480.00 USD | 470,960.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.95` | 1,020.00 USD | 17,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.00` | 63,670,000.00 USD | 63,670,000.00 USD | 2,810,000.00 USD | 5,870,000.00 USD | 5,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.00` | 68,700,000.00 USD | 68,700,000.00 USD | 1,830,000.00 USD | 2,660,000.00 USD | 3,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.05` | 5,640.00 USD | 22,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.15` | 1,110,000.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.20` | 74,680,000.00 USD | 74,680,000.00 USD | 2,840,000.00 USD | 4,520,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.20` | 82,390,000.00 USD | 82,390,000.00 USD | 1,220,000.00 USD | 6,240,000.00 USD | 6,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.25` | 7,330.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.35` | 64,750.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.40` | 81,590,000.00 USD | 81,590,000.00 USD | 3,580,000.00 USD | 1,650,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.40` | 83,430,000.00 USD | 83,430,000.00 USD | 0.00 USD | 1,010,000.00 USD | 25,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.45` | 335.15 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.55` | 11,890.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.60` | 98,340,000.00 USD | 98,340,000.00 USD | 2,920,000.00 USD | 6,720,000.00 USD | 7,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.60` | 88,860,000.00 USD | 88,860,000.00 USD | 2,240,000.00 USD | 2,640,000.00 USD | 545,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.65` | 1,130.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.75` | 25,520.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.80` | 113,290,000.00 USD | 113,290,000.00 USD | 2,520,000.00 USD | 4,590,000.00 USD | 7,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.80` | 92,190,000.00 USD | 92,190,000.00 USD | 736,270.00 USD | 1,330,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.85` | 238.64 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.95` | 3,070.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.00` | 123,750,000.00 USD | 123,750,000.00 USD | 2,850,000.00 USD | 3,360,000.00 USD | 4,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.00` | 103,520,000.00 USD | 103,520,000.00 USD | 2,220,000.00 USD | 2,310,000.00 USD | 6,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.05` | 32,030.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.15` | 33,940.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.20` | 126,920,000.00 USD | 126,920,000.00 USD | 651,800.00 USD | 2,130,000.00 USD | 388,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.20` | 109,600,000.00 USD | 109,600,000.00 USD | 843,770.00 USD | 2,460,000.00 USD | 2,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.25` | 345,350.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.35` | 410,700.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.40` | 132,670,000.00 USD | 132,670,000.00 USD | 976,110.00 USD | 1,790,000.00 USD | 2,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.40` | 114,080,000.00 USD | 114,080,000.00 USD | 993,830.00 USD | 654,600.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.45` | 26,900.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.55` | 41,910.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.60` | 143,310,000.00 USD | 143,310,000.00 USD | 2,220,000.00 USD | 1,710,000.00 USD | 6,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.60` | 119,860,000.00 USD | 119,860,000.00 USD | 2,110,000.00 USD | 1,450,000.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.65` | 102,960.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.75` | 19,590.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.80` | 148,760,000.00 USD | 148,760,000.00 USD | 1,990,000.00 USD | 1,820,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.80` | 121,600,000.00 USD | 121,600,000.00 USD | 491,210.00 USD | 1,220,000.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.95` | 498.69 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.00` | 158,930,000.00 USD | 158,930,000.00 USD | 5,730,000.00 USD | 3,220,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.00` | 140,380,000.00 USD | 140,380,000.00 USD | 4,000,000.00 USD | 7,040,000.00 USD | 7,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.05` | 168.75 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.15` | 12,350.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.20` | 171,650,000.00 USD | 171,650,000.00 USD | 5,410,000.00 USD | 4,390,000.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.20` | 159,650,000.00 USD | 159,650,000.00 USD | 7,240,000.00 USD | 5,180,000.00 USD | 6,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.25` | 769.50 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.40` | 182,320,000.00 USD | 182,320,000.00 USD | 3,860,000.00 USD | 2,700,000.00 USD | 4,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.40` | 176,710,000.00 USD | 176,710,000.00 USD | 4,720,000.00 USD | 1,270,000.00 USD | 11,070,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.45` | 1,340.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.55` | 2,790.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.60` | 198,130,000.00 USD | 198,130,000.00 USD | 3,100,000.00 USD | 2,930,000.00 USD | 9,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.60` | 187,230,000.00 USD | 187,230,000.00 USD | 3,650,000.00 USD | 30,170.00 USD | 6,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.65` | 2,640.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.80` | 204,350,000.00 USD | 204,350,000.00 USD | 646,170.00 USD | 836,200.00 USD | 4,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.80` | 197,160,000.00 USD | 197,160,000.00 USD | 3,050,000.00 USD | 609,510.00 USD | 6,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.85` | 8,240.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.95` | 1,760.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.00` | 210,630,000.00 USD | 210,630,000.00 USD | 2,520,000.00 USD | 1,780,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.00` | 203,150,000.00 USD | 203,150,000.00 USD | 1,830,000.00 USD | 1,470,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.05` | 5,220.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.20` | 216,980,000.00 USD | 216,980,000.00 USD | 3,180,000.00 USD | 1,360,000.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.20` | 209,870,000.00 USD | 209,870,000.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.25` | 1,170.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.35` | 720.54 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.40` | 221,480,000.00 USD | 221,480,000.00 USD | 1,560,000.00 USD | 716,320.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.40` | 215,180,000.00 USD | 215,180,000.00 USD | 2,340,000.00 USD | 304,350.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.45` | 175.19 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.55` | 6,330.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.60` | 224,110,000.00 USD | 224,110,000.00 USD | 985,660.00 USD | 606,030.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.60` | 217,640,000.00 USD | 217,640,000.00 USD | 1,450,000.00 USD | 979,270.00 USD | 33,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.65` | 1,070.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.75` | 3,340.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.80` | 228,160,000.00 USD | 228,160,000.00 USD | 1,260,000.00 USD | 1,570,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.80` | 225,730,000.00 USD | 225,730,000.00 USD | 7,780,000.00 USD | 23,810.00 USD | 286,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.95` | 4,150.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.00` | 233,220,000.00 USD | 233,220,000.00 USD | 3,120,000.00 USD | 1,440,000.00 USD | 498,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.00` | 242,660,000.00 USD | 242,660,000.00 USD | 12,270,000.00 USD | 394,420.00 USD | 4,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.05` | 692.50 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.15` | 11,000.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.20` | 235,590,000.00 USD | 235,590,000.00 USD | 301,000.00 USD | 853,780.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.20` | 255,340,000.00 USD | 255,340,000.00 USD | 11,620,000.00 USD | 140,550.00 USD | 913,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.25` | 859.04 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.35` | 385.50 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.40` | 238,510,000.00 USD | 238,510,000.00 USD | 867,130.00 USD | 1,180,000.00 USD | 877,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.40` | 269,910,000.00 USD | 269,910,000.00 USD | 11,050,000.00 USD | 233,330.00 USD | 3,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.45` | 14,540.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.60` | 246,140,000.00 USD | 246,140,000.00 USD | 2,430,000.00 USD | 183,360.00 USD | 5,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.60` | 288,300,000.00 USD | 288,300,000.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.65` | 4,360.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.75` | 261,050.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.80` | 249,300,000.00 USD | 249,300,000.00 USD | 481,980.00 USD | 1,320,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.80` | 300,680,000.00 USD | 300,680,000.00 USD | 7,960,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.85` | 14,220.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.95` | 827.44 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.00` | 255,150,000.00 USD | 255,150,000.00 USD | 2,410,000.00 USD | 1,540,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.00` | 327,390,000.00 USD | 327,390,000.00 USD | 10,830,000.00 USD | 7,160,000.00 USD | 8,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.05` | 775.17 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.15` | 1,180.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.20` | 258,570,000.00 USD | 258,570,000.00 USD | 1,440,000.00 USD | 931,620.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.20` | 349,410,000.00 USD | 349,410,000.00 USD | 8,520,000.00 USD | 7,230,000.00 USD | 6,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.25` | 722.45 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.35` | 11,820.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.40` | 263,420,000.00 USD | 263,420,000.00 USD | 1,860,000.00 USD | 1,510,000.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.40` | 366,600,000.00 USD | 366,600,000.00 USD | 5,100,000.00 USD | 3,710,000.00 USD | 8,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.45` | 12,640.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.55` | 360.70 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.60` | 267,660,000.00 USD | 267,660,000.00 USD | 1,060,000.00 USD | 868,480.00 USD | 2,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.60` | 384,350,000.00 USD | 384,350,000.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 7,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.65` | 401.86 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.75` | 199.02 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.80` | 271,680,000.00 USD | 271,680,000.00 USD | 1,250,000.00 USD | 820,470.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.80` | 401,740,000.00 USD | 401,740,000.00 USD | 5,170,000.00 USD | 4,410,000.00 USD | 7,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.85` | 3,430.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.95` | 126,060.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.00` | 272,900,000.00 USD | 272,900,000.00 USD | 463,890.00 USD | 350,040.00 USD | 413,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.00` | 417,900,000.00 USD | 417,900,000.00 USD | 5,730,000.00 USD | 4,110,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.05` | 2,800.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.15` | 21,880.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.20` | 273,970,000.00 USD | 273,970,000.00 USD | 111,930.00 USD | 94,030.00 USD | 864,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.20` | 428,570,000.00 USD | 428,570,000.00 USD | 5,340,000.00 USD | 2,800,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.25` | 2,860.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.35` | 6,840.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.40` | 274,450,000.00 USD | 274,450,000.00 USD | 262,490.00 USD | 138,720.00 USD | 78,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.40` | 436,790,000.00 USD | 436,790,000.00 USD | 1,570,000.00 USD | 3,170,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.45` | 531,450.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.55` | 5,240.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.60` | 274,880,000.00 USD | 274,880,000.00 USD | 130,280.00 USD | 187,950.00 USD | 110,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.60` | 447,170,000.00 USD | 447,170,000.00 USD | 3,700,000.00 USD | 2,700,000.00 USD | 3,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.65` | 1,740.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.80` | 275,570,000.00 USD | 275,570,000.00 USD | 87,540.00 USD | 526,970.00 USD | 76,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.80` | 455,980,000.00 USD | 455,980,000.00 USD | 2,690,000.00 USD | 2,620,000.00 USD | 3,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.85` | 92,920.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.95` | 592.26 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.00` | 276,730,000.00 USD | 276,730,000.00 USD | 372,000.00 USD | 554,120.00 USD | 226,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.00` | 461,130,000.00 USD | 461,130,000.00 USD | 1,970,000.00 USD | 1,050,000.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.05` | 33,380.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.15` | 248.39 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.20` | 278,140,000.00 USD | 278,140,000.00 USD | 623,340.00 USD | 349,490.00 USD | 440,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.20` | 470,020,000.00 USD | 470,020,000.00 USD | 3,820,000.00 USD | 2,560,000.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.35` | 256,250.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.40` | 278,870,000.00 USD | 278,870,000.00 USD | 181,780.00 USD | 354,890.00 USD | 197,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.40` | 476,080,000.00 USD | 476,080,000.00 USD | 2,420,000.00 USD | 2,170,000.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.45` | 34,730.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.55` | 105.48 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.60` | 280,550,000.00 USD | 280,550,000.00 USD | 388,660.00 USD | 278,100.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.60` | 481,900,000.00 USD | 481,900,000.00 USD | 1,330,000.00 USD | 1,460,000.00 USD | 3,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.65` | 6,360.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.80` | 281,930,000.00 USD | 281,930,000.00 USD | 340,680.00 USD | 316,760.00 USD | 718,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.80` | 486,540,000.00 USD | 486,540,000.00 USD | 999,190.00 USD | 918,930.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.85` | 479,130.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.95` | 37,730.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.00` | 282,690,000.00 USD | 282,690,000.00 USD | 193,920.00 USD | 413,830.00 USD | 147,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.00` | 490,680,000.00 USD | 490,680,000.00 USD | 527,980.00 USD | 1,180,000.00 USD | 2,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.05` | 14,600.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.15` | 3,060.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.20` | 283,170,000.00 USD | 283,170,000.00 USD | 0.00 USD | 50,140.00 USD | 436,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.20` | 491,770,000.00 USD | 491,770,000.00 USD | 230,020.00 USD | 507,570.00 USD | 352,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.25` | 35,230.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.35` | 766.48 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.40` | 284,010,000.00 USD | 284,010,000.00 USD | 90,150.00 USD | 226,090.00 USD | 523,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.40` | 493,060,000.00 USD | 493,060,000.00 USD | 0.00 USD | 576,040.00 USD | 709,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.45` | 32,580.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.55` | 11,910.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.60` | 284,750,000.00 USD | 284,750,000.00 USD | 47,860.00 USD | 202,660.00 USD | 485,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.60` | 493,690,000.00 USD | 493,690,000.00 USD | 213,520.00 USD | 12,070.00 USD | 406,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.80` | 285,420,000.00 USD | 285,420,000.00 USD | 140,490.00 USD | 168,390.00 USD | 365,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.80` | 494,530,000.00 USD | 494,530,000.00 USD | 499,550.00 USD | 31,020.00 USD | 305,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.85` | 143,340.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.95` | 17,360.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.00` | 285,750,000.00 USD | 285,750,000.00 USD | 84,680.00 USD | 178,840.00 USD | 65,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.00` | 495,110,000.00 USD | 495,110,000.00 USD | 5,950.00 USD | 237,870.00 USD | 335,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.05` | 1,080.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.15` | 1,150.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.20` | 285,880,000.00 USD | 285,880,000.00 USD | 68,370.00 USD | 62,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.20` | 495,390,000.00 USD | 495,390,000.00 USD | 0.00 USD | 205,080.00 USD | 74,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.25` | 38,000.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.35` | 3,470.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.40` | 495,880,000.00 USD | 495,880,000.00 USD | 487,890.00 USD | 0.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.45` | 108,080.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.55` | 117.23 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.60` | 496,060,000.00 USD | 496,060,000.00 USD | 17,470.00 USD | 167,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.65` | 5,050.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.75` | 2,120.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.80` | 497,490,000.00 USD | 497,490,000.00 USD | 350,210.00 USD | 397,420.00 USD | 674,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.85` | 3,230.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.95` | 3,170.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.00` | 497,780,000.00 USD | 497,780,000.00 USD | 8,180.00 USD | 0.00 USD | 286,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.05` | 163.58 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.25` | 131,370.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.35` | 247.13 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.45` | 202.48 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.55` | 408,340.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.65` | 38,640.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.85` | 3,190.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.95` | 301.26 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.05` | 14,560.00 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.15` | 194.97 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.25` | 195.14 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.35` | 158.90 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 143,580.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.55` | 203.41 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.65` | 38,290.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.85` | 1,090.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 4,450.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.15` | 1,710.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.35` | 390.84 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.45` | 841.45 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.55` | 892.40 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.65` | 3,220.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.75` | 169.86 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.85` | 15,880.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.95` | 223.90 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.15` | 528.23 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.35` | 61,610.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.45` | 5,670.00 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.55` | 844.13 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.65` | 707.44 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.75` | 118,640.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.85` | 108,760.00 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.05` | 406.98 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.15` | 9,560.00 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.25` | 698.75 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.35` | 4,120.00 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.45` | 3,360.00 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.55` | 263,860.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.65` | 105,510.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.75` | 5,200.00 USD | 6,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.85` | 104.74 USD | 6,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.95` | 21,840.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.05` | 31,740.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.25` | 2,150.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.45` | 3,830.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.55` | 7,090.00 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.65` | 3,430.00 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.05` | 569,550.00 USD | 6,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.15` | 1,100.00 USD | 6,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.25` | 161.35 USD | 6,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.45` | 893,760.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.55` | 167,330.00 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.75` | 160.89 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.85` | 289.62 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.05` | 4,450.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.25` | 180.19 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.35` | 4,960.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.55` | 2,040.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.65` | 113.15 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.85` | 1,520.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.05` | 156.85 USD | 7,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.15` | 90,390.00 USD | 8,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.25` | 225.12 USD | 8,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.35` | 4,790,000.00 USD | 12,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.55` | 188.08 USD | 12,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.65` | 47,200.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.75` | 20,960.00 USD | 12,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.95` | 353.85 USD | 12,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.25` | 4,470,000.00 USD | 17,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.45` | 30,080.00 USD | 17,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.55` | 7,700.00 USD | 17,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.75` | 309.94 USD | 17,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.25` | 240.88 USD | 17,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.35` | 57,850.00 USD | 17,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.45` | 27,900.00 USD | 17,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.55` | 8,970.00 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.65` | 1,760.00 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.75` | 731.67 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.85` | 485.39 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.95` | 4,200.00 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.05` | 96,110.00 USD | 17,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.15` | 2,980.00 USD | 17,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.45` | 145.74 USD | 17,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.55` | 1,190.00 USD | 17,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.65` | 60,330.00 USD | 17,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.95` | 13,290.00 USD | 17,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.15` | 316.20 USD | 17,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.25` | 1,550.00 USD | 17,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.55` | 6,460.00 USD | 17,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.75` | 105.92 USD | 17,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.05` | 56,150.00 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.15` | 169.79 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.25` | 883,070.00 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.45` | 17,500.00 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.65` | 116.52 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.25` | 472,220.00 USD | 19,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.35` | 2,330.00 USD | 19,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.45` | 126,270.00 USD | 19,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.65` | 6,680.00 USD | 19,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.05` | 586.76 USD | 19,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.15` | 121.67 USD | 19,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.25` | 23,360.00 USD | 19,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.35` | 29,710.00 USD | 19,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.45` | 46,110.00 USD | 19,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.55` | 3,080.00 USD | 19,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.65` | 675.60 USD | 19,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.75` | 6,020.00 USD | 19,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.95` | 3,500.00 USD | 19,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.05` | 208.83 USD | 19,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.15` | 462,650.00 USD | 19,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.35` | 5,320.00 USD | 19,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.45` | 590.87 USD | 19,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.55` | 4,610.00 USD | 19,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.65` | 1,560.00 USD | 19,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.75` | 1,930.00 USD | 19,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.85` | 57,880.00 USD | 19,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.95` | 110.84 USD | 19,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.05` | 810.50 USD | 19,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.15` | 470.54 USD | 19,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.35` | 4,090.00 USD | 19,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.45` | 5,000.00 USD | 19,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.65` | 30,830.00 USD | 19,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.75` | 10,650.00 USD | 19,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.85` | 3,870.00 USD | 19,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.05` | 262,490.00 USD | 20,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.15` | 389.08 USD | 20,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.35` | 6,610,000.00 USD | 26,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.55` | 139,870.00 USD | 26,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.65` | 4,840.00 USD | 26,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.75` | 20,800.00 USD | 26,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.85` | 388.66 USD | 26,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.95` | 10,510.00 USD | 27,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.05` | 116,190.00 USD | 27,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.35` | 195.09 USD | 27,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.45` | 783.54 USD | 27,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.65` | 788.62 USD | 27,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.75` | 18,730.00 USD | 27,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.85` | 32,440.00 USD | 27,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.15` | 55,570.00 USD | 27,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.25` | 32,310.00 USD | 27,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.35` | 699,390.00 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.55` | 2,590.00 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.75` | 71,060.00 USD | 28,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.85` | 490.83 USD | 28,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.25` | 13,200.00 USD | 28,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.35` | 145.99 USD | 28,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.65` | 866.21 USD | 28,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.75` | 132.06 USD | 28,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.85` | 3,180.00 USD | 28,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.95` | 2,070.00 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.05` | 188.71 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.25` | 1,560.00 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.45` | 219.52 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.85` | 3,100.00 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.95` | 3,710.00 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.05` | 11,940.00 USD | 28,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.15` | 325.09 USD | 28,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.55` | 8,730.00 USD | 28,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.65` | 240.10 USD | 28,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.85` | 49,280.00 USD | 28,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.05` | 30,050.00 USD | 28,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.15` | 10,040.00 USD | 28,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.25` | 1,330.00 USD | 28,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.35` | 390.72 USD | 28,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.65` | 156.37 USD | 28,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.75` | 151,200.00 USD | 28,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.95` | 503.65 USD | 28,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.05` | 12,620.00 USD | 28,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.25` | 11,590.00 USD | 28,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.65` | 67,330.00 USD | 28,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.35` | 414.17 USD | 28,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.75` | 6,420.00 USD | 28,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.85` | 3,250.00 USD | 28,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.95` | 49,400.00 USD | 28,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.15` | 14,640.00 USD | 28,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.35` | 8,690.00 USD | 28,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.55` | 136.55 USD | 28,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.65` | 1,110.00 USD | 28,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.75` | 4,090.00 USD | 28,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.95` | 34,240.00 USD | 28,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.05` | 836.00 USD | 28,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.15` | 2,220.00 USD | 28,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.35` | 18,410.00 USD | 28,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.55` | 697.38 USD | 28,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.95` | 2,050.00 USD | 28,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.05` | 4,090.00 USD | 28,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.15` | 41,450.00 USD | 28,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.25` | 45,220.00 USD | 28,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.45` | 7,310.00 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.75` | 2,360.00 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.15` | 552.43 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.35` | 4,180.00 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.45` | 253.80 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.55` | 494.01 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.65` | 1,680.00 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.75` | 4,870.00 USD | 28,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.95` | 394.66 USD | 28,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.05` | 116.24 USD | 28,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.35` | 158.60 USD | 28,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.45` | 4,870.00 USD | 28,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.55` | 1,330.00 USD | 28,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.65` | 7,340.00 USD | 28,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.85` | 5,160,000.00 USD | 33,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.95` | 1,940.00 USD | 33,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.05` | 3,080.00 USD | 33,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.35` | 210.61 USD | 33,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.45` | 247,540.00 USD | 34,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.55` | 1,950,000.00 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.65` | 211.06 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.75` | 4,780.00 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.95` | 23,020.00 USD | 36,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.05` | 782.70 USD | 36,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.25` | 3,470.00 USD | 36,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.45` | 151.00 USD | 36,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.75` | 368.30 USD | 36,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.15` | 90,580.00 USD | 36,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.25` | 2,830.00 USD | 36,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.35` | 64,570.00 USD | 36,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.55` | 103.36 USD | 36,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.95` | 597,390.00 USD | 36,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.05` | 3,750.00 USD | 36,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.15` | 23,300.00 USD | 36,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.55` | 602.77 USD | 36,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.65` | 3,260.00 USD | 36,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.75` | 72,380.00 USD | 36,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.15` | 1,760.00 USD | 36,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.35` | 106,270.00 USD | 37,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.45` | 28,990.00 USD | 37,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.65` | 145.65 USD | 37,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.85` | 5,850.00 USD | 37,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.95` | 490.39 USD | 37,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.15` | 88,760.00 USD | 37,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.25` | 4,050.00 USD | 37,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.35` | 7,330.00 USD | 37,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.55` | 17,380.00 USD | 37,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.65` | 587,730.00 USD | 37,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.75` | 2,110.00 USD | 37,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.95` | 78,060.00 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.05` | 166.17 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.15` | 1,730.00 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.35` | 169.45 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.45` | 204.96 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.55` | 1,000.00 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.65` | 237.72 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.85` | 578.09 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.15` | 122,350.00 USD | 37,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.25` | 78,630.00 USD | 38,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.35` | 445,050.00 USD | 38,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.45` | 519,740.00 USD | 39,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.55` | 373,600.00 USD | 39,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.65` | 5,650.00 USD | 39,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.75` | 93,700.00 USD | 39,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.05` | 1,120.00 USD | 39,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.35` | 1,390,000.00 USD | 40,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.55` | 116.65 USD | 40,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.65` | 16,030.00 USD | 40,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.95` | 234,200.00 USD | 41,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.05` | 5,200.00 USD | 41,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.15` | 123,300.00 USD | 41,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.85` | 346.96 USD | 41,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.95` | 2,370.00 USD | 41,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.15` | 3,180.00 USD | 41,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.45` | 8,830.00 USD | 41,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.55` | 1,740,000.00 USD | 43,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.95` | 1,110,000.00 USD | 44,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.05` | 4,610,000.00 USD | 48,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.15` | 44,670.00 USD | 48,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.25` | 400.42 USD | 48,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.35` | 287,690.00 USD | 49,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.45` | 5,950.00 USD | 49,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.55` | 757,860.00 USD | 49,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.75` | 1,570.00 USD | 49,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.95` | 925.35 USD | 49,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.05` | 1,060.00 USD | 49,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.15` | 44,610.00 USD | 49,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.25` | 239.07 USD | 49,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.35` | 2,300.00 USD | 49,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.45` | 1,230.00 USD | 49,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.65` | 8,340.00 USD | 49,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.85` | 1,490.00 USD | 49,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.15` | 292.89 USD | 49,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.25` | 2,340.00 USD | 49,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.45` | 4,240.00 USD | 49,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.75` | 363.66 USD | 49,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.05` | 117.84 USD | 49,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.25` | 1,110.00 USD | 49,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.35` | 2,810.00 USD | 49,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.55` | 267.55 USD | 49,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.05` | 326.14 USD | 49,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.15` | 7,810.00 USD | 49,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.35` | 197.00 USD | 49,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.45` | 4,900.00 USD | 49,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.05` | 80,150.00 USD | 50,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.15` | 49,270.00 USD | 50,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.65` | 654.25 USD | 50,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.75` | 92,600.00 USD | 50,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.85` | 237,070.00 USD | 50,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.35` | 23,570.00 USD | 50,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.65` | 428,360.00 USD | 50,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.75` | 3,610,000.00 USD | 54,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.05` | 145,990.00 USD | 54,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.25` | 654.52 USD | 54,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.65` | 1,760.00 USD | 54,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.95` | 497.44 USD | 54,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.15` | 683,000.00 USD | 55,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.25` | 80,940.00 USD | 55,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.35` | 655.83 USD | 55,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.55` | 28,140.00 USD | 55,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.05` | 2,240.00 USD | 55,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.35` | 1,530.00 USD | 55,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.45` | 322,900.00 USD | 55,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.55` | 410.34 USD | 55,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.65` | 86,120.00 USD | 55,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.75` | 18,940.00 USD | 55,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.95` | 5,840,000.00 USD | 61,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.35` | 6,500.00 USD | 61,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.45` | 142,860.00 USD | 61,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.55` | 24,150.00 USD | 61,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.55` | 23,440.00 USD | 61,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.85` | 786.48 USD | 61,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.95` | 208,190.00 USD | 62,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.75` | 677.12 USD | 62,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.15` | 198.18 USD | 62,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.15` | 1,620.00 USD | 62,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.25` | 14,070.00 USD | 62,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.65` | 67,790.00 USD | 62,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.95` | 3,440.00 USD | 62,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.15` | 17,120.00 USD | 62,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.55` | 150.80 USD | 62,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.65` | 115.68 USD | 62,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.75` | 1,890.00 USD | 62,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.95` | 4,090.00 USD | 62,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.05` | 122.68 USD | 62,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.35` | 19,740.00 USD | 62,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.65` | 437,600.00 USD | 62,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.05` | 34,790.00 USD | 62,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.35` | 443.70 USD | 62,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.55` | 335.71 USD | 62,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.75` | 3,180.00 USD | 62,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.95` | 181,510.00 USD | 62,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.45` | 111.44 USD | 62,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.55` | 1,180.00 USD | 62,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.75` | 20,440.00 USD | 62,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.45` | 51,730.00 USD | 62,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.65` | 27,960.00 USD | 62,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.35` | 204.55 USD | 62,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.45` | 16,540.00 USD | 62,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.75` | 284.95 USD | 62,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.85` | 695.40 USD | 62,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.95` | 346.16 USD | 62,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.15` | 104,490.00 USD | 63,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.25` | 245,010.00 USD | 63,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.35` | 205,490.00 USD | 63,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.75` | 146.79 USD | 63,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.85` | 38,470,000.00 USD | 102,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.15` | 238.20 USD | 102,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.45` | 119.31 USD | 102,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.75` | 263.62 USD | 102,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.85` | 105,510.00 USD | 102,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.95` | 19,890.00 USD | 102,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.05` | 123.23 USD | 102,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.25` | 625.69 USD | 102,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.35` | 3,530,000.00 USD | 105,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.65` | 25,540.00 USD | 105,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.75` | 1,300.00 USD | 105,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.85` | 4,420.00 USD | 105,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.55` | 267,040.00 USD | 105,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.65` | 4,320.00 USD | 105,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.75` | 208,810.00 USD | 106,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.85` | 277.45 USD | 106,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.95` | 78,300.00 USD | 106,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.05` | 142,440.00 USD | 106,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.05` | 4,970.00 USD | 106,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.65` | 44,930.00 USD | 106,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.85` | 1,040,000.00 USD | 107,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.15` | 1,340,000.00 USD | 108,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.55` | 38,150.00 USD | 108,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.25` | 19,490.00 USD | 108,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.55` | 254.17 USD | 108,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.05` | 91,030.00 USD | 108,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.15` | 3,990.00 USD | 108,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.35` | 72,940.00 USD | 109,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.45` | 9,440.00 USD | 109,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.05` | 3,660,000.00 USD | 112,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.15` | 793.69 USD | 112,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.25` | 1,680.00 USD | 112,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.95` | 165,230.00 USD | 112,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.15` | 7,670.00 USD | 112,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.25` | 737.29 USD | 112,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.45` | 56,050.00 USD | 112,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.55` | 1,220.00 USD | 112,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.65` | 11,090.00 USD | 112,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.85` | 2,190.00 USD | 112,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.55` | 232.56 USD | 112,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.75` | 2,460.00 USD | 112,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.85` | 14,260.00 USD | 112,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.15` | 997.20 USD | 112,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.55` | 231.92 USD | 112,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.65` | 29,110.00 USD | 113,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.75` | 4,070.00 USD | 113,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.95` | 1,450.00 USD | 113,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.25` | 456.09 USD | 113,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.85` | 189.85 USD | 113,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.95` | 284,930.00 USD | 113,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.15` | 148.32 USD | 113,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.45` | 118.08 USD | 113,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.55` | 118.14 USD | 113,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.95` | 13,570,000.00 USD | 126,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.35` | 68,210.00 USD | 126,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.85` | 383,700.00 USD | 127,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.95` | 514.43 USD | 127,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.15` | 872,340.00 USD | 128,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.25` | 280.69 USD | 128,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.15` | 2,170.00 USD | 128,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.55` | 114,580.00 USD | 128,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.05` | 19,910.00 USD | 128,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.15` | 1,380.00 USD | 128,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.25` | 9,380.00 USD | 128,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `19.45` | 123,110,000.00 USD | 0.00 USD | 11,880.00 USD | `-79.99%` | `610.74` |
| `Live` | `Long` | `19.65` | 123,100,000.00 USD | 0.00 USD | 55,020.00 USD | `-79.78%` | `2,800.00` |
| `Live` | `Long` | `19.85` | 123,040,000.00 USD | 0.00 USD | 468.46 USD | `-79.58%` | `23.60` |
| `Live` | `Long` | `19.95` | 123,040,000.00 USD | 0.00 USD | 379.05 USD | `-79.48%` | `19.00` |
| `Live` | `Long` | `20.25` | 123,040,000.00 USD | 0.00 USD | 167.26 USD | `-79.17%` | `8.26` |
| `Live` | `Long` | `20.55` | 123,040,000.00 USD | 0.00 USD | 4,790.00 USD | `-78.86%` | `233.31` |
| `Live` | `Long` | `20.65` | 123,040,000.00 USD | 0.00 USD | 748.56 USD | `-78.76%` | `36.25` |
| `Live` | `Long` | `21.15` | 123,030,000.00 USD | 0.00 USD | 994.47 USD | `-78.24%` | `47.02` |
| `Live` | `Long` | `21.35` | 123,030,000.00 USD | 0.00 USD | 3,470.00 USD | `-78.03%` | `162.52` |
| `Live` | `Long` | `21.45` | 123,030,000.00 USD | 0.00 USD | 161.73 USD | `-77.93%` | `7.54` |
| `Live` | `Long` | `21.65` | 123,030,000.00 USD | 0.00 USD | 631.10 USD | `-77.73%` | `29.15` |
| `Live` | `Long` | `21.75` | 123,030,000.00 USD | 0.00 USD | 4,630.00 USD | `-77.62%` | `212.70` |
| `Live` | `Long` | `21.95` | 123,020,000.00 USD | 0.00 USD | 1,800.00 USD | `-77.42%` | `82.04` |
| `Live` | `Long` | `22.05` | 123,020,000.00 USD | 0.00 USD | 1,080.00 USD | `-77.31%` | `49.01` |
| `Live` | `Long` | `22.35` | 123,020,000.00 USD | 0.00 USD | 5,040.00 USD | `-77.01%` | `225.60` |
| `Live` | `Long` | `22.45` | 123,020,000.00 USD | 0.00 USD | 8,570.00 USD | `-76.90%` | `381.58` |
| `Live` | `Long` | `22.95` | 123,010,000.00 USD | 0.00 USD | 1,150.00 USD | `-76.39%` | `50.00` |
| `Live` | `Long` | `23.05` | 123,010,000.00 USD | 0.00 USD | 114.10 USD | `-76.29%` | `4.95` |
| `Live` | `Long` | `23.15` | 123,010,000.00 USD | 0.00 USD | 1,010.00 USD | `-76.18%` | `43.60` |
| `Live` | `Long` | `23.45` | 123,010,000.00 USD | 0.00 USD | 1,380.00 USD | `-75.87%` | `58.86` |
| `Live` | `Long` | `23.65` | 123,000,000.00 USD | 0.00 USD | 619.16 USD | `-75.67%` | `26.18` |
| `Live` | `Long` | `23.75` | 123,000,000.00 USD | 0.00 USD | 1,190.00 USD | `-75.57%` | `50.00` |
| `Live` | `Long` | `23.95` | 123,000,000.00 USD | 0.00 USD | 1,120.00 USD | `-75.36%` | `46.58` |
| `Live` | `Long` | `24.05` | 123,000,000.00 USD | 0.00 USD | 8,870.00 USD | `-75.26%` | `369.00` |
| `Live` | `Long` | `24.25` | 122,990,000.00 USD | 0.00 USD | 10,230.00 USD | `-75.05%` | `422.03` |
| `Live` | `Long` | `24.35` | 122,980,000.00 USD | 0.00 USD | 878,940.00 USD | `-74.95%` | `36,095.99` |
| `Live` | `Long` | `24.85` | 122,100,000.00 USD | 0.00 USD | 12,430.00 USD | `-74.43%` | `500.00` |
| `Live` | `Long` | `24.95` | 122,090,000.00 USD | 0.00 USD | 160.43 USD | `-74.33%` | `6.43` |
| `Live` | `Long` | `25.05` | 122,090,000.00 USD | 0.00 USD | 2,640.00 USD | `-74.23%` | `105.27` |
| `Live` | `Long` | `25.15` | 122,090,000.00 USD | 0.00 USD | 2,010.00 USD | `-74.13%` | `80.00` |
| `Live` | `Long` | `25.25` | 122,090,000.00 USD | 0.00 USD | 4,660.00 USD | `-74.02%` | `184.67` |
| `Live` | `Long` | `25.45` | 122,080,000.00 USD | 0.00 USD | 106.64 USD | `-73.82%` | `4.19` |
| `Live` | `Long` | `25.55` | 122,080,000.00 USD | 0.00 USD | 2,760.00 USD | `-73.71%` | `108.12` |
| `Live` | `Long` | `25.85` | 122,080,000.00 USD | 0.00 USD | 148,650.00 USD | `-73.41%` | `5,750.44` |
| `Live` | `Long` | `25.95` | 121,930,000.00 USD | 0.00 USD | 2,930.00 USD | `-73.30%` | `113.00` |
| `Live` | `Long` | `26.05` | 121,930,000.00 USD | 0.00 USD | 5,210.00 USD | `-73.20%` | `200.00` |
| `Live` | `Long` | `26.15` | 121,920,000.00 USD | 0.00 USD | 1,620.00 USD | `-73.10%` | `62.00` |
| `Live` | `Long` | `26.25` | 121,920,000.00 USD | 0.00 USD | 22,600.00 USD | `-72.99%` | `861.04` |
| `Live` | `Long` | `26.55` | 121,900,000.00 USD | 0.00 USD | 478.70 USD | `-72.69%` | `18.03` |
| `Live` | `Long` | `26.65` | 121,900,000.00 USD | 0.00 USD | 265.17 USD | `-72.58%` | `9.95` |
| `Live` | `Long` | `26.95` | 121,900,000.00 USD | 0.00 USD | 11,420.00 USD | `-72.27%` | `423.77` |
| `Live` | `Long` | `27.25` | 121,890,000.00 USD | 0.00 USD | 5,450.00 USD | `-71.97%` | `200.00` |
| `Live` | `Long` | `27.35` | 121,880,000.00 USD | 0.00 USD | 332.30 USD | `-71.86%` | `12.15` |
| `Live` | `Long` | `27.45` | 121,880,000.00 USD | 0.00 USD | 982.98 USD | `-71.76%` | `35.81` |
| `Live` | `Long` | `27.85` | 121,880,000.00 USD | 0.00 USD | 808.21 USD | `-71.35%` | `29.02` |
| `Live` | `Long` | `27.95` | 121,880,000.00 USD | 0.00 USD | 747.10 USD | `-71.24%` | `26.73` |
| `Live` | `Long` | `28.05` | 121,880,000.00 USD | 0.00 USD | 2,740.00 USD | `-71.14%` | `97.63` |
| `Live` | `Long` | `28.35` | 121,870,000.00 USD | 0.00 USD | 6,330.00 USD | `-70.83%` | `223.13` |
| `Live` | `Long` | `28.45` | 121,870,000.00 USD | 0.00 USD | 113.80 USD | `-70.73%` | `4.00` |
| `Live` | `Long` | `28.75` | 121,870,000.00 USD | 0.00 USD | 86,250.00 USD | `-70.42%` | `3,000.00` |
| `Live` | `Long` | `28.85` | 121,780,000.00 USD | 0.00 USD | 721.25 USD | `-70.32%` | `25.00` |
| `Live` | `Long` | `29.15` | 121,780,000.00 USD | 0.00 USD | 9,910.00 USD | `-70.01%` | `340.00` |
| `Live` | `Long` | `29.25` | 121,770,000.00 USD | 0.00 USD | 150.93 USD | `-69.91%` | `5.16` |
| `Live` | `Long` | `29.35` | 121,770,000.00 USD | 0.00 USD | 15,380.00 USD | `-69.80%` | `523.99` |
| `Live` | `Long` | `29.45` | 121,760,000.00 USD | 0.00 USD | 18,410.00 USD | `-69.70%` | `625.00` |
| `Live` | `Long` | `29.55` | 121,740,000.00 USD | 0.00 USD | 2,940.00 USD | `-69.60%` | `99.64` |
| `Live` | `Long` | `29.65` | 121,730,000.00 USD | 0.00 USD | 44,480.00 USD | `-69.50%` | `1,500.00` |
| `Live` | `Long` | `29.85` | 121,690,000.00 USD | 0.00 USD | 10,070.00 USD | `-69.29%` | `337.19` |
| `Live` | `Long` | `29.95` | 121,680,000.00 USD | 0.00 USD | 1,430.00 USD | `-69.19%` | `47.80` |
| `Live` | `Long` | `30.05` | 121,680,000.00 USD | 0.00 USD | 3,010.00 USD | `-69.08%` | `100.04` |
| `Live` | `Long` | `30.15` | 121,680,000.00 USD | 0.00 USD | 47,340.00 USD | `-68.98%` | `1,570.00` |
| `Live` | `Long` | `30.45` | 121,630,000.00 USD | 0.00 USD | 4,240.00 USD | `-68.67%` | `139.36` |
| `Live` | `Long` | `30.55` | 121,620,000.00 USD | 0.00 USD | 889.01 USD | `-68.57%` | `29.10` |
| `Live` | `Long` | `30.65` | 121,620,000.00 USD | 0.00 USD | 233.86 USD | `-68.47%` | `7.63` |
| `Live` | `Long` | `30.75` | 121,620,000.00 USD | 0.00 USD | 450.80 USD | `-68.36%` | `14.66` |
| `Live` | `Long` | `30.85` | 121,620,000.00 USD | 0.00 USD | 157.64 USD | `-68.26%` | `5.11` |
| `Live` | `Long` | `31.05` | 121,620,000.00 USD | 0.00 USD | 3,380.00 USD | `-68.06%` | `108.86` |
| `Live` | `Long` | `31.25` | 121,620,000.00 USD | 0.00 USD | 1,340.00 USD | `-67.85%` | `42.78` |
| `Live` | `Long` | `31.35` | 121,620,000.00 USD | 0.00 USD | 35,160.00 USD | `-67.75%` | `1,121.64` |
| `Live` | `Long` | `31.45` | 121,580,000.00 USD | 0.00 USD | 278.33 USD | `-67.64%` | `8.85` |
| `Live` | `Long` | `31.65` | 121,580,000.00 USD | 0.00 USD | 16,560.00 USD | `-67.44%` | `523.23` |
| `Live` | `Long` | `32.05` | 121,570,000.00 USD | 0.00 USD | 1,970.00 USD | `-67.03%` | `61.57` |
| `Live` | `Long` | `32.25` | 121,560,000.00 USD | 0.00 USD | 496.01 USD | `-66.82%` | `15.38` |
| `Live` | `Long` | `32.45` | 121,560,000.00 USD | 0.00 USD | 804.11 USD | `-66.62%` | `24.78` |
| `Live` | `Long` | `32.55` | 121,560,000.00 USD | 0.00 USD | 3,770.00 USD | `-66.51%` | `115.67` |
| `Live` | `Long` | `32.75` | 121,560,000.00 USD | 0.00 USD | 5,360.00 USD | `-66.31%` | `163.78` |
| `Live` | `Long` | `32.85` | 121,550,000.00 USD | 0.00 USD | 5,240.00 USD | `-66.20%` | `159.61` |
| `Live` | `Long` | `32.95` | 121,550,000.00 USD | 0.00 USD | 875.15 USD | `-66.10%` | `26.56` |
| `Live` | `Long` | `33.05` | 121,550,000.00 USD | 0.00 USD | 39,660.00 USD | `-66.00%` | `1,200.00` |
| `Live` | `Long` | `33.15` | 121,510,000.00 USD | 0.00 USD | 193.93 USD | `-65.90%` | `5.85` |
| `Live` | `Long` | `33.35` | 121,510,000.00 USD | 0.00 USD | 12,380.00 USD | `-65.69%` | `371.10` |
| `Live` | `Long` | `33.45` | 121,490,000.00 USD | 0.00 USD | 6,580.00 USD | `-65.59%` | `196.65` |
| `Live` | `Long` | `33.55` | 121,490,000.00 USD | 0.00 USD | 302.62 USD | `-65.48%` | `9.02` |
| `Live` | `Long` | `33.65` | 121,490,000.00 USD | 0.00 USD | 494.99 USD | `-65.38%` | `14.71` |
| `Live` | `Long` | `33.75` | 121,490,000.00 USD | 0.00 USD | 1,830.00 USD | `-65.28%` | `54.25` |
| `Live` | `Long` | `33.95` | 121,490,000.00 USD | 0.00 USD | 577,150.00 USD | `-65.07%` | `17,000.02` |
| `Live` | `Long` | `34.25` | 120,910,000.00 USD | 0.00 USD | 141.79 USD | `-64.76%` | `4.14` |
| `Live` | `Long` | `34.65` | 120,910,000.00 USD | 0.00 USD | 1,710.00 USD | `-64.35%` | `49.29` |
| `Live` | `Long` | `34.85` | 120,910,000.00 USD | 0.00 USD | 580.95 USD | `-64.15%` | `16.67` |
| `Live` | `Long` | `35.05` | 120,910,000.00 USD | 0.00 USD | 6,640,000.00 USD | `-63.94%` | `189,509.23` |
| `Live` | `Long` | `35.15` | 114,260,000.00 USD | 0.00 USD | 734.28 USD | `-63.84%` | `20.89` |
| `Live` | `Long` | `35.75` | 114,260,000.00 USD | 0.00 USD | 8,590.00 USD | `-63.22%` | `240.28` |
| `Live` | `Long` | `35.85` | 114,250,000.00 USD | 0.00 USD | 3,360.00 USD | `-63.12%` | `93.75` |
| `Live` | `Long` | `35.95` | 114,250,000.00 USD | 0.00 USD | 557.94 USD | `-63.01%` | `15.52` |
| `Live` | `Long` | `36.05` | 114,250,000.00 USD | 0.00 USD | 5,070.00 USD | `-62.91%` | `140.61` |
| `Live` | `Long` | `36.15` | 114,240,000.00 USD | 0.00 USD | 531.41 USD | `-62.81%` | `14.70` |
| `Live` | `Long` | `36.25` | 114,240,000.00 USD | 0.00 USD | 78,700.00 USD | `-62.71%` | `2,171.10` |
| `Live` | `Long` | `36.35` | 114,170,000.00 USD | 0.00 USD | 4,410.00 USD | `-62.60%` | `121.32` |
| `Live` | `Long` | `36.45` | 114,160,000.00 USD | 0.00 USD | 2,410.00 USD | `-62.50%` | `66.24` |
| `Live` | `Long` | `36.55` | 114,160,000.00 USD | 0.00 USD | 49,130.00 USD | `-62.40%` | `1,344.19` |
| `Live` | `Long` | `36.65` | 114,110,000.00 USD | 0.00 USD | 111,820.00 USD | `-62.29%` | `3,051.08` |
| `Live` | `Long` | `36.75` | 114,000,000.00 USD | 0.00 USD | 500.90 USD | `-62.19%` | `13.63` |
| `Live` | `Long` | `36.85` | 114,000,000.00 USD | 0.00 USD | 903.93 USD | `-62.09%` | `24.53` |
| `Live` | `Long` | `36.95` | 114,000,000.00 USD | 0.00 USD | 1,660.00 USD | `-61.99%` | `45.00` |
| `Live` | `Long` | `37.05` | 113,990,000.00 USD | 0.00 USD | 41,180.00 USD | `-61.88%` | `1,111.41` |
| `Live` | `Long` | `37.25` | 113,950,000.00 USD | 0.00 USD | 1,690.00 USD | `-61.68%` | `45.41` |
| `Live` | `Long` | `37.35` | 113,950,000.00 USD | 0.00 USD | 20,600.00 USD | `-61.57%` | `551.61` |
| `Live` | `Long` | `37.45` | 113,930,000.00 USD | 0.00 USD | 631.03 USD | `-61.47%` | `16.85` |
| `Live` | `Long` | `37.55` | 113,930,000.00 USD | 0.00 USD | 262.85 USD | `-61.37%` | `7.00` |
| `Live` | `Long` | `37.65` | 113,930,000.00 USD | 0.00 USD | 23,340.00 USD | `-61.27%` | `619.99` |
| `Live` | `Long` | `37.85` | 113,910,000.00 USD | 0.00 USD | 5,570.00 USD | `-61.06%` | `147.15` |
| `Live` | `Long` | `37.95` | 113,900,000.00 USD | 0.00 USD | 5,430.00 USD | `-60.96%` | `143.17` |
| `Live` | `Long` | `38.05` | 113,900,000.00 USD | 0.00 USD | 542.59 USD | `-60.85%` | `14.26` |
| `Live` | `Long` | `38.15` | 113,900,000.00 USD | 0.00 USD | 18,020.00 USD | `-60.75%` | `472.38` |
| `Live` | `Long` | `38.25` | 113,880,000.00 USD | 0.00 USD | 759.64 USD | `-60.65%` | `19.86` |
| `Live` | `Long` | `38.35` | 113,880,000.00 USD | 0.00 USD | 287.63 USD | `-60.55%` | `7.50` |
| `Live` | `Long` | `38.45` | 113,880,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-60.44%` | `78,000.00` |
| `Live` | `Long` | `38.55` | 110,880,000.00 USD | 0.00 USD | 116.04 USD | `-60.34%` | `3.01` |
| `Live` | `Long` | `38.75` | 110,880,000.00 USD | 0.00 USD | 736.64 USD | `-60.13%` | `19.01` |
| `Live` | `Long` | `38.85` | 110,880,000.00 USD | 0.00 USD | 4,270.00 USD | `-60.03%` | `109.96` |
| `Live` | `Long` | `38.95` | 110,870,000.00 USD | 0.00 USD | 195,360.00 USD | `-59.93%` | `5,015.60` |
| `Live` | `Long` | `39.05` | 110,680,000.00 USD | 0.00 USD | 50,470.00 USD | `-59.83%` | `1,292.50` |
| `Live` | `Long` | `39.15` | 110,630,000.00 USD | 0.00 USD | 1,710.00 USD | `-59.72%` | `43.67` |
| `Live` | `Long` | `39.35` | 110,620,000.00 USD | 0.00 USD | 45,040.00 USD | `-59.52%` | `1,144.66` |
| `Live` | `Long` | `39.45` | 110,580,000.00 USD | 0.00 USD | 4,500.00 USD | `-59.41%` | `113.97` |
| `Live` | `Long` | `39.65` | 110,580,000.00 USD | 0.00 USD | 3,400.00 USD | `-59.21%` | `85.66` |
| `Live` | `Long` | `39.75` | 110,570,000.00 USD | 0.00 USD | 159.00 USD | `-59.10%` | `4.00` |
| `Live` | `Long` | `39.85` | 110,570,000.00 USD | 0.00 USD | 1,870.00 USD | `-59.00%` | `46.86` |
| `Live` | `Long` | `39.95` | 110,570,000.00 USD | 0.00 USD | 16,520.00 USD | `-58.90%` | `413.53` |
| `Live` | `Long` | `40.05` | 110,550,000.00 USD | 0.00 USD | 905,320.00 USD | `-58.80%` | `22,604.67` |
| `Live` | `Long` | `40.15` | 109,650,000.00 USD | 0.00 USD | 3,500.00 USD | `-58.69%` | `87.27` |
| `Live` | `Long` | `40.25` | 109,640,000.00 USD | 0.00 USD | 12,710.00 USD | `-58.59%` | `315.72` |
| `Live` | `Long` | `40.55` | 109,630,000.00 USD | 0.00 USD | 3,160.00 USD | `-58.28%` | `77.90` |
| `Live` | `Long` | `40.85` | 109,630,000.00 USD | 0.00 USD | 12,400.00 USD | `-57.97%` | `303.63` |
| `Live` | `Long` | `40.95` | 109,620,000.00 USD | 0.00 USD | 142.10 USD | `-57.87%` | `3.47` |
| `Live` | `Long` | `41.05` | 109,620,000.00 USD | 0.00 USD | 6,760.00 USD | `-57.77%` | `164.69` |
| `Live` | `Long` | `41.15` | 109,610,000.00 USD | 0.00 USD | 53,750.00 USD | `-57.66%` | `1,306.08` |
| `Live` | `Long` | `41.25` | 109,560,000.00 USD | 0.00 USD | 368.36 USD | `-57.56%` | `8.93` |
| `Live` | `Long` | `41.35` | 109,560,000.00 USD | 0.00 USD | 148.45 USD | `-57.46%` | `3.59` |
| `Live` | `Long` | `41.55` | 109,560,000.00 USD | 0.00 USD | 489.04 USD | `-57.25%` | `11.77` |
| `Live` | `Long` | `41.65` | 109,550,000.00 USD | 0.00 USD | 24,190.00 USD | `-57.15%` | `580.75` |
| `Live` | `Long` | `41.75` | 109,530,000.00 USD | 0.00 USD | 2,160.00 USD | `-57.05%` | `51.71` |
| `Live` | `Long` | `41.85` | 109,530,000.00 USD | 0.00 USD | 3,060.00 USD | `-56.94%` | `73.03` |
| `Live` | `Long` | `41.95` | 109,530,000.00 USD | 0.00 USD | 48,400.00 USD | `-56.84%` | `1,153.84` |
| `Live` | `Long` | `42.05` | 109,480,000.00 USD | 0.00 USD | 470.12 USD | `-56.74%` | `11.18` |
| `Live` | `Long` | `42.15` | 109,480,000.00 USD | 0.00 USD | 4,170.00 USD | `-56.64%` | `99.02` |
| `Live` | `Long` | `42.25` | 109,470,000.00 USD | 0.00 USD | 6,500.00 USD | `-56.53%` | `153.75` |
| `Live` | `Long` | `42.35` | 109,470,000.00 USD | 0.00 USD | 198.62 USD | `-56.43%` | `4.69` |
| `Live` | `Long` | `42.45` | 109,470,000.00 USD | 0.00 USD | 19,900.00 USD | `-56.33%` | `468.86` |
| `Live` | `Long` | `42.55` | 109,450,000.00 USD | 0.00 USD | 8,210.00 USD | `-56.22%` | `193.00` |
| `Live` | `Long` | `42.85` | 109,440,000.00 USD | 0.00 USD | 44,250.00 USD | `-55.92%` | `1,032.68` |
| `Live` | `Long` | `42.95` | 109,390,000.00 USD | 0.00 USD | 355.20 USD | `-55.81%` | `8.27` |
| `Live` | `Long` | `43.25` | 109,390,000.00 USD | 0.00 USD | 1,730.00 USD | `-55.50%` | `40.00` |
| `Live` | `Long` | `43.35` | 109,390,000.00 USD | 0.00 USD | 12,030.00 USD | `-55.40%` | `277.49` |
| `Live` | `Long` | `43.45` | 109,380,000.00 USD | 0.00 USD | 440.15 USD | `-55.30%` | `10.13` |
| `Live` | `Long` | `43.65` | 109,380,000.00 USD | 0.00 USD | 740.74 USD | `-55.09%` | `16.97` |
| `Live` | `Long` | `43.75` | 109,380,000.00 USD | 0.00 USD | 725,070.00 USD | `-54.99%` | `16,572.97` |
| `Live` | `Long` | `43.85` | 108,650,000.00 USD | 0.00 USD | 326.24 USD | `-54.89%` | `7.44` |
| `Live` | `Long` | `43.95` | 108,650,000.00 USD | 0.00 USD | 11,790.00 USD | `-54.78%` | `268.15` |
| `Live` | `Long` | `44.05` | 108,640,000.00 USD | 0.00 USD | 13,420.00 USD | `-54.68%` | `304.69` |
| `Live` | `Long` | `44.25` | 108,630,000.00 USD | 0.00 USD | 366,420.00 USD | `-54.48%` | `8,280.65` |
| `Live` | `Long` | `44.35` | 108,260,000.00 USD | 0.00 USD | 8,630.00 USD | `-54.37%` | `194.56` |
| `Live` | `Long` | `44.45` | 108,250,000.00 USD | 0.00 USD | 10,180.00 USD | `-54.27%` | `229.02` |
| `Live` | `Long` | `44.55` | 108,240,000.00 USD | 0.00 USD | 17,870.00 USD | `-54.17%` | `401.03` |
| `Live` | `Long` | `44.65` | 108,220,000.00 USD | 0.00 USD | 2,240.00 USD | `-54.06%` | `50.24` |
| `Live` | `Long` | `44.75` | 108,220,000.00 USD | 0.00 USD | 1,790.00 USD | `-53.96%` | `39.98` |
| `Live` | `Long` | `44.85` | 108,220,000.00 USD | 0.00 USD | 477.20 USD | `-53.86%` | `10.64` |
| `Live` | `Long` | `44.95` | 108,220,000.00 USD | 0.00 USD | 6,510.00 USD | `-53.76%` | `144.85` |
| `Live` | `Long` | `45.15` | 108,210,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-53.55%` | `25,143.68` |
| `Live` | `Long` | `45.35` | 107,080,000.00 USD | 0.00 USD | 31,200.00 USD | `-53.34%` | `688.07` |
| `Live` | `Long` | `45.45` | 107,050,000.00 USD | 0.00 USD | 19,810.00 USD | `-53.24%` | `435.92` |
| `Live` | `Long` | `45.55` | 107,030,000.00 USD | 0.00 USD | 7,940.00 USD | `-53.14%` | `174.26` |
| `Live` | `Long` | `45.65` | 107,020,000.00 USD | 0.00 USD | 319.09 USD | `-53.03%` | `6.99` |
| `Live` | `Long` | `45.75` | 107,020,000.00 USD | 0.00 USD | 9,450.00 USD | `-52.93%` | `206.46` |
| `Live` | `Long` | `45.85` | 107,010,000.00 USD | 0.00 USD | 458.50 USD | `-52.83%` | `10.00` |
| `Live` | `Long` | `45.95` | 107,010,000.00 USD | 0.00 USD | 62,910.00 USD | `-52.73%` | `1,369.05` |
| `Live` | `Long` | `46.05` | 106,950,000.00 USD | 0.00 USD | 281.83 USD | `-52.62%` | `6.12` |
| `Live` | `Long` | `46.45` | 106,950,000.00 USD | 0.00 USD | 824.95 USD | `-52.21%` | `17.76` |
| `Live` | `Long` | `46.55` | 106,940,000.00 USD | 0.00 USD | 522.76 USD | `-52.11%` | `11.23` |
| `Live` | `Long` | `46.65` | 106,940,000.00 USD | 0.00 USD | 1,190.00 USD | `-52.01%` | `25.57` |
| `Live` | `Long` | `46.75` | 106,940,000.00 USD | 0.00 USD | 374.00 USD | `-51.90%` | `8.00` |
| `Live` | `Long` | `46.85` | 106,940,000.00 USD | 0.00 USD | 702.75 USD | `-51.80%` | `15.00` |
| `Live` | `Long` | `46.95` | 106,940,000.00 USD | 0.00 USD | 2,490.00 USD | `-51.70%` | `53.09` |
| `Live` | `Long` | `47.15` | 106,940,000.00 USD | 0.00 USD | 3,860,000.00 USD | `-51.49%` | `81,886.29` |
| `Live` | `Long` | `47.25` | 103,080,000.00 USD | 0.00 USD | 3,220.00 USD | `-51.39%` | `68.21` |
| `Live` | `Long` | `47.35` | 103,080,000.00 USD | 0.00 USD | 324.82 USD | `-51.29%` | `6.86` |
| `Live` | `Long` | `47.55` | 103,070,000.00 USD | 0.00 USD | 449.82 USD | `-51.08%` | `9.46` |
| `Live` | `Long` | `47.65` | 103,070,000.00 USD | 0.00 USD | 99,760.00 USD | `-50.98%` | `2,093.61` |
| `Live` | `Long` | `47.75` | 102,970,000.00 USD | 0.00 USD | 66,920.00 USD | `-50.87%` | `1,401.45` |
| `Live` | `Long` | `47.85` | 102,910,000.00 USD | 0.00 USD | 125.37 USD | `-50.77%` | `2.62` |
| `Live` | `Long` | `48.05` | 102,910,000.00 USD | 0.00 USD | 13,300.00 USD | `-50.57%` | `276.89` |
| `Live` | `Long` | `48.15` | 102,890,000.00 USD | 0.00 USD | 5,970.00 USD | `-50.46%` | `124.07` |
| `Live` | `Long` | `48.25` | 102,890,000.00 USD | 0.00 USD | 3,980.00 USD | `-50.36%` | `82.45` |
| `Live` | `Long` | `48.35` | 102,880,000.00 USD | 0.00 USD | 8,060.00 USD | `-50.26%` | `166.61` |
| `Live` | `Long` | `48.45` | 102,880,000.00 USD | 0.00 USD | 7,790.00 USD | `-50.15%` | `160.82` |
| `Live` | `Long` | `48.55` | 102,870,000.00 USD | 0.00 USD | 97,530.00 USD | `-50.05%` | `2,008.83` |
| `Live` | `Long` | `48.65` | 102,770,000.00 USD | 0.00 USD | 9,260.00 USD | `-49.95%` | `190.42` |
| `Live` | `Long` | `48.75` | 102,760,000.00 USD | 0.00 USD | 31,020.00 USD | `-49.85%` | `636.39` |
| `Live` | `Long` | `48.85` | 102,730,000.00 USD | 0.00 USD | 14,260.00 USD | `-49.74%` | `291.88` |
| `Live` | `Long` | `48.95` | 102,720,000.00 USD | 0.00 USD | 1,490.00 USD | `-49.64%` | `30.41` |
| `Live` | `Long` | `49.05` | 102,710,000.00 USD | 0.00 USD | 11,600.00 USD | `-49.54%` | `236.51` |
| `Live` | `Long` | `49.25` | 102,700,000.00 USD | 0.00 USD | 21,190.00 USD | `-49.33%` | `430.30` |
| `Live` | `Long` | `49.35` | 102,680,000.00 USD | 0.00 USD | 585.29 USD | `-49.23%` | `11.86` |
| `Live` | `Long` | `49.45` | 102,680,000.00 USD | 0.00 USD | 17,180.00 USD | `-49.13%` | `347.51` |
| `Live` | `Long` | `49.55` | 102,660,000.00 USD | 0.00 USD | 627.80 USD | `-49.02%` | `12.67` |
| `Live` | `Long` | `49.65` | 102,660,000.00 USD | 0.00 USD | 11,440.00 USD | `-48.92%` | `230.39` |
| `Live` | `Long` | `49.75` | 102,650,000.00 USD | 0.00 USD | 783,640.00 USD | `-48.82%` | `15,751.46` |
| `Live` | `Long` | `49.85` | 101,870,000.00 USD | 0.00 USD | 43,150.00 USD | `-48.71%` | `865.63` |
| `Live` | `Long` | `49.95` | 101,830,000.00 USD | 0.00 USD | 23,020.00 USD | `-48.61%` | `460.92` |
| `Live` | `Long` | `50.05` | 101,800,000.00 USD | 0.00 USD | 15,660.00 USD | `-48.51%` | `312.96` |
| `Live` | `Long` | `50.15` | 101,790,000.00 USD | 0.00 USD | 1,780.00 USD | `-48.41%` | `35.57` |
| `Live` | `Long` | `50.25` | 101,790,000.00 USD | 0.00 USD | 8,060.00 USD | `-48.30%` | `160.45` |
| `Live` | `Long` | `50.35` | 101,780,000.00 USD | 0.00 USD | 12,490.00 USD | `-48.20%` | `247.98` |
| `Live` | `Long` | `50.45` | 101,760,000.00 USD | 0.00 USD | 11,730.00 USD | `-48.10%` | `232.60` |
| `Live` | `Long` | `50.55` | 101,750,000.00 USD | 0.00 USD | 2,400.00 USD | `-47.99%` | `47.47` |
| `Live` | `Long` | `50.65` | 101,750,000.00 USD | 0.00 USD | 843.83 USD | `-47.89%` | `16.66` |
| `Live` | `Long` | `50.75` | 101,750,000.00 USD | 0.00 USD | 12,800.00 USD | `-47.79%` | `252.21` |
| `Live` | `Long` | `50.85` | 101,740,000.00 USD | 0.00 USD | 20,140.00 USD | `-47.69%` | `396.09` |
| `Live` | `Long` | `50.95` | 101,720,000.00 USD | 0.00 USD | 9,430.00 USD | `-47.58%` | `185.18` |
| `Live` | `Long` | `51.05` | 101,710,000.00 USD | 0.00 USD | 319,690.00 USD | `-47.48%` | `6,262.21` |
| `Live` | `Long` | `51.15` | 101,390,000.00 USD | 0.00 USD | 1,230,000.00 USD | `-47.38%` | `24,063.31` |
| `Live` | `Long` | `51.25` | 100,160,000.00 USD | 0.00 USD | 10,940.00 USD | `-47.27%` | `213.44` |
| `Live` | `Long` | `51.35` | 100,150,000.00 USD | 0.00 USD | 360.48 USD | `-47.17%` | `7.02` |
| `Live` | `Long` | `51.45` | 100,150,000.00 USD | 0.00 USD | 4,170.00 USD | `-47.07%` | `81.14` |
| `Live` | `Long` | `51.55` | 100,140,000.00 USD | 0.00 USD | 138,060.00 USD | `-46.97%` | `2,678.14` |
| `Live` | `Long` | `51.65` | 100,000,000.00 USD | 0.00 USD | 3,280.00 USD | `-46.86%` | `63.50` |
| `Live` | `Long` | `51.75` | 100,000,000.00 USD | 0.00 USD | 24,770.00 USD | `-46.76%` | `478.71` |
| `Live` | `Long` | `51.85` | 99,980,000.00 USD | 0.00 USD | 46,110.00 USD | `-46.66%` | `889.34` |
| `Live` | `Long` | `51.95` | 99,930,000.00 USD | 0.00 USD | 469,860.00 USD | `-46.55%` | `9,044.37` |
| `Live` | `Long` | `52.15` | 99,460,000.00 USD | 0.00 USD | 99,630.00 USD | `-46.35%` | `1,910.43` |
| `Live` | `Long` | `52.25` | 99,360,000.00 USD | 0.00 USD | 3,340.00 USD | `-46.24%` | `63.96` |
| `Live` | `Long` | `52.35` | 99,360,000.00 USD | 0.00 USD | 1,030.00 USD | `-46.14%` | `19.66` |
| `Live` | `Long` | `52.45` | 99,360,000.00 USD | 0.00 USD | 879.59 USD | `-46.04%` | `16.77` |
| `Live` | `Long` | `52.55` | 99,350,000.00 USD | 0.00 USD | 39,900.00 USD | `-45.94%` | `759.31` |
| `Live` | `Long` | `52.65` | 99,310,000.00 USD | 0.00 USD | 2,630.00 USD | `-45.83%` | `50.00` |
| `Live` | `Long` | `52.75` | 99,310,000.00 USD | 0.00 USD | 3,180.00 USD | `-45.73%` | `60.32` |
| `Live` | `Long` | `52.85` | 99,310,000.00 USD | 0.00 USD | 9,370.00 USD | `-45.63%` | `177.38` |
| `Live` | `Long` | `52.95` | 99,300,000.00 USD | 0.00 USD | 6,120.00 USD | `-45.52%` | `115.56` |
| `Live` | `Long` | `53.05` | 99,290,000.00 USD | 0.00 USD | 5,120.00 USD | `-45.42%` | `96.59` |
| `Live` | `Long` | `53.15` | 99,290,000.00 USD | 0.00 USD | 3,110.00 USD | `-45.32%` | `58.53` |
| `Live` | `Long` | `53.25` | 99,280,000.00 USD | 0.00 USD | 35,570.00 USD | `-45.22%` | `667.90` |
| `Live` | `Long` | `53.35` | 99,250,000.00 USD | 0.00 USD | 13,390.00 USD | `-45.11%` | `250.94` |
| `Live` | `Long` | `53.45` | 99,240,000.00 USD | 0.00 USD | 35,530.00 USD | `-45.01%` | `664.64` |
| `Live` | `Long` | `53.55` | 99,200,000.00 USD | 0.00 USD | 54,310.00 USD | `-44.91%` | `1,014.27` |
| `Live` | `Long` | `53.65` | 99,150,000.00 USD | 0.00 USD | 11,440.00 USD | `-44.80%` | `213.19` |
| `Live` | `Long` | `53.75` | 99,130,000.00 USD | 0.00 USD | 3,600.00 USD | `-44.70%` | `67.00` |
| `Live` | `Long` | `53.85` | 99,130,000.00 USD | 0.00 USD | 19,810.00 USD | `-44.60%` | `367.96` |
| `Live` | `Long` | `53.95` | 99,110,000.00 USD | 0.00 USD | 59,450.00 USD | `-44.50%` | `1,102.01` |
| `Live` | `Long` | `54.05` | 99,050,000.00 USD | 0.00 USD | 18,910.00 USD | `-44.39%` | `349.85` |
| `Live` | `Long` | `54.15` | 99,030,000.00 USD | 0.00 USD | 14,640.00 USD | `-44.29%` | `270.39` |
| `Live` | `Long` | `54.25` | 99,020,000.00 USD | 0.00 USD | 5,360.00 USD | `-44.19%` | `98.83` |
| `Live` | `Long` | `54.35` | 99,010,000.00 USD | 0.00 USD | 11,720.00 USD | `-44.08%` | `215.69` |
| `Live` | `Long` | `54.45` | 99,000,000.00 USD | 0.00 USD | 2,060.00 USD | `-43.98%` | `37.90` |
| `Live` | `Long` | `54.55` | 99,000,000.00 USD | 0.00 USD | 64,910.00 USD | `-43.88%` | `1,189.98` |
| `Live` | `Long` | `54.65` | 98,930,000.00 USD | 0.00 USD | 3,380.00 USD | `-43.78%` | `61.91` |
| `Live` | `Long` | `54.75` | 98,930,000.00 USD | 0.00 USD | 37,350.00 USD | `-43.67%` | `682.16` |
| `Live` | `Long` | `54.85` | 98,890,000.00 USD | 0.00 USD | 861,400.00 USD | `-43.57%` | `15,704.66` |
| `Live` | `Long` | `54.95` | 98,030,000.00 USD | 0.00 USD | 142,480.00 USD | `-43.47%` | `2,592.93` |
| `Live` | `Long` | `55.05` | 97,890,000.00 USD | 0.00 USD | 552.70 USD | `-43.36%` | `10.04` |
| `Live` | `Long` | `55.15` | 97,890,000.00 USD | 0.00 USD | 341.93 USD | `-43.26%` | `6.20` |
| `Live` | `Long` | `55.25` | 97,890,000.00 USD | 0.00 USD | 2,010.00 USD | `-43.16%` | `36.31` |
| `Live` | `Long` | `55.35` | 97,890,000.00 USD | 0.00 USD | 9,920.00 USD | `-43.06%` | `179.16` |
| `Live` | `Long` | `55.45` | 97,880,000.00 USD | 0.00 USD | 8,670.00 USD | `-42.95%` | `156.35` |
| `Live` | `Long` | `55.55` | 97,870,000.00 USD | 0.00 USD | 5,090.00 USD | `-42.85%` | `91.69` |
| `Live` | `Long` | `55.65` | 97,860,000.00 USD | 0.00 USD | 11,490.00 USD | `-42.75%` | `206.41` |
| `Live` | `Long` | `55.75` | 97,850,000.00 USD | 0.00 USD | 233,170.00 USD | `-42.64%` | `4,182.42` |
| `Live` | `Long` | `55.85` | 97,620,000.00 USD | 0.00 USD | 5,050.00 USD | `-42.54%` | `90.34` |
| `Live` | `Long` | `55.95` | 97,610,000.00 USD | 0.00 USD | 7,390.00 USD | `-42.44%` | `132.09` |
| `Live` | `Long` | `56.05` | 97,610,000.00 USD | 0.00 USD | 19,890.00 USD | `-42.34%` | `354.84` |
| `Live` | `Long` | `56.15` | 97,590,000.00 USD | 0.00 USD | 40,270.00 USD | `-42.23%` | `717.16` |
| `Live` | `Long` | `56.25` | 97,550,000.00 USD | 0.00 USD | 13,300.00 USD | `-42.13%` | `236.52` |
| `Live` | `Long` | `56.35` | 97,530,000.00 USD | 0.00 USD | 12,550.00 USD | `-42.03%` | `222.68` |
| `Live` | `Long` | `56.45` | 97,520,000.00 USD | 0.00 USD | 12,980.00 USD | `-41.92%` | `229.97` |
| `Live` | `Long` | `56.55` | 97,510,000.00 USD | 0.00 USD | 4,730.00 USD | `-41.82%` | `83.63` |
| `Live` | `Long` | `56.65` | 97,500,000.00 USD | 0.00 USD | 3,190.00 USD | `-41.72%` | `56.32` |
| `Live` | `Long` | `56.75` | 97,500,000.00 USD | 0.00 USD | 9,410.00 USD | `-41.62%` | `165.87` |
| `Live` | `Long` | `56.85` | 97,490,000.00 USD | 0.00 USD | 122.80 USD | `-41.51%` | `2.16` |
| `Live` | `Long` | `56.95` | 97,490,000.00 USD | 0.00 USD | 2,780,000.00 USD | `-41.41%` | `48,815.94` |
| `Live` | `Long` | `57.05` | 94,710,000.00 USD | 0.00 USD | 3,620.00 USD | `-41.31%` | `63.42` |
| `Live` | `Long` | `57.15` | 94,710,000.00 USD | 0.00 USD | 6,590.00 USD | `-41.20%` | `115.39` |
| `Live` | `Long` | `57.25` | 94,700,000.00 USD | 0.00 USD | 1,270.00 USD | `-41.10%` | `22.11` |
| `Live` | `Long` | `57.35` | 94,700,000.00 USD | 0.00 USD | 7,120.00 USD | `-41.00%` | `124.09` |
| `Live` | `Long` | `57.45` | 94,690,000.00 USD | 0.00 USD | 19,200.00 USD | `-40.90%` | `334.25` |
| `Live` | `Long` | `57.55` | 94,670,000.00 USD | 0.00 USD | 1,390.00 USD | `-40.79%` | `24.22` |
| `Live` | `Long` | `57.65` | 94,670,000.00 USD | 0.00 USD | 13,130.00 USD | `-40.69%` | `227.82` |
| `Live` | `Long` | `57.75` | 94,660,000.00 USD | 0.00 USD | 26,230.00 USD | `-40.59%` | `454.14` |
| `Live` | `Long` | `57.85` | 94,630,000.00 USD | 0.00 USD | 22,150.00 USD | `-40.48%` | `382.92` |
| `Live` | `Long` | `57.95` | 94,610,000.00 USD | 0.00 USD | 324.52 USD | `-40.38%` | `5.60` |
| `Live` | `Long` | `58.05` | 94,610,000.00 USD | 0.00 USD | 9,900.00 USD | `-40.28%` | `170.53` |
| `Live` | `Long` | `58.15` | 94,600,000.00 USD | 0.00 USD | 130,170.00 USD | `-40.17%` | `2,238.54` |
| `Live` | `Long` | `58.25` | 94,470,000.00 USD | 0.00 USD | 6,670.00 USD | `-40.07%` | `114.44` |
| `Live` | `Long` | `58.35` | 94,460,000.00 USD | 0.00 USD | 46,410.00 USD | `-39.97%` | `795.36` |
| `Live` | `Long` | `58.45` | 94,420,000.00 USD | 0.00 USD | 463.51 USD | `-39.87%` | `7.93` |
| `Live` | `Long` | `58.55` | 94,410,000.00 USD | 0.00 USD | 4,680.00 USD | `-39.76%` | `79.85` |
| `Live` | `Long` | `58.65` | 94,410,000.00 USD | 0.00 USD | 62,850.00 USD | `-39.66%` | `1,071.57` |
| `Live` | `Long` | `58.75` | 94,350,000.00 USD | 0.00 USD | 7,250.00 USD | `-39.56%` | `123.33` |
| `Live` | `Long` | `58.85` | 94,340,000.00 USD | 0.00 USD | 13,980.00 USD | `-39.45%` | `237.58` |
| `Live` | `Long` | `58.95` | 94,330,000.00 USD | 0.00 USD | 488.70 USD | `-39.35%` | `8.29` |
| `Live` | `Long` | `59.05` | 94,330,000.00 USD | 0.00 USD | 3,780.00 USD | `-39.25%` | `63.97` |
| `Live` | `Long` | `59.15` | 94,320,000.00 USD | 0.00 USD | 9,070.00 USD | `-39.15%` | `153.27` |
| `Live` | `Long` | `59.25` | 94,310,000.00 USD | 0.00 USD | 41,950.00 USD | `-39.04%` | `708.00` |
| `Live` | `Long` | `59.35` | 94,270,000.00 USD | 0.00 USD | 44,180.00 USD | `-38.94%` | `744.44` |
| `Live` | `Long` | `59.45` | 94,230,000.00 USD | 0.00 USD | 33,950.00 USD | `-38.84%` | `571.12` |
| `Live` | `Long` | `59.55` | 94,190,000.00 USD | 0.00 USD | 8,610.00 USD | `-38.73%` | `144.57` |
| `Live` | `Long` | `59.65` | 94,180,000.00 USD | 0.00 USD | 3,640.00 USD | `-38.63%` | `61.07` |
| `Live` | `Long` | `59.75` | 94,180,000.00 USD | 0.00 USD | 13,130.00 USD | `-38.53%` | `219.76` |
| `Live` | `Long` | `59.85` | 94,170,000.00 USD | 0.00 USD | 46,860.00 USD | `-38.43%` | `782.98` |
| `Live` | `Long` | `59.95` | 94,120,000.00 USD | 0.00 USD | 2,440,000.00 USD | `-38.32%` | `40,621.17` |
| `Live` | `Long` | `60.05` | 91,680,000.00 USD | 0.00 USD | 19,790.00 USD | `-38.22%` | `329.50` |
| `Live` | `Long` | `60.15` | 91,670,000.00 USD | 0.00 USD | 36,590.00 USD | `-38.12%` | `608.24` |
| `Live` | `Long` | `60.25` | 91,630,000.00 USD | 0.00 USD | 499.47 USD | `-38.01%` | `8.29` |
| `Live` | `Long` | `60.35` | 91,630,000.00 USD | 0.00 USD | 3,930.00 USD | `-37.91%` | `65.10` |
| `Live` | `Long` | `60.45` | 91,620,000.00 USD | 0.00 USD | 25,390.00 USD | `-37.81%` | `420.00` |
| `Live` | `Long` | `60.55` | 91,600,000.00 USD | 0.00 USD | 2,760.00 USD | `-37.71%` | `45.51` |
| `Live` | `Long` | `60.65` | 91,600,000.00 USD | 0.00 USD | 711.42 USD | `-37.60%` | `11.73` |
| `Live` | `Long` | `60.75` | 91,600,000.00 USD | 0.00 USD | 5,300.00 USD | `-37.50%` | `87.26` |
| `Live` | `Long` | `60.85` | 91,590,000.00 USD | 0.00 USD | 28,860.00 USD | `-37.40%` | `474.33` |
| `Live` | `Long` | `60.95` | 91,560,000.00 USD | 0.00 USD | 98,640.00 USD | `-37.29%` | `1,618.38` |
| `Live` | `Long` | `61.05` | 91,460,000.00 USD | 0.00 USD | 4,230.00 USD | `-37.19%` | `69.34` |
| `Live` | `Long` | `61.15` | 91,460,000.00 USD | 0.00 USD | 10,300.00 USD | `-37.09%` | `168.45` |
| `Live` | `Long` | `61.25` | 91,450,000.00 USD | 0.00 USD | 41,080.00 USD | `-36.99%` | `670.67` |
| `Live` | `Long` | `61.35` | 91,410,000.00 USD | 0.00 USD | 10,170.00 USD | `-36.88%` | `165.83` |
| `Live` | `Long` | `61.45` | 91,400,000.00 USD | 0.00 USD | 20,920.00 USD | `-36.78%` | `340.48` |
| `Live` | `Long` | `61.55` | 91,380,000.00 USD | 0.00 USD | 320.06 USD | `-36.68%` | `5.20` |
| `Live` | `Long` | `61.65` | 91,380,000.00 USD | 0.00 USD | 18,880.00 USD | `-36.57%` | `306.22` |
| `Live` | `Long` | `61.75` | 91,360,000.00 USD | 0.00 USD | 16,580.00 USD | `-36.47%` | `268.54` |
| `Live` | `Long` | `61.85` | 91,340,000.00 USD | 0.00 USD | 24,050.00 USD | `-36.37%` | `388.89` |
| `Live` | `Long` | `61.95` | 91,320,000.00 USD | 0.00 USD | 19,750.00 USD | `-36.27%` | `318.75` |
| `Live` | `Long` | `62.05` | 91,300,000.00 USD | 0.00 USD | 9,000.00 USD | `-36.16%` | `145.05` |
| `Live` | `Long` | `62.15` | 91,290,000.00 USD | 0.00 USD | 32,930.00 USD | `-36.06%` | `529.83` |
| `Live` | `Long` | `62.25` | 91,250,000.00 USD | 0.00 USD | 177,610.00 USD | `-35.96%` | `2,853.17` |
| `Live` | `Long` | `62.35` | 91,080,000.00 USD | 0.00 USD | 16,720.00 USD | `-35.85%` | `268.09` |
| `Live` | `Long` | `62.45` | 91,060,000.00 USD | 0.00 USD | 33,530.00 USD | `-35.75%` | `536.84` |
| `Live` | `Long` | `62.55` | 91,030,000.00 USD | 0.00 USD | 180,290.00 USD | `-35.65%` | `2,882.40` |
| `Live` | `Long` | `62.65` | 90,850,000.00 USD | 0.00 USD | 2,480.00 USD | `-35.55%` | `39.62` |
| `Live` | `Long` | `62.75` | 90,840,000.00 USD | 0.00 USD | 3,140.00 USD | `-35.44%` | `49.97` |
| `Live` | `Long` | `62.85` | 90,840,000.00 USD | 0.00 USD | 31,310.00 USD | `-35.34%` | `498.17` |
| `Live` | `Long` | `62.95` | 90,810,000.00 USD | 0.00 USD | 9,610.00 USD | `-35.24%` | `152.71` |
| `Live` | `Long` | `63.05` | 90,800,000.00 USD | 0.00 USD | 16,430.00 USD | `-35.13%` | `260.51` |
| `Live` | `Long` | `63.15` | 90,780,000.00 USD | 0.00 USD | 88,070.00 USD | `-35.03%` | `1,394.64` |
| `Live` | `Long` | `63.25` | 90,700,000.00 USD | 0.00 USD | 15,410.00 USD | `-34.93%` | `243.68` |
| `Live` | `Long` | `63.45` | 90,680,000.00 USD | 0.00 USD | 291.24 USD | `-34.72%` | `4.59` |
| `Live` | `Long` | `63.55` | 90,680,000.00 USD | 0.00 USD | 50,360.00 USD | `-34.62%` | `792.39` |
| `Live` | `Long` | `63.65` | 90,630,000.00 USD | 0.00 USD | 1,320.00 USD | `-34.52%` | `20.75` |
| `Live` | `Long` | `63.75` | 90,630,000.00 USD | 0.00 USD | 50,640.00 USD | `-34.41%` | `794.39` |
| `Live` | `Long` | `63.85` | 90,580,000.00 USD | 0.00 USD | 36,960.00 USD | `-34.31%` | `578.89` |
| `Live` | `Long` | `63.95` | 90,540,000.00 USD | 0.00 USD | 5,560.00 USD | `-34.21%` | `86.95` |
| `Live` | `Long` | `64.15` | 90,530,000.00 USD | 0.00 USD | 160.38 USD | `-34.00%` | `2.50` |
| `Live` | `Long` | `64.25` | 90,530,000.00 USD | 0.00 USD | 23,150.00 USD | `-33.90%` | `360.35` |
| `Live` | `Long` | `64.35` | 90,510,000.00 USD | 0.00 USD | 3,020.00 USD | `-33.80%` | `46.96` |
| `Live` | `Long` | `64.45` | 90,510,000.00 USD | 0.00 USD | 101,630.00 USD | `-33.69%` | `1,576.88` |
| `Live` | `Long` | `64.55` | 90,410,000.00 USD | 0.00 USD | 18,080.00 USD | `-33.59%` | `280.16` |
| `Live` | `Long` | `64.65` | 90,390,000.00 USD | 0.00 USD | 2,220.00 USD | `-33.49%` | `34.28` |
| `Live` | `Long` | `64.75` | 90,390,000.00 USD | 0.00 USD | 1,110.00 USD | `-33.38%` | `17.19` |
| `Live` | `Long` | `64.85` | 90,390,000.00 USD | 0.00 USD | 396.23 USD | `-33.28%` | `6.11` |
| `Live` | `Long` | `64.95` | 90,380,000.00 USD | 0.00 USD | 209.79 USD | `-33.18%` | `3.23` |
| `Live` | `Long` | `65.05` | 90,380,000.00 USD | 0.00 USD | 247,180.00 USD | `-33.08%` | `3,799.85` |
| `Live` | `Long` | `65.15` | 90,140,000.00 USD | 0.00 USD | 13,490.00 USD | `-32.97%` | `207.08` |
| `Live` | `Long` | `65.25` | 90,120,000.00 USD | 0.00 USD | 16,320.00 USD | `-32.87%` | `250.16` |
| `Live` | `Long` | `65.35` | 90,110,000.00 USD | 0.00 USD | 37,840.00 USD | `-32.77%` | `579.07` |
| `Live` | `Long` | `65.45` | 90,070,000.00 USD | 0.00 USD | 4,380.00 USD | `-32.66%` | `66.88` |
| `Live` | `Long` | `65.55` | 90,070,000.00 USD | 0.00 USD | 10,690.00 USD | `-32.56%` | `163.01` |
| `Live` | `Long` | `65.65` | 90,050,000.00 USD | 0.00 USD | 156,750.00 USD | `-32.46%` | `2,387.62` |
| `Live` | `Long` | `65.75` | 89,900,000.00 USD | 0.00 USD | 5,050.00 USD | `-32.36%` | `76.84` |
| `Live` | `Long` | `65.85` | 89,890,000.00 USD | 0.00 USD | 1,620.00 USD | `-32.25%` | `24.59` |
| `Live` | `Long` | `65.95` | 89,890,000.00 USD | 0.00 USD | 5,780.00 USD | `-32.15%` | `87.71` |
| `Live` | `Long` | `66.05` | 89,890,000.00 USD | 0.00 USD | 6,180.00 USD | `-32.05%` | `93.62` |
| `Live` | `Long` | `66.25` | 89,880,000.00 USD | 0.00 USD | 15,600.00 USD | `-31.84%` | `235.52` |
| `Live` | `Long` | `66.35` | 89,860,000.00 USD | 0.00 USD | 1,600.00 USD | `-31.74%` | `24.08` |
| `Live` | `Long` | `66.45` | 89,860,000.00 USD | 0.00 USD | 10,990.00 USD | `-31.64%` | `165.37` |
| `Live` | `Long` | `66.55` | 89,850,000.00 USD | 0.00 USD | 111,220.00 USD | `-31.53%` | `1,671.27` |
| `Live` | `Long` | `66.65` | 89,740,000.00 USD | 0.00 USD | 13,170.00 USD | `-31.43%` | `197.56` |
| `Live` | `Long` | `66.75` | 89,730,000.00 USD | 0.00 USD | 49,390.00 USD | `-31.33%` | `739.96` |
| `Live` | `Long` | `66.85` | 89,680,000.00 USD | 0.00 USD | 39,430.00 USD | `-31.22%` | `589.90` |
| `Live` | `Long` | `66.95` | 89,640,000.00 USD | 0.00 USD | 937.30 USD | `-31.12%` | `14.00` |
| `Live` | `Long` | `67.05` | 89,640,000.00 USD | 0.00 USD | 40,230.00 USD | `-31.02%` | `599.98` |
| `Live` | `Long` | `67.15` | 89,600,000.00 USD | 0.00 USD | 24,540.00 USD | `-30.92%` | `365.44` |
| `Live` | `Long` | `67.25` | 89,570,000.00 USD | 0.00 USD | 248.83 USD | `-30.81%` | `3.70` |
| `Live` | `Long` | `67.35` | 89,570,000.00 USD | 0.00 USD | 29,330.00 USD | `-30.71%` | `435.51` |
| `Live` | `Long` | `67.45` | 89,540,000.00 USD | 0.00 USD | 35,570.00 USD | `-30.61%` | `527.40` |
| `Live` | `Long` | `67.55` | 89,510,000.00 USD | 0.00 USD | 77,840.00 USD | `-30.50%` | `1,152.33` |
| `Live` | `Long` | `67.65` | 89,430,000.00 USD | 0.00 USD | 148,910.00 USD | `-30.40%` | `2,201.17` |
| `Live` | `Long` | `67.75` | 89,280,000.00 USD | 0.00 USD | 11,310.00 USD | `-30.30%` | `166.97` |
| `Live` | `Long` | `67.85` | 89,270,000.00 USD | 0.00 USD | 4,670.00 USD | `-30.20%` | `68.85` |
| `Live` | `Long` | `68.05` | 89,260,000.00 USD | 0.00 USD | 10,180.00 USD | `-29.99%` | `149.62` |
| `Live` | `Long` | `68.15` | 89,250,000.00 USD | 0.00 USD | 37,490,000.00 USD | `-29.89%` | `550,118.38` |
| `Live` | `Long` | `68.25` | 51,760,000.00 USD | 0.00 USD | 13,650.00 USD | `-29.78%` | `199.93` |
| `Live` | `Long` | `68.35` | 51,750,000.00 USD | 0.00 USD | 2,860.00 USD | `-29.68%` | `41.82` |
| `Live` | `Long` | `68.45` | 51,750,000.00 USD | 0.00 USD | 20,580.00 USD | `-29.58%` | `300.73` |
| `Live` | `Long` | `68.55` | 51,730,000.00 USD | 0.00 USD | 3,370.00 USD | `-29.48%` | `49.09` |
| `Live` | `Long` | `68.65` | 51,720,000.00 USD | 0.00 USD | 6,530.00 USD | `-29.37%` | `95.06` |
| `Live` | `Long` | `68.75` | 51,720,000.00 USD | 0.00 USD | 365,790.00 USD | `-29.27%` | `5,320.58` |
| `Live` | `Long` | `68.85` | 51,350,000.00 USD | 0.00 USD | 3,040.00 USD | `-29.17%` | `44.12` |
| `Live` | `Long` | `68.95` | 51,350,000.00 USD | 0.00 USD | 46,330.00 USD | `-29.06%` | `671.97` |
| `Live` | `Long` | `69.05` | 51,300,000.00 USD | 0.00 USD | 145.70 USD | `-28.96%` | `2.11` |
| `Live` | `Long` | `69.15` | 51,300,000.00 USD | 0.00 USD | 791,690.00 USD | `-28.86%` | `11,448.94` |
| `Live` | `Long` | `69.25` | 50,510,000.00 USD | 0.00 USD | 9,630.00 USD | `-28.76%` | `139.01` |
| `Live` | `Long` | `69.45` | 50,500,000.00 USD | 0.00 USD | 15,870.00 USD | `-28.55%` | `228.56` |
| `Live` | `Long` | `69.55` | 50,480,000.00 USD | 0.00 USD | 8,880.00 USD | `-28.45%` | `127.63` |
| `Live` | `Long` | `69.65` | 50,480,000.00 USD | 0.00 USD | 3,590.00 USD | `-28.34%` | `51.50` |
| `Live` | `Long` | `69.75` | 50,470,000.00 USD | 0.00 USD | 12,770,000.00 USD | `-28.24%` | `183,080.30` |
| `Live` | `Long` | `69.85` | 37,700,000.00 USD | 0.00 USD | 9,160.00 USD | `-28.14%` | `131.19` |
| `Live` | `Long` | `69.95` | 37,690,000.00 USD | 0.00 USD | 12,050.00 USD | `-28.03%` | `172.23` |
| `Live` | `Long` | `70.05` | 37,680,000.00 USD | 0.00 USD | 542,190.00 USD | `-27.93%` | `7,740.02` |
| `Live` | `Long` | `70.15` | 37,140,000.00 USD | 0.00 USD | 4,900.00 USD | `-27.83%` | `69.88` |
| `Live` | `Long` | `70.25` | 37,130,000.00 USD | 0.00 USD | 82,890.00 USD | `-27.73%` | `1,179.87` |
| `Live` | `Long` | `70.35` | 37,050,000.00 USD | 0.00 USD | 2,140,000.00 USD | `-27.62%` | `30,414.81` |
| `Live` | `Long` | `70.45` | 34,910,000.00 USD | 0.00 USD | 113,930.00 USD | `-27.52%` | `1,617.15` |
| `Live` | `Long` | `70.55` | 34,800,000.00 USD | 0.00 USD | 1,630.00 USD | `-27.42%` | `23.17` |
| `Live` | `Long` | `70.65` | 34,800,000.00 USD | 0.00 USD | 50,360.00 USD | `-27.31%` | `712.88` |
| `Live` | `Long` | `70.75` | 34,740,000.00 USD | 0.00 USD | 1,430,000.00 USD | `-27.21%` | `20,184.80` |
| `Live` | `Long` | `70.85` | 33,320,000.00 USD | 0.00 USD | 14,360.00 USD | `-27.11%` | `202.72` |
| `Live` | `Long` | `70.95` | 33,300,000.00 USD | 0.00 USD | 4,430.00 USD | `-27.01%` | `62.38` |
| `Live` | `Long` | `71.05` | 33,300,000.00 USD | 0.00 USD | 33,380.00 USD | `-26.90%` | `469.75` |
| `Live` | `Long` | `71.15` | 33,260,000.00 USD | 0.00 USD | 70,650.00 USD | `-26.80%` | `992.99` |
| `Live` | `Long` | `71.25` | 33,190,000.00 USD | 0.00 USD | 18,270.00 USD | `-26.70%` | `256.46` |
| `Live` | `Long` | `71.35` | 33,180,000.00 USD | 0.00 USD | 29,280.00 USD | `-26.59%` | `410.44` |
| `Live` | `Long` | `71.45` | 33,150,000.00 USD | 0.00 USD | 23,900.00 USD | `-26.49%` | `334.48` |
| `Live` | `Long` | `71.55` | 33,120,000.00 USD | 0.00 USD | 52,920.00 USD | `-26.39%` | `739.59` |
| `Live` | `Long` | `71.65` | 33,070,000.00 USD | 0.00 USD | 1,280.00 USD | `-26.29%` | `17.89` |
| `Live` | `Long` | `71.75` | 33,070,000.00 USD | 0.00 USD | 27,710.00 USD | `-26.18%` | `386.16` |
| `Live` | `Long` | `71.85` | 33,040,000.00 USD | 0.00 USD | 2,670.00 USD | `-26.08%` | `37.11` |
| `Live` | `Long` | `71.95` | 33,040,000.00 USD | 0.00 USD | 45,220.00 USD | `-25.98%` | `628.50` |
| `Live` | `Long` | `72.05` | 32,990,000.00 USD | 0.00 USD | 1,090,000.00 USD | `-25.87%` | `15,118.77` |
| `Live` | `Long` | `72.15` | 31,900,000.00 USD | 0.00 USD | 130,700.00 USD | `-25.77%` | `1,811.56` |
| `Live` | `Long` | `72.25` | 31,770,000.00 USD | 0.00 USD | 260,210.00 USD | `-25.67%` | `3,601.59` |
| `Live` | `Long` | `72.35` | 31,510,000.00 USD | 0.00 USD | 29,100.00 USD | `-25.57%` | `402.20` |
| `Live` | `Long` | `72.45` | 31,480,000.00 USD | 0.00 USD | 1,590.00 USD | `-25.46%` | `22.01` |
| `Live` | `Long` | `72.55` | 31,480,000.00 USD | 0.00 USD | 17,280.00 USD | `-25.36%` | `238.13` |
| `Live` | `Long` | `72.65` | 31,460,000.00 USD | 0.00 USD | 35,010.00 USD | `-25.26%` | `481.90` |
| `Live` | `Long` | `72.75` | 31,430,000.00 USD | 0.00 USD | 3,100.00 USD | `-25.15%` | `42.56` |
| `Live` | `Long` | `72.85` | 31,430,000.00 USD | 0.00 USD | 186,830.00 USD | `-25.05%` | `2,564.61` |
| `Live` | `Long` | `72.95` | 31,240,000.00 USD | 0.00 USD | 5,600.00 USD | `-24.95%` | `76.71` |
| `Live` | `Long` | `73.05` | 31,230,000.00 USD | 0.00 USD | 32,880.00 USD | `-24.85%` | `450.09` |
| `Live` | `Long` | `73.15` | 31,200,000.00 USD | 0.00 USD | 17,430.00 USD | `-24.74%` | `238.30` |
| `Live` | `Long` | `73.25` | 31,180,000.00 USD | 0.00 USD | 41,540.00 USD | `-24.64%` | `567.12` |
| `Live` | `Long` | `73.35` | 31,140,000.00 USD | 0.00 USD | 10,250.00 USD | `-24.54%` | `139.73` |
| `Live` | `Long` | `73.45` | 31,130,000.00 USD | 0.00 USD | 5,350.00 USD | `-24.43%` | `72.82` |
| `Live` | `Long` | `73.55` | 31,130,000.00 USD | 0.00 USD | 15,600.00 USD | `-24.33%` | `212.14` |
| `Live` | `Long` | `73.65` | 31,110,000.00 USD | 0.00 USD | 37,850.00 USD | `-24.23%` | `513.85` |
| `Live` | `Long` | `73.75` | 31,070,000.00 USD | 0.00 USD | 70,280.00 USD | `-24.13%` | `952.95` |
| `Live` | `Long` | `73.85` | 31,000,000.00 USD | 0.00 USD | 11,710.00 USD | `-24.02%` | `158.63` |
| `Live` | `Long` | `73.95` | 30,990,000.00 USD | 0.00 USD | 40,040.00 USD | `-23.92%` | `541.40` |
| `Live` | `Long` | `74.05` | 30,950,000.00 USD | 0.00 USD | 24,560.00 USD | `-23.82%` | `331.73` |
| `Live` | `Long` | `74.15` | 30,930,000.00 USD | 0.00 USD | 21,430.00 USD | `-23.71%` | `289.03` |
| `Live` | `Long` | `74.25` | 30,910,000.00 USD | 0.00 USD | 27,320.00 USD | `-23.61%` | `367.91` |
| `Live` | `Long` | `74.35` | 30,880,000.00 USD | 0.00 USD | 39,600.00 USD | `-23.51%` | `532.62` |
| `Live` | `Long` | `74.45` | 30,840,000.00 USD | 0.00 USD | 27,460.00 USD | `-23.41%` | `368.85` |
| `Live` | `Long` | `74.55` | 30,810,000.00 USD | 0.00 USD | 6,260.00 USD | `-23.30%` | `84.00` |
| `Live` | `Long` | `74.65` | 30,800,000.00 USD | 0.00 USD | 10,450.00 USD | `-23.20%` | `140.05` |
| `Live` | `Long` | `74.75` | 30,790,000.00 USD | 0.00 USD | 123,070.00 USD | `-23.10%` | `1,646.41` |
| `Live` | `Long` | `74.85` | 30,670,000.00 USD | 0.00 USD | 134,930.00 USD | `-22.99%` | `1,802.70` |
| `Live` | `Long` | `74.95` | 30,540,000.00 USD | 0.00 USD | 18,610.00 USD | `-22.89%` | `248.31` |
| `Live` | `Long` | `75.05` | 30,520,000.00 USD | 0.00 USD | 40,670.00 USD | `-22.79%` | `541.85` |
| `Live` | `Long` | `75.25` | 30,480,000.00 USD | 0.00 USD | 287,360.00 USD | `-22.58%` | `3,818.68` |
| `Live` | `Long` | `75.35` | 30,190,000.00 USD | 0.00 USD | 21,080.00 USD | `-22.48%` | `279.73` |
| `Live` | `Long` | `75.45` | 30,170,000.00 USD | 0.00 USD | 33,560.00 USD | `-22.38%` | `444.85` |
| `Live` | `Long` | `75.55` | 30,130,000.00 USD | 0.00 USD | 1,650,000.00 USD | `-22.27%` | `21,889.29` |
| `Live` | `Long` | `75.65` | 28,480,000.00 USD | 0.00 USD | 130,250.00 USD | `-22.17%` | `1,721.70` |
| `Live` | `Long` | `75.75` | 28,350,000.00 USD | 0.00 USD | 53,060.00 USD | `-22.07%` | `700.51` |
| `Live` | `Long` | `75.85` | 28,300,000.00 USD | 0.00 USD | 2,880.00 USD | `-21.97%` | `37.95` |
| `Live` | `Long` | `75.95` | 28,290,000.00 USD | 0.00 USD | 37,010.00 USD | `-21.86%` | `487.32` |
| `Live` | `Long` | `76.05` | 28,260,000.00 USD | 0.00 USD | 6,260.00 USD | `-21.76%` | `82.27` |
| `Live` | `Long` | `76.15` | 28,250,000.00 USD | 0.00 USD | 4,370.00 USD | `-21.66%` | `57.43` |
| `Live` | `Long` | `76.25` | 28,250,000.00 USD | 0.00 USD | 10,140.00 USD | `-21.55%` | `133.04` |
| `Live` | `Long` | `76.35` | 28,240,000.00 USD | 0.00 USD | 41,020.00 USD | `-21.45%` | `537.32` |
| `Live` | `Long` | `76.45` | 28,200,000.00 USD | 0.00 USD | 1,490,000.00 USD | `-21.35%` | `19,460.09` |
| `Live` | `Long` | `76.55` | 26,710,000.00 USD | 0.00 USD | 37,610.00 USD | `-21.24%` | `491.36` |
| `Live` | `Long` | `76.65` | 26,670,000.00 USD | 0.00 USD | 55,910.00 USD | `-21.14%` | `729.36` |
| `Live` | `Long` | `76.75` | 26,610,000.00 USD | 0.00 USD | 29,450.00 USD | `-21.04%` | `383.75` |
| `Live` | `Long` | `76.85` | 26,590,000.00 USD | 0.00 USD | 134,000.00 USD | `-20.94%` | `1,743.66` |
| `Live` | `Long` | `76.95` | 26,450,000.00 USD | 0.00 USD | 41,940.00 USD | `-20.83%` | `545.09` |
| `Live` | `Long` | `77.05` | 26,410,000.00 USD | 0.00 USD | 80,610.00 USD | `-20.73%` | `1,046.25` |
| `Live` | `Long` | `77.15` | 26,330,000.00 USD | 0.00 USD | 84,180.00 USD | `-20.63%` | `1,091.07` |
| `Live` | `Long` | `77.25` | 26,240,000.00 USD | 0.00 USD | 25,020.00 USD | `-20.52%` | `323.94` |
| `Live` | `Long` | `77.35` | 26,220,000.00 USD | 0.00 USD | 36,280.00 USD | `-20.42%` | `468.99` |
| `Live` | `Long` | `77.45` | 26,180,000.00 USD | 0.00 USD | 40,590.00 USD | `-20.32%` | `524.13` |
| `Live` | `Long` | `77.55` | 26,140,000.00 USD | 0.00 USD | 12,900.00 USD | `-20.22%` | `166.30` |
| `Live` | `Long` | `77.75` | 26,130,000.00 USD | 0.00 USD | 20,230.00 USD | `-20.01%` | `260.19` |
| `Live` | `Long` | `77.85` | 26,110,000.00 USD | 0.00 USD | 81,170.00 USD | `-19.91%` | `1,042.65` |
| `Live` | `Long` | `77.95` | 26,030,000.00 USD | 0.00 USD | 8,370.00 USD | `-19.80%` | `107.32` |
| `Live` | `Long` | `78.05` | 26,020,000.00 USD | 0.00 USD | 21,520.00 USD | `-19.70%` | `275.71` |
| `Live` | `Long` | `78.15` | 26,000,000.00 USD | 0.00 USD | 65,600.00 USD | `-19.60%` | `839.39` |
| `Live` | `Long` | `78.25` | 25,930,000.00 USD | 0.00 USD | 39,440.00 USD | `-19.50%` | `504.08` |
| `Live` | `Long` | `78.35` | 25,890,000.00 USD | 0.00 USD | 55,060.00 USD | `-19.39%` | `702.76` |
| `Live` | `Long` | `78.45` | 25,840,000.00 USD | 0.00 USD | 29,370.00 USD | `-19.29%` | `374.40` |
| `Live` | `Long` | `78.55` | 25,810,000.00 USD | 0.00 USD | 5,740.00 USD | `-19.19%` | `73.09` |
| `Live` | `Long` | `78.65` | 25,800,000.00 USD | 0.00 USD | 32,860.00 USD | `-19.08%` | `417.75` |
| `Live` | `Long` | `78.75` | 25,770,000.00 USD | 0.00 USD | 52,670.00 USD | `-18.98%` | `668.88` |
| `Live` | `Long` | `78.85` | 25,720,000.00 USD | 0.00 USD | 240,940.00 USD | `-18.88%` | `3,055.65` |
| `Live` | `Long` | `78.95` | 25,480,000.00 USD | 0.00 USD | 2,270.00 USD | `-18.78%` | `28.81` |
| `Live` | `Long` | `79.05` | 25,470,000.00 USD | 0.00 USD | 6,490.00 USD | `-18.67%` | `82.14` |
| `Live` | `Long` | `79.15` | 25,470,000.00 USD | 0.00 USD | 128,420.00 USD | `-18.57%` | `1,622.43` |
| `Live` | `Long` | `79.25` | 25,340,000.00 USD | 0.00 USD | 47,570.00 USD | `-18.47%` | `600.23` |
| `Live` | `Long` | `79.35` | 25,290,000.00 USD | 0.00 USD | 20,900.00 USD | `-18.36%` | `263.44` |
| `Live` | `Long` | `79.45` | 25,270,000.00 USD | 0.00 USD | 8,800.00 USD | `-18.26%` | `110.73` |
| `Live` | `Long` | `79.55` | 25,260,000.00 USD | 0.00 USD | 1,900.00 USD | `-18.16%` | `23.91` |
| `Live` | `Long` | `79.65` | 25,260,000.00 USD | 0.00 USD | 19,960.00 USD | `-18.06%` | `250.58` |
| `Live` | `Long` | `79.75` | 25,240,000.00 USD | 0.00 USD | 13,190.00 USD | `-17.95%` | `165.41` |
| `Live` | `Long` | `79.85` | 25,230,000.00 USD | 0.00 USD | 14,710.00 USD | `-17.85%` | `184.18` |
| `Live` | `Long` | `79.95` | 25,210,000.00 USD | 0.00 USD | 189,340.00 USD | `-17.75%` | `2,368.25` |
| `Live` | `Long` | `80.05` | 25,020,000.00 USD | 0.00 USD | 14,790.00 USD | `-17.64%` | `184.74` |
| `Live` | `Long` | `80.15` | 25,010,000.00 USD | 0.00 USD | 31,900.00 USD | `-17.54%` | `398.06` |
| `Live` | `Long` | `80.25` | 24,980,000.00 USD | 0.00 USD | 57,660.00 USD | `-17.44%` | `718.54` |
| `Live` | `Long` | `80.35` | 24,920,000.00 USD | 0.00 USD | 132,270.00 USD | `-17.34%` | `1,646.22` |
| `Live` | `Long` | `80.45` | 24,790,000.00 USD | 0.00 USD | 20,100.00 USD | `-17.23%` | `249.79` |
| `Live` | `Long` | `80.55` | 24,770,000.00 USD | 0.00 USD | 15,600.00 USD | `-17.13%` | `193.65` |
| `Live` | `Long` | `80.65` | 24,750,000.00 USD | 0.00 USD | 77,670.00 USD | `-17.03%` | `963.09` |
| `Live` | `Long` | `80.75` | 24,670,000.00 USD | 0.00 USD | 33,470.00 USD | `-16.92%` | `414.46` |
| `Live` | `Long` | `80.85` | 24,640,000.00 USD | 0.00 USD | 449,860.00 USD | `-16.82%` | `5,564.16` |
| `Live` | `Long` | `80.95` | 24,190,000.00 USD | 0.00 USD | 10,620.00 USD | `-16.72%` | `131.18` |
| `Live` | `Long` | `81.05` | 24,180,000.00 USD | 0.00 USD | 2,250,000.00 USD | `-16.62%` | `27,783.98` |
| `Live` | `Long` | `81.15` | 21,930,000.00 USD | 0.00 USD | 101,800.00 USD | `-16.51%` | `1,254.44` |
| `Live` | `Long` | `81.25` | 21,830,000.00 USD | 0.00 USD | 22,790.00 USD | `-16.41%` | `280.49` |
| `Live` | `Long` | `81.35` | 21,800,000.00 USD | 0.00 USD | 56,470.00 USD | `-16.31%` | `694.17` |
| `Live` | `Long` | `81.45` | 21,750,000.00 USD | 0.00 USD | 59,690.00 USD | `-16.20%` | `732.84` |
| `Live` | `Long` | `81.55` | 21,690,000.00 USD | 0.00 USD | 190,680.00 USD | `-16.10%` | `2,338.18` |
| `Live` | `Long` | `81.65` | 21,500,000.00 USD | 0.00 USD | 15,590.00 USD | `-16.00%` | `190.89` |
| `Live` | `Long` | `81.75` | 21,480,000.00 USD | 0.00 USD | 19,020.00 USD | `-15.90%` | `232.64` |
| `Live` | `Long` | `81.85` | 21,460,000.00 USD | 0.00 USD | 36,460.00 USD | `-15.79%` | `445.40` |
| `Live` | `Long` | `81.95` | 21,420,000.00 USD | 0.00 USD | 22,190.00 USD | `-15.69%` | `270.82` |
| `Live` | `Long` | `82.05` | 21,400,000.00 USD | 0.00 USD | 117,060.00 USD | `-15.59%` | `1,426.69` |
| `Live` | `Long` | `82.15` | 21,290,000.00 USD | 0.00 USD | 808,740.00 USD | `-15.48%` | `9,844.70` |
| `Live` | `Long` | `82.25` | 20,480,000.00 USD | 0.00 USD | 50,310.00 USD | `-15.38%` | `611.69` |
| `Live` | `Long` | `82.35` | 20,430,000.00 USD | 0.00 USD | 166,860.00 USD | `-15.28%` | `2,026.20` |
| `Live` | `Long` | `82.45` | 20,260,000.00 USD | 0.00 USD | 214,440.00 USD | `-15.17%` | `2,600.88` |
| `Live` | `Long` | `82.55` | 20,050,000.00 USD | 0.00 USD | 27,730.00 USD | `-15.07%` | `335.97` |
| `Live` | `Long` | `82.65` | 20,020,000.00 USD | 0.00 USD | 98,590.00 USD | `-14.97%` | `1,192.87` |
| `Live` | `Long` | `82.75` | 19,920,000.00 USD | 0.00 USD | 7,950.00 USD | `-14.87%` | `96.13` |
| `Live` | `Long` | `82.85` | 19,910,000.00 USD | 0.00 USD | 23,000.00 USD | `-14.76%` | `277.57` |
| `Live` | `Long` | `82.95` | 19,890,000.00 USD | 0.00 USD | 29,750.00 USD | `-14.66%` | `358.59` |
| `Live` | `Long` | `83.05` | 19,860,000.00 USD | 0.00 USD | 137,530.00 USD | `-14.56%` | `1,655.98` |
| `Live` | `Long` | `83.15` | 19,720,000.00 USD | 0.00 USD | 52,900.00 USD | `-14.45%` | `636.22` |
| `Live` | `Long` | `83.25` | 19,670,000.00 USD | 0.00 USD | 153,060.00 USD | `-14.35%` | `1,838.55` |
| `Live` | `Long` | `83.35` | 19,510,000.00 USD | 0.00 USD | 637,030.00 USD | `-14.25%` | `7,642.86` |
| `Live` | `Long` | `83.45` | 18,880,000.00 USD | 0.00 USD | 55,880.00 USD | `-14.15%` | `669.57` |
| `Live` | `Long` | `83.55` | 18,820,000.00 USD | 0.00 USD | 65,570.00 USD | `-14.04%` | `784.75` |
| `Live` | `Long` | `83.65` | 18,760,000.00 USD | 0.00 USD | 76,120.00 USD | `-13.94%` | `909.99` |
| `Live` | `Long` | `83.75` | 18,680,000.00 USD | 0.00 USD | 81,510.00 USD | `-13.84%` | `973.24` |
| `Live` | `Long` | `83.85` | 18,600,000.00 USD | 0.00 USD | 13,630.00 USD | `-13.73%` | `162.57` |
| `Live` | `Long` | `83.95` | 18,590,000.00 USD | 0.00 USD | 842,760.00 USD | `-13.63%` | `10,038.79` |
| `Live` | `Long` | `84.05` | 17,740,000.00 USD | 0.00 USD | 113,720.00 USD | `-13.53%` | `1,353.03` |
| `Live` | `Long` | `84.15` | 17,630,000.00 USD | 0.00 USD | 65,310.00 USD | `-13.43%` | `776.06` |
| `Live` | `Long` | `84.25` | 17,560,000.00 USD | 0.00 USD | 46,440.00 USD | `-13.32%` | `551.21` |
| `Live` | `Long` | `84.35` | 17,520,000.00 USD | 0.00 USD | 25,180.00 USD | `-13.22%` | `298.47` |
| `Live` | `Long` | `84.45` | 17,490,000.00 USD | 0.00 USD | 85,770.00 USD | `-13.12%` | `1,015.66` |
| `Live` | `Long` | `84.55` | 17,410,000.00 USD | 0.00 USD | 1,230,000.00 USD | `-13.01%` | `14,555.22` |
| `Live` | `Long` | `84.65` | 16,180,000.00 USD | 0.00 USD | 261,450.00 USD | `-12.91%` | `3,088.60` |
| `Live` | `Long` | `84.75` | 15,910,000.00 USD | 0.00 USD | 289,310.00 USD | `-12.81%` | `3,413.65` |
| `Live` | `Long` | `84.85` | 15,620,000.00 USD | 0.00 USD | 94,510.00 USD | `-12.71%` | `1,113.86` |
| `Live` | `Long` | `84.95` | 15,530,000.00 USD | 0.00 USD | 617.59 USD | `-12.60%` | `7.27` |
| `Live` | `Long` | `85.05` | 15,530,000.00 USD | 0.00 USD | 15,920.00 USD | `-12.50%` | `187.17` |
| `Live` | `Long` | `85.15` | 15,510,000.00 USD | 0.00 USD | 5,400.00 USD | `-12.40%` | `63.38` |
| `Live` | `Long` | `85.25` | 15,510,000.00 USD | 0.00 USD | 609,970.00 USD | `-12.29%` | `7,155.05` |
| `Live` | `Long` | `85.35` | 14,900,000.00 USD | 0.00 USD | 21,250.00 USD | `-12.19%` | `248.94` |
| `Live` | `Long` | `85.45` | 14,880,000.00 USD | 0.00 USD | 52,900.00 USD | `-12.09%` | `619.05` |
| `Live` | `Long` | `85.55` | 14,820,000.00 USD | 0.00 USD | 10,360.00 USD | `-11.99%` | `121.14` |
| `Live` | `Long` | `85.65` | 14,810,000.00 USD | 0.00 USD | 53,210.00 USD | `-11.88%` | `621.29` |
| `Live` | `Long` | `85.75` | 14,760,000.00 USD | 0.00 USD | 23,470.00 USD | `-11.78%` | `273.76` |
| `Live` | `Long` | `85.85` | 14,740,000.00 USD | 0.00 USD | 69,910.00 USD | `-11.68%` | `814.28` |
| `Live` | `Long` | `85.95` | 14,670,000.00 USD | 0.00 USD | 363,970.00 USD | `-11.57%` | `4,234.72` |
| `Live` | `Long` | `86.05` | 14,300,000.00 USD | 0.00 USD | 276,690.00 USD | `-11.47%` | `3,215.43` |
| `Live` | `Long` | `86.15` | 14,030,000.00 USD | 0.00 USD | 68,570.00 USD | `-11.37%` | `795.91` |
| `Live` | `Long` | `86.25` | 13,960,000.00 USD | 0.00 USD | 52,990.00 USD | `-11.27%` | `614.34` |
| `Live` | `Long` | `86.35` | 13,900,000.00 USD | 0.00 USD | 5,680.00 USD | `-11.16%` | `65.77` |
| `Live` | `Long` | `86.45` | 13,900,000.00 USD | 0.00 USD | 187,940.00 USD | `-11.06%` | `2,174.00` |
| `Live` | `Long` | `86.55` | 13,710,000.00 USD | 0.00 USD | 43,510.00 USD | `-10.96%` | `502.72` |
| `Live` | `Long` | `86.65` | 13,670,000.00 USD | 0.00 USD | 190,730.00 USD | `-10.85%` | `2,201.12` |
| `Live` | `Long` | `86.75` | 13,480,000.00 USD | 0.00 USD | 34,660.00 USD | `-10.75%` | `399.50` |
| `Live` | `Long` | `86.85` | 13,440,000.00 USD | 0.00 USD | 78,950.00 USD | `-10.65%` | `909.01` |
| `Live` | `Long` | `86.95` | 13,360,000.00 USD | 0.00 USD | 152,510.00 USD | `-10.55%` | `1,754.01` |
| `Live` | `Long` | `87.05` | 13,210,000.00 USD | 0.00 USD | 30,820.00 USD | `-10.44%` | `354.08` |
| `Live` | `Long` | `87.15` | 13,180,000.00 USD | 0.00 USD | 4,410.00 USD | `-10.34%` | `50.58` |
| `Live` | `Long` | `87.25` | 13,180,000.00 USD | 0.00 USD | 92,480.00 USD | `-10.24%` | `1,059.91` |
| `Live` | `Long` | `87.35` | 13,080,000.00 USD | 0.00 USD | 72,050.00 USD | `-10.13%` | `824.89` |
| `Live` | `Long` | `87.45` | 13,010,000.00 USD | 0.00 USD | 149,740.00 USD | `-10.03%` | `1,712.27` |
| `Live` | `Long` | `87.55` | 12,860,000.00 USD | 0.00 USD | 128,700.00 USD | `-9.93%` | `1,470.04` |
| `Live` | `Long` | `87.65` | 12,730,000.00 USD | 0.00 USD | 105,660.00 USD | `-9.83%` | `1,205.42` |
| `Live` | `Long` | `87.75` | 12,630,000.00 USD | 0.00 USD | 90,160.00 USD | `-9.72%` | `1,027.45` |
| `Live` | `Long` | `87.85` | 12,540,000.00 USD | 0.00 USD | 66,830.00 USD | `-9.62%` | `760.69` |
| `Live` | `Long` | `87.95` | 12,470,000.00 USD | 0.00 USD | 9,000.00 USD | `-9.52%` | `102.33` |
| `Live` | `Long` | `88.05` | 12,460,000.00 USD | 0.00 USD | 157,110.00 USD | `-9.41%` | `1,784.38` |
| `Live` | `Long` | `88.15` | 12,300,000.00 USD | 0.00 USD | 25,750.00 USD | `-9.31%` | `292.10` |
| `Live` | `Long` | `88.25` | 12,280,000.00 USD | 0.00 USD | 74,760.00 USD | `-9.21%` | `847.09` |
| `Live` | `Long` | `88.35` | 12,200,000.00 USD | 0.00 USD | 26,970.00 USD | `-9.10%` | `305.29` |
| `Live` | `Long` | `88.45` | 12,180,000.00 USD | 0.00 USD | 64,640.00 USD | `-9.00%` | `730.78` |
| `Live` | `Long` | `88.55` | 12,110,000.00 USD | 0.00 USD | 267,270.00 USD | `-8.90%` | `3,018.28` |
| `Live` | `Long` | `88.65` | 11,840,000.00 USD | 0.00 USD | 95,980.00 USD | `-8.80%` | `1,082.67` |
| `Live` | `Long` | `88.75` | 11,750,000.00 USD | 0.00 USD | 236,310.00 USD | `-8.69%` | `2,662.68` |
| `Live` | `Long` | `88.85` | 11,510,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-8.59%` | `11,998.13` |
| `Live` | `Long` | `88.95` | 10,450,000.00 USD | 0.00 USD | 32,790.00 USD | `-8.49%` | `368.66` |
| `Live` | `Long` | `89.05` | 10,410,000.00 USD | 0.00 USD | 29,770.00 USD | `-8.38%` | `334.27` |
| `Live` | `Long` | `89.15` | 10,380,000.00 USD | 0.00 USD | 160,380.00 USD | `-8.28%` | `1,798.99` |
| `Live` | `Long` | `89.25` | 10,220,000.00 USD | 0.00 USD | 31,740.00 USD | `-8.18%` | `355.61` |
| `Live` | `Long` | `89.35` | 10,190,000.00 USD | 0.00 USD | 29,540.00 USD | `-8.08%` | `330.60` |
| `Live` | `Long` | `89.45` | 10,160,000.00 USD | 0.00 USD | 429,190.00 USD | `-7.97%` | `4,798.06` |
| `Live` | `Long` | `89.55` | 9,730,000.00 USD | 0.00 USD | 39,790.00 USD | `-7.87%` | `444.38` |
| `Live` | `Long` | `89.65` | 9,690,000.00 USD | 0.00 USD | 17,750.00 USD | `-7.77%` | `197.96` |
| `Live` | `Long` | `89.75` | 9,680,000.00 USD | 0.00 USD | 146,450.00 USD | `-7.66%` | `1,631.73` |
| `Live` | `Long` | `89.85` | 9,530,000.00 USD | 0.00 USD | 59,040.00 USD | `-7.56%` | `657.09` |
| `Live` | `Long` | `89.95` | 9,470,000.00 USD | 0.00 USD | 136,370.00 USD | `-7.46%` | `1,516.04` |
| `Live` | `Long` | `90.05` | 9,330,000.00 USD | 0.00 USD | 73,280.00 USD | `-7.36%` | `813.81` |
| `Live` | `Long` | `90.15` | 9,260,000.00 USD | 0.00 USD | 60,790.00 USD | `-7.25%` | `674.32` |
| `Live` | `Long` | `90.25` | 9,200,000.00 USD | 0.00 USD | 26,880.00 USD | `-7.15%` | `297.79` |
| `Live` | `Long` | `90.35` | 9,170,000.00 USD | 0.00 USD | 77,850.00 USD | `-7.05%` | `861.69` |
| `Live` | `Long` | `90.45` | 9,090,000.00 USD | 0.00 USD | 50,450.00 USD | `-6.94%` | `557.79` |
| `Live` | `Long` | `90.55` | 9,040,000.00 USD | 0.00 USD | 29,950.00 USD | `-6.84%` | `330.71` |
| `Live` | `Long` | `90.65` | 9,010,000.00 USD | 0.00 USD | 131,550.00 USD | `-6.74%` | `1,451.20` |
| `Live` | `Long` | `90.75` | 8,880,000.00 USD | 0.00 USD | 107,810.00 USD | `-6.64%` | `1,187.98` |
| `Live` | `Long` | `90.85` | 8,770,000.00 USD | 0.00 USD | 73,530.00 USD | `-6.53%` | `809.39` |
| `Live` | `Long` | `90.95` | 8,700,000.00 USD | 0.00 USD | 16,410.00 USD | `-6.43%` | `180.44` |
| `Live` | `Long` | `91.05` | 8,680,000.00 USD | 0.00 USD | 389,480.00 USD | `-6.33%` | `4,277.65` |
| `Live` | `Long` | `91.15` | 8,300,000.00 USD | 0.00 USD | 373,670.00 USD | `-6.22%` | `4,099.56` |
| `Live` | `Long` | `91.25` | 7,920,000.00 USD | 0.00 USD | 29,640.00 USD | `-6.12%` | `324.80` |
| `Live` | `Long` | `91.35` | 7,890,000.00 USD | 0.00 USD | 14,960.00 USD | `-6.02%` | `163.74` |
| `Live` | `Long` | `91.45` | 7,880,000.00 USD | 0.00 USD | 331,850.00 USD | `-5.92%` | `3,628.80` |
| `Live` | `Long` | `91.55` | 7,550,000.00 USD | 0.00 USD | 1,210,000.00 USD | `-5.81%` | `13,204.29` |
| `Live` | `Long` | `91.65` | 6,340,000.00 USD | 0.00 USD | 1,430,000.00 USD | `-5.71%` | `15,594.68` |
| `Live` | `Long` | `91.75` | 4,910,000.00 USD | 0.00 USD | 240,910.00 USD | `-5.61%` | `2,625.74` |
| `Live` | `Long` | `91.85` | 4,670,000.00 USD | 0.00 USD | 43,170.00 USD | `-5.50%` | `470.02` |
| `Live` | `Long` | `91.95` | 4,620,000.00 USD | 0.00 USD | 64,120.00 USD | `-5.40%` | `697.35` |
| `Live` | `Long` | `92.05` | 4,560,000.00 USD | 0.00 USD | 168,710.00 USD | `-5.30%` | `1,832.79` |
| `Live` | `Long` | `92.15` | 4,390,000.00 USD | 0.00 USD | 328,530.00 USD | `-5.20%` | `3,565.15` |
| `Live` | `Long` | `92.25` | 4,060,000.00 USD | 0.00 USD | 170,110.00 USD | `-5.09%` | `1,844.03` |
| `Live` | `Long` | `92.35` | 3,890,000.00 USD | 0.00 USD | 304,990.00 USD | `-4.99%` | `3,302.52` |
| `Live` | `Long` | `92.45` | 3,590,000.00 USD | 0.00 USD | 117,820.00 USD | `-4.89%` | `1,274.42` |
| `Live` | `Long` | `92.55` | 3,470,000.00 USD | 0.00 USD | 4,870.00 USD | `-4.78%` | `52.65` |
| `Live` | `Long` | `92.65` | 3,460,000.00 USD | 0.00 USD | 15,170.00 USD | `-4.68%` | `163.78` |
| `Live` | `Long` | `92.75` | 3,450,000.00 USD | 0.00 USD | 4,920.00 USD | `-4.58%` | `53.04` |
| `Live` | `Long` | `92.85` | 3,440,000.00 USD | 0.00 USD | 23,420.00 USD | `-4.48%` | `252.19` |
| `Live` | `Long` | `92.95` | 3,420,000.00 USD | 0.00 USD | 3,780.00 USD | `-4.37%` | `40.66` |
| `Live` | `Long` | `93.05` | 3,420,000.00 USD | 0.00 USD | 29,610.00 USD | `-4.27%` | `318.21` |
| `Live` | `Long` | `93.15` | 3,390,000.00 USD | 0.00 USD | 319,790.00 USD | `-4.17%` | `3,433.03` |
| `Live` | `Long` | `93.25` | 3,070,000.00 USD | 0.00 USD | 105,430.00 USD | `-4.06%` | `1,130.62` |
| `Live` | `Long` | `93.35` | 2,960,000.00 USD | 0.00 USD | 13,390.00 USD | `-3.96%` | `143.46` |
| `Live` | `Long` | `93.45` | 2,950,000.00 USD | 0.00 USD | 8,060.00 USD | `-3.86%` | `86.26` |
| `Live` | `Long` | `93.55` | 2,940,000.00 USD | 0.00 USD | 19,360.00 USD | `-3.76%` | `206.98` |
| `Live` | `Long` | `93.65` | 2,920,000.00 USD | 0.00 USD | 937,160.00 USD | `-3.65%` | `10,007.00` |
| `Live` | `Long` | `93.75` | 1,980,000.00 USD | 0.00 USD | 10,870.00 USD | `-3.55%` | `115.91` |
| `Live` | `Long` | `93.85` | 1,970,000.00 USD | 0.00 USD | 11,870.00 USD | `-3.45%` | `126.50` |
| `Live` | `Long` | `93.95` | 1,960,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-3.34%` | `12,128.34` |
| `Live` | `Long` | `94.05` | 821,600.00 USD | 0.00 USD | 4,190.00 USD | `-3.24%` | `44.53` |
| `Live` | `Long` | `94.15` | 817,410.00 USD | 0.00 USD | 29,950.00 USD | `-3.14%` | `318.16` |
| `Live` | `Long` | `94.25` | 787,460.00 USD | 0.00 USD | 8,860.00 USD | `-3.03%` | `93.98` |
| `Live` | `Long` | `94.35` | 778,600.00 USD | 0.00 USD | 5,200.00 USD | `-2.93%` | `55.11` |
| `Live` | `Long` | `94.45` | 773,400.00 USD | 0.00 USD | 146,220.00 USD | `-2.83%` | `1,548.16` |
| `Live` | `Long` | `94.55` | 627,170.00 USD | 0.00 USD | 60,600.00 USD | `-2.73%` | `640.93` |
| `Live` | `Short` | `94.65` | 28,740.00 USD | 28,740.00 USD | 0.00 USD | `-2.62%` | `303.69` |
| `Live` | `Long` | `94.75` | 566,570.00 USD | 0.00 USD | 82,810.00 USD | `-2.52%` | `873.94` |
| `Live` | `Long` | `94.85` | 483,770.00 USD | 0.00 USD | 54,830.00 USD | `-2.42%` | `578.03` |
| `Live` | `Long` | `94.95` | 428,940.00 USD | 0.00 USD | 58,350.00 USD | `-2.31%` | `614.55` |
| `Live` | `Long` | `95.05` | 370,590.00 USD | 0.00 USD | 57,060.00 USD | `-2.21%` | `600.29` |
| `Live` | `Long` | `95.15` | 313,530.00 USD | 0.00 USD | 21,470.00 USD | `-2.11%` | `225.63` |
| `Live` | `Long` | `95.25` | 292,060.00 USD | 0.00 USD | 42,730.00 USD | `-2.01%` | `448.66` |
| `Live` | `Long` | `95.35` | 249,330.00 USD | 0.00 USD | 7,550.00 USD | `-1.90%` | `79.19` |
| `Live` | `Long` | `95.45` | 241,780.00 USD | 0.00 USD | 24,230.00 USD | `-1.80%` | `253.81` |
| `Live` | `Long` | `95.55` | 217,550.00 USD | 0.00 USD | 44,760.00 USD | `-1.70%` | `468.49` |
| `Live` | `Long` | `95.65` | 172,790.00 USD | 0.00 USD | 92,490.00 USD | `-1.59%` | `966.99` |
| `Live` | `Long` | `95.75` | 80,300.00 USD | 0.00 USD | 49,350.00 USD | `-1.49%` | `515.41` |
| `Live` | `Long` | `95.85` | 30,950.00 USD | 0.00 USD | 30,710.00 USD | `-1.39%` | `320.44` |
| `Live` | `Long` | `95.95` | 231.24 USD | 0.00 USD | 231.24 USD | `-1.29%` | `2.41` |
| `Live` | `Short` | `97.75` | 29,970.00 USD | 1,220.00 USD | 0.00 USD | `+0.57%` | `12.49` |
| `Live` | `Short` | `98.55` | 35,890.00 USD | 5,930.00 USD | 0.00 USD | `+1.39%` | `60.17` |
| `Live` | `Short` | `98.65` | 45,630.00 USD | 9,740.00 USD | 0.00 USD | `+1.49%` | `98.70` |
| `Live` | `Short` | `98.95` | 46,650.00 USD | 1,020.00 USD | 0.00 USD | `+1.80%` | `10.28` |
| `Live` | `Short` | `99.05` | 50,260.00 USD | 3,610.00 USD | 0.00 USD | `+1.90%` | `36.45` |
| `Live` | `Short` | `99.15` | 1,160,000.00 USD | 1,110,000.00 USD | 0.00 USD | `+2.01%` | `11,226.96` |
| `Live` | `Short` | `99.25` | 1,240,000.00 USD | 72,450.00 USD | 0.00 USD | `+2.11%` | `729.96` |
| `Live` | `Short` | `99.35` | 1,330,000.00 USD | 92,510.00 USD | 0.00 USD | `+2.21%` | `931.19` |
| `Live` | `Short` | `99.45` | 1,350,000.00 USD | 19,710.00 USD | 0.00 USD | `+2.31%` | `198.16` |
| `Live` | `Short` | `99.55` | 1,490,000.00 USD | 138,120.00 USD | 0.00 USD | `+2.42%` | `1,387.43` |
| `Live` | `Short` | `99.65` | 1,500,000.00 USD | 9,360.00 USD | 0.00 USD | `+2.52%` | `93.92` |
| `Live` | `Short` | `99.75` | 1,530,000.00 USD | 33,470.00 USD | 0.00 USD | `+2.62%` | `335.55` |
| `Live` | `Short` | `99.85` | 1,530,000.00 USD | 883.67 USD | 0.00 USD | `+2.73%` | `8.85` |
| `Live` | `Short` | `99.95` | 1,530,000.00 USD | 4,010.00 USD | 0.00 USD | `+2.83%` | `40.15` |
| `Live` | `Short` | `100.05` | 1,570,000.00 USD | 36,990.00 USD | 0.00 USD | `+2.93%` | `369.67` |
| `Live` | `Short` | `100.15` | 1,600,000.00 USD | 25,710.00 USD | 0.00 USD | `+3.03%` | `256.74` |
| `Live` | `Short` | `100.25` | 1,940,000.00 USD | 347,460.00 USD | 0.00 USD | `+3.14%` | `3,465.93` |
| `Live` | `Short` | `100.35` | 2,340,000.00 USD | 391,910.00 USD | 0.00 USD | `+3.24%` | `3,905.45` |
| `Live` | `Short` | `100.45` | 2,360,000.00 USD | 26,900.00 USD | 0.00 USD | `+3.34%` | `267.76` |
| `Live` | `Short` | `100.55` | 2,360,000.00 USD | 1,510.00 USD | 0.00 USD | `+3.45%` | `15.00` |
| `Live` | `Short` | `100.65` | 2,470,000.00 USD | 101,930.00 USD | 0.00 USD | `+3.55%` | `1,012.76` |
| `Live` | `Short` | `100.75` | 2,490,000.00 USD | 19,590.00 USD | 0.00 USD | `+3.65%` | `194.44` |
| `Live` | `Short` | `100.85` | 2,550,000.00 USD | 62,360.00 USD | 0.00 USD | `+3.76%` | `618.31` |
| `Live` | `Short` | `100.95` | 2,550,000.00 USD | 498.69 USD | 0.00 USD | `+3.86%` | `4.94` |
| `Live` | `Short` | `101.05` | 2,550,000.00 USD | 698.26 USD | 0.00 USD | `+3.96%` | `6.91` |
| `Live` | `Short` | `101.15` | 2,560,000.00 USD | 12,940.00 USD | 0.00 USD | `+4.06%` | `127.95` |
| `Live` | `Short` | `101.25` | 2,560,000.00 USD | 769.50 USD | 0.00 USD | `+4.17%` | `7.60` |
| `Live` | `Short` | `101.45` | 2,560,000.00 USD | 118.70 USD | 0.00 USD | `+4.37%` | `1.17` |
| `Live` | `Short` | `101.55` | 2,570,000.00 USD | 2,790.00 USD | 0.00 USD | `+4.48%` | `27.47` |
| `Live` | `Short` | `101.65` | 2,570,000.00 USD | 3,870.00 USD | 0.00 USD | `+4.58%` | `38.10` |
| `Live` | `Short` | `101.95` | 2,570,000.00 USD | 1,760.00 USD | 0.00 USD | `+4.89%` | `17.31` |
| `Live` | `Short` | `102.05` | 2,580,000.00 USD | 4,280.00 USD | 0.00 USD | `+4.99%` | `41.98` |
| `Live` | `Short` | `102.15` | 2,580,000.00 USD | 719.14 USD | 0.00 USD | `+5.09%` | `7.04` |
| `Live` | `Short` | `102.25` | 2,580,000.00 USD | 1,170.00 USD | 0.00 USD | `+5.20%` | `11.44` |
| `Live` | `Short` | `102.55` | 2,580,000.00 USD | 6,330.00 USD | 0.00 USD | `+5.50%` | `61.77` |
| `Live` | `Short` | `102.65` | 2,590,000.00 USD | 1,500.00 USD | 0.00 USD | `+5.61%` | `14.61` |
| `Live` | `Short` | `102.75` | 2,590,000.00 USD | 3,240.00 USD | 0.00 USD | `+5.71%` | `31.50` |
| `Live` | `Short` | `102.95` | 2,590,000.00 USD | 4,150.00 USD | 0.00 USD | `+5.92%` | `40.32` |
| `Live` | `Short` | `103.05` | 2,590,000.00 USD | 692.50 USD | 0.00 USD | `+6.02%` | `6.72` |
| `Live` | `Short` | `103.15` | 2,600,000.00 USD | 11,000.00 USD | 0.00 USD | `+6.12%` | `106.62` |
| `Live` | `Short` | `103.25` | 2,610,000.00 USD | 863.17 USD | 0.00 USD | `+6.22%` | `8.36` |
| `Live` | `Short` | `103.35` | 2,610,000.00 USD | 385.50 USD | 0.00 USD | `+6.33%` | `3.73` |
| `Live` | `Short` | `103.45` | 2,610,000.00 USD | 3,300.00 USD | 0.00 USD | `+6.43%` | `31.94` |
| `Live` | `Short` | `103.65` | 2,610,000.00 USD | 4,360.00 USD | 0.00 USD | `+6.64%` | `42.09` |
| `Live` | `Short` | `103.75` | 2,870,000.00 USD | 261,050.00 USD | 0.00 USD | `+6.74%` | `2,516.13` |
| `Live` | `Short` | `103.85` | 2,890,000.00 USD | 13,560.00 USD | 0.00 USD | `+6.84%` | `130.56` |
| `Live` | `Short` | `103.95` | 2,890,000.00 USD | 827.44 USD | 0.00 USD | `+6.94%` | `7.96` |
| `Live` | `Short` | `104.05` | 2,890,000.00 USD | 775.17 USD | 0.00 USD | `+7.05%` | `7.45` |
| `Live` | `Short` | `104.15` | 2,890,000.00 USD | 4,830.00 USD | 0.00 USD | `+7.15%` | `46.35` |
| `Live` | `Short` | `104.25` | 2,940,000.00 USD | 41,100.00 USD | 0.00 USD | `+7.25%` | `394.28` |
| `Live` | `Short` | `104.35` | 2,950,000.00 USD | 11,630.00 USD | 0.00 USD | `+7.36%` | `111.45` |
| `Live` | `Short` | `104.45` | 2,960,000.00 USD | 8,550.00 USD | 0.00 USD | `+7.46%` | `81.88` |
| `Live` | `Short` | `104.55` | 2,960,000.00 USD | 575.03 USD | 0.00 USD | `+7.56%` | `5.50` |
| `Live` | `Short` | `104.65` | 2,960,000.00 USD | 401.86 USD | 0.00 USD | `+7.66%` | `3.84` |
| `Live` | `Short` | `104.75` | 2,960,000.00 USD | 3,620.00 USD | 0.00 USD | `+7.77%` | `34.59` |
| `Live` | `Short` | `104.95` | 3,090,000.00 USD | 126,400.00 USD | 0.00 USD | `+7.97%` | `1,204.39` |
| `Live` | `Short` | `105.05` | 3,090,000.00 USD | 578.83 USD | 0.00 USD | `+8.08%` | `5.51` |
| `Live` | `Short` | `105.15` | 3,110,000.00 USD | 19,740.00 USD | 0.00 USD | `+8.18%` | `187.73` |
| `Live` | `Short` | `105.25` | 3,110,000.00 USD | 2,110.00 USD | 0.00 USD | `+8.28%` | `20.07` |
| `Live` | `Short` | `105.35` | 3,120,000.00 USD | 6,840.00 USD | 0.00 USD | `+8.38%` | `64.89` |
| `Live` | `Short` | `105.45` | 3,650,000.00 USD | 531,450.00 USD | 0.00 USD | `+8.49%` | `5,039.81` |
| `Live` | `Short` | `105.55` | 3,650,000.00 USD | 4,180.00 USD | 0.00 USD | `+8.59%` | `39.61` |
| `Live` | `Short` | `105.65` | 3,660,000.00 USD | 3,540.00 USD | 0.00 USD | `+8.69%` | `33.54` |
| `Live` | `Short` | `105.85` | 3,750,000.00 USD | 91,370.00 USD | 0.00 USD | `+8.90%` | `863.23` |
| `Live` | `Short` | `105.95` | 3,750,000.00 USD | 840.18 USD | 0.00 USD | `+9.00%` | `7.93` |
| `Live` | `Short` | `106.05` | 3,780,000.00 USD | 33,380.00 USD | 0.00 USD | `+9.10%` | `314.77` |
| `Live` | `Short` | `106.15` | 3,790,000.00 USD | 5,820.00 USD | 0.00 USD | `+9.21%` | `54.81` |
| `Live` | `Short` | `106.35` | 4,040,000.00 USD | 252,430.00 USD | 0.00 USD | `+9.41%` | `2,373.61` |
| `Live` | `Short` | `106.45` | 4,070,000.00 USD | 33,200.00 USD | 0.00 USD | `+9.52%` | `311.90` |
| `Live` | `Short` | `106.55` | 4,070,000.00 USD | 218.43 USD | 0.00 USD | `+9.62%` | `2.05` |
| `Live` | `Short` | `106.65` | 4,080,000.00 USD | 6,460.00 USD | 0.00 USD | `+9.72%` | `60.58` |
| `Live` | `Short` | `106.85` | 4,560,000.00 USD | 479,570.00 USD | 0.00 USD | `+9.93%` | `4,488.25` |
| `Live` | `Short` | `106.95` | 4,560,000.00 USD | 131.55 USD | 0.00 USD | `+10.03%` | `1.23` |
| `Live` | `Short` | `107.05` | 4,570,000.00 USD | 14,820.00 USD | 0.00 USD | `+10.13%` | `138.41` |
| `Live` | `Short` | `107.15` | 4,580,000.00 USD | 3,060.00 USD | 0.00 USD | `+10.24%` | `28.58` |
| `Live` | `Short` | `107.25` | 4,620,000.00 USD | 46,610.00 USD | 0.00 USD | `+10.34%` | `434.60` |
| `Live` | `Short` | `107.35` | 4,620,000.00 USD | 766.48 USD | 0.00 USD | `+10.44%` | `7.14` |
| `Live` | `Short` | `107.45` | 4,660,000.00 USD | 32,580.00 USD | 0.00 USD | `+10.55%` | `303.18` |
| `Live` | `Short` | `107.55` | 4,660,000.00 USD | 221.55 USD | 0.00 USD | `+10.65%` | `2.06` |
| `Live` | `Short` | `107.75` | 4,810,000.00 USD | 150,290.00 USD | 0.00 USD | `+10.85%` | `1,394.81` |
| `Live` | `Short` | `107.85` | 4,950,000.00 USD | 143,860.00 USD | 0.00 USD | `+10.96%` | `1,333.92` |
| `Live` | `Short` | `108.05` | 4,950,000.00 USD | 1,080.00 USD | 0.00 USD | `+11.16%` | `10.04` |
| `Live` | `Short` | `108.15` | 4,950,000.00 USD | 1,150.00 USD | 0.00 USD | `+11.27%` | `10.66` |
| `Live` | `Short` | `108.25` | 5,110,000.00 USD | 161,430.00 USD | 0.00 USD | `+11.37%` | `1,491.26` |
| `Live` | `Short` | `108.35` | 5,120,000.00 USD | 3,470.00 USD | 0.00 USD | `+11.47%` | `32.00` |
| `Live` | `Short` | `108.45` | 5,230,000.00 USD | 108,080.00 USD | 0.00 USD | `+11.57%` | `996.61` |
| `Live` | `Short` | `108.55` | 5,230,000.00 USD | 261.61 USD | 0.00 USD | `+11.68%` | `2.41` |
| `Live` | `Short` | `108.65` | 5,230,000.00 USD | 7,980.00 USD | 0.00 USD | `+11.78%` | `73.48` |
| `Live` | `Short` | `108.85` | 5,280,000.00 USD | 41,550.00 USD | 0.00 USD | `+11.99%` | `381.74` |
| `Live` | `Short` | `108.95` | 5,280,000.00 USD | 3,170.00 USD | 0.00 USD | `+12.09%` | `29.10` |
| `Live` | `Short` | `109.05` | 5,280,000.00 USD | 163.58 USD | 0.00 USD | `+12.19%` | `1.50` |
| `Live` | `Short` | `109.15` | 5,300,000.00 USD | 17,440.00 USD | 0.00 USD | `+12.29%` | `159.75` |
| `Live` | `Short` | `109.25` | 5,300,000.00 USD | 2,720.00 USD | 0.00 USD | `+12.40%` | `24.90` |
| `Live` | `Short` | `109.35` | 5,300,000.00 USD | 247.13 USD | 0.00 USD | `+12.50%` | `2.26` |
| `Live` | `Short` | `109.45` | 5,300,000.00 USD | 620.58 USD | 0.00 USD | `+12.60%` | `5.67` |
| `Live` | `Short` | `109.55` | 5,300,000.00 USD | 356.04 USD | 0.00 USD | `+12.71%` | `3.25` |
| `Live` | `Short` | `109.65` | 5,750,000.00 USD | 447,000.00 USD | 0.00 USD | `+12.81%` | `4,076.57` |
| `Live` | `Short` | `109.75` | 5,750,000.00 USD | 111.95 USD | 0.00 USD | `+12.91%` | `1.02` |
| `Live` | `Short` | `109.85` | 5,750,000.00 USD | 459.17 USD | 0.00 USD | `+13.01%` | `4.18` |
| `Live` | `Short` | `109.95` | 5,750,000.00 USD | 4,480.00 USD | 0.00 USD | `+13.12%` | `40.77` |
| `Live` | `Short` | `110.05` | 5,770,000.00 USD | 14,790.00 USD | 0.00 USD | `+13.22%` | `134.36` |
| `Live` | `Short` | `110.15` | 5,770,000.00 USD | 194.97 USD | 0.00 USD | `+13.32%` | `1.77` |
| `Live` | `Short` | `110.25` | 5,770,000.00 USD | 226.01 USD | 0.00 USD | `+13.43%` | `2.05` |
| `Live` | `Short` | `110.35` | 5,770,000.00 USD | 385.12 USD | 0.00 USD | `+13.53%` | `3.49` |
| `Live` | `Short` | `110.45` | 5,910,000.00 USD | 143,580.00 USD | 0.00 USD | `+13.63%` | `1,299.91` |
| `Live` | `Short` | `110.55` | 5,910,000.00 USD | 1,820.00 USD | 0.00 USD | `+13.73%` | `16.50` |
| `Live` | `Short` | `110.85` | 5,920,000.00 USD | 1,090.00 USD | 0.00 USD | `+14.04%` | `9.87` |
| `Live` | `Short` | `110.95` | 5,920,000.00 USD | 4,450.00 USD | 0.00 USD | `+14.15%` | `40.12` |
| `Live` | `Short` | `111.15` | 5,950,000.00 USD | 29,660.00 USD | 0.00 USD | `+14.35%` | `266.81` |
| `Live` | `Short` | `111.35` | 5,950,000.00 USD | 390.84 USD | 0.00 USD | `+14.56%` | `3.51` |
| `Live` | `Short` | `111.45` | 5,950,000.00 USD | 841.45 USD | 0.00 USD | `+14.66%` | `7.55` |
| `Live` | `Short` | `111.55` | 5,950,000.00 USD | 892.40 USD | 0.00 USD | `+14.76%` | `8.00` |
| `Live` | `Short` | `111.65` | 5,950,000.00 USD | 199.85 USD | 0.00 USD | `+14.87%` | `1.79` |
| `Live` | `Short` | `111.75` | 5,950,000.00 USD | 169.86 USD | 0.00 USD | `+14.97%` | `1.52` |
| `Live` | `Short` | `111.85` | 5,970,000.00 USD | 15,880.00 USD | 0.00 USD | `+15.07%` | `141.95` |
| `Live` | `Short` | `111.95` | 5,970,000.00 USD | 223.90 USD | 0.00 USD | `+15.17%` | `2.00` |
| `Live` | `Short` | `112.15` | 5,970,000.00 USD | 528.23 USD | 0.00 USD | `+15.38%` | `4.71` |
| `Live` | `Short` | `112.25` | 6,230,000.00 USD | 261,320.00 USD | 0.00 USD | `+15.48%` | `2,328.02` |
| `Live` | `Short` | `112.35` | 6,230,000.00 USD | 1,910.00 USD | 0.00 USD | `+15.59%` | `17.00` |
| `Live` | `Short` | `112.45` | 6,240,000.00 USD | 5,670.00 USD | 0.00 USD | `+15.69%` | `50.42` |
| `Live` | `Short` | `112.55` | 6,240,000.00 USD | 1,070.00 USD | 0.00 USD | `+15.79%` | `9.55` |
| `Live` | `Short` | `112.65` | 6,240,000.00 USD | 707.44 USD | 0.00 USD | `+15.90%` | `6.28` |
| `Live` | `Short` | `112.75` | 6,360,000.00 USD | 118,640.00 USD | 0.00 USD | `+16.00%` | `1,052.24` |
| `Live` | `Short` | `112.85` | 6,470,000.00 USD | 108,760.00 USD | 0.00 USD | `+16.10%` | `963.76` |
| `Live` | `Short` | `113.05` | 6,470,000.00 USD | 406.98 USD | 0.00 USD | `+16.31%` | `3.60` |
| `Live` | `Short` | `113.15` | 6,480,000.00 USD | 9,560.00 USD | 0.00 USD | `+16.41%` | `84.51` |
| `Live` | `Short` | `113.25` | 6,480,000.00 USD | 698.75 USD | 0.00 USD | `+16.51%` | `6.17` |
| `Live` | `Short` | `113.35` | 6,480,000.00 USD | 4,120.00 USD | 0.00 USD | `+16.62%` | `36.36` |
| `Live` | `Short` | `113.45` | 6,490,000.00 USD | 5,120.00 USD | 0.00 USD | `+16.72%` | `45.09` |
| `Live` | `Short` | `113.65` | 6,590,000.00 USD | 105,650.00 USD | 0.00 USD | `+16.92%` | `929.65` |
| `Live` | `Short` | `113.75` | 6,600,000.00 USD | 5,200.00 USD | 0.00 USD | `+17.03%` | `45.74` |
| `Live` | `Short` | `113.85` | 6,600,000.00 USD | 461.09 USD | 0.00 USD | `+17.13%` | `4.05` |
| `Live` | `Short` | `113.95` | 6,620,000.00 USD | 21,840.00 USD | 0.00 USD | `+17.23%` | `191.69` |
| `Live` | `Short` | `114.05` | 6,650,000.00 USD | 31,740.00 USD | 0.00 USD | `+17.34%` | `278.26` |
| `Live` | `Short` | `114.25` | 6,660,000.00 USD | 6,230.00 USD | 0.00 USD | `+17.54%` | `54.51` |
| `Live` | `Short` | `114.45` | 6,660,000.00 USD | 3,830.00 USD | 0.00 USD | `+17.75%` | `33.46` |
| `Live` | `Short` | `114.65` | 6,660,000.00 USD | 3,430.00 USD | 0.00 USD | `+17.95%` | `29.93` |
| `Live` | `Short` | `114.95` | 6,670,000.00 USD | 1,260.00 USD | 0.00 USD | `+18.26%` | `10.94` |
| `Live` | `Short` | `115.05` | 7,240,000.00 USD | 569,550.00 USD | 0.00 USD | `+18.36%` | `4,950.49` |
| `Live` | `Short` | `115.15` | 7,240,000.00 USD | 1,100.00 USD | 0.00 USD | `+18.47%` | `9.52` |
| `Live` | `Short` | `115.35` | 7,240,000.00 USD | 161.49 USD | 0.00 USD | `+18.67%` | `1.40` |
| `Live` | `Short` | `115.45` | 8,120,000.00 USD | 879,040.00 USD | 0.00 USD | `+18.78%` | `7,614.00` |
| `Live` | `Short` | `115.55` | 8,280,000.00 USD | 167,330.00 USD | 0.00 USD | `+18.88%` | `1,448.12` |
| `Live` | `Short` | `115.65` | 8,300,000.00 USD | 14,750.00 USD | 0.00 USD | `+18.98%` | `127.54` |
| `Live` | `Short` | `115.75` | 8,300,000.00 USD | 6,060.00 USD | 0.00 USD | `+19.08%` | `52.35` |
| `Live` | `Short` | `115.85` | 8,300,000.00 USD | 512.06 USD | 0.00 USD | `+19.19%` | `4.42` |
| `Live` | `Short` | `116.05` | 8,310,000.00 USD | 4,450.00 USD | 0.00 USD | `+19.39%` | `38.34` |
| `Live` | `Short` | `116.25` | 8,310,000.00 USD | 180.19 USD | 0.00 USD | `+19.60%` | `1.55` |
| `Live` | `Short` | `116.35` | 8,310,000.00 USD | 4,960.00 USD | 0.00 USD | `+19.70%` | `42.60` |
| `Live` | `Short` | `116.55` | 8,320,000.00 USD | 2,040.00 USD | 0.00 USD | `+19.91%` | `17.52` |
| `Live` | `Short` | `116.65` | 8,320,000.00 USD | 113.15 USD | 0.00 USD | `+20.01%` | `0.97` |
| `Live` | `Short` | `116.75` | 8,320,000.00 USD | 6,020.00 USD | 0.00 USD | `+20.11%` | `51.58` |
| `Live` | `Short` | `116.85` | 8,330,000.00 USD | 10,520.00 USD | 0.00 USD | `+20.22%` | `90.00` |
| `Live` | `Short` | `117.05` | 8,330,000.00 USD | 156.85 USD | 0.00 USD | `+20.42%` | `1.34` |
| `Live` | `Short` | `117.15` | 8,420,000.00 USD | 89,950.00 USD | 0.00 USD | `+20.52%` | `767.80` |
| `Live` | `Short` | `117.35` | 8,430,000.00 USD | 11,610.00 USD | 0.00 USD | `+20.73%` | `98.95` |
| `Live` | `Short` | `117.55` | 13,220,000.00 USD | 4,790,000.00 USD | 0.00 USD | `+20.94%` | `40,718.41` |
| `Live` | `Short` | `117.75` | 13,230,000.00 USD | 10,360.00 USD | 0.00 USD | `+21.14%` | `87.98` |
| `Live` | `Short` | `117.95` | 13,230,000.00 USD | 2,310.00 USD | 0.00 USD | `+21.35%` | `19.61` |
| `Live` | `Short` | `118.25` | 13,230,000.00 USD | 614.90 USD | 0.00 USD | `+21.66%` | `5.20` |
| `Live` | `Short` | `118.45` | 17,740,000.00 USD | 4,510,000.00 USD | 0.00 USD | `+21.86%` | `38,050.04` |
| `Live` | `Short` | `118.55` | 17,750,000.00 USD | 7,700.00 USD | 0.00 USD | `+21.97%` | `64.98` |
| `Live` | `Short` | `118.75` | 17,750,000.00 USD | 309.94 USD | 0.00 USD | `+22.17%` | `2.61` |
| `Live` | `Short` | `119.25` | 17,750,000.00 USD | 240.88 USD | 0.00 USD | `+22.69%` | `2.02` |
| `Live` | `Short` | `119.35` | 17,810,000.00 USD | 57,850.00 USD | 0.00 USD | `+22.79%` | `484.72` |
| `Live` | `Short` | `119.45` | 17,810,000.00 USD | 1,560.00 USD | 0.00 USD | `+22.89%` | `13.05` |
| `Live` | `Short` | `119.55` | 17,820,000.00 USD | 8,970.00 USD | 0.00 USD | `+22.99%` | `75.00` |
| `Live` | `Short` | `119.65` | 17,820,000.00 USD | 470.22 USD | 0.00 USD | `+23.10%` | `3.93` |
| `Live` | `Short` | `119.75` | 17,850,000.00 USD | 28,230.00 USD | 0.00 USD | `+23.20%` | `235.73` |
| `Live` | `Short` | `119.85` | 17,850,000.00 USD | 485.39 USD | 0.00 USD | `+23.30%` | `4.05` |
| `Live` | `Short` | `120.15` | 17,990,000.00 USD | 140,720.00 USD | 0.00 USD | `+23.61%` | `1,171.24` |
| `Live` | `Short` | `120.25` | 17,990,000.00 USD | 453.34 USD | 0.00 USD | `+23.71%` | `3.77` |
| `Live` | `Short` | `120.45` | 17,990,000.00 USD | 145.74 USD | 0.00 USD | `+23.92%` | `1.21` |
| `Live` | `Short` | `120.55` | 17,990,000.00 USD | 1,190.00 USD | 0.00 USD | `+24.02%` | `9.86` |
| `Live` | `Short` | `120.75` | 17,990,000.00 USD | 515.60 USD | 0.00 USD | `+24.23%` | `4.27` |
| `Live` | `Short` | `120.95` | 18,000,000.00 USD | 13,290.00 USD | 0.00 USD | `+24.43%` | `109.91` |
| `Live` | `Short` | `121.05` | 18,060,000.00 USD | 60,530.00 USD | 0.00 USD | `+24.54%` | `500.00` |
| `Live` | `Short` | `121.15` | 18,070,000.00 USD | 2,100.00 USD | 0.00 USD | `+24.64%` | `17.33` |
| `Live` | `Short` | `121.35` | 18,560,000.00 USD | 489,130.00 USD | 0.00 USD | `+24.85%` | `4,030.75` |
| `Live` | `Short` | `121.55` | 18,560,000.00 USD | 5,940.00 USD | 0.00 USD | `+25.05%` | `48.87` |
| `Live` | `Short` | `121.75` | 18,560,000.00 USD | 105.92 USD | 0.00 USD | `+25.26%` | `0.87` |
| `Live` | `Short` | `122.05` | 18,620,000.00 USD | 56,150.00 USD | 0.00 USD | `+25.57%` | `460.06` |
| `Live` | `Short` | `122.15` | 18,620,000.00 USD | 169.79 USD | 0.00 USD | `+25.67%` | `1.39` |
| `Live` | `Short` | `122.25` | 18,620,000.00 USD | 2,330.00 USD | 0.00 USD | `+25.77%` | `19.10` |
| `Live` | `Short` | `122.35` | 19,500,000.00 USD | 881,450.00 USD | 0.00 USD | `+25.87%` | `7,204.35` |
| `Live` | `Short` | `122.45` | 19,520,000.00 USD | 17,500.00 USD | 0.00 USD | `+25.98%` | `142.95` |
| `Live` | `Short` | `122.65` | 19,520,000.00 USD | 116.52 USD | 0.00 USD | `+26.18%` | `0.95` |
| `Live` | `Short` | `122.95` | 19,520,000.00 USD | 4,300.00 USD | 0.00 USD | `+26.49%` | `35.00` |
| `Live` | `Short` | `123.25` | 19,990,000.00 USD | 471,560.00 USD | 0.00 USD | `+26.80%` | `3,826.05` |
| `Live` | `Short` | `123.35` | 20,000,000.00 USD | 2,330.00 USD | 0.00 USD | `+26.90%` | `18.92` |
| `Live` | `Short` | `123.45` | 20,000,000.00 USD | 1,960.00 USD | 0.00 USD | `+27.01%` | `15.87` |
| `Live` | `Short` | `123.65` | 20,120,000.00 USD | 124,510.00 USD | 0.00 USD | `+27.21%` | `1,006.96` |
| `Live` | `Short` | `124.05` | 20,130,000.00 USD | 7,950.00 USD | 0.00 USD | `+27.62%` | `64.10` |
| `Live` | `Short` | `124.15` | 20,130,000.00 USD | 121.67 USD | 0.00 USD | `+27.73%` | `0.98` |
| `Live` | `Short` | `124.25` | 20,150,000.00 USD | 23,360.00 USD | 0.00 USD | `+27.83%` | `188.01` |
| `Live` | `Short` | `124.35` | 20,180,000.00 USD | 29,710.00 USD | 0.00 USD | `+27.93%` | `238.96` |
| `Live` | `Short` | `124.55` | 20,190,000.00 USD | 3,080.00 USD | 0.00 USD | `+28.14%` | `24.76` |
| `Live` | `Short` | `124.65` | 20,190,000.00 USD | 675.60 USD | 0.00 USD | `+28.24%` | `5.42` |
| `Live` | `Short` | `124.75` | 20,190,000.00 USD | 5,330.00 USD | 0.00 USD | `+28.34%` | `42.73` |
| `Live` | `Short` | `124.95` | 20,200,000.00 USD | 2,800.00 USD | 0.00 USD | `+28.55%` | `22.41` |
| `Live` | `Short` | `125.05` | 20,200,000.00 USD | 208.83 USD | 0.00 USD | `+28.65%` | `1.67` |
| `Live` | `Short` | `125.25` | 20,200,000.00 USD | 690.13 USD | 0.00 USD | `+28.86%` | `5.51` |
| `Live` | `Short` | `125.35` | 20,200,000.00 USD | 5,320.00 USD | 0.00 USD | `+28.96%` | `42.44` |
| `Live` | `Short` | `125.45` | 20,200,000.00 USD | 590.87 USD | 0.00 USD | `+29.06%` | `4.71` |
| `Live` | `Short` | `125.55` | 20,250,000.00 USD | 51,130.00 USD | 0.00 USD | `+29.17%` | `407.21` |
| `Live` | `Short` | `125.65` | 20,260,000.00 USD | 1,560.00 USD | 0.00 USD | `+29.27%` | `12.41` |
| `Live` | `Short` | `125.75` | 20,260,000.00 USD | 1,930.00 USD | 0.00 USD | `+29.37%` | `15.31` |
| `Live` | `Short` | `125.85` | 25,690,000.00 USD | 5,430,000.00 USD | 0.00 USD | `+29.48%` | `43,151.65` |
| `Live` | `Short` | `125.95` | 25,690,000.00 USD | 110.84 USD | 0.00 USD | `+29.58%` | `0.88` |
| `Live` | `Short` | `126.05` | 25,690,000.00 USD | 810.50 USD | 0.00 USD | `+29.68%` | `6.43` |
| `Live` | `Short` | `126.15` | 25,690,000.00 USD | 470.54 USD | 0.00 USD | `+29.78%` | `3.73` |
| `Live` | `Short` | `126.35` | 25,690,000.00 USD | 4,090.00 USD | 0.00 USD | `+29.99%` | `32.36` |
| `Live` | `Short` | `126.45` | 25,700,000.00 USD | 5,150.00 USD | 0.00 USD | `+30.09%` | `40.70` |
| `Live` | `Short` | `126.55` | 25,700,000.00 USD | 403.69 USD | 0.00 USD | `+30.20%` | `3.19` |
| `Live` | `Short` | `126.65` | 25,730,000.00 USD | 30,830.00 USD | 0.00 USD | `+30.30%` | `243.46` |
| `Live` | `Short` | `126.85` | 25,730,000.00 USD | 3,870.00 USD | 0.00 USD | `+30.50%` | `30.49` |
| `Live` | `Short` | `127.05` | 25,740,000.00 USD | 2,030.00 USD | 0.00 USD | `+30.71%` | `16.01` |
| `Live` | `Short` | `127.15` | 25,740,000.00 USD | 389.08 USD | 0.00 USD | `+30.81%` | `3.06` |
| `Live` | `Short` | `127.35` | 25,770,000.00 USD | 28,940.00 USD | 0.00 USD | `+31.02%` | `227.26` |
| `Live` | `Short` | `127.45` | 25,770,000.00 USD | 138.92 USD | 0.00 USD | `+31.12%` | `1.09` |
| `Live` | `Short` | `127.65` | 25,770,000.00 USD | 4,840.00 USD | 0.00 USD | `+31.33%` | `37.89` |
| `Live` | `Short` | `127.75` | 25,790,000.00 USD | 20,800.00 USD | 0.00 USD | `+31.43%` | `162.83` |
| `Live` | `Short` | `127.85` | 25,790,000.00 USD | 388.66 USD | 0.00 USD | `+31.53%` | `3.04` |
| `Live` | `Short` | `127.95` | 25,800,000.00 USD | 10,510.00 USD | 0.00 USD | `+31.64%` | `82.13` |
| `Live` | `Short` | `128.05` | 25,920,000.00 USD | 116,190.00 USD | 0.00 USD | `+31.74%` | `907.38` |
| `Live` | `Short` | `128.15` | 25,920,000.00 USD | 221.70 USD | 0.00 USD | `+31.84%` | `1.73` |
| `Live` | `Short` | `128.25` | 25,920,000.00 USD | 782.32 USD | 0.00 USD | `+31.94%` | `6.10` |
| `Live` | `Short` | `128.35` | 25,920,000.00 USD | 195.09 USD | 0.00 USD | `+32.05%` | `1.52` |
| `Live` | `Short` | `128.65` | 25,920,000.00 USD | 788.62 USD | 0.00 USD | `+32.36%` | `6.13` |
| `Live` | `Short` | `128.75` | 25,940,000.00 USD | 18,730.00 USD | 0.00 USD | `+32.46%` | `145.45` |
| `Live` | `Short` | `128.85` | 25,970,000.00 USD | 32,440.00 USD | 0.00 USD | `+32.56%` | `251.77` |
| `Live` | `Short` | `129.15` | 26,290,000.00 USD | 313,870.00 USD | 0.00 USD | `+32.87%` | `2,430.25` |
| `Live` | `Short` | `129.25` | 26,320,000.00 USD | 32,310.00 USD | 0.00 USD | `+32.97%` | `250.00` |
| `Live` | `Short` | `129.35` | 26,350,000.00 USD | 35,060.00 USD | 0.00 USD | `+33.08%` | `271.06` |
| `Live` | `Short` | `129.45` | 26,350,000.00 USD | 730.10 USD | 0.00 USD | `+33.18%` | `5.64` |
| `Live` | `Short` | `129.55` | 27,050,000.00 USD | 701,210.00 USD | 0.00 USD | `+33.28%` | `5,412.69` |
| `Live` | `Short` | `129.75` | 27,060,000.00 USD | 2,210.00 USD | 0.00 USD | `+33.49%` | `17.05` |
| `Live` | `Short` | `129.85` | 27,060,000.00 USD | 490.83 USD | 0.00 USD | `+33.59%` | `3.78` |
| `Live` | `Short` | `130.25` | 27,060,000.00 USD | 131.55 USD | 0.00 USD | `+34.00%` | `1.01` |
| `Live` | `Short` | `130.35` | 27,070,000.00 USD | 13,360.00 USD | 0.00 USD | `+34.10%` | `102.50` |
| `Live` | `Short` | `130.55` | 27,140,000.00 USD | 69,270.00 USD | 0.00 USD | `+34.31%` | `530.61` |
| `Live` | `Short` | `130.85` | 27,140,000.00 USD | 3,180.00 USD | 0.00 USD | `+34.62%` | `24.34` |
| `Live` | `Short` | `130.95` | 27,150,000.00 USD | 2,070.00 USD | 0.00 USD | `+34.72%` | `15.84` |
| `Live` | `Short` | `131.05` | 27,150,000.00 USD | 188.71 USD | 0.00 USD | `+34.83%` | `1.44` |
| `Live` | `Short` | `131.25` | 27,150,000.00 USD | 1,560.00 USD | 0.00 USD | `+35.03%` | `11.87` |
| `Live` | `Short` | `131.35` | 27,150,000.00 USD | 855.09 USD | 0.00 USD | `+35.13%` | `6.51` |
| `Live` | `Short` | `131.45` | 27,150,000.00 USD | 219.52 USD | 0.00 USD | `+35.24%` | `1.67` |
| `Live` | `Short` | `131.85` | 27,150,000.00 USD | 3,100.00 USD | 0.00 USD | `+35.65%` | `23.54` |
| `Live` | `Short` | `131.95` | 27,150,000.00 USD | 106.88 USD | 0.00 USD | `+35.75%` | `0.81` |
| `Live` | `Short` | `132.05` | 27,170,000.00 USD | 13,650.00 USD | 0.00 USD | `+35.85%` | `103.36` |
| `Live` | `Short` | `132.15` | 27,170,000.00 USD | 3,930.00 USD | 0.00 USD | `+35.96%` | `29.75` |
| `Live` | `Short` | `132.55` | 27,180,000.00 USD | 8,730.00 USD | 0.00 USD | `+36.37%` | `65.85` |
| `Live` | `Short` | `132.65` | 27,210,000.00 USD | 30,100.00 USD | 0.00 USD | `+36.47%` | `226.89` |
| `Live` | `Short` | `132.75` | 27,210,000.00 USD | 136.73 USD | 0.00 USD | `+36.57%` | `1.03` |
| `Live` | `Short` | `132.85` | 27,260,000.00 USD | 49,280.00 USD | 0.00 USD | `+36.68%` | `370.98` |
| `Live` | `Short` | `133.05` | 27,260,000.00 USD | 103.78 USD | 0.00 USD | `+36.88%` | `0.78` |
| `Live` | `Short` | `133.15` | 27,270,000.00 USD | 8,440.00 USD | 0.00 USD | `+36.99%` | `63.42` |
| `Live` | `Short` | `133.25` | 27,270,000.00 USD | 1,330.00 USD | 0.00 USD | `+37.09%` | `9.95` |
| `Live` | `Short` | `133.45` | 27,270,000.00 USD | 1,600.00 USD | 0.00 USD | `+37.29%` | `11.97` |
| `Live` | `Short` | `133.65` | 27,270,000.00 USD | 156.37 USD | 0.00 USD | `+37.50%` | `1.17` |
| `Live` | `Short` | `133.75` | 27,420,000.00 USD | 151,200.00 USD | 0.00 USD | `+37.60%` | `1,130.50` |
| `Live` | `Short` | `133.95` | 27,420,000.00 USD | 503.65 USD | 0.00 USD | `+37.81%` | `3.76` |
| `Live` | `Short` | `134.05` | 27,430,000.00 USD | 12,620.00 USD | 0.00 USD | `+37.91%` | `94.18` |
| `Live` | `Short` | `134.25` | 27,450,000.00 USD | 11,980.00 USD | 0.00 USD | `+38.12%` | `89.25` |
| `Live` | `Short` | `134.65` | 27,460,000.00 USD | 18,040.00 USD | 0.00 USD | `+38.53%` | `134.01` |
| `Live` | `Short` | `135.25` | 27,480,000.00 USD | 14,540.00 USD | 0.00 USD | `+39.15%` | `107.50` |
| `Live` | `Short` | `135.65` | 27,480,000.00 USD | 6,420.00 USD | 0.00 USD | `+39.56%` | `47.30` |
| `Live` | `Short` | `135.75` | 27,480,000.00 USD | 415.39 USD | 0.00 USD | `+39.66%` | `3.06` |
| `Live` | `Short` | `135.85` | 27,490,000.00 USD | 3,250.00 USD | 0.00 USD | `+39.76%` | `23.94` |
| `Live` | `Short` | `135.95` | 27,490,000.00 USD | 504.37 USD | 0.00 USD | `+39.87%` | `3.71` |
| `Live` | `Short` | `136.35` | 27,540,000.00 USD | 49,040.00 USD | 0.00 USD | `+40.28%` | `359.64` |
| `Live` | `Short` | `136.45` | 27,550,000.00 USD | 8,630.00 USD | 0.00 USD | `+40.38%` | `63.22` |
| `Live` | `Short` | `136.55` | 27,550,000.00 USD | 136.55 USD | 0.00 USD | `+40.48%` | `1.00` |
| `Live` | `Short` | `136.65` | 27,550,000.00 USD | 1,110.00 USD | 0.00 USD | `+40.59%` | `8.14` |
| `Live` | `Short` | `136.95` | 27,580,000.00 USD | 34,240.00 USD | 0.00 USD | `+40.90%` | `250.00` |
| `Live` | `Short` | `137.05` | 27,580,000.00 USD | 836.00 USD | 0.00 USD | `+41.00%` | `6.10` |
| `Live` | `Short` | `137.15` | 27,580,000.00 USD | 809.19 USD | 0.00 USD | `+41.10%` | `5.90` |
| `Live` | `Short` | `137.25` | 27,650,000.00 USD | 68,620.00 USD | 0.00 USD | `+41.20%` | `500.00` |
| `Live` | `Short` | `138.05` | 27,650,000.00 USD | 1,270.00 USD | 0.00 USD | `+42.03%` | `9.20` |
| `Live` | `Short` | `138.15` | 27,700,000.00 USD | 50,150.00 USD | 0.00 USD | `+42.13%` | `363.00` |
| `Live` | `Short` | `138.25` | 27,750,000.00 USD | 48,050.00 USD | 0.00 USD | `+42.23%` | `347.53` |
| `Live` | `Short` | `138.35` | 27,750,000.00 USD | 2,060.00 USD | 0.00 USD | `+42.34%` | `14.87` |
| `Live` | `Short` | `138.45` | 27,760,000.00 USD | 7,310.00 USD | 0.00 USD | `+42.44%` | `52.83` |
| `Live` | `Short` | `138.75` | 27,760,000.00 USD | 2,360.00 USD | 0.00 USD | `+42.75%` | `17.04` |
| `Live` | `Short` | `139.15` | 27,770,000.00 USD | 4,720.00 USD | 0.00 USD | `+43.16%` | `33.90` |
| `Live` | `Short` | `139.35` | 27,770,000.00 USD | 4,430.00 USD | 0.00 USD | `+43.36%` | `31.82` |
| `Live` | `Short` | `139.45` | 27,780,000.00 USD | 12,680.00 USD | 0.00 USD | `+43.47%` | `90.91` |
| `Live` | `Short` | `139.55` | 27,790,000.00 USD | 494.01 USD | 0.00 USD | `+43.57%` | `3.54` |
| `Live` | `Short` | `139.75` | 27,790,000.00 USD | 4,870.00 USD | 0.00 USD | `+43.78%` | `34.82` |
| `Live` | `Short` | `139.95` | 27,790,000.00 USD | 2,080.00 USD | 0.00 USD | `+43.98%` | `14.84` |
| `Live` | `Short` | `140.05` | 27,790,000.00 USD | 116.24 USD | 0.00 USD | `+44.08%` | `0.83` |
| `Live` | `Short` | `140.35` | 27,790,000.00 USD | 1,600.00 USD | 0.00 USD | `+44.39%` | `11.39` |
| `Live` | `Short` | `140.45` | 27,800,000.00 USD | 4,870.00 USD | 0.00 USD | `+44.50%` | `34.66` |
| `Live` | `Short` | `140.55` | 27,800,000.00 USD | 702.75 USD | 0.00 USD | `+44.60%` | `5.00` |
| `Live` | `Short` | `140.65` | 27,810,000.00 USD | 7,340.00 USD | 0.00 USD | `+44.70%` | `52.16` |
| `Live` | `Short` | `140.95` | 27,810,000.00 USD | 1,940.00 USD | 0.00 USD | `+45.01%` | `13.73` |
| `Live` | `Short` | `141.05` | 27,880,000.00 USD | 70,450.00 USD | 0.00 USD | `+45.11%` | `499.50` |
| `Live` | `Short` | `141.15` | 32,980,000.00 USD | 5,100,000.00 USD | 0.00 USD | `+45.22%` | `36,104.04` |
| `Live` | `Short` | `141.35` | 32,980,000.00 USD | 210.61 USD | 0.00 USD | `+45.42%` | `1.49` |
| `Live` | `Short` | `141.45` | 33,270,000.00 USD | 289,400.00 USD | 0.00 USD | `+45.52%` | `2,045.98` |
| `Live` | `Short` | `141.55` | 33,270,000.00 USD | 236.39 USD | 0.00 USD | `+45.63%` | `1.67` |
| `Live` | `Short` | `141.75` | 35,220,000.00 USD | 1,950,000.00 USD | 0.00 USD | `+45.83%` | `13,760.46` |
| `Live` | `Short` | `141.95` | 35,220,000.00 USD | 2,640.00 USD | 0.00 USD | `+46.04%` | `18.59` |
| `Live` | `Short` | `142.15` | 35,240,000.00 USD | 23,060.00 USD | 0.00 USD | `+46.24%` | `162.19` |
| `Live` | `Short` | `142.25` | 35,250,000.00 USD | 3,470.00 USD | 0.00 USD | `+46.35%` | `24.41` |
| `Live` | `Short` | `142.45` | 35,250,000.00 USD | 151.00 USD | 0.00 USD | `+46.55%` | `1.06` |
| `Live` | `Short` | `142.75` | 35,250,000.00 USD | 1,150.00 USD | 0.00 USD | `+46.86%` | `8.09` |
| `Live` | `Short` | `142.95` | 35,250,000.00 USD | 283.04 USD | 0.00 USD | `+47.07%` | `1.98` |
| `Live` | `Short` | `143.15` | 35,320,000.00 USD | 73,040.00 USD | 0.00 USD | `+47.27%` | `510.22` |
| `Live` | `Short` | `143.35` | 35,430,000.00 USD | 110,660.00 USD | 0.00 USD | `+47.48%` | `771.94` |
| `Live` | `Short` | `143.55` | 35,430,000.00 USD | 103.36 USD | 0.00 USD | `+47.69%` | `0.72` |
| `Live` | `Short` | `143.65` | 35,430,000.00 USD | 2,840.00 USD | 0.00 USD | `+47.79%` | `19.75` |
| `Live` | `Short` | `144.05` | 35,440,000.00 USD | 3,750.00 USD | 0.00 USD | `+48.20%` | `26.00` |
| `Live` | `Short` | `144.65` | 35,440,000.00 USD | 1,240.00 USD | 0.00 USD | `+48.82%` | `8.60` |
| `Live` | `Short` | `144.85` | 36,040,000.00 USD | 601,130.00 USD | 0.00 USD | `+49.02%` | `4,150.00` |
| `Live` | `Short` | `145.15` | 36,040,000.00 USD | 3,100.00 USD | 0.00 USD | `+49.33%` | `21.34` |
| `Live` | `Short` | `145.35` | 36,060,000.00 USD | 15,840.00 USD | 0.00 USD | `+49.54%` | `109.00` |
| `Live` | `Short` | `145.45` | 36,090,000.00 USD | 28,990.00 USD | 0.00 USD | `+49.64%` | `199.30` |
| `Live` | `Short` | `145.85` | 36,090,000.00 USD | 7,120.00 USD | 0.00 USD | `+50.05%` | `48.84` |
| `Live` | `Short` | `145.95` | 36,200,000.00 USD | 106,560.00 USD | 0.00 USD | `+50.15%` | `730.14` |
| `Live` | `Short` | `146.15` | 36,290,000.00 USD | 89,370.00 USD | 0.00 USD | `+50.36%` | `611.50` |
| `Live` | `Short` | `146.25` | 36,290,000.00 USD | 2,920.00 USD | 0.00 USD | `+50.46%` | `19.95` |
| `Live` | `Short` | `146.35` | 36,300,000.00 USD | 8,510.00 USD | 0.00 USD | `+50.57%` | `58.16` |
| `Live` | `Short` | `146.55` | 36,410,000.00 USD | 103,990.00 USD | 0.00 USD | `+50.77%` | `709.57` |
| `Live` | `Short` | `146.65` | 36,990,000.00 USD | 587,730.00 USD | 0.00 USD | `+50.87%` | `4,007.68` |
| `Live` | `Short` | `146.85` | 37,000,000.00 USD | 2,120.00 USD | 0.00 USD | `+51.08%` | `14.41` |
| `Live` | `Short` | `146.95` | 37,070,000.00 USD | 78,060.00 USD | 0.00 USD | `+51.18%` | `531.18` |
| `Live` | `Short` | `147.05` | 37,070,000.00 USD | 166.17 USD | 0.00 USD | `+51.29%` | `1.13` |
| `Live` | `Short` | `147.15` | 37,080,000.00 USD | 1,730.00 USD | 0.00 USD | `+51.39%` | `11.75` |
| `Live` | `Short` | `147.35` | 37,080,000.00 USD | 169.45 USD | 0.00 USD | `+51.59%` | `1.15` |
| `Live` | `Short` | `147.45` | 37,080,000.00 USD | 204.96 USD | 0.00 USD | `+51.70%` | `1.39` |
| `Live` | `Short` | `147.55` | 37,080,000.00 USD | 1,280.00 USD | 0.00 USD | `+51.80%` | `8.66` |
| `Live` | `Short` | `147.65` | 37,520,000.00 USD | 443,190.00 USD | 0.00 USD | `+51.90%` | `3,001.61` |
| `Live` | `Short` | `147.75` | 37,550,000.00 USD | 28,660.00 USD | 0.00 USD | `+52.01%` | `194.00` |
| `Live` | `Short` | `147.85` | 37,550,000.00 USD | 510.08 USD | 0.00 USD | `+52.11%` | `3.45` |
| `Live` | `Short` | `148.15` | 37,550,000.00 USD | 102.22 USD | 0.00 USD | `+52.42%` | `0.69` |
| `Live` | `Short` | `148.35` | 37,570,000.00 USD | 18,560.00 USD | 0.00 USD | `+52.62%` | `125.13` |
| `Live` | `Short` | `148.45` | 37,570,000.00 USD | 163.29 USD | 0.00 USD | `+52.73%` | `1.10` |
| `Live` | `Short` | `148.55` | 37,910,000.00 USD | 344,780.00 USD | 0.00 USD | `+52.83%` | `2,321.00` |
| `Live` | `Short` | `148.75` | 38,090,000.00 USD | 178,250.00 USD | 0.00 USD | `+53.03%` | `1,198.33` |
| `Live` | `Short` | `148.95` | 38,610,000.00 USD | 521,320.00 USD | 0.00 USD | `+53.24%` | `3,500.00` |
| `Live` | `Short` | `149.15` | 38,610,000.00 USD | 1,120.00 USD | 0.00 USD | `+53.45%` | `7.50` |
| `Live` | `Short` | `149.45` | 40,000,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+53.76%` | `9,282.33` |
| `Live` | `Short` | `149.55` | 40,000,000.00 USD | 116.65 USD | 0.00 USD | `+53.86%` | `0.78` |
| `Live` | `Short` | `149.65` | 40,020,000.00 USD | 16,030.00 USD | 0.00 USD | `+53.96%` | `107.15` |
| `Live` | `Short` | `149.95` | 40,250,000.00 USD | 234,200.00 USD | 0.00 USD | `+54.27%` | `1,561.87` |
| `Live` | `Short` | `150.05` | 40,250,000.00 USD | 2,930.00 USD | 0.00 USD | `+54.37%` | `19.54` |
| `Live` | `Short` | `150.15` | 40,380,000.00 USD | 123,300.00 USD | 0.00 USD | `+54.48%` | `821.21` |
| `Live` | `Short` | `150.85` | 44,950,000.00 USD | 4,570,000.00 USD | 0.00 USD | `+55.20%` | `30,310.49` |
| `Live` | `Short` | `151.05` | 44,950,000.00 USD | 347.42 USD | 0.00 USD | `+55.40%` | `2.30` |
| `Live` | `Short` | `151.15` | 44,960,000.00 USD | 5,550.00 USD | 0.00 USD | `+55.50%` | `36.74` |
| `Live` | `Short` | `151.35` | 44,980,000.00 USD | 22,020.00 USD | 0.00 USD | `+55.71%` | `145.49` |
| `Live` | `Short` | `151.45` | 44,990,000.00 USD | 8,830.00 USD | 0.00 USD | `+55.81%` | `58.32` |
| `Live` | `Short` | `151.95` | 44,990,000.00 USD | 1,920.00 USD | 0.00 USD | `+56.33%` | `12.64` |
| `Live` | `Short` | `152.05` | 46,740,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+56.43%` | `11,488.27` |
| `Live` | `Short` | `152.15` | 48,600,000.00 USD | 1,860,000.00 USD | 0.00 USD | `+56.53%` | `12,257.64` |
| `Live` | `Short` | `152.25` | 48,600,000.00 USD | 200.97 USD | 0.00 USD | `+56.64%` | `1.32` |
| `Live` | `Short` | `152.35` | 48,930,000.00 USD | 331,280.00 USD | 0.00 USD | `+56.74%` | `2,174.44` |
| `Live` | `Short` | `152.45` | 48,940,000.00 USD | 3,150.00 USD | 0.00 USD | `+56.84%` | `20.65` |
| `Live` | `Short` | `152.75` | 48,940,000.00 USD | 2,800.00 USD | 0.00 USD | `+57.15%` | `18.30` |
| `Live` | `Short` | `153.05` | 48,940,000.00 USD | 1,060.00 USD | 0.00 USD | `+57.46%` | `6.95` |
| `Live` | `Short` | `153.15` | 48,940,000.00 USD | 2,810.00 USD | 0.00 USD | `+57.56%` | `18.37` |
| `Live` | `Short` | `153.25` | 48,940,000.00 USD | 239.07 USD | 0.00 USD | `+57.66%` | `1.56` |
| `Live` | `Short` | `153.35` | 48,990,000.00 USD | 46,960.00 USD | 0.00 USD | `+57.77%` | `306.26` |
| `Live` | `Short` | `153.65` | 49,000,000.00 USD | 8,340.00 USD | 0.00 USD | `+58.08%` | `54.29` |
| `Live` | `Short` | `153.85` | 49,000,000.00 USD | 995.41 USD | 0.00 USD | `+58.28%` | `6.47` |
| `Live` | `Short` | `154.15` | 49,000,000.00 USD | 292.89 USD | 0.00 USD | `+58.59%` | `1.90` |
| `Live` | `Short` | `154.25` | 49,000,000.00 USD | 2,340.00 USD | 0.00 USD | `+58.69%` | `15.20` |
| `Live` | `Short` | `154.45` | 49,010,000.00 USD | 4,240.00 USD | 0.00 USD | `+58.90%` | `27.45` |
| `Live` | `Short` | `154.55` | 49,010,000.00 USD | 1,860.00 USD | 0.00 USD | `+59.00%` | `12.03` |
| `Live` | `Short` | `155.05` | 49,010,000.00 USD | 2,340.00 USD | 0.00 USD | `+59.52%` | `15.09` |
| `Live` | `Short` | `155.25` | 49,010,000.00 USD | 1,110.00 USD | 0.00 USD | `+59.72%` | `7.16` |
| `Live` | `Short` | `155.45` | 49,010,000.00 USD | 118.14 USD | 0.00 USD | `+59.93%` | `0.76` |
| `Live` | `Short` | `155.55` | 49,010,000.00 USD | 1,430.00 USD | 0.00 USD | `+60.03%` | `9.22` |
| `Live` | `Short` | `155.75` | 49,020,000.00 USD | 4,050.00 USD | 0.00 USD | `+60.24%` | `26.02` |
| `Live` | `Short` | `156.15` | 49,020,000.00 USD | 8,130.00 USD | 0.00 USD | `+60.65%` | `52.09` |
| `Live` | `Short` | `156.35` | 49,020,000.00 USD | 197.00 USD | 0.00 USD | `+60.85%` | `1.26` |
| `Live` | `Short` | `156.45` | 49,030,000.00 USD | 4,900.00 USD | 0.00 USD | `+60.96%` | `31.29` |
| `Live` | `Short` | `156.85` | 49,040,000.00 USD | 6,280.00 USD | 0.00 USD | `+61.37%` | `40.03` |
| `Live` | `Short` | `157.15` | 49,080,000.00 USD | 49,270.00 USD | 0.00 USD | `+61.68%` | `313.50` |
| `Live` | `Short` | `157.65` | 49,090,000.00 USD | 654.25 USD | 0.00 USD | `+62.19%` | `4.15` |
| `Live` | `Short` | `157.75` | 49,260,000.00 USD | 173,110.00 USD | 0.00 USD | `+62.29%` | `1,097.34` |
| `Live` | `Short` | `158.35` | 49,260,000.00 USD | 299.28 USD | 0.00 USD | `+62.91%` | `1.89` |
| `Live` | `Short` | `158.45` | 49,500,000.00 USD | 237,670.00 USD | 0.00 USD | `+63.01%` | `1,500.00` |
| `Live` | `Short` | `159.05` | 49,540,000.00 USD | 45,380.00 USD | 0.00 USD | `+63.63%` | `285.30` |
| `Live` | `Short` | `159.45` | 49,570,000.00 USD | 27,950.00 USD | 0.00 USD | `+64.04%` | `175.30` |
| `Live` | `Short` | `159.55` | 49,570,000.00 USD | 655.75 USD | 0.00 USD | `+64.15%` | `4.11` |
| `Live` | `Short` | `159.65` | 50,000,000.00 USD | 432,810.00 USD | 0.00 USD | `+64.25%` | `2,711.01` |
| `Live` | `Short` | `159.75` | 53,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | `+64.35%` | `22,770.74` |
| `Live` | `Short` | `160.05` | 53,640,000.00 USD | 448.14 USD | 0.00 USD | `+64.66%` | `2.80` |
| `Live` | `Short` | `160.15` | 54,330,000.00 USD | 683,500.00 USD | 0.00 USD | `+64.76%` | `4,267.86` |
| `Live` | `Short` | `160.35` | 54,330,000.00 USD | 655.83 USD | 0.00 USD | `+64.97%` | `4.09` |
| `Live` | `Short` | `160.55` | 54,430,000.00 USD | 102,250.00 USD | 0.00 USD | `+65.17%` | `636.89` |
| `Live` | `Short` | `161.05` | 54,430,000.00 USD | 2,240.00 USD | 0.00 USD | `+65.69%` | `13.93` |
| `Live` | `Short` | `161.25` | 54,520,000.00 USD | 85,560.00 USD | 0.00 USD | `+65.90%` | `530.61` |
| `Live` | `Short` | `161.35` | 54,540,000.00 USD | 21,430.00 USD | 0.00 USD | `+66.00%` | `132.81` |
| `Live` | `Short` | `161.55` | 54,540,000.00 USD | 410.34 USD | 0.00 USD | `+66.20%` | `2.54` |
| `Live` | `Short` | `161.75` | 54,860,000.00 USD | 323,500.00 USD | 0.00 USD | `+66.41%` | `2,000.00` |
| `Live` | `Short` | `161.85` | 54,880,000.00 USD | 18,950.00 USD | 0.00 USD | `+66.51%` | `117.09` |
| `Live` | `Short` | `161.95` | 55,020,000.00 USD | 144,610.00 USD | 0.00 USD | `+66.62%` | `892.95` |
| `Live` | `Short` | `162.15` | 55,250,000.00 USD | 228,980.00 USD | 0.00 USD | `+66.82%` | `1,412.13` |
| `Live` | `Short` | `162.45` | 55,260,000.00 USD | 5,980.00 USD | 0.00 USD | `+67.13%` | `36.83` |
| `Live` | `Short` | `163.55` | 55,260,000.00 USD | 1,060.00 USD | 0.00 USD | `+68.26%` | `6.49` |
| `Live` | `Short` | `163.85` | 55,260,000.00 USD | 786.48 USD | 0.00 USD | `+68.57%` | `4.80` |
| `Live` | `Short` | `163.95` | 55,470,000.00 USD | 206,830.00 USD | 0.00 USD | `+68.67%` | `1,261.56` |
| `Live` | `Short` | `165.15` | 55,470,000.00 USD | 198.18 USD | 0.00 USD | `+69.91%` | `1.20` |
| `Live` | `Short` | `165.55` | 55,470,000.00 USD | 1,370.00 USD | 0.00 USD | `+70.32%` | `8.29` |
| `Live` | `Short` | `165.85` | 55,470,000.00 USD | 681.64 USD | 0.00 USD | `+70.63%` | `4.11` |
| `Live` | `Short` | `166.15` | 55,470,000.00 USD | 996.90 USD | 0.00 USD | `+70.94%` | `6.00` |
| `Live` | `Short` | `166.25` | 55,490,000.00 USD | 14,070.00 USD | 0.00 USD | `+71.04%` | `84.61` |
| `Live` | `Short` | `166.75` | 55,490,000.00 USD | 3,220.00 USD | 0.00 USD | `+71.55%` | `19.33` |
| `Live` | `Short` | `166.95` | 55,490,000.00 USD | 3,590.00 USD | 0.00 USD | `+71.76%` | `21.53` |
| `Live` | `Short` | `167.65` | 55,490,000.00 USD | 115.68 USD | 0.00 USD | `+72.48%` | `0.69` |
| `Live` | `Short` | `167.75` | 55,500,000.00 USD | 2,520.00 USD | 0.00 USD | `+72.58%` | `15.01` |
| `Live` | `Short` | `168.05` | 55,540,000.00 USD | 46,060.00 USD | 0.00 USD | `+72.89%` | `274.10` |
| `Live` | `Short` | `168.15` | 61,220,000.00 USD | 5,670,000.00 USD | 0.00 USD | `+72.99%` | `33,744.03` |
| `Live` | `Short` | `168.35` | 61,230,000.00 USD | 19,740.00 USD | 0.00 USD | `+73.20%` | `117.24` |
| `Live` | `Short` | `168.55` | 61,350,000.00 USD | 111,680.00 USD | 0.00 USD | `+73.41%` | `662.62` |
| `Live` | `Short` | `168.65` | 61,670,000.00 USD | 325,850.00 USD | 0.00 USD | `+73.51%` | `1,932.10` |
| `Live` | `Short` | `168.75` | 61,700,000.00 USD | 25,920.00 USD | 0.00 USD | `+73.61%` | `153.59` |
| `Live` | `Short` | `169.75` | 61,700,000.00 USD | 100.15 USD | 0.00 USD | `+74.64%` | `0.59` |
| `Live` | `Short` | `170.45` | 61,700,000.00 USD | 446.58 USD | 0.00 USD | `+75.36%` | `2.62` |
| `Live` | `Short` | `171.35` | 61,880,000.00 USD | 181,940.00 USD | 0.00 USD | `+76.29%` | `1,061.79` |
| `Live` | `Short` | `171.45` | 61,880,000.00 USD | 1,570.00 USD | 0.00 USD | `+76.39%` | `9.17` |
| `Live` | `Short` | `172.05` | 61,900,000.00 USD | 20,480.00 USD | 0.00 USD | `+77.01%` | `119.02` |
| `Live` | `Short` | `172.45` | 61,950,000.00 USD | 51,730.00 USD | 0.00 USD | `+77.42%` | `300.00` |
| `Live` | `Short` | `173.05` | 61,990,000.00 USD | 36,010.00 USD | 0.00 USD | `+78.03%` | `208.07` |
| `Live` | `Short` | `173.15` | 62,010,000.00 USD | 15,580.00 USD | 0.00 USD | `+78.14%` | `90.00` |
| `Live` | `Short` | `173.35` | 62,030,000.00 USD | 28,070.00 USD | 0.00 USD | `+78.34%` | `161.92` |
| `Live` | `Short` | `173.45` | 62,050,000.00 USD | 16,540.00 USD | 0.00 USD | `+78.45%` | `95.36` |
| `Live` | `Short` | `173.85` | 62,050,000.00 USD | 695.40 USD | 0.00 USD | `+78.86%` | `4.00` |
| `Live` | `Short` | `174.05` | 62,050,000.00 USD | 205.38 USD | 0.00 USD | `+79.06%` | `1.18` |
| `Live` | `Short` | `174.15` | 62,160,000.00 USD | 104,490.00 USD | 0.00 USD | `+79.17%` | `600.00` |
| `Live` | `Short` | `174.25` | 62,400,000.00 USD | 245,010.00 USD | 0.00 USD | `+79.27%` | `1,406.07` |
| `Live` | `Short` | `174.35` | 62,610,000.00 USD | 205,490.00 USD | 0.00 USD | `+79.37%` | `1,178.60` |
| `Live` | `Short` | `174.75` | 62,610,000.00 USD | 146.79 USD | 0.00 USD | `+79.78%` | `0.84` |
| `Live` | `Short` | `174.95` | 62,610,000.00 USD | 348.15 USD | 0.00 USD | `+79.99%` | `1.99` |
| `Live` | `Short` | `175.45` | 62,610,000.00 USD | 119.31 USD | 0.00 USD | `+80.50%` | `0.68` |
| `Live` | `Short` | `175.75` | 62,610,000.00 USD | 263.62 USD | 0.00 USD | `+80.81%` | `1.50` |
| `Live` | `Short` | `175.85` | 101,290,000.00 USD | 38,690,000.00 USD | 0.00 USD | `+80.92%` | `220,000.19` |
| `Live` | `Short` | `176.15` | 101,310,000.00 USD | 19,920.00 USD | 0.00 USD | `+81.22%` | `113.07` |
| `Live` | `Short` | `176.25` | 101,320,000.00 USD | 625.69 USD | 0.00 USD | `+81.33%` | `3.55` |
| `Live` | `Short` | `176.35` | 104,840,000.00 USD | 3,530,000.00 USD | 0.00 USD | `+81.43%` | `20,000.00` |
| `Live` | `Short` | `176.65` | 104,950,000.00 USD | 105,990.00 USD | 0.00 USD | `+81.74%` | `600.00` |
| `Live` | `Short` | `176.75` | 105,150,000.00 USD | 204,830.00 USD | 0.00 USD | `+81.84%` | `1,158.88` |
| `Live` | `Short` | `176.95` | 105,420,000.00 USD | 265,430.00 USD | 0.00 USD | `+82.05%` | `1,500.00` |
| `Live` | `Short` | `177.55` | 105,440,000.00 USD | 25,670.00 USD | 0.00 USD | `+82.66%` | `144.60` |
| `Live` | `Short` | `177.65` | 105,440,000.00 USD | 637.76 USD | 0.00 USD | `+82.77%` | `3.59` |
| `Live` | `Short` | `177.95` | 105,520,000.00 USD | 78,300.00 USD | 0.00 USD | `+83.08%` | `440.00` |
| `Live` | `Short` | `178.35` | 105,530,000.00 USD | 7,280.00 USD | 0.00 USD | `+83.49%` | `40.84` |
| `Live` | `Short` | `178.45` | 105,530,000.00 USD | 1,320.00 USD | 0.00 USD | `+83.59%` | `7.37` |
| `Live` | `Short` | `179.05` | 105,580,000.00 USD | 44,780.00 USD | 0.00 USD | `+84.21%` | `250.10` |
| `Live` | `Short` | `179.25` | 105,720,000.00 USD | 143,400.00 USD | 0.00 USD | `+84.41%` | `800.00` |
| `Live` | `Short` | `179.45` | 106,760,000.00 USD | 1,040,000.00 USD | 0.00 USD | `+84.62%` | `5,820.70` |
| `Live` | `Short` | `179.65` | 106,770,000.00 USD | 718.60 USD | 0.00 USD | `+84.83%` | `4.00` |
| `Live` | `Short` | `179.75` | 106,770,000.00 USD | 280.41 USD | 0.00 USD | `+84.93%` | `1.56` |
| `Live` | `Short` | `180.25` | 106,770,000.00 USD | 2,030.00 USD | 0.00 USD | `+85.44%` | `11.27` |
| `Live` | `Short` | `180.35` | 108,110,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+85.55%` | `7,439.01` |
| `Live` | `Short` | `180.55` | 108,110,000.00 USD | 3,970.00 USD | 0.00 USD | `+85.75%` | `22.01` |
| `Live` | `Short` | `181.05` | 108,190,000.00 USD | 77,440.00 USD | 0.00 USD | `+86.27%` | `427.73` |
| `Live` | `Short` | `181.15` | 108,210,000.00 USD | 18,120.00 USD | 0.00 USD | `+86.37%` | `100.00` |
| `Live` | `Short` | `181.55` | 108,210,000.00 USD | 254.17 USD | 0.00 USD | `+86.78%` | `1.40` |
| `Live` | `Short` | `181.95` | 108,210,000.00 USD | 1,370.00 USD | 0.00 USD | `+87.19%` | `7.52` |
| `Live` | `Short` | `182.05` | 108,300,000.00 USD | 91,030.00 USD | 0.00 USD | `+87.29%` | `500.00` |
| `Live` | `Short` | `182.15` | 108,310,000.00 USD | 3,990.00 USD | 0.00 USD | `+87.40%` | `21.93` |
| `Live` | `Short` | `182.45` | 108,310,000.00 USD | 248.13 USD | 0.00 USD | `+87.71%` | `1.36` |
| `Live` | `Short` | `183.55` | 108,310,000.00 USD | 9,490.00 USD | 0.00 USD | `+88.84%` | `51.72` |
| `Live` | `Short` | `184.25` | 108,320,000.00 USD | 1,680.00 USD | 0.00 USD | `+89.56%` | `9.12` |
| `Live` | `Short` | `184.65` | 108,320,000.00 USD | 2,080.00 USD | 0.00 USD | `+89.97%` | `11.24` |
| `Live` | `Short` | `184.95` | 108,480,000.00 USD | 165,230.00 USD | 0.00 USD | `+90.28%` | `893.35` |
| `Live` | `Short` | `185.15` | 108,490,000.00 USD | 10,920.00 USD | 0.00 USD | `+90.48%` | `59.00` |
| `Live` | `Short` | `185.25` | 108,500,000.00 USD | 737.29 USD | 0.00 USD | `+90.59%` | `3.98` |
| `Live` | `Short` | `185.45` | 108,500,000.00 USD | 2,770.00 USD | 0.00 USD | `+90.79%` | `14.94` |
| `Live` | `Short` | `185.65` | 108,500,000.00 USD | 137.38 USD | 0.00 USD | `+91.00%` | `0.74` |
| `Live` | `Short` | `185.75` | 108,510,000.00 USD | 8,410.00 USD | 0.00 USD | `+91.10%` | `45.27` |
| `Live` | `Short` | `186.65` | 108,560,000.00 USD | 53,620.00 USD | 0.00 USD | `+92.03%` | `287.30` |
| `Live` | `Short` | `186.85` | 112,300,000.00 USD | 3,740,000.00 USD | 0.00 USD | `+92.23%` | `20,011.72` |
| `Live` | `Short` | `186.95` | 112,300,000.00 USD | 805.75 USD | 0.00 USD | `+92.34%` | `4.31` |
| `Live` | `Short` | `187.05` | 112,310,000.00 USD | 10,740.00 USD | 0.00 USD | `+92.44%` | `57.40` |
| `Live` | `Short` | `187.45` | 112,310,000.00 USD | 2,460.00 USD | 0.00 USD | `+92.85%` | `13.11` |
| `Live` | `Short` | `187.65` | 112,310,000.00 USD | 232.69 USD | 0.00 USD | `+93.06%` | `1.24` |
| `Live` | `Short` | `187.85` | 112,320,000.00 USD | 1,560.00 USD | 0.00 USD | `+93.26%` | `8.32` |
| `Live` | `Short` | `188.55` | 112,320,000.00 USD | 231.92 USD | 0.00 USD | `+93.98%` | `1.23` |
| `Live` | `Short` | `188.65` | 112,340,000.00 USD | 29,110.00 USD | 0.00 USD | `+94.08%` | `154.32` |
| `Live` | `Short` | `188.95` | 112,350,000.00 USD | 1,450.00 USD | 0.00 USD | `+94.39%` | `7.69` |
| `Live` | `Short` | `189.05` | 112,350,000.00 USD | 1,000.00 USD | 0.00 USD | `+94.50%` | `5.30` |
| `Live` | `Short` | `189.25` | 112,350,000.00 USD | 456.09 USD | 0.00 USD | `+94.70%` | `2.41` |
| `Live` | `Short` | `189.65` | 112,350,000.00 USD | 117.58 USD | 0.00 USD | `+95.11%` | `0.62` |
| `Live` | `Short` | `189.85` | 112,350,000.00 USD | 189.85 USD | 0.00 USD | `+95.32%` | `1.00` |
| `Live` | `Short` | `189.95` | 112,630,000.00 USD | 284,930.00 USD | 0.00 USD | `+95.42%` | `1,500.00` |
| `Live` | `Short` | `190.15` | 112,630,000.00 USD | 148.32 USD | 0.00 USD | `+95.63%` | `0.78` |
| `Live` | `Short` | `190.45` | 112,630,000.00 USD | 118.08 USD | 0.00 USD | `+95.94%` | `0.62` |
| `Live` | `Short` | `190.85` | 112,630,000.00 USD | 118.33 USD | 0.00 USD | `+96.35%` | `0.62` |
| `Live` | `Short` | `190.95` | 126,200,000.00 USD | 13,570,000.00 USD | 0.00 USD | `+96.45%` | `71,044.42` |
| `Live` | `Short` | `191.05` | 126,200,000.00 USD | 278.93 USD | 0.00 USD | `+96.55%` | `1.46` |
| `Live` | `Short` | `191.55` | 126,200,000.00 USD | 191.55 USD | 0.00 USD | `+97.07%` | `1.00` |
| `Live` | `Short` | `191.65` | 126,260,000.00 USD | 62,880.00 USD | 0.00 USD | `+97.17%` | `328.11` |
| `Live` | `Short` | `191.95` | 126,260,000.00 USD | 322.48 USD | 0.00 USD | `+97.48%` | `1.68` |
| `Live` | `Short` | `192.55` | 126,270,000.00 USD | 5,460.00 USD | 0.00 USD | `+98.10%` | `28.34` |
| `Live` | `Short` | `192.75` | 126,650,000.00 USD | 385,500.00 USD | 0.00 USD | `+98.30%` | `2,000.00` |
| `Live` | `Short` | `192.85` | 126,670,000.00 USD | 19,780.00 USD | 0.00 USD | `+98.41%` | `102.58` |
| `Live` | `Short` | `193.05` | 126,680,000.00 USD | 9,320.00 USD | 0.00 USD | `+98.61%` | `48.28` |
| `Live` | `Short` | `193.55` | 126,800,000.00 USD | 114,580.00 USD | 0.00 USD | `+99.13%` | `592.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.05` | 9,350,000.00 USD | 0.00 USD | 14,230.00 USD | `-76.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.35` | 9,330,000.00 USD | 0.00 USD | 499.56 USD | `-68.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `32.05` | 9,330,000.00 USD | 0.00 USD | 1,230.00 USD | `-67.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.05` | 9,330,000.00 USD | 0.00 USD | 818.32 USD | `-66.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.85` | 9,330,000.00 USD | 0.00 USD | 1,340.00 USD | `-64.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 9,330,000.00 USD | 0.00 USD | 2,160.00 USD | `-62.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.45` | 9,330,000.00 USD | 0.00 USD | 434.85 USD | `-62.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.05` | 9,330,000.00 USD | 0.00 USD | 267.87 USD | `-60.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.55` | 9,320,000.00 USD | 0.00 USD | 3,460.00 USD | `-59.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.75` | 9,320,000.00 USD | 0.00 USD | 157.01 USD | `-59.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 9,320,000.00 USD | 0.00 USD | 1,050.00 USD | `-58.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.75` | 9,320,000.00 USD | 0.00 USD | 120.66 USD | `-57.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.15` | 9,320,000.00 USD | 0.00 USD | 121.81 USD | `-56.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.55` | 9,320,000.00 USD | 0.00 USD | 170,530.00 USD | `-56.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.75` | 9,150,000.00 USD | 0.00 USD | 105.00 USD | `-54.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 9,150,000.00 USD | 0.00 USD | 64,240.00 USD | `-53.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.75` | 9,090,000.00 USD | 0.00 USD | 251.05 USD | `-51.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.75` | 9,080,000.00 USD | 0.00 USD | 143.25 USD | `-50.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.85` | 9,080,000.00 USD | 0.00 USD | 191.40 USD | `-50.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 9,080,000.00 USD | 0.00 USD | 50,240.00 USD | `-50.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.55` | 9,030,000.00 USD | 0.00 USD | 664.65 USD | `-50.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.75` | 9,030,000.00 USD | 0.00 USD | 103.35 USD | `-49.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 9,030,000.00 USD | 0.00 USD | 4,660.00 USD | `-48.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.25` | 9,030,000.00 USD | 0.00 USD | 107.03 USD | `-48.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 9,030,000.00 USD | 0.00 USD | 102.62 USD | `-47.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.25` | 9,030,000.00 USD | 0.00 USD | 134.28 USD | `-47.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 9,030,000.00 USD | 0.00 USD | 3,950.00 USD | `-46.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.15` | 9,020,000.00 USD | 0.00 USD | 102.74 USD | `-46.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 9,020,000.00 USD | 0.00 USD | 126.12 USD | `-45.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 9,020,000.00 USD | 0.00 USD | 200.15 USD | `-45.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 9,020,000.00 USD | 0.00 USD | 24,450.00 USD | `-45.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 9,000,000.00 USD | 0.00 USD | 1,660.00 USD | `-45.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 9,000,000.00 USD | 0.00 USD | 641.57 USD | `-44.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 9,000,000.00 USD | 0.00 USD | 139.87 USD | `-43.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 9,000,000.00 USD | 0.00 USD | 209.19 USD | `-43.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 9,000,000.00 USD | 0.00 USD | 4,350.00 USD | `-42.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 8,990,000.00 USD | 0.00 USD | 894.56 USD | `-42.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 8,990,000.00 USD | 0.00 USD | 4,930.00 USD | `-42.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 8,990,000.00 USD | 0.00 USD | 6,790.00 USD | `-41.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.35` | 8,980,000.00 USD | 0.00 USD | 265.53 USD | `-41.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.95` | 8,980,000.00 USD | 0.00 USD | 268.31 USD | `-40.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.05` | 8,980,000.00 USD | 0.00 USD | 158.48 USD | `-40.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.15` | 8,980,000.00 USD | 0.00 USD | 3,820.00 USD | `-40.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.25` | 8,980,000.00 USD | 0.00 USD | 428.72 USD | `-40.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.05` | 8,980,000.00 USD | 0.00 USD | 295.25 USD | `-39.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.35` | 8,970,000.00 USD | 0.00 USD | 200.01 USD | `-38.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.55` | 8,970,000.00 USD | 0.00 USD | 1,460.00 USD | `-38.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.95` | 8,970,000.00 USD | 0.00 USD | 9,040.00 USD | `-38.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.05` | 8,960,000.00 USD | 0.00 USD | 35,050.00 USD | `-38.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.15` | 8,930,000.00 USD | 0.00 USD | 2,820.00 USD | `-38.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.25` | 8,930,000.00 USD | 0.00 USD | 488.63 USD | `-38.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.35` | 8,930,000.00 USD | 0.00 USD | 258.90 USD | `-37.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.45` | 8,930,000.00 USD | 0.00 USD | 206.13 USD | `-37.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.55` | 8,930,000.00 USD | 0.00 USD | 724.78 USD | `-37.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.05` | 8,920,000.00 USD | 0.00 USD | 14,350.00 USD | `-37.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.35` | 8,910,000.00 USD | 0.00 USD | 142.33 USD | `-36.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.45` | 8,910,000.00 USD | 0.00 USD | 100.78 USD | `-36.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.55` | 8,910,000.00 USD | 0.00 USD | 243.74 USD | `-36.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.05` | 8,910,000.00 USD | 0.00 USD | 6,720.00 USD | `-36.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.55` | 8,900,000.00 USD | 0.00 USD | 136.98 USD | `-35.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.05` | 8,900,000.00 USD | 0.00 USD | 9,990.00 USD | `-35.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.55` | 8,890,000.00 USD | 0.00 USD | 2,980.00 USD | `-34.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.95` | 8,890,000.00 USD | 0.00 USD | 222.55 USD | `-34.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.25` | 8,890,000.00 USD | 0.00 USD | 163.19 USD | `-33.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.85` | 8,890,000.00 USD | 0.00 USD | 129.70 USD | `-33.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.05` | 8,890,000.00 USD | 0.00 USD | 2,440.00 USD | `-33.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.15` | 8,890,000.00 USD | 0.00 USD | 2,190.00 USD | `-32.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.55` | 8,880,000.00 USD | 0.00 USD | 2,200.00 USD | `-32.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.05` | 8,880,000.00 USD | 0.00 USD | 7,100.00 USD | `-32.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.55` | 8,880,000.00 USD | 0.00 USD | 541.72 USD | `-31.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.05` | 8,880,000.00 USD | 0.00 USD | 335.25 USD | `-31.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.15` | 8,870,000.00 USD | 0.00 USD | 268.60 USD | `-30.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.05` | 8,870,000.00 USD | 0.00 USD | 195.30 USD | `-29.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.45` | 8,870,000.00 USD | 0.00 USD | 7,600.00 USD | `-29.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.55` | 8,870,000.00 USD | 0.00 USD | 5,610.00 USD | `-29.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.65` | 8,860,000.00 USD | 0.00 USD | 552.63 USD | `-29.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.75` | 8,860,000.00 USD | 0.00 USD | 1,200.00 USD | `-29.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.05` | 8,860,000.00 USD | 0.00 USD | 11,360.00 USD | `-28.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.15` | 8,850,000.00 USD | 0.00 USD | 172.18 USD | `-28.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.25` | 8,850,000.00 USD | 0.00 USD | 668.96 USD | `-28.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.65` | 8,850,000.00 USD | 0.00 USD | 107.96 USD | `-28.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.75` | 8,850,000.00 USD | 0.00 USD | 42,360.00 USD | `-28.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.85` | 8,800,000.00 USD | 0.00 USD | 365.32 USD | `-28.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.95` | 8,800,000.00 USD | 0.00 USD | 1,510.00 USD | `-28.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.05` | 8,800,000.00 USD | 0.00 USD | 43,920.00 USD | `-27.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.25` | 8,760,000.00 USD | 0.00 USD | 5,270.00 USD | `-27.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.35` | 8,750,000.00 USD | 0.00 USD | 562.80 USD | `-27.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.55` | 8,750,000.00 USD | 0.00 USD | 681.51 USD | `-27.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.65` | 8,750,000.00 USD | 0.00 USD | 4,920.00 USD | `-27.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.75` | 8,750,000.00 USD | 0.00 USD | 2,790.00 USD | `-27.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.05` | 8,740,000.00 USD | 0.00 USD | 265.02 USD | `-26.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.35` | 8,740,000.00 USD | 0.00 USD | 32,450.00 USD | `-26.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.45` | 8,710,000.00 USD | 0.00 USD | 289.37 USD | `-26.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.65` | 8,710,000.00 USD | 0.00 USD | 1,930.00 USD | `-26.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.75` | 8,710,000.00 USD | 0.00 USD | 235.34 USD | `-26.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.05` | 8,710,000.00 USD | 0.00 USD | 20,410.00 USD | `-25.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.55` | 8,690,000.00 USD | 0.00 USD | 19,560.00 USD | `-25.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.65` | 8,670,000.00 USD | 0.00 USD | 14,530.00 USD | `-25.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.95` | 8,650,000.00 USD | 0.00 USD | 66,160.00 USD | `-24.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.05` | 8,590,000.00 USD | 0.00 USD | 7,970.00 USD | `-24.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.35` | 8,580,000.00 USD | 0.00 USD | 733.50 USD | `-24.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.45` | 8,580,000.00 USD | 0.00 USD | 139.56 USD | `-24.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.05` | 8,580,000.00 USD | 0.00 USD | 510.95 USD | `-23.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.25` | 8,580,000.00 USD | 0.00 USD | 621.47 USD | `-23.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.35` | 8,580,000.00 USD | 0.00 USD | 1,660.00 USD | `-23.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.45` | 8,580,000.00 USD | 0.00 USD | 10,730.00 USD | `-23.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.55` | 8,570,000.00 USD | 0.00 USD | 331.00 USD | `-23.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.75` | 8,570,000.00 USD | 0.00 USD | 28,050.00 USD | `-23.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.05` | 8,540,000.00 USD | 0.00 USD | 30,040.00 USD | `-22.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.35` | 8,510,000.00 USD | 0.00 USD | 153.71 USD | `-22.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.45` | 8,510,000.00 USD | 0.00 USD | 163.73 USD | `-22.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.75` | 8,510,000.00 USD | 0.00 USD | 2,220.00 USD | `-22.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.95` | 8,510,000.00 USD | 0.00 USD | 277.98 USD | `-21.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.05` | 8,510,000.00 USD | 0.00 USD | 8,680.00 USD | `-21.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.15` | 8,500,000.00 USD | 0.00 USD | 254.34 USD | `-21.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.25` | 8,500,000.00 USD | 0.00 USD | 486.47 USD | `-21.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.35` | 8,500,000.00 USD | 0.00 USD | 358.84 USD | `-21.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.55` | 8,500,000.00 USD | 0.00 USD | 4,340.00 USD | `-21.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.65` | 8,490,000.00 USD | 0.00 USD | 536.55 USD | `-21.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.75` | 8,490,000.00 USD | 0.00 USD | 251.74 USD | `-21.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.05` | 8,490,000.00 USD | 0.00 USD | 17,010.00 USD | `-20.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.35` | 8,470,000.00 USD | 0.00 USD | 5,690.00 USD | `-20.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.45` | 8,470,000.00 USD | 0.00 USD | 1,020.00 USD | `-20.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.95` | 8,470,000.00 USD | 0.00 USD | 155.12 USD | `-19.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.05` | 8,470,000.00 USD | 0.00 USD | 56,850.00 USD | `-19.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.15` | 8,410,000.00 USD | 0.00 USD | 738.52 USD | `-19.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.55` | 8,410,000.00 USD | 0.00 USD | 18,590.00 USD | `-19.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.65` | 8,390,000.00 USD | 0.00 USD | 116.40 USD | `-19.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.75` | 8,390,000.00 USD | 0.00 USD | 379.58 USD | `-18.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.05` | 8,390,000.00 USD | 0.00 USD | 5,300.00 USD | `-18.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.15` | 8,380,000.00 USD | 0.00 USD | 201.04 USD | `-18.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.25` | 8,380,000.00 USD | 0.00 USD | 2,140.00 USD | `-18.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.45` | 8,380,000.00 USD | 0.00 USD | 5,850.00 USD | `-18.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.65` | 8,380,000.00 USD | 0.00 USD | 238.95 USD | `-18.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.75` | 8,380,000.00 USD | 0.00 USD | 1,330.00 USD | `-17.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.85` | 8,370,000.00 USD | 0.00 USD | 289.06 USD | `-17.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.95` | 8,370,000.00 USD | 0.00 USD | 808.29 USD | `-17.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.05` | 8,370,000.00 USD | 0.00 USD | 41,050.00 USD | `-17.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.15` | 8,330,000.00 USD | 0.00 USD | 8,360.00 USD | `-17.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.35` | 8,320,000.00 USD | 0.00 USD | 359.97 USD | `-17.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.45` | 8,320,000.00 USD | 0.00 USD | 8,770.00 USD | `-17.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.55` | 8,310,000.00 USD | 0.00 USD | 1,280.00 USD | `-17.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.65` | 8,310,000.00 USD | 0.00 USD | 1,280.00 USD | `-17.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.75` | 8,310,000.00 USD | 0.00 USD | 22,780.00 USD | `-16.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.85` | 8,290,000.00 USD | 0.00 USD | 341.19 USD | `-16.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.05` | 8,290,000.00 USD | 0.00 USD | 1,620.00 USD | `-16.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.25` | 8,290,000.00 USD | 0.00 USD | 266.50 USD | `-16.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.45` | 8,290,000.00 USD | 0.00 USD | 5,830.00 USD | `-16.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.55` | 8,280,000.00 USD | 0.00 USD | 572.48 USD | `-16.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.65` | 8,280,000.00 USD | 0.00 USD | 952.86 USD | `-16.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.75` | 8,280,000.00 USD | 0.00 USD | 1,390.00 USD | `-15.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.85` | 8,280,000.00 USD | 0.00 USD | 818.50 USD | `-15.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.95` | 8,280,000.00 USD | 0.00 USD | 70,900.00 USD | `-15.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.05` | 8,210,000.00 USD | 0.00 USD | 3,220.00 USD | `-15.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.15` | 8,200,000.00 USD | 0.00 USD | 684.31 USD | `-15.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.25` | 8,200,000.00 USD | 0.00 USD | 486.92 USD | `-15.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.35` | 8,200,000.00 USD | 0.00 USD | 386.22 USD | `-15.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.45` | 8,200,000.00 USD | 0.00 USD | 1,870.00 USD | `-15.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.55` | 8,200,000.00 USD | 0.00 USD | 1,310.00 USD | `-15.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.65` | 8,200,000.00 USD | 0.00 USD | 267,390.00 USD | `-14.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.75` | 7,930,000.00 USD | 0.00 USD | 1,660.00 USD | `-14.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.85` | 7,930,000.00 USD | 0.00 USD | 3,270.00 USD | `-14.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.95` | 7,930,000.00 USD | 0.00 USD | 945.63 USD | `-14.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.05` | 7,930,000.00 USD | 0.00 USD | 6,420.00 USD | `-14.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.15` | 7,920,000.00 USD | 0.00 USD | 239.47 USD | `-14.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.25` | 7,920,000.00 USD | 0.00 USD | 18,330.00 USD | `-14.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.45` | 7,900,000.00 USD | 0.00 USD | 168.57 USD | `-14.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.55` | 7,900,000.00 USD | 0.00 USD | 421.09 USD | `-14.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.65` | 7,900,000.00 USD | 0.00 USD | 1,100.00 USD | `-13.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.75` | 7,900,000.00 USD | 0.00 USD | 1,320.00 USD | `-13.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.95` | 7,900,000.00 USD | 0.00 USD | 4,550.00 USD | `-13.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.05` | 7,890,000.00 USD | 0.00 USD | 40,720.00 USD | `-13.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.15` | 7,850,000.00 USD | 0.00 USD | 25,220.00 USD | `-13.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.25` | 7,830,000.00 USD | 0.00 USD | 2,690.00 USD | `-13.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.45` | 7,820,000.00 USD | 0.00 USD | 965.26 USD | `-13.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.55` | 7,820,000.00 USD | 0.00 USD | 169.95 USD | `-13.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.65` | 7,820,000.00 USD | 0.00 USD | 858.35 USD | `-12.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.75` | 7,820,000.00 USD | 0.00 USD | 306.80 USD | `-12.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.95` | 7,820,000.00 USD | 0.00 USD | 137.62 USD | `-12.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.05` | 7,820,000.00 USD | 0.00 USD | 238,730.00 USD | `-12.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.15` | 7,580,000.00 USD | 0.00 USD | 437.67 USD | `-12.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.25` | 7,580,000.00 USD | 0.00 USD | 1,320.00 USD | `-12.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.35` | 7,580,000.00 USD | 0.00 USD | 39,110.00 USD | `-12.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.45` | 7,540,000.00 USD | 0.00 USD | 120.48 USD | `-12.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.55` | 7,540,000.00 USD | 0.00 USD | 105.23 USD | `-11.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.65` | 7,540,000.00 USD | 0.00 USD | 310.05 USD | `-11.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.75` | 7,540,000.00 USD | 0.00 USD | 1,410.00 USD | `-11.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.85` | 7,540,000.00 USD | 0.00 USD | 360.57 USD | `-11.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.95` | 7,540,000.00 USD | 0.00 USD | 2,050.00 USD | `-11.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.05` | 7,540,000.00 USD | 0.00 USD | 10,910.00 USD | `-11.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.15` | 7,530,000.00 USD | 0.00 USD | 2,210.00 USD | `-11.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.25` | 7,530,000.00 USD | 0.00 USD | 163.88 USD | `-11.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.35` | 7,520,000.00 USD | 0.00 USD | 4,080.00 USD | `-11.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.45` | 7,520,000.00 USD | 0.00 USD | 2,790.00 USD | `-11.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.55` | 7,520,000.00 USD | 0.00 USD | 417.17 USD | `-10.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.65` | 7,520,000.00 USD | 0.00 USD | 220,550.00 USD | `-10.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.75` | 7,300,000.00 USD | 0.00 USD | 3,060.00 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.85` | 7,290,000.00 USD | 0.00 USD | 788.60 USD | `-10.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.95` | 7,290,000.00 USD | 0.00 USD | 132.16 USD | `-10.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.05` | 7,290,000.00 USD | 0.00 USD | 280,590.00 USD | `-10.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.15` | 7,010,000.00 USD | 0.00 USD | 23,550.00 USD | `-10.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.25` | 6,990,000.00 USD | 0.00 USD | 8,200.00 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.35` | 6,980,000.00 USD | 0.00 USD | 102.20 USD | `-10.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.45` | 6,980,000.00 USD | 0.00 USD | 730.21 USD | `-10.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.55` | 6,980,000.00 USD | 0.00 USD | 7,840.00 USD | `-9.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.65` | 6,970,000.00 USD | 0.00 USD | 2,300.00 USD | `-9.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.85` | 6,970,000.00 USD | 0.00 USD | 131.78 USD | `-9.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.95` | 6,970,000.00 USD | 0.00 USD | 1,410.00 USD | `-9.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.05` | 6,970,000.00 USD | 0.00 USD | 132,850.00 USD | `-9.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.15` | 6,840,000.00 USD | 0.00 USD | 833.02 USD | `-9.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.25` | 6,830,000.00 USD | 0.00 USD | 1,870.00 USD | `-9.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.35` | 6,830,000.00 USD | 0.00 USD | 38,020.00 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.45` | 6,790,000.00 USD | 0.00 USD | 867.69 USD | `-9.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.55` | 6,790,000.00 USD | 0.00 USD | 32,610.00 USD | `-8.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.65` | 6,760,000.00 USD | 0.00 USD | 27,220.00 USD | `-8.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.75` | 6,730,000.00 USD | 0.00 USD | 53,390.00 USD | `-8.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.85` | 6,680,000.00 USD | 0.00 USD | 91,430.00 USD | `-8.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.95` | 6,590,000.00 USD | 0.00 USD | 141.43 USD | `-8.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.05` | 6,590,000.00 USD | 0.00 USD | 15,380.00 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.15` | 6,570,000.00 USD | 0.00 USD | 6,470.00 USD | `-8.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.25` | 6,570,000.00 USD | 0.00 USD | 1,340.00 USD | `-8.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.35` | 6,570,000.00 USD | 0.00 USD | 4,220.00 USD | `-8.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.45` | 6,560,000.00 USD | 0.00 USD | 5,280.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.55` | 6,560,000.00 USD | 0.00 USD | 348.35 USD | `-7.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.65` | 6,560,000.00 USD | 0.00 USD | 297.64 USD | `-7.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.75` | 6,560,000.00 USD | 0.00 USD | 105.01 USD | `-7.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.85` | 6,560,000.00 USD | 0.00 USD | 17,170.00 USD | `-7.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.95` | 6,540,000.00 USD | 0.00 USD | 87,020.00 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.05` | 6,450,000.00 USD | 0.00 USD | 3,270,000.00 USD | `-7.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.15` | 3,180,000.00 USD | 0.00 USD | 301.10 USD | `-7.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.25` | 3,180,000.00 USD | 0.00 USD | 12,170.00 USD | `-7.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.35` | 3,170,000.00 USD | 0.00 USD | 106,890.00 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.45` | 3,070,000.00 USD | 0.00 USD | 5,010.00 USD | `-6.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.55` | 3,060,000.00 USD | 0.00 USD | 13,500.00 USD | `-6.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.65` | 3,050,000.00 USD | 0.00 USD | 75,820.00 USD | `-6.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.75` | 2,970,000.00 USD | 0.00 USD | 4,980.00 USD | `-6.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.85` | 2,970,000.00 USD | 0.00 USD | 6,580.00 USD | `-6.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.95` | 2,960,000.00 USD | 0.00 USD | 7,300.00 USD | `-6.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.05` | 2,950,000.00 USD | 0.00 USD | 642,140.00 USD | `-6.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.15` | 2,310,000.00 USD | 0.00 USD | 1,120.00 USD | `-6.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.25` | 2,310,000.00 USD | 0.00 USD | 743.69 USD | `-6.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.35` | 2,310,000.00 USD | 0.00 USD | 16,770.00 USD | `-6.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.45` | 2,290,000.00 USD | 0.00 USD | 920.90 USD | `-5.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.55` | 2,290,000.00 USD | 0.00 USD | 20,520.00 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.65` | 2,270,000.00 USD | 0.00 USD | 38,100.00 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.75` | 2,230,000.00 USD | 0.00 USD | 21,870.00 USD | `-5.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.85` | 2,210,000.00 USD | 0.00 USD | 41,980.00 USD | `-5.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.95` | 2,170,000.00 USD | 0.00 USD | 33,290.00 USD | `-5.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.05` | 2,130,000.00 USD | 0.00 USD | 267,700.00 USD | `-5.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.15` | 1,870,000.00 USD | 0.00 USD | 49,850.00 USD | `-5.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.25` | 1,820,000.00 USD | 0.00 USD | 5,610.00 USD | `-5.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.35` | 1,810,000.00 USD | 0.00 USD | 18,900.00 USD | `-4.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.45` | 1,790,000.00 USD | 0.00 USD | 11,060.00 USD | `-4.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.55` | 1,780,000.00 USD | 0.00 USD | 17,280.00 USD | `-4.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.65` | 1,760,000.00 USD | 0.00 USD | 55,540.00 USD | `-4.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.75` | 1,710,000.00 USD | 0.00 USD | 6,990.00 USD | `-4.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.85` | 1,700,000.00 USD | 0.00 USD | 32,630.00 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.95` | 1,670,000.00 USD | 0.00 USD | 14,800.00 USD | `-4.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.05` | 1,650,000.00 USD | 0.00 USD | 44,480.00 USD | `-4.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.15` | 1,610,000.00 USD | 0.00 USD | 135,650.00 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.25` | 1,470,000.00 USD | 0.00 USD | 7,920.00 USD | `-4.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.35` | 1,470,000.00 USD | 0.00 USD | 385.54 USD | `-3.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.45` | 1,470,000.00 USD | 0.00 USD | 1,380.00 USD | `-3.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.55` | 1,460,000.00 USD | 0.00 USD | 1,120.00 USD | `-3.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.65` | 1,460,000.00 USD | 0.00 USD | 3,290.00 USD | `-3.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.75` | 1,460,000.00 USD | 0.00 USD | 3,660.00 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.85` | 1,460,000.00 USD | 0.00 USD | 1,200.00 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.95` | 1,460,000.00 USD | 0.00 USD | 106.16 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.05` | 1,460,000.00 USD | 0.00 USD | 111,370.00 USD | `-3.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.15` | 1,340,000.00 USD | 0.00 USD | 318.23 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.25` | 1,340,000.00 USD | 0.00 USD | 1,050.00 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.35` | 1,340,000.00 USD | 0.00 USD | 12,280.00 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.45` | 1,330,000.00 USD | 0.00 USD | 63,650.00 USD | `-2.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.55` | 1,270,000.00 USD | 0.00 USD | 91,930.00 USD | `-2.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.65` | 1,170,000.00 USD | 0.00 USD | 24,170.00 USD | `-2.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.75` | 1,150,000.00 USD | 0.00 USD | 27,810.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.85` | 1,120,000.00 USD | 0.00 USD | 22,510.00 USD | `-2.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.95` | 1,100,000.00 USD | 0.00 USD | 4,000.00 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.05` | 1,100,000.00 USD | 0.00 USD | 68,710.00 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.15` | 1,030,000.00 USD | 0.00 USD | 61,360.00 USD | `-2.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.25` | 965,990.00 USD | 0.00 USD | 7,310.00 USD | `-2.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.35` | 958,680.00 USD | 0.00 USD | 11,640.00 USD | `-1.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.45` | 947,040.00 USD | 0.00 USD | 77,760.00 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.55` | 869,280.00 USD | 0.00 USD | 162,880.00 USD | `-1.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.65` | 706,400.00 USD | 0.00 USD | 4,590.00 USD | `-1.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.75` | 701,810.00 USD | 0.00 USD | 60,370.00 USD | `-1.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.85` | 641,440.00 USD | 0.00 USD | 32,460.00 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.95` | 608,990.00 USD | 0.00 USD | 24,880.00 USD | `-1.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.05` | 584,100.00 USD | 0.00 USD | 24,810.00 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.15` | 559,290.00 USD | 0.00 USD | 27,080.00 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.25` | 532,210.00 USD | 0.00 USD | 7,290.00 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.35` | 524,930.00 USD | 0.00 USD | 63,210.00 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.45` | 461,720.00 USD | 0.00 USD | 152.39 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.55` | 461,570.00 USD | 0.00 USD | 8,770.00 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.65` | 452,800.00 USD | 0.00 USD | 25,020.00 USD | `-0.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.75` | 427,780.00 USD | 0.00 USD | 353,830.00 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.85` | 73,950.00 USD | 0.00 USD | 15,490.00 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.95` | 58,460.00 USD | 0.00 USD | 35,570.00 USD | `-0.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.05` | 22,890.00 USD | 0.00 USD | 16,800.00 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.15` | 6,080.00 USD | 0.00 USD | 6,080.00 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.25` | 32,370.00 USD | 32,370.00 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.35` | 40,520.00 USD | 8,150.00 USD | 0.00 USD | `+0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.45` | 52,960.00 USD | 12,440.00 USD | 0.00 USD | `+0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.55` | 57,260.00 USD | 4,300.00 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.65` | 71,480.00 USD | 14,220.00 USD | 0.00 USD | `+0.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.75` | 77,580.00 USD | 6,090.00 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.85` | 79,530.00 USD | 1,950.00 USD | 0.00 USD | `+0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.95` | 81,450.00 USD | 1,920.00 USD | 0.00 USD | `+0.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 95,630.00 USD | 14,180.00 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.15` | 96,890.00 USD | 1,260.00 USD | 0.00 USD | `+0.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.25` | 151,610.00 USD | 54,730.00 USD | 0.00 USD | `+1.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.35` | 153,010.00 USD | 1,400.00 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.45` | 157,130.00 USD | 4,120.00 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.55` | 270,970.00 USD | 113,850.00 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.65` | 309,360.00 USD | 38,380.00 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.75` | 392,110.00 USD | 82,750.00 USD | 0.00 USD | `+1.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.85` | 398,690.00 USD | 6,580.00 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.95` | 403,670.00 USD | 4,980.00 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 472,520.00 USD | 68,850.00 USD | 0.00 USD | `+1.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.15` | 490,010.00 USD | 17,490.00 USD | 0.00 USD | `+2.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.25` | 494,740.00 USD | 4,730.00 USD | 0.00 USD | `+2.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.35` | 534,120.00 USD | 39,390.00 USD | 0.00 USD | `+2.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.45` | 672,030.00 USD | 137,900.00 USD | 0.00 USD | `+2.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.55` | 806,690.00 USD | 134,670.00 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.65` | 820,560.00 USD | 13,860.00 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.75` | 830,330.00 USD | 9,780.00 USD | 0.00 USD | `+2.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.85` | 835,010.00 USD | 4,680.00 USD | 0.00 USD | `+2.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.95` | 877,430.00 USD | 42,410.00 USD | 0.00 USD | `+2.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 2,670,000.00 USD | 1,790,000.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.15` | 2,680,000.00 USD | 12,820.00 USD | 0.00 USD | `+3.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.25` | 2,690,000.00 USD | 5,240.00 USD | 0.00 USD | `+3.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.35` | 2,690,000.00 USD | 254.89 USD | 0.00 USD | `+3.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.45` | 2,690,000.00 USD | 6,690.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.55` | 2,700,000.00 USD | 2,490.00 USD | 0.00 USD | `+3.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.65` | 2,750,000.00 USD | 52,210.00 USD | 0.00 USD | `+3.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.75` | 2,750,000.00 USD | 1,220.00 USD | 0.00 USD | `+3.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.85` | 2,780,000.00 USD | 27,710.00 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.95` | 2,780,000.00 USD | 2,760.00 USD | 0.00 USD | `+3.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.05` | 3,010,000.00 USD | 227,930.00 USD | 0.00 USD | `+3.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.15` | 3,010,000.00 USD | 1,730.00 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.25` | 3,020,000.00 USD | 7,600.00 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.35` | 3,020,000.00 USD | 3,850.00 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.45` | 3,030,000.00 USD | 5,550.00 USD | 0.00 USD | `+4.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.55` | 3,030,000.00 USD | 4,880.00 USD | 0.00 USD | `+4.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.65` | 3,030,000.00 USD | 477.76 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.75` | 3,030,000.00 USD | 417.17 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.85` | 3,030,000.00 USD | 2,110.00 USD | 0.00 USD | `+4.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.95` | 3,040,000.00 USD | 1,080.00 USD | 0.00 USD | `+4.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 3,120,000.00 USD | 82,730.00 USD | 0.00 USD | `+4.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.15` | 3,140,000.00 USD | 17,480.00 USD | 0.00 USD | `+5.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.25` | 3,140,000.00 USD | 2,120.00 USD | 0.00 USD | `+5.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.35` | 3,140,000.00 USD | 4,580.00 USD | 0.00 USD | `+5.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.45` | 3,150,000.00 USD | 7,280.00 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.55` | 3,160,000.00 USD | 13,740.00 USD | 0.00 USD | `+5.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.65` | 3,430,000.00 USD | 266,350.00 USD | 0.00 USD | `+5.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.75` | 3,430,000.00 USD | 1,280.00 USD | 0.00 USD | `+5.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.85` | 3,430,000.00 USD | 2,480.00 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.95` | 3,440,000.00 USD | 4,280.00 USD | 0.00 USD | `+5.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 3,480,000.00 USD | 45,690.00 USD | 0.00 USD | `+6.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 3,490,000.00 USD | 3,180.00 USD | 0.00 USD | `+6.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.25` | 3,550,000.00 USD | 64,080.00 USD | 0.00 USD | `+6.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.35` | 3,560,000.00 USD | 4,260.00 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.45` | 3,560,000.00 USD | 3,860.00 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.55` | 3,580,000.00 USD | 20,580.00 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.65` | 3,600,000.00 USD | 17,250.00 USD | 0.00 USD | `+6.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.75` | 3,600,000.00 USD | 980.44 USD | 0.00 USD | `+6.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.85` | 3,820,000.00 USD | 226,740.00 USD | 0.00 USD | `+6.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.95` | 3,890,000.00 USD | 62,400.00 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.05` | 3,900,000.00 USD | 13,180.00 USD | 0.00 USD | `+7.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.15` | 3,900,000.00 USD | 1,180.00 USD | 0.00 USD | `+7.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.25` | 3,900,000.00 USD | 519.17 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.35` | 3,900,000.00 USD | 146.09 USD | 0.00 USD | `+7.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.45` | 4,000,000.00 USD | 95,950.00 USD | 0.00 USD | `+7.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.55` | 4,030,000.00 USD | 28,290.00 USD | 0.00 USD | `+7.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.65` | 4,030,000.00 USD | 230.23 USD | 0.00 USD | `+7.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.75` | 4,030,000.00 USD | 2,150.00 USD | 0.00 USD | `+7.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.85` | 4,030,000.00 USD | 5,900.00 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.95` | 4,060,000.00 USD | 25,930.00 USD | 0.00 USD | `+7.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.05` | 4,190,000.00 USD | 132,100.00 USD | 0.00 USD | `+8.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.15` | 4,220,000.00 USD | 28,780.00 USD | 0.00 USD | `+8.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.25` | 4,220,000.00 USD | 1,010.00 USD | 0.00 USD | `+8.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.35` | 4,220,000.00 USD | 1,090.00 USD | 0.00 USD | `+8.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.45` | 4,220,000.00 USD | 266.79 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.55` | 4,230,000.00 USD | 3,620.00 USD | 0.00 USD | `+8.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.65` | 4,230,000.00 USD | 1,970.00 USD | 0.00 USD | `+8.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.75` | 4,230,000.00 USD | 549.90 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.85` | 4,240,000.00 USD | 10,600.00 USD | 0.00 USD | `+8.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.95` | 4,240,000.00 USD | 206.60 USD | 0.00 USD | `+9.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.05` | 4,260,000.00 USD | 19,890.00 USD | 0.00 USD | `+9.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.15` | 4,270,000.00 USD | 7,900.00 USD | 0.00 USD | `+9.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.25` | 4,270,000.00 USD | 758.62 USD | 0.00 USD | `+9.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.35` | 4,280,000.00 USD | 7,980.00 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.45` | 4,300,000.00 USD | 26,170.00 USD | 0.00 USD | `+9.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.55` | 4,310,000.00 USD | 7,640.00 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.65` | 4,310,000.00 USD | 355.14 USD | 0.00 USD | `+9.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.75` | 4,420,000.00 USD | 110,390.00 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.85` | 4,420,000.00 USD | 1,400.00 USD | 0.00 USD | `+9.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.95` | 4,430,000.00 USD | 2,990.00 USD | 0.00 USD | `+10.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.05` | 4,570,000.00 USD | 142,930.00 USD | 0.00 USD | `+10.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.15` | 4,570,000.00 USD | 109.29 USD | 0.00 USD | `+10.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.25` | 4,590,000.00 USD | 20,190.00 USD | 0.00 USD | `+10.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.35` | 4,590,000.00 USD | 698.85 USD | 0.00 USD | `+10.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.45` | 4,600,000.00 USD | 8,930.00 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.55` | 4,650,000.00 USD | 52,130.00 USD | 0.00 USD | `+10.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.65` | 4,720,000.00 USD | 65,380.00 USD | 0.00 USD | `+10.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.75` | 4,720,000.00 USD | 536.60 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.85` | 4,730,000.00 USD | 11,350.00 USD | 0.00 USD | `+10.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.95` | 4,740,000.00 USD | 9,120.00 USD | 0.00 USD | `+11.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 4,830,000.00 USD | 89,330.00 USD | 0.00 USD | `+11.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.15` | 4,900,000.00 USD | 68,190.00 USD | 0.00 USD | `+11.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.35` | 4,900,000.00 USD | 7,140.00 USD | 0.00 USD | `+11.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.45` | 4,900,000.00 USD | 2,580.00 USD | 0.00 USD | `+11.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.55` | 4,910,000.00 USD | 5,430.00 USD | 0.00 USD | `+11.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.65` | 4,910,000.00 USD | 666.02 USD | 0.00 USD | `+11.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.75` | 4,910,000.00 USD | 1,030.00 USD | 0.00 USD | `+11.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.85` | 4,910,000.00 USD | 1,430.00 USD | 0.00 USD | `+11.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.95` | 4,950,000.00 USD | 40,920.00 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 5,030,000.00 USD | 73,460.00 USD | 0.00 USD | `+12.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.15` | 5,040,000.00 USD | 7,660.00 USD | 0.00 USD | `+12.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.25` | 8,980,000.00 USD | 3,950,000.00 USD | 0.00 USD | `+12.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.35` | 9,010,000.00 USD | 31,070.00 USD | 0.00 USD | `+12.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.45` | 9,020,000.00 USD | 5,880.00 USD | 0.00 USD | `+12.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.55` | 9,020,000.00 USD | 1,070.00 USD | 0.00 USD | `+12.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.65` | 9,020,000.00 USD | 5,040.00 USD | 0.00 USD | `+12.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.75` | 9,030,000.00 USD | 1,370.00 USD | 0.00 USD | `+12.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.85` | 9,030,000.00 USD | 1,430.00 USD | 0.00 USD | `+13.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.95` | 9,030,000.00 USD | 357.34 USD | 0.00 USD | `+13.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.05` | 9,550,000.00 USD | 522,250.00 USD | 0.00 USD | `+13.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.15` | 9,550,000.00 USD | 4,150.00 USD | 0.00 USD | `+13.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.25` | 9,550,000.00 USD | 102.53 USD | 0.00 USD | `+13.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.35` | 9,560,000.00 USD | 1,610.00 USD | 0.00 USD | `+13.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.45` | 9,560,000.00 USD | 1,580.00 USD | 0.00 USD | `+13.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.55` | 9,570,000.00 USD | 10,280.00 USD | 0.00 USD | `+13.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.65` | 9,570,000.00 USD | 3,030.00 USD | 0.00 USD | `+13.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.85` | 9,590,000.00 USD | 17,740.00 USD | 0.00 USD | `+14.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.95` | 9,660,000.00 USD | 74,410.00 USD | 0.00 USD | `+14.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 9,730,000.00 USD | 64,770.00 USD | 0.00 USD | `+14.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.15` | 9,730,000.00 USD | 1,300.00 USD | 0.00 USD | `+14.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.25` | 9,740,000.00 USD | 5,910.00 USD | 0.00 USD | `+14.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.45` | 9,740,000.00 USD | 585.11 USD | 0.00 USD | `+14.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.55` | 9,740,000.00 USD | 852.24 USD | 0.00 USD | `+14.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.65` | 9,760,000.00 USD | 22,910.00 USD | 0.00 USD | `+14.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.75` | 9,760,000.00 USD | 2,420.00 USD | 0.00 USD | `+14.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.85` | 9,760,000.00 USD | 2,330.00 USD | 0.00 USD | `+15.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.05` | 9,780,000.00 USD | 14,190.00 USD | 0.00 USD | `+15.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.15` | 9,830,000.00 USD | 49,680.00 USD | 0.00 USD | `+15.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.25` | 9,830,000.00 USD | 5,260.00 USD | 0.00 USD | `+15.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.35` | 9,840,000.00 USD | 6,270.00 USD | 0.00 USD | `+15.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.45` | 9,840,000.00 USD | 843.38 USD | 0.00 USD | `+15.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.55` | 9,880,000.00 USD | 36,280.00 USD | 0.00 USD | `+15.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.65` | 9,880,000.00 USD | 6,150.00 USD | 0.00 USD | `+15.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.85` | 9,880,000.00 USD | 586.82 USD | 0.00 USD | `+16.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.05` | 9,960,000.00 USD | 78,560.00 USD | 0.00 USD | `+16.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.25` | 9,960,000.00 USD | 473.38 USD | 0.00 USD | `+16.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.35` | 10,000,000.00 USD | 35,250.00 USD | 0.00 USD | `+16.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.45` | 10,000,000.00 USD | 655.74 USD | 0.00 USD | `+16.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.55` | 10,000,000.00 USD | 4,470.00 USD | 0.00 USD | `+16.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.65` | 10,000,000.00 USD | 230.71 USD | 0.00 USD | `+16.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.75` | 10,000,000.00 USD | 257.07 USD | 0.00 USD | `+17.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.85` | 10,010,000.00 USD | 4,540.00 USD | 0.00 USD | `+17.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.05` | 10,010,000.00 USD | 1,970.00 USD | 0.00 USD | `+17.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.15` | 10,010,000.00 USD | 122.14 USD | 0.00 USD | `+17.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.25` | 10,010,000.00 USD | 907.14 USD | 0.00 USD | `+17.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.35` | 10,010,000.00 USD | 740.99 USD | 0.00 USD | `+17.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.45` | 10,010,000.00 USD | 343.35 USD | 0.00 USD | `+17.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.55` | 10,010,000.00 USD | 1,640.00 USD | 0.00 USD | `+17.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.65` | 10,010,000.00 USD | 105.48 USD | 0.00 USD | `+17.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.75` | 10,010,000.00 USD | 1,010.00 USD | 0.00 USD | `+18.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.95` | 10,020,000.00 USD | 2,520.00 USD | 0.00 USD | `+18.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.05` | 10,100,000.00 USD | 81,890.00 USD | 0.00 USD | `+18.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.35` | 10,100,000.00 USD | 309.14 USD | 0.00 USD | `+18.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.45` | 10,100,000.00 USD | 346.35 USD | 0.00 USD | `+18.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.55` | 10,100,000.00 USD | 2,440.00 USD | 0.00 USD | `+18.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.75` | 10,100,000.00 USD | 121.54 USD | 0.00 USD | `+19.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.85` | 10,100,000.00 USD | 579.25 USD | 0.00 USD | `+19.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.05` | 10,110,000.00 USD | 6,400.00 USD | 0.00 USD | `+19.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.15` | 10,110,000.00 USD | 1,740.00 USD | 0.00 USD | `+19.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.25` | 10,110,000.00 USD | 1,920.00 USD | 0.00 USD | `+19.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.45` | 10,120,000.00 USD | 2,870.00 USD | 0.00 USD | `+19.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.55` | 10,130,000.00 USD | 14,010.00 USD | 0.00 USD | `+19.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.65` | 10,140,000.00 USD | 6,000.00 USD | 0.00 USD | `+20.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.75` | 10,140,000.00 USD | 3,580.00 USD | 0.00 USD | `+20.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.85` | 10,140,000.00 USD | 234.87 USD | 0.00 USD | `+20.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.95` | 10,150,000.00 USD | 12,860.00 USD | 0.00 USD | `+20.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.05` | 10,160,000.00 USD | 4,200.00 USD | 0.00 USD | `+20.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.15` | 10,160,000.00 USD | 584.58 USD | 0.00 USD | `+20.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.25` | 10,160,000.00 USD | 1,740.00 USD | 0.00 USD | `+20.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.35` | 10,160,000.00 USD | 2,330.00 USD | 0.00 USD | `+20.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.45` | 10,280,000.00 USD | 118,690.00 USD | 0.00 USD | `+20.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.65` | 10,390,000.00 USD | 106,330.00 USD | 0.00 USD | `+21.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.75` | 10,390,000.00 USD | 5,920.00 USD | 0.00 USD | `+21.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.85` | 10,450,000.00 USD | 55,580.00 USD | 0.00 USD | `+21.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.05` | 10,520,000.00 USD | 69,220.00 USD | 0.00 USD | `+21.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.15` | 10,520,000.00 USD | 3,980.00 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.25` | 10,530,000.00 USD | 4,460.00 USD | 0.00 USD | `+21.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.35` | 10,530,000.00 USD | 127.82 USD | 0.00 USD | `+21.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.45` | 10,530,000.00 USD | 707.15 USD | 0.00 USD | `+21.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.55` | 10,530,000.00 USD | 1,260.00 USD | 0.00 USD | `+21.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.65` | 10,530,000.00 USD | 2,970.00 USD | 0.00 USD | `+22.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.75` | 10,530,000.00 USD | 403.75 USD | 0.00 USD | `+22.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.85` | 10,550,000.00 USD | 15,940.00 USD | 0.00 USD | `+22.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.95` | 10,590,000.00 USD | 42,290.00 USD | 0.00 USD | `+22.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.05` | 10,640,000.00 USD | 52,430.00 USD | 0.00 USD | `+22.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.15` | 10,660,000.00 USD | 15,130.00 USD | 0.00 USD | `+22.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.25` | 10,660,000.00 USD | 1,850.00 USD | 0.00 USD | `+22.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.35` | 10,660,000.00 USD | 4,150.00 USD | 0.00 USD | `+22.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.45` | 10,660,000.00 USD | 310.57 USD | 0.00 USD | `+22.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.65` | 10,660,000.00 USD | 615.00 USD | 0.00 USD | `+23.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.75` | 10,790,000.00 USD | 125,500.00 USD | 0.00 USD | `+23.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.85` | 10,830,000.00 USD | 37,630.00 USD | 0.00 USD | `+23.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.95` | 10,830,000.00 USD | 458.21 USD | 0.00 USD | `+23.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.05` | 11,010,000.00 USD | 181,410.00 USD | 0.00 USD | `+23.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.15` | 11,010,000.00 USD | 414.52 USD | 0.00 USD | `+23.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.25` | 11,010,000.00 USD | 3,210.00 USD | 0.00 USD | `+23.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.35` | 11,020,000.00 USD | 7,850.00 USD | 0.00 USD | `+23.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.45` | 11,030,000.00 USD | 13,560.00 USD | 0.00 USD | `+23.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.55` | 11,030,000.00 USD | 904.13 USD | 0.00 USD | `+24.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.65` | 11,030,000.00 USD | 191.83 USD | 0.00 USD | `+24.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.75` | 11,040,000.00 USD | 2,150.00 USD | 0.00 USD | `+24.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.85` | 11,040,000.00 USD | 663.47 USD | 0.00 USD | `+24.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.05` | 11,060,000.00 USD | 20,960.00 USD | 0.00 USD | `+24.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.15` | 11,060,000.00 USD | 122.36 USD | 0.00 USD | `+24.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.25` | 11,070,000.00 USD | 11,200.00 USD | 0.00 USD | `+24.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.45` | 11,080,000.00 USD | 11,570.00 USD | 0.00 USD | `+24.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.55` | 11,090,000.00 USD | 7,860.00 USD | 0.00 USD | `+25.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.65` | 11,090,000.00 USD | 2,070.00 USD | 0.00 USD | `+25.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.75` | 11,090,000.00 USD | 2,450.00 USD | 0.00 USD | `+25.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.85` | 11,100,000.00 USD | 1,480.00 USD | 0.00 USD | `+25.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.95` | 11,180,000.00 USD | 80,260.00 USD | 0.00 USD | `+25.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.05` | 11,370,000.00 USD | 192,930.00 USD | 0.00 USD | `+25.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.15` | 11,370,000.00 USD | 1,000.00 USD | 0.00 USD | `+25.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.25` | 11,600,000.00 USD | 234,430.00 USD | 0.00 USD | `+25.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.35` | 11,660,000.00 USD | 52,330.00 USD | 0.00 USD | `+25.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.45` | 11,660,000.00 USD | 3,060.00 USD | 0.00 USD | `+25.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.55` | 11,670,000.00 USD | 14,830.00 USD | 0.00 USD | `+26.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.65` | 11,690,000.00 USD | 11,000.00 USD | 0.00 USD | `+26.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.75` | 11,690,000.00 USD | 104.34 USD | 0.00 USD | `+26.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.85` | 11,690,000.00 USD | 3,850.00 USD | 0.00 USD | `+26.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.95` | 11,710,000.00 USD | 16,430.00 USD | 0.00 USD | `+26.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.05` | 12,720,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+26.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.15` | 12,720,000.00 USD | 252.46 USD | 0.00 USD | `+26.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.25` | 12,720,000.00 USD | 7,710.00 USD | 0.00 USD | `+26.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.35` | 12,730,000.00 USD | 6,790.00 USD | 0.00 USD | `+26.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.45` | 12,730,000.00 USD | 2,670.00 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.55` | 12,730,000.00 USD | 632.58 USD | 0.00 USD | `+27.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.65` | 12,750,000.00 USD | 11,550.00 USD | 0.00 USD | `+27.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.85` | 12,750,000.00 USD | 5,530.00 USD | 0.00 USD | `+27.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.95` | 12,770,000.00 USD | 18,470.00 USD | 0.00 USD | `+27.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.05` | 12,790,000.00 USD | 16,360.00 USD | 0.00 USD | `+27.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.15` | 12,790,000.00 USD | 1,320.00 USD | 0.00 USD | `+27.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.25` | 12,790,000.00 USD | 151.59 USD | 0.00 USD | `+27.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.35` | 12,790,000.00 USD | 4,240.00 USD | 0.00 USD | `+27.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.45` | 12,790,000.00 USD | 1,370.00 USD | 0.00 USD | `+28.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.55` | 12,800,000.00 USD | 7,330.00 USD | 0.00 USD | `+28.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.65` | 12,810,000.00 USD | 6,610.00 USD | 0.00 USD | `+28.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.85` | 12,810,000.00 USD | 596.78 USD | 0.00 USD | `+28.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.95` | 12,820,000.00 USD | 10,310.00 USD | 0.00 USD | `+28.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.05` | 13,370,000.00 USD | 554,250.00 USD | 0.00 USD | `+28.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.15` | 13,370,000.00 USD | 603.22 USD | 0.00 USD | `+28.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.25` | 13,370,000.00 USD | 311.87 USD | 0.00 USD | `+28.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.35` | 13,380,000.00 USD | 6,780.00 USD | 0.00 USD | `+28.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.45` | 13,380,000.00 USD | 993.56 USD | 0.00 USD | `+29.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.55` | 13,400,000.00 USD | 16,280.00 USD | 0.00 USD | `+29.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.85` | 13,400,000.00 USD | 471.94 USD | 0.00 USD | `+29.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.95` | 13,400,000.00 USD | 209.08 USD | 0.00 USD | `+29.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.05` | 13,550,000.00 USD | 151,060.00 USD | 0.00 USD | `+29.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.15` | 13,550,000.00 USD | 189.23 USD | 0.00 USD | `+29.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.45` | 13,550,000.00 USD | 187.15 USD | 0.00 USD | `+30.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.65` | 13,550,000.00 USD | 3,550.00 USD | 0.00 USD | `+30.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.75` | 13,560,000.00 USD | 7,460.00 USD | 0.00 USD | `+30.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.05` | 13,750,000.00 USD | 190,580.00 USD | 0.00 USD | `+30.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.35` | 13,750,000.00 USD | 534.87 USD | 0.00 USD | `+31.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.45` | 13,760,000.00 USD | 4,620.00 USD | 0.00 USD | `+31.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.65` | 13,760,000.00 USD | 5,000.00 USD | 0.00 USD | `+31.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.75` | 13,760,000.00 USD | 362.81 USD | 0.00 USD | `+31.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.85` | 13,820,000.00 USD | 60,770.00 USD | 0.00 USD | `+31.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.95` | 13,820,000.00 USD | 482.37 USD | 0.00 USD | `+31.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.05` | 13,830,000.00 USD | 3,700.00 USD | 0.00 USD | `+31.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.15` | 13,830,000.00 USD | 3,010.00 USD | 0.00 USD | `+31.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.25` | 13,830,000.00 USD | 191.09 USD | 0.00 USD | `+31.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.65` | 13,870,000.00 USD | 41,130.00 USD | 0.00 USD | `+32.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.95` | 13,880,000.00 USD | 12,600.00 USD | 0.00 USD | `+32.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.05` | 13,930,000.00 USD | 50,720.00 USD | 0.00 USD | `+32.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.15` | 13,930,000.00 USD | 229.89 USD | 0.00 USD | `+32.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.25` | 13,950,000.00 USD | 15,330.00 USD | 0.00 USD | `+32.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.45` | 13,950,000.00 USD | 401.29 USD | 0.00 USD | `+33.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.55` | 13,950,000.00 USD | 1,320.00 USD | 0.00 USD | `+33.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.65` | 13,950,000.00 USD | 152.99 USD | 0.00 USD | `+33.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.75` | 13,950,000.00 USD | 153.10 USD | 0.00 USD | `+33.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.85` | 13,950,000.00 USD | 116.87 USD | 0.00 USD | `+33.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.05` | 14,000,000.00 USD | 51,520.00 USD | 0.00 USD | `+33.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.35` | 14,000,000.00 USD | 1,760.00 USD | 0.00 USD | `+34.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.45` | 14,010,000.00 USD | 4,090.00 USD | 0.00 USD | `+34.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.65` | 14,010,000.00 USD | 192.06 USD | 0.00 USD | `+34.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.75` | 14,010,000.00 USD | 3,150.00 USD | 0.00 USD | `+34.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.85` | 14,010,000.00 USD | 2,620.00 USD | 0.00 USD | `+34.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.95` | 14,020,000.00 USD | 10,140.00 USD | 0.00 USD | `+34.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.05` | 14,030,000.00 USD | 6,000.00 USD | 0.00 USD | `+34.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.15` | 14,040,000.00 USD | 5,950.00 USD | 0.00 USD | `+34.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.25` | 14,050,000.00 USD | 8,820.00 USD | 0.00 USD | `+35.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.45` | 14,050,000.00 USD | 135.39 USD | 0.00 USD | `+35.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.65` | 14,210,000.00 USD | 160,920.00 USD | 0.00 USD | `+35.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.75` | 14,210,000.00 USD | 144.93 USD | 0.00 USD | `+35.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.05` | 14,220,000.00 USD | 12,390.00 USD | 0.00 USD | `+35.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.65` | 14,220,000.00 USD | 397.95 USD | 0.00 USD | `+36.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.85` | 14,230,000.00 USD | 9,310.00 USD | 0.00 USD | `+36.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.95` | 14,230,000.00 USD | 3,910.00 USD | 0.00 USD | `+36.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.05` | 14,230,000.00 USD | 267.43 USD | 0.00 USD | `+36.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.15` | 14,230,000.00 USD | 509.96 USD | 0.00 USD | `+36.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.25` | 14,230,000.00 USD | 191.88 USD | 0.00 USD | `+37.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.35` | 14,230,000.00 USD | 237.36 USD | 0.00 USD | `+37.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.55` | 14,240,000.00 USD | 1,210.00 USD | 0.00 USD | `+37.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.65` | 14,240,000.00 USD | 192.46 USD | 0.00 USD | `+37.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.75` | 14,240,000.00 USD | 112.35 USD | 0.00 USD | `+37.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.95` | 14,240,000.00 USD | 4,620.00 USD | 0.00 USD | `+37.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.05` | 14,290,000.00 USD | 54,080.00 USD | 0.00 USD | `+37.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.25` | 14,290,000.00 USD | 331.60 USD | 0.00 USD | `+38.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.55` | 14,560,000.00 USD | 270,270.00 USD | 0.00 USD | `+38.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.85` | 14,570,000.00 USD | 647.28 USD | 0.00 USD | `+38.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.05` | 14,680,000.00 USD | 116,220.00 USD | 0.00 USD | `+38.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.55` | 14,690,000.00 USD | 7,560.00 USD | 0.00 USD | `+39.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.05` | 14,690,000.00 USD | 1,890.00 USD | 0.00 USD | `+39.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.35` | 14,690,000.00 USD | 192.25 USD | 0.00 USD | `+40.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.45` | 14,690,000.00 USD | 465.29 USD | 0.00 USD | `+40.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.55` | 14,690,000.00 USD | 389.17 USD | 0.00 USD | `+40.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.85` | 14,690,000.00 USD | 826.57 USD | 0.00 USD | `+40.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.05` | 14,690,000.00 USD | 231.61 USD | 0.00 USD | `+41.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.25` | 14,700,000.00 USD | 2,910.00 USD | 0.00 USD | `+41.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.35` | 14,700,000.00 USD | 3,920.00 USD | 0.00 USD | `+41.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.65` | 14,730,000.00 USD | 26,260.00 USD | 0.00 USD | `+41.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.75` | 14,730,000.00 USD | 133.62 USD | 0.00 USD | `+41.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.05` | 14,740,000.00 USD | 14,550.00 USD | 0.00 USD | `+42.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.45` | 14,740,000.00 USD | 692.25 USD | 0.00 USD | `+42.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.65` | 14,740,000.00 USD | 406.24 USD | 0.00 USD | `+42.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.85` | 21,490,000.00 USD | 6,740,000.00 USD | 0.00 USD | `+42.85%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `138.95` | 21,490,000.00 USD | 826.75 USD | 0.00 USD | `+42.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.05` | 23,680,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+43.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.55` | 23,680,000.00 USD | 5,920.00 USD | 0.00 USD | `+43.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.05` | 23,790,000.00 USD | 110,660.00 USD | 0.00 USD | `+44.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.45` | 23,810,000.00 USD | 12,120.00 USD | 0.00 USD | `+44.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.55` | 23,900,000.00 USD | 98,400.00 USD | 0.00 USD | `+44.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.75` | 23,910,000.00 USD | 990.88 USD | 0.00 USD | `+44.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.05` | 23,920,000.00 USD | 11,640.00 USD | 0.00 USD | `+45.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.25` | 23,920,000.00 USD | 6,190.00 USD | 0.00 USD | `+45.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.65` | 23,920,000.00 USD | 796.07 USD | 0.00 USD | `+45.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.05` | 23,930,000.00 USD | 826.73 USD | 0.00 USD | `+46.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.85` | 23,930,000.00 USD | 278.56 USD | 0.00 USD | `+46.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.95` | 24,250,000.00 USD | 329,100.00 USD | 0.00 USD | `+47.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.05` | 24,330,000.00 USD | 72,610.00 USD | 0.00 USD | `+47.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.15` | 24,340,000.00 USD | 16,980.00 USD | 0.00 USD | `+47.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.35` | 24,340,000.00 USD | 528.96 USD | 0.00 USD | `+47.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.05` | 24,350,000.00 USD | 6,330.00 USD | 0.00 USD | `+48.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.25` | 24,350,000.00 USD | 415.44 USD | 0.00 USD | `+48.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.35` | 24,630,000.00 USD | 282,520.00 USD | 0.00 USD | `+48.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.55` | 24,640,000.00 USD | 7,260.00 USD | 0.00 USD | `+48.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.75` | 24,640,000.00 USD | 791.78 USD | 0.00 USD | `+48.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.05` | 24,680,000.00 USD | 36,040.00 USD | 0.00 USD | `+49.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.25` | 24,680,000.00 USD | 209.16 USD | 0.00 USD | `+49.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.55` | 24,680,000.00 USD | 698.64 USD | 0.00 USD | `+49.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.05` | 24,870,000.00 USD | 190,100.00 USD | 0.00 USD | `+50.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.15` | 24,870,000.00 USD | 3,300.00 USD | 0.00 USD | `+50.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.25` | 24,870,000.00 USD | 1,020.00 USD | 0.00 USD | `+50.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.95` | 24,870,000.00 USD | 1,500.00 USD | 0.00 USD | `+51.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.05` | 24,910,000.00 USD | 37,700.00 USD | 0.00 USD | `+51.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.45` | 24,910,000.00 USD | 844.89 USD | 0.00 USD | `+51.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.85` | 24,920,000.00 USD | 4,610.00 USD | 0.00 USD | `+52.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.95` | 24,920,000.00 USD | 3,100.00 USD | 0.00 USD | `+52.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.05` | 26,260,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+52.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.45` | 26,260,000.00 USD | 1,370.00 USD | 0.00 USD | `+52.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.55` | 26,270,000.00 USD | 4,760.00 USD | 0.00 USD | `+52.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.05` | 26,270,000.00 USD | 549.99 USD | 0.00 USD | `+53.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.15` | 26,780,000.00 USD | 510,120.00 USD | 0.00 USD | `+53.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.05` | 27,030,000.00 USD | 249,190.00 USD | 0.00 USD | `+54.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.25` | 27,030,000.00 USD | 1,200.00 USD | 0.00 USD | `+54.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.35` | 27,030,000.00 USD | 178.92 USD | 0.00 USD | `+54.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.55` | 27,030,000.00 USD | 1,360.00 USD | 0.00 USD | `+54.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.05` | 27,040,000.00 USD | 14,430.00 USD | 0.00 USD | `+55.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.25` | 27,050,000.00 USD | 2,000.00 USD | 0.00 USD | `+55.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.45` | 27,050,000.00 USD | 411.94 USD | 0.00 USD | `+55.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.15` | 27,060,000.00 USD | 10,620.00 USD | 0.00 USD | `+57.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.65` | 27,060,000.00 USD | 1,020.00 USD | 0.00 USD | `+58.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.55` | 27,070,000.00 USD | 12,000.00 USD | 0.00 USD | `+59.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.85` | 27,070,000.00 USD | 113.04 USD | 0.00 USD | `+59.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.05` | 27,070,000.00 USD | 1,830.00 USD | 0.00 USD | `+59.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.35` | 27,090,000.00 USD | 22,680.00 USD | 0.00 USD | `+59.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.85` | 27,110,000.00 USD | 16,970.00 USD | 0.00 USD | `+60.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.05` | 27,110,000.00 USD | 2,230.00 USD | 0.00 USD | `+60.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.05` | 27,120,000.00 USD | 6,640.00 USD | 0.00 USD | `+62.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.75` | 27,140,000.00 USD | 15,880.00 USD | 0.00 USD | `+63.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.15` | 27,140,000.00 USD | 692.30 USD | 0.00 USD | `+63.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.95` | 27,140,000.00 USD | 5,620.00 USD | 0.00 USD | `+64.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.05` | 27,230,000.00 USD | 89,040.00 USD | 0.00 USD | `+64.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.05` | 27,230,000.00 USD | 281.84 USD | 0.00 USD | `+65.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.05` | 27,240,000.00 USD | 4,080.00 USD | 0.00 USD | `+67.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.05` | 27,320,000.00 USD | 89,230.00 USD | 0.00 USD | `+69.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.45` | 27,330,000.00 USD | 823.94 USD | 0.00 USD | `+70.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.45` | 27,330,000.00 USD | 211.39 USD | 0.00 USD | `+71.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.95` | 27,330,000.00 USD | 307.19 USD | 0.00 USD | `+71.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.05` | 27,330,000.00 USD | 593.03 USD | 0.00 USD | `+71.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.75` | 27,330,000.00 USD | 1,440.00 USD | 0.00 USD | `+72.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.05` | 27,330,000.00 USD | 5,720.00 USD | 0.00 USD | `+72.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.55` | 27,330,000.00 USD | 495.09 USD | 0.00 USD | `+74.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.95` | 27,330,000.00 USD | 912.63 USD | 0.00 USD | `+74.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.05` | 27,380,000.00 USD | 43,480.00 USD | 0.00 USD | `+74.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.55` | 27,380,000.00 USD | 686.20 USD | 0.00 USD | `+76.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.05` | 27,410,000.00 USD | 35,280.00 USD | 0.00 USD | `+77.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.45` | 27,410,000.00 USD | 703.60 USD | 0.00 USD | `+77.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.05` | 27,420,000.00 USD | 3,160.00 USD | 0.00 USD | `+78.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `174.85` | 27,420,000.00 USD | 1,430.00 USD | 0.00 USD | `+79.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.05` | 27,470,000.00 USD | 52,520.00 USD | 0.00 USD | `+80.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.25` | 27,490,000.00 USD | 21,960.00 USD | 0.00 USD | `+80.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.85` | 27,500,000.00 USD | 1,450.00 USD | 0.00 USD | `+81.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.05` | 27,500,000.00 USD | 885.25 USD | 0.00 USD | `+82.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.55` | 27,500,000.00 USD | 2,990.00 USD | 0.00 USD | `+83.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.15` | 27,500,000.00 USD | 261.56 USD | 0.00 USD | `+84.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.05` | 27,580,000.00 USD | 80,290.00 USD | 0.00 USD | `+85.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.05` | 27,580,000.00 USD | 2,440.00 USD | 0.00 USD | `+86.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.95` | 27,580,000.00 USD | 349.34 USD | 0.00 USD | `+87.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.45` | 27,600,000.00 USD | 19,620.00 USD | 0.00 USD | `+87.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.45` | 28,150,000.00 USD | 550,350.00 USD | 0.00 USD | `+88.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.05` | 28,180,000.00 USD | 29,610.00 USD | 0.00 USD | `+90.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.05` | 28,350,000.00 USD | 165,580.00 USD | 0.00 USD | `+92.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.05` | 28,490,000.00 USD | 141,190.00 USD | 0.00 USD | `+93.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.05` | 28,520,000.00 USD | 35,880.00 USD | 0.00 USD | `+95.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.35` | 28,530,000.00 USD | 744.27 USD | 0.00 USD | `+95.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.65` | 28,530,000.00 USD | 7,750.00 USD | 0.00 USD | `+96.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `194.05` | 28,540,000.00 USD | 4,270.00 USD | 0.00 USD | `+99.64%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `82.60` | 171,490,000.00 USD | 0.00 USD | 171,490,000.00 USD | 53,130.00 USD | 56,870.00 USD | 141,300.00 USD |
| `7D` | `82.80` | 171,240,000.00 USD | 0.00 USD | 171,240,000.00 USD | 1,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `83.00` | 171,230,000.00 USD | 0.00 USD | 171,230,000.00 USD | 1,690.00 USD | 2,080.00 USD | 0.00 USD |
| `7D` | `83.20` | 171,230,000.00 USD | 0.00 USD | 171,230,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD |
| `7D` | `83.40` | 171,190,000.00 USD | 0.00 USD | 171,190,000.00 USD | 0.00 USD | 0.00 USD | 579.46 USD |
| `7D` | `83.60` | 171,190,000.00 USD | 0.00 USD | 171,190,000.00 USD | 0.00 USD | 0.00 USD | 86,160.00 USD |
| `7D` | `83.80` | 171,100,000.00 USD | 0.00 USD | 171,100,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD |
| `7D` | `84.20` | 171,090,000.00 USD | 0.00 USD | 171,090,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD |
| `7D` | `84.40` | 171,070,000.00 USD | 0.00 USD | 171,070,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD |
| `7D` | `85.20` | 171,040,000.00 USD | 0.00 USD | 171,040,000.00 USD | 0.00 USD | 218,580.00 USD | 0.00 USD |
| `7D` | `85.40` | 170,830,000.00 USD | 0.00 USD | 170,830,000.00 USD | 0.00 USD | 12,950.00 USD | 192,310.00 USD |
| `7D` | `85.60` | 170,620,000.00 USD | 0.00 USD | 170,620,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD |
| `7D` | `85.80` | 170,430,000.00 USD | 0.00 USD | 170,430,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD |
| `7D` | `86.20` | 170,170,000.00 USD | 0.00 USD | 170,170,000.00 USD | 0.00 USD | 12,130.00 USD | 199,350.00 USD |
| `7D` | `86.40` | 169,960,000.00 USD | 0.00 USD | 169,960,000.00 USD | 0.00 USD | 311,220.00 USD | 4,340.00 USD |
| `7D` | `86.80` | 169,640,000.00 USD | 0.00 USD | 169,640,000.00 USD | 0.00 USD | 149,840.00 USD | 0.00 USD |
| `7D` | `87.00` | 169,490,000.00 USD | 0.00 USD | 169,490,000.00 USD | 263,340.00 USD | 176,600.00 USD | 297,340.00 USD |
| `1D` | `87.20` | 174,240,000.00 USD | 0.00 USD | 174,240,000.00 USD | 129,420.00 USD | 138,340.00 USD | 351,900.00 USD |
| `7D` | `87.20` | 168,760,000.00 USD | 0.00 USD | 168,760,000.00 USD | 8,850.00 USD | 0.00 USD | 6,820.00 USD |
| `1D` | `87.40` | 173,620,000.00 USD | 0.00 USD | 173,620,000.00 USD | 30,080.00 USD | 232,930.00 USD | 109,500.00 USD |
| `7D` | `87.40` | 168,740,000.00 USD | 0.00 USD | 168,740,000.00 USD | 248,310.00 USD | 217,060.00 USD | 288,100.00 USD |
| `1D` | `87.60` | 173,250,000.00 USD | 0.00 USD | 173,250,000.00 USD | 105,350.00 USD | 295,330.00 USD | 57,210.00 USD |
| `7D` | `87.60` | 167,990,000.00 USD | 0.00 USD | 167,990,000.00 USD | 0.00 USD | 275,130.00 USD | 421,310.00 USD |
| `1D` | `87.80` | 172,790,000.00 USD | 0.00 USD | 172,790,000.00 USD | 90,150.00 USD | 276,230.00 USD | 716,950.00 USD |
| `7D` | `87.80` | 167,290,000.00 USD | 0.00 USD | 167,290,000.00 USD | 0.00 USD | 413,150.00 USD | 11,130.00 USD |
| `1D` | `88.00` | 171,710,000.00 USD | 0.00 USD | 171,710,000.00 USD | 47,860.00 USD | 202,660.00 USD | 485,910.00 USD |
| `7D` | `88.00` | 166,870,000.00 USD | 0.00 USD | 166,870,000.00 USD | 0.00 USD | 12,070.00 USD | 251,100.00 USD |
| `1D` | `88.20` | 170,970,000.00 USD | 0.00 USD | 170,970,000.00 USD | 140,490.00 USD | 168,390.00 USD | 365,710.00 USD |
| `7D` | `88.20` | 166,600,000.00 USD | 0.00 USD | 166,600,000.00 USD | 9,900.00 USD | 20,610.00 USD | 28,240.00 USD |
| `1D` | `88.40` | 170,300,000.00 USD | 0.00 USD | 170,300,000.00 USD | 84,680.00 USD | 178,840.00 USD | 65,030.00 USD |
| `7D` | `88.40` | 166,540,000.00 USD | 0.00 USD | 166,540,000.00 USD | 0.00 USD | 237,870.00 USD | 335,390.00 USD |
| `1D` | `88.60` | 169,970,000.00 USD | 0.00 USD | 169,970,000.00 USD | 68,370.00 USD | 64,340.00 USD | 0.00 USD |
| `1D` | `88.80` | 169,840,000.00 USD | 0.00 USD | 169,840,000.00 USD | 304,990.00 USD | 175,710.00 USD | 415,440.00 USD |
| `7D` | `88.80` | 165,970,000.00 USD | 0.00 USD | 165,970,000.00 USD | 241,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `89.00` | 168,940,000.00 USD | 0.00 USD | 168,940,000.00 USD | 8,600.00 USD | 11,540.00 USD | 227,790.00 USD |
| `7D` | `89.00` | 165,730,000.00 USD | 0.00 USD | 165,730,000.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD |
| `1D` | `89.20` | 168,690,000.00 USD | 0.00 USD | 168,690,000.00 USD | 377,030.00 USD | 119,090.00 USD | 11,970.00 USD |
| `7D` | `89.20` | 164,800,000.00 USD | 0.00 USD | 164,800,000.00 USD | 8,180.00 USD | 10,750.00 USD | 315,450.00 USD |
| `1D` | `89.40` | 168,180,000.00 USD | 0.00 USD | 168,180,000.00 USD | 5,150.00 USD | 292,120.00 USD | 274,990.00 USD |
| `7D` | `89.40` | 164,460,000.00 USD | 0.00 USD | 164,460,000.00 USD | 697,470.00 USD | 26,220.00 USD | 160,460.00 USD |
| `1D` | `89.60` | 167,610,000.00 USD | 0.00 USD | 167,610,000.00 USD | 138,450.00 USD | 5,250.00 USD | 135,260.00 USD |
| `7D` | `89.60` | 163,580,000.00 USD | 0.00 USD | 163,580,000.00 USD | 684,220.00 USD | 270,260.00 USD | 723,370.00 USD |
| `1D` | `89.80` | 167,330,000.00 USD | 0.00 USD | 167,330,000.00 USD | 54,220.00 USD | 91,280.00 USD | 440,250.00 USD |
| `7D` | `89.80` | 161,900,000.00 USD | 0.00 USD | 161,900,000.00 USD | 425,950.00 USD | 318,390.00 USD | 314,310.00 USD |
| `1D` | `90.00` | 166,750,000.00 USD | 0.00 USD | 166,750,000.00 USD | 686,700.00 USD | 302,220.00 USD | 278,530.00 USD |
| `7D` | `90.00` | 160,840,000.00 USD | 0.00 USD | 160,840,000.00 USD | 374,600.00 USD | 647,410.00 USD | 1,090,000.00 USD |
| `1D` | `90.20` | 165,480,000.00 USD | 0.00 USD | 165,480,000.00 USD | 822,890.00 USD | 930,230.00 USD | 363,600.00 USD |
| `7D` | `90.20` | 158,720,000.00 USD | 0.00 USD | 158,720,000.00 USD | 1,250,000.00 USD | 590,390.00 USD | 735,310.00 USD |
| `1D` | `90.40` | 163,360,000.00 USD | 0.00 USD | 163,360,000.00 USD | 779,410.00 USD | 544,380.00 USD | 671,130.00 USD |
| `7D` | `90.40` | 156,140,000.00 USD | 0.00 USD | 156,140,000.00 USD | 796,240.00 USD | 68,740.00 USD | 694,770.00 USD |
| `1D` | `90.60` | 161,370,000.00 USD | 0.00 USD | 161,370,000.00 USD | 676,760.00 USD | 671,710.00 USD | 840,150.00 USD |
| `7D` | `90.60` | 154,580,000.00 USD | 0.00 USD | 154,580,000.00 USD | 1,040,000.00 USD | 1,010,000.00 USD | 1,560,000.00 USD |
| `1D` | `90.80` | 159,180,000.00 USD | 0.00 USD | 159,180,000.00 USD | 404,570.00 USD | 518,670.00 USD | 250,200.00 USD |
| `7D` | `90.80` | 150,970,000.00 USD | 0.00 USD | 150,970,000.00 USD | 1,210,000.00 USD | 1,200,000.00 USD | 1,480,000.00 USD |
| `1D` | `91.00` | 158,010,000.00 USD | 0.00 USD | 158,010,000.00 USD | 1,020,000.00 USD | 597,650.00 USD | 483,730.00 USD |
| `7D` | `91.00` | 147,080,000.00 USD | 0.00 USD | 147,080,000.00 USD | 1,190,000.00 USD | 609,900.00 USD | 810,620.00 USD |
| `1D` | `91.20` | 155,900,000.00 USD | 0.00 USD | 155,900,000.00 USD | 16,980.00 USD | 493,060.00 USD | 403,810.00 USD |
| `7D` | `91.20` | 144,470,000.00 USD | 0.00 USD | 144,470,000.00 USD | 2,280,000.00 USD | 868,420.00 USD | 638,860.00 USD |
| `1D` | `91.40` | 154,990,000.00 USD | 0.00 USD | 154,990,000.00 USD | 664,720.00 USD | 758,110.00 USD | 111,340.00 USD |
| `7D` | `91.40` | 140,690,000.00 USD | 0.00 USD | 140,690,000.00 USD | 1,180,000.00 USD | 1,030,000.00 USD | 1,620,000.00 USD |
| `1D` | `91.60` | 153,450,000.00 USD | 0.00 USD | 153,450,000.00 USD | 488,750.00 USD | 281,460.00 USD | 1,100,000.00 USD |
| `7D` | `91.60` | 136,870,000.00 USD | 0.00 USD | 136,870,000.00 USD | 500,280.00 USD | 1,020,000.00 USD | 872,760.00 USD |
| `1D` | `91.80` | 151,580,000.00 USD | 0.00 USD | 151,580,000.00 USD | 526,140.00 USD | 449,000.00 USD | 713,610.00 USD |
| `7D` | `91.80` | 134,480,000.00 USD | 0.00 USD | 134,480,000.00 USD | 932,400.00 USD | 797,110.00 USD | 688,730.00 USD |
| `1D` | `92.00` | 149,890,000.00 USD | 0.00 USD | 149,890,000.00 USD | 2,810,000.00 USD | 2,220,000.00 USD | 1,110,000.00 USD |
| `7D` | `92.00` | 132,060,000.00 USD | 0.00 USD | 132,060,000.00 USD | 681,440.00 USD | 656,110.00 USD | 990,500.00 USD |
| `1D` | `92.20` | 143,750,000.00 USD | 0.00 USD | 143,750,000.00 USD | 887,260.00 USD | 1,630,000.00 USD | 465,660.00 USD |
| `7D` | `92.20` | 129,730,000.00 USD | 0.00 USD | 129,730,000.00 USD | 2,870,000.00 USD | 1,110,000.00 USD | 289,060.00 USD |
| `1D` | `92.40` | 140,770,000.00 USD | 0.00 USD | 140,770,000.00 USD | 731,980.00 USD | 331,330.00 USD | 2,170,000.00 USD |
| `7D` | `92.40` | 125,470,000.00 USD | 0.00 USD | 125,470,000.00 USD | 550,500.00 USD | 833,900.00 USD | 1,540,000.00 USD |
| `1D` | `92.60` | 137,540,000.00 USD | 0.00 USD | 137,540,000.00 USD | 1,330,000.00 USD | 1,530,000.00 USD | 2,410,000.00 USD |
| `7D` | `92.60` | 122,540,000.00 USD | 0.00 USD | 122,540,000.00 USD | 98,670.00 USD | 880,990.00 USD | 1,480,000.00 USD |
| `1D` | `92.80` | 132,260,000.00 USD | 0.00 USD | 132,260,000.00 USD | 1,940,000.00 USD | 824,500.00 USD | 775,910.00 USD |
| `7D` | `92.80` | 120,090,000.00 USD | 0.00 USD | 120,090,000.00 USD | 422,920.00 USD | 2,340,000.00 USD | 1,610,000.00 USD |
| `1D` | `93.00` | 128,720,000.00 USD | 0.00 USD | 128,720,000.00 USD | 2,640,000.00 USD | 3,760,000.00 USD | 3,040,000.00 USD |
| `7D` | `93.00` | 115,710,000.00 USD | 0.00 USD | 115,710,000.00 USD | 35,740.00 USD | 393,980.00 USD | 1,270,000.00 USD |
| `1D` | `93.20` | 119,280,000.00 USD | 0.00 USD | 119,280,000.00 USD | 2,380,000.00 USD | 1,620,000.00 USD | 1,940,000.00 USD |
| `7D` | `93.20` | 114,020,000.00 USD | 0.00 USD | 114,020,000.00 USD | 921,350.00 USD | 650,760.00 USD | 2,130,000.00 USD |
| `1D` | `93.40` | 113,350,000.00 USD | 0.00 USD | 113,350,000.00 USD | 3,070,000.00 USD | 3,100,000.00 USD | 2,300,000.00 USD |
| `7D` | `93.40` | 110,320,000.00 USD | 0.00 USD | 110,320,000.00 USD | 611,840.00 USD | 2,520,000.00 USD | 1,430,000.00 USD |
| `1D` | `93.60` | 104,880,000.00 USD | 0.00 USD | 104,880,000.00 USD | 1,950,000.00 USD | 3,880,000.00 USD | 1,070,000.00 USD |
| `7D` | `93.60` | 105,750,000.00 USD | 0.00 USD | 105,750,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,640,000.00 USD |
| `1D` | `93.80` | 97,980,000.00 USD | 0.00 USD | 97,980,000.00 USD | 1,010,000.00 USD | 1,030,000.00 USD | 483,140.00 USD |
| `7D` | `93.80` | 102,810,000.00 USD | 0.00 USD | 102,810,000.00 USD | 0.00 USD | 2,080,000.00 USD | 3,170,000.00 USD |
| `1D` | `94.00` | 95,460,000.00 USD | 0.00 USD | 95,460,000.00 USD | 759,420.00 USD | 1,060,000.00 USD | 1,830,000.00 USD |
| `7D` | `94.00` | 97,560,000.00 USD | 0.00 USD | 97,560,000.00 USD | 2,660,000.00 USD | 1,780,000.00 USD | 2,210,000.00 USD |
| `1D` | `94.20` | 91,820,000.00 USD | 0.00 USD | 91,820,000.00 USD | 1,980,000.00 USD | 1,940,000.00 USD | 2,160,000.00 USD |
| `7D` | `94.20` | 90,910,000.00 USD | 0.00 USD | 90,910,000.00 USD | 24,740.00 USD | 962,410.00 USD | 2,750,000.00 USD |
| `1D` | `94.40` | 85,730,000.00 USD | 0.00 USD | 85,730,000.00 USD | 1,650,000.00 USD | 568,640.00 USD | 1,010,000.00 USD |
| `7D` | `94.40` | 87,170,000.00 USD | 0.00 USD | 87,170,000.00 USD | 0.00 USD | 496,790.00 USD | 9,790.00 USD |
| `1D` | `94.60` | 82,510,000.00 USD | 0.00 USD | 82,510,000.00 USD | 142,910.00 USD | 1,380,000.00 USD | 396,580.00 USD |
| `7D` | `94.60` | 86,660,000.00 USD | 0.00 USD | 86,660,000.00 USD | 560,570.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `94.80` | 80,590,000.00 USD | 0.00 USD | 80,590,000.00 USD | 2,800,000.00 USD | 553,660.00 USD | 1,220,000.00 USD |
| `7D` | `94.80` | 86,100,000.00 USD | 0.00 USD | 86,100,000.00 USD | 2,010,000.00 USD | 99,300.00 USD | 3,360,000.00 USD |
| `1D` | `95.00` | 76,020,000.00 USD | 0.00 USD | 76,020,000.00 USD | 3,210,000.00 USD | 673,040.00 USD | 25,490.00 USD |
| `7D` | `95.00` | 80,630,000.00 USD | 0.00 USD | 80,630,000.00 USD | 2,400,000.00 USD | 4,460,000.00 USD | 47,940.00 USD |
| `1D` | `95.20` | 72,110,000.00 USD | 0.00 USD | 72,110,000.00 USD | 1,030,000.00 USD | 1,780,000.00 USD | 3,040,000.00 USD |
| `7D` | `95.20` | 73,730,000.00 USD | 0.00 USD | 73,730,000.00 USD | 2,080,000.00 USD | 277,550.00 USD | 17,980.00 USD |
| `1D` | `95.40` | 66,270,000.00 USD | 0.00 USD | 66,270,000.00 USD | 1,120,000.00 USD | 1,820,000.00 USD | 1,170,000.00 USD |
| `7D` | `95.40` | 71,350,000.00 USD | 0.00 USD | 71,350,000.00 USD | 2,080,000.00 USD | 2,340,000.00 USD | 4,590,000.00 USD |
| `1D` | `95.60` | 62,160,000.00 USD | 0.00 USD | 62,160,000.00 USD | 1,850,000.00 USD | 2,410,000.00 USD | 1,130,000.00 USD |
| `7D` | `95.60` | 62,340,000.00 USD | 0.00 USD | 62,340,000.00 USD | 3,820,000.00 USD | 7,040,000.00 USD | 4,590,000.00 USD |
| `1D` | `95.80` | 56,770,000.00 USD | 0.00 USD | 56,770,000.00 USD | 571,180.00 USD | 1,020,000.00 USD | 5,910,000.00 USD |
| `7D` | `95.80` | 46,890,000.00 USD | 0.00 USD | 46,890,000.00 USD | 3,400,000.00 USD | 93,510.00 USD | 1,280,000.00 USD |
| `1D` | `96.00` | 49,260,000.00 USD | 0.00 USD | 49,260,000.00 USD | 3,070,000.00 USD | 2,590,000.00 USD | 4,580,000.00 USD |
| `7D` | `96.00` | 42,130,000.00 USD | 0.00 USD | 42,130,000.00 USD | 2,670,000.00 USD | 728,410.00 USD | 3,590,000.00 USD |
| `1D` | `96.20` | 39,020,000.00 USD | 0.00 USD | 39,020,000.00 USD | 5,210,000.00 USD | 6,860,000.00 USD | 1,440,000.00 USD |
| `7D` | `96.20` | 35,140,000.00 USD | 0.00 USD | 35,140,000.00 USD | 6,840,000.00 USD | 2,140,000.00 USD | 5,250,000.00 USD |
| `1D` | `96.40` | 25,520,000.00 USD | 0.00 USD | 25,520,000.00 USD | 4,170,000.00 USD | 2,150,000.00 USD | 4,620,000.00 USD |
| `7D` | `96.40` | 20,910,000.00 USD | 0.00 USD | 20,910,000.00 USD | 1,600,000.00 USD | 2,590,000.00 USD | 6,470,000.00 USD |
| `1D` | `96.60` | 14,580,000.00 USD | 0.00 USD | 14,580,000.00 USD | 1,410,000.00 USD | 2,010,000.00 USD | 299,180.00 USD |
| `7D` | `96.60` | 10,250,000.00 USD | 0.00 USD | 10,250,000.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD |
| `1D` | `96.80` | 10,860,000.00 USD | 0.00 USD | 10,860,000.00 USD | 1,350,000.00 USD | 2,230,000.00 USD | 2,320,000.00 USD |
| `7D` | `96.80` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 0.00 USD | 79,170.00 USD | 2,350,000.00 USD |
| `1D` | `97.00` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 0.00 USD | 1,410,000.00 USD | 3,550,000.00 USD |
| `7D` | `97.00` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 0.00 USD | 2,240,000.00 USD | 2,160,000.00 USD |
| `7D` | `97.20` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 0.00 USD | 87,380.00 USD | 3,310,000.00 USD |
| `1D` | `97.40` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 534,370.00 USD | 1,280,000.00 USD | 292,940.00 USD |
| `1D` | `97.40` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 534,370.00 USD | 1,280,000.00 USD | 292,940.00 USD |
| `7D` | `97.40` | 101,560.00 USD | 101,560.00 USD | 0.00 USD | 0.00 USD | 101,560.00 USD | 0.00 USD |
| `7D` | `97.40` | 203,120.00 USD | 203,120.00 USD | 0.00 USD | 0.00 USD | 101,560.00 USD | 0.00 USD |
| `1D` | `97.60` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,230,000.00 USD |
| `7D` | `97.60` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 24,930.00 USD | 3,910,000.00 USD |
| `1D` | `97.80` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `97.80` | 15,160,000.00 USD | 15,160,000.00 USD | 0.00 USD | 7,580,000.00 USD | 3,430,000.00 USD | 0.00 USD |
| `1D` | `98.00` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 773,040.00 USD | 407,460.00 USD | 320,840.00 USD |
| `7D` | `98.00` | 26,590,000.00 USD | 26,590,000.00 USD | 0.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `98.20` | 13,930,000.00 USD | 13,930,000.00 USD | 0.00 USD | 2,200,000.00 USD | 1,790,000.00 USD | 1,450,000.00 USD |
| `7D` | `98.20` | 36,930,000.00 USD | 36,930,000.00 USD | 0.00 USD | 9,790,000.00 USD | 555,110.00 USD | 0.00 USD |
| `1D` | `98.40` | 24,730,000.00 USD | 24,730,000.00 USD | 0.00 USD | 772,180.00 USD | 311,650.00 USD | 9,720,000.00 USD |
| `7D` | `98.40` | 48,060,000.00 USD | 48,060,000.00 USD | 0.00 USD | 1,780,000.00 USD | 3,320,000.00 USD | 6,030,000.00 USD |
| `1D` | `98.60` | 37,960,000.00 USD | 37,960,000.00 USD | 0.00 USD | 488,190.00 USD | 5,730,000.00 USD | 7,000,000.00 USD |
| `7D` | `98.60` | 57,290,000.00 USD | 57,290,000.00 USD | 0.00 USD | 1,880,000.00 USD | 5,400,000.00 USD | 1,950,000.00 USD |
| `1D` | `98.80` | 49,510,000.00 USD | 49,510,000.00 USD | 0.00 USD | 1,400,000.00 USD | 4,160,000.00 USD | 6,000,000.00 USD |
| `7D` | `98.80` | 60,250,000.00 USD | 60,250,000.00 USD | 0.00 USD | 71,480.00 USD | 470,960.00 USD | 2,410,000.00 USD |
| `1D` | `99.00` | 63,670,000.00 USD | 63,670,000.00 USD | 0.00 USD | 2,810,000.00 USD | 5,870,000.00 USD | 5,480,000.00 USD |
| `7D` | `99.00` | 68,700,000.00 USD | 68,700,000.00 USD | 0.00 USD | 1,830,000.00 USD | 2,660,000.00 USD | 3,960,000.00 USD |
| `1D` | `99.20` | 74,680,000.00 USD | 74,680,000.00 USD | 0.00 USD | 2,840,000.00 USD | 4,520,000.00 USD | 3,640,000.00 USD |
| `7D` | `99.20` | 82,390,000.00 USD | 82,390,000.00 USD | 0.00 USD | 1,220,000.00 USD | 6,240,000.00 USD | 6,240,000.00 USD |
| `1D` | `99.40` | 81,590,000.00 USD | 81,590,000.00 USD | 0.00 USD | 3,580,000.00 USD | 1,650,000.00 USD | 1,680,000.00 USD |
| `7D` | `99.40` | 83,430,000.00 USD | 83,430,000.00 USD | 0.00 USD | 0.00 USD | 1,010,000.00 USD | 25,850.00 USD |
| `1D` | `99.60` | 98,340,000.00 USD | 98,340,000.00 USD | 0.00 USD | 2,920,000.00 USD | 6,720,000.00 USD | 7,120,000.00 USD |
| `7D` | `99.60` | 88,860,000.00 USD | 88,860,000.00 USD | 0.00 USD | 2,240,000.00 USD | 2,640,000.00 USD | 545,090.00 USD |
| `1D` | `99.80` | 113,290,000.00 USD | 113,290,000.00 USD | 0.00 USD | 2,520,000.00 USD | 4,590,000.00 USD | 7,850,000.00 USD |
| `7D` | `99.80` | 92,190,000.00 USD | 92,190,000.00 USD | 0.00 USD | 736,270.00 USD | 1,330,000.00 USD | 1,270,000.00 USD |
| `1D` | `100.00` | 123,750,000.00 USD | 123,750,000.00 USD | 0.00 USD | 2,850,000.00 USD | 3,360,000.00 USD | 4,250,000.00 USD |
| `7D` | `100.00` | 103,520,000.00 USD | 103,520,000.00 USD | 0.00 USD | 2,220,000.00 USD | 2,310,000.00 USD | 6,790,000.00 USD |
| `1D` | `100.20` | 126,920,000.00 USD | 126,920,000.00 USD | 0.00 USD | 651,800.00 USD | 2,130,000.00 USD | 388,240.00 USD |
| `7D` | `100.20` | 109,600,000.00 USD | 109,600,000.00 USD | 0.00 USD | 843,770.00 USD | 2,460,000.00 USD | 2,780,000.00 USD |
| `1D` | `100.40` | 132,670,000.00 USD | 132,670,000.00 USD | 0.00 USD | 976,110.00 USD | 1,790,000.00 USD | 2,990,000.00 USD |
| `7D` | `100.40` | 114,080,000.00 USD | 114,080,000.00 USD | 0.00 USD | 993,830.00 USD | 654,600.00 USD | 2,830,000.00 USD |
| `1D` | `100.60` | 143,310,000.00 USD | 143,310,000.00 USD | 0.00 USD | 2,220,000.00 USD | 1,710,000.00 USD | 6,710,000.00 USD |
| `7D` | `100.60` | 119,860,000.00 USD | 119,860,000.00 USD | 0.00 USD | 2,110,000.00 USD | 1,450,000.00 USD | 2,220,000.00 USD |
| `1D` | `100.80` | 148,760,000.00 USD | 148,760,000.00 USD | 0.00 USD | 1,990,000.00 USD | 1,820,000.00 USD | 1,650,000.00 USD |
| `7D` | `100.80` | 121,600,000.00 USD | 121,600,000.00 USD | 0.00 USD | 491,210.00 USD | 1,220,000.00 USD | 23,970.00 USD |
| `1D` | `101.00` | 158,930,000.00 USD | 158,930,000.00 USD | 0.00 USD | 5,730,000.00 USD | 3,220,000.00 USD | 1,220,000.00 USD |
| `7D` | `101.00` | 140,380,000.00 USD | 140,380,000.00 USD | 0.00 USD | 4,000,000.00 USD | 7,040,000.00 USD | 7,750,000.00 USD |
| `1D` | `101.20` | 171,650,000.00 USD | 171,650,000.00 USD | 0.00 USD | 5,410,000.00 USD | 4,390,000.00 USD | 2,920,000.00 USD |
| `7D` | `101.20` | 159,650,000.00 USD | 159,650,000.00 USD | 0.00 USD | 7,240,000.00 USD | 5,180,000.00 USD | 6,850,000.00 USD |
| `1D` | `101.40` | 182,320,000.00 USD | 182,320,000.00 USD | 0.00 USD | 3,860,000.00 USD | 2,700,000.00 USD | 4,110,000.00 USD |
| `7D` | `101.40` | 176,710,000.00 USD | 176,710,000.00 USD | 0.00 USD | 4,720,000.00 USD | 1,270,000.00 USD | 11,070,000.00 USD |
| `1D` | `101.60` | 198,130,000.00 USD | 198,130,000.00 USD | 0.00 USD | 3,100,000.00 USD | 2,930,000.00 USD | 9,780,000.00 USD |
| `7D` | `101.60` | 187,230,000.00 USD | 187,230,000.00 USD | 0.00 USD | 3,650,000.00 USD | 30,170.00 USD | 6,840,000.00 USD |
| `1D` | `101.80` | 204,350,000.00 USD | 204,350,000.00 USD | 0.00 USD | 646,170.00 USD | 836,200.00 USD | 4,730,000.00 USD |
| `7D` | `101.80` | 197,160,000.00 USD | 197,160,000.00 USD | 0.00 USD | 3,050,000.00 USD | 609,510.00 USD | 6,270,000.00 USD |
| `1D` | `102.00` | 210,630,000.00 USD | 210,630,000.00 USD | 0.00 USD | 2,520,000.00 USD | 1,780,000.00 USD | 1,990,000.00 USD |
| `7D` | `102.00` | 203,150,000.00 USD | 203,150,000.00 USD | 0.00 USD | 1,830,000.00 USD | 1,470,000.00 USD | 2,690,000.00 USD |
| `1D` | `102.20` | 216,980,000.00 USD | 216,980,000.00 USD | 0.00 USD | 3,180,000.00 USD | 1,360,000.00 USD | 1,800,000.00 USD |
| `7D` | `102.20` | 209,870,000.00 USD | 209,870,000.00 USD | 0.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,540,000.00 USD |
| `1D` | `102.40` | 221,480,000.00 USD | 221,480,000.00 USD | 0.00 USD | 1,560,000.00 USD | 716,320.00 USD | 2,220,000.00 USD |
| `7D` | `102.40` | 215,180,000.00 USD | 215,180,000.00 USD | 0.00 USD | 2,340,000.00 USD | 304,350.00 USD | 2,660,000.00 USD |
| `1D` | `102.60` | 224,110,000.00 USD | 224,110,000.00 USD | 0.00 USD | 985,660.00 USD | 606,030.00 USD | 1,040,000.00 USD |
| `7D` | `102.60` | 217,640,000.00 USD | 217,640,000.00 USD | 0.00 USD | 1,450,000.00 USD | 979,270.00 USD | 33,240.00 USD |
| `1D` | `102.80` | 228,160,000.00 USD | 228,160,000.00 USD | 0.00 USD | 1,260,000.00 USD | 1,570,000.00 USD | 1,220,000.00 USD |
| `7D` | `102.80` | 225,730,000.00 USD | 225,730,000.00 USD | 0.00 USD | 7,780,000.00 USD | 23,810.00 USD | 286,910.00 USD |
| `1D` | `103.00` | 233,220,000.00 USD | 233,220,000.00 USD | 0.00 USD | 3,120,000.00 USD | 1,440,000.00 USD | 498,100.00 USD |
| `7D` | `103.00` | 242,660,000.00 USD | 242,660,000.00 USD | 0.00 USD | 12,270,000.00 USD | 394,420.00 USD | 4,270,000.00 USD |
| `1D` | `103.20` | 235,590,000.00 USD | 235,590,000.00 USD | 0.00 USD | 301,000.00 USD | 853,780.00 USD | 1,220,000.00 USD |
| `7D` | `103.20` | 255,340,000.00 USD | 255,340,000.00 USD | 0.00 USD | 11,620,000.00 USD | 140,550.00 USD | 913,680.00 USD |
| `1D` | `103.40` | 238,510,000.00 USD | 238,510,000.00 USD | 0.00 USD | 867,130.00 USD | 1,180,000.00 USD | 877,320.00 USD |
| `7D` | `103.40` | 269,910,000.00 USD | 269,910,000.00 USD | 0.00 USD | 11,050,000.00 USD | 233,330.00 USD | 3,280,000.00 USD |
| `1D` | `103.60` | 246,140,000.00 USD | 246,140,000.00 USD | 0.00 USD | 2,430,000.00 USD | 183,360.00 USD | 5,010,000.00 USD |
| `7D` | `103.60` | 288,300,000.00 USD | 288,300,000.00 USD | 0.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD |
| `1D` | `103.80` | 249,300,000.00 USD | 249,300,000.00 USD | 0.00 USD | 481,980.00 USD | 1,320,000.00 USD | 1,350,000.00 USD |
| `7D` | `103.80` | 300,680,000.00 USD | 300,680,000.00 USD | 0.00 USD | 7,960,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD |
| `1D` | `104.00` | 255,150,000.00 USD | 255,150,000.00 USD | 0.00 USD | 2,410,000.00 USD | 1,540,000.00 USD | 1,910,000.00 USD |
| `7D` | `104.00` | 327,390,000.00 USD | 327,390,000.00 USD | 0.00 USD | 10,830,000.00 USD | 7,160,000.00 USD | 8,710,000.00 USD |
| `1D` | `104.20` | 258,570,000.00 USD | 258,570,000.00 USD | 0.00 USD | 1,440,000.00 USD | 931,620.00 USD | 1,050,000.00 USD |
| `7D` | `104.20` | 349,410,000.00 USD | 349,410,000.00 USD | 0.00 USD | 8,520,000.00 USD | 7,230,000.00 USD | 6,280,000.00 USD |
| `1D` | `104.40` | 263,420,000.00 USD | 263,420,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,510,000.00 USD | 1,490,000.00 USD |
| `7D` | `104.40` | 366,600,000.00 USD | 366,600,000.00 USD | 0.00 USD | 5,100,000.00 USD | 3,710,000.00 USD | 8,360,000.00 USD |
| `1D` | `104.60` | 267,660,000.00 USD | 267,660,000.00 USD | 0.00 USD | 1,060,000.00 USD | 868,480.00 USD | 2,310,000.00 USD |
| `7D` | `104.60` | 384,350,000.00 USD | 384,350,000.00 USD | 0.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 7,020,000.00 USD |
| `1D` | `104.80` | 271,680,000.00 USD | 271,680,000.00 USD | 0.00 USD | 1,250,000.00 USD | 820,470.00 USD | 1,950,000.00 USD |
| `7D` | `104.80` | 401,740,000.00 USD | 401,740,000.00 USD | 0.00 USD | 5,170,000.00 USD | 4,410,000.00 USD | 7,820,000.00 USD |
| `1D` | `105.00` | 272,900,000.00 USD | 272,900,000.00 USD | 0.00 USD | 463,890.00 USD | 350,040.00 USD | 413,950.00 USD |
| `7D` | `105.00` | 417,900,000.00 USD | 417,900,000.00 USD | 0.00 USD | 5,730,000.00 USD | 4,110,000.00 USD | 6,330,000.00 USD |
| `1D` | `105.20` | 273,970,000.00 USD | 273,970,000.00 USD | 0.00 USD | 111,930.00 USD | 94,030.00 USD | 864,650.00 USD |
| `7D` | `105.20` | 428,570,000.00 USD | 428,570,000.00 USD | 0.00 USD | 5,340,000.00 USD | 2,800,000.00 USD | 2,530,000.00 USD |
| `1D` | `105.40` | 274,450,000.00 USD | 274,450,000.00 USD | 0.00 USD | 262,490.00 USD | 138,720.00 USD | 78,430.00 USD |
| `7D` | `105.40` | 436,790,000.00 USD | 436,790,000.00 USD | 0.00 USD | 1,570,000.00 USD | 3,170,000.00 USD | 3,470,000.00 USD |
| `1D` | `105.60` | 274,880,000.00 USD | 274,880,000.00 USD | 0.00 USD | 130,280.00 USD | 187,950.00 USD | 110,700.00 USD |
| `7D` | `105.60` | 447,170,000.00 USD | 447,170,000.00 USD | 0.00 USD | 3,700,000.00 USD | 2,700,000.00 USD | 3,970,000.00 USD |
| `1D` | `105.80` | 275,570,000.00 USD | 275,570,000.00 USD | 0.00 USD | 87,540.00 USD | 526,970.00 USD | 76,760.00 USD |
| `7D` | `105.80` | 455,980,000.00 USD | 455,980,000.00 USD | 0.00 USD | 2,690,000.00 USD | 2,620,000.00 USD | 3,510,000.00 USD |
| `1D` | `106.00` | 276,730,000.00 USD | 276,730,000.00 USD | 0.00 USD | 372,000.00 USD | 554,120.00 USD | 226,820.00 USD |
| `7D` | `106.00` | 461,130,000.00 USD | 461,130,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,050,000.00 USD | 2,130,000.00 USD |
| `1D` | `106.20` | 278,140,000.00 USD | 278,140,000.00 USD | 0.00 USD | 623,340.00 USD | 349,490.00 USD | 440,280.00 USD |
| `7D` | `106.20` | 470,020,000.00 USD | 470,020,000.00 USD | 0.00 USD | 3,820,000.00 USD | 2,560,000.00 USD | 2,520,000.00 USD |
| `1D` | `106.40` | 278,870,000.00 USD | 278,870,000.00 USD | 0.00 USD | 181,780.00 USD | 354,890.00 USD | 197,110.00 USD |
| `7D` | `106.40` | 476,080,000.00 USD | 476,080,000.00 USD | 0.00 USD | 2,420,000.00 USD | 2,170,000.00 USD | 1,470,000.00 USD |
| `1D` | `106.60` | 280,550,000.00 USD | 280,550,000.00 USD | 0.00 USD | 388,660.00 USD | 278,100.00 USD | 1,010,000.00 USD |
| `7D` | `106.60` | 481,900,000.00 USD | 481,900,000.00 USD | 0.00 USD | 1,330,000.00 USD | 1,460,000.00 USD | 3,020,000.00 USD |
| `1D` | `106.80` | 281,930,000.00 USD | 281,930,000.00 USD | 0.00 USD | 340,680.00 USD | 316,760.00 USD | 718,820.00 USD |
| `7D` | `106.80` | 486,540,000.00 USD | 486,540,000.00 USD | 0.00 USD | 999,190.00 USD | 918,930.00 USD | 2,730,000.00 USD |
| `1D` | `107.00` | 282,690,000.00 USD | 282,690,000.00 USD | 0.00 USD | 193,920.00 USD | 413,830.00 USD | 147,220.00 USD |
| `7D` | `107.00` | 490,680,000.00 USD | 490,680,000.00 USD | 0.00 USD | 527,980.00 USD | 1,180,000.00 USD | 2,430,000.00 USD |
| `1D` | `107.20` | 283,170,000.00 USD | 283,170,000.00 USD | 0.00 USD | 0.00 USD | 50,140.00 USD | 436,040.00 USD |
| `7D` | `107.20` | 491,770,000.00 USD | 491,770,000.00 USD | 0.00 USD | 230,020.00 USD | 507,570.00 USD | 352,500.00 USD |
| `1D` | `107.40` | 284,010,000.00 USD | 284,010,000.00 USD | 0.00 USD | 90,150.00 USD | 226,090.00 USD | 523,690.00 USD |
| `7D` | `107.40` | 493,060,000.00 USD | 493,060,000.00 USD | 0.00 USD | 0.00 USD | 576,040.00 USD | 709,670.00 USD |
| `1D` | `107.60` | 284,750,000.00 USD | 284,750,000.00 USD | 0.00 USD | 47,860.00 USD | 202,660.00 USD | 485,910.00 USD |
| `7D` | `107.60` | 493,690,000.00 USD | 493,690,000.00 USD | 0.00 USD | 213,520.00 USD | 12,070.00 USD | 406,020.00 USD |
| `1D` | `107.80` | 285,420,000.00 USD | 285,420,000.00 USD | 0.00 USD | 140,490.00 USD | 168,390.00 USD | 365,710.00 USD |
| `7D` | `107.80` | 494,530,000.00 USD | 494,530,000.00 USD | 0.00 USD | 499,550.00 USD | 31,020.00 USD | 305,630.00 USD |
| `1D` | `108.00` | 285,750,000.00 USD | 285,750,000.00 USD | 0.00 USD | 84,680.00 USD | 178,840.00 USD | 65,030.00 USD |
| `7D` | `108.00` | 495,110,000.00 USD | 495,110,000.00 USD | 0.00 USD | 5,950.00 USD | 237,870.00 USD | 335,390.00 USD |
| `1D` | `108.20` | 285,880,000.00 USD | 285,880,000.00 USD | 0.00 USD | 68,370.00 USD | 62,390.00 USD | 0.00 USD |
| `7D` | `108.20` | 495,390,000.00 USD | 495,390,000.00 USD | 0.00 USD | 0.00 USD | 205,080.00 USD | 74,400.00 USD |
| `7D` | `108.40` | 495,880,000.00 USD | 495,880,000.00 USD | 0.00 USD | 487,890.00 USD | 0.00 USD | 2,900.00 USD |
| `7D` | `108.60` | 496,060,000.00 USD | 496,060,000.00 USD | 0.00 USD | 17,470.00 USD | 167,730.00 USD | 0.00 USD |
| `7D` | `108.80` | 497,490,000.00 USD | 497,490,000.00 USD | 0.00 USD | 350,210.00 USD | 397,420.00 USD | 674,910.00 USD |
| `7D` | `109.00` | 497,780,000.00 USD | 497,780,000.00 USD | 0.00 USD | 8,180.00 USD | 0.00 USD | 286,720.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `5.61B` | Total OI Tokens: `57,630,108.2 SOL`
  * 1h OI Change: `+0.45%` | 4h OI Change: `-1.98%` | 24h OI Change: `-12.82%`
  * Exchange Breakdown: Binance=`971.23M` | Bybit=`611.51M` | OKX=`390.88M` | Hyperliquid=`521.91M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-134.78K` | Last 24h: `177.62K` | Last 3d: `997.77K` | Last 7d: `2.11M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0019%` | **USDT OKX** | `-0.0239%` |
| **USDT Bybit** | `-0.0127%` | **USDT KuCoin** | `-0.0110%` |
| **USDT MEXC** | `0.0018%` | **USDT BingX** | `0.0017%` |
| **USDT Gate** | `-0.0129%` | **USDT Bitget** | `-0.0113%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0053%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `42.64%` | `57.36%` | `0.74` | 51,350,000.00 USD |
| `15M` | `Binance` | `39.39%` | `60.61%` | `0.65` | 12,520,000.00 USD |
| `15M` | `OKX` | `32.2%` | `67.8%` | `0.47` | 9,820,000.00 USD |
| `15M` | `Bybit` | `50.81%` | `49.19%` | `1.03` | 2,570,000.00 USD |
| `15M` | `KuCoin` | `48.32%` | `51.68%` | `0.93` | 147,880.00 USD |
| `15M` | `Gate` | `46.35%` | `53.65%` | `0.86` | 3,510,000.00 USD |
| `15M` | `Bitget` | `41.46%` | `58.54%` | `0.71` | 3,180,000.00 USD |
| `15M` | `BingX` | `43.43%` | `56.57%` | `0.77` | 2,390,000.00 USD |
| `15M` | `MEXC` | `48.34%` | `51.66%` | `0.94` | 9,500,000.00 USD |
| `15M` | `Bitunix` | `54.22%` | `45.78%` | `1.18` | 2,250,000.00 USD |
| `15M` | `Hyperliquid` | `36.2%` | `63.8%` | `0.57` | 1,770,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.63%` | `48.37%` | `1.07` | 2,190,000.00 USD |
| `15M` | `Crypto.com` | `34.3%` | `65.7%` | `0.52` | 129,270.00 USD |
| `15M` | `WhiteBIT` | `69.6%` | `30.4%` | `2.29` | 519,280.00 USD |
| `15M` | `HTX` | `46.9%` | `53.1%` | `0.88` | 67,290.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `46.75%` | `53.25%` | `0.88` | 281,790.00 USD |
| `15M` | `Aster` | `58.91%` | `41.09%` | `1.43` | 209,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `57.17%` | `42.83%` | `1.33` | 276,330.00 USD |
| `15M` | `Whale Positions` | `39.39%` | `60.61%` | `0.65` | 12,520,000.00 USD |
| `15M` | `Global Accounts` | `42.64%` | `57.36%` | `0.74` | 51,350,000.00 USD |
| `1H` | `SOL` | `49.93%` | `50.07%` | `1.00` | 100,510,000.00 USD |
| `1H` | `Binance` | `51.29%` | `48.71%` | `1.05` | 32,150,000.00 USD |
| `1H` | `OKX` | `48.55%` | `51.45%` | `0.94` | 8,550,000.00 USD |
| `1H` | `Bybit` | `60.46%` | `39.54%` | `1.53` | 16,080,000.00 USD |
| `1H` | `KuCoin` | `57.84%` | `42.16%` | `1.37` | 974,580.00 USD |
| `1H` | `Gate` | `56.2%` | `43.8%` | `1.28` | 6,890,000.00 USD |
| `1H` | `Bitget` | `51.34%` | `48.66%` | `1.06` | 8,110,000.00 USD |
| `1H` | `BingX` | `28.78%` | `71.22%` | `0.40` | 2,160,000.00 USD |
| `1H` | `MEXC` | `46.45%` | `53.55%` | `0.87` | 11,390,000.00 USD |
| `1H` | `Bitunix` | `47.64%` | `52.36%` | `0.91` | 3,470,000.00 USD |
| `1H` | `Hyperliquid` | `72.03%` | `27.97%` | `2.58` | 3,780,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `56.66%` | `43.34%` | `1.31` | 486,860.00 USD |
| `1H` | `Crypto.com` | `56.48%` | `43.52%` | `1.30` | 240,120.00 USD |
| `1H` | `WhiteBIT` | `1.44%` | `98.56%` | `0.01` | 4,540,000.00 USD |
| `1H` | `HTX` | `46.76%` | `53.24%` | `0.88` | 34,580.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `19.89%` | `80.11%` | `0.25` | 721,110.00 USD |
| `1H` | `Aster` | `26.41%` | `73.59%` | `0.36` | 780,700.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `60.39%` | `39.61%` | `1.52` | 161,670.00 USD |
| `1H` | `Whale Positions` | `51.29%` | `48.71%` | `1.05` | 32,150,000.00 USD |
| `1H` | `Global Accounts` | `49.93%` | `50.07%` | `1.00` | 100,510,000.00 USD |
| `4H` | `SOL` | `48.47%` | `51.53%` | `0.94` | 1,090,000,000.00 USD |
| `4H` | `Binance` | `47.08%` | `52.92%` | `0.89` | 326,570,000.00 USD |
| `4H` | `OKX` | `48.02%` | `51.98%` | `0.92` | 221,340,000.00 USD |
| `4H` | `Bybit` | `50.24%` | `49.76%` | `1.01` | 121,240,000.00 USD |
| `4H` | `KuCoin` | `49.94%` | `50.06%` | `1.00` | 4,810,000.00 USD |
| `4H` | `Gate` | `52.47%` | `47.53%` | `1.10` | 78,770,000.00 USD |
| `4H` | `Bitget` | `44.1%` | `55.9%` | `0.79` | 50,890,000.00 USD |
| `4H` | `BingX` | `46.22%` | `53.78%` | `0.86` | 45,120,000.00 USD |
| `4H` | `MEXC` | `45.42%` | `54.58%` | `0.83` | 94,220,000.00 USD |
| `4H` | `Bitunix` | `48.24%` | `51.76%` | `0.93` | 58,240,000.00 USD |
| `4H` | `Hyperliquid` | `52.26%` | `47.74%` | `1.09` | 41,960,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.31%` | `48.69%` | `1.05` | 12,920,000.00 USD |
| `4H` | `Crypto.com` | `50.14%` | `49.86%` | `1.01` | 2,290,000.00 USD |
| `4H` | `WhiteBIT` | `87.08%` | `12.92%` | `6.74` | 14,090,000.00 USD |
| `4H` | `HTX` | `55.74%` | `44.26%` | `1.26` | 1,710,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `30.45%` | `69.55%` | `0.44` | 1,070,000.00 USD |
| `4H` | `Aster` | `46.19%` | `53.81%` | `0.86` | 6,930,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `42.5%` | `57.5%` | `0.74` | 12,660,000.00 USD |
| `4H` | `Whale Positions` | `47.08%` | `52.92%` | `0.89` | 326,570,000.00 USD |
| `4H` | `Global Accounts` | `48.47%` | `51.53%` | `0.94` | 1,090,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `98.16` | `98.20` | `98.16` | `98.53` | `98.00` | 14,041,198.88 USD | 6,875,129.47 USD | 7,166,069.42 USD | -290,939.95 USD | `-2.07%` | `8B / 3S` |
| `5:00 UTC` | `98.00` | `98.10` | `98.00` | `98.38` | `97.82` | 11,697,482.78 USD | 5,190,334.49 USD | 6,507,148.30 USD | -1,316,813.81 USD | `-11.26%` | `5B / 11S` |
| `0:00 UTC` | `98.09` | `98.10` | `98.09` | `98.28` | `97.90` | 11,316,185.46 USD | 4,994,801.42 USD | 6,321,384.04 USD | -1,326,582.61 USD | `-11.72%` | `0B / 11S` |
| `5:00 UTC` | `97.95` | `97.99` | `97.95` | `98.12` | `97.90` | 8,075,212.15 USD | 2,930,391.45 USD | 5,144,820.70 USD | -2,214,429.25 USD | `-27.42%` | `1B / 4S` |
| `0:00 UTC` | `97.70` | `97.69` | `97.70` | `98.20` | `97.19` | 26,621,435.83 USD | 11,084,087.20 USD | 15,537,348.64 USD | -4,453,261.44 USD | `-16.73%` | `5B / 32S` |
| `5:00 UTC` | `97.31` | `97.23` | `97.31` | `97.59` | `96.94` | 34,349,154.70 USD | 16,069,023.45 USD | 18,280,131.25 USD | -2,211,107.80 USD | `-6.44%` | `8B / 12S` |
| `0:00 UTC` | `97.07` | `97.11` | `97.07` | `97.31` | `96.84` | 19,320,776.86 USD | 9,044,516.83 USD | 10,276,260.03 USD | -1,231,743.19 USD | `-6.38%` | `6B / 9S` |
| `5:00 UTC` | `97.31` | `97.36` | `97.31` | `97.56` | `97.18` | 14,539,694.05 USD | 7,744,567.35 USD | 6,795,126.70 USD | 949,440.65 USD | `+6.53%` | `8B / 2S` |
| `0:00 UTC` | `97.15` | `97.19` | `97.15` | `97.37` | `97.05` | 9,961,152.58 USD | 4,407,159.48 USD | 5,553,993.10 USD | -1,146,833.62 USD | `-11.51%` | `1B / 5S` |
| `5:00 UTC` | `97.03` | `97.23` | `97.03` | `97.56` | `97.00` | 10,801,128.91 USD | 5,445,655.05 USD | 5,355,473.86 USD | 90,181.19 USD | `+0.83%` | `14B / 4S` |

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
| `5m` | -210,460.00 USD | -4,170,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -479,490.00 USD | -6,580,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -253,680.00 USD | -7,510,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 2,120,000.00 USD | -7,610,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -881,700.00 USD | -30,780,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 3,130,000.00 USD | -30,500,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 5,440,000.00 USD | 10,210,000.00 USD | **`ACCUMULATION`** |
| `8h` | 13,430,000.00 USD | -83,110,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -30,010,000.00 USD | -227,260,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -43,140,000.00 USD | -424,520,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 31,990,000.00 USD | -687,610,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -1,820,000.00 USD | -2,190,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-210.46K` | 15m=`-479.49K` | 1h=`+2.12M` | 24h=`-43.14M`
* Futures Capital Netflows: 5m=`-4.17M` | 15m=`-6.58M` | 1h=`-7.61M` | 24h=`-424.52M`
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
  * Execution Entry: `95.01` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `93.47` (Risk Distance: `1.55` pts)
  * +2.5R Take Profit: `98.87`
  * Mathematical Lot Sizing: **`6.47 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `98.09` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `99.64` (Risk Distance: `1.55` pts)
  * +2.5R Take Profit: `94.23`
  * Mathematical Lot Sizing: **`6.47 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`97.89`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
