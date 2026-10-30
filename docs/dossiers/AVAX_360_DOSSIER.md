# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 08:33:46 IST` (`2026-10-30 03:03:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.29` | **Live Ask Quote**: `8.32` | **Mid Price**: `8.30`
- **Spread Points**: `3.00` | **Spread BPS**: `36.12 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
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
  * Session VWAP: `8.15` | VWAP Z-Score: `+2.45` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0978` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `48.22` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `8.36` | Lower -3.00σ Band: `7.95`
  * Upper +2.51σ Band: `8.32` | Lower -2.51σ Band: `7.98`
  * Upper +2.01σ Band: `8.29` | Lower -2.01σ Band: `8.02`
  * Upper +2.00σ Band: `8.29` | Lower -2.00σ Band: `8.02`
  * Upper +1.28σ Band: `8.24` | Lower -1.28σ Band: `8.07`
  * Upper +1.00σ Band: `8.22` | Lower -1.00σ Band: `8.09`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.24` | EMA-20=`8.29` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.47` (Slope: `+0.0000`) | EMA-100=`8.60`
  * Institutional Anchors: EMA-144=`8.66` | EMA-200=`8.70` (Slope: `-0.7218`) | EMA-233=`8.73`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`7.97` | Weekly High=`9.14` | Weekly Low=`7.97`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.40` (Distance: `-1.17%`)
  * Point of Control (POC) = `8.32` (Distance: `-0.20%`)
  * Value Area Low (VAL) = `8.13` (Distance: `+2.09%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`9.01` | Weekly POC=`8.92` | Weekly VAL=`8.73`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.58` | Low=`7.97`
  * London Session (08:00-16:00 UTC): High=`8.34` | Low=`8.27`
  * New York Session (13:00-21:00 UTC): High=`8.35` | Low=`8.26`
  * Initial Balance (First Hour): IB High=`8.33` | IB Low=`8.28`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.27` - `8.34`
  * Optimal Trade Entry (OTE 0.705): `8.32`
  * Structural Invalidation Anchor (0.786): `8.37`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.32` | `8.33` | `8.30` | `8.31` | `38,249` | 318,213.22 USD | -37,166.82 USD | `-11.68%` | -6,212,527.98 USD | `-0.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `8.31` | `8.34` | `8.30` | `8.33` | `34,554` | 287,957.01 USD | 103,562.60 USD | `+35.96%` | -6,108,965.38 USD | `+0.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `8.33` | `8.34` | `8.33` | `8.34` | `18,256` | 152,173.33 USD | -3,659.15 USD | `-2.40%` | -6,112,624.53 USD | `-0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `8.21` | `8.25` | `8.15` | `8.25` | `149,172` | 1,223,062.19 USD | 214,869.37 USD | `+17.57%` | -6,483,090.30 USD | `+0.15` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.25` | `8.33` | `8.24` | `8.32` | `125,760` | 1,042,239.86 USD | 307,729.14 USD | `+29.53%` | -6,175,361.16 USD | `+0.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.32` | `8.34` | `8.30` | `8.34` | `91,059` | 758,343.56 USD | 62,736.63 USD | `+8.27%` | -6,112,624.53 USD | `-0.03` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `8.28` | `8.30` | `7.99` | `8.21` | `2,821,552` | 22,964,413.15 USD | -1,514,352.98 USD | `-6.59%` | -7,460,951.56 USD | `-0.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `8.21` | `8.28` | `8.11` | `8.21` | `1,052,344` | 8,640,631.11 USD | 498,870.95 USD | `+5.77%` | -6,962,080.61 USD | `+0.51` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `8.21` | `8.34` | `8.15` | `8.34` | `365,991` | 3,023,645.62 USD | 585,335.14 USD | `+19.36%` | -6,376,745.47 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,242,979.60 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,578,925.42 USD | `-1.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.34` | `7.99` | `8.34` | `4,239,887` | 34,628,689.87 USD | -430,146.90 USD | `-1.24%` | -6,009,072.32 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | 322,838.02 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | 269,016.05 USD | `-1.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,242,979.60 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,578,925.42 USD | `-1.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.35` | `7.99` | `8.32` | `4,327,760` | 35,360,117.70 USD | -471,997.59 USD | `-1.33%` | -6,050,923.01 USD | `+0.39` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`8.30`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BUY` | `8.16` | `2696.4400` | 21,999.98 USD | 4,318,678.10 USD | `STANDARD` | `-1.95%` | `0x0efb38a5fa` |
