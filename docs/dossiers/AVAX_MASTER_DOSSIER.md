# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 00:08:07 IST` (`2026-10-29 18:38:07 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.79` | **Live Ask Quote**: `8.83` | **Mid Price**: `8.81`
- **Spread Points**: `4.00` | **Spread BPS**: `45.40 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.76` | VWAP Z-Score: `+0.47` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0552` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `46.12` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `9.14` | Lower -3.00σ Band: `8.38`
  * Upper +2.51σ Band: `9.07` | Lower -2.51σ Band: `8.45`
  * Upper +2.01σ Band: `9.01` | Lower -2.01σ Band: `8.51`
  * Upper +2.00σ Band: `9.01` | Lower -2.00σ Band: `8.51`
  * Upper +1.28σ Band: `8.92` | Lower -1.28σ Band: `8.60`
  * Upper +1.00σ Band: `8.89` | Lower -1.00σ Band: `8.64`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.87` | EMA-20=`8.86` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.82` (Slope: `+0.0000`) | EMA-100=`8.82`
  * Institutional Anchors: EMA-144=`8.82` | EMA-200=`8.83` (Slope: `+0.1157`) | EMA-233=`8.82`
- **Range Boundaries**: 24H High=`9.14` | 24H Low=`8.53` | Weekly High=`9.14` | Weekly Low=`8.53`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.91` (Distance: `-1.18%`)
  * Point of Control (POC) = `8.74` (Distance: `+0.74%`)
  * Value Area Low (VAL) = `8.58` (Distance: `+2.61%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`9.02` | POC=`8.99` | VAL=`8.86`
  * Prior Day Extremes: PDH=`9.14` | PDL=`8.76` | PDC=`8.99`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`8.96` | Weekly POC=`8.91` | Weekly VAL=`8.75`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`9.04` | Low=`8.53`
  * London Session (08:00-16:00 UTC): High=`8.81` | Low=`8.59`
  * New York Session (13:00-21:00 UTC): High=`9.06` | Low=`8.68`
  * Initial Balance (First Hour): IB High=`8.78` | IB Low=`8.65`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.77` - `8.85`
  * Optimal Trade Entry (OTE 0.705): `8.83`
  * Structural Invalidation Anchor (0.786): `8.88`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.85` | `8.86` | `8.84` | `8.84` | `22,050` | 194,996.78 USD | -17,098.72 USD | `-8.77%` | -3,043,318.07 USD | `+0.38` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `8.84` | `8.84` | `8.80` | `8.82` | `99,809` | 880,002.61 USD | -82,570.58 USD | `-9.38%` | -3,125,888.65 USD | `+0.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `8.82` | `8.82` | `8.81` | `8.82` | `11,845` | 104,427.46 USD | -82,805.04 USD | `-79.29%` | -3,208,693.69 USD | `+0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `8.87` | `8.88` | `8.86` | `8.88` | `73,487` | 651,856.32 USD | 86,534.20 USD | `+13.28%` | -2,775,073.90 USD | `+0.59` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `8.88` | `8.89` | `8.84` | `8.84` | `76,959` | 682,076.12 USD | -104,535.61 USD | `-15.33%` | -2,879,609.51 USD | `+0.09` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `8.84` | `8.84` | `8.80` | `8.82` | `111,654` | 984,430.07 USD | -165,375.62 USD | `-16.80%` | -3,044,985.13 USD | `-0.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `9.01` | `9.08` | `8.93` | `8.96` | `840,436` | 7,558,281.78 USD | -1,066,050.82 USD | `-14.10%` | -675,045.77 USD | `-2.27` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `8.96` | `8.96` | `8.82` | `8.87` | `732,279` | 6,517,786.37 USD | -1,600,470.16 USD | `-24.56%` | -2,275,515.94 USD | `-2.72` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `8.87` | `8.89` | `8.80` | `8.82` | `262,100` | 2,318,362.51 USD | -183,377.02 USD | `-7.91%` | -2,458,892.96 USD | `+0.11` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -426,486.82 USD | `+0.25` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -480,308.79 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.80` | `8.82` | `1,834,815` | 16,394,430.66 USD | -2,849,898.01 USD | `-17.38%` | -3,330,206.80 USD | `-1.45` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `9.00` | `9.02` | `8.55` | `8.59` | `3,515,330` | 30,612,875.98 USD | -2,423,031.38 USD | `-7.92%` | -749,324.84 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.59` | `8.80` | `8.57` | `8.62` | `1,816,830` | 15,790,058.74 USD | 58,580.54 USD | `+0.37%` | -690,744.30 USD | `+0.17` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -426,486.82 USD | `+0.25` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -480,308.79 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.80` | `8.82` | `1,834,815` | 16,394,430.66 USD | -2,849,898.01 USD | `-17.38%` | -3,330,206.80 USD | `-1.45` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`8.81`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BUY` | `8.63` | `90808.1500` | 783,783.30 USD | 1,599,167.84 USD | `LARGE (>= USD 100K)` | `-2.00%` | `0x71cfa5e263` |
| `BUY` | `8.63` | `140.9400` | 1,216.59 USD | 7,277,490.72 USD | `STANDARD` | `-1.99%` | `0x0ad81cbc47` |
| `BUY` | `8.65` | `17526.0100` | 151,554.42 USD | 3,809,871.56 USD | `LARGE (>= USD 100K)` | `-1.81%` | `0x71d0e11ebb` |
| `BUY` | `8.66` | `383.1600` | 3,319.58 USD | 7,102,952.65 USD | `STANDARD` | `-1.63%` | `0x14f8e04290` |
| `BUY` | `8.67` | `13127.1600` | 113,770.47 USD | 4,722,247.18 USD | `LARGE (>= USD 100K)` | `-1.59%` | `0xecb63caa47` |
| `BUY` | `8.67` | `2190.2500` | 18,999.98 USD | 5,899,879.98 USD | `STANDARD` | `-1.50%` | `0x0efb38a5fa` |
| `BUY` | `8.67` | `186.1300` | 1,613.93 USD | 7,266,454.43 USD | `STANDARD` | `-1.55%` | `0x0ad81cbc47` |
| `BUY` | `8.67` | `181.1300` | 1,570.16 USD | 7,268,024.59 USD | `STANDARD` | `-1.57%` | `0x010461c14e` |
| `BUY` | `8.67` | `169.6600` | 1,470.32 USD | 7,271,031.26 USD | `STANDARD` | `-1.60%` | `0x31ca8395cf` |
| `BUY` | `8.67` | `76.4300` | 662.72 USD | 7,315,707.39 USD | `STANDARD` | `-1.55%` | `0xdadbb4b2a0` |
| `BUY` | `8.68` | `2119.6200` | 18,405.30 USD | 5,974,869.60 USD | `STANDARD` | `-1.41%` | `0xd3943e4008` |
| `BUY` | `8.68` | `315.7300` | 2,740.85 USD | 7,176,097.52 USD | `STANDARD` | `-1.43%` | `0x07fd993f0f` |
| `BUY` | `8.69` | `12893.8400` | 112,041.02 USD | 4,947,199.29 USD | `LARGE (>= USD 100K)` | `-1.34%` | `0x71d0e11ebb` |
| `BUY` | `8.69` | `10901.7300` | 94,685.89 USD | 5,645,205.09 USD | `MEDIUM (>= USD 25K)` | `-1.38%` | `0xecb63caa47` |
| `BUY` | `8.69` | `74.4300` | 646.62 USD | 7,317,658.79 USD | `STANDARD` | `-1.36%` | `0x010461c14e` |
| `BUY` | `8.70` | `17523.2300` | 152,488.90 USD | 3,658,317.14 USD | `LARGE (>= USD 100K)` | `-1.19%` | `0x71d0e11ebb` |
| `BUY` | `8.70` | `12316.8100` | 107,189.50 USD | 5,054,388.79 USD | `LARGE (>= USD 100K)` | `-1.19%` | `0xecb63caa47` |
| `BUY` | `8.70` | `1838.8000` | 15,999.95 USD | 5,990,869.55 USD | `STANDARD` | `-1.20%` | `0x0efb38a5fa` |
| `BUY` | `8.70` | `383.1600` | 3,332.88 USD | 7,099,633.07 USD | `STANDARD` | `-1.23%` | `0x14f8e04290` |
| `BUY` | `8.70` | `76.6700` | 667.10 USD | 7,315,044.68 USD | `STANDARD` | `-1.21%` | `0x31ca8395cf` |
| `BUY` | `8.71` | `46837.8300` | 408,055.86 USD | 2,423,728.38 USD | `LARGE (>= USD 100K)` | `-1.08%` | `0x71cfa5e263` |
| `BUY` | `8.71` | `3667.0700` | 31,946.78 USD | 5,828,685.97 USD | `MEDIUM (>= USD 25K)` | `-1.08%` | `0xa38f19c4cc` |
| `BUY` | `8.71` | `186.1300` | 1,621.19 USD | 7,264,840.50 USD | `STANDARD` | `-1.10%` | `0x0ad81cbc47` |
| `BUY` | `8.72` | `11243.8700` | 98,055.54 USD | 5,452,748.44 USD | `MEDIUM (>= USD 25K)` | `-0.98%` | `0xecb63caa47` |
| `BUY` | `8.72` | `4082.5500` | 35,617.39 USD | 5,796,739.19 USD | `MEDIUM (>= USD 25K)` | `-0.94%` | `0xa24c5ca26c` |
| `BUY` | `8.72` | `1650.1800` | 14,387.26 USD | 6,476,974.49 USD | `STANDARD` | `-1.01%` | `0xd3943e4008` |
| `BUY` | `8.72` | `1345.6200` | 11,731.52 USD | 6,600,775.63 USD | `STANDARD` | `-1.01%` | `0x33ad48ed92` |
| `BUY` | `8.73` | `22398.7000` | 195,641.45 USD | 3,040,308.75 USD | `LARGE (>= USD 100K)` | `-0.82%` | `0xa20fb0c9e0` |
| `BUY` | `8.73` | `1483.1200` | 12,953.27 USD | 6,516,299.43 USD | `STANDARD` | `-0.83%` | `0xd3943e4008` |
| `BUY` | `8.73` | `366.8200` | 3,203.81 USD | 7,122,306.77 USD | `STANDARD` | `-0.83%` | `0xdd4f66125d` |
| `BUY` | `8.73` | `175.9900` | 1,536.34 USD | 7,269,560.93 USD | `STANDARD` | `-0.88%` | `0xdadbb4b2a0` |
| `BUY` | `8.73` | `131.2700` | 1,146.09 USD | 7,289,273.75 USD | `STANDARD` | `-0.87%` | `0xe34d21d198` |
| `BUY` | `8.74` | `17537.1400` | 153,283.37 USD | 3,505,828.24 USD | `LARGE (>= USD 100K)` | `-0.76%` | `0x71d0e11ebb` |
| `BUY` | `8.74` | `1372.8500` | 11,999.94 USD | 6,553,149.57 USD | `STANDARD` | `-0.75%` | `0x0efb38a5fa` |
| `BUY` | `8.74` | `1250.0000` | 10,923.00 USD | 6,667,593.55 USD | `STANDARD` | `-0.78%` | `0xb7bd9cef0e` |
| `BUY` | `8.74` | `383.1600` | 3,349.39 USD | 7,092,953.13 USD | `STANDARD` | `-0.75%` | `0x14f8e04290` |
| `BUY` | `8.74` | `383.1600` | 3,347.06 USD | 7,096,300.19 USD | `STANDARD` | `-0.81%` | `0x14f8e04290` |
| `BUY` | `8.74` | `315.7300` | 2,758.85 USD | 7,167,859.57 USD | `STANDARD` | `-0.79%` | `0x07fd993f0f` |
| `BUY` | `8.74` | `73.5900` | 643.49 USD | 7,318,948.14 USD | `STANDARD` | `-0.71%` | `0x010461c14e` |
| `BUY` | `8.74` | `72.8300` | 636.83 USD | 7,320,865.25 USD | `STANDARD` | `-0.72%` | `0x31ca8395cf` |
| `BUY` | `8.75` | `11447.1200` | 100,113.08 USD | 5,154,501.87 USD | `LARGE (>= USD 100K)` | `-0.70%` | `0x881cd92459` |
| `BUY` | `8.75` | `2147.7500` | 18,792.17 USD | 5,956,464.30 USD | `STANDARD` | `-0.65%` | `0xa38f19c4cc` |
| `BUY` | `8.75` | `1666.8600` | 14,590.03 USD | 6,448,005.54 USD | `STANDARD` | `-0.61%` | `0x57d8e75f47` |
| `BUY` | `8.75` | `1666.8600` | 14,581.69 USD | 6,462,587.23 USD | `STANDARD` | `-0.67%` | `0x57d8e75f47` |
| `BUY` | `8.75` | `1007.9000` | 8,820.54 USD | 6,804,431.73 USD | `STANDARD` | `-0.63%` | `0x33ad48ed92` |
| `BUY` | `8.75` | `231.2300` | 2,023.52 USD | 7,246,602.53 USD | `STANDARD` | `-0.64%` | `0x9d732bed51` |
| `BUY` | `8.75` | `142.8700` | 1,249.97 USD | 7,276,274.12 USD | `STANDARD` | `-0.66%` | `0x0ad81cbc47` |
| `BUY` | `8.75` | `131.2700` | 1,149.02 USD | 7,288,127.66 USD | `STANDARD` | `-0.61%` | `0xe34d21d198` |
| `BUY` | `8.76` | `1666.8600` | 14,606.69 USD | 6,418,817.15 USD | `STANDARD` | `-0.50%` | `0x57d8e75f47` |
| `BUY` | `8.76` | `1666.8600` | 14,598.36 USD | 6,433,415.51 USD | `STANDARD` | `-0.56%` | `0x57d8e75f47` |
| `BUY` | `8.76` | `1294.2000` | 11,332.66 USD | 6,623,466.63 USD | `STANDARD` | `-0.58%` | `0xd3943e4008` |
| `BUY` | `8.76` | `912.7500` | 7,999.98 USD | 6,837,352.57 USD | `STANDARD` | `-0.48%` | `0x0efb38a5fa` |
| `BUY` | `8.76` | `830.0000` | 7,270.47 USD | 6,867,971.07 USD | `STANDARD` | `-0.54%` | `0xb7bd9cef0e` |
| `BUY` | `8.76` | `490.7400` | 4,300.85 USD | 7,004,120.03 USD | `STANDARD` | `-0.49%` | `0xcd7f60e943` |
| `BUY` | `8.76` | `366.8200` | 3,214.08 USD | 7,115,891.16 USD | `STANDARD` | `-0.51%` | `0xdd4f66125d` |
| `BUY` | `8.76` | `366.8200` | 3,211.80 USD | 7,119,102.97 USD | `STANDARD` | `-0.58%` | `0xdd4f66125d` |
| `BUY` | `8.76` | `231.2300` | 2,026.68 USD | 7,240,528.81 USD | `STANDARD` | `-0.48%` | `0x9d732bed51` |
| `BUY` | `8.76` | `231.2300` | 2,025.64 USD | 7,242,554.46 USD | `STANDARD` | `-0.53%` | `0x9d732bed51` |
| `BUY` | `8.76` | `231.2300` | 2,024.56 USD | 7,244,579.02 USD | `STANDARD` | `-0.59%` | `0x9d732bed51` |
| `BUY` | `8.76` | `79.1500` | 693.71 USD | 7,313,016.34 USD | `STANDARD` | `-0.48%` | `0x31ca8395cf` |
| `BUY` | `8.76` | `74.9800` | 657.18 USD | 7,316,364.57 USD | `STANDARD` | `-0.48%` | `0x010461c14e` |
| `BUY` | `8.77` | `23868.8000` | 209,312.67 USD | 2,844,667.31 USD | `LARGE (>= USD 100K)` | `-0.43%` | `0x71cfa5e263` |
| `BUY` | `8.77` | `14828.0200` | 130,081.77 USD | 4,366,577.25 USD | `LARGE (>= USD 100K)` | `-0.39%` | `0x71d0e11ebb` |
| `BUY` | `8.77` | `1666.8600` | 14,623.36 USD | 6,389,595.43 USD | `STANDARD` | `-0.39%` | `0x57d8e75f47` |
| `BUY` | `8.77` | `1666.8600` | 14,615.03 USD | 6,404,210.46 USD | `STANDARD` | `-0.44%` | `0x57d8e75f47` |
| `BUY` | `8.77` | `1259.9500` | 11,054.17 USD | 6,656,670.55 USD | `STANDARD` | `-0.38%` | `0xa38f19c4cc` |
| `BUY` | `8.77` | `1122.8400` | 9,848.54 USD | 6,767,487.88 USD | `STANDARD` | `-0.41%` | `0xd3342d3b1e` |
| `BUY` | `8.77` | `1090.6600` | 9,566.40 USD | 6,786,722.92 USD | `STANDARD` | `-0.41%` | `0xd3943e4008` |
| `BUY` | `8.77` | `801.7400` | 7,031.66 USD | 6,875,002.73 USD | `STANDARD` | `-0.42%` | `0xecb63caa47` |
| `BUY` | `8.77` | `796.2400` | 6,983.82 USD | 6,888,970.39 USD | `STANDARD` | `-0.41%` | `0x47a4471457` |
| `BUY` | `8.77` | `403.9300` | 3,542.10 USD | 7,075,934.43 USD | `STANDARD` | `-0.43%` | `0x2a72b57dea` |
| `BUY` | `8.77` | `231.2300` | 2,028.79 USD | 7,236,474.41 USD | `STANDARD` | `-0.38%` | `0x9d732bed51` |
| `BUY` | `8.77` | `231.2300` | 2,027.73 USD | 7,238,502.13 USD | `STANDARD` | `-0.43%` | `0x9d732bed51` |
| `BUY` | `8.78` | `4242.7300` | 37,256.68 USD | 5,761,121.80 USD | `MEDIUM (>= USD 25K)` | `-0.29%` | `0x08a49e7f71` |
| `BUY` | `8.78` | `1666.8600` | 14,640.03 USD | 6,360,340.37 USD | `STANDARD` | `-0.27%` | `0x57d8e75f47` |
| `BUY` | `8.78` | `1666.8600` | 14,631.70 USD | 6,374,972.06 USD | `STANDARD` | `-0.33%` | `0x57d8e75f47` |
| `BUY` | `8.78` | `969.2800` | 8,511.83 USD | 6,812,943.56 USD | `STANDARD` | `-0.29%` | `0xd3943e4008` |
| `BUY` | `8.78` | `749.7200` | 6,579.39 USD | 6,895,549.79 USD | `STANDARD` | `-0.36%` | `0xecb63caa47` |
| `BUY` | `8.78` | `739.2700` | 6,493.23 USD | 6,915,047.92 USD | `STANDARD` | `-0.27%` | `0xecb63caa47` |
| `BUY` | `8.78` | `672.9200` | 5,907.30 USD | 6,938,863.47 USD | `STANDARD` | `-0.32%` | `0xecb63caa47` |
| `BUY` | `8.78` | `671.9300` | 5,896.99 USD | 6,944,760.46 USD | `STANDARD` | `-0.35%` | `0x33ad48ed92` |
| `BUY` | `8.78` | `569.1500` | 4,999.93 USD | 6,980,916.76 USD | `STANDARD` | `-0.25%` | `0x0efb38a5fa` |
| `BUY` | `8.78` | `420.0000` | 3,688.61 USD | 7,043,929.60 USD | `STANDARD` | `-0.28%` | `0xb7bd9cef0e` |
| `BUY` | `8.78` | `403.9300` | 3,546.38 USD | 7,072,392.33 USD | `STANDARD` | `-0.31%` | `0x2a72b57dea` |
| `BUY` | `8.78` | `231.2300` | 2,030.82 USD | 7,232,415.79 USD | `STANDARD` | `-0.28%` | `0x9d732bed51` |
| `BUY` | `8.78` | `231.2300` | 2,029.83 USD | 7,234,445.62 USD | `STANDARD` | `-0.33%` | `0x9d732bed51` |
| `BUY` | `8.78` | `131.2700` | 1,151.89 USD | 7,286,978.64 USD | `STANDARD` | `-0.37%` | `0xe34d21d198` |
| `BUY` | `8.78` | `78.8000` | 692.15 USD | 7,313,708.48 USD | `STANDARD` | `-0.27%` | `0x010461c14e` |
| `BUY` | `8.78` | `72.4500` | 636.41 USD | 7,321,501.66 USD | `STANDARD` | `-0.26%` | `0x31ca8395cf` |
| `BUY` | `8.78` | `62.6400` | 550.03 USD | 7,324,491.41 USD | `STANDARD` | `-0.30%` | `0x5cc518f6e6` |
| `BUY` | `8.78` | `57.3100` | 503.37 USD | 7,329,079.88 USD | `STANDARD` | `-0.27%` | `0x57d8e75f47` |
| `BUY` | `8.78` | `57.0000` | 500.65 USD | 7,330,584.19 USD | `STANDARD` | `-0.27%` | `0x667b8184fc` |
| `BUY` | `8.79` | `16763.4500` | 147,298.76 USD | 4,105,215.35 USD | `LARGE (>= USD 100K)` | `-0.23%` | `0x71d0e11ebb` |
| `BUY` | `8.79` | `1666.8600` | 14,648.37 USD | 6,345,700.34 USD | `STANDARD` | `-0.22%` | `0x57d8e75f47` |
| `BUY` | `8.79` | `1137.9700` | 10,008.45 USD | 6,707,721.78 USD | `STANDARD` | `-0.14%` | `0xaf9f722a67` |
| `BUY` | `8.79` | `1137.9700` | 10,007.99 USD | 6,717,729.77 USD | `STANDARD` | `-0.14%` | `0x621c555167` |
| `BUY` | `8.79` | `1137.9700` | 9,998.43 USD | 6,747,729.42 USD | `STANDARD` | `-0.24%` | `0xaf9f722a67` |
| `BUY` | `8.79` | `739.9200` | 6,502.42 USD | 6,908,554.69 USD | `STANDARD` | `-0.22%` | `0xa38f19c4cc` |
| `BUY` | `8.79` | `599.1800` | 5,268.11 USD | 6,955,887.66 USD | `STANDARD` | `-0.17%` | `0xecb63caa47` |
| `BUY` | `8.79` | `568.2000` | 4,994.53 USD | 6,985,911.29 USD | `STANDARD` | `-0.19%` | `0x3ca146d269` |
| `BUY` | `8.79` | `548.3100` | 4,817.18 USD | 6,990,728.47 USD | `STANDARD` | `-0.25%` | `0xecb63caa47` |
| `BUY` | `8.79` | `481.6400` | 4,234.19 USD | 7,021,126.67 USD | `STANDARD` | `-0.18%` | `0x7717a7a245` |
| `BUY` | `8.79` | `451.5500` | 3,971.16 USD | 7,025,097.83 USD | `STANDARD` | `-0.14%` | `0xecb63caa47` |
| `BUY` | `8.79` | `403.9300` | 3,551.07 USD | 7,065,297.02 USD | `STANDARD` | `-0.18%` | `0x2a72b57dea` |
| `BUY` | `8.79` | `403.9300` | 3,548.93 USD | 7,068,845.94 USD | `STANDARD` | `-0.24%` | `0x2a72b57dea` |
| `BUY` | `8.79` | `362.8700` | 3,190.72 USD | 7,125,497.49 USD | `STANDARD` | `-0.16%` | `0x57d8e75f47` |
| `BUY` | `8.79` | `347.2700` | 3,051.74 USD | 7,156,174.53 USD | `STANDARD` | `-0.22%` | `0x6ba889db7f` |
| `BUY` | `8.79` | `346.7100` | 3,047.82 USD | 7,159,222.35 USD | `STANDARD` | `-0.19%` | `0x6ba889db7f` |
| `BUY` | `8.79` | `346.5500` | 3,047.21 USD | 7,162,269.57 USD | `STANDARD` | `-0.16%` | `0x6ba889db7f` |
| `BUY` | `8.79` | `268.7700` | 2,363.24 USD | 7,196,740.28 USD | `STANDARD` | `-0.16%` | `0x33ad48ed92` |
| `BUY` | `8.79` | `259.3000` | 2,279.35 USD | 7,201,378.38 USD | `STANDARD` | `-0.19%` | `0xecb63caa47` |
| `BUY` | `8.79` | `255.8400` | 2,249.93 USD | 7,205,878.26 USD | `STANDARD` | `-0.15%` | `0xa38f19c4cc` |
| `BUY` | `8.79` | `231.2300` | 2,032.86 USD | 7,228,353.05 USD | `STANDARD` | `-0.18%` | `0x9d732bed51` |
| `BUY` | `8.79` | `231.2300` | 2,031.91 USD | 7,230,384.96 USD | `STANDARD` | `-0.22%` | `0x9d732bed51` |
| `BUY` | `8.79` | `226.8000` | 1,993.46 USD | 7,250,599.24 USD | `STANDARD` | `-0.20%` | `0x39bac00809` |
| `BUY` | `8.79` | `200.0000` | 1,758.96 USD | 7,261,479.33 USD | `STANDARD` | `-0.14%` | `0xfc27136e42` |
| `BUY` | `8.79` | `142.2200` | 1,249.97 USD | 7,275,024.15 USD | `STANDARD` | `-0.21%` | `0x0ad81cbc47` |
| `BUY` | `8.79` | `137.5600` | 1,209.51 USD | 7,282,333.23 USD | `STANDARD` | `-0.17%` | `0xdd4f66125d` |
| `BUY` | `8.79` | `113.7000` | 999.97 USD | 7,298,724.25 USD | `STANDARD` | `-0.14%` | `0x27c9fa86c9` |
| `BUY` | `8.79` | `57.3100` | 503.78 USD | 7,328,576.51 USD | `STANDARD` | `-0.19%` | `0x57d8e75f47` |
| `BID` | `8.80` | `4.5400` | 39.97 USD | 56.26 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.80` | `681.5200` | 5,999.69 USD | 6,055.96 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.80` | `50.0000` | 440.17 USD | 6,496.12 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.80` | `1666.8600` | 14,673.70 USD | 21,169.82 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.80` | `2.9100` | 25.62 USD | 21,195.44 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.80` | `100.7500` | 886.88 USD | 22,082.32 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.80` | `73.3700` | 645.85 USD | 22,728.18 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.80` | `908.8900` | 7,999.78 USD | 30,727.95 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.80` | `120.0800` | 1,056.88 USD | 31,784.84 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.80` | `5.3100` | 46.74 USD | 31,831.57 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.80` | `113.6200` | 999.97 USD | 32,831.54 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.80` | `352.9900` | 3,106.63 USD | 35,938.17 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.80` | `46.1600` | 406.24 USD | 36,344.42 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `8.80` | `16.8600` | 148.38 USD | 36,492.80 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.80` | `18.3800` | 161.76 USD | 36,654.55 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.80` | `38.6500` | 340.14 USD | 36,994.69 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.80` | `284.0800` | 2,499.99 USD | 39,494.68 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.80` | `142.8900` | 1,257.45 USD | 40,752.13 USD | `3 orders` | `-0.08%` | `-` |
| `BID` | `8.80` | `1136.3600` | 9,999.85 USD | 50,751.98 USD | `1 orders` | `-0.08%` | `-` |
| `BUY` | `8.80` | `1666.8600` | 14,673.70 USD | 6,301,723.90 USD | `STANDARD` | `-0.04%` | `0x57d8e75f47` |
| `BUY` | `8.80` | `1666.8600` | 14,666.87 USD | 6,316,390.77 USD | `STANDARD` | `-0.09%` | `0x57d8e75f47` |
| `BUY` | `8.80` | `1666.8600` | 14,661.20 USD | 6,331,051.97 USD | `STANDARD` | `-0.13%` | `0x57d8e75f47` |
| `BUY` | `8.80` | `1498.9800` | 13,185.78 USD | 6,503,346.15 USD | `STANDARD` | `-0.12%` | `0x08a49e7f71` |
| `BUY` | `8.80` | `1363.6100` | 11,997.59 USD | 6,577,147.08 USD | `STANDARD` | `-0.10%` | `0x7d0c59691f` |
| `BUY` | `8.80` | `1136.3600` | 9,999.85 USD | 6,737,730.99 USD | `STANDARD` | `-0.08%` | `0x7d0c59691f` |
| `BUY` | `8.80` | `908.8900` | 7,999.78 USD | 6,853,352.28 USD | `STANDARD` | `-0.06%` | `0x7d0c59691f` |
| `BUY` | `8.80` | `681.5200` | 5,999.69 USD | 6,927,047.83 USD | `STANDARD` | `-0.04%` | `0x7d0c59691f` |
| `BUY` | `8.80` | `483.5600` | 4,254.89 USD | 7,012,640.70 USD | `STANDARD` | `-0.09%` | `0x71d0e11ebb` |
| `BUY` | `8.80` | `434.8000` | 3,824.98 USD | 7,028,922.81 USD | `STANDARD` | `-0.11%` | `0xa38f19c4cc` |
| `BUY` | `8.80` | `403.9300` | 3,553.41 USD | 7,061,745.95 USD | `STANDARD` | `-0.11%` | `0x2a72b57dea` |
| `BUY` | `8.80` | `352.9900` | 3,106.63 USD | 7,128,604.12 USD | `STANDARD` | `-0.07%` | `0x6ba889db7f` |
| `BUY` | `8.80` | `351.1300` | 3,089.24 USD | 7,131,693.36 USD | `STANDARD` | `-0.10%` | `0x6ba889db7f` |
| `BUY` | `8.80` | `348.5300` | 3,065.43 USD | 7,137,838.52 USD | `STANDARD` | `-0.13%` | `0x6ba889db7f` |
| `BUY` | `8.80` | `312.0500` | 2,744.92 USD | 7,173,356.67 USD | `STANDARD` | `-0.12%` | `0x7717a7a245` |
| `BUY` | `8.80` | `284.0800` | 2,499.99 USD | 7,189,439.06 USD | `STANDARD` | `-0.08%` | `0x0efb38a5fa` |
| `BUY` | `8.80` | `137.5600` | 1,210.21 USD | 7,279,913.78 USD | `STANDARD` | `-0.11%` | `0xdd4f66125d` |
| `BUY` | `8.80` | `137.5600` | 1,209.94 USD | 7,281,123.72 USD | `STANDARD` | `-0.13%` | `0xdd4f66125d` |
| `BUY` | `8.80` | `125.8300` | 1,107.27 USD | 7,291,494.29 USD | `STANDARD` | `-0.08%` | `0x2eddf3aa5c` |
| `BUY` | `8.80` | `122.7500` | 1,080.45 USD | 7,292,574.73 USD | `STANDARD` | `-0.06%` | `0x2eddf3aa5c` |
| `BUY` | `8.80` | `120.0800` | 1,056.88 USD | 7,294,689.83 USD | `STANDARD` | `-0.06%` | `0x7717a7a245` |
| `BUY` | `8.80` | `113.6200` | 999.97 USD | 7,297,724.29 USD | `STANDARD` | `-0.07%` | `0x0eecd62efb` |
| `BUY` | `8.80` | `100.7500` | 886.88 USD | 7,302,515.98 USD | `STANDARD` | `-0.05%` | `0xecb63caa47` |
| `BUY` | `8.80` | `86.3700` | 759.65 USD | 7,307,224.98 USD | `STANDARD` | `-0.13%` | `0x010461c14e` |
| `BUY` | `8.80` | `73.3700` | 645.85 USD | 7,318,304.64 USD | `STANDARD` | `-0.05%` | `0x727956612a` |
| `BUY` | `8.80` | `72.8800` | 641.01 USD | 7,319,589.15 USD | `STANDARD` | `-0.13%` | `0x31ca8395cf` |
| `BUY` | `8.80` | `71.2500` | 627.28 USD | 7,322,760.92 USD | `STANDARD` | `-0.04%` | `0x2eddf3aa5c` |
| `BUY` | `8.80` | `67.1900` | 591.24 USD | 7,323,352.16 USD | `STANDARD` | `-0.09%` | `0x33ad48ed92` |
| `BUY` | `8.80` | `57.3100` | 504.17 USD | 7,328,072.73 USD | `STANDARD` | `-0.11%` | `0x57d8e75f47` |
| `ASK` | `8.81` | `680.9300` | 6,000.22 USD | 49,186.10 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.81` | `1666.8600` | 14,687.87 USD | 43,185.88 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.81` | `108.0000` | 951.64 USD | 28,498.01 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.81` | `1026.7400` | 9,047.02 USD | 27,546.36 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `8.81` | `113.4900` | 999.97 USD | 18,499.35 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.81` | `346.7100` | 3,054.86 USD | 17,499.38 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.81` | `54.0100` | 475.88 USD | 14,444.51 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.81` | `164.1400` | 1,446.20 USD | 13,968.64 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `8.81` | `50.0000` | 440.54 USD | 12,522.43 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.81` | `54.0100` | 475.84 USD | 12,081.90 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.81` | `50.0000` | 440.50 USD | 11,606.06 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.81` | `53.9800` | 475.54 USD | 11,165.55 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.81` | `50.0000` | 440.47 USD | 10,690.02 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.81` | `85.2400` | 750.89 USD | 10,249.55 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `8.81` | `50.0000` | 440.45 USD | 9,498.66 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.81` | `157.2100` | 1,384.83 USD | 9,058.21 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `8.81` | `70.8000` | 623.66 USD | 7,673.38 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `8.81` | `53.9800` | 475.46 USD | 7,049.72 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.81` | `53.9800` | 475.45 USD | 6,574.26 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.81` | `692.4800` | 6,098.81 USD | 6,098.81 USD | `9 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `8.81` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.81` | `0.00%` | `-` |
| `BID` | `8.81` | `1.8500` | 16.29 USD | 16.29 USD | `1 orders` | `-0.00%` | `-` |
| `SELL` | `8.81` | `1666.8600` | 14,687.87 USD | 6,287,050.20 USD | `STANDARD` | `+0.05%` | `0x57d8e75f47` |
| `SELL` | `8.81` | `907.9500` | 8,000.31 USD | 6,829,352.59 USD | `STANDARD` | `+0.05%` | `0x7d0c59691f` |
| `SELL` | `8.81` | `680.9300` | 6,000.22 USD | 6,921,048.14 USD | `STANDARD` | `+0.05%` | `0x7d0c59691f` |
| `SELL` | `8.81` | `567.2600` | 4,999.94 USD | 6,975,916.83 USD | `STANDARD` | `+0.08%` | `0x44f481f406` |
| `SELL` | `8.81` | `347.4100` | 3,059.71 USD | 7,140,898.23 USD | `STANDARD` | `+0.00%` | `0x6ba889db7f` |
| `SELL` | `8.81` | `346.7100` | 3,055.66 USD | 7,150,067.93 USD | `STANDARD` | `+0.07%` | `0x6ba889db7f` |
| `SELL` | `8.81` | `346.7100` | 3,054.86 USD | 7,153,122.79 USD | `STANDARD` | `+0.04%` | `0x6ba889db7f` |
| `SELL` | `8.81` | `283.6600` | 2,499.92 USD | 7,191,938.98 USD | `STANDARD` | `+0.07%` | `0x0efb38a5fa` |
| `SELL` | `8.81` | `209.5700` | 1,846.98 USD | 7,256,196.15 USD | `STANDARD` | `+0.07%` | `0x023a3d0580` |
| `SELL` | `8.81` | `200.0000` | 1,762.38 USD | 7,257,958.53 USD | `STANDARD` | `+0.05%` | `0xfc27136e42` |
| `SELL` | `8.81` | `200.0000` | 1,761.84 USD | 7,259,720.37 USD | `STANDARD` | `+0.02%` | `0xfc27136e42` |
| `SELL` | `8.81` | `146.0800` | 1,286.56 USD | 7,273,774.18 USD | `STANDARD` | `+0.00%` | `0x727956612a` |
| `SELL` | `8.81` | `120.0800` | 1,058.22 USD | 7,293,632.95 USD | `STANDARD` | `+0.06%` | `0x7717a7a245` |
| `SELL` | `8.81` | `113.4900` | 999.97 USD | 7,296,724.32 USD | `STANDARD` | `+0.04%` | `0x27c9fa86c9` |
| `SELL` | `8.81` | `113.4800` | 999.92 USD | 7,299,724.17 USD | `STANDARD` | `+0.05%` | `0x0eecd62efb` |
| `SELL` | `8.81` | `103.2300` | 909.33 USD | 7,301,629.10 USD | `STANDARD` | `+0.02%` | `0xecb63caa47` |
| `SELL` | `8.81` | `72.5600` | 639.28 USD | 7,320,228.43 USD | `STANDARD` | `+0.04%` | `0x2eddf3aa5c` |
| `SELL` | `8.81` | `62.4300` | 549.95 USD | 7,325,041.37 USD | `STANDARD` | `+0.02%` | `0x023a3d0580` |
| `SELL` | `8.81` | `57.3100` | 505.17 USD | 7,327,063.61 USD | `STANDARD` | `+0.09%` | `0x57d8e75f47` |
| `SELL` | `8.81` | `57.3100` | 504.95 USD | 7,327,568.56 USD | `STANDARD` | `+0.04%` | `0x57d8e75f47` |
| `SELL` | `8.81` | `56.8300` | 500.72 USD | 7,330,083.55 USD | `STANDARD` | `+0.04%` | `0x023a3d0580` |
| `SELL` | `8.82` | `1666.8600` | 14,708.04 USD | 6,228,266.88 USD | `STANDARD` | `+0.19%` | `0x57d8e75f47` |
| `SELL` | `8.82` | `1666.8600` | 14,703.54 USD | 6,242,970.42 USD | `STANDARD` | `+0.16%` | `0x57d8e75f47` |
| `SELL` | `8.82` | `1666.8600` | 14,698.37 USD | 6,257,668.79 USD | `STANDARD` | `+0.12%` | `0x57d8e75f47` |
| `SELL` | `8.82` | `1666.8600` | 14,693.54 USD | 6,272,362.33 USD | `STANDARD` | `+0.09%` | `0x57d8e75f47` |
| `SELL` | `8.82` | `1495.8300` | 13,185.89 USD | 6,490,160.38 USD | `STANDARD` | `+0.09%` | `0x08a49e7f71` |
| `SELL` | `8.82` | `1360.8000` | 12,000.21 USD | 6,541,149.62 USD | `STANDARD` | `+0.13%` | `0x7d0c59691f` |
| `SELL` | `8.82` | `1137.9700` | 10,038.37 USD | 6,687,680.31 USD | `STANDARD` | `+0.16%` | `0xaf9f722a67` |
| `SELL` | `8.82` | `1137.9700` | 10,033.03 USD | 6,697,713.34 USD | `STANDARD` | `+0.11%` | `0x621c555167` |
| `SELL` | `8.82` | `1134.5200` | 10,001.36 USD | 6,727,731.14 USD | `STANDARD` | `+0.09%` | `0x7d0c59691f` |
| `SELL` | `8.82` | `567.0400` | 4,999.99 USD | 6,965,916.94 USD | `STANDARD` | `+0.12%` | `0x44f481f406` |
| `SELL` | `8.82` | `483.6600` | 4,265.78 USD | 7,008,385.81 USD | `STANDARD` | `+0.14%` | `0x71d0e11ebb` |
| `SELL` | `8.82` | `433.5900` | 3,824.91 USD | 7,032,747.72 USD | `STANDARD` | `+0.16%` | `0xa38f19c4cc` |
| `SELL` | `8.82` | `403.9300` | 3,564.16 USD | 7,054,631.12 USD | `STANDARD` | `+0.19%` | `0x2a72b57dea` |
| `SELL` | `8.82` | `403.9300` | 3,561.41 USD | 7,058,192.53 USD | `STANDARD` | `+0.11%` | `0x2a72b57dea` |
| `SELL` | `8.82` | `349.1600` | 3,079.73 USD | 7,134,773.09 USD | `STANDARD` | `+0.15%` | `0x6ba889db7f` |
| `SELL` | `8.82` | `346.7400` | 3,057.59 USD | 7,143,955.81 USD | `STANDARD` | `+0.12%` | `0x6ba889db7f` |
| `SELL` | `8.82` | `346.7100` | 3,056.46 USD | 7,147,012.27 USD | `STANDARD` | `+0.10%` | `0x6ba889db7f` |
| `SELL` | `8.82` | `312.0500` | 2,752.19 USD | 7,170,611.76 USD | `STANDARD` | `+0.14%` | `0x7717a7a245` |
| `SELL` | `8.82` | `308.1500` | 2,718.62 USD | 7,178,816.15 USD | `STANDARD` | `+0.17%` | `0xecb63caa47` |
| `SELL` | `8.82` | `308.2300` | 2,718.62 USD | 7,181,534.77 USD | `STANDARD` | `+0.15%` | `0xecb63caa47` |
| `SELL` | `8.82` | `276.4900` | 2,438.06 USD | 7,194,377.04 USD | `STANDARD` | `+0.12%` | `0xecb63caa47` |
| `SELL` | `8.82` | `255.1600` | 2,249.95 USD | 7,203,628.33 USD | `STANDARD` | `+0.12%` | `0xa38f19c4cc` |
| `SELL` | `8.82` | `231.2300` | 2,040.60 USD | 7,224,280.61 USD | `STANDARD` | `+0.20%` | `0x9d732bed51` |
| `SELL` | `8.82` | `231.2300` | 2,039.59 USD | 7,226,320.19 USD | `STANDARD` | `+0.15%` | `0x9d732bed51` |
| `SELL` | `8.82` | `137.5600` | 1,212.85 USD | 7,278,703.57 USD | `STANDARD` | `+0.11%` | `0xdd4f66125d` |
| `SELL` | `8.82` | `126.2700` | 1,113.27 USD | 7,290,387.02 USD | `STANDARD` | `+0.11%` | `0x2eddf3aa5c` |
| `SELL` | `8.82` | `117.3500` | 1,034.51 USD | 7,295,724.34 USD | `STANDARD` | `+0.10%` | `0x2eddf3aa5c` |
| `SELL` | `8.82` | `91.7000` | 809.00 USD | 7,303,324.98 USD | `STANDARD` | `+0.17%` | `0xdd4f66125d` |
| `SELL` | `8.82` | `91.7000` | 808.98 USD | 7,304,133.95 USD | `STANDARD` | `+0.17%` | `0xdd4f66125d` |
| `SELL` | `8.82` | `91.7000` | 808.93 USD | 7,304,942.88 USD | `STANDARD` | `+0.16%` | `0xdd4f66125d` |
| `SELL` | `8.82` | `86.3600` | 761.58 USD | 7,305,704.47 USD | `STANDARD` | `+0.13%` | `0x31ca8395cf` |
| `SELL` | `8.82` | `85.6800` | 755.62 USD | 7,307,980.60 USD | `STANDARD` | `+0.14%` | `0x010461c14e` |
| `SELL` | `8.82` | `82.4800` | 727.60 USD | 7,310,206.63 USD | `STANDARD` | `+0.16%` | `0x2eddf3aa5c` |
| `SELL` | `8.82` | `79.0400` | 696.79 USD | 7,312,322.63 USD | `STANDARD` | `+0.10%` | `0x2eddf3aa5c` |
| `SELL` | `8.82` | `66.8100` | 589.22 USD | 7,323,941.39 USD | `STANDARD` | `+0.14%` | `0x33ad48ed92` |
| `SELL` | `8.82` | `57.3100` | 505.67 USD | 7,326,053.06 USD | `STANDARD` | `+0.18%` | `0x57d8e75f47` |
| `SELL` | `8.82` | `57.3100` | 505.38 USD | 7,326,558.44 USD | `STANDARD` | `+0.13%` | `0x57d8e75f47` |
| `SELL` | `8.82` | `57.0000` | 502.95 USD | 7,329,582.83 USD | `STANDARD` | `+0.19%` | `0x6628f82999` |
| `SELL` | `8.83` | `16775.0700` | 148,045.03 USD | 3,957,916.59 USD | `LARGE (>= USD 100K)` | `+0.21%` | `0x71d0e11ebb` |
| `SELL` | `8.83` | `4218.8000` | 37,257.07 USD | 5,723,865.12 USD | `MEDIUM (>= USD 25K)` | `+0.27%` | `0x08a49e7f71` |
| `SELL` | `8.83` | `1666.8600` | 14,722.04 USD | 6,184,129.93 USD | `STANDARD` | `+0.28%` | `0x57d8e75f47` |
| `SELL` | `8.83` | `1666.8600` | 14,716.54 USD | 6,198,846.47 USD | `STANDARD` | `+0.25%` | `0x57d8e75f47` |
| `SELL` | `8.83` | `1666.8600` | 14,712.37 USD | 6,213,558.84 USD | `STANDARD` | `+0.22%` | `0x57d8e75f47` |
| `SELL` | `8.83` | `1137.9700` | 10,048.39 USD | 6,677,641.94 USD | `STANDARD` | `+0.26%` | `0xaf9f722a67` |
| `SELL` | `8.83` | `566.1500` | 4,999.95 USD | 6,970,916.89 USD | `STANDARD` | `+0.28%` | `0x0efb38a5fa` |
| `SELL` | `8.83` | `481.6400` | 4,251.77 USD | 7,016,892.48 USD | `STANDARD` | `+0.23%` | `0x7717a7a245` |
| `SELL` | `8.83` | `428.6600` | 3,784.30 USD | 7,036,532.02 USD | `STANDARD` | `+0.24%` | `0xecb63caa47` |
| `SELL` | `8.83` | `420.0000` | 3,708.98 USD | 7,040,241.00 USD | `STANDARD` | `+0.27%` | `0xb7bd9cef0e` |
| `SELL` | `8.83` | `403.9300` | 3,567.31 USD | 7,051,066.97 USD | `STANDARD` | `+0.28%` | `0x2a72b57dea` |
| `SELL` | `8.83` | `366.8200` | 3,239.09 USD | 7,112,677.09 USD | `STANDARD` | `+0.26%` | `0xdd4f66125d` |
| `SELL` | `8.83` | `308.0400` | 2,718.61 USD | 7,184,253.37 USD | `STANDARD` | `+0.21%` | `0xecb63caa47` |
| `SELL` | `8.83` | `267.2400` | 2,358.74 USD | 7,199,099.03 USD | `STANDARD` | `+0.22%` | `0x33ad48ed92` |
| `SELL` | `8.83` | `231.2300` | 2,042.64 USD | 7,220,198.38 USD | `STANDARD` | `+0.30%` | `0x9d732bed51` |
| `SELL` | `8.83` | `231.2300` | 2,041.62 USD | 7,222,240.00 USD | `STANDARD` | `+0.25%` | `0x9d732bed51` |
| `SELL` | `8.83` | `81.2200` | 717.28 USD | 7,310,923.91 USD | `STANDARD` | `+0.27%` | `0x010461c14e` |
| `SELL` | `8.83` | `79.4800` | 701.93 USD | 7,311,625.84 USD | `STANDARD` | `+0.28%` | `0x31ca8395cf` |
| `SELL` | `8.83` | `57.3100` | 506.02 USD | 7,325,547.39 USD | `STANDARD` | `+0.25%` | `0x57d8e75f47` |
| `SELL` | `8.84` | `1666.8600` | 14,741.54 USD | 6,125,211.60 USD | `STANDARD` | `+0.42%` | `0x57d8e75f47` |
| `SELL` | `8.84` | `1666.8600` | 14,736.54 USD | 6,139,948.14 USD | `STANDARD` | `+0.38%` | `0x57d8e75f47` |
| `SELL` | `8.84` | `1666.8600` | 14,732.38 USD | 6,154,680.51 USD | `STANDARD` | `+0.35%` | `0x57d8e75f47` |
| `SELL` | `8.84` | `1666.8600` | 14,727.37 USD | 6,169,407.89 USD | `STANDARD` | `+0.32%` | `0x57d8e75f47` |
| `SELL` | `8.84` | `951.7400` | 8,408.72 USD | 6,821,352.28 USD | `STANDARD` | `+0.32%` | `0xd3943e4008` |
| `SELL` | `8.84` | `735.9000` | 6,502.49 USD | 6,902,052.27 USD | `STANDARD` | `+0.33%` | `0xa38f19c4cc` |
| `SELL` | `8.84` | `668.1000` | 5,908.34 USD | 6,932,956.17 USD | `STANDARD` | `+0.41%` | `0x33ad48ed92` |
| `SELL` | `8.84` | `662.7100` | 5,859.09 USD | 6,950,619.55 USD | `STANDARD` | `+0.39%` | `0xecb63caa47` |
| `SELL` | `8.84` | `403.9300` | 3,570.05 USD | 7,047,499.66 USD | `STANDARD` | `+0.35%` | `0x2a72b57dea` |
| `SELL` | `8.84` | `366.8200` | 3,242.76 USD | 7,106,195.41 USD | `STANDARD` | `+0.38%` | `0xdd4f66125d` |
| `SELL` | `8.84` | `366.8200` | 3,242.58 USD | 7,109,437.99 USD | `STANDARD` | `+0.37%` | `0xdd4f66125d` |
| `SELL` | `8.84` | `303.9700` | 2,685.70 USD | 7,186,939.07 USD | `STANDARD` | `+0.32%` | `0xecb63caa47` |
| `SELL` | `8.84` | `231.2300` | 2,044.72 USD | 7,216,112.11 USD | `STANDARD` | `+0.40%` | `0x9d732bed51` |
| `SELL` | `8.84` | `231.2300` | 2,043.63 USD | 7,218,155.74 USD | `STANDARD` | `+0.35%` | `0x9d732bed51` |
| `SELL` | `8.85` | `14835.5900` | 131,280.14 USD | 4,236,495.48 USD | `LARGE (>= USD 100K)` | `+0.48%` | `0x71d0e11ebb` |
| `SELL` | `8.85` | `1666.8600` | 14,755.54 USD | 6,080,973.13 USD | `STANDARD` | `+0.51%` | `0x57d8e75f47` |
| `SELL` | `8.85` | `1666.8600` | 14,750.71 USD | 6,095,723.84 USD | `STANDARD` | `+0.48%` | `0x57d8e75f47` |
| `SELL` | `8.85` | `1666.8600` | 14,746.21 USD | 6,110,470.05 USD | `STANDARD` | `+0.45%` | `0x57d8e75f47` |
| `SELL` | `8.85` | `1249.5900` | 11,054.25 USD | 6,645,616.38 USD | `STANDARD` | `+0.44%` | `0xa38f19c4cc` |
| `SELL` | `8.85` | `1120.1700` | 9,909.92 USD | 6,757,639.34 USD | `STANDARD` | `+0.45%` | `0xd3342d3b1e` |
| `SELL` | `8.85` | `904.0700` | 7,999.93 USD | 6,845,352.50 USD | `STANDARD` | `+0.47%` | `0x0efb38a5fa` |
| `SELL` | `8.85` | `830.0000` | 7,348.32 USD | 6,860,700.60 USD | `STANDARD` | `+0.53%` | `0xb7bd9cef0e` |
| `SELL` | `8.85` | `789.4200` | 6,983.84 USD | 6,881,986.57 USD | `STANDARD` | `+0.45%` | `0x47a4471457` |
| `SELL` | `8.85` | `535.9600` | 4,741.48 USD | 6,995,469.95 USD | `STANDARD` | `+0.45%` | `0xecb63caa47` |
| `SELL` | `8.85` | `231.2300` | 2,046.71 USD | 7,212,021.65 USD | `STANDARD` | `+0.50%` | `0x9d732bed51` |
| `SELL` | `8.85` | `231.2300` | 2,045.74 USD | 7,214,067.39 USD | `STANDARD` | `+0.45%` | `0x9d732bed51` |
| `SELL` | `8.85` | `131.2700` | 1,161.60 USD | 7,285,826.74 USD | `STANDARD` | `+0.47%` | `0xe34d21d198` |
| `SELL` | `8.85` | `84.6200` | 748.84 USD | 7,309,479.04 USD | `STANDARD` | `+0.48%` | `0x010461c14e` |
| `SELL` | `8.85` | `75.6400` | 669.10 USD | 7,314,377.58 USD | `STANDARD` | `+0.44%` | `0x31ca8395cf` |
| `SELL` | `8.86` | `23896.9100` | 211,626.26 USD | 2,635,354.64 USD | `LARGE (>= USD 100K)` | `+0.55%` | `0x71cfa5e263` |
| `SELL` | `8.86` | `2120.5100` | 18,792.17 USD | 5,937,672.13 USD | `STANDARD` | `+0.62%` | `0xa38f19c4cc` |
| `SELL` | `8.86` | `1666.8600` | 14,770.55 USD | 6,036,690.50 USD | `STANDARD` | `+0.61%` | `0x57d8e75f47` |
| `SELL` | `8.86` | `1666.8600` | 14,765.71 USD | 6,051,456.21 USD | `STANDARD` | `+0.58%` | `0x57d8e75f47` |
| `SELL` | `8.86` | `1666.8600` | 14,761.38 USD | 6,066,217.59 USD | `STANDARD` | `+0.55%` | `0x57d8e75f47` |
| `SELL` | `8.86` | `1091.6500` | 9,668.63 USD | 6,777,156.52 USD | `STANDARD` | `+0.56%` | `0xd3943e4008` |
| `SELL` | `8.86` | `490.7400` | 4,349.23 USD | 6,999,819.18 USD | `STANDARD` | `+0.63%` | `0xcd7f60e943` |
| `SELL` | `8.86` | `231.2300` | 2,048.95 USD | 7,207,927.21 USD | `STANDARD` | `+0.61%` | `0x9d732bed51` |
| `SELL` | `8.86` | `231.2300` | 2,047.73 USD | 7,209,974.94 USD | `STANDARD` | `+0.55%` | `0x9d732bed51` |
| `SELL` | `8.87` | `1352.4700` | 11,999.93 USD | 6,565,149.49 USD | `STANDARD` | `+0.74%` | `0x0efb38a5fa` |
| `SELL` | `8.87` | `1281.1400` | 11,358.33 USD | 6,612,133.97 USD | `STANDARD` | `+0.67%` | `0xd3943e4008` |
| `SELL` | `8.87` | `1002.1400` | 8,888.28 USD | 6,795,611.20 USD | `STANDARD` | `+0.71%` | `0x33ad48ed92` |
| `SELL` | `8.87` | `384.5400` | 3,409.14 USD | 7,086,197.69 USD | `STANDARD` | `+0.66%` | `0x14f8e04290` |
| `SELL` | `8.87` | `131.2700` | 1,164.48 USD | 7,284,665.15 USD | `STANDARD` | `+0.72%` | `0xe34d21d198` |
| `SELL` | `8.87` | `85.7900` | 760.86 USD | 7,306,465.33 USD | `STANDARD` | `+0.70%` | `0x31ca8395cf` |
| `SELL` | `8.87` | `73.0200` | 647.60 USD | 7,317,012.17 USD | `STANDARD` | `+0.70%` | `0x010461c14e` |
| `SELL` | `8.88` | `17540.6300` | 155,748.52 USD | 3,352,544.87 USD | `LARGE (>= USD 100K)` | `+0.82%` | `0x71d0e11ebb` |
| `SELL` | `8.88` | `1447.8200` | 12,849.98 USD | 6,529,149.41 USD | `STANDARD` | `+0.77%` | `0xd3943e4008` |
| `SELL` | `8.88` | `1250.0000` | 11,095.50 USD | 6,634,562.13 USD | `STANDARD` | `+0.79%` | `0xb7bd9cef0e` |
| `SELL` | `8.89` | `11255.1000` | 100,112.99 USD | 5,254,614.86 USD | `LARGE (>= USD 100K)` | `+1.00%` | `0x881cd92459` |
| `SELL` | `8.89` | `3594.6900` | 31,946.73 USD | 5,860,632.70 USD | `MEDIUM (>= USD 25K)` | `+0.91%` | `0xa38f19c4cc` |
| `SELL` | `8.89` | `131.2700` | 1,167.44 USD | 7,283,500.66 USD | `STANDARD` | `+0.98%` | `0xe34d21d198` |
| `SELL` | `8.90` | `14209.6600` | 126,511.44 USD | 4,493,088.70 USD | `LARGE (>= USD 100K)` | `+1.09%` | `0xecb63caa47` |
| `SELL` | `8.90` | `1336.1900` | 11,897.03 USD | 6,589,044.12 USD | `STANDARD` | `+1.10%` | `0x33ad48ed92` |
| `SELL` | `8.90` | `565.0000` | 5,029.29 USD | 6,960,916.95 USD | `STANDARD` | `+1.07%` | `0x3ca146d269` |
| `SELL` | `8.90` | `382.5000` | 3,406.05 USD | 7,089,603.74 USD | `STANDARD` | `+1.11%` | `0x14f8e04290` |
| `SELL` | `8.91` | `46727.4000` | 416,504.68 USD | 2,015,672.52 USD | `LARGE (>= USD 100K)` | `+1.21%` | `0x71cfa5e263` |
| `SELL` | `8.91` | `4647.3700` | 41,402.95 USD | 5,686,608.05 USD | `MEDIUM (>= USD 25K)` | `+1.16%` | `0xa24c5ca26c` |
| `SELL` | `8.91` | `1794.7600` | 15,999.93 USD | 6,006,869.47 USD | `STANDARD` | `+1.22%` | `0x0efb38a5fa` |
| `SELL` | `8.91` | `224.9000` | 2,003.25 USD | 7,248,605.79 USD | `STANDARD` | `+1.14%` | `0x39bac00809` |
| `SELL` | `8.91` | `210.4600` | 1,874.99 USD | 7,252,474.23 USD | `STANDARD` | `+1.16%` | `0x0ad81cbc47` |
| `SELL` | `8.92` | `10959.6200` | 97,770.77 USD | 5,550,519.21 USD | `MEDIUM (>= USD 25K)` | `+1.29%` | `0xecb63caa47` |
| `SELL` | `8.92` | `1687.5000` | 15,050.47 USD | 6,021,919.95 USD | `STANDARD` | `+1.27%` | `0xd3943e4008` |
| `SELL` | `8.92` | `84.0500` | 749.59 USD | 7,308,730.19 USD | `STANDARD` | `+1.26%` | `0x010461c14e` |
| `SELL` | `8.92` | `70.8700` | 631.98 USD | 7,322,133.64 USD | `STANDARD` | `+1.25%` | `0x31ca8395cf` |
| `SELL` | `8.93` | `17532.2500` | 156,487.60 USD | 3,196,796.36 USD | `LARGE (>= USD 100K)` | `+1.35%` | `0x71d0e11ebb` |
| `SELL` | `8.93` | `111.4300` | 995.59 USD | 7,300,719.77 USD | `STANDARD` | `+1.45%` | `0x23cc6b8202` |
| `SELL` | `8.94` | `12909.6800` | 115,388.01 USD | 4,608,476.71 USD | `LARGE (>= USD 100K)` | `+1.49%` | `0x71d0e11ebb` |
| `SELL` | `8.94` | `12631.4300` | 112,911.09 USD | 4,835,158.27 USD | `LARGE (>= USD 100K)` | `+1.50%` | `0xecb63caa47` |
| `SELL` | `8.94` | `2263.7100` | 20,247.30 USD | 5,880,880.00 USD | `STANDARD` | `+1.56%` | `0xd3943e4008` |
| `SELL` | `8.94` | `2125.6100` | 18,999.98 USD | 5,918,879.96 USD | `STANDARD` | `+1.49%` | `0x0efb38a5fa` |
| `SELL` | `8.94` | `382.5900` | 3,418.75 USD | 7,082,788.55 USD | `STANDARD` | `+1.46%` | `0x14f8e04290` |
| `SELL` | `8.95` | `209.4900` | 1,874.94 USD | 7,254,349.17 USD | `STANDARD` | `+1.62%` | `0x0ad81cbc47` |
| `SELL` | `8.96` | `11173.0400` | 100,078.04 USD | 5,354,692.90 USD | `LARGE (>= USD 100K)` | `+1.70%` | `0xecb63caa47` |
| `SELL` | `8.97` | `383.1600` | 3,435.37 USD | 7,079,369.81 USD | `STANDARD` | `+1.80%` | `0x14f8e04290` |
| `SELL` | `8.97` | `315.7300` | 2,831.15 USD | 7,165,100.72 USD | `STANDARD` | `+1.82%` | `0x07fd993f0f` |
| `SELL` | `8.97` | `193.9600` | 1,739.98 USD | 7,263,219.31 USD | `STANDARD` | `+1.86%` | `0x31ca8395cf` |
| `SELL` | `8.97` | `162.3400` | 1,456.37 USD | 7,272,487.63 USD | `STANDARD` | `+1.86%` | `0x010461c14e` |
| `SELL` | `8.98` | `90808.1500` | 815,384.54 USD | 815,384.54 USD | `LARGE (>= USD 100K)` | `+1.95%` | `0x71cfa5e263` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:05:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1491` | `0x7737...bf66` | `SHORT` | 1,510,742.55 USD | `171,568.06` | `7.43` | `8.82` | `111.19` | -235,197.53 USD | `-15.57%` | `10X Cross` |
| `1578` | `0xeadc...9d55` | `LONG` | 1,409,501.32 USD | `160,070.56` | `8.11` | `8.82` | `0.000000` | 111,863.74 USD | `+7.94%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `8.94` | 5,181.55 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 5.18K USD at 8.9425 USD [API] | `2026-10-27 21:41:02` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`9.22` (Vol: 221,300.00 USD, Dist: `+4.32%`) | Long MP=`8.46` (Vol: 190,100.00 USD, Dist: `--4.33%`)
  * 48H Horizon: Short MP=`9.22` (Vol: 242,900.00 USD, Dist: `+4.32%`) | Long MP=`8.46` (Vol: 190,100.00 USD, Dist: `--4.33%`)
  * 3D Horizon: Short MP=`9.22` (Vol: 264,100.00 USD, Dist: `+4.32%`) | Long MP=`8.75` (Vol: 159,700.00 USD, Dist: `--1.00%`)
  * 7D Horizon: Short MP=`9.28` (Vol: 419,200.00 USD, Dist: `+4.99%`) | Long MP=`8.54` (Vol: 343,100.00 USD, Dist: `--3.44%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.86` | 205.15 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 229.50 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 159.60 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 111.40 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 372.09 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 263.45 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 814.80 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 17,510.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 1,680.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 268.14 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 600.69 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 1,090.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 674.12 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 1,500.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 404.38 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 293.24 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 297.24 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.71` | 2,110.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.81` | 2,130.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.83` | 8,720.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.94` | 1,290.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.12` | 412.50 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 159.29 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.18` | 174.89 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.21` | 113.53 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.21` | 171.17 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.32` | 852.47 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.38` | 210.96 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.42` | 2,230.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 1,160.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 2,680.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 15,400.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.71` | 1,270.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.74` | 4,990.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 240.48 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.79` | 15,760.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.86` | 112.64 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 146.85 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 527.19 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 4,080.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.99` | 329.11 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 167.78 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 314.59 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 484.57 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 318.46 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 156,680.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 2,300.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 300.91 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 640.70 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.30` | 2,880.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.36` | 589.05 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 21,080.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.51` | 367.41 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 121.38 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.57` | 967.98 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.59` | 34,430.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 22,590.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.64` | 4,120.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.68` | 404.32 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 2,340.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 238.86 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 2,890.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 736.72 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 326,400.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 22,060.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 2,120.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.99` | 447.98 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 1,690.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 105.61 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 405.14 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,550.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.11` | 5,560.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 4,390.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 187.29 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 2,560.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.22` | 715.31 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 971.10 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 2,060.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.26` | 1,450.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.29` | 147.51 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.32` | 277.04 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 105.25 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 5,110.00 USD | 894,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 1,690.00 USD | 889,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 888,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 887,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 880,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 3,620.00 USD | 879,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 876,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 1,100.00 USD | 867,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.59` | 408.89 USD | 866,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 865,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.70` | 506.54 USD | 863,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 19,850.00 USD | 863,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 843,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 6,780.00 USD | 841,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 16,960.00 USD | 835,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 4,260.00 USD | 818,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 814,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 2,670.00 USD | 812,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 158.14 USD | 809,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 4,410.00 USD | 809,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.86` | 18,930.00 USD | 805,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 786,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 1,380.00 USD | 782,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.89` | 32,830.00 USD | 781,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.91` | 269.30 USD | 748,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,760.00 USD | 748,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 3,480.00 USD | 744,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 741,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 746.58 USD | 740,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 22,390.00 USD | 739,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.04` | 811.35 USD | 717,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.04` | 4,100.00 USD | 716,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 712,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,670.00 USD | 705,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.09` | 1,620.00 USD | 704,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,230.00 USD | 702,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 674,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 2,300.00 USD | 674,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,950.00 USD | 671,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 650,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 581.02 USD | 649,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.24` | 179.65 USD | 648,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 648,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,560.00 USD | 648,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 19,790.00 USD | 611,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.32` | 168.76 USD | 592,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 4,910.00 USD | 591,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 2,450.00 USD | 586,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 4,370.00 USD | 584,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.36` | 1,030.00 USD | 580,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.37` | 5,720.00 USD | 579,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 3,920.00 USD | 573,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 17,770.00 USD | 569,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.39` | 1,550.00 USD | 551,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.42` | 1,480.00 USD | 550,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.42` | 500.00 USD | 548,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 210.99 USD | 548,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 1,370.00 USD | 547,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 546,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 3,210.00 USD | 541,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,580.00 USD | 538,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,080.00 USD | 537,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.53` | 995.86 USD | 536,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 535,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 157.14 USD | 530,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.57` | 4,380.00 USD | 530,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.59` | 25,140.00 USD | 526,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 312.22 USD | 501,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 500,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.63` | 514.52 USD | 500,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 499,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.67` | 1,740.00 USD | 499,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.68` | 1,120.00 USD | 497,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.70` | 1,460.00 USD | 496,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.71` | 19,410.00 USD | 495,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.72` | 2,550.00 USD | 475,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 893.76 USD | 473,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.76` | 9,520,000.00 USD | 9,520,000.00 USD | 1,790.00 USD | 5,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 472,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.78` | 695.32 USD | 471,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.78` | 9,520,000.00 USD | 9,520,000.00 USD | 23,430.00 USD | 4,900.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,900.00 USD | 471,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 1,940.00 USD | 467,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.80` | 9,470,000.00 USD | 9,470,000.00 USD | 13,050.00 USD | 12,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 633.77 USD | 465,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.82` | 5,280.00 USD | 464,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.82` | 9,440,000.00 USD | 9,440,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 9,430,000.00 USD | 9,430,000.00 USD | 29,020.00 USD | 2,380.00 USD | 19,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 10,930.00 USD | 459,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.86` | 2,110.00 USD | 448,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.86` | 9,380,000.00 USD | 9,380,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 176.18 USD | 446,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 446,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.88` | 9,330,000.00 USD | 9,330,000.00 USD | 46,450.00 USD | 12,780.00 USD | 29,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 9,240,000.00 USD | 9,240,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 2,410.00 USD | 445,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.92` | 9,180,000.00 USD | 9,180,000.00 USD | 53,660.00 USD | 8,420.00 USD | 14,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 923.42 USD | 443,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 4,910,000.00 USD | 4,910,000.00 USD | 12,900.00 USD | 2,950.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 1,820.00 USD | 442,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 4,890,000.00 USD | 4,890,000.00 USD | 7,510.00 USD | 4,150.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.94` | 9,100,000.00 USD | 9,100,000.00 USD | 38,370.00 USD | 9,960.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 440,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 4,880,000.00 USD | 4,880,000.00 USD | 74.90 USD | 4,140.00 USD | 2,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 843.15 USD | 313,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 4,870,000.00 USD | 4,870,000.00 USD | 133.15 USD | 1,790.00 USD | 8.59 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.96` | 9,020,000.00 USD | 9,020,000.00 USD | 21,840.00 USD | 6,920.00 USD | 26,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.97` | 4,870,000.00 USD | 4,870,000.00 USD | 5,250.00 USD | 0.00 USD | 2,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.98` | 4,860,000.00 USD | 4,860,000.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.98` | 8,970,000.00 USD | 8,970,000.00 USD | 43,200.00 USD | 19,680.00 USD | 70,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,600.00 USD | 312,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 4,850,000.00 USD | 4,850,000.00 USD | 675.88 USD | 677.82 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 210.99 USD | 310,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 4,850,000.00 USD | 4,850,000.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.00` | 8,830,000.00 USD | 8,830,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 4,850,000.00 USD | 4,850,000.00 USD | 6,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 4,840,000.00 USD | 4,840,000.00 USD | 9,100.00 USD | 770.83 USD | 9.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.02` | 8,760,000.00 USD | 8,760,000.00 USD | 20,910.00 USD | 28,440.00 USD | 10,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 957.70 USD | 310,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 4,830,000.00 USD | 4,830,000.00 USD | 9,140.00 USD | 1,540.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 88,380.00 USD | 309,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.04` | 4,810,000.00 USD | 4,810,000.00 USD | 9,860.00 USD | 0.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.04` | 8,700,000.00 USD | 8,700,000.00 USD | 123,080.00 USD | 27,860.00 USD | 86,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 6,890.00 USD | 221,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.05` | 4,790,000.00 USD | 4,790,000.00 USD | 17,150.00 USD | 4,800.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.05` | 3,340.00 USD | 214,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.06` | 4,770,000.00 USD | 4,770,000.00 USD | 17,130.00 USD | 1,700.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.06` | 8,460,000.00 USD | 8,460,000.00 USD | 70,840.00 USD | 10,070.00 USD | 86,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 37,830.00 USD | 211,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 4,740,000.00 USD | 4,740,000.00 USD | 1,100.00 USD | 2,400.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.08` | 4,730,000.00 USD | 4,730,000.00 USD | 4,700.00 USD | 1,410.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.08` | 8,290,000.00 USD | 8,290,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 617.61 USD | 173,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.09` | 4,720,000.00 USD | 4,720,000.00 USD | 9,630.00 USD | 1,220.00 USD | 6,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.10` | 11,700.00 USD | 172,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.10` | 4,710,000.00 USD | 4,710,000.00 USD | 23,830.00 USD | 3,750.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.10` | 8,250,000.00 USD | 8,250,000.00 USD | 61,500.00 USD | 19,700.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.11` | 4,670,000.00 USD | 4,670,000.00 USD | 4,510.00 USD | 4,240.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 241.26 USD | 160,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 4,660,000.00 USD | 4,660,000.00 USD | 9,910.00 USD | 0.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.12` | 8,160,000.00 USD | 8,160,000.00 USD | 27,520.00 USD | 10,810.00 USD | 9,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 233.92 USD | 160,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.13` | 4,640,000.00 USD | 4,640,000.00 USD | 7,130.00 USD | 693.45 USD | 1,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 4,640,000.00 USD | 4,640,000.00 USD | 16,900.00 USD | 0.00 USD | 26.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.14` | 8,110,000.00 USD | 8,110,000.00 USD | 72,460.00 USD | 11,150.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 4,620,000.00 USD | 4,620,000.00 USD | 14,590.00 USD | 662.47 USD | 5,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 4,600,000.00 USD | 4,600,000.00 USD | 385.98 USD | 2,120.00 USD | 47.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 7,990,000.00 USD | 7,990,000.00 USD | 38,430.00 USD | 5,510.00 USD | 30,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.16` | 871.61 USD | 160,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.17` | 4,600,000.00 USD | 4,600,000.00 USD | 2,970.00 USD | 0.00 USD | 12.32 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 4,590,000.00 USD | 4,590,000.00 USD | 1,150.00 USD | 1,980.00 USD | 466.21 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 7,910,000.00 USD | 7,910,000.00 USD | 10,520.00 USD | 6,790.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.19` | 4,030.00 USD | 159,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.19` | 4,590,000.00 USD | 4,590,000.00 USD | 4,450.00 USD | 0.00 USD | 19.88 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.20` | 2,380.00 USD | 155,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.20` | 4,580,000.00 USD | 4,580,000.00 USD | 7,720.00 USD | 2,310.00 USD | 431.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.20` | 7,890,000.00 USD | 7,890,000.00 USD | 34,140.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 577.06 USD | 153,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.21` | 4,570,000.00 USD | 4,570,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 147.87 USD | 152,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.22` | 4,570,000.00 USD | 4,570,000.00 USD | 5,330.00 USD | 0.00 USD | 12,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.22` | 7,850,000.00 USD | 7,850,000.00 USD | 19,850.00 USD | 0.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.22` | 2,100.00 USD | 152,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.23` | 4,550,000.00 USD | 4,550,000.00 USD | 20,790.00 USD | 4,080.00 USD | 31,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.23` | 1,160.00 USD | 150,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.24` | 4,500,000.00 USD | 4,500,000.00 USD | 10,190.00 USD | 1,150.00 USD | 3,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 7,820,000.00 USD | 7,820,000.00 USD | 39,950.00 USD | 3,480.00 USD | 107,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.24` | 1,300.00 USD | 149,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.25` | 4,480,000.00 USD | 4,480,000.00 USD | 8,080.00 USD | 0.00 USD | 6,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.26` | 13,810.00 USD | 147,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.26` | 4,470,000.00 USD | 4,470,000.00 USD | 192.60 USD | 11,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.26` | 7,670,000.00 USD | 7,670,000.00 USD | 30,490.00 USD | 5,750.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.27` | 6,110.00 USD | 134,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.27` | 4,460,000.00 USD | 4,460,000.00 USD | 11,310.00 USD | 2,760.00 USD | 21.52 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.28` | 3,190.00 USD | 128,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.28` | 4,440,000.00 USD | 4,440,000.00 USD | 74,500.00 USD | 7,070.00 USD | 40,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.28` | 7,620,000.00 USD | 7,620,000.00 USD | 122,850.00 USD | 33,920.00 USD | 14,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 498.26 USD | 124,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.29` | 4,320,000.00 USD | 4,320,000.00 USD | 35,140.00 USD | 9,470.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 18,970.00 USD | 124,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.30` | 4,270,000.00 USD | 4,270,000.00 USD | 53,200.00 USD | 13,130.00 USD | 19,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.30` | 7,450,000.00 USD | 7,450,000.00 USD | 101,900.00 USD | 13,500.00 USD | 47,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.30` | 33,500.00 USD | 105,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.31` | 4,190,000.00 USD | 4,190,000.00 USD | 56,000.00 USD | 11,410.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.31` | 4,550.00 USD | 71,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.32` | 4,120,000.00 USD | 4,120,000.00 USD | 20,190.00 USD | 4,190.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.32` | 7,290,000.00 USD | 7,290,000.00 USD | 61,880.00 USD | 26,020.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 4,090,000.00 USD | 4,090,000.00 USD | 2,970.00 USD | 22,580.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.34` | 4,630.00 USD | 67,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.34` | 4,050,000.00 USD | 4,050,000.00 USD | 14,500.00 USD | 4,810.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.34` | 7,200,000.00 USD | 7,200,000.00 USD | 37,760.00 USD | 15,520.00 USD | 30,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 4,020,000.00 USD | 4,020,000.00 USD | 6,790.00 USD | 11,270.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.36` | 3,180.00 USD | 62,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.36` | 3,990,000.00 USD | 3,990,000.00 USD | 4,230.00 USD | 2,420.00 USD | 21,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.36` | 7,110,000.00 USD | 7,110,000.00 USD | 107,760.00 USD | 13,470.00 USD | 71,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.37` | 7,160.00 USD | 59,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.37` | 3,960,000.00 USD | 3,960,000.00 USD | 21,970.00 USD | 7,980.00 USD | 8,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.38` | 223.70 USD | 52,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.38` | 3,920,000.00 USD | 3,920,000.00 USD | 35,970.00 USD | 4,080.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.38` | 6,920,000.00 USD | 6,920,000.00 USD | 143,540.00 USD | 20,560.00 USD | 66,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.39` | 3,850,000.00 USD | 3,850,000.00 USD | 63,440.00 USD | 10,540.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.39` | 1,680.00 USD | 52,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.40` | 3,720,000.00 USD | 3,720,000.00 USD | 67,650.00 USD | 22,890.00 USD | 67,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.40` | 6,690,000.00 USD | 6,690,000.00 USD | 150,350.00 USD | 19,710.00 USD | 220,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.40` | 1,280.00 USD | 50,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.41` | 3,560,000.00 USD | 3,560,000.00 USD | 33,190.00 USD | 3,620.00 USD | 20,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.42` | 3,500,000.00 USD | 3,500,000.00 USD | 33,600.00 USD | 12,790.00 USD | 18,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.42` | 6,300,000.00 USD | 6,300,000.00 USD | 178,300.00 USD | 57,340.00 USD | 72,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.43` | 3,440,000.00 USD | 3,440,000.00 USD | 29,980.00 USD | 34,530.00 USD | 14,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.44` | 188.61 USD | 49,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.44` | 3,360,000.00 USD | 3,360,000.00 USD | 35,960.00 USD | 8,900.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.44` | 5,990,000.00 USD | 5,990,000.00 USD | 155,040.00 USD | 68,350.00 USD | 76,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.45` | 588.70 USD | 48,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.45` | 3,310,000.00 USD | 3,310,000.00 USD | 73,020.00 USD | 14,270.00 USD | 45,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.46` | 4,100.00 USD | 48,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.46` | 3,180,000.00 USD | 3,180,000.00 USD | 133,440.00 USD | 8,250.00 USD | 47,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.46` | 5,690,000.00 USD | 5,690,000.00 USD | 392,550.00 USD | 59,170.00 USD | 107,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.46` | 2,840.00 USD | 44,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.47` | 2,990,000.00 USD | 2,990,000.00 USD | 103,290.00 USD | 30,070.00 USD | 15,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.47` | 12,890.00 USD | 41,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.48` | 2,840,000.00 USD | 2,840,000.00 USD | 126,360.00 USD | 36,620.00 USD | 46,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.48` | 5,130,000.00 USD | 5,130,000.00 USD | 317,690.00 USD | 61,660.00 USD | 220,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.48` | 1,160.00 USD | 28,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.49` | 2,630,000.00 USD | 2,630,000.00 USD | 121,830.00 USD | 32,760.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.49` | 403.51 USD | 27,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.50` | 2,470,000.00 USD | 2,470,000.00 USD | 51,910.00 USD | 11,120.00 USD | 26,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.50` | 4,530,000.00 USD | 4,530,000.00 USD | 191,430.00 USD | 100,070.00 USD | 112,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.51` | 6,380.00 USD | 26,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.51` | 2,380,000.00 USD | 2,380,000.00 USD | 8,030.00 USD | 46,200.00 USD | 20,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.52` | 8,060.00 USD | 20,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.52` | 2,300,000.00 USD | 2,300,000.00 USD | 48,940.00 USD | 18,950.00 USD | 23,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.52` | 4,130,000.00 USD | 4,130,000.00 USD | 271,100.00 USD | 98,920.00 USD | 250,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.53` | 2,210,000.00 USD | 2,210,000.00 USD | 17,330.00 USD | 29,630.00 USD | 41,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 6,350.00 USD | 12,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.54` | 2,120,000.00 USD | 2,120,000.00 USD | 19,400.00 USD | 6,040.00 USD | 43,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.54` | 3,510,000.00 USD | 3,510,000.00 USD | 379,850.00 USD | 78,380.00 USD | 152,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 1,550.00 USD | 6,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.55` | 2,060,000.00 USD | 2,060,000.00 USD | 64,630.00 USD | 19,250.00 USD | 19,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.55` | 1,660.00 USD | 4,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.56` | 1,950,000.00 USD | 1,950,000.00 USD | 69,420.00 USD | 12,010.00 USD | 67,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.56` | 2,900,000.00 USD | 2,900,000.00 USD | 593,510.00 USD | 101,070.00 USD | 88,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.57` | 1,800,000.00 USD | 1,800,000.00 USD | 73,460.00 USD | 11,140.00 USD | 73,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.58` | 1,650,000.00 USD | 1,650,000.00 USD | 87,680.00 USD | 21,440.00 USD | 39,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.58` | 2,110,000.00 USD | 2,110,000.00 USD | 541,170.00 USD | 164,810.00 USD | 45,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.59` | 1,500,000.00 USD | 1,500,000.00 USD | 70,460.00 USD | 29,830.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.60` | 1,370,000.00 USD | 1,370,000.00 USD | 68,090.00 USD | 23,230.00 USD | 39,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.60` | 1,360,000.00 USD | 1,360,000.00 USD | 75,040.00 USD | 39,160.00 USD | 206,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.61` | 2,980.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.61` | 1,240,000.00 USD | 1,240,000.00 USD | 35,340.00 USD | 12,770.00 USD | 26,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.62` | 1,160,000.00 USD | 1,160,000.00 USD | 102,610.00 USD | 17,600.00 USD | 23,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.62` | 1,040,000.00 USD | 1,040,000.00 USD | 13,680.00 USD | 43,670.00 USD | 78,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.63` | 1,020,000.00 USD | 1,020,000.00 USD | 38,050.00 USD | 2,010.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.64` | 971,830.00 USD | 971,830.00 USD | 68,660.00 USD | 11,790.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.64` | 906,450.00 USD | 906,450.00 USD | 73,980.00 USD | 5,680.00 USD | 10,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.65` | 880,280.00 USD | 880,280.00 USD | 50,810.00 USD | 26,390.00 USD | 19,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.66` | 783,890.00 USD | 783,890.00 USD | 36,050.00 USD | 19,900.00 USD | 10,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.66` | 816,140.00 USD | 816,140.00 USD | 23,060.00 USD | 16,520.00 USD | 37,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.67` | 717,750.00 USD | 717,750.00 USD | 33,710.00 USD | 5,480.00 USD | 23,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.68` | 655,400.00 USD | 655,400.00 USD | 21,030.00 USD | 0.00 USD | 56.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.68` | 739,010.00 USD | 739,010.00 USD | 93,990.00 USD | 24,870.00 USD | 173,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.69` | 634,310.00 USD | 634,310.00 USD | 18,040.00 USD | 5,700.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.70` | 588,390.00 USD | 588,390.00 USD | 34,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.70` | 446,480.00 USD | 446,480.00 USD | 0.00 USD | 12,790.00 USD | 22,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.71` | 554,020.00 USD | 554,020.00 USD | 18,250.00 USD | 11,690.00 USD | 18,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.73` | 505,100.00 USD | 505,100.00 USD | 44,990.00 USD | 2,720.00 USD | 5,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.74` | 452,270.00 USD | 452,270.00 USD | 0.00 USD | 7,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.74` | 411,400.00 USD | 411,400.00 USD | 144,660.00 USD | 19,690.00 USD | 56,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.75` | 444,550.00 USD | 444,550.00 USD | 32,080.00 USD | 8,290.00 USD | 35,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.76` | 368,350.00 USD | 368,350.00 USD | 78,530.00 USD | 15,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.76` | 190,450.00 USD | 190,450.00 USD | 26,810.00 USD | 0.00 USD | 22,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.77` | 274,780.00 USD | 274,780.00 USD | 54,300.00 USD | 8,510.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.78` | 186,250.00 USD | 186,250.00 USD | 19,230.00 USD | 0.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.78` | 141,240.00 USD | 141,240.00 USD | 0.00 USD | 0.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.79` | 157,140.00 USD | 157,140.00 USD | 13,010.00 USD | 12,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.80` | 132,130.00 USD | 132,130.00 USD | 30,940.00 USD | 5,690.00 USD | 6,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.80` | 82,400.00 USD | 82,400.00 USD | 27,360.00 USD | 33,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.81` | 88,900.00 USD | 88,900.00 USD | 26,650.00 USD | 0.00 USD | 10,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.82` | 51,300.00 USD | 51,300.00 USD | 8,370.00 USD | 0.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.82` | 21,290.00 USD | 21,290.00 USD | 0.00 USD | 0.00 USD | 21,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.83` | 27,060.00 USD | 27,060.00 USD | 21,850.00 USD | 0.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 98,130.00 USD | 98,130.00 USD | 29,490.00 USD | 0.00 USD | 68,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 196,250.00 USD | 196,250.00 USD | 29,490.00 USD | 0.00 USD | 68,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 263,630.00 USD | 263,630.00 USD | 67,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 341,400.00 USD | 341,400.00 USD | 0.00 USD | 0.00 USD | 77,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.90` | 115,480.00 USD | 115,480.00 USD | 0.00 USD | 0.00 USD | 115,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 352,960.00 USD | 352,960.00 USD | 8,060.00 USD | 0.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 365,080.00 USD | 365,080.00 USD | 643.50 USD | 11,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.00` | 288,400.00 USD | 288,400.00 USD | 161,560.00 USD | 11,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 366,160.00 USD | 366,160.00 USD | 1,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 390,250.00 USD | 390,250.00 USD | 0.00 USD | 24,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.02` | 346,850.00 USD | 346,850.00 USD | 2,330.00 USD | 56,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 470,690.00 USD | 470,690.00 USD | 29,210.00 USD | 28,060.00 USD | 23,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 484,470.00 USD | 484,470.00 USD | 0.00 USD | 4,810.00 USD | 8,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.04` | 472,790.00 USD | 472,790.00 USD | 36,040.00 USD | 74,750.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 552,770.00 USD | 552,770.00 USD | 3,520.00 USD | 26,530.00 USD | 38,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.06` | 607,490.00 USD | 607,490.00 USD | 27,120.00 USD | 5,810.00 USD | 21,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.06` | 532,500.00 USD | 532,500.00 USD | 5,610.00 USD | 14,960.00 USD | 39,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 671,500.00 USD | 671,500.00 USD | 14,580.00 USD | 22,140.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 713,120.00 USD | 713,120.00 USD | 1,260.00 USD | 6,490.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.08` | 609,550.00 USD | 609,550.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 871,680.00 USD | 871,680.00 USD | 99,950.00 USD | 17,120.00 USD | 41,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.10` | 987,680.00 USD | 987,680.00 USD | 66,840.00 USD | 22,440.00 USD | 26,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.10` | 1,770,000.00 USD | 1,770,000.00 USD | 797,340.00 USD | 35,760.00 USD | 325,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 1,100,000.00 USD | 1,100,000.00 USD | 51,780.00 USD | 9,610.00 USD | 49,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 1,240,000.00 USD | 1,240,000.00 USD | 106,750.00 USD | 31,620.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.12` | 2,760,000.00 USD | 2,760,000.00 USD | 490,020.00 USD | 24,170.00 USD | 479,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 1,390,000.00 USD | 1,390,000.00 USD | 84,020.00 USD | 20,120.00 USD | 40,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.13` | 314.34 USD | 314.34 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.14` | 1,460,000.00 USD | 1,460,000.00 USD | 33,890.00 USD | 8,440.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.14` | 3,800,000.00 USD | 3,800,000.00 USD | 536,560.00 USD | 18,540.00 USD | 479,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.15` | 1,550,000.00 USD | 1,550,000.00 USD | 57,880.00 USD | 19,380.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 1,630,000.00 USD | 1,630,000.00 USD | 43,310.00 USD | 9,390.00 USD | 27,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.16` | 4,390,000.00 USD | 4,390,000.00 USD | 358,370.00 USD | 44,360.00 USD | 195,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 1,800,000.00 USD | 1,800,000.00 USD | 89,060.00 USD | 18,740.00 USD | 55,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 2,040,000.00 USD | 2,040,000.00 USD | 151,850.00 USD | 37,610.00 USD | 58,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.18` | 5,330,000.00 USD | 5,330,000.00 USD | 506,170.00 USD | 162,460.00 USD | 263,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 2,180,000.00 USD | 2,180,000.00 USD | 78,860.00 USD | 36,770.00 USD | 14,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.20` | 2,360,000.00 USD | 2,360,000.00 USD | 106,980.00 USD | 10,810.00 USD | 65,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 6,210,000.00 USD | 6,210,000.00 USD | 520,860.00 USD | 120,080.00 USD | 238,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 2,410,000.00 USD | 2,410,000.00 USD | 39,120.00 USD | 4,510.00 USD | 8,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.22` | 2,530,000.00 USD | 2,530,000.00 USD | 93,870.00 USD | 10,040.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.22` | 7,350,000.00 USD | 7,350,000.00 USD | 585,170.00 USD | 140,390.00 USD | 416,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 2,620,000.00 USD | 2,620,000.00 USD | 57,020.00 USD | 3,310.00 USD | 33,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 2,650,000.00 USD | 2,650,000.00 USD | 30,460.00 USD | 2,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 7,890,000.00 USD | 7,890,000.00 USD | 316,220.00 USD | 52,090.00 USD | 174,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 2,700,000.00 USD | 2,700,000.00 USD | 18,710.00 USD | 17,700.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 2,720,000.00 USD | 2,720,000.00 USD | 16,080.00 USD | 1,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 8,320,000.00 USD | 8,320,000.00 USD | 273,920.00 USD | 96,980.00 USD | 60,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 2,750,000.00 USD | 2,750,000.00 USD | 22,870.00 USD | 13,170.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 2,790,000.00 USD | 2,790,000.00 USD | 20,250.00 USD | 3,860.00 USD | 10,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 9,020,000.00 USD | 9,020,000.00 USD | 428,160.00 USD | 103,490.00 USD | 170,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 100.93 USD | 415.26 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.29` | 2,890,000.00 USD | 2,890,000.00 USD | 48,940.00 USD | 18,260.00 USD | 31,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.30` | 2,970,000.00 USD | 2,970,000.00 USD | 58,500.00 USD | 16,060.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.30` | 9,590,000.00 USD | 9,590,000.00 USD | 199,810.00 USD | 97,780.00 USD | 262,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 3,040,000.00 USD | 3,040,000.00 USD | 39,620.00 USD | 4,250.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 3,060,000.00 USD | 3,060,000.00 USD | 10,000.00 USD | 2,530.00 USD | 10,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.32` | 10,250,000.00 USD | 10,250,000.00 USD | 271,660.00 USD | 59,310.00 USD | 337,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 3,100,000.00 USD | 3,100,000.00 USD | 16,620.00 USD | 6,000.00 USD | 15,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.34` | 1,060.00 USD | 1,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.34` | 3,130,000.00 USD | 3,130,000.00 USD | 15,860.00 USD | 4,190.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.34` | 10,580,000.00 USD | 10,580,000.00 USD | 203,440.00 USD | 53,150.00 USD | 70,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.35` | 3,930.00 USD | 5,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.35` | 3,190,000.00 USD | 3,190,000.00 USD | 28,980.00 USD | 3,810.00 USD | 24,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 3,300,000.00 USD | 3,300,000.00 USD | 66,220.00 USD | 13,630.00 USD | 25,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.36` | 11,020,000.00 USD | 11,020,000.00 USD | 247,120.00 USD | 78,550.00 USD | 112,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 3,350,000.00 USD | 3,350,000.00 USD | 37,700.00 USD | 13,410.00 USD | 6,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 3,430,000.00 USD | 3,430,000.00 USD | 47,540.00 USD | 4,040.00 USD | 27,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.38` | 11,540,000.00 USD | 11,540,000.00 USD | 383,530.00 USD | 55,400.00 USD | 85,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.38` | 404,120.00 USD | 409,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.39` | 3,450,000.00 USD | 3,450,000.00 USD | 16,470.00 USD | 1,730.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 3,500,000.00 USD | 3,500,000.00 USD | 44,280.00 USD | 1,210.00 USD | 12.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.40` | 11,990,000.00 USD | 11,990,000.00 USD | 234,760.00 USD | 58,130.00 USD | 153,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 3,550,000.00 USD | 3,550,000.00 USD | 30,150.00 USD | 1,660.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 2,470.00 USD | 411,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 3,560,000.00 USD | 3,560,000.00 USD | 10,620.00 USD | 622.99 USD | 4,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.42` | 12,300,000.00 USD | 12,300,000.00 USD | 176,920.00 USD | 44,410.00 USD | 84,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.43` | 3,590,000.00 USD | 3,590,000.00 USD | 10,390.00 USD | 6,940.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 3,590,000.00 USD | 3,590,000.00 USD | 1,500.00 USD | 0.00 USD | 48.84 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 12,410,000.00 USD | 12,410,000.00 USD | 41,250.00 USD | 19,420.00 USD | 56,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 3,600,000.00 USD | 3,600,000.00 USD | 1,380.00 USD | 4,940.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.46` | 3,010.00 USD | 414,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.46` | 3,610,000.00 USD | 3,610,000.00 USD | 1,320.00 USD | 4,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 12,600,000.00 USD | 12,600,000.00 USD | 136,670.00 USD | 29,830.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.47` | 3,630,000.00 USD | 3,630,000.00 USD | 18,510.00 USD | 6,870.00 USD | 192.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.48` | 3,640,000.00 USD | 3,640,000.00 USD | 1,510.00 USD | 0.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.48` | 12,670,000.00 USD | 12,670,000.00 USD | 12,180.00 USD | 30,160.00 USD | 25,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 3,670,000.00 USD | 3,670,000.00 USD | 21,080.00 USD | 572.85 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.50` | 3,690,000.00 USD | 3,690,000.00 USD | 11,990.00 USD | 3,160.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 12,850,000.00 USD | 12,850,000.00 USD | 69,270.00 USD | 33,210.00 USD | 83,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.51` | 3,690,000.00 USD | 3,690,000.00 USD | 295.05 USD | 0.00 USD | 124.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.52` | 3,720,000.00 USD | 3,720,000.00 USD | 17,990.00 USD | 3,070.00 USD | 5,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 13,040,000.00 USD | 13,040,000.00 USD | 102,150.00 USD | 29,320.00 USD | 51,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.53` | 3,740,000.00 USD | 3,740,000.00 USD | 18,780.00 USD | 4,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.54` | 3,750,000.00 USD | 3,750,000.00 USD | 5,910.00 USD | 1,470.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 13,260,000.00 USD | 13,260,000.00 USD | 192,090.00 USD | 27,650.00 USD | 930.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.55` | 3,760,000.00 USD | 3,760,000.00 USD | 2,910.00 USD | 6,330.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.56` | 3,770,000.00 USD | 3,770,000.00 USD | 5,490.00 USD | 1,280.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 13,380,000.00 USD | 13,380,000.00 USD | 89,210.00 USD | 5,260.00 USD | 32,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.57` | 3,780,000.00 USD | 3,780,000.00 USD | 1,370.00 USD | 3,100.00 USD | 4,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.58` | 3,790,000.00 USD | 3,790,000.00 USD | 1,290.00 USD | 563.17 USD | 7,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 13,460,000.00 USD | 13,460,000.00 USD | 35,340.00 USD | 16,980.00 USD | 21,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.59` | 3,800,000.00 USD | 3,800,000.00 USD | 5,050.00 USD | 1,250.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.60` | 3,820,000.00 USD | 3,820,000.00 USD | 11,210.00 USD | 424.36 USD | 11,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 13,540,000.00 USD | 13,540,000.00 USD | 39,470.00 USD | 10,820.00 USD | 33,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.61` | 3,850,000.00 USD | 3,850,000.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.62` | 3,850,000.00 USD | 3,850,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 13,640,000.00 USD | 13,640,000.00 USD | 70,470.00 USD | 13,850.00 USD | 17,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.63` | 3,870,000.00 USD | 3,870,000.00 USD | 10,190.00 USD | 4,370.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.64` | 3,870,000.00 USD | 3,870,000.00 USD | 5,830.00 USD | 0.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.64` | 13,740,000.00 USD | 13,740,000.00 USD | 61,870.00 USD | 17,650.00 USD | 19,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.65` | 3,890,000.00 USD | 3,890,000.00 USD | 5,960.00 USD | 4,150.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.66` | 3,900,000.00 USD | 3,900,000.00 USD | 8,930.00 USD | 3,480.00 USD | 5,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.66` | 13,820,000.00 USD | 13,820,000.00 USD | 37,340.00 USD | 21,280.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.67` | 3,910,000.00 USD | 3,910,000.00 USD | 2,990.00 USD | 0.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.68` | 3,930,000.00 USD | 3,930,000.00 USD | 12,900.00 USD | 2,950.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.68` | 13,940,000.00 USD | 13,940,000.00 USD | 68,230.00 USD | 20,310.00 USD | 34,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.70` | 3,940,000.00 USD | 3,940,000.00 USD | 7,510.00 USD | 4,150.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.70` | 14,060,000.00 USD | 14,060,000.00 USD | 69,040.00 USD | 12,990.00 USD | 31,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.71` | 3,950,000.00 USD | 3,950,000.00 USD | 74.90 USD | 4,140.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.72` | 3,950,000.00 USD | 3,950,000.00 USD | 133.15 USD | 1,790.00 USD | 52.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.72` | 14,160,000.00 USD | 14,160,000.00 USD | 71,790.00 USD | 6,920.00 USD | 26,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 415,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.74` | 3,960,000.00 USD | 3,960,000.00 USD | 5,250.00 USD | 0.00 USD | 2,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.74` | 14,200,000.00 USD | 14,200,000.00 USD | 10,890.00 USD | 7,200.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.75` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 42.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.76` | 3,970,000.00 USD | 3,970,000.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.76` | 14,300,000.00 USD | 14,300,000.00 USD | 35,520.00 USD | 12,480.00 USD | 52,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.77` | 549.67 USD | 415,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.77` | 3,970,000.00 USD | 3,970,000.00 USD | 193.50 USD | 677.82 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.78` | 3,970,000.00 USD | 3,970,000.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.78` | 14,380,000.00 USD | 14,380,000.00 USD | 65,390.00 USD | 10,300.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.79` | 470.66 USD | 416,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.79` | 3,980,000.00 USD | 3,980,000.00 USD | 5,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.80` | 3,990,000.00 USD | 3,990,000.00 USD | 6,870.00 USD | 770.83 USD | 9.39 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.80` | 14,440,000.00 USD | 14,440,000.00 USD | 18,630.00 USD | 28,440.00 USD | 10,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.81` | 4,000,000.00 USD | 4,000,000.00 USD | 9,140.00 USD | 1,540.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.82` | 4,020,000.00 USD | 4,020,000.00 USD | 7,220.00 USD | 0.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.82` | 14,670,000.00 USD | 14,670,000.00 USD | 121,860.00 USD | 27,860.00 USD | 86,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.83` | 4,040,000.00 USD | 4,040,000.00 USD | 16,240.00 USD | 4,800.00 USD | 1,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.84` | 14,710,000.00 USD | 14,710,000.00 USD | 9,730.00 USD | 7,850.00 USD | 14,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.85` | 1,410.00 USD | 417,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.85` | 4,060,000.00 USD | 4,060,000.00 USD | 11,610.00 USD | 1,700.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.86` | 4,070,000.00 USD | 4,070,000.00 USD | 4,390.00 USD | 0.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.86` | 14,840,000.00 USD | 14,840,000.00 USD | 59,550.00 USD | 2,210.00 USD | 72,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.87` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 2,400.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.88` | 4,080,000.00 USD | 4,080,000.00 USD | 3,930.00 USD | 1,410.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.88` | 14,880,000.00 USD | 14,880,000.00 USD | 7,900.00 USD | 8,710.00 USD | 20,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.90` | 14,970,000.00 USD | 14,970,000.00 USD | 55,970.00 USD | 19,700.00 USD | 14,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.92` | 15,010,000.00 USD | 15,010,000.00 USD | 27,710.00 USD | 10,810.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.94` | 15,130,000.00 USD | 15,130,000.00 USD | 69,320.00 USD | 11,150.00 USD | 39,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.96` | 15,180,000.00 USD | 15,180,000.00 USD | 29,800.00 USD | 1,360.00 USD | 11,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.98` | 15,200,000.00 USD | 15,200,000.00 USD | 840.10 USD | 4,150.00 USD | 18,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.00` | 15,210,000.00 USD | 15,210,000.00 USD | 0.00 USD | 6,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.02` | 15,230,000.00 USD | 15,230,000.00 USD | 15,960.00 USD | 0.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.21` | 7,330.00 USD | 424,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.23` | 114.12 USD | 425,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 3,380.00 USD | 428,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.46` | 36,200.00 USD | 464,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 465,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.71` | 218.91 USD | 465,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.96` | 1,920.00 USD | 467,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 474,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,810.00 USD | 486,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.51` | 7,460.00 USD | 493,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 505,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.66` | 776.89 USD | 506,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.69` | 733.47 USD | 507,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.86` | 59,270.00 USD | 566,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.98` | 1,360.00 USD | 567,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 569,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 569,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.43` | 35,780.00 USD | 605,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.60` | 14,110.00 USD | 619,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.64` | 431.19 USD | 620,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.79` | 953.38 USD | 621,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.96` | 102.68 USD | 621,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 709,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 234,840.00 USD | 944,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 947,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.43` | 156.40 USD | 948,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 948,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 948,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.18` | 3,930.00 USD | 952,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 953,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.80` | 2,460.00 USD | 955,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.87` | 243.93 USD | 956,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.88` | 293.48 USD | 956,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.93` | 321.63 USD | 956,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 956,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.34` | 153,350.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.64` | 111.24 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.27` | 263,790.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.41` | 22,540.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 83,400.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 162.26 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.02` | 191.87 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.14` | 1,710.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.46` | 101.47 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.62` | 4,120.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.64` | 4,930.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.66` | 2,660.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.70` | 108.89 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.86` | 2,340,000.00 USD | 0.00 USD | 205.15 USD | `-78.98%` | `110.00` |
| `Live` | `Long` | `1.89` | 2,340,000.00 USD | 0.00 USD | 229.50 USD | `-78.76%` | `121.75` |
| `Live` | `Long` | `2.00` | 2,340,000.00 USD | 0.00 USD | 159.60 USD | `-77.52%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,340,000.00 USD | 0.00 USD | 110.52 USD | `-77.07%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,340,000.00 USD | 0.00 USD | 4,920.00 USD | `-76.73%` | `2,382.76` |
| `Live` | `Long` | `2.25` | 2,330,000.00 USD | 0.00 USD | 111.40 USD | `-74.70%` | `49.62` |
| `Live` | `Long` | `2.29` | 2,330,000.00 USD | 0.00 USD | 372.09 USD | `-74.25%` | `162.84` |
| `Live` | `Long` | `2.40` | 2,330,000.00 USD | 0.00 USD | 263.45 USD | `-73.01%` | `110.00` |
| `Live` | `Long` | `2.42` | 2,330,000.00 USD | 0.00 USD | 814.80 USD | `-72.67%` | `336.00` |
| `Live` | `Long` | `2.50` | 2,330,000.00 USD | 0.00 USD | 17,510.00 USD | `-71.77%` | `6,990.57` |
| `Live` | `Long` | `2.52` | 2,310,000.00 USD | 0.00 USD | 1,680.00 USD | `-71.54%` | `666.20` |
| `Live` | `Long` | `2.58` | 2,310,000.00 USD | 0.00 USD | 268.14 USD | `-70.87%` | `103.73` |
| `Live` | `Long` | `2.69` | 2,310,000.00 USD | 0.00 USD | 600.69 USD | `-69.63%` | `222.89` |
| `Live` | `Long` | `2.87` | 2,310,000.00 USD | 0.00 USD | 232.67 USD | `-67.71%` | `81.21` |
| `Live` | `Long` | `2.90` | 2,310,000.00 USD | 0.00 USD | 1,090.00 USD | `-67.37%` | `377.71` |
| `Live` | `Long` | `2.94` | 2,310,000.00 USD | 0.00 USD | 44,510.00 USD | `-66.92%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,260,000.00 USD | 0.00 USD | 111.12 USD | `-66.47%` | `37.35` |
| `Live` | `Long` | `3.13` | 2,260,000.00 USD | 0.00 USD | 674.12 USD | `-64.67%` | `215.03` |
| `Live` | `Long` | `3.19` | 2,260,000.00 USD | 0.00 USD | 1,500.00 USD | `-64.10%` | `470.82` |
| `Live` | `Long` | `3.23` | 2,260,000.00 USD | 0.00 USD | 404.38 USD | `-63.54%` | `125.00` |
| `Live` | `Long` | `3.31` | 2,260,000.00 USD | 0.00 USD | 293.24 USD | `-62.64%` | `88.46` |
| `Live` | `Long` | `3.37` | 2,260,000.00 USD | 0.00 USD | 389.53 USD | `-62.08%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,260,000.00 USD | 0.00 USD | 297.24 USD | `-61.96%` | `88.07` |
| `Live` | `Long` | `3.67` | 2,260,000.00 USD | 0.00 USD | 109.95 USD | `-58.69%` | `30.00` |
| `Live` | `Long` | `3.71` | 2,260,000.00 USD | 0.00 USD | 2,110.00 USD | `-58.24%` | `568.43` |
| `Live` | `Long` | `3.75` | 2,260,000.00 USD | 0.00 USD | 1,500.00 USD | `-57.68%` | `400.00` |
| `Live` | `Long` | `3.81` | 2,260,000.00 USD | 0.00 USD | 2,130.00 USD | `-57.00%` | `558.69` |
| `Live` | `Long` | `3.83` | 2,250,000.00 USD | 0.00 USD | 8,720.00 USD | `-56.78%` | `2,273.34` |
| `Live` | `Long` | `3.90` | 2,250,000.00 USD | 0.00 USD | 131.73 USD | `-56.10%` | `33.82` |
| `Live` | `Long` | `3.94` | 2,250,000.00 USD | 0.00 USD | 1,290.00 USD | `-55.54%` | `326.92` |
| `Live` | `Long` | `4.03` | 2,240,000.00 USD | 0.00 USD | 402.70 USD | `-54.64%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,240,000.00 USD | 0.00 USD | 152.29 USD | `-54.41%` | `37.65` |
| `Live` | `Long` | `4.12` | 2,240,000.00 USD | 0.00 USD | 412.50 USD | `-53.51%` | `100.00` |
| `Live` | `Long` | `4.14` | 2,240,000.00 USD | 0.00 USD | 159.29 USD | `-53.29%` | `38.43` |
| `Live` | `Long` | `4.18` | 2,240,000.00 USD | 0.00 USD | 174.89 USD | `-52.83%` | `41.79` |
| `Live` | `Long` | `4.21` | 2,240,000.00 USD | 0.00 USD | 113.53 USD | `-52.61%` | `27.00` |
| `Live` | `Long` | `4.21` | 2,240,000.00 USD | 0.00 USD | 171.17 USD | `-52.50%` | `40.61` |
| `Live` | `Long` | `4.24` | 2,240,000.00 USD | 0.00 USD | 169.40 USD | `-52.27%` | `40.00` |
| `Live` | `Long` | `4.32` | 2,240,000.00 USD | 0.00 USD | 852.47 USD | `-51.37%` | `197.56` |
| `Live` | `Long` | `4.38` | 2,240,000.00 USD | 0.00 USD | 210.96 USD | `-50.69%` | `48.22` |
| `Live` | `Long` | `4.42` | 2,240,000.00 USD | 0.00 USD | 2,230.00 USD | `-50.13%` | `504.56` |
| `Live` | `Long` | `4.59` | 2,240,000.00 USD | 0.00 USD | 30,970.00 USD | `-48.21%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,210,000.00 USD | 0.00 USD | 1,160.00 USD | `-47.99%` | `251.49` |
| `Live` | `Long` | `4.62` | 2,210,000.00 USD | 0.00 USD | 2,680.00 USD | `-47.88%` | `579.06` |
| `Live` | `Long` | `4.67` | 2,200,000.00 USD | 0.00 USD | 3,280.00 USD | `-47.42%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,200,000.00 USD | 0.00 USD | 1,490.00 USD | `-47.31%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,200,000.00 USD | 0.00 USD | 15,400.00 USD | `-47.20%` | `3,287.97` |
| `Live` | `Long` | `4.71` | 2,180,000.00 USD | 0.00 USD | 1,270.00 USD | `-46.86%` | `270.00` |
| `Live` | `Long` | `4.74` | 2,180,000.00 USD | 0.00 USD | 4,990.00 USD | `-46.64%` | `1,053.00` |
| `Live` | `Long` | `4.75` | 2,180,000.00 USD | 0.00 USD | 240.48 USD | `-46.52%` | `50.68` |
| `Live` | `Long` | `4.76` | 2,180,000.00 USD | 0.00 USD | 105.64 USD | `-46.30%` | `22.17` |
| `Live` | `Long` | `4.79` | 2,180,000.00 USD | 0.00 USD | 15,760.00 USD | `-45.96%` | `3,286.00` |
| `Live` | `Long` | `4.83` | 2,160,000.00 USD | 0.00 USD | 467.01 USD | `-45.51%` | `96.59` |
| `Live` | `Long` | `4.86` | 2,160,000.00 USD | 0.00 USD | 112.64 USD | `-45.28%` | `23.20` |
| `Live` | `Long` | `4.89` | 2,160,000.00 USD | 0.00 USD | 146.85 USD | `-44.83%` | `30.00` |
| `Live` | `Long` | `4.91` | 2,160,000.00 USD | 0.00 USD | 527.19 USD | `-44.72%` | `107.48` |
| `Live` | `Long` | `4.92` | 2,160,000.00 USD | 0.00 USD | 1,230.00 USD | `-44.61%` | `251.00` |
| `Live` | `Long` | `4.95` | 2,160,000.00 USD | 0.00 USD | 4,080.00 USD | `-44.27%` | `824.62` |
| `Live` | `Long` | `4.96` | 2,160,000.00 USD | 0.00 USD | 945.36 USD | `-44.16%` | `190.79` |
| `Live` | `Long` | `4.97` | 2,150,000.00 USD | 0.00 USD | 282.23 USD | `-43.93%` | `56.73` |
| `Live` | `Long` | `4.99` | 2,150,000.00 USD | 0.00 USD | 329.11 USD | `-43.82%` | `66.02` |
| `Live` | `Long` | `5.01` | 2,150,000.00 USD | 0.00 USD | 56,390.00 USD | `-43.48%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,100,000.00 USD | 0.00 USD | 167.78 USD | `-43.37%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,100,000.00 USD | 0.00 USD | 314.59 USD | `-43.25%` | `62.48` |
| `Live` | `Long` | `5.04` | 2,100,000.00 USD | 0.00 USD | 484.57 USD | `-43.14%` | `96.05` |
| `Live` | `Long` | `5.05` | 2,100,000.00 USD | 0.00 USD | 504.74 USD | `-43.03%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,100,000.00 USD | 0.00 USD | 318.46 USD | `-42.80%` | `62.75` |
| `Live` | `Long` | `5.12` | 2,100,000.00 USD | 0.00 USD | 250.20 USD | `-42.24%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,100,000.00 USD | 0.00 USD | 156,680.00 USD | `-42.13%` | `30,512.33` |
| `Live` | `Long` | `5.17` | 1,940,000.00 USD | 0.00 USD | 2,300.00 USD | `-41.79%` | `445.16` |
| `Live` | `Long` | `5.17` | 1,940,000.00 USD | 0.00 USD | 1,620.00 USD | `-41.68%` | `312.94` |
| `Live` | `Long` | `5.18` | 1,930,000.00 USD | 0.00 USD | 150.57 USD | `-41.56%` | `29.04` |
| `Live` | `Long` | `5.21` | 1,930,000.00 USD | 0.00 USD | 300.91 USD | `-41.23%` | `57.70` |
| `Live` | `Long` | `5.29` | 1,930,000.00 USD | 0.00 USD | 640.70 USD | `-40.44%` | `121.23` |
| `Live` | `Long` | `5.30` | 1,930,000.00 USD | 0.00 USD | 2,880.00 USD | `-40.21%` | `543.81` |
| `Live` | `Long` | `5.33` | 1,930,000.00 USD | 0.00 USD | 716.11 USD | `-39.99%` | `134.48` |
| `Live` | `Long` | `5.36` | 1,930,000.00 USD | 0.00 USD | 589.05 USD | `-39.65%` | `110.00` |
| `Live` | `Long` | `5.39` | 1,930,000.00 USD | 0.00 USD | 660.46 USD | `-39.20%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,930,000.00 USD | 0.00 USD | 21,080.00 USD | `-38.97%` | `3,892.05` |
| `Live` | `Long` | `5.42` | 1,910,000.00 USD | 0.00 USD | 160,400.00 USD | `-38.86%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,750,000.00 USD | 0.00 USD | 1,360.00 USD | `-38.75%` | `250.00` |
| `Live` | `Long` | `5.46` | 1,750,000.00 USD | 0.00 USD | 264.72 USD | `-38.41%` | `48.44` |
| `Live` | `Long` | `5.49` | 1,750,000.00 USD | 0.00 USD | 354.06 USD | `-38.18%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,750,000.00 USD | 0.00 USD | 19,290.00 USD | `-38.07%` | `3,510.41` |
| `Live` | `Long` | `5.51` | 1,730,000.00 USD | 0.00 USD | 367.41 USD | `-37.85%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,730,000.00 USD | 0.00 USD | 121.38 USD | `-37.62%` | `21.93` |
| `Live` | `Long` | `5.57` | 1,730,000.00 USD | 0.00 USD | 967.98 USD | `-37.28%` | `173.94` |
| `Live` | `Long` | `5.58` | 1,720,000.00 USD | 0.00 USD | 63,260.00 USD | `-37.17%` | `11,347.58` |
| `Live` | `Long` | `5.59` | 1,660,000.00 USD | 0.00 USD | 34,430.00 USD | `-36.94%` | `6,153.60` |
| `Live` | `Long` | `5.63` | 1,630,000.00 USD | 0.00 USD | 22,590.00 USD | `-36.49%` | `4,009.72` |
| `Live` | `Long` | `5.64` | 1,600,000.00 USD | 0.00 USD | 4,120.00 USD | `-36.38%` | `730.59` |
| `Live` | `Long` | `5.68` | 1,600,000.00 USD | 0.00 USD | 404.32 USD | `-35.93%` | `71.12` |
| `Live` | `Long` | `5.71` | 1,600,000.00 USD | 0.00 USD | 2,340.00 USD | `-35.70%` | `409.39` |
| `Live` | `Long` | `5.74` | 1,600,000.00 USD | 0.00 USD | 238.86 USD | `-35.37%` | `41.65` |
| `Live` | `Long` | `5.75` | 1,600,000.00 USD | 0.00 USD | 125.70 USD | `-35.25%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,600,000.00 USD | 0.00 USD | 3,190.00 USD | `-35.14%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,590,000.00 USD | 0.00 USD | 10,850.00 USD | `-35.03%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,580,000.00 USD | 0.00 USD | 801.40 USD | `-34.91%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,580,000.00 USD | 0.00 USD | 2,890.00 USD | `-34.80%` | `500.00` |
| `Live` | `Long` | `5.79` | 1,580,000.00 USD | 0.00 USD | 736.72 USD | `-34.69%` | `127.13` |
| `Live` | `Long` | `5.80` | 1,580,000.00 USD | 0.00 USD | 326,400.00 USD | `-34.58%` | `56,226.53` |
| `Live` | `Long` | `5.82` | 1,250,000.00 USD | 0.00 USD | 106.65 USD | `-34.46%` | `18.34` |
| `Live` | `Long` | `5.89` | 1,250,000.00 USD | 0.00 USD | 22,060.00 USD | `-33.56%` | `3,742.70` |
| `Live` | `Long` | `5.91` | 1,230,000.00 USD | 0.00 USD | 399.18 USD | `-33.45%` | `67.60` |
| `Live` | `Long` | `5.96` | 1,230,000.00 USD | 0.00 USD | 11,720.00 USD | `-32.89%` | `1,968.19` |
| `Live` | `Long` | `5.97` | 1,220,000.00 USD | 0.00 USD | 2,120.00 USD | `-32.66%` | `354.27` |
| `Live` | `Long` | `5.99` | 1,220,000.00 USD | 0.00 USD | 447.98 USD | `-32.55%` | `74.85` |
| `Live` | `Long` | `6.00` | 1,220,000.00 USD | 0.00 USD | 341.56 USD | `-32.32%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,220,000.00 USD | 0.00 USD | 446.85 USD | `-32.21%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,210,000.00 USD | 0.00 USD | 1,690.00 USD | `-31.98%` | `280.10` |
| `Live` | `Long` | `6.04` | 1,210,000.00 USD | 0.00 USD | 105.61 USD | `-31.87%` | `17.47` |
| `Live` | `Long` | `6.05` | 1,210,000.00 USD | 0.00 USD | 1,310.00 USD | `-31.76%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,210,000.00 USD | 0.00 USD | 265.10 USD | `-31.65%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,210,000.00 USD | 0.00 USD | 1,690.00 USD | `-31.53%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,210,000.00 USD | 0.00 USD | 405.14 USD | `-31.42%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,210,000.00 USD | 0.00 USD | 3,550.00 USD | `-31.31%` | `582.81` |
| `Live` | `Long` | `6.11` | 1,210,000.00 USD | 0.00 USD | 5,560.00 USD | `-31.20%` | `911.19` |
| `Live` | `Long` | `6.12` | 1,200,000.00 USD | 0.00 USD | 137.02 USD | `-30.97%` | `22.37` |
| `Live` | `Long` | `6.14` | 1,200,000.00 USD | 0.00 USD | 238.61 USD | `-30.74%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,200,000.00 USD | 0.00 USD | 4,390.00 USD | `-30.63%` | `713.75` |
| `Live` | `Long` | `6.17` | 1,200,000.00 USD | 0.00 USD | 187.29 USD | `-30.52%` | `30.38` |
| `Live` | `Long` | `6.17` | 1,200,000.00 USD | 0.00 USD | 104.36 USD | `-30.41%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,200,000.00 USD | 0.00 USD | 310.25 USD | `-30.07%` | `50.00` |
| `Live` | `Long` | `6.21` | 1,190,000.00 USD | 0.00 USD | 2,560.00 USD | `-29.96%` | `411.30` |
| `Live` | `Long` | `6.22` | 1,190,000.00 USD | 0.00 USD | 715.31 USD | `-29.84%` | `114.91` |
| `Live` | `Long` | `6.25` | 1,190,000.00 USD | 0.00 USD | 971.10 USD | `-29.62%` | `155.50` |
| `Live` | `Long` | `6.25` | 1,190,000.00 USD | 0.00 USD | 2,060.00 USD | `-29.51%` | `330.00` |
| `Live` | `Long` | `6.26` | 1,190,000.00 USD | 0.00 USD | 1,450.00 USD | `-29.39%` | `232.17` |
| `Live` | `Long` | `6.28` | 1,190,000.00 USD | 0.00 USD | 2,510.00 USD | `-29.28%` | `400.00` |
| `Live` | `Long` | `6.29` | 1,180,000.00 USD | 0.00 USD | 147.51 USD | `-29.17%` | `23.47` |
| `Live` | `Long` | `6.32` | 1,180,000.00 USD | 0.00 USD | 277.04 USD | `-28.83%` | `43.87` |
| `Live` | `Long` | `6.33` | 1,180,000.00 USD | 0.00 USD | 105.25 USD | `-28.72%` | `16.64` |
| `Live` | `Long` | `6.36` | 1,180,000.00 USD | 0.00 USD | 4,470.00 USD | `-28.38%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,180,000.00 USD | 0.00 USD | 284,770.00 USD | `-28.27%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 894,820.00 USD | 0.00 USD | 5,110.00 USD | `-28.15%` | `801.31` |
| `Live` | `Long` | `6.38` | 889,710.00 USD | 0.00 USD | 1,690.00 USD | `-28.04%` | `265.15` |
| `Live` | `Long` | `6.42` | 888,020.00 USD | 0.00 USD | 306.32 USD | `-27.70%` | `47.75` |
| `Live` | `Long` | `6.43` | 887,710.00 USD | 0.00 USD | 6,780.00 USD | `-27.48%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 880,940.00 USD | 0.00 USD | 1,050.00 USD | `-27.14%` | `162.75` |
| `Live` | `Long` | `6.54` | 879,880.00 USD | 0.00 USD | 3,620.00 USD | `-26.35%` | `554.55` |
| `Live` | `Long` | `6.54` | 876,260.00 USD | 0.00 USD | 8,970.00 USD | `-26.24%` | `1,370.89` |
| `Live` | `Long` | `6.58` | 867,290.00 USD | 0.00 USD | 1,100.00 USD | `-25.79%` | `166.55` |
| `Live` | `Long` | `6.59` | 866,190.00 USD | 0.00 USD | 408.89 USD | `-25.67%` | `62.00` |
| `Live` | `Long` | `6.62` | 865,780.00 USD | 0.00 USD | 2,110.00 USD | `-25.45%` | `318.57` |
| `Live` | `Long` | `6.70` | 863,670.00 USD | 0.00 USD | 506.54 USD | `-24.55%` | `75.66` |
| `Live` | `Long` | `6.71` | 863,170.00 USD | 0.00 USD | 19,850.00 USD | `-24.43%` | `2,960.22` |
| `Live` | `Long` | `6.75` | 843,320.00 USD | 0.00 USD | 1,330.00 USD | `-23.98%` | `196.95` |
| `Live` | `Long` | `6.78` | 841,990.00 USD | 0.00 USD | 6,780.00 USD | `-23.64%` | `1,000.00` |
| `Live` | `Long` | `6.79` | 835,220.00 USD | 0.00 USD | 16,960.00 USD | `-23.53%` | `2,500.00` |
| `Live` | `Long` | `6.79` | 818,250.00 USD | 0.00 USD | 4,260.00 USD | `-23.42%` | `626.24` |
| `Live` | `Long` | `6.80` | 814,000.00 USD | 0.00 USD | 1,500.00 USD | `-23.31%` | `220.95` |
| `Live` | `Long` | `6.82` | 812,490.00 USD | 0.00 USD | 2,670.00 USD | `-23.19%` | `391.11` |
| `Live` | `Long` | `6.83` | 809,830.00 USD | 0.00 USD | 158.14 USD | `-23.08%` | `23.17` |
| `Live` | `Long` | `6.83` | 809,670.00 USD | 0.00 USD | 4,410.00 USD | `-22.97%` | `644.73` |
| `Live` | `Long` | `6.86` | 805,260.00 USD | 0.00 USD | 18,930.00 USD | `-22.74%` | `2,761.63` |
| `Live` | `Long` | `6.87` | 786,330.00 USD | 0.00 USD | 3,340.00 USD | `-22.63%` | `486.46` |
| `Live` | `Long` | `6.88` | 782,990.00 USD | 0.00 USD | 1,380.00 USD | `-22.52%` | `200.00` |
| `Live` | `Long` | `6.89` | 781,620.00 USD | 0.00 USD | 32,830.00 USD | `-22.29%` | `4,761.63` |
| `Live` | `Long` | `6.91` | 748,790.00 USD | 0.00 USD | 269.30 USD | `-22.18%` | `39.00` |
| `Live` | `Long` | `6.95` | 748,520.00 USD | 0.00 USD | 3,760.00 USD | `-21.73%` | `541.68` |
| `Live` | `Long` | `6.96` | 744,760.00 USD | 0.00 USD | 3,480.00 USD | `-21.62%` | `500.00` |
| `Live` | `Long` | `6.96` | 741,280.00 USD | 0.00 USD | 636.74 USD | `-21.50%` | `91.42` |
| `Live` | `Long` | `7.00` | 740,640.00 USD | 0.00 USD | 746.58 USD | `-21.17%` | `106.73` |
| `Live` | `Long` | `7.00` | 739,890.00 USD | 0.00 USD | 22,390.00 USD | `-21.05%` | `3,195.81` |
| `Live` | `Long` | `7.04` | 717,510.00 USD | 0.00 USD | 811.35 USD | `-20.71%` | `115.33` |
| `Live` | `Long` | `7.04` | 716,700.00 USD | 0.00 USD | 4,100.00 USD | `-20.60%` | `581.44` |
| `Live` | `Long` | `7.08` | 712,600.00 USD | 0.00 USD | 6,700.00 USD | `-20.26%` | `947.44` |
| `Live` | `Long` | `7.08` | 705,900.00 USD | 0.00 USD | 1,670.00 USD | `-20.15%` | `236.20` |
| `Live` | `Long` | `7.09` | 704,220.00 USD | 0.00 USD | 1,620.00 USD | `-20.04%` | `228.41` |
| `Live` | `Long` | `7.11` | 702,600.00 USD | 0.00 USD | 28,230.00 USD | `-19.93%` | `3,972.61` |
| `Live` | `Long` | `7.12` | 674,380.00 USD | 0.00 USD | 379.66 USD | `-19.81%` | `53.36` |
| `Live` | `Long` | `7.13` | 674,000.00 USD | 0.00 USD | 2,300.00 USD | `-19.59%` | `322.72` |
| `Live` | `Long` | `7.14` | 671,700.00 USD | 0.00 USD | 20,950.00 USD | `-19.47%` | `2,931.56` |
| `Live` | `Long` | `7.18` | 650,750.00 USD | 0.00 USD | 1,440.00 USD | `-19.02%` | `200.00` |
| `Live` | `Long` | `7.21` | 649,310.00 USD | 0.00 USD | 581.02 USD | `-18.69%` | `80.53` |
| `Live` | `Long` | `7.24` | 648,730.00 USD | 0.00 USD | 179.65 USD | `-18.46%` | `24.83` |
| `Live` | `Long` | `7.25` | 648,550.00 USD | 0.00 USD | 185.83 USD | `-18.35%` | `25.65` |
| `Live` | `Long` | `7.29` | 648,370.00 USD | 0.00 USD | 36,560.00 USD | `-17.90%` | `5,019.00` |
| `Live` | `Long` | `7.29` | 611,800.00 USD | 0.00 USD | 19,790.00 USD | `-17.78%` | `2,712.69` |
| `Live` | `Long` | `7.32` | 592,010.00 USD | 0.00 USD | 168.76 USD | `-17.56%` | `23.07` |
| `Live` | `Long` | `7.33` | 591,840.00 USD | 0.00 USD | 4,910.00 USD | `-17.45%` | `669.93` |
| `Live` | `Long` | `7.33` | 586,940.00 USD | 0.00 USD | 2,450.00 USD | `-17.33%` | `333.54` |
| `Live` | `Long` | `7.34` | 584,490.00 USD | 0.00 USD | 4,370.00 USD | `-17.22%` | `594.84` |
| `Live` | `Long` | `7.36` | 580,120.00 USD | 0.00 USD | 1,030.00 USD | `-17.11%` | `140.00` |
| `Live` | `Long` | `7.37` | 579,090.00 USD | 0.00 USD | 5,720.00 USD | `-17.00%` | `776.95` |
| `Live` | `Long` | `7.38` | 573,370.00 USD | 0.00 USD | 3,920.00 USD | `-16.88%` | `531.65` |
| `Live` | `Long` | `7.38` | 569,450.00 USD | 0.00 USD | 17,770.00 USD | `-16.77%` | `2,406.10` |
| `Live` | `Long` | `7.39` | 551,680.00 USD | 0.00 USD | 1,550.00 USD | `-16.66%` | `210.17` |
| `Live` | `Long` | `7.42` | 550,130.00 USD | 0.00 USD | 1,480.00 USD | `-16.43%` | `200.00` |
| `Live` | `Long` | `7.42` | 548,640.00 USD | 0.00 USD | 500.00 USD | `-16.32%` | `67.34` |
| `Live` | `Long` | `7.45` | 548,140.00 USD | 0.00 USD | 210.99 USD | `-16.09%` | `28.34` |
| `Live` | `Long` | `7.46` | 547,930.00 USD | 0.00 USD | 1,370.00 USD | `-15.98%` | `183.84` |
| `Live` | `Long` | `7.46` | 546,560.00 USD | 0.00 USD | 4,590.00 USD | `-15.87%` | `614.36` |
| `Live` | `Long` | `7.47` | 541,980.00 USD | 0.00 USD | 3,210.00 USD | `-15.76%` | `430.09` |
| `Live` | `Long` | `7.50` | 538,760.00 USD | 0.00 USD | 1,580.00 USD | `-15.53%` | `211.22` |
| `Live` | `Long` | `7.50` | 537,180.00 USD | 0.00 USD | 1,080.00 USD | `-15.42%` | `143.74` |
| `Live` | `Long` | `7.53` | 536,100.00 USD | 0.00 USD | 995.86 USD | `-15.19%` | `132.34` |
| `Live` | `Long` | `7.54` | 535,100.00 USD | 0.00 USD | 4,210.00 USD | `-15.08%` | `559.01` |
| `Live` | `Long` | `7.55` | 530,890.00 USD | 0.00 USD | 157.14 USD | `-14.85%` | `20.80` |
| `Live` | `Long` | `7.57` | 530,730.00 USD | 0.00 USD | 4,380.00 USD | `-14.74%` | `578.50` |
| `Live` | `Long` | `7.59` | 526,360.00 USD | 0.00 USD | 25,140.00 USD | `-14.40%` | `3,310.14` |
| `Live` | `Long` | `7.62` | 501,220.00 USD | 0.00 USD | 312.22 USD | `-14.18%` | `41.00` |
| `Live` | `Long` | `7.62` | 500,900.00 USD | 0.00 USD | 787.51 USD | `-14.07%` | `103.28` |
| `Live` | `Long` | `7.63` | 500,120.00 USD | 0.00 USD | 514.52 USD | `-13.95%` | `67.39` |
| `Live` | `Long` | `7.66` | 499,600.00 USD | 0.00 USD | 135.42 USD | `-13.73%` | `17.69` |
| `Live` | `Long` | `7.67` | 499,470.00 USD | 0.00 USD | 1,740.00 USD | `-13.61%` | `226.45` |
| `Live` | `Long` | `7.68` | 497,730.00 USD | 0.00 USD | 1,120.00 USD | `-13.39%` | `145.25` |
| `Live` | `Long` | `7.70` | 496,610.00 USD | 0.00 USD | 1,460.00 USD | `-13.28%` | `190.36` |
| `Live` | `Long` | `7.71` | 495,150.00 USD | 0.00 USD | 19,410.00 USD | `-13.16%` | `2,518.82` |
| `Live` | `Long` | `7.72` | 475,740.00 USD | 0.00 USD | 2,550.00 USD | `-12.94%` | `330.65` |
| `Live` | `Long` | `7.75` | 473,190.00 USD | 0.00 USD | 893.76 USD | `-12.60%` | `115.25` |
| `Live` | `Long` | `7.76` | 472,290.00 USD | 0.00 USD | 455.73 USD | `-12.49%` | `58.69` |
| `Live` | `Long` | `7.78` | 471,840.00 USD | 0.00 USD | 695.32 USD | `-12.37%` | `89.43` |
| `Live` | `Long` | `7.79` | 471,140.00 USD | 0.00 USD | 3,900.00 USD | `-12.26%` | `500.57` |
| `Live` | `Long` | `7.79` | 467,250.00 USD | 0.00 USD | 1,940.00 USD | `-12.15%` | `248.84` |
| `Live` | `Long` | `7.80` | 465,310.00 USD | 0.00 USD | 633.77 USD | `-12.04%` | `81.20` |
| `Live` | `Long` | `7.82` | 464,670.00 USD | 0.00 USD | 5,280.00 USD | `-11.92%` | `675.43` |
| `Live` | `Long` | `7.84` | 459,390.00 USD | 0.00 USD | 10,930.00 USD | `-11.59%` | `1,393.53` |
| `Live` | `Long` | `7.86` | 448,460.00 USD | 0.00 USD | 2,110.00 USD | `-11.47%` | `269.14` |
| `Live` | `Long` | `7.87` | 446,350.00 USD | 0.00 USD | 176.18 USD | `-11.36%` | `22.40` |
| `Live` | `Long` | `7.88` | 446,170.00 USD | 0.00 USD | 555.19 USD | `-11.25%` | `70.50` |
| `Live` | `Long` | `7.91` | 445,620.00 USD | 0.00 USD | 2,410.00 USD | `-10.91%` | `304.85` |
| `Live` | `Long` | `7.92` | 443,210.00 USD | 0.00 USD | 923.42 USD | `-10.68%` | `116.52` |
| `Live` | `Long` | `7.93` | 442,280.00 USD | 0.00 USD | 1,820.00 USD | `-10.57%` | `228.88` |
| `Live` | `Long` | `7.95` | 440,470.00 USD | 0.00 USD | 127,110.00 USD | `-10.46%` | `15,999.24` |
| `Live` | `Long` | `7.96` | 313,350.00 USD | 0.00 USD | 843.15 USD | `-10.35%` | `105.99` |
| `Live` | `Long` | `7.99` | 312,510.00 USD | 0.00 USD | 1,600.00 USD | `-10.01%` | `200.68` |
| `Live` | `Long` | `8.00` | 310,910.00 USD | 0.00 USD | 210.99 USD | `-9.90%` | `26.39` |
| `Live` | `Long` | `8.03` | 310,700.00 USD | 0.00 USD | 957.70 USD | `-9.56%` | `119.34` |
| `Live` | `Long` | `8.04` | 309,740.00 USD | 0.00 USD | 88,380.00 USD | `-9.44%` | `10,999.50` |
| `Live` | `Long` | `8.04` | 221,360.00 USD | 0.00 USD | 6,890.00 USD | `-9.33%` | `856.44` |
| `Live` | `Long` | `8.05` | 214,470.00 USD | 0.00 USD | 3,340.00 USD | `-9.22%` | `414.27` |
| `Live` | `Long` | `8.06` | 211,130.00 USD | 0.00 USD | 37,830.00 USD | `-9.11%` | `4,690.67` |
| `Live` | `Long` | `8.09` | 173,300.00 USD | 0.00 USD | 617.61 USD | `-8.88%` | `76.39` |
| `Live` | `Long` | `8.10` | 172,680.00 USD | 0.00 USD | 11,700.00 USD | `-8.77%` | `1,445.70` |
| `Live` | `Long` | `8.12` | 160,980.00 USD | 0.00 USD | 241.26 USD | `-8.54%` | `29.73` |
| `Live` | `Long` | `8.12` | 160,740.00 USD | 0.00 USD | 233.92 USD | `-8.43%` | `28.79` |
| `Live` | `Long` | `8.16` | 160,500.00 USD | 0.00 USD | 871.61 USD | `-7.98%` | `106.75` |
| `Live` | `Long` | `8.19` | 159,630.00 USD | 0.00 USD | 4,030.00 USD | `-7.75%` | `492.37` |
| `Live` | `Long` | `8.20` | 155,600.00 USD | 0.00 USD | 2,380.00 USD | `-7.64%` | `290.16` |
| `Live` | `Long` | `8.21` | 153,230.00 USD | 0.00 USD | 577.06 USD | `-7.53%` | `70.33` |
| `Live` | `Long` | `8.21` | 152,650.00 USD | 0.00 USD | 147.87 USD | `-7.42%` | `18.00` |
| `Live` | `Long` | `8.22` | 152,500.00 USD | 0.00 USD | 2,100.00 USD | `-7.30%` | `255.16` |
| `Live` | `Long` | `8.23` | 150,400.00 USD | 0.00 USD | 1,160.00 USD | `-7.19%` | `140.81` |
| `Live` | `Long` | `8.24` | 149,240.00 USD | 0.00 USD | 1,300.00 USD | `-7.08%` | `158.06` |
| `Live` | `Long` | `8.26` | 147,940.00 USD | 0.00 USD | 13,810.00 USD | `-6.96%` | `1,673.14` |
| `Live` | `Long` | `8.27` | 134,130.00 USD | 0.00 USD | 6,110.00 USD | `-6.85%` | `739.00` |
| `Live` | `Long` | `8.28` | 128,020.00 USD | 0.00 USD | 3,190.00 USD | `-6.74%` | `386.07` |
| `Live` | `Long` | `8.29` | 124,820.00 USD | 0.00 USD | 498.26 USD | `-6.63%` | `60.14` |
| `Live` | `Long` | `8.29` | 124,330.00 USD | 0.00 USD | 18,970.00 USD | `-6.51%` | `2,286.62` |
| `Live` | `Long` | `8.30` | 105,360.00 USD | 0.00 USD | 33,500.00 USD | `-6.40%` | `4,033.57` |
| `Live` | `Long` | `8.31` | 71,860.00 USD | 0.00 USD | 4,550.00 USD | `-6.29%` | `547.70` |
| `Live` | `Long` | `8.34` | 67,310.00 USD | 0.00 USD | 4,630.00 USD | `-6.06%` | `555.62` |
| `Live` | `Long` | `8.36` | 62,670.00 USD | 0.00 USD | 3,180.00 USD | `-5.84%` | `380.92` |
| `Live` | `Long` | `8.37` | 59,490.00 USD | 0.00 USD | 7,160.00 USD | `-5.73%` | `856.48` |
| `Live` | `Long` | `8.38` | 52,330.00 USD | 0.00 USD | 223.70 USD | `-5.61%` | `26.71` |
| `Live` | `Long` | `8.39` | 52,100.00 USD | 0.00 USD | 1,680.00 USD | `-5.39%` | `200.00` |
| `Live` | `Long` | `8.40` | 50,430.00 USD | 0.00 USD | 1,280.00 USD | `-5.27%` | `152.34` |
| `Live` | `Long` | `8.44` | 49,140.00 USD | 0.00 USD | 188.61 USD | `-4.94%` | `22.36` |
| `Live` | `Long` | `8.45` | 48,960.00 USD | 0.00 USD | 588.70 USD | `-4.82%` | `69.71` |
| `Live` | `Long` | `8.46` | 48,370.00 USD | 0.00 USD | 4,100.00 USD | `-4.71%` | `485.34` |
| `Live` | `Long` | `8.46` | 44,260.00 USD | 0.00 USD | 2,840.00 USD | `-4.60%` | `335.62` |
| `Live` | `Long` | `8.47` | 41,420.00 USD | 0.00 USD | 12,890.00 USD | `-4.49%` | `1,520.51` |
| `Live` | `Long` | `8.48` | 28,540.00 USD | 0.00 USD | 1,160.00 USD | `-4.37%` | `136.39` |
| `Live` | `Long` | `8.49` | 27,380.00 USD | 0.00 USD | 403.51 USD | `-4.26%` | `47.50` |
| `Live` | `Long` | `8.51` | 26,980.00 USD | 0.00 USD | 6,380.00 USD | `-4.15%` | `750.34` |
| `Live` | `Long` | `8.52` | 20,590.00 USD | 0.00 USD | 8,060.00 USD | `-4.03%` | `947.05` |
| `Live` | `Long` | `8.54` | 12,530.00 USD | 0.00 USD | 6,350.00 USD | `-3.81%` | `743.78` |
| `Live` | `Long` | `8.54` | 6,180.00 USD | 0.00 USD | 1,550.00 USD | `-3.70%` | `180.95` |
| `Live` | `Long` | `8.55` | 4,640.00 USD | 0.00 USD | 1,660.00 USD | `-3.58%` | `193.54` |
| `Live` | `Long` | `8.61` | 2,980.00 USD | 0.00 USD | 2,980.00 USD | `-3.02%` | `346.30` |
| `Live` | `Short` | `9.13` | 314.34 USD | 314.34 USD | 0.00 USD | `+2.95%` | `34.41` |
| `Live` | `Short` | `9.29` | 415.26 USD | 100.93 USD | 0.00 USD | `+4.64%` | `10.87` |
| `Live` | `Short` | `9.34` | 1,470.00 USD | 1,060.00 USD | 0.00 USD | `+5.21%` | `113.04` |
| `Live` | `Short` | `9.35` | 5,400.00 USD | 3,930.00 USD | 0.00 USD | `+5.32%` | `420.07` |
| `Live` | `Short` | `9.38` | 409,510.00 USD | 404,120.00 USD | 0.00 USD | `+5.77%` | `43,059.94` |
| `Live` | `Short` | `9.41` | 411,990.00 USD | 2,470.00 USD | 0.00 USD | `+6.11%` | `262.71` |
| `Live` | `Short` | `9.46` | 414,990.00 USD | 3,010.00 USD | 0.00 USD | `+6.56%` | `318.12` |
| `Live` | `Short` | `9.73` | 415,190.00 USD | 192.95 USD | 0.00 USD | `+9.71%` | `19.82` |
| `Live` | `Short` | `9.77` | 415,740.00 USD | 549.67 USD | 0.00 USD | `+10.05%` | `56.29` |
| `Live` | `Short` | `9.79` | 416,210.00 USD | 470.66 USD | 0.00 USD | `+10.28%` | `48.10` |
| `Live` | `Short` | `9.85` | 417,620.00 USD | 1,410.00 USD | 0.00 USD | `+10.95%` | `143.31` |
| `Live` | `Short` | `10.21` | 424,950.00 USD | 7,330.00 USD | 0.00 USD | `+15.12%` | `717.30` |
| `Live` | `Short` | `10.23` | 425,060.00 USD | 114.12 USD | 0.00 USD | `+15.35%` | `11.15` |
| `Live` | `Short` | `10.35` | 428,440.00 USD | 3,380.00 USD | 0.00 USD | `+16.59%` | `326.92` |
| `Live` | `Short` | `10.46` | 464,650.00 USD | 36,200.00 USD | 0.00 USD | `+17.83%` | `3,462.73` |
| `Live` | `Short` | `10.56` | 465,170.00 USD | 523.81 USD | 0.00 USD | `+19.07%` | `49.58` |
| `Live` | `Short` | `10.71` | 465,390.00 USD | 218.91 USD | 0.00 USD | `+20.76%` | `20.43` |
| `Live` | `Short` | `10.96` | 467,300.00 USD | 1,920.00 USD | 0.00 USD | `+23.58%` | `174.67` |
| `Live` | `Short` | `11.01` | 474,270.00 USD | 6,970.00 USD | 0.00 USD | `+24.03%` | `633.00` |
| `Live` | `Short` | `11.27` | 486,080.00 USD | 11,810.00 USD | 0.00 USD | `+26.96%` | `1,048.25` |
| `Live` | `Short` | `11.51` | 493,530.00 USD | 7,460.00 USD | 0.00 USD | `+29.66%` | `648.15` |
| `Live` | `Short` | `11.62` | 505,670.00 USD | 12,140.00 USD | 0.00 USD | `+31.02%` | `1,043.90` |
| `Live` | `Short` | `11.66` | 506,450.00 USD | 776.89 USD | 0.00 USD | `+31.47%` | `66.60` |
| `Live` | `Short` | `11.69` | 507,180.00 USD | 733.47 USD | 0.00 USD | `+31.69%` | `62.77` |
| `Live` | `Short` | `11.86` | 566,460.00 USD | 59,270.00 USD | 0.00 USD | `+33.61%` | `5,000.00` |
| `Live` | `Short` | `11.98` | 567,820.00 USD | 1,360.00 USD | 0.00 USD | `+35.07%` | `113.77` |
| `Live` | `Short` | `12.30` | 569,550.00 USD | 1,730.00 USD | 0.00 USD | `+38.68%` | `140.71` |
| `Live` | `Short` | `12.40` | 569,890.00 USD | 343.62 USD | 0.00 USD | `+39.81%` | `27.70` |
| `Live` | `Short` | `12.43` | 605,670.00 USD | 35,780.00 USD | 0.00 USD | `+40.03%` | `2,879.71` |
| `Live` | `Short` | `12.60` | 619,780.00 USD | 14,110.00 USD | 0.00 USD | `+41.95%` | `1,120.14` |
| `Live` | `Short` | `12.64` | 620,210.00 USD | 431.19 USD | 0.00 USD | `+42.51%` | `34.10` |
| `Live` | `Short` | `12.79` | 621,170.00 USD | 953.38 USD | 0.00 USD | `+44.09%` | `74.57` |
| `Live` | `Short` | `12.96` | 621,270.00 USD | 102.68 USD | 0.00 USD | `+46.12%` | `7.92` |
| `Live` | `Short` | `13.20` | 709,210.00 USD | 87,940.00 USD | 0.00 USD | `+48.71%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 944,050.00 USD | 234,840.00 USD | 0.00 USD | `+49.72%` | `17,677.02` |
| `Live` | `Short` | `13.29` | 947,860.00 USD | 3,810.00 USD | 0.00 USD | `+49.84%` | `286.56` |
| `Live` | `Short` | `13.43` | 948,020.00 USD | 156.40 USD | 0.00 USD | `+51.30%` | `11.65` |
| `Live` | `Short` | `13.46` | 948,450.00 USD | 430.34 USD | 0.00 USD | `+51.75%` | `31.96` |
| `Live` | `Short` | `13.69` | 948,620.00 USD | 172.29 USD | 0.00 USD | `+54.23%` | `12.59` |
| `Live` | `Short` | `14.18` | 952,560.00 USD | 3,930.00 USD | 0.00 USD | `+59.75%` | `277.54` |
| `Live` | `Short` | `14.66` | 953,380.00 USD | 823.29 USD | 0.00 USD | `+65.28%` | `56.14` |
| `Live` | `Short` | `14.80` | 955,840.00 USD | 2,460.00 USD | 0.00 USD | `+66.85%` | `166.16` |
| `Live` | `Short` | `14.87` | 956,080.00 USD | 243.93 USD | 0.00 USD | `+67.53%` | `16.41` |
| `Live` | `Short` | `14.88` | 956,380.00 USD | 293.48 USD | 0.00 USD | `+67.64%` | `19.73` |
| `Live` | `Short` | `14.93` | 956,700.00 USD | 321.63 USD | 0.00 USD | `+68.21%` | `21.55` |
| `Live` | `Short` | `15.29` | 956,930.00 USD | 229.43 USD | 0.00 USD | `+72.38%` | `15.00` |
| `Live` | `Short` | `15.34` | 1,110,000.00 USD | 153,350.00 USD | 0.00 USD | `+72.83%` | `10,000.00` |
| `Live` | `Short` | `15.35` | 1,110,000.00 USD | 230.17 USD | 0.00 USD | `+72.94%` | `15.00` |
| `Live` | `Short` | `15.38` | 1,130,000.00 USD | 20,000.00 USD | 0.00 USD | `+73.39%` | `1,300.00` |
| `Live` | `Short` | `15.64` | 1,130,000.00 USD | 111.24 USD | 0.00 USD | `+76.32%` | `7.11` |
| `Live` | `Short` | `16.27` | 1,390,000.00 USD | 263,790.00 USD | 0.00 USD | `+83.42%` | `16,208.00` |
| `Live` | `Short` | `16.41` | 1,420,000.00 USD | 22,540.00 USD | 0.00 USD | `+84.89%` | `1,373.91` |
| `Live` | `Short` | `16.52` | 1,420,000.00 USD | 190.91 USD | 0.00 USD | `+86.13%` | `11.56` |
| `Live` | `Short` | `16.55` | 1,500,000.00 USD | 83,400.00 USD | 0.00 USD | `+86.58%` | `5,037.66` |
| `Live` | `Short` | `16.75` | 1,500,000.00 USD | 162.26 USD | 0.00 USD | `+88.72%` | `9.69` |
| `Live` | `Short` | `17.02` | 1,500,000.00 USD | 191.87 USD | 0.00 USD | `+91.87%` | `11.27` |
| `Live` | `Short` | `17.14` | 1,500,000.00 USD | 1,710.00 USD | 0.00 USD | `+93.11%` | `100.00` |
| `Live` | `Short` | `17.46` | 1,500,000.00 USD | 101.47 USD | 0.00 USD | `+96.83%` | `5.81` |
| `Live` | `Short` | `17.62` | 1,510,000.00 USD | 4,120.00 USD | 0.00 USD | `+98.64%` | `233.67` |
| `Live` | `Short` | `17.64` | 1,510,000.00 USD | 4,930.00 USD | 0.00 USD | `+98.86%` | `279.46` |
| `Live` | `Short` | `17.66` | 1,510,000.00 USD | 2,660.00 USD | 0.00 USD | `+99.09%` | `150.82` |
| `Live` | `Short` | `17.70` | 1,510,000.00 USD | 108.89 USD | 0.00 USD | `+99.54%` | `6.15` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 338,360.00 USD | 0.00 USD | 611.73 USD | `-73.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 337,750.00 USD | 0.00 USD | 793.75 USD | `-54.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 336,960.00 USD | 0.00 USD | 105.04 USD | `-49.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 336,850.00 USD | 0.00 USD | 67,970.00 USD | `-43.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 268,890.00 USD | 0.00 USD | 205.30 USD | `-40.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 268,680.00 USD | 0.00 USD | 465.42 USD | `-38.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 268,220.00 USD | 0.00 USD | 349.35 USD | `-37.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 267,870.00 USD | 0.00 USD | 1,330.00 USD | `-34.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 266,540.00 USD | 0.00 USD | 493.50 USD | `-33.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 266,040.00 USD | 0.00 USD | 100.98 USD | `-32.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 265,940.00 USD | 0.00 USD | 620.80 USD | `-32.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 265,320.00 USD | 0.00 USD | 4,160.00 USD | `-31.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 261,170.00 USD | 0.00 USD | 6,500.00 USD | `-30.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 254,670.00 USD | 0.00 USD | 864.38 USD | `-29.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 253,800.00 USD | 0.00 USD | 1,430.00 USD | `-26.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 252,370.00 USD | 0.00 USD | 4,340.00 USD | `-26.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 248,030.00 USD | 0.00 USD | 5,520.00 USD | `-24.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 242,510.00 USD | 0.00 USD | 100.72 USD | `-24.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 242,410.00 USD | 0.00 USD | 296.34 USD | `-23.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 242,110.00 USD | 0.00 USD | 921.19 USD | `-23.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 241,190.00 USD | 0.00 USD | 709.98 USD | `-22.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 240,480.00 USD | 0.00 USD | 262.44 USD | `-21.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 240,220.00 USD | 0.00 USD | 3,610.00 USD | `-21.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 236,600.00 USD | 0.00 USD | 6,790.00 USD | `-19.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 229,810.00 USD | 0.00 USD | 9,770.00 USD | `-19.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 220,050.00 USD | 0.00 USD | 103.46 USD | `-18.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 219,940.00 USD | 0.00 USD | 603.44 USD | `-18.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 219,340.00 USD | 0.00 USD | 891.57 USD | `-18.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 218,450.00 USD | 0.00 USD | 2,300.00 USD | `-17.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 216,140.00 USD | 0.00 USD | 129.58 USD | `-17.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 216,010.00 USD | 0.00 USD | 236.19 USD | `-17.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 215,780.00 USD | 0.00 USD | 199.39 USD | `-15.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 215,580.00 USD | 0.00 USD | 4,730.00 USD | `-15.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 210,850.00 USD | 0.00 USD | 37,420.00 USD | `-15.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 173,420.00 USD | 0.00 USD | 778.49 USD | `-15.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 172,640.00 USD | 0.00 USD | 799.83 USD | `-15.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 171,840.00 USD | 0.00 USD | 103.41 USD | `-14.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 171,740.00 USD | 0.00 USD | 1,370.00 USD | `-14.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 170,370.00 USD | 0.00 USD | 360.13 USD | `-13.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 170,010.00 USD | 0.00 USD | 175.42 USD | `-12.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 169,830.00 USD | 0.00 USD | 2,990.00 USD | `-12.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 166,840.00 USD | 0.00 USD | 143.51 USD | `-11.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 166,690.00 USD | 0.00 USD | 183.33 USD | `-11.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.88` | 166,510.00 USD | 0.00 USD | 194.52 USD | `-11.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 166,310.00 USD | 0.00 USD | 394.75 USD | `-11.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 165,920.00 USD | 0.00 USD | 1,350.00 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 164,570.00 USD | 0.00 USD | 1,590.00 USD | `-10.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 162,990.00 USD | 0.00 USD | 898.42 USD | `-10.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.97` | 162,090.00 USD | 0.00 USD | 107.74 USD | `-10.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 161,980.00 USD | 0.00 USD | 1,350.00 USD | `-9.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 160,630.00 USD | 0.00 USD | 7,400.00 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 153,240.00 USD | 0.00 USD | 123.58 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 153,110.00 USD | 0.00 USD | 2,110.00 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 151,000.00 USD | 0.00 USD | 563.85 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 150,440.00 USD | 0.00 USD | 105.14 USD | `-8.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 150,330.00 USD | 0.00 USD | 367.76 USD | `-8.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 149,970.00 USD | 0.00 USD | 2,330.00 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 147,630.00 USD | 0.00 USD | 120.10 USD | `-8.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 147,510.00 USD | 0.00 USD | 6,500.00 USD | `-8.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 141,010.00 USD | 0.00 USD | 462.15 USD | `-8.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 140,550.00 USD | 0.00 USD | 654.53 USD | `-8.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 139,890.00 USD | 0.00 USD | 367.91 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 139,530.00 USD | 0.00 USD | 520.75 USD | `-7.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 139,010.00 USD | 0.00 USD | 167.22 USD | `-7.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 138,840.00 USD | 0.00 USD | 141.04 USD | `-7.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 138,700.00 USD | 0.00 USD | 1,780.00 USD | `-7.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 136,910.00 USD | 0.00 USD | 515.66 USD | `-7.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.22` | 136,400.00 USD | 0.00 USD | 165.40 USD | `-7.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 136,230.00 USD | 0.00 USD | 143.54 USD | `-7.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 136,090.00 USD | 0.00 USD | 168.64 USD | `-6.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 135,920.00 USD | 0.00 USD | 201.49 USD | `-6.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 135,720.00 USD | 0.00 USD | 6,530.00 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 129,190.00 USD | 0.00 USD | 1,140.00 USD | `-6.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 128,050.00 USD | 0.00 USD | 2,000.00 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 126,040.00 USD | 0.00 USD | 756.06 USD | `-5.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 125,290.00 USD | 0.00 USD | 970.35 USD | `-5.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 124,320.00 USD | 0.00 USD | 5,470.00 USD | `-5.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 118,850.00 USD | 0.00 USD | 100.74 USD | `-5.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 118,750.00 USD | 0.00 USD | 3,290.00 USD | `-5.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 115,470.00 USD | 0.00 USD | 358.56 USD | `-5.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 115,110.00 USD | 0.00 USD | 1,880.00 USD | `-5.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 113,220.00 USD | 0.00 USD | 140.36 USD | `-4.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 113,080.00 USD | 0.00 USD | 138.24 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 112,950.00 USD | 0.00 USD | 954.23 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 111,990.00 USD | 0.00 USD | 7,030.00 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.48` | 104,960.00 USD | 0.00 USD | 489.58 USD | `-4.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.51` | 104,470.00 USD | 0.00 USD | 5,630.00 USD | `-4.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.52` | 98,840.00 USD | 0.00 USD | 5,060.00 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.53` | 93,770.00 USD | 0.00 USD | 1,130.00 USD | `-3.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 92,650.00 USD | 0.00 USD | 132.45 USD | `-3.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 92,510.00 USD | 0.00 USD | 7,740.00 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.57` | 84,780.00 USD | 0.00 USD | 428.58 USD | `-3.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.59` | 84,350.00 USD | 0.00 USD | 2,500.00 USD | `-3.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.60` | 81,850.00 USD | 0.00 USD | 435.59 USD | `-3.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.61` | 81,410.00 USD | 0.00 USD | 1,080.00 USD | `-3.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 80,330.00 USD | 0.00 USD | 1,980.00 USD | `-2.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 78,350.00 USD | 0.00 USD | 2,740.00 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.63` | 75,610.00 USD | 0.00 USD | 103.19 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.64` | 75,510.00 USD | 0.00 USD | 103.31 USD | `-2.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 75,400.00 USD | 0.00 USD | 3,810.00 USD | `-2.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.66` | 71,600.00 USD | 0.00 USD | 196.87 USD | `-2.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.68` | 71,400.00 USD | 0.00 USD | 223.82 USD | `-2.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.69` | 71,180.00 USD | 0.00 USD | 990.09 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.70` | 70,190.00 USD | 0.00 USD | 5,010.00 USD | `-2.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 65,170.00 USD | 0.00 USD | 494.27 USD | `-1.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 64,680.00 USD | 0.00 USD | 134.30 USD | `-1.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.72` | 64,550.00 USD | 0.00 USD | 315.85 USD | `-1.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.73` | 64,230.00 USD | 0.00 USD | 1,390.00 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.74` | 62,840.00 USD | 0.00 USD | 933.70 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.76` | 61,910.00 USD | 0.00 USD | 6,140.00 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.77` | 55,770.00 USD | 0.00 USD | 39,810.00 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.78` | 15,960.00 USD | 0.00 USD | 114.25 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 15,840.00 USD | 0.00 USD | 4,230.00 USD | `-0.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 11,610.00 USD | 0.00 USD | 299.65 USD | `-0.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.80` | 11,310.00 USD | 0.00 USD | 1,760.00 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.81` | 9,550.00 USD | 0.00 USD | 705.20 USD | `-0.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.82` | 8,850.00 USD | 0.00 USD | 2,030.00 USD | `-0.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.84` | 6,820.00 USD | 0.00 USD | 243.40 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 6,570.00 USD | 0.00 USD | 5,760.00 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.86` | 807.74 USD | 0.00 USD | 192.86 USD | `-0.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.87` | 614.88 USD | 0.00 USD | 614.88 USD | `-0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 543.33 USD | 543.33 USD | 0.00 USD | `+0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 1,650.00 USD | 1,100.00 USD | 0.00 USD | `+0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 1,840.00 USD | 188.66 USD | 0.00 USD | `+0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 2,620.00 USD | 788.72 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 5,980.00 USD | 3,360.00 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 6,090.00 USD | 110.58 USD | 0.00 USD | `+0.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 7,110.00 USD | 1,020.00 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 7,340.00 USD | 223.62 USD | 0.00 USD | `+0.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 7,470.00 USD | 137.73 USD | 0.00 USD | `+0.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 10,650.00 USD | 3,170.00 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 325,800.00 USD | 315,150.00 USD | 0.00 USD | `+1.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 325,900.00 USD | 104.59 USD | 0.00 USD | `+1.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 326,680.00 USD | 776.54 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 327,210.00 USD | 531.20 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 328,590.00 USD | 1,380.00 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 329,680.00 USD | 1,090.00 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 330,290.00 USD | 616.37 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 330,480.00 USD | 188.59 USD | 0.00 USD | `+1.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 330,930.00 USD | 453.84 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 331,100.00 USD | 160.99 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 331,510.00 USD | 415.00 USD | 0.00 USD | `+2.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 333,020.00 USD | 1,510.00 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 335,060.00 USD | 2,040.00 USD | 0.00 USD | `+2.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 562,690.00 USD | 227,630.00 USD | 0.00 USD | `+2.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 565,730.00 USD | 3,030.00 USD | 0.00 USD | `+2.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.13` | 569,220.00 USD | 3,500.00 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 571,220.00 USD | 2,000.00 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 965,440.00 USD | 394,210.00 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,000,000.00 USD | 39,130.00 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.20` | 1,010,000.00 USD | 1,590.00 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,010,000.00 USD | 8,580.00 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,010,000.00 USD | 131.87 USD | 0.00 USD | `+3.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,020,000.00 USD | 687.91 USD | 0.00 USD | `+3.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,020,000.00 USD | 954.71 USD | 0.00 USD | `+4.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,420,000.00 USD | 398,520.00 USD | 0.00 USD | `+4.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.27` | 1,420,000.00 USD | 205.87 USD | 0.00 USD | `+4.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,420,000.00 USD | 1,960.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,420,000.00 USD | 434.45 USD | 0.00 USD | `+4.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,440,000.00 USD | 18,610.00 USD | 0.00 USD | `+4.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,440,000.00 USD | 354.81 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,440,000.00 USD | 2,180.00 USD | 0.00 USD | `+5.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,440,000.00 USD | 579.86 USD | 0.00 USD | `+5.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,770,000.00 USD | 327,430.00 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,770,000.00 USD | 233.38 USD | 0.00 USD | `+5.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,770,000.00 USD | 163.41 USD | 0.00 USD | `+5.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,770,000.00 USD | 1,150.00 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,770,000.00 USD | 660.84 USD | 0.00 USD | `+5.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,770,000.00 USD | 2,480.00 USD | 0.00 USD | `+6.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,770,000.00 USD | 1,110.00 USD | 0.00 USD | `+6.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,770,000.00 USD | 109.92 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,770,000.00 USD | 140.35 USD | 0.00 USD | `+6.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,770,000.00 USD | 1,890.00 USD | 0.00 USD | `+6.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.47` | 1,780,000.00 USD | 1,780.00 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,780,000.00 USD | 2,210.00 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,780,000.00 USD | 288.46 USD | 0.00 USD | `+7.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.51` | 1,780,000.00 USD | 1,600.00 USD | 0.00 USD | `+7.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,780,000.00 USD | 103.54 USD | 0.00 USD | `+7.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.54` | 1,780,000.00 USD | 1,320.00 USD | 0.00 USD | `+7.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.56` | 1,780,000.00 USD | 535.35 USD | 0.00 USD | `+7.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,780,000.00 USD | 231.00 USD | 0.00 USD | `+8.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,780,000.00 USD | 221.07 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,780,000.00 USD | 1,470.00 USD | 0.00 USD | `+8.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,780,000.00 USD | 148.48 USD | 0.00 USD | `+8.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,780,000.00 USD | 329.43 USD | 0.00 USD | `+8.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,790,000.00 USD | 446.58 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,790,000.00 USD | 108.21 USD | 0.00 USD | `+9.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,790,000.00 USD | 169.68 USD | 0.00 USD | `+9.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,790,000.00 USD | 121.87 USD | 0.00 USD | `+10.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.80` | 1,790,000.00 USD | 619.28 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,790,000.00 USD | 5,030.00 USD | 0.00 USD | `+10.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,790,000.00 USD | 340.05 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,790,000.00 USD | 742.12 USD | 0.00 USD | `+11.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,790,000.00 USD | 899.47 USD | 0.00 USD | `+11.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,860,000.00 USD | 70,020.00 USD | 0.00 USD | `+11.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,860,000.00 USD | 373.97 USD | 0.00 USD | `+11.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,870,000.00 USD | 5,280.00 USD | 0.00 USD | `+12.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,880,000.00 USD | 6,370.00 USD | 0.00 USD | `+13.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,880,000.00 USD | 202.10 USD | 0.00 USD | `+13.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,090,000.00 USD | 210,980.00 USD | 0.00 USD | `+14.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,090,000.00 USD | 1,150.00 USD | 0.00 USD | `+14.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 2,090,000.00 USD | 172.16 USD | 0.00 USD | `+15.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 2,090,000.00 USD | 868.36 USD | 0.00 USD | `+15.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 2,090,000.00 USD | 489.40 USD | 0.00 USD | `+16.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 2,090,000.00 USD | 1,200.00 USD | 0.00 USD | `+16.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 2,090,000.00 USD | 118.01 USD | 0.00 USD | `+17.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 2,090,000.00 USD | 312.31 USD | 0.00 USD | `+18.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 2,090,000.00 USD | 1,530.00 USD | 0.00 USD | `+18.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 2,090,000.00 USD | 178.46 USD | 0.00 USD | `+19.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.62` | 2,090,000.00 USD | 153.11 USD | 0.00 USD | `+19.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 2,090,000.00 USD | 173.42 USD | 0.00 USD | `+20.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 2,090,000.00 USD | 184.75 USD | 0.00 USD | `+20.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 2,090,000.00 USD | 135.78 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 2,090,000.00 USD | 127.96 USD | 0.00 USD | `+22.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 2,090,000.00 USD | 476.43 USD | 0.00 USD | `+22.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 2,100,000.00 USD | 1,730.00 USD | 0.00 USD | `+22.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 2,100,000.00 USD | 118.97 USD | 0.00 USD | `+23.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 2,100,000.00 USD | 251.06 USD | 0.00 USD | `+23.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 2,100,000.00 USD | 552.44 USD | 0.00 USD | `+23.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 2,100,000.00 USD | 1,750.00 USD | 0.00 USD | `+24.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 2,100,000.00 USD | 320.29 USD | 0.00 USD | `+25.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 2,100,000.00 USD | 1,100.00 USD | 0.00 USD | `+25.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 2,100,000.00 USD | 2,610.00 USD | 0.00 USD | `+26.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 2,100,000.00 USD | 1,270.00 USD | 0.00 USD | `+26.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 2,110,000.00 USD | 1,380.00 USD | 0.00 USD | `+27.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 2,110,000.00 USD | 2,410.00 USD | 0.00 USD | `+28.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 2,120,000.00 USD | 9,520.00 USD | 0.00 USD | `+29.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 2,120,000.00 USD | 3,530.00 USD | 0.00 USD | `+29.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 2,130,000.00 USD | 7,700.00 USD | 0.00 USD | `+30.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 2,130,000.00 USD | 1,130.00 USD | 0.00 USD | `+33.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 2,130,000.00 USD | 434.61 USD | 0.00 USD | `+33.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 2,130,000.00 USD | 163.52 USD | 0.00 USD | `+33.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 2,250,000.00 USD | 124,300.00 USD | 0.00 USD | `+35.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.51` | 2,260,000.00 USD | 2,770.00 USD | 0.00 USD | `+40.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 2,260,000.00 USD | 3,350.00 USD | 0.00 USD | `+43.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 2,260,000.00 USD | 197.97 USD | 0.00 USD | `+44.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 2,260,000.00 USD | 3,200.00 USD | 0.00 USD | `+45.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 2,260,000.00 USD | 179.58 USD | 0.00 USD | `+46.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 2,260,000.00 USD | 720.74 USD | 0.00 USD | `+46.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.07` | 2,270,000.00 USD | 504.17 USD | 0.00 USD | `+47.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 2,270,000.00 USD | 169.57 USD | 0.00 USD | `+48.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.30` | 2,270,000.00 USD | 159.66 USD | 0.00 USD | `+49.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 2,270,000.00 USD | 446.52 USD | 0.00 USD | `+50.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.46` | 2,270,000.00 USD | 1,710.00 USD | 0.00 USD | `+51.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 2,270,000.00 USD | 5,320.00 USD | 0.00 USD | `+51.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,480,000.00 USD | 207,980.00 USD | 0.00 USD | `+52.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,480,000.00 USD | 407.95 USD | 0.00 USD | `+54.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,480,000.00 USD | 174.91 USD | 0.00 USD | `+55.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,490,000.00 USD | 9,230.00 USD | 0.00 USD | `+57.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,490,000.00 USD | 960.26 USD | 0.00 USD | `+60.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,490,000.00 USD | 2,710.00 USD | 0.00 USD | `+61.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,500,000.00 USD | 805.90 USD | 0.00 USD | `+63.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,500,000.00 USD | 655.55 USD | 0.00 USD | `+65.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,500,000.00 USD | 4,890.00 USD | 0.00 USD | `+66.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,500,000.00 USD | 471.09 USD | 0.00 USD | `+67.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,500,000.00 USD | 383.85 USD | 0.00 USD | `+68.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 3,150,000.00 USD | 652,070.00 USD | 0.00 USD | `+69.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 3,150,000.00 USD | 111.87 USD | 0.00 USD | `+78.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 3,150,000.00 USD | 219.91 USD | 0.00 USD | `+80.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 3,150,000.00 USD | 121.74 USD | 0.00 USD | `+91.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.00` | 3,150,000.00 USD | 297.59 USD | 0.00 USD | `+91.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.18` | 3,160,000.00 USD | 4,500.00 USD | 0.00 USD | `+93.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.20` | 3,280,000.00 USD | 120,270.00 USD | 0.00 USD | `+93.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.34` | 3,280,000.00 USD | 122.39 USD | 0.00 USD | `+95.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.50` | 3,280,000.00 USD | 586.59 USD | 0.00 USD | `+97.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.61` | 3,280,000.00 USD | 580.97 USD | 0.00 USD | `+98.41%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.76` | 9,520,000.00 USD | 0.00 USD | 9,520,000.00 USD | 1,790.00 USD | 5,760.00 USD | 0.00 USD |
| `7D` | `7.78` | 9,520,000.00 USD | 0.00 USD | 9,520,000.00 USD | 23,430.00 USD | 4,900.00 USD | 20,150.00 USD |
| `7D` | `7.80` | 9,470,000.00 USD | 0.00 USD | 9,470,000.00 USD | 13,050.00 USD | 12,980.00 USD | 0.00 USD |
| `7D` | `7.82` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,280.00 USD |
| `7D` | `7.84` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 29,020.00 USD | 2,380.00 USD | 19,730.00 USD |
| `7D` | `7.86` | 9,380,000.00 USD | 0.00 USD | 9,380,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD |
| `7D` | `7.88` | 9,330,000.00 USD | 0.00 USD | 9,330,000.00 USD | 46,450.00 USD | 12,780.00 USD | 29,190.00 USD |
| `7D` | `7.90` | 9,240,000.00 USD | 0.00 USD | 9,240,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,650.00 USD |
| `7D` | `7.92` | 9,180,000.00 USD | 0.00 USD | 9,180,000.00 USD | 53,660.00 USD | 8,420.00 USD | 14,900.00 USD |
| `1D` | `7.93` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 12,900.00 USD | 2,950.00 USD | 3,970.00 USD |
| `1D` | `7.94` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 7,510.00 USD | 4,150.00 USD | 1,730.00 USD |
| `7D` | `7.94` | 9,100,000.00 USD | 0.00 USD | 9,100,000.00 USD | 38,370.00 USD | 9,960.00 USD | 31,670.00 USD |
| `1D` | `7.95` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 74.90 USD | 4,140.00 USD | 2,440.00 USD |
| `1D` | `7.96` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 133.15 USD | 1,790.00 USD | 8.59 USD |
| `7D` | `7.96` | 9,020,000.00 USD | 0.00 USD | 9,020,000.00 USD | 21,840.00 USD | 6,920.00 USD | 26,340.00 USD |
| `1D` | `7.97` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 5,250.00 USD | 0.00 USD | 2,280.00 USD |
| `1D` | `7.98` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD |
| `7D` | `7.98` | 8,970,000.00 USD | 0.00 USD | 8,970,000.00 USD | 43,200.00 USD | 19,680.00 USD | 70,210.00 USD |
| `1D` | `7.99` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 675.88 USD | 677.82 USD | 0.00 USD |
| `1D` | `8.00` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD |
| `7D` | `8.00` | 8,830,000.00 USD | 0.00 USD | 8,830,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,130.00 USD |
| `1D` | `8.01` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 6,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.02` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 9,100.00 USD | 770.83 USD | 9.39 USD |
| `7D` | `8.02` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 20,910.00 USD | 28,440.00 USD | 10,370.00 USD |
| `1D` | `8.03` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 9,140.00 USD | 1,540.00 USD | 4,430.00 USD |
| `1D` | `8.04` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 9,860.00 USD | 0.00 USD | 11,460.00 USD |
| `7D` | `8.04` | 8,700,000.00 USD | 0.00 USD | 8,700,000.00 USD | 123,080.00 USD | 27,860.00 USD | 86,550.00 USD |
| `1D` | `8.05` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 17,150.00 USD | 4,800.00 USD | 2,250.00 USD |
| `1D` | `8.06` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 17,130.00 USD | 1,700.00 USD | 5,880.00 USD |
| `7D` | `8.06` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 70,840.00 USD | 10,070.00 USD | 86,170.00 USD |
| `1D` | `8.07` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 1,100.00 USD | 2,400.00 USD | 6,030.00 USD |
| `1D` | `8.08` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 4,700.00 USD | 1,410.00 USD | 3,220.00 USD |
| `7D` | `8.08` | 8,290,000.00 USD | 0.00 USD | 8,290,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,860.00 USD |
| `1D` | `8.09` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 9,630.00 USD | 1,220.00 USD | 6,380.00 USD |
| `1D` | `8.10` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 23,830.00 USD | 3,750.00 USD | 8,060.00 USD |
| `7D` | `8.10` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 61,500.00 USD | 19,700.00 USD | 14,170.00 USD |
| `1D` | `8.11` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 4,510.00 USD | 4,240.00 USD | 1,360.00 USD |
| `1D` | `8.12` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 9,910.00 USD | 0.00 USD | 7,240.00 USD |
| `7D` | `8.12` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 27,520.00 USD | 10,810.00 USD | 9,260.00 USD |
| `1D` | `8.13` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 7,130.00 USD | 693.45 USD | 1,310.00 USD |
| `1D` | `8.14` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 16,900.00 USD | 0.00 USD | 26.83 USD |
| `7D` | `8.14` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 72,460.00 USD | 11,150.00 USD | 39,780.00 USD |
| `1D` | `8.15` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 14,590.00 USD | 662.47 USD | 5,000.00 USD |
| `1D` | `8.16` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 385.98 USD | 2,120.00 USD | 47.18 USD |
| `7D` | `8.16` | 7,990,000.00 USD | 0.00 USD | 7,990,000.00 USD | 38,430.00 USD | 5,510.00 USD | 30,640.00 USD |
| `1D` | `8.17` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 2,970.00 USD | 0.00 USD | 12.32 USD |
| `1D` | `8.18` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 1,150.00 USD | 1,980.00 USD | 466.21 USD |
| `7D` | `8.18` | 7,910,000.00 USD | 0.00 USD | 7,910,000.00 USD | 10,520.00 USD | 6,790.00 USD | 2,750.00 USD |
| `1D` | `8.19` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 4,450.00 USD | 0.00 USD | 19.88 USD |
| `1D` | `8.20` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 7,720.00 USD | 2,310.00 USD | 431.88 USD |
| `7D` | `8.20` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 34,140.00 USD | 0.00 USD | 9,870.00 USD |
| `1D` | `8.21` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.22` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 5,330.00 USD | 0.00 USD | 12,570.00 USD |
| `7D` | `8.22` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 19,850.00 USD | 0.00 USD | 10,790.00 USD |
| `1D` | `8.23` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 20,790.00 USD | 4,080.00 USD | 31,000.00 USD |
| `1D` | `8.24` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 10,190.00 USD | 1,150.00 USD | 3,510.00 USD |
| `7D` | `8.24` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 39,950.00 USD | 3,480.00 USD | 107,080.00 USD |
| `1D` | `8.25` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 8,080.00 USD | 0.00 USD | 6,090.00 USD |
| `1D` | `8.26` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 192.60 USD | 11,460.00 USD | 0.00 USD |
| `7D` | `8.26` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 30,490.00 USD | 5,750.00 USD | 9,280.00 USD |
| `1D` | `8.27` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 11,310.00 USD | 2,760.00 USD | 21.52 USD |
| `1D` | `8.28` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 74,500.00 USD | 7,070.00 USD | 40,790.00 USD |
| `7D` | `8.28` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 122,850.00 USD | 33,920.00 USD | 14,010.00 USD |
| `1D` | `8.29` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 35,140.00 USD | 9,470.00 USD | 4,640.00 USD |
| `1D` | `8.30` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 53,200.00 USD | 13,130.00 USD | 19,010.00 USD |
| `7D` | `8.30` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 101,900.00 USD | 13,500.00 USD | 47,820.00 USD |
| `1D` | `8.31` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 56,000.00 USD | 11,410.00 USD | 1,570.00 USD |
| `1D` | `8.32` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 20,190.00 USD | 4,190.00 USD | 7,320.00 USD |
| `7D` | `8.32` | 7,290,000.00 USD | 0.00 USD | 7,290,000.00 USD | 61,880.00 USD | 26,020.00 USD | 4,900.00 USD |
| `1D` | `8.33` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 2,970.00 USD | 22,580.00 USD | 9,950.00 USD |
| `1D` | `8.34` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 14,500.00 USD | 4,810.00 USD | 6,270.00 USD |
| `7D` | `8.34` | 7,200,000.00 USD | 0.00 USD | 7,200,000.00 USD | 37,760.00 USD | 15,520.00 USD | 30,360.00 USD |
| `1D` | `8.35` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 6,790.00 USD | 11,270.00 USD | 16,070.00 USD |
| `1D` | `8.36` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 4,230.00 USD | 2,420.00 USD | 21,790.00 USD |
| `7D` | `8.36` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 107,760.00 USD | 13,470.00 USD | 71,060.00 USD |
| `1D` | `8.37` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 21,970.00 USD | 7,980.00 USD | 8,340.00 USD |
| `1D` | `8.38` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 35,970.00 USD | 4,080.00 USD | 33,870.00 USD |
| `7D` | `8.38` | 6,920,000.00 USD | 0.00 USD | 6,920,000.00 USD | 143,540.00 USD | 20,560.00 USD | 66,570.00 USD |
| `1D` | `8.39` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 63,440.00 USD | 10,540.00 USD | 56,460.00 USD |
| `1D` | `8.40` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 67,650.00 USD | 22,890.00 USD | 67,990.00 USD |
| `7D` | `8.40` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 150,350.00 USD | 19,710.00 USD | 220,030.00 USD |
| `1D` | `8.41` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 33,190.00 USD | 3,620.00 USD | 20,930.00 USD |
| `1D` | `8.42` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 33,600.00 USD | 12,790.00 USD | 18,430.00 USD |
| `7D` | `8.42` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 178,300.00 USD | 57,340.00 USD | 72,790.00 USD |
| `1D` | `8.43` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 29,980.00 USD | 34,530.00 USD | 14,410.00 USD |
| `1D` | `8.44` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 35,960.00 USD | 8,900.00 USD | 5,560.00 USD |
| `7D` | `8.44` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 155,040.00 USD | 68,350.00 USD | 76,630.00 USD |
| `1D` | `8.45` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 73,020.00 USD | 14,270.00 USD | 45,640.00 USD |
| `1D` | `8.46` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 133,440.00 USD | 8,250.00 USD | 47,800.00 USD |
| `7D` | `8.46` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 392,550.00 USD | 59,170.00 USD | 107,670.00 USD |
| `1D` | `8.47` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 103,290.00 USD | 30,070.00 USD | 15,180.00 USD |
| `1D` | `8.48` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 126,360.00 USD | 36,620.00 USD | 46,270.00 USD |
| `7D` | `8.48` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 317,690.00 USD | 61,660.00 USD | 220,080.00 USD |
| `1D` | `8.49` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 121,830.00 USD | 32,760.00 USD | 5,300.00 USD |
| `1D` | `8.50` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 51,910.00 USD | 11,120.00 USD | 26,230.00 USD |
| `7D` | `8.50` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 191,430.00 USD | 100,070.00 USD | 112,460.00 USD |
| `1D` | `8.51` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 8,030.00 USD | 46,200.00 USD | 20,840.00 USD |
| `1D` | `8.52` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 48,940.00 USD | 18,950.00 USD | 23,620.00 USD |
| `7D` | `8.52` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 271,100.00 USD | 98,920.00 USD | 250,640.00 USD |
| `1D` | `8.53` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 17,330.00 USD | 29,630.00 USD | 41,670.00 USD |
| `1D` | `8.54` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 19,400.00 USD | 6,040.00 USD | 43,640.00 USD |
| `7D` | `8.54` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 379,850.00 USD | 78,380.00 USD | 152,160.00 USD |
| `1D` | `8.55` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 64,630.00 USD | 19,250.00 USD | 19,190.00 USD |
| `1D` | `8.56` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 69,420.00 USD | 12,010.00 USD | 67,740.00 USD |
| `7D` | `8.56` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 593,510.00 USD | 101,070.00 USD | 88,350.00 USD |
| `1D` | `8.57` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 73,460.00 USD | 11,140.00 USD | 73,570.00 USD |
| `1D` | `8.58` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 87,680.00 USD | 21,440.00 USD | 39,900.00 USD |
| `7D` | `8.58` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 541,170.00 USD | 164,810.00 USD | 45,310.00 USD |
| `1D` | `8.59` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 70,460.00 USD | 29,830.00 USD | 25,420.00 USD |
| `1D` | `8.60` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 68,090.00 USD | 23,230.00 USD | 39,600.00 USD |
| `7D` | `8.60` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 75,040.00 USD | 39,160.00 USD | 206,190.00 USD |
| `1D` | `8.61` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 35,340.00 USD | 12,770.00 USD | 26,950.00 USD |
| `1D` | `8.62` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 102,610.00 USD | 17,600.00 USD | 23,130.00 USD |
| `7D` | `8.62` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 13,680.00 USD | 43,670.00 USD | 78,730.00 USD |
| `1D` | `8.63` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 38,050.00 USD | 2,010.00 USD | 9,310.00 USD |
| `1D` | `8.64` | 971,830.00 USD | 0.00 USD | 971,830.00 USD | 68,660.00 USD | 11,790.00 USD | 11,100.00 USD |
| `7D` | `8.64` | 906,450.00 USD | 0.00 USD | 906,450.00 USD | 73,980.00 USD | 5,680.00 USD | 10,650.00 USD |
| `1D` | `8.65` | 880,280.00 USD | 0.00 USD | 880,280.00 USD | 50,810.00 USD | 26,390.00 USD | 19,190.00 USD |
| `1D` | `8.66` | 783,890.00 USD | 0.00 USD | 783,890.00 USD | 36,050.00 USD | 19,900.00 USD | 10,190.00 USD |
| `7D` | `8.66` | 816,140.00 USD | 0.00 USD | 816,140.00 USD | 23,060.00 USD | 16,520.00 USD | 37,540.00 USD |
| `1D` | `8.67` | 717,750.00 USD | 0.00 USD | 717,750.00 USD | 33,710.00 USD | 5,480.00 USD | 23,170.00 USD |
| `1D` | `8.68` | 655,400.00 USD | 0.00 USD | 655,400.00 USD | 21,030.00 USD | 0.00 USD | 56.84 USD |
| `7D` | `8.68` | 739,010.00 USD | 0.00 USD | 739,010.00 USD | 93,990.00 USD | 24,870.00 USD | 173,670.00 USD |
| `1D` | `8.69` | 634,310.00 USD | 0.00 USD | 634,310.00 USD | 18,040.00 USD | 5,700.00 USD | 22,180.00 USD |
| `1D` | `8.70` | 588,390.00 USD | 0.00 USD | 588,390.00 USD | 34,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.70` | 446,480.00 USD | 0.00 USD | 446,480.00 USD | 0.00 USD | 12,790.00 USD | 22,290.00 USD |
| `1D` | `8.71` | 554,020.00 USD | 0.00 USD | 554,020.00 USD | 18,250.00 USD | 11,690.00 USD | 18,980.00 USD |
| `1D` | `8.73` | 505,100.00 USD | 0.00 USD | 505,100.00 USD | 44,990.00 USD | 2,720.00 USD | 5,120.00 USD |
| `1D` | `8.74` | 452,270.00 USD | 0.00 USD | 452,270.00 USD | 0.00 USD | 7,720.00 USD | 0.00 USD |
| `7D` | `8.74` | 411,400.00 USD | 0.00 USD | 411,400.00 USD | 144,660.00 USD | 19,690.00 USD | 56,610.00 USD |
| `1D` | `8.75` | 444,550.00 USD | 0.00 USD | 444,550.00 USD | 32,080.00 USD | 8,290.00 USD | 35,830.00 USD |
| `1D` | `8.76` | 368,350.00 USD | 0.00 USD | 368,350.00 USD | 78,530.00 USD | 15,050.00 USD | 0.00 USD |
| `7D` | `8.76` | 190,450.00 USD | 0.00 USD | 190,450.00 USD | 26,810.00 USD | 0.00 USD | 22,400.00 USD |
| `1D` | `8.77` | 274,780.00 USD | 0.00 USD | 274,780.00 USD | 54,300.00 USD | 8,510.00 USD | 25,720.00 USD |
| `1D` | `8.78` | 186,250.00 USD | 0.00 USD | 186,250.00 USD | 19,230.00 USD | 0.00 USD | 9,880.00 USD |
| `7D` | `8.78` | 141,240.00 USD | 0.00 USD | 141,240.00 USD | 0.00 USD | 0.00 USD | 58,840.00 USD |
| `1D` | `8.79` | 157,140.00 USD | 0.00 USD | 157,140.00 USD | 13,010.00 USD | 12,000.00 USD | 0.00 USD |
| `1D` | `8.80` | 132,130.00 USD | 0.00 USD | 132,130.00 USD | 30,940.00 USD | 5,690.00 USD | 6,590.00 USD |
| `7D` | `8.80` | 82,400.00 USD | 0.00 USD | 82,400.00 USD | 27,360.00 USD | 33,750.00 USD | 0.00 USD |
| `1D` | `8.81` | 88,900.00 USD | 0.00 USD | 88,900.00 USD | 26,650.00 USD | 0.00 USD | 10,950.00 USD |
| `1D` | `8.82` | 51,300.00 USD | 0.00 USD | 51,300.00 USD | 8,370.00 USD | 0.00 USD | 15,860.00 USD |
| `7D` | `8.82` | 21,290.00 USD | 0.00 USD | 21,290.00 USD | 0.00 USD | 0.00 USD | 21,290.00 USD |
| `1D` | `8.83` | 27,060.00 USD | 0.00 USD | 27,060.00 USD | 21,850.00 USD | 0.00 USD | 5,210.00 USD |
| `1D` | `8.84` | 98,130.00 USD | 98,130.00 USD | 0.00 USD | 29,490.00 USD | 0.00 USD | 68,640.00 USD |
| `1D` | `8.84` | 196,250.00 USD | 196,250.00 USD | 0.00 USD | 29,490.00 USD | 0.00 USD | 68,640.00 USD |
| `7D` | `8.84` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.86` | 263,630.00 USD | 263,630.00 USD | 0.00 USD | 67,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.90` | 341,400.00 USD | 341,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 77,770.00 USD |
| `7D` | `8.90` | 115,480.00 USD | 115,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 115,480.00 USD |
| `1D` | `8.92` | 352,960.00 USD | 352,960.00 USD | 0.00 USD | 8,060.00 USD | 0.00 USD | 3,500.00 USD |
| `1D` | `8.99` | 365,080.00 USD | 365,080.00 USD | 0.00 USD | 643.50 USD | 11,480.00 USD | 0.00 USD |
| `7D` | `9.00` | 288,400.00 USD | 288,400.00 USD | 0.00 USD | 161,560.00 USD | 11,360.00 USD | 0.00 USD |
| `1D` | `9.01` | 366,160.00 USD | 366,160.00 USD | 0.00 USD | 1,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.02` | 390,250.00 USD | 390,250.00 USD | 0.00 USD | 0.00 USD | 24,090.00 USD | 0.00 USD |
| `7D` | `9.02` | 346,850.00 USD | 346,850.00 USD | 0.00 USD | 2,330.00 USD | 56,120.00 USD | 0.00 USD |
| `1D` | `9.03` | 470,690.00 USD | 470,690.00 USD | 0.00 USD | 29,210.00 USD | 28,060.00 USD | 23,170.00 USD |
| `1D` | `9.04` | 484,470.00 USD | 484,470.00 USD | 0.00 USD | 0.00 USD | 4,810.00 USD | 8,970.00 USD |
| `7D` | `9.04` | 472,790.00 USD | 472,790.00 USD | 0.00 USD | 36,040.00 USD | 74,750.00 USD | 15,140.00 USD |
| `1D` | `9.05` | 552,770.00 USD | 552,770.00 USD | 0.00 USD | 3,520.00 USD | 26,530.00 USD | 38,250.00 USD |
| `1D` | `9.06` | 607,490.00 USD | 607,490.00 USD | 0.00 USD | 27,120.00 USD | 5,810.00 USD | 21,790.00 USD |
| `7D` | `9.06` | 532,500.00 USD | 532,500.00 USD | 0.00 USD | 5,610.00 USD | 14,960.00 USD | 39,130.00 USD |
| `1D` | `9.07` | 671,500.00 USD | 671,500.00 USD | 0.00 USD | 14,580.00 USD | 22,140.00 USD | 27,290.00 USD |
| `1D` | `9.08` | 713,120.00 USD | 713,120.00 USD | 0.00 USD | 1,260.00 USD | 6,490.00 USD | 33,870.00 USD |
| `7D` | `9.08` | 609,550.00 USD | 609,550.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD |
| `1D` | `9.09` | 871,680.00 USD | 871,680.00 USD | 0.00 USD | 99,950.00 USD | 17,120.00 USD | 41,490.00 USD |
| `1D` | `9.10` | 987,680.00 USD | 987,680.00 USD | 0.00 USD | 66,840.00 USD | 22,440.00 USD | 26,710.00 USD |
| `7D` | `9.10` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 797,340.00 USD | 35,760.00 USD | 325,210.00 USD |
| `1D` | `9.11` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 51,780.00 USD | 9,610.00 USD | 49,760.00 USD |
| `1D` | `9.12` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 106,750.00 USD | 31,620.00 USD | 6,270.00 USD |
| `7D` | `9.12` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 490,020.00 USD | 24,170.00 USD | 479,410.00 USD |
| `1D` | `9.13` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 84,020.00 USD | 20,120.00 USD | 40,100.00 USD |
| `1D` | `9.14` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 33,890.00 USD | 8,440.00 USD | 27,230.00 USD |
| `7D` | `9.14` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 536,560.00 USD | 18,540.00 USD | 479,710.00 USD |
| `1D` | `9.15` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 57,880.00 USD | 19,380.00 USD | 18,890.00 USD |
| `1D` | `9.16` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 43,310.00 USD | 9,390.00 USD | 27,740.00 USD |
| `7D` | `9.16` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 358,370.00 USD | 44,360.00 USD | 195,800.00 USD |
| `1D` | `9.17` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 89,060.00 USD | 18,740.00 USD | 55,730.00 USD |
| `1D` | `9.18` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 151,850.00 USD | 37,610.00 USD | 58,150.00 USD |
| `7D` | `9.18` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 506,170.00 USD | 162,460.00 USD | 263,140.00 USD |
| `1D` | `9.19` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 78,860.00 USD | 36,770.00 USD | 14,620.00 USD |
| `1D` | `9.20` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 106,980.00 USD | 10,810.00 USD | 65,640.00 USD |
| `7D` | `9.20` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 520,860.00 USD | 120,080.00 USD | 238,640.00 USD |
| `1D` | `9.21` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 39,120.00 USD | 4,510.00 USD | 8,070.00 USD |
| `1D` | `9.22` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 93,870.00 USD | 10,040.00 USD | 11,100.00 USD |
| `7D` | `9.22` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 585,170.00 USD | 140,390.00 USD | 416,230.00 USD |
| `1D` | `9.23` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 57,020.00 USD | 3,310.00 USD | 33,930.00 USD |
| `1D` | `9.24` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 30,460.00 USD | 2,940.00 USD | 0.00 USD |
| `7D` | `9.24` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 316,220.00 USD | 52,090.00 USD | 174,910.00 USD |
| `1D` | `9.25` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 18,710.00 USD | 17,700.00 USD | 9,510.00 USD |
| `1D` | `9.26` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 16,080.00 USD | 1,210.00 USD | 0.00 USD |
| `7D` | `9.26` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 273,920.00 USD | 96,980.00 USD | 60,730.00 USD |
| `1D` | `9.27` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 22,870.00 USD | 13,170.00 USD | 2,560.00 USD |
| `1D` | `9.28` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 20,250.00 USD | 3,860.00 USD | 10,360.00 USD |
| `7D` | `9.28` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 428,160.00 USD | 103,490.00 USD | 170,450.00 USD |
| `1D` | `9.29` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 48,940.00 USD | 18,260.00 USD | 31,090.00 USD |
| `1D` | `9.30` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 58,500.00 USD | 16,060.00 USD | 6,790.00 USD |
| `7D` | `9.30` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 199,810.00 USD | 97,780.00 USD | 262,830.00 USD |
| `1D` | `9.31` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 39,620.00 USD | 4,250.00 USD | 25,510.00 USD |
| `1D` | `9.32` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 10,000.00 USD | 2,530.00 USD | 10,830.00 USD |
| `7D` | `9.32` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 271,660.00 USD | 59,310.00 USD | 337,940.00 USD |
| `1D` | `9.33` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 16,620.00 USD | 6,000.00 USD | 15,710.00 USD |
| `1D` | `9.34` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 15,860.00 USD | 4,190.00 USD | 12,940.00 USD |
| `7D` | `9.34` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 203,440.00 USD | 53,150.00 USD | 70,360.00 USD |
| `1D` | `9.35` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 28,980.00 USD | 3,810.00 USD | 24,920.00 USD |
| `1D` | `9.36` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 66,220.00 USD | 13,630.00 USD | 25,050.00 USD |
| `7D` | `9.36` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 247,120.00 USD | 78,550.00 USD | 112,550.00 USD |
| `1D` | `9.37` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 37,700.00 USD | 13,410.00 USD | 6,010.00 USD |
| `1D` | `9.38` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 47,540.00 USD | 4,040.00 USD | 27,020.00 USD |
| `7D` | `9.38` | 11,540,000.00 USD | 11,540,000.00 USD | 0.00 USD | 383,530.00 USD | 55,400.00 USD | 85,250.00 USD |
| `1D` | `9.39` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 16,470.00 USD | 1,730.00 USD | 3,240.00 USD |
| `1D` | `9.40` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 44,280.00 USD | 1,210.00 USD | 12.64 USD |
| `7D` | `9.40` | 11,990,000.00 USD | 11,990,000.00 USD | 0.00 USD | 234,760.00 USD | 58,130.00 USD | 153,100.00 USD |
| `1D` | `9.41` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 30,150.00 USD | 1,660.00 USD | 16,970.00 USD |
| `1D` | `9.42` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 10,620.00 USD | 622.99 USD | 4,030.00 USD |
| `7D` | `9.42` | 12,300,000.00 USD | 12,300,000.00 USD | 0.00 USD | 176,920.00 USD | 44,410.00 USD | 84,120.00 USD |
| `1D` | `9.43` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 10,390.00 USD | 6,940.00 USD | 12,400.00 USD |
| `1D` | `9.44` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 1,500.00 USD | 0.00 USD | 48.84 USD |
| `7D` | `9.44` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 41,250.00 USD | 19,420.00 USD | 56,550.00 USD |
| `1D` | `9.45` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 1,380.00 USD | 4,940.00 USD | 2,430.00 USD |
| `1D` | `9.46` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 1,320.00 USD | 4,580.00 USD | 0.00 USD |
| `7D` | `9.46` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 136,670.00 USD | 29,830.00 USD | 19,460.00 USD |
| `1D` | `9.47` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 18,510.00 USD | 6,870.00 USD | 192.20 USD |
| `1D` | `9.48` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 1,510.00 USD | 0.00 USD | 5,190.00 USD |
| `7D` | `9.48` | 12,670,000.00 USD | 12,670,000.00 USD | 0.00 USD | 12,180.00 USD | 30,160.00 USD | 25,250.00 USD |
| `1D` | `9.49` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 21,080.00 USD | 572.85 USD | 5,600.00 USD |
| `1D` | `9.50` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 11,990.00 USD | 3,160.00 USD | 6,320.00 USD |
| `7D` | `9.50` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 69,270.00 USD | 33,210.00 USD | 83,550.00 USD |
| `1D` | `9.51` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 295.05 USD | 0.00 USD | 124.70 USD |
| `1D` | `9.52` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 17,990.00 USD | 3,070.00 USD | 5,400.00 USD |
| `7D` | `9.52` | 13,040,000.00 USD | 13,040,000.00 USD | 0.00 USD | 102,150.00 USD | 29,320.00 USD | 51,740.00 USD |
| `1D` | `9.53` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 18,780.00 USD | 4,560.00 USD | 0.00 USD |
| `1D` | `9.54` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 5,910.00 USD | 1,470.00 USD | 2,930.00 USD |
| `7D` | `9.54` | 13,260,000.00 USD | 13,260,000.00 USD | 0.00 USD | 192,090.00 USD | 27,650.00 USD | 930.52 USD |
| `1D` | `9.55` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 2,910.00 USD | 6,330.00 USD | 3,100.00 USD |
| `1D` | `9.56` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 5,490.00 USD | 1,280.00 USD | 2,530.00 USD |
| `7D` | `9.56` | 13,380,000.00 USD | 13,380,000.00 USD | 0.00 USD | 89,210.00 USD | 5,260.00 USD | 32,680.00 USD |
| `1D` | `9.57` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 1,370.00 USD | 3,100.00 USD | 4,960.00 USD |
| `1D` | `9.58` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 1,290.00 USD | 563.17 USD | 7,730.00 USD |
| `7D` | `9.58` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 35,340.00 USD | 16,980.00 USD | 21,640.00 USD |
| `1D` | `9.59` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 5,050.00 USD | 1,250.00 USD | 1,170.00 USD |
| `1D` | `9.60` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 11,210.00 USD | 424.36 USD | 11,260.00 USD |
| `7D` | `9.60` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 39,470.00 USD | 10,820.00 USD | 33,120.00 USD |
| `1D` | `9.61` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD |
| `1D` | `9.62` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.62` | 13,640,000.00 USD | 13,640,000.00 USD | 0.00 USD | 70,470.00 USD | 13,850.00 USD | 17,600.00 USD |
| `1D` | `9.63` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 10,190.00 USD | 4,370.00 USD | 1,150.00 USD |
| `1D` | `9.64` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 5,830.00 USD | 0.00 USD | 3,410.00 USD |
| `7D` | `9.64` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 61,870.00 USD | 17,650.00 USD | 19,900.00 USD |
| `1D` | `9.65` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 5,960.00 USD | 4,150.00 USD | 1,740.00 USD |
| `1D` | `9.66` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 8,930.00 USD | 3,480.00 USD | 5,760.00 USD |
| `7D` | `9.66` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 37,340.00 USD | 21,280.00 USD | 18,480.00 USD |
| `1D` | `9.67` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 2,990.00 USD | 0.00 USD | 2,310.00 USD |
| `1D` | `9.68` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 12,900.00 USD | 2,950.00 USD | 3,970.00 USD |
| `7D` | `9.68` | 13,940,000.00 USD | 13,940,000.00 USD | 0.00 USD | 68,230.00 USD | 20,310.00 USD | 34,130.00 USD |
| `1D` | `9.70` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 7,510.00 USD | 4,150.00 USD | 1,730.00 USD |
| `7D` | `9.70` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 69,040.00 USD | 12,990.00 USD | 31,760.00 USD |
| `1D` | `9.71` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 74.90 USD | 4,140.00 USD | 2,460.00 USD |
| `1D` | `9.72` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 133.15 USD | 1,790.00 USD | 52.16 USD |
| `7D` | `9.72` | 14,160,000.00 USD | 14,160,000.00 USD | 0.00 USD | 71,790.00 USD | 6,920.00 USD | 26,820.00 USD |
| `1D` | `9.74` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 5,250.00 USD | 0.00 USD | 2,280.00 USD |
| `7D` | `9.74` | 14,200,000.00 USD | 14,200,000.00 USD | 0.00 USD | 10,890.00 USD | 7,200.00 USD | 19,560.00 USD |
| `1D` | `9.75` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 42.61 USD |
| `1D` | `9.76` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD |
| `7D` | `9.76` | 14,300,000.00 USD | 14,300,000.00 USD | 0.00 USD | 35,520.00 USD | 12,480.00 USD | 52,240.00 USD |
| `1D` | `9.77` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 193.50 USD | 677.82 USD | 0.00 USD |
| `1D` | `9.78` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD |
| `7D` | `9.78` | 14,380,000.00 USD | 14,380,000.00 USD | 0.00 USD | 65,390.00 USD | 10,300.00 USD | 5,270.00 USD |
| `1D` | `9.79` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 5,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.80` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 6,870.00 USD | 770.83 USD | 9.39 USD |
| `7D` | `9.80` | 14,440,000.00 USD | 14,440,000.00 USD | 0.00 USD | 18,630.00 USD | 28,440.00 USD | 10,680.00 USD |
| `1D` | `9.81` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 9,140.00 USD | 1,540.00 USD | 4,140.00 USD |
| `1D` | `9.82` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 7,220.00 USD | 0.00 USD | 11,460.00 USD |
| `7D` | `9.82` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 121,860.00 USD | 27,860.00 USD | 86,290.00 USD |
| `1D` | `9.83` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 16,240.00 USD | 4,800.00 USD | 1,920.00 USD |
| `7D` | `9.84` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 9,730.00 USD | 7,850.00 USD | 14,230.00 USD |
| `1D` | `9.85` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 11,610.00 USD | 1,700.00 USD | 3,530.00 USD |
| `1D` | `9.86` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 4,390.00 USD | 0.00 USD | 2,360.00 USD |
| `7D` | `9.86` | 14,840,000.00 USD | 14,840,000.00 USD | 0.00 USD | 59,550.00 USD | 2,210.00 USD | 72,010.00 USD |
| `1D` | `9.87` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 2,400.00 USD | 6,020.00 USD |
| `1D` | `9.88` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 3,930.00 USD | 1,410.00 USD | 3,220.00 USD |
| `7D` | `9.88` | 14,880,000.00 USD | 14,880,000.00 USD | 0.00 USD | 7,900.00 USD | 8,710.00 USD | 20,970.00 USD |
| `7D` | `9.90` | 14,970,000.00 USD | 14,970,000.00 USD | 0.00 USD | 55,970.00 USD | 19,700.00 USD | 14,360.00 USD |
| `7D` | `9.92` | 15,010,000.00 USD | 15,010,000.00 USD | 0.00 USD | 27,710.00 USD | 10,810.00 USD | 9,370.00 USD |
| `7D` | `9.94` | 15,130,000.00 USD | 15,130,000.00 USD | 0.00 USD | 69,320.00 USD | 11,150.00 USD | 39,810.00 USD |
| `7D` | `9.96` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 29,800.00 USD | 1,360.00 USD | 11,160.00 USD |
| `7D` | `9.98` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 840.10 USD | 4,150.00 USD | 18,990.00 USD |
| `7D` | `10.00` | 15,210,000.00 USD | 15,210,000.00 USD | 0.00 USD | 0.00 USD | 6,790.00 USD | 0.00 USD |
| `7D` | `10.02` | 15,230,000.00 USD | 15,230,000.00 USD | 0.00 USD | 15,960.00 USD | 0.00 USD | 5,890.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `382.46M` | Total OI Tokens: `43,258,198.2 AVAX`
  * 1h OI Change: `-0.69%` | 4h OI Change: `+0.06%` | 24h OI Change: `-1.45%`
  * Exchange Breakdown: Binance=`89.18M` | Bybit=`59.45M` | OKX=`12.74M` | Hyperliquid=`17.65M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `15.58K` | Last 24h: `33.77K` | Last 3d: `72.05K` | Last 7d: `92.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0097%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0094%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `38.70%` | `61.30%` | `0.63` | 6,790,000.00 USD |
| `15M` | `Binance` | `42.84%` | `57.16%` | `0.75` | 1,990,000.00 USD |
| `15M` | `OKX` | `36.41%` | `63.59%` | `0.57` | 486,070.00 USD |
| `15M` | `Bybit` | `29.14%` | `70.86%` | `0.41` | 663,790.00 USD |
| `15M` | `KuCoin` | `46.1%` | `53.9%` | `0.86` | 75,840.00 USD |
| `15M` | `Gate` | `35.91%` | `64.09%` | `0.56` | 56,340.00 USD |
| `15M` | `Bitget` | `44.14%` | `55.86%` | `0.79` | 226,260.00 USD |
| `15M` | `BingX` | `51.67%` | `48.33%` | `1.07` | 145,830.00 USD |
| `15M` | `MEXC` | `45.83%` | `54.17%` | `0.85` | 2,000,000.00 USD |
| `15M` | `Bitunix` | `20%` | `80%` | `0.25` | 250,380.00 USD |
| `15M` | `Hyperliquid` | `11.13%` | `88.87%` | `0.13` | 415,320.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `54.95%` | `45.05%` | `1.22` | 272,270.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 155,240.00 USD |
| `15M` | `HTX` | `22.3%` | `77.7%` | `0.29` | 891.85 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `13.03%` | `86.97%` | `0.15` | 37,410.00 USD |
| `15M` | `Aster` | `3.92%` | `96.08%` | `0.04` | 152.57 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `46.82%` | `53.18%` | `0.88` | 7,910.00 USD |
| `15M` | `Whale Positions` | `42.84%` | `57.16%` | `0.75` | 1,990,000.00 USD |
| `15M` | `Global Accounts` | `38.70%` | `61.30%` | `0.63` | 6,790,000.00 USD |
| `1H` | `AVAX` | `40.61%` | `59.39%` | `0.68` | 25,050,000.00 USD |
| `1H` | `Binance` | `43.39%` | `56.61%` | `0.77` | 6,740,000.00 USD |
| `1H` | `OKX` | `34.13%` | `65.87%` | `0.52` | 2,370,000.00 USD |
| `1H` | `Bybit` | `42.44%` | `57.56%` | `0.74` | 2,110,000.00 USD |
| `1H` | `KuCoin` | `45.05%` | `54.95%` | `0.82` | 214,660.00 USD |
| `1H` | `Gate` | `46.15%` | `53.85%` | `0.86` | 257,080.00 USD |
| `1H` | `Bitget` | `28.13%` | `71.87%` | `0.39` | 612,200.00 USD |
| `1H` | `BingX` | `41.69%` | `58.31%` | `0.71` | 820,340.00 USD |
| `1H` | `MEXC` | `51.75%` | `48.25%` | `1.07` | 8,720,000.00 USD |
| `1H` | `Bitunix` | `51.24%` | `48.76%` | `1.05` | 912,800.00 USD |
| `1H` | `Hyperliquid` | `14.33%` | `85.67%` | `0.17` | 888,880.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.03%` | `47.97%` | `1.08` | 628,540.00 USD |
| `1H` | `Crypto.com` | `20.03%` | `79.97%` | `0.25` | 0.00 USD |
| `1H` | `WhiteBIT` | `0%` | `100%` | `0.00` | 604,260.00 USD |
| `1H` | `HTX` | `43.81%` | `56.19%` | `0.78` | 4,790.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `42.43%` | `57.57%` | `0.74` | 112,280.00 USD |
| `1H` | `Aster` | `21.49%` | `78.51%` | `0.27` | 7,930.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `43.91%` | `56.09%` | `0.78` | 39,960.00 USD |
| `1H` | `Whale Positions` | `43.39%` | `56.61%` | `0.77` | 6,740,000.00 USD |
| `1H` | `Global Accounts` | `40.61%` | `59.39%` | `0.68` | 25,050,000.00 USD |
| `4H` | `AVAX` | `47.43%` | `52.57%` | `0.90` | 120,780,000.00 USD |
| `4H` | `Binance` | `48.81%` | `51.19%` | `0.95` | 37,300,000.00 USD |
| `4H` | `OKX` | `44.96%` | `55.04%` | `0.82` | 9,320,000.00 USD |
| `4H` | `Bybit` | `48.95%` | `51.05%` | `0.96` | 7,740,000.00 USD |
| `4H` | `KuCoin` | `48.19%` | `51.81%` | `0.93` | 1,070,000.00 USD |
| `4H` | `Gate` | `49.5%` | `50.5%` | `0.98` | 1,580,000.00 USD |
| `4H` | `Bitget` | `45.3%` | `54.7%` | `0.83` | 3,310,000.00 USD |
| `4H` | `BingX` | `44.8%` | `55.2%` | `0.81` | 4,130,000.00 USD |
| `4H` | `MEXC` | `48.75%` | `51.25%` | `0.95` | 40,330,000.00 USD |
| `4H` | `Bitunix` | `51.26%` | `48.74%` | `1.05` | 5,440,000.00 USD |
| `4H` | `Hyperliquid` | `47.82%` | `52.18%` | `0.92` | 3,540,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.9%` | `51.1%` | `0.96` | 2,960,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `4.11%` | `95.89%` | `0.04` | 2,640,000.00 USD |
| `4H` | `HTX` | `62.16%` | `37.84%` | `1.64` | 48,100.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44.08%` | `55.92%` | `0.79` | 609,270.00 USD |
| `4H` | `Aster` | `64.62%` | `35.38%` | `1.83` | 625,100.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.26%` | `58.74%` | `0.70` | 126,440.00 USD |
| `4H` | `Whale Positions` | `48.81%` | `51.19%` | `0.95` | 37,300,000.00 USD |
| `4H` | `Global Accounts` | `47.43%` | `52.57%` | `0.90` | 120,780,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `8.97` | `8.99` | `8.97` | `9.03` | `8.96` | 2,070,720.90 USD | 687,717.97 USD | 1,383,002.93 USD | -695,284.97 USD | `-33.58%` | `10B / 24S` |
| `0:00 UTC` | `8.94` | `8.95` | `8.94` | `8.97` | `8.93` | 1,552,686.03 USD | 580,933.43 USD | 971,752.60 USD | -390,819.17 USD | `-25.17%` | `3B / 11S` |
| `5:00 UTC` | `8.95` | `8.95` | `8.95` | `8.96` | `8.93` | 786,504.93 USD | 221,063.85 USD | 565,441.08 USD | -344,377.23 USD | `-43.79%` | `0B / 11S` |
| `0:00 UTC` | `8.93` | `8.93` | `8.93` | `8.96` | `8.91` | 1,932,405.67 USD | 423,821.82 USD | 1,508,583.84 USD | -1,084,762.02 USD | `-56.14%` | `2B / 26S` |
| `5:00 UTC` | `8.91` | `8.92` | `8.91` | `8.94` | `8.90` | 1,295,523.82 USD | 616,181.90 USD | 679,341.92 USD | -63,160.02 USD | `-4.88%` | `3B / 6S` |
| `0:00 UTC` | `8.94` | `8.90` | `8.94` | `8.94` | `8.85` | 1,871,719.04 USD | 766,811.36 USD | 1,104,907.68 USD | -338,096.31 USD | `-18.06%` | `8B / 28S` |
| `5:00 UTC` | `8.85` | `8.85` | `8.85` | `8.87` | `8.82` | 1,418,137.84 USD | 651,843.02 USD | 766,294.83 USD | -114,451.81 USD | `-8.07%` | `11B / 12S` |
| `0:00 UTC` | `8.87` | `8.87` | `8.87` | `8.88` | `8.86` | 651,856.32 USD | 369,195.26 USD | 282,661.06 USD | 86,534.20 USD | `+13.28%` | `5B / 4S` |
| `5:00 UTC` | `8.84` | `8.86` | `8.84` | `8.89` | `8.84` | 682,076.12 USD | 288,770.26 USD | 393,305.86 USD | -104,535.61 USD | `-15.33%` | `9B / 13S` |
| `0:00 UTC` | `8.80` | `8.82` | `8.80` | `8.84` | `8.80` | 562,790.75 USD | 204,086.74 USD | 358,704.01 USD | -154,617.27 USD | `-27.47%` | `7B / 10S` |

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
| `5m` | -20,820.00 USD | -306,730.00 USD | **`DISTRIBUTION`** |
| `15m` | 82,910.00 USD | -409,870.00 USD | **`DISTRIBUTION`** |
| `30m` | 78,440.00 USD | -206,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -80,950.00 USD | -1,470,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -194,290.00 USD | -3,510,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 230,430.00 USD | -3,660,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 39,860.00 USD | -3,320,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -89,900.00 USD | -3,840,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -87,170.00 USD | -3,080,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -96,790.00 USD | -5,310,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,710,000.00 USD | -43,110,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -52,980,000.00 USD | -275,190,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-20.82K` | 15m=`+82.91K` | 1h=`-80.95K` | 24h=`-96.79K`
* Futures Capital Netflows: 5m=`-306.73K` | 15m=`-409.87K` | 1h=`-1.47M` | 24h=`-5.31M`
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
  * `2026-10-29 23:31:27 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:27 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:27 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:00:27 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-30 00:00:27 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:00:27 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:02:27 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:02:27 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:02:27 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:27 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:27 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `8.58` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.45` (Risk Distance: `0.1262` pts)
  * +2.5R Take Profit: `8.90`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.91` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `9.04` (Risk Distance: `0.1262` pts)
  * +2.5R Take Profit: `8.59`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.88`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
