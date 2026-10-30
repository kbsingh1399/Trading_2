# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 15:24:07 IST` (`2026-10-30 09:54:07 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `96.62` | **Live Ask Quote**: `96.86` | **Mid Price**: `96.74`
- **Spread Points**: `24.00` | **Spread BPS**: `24.81 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `95.71` | VWAP Z-Score: `+0.62` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.6055` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `46.91` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `100.58` | Lower -3.00σ Band: `90.83`
  * Upper +2.51σ Band: `99.79` | Lower -2.51σ Band: `91.62`
  * Upper +2.01σ Band: `98.97` | Lower -2.01σ Band: `92.44`
  * Upper +2.00σ Band: `98.96` | Lower -2.00σ Band: `92.45`
  * Upper +1.28σ Band: `97.79` | Lower -1.28σ Band: `93.62`
  * Upper +1.00σ Band: `97.33` | Lower -1.00σ Band: `94.08`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`96.92` | EMA-20=`96.95` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`97.10` (Slope: `+0.0000`) | EMA-100=`97.91`
  * Institutional Anchors: EMA-144=`98.47` | EMA-200=`98.99` (Slope: `-0.2454`) | EMA-233=`99.21`
- **Range Boundaries**: 24H High=`102.93` | 24H Low=`91.86` | Weekly High=`103.63` | Weekly Low=`91.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `98.09` (Distance: `-1.35%`)
  * Point of Control (POC) = `96.89` (Distance: `-0.13%`)
  * Value Area Low (VAL) = `95.09` (Distance: `+1.76%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`101.56` | POC=`99.94` | VAL=`98.94`
  * Prior Day Extremes: PDH=`102.93` | PDL=`94.56` | PDC=`95.94`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`102.10` | Weekly POC=`100.92` | Weekly VAL=`99.51`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`97.84` | Low=`91.86`
  * London Session (08:00-16:00 UTC): High=`98.28` | Low=`96.34`
  * New York Session (13:00-21:00 UTC): High=`97.32` | Low=`96.16`
  * Initial Balance (First Hour): IB High=`98.28` | IB Low=`96.72`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `96.35` - `97.13`
  * Optimal Trade Entry (OTE 0.705): `96.93`
  * Structural Invalidation Anchor (0.786): `97.51`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `97.03` | `97.15` | `96.88` | `96.99` | `41,647` | 4,040,667.20 USD | 896,069.26 USD | `+22.18%` | -225,025,593.08 USD | `+1.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `96.98` | `97.01` | `96.77` | `96.95` | `45,495` | 4,408,108.96 USD | 940,591.70 USD | `+21.34%` | -224,085,001.38 USD | `+1.09` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `96.95` | `96.95` | `96.87` | `96.87` | `1,228` | 119,024.14 USD | -47,449.23 USD | `-39.87%` | -224,132,450.61 USD | `+0.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `97.06` | `97.15` | `96.80` | `96.92` | `127,277` | 12,337,515.78 USD | -1,883,907.48 USD | `-15.27%` | -225,958,585.56 USD | `-0.32` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `96.91` | `97.15` | `96.68` | `96.99` | `154,066` | 14,931,632.13 USD | 1,124,750.63 USD | `+7.53%` | -224,833,834.93 USD | `+1.20` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `96.98` | `97.01` | `96.77` | `96.87` | `46,723` | 4,527,133.10 USD | 893,142.47 USD | `+19.73%` | -223,940,692.46 USD | `+0.98` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `98.26` | `98.28` | `96.93` | `97.28` | `823,584` | 80,361,988.15 USD | -10,205,381.09 USD | `-12.70%` | -219,805,116.69 USD | `+0.02` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `97.28` | `97.55` | `96.84` | `97.33` | `564,307` | 54,855,982.25 USD | -1,256,866.37 USD | `-2.29%` | -221,061,983.07 USD | `+0.46` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `97.34` | `97.44` | `96.68` | `96.87` | `508,767` | 49,358,160.09 USD | -2,878,745.22 USD | `-5.83%` | -223,940,728.29 USD | `+0.38` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -192,935,382.59 USD | `+0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.54` | `96.72` | `97.28` | `3,030,040` | 295,921,356.18 USD | -16,839,868.63 USD | `-5.69%` | -209,775,251.22 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.28` | `97.55` | `96.68` | `96.87` | `1,073,074` | 104,214,142.35 USD | -4,135,611.60 USD | `-3.97%` | -213,910,862.82 USD | `+0.81` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -33,800,710.11 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `95.62` | `13,887,188` | 1,349,343,315.53 USD | -115,873,425.65 USD | `-8.59%` | -149,674,135.76 USD | `-1.37` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -192,935,382.59 USD | `+0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.54` | `96.72` | `97.28` | `3,030,040` | 295,921,356.18 USD | -16,839,868.63 USD | `-5.69%` | -209,775,251.22 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.28` | `97.55` | `96.68` | `96.87` | `1,073,074` | 104,214,142.35 USD | -4,135,611.60 USD | `-3.97%` | -213,910,862.82 USD | `+0.81` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`96.74`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `96.82` | `116.5400` | 11,283.87 USD | 853,369.80 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `96.83` | `181.4800` | 17,573.62 USD | 593,073.92 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `96.83` | `41.3000` | 3,999.16 USD | 597,073.08 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `96.83` | `41.3000` | 3,999.12 USD | 601,072.20 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `96.83` | `2058.7700` | 199,350.70 USD | 800,422.90 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `96.83` | `143.9200` | 13,935.63 USD | 814,358.53 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `96.83` | `140.4800` | 13,602.40 USD | 827,960.93 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `96.83` | `63.2600` | 6,125.28 USD | 834,086.21 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `96.83` | `41.3100` | 3,999.88 USD | 838,086.09 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `96.83` | `41.3100` | 3,999.84 USD | 842,085.93 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `96.84` | `197.8000` | 19,155.74 USD | 489,303.75 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `96.84` | `72.1200` | 6,984.25 USD | 496,287.99 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `96.84` | `321.2500` | 31,110.17 USD | 527,398.17 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `96.84` | `314.9400` | 30,498.79 USD | 557,896.96 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `96.84` | `140.4800` | 13,603.94 USD | 571,500.90 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `96.84` | `41.3000` | 3,999.41 USD | 575,500.31 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `96.85` | `0.6200` | 60.05 USD | 60.05 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `96.85` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 96.85` | `0.00%` | `-` |
| `BID` | `96.85` | `2257.9900` | 218,684.07 USD | 218,684.07 USD | `20 orders` | `-0.00%` | `-` |
| `BID` | `96.85` | `174.8600` | 16,934.84 USD | 235,618.91 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `96.85` | `38.4600` | 3,724.74 USD | 239,343.65 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `96.85` | `2383.2100` | 230,804.36 USD | 470,148.01 USD | `3 orders` | `-0.00%` | `-` |
| `ASK` | `96.87` | `173.7300` | 16,829.75 USD | 16,889.79 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.89` | `2.5900` | 250.95 USD | 17,350.02 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `96.89` | `2.1600` | 209.28 USD | 17,099.07 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `96.90` | `40.6500` | 3,938.99 USD | 21,289.00 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `96.92` | `7.5100` | 727.91 USD | 84,703.73 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `96.92` | `625.8800` | 60,660.29 USD | 83,975.83 USD | `4 orders` | `+0.07%` | `-` |
| `ASK` | `96.92` | `20.9100` | 2,026.53 USD | 23,315.54 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `96.93` | `86.2600` | 8,361.53 USD | 170,070.86 USD | `1 orders` | `+0.09%` | `-` |
| `ASK` | `96.93` | `86.2600` | 8,361.44 USD | 161,709.33 USD | `1 orders` | `+0.09%` | `-` |
| `ASK` | `96.93` | `86.2600` | 8,361.35 USD | 153,347.89 USD | `1 orders` | `+0.09%` | `-` |
| `ASK` | `96.93` | `91.4600` | 8,865.31 USD | 144,986.54 USD | `2 orders` | `+0.08%` | `-` |
| `ASK` | `96.93` | `86.2600` | 8,361.18 USD | 136,121.23 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `96.93` | `185.4400` | 17,974.51 USD | 127,760.05 USD | `2 orders` | `+0.08%` | `-` |
| `ASK` | `96.93` | `86.2600` | 8,361.01 USD | 109,785.53 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `96.93` | `86.2600` | 8,360.92 USD | 101,424.52 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `96.93` | `86.2500` | 8,359.87 USD | 93,063.60 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `96.94` | `86.2600` | 8,361.79 USD | 195,155.96 USD | `1 orders` | `+0.09%` | `-` |
| `ASK` | `96.94` | `86.2600` | 8,361.70 USD | 186,794.17 USD | `1 orders` | `+0.09%` | `-` |
| `ASK` | `96.94` | `86.2600` | 8,361.61 USD | 178,432.47 USD | `1 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:20:42 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `11` | `0x5b5d...c060` | `SHORT` | 67,394,870.39 USD | `696,120.13` | `94.33` | `96.75` | `313.92` | -1,726,604.17 USD | `-2.56%` | `7X Cross` |
| `18` | `0x9c6a...a4ed` | `LONG` | 53,256,739.71 USD | `550,087.69` | `80.86` | `96.75` | `68.18` | 8,777,753.32 USD | `+16.48%` | `20X Cross` |
| `49` | `0xb83d...6e36` | `SHORT` | 25,102,882.98 USD | `259,338.02` | `91.42` | `96.75` | `551.94` | -1,394,068.94 USD | `-5.55%` | `5X Cross` |
| `79` | `0x3dc9...54b0` | `SHORT` | 21,299,758.40 USD | `220,000.19` | `105.90` | `96.75` | `176.28` | 1,999,348.88 USD | `+9.39%` | `20X Cross` |
| `109` | `0x9c89...600e` | `LONG` | 18,338,095.91 USD | `189,472.50` | `115.21` | `96.75` | `35.02` | -3,490,919.35 USD | `-19.04%` | `20X Cross` |
| `118` | `0x4a20...3c26` | `LONG` | 17,429,580.00 USD | `180,000.00` | `106.43` | `96.75` | `69.95` | -1,728,698.71 USD | `-9.92%` | `20X Cross` |
| `155` | `0xecb6...2b00` | `SHORT` | 13,105,230.62 USD | `135,450.38` | `101.13` | `96.75` | `329.52` | 592,342.60 USD | `+4.52%` | `20X Cross` |
| `222` | `0xb581...6f4f` | `LONG` | 9,681,500.00 USD | `100,000.00` | `112.81` | `96.75` | `0.000000` | -1,599,209.14 USD | `-16.52%` | `3X Cross` |
| `223` | `0xc63a...a3cd` | `LONG` | 9,675,300.00 USD | `100,000.00` | `112.22` | `96.75` | `0.000000` | -1,546,808.97 USD | `-15.99%` | `20X Cross` |
| `291` | `0x645b...87b8` | `SHORT` | 8,018,884.77 USD | `82,879.96` | `103.90` | `96.75` | `364.55` | 592,585.45 USD | `+7.39%` | `20X Cross` |
| `296` | `0xdb3a...cf3b` | `LONG` | 7,923,661.56 USD | `81,851.78` | `106.04` | `96.75` | `47.30` | -756,085.29 USD | `-9.54%` | `4X Cross` |
| `313` | `0xe927...98ef` | `LONG` | 7,551,414.00 USD | `78,000.00` | `96.34` | `96.75` | `38.45` | 37,272.52 USD | `+0.49%` | `3X Cross` |
| `321` | `0xca49...53c8` | `SHORT` | 7,166,229.46 USD | `73,943.45` | `110.70` | `96.75` | `303.15` | 1,019,392.80 USD | `+14.22%` | `20X Cross` |
| `327` | `0x8ae4...3d60` | `LONG` | 6,997,494.95 USD | `72,180.05` | `111.72` | `96.75` | `12.15` | -1,066,665.29 USD | `-15.24%` | `10X Cross` |
| `331` | `0xa0b7...6165` | `SHORT` | 6,878,165.52 USD | `71,044.42` | `107.87` | `96.75` | `190.91` | 785,301.68 USD | `+11.42%` | `2X Cross` |
| `350` | `0xf517...c032` | `SHORT` | 6,561,707.27 USD | `67,778.53` | `84.64` | `96.75` | `218.60` | -824,676.10 USD | `-12.57%` | `20X Cross` |
| `412` | `0x7fda...17d1` | `SHORT` | 5,392,975.45 USD | `55,739.62` | `100.53` | `96.75` | `801.25` | 210,737.55 USD | `+3.91%` | `20X Cross` |
| `467` | `0x7e23...5a5a` | `LONG` | 4,701,632.18 USD | `48,564.56` | `105.17` | `96.75` | `57.00` | -405,936.98 USD | `-8.63%` | `5X Isolated` |
| `561` | `0xf899...88db` | `SHORT` | 3,941,997.96 USD | `40,716.81` | `88.40` | `96.75` | `109.22` | -342,725.09 USD | `-8.69%` | `20X Cross` |
| `580` | `0x2e2b...2fab` | `LONG` | 3,872,480.00 USD | `40,000.00` | `119.55` | `96.75` | `60.09` | -909,555.64 USD | `-23.49%` | `10X Cross` |
| `613` | `0x9c16...4a6f` | `SHORT` | 3,663,011.94 USD | `37,796.13` | `90.79` | `96.75` | `118.57` | -231,661.21 USD | `-6.32%` | `20X Cross` |
| `626` | `0x7a5a...0394` | `SHORT` | 3,612,849.84 USD | `37,315.89` | `99.28` | `96.75` | `124.75` | 91,695.73 USD | `+2.54%` | `10X Cross` |
| `642` | `0x27b8...12fc` | `LONG` | 3,498,331.09 USD | `36,085.73` | `110.86` | `96.75` | `24.61` | -502,014.16 USD | `-14.35%` | `10X Cross` |
| `645` | `0x9946...0852` | `SHORT` | 3,494,980.84 USD | `36,099.58` | `110.82` | `96.75` | `141.15` | 505,605.55 USD | `+14.47%` | `20X Cross` |
| `676` | `0xa61c...66b9` | `LONG` | 3,336,761.50 USD | `34,466.76` | `102.77` | `96.75` | `0.000000` | -205,407.24 USD | `-6.16%` | `5X Cross` |
| `687` | `0x3440...32c5` | `SHORT` | 3,266,928.26 USD | `33,744.03` | `95.02` | `96.75` | `169.17` | -60,528.32 USD | `-1.85%` | `20X Cross` |
| `735` | `0x96a7...79df` | `LONG` | 3,098,080.00 USD | `32,000.00` | `74.39` | `96.75` | `0.000000` | 717,674.15 USD | `+23.17%` | `20X Cross` |
| `774` | `0xbe19...8bd1` | `SHORT` | 2,949,215.72 USD | `30,451.69` | `97.62` | `96.75` | `765.02` | 23,330.91 USD | `+0.79%` | `3X Cross` |
| `776` | `0x482b...cae4` | `SHORT` | 2,936,631.82 USD | `30,310.49` | `88.03` | `96.75` | `150.56` | -268,383.54 USD | `-9.14%` | `20X Cross` |
| `792` | `0x610b...b613` | `LONG` | 2,869,088.53 USD | `29,634.14` | `101.23` | `96.75` | `70.39` | -130,910.82 USD | `-4.56%` | `3X Isolated` |
| `804` | `0x45d2...4029` | `SHORT` | 2,829,401.82 USD | `29,220.00` | `93.28` | `96.75` | `1586.94` | -103,625.84 USD | `-3.66%` | `20X Cross` |
| `851` | `0x458d...ab3b` | `LONG` | 2,651,226.91 USD | `27,385.03` | `117.17` | `96.75` | `81.07` | -557,435.61 USD | `-21.03%` | `3X Isolated` |
| `882` | `0x023a...2355` | `SHORT` | 2,512,840.84 USD | `25,956.15` | `101.16` | `96.75` | `297.42` | 112,789.04 USD | `+4.49%` | `20X Cross` |
| `911` | `0x051c...693c` | `LONG` | 2,433,849.78 USD | `25,139.70` | `89.76` | `96.75` | `44.85` | 177,288.45 USD | `+7.28%` | `20X Cross` |
| `921` | `0xfc27...9d9d` | `SHORT` | 2,400,062.52 USD | `24,781.49` | `100.36` | `96.75` | `864.19` | 87,017.94 USD | `+3.63%` | `20X Cross` |
| `949` | `0x638f...f5f0` | `LONG` | 2,323,944.00 USD | `24,000.00` | `136.71` | `96.75` | `51.67` | -957,024.54 USD | `-41.18%` | `20X Cross` |
| `997` | `0x7277...0b98` | `SHORT` | 2,205,277.86 USD | `22,770.74` | `99.32` | `96.75` | `159.60` | 56,325.90 USD | `+2.55%` | `20X Cross` |
| `1004` | `0x7178...0854` | `LONG` | 2,182,717.41 USD | `22,545.24` | `110.94` | `96.75` | `40.28` | -318,427.06 USD | `-14.59%` | `10X Cross` |
| `1032` | `0x739c...cfb2` | `LONG` | 2,081,565.50 USD | `21,500.00` | `91.95` | `96.75` | `76.95` | 104,633.35 USD | `+5.03%` | `20X Cross` |
| `1099` | `0x7737...bf66` | `SHORT` | 1,973,482.77 USD | `20,384.06` | `102.94` | `96.75` | `991.46` | 124,859.12 USD | `+6.33%` | `10X Cross` |
| `1100` | `0x69cc...14fd` | `SHORT` | 1,972,286.01 USD | `20,372.33` | `99.01` | `96.75` | `499.13` | 44,759.89 USD | `+2.27%` | `20X Cross` |
| `1129` | `0xea00...a918` | `LONG` | 1,938,536.78 USD | `20,022.69` | `66.09` | `96.75` | `0.000000` | 615,228.18 USD | `+31.74%` | `20X Cross` |
| `1133` | `0xbfc7...80b4` | `SHORT` | 1,936,300.00 USD | `20,000.00` | `85.98` | `96.75` | `176.14` | -216,765.50 USD | `-11.19%` | `20X Cross` |
| `1134` | `0x3fc5...c0c1` | `SHORT` | 1,936,240.00 USD | `20,000.00` | `98.28` | `96.75` | `187.51` | 29,319.84 USD | `+1.51%` | `20X Cross` |
| `1135` | `0x251f...6e5d` | `LONG` | 1,936,220.00 USD | `20,000.00` | `101.15` | `96.75` | `71.73` | -86,877.77 USD | `-4.49%` | `20X Cross` |
| `1169` | `0x7160...d47c` | `LONG` | 1,881,434.66 USD | `19,434.10` | `105.03` | `96.75` | `76.33` | -159,786.64 USD | `-8.49%` | `20X Cross` |
| `1190` | `0xe097...d0fe` | `LONG` | 1,838,123.75 USD | `18,995.75` | `109.71` | `96.75` | `0.000000` | -245,873.14 USD | `-13.38%` | `20X Cross` |
| `1192` | `0x936c...bb0f` | `SHORT` | 1,837,234.01 USD | `18,988.91` | `105.57` | `96.75` | `536.61` | 167,453.68 USD | `+9.11%` | `20X Cross` |
| `1267` | `0xdf95...7d72` | `SHORT` | 1,723,556.78 USD | `17,802.58` | `104.53` | `96.75` | `2305.43` | 137,400.07 USD | `+7.97%` | `20X Cross` |
| `1273` | `0xe98b...8cd5` | `SHORT` | 1,706,160.10 USD | `17,622.89` | `187.95` | `96.75` | `262.70` | 1,606,060.63 USD | `+94.13%` | `20X Cross` |
| `1308` | `0xee2b...d67e` | `LONG` | 1,642,223.39 USD | `16,963.19` | `119.86` | `96.75` | `34.86` | -391,048.25 USD | `-23.81%` | `4X Cross` |
| `1323` | `0x123d...3bff` | `LONG` | 1,629,943.24 USD | `16,835.30` | `89.54` | `96.75` | `0.000000` | 122,501.98 USD | `+7.52%` | `10X Cross` |
| `1427` | `0x73d7...8be1` | `LONG` | 1,518,556.29 USD | `15,668.95` | `106.60` | `96.75` | `49.42` | -151,784.67 USD | `-10.00%` | `20X Cross` |
| `1442` | `0xc74a...ab93` | `LONG` | 1,504,197.23 USD | `15,536.82` | `64.06` | `96.75` | `54.88` | 508,968.39 USD | `+33.84%` | `5X Isolated` |
| `1475` | `0x5f10...d49d` | `LONG` | 1,452,735.00 USD | `15,000.00` | `96.35` | `96.75` | `72.01` | 7,433.84 USD | `+0.51%` | `20X Cross` |
| `1476` | `0xb322...d51f` | `LONG` | 1,452,147.57 USD | `14,999.82` | `102.98` | `96.75` | `44.11` | -92,579.73 USD | `-6.38%` | `20X Cross` |
| `1525` | `0xffb2...5ed6` | `LONG` | 1,403,774.48 USD | `14,504.05` | `117.89` | `96.75` | `84.66` | -306,130.23 USD | `-21.81%` | `20X Cross` |
| `1553` | `0x0d6a...ca57` | `LONG` | 1,375,374.20 USD | `14,206.65` | `110.41` | `96.75` | `91.60` | -193,216.16 USD | `-14.05%` | `5X Isolated` |
| `1763` | `0x2814...9b08` | `LONG` | 1,167,006.63 USD | `12,061.71` | `96.37` | `96.75` | `93.93` | 4,667.88 USD | `+0.40%` | `20X Isolated` |
| `1820` | `0x2577...4897` | `LONG` | 1,133,496.56 USD | `11,711.49` | `96.60` | `96.75` | `0.000000` | 2,136.90 USD | `+0.19%` | `15X Cross` |
| `1846` | `0x7808...6e70` | `SHORT` | 1,111,892.21 USD | `11,488.27` | `97.15` | `96.75` | `152.29` | 4,170.01 USD | `+0.38%` | `10X Cross` |
| `1859` | `0x2482...0e55` | `LONG` | 1,099,987.81 USD | `11,363.98` | `122.03` | `96.75` | `88.83` | -286,714.12 USD | `-26.07%` | `20X Isolated` |
| `1889` | `0x45db...86eb` | `LONG` | 1,074,202.50 USD | `11,100.00` | `110.69` | `96.75` | `69.28` | -154,479.40 USD | `-14.38%` | `5X Cross` |
| `1897` | `0xe863...8bb8` | `SHORT` | 1,062,172.82 USD | `10,978.19` | `97.06` | `96.75` | `261.08` | 3,400.37 USD | `+0.32%` | `20X Cross` |
| `1916` | `0x1d04...7c43` | `LONG` | 1,046,740.54 USD | `10,811.76` | `111.55` | `96.75` | `17.17` | -159,320.95 USD | `-15.22%` | `6X Cross` |
| `1932` | `0x34e6...8d74` | `LONG` | 1,033,842.35 USD | `10,671.15` | `101.19` | `96.75` | `15.56` | -45,932.29 USD | `-4.44%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `7D` | `Long Liquidation` | `82.60` | 172,810,000.00 USD | 172,810,000.00 USD | 53,130.00 USD | 56,870.00 USD | 141,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `82.65` | 98,590.00 USD | 20,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.75` | 7,950.00 USD | 19,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `82.80` | 172,560,000.00 USD | 172,560,000.00 USD | 1,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `82.85` | 23,000.00 USD | 19,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.95` | 29,750.00 USD | 19,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.00` | 172,560,000.00 USD | 172,560,000.00 USD | 1,690.00 USD | 2,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.05` | 137,530.00 USD | 19,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.15` | 52,900.00 USD | 19,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.20` | 172,550,000.00 USD | 172,550,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.25` | 153,060.00 USD | 19,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.35` | 637,030.00 USD | 19,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.45` | 55,880.00 USD | 18,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.55` | 65,570.00 USD | 18,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.60` | 172,510,000.00 USD | 172,510,000.00 USD | 0.00 USD | 0.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.65` | 76,120.00 USD | 18,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.75` | 81,510.00 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.80` | 172,500,000.00 USD | 172,500,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.85` | 13,630.00 USD | 18,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.95` | 842,760.00 USD | 18,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.05` | 113,720.00 USD | 17,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.15` | 65,310.00 USD | 17,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.20` | 172,490,000.00 USD | 172,490,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.25` | 46,440.00 USD | 17,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.35` | 25,180.00 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.40` | 172,470,000.00 USD | 172,470,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.45` | 85,770.00 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.55` | 1,230,000.00 USD | 17,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.65` | 261,450.00 USD | 16,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.75` | 289,310.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.85` | 94,510.00 USD | 15,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.95` | 617.59 USD | 15,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.05` | 15,920.00 USD | 15,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.15` | 5,400.00 USD | 15,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.20` | 172,440,000.00 USD | 172,440,000.00 USD | 0.00 USD | 218,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.25` | 609,970.00 USD | 15,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.35` | 21,250.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.40` | 172,220,000.00 USD | 172,220,000.00 USD | 0.00 USD | 12,950.00 USD | 192,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.45` | 52,900.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.55` | 10,360.00 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.60` | 172,020,000.00 USD | 172,020,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.65` | 53,210.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.75` | 23,470.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.80` | 171,830,000.00 USD | 171,830,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.85` | 69,910.00 USD | 14,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.95` | 363,970.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.05` | 276,690.00 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.15` | 68,570.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.20` | 171,570,000.00 USD | 171,570,000.00 USD | 0.00 USD | 12,130.00 USD | 199,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.25` | 52,990.00 USD | 13,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.35` | 5,680.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.40` | 171,360,000.00 USD | 171,360,000.00 USD | 0.00 USD | 311,220.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.45` | 187,940.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.55` | 43,510.00 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.65` | 190,730.00 USD | 13,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.75` | 34,660.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.80` | 171,040,000.00 USD | 171,040,000.00 USD | 0.00 USD | 149,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.85` | 78,950.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.95` | 152,510.00 USD | 13,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.00` | 170,890,000.00 USD | 170,890,000.00 USD | 263,340.00 USD | 176,600.00 USD | 297,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.05` | 30,820.00 USD | 13,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.10` | 180,530,000.00 USD | 180,530,000.00 USD | 412,880.00 USD | 386,260.00 USD | 441,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.15` | 4,410.00 USD | 13,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.20` | 170,150,000.00 USD | 170,150,000.00 USD | 8,850.00 USD | 6,510.00 USD | 6,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.25` | 92,480.00 USD | 13,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.30` | 179,290,000.00 USD | 179,290,000.00 USD | 150,010.00 USD | 242,640.00 USD | 278,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.35` | 72,050.00 USD | 13,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.40` | 170,130,000.00 USD | 170,130,000.00 USD | 248,310.00 USD | 225,130.00 USD | 288,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.45` | 149,740.00 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.50` | 178,620,000.00 USD | 178,620,000.00 USD | 156,730.00 USD | 252,960.00 USD | 89,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.55` | 128,700.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.60` | 169,370,000.00 USD | 169,370,000.00 USD | 0.00 USD | 275,130.00 USD | 421,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.65` | 105,660.00 USD | 12,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.70` | 178,120,000.00 USD | 178,120,000.00 USD | 8,600.00 USD | 250,230.00 USD | 267,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.75` | 90,160.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.80` | 168,670,000.00 USD | 168,670,000.00 USD | 0.00 USD | 413,150.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.85` | 66,830.00 USD | 12,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.90` | 177,590,000.00 USD | 177,590,000.00 USD | 134,550.00 USD | 427,430.00 USD | 933,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.95` | 9,000.00 USD | 12,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.00` | 168,250,000.00 USD | 168,250,000.00 USD | 0.00 USD | 12,070.00 USD | 251,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.05` | 157,110.00 USD | 12,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.10` | 176,090,000.00 USD | 176,090,000.00 USD | 59,290.00 USD | 35,690.00 USD | 232,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.15` | 25,750.00 USD | 12,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.20` | 167,990,000.00 USD | 167,990,000.00 USD | 9,900.00 USD | 20,610.00 USD | 28,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.25` | 74,760.00 USD | 12,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.30` | 175,770,000.00 USD | 175,770,000.00 USD | 116,980.00 USD | 275,350.00 USD | 271,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.35` | 26,970.00 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.40` | 167,930,000.00 USD | 167,930,000.00 USD | 0.00 USD | 237,870.00 USD | 335,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.45` | 64,640.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.50` | 175,100,000.00 USD | 175,100,000.00 USD | 86,840.00 USD | 99,900.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.55` | 267,270.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.65` | 95,980.00 USD | 11,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.70` | 174,910,000.00 USD | 174,910,000.00 USD | 204,330.00 USD | 124,180.00 USD | 415,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.75` | 236,310.00 USD | 11,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.80` | 167,350,000.00 USD | 167,350,000.00 USD | 241,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.85` | 1,070,000.00 USD | 11,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.90` | 174,170,000.00 USD | 174,170,000.00 USD | 143,140.00 USD | 62,660.00 USD | 214,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.95` | 32,790.00 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.00` | 167,110,000.00 USD | 167,110,000.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.05` | 29,770.00 USD | 10,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.10` | 173,750,000.00 USD | 173,750,000.00 USD | 160,900.00 USD | 83,520.00 USD | 36,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.15` | 160,380.00 USD | 10,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.20` | 166,180,000.00 USD | 166,180,000.00 USD | 8,180.00 USD | 10,750.00 USD | 315,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.25` | 31,740.00 USD | 10,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.30` | 173,470,000.00 USD | 173,470,000.00 USD | 221,290.00 USD | 284,680.00 USD | 1,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.35` | 29,540.00 USD | 10,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.40` | 165,850,000.00 USD | 165,850,000.00 USD | 697,470.00 USD | 26,220.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.45` | 429,190.00 USD | 10,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.50` | 172,960,000.00 USD | 172,960,000.00 USD | 4,870.00 USD | 50,620.00 USD | 273,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.55` | 39,790.00 USD | 9,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.60` | 164,960,000.00 USD | 164,960,000.00 USD | 684,220.00 USD | 270,260.00 USD | 723,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.65` | 17,750.00 USD | 9,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.70` | 172,630,000.00 USD | 172,630,000.00 USD | 133,580.00 USD | 30,600.00 USD | 428,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.75` | 146,450.00 USD | 9,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.80` | 163,280,000.00 USD | 163,280,000.00 USD | 425,950.00 USD | 318,390.00 USD | 314,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.85` | 59,040.00 USD | 9,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.90` | 172,040,000.00 USD | 172,040,000.00 USD | 129,660.00 USD | 91,010.00 USD | 141,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.95` | 136,370.00 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.00` | 162,220,000.00 USD | 162,220,000.00 USD | 374,600.00 USD | 647,410.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.05` | 73,280.00 USD | 9,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.10` | 171,680,000.00 USD | 171,680,000.00 USD | 1,120,000.00 USD | 893,200.00 USD | 574,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.15` | 60,790.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.20` | 160,110,000.00 USD | 160,110,000.00 USD | 1,250,000.00 USD | 590,390.00 USD | 735,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.25` | 26,880.00 USD | 9,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.30` | 169,090,000.00 USD | 169,090,000.00 USD | 697,230.00 USD | 491,550.00 USD | 441,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.35` | 77,850.00 USD | 9,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.40` | 157,530,000.00 USD | 157,530,000.00 USD | 796,240.00 USD | 68,740.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.45` | 50,450.00 USD | 9,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.50` | 167,460,000.00 USD | 167,460,000.00 USD | 650,510.00 USD | 518,660.00 USD | 884,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.55` | 29,950.00 USD | 9,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.60` | 155,970,000.00 USD | 155,970,000.00 USD | 1,040,000.00 USD | 1,010,000.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.65` | 131,550.00 USD | 9,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.70` | 165,400,000.00 USD | 165,400,000.00 USD | 628,630.00 USD | 803,190.00 USD | 369,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.75` | 107,810.00 USD | 8,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.80` | 152,360,000.00 USD | 152,360,000.00 USD | 1,210,000.00 USD | 1,200,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.85` | 73,530.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.90` | 163,600,000.00 USD | 163,600,000.00 USD | 673,680.00 USD | 420,760.00 USD | 119,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.95` | 16,410.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.00` | 148,460,000.00 USD | 148,460,000.00 USD | 1,190,000.00 USD | 609,900.00 USD | 810,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.05` | 389,480.00 USD | 8,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.10` | 162,390,000.00 USD | 162,390,000.00 USD | 436,270.00 USD | 732,110.00 USD | 466,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.15` | 373,670.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.20` | 145,860,000.00 USD | 145,860,000.00 USD | 2,280,000.00 USD | 868,420.00 USD | 638,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.25` | 29,640.00 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.30` | 160,750,000.00 USD | 160,750,000.00 USD | 150,320.00 USD | 221,290.00 USD | 443,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.35` | 14,960.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.40` | 142,070,000.00 USD | 142,070,000.00 USD | 1,180,000.00 USD | 1,030,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.45` | 331,850.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.50` | 159,940,000.00 USD | 159,940,000.00 USD | 850,930.00 USD | 781,420.00 USD | 664,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.55` | 1,210,000.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.60` | 138,250,000.00 USD | 138,250,000.00 USD | 500,280.00 USD | 1,020,000.00 USD | 872,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.65` | 1,430,000.00 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.70` | 157,640,000.00 USD | 157,640,000.00 USD | 268,750.00 USD | 463,180.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.75` | 240,910.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.80` | 135,860,000.00 USD | 135,860,000.00 USD | 932,400.00 USD | 797,110.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.85` | 43,170.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.90` | 155,750,000.00 USD | 155,750,000.00 USD | 1,280,000.00 USD | 813,050.00 USD | 665,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.95` | 64,120.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.00` | 133,440,000.00 USD | 133,440,000.00 USD | 681,440.00 USD | 656,110.00 USD | 990,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.05` | 168,710.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.10` | 152,990,000.00 USD | 152,990,000.00 USD | 2,310,000.00 USD | 2,670,000.00 USD | 545,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.15` | 328,530.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.20` | 131,110,000.00 USD | 131,110,000.00 USD | 2,870,000.00 USD | 1,110,000.00 USD | 289,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.25` | 170,110.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.30` | 147,470,000.00 USD | 147,470,000.00 USD | 720,590.00 USD | 799,660.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.35` | 304,990.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.40` | 126,850,000.00 USD | 126,850,000.00 USD | 550,500.00 USD | 833,900.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.45` | 117,820.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.50` | 144,530,000.00 USD | 144,530,000.00 USD | 1,140,000.00 USD | 703,500.00 USD | 2,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.55` | 4,870.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.60` | 123,930,000.00 USD | 123,930,000.00 USD | 98,670.00 USD | 880,990.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.65` | 15,170.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.70` | 140,330,000.00 USD | 140,330,000.00 USD | 988,340.00 USD | 1,110,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.75` | 4,920.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.80` | 121,470,000.00 USD | 121,470,000.00 USD | 444,580.00 USD | 2,340,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.85` | 23,420.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.90` | 136,550,000.00 USD | 136,550,000.00 USD | 3,310,000.00 USD | 1,980,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.95` | 3,780.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.00` | 117,080,000.00 USD | 117,080,000.00 USD | 365,950.00 USD | 550,690.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.05` | 29,610.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.10` | 128,730,000.00 USD | 128,730,000.00 USD | 2,550,000.00 USD | 3,410,000.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.15` | 319,790.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.20` | 114,380,000.00 USD | 114,380,000.00 USD | 1,090,000.00 USD | 670,930.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.25` | 105,430.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.30` | 120,640,000.00 USD | 120,640,000.00 USD | 2,980,000.00 USD | 3,170,000.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.35` | 13,390.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.40` | 110,500,000.00 USD | 110,500,000.00 USD | 611,840.00 USD | 2,660,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.45` | 8,060.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.50` | 113,060,000.00 USD | 113,060,000.00 USD | 3,020,000.00 USD | 2,340,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.55` | 19,360.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.60` | 105,780,000.00 USD | 105,780,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.65` | 937,160.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.70` | 105,360,000.00 USD | 105,360,000.00 USD | 640,730.00 USD | 3,170,000.00 USD | 955,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.75` | 10,870.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.80` | 102,840,000.00 USD | 102,840,000.00 USD | 0.00 USD | 2,080,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.85` | 11,870.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.90` | 100,590,000.00 USD | 100,590,000.00 USD | 1,610,000.00 USD | 967,780.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.95` | 1,140,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.00` | 97,590,000.00 USD | 97,590,000.00 USD | 2,660,000.00 USD | 1,780,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.05` | 4,190.00 USD | 821,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.10` | 96,590,000.00 USD | 96,590,000.00 USD | 768,990.00 USD | 1,310,000.00 USD | 2,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.15` | 29,950.00 USD | 817,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.20` | 90,950,000.00 USD | 90,950,000.00 USD | 24,740.00 USD | 962,410.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.25` | 8,860.00 USD | 787,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.30` | 91,820,000.00 USD | 91,820,000.00 USD | 2,270,000.00 USD | 1,250,000.00 USD | 518,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.35` | 5,200.00 USD | 778,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.40` | 87,210,000.00 USD | 87,210,000.00 USD | 0.00 USD | 496,790.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.45` | 146,220.00 USD | 773,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.50` | 87,790,000.00 USD | 87,790,000.00 USD | 882,080.00 USD | 1,250,000.00 USD | 642,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.55` | 60,600.00 USD | 627,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.60` | 86,700,000.00 USD | 86,700,000.00 USD | 560,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `94.65` | 28,740.00 USD | 28,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.70` | 85,020,000.00 USD | 85,020,000.00 USD | 1,370,000.00 USD | 571,830.00 USD | 402,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.75` | 82,810.00 USD | 566,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.80` | 86,140,000.00 USD | 86,140,000.00 USD | 2,050,000.00 USD | 99,300.00 USD | 3,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.85` | 54,830.00 USD | 483,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.90` | 82,670,000.00 USD | 82,670,000.00 USD | 3,300,000.00 USD | 660,630.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.95` | 58,350.00 USD | 428,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.00` | 80,630,000.00 USD | 80,630,000.00 USD | 3,060,000.00 USD | 4,770,000.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.05` | 57,060.00 USD | 370,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.10` | 77,390,000.00 USD | 77,390,000.00 USD | 3,170,000.00 USD | 1,780,000.00 USD | 852,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.15` | 21,470.00 USD | 313,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.20` | 71,740,000.00 USD | 71,740,000.00 USD | 2,420,000.00 USD | 317,900.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.25` | 42,730.00 USD | 292,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.30` | 71,590,000.00 USD | 71,590,000.00 USD | 1,550,000.00 USD | 1,680,000.00 USD | 3,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.35` | 7,550.00 USD | 249,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.40` | 68,980,000.00 USD | 68,980,000.00 USD | 2,080,000.00 USD | 2,620,000.00 USD | 4,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.45` | 24,230.00 USD | 241,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.50` | 64,670,000.00 USD | 64,670,000.00 USD | 471,290.00 USD | 1,690,000.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.55` | 44,760.00 USD | 217,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.60` | 59,690,000.00 USD | 59,690,000.00 USD | 3,820,000.00 USD | 7,040,000.00 USD | 4,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.65` | 92,490.00 USD | 172,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.70` | 60,940,000.00 USD | 60,940,000.00 USD | 1,900,000.00 USD | 2,230,000.00 USD | 5,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.75` | 49,350.00 USD | 80,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.80` | 44,240,000.00 USD | 44,240,000.00 USD | 3,400,000.00 USD | 93,510.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.85` | 30,710.00 USD | 30,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.90` | 51,160,000.00 USD | 51,160,000.00 USD | 3,100,000.00 USD | 1,850,000.00 USD | 3,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.95` | 231.24 USD | 231.24 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `96.00` | 39,470,000.00 USD | 39,470,000.00 USD | 4,660,000.00 USD | 1,290,000.00 USD | 5,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.10` | 42,950,000.00 USD | 42,950,000.00 USD | 4,020,000.00 USD | 5,430,000.00 USD | 4,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.20` | 27,910,000.00 USD | 27,910,000.00 USD | 6,840,000.00 USD | 2,710,000.00 USD | 5,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.30` | 28,950,000.00 USD | 28,950,000.00 USD | 6,780,000.00 USD | 6,050,000.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.40` | 13,110,000.00 USD | 13,110,000.00 USD | 1,600,000.00 USD | 2,590,000.00 USD | 6,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.50` | 14,750,000.00 USD | 14,750,000.00 USD | 3,180,000.00 USD | 1,260,000.00 USD | 4,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.60` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.70` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 2,360,000.00 USD | 965,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.80` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 79,170.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.90` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 1,410,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.20` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.30` | 6,730.00 USD | 6,730.00 USD | 0.00 USD | 0.00 USD | 6,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.40` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 101,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.50` | 1,840,000.00 USD | 1,840,000.00 USD | 534,370.00 USD | 1,280,000.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.60` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 24,930.00 USD | 3,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.70` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.75` | 1,220.00 USD | 29,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `97.80` | 18,370,000.00 USD | 18,370,000.00 USD | 7,580,000.00 USD | 3,430,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.90` | 8,380,000.00 USD | 8,380,000.00 USD | 3,340,000.00 USD | 434,450.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.00` | 34,380,000.00 USD | 34,380,000.00 USD | 13,420,000.00 USD | 561,730.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.10` | 13,870,000.00 USD | 13,870,000.00 USD | 2,540,000.00 USD | 2,320,000.00 USD | 636,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.20` | 45,290,000.00 USD | 45,290,000.00 USD | 9,790,000.00 USD | 1,120,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.30` | 23,290,000.00 USD | 23,290,000.00 USD | 2,120,000.00 USD | 924,810.00 USD | 6,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.40` | 56,430,000.00 USD | 56,430,000.00 USD | 1,780,000.00 USD | 3,320,000.00 USD | 6,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.50` | 34,260,000.00 USD | 34,260,000.00 USD | 654,930.00 USD | 3,460,000.00 USD | 6,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.55` | 5,930.00 USD | 35,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `98.60` | 65,700,000.00 USD | 65,700,000.00 USD | 1,920,000.00 USD | 5,400,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.65` | 9,740.00 USD | 45,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.70` | 50,950,000.00 USD | 50,950,000.00 USD | 1,560,000.00 USD | 5,460,000.00 USD | 9,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.80` | 70,640,000.00 USD | 70,640,000.00 USD | 731,910.00 USD | 784,380.00 USD | 3,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.90` | 62,130,000.00 USD | 62,130,000.00 USD | 2,200,000.00 USD | 3,820,000.00 USD | 5,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.95` | 1,020.00 USD | 46,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.00` | 79,470,000.00 USD | 79,470,000.00 USD | 2,170,000.00 USD | 2,700,000.00 USD | 3,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.05` | 3,610.00 USD | 50,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.10` | 77,520,000.00 USD | 77,520,000.00 USD | 3,520,000.00 USD | 6,260,000.00 USD | 5,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.15` | 1,110,000.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.20` | 93,450,000.00 USD | 93,450,000.00 USD | 1,220,000.00 USD | 6,520,000.00 USD | 6,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.25` | 72,450.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.30` | 87,060,000.00 USD | 87,060,000.00 USD | 3,670,000.00 USD | 3,420,000.00 USD | 2,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.35` | 92,510.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.40` | 94,480,000.00 USD | 94,480,000.00 USD | 0.00 USD | 1,010,000.00 USD | 25,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.45` | 19,710.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.50` | 92,400,000.00 USD | 92,400,000.00 USD | 1,560,000.00 USD | 2,990,000.00 USD | 797,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.55` | 138,120.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.60` | 99,910,000.00 USD | 99,910,000.00 USD | 2,240,000.00 USD | 2,640,000.00 USD | 545,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.65` | 9,360.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.70` | 115,430,000.00 USD | 115,430,000.00 USD | 4,400,000.00 USD | 7,410,000.00 USD | 11,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.75` | 33,470.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.80` | 103,250,000.00 USD | 103,250,000.00 USD | 736,270.00 USD | 1,330,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.85` | 883.67 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.90` | 124,240,000.00 USD | 124,240,000.00 USD | 857,690.00 USD | 1,960,000.00 USD | 5,990,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.95` | 4,010.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.00` | 114,570,000.00 USD | 114,570,000.00 USD | 2,220,000.00 USD | 2,310,000.00 USD | 6,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.05` | 36,990.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.10` | 131,440,000.00 USD | 131,440,000.00 USD | 2,200,000.00 USD | 3,440,000.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.15` | 25,710.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.20` | 120,660,000.00 USD | 120,660,000.00 USD | 843,770.00 USD | 2,460,000.00 USD | 2,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.25` | 347,460.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.30` | 137,000,000.00 USD | 137,000,000.00 USD | 734,910.00 USD | 2,120,000.00 USD | 2,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.35` | 391,910.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.40` | 125,140,000.00 USD | 125,140,000.00 USD | 993,830.00 USD | 654,600.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.45` | 26,900.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.50` | 144,670,000.00 USD | 144,670,000.00 USD | 2,200,000.00 USD | 1,260,000.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.55` | 1,510.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.60` | 130,940,000.00 USD | 130,940,000.00 USD | 2,130,000.00 USD | 1,450,000.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.65` | 101,930.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.70` | 152,440,000.00 USD | 152,440,000.00 USD | 2,230,000.00 USD | 2,360,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.75` | 19,590.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.80` | 133,670,000.00 USD | 133,670,000.00 USD | 821,420.00 USD | 1,380,000.00 USD | 530,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.85` | 62,360.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.90` | 159,520,000.00 USD | 159,520,000.00 USD | 2,270,000.00 USD | 2,600,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.95` | 498.69 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.00` | 152,640,000.00 USD | 152,640,000.00 USD | 4,160,000.00 USD | 7,060,000.00 USD | 7,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.05` | 698.26 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.10` | 173,120,000.00 USD | 173,120,000.00 USD | 8,090,000.00 USD | 2,820,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.15` | 12,940.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.20` | 172,050,000.00 USD | 172,050,000.00 USD | 7,240,000.00 USD | 5,320,000.00 USD | 6,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.25` | 769.50 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.30` | 183,460,000.00 USD | 183,460,000.00 USD | 3,550,000.00 USD | 3,910,000.00 USD | 2,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.40` | 189,110,000.00 USD | 189,110,000.00 USD | 4,720,000.00 USD | 1,270,000.00 USD | 11,070,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.45` | 118.70 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.50` | 198,970,000.00 USD | 198,970,000.00 USD | 3,140,000.00 USD | 3,660,000.00 USD | 8,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.55` | 2,790.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.60` | 199,630,000.00 USD | 199,630,000.00 USD | 3,650,000.00 USD | 30,170.00 USD | 6,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.65` | 3,870.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.70` | 208,780,000.00 USD | 208,780,000.00 USD | 2,220,000.00 USD | 881,090.00 USD | 6,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.80` | 209,550,000.00 USD | 209,550,000.00 USD | 3,050,000.00 USD | 609,510.00 USD | 6,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.90` | 214,610,000.00 USD | 214,610,000.00 USD | 2,320,000.00 USD | 1,290,000.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.95` | 1,760.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.00` | 215,550,000.00 USD | 215,550,000.00 USD | 1,830,000.00 USD | 1,470,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.05` | 4,280.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.10` | 221,070,000.00 USD | 221,070,000.00 USD | 2,960,000.00 USD | 1,440,000.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.15` | 719.14 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.20` | 222,270,000.00 USD | 222,270,000.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.25` | 1,170.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.30` | 225,840,000.00 USD | 225,840,000.00 USD | 1,740,000.00 USD | 1,400,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.40` | 227,580,000.00 USD | 227,580,000.00 USD | 2,340,000.00 USD | 304,350.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.50` | 230,160,000.00 USD | 230,160,000.00 USD | 1,510,000.00 USD | 785,070.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.55` | 6,330.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.60` | 230,040,000.00 USD | 230,040,000.00 USD | 1,450,000.00 USD | 979,270.00 USD | 33,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.65` | 1,500.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.70` | 232,050,000.00 USD | 232,050,000.00 USD | 1,110,000.00 USD | 661,840.00 USD | 123,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.75` | 3,240.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.80` | 238,130,000.00 USD | 238,130,000.00 USD | 7,780,000.00 USD | 23,810.00 USD | 286,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.90` | 236,580,000.00 USD | 236,580,000.00 USD | 1,510,000.00 USD | 1,530,000.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.95` | 4,150.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.00` | 255,060,000.00 USD | 255,060,000.00 USD | 12,270,000.00 USD | 394,420.00 USD | 4,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.05` | 692.50 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.10` | 241,550,000.00 USD | 241,550,000.00 USD | 2,380,000.00 USD | 1,360,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.15` | 11,000.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.20` | 267,740,000.00 USD | 267,740,000.00 USD | 11,620,000.00 USD | 140,550.00 USD | 913,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.25` | 863.17 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.30` | 243,370,000.00 USD | 243,370,000.00 USD | 334,720.00 USD | 717,010.00 USD | 770,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.35` | 385.50 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.40` | 282,310,000.00 USD | 282,310,000.00 USD | 11,050,000.00 USD | 233,330.00 USD | 3,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.45` | 3,300.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.50` | 249,950,000.00 USD | 249,950,000.00 USD | 1,770,000.00 USD | 1,090,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.60` | 300,700,000.00 USD | 300,700,000.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.65` | 4,360.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.70` | 254,660,000.00 USD | 254,660,000.00 USD | 1,370,000.00 USD | 720,260.00 USD | 2,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.75` | 261,050.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.80` | 313,080,000.00 USD | 313,080,000.00 USD | 7,960,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.85` | 13,560.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.90` | 258,470,000.00 USD | 258,470,000.00 USD | 1,370,000.00 USD | 1,640,000.00 USD | 801,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.95` | 827.44 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.00` | 339,790,000.00 USD | 339,790,000.00 USD | 10,830,000.00 USD | 7,160,000.00 USD | 8,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.05` | 775.17 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.10` | 263,580,000.00 USD | 263,580,000.00 USD | 2,180,000.00 USD | 748,620.00 USD | 2,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.15` | 4,830.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.20` | 361,810,000.00 USD | 361,810,000.00 USD | 8,520,000.00 USD | 7,230,000.00 USD | 6,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.25` | 41,100.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.30` | 266,880,000.00 USD | 266,880,000.00 USD | 1,160,000.00 USD | 1,150,000.00 USD | 985,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.35` | 11,630.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.40` | 379,000,000.00 USD | 379,000,000.00 USD | 5,100,000.00 USD | 3,710,000.00 USD | 8,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.45` | 8,550.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.50` | 270,590,000.00 USD | 270,590,000.00 USD | 1,350,000.00 USD | 1,140,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.55` | 575.03 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.60` | 396,750,000.00 USD | 396,750,000.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 7,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.65` | 401.86 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.70` | 276,360,000.00 USD | 276,360,000.00 USD | 1,690,000.00 USD | 982,920.00 USD | 3,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.75` | 3,620.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.80` | 414,140,000.00 USD | 414,140,000.00 USD | 5,170,000.00 USD | 4,410,000.00 USD | 7,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.90` | 277,830,000.00 USD | 277,830,000.00 USD | 486,940.00 USD | 283,560.00 USD | 703,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.95` | 126,400.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.00` | 430,300,000.00 USD | 430,300,000.00 USD | 5,730,000.00 USD | 4,110,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.05` | 578.83 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.10` | 279,670,000.00 USD | 279,670,000.00 USD | 299,230.00 USD | 436,680.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.15` | 19,740.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.20` | 440,970,000.00 USD | 440,970,000.00 USD | 5,340,000.00 USD | 2,800,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.25` | 2,110.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.30` | 279,860,000.00 USD | 279,860,000.00 USD | 94,380.00 USD | 96,460.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.35` | 6,840.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.40` | 449,180,000.00 USD | 449,180,000.00 USD | 1,570,000.00 USD | 3,170,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.45` | 531,450.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.50` | 280,470,000.00 USD | 280,470,000.00 USD | 245,610.00 USD | 180,000.00 USD | 187,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.55` | 4,180.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.60` | 457,610,000.00 USD | 457,610,000.00 USD | 3,700,000.00 USD | 2,270,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.65` | 3,540.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.70` | 280,690,000.00 USD | 280,690,000.00 USD | 65,040.00 USD | 150,210.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.80` | 466,420,000.00 USD | 466,420,000.00 USD | 2,690,000.00 USD | 2,620,000.00 USD | 3,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.85` | 91,370.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.90` | 281,740,000.00 USD | 281,740,000.00 USD | 171,160.00 USD | 683,690.00 USD | 192,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.95` | 840.18 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.00` | 471,570,000.00 USD | 471,570,000.00 USD | 1,970,000.00 USD | 1,050,000.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.05` | 33,380.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.10` | 283,130,000.00 USD | 283,130,000.00 USD | 706,860.00 USD | 457,510.00 USD | 222,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.15` | 5,820.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.20` | 480,460,000.00 USD | 480,460,000.00 USD | 3,820,000.00 USD | 2,560,000.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.30` | 284,290,000.00 USD | 284,290,000.00 USD | 283,710.00 USD | 484,380.00 USD | 395,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.35` | 252,430.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.40` | 486,520,000.00 USD | 486,520,000.00 USD | 2,420,000.00 USD | 2,170,000.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.45` | 33,200.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.50` | 285,120,000.00 USD | 285,120,000.00 USD | 323,470.00 USD | 246,080.00 USD | 256,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.55` | 218.43 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.60` | 491,360,000.00 USD | 491,360,000.00 USD | 1,330,000.00 USD | 1,250,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.65` | 6,460.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.70` | 287,490,000.00 USD | 287,490,000.00 USD | 654,410.00 USD | 284,770.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.80` | 496,020,000.00 USD | 496,020,000.00 USD | 999,190.00 USD | 927,000.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.85` | 479,570.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.90` | 288,310,000.00 USD | 288,310,000.00 USD | 156,730.00 USD | 336,790.00 USD | 325,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.95` | 131.55 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.00` | 500,160,000.00 USD | 500,160,000.00 USD | 527,980.00 USD | 1,180,000.00 USD | 2,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.05` | 14,820.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.10` | 289,380,000.00 USD | 289,380,000.00 USD | 97,170.00 USD | 368,740.00 USD | 600,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.15` | 3,060.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.20` | 501,250,000.00 USD | 501,250,000.00 USD | 230,020.00 USD | 507,570.00 USD | 352,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.25` | 46,610.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.30` | 289,710,000.00 USD | 289,710,000.00 USD | 60,260.00 USD | 159,710.00 USD | 110,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.35` | 766.48 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.40` | 290,160,000.00 USD | 290,160,000.00 USD | 0.00 USD | 41,740.00 USD | 408,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.40` | 502,530,000.00 USD | 502,530,000.00 USD | 0.00 USD | 576,040.00 USD | 709,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.45` | 32,580.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.55` | 221.55 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.60` | 503,160,000.00 USD | 503,160,000.00 USD | 213,520.00 USD | 12,070.00 USD | 406,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.75` | 150,290.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.80` | 504,000,000.00 USD | 504,000,000.00 USD | 499,550.00 USD | 31,020.00 USD | 305,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.85` | 143,860.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.00` | 504,580,000.00 USD | 504,580,000.00 USD | 5,950.00 USD | 237,870.00 USD | 335,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.05` | 1,080.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.15` | 1,150.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.20` | 504,860,000.00 USD | 504,860,000.00 USD | 0.00 USD | 205,080.00 USD | 74,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.25` | 161,430.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.35` | 3,470.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.40` | 505,350,000.00 USD | 505,350,000.00 USD | 487,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.45` | 108,080.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.55` | 261.61 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.60` | 505,530,000.00 USD | 505,530,000.00 USD | 17,470.00 USD | 167,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.65` | 7,980.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.80` | 506,470,000.00 USD | 506,470,000.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.85` | 41,550.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.95` | 3,170.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.00` | 506,760,000.00 USD | 506,760,000.00 USD | 8,180.00 USD | 0.00 USD | 286,720.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `19.45` | 123,110,000.00 USD | 0.00 USD | 11,880.00 USD | `-79.96%` | `610.74` |
| `Live` | `Long` | `19.65` | 123,100,000.00 USD | 0.00 USD | 55,020.00 USD | `-79.75%` | `2,800.00` |
| `Live` | `Long` | `19.85` | 123,040,000.00 USD | 0.00 USD | 468.46 USD | `-79.55%` | `23.60` |
| `Live` | `Long` | `19.95` | 123,040,000.00 USD | 0.00 USD | 379.05 USD | `-79.44%` | `19.00` |
| `Live` | `Long` | `20.25` | 123,040,000.00 USD | 0.00 USD | 167.26 USD | `-79.14%` | `8.26` |
| `Live` | `Long` | `20.55` | 123,040,000.00 USD | 0.00 USD | 4,790.00 USD | `-78.83%` | `233.31` |
| `Live` | `Long` | `20.65` | 123,040,000.00 USD | 0.00 USD | 748.56 USD | `-78.72%` | `36.25` |
| `Live` | `Long` | `21.15` | 123,030,000.00 USD | 0.00 USD | 994.47 USD | `-78.21%` | `47.02` |
| `Live` | `Long` | `21.35` | 123,030,000.00 USD | 0.00 USD | 3,470.00 USD | `-78.00%` | `162.52` |
| `Live` | `Long` | `21.45` | 123,030,000.00 USD | 0.00 USD | 161.73 USD | `-77.90%` | `7.54` |
| `Live` | `Long` | `21.65` | 123,030,000.00 USD | 0.00 USD | 631.10 USD | `-77.69%` | `29.15` |
| `Live` | `Long` | `21.75` | 123,030,000.00 USD | 0.00 USD | 4,630.00 USD | `-77.59%` | `212.70` |
| `Live` | `Long` | `21.95` | 123,020,000.00 USD | 0.00 USD | 1,800.00 USD | `-77.38%` | `82.04` |
| `Live` | `Long` | `22.05` | 123,020,000.00 USD | 0.00 USD | 1,080.00 USD | `-77.28%` | `49.01` |
| `Live` | `Long` | `22.35` | 123,020,000.00 USD | 0.00 USD | 5,040.00 USD | `-76.97%` | `225.60` |
| `Live` | `Long` | `22.45` | 123,020,000.00 USD | 0.00 USD | 8,570.00 USD | `-76.87%` | `381.58` |
| `Live` | `Long` | `22.95` | 123,010,000.00 USD | 0.00 USD | 1,150.00 USD | `-76.35%` | `50.00` |
| `Live` | `Long` | `23.05` | 123,010,000.00 USD | 0.00 USD | 114.10 USD | `-76.25%` | `4.95` |
| `Live` | `Long` | `23.15` | 123,010,000.00 USD | 0.00 USD | 1,010.00 USD | `-76.15%` | `43.60` |
| `Live` | `Long` | `23.45` | 123,010,000.00 USD | 0.00 USD | 1,380.00 USD | `-75.84%` | `58.86` |
| `Live` | `Long` | `23.65` | 123,000,000.00 USD | 0.00 USD | 619.16 USD | `-75.63%` | `26.18` |
| `Live` | `Long` | `23.75` | 123,000,000.00 USD | 0.00 USD | 1,190.00 USD | `-75.53%` | `50.00` |
| `Live` | `Long` | `23.95` | 123,000,000.00 USD | 0.00 USD | 1,120.00 USD | `-75.32%` | `46.58` |
| `Live` | `Long` | `24.05` | 123,000,000.00 USD | 0.00 USD | 8,870.00 USD | `-75.22%` | `369.00` |
| `Live` | `Long` | `24.25` | 122,990,000.00 USD | 0.00 USD | 10,230.00 USD | `-75.01%` | `422.03` |
| `Live` | `Long` | `24.35` | 122,980,000.00 USD | 0.00 USD | 878,940.00 USD | `-74.91%` | `36,095.99` |
| `Live` | `Long` | `24.85` | 122,100,000.00 USD | 0.00 USD | 12,430.00 USD | `-74.40%` | `500.00` |
| `Live` | `Long` | `24.95` | 122,090,000.00 USD | 0.00 USD | 160.43 USD | `-74.29%` | `6.43` |
| `Live` | `Long` | `25.05` | 122,090,000.00 USD | 0.00 USD | 2,640.00 USD | `-74.19%` | `105.27` |
| `Live` | `Long` | `25.15` | 122,090,000.00 USD | 0.00 USD | 2,010.00 USD | `-74.09%` | `80.00` |
| `Live` | `Long` | `25.25` | 122,090,000.00 USD | 0.00 USD | 4,660.00 USD | `-73.98%` | `184.67` |
| `Live` | `Long` | `25.45` | 122,080,000.00 USD | 0.00 USD | 106.64 USD | `-73.78%` | `4.19` |
| `Live` | `Long` | `25.55` | 122,080,000.00 USD | 0.00 USD | 2,760.00 USD | `-73.67%` | `108.12` |
| `Live` | `Long` | `25.85` | 122,080,000.00 USD | 0.00 USD | 148,650.00 USD | `-73.37%` | `5,750.44` |
| `Live` | `Long` | `25.95` | 121,930,000.00 USD | 0.00 USD | 2,930.00 USD | `-73.26%` | `113.00` |
| `Live` | `Long` | `26.05` | 121,930,000.00 USD | 0.00 USD | 5,210.00 USD | `-73.16%` | `200.00` |
| `Live` | `Long` | `26.15` | 121,920,000.00 USD | 0.00 USD | 1,620.00 USD | `-73.06%` | `62.00` |
| `Live` | `Long` | `26.25` | 121,920,000.00 USD | 0.00 USD | 22,600.00 USD | `-72.95%` | `861.04` |
| `Live` | `Long` | `26.55` | 121,900,000.00 USD | 0.00 USD | 478.70 USD | `-72.64%` | `18.03` |
| `Live` | `Long` | `26.65` | 121,900,000.00 USD | 0.00 USD | 265.17 USD | `-72.54%` | `9.95` |
| `Live` | `Long` | `26.95` | 121,900,000.00 USD | 0.00 USD | 11,420.00 USD | `-72.23%` | `423.77` |
| `Live` | `Long` | `27.25` | 121,890,000.00 USD | 0.00 USD | 5,450.00 USD | `-71.92%` | `200.00` |
| `Live` | `Long` | `27.35` | 121,880,000.00 USD | 0.00 USD | 332.30 USD | `-71.82%` | `12.15` |
| `Live` | `Long` | `27.45` | 121,880,000.00 USD | 0.00 USD | 982.98 USD | `-71.72%` | `35.81` |
| `Live` | `Long` | `27.85` | 121,880,000.00 USD | 0.00 USD | 808.21 USD | `-71.30%` | `29.02` |
| `Live` | `Long` | `27.95` | 121,880,000.00 USD | 0.00 USD | 747.10 USD | `-71.20%` | `26.73` |
| `Live` | `Long` | `28.05` | 121,880,000.00 USD | 0.00 USD | 2,740.00 USD | `-71.10%` | `97.63` |
| `Live` | `Long` | `28.35` | 121,870,000.00 USD | 0.00 USD | 6,330.00 USD | `-70.79%` | `223.13` |
| `Live` | `Long` | `28.45` | 121,870,000.00 USD | 0.00 USD | 113.80 USD | `-70.69%` | `4.00` |
| `Live` | `Long` | `28.75` | 121,870,000.00 USD | 0.00 USD | 86,250.00 USD | `-70.38%` | `3,000.00` |
| `Live` | `Long` | `28.85` | 121,780,000.00 USD | 0.00 USD | 721.25 USD | `-70.27%` | `25.00` |
| `Live` | `Long` | `29.15` | 121,780,000.00 USD | 0.00 USD | 9,910.00 USD | `-69.97%` | `340.00` |
| `Live` | `Long` | `29.25` | 121,770,000.00 USD | 0.00 USD | 150.93 USD | `-69.86%` | `5.16` |
| `Live` | `Long` | `29.35` | 121,770,000.00 USD | 0.00 USD | 15,380.00 USD | `-69.76%` | `523.99` |
| `Live` | `Long` | `29.45` | 121,760,000.00 USD | 0.00 USD | 18,410.00 USD | `-69.66%` | `625.00` |
| `Live` | `Long` | `29.55` | 121,740,000.00 USD | 0.00 USD | 2,940.00 USD | `-69.55%` | `99.64` |
| `Live` | `Long` | `29.65` | 121,730,000.00 USD | 0.00 USD | 44,480.00 USD | `-69.45%` | `1,500.00` |
| `Live` | `Long` | `29.85` | 121,690,000.00 USD | 0.00 USD | 10,070.00 USD | `-69.24%` | `337.19` |
| `Live` | `Long` | `29.95` | 121,680,000.00 USD | 0.00 USD | 1,430.00 USD | `-69.14%` | `47.80` |
| `Live` | `Long` | `30.05` | 121,680,000.00 USD | 0.00 USD | 3,010.00 USD | `-69.04%` | `100.04` |
| `Live` | `Long` | `30.15` | 121,680,000.00 USD | 0.00 USD | 47,340.00 USD | `-68.94%` | `1,570.00` |
| `Live` | `Long` | `30.45` | 121,630,000.00 USD | 0.00 USD | 4,240.00 USD | `-68.63%` | `139.36` |
| `Live` | `Long` | `30.55` | 121,620,000.00 USD | 0.00 USD | 889.01 USD | `-68.52%` | `29.10` |
| `Live` | `Long` | `30.65` | 121,620,000.00 USD | 0.00 USD | 233.86 USD | `-68.42%` | `7.63` |
| `Live` | `Long` | `30.75` | 121,620,000.00 USD | 0.00 USD | 450.80 USD | `-68.32%` | `14.66` |
| `Live` | `Long` | `30.85` | 121,620,000.00 USD | 0.00 USD | 157.64 USD | `-68.21%` | `5.11` |
| `Live` | `Long` | `31.05` | 121,620,000.00 USD | 0.00 USD | 3,380.00 USD | `-68.01%` | `108.86` |
| `Live` | `Long` | `31.25` | 121,620,000.00 USD | 0.00 USD | 1,340.00 USD | `-67.80%` | `42.78` |
| `Live` | `Long` | `31.35` | 121,620,000.00 USD | 0.00 USD | 35,160.00 USD | `-67.70%` | `1,121.64` |
| `Live` | `Long` | `31.45` | 121,580,000.00 USD | 0.00 USD | 278.33 USD | `-67.60%` | `8.85` |
| `Live` | `Long` | `31.65` | 121,580,000.00 USD | 0.00 USD | 16,560.00 USD | `-67.39%` | `523.23` |
| `Live` | `Long` | `32.05` | 121,570,000.00 USD | 0.00 USD | 1,970.00 USD | `-66.98%` | `61.57` |
| `Live` | `Long` | `32.25` | 121,560,000.00 USD | 0.00 USD | 496.01 USD | `-66.77%` | `15.38` |
| `Live` | `Long` | `32.45` | 121,560,000.00 USD | 0.00 USD | 804.11 USD | `-66.57%` | `24.78` |
| `Live` | `Long` | `32.55` | 121,560,000.00 USD | 0.00 USD | 3,770.00 USD | `-66.46%` | `115.67` |
| `Live` | `Long` | `32.75` | 121,560,000.00 USD | 0.00 USD | 5,360.00 USD | `-66.26%` | `163.78` |
| `Live` | `Long` | `32.85` | 121,550,000.00 USD | 0.00 USD | 5,240.00 USD | `-66.15%` | `159.61` |
| `Live` | `Long` | `32.95` | 121,550,000.00 USD | 0.00 USD | 875.15 USD | `-66.05%` | `26.56` |
| `Live` | `Long` | `33.05` | 121,550,000.00 USD | 0.00 USD | 39,660.00 USD | `-65.95%` | `1,200.00` |
| `Live` | `Long` | `33.15` | 121,510,000.00 USD | 0.00 USD | 193.93 USD | `-65.84%` | `5.85` |
| `Live` | `Long` | `33.35` | 121,510,000.00 USD | 0.00 USD | 12,380.00 USD | `-65.64%` | `371.10` |
| `Live` | `Long` | `33.45` | 121,490,000.00 USD | 0.00 USD | 6,580.00 USD | `-65.54%` | `196.65` |
| `Live` | `Long` | `33.55` | 121,490,000.00 USD | 0.00 USD | 302.62 USD | `-65.43%` | `9.02` |
| `Live` | `Long` | `33.65` | 121,490,000.00 USD | 0.00 USD | 494.99 USD | `-65.33%` | `14.71` |
| `Live` | `Long` | `33.75` | 121,490,000.00 USD | 0.00 USD | 1,830.00 USD | `-65.23%` | `54.25` |
| `Live` | `Long` | `33.95` | 121,490,000.00 USD | 0.00 USD | 577,150.00 USD | `-65.02%` | `17,000.02` |
| `Live` | `Long` | `34.25` | 120,910,000.00 USD | 0.00 USD | 141.79 USD | `-64.71%` | `4.14` |
| `Live` | `Long` | `34.65` | 120,910,000.00 USD | 0.00 USD | 1,710.00 USD | `-64.30%` | `49.29` |
| `Live` | `Long` | `34.85` | 120,910,000.00 USD | 0.00 USD | 580.95 USD | `-64.09%` | `16.67` |
| `Live` | `Long` | `35.05` | 120,910,000.00 USD | 0.00 USD | 6,640,000.00 USD | `-63.89%` | `189,509.23` |
| `Live` | `Long` | `35.15` | 114,260,000.00 USD | 0.00 USD | 734.28 USD | `-63.78%` | `20.89` |
| `Live` | `Long` | `35.75` | 114,260,000.00 USD | 0.00 USD | 8,590.00 USD | `-63.17%` | `240.28` |
| `Live` | `Long` | `35.85` | 114,250,000.00 USD | 0.00 USD | 3,360.00 USD | `-63.06%` | `93.75` |
| `Live` | `Long` | `35.95` | 114,250,000.00 USD | 0.00 USD | 557.94 USD | `-62.96%` | `15.52` |
| `Live` | `Long` | `36.05` | 114,250,000.00 USD | 0.00 USD | 5,070.00 USD | `-62.86%` | `140.61` |
| `Live` | `Long` | `36.15` | 114,240,000.00 USD | 0.00 USD | 531.41 USD | `-62.75%` | `14.70` |
| `Live` | `Long` | `36.25` | 114,240,000.00 USD | 0.00 USD | 78,700.00 USD | `-62.65%` | `2,171.10` |
| `Live` | `Long` | `36.35` | 114,170,000.00 USD | 0.00 USD | 4,410.00 USD | `-62.55%` | `121.32` |
| `Live` | `Long` | `36.45` | 114,160,000.00 USD | 0.00 USD | 2,410.00 USD | `-62.44%` | `66.24` |
| `Live` | `Long` | `36.55` | 114,160,000.00 USD | 0.00 USD | 49,130.00 USD | `-62.34%` | `1,344.19` |
| `Live` | `Long` | `36.65` | 114,110,000.00 USD | 0.00 USD | 111,820.00 USD | `-62.24%` | `3,051.08` |
| `Live` | `Long` | `36.75` | 114,000,000.00 USD | 0.00 USD | 500.90 USD | `-62.13%` | `13.63` |
| `Live` | `Long` | `36.85` | 114,000,000.00 USD | 0.00 USD | 903.93 USD | `-62.03%` | `24.53` |
| `Live` | `Long` | `36.95` | 114,000,000.00 USD | 0.00 USD | 1,660.00 USD | `-61.93%` | `45.00` |
| `Live` | `Long` | `37.05` | 113,990,000.00 USD | 0.00 USD | 41,180.00 USD | `-61.83%` | `1,111.41` |
| `Live` | `Long` | `37.25` | 113,950,000.00 USD | 0.00 USD | 1,690.00 USD | `-61.62%` | `45.41` |
| `Live` | `Long` | `37.35` | 113,950,000.00 USD | 0.00 USD | 20,600.00 USD | `-61.52%` | `551.61` |
| `Live` | `Long` | `37.45` | 113,930,000.00 USD | 0.00 USD | 631.03 USD | `-61.41%` | `16.85` |
| `Live` | `Long` | `37.55` | 113,930,000.00 USD | 0.00 USD | 262.85 USD | `-61.31%` | `7.00` |
| `Live` | `Long` | `37.65` | 113,930,000.00 USD | 0.00 USD | 23,340.00 USD | `-61.21%` | `619.99` |
| `Live` | `Long` | `37.85` | 113,910,000.00 USD | 0.00 USD | 5,570.00 USD | `-61.00%` | `147.15` |
| `Live` | `Long` | `37.95` | 113,900,000.00 USD | 0.00 USD | 5,430.00 USD | `-60.90%` | `143.17` |
| `Live` | `Long` | `38.05` | 113,900,000.00 USD | 0.00 USD | 542.59 USD | `-60.80%` | `14.26` |
| `Live` | `Long` | `38.15` | 113,900,000.00 USD | 0.00 USD | 18,020.00 USD | `-60.69%` | `472.38` |
| `Live` | `Long` | `38.25` | 113,880,000.00 USD | 0.00 USD | 759.64 USD | `-60.59%` | `19.86` |
| `Live` | `Long` | `38.35` | 113,880,000.00 USD | 0.00 USD | 287.63 USD | `-60.49%` | `7.50` |
| `Live` | `Long` | `38.45` | 113,880,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-60.38%` | `78,000.00` |
| `Live` | `Long` | `38.55` | 110,880,000.00 USD | 0.00 USD | 116.04 USD | `-60.28%` | `3.01` |
| `Live` | `Long` | `38.75` | 110,880,000.00 USD | 0.00 USD | 736.64 USD | `-60.07%` | `19.01` |
| `Live` | `Long` | `38.85` | 110,880,000.00 USD | 0.00 USD | 4,270.00 USD | `-59.97%` | `109.96` |
| `Live` | `Long` | `38.95` | 110,870,000.00 USD | 0.00 USD | 195,360.00 USD | `-59.87%` | `5,015.60` |
| `Live` | `Long` | `39.05` | 110,680,000.00 USD | 0.00 USD | 50,470.00 USD | `-59.77%` | `1,292.50` |
| `Live` | `Long` | `39.15` | 110,630,000.00 USD | 0.00 USD | 1,710.00 USD | `-59.66%` | `43.67` |
| `Live` | `Long` | `39.35` | 110,620,000.00 USD | 0.00 USD | 45,040.00 USD | `-59.46%` | `1,144.66` |
| `Live` | `Long` | `39.45` | 110,580,000.00 USD | 0.00 USD | 4,500.00 USD | `-59.35%` | `113.97` |
| `Live` | `Long` | `39.65` | 110,580,000.00 USD | 0.00 USD | 3,400.00 USD | `-59.15%` | `85.66` |
| `Live` | `Long` | `39.75` | 110,570,000.00 USD | 0.00 USD | 159.00 USD | `-59.04%` | `4.00` |
| `Live` | `Long` | `39.85` | 110,570,000.00 USD | 0.00 USD | 1,870.00 USD | `-58.94%` | `46.86` |
| `Live` | `Long` | `39.95` | 110,570,000.00 USD | 0.00 USD | 16,520.00 USD | `-58.84%` | `413.53` |
| `Live` | `Long` | `40.05` | 110,550,000.00 USD | 0.00 USD | 905,320.00 USD | `-58.73%` | `22,604.67` |
| `Live` | `Long` | `40.15` | 109,650,000.00 USD | 0.00 USD | 3,500.00 USD | `-58.63%` | `87.27` |
| `Live` | `Long` | `40.25` | 109,640,000.00 USD | 0.00 USD | 12,710.00 USD | `-58.53%` | `315.72` |
| `Live` | `Long` | `40.55` | 109,630,000.00 USD | 0.00 USD | 3,160.00 USD | `-58.22%` | `77.90` |
| `Live` | `Long` | `40.85` | 109,630,000.00 USD | 0.00 USD | 12,400.00 USD | `-57.91%` | `303.63` |
| `Live` | `Long` | `40.95` | 109,620,000.00 USD | 0.00 USD | 142.10 USD | `-57.81%` | `3.47` |
| `Live` | `Long` | `41.05` | 109,620,000.00 USD | 0.00 USD | 6,760.00 USD | `-57.70%` | `164.69` |
| `Live` | `Long` | `41.15` | 109,610,000.00 USD | 0.00 USD | 53,750.00 USD | `-57.60%` | `1,306.08` |
| `Live` | `Long` | `41.25` | 109,560,000.00 USD | 0.00 USD | 368.36 USD | `-57.50%` | `8.93` |
| `Live` | `Long` | `41.35` | 109,560,000.00 USD | 0.00 USD | 148.45 USD | `-57.40%` | `3.59` |
| `Live` | `Long` | `41.55` | 109,560,000.00 USD | 0.00 USD | 489.04 USD | `-57.19%` | `11.77` |
| `Live` | `Long` | `41.65` | 109,550,000.00 USD | 0.00 USD | 24,190.00 USD | `-57.09%` | `580.75` |
| `Live` | `Long` | `41.75` | 109,530,000.00 USD | 0.00 USD | 2,160.00 USD | `-56.98%` | `51.71` |
| `Live` | `Long` | `41.85` | 109,530,000.00 USD | 0.00 USD | 3,060.00 USD | `-56.88%` | `73.03` |
| `Live` | `Long` | `41.95` | 109,530,000.00 USD | 0.00 USD | 48,400.00 USD | `-56.78%` | `1,153.84` |
| `Live` | `Long` | `42.05` | 109,480,000.00 USD | 0.00 USD | 470.12 USD | `-56.67%` | `11.18` |
| `Live` | `Long` | `42.15` | 109,480,000.00 USD | 0.00 USD | 4,170.00 USD | `-56.57%` | `99.02` |
| `Live` | `Long` | `42.25` | 109,470,000.00 USD | 0.00 USD | 6,500.00 USD | `-56.47%` | `153.75` |
| `Live` | `Long` | `42.35` | 109,470,000.00 USD | 0.00 USD | 198.62 USD | `-56.36%` | `4.69` |
| `Live` | `Long` | `42.45` | 109,470,000.00 USD | 0.00 USD | 19,900.00 USD | `-56.26%` | `468.86` |
| `Live` | `Long` | `42.55` | 109,450,000.00 USD | 0.00 USD | 8,210.00 USD | `-56.16%` | `193.00` |
| `Live` | `Long` | `42.85` | 109,440,000.00 USD | 0.00 USD | 44,250.00 USD | `-55.85%` | `1,032.68` |
| `Live` | `Long` | `42.95` | 109,390,000.00 USD | 0.00 USD | 355.20 USD | `-55.75%` | `8.27` |
| `Live` | `Long` | `43.25` | 109,390,000.00 USD | 0.00 USD | 1,730.00 USD | `-55.44%` | `40.00` |
| `Live` | `Long` | `43.35` | 109,390,000.00 USD | 0.00 USD | 12,030.00 USD | `-55.33%` | `277.49` |
| `Live` | `Long` | `43.45` | 109,380,000.00 USD | 0.00 USD | 440.15 USD | `-55.23%` | `10.13` |
| `Live` | `Long` | `43.65` | 109,380,000.00 USD | 0.00 USD | 740.74 USD | `-55.03%` | `16.97` |
| `Live` | `Long` | `43.75` | 109,380,000.00 USD | 0.00 USD | 725,070.00 USD | `-54.92%` | `16,572.97` |
| `Live` | `Long` | `43.85` | 108,650,000.00 USD | 0.00 USD | 326.24 USD | `-54.82%` | `7.44` |
| `Live` | `Long` | `43.95` | 108,650,000.00 USD | 0.00 USD | 11,790.00 USD | `-54.72%` | `268.15` |
| `Live` | `Long` | `44.05` | 108,640,000.00 USD | 0.00 USD | 13,420.00 USD | `-54.61%` | `304.69` |
| `Live` | `Long` | `44.25` | 108,630,000.00 USD | 0.00 USD | 366,420.00 USD | `-54.41%` | `8,280.65` |
| `Live` | `Long` | `44.35` | 108,260,000.00 USD | 0.00 USD | 8,630.00 USD | `-54.30%` | `194.56` |
| `Live` | `Long` | `44.45` | 108,250,000.00 USD | 0.00 USD | 10,180.00 USD | `-54.20%` | `229.02` |
| `Live` | `Long` | `44.55` | 108,240,000.00 USD | 0.00 USD | 17,870.00 USD | `-54.10%` | `401.03` |
| `Live` | `Long` | `44.65` | 108,220,000.00 USD | 0.00 USD | 2,240.00 USD | `-54.00%` | `50.24` |
| `Live` | `Long` | `44.75` | 108,220,000.00 USD | 0.00 USD | 1,790.00 USD | `-53.89%` | `39.98` |
| `Live` | `Long` | `44.85` | 108,220,000.00 USD | 0.00 USD | 477.20 USD | `-53.79%` | `10.64` |
| `Live` | `Long` | `44.95` | 108,220,000.00 USD | 0.00 USD | 6,510.00 USD | `-53.69%` | `144.85` |
| `Live` | `Long` | `45.15` | 108,210,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-53.48%` | `25,143.68` |
| `Live` | `Long` | `45.35` | 107,080,000.00 USD | 0.00 USD | 31,200.00 USD | `-53.27%` | `688.07` |
| `Live` | `Long` | `45.45` | 107,050,000.00 USD | 0.00 USD | 19,810.00 USD | `-53.17%` | `435.92` |
| `Live` | `Long` | `45.55` | 107,030,000.00 USD | 0.00 USD | 7,940.00 USD | `-53.07%` | `174.26` |
| `Live` | `Long` | `45.65` | 107,020,000.00 USD | 0.00 USD | 319.09 USD | `-52.96%` | `6.99` |
| `Live` | `Long` | `45.75` | 107,020,000.00 USD | 0.00 USD | 9,450.00 USD | `-52.86%` | `206.46` |
| `Live` | `Long` | `45.85` | 107,010,000.00 USD | 0.00 USD | 458.50 USD | `-52.76%` | `10.00` |
| `Live` | `Long` | `45.95` | 107,010,000.00 USD | 0.00 USD | 62,910.00 USD | `-52.66%` | `1,369.05` |
| `Live` | `Long` | `46.05` | 106,950,000.00 USD | 0.00 USD | 281.83 USD | `-52.55%` | `6.12` |
| `Live` | `Long` | `46.45` | 106,950,000.00 USD | 0.00 USD | 824.95 USD | `-52.14%` | `17.76` |
| `Live` | `Long` | `46.55` | 106,940,000.00 USD | 0.00 USD | 522.76 USD | `-52.04%` | `11.23` |
| `Live` | `Long` | `46.65` | 106,940,000.00 USD | 0.00 USD | 1,190.00 USD | `-51.93%` | `25.57` |
| `Live` | `Long` | `46.75` | 106,940,000.00 USD | 0.00 USD | 374.00 USD | `-51.83%` | `8.00` |
| `Live` | `Long` | `46.85` | 106,940,000.00 USD | 0.00 USD | 702.75 USD | `-51.73%` | `15.00` |
| `Live` | `Long` | `46.95` | 106,940,000.00 USD | 0.00 USD | 2,490.00 USD | `-51.63%` | `53.09` |
| `Live` | `Long` | `47.15` | 106,940,000.00 USD | 0.00 USD | 3,860,000.00 USD | `-51.42%` | `81,886.29` |
| `Live` | `Long` | `47.25` | 103,080,000.00 USD | 0.00 USD | 3,220.00 USD | `-51.32%` | `68.21` |
| `Live` | `Long` | `47.35` | 103,080,000.00 USD | 0.00 USD | 324.82 USD | `-51.21%` | `6.86` |
| `Live` | `Long` | `47.55` | 103,070,000.00 USD | 0.00 USD | 449.82 USD | `-51.01%` | `9.46` |
| `Live` | `Long` | `47.65` | 103,070,000.00 USD | 0.00 USD | 99,760.00 USD | `-50.90%` | `2,093.61` |
| `Live` | `Long` | `47.75` | 102,970,000.00 USD | 0.00 USD | 66,920.00 USD | `-50.80%` | `1,401.45` |
| `Live` | `Long` | `47.85` | 102,910,000.00 USD | 0.00 USD | 125.37 USD | `-50.70%` | `2.62` |
| `Live` | `Long` | `48.05` | 102,910,000.00 USD | 0.00 USD | 13,300.00 USD | `-50.49%` | `276.89` |
| `Live` | `Long` | `48.15` | 102,890,000.00 USD | 0.00 USD | 5,970.00 USD | `-50.39%` | `124.07` |
| `Live` | `Long` | `48.25` | 102,890,000.00 USD | 0.00 USD | 3,980.00 USD | `-50.29%` | `82.45` |
| `Live` | `Long` | `48.35` | 102,880,000.00 USD | 0.00 USD | 8,060.00 USD | `-50.18%` | `166.61` |
| `Live` | `Long` | `48.45` | 102,880,000.00 USD | 0.00 USD | 7,790.00 USD | `-50.08%` | `160.82` |
| `Live` | `Long` | `48.55` | 102,870,000.00 USD | 0.00 USD | 97,530.00 USD | `-49.98%` | `2,008.83` |
| `Live` | `Long` | `48.65` | 102,770,000.00 USD | 0.00 USD | 9,260.00 USD | `-49.87%` | `190.42` |
| `Live` | `Long` | `48.75` | 102,760,000.00 USD | 0.00 USD | 31,020.00 USD | `-49.77%` | `636.39` |
| `Live` | `Long` | `48.85` | 102,730,000.00 USD | 0.00 USD | 14,260.00 USD | `-49.67%` | `291.88` |
| `Live` | `Long` | `48.95` | 102,720,000.00 USD | 0.00 USD | 1,490.00 USD | `-49.56%` | `30.41` |
| `Live` | `Long` | `49.05` | 102,710,000.00 USD | 0.00 USD | 11,600.00 USD | `-49.46%` | `236.51` |
| `Live` | `Long` | `49.25` | 102,700,000.00 USD | 0.00 USD | 21,190.00 USD | `-49.26%` | `430.30` |
| `Live` | `Long` | `49.35` | 102,680,000.00 USD | 0.00 USD | 585.29 USD | `-49.15%` | `11.86` |
| `Live` | `Long` | `49.45` | 102,680,000.00 USD | 0.00 USD | 17,180.00 USD | `-49.05%` | `347.51` |
| `Live` | `Long` | `49.55` | 102,660,000.00 USD | 0.00 USD | 627.80 USD | `-48.95%` | `12.67` |
| `Live` | `Long` | `49.65` | 102,660,000.00 USD | 0.00 USD | 11,440.00 USD | `-48.84%` | `230.39` |
| `Live` | `Long` | `49.75` | 102,650,000.00 USD | 0.00 USD | 783,640.00 USD | `-48.74%` | `15,751.46` |
| `Live` | `Long` | `49.85` | 101,870,000.00 USD | 0.00 USD | 43,150.00 USD | `-48.64%` | `865.63` |
| `Live` | `Long` | `49.95` | 101,830,000.00 USD | 0.00 USD | 23,020.00 USD | `-48.53%` | `460.92` |
| `Live` | `Long` | `50.05` | 101,800,000.00 USD | 0.00 USD | 15,660.00 USD | `-48.43%` | `312.96` |
| `Live` | `Long` | `50.15` | 101,790,000.00 USD | 0.00 USD | 1,780.00 USD | `-48.33%` | `35.57` |
| `Live` | `Long` | `50.25` | 101,790,000.00 USD | 0.00 USD | 8,060.00 USD | `-48.23%` | `160.45` |
| `Live` | `Long` | `50.35` | 101,780,000.00 USD | 0.00 USD | 12,490.00 USD | `-48.12%` | `247.98` |
| `Live` | `Long` | `50.45` | 101,760,000.00 USD | 0.00 USD | 11,730.00 USD | `-48.02%` | `232.60` |
| `Live` | `Long` | `50.55` | 101,750,000.00 USD | 0.00 USD | 2,400.00 USD | `-47.92%` | `47.47` |
| `Live` | `Long` | `50.65` | 101,750,000.00 USD | 0.00 USD | 843.83 USD | `-47.81%` | `16.66` |
| `Live` | `Long` | `50.75` | 101,750,000.00 USD | 0.00 USD | 12,800.00 USD | `-47.71%` | `252.21` |
| `Live` | `Long` | `50.85` | 101,740,000.00 USD | 0.00 USD | 20,140.00 USD | `-47.61%` | `396.09` |
| `Live` | `Long` | `50.95` | 101,720,000.00 USD | 0.00 USD | 9,430.00 USD | `-47.50%` | `185.18` |
| `Live` | `Long` | `51.05` | 101,710,000.00 USD | 0.00 USD | 319,690.00 USD | `-47.40%` | `6,262.21` |
| `Live` | `Long` | `51.15` | 101,390,000.00 USD | 0.00 USD | 1,230,000.00 USD | `-47.30%` | `24,063.31` |
| `Live` | `Long` | `51.25` | 100,160,000.00 USD | 0.00 USD | 10,940.00 USD | `-47.19%` | `213.44` |
| `Live` | `Long` | `51.35` | 100,150,000.00 USD | 0.00 USD | 360.48 USD | `-47.09%` | `7.02` |
| `Live` | `Long` | `51.45` | 100,150,000.00 USD | 0.00 USD | 4,170.00 USD | `-46.99%` | `81.14` |
| `Live` | `Long` | `51.55` | 100,140,000.00 USD | 0.00 USD | 138,060.00 USD | `-46.89%` | `2,678.14` |
| `Live` | `Long` | `51.65` | 100,000,000.00 USD | 0.00 USD | 3,280.00 USD | `-46.78%` | `63.50` |
| `Live` | `Long` | `51.75` | 100,000,000.00 USD | 0.00 USD | 24,770.00 USD | `-46.68%` | `478.71` |
| `Live` | `Long` | `51.85` | 99,980,000.00 USD | 0.00 USD | 46,110.00 USD | `-46.58%` | `889.34` |
| `Live` | `Long` | `51.95` | 99,930,000.00 USD | 0.00 USD | 469,860.00 USD | `-46.47%` | `9,044.37` |
| `Live` | `Long` | `52.15` | 99,460,000.00 USD | 0.00 USD | 99,630.00 USD | `-46.27%` | `1,910.43` |
| `Live` | `Long` | `52.25` | 99,360,000.00 USD | 0.00 USD | 3,340.00 USD | `-46.16%` | `63.96` |
| `Live` | `Long` | `52.35` | 99,360,000.00 USD | 0.00 USD | 1,030.00 USD | `-46.06%` | `19.66` |
| `Live` | `Long` | `52.45` | 99,360,000.00 USD | 0.00 USD | 879.59 USD | `-45.96%` | `16.77` |
| `Live` | `Long` | `52.55` | 99,350,000.00 USD | 0.00 USD | 39,900.00 USD | `-45.86%` | `759.31` |
| `Live` | `Long` | `52.65` | 99,310,000.00 USD | 0.00 USD | 2,630.00 USD | `-45.75%` | `50.00` |
| `Live` | `Long` | `52.75` | 99,310,000.00 USD | 0.00 USD | 3,180.00 USD | `-45.65%` | `60.32` |
| `Live` | `Long` | `52.85` | 99,310,000.00 USD | 0.00 USD | 9,370.00 USD | `-45.55%` | `177.38` |
| `Live` | `Long` | `52.95` | 99,300,000.00 USD | 0.00 USD | 6,120.00 USD | `-45.44%` | `115.56` |
| `Live` | `Long` | `53.05` | 99,290,000.00 USD | 0.00 USD | 5,120.00 USD | `-45.34%` | `96.59` |
| `Live` | `Long` | `53.15` | 99,290,000.00 USD | 0.00 USD | 3,110.00 USD | `-45.24%` | `58.53` |
| `Live` | `Long` | `53.25` | 99,280,000.00 USD | 0.00 USD | 35,570.00 USD | `-45.13%` | `667.90` |
| `Live` | `Long` | `53.35` | 99,250,000.00 USD | 0.00 USD | 13,390.00 USD | `-45.03%` | `250.94` |
| `Live` | `Long` | `53.45` | 99,240,000.00 USD | 0.00 USD | 35,530.00 USD | `-44.93%` | `664.64` |
| `Live` | `Long` | `53.55` | 99,200,000.00 USD | 0.00 USD | 54,310.00 USD | `-44.83%` | `1,014.27` |
| `Live` | `Long` | `53.65` | 99,150,000.00 USD | 0.00 USD | 11,440.00 USD | `-44.72%` | `213.19` |
| `Live` | `Long` | `53.75` | 99,130,000.00 USD | 0.00 USD | 3,600.00 USD | `-44.62%` | `67.00` |
| `Live` | `Long` | `53.85` | 99,130,000.00 USD | 0.00 USD | 19,810.00 USD | `-44.52%` | `367.96` |
| `Live` | `Long` | `53.95` | 99,110,000.00 USD | 0.00 USD | 59,450.00 USD | `-44.41%` | `1,102.01` |
| `Live` | `Long` | `54.05` | 99,050,000.00 USD | 0.00 USD | 18,910.00 USD | `-44.31%` | `349.85` |
| `Live` | `Long` | `54.15` | 99,030,000.00 USD | 0.00 USD | 14,640.00 USD | `-44.21%` | `270.39` |
| `Live` | `Long` | `54.25` | 99,020,000.00 USD | 0.00 USD | 5,360.00 USD | `-44.10%` | `98.83` |
| `Live` | `Long` | `54.35` | 99,010,000.00 USD | 0.00 USD | 11,720.00 USD | `-44.00%` | `215.69` |
| `Live` | `Long` | `54.45` | 99,000,000.00 USD | 0.00 USD | 2,060.00 USD | `-43.90%` | `37.90` |
| `Live` | `Long` | `54.55` | 99,000,000.00 USD | 0.00 USD | 64,910.00 USD | `-43.79%` | `1,189.98` |
| `Live` | `Long` | `54.65` | 98,930,000.00 USD | 0.00 USD | 3,380.00 USD | `-43.69%` | `61.91` |
| `Live` | `Long` | `54.75` | 98,930,000.00 USD | 0.00 USD | 37,350.00 USD | `-43.59%` | `682.16` |
| `Live` | `Long` | `54.85` | 98,890,000.00 USD | 0.00 USD | 861,400.00 USD | `-43.49%` | `15,704.66` |
| `Live` | `Long` | `54.95` | 98,030,000.00 USD | 0.00 USD | 142,480.00 USD | `-43.38%` | `2,592.93` |
| `Live` | `Long` | `55.05` | 97,890,000.00 USD | 0.00 USD | 552.70 USD | `-43.28%` | `10.04` |
| `Live` | `Long` | `55.15` | 97,890,000.00 USD | 0.00 USD | 341.93 USD | `-43.18%` | `6.20` |
| `Live` | `Long` | `55.25` | 97,890,000.00 USD | 0.00 USD | 2,010.00 USD | `-43.07%` | `36.31` |
| `Live` | `Long` | `55.35` | 97,890,000.00 USD | 0.00 USD | 9,920.00 USD | `-42.97%` | `179.16` |
| `Live` | `Long` | `55.45` | 97,880,000.00 USD | 0.00 USD | 8,670.00 USD | `-42.87%` | `156.35` |
| `Live` | `Long` | `55.55` | 97,870,000.00 USD | 0.00 USD | 5,090.00 USD | `-42.76%` | `91.69` |
| `Live` | `Long` | `55.65` | 97,860,000.00 USD | 0.00 USD | 11,490.00 USD | `-42.66%` | `206.41` |
| `Live` | `Long` | `55.75` | 97,850,000.00 USD | 0.00 USD | 233,170.00 USD | `-42.56%` | `4,182.42` |
| `Live` | `Long` | `55.85` | 97,620,000.00 USD | 0.00 USD | 5,050.00 USD | `-42.46%` | `90.34` |
| `Live` | `Long` | `55.95` | 97,610,000.00 USD | 0.00 USD | 7,390.00 USD | `-42.35%` | `132.09` |
| `Live` | `Long` | `56.05` | 97,610,000.00 USD | 0.00 USD | 19,890.00 USD | `-42.25%` | `354.84` |
| `Live` | `Long` | `56.15` | 97,590,000.00 USD | 0.00 USD | 40,270.00 USD | `-42.15%` | `717.16` |
| `Live` | `Long` | `56.25` | 97,550,000.00 USD | 0.00 USD | 13,300.00 USD | `-42.04%` | `236.52` |
| `Live` | `Long` | `56.35` | 97,530,000.00 USD | 0.00 USD | 12,550.00 USD | `-41.94%` | `222.68` |
| `Live` | `Long` | `56.45` | 97,520,000.00 USD | 0.00 USD | 12,980.00 USD | `-41.84%` | `229.97` |
| `Live` | `Long` | `56.55` | 97,510,000.00 USD | 0.00 USD | 4,730.00 USD | `-41.73%` | `83.63` |
| `Live` | `Long` | `56.65` | 97,500,000.00 USD | 0.00 USD | 3,190.00 USD | `-41.63%` | `56.32` |
| `Live` | `Long` | `56.75` | 97,500,000.00 USD | 0.00 USD | 9,410.00 USD | `-41.53%` | `165.87` |
| `Live` | `Long` | `56.85` | 97,490,000.00 USD | 0.00 USD | 122.80 USD | `-41.42%` | `2.16` |
| `Live` | `Long` | `56.95` | 97,490,000.00 USD | 0.00 USD | 2,780,000.00 USD | `-41.32%` | `48,815.94` |
| `Live` | `Long` | `57.05` | 94,710,000.00 USD | 0.00 USD | 3,620.00 USD | `-41.22%` | `63.42` |
| `Live` | `Long` | `57.15` | 94,710,000.00 USD | 0.00 USD | 6,590.00 USD | `-41.12%` | `115.39` |
| `Live` | `Long` | `57.25` | 94,700,000.00 USD | 0.00 USD | 1,270.00 USD | `-41.01%` | `22.11` |
| `Live` | `Long` | `57.35` | 94,700,000.00 USD | 0.00 USD | 7,120.00 USD | `-40.91%` | `124.09` |
| `Live` | `Long` | `57.45` | 94,690,000.00 USD | 0.00 USD | 19,200.00 USD | `-40.81%` | `334.25` |
| `Live` | `Long` | `57.55` | 94,670,000.00 USD | 0.00 USD | 1,390.00 USD | `-40.70%` | `24.22` |
| `Live` | `Long` | `57.65` | 94,670,000.00 USD | 0.00 USD | 13,130.00 USD | `-40.60%` | `227.82` |
| `Live` | `Long` | `57.75` | 94,660,000.00 USD | 0.00 USD | 26,230.00 USD | `-40.50%` | `454.14` |
| `Live` | `Long` | `57.85` | 94,630,000.00 USD | 0.00 USD | 22,150.00 USD | `-40.39%` | `382.92` |
| `Live` | `Long` | `57.95` | 94,610,000.00 USD | 0.00 USD | 324.52 USD | `-40.29%` | `5.60` |
| `Live` | `Long` | `58.05` | 94,610,000.00 USD | 0.00 USD | 9,900.00 USD | `-40.19%` | `170.53` |
| `Live` | `Long` | `58.15` | 94,600,000.00 USD | 0.00 USD | 130,170.00 USD | `-40.09%` | `2,238.54` |
| `Live` | `Long` | `58.25` | 94,470,000.00 USD | 0.00 USD | 6,670.00 USD | `-39.98%` | `114.44` |
| `Live` | `Long` | `58.35` | 94,460,000.00 USD | 0.00 USD | 46,410.00 USD | `-39.88%` | `795.36` |
| `Live` | `Long` | `58.45` | 94,420,000.00 USD | 0.00 USD | 463.51 USD | `-39.78%` | `7.93` |
| `Live` | `Long` | `58.55` | 94,410,000.00 USD | 0.00 USD | 4,680.00 USD | `-39.67%` | `79.85` |
| `Live` | `Long` | `58.65` | 94,410,000.00 USD | 0.00 USD | 62,850.00 USD | `-39.57%` | `1,071.57` |
| `Live` | `Long` | `58.75` | 94,350,000.00 USD | 0.00 USD | 7,250.00 USD | `-39.47%` | `123.33` |
| `Live` | `Long` | `58.85` | 94,340,000.00 USD | 0.00 USD | 13,980.00 USD | `-39.36%` | `237.58` |
| `Live` | `Long` | `58.95` | 94,330,000.00 USD | 0.00 USD | 488.70 USD | `-39.26%` | `8.29` |
| `Live` | `Long` | `59.05` | 94,330,000.00 USD | 0.00 USD | 3,780.00 USD | `-39.16%` | `63.97` |
| `Live` | `Long` | `59.15` | 94,320,000.00 USD | 0.00 USD | 9,070.00 USD | `-39.06%` | `153.27` |
| `Live` | `Long` | `59.25` | 94,310,000.00 USD | 0.00 USD | 41,950.00 USD | `-38.95%` | `708.00` |
| `Live` | `Long` | `59.35` | 94,270,000.00 USD | 0.00 USD | 44,180.00 USD | `-38.85%` | `744.44` |
| `Live` | `Long` | `59.45` | 94,230,000.00 USD | 0.00 USD | 33,950.00 USD | `-38.75%` | `571.12` |
| `Live` | `Long` | `59.55` | 94,190,000.00 USD | 0.00 USD | 8,610.00 USD | `-38.64%` | `144.57` |
| `Live` | `Long` | `59.65` | 94,180,000.00 USD | 0.00 USD | 3,640.00 USD | `-38.54%` | `61.07` |
| `Live` | `Long` | `59.75` | 94,180,000.00 USD | 0.00 USD | 13,130.00 USD | `-38.44%` | `219.76` |
| `Live` | `Long` | `59.85` | 94,170,000.00 USD | 0.00 USD | 46,860.00 USD | `-38.33%` | `782.98` |
| `Live` | `Long` | `59.95` | 94,120,000.00 USD | 0.00 USD | 2,440,000.00 USD | `-38.23%` | `40,621.17` |
| `Live` | `Long` | `60.05` | 91,680,000.00 USD | 0.00 USD | 19,790.00 USD | `-38.13%` | `329.50` |
| `Live` | `Long` | `60.15` | 91,670,000.00 USD | 0.00 USD | 36,590.00 USD | `-38.02%` | `608.24` |
| `Live` | `Long` | `60.25` | 91,630,000.00 USD | 0.00 USD | 499.47 USD | `-37.92%` | `8.29` |
| `Live` | `Long` | `60.35` | 91,630,000.00 USD | 0.00 USD | 3,930.00 USD | `-37.82%` | `65.10` |
| `Live` | `Long` | `60.45` | 91,620,000.00 USD | 0.00 USD | 25,390.00 USD | `-37.72%` | `420.00` |
| `Live` | `Long` | `60.55` | 91,600,000.00 USD | 0.00 USD | 2,760.00 USD | `-37.61%` | `45.51` |
| `Live` | `Long` | `60.65` | 91,600,000.00 USD | 0.00 USD | 711.42 USD | `-37.51%` | `11.73` |
| `Live` | `Long` | `60.75` | 91,600,000.00 USD | 0.00 USD | 5,300.00 USD | `-37.41%` | `87.26` |
| `Live` | `Long` | `60.85` | 91,590,000.00 USD | 0.00 USD | 28,860.00 USD | `-37.30%` | `474.33` |
| `Live` | `Long` | `60.95` | 91,560,000.00 USD | 0.00 USD | 98,640.00 USD | `-37.20%` | `1,618.38` |
| `Live` | `Long` | `61.05` | 91,460,000.00 USD | 0.00 USD | 4,230.00 USD | `-37.10%` | `69.34` |
| `Live` | `Long` | `61.15` | 91,460,000.00 USD | 0.00 USD | 10,300.00 USD | `-36.99%` | `168.45` |
| `Live` | `Long` | `61.25` | 91,450,000.00 USD | 0.00 USD | 41,080.00 USD | `-36.89%` | `670.67` |
| `Live` | `Long` | `61.35` | 91,410,000.00 USD | 0.00 USD | 10,170.00 USD | `-36.79%` | `165.83` |
| `Live` | `Long` | `61.45` | 91,400,000.00 USD | 0.00 USD | 20,920.00 USD | `-36.69%` | `340.48` |
| `Live` | `Long` | `61.55` | 91,380,000.00 USD | 0.00 USD | 320.06 USD | `-36.58%` | `5.20` |
| `Live` | `Long` | `61.65` | 91,380,000.00 USD | 0.00 USD | 18,880.00 USD | `-36.48%` | `306.22` |
| `Live` | `Long` | `61.75` | 91,360,000.00 USD | 0.00 USD | 16,580.00 USD | `-36.38%` | `268.54` |
| `Live` | `Long` | `61.85` | 91,340,000.00 USD | 0.00 USD | 24,050.00 USD | `-36.27%` | `388.89` |
| `Live` | `Long` | `61.95` | 91,320,000.00 USD | 0.00 USD | 19,750.00 USD | `-36.17%` | `318.75` |
| `Live` | `Long` | `62.05` | 91,300,000.00 USD | 0.00 USD | 9,000.00 USD | `-36.07%` | `145.05` |
| `Live` | `Long` | `62.15` | 91,290,000.00 USD | 0.00 USD | 32,930.00 USD | `-35.96%` | `529.83` |
| `Live` | `Long` | `62.25` | 91,250,000.00 USD | 0.00 USD | 177,610.00 USD | `-35.86%` | `2,853.17` |
| `Live` | `Long` | `62.35` | 91,080,000.00 USD | 0.00 USD | 16,720.00 USD | `-35.76%` | `268.09` |
| `Live` | `Long` | `62.45` | 91,060,000.00 USD | 0.00 USD | 33,530.00 USD | `-35.66%` | `536.84` |
| `Live` | `Long` | `62.55` | 91,030,000.00 USD | 0.00 USD | 180,290.00 USD | `-35.55%` | `2,882.40` |
| `Live` | `Long` | `62.65` | 90,850,000.00 USD | 0.00 USD | 2,480.00 USD | `-35.45%` | `39.62` |
| `Live` | `Long` | `62.75` | 90,840,000.00 USD | 0.00 USD | 3,140.00 USD | `-35.35%` | `49.97` |
| `Live` | `Long` | `62.85` | 90,840,000.00 USD | 0.00 USD | 31,310.00 USD | `-35.24%` | `498.17` |
| `Live` | `Long` | `62.95` | 90,810,000.00 USD | 0.00 USD | 9,610.00 USD | `-35.14%` | `152.71` |
| `Live` | `Long` | `63.05` | 90,800,000.00 USD | 0.00 USD | 16,430.00 USD | `-35.04%` | `260.51` |
| `Live` | `Long` | `63.15` | 90,780,000.00 USD | 0.00 USD | 88,070.00 USD | `-34.93%` | `1,394.64` |
| `Live` | `Long` | `63.25` | 90,700,000.00 USD | 0.00 USD | 15,410.00 USD | `-34.83%` | `243.68` |
| `Live` | `Long` | `63.45` | 90,680,000.00 USD | 0.00 USD | 291.24 USD | `-34.62%` | `4.59` |
| `Live` | `Long` | `63.55` | 90,680,000.00 USD | 0.00 USD | 50,360.00 USD | `-34.52%` | `792.39` |
| `Live` | `Long` | `63.65` | 90,630,000.00 USD | 0.00 USD | 1,320.00 USD | `-34.42%` | `20.75` |
| `Live` | `Long` | `63.75` | 90,630,000.00 USD | 0.00 USD | 50,640.00 USD | `-34.32%` | `794.39` |
| `Live` | `Long` | `63.85` | 90,580,000.00 USD | 0.00 USD | 36,960.00 USD | `-34.21%` | `578.89` |
| `Live` | `Long` | `63.95` | 90,540,000.00 USD | 0.00 USD | 5,560.00 USD | `-34.11%` | `86.95` |
| `Live` | `Long` | `64.15` | 90,530,000.00 USD | 0.00 USD | 160.38 USD | `-33.90%` | `2.50` |
| `Live` | `Long` | `64.25` | 90,530,000.00 USD | 0.00 USD | 23,150.00 USD | `-33.80%` | `360.35` |
| `Live` | `Long` | `64.35` | 90,510,000.00 USD | 0.00 USD | 3,020.00 USD | `-33.70%` | `46.96` |
| `Live` | `Long` | `64.45` | 90,510,000.00 USD | 0.00 USD | 101,630.00 USD | `-33.59%` | `1,576.88` |
| `Live` | `Long` | `64.55` | 90,410,000.00 USD | 0.00 USD | 18,080.00 USD | `-33.49%` | `280.16` |
| `Live` | `Long` | `64.65` | 90,390,000.00 USD | 0.00 USD | 2,220.00 USD | `-33.39%` | `34.28` |
| `Live` | `Long` | `64.75` | 90,390,000.00 USD | 0.00 USD | 1,110.00 USD | `-33.29%` | `17.19` |
| `Live` | `Long` | `64.85` | 90,390,000.00 USD | 0.00 USD | 396.23 USD | `-33.18%` | `6.11` |
| `Live` | `Long` | `64.95` | 90,380,000.00 USD | 0.00 USD | 209.79 USD | `-33.08%` | `3.23` |
| `Live` | `Long` | `65.05` | 90,380,000.00 USD | 0.00 USD | 247,180.00 USD | `-32.98%` | `3,799.85` |
| `Live` | `Long` | `65.15` | 90,140,000.00 USD | 0.00 USD | 13,490.00 USD | `-32.87%` | `207.08` |
| `Live` | `Long` | `65.25` | 90,120,000.00 USD | 0.00 USD | 16,320.00 USD | `-32.77%` | `250.16` |
| `Live` | `Long` | `65.35` | 90,110,000.00 USD | 0.00 USD | 37,840.00 USD | `-32.67%` | `579.07` |
| `Live` | `Long` | `65.45` | 90,070,000.00 USD | 0.00 USD | 4,380.00 USD | `-32.56%` | `66.88` |
| `Live` | `Long` | `65.55` | 90,070,000.00 USD | 0.00 USD | 10,690.00 USD | `-32.46%` | `163.01` |
| `Live` | `Long` | `65.65` | 90,050,000.00 USD | 0.00 USD | 156,750.00 USD | `-32.36%` | `2,387.62` |
| `Live` | `Long` | `65.75` | 89,900,000.00 USD | 0.00 USD | 5,050.00 USD | `-32.25%` | `76.84` |
| `Live` | `Long` | `65.85` | 89,890,000.00 USD | 0.00 USD | 1,620.00 USD | `-32.15%` | `24.59` |
| `Live` | `Long` | `65.95` | 89,890,000.00 USD | 0.00 USD | 5,780.00 USD | `-32.05%` | `87.71` |
| `Live` | `Long` | `66.05` | 89,890,000.00 USD | 0.00 USD | 6,180.00 USD | `-31.95%` | `93.62` |
| `Live` | `Long` | `66.25` | 89,880,000.00 USD | 0.00 USD | 15,600.00 USD | `-31.74%` | `235.52` |
| `Live` | `Long` | `66.35` | 89,860,000.00 USD | 0.00 USD | 1,600.00 USD | `-31.64%` | `24.08` |
| `Live` | `Long` | `66.45` | 89,860,000.00 USD | 0.00 USD | 10,990.00 USD | `-31.53%` | `165.37` |
| `Live` | `Long` | `66.55` | 89,850,000.00 USD | 0.00 USD | 111,220.00 USD | `-31.43%` | `1,671.27` |
| `Live` | `Long` | `66.65` | 89,740,000.00 USD | 0.00 USD | 13,170.00 USD | `-31.33%` | `197.56` |
| `Live` | `Long` | `66.75` | 89,730,000.00 USD | 0.00 USD | 49,390.00 USD | `-31.22%` | `739.96` |
| `Live` | `Long` | `66.85` | 89,680,000.00 USD | 0.00 USD | 39,430.00 USD | `-31.12%` | `589.90` |
| `Live` | `Long` | `66.95` | 89,640,000.00 USD | 0.00 USD | 937.30 USD | `-31.02%` | `14.00` |
| `Live` | `Long` | `67.05` | 89,640,000.00 USD | 0.00 USD | 40,230.00 USD | `-30.92%` | `599.98` |
| `Live` | `Long` | `67.15` | 89,600,000.00 USD | 0.00 USD | 24,540.00 USD | `-30.81%` | `365.44` |
| `Live` | `Long` | `67.25` | 89,570,000.00 USD | 0.00 USD | 248.83 USD | `-30.71%` | `3.70` |
| `Live` | `Long` | `67.35` | 89,570,000.00 USD | 0.00 USD | 29,330.00 USD | `-30.61%` | `435.51` |
| `Live` | `Long` | `67.45` | 89,540,000.00 USD | 0.00 USD | 35,570.00 USD | `-30.50%` | `527.40` |
| `Live` | `Long` | `67.55` | 89,510,000.00 USD | 0.00 USD | 77,840.00 USD | `-30.40%` | `1,152.33` |
| `Live` | `Long` | `67.65` | 89,430,000.00 USD | 0.00 USD | 148,910.00 USD | `-30.30%` | `2,201.17` |
| `Live` | `Long` | `67.75` | 89,280,000.00 USD | 0.00 USD | 11,310.00 USD | `-30.19%` | `166.97` |
| `Live` | `Long` | `67.85` | 89,270,000.00 USD | 0.00 USD | 4,670.00 USD | `-30.09%` | `68.85` |
| `Live` | `Long` | `68.05` | 89,260,000.00 USD | 0.00 USD | 10,180.00 USD | `-29.89%` | `149.62` |
| `Live` | `Long` | `68.15` | 89,250,000.00 USD | 0.00 USD | 37,490,000.00 USD | `-29.78%` | `550,118.38` |
| `Live` | `Long` | `68.25` | 51,760,000.00 USD | 0.00 USD | 13,650.00 USD | `-29.68%` | `199.93` |
| `Live` | `Long` | `68.35` | 51,750,000.00 USD | 0.00 USD | 2,860.00 USD | `-29.58%` | `41.82` |
| `Live` | `Long` | `68.45` | 51,750,000.00 USD | 0.00 USD | 20,580.00 USD | `-29.47%` | `300.73` |
| `Live` | `Long` | `68.55` | 51,730,000.00 USD | 0.00 USD | 3,370.00 USD | `-29.37%` | `49.09` |
| `Live` | `Long` | `68.65` | 51,720,000.00 USD | 0.00 USD | 6,530.00 USD | `-29.27%` | `95.06` |
| `Live` | `Long` | `68.75` | 51,720,000.00 USD | 0.00 USD | 365,790.00 USD | `-29.16%` | `5,320.58` |
| `Live` | `Long` | `68.85` | 51,350,000.00 USD | 0.00 USD | 3,040.00 USD | `-29.06%` | `44.12` |
| `Live` | `Long` | `68.95` | 51,350,000.00 USD | 0.00 USD | 46,330.00 USD | `-28.96%` | `671.97` |
| `Live` | `Long` | `69.05` | 51,300,000.00 USD | 0.00 USD | 145.70 USD | `-28.85%` | `2.11` |
| `Live` | `Long` | `69.15` | 51,300,000.00 USD | 0.00 USD | 791,690.00 USD | `-28.75%` | `11,448.94` |
| `Live` | `Long` | `69.25` | 50,510,000.00 USD | 0.00 USD | 9,630.00 USD | `-28.65%` | `139.01` |
| `Live` | `Long` | `69.45` | 50,500,000.00 USD | 0.00 USD | 15,870.00 USD | `-28.44%` | `228.56` |
| `Live` | `Long` | `69.55` | 50,480,000.00 USD | 0.00 USD | 8,880.00 USD | `-28.34%` | `127.63` |
| `Live` | `Long` | `69.65` | 50,480,000.00 USD | 0.00 USD | 3,590.00 USD | `-28.24%` | `51.50` |
| `Live` | `Long` | `69.75` | 50,470,000.00 USD | 0.00 USD | 12,770,000.00 USD | `-28.13%` | `183,080.30` |
| `Live` | `Long` | `69.85` | 37,700,000.00 USD | 0.00 USD | 9,160.00 USD | `-28.03%` | `131.19` |
| `Live` | `Long` | `69.95` | 37,690,000.00 USD | 0.00 USD | 12,050.00 USD | `-27.93%` | `172.23` |
| `Live` | `Long` | `70.05` | 37,680,000.00 USD | 0.00 USD | 542,190.00 USD | `-27.82%` | `7,740.02` |
| `Live` | `Long` | `70.15` | 37,140,000.00 USD | 0.00 USD | 4,900.00 USD | `-27.72%` | `69.88` |
| `Live` | `Long` | `70.25` | 37,130,000.00 USD | 0.00 USD | 82,890.00 USD | `-27.62%` | `1,179.87` |
| `Live` | `Long` | `70.35` | 37,050,000.00 USD | 0.00 USD | 2,140,000.00 USD | `-27.52%` | `30,414.81` |
| `Live` | `Long` | `70.45` | 34,910,000.00 USD | 0.00 USD | 113,930.00 USD | `-27.41%` | `1,617.15` |
| `Live` | `Long` | `70.55` | 34,800,000.00 USD | 0.00 USD | 1,630.00 USD | `-27.31%` | `23.17` |
| `Live` | `Long` | `70.65` | 34,800,000.00 USD | 0.00 USD | 50,360.00 USD | `-27.21%` | `712.88` |
| `Live` | `Long` | `70.75` | 34,740,000.00 USD | 0.00 USD | 1,430,000.00 USD | `-27.10%` | `20,184.80` |
| `Live` | `Long` | `70.85` | 33,320,000.00 USD | 0.00 USD | 14,360.00 USD | `-27.00%` | `202.72` |
| `Live` | `Long` | `70.95` | 33,300,000.00 USD | 0.00 USD | 4,430.00 USD | `-26.90%` | `62.38` |
| `Live` | `Long` | `71.05` | 33,300,000.00 USD | 0.00 USD | 33,380.00 USD | `-26.79%` | `469.75` |
| `Live` | `Long` | `71.15` | 33,260,000.00 USD | 0.00 USD | 70,650.00 USD | `-26.69%` | `992.99` |
| `Live` | `Long` | `71.25` | 33,190,000.00 USD | 0.00 USD | 18,270.00 USD | `-26.59%` | `256.46` |
| `Live` | `Long` | `71.35` | 33,180,000.00 USD | 0.00 USD | 29,280.00 USD | `-26.48%` | `410.44` |
| `Live` | `Long` | `71.45` | 33,150,000.00 USD | 0.00 USD | 23,900.00 USD | `-26.38%` | `334.48` |
| `Live` | `Long` | `71.55` | 33,120,000.00 USD | 0.00 USD | 52,920.00 USD | `-26.28%` | `739.59` |
| `Live` | `Long` | `71.65` | 33,070,000.00 USD | 0.00 USD | 1,280.00 USD | `-26.18%` | `17.89` |
| `Live` | `Long` | `71.75` | 33,070,000.00 USD | 0.00 USD | 27,710.00 USD | `-26.07%` | `386.16` |
| `Live` | `Long` | `71.85` | 33,040,000.00 USD | 0.00 USD | 2,670.00 USD | `-25.97%` | `37.11` |
| `Live` | `Long` | `71.95` | 33,040,000.00 USD | 0.00 USD | 45,220.00 USD | `-25.87%` | `628.50` |
| `Live` | `Long` | `72.05` | 32,990,000.00 USD | 0.00 USD | 1,090,000.00 USD | `-25.76%` | `15,118.77` |
| `Live` | `Long` | `72.15` | 31,900,000.00 USD | 0.00 USD | 130,700.00 USD | `-25.66%` | `1,811.56` |
| `Live` | `Long` | `72.25` | 31,770,000.00 USD | 0.00 USD | 260,210.00 USD | `-25.56%` | `3,601.59` |
| `Live` | `Long` | `72.35` | 31,510,000.00 USD | 0.00 USD | 29,100.00 USD | `-25.45%` | `402.20` |
| `Live` | `Long` | `72.45` | 31,480,000.00 USD | 0.00 USD | 1,590.00 USD | `-25.35%` | `22.01` |
| `Live` | `Long` | `72.55` | 31,480,000.00 USD | 0.00 USD | 17,280.00 USD | `-25.25%` | `238.13` |
| `Live` | `Long` | `72.65` | 31,460,000.00 USD | 0.00 USD | 35,010.00 USD | `-25.15%` | `481.90` |
| `Live` | `Long` | `72.75` | 31,430,000.00 USD | 0.00 USD | 3,100.00 USD | `-25.04%` | `42.56` |
| `Live` | `Long` | `72.85` | 31,430,000.00 USD | 0.00 USD | 186,830.00 USD | `-24.94%` | `2,564.61` |
| `Live` | `Long` | `72.95` | 31,240,000.00 USD | 0.00 USD | 5,600.00 USD | `-24.84%` | `76.71` |
| `Live` | `Long` | `73.05` | 31,230,000.00 USD | 0.00 USD | 32,880.00 USD | `-24.73%` | `450.09` |
| `Live` | `Long` | `73.15` | 31,200,000.00 USD | 0.00 USD | 17,430.00 USD | `-24.63%` | `238.30` |
| `Live` | `Long` | `73.25` | 31,180,000.00 USD | 0.00 USD | 41,540.00 USD | `-24.53%` | `567.12` |
| `Live` | `Long` | `73.35` | 31,140,000.00 USD | 0.00 USD | 10,250.00 USD | `-24.42%` | `139.73` |
| `Live` | `Long` | `73.45` | 31,130,000.00 USD | 0.00 USD | 5,350.00 USD | `-24.32%` | `72.82` |
| `Live` | `Long` | `73.55` | 31,130,000.00 USD | 0.00 USD | 15,600.00 USD | `-24.22%` | `212.14` |
| `Live` | `Long` | `73.65` | 31,110,000.00 USD | 0.00 USD | 37,850.00 USD | `-24.12%` | `513.85` |
| `Live` | `Long` | `73.75` | 31,070,000.00 USD | 0.00 USD | 70,280.00 USD | `-24.01%` | `952.95` |
| `Live` | `Long` | `73.85` | 31,000,000.00 USD | 0.00 USD | 11,710.00 USD | `-23.91%` | `158.63` |
| `Live` | `Long` | `73.95` | 30,990,000.00 USD | 0.00 USD | 40,040.00 USD | `-23.81%` | `541.40` |
| `Live` | `Long` | `74.05` | 30,950,000.00 USD | 0.00 USD | 24,560.00 USD | `-23.70%` | `331.73` |
| `Live` | `Long` | `74.15` | 30,930,000.00 USD | 0.00 USD | 21,430.00 USD | `-23.60%` | `289.03` |
| `Live` | `Long` | `74.25` | 30,910,000.00 USD | 0.00 USD | 27,320.00 USD | `-23.50%` | `367.91` |
| `Live` | `Long` | `74.35` | 30,880,000.00 USD | 0.00 USD | 39,600.00 USD | `-23.39%` | `532.62` |
| `Live` | `Long` | `74.45` | 30,840,000.00 USD | 0.00 USD | 27,460.00 USD | `-23.29%` | `368.85` |
| `Live` | `Long` | `74.55` | 30,810,000.00 USD | 0.00 USD | 6,260.00 USD | `-23.19%` | `84.00` |
| `Live` | `Long` | `74.65` | 30,800,000.00 USD | 0.00 USD | 10,450.00 USD | `-23.08%` | `140.05` |
| `Live` | `Long` | `74.75` | 30,790,000.00 USD | 0.00 USD | 123,070.00 USD | `-22.98%` | `1,646.41` |
| `Live` | `Long` | `74.85` | 30,670,000.00 USD | 0.00 USD | 134,930.00 USD | `-22.88%` | `1,802.70` |
| `Live` | `Long` | `74.95` | 30,540,000.00 USD | 0.00 USD | 18,610.00 USD | `-22.78%` | `248.31` |
| `Live` | `Long` | `75.05` | 30,520,000.00 USD | 0.00 USD | 40,670.00 USD | `-22.67%` | `541.85` |
| `Live` | `Long` | `75.25` | 30,480,000.00 USD | 0.00 USD | 287,360.00 USD | `-22.47%` | `3,818.68` |
| `Live` | `Long` | `75.35` | 30,190,000.00 USD | 0.00 USD | 21,080.00 USD | `-22.36%` | `279.73` |
| `Live` | `Long` | `75.45` | 30,170,000.00 USD | 0.00 USD | 33,560.00 USD | `-22.26%` | `444.85` |
| `Live` | `Long` | `75.55` | 30,130,000.00 USD | 0.00 USD | 1,650,000.00 USD | `-22.16%` | `21,889.29` |
| `Live` | `Long` | `75.65` | 28,480,000.00 USD | 0.00 USD | 130,250.00 USD | `-22.05%` | `1,721.70` |
| `Live` | `Long` | `75.75` | 28,350,000.00 USD | 0.00 USD | 53,060.00 USD | `-21.95%` | `700.51` |
| `Live` | `Long` | `75.85` | 28,300,000.00 USD | 0.00 USD | 2,880.00 USD | `-21.85%` | `37.95` |
| `Live` | `Long` | `75.95` | 28,290,000.00 USD | 0.00 USD | 37,010.00 USD | `-21.75%` | `487.32` |
| `Live` | `Long` | `76.05` | 28,260,000.00 USD | 0.00 USD | 6,260.00 USD | `-21.64%` | `82.27` |
| `Live` | `Long` | `76.15` | 28,250,000.00 USD | 0.00 USD | 4,370.00 USD | `-21.54%` | `57.43` |
| `Live` | `Long` | `76.25` | 28,250,000.00 USD | 0.00 USD | 10,140.00 USD | `-21.44%` | `133.04` |
| `Live` | `Long` | `76.35` | 28,240,000.00 USD | 0.00 USD | 41,020.00 USD | `-21.33%` | `537.32` |
| `Live` | `Long` | `76.45` | 28,200,000.00 USD | 0.00 USD | 1,490,000.00 USD | `-21.23%` | `19,460.09` |
| `Live` | `Long` | `76.55` | 26,710,000.00 USD | 0.00 USD | 37,610.00 USD | `-21.13%` | `491.36` |
| `Live` | `Long` | `76.65` | 26,670,000.00 USD | 0.00 USD | 55,910.00 USD | `-21.02%` | `729.36` |
| `Live` | `Long` | `76.75` | 26,610,000.00 USD | 0.00 USD | 29,450.00 USD | `-20.92%` | `383.75` |
| `Live` | `Long` | `76.85` | 26,590,000.00 USD | 0.00 USD | 134,000.00 USD | `-20.82%` | `1,743.66` |
| `Live` | `Long` | `76.95` | 26,450,000.00 USD | 0.00 USD | 41,940.00 USD | `-20.72%` | `545.09` |
| `Live` | `Long` | `77.05` | 26,410,000.00 USD | 0.00 USD | 80,610.00 USD | `-20.61%` | `1,046.25` |
| `Live` | `Long` | `77.15` | 26,330,000.00 USD | 0.00 USD | 84,180.00 USD | `-20.51%` | `1,091.07` |
| `Live` | `Long` | `77.25` | 26,240,000.00 USD | 0.00 USD | 25,020.00 USD | `-20.41%` | `323.94` |
| `Live` | `Long` | `77.35` | 26,220,000.00 USD | 0.00 USD | 36,280.00 USD | `-20.30%` | `468.99` |
| `Live` | `Long` | `77.45` | 26,180,000.00 USD | 0.00 USD | 40,590.00 USD | `-20.20%` | `524.13` |
| `Live` | `Long` | `77.55` | 26,140,000.00 USD | 0.00 USD | 12,900.00 USD | `-20.10%` | `166.30` |
| `Live` | `Long` | `77.75` | 26,130,000.00 USD | 0.00 USD | 20,230.00 USD | `-19.89%` | `260.19` |
| `Live` | `Long` | `77.85` | 26,110,000.00 USD | 0.00 USD | 81,170.00 USD | `-19.79%` | `1,042.65` |
| `Live` | `Long` | `77.95` | 26,030,000.00 USD | 0.00 USD | 8,370.00 USD | `-19.68%` | `107.32` |
| `Live` | `Long` | `78.05` | 26,020,000.00 USD | 0.00 USD | 21,520.00 USD | `-19.58%` | `275.71` |
| `Live` | `Long` | `78.15` | 26,000,000.00 USD | 0.00 USD | 65,600.00 USD | `-19.48%` | `839.39` |
| `Live` | `Long` | `78.25` | 25,930,000.00 USD | 0.00 USD | 39,440.00 USD | `-19.38%` | `504.08` |
| `Live` | `Long` | `78.35` | 25,890,000.00 USD | 0.00 USD | 55,060.00 USD | `-19.27%` | `702.76` |
| `Live` | `Long` | `78.45` | 25,840,000.00 USD | 0.00 USD | 29,370.00 USD | `-19.17%` | `374.40` |
| `Live` | `Long` | `78.55` | 25,810,000.00 USD | 0.00 USD | 5,740.00 USD | `-19.07%` | `73.09` |
| `Live` | `Long` | `78.65` | 25,800,000.00 USD | 0.00 USD | 32,860.00 USD | `-18.96%` | `417.75` |
| `Live` | `Long` | `78.75` | 25,770,000.00 USD | 0.00 USD | 52,670.00 USD | `-18.86%` | `668.88` |
| `Live` | `Long` | `78.85` | 25,720,000.00 USD | 0.00 USD | 240,940.00 USD | `-18.76%` | `3,055.65` |
| `Live` | `Long` | `78.95` | 25,480,000.00 USD | 0.00 USD | 2,270.00 USD | `-18.65%` | `28.81` |
| `Live` | `Long` | `79.05` | 25,470,000.00 USD | 0.00 USD | 6,490.00 USD | `-18.55%` | `82.14` |
| `Live` | `Long` | `79.15` | 25,470,000.00 USD | 0.00 USD | 128,420.00 USD | `-18.45%` | `1,622.43` |
| `Live` | `Long` | `79.25` | 25,340,000.00 USD | 0.00 USD | 47,570.00 USD | `-18.35%` | `600.23` |
| `Live` | `Long` | `79.35` | 25,290,000.00 USD | 0.00 USD | 20,900.00 USD | `-18.24%` | `263.44` |
| `Live` | `Long` | `79.45` | 25,270,000.00 USD | 0.00 USD | 8,800.00 USD | `-18.14%` | `110.73` |
| `Live` | `Long` | `79.55` | 25,260,000.00 USD | 0.00 USD | 1,900.00 USD | `-18.04%` | `23.91` |
| `Live` | `Long` | `79.65` | 25,260,000.00 USD | 0.00 USD | 19,960.00 USD | `-17.93%` | `250.58` |
| `Live` | `Long` | `79.75` | 25,240,000.00 USD | 0.00 USD | 13,190.00 USD | `-17.83%` | `165.41` |
| `Live` | `Long` | `79.85` | 25,230,000.00 USD | 0.00 USD | 14,710.00 USD | `-17.73%` | `184.18` |
| `Live` | `Long` | `79.95` | 25,210,000.00 USD | 0.00 USD | 189,340.00 USD | `-17.62%` | `2,368.25` |
| `Live` | `Long` | `80.05` | 25,020,000.00 USD | 0.00 USD | 14,790.00 USD | `-17.52%` | `184.74` |
| `Live` | `Long` | `80.15` | 25,010,000.00 USD | 0.00 USD | 31,900.00 USD | `-17.42%` | `398.06` |
| `Live` | `Long` | `80.25` | 24,980,000.00 USD | 0.00 USD | 57,660.00 USD | `-17.31%` | `718.54` |
| `Live` | `Long` | `80.35` | 24,920,000.00 USD | 0.00 USD | 132,270.00 USD | `-17.21%` | `1,646.22` |
| `Live` | `Long` | `80.45` | 24,790,000.00 USD | 0.00 USD | 20,100.00 USD | `-17.11%` | `249.79` |
| `Live` | `Long` | `80.55` | 24,770,000.00 USD | 0.00 USD | 15,600.00 USD | `-17.01%` | `193.65` |
| `Live` | `Long` | `80.65` | 24,750,000.00 USD | 0.00 USD | 77,670.00 USD | `-16.90%` | `963.09` |
| `Live` | `Long` | `80.75` | 24,670,000.00 USD | 0.00 USD | 33,470.00 USD | `-16.80%` | `414.46` |
| `Live` | `Long` | `80.85` | 24,640,000.00 USD | 0.00 USD | 449,860.00 USD | `-16.70%` | `5,564.16` |
| `Live` | `Long` | `80.95` | 24,190,000.00 USD | 0.00 USD | 10,620.00 USD | `-16.59%` | `131.18` |
| `Live` | `Long` | `81.05` | 24,180,000.00 USD | 0.00 USD | 2,250,000.00 USD | `-16.49%` | `27,783.98` |
| `Live` | `Long` | `81.15` | 21,930,000.00 USD | 0.00 USD | 101,800.00 USD | `-16.39%` | `1,254.44` |
| `Live` | `Long` | `81.25` | 21,830,000.00 USD | 0.00 USD | 22,790.00 USD | `-16.28%` | `280.49` |
| `Live` | `Long` | `81.35` | 21,800,000.00 USD | 0.00 USD | 56,470.00 USD | `-16.18%` | `694.17` |
| `Live` | `Long` | `81.45` | 21,750,000.00 USD | 0.00 USD | 59,690.00 USD | `-16.08%` | `732.84` |
| `Live` | `Long` | `81.55` | 21,690,000.00 USD | 0.00 USD | 190,680.00 USD | `-15.98%` | `2,338.18` |
| `Live` | `Long` | `81.65` | 21,500,000.00 USD | 0.00 USD | 15,590.00 USD | `-15.87%` | `190.89` |
| `Live` | `Long` | `81.75` | 21,480,000.00 USD | 0.00 USD | 19,020.00 USD | `-15.77%` | `232.64` |
| `Live` | `Long` | `81.85` | 21,460,000.00 USD | 0.00 USD | 36,460.00 USD | `-15.67%` | `445.40` |
| `Live` | `Long` | `81.95` | 21,420,000.00 USD | 0.00 USD | 22,190.00 USD | `-15.56%` | `270.82` |
| `Live` | `Long` | `82.05` | 21,400,000.00 USD | 0.00 USD | 117,060.00 USD | `-15.46%` | `1,426.69` |
| `Live` | `Long` | `82.15` | 21,290,000.00 USD | 0.00 USD | 808,740.00 USD | `-15.36%` | `9,844.70` |
| `Live` | `Long` | `82.25` | 20,480,000.00 USD | 0.00 USD | 50,310.00 USD | `-15.25%` | `611.69` |
| `Live` | `Long` | `82.35` | 20,430,000.00 USD | 0.00 USD | 166,860.00 USD | `-15.15%` | `2,026.20` |
| `Live` | `Long` | `82.45` | 20,260,000.00 USD | 0.00 USD | 214,440.00 USD | `-15.05%` | `2,600.88` |
| `Live` | `Long` | `82.55` | 20,050,000.00 USD | 0.00 USD | 27,730.00 USD | `-14.95%` | `335.97` |
| `Live` | `Long` | `82.65` | 20,020,000.00 USD | 0.00 USD | 98,590.00 USD | `-14.84%` | `1,192.87` |
| `Live` | `Long` | `82.75` | 19,920,000.00 USD | 0.00 USD | 7,950.00 USD | `-14.74%` | `96.13` |
| `Live` | `Long` | `82.85` | 19,910,000.00 USD | 0.00 USD | 23,000.00 USD | `-14.64%` | `277.57` |
| `Live` | `Long` | `82.95` | 19,890,000.00 USD | 0.00 USD | 29,750.00 USD | `-14.53%` | `358.59` |
| `Live` | `Long` | `83.05` | 19,860,000.00 USD | 0.00 USD | 137,530.00 USD | `-14.43%` | `1,655.98` |
| `Live` | `Long` | `83.15` | 19,720,000.00 USD | 0.00 USD | 52,900.00 USD | `-14.33%` | `636.22` |
| `Live` | `Long` | `83.25` | 19,670,000.00 USD | 0.00 USD | 153,060.00 USD | `-14.22%` | `1,838.55` |
| `Live` | `Long` | `83.35` | 19,510,000.00 USD | 0.00 USD | 637,030.00 USD | `-14.12%` | `7,642.86` |
| `Live` | `Long` | `83.45` | 18,880,000.00 USD | 0.00 USD | 55,880.00 USD | `-14.02%` | `669.57` |
| `Live` | `Long` | `83.55` | 18,820,000.00 USD | 0.00 USD | 65,570.00 USD | `-13.91%` | `784.75` |
| `Live` | `Long` | `83.65` | 18,760,000.00 USD | 0.00 USD | 76,120.00 USD | `-13.81%` | `909.99` |
| `Live` | `Long` | `83.75` | 18,680,000.00 USD | 0.00 USD | 81,510.00 USD | `-13.71%` | `973.24` |
| `Live` | `Long` | `83.85` | 18,600,000.00 USD | 0.00 USD | 13,630.00 USD | `-13.61%` | `162.57` |
| `Live` | `Long` | `83.95` | 18,590,000.00 USD | 0.00 USD | 842,760.00 USD | `-13.50%` | `10,038.79` |
| `Live` | `Long` | `84.05` | 17,740,000.00 USD | 0.00 USD | 113,720.00 USD | `-13.40%` | `1,353.03` |
| `Live` | `Long` | `84.15` | 17,630,000.00 USD | 0.00 USD | 65,310.00 USD | `-13.30%` | `776.06` |
| `Live` | `Long` | `84.25` | 17,560,000.00 USD | 0.00 USD | 46,440.00 USD | `-13.19%` | `551.21` |
| `Live` | `Long` | `84.35` | 17,520,000.00 USD | 0.00 USD | 25,180.00 USD | `-13.09%` | `298.47` |
| `Live` | `Long` | `84.45` | 17,490,000.00 USD | 0.00 USD | 85,770.00 USD | `-12.99%` | `1,015.66` |
| `Live` | `Long` | `84.55` | 17,410,000.00 USD | 0.00 USD | 1,230,000.00 USD | `-12.88%` | `14,555.22` |
| `Live` | `Long` | `84.65` | 16,180,000.00 USD | 0.00 USD | 261,450.00 USD | `-12.78%` | `3,088.60` |
| `Live` | `Long` | `84.75` | 15,910,000.00 USD | 0.00 USD | 289,310.00 USD | `-12.68%` | `3,413.65` |
| `Live` | `Long` | `84.85` | 15,620,000.00 USD | 0.00 USD | 94,510.00 USD | `-12.58%` | `1,113.86` |
| `Live` | `Long` | `84.95` | 15,530,000.00 USD | 0.00 USD | 617.59 USD | `-12.47%` | `7.27` |
| `Live` | `Long` | `85.05` | 15,530,000.00 USD | 0.00 USD | 15,920.00 USD | `-12.37%` | `187.17` |
| `Live` | `Long` | `85.15` | 15,510,000.00 USD | 0.00 USD | 5,400.00 USD | `-12.27%` | `63.38` |
| `Live` | `Long` | `85.25` | 15,510,000.00 USD | 0.00 USD | 609,970.00 USD | `-12.16%` | `7,155.05` |
| `Live` | `Long` | `85.35` | 14,900,000.00 USD | 0.00 USD | 21,250.00 USD | `-12.06%` | `248.94` |
| `Live` | `Long` | `85.45` | 14,880,000.00 USD | 0.00 USD | 52,900.00 USD | `-11.96%` | `619.05` |
| `Live` | `Long` | `85.55` | 14,820,000.00 USD | 0.00 USD | 10,360.00 USD | `-11.85%` | `121.14` |
| `Live` | `Long` | `85.65` | 14,810,000.00 USD | 0.00 USD | 53,210.00 USD | `-11.75%` | `621.29` |
| `Live` | `Long` | `85.75` | 14,760,000.00 USD | 0.00 USD | 23,470.00 USD | `-11.65%` | `273.76` |
| `Live` | `Long` | `85.85` | 14,740,000.00 USD | 0.00 USD | 69,910.00 USD | `-11.55%` | `814.28` |
| `Live` | `Long` | `85.95` | 14,670,000.00 USD | 0.00 USD | 363,970.00 USD | `-11.44%` | `4,234.72` |
| `Live` | `Long` | `86.05` | 14,300,000.00 USD | 0.00 USD | 276,690.00 USD | `-11.34%` | `3,215.43` |
| `Live` | `Long` | `86.15` | 14,030,000.00 USD | 0.00 USD | 68,570.00 USD | `-11.24%` | `795.91` |
| `Live` | `Long` | `86.25` | 13,960,000.00 USD | 0.00 USD | 52,990.00 USD | `-11.13%` | `614.34` |
| `Live` | `Long` | `86.35` | 13,900,000.00 USD | 0.00 USD | 5,680.00 USD | `-11.03%` | `65.77` |
| `Live` | `Long` | `86.45` | 13,900,000.00 USD | 0.00 USD | 187,940.00 USD | `-10.93%` | `2,174.00` |
| `Live` | `Long` | `86.55` | 13,710,000.00 USD | 0.00 USD | 43,510.00 USD | `-10.82%` | `502.72` |
| `Live` | `Long` | `86.65` | 13,670,000.00 USD | 0.00 USD | 190,730.00 USD | `-10.72%` | `2,201.12` |
| `Live` | `Long` | `86.75` | 13,480,000.00 USD | 0.00 USD | 34,660.00 USD | `-10.62%` | `399.50` |
| `Live` | `Long` | `86.85` | 13,440,000.00 USD | 0.00 USD | 78,950.00 USD | `-10.51%` | `909.01` |
| `Live` | `Long` | `86.95` | 13,360,000.00 USD | 0.00 USD | 152,510.00 USD | `-10.41%` | `1,754.01` |
| `Live` | `Long` | `87.05` | 13,210,000.00 USD | 0.00 USD | 30,820.00 USD | `-10.31%` | `354.08` |
| `Live` | `Long` | `87.15` | 13,180,000.00 USD | 0.00 USD | 4,410.00 USD | `-10.21%` | `50.58` |
| `Live` | `Long` | `87.25` | 13,180,000.00 USD | 0.00 USD | 92,480.00 USD | `-10.10%` | `1,059.91` |
| `Live` | `Long` | `87.35` | 13,080,000.00 USD | 0.00 USD | 72,050.00 USD | `-10.00%` | `824.89` |
| `Live` | `Long` | `87.45` | 13,010,000.00 USD | 0.00 USD | 149,740.00 USD | `-9.90%` | `1,712.27` |
| `Live` | `Long` | `87.55` | 12,860,000.00 USD | 0.00 USD | 128,700.00 USD | `-9.79%` | `1,470.04` |
| `Live` | `Long` | `87.65` | 12,730,000.00 USD | 0.00 USD | 105,660.00 USD | `-9.69%` | `1,205.42` |
| `Live` | `Long` | `87.75` | 12,630,000.00 USD | 0.00 USD | 90,160.00 USD | `-9.59%` | `1,027.45` |
| `Live` | `Long` | `87.85` | 12,540,000.00 USD | 0.00 USD | 66,830.00 USD | `-9.48%` | `760.69` |
| `Live` | `Long` | `87.95` | 12,470,000.00 USD | 0.00 USD | 9,000.00 USD | `-9.38%` | `102.33` |
| `Live` | `Long` | `88.05` | 12,460,000.00 USD | 0.00 USD | 157,110.00 USD | `-9.28%` | `1,784.38` |
| `Live` | `Long` | `88.15` | 12,300,000.00 USD | 0.00 USD | 25,750.00 USD | `-9.18%` | `292.10` |
| `Live` | `Long` | `88.25` | 12,280,000.00 USD | 0.00 USD | 74,760.00 USD | `-9.07%` | `847.09` |
| `Live` | `Long` | `88.35` | 12,200,000.00 USD | 0.00 USD | 26,970.00 USD | `-8.97%` | `305.29` |
| `Live` | `Long` | `88.45` | 12,180,000.00 USD | 0.00 USD | 64,640.00 USD | `-8.87%` | `730.78` |
| `Live` | `Long` | `88.55` | 12,110,000.00 USD | 0.00 USD | 267,270.00 USD | `-8.76%` | `3,018.28` |
| `Live` | `Long` | `88.65` | 11,840,000.00 USD | 0.00 USD | 95,980.00 USD | `-8.66%` | `1,082.67` |
| `Live` | `Long` | `88.75` | 11,750,000.00 USD | 0.00 USD | 236,310.00 USD | `-8.56%` | `2,662.68` |
| `Live` | `Long` | `88.85` | 11,510,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-8.45%` | `11,998.13` |
| `Live` | `Long` | `88.95` | 10,450,000.00 USD | 0.00 USD | 32,790.00 USD | `-8.35%` | `368.66` |
| `Live` | `Long` | `89.05` | 10,410,000.00 USD | 0.00 USD | 29,770.00 USD | `-8.25%` | `334.27` |
| `Live` | `Long` | `89.15` | 10,380,000.00 USD | 0.00 USD | 160,380.00 USD | `-8.14%` | `1,798.99` |
| `Live` | `Long` | `89.25` | 10,220,000.00 USD | 0.00 USD | 31,740.00 USD | `-8.04%` | `355.61` |
| `Live` | `Long` | `89.35` | 10,190,000.00 USD | 0.00 USD | 29,540.00 USD | `-7.94%` | `330.60` |
| `Live` | `Long` | `89.45` | 10,160,000.00 USD | 0.00 USD | 429,190.00 USD | `-7.84%` | `4,798.06` |
| `Live` | `Long` | `89.55` | 9,730,000.00 USD | 0.00 USD | 39,790.00 USD | `-7.73%` | `444.38` |
| `Live` | `Long` | `89.65` | 9,690,000.00 USD | 0.00 USD | 17,750.00 USD | `-7.63%` | `197.96` |
| `Live` | `Long` | `89.75` | 9,680,000.00 USD | 0.00 USD | 146,450.00 USD | `-7.53%` | `1,631.73` |
| `Live` | `Long` | `89.85` | 9,530,000.00 USD | 0.00 USD | 59,040.00 USD | `-7.42%` | `657.09` |
| `Live` | `Long` | `89.95` | 9,470,000.00 USD | 0.00 USD | 136,370.00 USD | `-7.32%` | `1,516.04` |
| `Live` | `Long` | `90.05` | 9,330,000.00 USD | 0.00 USD | 73,280.00 USD | `-7.22%` | `813.81` |
| `Live` | `Long` | `90.15` | 9,260,000.00 USD | 0.00 USD | 60,790.00 USD | `-7.11%` | `674.32` |
| `Live` | `Long` | `90.25` | 9,200,000.00 USD | 0.00 USD | 26,880.00 USD | `-7.01%` | `297.79` |
| `Live` | `Long` | `90.35` | 9,170,000.00 USD | 0.00 USD | 77,850.00 USD | `-6.91%` | `861.69` |
| `Live` | `Long` | `90.45` | 9,090,000.00 USD | 0.00 USD | 50,450.00 USD | `-6.81%` | `557.79` |
| `Live` | `Long` | `90.55` | 9,040,000.00 USD | 0.00 USD | 29,950.00 USD | `-6.70%` | `330.71` |
| `Live` | `Long` | `90.65` | 9,010,000.00 USD | 0.00 USD | 131,550.00 USD | `-6.60%` | `1,451.20` |
| `Live` | `Long` | `90.75` | 8,880,000.00 USD | 0.00 USD | 107,810.00 USD | `-6.50%` | `1,187.98` |
| `Live` | `Long` | `90.85` | 8,770,000.00 USD | 0.00 USD | 73,530.00 USD | `-6.39%` | `809.39` |
| `Live` | `Long` | `90.95` | 8,700,000.00 USD | 0.00 USD | 16,410.00 USD | `-6.29%` | `180.44` |
| `Live` | `Long` | `91.05` | 8,680,000.00 USD | 0.00 USD | 389,480.00 USD | `-6.19%` | `4,277.65` |
| `Live` | `Long` | `91.15` | 8,300,000.00 USD | 0.00 USD | 373,670.00 USD | `-6.08%` | `4,099.56` |
| `Live` | `Long` | `91.25` | 7,920,000.00 USD | 0.00 USD | 29,640.00 USD | `-5.98%` | `324.80` |
| `Live` | `Long` | `91.35` | 7,890,000.00 USD | 0.00 USD | 14,960.00 USD | `-5.88%` | `163.74` |
| `Live` | `Long` | `91.45` | 7,880,000.00 USD | 0.00 USD | 331,850.00 USD | `-5.78%` | `3,628.80` |
| `Live` | `Long` | `91.55` | 7,550,000.00 USD | 0.00 USD | 1,210,000.00 USD | `-5.67%` | `13,204.29` |
| `Live` | `Long` | `91.65` | 6,340,000.00 USD | 0.00 USD | 1,430,000.00 USD | `-5.57%` | `15,594.68` |
| `Live` | `Long` | `91.75` | 4,910,000.00 USD | 0.00 USD | 240,910.00 USD | `-5.47%` | `2,625.74` |
| `Live` | `Long` | `91.85` | 4,670,000.00 USD | 0.00 USD | 43,170.00 USD | `-5.36%` | `470.02` |
| `Live` | `Long` | `91.95` | 4,620,000.00 USD | 0.00 USD | 64,120.00 USD | `-5.26%` | `697.35` |
| `Live` | `Long` | `92.05` | 4,560,000.00 USD | 0.00 USD | 168,710.00 USD | `-5.16%` | `1,832.79` |
| `Live` | `Long` | `92.15` | 4,390,000.00 USD | 0.00 USD | 328,530.00 USD | `-5.05%` | `3,565.15` |
| `Live` | `Long` | `92.25` | 4,060,000.00 USD | 0.00 USD | 170,110.00 USD | `-4.95%` | `1,844.03` |
| `Live` | `Long` | `92.35` | 3,890,000.00 USD | 0.00 USD | 304,990.00 USD | `-4.85%` | `3,302.52` |
| `Live` | `Long` | `92.45` | 3,590,000.00 USD | 0.00 USD | 117,820.00 USD | `-4.74%` | `1,274.42` |
| `Live` | `Long` | `92.55` | 3,470,000.00 USD | 0.00 USD | 4,870.00 USD | `-4.64%` | `52.65` |
| `Live` | `Long` | `92.65` | 3,460,000.00 USD | 0.00 USD | 15,170.00 USD | `-4.54%` | `163.78` |
| `Live` | `Long` | `92.75` | 3,450,000.00 USD | 0.00 USD | 4,920.00 USD | `-4.44%` | `53.04` |
| `Live` | `Long` | `92.85` | 3,440,000.00 USD | 0.00 USD | 23,420.00 USD | `-4.33%` | `252.19` |
| `Live` | `Long` | `92.95` | 3,420,000.00 USD | 0.00 USD | 3,780.00 USD | `-4.23%` | `40.66` |
| `Live` | `Long` | `93.05` | 3,420,000.00 USD | 0.00 USD | 29,610.00 USD | `-4.13%` | `318.21` |
| `Live` | `Long` | `93.15` | 3,390,000.00 USD | 0.00 USD | 319,790.00 USD | `-4.02%` | `3,433.03` |
| `Live` | `Long` | `93.25` | 3,070,000.00 USD | 0.00 USD | 105,430.00 USD | `-3.92%` | `1,130.62` |
| `Live` | `Long` | `93.35` | 2,960,000.00 USD | 0.00 USD | 13,390.00 USD | `-3.82%` | `143.46` |
| `Live` | `Long` | `93.45` | 2,950,000.00 USD | 0.00 USD | 8,060.00 USD | `-3.71%` | `86.26` |
| `Live` | `Long` | `93.55` | 2,940,000.00 USD | 0.00 USD | 19,360.00 USD | `-3.61%` | `206.98` |
| `Live` | `Long` | `93.65` | 2,920,000.00 USD | 0.00 USD | 937,160.00 USD | `-3.51%` | `10,007.00` |
| `Live` | `Long` | `93.75` | 1,980,000.00 USD | 0.00 USD | 10,870.00 USD | `-3.41%` | `115.91` |
| `Live` | `Long` | `93.85` | 1,970,000.00 USD | 0.00 USD | 11,870.00 USD | `-3.30%` | `126.50` |
| `Live` | `Long` | `93.95` | 1,960,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-3.20%` | `12,128.34` |
| `Live` | `Long` | `94.05` | 821,600.00 USD | 0.00 USD | 4,190.00 USD | `-3.10%` | `44.53` |
| `Live` | `Long` | `94.15` | 817,410.00 USD | 0.00 USD | 29,950.00 USD | `-2.99%` | `318.16` |
| `Live` | `Long` | `94.25` | 787,460.00 USD | 0.00 USD | 8,860.00 USD | `-2.89%` | `93.98` |
| `Live` | `Long` | `94.35` | 778,600.00 USD | 0.00 USD | 5,200.00 USD | `-2.79%` | `55.11` |
| `Live` | `Long` | `94.45` | 773,400.00 USD | 0.00 USD | 146,220.00 USD | `-2.68%` | `1,548.16` |
| `Live` | `Long` | `94.55` | 627,170.00 USD | 0.00 USD | 60,600.00 USD | `-2.58%` | `640.93` |
| `Live` | `Short` | `94.65` | 28,740.00 USD | 28,740.00 USD | 0.00 USD | `-2.48%` | `303.69` |
| `Live` | `Long` | `94.75` | 566,570.00 USD | 0.00 USD | 82,810.00 USD | `-2.37%` | `873.94` |
| `Live` | `Long` | `94.85` | 483,770.00 USD | 0.00 USD | 54,830.00 USD | `-2.27%` | `578.03` |
| `Live` | `Long` | `94.95` | 428,940.00 USD | 0.00 USD | 58,350.00 USD | `-2.17%` | `614.55` |
| `Live` | `Long` | `95.05` | 370,590.00 USD | 0.00 USD | 57,060.00 USD | `-2.07%` | `600.29` |
| `Live` | `Long` | `95.15` | 313,530.00 USD | 0.00 USD | 21,470.00 USD | `-1.96%` | `225.63` |
| `Live` | `Long` | `95.25` | 292,060.00 USD | 0.00 USD | 42,730.00 USD | `-1.86%` | `448.66` |
| `Live` | `Long` | `95.35` | 249,330.00 USD | 0.00 USD | 7,550.00 USD | `-1.76%` | `79.19` |
| `Live` | `Long` | `95.45` | 241,780.00 USD | 0.00 USD | 24,230.00 USD | `-1.65%` | `253.81` |
| `Live` | `Long` | `95.55` | 217,550.00 USD | 0.00 USD | 44,760.00 USD | `-1.55%` | `468.49` |
| `Live` | `Long` | `95.65` | 172,790.00 USD | 0.00 USD | 92,490.00 USD | `-1.45%` | `966.99` |
| `Live` | `Long` | `95.75` | 80,300.00 USD | 0.00 USD | 49,350.00 USD | `-1.34%` | `515.41` |
| `Live` | `Long` | `95.85` | 30,950.00 USD | 0.00 USD | 30,710.00 USD | `-1.24%` | `320.44` |
| `Live` | `Long` | `95.95` | 231.24 USD | 0.00 USD | 231.24 USD | `-1.14%` | `2.41` |
| `Live` | `Short` | `97.75` | 29,970.00 USD | 1,220.00 USD | 0.00 USD | `+0.72%` | `12.49` |
| `Live` | `Short` | `98.55` | 35,890.00 USD | 5,930.00 USD | 0.00 USD | `+1.54%` | `60.17` |
| `Live` | `Short` | `98.65` | 45,630.00 USD | 9,740.00 USD | 0.00 USD | `+1.64%` | `98.70` |
| `Live` | `Short` | `98.95` | 46,650.00 USD | 1,020.00 USD | 0.00 USD | `+1.95%` | `10.28` |
| `Live` | `Short` | `99.05` | 50,260.00 USD | 3,610.00 USD | 0.00 USD | `+2.06%` | `36.45` |
| `Live` | `Short` | `99.15` | 1,160,000.00 USD | 1,110,000.00 USD | 0.00 USD | `+2.16%` | `11,226.96` |
| `Live` | `Short` | `99.25` | 1,240,000.00 USD | 72,450.00 USD | 0.00 USD | `+2.26%` | `729.96` |
| `Live` | `Short` | `99.35` | 1,330,000.00 USD | 92,510.00 USD | 0.00 USD | `+2.36%` | `931.19` |
| `Live` | `Short` | `99.45` | 1,350,000.00 USD | 19,710.00 USD | 0.00 USD | `+2.47%` | `198.16` |
| `Live` | `Short` | `99.55` | 1,490,000.00 USD | 138,120.00 USD | 0.00 USD | `+2.57%` | `1,387.43` |
| `Live` | `Short` | `99.65` | 1,500,000.00 USD | 9,360.00 USD | 0.00 USD | `+2.67%` | `93.92` |
| `Live` | `Short` | `99.75` | 1,530,000.00 USD | 33,470.00 USD | 0.00 USD | `+2.78%` | `335.55` |
| `Live` | `Short` | `99.85` | 1,530,000.00 USD | 883.67 USD | 0.00 USD | `+2.88%` | `8.85` |
| `Live` | `Short` | `99.95` | 1,530,000.00 USD | 4,010.00 USD | 0.00 USD | `+2.98%` | `40.15` |
| `Live` | `Short` | `100.05` | 1,570,000.00 USD | 36,990.00 USD | 0.00 USD | `+3.09%` | `369.67` |
| `Live` | `Short` | `100.15` | 1,600,000.00 USD | 25,710.00 USD | 0.00 USD | `+3.19%` | `256.74` |
| `Live` | `Short` | `100.25` | 1,940,000.00 USD | 347,460.00 USD | 0.00 USD | `+3.29%` | `3,465.93` |
| `Live` | `Short` | `100.35` | 2,340,000.00 USD | 391,910.00 USD | 0.00 USD | `+3.39%` | `3,905.45` |
| `Live` | `Short` | `100.45` | 2,360,000.00 USD | 26,900.00 USD | 0.00 USD | `+3.50%` | `267.76` |
| `Live` | `Short` | `100.55` | 2,360,000.00 USD | 1,510.00 USD | 0.00 USD | `+3.60%` | `15.00` |
| `Live` | `Short` | `100.65` | 2,470,000.00 USD | 101,930.00 USD | 0.00 USD | `+3.70%` | `1,012.76` |
| `Live` | `Short` | `100.75` | 2,490,000.00 USD | 19,590.00 USD | 0.00 USD | `+3.81%` | `194.44` |
| `Live` | `Short` | `100.85` | 2,550,000.00 USD | 62,360.00 USD | 0.00 USD | `+3.91%` | `618.31` |
| `Live` | `Short` | `100.95` | 2,550,000.00 USD | 498.69 USD | 0.00 USD | `+4.01%` | `4.94` |
| `Live` | `Short` | `101.05` | 2,550,000.00 USD | 698.26 USD | 0.00 USD | `+4.12%` | `6.91` |
| `Live` | `Short` | `101.15` | 2,560,000.00 USD | 12,940.00 USD | 0.00 USD | `+4.22%` | `127.95` |
| `Live` | `Short` | `101.25` | 2,560,000.00 USD | 769.50 USD | 0.00 USD | `+4.32%` | `7.60` |
| `Live` | `Short` | `101.45` | 2,560,000.00 USD | 118.70 USD | 0.00 USD | `+4.53%` | `1.17` |
| `Live` | `Short` | `101.55` | 2,570,000.00 USD | 2,790.00 USD | 0.00 USD | `+4.63%` | `27.47` |
| `Live` | `Short` | `101.65` | 2,570,000.00 USD | 3,870.00 USD | 0.00 USD | `+4.73%` | `38.10` |
| `Live` | `Short` | `101.95` | 2,570,000.00 USD | 1,760.00 USD | 0.00 USD | `+5.04%` | `17.31` |
| `Live` | `Short` | `102.05` | 2,580,000.00 USD | 4,280.00 USD | 0.00 USD | `+5.15%` | `41.98` |
| `Live` | `Short` | `102.15` | 2,580,000.00 USD | 719.14 USD | 0.00 USD | `+5.25%` | `7.04` |
| `Live` | `Short` | `102.25` | 2,580,000.00 USD | 1,170.00 USD | 0.00 USD | `+5.35%` | `11.44` |
| `Live` | `Short` | `102.55` | 2,580,000.00 USD | 6,330.00 USD | 0.00 USD | `+5.66%` | `61.77` |
| `Live` | `Short` | `102.65` | 2,590,000.00 USD | 1,500.00 USD | 0.00 USD | `+5.76%` | `14.61` |
| `Live` | `Short` | `102.75` | 2,590,000.00 USD | 3,240.00 USD | 0.00 USD | `+5.87%` | `31.50` |
| `Live` | `Short` | `102.95` | 2,590,000.00 USD | 4,150.00 USD | 0.00 USD | `+6.07%` | `40.32` |
| `Live` | `Short` | `103.05` | 2,590,000.00 USD | 692.50 USD | 0.00 USD | `+6.18%` | `6.72` |
| `Live` | `Short` | `103.15` | 2,600,000.00 USD | 11,000.00 USD | 0.00 USD | `+6.28%` | `106.62` |
| `Live` | `Short` | `103.25` | 2,610,000.00 USD | 863.17 USD | 0.00 USD | `+6.38%` | `8.36` |
| `Live` | `Short` | `103.35` | 2,610,000.00 USD | 385.50 USD | 0.00 USD | `+6.49%` | `3.73` |
| `Live` | `Short` | `103.45` | 2,610,000.00 USD | 3,300.00 USD | 0.00 USD | `+6.59%` | `31.94` |
| `Live` | `Short` | `103.65` | 2,610,000.00 USD | 4,360.00 USD | 0.00 USD | `+6.80%` | `42.09` |
| `Live` | `Short` | `103.75` | 2,870,000.00 USD | 261,050.00 USD | 0.00 USD | `+6.90%` | `2,516.13` |
| `Live` | `Short` | `103.85` | 2,890,000.00 USD | 13,560.00 USD | 0.00 USD | `+7.00%` | `130.56` |
| `Live` | `Short` | `103.95` | 2,890,000.00 USD | 827.44 USD | 0.00 USD | `+7.10%` | `7.96` |
| `Live` | `Short` | `104.05` | 2,890,000.00 USD | 775.17 USD | 0.00 USD | `+7.21%` | `7.45` |
| `Live` | `Short` | `104.15` | 2,890,000.00 USD | 4,830.00 USD | 0.00 USD | `+7.31%` | `46.35` |
| `Live` | `Short` | `104.25` | 2,940,000.00 USD | 41,100.00 USD | 0.00 USD | `+7.41%` | `394.28` |
| `Live` | `Short` | `104.35` | 2,950,000.00 USD | 11,630.00 USD | 0.00 USD | `+7.52%` | `111.45` |
| `Live` | `Short` | `104.45` | 2,960,000.00 USD | 8,550.00 USD | 0.00 USD | `+7.62%` | `81.88` |
| `Live` | `Short` | `104.55` | 2,960,000.00 USD | 575.03 USD | 0.00 USD | `+7.72%` | `5.50` |
| `Live` | `Short` | `104.65` | 2,960,000.00 USD | 401.86 USD | 0.00 USD | `+7.83%` | `3.84` |
| `Live` | `Short` | `104.75` | 2,960,000.00 USD | 3,620.00 USD | 0.00 USD | `+7.93%` | `34.59` |
| `Live` | `Short` | `104.95` | 3,090,000.00 USD | 126,400.00 USD | 0.00 USD | `+8.13%` | `1,204.39` |
| `Live` | `Short` | `105.05` | 3,090,000.00 USD | 578.83 USD | 0.00 USD | `+8.24%` | `5.51` |
| `Live` | `Short` | `105.15` | 3,110,000.00 USD | 19,740.00 USD | 0.00 USD | `+8.34%` | `187.73` |
| `Live` | `Short` | `105.25` | 3,110,000.00 USD | 2,110.00 USD | 0.00 USD | `+8.44%` | `20.07` |
| `Live` | `Short` | `105.35` | 3,120,000.00 USD | 6,840.00 USD | 0.00 USD | `+8.55%` | `64.89` |
| `Live` | `Short` | `105.45` | 3,650,000.00 USD | 531,450.00 USD | 0.00 USD | `+8.65%` | `5,039.81` |
| `Live` | `Short` | `105.55` | 3,650,000.00 USD | 4,180.00 USD | 0.00 USD | `+8.75%` | `39.61` |
| `Live` | `Short` | `105.65` | 3,660,000.00 USD | 3,540.00 USD | 0.00 USD | `+8.86%` | `33.54` |
| `Live` | `Short` | `105.85` | 3,750,000.00 USD | 91,370.00 USD | 0.00 USD | `+9.06%` | `863.23` |
| `Live` | `Short` | `105.95` | 3,750,000.00 USD | 840.18 USD | 0.00 USD | `+9.16%` | `7.93` |
| `Live` | `Short` | `106.05` | 3,780,000.00 USD | 33,380.00 USD | 0.00 USD | `+9.27%` | `314.77` |
| `Live` | `Short` | `106.15` | 3,790,000.00 USD | 5,820.00 USD | 0.00 USD | `+9.37%` | `54.81` |
| `Live` | `Short` | `106.35` | 4,040,000.00 USD | 252,430.00 USD | 0.00 USD | `+9.58%` | `2,373.61` |
| `Live` | `Short` | `106.45` | 4,070,000.00 USD | 33,200.00 USD | 0.00 USD | `+9.68%` | `311.90` |
| `Live` | `Short` | `106.55` | 4,070,000.00 USD | 218.43 USD | 0.00 USD | `+9.78%` | `2.05` |
| `Live` | `Short` | `106.65` | 4,080,000.00 USD | 6,460.00 USD | 0.00 USD | `+9.89%` | `60.58` |
| `Live` | `Short` | `106.85` | 4,560,000.00 USD | 479,570.00 USD | 0.00 USD | `+10.09%` | `4,488.25` |
| `Live` | `Short` | `106.95` | 4,560,000.00 USD | 131.55 USD | 0.00 USD | `+10.20%` | `1.23` |
| `Live` | `Short` | `107.05` | 4,570,000.00 USD | 14,820.00 USD | 0.00 USD | `+10.30%` | `138.41` |
| `Live` | `Short` | `107.15` | 4,580,000.00 USD | 3,060.00 USD | 0.00 USD | `+10.40%` | `28.58` |
| `Live` | `Short` | `107.25` | 4,620,000.00 USD | 46,610.00 USD | 0.00 USD | `+10.50%` | `434.60` |
| `Live` | `Short` | `107.35` | 4,620,000.00 USD | 766.48 USD | 0.00 USD | `+10.61%` | `7.14` |
| `Live` | `Short` | `107.45` | 4,660,000.00 USD | 32,580.00 USD | 0.00 USD | `+10.71%` | `303.18` |
| `Live` | `Short` | `107.55` | 4,660,000.00 USD | 221.55 USD | 0.00 USD | `+10.81%` | `2.06` |
| `Live` | `Short` | `107.75` | 4,810,000.00 USD | 150,290.00 USD | 0.00 USD | `+11.02%` | `1,394.81` |
| `Live` | `Short` | `107.85` | 4,950,000.00 USD | 143,860.00 USD | 0.00 USD | `+11.12%` | `1,333.92` |
| `Live` | `Short` | `108.05` | 4,950,000.00 USD | 1,080.00 USD | 0.00 USD | `+11.33%` | `10.04` |
| `Live` | `Short` | `108.15` | 4,950,000.00 USD | 1,150.00 USD | 0.00 USD | `+11.43%` | `10.66` |
| `Live` | `Short` | `108.25` | 5,110,000.00 USD | 161,430.00 USD | 0.00 USD | `+11.53%` | `1,491.26` |
| `Live` | `Short` | `108.35` | 5,120,000.00 USD | 3,470.00 USD | 0.00 USD | `+11.64%` | `32.00` |
| `Live` | `Short` | `108.45` | 5,230,000.00 USD | 108,080.00 USD | 0.00 USD | `+11.74%` | `996.61` |
| `Live` | `Short` | `108.55` | 5,230,000.00 USD | 261.61 USD | 0.00 USD | `+11.84%` | `2.41` |
| `Live` | `Short` | `108.65` | 5,230,000.00 USD | 7,980.00 USD | 0.00 USD | `+11.95%` | `73.48` |
| `Live` | `Short` | `108.85` | 5,280,000.00 USD | 41,550.00 USD | 0.00 USD | `+12.15%` | `381.74` |
| `Live` | `Short` | `108.95` | 5,280,000.00 USD | 3,170.00 USD | 0.00 USD | `+12.26%` | `29.10` |
| `Live` | `Short` | `109.05` | 5,280,000.00 USD | 163.58 USD | 0.00 USD | `+12.36%` | `1.50` |
| `Live` | `Short` | `109.15` | 5,300,000.00 USD | 17,440.00 USD | 0.00 USD | `+12.46%` | `159.75` |
| `Live` | `Short` | `109.25` | 5,300,000.00 USD | 2,720.00 USD | 0.00 USD | `+12.57%` | `24.90` |
| `Live` | `Short` | `109.35` | 5,300,000.00 USD | 247.13 USD | 0.00 USD | `+12.67%` | `2.26` |
| `Live` | `Short` | `109.45` | 5,300,000.00 USD | 620.58 USD | 0.00 USD | `+12.77%` | `5.67` |
| `Live` | `Short` | `109.55` | 5,300,000.00 USD | 356.04 USD | 0.00 USD | `+12.87%` | `3.25` |
| `Live` | `Short` | `109.65` | 5,750,000.00 USD | 447,000.00 USD | 0.00 USD | `+12.98%` | `4,076.57` |
| `Live` | `Short` | `109.75` | 5,750,000.00 USD | 111.95 USD | 0.00 USD | `+13.08%` | `1.02` |
| `Live` | `Short` | `109.85` | 5,750,000.00 USD | 459.17 USD | 0.00 USD | `+13.18%` | `4.18` |
| `Live` | `Short` | `109.95` | 5,750,000.00 USD | 4,480.00 USD | 0.00 USD | `+13.29%` | `40.77` |
| `Live` | `Short` | `110.05` | 5,770,000.00 USD | 14,790.00 USD | 0.00 USD | `+13.39%` | `134.36` |
| `Live` | `Short` | `110.15` | 5,770,000.00 USD | 194.97 USD | 0.00 USD | `+13.49%` | `1.77` |
| `Live` | `Short` | `110.25` | 5,770,000.00 USD | 226.01 USD | 0.00 USD | `+13.60%` | `2.05` |
| `Live` | `Short` | `110.35` | 5,770,000.00 USD | 385.12 USD | 0.00 USD | `+13.70%` | `3.49` |
| `Live` | `Short` | `110.45` | 5,910,000.00 USD | 143,580.00 USD | 0.00 USD | `+13.80%` | `1,299.91` |
| `Live` | `Short` | `110.55` | 5,910,000.00 USD | 1,820.00 USD | 0.00 USD | `+13.90%` | `16.50` |
| `Live` | `Short` | `110.85` | 5,920,000.00 USD | 1,090.00 USD | 0.00 USD | `+14.21%` | `9.87` |
| `Live` | `Short` | `110.95` | 5,920,000.00 USD | 4,450.00 USD | 0.00 USD | `+14.32%` | `40.12` |
| `Live` | `Short` | `111.15` | 5,950,000.00 USD | 29,660.00 USD | 0.00 USD | `+14.52%` | `266.81` |
| `Live` | `Short` | `111.35` | 5,950,000.00 USD | 390.84 USD | 0.00 USD | `+14.73%` | `3.51` |
| `Live` | `Short` | `111.45` | 5,950,000.00 USD | 841.45 USD | 0.00 USD | `+14.83%` | `7.55` |
| `Live` | `Short` | `111.55` | 5,950,000.00 USD | 892.40 USD | 0.00 USD | `+14.93%` | `8.00` |
| `Live` | `Short` | `111.65` | 5,950,000.00 USD | 199.85 USD | 0.00 USD | `+15.04%` | `1.79` |
| `Live` | `Short` | `111.75` | 5,950,000.00 USD | 169.86 USD | 0.00 USD | `+15.14%` | `1.52` |
| `Live` | `Short` | `111.85` | 5,970,000.00 USD | 15,880.00 USD | 0.00 USD | `+15.24%` | `141.95` |
| `Live` | `Short` | `111.95` | 5,970,000.00 USD | 223.90 USD | 0.00 USD | `+15.35%` | `2.00` |
| `Live` | `Short` | `112.15` | 5,970,000.00 USD | 528.23 USD | 0.00 USD | `+15.55%` | `4.71` |
| `Live` | `Short` | `112.25` | 6,230,000.00 USD | 261,320.00 USD | 0.00 USD | `+15.66%` | `2,328.02` |
| `Live` | `Short` | `112.35` | 6,230,000.00 USD | 1,910.00 USD | 0.00 USD | `+15.76%` | `17.00` |
| `Live` | `Short` | `112.45` | 6,240,000.00 USD | 5,670.00 USD | 0.00 USD | `+15.86%` | `50.42` |
| `Live` | `Short` | `112.55` | 6,240,000.00 USD | 1,070.00 USD | 0.00 USD | `+15.97%` | `9.55` |
| `Live` | `Short` | `112.65` | 6,240,000.00 USD | 707.44 USD | 0.00 USD | `+16.07%` | `6.28` |
| `Live` | `Short` | `112.75` | 6,360,000.00 USD | 118,640.00 USD | 0.00 USD | `+16.17%` | `1,052.24` |
| `Live` | `Short` | `112.85` | 6,470,000.00 USD | 108,760.00 USD | 0.00 USD | `+16.27%` | `963.76` |
| `Live` | `Short` | `113.05` | 6,470,000.00 USD | 406.98 USD | 0.00 USD | `+16.48%` | `3.60` |
| `Live` | `Short` | `113.15` | 6,480,000.00 USD | 9,560.00 USD | 0.00 USD | `+16.58%` | `84.51` |
| `Live` | `Short` | `113.25` | 6,480,000.00 USD | 698.75 USD | 0.00 USD | `+16.69%` | `6.17` |
| `Live` | `Short` | `113.35` | 6,480,000.00 USD | 4,120.00 USD | 0.00 USD | `+16.79%` | `36.36` |
| `Live` | `Short` | `113.45` | 6,490,000.00 USD | 5,120.00 USD | 0.00 USD | `+16.89%` | `45.09` |
| `Live` | `Short` | `113.65` | 6,590,000.00 USD | 105,650.00 USD | 0.00 USD | `+17.10%` | `929.65` |
| `Live` | `Short` | `113.75` | 6,600,000.00 USD | 5,200.00 USD | 0.00 USD | `+17.20%` | `45.74` |
| `Live` | `Short` | `113.85` | 6,600,000.00 USD | 461.09 USD | 0.00 USD | `+17.30%` | `4.05` |
| `Live` | `Short` | `113.95` | 6,620,000.00 USD | 21,840.00 USD | 0.00 USD | `+17.41%` | `191.69` |
| `Live` | `Short` | `114.05` | 6,650,000.00 USD | 31,740.00 USD | 0.00 USD | `+17.51%` | `278.26` |
| `Live` | `Short` | `114.25` | 6,660,000.00 USD | 6,230.00 USD | 0.00 USD | `+17.72%` | `54.51` |
| `Live` | `Short` | `114.45` | 6,660,000.00 USD | 3,830.00 USD | 0.00 USD | `+17.92%` | `33.46` |
| `Live` | `Short` | `114.65` | 6,660,000.00 USD | 3,430.00 USD | 0.00 USD | `+18.13%` | `29.93` |
| `Live` | `Short` | `114.95` | 6,670,000.00 USD | 1,260.00 USD | 0.00 USD | `+18.44%` | `10.94` |
| `Live` | `Short` | `115.05` | 7,240,000.00 USD | 569,550.00 USD | 0.00 USD | `+18.54%` | `4,950.49` |
| `Live` | `Short` | `115.15` | 7,240,000.00 USD | 1,100.00 USD | 0.00 USD | `+18.64%` | `9.52` |
| `Live` | `Short` | `115.35` | 7,240,000.00 USD | 161.49 USD | 0.00 USD | `+18.85%` | `1.40` |
| `Live` | `Short` | `115.45` | 8,120,000.00 USD | 879,040.00 USD | 0.00 USD | `+18.95%` | `7,614.00` |
| `Live` | `Short` | `115.55` | 8,280,000.00 USD | 167,330.00 USD | 0.00 USD | `+19.06%` | `1,448.12` |
| `Live` | `Short` | `115.65` | 8,300,000.00 USD | 14,750.00 USD | 0.00 USD | `+19.16%` | `127.54` |
| `Live` | `Short` | `115.75` | 8,300,000.00 USD | 6,060.00 USD | 0.00 USD | `+19.26%` | `52.35` |
| `Live` | `Short` | `115.85` | 8,300,000.00 USD | 512.06 USD | 0.00 USD | `+19.37%` | `4.42` |
| `Live` | `Short` | `116.05` | 8,310,000.00 USD | 4,450.00 USD | 0.00 USD | `+19.57%` | `38.34` |
| `Live` | `Short` | `116.25` | 8,310,000.00 USD | 180.19 USD | 0.00 USD | `+19.78%` | `1.55` |
| `Live` | `Short` | `116.35` | 8,310,000.00 USD | 4,960.00 USD | 0.00 USD | `+19.88%` | `42.60` |
| `Live` | `Short` | `116.55` | 8,320,000.00 USD | 2,040.00 USD | 0.00 USD | `+20.09%` | `17.52` |
| `Live` | `Short` | `116.65` | 8,320,000.00 USD | 113.15 USD | 0.00 USD | `+20.19%` | `0.97` |
| `Live` | `Short` | `116.75` | 8,320,000.00 USD | 6,020.00 USD | 0.00 USD | `+20.29%` | `51.58` |
| `Live` | `Short` | `116.85` | 8,330,000.00 USD | 10,520.00 USD | 0.00 USD | `+20.40%` | `90.00` |
| `Live` | `Short` | `117.05` | 8,330,000.00 USD | 156.85 USD | 0.00 USD | `+20.60%` | `1.34` |
| `Live` | `Short` | `117.15` | 8,420,000.00 USD | 89,950.00 USD | 0.00 USD | `+20.70%` | `767.80` |
| `Live` | `Short` | `117.35` | 8,430,000.00 USD | 11,610.00 USD | 0.00 USD | `+20.91%` | `98.95` |
| `Live` | `Short` | `117.55` | 13,220,000.00 USD | 4,790,000.00 USD | 0.00 USD | `+21.12%` | `40,718.41` |
| `Live` | `Short` | `117.75` | 13,230,000.00 USD | 10,360.00 USD | 0.00 USD | `+21.32%` | `87.98` |
| `Live` | `Short` | `117.95` | 13,230,000.00 USD | 2,310.00 USD | 0.00 USD | `+21.53%` | `19.61` |
| `Live` | `Short` | `118.25` | 13,230,000.00 USD | 614.90 USD | 0.00 USD | `+21.84%` | `5.20` |
| `Live` | `Short` | `118.45` | 17,740,000.00 USD | 4,510,000.00 USD | 0.00 USD | `+22.04%` | `38,050.04` |
| `Live` | `Short` | `118.55` | 17,750,000.00 USD | 7,700.00 USD | 0.00 USD | `+22.15%` | `64.98` |
| `Live` | `Short` | `118.75` | 17,750,000.00 USD | 309.94 USD | 0.00 USD | `+22.35%` | `2.61` |
| `Live` | `Short` | `119.25` | 17,750,000.00 USD | 240.88 USD | 0.00 USD | `+22.87%` | `2.02` |
| `Live` | `Short` | `119.35` | 17,810,000.00 USD | 57,850.00 USD | 0.00 USD | `+22.97%` | `484.72` |
| `Live` | `Short` | `119.45` | 17,810,000.00 USD | 1,560.00 USD | 0.00 USD | `+23.07%` | `13.05` |
| `Live` | `Short` | `119.55` | 17,820,000.00 USD | 8,970.00 USD | 0.00 USD | `+23.18%` | `75.00` |
| `Live` | `Short` | `119.65` | 17,820,000.00 USD | 470.22 USD | 0.00 USD | `+23.28%` | `3.93` |
| `Live` | `Short` | `119.75` | 17,850,000.00 USD | 28,230.00 USD | 0.00 USD | `+23.38%` | `235.73` |
| `Live` | `Short` | `119.85` | 17,850,000.00 USD | 485.39 USD | 0.00 USD | `+23.49%` | `4.05` |
| `Live` | `Short` | `120.15` | 17,990,000.00 USD | 140,720.00 USD | 0.00 USD | `+23.80%` | `1,171.24` |
| `Live` | `Short` | `120.25` | 17,990,000.00 USD | 453.34 USD | 0.00 USD | `+23.90%` | `3.77` |
| `Live` | `Short` | `120.45` | 17,990,000.00 USD | 145.74 USD | 0.00 USD | `+24.10%` | `1.21` |
| `Live` | `Short` | `120.55` | 17,990,000.00 USD | 1,190.00 USD | 0.00 USD | `+24.21%` | `9.86` |
| `Live` | `Short` | `120.75` | 17,990,000.00 USD | 515.60 USD | 0.00 USD | `+24.41%` | `4.27` |
| `Live` | `Short` | `120.95` | 18,000,000.00 USD | 13,290.00 USD | 0.00 USD | `+24.62%` | `109.91` |
| `Live` | `Short` | `121.05` | 18,060,000.00 USD | 60,530.00 USD | 0.00 USD | `+24.72%` | `500.00` |
| `Live` | `Short` | `121.15` | 18,070,000.00 USD | 2,100.00 USD | 0.00 USD | `+24.83%` | `17.33` |
| `Live` | `Short` | `121.35` | 18,560,000.00 USD | 489,130.00 USD | 0.00 USD | `+25.03%` | `4,030.75` |
| `Live` | `Short` | `121.55` | 18,560,000.00 USD | 5,940.00 USD | 0.00 USD | `+25.24%` | `48.87` |
| `Live` | `Short` | `121.75` | 18,560,000.00 USD | 105.92 USD | 0.00 USD | `+25.44%` | `0.87` |
| `Live` | `Short` | `122.05` | 18,620,000.00 USD | 56,150.00 USD | 0.00 USD | `+25.75%` | `460.06` |
| `Live` | `Short` | `122.15` | 18,620,000.00 USD | 169.79 USD | 0.00 USD | `+25.86%` | `1.39` |
| `Live` | `Short` | `122.25` | 18,620,000.00 USD | 2,330.00 USD | 0.00 USD | `+25.96%` | `19.10` |
| `Live` | `Short` | `122.35` | 19,500,000.00 USD | 881,450.00 USD | 0.00 USD | `+26.06%` | `7,204.35` |
| `Live` | `Short` | `122.45` | 19,520,000.00 USD | 17,500.00 USD | 0.00 USD | `+26.17%` | `142.95` |
| `Live` | `Short` | `122.65` | 19,520,000.00 USD | 116.52 USD | 0.00 USD | `+26.37%` | `0.95` |
| `Live` | `Short` | `122.95` | 19,520,000.00 USD | 4,300.00 USD | 0.00 USD | `+26.68%` | `35.00` |
| `Live` | `Short` | `123.25` | 19,990,000.00 USD | 471,560.00 USD | 0.00 USD | `+26.99%` | `3,826.05` |
| `Live` | `Short` | `123.35` | 20,000,000.00 USD | 2,330.00 USD | 0.00 USD | `+27.09%` | `18.92` |
| `Live` | `Short` | `123.45` | 20,000,000.00 USD | 1,960.00 USD | 0.00 USD | `+27.20%` | `15.87` |
| `Live` | `Short` | `123.65` | 20,120,000.00 USD | 124,510.00 USD | 0.00 USD | `+27.40%` | `1,006.96` |
| `Live` | `Short` | `124.05` | 20,130,000.00 USD | 7,950.00 USD | 0.00 USD | `+27.81%` | `64.10` |
| `Live` | `Short` | `124.15` | 20,130,000.00 USD | 121.67 USD | 0.00 USD | `+27.92%` | `0.98` |
| `Live` | `Short` | `124.25` | 20,150,000.00 USD | 23,360.00 USD | 0.00 USD | `+28.02%` | `188.01` |
| `Live` | `Short` | `124.35` | 20,180,000.00 USD | 29,710.00 USD | 0.00 USD | `+28.12%` | `238.96` |
| `Live` | `Short` | `124.55` | 20,190,000.00 USD | 3,080.00 USD | 0.00 USD | `+28.33%` | `24.76` |
| `Live` | `Short` | `124.65` | 20,190,000.00 USD | 675.60 USD | 0.00 USD | `+28.43%` | `5.42` |
| `Live` | `Short` | `124.75` | 20,190,000.00 USD | 5,330.00 USD | 0.00 USD | `+28.54%` | `42.73` |
| `Live` | `Short` | `124.95` | 20,200,000.00 USD | 2,800.00 USD | 0.00 USD | `+28.74%` | `22.41` |
| `Live` | `Short` | `125.05` | 20,200,000.00 USD | 208.83 USD | 0.00 USD | `+28.84%` | `1.67` |
| `Live` | `Short` | `125.25` | 20,200,000.00 USD | 690.13 USD | 0.00 USD | `+29.05%` | `5.51` |
| `Live` | `Short` | `125.35` | 20,200,000.00 USD | 5,320.00 USD | 0.00 USD | `+29.15%` | `42.44` |
| `Live` | `Short` | `125.45` | 20,200,000.00 USD | 590.87 USD | 0.00 USD | `+29.26%` | `4.71` |
| `Live` | `Short` | `125.55` | 20,250,000.00 USD | 51,130.00 USD | 0.00 USD | `+29.36%` | `407.21` |
| `Live` | `Short` | `125.65` | 20,260,000.00 USD | 1,560.00 USD | 0.00 USD | `+29.46%` | `12.41` |
| `Live` | `Short` | `125.75` | 20,260,000.00 USD | 1,930.00 USD | 0.00 USD | `+29.57%` | `15.31` |
| `Live` | `Short` | `125.85` | 25,690,000.00 USD | 5,430,000.00 USD | 0.00 USD | `+29.67%` | `43,151.65` |
| `Live` | `Short` | `125.95` | 25,690,000.00 USD | 110.84 USD | 0.00 USD | `+29.77%` | `0.88` |
| `Live` | `Short` | `126.05` | 25,690,000.00 USD | 810.50 USD | 0.00 USD | `+29.87%` | `6.43` |
| `Live` | `Short` | `126.15` | 25,690,000.00 USD | 470.54 USD | 0.00 USD | `+29.98%` | `3.73` |
| `Live` | `Short` | `126.35` | 25,690,000.00 USD | 4,090.00 USD | 0.00 USD | `+30.18%` | `32.36` |
| `Live` | `Short` | `126.45` | 25,700,000.00 USD | 5,150.00 USD | 0.00 USD | `+30.29%` | `40.70` |
| `Live` | `Short` | `126.55` | 25,700,000.00 USD | 403.69 USD | 0.00 USD | `+30.39%` | `3.19` |
| `Live` | `Short` | `126.65` | 25,730,000.00 USD | 30,830.00 USD | 0.00 USD | `+30.49%` | `243.46` |
| `Live` | `Short` | `126.85` | 25,730,000.00 USD | 3,870.00 USD | 0.00 USD | `+30.70%` | `30.49` |
| `Live` | `Short` | `127.05` | 25,740,000.00 USD | 2,030.00 USD | 0.00 USD | `+30.91%` | `16.01` |
| `Live` | `Short` | `127.15` | 25,740,000.00 USD | 389.08 USD | 0.00 USD | `+31.01%` | `3.06` |
| `Live` | `Short` | `127.35` | 25,770,000.00 USD | 28,940.00 USD | 0.00 USD | `+31.21%` | `227.26` |
| `Live` | `Short` | `127.45` | 25,770,000.00 USD | 138.92 USD | 0.00 USD | `+31.32%` | `1.09` |
| `Live` | `Short` | `127.65` | 25,770,000.00 USD | 4,840.00 USD | 0.00 USD | `+31.52%` | `37.89` |
| `Live` | `Short` | `127.75` | 25,790,000.00 USD | 20,800.00 USD | 0.00 USD | `+31.63%` | `162.83` |
| `Live` | `Short` | `127.85` | 25,790,000.00 USD | 388.66 USD | 0.00 USD | `+31.73%` | `3.04` |
| `Live` | `Short` | `127.95` | 25,800,000.00 USD | 10,510.00 USD | 0.00 USD | `+31.83%` | `82.13` |
| `Live` | `Short` | `128.05` | 25,920,000.00 USD | 116,190.00 USD | 0.00 USD | `+31.94%` | `907.38` |
| `Live` | `Short` | `128.15` | 25,920,000.00 USD | 221.70 USD | 0.00 USD | `+32.04%` | `1.73` |
| `Live` | `Short` | `128.25` | 25,920,000.00 USD | 782.32 USD | 0.00 USD | `+32.14%` | `6.10` |
| `Live` | `Short` | `128.35` | 25,920,000.00 USD | 195.09 USD | 0.00 USD | `+32.24%` | `1.52` |
| `Live` | `Short` | `128.65` | 25,920,000.00 USD | 788.62 USD | 0.00 USD | `+32.55%` | `6.13` |
| `Live` | `Short` | `128.75` | 25,940,000.00 USD | 18,730.00 USD | 0.00 USD | `+32.66%` | `145.45` |
| `Live` | `Short` | `128.85` | 25,970,000.00 USD | 32,440.00 USD | 0.00 USD | `+32.76%` | `251.77` |
| `Live` | `Short` | `129.15` | 26,290,000.00 USD | 313,870.00 USD | 0.00 USD | `+33.07%` | `2,430.25` |
| `Live` | `Short` | `129.25` | 26,320,000.00 USD | 32,310.00 USD | 0.00 USD | `+33.17%` | `250.00` |
| `Live` | `Short` | `129.35` | 26,350,000.00 USD | 35,060.00 USD | 0.00 USD | `+33.27%` | `271.06` |
| `Live` | `Short` | `129.45` | 26,350,000.00 USD | 730.10 USD | 0.00 USD | `+33.38%` | `5.64` |
| `Live` | `Short` | `129.55` | 27,050,000.00 USD | 701,210.00 USD | 0.00 USD | `+33.48%` | `5,412.69` |
| `Live` | `Short` | `129.75` | 27,060,000.00 USD | 2,210.00 USD | 0.00 USD | `+33.69%` | `17.05` |
| `Live` | `Short` | `129.85` | 27,060,000.00 USD | 490.83 USD | 0.00 USD | `+33.79%` | `3.78` |
| `Live` | `Short` | `130.25` | 27,060,000.00 USD | 131.55 USD | 0.00 USD | `+34.20%` | `1.01` |
| `Live` | `Short` | `130.35` | 27,070,000.00 USD | 13,360.00 USD | 0.00 USD | `+34.31%` | `102.50` |
| `Live` | `Short` | `130.55` | 27,140,000.00 USD | 69,270.00 USD | 0.00 USD | `+34.51%` | `530.61` |
| `Live` | `Short` | `130.85` | 27,140,000.00 USD | 3,180.00 USD | 0.00 USD | `+34.82%` | `24.34` |
| `Live` | `Short` | `130.95` | 27,150,000.00 USD | 2,070.00 USD | 0.00 USD | `+34.92%` | `15.84` |
| `Live` | `Short` | `131.05` | 27,150,000.00 USD | 188.71 USD | 0.00 USD | `+35.03%` | `1.44` |
| `Live` | `Short` | `131.25` | 27,150,000.00 USD | 1,560.00 USD | 0.00 USD | `+35.23%` | `11.87` |
| `Live` | `Short` | `131.35` | 27,150,000.00 USD | 855.09 USD | 0.00 USD | `+35.34%` | `6.51` |
| `Live` | `Short` | `131.45` | 27,150,000.00 USD | 219.52 USD | 0.00 USD | `+35.44%` | `1.67` |
| `Live` | `Short` | `131.85` | 27,150,000.00 USD | 3,100.00 USD | 0.00 USD | `+35.85%` | `23.54` |
| `Live` | `Short` | `131.95` | 27,150,000.00 USD | 106.88 USD | 0.00 USD | `+35.95%` | `0.81` |
| `Live` | `Short` | `132.05` | 27,170,000.00 USD | 13,650.00 USD | 0.00 USD | `+36.06%` | `103.36` |
| `Live` | `Short` | `132.15` | 27,170,000.00 USD | 3,930.00 USD | 0.00 USD | `+36.16%` | `29.75` |
| `Live` | `Short` | `132.55` | 27,180,000.00 USD | 8,730.00 USD | 0.00 USD | `+36.57%` | `65.85` |
| `Live` | `Short` | `132.65` | 27,210,000.00 USD | 30,100.00 USD | 0.00 USD | `+36.68%` | `226.89` |
| `Live` | `Short` | `132.75` | 27,210,000.00 USD | 136.73 USD | 0.00 USD | `+36.78%` | `1.03` |
| `Live` | `Short` | `132.85` | 27,260,000.00 USD | 49,280.00 USD | 0.00 USD | `+36.88%` | `370.98` |
| `Live` | `Short` | `133.05` | 27,260,000.00 USD | 103.78 USD | 0.00 USD | `+37.09%` | `0.78` |
| `Live` | `Short` | `133.15` | 27,270,000.00 USD | 8,440.00 USD | 0.00 USD | `+37.19%` | `63.42` |
| `Live` | `Short` | `133.25` | 27,270,000.00 USD | 1,330.00 USD | 0.00 USD | `+37.29%` | `9.95` |
| `Live` | `Short` | `133.45` | 27,270,000.00 USD | 1,600.00 USD | 0.00 USD | `+37.50%` | `11.97` |
| `Live` | `Short` | `133.65` | 27,270,000.00 USD | 156.37 USD | 0.00 USD | `+37.71%` | `1.17` |
| `Live` | `Short` | `133.75` | 27,420,000.00 USD | 151,200.00 USD | 0.00 USD | `+37.81%` | `1,130.50` |
| `Live` | `Short` | `133.95` | 27,420,000.00 USD | 503.65 USD | 0.00 USD | `+38.01%` | `3.76` |
| `Live` | `Short` | `134.05` | 27,430,000.00 USD | 12,620.00 USD | 0.00 USD | `+38.12%` | `94.18` |
| `Live` | `Short` | `134.25` | 27,450,000.00 USD | 11,980.00 USD | 0.00 USD | `+38.32%` | `89.25` |
| `Live` | `Short` | `134.65` | 27,460,000.00 USD | 18,040.00 USD | 0.00 USD | `+38.74%` | `134.01` |
| `Live` | `Short` | `135.25` | 27,480,000.00 USD | 14,540.00 USD | 0.00 USD | `+39.35%` | `107.50` |
| `Live` | `Short` | `135.65` | 27,480,000.00 USD | 6,420.00 USD | 0.00 USD | `+39.77%` | `47.30` |
| `Live` | `Short` | `135.75` | 27,480,000.00 USD | 415.39 USD | 0.00 USD | `+39.87%` | `3.06` |
| `Live` | `Short` | `135.85` | 27,490,000.00 USD | 3,250.00 USD | 0.00 USD | `+39.97%` | `23.94` |
| `Live` | `Short` | `135.95` | 27,490,000.00 USD | 504.37 USD | 0.00 USD | `+40.08%` | `3.71` |
| `Live` | `Short` | `136.35` | 27,540,000.00 USD | 49,040.00 USD | 0.00 USD | `+40.49%` | `359.64` |
| `Live` | `Short` | `136.45` | 27,550,000.00 USD | 8,630.00 USD | 0.00 USD | `+40.59%` | `63.22` |
| `Live` | `Short` | `136.55` | 27,550,000.00 USD | 136.55 USD | 0.00 USD | `+40.69%` | `1.00` |
| `Live` | `Short` | `136.65` | 27,550,000.00 USD | 1,110.00 USD | 0.00 USD | `+40.80%` | `8.14` |
| `Live` | `Short` | `136.95` | 27,580,000.00 USD | 34,240.00 USD | 0.00 USD | `+41.11%` | `250.00` |
| `Live` | `Short` | `137.05` | 27,580,000.00 USD | 836.00 USD | 0.00 USD | `+41.21%` | `6.10` |
| `Live` | `Short` | `137.15` | 27,580,000.00 USD | 809.19 USD | 0.00 USD | `+41.31%` | `5.90` |
| `Live` | `Short` | `137.25` | 27,650,000.00 USD | 68,620.00 USD | 0.00 USD | `+41.41%` | `500.00` |
| `Live` | `Short` | `138.05` | 27,650,000.00 USD | 1,270.00 USD | 0.00 USD | `+42.24%` | `9.20` |
| `Live` | `Short` | `138.15` | 27,700,000.00 USD | 50,150.00 USD | 0.00 USD | `+42.34%` | `363.00` |
| `Live` | `Short` | `138.25` | 27,750,000.00 USD | 48,050.00 USD | 0.00 USD | `+42.45%` | `347.53` |
| `Live` | `Short` | `138.35` | 27,750,000.00 USD | 2,060.00 USD | 0.00 USD | `+42.55%` | `14.87` |
| `Live` | `Short` | `138.45` | 27,760,000.00 USD | 7,310.00 USD | 0.00 USD | `+42.65%` | `52.83` |
| `Live` | `Short` | `138.75` | 27,760,000.00 USD | 2,360.00 USD | 0.00 USD | `+42.96%` | `17.04` |
| `Live` | `Short` | `139.15` | 27,770,000.00 USD | 4,720.00 USD | 0.00 USD | `+43.37%` | `33.90` |
| `Live` | `Short` | `139.35` | 27,770,000.00 USD | 4,430.00 USD | 0.00 USD | `+43.58%` | `31.82` |
| `Live` | `Short` | `139.45` | 27,780,000.00 USD | 12,680.00 USD | 0.00 USD | `+43.68%` | `90.91` |
| `Live` | `Short` | `139.55` | 27,790,000.00 USD | 494.01 USD | 0.00 USD | `+43.78%` | `3.54` |
| `Live` | `Short` | `139.75` | 27,790,000.00 USD | 4,870.00 USD | 0.00 USD | `+43.99%` | `34.82` |
| `Live` | `Short` | `139.95` | 27,790,000.00 USD | 2,080.00 USD | 0.00 USD | `+44.20%` | `14.84` |
| `Live` | `Short` | `140.05` | 27,790,000.00 USD | 116.24 USD | 0.00 USD | `+44.30%` | `0.83` |
| `Live` | `Short` | `140.35` | 27,790,000.00 USD | 1,600.00 USD | 0.00 USD | `+44.61%` | `11.39` |
| `Live` | `Short` | `140.45` | 27,800,000.00 USD | 4,870.00 USD | 0.00 USD | `+44.71%` | `34.66` |
| `Live` | `Short` | `140.55` | 27,800,000.00 USD | 702.75 USD | 0.00 USD | `+44.81%` | `5.00` |
| `Live` | `Short` | `140.65` | 27,810,000.00 USD | 7,340.00 USD | 0.00 USD | `+44.92%` | `52.16` |
| `Live` | `Short` | `140.95` | 27,810,000.00 USD | 1,940.00 USD | 0.00 USD | `+45.23%` | `13.73` |
| `Live` | `Short` | `141.05` | 27,880,000.00 USD | 70,450.00 USD | 0.00 USD | `+45.33%` | `499.50` |
| `Live` | `Short` | `141.15` | 32,980,000.00 USD | 5,100,000.00 USD | 0.00 USD | `+45.43%` | `36,104.04` |
| `Live` | `Short` | `141.35` | 32,980,000.00 USD | 210.61 USD | 0.00 USD | `+45.64%` | `1.49` |
| `Live` | `Short` | `141.45` | 33,270,000.00 USD | 289,400.00 USD | 0.00 USD | `+45.74%` | `2,045.98` |
| `Live` | `Short` | `141.55` | 33,270,000.00 USD | 236.39 USD | 0.00 USD | `+45.85%` | `1.67` |
| `Live` | `Short` | `141.75` | 35,220,000.00 USD | 1,950,000.00 USD | 0.00 USD | `+46.05%` | `13,760.46` |
| `Live` | `Short` | `141.95` | 35,220,000.00 USD | 2,640.00 USD | 0.00 USD | `+46.26%` | `18.59` |
| `Live` | `Short` | `142.15` | 35,240,000.00 USD | 23,060.00 USD | 0.00 USD | `+46.46%` | `162.19` |
| `Live` | `Short` | `142.25` | 35,250,000.00 USD | 3,470.00 USD | 0.00 USD | `+46.57%` | `24.41` |
| `Live` | `Short` | `142.45` | 35,250,000.00 USD | 151.00 USD | 0.00 USD | `+46.77%` | `1.06` |
| `Live` | `Short` | `142.75` | 35,250,000.00 USD | 1,150.00 USD | 0.00 USD | `+47.08%` | `8.09` |
| `Live` | `Short` | `142.95` | 35,250,000.00 USD | 283.04 USD | 0.00 USD | `+47.29%` | `1.98` |
| `Live` | `Short` | `143.15` | 35,320,000.00 USD | 73,040.00 USD | 0.00 USD | `+47.49%` | `510.22` |
| `Live` | `Short` | `143.35` | 35,430,000.00 USD | 110,660.00 USD | 0.00 USD | `+47.70%` | `771.94` |
| `Live` | `Short` | `143.55` | 35,430,000.00 USD | 103.36 USD | 0.00 USD | `+47.91%` | `0.72` |
| `Live` | `Short` | `143.65` | 35,430,000.00 USD | 2,840.00 USD | 0.00 USD | `+48.01%` | `19.75` |
| `Live` | `Short` | `144.05` | 35,440,000.00 USD | 3,750.00 USD | 0.00 USD | `+48.42%` | `26.00` |
| `Live` | `Short` | `144.65` | 35,440,000.00 USD | 1,240.00 USD | 0.00 USD | `+49.04%` | `8.60` |
| `Live` | `Short` | `144.85` | 36,040,000.00 USD | 601,130.00 USD | 0.00 USD | `+49.25%` | `4,150.00` |
| `Live` | `Short` | `145.15` | 36,040,000.00 USD | 3,100.00 USD | 0.00 USD | `+49.55%` | `21.34` |
| `Live` | `Short` | `145.35` | 36,060,000.00 USD | 15,840.00 USD | 0.00 USD | `+49.76%` | `109.00` |
| `Live` | `Short` | `145.45` | 36,090,000.00 USD | 28,990.00 USD | 0.00 USD | `+49.86%` | `199.30` |
| `Live` | `Short` | `145.85` | 36,090,000.00 USD | 7,120.00 USD | 0.00 USD | `+50.28%` | `48.84` |
| `Live` | `Short` | `145.95` | 36,200,000.00 USD | 106,560.00 USD | 0.00 USD | `+50.38%` | `730.14` |
| `Live` | `Short` | `146.15` | 36,290,000.00 USD | 89,370.00 USD | 0.00 USD | `+50.58%` | `611.50` |
| `Live` | `Short` | `146.25` | 36,290,000.00 USD | 2,920.00 USD | 0.00 USD | `+50.69%` | `19.95` |
| `Live` | `Short` | `146.35` | 36,300,000.00 USD | 8,510.00 USD | 0.00 USD | `+50.79%` | `58.16` |
| `Live` | `Short` | `146.55` | 36,410,000.00 USD | 103,990.00 USD | 0.00 USD | `+51.00%` | `709.57` |
| `Live` | `Short` | `146.65` | 36,990,000.00 USD | 587,730.00 USD | 0.00 USD | `+51.10%` | `4,007.68` |
| `Live` | `Short` | `146.85` | 37,000,000.00 USD | 2,120.00 USD | 0.00 USD | `+51.31%` | `14.41` |
| `Live` | `Short` | `146.95` | 37,070,000.00 USD | 78,060.00 USD | 0.00 USD | `+51.41%` | `531.18` |
| `Live` | `Short` | `147.05` | 37,070,000.00 USD | 166.17 USD | 0.00 USD | `+51.51%` | `1.13` |
| `Live` | `Short` | `147.15` | 37,080,000.00 USD | 1,730.00 USD | 0.00 USD | `+51.62%` | `11.75` |
| `Live` | `Short` | `147.35` | 37,080,000.00 USD | 169.45 USD | 0.00 USD | `+51.82%` | `1.15` |
| `Live` | `Short` | `147.45` | 37,080,000.00 USD | 204.96 USD | 0.00 USD | `+51.92%` | `1.39` |
| `Live` | `Short` | `147.55` | 37,080,000.00 USD | 1,280.00 USD | 0.00 USD | `+52.03%` | `8.66` |
| `Live` | `Short` | `147.65` | 37,520,000.00 USD | 443,190.00 USD | 0.00 USD | `+52.13%` | `3,001.61` |
| `Live` | `Short` | `147.75` | 37,550,000.00 USD | 28,660.00 USD | 0.00 USD | `+52.23%` | `194.00` |
| `Live` | `Short` | `147.85` | 37,550,000.00 USD | 510.08 USD | 0.00 USD | `+52.34%` | `3.45` |
| `Live` | `Short` | `148.15` | 37,550,000.00 USD | 102.22 USD | 0.00 USD | `+52.65%` | `0.69` |
| `Live` | `Short` | `148.35` | 37,570,000.00 USD | 18,560.00 USD | 0.00 USD | `+52.85%` | `125.13` |
| `Live` | `Short` | `148.45` | 37,570,000.00 USD | 163.29 USD | 0.00 USD | `+52.95%` | `1.10` |
| `Live` | `Short` | `148.55` | 37,910,000.00 USD | 344,780.00 USD | 0.00 USD | `+53.06%` | `2,321.00` |
| `Live` | `Short` | `148.75` | 38,090,000.00 USD | 178,250.00 USD | 0.00 USD | `+53.26%` | `1,198.33` |
| `Live` | `Short` | `148.95` | 38,610,000.00 USD | 521,320.00 USD | 0.00 USD | `+53.47%` | `3,500.00` |
| `Live` | `Short` | `149.15` | 38,610,000.00 USD | 1,120.00 USD | 0.00 USD | `+53.68%` | `7.50` |
| `Live` | `Short` | `149.45` | 40,000,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+53.98%` | `9,282.33` |
| `Live` | `Short` | `149.55` | 40,000,000.00 USD | 116.65 USD | 0.00 USD | `+54.09%` | `0.78` |
| `Live` | `Short` | `149.65` | 40,020,000.00 USD | 16,030.00 USD | 0.00 USD | `+54.19%` | `107.15` |
| `Live` | `Short` | `149.95` | 40,250,000.00 USD | 234,200.00 USD | 0.00 USD | `+54.50%` | `1,561.87` |
| `Live` | `Short` | `150.05` | 40,250,000.00 USD | 2,930.00 USD | 0.00 USD | `+54.60%` | `19.54` |
| `Live` | `Short` | `150.15` | 40,380,000.00 USD | 123,300.00 USD | 0.00 USD | `+54.71%` | `821.21` |
| `Live` | `Short` | `150.85` | 44,950,000.00 USD | 4,570,000.00 USD | 0.00 USD | `+55.43%` | `30,310.49` |
| `Live` | `Short` | `151.05` | 44,950,000.00 USD | 347.42 USD | 0.00 USD | `+55.63%` | `2.30` |
| `Live` | `Short` | `151.15` | 44,960,000.00 USD | 5,550.00 USD | 0.00 USD | `+55.74%` | `36.74` |
| `Live` | `Short` | `151.35` | 44,980,000.00 USD | 22,020.00 USD | 0.00 USD | `+55.94%` | `145.49` |
| `Live` | `Short` | `151.45` | 44,990,000.00 USD | 8,830.00 USD | 0.00 USD | `+56.05%` | `58.32` |
| `Live` | `Short` | `151.95` | 44,990,000.00 USD | 1,920.00 USD | 0.00 USD | `+56.56%` | `12.64` |
| `Live` | `Short` | `152.05` | 46,740,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+56.66%` | `11,488.27` |
| `Live` | `Short` | `152.15` | 48,600,000.00 USD | 1,860,000.00 USD | 0.00 USD | `+56.77%` | `12,257.64` |
| `Live` | `Short` | `152.25` | 48,600,000.00 USD | 200.97 USD | 0.00 USD | `+56.87%` | `1.32` |
| `Live` | `Short` | `152.35` | 48,930,000.00 USD | 331,280.00 USD | 0.00 USD | `+56.97%` | `2,174.44` |
| `Live` | `Short` | `152.45` | 48,940,000.00 USD | 3,150.00 USD | 0.00 USD | `+57.08%` | `20.65` |
| `Live` | `Short` | `152.75` | 48,940,000.00 USD | 2,800.00 USD | 0.00 USD | `+57.38%` | `18.30` |
| `Live` | `Short` | `153.05` | 48,940,000.00 USD | 1,060.00 USD | 0.00 USD | `+57.69%` | `6.95` |
| `Live` | `Short` | `153.15` | 48,940,000.00 USD | 2,810.00 USD | 0.00 USD | `+57.80%` | `18.37` |
| `Live` | `Short` | `153.25` | 48,940,000.00 USD | 239.07 USD | 0.00 USD | `+57.90%` | `1.56` |
| `Live` | `Short` | `153.35` | 48,990,000.00 USD | 46,960.00 USD | 0.00 USD | `+58.00%` | `306.26` |
| `Live` | `Short` | `153.65` | 49,000,000.00 USD | 8,340.00 USD | 0.00 USD | `+58.31%` | `54.29` |
| `Live` | `Short` | `153.85` | 49,000,000.00 USD | 995.41 USD | 0.00 USD | `+58.52%` | `6.47` |
| `Live` | `Short` | `154.15` | 49,000,000.00 USD | 292.89 USD | 0.00 USD | `+58.83%` | `1.90` |
| `Live` | `Short` | `154.25` | 49,000,000.00 USD | 2,340.00 USD | 0.00 USD | `+58.93%` | `15.20` |
| `Live` | `Short` | `154.45` | 49,010,000.00 USD | 4,240.00 USD | 0.00 USD | `+59.14%` | `27.45` |
| `Live` | `Short` | `154.55` | 49,010,000.00 USD | 1,860.00 USD | 0.00 USD | `+59.24%` | `12.03` |
| `Live` | `Short` | `155.05` | 49,010,000.00 USD | 2,340.00 USD | 0.00 USD | `+59.75%` | `15.09` |
| `Live` | `Short` | `155.25` | 49,010,000.00 USD | 1,110.00 USD | 0.00 USD | `+59.96%` | `7.16` |
| `Live` | `Short` | `155.45` | 49,010,000.00 USD | 118.14 USD | 0.00 USD | `+60.17%` | `0.76` |
| `Live` | `Short` | `155.55` | 49,010,000.00 USD | 1,430.00 USD | 0.00 USD | `+60.27%` | `9.22` |
| `Live` | `Short` | `155.75` | 49,020,000.00 USD | 4,050.00 USD | 0.00 USD | `+60.48%` | `26.02` |
| `Live` | `Short` | `156.15` | 49,020,000.00 USD | 8,130.00 USD | 0.00 USD | `+60.89%` | `52.09` |
| `Live` | `Short` | `156.35` | 49,020,000.00 USD | 197.00 USD | 0.00 USD | `+61.09%` | `1.26` |
| `Live` | `Short` | `156.45` | 49,030,000.00 USD | 4,900.00 USD | 0.00 USD | `+61.20%` | `31.29` |
| `Live` | `Short` | `156.85` | 49,040,000.00 USD | 6,280.00 USD | 0.00 USD | `+61.61%` | `40.03` |
| `Live` | `Short` | `157.15` | 49,080,000.00 USD | 49,270.00 USD | 0.00 USD | `+61.92%` | `313.50` |
| `Live` | `Short` | `157.65` | 49,090,000.00 USD | 654.25 USD | 0.00 USD | `+62.43%` | `4.15` |
| `Live` | `Short` | `157.75` | 49,260,000.00 USD | 173,110.00 USD | 0.00 USD | `+62.54%` | `1,097.34` |
| `Live` | `Short` | `158.35` | 49,260,000.00 USD | 299.28 USD | 0.00 USD | `+63.15%` | `1.89` |
| `Live` | `Short` | `158.45` | 49,500,000.00 USD | 237,670.00 USD | 0.00 USD | `+63.26%` | `1,500.00` |
| `Live` | `Short` | `159.05` | 49,540,000.00 USD | 45,380.00 USD | 0.00 USD | `+63.88%` | `285.30` |
| `Live` | `Short` | `159.45` | 49,570,000.00 USD | 27,950.00 USD | 0.00 USD | `+64.29%` | `175.30` |
| `Live` | `Short` | `159.55` | 49,570,000.00 USD | 655.75 USD | 0.00 USD | `+64.39%` | `4.11` |
| `Live` | `Short` | `159.65` | 50,000,000.00 USD | 432,810.00 USD | 0.00 USD | `+64.49%` | `2,711.01` |
| `Live` | `Short` | `159.75` | 53,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | `+64.60%` | `22,770.74` |
| `Live` | `Short` | `160.05` | 53,640,000.00 USD | 448.14 USD | 0.00 USD | `+64.91%` | `2.80` |
| `Live` | `Short` | `160.15` | 54,330,000.00 USD | 683,500.00 USD | 0.00 USD | `+65.01%` | `4,267.86` |
| `Live` | `Short` | `160.35` | 54,330,000.00 USD | 655.83 USD | 0.00 USD | `+65.22%` | `4.09` |
| `Live` | `Short` | `160.55` | 54,430,000.00 USD | 102,250.00 USD | 0.00 USD | `+65.42%` | `636.89` |
| `Live` | `Short` | `161.05` | 54,430,000.00 USD | 2,240.00 USD | 0.00 USD | `+65.94%` | `13.93` |
| `Live` | `Short` | `161.25` | 54,520,000.00 USD | 85,560.00 USD | 0.00 USD | `+66.14%` | `530.61` |
| `Live` | `Short` | `161.35` | 54,540,000.00 USD | 21,430.00 USD | 0.00 USD | `+66.25%` | `132.81` |
| `Live` | `Short` | `161.55` | 54,540,000.00 USD | 410.34 USD | 0.00 USD | `+66.45%` | `2.54` |
| `Live` | `Short` | `161.75` | 54,860,000.00 USD | 323,500.00 USD | 0.00 USD | `+66.66%` | `2,000.00` |
| `Live` | `Short` | `161.85` | 54,880,000.00 USD | 18,950.00 USD | 0.00 USD | `+66.76%` | `117.09` |
| `Live` | `Short` | `161.95` | 55,020,000.00 USD | 144,610.00 USD | 0.00 USD | `+66.86%` | `892.95` |
| `Live` | `Short` | `162.15` | 55,250,000.00 USD | 228,980.00 USD | 0.00 USD | `+67.07%` | `1,412.13` |
| `Live` | `Short` | `162.45` | 55,260,000.00 USD | 5,980.00 USD | 0.00 USD | `+67.38%` | `36.83` |
| `Live` | `Short` | `163.55` | 55,260,000.00 USD | 1,060.00 USD | 0.00 USD | `+68.51%` | `6.49` |
| `Live` | `Short` | `163.85` | 55,260,000.00 USD | 786.48 USD | 0.00 USD | `+68.82%` | `4.80` |
| `Live` | `Short` | `163.95` | 55,470,000.00 USD | 206,830.00 USD | 0.00 USD | `+68.92%` | `1,261.56` |
| `Live` | `Short` | `165.15` | 55,470,000.00 USD | 198.18 USD | 0.00 USD | `+70.16%` | `1.20` |
| `Live` | `Short` | `165.55` | 55,470,000.00 USD | 1,370.00 USD | 0.00 USD | `+70.57%` | `8.29` |
| `Live` | `Short` | `165.85` | 55,470,000.00 USD | 681.64 USD | 0.00 USD | `+70.88%` | `4.11` |
| `Live` | `Short` | `166.15` | 55,470,000.00 USD | 996.90 USD | 0.00 USD | `+71.19%` | `6.00` |
| `Live` | `Short` | `166.25` | 55,490,000.00 USD | 14,070.00 USD | 0.00 USD | `+71.29%` | `84.61` |
| `Live` | `Short` | `166.75` | 55,490,000.00 USD | 3,220.00 USD | 0.00 USD | `+71.81%` | `19.33` |
| `Live` | `Short` | `166.95` | 55,490,000.00 USD | 3,590.00 USD | 0.00 USD | `+72.02%` | `21.53` |
| `Live` | `Short` | `167.65` | 55,490,000.00 USD | 115.68 USD | 0.00 USD | `+72.74%` | `0.69` |
| `Live` | `Short` | `167.75` | 55,500,000.00 USD | 2,520.00 USD | 0.00 USD | `+72.84%` | `15.01` |
| `Live` | `Short` | `168.05` | 55,540,000.00 USD | 46,060.00 USD | 0.00 USD | `+73.15%` | `274.10` |
| `Live` | `Short` | `168.15` | 61,220,000.00 USD | 5,670,000.00 USD | 0.00 USD | `+73.25%` | `33,744.03` |
| `Live` | `Short` | `168.35` | 61,230,000.00 USD | 19,740.00 USD | 0.00 USD | `+73.46%` | `117.24` |
| `Live` | `Short` | `168.55` | 61,350,000.00 USD | 111,680.00 USD | 0.00 USD | `+73.66%` | `662.62` |
| `Live` | `Short` | `168.65` | 61,670,000.00 USD | 325,850.00 USD | 0.00 USD | `+73.77%` | `1,932.10` |
| `Live` | `Short` | `168.75` | 61,700,000.00 USD | 25,920.00 USD | 0.00 USD | `+73.87%` | `153.59` |
| `Live` | `Short` | `169.75` | 61,700,000.00 USD | 100.15 USD | 0.00 USD | `+74.90%` | `0.59` |
| `Live` | `Short` | `170.45` | 61,700,000.00 USD | 446.58 USD | 0.00 USD | `+75.62%` | `2.62` |
| `Live` | `Short` | `171.35` | 61,880,000.00 USD | 181,940.00 USD | 0.00 USD | `+76.55%` | `1,061.79` |
| `Live` | `Short` | `171.45` | 61,880,000.00 USD | 1,570.00 USD | 0.00 USD | `+76.65%` | `9.17` |
| `Live` | `Short` | `172.05` | 61,900,000.00 USD | 20,480.00 USD | 0.00 USD | `+77.27%` | `119.02` |
| `Live` | `Short` | `172.45` | 61,950,000.00 USD | 51,730.00 USD | 0.00 USD | `+77.68%` | `300.00` |
| `Live` | `Short` | `173.05` | 61,990,000.00 USD | 36,010.00 USD | 0.00 USD | `+78.30%` | `208.07` |
| `Live` | `Short` | `173.15` | 62,010,000.00 USD | 15,580.00 USD | 0.00 USD | `+78.40%` | `90.00` |
| `Live` | `Short` | `173.35` | 62,030,000.00 USD | 28,070.00 USD | 0.00 USD | `+78.61%` | `161.92` |
| `Live` | `Short` | `173.45` | 62,050,000.00 USD | 16,540.00 USD | 0.00 USD | `+78.71%` | `95.36` |
| `Live` | `Short` | `173.85` | 62,050,000.00 USD | 695.40 USD | 0.00 USD | `+79.13%` | `4.00` |
| `Live` | `Short` | `174.05` | 62,050,000.00 USD | 205.38 USD | 0.00 USD | `+79.33%` | `1.18` |
| `Live` | `Short` | `174.15` | 62,160,000.00 USD | 104,490.00 USD | 0.00 USD | `+79.43%` | `600.00` |
| `Live` | `Short` | `174.25` | 62,400,000.00 USD | 245,010.00 USD | 0.00 USD | `+79.54%` | `1,406.07` |
| `Live` | `Short` | `174.35` | 62,610,000.00 USD | 205,490.00 USD | 0.00 USD | `+79.64%` | `1,178.60` |
| `Live` | `Short` | `174.75` | 62,610,000.00 USD | 146.79 USD | 0.00 USD | `+80.05%` | `0.84` |
| `Live` | `Short` | `174.95` | 62,610,000.00 USD | 348.15 USD | 0.00 USD | `+80.26%` | `1.99` |
| `Live` | `Short` | `175.45` | 62,610,000.00 USD | 119.31 USD | 0.00 USD | `+80.77%` | `0.68` |
| `Live` | `Short` | `175.75` | 62,610,000.00 USD | 263.62 USD | 0.00 USD | `+81.08%` | `1.50` |
| `Live` | `Short` | `175.85` | 101,290,000.00 USD | 38,690,000.00 USD | 0.00 USD | `+81.19%` | `220,000.19` |
| `Live` | `Short` | `176.15` | 101,310,000.00 USD | 19,920.00 USD | 0.00 USD | `+81.50%` | `113.07` |
| `Live` | `Short` | `176.25` | 101,320,000.00 USD | 625.69 USD | 0.00 USD | `+81.60%` | `3.55` |
| `Live` | `Short` | `176.35` | 104,840,000.00 USD | 3,530,000.00 USD | 0.00 USD | `+81.70%` | `20,000.00` |
| `Live` | `Short` | `176.65` | 104,950,000.00 USD | 105,990.00 USD | 0.00 USD | `+82.01%` | `600.00` |
| `Live` | `Short` | `176.75` | 105,150,000.00 USD | 204,830.00 USD | 0.00 USD | `+82.11%` | `1,158.88` |
| `Live` | `Short` | `176.95` | 105,420,000.00 USD | 265,430.00 USD | 0.00 USD | `+82.32%` | `1,500.00` |
| `Live` | `Short` | `177.55` | 105,440,000.00 USD | 25,670.00 USD | 0.00 USD | `+82.94%` | `144.60` |
| `Live` | `Short` | `177.65` | 105,440,000.00 USD | 637.76 USD | 0.00 USD | `+83.04%` | `3.59` |
| `Live` | `Short` | `177.95` | 105,520,000.00 USD | 78,300.00 USD | 0.00 USD | `+83.35%` | `440.00` |
| `Live` | `Short` | `178.35` | 105,530,000.00 USD | 7,280.00 USD | 0.00 USD | `+83.76%` | `40.84` |
| `Live` | `Short` | `178.45` | 105,530,000.00 USD | 1,320.00 USD | 0.00 USD | `+83.86%` | `7.37` |
| `Live` | `Short` | `179.05` | 105,580,000.00 USD | 44,780.00 USD | 0.00 USD | `+84.48%` | `250.10` |
| `Live` | `Short` | `179.25` | 105,720,000.00 USD | 143,400.00 USD | 0.00 USD | `+84.69%` | `800.00` |
| `Live` | `Short` | `179.45` | 106,760,000.00 USD | 1,040,000.00 USD | 0.00 USD | `+84.90%` | `5,820.70` |
| `Live` | `Short` | `179.65` | 106,770,000.00 USD | 718.60 USD | 0.00 USD | `+85.10%` | `4.00` |
| `Live` | `Short` | `179.75` | 106,770,000.00 USD | 280.41 USD | 0.00 USD | `+85.20%` | `1.56` |
| `Live` | `Short` | `180.25` | 106,770,000.00 USD | 2,030.00 USD | 0.00 USD | `+85.72%` | `11.27` |
| `Live` | `Short` | `180.35` | 108,110,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+85.82%` | `7,439.01` |
| `Live` | `Short` | `180.55` | 108,110,000.00 USD | 3,970.00 USD | 0.00 USD | `+86.03%` | `22.01` |
| `Live` | `Short` | `181.05` | 108,190,000.00 USD | 77,440.00 USD | 0.00 USD | `+86.54%` | `427.73` |
| `Live` | `Short` | `181.15` | 108,210,000.00 USD | 18,120.00 USD | 0.00 USD | `+86.65%` | `100.00` |
| `Live` | `Short` | `181.55` | 108,210,000.00 USD | 254.17 USD | 0.00 USD | `+87.06%` | `1.40` |
| `Live` | `Short` | `181.95` | 108,210,000.00 USD | 1,370.00 USD | 0.00 USD | `+87.47%` | `7.52` |
| `Live` | `Short` | `182.05` | 108,300,000.00 USD | 91,030.00 USD | 0.00 USD | `+87.57%` | `500.00` |
| `Live` | `Short` | `182.15` | 108,310,000.00 USD | 3,990.00 USD | 0.00 USD | `+87.68%` | `21.93` |
| `Live` | `Short` | `182.45` | 108,310,000.00 USD | 248.13 USD | 0.00 USD | `+87.99%` | `1.36` |
| `Live` | `Short` | `183.55` | 108,310,000.00 USD | 9,490.00 USD | 0.00 USD | `+89.12%` | `51.72` |
| `Live` | `Short` | `184.25` | 108,320,000.00 USD | 1,680.00 USD | 0.00 USD | `+89.84%` | `9.12` |
| `Live` | `Short` | `184.65` | 108,320,000.00 USD | 2,080.00 USD | 0.00 USD | `+90.25%` | `11.24` |
| `Live` | `Short` | `184.95` | 108,480,000.00 USD | 165,230.00 USD | 0.00 USD | `+90.56%` | `893.35` |
| `Live` | `Short` | `185.15` | 108,490,000.00 USD | 10,920.00 USD | 0.00 USD | `+90.77%` | `59.00` |
| `Live` | `Short` | `185.25` | 108,500,000.00 USD | 737.29 USD | 0.00 USD | `+90.87%` | `3.98` |
| `Live` | `Short` | `185.45` | 108,500,000.00 USD | 2,770.00 USD | 0.00 USD | `+91.08%` | `14.94` |
| `Live` | `Short` | `185.65` | 108,500,000.00 USD | 137.38 USD | 0.00 USD | `+91.28%` | `0.74` |
| `Live` | `Short` | `185.75` | 108,510,000.00 USD | 8,410.00 USD | 0.00 USD | `+91.39%` | `45.27` |
| `Live` | `Short` | `186.65` | 108,560,000.00 USD | 53,620.00 USD | 0.00 USD | `+92.31%` | `287.30` |
| `Live` | `Short` | `186.85` | 112,300,000.00 USD | 3,740,000.00 USD | 0.00 USD | `+92.52%` | `20,011.72` |
| `Live` | `Short` | `186.95` | 112,300,000.00 USD | 805.75 USD | 0.00 USD | `+92.62%` | `4.31` |
| `Live` | `Short` | `187.05` | 112,310,000.00 USD | 10,740.00 USD | 0.00 USD | `+92.73%` | `57.40` |
| `Live` | `Short` | `187.45` | 112,310,000.00 USD | 2,460.00 USD | 0.00 USD | `+93.14%` | `13.11` |
| `Live` | `Short` | `187.65` | 112,310,000.00 USD | 232.69 USD | 0.00 USD | `+93.34%` | `1.24` |
| `Live` | `Short` | `187.85` | 112,320,000.00 USD | 1,560.00 USD | 0.00 USD | `+93.55%` | `8.32` |
| `Live` | `Short` | `188.55` | 112,320,000.00 USD | 231.92 USD | 0.00 USD | `+94.27%` | `1.23` |
| `Live` | `Short` | `188.65` | 112,340,000.00 USD | 29,110.00 USD | 0.00 USD | `+94.37%` | `154.32` |
| `Live` | `Short` | `188.95` | 112,350,000.00 USD | 1,450.00 USD | 0.00 USD | `+94.68%` | `7.69` |
| `Live` | `Short` | `189.05` | 112,350,000.00 USD | 1,000.00 USD | 0.00 USD | `+94.79%` | `5.30` |
| `Live` | `Short` | `189.25` | 112,350,000.00 USD | 456.09 USD | 0.00 USD | `+94.99%` | `2.41` |
| `Live` | `Short` | `189.65` | 112,350,000.00 USD | 117.58 USD | 0.00 USD | `+95.40%` | `0.62` |
| `Live` | `Short` | `189.85` | 112,350,000.00 USD | 189.85 USD | 0.00 USD | `+95.61%` | `1.00` |
| `Live` | `Short` | `189.95` | 112,630,000.00 USD | 284,930.00 USD | 0.00 USD | `+95.71%` | `1,500.00` |
| `Live` | `Short` | `190.15` | 112,630,000.00 USD | 148.32 USD | 0.00 USD | `+95.92%` | `0.78` |
| `Live` | `Short` | `190.45` | 112,630,000.00 USD | 118.08 USD | 0.00 USD | `+96.23%` | `0.62` |
| `Live` | `Short` | `190.85` | 112,630,000.00 USD | 118.33 USD | 0.00 USD | `+96.64%` | `0.62` |
| `Live` | `Short` | `190.95` | 126,200,000.00 USD | 13,570,000.00 USD | 0.00 USD | `+96.74%` | `71,044.42` |
| `Live` | `Short` | `191.05` | 126,200,000.00 USD | 278.93 USD | 0.00 USD | `+96.85%` | `1.46` |
| `Live` | `Short` | `191.55` | 126,200,000.00 USD | 191.55 USD | 0.00 USD | `+97.36%` | `1.00` |
| `Live` | `Short` | `191.65` | 126,260,000.00 USD | 62,880.00 USD | 0.00 USD | `+97.47%` | `328.11` |
| `Live` | `Short` | `191.95` | 126,260,000.00 USD | 322.48 USD | 0.00 USD | `+97.77%` | `1.68` |
| `Live` | `Short` | `192.55` | 126,270,000.00 USD | 5,460.00 USD | 0.00 USD | `+98.39%` | `28.34` |
| `Live` | `Short` | `192.75` | 126,650,000.00 USD | 385,500.00 USD | 0.00 USD | `+98.60%` | `2,000.00` |
| `Live` | `Short` | `192.85` | 126,670,000.00 USD | 19,780.00 USD | 0.00 USD | `+98.70%` | `102.58` |
| `Live` | `Short` | `193.05` | 126,680,000.00 USD | 9,320.00 USD | 0.00 USD | `+98.91%` | `48.28` |
| `Live` | `Short` | `193.55` | 126,800,000.00 USD | 114,580.00 USD | 0.00 USD | `+99.42%` | `592.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.05` | 10,820,000.00 USD | 0.00 USD | 14,210.00 USD | `-76.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.35` | 10,810,000.00 USD | 0.00 USD | 499.56 USD | `-68.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `32.05` | 10,810,000.00 USD | 0.00 USD | 1,230.00 USD | `-66.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.05` | 10,810,000.00 USD | 0.00 USD | 818.32 USD | `-65.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.85` | 10,810,000.00 USD | 0.00 USD | 1,340.00 USD | `-64.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 10,810,000.00 USD | 0.00 USD | 2,160.00 USD | `-62.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.45` | 10,800,000.00 USD | 0.00 USD | 434.85 USD | `-62.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.05` | 10,800,000.00 USD | 0.00 USD | 267.87 USD | `-60.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.55` | 10,800,000.00 USD | 0.00 USD | 3,460.00 USD | `-59.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.75` | 10,800,000.00 USD | 0.00 USD | 157.01 USD | `-59.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 10,800,000.00 USD | 0.00 USD | 1,050.00 USD | `-58.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.75` | 10,800,000.00 USD | 0.00 USD | 120.66 USD | `-56.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.15` | 10,800,000.00 USD | 0.00 USD | 121.81 USD | `-56.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.55` | 10,800,000.00 USD | 0.00 USD | 170,530.00 USD | `-56.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.75` | 10,630,000.00 USD | 0.00 USD | 105.00 USD | `-54.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 10,630,000.00 USD | 0.00 USD | 64,240.00 USD | `-53.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.75` | 10,560,000.00 USD | 0.00 USD | 251.05 USD | `-51.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.75` | 10,560,000.00 USD | 0.00 USD | 143.25 USD | `-50.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.85` | 10,560,000.00 USD | 0.00 USD | 191.40 USD | `-50.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 10,560,000.00 USD | 0.00 USD | 50,240.00 USD | `-50.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.55` | 10,510,000.00 USD | 0.00 USD | 664.65 USD | `-49.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.75` | 10,510,000.00 USD | 0.00 USD | 103.35 USD | `-49.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 10,510,000.00 USD | 0.00 USD | 4,660.00 USD | `-48.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.25` | 10,510,000.00 USD | 0.00 USD | 107.03 USD | `-48.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 10,510,000.00 USD | 0.00 USD | 102.62 USD | `-47.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.25` | 10,510,000.00 USD | 0.00 USD | 134.28 USD | `-47.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 10,510,000.00 USD | 0.00 USD | 3,950.00 USD | `-46.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.15` | 10,500,000.00 USD | 0.00 USD | 102.74 USD | `-46.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 10,500,000.00 USD | 0.00 USD | 126.12 USD | `-45.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 10,500,000.00 USD | 0.00 USD | 200.15 USD | `-45.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 10,500,000.00 USD | 0.00 USD | 24,450.00 USD | `-45.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 10,480,000.00 USD | 0.00 USD | 1,660.00 USD | `-44.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 10,480,000.00 USD | 0.00 USD | 641.57 USD | `-44.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 10,480,000.00 USD | 0.00 USD | 139.87 USD | `-43.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 10,480,000.00 USD | 0.00 USD | 209.19 USD | `-43.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 10,480,000.00 USD | 0.00 USD | 4,350.00 USD | `-42.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 10,470,000.00 USD | 0.00 USD | 894.56 USD | `-42.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 10,470,000.00 USD | 0.00 USD | 4,930.00 USD | `-42.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 10,470,000.00 USD | 0.00 USD | 6,790.00 USD | `-41.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.35` | 10,460,000.00 USD | 0.00 USD | 265.53 USD | `-40.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.95` | 10,460,000.00 USD | 0.00 USD | 268.31 USD | `-40.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.05` | 10,460,000.00 USD | 0.00 USD | 158.48 USD | `-40.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.15` | 10,460,000.00 USD | 0.00 USD | 3,820.00 USD | `-40.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.25` | 10,450,000.00 USD | 0.00 USD | 428.72 USD | `-39.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.05` | 10,450,000.00 USD | 0.00 USD | 295.25 USD | `-39.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.35` | 10,450,000.00 USD | 0.00 USD | 200.01 USD | `-38.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.55` | 10,450,000.00 USD | 0.00 USD | 1,460.00 USD | `-38.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.95` | 10,450,000.00 USD | 0.00 USD | 9,040.00 USD | `-38.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.05` | 10,440,000.00 USD | 0.00 USD | 35,050.00 USD | `-38.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.15` | 10,410,000.00 USD | 0.00 USD | 2,820.00 USD | `-38.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.25` | 10,410,000.00 USD | 0.00 USD | 488.63 USD | `-37.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.35` | 10,400,000.00 USD | 0.00 USD | 258.90 USD | `-37.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.45` | 10,400,000.00 USD | 0.00 USD | 206.13 USD | `-37.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.55` | 10,400,000.00 USD | 0.00 USD | 724.78 USD | `-37.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.05` | 10,400,000.00 USD | 0.00 USD | 14,350.00 USD | `-37.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.35` | 10,390,000.00 USD | 0.00 USD | 142.33 USD | `-36.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.45` | 10,390,000.00 USD | 0.00 USD | 100.78 USD | `-36.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.55` | 10,390,000.00 USD | 0.00 USD | 243.74 USD | `-36.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.05` | 10,390,000.00 USD | 0.00 USD | 6,720.00 USD | `-36.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.55` | 10,380,000.00 USD | 0.00 USD | 136.98 USD | `-35.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.05` | 10,380,000.00 USD | 0.00 USD | 9,990.00 USD | `-35.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.55` | 10,370,000.00 USD | 0.00 USD | 2,980.00 USD | `-34.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.95` | 10,370,000.00 USD | 0.00 USD | 222.55 USD | `-34.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.25` | 10,370,000.00 USD | 0.00 USD | 163.19 USD | `-33.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.85` | 10,370,000.00 USD | 0.00 USD | 129.70 USD | `-33.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.05` | 10,370,000.00 USD | 0.00 USD | 2,450.00 USD | `-32.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.15` | 10,370,000.00 USD | 0.00 USD | 2,190.00 USD | `-32.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.55` | 10,360,000.00 USD | 0.00 USD | 2,200.00 USD | `-32.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.05` | 10,360,000.00 USD | 0.00 USD | 7,100.00 USD | `-31.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.55` | 10,350,000.00 USD | 0.00 USD | 541.72 USD | `-31.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.05` | 10,350,000.00 USD | 0.00 USD | 335.25 USD | `-30.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.15` | 10,350,000.00 USD | 0.00 USD | 268.60 USD | `-30.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.05` | 10,350,000.00 USD | 0.00 USD | 195.30 USD | `-29.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.45` | 10,350,000.00 USD | 0.00 USD | 7,600.00 USD | `-29.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.55` | 10,350,000.00 USD | 0.00 USD | 5,610.00 USD | `-29.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.65` | 10,340,000.00 USD | 0.00 USD | 552.63 USD | `-29.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.75` | 10,340,000.00 USD | 0.00 USD | 1,200.00 USD | `-29.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.05` | 10,340,000.00 USD | 0.00 USD | 11,360.00 USD | `-28.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.15` | 10,330,000.00 USD | 0.00 USD | 172.18 USD | `-28.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.25` | 10,330,000.00 USD | 0.00 USD | 668.96 USD | `-28.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.65` | 10,330,000.00 USD | 0.00 USD | 107.96 USD | `-28.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.75` | 10,330,000.00 USD | 0.00 USD | 42,360.00 USD | `-28.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.85` | 10,280,000.00 USD | 0.00 USD | 365.32 USD | `-28.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.95` | 10,280,000.00 USD | 0.00 USD | 1,510.00 USD | `-27.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.05` | 10,280,000.00 USD | 0.00 USD | 43,920.00 USD | `-27.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.25` | 10,240,000.00 USD | 0.00 USD | 5,270.00 USD | `-27.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.35` | 10,230,000.00 USD | 0.00 USD | 562.80 USD | `-27.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.55` | 10,230,000.00 USD | 0.00 USD | 681.51 USD | `-27.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.65` | 10,230,000.00 USD | 0.00 USD | 4,920.00 USD | `-27.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.75` | 10,230,000.00 USD | 0.00 USD | 2,790.00 USD | `-27.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.05` | 10,220,000.00 USD | 0.00 USD | 265.02 USD | `-26.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.35` | 10,220,000.00 USD | 0.00 USD | 32,450.00 USD | `-26.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.45` | 10,190,000.00 USD | 0.00 USD | 289.37 USD | `-26.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.65` | 10,190,000.00 USD | 0.00 USD | 1,930.00 USD | `-26.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.75` | 10,190,000.00 USD | 0.00 USD | 235.34 USD | `-26.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.05` | 10,190,000.00 USD | 0.00 USD | 20,410.00 USD | `-25.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.55` | 10,170,000.00 USD | 0.00 USD | 19,560.00 USD | `-25.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.65` | 10,150,000.00 USD | 0.00 USD | 14,530.00 USD | `-25.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.95` | 10,130,000.00 USD | 0.00 USD | 66,160.00 USD | `-24.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.05` | 10,070,000.00 USD | 0.00 USD | 7,970.00 USD | `-24.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.35` | 10,060,000.00 USD | 0.00 USD | 733.50 USD | `-24.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.45` | 10,060,000.00 USD | 0.00 USD | 139.56 USD | `-24.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.05` | 10,060,000.00 USD | 0.00 USD | 510.95 USD | `-23.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.25` | 10,060,000.00 USD | 0.00 USD | 621.47 USD | `-23.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.35` | 10,060,000.00 USD | 0.00 USD | 1,660.00 USD | `-23.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.45` | 10,060,000.00 USD | 0.00 USD | 10,730.00 USD | `-23.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.55` | 10,050,000.00 USD | 0.00 USD | 331.00 USD | `-23.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.75` | 10,040,000.00 USD | 0.00 USD | 28,050.00 USD | `-22.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.05` | 10,020,000.00 USD | 0.00 USD | 30,040.00 USD | `-22.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.35` | 9,990,000.00 USD | 0.00 USD | 153.71 USD | `-22.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.45` | 9,990,000.00 USD | 0.00 USD | 163.73 USD | `-22.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.75` | 9,990,000.00 USD | 0.00 USD | 2,220.00 USD | `-21.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.95` | 9,980,000.00 USD | 0.00 USD | 277.98 USD | `-21.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.05` | 9,980,000.00 USD | 0.00 USD | 8,680.00 USD | `-21.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.15` | 9,980,000.00 USD | 0.00 USD | 254.34 USD | `-21.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.25` | 9,980,000.00 USD | 0.00 USD | 486.47 USD | `-21.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.35` | 9,970,000.00 USD | 0.00 USD | 358.84 USD | `-21.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.55` | 9,970,000.00 USD | 0.00 USD | 4,340.00 USD | `-21.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.65` | 9,970,000.00 USD | 0.00 USD | 536.55 USD | `-21.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.75` | 9,970,000.00 USD | 0.00 USD | 251.74 USD | `-20.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.05` | 9,970,000.00 USD | 0.00 USD | 2,160.00 USD | `-20.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.35` | 9,970,000.00 USD | 0.00 USD | 5,690.00 USD | `-20.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.45` | 9,960,000.00 USD | 0.00 USD | 1,020.00 USD | `-20.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.55` | 9,960,000.00 USD | 0.00 USD | 242.73 USD | `-20.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.95` | 9,960,000.00 USD | 0.00 USD | 155.12 USD | `-19.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.05` | 9,960,000.00 USD | 0.00 USD | 56,850.00 USD | `-19.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.15` | 9,900,000.00 USD | 0.00 USD | 738.52 USD | `-19.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.55` | 9,900,000.00 USD | 0.00 USD | 18,590.00 USD | `-19.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.65` | 9,880,000.00 USD | 0.00 USD | 116.40 USD | `-18.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.75` | 9,880,000.00 USD | 0.00 USD | 379.58 USD | `-18.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.05` | 9,880,000.00 USD | 0.00 USD | 5,300.00 USD | `-18.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.15` | 9,880,000.00 USD | 0.00 USD | 201.04 USD | `-18.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.25` | 9,880,000.00 USD | 0.00 USD | 2,140.00 USD | `-18.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.45` | 9,880,000.00 USD | 0.00 USD | 5,850.00 USD | `-18.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.65` | 9,870,000.00 USD | 0.00 USD | 238.95 USD | `-17.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.75` | 9,870,000.00 USD | 0.00 USD | 1,330.00 USD | `-17.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.85` | 9,870,000.00 USD | 0.00 USD | 289.06 USD | `-17.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.95` | 9,870,000.00 USD | 0.00 USD | 808.29 USD | `-17.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.05` | 9,870,000.00 USD | 0.00 USD | 41,050.00 USD | `-17.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.15` | 9,830,000.00 USD | 0.00 USD | 8,360.00 USD | `-17.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.35` | 9,820,000.00 USD | 0.00 USD | 359.97 USD | `-17.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.45` | 9,820,000.00 USD | 0.00 USD | 8,770.00 USD | `-17.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.55` | 9,810,000.00 USD | 0.00 USD | 1,280.00 USD | `-17.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.65` | 9,810,000.00 USD | 0.00 USD | 1,280.00 USD | `-16.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.75` | 9,810,000.00 USD | 0.00 USD | 22,780.00 USD | `-16.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.85` | 9,780,000.00 USD | 0.00 USD | 341.19 USD | `-16.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.05` | 9,780,000.00 USD | 0.00 USD | 1,620.00 USD | `-16.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.25` | 9,780,000.00 USD | 0.00 USD | 266.50 USD | `-16.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.45` | 9,780,000.00 USD | 0.00 USD | 5,830.00 USD | `-16.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.55` | 9,770,000.00 USD | 0.00 USD | 572.48 USD | `-15.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.65` | 9,770,000.00 USD | 0.00 USD | 952.86 USD | `-15.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.75` | 9,770,000.00 USD | 0.00 USD | 1,390.00 USD | `-15.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.85` | 9,770,000.00 USD | 0.00 USD | 818.50 USD | `-15.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.95` | 9,770,000.00 USD | 0.00 USD | 70,900.00 USD | `-15.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.05` | 9,700,000.00 USD | 0.00 USD | 3,220.00 USD | `-15.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.15` | 9,700,000.00 USD | 0.00 USD | 684.31 USD | `-15.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.25` | 9,700,000.00 USD | 0.00 USD | 486.92 USD | `-15.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.35` | 9,700,000.00 USD | 0.00 USD | 386.22 USD | `-15.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.45` | 9,700,000.00 USD | 0.00 USD | 1,870.00 USD | `-15.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.55` | 9,690,000.00 USD | 0.00 USD | 1,310.00 USD | `-14.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.65` | 9,690,000.00 USD | 0.00 USD | 267,390.00 USD | `-14.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.75` | 9,430,000.00 USD | 0.00 USD | 1,660.00 USD | `-14.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.85` | 9,420,000.00 USD | 0.00 USD | 3,270.00 USD | `-14.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.95` | 9,420,000.00 USD | 0.00 USD | 945.63 USD | `-14.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.05` | 9,420,000.00 USD | 0.00 USD | 6,420.00 USD | `-14.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.15` | 9,410,000.00 USD | 0.00 USD | 239.47 USD | `-14.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.25` | 9,410,000.00 USD | 0.00 USD | 18,330.00 USD | `-14.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.45` | 9,390,000.00 USD | 0.00 USD | 168.57 USD | `-14.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.55` | 9,390,000.00 USD | 0.00 USD | 421.09 USD | `-13.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.65` | 9,390,000.00 USD | 0.00 USD | 1,100.00 USD | `-13.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.75` | 9,390,000.00 USD | 0.00 USD | 1,320.00 USD | `-13.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.95` | 9,390,000.00 USD | 0.00 USD | 4,550.00 USD | `-13.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.05` | 9,390,000.00 USD | 0.00 USD | 56,920.00 USD | `-13.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.15` | 9,330,000.00 USD | 0.00 USD | 25,220.00 USD | `-13.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.25` | 9,300,000.00 USD | 0.00 USD | 2,690.00 USD | `-13.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.45` | 9,300,000.00 USD | 0.00 USD | 965.26 USD | `-12.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.55` | 9,300,000.00 USD | 0.00 USD | 169.95 USD | `-12.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.65` | 9,300,000.00 USD | 0.00 USD | 858.35 USD | `-12.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.75` | 9,300,000.00 USD | 0.00 USD | 306.80 USD | `-12.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.95` | 9,300,000.00 USD | 0.00 USD | 137.62 USD | `-12.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.05` | 9,300,000.00 USD | 0.00 USD | 239,080.00 USD | `-12.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.15` | 9,060,000.00 USD | 0.00 USD | 437.67 USD | `-12.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.25` | 9,060,000.00 USD | 0.00 USD | 1,320.00 USD | `-12.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.35` | 9,060,000.00 USD | 0.00 USD | 39,110.00 USD | `-12.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.45` | 9,020,000.00 USD | 0.00 USD | 120.48 USD | `-11.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.55` | 9,020,000.00 USD | 0.00 USD | 105.23 USD | `-11.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.65` | 9,020,000.00 USD | 0.00 USD | 493,240.00 USD | `-11.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.75` | 8,530,000.00 USD | 0.00 USD | 1,410.00 USD | `-11.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.85` | 8,520,000.00 USD | 0.00 USD | 360.57 USD | `-11.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.95` | 8,520,000.00 USD | 0.00 USD | 2,050.00 USD | `-11.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.05` | 8,520,000.00 USD | 0.00 USD | 10,910.00 USD | `-11.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.15` | 8,510,000.00 USD | 0.00 USD | 2,210.00 USD | `-11.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.25` | 8,510,000.00 USD | 0.00 USD | 163.88 USD | `-11.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.35` | 8,510,000.00 USD | 0.00 USD | 4,080.00 USD | `-11.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.45` | 8,500,000.00 USD | 0.00 USD | 2,790.00 USD | `-10.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.55` | 8,500,000.00 USD | 0.00 USD | 417.17 USD | `-10.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.65` | 8,500,000.00 USD | 0.00 USD | 220,550.00 USD | `-10.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.75` | 8,280,000.00 USD | 0.00 USD | 3,060.00 USD | `-10.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.85` | 8,280,000.00 USD | 0.00 USD | 788.60 USD | `-10.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.95` | 8,280,000.00 USD | 0.00 USD | 132.16 USD | `-10.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.05` | 8,280,000.00 USD | 0.00 USD | 283,280.00 USD | `-10.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.15` | 7,990,000.00 USD | 0.00 USD | 23,550.00 USD | `-10.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.25` | 7,970,000.00 USD | 0.00 USD | 8,200.00 USD | `-10.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.35` | 7,960,000.00 USD | 0.00 USD | 102.20 USD | `-10.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.45` | 7,960,000.00 USD | 0.00 USD | 730.21 USD | `-9.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.55` | 7,960,000.00 USD | 0.00 USD | 1,160.00 USD | `-9.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.65` | 7,960,000.00 USD | 0.00 USD | 2,300.00 USD | `-9.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.85` | 7,960,000.00 USD | 0.00 USD | 131.78 USD | `-9.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.95` | 7,960,000.00 USD | 0.00 USD | 1,410.00 USD | `-9.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.05` | 7,960,000.00 USD | 0.00 USD | 132,850.00 USD | `-9.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.15` | 7,820,000.00 USD | 0.00 USD | 833.02 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.25` | 7,820,000.00 USD | 0.00 USD | 1,870.00 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.35` | 7,820,000.00 USD | 0.00 USD | 38,020.00 USD | `-8.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.45` | 7,780,000.00 USD | 0.00 USD | 867.69 USD | `-8.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.55` | 7,780,000.00 USD | 0.00 USD | 32,280.00 USD | `-8.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.65` | 7,750,000.00 USD | 0.00 USD | 27,220.00 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.75` | 7,720,000.00 USD | 0.00 USD | 53,390.00 USD | `-8.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.85` | 7,670,000.00 USD | 0.00 USD | 91,430.00 USD | `-8.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.95` | 7,580,000.00 USD | 0.00 USD | 141.43 USD | `-8.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.05` | 7,580,000.00 USD | 0.00 USD | 15,380.00 USD | `-8.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.15` | 7,560,000.00 USD | 0.00 USD | 6,470.00 USD | `-8.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.25` | 7,560,000.00 USD | 0.00 USD | 1,680.00 USD | `-8.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.35` | 7,550,000.00 USD | 0.00 USD | 4,220.00 USD | `-7.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.45` | 7,550,000.00 USD | 0.00 USD | 5,280.00 USD | `-7.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.55` | 7,540,000.00 USD | 0.00 USD | 348.35 USD | `-7.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.65` | 7,540,000.00 USD | 0.00 USD | 192.75 USD | `-7.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.75` | 7,540,000.00 USD | 0.00 USD | 105.01 USD | `-7.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.85` | 7,540,000.00 USD | 0.00 USD | 17,800.00 USD | `-7.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.95` | 7,530,000.00 USD | 0.00 USD | 87,020.00 USD | `-7.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.05` | 7,440,000.00 USD | 0.00 USD | 3,250,000.00 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.15` | 4,190,000.00 USD | 0.00 USD | 301.10 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.25` | 4,190,000.00 USD | 0.00 USD | 12,170.00 USD | `-7.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.35` | 4,180,000.00 USD | 0.00 USD | 106,890.00 USD | `-6.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.45` | 4,070,000.00 USD | 0.00 USD | 5,010.00 USD | `-6.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.55` | 4,060,000.00 USD | 0.00 USD | 13,500.00 USD | `-6.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.65` | 4,050,000.00 USD | 0.00 USD | 75,820.00 USD | `-6.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.75` | 3,970,000.00 USD | 0.00 USD | 4,980.00 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.85` | 3,970,000.00 USD | 0.00 USD | 6,580.00 USD | `-6.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.95` | 3,960,000.00 USD | 0.00 USD | 7,300.00 USD | `-6.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.05` | 3,960,000.00 USD | 0.00 USD | 628,480.00 USD | `-6.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.15` | 3,330,000.00 USD | 0.00 USD | 1,120.00 USD | `-6.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.25` | 3,330,000.00 USD | 0.00 USD | 1,660.00 USD | `-5.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.35` | 3,320,000.00 USD | 0.00 USD | 16,980.00 USD | `-5.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.45` | 3,310,000.00 USD | 0.00 USD | 920.90 USD | `-5.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.55` | 3,310,000.00 USD | 0.00 USD | 20,520.00 USD | `-5.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.65` | 3,290,000.00 USD | 0.00 USD | 38,100.00 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.75` | 3,250,000.00 USD | 0.00 USD | 21,870.00 USD | `-5.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.85` | 3,230,000.00 USD | 0.00 USD | 41,980.00 USD | `-5.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.95` | 3,180,000.00 USD | 0.00 USD | 33,290.00 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.05` | 3,150,000.00 USD | 0.00 USD | 268,250.00 USD | `-5.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.15` | 2,880,000.00 USD | 0.00 USD | 49,850.00 USD | `-5.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.25` | 2,830,000.00 USD | 0.00 USD | 5,780.00 USD | `-4.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.35` | 2,830,000.00 USD | 0.00 USD | 20,880.00 USD | `-4.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.45` | 2,810,000.00 USD | 0.00 USD | 132.20 USD | `-4.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.55` | 2,810,000.00 USD | 0.00 USD | 17,280.00 USD | `-4.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.65` | 2,790,000.00 USD | 0.00 USD | 58,520.00 USD | `-4.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.75` | 2,730,000.00 USD | 0.00 USD | 6,990.00 USD | `-4.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.85` | 2,720,000.00 USD | 0.00 USD | 32,380.00 USD | `-4.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.95` | 2,690,000.00 USD | 0.00 USD | 14,800.00 USD | `-4.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.05` | 2,680,000.00 USD | 0.00 USD | 42,680.00 USD | `-4.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.15` | 2,630,000.00 USD | 0.00 USD | 135,720.00 USD | `-4.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.25` | 2,500,000.00 USD | 0.00 USD | 9,220.00 USD | `-3.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.35` | 2,490,000.00 USD | 0.00 USD | 385.54 USD | `-3.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.45` | 2,490,000.00 USD | 0.00 USD | 1,380.00 USD | `-3.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.55` | 2,490,000.00 USD | 0.00 USD | 12,650.00 USD | `-3.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.65` | 2,470,000.00 USD | 0.00 USD | 3,290.00 USD | `-3.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.75` | 2,470,000.00 USD | 0.00 USD | 4,050.00 USD | `-3.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.85` | 2,470,000.00 USD | 0.00 USD | 479.57 USD | `-3.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.95` | 2,470,000.00 USD | 0.00 USD | 454.72 USD | `-3.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.05` | 2,470,000.00 USD | 0.00 USD | 109,610.00 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.15` | 2,360,000.00 USD | 0.00 USD | 318.23 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.25` | 2,360,000.00 USD | 0.00 USD | 1,050.00 USD | `-2.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.35` | 2,350,000.00 USD | 0.00 USD | 12,280.00 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.45` | 2,340,000.00 USD | 0.00 USD | 63,650.00 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.55` | 2,280,000.00 USD | 0.00 USD | 93,700.00 USD | `-2.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.65` | 2,180,000.00 USD | 0.00 USD | 25,000.00 USD | `-2.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.75` | 2,160,000.00 USD | 0.00 USD | 8,730.00 USD | `-2.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.85` | 2,150,000.00 USD | 0.00 USD | 15,220.00 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.95` | 2,140,000.00 USD | 0.00 USD | 4,000.00 USD | `-2.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.05` | 2,130,000.00 USD | 0.00 USD | 87,290.00 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.15` | 2,040,000.00 USD | 0.00 USD | 64,210.00 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.25` | 1,980,000.00 USD | 0.00 USD | 3,270.00 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.35` | 1,980,000.00 USD | 0.00 USD | 11,350.00 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.45` | 1,970,000.00 USD | 0.00 USD | 78,000.00 USD | `-1.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.55` | 1,890,000.00 USD | 0.00 USD | 159,700.00 USD | `-1.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.65` | 1,730,000.00 USD | 0.00 USD | 5,000.00 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.75` | 1,720,000.00 USD | 0.00 USD | 60,370.00 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.85` | 1,660,000.00 USD | 0.00 USD | 21,880.00 USD | `-1.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.95` | 1,640,000.00 USD | 0.00 USD | 31,070.00 USD | `-1.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.05` | 1,610,000.00 USD | 0.00 USD | 92,390.00 USD | `-1.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.15` | 1,520,000.00 USD | 0.00 USD | 38,540.00 USD | `-0.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.25` | 1,480,000.00 USD | 0.00 USD | 7,640.00 USD | `-0.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.35` | 1,470,000.00 USD | 0.00 USD | 66,600.00 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.45` | 1,400,000.00 USD | 0.00 USD | 152.39 USD | `-0.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.55` | 1,400,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-0.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.65` | 388,930.00 USD | 0.00 USD | 26,630.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.75` | 362,300.00 USD | 0.00 USD | 353,080.00 USD | `-0.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.85` | 9,220.00 USD | 0.00 USD | 8,290.00 USD | `-0.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.95` | 926.07 USD | 0.00 USD | 731.97 USD | `-0.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.05` | 194.10 USD | 0.00 USD | 194.10 USD | `-0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.15` | 3,200.00 USD | 3,200.00 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.25` | 35,570.00 USD | 32,370.00 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.35` | 43,720.00 USD | 8,150.00 USD | 0.00 USD | `+0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.45` | 44,260.00 USD | 535.98 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.55` | 576,630.00 USD | 532,370.00 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.65` | 590,850.00 USD | 14,220.00 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.75` | 599,600.00 USD | 8,750.00 USD | 0.00 USD | `+0.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.85` | 620,730.00 USD | 21,130.00 USD | 0.00 USD | `+0.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.95` | 635,250.00 USD | 14,520.00 USD | 0.00 USD | `+0.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 651,620.00 USD | 16,370.00 USD | 0.00 USD | `+1.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.15` | 654,850.00 USD | 3,230.00 USD | 0.00 USD | `+1.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.25` | 758,340.00 USD | 103,490.00 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.35` | 759,820.00 USD | 1,480.00 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.45` | 783,660.00 USD | 23,840.00 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.55` | 900,780.00 USD | 117,130.00 USD | 0.00 USD | `+1.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.65` | 923,380.00 USD | 22,600.00 USD | 0.00 USD | `+1.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.75` | 982,900.00 USD | 59,520.00 USD | 0.00 USD | `+1.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.85` | 988,920.00 USD | 6,020.00 USD | 0.00 USD | `+1.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.95` | 1,010,000.00 USD | 24,450.00 USD | 0.00 USD | `+1.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,070,000.00 USD | 60,980.00 USD | 0.00 USD | `+2.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.15` | 1,090,000.00 USD | 17,670.00 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.25` | 1,100,000.00 USD | 6,940.00 USD | 0.00 USD | `+2.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.35` | 1,140,000.00 USD | 39,720.00 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.45` | 1,140,000.00 USD | 1,920.00 USD | 0.00 USD | `+2.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.55` | 1,330,000.00 USD | 184,650.00 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.65` | 1,340,000.00 USD | 17,050.00 USD | 0.00 USD | `+2.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.75` | 1,350,000.00 USD | 9,780.00 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.85` | 1,360,000.00 USD | 3,680.00 USD | 0.00 USD | `+2.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.95` | 1,400,000.00 USD | 42,410.00 USD | 0.00 USD | `+2.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 3,200,000.00 USD | 1,800,000.00 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.15` | 3,210,000.00 USD | 12,360.00 USD | 0.00 USD | `+3.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.25` | 3,210,000.00 USD | 5,240.00 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.35` | 3,220,000.00 USD | 1,250.00 USD | 0.00 USD | `+3.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.45` | 3,230,000.00 USD | 11,390.00 USD | 0.00 USD | `+3.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.55` | 3,230,000.00 USD | 2,700.00 USD | 0.00 USD | `+3.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.65` | 3,280,000.00 USD | 49,970.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.75` | 3,280,000.00 USD | 1,110.00 USD | 0.00 USD | `+3.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.85` | 3,310,000.00 USD | 27,710.00 USD | 0.00 USD | `+3.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.95` | 3,310,000.00 USD | 2,760.00 USD | 0.00 USD | `+4.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.05` | 3,540,000.00 USD | 228,090.00 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.15` | 3,540,000.00 USD | 115.31 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.25` | 3,550,000.00 USD | 8,940.00 USD | 0.00 USD | `+4.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.35` | 3,550,000.00 USD | 3,850.00 USD | 0.00 USD | `+4.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.45` | 3,560,000.00 USD | 5,550.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.55` | 3,560,000.00 USD | 4,880.00 USD | 0.00 USD | `+4.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.65` | 3,560,000.00 USD | 477.76 USD | 0.00 USD | `+4.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.75` | 3,560,000.00 USD | 417.17 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.85` | 3,570,000.00 USD | 4,720.00 USD | 0.00 USD | `+4.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.95` | 3,570,000.00 USD | 1,080.00 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 3,650,000.00 USD | 83,280.00 USD | 0.00 USD | `+5.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.15` | 3,670,000.00 USD | 17,480.00 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.25` | 3,670,000.00 USD | 3,630.00 USD | 0.00 USD | `+5.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.35` | 3,680,000.00 USD | 4,280.00 USD | 0.00 USD | `+5.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.45` | 3,690,000.00 USD | 7,280.00 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.55` | 3,860,000.00 USD | 175,070.00 USD | 0.00 USD | `+5.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.65` | 4,130,000.00 USD | 267,140.00 USD | 0.00 USD | `+5.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.75` | 4,130,000.00 USD | 1,280.00 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.85` | 4,130,000.00 USD | 2,120.00 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.95` | 4,140,000.00 USD | 4,280.00 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 4,180,000.00 USD | 42,010.00 USD | 0.00 USD | `+6.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 4,180,000.00 USD | 3,180.00 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.25` | 4,250,000.00 USD | 64,080.00 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.35` | 4,250,000.00 USD | 4,260.00 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.45` | 4,250,000.00 USD | 3,860.00 USD | 0.00 USD | `+6.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.55` | 4,270,000.00 USD | 20,580.00 USD | 0.00 USD | `+6.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.65` | 4,290,000.00 USD | 17,250.00 USD | 0.00 USD | `+6.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.75` | 4,290,000.00 USD | 980.44 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.85` | 4,520,000.00 USD | 227,080.00 USD | 0.00 USD | `+7.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.95` | 4,580,000.00 USD | 62,400.00 USD | 0.00 USD | `+7.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.05` | 4,590,000.00 USD | 13,180.00 USD | 0.00 USD | `+7.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.15` | 4,600,000.00 USD | 1,180.00 USD | 0.00 USD | `+7.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.25` | 4,600,000.00 USD | 519.17 USD | 0.00 USD | `+7.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.35` | 4,600,000.00 USD | 146.09 USD | 0.00 USD | `+7.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.45` | 4,690,000.00 USD | 95,950.00 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.55` | 4,720,000.00 USD | 28,500.00 USD | 0.00 USD | `+7.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.65` | 4,720,000.00 USD | 680.23 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.75` | 4,720,000.00 USD | 2,150.00 USD | 0.00 USD | `+7.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.85` | 4,730,000.00 USD | 5,900.00 USD | 0.00 USD | `+8.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.95` | 4,760,000.00 USD | 25,930.00 USD | 0.00 USD | `+8.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.05` | 4,890,000.00 USD | 132,100.00 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.15` | 4,920,000.00 USD | 28,780.00 USD | 0.00 USD | `+8.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.25` | 4,920,000.00 USD | 1,010.00 USD | 0.00 USD | `+8.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.35` | 4,920,000.00 USD | 1,090.00 USD | 0.00 USD | `+8.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.45` | 4,920,000.00 USD | 266.79 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.55` | 4,920,000.00 USD | 3,620.00 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.65` | 4,920,000.00 USD | 1,970.00 USD | 0.00 USD | `+8.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.75` | 4,920,000.00 USD | 549.90 USD | 0.00 USD | `+8.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.85` | 4,940,000.00 USD | 10,600.00 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.95` | 4,940,000.00 USD | 3,620.00 USD | 0.00 USD | `+9.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.05` | 4,960,000.00 USD | 19,890.00 USD | 0.00 USD | `+9.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.15` | 4,970,000.00 USD | 7,080.00 USD | 0.00 USD | `+9.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.25` | 4,970,000.00 USD | 758.62 USD | 0.00 USD | `+9.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.35` | 4,970,000.00 USD | 7,980.00 USD | 0.00 USD | `+9.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.45` | 5,000,000.00 USD | 26,170.00 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.55` | 5,010,000.00 USD | 7,640.00 USD | 0.00 USD | `+9.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.65` | 5,010,000.00 USD | 355.14 USD | 0.00 USD | `+9.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.75` | 5,120,000.00 USD | 110,390.00 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.85` | 5,120,000.00 USD | 1,400.00 USD | 0.00 USD | `+10.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.95` | 5,120,000.00 USD | 2,990.00 USD | 0.00 USD | `+10.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.05` | 5,270,000.00 USD | 142,930.00 USD | 0.00 USD | `+10.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.15` | 5,270,000.00 USD | 109.29 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.25` | 5,290,000.00 USD | 20,190.00 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.35` | 5,290,000.00 USD | 698.85 USD | 0.00 USD | `+10.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.45` | 5,300,000.00 USD | 8,930.00 USD | 0.00 USD | `+10.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.55` | 5,350,000.00 USD | 52,130.00 USD | 0.00 USD | `+10.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.65` | 5,410,000.00 USD | 65,380.00 USD | 0.00 USD | `+10.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.75` | 5,410,000.00 USD | 536.60 USD | 0.00 USD | `+11.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.85` | 5,430,000.00 USD | 11,350.00 USD | 0.00 USD | `+11.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.95` | 5,440,000.00 USD | 9,120.00 USD | 0.00 USD | `+11.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 5,520,000.00 USD | 89,330.00 USD | 0.00 USD | `+11.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.15` | 5,590,000.00 USD | 68,190.00 USD | 0.00 USD | `+11.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.35` | 5,600,000.00 USD | 7,140.00 USD | 0.00 USD | `+11.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.45` | 5,600,000.00 USD | 2,580.00 USD | 0.00 USD | `+11.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.55` | 5,610,000.00 USD | 5,430.00 USD | 0.00 USD | `+11.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.65` | 5,610,000.00 USD | 666.02 USD | 0.00 USD | `+11.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.75` | 5,610,000.00 USD | 1,010.00 USD | 0.00 USD | `+12.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.85` | 5,610,000.00 USD | 1,430.00 USD | 0.00 USD | `+12.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.95` | 5,650,000.00 USD | 40,920.00 USD | 0.00 USD | `+12.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 5,730,000.00 USD | 73,460.00 USD | 0.00 USD | `+12.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.15` | 5,730,000.00 USD | 7,660.00 USD | 0.00 USD | `+12.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.25` | 9,680,000.00 USD | 3,950,000.00 USD | 0.00 USD | `+12.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.35` | 9,710,000.00 USD | 31,070.00 USD | 0.00 USD | `+12.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.45` | 9,720,000.00 USD | 5,880.00 USD | 0.00 USD | `+12.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.55` | 9,720,000.00 USD | 1,070.00 USD | 0.00 USD | `+12.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.65` | 9,720,000.00 USD | 5,040.00 USD | 0.00 USD | `+12.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.75` | 9,720,000.00 USD | 1,370.00 USD | 0.00 USD | `+13.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.85` | 9,730,000.00 USD | 1,420.00 USD | 0.00 USD | `+13.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.95` | 9,730,000.00 USD | 357.34 USD | 0.00 USD | `+13.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.05` | 10,250,000.00 USD | 522,250.00 USD | 0.00 USD | `+13.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.15` | 10,250,000.00 USD | 4,150.00 USD | 0.00 USD | `+13.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.25` | 10,250,000.00 USD | 102.53 USD | 0.00 USD | `+13.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.35` | 10,250,000.00 USD | 1,610.00 USD | 0.00 USD | `+13.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.45` | 10,260,000.00 USD | 1,580.00 USD | 0.00 USD | `+13.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.55` | 10,270,000.00 USD | 10,280.00 USD | 0.00 USD | `+13.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.65` | 10,270,000.00 USD | 3,030.00 USD | 0.00 USD | `+14.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.85` | 10,290,000.00 USD | 17,520.00 USD | 0.00 USD | `+14.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.95` | 10,360,000.00 USD | 74,620.00 USD | 0.00 USD | `+14.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 10,430,000.00 USD | 64,770.00 USD | 0.00 USD | `+14.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.15` | 10,430,000.00 USD | 1,300.00 USD | 0.00 USD | `+14.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.25` | 10,430,000.00 USD | 5,910.00 USD | 0.00 USD | `+14.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.45` | 10,430,000.00 USD | 585.11 USD | 0.00 USD | `+14.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.55` | 10,430,000.00 USD | 852.24 USD | 0.00 USD | `+14.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.65` | 10,460,000.00 USD | 22,910.00 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.75` | 10,460,000.00 USD | 2,420.00 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.85` | 10,460,000.00 USD | 2,100.00 USD | 0.00 USD | `+15.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.05` | 10,480,000.00 USD | 14,400.00 USD | 0.00 USD | `+15.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.15` | 10,530,000.00 USD | 49,680.00 USD | 0.00 USD | `+15.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.25` | 10,530,000.00 USD | 5,260.00 USD | 0.00 USD | `+15.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.35` | 10,540,000.00 USD | 6,270.00 USD | 0.00 USD | `+15.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.45` | 10,540,000.00 USD | 843.38 USD | 0.00 USD | `+15.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.55` | 10,570,000.00 USD | 36,280.00 USD | 0.00 USD | `+15.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.65` | 10,580,000.00 USD | 6,150.00 USD | 0.00 USD | `+16.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.85` | 10,580,000.00 USD | 586.82 USD | 0.00 USD | `+16.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.05` | 10,660,000.00 USD | 78,560.00 USD | 0.00 USD | `+16.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.25` | 10,660,000.00 USD | 473.38 USD | 0.00 USD | `+16.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.35` | 10,700,000.00 USD | 35,250.00 USD | 0.00 USD | `+16.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.45` | 10,700,000.00 USD | 655.74 USD | 0.00 USD | `+16.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.55` | 10,700,000.00 USD | 4,470.00 USD | 0.00 USD | `+17.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.65` | 10,700,000.00 USD | 230.71 USD | 0.00 USD | `+17.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.75` | 10,700,000.00 USD | 257.07 USD | 0.00 USD | `+17.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.85` | 10,710,000.00 USD | 4,540.00 USD | 0.00 USD | `+17.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.05` | 10,710,000.00 USD | 1,970.00 USD | 0.00 USD | `+17.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.15` | 10,710,000.00 USD | 122.14 USD | 0.00 USD | `+17.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.25` | 10,710,000.00 USD | 907.14 USD | 0.00 USD | `+17.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.35` | 10,710,000.00 USD | 740.99 USD | 0.00 USD | `+17.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.45` | 10,710,000.00 USD | 343.35 USD | 0.00 USD | `+17.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.55` | 10,710,000.00 USD | 1,640.00 USD | 0.00 USD | `+18.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.65` | 10,710,000.00 USD | 105.48 USD | 0.00 USD | `+18.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.75` | 10,710,000.00 USD | 1,010.00 USD | 0.00 USD | `+18.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.95` | 10,710,000.00 USD | 2,520.00 USD | 0.00 USD | `+18.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.05` | 10,800,000.00 USD | 81,890.00 USD | 0.00 USD | `+18.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.35` | 10,800,000.00 USD | 309.14 USD | 0.00 USD | `+18.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.45` | 10,800,000.00 USD | 346.35 USD | 0.00 USD | `+18.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.55` | 10,800,000.00 USD | 2,440.00 USD | 0.00 USD | `+19.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.75` | 10,800,000.00 USD | 121.54 USD | 0.00 USD | `+19.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.85` | 10,800,000.00 USD | 579.25 USD | 0.00 USD | `+19.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.05` | 10,810,000.00 USD | 6,400.00 USD | 0.00 USD | `+19.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.15` | 10,810,000.00 USD | 1,740.00 USD | 0.00 USD | `+19.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.25` | 10,810,000.00 USD | 1,920.00 USD | 0.00 USD | `+19.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.45` | 10,810,000.00 USD | 2,870.00 USD | 0.00 USD | `+19.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.55` | 10,830,000.00 USD | 14,010.00 USD | 0.00 USD | `+20.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.65` | 10,830,000.00 USD | 6,000.00 USD | 0.00 USD | `+20.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.75` | 10,840,000.00 USD | 3,580.00 USD | 0.00 USD | `+20.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.85` | 10,840,000.00 USD | 234.87 USD | 0.00 USD | `+20.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.95` | 10,850,000.00 USD | 12,860.00 USD | 0.00 USD | `+20.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.05` | 10,850,000.00 USD | 4,200.00 USD | 0.00 USD | `+20.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.15` | 10,850,000.00 USD | 584.58 USD | 0.00 USD | `+20.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.25` | 10,860,000.00 USD | 1,740.00 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.35` | 10,860,000.00 USD | 2,330.00 USD | 0.00 USD | `+20.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.45` | 10,980,000.00 USD | 118,690.00 USD | 0.00 USD | `+21.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.65` | 11,080,000.00 USD | 106,330.00 USD | 0.00 USD | `+21.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.75` | 11,090,000.00 USD | 5,920.00 USD | 0.00 USD | `+21.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.85` | 11,150,000.00 USD | 55,580.00 USD | 0.00 USD | `+21.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.05` | 11,210,000.00 USD | 69,220.00 USD | 0.00 USD | `+21.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.15` | 11,220,000.00 USD | 3,980.00 USD | 0.00 USD | `+21.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.25` | 11,220,000.00 USD | 4,460.00 USD | 0.00 USD | `+21.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.35` | 11,220,000.00 USD | 127.82 USD | 0.00 USD | `+21.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.45` | 11,220,000.00 USD | 707.15 USD | 0.00 USD | `+22.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.55` | 11,230,000.00 USD | 1,260.00 USD | 0.00 USD | `+22.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.65` | 11,230,000.00 USD | 2,970.00 USD | 0.00 USD | `+22.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.75` | 11,230,000.00 USD | 403.75 USD | 0.00 USD | `+22.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.85` | 11,240,000.00 USD | 15,940.00 USD | 0.00 USD | `+22.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.95` | 11,290,000.00 USD | 42,290.00 USD | 0.00 USD | `+22.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.05` | 11,340,000.00 USD | 52,430.00 USD | 0.00 USD | `+22.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.15` | 11,350,000.00 USD | 15,130.00 USD | 0.00 USD | `+22.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.25` | 11,360,000.00 USD | 1,850.00 USD | 0.00 USD | `+22.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.35` | 11,360,000.00 USD | 4,150.00 USD | 0.00 USD | `+22.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.45` | 11,360,000.00 USD | 310.57 USD | 0.00 USD | `+23.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.65` | 11,360,000.00 USD | 615.00 USD | 0.00 USD | `+23.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.75` | 11,490,000.00 USD | 125,500.00 USD | 0.00 USD | `+23.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.85` | 11,520,000.00 USD | 37,630.00 USD | 0.00 USD | `+23.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.95` | 11,520,000.00 USD | 458.21 USD | 0.00 USD | `+23.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.05` | 11,700,000.00 USD | 179,160.00 USD | 0.00 USD | `+23.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.15` | 11,700,000.00 USD | 414.52 USD | 0.00 USD | `+23.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.25` | 11,710,000.00 USD | 3,210.00 USD | 0.00 USD | `+23.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.35` | 11,720,000.00 USD | 7,850.00 USD | 0.00 USD | `+24.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.45` | 11,730,000.00 USD | 13,560.00 USD | 0.00 USD | `+24.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.55` | 11,730,000.00 USD | 904.13 USD | 0.00 USD | `+24.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.65` | 11,730,000.00 USD | 191.83 USD | 0.00 USD | `+24.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.75` | 11,730,000.00 USD | 2,150.00 USD | 0.00 USD | `+24.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.85` | 11,730,000.00 USD | 663.47 USD | 0.00 USD | `+24.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.05` | 11,750,000.00 USD | 20,960.00 USD | 0.00 USD | `+24.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.15` | 11,750,000.00 USD | 122.36 USD | 0.00 USD | `+24.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.25` | 11,770,000.00 USD | 11,200.00 USD | 0.00 USD | `+24.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.45` | 11,780,000.00 USD | 11,570.00 USD | 0.00 USD | `+25.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.55` | 11,780,000.00 USD | 7,860.00 USD | 0.00 USD | `+25.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.65` | 11,790,000.00 USD | 4,430.00 USD | 0.00 USD | `+25.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.75` | 11,790,000.00 USD | 2,450.00 USD | 0.00 USD | `+25.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.85` | 11,790,000.00 USD | 1,480.00 USD | 0.00 USD | `+25.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.95` | 11,870,000.00 USD | 80,260.00 USD | 0.00 USD | `+25.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.05` | 12,070,000.00 USD | 192,930.00 USD | 0.00 USD | `+25.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.15` | 12,070,000.00 USD | 1,000.00 USD | 0.00 USD | `+25.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.25` | 12,300,000.00 USD | 234,430.00 USD | 0.00 USD | `+25.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.35` | 12,350,000.00 USD | 52,330.00 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.45` | 12,360,000.00 USD | 3,060.00 USD | 0.00 USD | `+26.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.55` | 12,370,000.00 USD | 14,770.00 USD | 0.00 USD | `+26.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.65` | 12,380,000.00 USD | 11,000.00 USD | 0.00 USD | `+26.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.75` | 12,380,000.00 USD | 368.25 USD | 0.00 USD | `+26.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.85` | 12,390,000.00 USD | 3,850.00 USD | 0.00 USD | `+26.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.95` | 12,400,000.00 USD | 16,430.00 USD | 0.00 USD | `+26.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.05` | 13,410,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.15` | 13,410,000.00 USD | 252.46 USD | 0.00 USD | `+26.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.25` | 13,420,000.00 USD | 7,710.00 USD | 0.00 USD | `+26.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.35` | 13,430,000.00 USD | 6,790.00 USD | 0.00 USD | `+27.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.45` | 13,430,000.00 USD | 2,670.00 USD | 0.00 USD | `+27.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.55` | 13,430,000.00 USD | 632.58 USD | 0.00 USD | `+27.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.65` | 13,440,000.00 USD | 11,550.00 USD | 0.00 USD | `+27.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.85` | 13,450,000.00 USD | 5,530.00 USD | 0.00 USD | `+27.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.95` | 13,470,000.00 USD | 18,470.00 USD | 0.00 USD | `+27.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.05` | 13,480,000.00 USD | 16,360.00 USD | 0.00 USD | `+27.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.15` | 13,480,000.00 USD | 1,320.00 USD | 0.00 USD | `+27.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.25` | 13,480,000.00 USD | 151.59 USD | 0.00 USD | `+28.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.35` | 13,490,000.00 USD | 4,240.00 USD | 0.00 USD | `+28.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.45` | 13,490,000.00 USD | 1,370.00 USD | 0.00 USD | `+28.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.55` | 13,500,000.00 USD | 7,330.00 USD | 0.00 USD | `+28.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.65` | 13,500,000.00 USD | 6,610.00 USD | 0.00 USD | `+28.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.85` | 13,500,000.00 USD | 596.78 USD | 0.00 USD | `+28.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.95` | 13,520,000.00 USD | 10,310.00 USD | 0.00 USD | `+28.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.05` | 14,070,000.00 USD | 554,250.00 USD | 0.00 USD | `+28.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.15` | 14,070,000.00 USD | 603.22 USD | 0.00 USD | `+28.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.25` | 14,070,000.00 USD | 311.87 USD | 0.00 USD | `+29.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.35` | 14,080,000.00 USD | 6,780.00 USD | 0.00 USD | `+29.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.45` | 14,080,000.00 USD | 993.56 USD | 0.00 USD | `+29.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.55` | 14,090,000.00 USD | 16,280.00 USD | 0.00 USD | `+29.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.85` | 14,090,000.00 USD | 471.94 USD | 0.00 USD | `+29.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.95` | 14,100,000.00 USD | 209.08 USD | 0.00 USD | `+29.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.05` | 14,250,000.00 USD | 151,060.00 USD | 0.00 USD | `+29.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.15` | 14,250,000.00 USD | 189.23 USD | 0.00 USD | `+29.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.45` | 14,250,000.00 USD | 187.15 USD | 0.00 USD | `+30.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.65` | 14,250,000.00 USD | 3,550.00 USD | 0.00 USD | `+30.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.75` | 14,260,000.00 USD | 7,460.00 USD | 0.00 USD | `+30.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.05` | 14,450,000.00 USD | 190,580.00 USD | 0.00 USD | `+30.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.35` | 14,450,000.00 USD | 534.87 USD | 0.00 USD | `+31.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.45` | 14,450,000.00 USD | 4,620.00 USD | 0.00 USD | `+31.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.65` | 14,460,000.00 USD | 5,000.00 USD | 0.00 USD | `+31.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.75` | 14,460,000.00 USD | 362.81 USD | 0.00 USD | `+31.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.85` | 14,520,000.00 USD | 60,770.00 USD | 0.00 USD | `+31.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.95` | 14,520,000.00 USD | 482.37 USD | 0.00 USD | `+31.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.05` | 14,530,000.00 USD | 5,290.00 USD | 0.00 USD | `+31.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.15` | 14,530,000.00 USD | 3,010.00 USD | 0.00 USD | `+32.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.25` | 14,530,000.00 USD | 191.09 USD | 0.00 USD | `+32.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.65` | 14,570,000.00 USD | 41,130.00 USD | 0.00 USD | `+32.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.95` | 14,580,000.00 USD | 12,600.00 USD | 0.00 USD | `+32.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.05` | 14,630,000.00 USD | 50,720.00 USD | 0.00 USD | `+32.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.15` | 14,630,000.00 USD | 229.89 USD | 0.00 USD | `+33.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.25` | 14,650,000.00 USD | 15,330.00 USD | 0.00 USD | `+33.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.45` | 14,650,000.00 USD | 401.29 USD | 0.00 USD | `+33.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.55` | 14,650,000.00 USD | 1,320.00 USD | 0.00 USD | `+33.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.65` | 14,650,000.00 USD | 152.99 USD | 0.00 USD | `+33.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.75` | 14,650,000.00 USD | 153.10 USD | 0.00 USD | `+33.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.85` | 14,650,000.00 USD | 116.87 USD | 0.00 USD | `+33.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.05` | 14,700,000.00 USD | 51,520.00 USD | 0.00 USD | `+34.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.35` | 14,700,000.00 USD | 1,760.00 USD | 0.00 USD | `+34.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.45` | 14,710,000.00 USD | 4,090.00 USD | 0.00 USD | `+34.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.65` | 14,710,000.00 USD | 192.06 USD | 0.00 USD | `+34.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.75` | 14,710,000.00 USD | 3,150.00 USD | 0.00 USD | `+34.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.85` | 14,710,000.00 USD | 2,620.00 USD | 0.00 USD | `+34.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.95` | 14,720,000.00 USD | 10,140.00 USD | 0.00 USD | `+34.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.05` | 14,730,000.00 USD | 6,000.00 USD | 0.00 USD | `+35.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.15` | 14,740,000.00 USD | 5,950.00 USD | 0.00 USD | `+35.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.25` | 14,740,000.00 USD | 8,820.00 USD | 0.00 USD | `+35.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.45` | 14,740,000.00 USD | 135.39 USD | 0.00 USD | `+35.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.65` | 14,910,000.00 USD | 160,920.00 USD | 0.00 USD | `+35.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.75` | 14,910,000.00 USD | 144.93 USD | 0.00 USD | `+35.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.05` | 14,920,000.00 USD | 12,390.00 USD | 0.00 USD | `+36.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.65` | 14,920,000.00 USD | 397.95 USD | 0.00 USD | `+36.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.85` | 14,930,000.00 USD | 9,310.00 USD | 0.00 USD | `+36.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.95` | 14,930,000.00 USD | 3,910.00 USD | 0.00 USD | `+36.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.05` | 14,930,000.00 USD | 267.43 USD | 0.00 USD | `+37.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.15` | 14,930,000.00 USD | 509.96 USD | 0.00 USD | `+37.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.25` | 14,930,000.00 USD | 191.88 USD | 0.00 USD | `+37.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.35` | 14,930,000.00 USD | 237.36 USD | 0.00 USD | `+37.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.55` | 14,930,000.00 USD | 1,210.00 USD | 0.00 USD | `+37.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.65` | 14,930,000.00 USD | 192.46 USD | 0.00 USD | `+37.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.75` | 14,930,000.00 USD | 112.35 USD | 0.00 USD | `+37.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.95` | 14,940,000.00 USD | 4,620.00 USD | 0.00 USD | `+38.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.05` | 14,990,000.00 USD | 54,080.00 USD | 0.00 USD | `+38.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.25` | 14,990,000.00 USD | 331.60 USD | 0.00 USD | `+38.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.55` | 15,260,000.00 USD | 270,270.00 USD | 0.00 USD | `+38.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.85` | 15,260,000.00 USD | 647.28 USD | 0.00 USD | `+38.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.05` | 15,380,000.00 USD | 116,220.00 USD | 0.00 USD | `+39.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.55` | 15,390,000.00 USD | 7,560.00 USD | 0.00 USD | `+39.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.05` | 15,390,000.00 USD | 1,890.00 USD | 0.00 USD | `+40.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.35` | 15,390,000.00 USD | 192.25 USD | 0.00 USD | `+40.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.45` | 15,390,000.00 USD | 465.29 USD | 0.00 USD | `+40.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.55` | 15,390,000.00 USD | 389.17 USD | 0.00 USD | `+40.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.85` | 15,390,000.00 USD | 826.57 USD | 0.00 USD | `+41.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.05` | 15,390,000.00 USD | 231.61 USD | 0.00 USD | `+41.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.25` | 15,400,000.00 USD | 2,910.00 USD | 0.00 USD | `+41.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.35` | 15,400,000.00 USD | 3,920.00 USD | 0.00 USD | `+41.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.65` | 15,430,000.00 USD | 26,260.00 USD | 0.00 USD | `+41.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.75` | 15,430,000.00 USD | 133.62 USD | 0.00 USD | `+41.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.05` | 15,440,000.00 USD | 14,550.00 USD | 0.00 USD | `+42.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.45` | 15,440,000.00 USD | 692.25 USD | 0.00 USD | `+42.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.65` | 15,440,000.00 USD | 447.84 USD | 0.00 USD | `+42.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.85` | 22,180,000.00 USD | 6,740,000.00 USD | 0.00 USD | `+43.06%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `138.95` | 22,190,000.00 USD | 826.75 USD | 0.00 USD | `+43.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.05` | 24,380,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+43.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.55` | 24,380,000.00 USD | 5,920.00 USD | 0.00 USD | `+43.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.05` | 24,490,000.00 USD | 110,660.00 USD | 0.00 USD | `+44.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.45` | 24,510,000.00 USD | 12,120.00 USD | 0.00 USD | `+44.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.55` | 24,600,000.00 USD | 98,400.00 USD | 0.00 USD | `+44.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.75` | 24,610,000.00 USD | 990.88 USD | 0.00 USD | `+45.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.05` | 24,620,000.00 USD | 11,640.00 USD | 0.00 USD | `+45.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.25` | 24,620,000.00 USD | 6,190.00 USD | 0.00 USD | `+45.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.65` | 24,620,000.00 USD | 796.07 USD | 0.00 USD | `+45.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.05` | 24,620,000.00 USD | 826.73 USD | 0.00 USD | `+46.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.85` | 24,620,000.00 USD | 278.56 USD | 0.00 USD | `+47.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.95` | 24,950,000.00 USD | 329,100.00 USD | 0.00 USD | `+47.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.05` | 25,030,000.00 USD | 72,610.00 USD | 0.00 USD | `+47.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.15` | 25,040,000.00 USD | 16,980.00 USD | 0.00 USD | `+47.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.35` | 25,040,000.00 USD | 528.96 USD | 0.00 USD | `+47.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.05` | 25,050,000.00 USD | 6,330.00 USD | 0.00 USD | `+48.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.25` | 25,050,000.00 USD | 415.44 USD | 0.00 USD | `+48.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.35` | 25,330,000.00 USD | 282,520.00 USD | 0.00 USD | `+48.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.55` | 25,340,000.00 USD | 7,260.00 USD | 0.00 USD | `+48.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.75` | 25,340,000.00 USD | 791.78 USD | 0.00 USD | `+49.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.05` | 25,380,000.00 USD | 36,040.00 USD | 0.00 USD | `+49.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.25` | 25,380,000.00 USD | 209.16 USD | 0.00 USD | `+49.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.55` | 25,380,000.00 USD | 698.64 USD | 0.00 USD | `+49.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.05` | 25,570,000.00 USD | 190,100.00 USD | 0.00 USD | `+50.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.15` | 25,570,000.00 USD | 3,300.00 USD | 0.00 USD | `+50.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.25` | 25,570,000.00 USD | 1,020.00 USD | 0.00 USD | `+50.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.95` | 25,570,000.00 USD | 1,500.00 USD | 0.00 USD | `+51.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.05` | 25,610,000.00 USD | 37,700.00 USD | 0.00 USD | `+51.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.45` | 25,610,000.00 USD | 844.89 USD | 0.00 USD | `+51.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.85` | 25,620,000.00 USD | 4,610.00 USD | 0.00 USD | `+52.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.95` | 25,620,000.00 USD | 3,100.00 USD | 0.00 USD | `+52.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.05` | 26,960,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+52.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.45` | 26,960,000.00 USD | 1,370.00 USD | 0.00 USD | `+52.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.55` | 26,970,000.00 USD | 4,760.00 USD | 0.00 USD | `+53.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.05` | 26,970,000.00 USD | 549.99 USD | 0.00 USD | `+53.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.15` | 27,480,000.00 USD | 510,120.00 USD | 0.00 USD | `+53.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.05` | 27,730,000.00 USD | 249,190.00 USD | 0.00 USD | `+54.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.25` | 27,730,000.00 USD | 1,200.00 USD | 0.00 USD | `+54.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.35` | 27,730,000.00 USD | 178.92 USD | 0.00 USD | `+54.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.55` | 27,730,000.00 USD | 1,360.00 USD | 0.00 USD | `+55.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.05` | 27,740,000.00 USD | 14,430.00 USD | 0.00 USD | `+55.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.25` | 27,740,000.00 USD | 2,000.00 USD | 0.00 USD | `+55.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.45` | 27,740,000.00 USD | 411.94 USD | 0.00 USD | `+56.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.15` | 27,760,000.00 USD | 10,620.00 USD | 0.00 USD | `+57.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.65` | 27,760,000.00 USD | 1,020.00 USD | 0.00 USD | `+58.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.55` | 27,770,000.00 USD | 12,000.00 USD | 0.00 USD | `+59.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.85` | 27,770,000.00 USD | 113.04 USD | 0.00 USD | `+59.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.05` | 27,770,000.00 USD | 1,830.00 USD | 0.00 USD | `+59.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.35` | 27,790,000.00 USD | 22,680.00 USD | 0.00 USD | `+60.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.85` | 27,810,000.00 USD | 16,970.00 USD | 0.00 USD | `+60.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.05` | 27,810,000.00 USD | 2,230.00 USD | 0.00 USD | `+60.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.05` | 27,820,000.00 USD | 6,640.00 USD | 0.00 USD | `+62.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.75` | 27,830,000.00 USD | 15,880.00 USD | 0.00 USD | `+63.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.15` | 27,840,000.00 USD | 692.30 USD | 0.00 USD | `+63.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.95` | 27,840,000.00 USD | 5,620.00 USD | 0.00 USD | `+64.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.05` | 27,930,000.00 USD | 89,040.00 USD | 0.00 USD | `+64.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.05` | 27,930,000.00 USD | 281.84 USD | 0.00 USD | `+65.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.05` | 27,930,000.00 USD | 4,080.00 USD | 0.00 USD | `+68.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.05` | 28,020,000.00 USD | 89,230.00 USD | 0.00 USD | `+70.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.45` | 28,020,000.00 USD | 823.94 USD | 0.00 USD | `+70.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.45` | 28,020,000.00 USD | 211.39 USD | 0.00 USD | `+71.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.95` | 28,030,000.00 USD | 307.19 USD | 0.00 USD | `+72.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.05` | 28,030,000.00 USD | 593.03 USD | 0.00 USD | `+72.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.75` | 28,030,000.00 USD | 1,440.00 USD | 0.00 USD | `+72.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.05` | 28,030,000.00 USD | 5,720.00 USD | 0.00 USD | `+73.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.55` | 28,030,000.00 USD | 495.09 USD | 0.00 USD | `+74.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.95` | 28,030,000.00 USD | 912.63 USD | 0.00 USD | `+75.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.05` | 28,080,000.00 USD | 43,480.00 USD | 0.00 USD | `+75.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.55` | 28,080,000.00 USD | 686.20 USD | 0.00 USD | `+76.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.05` | 28,110,000.00 USD | 35,280.00 USD | 0.00 USD | `+77.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.45` | 28,110,000.00 USD | 703.60 USD | 0.00 USD | `+77.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.05` | 28,120,000.00 USD | 3,160.00 USD | 0.00 USD | `+78.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `174.85` | 28,120,000.00 USD | 1,430.00 USD | 0.00 USD | `+80.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.05` | 28,170,000.00 USD | 52,520.00 USD | 0.00 USD | `+80.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.25` | 28,190,000.00 USD | 21,960.00 USD | 0.00 USD | `+80.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.85` | 28,190,000.00 USD | 1,450.00 USD | 0.00 USD | `+82.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.05` | 28,200,000.00 USD | 885.25 USD | 0.00 USD | `+82.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.55` | 28,200,000.00 USD | 2,990.00 USD | 0.00 USD | `+83.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.15` | 28,200,000.00 USD | 261.56 USD | 0.00 USD | `+84.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.05` | 28,280,000.00 USD | 80,290.00 USD | 0.00 USD | `+85.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.05` | 28,280,000.00 USD | 2,440.00 USD | 0.00 USD | `+86.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.95` | 28,280,000.00 USD | 349.34 USD | 0.00 USD | `+87.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.45` | 28,300,000.00 USD | 19,620.00 USD | 0.00 USD | `+87.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.45` | 28,850,000.00 USD | 550,350.00 USD | 0.00 USD | `+89.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.05` | 28,880,000.00 USD | 29,610.00 USD | 0.00 USD | `+90.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.05` | 29,050,000.00 USD | 165,580.00 USD | 0.00 USD | `+92.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.05` | 29,190,000.00 USD | 141,190.00 USD | 0.00 USD | `+93.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `189.05` | 29,200,000.00 USD | 15,340.00 USD | 0.00 USD | `+94.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.05` | 29,240,000.00 USD | 35,880.00 USD | 0.00 USD | `+95.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.35` | 29,240,000.00 USD | 744.27 USD | 0.00 USD | `+96.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.65` | 29,250,000.00 USD | 7,750.00 USD | 0.00 USD | `+96.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `194.05` | 29,250,000.00 USD | 4,270.00 USD | 0.00 USD | `+99.94%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `82.60` | 172,810,000.00 USD | 0.00 USD | 172,810,000.00 USD | 53,130.00 USD | 56,870.00 USD | 141,300.00 USD |
| `7D` | `82.80` | 172,560,000.00 USD | 0.00 USD | 172,560,000.00 USD | 1,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `83.00` | 172,560,000.00 USD | 0.00 USD | 172,560,000.00 USD | 1,690.00 USD | 2,080.00 USD | 0.00 USD |
| `7D` | `83.20` | 172,550,000.00 USD | 0.00 USD | 172,550,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD |
| `7D` | `83.60` | 172,510,000.00 USD | 0.00 USD | 172,510,000.00 USD | 0.00 USD | 0.00 USD | 9,920.00 USD |
| `7D` | `83.80` | 172,500,000.00 USD | 0.00 USD | 172,500,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD |
| `7D` | `84.20` | 172,490,000.00 USD | 0.00 USD | 172,490,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD |
| `7D` | `84.40` | 172,470,000.00 USD | 0.00 USD | 172,470,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD |
| `7D` | `85.20` | 172,440,000.00 USD | 0.00 USD | 172,440,000.00 USD | 0.00 USD | 218,580.00 USD | 0.00 USD |
| `7D` | `85.40` | 172,220,000.00 USD | 0.00 USD | 172,220,000.00 USD | 0.00 USD | 12,950.00 USD | 192,310.00 USD |
| `7D` | `85.60` | 172,020,000.00 USD | 0.00 USD | 172,020,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD |
| `7D` | `85.80` | 171,830,000.00 USD | 0.00 USD | 171,830,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD |
| `7D` | `86.20` | 171,570,000.00 USD | 0.00 USD | 171,570,000.00 USD | 0.00 USD | 12,130.00 USD | 199,350.00 USD |
| `7D` | `86.40` | 171,360,000.00 USD | 0.00 USD | 171,360,000.00 USD | 0.00 USD | 311,220.00 USD | 4,340.00 USD |
| `7D` | `86.80` | 171,040,000.00 USD | 0.00 USD | 171,040,000.00 USD | 0.00 USD | 149,840.00 USD | 0.00 USD |
| `7D` | `87.00` | 170,890,000.00 USD | 0.00 USD | 170,890,000.00 USD | 263,340.00 USD | 176,600.00 USD | 297,340.00 USD |
| `1D` | `87.10` | 180,530,000.00 USD | 0.00 USD | 180,530,000.00 USD | 412,880.00 USD | 386,260.00 USD | 441,210.00 USD |
| `7D` | `87.20` | 170,150,000.00 USD | 0.00 USD | 170,150,000.00 USD | 8,850.00 USD | 6,510.00 USD | 6,820.00 USD |
| `1D` | `87.30` | 179,290,000.00 USD | 0.00 USD | 179,290,000.00 USD | 150,010.00 USD | 242,640.00 USD | 278,230.00 USD |
| `7D` | `87.40` | 170,130,000.00 USD | 0.00 USD | 170,130,000.00 USD | 248,310.00 USD | 225,130.00 USD | 288,100.00 USD |
| `1D` | `87.50` | 178,620,000.00 USD | 0.00 USD | 178,620,000.00 USD | 156,730.00 USD | 252,960.00 USD | 89,770.00 USD |
| `7D` | `87.60` | 169,370,000.00 USD | 0.00 USD | 169,370,000.00 USD | 0.00 USD | 275,130.00 USD | 421,310.00 USD |
| `1D` | `87.70` | 178,120,000.00 USD | 0.00 USD | 178,120,000.00 USD | 8,600.00 USD | 250,230.00 USD | 267,450.00 USD |
| `7D` | `87.80` | 168,670,000.00 USD | 0.00 USD | 168,670,000.00 USD | 0.00 USD | 413,150.00 USD | 11,130.00 USD |
| `1D` | `87.90` | 177,590,000.00 USD | 0.00 USD | 177,590,000.00 USD | 134,550.00 USD | 427,430.00 USD | 933,340.00 USD |
| `7D` | `88.00` | 168,250,000.00 USD | 0.00 USD | 168,250,000.00 USD | 0.00 USD | 12,070.00 USD | 251,100.00 USD |
| `1D` | `88.10` | 176,090,000.00 USD | 0.00 USD | 176,090,000.00 USD | 59,290.00 USD | 35,690.00 USD | 232,900.00 USD |
| `7D` | `88.20` | 167,990,000.00 USD | 0.00 USD | 167,990,000.00 USD | 9,900.00 USD | 20,610.00 USD | 28,240.00 USD |
| `1D` | `88.30` | 175,770,000.00 USD | 0.00 USD | 175,770,000.00 USD | 116,980.00 USD | 275,350.00 USD | 271,390.00 USD |
| `7D` | `88.40` | 167,930,000.00 USD | 0.00 USD | 167,930,000.00 USD | 0.00 USD | 237,870.00 USD | 335,390.00 USD |
| `1D` | `88.50` | 175,100,000.00 USD | 0.00 USD | 175,100,000.00 USD | 86,840.00 USD | 99,900.00 USD | 2,700.00 USD |
| `1D` | `88.70` | 174,910,000.00 USD | 0.00 USD | 174,910,000.00 USD | 204,330.00 USD | 124,180.00 USD | 415,440.00 USD |
| `7D` | `88.80` | 167,350,000.00 USD | 0.00 USD | 167,350,000.00 USD | 241,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `88.90` | 174,170,000.00 USD | 0.00 USD | 174,170,000.00 USD | 143,140.00 USD | 62,660.00 USD | 214,680.00 USD |
| `7D` | `89.00` | 167,110,000.00 USD | 0.00 USD | 167,110,000.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD |
| `1D` | `89.10` | 173,750,000.00 USD | 0.00 USD | 173,750,000.00 USD | 160,900.00 USD | 83,520.00 USD | 36,950.00 USD |
| `7D` | `89.20` | 166,180,000.00 USD | 0.00 USD | 166,180,000.00 USD | 8,180.00 USD | 10,750.00 USD | 315,450.00 USD |
| `1D` | `89.30` | 173,470,000.00 USD | 0.00 USD | 173,470,000.00 USD | 221,290.00 USD | 284,680.00 USD | 1,450.00 USD |
| `7D` | `89.40` | 165,850,000.00 USD | 0.00 USD | 165,850,000.00 USD | 697,470.00 USD | 26,220.00 USD | 160,460.00 USD |
| `1D` | `89.50` | 172,960,000.00 USD | 0.00 USD | 172,960,000.00 USD | 4,870.00 USD | 50,620.00 USD | 273,380.00 USD |
| `7D` | `89.60` | 164,960,000.00 USD | 0.00 USD | 164,960,000.00 USD | 684,220.00 USD | 270,260.00 USD | 723,370.00 USD |
| `1D` | `89.70` | 172,630,000.00 USD | 0.00 USD | 172,630,000.00 USD | 133,580.00 USD | 30,600.00 USD | 428,970.00 USD |
| `7D` | `89.80` | 163,280,000.00 USD | 0.00 USD | 163,280,000.00 USD | 425,950.00 USD | 318,390.00 USD | 314,310.00 USD |
| `1D` | `89.90` | 172,040,000.00 USD | 0.00 USD | 172,040,000.00 USD | 129,660.00 USD | 91,010.00 USD | 141,240.00 USD |
| `7D` | `90.00` | 162,220,000.00 USD | 0.00 USD | 162,220,000.00 USD | 374,600.00 USD | 647,410.00 USD | 1,090,000.00 USD |
| `1D` | `90.10` | 171,680,000.00 USD | 0.00 USD | 171,680,000.00 USD | 1,120,000.00 USD | 893,200.00 USD | 574,300.00 USD |
| `7D` | `90.20` | 160,110,000.00 USD | 0.00 USD | 160,110,000.00 USD | 1,250,000.00 USD | 590,390.00 USD | 735,310.00 USD |
| `1D` | `90.30` | 169,090,000.00 USD | 0.00 USD | 169,090,000.00 USD | 697,230.00 USD | 491,550.00 USD | 441,070.00 USD |
| `7D` | `90.40` | 157,530,000.00 USD | 0.00 USD | 157,530,000.00 USD | 796,240.00 USD | 68,740.00 USD | 694,770.00 USD |
| `1D` | `90.50` | 167,460,000.00 USD | 0.00 USD | 167,460,000.00 USD | 650,510.00 USD | 518,660.00 USD | 884,190.00 USD |
| `7D` | `90.60` | 155,970,000.00 USD | 0.00 USD | 155,970,000.00 USD | 1,040,000.00 USD | 1,010,000.00 USD | 1,560,000.00 USD |
| `1D` | `90.70` | 165,400,000.00 USD | 0.00 USD | 165,400,000.00 USD | 628,630.00 USD | 803,190.00 USD | 369,100.00 USD |
| `7D` | `90.80` | 152,360,000.00 USD | 0.00 USD | 152,360,000.00 USD | 1,210,000.00 USD | 1,200,000.00 USD | 1,480,000.00 USD |
| `1D` | `90.90` | 163,600,000.00 USD | 0.00 USD | 163,600,000.00 USD | 673,680.00 USD | 420,760.00 USD | 119,710.00 USD |
| `7D` | `91.00` | 148,460,000.00 USD | 0.00 USD | 148,460,000.00 USD | 1,190,000.00 USD | 609,900.00 USD | 810,620.00 USD |
| `1D` | `91.10` | 162,390,000.00 USD | 0.00 USD | 162,390,000.00 USD | 436,270.00 USD | 732,110.00 USD | 466,230.00 USD |
| `7D` | `91.20` | 145,860,000.00 USD | 0.00 USD | 145,860,000.00 USD | 2,280,000.00 USD | 868,420.00 USD | 638,860.00 USD |
| `1D` | `91.30` | 160,750,000.00 USD | 0.00 USD | 160,750,000.00 USD | 150,320.00 USD | 221,290.00 USD | 443,030.00 USD |
| `7D` | `91.40` | 142,070,000.00 USD | 0.00 USD | 142,070,000.00 USD | 1,180,000.00 USD | 1,030,000.00 USD | 1,620,000.00 USD |
| `1D` | `91.50` | 159,940,000.00 USD | 0.00 USD | 159,940,000.00 USD | 850,930.00 USD | 781,420.00 USD | 664,870.00 USD |
| `7D` | `91.60` | 138,250,000.00 USD | 0.00 USD | 138,250,000.00 USD | 500,280.00 USD | 1,020,000.00 USD | 872,760.00 USD |
| `1D` | `91.70` | 157,640,000.00 USD | 0.00 USD | 157,640,000.00 USD | 268,750.00 USD | 463,180.00 USD | 1,160,000.00 USD |
| `7D` | `91.80` | 135,860,000.00 USD | 0.00 USD | 135,860,000.00 USD | 932,400.00 USD | 797,110.00 USD | 688,730.00 USD |
| `1D` | `91.90` | 155,750,000.00 USD | 0.00 USD | 155,750,000.00 USD | 1,280,000.00 USD | 813,050.00 USD | 665,680.00 USD |
| `7D` | `92.00` | 133,440,000.00 USD | 0.00 USD | 133,440,000.00 USD | 681,440.00 USD | 656,110.00 USD | 990,500.00 USD |
| `1D` | `92.10` | 152,990,000.00 USD | 0.00 USD | 152,990,000.00 USD | 2,310,000.00 USD | 2,670,000.00 USD | 545,990.00 USD |
| `7D` | `92.20` | 131,110,000.00 USD | 0.00 USD | 131,110,000.00 USD | 2,870,000.00 USD | 1,110,000.00 USD | 289,060.00 USD |
| `1D` | `92.30` | 147,470,000.00 USD | 0.00 USD | 147,470,000.00 USD | 720,590.00 USD | 799,660.00 USD | 1,410,000.00 USD |
| `7D` | `92.40` | 126,850,000.00 USD | 0.00 USD | 126,850,000.00 USD | 550,500.00 USD | 833,900.00 USD | 1,540,000.00 USD |
| `1D` | `92.50` | 144,530,000.00 USD | 0.00 USD | 144,530,000.00 USD | 1,140,000.00 USD | 703,500.00 USD | 2,360,000.00 USD |
| `7D` | `92.60` | 123,930,000.00 USD | 0.00 USD | 123,930,000.00 USD | 98,670.00 USD | 880,990.00 USD | 1,480,000.00 USD |
| `1D` | `92.70` | 140,330,000.00 USD | 0.00 USD | 140,330,000.00 USD | 988,340.00 USD | 1,110,000.00 USD | 1,680,000.00 USD |
| `7D` | `92.80` | 121,470,000.00 USD | 0.00 USD | 121,470,000.00 USD | 444,580.00 USD | 2,340,000.00 USD | 1,610,000.00 USD |
| `1D` | `92.90` | 136,550,000.00 USD | 0.00 USD | 136,550,000.00 USD | 3,310,000.00 USD | 1,980,000.00 USD | 2,530,000.00 USD |
| `7D` | `93.00` | 117,080,000.00 USD | 0.00 USD | 117,080,000.00 USD | 365,950.00 USD | 550,690.00 USD | 1,770,000.00 USD |
| `1D` | `93.10` | 128,730,000.00 USD | 0.00 USD | 128,730,000.00 USD | 2,550,000.00 USD | 3,410,000.00 USD | 2,140,000.00 USD |
| `7D` | `93.20` | 114,380,000.00 USD | 0.00 USD | 114,380,000.00 USD | 1,090,000.00 USD | 670,930.00 USD | 2,130,000.00 USD |
| `1D` | `93.30` | 120,640,000.00 USD | 0.00 USD | 120,640,000.00 USD | 2,980,000.00 USD | 3,170,000.00 USD | 1,420,000.00 USD |
| `7D` | `93.40` | 110,500,000.00 USD | 0.00 USD | 110,500,000.00 USD | 611,840.00 USD | 2,660,000.00 USD | 1,430,000.00 USD |
| `1D` | `93.50` | 113,060,000.00 USD | 0.00 USD | 113,060,000.00 USD | 3,020,000.00 USD | 2,340,000.00 USD | 2,340,000.00 USD |
| `7D` | `93.60` | 105,780,000.00 USD | 0.00 USD | 105,780,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,640,000.00 USD |
| `1D` | `93.70` | 105,360,000.00 USD | 0.00 USD | 105,360,000.00 USD | 640,730.00 USD | 3,170,000.00 USD | 955,360.00 USD |
| `7D` | `93.80` | 102,840,000.00 USD | 0.00 USD | 102,840,000.00 USD | 0.00 USD | 2,080,000.00 USD | 3,170,000.00 USD |
| `1D` | `93.90` | 100,590,000.00 USD | 0.00 USD | 100,590,000.00 USD | 1,610,000.00 USD | 967,780.00 USD | 1,420,000.00 USD |
| `7D` | `94.00` | 97,590,000.00 USD | 0.00 USD | 97,590,000.00 USD | 2,660,000.00 USD | 1,780,000.00 USD | 2,210,000.00 USD |
| `1D` | `94.10` | 96,590,000.00 USD | 0.00 USD | 96,590,000.00 USD | 768,990.00 USD | 1,310,000.00 USD | 2,680,000.00 USD |
| `7D` | `94.20` | 90,950,000.00 USD | 0.00 USD | 90,950,000.00 USD | 24,740.00 USD | 962,410.00 USD | 2,750,000.00 USD |
| `1D` | `94.30` | 91,820,000.00 USD | 0.00 USD | 91,820,000.00 USD | 2,270,000.00 USD | 1,250,000.00 USD | 518,820.00 USD |
| `7D` | `94.40` | 87,210,000.00 USD | 0.00 USD | 87,210,000.00 USD | 0.00 USD | 496,790.00 USD | 9,790.00 USD |
| `1D` | `94.50` | 87,790,000.00 USD | 0.00 USD | 87,790,000.00 USD | 882,080.00 USD | 1,250,000.00 USD | 642,190.00 USD |
| `7D` | `94.60` | 86,700,000.00 USD | 0.00 USD | 86,700,000.00 USD | 560,570.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `94.70` | 85,020,000.00 USD | 0.00 USD | 85,020,000.00 USD | 1,370,000.00 USD | 571,830.00 USD | 402,830.00 USD |
| `7D` | `94.80` | 86,140,000.00 USD | 0.00 USD | 86,140,000.00 USD | 2,050,000.00 USD | 99,300.00 USD | 3,360,000.00 USD |
| `1D` | `94.90` | 82,670,000.00 USD | 0.00 USD | 82,670,000.00 USD | 3,300,000.00 USD | 660,630.00 USD | 1,320,000.00 USD |
| `7D` | `95.00` | 80,630,000.00 USD | 0.00 USD | 80,630,000.00 USD | 3,060,000.00 USD | 4,770,000.00 USD | 1,060,000.00 USD |
| `1D` | `95.10` | 77,390,000.00 USD | 0.00 USD | 77,390,000.00 USD | 3,170,000.00 USD | 1,780,000.00 USD | 852,890.00 USD |
| `7D` | `95.20` | 71,740,000.00 USD | 0.00 USD | 71,740,000.00 USD | 2,420,000.00 USD | 317,900.00 USD | 17,980.00 USD |
| `1D` | `95.30` | 71,590,000.00 USD | 0.00 USD | 71,590,000.00 USD | 1,550,000.00 USD | 1,680,000.00 USD | 3,690,000.00 USD |
| `7D` | `95.40` | 68,980,000.00 USD | 0.00 USD | 68,980,000.00 USD | 2,080,000.00 USD | 2,620,000.00 USD | 4,590,000.00 USD |
| `1D` | `95.50` | 64,670,000.00 USD | 0.00 USD | 64,670,000.00 USD | 471,290.00 USD | 1,690,000.00 USD | 1,560,000.00 USD |
| `7D` | `95.60` | 59,690,000.00 USD | 0.00 USD | 59,690,000.00 USD | 3,820,000.00 USD | 7,040,000.00 USD | 4,590,000.00 USD |
| `1D` | `95.70` | 60,940,000.00 USD | 0.00 USD | 60,940,000.00 USD | 1,900,000.00 USD | 2,230,000.00 USD | 5,660,000.00 USD |
| `7D` | `95.80` | 44,240,000.00 USD | 0.00 USD | 44,240,000.00 USD | 3,400,000.00 USD | 93,510.00 USD | 1,280,000.00 USD |
| `1D` | `95.90` | 51,160,000.00 USD | 0.00 USD | 51,160,000.00 USD | 3,100,000.00 USD | 1,850,000.00 USD | 3,260,000.00 USD |
| `7D` | `96.00` | 39,470,000.00 USD | 0.00 USD | 39,470,000.00 USD | 4,660,000.00 USD | 1,290,000.00 USD | 5,620,000.00 USD |
| `1D` | `96.10` | 42,950,000.00 USD | 0.00 USD | 42,950,000.00 USD | 4,020,000.00 USD | 5,430,000.00 USD | 4,550,000.00 USD |
| `7D` | `96.20` | 27,910,000.00 USD | 0.00 USD | 27,910,000.00 USD | 6,840,000.00 USD | 2,710,000.00 USD | 5,250,000.00 USD |
| `1D` | `96.30` | 28,950,000.00 USD | 0.00 USD | 28,950,000.00 USD | 6,780,000.00 USD | 6,050,000.00 USD | 1,370,000.00 USD |
| `7D` | `96.40` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 1,600,000.00 USD | 2,590,000.00 USD | 6,470,000.00 USD |
| `1D` | `96.50` | 14,750,000.00 USD | 0.00 USD | 14,750,000.00 USD | 3,180,000.00 USD | 1,260,000.00 USD | 4,210,000.00 USD |
| `7D` | `96.60` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD |
| `1D` | `96.70` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 0.00 USD | 2,360,000.00 USD | 965,830.00 USD |
| `7D` | `96.80` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 0.00 USD | 79,170.00 USD | 2,350,000.00 USD |
| `1D` | `96.90` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 0.00 USD | 1,410,000.00 USD | 1,360,000.00 USD |
| `7D` | `97.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `97.20` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,310,000.00 USD |
| `1D` | `97.30` | 6,730.00 USD | 6,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,730.00 USD |
| `7D` | `97.40` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 101,560.00 USD | 0.00 USD |
| `1D` | `97.50` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 534,370.00 USD | 1,280,000.00 USD | 18,370.00 USD |
| `7D` | `97.60` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 0.00 USD | 24,930.00 USD | 3,910,000.00 USD |
| `1D` | `97.70` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,230,000.00 USD |
| `7D` | `97.80` | 18,370,000.00 USD | 18,370,000.00 USD | 0.00 USD | 7,580,000.00 USD | 3,430,000.00 USD | 0.00 USD |
| `1D` | `97.90` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 3,340,000.00 USD | 434,450.00 USD | 1,540,000.00 USD |
| `7D` | `98.00` | 34,380,000.00 USD | 34,380,000.00 USD | 0.00 USD | 13,420,000.00 USD | 561,730.00 USD | 2,030,000.00 USD |
| `1D` | `98.10` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 2,540,000.00 USD | 2,320,000.00 USD | 636,250.00 USD |
| `7D` | `98.20` | 45,290,000.00 USD | 45,290,000.00 USD | 0.00 USD | 9,790,000.00 USD | 1,120,000.00 USD | 0.00 USD |
| `1D` | `98.30` | 23,290,000.00 USD | 23,290,000.00 USD | 0.00 USD | 2,120,000.00 USD | 924,810.00 USD | 6,370,000.00 USD |
| `7D` | `98.40` | 56,430,000.00 USD | 56,430,000.00 USD | 0.00 USD | 1,780,000.00 USD | 3,320,000.00 USD | 6,030,000.00 USD |
| `1D` | `98.50` | 34,260,000.00 USD | 34,260,000.00 USD | 0.00 USD | 654,930.00 USD | 3,460,000.00 USD | 6,850,000.00 USD |
| `7D` | `98.60` | 65,700,000.00 USD | 65,700,000.00 USD | 0.00 USD | 1,920,000.00 USD | 5,400,000.00 USD | 1,950,000.00 USD |
| `1D` | `98.70` | 50,950,000.00 USD | 50,950,000.00 USD | 0.00 USD | 1,560,000.00 USD | 5,460,000.00 USD | 9,680,000.00 USD |
| `7D` | `98.80` | 70,640,000.00 USD | 70,640,000.00 USD | 0.00 USD | 731,910.00 USD | 784,380.00 USD | 3,420,000.00 USD |
| `1D` | `98.90` | 62,130,000.00 USD | 62,130,000.00 USD | 0.00 USD | 2,200,000.00 USD | 3,820,000.00 USD | 5,160,000.00 USD |
| `7D` | `99.00` | 79,470,000.00 USD | 79,470,000.00 USD | 0.00 USD | 2,170,000.00 USD | 2,700,000.00 USD | 3,960,000.00 USD |
| `1D` | `99.10` | 77,520,000.00 USD | 77,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 6,260,000.00 USD | 5,620,000.00 USD |
| `7D` | `99.20` | 93,450,000.00 USD | 93,450,000.00 USD | 0.00 USD | 1,220,000.00 USD | 6,520,000.00 USD | 6,240,000.00 USD |
| `1D` | `99.30` | 87,060,000.00 USD | 87,060,000.00 USD | 0.00 USD | 3,670,000.00 USD | 3,420,000.00 USD | 2,440,000.00 USD |
| `7D` | `99.40` | 94,480,000.00 USD | 94,480,000.00 USD | 0.00 USD | 0.00 USD | 1,010,000.00 USD | 25,850.00 USD |
| `1D` | `99.50` | 92,400,000.00 USD | 92,400,000.00 USD | 0.00 USD | 1,560,000.00 USD | 2,990,000.00 USD | 797,090.00 USD |
| `7D` | `99.60` | 99,910,000.00 USD | 99,910,000.00 USD | 0.00 USD | 2,240,000.00 USD | 2,640,000.00 USD | 545,090.00 USD |
| `1D` | `99.70` | 115,430,000.00 USD | 115,430,000.00 USD | 0.00 USD | 4,400,000.00 USD | 7,410,000.00 USD | 11,230,000.00 USD |
| `7D` | `99.80` | 103,250,000.00 USD | 103,250,000.00 USD | 0.00 USD | 736,270.00 USD | 1,330,000.00 USD | 1,270,000.00 USD |
| `1D` | `99.90` | 124,240,000.00 USD | 124,240,000.00 USD | 0.00 USD | 857,690.00 USD | 1,960,000.00 USD | 5,990,000.00 USD |
| `7D` | `100.00` | 114,570,000.00 USD | 114,570,000.00 USD | 0.00 USD | 2,220,000.00 USD | 2,310,000.00 USD | 6,790,000.00 USD |
| `1D` | `100.10` | 131,440,000.00 USD | 131,440,000.00 USD | 0.00 USD | 2,200,000.00 USD | 3,440,000.00 USD | 1,560,000.00 USD |
| `7D` | `100.20` | 120,660,000.00 USD | 120,660,000.00 USD | 0.00 USD | 843,770.00 USD | 2,460,000.00 USD | 2,780,000.00 USD |
| `1D` | `100.30` | 137,000,000.00 USD | 137,000,000.00 USD | 0.00 USD | 734,910.00 USD | 2,120,000.00 USD | 2,710,000.00 USD |
| `7D` | `100.40` | 125,140,000.00 USD | 125,140,000.00 USD | 0.00 USD | 993,830.00 USD | 654,600.00 USD | 2,830,000.00 USD |
| `1D` | `100.50` | 144,670,000.00 USD | 144,670,000.00 USD | 0.00 USD | 2,200,000.00 USD | 1,260,000.00 USD | 4,200,000.00 USD |
| `7D` | `100.60` | 130,940,000.00 USD | 130,940,000.00 USD | 0.00 USD | 2,130,000.00 USD | 1,450,000.00 USD | 2,220,000.00 USD |
| `1D` | `100.70` | 152,440,000.00 USD | 152,440,000.00 USD | 0.00 USD | 2,230,000.00 USD | 2,360,000.00 USD | 3,180,000.00 USD |
| `7D` | `100.80` | 133,670,000.00 USD | 133,670,000.00 USD | 0.00 USD | 821,420.00 USD | 1,380,000.00 USD | 530,700.00 USD |
| `1D` | `100.90` | 159,520,000.00 USD | 159,520,000.00 USD | 0.00 USD | 2,270,000.00 USD | 2,600,000.00 USD | 2,210,000.00 USD |
| `7D` | `101.00` | 152,640,000.00 USD | 152,640,000.00 USD | 0.00 USD | 4,160,000.00 USD | 7,060,000.00 USD | 7,750,000.00 USD |
| `1D` | `101.10` | 173,120,000.00 USD | 173,120,000.00 USD | 0.00 USD | 8,090,000.00 USD | 2,820,000.00 USD | 2,690,000.00 USD |
| `7D` | `101.20` | 172,050,000.00 USD | 172,050,000.00 USD | 0.00 USD | 7,240,000.00 USD | 5,320,000.00 USD | 6,850,000.00 USD |
| `1D` | `101.30` | 183,460,000.00 USD | 183,460,000.00 USD | 0.00 USD | 3,550,000.00 USD | 3,910,000.00 USD | 2,880,000.00 USD |
| `7D` | `101.40` | 189,110,000.00 USD | 189,110,000.00 USD | 0.00 USD | 4,720,000.00 USD | 1,270,000.00 USD | 11,070,000.00 USD |
| `1D` | `101.50` | 198,970,000.00 USD | 198,970,000.00 USD | 0.00 USD | 3,140,000.00 USD | 3,660,000.00 USD | 8,710,000.00 USD |
| `7D` | `101.60` | 199,630,000.00 USD | 199,630,000.00 USD | 0.00 USD | 3,650,000.00 USD | 30,170.00 USD | 6,840,000.00 USD |
| `1D` | `101.70` | 208,780,000.00 USD | 208,780,000.00 USD | 0.00 USD | 2,220,000.00 USD | 881,090.00 USD | 6,720,000.00 USD |
| `7D` | `101.80` | 209,550,000.00 USD | 209,550,000.00 USD | 0.00 USD | 3,050,000.00 USD | 609,510.00 USD | 6,270,000.00 USD |
| `1D` | `101.90` | 214,610,000.00 USD | 214,610,000.00 USD | 0.00 USD | 2,320,000.00 USD | 1,290,000.00 USD | 2,220,000.00 USD |
| `7D` | `102.00` | 215,550,000.00 USD | 215,550,000.00 USD | 0.00 USD | 1,830,000.00 USD | 1,470,000.00 USD | 2,690,000.00 USD |
| `1D` | `102.10` | 221,070,000.00 USD | 221,070,000.00 USD | 0.00 USD | 2,960,000.00 USD | 1,440,000.00 USD | 2,050,000.00 USD |
| `7D` | `102.20` | 222,270,000.00 USD | 222,270,000.00 USD | 0.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,540,000.00 USD |
| `1D` | `102.30` | 225,840,000.00 USD | 225,840,000.00 USD | 0.00 USD | 1,740,000.00 USD | 1,400,000.00 USD | 1,640,000.00 USD |
| `7D` | `102.40` | 227,580,000.00 USD | 227,580,000.00 USD | 0.00 USD | 2,340,000.00 USD | 304,350.00 USD | 2,660,000.00 USD |
| `1D` | `102.50` | 230,160,000.00 USD | 230,160,000.00 USD | 0.00 USD | 1,510,000.00 USD | 785,070.00 USD | 2,020,000.00 USD |
| `7D` | `102.60` | 230,040,000.00 USD | 230,040,000.00 USD | 0.00 USD | 1,450,000.00 USD | 979,270.00 USD | 33,240.00 USD |
| `1D` | `102.70` | 232,050,000.00 USD | 232,050,000.00 USD | 0.00 USD | 1,110,000.00 USD | 661,840.00 USD | 123,860.00 USD |
| `7D` | `102.80` | 238,130,000.00 USD | 238,130,000.00 USD | 0.00 USD | 7,780,000.00 USD | 23,810.00 USD | 286,910.00 USD |
| `1D` | `102.90` | 236,580,000.00 USD | 236,580,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,530,000.00 USD | 1,490,000.00 USD |
| `7D` | `103.00` | 255,060,000.00 USD | 255,060,000.00 USD | 0.00 USD | 12,270,000.00 USD | 394,420.00 USD | 4,270,000.00 USD |
| `1D` | `103.10` | 241,550,000.00 USD | 241,550,000.00 USD | 0.00 USD | 2,380,000.00 USD | 1,360,000.00 USD | 1,230,000.00 USD |
| `7D` | `103.20` | 267,740,000.00 USD | 267,740,000.00 USD | 0.00 USD | 11,620,000.00 USD | 140,550.00 USD | 913,680.00 USD |
| `1D` | `103.30` | 243,370,000.00 USD | 243,370,000.00 USD | 0.00 USD | 334,720.00 USD | 717,010.00 USD | 770,340.00 USD |
| `7D` | `103.40` | 282,310,000.00 USD | 282,310,000.00 USD | 0.00 USD | 11,050,000.00 USD | 233,330.00 USD | 3,280,000.00 USD |
| `1D` | `103.50` | 249,950,000.00 USD | 249,950,000.00 USD | 0.00 USD | 1,770,000.00 USD | 1,090,000.00 USD | 3,730,000.00 USD |
| `7D` | `103.60` | 300,700,000.00 USD | 300,700,000.00 USD | 0.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD |
| `1D` | `103.70` | 254,660,000.00 USD | 254,660,000.00 USD | 0.00 USD | 1,370,000.00 USD | 720,260.00 USD | 2,620,000.00 USD |
| `7D` | `103.80` | 313,080,000.00 USD | 313,080,000.00 USD | 0.00 USD | 7,960,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD |
| `1D` | `103.90` | 258,470,000.00 USD | 258,470,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,640,000.00 USD | 801,570.00 USD |
| `7D` | `104.00` | 339,790,000.00 USD | 339,790,000.00 USD | 0.00 USD | 10,830,000.00 USD | 7,160,000.00 USD | 8,710,000.00 USD |
| `1D` | `104.10` | 263,580,000.00 USD | 263,580,000.00 USD | 0.00 USD | 2,180,000.00 USD | 748,620.00 USD | 2,180,000.00 USD |
| `7D` | `104.20` | 361,810,000.00 USD | 361,810,000.00 USD | 0.00 USD | 8,520,000.00 USD | 7,230,000.00 USD | 6,280,000.00 USD |
| `1D` | `104.30` | 266,880,000.00 USD | 266,880,000.00 USD | 0.00 USD | 1,160,000.00 USD | 1,150,000.00 USD | 985,040.00 USD |
| `7D` | `104.40` | 379,000,000.00 USD | 379,000,000.00 USD | 0.00 USD | 5,100,000.00 USD | 3,710,000.00 USD | 8,360,000.00 USD |
| `1D` | `104.50` | 270,590,000.00 USD | 270,590,000.00 USD | 0.00 USD | 1,350,000.00 USD | 1,140,000.00 USD | 1,220,000.00 USD |
| `7D` | `104.60` | 396,750,000.00 USD | 396,750,000.00 USD | 0.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 7,020,000.00 USD |
| `1D` | `104.70` | 276,360,000.00 USD | 276,360,000.00 USD | 0.00 USD | 1,690,000.00 USD | 982,920.00 USD | 3,090,000.00 USD |
| `7D` | `104.80` | 414,140,000.00 USD | 414,140,000.00 USD | 0.00 USD | 5,170,000.00 USD | 4,410,000.00 USD | 7,820,000.00 USD |
| `1D` | `104.90` | 277,830,000.00 USD | 277,830,000.00 USD | 0.00 USD | 486,940.00 USD | 283,560.00 USD | 703,940.00 USD |
| `7D` | `105.00` | 430,300,000.00 USD | 430,300,000.00 USD | 0.00 USD | 5,730,000.00 USD | 4,110,000.00 USD | 6,330,000.00 USD |
| `1D` | `105.10` | 279,670,000.00 USD | 279,670,000.00 USD | 0.00 USD | 299,230.00 USD | 436,680.00 USD | 1,100,000.00 USD |
| `7D` | `105.20` | 440,970,000.00 USD | 440,970,000.00 USD | 0.00 USD | 5,340,000.00 USD | 2,800,000.00 USD | 2,530,000.00 USD |
| `1D` | `105.30` | 279,860,000.00 USD | 279,860,000.00 USD | 0.00 USD | 94,380.00 USD | 96,460.00 USD | 2,140.00 USD |
| `7D` | `105.40` | 449,180,000.00 USD | 449,180,000.00 USD | 0.00 USD | 1,570,000.00 USD | 3,170,000.00 USD | 3,470,000.00 USD |
| `1D` | `105.50` | 280,470,000.00 USD | 280,470,000.00 USD | 0.00 USD | 245,610.00 USD | 180,000.00 USD | 187,100.00 USD |
| `7D` | `105.60` | 457,610,000.00 USD | 457,610,000.00 USD | 0.00 USD | 3,700,000.00 USD | 2,270,000.00 USD | 2,450,000.00 USD |
| `1D` | `105.70` | 280,690,000.00 USD | 280,690,000.00 USD | 0.00 USD | 65,040.00 USD | 150,210.00 USD | 2,630.00 USD |
| `7D` | `105.80` | 466,420,000.00 USD | 466,420,000.00 USD | 0.00 USD | 2,690,000.00 USD | 2,620,000.00 USD | 3,510,000.00 USD |
| `1D` | `105.90` | 281,740,000.00 USD | 281,740,000.00 USD | 0.00 USD | 171,160.00 USD | 683,690.00 USD | 192,750.00 USD |
| `7D` | `106.00` | 471,570,000.00 USD | 471,570,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,050,000.00 USD | 2,130,000.00 USD |
| `1D` | `106.10` | 283,130,000.00 USD | 283,130,000.00 USD | 0.00 USD | 706,860.00 USD | 457,510.00 USD | 222,640.00 USD |
| `7D` | `106.20` | 480,460,000.00 USD | 480,460,000.00 USD | 0.00 USD | 3,820,000.00 USD | 2,560,000.00 USD | 2,520,000.00 USD |
| `1D` | `106.30` | 284,290,000.00 USD | 284,290,000.00 USD | 0.00 USD | 283,710.00 USD | 484,380.00 USD | 395,590.00 USD |
| `7D` | `106.40` | 486,520,000.00 USD | 486,520,000.00 USD | 0.00 USD | 2,420,000.00 USD | 2,170,000.00 USD | 1,460,000.00 USD |
| `1D` | `106.50` | 285,120,000.00 USD | 285,120,000.00 USD | 0.00 USD | 323,470.00 USD | 246,080.00 USD | 256,190.00 USD |
| `7D` | `106.60` | 491,360,000.00 USD | 491,360,000.00 USD | 0.00 USD | 1,330,000.00 USD | 1,250,000.00 USD | 2,260,000.00 USD |
| `1D` | `106.70` | 287,490,000.00 USD | 287,490,000.00 USD | 0.00 USD | 654,410.00 USD | 284,770.00 USD | 1,440,000.00 USD |
| `7D` | `106.80` | 496,020,000.00 USD | 496,020,000.00 USD | 0.00 USD | 999,190.00 USD | 927,000.00 USD | 2,730,000.00 USD |
| `1D` | `106.90` | 288,310,000.00 USD | 288,310,000.00 USD | 0.00 USD | 156,730.00 USD | 336,790.00 USD | 325,920.00 USD |
| `7D` | `107.00` | 500,160,000.00 USD | 500,160,000.00 USD | 0.00 USD | 527,980.00 USD | 1,180,000.00 USD | 2,430,000.00 USD |
| `1D` | `107.10` | 289,380,000.00 USD | 289,380,000.00 USD | 0.00 USD | 97,170.00 USD | 368,740.00 USD | 600,240.00 USD |
| `7D` | `107.20` | 501,250,000.00 USD | 501,250,000.00 USD | 0.00 USD | 230,020.00 USD | 507,570.00 USD | 352,500.00 USD |
| `1D` | `107.30` | 289,710,000.00 USD | 289,710,000.00 USD | 0.00 USD | 60,260.00 USD | 159,710.00 USD | 110,290.00 USD |
| `1D` | `107.40` | 290,160,000.00 USD | 290,160,000.00 USD | 0.00 USD | 0.00 USD | 41,740.00 USD | 408,060.00 USD |
| `7D` | `107.40` | 502,530,000.00 USD | 502,530,000.00 USD | 0.00 USD | 0.00 USD | 576,040.00 USD | 709,670.00 USD |
| `7D` | `107.60` | 503,160,000.00 USD | 503,160,000.00 USD | 0.00 USD | 213,520.00 USD | 12,070.00 USD | 406,020.00 USD |
| `7D` | `107.80` | 504,000,000.00 USD | 504,000,000.00 USD | 0.00 USD | 499,550.00 USD | 31,020.00 USD | 305,630.00 USD |
| `7D` | `108.00` | 504,580,000.00 USD | 504,580,000.00 USD | 0.00 USD | 5,950.00 USD | 237,870.00 USD | 335,390.00 USD |
| `7D` | `108.20` | 504,860,000.00 USD | 504,860,000.00 USD | 0.00 USD | 0.00 USD | 205,080.00 USD | 74,400.00 USD |
| `7D` | `108.40` | 505,350,000.00 USD | 505,350,000.00 USD | 0.00 USD | 487,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `108.60` | 505,530,000.00 USD | 505,530,000.00 USD | 0.00 USD | 17,470.00 USD | 167,730.00 USD | 0.00 USD |
| `7D` | `108.80` | 506,470,000.00 USD | 506,470,000.00 USD | 0.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD |
| `7D` | `109.00` | 506,760,000.00 USD | 506,760,000.00 USD | 0.00 USD | 8,180.00 USD | 0.00 USD | 286,720.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `5.60B` | Total OI Tokens: `57,836,804.5 SOL`
  * 1h OI Change: `-0.06%` | 4h OI Change: `-2.06%` | 24h OI Change: `-13.41%`
  * Exchange Breakdown: Binance=`968.34M` | Bybit=`608.96M` | OKX=`384.75M` | Hyperliquid=`517.53M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-46.56K` | Last 24h: `177.62K` | Last 3d: `997.77K` | Last 7d: `2.11M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0054%` | **USDT OKX** | `-0.0165%` |
| **USDT Bybit** | `-0.0057%` | **USDT KuCoin** | `-0.0088%` |
| **USDT MEXC** | `0.0053%` | **USDT BingX** | `0.0052%` |
| **USDT Gate** | `-0.0070%` | **USDT Bitget** | `-0.0114%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0013%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `39.40%` | `60.60%` | `0.65` | 27,410,000.00 USD |
| `15M` | `Binance` | `43.19%` | `56.81%` | `0.76` | 7,430,000.00 USD |
| `15M` | `OKX` | `27.26%` | `72.74%` | `0.37` | 2,420,000.00 USD |
| `15M` | `Bybit` | `26.53%` | `73.47%` | `0.36` | 3,360,000.00 USD |
| `15M` | `KuCoin` | `51.86%` | `48.14%` | `1.08` | 415,930.00 USD |
| `15M` | `Gate` | `60.15%` | `39.85%` | `1.51` | 1,560,000.00 USD |
| `15M` | `Bitget` | `34.82%` | `65.18%` | `0.53` | 2,240,000.00 USD |
| `15M` | `BingX` | `57.33%` | `42.67%` | `1.34` | 573,710.00 USD |
| `15M` | `MEXC` | `49.39%` | `50.61%` | `0.98` | 5,410,000.00 USD |
| `15M` | `Bitunix` | `50.87%` | `49.13%` | `1.04` | 1,120,000.00 USD |
| `15M` | `Hyperliquid` | `38.77%` | `61.23%` | `0.63` | 475,190.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.1%` | `50.9%` | `0.96` | 66,250.00 USD |
| `15M` | `Crypto.com` | `55.66%` | `44.34%` | `1.26` | 44,250.00 USD |
| `15M` | `WhiteBIT` | `8.32%` | `91.68%` | `0.09` | 2,010,000.00 USD |
| `15M` | `HTX` | `46.24%` | `53.76%` | `0.86` | 10,470.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `32.11%` | `67.89%` | `0.47` | 98,580.00 USD |
| `15M` | `Aster` | `44.09%` | `55.91%` | `0.79` | 91,700.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `62.61%` | `37.39%` | `1.67` | 63,520.00 USD |
| `15M` | `Whale Positions` | `43.19%` | `56.81%` | `0.76` | 7,430,000.00 USD |
| `15M` | `Global Accounts` | `39.40%` | `60.60%` | `0.65` | 27,410,000.00 USD |
| `1H` | `SOL` | `44.63%` | `55.37%` | `0.81` | 115,130,000.00 USD |
| `1H` | `Binance` | `48.16%` | `51.84%` | `0.93` | 36,300,000.00 USD |
| `1H` | `OKX` | `45.19%` | `54.81%` | `0.82` | 13,080,000.00 USD |
| `1H` | `Bybit` | `43.49%` | `56.51%` | `0.77` | 18,640,000.00 USD |
| `1H` | `KuCoin` | `51.97%` | `48.03%` | `1.08` | 1,220,000.00 USD |
| `1H` | `Gate` | `54.57%` | `45.43%` | `1.20` | 5,370,000.00 USD |
| `1H` | `Bitget` | `50.18%` | `49.82%` | `1.01` | 7,990,000.00 USD |
| `1H` | `BingX` | `36.46%` | `63.54%` | `0.57` | 2,660,000.00 USD |
| `1H` | `MEXC` | `47.42%` | `52.58%` | `0.90` | 14,440,000.00 USD |
| `1H` | `Bitunix` | `51.11%` | `48.89%` | `1.05` | 4,150,000.00 USD |
| `1H` | `Hyperliquid` | `51.99%` | `48.01%` | `1.08` | 2,310,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.29%` | `48.71%` | `1.05` | 395,140.00 USD |
| `1H` | `Crypto.com` | `46.3%` | `53.7%` | `0.86` | 206,310.00 USD |
| `1H` | `WhiteBIT` | `2.4%` | `97.6%` | `0.02` | 6,770,000.00 USD |
| `1H` | `HTX` | `28.79%` | `71.21%` | `0.40` | 69,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `36.73%` | `63.27%` | `0.58` | 712,800.00 USD |
| `1H` | `Aster` | `47.05%` | `52.95%` | `0.89` | 564,280.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `65.2%` | `34.8%` | `1.87` | 280,220.00 USD |
| `1H` | `Whale Positions` | `48.16%` | `51.84%` | `0.93` | 36,300,000.00 USD |
| `1H` | `Global Accounts` | `44.63%` | `55.37%` | `0.81` | 115,130,000.00 USD |
| `4H` | `SOL` | `47.02%` | `52.98%` | `0.89` | 481,530,000.00 USD |
| `4H` | `Binance` | `48.6%` | `51.4%` | `0.95` | 163,890,000.00 USD |
| `4H` | `OKX` | `46.72%` | `53.28%` | `0.88` | 54,130,000.00 USD |
| `4H` | `Bybit` | `48.62%` | `51.38%` | `0.95` | 80,440,000.00 USD |
| `4H` | `KuCoin` | `49.96%` | `50.04%` | `1.00` | 4,370,000.00 USD |
| `4H` | `Gate` | `55.59%` | `44.41%` | `1.25` | 23,730,000.00 USD |
| `4H` | `Bitget` | `49.43%` | `50.57%` | `0.98` | 34,890,000.00 USD |
| `4H` | `BingX` | `27.84%` | `72.16%` | `0.39` | 11,140,000.00 USD |
| `4H` | `MEXC` | `48.07%` | `51.93%` | `0.93` | 57,650,000.00 USD |
| `4H` | `Bitunix` | `46.02%` | `53.98%` | `0.85` | 17,930,000.00 USD |
| `4H` | `Hyperliquid` | `62.15%` | `37.85%` | `1.64` | 10,540,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.44%` | `50.56%` | `0.98` | 1,550,000.00 USD |
| `4H` | `Crypto.com` | `48.16%` | `51.84%` | `0.93` | 905,160.00 USD |
| `4H` | `WhiteBIT` | `5.03%` | `94.97%` | `0.05` | 14,620,000.00 USD |
| `4H` | `HTX` | `46.93%` | `53.07%` | `0.88` | 265,190.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `28.63%` | `71.37%` | `0.40` | 1,420,000.00 USD |
| `4H` | `Aster` | `36.15%` | `63.85%` | `0.57` | 3,340,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `59.01%` | `40.99%` | `1.44` | 728,840.00 USD |
| `4H` | `Whale Positions` | `48.6%` | `51.4%` | `0.95` | 163,890,000.00 USD |
| `4H` | `Global Accounts` | `47.02%` | `52.98%` | `0.89` | 481,530,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `97.70` | `97.69` | `97.70` | `98.20` | `97.19` | 26,621,435.83 USD | 11,084,087.20 USD | 15,537,348.64 USD | -4,453,261.44 USD | `-16.73%` | `5B / 32S` |
| `5:00 UTC` | `97.31` | `97.23` | `97.31` | `97.59` | `96.94` | 34,349,154.70 USD | 16,069,023.45 USD | 18,280,131.25 USD | -2,211,107.80 USD | `-6.44%` | `8B / 12S` |
| `0:00 UTC` | `97.07` | `97.11` | `97.07` | `97.31` | `96.84` | 19,320,776.86 USD | 9,044,516.83 USD | 10,276,260.03 USD | -1,231,743.19 USD | `-6.38%` | `6B / 9S` |
| `5:00 UTC` | `97.31` | `97.36` | `97.31` | `97.56` | `97.18` | 14,539,694.05 USD | 7,744,567.35 USD | 6,795,126.70 USD | 949,440.65 USD | `+6.53%` | `8B / 2S` |
| `0:00 UTC` | `97.15` | `97.19` | `97.15` | `97.37` | `97.05` | 9,961,152.58 USD | 4,407,159.48 USD | 5,553,993.10 USD | -1,146,833.62 USD | `-11.51%` | `1B / 5S` |
| `5:00 UTC` | `97.03` | `97.24` | `97.03` | `97.56` | `97.00` | 11,034,358.76 USD | 5,603,314.27 USD | 5,431,044.48 USD | 172,269.79 USD | `+1.56%` | `15B / 4S` |
| `0:00 UTC` | `97.13` | `97.19` | `97.13` | `97.44` | `97.03` | 17,561,649.50 USD | 7,274,477.25 USD | 10,287,172.25 USD | -3,012,695.00 USD | `-17.15%` | `4B / 13S` |
| `5:00 UTC` | `96.81` | `96.94` | `96.81` | `97.16` | `96.81` | 12,337,515.78 USD | 5,226,804.15 USD | 7,110,711.63 USD | -1,883,907.48 USD | `-15.27%` | `2B / 2S` |
| `0:00 UTC` | `96.81` | `96.92` | `96.81` | `97.16` | `96.69` | 14,931,632.13 USD | 8,028,191.38 USD | 6,903,440.75 USD | 1,124,750.63 USD | `+7.53%` | `9B / 6S` |
| `5:00 UTC` | `96.95` | `96.91` | `96.95` | `97.02` | `96.78` | 2,402,359.64 USD | 1,419,930.49 USD | 982,429.15 USD | 437,501.34 USD | `+18.21%` | `5B / 8S` |

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
| `5m` | 48,100.00 USD | 693,210.00 USD | **`ACCUMULATION`** |
| `15m` | 477,760.00 USD | 4,440,000.00 USD | **`ACCUMULATION`** |
| `30m` | -869,710.00 USD | -1,310,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,100,000.00 USD | -9,940,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -876,090.00 USD | -17,920,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -3,800,000.00 USD | -38,100,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 1,490,000.00 USD | -31,480,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 4,800,000.00 USD | -798,550.00 USD | **`ACCUMULATION`** |
| `12h` | -26,610,000.00 USD | -121,370,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -48,190,000.00 USD | -437,730,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 33,240,000.00 USD | -695,420,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -8,270,000.00 USD | -2,200,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+48.10K` | 15m=`+477.76K` | 1h=`-2.10M` | 24h=`-48.19M`
* Futures Capital Netflows: 5m=`+693.21K` | 15m=`+4.44M` | 1h=`-9.94M` | 24h=`-437.73M`
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
  * `2026-10-30 15:12:05 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:05 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:34:05 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:05 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `95.09` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `94.00` (Risk Distance: `1.09` pts)
  * +2.5R Take Profit: `97.81`
  * Mathematical Lot Sizing: **`9.20 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `98.09` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `99.18` (Risk Distance: `1.09` pts)
  * +2.5R Take Profit: `95.37`
  * Mathematical Lot Sizing: **`9.20 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`97.51`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
