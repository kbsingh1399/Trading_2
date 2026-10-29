# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 21:43:08 IST` (`2026-10-29 16:13:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.81` | **Live Ask Quote**: `8.85` | **Mid Price**: `8.83`
- **Spread Points**: `4.00` | **Spread BPS**: `45.30 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.70` | VWAP Z-Score: `+1.01` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0487` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `59.44` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `8.99` | Lower -3.00σ Band: `8.41`
  * Upper +2.51σ Band: `8.94` | Lower -2.51σ Band: `8.46`
  * Upper +2.01σ Band: `8.90` | Lower -2.01σ Band: `8.51`
  * Upper +2.00σ Band: `8.90` | Lower -2.00σ Band: `8.51`
  * Upper +1.28σ Band: `8.83` | Lower -1.28σ Band: `8.58`
  * Upper +1.00σ Band: `8.80` | Lower -1.00σ Band: `8.61`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.77` | EMA-20=`8.74` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.74` (Slope: `+0.0000`) | EMA-100=`8.78`
  * Institutional Anchors: EMA-144=`8.80` | EMA-200=`8.81` (Slope: `-0.0797`) | EMA-233=`8.82`
- **Range Boundaries**: 24H High=`9.14` | 24H Low=`8.53` | Weekly High=`9.14` | Weekly Low=`8.53`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.81` (Distance: `+0.18%`)
  * Point of Control (POC) = `8.74` (Distance: `+1.04%`)
  * Value Area Low (VAL) = `8.59` (Distance: `+2.80%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`9.02` | POC=`8.99` | VAL=`8.86`
  * Prior Day Extremes: PDH=`9.14` | PDL=`8.76` | PDC=`8.99`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`8.96` | Weekly POC=`8.91` | Weekly VAL=`8.74`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`9.04` | Low=`8.53`
  * London Session (08:00-16:00 UTC): High=`8.81` | Low=`8.59`
  * New York Session (13:00-21:00 UTC): High=`8.83` | Low=`8.68`
  * Initial Balance (First Hour): IB High=`8.78` | IB Low=`8.65`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.79` - `8.87`
  * Optimal Trade Entry (OTE 0.705): `8.85`
  * Structural Invalidation Anchor (0.786): `8.90`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.82` | `8.84` | `8.80` | `8.82` | `51,586` | 454,957.09 USD | -58,569.03 USD | `-12.87%` | 724,076.02 USD | `-0.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `8.82` | `8.83` | `8.81` | `8.82` | `41,495` | 366,116.87 USD | 17,671.12 USD | `+4.83%` | 741,747.14 USD | `+0.22` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `8.82` | `8.84` | `8.81` | `8.84` | `19,728` | 174,069.93 USD | 30,429.91 USD | `+17.48%` | 772,177.05 USD | `+0.31` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.82` | `8.83` | `8.76` | `8.79` | `239,344` | 2,103,704.78 USD | -155,428.59 USD | `-7.39%` | 680,423.22 USD | `-0.80` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `8.79` | `8.85` | `8.78` | `8.82` | `153,877` | 1,356,806.78 USD | 102,221.83 USD | `+7.53%` | 782,645.05 USD | `+0.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `8.82` | `8.84` | `8.80` | `8.84` | `112,807` | 995,126.22 USD | -10,485.67 USD | `-1.05%` | 772,159.38 USD | `+0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `8.77` | `8.81` | `8.71` | `8.79` | `424,883` | 3,722,969.55 USD | -48,717.59 USD | `-1.31%` | 633,886.61 USD | `-0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `8.79` | `8.85` | `8.76` | `8.82` | `670,094` | 5,899,688.59 USD | -4,971.59 USD | `-0.08%` | 628,915.02 USD | `+0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `8.82` | `8.84` | `8.80` | `8.84` | `112,809` | 995,143.89 USD | -10,468.00 USD | `-1.05%` | 618,447.02 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.59` | `8.80` | `8.57` | `8.62` | `1,816,830` | 15,790,058.74 USD | 58,580.54 USD | `+0.37%` | 960,150.42 USD | `-0.11` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | 1,224,407.91 USD | `+0.01` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `8.85` | `8.71` | `8.84` | `1,207,784` | 10,617,784.36 USD | -64,174.86 USD | `-0.60%` | 1,160,233.05 USD | `-0.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.04` | `9.17` | `8.93` | `9.00` | `2,161,189` | 19,537,237.40 USD | 1,673,706.54 USD | `+8.57%` | 3,324,601.27 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `9.00` | `9.02` | `8.55` | `8.59` | `3,515,330` | 30,612,875.98 USD | -2,423,031.38 USD | `-7.92%` | 901,569.89 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.59` | `8.80` | `8.57` | `8.62` | `1,816,830` | 15,790,058.74 USD | 58,580.54 USD | `+0.37%` | 960,150.42 USD | `-0.11` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | 1,224,407.91 USD | `+0.01` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `8.85` | `8.71` | `8.84` | `1,207,784` | 10,617,784.36 USD | -64,174.86 USD | `-0.60%` | 1,160,233.05 USD | `-0.19` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`8.83`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BUY` | `8.65` | `2542.8500` | 21,999.98 USD | 4,326,832.96 USD | `STANDARD` | `-1.99%` | `0x0efb38a5fa` |
| `BUY` | `8.66` | `17508.7300` | 151,553.82 USD | 2,314,105.51 USD | `LARGE (>= USD 100K)` | `-1.95%` | `0x71d0e11ebb` |
| `BUY` | `8.67` | `193.7100` | 1,679.10 USD | 5,815,651.83 USD | `STANDARD` | `-1.81%` | `0x31ca8395cf` |
| `BUY` | `8.67` | `181.8100` | 1,576.11 USD | 5,817,227.94 USD | `STANDARD` | `-1.80%` | `0x010461c14e` |
| `BUY` | `8.68` | `11723.4300` | 101,800.40 USD | 3,778,636.91 USD | `LARGE (>= USD 100K)` | `-1.63%` | `0xecb63caa47` |
| `BUY` | `8.68` | `2098.0100` | 18,214.50 USD | 4,440,639.34 USD | `STANDARD` | `-1.65%` | `0xd3943e4008` |
| `BUY` | `8.68` | `315.7300` | 2,740.85 USD | 5,653,066.43 USD | `STANDARD` | `-1.66%` | `0x07fd993f0f` |
| `BUY` | `8.69` | `2185.7600` | 18,999.94 USD | 4,384,840.46 USD | `STANDARD` | `-1.53%` | `0x0efb38a5fa` |
| `BUY` | `8.69` | `387.9000` | 3,372.29 USD | 5,570,359.85 USD | `STANDARD` | `-1.52%` | `0x14f8e04290` |
| `BUY` | `8.70` | `12906.1700` | 112,287.55 USD | 3,345,326.77 USD | `LARGE (>= USD 100K)` | `-1.44%` | `0xecb63caa47` |
| `BUY` | `8.70` | `12876.9200` | 112,049.81 USD | 3,457,376.57 USD | `LARGE (>= USD 100K)` | `-1.43%` | `0x71d0e11ebb` |
| `BUY` | `8.71` | `52120.8200` | 454,029.68 USD | 917,795.56 USD | `LARGE (>= USD 100K)` | `-1.32%` | `0x71cfa5e263` |
| `BUY` | `8.72` | `17525.0400` | 152,804.33 USD | 2,162,551.69 USD | `LARGE (>= USD 100K)` | `-1.23%` | `0x71d0e11ebb` |
| `BUY` | `8.72` | `14611.3500` | 127,383.21 USD | 2,998,718.70 USD | `LARGE (>= USD 100K)` | `-1.24%` | `0xecb63caa47` |
| `BUY` | `8.72` | `1835.0700` | 15,999.98 USD | 4,456,639.31 USD | `STANDARD` | `-1.23%` | `0x0efb38a5fa` |
| `BUY` | `8.72` | `1651.9400` | 14,399.63 USD | 4,942,687.09 USD | `STANDARD` | `-1.26%` | `0xd3943e4008` |
| `BUY` | `8.72` | `385.3700` | 3,359.54 USD | 5,577,084.33 USD | `STANDARD` | `-1.24%` | `0x14f8e04290` |
| `BUY` | `8.73` | `82.9200` | 723.54 USD | 5,849,253.95 USD | `STANDARD` | `-1.15%` | `0x010461c14e` |
| `BUY` | `8.74` | `12510.5500` | 109,287.16 USD | 3,676,836.51 USD | `LARGE (>= USD 100K)` | `-1.04%` | `0xecb63caa47` |
| `BUY` | `8.74` | `3656.0300` | 31,946.76 USD | 4,241,038.16 USD | `MEDIUM (>= USD 25K)` | `-1.01%` | `0xa38f19c4cc` |
| `BUY` | `8.74` | `1414.0600` | 12,358.18 USD | 4,968,255.39 USD | `STANDARD` | `-1.00%` | `0xd3943e4008` |
| `BUY` | `8.74` | `1371.6600` | 11,988.03 USD | 5,064,730.21 USD | `STANDARD` | `-0.99%` | `0x33ad48ed92` |
| `BUY` | `8.74` | `625.4400` | 5,469.16 USD | 5,417,036.67 USD | `STANDARD` | `-0.94%` | `0xd2ccf2ebc5` |
| `BUY` | `8.74` | `568.9000` | 4,974.35 USD | 5,442,035.32 USD | `STANDARD` | `-0.95%` | `0x3ca146d269` |
| `BUY` | `8.74` | `227.5000` | 1,989.26 USD | 5,731,114.91 USD | `STANDARD` | `-0.95%` | `0x39bac00809` |
| `BUY` | `8.74` | `131.2700` | 1,147.38 USD | 5,834,030.21 USD | `STANDARD` | `-0.99%` | `0xe34d21d198` |
| `BUY` | `8.74` | `74.4900` | 651.12 USD | 5,854,710.22 USD | `STANDARD` | `-0.98%` | `0x31ca8395cf` |
| `BUY` | `8.75` | `384.3800` | 3,364.94 USD | 5,573,724.79 USD | `STANDARD` | `-0.83%` | `0x14f8e04290` |
| `BUY` | `8.76` | `11429.8400` | 100,125.40 USD | 4,079,650.87 USD | `LARGE (>= USD 100K)` | `-0.77%` | `0x881cd92459` |
| `BUY` | `8.76` | `1369.7200` | 11,999.98 USD | 5,028,742.41 USD | `STANDARD` | `-0.76%` | `0x0efb38a5fa` |
| `BUY` | `8.76` | `1250.0000` | 10,950.00 USD | 5,120,256.59 USD | `STANDARD` | `-0.77%` | `0xb7bd9cef0e` |
| `BUY` | `8.76` | `131.2700` | 1,150.44 USD | 5,832,882.83 USD | `STANDARD` | `-0.72%` | `0xe34d21d198` |
| `BUY` | `8.77` | `26550.8200` | 232,792.28 USD | 1,386,194.44 USD | `LARGE (>= USD 100K)` | `-0.68%` | `0x71cfa5e263` |
| `BUY` | `8.77` | `17504.9900` | 153,496.01 USD | 2,009,747.36 USD | `LARGE (>= USD 100K)` | `-0.67%` | `0x71d0e11ebb` |
| `BUY` | `8.77` | `2143.2000` | 18,792.22 USD | 4,403,632.68 USD | `STANDARD` | `-0.67%` | `0xa38f19c4cc` |
| `BUY` | `8.77` | `1184.9700` | 10,386.97 USD | 5,130,643.56 USD | `STANDARD` | `-0.70%` | `0xd3943e4008` |
| `BUY` | `8.77` | `1009.2100` | 8,848.96 USD | 5,286,228.04 USD | `STANDARD` | `-0.67%` | `0x33ad48ed92` |
| `BUY` | `8.77` | `511.0900` | 4,483.08 USD | 5,469,881.52 USD | `STANDARD` | `-0.63%` | `0xcd7f60e943` |
| `BUY` | `8.77` | `231.2300` | 2,028.63 USD | 5,723,092.94 USD | `STANDARD` | `-0.62%` | `0x9d732bed51` |
| `BUY` | `8.77` | `231.2300` | 2,027.59 USD | 5,725,120.53 USD | `STANDARD` | `-0.67%` | `0x9d732bed51` |
| `BUY` | `8.78` | `1661.8400` | 14,594.28 USD | 4,899,113.69 USD | `STANDARD` | `-0.52%` | `0x57d8e75f47` |
| `BUY` | `8.78` | `1661.8400` | 14,590.12 USD | 4,913,703.82 USD | `STANDARD` | `-0.54%` | `0x57d8e75f47` |
| `BUY` | `8.78` | `1661.8400` | 14,583.64 USD | 4,928,287.46 USD | `STANDARD` | `-0.59%` | `0x57d8e75f47` |
| `BUY` | `8.78` | `910.8900` | 7,999.98 USD | 5,310,470.80 USD | `STANDARD` | `-0.51%` | `0x0efb38a5fa` |
| `BUY` | `8.78` | `830.0000` | 7,287.65 USD | 5,348,891.35 USD | `STANDARD` | `-0.54%` | `0xb7bd9cef0e` |
| `BUY` | `8.78` | `231.2300` | 2,030.75 USD | 5,719,034.58 USD | `STANDARD` | `-0.51%` | `0x9d732bed51` |
| `BUY` | `8.78` | `231.2300` | 2,029.74 USD | 5,721,064.31 USD | `STANDARD` | `-0.56%` | `0x9d732bed51` |
| `BUY` | `8.78` | `84.7500` | 744.28 USD | 5,845,602.53 USD | `STANDARD` | `-0.52%` | `0x010461c14e` |
| `BUY` | `8.78` | `73.4100` | 644.77 USD | 5,855,354.99 USD | `STANDARD` | `-0.50%` | `0x31ca8395cf` |
| `BUY` | `8.79` | `14810.4500` | 130,169.05 USD | 2,871,335.48 USD | `LARGE (>= USD 100K)` | `-0.44%` | `0x71d0e11ebb` |
| `BUY` | `8.79` | `1661.8400` | 14,611.89 USD | 4,855,311.91 USD | `STANDARD` | `-0.40%` | `0x57d8e75f47` |
| `BUY` | `8.79` | `1661.8400` | 14,606.08 USD | 4,869,917.99 USD | `STANDARD` | `-0.44%` | `0x57d8e75f47` |
| `BUY` | `8.79` | `1661.8400` | 14,601.42 USD | 4,884,519.41 USD | `STANDARD` | `-0.47%` | `0x57d8e75f47` |
| `BUY` | `8.79` | `1257.9500` | 11,054.24 USD | 5,098,252.39 USD | `STANDARD` | `-0.45%` | `0xa38f19c4cc` |
| `BUY` | `8.79` | `1090.3000` | 9,586.79 USD | 5,250,253.47 USD | `STANDARD` | `-0.39%` | `0xd3342d3b1e` |
| `BUY` | `8.79` | `1041.2800` | 9,149.83 USD | 5,259,403.30 USD | `STANDARD` | `-0.46%` | `0xd3943e4008` |
| `BUY` | `8.79` | `767.9700` | 6,746.92 USD | 5,362,385.19 USD | `STANDARD` | `-0.48%` | `0x47a4471457` |
| `BUY` | `8.79` | `684.5500` | 6,019.59 USD | 5,387,875.51 USD | `STANDARD` | `-0.39%` | `0x33ad48ed92` |
| `BUY` | `8.79` | `514.8800` | 4,528.32 USD | 5,465,398.45 USD | `STANDARD` | `-0.37%` | `0xecb63caa47` |
| `BUY` | `8.79` | `231.2300` | 2,032.97 USD | 5,714,972.03 USD | `STANDARD` | `-0.40%` | `0x9d732bed51` |
| `BUY` | `8.79` | `231.2300` | 2,031.79 USD | 5,717,003.82 USD | `STANDARD` | `-0.46%` | `0x9d732bed51` |
| `BUY` | `8.79` | `131.2700` | 1,153.21 USD | 5,831,732.40 USD | `STANDARD` | `-0.48%` | `0xe34d21d198` |
| `BUY` | `8.80` | `3622.6600` | 31,897.16 USD | 4,304,832.98 USD | `MEDIUM (>= USD 25K)` | `-0.26%` | `0x08a49e7f71` |
| `BUY` | `8.80` | `1661.8400` | 14,630.01 USD | 4,796,837.24 USD | `STANDARD` | `-0.27%` | `0x57d8e75f47` |
| `BUY` | `8.80` | `1661.8400` | 14,625.36 USD | 4,811,462.60 USD | `STANDARD` | `-0.30%` | `0x57d8e75f47` |
| `BUY` | `8.80` | `1661.8400` | 14,620.87 USD | 4,826,083.47 USD | `STANDARD` | `-0.34%` | `0x57d8e75f47` |
| `BUY` | `8.80` | `1661.8400` | 14,616.55 USD | 4,840,700.02 USD | `STANDARD` | `-0.36%` | `0x57d8e75f47` |
| `BUY` | `8.80` | `936.6900` | 8,242.40 USD | 5,294,470.44 USD | `STANDARD` | `-0.32%` | `0xd3943e4008` |
| `BUY` | `8.80` | `738.8200` | 6,502.43 USD | 5,375,390.12 USD | `STANDARD` | `-0.30%` | `0xa38f19c4cc` |
| `BUY` | `8.80` | `567.8800` | 4,999.96 USD | 5,432,063.30 USD | `STANDARD` | `-0.26%` | `0x0efb38a5fa` |
| `BUY` | `8.80` | `568.0400` | 4,997.67 USD | 5,437,060.97 USD | `STANDARD` | `-0.33%` | `0xecb63caa47` |
| `BUY` | `8.80` | `563.6200` | 4,959.97 USD | 5,446,995.28 USD | `STANDARD` | `-0.31%` | `0xecb63caa47` |
| `BUY` | `8.80` | `474.9000` | 4,180.26 USD | 5,491,095.83 USD | `STANDARD` | `-0.29%` | `0x6fb997fb18` |
| `BUY` | `8.80` | `446.9800` | 3,934.45 USD | 5,526,828.19 USD | `STANDARD` | `-0.29%` | `0x2a72b57dea` |
| `BUY` | `8.80` | `446.9800` | 3,931.46 USD | 5,530,759.64 USD | `STANDARD` | `-0.36%` | `0x2a72b57dea` |
| `BUY` | `8.80` | `420.0000` | 3,696.76 USD | 5,549,708.89 USD | `STANDARD` | `-0.29%` | `0xb7bd9cef0e` |
| `BUY` | `8.80` | `366.8200` | 3,229.67 USD | 5,596,514.02 USD | `STANDARD` | `-0.26%` | `0xdd4f66125d` |
| `BUY` | `8.80` | `231.2300` | 2,034.92 USD | 5,710,905.15 USD | `STANDARD` | `-0.31%` | `0x9d732bed51` |
| `BUY` | `8.80` | `231.2300` | 2,033.90 USD | 5,712,939.05 USD | `STANDARD` | `-0.36%` | `0x9d732bed51` |
| `BUY` | `8.80` | `87.0400` | 766.19 USD | 5,843,343.93 USD | `STANDARD` | `-0.28%` | `0x010461c14e` |
| `BUY` | `8.80` | `79.3000` | 698.05 USD | 5,852,058.33 USD | `STANDARD` | `-0.28%` | `0x31ca8395cf` |
| `BUY` | `8.81` | `16742.6600` | 147,499.49 USD | 2,609,719.43 USD | `LARGE (>= USD 100K)` | `-0.20%` | `0x71d0e11ebb` |
| `BUY` | `8.81` | `1661.8400` | 14,647.13 USD | 4,738,292.12 USD | `STANDARD` | `-0.16%` | `0x57d8e75f47` |
| `BUY` | `8.81` | `1661.8400` | 14,642.64 USD | 4,752,934.76 USD | `STANDARD` | `-0.19%` | `0x57d8e75f47` |
| `BUY` | `8.81` | `1661.8400` | 14,638.32 USD | 4,767,573.07 USD | `STANDARD` | `-0.22%` | `0x57d8e75f47` |
| `BUY` | `8.81` | `1661.8400` | 14,634.16 USD | 4,782,207.24 USD | `STANDARD` | `-0.24%` | `0x57d8e75f47` |
| `BUY` | `8.81` | `1137.9700` | 10,028.47 USD | 5,201,008.23 USD | `STANDARD` | `-0.17%` | `0xaf9f722a67` |
| `BUY` | `8.81` | `646.3800` | 5,692.15 USD | 5,411,567.51 USD | `STANDARD` | `-0.24%` | `0xecb63caa47` |
| `BUY` | `8.81` | `481.6400` | 4,243.34 USD | 5,486,915.57 USD | `STANDARD` | `-0.20%` | `0x7717a7a245` |
| `BUY` | `8.81` | `446.9800` | 3,937.49 USD | 5,522,893.74 USD | `STANDARD` | `-0.21%` | `0x2a72b57dea` |
| `BUY` | `8.81` | `440.8600` | 3,885.65 USD | 5,534,645.30 USD | `STANDARD` | `-0.16%` | `0xecb63caa47` |
| `BUY` | `8.81` | `434.3500` | 3,824.97 USD | 5,538,470.27 USD | `STANDARD` | `-0.24%` | `0xa38f19c4cc` |
| `BUY` | `8.81` | `366.8200` | 3,232.97 USD | 5,590,054.02 USD | `STANDARD` | `-0.16%` | `0xdd4f66125d` |
| `BUY` | `8.81` | `366.8200` | 3,230.33 USD | 5,593,284.35 USD | `STANDARD` | `-0.24%` | `0xdd4f66125d` |
| `BUY` | `8.81` | `350.0300` | 3,083.48 USD | 5,599,597.50 USD | `STANDARD` | `-0.21%` | `0xecb63caa47` |
| `BUY` | `8.81` | `319.8500` | 2,818.84 USD | 5,622,392.55 USD | `STANDARD` | `-0.17%` | `0x6ba889db7f` |
| `BUY` | `8.81` | `319.8500` | 2,818.04 USD | 5,625,210.59 USD | `STANDARD` | `-0.19%` | `0x6ba889db7f` |
| `BUY` | `8.81` | `269.1200` | 2,371.11 USD | 5,670,825.48 USD | `STANDARD` | `-0.19%` | `0x33ad48ed92` |
| `BUY` | `8.81` | `255.3000` | 2,249.98 USD | 5,675,440.98 USD | `STANDARD` | `-0.16%` | `0xa38f19c4cc` |
| `BUY` | `8.81` | `231.2300` | 2,037.04 USD | 5,706,834.21 USD | `STANDARD` | `-0.20%` | `0x9d732bed51` |
| `BUY` | `8.81` | `231.2300` | 2,036.03 USD | 5,708,870.24 USD | `STANDARD` | `-0.25%` | `0x9d732bed51` |
| `BUY` | `8.81` | `113.4500` | 999.93 USD | 5,840,148.17 USD | `STANDARD` | `-0.16%` | `0x27c9fa86c9` |
| `BUY` | `8.81` | `85.2800` | 751.46 USD | 5,844,858.24 USD | `STANDARD` | `-0.18%` | `0x010461c14e` |
| `BUY` | `8.81` | `82.2600` | 725.01 USD | 5,848,530.41 USD | `STANDARD` | `-0.16%` | `0x31ca8395cf` |
| `BUY` | `8.81` | `57.3100` | 505.18 USD | 5,863,006.48 USD | `STANDARD` | `-0.14%` | `0x57d8e75f47` |
| `BUY` | `8.81` | `57.3100` | 504.78 USD | 5,863,511.25 USD | `STANDARD` | `-0.22%` | `0x57d8e75f47` |
| `BID` | `8.82` | `104.1500` | 919.10 USD | 13,596.09 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.82` | `1026.5900` | 9,059.35 USD | 22,655.43 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.82` | `63.4600` | 559.99 USD | 23,215.42 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.82` | `79.8000` | 704.17 USD | 23,919.60 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `8.82` | `54.1700` | 478.00 USD | 24,397.60 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.82` | `54.1500` | 477.81 USD | 24,875.41 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.82` | `37.0200` | 326.65 USD | 25,202.06 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.82` | `1773.3000` | 15,646.54 USD | 40,848.60 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `8.82` | `1453.9900` | 12,828.41 USD | 53,677.01 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.82` | `40.7600` | 359.62 USD | 54,036.62 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.82` | `5.3000` | 46.76 USD | 54,083.38 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.82` | `167.5000` | 1,477.70 USD | 55,561.08 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `8.82` | `54.1500` | 477.71 USD | 56,038.80 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.82` | `54.1500` | 477.70 USD | 56,516.50 USD | `1 orders` | `-0.07%` | `-` |
| `BUY` | `8.82` | `1661.8400` | 14,663.08 USD | 4,694,335.12 USD | `STANDARD` | `-0.05%` | `0x57d8e75f47` |
| `BUY` | `8.82` | `1661.8400` | 14,657.10 USD | 4,708,992.22 USD | `STANDARD` | `-0.09%` | `0x57d8e75f47` |
| `BUY` | `8.82` | `1661.8400` | 14,652.78 USD | 4,723,644.99 USD | `STANDARD` | `-0.12%` | `0x57d8e75f47` |
| `BUY` | `8.82` | `1383.6200` | 12,198.13 USD | 4,992,651.82 USD | `STANDARD` | `-0.13%` | `0x08a49e7f71` |
| `BUY` | `8.82` | `1360.3700` | 11,999.82 USD | 5,052,742.17 USD | `STANDARD` | `-0.07%` | `0x7d0c59691f` |
| `BUY` | `8.82` | `1137.9700` | 10,038.49 USD | 5,180,945.48 USD | `STANDARD` | `-0.07%` | `0xaf9f722a67` |
| `BUY` | `8.82` | `1137.9700` | 10,034.28 USD | 5,190,979.75 USD | `STANDARD` | `-0.11%` | `0x621c555167` |
| `BUY` | `8.82` | `1133.3800` | 9,999.70 USD | 5,221,007.98 USD | `STANDARD` | `-0.05%` | `0x7d0c59691f` |
| `BUY` | `8.82` | `906.5100` | 7,999.68 USD | 5,326,470.41 USD | `STANDARD` | `-0.03%` | `0x7d0c59691f` |
| `BUY` | `8.82` | `482.7200` | 4,257.45 USD | 5,482,672.22 USD | `STANDARD` | `-0.09%` | `0x71d0e11ebb` |
| `BUY` | `8.82` | `446.9800` | 3,940.62 USD | 5,518,956.24 USD | `STANDARD` | `-0.13%` | `0x2a72b57dea` |
| `BUY` | `8.82` | `320.6100` | 2,828.71 USD | 5,613,921.97 USD | `STANDARD` | `-0.05%` | `0x6ba889db7f` |
| `BUY` | `8.82` | `319.5000` | 2,816.55 USD | 5,628,027.14 USD | `STANDARD` | `-0.14%` | `0x6ba889db7f` |
| `BUY` | `8.82` | `315.3000` | 2,780.35 USD | 5,644,816.12 USD | `STANDARD` | `-0.11%` | `0x6ba889db7f` |
| `BUY` | `8.82` | `312.0500` | 2,751.06 USD | 5,650,325.58 USD | `STANDARD` | `-0.13%` | `0x7717a7a245` |
| `BUY` | `8.82` | `288.6300` | 2,544.36 USD | 5,660,957.26 USD | `STANDARD` | `-0.14%` | `0xecb63caa47` |
| `BUY` | `8.82` | `283.5300` | 2,499.97 USD | 5,663,457.23 USD | `STANDARD` | `-0.12%` | `0x0efb38a5fa` |
| `BUY` | `8.82` | `250.1000` | 2,204.96 USD | 5,682,108.14 USD | `STANDARD` | `-0.13%` | `0xecb63caa47` |
| `BUY` | `8.82` | `207.1500` | 1,827.37 USD | 5,734,830.21 USD | `STANDARD` | `-0.07%` | `0x023a3d0580` |
| `BUY` | `8.82` | `200.0000` | 1,763.82 USD | 5,805,265.46 USD | `STANDARD` | `-0.10%` | `0xfc27136e42` |
| `BUY` | `8.82` | `200.0000` | 1,763.64 USD | 5,807,029.10 USD | `STANDARD` | `-0.11%` | `0xfc27136e42` |
| `BUY` | `8.82` | `200.0000` | 1,763.46 USD | 5,808,792.56 USD | `STANDARD` | `-0.12%` | `0xfc27136e42` |
| `BUY` | `8.82` | `137.5600` | 1,213.22 USD | 5,823,463.84 USD | `STANDARD` | `-0.09%` | `0xdd4f66125d` |
| `BUY` | `8.82` | `137.5600` | 1,213.11 USD | 5,824,676.96 USD | `STANDARD` | `-0.10%` | `0xdd4f66125d` |
| `BUY` | `8.82` | `137.5600` | 1,213.09 USD | 5,825,890.04 USD | `STANDARD` | `-0.10%` | `0xdd4f66125d` |
| `BUY` | `8.82` | `113.3500` | 999.99 USD | 5,837,148.38 USD | `STANDARD` | `-0.06%` | `0x0eecd62efb` |
| `BUY` | `8.82` | `83.8800` | 739.81 USD | 5,846,342.34 USD | `STANDARD` | `-0.09%` | `0x010461c14e` |
| `BUY` | `8.82` | `80.1700` | 707.11 USD | 5,849,961.06 USD | `STANDARD` | `-0.08%` | `0x31ca8395cf` |
| `BUY` | `8.82` | `67.2800` | 593.22 USD | 5,857,833.24 USD | `STANDARD` | `-0.12%` | `0x33ad48ed92` |
| `BUY` | `8.82` | `63.4600` | 559.99 USD | 5,858,957.08 USD | `STANDARD` | `-0.04%` | `0x023a3d0580` |
| `BUY` | `8.82` | `57.3100` | 505.67 USD | 5,861,995.83 USD | `STANDARD` | `-0.05%` | `0x57d8e75f47` |
| `BUY` | `8.82` | `57.3100` | 505.46 USD | 5,862,501.30 USD | `STANDARD` | `-0.09%` | `0x57d8e75f47` |
| `ASK` | `8.83` | `40.6200` | 358.78 USD | 35,703.50 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.83` | `153.8200` | 1,358.63 USD | 35,344.72 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.83` | `113.2100` | 999.93 USD | 33,986.08 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.83` | `91.7000` | 809.89 USD | 32,986.16 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.83` | `91.7000` | 809.89 USD | 32,176.26 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.83` | `679.3600` | 5,999.97 USD | 31,366.38 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.83` | `54.3500` | 480.00 USD | 25,366.41 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.83` | `1781.9200` | 15,737.20 USD | 24,886.40 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.83` | `208.1400` | 1,838.19 USD | 9,149.20 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `8.83` | `91.7000` | 809.79 USD | 7,311.01 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.83` | `5.8000` | 51.22 USD | 6,501.22 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.83` | `191.9200` | 1,694.77 USD | 6,450.00 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `8.83` | `50.0000` | 441.53 USD | 4,755.23 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.83` | `57.3100` | 506.07 USD | 4,313.70 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.83` | `54.3600` | 479.99 USD | 3,807.63 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.83` | `54.3500` | 479.89 USD | 3,327.64 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.83` | `54.1500` | 478.10 USD | 2,847.75 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.83` | `44.0300` | 388.74 USD | 2,369.65 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `8.83` | `149.2200` | 1,317.45 USD | 1,980.91 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.83` | `75.1500` | 663.46 USD | 663.46 USD | `2 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `8.83` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.83` | `0.00%` | `-` |
| `BID` | `8.83` | `320.6100` | 2,829.93 USD | 2,829.93 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.83` | `679.7800` | 5,999.74 USD | 8,829.67 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.83` | `141.8500` | 1,251.95 USD | 10,081.62 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.83` | `119.8400` | 1,057.68 USD | 11,139.30 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.83` | `120.0800` | 1,059.78 USD | 12,199.08 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.83` | `54.1500` | 477.90 USD | 12,676.98 USD | `1 orders` | `-0.02%` | `-` |
| `SELL` | `8.83` | `1661.8400` | 14,680.86 USD | 4,664,995.33 USD | `STANDARD` | `+0.07%` | `0x57d8e75f47` |
| `SELL` | `8.83` | `1661.8400` | 14,676.71 USD | 4,679,672.04 USD | `STANDARD` | `+0.05%` | `0x57d8e75f47` |
| `SELL` | `8.83` | `679.3600` | 5,999.97 USD | 5,399,875.62 USD | `STANDARD` | `+0.05%` | `0x7d0c59691f` |
| `BUY` | `8.83` | `679.7800` | 5,999.74 USD | 5,405,875.36 USD | `STANDARD` | `-0.02%` | `0x7d0c59691f` |
| `SELL` | `8.83` | `446.9800` | 3,948.53 USD | 5,515,015.62 USD | `STANDARD` | `+0.07%` | `0x2a72b57dea` |
| `BUY` | `8.83` | `320.6100` | 2,829.93 USD | 5,611,093.26 USD | `STANDARD` | `-0.01%` | `0x6ba889db7f` |
| `SELL` | `8.83` | `320.0700` | 2,827.37 USD | 5,616,749.34 USD | `STANDARD` | `+0.07%` | `0x6ba889db7f` |
| `SELL` | `8.83` | `282.9700` | 2,499.93 USD | 5,665,957.15 USD | `STANDARD` | `+0.08%` | `0x0efb38a5fa` |
| `SELL` | `8.83` | `200.0000` | 1,766.70 USD | 5,803,501.64 USD | `STANDARD` | `+0.07%` | `0xfc27136e42` |
| `SELL` | `8.83` | `149.2200` | 1,317.45 USD | 5,818,545.39 USD | `STANDARD` | `+0.01%` | `0x727956612a` |
| `BUY` | `8.83` | `141.8500` | 1,251.95 USD | 5,819,797.35 USD | `STANDARD` | `-0.02%` | `0x727956612a` |
| `SELL` | `8.83` | `140.2200` | 1,238.54 USD | 5,821,035.88 USD | `STANDARD` | `+0.06%` | `0xecb63caa47` |
| `SELL` | `8.83` | `137.5600` | 1,214.74 USD | 5,822,250.62 USD | `STANDARD` | `+0.03%` | `0xdd4f66125d` |
| `SELL` | `8.83` | `120.0800` | 1,060.50 USD | 5,835,090.71 USD | `STANDARD` | `+0.05%` | `0x7717a7a245` |
| `BUY` | `8.83` | `119.8400` | 1,057.68 USD | 5,836,148.40 USD | `STANDARD` | `-0.02%` | `0xecb63caa47` |
| `SELL` | `8.83` | `113.2100` | 999.94 USD | 5,838,148.32 USD | `STANDARD` | `+0.06%` | `0x0eecd62efb` |
| `SELL` | `8.83` | `113.2100` | 999.93 USD | 5,839,148.25 USD | `STANDARD` | `+0.06%` | `0x27c9fa86c9` |
| `SELL` | `8.83` | `91.7000` | 809.89 USD | 5,840,958.07 USD | `STANDARD` | `+0.05%` | `0xdd4f66125d` |
| `SELL` | `8.83` | `91.7000` | 809.89 USD | 5,841,767.95 USD | `STANDARD` | `+0.05%` | `0xdd4f66125d` |
| `SELL` | `8.83` | `91.7000` | 809.79 USD | 5,842,577.75 USD | `STANDARD` | `+0.04%` | `0xdd4f66125d` |
| `SELL` | `8.83` | `79.0900` | 698.48 USD | 5,851,360.27 USD | `STANDARD` | `+0.04%` | `0x31ca8395cf` |
| `SELL` | `8.83` | `74.9000` | 661.48 USD | 5,854,059.09 USD | `STANDARD` | `+0.04%` | `0x010461c14e` |
| `SELL` | `8.83` | `57.3100` | 506.28 USD | 5,860,984.09 USD | `STANDARD` | `+0.07%` | `0x57d8e75f47` |
| `SELL` | `8.83` | `57.3100` | 506.07 USD | 5,861,490.16 USD | `STANDARD` | `+0.03%` | `0x57d8e75f47` |
| `SELL` | `8.84` | `1661.8400` | 14,698.64 USD | 4,620,935.47 USD | `STANDARD` | `+0.19%` | `0x57d8e75f47` |
| `SELL` | `8.84` | `1661.8400` | 14,691.83 USD | 4,635,627.30 USD | `STANDARD` | `+0.15%` | `0x57d8e75f47` |
| `SELL` | `8.84` | `1661.8400` | 14,687.18 USD | 4,650,314.47 USD | `STANDARD` | `+0.12%` | `0x57d8e75f47` |
| `SELL` | `8.84` | `1380.3200` | 12,198.30 USD | 4,980,453.69 USD | `STANDARD` | `+0.11%` | `0x08a49e7f71` |
| `SELL` | `8.84` | `1357.8500` | 12,002.31 USD | 5,016,742.43 USD | `STANDARD` | `+0.13%` | `0x7d0c59691f` |
| `SELL` | `8.84` | `1137.9700` | 10,058.52 USD | 5,160,849.15 USD | `STANDARD` | `+0.13%` | `0xaf9f722a67` |
| `SELL` | `8.84` | `1137.9700` | 10,057.83 USD | 5,170,906.99 USD | `STANDARD` | `+0.12%` | `0x621c555167` |
| `SELL` | `8.84` | `1131.5600` | 10,000.05 USD | 5,211,008.28 USD | `STANDARD` | `+0.11%` | `0x7d0c59691f` |
| `SELL` | `8.84` | `905.4700` | 8,000.37 USD | 5,302,470.82 USD | `STANDARD` | `+0.09%` | `0x7d0c59691f` |
| `SELL` | `8.84` | `735.3100` | 6,502.49 USD | 5,368,887.69 USD | `STANDARD` | `+0.18%` | `0xa38f19c4cc` |
| `SELL` | `8.84` | `481.6400` | 4,259.96 USD | 5,478,414.78 USD | `STANDARD` | `+0.19%` | `0x7717a7a245` |
| `SELL` | `8.84` | `446.9800` | 3,951.39 USD | 5,511,067.09 USD | `STANDARD` | `+0.14%` | `0x2a72b57dea` |
| `SELL` | `8.84` | `366.8200` | 3,243.09 USD | 5,586,821.05 USD | `STANDARD` | `+0.15%` | `0xdd4f66125d` |
| `SELL` | `8.84` | `319.5900` | 2,824.38 USD | 5,619,573.71 USD | `STANDARD` | `+0.11%` | `0x6ba889db7f` |
| `SELL` | `8.84` | `316.6700` | 2,800.85 USD | 5,636,453.02 USD | `STANDARD` | `+0.19%` | `0x6ba889db7f` |
| `SELL` | `8.84` | `315.3000` | 2,787.91 USD | 5,642,035.77 USD | `STANDARD` | `+0.16%` | `0x6ba889db7f` |
| `SELL` | `8.84` | `312.0500` | 2,758.40 USD | 5,647,574.52 USD | `STANDARD` | `+0.14%` | `0x7717a7a245` |
| `SELL` | `8.84` | `302.3000` | 2,673.21 USD | 5,658,412.90 USD | `STANDARD` | `+0.17%` | `0xecb63caa47` |
| `SELL` | `8.84` | `267.4800` | 2,365.51 USD | 5,673,190.99 USD | `STANDARD` | `+0.18%` | `0x33ad48ed92` |
| `SELL` | `8.84` | `254.5200` | 2,249.93 USD | 5,677,690.91 USD | `STANDARD` | `+0.14%` | `0xa38f19c4cc` |
| `SELL` | `8.84` | `250.2400` | 2,212.27 USD | 5,679,903.18 USD | `STANDARD` | `+0.15%` | `0xecb63caa47` |
| `SELL` | `8.84` | `231.2300` | 2,044.24 USD | 5,704,797.17 USD | `STANDARD` | `+0.15%` | `0x9d732bed51` |
| `SELL` | `8.84` | `213.6800` | 1,887.93 USD | 5,733,002.83 USD | `STANDARD` | `+0.09%` | `0xe86b057f5e` |
| `SELL` | `8.84` | `82.7500` | 731.25 USD | 5,847,805.40 USD | `STANDARD` | `+0.10%` | `0x010461c14e` |
| `SELL` | `8.84` | `76.4400` | 675.61 USD | 5,852,733.94 USD | `STANDARD` | `+0.12%` | `0x31ca8395cf` |
| `SELL` | `8.84` | `67.7200` | 598.46 USD | 5,857,240.02 USD | `STANDARD` | `+0.11%` | `0x33ad48ed92` |
| `SELL` | `8.84` | `63.8200` | 563.85 USD | 5,858,397.09 USD | `STANDARD` | `+0.08%` | `0x023a3d0580` |
| `SELL` | `8.84` | `57.3100` | 506.55 USD | 5,860,477.82 USD | `STANDARD` | `+0.13%` | `0x57d8e75f47` |
| `SELL` | `8.85` | `16737.0400` | 148,114.44 USD | 2,462,219.94 USD | `LARGE (>= USD 100K)` | `+0.25%` | `0x71d0e11ebb` |
| `SELL` | `8.85` | `3603.9300` | 31,897.66 USD | 4,272,935.82 USD | `MEDIUM (>= USD 25K)` | `+0.26%` | `0x08a49e7f71` |
| `SELL` | `8.85` | `1661.8400` | 14,712.93 USD | 4,576,823.75 USD | `STANDARD` | `+0.29%` | `0x57d8e75f47` |
| `SELL` | `8.85` | `1661.8400` | 14,708.78 USD | 4,591,532.53 USD | `STANDARD` | `+0.26%` | `0x57d8e75f47` |
| `SELL` | `8.85` | `1661.8400` | 14,704.29 USD | 4,606,236.83 USD | `STANDARD` | `+0.23%` | `0x57d8e75f47` |
| `SELL` | `8.85` | `1248.6100` | 11,054.19 USD | 5,109,306.59 USD | `STANDARD` | `+0.29%` | `0xa38f19c4cc` |
| `SELL` | `8.85` | `1137.9700` | 10,068.53 USD | 5,150,790.64 USD | `STANDARD` | `+0.23%` | `0xaf9f722a67` |
| `SELL` | `8.85` | `730.5500` | 6,465.81 USD | 5,381,855.92 USD | `STANDARD` | `+0.26%` | `0xecb63caa47` |
| `SELL` | `8.85` | `564.9700` | 4,999.98 USD | 5,427,063.34 USD | `STANDARD` | `+0.25%` | `0x0efb38a5fa` |
| `SELL` | `8.85` | `482.9400` | 4,273.29 USD | 5,474,154.82 USD | `STANDARD` | `+0.24%` | `0x71d0e11ebb` |
| `SELL` | `8.85` | `446.9800` | 3,957.20 USD | 5,503,161.45 USD | `STANDARD` | `+0.29%` | `0x2a72b57dea` |
| `SELL` | `8.85` | `446.9800` | 3,954.25 USD | 5,507,115.70 USD | `STANDARD` | `+0.22%` | `0x2a72b57dea` |
| `SELL` | `8.85` | `432.3000` | 3,824.95 USD | 5,542,295.22 USD | `STANDARD` | `+0.23%` | `0xa38f19c4cc` |
| `SELL` | `8.85` | `420.0000` | 3,716.92 USD | 5,546,012.13 USD | `STANDARD` | `+0.25%` | `0xb7bd9cef0e` |
| `SELL` | `8.85` | `366.8200` | 3,248.08 USD | 5,580,332.41 USD | `STANDARD` | `+0.31%` | `0xdd4f66125d` |
| `SELL` | `8.85` | `366.8200` | 3,245.55 USD | 5,583,577.96 USD | `STANDARD` | `+0.23%` | `0xdd4f66125d` |
| `SELL` | `8.85` | `320.6200` | 2,838.06 USD | 5,605,432.18 USD | `STANDARD` | `+0.27%` | `0x6ba889db7f` |
| `SELL` | `8.85` | `317.8400` | 2,812.18 USD | 5,633,652.17 USD | `STANDARD` | `+0.23%` | `0x6ba889db7f` |
| `SELL` | `8.85` | `315.7300` | 2,794.84 USD | 5,639,247.86 USD | `STANDARD` | `+0.28%` | `0x07fd993f0f` |
| `SELL` | `8.85` | `302.2300` | 2,673.25 USD | 5,655,739.69 USD | `STANDARD` | `+0.20%` | `0xecb63caa47` |
| `SELL` | `8.85` | `248.7000` | 2,200.87 USD | 5,684,309.01 USD | `STANDARD` | `+0.25%` | `0xecb63caa47` |
| `SELL` | `8.85` | `231.2300` | 2,047.31 USD | 5,698,661.55 USD | `STANDARD` | `+0.30%` | `0x9d732bed51` |
| `SELL` | `8.85` | `231.2300` | 2,046.13 USD | 5,700,707.68 USD | `STANDARD` | `+0.24%` | `0x9d732bed51` |
| `SELL` | `8.85` | `231.2300` | 2,045.25 USD | 5,702,752.93 USD | `STANDARD` | `+0.20%` | `0x9d732bed51` |
| `SELL` | `8.85` | `202.8700` | 1,794.69 USD | 5,798,147.39 USD | `STANDARD` | `+0.21%` | `0x26934acbd3` |
| `SELL` | `8.85` | `202.6500` | 1,794.22 USD | 5,799,941.61 USD | `STANDARD` | `+0.30%` | `0xc3a5b2551d` |
| `SELL` | `8.85` | `202.6500` | 1,793.33 USD | 5,801,734.94 USD | `STANDARD` | `+0.25%` | `0xc3a5b2551d` |
| `SELL` | `8.85` | `197.4100` | 1,746.11 USD | 5,812,288.35 USD | `STANDARD` | `+0.20%` | `0xc3a5b2551d` |
| `SELL` | `8.85` | `86.2200` | 762.85 USD | 5,844,106.78 USD | `STANDARD` | `+0.23%` | `0x31ca8395cf` |
| `SELL` | `8.85` | `75.0100` | 663.67 USD | 5,853,397.61 USD | `STANDARD` | `+0.23%` | `0x010461c14e` |
| `SELL` | `8.85` | `57.3100` | 507.24 USD | 5,859,464.32 USD | `STANDARD` | `+0.26%` | `0x57d8e75f47` |
| `SELL` | `8.85` | `57.3100` | 506.95 USD | 5,859,971.27 USD | `STANDARD` | `+0.21%` | `0x57d8e75f47` |
| `SELL` | `8.86` | `1661.8400` | 14,725.40 USD | 4,547,393.73 USD | `STANDARD` | `+0.38%` | `0x57d8e75f47` |
| `SELL` | `8.86` | `1661.8400` | 14,717.09 USD | 4,562,110.82 USD | `STANDARD` | `+0.32%` | `0x57d8e75f47` |
| `SELL` | `8.86` | `1137.9700` | 10,078.55 USD | 5,140,722.11 USD | `STANDARD` | `+0.33%` | `0xaf9f722a67` |
| `SELL` | `8.86` | `1009.6600` | 8,949.42 USD | 5,277,379.09 USD | `STANDARD` | `+0.41%` | `0xd3943e4008` |
| `SELL` | `8.86` | `876.6300` | 7,768.78 USD | 5,334,239.19 USD | `STANDARD` | `+0.39%` | `0xecb63caa47` |
| `SELL` | `8.86` | `677.1700` | 6,000.13 USD | 5,393,875.65 USD | `STANDARD` | `+0.37%` | `0x33ad48ed92` |
| `SELL` | `8.86` | `567.5000` | 5,026.69 USD | 5,422,063.35 USD | `STANDARD` | `+0.34%` | `0x3ca146d269` |
| `SELL` | `8.86` | `468.4600` | 4,148.26 USD | 5,495,244.09 USD | `STANDARD` | `+0.31%` | `0xecb63caa47` |
| `SELL` | `8.86` | `446.9800` | 3,960.15 USD | 5,499,204.24 USD | `STANDARD` | `+0.36%` | `0x2a72b57dea` |
| `SELL` | `8.86` | `231.2300` | 2,049.35 USD | 5,694,565.91 USD | `STANDARD` | `+0.40%` | `0x9d732bed51` |
| `SELL` | `8.86` | `231.2300` | 2,048.33 USD | 5,696,614.24 USD | `STANDARD` | `+0.35%` | `0x9d732bed51` |
| `SELL` | `8.86` | `226.5000` | 2,007.38 USD | 5,727,127.91 USD | `STANDARD` | `+0.40%` | `0x39bac00809` |
| `SELL` | `8.86` | `202.6500` | 1,795.97 USD | 5,794,557.61 USD | `STANDARD` | `+0.39%` | `0xc3a5b2551d` |
| `SELL` | `8.86` | `202.6500` | 1,795.09 USD | 5,796,352.70 USD | `STANDARD` | `+0.35%` | `0xc3a5b2551d` |
| `SELL` | `8.86` | `131.2700` | 1,163.05 USD | 5,830,579.19 USD | `STANDARD` | `+0.37%` | `0xe34d21d198` |
| `SELL` | `8.87` | `14816.4400` | 131,447.01 USD | 2,741,166.44 USD | `LARGE (>= USD 100K)` | `+0.50%` | `0x71d0e11ebb` |
| `SELL` | `8.87` | `2118.9300` | 18,792.15 USD | 4,422,424.83 USD | `STANDARD` | `+0.47%` | `0xa38f19c4cc` |
| `SELL` | `8.87` | `1661.8400` | 14,742.02 USD | 4,517,934.63 USD | `STANDARD` | `+0.49%` | `0x57d8e75f47` |
| `SELL` | `8.87` | `1661.8400` | 14,733.71 USD | 4,532,668.33 USD | `STANDARD` | `+0.43%` | `0x57d8e75f47` |
| `SELL` | `8.87` | `1126.2500` | 9,992.54 USD | 5,231,000.52 USD | `STANDARD` | `+0.51%` | `0xd3943e4008` |
| `SELL` | `8.87` | `1090.3000` | 9,666.16 USD | 5,240,666.68 USD | `STANDARD` | `+0.43%` | `0xd3342d3b1e` |
| `SELL` | `8.87` | `901.9800` | 7,999.93 USD | 5,318,470.73 USD | `STANDARD` | `+0.47%` | `0x0efb38a5fa` |
| `SELL` | `8.87` | `830.0000` | 7,364.51 USD | 5,341,603.70 USD | `STANDARD` | `+0.51%` | `0xb7bd9cef0e` |
| `SELL` | `8.87` | `761.0400` | 6,746.92 USD | 5,355,638.27 USD | `STANDARD` | `+0.43%` | `0x47a4471457` |
| `SELL` | `8.87` | `530.9900` | 4,711.58 USD | 5,451,706.87 USD | `STANDARD` | `+0.52%` | `0x26934acbd3` |
| `SELL` | `8.87` | `522.3000` | 4,630.71 USD | 5,456,337.58 USD | `STANDARD` | `+0.43%` | `0xecb63caa47` |
| `SELL` | `8.87` | `511.0900` | 4,532.55 USD | 5,460,870.13 USD | `STANDARD` | `+0.46%` | `0xcd7f60e943` |
| `SELL` | `8.87` | `231.2300` | 2,051.33 USD | 5,690,466.27 USD | `STANDARD` | `+0.50%` | `0x9d732bed51` |
| `SELL` | `8.87` | `231.2300` | 2,050.29 USD | 5,692,516.56 USD | `STANDARD` | `+0.45%` | `0x9d732bed51` |
| `SELL` | `8.87` | `202.6500` | 1,797.71 USD | 5,790,964.81 USD | `STANDARD` | `+0.49%` | `0xc3a5b2551d` |
| `SELL` | `8.87` | `202.6500` | 1,796.84 USD | 5,792,761.64 USD | `STANDARD` | `+0.44%` | `0xc3a5b2551d` |
| `SELL` | `8.87` | `72.6200` | 644.44 USD | 5,855,999.44 USD | `STANDARD` | `+0.53%` | `0x31ca8395cf` |
| `SELL` | `8.88` | `1661.8400` | 14,750.33 USD | 4,503,192.61 USD | `STANDARD` | `+0.55%` | `0x57d8e75f47` |
| `SELL` | `8.88` | `1486.9900` | 13,210.12 USD | 4,955,897.21 USD | `STANDARD` | `+0.64%` | `0xd3943e4008` |
| `SELL` | `8.88` | `1277.6200` | 11,348.08 USD | 5,076,078.28 USD | `STANDARD` | `+0.62%` | `0xd3943e4008` |
| `SELL` | `8.88` | `393.5800` | 3,496.09 USD | 5,553,204.98 USD | `STANDARD` | `+0.63%` | `0xd2ccf2ebc5` |
| `SELL` | `8.88` | `337.3500` | 2,996.61 USD | 5,602,594.11 USD | `STANDARD` | `+0.63%` | `0xd2ccf2ebc5` |
| `SELL` | `8.88` | `281.1300` | 2,497.22 USD | 5,668,454.37 USD | `STANDARD` | `+0.63%` | `0xd2ccf2ebc5` |
| `SELL` | `8.88` | `231.2300` | 2,053.48 USD | 5,686,362.49 USD | `STANDARD` | `+0.60%` | `0x9d732bed51` |
| `SELL` | `8.88` | `231.2300` | 2,052.44 USD | 5,688,414.94 USD | `STANDARD` | `+0.55%` | `0x9d732bed51` |
| `SELL` | `8.88` | `224.9000` | 1,997.74 USD | 5,729,125.65 USD | `STANDARD` | `+0.63%` | `0xd2ccf2ebc5` |
| `SELL` | `8.88` | `202.6500` | 1,800.32 USD | 5,785,569.07 USD | `STANDARD` | `+0.64%` | `0xc3a5b2551d` |
| `SELL` | `8.88` | `202.6500` | 1,799.45 USD | 5,787,368.52 USD | `STANDARD` | `+0.59%` | `0xc3a5b2551d` |
| `SELL` | `8.88` | `202.6500` | 1,798.58 USD | 5,789,167.10 USD | `STANDARD` | `+0.54%` | `0xc3a5b2551d` |
| `SELL` | `8.88` | `131.2700` | 1,165.85 USD | 5,829,416.14 USD | `STANDARD` | `+0.61%` | `0xe34d21d198` |
| `SELL` | `8.88` | `78.9300` | 700.73 USD | 5,850,661.79 USD | `STANDARD` | `+0.57%` | `0x010461c14e` |
| `SELL` | `8.88` | `56.2800` | 500.03 USD | 5,864,011.28 USD | `STANDARD` | `+0.65%` | `0xf7840f07d8` |
| `SELL` | `8.89` | `26508.9900` | 235,606.60 USD | 1,153,402.16 USD | `LARGE (>= USD 100K)` | `+0.68%` | `0x71cfa5e263` |
| `SELL` | `8.89` | `3592.2300` | 31,946.78 USD | 4,209,091.40 USD | `MEDIUM (>= USD 25K)` | `+0.74%` | `0xa38f19c4cc` |
| `SELL` | `8.89` | `1015.7500` | 9,026.36 USD | 5,268,429.66 USD | `STANDARD` | `+0.67%` | `0x33ad48ed92` |
| `SELL` | `8.89` | `202.6500` | 1,802.07 USD | 5,781,967.55 USD | `STANDARD` | `+0.74%` | `0xc3a5b2551d` |
| `SELL` | `8.89` | `202.6500` | 1,801.19 USD | 5,783,768.74 USD | `STANDARD` | `+0.69%` | `0xc3a5b2551d` |
| `SELL` | `8.90` | `17504.3500` | 155,788.71 USD | 1,856,251.36 USD | `LARGE (>= USD 100K)` | `+0.82%` | `0x71d0e11ebb` |
| `SELL` | `8.90` | `1348.9900` | 11,999.94 USD | 5,040,742.35 USD | `STANDARD` | `+0.77%` | `0x0efb38a5fa` |
| `SELL` | `8.90` | `1250.0000` | 11,119.87 USD | 5,087,198.16 USD | `STANDARD` | `+0.77%` | `0xb7bd9cef0e` |
| `SELL` | `8.90` | `382.1700` | 3,402.04 USD | 5,566,987.57 USD | `STANDARD` | `+0.84%` | `0x14f8e04290` |
| `SELL` | `8.90` | `202.6500` | 1,803.81 USD | 5,778,362.55 USD | `STANDARD` | `+0.83%` | `0xc3a5b2551d` |
| `SELL` | `8.90` | `202.6500` | 1,802.94 USD | 5,780,165.49 USD | `STANDARD` | `+0.78%` | `0xc3a5b2551d` |
| `SELL` | `8.90` | `131.2700` | 1,168.92 USD | 5,828,250.29 USD | `STANDARD` | `+0.87%` | `0xe34d21d198` |
| `SELL` | `8.91` | `52039.5300` | 463,765.88 USD | 463,765.88 USD | `LARGE (>= USD 100K)` | `+0.95%` | `0x71cfa5e263` |
| `SELL` | `8.91` | `11241.0300` | 100,126.10 USD | 3,979,525.47 USD | `LARGE (>= USD 100K)` | `+0.90%` | `0x881cd92459` |
| `SELL` | `8.91` | `315.7300` | 2,812.84 USD | 5,630,839.98 USD | `STANDARD` | `+0.92%` | `0x07fd993f0f` |
| `SELL` | `8.91` | `202.6500` | 1,806.42 USD | 5,772,948.51 USD | `STANDARD` | `+0.98%` | `0xc3a5b2551d` |
| `SELL` | `8.91` | `202.6500` | 1,805.55 USD | 5,774,754.06 USD | `STANDARD` | `+0.93%` | `0xc3a5b2551d` |
| `SELL` | `8.91` | `202.6500` | 1,804.68 USD | 5,776,558.74 USD | `STANDARD` | `+0.88%` | `0xc3a5b2551d` |
| `SELL` | `8.92` | `11293.9600` | 100,762.45 USD | 3,879,399.37 USD | `LARGE (>= USD 100K)` | `+1.07%` | `0xecb63caa47` |
| `SELL` | `8.92` | `1772.0400` | 15,803.05 USD | 4,488,442.28 USD | `STANDARD` | `+1.02%` | `0xd3943e4008` |
| `SELL` | `8.92` | `202.6500` | 1,808.19 USD | 5,769,334.80 USD | `STANDARD` | `+1.08%` | `0xc3a5b2551d` |
| `SELL` | `8.92` | `202.6500` | 1,807.29 USD | 5,771,142.09 USD | `STANDARD` | `+1.03%` | `0xc3a5b2551d` |
| `SELL` | `8.92` | `82.0300` | 731.81 USD | 5,847,074.15 USD | `STANDARD` | `+1.06%` | `0x010461c14e` |
| `SELL` | `8.92` | `71.9500` | 642.12 USD | 5,856,641.56 USD | `STANDARD` | `+1.10%` | `0x31ca8395cf` |
| `SELL` | `8.93` | `1354.3400` | 12,088.30 USD | 5,004,740.12 USD | `STANDARD` | `+1.11%` | `0x33ad48ed92` |
| `SELL` | `8.93` | `381.2400` | 3,403.67 USD | 5,563,585.53 USD | `STANDARD` | `+1.14%` | `0x14f8e04290` |
| `SELL` | `8.93` | `202.6500` | 1,809.93 USD | 5,765,717.55 USD | `STANDARD` | `+1.17%` | `0xc3a5b2551d` |
| `SELL` | `8.93` | `202.6500` | 1,809.06 USD | 5,767,526.61 USD | `STANDARD` | `+1.13%` | `0xc3a5b2551d` |
| `SELL` | `8.94` | `17506.5300` | 156,518.88 USD | 1,700,462.64 USD | `LARGE (>= USD 100K)` | `+1.28%` | `0x71d0e11ebb` |
| `SELL` | `8.94` | `12323.9900` | 110,172.77 USD | 3,567,549.35 USD | `LARGE (>= USD 100K)` | `+1.27%` | `0xecb63caa47` |
| `SELL` | `8.94` | `2237.3100` | 20,007.59 USD | 4,346,840.55 USD | `STANDARD` | `+1.30%` | `0xd3943e4008` |
| `SELL` | `8.94` | `1789.5800` | 15,999.92 USD | 4,472,639.23 USD | `STANDARD` | `+1.28%` | `0x0efb38a5fa` |
| `SELL` | `8.94` | `202.6500` | 1,812.54 USD | 5,760,285.16 USD | `STANDARD` | `+1.32%` | `0xc3a5b2551d` |
| `SELL` | `8.94` | `202.6500` | 1,811.67 USD | 5,762,096.83 USD | `STANDARD` | `+1.27%` | `0xc3a5b2551d` |
| `SELL` | `8.94` | `202.6500` | 1,810.80 USD | 5,763,907.63 USD | `STANDARD` | `+1.22%` | `0xc3a5b2551d` |
| `SELL` | `8.95` | `12883.5500` | 115,329.67 USD | 3,233,039.22 USD | `LARGE (>= USD 100K)` | `+1.41%` | `0x71d0e11ebb` |
| `SELL` | `8.95` | `202.6500` | 1,814.28 USD | 5,756,659.20 USD | `STANDARD` | `+1.42%` | `0xc3a5b2551d` |
| `SELL` | `8.95` | `202.6500` | 1,813.41 USD | 5,758,472.61 USD | `STANDARD` | `+1.37%` | `0xc3a5b2551d` |
| `SELL` | `8.95` | `195.4700` | 1,749.67 USD | 5,810,542.24 USD | `STANDARD` | `+1.40%` | `0x31ca8395cf` |
| `SELL` | `8.96` | `13283.4900` | 118,990.85 USD | 3,117,709.54 USD | `LARGE (>= USD 100K)` | `+1.47%` | `0xecb63caa47` |
| `SELL` | `8.96` | `2119.3500` | 18,999.97 USD | 4,365,840.52 USD | `STANDARD` | `+1.56%` | `0x0efb38a5fa` |
| `SELL` | `8.96` | `202.6500` | 1,816.03 USD | 5,753,029.76 USD | `STANDARD` | `+1.52%` | `0xc3a5b2551d` |
| `SELL` | `8.96` | `202.6500` | 1,815.16 USD | 5,754,844.91 USD | `STANDARD` | `+1.47%` | `0xc3a5b2551d` |
| `SELL` | `8.96` | `188.0800` | 1,684.39 USD | 5,813,972.73 USD | `STANDARD` | `+1.45%` | `0x010461c14e` |
| `SELL` | `8.96` | `133.0200` | 1,191.33 USD | 5,827,081.37 USD | `STANDARD` | `+1.45%` | `0xdadbb4b2a0` |
| `SELL` | `8.97` | `315.7300` | 2,831.15 USD | 5,608,263.33 USD | `STANDARD` | `+1.58%` | `0x07fd993f0f` |
| `SELL` | `8.97` | `202.6500` | 1,818.64 USD | 5,747,579.06 USD | `STANDARD` | `+1.66%` | `0xc3a5b2551d` |
| `SELL` | `8.97` | `202.6500` | 1,817.77 USD | 5,749,396.83 USD | `STANDARD` | `+1.61%` | `0xc3a5b2551d` |
| `SELL` | `8.97` | `202.6500` | 1,816.90 USD | 5,751,213.73 USD | `STANDARD` | `+1.56%` | `0xc3a5b2551d` |
| `SELL` | `8.98` | `10861.1200` | 97,493.76 USD | 4,177,144.62 USD | `MEDIUM (>= USD 25K)` | `+1.69%` | `0xecb63caa47` |
| `SELL` | `8.98` | `388.5400` | 3,489.44 USD | 5,556,694.42 USD | `STANDARD` | `+1.74%` | `0x14f8e04290` |
| `SELL` | `8.98` | `202.6500` | 1,820.38 USD | 5,743,940.91 USD | `STANDARD` | `+1.76%` | `0xc3a5b2551d` |
| `SELL` | `8.98` | `202.6500` | 1,819.51 USD | 5,745,760.42 USD | `STANDARD` | `+1.71%` | `0xc3a5b2551d` |
| `SELL` | `8.99` | `202.6500` | 1,822.15 USD | 5,740,299.27 USD | `STANDARD` | `+1.86%` | `0xc3a5b2551d` |
| `SELL` | `8.99` | `202.6500` | 1,821.26 USD | 5,742,120.52 USD | `STANDARD` | `+1.81%` | `0xc3a5b2551d` |
| `SELL` | `9.00` | `17529.6500` | 157,749.32 USD | 1,543,943.76 USD | `LARGE (>= USD 100K)` | `+1.94%` | `0x71d0e11ebb` |
| `SELL` | `9.00` | `387.5400` | 3,487.43 USD | 5,560,181.85 USD | `STANDARD` | `+1.94%` | `0x14f8e04290` |
| `SELL` | `9.00` | `202.6500` | 1,823.89 USD | 5,736,654.10 USD | `STANDARD` | `+1.96%` | `0xc3a5b2551d` |
| `SELL` | `9.00` | `202.6500` | 1,823.02 USD | 5,738,477.12 USD | `STANDARD` | `+1.91%` | `0xc3a5b2551d` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 19:44:05 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1497` | `0x7737...bf66` | `SHORT` | 1,514,517.05 USD | `171,568.06` | `7.43` | `8.83` | `111.70` | -238,972.03 USD | `-15.78%` | `10X Cross` |
| `1582` | `0xeadc...9d55` | `LONG` | 1,413,294.99 USD | `160,070.56` | `8.11` | `8.83` | `0.000000` | 115,657.41 USD | `+8.18%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `8.87` | 13,481.68 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 13.48K USD at 8.8655 USD [API] | `2026-10-27 20:29:33` |
| `ANNOUNCEMENT` | `INFO` | `8.87` | 9,999.42 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 10.00K USD at 8.8656 USD [API] | `2026-10-27 20:29:33` |
| `ANNOUNCEMENT` | `INFO` | `8.94` | 5,181.55 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 5.18K USD at 8.9425 USD [API] | `2026-10-27 21:41:02` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`8.96` (Vol: 194,000.00 USD, Dist: `+1.37%`) | Long MP=`8.46` (Vol: 190,100.00 USD, Dist: `--4.33%`)
  * 48H Horizon: Short MP=`8.96` (Vol: 194,000.00 USD, Dist: `+1.37%`) | Long MP=`8.46` (Vol: 190,100.00 USD, Dist: `--4.33%`)
  * 3D Horizon: Short MP=`8.96` (Vol: 194,000.00 USD, Dist: `+1.37%`) | Long MP=`8.55` (Vol: 157,300.00 USD, Dist: `--3.28%`)
  * 7D Horizon: Short MP=`9.28` (Vol: 346,800.00 USD, Dist: `+4.99%`) | Long MP=`8.54` (Vol: 343,100.00 USD, Dist: `--3.44%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.77` | 195.25 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 209.55 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 159.60 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 117.35 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 958.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 814.80 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 273.35 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 17,580.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 1,740.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 598.46 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 1,100.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 1,510.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 103.35 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 689.17 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 151.82 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.63` | 2,070.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 1,410.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 385.50 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.88` | 2,160.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.88` | 362.55 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.92` | 8,900.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.00` | 100.12 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 159.29 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.18` | 174.89 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.21` | 982.29 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 4,630.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.26` | 639.75 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.30` | 174.83 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.32` | 852.47 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 486.93 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 2,680.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.63` | 676.62 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 3,280.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 15,400.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 2,390.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.79` | 15,760.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.80` | 1,300.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 3,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 4,180.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 527.19 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 239.41 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.99` | 807.92 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 167.78 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 314.59 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 318.46 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.16` | 156,890.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 2,300.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 300.91 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 640.70 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.30` | 232.41 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 21,080.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.51` | 367.41 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 121.38 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.57` | 967.98 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.59` | 34,430.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 468.55 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.70` | 405.03 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 2,340.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 238.86 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 2,890.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 5,140.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 580.50 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 22,060.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 1,910.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.99` | 447.98 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 1,690.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 448.72 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 672.24 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 405.14 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 4,220.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.11` | 3,200.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 2,360.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.13` | 809.21 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 4,390.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 345,790.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.18` | 1,440.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 2,560.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.22` | 715.31 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 971.10 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.32` | 277.04 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 105.25 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.34` | 248.79 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,220.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 5,110.00 USD | 889,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 2,010.00 USD | 884,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 882,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 875,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 3,620.00 USD | 874,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 11,130.00 USD | 870,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 3,170.00 USD | 859,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 1,100.00 USD | 856,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 855,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.70` | 506.54 USD | 853,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 16,610.00 USD | 852,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 835,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.76` | 15,310.00 USD | 834,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 6,780.00 USD | 819,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 16,960.00 USD | 812,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 4,260.00 USD | 795,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 28,720.00 USD | 791,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 2,820.00 USD | 762,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 4,410.00 USD | 759,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.86` | 18,930.00 USD | 755,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,770.00 USD | 736,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.89` | 5,250.00 USD | 732,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.91` | 269.30 USD | 727,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 1,390.00 USD | 727,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,760.00 USD | 725,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 3,480.00 USD | 722,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 718,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 746.58 USD | 717,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 20,860.00 USD | 717,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.04` | 4,100.00 USD | 696,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 692,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,670.00 USD | 685,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 683,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 821.73 USD | 683,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 2,410.00 USD | 682,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,950.00 USD | 680,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 659,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 257.72 USD | 657,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 322.94 USD | 657,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.24` | 179.65 USD | 657,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 657,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.26` | 1,020.00 USD | 656,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,420.00 USD | 655,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.32` | 1,760.00 USD | 619,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 4,910.00 USD | 617,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 2,450.00 USD | 612,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 4,370.00 USD | 610,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.37` | 5,720.00 USD | 605,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 3,920.00 USD | 600,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 18,090.00 USD | 596,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.39` | 1,550.00 USD | 578,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.41` | 1,480.00 USD | 576,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.42` | 147.41 USD | 575,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.42` | 352.39 USD | 575,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 210.99 USD | 574,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 1,370.00 USD | 574,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 573,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 3,210.00 USD | 568,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.49` | 322.45 USD | 565,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,580.00 USD | 564,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 656.99 USD | 563,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.53` | 433.52 USD | 562,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 562,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 844.21 USD | 558,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 1,310.00 USD | 557,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.57` | 4,380.00 USD | 555,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.59` | 25,140.00 USD | 551,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 312.22 USD | 526,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 526,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 525,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 524,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.67` | 1,740.00 USD | 524,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.68` | 1,120.00 USD | 523,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.70` | 1,460.00 USD | 521,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.71` | 19,410.00 USD | 520,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.71` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 0.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.72` | 2,550.00 USD | 501,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.75` | 8,530,000.00 USD | 8,530,000.00 USD | 976.80 USD | 5,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 1,820.00 USD | 498,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 496,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.77` | 8,520,000.00 USD | 8,520,000.00 USD | 17,170.00 USD | 4,900.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.78` | 2,810.00 USD | 496,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 1,780.00 USD | 493,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.79` | 8,500,000.00 USD | 8,500,000.00 USD | 19,090.00 USD | 4,540.00 USD | 15,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 1,940.00 USD | 491,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.80` | 633.77 USD | 489,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.81` | 8,460,000.00 USD | 8,460,000.00 USD | 2,240.00 USD | 11,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.82` | 5,280.00 USD | 489,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.83` | 3,970,000.00 USD | 3,970,000.00 USD | 4,150.00 USD | 4,390.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.83` | 8,440,000.00 USD | 8,440,000.00 USD | 28,130.00 USD | 2,130.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.83` | 160.30 USD | 483,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.84` | 3,950,000.00 USD | 3,950,000.00 USD | 245.00 USD | 563.17 USD | 7,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 10,930.00 USD | 483,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.85` | 3,940,000.00 USD | 3,940,000.00 USD | 4,330.00 USD | 1,250.00 USD | 1,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.85` | 8,390,000.00 USD | 8,390,000.00 USD | 15,410.00 USD | 7,840.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.86` | 2,110.00 USD | 472,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.86` | 3,940,000.00 USD | 3,940,000.00 USD | 10,180.00 USD | 424.36 USD | 11,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.87` | 3,910,000.00 USD | 3,910,000.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.87` | 8,360,000.00 USD | 8,360,000.00 USD | 39,380.00 USD | 1,540.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 1,080.00 USD | 470,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 3,890,000.00 USD | 3,890,000.00 USD | 16,020.00 USD | 4,370.00 USD | 4,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.89` | 3,860,000.00 USD | 3,860,000.00 USD | 5,220.00 USD | 4,150.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.89` | 8,300,000.00 USD | 8,300,000.00 USD | 25,450.00 USD | 18,320.00 USD | 24,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.90` | 3,850,000.00 USD | 3,850,000.00 USD | 9,200.00 USD | 3,480.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 505.13 USD | 469,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 3,830,000.00 USD | 3,830,000.00 USD | 2,990.00 USD | 0.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.91` | 8,230,000.00 USD | 8,230,000.00 USD | 29,920.00 USD | 11,120.00 USD | 17,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.92` | 3,830,000.00 USD | 3,830,000.00 USD | 12,900.00 USD | 2,950.00 USD | 3,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 923.42 USD | 469,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 2,050.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.93` | 8,170,000.00 USD | 8,170,000.00 USD | 78,470.00 USD | 7,330.00 USD | 14,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 1,820.00 USD | 468,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 3,800,000.00 USD | 3,800,000.00 USD | 10,710.00 USD | 3,900.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 129,030.00 USD | 466,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.95` | 8,070,000.00 USD | 8,070,000.00 USD | 30,870.00 USD | 7,400.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 1,140.00 USD | 337,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 3,780,000.00 USD | 3,780,000.00 USD | 8,450.00 USD | 2,280.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.97` | 3,770,000.00 USD | 3,770,000.00 USD | 11,690.00 USD | 5,500.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.97` | 8,000,000.00 USD | 8,000,000.00 USD | 23,940.00 USD | 18,700.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.98` | 3,740,000.00 USD | 3,740,000.00 USD | 10,080.00 USD | 1,760.00 USD | 548.73 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,970.00 USD | 336,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 3,730,000.00 USD | 3,730,000.00 USD | 9,190.00 USD | 2,180.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.99` | 7,920,000.00 USD | 7,920,000.00 USD | 49,120.00 USD | 7,410.00 USD | 45,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 210.99 USD | 334,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 3,710,000.00 USD | 3,710,000.00 USD | 2,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 3,710,000.00 USD | 3,710,000.00 USD | 6,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.01` | 7,810,000.00 USD | 7,810,000.00 USD | 48,920.00 USD | 17,990.00 USD | 470.04 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.02` | 1,530.00 USD | 333,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.02` | 3,700,000.00 USD | 3,700,000.00 USD | 2,230.00 USD | 770.83 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 957.70 USD | 332,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 3,700,000.00 USD | 3,700,000.00 USD | 8,800.00 USD | 0.00 USD | 4,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.03` | 7,750,000.00 USD | 7,750,000.00 USD | 74,890.00 USD | 19,990.00 USD | 36,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 88,380.00 USD | 331,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.04` | 3,690,000.00 USD | 3,690,000.00 USD | 3,240.00 USD | 0.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 12,840.00 USD | 243,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.05` | 3,680,000.00 USD | 3,680,000.00 USD | 3,700.00 USD | 1,790.00 USD | 1,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.05` | 7,610,000.00 USD | 7,610,000.00 USD | 35,690.00 USD | 29,270.00 USD | 62,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.05` | 3,340.00 USD | 230,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.06` | 3,670,000.00 USD | 3,670,000.00 USD | 7,120.00 USD | 0.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 37,830.00 USD | 226,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 3,660,000.00 USD | 3,660,000.00 USD | 944.98 USD | 0.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.07` | 7,490,000.00 USD | 7,490,000.00 USD | 63,420.00 USD | 5,870.00 USD | 68,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.08` | 3,660,000.00 USD | 3,660,000.00 USD | 769.07 USD | 269.63 USD | 3,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 617.61 USD | 189,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.09` | 3,650,000.00 USD | 3,650,000.00 USD | 6,700.00 USD | 1,220.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.09` | 7,350,000.00 USD | 7,350,000.00 USD | 36,020.00 USD | 16,210.00 USD | 27,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.10` | 3,640,000.00 USD | 3,640,000.00 USD | 23,830.00 USD | 1,620.00 USD | 6,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.11` | 3,610,000.00 USD | 3,610,000.00 USD | 144.37 USD | 1,980.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.11` | 7,270,000.00 USD | 7,270,000.00 USD | 36,180.00 USD | 10,160.00 USD | 7,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 241.26 USD | 188,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 3,600,000.00 USD | 3,600,000.00 USD | 3,730.00 USD | 0.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.13` | 3,590,000.00 USD | 3,590,000.00 USD | 4,140.00 USD | 693.45 USD | 1,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.13` | 7,210,000.00 USD | 7,210,000.00 USD | 32,750.00 USD | 11,560.00 USD | 20,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 3,590,000.00 USD | 3,590,000.00 USD | 8,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.14` | 11,610.00 USD | 188,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.15` | 3,580,000.00 USD | 3,580,000.00 USD | 11,200.00 USD | 662.47 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.15` | 7,150,000.00 USD | 7,150,000.00 USD | 77,290.00 USD | 5,090.00 USD | 46,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 3,560,000.00 USD | 3,560,000.00 USD | 385.98 USD | 2,120.00 USD | 92.96 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.16` | 871.61 USD | 176,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.17` | 3,560,000.00 USD | 3,560,000.00 USD | 2,970.00 USD | 0.00 USD | 8.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.17` | 7,020,000.00 USD | 7,020,000.00 USD | 15,580.00 USD | 7,770.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 3,560,000.00 USD | 3,560,000.00 USD | 1,150.00 USD | 1,980.00 USD | 898.09 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.19` | 31,640.00 USD | 175,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.19` | 3,550,000.00 USD | 3,550,000.00 USD | 4,850.00 USD | 0.00 USD | 28.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.19` | 6,990,000.00 USD | 6,990,000.00 USD | 50,160.00 USD | 3,170.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.20` | 1,740.00 USD | 144,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.20` | 3,550,000.00 USD | 3,550,000.00 USD | 7,720.00 USD | 2,310.00 USD | 53.42 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 577.06 USD | 142,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.21` | 3,540,000.00 USD | 3,540,000.00 USD | 1,880.00 USD | 0.00 USD | 20.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.21` | 6,930,000.00 USD | 6,930,000.00 USD | 41,390.00 USD | 0.00 USD | 23,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 565.68 USD | 141,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.22` | 3,540,000.00 USD | 3,540,000.00 USD | 5,330.00 USD | 0.00 USD | 12,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.22` | 2,100.00 USD | 141,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.23` | 3,520,000.00 USD | 3,520,000.00 USD | 20,950.00 USD | 4,080.00 USD | 30,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.23` | 6,870,000.00 USD | 6,870,000.00 USD | 21,610.00 USD | 3,480.00 USD | 115,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.23` | 1,530.00 USD | 139,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.24` | 3,460,000.00 USD | 3,460,000.00 USD | 10,020.00 USD | 1,150.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.24` | 1,120.00 USD | 137,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.25` | 3,450,000.00 USD | 3,450,000.00 USD | 8,710.00 USD | 0.00 USD | 6,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.25` | 6,720,000.00 USD | 6,720,000.00 USD | 55,820.00 USD | 5,750.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.26` | 21,400.00 USD | 136,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.26` | 3,430,000.00 USD | 3,430,000.00 USD | 192.60 USD | 11,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.27` | 2,160.00 USD | 115,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.27` | 3,420,000.00 USD | 3,420,000.00 USD | 11,800.00 USD | 2,760.00 USD | 22.02 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.27` | 6,650,000.00 USD | 6,650,000.00 USD | 64,340.00 USD | 14,400.00 USD | 8,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.28` | 1,190.00 USD | 112,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.28` | 3,410,000.00 USD | 3,410,000.00 USD | 74,980.00 USD | 7,070.00 USD | 40,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 498.26 USD | 111,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.29` | 3,280,000.00 USD | 3,280,000.00 USD | 34,940.00 USD | 9,470.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.29` | 6,570,000.00 USD | 6,570,000.00 USD | 116,340.00 USD | 19,520.00 USD | 52,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 23,710.00 USD | 111,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.30` | 3,230,000.00 USD | 3,230,000.00 USD | 52,980.00 USD | 13,130.00 USD | 19,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.30` | 34,320.00 USD | 87,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.31` | 3,150,000.00 USD | 3,150,000.00 USD | 55,700.00 USD | 11,410.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.31` | 6,380,000.00 USD | 6,380,000.00 USD | 79,020.00 USD | 13,500.00 USD | 10,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.31` | 4,730.00 USD | 53,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.32` | 3,080,000.00 USD | 3,080,000.00 USD | 19,320.00 USD | 4,190.00 USD | 7,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 3,050,000.00 USD | 3,050,000.00 USD | 2,670.00 USD | 22,580.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.33` | 6,270,000.00 USD | 6,270,000.00 USD | 58,510.00 USD | 36,210.00 USD | 19,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.34` | 945.86 USD | 48,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.34` | 3,010,000.00 USD | 3,010,000.00 USD | 14,430.00 USD | 4,810.00 USD | 6,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.35` | 185.09 USD | 47,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.35` | 2,990,000.00 USD | 2,990,000.00 USD | 6,060.00 USD | 11,270.00 USD | 16,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.35` | 6,160,000.00 USD | 6,160,000.00 USD | 93,810.00 USD | 5,340.00 USD | 81,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.36` | 3,410.00 USD | 47,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.36` | 2,960,000.00 USD | 2,960,000.00 USD | 3,900.00 USD | 2,420.00 USD | 21,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.37` | 7,410.00 USD | 43,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.37` | 2,930,000.00 USD | 2,930,000.00 USD | 21,620.00 USD | 7,980.00 USD | 8,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.37` | 5,980,000.00 USD | 5,980,000.00 USD | 92,990.00 USD | 31,220.00 USD | 24,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.38` | 2,890,000.00 USD | 2,890,000.00 USD | 36,180.00 USD | 4,080.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.38` | 955.89 USD | 36,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.39` | 2,820,000.00 USD | 2,820,000.00 USD | 62,830.00 USD | 10,540.00 USD | 56,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.39` | 5,830,000.00 USD | 5,830,000.00 USD | 197,080.00 USD | 8,930.00 USD | 68,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.39` | 1,680.00 USD | 35,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.40` | 2,690,000.00 USD | 2,690,000.00 USD | 68,490.00 USD | 22,890.00 USD | 68,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.40` | 608.02 USD | 33,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.41` | 2,530,000.00 USD | 2,530,000.00 USD | 33,190.00 USD | 3,620.00 USD | 20,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.41` | 5,560,000.00 USD | 5,560,000.00 USD | 120,570.00 USD | 32,690.00 USD | 244,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.41` | 102.33 USD | 33,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.42` | 2,470,000.00 USD | 2,470,000.00 USD | 33,460.00 USD | 12,790.00 USD | 18,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.43` | 674.00 USD | 33,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.43` | 2,400,000.00 USD | 2,400,000.00 USD | 30,620.00 USD | 34,530.00 USD | 14,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.43` | 5,160,000.00 USD | 5,160,000.00 USD | 179,770.00 USD | 62,350.00 USD | 73,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.44` | 188.61 USD | 32,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.44` | 2,320,000.00 USD | 2,320,000.00 USD | 35,960.00 USD | 8,900.00 USD | 7,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.45` | 588.70 USD | 32,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.45` | 2,270,000.00 USD | 2,270,000.00 USD | 72,750.00 USD | 14,270.00 USD | 45,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.45` | 4,840,000.00 USD | 4,840,000.00 USD | 210,670.00 USD | 59,180.00 USD | 89,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.46` | 226.93 USD | 31,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.46` | 2,140,000.00 USD | 2,140,000.00 USD | 138,660.00 USD | 16,750.00 USD | 52,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.47` | 1,930,000.00 USD | 1,930,000.00 USD | 104,430.00 USD | 30,750.00 USD | 22,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.47` | 4,480,000.00 USD | 4,480,000.00 USD | 372,700.00 USD | 70,760.00 USD | 189,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.47` | 12,430.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.48` | 1,770,000.00 USD | 1,770,000.00 USD | 109,960.00 USD | 32,070.00 USD | 41,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.48` | 1,850.00 USD | 19,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.49` | 1,590,000.00 USD | 1,590,000.00 USD | 136,720.00 USD | 29,970.00 USD | 21,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.49` | 3,850,000.00 USD | 3,850,000.00 USD | 256,280.00 USD | 46,290.00 USD | 100,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.49` | 205.24 USD | 17,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.50` | 1,400,000.00 USD | 1,400,000.00 USD | 46,010.00 USD | 19,260.00 USD | 21,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.51` | 5,770.00 USD | 16,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.51` | 1,320,000.00 USD | 1,320,000.00 USD | 55,990.00 USD | 54,280.00 USD | 43,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.51` | 3,450,000.00 USD | 3,450,000.00 USD | 172,680.00 USD | 117,050.00 USD | 139,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.52` | 2,260.00 USD | 11,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.52` | 1,160,000.00 USD | 1,160,000.00 USD | 79,750.00 USD | 22,420.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.53` | 1,040,000.00 USD | 1,040,000.00 USD | 16,630.00 USD | 23,780.00 USD | 32,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.53` | 3,020,000.00 USD | 3,020,000.00 USD | 415,280.00 USD | 66,260.00 USD | 317,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 6,350.00 USD | 8,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.54` | 971,010.00 USD | 971,010.00 USD | 18,880.00 USD | 6,040.00 USD | 43,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 1,550.00 USD | 2,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.55` | 902,430.00 USD | 902,430.00 USD | 42,130.00 USD | 17,890.00 USD | 16,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.55` | 2,220,000.00 USD | 2,220,000.00 USD | 278,460.00 USD | 136,440.00 USD | 16,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.55` | 1,060.00 USD | 1,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.56` | 825,790.00 USD | 825,790.00 USD | 69,420.00 USD | 8,150.00 USD | 67,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.57` | 680,470.00 USD | 680,470.00 USD | 56,370.00 USD | 7,000.00 USD | 55,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.57` | 1,790,000.00 USD | 1,790,000.00 USD | 636,260.00 USD | 84,440.00 USD | 47,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.58` | 561,460.00 USD | 561,460.00 USD | 48,420.00 USD | 13,910.00 USD | 39,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.59` | 459,220.00 USD | 459,220.00 USD | 43,310.00 USD | 25,580.00 USD | 12,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.59` | 1,020,000.00 USD | 1,020,000.00 USD | 265,650.00 USD | 118,220.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.60` | 377,810.00 USD | 377,810.00 USD | 58,480.00 USD | 23,230.00 USD | 34,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.61` | 261,430.00 USD | 261,430.00 USD | 28,830.00 USD | 6,770.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.61` | 588,050.00 USD | 588,050.00 USD | 75,040.00 USD | 23,160.00 USD | 229,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.62` | 194,930.00 USD | 194,930.00 USD | 87,140.00 USD | 14,760.00 USD | 19,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.63` | 73,100.00 USD | 73,100.00 USD | 24,730.00 USD | 2,010.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.63` | 260,790.00 USD | 260,790.00 USD | 51,260.00 USD | 21,230.00 USD | 13,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.64` | 42,500.00 USD | 42,500.00 USD | 27,270.00 USD | 1,540.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.65` | 10,520.00 USD | 10,520.00 USD | 7,900.00 USD | 2,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.65` | 175,050.00 USD | 175,050.00 USD | 0.00 USD | 0.00 USD | 748.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.67` | 174,300.00 USD | 174,300.00 USD | 0.00 USD | 0.00 USD | 173,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.69` | 388.62 USD | 388.62 USD | 0.00 USD | 0.00 USD | 270.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.81` | 118.36 USD | 118.36 USD | 0.00 USD | 0.00 USD | 118.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.83` | 60,010.00 USD | 60,010.00 USD | 0.00 USD | 0.00 USD | 60,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 162,460.00 USD | 162,460.00 USD | 97,740.00 USD | 16,450.00 USD | 48,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 237,220.00 USD | 237,220.00 USD | 0.00 USD | 48,620.00 USD | 26,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.85` | 226,750.00 USD | 226,750.00 USD | 35,640.00 USD | 62,560.00 USD | 68,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 287,070.00 USD | 287,070.00 USD | 25,310.00 USD | 12,040.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.87` | 385,090.00 USD | 385,090.00 USD | 9,410.00 USD | 22,550.00 USD | 66,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.87` | 389,670.00 USD | 389,670.00 USD | 84,140.00 USD | 0.00 USD | 78,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 438,060.00 USD | 438,060.00 USD | 4,550.00 USD | 4,830.00 USD | 43,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.89` | 511,410.00 USD | 511,410.00 USD | 40,760.00 USD | 15,970.00 USD | 16,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.89` | 545,150.00 USD | 545,150.00 USD | 70,340.00 USD | 40,670.00 USD | 44,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 670,570.00 USD | 670,570.00 USD | 73,240.00 USD | 8,150.00 USD | 77,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.91` | 929,700.00 USD | 929,700.00 USD | 130,250.00 USD | 25,170.00 USD | 103,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.91` | 831,840.00 USD | 831,840.00 USD | 108,450.00 USD | 25,770.00 USD | 152,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 942,410.00 USD | 942,410.00 USD | 8,060.00 USD | 1,150.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 1,060,000.00 USD | 1,060,000.00 USD | 55,830.00 USD | 40,980.00 USD | 18,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.93` | 908,520.00 USD | 908,520.00 USD | 14,600.00 USD | 20,540.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 1,130,000.00 USD | 1,130,000.00 USD | 34,120.00 USD | 14,100.00 USD | 27,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.95` | 1,240,000.00 USD | 1,240,000.00 USD | 53,880.00 USD | 28,330.00 USD | 25,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.95` | 1,030,000.00 USD | 1,030,000.00 USD | 59,990.00 USD | 53,160.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.96` | 1,390,000.00 USD | 1,390,000.00 USD | 73,070.00 USD | 26,680.00 USD | 46,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.97` | 1,430,000.00 USD | 1,430,000.00 USD | 28,830.00 USD | 6,770.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.97` | 1,250,000.00 USD | 1,250,000.00 USD | 144,250.00 USD | 61,890.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.98` | 1,640,000.00 USD | 1,640,000.00 USD | 147,050.00 USD | 18,380.00 USD | 42,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 1,720,000.00 USD | 1,720,000.00 USD | 59,440.00 USD | 11,480.00 USD | 8,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.99` | 1,510,000.00 USD | 1,510,000.00 USD | 155,540.00 USD | 33,480.00 USD | 63,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.00` | 1,860,000.00 USD | 1,860,000.00 USD | 79,520.00 USD | 31,900.00 USD | 30,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 1,940,000.00 USD | 1,940,000.00 USD | 64,160.00 USD | 14,030.00 USD | 1,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.01` | 1,590,000.00 USD | 1,590,000.00 USD | 59,290.00 USD | 19,660.00 USD | 8,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 1,980,000.00 USD | 1,980,000.00 USD | 18,000.00 USD | 4,190.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 2,050,000.00 USD | 2,050,000.00 USD | 2,970.00 USD | 44,330.00 USD | 22,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.03` | 1,700,000.00 USD | 1,700,000.00 USD | 18,890.00 USD | 76,280.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 2,130,000.00 USD | 2,130,000.00 USD | 24,830.00 USD | 4,810.00 USD | 54,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 2,180,000.00 USD | 2,180,000.00 USD | 8,220.00 USD | 20,830.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.05` | 1,730,000.00 USD | 1,730,000.00 USD | 1,630.00 USD | 4,910.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.06` | 2,220,000.00 USD | 2,220,000.00 USD | 3,490.00 USD | 16,550.00 USD | 21,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 2,260,000.00 USD | 2,260,000.00 USD | 21,880.00 USD | 10,450.00 USD | 8,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.07` | 2,040,000.00 USD | 2,040,000.00 USD | 278,000.00 USD | 14,140.00 USD | 22,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 2,360,000.00 USD | 2,360,000.00 USD | 63,740.00 USD | 6,490.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 2,470,000.00 USD | 2,470,000.00 USD | 54,960.00 USD | 14,400.00 USD | 36,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.09` | 2,380,000.00 USD | 2,380,000.00 USD | 195,250.00 USD | 8,680.00 USD | 134,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.10` | 2,580,000.00 USD | 2,580,000.00 USD | 66,840.00 USD | 14,720.00 USD | 26,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.11` | 783.94 USD | 783.94 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.11` | 2,610,000.00 USD | 2,610,000.00 USD | 19,700.00 USD | 1,320.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.11` | 3,590,000.00 USD | 3,590,000.00 USD | 703,290.00 USD | 17,930.00 USD | 489,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 2,660,000.00 USD | 2,660,000.00 USD | 28,220.00 USD | 16,570.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 2,720,000.00 USD | 2,720,000.00 USD | 29,720.00 USD | 11,620.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.13` | 4,680,000.00 USD | 4,680,000.00 USD | 663,430.00 USD | 26,540.00 USD | 403,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.13` | 314.34 USD | 1,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.14` | 2,760,000.00 USD | 2,760,000.00 USD | 14,660.00 USD | 8,440.00 USD | 17,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.14` | 4,190.00 USD | 5,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.15` | 2,830,000.00 USD | 2,830,000.00 USD | 44,870.00 USD | 7,380.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.15` | 5,280,000.00 USD | 5,280,000.00 USD | 329,660.00 USD | 13,400.00 USD | 249,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 2,880,000.00 USD | 2,880,000.00 USD | 12,360.00 USD | 12,200.00 USD | 25,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 3,020,000.00 USD | 3,020,000.00 USD | 64,710.00 USD | 19,430.00 USD | 51,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.17` | 6,010,000.00 USD | 6,010,000.00 USD | 354,280.00 USD | 125,040.00 USD | 253,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 3,200,000.00 USD | 3,200,000.00 USD | 127,480.00 USD | 19,550.00 USD | 37,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 3,320,000.00 USD | 3,320,000.00 USD | 72,700.00 USD | 22,640.00 USD | 25,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.19` | 6,750,000.00 USD | 6,750,000.00 USD | 475,560.00 USD | 92,890.00 USD | 175,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.20` | 3,450,000.00 USD | 3,450,000.00 USD | 72,570.00 USD | 18,950.00 USD | 40,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 3,570,000.00 USD | 3,570,000.00 USD | 72,580.00 USD | 12,590.00 USD | 30,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.21` | 7,650,000.00 USD | 7,650,000.00 USD | 498,780.00 USD | 120,420.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.21` | 209.36 USD | 5,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.22` | 3,650,000.00 USD | 3,650,000.00 USD | 71,070.00 USD | 8,140.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 3,740,000.00 USD | 3,740,000.00 USD | 57,020.00 USD | 3,310.00 USD | 34,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.23` | 8,580,000.00 USD | 8,580,000.00 USD | 489,380.00 USD | 82,070.00 USD | 360,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 3,780,000.00 USD | 3,780,000.00 USD | 26,080.00 USD | 8,310.00 USD | 3,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 3,800,000.00 USD | 3,800,000.00 USD | 7,640.00 USD | 11,850.00 USD | 37.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.25` | 9,070,000.00 USD | 9,070,000.00 USD | 277,290.00 USD | 73,690.00 USD | 141,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 3,820,000.00 USD | 3,820,000.00 USD | 16,290.00 USD | 1,210.00 USD | 0.73 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 3,830,000.00 USD | 3,830,000.00 USD | 144.37 USD | 11,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.27` | 9,400,000.00 USD | 9,400,000.00 USD | 156,190.00 USD | 118,550.00 USD | 54,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 3,860,000.00 USD | 3,860,000.00 USD | 21,090.00 USD | 0.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 6,150.00 USD | 11,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.29` | 3,920,000.00 USD | 3,920,000.00 USD | 32,900.00 USD | 14,120.00 USD | 13,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.29` | 10,340,000.00 USD | 10,340,000.00 USD | 557,420.00 USD | 90,360.00 USD | 292,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.30` | 3,960,000.00 USD | 3,960,000.00 USD | 19,890.00 USD | 8,530.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 3,980,000.00 USD | 3,980,000.00 USD | 13,100.00 USD | 0.00 USD | 12,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.31` | 11,040,000.00 USD | 11,040,000.00 USD | 355,840.00 USD | 55,090.00 USD | 288,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 3,990,000.00 USD | 3,990,000.00 USD | 387.00 USD | 2,530.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 4,020,000.00 USD | 4,020,000.00 USD | 9,850.00 USD | 0.00 USD | 15,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.33` | 11,410,000.00 USD | 11,410,000.00 USD | 110,980.00 USD | 52,060.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 4,030,000.00 USD | 4,030,000.00 USD | 385.98 USD | 1,350.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.35` | 4,070,000.00 USD | 4,070,000.00 USD | 15,350.00 USD | 3,810.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.35` | 11,910,000.00 USD | 11,910,000.00 USD | 288,510.00 USD | 89,230.00 USD | 115,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 4,150,000.00 USD | 4,150,000.00 USD | 61,640.00 USD | 6,870.00 USD | 17,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 4,190,000.00 USD | 4,190,000.00 USD | 26,010.00 USD | 7,740.00 USD | 3,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.37` | 12,420,000.00 USD | 12,420,000.00 USD | 368,270.00 USD | 34,660.00 USD | 108,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 4,240,000.00 USD | 4,240,000.00 USD | 32,400.00 USD | 4,040.00 USD | 16,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.39` | 4,260,000.00 USD | 4,260,000.00 USD | 8,200.00 USD | 1,730.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.39` | 12,770,000.00 USD | 12,770,000.00 USD | 205,910.00 USD | 62,160.00 USD | 87,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 4,280,000.00 USD | 4,280,000.00 USD | 22,280.00 USD | 1,210.00 USD | 24.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 4,330,000.00 USD | 4,330,000.00 USD | 29,870.00 USD | 1,660.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.41` | 13,190,000.00 USD | 13,190,000.00 USD | 227,860.00 USD | 41,500.00 USD | 147,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 440.06 USD | 12,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 4,340,000.00 USD | 4,340,000.00 USD | 1,520.00 USD | 622.99 USD | 4,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.43` | 4,360,000.00 USD | 4,360,000.00 USD | 5,840.00 USD | 6,940.00 USD | 12,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.43` | 13,430,000.00 USD | 13,430,000.00 USD | 101,970.00 USD | 43,920.00 USD | 95,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 4,360,000.00 USD | 4,360,000.00 USD | 992.05 USD | 0.00 USD | 68.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 4,370,000.00 USD | 4,370,000.00 USD | 1,860.00 USD | 4,940.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.45` | 13,590,000.00 USD | 13,590,000.00 USD | 126,350.00 USD | 16,970.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.46` | 4,380,000.00 USD | 4,380,000.00 USD | 1,800.00 USD | 4,580.00 USD | 21.27 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.47` | 4,400,000.00 USD | 4,400,000.00 USD | 17,460.00 USD | 6,870.00 USD | 192.20 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.47` | 13,800,000.00 USD | 13,800,000.00 USD | 133,560.00 USD | 37,670.00 USD | 40,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.48` | 4,410,000.00 USD | 4,410,000.00 USD | 1,510.00 USD | 0.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 4,440,000.00 USD | 4,440,000.00 USD | 20,880.00 USD | 572.85 USD | 5,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.49` | 13,940,000.00 USD | 13,940,000.00 USD | 57,780.00 USD | 39,440.00 USD | 42,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.50` | 4,460,000.00 USD | 4,460,000.00 USD | 11,770.00 USD | 3,160.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.51` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 58.12 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.51` | 14,280,000.00 USD | 14,280,000.00 USD | 156,120.00 USD | 43,360.00 USD | 142,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.52` | 4,480,000.00 USD | 4,480,000.00 USD | 17,120.00 USD | 3,070.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.53` | 4,510,000.00 USD | 4,510,000.00 USD | 18,480.00 USD | 4,560.00 USD | 29.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.53` | 14,520,000.00 USD | 14,520,000.00 USD | 190,350.00 USD | 15,360.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.54` | 4,520,000.00 USD | 4,520,000.00 USD | 5,310.00 USD | 1,470.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.55` | 4,530,000.00 USD | 4,530,000.00 USD | 2,170.00 USD | 6,330.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.55` | 14,590,000.00 USD | 14,590,000.00 USD | 27,300.00 USD | 19,960.00 USD | 19,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.56` | 4,540,000.00 USD | 4,540,000.00 USD | 5,160.00 USD | 1,280.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.57` | 4,550,000.00 USD | 4,550,000.00 USD | 1,020.00 USD | 3,100.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.57` | 14,760,000.00 USD | 14,760,000.00 USD | 117,990.00 USD | 14,280.00 USD | 33,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.58` | 4,550,000.00 USD | 4,550,000.00 USD | 1,290.00 USD | 563.17 USD | 7,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.59` | 4,560,000.00 USD | 4,560,000.00 USD | 4,670.00 USD | 1,250.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.59` | 14,820,000.00 USD | 14,820,000.00 USD | 28,190.00 USD | 15,650.00 USD | 23,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.60` | 4,580,000.00 USD | 4,580,000.00 USD | 11,210.00 USD | 424.36 USD | 11,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.61` | 4,610,000.00 USD | 4,610,000.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.61` | 14,950,000.00 USD | 14,950,000.00 USD | 81,250.00 USD | 13,850.00 USD | 28,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.62` | 4,610,000.00 USD | 4,610,000.00 USD | 675.26 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.63` | 4,630,000.00 USD | 4,630,000.00 USD | 10,190.00 USD | 4,370.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.63` | 15,000,000.00 USD | 15,000,000.00 USD | 42,830.00 USD | 4,500.00 USD | 6,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.64` | 4,640,000.00 USD | 4,640,000.00 USD | 5,830.00 USD | 0.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.65` | 4,650,000.00 USD | 4,650,000.00 USD | 5,960.00 USD | 4,150.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.65` | 15,070,000.00 USD | 15,070,000.00 USD | 33,020.00 USD | 20,230.00 USD | 18,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.66` | 4,670,000.00 USD | 4,670,000.00 USD | 9,200.00 USD | 3,480.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.67` | 4,670,000.00 USD | 4,670,000.00 USD | 2,990.00 USD | 0.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.67` | 15,150,000.00 USD | 15,150,000.00 USD | 31,000.00 USD | 24,380.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.68` | 4,690,000.00 USD | 4,690,000.00 USD | 12,900.00 USD | 2,950.00 USD | 4,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.69` | 533.26 USD | 12,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.69` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 2,050.00 USD | 1,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.69` | 15,320,000.00 USD | 15,320,000.00 USD | 123,510.00 USD | 17,380.00 USD | 33,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.70` | 4,720,000.00 USD | 4,720,000.00 USD | 10,710.00 USD | 3,900.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.71` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.71` | 15,450,000.00 USD | 15,450,000.00 USD | 82,670.00 USD | 7,400.00 USD | 35,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.72` | 4,730,000.00 USD | 4,730,000.00 USD | 8,450.00 USD | 2,280.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.73` | 15,470,000.00 USD | 15,470,000.00 USD | 5,700.00 USD | 3,160.00 USD | 11,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 12,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.74` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 3,560.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.75` | 4,760,000.00 USD | 4,760,000.00 USD | 11,500.00 USD | 1,940.00 USD | 7,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.75` | 15,540,000.00 USD | 15,540,000.00 USD | 22,950.00 USD | 15,540.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.76` | 15,600,000.00 USD | 15,600,000.00 USD | 18,870.00 USD | 4,140.00 USD | 40,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.80` | 294,160.00 USD | 306,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.88` | 555.86 USD | 307,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.88` | 1,230.00 USD | 308,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.21` | 4,100.00 USD | 312,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.27` | 331.15 USD | 313,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.32` | 20,650.00 USD | 333,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 3,380.00 USD | 337,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.36` | 1,130.00 USD | 338,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.54` | 36,510.00 USD | 374,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 375,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.71` | 218.91 USD | 375,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.96` | 1,920.00 USD | 377,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 384,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.15` | 266.49 USD | 384,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,670.00 USD | 396,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.54` | 125.84 USD | 396,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 408,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.66` | 3,240.00 USD | 411,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.79` | 784.88 USD | 412,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.88` | 59,430.00 USD | 472,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.18` | 1,390.00 USD | 473,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.27` | 723.51 USD | 474,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 475,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 476,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.54` | 36,100.00 USD | 512,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.70` | 14,220.00 USD | 526,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.77` | 435.29 USD | 527,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.79` | 953.38 USD | 528,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 615,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 238,800.00 USD | 854,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.31` | 218.50 USD | 855,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 855,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.54` | 291.68 USD | 855,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 855,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.76` | 3,150.00 USD | 859,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.02` | 276.52 USD | 859,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.28` | 114,750.00 USD | 974,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 974,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.85` | 2,470.00 USD | 977,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 977,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.32` | 12,100.00 USD | 989,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 989,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.40` | 154,050.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.41` | 23,170.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.52` | 110.31 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.81` | 256,330.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.09` | 81,030.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.27` | 1,500.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.48` | 122.81 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 188.78 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.64` | 945.10 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 162.26 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.02` | 191.87 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.14` | 1,710.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.46` | 101.47 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.62` | 4,120.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.64` | 6,530.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.77` | 2,330,000.00 USD | 0.00 USD | 195.25 USD | `-79.89%` | `110.00` |
| `Live` | `Long` | `1.91` | 2,330,000.00 USD | 0.00 USD | 209.55 USD | `-78.42%` | `110.00` |
| `Live` | `Long` | `2.00` | 2,330,000.00 USD | 0.00 USD | 159.60 USD | `-77.40%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,330,000.00 USD | 0.00 USD | 110.52 USD | `-76.95%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,330,000.00 USD | 0.00 USD | 4,920.00 USD | `-76.61%` | `2,382.76` |
| `Live` | `Long` | `2.37` | 2,330,000.00 USD | 0.00 USD | 117.35 USD | `-73.21%` | `49.62` |
| `Live` | `Long` | `2.40` | 2,320,000.00 USD | 0.00 USD | 958.00 USD | `-72.87%` | `400.00` |
| `Live` | `Long` | `2.42` | 2,320,000.00 USD | 0.00 USD | 814.80 USD | `-72.53%` | `336.00` |
| `Live` | `Long` | `2.48` | 2,320,000.00 USD | 0.00 USD | 273.35 USD | `-71.85%` | `110.00` |
| `Live` | `Long` | `2.52` | 2,320,000.00 USD | 0.00 USD | 17,580.00 USD | `-71.51%` | `6,990.57` |
| `Live` | `Long` | `2.60` | 2,310,000.00 USD | 0.00 USD | 1,740.00 USD | `-70.49%` | `666.20` |
| `Live` | `Long` | `2.69` | 2,300,000.00 USD | 0.00 USD | 598.46 USD | `-69.58%` | `222.89` |
| `Live` | `Long` | `2.87` | 2,300,000.00 USD | 0.00 USD | 232.67 USD | `-67.54%` | `81.21` |
| `Live` | `Long` | `2.92` | 2,300,000.00 USD | 0.00 USD | 1,100.00 USD | `-66.86%` | `377.71` |
| `Live` | `Long` | `2.94` | 2,300,000.00 USD | 0.00 USD | 44,510.00 USD | `-66.75%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,260,000.00 USD | 0.00 USD | 1,510.00 USD | `-66.30%` | `508.17` |
| `Live` | `Long` | `3.06` | 2,260,000.00 USD | 0.00 USD | 103.35 USD | `-65.28%` | `33.72` |
| `Live` | `Long` | `3.21` | 2,260,000.00 USD | 0.00 USD | 689.17 USD | `-63.69%` | `215.03` |
| `Live` | `Long` | `3.37` | 2,250,000.00 USD | 0.00 USD | 389.53 USD | `-61.88%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,250,000.00 USD | 0.00 USD | 151.88 USD | `-61.77%` | `45.00` |
| `Live` | `Long` | `3.52` | 2,250,000.00 USD | 0.00 USD | 151.82 USD | `-60.07%` | `43.07` |
| `Live` | `Long` | `3.63` | 2,250,000.00 USD | 0.00 USD | 2,070.00 USD | `-58.82%` | `568.43` |
| `Live` | `Long` | `3.67` | 2,250,000.00 USD | 0.00 USD | 1,410.00 USD | `-58.48%` | `384.03` |
| `Live` | `Long` | `3.75` | 2,250,000.00 USD | 0.00 USD | 1,500.00 USD | `-57.46%` | `400.00` |
| `Live` | `Long` | `3.85` | 2,250,000.00 USD | 0.00 USD | 385.50 USD | `-56.33%` | `100.00` |
| `Live` | `Long` | `3.88` | 2,250,000.00 USD | 0.00 USD | 2,160.00 USD | `-56.10%` | `558.69` |
| `Live` | `Long` | `3.88` | 2,250,000.00 USD | 0.00 USD | 362.55 USD | `-55.99%` | `93.32` |
| `Live` | `Long` | `3.90` | 2,250,000.00 USD | 0.00 USD | 131.73 USD | `-55.87%` | `33.82` |
| `Live` | `Long` | `3.92` | 2,250,000.00 USD | 0.00 USD | 8,900.00 USD | `-55.65%` | `2,273.34` |
| `Live` | `Long` | `4.00` | 2,240,000.00 USD | 0.00 USD | 100.12 USD | `-54.63%` | `25.00` |
| `Live` | `Long` | `4.03` | 2,240,000.00 USD | 0.00 USD | 402.70 USD | `-54.40%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,240,000.00 USD | 0.00 USD | 152.29 USD | `-54.17%` | `37.65` |
| `Live` | `Long` | `4.14` | 2,240,000.00 USD | 0.00 USD | 159.29 USD | `-53.04%` | `38.43` |
| `Live` | `Long` | `4.18` | 2,240,000.00 USD | 0.00 USD | 174.89 USD | `-52.59%` | `41.79` |
| `Live` | `Long` | `4.21` | 2,240,000.00 USD | 0.00 USD | 982.29 USD | `-52.36%` | `233.60` |
| `Live` | `Long` | `4.24` | 2,240,000.00 USD | 0.00 USD | 4,630.00 USD | `-52.02%` | `1,093.00` |
| `Live` | `Long` | `4.26` | 2,230,000.00 USD | 0.00 USD | 639.75 USD | `-51.68%` | `150.00` |
| `Live` | `Long` | `4.30` | 2,230,000.00 USD | 0.00 USD | 174.83 USD | `-51.23%` | `40.61` |
| `Live` | `Long` | `4.32` | 2,230,000.00 USD | 0.00 USD | 852.47 USD | `-51.12%` | `197.56` |
| `Live` | `Long` | `4.59` | 2,230,000.00 USD | 0.00 USD | 30,970.00 USD | `-47.94%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,200,000.00 USD | 0.00 USD | 486.93 USD | `-47.72%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,200,000.00 USD | 0.00 USD | 2,680.00 USD | `-47.60%` | `579.06` |
| `Live` | `Long` | `4.63` | 2,190,000.00 USD | 0.00 USD | 676.62 USD | `-47.49%` | `145.98` |
| `Live` | `Long` | `4.66` | 2,190,000.00 USD | 0.00 USD | 3,280.00 USD | `-47.26%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,190,000.00 USD | 0.00 USD | 1,490.00 USD | `-47.04%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,190,000.00 USD | 0.00 USD | 15,400.00 USD | `-46.92%` | `3,287.97` |
| `Live` | `Long` | `4.75` | 2,170,000.00 USD | 0.00 USD | 2,390.00 USD | `-46.24%` | `504.56` |
| `Live` | `Long` | `4.76` | 2,170,000.00 USD | 0.00 USD | 105.64 USD | `-46.02%` | `22.17` |
| `Live` | `Long` | `4.79` | 2,170,000.00 USD | 0.00 USD | 15,760.00 USD | `-45.68%` | `3,286.00` |
| `Live` | `Long` | `4.80` | 2,160,000.00 USD | 0.00 USD | 1,300.00 USD | `-45.56%` | `270.00` |
| `Live` | `Long` | `4.83` | 2,150,000.00 USD | 0.00 USD | 3,000.00 USD | `-45.22%` | `619.79` |
| `Live` | `Long` | `4.89` | 2,150,000.00 USD | 0.00 USD | 4,180.00 USD | `-44.55%` | `854.62` |
| `Live` | `Long` | `4.91` | 2,150,000.00 USD | 0.00 USD | 527.19 USD | `-44.43%` | `107.48` |
| `Live` | `Long` | `4.92` | 2,150,000.00 USD | 0.00 USD | 1,230.00 USD | `-44.32%` | `251.00` |
| `Live` | `Long` | `4.96` | 2,150,000.00 USD | 0.00 USD | 945.36 USD | `-43.87%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,140,000.00 USD | 0.00 USD | 239.41 USD | `-43.75%` | `48.22` |
| `Live` | `Long` | `4.97` | 2,140,000.00 USD | 0.00 USD | 282.23 USD | `-43.64%` | `56.73` |
| `Live` | `Long` | `4.99` | 2,140,000.00 USD | 0.00 USD | 807.92 USD | `-43.53%` | `162.07` |
| `Live` | `Long` | `5.01` | 2,140,000.00 USD | 0.00 USD | 56,390.00 USD | `-43.19%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,090,000.00 USD | 0.00 USD | 167.78 USD | `-43.07%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,090,000.00 USD | 0.00 USD | 314.59 USD | `-42.96%` | `62.48` |
| `Live` | `Long` | `5.05` | 2,090,000.00 USD | 0.00 USD | 504.74 USD | `-42.73%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,090,000.00 USD | 0.00 USD | 318.46 USD | `-42.51%` | `62.75` |
| `Live` | `Long` | `5.12` | 2,090,000.00 USD | 0.00 USD | 250.20 USD | `-41.94%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,090,000.00 USD | 0.00 USD | 396.06 USD | `-41.83%` | `77.13` |
| `Live` | `Long` | `5.16` | 2,080,000.00 USD | 0.00 USD | 156,890.00 USD | `-41.60%` | `30,435.20` |
| `Live` | `Long` | `5.17` | 1,930,000.00 USD | 0.00 USD | 2,300.00 USD | `-41.49%` | `445.16` |
| `Live` | `Long` | `5.17` | 1,930,000.00 USD | 0.00 USD | 1,620.00 USD | `-41.37%` | `312.94` |
| `Live` | `Long` | `5.18` | 1,920,000.00 USD | 0.00 USD | 150.57 USD | `-41.26%` | `29.04` |
| `Live` | `Long` | `5.21` | 1,920,000.00 USD | 0.00 USD | 300.91 USD | `-40.92%` | `57.70` |
| `Live` | `Long` | `5.29` | 1,920,000.00 USD | 0.00 USD | 640.70 USD | `-40.13%` | `121.23` |
| `Live` | `Long` | `5.30` | 1,920,000.00 USD | 0.00 USD | 232.41 USD | `-39.90%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,920,000.00 USD | 0.00 USD | 716.11 USD | `-39.67%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,920,000.00 USD | 0.00 USD | 660.46 USD | `-38.88%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,920,000.00 USD | 0.00 USD | 21,080.00 USD | `-38.65%` | `3,892.05` |
| `Live` | `Long` | `5.42` | 1,900,000.00 USD | 0.00 USD | 160,400.00 USD | `-38.54%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,740,000.00 USD | 0.00 USD | 1,360.00 USD | `-38.43%` | `250.00` |
| `Live` | `Long` | `5.46` | 1,740,000.00 USD | 0.00 USD | 264.72 USD | `-38.09%` | `48.44` |
| `Live` | `Long` | `5.49` | 1,740,000.00 USD | 0.00 USD | 354.06 USD | `-37.86%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,740,000.00 USD | 0.00 USD | 19,290.00 USD | `-37.75%` | `3,510.41` |
| `Live` | `Long` | `5.51` | 1,720,000.00 USD | 0.00 USD | 367.41 USD | `-37.52%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,720,000.00 USD | 0.00 USD | 121.38 USD | `-37.29%` | `21.93` |
| `Live` | `Long` | `5.57` | 1,720,000.00 USD | 0.00 USD | 967.98 USD | `-36.95%` | `173.94` |
| `Live` | `Long` | `5.58` | 1,720,000.00 USD | 0.00 USD | 63,260.00 USD | `-36.84%` | `11,347.58` |
| `Live` | `Long` | `5.59` | 1,650,000.00 USD | 0.00 USD | 34,430.00 USD | `-36.61%` | `6,153.60` |
| `Live` | `Long` | `5.63` | 1,620,000.00 USD | 0.00 USD | 468.55 USD | `-36.16%` | `83.15` |
| `Live` | `Long` | `5.70` | 1,620,000.00 USD | 0.00 USD | 405.03 USD | `-35.48%` | `71.12` |
| `Live` | `Long` | `5.71` | 1,620,000.00 USD | 0.00 USD | 2,340.00 USD | `-35.37%` | `409.39` |
| `Live` | `Long` | `5.74` | 1,620,000.00 USD | 0.00 USD | 238.86 USD | `-35.03%` | `41.65` |
| `Live` | `Long` | `5.75` | 1,620,000.00 USD | 0.00 USD | 125.70 USD | `-34.92%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,620,000.00 USD | 0.00 USD | 3,190.00 USD | `-34.80%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,610,000.00 USD | 0.00 USD | 10,850.00 USD | `-34.69%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,600,000.00 USD | 0.00 USD | 801.40 USD | `-34.58%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,600,000.00 USD | 0.00 USD | 2,890.00 USD | `-34.46%` | `500.00` |
| `Live` | `Long` | `5.79` | 1,600,000.00 USD | 0.00 USD | 5,140.00 USD | `-34.35%` | `886.37` |
| `Live` | `Long` | `5.80` | 1,590,000.00 USD | 0.00 USD | 580.50 USD | `-34.24%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,590,000.00 USD | 0.00 USD | 106.65 USD | `-34.12%` | `18.34` |
| `Live` | `Long` | `5.89` | 1,590,000.00 USD | 0.00 USD | 22,060.00 USD | `-33.22%` | `3,742.70` |
| `Live` | `Long` | `5.91` | 1,570,000.00 USD | 0.00 USD | 1,910.00 USD | `-33.10%` | `323.80` |
| `Live` | `Long` | `5.96` | 1,570,000.00 USD | 0.00 USD | 11,720.00 USD | `-32.54%` | `1,968.19` |
| `Live` | `Long` | `5.97` | 1,560,000.00 USD | 0.00 USD | 585.97 USD | `-32.31%` | `98.07` |
| `Live` | `Long` | `5.99` | 1,560,000.00 USD | 0.00 USD | 447.98 USD | `-32.20%` | `74.85` |
| `Live` | `Long` | `6.00` | 1,560,000.00 USD | 0.00 USD | 341.56 USD | `-31.97%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,560,000.00 USD | 0.00 USD | 446.85 USD | `-31.86%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,550,000.00 USD | 0.00 USD | 1,690.00 USD | `-31.63%` | `280.10` |
| `Live` | `Long` | `6.04` | 1,550,000.00 USD | 0.00 USD | 448.72 USD | `-31.52%` | `74.23` |
| `Live` | `Long` | `6.05` | 1,550,000.00 USD | 0.00 USD | 1,310.00 USD | `-31.40%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,550,000.00 USD | 0.00 USD | 672.24 USD | `-31.29%` | `110.84` |
| `Live` | `Long` | `6.08` | 1,550,000.00 USD | 0.00 USD | 1,690.00 USD | `-31.18%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,550,000.00 USD | 0.00 USD | 405.14 USD | `-31.06%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,550,000.00 USD | 0.00 USD | 4,220.00 USD | `-30.95%` | `692.81` |
| `Live` | `Long` | `6.11` | 1,540,000.00 USD | 0.00 USD | 3,200.00 USD | `-30.84%` | `524.73` |
| `Live` | `Long` | `6.12` | 1,540,000.00 USD | 0.00 USD | 2,360.00 USD | `-30.72%` | `386.46` |
| `Live` | `Long` | `6.12` | 1,540,000.00 USD | 0.00 USD | 137.02 USD | `-30.61%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,540,000.00 USD | 0.00 USD | 809.21 USD | `-30.50%` | `131.90` |
| `Live` | `Long` | `6.14` | 1,540,000.00 USD | 0.00 USD | 238.61 USD | `-30.38%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,540,000.00 USD | 0.00 USD | 4,390.00 USD | `-30.27%` | `713.75` |
| `Live` | `Long` | `6.17` | 1,530,000.00 USD | 0.00 USD | 345,790.00 USD | `-30.16%` | `56,089.78` |
| `Live` | `Long` | `6.17` | 1,190,000.00 USD | 0.00 USD | 104.36 USD | `-30.04%` | `16.90` |
| `Live` | `Long` | `6.18` | 1,190,000.00 USD | 0.00 USD | 1,440.00 USD | `-29.93%` | `232.17` |
| `Live` | `Long` | `6.21` | 1,190,000.00 USD | 0.00 USD | 310.25 USD | `-29.70%` | `50.00` |
| `Live` | `Long` | `6.21` | 1,190,000.00 USD | 0.00 USD | 2,560.00 USD | `-29.59%` | `411.30` |
| `Live` | `Long` | `6.22` | 1,180,000.00 USD | 0.00 USD | 715.31 USD | `-29.48%` | `114.91` |
| `Live` | `Long` | `6.25` | 1,180,000.00 USD | 0.00 USD | 971.10 USD | `-29.25%` | `155.50` |
| `Live` | `Long` | `6.28` | 1,180,000.00 USD | 0.00 USD | 2,510.00 USD | `-28.91%` | `400.00` |
| `Live` | `Long` | `6.32` | 1,180,000.00 USD | 0.00 USD | 277.04 USD | `-28.46%` | `43.87` |
| `Live` | `Long` | `6.33` | 1,180,000.00 USD | 0.00 USD | 105.25 USD | `-28.34%` | `16.64` |
| `Live` | `Long` | `6.34` | 1,180,000.00 USD | 0.00 USD | 248.79 USD | `-28.12%` | `39.21` |
| `Live` | `Long` | `6.36` | 1,180,000.00 USD | 0.00 USD | 4,220.00 USD | `-28.00%` | `664.12` |
| `Live` | `Long` | `6.37` | 1,170,000.00 USD | 0.00 USD | 284,770.00 USD | `-27.89%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 889,150.00 USD | 0.00 USD | 5,110.00 USD | `-27.78%` | `801.31` |
| `Live` | `Long` | `6.42` | 884,040.00 USD | 0.00 USD | 2,010.00 USD | `-27.33%` | `312.90` |
| `Live` | `Long` | `6.43` | 882,040.00 USD | 0.00 USD | 6,780.00 USD | `-27.10%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 875,260.00 USD | 0.00 USD | 1,050.00 USD | `-26.76%` | `162.75` |
| `Live` | `Long` | `6.54` | 874,210.00 USD | 0.00 USD | 3,620.00 USD | `-25.97%` | `554.55` |
| `Live` | `Long` | `6.54` | 870,580.00 USD | 0.00 USD | 11,130.00 USD | `-25.85%` | `1,700.89` |
| `Live` | `Long` | `6.58` | 859,450.00 USD | 0.00 USD | 3,170.00 USD | `-25.51%` | `482.43` |
| `Live` | `Long` | `6.58` | 856,280.00 USD | 0.00 USD | 1,100.00 USD | `-25.40%` | `166.55` |
| `Live` | `Long` | `6.62` | 855,180.00 USD | 0.00 USD | 2,110.00 USD | `-25.06%` | `318.57` |
| `Live` | `Long` | `6.70` | 853,080.00 USD | 0.00 USD | 506.54 USD | `-24.15%` | `75.66` |
| `Live` | `Long` | `6.71` | 852,570.00 USD | 0.00 USD | 16,610.00 USD | `-24.04%` | `2,477.79` |
| `Live` | `Long` | `6.75` | 835,960.00 USD | 0.00 USD | 1,330.00 USD | `-23.59%` | `196.95` |
| `Live` | `Long` | `6.76` | 834,630.00 USD | 0.00 USD | 15,310.00 USD | `-23.36%` | `2,262.66` |
| `Live` | `Long` | `6.78` | 819,320.00 USD | 0.00 USD | 6,780.00 USD | `-23.25%` | `1,000.00` |
| `Live` | `Long` | `6.79` | 812,550.00 USD | 0.00 USD | 16,960.00 USD | `-23.13%` | `2,500.00` |
| `Live` | `Long` | `6.79` | 795,580.00 USD | 0.00 USD | 4,260.00 USD | `-23.02%` | `626.24` |
| `Live` | `Long` | `6.80` | 791,330.00 USD | 0.00 USD | 28,720.00 USD | `-22.91%` | `4,220.95` |
| `Live` | `Long` | `6.82` | 762,600.00 USD | 0.00 USD | 2,820.00 USD | `-22.79%` | `414.28` |
| `Live` | `Long` | `6.83` | 759,780.00 USD | 0.00 USD | 4,410.00 USD | `-22.57%` | `644.73` |
| `Live` | `Long` | `6.86` | 755,370.00 USD | 0.00 USD | 18,930.00 USD | `-22.34%` | `2,761.63` |
| `Live` | `Long` | `6.87` | 736,440.00 USD | 0.00 USD | 3,770.00 USD | `-22.23%` | `548.46` |
| `Live` | `Long` | `6.89` | 732,680.00 USD | 0.00 USD | 5,250.00 USD | `-21.89%` | `761.63` |
| `Live` | `Long` | `6.91` | 727,430.00 USD | 0.00 USD | 269.30 USD | `-21.77%` | `39.00` |
| `Live` | `Long` | `6.92` | 727,160.00 USD | 0.00 USD | 1,390.00 USD | `-21.55%` | `200.00` |
| `Live` | `Long` | `6.95` | 725,770.00 USD | 0.00 USD | 3,760.00 USD | `-21.32%` | `541.68` |
| `Live` | `Long` | `6.96` | 722,010.00 USD | 0.00 USD | 3,480.00 USD | `-21.21%` | `500.00` |
| `Live` | `Long` | `6.96` | 718,530.00 USD | 0.00 USD | 636.74 USD | `-21.09%` | `91.42` |
| `Live` | `Long` | `7.00` | 717,900.00 USD | 0.00 USD | 746.58 USD | `-20.75%` | `106.73` |
| `Live` | `Long` | `7.00` | 717,150.00 USD | 0.00 USD | 20,860.00 USD | `-20.64%` | `2,978.11` |
| `Live` | `Long` | `7.04` | 696,290.00 USD | 0.00 USD | 4,100.00 USD | `-20.19%` | `581.44` |
| `Live` | `Long` | `7.08` | 692,190.00 USD | 0.00 USD | 6,700.00 USD | `-19.85%` | `947.44` |
| `Live` | `Long` | `7.08` | 685,490.00 USD | 0.00 USD | 1,670.00 USD | `-19.73%` | `236.20` |
| `Live` | `Long` | `7.12` | 683,810.00 USD | 0.00 USD | 379.66 USD | `-19.40%` | `53.36` |
| `Live` | `Long` | `7.12` | 683,440.00 USD | 0.00 USD | 821.73 USD | `-19.28%` | `115.33` |
| `Live` | `Long` | `7.13` | 682,610.00 USD | 0.00 USD | 2,410.00 USD | `-19.17%` | `337.38` |
| `Live` | `Long` | `7.14` | 680,210.00 USD | 0.00 USD | 20,950.00 USD | `-19.06%` | `2,931.56` |
| `Live` | `Long` | `7.18` | 659,260.00 USD | 0.00 USD | 1,440.00 USD | `-18.60%` | `200.00` |
| `Live` | `Long` | `7.21` | 657,820.00 USD | 0.00 USD | 257.72 USD | `-18.38%` | `35.77` |
| `Live` | `Long` | `7.21` | 657,570.00 USD | 0.00 USD | 322.94 USD | `-18.26%` | `44.76` |
| `Live` | `Long` | `7.24` | 657,240.00 USD | 0.00 USD | 179.65 USD | `-18.04%` | `24.83` |
| `Live` | `Long` | `7.25` | 657,060.00 USD | 0.00 USD | 185.83 USD | `-17.92%` | `25.65` |
| `Live` | `Long` | `7.26` | 656,880.00 USD | 0.00 USD | 1,020.00 USD | `-17.70%` | `140.00` |
| `Live` | `Long` | `7.29` | 655,860.00 USD | 0.00 USD | 36,420.00 USD | `-17.47%` | `5,000.00` |
| `Live` | `Long` | `7.32` | 619,440.00 USD | 0.00 USD | 1,760.00 USD | `-17.13%` | `240.77` |
| `Live` | `Long` | `7.33` | 617,670.00 USD | 0.00 USD | 4,910.00 USD | `-17.02%` | `669.93` |
| `Live` | `Long` | `7.33` | 612,770.00 USD | 0.00 USD | 2,450.00 USD | `-16.90%` | `333.54` |
| `Live` | `Long` | `7.34` | 610,320.00 USD | 0.00 USD | 4,370.00 USD | `-16.79%` | `594.84` |
| `Live` | `Long` | `7.37` | 605,950.00 USD | 0.00 USD | 5,720.00 USD | `-16.56%` | `776.95` |
| `Live` | `Long` | `7.38` | 600,230.00 USD | 0.00 USD | 3,920.00 USD | `-16.45%` | `531.65` |
| `Live` | `Long` | `7.38` | 596,310.00 USD | 0.00 USD | 18,090.00 USD | `-16.34%` | `2,450.10` |
| `Live` | `Long` | `7.39` | 578,210.00 USD | 0.00 USD | 1,550.00 USD | `-16.22%` | `210.17` |
| `Live` | `Long` | `7.41` | 576,660.00 USD | 0.00 USD | 1,480.00 USD | `-16.11%` | `200.00` |
| `Live` | `Long` | `7.42` | 575,180.00 USD | 0.00 USD | 147.41 USD | `-16.00%` | `19.88` |
| `Live` | `Long` | `7.42` | 575,030.00 USD | 0.00 USD | 352.39 USD | `-15.88%` | `47.46` |
| `Live` | `Long` | `7.45` | 574,680.00 USD | 0.00 USD | 210.99 USD | `-15.66%` | `28.34` |
| `Live` | `Long` | `7.46` | 574,470.00 USD | 0.00 USD | 1,370.00 USD | `-15.54%` | `183.84` |
| `Live` | `Long` | `7.46` | 573,100.00 USD | 0.00 USD | 4,590.00 USD | `-15.43%` | `614.36` |
| `Live` | `Long` | `7.47` | 568,510.00 USD | 0.00 USD | 3,210.00 USD | `-15.32%` | `430.09` |
| `Live` | `Long` | `7.49` | 565,300.00 USD | 0.00 USD | 322.45 USD | `-15.20%` | `43.08` |
| `Live` | `Long` | `7.50` | 564,970.00 USD | 0.00 USD | 1,580.00 USD | `-15.09%` | `211.22` |
| `Live` | `Long` | `7.50` | 563,390.00 USD | 0.00 USD | 656.99 USD | `-14.98%` | `87.54` |
| `Live` | `Long` | `7.53` | 562,730.00 USD | 0.00 USD | 433.52 USD | `-14.75%` | `57.61` |
| `Live` | `Long` | `7.54` | 562,300.00 USD | 0.00 USD | 4,210.00 USD | `-14.64%` | `559.01` |
| `Live` | `Long` | `7.54` | 558,090.00 USD | 0.00 USD | 844.21 USD | `-14.52%` | `111.89` |
| `Live` | `Long` | `7.55` | 557,240.00 USD | 0.00 USD | 1,310.00 USD | `-14.41%` | `173.59` |
| `Live` | `Long` | `7.57` | 555,930.00 USD | 0.00 USD | 4,380.00 USD | `-14.30%` | `578.50` |
| `Live` | `Long` | `7.59` | 551,560.00 USD | 0.00 USD | 25,140.00 USD | `-13.96%` | `3,310.14` |
| `Live` | `Long` | `7.62` | 526,420.00 USD | 0.00 USD | 312.22 USD | `-13.73%` | `41.00` |
| `Live` | `Long` | `7.62` | 526,100.00 USD | 0.00 USD | 787.51 USD | `-13.62%` | `103.28` |
| `Live` | `Long` | `7.63` | 525,320.00 USD | 0.00 USD | 378.93 USD | `-13.50%` | `49.63` |
| `Live` | `Long` | `7.66` | 524,940.00 USD | 0.00 USD | 135.42 USD | `-13.28%` | `17.69` |
| `Live` | `Long` | `7.67` | 524,800.00 USD | 0.00 USD | 1,740.00 USD | `-13.16%` | `226.45` |
| `Live` | `Long` | `7.68` | 523,070.00 USD | 0.00 USD | 1,120.00 USD | `-12.94%` | `145.25` |
| `Live` | `Long` | `7.70` | 521,950.00 USD | 0.00 USD | 1,460.00 USD | `-12.82%` | `190.36` |
| `Live` | `Long` | `7.71` | 520,480.00 USD | 0.00 USD | 19,410.00 USD | `-12.71%` | `2,518.82` |
| `Live` | `Long` | `7.72` | 501,080.00 USD | 0.00 USD | 2,550.00 USD | `-12.48%` | `330.65` |
| `Live` | `Long` | `7.75` | 498,520.00 USD | 0.00 USD | 1,820.00 USD | `-12.14%` | `235.11` |
| `Live` | `Long` | `7.76` | 496,700.00 USD | 0.00 USD | 455.73 USD | `-12.03%` | `58.69` |
| `Live` | `Long` | `7.78` | 496,240.00 USD | 0.00 USD | 2,810.00 USD | `-11.92%` | `361.33` |
| `Live` | `Long` | `7.79` | 493,430.00 USD | 0.00 USD | 1,780.00 USD | `-11.80%` | `228.67` |
| `Live` | `Long` | `7.79` | 491,650.00 USD | 0.00 USD | 1,940.00 USD | `-11.69%` | `248.84` |
| `Live` | `Long` | `7.80` | 489,710.00 USD | 0.00 USD | 633.77 USD | `-11.58%` | `81.20` |
| `Live` | `Long` | `7.82` | 489,080.00 USD | 0.00 USD | 5,280.00 USD | `-11.46%` | `675.43` |
| `Live` | `Long` | `7.83` | 483,800.00 USD | 0.00 USD | 160.30 USD | `-11.24%` | `20.46` |
| `Live` | `Long` | `7.84` | 483,640.00 USD | 0.00 USD | 10,930.00 USD | `-11.12%` | `1,393.53` |
| `Live` | `Long` | `7.86` | 472,710.00 USD | 0.00 USD | 2,110.00 USD | `-11.01%` | `269.14` |
| `Live` | `Long` | `7.88` | 470,600.00 USD | 0.00 USD | 1,080.00 USD | `-10.79%` | `137.44` |
| `Live` | `Long` | `7.91` | 469,510.00 USD | 0.00 USD | 505.13 USD | `-10.45%` | `63.90` |
| `Live` | `Long` | `7.92` | 469,010.00 USD | 0.00 USD | 923.42 USD | `-10.22%` | `116.52` |
| `Live` | `Long` | `7.93` | 468,080.00 USD | 0.00 USD | 1,820.00 USD | `-10.11%` | `228.88` |
| `Live` | `Long` | `7.95` | 466,270.00 USD | 0.00 USD | 129,030.00 USD | `-9.99%` | `16,240.19` |
| `Live` | `Long` | `7.96` | 337,240.00 USD | 0.00 USD | 1,140.00 USD | `-9.88%` | `143.40` |
| `Live` | `Long` | `7.99` | 336,100.00 USD | 0.00 USD | 1,970.00 USD | `-9.54%` | `246.41` |
| `Live` | `Long` | `8.00` | 334,130.00 USD | 0.00 USD | 210.99 USD | `-9.43%` | `26.39` |
| `Live` | `Long` | `8.02` | 333,920.00 USD | 0.00 USD | 1,530.00 USD | `-9.20%` | `191.35` |
| `Live` | `Long` | `8.03` | 332,390.00 USD | 0.00 USD | 957.70 USD | `-9.09%` | `119.34` |
| `Live` | `Long` | `8.04` | 331,430.00 USD | 0.00 USD | 88,380.00 USD | `-8.97%` | `10,999.50` |
| `Live` | `Long` | `8.04` | 243,050.00 USD | 0.00 USD | 12,840.00 USD | `-8.86%` | `1,595.44` |
| `Live` | `Long` | `8.05` | 230,210.00 USD | 0.00 USD | 3,340.00 USD | `-8.75%` | `414.27` |
| `Live` | `Long` | `8.06` | 226,880.00 USD | 0.00 USD | 37,830.00 USD | `-8.63%` | `4,690.67` |
| `Live` | `Long` | `8.09` | 189,050.00 USD | 0.00 USD | 617.61 USD | `-8.41%` | `76.39` |
| `Live` | `Long` | `8.12` | 188,430.00 USD | 0.00 USD | 241.26 USD | `-8.07%` | `29.73` |
| `Live` | `Long` | `8.14` | 188,190.00 USD | 0.00 USD | 11,610.00 USD | `-7.73%` | `1,425.26` |
| `Live` | `Long` | `8.16` | 176,580.00 USD | 0.00 USD | 871.61 USD | `-7.50%` | `106.75` |
| `Live` | `Long` | `8.19` | 175,710.00 USD | 0.00 USD | 31,640.00 USD | `-7.27%` | `3,865.53` |
| `Live` | `Long` | `8.20` | 144,070.00 USD | 0.00 USD | 1,740.00 USD | `-7.16%` | `211.86` |
| `Live` | `Long` | `8.21` | 142,330.00 USD | 0.00 USD | 577.06 USD | `-7.05%` | `70.33` |
| `Live` | `Long` | `8.21` | 141,750.00 USD | 0.00 USD | 565.68 USD | `-6.93%` | `68.86` |
| `Live` | `Long` | `8.22` | 141,190.00 USD | 0.00 USD | 2,100.00 USD | `-6.82%` | `255.16` |
| `Live` | `Long` | `8.23` | 139,090.00 USD | 0.00 USD | 1,530.00 USD | `-6.71%` | `185.53` |
| `Live` | `Long` | `8.24` | 137,560.00 USD | 0.00 USD | 1,120.00 USD | `-6.59%` | `135.66` |
| `Live` | `Long` | `8.26` | 136,440.00 USD | 0.00 USD | 21,400.00 USD | `-6.48%` | `2,591.96` |
| `Live` | `Long` | `8.27` | 115,050.00 USD | 0.00 USD | 2,160.00 USD | `-6.37%` | `261.48` |
| `Live` | `Long` | `8.28` | 112,890.00 USD | 0.00 USD | 1,190.00 USD | `-6.25%` | `144.16` |
| `Live` | `Long` | `8.29` | 111,690.00 USD | 0.00 USD | 498.26 USD | `-6.14%` | `60.14` |
| `Live` | `Long` | `8.29` | 111,190.00 USD | 0.00 USD | 23,710.00 USD | `-6.03%` | `2,858.11` |
| `Live` | `Long` | `8.30` | 87,490.00 USD | 0.00 USD | 34,320.00 USD | `-5.91%` | `4,132.87` |
| `Live` | `Long` | `8.31` | 53,160.00 USD | 0.00 USD | 4,730.00 USD | `-5.80%` | `568.64` |
| `Live` | `Long` | `8.34` | 48,430.00 USD | 0.00 USD | 945.86 USD | `-5.57%` | `113.48` |
| `Live` | `Long` | `8.35` | 47,490.00 USD | 0.00 USD | 185.09 USD | `-5.46%` | `22.18` |
| `Live` | `Long` | `8.36` | 47,300.00 USD | 0.00 USD | 3,410.00 USD | `-5.35%` | `407.63` |
| `Live` | `Long` | `8.37` | 43,900.00 USD | 0.00 USD | 7,410.00 USD | `-5.23%` | `886.24` |
| `Live` | `Long` | `8.38` | 36,480.00 USD | 0.00 USD | 955.89 USD | `-5.01%` | `114.00` |
| `Live` | `Long` | `8.39` | 35,530.00 USD | 0.00 USD | 1,680.00 USD | `-4.89%` | `200.00` |
| `Live` | `Long` | `8.40` | 33,850.00 USD | 0.00 USD | 608.02 USD | `-4.78%` | `72.34` |
| `Live` | `Long` | `8.41` | 33,240.00 USD | 0.00 USD | 102.33 USD | `-4.67%` | `12.16` |
| `Live` | `Long` | `8.43` | 33,140.00 USD | 0.00 USD | 674.00 USD | `-4.55%` | `80.00` |
| `Live` | `Long` | `8.44` | 32,470.00 USD | 0.00 USD | 188.61 USD | `-4.44%` | `22.36` |
| `Live` | `Long` | `8.45` | 32,280.00 USD | 0.00 USD | 588.70 USD | `-4.33%` | `69.71` |
| `Live` | `Long` | `8.46` | 31,690.00 USD | 0.00 USD | 226.93 USD | `-4.21%` | `26.84` |
| `Live` | `Long` | `8.47` | 31,460.00 USD | 0.00 USD | 12,430.00 USD | `-3.99%` | `1,466.22` |
| `Live` | `Long` | `8.48` | 19,040.00 USD | 0.00 USD | 1,850.00 USD | `-3.87%` | `218.58` |
| `Live` | `Long` | `8.49` | 17,180.00 USD | 0.00 USD | 205.24 USD | `-3.76%` | `24.16` |
| `Live` | `Long` | `8.51` | 16,980.00 USD | 0.00 USD | 5,770.00 USD | `-3.65%` | `677.95` |
| `Live` | `Long` | `8.52` | 11,210.00 USD | 0.00 USD | 2,260.00 USD | `-3.53%` | `264.85` |
| `Live` | `Long` | `8.54` | 8,950.00 USD | 0.00 USD | 6,350.00 USD | `-3.31%` | `743.78` |
| `Live` | `Long` | `8.54` | 2,610.00 USD | 0.00 USD | 1,550.00 USD | `-3.19%` | `180.95` |
| `Live` | `Long` | `8.55` | 1,060.00 USD | 0.00 USD | 1,060.00 USD | `-3.08%` | `123.86` |
| `Live` | `Short` | `9.11` | 783.94 USD | 783.94 USD | 0.00 USD | `+3.15%` | `86.10` |
| `Live` | `Short` | `9.13` | 1,100.00 USD | 314.34 USD | 0.00 USD | `+3.49%` | `34.41` |
| `Live` | `Short` | `9.14` | 5,290.00 USD | 4,190.00 USD | 0.00 USD | `+3.60%` | `458.50` |
| `Live` | `Short` | `9.21` | 5,500.00 USD | 209.36 USD | 0.00 USD | `+4.40%` | `22.72` |
| `Live` | `Short` | `9.29` | 11,650.00 USD | 6,150.00 USD | 0.00 USD | `+5.19%` | `662.64` |
| `Live` | `Short` | `9.41` | 12,090.00 USD | 440.06 USD | 0.00 USD | `+6.66%` | `46.74` |
| `Live` | `Short` | `9.69` | 12,630.00 USD | 533.26 USD | 0.00 USD | `+9.72%` | `55.06` |
| `Live` | `Short` | `9.73` | 12,820.00 USD | 192.95 USD | 0.00 USD | `+10.29%` | `19.82` |
| `Live` | `Short` | `9.80` | 306,980.00 USD | 294,160.00 USD | 0.00 USD | `+11.08%` | `30,000.83` |
| `Live` | `Short` | `9.88` | 307,530.00 USD | 555.86 USD | 0.00 USD | `+11.87%` | `56.29` |
| `Live` | `Short` | `9.88` | 308,770.00 USD | 1,230.00 USD | 0.00 USD | `+11.99%` | `124.89` |
| `Live` | `Short` | `10.21` | 312,870.00 USD | 4,100.00 USD | 0.00 USD | `+15.72%` | `401.08` |
| `Live` | `Short` | `10.27` | 313,200.00 USD | 331.15 USD | 0.00 USD | `+16.29%` | `32.26` |
| `Live` | `Short` | `10.32` | 333,850.00 USD | 20,650.00 USD | 0.00 USD | `+16.97%` | `2,000.00` |
| `Live` | `Short` | `10.35` | 337,230.00 USD | 3,380.00 USD | 0.00 USD | `+17.20%` | `326.92` |
| `Live` | `Short` | `10.36` | 338,360.00 USD | 1,130.00 USD | 0.00 USD | `+17.31%` | `109.45` |
| `Live` | `Short` | `10.54` | 374,880.00 USD | 36,510.00 USD | 0.00 USD | `+19.46%` | `3,462.73` |
| `Live` | `Short` | `10.56` | 375,400.00 USD | 523.81 USD | 0.00 USD | `+19.69%` | `49.58` |
| `Live` | `Short` | `10.71` | 375,620.00 USD | 218.91 USD | 0.00 USD | `+21.39%` | `20.43` |
| `Live` | `Short` | `10.96` | 377,530.00 USD | 1,920.00 USD | 0.00 USD | `+24.22%` | `174.67` |
| `Live` | `Short` | `11.01` | 384,500.00 USD | 6,970.00 USD | 0.00 USD | `+24.67%` | `633.00` |
| `Live` | `Short` | `11.15` | 384,770.00 USD | 266.49 USD | 0.00 USD | `+26.37%` | `23.89` |
| `Live` | `Short` | `11.27` | 396,440.00 USD | 11,670.00 USD | 0.00 USD | `+27.62%` | `1,035.87` |
| `Live` | `Short` | `11.54` | 396,560.00 USD | 125.84 USD | 0.00 USD | `+30.79%` | `10.90` |
| `Live` | `Short` | `11.62` | 408,700.00 USD | 12,140.00 USD | 0.00 USD | `+31.70%` | `1,043.90` |
| `Live` | `Short` | `11.66` | 411,930.00 USD | 3,240.00 USD | 0.00 USD | `+32.15%` | `277.54` |
| `Live` | `Short` | `11.79` | 412,720.00 USD | 784.88 USD | 0.00 USD | `+33.51%` | `66.60` |
| `Live` | `Short` | `11.88` | 472,140.00 USD | 59,430.00 USD | 0.00 USD | `+34.64%` | `5,000.00` |
| `Live` | `Short` | `12.18` | 473,530.00 USD | 1,390.00 USD | 0.00 USD | `+37.93%` | `113.77` |
| `Live` | `Short` | `12.27` | 474,250.00 USD | 723.51 USD | 0.00 USD | `+38.95%` | `58.99` |
| `Live` | `Short` | `12.30` | 475,980.00 USD | 1,730.00 USD | 0.00 USD | `+39.40%` | `140.71` |
| `Live` | `Short` | `12.40` | 476,330.00 USD | 343.62 USD | 0.00 USD | `+40.53%` | `27.70` |
| `Live` | `Short` | `12.54` | 512,430.00 USD | 36,100.00 USD | 0.00 USD | `+42.01%` | `2,879.71` |
| `Live` | `Short` | `12.70` | 526,650.00 USD | 14,220.00 USD | 0.00 USD | `+43.82%` | `1,120.14` |
| `Live` | `Short` | `12.77` | 527,080.00 USD | 435.29 USD | 0.00 USD | `+44.61%` | `34.10` |
| `Live` | `Short` | `12.79` | 528,030.00 USD | 953.38 USD | 0.00 USD | `+44.84%` | `74.57` |
| `Live` | `Short` | `13.20` | 615,980.00 USD | 87,940.00 USD | 0.00 USD | `+49.48%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 854,780.00 USD | 238,800.00 USD | 0.00 USD | `+50.50%` | `17,975.23` |
| `Live` | `Short` | `13.31` | 855,000.00 USD | 218.50 USD | 0.00 USD | `+50.84%` | `16.41` |
| `Live` | `Short` | `13.46` | 855,430.00 USD | 430.34 USD | 0.00 USD | `+52.54%` | `31.96` |
| `Live` | `Short` | `13.54` | 855,720.00 USD | 291.68 USD | 0.00 USD | `+53.34%` | `21.55` |
| `Live` | `Short` | `13.69` | 855,890.00 USD | 172.29 USD | 0.00 USD | `+55.04%` | `12.59` |
| `Live` | `Short` | `13.76` | 859,040.00 USD | 3,150.00 USD | 0.00 USD | `+55.83%` | `228.83` |
| `Live` | `Short` | `14.02` | 859,320.00 USD | 276.52 USD | 0.00 USD | `+58.77%` | `19.73` |
| `Live` | `Short` | `14.28` | 974,070.00 USD | 114,750.00 USD | 0.00 USD | `+61.72%` | `8,038.77` |
| `Live` | `Short` | `14.66` | 974,890.00 USD | 823.29 USD | 0.00 USD | `+66.14%` | `56.14` |
| `Live` | `Short` | `14.85` | 977,360.00 USD | 2,470.00 USD | 0.00 USD | `+68.18%` | `166.16` |
| `Live` | `Short` | `15.29` | 977,590.00 USD | 229.43 USD | 0.00 USD | `+73.28%` | `15.00` |
| `Live` | `Short` | `15.32` | 989,690.00 USD | 12,100.00 USD | 0.00 USD | `+73.62%` | `789.80` |
| `Live` | `Short` | `15.35` | 989,920.00 USD | 230.17 USD | 0.00 USD | `+73.84%` | `15.00` |
| `Live` | `Short` | `15.38` | 1,010,000.00 USD | 20,000.00 USD | 0.00 USD | `+74.29%` | `1,300.00` |
| `Live` | `Short` | `15.40` | 1,160,000.00 USD | 154,050.00 USD | 0.00 USD | `+74.52%` | `10,000.00` |
| `Live` | `Short` | `15.41` | 1,190,000.00 USD | 23,170.00 USD | 0.00 USD | `+74.63%` | `1,502.91` |
| `Live` | `Short` | `15.52` | 1,190,000.00 USD | 110.31 USD | 0.00 USD | `+75.77%` | `7.11` |
| `Live` | `Short` | `15.81` | 1,440,000.00 USD | 256,330.00 USD | 0.00 USD | `+79.17%` | `16,208.00` |
| `Live` | `Short` | `16.09` | 1,520,000.00 USD | 81,030.00 USD | 0.00 USD | `+82.22%` | `5,037.66` |
| `Live` | `Short` | `16.27` | 1,530,000.00 USD | 1,500.00 USD | 0.00 USD | `+84.38%` | `92.02` |
| `Live` | `Short` | `16.48` | 1,530,000.00 USD | 122.81 USD | 0.00 USD | `+86.76%` | `7.45` |
| `Live` | `Short` | `16.52` | 1,530,000.00 USD | 190.91 USD | 0.00 USD | `+87.10%` | `11.56` |
| `Live` | `Short` | `16.55` | 1,530,000.00 USD | 188.78 USD | 0.00 USD | `+87.44%` | `11.41` |
| `Live` | `Short` | `16.64` | 1,530,000.00 USD | 945.10 USD | 0.00 USD | `+88.57%` | `56.78` |
| `Live` | `Short` | `16.75` | 1,530,000.00 USD | 162.26 USD | 0.00 USD | `+89.70%` | `9.69` |
| `Live` | `Short` | `17.02` | 1,530,000.00 USD | 191.87 USD | 0.00 USD | `+92.87%` | `11.27` |
| `Live` | `Short` | `17.14` | 1,530,000.00 USD | 1,710.00 USD | 0.00 USD | `+94.12%` | `100.00` |
| `Live` | `Short` | `17.46` | 1,530,000.00 USD | 101.47 USD | 0.00 USD | `+97.86%` | `5.81` |
| `Live` | `Short` | `17.62` | 1,530,000.00 USD | 4,120.00 USD | 0.00 USD | `+99.67%` | `233.67` |
| `Live` | `Short` | `17.64` | 1,540,000.00 USD | 6,530.00 USD | 0.00 USD | `+99.90%` | `370.06` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 333,490.00 USD | 0.00 USD | 611.73 USD | `-73.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 332,880.00 USD | 0.00 USD | 793.75 USD | `-54.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 332,090.00 USD | 0.00 USD | 105.04 USD | `-49.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 331,980.00 USD | 0.00 USD | 67,970.00 USD | `-43.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 264,020.00 USD | 0.00 USD | 205.30 USD | `-39.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 263,810.00 USD | 0.00 USD | 7,450.00 USD | `-38.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 256,360.00 USD | 0.00 USD | 349.35 USD | `-37.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 256,010.00 USD | 0.00 USD | 1,330.00 USD | `-34.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 254,690.00 USD | 0.00 USD | 493.50 USD | `-32.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 254,190.00 USD | 0.00 USD | 100.98 USD | `-32.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 254,090.00 USD | 0.00 USD | 620.80 USD | `-31.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 253,470.00 USD | 0.00 USD | 4,160.00 USD | `-30.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 249,320.00 USD | 0.00 USD | 6,500.00 USD | `-30.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 242,810.00 USD | 0.00 USD | 864.38 USD | `-28.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 241,950.00 USD | 0.00 USD | 1,430.00 USD | `-26.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 240,520.00 USD | 0.00 USD | 4,340.00 USD | `-25.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 236,180.00 USD | 0.00 USD | 5,520.00 USD | `-24.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 230,660.00 USD | 0.00 USD | 100.72 USD | `-23.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 230,550.00 USD | 0.00 USD | 296.34 USD | `-23.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 230,260.00 USD | 0.00 USD | 921.19 USD | `-23.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 229,340.00 USD | 0.00 USD | 709.98 USD | `-21.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 228,630.00 USD | 0.00 USD | 262.44 USD | `-21.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 228,360.00 USD | 0.00 USD | 3,610.00 USD | `-20.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 224,750.00 USD | 0.00 USD | 6,790.00 USD | `-18.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 217,960.00 USD | 0.00 USD | 9,770.00 USD | `-18.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 208,190.00 USD | 0.00 USD | 103.46 USD | `-18.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 208,090.00 USD | 0.00 USD | 603.44 USD | `-17.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 207,490.00 USD | 0.00 USD | 891.57 USD | `-17.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 206,590.00 USD | 0.00 USD | 2,090.00 USD | `-17.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 204,500.00 USD | 0.00 USD | 129.58 USD | `-17.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 204,370.00 USD | 0.00 USD | 236.19 USD | `-16.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 204,140.00 USD | 0.00 USD | 199.39 USD | `-15.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 203,940.00 USD | 0.00 USD | 4,730.00 USD | `-15.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 199,200.00 USD | 0.00 USD | 37,420.00 USD | `-15.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 161,780.00 USD | 0.00 USD | 799.83 USD | `-14.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 160,980.00 USD | 0.00 USD | 103.41 USD | `-14.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 160,880.00 USD | 0.00 USD | 1,370.00 USD | `-14.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 159,500.00 USD | 0.00 USD | 1,000.00 USD | `-13.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 158,500.00 USD | 0.00 USD | 360.13 USD | `-12.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 158,140.00 USD | 0.00 USD | 175.42 USD | `-12.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 157,960.00 USD | 0.00 USD | 2,990.00 USD | `-11.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 154,970.00 USD | 0.00 USD | 143.51 USD | `-11.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 154,820.00 USD | 0.00 USD | 183.33 USD | `-10.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.88` | 154,640.00 USD | 0.00 USD | 194.52 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 154,450.00 USD | 0.00 USD | 1,090.00 USD | `-10.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 153,350.00 USD | 0.00 USD | 1,350.00 USD | `-10.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 152,010.00 USD | 0.00 USD | 1,590.00 USD | `-10.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 150,420.00 USD | 0.00 USD | 898.42 USD | `-9.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.97` | 149,520.00 USD | 0.00 USD | 107.74 USD | `-9.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 149,410.00 USD | 0.00 USD | 1,350.00 USD | `-9.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 148,070.00 USD | 0.00 USD | 7,930.00 USD | `-9.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 140,130.00 USD | 0.00 USD | 123.58 USD | `-8.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 140,010.00 USD | 0.00 USD | 2,110.00 USD | `-8.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 137,900.00 USD | 0.00 USD | 563.85 USD | `-8.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 137,340.00 USD | 0.00 USD | 105.14 USD | `-8.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 137,230.00 USD | 0.00 USD | 367.76 USD | `-8.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 136,860.00 USD | 0.00 USD | 2,330.00 USD | `-8.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 134,530.00 USD | 0.00 USD | 120.10 USD | `-8.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 134,410.00 USD | 0.00 USD | 6,500.00 USD | `-7.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 127,910.00 USD | 0.00 USD | 462.15 USD | `-7.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 127,450.00 USD | 0.00 USD | 654.53 USD | `-7.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 126,790.00 USD | 0.00 USD | 520.75 USD | `-7.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 126,270.00 USD | 0.00 USD | 725.60 USD | `-7.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 125,550.00 USD | 0.00 USD | 141.04 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 125,400.00 USD | 0.00 USD | 1,780.00 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.22` | 123,620.00 USD | 0.00 USD | 165.40 USD | `-6.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 123,450.00 USD | 0.00 USD | 143.54 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 123,310.00 USD | 0.00 USD | 168.64 USD | `-6.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 123,140.00 USD | 0.00 USD | 950.46 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 122,190.00 USD | 0.00 USD | 6,530.00 USD | `-5.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 115,670.00 USD | 0.00 USD | 1,140.00 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 114,520.00 USD | 0.00 USD | 2,000.00 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 112,520.00 USD | 0.00 USD | 756.06 USD | `-5.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 111,760.00 USD | 0.00 USD | 970.35 USD | `-5.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 110,790.00 USD | 0.00 USD | 5,470.00 USD | `-5.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 105,330.00 USD | 0.00 USD | 100.74 USD | `-4.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 105,230.00 USD | 0.00 USD | 3,290.00 USD | `-4.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 101,940.00 USD | 0.00 USD | 358.56 USD | `-4.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 101,580.00 USD | 0.00 USD | 1,880.00 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 99,700.00 USD | 0.00 USD | 140.36 USD | `-4.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 99,560.00 USD | 0.00 USD | 138.24 USD | `-4.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 99,420.00 USD | 0.00 USD | 1,130.00 USD | `-4.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 98,290.00 USD | 0.00 USD | 9,130.00 USD | `-3.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.48` | 89,160.00 USD | 0.00 USD | 489.58 USD | `-3.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.51` | 88,670.00 USD | 0.00 USD | 5,630.00 USD | `-3.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.52` | 83,040.00 USD | 0.00 USD | 7,620.00 USD | `-3.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.53` | 75,420.00 USD | 0.00 USD | 1,130.00 USD | `-3.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 74,290.00 USD | 0.00 USD | 132.45 USD | `-3.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 74,160.00 USD | 0.00 USD | 7,740.00 USD | `-3.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.57` | 66,420.00 USD | 0.00 USD | 1,610.00 USD | `-2.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.59` | 64,820.00 USD | 0.00 USD | 2,500.00 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.60` | 62,320.00 USD | 0.00 USD | 2,970.00 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.61` | 59,340.00 USD | 0.00 USD | 5,060.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 54,280.00 USD | 0.00 USD | 1,980.00 USD | `-2.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 52,300.00 USD | 0.00 USD | 6,310.00 USD | `-2.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.63` | 45,990.00 USD | 0.00 USD | 103.19 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.64` | 45,890.00 USD | 0.00 USD | 398.19 USD | `-2.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 45,490.00 USD | 0.00 USD | 3,000.00 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.66` | 42,500.00 USD | 0.00 USD | 196.87 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.68` | 42,300.00 USD | 0.00 USD | 223.82 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.69` | 42,080.00 USD | 0.00 USD | 1,330.00 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.70` | 40,750.00 USD | 0.00 USD | 5,010.00 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 35,740.00 USD | 0.00 USD | 5,510.00 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 30,220.00 USD | 0.00 USD | 4,940.00 USD | `-1.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.72` | 25,280.00 USD | 0.00 USD | 315.85 USD | `-1.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.73` | 24,960.00 USD | 0.00 USD | 1,390.00 USD | `-1.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.74` | 23,570.00 USD | 0.00 USD | 933.70 USD | `-0.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.76` | 22,640.00 USD | 0.00 USD | 183.33 USD | `-0.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.77` | 22,460.00 USD | 0.00 USD | 4,950.00 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.78` | 17,510.00 USD | 0.00 USD | 114.25 USD | `-0.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 17,390.00 USD | 0.00 USD | 4,230.00 USD | `-0.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 13,170.00 USD | 0.00 USD | 8,670.00 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.80` | 4,500.00 USD | 0.00 USD | 1,760.00 USD | `-0.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.81` | 2,740.00 USD | 0.00 USD | 705.20 USD | `-0.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.82` | 2,030.00 USD | 0.00 USD | 2,030.00 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 243.05 USD | 243.05 USD | 0.00 USD | `+0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 6,010.00 USD | 5,760.00 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 8,020.00 USD | 2,010.00 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 8,400.00 USD | 375.34 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 8,940.00 USD | 543.33 USD | 0.00 USD | `+0.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 10,040.00 USD | 1,100.00 USD | 0.00 USD | `+0.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 10,550.00 USD | 510.04 USD | 0.00 USD | `+0.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 11,340.00 USD | 788.72 USD | 0.00 USD | `+0.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 14,700.00 USD | 3,360.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 14,810.00 USD | 110.58 USD | 0.00 USD | `+1.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 16,860.00 USD | 2,040.00 USD | 0.00 USD | `+1.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 20,760.00 USD | 3,910.00 USD | 0.00 USD | `+1.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 20,900.00 USD | 137.73 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 336,050.00 USD | 315,150.00 USD | 0.00 USD | `+1.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 336,160.00 USD | 104.59 USD | 0.00 USD | `+1.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 336,930.00 USD | 776.54 USD | 0.00 USD | `+1.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 337,470.00 USD | 531.20 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 338,840.00 USD | 1,380.00 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 339,930.00 USD | 1,090.00 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 340,550.00 USD | 616.37 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 340,740.00 USD | 188.59 USD | 0.00 USD | `+2.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 340,900.00 USD | 160.99 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 341,310.00 USD | 415.00 USD | 0.00 USD | `+2.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 342,820.00 USD | 1,510.00 USD | 0.00 USD | `+2.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 344,410.00 USD | 1,590.00 USD | 0.00 USD | `+3.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 572,040.00 USD | 227,630.00 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 575,080.00 USD | 3,030.00 USD | 0.00 USD | `+3.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.13` | 578,570.00 USD | 3,500.00 USD | 0.00 USD | `+3.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 580,570.00 USD | 2,000.00 USD | 0.00 USD | `+3.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 580,870.00 USD | 295.11 USD | 0.00 USD | `+3.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.20` | 582,460.00 USD | 1,590.00 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 590,570.00 USD | 8,110.00 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 590,700.00 USD | 131.87 USD | 0.00 USD | `+4.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 591,390.00 USD | 687.91 USD | 0.00 USD | `+4.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 592,350.00 USD | 954.71 USD | 0.00 USD | `+4.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 593,410.00 USD | 1,060.00 USD | 0.00 USD | `+4.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.27` | 593,610.00 USD | 205.87 USD | 0.00 USD | `+4.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 595,680.00 USD | 2,070.00 USD | 0.00 USD | `+5.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 596,110.00 USD | 434.45 USD | 0.00 USD | `+5.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 614,720.00 USD | 18,610.00 USD | 0.00 USD | `+5.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 616,900.00 USD | 2,180.00 USD | 0.00 USD | `+5.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 617,480.00 USD | 579.86 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 944,910.00 USD | 327,430.00 USD | 0.00 USD | `+5.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 945,150.00 USD | 233.38 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 945,310.00 USD | 163.41 USD | 0.00 USD | `+6.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 946,460.00 USD | 1,150.00 USD | 0.00 USD | `+6.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 947,230.00 USD | 762.97 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 949,710.00 USD | 2,480.00 USD | 0.00 USD | `+6.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 950,720.00 USD | 1,010.00 USD | 0.00 USD | `+6.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 950,830.00 USD | 109.92 USD | 0.00 USD | `+6.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 950,970.00 USD | 140.35 USD | 0.00 USD | `+7.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 952,860.00 USD | 1,890.00 USD | 0.00 USD | `+7.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.47` | 954,640.00 USD | 1,780.00 USD | 0.00 USD | `+7.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 956,850.00 USD | 2,210.00 USD | 0.00 USD | `+7.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 957,140.00 USD | 288.46 USD | 0.00 USD | `+7.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.51` | 958,740.00 USD | 1,600.00 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 958,850.00 USD | 103.54 USD | 0.00 USD | `+7.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.54` | 960,160.00 USD | 1,320.00 USD | 0.00 USD | `+8.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.56` | 960,700.00 USD | 535.35 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 960,930.00 USD | 231.00 USD | 0.00 USD | `+8.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 961,150.00 USD | 221.07 USD | 0.00 USD | `+8.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 962,620.00 USD | 1,470.00 USD | 0.00 USD | `+8.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 962,950.00 USD | 329.43 USD | 0.00 USD | `+9.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 963,400.00 USD | 446.58 USD | 0.00 USD | `+9.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 963,520.00 USD | 121.87 USD | 0.00 USD | `+10.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.80` | 964,140.00 USD | 619.28 USD | 0.00 USD | `+11.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 969,170.00 USD | 5,030.00 USD | 0.00 USD | `+11.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 969,510.00 USD | 340.05 USD | 0.00 USD | `+11.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 970,250.00 USD | 742.12 USD | 0.00 USD | `+12.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 971,600.00 USD | 1,340.00 USD | 0.00 USD | `+12.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,040,000.00 USD | 70,020.00 USD | 0.00 USD | `+12.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,040,000.00 USD | 373.97 USD | 0.00 USD | `+12.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,050,000.00 USD | 5,480.00 USD | 0.00 USD | `+13.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,050,000.00 USD | 6,370.00 USD | 0.00 USD | `+14.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,050,000.00 USD | 202.10 USD | 0.00 USD | `+14.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,210,000.00 USD | 155,680.00 USD | 0.00 USD | `+14.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,210,000.00 USD | 1,150.00 USD | 0.00 USD | `+14.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,210,000.00 USD | 172.16 USD | 0.00 USD | `+15.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,210,000.00 USD | 868.36 USD | 0.00 USD | `+16.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,210,000.00 USD | 489.40 USD | 0.00 USD | `+16.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,210,000.00 USD | 1,200.00 USD | 0.00 USD | `+17.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,210,000.00 USD | 118.01 USD | 0.00 USD | `+18.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,210,000.00 USD | 312.31 USD | 0.00 USD | `+19.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,210,000.00 USD | 764.23 USD | 0.00 USD | `+19.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,210,000.00 USD | 178.46 USD | 0.00 USD | `+19.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.62` | 1,220,000.00 USD | 153.11 USD | 0.00 USD | `+20.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,220,000.00 USD | 173.42 USD | 0.00 USD | `+21.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,220,000.00 USD | 184.75 USD | 0.00 USD | `+21.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,220,000.00 USD | 135.78 USD | 0.00 USD | `+22.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,220,000.00 USD | 127.96 USD | 0.00 USD | `+22.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,220,000.00 USD | 476.43 USD | 0.00 USD | `+23.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,220,000.00 USD | 1,730.00 USD | 0.00 USD | `+23.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,220,000.00 USD | 118.97 USD | 0.00 USD | `+23.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,220,000.00 USD | 552.44 USD | 0.00 USD | `+23.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,220,000.00 USD | 3,430.00 USD | 0.00 USD | `+24.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,220,000.00 USD | 1,100.00 USD | 0.00 USD | `+26.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,230,000.00 USD | 2,610.00 USD | 0.00 USD | `+26.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,230,000.00 USD | 1,270.00 USD | 0.00 USD | `+27.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,230,000.00 USD | 1,380.00 USD | 0.00 USD | `+28.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,230,000.00 USD | 2,410.00 USD | 0.00 USD | `+29.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,240,000.00 USD | 9,520.00 USD | 0.00 USD | `+29.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,240,000.00 USD | 3,820.00 USD | 0.00 USD | `+30.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,250,000.00 USD | 7,700.00 USD | 0.00 USD | `+31.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,250,000.00 USD | 1,130.00 USD | 0.00 USD | `+33.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,250,000.00 USD | 434.61 USD | 0.00 USD | `+34.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,250,000.00 USD | 163.52 USD | 0.00 USD | `+34.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 1,380,000.00 USD | 124,300.00 USD | 0.00 USD | `+36.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.51` | 1,380,000.00 USD | 2,770.00 USD | 0.00 USD | `+41.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 1,380,000.00 USD | 3,350.00 USD | 0.00 USD | `+43.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 1,380,000.00 USD | 197.97 USD | 0.00 USD | `+45.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 1,390,000.00 USD | 3,200.00 USD | 0.00 USD | `+46.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 1,390,000.00 USD | 179.58 USD | 0.00 USD | `+47.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 1,390,000.00 USD | 720.74 USD | 0.00 USD | `+47.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.07` | 1,390,000.00 USD | 504.17 USD | 0.00 USD | `+48.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 1,390,000.00 USD | 169.57 USD | 0.00 USD | `+48.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.30` | 1,390,000.00 USD | 159.66 USD | 0.00 USD | `+50.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 1,390,000.00 USD | 446.52 USD | 0.00 USD | `+51.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.46` | 1,390,000.00 USD | 1,710.00 USD | 0.00 USD | `+52.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 1,400,000.00 USD | 5,320.00 USD | 0.00 USD | `+52.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 1,600,000.00 USD | 207,980.00 USD | 0.00 USD | `+53.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 1,610,000.00 USD | 407.95 USD | 0.00 USD | `+55.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 1,610,000.00 USD | 174.91 USD | 0.00 USD | `+56.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 1,610,000.00 USD | 9,230.00 USD | 0.00 USD | `+58.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 1,620,000.00 USD | 960.26 USD | 0.00 USD | `+60.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 1,620,000.00 USD | 2,710.00 USD | 0.00 USD | `+62.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 1,620,000.00 USD | 805.90 USD | 0.00 USD | `+64.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 1,620,000.00 USD | 655.55 USD | 0.00 USD | `+66.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 1,620,000.00 USD | 4,890.00 USD | 0.00 USD | `+67.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 1,620,000.00 USD | 471.09 USD | 0.00 USD | `+68.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 1,630,000.00 USD | 383.85 USD | 0.00 USD | `+69.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,280,000.00 USD | 653,070.00 USD | 0.00 USD | `+69.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,280,000.00 USD | 111.87 USD | 0.00 USD | `+79.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,280,000.00 USD | 219.91 USD | 0.00 USD | `+81.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 2,280,000.00 USD | 121.74 USD | 0.00 USD | `+92.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.00` | 2,280,000.00 USD | 297.59 USD | 0.00 USD | `+92.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.18` | 2,280,000.00 USD | 4,500.00 USD | 0.00 USD | `+94.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.20` | 2,400,000.00 USD | 120,270.00 USD | 0.00 USD | `+94.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.34` | 2,400,000.00 USD | 122.39 USD | 0.00 USD | `+96.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.50` | 2,400,000.00 USD | 586.59 USD | 0.00 USD | `+98.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.61` | 2,410,000.00 USD | 580.97 USD | 0.00 USD | `+99.44%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.74` | 8,640,000.00 USD | 0.00 USD | 8,640,000.00 USD | 976.80 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.76` | 8,640,000.00 USD | 0.00 USD | 8,640,000.00 USD | 812.95 USD | 5,760.00 USD | 0.00 USD |
| `7D` | `7.78` | 8,630,000.00 USD | 0.00 USD | 8,630,000.00 USD | 23,430.00 USD | 4,900.00 USD | 20,150.00 USD |
| `7D` | `7.80` | 8,580,000.00 USD | 0.00 USD | 8,580,000.00 USD | 13,050.00 USD | 12,980.00 USD | 0.00 USD |
| `7D` | `7.82` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,280.00 USD |
| `7D` | `7.84` | 8,540,000.00 USD | 0.00 USD | 8,540,000.00 USD | 29,020.00 USD | 2,380.00 USD | 19,730.00 USD |
| `1D` | `7.85` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 4,700.00 USD | 1,820.00 USD | 8,870.00 USD |
| `1D` | `7.86` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 10,180.00 USD | 424.36 USD | 11,210.00 USD |
| `7D` | `7.86` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD |
| `1D` | `7.87` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD |
| `1D` | `7.88` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 16,020.00 USD | 4,370.00 USD | 4,550.00 USD |
| `7D` | `7.88` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 46,450.00 USD | 12,780.00 USD | 29,190.00 USD |
| `1D` | `7.89` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 5,220.00 USD | 4,150.00 USD | 1,720.00 USD |
| `1D` | `7.90` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 9,200.00 USD | 3,480.00 USD | 5,760.00 USD |
| `7D` | `7.90` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,650.00 USD |
| `1D` | `7.91` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 2,990.00 USD | 0.00 USD | 2,230.00 USD |
| `1D` | `7.92` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 12,900.00 USD | 2,950.00 USD | 3,980.00 USD |
| `7D` | `7.92` | 8,290,000.00 USD | 0.00 USD | 8,290,000.00 USD | 53,660.00 USD | 8,420.00 USD | 14,900.00 USD |
| `1D` | `7.93` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 0.00 USD | 831.98 USD | 0.00 USD |
| `1D` | `7.94` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 11,450.00 USD | 3,900.00 USD | 4,500.00 USD |
| `7D` | `7.94` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 38,370.00 USD | 9,960.00 USD | 31,670.00 USD |
| `1D` | `7.95` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 0.00 USD | 1,420.00 USD | 2,440.00 USD |
| `1D` | `7.96` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 8,450.00 USD | 2,280.00 USD | 6,320.00 USD |
| `7D` | `7.96` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 21,840.00 USD | 4,820.00 USD | 26,380.00 USD |
| `1D` | `7.97` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 11,690.00 USD | 5,500.00 USD | 10,350.00 USD |
| `1D` | `7.98` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 10,080.00 USD | 1,760.00 USD | 548.73 USD |
| `7D` | `7.98` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 42,740.00 USD | 19,680.00 USD | 70,210.00 USD |
| `1D` | `7.99` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 9,190.00 USD | 2,180.00 USD | 1,510.00 USD |
| `1D` | `8.00` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 2,330.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.00` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,130.00 USD |
| `1D` | `8.01` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 6,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.02` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 2,230.00 USD | 770.83 USD | 0.00 USD |
| `7D` | `8.02` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 20,050.00 USD | 28,440.00 USD | 10,280.00 USD |
| `1D` | `8.03` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 8,800.00 USD | 0.00 USD | 4,430.00 USD |
| `1D` | `8.04` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 3,240.00 USD | 0.00 USD | 5,260.00 USD |
| `7D` | `8.04` | 7,810,000.00 USD | 0.00 USD | 7,810,000.00 USD | 94,150.00 USD | 23,930.00 USD | 75,230.00 USD |
| `1D` | `8.05` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 3,700.00 USD | 1,790.00 USD | 2,240.00 USD |
| `1D` | `8.06` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 7,120.00 USD | 0.00 USD | 2,360.00 USD |
| `7D` | `8.06` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 69,980.00 USD | 10,070.00 USD | 78,860.00 USD |
| `1D` | `8.07` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 944.98 USD | 0.00 USD | 6,030.00 USD |
| `1D` | `8.08` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 769.07 USD | 269.63 USD | 3,220.00 USD |
| `7D` | `8.08` | 7,460,000.00 USD | 0.00 USD | 7,460,000.00 USD | 7,170.00 USD | 3,650.00 USD | 20,860.00 USD |
| `1D` | `8.09` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 6,700.00 USD | 1,220.00 USD | 5,350.00 USD |
| `1D` | `8.10` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 23,830.00 USD | 1,620.00 USD | 6,040.00 USD |
| `7D` | `8.10` | 7,430,000.00 USD | 0.00 USD | 7,430,000.00 USD | 61,140.00 USD | 19,700.00 USD | 14,170.00 USD |
| `1D` | `8.11` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 144.37 USD | 1,980.00 USD | 1,360.00 USD |
| `1D` | `8.12` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 3,730.00 USD | 0.00 USD | 5,360.00 USD |
| `7D` | `8.12` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 27,150.00 USD | 10,810.00 USD | 9,260.00 USD |
| `1D` | `8.13` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 4,140.00 USD | 693.45 USD | 1,310.00 USD |
| `1D` | `8.14` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 8,480.00 USD | 0.00 USD | 26.83 USD |
| `7D` | `8.14` | 7,290,000.00 USD | 0.00 USD | 7,290,000.00 USD | 57,880.00 USD | 11,150.00 USD | 39,780.00 USD |
| `1D` | `8.15` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 11,200.00 USD | 662.47 USD | 4,950.00 USD |
| `1D` | `8.16` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 385.98 USD | 2,120.00 USD | 47.18 USD |
| `7D` | `8.16` | 7,180,000.00 USD | 0.00 USD | 7,180,000.00 USD | 38,430.00 USD | 5,510.00 USD | 30,640.00 USD |
| `1D` | `8.17` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 2,970.00 USD | 0.00 USD | 12.32 USD |
| `1D` | `8.18` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 1,150.00 USD | 1,980.00 USD | 466.21 USD |
| `7D` | `8.18` | 7,100,000.00 USD | 0.00 USD | 7,100,000.00 USD | 19,550.00 USD | 6,790.00 USD | 2,750.00 USD |
| `1D` | `8.19` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 4,850.00 USD | 0.00 USD | 48.71 USD |
| `1D` | `8.20` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 7,720.00 USD | 2,310.00 USD | 431.88 USD |
| `7D` | `8.20` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 63,560.00 USD | 0.00 USD | 16,030.00 USD |
| `1D` | `8.21` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 1,880.00 USD | 0.00 USD | 46.18 USD |
| `1D` | `8.22` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 5,330.00 USD | 0.00 USD | 12,570.00 USD |
| `7D` | `8.22` | 6,990,000.00 USD | 0.00 USD | 6,990,000.00 USD | 35,730.00 USD | 0.00 USD | 26,510.00 USD |
| `1D` | `8.23` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 20,950.00 USD | 4,080.00 USD | 31,000.00 USD |
| `1D` | `8.24` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 10,020.00 USD | 1,150.00 USD | 3,510.00 USD |
| `7D` | `8.24` | 6,930,000.00 USD | 0.00 USD | 6,930,000.00 USD | 39,950.00 USD | 3,480.00 USD | 107,080.00 USD |
| `1D` | `8.25` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 8,710.00 USD | 0.00 USD | 6,100.00 USD |
| `1D` | `8.26` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 192.60 USD | 11,460.00 USD | 0.00 USD |
| `7D` | `8.26` | 6,780,000.00 USD | 0.00 USD | 6,780,000.00 USD | 29,800.00 USD | 5,750.00 USD | 9,280.00 USD |
| `1D` | `8.27` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 11,800.00 USD | 2,760.00 USD | 36.54 USD |
| `1D` | `8.28` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 74,980.00 USD | 7,070.00 USD | 40,810.00 USD |
| `7D` | `8.28` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 122,850.00 USD | 33,920.00 USD | 14,010.00 USD |
| `1D` | `8.29` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 34,940.00 USD | 9,470.00 USD | 4,640.00 USD |
| `1D` | `8.30` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 52,980.00 USD | 13,130.00 USD | 19,010.00 USD |
| `7D` | `8.30` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 101,180.00 USD | 13,500.00 USD | 47,820.00 USD |
| `1D` | `8.31` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 55,700.00 USD | 11,410.00 USD | 1,560.00 USD |
| `1D` | `8.32` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 19,320.00 USD | 4,190.00 USD | 7,320.00 USD |
| `7D` | `8.32` | 6,400,000.00 USD | 0.00 USD | 6,400,000.00 USD | 61,070.00 USD | 26,020.00 USD | 4,710.00 USD |
| `1D` | `8.33` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 2,670.00 USD | 22,580.00 USD | 9,950.00 USD |
| `1D` | `8.34` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 14,430.00 USD | 4,810.00 USD | 6,300.00 USD |
| `7D` | `8.34` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 36,960.00 USD | 15,520.00 USD | 30,170.00 USD |
| `1D` | `8.35` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 6,060.00 USD | 11,270.00 USD | 16,070.00 USD |
| `1D` | `8.36` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 3,900.00 USD | 2,420.00 USD | 21,850.00 USD |
| `7D` | `8.36` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 107,010.00 USD | 13,470.00 USD | 71,060.00 USD |
| `1D` | `8.37` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 21,620.00 USD | 7,980.00 USD | 8,340.00 USD |
| `1D` | `8.38` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 36,180.00 USD | 4,080.00 USD | 33,870.00 USD |
| `7D` | `8.38` | 6,040,000.00 USD | 0.00 USD | 6,040,000.00 USD | 143,540.00 USD | 20,560.00 USD | 66,570.00 USD |
| `1D` | `8.39` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 62,830.00 USD | 10,540.00 USD | 56,460.00 USD |
| `1D` | `8.40` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 68,490.00 USD | 22,890.00 USD | 67,990.00 USD |
| `7D` | `8.40` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 149,520.00 USD | 19,710.00 USD | 220,030.00 USD |
| `1D` | `8.41` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 33,190.00 USD | 3,620.00 USD | 20,930.00 USD |
| `1D` | `8.42` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 33,460.00 USD | 12,790.00 USD | 18,450.00 USD |
| `7D` | `8.42` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 176,550.00 USD | 57,340.00 USD | 72,790.00 USD |
| `1D` | `8.43` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 30,620.00 USD | 34,530.00 USD | 14,440.00 USD |
| `1D` | `8.44` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 35,960.00 USD | 8,900.00 USD | 7,570.00 USD |
| `7D` | `8.44` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 155,040.00 USD | 68,350.00 USD | 76,630.00 USD |
| `1D` | `8.45` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 72,750.00 USD | 14,270.00 USD | 45,560.00 USD |
| `1D` | `8.46` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 138,660.00 USD | 13,720.00 USD | 49,580.00 USD |
| `7D` | `8.46` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 391,750.00 USD | 59,170.00 USD | 107,410.00 USD |
| `1D` | `8.47` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 111,460.00 USD | 29,440.00 USD | 22,100.00 USD |
| `1D` | `8.48` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 115,230.00 USD | 32,510.00 USD | 47,200.00 USD |
| `7D` | `8.48` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 306,870.00 USD | 56,420.00 USD | 220,180.00 USD |
| `1D` | `8.49` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 130,130.00 USD | 29,970.00 USD | 21,050.00 USD |
| `1D` | `8.50` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 46,010.00 USD | 19,260.00 USD | 21,100.00 USD |
| `7D` | `8.50` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 180,050.00 USD | 87,640.00 USD | 112,330.00 USD |
| `1D` | `8.51` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 55,990.00 USD | 54,280.00 USD | 43,390.00 USD |
| `1D` | `8.52` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 79,750.00 USD | 22,420.00 USD | 17,670.00 USD |
| `7D` | `8.52` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 255,070.00 USD | 92,530.00 USD | 239,490.00 USD |
| `1D` | `8.53` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 16,630.00 USD | 23,780.00 USD | 32,180.00 USD |
| `1D` | `8.54` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 18,880.00 USD | 6,040.00 USD | 43,640.00 USD |
| `7D` | `8.54` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 378,750.00 USD | 78,380.00 USD | 152,160.00 USD |
| `1D` | `8.55` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 42,130.00 USD | 17,890.00 USD | 16,620.00 USD |
| `1D` | `8.56` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 69,420.00 USD | 8,150.00 USD | 67,740.00 USD |
| `7D` | `8.56` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 520,060.00 USD | 91,230.00 USD | 60,050.00 USD |
| `1D` | `8.57` | 907,360.00 USD | 0.00 USD | 907,360.00 USD | 56,370.00 USD | 7,000.00 USD | 55,660.00 USD |
| `1D` | `8.58` | 788,340.00 USD | 0.00 USD | 788,340.00 USD | 48,420.00 USD | 13,910.00 USD | 39,900.00 USD |
| `7D` | `8.58` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 527,760.00 USD | 164,810.00 USD | 34,110.00 USD |
| `1D` | `8.59` | 686,110.00 USD | 0.00 USD | 686,110.00 USD | 43,310.00 USD | 25,580.00 USD | 12,560.00 USD |
| `1D` | `8.60` | 604,660.00 USD | 0.00 USD | 604,660.00 USD | 58,480.00 USD | 23,230.00 USD | 34,660.00 USD |
| `7D` | `8.60` | 693,950.00 USD | 0.00 USD | 693,950.00 USD | 75,040.00 USD | 39,160.00 USD | 176,770.00 USD |
| `1D` | `8.61` | 488,290.00 USD | 0.00 USD | 488,290.00 USD | 28,830.00 USD | 6,770.00 USD | 30,850.00 USD |
| `1D` | `8.62` | 421,840.00 USD | 0.00 USD | 421,840.00 USD | 87,140.00 USD | 14,760.00 USD | 19,830.00 USD |
| `7D` | `8.62` | 402,980.00 USD | 0.00 USD | 402,980.00 USD | 0.00 USD | 26,800.00 USD | 78,730.00 USD |
| `1D` | `8.63` | 300,110.00 USD | 0.00 USD | 300,110.00 USD | 24,730.00 USD | 2,010.00 USD | 3,840.00 USD |
| `1D` | `8.64` | 269,530.00 USD | 0.00 USD | 269,530.00 USD | 64,480.00 USD | 1,540.00 USD | 3,170.00 USD |
| `7D` | `8.64` | 297,450.00 USD | 0.00 USD | 297,450.00 USD | 73,980.00 USD | 5,680.00 USD | 58.11 USD |
| `1D` | `8.65` | 200,340.00 USD | 0.00 USD | 200,340.00 USD | 18,440.00 USD | 7,110.00 USD | 12,280.00 USD |
| `7D` | `8.66` | 217,730.00 USD | 0.00 USD | 217,730.00 USD | 0.00 USD | 6,040.00 USD | 37,900.00 USD |
| `1D` | `8.68` | 162,510.00 USD | 0.00 USD | 162,510.00 USD | 0.00 USD | 0.00 USD | 56.84 USD |
| `7D` | `8.68` | 173,790.00 USD | 0.00 USD | 173,790.00 USD | 0.00 USD | 0.00 USD | 173,670.00 USD |
| `7D` | `8.82` | 118.36 USD | 0.00 USD | 118.36 USD | 0.00 USD | 0.00 USD | 118.36 USD |
| `1D` | `8.84` | 162,460.00 USD | 0.00 USD | 162,460.00 USD | 97,740.00 USD | 16,450.00 USD | 48,260.00 USD |
| `7D` | `8.84` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.85` | 74,760.00 USD | 74,760.00 USD | 0.00 USD | 0.00 USD | 48,620.00 USD | 26,140.00 USD |
| `1D` | `8.85` | 149,520.00 USD | 149,520.00 USD | 0.00 USD | 0.00 USD | 48,620.00 USD | 26,140.00 USD |
| `1D` | `8.86` | 199,380.00 USD | 199,380.00 USD | 0.00 USD | 25,310.00 USD | 12,040.00 USD | 12,510.00 USD |
| `7D` | `8.86` | 119,780.00 USD | 119,780.00 USD | 0.00 USD | 119,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.87` | 297,400.00 USD | 297,400.00 USD | 0.00 USD | 9,410.00 USD | 22,550.00 USD | 66,070.00 USD |
| `1D` | `8.88` | 350,360.00 USD | 350,360.00 USD | 0.00 USD | 4,550.00 USD | 4,830.00 USD | 43,590.00 USD |
| `7D` | `8.88` | 202,910.00 USD | 202,910.00 USD | 0.00 USD | 0.00 USD | 4,350.00 USD | 78,770.00 USD |
| `1D` | `8.89` | 423,710.00 USD | 423,710.00 USD | 0.00 USD | 40,760.00 USD | 15,970.00 USD | 16,620.00 USD |
| `1D` | `8.90` | 582,870.00 USD | 582,870.00 USD | 0.00 USD | 73,240.00 USD | 8,150.00 USD | 77,770.00 USD |
| `7D` | `8.90` | 532,330.00 USD | 532,330.00 USD | 0.00 USD | 159,560.00 USD | 54,390.00 USD | 115,480.00 USD |
| `1D` | `8.91` | 842,000.00 USD | 842,000.00 USD | 0.00 USD | 130,250.00 USD | 25,170.00 USD | 103,710.00 USD |
| `1D` | `8.92` | 854,710.00 USD | 854,710.00 USD | 0.00 USD | 8,060.00 USD | 1,150.00 USD | 3,500.00 USD |
| `7D` | `8.92` | 648,960.00 USD | 648,960.00 USD | 0.00 USD | 19,230.00 USD | 7,700.00 USD | 89,700.00 USD |
| `1D` | `8.93` | 969,640.00 USD | 969,640.00 USD | 0.00 USD | 55,830.00 USD | 40,980.00 USD | 18,120.00 USD |
| `1D` | `8.94` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 34,120.00 USD | 14,100.00 USD | 27,860.00 USD |
| `7D` | `8.94` | 774,510.00 USD | 774,510.00 USD | 0.00 USD | 60,190.00 USD | 32,050.00 USD | 33,310.00 USD |
| `1D` | `8.95` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 53,880.00 USD | 28,330.00 USD | 25,180.00 USD |
| `1D` | `8.96` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 73,070.00 USD | 26,680.00 USD | 46,590.00 USD |
| `7D` | `8.96` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 158,650.00 USD | 92,290.00 USD | 12,730.00 USD |
| `1D` | `8.97` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 28,830.00 USD | 6,770.00 USD | 11,130.00 USD |
| `1D` | `8.98` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 147,050.00 USD | 18,380.00 USD | 42,760.00 USD |
| `7D` | `8.98` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 61,300.00 USD | 39,050.00 USD | 38,480.00 USD |
| `1D` | `8.99` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 59,440.00 USD | 11,480.00 USD | 8,470.00 USD |
| `1D` | `9.00` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 116,720.00 USD | 31,900.00 USD | 30,820.00 USD |
| `7D` | `9.00` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 161,560.00 USD | 17,050.00 USD | 46,410.00 USD |
| `1D` | `9.01` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 74,700.00 USD | 18,520.00 USD | 13,690.00 USD |
| `1D` | `9.02` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 18,000.00 USD | 4,190.00 USD | 11,830.00 USD |
| `7D` | `9.02` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 31,620.00 USD | 45,640.00 USD | 36,700.00 USD |
| `1D` | `9.03` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 2,970.00 USD | 44,330.00 USD | 22,750.00 USD |
| `1D` | `9.04` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 24,830.00 USD | 4,810.00 USD | 54,070.00 USD |
| `7D` | `9.04` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 1,950.00 USD | 49,890.00 USD | 15,140.00 USD |
| `1D` | `9.05` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 8,220.00 USD | 20,830.00 USD | 16,070.00 USD |
| `1D` | `9.06` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 3,490.00 USD | 16,550.00 USD | 22,230.00 USD |
| `7D` | `9.06` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 181,600.00 USD | 2,170.00 USD | 16,840.00 USD |
| `1D` | `9.07` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 21,880.00 USD | 10,450.00 USD | 8,310.00 USD |
| `1D` | `9.08` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 63,740.00 USD | 6,490.00 USD | 33,870.00 USD |
| `7D` | `9.08` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 142,630.00 USD | 11,960.00 USD | 65,080.00 USD |
| `1D` | `9.09` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 54,960.00 USD | 14,400.00 USD | 36,370.00 USD |
| `1D` | `9.10` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 66,840.00 USD | 14,720.00 USD | 26,710.00 USD |
| `7D` | `9.10` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 652,680.00 USD | 16,080.00 USD | 268,600.00 USD |
| `1D` | `9.11` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 19,700.00 USD | 1,320.00 USD | 13,930.00 USD |
| `1D` | `9.12` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 28,220.00 USD | 16,570.00 USD | 6,270.00 USD |
| `7D` | `9.12` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 463,210.00 USD | 24,170.00 USD | 457,010.00 USD |
| `1D` | `9.13` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 29,720.00 USD | 11,620.00 USD | 14,390.00 USD |
| `1D` | `9.14` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 14,660.00 USD | 8,440.00 USD | 17,350.00 USD |
| `7D` | `9.14` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 536,560.00 USD | 18,540.00 USD | 420,870.00 USD |
| `1D` | `9.15` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 44,870.00 USD | 7,380.00 USD | 18,890.00 USD |
| `1D` | `9.16` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 12,360.00 USD | 9,170.00 USD | 22,950.00 USD |
| `7D` | `9.16` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 331,010.00 USD | 10,610.00 USD | 195,800.00 USD |
| `1D` | `9.17` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 71,740.00 USD | 18,120.00 USD | 51,710.00 USD |
| `1D` | `9.18` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 132,750.00 USD | 19,990.00 USD | 43,220.00 USD |
| `7D` | `9.18` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 494,640.00 USD | 157,220.00 USD | 242,060.00 USD |
| `1D` | `9.19` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 66,110.00 USD | 22,640.00 USD | 25,180.00 USD |
| `1D` | `9.20` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 72,570.00 USD | 18,950.00 USD | 40,140.00 USD |
| `7D` | `9.20` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 509,140.00 USD | 107,650.00 USD | 238,640.00 USD |
| `1D` | `9.21` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 72,580.00 USD | 12,590.00 USD | 30,610.00 USD |
| `1D` | `9.22` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 71,070.00 USD | 8,140.00 USD | 1,410.00 USD |
| `7D` | `9.22` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 495,210.00 USD | 134,000.00 USD | 405,090.00 USD |
| `1D` | `9.23` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 57,020.00 USD | 3,310.00 USD | 33,930.00 USD |
| `1D` | `9.24` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 26,080.00 USD | 8,310.00 USD | 3,830.00 USD |
| `7D` | `9.24` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 316,220.00 USD | 52,090.00 USD | 174,910.00 USD |
| `1D` | `9.25` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 7,640.00 USD | 11,850.00 USD | 22.09 USD |
| `1D` | `9.26` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 16,290.00 USD | 1,210.00 USD | 0.00 USD |
| `7D` | `9.26` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 273,920.00 USD | 96,980.00 USD | 60,730.00 USD |
| `1D` | `9.27` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 144.37 USD | 11,810.00 USD | 0.00 USD |
| `1D` | `9.28` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 21,090.00 USD | 0.00 USD | 10,370.00 USD |
| `7D` | `9.28` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 451,410.00 USD | 93,640.00 USD | 142,150.00 USD |
| `1D` | `9.29` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 32,900.00 USD | 14,120.00 USD | 13,170.00 USD |
| `1D` | `9.30` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 19,890.00 USD | 8,530.00 USD | 6,810.00 USD |
| `7D` | `9.30` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 314,150.00 USD | 97,780.00 USD | 335,920.00 USD |
| `1D` | `9.31` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 13,100.00 USD | 0.00 USD | 12,680.00 USD |
| `1D` | `9.32` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 387.00 USD | 2,530.00 USD | 5,890.00 USD |
| `7D` | `9.32` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 271,660.00 USD | 59,310.00 USD | 308,520.00 USD |
| `1D` | `9.33` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 9,850.00 USD | 0.00 USD | 15,710.00 USD |
| `1D` | `9.34` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 385.98 USD | 1,350.00 USD | 9,650.00 USD |
| `7D` | `9.34` | 11,590,000.00 USD | 11,590,000.00 USD | 0.00 USD | 189,770.00 USD | 36,270.00 USD | 129,810.00 USD |
| `1D` | `9.35` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 15,350.00 USD | 3,810.00 USD | 19,450.00 USD |
| `1D` | `9.36` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 61,640.00 USD | 6,870.00 USD | 17,100.00 USD |
| `7D` | `9.36` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 245,070.00 USD | 78,550.00 USD | 101,700.00 USD |
| `1D` | `9.37` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 26,010.00 USD | 7,740.00 USD | 3,430.00 USD |
| `1D` | `9.38` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 32,400.00 USD | 4,040.00 USD | 16,830.00 USD |
| `7D` | `9.38` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 383,530.00 USD | 55,400.00 USD | 85,250.00 USD |
| `1D` | `9.39` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 8,200.00 USD | 1,730.00 USD | 3,280.00 USD |
| `1D` | `9.40` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 22,280.00 USD | 1,210.00 USD | 12.64 USD |
| `7D` | `9.40` | 12,940,000.00 USD | 12,940,000.00 USD | 0.00 USD | 196,230.00 USD | 58,130.00 USD | 152,850.00 USD |
| `1D` | `9.41` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 29,870.00 USD | 1,660.00 USD | 16,970.00 USD |
| `1D` | `9.42` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 1,520.00 USD | 622.99 USD | 4,030.00 USD |
| `7D` | `9.42` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 176,920.00 USD | 44,410.00 USD | 84,120.00 USD |
| `1D` | `9.43` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 5,840.00 USD | 6,940.00 USD | 12,410.00 USD |
| `1D` | `9.44` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 992.05 USD | 0.00 USD | 48.84 USD |
| `7D` | `9.44` | 13,390,000.00 USD | 13,390,000.00 USD | 0.00 USD | 62,040.00 USD | 19,420.00 USD | 56,550.00 USD |
| `1D` | `9.45` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 1,860.00 USD | 4,940.00 USD | 2,450.00 USD |
| `1D` | `9.46` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 1,800.00 USD | 4,580.00 USD | 21.27 USD |
| `7D` | `9.46` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 183,340.00 USD | 32,490.00 USD | 19,460.00 USD |
| `1D` | `9.47` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 17,460.00 USD | 6,870.00 USD | 192.20 USD |
| `1D` | `9.48` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 1,510.00 USD | 0.00 USD | 5,190.00 USD |
| `7D` | `9.48` | 13,800,000.00 USD | 13,800,000.00 USD | 0.00 USD | 76,510.00 USD | 37,930.00 USD | 67,400.00 USD |
| `1D` | `9.49` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 20,880.00 USD | 572.85 USD | 5,600.00 USD |
| `1D` | `9.50` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 11,770.00 USD | 3,160.00 USD | 6,320.00 USD |
| `7D` | `9.50` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 94,930.00 USD | 33,210.00 USD | 103,070.00 USD |
| `1D` | `9.52` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 17,120.00 USD | 3,070.00 USD | 5,400.00 USD |
| `7D` | `9.52` | 14,230,000.00 USD | 14,230,000.00 USD | 0.00 USD | 103,000.00 USD | 29,320.00 USD | 66,250.00 USD |
| `1D` | `9.53` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 18,480.00 USD | 4,560.00 USD | 0.00 USD |
| `1D` | `9.54` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 5,310.00 USD | 1,470.00 USD | 2,920.00 USD |
| `7D` | `9.54` | 14,470,000.00 USD | 14,470,000.00 USD | 0.00 USD | 192,230.00 USD | 27,650.00 USD | 15,770.00 USD |
| `1D` | `9.55` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 2,170.00 USD | 6,330.00 USD | 3,100.00 USD |
| `1D` | `9.56` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 5,160.00 USD | 1,280.00 USD | 2,530.00 USD |
| `7D` | `9.56` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 89,520.00 USD | 5,260.00 USD | 32,840.00 USD |
| `1D` | `9.57` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 1,020.00 USD | 3,100.00 USD | 4,960.00 USD |
| `1D` | `9.58` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 1,290.00 USD | 563.17 USD | 7,730.00 USD |
| `7D` | `9.58` | 14,680,000.00 USD | 14,680,000.00 USD | 0.00 USD | 38,860.00 USD | 16,980.00 USD | 21,640.00 USD |
| `1D` | `9.59` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 4,670.00 USD | 1,250.00 USD | 1,170.00 USD |
| `1D` | `9.60` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 11,210.00 USD | 424.36 USD | 11,260.00 USD |
| `7D` | `9.60` | 14,760,000.00 USD | 14,760,000.00 USD | 0.00 USD | 38,650.00 USD | 10,820.00 USD | 33,120.00 USD |
| `1D` | `9.61` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD |
| `1D` | `9.62` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 675.26 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.62` | 14,860,000.00 USD | 14,860,000.00 USD | 0.00 USD | 69,630.00 USD | 13,850.00 USD | 17,600.00 USD |
| `1D` | `9.63` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 10,190.00 USD | 4,370.00 USD | 1,150.00 USD |
| `1D` | `9.64` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 5,830.00 USD | 0.00 USD | 3,410.00 USD |
| `7D` | `9.64` | 14,960,000.00 USD | 14,960,000.00 USD | 0.00 USD | 61,870.00 USD | 17,650.00 USD | 19,900.00 USD |
| `1D` | `9.65` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 5,960.00 USD | 4,150.00 USD | 1,740.00 USD |
| `1D` | `9.66` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 9,200.00 USD | 3,480.00 USD | 5,760.00 USD |
| `7D` | `9.66` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 37,340.00 USD | 21,280.00 USD | 18,480.00 USD |
| `1D` | `9.67` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 2,990.00 USD | 0.00 USD | 2,230.00 USD |
| `1D` | `9.68` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 12,900.00 USD | 2,950.00 USD | 3,980.00 USD |
| `7D` | `9.68` | 15,160,000.00 USD | 15,160,000.00 USD | 0.00 USD | 69,470.00 USD | 20,310.00 USD | 34,130.00 USD |
| `1D` | `9.69` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 831.98 USD | 0.00 USD |
| `1D` | `9.70` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 11,450.00 USD | 3,900.00 USD | 4,500.00 USD |
| `7D` | `9.70` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 69,750.00 USD | 12,990.00 USD | 31,760.00 USD |
| `1D` | `9.71` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 1,420.00 USD | 2,460.00 USD |
| `1D` | `9.72` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 8,450.00 USD | 2,280.00 USD | 6,360.00 USD |
| `7D` | `9.72` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 74,210.00 USD | 4,820.00 USD | 26,980.00 USD |
| `1D` | `9.74` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 3,560.00 USD | 2,580.00 USD |
| `7D` | `9.74` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 11,450.00 USD | 7,200.00 USD | 19,560.00 USD |
| `1D` | `9.75` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 11,500.00 USD | 1,940.00 USD | 7,760.00 USD |
| `1D` | `9.76` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 9,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.76` | 15,510,000.00 USD | 15,510,000.00 USD | 0.00 USD | 31,950.00 USD | 12,480.00 USD | 51,420.00 USD |
| `7D` | `9.77` | 15,550,000.00 USD | 15,550,000.00 USD | 0.00 USD | 28,630.00 USD | 3,270.00 USD | 4,650.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `381.92M` | Total OI Tokens: `43,320,504.4 AVAX`
  * 1h OI Change: `+0.32%` | 4h OI Change: `+1.10%` | 24h OI Change: `-2.04%`
  * Exchange Breakdown: Binance=`88.71M` | Bybit=`59.43M` | OKX=`12.64M` | Hyperliquid=`17.94M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `14.21K` | Last 24h: `22.13K` | Last 3d: `69.43K` | Last 7d: `58.50K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0075%` | **USDT KuCoin** | `0.0018%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0015%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `48.56%` | `51.44%` | `0.94` | 3,950,000.00 USD |
| `15M` | `Binance` | `52.11%` | `47.89%` | `1.09` | 1,680,000.00 USD |
| `15M` | `OKX` | `50.1%` | `49.9%` | `1.00` | 382,590.00 USD |
| `15M` | `Bybit` | `45.18%` | `54.82%` | `0.82` | 204,750.00 USD |
| `15M` | `KuCoin` | `43.59%` | `56.41%` | `0.77` | 35,150.00 USD |
| `15M` | `Gate` | `38.76%` | `61.24%` | `0.63` | 163,750.00 USD |
| `15M` | `Bitget` | `32.57%` | `67.43%` | `0.48` | 163,830.00 USD |
| `15M` | `BingX` | `61.43%` | `38.57%` | `1.59` | 143,000.00 USD |
| `15M` | `MEXC` | `41.27%` | `58.73%` | `0.70` | 124,200.00 USD |
| `15M` | `Bitunix` | `48.47%` | `51.53%` | `0.94` | 75,250.00 USD |
| `15M` | `Hyperliquid` | `28.38%` | `71.62%` | `0.40` | 16,820.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `53.9%` | `46.1%` | `1.17` | 794,410.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 132,490.00 USD |
| `15M` | `HTX` | `51.94%` | `48.06%` | `1.08` | 9,160.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `55.22%` | `44.78%` | `1.23` | 20,040.00 USD |
| `15M` | `Aster` | `52.46%` | `47.54%` | `1.10` | 649.43 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `37.37%` | `62.63%` | `0.60` | 2,460.00 USD |
| `15M` | `Whale Positions` | `52.11%` | `47.89%` | `1.09` | 1,680,000.00 USD |
| `15M` | `Global Accounts` | `48.56%` | `51.44%` | `0.94` | 3,950,000.00 USD |
| `1H` | `AVAX` | `49.71%` | `50.29%` | `0.99` | 23,930,000.00 USD |
| `1H` | `Binance` | `52.95%` | `47.05%` | `1.13` | 8,570,000.00 USD |
| `1H` | `OKX` | `53.98%` | `46.02%` | `1.17` | 2,170,000.00 USD |
| `1H` | `Bybit` | `58.98%` | `41.02%` | `1.44` | 1,690,000.00 USD |
| `1H` | `KuCoin` | `42.48%` | `57.52%` | `0.74` | 154,980.00 USD |
| `1H` | `Gate` | `43.67%` | `56.33%` | `0.78` | 1,080,000.00 USD |
| `1H` | `Bitget` | `46.25%` | `53.75%` | `0.86` | 1,450,000.00 USD |
| `1H` | `BingX` | `28.8%` | `71.2%` | `0.40` | 920,090.00 USD |
| `1H` | `MEXC` | `48.43%` | `51.57%` | `0.94` | 2,500,000.00 USD |
| `1H` | `Bitunix` | `42.62%` | `57.38%` | `0.74` | 583,260.00 USD |
| `1H` | `Hyperliquid` | `71.89%` | `28.11%` | `2.56` | 217,850.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.63%` | `48.37%` | `1.07` | 3,830,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `0.55%` | `99.45%` | `0.01` | 526,590.00 USD |
| `1H` | `HTX` | `57.76%` | `42.24%` | `1.37` | 90,280.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `46.26%` | `53.74%` | `0.86` | 129,130.00 USD |
| `1H` | `Aster` | `27.7%` | `72.3%` | `0.38` | 2,170.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `36.36%` | `63.64%` | `0.57` | 2,570.00 USD |
| `1H` | `Whale Positions` | `52.95%` | `47.05%` | `1.13` | 8,570,000.00 USD |
| `1H` | `Global Accounts` | `49.71%` | `50.29%` | `0.99` | 23,930,000.00 USD |
| `4H` | `AVAX` | `48.28%` | `51.72%` | `0.93` | 88,690,000.00 USD |
| `4H` | `Binance` | `50.39%` | `49.61%` | `1.02` | 31,290,000.00 USD |
| `4H` | `OKX` | `54.19%` | `45.81%` | `1.18` | 7,660,000.00 USD |
| `4H` | `Bybit` | `52.54%` | `47.46%` | `1.11` | 7,480,000.00 USD |
| `4H` | `KuCoin` | `39.42%` | `60.58%` | `0.65` | 664,120.00 USD |
| `4H` | `Gate` | `45.09%` | `54.91%` | `0.82` | 4,280,000.00 USD |
| `4H` | `Bitget` | `48.81%` | `51.19%` | `0.95` | 4,490,000.00 USD |
| `4H` | `BingX` | `32.08%` | `67.92%` | `0.47` | 4,970,000.00 USD |
| `4H` | `MEXC` | `51.6%` | `48.4%` | `1.07` | 6,470,000.00 USD |
| `4H` | `Bitunix` | `50.14%` | `49.86%` | `1.01` | 2,230,000.00 USD |
| `4H` | `Hyperliquid` | `65.07%` | `34.93%` | `1.86` | 481,150.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.24%` | `47.76%` | `1.09` | 14,970,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `0.85%` | `99.15%` | `0.01` | 2,890,000.00 USD |
| `4H` | `HTX` | `45.8%` | `54.2%` | `0.85` | 370,620.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `47.12%` | `52.88%` | `0.89` | 444,000.00 USD |
| `4H` | `Aster` | `65.39%` | `34.61%` | `1.89` | 9,150.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `63.03%` | `36.97%` | `1.70` | 20,120.00 USD |
| `4H` | `Whale Positions` | `50.39%` | `49.61%` | `1.02` | 31,290,000.00 USD |
| `4H` | `Global Accounts` | `48.28%` | `51.72%` | `0.93` | 88,690,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `8.77` | `8.78` | `8.77` | `8.80` | `8.76` | 895,818.33 USD | 668,329.66 USD | 227,488.66 USD | 440,841.00 USD | `+49.21%` | `13B / 5S` |
| `0:00 UTC` | `8.71` | `8.74` | `8.71` | `8.78` | `8.71` | 899,092.10 USD | 311,381.85 USD | 587,710.25 USD | -276,328.40 USD | `-30.73%` | `2B / 27S` |
| `5:00 UTC` | `8.74` | `8.74` | `8.74` | `8.77` | `8.72` | 647,153.63 USD | 422,311.32 USD | 224,842.31 USD | 197,469.01 USD | `+30.51%` | `19B / 2S` |
| `0:00 UTC` | `8.77` | `8.78` | `8.77` | `8.81` | `8.75` | 1,455,460.16 USD | 791,722.04 USD | 663,738.12 USD | 127,983.92 USD | `+8.79%` | `9B / 4S` |
| `5:00 UTC` | `8.80` | `8.79` | `8.80` | `8.81` | `8.76` | 721,263.66 USD | 311,710.76 USD | 409,552.89 USD | -97,842.13 USD | `-13.57%` | `3B / 6S` |
| `0:00 UTC` | `8.80` | `8.81` | `8.80` | `8.84` | `8.78` | 1,475,500.72 USD | 733,191.17 USD | 742,309.55 USD | -9,118.38 USD | `-0.62%` | `6B / 10S` |
| `5:00 UTC` | `8.80` | `8.81` | `8.80` | `8.83` | `8.79` | 963,676.32 USD | 510,514.93 USD | 453,161.39 USD | 57,353.55 USD | `+5.95%` | `7B / 4S` |
| `0:00 UTC` | `8.77` | `8.79` | `8.77` | `8.83` | `8.76` | 2,103,704.78 USD | 974,138.09 USD | 1,129,566.68 USD | -155,428.59 USD | `-7.39%` | `4B / 14S` |
| `5:00 UTC` | `8.83` | `8.82` | `8.83` | `8.85` | `8.78` | 1,356,806.78 USD | 729,514.30 USD | 627,292.47 USD | 102,221.83 USD | `+7.53%` | `11B / 9S` |
| `0:00 UTC` | `8.82` | `8.82` | `8.82` | `8.84` | `8.80` | 849,519.07 USD | 394,689.65 USD | 454,829.42 USD | -60,139.77 USD | `-7.08%` | `3B / 5S` |

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
| `5m` | 646.83 USD | -9,890.00 USD | **`DISTRIBUTION`** |
| `15m` | -40,790.00 USD | 40,360.00 USD | **`DISTRIBUTION`** |
| `30m` | -95,790.00 USD | 39,430.00 USD | **`DISTRIBUTION`** |
| `1h` | -99,880.00 USD | -41,560.00 USD | **`DISTRIBUTION`** |
| `2h` | -248,410.00 USD | 829,060.00 USD | **`ACCUMULATION`** |
| `4h` | -379,800.00 USD | 74,940.00 USD | **`DISTRIBUTION`** |
| `6h` | -407,590.00 USD | 389,580.00 USD | **`DISTRIBUTION`** |
| `8h` | -477,490.00 USD | -73,620.00 USD | **`DISTRIBUTION`** |
| `12h` | 13,320.00 USD | -312,860.00 USD | **`DISTRIBUTION`** |
| `24h` | 88,750.00 USD | -336,550.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,910,000.00 USD | -42,930,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -51,830,000.00 USD | -275,110,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+646.83` | 15m=`-40.79K` | 1h=`-99.88K` | 24h=`+88.75K`
* Futures Capital Netflows: 5m=`-9.89K` | 15m=`+40.36K` | 1h=`-41.56K` | 24h=`-336.55K`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `8.59` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.47` (Risk Distance: `0.1185` pts)
  * +2.5R Take Profit: `8.89`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.81` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.93` (Risk Distance: `0.1185` pts)
  * +2.5R Take Profit: `8.51`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.90`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