| `BUY` | `8.16` | `453.2000` | 3,698.20 USD | 5,417,240.92 USD | `STANDARD` | `-1.93%` | `0x6abc111bd2` |
| `BUY` | `8.16` | `250.0000` | 2,040.53 USD | 5,483,735.03 USD | `STANDARD` | `-1.91%` | `0x6abc111bd2` |
| `BUY` | `8.17` | `76046.4300` | 621,428.61 USD | 1,267,998.90 USD | `LARGE (>= USD 100K)` | `-1.79%` | `0x71cfa5e263` |
| `BUY` | `8.17` | `315.7300` | 2,578.57 USD | 5,457,239.32 USD | `STANDARD` | `-1.85%` | `0x07fd993f0f` |
| `BUY` | `8.17` | `250.0000` | 2,042.83 USD | 5,481,694.50 USD | `STANDARD` | `-1.80%` | `0x6abc111bd2` |
| `BUY` | `8.18` | `250.0000` | 2,045.55 USD | 5,479,651.68 USD | `STANDARD` | `-1.67%` | `0x6abc111bd2` |
| `BUY` | `8.19` | `14758.7700` | 120,908.27 USD | 3,606,654.76 USD | `LARGE (>= USD 100K)` | `-1.55%` | `0xecb63caa47` |
| `BUY` | `8.19` | `2319.3000` | 18,999.94 USD | 4,356,678.00 USD | `STANDARD` | `-1.55%` | `0x0efb38a5fa` |
| `BUY` | `8.19` | `2223.5100` | 18,213.88 USD | 4,412,476.30 USD | `STANDARD` | `-1.56%` | `0xd3943e4008` |
| `BUY` | `8.19` | `250.0000` | 2,048.70 USD | 5,477,606.13 USD | `STANDARD` | `-1.52%` | `0x6abc111bd2` |
| `BUY` | `8.20` | `17723.0700` | 145,341.58 USD | 2,845,427.46 USD | `LARGE (>= USD 100K)` | `-1.44%` | `0x71d0e11ebb` |
| `BUY` | `8.20` | `208.1000` | 1,706.21 USD | 5,487,454.74 USD | `STANDARD` | `-1.46%` | `0x010461c14e` |
| `BUY` | `8.20` | `200.9500` | 1,647.61 USD | 5,490,755.17 USD | `STANDARD` | `-1.46%` | `0x31ca8395cf` |
| `BUY` | `8.21` | `15570.4600` | 127,808.56 USD | 3,230,597.27 USD | `LARGE (>= USD 100K)` | `-1.35%` | `0xecb63caa47` |
| `BUY` | `8.21` | `4339.9600` | 35,615.88 USD | 4,269,933.12 USD | `MEDIUM (>= USD 25K)` | `-1.37%` | `0xa24c5ca26c` |
| `BUY` | `8.21` | `500.0000` | 4,103.60 USD | 5,343,414.78 USD | `STANDARD` | `-1.37%` | `0x6abc111bd2` |
| `BUY` | `8.22` | `39372.5600` | 323,504.64 USD | 1,922,163.64 USD | `LARGE (>= USD 100K)` | `-1.25%` | `0x71cfa5e263` |
| `BUY` | `8.22` | `13727.6000` | 112,908.14 USD | 3,719,562.89 USD | `LARGE (>= USD 100K)` | `-1.15%` | `0xecb63caa47` |
| `BUY` | `8.22` | `7699.5600` | 63,288.07 USD | 4,193,854.04 USD | `MEDIUM (>= USD 25K)` | `-1.22%` | `0x71d0e11ebb` |
| `BUY` | `8.22` | `1945.8500` | 15,999.95 USD | 4,446,305.58 USD | `STANDARD` | `-1.18%` | `0x0efb38a5fa` |
| `BUY` | `8.22` | `1750.5800` | 14,383.64 USD | 4,942,229.45 USD | `STANDARD` | `-1.25%` | `0xd3943e4008` |
| `BUY` | `8.22` | `500.0000` | 4,109.25 USD | 5,335,206.50 USD | `STANDARD` | `-1.23%` | `0x6abc111bd2` |
| `BUY` | `8.22` | `315.7300` | 2,596.56 USD | 5,452,067.80 USD | `STANDARD` | `-1.16%` | `0x07fd993f0f` |
| `BUY` | `8.23` | `500.0000` | 4,117.40 USD | 5,331,097.25 USD | `STANDARD` | `-1.03%` | `0x6abc111bd2` |
| `BUY` | `8.24` | `17710.1200` | 145,945.56 USD | 2,700,085.88 USD | `LARGE (>= USD 100K)` | `-0.96%` | `0x71d0e11ebb` |
| `BUY` | `8.24` | `8161.7900` | 67,266.21 USD | 4,065,729.23 USD | `MEDIUM (>= USD 25K)` | `-0.95%` | `0xecb63caa47` |
| `BUY` | `8.25` | `12142.3000` | 100,188.55 USD | 3,919,943.65 USD | `LARGE (>= USD 100K)` | `-0.84%` | `0x881cd92459` |
| `BUY` | `8.25` | `2278.1200` | 18,792.21 USD | 4,375,470.21 USD | `STANDARD` | `-0.86%` | `0xa38f19c4cc` |
| `BUY` | `8.25` | `1866.9900` | 15,407.33 USD | 4,927,845.81 USD | `STANDARD` | `-0.82%` | `0x57d8e75f47` |
| `BUY` | `8.25` | `1496.4100` | 12,338.80 USD | 4,981,541.25 USD | `STANDARD` | `-0.90%` | `0xd3943e4008` |
| `BUY` | `8.25` | `1453.7500` | 11,999.98 USD | 4,993,541.23 USD | `STANDARD` | `-0.80%` | `0x0efb38a5fa` |
| `BUY` | `8.25` | `962.0800` | 7,941.39 USD | 5,216,104.24 USD | `STANDARD` | `-0.80%` | `0xd2ccf2ebc5` |
| `BUY` | `8.25` | `150.0000` | 1,237.20 USD | 5,499,484.07 USD | `STANDARD` | `-0.88%` | `0x6abc111bd2` |
| `BUY` | `8.25` | `88.2500` | 727.66 USD | 5,549,655.91 USD | `STANDARD` | `-0.91%` | `0x31ca8395cf` |
| `BUY` | `8.25` | `79.5400` | 655.84 USD | 5,558,563.79 USD | `STANDARD` | `-0.91%` | `0x010461c14e` |
| `BUY` | `8.26` | `3236.1300` | 26,745.00 USD | 4,296,678.12 USD | `MEDIUM (>= USD 25K)` | `-0.68%` | `0x26934acbd3` |
| `BUY` | `8.26` | `1866.9900` | 15,424.88 USD | 4,897,022.37 USD | `STANDARD` | `-0.71%` | `0x57d8e75f47` |
| `BUY` | `8.26` | `1866.9900` | 15,416.11 USD | 4,912,438.48 USD | `STANDARD` | `-0.77%` | `0x57d8e75f47` |
| `BUY` | `8.27` | `20056.2000` | 165,896.86 USD | 2,255,861.75 USD | `LARGE (>= USD 100K)` | `-0.59%` | `0x71cfa5e263` |
| `BUY` | `8.27` | `15402.0800` | 127,404.47 USD | 3,485,746.48 USD | `LARGE (>= USD 100K)` | `-0.59%` | `0x71d0e11ebb` |
| `BUY` | `8.27` | `1866.9900` | 15,442.43 USD | 4,866,163.83 USD | `STANDARD` | `-0.60%` | `0x57d8e75f47` |
| `BUY` | `8.27` | `1866.9900` | 15,433.66 USD | 4,881,597.48 USD | `STANDARD` | `-0.65%` | `0x57d8e75f47` |
| `BUY` | `8.27` | `1336.5000` | 11,054.19 USD | 5,028,592.86 USD | `STANDARD` | `-0.60%` | `0xa38f19c4cc` |
| `BUY` | `8.27` | `1233.9000` | 10,208.92 USD | 5,081,321.70 USD | `STANDARD` | `-0.57%` | `0xd3943e4008` |
| `BUY` | `8.27` | `487.0900` | 4,027.26 USD | 5,351,514.60 USD | `STANDARD` | `-0.64%` | `0xcd7f60e943` |
| `BUY` | `8.27` | `105.1400` | 869.78 USD | 5,541,148.09 USD | `STANDARD` | `-0.58%` | `0xf30120f048` |
| `BUY` | `8.27` | `105.1400` | 869.72 USD | 5,542,017.81 USD | `STANDARD` | `-0.59%` | `0xd0956a1eba` |
| `BUY` | `8.28` | `1866.9900` | 15,459.98 USD | 4,835,270.18 USD | `STANDARD` | `-0.48%` | `0x57d8e75f47` |
| `BUY` | `8.28` | `1866.9900` | 15,451.21 USD | 4,850,721.39 USD | `STANDARD` | `-0.54%` | `0x57d8e75f47` |
| `BUY` | `8.28` | `1084.3700` | 8,980.54 USD | 5,158,241.28 USD | `STANDARD` | `-0.47%` | `0xd3342d3b1e` |
| `BUY` | `8.28` | `965.8900` | 7,999.98 USD | 5,192,163.40 USD | `STANDARD` | `-0.46%` | `0x0efb38a5fa` |
| `BUY` | `8.28` | `954.4300` | 7,907.07 USD | 5,224,011.31 USD | `STANDARD` | `-0.44%` | `0xecb63caa47` |
| `BUY` | `8.28` | `767.3800` | 6,356.82 USD | 5,279,885.05 USD | `STANDARD` | `-0.45%` | `0x47a4471457` |
| `BUY` | `8.28` | `76.9000` | 636.50 USD | 5,561,139.71 USD | `STANDARD` | `-0.53%` | `0x31ca8395cf` |
| `BUY` | `8.28` | `76.8800` | 636.34 USD | 5,561,776.05 USD | `STANDARD` | `-0.53%` | `0x010461c14e` |
| `BUY` | `8.29` | `1866.9900` | 15,486.31 USD | 4,788,863.90 USD | `STANDARD` | `-0.31%` | `0x57d8e75f47` |
| `BUY` | `8.29` | `1866.9900` | 15,477.53 USD | 4,804,341.44 USD | `STANDARD` | `-0.37%` | `0x57d8e75f47` |
| `BUY` | `8.29` | `1866.9900` | 15,468.76 USD | 4,819,810.20 USD | `STANDARD` | `-0.43%` | `0x57d8e75f47` |
| `BUY` | `8.29` | `1086.6200` | 9,011.45 USD | 5,149,260.75 USD | `STANDARD` | `-0.33%` | `0x26934acbd3` |
| `BUY` | `8.29` | `1048.5300` | 8,689.17 USD | 5,175,766.07 USD | `STANDARD` | `-0.41%` | `0xd3943e4008` |
| `BUY` | `8.29` | `942.9800` | 7,817.59 USD | 5,239,689.46 USD | `STANDARD` | `-0.37%` | `0xd3943e4008` |
| `BUY` | `8.29` | `831.4900` | 6,888.98 USD | 5,254,100.71 USD | `STANDARD` | `-0.43%` | `0xecb63caa47` |
| `BUY` | `8.29` | `784.8300` | 6,502.47 USD | 5,260,603.19 USD | `STANDARD` | `-0.43%` | `0xa38f19c4cc` |
| `BUY` | `8.29` | `495.2200` | 4,104.68 USD | 5,339,311.18 USD | `STANDARD` | `-0.39%` | `0xecb63caa47` |
| `BUY` | `8.29` | `467.8500` | 3,877.63 USD | 5,398,460.42 USD | `STANDARD` | `-0.39%` | `0x2a72b57dea` |
| `BUY` | `8.29` | `366.8200` | 3,042.77 USD | 5,438,816.31 USD | `STANDARD` | `-0.31%` | `0xdd4f66125d` |
| `BUY` | `8.29` | `255.8700` | 2,122.34 USD | 5,475,557.43 USD | `STANDARD` | `-0.32%` | `0xecb63caa47` |
| `BUY` | `8.30` | `15398.5400` | 127,744.75 USD | 3,358,342.02 USD | `LARGE (>= USD 100K)` | `-0.30%` | `0x71d0e11ebb` |
| `BUY` | `8.30` | `1866.9900` | 15,501.43 USD | 4,742,388.18 USD | `STANDARD` | `-0.22%` | `0x57d8e75f47` |
| `BUY` | `8.30` | `1866.9900` | 15,496.95 USD | 4,757,885.13 USD | `STANDARD` | `-0.25%` | `0x57d8e75f47` |
| `BUY` | `8.30` | `1866.9900` | 15,492.47 USD | 4,773,377.60 USD | `STANDARD` | `-0.27%` | `0x57d8e75f47` |
| `BUY` | `8.30` | `1197.9600` | 9,942.59 USD | 5,131,191.12 USD | `STANDARD` | `-0.26%` | `0xaf9f722a67` |
| `BUY` | `8.30` | `774.0600` | 6,422.61 USD | 5,273,528.23 USD | `STANDARD` | `-0.28%` | `0xecb63caa47` |
| `BUY` | `8.30` | `602.6200` | 4,999.94 USD | 5,313,576.55 USD | `STANDARD` | `-0.29%` | `0x0efb38a5fa` |
| `BUY` | `8.30` | `481.6400` | 3,998.38 USD | 5,359,528.70 USD | `STANDARD` | `-0.23%` | `0x7717a7a245` |
| `BUY` | `8.30` | `467.8500` | 3,884.75 USD | 5,390,700.47 USD | `STANDARD` | `-0.21%` | `0x2a72b57dea` |
| `BUY` | `8.30` | `467.8500` | 3,882.31 USD | 5,394,582.79 USD | `STANDARD` | `-0.27%` | `0x2a72b57dea` |
| `BUY` | `8.30` | `460.6300` | 3,824.98 USD | 5,402,285.40 USD | `STANDARD` | `-0.21%` | `0xa38f19c4cc` |
| `BUY` | `8.30` | `366.8200` | 3,043.14 USD | 5,435,773.54 USD | `STANDARD` | `-0.30%` | `0xdd4f66125d` |
| `BUY` | `8.30` | `329.4900` | 2,735.82 USD | 5,441,552.13 USD | `STANDARD` | `-0.21%` | `0xecb63caa47` |
| `BUY` | `8.30` | `288.4500` | 2,394.42 USD | 5,464,633.66 USD | `STANDARD` | `-0.24%` | `0xecb63caa47` |
| `BUY` | `8.30` | `105.1500` | 872.82 USD | 5,539,405.59 USD | `STANDARD` | `-0.24%` | `0xa382fa9f4b` |
| `BUY` | `8.30` | `105.1400` | 872.73 USD | 5,540,278.31 USD | `STANDARD` | `-0.24%` | `0xf30120f048` |
| `BUY` | `8.30` | `83.1400` | 690.02 USD | 5,554,585.21 USD | `STANDARD` | `-0.26%` | `0x31ca8395cf` |
| `BUY` | `8.30` | `81.3700` | 675.34 USD | 5,555,260.55 USD | `STANDARD` | `-0.26%` | `0x010461c14e` |
| `BUY` | `8.31` | `1866.9900` | 15,523.84 USD | 4,680,350.90 USD | `STANDARD` | `-0.07%` | `0x57d8e75f47` |
| `BUY` | `8.31` | `1866.9900` | 15,517.86 USD | 4,695,868.76 USD | `STANDARD` | `-0.11%` | `0x57d8e75f47` |
| `BUY` | `8.31` | `1866.9900` | 15,511.33 USD | 4,711,380.09 USD | `STANDARD` | `-0.15%` | `0x57d8e75f47` |
| `BUY` | `8.31` | `1866.9900` | 15,506.66 USD | 4,726,886.74 USD | `STANDARD` | `-0.18%` | `0x57d8e75f47` |
| `BUY` | `8.31` | `1443.8300` | 11,997.51 USD | 5,017,538.67 USD | `STANDARD` | `-0.14%` | `0x7d0c59691f` |
| `BUY` | `8.31` | `1245.4400` | 10,353.72 USD | 5,071,112.79 USD | `STANDARD` | `-0.09%` | `0x621c555167` |
| `BUY` | `8.31` | `1202.9200` | 9,999.63 USD | 5,091,321.34 USD | `STANDARD` | `-0.10%` | `0x7d0c59691f` |
| `BUY` | `8.31` | `1197.9600` | 9,952.53 USD | 5,121,248.53 USD | `STANDARD` | `-0.16%` | `0xaf9f722a67` |
| `BUY` | `8.31` | `962.1300` | 7,999.53 USD | 5,208,162.85 USD | `STANDARD` | `-0.08%` | `0x7d0c59691f` |
| `BUY` | `8.31` | `505.4800` | 4,199.22 USD | 5,326,979.85 USD | `STANDARD` | `-0.16%` | `0x71d0e11ebb` |
| `BUY` | `8.31` | `467.8500` | 3,889.42 USD | 5,382,928.64 USD | `STANDARD` | `-0.09%` | `0x2a72b57dea` |
| `BUY` | `8.31` | `467.8500` | 3,887.08 USD | 5,386,815.73 USD | `STANDARD` | `-0.15%` | `0x2a72b57dea` |
| `BUY` | `8.31` | `445.7400` | 3,702.63 USD | 5,413,542.71 USD | `STANDARD` | `-0.17%` | `0xecb63caa47` |
| `BUY` | `8.31` | `366.8200` | 3,046.59 USD | 5,432,730.40 USD | `STANDARD` | `-0.19%` | `0xdd4f66125d` |
| `BUY` | `8.31` | `312.0500` | 2,592.95 USD | 5,454,660.75 USD | `STANDARD` | `-0.14%` | `0x7717a7a245` |
| `BUY` | `8.31` | `300.7400` | 2,499.96 USD | 5,459,739.28 USD | `STANDARD` | `-0.10%` | `0x0efb38a5fa` |
| `BUY` | `8.31` | `270.8900` | 2,249.96 USD | 5,469,133.62 USD | `STANDARD` | `-0.18%` | `0xa38f19c4cc` |
| `BUY` | `8.31` | `136.6600` | 1,136.30 USD | 5,504,084.95 USD | `STANDARD` | `-0.07%` | `0xecb63caa47` |
| `BUY` | `8.31` | `120.2100` | 998.63 USD | 5,511,266.66 USD | `STANDARD` | `-0.16%` | `0x83bec364a5` |
| `BUY` | `8.31` | `105.1400` | 874.24 USD | 5,538,532.77 USD | `STANDARD` | `-0.07%` | `0x63f6411ca6` |
| `BUY` | `8.31` | `89.5000` | 743.55 USD | 5,548,199.43 USD | `STANDARD` | `-0.16%` | `0x31ca8395cf` |
| `BUY` | `8.31` | `87.6600` | 728.82 USD | 5,548,928.25 USD | `STANDARD` | `-0.08%` | `0x31ca8395cf` |
| `BUY` | `8.31` | `87.4000` | 726.10 USD | 5,550,382.01 USD | `STANDARD` | `-0.16%` | `0x010461c14e` |
| `BUY` | `8.31` | `75.7800` | 630.05 USD | 5,563,038.70 USD | `STANDARD` | `-0.08%` | `0x010461c14e` |
| `BUY` | `8.31` | `60.3400` | 501.50 USD | 5,566,165.54 USD | `STANDARD` | `-0.12%` | `0x57d8e75f47` |
| `BUY` | `8.31` | `60.3400` | 501.18 USD | 5,566,666.72 USD | `STANDARD` | `-0.18%` | `0x57d8e75f47` |
| `ASK` | `8.32` | `105.1500` | 875.37 USD | 12,603.09 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.32` | `30.0500` | 250.15 USD | 11,727.72 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.32` | `152.7700` | 1,271.70 USD | 11,477.56 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.32` | `50.0000` | 416.21 USD | 10,205.86 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.32` | `165.6200` | 1,378.62 USD | 9,789.65 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.32` | `50.0000` | 416.19 USD | 8,411.03 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.32` | `30.0400` | 250.04 USD | 7,994.83 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.32` | `105.1400` | 875.13 USD | 7,744.79 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.32` | `50.0000` | 416.17 USD | 6,869.66 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.32` | `60.3400` | 502.21 USD | 6,453.49 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.32` | `105.1300` | 874.97 USD | 5,951.28 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.32` | `105.1400` | 875.01 USD | 5,076.31 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.32` | `135.9700` | 1,131.56 USD | 4,201.31 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.32` | `43.9400` | 365.66 USD | 3,069.75 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `8.32` | `105.1400` | 874.93 USD | 2,704.08 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.32` | `17.2600` | 143.63 USD | 1,829.15 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.32` | `52.5600` | 437.37 USD | 1,685.52 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `8.32` | `150.0000` | 1,248.15 USD | 1,248.15 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `8.32` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.32` | `0.00%` | `-` |
| `BID` | `8.32` | `25.0000` | 208.02 USD | 208.02 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `8.32` | `16.0000` | 133.10 USD | 341.12 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.32` | `137.5600` | 1,144.29 USD | 1,485.41 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.32` | `154.2000` | 1,282.70 USD | 2,768.11 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.32` | `155.1500` | 1,290.57 USD | 4,058.68 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.32` | `721.2800` | 5,999.68 USD | 10,058.36 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.32` | `105.1400` | 874.55 USD | 10,932.91 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.32` | `137.5600` | 1,144.20 USD | 12,077.11 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.32` | `105.1400` | 874.48 USD | 12,951.59 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.32` | `50.0000` | 415.86 USD | 13,367.44 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.32` | `45.7600` | 380.59 USD | 13,748.03 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.32` | `50.0000` | 415.84 USD | 14,163.87 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.32` | `206.8100` | 1,719.96 USD | 15,883.82 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.32` | `50.0000` | 415.82 USD | 16,299.64 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.32` | `961.9500` | 7,999.86 USD | 24,299.51 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.32` | `257.6400` | 2,142.59 USD | 26,442.09 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `8.32` | `30.0500` | 249.90 USD | 26,691.99 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.32` | `105.1400` | 874.33 USD | 27,566.32 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.32` | `5.6200` | 46.73 USD | 27,613.06 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.32` | `105.1400` | 874.26 USD | 28,487.32 USD | `1 orders` | `-0.07%` | `-` |
| `BUY` | `8.32` | `721.3700` | 5,999.92 USD | 5,298,550.94 USD | `STANDARD` | `-0.04%` | `0x7d0c59691f` |
| `SELL` | `8.32` | `152.9000` | 1,272.27 USD | 5,498,246.87 USD | `STANDARD` | `+0.00%` | `0x727956612a` |
| `BUY` | `8.32` | `141.2800` | 1,175.07 USD | 5,500,659.14 USD | `STANDARD` | `-0.04%` | `0x727956612a` |
| `BUY` | `8.32` | `137.5600` | 1,143.98 USD | 5,502,948.65 USD | `STANDARD` | `-0.06%` | `0xdd4f66125d` |
| `SELL` | `8.32` | `120.1300` | 999.93 USD | 5,507,268.99 USD | `STANDARD` | `+0.03%` | `0x0eecd62efb` |
| `SELL` | `8.32` | `120.0800` | 999.44 USD | 5,510,268.03 USD | `STANDARD` | `+0.03%` | `0x7717a7a245` |
| `BUY` | `8.32` | `120.0800` | 998.61 USD | 5,512,265.27 USD | `STANDARD` | `-0.06%` | `0x7717a7a245` |
| `SELL` | `8.32` | `105.1500` | 875.37 USD | 5,529,784.91 USD | `STANDARD` | `+0.05%` | `0xfd66e33095` |
| `SELL` | `8.32` | `105.1400` | 875.13 USD | 5,531,535.37 USD | `STANDARD` | `+0.03%` | `0xa382fa9f4b` |
| `SELL` | `8.32` | `105.1400` | 875.01 USD | 5,532,410.38 USD | `STANDARD` | `+0.02%` | `0xd0956a1eba` |
| `SELL` | `8.32` | `105.1300` | 874.97 USD | 5,533,285.35 USD | `STANDARD` | `+0.02%` | `0xf30120f048` |
| `SELL` | `8.32` | `105.1400` | 874.93 USD | 5,534,160.28 USD | `STANDARD` | `+0.01%` | `0x9d81a3adf8` |
| `SELL` | `8.32` | `105.1400` | 874.86 USD | 5,535,035.14 USD | `STANDARD` | `+0.00%` | `0x9d81a3adf8` |
| `SELL` | `8.32` | `105.1400` | 874.86 USD | 5,535,910.00 USD | `STANDARD` | `+0.00%` | `0x63f6411ca6` |
| `BUY` | `8.32` | `105.1400` | 874.27 USD | 5,536,784.27 USD | `STANDARD` | `-0.07%` | `0xea0e878d5d` |
| `BUY` | `8.32` | `105.1400` | 874.26 USD | 5,537,658.53 USD | `STANDARD` | `-0.07%` | `0x53136b4a7c` |
| `SELL` | `8.32` | `104.1500` | 866.63 USD | 5,542,884.44 USD | `STANDARD` | `+0.00%` | `0xecb63caa47` |
| `SELL` | `8.32` | `83.9800` | 699.05 USD | 5,552,508.21 USD | `STANDARD` | `+0.04%` | `0x010461c14e` |
| `SELL` | `8.32` | `78.8600` | 656.45 USD | 5,557,907.96 USD | `STANDARD` | `+0.04%` | `0xa382fa9f4b` |
| `SELL` | `8.32` | `78.3100` | 651.77 USD | 5,559,215.57 USD | `STANDARD` | `+0.03%` | `0x010461c14e` |
| `SELL` | `8.32` | `76.8400` | 639.54 USD | 5,560,503.21 USD | `STANDARD` | `+0.03%` | `0x31ca8395cf` |
| `SELL` | `8.32` | `73.9100` | 615.25 USD | 5,563,653.95 USD | `STANDARD` | `+0.04%` | `0x2eddf3aa5c` |
| `SELL` | `8.32` | `60.3400` | 502.21 USD | 5,565,664.04 USD | `STANDARD` | `+0.03%` | `0x57d8e75f47` |
| `ASK` | `8.33` | `6.2200` | 51.78 USD | 14,366.35 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.33` | `205.5800` | 1,711.47 USD | 14,314.56 USD | `2 orders` | `+0.05%` | `-` |
| `SELL` | `8.33` | `1866.9900` | 15,558.75 USD | 4,633,728.98 USD | `STANDARD` | `+0.15%` | `0x57d8e75f47` |
| `SELL` | `8.33` | `1866.9900` | 15,551.47 USD | 4,649,280.45 USD | `STANDARD` | `+0.11%` | `0x57d8e75f47` |
| `SELL` | `8.33` | `1866.9900` | 15,546.61 USD | 4,664,827.06 USD | `STANDARD` | `+0.07%` | `0x57d8e75f47` |
| `SELL` | `8.33` | `1245.4400` | 10,377.63 USD | 5,060,759.07 USD | `STANDARD` | `+0.14%` | `0x621c555167` |
| `SELL` | `8.33` | `1197.9600` | 9,982.36 USD | 5,111,296.00 USD | `STANDARD` | `+0.14%` | `0xaf9f722a67` |
| `SELL` | `8.33` | `780.2200` | 6,502.43 USD | 5,267,105.62 USD | `STANDARD` | `+0.16%` | `0xa38f19c4cc` |
| `SELL` | `8.33` | `505.4600` | 4,210.43 USD | 5,322,780.63 USD | `STANDARD` | `+0.11%` | `0x71d0e11ebb` |
| `SELL` | `8.33` | `467.8500` | 3,898.87 USD | 5,375,143.34 USD | `STANDARD` | `+0.15%` | `0x2a72b57dea` |
| `SELL` | `8.33` | `467.8500` | 3,895.88 USD | 5,379,039.22 USD | `STANDARD` | `+0.08%` | `0x2a72b57dea` |
| `SELL` | `8.33` | `447.7600` | 3,729.71 USD | 5,409,840.08 USD | `STANDARD` | `+0.11%` | `0xecb63caa47` |
| `SELL` | `8.33` | `391.6800` | 3,264.18 USD | 5,420,505.10 USD | `STANDARD` | `+0.16%` | `0xecb63caa47` |
| `SELL` | `8.33` | `312.0500` | 2,599.69 USD | 5,449,471.24 USD | `STANDARD` | `+0.12%` | `0x7717a7a245` |
| `SELL` | `8.33` | `300.1400` | 2,499.96 USD | 5,462,239.24 USD | `STANDARD` | `+0.10%` | `0x0efb38a5fa` |
| `SELL` | `8.33` | `270.1500` | 2,250.00 USD | 5,466,883.66 USD | `STANDARD` | `+0.09%` | `0xa38f19c4cc` |
| `SELL` | `8.33` | `198.3300` | 1,652.82 USD | 5,489,107.57 USD | `STANDARD` | `+0.15%` | `0xfdba13d24c` |
| `SELL` | `8.33` | `137.5600` | 1,145.53 USD | 5,501,804.67 USD | `STANDARD` | `+0.08%` | `0xdd4f66125d` |
| `SELL` | `8.33` | `133.1500` | 1,108.91 USD | 5,505,193.86 USD | `STANDARD` | `+0.09%` | `0x2eddf3aa5c` |
| `SELL` | `8.33` | `129.1400` | 1,075.21 USD | 5,506,269.07 USD | `STANDARD` | `+0.06%` | `0x2eddf3aa5c` |
| `SELL` | `8.33` | `120.0800` | 999.92 USD | 5,508,268.91 USD | `STANDARD` | `+0.07%` | `0x27c9fa86c9` |
| `SELL` | `8.33` | `120.0800` | 999.68 USD | 5,509,268.59 USD | `STANDARD` | `+0.05%` | `0x7717a7a245` |
| `SELL` | `8.33` | `105.1400` | 876.18 USD | 5,518,401.35 USD | `STANDARD` | `+0.15%` | `0xd0956a1eba` |
| `SELL` | `8.33` | `105.1400` | 876.04 USD | 5,519,277.39 USD | `STANDARD` | `+0.13%` | `0xf30120f048` |
| `SELL` | `8.33` | `105.1300` | 875.99 USD | 5,520,153.38 USD | `STANDARD` | `+0.14%` | `0xa382fa9f4b` |
| `SELL` | `8.33` | `105.1400` | 875.89 USD | 5,521,029.27 USD | `STANDARD` | `+0.12%` | `0x9d81a3adf8` |
| `SELL` | `8.33` | `105.1300` | 875.85 USD | 5,521,905.11 USD | `STANDARD` | `+0.12%` | `0xf30120f048` |
| `SELL` | `8.33` | `105.1400` | 875.75 USD | 5,522,780.87 USD | `STANDARD` | `+0.10%` | `0xa382fa9f4b` |
| `SELL` | `8.33` | `105.1400` | 875.73 USD | 5,523,656.60 USD | `STANDARD` | `+0.10%` | `0x9d81a3adf8` |
| `SELL` | `8.33` | `105.1400` | 875.67 USD | 5,524,532.27 USD | `STANDARD` | `+0.09%` | `0xa382fa9f4b` |
| `SELL` | `8.33` | `105.1400` | 875.53 USD | 5,525,407.80 USD | `STANDARD` | `+0.08%` | `0x9d81a3adf8` |
| `SELL` | `8.33` | `105.1500` | 875.47 USD | 5,526,283.27 USD | `STANDARD` | `+0.06%` | `0xd0956a1eba` |
| `SELL` | `8.33` | `105.1400` | 875.46 USD | 5,527,158.73 USD | `STANDARD` | `+0.07%` | `0xf30120f048` |
| `SELL` | `8.33` | `105.1000` | 875.43 USD | 5,528,034.16 USD | `STANDARD` | `+0.10%` | `0x53136b4a7c` |
| `SELL` | `8.33` | `105.1400` | 875.37 USD | 5,528,909.53 USD | `STANDARD` | `+0.06%` | `0x9d81a3adf8` |
| `SELL` | `8.33` | `105.1100` | 875.34 USD | 5,530,660.24 USD | `STANDARD` | `+0.08%` | `0x53136b4a7c` |
| `SELL` | `8.33` | `91.7000` | 764.15 USD | 5,543,648.59 USD | `STANDARD` | `+0.15%` | `0xdd4f66125d` |
| `SELL` | `8.33` | `91.7000` | 764.05 USD | 5,544,412.64 USD | `STANDARD` | `+0.13%` | `0xdd4f66125d` |
| `SELL` | `8.33` | `91.7000` | 763.92 USD | 5,545,176.56 USD | `STANDARD` | `+0.12%` | `0xdd4f66125d` |
| `SELL` | `8.33` | `91.6900` | 763.92 USD | 5,545,940.47 USD | `STANDARD` | `+0.13%` | `0x010461c14e` |
| `SELL` | `8.33` | `91.5200` | 762.29 USD | 5,546,702.76 USD | `STANDARD` | `+0.10%` | `0x31ca8395cf` |
| `SELL` | `8.33` | `90.4200` | 753.12 USD | 5,547,455.88 USD | `STANDARD` | `+0.10%` | `0x010461c14e` |
| `SELL` | `8.33` | `85.8500` | 715.35 USD | 5,551,097.36 USD | `STANDARD` | `+0.14%` | `0x2eddf3aa5c` |
| `SELL` | `8.33` | `85.5000` | 711.80 USD | 5,551,809.16 USD | `STANDARD` | `+0.05%` | `0x2eddf3aa5c` |
| `SELL` | `8.33` | `60.3400` | 502.84 USD | 5,564,156.79 USD | `STANDARD` | `+0.15%` | `0x57d8e75f47` |
| `SELL` | `8.33` | `60.3400` | 502.63 USD | 5,564,659.42 USD | `STANDARD` | `+0.11%` | `0x57d8e75f47` |
| `SELL` | `8.33` | `60.3400` | 502.41 USD | 5,565,161.83 USD | `STANDARD` | `+0.07%` | `0x57d8e75f47` |
| `SELL` | `8.34` | `15399.5700` | 128,435.49 USD | 3,102,788.71 USD | `LARGE (>= USD 100K)` | `+0.23%` | `0x71d0e11ebb` |
| `SELL` | `8.34` | `1866.9900` | 15,579.10 USD | 4,571,463.19 USD | `STANDARD` | `+0.28%` | `0x57d8e75f47` |
| `SELL` | `8.34` | `1866.9900` | 15,573.87 USD | 4,587,037.06 USD | `STANDARD` | `+0.25%` | `0x57d8e75f47` |
| `SELL` | `8.34` | `1866.9900` | 15,569.39 USD | 4,602,606.45 USD | `STANDARD` | `+0.22%` | `0x57d8e75f47` |
| `SELL` | `8.34` | `1866.9900` | 15,563.79 USD | 4,618,170.24 USD | `STANDARD` | `+0.19%` | `0x57d8e75f47` |
| `SELL` | `8.34` | `1324.9500` | 11,054.19 USD | 5,039,647.05 USD | `STANDARD` | `+0.27%` | `0xa38f19c4cc` |
| `SELL` | `8.34` | `1197.9600` | 9,992.30 USD | 5,101,313.64 USD | `STANDARD` | `+0.24%` | `0xaf9f722a67` |
| `SELL` | `8.34` | `901.9300` | 7,522.28 USD | 5,247,211.74 USD | `STANDARD` | `+0.23%` | `0xecb63caa47` |
| `SELL` | `8.34` | `599.3100` | 4,999.98 USD | 5,308,576.61 USD | `STANDARD` | `+0.26%` | `0x0efb38a5fa` |
| `SELL` | `8.34` | `598.4500` | 4,993.65 USD | 5,318,570.19 USD | `STANDARD` | `+0.28%` | `0xecb63caa47` |
| `SELL` | `8.34` | `481.6400` | 4,015.72 USD | 5,355,530.32 USD | `STANDARD` | `+0.20%` | `0x7717a7a245` |
| `SELL` | `8.34` | `467.8500` | 3,901.26 USD | 5,371,244.46 USD | `STANDARD` | `+0.21%` | `0x2a72b57dea` |
| `SELL` | `8.34` | `458.9000` | 3,824.98 USD | 5,406,110.38 USD | `STANDARD` | `+0.17%` | `0xa38f19c4cc` |
| `SELL` | `8.34` | `366.8200` | 3,058.47 USD | 5,426,625.75 USD | `STANDARD` | `+0.20%` | `0xdd4f66125d` |
| `SELL` | `8.34` | `366.8200` | 3,058.07 USD | 5,429,683.81 USD | `STANDARD` | `+0.19%` | `0xdd4f66125d` |
| `SELL` | `8.34` | `261.2800` | 2,178.03 USD | 5,471,311.65 USD | `STANDARD` | `+0.18%` | `0xecb63caa47` |
| `SELL` | `8.34` | `254.6000` | 2,123.44 USD | 5,473,435.09 USD | `STANDARD` | `+0.23%` | `0xecb63caa47` |
| `SELL` | `8.34` | `105.1500` | 876.87 USD | 5,513,142.14 USD | `STANDARD` | `+0.22%` | `0xfd66e33095` |
| `SELL` | `8.34` | `105.1500` | 876.78 USD | 5,514,018.92 USD | `STANDARD` | `+0.21%` | `0xa382fa9f4b` |
| `SELL` | `8.34` | `105.1400` | 876.77 USD | 5,514,895.69 USD | `STANDARD` | `+0.22%` | `0x53136b4a7c` |
| `SELL` | `8.34` | `105.1400` | 876.60 USD | 5,515,772.30 USD | `STANDARD` | `+0.20%` | `0xd0956a1eba` |
| `SELL` | `8.34` | `105.1400` | 876.47 USD | 5,516,648.76 USD | `STANDARD` | `+0.18%` | `0xfd66e33095` |
| `SELL` | `8.34` | `105.1400` | 876.40 USD | 5,517,525.17 USD | `STANDARD` | `+0.18%` | `0x53136b4a7c` |
| `SELL` | `8.34` | `83.2100` | 694.18 USD | 5,553,202.39 USD | `STANDARD` | `+0.26%` | `0x010461c14e` |
| `SELL` | `8.34` | `77.7200` | 648.10 USD | 5,559,863.67 USD | `STANDARD` | `+0.22%` | `0x31ca8395cf` |
| `SELL` | `8.34` | `75.8700` | 632.60 USD | 5,562,408.65 USD | `STANDARD` | `+0.20%` | `0x010461c14e` |
| `SELL` | `8.35` | `1866.9900` | 15,597.95 USD | 4,509,118.60 USD | `STANDARD` | `+0.41%` | `0x57d8e75f47` |
| `SELL` | `8.35` | `1866.9900` | 15,593.29 USD | 4,524,711.89 USD | `STANDARD` | `+0.37%` | `0x57d8e75f47` |
| `SELL` | `8.35` | `1866.9900` | 15,588.43 USD | 4,540,300.32 USD | `STANDARD` | `+0.34%` | `0x57d8e75f47` |
| `SELL` | `8.35` | `1866.9900` | 15,583.77 USD | 4,555,884.09 USD | `STANDARD` | `+0.31%` | `0x57d8e75f47` |
| `SELL` | `8.35` | `1084.3700` | 9,058.18 USD | 5,140,249.30 USD | `STANDARD` | `+0.39%` | `0xd3342d3b1e` |
| `SELL` | `8.35` | `1005.0800` | 8,397.34 USD | 5,184,163.41 USD | `STANDARD` | `+0.41%` | `0xd3943e4008` |
| `SELL` | `8.35` | `941.1700` | 7,860.56 USD | 5,231,871.87 USD | `STANDARD` | `+0.37%` | `0xecb63caa47` |
| `SELL` | `8.35` | `755.5800` | 6,309.17 USD | 5,292,551.02 USD | `STANDARD` | `+0.35%` | `0xecb63caa47` |
| `SELL` | `8.35` | `467.8500` | 3,908.56 USD | 5,363,437.26 USD | `STANDARD` | `+0.40%` | `0x2a72b57dea` |
| `SELL` | `8.35` | `467.8500` | 3,905.94 USD | 5,367,343.20 USD | `STANDARD` | `+0.33%` | `0x2a72b57dea` |
| `SELL` | `8.35` | `366.8200` | 3,062.18 USD | 5,423,567.27 USD | `STANDARD` | `+0.32%` | `0xdd4f66125d` |
| `SELL` | `8.35` | `80.2100` | 670.07 USD | 5,555,930.62 USD | `STANDARD` | `+0.40%` | `0x010461c14e` |
| `SELL` | `8.36` | `2248.0600` | 18,792.21 USD | 4,394,262.42 USD | `STANDARD` | `+0.46%` | `0xa38f19c4cc` |
| `SELL` | `8.36` | `1866.9900` | 15,612.14 USD | 4,477,917.65 USD | `STANDARD` | `+0.50%` | `0x57d8e75f47` |
| `SELL` | `8.36` | `1866.9900` | 15,603.00 USD | 4,493,520.65 USD | `STANDARD` | `+0.44%` | `0x57d8e75f47` |
| `SELL` | `8.36` | `1056.9300` | 8,835.62 USD | 5,167,076.90 USD | `STANDARD` | `+0.47%` | `0xd3943e4008` |
| `SELL` | `8.36` | `957.1000` | 7,999.92 USD | 5,200,163.32 USD | `STANDARD` | `+0.45%` | `0x0efb38a5fa` |
| `SELL` | `8.36` | `760.6100` | 6,356.80 USD | 5,286,241.85 USD | `STANDARD` | `+0.44%` | `0x47a4471457` |
| `SELL` | `8.36` | `600.9000` | 5,025.69 USD | 5,303,576.63 USD | `STANDARD` | `+0.51%` | `0x3ca146d269` |
| `SELL` | `8.36` | `487.0900` | 4,072.56 USD | 5,347,487.34 USD | `STANDARD` | `+0.48%` | `0xcd7f60e943` |
| `SELL` | `8.36` | `79.1400` | 661.61 USD | 5,556,592.23 USD | `STANDARD` | `+0.47%` | `0x31ca8395cf` |
| `SELL` | `8.37` | `20053.2100` | 167,801.25 USD | 2,089,964.89 USD | `LARGE (>= USD 100K)` | `+0.56%` | `0x71cfa5e263` |
| `SELL` | `8.37` | `15400.7400` | 128,925.75 USD | 2,974,353.21 USD | `LARGE (>= USD 100K)` | `+0.61%` | `0x71d0e11ebb` |
| `SELL` | `8.37` | `1282.7900` | 10,734.39 USD | 5,050,381.44 USD | `STANDARD` | `+0.57%` | `0xd3943e4008` |
| `SELL` | `8.37` | `240.7000` | 2,013.50 USD | 5,485,748.53 USD | `STANDARD` | `+0.53%` | `0x39bac00809` |
| `SELL` | `8.38` | `1535.9900` | 12,867.30 USD | 4,969,202.45 USD | `STANDARD` | `+0.68%` | `0xd3943e4008` |
| `SELL` | `8.38` | `1431.8200` | 11,999.94 USD | 5,005,541.17 USD | `STANDARD` | `+0.72%` | `0x0efb38a5fa` |
| `SELL` | `8.39` | `17729.0700` | 148,784.13 USD | 2,554,140.32 USD | `LARGE (>= USD 100K)` | `+0.86%` | `0x71d0e11ebb` |
| `SELL` | `8.39` | `11937.4500` | 100,192.21 USD | 3,819,755.10 USD | `LARGE (>= USD 100K)` | `+0.87%` | `0x881cd92459` |
| `SELL` | `8.39` | `315.7300` | 2,650.55 USD | 5,446,871.55 USD | `STANDARD` | `+0.89%` | `0x07fd993f0f` |
| `SELL` | `8.39` | `82.5800` | 692.80 USD | 5,553,895.19 USD | `STANDARD` | `+0.82%` | `0x010461c14e` |
| `SELL` | `8.39` | `78.6000` | 659.27 USD | 5,557,251.50 USD | `STANDARD` | `+0.80%` | `0x31ca8395cf` |
| `SELL` | `8.40` | `1679.0300` | 14,105.70 USD | 4,956,335.15 USD | `STANDARD` | `+0.96%` | `0xd3943e4008` |
| `SELL` | `8.41` | `39295.5300` | 330,660.10 USD | 1,598,659.00 USD | `LARGE (>= USD 100K)` | `+1.13%` | `0x71cfa5e263` |
| `SELL` | `8.42` | `7699.4100` | 64,836.73 USD | 4,130,565.96 USD | `MEDIUM (>= USD 25K)` | `+1.20%` | `0x71d0e11ebb` |
| `SELL` | `8.42` | `1900.5900` | 15,999.93 USD | 4,462,305.51 USD | `STANDARD` | `+1.17%` | `0x0efb38a5fa` |
| `SELL` | `8.43` | `9316.6000` | 78,519.37 USD | 3,998,463.02 USD | `MEDIUM (>= USD 25K)` | `+1.29%` | `0xecb63caa47` |
| `SELL` | `8.43` | `4802.6400` | 40,463.20 USD | 4,234,317.24 USD | `MEDIUM (>= USD 25K)` | `+1.25%` | `0xa24c5ca26c` |
| `SELL` | `8.44` | `17715.3400` | 149,494.44 USD | 2,405,356.19 USD | `LARGE (>= USD 100K)` | `+1.42%` | `0x71d0e11ebb` |
| `SELL` | `8.44` | `2250.3000` | 18,999.96 USD | 4,337,678.06 USD | `STANDARD` | `+1.47%` | `0x0efb38a5fa` |
| `SELL` | `8.44` | `2111.3800` | 17,829.34 USD | 4,430,305.64 USD | `STANDARD` | `+1.48%` | `0xd3943e4008` |
| `SELL` | `8.44` | `190.3200` | 1,606.64 USD | 5,492,361.82 USD | `STANDARD` | `+1.45%` | `0x31ca8395cf` |
| `SELL` | `8.44` | `189.6000` | 1,600.32 USD | 5,493,962.14 USD | `STANDARD` | `+1.44%` | `0x010461c14e` |
| `SELL` | `8.45` | `315.7300` | 2,668.87 USD | 5,444,221.00 USD | `STANDARD` | `+1.59%` | `0x07fd993f0f` |
| `SELL` | `8.47` | `76292.3800` | 646,570.29 USD | 646,570.29 USD | `LARGE (>= USD 100K)` | `+1.85%` | `0x71cfa5e263` |
| `SELL` | `8.48` | `185.0800` | 1,569.89 USD | 5,495,532.02 USD | `STANDARD` | `+1.94%` | `0x010461c14e` |
| `SELL` | `8.48` | `170.1100` | 1,442.58 USD | 5,496,974.61 USD | `STANDARD` | `+1.92%` | `0x31ca8395cf` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:26:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1492` | `0x7737...bf66` | `SHORT` | 1,428,458.51 USD | `171,568.06` | `7.43` | `8.31` | `104.31` | -152,913.49 USD | `-10.70%` | `10X Cross` |
| `1575` | `0xeadc...9d55` | `LONG` | 1,330,282.40 USD | `160,070.56` | `8.11` | `8.31` | `0.000000` | 32,644.82 USD | `+2.45%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `9.01` | 13,483.75 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 13.48K USD at 9.0123 USD [API] | `2026-10-28 22:45:26` |
| `ANNOUNCEMENT` | `INFO` | `8.89` | 5,999.48 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 6.00K USD at 8.8930 USD [API] | `2026-10-29 01:10:17` |
| `ANNOUNCEMENT` | `INFO` | `8.91` | 5,999.75 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 6.00K USD at 8.9103 USD [API] | `2026-10-29 01:20:09` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`9.10` (Vol: 233,400.00 USD, Dist: `+9.16%`) | Long MP=`8.23` (Vol: 195,200.00 USD, Dist: `--1.32%`)
  * 48H Horizon: Short MP=`9.10` (Vol: 233,400.00 USD, Dist: `+9.18%`) | Long MP=`8.23` (Vol: 195,200.00 USD, Dist: `--1.31%`)
  * 3D Horizon: Short MP=`9.22` (Vol: 251,900.00 USD, Dist: `+10.66%`) | Long MP=`8.23` (Vol: 195,200.00 USD, Dist: `--1.31%`)
  * 7D Horizon: Short MP=`9.28` (Vol: 426,900.00 USD, Dist: `+11.36%`) | Long MP=`8.22` (Vol: 195,200.00 USD, Dist: `--1.36%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.71` | 802.75 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.99` | 228.27 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 159.60 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 224.39 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 1,450.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 265.08 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 284.29 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 275.43 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 285.78 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 131.67 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 942.44 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 676.25 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 848.24 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 196.35 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 351.33 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 162.51 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 174.46 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 23,920.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 26,390.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 392.22 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 414.26 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 692.51 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 1,460.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 1,350.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.77` | 4,850.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.79` | 3,790.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.83` | 1,450.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.96` | 186.12 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.09` | 147.34 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 159.29 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.20` | 194.10 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.29` | 697.77 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 599.72 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.54` | 3,030.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.58` | 2,290.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 486.93 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 2,930.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,530.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,040.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.72` | 440.94 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 3,880.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 17,380.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 19,690.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 4,430.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 269.53 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 175.17 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 167.78 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 314.59 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 318.46 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.09` | 651.75 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 1,020.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.20` | 480.07 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 300.91 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 1,050.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.26` | 2,230.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 1,410.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 228.06 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 5,830.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 839.65 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.34` | 162,680.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 1,180.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.41` | 918.53 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 20,160.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 2,200.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.51` | 367.41 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 121.38 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 2,760.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.59` | 34,430.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 468.55 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.67` | 11,350.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 147.33 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.72` | 2,390.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 238.86 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 902.40 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 635.31 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 580.50 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 243.07 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.83` | 145.88 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.86` | 2,110.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 984.70 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.92` | 277.35 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 1,610.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.99` | 243.05 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 331.68 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 105.61 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 405.14 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,130.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 1,140.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.13` | 2,030.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 7,810.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 6,510.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 3,020.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 972.65 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.29` | 2,430.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.32` | 277.04 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 6,410.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 484.64 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.50` | 257.99 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.51` | 651.50 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 852.03 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 3,250.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.59` | 1,100.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 364.90 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.63` | 245.89 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.67` | 1,320.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.70` | 1,200.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 16,070.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 6,180.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.72` | 428.72 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 6,780.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 401,940.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 4,720.00 USD | 693,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 688,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 7,230.00 USD | 687,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 446.83 USD | 680,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 1,560.00 USD | 679,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.84` | 204.12 USD | 678,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 677,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 1,580.00 USD | 674,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.93` | 3,500.00 USD | 672,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,980.00 USD | 669,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 3,480.00 USD | 665,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 972.59 USD | 662,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.97` | 128,810.00 USD | 661,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.99` | 297.49 USD | 532,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 746.58 USD | 531,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 20,860.00 USD | 531,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.03` | 1,370.00 USD | 510,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 354.23 USD | 508,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.07` | 24,310.00 USD | 508,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 484,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 644.88 USD | 477,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 29,350.00 USD | 476,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 447,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 777.50 USD | 447,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,270.00 USD | 446,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.17` | 9,550.00 USD | 426,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 4,570.00 USD | 416,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 322.94 USD | 412,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.24` | 1,480.00 USD | 411,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 410,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 21,280.00 USD | 410,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 65,980.00 USD | 388,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 1,680.00 USD | 322,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 4,370.00 USD | 321,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.36` | 3,590,000.00 USD | 3,590,000.00 USD | 6,810.00 USD | 2,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.37` | 2,940.00 USD | 316,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 1,100.00 USD | 313,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.39` | 1,480.00 USD | 312,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.40` | 3,580,000.00 USD | 3,580,000.00 USD | 6,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.42` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 48.44 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 147.61 USD | 311,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 2,430.00 USD | 311,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.44` | 3,230,000.00 USD | 3,230,000.00 USD | 196.00 USD | 0.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.44` | 3,570,000.00 USD | 3,570,000.00 USD | 331.70 USD | 1,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.45` | 13,520.00 USD | 308,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 10,390.00 USD | 295,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.46` | 3,210,000.00 USD | 3,210,000.00 USD | 7,860.00 USD | 0.00 USD | 52,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.46` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 1,410.00 USD | 24,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 284,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 1,120.00 USD | 280,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.48` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.48` | 3,540,000.00 USD | 3,540,000.00 USD | 9,120.00 USD | 0.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 962.81 USD | 279,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.50` | 3,130,000.00 USD | 3,130,000.00 USD | 717.40 USD | 4,920.00 USD | 24,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 421.78 USD | 278,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.51` | 1,710.00 USD | 277,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.52` | 3,110,000.00 USD | 3,110,000.00 USD | 26,110.00 USD | 9,580.00 USD | 36,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.52` | 3,520,000.00 USD | 3,520,000.00 USD | 1,150.00 USD | 14,470.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.53` | 1,570.00 USD | 275,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 274,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.54` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 4,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.55` | 572.67 USD | 270,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.56` | 3,030,000.00 USD | 3,030,000.00 USD | 15,020.00 USD | 4,270.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.56` | 3,480,000.00 USD | 3,480,000.00 USD | 19,530.00 USD | 4,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.57` | 25,060.00 USD | 269,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 1,180.00 USD | 244,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.58` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 147.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.59` | 24,760.00 USD | 243,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.60` | 3,010,000.00 USD | 3,010,000.00 USD | 405.20 USD | 3,770.00 USD | 194.10 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.61` | 2,660.00 USD | 218,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 754.04 USD | 215,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 3,010,000.00 USD | 3,010,000.00 USD | 583.80 USD | 0.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 215,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 214,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 2,990,000.00 USD | 2,990,000.00 USD | 17,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.64` | 3,450,000.00 USD | 3,450,000.00 USD | 812.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.64` | 1,890.00 USD | 214,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 212,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.66` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 9,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.66` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 23,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 256.09 USD | 211,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.67` | 6,780.00 USD | 211,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.68` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.68` | 739.30 USD | 204,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.70` | 3,250.00 USD | 204,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 2,970,000.00 USD | 2,970,000.00 USD | 321.75 USD | 2,390.00 USD | 14,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.72` | 2,950,000.00 USD | 2,950,000.00 USD | 4,600.00 USD | 1,630.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.72` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.74` | 2,930,000.00 USD | 2,930,000.00 USD | 3,340.00 USD | 4,580.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.74` | 3,390,000.00 USD | 3,390,000.00 USD | 976.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 500.12 USD | 200,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.76` | 2,920,000.00 USD | 2,920,000.00 USD | 1,660.00 USD | 1,100.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.76` | 3,390,000.00 USD | 3,390,000.00 USD | 812.95 USD | 5,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 200,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.78` | 8,670.00 USD | 199,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 2,910,000.00 USD | 2,910,000.00 USD | 44,950.00 USD | 3,730.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.78` | 3,380,000.00 USD | 3,380,000.00 USD | 43,620.00 USD | 4,900.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 2,470.00 USD | 191,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 4,480.00 USD | 188,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 2,850,000.00 USD | 2,850,000.00 USD | 39,070.00 USD | 10,860.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.80` | 3,310,000.00 USD | 3,310,000.00 USD | 14,770.00 USD | 12,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 4,020.00 USD | 184,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.82` | 1,560.00 USD | 180,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.82` | 2,800,000.00 USD | 2,800,000.00 USD | 5,100.00 USD | 7,610.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.82` | 3,280,000.00 USD | 3,280,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.83` | 706.68 USD | 178,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.84` | 2,780,000.00 USD | 2,780,000.00 USD | 2,680.00 USD | 4,910.00 USD | 12,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 3,270,000.00 USD | 3,270,000.00 USD | 30,950.00 USD | 2,380.00 USD | 25,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 24,340.00 USD | 178,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.86` | 2,760,000.00 USD | 2,760,000.00 USD | 15,790.00 USD | 1,680.00 USD | 16,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.86` | 3,210,000.00 USD | 3,210,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 233.83 USD | 153,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 153,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 2,720,000.00 USD | 2,720,000.00 USD | 46,100.00 USD | 9,570.00 USD | 22,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.88` | 3,160,000.00 USD | 3,160,000.00 USD | 58,120.00 USD | 12,780.00 USD | 29,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.89` | 986.88 USD | 152,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.90` | 2,650,000.00 USD | 2,650,000.00 USD | 14,350.00 USD | 7,630.00 USD | 7,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 3,060,000.00 USD | 3,060,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 505.13 USD | 151,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.92` | 2,620,000.00 USD | 2,620,000.00 USD | 24,660.00 USD | 2,950.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.92` | 3,000,000.00 USD | 3,000,000.00 USD | 55,490.00 USD | 8,420.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 4,600.00 USD | 151,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.93` | 16,340.00 USD | 146,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 2,580,000.00 USD | 2,580,000.00 USD | 20,330.00 USD | 6,860.00 USD | 48,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.94` | 2,920,000.00 USD | 2,920,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 130,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 2,510,000.00 USD | 2,510,000.00 USD | 20,670.00 USD | 11,220.00 USD | 149,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.96` | 2,830,000.00 USD | 2,830,000.00 USD | 21,840.00 USD | 6,920.00 USD | 86,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.97` | 1,580.00 USD | 3,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.98` | 2,330,000.00 USD | 2,330,000.00 USD | 17,030.00 USD | 3,300.00 USD | 37,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.98` | 2,710,000.00 USD | 2,710,000.00 USD | 56,660.00 USD | 26,790.00 USD | 146,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,600.00 USD | 1,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.00` | 210.99 USD | 210.99 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 2,270,000.00 USD | 2,270,000.00 USD | 1,500.00 USD | 22,850.00 USD | 62,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.00` | 2,480,000.00 USD | 2,480,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 2,180,000.00 USD | 2,180,000.00 USD | 81,330.00 USD | 10,580.00 USD | 82,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.02` | 2,400,000.00 USD | 2,400,000.00 USD | 20,910.00 USD | 46,670.00 USD | 56,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.04` | 2,010,000.00 USD | 2,010,000.00 USD | 33,700.00 USD | 17,810.00 USD | 15,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.04` | 2,280,000.00 USD | 2,280,000.00 USD | 152,340.00 USD | 56,910.00 USD | 86,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.06` | 1,940,000.00 USD | 1,940,000.00 USD | 76,840.00 USD | 22,300.00 USD | 19,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.06` | 1,980,000.00 USD | 1,980,000.00 USD | 122,100.00 USD | 20,850.00 USD | 86,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.08` | 1,820,000.00 USD | 1,820,000.00 USD | 36,720.00 USD | 6,070.00 USD | 13,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.08` | 1,760,000.00 USD | 1,760,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.10` | 1,770,000.00 USD | 1,770,000.00 USD | 30,110.00 USD | 14,390.00 USD | 96,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.10` | 1,720,000.00 USD | 1,720,000.00 USD | 61,500.00 USD | 19,700.00 USD | 15,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.12` | 1,620,000.00 USD | 1,620,000.00 USD | 110,990.00 USD | 12,270.00 USD | 319,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.12` | 1,620,000.00 USD | 1,620,000.00 USD | 27,520.00 USD | 10,810.00 USD | 142,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 1,180,000.00 USD | 1,180,000.00 USD | 12,410.00 USD | 0.00 USD | 58,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.14` | 1,440,000.00 USD | 1,440,000.00 USD | 72,460.00 USD | 25,370.00 USD | 192,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 1,110,000.00 USD | 1,110,000.00 USD | 44,830.00 USD | 42,030.00 USD | 159,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 1,150,000.00 USD | 1,150,000.00 USD | 38,430.00 USD | 5,510.00 USD | 30,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 864,670.00 USD | 864,670.00 USD | 133,120.00 USD | 19,620.00 USD | 175,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 1,080,000.00 USD | 1,080,000.00 USD | 39,830.00 USD | 43,260.00 USD | 176,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.20` | 535,970.00 USD | 535,970.00 USD | 33,560.00 USD | 32,530.00 USD | 17,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.20` | 817,140.00 USD | 817,140.00 USD | 92,320.00 USD | 58,100.00 USD | 8,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.22` | 452,680.00 USD | 452,680.00 USD | 32,330.00 USD | 39,650.00 USD | 35,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.22` | 658,310.00 USD | 658,310.00 USD | 117,230.00 USD | 21,570.00 USD | 10,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.24` | 345,380.00 USD | 345,380.00 USD | 163,080.00 USD | 10,300.00 USD | 69,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 508,550.00 USD | 508,550.00 USD | 39,950.00 USD | 3,480.00 USD | 107,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.26` | 102,620.00 USD | 102,620.00 USD | 15,150.00 USD | 15,590.00 USD | 16,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.26` | 357,410.00 USD | 357,410.00 USD | 30,490.00 USD | 5,750.00 USD | 1,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.28` | 55,260.00 USD | 55,260.00 USD | 0.00 USD | 0.00 USD | 57.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.28` | 319,300.00 USD | 319,300.00 USD | 122,850.00 USD | 0.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.30` | 195,270.00 USD | 195,270.00 USD | 152,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.32` | 55,210.00 USD | 55,210.00 USD | 55,190.00 USD | 0.00 USD | 16.44 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.32` | 42,900.00 USD | 42,900.00 USD | 42,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.34` | 122.98 USD | 122.98 USD | 0.00 USD | 0.00 USD | 122.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.34` | 245.96 USD | 245.96 USD | 0.00 USD | 0.00 USD | 122.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.36` | 263.76 USD | 263.76 USD | 0.00 USD | 0.00 USD | 17.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.36` | 14,290.00 USD | 14,290.00 USD | 0.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.38` | 1,020.00 USD | 1,020.00 USD | 691.75 USD | 0.00 USD | 64.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.38` | 73,260.00 USD | 73,260.00 USD | 0.00 USD | 0.00 USD | 58,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.40` | 108,990.00 USD | 108,990.00 USD | 0.00 USD | 0.00 USD | 35,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.42` | 1,810.00 USD | 1,810.00 USD | 788.46 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.42` | 128,030.00 USD | 128,030.00 USD | 16,070.00 USD | 0.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.44` | 91,790.00 USD | 91,790.00 USD | 0.00 USD | 0.00 USD | 89,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.44` | 138,510.00 USD | 138,510.00 USD | 10,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.46` | 419,730.00 USD | 419,730.00 USD | 35,680.00 USD | 4,700.00 USD | 287,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.46` | 623,300.00 USD | 623,300.00 USD | 365,050.00 USD | 0.00 USD | 119,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.48` | 517,470.00 USD | 517,470.00 USD | 0.00 USD | 39,180.00 USD | 58,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.48` | 825,140.00 USD | 825,140.00 USD | 0.00 USD | 49,360.00 USD | 152,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.50` | 805,570.00 USD | 805,570.00 USD | 66,120.00 USD | 101,350.00 USD | 120,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.50` | 925,210.00 USD | 925,210.00 USD | 0.00 USD | 100,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.52` | 2,830.00 USD | 2,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.52` | 1,240,000.00 USD | 1,240,000.00 USD | 203,080.00 USD | 69,980.00 USD | 164,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.52` | 1,150,000.00 USD | 1,150,000.00 USD | 2,990.00 USD | 135,400.00 USD | 91,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.54` | 637.99 USD | 3,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.54` | 1,350,000.00 USD | 1,350,000.00 USD | 61,500.00 USD | 32,530.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.54` | 1,360,000.00 USD | 1,360,000.00 USD | 71,540.00 USD | 136,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.56` | 1,570,000.00 USD | 1,570,000.00 USD | 183,280.00 USD | 33,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.56` | 2,180,000.00 USD | 2,180,000.00 USD | 691,140.00 USD | 122,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.58` | 1,990,000.00 USD | 1,990,000.00 USD | 234,090.00 USD | 5,060.00 USD | 179,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.58` | 2,940,000.00 USD | 2,940,000.00 USD | 599,490.00 USD | 164,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.60` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 57,190.00 USD | 120,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.60` | 3,060,000.00 USD | 3,060,000.00 USD | 75,040.00 USD | 39,160.00 USD | 388.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.62` | 2,510,000.00 USD | 2,510,000.00 USD | 83,560.00 USD | 57,150.00 USD | 201,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.62` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 43,670.00 USD | 87,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 2,660,000.00 USD | 2,660,000.00 USD | 89,460.00 USD | 30,330.00 USD | 29,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.64` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 12,800.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.64` | 864.50 USD | 4,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.66` | 2,870,000.00 USD | 2,870,000.00 USD | 78,620.00 USD | 21,010.00 USD | 108,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.66` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 16,520.00 USD | 281.77 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 3,150,000.00 USD | 3,150,000.00 USD | 65,090.00 USD | 9,810.00 USD | 212,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.68` | 3,880,000.00 USD | 3,880,000.00 USD | 207,090.00 USD | 43,100.00 USD | 334,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.69` | 209.31 USD | 4,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.70` | 3,250,000.00 USD | 3,250,000.00 USD | 50,130.00 USD | 16,260.00 USD | 30,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.70` | 3,990,000.00 USD | 3,990,000.00 USD | 29,260.00 USD | 41,840.00 USD | 46,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 3,320,000.00 USD | 3,320,000.00 USD | 18,250.00 USD | 0.00 USD | 50,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 3,410,000.00 USD | 3,410,000.00 USD | 49,310.00 USD | 28,810.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.74` | 4,070,000.00 USD | 4,070,000.00 USD | 48,810.00 USD | 30,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.76` | 3,540,000.00 USD | 3,540,000.00 USD | 112,960.00 USD | 2,530.00 USD | 9,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.76` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.78` | 3,690,000.00 USD | 3,690,000.00 USD | 108,350.00 USD | 11,500.00 USD | 35,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.78` | 4,160,000.00 USD | 4,160,000.00 USD | 2,300.00 USD | 0.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.80` | 3,890,000.00 USD | 3,890,000.00 USD | 125,120.00 USD | 22,330.00 USD | 52,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.80` | 4,250,000.00 USD | 4,250,000.00 USD | 27,360.00 USD | 33,750.00 USD | 31,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.80` | 431.62 USD | 4,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.82` | 3,910,000.00 USD | 3,910,000.00 USD | 19,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.82` | 4,350,000.00 USD | 4,350,000.00 USD | 103,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.82` | 6,000.00 USD | 10,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.84` | 4,030,000.00 USD | 4,030,000.00 USD | 40,640.00 USD | 8,820.00 USD | 73,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 4,060,000.00 USD | 4,060,000.00 USD | 13,620.00 USD | 2,250.00 USD | 11,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.86` | 4,470,000.00 USD | 4,470,000.00 USD | 29,310.00 USD | 0.00 USD | 81,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 4,070,000.00 USD | 4,070,000.00 USD | 1,320.00 USD | 8,950.00 USD | 186.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.88` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 4,230,000.00 USD | 4,230,000.00 USD | 31,860.00 USD | 8,140.00 USD | 122,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.90` | 4,610,000.00 USD | 4,610,000.00 USD | 2,440.00 USD | 0.00 USD | 115,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 4,300,000.00 USD | 4,300,000.00 USD | 40,710.00 USD | 7,360.00 USD | 17,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.92` | 4,630,000.00 USD | 4,630,000.00 USD | 1,730.00 USD | 0.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 4,370,000.00 USD | 4,370,000.00 USD | 41,740.00 USD | 12,260.00 USD | 17,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.94` | 4,690,000.00 USD | 4,690,000.00 USD | 58,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.96` | 4,370,000.00 USD | 4,370,000.00 USD | 2,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.96` | 4,690,000.00 USD | 4,690,000.00 USD | 1,930.00 USD | 0.00 USD | 432.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.98` | 4,420,000.00 USD | 4,420,000.00 USD | 25,040.00 USD | 5,550.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.98` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.00` | 4,550,000.00 USD | 4,550,000.00 USD | 85,360.00 USD | 30,520.00 USD | 11,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.00` | 5,030,000.00 USD | 5,030,000.00 USD | 297,650.00 USD | 11,360.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 4,650,000.00 USD | 4,650,000.00 USD | 40,920.00 USD | 43,160.00 USD | 18,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.02` | 5,120,000.00 USD | 5,120,000.00 USD | 34,650.00 USD | 56,120.00 USD | 425.46 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 4,820,000.00 USD | 4,820,000.00 USD | 87,540.00 USD | 43,590.00 USD | 38,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.04` | 5,300,000.00 USD | 5,300,000.00 USD | 90,520.00 USD | 74,750.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.06` | 4,950,000.00 USD | 4,950,000.00 USD | 35,620.00 USD | 33,420.00 USD | 60,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.06` | 5,380,000.00 USD | 5,380,000.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 5,080,000.00 USD | 5,080,000.00 USD | 28,800.00 USD | 29,710.00 USD | 70,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.08` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.10` | 5,400,000.00 USD | 5,400,000.00 USD | 197,760.00 USD | 43,240.00 USD | 81,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.10` | 6,650,000.00 USD | 6,650,000.00 USD | 826,500.00 USD | 35,760.00 USD | 334,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 5,730,000.00 USD | 5,730,000.00 USD | 167,130.00 USD | 47,350.00 USD | 108,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.12` | 7,670,000.00 USD | 7,670,000.00 USD | 490,020.00 USD | 24,170.00 USD | 503,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.14` | 5,950,000.00 USD | 5,950,000.00 USD | 118,520.00 USD | 23,510.00 USD | 79,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.14` | 8,730,000.00 USD | 8,730,000.00 USD | 536,560.00 USD | 18,540.00 USD | 500,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 6,180,000.00 USD | 6,180,000.00 USD | 121,810.00 USD | 44,640.00 USD | 63,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.16` | 9,320,000.00 USD | 9,320,000.00 USD | 358,370.00 USD | 44,360.00 USD | 195,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 6,500,000.00 USD | 6,500,000.00 USD | 174,230.00 USD | 44,900.00 USD | 105,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.18` | 10,340,000.00 USD | 10,340,000.00 USD | 565,140.00 USD | 162,460.00 USD | 291,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.19` | 1,590.00 USD | 12,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.20` | 6,740,000.00 USD | 6,740,000.00 USD | 141,410.00 USD | 43,540.00 USD | 51,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 11,270,000.00 USD | 11,270,000.00 USD | 549,250.00 USD | 134,550.00 USD | 238,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.21` | 1,870.00 USD | 14,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.22` | 6,850,000.00 USD | 6,850,000.00 USD | 86,390.00 USD | 10,580.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.22` | 12,410,000.00 USD | 12,410,000.00 USD | 585,170.00 USD | 144,840.00 USD | 417,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 6,910,000.00 USD | 6,910,000.00 USD | 47,010.00 USD | 4,270.00 USD | 3,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 12,980,000.00 USD | 12,980,000.00 USD | 335,740.00 USD | 56,410.00 USD | 173,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 6,960,000.00 USD | 6,960,000.00 USD | 35,150.00 USD | 8,290.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 13,410,000.00 USD | 13,410,000.00 USD | 273,920.00 USD | 96,980.00 USD | 61,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 7,020,000.00 USD | 7,020,000.00 USD | 44,530.00 USD | 10,920.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 14,110,000.00 USD | 14,110,000.00 USD | 428,160.00 USD | 103,490.00 USD | 170,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.30` | 7,120,000.00 USD | 7,120,000.00 USD | 59,470.00 USD | 13,560.00 USD | 29,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.30` | 14,670,000.00 USD | 14,670,000.00 USD | 199,810.00 USD | 97,780.00 USD | 263,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 7,180,000.00 USD | 7,180,000.00 USD | 37,200.00 USD | 4,250.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.32` | 15,340,000.00 USD | 15,340,000.00 USD | 271,660.00 USD | 59,310.00 USD | 337,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 7,250,000.00 USD | 7,250,000.00 USD | 40,730.00 USD | 9,520.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.34` | 15,670,000.00 USD | 15,670,000.00 USD | 204,260.00 USD | 53,150.00 USD | 69,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 7,340,000.00 USD | 7,340,000.00 USD | 52,470.00 USD | 10,420.00 USD | 33,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.36` | 16,090,000.00 USD | 16,090,000.00 USD | 247,120.00 USD | 73,430.00 USD | 98,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 7,390,000.00 USD | 7,390,000.00 USD | 29,420.00 USD | 7,320.00 USD | 14,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.38` | 16,620,000.00 USD | 16,620,000.00 USD | 383,530.00 USD | 55,400.00 USD | 93,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 7,430,000.00 USD | 7,430,000.00 USD | 31,880.00 USD | 0.00 USD | 25.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.40` | 17,020,000.00 USD | 17,020,000.00 USD | 234,760.00 USD | 42,520.00 USD | 124,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 440.06 USD | 14,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 7,450,000.00 USD | 7,450,000.00 USD | 10,810.00 USD | 2,390.00 USD | 14,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.42` | 17,290,000.00 USD | 17,290,000.00 USD | 176,920.00 USD | 19,780.00 USD | 71,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 7,480,000.00 USD | 7,480,000.00 USD | 10,560.00 USD | 1,630.00 USD | 12,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 17,410,000.00 USD | 17,410,000.00 USD | 41,250.00 USD | 19,420.00 USD | 56,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.46` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 4,580.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 17,520,000.00 USD | 17,520,000.00 USD | 60,020.00 USD | 29,830.00 USD | 19,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.46` | 138.85 USD | 15,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.48` | 17,580,000.00 USD | 17,580,000.00 USD | 12,180.00 USD | 27,840.00 USD | 26,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 17,750,000.00 USD | 17,750,000.00 USD | 89,460.00 USD | 33,210.00 USD | 45,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 17,940,000.00 USD | 17,940,000.00 USD | 102,150.00 USD | 29,320.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 18,150,000.00 USD | 18,150,000.00 USD | 192,090.00 USD | 25,090.00 USD | 378.07 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 18,260,000.00 USD | 18,260,000.00 USD | 88,510.00 USD | 5,260.00 USD | 13,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 18,340,000.00 USD | 18,340,000.00 USD | 35,340.00 USD | 14,530.00 USD | 26,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 18,400,000.00 USD | 18,400,000.00 USD | 38,740.00 USD | 5,460.00 USD | 20,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 18,480,000.00 USD | 18,480,000.00 USD | 70,470.00 USD | 1,540.00 USD | 10,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.62` | 138.98 USD | 15,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.64` | 18,560,000.00 USD | 18,560,000.00 USD | 35,210.00 USD | 17,650.00 USD | 20,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.64` | 1,930.00 USD | 17,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.66` | 18,630,000.00 USD | 18,630,000.00 USD | 37,340.00 USD | 21,280.00 USD | 17,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.68` | 18,740,000.00 USD | 18,740,000.00 USD | 68,230.00 USD | 20,310.00 USD | 15,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.70` | 18,860,000.00 USD | 18,860,000.00 USD | 77,860.00 USD | 12,990.00 USD | 31,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.72` | 18,960,000.00 USD | 18,960,000.00 USD | 70,300.00 USD | 6,920.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 17,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.74` | 19,010,000.00 USD | 19,010,000.00 USD | 21,230.00 USD | 7,200.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.76` | 19,110,000.00 USD | 19,110,000.00 USD | 35,520.00 USD | 12,480.00 USD | 51,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.78` | 19,190,000.00 USD | 19,190,000.00 USD | 65,390.00 USD | 10,300.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.80` | 19,250,000.00 USD | 19,250,000.00 USD | 18,630.00 USD | 28,440.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.82` | 19,490,000.00 USD | 19,490,000.00 USD | 121,860.00 USD | 27,860.00 USD | 86,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.84` | 19,520,000.00 USD | 19,520,000.00 USD | 9,730.00 USD | 7,850.00 USD | 14,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.86` | 19,650,000.00 USD | 19,650,000.00 USD | 58,130.00 USD | 2,210.00 USD | 71,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.88` | 19,690,000.00 USD | 19,690,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.90` | 19,780,000.00 USD | 19,780,000.00 USD | 55,970.00 USD | 19,700.00 USD | 15,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.92` | 19,830,000.00 USD | 19,830,000.00 USD | 27,710.00 USD | 10,810.00 USD | 8,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.94` | 19,960,000.00 USD | 19,960,000.00 USD | 69,320.00 USD | 11,150.00 USD | 51,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.96` | 20,000,000.00 USD | 20,000,000.00 USD | 29,800.00 USD | 1,360.00 USD | 11,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.98` | 20,030,000.00 USD | 20,030,000.00 USD | 840.10 USD | 4,150.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.00` | 20,040,000.00 USD | 20,040,000.00 USD | 0.00 USD | 6,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.02` | 20,080,000.00 USD | 20,080,000.00 USD | 16,100.00 USD | 3,650.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.04` | 20,090,000.00 USD | 20,090,000.00 USD | 1,080.00 USD | 3,590.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.06` | 20,110,000.00 USD | 20,110,000.00 USD | 0.00 USD | 3,480.00 USD | 17,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.08` | 20,130,000.00 USD | 20,130,000.00 USD | 23,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.35` | 2,650.00 USD | 19,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 20,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.88` | 108,750.00 USD | 129,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.89` | 100.13 USD | 129,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.97` | 274,390.00 USD | 403,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 410,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.21` | 419.18 USD | 411,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,670.00 USD | 422,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 434,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.69` | 296,760.00 USD | 731,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.74` | 57,020.00 USD | 788,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.80` | 114.27 USD | 788,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.84` | 283.57 USD | 789,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.88` | 334.56 USD | 789,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.93` | 505.74 USD | 789,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,050.00 USD | 790,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 792,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 793,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 880,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 884,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 885,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 885,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.35` | 283.03 USD | 885,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 886,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.96` | 245.58 USD | 886,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 886,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.30` | 329.82 USD | 887,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 887,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 907,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.44` | 4,280.00 USD | 911,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.63` | 561.14 USD | 912,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.72` | 167.79 USD | 912,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.77` | 185.55 USD | 912,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.79` | 261.72 USD | 912,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.23` | 21,270.00 USD | 934,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.71` | 2,320,000.00 USD | 0.00 USD | 802.75 USD | `-79.23%` | `470.82` |
| `Live` | `Long` | `1.99` | 2,320,000.00 USD | 0.00 USD | 228.27 USD | `-75.82%` | `115.00` |
| `Live` | `Long` | `2.00` | 2,320,000.00 USD | 0.00 USD | 159.60 USD | `-75.70%` | `80.00` |
| `Live` | `Long` | `2.02` | 2,310,000.00 USD | 0.00 USD | 224.39 USD | `-75.33%` | `110.81` |
| `Live` | `Long` | `2.04` | 2,310,000.00 USD | 0.00 USD | 110.52 USD | `-75.21%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,310,000.00 USD | 0.00 USD | 4,920.00 USD | `-74.84%` | `2,382.76` |
| `Live` | `Long` | `2.23` | 2,310,000.00 USD | 0.00 USD | 1,450.00 USD | `-72.77%` | `647.30` |
| `Live` | `Long` | `2.31` | 2,310,000.00 USD | 0.00 USD | 265.08 USD | `-71.92%` | `115.00` |
| `Live` | `Long` | `2.33` | 2,310,000.00 USD | 0.00 USD | 284.29 USD | `-71.55%` | `121.75` |
| `Live` | `Long` | `2.40` | 2,310,000.00 USD | 0.00 USD | 275.43 USD | `-70.82%` | `115.00` |
| `Live` | `Long` | `2.48` | 2,310,000.00 USD | 0.00 USD | 285.78 USD | `-69.73%` | `115.00` |
| `Live` | `Long` | `2.62` | 2,310,000.00 USD | 0.00 USD | 131.67 USD | `-68.02%` | `50.16` |
| `Live` | `Long` | `2.69` | 2,310,000.00 USD | 0.00 USD | 942.44 USD | `-67.29%` | `351.00` |
| `Live` | `Long` | `2.71` | 2,310,000.00 USD | 0.00 USD | 676.25 USD | `-67.05%` | `250.00` |
| `Live` | `Long` | `2.75` | 2,310,000.00 USD | 0.00 USD | 848.24 USD | `-66.44%` | `307.89` |
| `Live` | `Long` | `2.81` | 2,300,000.00 USD | 0.00 USD | 196.35 USD | `-65.83%` | `70.00` |
| `Live` | `Long` | `2.87` | 2,300,000.00 USD | 0.00 USD | 232.67 USD | `-65.10%` | `81.21` |
| `Live` | `Long` | `2.94` | 2,300,000.00 USD | 0.00 USD | 44,510.00 USD | `-64.25%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,260,000.00 USD | 0.00 USD | 111.12 USD | `-63.76%` | `37.35` |
| `Live` | `Long` | `3.06` | 2,260,000.00 USD | 0.00 USD | 351.33 USD | `-62.78%` | `115.00` |
| `Live` | `Long` | `3.27` | 2,260,000.00 USD | 0.00 USD | 162.51 USD | `-60.10%` | `49.62` |
| `Live` | `Long` | `3.35` | 2,260,000.00 USD | 0.00 USD | 174.46 USD | `-59.13%` | `52.00` |
| `Live` | `Long` | `3.37` | 2,260,000.00 USD | 0.00 USD | 389.53 USD | `-59.01%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,260,000.00 USD | 0.00 USD | 151.88 USD | `-58.89%` | `45.00` |
| `Live` | `Long` | `3.40` | 2,260,000.00 USD | 0.00 USD | 23,920.00 USD | `-58.52%` | `7,024.08` |
| `Live` | `Long` | `3.54` | 2,230,000.00 USD | 0.00 USD | 26,390.00 USD | `-56.94%` | `7,465.11` |
| `Live` | `Long` | `3.54` | 2,210,000.00 USD | 0.00 USD | 392.22 USD | `-56.81%` | `110.64` |
| `Live` | `Long` | `3.62` | 2,210,000.00 USD | 0.00 USD | 414.26 USD | `-55.84%` | `114.28` |
| `Live` | `Long` | `3.65` | 2,210,000.00 USD | 0.00 USD | 692.51 USD | `-55.60%` | `189.99` |
| `Live` | `Long` | `3.65` | 2,210,000.00 USD | 0.00 USD | 1,460.00 USD | `-55.47%` | `400.75` |
| `Live` | `Long` | `3.67` | 2,200,000.00 USD | 0.00 USD | 109.95 USD | `-55.35%` | `30.00` |
| `Live` | `Long` | `3.69` | 2,200,000.00 USD | 0.00 USD | 1,350.00 USD | `-54.99%` | `365.02` |
| `Live` | `Long` | `3.75` | 2,200,000.00 USD | 0.00 USD | 1,500.00 USD | `-54.26%` | `400.00` |
| `Live` | `Long` | `3.77` | 2,200,000.00 USD | 0.00 USD | 4,850.00 USD | `-54.13%` | `1,288.03` |
| `Live` | `Long` | `3.79` | 2,200,000.00 USD | 0.00 USD | 3,790.00 USD | `-53.77%` | `1,000.00` |
| `Live` | `Long` | `3.83` | 2,190,000.00 USD | 0.00 USD | 1,450.00 USD | `-53.28%` | `377.71` |
| `Live` | `Long` | `3.90` | 2,190,000.00 USD | 0.00 USD | 131.73 USD | `-52.55%` | `33.82` |
| `Live` | `Long` | `3.96` | 2,190,000.00 USD | 0.00 USD | 186.12 USD | `-51.70%` | `46.94` |
| `Live` | `Long` | `4.03` | 2,190,000.00 USD | 0.00 USD | 402.70 USD | `-50.97%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,190,000.00 USD | 0.00 USD | 152.29 USD | `-50.72%` | `37.65` |
| `Live` | `Long` | `4.09` | 2,190,000.00 USD | 0.00 USD | 147.34 USD | `-50.11%` | `35.98` |
| `Live` | `Long` | `4.14` | 2,190,000.00 USD | 0.00 USD | 159.29 USD | `-49.51%` | `38.43` |
| `Live` | `Long` | `4.20` | 2,190,000.00 USD | 0.00 USD | 194.10 USD | `-48.90%` | `46.27` |
| `Live` | `Long` | `4.24` | 2,190,000.00 USD | 0.00 USD | 169.40 USD | `-48.41%` | `40.00` |
| `Live` | `Long` | `4.29` | 2,190,000.00 USD | 0.00 USD | 697.77 USD | `-47.80%` | `162.84` |
| `Live` | `Long` | `4.45` | 2,190,000.00 USD | 0.00 USD | 599.72 USD | `-45.85%` | `134.92` |
| `Live` | `Long` | `4.54` | 2,190,000.00 USD | 0.00 USD | 3,030.00 USD | `-44.63%` | `666.20` |
| `Live` | `Long` | `4.58` | 2,190,000.00 USD | 0.00 USD | 2,290.00 USD | `-44.15%` | `500.00` |
| `Live` | `Long` | `4.59` | 2,180,000.00 USD | 0.00 USD | 30,970.00 USD | `-44.02%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,150,000.00 USD | 0.00 USD | 486.93 USD | `-43.78%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,150,000.00 USD | 0.00 USD | 2,930.00 USD | `-43.66%` | `634.06` |
| `Live` | `Long` | `4.66` | 2,150,000.00 USD | 0.00 USD | 105.11 USD | `-43.29%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,150,000.00 USD | 0.00 USD | 3,280.00 USD | `-43.17%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,150,000.00 USD | 0.00 USD | 1,490.00 USD | `-43.05%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,140,000.00 USD | 0.00 USD | 8,530.00 USD | `-42.93%` | `1,819.64` |
| `Live` | `Long` | `4.70` | 2,140,000.00 USD | 0.00 USD | 7,040.00 USD | `-42.81%` | `1,500.00` |
| `Live` | `Long` | `4.72` | 2,130,000.00 USD | 0.00 USD | 440.94 USD | `-42.44%` | `93.32` |
| `Live` | `Long` | `4.76` | 2,130,000.00 USD | 0.00 USD | 105.64 USD | `-41.95%` | `22.17` |
| `Live` | `Long` | `4.83` | 2,130,000.00 USD | 0.00 USD | 467.01 USD | `-41.10%` | `96.59` |
| `Live` | `Long` | `4.91` | 2,130,000.00 USD | 0.00 USD | 3,880.00 USD | `-40.25%` | `790.61` |
| `Live` | `Long` | `4.92` | 2,120,000.00 USD | 0.00 USD | 17,380.00 USD | `-40.13%` | `3,537.00` |
| `Live` | `Long` | `4.95` | 2,110,000.00 USD | 0.00 USD | 19,690.00 USD | `-39.76%` | `3,981.48` |
| `Live` | `Long` | `4.96` | 2,090,000.00 USD | 0.00 USD | 945.36 USD | `-39.64%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,090,000.00 USD | 0.00 USD | 4,430.00 USD | `-39.52%` | `893.25` |
| `Live` | `Long` | `4.97` | 2,080,000.00 USD | 0.00 USD | 282.23 USD | `-39.39%` | `56.73` |
| `Live` | `Long` | `5.00` | 2,080,000.00 USD | 0.00 USD | 269.53 USD | `-39.15%` | `53.96` |
| `Live` | `Long` | `5.00` | 2,080,000.00 USD | 0.00 USD | 175.17 USD | `-39.03%` | `35.00` |
| `Live` | `Long` | `5.01` | 2,080,000.00 USD | 0.00 USD | 56,390.00 USD | `-38.91%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,020,000.00 USD | 0.00 USD | 167.78 USD | `-38.79%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,020,000.00 USD | 0.00 USD | 314.59 USD | `-38.66%` | `62.48` |
| `Live` | `Long` | `5.05` | 2,020,000.00 USD | 0.00 USD | 504.74 USD | `-38.42%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,020,000.00 USD | 0.00 USD | 318.46 USD | `-38.18%` | `62.75` |
| `Live` | `Long` | `5.09` | 2,020,000.00 USD | 0.00 USD | 651.75 USD | `-37.93%` | `127.92` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 1,020.00 USD | `-37.69%` | `198.97` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 250.20 USD | `-37.57%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,020,000.00 USD | 0.00 USD | 396.06 USD | `-37.45%` | `77.13` |
| `Live` | `Long` | `5.17` | 2,020,000.00 USD | 0.00 USD | 1,620.00 USD | `-36.96%` | `312.94` |
| `Live` | `Long` | `5.18` | 2,020,000.00 USD | 0.00 USD | 150.57 USD | `-36.84%` | `29.04` |
| `Live` | `Long` | `5.20` | 2,020,000.00 USD | 0.00 USD | 480.07 USD | `-36.71%` | `92.41` |
| `Live` | `Long` | `5.21` | 2,020,000.00 USD | 0.00 USD | 300.91 USD | `-36.47%` | `57.70` |
| `Live` | `Long` | `5.25` | 2,020,000.00 USD | 0.00 USD | 1,050.00 USD | `-35.98%` | `200.00` |
| `Live` | `Long` | `5.26` | 2,020,000.00 USD | 0.00 USD | 2,230.00 USD | `-35.86%` | `423.54` |
| `Live` | `Long` | `5.29` | 2,010,000.00 USD | 0.00 USD | 1,410.00 USD | `-35.62%` | `267.21` |
| `Live` | `Long` | `5.29` | 2,010,000.00 USD | 0.00 USD | 228.06 USD | `-35.50%` | `43.07` |
| `Live` | `Long` | `5.32` | 2,010,000.00 USD | 0.00 USD | 5,830.00 USD | `-35.25%` | `1,096.81` |
| `Live` | `Long` | `5.33` | 2,010,000.00 USD | 0.00 USD | 839.65 USD | `-35.13%` | `157.68` |
| `Live` | `Long` | `5.34` | 2,010,000.00 USD | 0.00 USD | 162,680.00 USD | `-34.89%` | `30,435.20` |
| `Live` | `Long` | `5.39` | 1,840,000.00 USD | 0.00 USD | 1,180.00 USD | `-34.28%` | `218.47` |
| `Live` | `Long` | `5.41` | 1,840,000.00 USD | 0.00 USD | 918.53 USD | `-34.16%` | `169.94` |
| `Live` | `Long` | `5.42` | 1,840,000.00 USD | 0.00 USD | 20,160.00 USD | `-34.03%` | `3,723.69` |
| `Live` | `Long` | `5.42` | 1,820,000.00 USD | 0.00 USD | 160,400.00 USD | `-33.91%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,660,000.00 USD | 0.00 USD | 1,360.00 USD | `-33.79%` | `250.00` |
| `Live` | `Long` | `5.46` | 1,660,000.00 USD | 0.00 USD | 264.72 USD | `-33.43%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-33.30%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,660,000.00 USD | 0.00 USD | 354.06 USD | `-33.18%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,660,000.00 USD | 0.00 USD | 19,290.00 USD | `-33.06%` | `3,510.41` |
| `Live` | `Long` | `5.50` | 1,640,000.00 USD | 0.00 USD | 2,200.00 USD | `-32.94%` | `400.00` |
| `Live` | `Long` | `5.51` | 1,640,000.00 USD | 0.00 USD | 367.41 USD | `-32.82%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,640,000.00 USD | 0.00 USD | 121.38 USD | `-32.57%` | `21.93` |
| `Live` | `Long` | `5.54` | 1,640,000.00 USD | 0.00 USD | 2,760.00 USD | `-32.45%` | `497.70` |
| `Live` | `Long` | `5.58` | 1,630,000.00 USD | 0.00 USD | 63,260.00 USD | `-32.09%` | `11,347.58` |
| `Live` | `Long` | `5.59` | 1,570,000.00 USD | 0.00 USD | 34,430.00 USD | `-31.84%` | `6,153.60` |
| `Live` | `Long` | `5.63` | 1,540,000.00 USD | 0.00 USD | 468.55 USD | `-31.35%` | `83.15` |
| `Live` | `Long` | `5.67` | 1,540,000.00 USD | 0.00 USD | 11,350.00 USD | `-30.87%` | `2,000.00` |
| `Live` | `Long` | `5.71` | 1,520,000.00 USD | 0.00 USD | 147.33 USD | `-30.38%` | `25.78` |
| `Live` | `Long` | `5.72` | 1,520,000.00 USD | 0.00 USD | 2,390.00 USD | `-30.26%` | `417.17` |
| `Live` | `Long` | `5.74` | 1,520,000.00 USD | 0.00 USD | 238.86 USD | `-30.14%` | `41.65` |
| `Live` | `Long` | `5.75` | 1,520,000.00 USD | 0.00 USD | 125.70 USD | `-30.01%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,520,000.00 USD | 0.00 USD | 3,190.00 USD | `-29.89%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,520,000.00 USD | 0.00 USD | 10,850.00 USD | `-29.77%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,510,000.00 USD | 0.00 USD | 902.40 USD | `-29.65%` | `156.26` |
| `Live` | `Long` | `5.79` | 1,510,000.00 USD | 0.00 USD | 635.31 USD | `-29.41%` | `109.63` |
| `Live` | `Long` | `5.80` | 1,510,000.00 USD | 0.00 USD | 580.50 USD | `-29.28%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,500,000.00 USD | 0.00 USD | 243.07 USD | `-29.16%` | `41.80` |
| `Live` | `Long` | `5.83` | 1,500,000.00 USD | 0.00 USD | 145.88 USD | `-28.92%` | `25.00` |
| `Live` | `Long` | `5.86` | 1,500,000.00 USD | 0.00 USD | 2,110.00 USD | `-28.67%` | `360.33` |
| `Live` | `Long` | `5.89` | 1,500,000.00 USD | 0.00 USD | 984.70 USD | `-28.19%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,500,000.00 USD | 0.00 USD | 399.18 USD | `-28.07%` | `67.60` |
| `Live` | `Long` | `5.92` | 1,500,000.00 USD | 0.00 USD | 277.35 USD | `-27.94%` | `46.89` |
| `Live` | `Long` | `5.95` | 1,500,000.00 USD | 0.00 USD | 1,610.00 USD | `-27.58%` | `270.00` |
| `Live` | `Long` | `5.96` | 1,500,000.00 USD | 0.00 USD | 11,720.00 USD | `-27.46%` | `1,968.19` |
| `Live` | `Long` | `5.97` | 1,490,000.00 USD | 0.00 USD | 585.97 USD | `-27.21%` | `98.07` |
| `Live` | `Long` | `5.99` | 1,490,000.00 USD | 0.00 USD | 243.05 USD | `-27.09%` | `40.61` |
| `Live` | `Long` | `6.00` | 1,490,000.00 USD | 0.00 USD | 341.56 USD | `-26.85%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,490,000.00 USD | 0.00 USD | 446.85 USD | `-26.72%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,490,000.00 USD | 0.00 USD | 331.68 USD | `-26.48%` | `54.96` |
| `Live` | `Long` | `6.04` | 1,490,000.00 USD | 0.00 USD | 105.61 USD | `-26.36%` | `17.47` |
| `Live` | `Long` | `6.05` | 1,490,000.00 USD | 0.00 USD | 1,310.00 USD | `-26.24%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,480,000.00 USD | 0.00 USD | 265.10 USD | `-26.12%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,480,000.00 USD | 0.00 USD | 1,690.00 USD | `-25.99%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,480,000.00 USD | 0.00 USD | 405.14 USD | `-25.87%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,480,000.00 USD | 0.00 USD | 3,130.00 USD | `-25.75%` | `512.81` |
| `Live` | `Long` | `6.12` | 1,480,000.00 USD | 0.00 USD | 1,140.00 USD | `-25.51%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,480,000.00 USD | 0.00 USD | 137.02 USD | `-25.38%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,480,000.00 USD | 0.00 USD | 2,030.00 USD | `-25.26%` | `330.65` |
| `Live` | `Long` | `6.14` | 1,480,000.00 USD | 0.00 USD | 238.61 USD | `-25.14%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,470,000.00 USD | 0.00 USD | 7,810.00 USD | `-25.02%` | `1,268.30` |
| `Live` | `Long` | `6.17` | 1,470,000.00 USD | 0.00 USD | 6,510.00 USD | `-24.90%` | `1,056.68` |
| `Live` | `Long` | `6.17` | 1,460,000.00 USD | 0.00 USD | 104.36 USD | `-24.78%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,460,000.00 USD | 0.00 USD | 310.25 USD | `-24.41%` | `50.00` |
| `Live` | `Long` | `6.25` | 1,460,000.00 USD | 0.00 USD | 3,020.00 USD | `-23.92%` | `483.77` |
| `Live` | `Long` | `6.25` | 1,460,000.00 USD | 0.00 USD | 972.65 USD | `-23.80%` | `155.50` |
| `Live` | `Long` | `6.28` | 1,460,000.00 USD | 0.00 USD | 2,510.00 USD | `-23.56%` | `400.00` |
| `Live` | `Long` | `6.29` | 1,450,000.00 USD | 0.00 USD | 2,430.00 USD | `-23.31%` | `386.46` |
| `Live` | `Long` | `6.32` | 1,450,000.00 USD | 0.00 USD | 277.04 USD | `-23.07%` | `43.87` |
| `Live` | `Long` | `6.36` | 1,450,000.00 USD | 0.00 USD | 4,470.00 USD | `-22.58%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,450,000.00 USD | 0.00 USD | 284,770.00 USD | `-22.46%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 1,160,000.00 USD | 0.00 USD | 6,410.00 USD | `-22.34%` | `1,006.23` |
| `Live` | `Long` | `6.42` | 1,160,000.00 USD | 0.00 USD | 306.32 USD | `-21.85%` | `47.75` |
| `Live` | `Long` | `6.42` | 1,150,000.00 USD | 0.00 USD | 484.64 USD | `-21.73%` | `75.43` |
| `Live` | `Long` | `6.43` | 1,150,000.00 USD | 0.00 USD | 6,780.00 USD | `-21.61%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 1,150,000.00 USD | 0.00 USD | 1,050.00 USD | `-21.24%` | `162.75` |
| `Live` | `Long` | `6.50` | 1,150,000.00 USD | 0.00 USD | 257.99 USD | `-20.76%` | `39.66` |
| `Live` | `Long` | `6.51` | 1,150,000.00 USD | 0.00 USD | 651.50 USD | `-20.63%` | `100.00` |
| `Live` | `Long` | `6.54` | 1,150,000.00 USD | 0.00 USD | 852.03 USD | `-20.39%` | `130.38` |
| `Live` | `Long` | `6.54` | 1,140,000.00 USD | 0.00 USD | 8,970.00 USD | `-20.27%` | `1,370.89` |
| `Live` | `Long` | `6.58` | 1,140,000.00 USD | 0.00 USD | 3,250.00 USD | `-19.78%` | `494.28` |
| `Live` | `Long` | `6.59` | 1,130,000.00 USD | 0.00 USD | 1,100.00 USD | `-19.66%` | `166.55` |
| `Live` | `Long` | `6.62` | 1,130,000.00 USD | 0.00 USD | 2,110.00 USD | `-19.42%` | `318.57` |
| `Live` | `Long` | `6.62` | 1,130,000.00 USD | 0.00 USD | 364.90 USD | `-19.29%` | `55.08` |
| `Live` | `Long` | `6.63` | 1,130,000.00 USD | 0.00 USD | 245.89 USD | `-19.17%` | `37.06` |
| `Live` | `Long` | `6.67` | 1,130,000.00 USD | 0.00 USD | 1,320.00 USD | `-18.68%` | `198.12` |
| `Live` | `Long` | `6.70` | 1,130,000.00 USD | 0.00 USD | 1,200.00 USD | `-18.44%` | `179.39` |
| `Live` | `Long` | `6.71` | 1,130,000.00 USD | 0.00 USD | 16,070.00 USD | `-18.32%` | `2,396.06` |
| `Live` | `Long` | `6.71` | 1,110,000.00 USD | 0.00 USD | 6,180.00 USD | `-18.20%` | `920.74` |
| `Live` | `Long` | `6.72` | 1,100,000.00 USD | 0.00 USD | 428.72 USD | `-18.08%` | `63.75` |
| `Live` | `Long` | `6.75` | 1,100,000.00 USD | 0.00 USD | 1,330.00 USD | `-17.83%` | `196.95` |
| `Live` | `Long` | `6.78` | 1,100,000.00 USD | 0.00 USD | 6,780.00 USD | `-17.47%` | `1,000.00` |
| `Live` | `Long` | `6.79` | 1,100,000.00 USD | 0.00 USD | 401,940.00 USD | `-17.34%` | `59,240.06` |
| `Live` | `Long` | `6.79` | 693,540.00 USD | 0.00 USD | 4,720.00 USD | `-17.22%` | `694.73` |
| `Live` | `Long` | `6.80` | 688,820.00 USD | 0.00 USD | 1,500.00 USD | `-17.10%` | `220.95` |
| `Live` | `Long` | `6.82` | 687,310.00 USD | 0.00 USD | 7,230.00 USD | `-16.98%` | `1,061.04` |
| `Live` | `Long` | `6.83` | 680,080.00 USD | 0.00 USD | 446.83 USD | `-16.86%` | `65.47` |
| `Live` | `Long` | `6.83` | 679,640.00 USD | 0.00 USD | 1,560.00 USD | `-16.74%` | `228.41` |
| `Live` | `Long` | `6.84` | 678,080.00 USD | 0.00 USD | 204.12 USD | `-16.61%` | `29.82` |
| `Live` | `Long` | `6.87` | 677,870.00 USD | 0.00 USD | 3,340.00 USD | `-16.37%` | `486.46` |
| `Live` | `Long` | `6.88` | 674,530.00 USD | 0.00 USD | 1,580.00 USD | `-16.13%` | `229.18` |
| `Live` | `Long` | `6.93` | 672,950.00 USD | 0.00 USD | 3,500.00 USD | `-15.52%` | `504.07` |
| `Live` | `Long` | `6.95` | 669,460.00 USD | 0.00 USD | 3,980.00 USD | `-15.40%` | `572.68` |
| `Live` | `Long` | `6.96` | 665,480.00 USD | 0.00 USD | 3,480.00 USD | `-15.27%` | `500.00` |
| `Live` | `Long` | `6.96` | 662,000.00 USD | 0.00 USD | 972.59 USD | `-15.15%` | `139.64` |
| `Live` | `Long` | `6.97` | 661,030.00 USD | 0.00 USD | 128,810.00 USD | `-15.03%` | `18,466.99` |
| `Live` | `Long` | `6.99` | 532,220.00 USD | 0.00 USD | 297.49 USD | `-14.91%` | `42.59` |
| `Live` | `Long` | `7.00` | 531,930.00 USD | 0.00 USD | 746.58 USD | `-14.79%` | `106.73` |
| `Live` | `Long` | `7.00` | 531,180.00 USD | 0.00 USD | 20,860.00 USD | `-14.66%` | `2,978.11` |
| `Live` | `Long` | `7.03` | 510,320.00 USD | 0.00 USD | 1,370.00 USD | `-14.42%` | `194.51` |
| `Live` | `Long` | `7.05` | 508,950.00 USD | 0.00 USD | 354.23 USD | `-14.06%` | `50.21` |
| `Live` | `Long` | `7.07` | 508,600.00 USD | 0.00 USD | 24,310.00 USD | `-13.93%` | `3,441.37` |
| `Live` | `Long` | `7.08` | 484,280.00 USD | 0.00 USD | 6,700.00 USD | `-13.81%` | `947.44` |
| `Live` | `Long` | `7.08` | 477,580.00 USD | 0.00 USD | 644.88 USD | `-13.69%` | `91.02` |
| `Live` | `Long` | `7.11` | 476,940.00 USD | 0.00 USD | 29,350.00 USD | `-13.45%` | `4,130.68` |
| `Live` | `Long` | `7.12` | 447,590.00 USD | 0.00 USD | 379.66 USD | `-13.32%` | `53.36` |
| `Live` | `Long` | `7.13` | 447,210.00 USD | 0.00 USD | 777.50 USD | `-13.08%` | `108.97` |
| `Live` | `Long` | `7.14` | 446,430.00 USD | 0.00 USD | 20,270.00 USD | `-12.96%` | `2,837.00` |
| `Live` | `Long` | `7.17` | 426,160.00 USD | 0.00 USD | 9,550.00 USD | `-12.59%` | `1,331.12` |
| `Live` | `Long` | `7.18` | 416,610.00 USD | 0.00 USD | 4,570.00 USD | `-12.47%` | `635.49` |
| `Live` | `Long` | `7.21` | 412,040.00 USD | 0.00 USD | 322.94 USD | `-12.11%` | `44.76` |
| `Live` | `Long` | `7.24` | 411,720.00 USD | 0.00 USD | 1,480.00 USD | `-11.86%` | `205.21` |
| `Live` | `Long` | `7.25` | 410,240.00 USD | 0.00 USD | 185.83 USD | `-11.74%` | `25.65` |
| `Live` | `Long` | `7.25` | 410,050.00 USD | 0.00 USD | 21,280.00 USD | `-11.62%` | `2,933.17` |
| `Live` | `Long` | `7.29` | 388,770.00 USD | 0.00 USD | 65,980.00 USD | `-11.25%` | `9,057.61` |
| `Live` | `Long` | `7.29` | 322,790.00 USD | 0.00 USD | 1,680.00 USD | `-11.13%` | `230.97` |
| `Live` | `Long` | `7.34` | 321,100.00 USD | 0.00 USD | 4,370.00 USD | `-10.52%` | `594.84` |
| `Live` | `Long` | `7.37` | 316,730.00 USD | 0.00 USD | 2,940.00 USD | `-10.28%` | `399.15` |
| `Live` | `Long` | `7.38` | 313,790.00 USD | 0.00 USD | 1,100.00 USD | `-10.16%` | `148.75` |
| `Live` | `Long` | `7.39` | 312,690.00 USD | 0.00 USD | 1,480.00 USD | `-9.91%` | `200.00` |
| `Live` | `Long` | `7.42` | 311,220.00 USD | 0.00 USD | 147.61 USD | `-9.55%` | `19.88` |
| `Live` | `Long` | `7.43` | 311,070.00 USD | 0.00 USD | 2,430.00 USD | `-9.43%` | `327.05` |
| `Live` | `Long` | `7.45` | 308,640.00 USD | 0.00 USD | 13,520.00 USD | `-9.30%` | `1,815.39` |
| `Live` | `Long` | `7.46` | 295,120.00 USD | 0.00 USD | 10,390.00 USD | `-9.18%` | `1,393.53` |
| `Live` | `Long` | `7.46` | 284,730.00 USD | 0.00 USD | 4,590.00 USD | `-9.06%` | `614.36` |
| `Live` | `Long` | `7.47` | 280,150.00 USD | 0.00 USD | 1,120.00 USD | `-8.94%` | `149.52` |
| `Live` | `Long` | `7.50` | 279,030.00 USD | 0.00 USD | 962.81 USD | `-8.70%` | `128.46` |
| `Live` | `Long` | `7.50` | 278,070.00 USD | 0.00 USD | 421.78 USD | `-8.57%` | `56.20` |
| `Live` | `Long` | `7.51` | 277,640.00 USD | 0.00 USD | 1,710.00 USD | `-8.45%` | `228.21` |
| `Live` | `Long` | `7.53` | 275,930.00 USD | 0.00 USD | 1,570.00 USD | `-8.33%` | `208.52` |
| `Live` | `Long` | `7.54` | 274,360.00 USD | 0.00 USD | 4,210.00 USD | `-8.21%` | `559.01` |
| `Live` | `Long` | `7.55` | 270,150.00 USD | 0.00 USD | 572.67 USD | `-7.96%` | `75.80` |
| `Live` | `Long` | `7.57` | 269,570.00 USD | 0.00 USD | 25,060.00 USD | `-7.84%` | `3,312.23` |
| `Live` | `Long` | `7.58` | 244,520.00 USD | 0.00 USD | 1,180.00 USD | `-7.72%` | `155.61` |
| `Live` | `Long` | `7.59` | 243,340.00 USD | 0.00 USD | 24,760.00 USD | `-7.48%` | `3,260.14` |
| `Live` | `Long` | `7.61` | 218,580.00 USD | 0.00 USD | 2,660.00 USD | `-7.36%` | `349.34` |
| `Live` | `Long` | `7.62` | 215,920.00 USD | 0.00 USD | 754.04 USD | `-7.23%` | `99.02` |
| `Live` | `Long` | `7.62` | 215,170.00 USD | 0.00 USD | 787.51 USD | `-7.11%` | `103.28` |
| `Live` | `Long` | `7.63` | 214,380.00 USD | 0.00 USD | 378.93 USD | `-6.99%` | `49.63` |
| `Live` | `Long` | `7.64` | 214,000.00 USD | 0.00 USD | 1,890.00 USD | `-6.87%` | `247.83` |
| `Live` | `Long` | `7.66` | 212,110.00 USD | 0.00 USD | 135.42 USD | `-6.75%` | `17.69` |
| `Live` | `Long` | `7.67` | 211,970.00 USD | 0.00 USD | 256.09 USD | `-6.62%` | `33.41` |
| `Live` | `Long` | `7.67` | 211,710.00 USD | 0.00 USD | 6,780.00 USD | `-6.50%` | `883.63` |
| `Live` | `Long` | `7.68` | 204,930.00 USD | 0.00 USD | 739.30 USD | `-6.38%` | `96.20` |
| `Live` | `Long` | `7.70` | 204,190.00 USD | 0.00 USD | 3,250.00 USD | `-6.26%` | `422.01` |
| `Live` | `Long` | `7.75` | 200,950.00 USD | 0.00 USD | 500.12 USD | `-5.53%` | `64.49` |
| `Live` | `Long` | `7.76` | 200,450.00 USD | 0.00 USD | 455.73 USD | `-5.41%` | `58.69` |
| `Live` | `Long` | `7.78` | 199,990.00 USD | 0.00 USD | 8,670.00 USD | `-5.28%` | `1,115.74` |
| `Live` | `Long` | `7.79` | 191,320.00 USD | 0.00 USD | 2,470.00 USD | `-5.16%` | `317.11` |
| `Live` | `Long` | `7.79` | 188,850.00 USD | 0.00 USD | 4,480.00 USD | `-5.04%` | `574.50` |
| `Live` | `Long` | `7.80` | 184,370.00 USD | 0.00 USD | 4,020.00 USD | `-4.92%` | `515.59` |
| `Live` | `Long` | `7.82` | 180,340.00 USD | 0.00 USD | 1,560.00 USD | `-4.80%` | `200.00` |
| `Live` | `Long` | `7.83` | 178,780.00 USD | 0.00 USD | 706.68 USD | `-4.68%` | `90.31` |
| `Live` | `Long` | `7.84` | 178,070.00 USD | 0.00 USD | 24,340.00 USD | `-4.43%` | `3,102.56` |
| `Live` | `Long` | `7.87` | 153,730.00 USD | 0.00 USD | 233.83 USD | `-4.19%` | `29.73` |
| `Live` | `Long` | `7.88` | 153,500.00 USD | 0.00 USD | 555.19 USD | `-4.07%` | `70.50` |
| `Live` | `Long` | `7.89` | 152,950.00 USD | 0.00 USD | 986.88 USD | `-3.82%` | `125.00` |
| `Live` | `Long` | `7.91` | 151,960.00 USD | 0.00 USD | 505.13 USD | `-3.70%` | `63.90` |
| `Live` | `Long` | `7.92` | 151,450.00 USD | 0.00 USD | 4,600.00 USD | `-3.46%` | `580.78` |
| `Live` | `Long` | `7.93` | 146,850.00 USD | 0.00 USD | 16,340.00 USD | `-3.34%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 130,510.00 USD | 0.00 USD | 127,110.00 USD | `-3.21%` | `15,999.24` |
| `Live` | `Long` | `7.97` | 3,390.00 USD | 0.00 USD | 1,580.00 USD | `-2.85%` | `198.26` |
| `Live` | `Long` | `7.99` | 1,810.00 USD | 0.00 USD | 1,600.00 USD | `-2.73%` | `200.68` |
| `Live` | `Long` | `8.00` | 210.99 USD | 0.00 USD | 210.99 USD | `-2.60%` | `26.39` |
| `Live` | `Short` | `8.52` | 2,830.00 USD | 2,830.00 USD | 0.00 USD | `+3.73%` | `332.64` |
| `Live` | `Short` | `8.54` | 3,470.00 USD | 637.99 USD | 0.00 USD | `+3.97%` | `74.75` |
| `Live` | `Short` | `8.64` | 4,330.00 USD | 864.50 USD | 0.00 USD | `+5.31%` | `100.00` |
| `Live` | `Short` | `8.69` | 4,540.00 USD | 209.31 USD | 0.00 USD | `+5.80%` | `24.10` |
| `Live` | `Short` | `8.80` | 4,980.00 USD | 431.62 USD | 0.00 USD | `+7.26%` | `49.02` |
| `Live` | `Short` | `8.82` | 10,980.00 USD | 6,000.00 USD | 0.00 USD | `+7.51%` | `680.16` |
| `Live` | `Short` | `9.19` | 12,570.00 USD | 1,590.00 USD | 0.00 USD | `+11.89%` | `173.30` |
| `Live` | `Short` | `9.21` | 14,440.00 USD | 1,870.00 USD | 0.00 USD | `+12.26%` | `202.76` |
| `Live` | `Short` | `9.41` | 14,880.00 USD | 440.06 USD | 0.00 USD | `+14.69%` | `46.74` |
| `Live` | `Short` | `9.46` | 15,020.00 USD | 138.85 USD | 0.00 USD | `+15.30%` | `14.67` |
| `Live` | `Short` | `9.62` | 15,160.00 USD | 138.98 USD | 0.00 USD | `+17.25%` | `14.44` |
| `Live` | `Short` | `9.64` | 17,090.00 USD | 1,930.00 USD | 0.00 USD | `+17.50%` | `200.61` |
| `Live` | `Short` | `9.73` | 17,280.00 USD | 192.95 USD | 0.00 USD | `+18.59%` | `19.82` |
| `Live` | `Short` | `10.35` | 19,940.00 USD | 2,650.00 USD | 0.00 USD | `+26.02%` | `256.58` |
| `Live` | `Short` | `10.56` | 20,460.00 USD | 523.81 USD | 0.00 USD | `+28.70%` | `49.58` |
| `Live` | `Short` | `10.88` | 129,210.00 USD | 108,750.00 USD | 0.00 USD | `+32.48%` | `10,000.00` |
| `Live` | `Short` | `10.89` | 129,310.00 USD | 100.13 USD | 0.00 USD | `+32.72%` | `9.19` |
| `Live` | `Short` | `10.97` | 403,700.00 USD | 274,390.00 USD | 0.00 USD | `+33.70%` | `25,000.94` |
| `Live` | `Short` | `11.01` | 410,660.00 USD | 6,970.00 USD | 0.00 USD | `+34.06%` | `633.00` |
| `Live` | `Short` | `11.21` | 411,080.00 USD | 419.18 USD | 0.00 USD | `+36.50%` | `37.41` |
| `Live` | `Short` | `11.27` | 422,750.00 USD | 11,670.00 USD | 0.00 USD | `+37.23%` | `1,035.87` |
| `Live` | `Short` | `11.62` | 434,890.00 USD | 12,140.00 USD | 0.00 USD | `+41.62%` | `1,043.90` |
| `Live` | `Short` | `11.69` | 731,650.00 USD | 296,760.00 USD | 0.00 USD | `+42.35%` | `25,397.02` |
| `Live` | `Short` | `11.74` | 788,680.00 USD | 57,020.00 USD | 0.00 USD | `+43.08%` | `4,855.14` |
| `Live` | `Short` | `11.80` | 788,790.00 USD | 114.27 USD | 0.00 USD | `+43.81%` | `9.68` |
| `Live` | `Short` | `11.84` | 789,070.00 USD | 283.57 USD | 0.00 USD | `+44.17%` | `23.96` |
| `Live` | `Short` | `11.88` | 789,410.00 USD | 334.56 USD | 0.00 USD | `+44.78%` | `28.15` |
| `Live` | `Short` | `11.93` | 789,910.00 USD | 505.74 USD | 0.00 USD | `+45.27%` | `42.41` |
| `Live` | `Short` | `11.95` | 790,960.00 USD | 1,050.00 USD | 0.00 USD | `+45.51%` | `87.54` |
| `Live` | `Short` | `12.30` | 792,690.00 USD | 1,730.00 USD | 0.00 USD | `+49.90%` | `140.71` |
| `Live` | `Short` | `12.40` | 793,030.00 USD | 343.62 USD | 0.00 USD | `+51.12%` | `27.70` |
| `Live` | `Short` | `13.20` | 880,980.00 USD | 87,940.00 USD | 0.00 USD | `+60.74%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 884,790.00 USD | 3,810.00 USD | 0.00 USD | `+61.96%` | `286.56` |
| `Live` | `Short` | `13.46` | 885,220.00 USD | 430.34 USD | 0.00 USD | `+64.03%` | `31.96` |
| `Live` | `Short` | `13.69` | 885,390.00 USD | 172.29 USD | 0.00 USD | `+66.71%` | `12.59` |
| `Live` | `Short` | `14.35` | 885,670.00 USD | 283.03 USD | 0.00 USD | `+74.75%` | `19.73` |
| `Live` | `Short` | `14.66` | 886,500.00 USD | 823.29 USD | 0.00 USD | `+78.65%` | `56.14` |
| `Live` | `Short` | `14.96` | 886,740.00 USD | 245.58 USD | 0.00 USD | `+82.30%` | `16.41` |
| `Live` | `Short` | `15.29` | 886,970.00 USD | 229.43 USD | 0.00 USD | `+86.32%` | `15.00` |
| `Live` | `Short` | `15.30` | 887,300.00 USD | 329.82 USD | 0.00 USD | `+86.45%` | `21.55` |
| `Live` | `Short` | `15.35` | 887,530.00 USD | 230.17 USD | 0.00 USD | `+86.93%` | `15.00` |
| `Live` | `Short` | `15.38` | 907,530.00 USD | 20,000.00 USD | 0.00 USD | `+87.42%` | `1,300.00` |
| `Live` | `Short` | `15.44` | 911,820.00 USD | 4,280.00 USD | 0.00 USD | `+88.03%` | `277.54` |
| `Live` | `Short` | `15.63` | 912,380.00 USD | 561.14 USD | 0.00 USD | `+90.47%` | `35.89` |
| `Live` | `Short` | `15.72` | 912,550.00 USD | 167.79 USD | 0.00 USD | `+91.56%` | `10.67` |
| `Live` | `Short` | `15.77` | 912,730.00 USD | 185.55 USD | 0.00 USD | `+92.05%` | `11.77` |
| `Live` | `Short` | `15.79` | 912,990.00 USD | 261.72 USD | 0.00 USD | `+92.29%` | `16.58` |
| `Live` | `Short` | `16.23` | 934,270.00 USD | 21,270.00 USD | 0.00 USD | `+97.65%` | `1,311.22` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 306,040.00 USD | 0.00 USD | 611.73 USD | `-71.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 305,430.00 USD | 0.00 USD | 793.75 USD | `-51.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 304,640.00 USD | 0.00 USD | 105.04 USD | `-45.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 304,530.00 USD | 0.00 USD | 67,970.00 USD | `-39.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 236,570.00 USD | 0.00 USD | 205.30 USD | `-35.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 236,360.00 USD | 0.00 USD | 465.42 USD | `-33.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 235,900.00 USD | 0.00 USD | 349.35 USD | `-32.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 235,550.00 USD | 0.00 USD | 1,020.00 USD | `-32.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 234,530.00 USD | 0.00 USD | 1,330.00 USD | `-29.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 233,200.00 USD | 0.00 USD | 493.50 USD | `-27.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 232,710.00 USD | 0.00 USD | 100.98 USD | `-27.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 232,610.00 USD | 0.00 USD | 500.70 USD | `-26.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 232,110.00 USD | 0.00 USD | 4,160.00 USD | `-25.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 227,950.00 USD | 0.00 USD | 6,500.00 USD | `-24.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.21` | 221,450.00 USD | 0.00 USD | 906.18 USD | `-24.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.25` | 220,540.00 USD | 0.00 USD | 127.35 USD | `-23.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 220,420.00 USD | 0.00 USD | 864.38 USD | `-23.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 219,550.00 USD | 0.00 USD | 130.10 USD | `-20.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 219,420.00 USD | 0.00 USD | 4,340.00 USD | `-20.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 215,080.00 USD | 0.00 USD | 5,520.00 USD | `-18.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 209,560.00 USD | 0.00 USD | 100.72 USD | `-18.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 209,460.00 USD | 0.00 USD | 296.34 USD | `-17.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 209,160.00 USD | 0.00 USD | 921.19 USD | `-17.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 208,240.00 USD | 0.00 USD | 709.98 USD | `-16.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 207,530.00 USD | 0.00 USD | 1,380.00 USD | `-15.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 206,150.00 USD | 0.00 USD | 262.44 USD | `-15.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 205,880.00 USD | 0.00 USD | 24,350.00 USD | `-14.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.11` | 181,530.00 USD | 0.00 USD | 187.79 USD | `-13.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 181,340.00 USD | 0.00 USD | 6,790.00 USD | `-12.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 174,560.00 USD | 0.00 USD | 9,770.00 USD | `-12.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.21` | 164,790.00 USD | 0.00 USD | 7,210.00 USD | `-12.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 157,580.00 USD | 0.00 USD | 282.74 USD | `-11.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 157,300.00 USD | 0.00 USD | 603.44 USD | `-11.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 156,700.00 USD | 0.00 USD | 464.61 USD | `-11.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 156,230.00 USD | 0.00 USD | 2,090.00 USD | `-11.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 154,140.00 USD | 0.00 USD | 129.58 USD | `-10.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 154,010.00 USD | 0.00 USD | 114.65 USD | `-10.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.39` | 153,890.00 USD | 0.00 USD | 702.75 USD | `-9.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.41` | 153,190.00 USD | 0.00 USD | 4,630.00 USD | `-9.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 148,560.00 USD | 0.00 USD | 199.39 USD | `-9.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 148,360.00 USD | 0.00 USD | 6,270.00 USD | `-8.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 142,090.00 USD | 0.00 USD | 37,420.00 USD | `-8.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 104,670.00 USD | 0.00 USD | 2,120.00 USD | `-8.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 102,550.00 USD | 0.00 USD | 799.83 USD | `-8.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 101,750.00 USD | 0.00 USD | 820.44 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 100,930.00 USD | 0.00 USD | 103.41 USD | `-7.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 100,820.00 USD | 0.00 USD | 113.78 USD | `-7.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 100,710.00 USD | 0.00 USD | 297.59 USD | `-7.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.68` | 100,410.00 USD | 0.00 USD | 528.88 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 99,880.00 USD | 0.00 USD | 360.13 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 99,520.00 USD | 0.00 USD | 578.04 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.79` | 98,950.00 USD | 0.00 USD | 424.05 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 98,520.00 USD | 0.00 USD | 23,790.00 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.82` | 74,740.00 USD | 0.00 USD | 3,940.00 USD | `-4.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 70,800.00 USD | 0.00 USD | 115.23 USD | `-4.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 70,680.00 USD | 0.00 USD | 183.33 USD | `-4.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.88` | 70,500.00 USD | 0.00 USD | 194.52 USD | `-3.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 70,300.00 USD | 0.00 USD | 2,290.00 USD | `-3.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 68,010.00 USD | 0.00 USD | 6,520.00 USD | `-3.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 61,500.00 USD | 0.00 USD | 5,710.00 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 55,790.00 USD | 0.00 USD | 1,590.00 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 54,210.00 USD | 0.00 USD | 898.42 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 53,310.00 USD | 0.00 USD | 7,960.00 USD | `-3.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 45,350.00 USD | 0.00 USD | 9,160.00 USD | `-2.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 36,190.00 USD | 0.00 USD | 3,430.00 USD | `-2.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 32,760.00 USD | 0.00 USD | 123.58 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 32,630.00 USD | 0.00 USD | 2,110.00 USD | `-2.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 30,520.00 USD | 0.00 USD | 152.56 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.06` | 30,370.00 USD | 0.00 USD | 2,730.00 USD | `-1.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 27,640.00 USD | 0.00 USD | 121.69 USD | `-1.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 27,520.00 USD | 0.00 USD | 477.36 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 27,040.00 USD | 0.00 USD | 924.78 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 26,120.00 USD | 0.00 USD | 1,140.00 USD | `-1.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 24,980.00 USD | 0.00 USD | 6,500.00 USD | `-1.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 18,480.00 USD | 0.00 USD | 884.60 USD | `-0.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 17,590.00 USD | 0.00 USD | 5,550.00 USD | `-0.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 12,040.00 USD | 0.00 USD | 1,430.00 USD | `-0.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 10,600.00 USD | 0.00 USD | 3,080.00 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 7,520.00 USD | 0.00 USD | 520.75 USD | `-0.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 7,000.00 USD | 0.00 USD | 3,020.00 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 3,980.00 USD | 0.00 USD | 141.04 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 3,840.00 USD | 0.00 USD | 3,840.00 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 515.66 USD | 515.66 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.23` | 1,540.00 USD | 1,030.00 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.24` | 5,050.00 USD | 3,510.00 USD | 0.00 USD | `+0.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.26` | 14,170.00 USD | 9,110.00 USD | 0.00 USD | `+0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.27` | 14,520.00 USD | 353.00 USD | 0.00 USD | `+0.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.28` | 14,930.00 USD | 408.78 USD | 0.00 USD | `+0.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.29` | 15,130.00 USD | 201.49 USD | 0.00 USD | `+0.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.29` | 19,280.00 USD | 4,150.00 USD | 0.00 USD | `+1.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.30` | 19,520.00 USD | 242.42 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.31` | 22,440.00 USD | 2,920.00 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.32` | 24,130.00 USD | 1,690.00 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.34` | 24,540.00 USD | 408.58 USD | 0.00 USD | `+1.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.35` | 25,290.00 USD | 756.06 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.36` | 26,260.00 USD | 970.35 USD | 0.00 USD | `+1.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 26,770.00 USD | 503.59 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 27,190.00 USD | 419.25 USD | 0.00 USD | `+2.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 29,150.00 USD | 1,970.00 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 29,480.00 USD | 328.55 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.41` | 29,800.00 USD | 314.81 USD | 0.00 USD | `+2.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.43` | 31,680.00 USD | 1,880.00 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.44` | 31,990.00 USD | 307.54 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.45` | 32,130.00 USD | 138.24 USD | 0.00 USD | `+2.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 32,840.00 USD | 710.81 USD | 0.00 USD | `+3.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.47` | 33,610.00 USD | 769.61 USD | 0.00 USD | `+3.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.48` | 33,750.00 USD | 146.79 USD | 0.00 USD | `+3.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.49` | 35,170.00 USD | 1,410.00 USD | 0.00 USD | `+3.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 43,670.00 USD | 8,500.00 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.52` | 44,080.00 USD | 408.55 USD | 0.00 USD | `+3.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.53` | 45,210.00 USD | 1,130.00 USD | 0.00 USD | `+3.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 45,370.00 USD | 162.68 USD | 0.00 USD | `+3.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 49,770.00 USD | 4,400.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.55` | 50,020.00 USD | 243.82 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.56` | 51,620.00 USD | 1,600.00 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.57` | 53,040.00 USD | 1,420.00 USD | 0.00 USD | `+4.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.60` | 54,170.00 USD | 1,130.00 USD | 0.00 USD | `+4.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 54,920.00 USD | 751.56 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 56,410.00 USD | 1,490.00 USD | 0.00 USD | `+4.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 60,590.00 USD | 4,180.00 USD | 0.00 USD | `+5.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 60,800.00 USD | 201.97 USD | 0.00 USD | `+5.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 60,900.00 USD | 103.31 USD | 0.00 USD | `+5.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 61,010.00 USD | 107.84 USD | 0.00 USD | `+5.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 61,120.00 USD | 107.97 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 61,290.00 USD | 176.62 USD | 0.00 USD | `+5.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 62,280.00 USD | 990.09 USD | 0.00 USD | `+5.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 67,290.00 USD | 5,010.00 USD | 0.00 USD | `+5.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 67,870.00 USD | 575.14 USD | 0.00 USD | `+6.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 68,270.00 USD | 399.67 USD | 0.00 USD | `+6.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 69,090.00 USD | 819.28 USD | 0.00 USD | `+6.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 69,420.00 USD | 333.07 USD | 0.00 USD | `+6.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 73,790.00 USD | 4,370.00 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 75,570.00 USD | 1,780.00 USD | 0.00 USD | `+6.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 115,380.00 USD | 39,810.00 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 115,590.00 USD | 215.16 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 115,980.00 USD | 388.12 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 116,690.00 USD | 711.78 USD | 0.00 USD | `+7.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 117,260.00 USD | 563.87 USD | 0.00 USD | `+7.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.82` | 119,290.00 USD | 2,030.00 USD | 0.00 USD | `+7.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 119,530.00 USD | 243.40 USD | 0.00 USD | `+7.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 125,300.00 USD | 5,760.00 USD | 0.00 USD | `+7.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 125,530.00 USD | 234.04 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 125,700.00 USD | 163.91 USD | 0.00 USD | `+7.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 125,810.00 USD | 110.58 USD | 0.00 USD | `+8.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 126,910.00 USD | 1,100.00 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 128,840.00 USD | 1,930.00 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 129,630.00 USD | 788.72 USD | 0.00 USD | `+8.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 131,440.00 USD | 1,800.00 USD | 0.00 USD | `+8.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 131,600.00 USD | 163.33 USD | 0.00 USD | `+8.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 161,120.00 USD | 29,520.00 USD | 0.00 USD | `+8.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 161,350.00 USD | 223.62 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 161,530.00 USD | 180.53 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 161,930.00 USD | 401.63 USD | 0.00 USD | `+9.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 477,080.00 USD | 315,150.00 USD | 0.00 USD | `+9.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 477,180.00 USD | 104.59 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 477,450.00 USD | 262.56 USD | 0.00 USD | `+9.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 477,580.00 USD | 130.03 USD | 0.00 USD | `+9.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 478,950.00 USD | 1,380.00 USD | 0.00 USD | `+9.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 480,040.00 USD | 1,090.00 USD | 0.00 USD | `+9.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 480,660.00 USD | 616.37 USD | 0.00 USD | `+10.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 480,760.00 USD | 102.03 USD | 0.00 USD | `+10.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 481,210.00 USD | 453.84 USD | 0.00 USD | `+10.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 481,380.00 USD | 160.99 USD | 0.00 USD | `+10.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 481,790.00 USD | 415.00 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 483,300.00 USD | 1,510.00 USD | 0.00 USD | `+10.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 483,910.00 USD | 606.18 USD | 0.00 USD | `+10.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 484,090.00 USD | 182.10 USD | 0.00 USD | `+10.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 488,650.00 USD | 4,560.00 USD | 0.00 USD | `+11.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 488,810.00 USD | 166.53 USD | 0.00 USD | `+11.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 490,810.00 USD | 2,000.00 USD | 0.00 USD | `+11.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 885,030.00 USD | 394,210.00 USD | 0.00 USD | `+11.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 885,140.00 USD | 119.24 USD | 0.00 USD | `+11.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.20` | 886,740.00 USD | 1,590.00 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 889,400.00 USD | 2,660.00 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 889,530.00 USD | 131.87 USD | 0.00 USD | `+12.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 889,680.00 USD | 149.17 USD | 0.00 USD | `+12.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 891,890.00 USD | 2,220.00 USD | 0.00 USD | `+12.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,120,000.00 USD | 231,380.00 USD | 0.00 USD | `+12.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,130,000.00 USD | 1,960.00 USD | 0.00 USD | `+12.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,130,000.00 USD | 434.45 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,140,000.00 USD | 18,610.00 USD | 0.00 USD | `+13.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,140,000.00 USD | 166.83 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,140,000.00 USD | 150.79 USD | 0.00 USD | `+13.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,140,000.00 USD | 101.58 USD | 0.00 USD | `+13.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,140,000.00 USD | 109.36 USD | 0.00 USD | `+13.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,140,000.00 USD | 116.69 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,150,000.00 USD | 163.41 USD | 0.00 USD | `+14.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,150,000.00 USD | 1,150.00 USD | 0.00 USD | `+14.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,150,000.00 USD | 660.84 USD | 0.00 USD | `+14.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,150,000.00 USD | 714.59 USD | 0.00 USD | `+14.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,150,000.00 USD | 928.13 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,150,000.00 USD | 102.45 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,150,000.00 USD | 219.84 USD | 0.00 USD | `+14.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,150,000.00 USD | 1,890.00 USD | 0.00 USD | `+15.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.47` | 1,150,000.00 USD | 1,780.00 USD | 0.00 USD | `+15.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,150,000.00 USD | 1,130.00 USD | 0.00 USD | `+15.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,150,000.00 USD | 288.46 USD | 0.00 USD | `+15.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,150,000.00 USD | 119.92 USD | 0.00 USD | `+16.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,150,000.00 USD | 231.00 USD | 0.00 USD | `+16.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,150,000.00 USD | 221.07 USD | 0.00 USD | `+16.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,160,000.00 USD | 992.00 USD | 0.00 USD | `+17.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,160,000.00 USD | 148.48 USD | 0.00 USD | `+17.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,160,000.00 USD | 191.36 USD | 0.00 USD | `+17.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,160,000.00 USD | 4,440.00 USD | 0.00 USD | `+17.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,160,000.00 USD | 108.21 USD | 0.00 USD | `+18.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,160,000.00 USD | 169.68 USD | 0.00 USD | `+18.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,160,000.00 USD | 574.66 USD | 0.00 USD | `+18.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,160,000.00 USD | 121.87 USD | 0.00 USD | `+18.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,160,000.00 USD | 115.88 USD | 0.00 USD | `+19.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,160,000.00 USD | 340.05 USD | 0.00 USD | `+20.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,160,000.00 USD | 742.12 USD | 0.00 USD | `+20.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,160,000.00 USD | 899.47 USD | 0.00 USD | `+20.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,230,000.00 USD | 70,020.00 USD | 0.00 USD | `+20.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,230,000.00 USD | 373.97 USD | 0.00 USD | `+20.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,240,000.00 USD | 5,050.00 USD | 0.00 USD | `+21.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,250,000.00 USD | 6,370.00 USD | 0.00 USD | `+22.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,250,000.00 USD | 404.20 USD | 0.00 USD | `+23.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,460,000.00 USD | 210,980.00 USD | 0.00 USD | `+23.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,460,000.00 USD | 1,150.00 USD | 0.00 USD | `+23.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,460,000.00 USD | 172.16 USD | 0.00 USD | `+24.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,460,000.00 USD | 895.21 USD | 0.00 USD | `+25.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,460,000.00 USD | 489.40 USD | 0.00 USD | `+25.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,460,000.00 USD | 1,200.00 USD | 0.00 USD | `+26.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,460,000.00 USD | 118.01 USD | 0.00 USD | `+27.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.47` | 1,460,000.00 USD | 818.31 USD | 0.00 USD | `+27.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,460,000.00 USD | 312.31 USD | 0.00 USD | `+27.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,460,000.00 USD | 2,290.00 USD | 0.00 USD | `+28.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,460,000.00 USD | 178.46 USD | 0.00 USD | `+28.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,460,000.00 USD | 173.42 USD | 0.00 USD | `+30.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,460,000.00 USD | 184.75 USD | 0.00 USD | `+30.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,460,000.00 USD | 135.78 USD | 0.00 USD | `+31.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,460,000.00 USD | 127.96 USD | 0.00 USD | `+31.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,470,000.00 USD | 476.43 USD | 0.00 USD | `+32.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,470,000.00 USD | 869.35 USD | 0.00 USD | `+32.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,470,000.00 USD | 118.97 USD | 0.00 USD | `+32.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,470,000.00 USD | 251.06 USD | 0.00 USD | `+33.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,470,000.00 USD | 552.44 USD | 0.00 USD | `+33.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,470,000.00 USD | 537.26 USD | 0.00 USD | `+34.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,470,000.00 USD | 320.29 USD | 0.00 USD | `+35.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,470,000.00 USD | 1,100.00 USD | 0.00 USD | `+36.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,470,000.00 USD | 2,270.00 USD | 0.00 USD | `+36.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,470,000.00 USD | 1,270.00 USD | 0.00 USD | `+37.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,470,000.00 USD | 1,380.00 USD | 0.00 USD | `+38.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,480,000.00 USD | 2,410.00 USD | 0.00 USD | `+38.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,490,000.00 USD | 9,520.00 USD | 0.00 USD | `+39.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 1,490,000.00 USD | 2,050.00 USD | 0.00 USD | `+39.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,490,000.00 USD | 529.11 USD | 0.00 USD | `+40.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,500,000.00 USD | 7,700.00 USD | 0.00 USD | `+41.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,500,000.00 USD | 906.03 USD | 0.00 USD | `+44.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,500,000.00 USD | 434.61 USD | 0.00 USD | `+44.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,500,000.00 USD | 163.52 USD | 0.00 USD | `+44.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 1,510,000.00 USD | 10,370.00 USD | 0.00 USD | `+46.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.19` | 1,510,000.00 USD | 5,270.00 USD | 0.00 USD | `+48.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 1,520,000.00 USD | 3,350.00 USD | 0.00 USD | `+54.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 1,520,000.00 USD | 197.97 USD | 0.00 USD | `+55.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 1,520,000.00 USD | 3,200.00 USD | 0.00 USD | `+57.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 1,520,000.00 USD | 179.58 USD | 0.00 USD | `+58.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 1,520,000.00 USD | 568.45 USD | 0.00 USD | `+58.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 1,520,000.00 USD | 169.57 USD | 0.00 USD | `+60.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 1,520,000.00 USD | 446.52 USD | 0.00 USD | `+62.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 1,530,000.00 USD | 5,320.00 USD | 0.00 USD | `+64.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 1,740,000.00 USD | 210,750.00 USD | 0.00 USD | `+64.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 1,740,000.00 USD | 407.95 USD | 0.00 USD | `+66.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 1,740,000.00 USD | 174.91 USD | 0.00 USD | `+68.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 1,740,000.00 USD | 4,650.00 USD | 0.00 USD | `+70.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 1,740,000.00 USD | 960.26 USD | 0.00 USD | `+73.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 1,750,000.00 USD | 2,710.00 USD | 0.00 USD | `+74.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 1,750,000.00 USD | 805.90 USD | 0.00 USD | `+76.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 1,750,000.00 USD | 655.55 USD | 0.00 USD | `+79.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 1,750,000.00 USD | 4,890.00 USD | 0.00 USD | `+80.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 1,750,000.00 USD | 471.09 USD | 0.00 USD | `+81.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 1,750,000.00 USD | 383.85 USD | 0.00 USD | `+82.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,410,000.00 USD | 653,420.00 USD | 0.00 USD | `+82.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 2,410,000.00 USD | 3,010.00 USD | 0.00 USD | `+83.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,410,000.00 USD | 111.87 USD | 0.00 USD | `+93.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,410,000.00 USD | 219.91 USD | 0.00 USD | `+94.97%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.36` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 6,810.00 USD | 2,430.00 USD | 0.00 USD |
| `7D` | `7.40` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 6,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.42` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 48.44 USD |
| `1D` | `7.44` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 196.00 USD | 0.00 USD | 18,000.00 USD |
| `7D` | `7.44` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 331.70 USD | 1,680.00 USD | 0.00 USD |
| `1D` | `7.46` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 7,860.00 USD | 0.00 USD | 52,720.00 USD |
| `7D` | `7.46` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 0.00 USD | 1,410.00 USD | 24,000.00 USD |
| `1D` | `7.48` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 11,780.00 USD |
| `7D` | `7.48` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 9,120.00 USD | 0.00 USD | 20,570.00 USD |
| `1D` | `7.50` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 717.40 USD | 4,920.00 USD | 24,120.00 USD |
| `1D` | `7.52` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 26,110.00 USD | 9,580.00 USD | 36,310.00 USD |
| `7D` | `7.52` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,150.00 USD | 14,470.00 USD | 18,280.00 USD |
| `7D` | `7.54` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 0.00 USD | 4,450.00 USD | 0.00 USD |
| `1D` | `7.56` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 15,020.00 USD | 4,270.00 USD | 3,020.00 USD |
| `7D` | `7.56` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 19,530.00 USD | 4,310.00 USD | 0.00 USD |
| `1D` | `7.58` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 147.02 USD |
| `1D` | `7.60` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 405.20 USD | 3,770.00 USD | 194.10 USD |
| `1D` | `7.62` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 583.80 USD | 0.00 USD | 11,670.00 USD |
| `1D` | `7.64` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 17,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.64` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 812.40 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.66` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 9,430.00 USD |
| `7D` | `7.66` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 23,280.00 USD |
| `7D` | `7.68` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD |
| `1D` | `7.70` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 321.75 USD | 2,390.00 USD | 14,120.00 USD |
| `1D` | `7.72` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 4,600.00 USD | 1,630.00 USD | 12,390.00 USD |
| `7D` | `7.72` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 32,590.00 USD |
| `1D` | `7.74` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 3,340.00 USD | 4,580.00 USD | 2,590.00 USD |
| `7D` | `7.74` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 976.80 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.76` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 1,660.00 USD | 1,100.00 USD | 5,380.00 USD |
| `7D` | `7.76` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 812.95 USD | 5,760.00 USD | 0.00 USD |
| `1D` | `7.78` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 44,950.00 USD | 3,730.00 USD | 8,950.00 USD |
| `7D` | `7.78` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 43,620.00 USD | 4,900.00 USD | 20,580.00 USD |
| `1D` | `7.80` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 39,070.00 USD | 10,860.00 USD | 8,320.00 USD |
| `7D` | `7.80` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 14,770.00 USD | 12,980.00 USD | 0.00 USD |
| `1D` | `7.82` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 5,100.00 USD | 7,610.00 USD | 5,600.00 USD |
| `7D` | `7.82` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,330.00 USD |
| `1D` | `7.84` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 2,680.00 USD | 4,910.00 USD | 12,620.00 USD |
| `7D` | `7.84` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 30,950.00 USD | 2,380.00 USD | 25,490.00 USD |
| `1D` | `7.86` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 15,790.00 USD | 1,680.00 USD | 16,520.00 USD |
| `7D` | `7.86` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD |
| `1D` | `7.88` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 46,100.00 USD | 9,570.00 USD | 22,860.00 USD |
| `7D` | `7.88` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 58,120.00 USD | 12,780.00 USD | 29,720.00 USD |
| `1D` | `7.90` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 14,350.00 USD | 7,630.00 USD | 7,820.00 USD |
| `7D` | `7.90` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,500.00 USD |
| `1D` | `7.92` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 24,660.00 USD | 2,950.00 USD | 6,190.00 USD |
| `7D` | `7.92` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 55,490.00 USD | 8,420.00 USD | 15,500.00 USD |
| `1D` | `7.94` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 20,330.00 USD | 6,860.00 USD | 48,360.00 USD |
| `7D` | `7.94` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,780.00 USD |
| `1D` | `7.96` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 20,670.00 USD | 11,220.00 USD | 149,000.00 USD |
| `7D` | `7.96` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 21,840.00 USD | 6,920.00 USD | 86,150.00 USD |
| `1D` | `7.98` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 17,030.00 USD | 3,300.00 USD | 37,760.00 USD |
| `7D` | `7.98` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 56,660.00 USD | 26,790.00 USD | 146,520.00 USD |
| `1D` | `8.00` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 1,500.00 USD | 22,850.00 USD | 62,450.00 USD |
| `7D` | `8.00` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,470.00 USD |
| `1D` | `8.02` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 81,330.00 USD | 10,580.00 USD | 82,920.00 USD |
| `7D` | `8.02` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 20,910.00 USD | 46,670.00 USD | 56,400.00 USD |
| `1D` | `8.04` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 33,700.00 USD | 17,810.00 USD | 15,050.00 USD |
| `7D` | `8.04` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 152,340.00 USD | 56,910.00 USD | 86,510.00 USD |
| `1D` | `8.06` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 76,840.00 USD | 22,300.00 USD | 19,110.00 USD |
| `7D` | `8.06` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 122,100.00 USD | 20,850.00 USD | 86,210.00 USD |
| `1D` | `8.08` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 36,720.00 USD | 6,070.00 USD | 13,010.00 USD |
| `7D` | `8.08` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,570.00 USD |
| `1D` | `8.10` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 30,110.00 USD | 14,390.00 USD | 96,600.00 USD |
| `7D` | `8.10` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 61,500.00 USD | 19,700.00 USD | 15,580.00 USD |
| `1D` | `8.12` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 110,990.00 USD | 12,270.00 USD | 319,110.00 USD |
| `7D` | `8.12` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 27,520.00 USD | 10,810.00 USD | 142,650.00 USD |
| `1D` | `8.14` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 12,410.00 USD | 0.00 USD | 58,600.00 USD |
| `7D` | `8.14` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 72,460.00 USD | 25,370.00 USD | 192,000.00 USD |
| `1D` | `8.16` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 44,830.00 USD | 42,030.00 USD | 159,250.00 USD |
| `7D` | `8.16` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 38,430.00 USD | 5,510.00 USD | 30,350.00 USD |
| `1D` | `8.18` | 864,670.00 USD | 0.00 USD | 864,670.00 USD | 133,120.00 USD | 19,620.00 USD | 175,960.00 USD |
| `7D` | `8.18` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 39,830.00 USD | 43,260.00 USD | 176,600.00 USD |
| `1D` | `8.20` | 535,970.00 USD | 0.00 USD | 535,970.00 USD | 33,560.00 USD | 32,530.00 USD | 17,200.00 USD |
| `7D` | `8.20` | 817,140.00 USD | 0.00 USD | 817,140.00 USD | 92,320.00 USD | 58,100.00 USD | 8,420.00 USD |
| `1D` | `8.22` | 452,680.00 USD | 0.00 USD | 452,680.00 USD | 32,330.00 USD | 39,650.00 USD | 35,310.00 USD |
| `7D` | `8.22` | 658,310.00 USD | 0.00 USD | 658,310.00 USD | 117,230.00 USD | 21,570.00 USD | 10,950.00 USD |
| `1D` | `8.24` | 345,380.00 USD | 0.00 USD | 345,380.00 USD | 163,080.00 USD | 10,300.00 USD | 69,390.00 USD |
| `7D` | `8.24` | 508,550.00 USD | 0.00 USD | 508,550.00 USD | 39,950.00 USD | 3,480.00 USD | 107,710.00 USD |
| `1D` | `8.26` | 102,620.00 USD | 0.00 USD | 102,620.00 USD | 15,150.00 USD | 15,590.00 USD | 16,620.00 USD |
| `7D` | `8.26` | 357,410.00 USD | 0.00 USD | 357,410.00 USD | 30,490.00 USD | 5,750.00 USD | 1,870.00 USD |
| `1D` | `8.28` | 55,260.00 USD | 0.00 USD | 55,260.00 USD | 0.00 USD | 0.00 USD | 57.32 USD |
| `7D` | `8.28` | 319,300.00 USD | 0.00 USD | 319,300.00 USD | 122,850.00 USD | 0.00 USD | 1,170.00 USD |
| `7D` | `8.30` | 195,270.00 USD | 0.00 USD | 195,270.00 USD | 152,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.32` | 55,210.00 USD | 0.00 USD | 55,210.00 USD | 55,190.00 USD | 0.00 USD | 16.44 USD |
| `7D` | `8.32` | 42,900.00 USD | 0.00 USD | 42,900.00 USD | 42,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.34` | 122.98 USD | 122.98 USD | 0.00 USD | 0.00 USD | 0.00 USD | 122.98 USD |
| `1D` | `8.34` | 245.96 USD | 245.96 USD | 0.00 USD | 0.00 USD | 0.00 USD | 122.98 USD |
| `7D` | `8.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.36` | 263.76 USD | 263.76 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17.80 USD |
| `7D` | `8.36` | 14,290.00 USD | 14,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `8.38` | 1,020.00 USD | 1,020.00 USD | 0.00 USD | 691.75 USD | 0.00 USD | 64.64 USD |
| `7D` | `8.38` | 73,260.00 USD | 73,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 58,970.00 USD |
| `7D` | `8.40` | 108,990.00 USD | 108,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 35,730.00 USD |
| `1D` | `8.42` | 1,810.00 USD | 1,810.00 USD | 0.00 USD | 788.46 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.42` | 128,030.00 USD | 128,030.00 USD | 0.00 USD | 16,070.00 USD | 0.00 USD | 2,970.00 USD |
| `1D` | `8.44` | 91,790.00 USD | 91,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 89,980.00 USD |
| `7D` | `8.44` | 138,510.00 USD | 138,510.00 USD | 0.00 USD | 10,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.46` | 419,730.00 USD | 419,730.00 USD | 0.00 USD | 35,680.00 USD | 4,700.00 USD | 287,550.00 USD |
| `7D` | `8.46` | 623,300.00 USD | 623,300.00 USD | 0.00 USD | 365,050.00 USD | 0.00 USD | 119,740.00 USD |
| `1D` | `8.48` | 517,470.00 USD | 517,470.00 USD | 0.00 USD | 0.00 USD | 39,180.00 USD | 58,560.00 USD |
| `7D` | `8.48` | 825,140.00 USD | 825,140.00 USD | 0.00 USD | 0.00 USD | 49,360.00 USD | 152,480.00 USD |
| `1D` | `8.50` | 805,570.00 USD | 805,570.00 USD | 0.00 USD | 66,120.00 USD | 101,350.00 USD | 120,630.00 USD |
| `7D` | `8.50` | 925,210.00 USD | 925,210.00 USD | 0.00 USD | 0.00 USD | 100,070.00 USD | 0.00 USD |
| `1D` | `8.52` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 203,080.00 USD | 69,980.00 USD | 164,800.00 USD |
| `7D` | `8.52` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 2,990.00 USD | 135,400.00 USD | 91,380.00 USD |
| `1D` | `8.54` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 61,500.00 USD | 32,530.00 USD | 16,750.00 USD |
| `7D` | `8.54` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 71,540.00 USD | 136,470.00 USD | 0.00 USD |
| `1D` | `8.56` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 183,280.00 USD | 33,670.00 USD | 0.00 USD |
| `7D` | `8.56` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 691,140.00 USD | 122,650.00 USD | 0.00 USD |
| `1D` | `8.58` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 234,090.00 USD | 5,060.00 USD | 179,360.00 USD |
| `7D` | `8.58` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 599,490.00 USD | 164,810.00 USD | 0.00 USD |
| `1D` | `8.60` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 57,190.00 USD | 120,500.00 USD |
| `7D` | `8.60` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 75,040.00 USD | 39,160.00 USD | 388.58 USD |
| `1D` | `8.62` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 83,560.00 USD | 57,150.00 USD | 201,890.00 USD |
| `7D` | `8.62` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 43,670.00 USD | 87,180.00 USD |
| `1D` | `8.64` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 89,460.00 USD | 30,330.00 USD | 29,280.00 USD |
| `7D` | `8.64` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 12,800.00 USD | 76,240.00 USD |
| `1D` | `8.66` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 78,620.00 USD | 21,010.00 USD | 108,320.00 USD |
| `7D` | `8.66` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 16,520.00 USD | 281.77 USD |
| `1D` | `8.68` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 65,090.00 USD | 9,810.00 USD | 212,540.00 USD |
| `7D` | `8.68` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 207,090.00 USD | 43,100.00 USD | 334,680.00 USD |
| `1D` | `8.70` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 50,130.00 USD | 16,260.00 USD | 30,560.00 USD |
| `7D` | `8.70` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 29,260.00 USD | 41,840.00 USD | 46,400.00 USD |
| `1D` | `8.72` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 18,250.00 USD | 0.00 USD | 50,740.00 USD |
| `1D` | `8.74` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 49,310.00 USD | 28,810.00 USD | 12,900.00 USD |
| `7D` | `8.74` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 48,810.00 USD | 30,470.00 USD | 0.00 USD |
| `1D` | `8.76` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 112,960.00 USD | 2,530.00 USD | 9,800.00 USD |
| `7D` | `8.76` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,980.00 USD |
| `1D` | `8.78` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 108,350.00 USD | 11,500.00 USD | 35,600.00 USD |
| `7D` | `8.78` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 2,300.00 USD | 0.00 USD | 58,840.00 USD |
| `1D` | `8.80` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 125,120.00 USD | 22,330.00 USD | 52,850.00 USD |
| `7D` | `8.80` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 27,360.00 USD | 33,750.00 USD | 31,560.00 USD |
| `1D` | `8.82` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 19,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.82` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 103,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.84` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 40,640.00 USD | 8,820.00 USD | 73,730.00 USD |
| `1D` | `8.86` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 13,620.00 USD | 2,250.00 USD | 11,350.00 USD |
| `7D` | `8.86` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 29,310.00 USD | 0.00 USD | 81,960.00 USD |
| `1D` | `8.88` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 1,320.00 USD | 8,950.00 USD | 186.36 USD |
| `7D` | `8.88` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD |
| `1D` | `8.90` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 31,860.00 USD | 8,140.00 USD | 122,600.00 USD |
| `7D` | `8.90` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 2,440.00 USD | 0.00 USD | 115,910.00 USD |
| `1D` | `8.92` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 40,710.00 USD | 7,360.00 USD | 17,020.00 USD |
| `7D` | `8.92` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 1,730.00 USD | 0.00 USD | 17,620.00 USD |
| `1D` | `8.94` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 41,740.00 USD | 12,260.00 USD | 17,500.00 USD |
| `7D` | `8.94` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 58,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.96` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 2,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.96` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD | 432.56 USD |
| `1D` | `8.98` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 25,040.00 USD | 5,550.00 USD | 19,670.00 USD |
| `7D` | `8.98` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,090.00 USD |
| `1D` | `9.00` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 85,360.00 USD | 30,520.00 USD | 11,400.00 USD |
| `7D` | `9.00` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 297,650.00 USD | 11,360.00 USD | 20,780.00 USD |
| `1D` | `9.02` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 40,920.00 USD | 43,160.00 USD | 18,840.00 USD |
| `7D` | `9.02` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 34,650.00 USD | 56,120.00 USD | 425.46 USD |
| `1D` | `9.04` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 87,540.00 USD | 43,590.00 USD | 38,730.00 USD |
| `7D` | `9.04` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 90,520.00 USD | 74,750.00 USD | 15,140.00 USD |
| `1D` | `9.06` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 35,620.00 USD | 33,420.00 USD | 60,040.00 USD |
| `7D` | `9.06` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD |
| `1D` | `9.08` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 28,800.00 USD | 29,710.00 USD | 70,940.00 USD |
| `7D` | `9.08` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD |
| `1D` | `9.10` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 197,760.00 USD | 43,240.00 USD | 81,020.00 USD |
| `7D` | `9.10` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 826,500.00 USD | 35,760.00 USD | 334,340.00 USD |
| `1D` | `9.12` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 167,130.00 USD | 47,350.00 USD | 108,750.00 USD |
| `7D` | `9.12` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 490,020.00 USD | 24,170.00 USD | 503,470.00 USD |
| `1D` | `9.14` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 118,520.00 USD | 23,510.00 USD | 79,110.00 USD |
| `7D` | `9.14` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 536,560.00 USD | 18,540.00 USD | 500,920.00 USD |
| `1D` | `9.16` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 121,810.00 USD | 44,640.00 USD | 63,950.00 USD |
| `7D` | `9.16` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 358,370.00 USD | 44,360.00 USD | 195,690.00 USD |
| `1D` | `9.18` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 174,230.00 USD | 44,900.00 USD | 105,630.00 USD |
| `7D` | `9.18` | 10,340,000.00 USD | 10,340,000.00 USD | 0.00 USD | 565,140.00 USD | 162,460.00 USD | 291,400.00 USD |
| `1D` | `9.20` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 141,410.00 USD | 43,540.00 USD | 51,090.00 USD |
| `7D` | `9.20` | 11,270,000.00 USD | 11,270,000.00 USD | 0.00 USD | 549,250.00 USD | 134,550.00 USD | 238,560.00 USD |
| `1D` | `9.22` | 6,850,000.00 USD | 6,850,000.00 USD | 0.00 USD | 86,390.00 USD | 10,580.00 USD | 13,790.00 USD |
| `7D` | `9.22` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 585,170.00 USD | 144,840.00 USD | 417,600.00 USD |
| `1D` | `9.24` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 47,010.00 USD | 4,270.00 USD | 3,040.00 USD |
| `7D` | `9.24` | 12,980,000.00 USD | 12,980,000.00 USD | 0.00 USD | 335,740.00 USD | 56,410.00 USD | 173,010.00 USD |
| `1D` | `9.26` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 35,150.00 USD | 8,290.00 USD | 9,710.00 USD |
| `7D` | `9.26` | 13,410,000.00 USD | 13,410,000.00 USD | 0.00 USD | 273,920.00 USD | 96,980.00 USD | 61,560.00 USD |
| `1D` | `9.28` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 44,530.00 USD | 10,920.00 USD | 2,780.00 USD |
| `7D` | `9.28` | 14,110,000.00 USD | 14,110,000.00 USD | 0.00 USD | 428,160.00 USD | 103,490.00 USD | 170,240.00 USD |
| `1D` | `9.30` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 59,470.00 USD | 13,560.00 USD | 29,560.00 USD |
| `7D` | `9.30` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 199,810.00 USD | 97,780.00 USD | 263,720.00 USD |
| `1D` | `9.32` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 37,200.00 USD | 4,250.00 USD | 23,760.00 USD |
| `7D` | `9.32` | 15,340,000.00 USD | 15,340,000.00 USD | 0.00 USD | 271,660.00 USD | 59,310.00 USD | 337,810.00 USD |
| `1D` | `9.34` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 40,730.00 USD | 9,520.00 USD | 11,500.00 USD |
| `7D` | `9.34` | 15,670,000.00 USD | 15,670,000.00 USD | 0.00 USD | 204,260.00 USD | 53,150.00 USD | 69,970.00 USD |
| `1D` | `9.36` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 52,470.00 USD | 10,420.00 USD | 33,220.00 USD |
| `7D` | `9.36` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 247,120.00 USD | 73,430.00 USD | 98,250.00 USD |
| `1D` | `9.38` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 29,420.00 USD | 7,320.00 USD | 14,510.00 USD |
| `7D` | `9.38` | 16,620,000.00 USD | 16,620,000.00 USD | 0.00 USD | 383,530.00 USD | 55,400.00 USD | 93,430.00 USD |
| `1D` | `9.40` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 31,880.00 USD | 0.00 USD | 25.34 USD |
| `7D` | `9.40` | 17,020,000.00 USD | 17,020,000.00 USD | 0.00 USD | 234,760.00 USD | 42,520.00 USD | 124,420.00 USD |
| `1D` | `9.42` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 10,810.00 USD | 2,390.00 USD | 14,160.00 USD |
| `7D` | `9.42` | 17,290,000.00 USD | 17,290,000.00 USD | 0.00 USD | 176,920.00 USD | 19,780.00 USD | 71,300.00 USD |
| `1D` | `9.44` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 10,560.00 USD | 1,630.00 USD | 12,410.00 USD |
| `7D` | `9.44` | 17,410,000.00 USD | 17,410,000.00 USD | 0.00 USD | 41,250.00 USD | 19,420.00 USD | 56,590.00 USD |
| `1D` | `9.46` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 4,580.00 USD | 2,430.00 USD |
| `7D` | `9.46` | 17,520,000.00 USD | 17,520,000.00 USD | 0.00 USD | 60,020.00 USD | 29,830.00 USD | 19,240.00 USD |
| `7D` | `9.48` | 17,580,000.00 USD | 17,580,000.00 USD | 0.00 USD | 12,180.00 USD | 27,840.00 USD | 26,460.00 USD |
| `7D` | `9.50` | 17,750,000.00 USD | 17,750,000.00 USD | 0.00 USD | 89,460.00 USD | 33,210.00 USD | 45,830.00 USD |
| `7D` | `9.52` | 17,940,000.00 USD | 17,940,000.00 USD | 0.00 USD | 102,150.00 USD | 29,320.00 USD | 50,930.00 USD |
| `7D` | `9.54` | 18,150,000.00 USD | 18,150,000.00 USD | 0.00 USD | 192,090.00 USD | 25,090.00 USD | 378.07 USD |
| `7D` | `9.56` | 18,260,000.00 USD | 18,260,000.00 USD | 0.00 USD | 88,510.00 USD | 5,260.00 USD | 13,410.00 USD |
| `7D` | `9.58` | 18,340,000.00 USD | 18,340,000.00 USD | 0.00 USD | 35,340.00 USD | 14,530.00 USD | 26,840.00 USD |
| `7D` | `9.60` | 18,400,000.00 USD | 18,400,000.00 USD | 0.00 USD | 38,740.00 USD | 5,460.00 USD | 20,730.00 USD |
| `7D` | `9.62` | 18,480,000.00 USD | 18,480,000.00 USD | 0.00 USD | 70,470.00 USD | 1,540.00 USD | 10,380.00 USD |
| `7D` | `9.64` | 18,560,000.00 USD | 18,560,000.00 USD | 0.00 USD | 35,210.00 USD | 17,650.00 USD | 20,030.00 USD |
| `7D` | `9.66` | 18,630,000.00 USD | 18,630,000.00 USD | 0.00 USD | 37,340.00 USD | 21,280.00 USD | 17,790.00 USD |
| `7D` | `9.68` | 18,740,000.00 USD | 18,740,000.00 USD | 0.00 USD | 68,230.00 USD | 20,310.00 USD | 15,370.00 USD |
| `7D` | `9.70` | 18,860,000.00 USD | 18,860,000.00 USD | 0.00 USD | 77,860.00 USD | 12,990.00 USD | 31,780.00 USD |
| `7D` | `9.72` | 18,960,000.00 USD | 18,960,000.00 USD | 0.00 USD | 70,300.00 USD | 6,920.00 USD | 26,080.00 USD |
| `7D` | `9.74` | 19,010,000.00 USD | 19,010,000.00 USD | 0.00 USD | 21,230.00 USD | 7,200.00 USD | 20,230.00 USD |
| `7D` | `9.76` | 19,110,000.00 USD | 19,110,000.00 USD | 0.00 USD | 35,520.00 USD | 12,480.00 USD | 51,830.00 USD |
| `7D` | `9.78` | 19,190,000.00 USD | 19,190,000.00 USD | 0.00 USD | 65,390.00 USD | 10,300.00 USD | 5,470.00 USD |
| `7D` | `9.80` | 19,250,000.00 USD | 19,250,000.00 USD | 0.00 USD | 18,630.00 USD | 28,440.00 USD | 10,400.00 USD |
| `7D` | `9.82` | 19,490,000.00 USD | 19,490,000.00 USD | 0.00 USD | 121,860.00 USD | 27,860.00 USD | 86,510.00 USD |
| `7D` | `9.84` | 19,520,000.00 USD | 19,520,000.00 USD | 0.00 USD | 9,730.00 USD | 7,850.00 USD | 14,130.00 USD |
| `7D` | `9.86` | 19,650,000.00 USD | 19,650,000.00 USD | 0.00 USD | 58,130.00 USD | 2,210.00 USD | 71,810.00 USD |
| `7D` | `9.88` | 19,690,000.00 USD | 19,690,000.00 USD | 0.00 USD | 7,170.00 USD | 8,710.00 USD | 20,570.00 USD |
| `7D` | `9.90` | 19,780,000.00 USD | 19,780,000.00 USD | 0.00 USD | 55,970.00 USD | 19,700.00 USD | 15,360.00 USD |
| `7D` | `9.92` | 19,830,000.00 USD | 19,830,000.00 USD | 0.00 USD | 27,710.00 USD | 10,810.00 USD | 8,990.00 USD |
| `7D` | `9.94` | 19,960,000.00 USD | 19,960,000.00 USD | 0.00 USD | 69,320.00 USD | 11,150.00 USD | 51,560.00 USD |
| `7D` | `9.96` | 20,000,000.00 USD | 20,000,000.00 USD | 0.00 USD | 29,800.00 USD | 1,360.00 USD | 11,080.00 USD |
| `7D` | `9.98` | 20,030,000.00 USD | 20,030,000.00 USD | 0.00 USD | 840.10 USD | 4,150.00 USD | 29,460.00 USD |
| `7D` | `10.00` | 20,040,000.00 USD | 20,040,000.00 USD | 0.00 USD | 0.00 USD | 6,790.00 USD | 0.00 USD |
| `7D` | `10.02` | 20,080,000.00 USD | 20,080,000.00 USD | 0.00 USD | 16,100.00 USD | 3,650.00 USD | 15,030.00 USD |
| `7D` | `10.04` | 20,090,000.00 USD | 20,090,000.00 USD | 0.00 USD | 1,080.00 USD | 3,590.00 USD | 9,540.00 USD |
| `7D` | `10.06` | 20,110,000.00 USD | 20,110,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD | 17,230.00 USD |
| `7D` | `10.08` | 20,130,000.00 USD | 20,130,000.00 USD | 0.00 USD | 23,580.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `346.05M` | Total OI Tokens: `41,627,751.2 AVAX`
  * 1h OI Change: `+1.77%` | 4h OI Change: `-2.04%` | 24h OI Change: `-8.63%`
  * Exchange Breakdown: Binance=`79.90M` | Bybit=`56.84M` | OKX=`11.48M` | Hyperliquid=`16.14M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-7.09K` | Last 24h: `18.18K` | Last 3d: `59.53K` | Last 7d: `106.20K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0044%` | **USDT OKX** | `0.0062%` |
| **USDT Bybit** | `-0.0203%` | **USDT KuCoin** | `0.0098%` |
| **USDT MEXC** | `0.0041%` | **USDT BingX** | `0.0057%` |
| **USDT Gate** | `-0.0006%` | **USDT Bitget** | `-0.0017%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `50.40%` | `49.60%` | `1.02` | 6,120,000.00 USD |
| `15M` | `Binance` | `52.49%` | `47.51%` | `1.10` | 1,720,000.00 USD |
| `15M` | `OKX` | `60.43%` | `39.57%` | `1.53` | 547,610.00 USD |
| `15M` | `Bybit` | `61.19%` | `38.81%` | `1.58` | 679,230.00 USD |
| `15M` | `KuCoin` | `23.93%` | `76.07%` | `0.31` | 95,540.00 USD |
| `15M` | `Gate` | `39.89%` | `60.11%` | `0.66` | 92,630.00 USD |
| `15M` | `Bitget` | `63.3%` | `36.7%` | `1.72` | 176,650.00 USD |
| `15M` | `BingX` | `24.02%` | `75.98%` | `0.32` | 697,300.00 USD |
| `15M` | `MEXC` | `50.73%` | `49.27%` | `1.03` | 1,740,000.00 USD |
| `15M` | `Bitunix` | `53.91%` | `46.09%` | `1.17` | 118,450.00 USD |
| `15M` | `Hyperliquid` | `70.8%` | `29.2%` | `2.42` | 116,370.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.94%` | `49.06%` | `1.04` | 113,350.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 4,190.00 USD |
| `15M` | `HTX` | `59.84%` | `40.16%` | `1.49` | 11,770.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `29.87%` | `70.13%` | `0.43` | 1,270.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `23.27%` | `76.73%` | `0.30` | 4,610.00 USD |
| `15M` | `Whale Positions` | `52.49%` | `47.51%` | `1.10` | 1,720,000.00 USD |
| `15M` | `Global Accounts` | `50.40%` | `49.60%` | `1.02` | 6,120,000.00 USD |
| `1H` | `AVAX` | `51.17%` | `48.83%` | `1.05` | 46,660,000.00 USD |
| `1H` | `Binance` | `53.88%` | `46.12%` | `1.17` | 17,910,000.00 USD |
| `1H` | `OKX` | `46.35%` | `53.65%` | `0.86` | 3,320,000.00 USD |
| `1H` | `Bybit` | `39.93%` | `60.07%` | `0.66` | 6,840,000.00 USD |
| `1H` | `KuCoin` | `38.49%` | `61.51%` | `0.63` | 305,580.00 USD |
| `1H` | `Gate` | `48.11%` | `51.89%` | `0.93` | 908,530.00 USD |
| `1H` | `Bitget` | `63.08%` | `36.92%` | `1.71` | 2,010,000.00 USD |
| `1H` | `BingX` | `37.12%` | `62.88%` | `0.59` | 1,140,000.00 USD |
| `1H` | `MEXC` | `52.35%` | `47.65%` | `1.10` | 10,430,000.00 USD |
| `1H` | `Bitunix` | `40.88%` | `59.12%` | `0.69` | 1,190,000.00 USD |
| `1H` | `Hyperliquid` | `73.03%` | `26.97%` | `2.71` | 786,310.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.33%` | `51.67%` | `0.94` | 685,130.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `55.9%` | `44.1%` | `1.27` | 199,420.00 USD |
| `1H` | `HTX` | `52.3%` | `47.7%` | `1.10` | 27,880.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `86.35%` | `13.65%` | `6.33` | 729,120.00 USD |
| `1H` | `Aster` | `79.8%` | `20.2%` | `3.95` | 50,360.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `51.02%` | `48.98%` | `1.04` | 133,060.00 USD |
| `1H` | `Whale Positions` | `53.88%` | `46.12%` | `1.17` | 17,910,000.00 USD |
| `1H` | `Global Accounts` | `51.17%` | `48.83%` | `1.05` | 46,660,000.00 USD |
| `4H` | `AVAX` | `49.03%` | `50.97%` | `0.96` | 308,770,000.00 USD |
| `4H` | `Binance` | `50.55%` | `49.45%` | `1.02` | 120,000,000.00 USD |
| `4H` | `OKX` | `49.55%` | `50.45%` | `0.98` | 26,760,000.00 USD |
| `4H` | `Bybit` | `46.01%` | `53.99%` | `0.85` | 32,420,000.00 USD |
| `4H` | `KuCoin` | `41.57%` | `58.43%` | `0.71` | 2,070,000.00 USD |
| `4H` | `Gate` | `48.24%` | `51.76%` | `0.93` | 6,280,000.00 USD |
| `4H` | `Bitget` | `54.06%` | `45.94%` | `1.18` | 12,740,000.00 USD |
| `4H` | `BingX` | `39.71%` | `60.29%` | `0.66` | 6,830,000.00 USD |
| `4H` | `MEXC` | `49.92%` | `50.08%` | `1.00` | 61,160,000.00 USD |
| `4H` | `Bitunix` | `41.51%` | `58.49%` | `0.71` | 11,250,000.00 USD |
| `4H` | `Hyperliquid` | `41.71%` | `58.29%` | `0.72` | 16,380,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.07%` | `51.93%` | `0.93` | 5,320,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `67.54%` | `32.46%` | `2.08` | 1,970,000.00 USD |
| `4H` | `HTX` | `44.31%` | `55.69%` | `0.80` | 154,760.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `62.68%` | `37.32%` | `1.68` | 3,540,000.00 USD |
| `4H` | `Aster` | `51.56%` | `48.44%` | `1.06` | 756,550.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.77%` | `58.23%` | `0.72` | 1,120,000.00 USD |
| `4H` | `Whale Positions` | `50.55%` | `49.45%` | `1.02` | 120,000,000.00 USD |
| `4H` | `Global Accounts` | `49.03%` | `50.97%` | `0.96` | 308,770,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `8.11` | `8.09` | `8.11` | `8.17` | `7.99` | 4,144,943.56 USD | 2,123,682.88 USD | 2,021,260.68 USD | 102,422.20 USD | `+2.47%` | `21B / 22S` |
| `5:00 UTC` | `8.24` | `8.20` | `8.24` | `8.24` | `8.11` | 3,101,647.59 USD | 2,221,188.12 USD | 880,459.47 USD | 1,340,728.65 USD | `+43.23%` | `44B / 11S` |
| `0:00 UTC` | `8.21` | `8.23` | `8.21` | `8.28` | `8.19` | 3,097,134.32 USD | 1,901,895.55 USD | 1,195,238.77 USD | 706,656.79 USD | `+22.82%` | `14B / 3S` |
| `5:00 UTC` | `8.25` | `8.23` | `8.25` | `8.27` | `8.20` | 1,839,796.84 USD | 879,856.22 USD | 959,940.62 USD | -80,084.40 USD | `-4.35%` | `8B / 14S` |
| `0:00 UTC` | `8.21` | `8.19` | `8.21` | `8.26` | `8.11` | 2,539,835.55 USD | 1,124,809.52 USD | 1,415,026.03 USD | -290,216.50 USD | `-11.43%` | `12B / 26S` |
| `5:00 UTC` | `8.21` | `8.19` | `8.21` | `8.22` | `8.16` | 1,163,864.40 USD | 663,189.73 USD | 500,674.67 USD | 162,515.06 USD | `+13.96%` | `9B / 6S` |
| `0:00 UTC` | `8.17` | `8.20` | `8.17` | `8.25` | `8.15` | 1,223,062.19 USD | 718,965.78 USD | 504,096.41 USD | 214,869.37 USD | `+17.57%` | `26B / 17S` |
| `5:00 UTC` | `8.30` | `8.29` | `8.30` | `8.33` | `8.24` | 1,042,239.86 USD | 674,984.50 USD | 367,255.36 USD | 307,729.14 USD | `+29.53%` | `28B / 5S` |
| `0:00 UTC` | `8.34` | `8.33` | `8.34` | `8.35` | `8.30` | 876,108.07 USD | 469,253.46 USD | 406,854.61 USD | 62,398.85 USD | `+7.12%` | `5B / 6S` |
| `5:00 UTC` | `8.31` | `8.32` | `8.31` | `8.35` | `8.30` | 465,848.78 USD | 215,908.41 USD | 249,940.38 USD | -34,031.97 USD | `-7.31%` | `6B / 7S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:30` | `Range 0.025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `8.88` | 0.00 USD | 0.00 USD |
| `10-28 20:17` | `Volume 200K AVAX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `8.88` | 0.00 USD | 0.00 USD |
| `10-28 19:50` | `Volume 200K AVAX` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.79` | 0.00 USD | 0.00 USD |
| `10-28 19:17` | `Volume 200K AVAX` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `8.81` | 35,000.00 USD | 0.00 USD |
| `10-28 19:17` | `Range 0.025` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `8.81` | 35,000.00 USD | 0.00 USD |
| `10-28 19:17` | `Range 0.025` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `8.81` | 28,000.00 USD | 0.00 USD |
| `10-28 19:05` | `Volume 200K AVAX` | `Divergence` | **`BULLISH`** | Drop without taker selling | `8.86` | 0.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.025` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `8.85` | 15,000.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.025` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `8.85` | 15,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 200K AVAX` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.90` | 0.00 USD | 0.00 USD |
| `10-28 17:35` | `Volume 200K AVAX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `8.96` | 41,000.00 USD | 0.00 USD |
| `10-28 15:02` | `Range 0.025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `9.02` | 0.00 USD | 0.00 USD |
| `10-28 15:02` | `Range 0.025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.99` | 0.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.025` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `9.08` | 114,000.00 USD | 0.00 USD |
| `10-28 14:01` | `Volume 200K AVAX` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `9.08` | 125,000.00 USD | 0.00 USD |
| `10-28 13:57` | `Range 0.025` | `Divergence` | **`BULLISH`** | Drop without taker selling | `9.03` | 0.00 USD | 0.00 USD |
| `10-28 13:44` | `Range 0.025` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `9.00` | 16,000.00 USD | 0.00 USD |
| `10-28 12:46` | `Range 0.025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.95` | 0.00 USD | 0.00 USD |
| `10-28 09:02` | `Volume 200K AVAX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `9.08` | 38,000.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.025` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `9.07` | 0.00 USD | 0.00 USD |
| `10-28 06:13` | `Range 0.025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `8.98` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 16,910.00 USD | 3,550.00 USD | **`ACCUMULATION`** |
| `15m` | 21,230.00 USD | 111,800.00 USD | **`ACCUMULATION`** |
| `30m` | -7,770.00 USD | 548,760.00 USD | **`ACCUMULATION`** |
| `1h` | 142,400.00 USD | 1,210,000.00 USD | **`ACCUMULATION`** |
| `2h` | -57,340.00 USD | 1,340,000.00 USD | **`ACCUMULATION`** |
| `4h` | -1,210,000.00 USD | -2,950,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -968,780.00 USD | -542,160.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,720,000.00 USD | -9,710,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,600,000.00 USD | -11,980,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,520,000.00 USD | -12,030,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,640,000.00 USD | -55,670,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -57,770,000.00 USD | -276,220,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+16.91K` | 15m=`+21.23K` | 1h=`+142.40K` | 24h=`-2.52M`
* Futures Capital Netflows: 5m=`+3.55K` | 15m=`+111.80K` | 1h=`+1.21M` | 24h=`-12.03M`
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
  * `2026-10-30 08:00:51 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:21:51 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:21:51 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:51 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:51 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:51 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:51 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:22:51 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:22:51 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:22:51 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:22:51 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:22:51 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:22:51 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:22:51 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:22:51 IST`: [morningstar.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `8.13` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `7.97` (Risk Distance: `0.1623` pts)
  * +2.5R Take Profit: `8.54`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.40` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.56` (Risk Distance: `0.1623` pts)
  * +2.5R Take Profit: `7.99`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.37`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
