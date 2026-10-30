# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:48:54 IST` (`2026-10-30 11:18:54 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.55` | **Live Ask Quote**: `8.58` | **Mid Price**: `8.57`
- **Spread Points**: `3.00` | **Spread BPS**: `35.03 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.34` | VWAP Z-Score: `+1.33` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0591` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `63.59` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `8.88` | Lower -3.00σ Band: `7.81`
  * Upper +2.51σ Band: `8.79` | Lower -2.51σ Band: `7.90`
  * Upper +2.01σ Band: `8.70` | Lower -2.01σ Band: `7.99`
  * Upper +2.00σ Band: `8.70` | Lower -2.00σ Band: `7.99`
  * Upper +1.28σ Band: `8.57` | Lower -1.28σ Band: `8.12`
  * Upper +1.00σ Band: `8.52` | Lower -1.00σ Band: `8.17`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.50` | EMA-20=`8.48` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.48` (Slope: `+0.0000`) | EMA-100=`8.54`
  * Institutional Anchors: EMA-144=`8.59` | EMA-200=`8.65` (Slope: `-0.2642`) | EMA-233=`8.67`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`7.97` | Weekly High=`9.14` | Weekly Low=`7.97`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.59` (Distance: `-0.33%`)
  * Point of Control (POC) = `8.46` (Distance: `+1.25%`)
  * Value Area Low (VAL) = `8.25` (Distance: `+3.77%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`9.03` | Weekly POC=`8.92` | Weekly VAL=`8.68`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.58` | Low=`7.97`
  * London Session (08:00-16:00 UTC): High=`8.64` | Low=`8.42`
  * New York Session (13:00-21:00 UTC): High=`8.59` | Low=`8.43`
  * Initial Balance (First Hour): IB High=`8.59` | IB Low=`8.50`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.53` - `8.60`
  * Optimal Trade Entry (OTE 0.705): `8.58`
  * Structural Invalidation Anchor (0.786): `8.63`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.60` | `8.62` | `8.58` | `8.58` | `63,760` | 548,149.20 USD | -92,278.76 USD | `-16.83%` | -5,029,192.25 USD | `-0.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `8.58` | `8.59` | `8.57` | `8.58` | `28,815` | 247,177.17 USD | -26,037.48 USD | `-10.53%` | -5,055,229.73 USD | `-0.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `8.58` | `8.58` | `8.57` | `8.57` | `5,556` | 47,652.35 USD | -4,476.15 USD | `-9.39%` | -5,059,705.88 USD | `-0.28` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `8.51` | `8.56` | `8.50` | `8.55` | `127,080` | 1,085,360.20 USD | 147,649.89 USD | `+13.60%` | -5,387,782.67 USD | `+0.50` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `8.56` | `8.60` | `8.53` | `8.60` | `121,252` | 1,039,077.87 USD | 450,869.18 USD | `+43.39%` | -4,936,913.49 USD | `+1.29` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.60` | `8.62` | `8.57` | `8.57` | `98,135` | 843,013.01 USD | -122,758.10 USD | `-14.56%` | -5,059,671.59 USD | `-0.43` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `8.48` | `8.51` | `8.44` | `8.49` | `406,103` | 3,439,281.91 USD | -233,726.45 USD | `-6.80%` | -5,798,525.18 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `8.49` | `8.60` | `8.46` | `8.60` | `451,182` | 3,846,932.02 USD | 844,817.04 USD | `+21.96%` | -4,953,708.14 USD | `+0.63` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `8.60` | `8.62` | `8.57` | `8.57` | `98,135` | 843,013.01 USD | -122,758.10 USD | `-14.56%` | -5,076,466.24 USD | `+0.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.62` | `8.44` | `8.57` | `1,394,446` | 11,853,065.54 USD | 328,339.47 USD | `+2.77%` | -5,076,500.53 USD | `+0.77` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,565,817.62 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,901,763.44 USD | `-0.98` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.62` | `8.44` | `8.57` | `1,394,446` | 11,853,065.54 USD | 328,339.47 USD | `+2.77%` | -5,076,500.53 USD | `+0.77` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`8.57`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BUY` | `8.42` | `60660.7100` | 511,054.35 USD | 511,054.35 USD | `LARGE (>= USD 100K)` | `-1.71%` | `0x71cfa5e263` |
| `BUY` | `8.42` | `399.8500` | 3,368.38 USD | 4,478,601.34 USD | `STANDARD` | `-1.72%` | `0x14f8e04290` |
| `BUY` | `8.43` | `171.9900` | 1,450.67 USD | 4,540,925.73 USD | `STANDARD` | `-1.60%` | `0x010461c14e` |
| `BUY` | `8.44` | `176.5100` | 1,489.82 USD | 4,539,475.06 USD | `STANDARD` | `-1.53%` | `0x31ca8395cf` |
| `BUY` | `8.45` | `17182.1600` | 145,144.58 USD | 1,637,857.94 USD | `LARGE (>= USD 100K)` | `-1.45%` | `0x71d0e11ebb` |
| `BUY` | `8.45` | `14470.5200` | 122,203.54 USD | 2,546,383.70 USD | `LARGE (>= USD 100K)` | `-1.48%` | `0xecb63caa47` |
| `BUY` | `8.45` | `2248.8600` | 18,999.94 USD | 3,335,192.76 USD | `STANDARD` | `-1.44%` | `0x0efb38a5fa` |
| `BUY` | `8.45` | `2139.7000` | 18,082.60 USD | 3,446,683.58 USD | `STANDARD` | `-1.41%` | `0xd3943e4008` |
| `BUY` | `8.45` | `315.7300` | 2,668.87 USD | 4,500,427.20 USD | `STANDARD` | `-1.39%` | `0x07fd993f0f` |
| `BUY` | `8.46` | `11522.2600` | 97,494.45 USD | 2,844,161.46 USD | `MEDIUM (>= USD 25K)` | `-1.29%` | `0xecb63caa47` |
| `BUY` | `8.46` | `98.3400` | 832.21 USD | 4,553,223.13 USD | `STANDARD` | `-1.27%` | `0xdadbb4b2a0` |
| `BUY` | `8.47` | `7465.8000` | 63,242.05 USD | 3,132,209.34 USD | `MEDIUM (>= USD 25K)` | `-1.18%` | `0x71d0e11ebb` |
| `BUY` | `8.47` | `1888.3700` | 15,999.97 USD | 3,478,683.53 USD | `STANDARD` | `-1.15%` | `0x0efb38a5fa` |
| `BUY` | `8.47` | `1764.7000` | 14,955.83 USD | 3,946,198.36 USD | `STANDARD` | `-1.13%` | `0xd3943e4008` |
| `BUY` | `8.47` | `398.7200` | 3,377.36 USD | 4,471,863.01 USD | `STANDARD` | `-1.18%` | `0x14f8e04290` |
| `BUY` | `8.47` | `90.2200` | 764.24 USD | 4,555,523.70 USD | `STANDARD` | `-1.18%` | `0x010461c14e` |
| `BUY` | `8.47` | `87.1300` | 738.19 USD | 4,557,749.24 USD | `STANDARD` | `-1.16%` | `0x31ca8395cf` |
| `BUY` | `8.48` | `9629.2300` | 81,642.39 USD | 2,925,803.85 USD | `MEDIUM (>= USD 25K)` | `-1.09%` | `0xecb63caa47` |
| `BUY` | `8.49` | `17172.4500` | 145,830.16 USD | 1,492,713.36 USD | `LARGE (>= USD 100K)` | `-0.93%` | `0x71d0e11ebb` |
| `BUY` | `8.49` | `588.4000` | 4,993.63 USD | 4,375,578.30 USD | `STANDARD` | `-0.99%` | `0x3ca146d269` |
| `BUY` | `8.50` | `31288.0800` | 266,067.57 USD | 1,048,930.51 USD | `LARGE (>= USD 100K)` | `-0.79%` | `0x71cfa5e263` |
| `BUY` | `8.50` | `9227.8600` | 78,398.05 USD | 3,004,201.90 USD | `MEDIUM (>= USD 25K)` | `-0.89%` | `0xecb63caa47` |
| `BUY` | `8.50` | `1417.9000` | 12,058.25 USD | 3,999,324.87 USD | `STANDARD` | `-0.79%` | `0xd3943e4008` |
| `BUY` | `8.50` | `396.6800` | 3,369.96 USD | 4,475,232.96 USD | `STANDARD` | `-0.89%` | `0x14f8e04290` |
| `BUY` | `8.50` | `234.4200` | 1,992.57 USD | 4,527,889.09 USD | `STANDARD` | `-0.84%` | `0x93f0435268` |
| `BUY` | `8.51` | `11771.9400` | 100,143.89 USD | 2,646,527.60 USD | `LARGE (>= USD 100K)` | `-0.76%` | `0x881cd92459` |
| `BUY` | `8.51` | `1409.6000` | 11,999.92 USD | 4,035,324.72 USD | `STANDARD` | `-0.69%` | `0x0efb38a5fa` |
| `BUY` | `8.51` | `1250.0000` | 10,635.25 USD | 4,113,152.90 USD | `STANDARD` | `-0.74%` | `0xb7bd9cef0e` |
| `BUY` | `8.51` | `183.6400` | 1,562.52 USD | 4,536,470.28 USD | `STANDARD` | `-0.74%` | `0xdadbb4b2a0` |
| `BUY` | `8.52` | `14940.3900` | 127,254.77 USD | 2,424,180.16 USD | `LARGE (>= USD 100K)` | `-0.63%` | `0x71d0e11ebb` |
| `BUY` | `8.52` | `3330.8100` | 28,368.84 USD | 3,292,306.55 USD | `MEDIUM (>= USD 25K)` | `-0.64%` | `0x26934acbd3` |
| `BUY` | `8.52` | `83.0600` | 708.03 USD | 4,625,468.46 USD | `STANDARD` | `-0.55%` | `0xa382fa9f4b` |
| `BUY` | `8.52` | `83.0600` | 707.97 USD | 4,626,176.43 USD | `STANDARD` | `-0.56%` | `0xea0e878d5d` |
| `BUY` | `8.52` | `83.0600` | 707.91 USD | 4,626,884.34 USD | `STANDARD` | `-0.57%` | `0xd0956a1eba` |
| `BUY` | `8.52` | `83.0600` | 707.85 USD | 4,627,592.20 USD | `STANDARD` | `-0.58%` | `0x9d81a3adf8` |
| `BUY` | `8.52` | `83.0600` | 707.74 USD | 4,628,299.93 USD | `STANDARD` | `-0.59%` | `0xf30120f048` |
| `BUY` | `8.52` | `75.4200` | 642.28 USD | 4,634,338.04 USD | `STANDARD` | `-0.65%` | `0x31ca8395cf` |
| `BUY` | `8.52` | `62.2900` | 530.80 USD | 4,638,925.31 USD | `STANDARD` | `-0.59%` | `0xfd66e33095` |
| `BUY` | `8.53` | `1246.1900` | 10,629.63 USD | 4,123,782.53 USD | `STANDARD` | `-0.49%` | `0xd3943e4008` |
| `BUY` | `8.53` | `830.0000` | 7,079.65 USD | 4,320,441.00 USD | `STANDARD` | `-0.49%` | `0xb7bd9cef0e` |
| `BUY` | `8.53` | `454.5600` | 3,878.22 USD | 4,447,470.38 USD | `STANDARD` | `-0.47%` | `0xcd7f60e943` |
| `BUY` | `8.53` | `83.0600` | 708.14 USD | 4,624,052.34 USD | `STANDARD` | `-0.54%` | `0x53136b4a7c` |
| `BUY` | `8.53` | `83.0600` | 708.09 USD | 4,624,760.43 USD | `STANDARD` | `-0.55%` | `0xfd66e33095` |
| `BUY` | `8.53` | `81.3200` | 693.30 USD | 4,628,993.24 USD | `STANDARD` | `-0.54%` | `0x010461c14e` |
| `BUY` | `8.54` | `15957.9000` | 136,342.70 USD | 1,912,163.49 USD | `LARGE (>= USD 100K)` | `-0.33%` | `0x71cfa5e263` |
| `BUY` | `8.54` | `14939.3100` | 127,635.49 USD | 2,296,925.39 USD | `LARGE (>= USD 100K)` | `-0.33%` | `0x71d0e11ebb` |
| `BUY` | `8.54` | `1756.8400` | 15,004.47 USD | 3,916,243.69 USD | `STANDARD` | `-0.36%` | `0x57d8e75f47` |
| `BUY` | `8.54` | `1756.8400` | 14,998.85 USD | 3,931,242.53 USD | `STANDARD` | `-0.40%` | `0x57d8e75f47` |
| `BUY` | `8.54` | `1026.1900` | 8,762.64 USD | 4,243,460.00 USD | `STANDARD` | `-0.38%` | `0xd3943e4008` |
| `BUY` | `8.54` | `937.1800` | 7,999.96 USD | 4,267,836.23 USD | `STANDARD` | `-0.42%` | `0x0efb38a5fa` |
| `BUY` | `8.54` | `722.5600` | 6,169.36 USD | 4,333,289.45 USD | `STANDARD` | `-0.39%` | `0xecb63caa47` |
| `BUY` | `8.54` | `611.1100` | 5,220.59 USD | 4,350,509.73 USD | `STANDARD` | `-0.34%` | `0xecb63caa47` |
| `BUY` | `8.54` | `455.5400` | 3,889.13 USD | 4,443,592.16 USD | `STANDARD` | `-0.40%` | `0x2a72b57dea` |
| `BUY` | `8.54` | `84.8300` | 724.74 USD | 4,558,473.98 USD | `STANDARD` | `-0.33%` | `0x010461c14e` |
| `BUY` | `8.54` | `83.0600` | 709.71 USD | 4,622,634.54 USD | `STANDARD` | `-0.32%` | `0x63f6411ca6` |
| `BUY` | `8.54` | `83.0600` | 709.66 USD | 4,623,344.20 USD | `STANDARD` | `-0.32%` | `0xf30120f048` |
| `BUY` | `8.54` | `73.9800` | 632.04 USD | 4,635,602.23 USD | `STANDARD` | `-0.33%` | `0x31ca8395cf` |
| `BUY` | `8.55` | `3689.1100` | 31,548.90 USD | 3,263,937.70 USD | `MEDIUM (>= USD 25K)` | `-0.23%` | `0x08a49e7f71` |
| `BUY` | `8.55` | `2198.6600` | 18,792.17 USD | 3,372,984.87 USD | `STANDARD` | `-0.29%` | `0xa38f19c4cc` |
| `BUY` | `8.55` | `1756.8400` | 15,029.77 USD | 3,856,181.54 USD | `STANDARD` | `-0.20%` | `0x57d8e75f47` |
| `BUY` | `8.55` | `1756.8400` | 15,025.55 USD | 3,871,207.09 USD | `STANDARD` | `-0.22%` | `0x57d8e75f47` |
| `BUY` | `8.55` | `1756.8400` | 15,019.05 USD | 3,886,226.14 USD | `STANDARD` | `-0.27%` | `0x57d8e75f47` |
| `BUY` | `8.55` | `1756.8400` | 15,013.08 USD | 3,901,239.22 USD | `STANDARD` | `-0.31%` | `0x57d8e75f47` |
| `BUY` | `8.55` | `1197.9600` | 10,245.31 USD | 4,175,141.95 USD | `STANDARD` | `-0.23%` | `0xaf9f722a67` |
| `BUY` | `8.55` | `1113.1700` | 9,519.27 USD | 4,234,697.37 USD | `STANDARD` | `-0.24%` | `0x26934acbd3` |
| `BUY` | `8.55` | `979.8500` | 8,375.76 USD | 4,251,835.76 USD | `STANDARD` | `-0.28%` | `0xd3943e4008` |
| `BUY` | `8.55` | `832.1400` | 7,113.80 USD | 4,313,361.35 USD | `STANDARD` | `-0.27%` | `0xecb63caa47` |
| `BUY` | `8.55` | `584.9800` | 4,999.94 USD | 4,370,584.67 USD | `STANDARD` | `-0.29%` | `0x0efb38a5fa` |
| `BUY` | `8.55` | `517.2800` | 4,422.54 USD | 4,380,000.84 USD | `STANDARD` | `-0.26%` | `0xecb63caa47` |
| `BUY` | `8.55` | `481.6400` | 4,120.19 USD | 4,396,659.95 USD | `STANDARD` | `-0.20%` | `0x7717a7a245` |
| `BUY` | `8.55` | `455.5400` | 3,892.82 USD | 4,439,703.04 USD | `STANDARD` | `-0.31%` | `0x2a72b57dea` |
| `BUY` | `8.55` | `420.0000` | 3,591.13 USD | 4,454,671.15 USD | `STANDARD` | `-0.25%` | `0xb7bd9cef0e` |
| `BUY` | `8.55` | `83.0600` | 710.55 USD | 4,615,532.78 USD | `STANDARD` | `-0.20%` | `0xea0e878d5d` |
| `BUY` | `8.55` | `83.0600` | 710.48 USD | 4,616,243.26 USD | `STANDARD` | `-0.21%` | `0xf30120f048` |
| `BUY` | `8.55` | `83.0600` | 710.47 USD | 4,616,953.73 USD | `STANDARD` | `-0.21%` | `0x63f6411ca6` |
| `BUY` | `8.55` | `83.0600` | 710.41 USD | 4,617,664.14 USD | `STANDARD` | `-0.22%` | `0xfd66e33095` |
| `BUY` | `8.55` | `83.0600` | 710.39 USD | 4,618,374.53 USD | `STANDARD` | `-0.22%` | `0x9d81a3adf8` |
| `BUY` | `8.55` | `83.0600` | 710.33 USD | 4,619,084.86 USD | `STANDARD` | `-0.23%` | `0xd0956a1eba` |
| `BUY` | `8.55` | `83.0600` | 710.14 USD | 4,619,795.00 USD | `STANDARD` | `-0.26%` | `0x63f6411ca6` |
| `BUY` | `8.55` | `83.0600` | 710.08 USD | 4,620,505.08 USD | `STANDARD` | `-0.27%` | `0x9d81a3adf8` |
| `BUY` | `8.55` | `83.0600` | 709.95 USD | 4,621,215.02 USD | `STANDARD` | `-0.28%` | `0xa382fa9f4b` |
| `BUY` | `8.55` | `83.0600` | 709.80 USD | 4,621,924.82 USD | `STANDARD` | `-0.31%` | `0x9d81a3adf8` |
| `BUY` | `8.56` | `1756.8400` | 15,042.59 USD | 3,811,079.59 USD | `STANDARD` | `-0.11%` | `0x57d8e75f47` |
| `BUY` | `8.56` | `1756.8400` | 15,038.20 USD | 3,826,117.79 USD | `STANDARD` | `-0.14%` | `0x57d8e75f47` |
| `BUY` | `8.56` | `1756.8400` | 15,033.98 USD | 3,841,151.78 USD | `STANDARD` | `-0.17%` | `0x57d8e75f47` |
| `BUY` | `8.56` | `1401.8400` | 11,999.89 USD | 4,047,324.61 USD | `STANDARD` | `-0.14%` | `0x7d0c59691f` |
| `BUY` | `8.56` | `1315.7500` | 11,262.82 USD | 4,069,850.43 USD | `STANDARD` | `-0.14%` | `0x08a49e7f71` |
| `BUY` | `8.56` | `1197.9600` | 10,255.50 USD | 4,164,896.63 USD | `STANDARD` | `-0.13%` | `0xaf9f722a67` |
| `BUY` | `8.56` | `1167.9300` | 9,999.58 USD | 4,215,483.64 USD | `STANDARD` | `-0.12%` | `0x7d0c59691f` |
| `BUY` | `8.56` | `934.1400` | 7,999.79 USD | 4,283,835.96 USD | `STANDARD` | `-0.09%` | `0x7d0c59691f` |
| `BUY` | `8.56` | `490.0400` | 4,193.96 USD | 4,388,401.79 USD | `STANDARD` | `-0.16%` | `0x71d0e11ebb` |
| `BUY` | `8.56` | `455.5400` | 3,900.52 USD | 4,431,913.03 USD | `STANDARD` | `-0.11%` | `0x2a72b57dea` |
| `BUY` | `8.56` | `455.5400` | 3,897.19 USD | 4,435,810.22 USD | `STANDARD` | `-0.19%` | `0x2a72b57dea` |
| `BUY` | `8.56` | `323.1400` | 2,766.37 USD | 4,484,186.49 USD | `STANDARD` | `-0.13%` | `0xecb63caa47` |
| `BUY` | `8.56` | `312.0500` | 2,671.68 USD | 4,497,758.33 USD | `STANDARD` | `-0.12%` | `0x7717a7a245` |
| `BUY` | `8.56` | `297.9200` | 2,549.66 USD | 4,505,600.55 USD | `STANDARD` | `-0.16%` | `0xecb63caa47` |
| `BUY` | `8.56` | `291.9200` | 2,499.92 USD | 4,510,600.46 USD | `STANDARD` | `-0.09%` | `0x0efb38a5fa` |
| `BUY` | `8.56` | `281.5300` | 2,408.83 USD | 4,515,449.41 USD | `STANDARD` | `-0.18%` | `0xecb63caa47` |
| `BUY` | `8.56` | `245.1700` | 2,097.53 USD | 4,519,832.94 USD | `STANDARD` | `-0.19%` | `0xecb63caa47` |
| `BUY` | `8.56` | `233.7000` | 2,000.10 USD | 4,525,896.52 USD | `STANDARD` | `-0.16%` | `0x39bac00809` |
| `BUY` | `8.56` | `214.3300` | 1,835.05 USD | 4,531,612.12 USD | `STANDARD` | `-0.12%` | `0x26934acbd3` |
| `BUY` | `8.56` | `84.0800` | 719.41 USD | 4,559,916.44 USD | `STANDARD` | `-0.18%` | `0x010461c14e` |
| `BUY` | `8.56` | `83.5800` | 715.13 USD | 4,572,082.43 USD | `STANDARD` | `-0.18%` | `0x31ca8395cf` |
| `BUY` | `8.56` | `83.0600` | 711.39 USD | 4,605,579.72 USD | `STANDARD` | `-0.08%` | `0xea0e878d5d` |
| `BUY` | `8.56` | `83.0600` | 711.35 USD | 4,606,291.07 USD | `STANDARD` | `-0.09%` | `0x9d81a3adf8` |
| `BUY` | `8.56` | `83.0600` | 711.32 USD | 4,607,002.39 USD | `STANDARD` | `-0.09%` | `0xfd66e33095` |
| `BUY` | `8.56` | `83.0600` | 711.20 USD | 4,607,713.59 USD | `STANDARD` | `-0.11%` | `0x9d81a3adf8` |
| `BUY` | `8.56` | `83.0600` | 711.15 USD | 4,608,424.74 USD | `STANDARD` | `-0.12%` | `0xd0956a1eba` |
| `BUY` | `8.56` | `83.0600` | 711.08 USD | 4,609,135.82 USD | `STANDARD` | `-0.13%` | `0xf30120f048` |
| `BUY` | `8.56` | `83.0600` | 711.01 USD | 4,609,846.83 USD | `STANDARD` | `-0.14%` | `0xea0e878d5d` |
| `BUY` | `8.56` | `83.0600` | 710.99 USD | 4,610,557.81 USD | `STANDARD` | `-0.14%` | `0x53136b4a7c` |
| `BUY` | `8.56` | `83.0600` | 710.88 USD | 4,611,268.69 USD | `STANDARD` | `-0.15%` | `0x63f6411ca6` |
| `BUY` | `8.56` | `83.0600` | 710.82 USD | 4,611,979.51 USD | `STANDARD` | `-0.16%` | `0xfd66e33095` |
| `BUY` | `8.56` | `83.0600` | 710.79 USD | 4,612,690.29 USD | `STANDARD` | `-0.17%` | `0x53136b4a7c` |
| `BUY` | `8.56` | `83.0600` | 710.70 USD | 4,613,401.00 USD | `STANDARD` | `-0.18%` | `0x9d81a3adf8` |
| `BUY` | `8.56` | `83.0600` | 710.64 USD | 4,614,111.64 USD | `STANDARD` | `-0.19%` | `0xd0956a1eba` |
| `BUY` | `8.56` | `83.0600` | 710.59 USD | 4,614,822.24 USD | `STANDARD` | `-0.19%` | `0xf30120f048` |
| `BUY` | `8.56` | `62.2900` | 533.38 USD | 4,638,394.51 USD | `STANDARD` | `-0.10%` | `0x63f6411ca6` |
| `BUY` | `8.56` | `60.3400` | 516.56 USD | 4,642,030.10 USD | `STANDARD` | `-0.13%` | `0x57d8e75f47` |
| `BUY` | `8.56` | `60.3400` | 516.22 USD | 4,642,546.32 USD | `STANDARD` | `-0.19%` | `0x57d8e75f47` |
| `ASK` | `8.57` | `11.6700` | 100.07 USD | 10,242.59 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.57` | `83.0600` | 712.21 USD | 10,142.52 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.57` | `83.0600` | 712.15 USD | 9,430.31 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.57` | `233.9700` | 2,005.90 USD | 8,718.16 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `8.57` | `83.0600` | 712.05 USD | 6,712.27 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.57` | `699.9300` | 6,000.22 USD | 6,000.22 USD | `1 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `8.57` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.57` | `0.00%` | `-` |
| `BID` | `8.57` | `144.4500` | 1,238.08 USD | 1,238.08 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.57` | `17.6300` | 151.10 USD | 1,389.18 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.57` | `83.0600` | 711.87 USD | 2,101.05 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.57` | `20.4000` | 174.83 USD | 2,275.88 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.57` | `133.8300` | 1,146.92 USD | 3,422.80 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.57` | `83.0600` | 711.81 USD | 4,134.61 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.57` | `102.4600` | 878.03 USD | 5,012.64 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.57` | `1756.8400` | 15,055.06 USD | 20,067.71 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.57` | `83.0600` | 711.70 USD | 20,779.41 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.57` | `83.0600` | 711.69 USD | 21,491.10 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.57` | `220.3500` | 1,887.98 USD | 23,379.08 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.57` | `1.9000` | 16.28 USD | 23,395.36 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.57` | `203.1400` | 1,740.44 USD | 25,135.80 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.57` | `83.0600` | 711.58 USD | 25,847.38 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.57` | `776.9300` | 6,655.96 USD | 32,503.34 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `8.57` | `5.4600` | 46.78 USD | 32,550.12 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.57` | `83.0600` | 711.53 USD | 33,261.64 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.57` | `116.7300` | 999.94 USD | 34,261.59 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.57` | `84.4100` | 723.06 USD | 34,984.64 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.57` | `5.8000` | 49.68 USD | 35,034.33 USD | `2 orders` | `-0.07%` | `-` |
| `BUY` | `8.57` | `1756.8400` | 15,055.06 USD | 3,780,988.97 USD | `STANDARD` | `-0.03%` | `0x57d8e75f47` |
| `BUY` | `8.57` | `1756.8400` | 15,048.04 USD | 3,796,037.00 USD | `STANDARD` | `-0.07%` | `0x57d8e75f47` |
| `BUY` | `8.57` | `1186.1000` | 10,159.30 USD | 4,195,484.04 USD | `STANDARD` | `-0.08%` | `0x621c555167` |
| `SELL` | `8.57` | `699.9300` | 6,000.22 USD | 4,339,289.67 USD | `STANDARD` | `+0.01%` | `0x7d0c59691f` |
| `BUY` | `8.57` | `700.3000` | 5,999.47 USD | 4,345,289.14 USD | `STANDARD` | `-0.06%` | `0x7d0c59691f` |
| `BUY` | `8.57` | `220.3500` | 1,887.98 USD | 4,529,777.07 USD | `STANDARD` | `-0.04%` | `0x414ade317c` |
| `SELL` | `8.57` | `150.9100` | 1,293.80 USD | 4,542,219.53 USD | `STANDARD` | `+0.02%` | `0x727956612a` |
| `BUY` | `8.57` | `144.4500` | 1,238.08 USD | 4,543,457.61 USD | `STANDARD` | `-0.01%` | `0x727956612a` |
| `BUY` | `8.57` | `133.8300` | 1,146.92 USD | 4,544,604.53 USD | `STANDARD` | `-0.02%` | `0xecb63caa47` |
| `BUY` | `8.57` | `120.0800` | 1,028.81 USD | 4,546,663.11 USD | `STANDARD` | `-0.05%` | `0x7717a7a245` |
| `BUY` | `8.57` | `116.7300` | 999.94 USD | 4,549,664.55 USD | `STANDARD` | `-0.06%` | `0x0eecd62efb` |
| `BUY` | `8.57` | `84.4100` | 723.06 USD | 4,559,197.03 USD | `STANDARD` | `-0.07%` | `0x31ca8395cf` |
| `SELL` | `8.57` | `83.0600` | 712.21 USD | 4,595,615.53 USD | `STANDARD` | `+0.03%` | `0x53136b4a7c` |
| `SELL` | `8.57` | `83.0600` | 712.15 USD | 4,596,327.68 USD | `STANDARD` | `+0.02%` | `0xd0956a1eba` |
| `SELL` | `8.57` | `83.0600` | 712.10 USD | 4,597,039.78 USD | `STANDARD` | `+0.02%` | `0x63f6411ca6` |
| `SELL` | `8.57` | `83.0600` | 712.05 USD | 4,597,751.83 USD | `STANDARD` | `+0.01%` | `0x9d81a3adf8` |
| `BUY` | `8.57` | `83.0600` | 711.87 USD | 4,598,463.69 USD | `STANDARD` | `-0.02%` | `0xea0e878d5d` |
| `BUY` | `8.57` | `83.0600` | 711.81 USD | 4,599,175.50 USD | `STANDARD` | `-0.02%` | `0x63f6411ca6` |
| `BUY` | `8.57` | `83.0600` | 711.78 USD | 4,599,887.28 USD | `STANDARD` | `-0.03%` | `0xfd66e33095` |
| `BUY` | `8.57` | `83.0600` | 711.70 USD | 4,600,598.98 USD | `STANDARD` | `-0.04%` | `0xea0e878d5d` |
| `BUY` | `8.57` | `83.0600` | 711.69 USD | 4,601,310.67 USD | `STANDARD` | `-0.04%` | `0x9d81a3adf8` |
| `BUY` | `8.57` | `83.0600` | 711.63 USD | 4,602,022.31 USD | `STANDARD` | `-0.05%` | `0xea0e878d5d` |
| `BUY` | `8.57` | `83.0600` | 711.58 USD | 4,602,733.89 USD | `STANDARD` | `-0.05%` | `0x63f6411ca6` |
| `BUY` | `8.57` | `83.0600` | 711.53 USD | 4,603,445.42 USD | `STANDARD` | `-0.06%` | `0xd0956a1eba` |
| `BUY` | `8.57` | `83.0600` | 711.46 USD | 4,604,156.88 USD | `STANDARD` | `-0.07%` | `0xf30120f048` |
| `BUY` | `8.57` | `83.0600` | 711.45 USD | 4,604,868.33 USD | `STANDARD` | `-0.07%` | `0xea0e878d5d` |
| `BUY` | `8.57` | `76.6300` | 656.49 USD | 4,633,695.77 USD | `STANDARD` | `-0.06%` | `0x010461c14e` |
| `BUY` | `8.57` | `60.3400` | 516.85 USD | 4,641,513.54 USD | `STANDARD` | `-0.07%` | `0x57d8e75f47` |
| `ASK` | `8.58` | `78.2600` | 671.28 USD | 38,948.49 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.58` | `16.9900` | 145.73 USD | 38,277.22 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.58` | `1165.8700` | 10,000.02 USD | 38,131.49 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.58` | `83.0600` | 712.42 USD | 28,131.47 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.58` | `112.8500` | 967.88 USD | 27,419.05 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.58` | `5.8000` | 49.74 USD | 26,451.17 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.58` | `60.3400` | 517.49 USD | 26,401.43 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.58` | `467.2600` | 4,007.27 USD | 25,883.94 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.58` | `83.0600` | 712.32 USD | 21,876.67 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.58` | `27.9000` | 239.26 USD | 21,164.35 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.58` | `120.0800` | 1,029.77 USD | 20,925.08 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.58` | `932.9500` | 8,000.51 USD | 19,895.31 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.58` | `109.6100` | 939.95 USD | 11,894.80 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.58` | `83.0600` | 712.26 USD | 10,954.85 USD | `1 orders` | `+0.04%` | `-` |
| `SELL` | `8.58` | `1756.8400` | 15,082.30 USD | 3,735,783.19 USD | `STANDARD` | `+0.15%` | `0x57d8e75f47` |
| `SELL` | `8.58` | `1756.8400` | 15,077.90 USD | 3,750,861.09 USD | `STANDARD` | `+0.12%` | `0x57d8e75f47` |
| `SELL` | `8.58` | `1756.8400` | 15,072.81 USD | 3,765,933.90 USD | `STANDARD` | `+0.09%` | `0x57d8e75f47` |
| `SELL` | `8.58` | `1398.6500` | 12,000.00 USD | 4,011,324.86 USD | `STANDARD` | `+0.09%` | `0x7d0c59691f` |
| `SELL` | `8.58` | `1312.4900` | 11,263.00 USD | 4,058,587.61 USD | `STANDARD` | `+0.11%` | `0x08a49e7f71` |
| `SELL` | `8.58` | `1197.9600` | 10,275.98 USD | 4,154,641.14 USD | `STANDARD` | `+0.07%` | `0xaf9f722a67` |
| `SELL` | `8.58` | `1165.8700` | 10,000.02 USD | 4,205,484.05 USD | `STANDARD` | `+0.06%` | `0x7d0c59691f` |
| `SELL` | `8.58` | `932.9500` | 8,000.51 USD | 4,259,836.27 USD | `STANDARD` | `+0.04%` | `0x7d0c59691f` |
| `SELL` | `8.58` | `490.1600` | 4,206.99 USD | 4,384,207.84 USD | `STANDARD` | `+0.13%` | `0x71d0e11ebb` |
| `SELL` | `8.58` | `460.4500` | 3,952.46 USD | 4,400,612.40 USD | `STANDARD` | `+0.14%` | `0xecb63caa47` |
| `SELL` | `8.58` | `455.5400` | 3,909.26 USD | 4,424,105.76 USD | `STANDARD` | `+0.11%` | `0x2a72b57dea` |
| `SELL` | `8.58` | `455.5400` | 3,906.76 USD | 4,428,012.51 USD | `STANDARD` | `+0.05%` | `0x2a72b57dea` |
| `SELL` | `8.58` | `312.0500` | 2,677.61 USD | 4,495,086.65 USD | `STANDARD` | `+0.10%` | `0x7717a7a245` |
| `SELL` | `8.58` | `291.3200` | 2,499.99 USD | 4,508,100.54 USD | `STANDARD` | `+0.11%` | `0x0efb38a5fa` |
| `SELL` | `8.58` | `120.0800` | 1,029.77 USD | 4,545,634.30 USD | `STANDARD` | `+0.05%` | `0x7717a7a245` |
| `SELL` | `8.58` | `116.5800` | 999.98 USD | 4,548,664.61 USD | `STANDARD` | `+0.07%` | `0x0eecd62efb` |
| `SELL` | `8.58` | `109.6100` | 939.95 USD | 4,550,604.50 USD | `STANDARD` | `+0.04%` | `0xecb63caa47` |
| `SELL` | `8.58` | `107.2200` | 920.42 USD | 4,551,524.92 USD | `STANDARD` | `+0.15%` | `0x2eddf3aa5c` |
| `SELL` | `8.58` | `86.1800` | 739.63 USD | 4,557,011.05 USD | `STANDARD` | `+0.12%` | `0x31ca8395cf` |
| `SELL` | `8.58` | `83.0600` | 713.05 USD | 4,584,213.79 USD | `STANDARD` | `+0.15%` | `0x9d81a3adf8` |
| `SELL` | `8.58` | `83.0600` | 713.02 USD | 4,584,926.81 USD | `STANDARD` | `+0.15%` | `0x53136b4a7c` |
| `SELL` | `8.58` | `83.0600` | 712.96 USD | 4,585,639.77 USD | `STANDARD` | `+0.14%` | `0xfd66e33095` |
| `SELL` | `8.58` | `83.0600` | 712.89 USD | 4,586,352.66 USD | `STANDARD` | `+0.13%` | `0x63f6411ca6` |
| `SELL` | `8.58` | `83.0600` | 712.85 USD | 4,587,065.50 USD | `STANDARD` | `+0.12%` | `0xea0e878d5d` |
| `SELL` | `8.58` | `83.0600` | 712.76 USD | 4,587,778.27 USD | `STANDARD` | `+0.11%` | `0xf30120f048` |
| `SELL` | `8.58` | `83.0600` | 712.73 USD | 4,588,490.99 USD | `STANDARD` | `+0.11%` | `0xa382fa9f4b` |
| `SELL` | `8.58` | `83.0600` | 712.69 USD | 4,589,203.68 USD | `STANDARD` | `+0.10%` | `0xfd66e33095` |
| `SELL` | `8.58` | `83.0600` | 712.62 USD | 4,589,916.30 USD | `STANDARD` | `+0.09%` | `0xa382fa9f4b` |
| `SELL` | `8.58` | `83.0600` | 712.60 USD | 4,590,628.91 USD | `STANDARD` | `+0.09%` | `0xa382fa9f4b` |
| `SELL` | `8.58` | `83.0600` | 712.56 USD | 4,591,341.46 USD | `STANDARD` | `+0.08%` | `0x53136b4a7c` |
| `SELL` | `8.58` | `83.0600` | 712.47 USD | 4,592,053.94 USD | `STANDARD` | `+0.07%` | `0xa382fa9f4b` |
| `SELL` | `8.58` | `83.0600` | 712.42 USD | 4,592,766.36 USD | `STANDARD` | `+0.06%` | `0x53136b4a7c` |
| `SELL` | `8.58` | `83.0600` | 712.38 USD | 4,593,478.74 USD | `STANDARD` | `+0.06%` | `0xf30120f048` |
| `SELL` | `8.58` | `83.0600` | 712.32 USD | 4,594,191.06 USD | `STANDARD` | `+0.05%` | `0xd0956a1eba` |
| `SELL` | `8.58` | `83.0600` | 712.26 USD | 4,594,903.33 USD | `STANDARD` | `+0.04%` | `0xa382fa9f4b` |
| `SELL` | `8.58` | `78.8200` | 676.46 USD | 4,630,350.43 USD | `STANDARD` | `+0.12%` | `0x010461c14e` |
| `SELL` | `8.58` | `78.2600` | 671.28 USD | 4,632,368.95 USD | `STANDARD` | `+0.07%` | `0x2eddf3aa5c` |
| `SELL` | `8.58` | `60.3400` | 517.96 USD | 4,639,961.45 USD | `STANDARD` | `+0.14%` | `0x57d8e75f47` |
| `SELL` | `8.58` | `60.3400` | 517.75 USD | 4,640,479.20 USD | `STANDARD` | `+0.10%` | `0x57d8e75f47` |
| `SELL` | `8.58` | `60.3400` | 517.49 USD | 4,640,996.69 USD | `STANDARD` | `+0.05%` | `0x57d8e75f47` |
| `SELL` | `8.59` | `14936.1900` | 128,346.68 USD | 2,169,289.90 USD | `LARGE (>= USD 100K)` | `+0.25%` | `0x71d0e11ebb` |
| `SELL` | `8.59` | `1756.8400` | 15,096.17 USD | 3,690,522.60 USD | `STANDARD` | `+0.24%` | `0x57d8e75f47` |
| `SELL` | `8.59` | `1756.8400` | 15,091.61 USD | 3,705,614.21 USD | `STANDARD` | `+0.21%` | `0x57d8e75f47` |
| `SELL` | `8.59` | `1756.8400` | 15,086.69 USD | 3,720,700.89 USD | `STANDARD` | `+0.18%` | `0x57d8e75f47` |
| `SELL` | `8.59` | `1264.1900` | 10,862.55 USD | 4,091,715.03 USD | `STANDARD` | `+0.24%` | `0x26934acbd3` |
| `SELL` | `8.59` | `1197.9600` | 10,286.16 USD | 4,144,365.16 USD | `STANDARD` | `+0.17%` | `0xaf9f722a67` |
| `SELL` | `8.59` | `1186.1000` | 10,182.79 USD | 4,185,324.73 USD | `STANDARD` | `+0.16%` | `0x621c555167` |
| `SELL` | `8.59` | `855.3100` | 7,350.11 USD | 4,299,094.61 USD | `STANDARD` | `+0.25%` | `0xecb63caa47` |
| `SELL` | `8.59` | `481.6400` | 4,137.96 USD | 4,392,539.76 USD | `STANDARD` | `+0.23%` | `0x7717a7a245` |
| `SELL` | `8.59` | `455.5400` | 3,914.32 USD | 4,416,284.55 USD | `STANDARD` | `+0.24%` | `0x2a72b57dea` |
| `SELL` | `8.59` | `455.5400` | 3,911.95 USD | 4,420,196.50 USD | `STANDARD` | `+0.18%` | `0x2a72b57dea` |
| `SELL` | `8.59` | `420.0000` | 3,609.65 USD | 4,451,080.03 USD | `STANDARD` | `+0.26%` | `0xb7bd9cef0e` |
| `SELL` | `8.59` | `328.3000` | 2,818.78 USD | 4,481,420.12 USD | `STANDARD` | `+0.17%` | `0xecb63caa47` |
| `SELL` | `8.59` | `305.6100` | 2,623.69 USD | 4,503,050.89 USD | `STANDARD` | `+0.16%` | `0x26934acbd3` |
| `SELL` | `8.59` | `283.9600` | 2,440.13 USD | 4,513,040.58 USD | `STANDARD` | `+0.25%` | `0xecb63caa47` |
| `SELL` | `8.59` | `266.1800` | 2,286.01 USD | 4,517,735.42 USD | `STANDARD` | `+0.19%` | `0xecb63caa47` |
| `SELL` | `8.59` | `116.6000` | 1,001.52 USD | 4,547,664.63 USD | `STANDARD` | `+0.21%` | `0x83bec364a5` |
| `SELL` | `8.59` | `83.0600` | 713.73 USD | 4,574,226.30 USD | `STANDARD` | `+0.25%` | `0xea0e878d5d` |
| `SELL` | `8.59` | `83.0600` | 713.68 USD | 4,574,939.99 USD | `STANDARD` | `+0.24%` | `0xf30120f048` |
| `SELL` | `8.59` | `83.0600` | 713.66 USD | 4,575,653.65 USD | `STANDARD` | `+0.24%` | `0xd0956a1eba` |
| `SELL` | `8.59` | `83.0600` | 713.59 USD | 4,576,367.24 USD | `STANDARD` | `+0.23%` | `0xa382fa9f4b` |
| `SELL` | `8.59` | `83.0600` | 713.56 USD | 4,577,080.80 USD | `STANDARD` | `+0.22%` | `0xea0e878d5d` |
| `SELL` | `8.59` | `83.0600` | 713.49 USD | 4,577,794.30 USD | `STANDARD` | `+0.21%` | `0x9d81a3adf8` |
| `SELL` | `8.59` | `83.0600` | 713.49 USD | 4,578,507.78 USD | `STANDARD` | `+0.21%` | `0x53136b4a7c` |
| `SELL` | `8.59` | `83.0600` | 713.43 USD | 4,579,221.21 USD | `STANDARD` | `+0.20%` | `0xfd66e33095` |
| `SELL` | `8.59` | `83.0600` | 713.37 USD | 4,579,934.58 USD | `STANDARD` | `+0.20%` | `0x63f6411ca6` |
| `SELL` | `8.59` | `83.0600` | 713.33 USD | 4,580,647.90 USD | `STANDARD` | `+0.19%` | `0x53136b4a7c` |
| `SELL` | `8.59` | `83.0600` | 713.26 USD | 4,581,361.17 USD | `STANDARD` | `+0.18%` | `0xea0e878d5d` |
| `SELL` | `8.59` | `83.0600` | 713.25 USD | 4,582,074.42 USD | `STANDARD` | `+0.18%` | `0xf30120f048` |
| `SELL` | `8.59` | `83.0600` | 713.18 USD | 4,582,787.60 USD | `STANDARD` | `+0.17%` | `0xd0956a1eba` |
| `SELL` | `8.59` | `83.0600` | 713.14 USD | 4,583,500.73 USD | `STANDARD` | `+0.16%` | `0xa382fa9f4b` |
| `SELL` | `8.59` | `78.3500` | 673.03 USD | 4,631,697.68 USD | `STANDARD` | `+0.21%` | `0x31ca8395cf` |
| `SELL` | `8.59` | `78.0300` | 670.32 USD | 4,633,039.28 USD | `STANDARD` | `+0.22%` | `0x010461c14e` |
| `SELL` | `8.59` | `60.3400` | 518.18 USD | 4,639,443.49 USD | `STANDARD` | `+0.19%` | `0x57d8e75f47` |
| `SELL` | `8.60` | `3668.9500` | 31,549.30 USD | 3,232,388.80 USD | `MEDIUM (>= USD 25K)` | `+0.32%` | `0x08a49e7f71` |
| `SELL` | `8.60` | `1756.8400` | 15,116.03 USD | 3,630,105.05 USD | `STANDARD` | `+0.38%` | `0x57d8e75f47` |
| `SELL` | `8.60` | `1756.8400` | 15,111.63 USD | 3,645,216.68 USD | `STANDARD` | `+0.35%` | `0x57d8e75f47` |
| `SELL` | `8.60` | `1756.8400` | 15,107.07 USD | 3,660,323.75 USD | `STANDARD` | `+0.32%` | `0x57d8e75f47` |
| `SELL` | `8.60` | `1756.8400` | 15,102.68 USD | 3,675,426.42 USD | `STANDARD` | `+0.29%` | `0x57d8e75f47` |
| `SELL` | `8.60` | `1640.3000` | 14,114.13 USD | 3,975,202.84 USD | `STANDARD` | `+0.38%` | `0xb45f5c538d` |
| `SELL` | `8.60` | `1197.9600` | 10,296.47 USD | 4,134,078.99 USD | `STANDARD` | `+0.27%` | `0xaf9f722a67` |
| `SELL` | `8.60` | `776.3500` | 6,679.09 USD | 4,327,120.09 USD | `STANDARD` | `+0.37%` | `0xecb63caa47` |
| `SELL` | `8.60` | `583.7000` | 5,017.49 USD | 4,360,584.77 USD | `STANDARD` | `+0.28%` | `0x3ca146d269` |
| `SELL` | `8.60` | `581.3700` | 4,999.96 USD | 4,365,584.73 USD | `STANDARD` | `+0.33%` | `0x0efb38a5fa` |
| `SELL` | `8.60` | `455.5400` | 3,919.19 USD | 4,408,453.45 USD | `STANDARD` | `+0.37%` | `0x2a72b57dea` |
| `SELL` | `8.60` | `455.5400` | 3,916.78 USD | 4,412,370.23 USD | `STANDARD` | `+0.31%` | `0x2a72b57dea` |
| `SELL` | `8.60` | `238.9900` | 2,054.81 USD | 4,521,887.76 USD | `STANDARD` | `+0.30%` | `0xecb63caa47` |
| `SELL` | `8.60` | `79.1100` | 680.73 USD | 4,629,673.96 USD | `STANDARD` | `+0.38%` | `0x010461c14e` |
| `SELL` | `8.60` | `73.2900` | 630.48 USD | 4,636,232.71 USD | `STANDARD` | `+0.36%` | `0x31ca8395cf` |
| `SELL` | `8.61` | `2772.6700` | 23,886.27 USD | 3,316,192.82 USD | `STANDARD` | `+0.50%` | `0xb45f5c538d` |
| `SELL` | `8.61` | `2132.5200` | 18,363.77 USD | 3,428,600.97 USD | `STANDARD` | `+0.46%` | `0xb45f5c538d` |
| `SELL` | `8.61` | `1756.8400` | 15,130.08 USD | 3,584,743.09 USD | `STANDARD` | `+0.47%` | `0x57d8e75f47` |
| `SELL` | `8.61` | `1756.8400` | 15,125.34 USD | 3,599,868.42 USD | `STANDARD` | `+0.44%` | `0x57d8e75f47` |
| `SELL` | `8.61` | `1756.8400` | 15,120.59 USD | 3,614,989.02 USD | `STANDARD` | `+0.41%` | `0x57d8e75f47` |
| `SELL` | `8.61` | `928.8000` | 7,999.94 USD | 4,275,836.17 USD | `STANDARD` | `+0.48%` | `0x0efb38a5fa` |
| `SELL` | `8.61` | `918.3700` | 7,908.54 USD | 4,291,744.50 USD | `STANDARD` | `+0.46%` | `0xd3943e4008` |
| `SELL` | `8.61` | `587.6300` | 5,057.56 USD | 4,355,567.29 USD | `STANDARD` | `+0.41%` | `0xecb63caa47` |
| `SELL` | `8.61` | `233.2000` | 2,008.67 USD | 4,523,896.42 USD | `STANDARD` | `+0.49%` | `0x39bac00809` |
| `SELL` | `8.61` | `83.0600` | 715.55 USD | 4,567,075.27 USD | `STANDARD` | `+0.50%` | `0xfd66e33095` |
| `SELL` | `8.61` | `83.0600` | 715.52 USD | 4,567,790.79 USD | `STANDARD` | `+0.50%` | `0xa382fa9f4b` |
| `SELL` | `8.61` | `83.0600` | 715.46 USD | 4,568,506.26 USD | `STANDARD` | `+0.49%` | `0x9d81a3adf8` |
| `SELL` | `8.61` | `83.0600` | 715.40 USD | 4,569,221.66 USD | `STANDARD` | `+0.48%` | `0x53136b4a7c` |
| `SELL` | `8.61` | `83.0600` | 715.25 USD | 4,569,936.91 USD | `STANDARD` | `+0.46%` | `0xf30120f048` |
| `SELL` | `8.61` | `83.0600` | 715.23 USD | 4,570,652.14 USD | `STANDARD` | `+0.46%` | `0xd0956a1eba` |
| `SELL` | `8.61` | `83.0600` | 715.17 USD | 4,571,367.31 USD | `STANDARD` | `+0.45%` | `0xa382fa9f4b` |
| `SELL` | `8.61` | `83.0600` | 715.09 USD | 4,572,797.52 USD | `STANDARD` | `+0.44%` | `0x9d81a3adf8` |
| `SELL` | `8.61` | `83.0600` | 715.06 USD | 4,573,512.58 USD | `STANDARD` | `+0.43%` | `0x53136b4a7c` |
| `SELL` | `8.62` | `14931.3300` | 128,779.73 USD | 2,040,943.22 USD | `LARGE (>= USD 100K)` | `+0.62%` | `0x71d0e11ebb` |
| `SELL` | `8.62` | `1756.8400` | 15,149.76 USD | 3,539,333.87 USD | `STANDARD` | `+0.60%` | `0x57d8e75f47` |
| `SELL` | `8.62` | `1756.8400` | 15,143.26 USD | 3,554,477.13 USD | `STANDARD` | `+0.56%` | `0x57d8e75f47` |
| `SELL` | `8.62` | `1756.8400` | 15,135.88 USD | 3,569,613.00 USD | `STANDARD` | `+0.51%` | `0x57d8e75f47` |
| `SELL` | `8.62` | `1275.8800` | 11,002.04 USD | 4,080,852.47 USD | `STANDARD` | `+0.60%` | `0xd3943e4008` |
| `SELL` | `8.62` | `1124.6600` | 9,694.46 USD | 4,225,178.09 USD | `STANDARD` | `+0.56%` | `0xd3943e4008` |
| `SELL` | `8.62` | `830.0000` | 7,152.94 USD | 4,306,247.55 USD | `STANDARD` | `+0.54%` | `0xb7bd9cef0e` |
| `SELL` | `8.62` | `315.7300` | 2,722.86 USD | 4,492,409.05 USD | `STANDARD` | `+0.61%` | `0x07fd993f0f` |
| `SELL` | `8.62` | `83.0600` | 716.16 USD | 4,560,632.60 USD | `STANDARD` | `+0.59%` | `0xf30120f048` |
| `SELL` | `8.62` | `83.0600` | 716.10 USD | 4,561,348.70 USD | `STANDARD` | `+0.58%` | `0x53136b4a7c` |
| `SELL` | `8.62` | `83.0600` | 716.04 USD | 4,562,064.74 USD | `STANDARD` | `+0.57%` | `0xfd66e33095` |
| `SELL` | `8.62` | `83.0600` | 715.94 USD | 4,562,780.68 USD | `STANDARD` | `+0.56%` | `0xa382fa9f4b` |
| `SELL` | `8.62` | `83.0600` | 715.93 USD | 4,563,496.61 USD | `STANDARD` | `+0.56%` | `0xea0e878d5d` |
| `SELL` | `8.62` | `83.0600` | 715.87 USD | 4,564,212.48 USD | `STANDARD` | `+0.55%` | `0xd0956a1eba` |
| `SELL` | `8.62` | `83.0600` | 715.80 USD | 4,564,928.28 USD | `STANDARD` | `+0.54%` | `0x9d81a3adf8` |
| `SELL` | `8.62` | `83.0600` | 715.75 USD | 4,565,644.03 USD | `STANDARD` | `+0.53%` | `0x63f6411ca6` |
| `SELL` | `8.62` | `83.0600` | 715.69 USD | 4,566,359.73 USD | `STANDARD` | `+0.52%` | `0xf30120f048` |
| `SELL` | `8.62` | `62.2900` | 537.12 USD | 4,637,324.20 USD | `STANDARD` | `+0.60%` | `0x63f6411ca6` |
| `SELL` | `8.62` | `62.2900` | 536.93 USD | 4,637,861.13 USD | `STANDARD` | `+0.56%` | `0xfd66e33095` |
| `SELL` | `8.63` | `15989.7600` | 137,962.85 USD | 1,775,820.79 USD | `LARGE (>= USD 100K)` | `+0.66%` | `0x71cfa5e263` |
| `SELL` | `8.63` | `3675.0300` | 31,705.59 USD | 3,200,839.50 USD | `MEDIUM (>= USD 25K)` | `+0.65%` | `0x26934acbd3` |
| `SELL` | `8.63` | `1756.8400` | 15,166.80 USD | 3,509,025.74 USD | `STANDARD` | `+0.71%` | `0x57d8e75f47` |
| `SELL` | `8.63` | `1756.8400` | 15,158.37 USD | 3,524,184.11 USD | `STANDARD` | `+0.66%` | `0x57d8e75f47` |
| `SELL` | `8.63` | `454.5600` | 3,921.85 USD | 4,404,534.26 USD | `STANDARD` | `+0.65%` | `0xcd7f60e943` |
| `SELL` | `8.63` | `89.0500` | 768.52 USD | 4,553,991.65 USD | `STANDARD` | `+0.68%` | `0x31ca8395cf` |
| `SELL` | `8.63` | `86.6500` | 747.72 USD | 4,556,271.42 USD | `STANDARD` | `+0.67%` | `0x010461c14e` |
| `SELL` | `8.63` | `64.2000` | 554.37 USD | 4,636,787.08 USD | `STANDARD` | `+0.74%` | `0x18c0b7b9fe` |
| `SELL` | `8.64` | `2176.2000` | 18,792.14 USD | 3,391,777.01 USD | `STANDARD` | `+0.74%` | `0xa38f19c4cc` |
| `SELL` | `8.64` | `1756.8400` | 15,175.41 USD | 3,493,858.94 USD | `STANDARD` | `+0.77%` | `0x57d8e75f47` |
| `SELL` | `8.64` | `1389.4600` | 11,999.93 USD | 4,023,324.80 USD | `STANDARD` | `+0.75%` | `0x0efb38a5fa` |
| `SELL` | `8.64` | `1250.0000` | 10,802.62 USD | 4,102,517.65 USD | `STANDARD` | `+0.82%` | `0xb7bd9cef0e` |
| `SELL` | `8.65` | `1395.3500` | 12,063.78 USD | 3,987,266.62 USD | `STANDARD` | `+0.86%` | `0xd3943e4008` |
| `SELL` | `8.65` | `394.0900` | 3,410.26 USD | 4,468,485.65 USD | `STANDARD` | `+0.95%` | `0x14f8e04290` |
| `SELL` | `8.66` | `17161.7600` | 148,624.27 USD | 1,346,883.20 USD | `LARGE (>= USD 100K)` | `+1.03%` | `0x71d0e11ebb` |
| `SELL` | `8.66` | `100.0000` | 866.00 USD | 4,552,390.92 USD | `STANDARD` | `+1.03%` | `0x9ea98d75ae` |
| `SELL` | `8.67` | `11545.7100` | 100,139.41 USD | 2,746,667.00 USD | `LARGE (>= USD 100K)` | `+1.18%` | `0x881cd92459` |
| `SELL` | `8.67` | `1844.4000` | 15,999.99 USD | 3,462,683.56 USD | `STANDARD` | `+1.20%` | `0x0efb38a5fa` |
| `SELL` | `8.68` | `31331.6800` | 271,808.59 USD | 782,862.94 USD | `LARGE (>= USD 100K)` | `+1.21%` | `0x71cfa5e263` |
| `SELL` | `8.68` | `7459.9900` | 64,765.40 USD | 3,068,967.29 USD | `MEDIUM (>= USD 25K)` | `+1.28%` | `0x71d0e11ebb` |
| `SELL` | `8.68` | `315.7300` | 2,740.85 USD | 4,489,686.19 USD | `STANDARD` | `+1.27%` | `0x07fd993f0f` |
| `SELL` | `8.68` | `77.7000` | 674.23 USD | 4,631,024.65 USD | `STANDARD` | `+1.23%` | `0x010461c14e` |
| `SELL` | `8.68` | `72.8500` | 632.14 USD | 4,634,970.19 USD | `STANDARD` | `+1.23%` | `0x31ca8395cf` |
| `SELL` | `8.69` | `4247.2800` | 36,924.58 USD | 3,169,133.92 USD | `MEDIUM (>= USD 25K)` | `+1.42%` | `0xa24c5ca26c` |
| `SELL` | `8.69` | `398.6500` | 3,465.74 USD | 4,465,075.39 USD | `STANDARD` | `+1.42%` | `0x14f8e04290` |
| `SELL` | `8.69` | `191.2300` | 1,662.34 USD | 4,533,274.47 USD | `STANDARD` | `+1.41%` | `0xdadbb4b2a0` |
| `SELL` | `8.70` | `17166.7500` | 149,328.41 USD | 1,198,258.92 USD | `LARGE (>= USD 100K)` | `+1.48%` | `0x71d0e11ebb` |
| `SELL` | `8.70` | `2183.7500` | 18,999.94 USD | 3,354,192.70 USD | `STANDARD` | `+1.50%` | `0x0efb38a5fa` |
| `SELL` | `8.70` | `1711.2200` | 14,890.35 USD | 3,961,088.72 USD | `STANDARD` | `+1.51%` | `0xd3943e4008` |
| `SELL` | `8.70` | `398.6500` | 3,469.97 USD | 4,458,141.12 USD | `STANDARD` | `+1.55%` | `0x14f8e04290` |
| `SELL` | `8.71` | `2120.5700` | 18,460.20 USD | 3,410,237.20 USD | `STANDARD` | `+1.56%` | `0xd3943e4008` |
| `SELL` | `8.71` | `187.4400` | 1,633.30 USD | 4,534,907.76 USD | `STANDARD` | `+1.66%` | `0x010461c14e` |
| `SELL` | `8.71` | `173.9200` | 1,514.96 USD | 4,537,985.25 USD | `STANDARD` | `+1.62%` | `0x31ca8395cf` |
| `SELL` | `8.73` | `397.2700` | 3,468.52 USD | 4,461,609.65 USD | `STANDARD` | `+1.86%` | `0x14f8e04290` |
| `SELL` | `8.74` | `315.7300` | 2,758.85 USD | 4,486,945.34 USD | `STANDARD` | `+1.94%` | `0x07fd993f0f` |
| `SELL` | `8.74` | `87.8600` | 767.81 USD | 4,554,759.46 USD | `STANDARD` | `+1.95%` | `0xdadbb4b2a0` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:42:20 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1463` | `0x7737...bf66` | `SHORT` | 1,471,865.23 USD | `171,568.06` | `7.43` | `8.57` | `111.49` | -196,320.21 USD | `-13.34%` | `10X Cross` |
| `1569` | `0xeadc...9d55` | `LONG` | 1,373,229.33 USD | `160,070.56` | `8.11` | `8.57` | `0.000000` | 75,591.75 USD | `+5.50%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+2.58%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--5.69%`)
  * 48H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+2.52%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--5.72%`)
  * 3D Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+2.52%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--5.72%`)
  * 7D Horizon: Short MP=`9.28` (Vol: 426,900.00 USD, Dist: `+8.70%`) | Long MP=`8.31` (Vol: 495,000.00 USD, Dist: `--2.68%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.98` | 1,510.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 160.40 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 223.28 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 565.80 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 252.43 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 257.03 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 267.38 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 942.44 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 10,990.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 332.93 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 1,150.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 21,430.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 23,480.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 905.85 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 392.22 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 8,600.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 590.29 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.16` | 159.68 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.18` | 390.54 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 196.42 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 110.77 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.58` | 107.56 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 3,420.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,380.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,040.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 474.50 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.78` | 525.25 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 3,320.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.87` | 310.14 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.88` | 505.68 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 16,080.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 4,110.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 352.68 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 4,090.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 269.53 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 216.43 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 482.71 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 710.03 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 954.05 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 105.46 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 915.43 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.14` | 3,070.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 421.89 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 159,630.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.26` | 2,230.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 640.70 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 20,560.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 299.48 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 2,880.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.61` | 34,490.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 468.55 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.72` | 2,390.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 661.65 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 4,530.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 635.31 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 688.15 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.84` | 146.13 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.86` | 2,110.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 984.70 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 147.55 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 6,320.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 437.84 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,530.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 1,140.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.13` | 2,030.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 7,810.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.22` | 795.06 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 972.65 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 354,280.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.29` | 1,420.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 277.48 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 287,230.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 1,310.00 USD | 829,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 5,120.00 USD | 827,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 822,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 484.64 USD | 822,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 822,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 815,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.49` | 1,480.00 USD | 814,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.50` | 6,030.00 USD | 812,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 852.03 USD | 806,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 805,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 1,510.00 USD | 796,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.59` | 2,870.00 USD | 795,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 792,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 364.90 USD | 790,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.63` | 245.89 USD | 790,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.66` | 1,740.00 USD | 789,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.67` | 1,320.00 USD | 788,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.68` | 3,160.00 USD | 786,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.70` | 15,800.00 USD | 783,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 11,000.00 USD | 767,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 6,180.00 USD | 756,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.72` | 2,200.00 USD | 750,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 748,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 7,990.00 USD | 747,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 22,020.00 USD | 739,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 5,170.00 USD | 717,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 219.12 USD | 711,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 8,520.00 USD | 711,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 158.14 USD | 703,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 702,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 263.66 USD | 699,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 3,990.00 USD | 699,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 579.62 USD | 695,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.93` | 3,500.00 USD | 694,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 215.30 USD | 691,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 7,240.00 USD | 691,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 683,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.97` | 128,810.00 USD | 683,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 1,040.00 USD | 554,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.01` | 20,890.00 USD | 553,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.03` | 1,370.00 USD | 532,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.07` | 23,960.00 USD | 531,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 507,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,050.00 USD | 500,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.09` | 2,130.00 USD | 499,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,530.00 USD | 497,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 468,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 13,410.00 USD | 468,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,270.00 USD | 454,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.17` | 4,470.00 USD | 434,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 430,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 322.94 USD | 428,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.24` | 2,500.00 USD | 428,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 425,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 21,280.00 USD | 425,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.27` | 7,140,000.00 USD | 7,140,000.00 USD | 360.23 USD | 1,810.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,420.00 USD | 404,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 1,680.00 USD | 368,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.30` | 29,220.00 USD | 366,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.31` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 0.00 USD | 104.04 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.33` | 13,110.00 USD | 337,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 1,400.00 USD | 324,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.36` | 5,290.00 USD | 322,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.37` | 2,940.00 USD | 317,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.37` | 7,130,000.00 USD | 7,130,000.00 USD | 45,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.38` | 1,100.00 USD | 314,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 227.97 USD | 313,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.39` | 7,090,000.00 USD | 7,090,000.00 USD | 46,200.00 USD | 0.00 USD | 457.98 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 147.61 USD | 313,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.43` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 0.00 USD | 503.12 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.43` | 2,430.00 USD | 312,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 2,410.00 USD | 310,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.45` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 10,390.00 USD | 308,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 297,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 1,120.00 USD | 293,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.49` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 962.81 USD | 291,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 421.78 USD | 290,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.51` | 6,990,000.00 USD | 6,990,000.00 USD | 2,070.00 USD | 0.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.51` | 1,710.00 USD | 290,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.53` | 1,570.00 USD | 288,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.53` | 6,970,000.00 USD | 6,970,000.00 USD | 35,990.00 USD | 18,910.00 USD | 570.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 287,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 1,510.00 USD | 283,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.55` | 6,920,000.00 USD | 6,920,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.55` | 1,070.00 USD | 281,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.57` | 25,060.00 USD | 280,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 118.25 USD | 255,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.59` | 5,830,000.00 USD | 5,830,000.00 USD | 1,740.00 USD | 0.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.59` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 301.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.60` | 5,820,000.00 USD | 5,820,000.00 USD | 706.40 USD | 4,900.00 USD | 351.13 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.61` | 5,820,000.00 USD | 5,820,000.00 USD | 2,750.00 USD | 1,250.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.61` | 6,890,000.00 USD | 6,890,000.00 USD | 626.55 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 754.04 USD | 255,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 5,800,000.00 USD | 5,800,000.00 USD | 8,960.00 USD | 1,330.00 USD | 133.28 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 254,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.63` | 5,790,000.00 USD | 5,790,000.00 USD | 5,940.00 USD | 0.00 USD | 9,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.63` | 6,890,000.00 USD | 6,890,000.00 USD | 41,300.00 USD | 2,130.00 USD | 386.35 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 253,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 5,780,000.00 USD | 5,780,000.00 USD | 33,010.00 USD | 812.96 USD | 2,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.65` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 1,320.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.65` | 6,850,000.00 USD | 6,850,000.00 USD | 4,870.00 USD | 2,350.00 USD | 813.38 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 253,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.66` | 5,730,000.00 USD | 5,730,000.00 USD | 3,030.00 USD | 0.00 USD | 531.95 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 256.09 USD | 253,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.67` | 5,730,000.00 USD | 5,730,000.00 USD | 1,410.00 USD | 1,110.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.67` | 6,840,000.00 USD | 6,840,000.00 USD | 1,110.00 USD | 0.00 USD | 34,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 140.45 USD | 253,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.68` | 5,720,000.00 USD | 5,720,000.00 USD | 892.30 USD | 0.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.68` | 739.30 USD | 252,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.69` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 1,600.00 USD | 0.13 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.69` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 0.00 USD | 1,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.70` | 6,690.00 USD | 252,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 5,710,000.00 USD | 5,710,000.00 USD | 4,140.00 USD | 3,380.00 USD | 16,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.71` | 5,690,000.00 USD | 5,690,000.00 USD | 660.12 USD | 5,720.00 USD | 7,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.71` | 6,800,000.00 USD | 6,800,000.00 USD | 393.33 USD | 1,650.00 USD | 33,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.72` | 5,680,000.00 USD | 5,680,000.00 USD | 701.68 USD | 1,840.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.73` | 5,670,000.00 USD | 5,670,000.00 USD | 4,120.00 USD | 1,240.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.73` | 6,770,000.00 USD | 6,770,000.00 USD | 39,770.00 USD | 2,520.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.74` | 5,660,000.00 USD | 5,660,000.00 USD | 16,520.00 USD | 0.00 USD | 184.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.75` | 5,640,000.00 USD | 5,640,000.00 USD | 900.06 USD | 6,210.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.75` | 6,720,000.00 USD | 6,720,000.00 USD | 29,320.00 USD | 13,360.00 USD | 10,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 500.12 USD | 245,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.76` | 5,630,000.00 USD | 5,630,000.00 USD | 458.75 USD | 494.12 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 244,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.77` | 5,630,000.00 USD | 5,630,000.00 USD | 13,020.00 USD | 689.91 USD | 3,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.77` | 6,670,000.00 USD | 6,670,000.00 USD | 20,120.00 USD | 4,900.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.78` | 12,100.00 USD | 244,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 5,610,000.00 USD | 5,610,000.00 USD | 2,730.00 USD | 6,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,750.00 USD | 232,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.79` | 5,600,000.00 USD | 5,600,000.00 USD | 18,960.00 USD | 2,920.00 USD | 7,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.79` | 6,640,000.00 USD | 6,640,000.00 USD | 70,950.00 USD | 7,170.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 4,480.00 USD | 228,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 5,570,000.00 USD | 5,570,000.00 USD | 4,920.00 USD | 7,910.00 USD | 709.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 6,380.00 USD | 224,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.81` | 5,560,000.00 USD | 5,560,000.00 USD | 349.70 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.81` | 6,540,000.00 USD | 6,540,000.00 USD | 3,970.00 USD | 11,570.00 USD | 970.74 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.82` | 5,560,000.00 USD | 5,560,000.00 USD | 248.67 USD | 1,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.83` | 1,940.00 USD | 217,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.83` | 5,550,000.00 USD | 5,550,000.00 USD | 27,230.00 USD | 5,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.83` | 6,520,000.00 USD | 6,520,000.00 USD | 29,530.00 USD | 2,130.00 USD | 25,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.84` | 5,520,000.00 USD | 5,520,000.00 USD | 978.04 USD | 1,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 22,560.00 USD | 215,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.85` | 5,520,000.00 USD | 5,520,000.00 USD | 3,320.00 USD | 639.88 USD | 2,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.85` | 6,460,000.00 USD | 6,460,000.00 USD | 17,330.00 USD | 7,840.00 USD | 12,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.86` | 5,510,000.00 USD | 5,510,000.00 USD | 1,290.00 USD | 6,270.00 USD | 13,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 233.83 USD | 193,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.87` | 5,490,000.00 USD | 5,490,000.00 USD | 10,980.00 USD | 10,860.00 USD | 22,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.87` | 6,420,000.00 USD | 6,420,000.00 USD | 150,960.00 USD | 1,540.00 USD | 21,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 193,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 5,450,000.00 USD | 5,450,000.00 USD | 158,960.00 USD | 4,280.00 USD | 33,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.89` | 5,250,000.00 USD | 5,250,000.00 USD | 57,720.00 USD | 3,720.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.89` | 6,250,000.00 USD | 6,250,000.00 USD | 150,040.00 USD | 18,320.00 USD | 24,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.89` | 13,270.00 USD | 192,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.90` | 5,160,000.00 USD | 5,160,000.00 USD | 56,620.00 USD | 6,970.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 2,930.00 USD | 179,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 5,090,000.00 USD | 5,090,000.00 USD | 14,180.00 USD | 10,370.00 USD | 26,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.91` | 6,060,000.00 USD | 6,060,000.00 USD | 31,740.00 USD | 26,330.00 USD | 44,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.92` | 5,040,000.00 USD | 5,040,000.00 USD | 15,830.00 USD | 2,040.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 4,600.00 USD | 176,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 5,020,000.00 USD | 5,020,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.93` | 5,950,000.00 USD | 5,950,000.00 USD | 78,470.00 USD | 7,330.00 USD | 15,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 16,340.00 USD | 171,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 5,000,000.00 USD | 5,000,000.00 USD | 15,580.00 USD | 20,510.00 USD | 61,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 141.74 USD | 155,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 4,900,000.00 USD | 4,900,000.00 USD | 28,200.00 USD | 9,190.00 USD | 86,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.95` | 5,850,000.00 USD | 5,850,000.00 USD | 45,890.00 USD | 9,500.00 USD | 102,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 127,900.00 USD | 155,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 4,780,000.00 USD | 4,780,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.97` | 4,700,000.00 USD | 4,700,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.97` | 5,690,000.00 USD | 5,690,000.00 USD | 37,150.00 USD | 18,700.00 USD | 41,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.97` | 1,580.00 USD | 27,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.98` | 4,670,000.00 USD | 4,670,000.00 USD | 5,050.00 USD | 2,060.00 USD | 42,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,280.00 USD | 25,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 4,620,000.00 USD | 4,620,000.00 USD | 3,450.00 USD | 10,180.00 USD | 4,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.99` | 5,600,000.00 USD | 5,600,000.00 USD | 52,570.00 USD | 20,640.00 USD | 122,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 889.52 USD | 24,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 4,600,000.00 USD | 4,600,000.00 USD | 50,430.00 USD | 8,950.00 USD | 21,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 4,520,000.00 USD | 4,520,000.00 USD | 6,540.00 USD | 3,750.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.01` | 5,400,000.00 USD | 5,400,000.00 USD | 47,380.00 USD | 17,990.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 4,510,000.00 USD | 4,510,000.00 USD | 75,150.00 USD | 0.00 USD | 274.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.03` | 4,430,000.00 USD | 4,430,000.00 USD | 9,070.00 USD | 12,540.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.03` | 5,290,000.00 USD | 5,290,000.00 USD | 353,080.00 USD | 35,720.00 USD | 47,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.04` | 4,400,000.00 USD | 4,400,000.00 USD | 49,540.00 USD | 0.00 USD | 10,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.05` | 4,340,000.00 USD | 4,340,000.00 USD | 318,600.00 USD | 6,430.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.05` | 4,850,000.00 USD | 4,850,000.00 USD | 390,130.00 USD | 0.00 USD | 62,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.06` | 3,960,000.00 USD | 3,960,000.00 USD | 155,360.00 USD | 0.00 USD | 66,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 439.54 USD | 23,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 3,740,000.00 USD | 3,740,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.07` | 4,400,000.00 USD | 4,400,000.00 USD | 60,670.00 USD | 0.00 USD | 75,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.07` | 21,710.00 USD | 23,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.08` | 3,590,000.00 USD | 3,590,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 887.25 USD | 1,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.09` | 3,510,000.00 USD | 3,510,000.00 USD | 3,650.00 USD | 0.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.09` | 4,260,000.00 USD | 4,260,000.00 USD | 32,760.00 USD | 0.00 USD | 80,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.10` | 3,480,000.00 USD | 3,480,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.11` | 3,320,000.00 USD | 3,320,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.11` | 4,150,000.00 USD | 4,150,000.00 USD | 33,000.00 USD | 0.00 USD | 141,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.12` | 3,050,000.00 USD | 3,050,000.00 USD | 19,930.00 USD | 11,230.00 USD | 126,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 521.62 USD | 521.62 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.13` | 2,890,000.00 USD | 2,890,000.00 USD | 34,890.00 USD | 9,180.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.13` | 3,980,000.00 USD | 3,980,000.00 USD | 47,290.00 USD | 12,740.00 USD | 21,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 2,840,000.00 USD | 2,840,000.00 USD | 17,740.00 USD | 8,630.00 USD | 105,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 2,710,000.00 USD | 2,710,000.00 USD | 47,020.00 USD | 12,240.00 USD | 53,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.15` | 3,900,000.00 USD | 3,900,000.00 USD | 179,060.00 USD | 31,560.00 USD | 182,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 2,600,000.00 USD | 2,600,000.00 USD | 192.50 USD | 22,250.00 USD | 165,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.17` | 2,410,000.00 USD | 2,410,000.00 USD | 11,100.00 USD | 9,120.00 USD | 183,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.17` | 3,500,000.00 USD | 3,500,000.00 USD | 1,590.00 USD | 13,650.00 USD | 151,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 2,210,000.00 USD | 2,210,000.00 USD | 7,140.00 USD | 3,280.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.19` | 2,190,000.00 USD | 2,190,000.00 USD | 18,260.00 USD | 545.08 USD | 19,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.19` | 3,340,000.00 USD | 3,340,000.00 USD | 1,200.00 USD | 72,340.00 USD | 26,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.20` | 2,160,000.00 USD | 2,160,000.00 USD | 25,900.00 USD | 4,000.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.21` | 2,110,000.00 USD | 2,110,000.00 USD | 41,620.00 USD | 2,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.21` | 3,240,000.00 USD | 3,240,000.00 USD | 174,220.00 USD | 22,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.22` | 2,070,000.00 USD | 2,070,000.00 USD | 3,620.00 USD | 1,530.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.23` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 3,450.00 USD | 2,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.23` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 40,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.24` | 2,040,000.00 USD | 2,040,000.00 USD | 168.44 USD | 6,390.00 USD | 9,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.25` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 5,000.00 USD | 38,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.25` | 3,000,000.00 USD | 3,000,000.00 USD | 129,050.00 USD | 12,050.00 USD | 17,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.26` | 1,980,000.00 USD | 1,980,000.00 USD | 50,590.00 USD | 12,510.00 USD | 25,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.27` | 1,900,000.00 USD | 1,900,000.00 USD | 13,860.00 USD | 12,270.00 USD | 20,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.27` | 2,840,000.00 USD | 2,840,000.00 USD | 103,730.00 USD | 4,000.00 USD | 38,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.28` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 13,760.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.29` | 1,830,000.00 USD | 1,830,000.00 USD | 39,480.00 USD | 11,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.29` | 2,690,000.00 USD | 2,690,000.00 USD | 166,800.00 USD | 6,550.00 USD | 21,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.30` | 1,780,000.00 USD | 1,780,000.00 USD | 69,220.00 USD | 13,810.00 USD | 20,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.31` | 1,680,000.00 USD | 1,680,000.00 USD | 82,900.00 USD | 11,920.00 USD | 56,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.31` | 2,500,000.00 USD | 2,500,000.00 USD | 370,260.00 USD | 10,660.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.32` | 1,530,000.00 USD | 1,530,000.00 USD | 80,060.00 USD | 6,080.00 USD | 14,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 8,710.00 USD | 109.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.33` | 2,120,000.00 USD | 2,120,000.00 USD | 14,600.00 USD | 11,770.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.34` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 3,230.00 USD | 13.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 23,440.00 USD | 25,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.35` | 2,080,000.00 USD | 2,080,000.00 USD | 223,170.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.36` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 1,090.00 USD | 25,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.37` | 1,340,000.00 USD | 1,340,000.00 USD | 691.75 USD | 14,420.00 USD | 16.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.37` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 38,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.38` | 1,320,000.00 USD | 1,320,000.00 USD | 17,220.00 USD | 7,830.00 USD | 50,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.39` | 1,250,000.00 USD | 1,250,000.00 USD | 107,990.00 USD | 16,670.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.39` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 15,860.00 USD | 68,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.40` | 1,090,000.00 USD | 1,090,000.00 USD | 10,500.00 USD | 10,400.00 USD | 56,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.41` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 12,780.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.41` | 1,730,000.00 USD | 1,730,000.00 USD | 194,850.00 USD | 0.00 USD | 90,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.42` | 981,740.00 USD | 981,740.00 USD | 0.00 USD | 16,260.00 USD | 42,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.43` | 922,590.00 USD | 922,590.00 USD | 81,350.00 USD | 7,730.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.43` | 1,450,000.00 USD | 1,450,000.00 USD | 163,340.00 USD | 12,610.00 USD | 25,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.44` | 821,850.00 USD | 821,850.00 USD | 11,130.00 USD | 32,380.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.45` | 617,870.00 USD | 617,870.00 USD | 54,790.00 USD | 5,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.45` | 1,250,000.00 USD | 1,250,000.00 USD | 156,410.00 USD | 8,000.00 USD | 173,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.47` | 557,120.00 USD | 557,120.00 USD | 663.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.47` | 907,710.00 USD | 907,710.00 USD | 0.00 USD | 0.00 USD | 44,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.48` | 556,450.00 USD | 556,450.00 USD | 749.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.49` | 555,700.00 USD | 555,700.00 USD | 0.00 USD | 0.00 USD | 12.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.49` | 863,450.00 USD | 863,450.00 USD | 0.00 USD | 0.00 USD | 152,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.51` | 710,480.00 USD | 710,480.00 USD | 0.00 USD | 0.00 USD | 91,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.52` | 555,690.00 USD | 555,690.00 USD | 158,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.53` | 397,060.00 USD | 397,060.00 USD | 24,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.53` | 619,100.00 USD | 619,100.00 USD | 173,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.54` | 372,880.00 USD | 372,880.00 USD | 198,250.00 USD | 0.00 USD | 156.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.55` | 174,470.00 USD | 174,470.00 USD | 1,650.00 USD | 0.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.55` | 445,730.00 USD | 445,730.00 USD | 434,770.00 USD | 0.00 USD | 839.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.56` | 147,690.00 USD | 147,690.00 USD | 686.73 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.57` | 147,010.00 USD | 147,010.00 USD | 147,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.57` | 10,120.00 USD | 10,120.00 USD | 9,740.00 USD | 0.00 USD | 377.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.58` | 59,120.00 USD | 59,120.00 USD | 59,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.58` | 118,240.00 USD | 118,240.00 USD | 59,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.59` | 1,430.00 USD | 1,430.00 USD | 0.00 USD | 0.00 USD | 1,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.60` | 120,280.00 USD | 120,280.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.61` | 121,470.00 USD | 121,470.00 USD | 497.00 USD | 0.00 USD | 699.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.61` | 4,850.00 USD | 4,850.00 USD | 2,810.00 USD | 0.00 USD | 610.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.62` | 288,740.00 USD | 288,740.00 USD | 41,980.00 USD | 0.00 USD | 125,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.63` | 420,450.00 USD | 420,450.00 USD | 129,280.00 USD | 2,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.63` | 32,680.00 USD | 32,680.00 USD | 0.00 USD | 0.00 USD | 27,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 502,420.00 USD | 502,420.00 USD | 69,220.00 USD | 9,340.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.65` | 564,530.00 USD | 564,530.00 USD | 35,830.00 USD | 9,010.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.65` | 84,600.00 USD | 84,600.00 USD | 40,260.00 USD | 10,660.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.66` | 593,830.00 USD | 593,830.00 USD | 13,240.00 USD | 2,020.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.67` | 607,230.00 USD | 607,230.00 USD | 880.60 USD | 12,460.00 USD | 56.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.67` | 97,100.00 USD | 97,100.00 USD | 0.00 USD | 11,770.00 USD | 730.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 646,750.00 USD | 646,750.00 USD | 588.00 USD | 13,040.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.69` | 209.31 USD | 209.31 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.69` | 722,610.00 USD | 722,610.00 USD | 10,820.00 USD | 22,830.00 USD | 42,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.69` | 338,110.00 USD | 338,110.00 USD | 29,260.00 USD | 48,960.00 USD | 162,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.70` | 817,130.00 USD | 817,130.00 USD | 62,600.00 USD | 1,090.00 USD | 30,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.71` | 843,820.00 USD | 843,820.00 USD | 18,700.00 USD | 7,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.71` | 436,340.00 USD | 436,340.00 USD | 87,110.00 USD | 11,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 933,070.00 USD | 933,070.00 USD | 34,050.00 USD | 4,410.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.73` | 1,020,000.00 USD | 1,020,000.00 USD | 19,820.00 USD | 31,860.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.73` | 506,410.00 USD | 506,410.00 USD | 51,030.00 USD | 19,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 1,080,000.00 USD | 1,080,000.00 USD | 38,500.00 USD | 6,910.00 USD | 17,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.75` | 1,150,000.00 USD | 1,150,000.00 USD | 33,520.00 USD | 15,310.00 USD | 23,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.75` | 758,280.00 USD | 758,280.00 USD | 196,960.00 USD | 19,690.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.76` | 1,300,000.00 USD | 1,300,000.00 USD | 82,470.00 USD | 10,010.00 USD | 57,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.77` | 1,510,000.00 USD | 1,510,000.00 USD | 155,740.00 USD | 2,060.00 USD | 47,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.77` | 1,020,000.00 USD | 1,020,000.00 USD | 141,710.00 USD | 12,610.00 USD | 104,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.78` | 1,620,000.00 USD | 1,620,000.00 USD | 41,500.00 USD | 25,510.00 USD | 50,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.79` | 1,710,000.00 USD | 1,710,000.00 USD | 31,710.00 USD | 17,970.00 USD | 31,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.79` | 1,150,000.00 USD | 1,150,000.00 USD | 29,660.00 USD | 33,300.00 USD | 65,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.80` | 1,860,000.00 USD | 1,860,000.00 USD | 113,160.00 USD | 19,150.00 USD | 23,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.81` | 1,930,000.00 USD | 1,930,000.00 USD | 53,290.00 USD | 9,030.00 USD | 1,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.81` | 1,350,000.00 USD | 1,350,000.00 USD | 122,920.00 USD | 26,890.00 USD | 58,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.82` | 2,010,000.00 USD | 2,010,000.00 USD | 19,950.00 USD | 4,510.00 USD | 61,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.82` | 6,000.00 USD | 6,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.83` | 2,210,000.00 USD | 2,210,000.00 USD | 174,730.00 USD | 19,400.00 USD | 7,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.83` | 1,600,000.00 USD | 1,600,000.00 USD | 242,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 2,280,000.00 USD | 2,280,000.00 USD | 1,500.00 USD | 4,360.00 USD | 59,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 2,310,000.00 USD | 2,310,000.00 USD | 13,040.00 USD | 3,870.00 USD | 11,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.85` | 1,690,000.00 USD | 1,690,000.00 USD | 29,310.00 USD | 5,880.00 USD | 58,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 2,320,000.00 USD | 2,320,000.00 USD | 2,060.00 USD | 3,280.00 USD | 4,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.87` | 1,160.00 USD | 7,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.87` | 2,330,000.00 USD | 2,330,000.00 USD | 1,410.00 USD | 545.08 USD | 12,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.87` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 23,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 2,350,000.00 USD | 2,350,000.00 USD | 803.70 USD | 14,670.00 USD | 186.36 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.88` | 691.70 USD | 8,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.89` | 2,400,000.00 USD | 2,400,000.00 USD | 13,040.00 USD | 4,360.00 USD | 32,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.89` | 1,790,000.00 USD | 1,790,000.00 USD | 1,250.00 USD | 0.00 USD | 73,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 2,500,000.00 USD | 2,500,000.00 USD | 32,320.00 USD | 7,510.00 USD | 65,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.91` | 2,560,000.00 USD | 2,560,000.00 USD | 32,240.00 USD | 13,320.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.91` | 1,890,000.00 USD | 1,890,000.00 USD | 2,440.00 USD | 4,130.00 USD | 88,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 2,580,000.00 USD | 2,580,000.00 USD | 1,110.00 USD | 6,390.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 2,660,000.00 USD | 2,660,000.00 USD | 31,830.00 USD | 6,810.00 USD | 38,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.93` | 2,070,000.00 USD | 2,070,000.00 USD | 157,480.00 USD | 6,300.00 USD | 17,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 2,730,000.00 USD | 2,730,000.00 USD | 50,590.00 USD | 12,260.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.95` | 3,140.00 USD | 11,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.95` | 2,760,000.00 USD | 2,760,000.00 USD | 3,080.00 USD | 6,630.00 USD | 20,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.95` | 2,180,000.00 USD | 2,180,000.00 USD | 74,920.00 USD | 4,000.00 USD | 38,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.96` | 227.82 USD | 11,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.96` | 2,760,000.00 USD | 2,760,000.00 USD | 1,260.00 USD | 2,980.00 USD | 175.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.97` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.26 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.97` | 2,190,000.00 USD | 2,190,000.00 USD | 1,930.00 USD | 0.00 USD | 791.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.98` | 2,820,000.00 USD | 2,820,000.00 USD | 35,320.00 USD | 9,420.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 2,900,000.00 USD | 2,900,000.00 USD | 48,380.00 USD | 22,110.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.99` | 2,370,000.00 USD | 2,370,000.00 USD | 145,880.00 USD | 6,550.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.99` | 539,710.00 USD | 551,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.00` | 2,960,000.00 USD | 2,960,000.00 USD | 36,960.00 USD | 0.00 USD | 24,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 3,040,000.00 USD | 3,040,000.00 USD | 49,510.00 USD | 14,940.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.01` | 2,730,000.00 USD | 2,730,000.00 USD | 303,030.00 USD | 36,180.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 3,110,000.00 USD | 3,110,000.00 USD | 39,170.00 USD | 29,440.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 3,280,000.00 USD | 3,280,000.00 USD | 125,760.00 USD | 10,300.00 USD | 34,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.03` | 2,950,000.00 USD | 2,950,000.00 USD | 107,490.00 USD | 101,140.00 USD | 15,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 3,350,000.00 USD | 3,350,000.00 USD | 41,710.00 USD | 5,900.00 USD | 14,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 3,400,000.00 USD | 3,400,000.00 USD | 21,980.00 USD | 7,560.00 USD | 22,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.05` | 3,050,000.00 USD | 3,050,000.00 USD | 38,740.00 USD | 17,700.00 USD | 39,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.05` | 213.70 USD | 551,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.06` | 3,440,000.00 USD | 3,440,000.00 USD | 28,180.00 USD | 5,480.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 3,500,000.00 USD | 3,500,000.00 USD | 13,070.00 USD | 15,350.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.07` | 3,100,000.00 USD | 3,100,000.00 USD | 3,990.00 USD | 14,140.00 USD | 37,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 3,540,000.00 USD | 3,540,000.00 USD | 12,960.00 USD | 1,040.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 3,640,000.00 USD | 3,640,000.00 USD | 71,230.00 USD | 9,730.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.09` | 3,410,000.00 USD | 3,410,000.00 USD | 152,640.00 USD | 8,680.00 USD | 144,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.10` | 3,890.00 USD | 555,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.10` | 3,700,000.00 USD | 3,700,000.00 USD | 16,320.00 USD | 10,640.00 USD | 30,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 3,850,000.00 USD | 3,850,000.00 USD | 51,080.00 USD | 14,420.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.11` | 4,900,000.00 USD | 4,900,000.00 USD | 877,120.00 USD | 37,620.00 USD | 570,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 3,990,000.00 USD | 3,990,000.00 USD | 94,400.00 USD | 21,650.00 USD | 26,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 4,120,000.00 USD | 4,120,000.00 USD | 75,260.00 USD | 15,960.00 USD | 35,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.13` | 6,070,000.00 USD | 6,070,000.00 USD | 666,880.00 USD | 26,540.00 USD | 485,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.14` | 4,170,000.00 USD | 4,170,000.00 USD | 30,520.00 USD | 0.00 USD | 24,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.14` | 180.80 USD | 555,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.15` | 4,260,000.00 USD | 4,260,000.00 USD | 56,980.00 USD | 20,890.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.15` | 6,740,000.00 USD | 6,740,000.00 USD | 357,020.00 USD | 38,700.00 USD | 269,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 4,380,000.00 USD | 4,380,000.00 USD | 63,930.00 USD | 23,900.00 USD | 32,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 4,510,000.00 USD | 4,510,000.00 USD | 74,820.00 USD | 3,200.00 USD | 49,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.17` | 7,590,000.00 USD | 7,590,000.00 USD | 409,650.00 USD | 133,490.00 USD | 302,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 4,600,000.00 USD | 4,600,000.00 USD | 28,310.00 USD | 26,430.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 4,710,000.00 USD | 4,710,000.00 USD | 77,890.00 USD | 29,140.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.19` | 8,390,000.00 USD | 8,390,000.00 USD | 504,150.00 USD | 108,440.00 USD | 193,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.20` | 4,820,000.00 USD | 4,820,000.00 USD | 64,910.00 USD | 11,090.00 USD | 37,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 4,860,000.00 USD | 4,860,000.00 USD | 30,000.00 USD | 2,950.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.21` | 9,400,000.00 USD | 9,400,000.00 USD | 590,780.00 USD | 144,470.00 USD | 277,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.22` | 4,930,000.00 USD | 4,930,000.00 USD | 58,470.00 USD | 2,850.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.22` | 416.69 USD | 555,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.23` | 4,940,000.00 USD | 4,940,000.00 USD | 471.32 USD | 4,270.00 USD | 17.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.23` | 10,410,000.00 USD | 10,410,000.00 USD | 582,450.00 USD | 92,780.00 USD | 331,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 4,990,000.00 USD | 4,990,000.00 USD | 45,580.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 5,020,000.00 USD | 5,020,000.00 USD | 17,240.00 USD | 5,840.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.25` | 10,810,000.00 USD | 10,810,000.00 USD | 277,290.00 USD | 61,940.00 USD | 61,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 5,030,000.00 USD | 5,030,000.00 USD | 574.60 USD | 0.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 5,060,000.00 USD | 5,060,000.00 USD | 23,430.00 USD | 1,360.00 USD | 6,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.27` | 11,110,000.00 USD | 11,110,000.00 USD | 156,190.00 USD | 102,670.00 USD | 38,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 5,070,000.00 USD | 5,070,000.00 USD | 1,610.00 USD | 8,760.00 USD | 169.17 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 326.09 USD | 556,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.29` | 5,110,000.00 USD | 5,110,000.00 USD | 16,070.00 USD | 4,140.00 USD | 17,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.29` | 11,830,000.00 USD | 11,830,000.00 USD | 392,980.00 USD | 82,050.00 USD | 244,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 3,860.00 USD | 560,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.30` | 5,160,000.00 USD | 5,160,000.00 USD | 39,880.00 USD | 7,520.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 5,210,000.00 USD | 5,210,000.00 USD | 28,930.00 USD | 5,500.00 USD | 12,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.31` | 12,400,000.00 USD | 12,400,000.00 USD | 308,150.00 USD | 55,090.00 USD | 209,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 5,240,000.00 USD | 5,240,000.00 USD | 17,660.00 USD | 1,330.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 5,260,000.00 USD | 5,260,000.00 USD | 12,710.00 USD | 6,000.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.33` | 12,650,000.00 USD | 12,650,000.00 USD | 134,040.00 USD | 29,420.00 USD | 82,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 5,320,000.00 USD | 5,320,000.00 USD | 46,100.00 USD | 3,660.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.35` | 5,350,000.00 USD | 5,350,000.00 USD | 13,620.00 USD | 1,320.00 USD | 14,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.35` | 12,930,000.00 USD | 12,930,000.00 USD | 114,090.00 USD | 67,130.00 USD | 98,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 5,370,000.00 USD | 5,370,000.00 USD | 4,730.00 USD | 6,760.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 5,390,000.00 USD | 5,390,000.00 USD | 13,170.00 USD | 6,780.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.37` | 13,260,000.00 USD | 13,260,000.00 USD | 211,790.00 USD | 34,660.00 USD | 84,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 5,420,000.00 USD | 5,420,000.00 USD | 15,290.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.39` | 5,430,000.00 USD | 5,430,000.00 USD | 8,850.00 USD | 1,600.00 USD | 12.83 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.39` | 13,580,000.00 USD | 13,580,000.00 USD | 206,980.00 USD | 32,960.00 USD | 86,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 5,460,000.00 USD | 5,460,000.00 USD | 22,270.00 USD | 0.00 USD | 12.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 5,470,000.00 USD | 5,470,000.00 USD | 4,410.00 USD | 378.69 USD | 10,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.41` | 13,980,000.00 USD | 13,980,000.00 USD | 265,720.00 USD | 30,790.00 USD | 99,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 1,450.00 USD | 561,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 5,490,000.00 USD | 5,490,000.00 USD | 9,240.00 USD | 3,010.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.43` | 5,500,000.00 USD | 5,500,000.00 USD | 5,380.00 USD | 1,380.00 USD | 25.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.43` | 14,070,000.00 USD | 14,070,000.00 USD | 33,890.00 USD | 15,080.00 USD | 42,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 5,500,000.00 USD | 5,500,000.00 USD | 795.69 USD | 1,840.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 5,510,000.00 USD | 5,510,000.00 USD | 96.25 USD | 1,240.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.45` | 14,160,000.00 USD | 14,160,000.00 USD | 68,680.00 USD | 11,560.00 USD | 9,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.46` | 5,530,000.00 USD | 5,530,000.00 USD | 16,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.47` | 5,540,000.00 USD | 5,540,000.00 USD | 1,180.00 USD | 1,900.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.47` | 14,220,000.00 USD | 14,220,000.00 USD | 44,170.00 USD | 5,760.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.48` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 494.12 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 5,550,000.00 USD | 5,550,000.00 USD | 9,740.00 USD | 689.91 USD | 3,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.49` | 14,270,000.00 USD | 14,270,000.00 USD | 25,360.00 USD | 10,200.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.51` | 3,580.00 USD | 565,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.51` | 14,360,000.00 USD | 14,360,000.00 USD | 57,130.00 USD | 7,150.00 USD | 25,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.53` | 14,420,000.00 USD | 14,420,000.00 USD | 50,200.00 USD | 9,410.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.55` | 14,440,000.00 USD | 14,440,000.00 USD | 11,560.00 USD | 11,570.00 USD | 398.17 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.57` | 14,500,000.00 USD | 14,500,000.00 USD | 31,530.00 USD | 2,130.00 USD | 24,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.59` | 14,530,000.00 USD | 14,530,000.00 USD | 14,070.00 USD | 7,840.00 USD | 14,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.61` | 14,580,000.00 USD | 14,580,000.00 USD | 37,000.00 USD | 0.00 USD | 11,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.62` | 138.98 USD | 565,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.64` | 1,930.00 USD | 567,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.68` | 319.28 USD | 567,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.69` | 285.51 USD | 567,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 567,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.88` | 371.77 USD | 568,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.10` | 119.83 USD | 568,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 2,650.00 USD | 571,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 571,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.81` | 1,150.00 USD | 572,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 117,020.00 USD | 689,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.11` | 55,520.00 USD | 745,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,670.00 USD | 756,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.30` | 960.92 USD | 757,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.44` | 1,620.00 USD | 759,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.61` | 326.68 USD | 759,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,410.00 USD | 772,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.69` | 296,760.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.93` | 505.74 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,050.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.46` | 63,360.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.90` | 75,090.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.02` | 4,170.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.04` | 246.89 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.09` | 219.34 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.24` | 875.67 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.39` | 20,010.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.72` | 234.30 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.77` | 185.55 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.82` | 1,700.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.36` | 265,080.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.43` | 1,900.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.50` | 117.28 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.64` | 23,530.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.98` | 1,690.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.00` | 1,940.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.02` | 191.87 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.05` | 207.78 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.05` | 575.27 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.07` | 6,740.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.14` | 1,270.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.20` | 263.60 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.98` | 2,290,000.00 USD | 0.00 USD | 1,510.00 USD | `-77.04%` | `762.30` |
| `Live` | `Long` | `2.00` | 2,290,000.00 USD | 0.00 USD | 160.40 USD | `-76.69%` | `80.00` |
| `Live` | `Long` | `2.02` | 2,290,000.00 USD | 0.00 USD | 223.28 USD | `-76.57%` | `110.81` |
| `Live` | `Long` | `2.04` | 2,290,000.00 USD | 0.00 USD | 110.52 USD | `-76.34%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,290,000.00 USD | 0.00 USD | 4,920.00 USD | `-75.99%` | `2,382.76` |
| `Live` | `Long` | `2.12` | 2,280,000.00 USD | 0.00 USD | 565.80 USD | `-75.29%` | `266.26` |
| `Live` | `Long` | `2.19` | 2,280,000.00 USD | 0.00 USD | 252.43 USD | `-74.48%` | `115.00` |
| `Live` | `Long` | `2.23` | 2,280,000.00 USD | 0.00 USD | 257.03 USD | `-74.02%` | `115.00` |
| `Live` | `Long` | `2.33` | 2,280,000.00 USD | 0.00 USD | 267.38 USD | `-72.97%` | `115.00` |
| `Live` | `Long` | `2.69` | 2,280,000.00 USD | 0.00 USD | 942.44 USD | `-68.78%` | `351.00` |
| `Live` | `Long` | `2.73` | 2,280,000.00 USD | 0.00 USD | 10,990.00 USD | `-68.32%` | `4,033.48` |
| `Live` | `Long` | `2.87` | 2,270,000.00 USD | 0.00 USD | 232.67 USD | `-66.69%` | `81.21` |
| `Live` | `Long` | `2.90` | 2,270,000.00 USD | 0.00 USD | 332.93 USD | `-66.34%` | `115.00` |
| `Live` | `Long` | `2.94` | 2,270,000.00 USD | 0.00 USD | 44,510.00 USD | `-65.88%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,220,000.00 USD | 0.00 USD | 111.12 USD | `-65.41%` | `37.35` |
| `Live` | `Long` | `3.06` | 2,220,000.00 USD | 0.00 USD | 1,150.00 USD | `-64.48%` | `377.71` |
| `Live` | `Long` | `3.06` | 2,220,000.00 USD | 0.00 USD | 21,430.00 USD | `-64.37%` | `6,990.57` |
| `Live` | `Long` | `3.15` | 2,200,000.00 USD | 0.00 USD | 23,480.00 USD | `-63.44%` | `7,465.11` |
| `Live` | `Long` | `3.35` | 2,180,000.00 USD | 0.00 USD | 905.85 USD | `-60.99%` | `270.00` |
| `Live` | `Long` | `3.37` | 2,180,000.00 USD | 0.00 USD | 389.53 USD | `-60.88%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,180,000.00 USD | 0.00 USD | 151.88 USD | `-60.76%` | `45.00` |
| `Live` | `Long` | `3.54` | 2,180,000.00 USD | 0.00 USD | 392.22 USD | `-58.79%` | `110.64` |
| `Live` | `Long` | `3.58` | 2,180,000.00 USD | 0.00 USD | 8,600.00 USD | `-58.32%` | `2,400.00` |
| `Live` | `Long` | `3.62` | 2,170,000.00 USD | 0.00 USD | 590.29 USD | `-57.86%` | `162.84` |
| `Live` | `Long` | `3.67` | 2,170,000.00 USD | 0.00 USD | 109.95 USD | `-57.39%` | `30.00` |
| `Live` | `Long` | `3.75` | 2,170,000.00 USD | 0.00 USD | 1,500.00 USD | `-56.34%` | `400.00` |
| `Live` | `Long` | `3.90` | 2,170,000.00 USD | 0.00 USD | 131.73 USD | `-54.72%` | `33.82` |
| `Live` | `Long` | `4.03` | 2,170,000.00 USD | 0.00 USD | 402.70 USD | `-53.21%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,160,000.00 USD | 0.00 USD | 152.29 USD | `-52.97%` | `37.65` |
| `Live` | `Long` | `4.16` | 2,160,000.00 USD | 0.00 USD | 159.68 USD | `-51.69%` | `38.43` |
| `Live` | `Long` | `4.18` | 2,160,000.00 USD | 0.00 USD | 390.54 USD | `-51.35%` | `93.32` |
| `Live` | `Long` | `4.24` | 2,160,000.00 USD | 0.00 USD | 169.40 USD | `-50.76%` | `40.00` |
| `Live` | `Long` | `4.25` | 2,160,000.00 USD | 0.00 USD | 196.42 USD | `-50.65%` | `46.27` |
| `Live` | `Long` | `4.45` | 2,160,000.00 USD | 0.00 USD | 110.77 USD | `-48.32%` | `24.92` |
| `Live` | `Long` | `4.58` | 2,160,000.00 USD | 0.00 USD | 107.56 USD | `-46.69%` | `23.46` |
| `Live` | `Long` | `4.59` | 2,160,000.00 USD | 0.00 USD | 30,970.00 USD | `-46.58%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,130,000.00 USD | 0.00 USD | 3,420.00 USD | `-46.23%` | `739.57` |
| `Live` | `Long` | `4.66` | 2,130,000.00 USD | 0.00 USD | 105.11 USD | `-45.88%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,130,000.00 USD | 0.00 USD | 3,280.00 USD | `-45.76%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,130,000.00 USD | 0.00 USD | 1,490.00 USD | `-45.65%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,120,000.00 USD | 0.00 USD | 8,380.00 USD | `-45.53%` | `1,787.97` |
| `Live` | `Long` | `4.70` | 2,120,000.00 USD | 0.00 USD | 7,040.00 USD | `-45.42%` | `1,500.00` |
| `Live` | `Long` | `4.75` | 2,110,000.00 USD | 0.00 USD | 474.50 USD | `-44.83%` | `100.00` |
| `Live` | `Long` | `4.76` | 2,110,000.00 USD | 0.00 USD | 105.64 USD | `-44.60%` | `22.17` |
| `Live` | `Long` | `4.78` | 2,110,000.00 USD | 0.00 USD | 525.25 USD | `-44.49%` | `110.00` |
| `Live` | `Long` | `4.83` | 2,110,000.00 USD | 0.00 USD | 3,320.00 USD | `-43.79%` | `685.94` |
| `Live` | `Long` | `4.87` | 2,100,000.00 USD | 0.00 USD | 310.14 USD | `-43.44%` | `63.75` |
| `Live` | `Long` | `4.88` | 2,100,000.00 USD | 0.00 USD | 505.68 USD | `-43.32%` | `103.73` |
| `Live` | `Long` | `4.89` | 2,100,000.00 USD | 0.00 USD | 16,080.00 USD | `-43.09%` | `3,286.00` |
| `Live` | `Long` | `4.91` | 2,090,000.00 USD | 0.00 USD | 4,110.00 USD | `-42.97%` | `838.83` |
| `Live` | `Long` | `4.92` | 2,080,000.00 USD | 0.00 USD | 1,230.00 USD | `-42.86%` | `251.00` |
| `Live` | `Long` | `4.95` | 2,080,000.00 USD | 0.00 USD | 352.68 USD | `-42.51%` | `71.32` |
| `Live` | `Long` | `4.96` | 2,080,000.00 USD | 0.00 USD | 945.36 USD | `-42.39%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,080,000.00 USD | 0.00 USD | 4,090.00 USD | `-42.28%` | `824.62` |
| `Live` | `Long` | `4.97` | 2,080,000.00 USD | 0.00 USD | 282.23 USD | `-42.16%` | `56.73` |
| `Live` | `Long` | `5.00` | 2,080,000.00 USD | 0.00 USD | 269.53 USD | `-41.93%` | `53.96` |
| `Live` | `Long` | `5.01` | 2,080,000.00 USD | 0.00 USD | 56,390.00 USD | `-41.70%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,020,000.00 USD | 0.00 USD | 216.43 USD | `-41.58%` | `43.07` |
| `Live` | `Long` | `5.04` | 2,020,000.00 USD | 0.00 USD | 482.71 USD | `-41.46%` | `95.87` |
| `Live` | `Long` | `5.05` | 2,020,000.00 USD | 0.00 USD | 710.03 USD | `-41.23%` | `140.46` |
| `Live` | `Long` | `5.08` | 2,020,000.00 USD | 0.00 USD | 954.05 USD | `-41.00%` | `187.99` |
| `Live` | `Long` | `5.08` | 2,020,000.00 USD | 0.00 USD | 105.46 USD | `-40.88%` | `20.74` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 915.43 USD | `-40.53%` | `178.97` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 250.20 USD | `-40.42%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,020,000.00 USD | 0.00 USD | 396.06 USD | `-40.30%` | `77.13` |
| `Live` | `Long` | `5.14` | 2,020,000.00 USD | 0.00 USD | 3,070.00 USD | `-40.18%` | `596.05` |
| `Live` | `Long` | `5.17` | 2,010,000.00 USD | 0.00 USD | 1,620.00 USD | `-39.84%` | `312.94` |
| `Live` | `Long` | `5.18` | 2,010,000.00 USD | 0.00 USD | 150.57 USD | `-39.72%` | `29.04` |
| `Live` | `Long` | `5.21` | 2,010,000.00 USD | 0.00 USD | 421.89 USD | `-39.37%` | `80.90` |
| `Live` | `Long` | `5.25` | 2,010,000.00 USD | 0.00 USD | 159,630.00 USD | `-39.02%` | `30,435.20` |
| `Live` | `Long` | `5.26` | 1,850,000.00 USD | 0.00 USD | 2,230.00 USD | `-38.79%` | `423.54` |
| `Live` | `Long` | `5.29` | 1,850,000.00 USD | 0.00 USD | 640.70 USD | `-38.56%` | `121.23` |
| `Live` | `Long` | `5.32` | 1,850,000.00 USD | 0.00 USD | 232.85 USD | `-38.21%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,850,000.00 USD | 0.00 USD | 716.11 USD | `-38.09%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,850,000.00 USD | 0.00 USD | 660.46 USD | `-37.28%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,850,000.00 USD | 0.00 USD | 20,560.00 USD | `-37.05%` | `3,797.34` |
| `Live` | `Long` | `5.42` | 1,830,000.00 USD | 0.00 USD | 160,400.00 USD | `-36.93%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,670,000.00 USD | 0.00 USD | 1,360.00 USD | `-36.81%` | `250.00` |
| `Live` | `Long` | `5.45` | 1,660,000.00 USD | 0.00 USD | 299.48 USD | `-36.70%` | `55.00` |
| `Live` | `Long` | `5.46` | 1,660,000.00 USD | 0.00 USD | 264.72 USD | `-36.46%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-36.35%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,660,000.00 USD | 0.00 USD | 354.06 USD | `-36.23%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,660,000.00 USD | 0.00 USD | 19,290.00 USD | `-36.12%` | `3,510.41` |
| `Live` | `Long` | `5.54` | 1,640,000.00 USD | 0.00 USD | 2,880.00 USD | `-35.53%` | `519.63` |
| `Live` | `Long` | `5.58` | 1,640,000.00 USD | 0.00 USD | 63,260.00 USD | `-35.18%` | `11,347.58` |
| `Live` | `Long` | `5.61` | 1,580,000.00 USD | 0.00 USD | 34,490.00 USD | `-34.84%` | `6,153.60` |
| `Live` | `Long` | `5.63` | 1,540,000.00 USD | 0.00 USD | 468.55 USD | `-34.49%` | `83.15` |
| `Live` | `Long` | `5.72` | 1,540,000.00 USD | 0.00 USD | 2,390.00 USD | `-33.44%` | `417.17` |
| `Live` | `Long` | `5.74` | 1,540,000.00 USD | 0.00 USD | 661.65 USD | `-33.32%` | `115.37` |
| `Live` | `Long` | `5.75` | 1,540,000.00 USD | 0.00 USD | 125.70 USD | `-33.21%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,540,000.00 USD | 0.00 USD | 4,530.00 USD | `-33.09%` | `787.78` |
| `Live` | `Long` | `5.76` | 1,530,000.00 USD | 0.00 USD | 10,850.00 USD | `-32.98%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,520,000.00 USD | 0.00 USD | 801.40 USD | `-32.86%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,520,000.00 USD | 0.00 USD | 635.31 USD | `-32.63%` | `109.63` |
| `Live` | `Long` | `5.82` | 1,520,000.00 USD | 0.00 USD | 688.15 USD | `-32.39%` | `118.34` |
| `Live` | `Long` | `5.84` | 1,520,000.00 USD | 0.00 USD | 146.13 USD | `-32.05%` | `25.00` |
| `Live` | `Long` | `5.86` | 1,520,000.00 USD | 0.00 USD | 2,110.00 USD | `-31.93%` | `360.33` |
| `Live` | `Long` | `5.89` | 1,520,000.00 USD | 0.00 USD | 984.70 USD | `-31.46%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,520,000.00 USD | 0.00 USD | 399.18 USD | `-31.35%` | `67.60` |
| `Live` | `Long` | `5.95` | 1,520,000.00 USD | 0.00 USD | 147.55 USD | `-30.88%` | `24.82` |
| `Live` | `Long` | `5.96` | 1,520,000.00 USD | 0.00 USD | 11,720.00 USD | `-30.77%` | `1,968.19` |
| `Live` | `Long` | `5.96` | 1,510,000.00 USD | 0.00 USD | 6,320.00 USD | `-30.65%` | `1,060.32` |
| `Live` | `Long` | `5.97` | 1,500,000.00 USD | 0.00 USD | 585.97 USD | `-30.53%` | `98.07` |
| `Live` | `Long` | `6.00` | 1,500,000.00 USD | 0.00 USD | 341.56 USD | `-30.19%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,500,000.00 USD | 0.00 USD | 446.85 USD | `-30.07%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,500,000.00 USD | 0.00 USD | 437.84 USD | `-29.72%` | `72.43` |
| `Live` | `Long` | `6.05` | 1,500,000.00 USD | 0.00 USD | 1,310.00 USD | `-29.60%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,500,000.00 USD | 0.00 USD | 265.10 USD | `-29.49%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,500,000.00 USD | 0.00 USD | 1,690.00 USD | `-29.37%` | `278.94` |
| `Live` | `Long` | `6.09` | 1,490,000.00 USD | 0.00 USD | 3,530.00 USD | `-29.14%` | `579.39` |
| `Live` | `Long` | `6.12` | 1,490,000.00 USD | 0.00 USD | 1,140.00 USD | `-28.91%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,490,000.00 USD | 0.00 USD | 137.02 USD | `-28.79%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,490,000.00 USD | 0.00 USD | 2,030.00 USD | `-28.67%` | `330.65` |
| `Live` | `Long` | `6.14` | 1,490,000.00 USD | 0.00 USD | 238.61 USD | `-28.56%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,490,000.00 USD | 0.00 USD | 7,810.00 USD | `-28.44%` | `1,268.30` |
| `Live` | `Long` | `6.17` | 1,480,000.00 USD | 0.00 USD | 104.36 USD | `-28.21%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,480,000.00 USD | 0.00 USD | 310.25 USD | `-27.86%` | `50.00` |
| `Live` | `Long` | `6.22` | 1,480,000.00 USD | 0.00 USD | 795.06 USD | `-27.63%` | `127.72` |
| `Live` | `Long` | `6.25` | 1,480,000.00 USD | 0.00 USD | 972.65 USD | `-27.28%` | `155.50` |
| `Live` | `Long` | `6.28` | 1,480,000.00 USD | 0.00 USD | 354,280.00 USD | `-27.05%` | `56,459.40` |
| `Live` | `Long` | `6.29` | 1,120,000.00 USD | 0.00 USD | 1,420.00 USD | `-26.93%` | `225.14` |
| `Live` | `Long` | `6.33` | 1,120,000.00 USD | 0.00 USD | 277.48 USD | `-26.47%` | `43.87` |
| `Live` | `Long` | `6.36` | 1,120,000.00 USD | 0.00 USD | 4,470.00 USD | `-26.12%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,120,000.00 USD | 0.00 USD | 287,230.00 USD | `-26.00%` | `45,126.53` |
| `Live` | `Long` | `6.38` | 829,240.00 USD | 0.00 USD | 1,310.00 USD | `-25.88%` | `204.92` |
| `Live` | `Long` | `6.38` | 827,940.00 USD | 0.00 USD | 5,120.00 USD | `-25.77%` | `801.31` |
| `Live` | `Long` | `6.42` | 822,820.00 USD | 0.00 USD | 306.32 USD | `-25.42%` | `47.75` |
| `Live` | `Long` | `6.42` | 822,510.00 USD | 0.00 USD | 484.64 USD | `-25.30%` | `75.43` |
| `Live` | `Long` | `6.43` | 822,030.00 USD | 0.00 USD | 6,780.00 USD | `-25.19%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 815,250.00 USD | 0.00 USD | 1,050.00 USD | `-24.84%` | `162.75` |
| `Live` | `Long` | `6.49` | 814,200.00 USD | 0.00 USD | 1,480.00 USD | `-24.61%` | `228.41` |
| `Live` | `Long` | `6.50` | 812,720.00 USD | 0.00 USD | 6,030.00 USD | `-24.49%` | `928.10` |
| `Live` | `Long` | `6.54` | 806,690.00 USD | 0.00 USD | 852.03 USD | `-24.02%` | `130.38` |
| `Live` | `Long` | `6.54` | 805,840.00 USD | 0.00 USD | 8,970.00 USD | `-23.91%` | `1,370.89` |
| `Live` | `Long` | `6.55` | 796,870.00 USD | 0.00 USD | 1,510.00 USD | `-23.79%` | `231.02` |
| `Live` | `Long` | `6.59` | 795,350.00 USD | 0.00 USD | 2,870.00 USD | `-23.33%` | `435.69` |
| `Live` | `Long` | `6.62` | 792,480.00 USD | 0.00 USD | 2,110.00 USD | `-23.09%` | `318.57` |
| `Live` | `Long` | `6.62` | 790,370.00 USD | 0.00 USD | 364.90 USD | `-22.98%` | `55.08` |
| `Live` | `Long` | `6.63` | 790,010.00 USD | 0.00 USD | 245.89 USD | `-22.86%` | `37.06` |
| `Live` | `Long` | `6.66` | 789,760.00 USD | 0.00 USD | 1,740.00 USD | `-22.63%` | `261.71` |
| `Live` | `Long` | `6.67` | 788,020.00 USD | 0.00 USD | 1,320.00 USD | `-22.40%` | `198.12` |
| `Live` | `Long` | `6.68` | 786,700.00 USD | 0.00 USD | 3,160.00 USD | `-22.28%` | `472.28` |
| `Live` | `Long` | `6.70` | 783,540.00 USD | 0.00 USD | 15,800.00 USD | `-22.16%` | `2,360.46` |
| `Live` | `Long` | `6.71` | 767,740.00 USD | 0.00 USD | 11,000.00 USD | `-22.05%` | `1,641.31` |
| `Live` | `Long` | `6.71` | 756,730.00 USD | 0.00 USD | 6,180.00 USD | `-21.93%` | `920.74` |
| `Live` | `Long` | `6.72` | 750,550.00 USD | 0.00 USD | 2,200.00 USD | `-21.82%` | `326.90` |
| `Live` | `Long` | `6.75` | 748,350.00 USD | 0.00 USD | 1,330.00 USD | `-21.47%` | `196.95` |
| `Live` | `Long` | `6.78` | 747,020.00 USD | 0.00 USD | 7,990.00 USD | `-21.23%` | `1,179.83` |
| `Live` | `Long` | `6.79` | 739,030.00 USD | 0.00 USD | 22,020.00 USD | `-21.12%` | `3,245.57` |
| `Live` | `Long` | `6.79` | 717,010.00 USD | 0.00 USD | 5,170.00 USD | `-21.00%` | `761.18` |
| `Live` | `Long` | `6.80` | 711,830.00 USD | 0.00 USD | 219.12 USD | `-20.88%` | `32.20` |
| `Live` | `Long` | `6.82` | 711,620.00 USD | 0.00 USD | 8,520.00 USD | `-20.77%` | `1,249.79` |
| `Live` | `Long` | `6.83` | 703,100.00 USD | 0.00 USD | 158.14 USD | `-20.65%` | `23.17` |
| `Live` | `Long` | `6.87` | 702,940.00 USD | 0.00 USD | 3,340.00 USD | `-20.19%` | `486.46` |
| `Live` | `Long` | `6.88` | 699,600.00 USD | 0.00 USD | 263.66 USD | `-20.07%` | `38.35` |
| `Live` | `Long` | `6.88` | 699,340.00 USD | 0.00 USD | 3,990.00 USD | `-19.95%` | `579.76` |
| `Live` | `Long` | `6.92` | 695,350.00 USD | 0.00 USD | 579.62 USD | `-19.49%` | `83.70` |
| `Live` | `Long` | `6.93` | 694,770.00 USD | 0.00 USD | 3,500.00 USD | `-19.37%` | `504.07` |
| `Live` | `Long` | `6.95` | 691,270.00 USD | 0.00 USD | 215.30 USD | `-19.26%` | `31.00` |
| `Live` | `Long` | `6.96` | 691,050.00 USD | 0.00 USD | 7,240.00 USD | `-19.14%` | `1,041.68` |
| `Live` | `Long` | `6.96` | 683,810.00 USD | 0.00 USD | 636.74 USD | `-19.02%` | `91.42` |
| `Live` | `Long` | `6.97` | 683,170.00 USD | 0.00 USD | 128,810.00 USD | `-18.91%` | `18,466.99` |
| `Live` | `Long` | `7.00` | 554,370.00 USD | 0.00 USD | 1,040.00 USD | `-18.68%` | `149.32` |
| `Live` | `Long` | `7.01` | 553,320.00 USD | 0.00 USD | 20,890.00 USD | `-18.44%` | `2,978.11` |
| `Live` | `Long` | `7.03` | 532,430.00 USD | 0.00 USD | 1,370.00 USD | `-18.33%` | `194.51` |
| `Live` | `Long` | `7.07` | 531,060.00 USD | 0.00 USD | 23,960.00 USD | `-17.86%` | `3,390.75` |
| `Live` | `Long` | `7.08` | 507,110.00 USD | 0.00 USD | 6,700.00 USD | `-17.75%` | `947.44` |
| `Live` | `Long` | `7.08` | 500,400.00 USD | 0.00 USD | 1,050.00 USD | `-17.63%` | `148.63` |
| `Live` | `Long` | `7.09` | 499,350.00 USD | 0.00 USD | 2,130.00 USD | `-17.51%` | `300.00` |
| `Live` | `Long` | `7.11` | 497,220.00 USD | 0.00 USD | 28,530.00 USD | `-17.40%` | `4,015.35` |
| `Live` | `Long` | `7.12` | 468,690.00 USD | 0.00 USD | 379.66 USD | `-17.28%` | `53.36` |
| `Live` | `Long` | `7.13` | 468,310.00 USD | 0.00 USD | 13,410.00 USD | `-17.05%` | `1,879.32` |
| `Live` | `Long` | `7.14` | 454,910.00 USD | 0.00 USD | 20,270.00 USD | `-16.93%` | `2,837.00` |
| `Live` | `Long` | `7.17` | 434,640.00 USD | 0.00 USD | 4,470.00 USD | `-16.58%` | `622.52` |
| `Live` | `Long` | `7.18` | 430,170.00 USD | 0.00 USD | 1,440.00 USD | `-16.47%` | `200.95` |
| `Live` | `Long` | `7.21` | 428,720.00 USD | 0.00 USD | 322.94 USD | `-16.12%` | `44.76` |
| `Live` | `Long` | `7.24` | 428,400.00 USD | 0.00 USD | 2,500.00 USD | `-15.89%` | `345.21` |
| `Live` | `Long` | `7.25` | 425,900.00 USD | 0.00 USD | 185.83 USD | `-15.77%` | `25.65` |
| `Live` | `Long` | `7.25` | 425,720.00 USD | 0.00 USD | 21,280.00 USD | `-15.65%` | `2,933.17` |
| `Live` | `Long` | `7.29` | 404,440.00 USD | 0.00 USD | 36,420.00 USD | `-15.30%` | `5,000.00` |
| `Live` | `Long` | `7.29` | 368,010.00 USD | 0.00 USD | 1,680.00 USD | `-15.19%` | `230.97` |
| `Live` | `Long` | `7.30` | 366,330.00 USD | 0.00 USD | 29,220.00 USD | `-15.07%` | `4,000.00` |
| `Live` | `Long` | `7.33` | 337,110.00 USD | 0.00 USD | 13,110.00 USD | `-14.72%` | `1,787.05` |
| `Live` | `Long` | `7.34` | 324,000.00 USD | 0.00 USD | 1,400.00 USD | `-14.61%` | `190.54` |
| `Live` | `Long` | `7.36` | 322,600.00 USD | 0.00 USD | 5,290.00 USD | `-14.49%` | `719.63` |
| `Live` | `Long` | `7.37` | 317,310.00 USD | 0.00 USD | 2,940.00 USD | `-14.37%` | `399.15` |
| `Live` | `Long` | `7.38` | 314,370.00 USD | 0.00 USD | 1,100.00 USD | `-14.26%` | `148.75` |
| `Live` | `Long` | `7.38` | 313,270.00 USD | 0.00 USD | 227.97 USD | `-14.14%` | `30.87` |
| `Live` | `Long` | `7.42` | 313,040.00 USD | 0.00 USD | 147.61 USD | `-13.68%` | `19.88` |
| `Live` | `Long` | `7.43` | 312,900.00 USD | 0.00 USD | 2,430.00 USD | `-13.56%` | `327.05` |
| `Live` | `Long` | `7.45` | 310,460.00 USD | 0.00 USD | 2,410.00 USD | `-13.44%` | `324.35` |
| `Live` | `Long` | `7.46` | 308,050.00 USD | 0.00 USD | 10,390.00 USD | `-13.33%` | `1,393.53` |
| `Live` | `Long` | `7.46` | 297,660.00 USD | 0.00 USD | 4,590.00 USD | `-13.21%` | `614.36` |
| `Live` | `Long` | `7.47` | 293,070.00 USD | 0.00 USD | 1,120.00 USD | `-13.10%` | `149.52` |
| `Live` | `Long` | `7.50` | 291,960.00 USD | 0.00 USD | 962.81 USD | `-12.86%` | `128.46` |
| `Live` | `Long` | `7.50` | 290,990.00 USD | 0.00 USD | 421.78 USD | `-12.75%` | `56.20` |
| `Live` | `Long` | `7.51` | 290,570.00 USD | 0.00 USD | 1,710.00 USD | `-12.63%` | `228.21` |
| `Live` | `Long` | `7.53` | 288,860.00 USD | 0.00 USD | 1,570.00 USD | `-12.51%` | `208.52` |
| `Live` | `Long` | `7.54` | 287,290.00 USD | 0.00 USD | 4,210.00 USD | `-12.40%` | `559.01` |
| `Live` | `Long` | `7.54` | 283,080.00 USD | 0.00 USD | 1,510.00 USD | `-12.28%` | `200.00` |
| `Live` | `Long` | `7.55` | 281,570.00 USD | 0.00 USD | 1,070.00 USD | `-12.17%` | `141.09` |
| `Live` | `Long` | `7.57` | 280,500.00 USD | 0.00 USD | 25,060.00 USD | `-12.05%` | `3,312.23` |
| `Live` | `Long` | `7.58` | 255,440.00 USD | 0.00 USD | 118.25 USD | `-11.93%` | `15.61` |
| `Live` | `Long` | `7.62` | 255,330.00 USD | 0.00 USD | 754.04 USD | `-11.47%` | `99.02` |
| `Live` | `Long` | `7.62` | 254,570.00 USD | 0.00 USD | 787.51 USD | `-11.35%` | `103.28` |
| `Live` | `Long` | `7.63` | 253,780.00 USD | 0.00 USD | 378.93 USD | `-11.24%` | `49.63` |
| `Live` | `Long` | `7.66` | 253,400.00 USD | 0.00 USD | 135.42 USD | `-11.00%` | `17.69` |
| `Live` | `Long` | `7.67` | 253,270.00 USD | 0.00 USD | 256.09 USD | `-10.89%` | `33.41` |
| `Live` | `Long` | `7.67` | 253,010.00 USD | 0.00 USD | 140.45 USD | `-10.77%` | `18.30` |
| `Live` | `Long` | `7.68` | 252,870.00 USD | 0.00 USD | 739.30 USD | `-10.65%` | `96.20` |
| `Live` | `Long` | `7.70` | 252,130.00 USD | 0.00 USD | 6,690.00 USD | `-10.54%` | `869.22` |
| `Live` | `Long` | `7.75` | 245,440.00 USD | 0.00 USD | 500.12 USD | `-9.84%` | `64.49` |
| `Live` | `Long` | `7.76` | 244,940.00 USD | 0.00 USD | 455.73 USD | `-9.72%` | `58.69` |
| `Live` | `Long` | `7.78` | 244,490.00 USD | 0.00 USD | 12,100.00 USD | `-9.61%` | `1,555.99` |
| `Live` | `Long` | `7.79` | 232,390.00 USD | 0.00 USD | 3,750.00 USD | `-9.49%` | `481.06` |
| `Live` | `Long` | `7.79` | 228,650.00 USD | 0.00 USD | 4,480.00 USD | `-9.38%` | `574.50` |
| `Live` | `Long` | `7.80` | 224,170.00 USD | 0.00 USD | 6,380.00 USD | `-9.26%` | `817.06` |
| `Live` | `Long` | `7.83` | 217,790.00 USD | 0.00 USD | 1,940.00 USD | `-9.03%` | `247.42` |
| `Live` | `Long` | `7.84` | 215,850.00 USD | 0.00 USD | 22,560.00 USD | `-8.79%` | `2,875.86` |
| `Live` | `Long` | `7.87` | 193,290.00 USD | 0.00 USD | 233.83 USD | `-8.56%` | `29.73` |
| `Live` | `Long` | `7.88` | 193,060.00 USD | 0.00 USD | 555.19 USD | `-8.45%` | `70.50` |
| `Live` | `Long` | `7.89` | 192,500.00 USD | 0.00 USD | 13,270.00 USD | `-8.21%` | `1,680.67` |
| `Live` | `Long` | `7.91` | 179,240.00 USD | 0.00 USD | 2,930.00 USD | `-8.10%` | `370.74` |
| `Live` | `Long` | `7.92` | 176,310.00 USD | 0.00 USD | 4,600.00 USD | `-7.86%` | `580.78` |
| `Live` | `Long` | `7.93` | 171,700.00 USD | 0.00 USD | 16,340.00 USD | `-7.75%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 155,360.00 USD | 0.00 USD | 141.74 USD | `-7.63%` | `17.84` |
| `Live` | `Long` | `7.96` | 155,220.00 USD | 0.00 USD | 127,900.00 USD | `-7.52%` | `16,078.30` |
| `Live` | `Long` | `7.97` | 27,320.00 USD | 0.00 USD | 1,580.00 USD | `-7.28%` | `198.26` |
| `Live` | `Long` | `7.99` | 25,730.00 USD | 0.00 USD | 1,280.00 USD | `-7.17%` | `160.68` |
| `Live` | `Long` | `8.00` | 24,450.00 USD | 0.00 USD | 889.52 USD | `-7.05%` | `111.26` |
| `Live` | `Long` | `8.06` | 23,560.00 USD | 0.00 USD | 439.54 USD | `-6.24%` | `54.50` |
| `Live` | `Long` | `8.07` | 23,120.00 USD | 0.00 USD | 21,710.00 USD | `-6.12%` | `2,688.93` |
| `Live` | `Long` | `8.09` | 1,410.00 USD | 0.00 USD | 887.25 USD | `-6.00%` | `109.74` |
| `Live` | `Long` | `8.12` | 521.62 USD | 0.00 USD | 521.62 USD | `-5.54%` | `64.20` |
| `Live` | `Short` | `8.69` | 209.31 USD | 209.31 USD | 0.00 USD | `+0.97%` | `24.10` |
| `Live` | `Short` | `8.82` | 6,210.00 USD | 6,000.00 USD | 0.00 USD | `+2.60%` | `680.16` |
| `Live` | `Short` | `8.87` | 7,370.00 USD | 1,160.00 USD | 0.00 USD | `+3.06%` | `130.57` |
| `Live` | `Short` | `8.88` | 8,060.00 USD | 691.70 USD | 0.00 USD | `+3.30%` | `77.85` |
| `Live` | `Short` | `8.95` | 11,200.00 USD | 3,140.00 USD | 0.00 USD | `+3.99%` | `350.65` |
| `Live` | `Short` | `8.96` | 11,430.00 USD | 227.82 USD | 0.00 USD | `+4.11%` | `25.44` |
| `Live` | `Short` | `8.99` | 551,130.00 USD | 539,710.00 USD | 0.00 USD | `+4.58%` | `60,000.94` |
| `Live` | `Short` | `9.05` | 551,350.00 USD | 213.70 USD | 0.00 USD | `+5.27%` | `23.60` |
| `Live` | `Short` | `9.10` | 555,240.00 USD | 3,890.00 USD | 0.00 USD | `+5.74%` | `427.53` |
| `Live` | `Short` | `9.14` | 555,420.00 USD | 180.80 USD | 0.00 USD | `+6.32%` | `19.77` |
| `Live` | `Short` | `9.22` | 555,830.00 USD | 416.69 USD | 0.00 USD | `+7.25%` | `45.17` |
| `Live` | `Short` | `9.29` | 556,160.00 USD | 326.09 USD | 0.00 USD | `+7.95%` | `35.12` |
| `Live` | `Short` | `9.29` | 560,020.00 USD | 3,860.00 USD | 0.00 USD | `+8.06%` | `415.00` |
| `Live` | `Short` | `9.41` | 561,460.00 USD | 1,450.00 USD | 0.00 USD | `+9.46%` | `153.50` |
| `Live` | `Short` | `9.51` | 565,040.00 USD | 3,580.00 USD | 0.00 USD | `+10.51%` | `376.48` |
| `Live` | `Short` | `9.62` | 565,180.00 USD | 138.98 USD | 0.00 USD | `+11.90%` | `14.44` |
| `Live` | `Short` | `9.64` | 567,110.00 USD | 1,930.00 USD | 0.00 USD | `+12.13%` | `200.61` |
| `Live` | `Short` | `9.68` | 567,430.00 USD | 319.28 USD | 0.00 USD | `+12.48%` | `33.00` |
| `Live` | `Short` | `9.69` | 567,720.00 USD | 285.51 USD | 0.00 USD | `+12.60%` | `29.48` |
| `Live` | `Short` | `9.73` | 567,910.00 USD | 192.95 USD | 0.00 USD | `+13.18%` | `19.82` |
| `Live` | `Short` | `9.88` | 568,280.00 USD | 371.77 USD | 0.00 USD | `+14.92%` | `37.61` |
| `Live` | `Short` | `10.10` | 568,400.00 USD | 119.83 USD | 0.00 USD | `+17.36%` | `11.87` |
| `Live` | `Short` | `10.35` | 571,060.00 USD | 2,650.00 USD | 0.00 USD | `+20.27%` | `256.58` |
| `Live` | `Short` | `10.56` | 571,580.00 USD | 523.81 USD | 0.00 USD | `+22.83%` | `49.58` |
| `Live` | `Short` | `10.81` | 572,730.00 USD | 1,150.00 USD | 0.00 USD | `+25.74%` | `106.17` |
| `Live` | `Short` | `11.01` | 689,750.00 USD | 117,020.00 USD | 0.00 USD | `+27.94%` | `10,633.00` |
| `Live` | `Short` | `11.11` | 745,270.00 USD | 55,520.00 USD | 0.00 USD | `+29.11%` | `5,000.00` |
| `Live` | `Short` | `11.27` | 756,940.00 USD | 11,670.00 USD | 0.00 USD | `+30.97%` | `1,035.87` |
| `Live` | `Short` | `11.30` | 757,900.00 USD | 960.92 USD | 0.00 USD | `+31.43%` | `85.00` |
| `Live` | `Short` | `11.44` | 759,520.00 USD | 1,620.00 USD | 0.00 USD | `+32.94%` | `141.51` |
| `Live` | `Short` | `11.61` | 759,850.00 USD | 326.68 USD | 0.00 USD | `+34.92%` | `28.15` |
| `Live` | `Short` | `11.62` | 772,260.00 USD | 12,410.00 USD | 0.00 USD | `+35.15%` | `1,067.86` |
| `Live` | `Short` | `11.69` | 1,070,000.00 USD | 296,760.00 USD | 0.00 USD | `+35.85%` | `25,397.02` |
| `Live` | `Short` | `11.93` | 1,070,000.00 USD | 505.74 USD | 0.00 USD | `+38.64%` | `42.41` |
| `Live` | `Short` | `11.95` | 1,070,000.00 USD | 1,050.00 USD | 0.00 USD | `+38.87%` | `87.54` |
| `Live` | `Short` | `12.30` | 1,070,000.00 USD | 1,730.00 USD | 0.00 USD | `+43.06%` | `140.71` |
| `Live` | `Short` | `12.40` | 1,070,000.00 USD | 343.62 USD | 0.00 USD | `+44.22%` | `27.70` |
| `Live` | `Short` | `12.46` | 1,140,000.00 USD | 63,360.00 USD | 0.00 USD | `+44.80%` | `5,087.03` |
| `Live` | `Short` | `13.20` | 1,220,000.00 USD | 87,940.00 USD | 0.00 USD | `+53.41%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 1,230,000.00 USD | 3,810.00 USD | 0.00 USD | `+54.57%` | `286.56` |
| `Live` | `Short` | `13.46` | 1,230,000.00 USD | 430.34 USD | 0.00 USD | `+56.54%` | `31.96` |
| `Live` | `Short` | `13.69` | 1,230,000.00 USD | 172.29 USD | 0.00 USD | `+59.10%` | `12.59` |
| `Live` | `Short` | `14.66` | 1,230,000.00 USD | 823.29 USD | 0.00 USD | `+70.50%` | `56.14` |
| `Live` | `Short` | `14.90` | 1,300,000.00 USD | 75,090.00 USD | 0.00 USD | `+73.29%` | `5,037.66` |
| `Live` | `Short` | `15.02` | 1,310,000.00 USD | 4,170.00 USD | 0.00 USD | `+74.56%` | `277.54` |
| `Live` | `Short` | `15.04` | 1,310,000.00 USD | 246.89 USD | 0.00 USD | `+74.91%` | `16.41` |
| `Live` | `Short` | `15.09` | 1,310,000.00 USD | 219.34 USD | 0.00 USD | `+75.38%` | `14.54` |
| `Live` | `Short` | `15.24` | 1,310,000.00 USD | 875.67 USD | 0.00 USD | `+77.24%` | `57.44` |
| `Live` | `Short` | `15.29` | 1,310,000.00 USD | 229.43 USD | 0.00 USD | `+77.82%` | `15.00` |
| `Live` | `Short` | `15.35` | 1,310,000.00 USD | 230.17 USD | 0.00 USD | `+78.40%` | `15.00` |
| `Live` | `Short` | `15.39` | 1,330,000.00 USD | 20,010.00 USD | 0.00 USD | `+78.98%` | `1,300.00` |
| `Live` | `Short` | `15.72` | 1,330,000.00 USD | 234.30 USD | 0.00 USD | `+82.82%` | `14.90` |
| `Live` | `Short` | `15.77` | 1,330,000.00 USD | 185.55 USD | 0.00 USD | `+83.28%` | `11.77` |
| `Live` | `Short` | `15.82` | 1,330,000.00 USD | 1,700.00 USD | 0.00 USD | `+83.98%` | `107.48` |
| `Live` | `Short` | `16.36` | 1,600,000.00 USD | 265,080.00 USD | 0.00 USD | `+90.14%` | `16,208.00` |
| `Live` | `Short` | `16.43` | 1,600,000.00 USD | 1,900.00 USD | 0.00 USD | `+91.07%` | `115.73` |
| `Live` | `Short` | `16.50` | 1,600,000.00 USD | 117.28 USD | 0.00 USD | `+91.77%` | `7.11` |
| `Live` | `Short` | `16.52` | 1,600,000.00 USD | 190.91 USD | 0.00 USD | `+92.00%` | `11.56` |
| `Live` | `Short` | `16.64` | 1,620,000.00 USD | 23,530.00 USD | 0.00 USD | `+93.40%` | `1,414.55` |
| `Live` | `Short` | `16.98` | 1,620,000.00 USD | 1,690.00 USD | 0.00 USD | `+97.47%` | `99.50` |
| `Live` | `Short` | `17.00` | 1,630,000.00 USD | 1,940.00 USD | 0.00 USD | `+97.70%` | `113.93` |
| `Live` | `Short` | `17.02` | 1,630,000.00 USD | 191.87 USD | 0.00 USD | `+97.93%` | `11.27` |
| `Live` | `Short` | `17.05` | 1,630,000.00 USD | 207.78 USD | 0.00 USD | `+98.17%` | `12.19` |
| `Live` | `Short` | `17.05` | 1,630,000.00 USD | 575.27 USD | 0.00 USD | `+98.28%` | `33.73` |
| `Live` | `Short` | `17.07` | 1,630,000.00 USD | 6,740.00 USD | 0.00 USD | `+98.51%` | `395.02` |
| `Live` | `Short` | `17.14` | 1,640,000.00 USD | 1,270.00 USD | 0.00 USD | `+99.21%` | `74.09` |
| `Live` | `Short` | `17.20` | 1,640,000.00 USD | 263.60 USD | 0.00 USD | `+99.91%` | `15.33` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 404,570.00 USD | 0.00 USD | 611.73 USD | `-72.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 403,960.00 USD | 0.00 USD | 793.75 USD | `-53.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 403,170.00 USD | 0.00 USD | 67,970.00 USD | `-41.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 335,200.00 USD | 0.00 USD | 205.30 USD | `-38.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 335,000.00 USD | 0.00 USD | 465.42 USD | `-36.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 334,530.00 USD | 0.00 USD | 349.35 USD | `-36.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 334,180.00 USD | 0.00 USD | 1,020.00 USD | `-35.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 333,160.00 USD | 0.00 USD | 1,330.00 USD | `-32.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 331,840.00 USD | 0.00 USD | 493.50 USD | `-31.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 331,340.00 USD | 0.00 USD | 100.98 USD | `-30.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 331,240.00 USD | 0.00 USD | 500.70 USD | `-30.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 330,740.00 USD | 0.00 USD | 4,160.00 USD | `-29.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 326,590.00 USD | 0.00 USD | 6,500.00 USD | `-28.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.21` | 320,080.00 USD | 0.00 USD | 906.18 USD | `-27.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.25` | 319,180.00 USD | 0.00 USD | 127.35 USD | `-27.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 319,050.00 USD | 0.00 USD | 864.38 USD | `-26.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 318,190.00 USD | 0.00 USD | 130.10 USD | `-24.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 318,060.00 USD | 0.00 USD | 4,340.00 USD | `-24.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 313,720.00 USD | 0.00 USD | 5,520.00 USD | `-22.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 308,190.00 USD | 0.00 USD | 203.67 USD | `-21.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 307,990.00 USD | 0.00 USD | 296.34 USD | `-21.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 307,690.00 USD | 0.00 USD | 921.19 USD | `-21.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 306,770.00 USD | 0.00 USD | 709.98 USD | `-19.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.91` | 306,060.00 USD | 0.00 USD | 4,630.00 USD | `-19.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 301,440.00 USD | 0.00 USD | 691.50 USD | `-19.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 300,740.00 USD | 0.00 USD | 262.44 USD | `-19.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 300,480.00 USD | 0.00 USD | 24,350.00 USD | `-18.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.04` | 276,130.00 USD | 0.00 USD | 653.69 USD | `-18.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.11` | 275,480.00 USD | 0.00 USD | 187.79 USD | `-17.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 275,290.00 USD | 0.00 USD | 6,790.00 USD | `-16.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 268,500.00 USD | 0.00 USD | 4,960.00 USD | `-16.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.21` | 263,540.00 USD | 0.00 USD | 7,210.00 USD | `-16.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 256,330.00 USD | 0.00 USD | 282.74 USD | `-15.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 256,050.00 USD | 0.00 USD | 603.44 USD | `-15.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 255,450.00 USD | 0.00 USD | 464.61 USD | `-15.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 254,980.00 USD | 0.00 USD | 2,090.00 USD | `-15.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 252,890.00 USD | 0.00 USD | 129.58 USD | `-14.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 252,760.00 USD | 0.00 USD | 114.65 USD | `-14.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.39` | 252,640.00 USD | 0.00 USD | 702.75 USD | `-14.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.41` | 251,940.00 USD | 0.00 USD | 4,630.00 USD | `-13.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 247,310.00 USD | 0.00 USD | 199.39 USD | `-13.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 247,110.00 USD | 0.00 USD | 6,270.00 USD | `-13.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 240,840.00 USD | 0.00 USD | 37,420.00 USD | `-12.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 203,420.00 USD | 0.00 USD | 2,120.00 USD | `-12.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 201,300.00 USD | 0.00 USD | 799.83 USD | `-12.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 200,500.00 USD | 0.00 USD | 820.44 USD | `-12.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 199,680.00 USD | 0.00 USD | 218.24 USD | `-11.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 199,460.00 USD | 0.00 USD | 113.78 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.61` | 199,340.00 USD | 0.00 USD | 152.10 USD | `-11.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 199,190.00 USD | 0.00 USD | 297.59 USD | `-11.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.68` | 198,900.00 USD | 0.00 USD | 528.88 USD | `-10.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 198,370.00 USD | 0.00 USD | 360.13 USD | `-10.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 198,010.00 USD | 0.00 USD | 578.04 USD | `-10.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 197,430.00 USD | 0.00 USD | 106.32 USD | `-9.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.79` | 197,320.00 USD | 0.00 USD | 424.05 USD | `-9.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 196,900.00 USD | 0.00 USD | 1,170.00 USD | `-9.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.82` | 195,730.00 USD | 0.00 USD | 3,940.00 USD | `-9.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.83` | 191,790.00 USD | 0.00 USD | 154.70 USD | `-9.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 191,630.00 USD | 0.00 USD | 115.23 USD | `-8.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 191,520.00 USD | 0.00 USD | 183.33 USD | `-8.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 191,330.00 USD | 0.00 USD | 1,890.00 USD | `-8.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 189,440.00 USD | 0.00 USD | 8,250.00 USD | `-8.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 181,190.00 USD | 0.00 USD | 5,710.00 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 175,480.00 USD | 0.00 USD | 1,590.00 USD | `-7.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 173,900.00 USD | 0.00 USD | 898.42 USD | `-7.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 173,000.00 USD | 0.00 USD | 7,960.00 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 165,040.00 USD | 0.00 USD | 246.52 USD | `-7.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.97` | 164,800.00 USD | 0.00 USD | 2,420.00 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 162,370.00 USD | 0.00 USD | 1,440.00 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 160,940.00 USD | 0.00 USD | 435.73 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 160,500.00 USD | 0.00 USD | 4,320.00 USD | `-6.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 156,180.00 USD | 0.00 USD | 123.58 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 156,060.00 USD | 0.00 USD | 796.62 USD | `-6.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 155,260.00 USD | 0.00 USD | 152.56 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.06` | 155,110.00 USD | 0.00 USD | 2,730.00 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 152,380.00 USD | 0.00 USD | 121.69 USD | `-6.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.09` | 152,260.00 USD | 0.00 USD | 5,230.00 USD | `-6.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 147,030.00 USD | 0.00 USD | 477.36 USD | `-5.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 146,550.00 USD | 0.00 USD | 16,210.00 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 130,340.00 USD | 0.00 USD | 744.88 USD | `-5.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 129,590.00 USD | 0.00 USD | 6,500.00 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 123,090.00 USD | 0.00 USD | 884.60 USD | `-5.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 122,210.00 USD | 0.00 USD | 5,550.00 USD | `-5.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 116,660.00 USD | 0.00 USD | 121.51 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 116,530.00 USD | 0.00 USD | 3,080.00 USD | `-5.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 113,450.00 USD | 0.00 USD | 520.75 USD | `-4.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 112,930.00 USD | 0.00 USD | 3,020.00 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 109,910.00 USD | 0.00 USD | 141.04 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 109,770.00 USD | 0.00 USD | 22,560.00 USD | `-4.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 87,200.00 USD | 0.00 USD | 515.66 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.22` | 86,690.00 USD | 0.00 USD | 3,020.00 USD | `-4.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 83,660.00 USD | 0.00 USD | 490.15 USD | `-4.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.24` | 83,170.00 USD | 0.00 USD | 197.96 USD | `-4.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.26` | 82,980.00 USD | 0.00 USD | 9,640.00 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.27` | 73,340.00 USD | 0.00 USD | 535.65 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 72,800.00 USD | 0.00 USD | 734.99 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 72,070.00 USD | 0.00 USD | 828.50 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 71,240.00 USD | 0.00 USD | 311.97 USD | `-3.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 70,930.00 USD | 0.00 USD | 5,380.00 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 65,550.00 USD | 0.00 USD | 245.13 USD | `-3.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.32` | 65,310.00 USD | 0.00 USD | 1,690.00 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 63,610.00 USD | 0.00 USD | 5,400.00 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 58,220.00 USD | 0.00 USD | 808.63 USD | `-2.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 57,410.00 USD | 0.00 USD | 4,070.00 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.37` | 53,340.00 USD | 0.00 USD | 24,090.00 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 29,250.00 USD | 0.00 USD | 1,140.00 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 28,110.00 USD | 0.00 USD | 419.25 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 27,690.00 USD | 0.00 USD | 376.68 USD | `-2.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 27,310.00 USD | 0.00 USD | 6,230.00 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 21,080.00 USD | 0.00 USD | 314.81 USD | `-2.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 20,770.00 USD | 0.00 USD | 198.83 USD | `-2.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 20,570.00 USD | 0.00 USD | 195.52 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 20,370.00 USD | 0.00 USD | 138.24 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 20,230.00 USD | 0.00 USD | 710.81 USD | `-1.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 19,520.00 USD | 0.00 USD | 769.61 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.48` | 18,750.00 USD | 0.00 USD | 777.14 USD | `-1.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.49` | 17,970.00 USD | 0.00 USD | 408.78 USD | `-1.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.51` | 17,570.00 USD | 0.00 USD | 122.47 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.52` | 17,440.00 USD | 0.00 USD | 1,720.00 USD | `-1.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.53` | 15,720.00 USD | 0.00 USD | 123.27 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 15,600.00 USD | 0.00 USD | 2,170.00 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 13,430.00 USD | 0.00 USD | 123.56 USD | `-0.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 13,310.00 USD | 0.00 USD | 9,990.00 USD | `-0.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.56` | 3,320.00 USD | 0.00 USD | 2,490.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.57` | 834.12 USD | 0.00 USD | 566.55 USD | `-0.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.59` | 267.57 USD | 0.00 USD | 143.28 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.60` | 124.28 USD | 0.00 USD | 124.28 USD | `-0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 102.14 USD | 102.14 USD | 0.00 USD | `+0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 226.71 USD | 124.57 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 355.23 USD | 128.51 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 1,090.00 USD | 733.98 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 3,380.00 USD | 2,290.00 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 3,840.00 USD | 459.41 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 4,040.00 USD | 200.85 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 4,210.00 USD | 176.62 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 7,260.00 USD | 3,050.00 USD | 0.00 USD | `+0.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 7,670.00 USD | 410.49 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 9,210.00 USD | 1,540.00 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 9,610.00 USD | 399.67 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 10,040.00 USD | 421.85 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 10,280.00 USD | 239.51 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 14,650.00 USD | 4,370.00 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 18,390.00 USD | 3,740.00 USD | 0.00 USD | `+1.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 18,560.00 USD | 173.28 USD | 0.00 USD | `+1.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 18,780.00 USD | 215.16 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 19,170.00 USD | 388.12 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 19,880.00 USD | 711.78 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 20,440.00 USD | 563.87 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 20,690.00 USD | 243.40 USD | 0.00 USD | `+2.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 20,850.00 USD | 168.05 USD | 0.00 USD | `+2.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 21,190.00 USD | 339.94 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 21,510.00 USD | 310.98 USD | 0.00 USD | `+3.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 21,620.00 USD | 110.58 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 22,480.00 USD | 860.96 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 24,410.00 USD | 1,930.00 USD | 0.00 USD | `+3.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 25,200.00 USD | 788.72 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 27,000.00 USD | 1,800.00 USD | 0.00 USD | `+3.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 27,170.00 USD | 163.33 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 27,950.00 USD | 782.17 USD | 0.00 USD | `+3.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 28,170.00 USD | 223.62 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 565,480.00 USD | 537,310.00 USD | 0.00 USD | `+4.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 565,880.00 USD | 401.63 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 881,030.00 USD | 315,150.00 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 881,220.00 USD | 186.53 USD | 0.00 USD | `+4.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 881,560.00 USD | 338.30 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 881,820.00 USD | 260.96 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 882,040.00 USD | 220.06 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 883,130.00 USD | 1,090.00 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 883,740.00 USD | 616.37 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 883,850.00 USD | 102.03 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 884,300.00 USD | 453.84 USD | 0.00 USD | `+5.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 884,460.00 USD | 160.99 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 884,680.00 USD | 215.98 USD | 0.00 USD | `+5.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 886,190.00 USD | 1,510.00 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 886,640.00 USD | 451.48 USD | 0.00 USD | `+5.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 886,780.00 USD | 139.58 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 888,070.00 USD | 1,290.00 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 888,230.00 USD | 166.53 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 890,230.00 USD | 2,000.00 USD | 0.00 USD | `+6.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 1,280,000.00 USD | 394,210.00 USD | 0.00 USD | `+6.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,280,000.00 USD | 119.24 USD | 0.00 USD | `+6.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,290,000.00 USD | 3,020.00 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,290,000.00 USD | 131.87 USD | 0.00 USD | `+7.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,290,000.00 USD | 149.17 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,290,000.00 USD | 2,220.00 USD | 0.00 USD | `+7.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,520,000.00 USD | 231,380.00 USD | 0.00 USD | `+7.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,520,000.00 USD | 1,960.00 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,520,000.00 USD | 434.45 USD | 0.00 USD | `+8.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,540,000.00 USD | 18,610.00 USD | 0.00 USD | `+8.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,540,000.00 USD | 166.83 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,540,000.00 USD | 674.29 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,540,000.00 USD | 101.58 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,540,000.00 USD | 109.36 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,540,000.00 USD | 116.69 USD | 0.00 USD | `+8.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,540,000.00 USD | 163.41 USD | 0.00 USD | `+8.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,540,000.00 USD | 102.01 USD | 0.00 USD | `+9.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,540,000.00 USD | 102.12 USD | 0.00 USD | `+9.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,540,000.00 USD | 714.59 USD | 0.00 USD | `+9.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,550,000.00 USD | 928.13 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,550,000.00 USD | 102.45 USD | 0.00 USD | `+9.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,550,000.00 USD | 219.84 USD | 0.00 USD | `+9.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,550,000.00 USD | 311.69 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,550,000.00 USD | 1,890.00 USD | 0.00 USD | `+9.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,550,000.00 USD | 1,130.00 USD | 0.00 USD | `+10.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,550,000.00 USD | 288.46 USD | 0.00 USD | `+10.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,550,000.00 USD | 119.92 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,550,000.00 USD | 231.00 USD | 0.00 USD | `+11.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,550,000.00 USD | 221.07 USD | 0.00 USD | `+11.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,550,000.00 USD | 992.00 USD | 0.00 USD | `+11.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,550,000.00 USD | 148.48 USD | 0.00 USD | `+12.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,550,000.00 USD | 191.36 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,560,000.00 USD | 4,440.00 USD | 0.00 USD | `+12.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,560,000.00 USD | 108.21 USD | 0.00 USD | `+12.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,560,000.00 USD | 169.68 USD | 0.00 USD | `+13.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,560,000.00 USD | 574.66 USD | 0.00 USD | `+13.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,560,000.00 USD | 121.87 USD | 0.00 USD | `+13.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,560,000.00 USD | 115.88 USD | 0.00 USD | `+14.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,560,000.00 USD | 340.05 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,560,000.00 USD | 742.12 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,560,000.00 USD | 899.47 USD | 0.00 USD | `+15.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,630,000.00 USD | 70,020.00 USD | 0.00 USD | `+15.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,630,000.00 USD | 373.97 USD | 0.00 USD | `+15.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,640,000.00 USD | 6,320.00 USD | 0.00 USD | `+16.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,640,000.00 USD | 6,370.00 USD | 0.00 USD | `+17.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,640,000.00 USD | 404.20 USD | 0.00 USD | `+17.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,850,000.00 USD | 210,980.00 USD | 0.00 USD | `+17.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,850,000.00 USD | 1,150.00 USD | 0.00 USD | `+17.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,850,000.00 USD | 172.16 USD | 0.00 USD | `+18.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,860,000.00 USD | 922.87 USD | 0.00 USD | `+19.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,860,000.00 USD | 489.40 USD | 0.00 USD | `+20.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,860,000.00 USD | 1,200.00 USD | 0.00 USD | `+20.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,860,000.00 USD | 118.01 USD | 0.00 USD | `+21.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.46` | 1,860,000.00 USD | 971.48 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.47` | 1,860,000.00 USD | 818.31 USD | 0.00 USD | `+21.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,860,000.00 USD | 312.31 USD | 0.00 USD | `+22.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,860,000.00 USD | 2,290.00 USD | 0.00 USD | `+22.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.53` | 1,860,000.00 USD | 1,890.00 USD | 0.00 USD | `+22.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,860,000.00 USD | 178.46 USD | 0.00 USD | `+23.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,860,000.00 USD | 173.42 USD | 0.00 USD | `+24.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,860,000.00 USD | 184.75 USD | 0.00 USD | `+24.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,860,000.00 USD | 135.78 USD | 0.00 USD | `+25.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,860,000.00 USD | 127.96 USD | 0.00 USD | `+25.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,870,000.00 USD | 476.43 USD | 0.00 USD | `+26.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,870,000.00 USD | 1,080.00 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,900,000.00 USD | 35,110.00 USD | 0.00 USD | `+26.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,900,000.00 USD | 251.06 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,900,000.00 USD | 552.44 USD | 0.00 USD | `+27.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,900,000.00 USD | 537.26 USD | 0.00 USD | `+27.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.11` | 1,900,000.00 USD | 1,110.00 USD | 0.00 USD | `+29.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,900,000.00 USD | 320.29 USD | 0.00 USD | `+29.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,910,000.00 USD | 1,100.00 USD | 0.00 USD | `+29.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,910,000.00 USD | 2,270.00 USD | 0.00 USD | `+30.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,910,000.00 USD | 1,270.00 USD | 0.00 USD | `+30.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,910,000.00 USD | 1,380.00 USD | 0.00 USD | `+32.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,910,000.00 USD | 2,410.00 USD | 0.00 USD | `+32.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,920,000.00 USD | 10,640.00 USD | 0.00 USD | `+33.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 1,930,000.00 USD | 2,050.00 USD | 0.00 USD | `+33.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,930,000.00 USD | 746.79 USD | 0.00 USD | `+33.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,930,000.00 USD | 7,700.00 USD | 0.00 USD | `+34.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,930,000.00 USD | 906.03 USD | 0.00 USD | `+37.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,930,000.00 USD | 434.61 USD | 0.00 USD | `+37.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,940,000.00 USD | 163.52 USD | 0.00 USD | `+38.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 1,950,000.00 USD | 10,370.00 USD | 0.00 USD | `+39.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.19` | 1,950,000.00 USD | 5,270.00 USD | 0.00 USD | `+41.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.28` | 1,950,000.00 USD | 115.02 USD | 0.00 USD | `+42.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 1,950,000.00 USD | 3,870.00 USD | 0.00 USD | `+47.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 1,950,000.00 USD | 197.97 USD | 0.00 USD | `+48.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 1,960,000.00 USD | 3,200.00 USD | 0.00 USD | `+50.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 1,960,000.00 USD | 179.58 USD | 0.00 USD | `+50.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 1,960,000.00 USD | 568.45 USD | 0.00 USD | `+51.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 1,960,000.00 USD | 169.57 USD | 0.00 USD | `+52.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 1,960,000.00 USD | 446.52 USD | 0.00 USD | `+55.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 1,960,000.00 USD | 5,320.00 USD | 0.00 USD | `+56.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,180,000.00 USD | 210,750.00 USD | 0.00 USD | `+57.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,180,000.00 USD | 407.95 USD | 0.00 USD | `+59.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,180,000.00 USD | 174.91 USD | 0.00 USD | `+60.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,180,000.00 USD | 5,070.00 USD | 0.00 USD | `+62.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,180,000.00 USD | 960.26 USD | 0.00 USD | `+65.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,180,000.00 USD | 2,710.00 USD | 0.00 USD | `+66.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,190,000.00 USD | 805.90 USD | 0.00 USD | `+68.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,190,000.00 USD | 655.55 USD | 0.00 USD | `+70.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,190,000.00 USD | 4,890.00 USD | 0.00 USD | `+71.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,190,000.00 USD | 471.09 USD | 0.00 USD | `+72.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,190,000.00 USD | 383.85 USD | 0.00 USD | `+73.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,850,000.00 USD | 653,420.00 USD | 0.00 USD | `+74.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 2,850,000.00 USD | 1,510.00 USD | 0.00 USD | `+75.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,850,000.00 USD | 111.87 USD | 0.00 USD | `+84.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,850,000.00 USD | 219.91 USD | 0.00 USD | `+86.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 2,850,000.00 USD | 121.74 USD | 0.00 USD | `+97.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.00` | 2,850,000.00 USD | 297.59 USD | 0.00 USD | `+97.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.20` | 2,970,000.00 USD | 120,270.00 USD | 0.00 USD | `+100.03%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.27` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 360.23 USD | 1,810.00 USD | 5,550.00 USD |
| `7D` | `7.31` | 7,160,000.00 USD | 0.00 USD | 7,160,000.00 USD | 0.00 USD | 0.00 USD | 104.04 USD |
| `7D` | `7.35` | 7,160,000.00 USD | 0.00 USD | 7,160,000.00 USD | 0.00 USD | 0.00 USD | 406.69 USD |
| `7D` | `7.37` | 7,160,000.00 USD | 0.00 USD | 7,160,000.00 USD | 45,620.00 USD | 0.00 USD | 457.98 USD |
| `7D` | `7.39` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 46,200.00 USD | 0.00 USD | 503.12 USD |
| `7D` | `7.45` | 7,060,000.00 USD | 0.00 USD | 7,060,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD |
| `7D` | `7.49` | 7,040,000.00 USD | 0.00 USD | 7,040,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD |
| `7D` | `7.51` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 2,070.00 USD | 0.00 USD | 18,280.00 USD |
| `7D` | `7.53` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 35,990.00 USD | 18,910.00 USD | 0.00 USD |
| `7D` | `7.55` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD |
| `1D` | `7.59` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 1,740.00 USD | 0.00 USD | 7,670.00 USD |
| `1D` | `7.60` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 706.40 USD | 4,900.00 USD | 351.13 USD |
| `1D` | `7.61` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 2,750.00 USD | 1,250.00 USD | 11,670.00 USD |
| `7D` | `7.61` | 6,920,000.00 USD | 0.00 USD | 6,920,000.00 USD | 626.55 USD | 0.00 USD | 301.55 USD |
| `1D` | `7.62` | 5,660,000.00 USD | 0.00 USD | 5,660,000.00 USD | 8,960.00 USD | 1,330.00 USD | 133.28 USD |
| `1D` | `7.63` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 5,940.00 USD | 0.00 USD | 9,660.00 USD |
| `7D` | `7.63` | 6,920,000.00 USD | 0.00 USD | 6,920,000.00 USD | 41,300.00 USD | 2,130.00 USD | 1,680.00 USD |
| `1D` | `7.64` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 33,010.00 USD | 812.96 USD | 2,390.00 USD |
| `1D` | `7.65` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 0.00 USD | 1,320.00 USD | 9,870.00 USD |
| `7D` | `7.65` | 6,870,000.00 USD | 0.00 USD | 6,870,000.00 USD | 4,870.00 USD | 2,350.00 USD | 0.00 USD |
| `1D` | `7.66` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 3,030.00 USD | 0.00 USD | 531.95 USD |
| `1D` | `7.67` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 1,410.00 USD | 1,110.00 USD | 1,790.00 USD |
| `7D` | `7.67` | 6,870,000.00 USD | 0.00 USD | 6,870,000.00 USD | 1,110.00 USD | 0.00 USD | 34,150.00 USD |
| `1D` | `7.68` | 5,580,000.00 USD | 0.00 USD | 5,580,000.00 USD | 892.30 USD | 0.00 USD | 5,300.00 USD |
| `1D` | `7.69` | 5,580,000.00 USD | 0.00 USD | 5,580,000.00 USD | 0.00 USD | 1,600.00 USD | 0.13 USD |
| `1D` | `7.70` | 5,580,000.00 USD | 0.00 USD | 5,580,000.00 USD | 4,140.00 USD | 3,380.00 USD | 16,770.00 USD |
| `1D` | `7.71` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 660.12 USD | 5,720.00 USD | 8,840.00 USD |
| `7D` | `7.71` | 6,830,000.00 USD | 0.00 USD | 6,830,000.00 USD | 393.33 USD | 1,650.00 USD | 39,010.00 USD |
| `1D` | `7.72` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 701.68 USD | 1,840.00 USD | 3,750.00 USD |
| `1D` | `7.73` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 4,120.00 USD | 1,240.00 USD | 5,600.00 USD |
| `7D` | `7.73` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 39,770.00 USD | 2,520.00 USD | 7,340.00 USD |
| `1D` | `7.74` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 16,520.00 USD | 0.00 USD | 184.39 USD |
| `1D` | `7.75` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 900.06 USD | 6,210.00 USD | 8,050.00 USD |
| `7D` | `7.75` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 29,320.00 USD | 13,360.00 USD | 10,360.00 USD |
| `1D` | `7.76` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 458.75 USD | 494.12 USD | 0.00 USD |
| `1D` | `7.77` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 13,020.00 USD | 689.91 USD | 3,430.00 USD |
| `7D` | `7.77` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 20,120.00 USD | 4,900.00 USD | 6,580.00 USD |
| `1D` | `7.78` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 2,730.00 USD | 6,250.00 USD | 0.00 USD |
| `1D` | `7.79` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 18,960.00 USD | 2,920.00 USD | 7,250.00 USD |
| `7D` | `7.79` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 70,950.00 USD | 7,170.00 USD | 23,040.00 USD |
| `1D` | `7.80` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 4,920.00 USD | 7,910.00 USD | 709.61 USD |
| `1D` | `7.81` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 349.70 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.81` | 6,560,000.00 USD | 0.00 USD | 6,560,000.00 USD | 3,970.00 USD | 11,570.00 USD | 1,770.00 USD |
| `1D` | `7.82` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 248.67 USD | 1,680.00 USD | 0.00 USD |
| `1D` | `7.83` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 27,230.00 USD | 5,360.00 USD | 0.00 USD |
| `7D` | `7.83` | 6,540,000.00 USD | 0.00 USD | 6,540,000.00 USD | 29,530.00 USD | 2,130.00 USD | 24,330.00 USD |
| `1D` | `7.84` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 978.04 USD | 1,240.00 USD | 0.00 USD |
| `1D` | `7.85` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 3,320.00 USD | 639.88 USD | 2,650.00 USD |
| `7D` | `7.85` | 6,480,000.00 USD | 0.00 USD | 6,480,000.00 USD | 17,330.00 USD | 7,840.00 USD | 13,000.00 USD |
| `1D` | `7.86` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 1,290.00 USD | 6,270.00 USD | 13,940.00 USD |
| `1D` | `7.87` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 10,980.00 USD | 10,860.00 USD | 22,910.00 USD |
| `7D` | `7.87` | 6,440,000.00 USD | 0.00 USD | 6,440,000.00 USD | 150,960.00 USD | 1,540.00 USD | 22,350.00 USD |
| `1D` | `7.88` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 158,960.00 USD | 4,280.00 USD | 33,710.00 USD |
| `1D` | `7.89` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 57,720.00 USD | 3,720.00 USD | 27,230.00 USD |
| `7D` | `7.89` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 150,040.00 USD | 18,320.00 USD | 24,270.00 USD |
| `1D` | `7.90` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 56,410.00 USD | 6,970.00 USD | 4,310.00 USD |
| `1D` | `7.91` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 11,200.00 USD | 10,370.00 USD | 26,070.00 USD |
| `7D` | `7.91` | 6,080,000.00 USD | 0.00 USD | 6,080,000.00 USD | 31,740.00 USD | 26,330.00 USD | 45,390.00 USD |
| `1D` | `7.92` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 15,830.00 USD | 2,040.00 USD | 4,800.00 USD |
| `1D` | `7.93` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,480.00 USD |
| `7D` | `7.93` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 78,470.00 USD | 7,330.00 USD | 14,550.00 USD |
| `1D` | `7.94` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 15,580.00 USD | 20,510.00 USD | 61,750.00 USD |
| `1D` | `7.95` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 28,200.00 USD | 9,190.00 USD | 86,980.00 USD |
| `7D` | `7.95` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 45,890.00 USD | 9,500.00 USD | 102,940.00 USD |
| `1D` | `7.96` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,330.00 USD |
| `1D` | `7.97` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD |
| `7D` | `7.97` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 37,150.00 USD | 18,700.00 USD | 40,570.00 USD |
| `1D` | `7.98` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 5,050.00 USD | 2,060.00 USD | 42,970.00 USD |
| `1D` | `7.99` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 3,450.00 USD | 10,180.00 USD | 4,660.00 USD |
| `7D` | `7.99` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 52,570.00 USD | 20,640.00 USD | 122,290.00 USD |
| `1D` | `8.00` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 50,430.00 USD | 8,950.00 USD | 21,810.00 USD |
| `1D` | `8.01` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 6,540.00 USD | 3,750.00 USD | 4,040.00 USD |
| `7D` | `8.01` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 47,380.00 USD | 17,990.00 USD | 46,600.00 USD |
| `1D` | `8.02` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 75,150.00 USD | 0.00 USD | 274.70 USD |
| `1D` | `8.03` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 9,070.00 USD | 12,540.00 USD | 12,890.00 USD |
| `7D` | `8.03` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 353,080.00 USD | 35,720.00 USD | 49,900.00 USD |
| `1D` | `8.04` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 49,540.00 USD | 0.00 USD | 10,010.00 USD |
| `1D` | `8.05` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 318,600.00 USD | 6,430.00 USD | 53,960.00 USD |
| `7D` | `8.05` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 390,130.00 USD | 0.00 USD | 63,560.00 USD |
| `1D` | `8.06` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 155,360.00 USD | 0.00 USD | 66,970.00 USD |
| `1D` | `8.07` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD |
| `7D` | `8.07` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 60,670.00 USD | 0.00 USD | 75,410.00 USD |
| `1D` | `8.08` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD |
| `1D` | `8.09` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 3,650.00 USD | 0.00 USD | 29,580.00 USD |
| `7D` | `8.09` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 32,760.00 USD | 0.00 USD | 81,280.00 USD |
| `1D` | `8.10` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD |
| `1D` | `8.11` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD |
| `7D` | `8.11` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 33,000.00 USD | 0.00 USD | 140,250.00 USD |
| `1D` | `8.12` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 19,930.00 USD | 11,230.00 USD | 126,250.00 USD |
| `1D` | `8.13` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 34,890.00 USD | 9,180.00 USD | 1,710.00 USD |
| `7D` | `8.13` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 47,290.00 USD | 12,740.00 USD | 20,490.00 USD |
| `1D` | `8.14` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 17,740.00 USD | 8,630.00 USD | 105,270.00 USD |
| `1D` | `8.15` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 47,020.00 USD | 12,240.00 USD | 53,660.00 USD |
| `7D` | `8.15` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 179,060.00 USD | 31,560.00 USD | 183,290.00 USD |
| `1D` | `8.16` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 192.50 USD | 22,250.00 USD | 165,460.00 USD |
| `1D` | `8.17` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 11,100.00 USD | 9,120.00 USD | 183,140.00 USD |
| `7D` | `8.17` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,590.00 USD | 13,650.00 USD | 149,580.00 USD |
| `1D` | `8.18` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 7,140.00 USD | 3,280.00 USD | 4,190.00 USD |
| `1D` | `8.19` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 18,260.00 USD | 545.08 USD | 19,120.00 USD |
| `7D` | `8.19` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 1,200.00 USD | 72,340.00 USD | 23,200.00 USD |
| `1D` | `8.20` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 25,900.00 USD | 4,000.00 USD | 11,560.00 USD |
| `1D` | `8.21` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 41,620.00 USD | 2,210.00 USD | 0.00 USD |
| `7D` | `8.21` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 174,220.00 USD | 22,240.00 USD | 0.00 USD |
| `1D` | `8.22` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 3,620.00 USD | 1,530.00 USD | 16,310.00 USD |
| `1D` | `8.23` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 0.00 USD | 3,450.00 USD | 5,970.00 USD |
| `7D` | `8.23` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 0.00 USD | 40,910.00 USD | 14,520.00 USD |
| `1D` | `8.24` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 168.44 USD | 6,390.00 USD | 9,270.00 USD |
| `1D` | `8.25` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 0.00 USD | 5,000.00 USD | 38,170.00 USD |
| `7D` | `8.25` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 129,050.00 USD | 12,050.00 USD | 17,610.00 USD |
| `1D` | `8.26` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 50,590.00 USD | 12,510.00 USD | 25,360.00 USD |
| `1D` | `8.27` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 13,860.00 USD | 12,270.00 USD | 20,120.00 USD |
| `7D` | `8.27` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 103,730.00 USD | 4,000.00 USD | 37,940.00 USD |
| `1D` | `8.28` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 0.00 USD | 13,760.00 USD | 4,240.00 USD |
| `1D` | `8.29` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 39,480.00 USD | 11,800.00 USD | 0.00 USD |
| `7D` | `8.29` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 166,800.00 USD | 6,550.00 USD | 21,950.00 USD |
| `1D` | `8.30` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 69,220.00 USD | 13,810.00 USD | 20,060.00 USD |
| `1D` | `8.31` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 82,900.00 USD | 11,920.00 USD | 56,400.00 USD |
| `7D` | `8.31` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 370,260.00 USD | 10,660.00 USD | 2,790.00 USD |
| `1D` | `8.32` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 80,060.00 USD | 6,080.00 USD | 14,060.00 USD |
| `1D` | `8.33` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 0.00 USD | 8,710.00 USD | 109.14 USD |
| `7D` | `8.33` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 14,600.00 USD | 11,770.00 USD | 4,900.00 USD |
| `1D` | `8.34` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 0.00 USD | 3,230.00 USD | 13.84 USD |
| `1D` | `8.35` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 23,440.00 USD | 25,350.00 USD |
| `7D` | `8.35` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 223,170.00 USD | 0.00 USD | 5,720.00 USD |
| `1D` | `8.36` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 0.00 USD | 1,090.00 USD | 25,130.00 USD |
| `1D` | `8.37` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 691.75 USD | 14,420.00 USD | 16.86 USD |
| `7D` | `8.37` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 36,530.00 USD |
| `1D` | `8.38` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 17,220.00 USD | 7,830.00 USD | 50,290.00 USD |
| `1D` | `8.39` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 107,990.00 USD | 16,670.00 USD | 32,610.00 USD |
| `7D` | `8.39` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 0.00 USD | 15,860.00 USD | 68,640.00 USD |
| `1D` | `8.40` | 950,050.00 USD | 0.00 USD | 950,050.00 USD | 10,500.00 USD | 10,400.00 USD | 63,770.00 USD |
| `1D` | `8.41` | 865,370.00 USD | 0.00 USD | 865,370.00 USD | 0.00 USD | 12,780.00 USD | 18,540.00 USD |
| `7D` | `8.41` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 194,850.00 USD | 0.00 USD | 118,070.00 USD |
| `1D` | `8.42` | 834,050.00 USD | 0.00 USD | 834,050.00 USD | 0.00 USD | 16,260.00 USD | 42,890.00 USD |
| `1D` | `8.43` | 774,900.00 USD | 0.00 USD | 774,900.00 USD | 81,350.00 USD | 7,730.00 USD | 11,670.00 USD |
| `7D` | `8.43` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 163,340.00 USD | 12,610.00 USD | 22,840.00 USD |
| `1D` | `8.44` | 674,160.00 USD | 0.00 USD | 674,160.00 USD | 11,130.00 USD | 32,380.00 USD | 160,460.00 USD |
| `1D` | `8.45` | 470,180.00 USD | 0.00 USD | 470,180.00 USD | 54,790.00 USD | 5,970.00 USD | 0.00 USD |
| `7D` | `8.45` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 156,410.00 USD | 8,000.00 USD | 171,560.00 USD |
| `1D` | `8.47` | 409,420.00 USD | 0.00 USD | 409,420.00 USD | 663.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.47` | 894,220.00 USD | 0.00 USD | 894,220.00 USD | 0.00 USD | 0.00 USD | 38,730.00 USD |
| `1D` | `8.48` | 408,760.00 USD | 0.00 USD | 408,760.00 USD | 749.80 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.49` | 408,010.00 USD | 0.00 USD | 408,010.00 USD | 0.00 USD | 0.00 USD | 12.70 USD |
| `7D` | `8.49` | 855,480.00 USD | 0.00 USD | 855,480.00 USD | 0.00 USD | 0.00 USD | 153,260.00 USD |
| `7D` | `8.51` | 702,220.00 USD | 0.00 USD | 702,220.00 USD | 0.00 USD | 0.00 USD | 92,390.00 USD |
| `1D` | `8.52` | 408,000.00 USD | 0.00 USD | 408,000.00 USD | 158,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.53` | 249,360.00 USD | 0.00 USD | 249,360.00 USD | 24,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.53` | 609,830.00 USD | 0.00 USD | 609,830.00 USD | 173,370.00 USD | 0.00 USD | 1,390.00 USD |
| `1D` | `8.54` | 225,180.00 USD | 0.00 USD | 225,180.00 USD | 198,250.00 USD | 0.00 USD | 156.94 USD |
| `1D` | `8.55` | 26,780.00 USD | 0.00 USD | 26,780.00 USD | 1,650.00 USD | 0.00 USD | 25,120.00 USD |
| `7D` | `8.55` | 435,070.00 USD | 0.00 USD | 435,070.00 USD | 434,770.00 USD | 0.00 USD | 300.56 USD |
| `1D` | `8.56` | 686.73 USD | 686.73 USD | 0.00 USD | 686.73 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.56` | 1,370.00 USD | 1,370.00 USD | 0.00 USD | 686.73 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.56` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.57` | 148,380.00 USD | 148,380.00 USD | 0.00 USD | 147,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.57` | 9,740.00 USD | 9,740.00 USD | 0.00 USD | 9,740.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.58` | 207,500.00 USD | 207,500.00 USD | 0.00 USD | 59,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.59` | 10,780.00 USD | 10,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD |
| `1D` | `8.60` | 209,540.00 USD | 209,540.00 USD | 0.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.61` | 210,730.00 USD | 210,730.00 USD | 0.00 USD | 497.00 USD | 0.00 USD | 699.64 USD |
| `7D` | `8.61` | 13,870.00 USD | 13,870.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 271.28 USD |
| `1D` | `8.62` | 378,000.00 USD | 378,000.00 USD | 0.00 USD | 41,980.00 USD | 0.00 USD | 125,290.00 USD |
| `1D` | `8.63` | 509,710.00 USD | 509,710.00 USD | 0.00 USD | 129,280.00 USD | 2,420.00 USD | 0.00 USD |
| `7D` | `8.63` | 42,380.00 USD | 42,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,520.00 USD |
| `1D` | `8.64` | 591,680.00 USD | 591,680.00 USD | 0.00 USD | 69,220.00 USD | 9,340.00 USD | 3,410.00 USD |
| `1D` | `8.65` | 653,790.00 USD | 653,790.00 USD | 0.00 USD | 35,830.00 USD | 9,010.00 USD | 17,260.00 USD |
| `7D` | `8.65` | 93,300.00 USD | 93,300.00 USD | 0.00 USD | 40,260.00 USD | 10,660.00 USD | 0.00 USD |
| `1D` | `8.66` | 683,090.00 USD | 683,090.00 USD | 0.00 USD | 13,240.00 USD | 2,020.00 USD | 14,040.00 USD |
| `1D` | `8.67` | 696,490.00 USD | 696,490.00 USD | 0.00 USD | 880.60 USD | 12,460.00 USD | 56.72 USD |
| `7D` | `8.67` | 106,630.00 USD | 106,630.00 USD | 0.00 USD | 0.00 USD | 11,770.00 USD | 1,570.00 USD |
| `1D` | `8.68` | 736,010.00 USD | 736,010.00 USD | 0.00 USD | 588.00 USD | 13,040.00 USD | 25,890.00 USD |
| `1D` | `8.69` | 811,870.00 USD | 811,870.00 USD | 0.00 USD | 10,820.00 USD | 22,830.00 USD | 42,210.00 USD |
| `7D` | `8.69` | 347,640.00 USD | 347,640.00 USD | 0.00 USD | 29,260.00 USD | 48,960.00 USD | 162,790.00 USD |
| `1D` | `8.70` | 906,390.00 USD | 906,390.00 USD | 0.00 USD | 62,600.00 USD | 1,090.00 USD | 30,830.00 USD |
| `1D` | `8.71` | 933,080.00 USD | 933,080.00 USD | 0.00 USD | 18,700.00 USD | 7,990.00 USD | 0.00 USD |
| `7D` | `8.71` | 445,870.00 USD | 445,870.00 USD | 0.00 USD | 87,110.00 USD | 11,120.00 USD | 0.00 USD |
| `1D` | `8.72` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 34,050.00 USD | 4,410.00 USD | 50,790.00 USD |
| `1D` | `8.73` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 19,820.00 USD | 31,860.00 USD | 32,610.00 USD |
| `7D` | `8.73` | 517,230.00 USD | 517,230.00 USD | 0.00 USD | 51,030.00 USD | 19,040.00 USD | 1,300.00 USD |
| `1D` | `8.74` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 38,500.00 USD | 6,910.00 USD | 24,770.00 USD |
| `1D` | `8.75` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 33,520.00 USD | 15,310.00 USD | 23,520.00 USD |
| `7D` | `8.75` | 798,150.00 USD | 798,150.00 USD | 0.00 USD | 196,960.00 USD | 19,690.00 USD | 64,270.00 USD |
| `1D` | `8.76` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 82,470.00 USD | 10,010.00 USD | 57,030.00 USD |
| `1D` | `8.77` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 155,740.00 USD | 2,060.00 USD | 47,150.00 USD |
| `7D` | `8.77` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 141,710.00 USD | 12,610.00 USD | 105,410.00 USD |
| `1D` | `8.78` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 41,500.00 USD | 25,510.00 USD | 50,110.00 USD |
| `1D` | `8.79` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 31,710.00 USD | 17,970.00 USD | 31,130.00 USD |
| `7D` | `8.79` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 29,660.00 USD | 33,300.00 USD | 65,190.00 USD |
| `1D` | `8.80` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 113,160.00 USD | 19,150.00 USD | 23,840.00 USD |
| `1D` | `8.81` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 53,290.00 USD | 9,030.00 USD | 1,750.00 USD |
| `7D` | `8.81` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 122,920.00 USD | 26,890.00 USD | 58,050.00 USD |
| `1D` | `8.82` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 19,950.00 USD | 4,510.00 USD | 61,490.00 USD |
| `1D` | `8.83` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 174,730.00 USD | 19,400.00 USD | 7,020.00 USD |
| `7D` | `8.83` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 242,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.84` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 1,500.00 USD | 4,360.00 USD | 59,130.00 USD |
| `1D` | `8.85` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 13,040.00 USD | 3,870.00 USD | 11,200.00 USD |
| `7D` | `8.85` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 29,310.00 USD | 5,880.00 USD | 58,190.00 USD |
| `1D` | `8.86` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 2,060.00 USD | 3,280.00 USD | 4,790.00 USD |
| `1D` | `8.87` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 1,410.00 USD | 545.08 USD | 12,570.00 USD |
| `7D` | `8.87` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD |
| `1D` | `8.88` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 803.70 USD | 14,670.00 USD | 186.36 USD |
| `1D` | `8.89` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 13,040.00 USD | 4,360.00 USD | 32,950.00 USD |
| `7D` | `8.89` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD | 73,830.00 USD |
| `1D` | `8.90` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 32,320.00 USD | 7,510.00 USD | 65,160.00 USD |
| `1D` | `8.91` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 32,240.00 USD | 13,320.00 USD | 19,460.00 USD |
| `7D` | `8.91` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 2,440.00 USD | 4,130.00 USD | 103,140.00 USD |
| `1D` | `8.92` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 1,110.00 USD | 6,390.00 USD | 9,340.00 USD |
| `1D` | `8.93` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 31,830.00 USD | 6,810.00 USD | 38,940.00 USD |
| `7D` | `8.93` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 157,480.00 USD | 6,300.00 USD | 17,610.00 USD |
| `1D` | `8.94` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 50,590.00 USD | 12,260.00 USD | 5,830.00 USD |
| `1D` | `8.95` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 3,080.00 USD | 6,630.00 USD | 20,340.00 USD |
| `7D` | `8.95` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 74,920.00 USD | 4,000.00 USD | 38,550.00 USD |
| `1D` | `8.96` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 1,260.00 USD | 2,980.00 USD | 175.90 USD |
| `1D` | `8.97` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.26 USD |
| `7D` | `8.97` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.98` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 35,320.00 USD | 9,420.00 USD | 19,670.00 USD |
| `1D` | `8.99` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 48,380.00 USD | 22,110.00 USD | 3,420.00 USD |
| `7D` | `8.99` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 145,880.00 USD | 6,550.00 USD | 29,050.00 USD |
| `1D` | `9.00` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 36,960.00 USD | 0.00 USD | 24,750.00 USD |
| `1D` | `9.01` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 49,510.00 USD | 14,940.00 USD | 16,240.00 USD |
| `7D` | `9.01` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 303,030.00 USD | 36,180.00 USD | 23,020.00 USD |
| `1D` | `9.02` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 39,170.00 USD | 29,440.00 USD | 5,010.00 USD |
| `1D` | `9.03` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 125,760.00 USD | 10,300.00 USD | 34,410.00 USD |
| `7D` | `9.03` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 107,490.00 USD | 101,140.00 USD | 15,640.00 USD |
| `1D` | `9.04` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 41,710.00 USD | 5,900.00 USD | 14,800.00 USD |
| `1D` | `9.05` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 21,980.00 USD | 7,560.00 USD | 22,410.00 USD |
| `7D` | `9.05` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 38,740.00 USD | 17,700.00 USD | 39,710.00 USD |
| `1D` | `9.06` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 28,180.00 USD | 5,480.00 USD | 10,490.00 USD |
| `1D` | `9.07` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 13,070.00 USD | 15,350.00 USD | 25,460.00 USD |
| `7D` | `9.07` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 3,990.00 USD | 14,140.00 USD | 36,530.00 USD |
| `1D` | `9.08` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 12,960.00 USD | 1,040.00 USD | 24,280.00 USD |
| `1D` | `9.09` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 71,230.00 USD | 9,730.00 USD | 25,300.00 USD |
| `7D` | `9.09` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 152,640.00 USD | 8,680.00 USD | 144,360.00 USD |
| `1D` | `9.10` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 16,320.00 USD | 10,640.00 USD | 30,930.00 USD |
| `1D` | `9.11` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 51,080.00 USD | 14,420.00 USD | 82,390.00 USD |
| `7D` | `9.11` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 877,120.00 USD | 37,620.00 USD | 570,050.00 USD |
| `1D` | `9.12` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 94,400.00 USD | 21,650.00 USD | 26,360.00 USD |
| `1D` | `9.13` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 75,260.00 USD | 15,960.00 USD | 35,980.00 USD |
| `7D` | `9.13` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 666,880.00 USD | 26,540.00 USD | 484,710.00 USD |
| `1D` | `9.14` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 20,200.00 USD | 0.00 USD | 24,040.00 USD |
| `1D` | `9.15` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 56,980.00 USD | 20,890.00 USD | 13,120.00 USD |
| `7D` | `9.15` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 357,020.00 USD | 38,700.00 USD | 270,200.00 USD |
| `1D` | `9.16` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 63,930.00 USD | 23,900.00 USD | 32,470.00 USD |
| `1D` | `9.17` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 74,820.00 USD | 3,200.00 USD | 49,540.00 USD |
| `7D` | `9.17` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 409,650.00 USD | 133,490.00 USD | 303,370.00 USD |
| `1D` | `9.18` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 28,310.00 USD | 26,430.00 USD | 31,220.00 USD |
| `1D` | `9.19` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 77,890.00 USD | 29,140.00 USD | 7,680.00 USD |
| `7D` | `9.19` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 504,150.00 USD | 108,440.00 USD | 193,800.00 USD |
| `1D` | `9.20` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 64,910.00 USD | 11,090.00 USD | 37,460.00 USD |
| `1D` | `9.21` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 30,000.00 USD | 2,950.00 USD | 4,760.00 USD |
| `7D` | `9.21` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 590,780.00 USD | 144,470.00 USD | 277,570.00 USD |
| `1D` | `9.22` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 58,060.00 USD | 2,850.00 USD | 11,100.00 USD |
| `1D` | `9.23` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 471.32 USD | 4,270.00 USD | 17.80 USD |
| `7D` | `9.23` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 582,450.00 USD | 92,780.00 USD | 331,960.00 USD |
| `1D` | `9.24` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 45,580.00 USD | 0.00 USD | 3,020.00 USD |
| `1D` | `9.25` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 17,240.00 USD | 5,840.00 USD | 9,510.00 USD |
| `7D` | `9.25` | 10,870,000.00 USD | 10,870,000.00 USD | 0.00 USD | 277,290.00 USD | 61,940.00 USD | 61,110.00 USD |
| `1D` | `9.26` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 574.60 USD | 0.00 USD | 3,540.00 USD |
| `1D` | `9.27` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 23,430.00 USD | 1,360.00 USD | 6,640.00 USD |
| `7D` | `9.27` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 156,190.00 USD | 102,670.00 USD | 37,770.00 USD |
| `1D` | `9.28` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 1,610.00 USD | 8,760.00 USD | 169.17 USD |
| `1D` | `9.29` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 16,070.00 USD | 4,140.00 USD | 17,910.00 USD |
| `7D` | `9.29` | 11,880,000.00 USD | 11,880,000.00 USD | 0.00 USD | 392,980.00 USD | 82,050.00 USD | 244,470.00 USD |
| `1D` | `9.30` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 39,880.00 USD | 7,520.00 USD | 11,600.00 USD |
| `1D` | `9.31` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 28,930.00 USD | 5,500.00 USD | 12,920.00 USD |
| `7D` | `9.31` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 308,150.00 USD | 44,500.00 USD | 209,900.00 USD |
| `1D` | `9.32` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 17,660.00 USD | 1,330.00 USD | 5,070.00 USD |
| `1D` | `9.33` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 12,710.00 USD | 6,000.00 USD | 9,780.00 USD |
| `7D` | `9.33` | 12,690,000.00 USD | 12,690,000.00 USD | 0.00 USD | 134,040.00 USD | 29,420.00 USD | 82,320.00 USD |
| `1D` | `9.34` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 46,100.00 USD | 3,660.00 USD | 5,580.00 USD |
| `1D` | `9.35` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 13,620.00 USD | 1,320.00 USD | 14,910.00 USD |
| `7D` | `9.35` | 12,970,000.00 USD | 12,970,000.00 USD | 0.00 USD | 114,090.00 USD | 67,130.00 USD | 96,310.00 USD |
| `1D` | `9.36` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 4,730.00 USD | 6,760.00 USD | 8,030.00 USD |
| `1D` | `9.37` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 12,860.00 USD | 6,780.00 USD | 4,400.00 USD |
| `7D` | `9.37` | 13,300,000.00 USD | 13,300,000.00 USD | 0.00 USD | 211,790.00 USD | 34,660.00 USD | 85,580.00 USD |
| `1D` | `9.38` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 15,290.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `9.39` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 8,850.00 USD | 1,600.00 USD | 12.83 USD |
| `7D` | `9.39` | 13,630,000.00 USD | 13,630,000.00 USD | 0.00 USD | 206,980.00 USD | 32,960.00 USD | 87,830.00 USD |
| `1D` | `9.40` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 22,270.00 USD | 0.00 USD | 12.64 USD |
| `1D` | `9.41` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 4,410.00 USD | 378.69 USD | 10,140.00 USD |
| `7D` | `9.41` | 14,020,000.00 USD | 14,020,000.00 USD | 0.00 USD | 265,720.00 USD | 30,790.00 USD | 99,880.00 USD |
| `1D` | `9.42` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 9,240.00 USD | 3,010.00 USD | 6,520.00 USD |
| `1D` | `9.43` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 5,380.00 USD | 1,380.00 USD | 1,460.00 USD |
| `7D` | `9.43` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 33,890.00 USD | 15,080.00 USD | 48,300.00 USD |
| `1D` | `9.44` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 795.69 USD | 1,840.00 USD | 3,750.00 USD |
| `1D` | `9.45` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 96.25 USD | 1,240.00 USD | 5,600.00 USD |
| `7D` | `9.45` | 14,210,000.00 USD | 14,210,000.00 USD | 0.00 USD | 68,680.00 USD | 11,560.00 USD | 8,600.00 USD |
| `1D` | `9.46` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 16,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.47` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 1,180.00 USD | 1,900.00 USD | 8,050.00 USD |
| `7D` | `9.47` | 14,270,000.00 USD | 14,270,000.00 USD | 0.00 USD | 44,170.00 USD | 5,760.00 USD | 12,750.00 USD |
| `1D` | `9.48` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 494.12 USD | 0.00 USD |
| `1D` | `9.49` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 9,740.00 USD | 689.91 USD | 3,380.00 USD |
| `7D` | `9.49` | 14,310,000.00 USD | 14,310,000.00 USD | 0.00 USD | 25,360.00 USD | 4,900.00 USD | 6,210.00 USD |
| `7D` | `9.51` | 14,400,000.00 USD | 14,400,000.00 USD | 0.00 USD | 57,130.00 USD | 7,150.00 USD | 25,660.00 USD |
| `7D` | `9.53` | 14,460,000.00 USD | 14,460,000.00 USD | 0.00 USD | 50,200.00 USD | 9,410.00 USD | 1,270.00 USD |
| `7D` | `9.55` | 14,490,000.00 USD | 14,490,000.00 USD | 0.00 USD | 11,560.00 USD | 11,570.00 USD | 880.26 USD |
| `7D` | `9.57` | 14,540,000.00 USD | 14,540,000.00 USD | 0.00 USD | 31,530.00 USD | 2,130.00 USD | 24,130.00 USD |
| `7D` | `9.59` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 14,070.00 USD | 7,840.00 USD | 14,300.00 USD |
| `7D` | `9.61` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 37,000.00 USD | 0.00 USD | 11,290.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `355.76M` | Total OI Tokens: `41,474,143.1 AVAX`
  * 1h OI Change: `+1.06%` | 4h OI Change: `-0.49%` | 24h OI Change: `-6.07%`
  * Exchange Breakdown: Binance=`80.66M` | Bybit=`57.58M` | OKX=`11.62M` | Hyperliquid=`16.96M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `11.15K` | Last 24h: `16.67K` | Last 3d: `66.43K` | Last 7d: `105.12K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0086%` |
| **USDT Bybit** | `0.0047%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0098%` | **USDT Bitget** | `0.0031%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `44.80%` | `55.20%` | `0.81` | 10,480,000.00 USD |
| `15M` | `Binance` | `39.78%` | `60.22%` | `0.66` | 4,120,000.00 USD |
| `15M` | `OKX` | `47.8%` | `52.2%` | `0.92` | 793,290.00 USD |
| `15M` | `Bybit` | `45.51%` | `54.49%` | `0.84` | 1,700,000.00 USD |
| `15M` | `KuCoin` | `48.7%` | `51.3%` | `0.95` | 208,910.00 USD |
| `15M` | `Gate` | `39.45%` | `60.55%` | `0.65` | 283,190.00 USD |
| `15M` | `Bitget` | `71.1%` | `28.9%` | `2.46` | 553,650.00 USD |
| `15M` | `BingX` | `44.79%` | `55.21%` | `0.81` | 118,010.00 USD |
| `15M` | `MEXC` | `44.74%` | `55.26%` | `0.81` | 123,930.00 USD |
| `15M` | `Bitunix` | `63.29%` | `36.71%` | `1.72` | 246,310.00 USD |
| `15M` | `Hyperliquid` | `50.81%` | `49.19%` | `1.03` | 138,180.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.71%` | `50.29%` | `0.99` | 115,600.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `40.91%` | `59.09%` | `0.69` | 1,900,000.00 USD |
| `15M` | `HTX` | `48.17%` | `51.83%` | `0.93` | 22,780.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `65.61%` | `34.39%` | `1.91` | 46,440.00 USD |
| `15M` | `Aster` | `30.06%` | `69.94%` | `0.43` | 26,050.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `89.19%` | `10.81%` | `8.25` | 90,710.00 USD |
| `15M` | `Whale Positions` | `39.78%` | `60.22%` | `0.66` | 4,120,000.00 USD |
| `15M` | `Global Accounts` | `44.80%` | `55.20%` | `0.81` | 10,480,000.00 USD |
| `1H` | `AVAX` | `48.98%` | `51.02%` | `0.96` | 50,070,000.00 USD |
| `1H` | `Binance` | `54.67%` | `45.33%` | `1.21` | 17,610,000.00 USD |
| `1H` | `OKX` | `49.64%` | `50.36%` | `0.99` | 4,420,000.00 USD |
| `1H` | `Bybit` | `56.68%` | `43.32%` | `1.31` | 9,490,000.00 USD |
| `1H` | `KuCoin` | `42.47%` | `57.53%` | `0.74` | 875,500.00 USD |
| `1H` | `Gate` | `38.06%` | `61.94%` | `0.61` | 1,990,000.00 USD |
| `1H` | `Bitget` | `57.17%` | `42.83%` | `1.33` | 2,250,000.00 USD |
| `1H` | `BingX` | `17.91%` | `82.09%` | `0.22` | 525,860.00 USD |
| `1H` | `MEXC` | `50.14%` | `49.86%` | `1.01` | 487,840.00 USD |
| `1H` | `Bitunix` | `44.44%` | `55.56%` | `0.80` | 769,620.00 USD |
| `1H` | `Hyperliquid` | `54.57%` | `45.43%` | `1.20` | 1,610,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.23%` | `50.77%` | `0.97` | 387,630.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `2.73%` | `97.27%` | `0.03` | 8,850,000.00 USD |
| `1H` | `HTX` | `52.29%` | `47.71%` | `1.10` | 93,690.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `35.19%` | `64.81%` | `0.54` | 399,790.00 USD |
| `1H` | `Aster` | `85.05%` | `14.95%` | `5.69` | 127,050.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `71.63%` | `28.37%` | `2.52` | 195,380.00 USD |
| `1H` | `Whale Positions` | `54.67%` | `45.33%` | `1.21` | 17,610,000.00 USD |
| `1H` | `Global Accounts` | `48.98%` | `51.02%` | `0.96` | 50,070,000.00 USD |
| `4H` | `AVAX` | `44.63%` | `55.37%` | `0.81` | 176,930,000.00 USD |
| `4H` | `Binance` | `45.05%` | `54.95%` | `0.82` | 62,730,000.00 USD |
| `4H` | `OKX` | `48%` | `52%` | `0.92` | 34,600,000.00 USD |
| `4H` | `Bybit` | `44.08%` | `55.92%` | `0.79` | 13,020,000.00 USD |
| `4H` | `KuCoin` | `45.87%` | `54.13%` | `0.85` | 1,190,000.00 USD |
| `4H` | `Gate` | `45.95%` | `54.05%` | `0.85` | 30,470,000.00 USD |
| `4H` | `Bitget` | `46.18%` | `53.82%` | `0.86` | 2,660,000.00 USD |
| `4H` | `BingX` | `37.81%` | `62.19%` | `0.61` | 3,630,000.00 USD |
| `4H` | `MEXC` | `48.47%` | `51.53%` | `0.94` | 8,810,000.00 USD |
| `4H` | `Bitunix` | `47.75%` | `52.25%` | `0.91` | 4,280,000.00 USD |
| `4H` | `Hyperliquid` | `74.38%` | `25.62%` | `2.90` | 2,530,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.23%` | `47.77%` | `1.09` | 1,110,000.00 USD |
| `4H` | `Crypto.com` | `41.74%` | `58.26%` | `0.72` | 263,770.00 USD |
| `4H` | `WhiteBIT` | `9.28%` | `90.72%` | `0.10` | 8,500,000.00 USD |
| `4H` | `HTX` | `50.64%` | `49.36%` | `1.03` | 1,010,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `55.49%` | `44.51%` | `1.25` | 1,170,000.00 USD |
| `4H` | `Aster` | `37.68%` | `62.32%` | `0.60` | 875,660.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `61.82%` | `38.18%` | `1.62` | 93,100.00 USD |
| `4H` | `Whale Positions` | `45.05%` | `54.95%` | `0.82` | 62,730,000.00 USD |
| `4H` | `Global Accounts` | `44.63%` | `55.37%` | `0.81` | 176,930,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `8.49` | `8.48` | `8.49` | `8.50` | `8.45` | 460,668.30 USD | 266,426.92 USD | 194,241.38 USD | 72,185.55 USD | `+15.67%` | `10B / 4S` |
| `0:00 UTC` | `8.48` | `8.48` | `8.48` | `8.51` | `8.46` | 702,848.74 USD | 346,932.98 USD | 355,915.76 USD | -8,982.78 USD | `-1.28%` | `2B / 6S` |
| `5:00 UTC` | `8.46` | `8.47` | `8.46` | `8.48` | `8.46` | 798,371.69 USD | 455,825.46 USD | 342,546.23 USD | 113,279.23 USD | `+14.19%` | `6B / 4S` |
| `0:00 UTC` | `8.47` | `8.46` | `8.47` | `8.48` | `8.44` | 1,028,869.35 USD | 429,609.02 USD | 599,260.32 USD | -169,651.30 USD | `-16.49%` | `4B / 8S` |
| `5:00 UTC` | `8.47` | `8.47` | `8.47` | `8.49` | `8.46` | 909,192.14 USD | 370,410.27 USD | 538,781.87 USD | -168,371.60 USD | `-18.52%` | `3B / 9S` |
| `0:00 UTC` | `8.47` | `8.48` | `8.47` | `8.49` | `8.46` | 824,624.01 USD | 408,080.13 USD | 416,543.88 USD | -8,463.75 USD | `-1.03%` | `2B / 3S` |
| `5:00 UTC` | `8.49` | `8.51` | `8.49` | `8.54` | `8.47` | 897,869.95 USD | 576,315.84 USD | 321,554.11 USD | 254,761.73 USD | `+28.37%` | `17B / 7S` |
| `0:00 UTC` | `8.56` | `8.54` | `8.56` | `8.56` | `8.50` | 1,085,360.20 USD | 616,505.04 USD | 468,855.16 USD | 147,649.89 USD | `+13.60%` | `20B / 10S` |
| `5:00 UTC` | `8.58` | `8.57` | `8.58` | `8.60` | `8.53` | 1,039,077.87 USD | 744,973.52 USD | 294,104.35 USD | 450,869.18 USD | `+43.39%` | `24B / 5S` |
| `0:00 UTC` | `8.58` | `8.59` | `8.58` | `8.62` | `8.57` | 767,591.37 USD | 319,131.88 USD | 448,459.49 USD | -129,327.61 USD | `-16.85%` | `6B / 10S` |

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
| `5m` | 3,320.00 USD | -54,220.00 USD | **`DISTRIBUTION`** |
| `15m` | 14,860.00 USD | -86,950.00 USD | **`DISTRIBUTION`** |
| `30m` | 36,980.00 USD | 468,620.00 USD | **`ACCUMULATION`** |
| `1h` | -62,290.00 USD | 1,150,000.00 USD | **`ACCUMULATION`** |
| `2h` | -123,460.00 USD | 948,370.00 USD | **`ACCUMULATION`** |
| `4h` | -440,250.00 USD | -1,360,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -560,470.00 USD | -537,370.00 USD | **`DISTRIBUTION`** |
| `8h` | -127,410.00 USD | 1,690,000.00 USD | **`ACCUMULATION`** |
| `12h` | -1,430,000.00 USD | -1,730,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,750,000.00 USD | -11,120,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,890,000.00 USD | -49,470,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -57,310,000.00 USD | -265,280,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+3.32K` | 15m=`+14.86K` | 1h=`-62.29K` | 24h=`-2.75M`
* Futures Capital Netflows: 5m=`-54.22K` | 15m=`-86.95K` | 1h=`+1.15M` | 24h=`-11.12M`
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
  * `2026-10-30 16:35:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:32 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:38:32 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Execution Entry: `8.25` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.13` (Risk Distance: `0.1159` pts)
  * +2.5R Take Profit: `8.54`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.59` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.71` (Risk Distance: `0.1159` pts)
  * +2.5R Take Profit: `8.30`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.63`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
