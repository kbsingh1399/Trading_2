# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:33:46 IST` (`2026-10-30 11:03:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.57` | **Live Ask Quote**: `8.60` | **Mid Price**: `8.59`
- **Spread Points**: `3.00` | **Spread BPS**: `34.94 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.59` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `8.65` | Lower -3.00σ Band: `8.52`
  * Upper +2.51σ Band: `8.63` | Lower -2.51σ Band: `8.54`
  * Upper +2.01σ Band: `8.62` | Lower -2.01σ Band: `8.55`
  * Upper +2.00σ Band: `8.62` | Lower -2.00σ Band: `8.55`
  * Upper +1.28σ Band: `8.61` | Lower -1.28σ Band: `8.56`
  * Upper +1.00σ Band: `8.60` | Lower -1.00σ Band: `8.57`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.59` | EMA-20=`8.59` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.59` (Slope: `+0.0000`) | EMA-100=`8.59`
  * Institutional Anchors: EMA-144=`8.59` | EMA-200=`8.59` (Slope: `+0.0000`) | EMA-233=`8.59`
- **Range Boundaries**: 24H High=`8.67` | 24H Low=`8.50` | Weekly High=`8.76` | Weekly Low=`8.41`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.59` (Distance: `-0.09%`)
  * Point of Control (POC) = `8.46` (Distance: `+1.49%`)
  * Value Area Low (VAL) = `8.25` (Distance: `+4.01%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `8.55` - `8.62`
  * Optimal Trade Entry (OTE 0.705): `8.60`
  * Structural Invalidation Anchor (0.786): `8.65`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.55` | `8.56` | `8.55` | `8.55` | `44,612` | 381,701.15 USD | -16,951.89 USD | `-4.44%` | -5,684,545.33 USD | `-0.20` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `8.56` | `8.56` | `8.53` | `8.55` | `26,218` | 224,030.08 USD | 42,474.51 USD | `+18.96%` | -5,642,070.82 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `8.55` | `8.56` | `8.54` | `8.56` | `14,832` | 126,835.94 USD | -2,909.95 USD | `-2.29%` | -5,644,980.77 USD | `-0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `8.51` | `8.56` | `8.50` | `8.55` | `127,080` | 1,085,360.20 USD | 147,649.89 USD | `+13.60%` | -5,387,782.67 USD | `+0.50` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `8.56` | `8.60` | `8.53` | `8.60` | `121,252` | 1,039,077.87 USD | 450,869.18 USD | `+43.39%` | -4,936,913.49 USD | `+1.29` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.60` | `8.62` | `8.59` | `8.60` | `46,154` | 396,990.97 USD | -48,235.96 USD | `-12.15%` | -4,985,149.45 USD | `-0.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `8.48` | `8.51` | `8.44` | `8.49` | `406,103` | 3,439,281.91 USD | -233,726.45 USD | `-6.80%` | -5,798,525.18 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `8.49` | `8.60` | `8.46` | `8.60` | `451,182` | 3,846,932.02 USD | 844,817.04 USD | `+21.96%` | -4,953,708.14 USD | `+0.63` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `8.60` | `8.62` | `8.59` | `8.60` | `45,034` | 387,361.21 USD | -38,606.20 USD | `-9.97%` | -4,992,314.34 USD | `+0.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.56` | `8.44` | `8.56` | `1,216,113` | 10,321,874.97 USD | 39,827.25 USD | `+0.39%` | -5,365,012.75 USD | `+0.63` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,565,817.62 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,901,763.44 USD | `-0.98` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.62` | `8.44` | `8.60` | `1,342,469` | 11,407,077.79 USD | 402,895.91 USD | `+3.53%` | -5,001,944.09 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`8.59`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BUY` | `8.42` | `60660.7100` | 511,054.35 USD | 1,042,654.48 USD | `LARGE (>= USD 100K)` | `-1.96%` | `0x71cfa5e263` |
| `BUY` | `8.42` | `399.8500` | 3,368.38 USD | 4,988,499.13 USD | `STANDARD` | `-1.96%` | `0x14f8e04290` |
| `BUY` | `8.43` | `202.1800` | 1,704.28 USD | 5,060,678.59 USD | `STANDARD` | `-1.90%` | `0x31ca8395cf` |
| `BUY` | `8.43` | `174.2400` | 1,468.76 USD | 5,071,898.43 USD | `STANDARD` | `-1.90%` | `0x010461c14e` |
| `BUY` | `8.45` | `2139.7000` | 18,082.60 USD | 3,870,811.83 USD | `STANDARD` | `-1.65%` | `0xd3943e4008` |
| `BUY` | `8.45` | `315.7300` | 2,668.87 USD | 5,029,154.29 USD | `STANDARD` | `-1.63%` | `0x07fd993f0f` |
| `BUY` | `8.46` | `11522.2600` | 97,494.45 USD | 3,253,823.84 USD | `MEDIUM (>= USD 25K)` | `-1.53%` | `0xecb63caa47` |
| `BUY` | `8.46` | `199.7800` | 1,691.10 USD | 5,064,069.28 USD | `STANDARD` | `-1.49%` | `0x010461c14e` |
| `BUY` | `8.46` | `98.3400` | 832.21 USD | 5,089,455.04 USD | `STANDARD` | `-1.52%` | `0xdadbb4b2a0` |
| `BUY` | `8.47` | `2243.7600` | 18,999.94 USD | 3,759,282.43 USD | `STANDARD` | `-1.45%` | `0x0efb38a5fa` |
| `BUY` | `8.47` | `398.7200` | 3,377.36 USD | 4,981,760.80 USD | `STANDARD` | `-1.42%` | `0x14f8e04290` |
| `BUY` | `8.47` | `200.7000` | 1,699.59 USD | 5,062,378.18 USD | `STANDARD` | `-1.45%` | `0x31ca8395cf` |
| `BUY` | `8.48` | `17135.3500` | 145,254.65 USD | 2,169,610.42 USD | `LARGE (>= USD 100K)` | `-1.35%` | `0x71d0e11ebb` |
| `BUY` | `8.48` | `9629.2300` | 81,642.39 USD | 3,335,466.23 USD | `MEDIUM (>= USD 25K)` | `-1.33%` | `0xecb63caa47` |
| `BUY` | `8.49` | `1884.1200` | 15,999.95 USD | 3,886,811.77 USD | `STANDARD` | `-1.17%` | `0x0efb38a5fa` |
| `BUY` | `8.49` | `588.4000` | 4,993.63 USD | 4,876,941.52 USD | `STANDARD` | `-1.23%` | `0x3ca146d269` |
| `BUY` | `8.50` | `31288.0800` | 266,067.57 USD | 1,580,530.65 USD | `LARGE (>= USD 100K)` | `-1.04%` | `0x71cfa5e263` |
| `BUY` | `8.50` | `9227.8600` | 78,398.05 USD | 3,413,864.28 USD | `MEDIUM (>= USD 25K)` | `-1.13%` | `0xecb63caa47` |
| `BUY` | `8.50` | `7447.7300` | 63,278.15 USD | 3,616,754.24 USD | `MEDIUM (>= USD 25K)` | `-1.12%` | `0x71d0e11ebb` |
| `BUY` | `8.50` | `396.6800` | 3,369.96 USD | 4,985,130.76 USD | `STANDARD` | `-1.13%` | `0x14f8e04290` |
| `BUY` | `8.50` | `234.4200` | 1,992.57 USD | 5,051,386.47 USD | `STANDARD` | `-1.08%` | `0x93f0435268` |
| `BUY` | `8.50` | `85.1200` | 723.43 USD | 5,099,220.52 USD | `STANDARD` | `-1.09%` | `0x010461c14e` |
| `BUY` | `8.51` | `17135.9800` | 145,885.45 USD | 2,024,355.78 USD | `LARGE (>= USD 100K)` | `-0.93%` | `0x71d0e11ebb` |
| `BUY` | `8.51` | `11762.2100` | 100,139.93 USD | 3,056,189.98 USD | `LARGE (>= USD 100K)` | `-0.92%` | `0x881cd92459` |
| `BUY` | `8.51` | `8789.8300` | 74,827.82 USD | 3,488,692.11 USD | `MEDIUM (>= USD 25K)` | `-0.93%` | `0xecb63caa47` |
| `BUY` | `8.51` | `1369.1100` | 11,647.02 USD | 4,514,099.20 USD | `STANDARD` | `-1.00%` | `0x33ad48ed92` |
| `BUY` | `8.51` | `183.6400` | 1,562.52 USD | 5,068,902.30 USD | `STANDARD` | `-0.98%` | `0xdadbb4b2a0` |
| `BUY` | `8.51` | `77.8300` | 662.54 USD | 5,189,864.29 USD | `STANDARD` | `-0.93%` | `0x31ca8395cf` |
| `BUY` | `8.52` | `1729.0300` | 14,729.09 USD | 4,416,137.51 USD | `STANDARD` | `-0.86%` | `0xd3943e4008` |
| `BUY` | `8.53` | `1421.0500` | 12,123.26 USD | 4,442,407.05 USD | `STANDARD` | `-0.72%` | `0xd3943e4008` |
| `BUY` | `8.53` | `1406.4200` | 12,000.00 USD | 4,478,452.45 USD | `STANDARD` | `-0.71%` | `0x0efb38a5fa` |
| `BUY` | `8.53` | `1250.0000` | 10,660.00 USD | 4,580,198.14 USD | `STANDARD` | `-0.76%` | `0xb7bd9cef0e` |
| `BUY` | `8.53` | `396.6800` | 3,383.60 USD | 4,978,383.44 USD | `STANDARD` | `-0.73%` | `0x14f8e04290` |
| `BUY` | `8.54` | `15957.9000` | 136,342.70 USD | 2,443,888.43 USD | `LARGE (>= USD 100K)` | `-0.57%` | `0x71cfa5e263` |
| `BUY` | `8.54` | `14908.2500` | 127,277.69 USD | 2,956,050.06 USD | `LARGE (>= USD 100K)` | `-0.65%` | `0x71d0e11ebb` |
| `BUY` | `8.54` | `1026.8300` | 8,768.00 USD | 4,727,531.29 USD | `STANDARD` | `-0.63%` | `0x33ad48ed92` |
| `BUY` | `8.54` | `83.3000` | 711.73 USD | 5,181,524.15 USD | `STANDARD` | `-0.57%` | `0xea0e878d5d` |
| `BUY` | `8.54` | `83.3000` | 711.72 USD | 5,182,235.87 USD | `STANDARD` | `-0.57%` | `0xfd66e33095` |
| `BUY` | `8.54` | `83.3000` | 711.38 USD | 5,183,658.95 USD | `STANDARD` | `-0.62%` | `0x9d81a3adf8` |
| `BUY` | `8.55` | `2198.6600` | 18,792.17 USD | 3,797,074.52 USD | `STANDARD` | `-0.53%` | `0xa38f19c4cc` |
| `BUY` | `8.55` | `1756.8400` | 15,029.77 USD | 4,371,492.52 USD | `STANDARD` | `-0.44%` | `0x57d8e75f47` |
| `BUY` | `8.55` | `1756.8400` | 15,025.55 USD | 4,386,518.07 USD | `STANDARD` | `-0.47%` | `0x57d8e75f47` |
| `BUY` | `8.55` | `1247.3100` | 10,660.76 USD | 4,569,538.14 USD | `STANDARD` | `-0.53%` | `0xd3943e4008` |
| `BUY` | `8.55` | `1050.8400` | 8,987.20 USD | 4,701,063.27 USD | `STANDARD` | `-0.47%` | `0xd3943e4008` |
| `BUY` | `8.55` | `830.0000` | 7,095.84 USD | 4,797,700.11 USD | `STANDARD` | `-0.51%` | `0xb7bd9cef0e` |
| `BUY` | `8.55` | `453.6900` | 3,878.19 USD | 4,953,967.48 USD | `STANDARD` | `-0.52%` | `0xcd7f60e943` |
| `BUY` | `8.55` | `86.0600` | 735.53 USD | 5,096,315.41 USD | `STANDARD` | `-0.54%` | `0x010461c14e` |
| `BUY` | `8.55` | `83.3100` | 712.55 USD | 5,169,418.67 USD | `STANDARD` | `-0.46%` | `0xea0e878d5d` |
| `BUY` | `8.55` | `83.3000` | 712.44 USD | 5,170,843.60 USD | `STANDARD` | `-0.47%` | `0x63f6411ca6` |
| `BUY` | `8.55` | `83.3100` | 712.33 USD | 5,171,555.93 USD | `STANDARD` | `-0.49%` | `0xd0956a1eba` |
| `BUY` | `8.55` | `83.3200` | 712.29 USD | 5,172,268.23 USD | `STANDARD` | `-0.51%` | `0xea0e878d5d` |
| `BUY` | `8.55` | `83.3000` | 712.26 USD | 5,172,980.48 USD | `STANDARD` | `-0.49%` | `0x53136b4a7c` |
| `BUY` | `8.55` | `83.3000` | 712.19 USD | 5,173,692.67 USD | `STANDARD` | `-0.50%` | `0xd0956a1eba` |
| `BUY` | `8.55` | `83.3000` | 712.18 USD | 5,174,404.86 USD | `STANDARD` | `-0.50%` | `0x53136b4a7c` |
| `BUY` | `8.55` | `83.3000` | 712.11 USD | 5,175,116.96 USD | `STANDARD` | `-0.51%` | `0xa382fa9f4b` |
| `BUY` | `8.55` | `83.3100` | 712.07 USD | 5,175,829.03 USD | `STANDARD` | `-0.53%` | `0xf30120f048` |
| `BUY` | `8.55` | `83.3000` | 712.05 USD | 5,176,541.08 USD | `STANDARD` | `-0.52%` | `0xf30120f048` |
| `BUY` | `8.55` | `83.3200` | 711.99 USD | 5,177,253.07 USD | `STANDARD` | `-0.55%` | `0x63f6411ca6` |
| `BUY` | `8.55` | `83.3000` | 711.92 USD | 5,177,965.00 USD | `STANDARD` | `-0.54%` | `0xea0e878d5d` |
| `BUY` | `8.55` | `83.2200` | 711.90 USD | 5,178,676.89 USD | `STANDARD` | `-0.45%` | `0xd0956a1eba` |
| `BUY` | `8.55` | `83.3000` | 711.85 USD | 5,179,388.74 USD | `STANDARD` | `-0.55%` | `0x9d81a3adf8` |
| `BUY` | `8.55` | `83.3000` | 711.84 USD | 5,180,100.58 USD | `STANDARD` | `-0.55%` | `0xf30120f048` |
| `BUY` | `8.55` | `83.2200` | 711.84 USD | 5,180,812.42 USD | `STANDARD` | `-0.46%` | `0xa382fa9f4b` |
| `BUY` | `8.55` | `83.2200` | 711.70 USD | 5,182,947.56 USD | `STANDARD` | `-0.48%` | `0xf30120f048` |
| `BUY` | `8.55` | `78.6900` | 673.16 USD | 5,189,201.76 USD | `STANDARD` | `-0.45%` | `0x31ca8395cf` |
| `BUY` | `8.56` | `1756.8400` | 15,042.59 USD | 4,326,390.57 USD | `STANDARD` | `-0.36%` | `0x57d8e75f47` |
| `BUY` | `8.56` | `1756.8400` | 15,038.20 USD | 4,341,428.77 USD | `STANDARD` | `-0.39%` | `0x57d8e75f47` |
| `BUY` | `8.56` | `1756.8400` | 15,033.98 USD | 4,356,462.75 USD | `STANDARD` | `-0.41%` | `0x57d8e75f47` |
| `BUY` | `8.56` | `1029.5200` | 8,811.97 USD | 4,718,763.29 USD | `STANDARD` | `-0.39%` | `0xd3342d3b1e` |
| `BUY` | `8.56` | `935.0600` | 8,000.00 USD | 4,751,764.28 USD | `STANDARD` | `-0.43%` | `0x0efb38a5fa` |
| `BUY` | `8.56` | `919.2600` | 7,869.88 USD | 4,775,633.96 USD | `STANDARD` | `-0.37%` | `0xd3943e4008` |
| `BUY` | `8.56` | `911.0400` | 7,799.69 USD | 4,783,433.65 USD | `STANDARD` | `-0.37%` | `0xecb63caa47` |
| `BUY` | `8.56` | `801.9500` | 6,868.54 USD | 4,804,568.65 USD | `STANDARD` | `-0.33%` | `0xecb63caa47` |
| `BUY` | `8.56` | `506.9600` | 4,339.07 USD | 4,890,630.64 USD | `STANDARD` | `-0.39%` | `0xecb63caa47` |
| `BUY` | `8.56` | `455.5400` | 3,897.19 USD | 4,950,089.29 USD | `STANDARD` | `-0.44%` | `0x2a72b57dea` |
| `BUY` | `8.56` | `83.3100` | 712.87 USD | 5,167,280.75 USD | `STANDARD` | `-0.42%` | `0x9d81a3adf8` |
| `BUY` | `8.56` | `83.3000` | 712.72 USD | 5,167,993.48 USD | `STANDARD` | `-0.43%` | `0xf30120f048` |
| `BUY` | `8.56` | `83.3000` | 712.64 USD | 5,168,706.11 USD | `STANDARD` | `-0.44%` | `0x63f6411ca6` |
| `BUY` | `8.56` | `83.2800` | 712.49 USD | 5,170,131.16 USD | `STANDARD` | `-0.44%` | `0xfd66e33095` |
| `BUY` | `8.57` | `14902.5400` | 127,658.14 USD | 2,828,772.36 USD | `LARGE (>= USD 100K)` | `-0.31%` | `0x71d0e11ebb` |
| `BUY` | `8.57` | `3656.3400` | 31,331.18 USD | 3,716,341.60 USD | `MEDIUM (>= USD 25K)` | `-0.28%` | `0x08a49e7f71` |
| `BUY` | `8.57` | `1756.8400` | 15,062.97 USD | 4,281,243.82 USD | `STANDARD` | `-0.22%` | `0x57d8e75f47` |
| `BUY` | `8.57` | `1756.8400` | 15,056.12 USD | 4,296,299.94 USD | `STANDARD` | `-0.27%` | `0x57d8e75f47` |
| `BUY` | `8.57` | `1756.8400` | 15,048.04 USD | 4,311,347.98 USD | `STANDARD` | `-0.32%` | `0x57d8e75f47` |
| `BUY` | `8.57` | `1197.9600` | 10,265.80 USD | 4,642,230.03 USD | `STANDARD` | `-0.27%` | `0xaf9f722a67` |
| `BUY` | `8.57` | `769.3000` | 6,592.36 USD | 4,811,161.01 USD | `STANDARD` | `-0.27%` | `0xecb63caa47` |
| `BUY` | `8.57` | `595.8000` | 5,107.20 USD | 4,846,948.10 USD | `STANDARD` | `-0.24%` | `0xecb63caa47` |
| `BUY` | `8.57` | `583.4100` | 5,000.00 USD | 4,856,948.10 USD | `STANDARD` | `-0.26%` | `0x0efb38a5fa` |
| `BUY` | `8.57` | `481.6400` | 4,128.57 USD | 4,903,111.34 USD | `STANDARD` | `-0.24%` | `0x7717a7a245` |
| `BUY` | `8.57` | `455.5400` | 3,901.93 USD | 4,946,192.10 USD | `STANDARD` | `-0.32%` | `0x2a72b57dea` |
| `BUY` | `8.57` | `420.0000` | 3,599.19 USD | 4,961,185.35 USD | `STANDARD` | `-0.27%` | `0xb7bd9cef0e` |
| `BUY` | `8.57` | `326.4800` | 2,799.53 USD | 5,012,901.38 USD | `STANDARD` | `-0.21%` | `0xecb63caa47` |
| `BUY` | `8.57` | `260.9500` | 2,236.99 USD | 5,041,090.36 USD | `STANDARD` | `-0.24%` | `0xdd4f66125d` |
| `BUY` | `8.57` | `260.9500` | 2,236.55 USD | 5,043,326.91 USD | `STANDARD` | `-0.26%` | `0xdd4f66125d` |
| `BUY` | `8.57` | `236.2000` | 2,024.61 USD | 5,047,385.23 USD | `STANDARD` | `-0.25%` | `0xecb63caa47` |
| `BUY` | `8.57` | `89.1400` | 763.69 USD | 5,093,329.41 USD | `STANDARD` | `-0.30%` | `0x010461c14e` |
| `BUY` | `8.57` | `88.8600` | 761.29 USD | 5,094,090.70 USD | `STANDARD` | `-0.30%` | `0x31ca8395cf` |
| `BUY` | `8.57` | `83.3000` | 714.21 USD | 5,155,861.24 USD | `STANDARD` | `-0.22%` | `0xf30120f048` |
| `BUY` | `8.57` | `83.3100` | 714.18 USD | 5,156,575.43 USD | `STANDARD` | `-0.24%` | `0x9d81a3adf8` |
| `BUY` | `8.57` | `83.3100` | 714.12 USD | 5,157,289.55 USD | `STANDARD` | `-0.24%` | `0x53136b4a7c` |
| `BUY` | `8.57` | `83.3100` | 714.07 USD | 5,158,003.62 USD | `STANDARD` | `-0.25%` | `0xfd66e33095` |
| `BUY` | `8.57` | `83.3000` | 713.89 USD | 5,158,717.51 USD | `STANDARD` | `-0.27%` | `0xea0e878d5d` |
| `BUY` | `8.57` | `83.3000` | 713.84 USD | 5,159,431.35 USD | `STANDARD` | `-0.27%` | `0xea0e878d5d` |
| `BUY` | `8.57` | `83.3000` | 713.81 USD | 5,160,145.15 USD | `STANDARD` | `-0.28%` | `0xd0956a1eba` |
| `BUY` | `8.57` | `83.3000` | 713.71 USD | 5,161,572.63 USD | `STANDARD` | `-0.29%` | `0xea0e878d5d` |
| `BUY` | `8.57` | `83.3000` | 713.71 USD | 5,162,286.34 USD | `STANDARD` | `-0.29%` | `0xf30120f048` |
| `BUY` | `8.57` | `83.3000` | 713.65 USD | 5,163,713.69 USD | `STANDARD` | `-0.30%` | `0x63f6411ca6` |
| `BUY` | `8.57` | `83.3000` | 713.59 USD | 5,164,427.28 USD | `STANDARD` | `-0.31%` | `0xea0e878d5d` |
| `BUY` | `8.57` | `83.3000` | 713.57 USD | 5,165,140.85 USD | `STANDARD` | `-0.31%` | `0xd0956a1eba` |
| `BUY` | `8.57` | `83.2200` | 713.56 USD | 5,165,854.41 USD | `STANDARD` | `-0.22%` | `0x53136b4a7c` |
| `BUY` | `8.57` | `83.2200` | 713.47 USD | 5,166,567.88 USD | `STANDARD` | `-0.23%` | `0x63f6411ca6` |
| `BUY` | `8.58` | `1756.8400` | 15,078.78 USD | 4,236,039.10 USD | `STANDARD` | `-0.12%` | `0x57d8e75f47` |
| `BUY` | `8.58` | `1756.8400` | 15,074.39 USD | 4,251,113.49 USD | `STANDARD` | `-0.15%` | `0x57d8e75f47` |
| `BUY` | `8.58` | `1756.8400` | 15,067.36 USD | 4,266,180.85 USD | `STANDARD` | `-0.19%` | `0x57d8e75f47` |
| `BUY` | `8.58` | `1398.2300` | 11,999.75 USD | 4,502,452.19 USD | `STANDARD` | `-0.13%` | `0x7d0c59691f` |
| `BUY` | `8.58` | `1301.5700` | 11,165.52 USD | 4,548,049.76 USD | `STANDARD` | `-0.17%` | `0x08a49e7f71` |
| `BUY` | `8.58` | `1197.9600` | 10,276.10 USD | 4,631,964.23 USD | `STANDARD` | `-0.17%` | `0xaf9f722a67` |
| `BUY` | `8.58` | `1186.1000` | 10,177.57 USD | 4,662,613.04 USD | `STANDARD` | `-0.14%` | `0x621c555167` |
| `BUY` | `8.58` | `1164.9300` | 9,999.88 USD | 4,682,613.00 USD | `STANDARD` | `-0.10%` | `0x7d0c59691f` |
| `BUY` | `8.58` | `582.4300` | 4,999.93 USD | 4,866,947.96 USD | `STANDARD` | `-0.10%` | `0x44f481f406` |
| `BUY` | `8.58` | `582.6600` | 4,999.92 USD | 4,871,947.89 USD | `STANDARD` | `-0.14%` | `0x44f481f406` |
| `BUY` | `8.58` | `455.5400` | 3,910.31 USD | 4,934,481.19 USD | `STANDARD` | `-0.10%` | `0x2a72b57dea` |
| `BUY` | `8.58` | `455.5400` | 3,907.03 USD | 4,938,388.22 USD | `STANDARD` | `-0.19%` | `0x2a72b57dea` |
| `BUY` | `8.58` | `454.8000` | 3,901.96 USD | 4,942,290.17 USD | `STANDARD` | `-0.16%` | `0xecb63caa47` |
| `BUY` | `8.58` | `312.0500` | 2,677.67 USD | 5,026,485.43 USD | `STANDARD` | `-0.14%` | `0x7717a7a245` |
| `BUY` | `8.58` | `291.2700` | 2,500.00 USD | 5,031,654.29 USD | `STANDARD` | `-0.11%` | `0x0efb38a5fa` |
| `BUY` | `8.58` | `260.9500` | 2,238.17 USD | 5,038,853.36 USD | `STANDARD` | `-0.19%` | `0xdd4f66125d` |
| `BUY` | `8.58` | `84.7100` | 726.74 USD | 5,097,770.82 USD | `STANDARD` | `-0.16%` | `0x31ca8395cf` |
| `BUY` | `8.58` | `83.5000` | 716.61 USD | 5,131,535.22 USD | `STANDARD` | `-0.12%` | `0x31ca8395cf` |
| `BUY` | `8.58` | `83.3000` | 715.06 USD | 5,147,285.14 USD | `STANDARD` | `-0.10%` | `0xa382fa9f4b` |
| `BUY` | `8.58` | `83.3000` | 714.96 USD | 5,148,000.11 USD | `STANDARD` | `-0.12%` | `0xd0956a1eba` |
| `BUY` | `8.58` | `83.3100` | 714.91 USD | 5,148,715.02 USD | `STANDARD` | `-0.13%` | `0x9d81a3adf8` |
| `BUY` | `8.58` | `83.3000` | 714.91 USD | 5,149,429.92 USD | `STANDARD` | `-0.12%` | `0xd0956a1eba` |
| `BUY` | `8.58` | `83.3100` | 714.87 USD | 5,150,144.79 USD | `STANDARD` | `-0.14%` | `0xa382fa9f4b` |
| `BUY` | `8.58` | `83.3100` | 714.72 USD | 5,150,859.51 USD | `STANDARD` | `-0.16%` | `0xea0e878d5d` |
| `BUY` | `8.58` | `83.3000` | 714.70 USD | 5,151,574.21 USD | `STANDARD` | `-0.15%` | `0x63f6411ca6` |
| `BUY` | `8.58` | `83.2900` | 714.67 USD | 5,152,288.88 USD | `STANDARD` | `-0.14%` | `0xfd66e33095` |
| `BUY` | `8.58` | `83.3100` | 714.59 USD | 5,153,003.47 USD | `STANDARD` | `-0.18%` | `0x63f6411ca6` |
| `BUY` | `8.58` | `83.3000` | 714.58 USD | 5,153,718.05 USD | `STANDARD` | `-0.17%` | `0xea0e878d5d` |
| `BUY` | `8.58` | `83.3000` | 714.56 USD | 5,154,432.61 USD | `STANDARD` | `-0.17%` | `0x63f6411ca6` |
| `BUY` | `8.58` | `83.3000` | 714.42 USD | 5,155,147.03 USD | `STANDARD` | `-0.19%` | `0x63f6411ca6` |
| `BUY` | `8.58` | `83.2300` | 713.76 USD | 5,160,858.92 USD | `STANDARD` | `-0.20%` | `0x9d81a3adf8` |
| `BUY` | `8.58` | `83.2300` | 713.71 USD | 5,163,000.04 USD | `STANDARD` | `-0.21%` | `0xfd66e33095` |
| `BUY` | `8.58` | `76.6000` | 657.17 USD | 5,190,521.46 USD | `STANDARD` | `-0.16%` | `0x010461c14e` |
| `ASK` | `8.59` | `142.3000` | 1,223.04 USD | 11,614.03 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.59` | `124.9500` | 1,073.90 USD | 10,390.99 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.59` | `818.2400` | 7,032.36 USD | 9,317.09 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `8.59` | `62.4700` | 536.87 USD | 2,284.73 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.59` | `120.0800` | 1,031.96 USD | 1,747.86 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.59` | `83.3100` | 715.91 USD | 715.91 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `8.59` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.59` | `0.00%` | `-` |
| `BID` | `8.59` | `20.7900` | 178.64 USD | 178.64 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `8.59` | `148.3200` | 1,274.34 USD | 1,452.97 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.59` | `83.3100` | 715.72 USD | 2,168.70 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.59` | `83.3000` | 715.58 USD | 2,884.28 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.59` | `166.2600` | 1,428.21 USD | 4,312.49 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.59` | `83.3100` | 715.61 USD | 5,028.09 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.59` | `62.4700` | 536.59 USD | 5,564.69 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.59` | `83.3000` | 715.46 USD | 6,280.15 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.59` | `83.3100` | 715.53 USD | 6,995.68 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.59` | `2047.9300` | 17,588.44 USD | 24,584.12 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.59` | `137.5600` | 1,181.39 USD | 25,765.52 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.59` | `582.2000` | 4,999.93 USD | 30,765.45 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.59` | `83.3000` | 715.36 USD | 31,480.81 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.59` | `815.0600` | 6,999.41 USD | 38,480.22 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `8.59` | `83.3000` | 715.34 USD | 39,195.55 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.59` | `83.3100` | 715.41 USD | 39,910.96 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.59` | `1186.1000` | 10,185.28 USD | 50,096.24 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.59` | `60.3400` | 518.13 USD | 50,614.37 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.59` | `2.9000` | 24.90 USD | 50,639.28 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.59` | `931.6600` | 7,999.88 USD | 58,639.16 USD | `1 orders` | `-0.07%` | `-` |
| `BUY` | `8.59` | `1756.8400` | 15,088.44 USD | 4,205,876.27 USD | `STANDARD` | `-0.05%` | `0x57d8e75f47` |
| `BUY` | `8.59` | `1756.8400` | 15,084.05 USD | 4,220,960.32 USD | `STANDARD` | `-0.08%` | `0x57d8e75f47` |
| `SELL` | `8.59` | `930.9100` | 8,000.05 USD | 4,743,764.28 USD | `STANDARD` | `+0.01%` | `0x7d0c59691f` |
| `BUY` | `8.59` | `931.8000` | 7,999.88 USD | 4,767,764.09 USD | `STANDARD` | `-0.09%` | `0x7d0c59691f` |
| `SELL` | `8.59` | `698.2800` | 6,000.95 USD | 4,835,841.04 USD | `STANDARD` | `+0.01%` | `0x7d0c59691f` |
| `BUY` | `8.59` | `698.7400` | 5,999.87 USD | 4,841,840.91 USD | `STANDARD` | `-0.07%` | `0x7d0c59691f` |
| `BUY` | `8.59` | `582.2000` | 4,999.93 USD | 4,861,948.04 USD | `STANDARD` | `-0.06%` | `0x44f481f406` |
| `SELL` | `8.59` | `221.1200` | 1,899.97 USD | 5,053,286.44 USD | `STANDARD` | `-0.00%` | `0xbb82851567` |
| `SELL` | `8.59` | `221.1200` | 1,899.95 USD | 5,055,186.39 USD | `STANDARD` | `-0.01%` | `0xbb82851567` |
| `SELL` | `8.59` | `221.1200` | 1,899.93 USD | 5,057,086.32 USD | `STANDARD` | `-0.01%` | `0xbb82851567` |
| `SELL` | `8.59` | `150.2700` | 1,291.29 USD | 5,073,189.71 USD | `STANDARD` | `+0.00%` | `0xecb63caa47` |
| `BUY` | `8.59` | `148.3200` | 1,274.19 USD | 5,074,463.90 USD | `STANDARD` | `-0.02%` | `0x727956612a` |
| `SELL` | `8.59` | `142.3000` | 1,222.93 USD | 5,075,686.82 USD | `STANDARD` | `+0.01%` | `0x727956612a` |
| `BUY` | `8.59` | `137.5600` | 1,181.26 USD | 5,078,054.91 USD | `STANDARD` | `-0.07%` | `0xdd4f66125d` |
| `BUY` | `8.59` | `137.5600` | 1,181.19 USD | 5,079,236.09 USD | `STANDARD` | `-0.07%` | `0xdd4f66125d` |
| `BUY` | `8.59` | `137.5600` | 1,181.05 USD | 5,080,417.14 USD | `STANDARD` | `-0.08%` | `0xdd4f66125d` |
| `BUY` | `8.59` | `131.4900` | 1,129.30 USD | 5,081,546.44 USD | `STANDARD` | `-0.05%` | `0xecb63caa47` |
| `SELL` | `8.59` | `124.9500` | 1,073.90 USD | 5,082,620.34 USD | `STANDARD` | `+0.02%` | `0x63f6411ca6` |
| `SELL` | `8.59` | `124.9500` | 1,073.65 USD | 5,083,693.98 USD | `STANDARD` | `-0.00%` | `0x63f6411ca6` |
| `SELL` | `8.59` | `120.0800` | 1,031.96 USD | 5,084,725.94 USD | `STANDARD` | `+0.01%` | `0x7717a7a245` |
| `BUY` | `8.59` | `120.0800` | 1,030.97 USD | 5,085,756.91 USD | `STANDARD` | `-0.08%` | `0x7717a7a245` |
| `BUY` | `8.59` | `116.4700` | 999.96 USD | 5,086,756.88 USD | `STANDARD` | `-0.08%` | `0x0eecd62efb` |
| `BUY` | `8.59` | `89.1500` | 765.62 USD | 5,092,565.72 USD | `STANDARD` | `-0.06%` | `0x010461c14e` |
| `SELL` | `8.59` | `83.3100` | 715.91 USD | 5,140,846.75 USD | `STANDARD` | `+0.00%` | `0xa382fa9f4b` |
| `BUY` | `8.59` | `83.3100` | 715.61 USD | 5,141,562.35 USD | `STANDARD` | `-0.04%` | `0xa382fa9f4b` |
| `BUY` | `8.59` | `83.3000` | 715.58 USD | 5,142,277.93 USD | `STANDARD` | `-0.03%` | `0x63f6411ca6` |
| `BUY` | `8.59` | `83.3100` | 715.53 USD | 5,142,993.47 USD | `STANDARD` | `-0.05%` | `0xfd66e33095` |
| `BUY` | `8.59` | `83.3000` | 715.46 USD | 5,143,708.93 USD | `STANDARD` | `-0.05%` | `0x9d81a3adf8` |
| `BUY` | `8.59` | `83.3000` | 715.36 USD | 5,144,424.29 USD | `STANDARD` | `-0.06%` | `0xfd66e33095` |
| `BUY` | `8.59` | `83.3000` | 715.34 USD | 5,145,139.62 USD | `STANDARD` | `-0.06%` | `0xf30120f048` |
| `BUY` | `8.59` | `83.3100` | 715.24 USD | 5,145,854.87 USD | `STANDARD` | `-0.09%` | `0xf30120f048` |
| `BUY` | `8.59` | `83.3000` | 715.21 USD | 5,146,570.08 USD | `STANDARD` | `-0.08%` | `0xfd66e33095` |
| `BUY` | `8.59` | `80.0200` | 687.21 USD | 5,187,844.74 USD | `STANDARD` | `-0.06%` | `0x31ca8395cf` |
| `ASK` | `8.60` | `138.5600` | 1,191.38 USD | 31,161.17 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.60` | `142.6500` | 1,226.53 USD | 29,969.79 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.60` | `476.9200` | 4,100.61 USD | 28,743.26 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.60` | `45.9200` | 394.80 USD | 24,642.65 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.60` | `83.3100` | 716.23 USD | 24,247.86 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.60` | `83.3000` | 716.11 USD | 23,531.62 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.60` | `116.3200` | 999.96 USD | 22,815.52 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.60` | `46.6700` | 401.19 USD | 21,815.56 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.60` | `14.3100` | 123.01 USD | 21,414.37 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.60` | `930.6700` | 8,000.23 USD | 21,291.36 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.60` | `16.8800` | 145.10 USD | 13,291.13 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.60` | `11.6300` | 99.97 USD | 13,146.03 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.60` | `83.3000` | 716.04 USD | 13,046.06 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.60` | `83.3000` | 715.99 USD | 12,330.02 USD | `1 orders` | `+0.03%` | `-` |
| `SELL` | `8.60` | `1756.8400` | 15,116.03 USD | 4,145,466.44 USD | `STANDARD` | `+0.13%` | `0x57d8e75f47` |
| `SELL` | `8.60` | `1756.8400` | 15,111.63 USD | 4,160,578.08 USD | `STANDARD` | `+0.10%` | `0x57d8e75f47` |
| `SELL` | `8.60` | `1756.8400` | 15,107.07 USD | 4,175,685.15 USD | `STANDARD` | `+0.07%` | `0x57d8e75f47` |
| `SELL` | `8.60` | `1756.8400` | 15,102.68 USD | 4,190,787.82 USD | `STANDARD` | `+0.04%` | `0x57d8e75f47` |
| `SELL` | `8.60` | `1395.4400` | 12,000.09 USD | 4,466,452.45 USD | `STANDARD` | `+0.08%` | `0x7d0c59691f` |
| `SELL` | `8.60` | `1297.9300` | 11,165.70 USD | 4,536,884.24 USD | `STANDARD` | `+0.11%` | `0x08a49e7f71` |
| `SELL` | `8.60` | `1197.9600` | 10,306.77 USD | 4,611,391.67 USD | `STANDARD` | `+0.12%` | `0xaf9f722a67` |
| `SELL` | `8.60` | `1197.9600` | 10,296.47 USD | 4,621,688.13 USD | `STANDARD` | `+0.02%` | `0xaf9f722a67` |
| `SELL` | `8.60` | `1186.1000` | 10,205.44 USD | 4,652,435.47 USD | `STANDARD` | `+0.13%` | `0x621c555167` |
| `SELL` | `8.60` | `1163.4500` | 10,000.09 USD | 4,672,613.13 USD | `STANDARD` | `+0.03%` | `0x7d0c59691f` |
| `SELL` | `8.60` | `489.0100` | 4,205.98 USD | 4,894,836.62 USD | `STANDARD` | `+0.09%` | `0x71d0e11ebb` |
| `SELL` | `8.60` | `455.5400` | 3,919.19 USD | 4,926,654.10 USD | `STANDARD` | `+0.12%` | `0x2a72b57dea` |
| `SELL` | `8.60` | `455.5400` | 3,916.78 USD | 4,930,570.88 USD | `STANDARD` | `+0.06%` | `0x2a72b57dea` |
| `SELL` | `8.60` | `331.0000` | 2,847.36 USD | 5,010,101.85 USD | `STANDARD` | `+0.11%` | `0xecb63caa47` |
| `SELL` | `8.60` | `312.0500` | 2,683.82 USD | 5,023,807.76 USD | `STANDARD` | `+0.09%` | `0x7717a7a245` |
| `SELL` | `8.60` | `290.7200` | 2,499.96 USD | 5,034,154.25 USD | `STANDARD` | `+0.07%` | `0x0efb38a5fa` |
| `SELL` | `8.60` | `286.0000` | 2,460.94 USD | 5,036,615.20 USD | `STANDARD` | `+0.14%` | `0xecb63caa47` |
| `SELL` | `8.60` | `219.5800` | 1,887.99 USD | 5,058,974.31 USD | `STANDARD` | `+0.06%` | `0x414ade317c` |
| `SELL` | `8.60` | `116.3200` | 999.96 USD | 5,087,756.83 USD | `STANDARD` | `+0.04%` | `0x0eecd62efb` |
| `SELL` | `8.60` | `91.7000` | 788.66 USD | 5,090,243.70 USD | `STANDARD` | `+0.09%` | `0xdd4f66125d` |
| `SELL` | `8.60` | `91.7000` | 788.59 USD | 5,091,032.29 USD | `STANDARD` | `+0.08%` | `0xdd4f66125d` |
| `SELL` | `8.60` | `83.3100` | 716.74 USD | 5,128,668.52 USD | `STANDARD` | `+0.12%` | `0x53136b4a7c` |
| `SELL` | `8.60` | `83.3000` | 716.71 USD | 5,129,385.23 USD | `STANDARD` | `+0.13%` | `0x9d81a3adf8` |
| `SELL` | `8.60` | `83.3100` | 716.69 USD | 5,130,101.93 USD | `STANDARD` | `+0.11%` | `0xd0956a1eba` |
| `SELL` | `8.60` | `83.2900` | 716.68 USD | 5,130,818.60 USD | `STANDARD` | `+0.14%` | `0xd0956a1eba` |
| `SELL` | `8.60` | `83.3100` | 716.60 USD | 5,132,251.82 USD | `STANDARD` | `+0.10%` | `0xf30120f048` |
| `SELL` | `8.60` | `83.3000` | 716.57 USD | 5,132,968.39 USD | `STANDARD` | `+0.11%` | `0xf30120f048` |
| `SELL` | `8.60` | `83.3000` | 716.45 USD | 5,133,684.83 USD | `STANDARD` | `+0.09%` | `0xa382fa9f4b` |
| `SELL` | `8.60` | `83.3000` | 716.39 USD | 5,134,401.22 USD | `STANDARD` | `+0.08%` | `0xf30120f048` |
| `SELL` | `8.60` | `83.3100` | 716.37 USD | 5,135,117.60 USD | `STANDARD` | `+0.07%` | `0xfd66e33095` |
| `SELL` | `8.60` | `83.3000` | 716.33 USD | 5,135,833.93 USD | `STANDARD` | `+0.08%` | `0x63f6411ca6` |
| `SELL` | `8.60` | `83.3100` | 716.29 USD | 5,136,550.22 USD | `STANDARD` | `+0.06%` | `0xd0956a1eba` |
| `SELL` | `8.60` | `83.3000` | 716.26 USD | 5,137,266.47 USD | `STANDARD` | `+0.07%` | `0xf30120f048` |
| `SELL` | `8.60` | `83.3100` | 716.23 USD | 5,137,982.71 USD | `STANDARD` | `+0.05%` | `0x9d81a3adf8` |
| `SELL` | `8.60` | `83.3000` | 716.11 USD | 5,138,698.81 USD | `STANDARD` | `+0.04%` | `0xd0956a1eba` |
| `SELL` | `8.60` | `83.3000` | 716.04 USD | 5,139,414.85 USD | `STANDARD` | `+0.03%` | `0xea0e878d5d` |
| `SELL` | `8.60` | `83.3000` | 715.99 USD | 5,140,130.84 USD | `STANDARD` | `+0.03%` | `0xd0956a1eba` |
| `SELL` | `8.60` | `81.2100` | 698.27 USD | 5,186,468.12 USD | `STANDARD` | `+0.06%` | `0x31ca8395cf` |
| `SELL` | `8.60` | `80.1800` | 689.40 USD | 5,187,157.52 USD | `STANDARD` | `+0.06%` | `0x2eddf3aa5c` |
| `SELL` | `8.60` | `73.3300` | 630.51 USD | 5,191,800.50 USD | `STANDARD` | `+0.06%` | `0x010461c14e` |
| `SELL` | `8.61` | `3637.3300` | 31,331.60 USD | 3,685,010.42 USD | `MEDIUM (>= USD 25K)` | `+0.24%` | `0x08a49e7f71` |
| `SELL` | `8.61` | `1756.8400` | 15,130.08 USD | 4,100,104.48 USD | `STANDARD` | `+0.22%` | `0x57d8e75f47` |
| `SELL` | `8.61` | `1756.8400` | 15,125.34 USD | 4,115,229.82 USD | `STANDARD` | `+0.19%` | `0x57d8e75f47` |
| `SELL` | `8.61` | `1756.8400` | 15,120.59 USD | 4,130,350.42 USD | `STANDARD` | `+0.16%` | `0x57d8e75f47` |
| `SELL` | `8.61` | `1197.9600` | 10,317.07 USD | 4,601,084.90 USD | `STANDARD` | `+0.22%` | `0xaf9f722a67` |
| `SELL` | `8.61` | `580.4100` | 5,000.00 USD | 4,851,948.10 USD | `STANDARD` | `+0.25%` | `0x0efb38a5fa` |
| `SELL` | `8.61` | `481.6400` | 4,146.15 USD | 4,898,982.77 USD | `STANDARD` | `+0.18%` | `0x7717a7a245` |
| `SELL` | `8.61` | `455.5400` | 3,924.11 USD | 4,914,891.33 USD | `STANDARD` | `+0.25%` | `0x2a72b57dea` |
| `SELL` | `8.61` | `455.5400` | 3,921.74 USD | 4,922,734.91 USD | `STANDARD` | `+0.19%` | `0x2a72b57dea` |
| `SELL` | `8.61` | `386.2900` | 3,324.72 USD | 4,991,823.85 USD | `STANDARD` | `+0.16%` | `0xecb63caa47` |
| `SELL` | `8.61` | `366.8200` | 3,158.10 USD | 5,001,304.90 USD | `STANDARD` | `+0.19%` | `0xdd4f66125d` |
| `SELL` | `8.61` | `349.1800` | 3,006.27 USD | 5,004,311.17 USD | `STANDARD` | `+0.19%` | `0xecb63caa47` |
| `SELL` | `8.61` | `341.7500` | 2,943.32 USD | 5,007,254.49 USD | `STANDARD` | `+0.23%` | `0xecb63caa47` |
| `SELL` | `8.61` | `233.2000` | 2,008.67 USD | 5,049,393.90 USD | `STANDARD` | `+0.24%` | `0x39bac00809` |
| `SELL` | `8.61` | `86.4300` | 743.77 USD | 5,095,579.88 USD | `STANDARD` | `+0.15%` | `0x31ca8395cf` |
| `SELL` | `8.61` | `83.3200` | 717.62 USD | 5,117,910.68 USD | `STANDARD` | `+0.23%` | `0xd0956a1eba` |
| `SELL` | `8.61` | `83.3000` | 717.60 USD | 5,118,628.27 USD | `STANDARD` | `+0.25%` | `0x9d81a3adf8` |
| `SELL` | `8.61` | `83.3000` | 717.53 USD | 5,119,345.80 USD | `STANDARD` | `+0.24%` | `0xa382fa9f4b` |
| `SELL` | `8.61` | `83.3000` | 717.50 USD | 5,120,063.31 USD | `STANDARD` | `+0.24%` | `0xa382fa9f4b` |
| `SELL` | `8.61` | `83.3100` | 717.46 USD | 5,120,780.76 USD | `STANDARD` | `+0.22%` | `0xea0e878d5d` |
| `SELL` | `8.61` | `83.3000` | 717.33 USD | 5,121,498.09 USD | `STANDARD` | `+0.22%` | `0xd0956a1eba` |
| `SELL` | `8.61` | `83.3000` | 717.27 USD | 5,122,215.36 USD | `STANDARD` | `+0.21%` | `0xea0e878d5d` |
| `SELL` | `8.61` | `83.3100` | 717.24 USD | 5,122,932.61 USD | `STANDARD` | `+0.19%` | `0xd0956a1eba` |
| `SELL` | `8.61` | `83.3000` | 717.21 USD | 5,123,649.82 USD | `STANDARD` | `+0.20%` | `0x53136b4a7c` |
| `SELL` | `8.61` | `83.3000` | 717.12 USD | 5,124,366.94 USD | `STANDARD` | `+0.19%` | `0xf30120f048` |
| `SELL` | `8.61` | `83.3000` | 717.05 USD | 5,125,083.99 USD | `STANDARD` | `+0.18%` | `0x9d81a3adf8` |
| `SELL` | `8.61` | `83.3000` | 717.05 USD | 5,125,801.04 USD | `STANDARD` | `+0.18%` | `0xa382fa9f4b` |
| `SELL` | `8.61` | `83.3000` | 716.99 USD | 5,126,518.03 USD | `STANDARD` | `+0.17%` | `0x9d81a3adf8` |
| `SELL` | `8.61` | `83.3000` | 716.93 USD | 5,127,234.96 USD | `STANDARD` | `+0.16%` | `0x53136b4a7c` |
| `SELL` | `8.61` | `83.3000` | 716.82 USD | 5,127,951.78 USD | `STANDARD` | `+0.14%` | `0xea0e878d5d` |
| `SELL` | `8.61` | `81.7700` | 703.66 USD | 5,185,071.53 USD | `STANDARD` | `+0.15%` | `0x010461c14e` |
| `SELL` | `8.61` | `81.1200` | 698.32 USD | 5,185,769.85 USD | `STANDARD` | `+0.18%` | `0x31ca8395cf` |
| `SELL` | `8.62` | `14908.8700` | 128,460.79 USD | 2,701,114.23 USD | `LARGE (>= USD 100K)` | `+0.27%` | `0x71d0e11ebb` |
| `SELL` | `8.62` | `1756.8400` | 15,149.76 USD | 4,054,695.27 USD | `STANDARD` | `+0.35%` | `0x57d8e75f47` |
| `SELL` | `8.62` | `1756.8400` | 15,143.26 USD | 4,069,838.52 USD | `STANDARD` | `+0.31%` | `0x57d8e75f47` |
| `SELL` | `8.62` | `1756.8400` | 15,135.88 USD | 4,084,974.40 USD | `STANDARD` | `+0.26%` | `0x57d8e75f47` |
| `SELL` | `8.62` | `1640.3000` | 14,146.28 USD | 4,430,283.78 USD | `STANDARD` | `+0.36%` | `0xb45f5c538d` |
| `SELL` | `8.62` | `954.6100` | 8,232.94 USD | 4,735,764.23 USD | `STANDARD` | `+0.37%` | `0xd3943e4008` |
| `SELL` | `8.62` | `538.1600` | 4,638.89 USD | 4,886,291.57 USD | `STANDARD` | `+0.31%` | `0xecb63caa47` |
| `SELL` | `8.62` | `455.5400` | 3,926.57 USD | 4,910,967.22 USD | `STANDARD` | `+0.31%` | `0x2a72b57dea` |
| `SELL` | `8.62` | `420.0000` | 3,618.68 USD | 4,957,586.16 USD | `STANDARD` | `+0.27%` | `0xb7bd9cef0e` |
| `SELL` | `8.62` | `366.8200` | 3,162.25 USD | 4,994,986.10 USD | `STANDARD` | `+0.32%` | `0xdd4f66125d` |
| `SELL` | `8.62` | `366.8200` | 3,160.70 USD | 4,998,146.80 USD | `STANDARD` | `+0.27%` | `0xdd4f66125d` |
| `SELL` | `8.62` | `315.7300` | 2,722.86 USD | 5,021,123.94 USD | `STANDARD` | `+0.36%` | `0x07fd993f0f` |
| `SELL` | `8.62` | `137.7500` | 1,186.83 USD | 5,076,873.65 USD | `STANDARD` | `+0.27%` | `0x26934acbd3` |
| `SELL` | `8.62` | `84.5400` | 728.67 USD | 5,097,044.08 USD | `STANDARD` | `+0.31%` | `0x31ca8395cf` |
| `SELL` | `8.62` | `83.3100` | 717.82 USD | 5,116,475.40 USD | `STANDARD` | `+0.27%` | `0xea0e878d5d` |
| `SELL` | `8.62` | `83.3000` | 717.65 USD | 5,117,193.06 USD | `STANDARD` | `+0.26%` | `0x53136b4a7c` |
| `SELL` | `8.62` | `82.2500` | 708.92 USD | 5,184,367.87 USD | `STANDARD` | `+0.30%` | `0x010461c14e` |
| `SELL` | `8.63` | `2772.6700` | 23,940.90 USD | 3,740,282.49 USD | `STANDARD` | `+0.49%` | `0xb45f5c538d` |
| `SELL` | `8.63` | `2132.5200` | 18,402.37 USD | 3,852,729.22 USD | `STANDARD` | `+0.42%` | `0xb45f5c538d` |
| `SELL` | `8.63` | `1756.8400` | 15,166.80 USD | 4,024,387.14 USD | `STANDARD` | `+0.47%` | `0x57d8e75f47` |
| `SELL` | `8.63` | `1756.8400` | 15,158.37 USD | 4,039,545.51 USD | `STANDARD` | `+0.41%` | `0x57d8e75f47` |
| `SELL` | `8.63` | `1096.1500` | 9,463.06 USD | 4,692,076.07 USD | `STANDARD` | `+0.47%` | `0xd3943e4008` |
| `SELL` | `8.63` | `1029.5200` | 8,888.05 USD | 4,709,951.32 USD | `STANDARD` | `+0.47%` | `0xd3342d3b1e` |
| `SELL` | `8.63` | `926.6900` | 7,999.93 USD | 4,759,764.21 USD | `STANDARD` | `+0.46%` | `0x0efb38a5fa` |
| `SELL` | `8.63` | `724.1900` | 6,246.79 USD | 4,823,821.94 USD | `STANDARD` | `+0.38%` | `0xecb63caa47` |
| `SELL` | `8.63` | `697.3600` | 6,018.15 USD | 4,829,840.09 USD | `STANDARD` | `+0.43%` | `0xecb63caa47` |
| `SELL` | `8.63` | `455.5400` | 3,929.31 USD | 4,907,040.64 USD | `STANDARD` | `+0.38%` | `0x2a72b57dea` |
| `SELL` | `8.63` | `235.5600` | 2,033.71 USD | 5,045,360.62 USD | `STANDARD` | `+0.47%` | `0x26934acbd3` |
| `SELL` | `8.63` | `83.3100` | 719.28 USD | 5,104,257.27 USD | `STANDARD` | `+0.48%` | `0xfd66e33095` |
| `SELL` | `8.63` | `83.3000` | 719.25 USD | 5,104,976.53 USD | `STANDARD` | `+0.48%` | `0xa382fa9f4b` |
| `SELL` | `8.63` | `83.3000` | 719.20 USD | 5,105,695.73 USD | `STANDARD` | `+0.48%` | `0xf30120f048` |
| `SELL` | `8.63` | `83.3100` | 719.11 USD | 5,106,414.84 USD | `STANDARD` | `+0.45%` | `0x53136b4a7c` |
| `SELL` | `8.63` | `83.3000` | 718.96 USD | 5,107,133.80 USD | `STANDARD` | `+0.44%` | `0x53136b4a7c` |
| `SELL` | `8.63` | `83.3000` | 718.95 USD | 5,107,852.75 USD | `STANDARD` | `+0.44%` | `0x63f6411ca6` |
| `SELL` | `8.63` | `83.3000` | 718.90 USD | 5,108,571.66 USD | `STANDARD` | `+0.44%` | `0xea0e878d5d` |
| `SELL` | `8.63` | `83.3000` | 718.78 USD | 5,110,728.12 USD | `STANDARD` | `+0.42%` | `0xa382fa9f4b` |
| `SELL` | `8.63` | `83.3000` | 718.72 USD | 5,111,446.84 USD | `STANDARD` | `+0.41%` | `0x53136b4a7c` |
| `SELL` | `8.63` | `83.3000` | 718.67 USD | 5,112,165.51 USD | `STANDARD` | `+0.40%` | `0xfd66e33095` |
| `SELL` | `8.63` | `83.3000` | 718.61 USD | 5,112,884.12 USD | `STANDARD` | `+0.39%` | `0xfd66e33095` |
| `SELL` | `8.63` | `83.3000` | 718.50 USD | 5,113,602.62 USD | `STANDARD` | `+0.38%` | `0x63f6411ca6` |
| `SELL` | `8.63` | `83.2100` | 718.34 USD | 5,114,320.97 USD | `STANDARD` | `+0.47%` | `0xfd66e33095` |
| `SELL` | `8.63` | `83.2100` | 718.34 USD | 5,115,039.30 USD | `STANDARD` | `+0.46%` | `0x53136b4a7c` |
| `SELL` | `8.63` | `83.2100` | 718.28 USD | 5,115,757.58 USD | `STANDARD` | `+0.46%` | `0xa382fa9f4b` |
| `SELL` | `8.63` | `64.2000` | 554.37 USD | 5,192,354.86 USD | `STANDARD` | `+0.49%` | `0x18c0b7b9fe` |
| `SELL` | `8.64` | `15957.9000` | 137,935.30 USD | 2,307,545.72 USD | `LARGE (>= USD 100K)` | `+0.59%` | `0x71cfa5e263` |
| `SELL` | `8.64` | `2176.2000` | 18,792.14 USD | 3,815,866.66 USD | `STANDARD` | `+0.49%` | `0xa38f19c4cc` |
| `SELL` | `8.64` | `1756.8400` | 15,184.02 USD | 3,994,044.93 USD | `STANDARD` | `+0.58%` | `0x57d8e75f47` |
| `SELL` | `8.64` | `1756.8400` | 15,175.41 USD | 4,009,220.34 USD | `STANDARD` | `+0.52%` | `0x57d8e75f47` |
| `SELL` | `8.64` | `1223.2300` | 10,569.69 USD | 4,590,767.83 USD | `STANDARD` | `+0.56%` | `0xd3943e4008` |
| `SELL` | `8.64` | `830.0000` | 7,170.62 USD | 4,790,604.27 USD | `STANDARD` | `+0.54%` | `0xb7bd9cef0e` |
| `SELL` | `8.64` | `742.3600` | 6,414.14 USD | 4,817,575.15 USD | `STANDARD` | `+0.55%` | `0x26934acbd3` |
| `SELL` | `8.64` | `453.6900` | 3,921.83 USD | 4,918,813.16 USD | `STANDARD` | `+0.60%` | `0xcd7f60e943` |
| `SELL` | `8.64` | `86.2800` | 745.41 USD | 5,094,836.11 USD | `STANDARD` | `+0.54%` | `0x31ca8395cf` |
| `SELL` | `8.64` | `83.3000` | 719.88 USD | 5,099,940.40 USD | `STANDARD` | `+0.57%` | `0xf30120f048` |
| `SELL` | `8.64` | `83.2900` | 719.73 USD | 5,100,660.13 USD | `STANDARD` | `+0.56%` | `0xea0e878d5d` |
| `SELL` | `8.64` | `83.3000` | 719.70 USD | 5,101,379.83 USD | `STANDARD` | `+0.55%` | `0x9d81a3adf8` |
| `SELL` | `8.64` | `83.3000` | 719.50 USD | 5,102,099.33 USD | `STANDARD` | `+0.52%` | `0x9d81a3adf8` |
| `SELL` | `8.64` | `83.2900` | 719.35 USD | 5,102,818.68 USD | `STANDARD` | `+0.51%` | `0x63f6411ca6` |
| `SELL` | `8.64` | `83.3000` | 719.31 USD | 5,103,537.99 USD | `STANDARD` | `+0.49%` | `0x53136b4a7c` |
| `SELL` | `8.64` | `83.2100` | 718.87 USD | 5,109,290.53 USD | `STANDARD` | `+0.54%` | `0xfd66e33095` |
| `SELL` | `8.64` | `83.2100` | 718.81 USD | 5,110,009.34 USD | `STANDARD` | `+0.53%` | `0x53136b4a7c` |
| `SELL` | `8.64` | `62.4800` | 540.00 USD | 5,192,894.86 USD | `STANDARD` | `+0.58%` | `0xfd66e33095` |
| `SELL` | `8.64` | `62.4700` | 539.78 USD | 5,193,434.64 USD | `STANDARD` | `+0.56%` | `0x53136b4a7c` |
| `SELL` | `8.64` | `62.4900` | 539.78 USD | 5,193,974.41 USD | `STANDARD` | `+0.52%` | `0x63f6411ca6` |
| `SELL` | `8.64` | `62.4800` | 539.61 USD | 5,194,514.03 USD | `STANDARD` | `+0.51%` | `0xa382fa9f4b` |
| `SELL` | `8.65` | `14893.3600` | 128,765.01 USD | 2,572,653.44 USD | `LARGE (>= USD 100K)` | `+0.62%` | `0x71d0e11ebb` |
| `SELL` | `8.65` | `1756.8400` | 15,201.23 USD | 3,963,668.29 USD | `STANDARD` | `+0.69%` | `0x57d8e75f47` |
| `SELL` | `8.65` | `1756.8400` | 15,192.63 USD | 3,978,860.92 USD | `STANDARD` | `+0.64%` | `0x57d8e75f47` |
| `SELL` | `8.65` | `544.4800` | 4,711.17 USD | 4,881,652.69 USD | `STANDARD` | `+0.69%` | `0x26934acbd3` |
| `SELL` | `8.65` | `394.0900` | 3,410.26 USD | 4,974,999.84 USD | `STANDARD` | `+0.71%` | `0x14f8e04290` |
| `SELL` | `8.65` | `79.1000` | 683.86 USD | 5,188,528.60 USD | `STANDARD` | `+0.61%` | `0x010461c14e` |
| `SELL` | `8.66` | `1756.8400` | 15,218.45 USD | 3,933,257.21 USD | `STANDARD` | `+0.81%` | `0x57d8e75f47` |
| `SELL` | `8.66` | `1756.8400` | 15,209.84 USD | 3,948,467.06 USD | `STANDARD` | `+0.75%` | `0x57d8e75f47` |
| `SELL` | `8.66` | `1386.3200` | 11,999.99 USD | 4,490,452.44 USD | `STANDARD` | `+0.73%` | `0x0efb38a5fa` |
| `SELL` | `8.66` | `1250.0000` | 10,827.62 USD | 4,558,877.38 USD | `STANDARD` | `+0.81%` | `0xb7bd9cef0e` |
| `SELL` | `8.66` | `100.0000` | 866.00 USD | 5,088,622.83 USD | `STANDARD` | `+0.78%` | `0x9ea98d75ae` |
| `SELL` | `8.67` | `17132.0900` | 148,566.06 USD | 1,878,470.32 USD | `LARGE (>= USD 100K)` | `+0.92%` | `0x71d0e11ebb` |
| `SELL` | `8.67` | `11545.7100` | 100,139.41 USD | 3,156,329.39 USD | `LARGE (>= USD 100K)` | `+0.94%` | `0x881cd92459` |
| `SELL` | `8.67` | `1756.8400` | 15,227.06 USD | 3,918,038.76 USD | `STANDARD` | `+0.87%` | `0x57d8e75f47` |
| `SELL` | `8.67` | `1388.9900` | 12,045.32 USD | 4,454,452.37 USD | `STANDARD` | `+0.92%` | `0xd3943e4008` |
| `SELL` | `8.68` | `31331.6800` | 271,808.59 USD | 1,314,463.07 USD | `LARGE (>= USD 100K)` | `+0.96%` | `0x71cfa5e263` |
| `SELL` | `8.68` | `315.7300` | 2,740.85 USD | 5,018,401.09 USD | `STANDARD` | `+1.03%` | `0x07fd993f0f` |
| `SELL` | `8.69` | `4247.2800` | 36,924.58 USD | 3,653,678.82 USD | `MEDIUM (>= USD 25K)` | `+1.17%` | `0xa24c5ca26c` |
| `SELL` | `8.69` | `1337.4000` | 11,619.33 USD | 4,525,718.54 USD | `STANDARD` | `+1.11%` | `0x33ad48ed92` |
| `SELL` | `8.69` | `398.6500` | 3,465.74 USD | 4,971,589.58 USD | `STANDARD` | `+1.17%` | `0x14f8e04290` |
| `SELL` | `8.69` | `191.2300` | 1,662.34 USD | 5,065,731.62 USD | `STANDARD` | `+1.16%` | `0xdadbb4b2a0` |
| `SELL` | `8.69` | `83.5300` | 726.26 USD | 5,098,497.08 USD | `STANDARD` | `+1.18%` | `0x010461c14e` |
| `SELL` | `8.69` | `74.5900` | 648.52 USD | 5,191,169.98 USD | `STANDARD` | `+1.18%` | `0x31ca8395cf` |
| `SELL` | `8.70` | `7446.3500` | 64,783.99 USD | 3,553,476.10 USD | `MEDIUM (>= USD 25K)` | `+1.25%` | `0x71d0e11ebb` |
| `SELL` | `8.70` | `1840.1300` | 15,999.93 USD | 3,902,811.70 USD | `STANDARD` | `+1.19%` | `0x0efb38a5fa` |
| `SELL` | `8.70` | `1711.2200` | 14,890.35 USD | 4,401,408.42 USD | `STANDARD` | `+1.26%` | `0xd3943e4008` |
| `SELL` | `8.70` | `398.6500` | 3,469.97 USD | 4,964,655.32 USD | `STANDARD` | `+1.30%` | `0x14f8e04290` |
| `SELL` | `8.71` | `2120.5700` | 18,460.20 USD | 3,834,326.85 USD | `STANDARD` | `+1.31%` | `0xd3943e4008` |
| `SELL` | `8.72` | `17139.2400` | 149,373.62 USD | 1,729,904.27 USD | `LARGE (>= USD 100K)` | `+1.42%` | `0x71d0e11ebb` |
| `SELL` | `8.72` | `2178.6900` | 18,999.92 USD | 3,778,282.35 USD | `STANDARD` | `+1.49%` | `0x0efb38a5fa` |
| `SELL` | `8.73` | `397.2700` | 3,468.52 USD | 4,968,123.84 USD | `STANDARD` | `+1.61%` | `0x14f8e04290` |
| `SELL` | `8.74` | `315.7300` | 2,758.85 USD | 5,015,660.23 USD | `STANDARD` | `+1.69%` | `0x07fd993f0f` |
| `SELL` | `8.74` | `183.9900` | 1,608.16 USD | 5,067,339.78 USD | `STANDARD` | `+1.72%` | `0x010461c14e` |
| `SELL` | `8.74` | `174.8300` | 1,527.37 USD | 5,070,429.67 USD | `STANDARD` | `+1.67%` | `0x31ca8395cf` |
| `SELL` | `8.74` | `87.8600` | 767.81 USD | 5,091,800.10 USD | `STANDARD` | `+1.70%` | `0xdadbb4b2a0` |
| `SELL` | `8.76` | `60660.7100` | 531,600.13 USD | 531,600.13 USD | `LARGE (>= USD 100K)` | `+1.99%` | `0x71cfa5e263` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:32:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1459` | `0x7737...bf66` | `SHORT` | 1,471,024.55 USD | `171,568.06` | `7.43` | `8.58` | `112.04` | -195,479.53 USD | `-13.29%` | `10X Cross` |
| `1559` | `0xeadc...9d55` | `LONG` | 1,373,613.50 USD | `160,070.56` | `8.11` | `8.58` | `0.000000` | 75,975.92 USD | `+5.53%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `8.81` | 5,999.91 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 6.00K USD at 8.8138 USD [API] | `2026-10-29 14:01:56` |
| `ANNOUNCEMENT` | `INFO` | `8.81` | 5,668.07 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 5.67K USD at 8.8149 USD [API] | `2026-10-29 14:01:46` |
| `ANNOUNCEMENT` | `INFO` | `8.82` | 9,104.31 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 9.10K USD at 8.8185 USD [API] | `2026-10-29 14:07:26` |


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
| `Live` | `Long Liquidation` | `1.83` | 128.45 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 232.92 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 229.43 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 382.57 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 2,760.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 254.72 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 260.48 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 619.05 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 381.37 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 928.98 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 942.44 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 151.06 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 2,220.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 103.38 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 22,950.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 12,840.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 24,520.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 392.22 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.71` | 604.95 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.81` | 2,240.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.09` | 1,640.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.12` | 2,740.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 159.29 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.16` | 8,310.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 196.88 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.30` | 401.74 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 110.77 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 3,420.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,380.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,040.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 474.50 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.80` | 2,400.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 16,080.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 3,880.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 352.68 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 4,090.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 269.53 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 482.71 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 554.95 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 213.20 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 105.46 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.09` | 219.44 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 915.43 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 998.35 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 119.83 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 801.81 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.22` | 122.58 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 213.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 1,050.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.26` | 2,780.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.28` | 160,550.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 640.70 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.38` | 259.66 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 1,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 20,560.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 299.48 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 2,880.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.61` | 34,490.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 468.55 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 1,540.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.72` | 2,390.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 661.65 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 635.31 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 580.50 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.84` | 146.13 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.86` | 2,110.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 984.70 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 147.55 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 6,320.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.99` | 1,400.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 437.84 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,530.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 1,140.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.13` | 2,030.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 7,810.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 972.65 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 277.48 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 2,450.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 1,310.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 6,550.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.39` | 5,940.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 484.64 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 1,510.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 361,860.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 810,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 852.03 USD | 809,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 809,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.59` | 2,870.00 USD | 800,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 797,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 364.90 USD | 795,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.63` | 245.89 USD | 794,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.66` | 1,540.00 USD | 794,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.67` | 2,850.00 USD | 792,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.68` | 3,160.00 USD | 790,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.70` | 15,800.00 USD | 786,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 11,000.00 USD | 771,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 6,180.00 USD | 760,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 753,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 7,990.00 USD | 752,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 22,020.00 USD | 744,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 5,170.00 USD | 722,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 717,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 7,230.00 USD | 715,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 271.02 USD | 708,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 708,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 263.66 USD | 705,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 1,580.00 USD | 704,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 579.62 USD | 703,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.93` | 3,500.00 USD | 702,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 215.30 USD | 699,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 7,240.00 USD | 698,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 691,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.97` | 128,810.00 USD | 691,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 1,040.00 USD | 562,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.01` | 20,890.00 USD | 561,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.03` | 1,370.00 USD | 540,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.07` | 23,960.00 USD | 538,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 515,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,050.00 USD | 508,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.09` | 2,130.00 USD | 507,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,530.00 USD | 505,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 476,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 13,410.00 USD | 476,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,270.00 USD | 462,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.17` | 2,380.00 USD | 442,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 440,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 322.94 USD | 438,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.24` | 1,480.00 USD | 438,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 2,730.00 USD | 436,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 21,280.00 USD | 434,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.27` | 6,480,000.00 USD | 6,480,000.00 USD | 360.23 USD | 1,810.00 USD | 5,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,420.00 USD | 412,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 1,680.00 USD | 376,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.30` | 2,130.00 USD | 374,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.31` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 5,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.33` | 29,300.00 USD | 372,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 1,030.00 USD | 343,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 552.42 USD | 342,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.35` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 406.69 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.36` | 3,820.00 USD | 341,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.37` | 2,940.00 USD | 337,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.37` | 6,470,000.00 USD | 6,470,000.00 USD | 45,620.00 USD | 0.00 USD | 457.98 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.38` | 2,570.00 USD | 335,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 227.97 USD | 332,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.39` | 6,420,000.00 USD | 6,420,000.00 USD | 46,200.00 USD | 0.00 USD | 503.12 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.39` | 13,220.00 USD | 332,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.42` | 147.61 USD | 319,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 2,430.00 USD | 318,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 2,410.00 USD | 316,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.45` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 10,390.00 USD | 314,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 303,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 1,120.00 USD | 299,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.49` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 962.81 USD | 297,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 421.78 USD | 296,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.51` | 6,330,000.00 USD | 6,330,000.00 USD | 2,070.00 USD | 0.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.51` | 2,580.00 USD | 296,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.53` | 1,570.00 USD | 293,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.53` | 6,310,000.00 USD | 6,310,000.00 USD | 35,990.00 USD | 18,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 292,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.55` | 6,250,000.00 USD | 6,250,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.55` | 1,070.00 USD | 288,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.57` | 26,570.00 USD | 287,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 118.25 USD | 260,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.59` | 5,890,000.00 USD | 5,890,000.00 USD | 1,740.00 USD | 0.00 USD | 7,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.60` | 5,880,000.00 USD | 5,880,000.00 USD | 706.40 USD | 4,900.00 USD | 351.13 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.61` | 1,630.00 USD | 260,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.61` | 5,870,000.00 USD | 5,870,000.00 USD | 2,750.00 USD | 1,250.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.61` | 6,230,000.00 USD | 6,230,000.00 USD | 626.55 USD | 0.00 USD | 301.55 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 754.04 USD | 258,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 5,860,000.00 USD | 5,860,000.00 USD | 8,960.00 USD | 1,330.00 USD | 133.28 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 258,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.63` | 5,850,000.00 USD | 5,850,000.00 USD | 5,940.00 USD | 0.00 USD | 9,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.63` | 6,230,000.00 USD | 6,230,000.00 USD | 41,300.00 USD | 2,130.00 USD | 1,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 257,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 5,830,000.00 USD | 5,830,000.00 USD | 33,010.00 USD | 812.96 USD | 2,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.65` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 1,320.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.65` | 6,180,000.00 USD | 6,180,000.00 USD | 4,870.00 USD | 2,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 256,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.66` | 5,780,000.00 USD | 5,780,000.00 USD | 3,030.00 USD | 0.00 USD | 531.95 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 256.09 USD | 256,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.67` | 5,780,000.00 USD | 5,780,000.00 USD | 1,410.00 USD | 1,110.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.67` | 6,180,000.00 USD | 6,180,000.00 USD | 1,110.00 USD | 0.00 USD | 34,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 4,480.00 USD | 256,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.68` | 5,770,000.00 USD | 5,770,000.00 USD | 892.30 USD | 0.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.68` | 739.30 USD | 252,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.69` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 1,600.00 USD | 0.13 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.70` | 6,690.00 USD | 251,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 5,770,000.00 USD | 5,770,000.00 USD | 4,140.00 USD | 3,380.00 USD | 16,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.71` | 5,740,000.00 USD | 5,740,000.00 USD | 660.12 USD | 5,720.00 USD | 7,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.71` | 6,140,000.00 USD | 6,140,000.00 USD | 393.33 USD | 0.00 USD | 33,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.72` | 5,730,000.00 USD | 5,730,000.00 USD | 701.68 USD | 1,320.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.73` | 5,720,000.00 USD | 5,720,000.00 USD | 4,120.00 USD | 1,240.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.73` | 6,110,000.00 USD | 6,110,000.00 USD | 39,770.00 USD | 0.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.74` | 5,710,000.00 USD | 5,710,000.00 USD | 16,520.00 USD | 0.00 USD | 184.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.75` | 5,700,000.00 USD | 5,700,000.00 USD | 900.06 USD | 6,210.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.75` | 6,060,000.00 USD | 6,060,000.00 USD | 29,320.00 USD | 13,360.00 USD | 10,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 500.12 USD | 244,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.76` | 5,680,000.00 USD | 5,680,000.00 USD | 458.75 USD | 494.12 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 244,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.77` | 5,680,000.00 USD | 5,680,000.00 USD | 13,020.00 USD | 689.91 USD | 3,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.77` | 6,010,000.00 USD | 6,010,000.00 USD | 20,120.00 USD | 4,900.00 USD | 6,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.78` | 6,310.00 USD | 243,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 5,660,000.00 USD | 5,660,000.00 USD | 2,730.00 USD | 6,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,750.00 USD | 237,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.79` | 5,650,000.00 USD | 5,650,000.00 USD | 18,960.00 USD | 2,920.00 USD | 7,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.79` | 5,970,000.00 USD | 5,970,000.00 USD | 70,950.00 USD | 7,170.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 4,480.00 USD | 233,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 5,620,000.00 USD | 5,620,000.00 USD | 4,920.00 USD | 7,910.00 USD | 709.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 7,240.00 USD | 229,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.81` | 5,610,000.00 USD | 5,610,000.00 USD | 349.70 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.81` | 5,870,000.00 USD | 5,870,000.00 USD | 3,970.00 USD | 11,570.00 USD | 1,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.82` | 5,610,000.00 USD | 5,610,000.00 USD | 248.67 USD | 1,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.83` | 1,940.00 USD | 221,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.83` | 5,610,000.00 USD | 5,610,000.00 USD | 27,230.00 USD | 5,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.83` | 5,860,000.00 USD | 5,860,000.00 USD | 29,530.00 USD | 2,130.00 USD | 24,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.84` | 5,580,000.00 USD | 5,580,000.00 USD | 978.04 USD | 1,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 22,560.00 USD | 219,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.85` | 5,570,000.00 USD | 5,570,000.00 USD | 3,320.00 USD | 639.88 USD | 2,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.85` | 5,800,000.00 USD | 5,800,000.00 USD | 17,330.00 USD | 7,840.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.86` | 5,570,000.00 USD | 5,570,000.00 USD | 1,290.00 USD | 6,270.00 USD | 13,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 233.83 USD | 197,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.87` | 5,550,000.00 USD | 5,550,000.00 USD | 10,980.00 USD | 10,860.00 USD | 22,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.87` | 5,760,000.00 USD | 5,760,000.00 USD | 150,960.00 USD | 1,540.00 USD | 22,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 197,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 5,500,000.00 USD | 5,500,000.00 USD | 158,960.00 USD | 4,280.00 USD | 33,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.89` | 5,300,000.00 USD | 5,300,000.00 USD | 57,720.00 USD | 3,720.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.89` | 5,590,000.00 USD | 5,590,000.00 USD | 150,040.00 USD | 18,320.00 USD | 24,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.89` | 15,880.00 USD | 196,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.90` | 5,210,000.00 USD | 5,210,000.00 USD | 56,620.00 USD | 6,970.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 2,930.00 USD | 180,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 5,150,000.00 USD | 5,150,000.00 USD | 14,180.00 USD | 10,370.00 USD | 28,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.91` | 5,390,000.00 USD | 5,390,000.00 USD | 31,740.00 USD | 26,330.00 USD | 45,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.92` | 5,090,000.00 USD | 5,090,000.00 USD | 15,830.00 USD | 2,040.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 4,600.00 USD | 177,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 5,070,000.00 USD | 5,070,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.93` | 5,290,000.00 USD | 5,290,000.00 USD | 78,470.00 USD | 7,330.00 USD | 14,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 16,340.00 USD | 173,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 5,050,000.00 USD | 5,050,000.00 USD | 15,580.00 USD | 20,510.00 USD | 61,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 141.74 USD | 156,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 4,950,000.00 USD | 4,950,000.00 USD | 28,200.00 USD | 9,190.00 USD | 86,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.95` | 5,190,000.00 USD | 5,190,000.00 USD | 45,890.00 USD | 9,500.00 USD | 102,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 127,900.00 USD | 156,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 4,830,000.00 USD | 4,830,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.97` | 4,750,000.00 USD | 4,750,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.97` | 5,030,000.00 USD | 5,030,000.00 USD | 37,150.00 USD | 18,700.00 USD | 40,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.97` | 1,580.00 USD | 28,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.98` | 4,720,000.00 USD | 4,720,000.00 USD | 5,050.00 USD | 2,060.00 USD | 42,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,280.00 USD | 27,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 4,670,000.00 USD | 4,670,000.00 USD | 3,450.00 USD | 10,180.00 USD | 4,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.99` | 4,940,000.00 USD | 4,940,000.00 USD | 52,570.00 USD | 20,640.00 USD | 122,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 889.52 USD | 25,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 4,650,000.00 USD | 4,650,000.00 USD | 50,430.00 USD | 8,950.00 USD | 21,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 4,570,000.00 USD | 4,570,000.00 USD | 6,540.00 USD | 3,750.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.01` | 4,740,000.00 USD | 4,740,000.00 USD | 47,380.00 USD | 17,990.00 USD | 46,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 4,560,000.00 USD | 4,560,000.00 USD | 75,150.00 USD | 0.00 USD | 274.70 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 1,590.00 USD | 25,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 4,480,000.00 USD | 4,480,000.00 USD | 9,070.00 USD | 12,540.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.03` | 4,630,000.00 USD | 4,630,000.00 USD | 353,080.00 USD | 35,720.00 USD | 49,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.04` | 4,450,000.00 USD | 4,450,000.00 USD | 49,540.00 USD | 0.00 USD | 10,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.05` | 4,390,000.00 USD | 4,390,000.00 USD | 318,600.00 USD | 6,430.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.05` | 4,190,000.00 USD | 4,190,000.00 USD | 390,130.00 USD | 0.00 USD | 63,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.06` | 4,010,000.00 USD | 4,010,000.00 USD | 155,360.00 USD | 0.00 USD | 66,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 439.54 USD | 23,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 3,790,000.00 USD | 3,790,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.07` | 3,740,000.00 USD | 3,740,000.00 USD | 60,670.00 USD | 0.00 USD | 75,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.07` | 21,710.00 USD | 22,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.08` | 3,640,000.00 USD | 3,640,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.09` | 3,560,000.00 USD | 3,560,000.00 USD | 3,650.00 USD | 0.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.09` | 3,600,000.00 USD | 3,600,000.00 USD | 32,760.00 USD | 0.00 USD | 81,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.10` | 3,530,000.00 USD | 3,530,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.11` | 3,370,000.00 USD | 3,370,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.11` | 3,490,000.00 USD | 3,490,000.00 USD | 33,000.00 USD | 0.00 USD | 140,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 738.14 USD | 1,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 3,100,000.00 USD | 3,100,000.00 USD | 19,930.00 USD | 11,230.00 USD | 126,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 521.62 USD | 521.62 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.13` | 2,940,000.00 USD | 2,940,000.00 USD | 34,890.00 USD | 9,180.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.13` | 3,310,000.00 USD | 3,310,000.00 USD | 47,290.00 USD | 12,740.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 2,890,000.00 USD | 2,890,000.00 USD | 17,740.00 USD | 8,630.00 USD | 105,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 2,760,000.00 USD | 2,760,000.00 USD | 47,020.00 USD | 12,240.00 USD | 53,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.15` | 3,230,000.00 USD | 3,230,000.00 USD | 179,060.00 USD | 31,560.00 USD | 183,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 2,650,000.00 USD | 2,650,000.00 USD | 192.50 USD | 22,250.00 USD | 165,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.17` | 2,460,000.00 USD | 2,460,000.00 USD | 11,100.00 USD | 9,120.00 USD | 183,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.17` | 2,840,000.00 USD | 2,840,000.00 USD | 1,590.00 USD | 13,650.00 USD | 149,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 2,260,000.00 USD | 2,260,000.00 USD | 7,140.00 USD | 3,280.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.19` | 2,240,000.00 USD | 2,240,000.00 USD | 18,260.00 USD | 545.08 USD | 19,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.19` | 2,670,000.00 USD | 2,670,000.00 USD | 1,200.00 USD | 72,340.00 USD | 23,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.20` | 2,200,000.00 USD | 2,200,000.00 USD | 25,900.00 USD | 4,000.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.21` | 2,160,000.00 USD | 2,160,000.00 USD | 41,620.00 USD | 2,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.21` | 2,580,000.00 USD | 2,580,000.00 USD | 174,220.00 USD | 22,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.22` | 2,120,000.00 USD | 2,120,000.00 USD | 3,620.00 USD | 1,530.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.23` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 3,450.00 USD | 2,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.23` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 40,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.24` | 2,090,000.00 USD | 2,090,000.00 USD | 168.44 USD | 5,100.00 USD | 9,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.25` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 5,000.00 USD | 38,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.25` | 2,340,000.00 USD | 2,340,000.00 USD | 129,050.00 USD | 5,750.00 USD | 17,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.26` | 2,030,000.00 USD | 2,030,000.00 USD | 50,590.00 USD | 12,510.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.27` | 1,950,000.00 USD | 1,950,000.00 USD | 13,860.00 USD | 12,270.00 USD | 20,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.27` | 2,190,000.00 USD | 2,190,000.00 USD | 103,730.00 USD | 4,000.00 USD | 37,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.28` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 13,760.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.29` | 1,880,000.00 USD | 1,880,000.00 USD | 39,480.00 USD | 11,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.29` | 2,040,000.00 USD | 2,040,000.00 USD | 166,800.00 USD | 6,550.00 USD | 21,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.30` | 1,830,000.00 USD | 1,830,000.00 USD | 69,220.00 USD | 13,810.00 USD | 20,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.31` | 1,730,000.00 USD | 1,730,000.00 USD | 82,900.00 USD | 11,920.00 USD | 56,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.31` | 1,850,000.00 USD | 1,850,000.00 USD | 370,260.00 USD | 10,660.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.32` | 1,580,000.00 USD | 1,580,000.00 USD | 80,060.00 USD | 6,080.00 USD | 14,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 8,710.00 USD | 109.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.33` | 1,460,000.00 USD | 1,460,000.00 USD | 14,600.00 USD | 11,770.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.34` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 3,230.00 USD | 13.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 23,440.00 USD | 25,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.35` | 1,430,000.00 USD | 1,430,000.00 USD | 223,170.00 USD | 0.00 USD | 5,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.36` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 1,090.00 USD | 25,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.37` | 1,390,000.00 USD | 1,390,000.00 USD | 691.75 USD | 14,420.00 USD | 16.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.37` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 36,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.38` | 1,380,000.00 USD | 1,380,000.00 USD | 17,220.00 USD | 7,830.00 USD | 50,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.39` | 1,300,000.00 USD | 1,300,000.00 USD | 107,990.00 USD | 16,670.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.39` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 7,600.00 USD | 68,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.40` | 1,140,000.00 USD | 1,140,000.00 USD | 10,500.00 USD | 10,400.00 USD | 56,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.41` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 10,190.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.41` | 1,090,000.00 USD | 1,090,000.00 USD | 194,850.00 USD | 0.00 USD | 89,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.42` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 16,260.00 USD | 42,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.43` | 977,590.00 USD | 977,590.00 USD | 81,350.00 USD | 7,730.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.43` | 806,530.00 USD | 806,530.00 USD | 163,340.00 USD | 0.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.44` | 880,970.00 USD | 880,970.00 USD | 11,130.00 USD | 32,380.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.45` | 676,990.00 USD | 676,990.00 USD | 54,790.00 USD | 5,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.45` | 620,350.00 USD | 620,350.00 USD | 156,410.00 USD | 8,000.00 USD | 171,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.47` | 616,240.00 USD | 616,240.00 USD | 663.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.47` | 284,390.00 USD | 284,390.00 USD | 0.00 USD | 0.00 USD | 38,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.48` | 615,570.00 USD | 615,570.00 USD | 749.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.49` | 614,820.00 USD | 614,820.00 USD | 0.00 USD | 0.00 USD | 12.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.49` | 245,650.00 USD | 245,650.00 USD | 0.00 USD | 0.00 USD | 153,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.51` | 92,390.00 USD | 92,390.00 USD | 0.00 USD | 0.00 USD | 92,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.52` | 614,810.00 USD | 614,810.00 USD | 158,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.53` | 456,180.00 USD | 456,180.00 USD | 24,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.53` | 174,760.00 USD | 174,760.00 USD | 173,370.00 USD | 0.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.53` | 349,520.00 USD | 349,520.00 USD | 173,370.00 USD | 0.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.54` | 432,000.00 USD | 432,000.00 USD | 198,250.00 USD | 0.00 USD | 156.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.55` | 233,590.00 USD | 233,590.00 USD | 1,650.00 USD | 0.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.55` | 865,520.00 USD | 865,520.00 USD | 434,770.00 USD | 80,630.00 USD | 601.43 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.56` | 206,810.00 USD | 206,810.00 USD | 686.73 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.57` | 206,130.00 USD | 206,130.00 USD | 147,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.57` | 991,800.00 USD | 991,800.00 USD | 9,740.00 USD | 115,860.00 USD | 678.07 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.58` | 59,120.00 USD | 59,120.00 USD | 59,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.59` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 90,970.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.60` | 2,040.00 USD | 2,040.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.61` | 3,230.00 USD | 3,230.00 USD | 497.00 USD | 0.00 USD | 699.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.61` | 1,090,000.00 USD | 1,090,000.00 USD | 2,810.00 USD | 0.00 USD | 271.28 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.62` | 170,510.00 USD | 170,510.00 USD | 41,980.00 USD | 0.00 USD | 125,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.63` | 302,210.00 USD | 302,210.00 USD | 129,280.00 USD | 2,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.63` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 384,180.00 USD | 384,180.00 USD | 69,220.00 USD | 9,340.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.65` | 446,290.00 USD | 446,290.00 USD | 35,830.00 USD | 9,010.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.65` | 1,170,000.00 USD | 1,170,000.00 USD | 40,260.00 USD | 10,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.66` | 475,590.00 USD | 475,590.00 USD | 13,240.00 USD | 2,020.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.67` | 488,990.00 USD | 488,990.00 USD | 880.60 USD | 12,460.00 USD | 56.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.67` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 11,770.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 528,510.00 USD | 528,510.00 USD | 588.00 USD | 13,040.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.69` | 209.31 USD | 209.31 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.69` | 604,370.00 USD | 604,370.00 USD | 10,820.00 USD | 22,830.00 USD | 42,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.69` | 1,420,000.00 USD | 1,420,000.00 USD | 29,260.00 USD | 48,960.00 USD | 162,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.70` | 698,890.00 USD | 698,890.00 USD | 62,600.00 USD | 1,090.00 USD | 30,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.71` | 725,580.00 USD | 725,580.00 USD | 18,700.00 USD | 7,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.71` | 1,520,000.00 USD | 1,520,000.00 USD | 87,110.00 USD | 11,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 814,830.00 USD | 814,830.00 USD | 34,050.00 USD | 4,410.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.73` | 899,130.00 USD | 899,130.00 USD | 19,820.00 USD | 31,860.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.73` | 1,580,000.00 USD | 1,580,000.00 USD | 51,030.00 USD | 10,790.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 962,120.00 USD | 962,120.00 USD | 38,500.00 USD | 6,910.00 USD | 17,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.75` | 1,030,000.00 USD | 1,030,000.00 USD | 33,520.00 USD | 12,720.00 USD | 23,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.75` | 1,830,000.00 USD | 1,830,000.00 USD | 196,960.00 USD | 19,690.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.76` | 1,180,000.00 USD | 1,180,000.00 USD | 82,470.00 USD | 10,010.00 USD | 57,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.77` | 1,380,000.00 USD | 1,380,000.00 USD | 155,740.00 USD | 2,060.00 USD | 43,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.77` | 2,080,000.00 USD | 2,080,000.00 USD | 141,710.00 USD | 0.00 USD | 105,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.78` | 1,500,000.00 USD | 1,500,000.00 USD | 41,500.00 USD | 25,510.00 USD | 50,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.79` | 1,580,000.00 USD | 1,580,000.00 USD | 31,710.00 USD | 17,970.00 USD | 31,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.79` | 2,210,000.00 USD | 2,210,000.00 USD | 29,660.00 USD | 33,300.00 USD | 65,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.80` | 1,740,000.00 USD | 1,740,000.00 USD | 113,160.00 USD | 19,150.00 USD | 23,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.81` | 1,800,000.00 USD | 1,800,000.00 USD | 53,290.00 USD | 9,030.00 USD | 1,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.81` | 2,420,000.00 USD | 2,420,000.00 USD | 122,920.00 USD | 26,890.00 USD | 58,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.82` | 1,890,000.00 USD | 1,890,000.00 USD | 19,950.00 USD | 4,510.00 USD | 61,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.82` | 6,000.00 USD | 6,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.83` | 2,090,000.00 USD | 2,090,000.00 USD | 174,730.00 USD | 19,400.00 USD | 7,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.83` | 2,660,000.00 USD | 2,660,000.00 USD | 242,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 2,150,000.00 USD | 2,150,000.00 USD | 1,500.00 USD | 4,360.00 USD | 59,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 2,180,000.00 USD | 2,180,000.00 USD | 13,040.00 USD | 3,870.00 USD | 11,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.85` | 2,750,000.00 USD | 2,750,000.00 USD | 29,310.00 USD | 5,880.00 USD | 58,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 2,190,000.00 USD | 2,190,000.00 USD | 2,060.00 USD | 3,280.00 USD | 4,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.87` | 1,160.00 USD | 7,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.87` | 2,210,000.00 USD | 2,210,000.00 USD | 1,410.00 USD | 545.08 USD | 12,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.87` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 2,220,000.00 USD | 2,220,000.00 USD | 803.70 USD | 14,670.00 USD | 186.36 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.88` | 691.70 USD | 8,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.89` | 2,270,000.00 USD | 2,270,000.00 USD | 13,040.00 USD | 4,360.00 USD | 32,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.89` | 2,850,000.00 USD | 2,850,000.00 USD | 1,250.00 USD | 0.00 USD | 73,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 2,380,000.00 USD | 2,380,000.00 USD | 32,320.00 USD | 7,510.00 USD | 65,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.91` | 2,440,000.00 USD | 2,440,000.00 USD | 32,240.00 USD | 13,320.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.91` | 2,940,000.00 USD | 2,940,000.00 USD | 2,440.00 USD | 0.00 USD | 88,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 2,450,000.00 USD | 2,450,000.00 USD | 1,110.00 USD | 5,100.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 2,530,000.00 USD | 2,530,000.00 USD | 31,830.00 USD | 6,810.00 USD | 38,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.93` | 3,120,000.00 USD | 3,120,000.00 USD | 157,480.00 USD | 0.00 USD | 17,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 2,600,000.00 USD | 2,600,000.00 USD | 50,590.00 USD | 12,260.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.95` | 2,630,000.00 USD | 2,630,000.00 USD | 3,080.00 USD | 6,630.00 USD | 20,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.95` | 3,240,000.00 USD | 3,240,000.00 USD | 74,920.00 USD | 4,000.00 USD | 38,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.96` | 2,630,000.00 USD | 2,630,000.00 USD | 1,260.00 USD | 2,980.00 USD | 175.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.97` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.26 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.97` | 3,240,000.00 USD | 3,240,000.00 USD | 1,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.97` | 10,480.00 USD | 18,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.98` | 2,700,000.00 USD | 2,700,000.00 USD | 35,320.00 USD | 9,420.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 2,770,000.00 USD | 2,770,000.00 USD | 48,380.00 USD | 22,110.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.99` | 3,420,000.00 USD | 3,420,000.00 USD | 145,880.00 USD | 6,550.00 USD | 28,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.99` | 539,710.00 USD | 558,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.00` | 2,830,000.00 USD | 2,830,000.00 USD | 36,960.00 USD | 0.00 USD | 24,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 2,910,000.00 USD | 2,910,000.00 USD | 49,510.00 USD | 14,940.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.01` | 3,780,000.00 USD | 3,780,000.00 USD | 303,030.00 USD | 36,180.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 2,990,000.00 USD | 2,990,000.00 USD | 39,170.00 USD | 29,440.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 3,160,000.00 USD | 3,160,000.00 USD | 125,760.00 USD | 10,300.00 USD | 34,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.03` | 4,010,000.00 USD | 4,010,000.00 USD | 107,490.00 USD | 101,140.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 3,220,000.00 USD | 3,220,000.00 USD | 41,710.00 USD | 5,900.00 USD | 14,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 3,270,000.00 USD | 3,270,000.00 USD | 21,980.00 USD | 7,560.00 USD | 22,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.05` | 4,100,000.00 USD | 4,100,000.00 USD | 38,740.00 USD | 17,700.00 USD | 39,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.05` | 213.70 USD | 558,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.06` | 3,320,000.00 USD | 3,320,000.00 USD | 28,180.00 USD | 5,480.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 3,370,000.00 USD | 3,370,000.00 USD | 13,070.00 USD | 15,350.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.07` | 4,160,000.00 USD | 4,160,000.00 USD | 3,990.00 USD | 14,140.00 USD | 36,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 3,410,000.00 USD | 3,410,000.00 USD | 12,960.00 USD | 1,040.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 3,510,000.00 USD | 3,510,000.00 USD | 71,230.00 USD | 9,730.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.09` | 4,460,000.00 USD | 4,460,000.00 USD | 152,640.00 USD | 8,680.00 USD | 144,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.10` | 3,890.00 USD | 562,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.10` | 3,570,000.00 USD | 3,570,000.00 USD | 16,320.00 USD | 10,640.00 USD | 30,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 3,720,000.00 USD | 3,720,000.00 USD | 51,080.00 USD | 14,420.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.11` | 5,950,000.00 USD | 5,950,000.00 USD | 877,120.00 USD | 37,620.00 USD | 570,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 3,860,000.00 USD | 3,860,000.00 USD | 94,400.00 USD | 21,650.00 USD | 26,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 3,990,000.00 USD | 3,990,000.00 USD | 75,260.00 USD | 15,960.00 USD | 35,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.13` | 7,130,000.00 USD | 7,130,000.00 USD | 666,880.00 USD | 26,540.00 USD | 484,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.14` | 4,050,000.00 USD | 4,050,000.00 USD | 30,520.00 USD | 2,600.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.14` | 180.80 USD | 562,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.15` | 4,150,000.00 USD | 4,150,000.00 USD | 56,980.00 USD | 20,890.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.15` | 7,790,000.00 USD | 7,790,000.00 USD | 357,020.00 USD | 38,700.00 USD | 270,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 4,270,000.00 USD | 4,270,000.00 USD | 63,930.00 USD | 23,900.00 USD | 32,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 4,400,000.00 USD | 4,400,000.00 USD | 74,820.00 USD | 3,200.00 USD | 49,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.17` | 8,640,000.00 USD | 8,640,000.00 USD | 409,650.00 USD | 133,490.00 USD | 303,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 4,480,000.00 USD | 4,480,000.00 USD | 28,310.00 USD | 26,430.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 4,600,000.00 USD | 4,600,000.00 USD | 77,890.00 USD | 29,140.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.19` | 9,440,000.00 USD | 9,440,000.00 USD | 504,150.00 USD | 108,440.00 USD | 193,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.20` | 4,710,000.00 USD | 4,710,000.00 USD | 64,910.00 USD | 11,090.00 USD | 37,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 4,750,000.00 USD | 4,750,000.00 USD | 30,000.00 USD | 2,950.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.21` | 10,460,000.00 USD | 10,460,000.00 USD | 590,780.00 USD | 144,470.00 USD | 277,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.22` | 4,820,000.00 USD | 4,820,000.00 USD | 58,470.00 USD | 2,850.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 4,820,000.00 USD | 4,820,000.00 USD | 471.32 USD | 4,270.00 USD | 17.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.23` | 11,460,000.00 USD | 11,460,000.00 USD | 582,450.00 USD | 92,780.00 USD | 331,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.23` | 225.43 USD | 562,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.24` | 4,870,000.00 USD | 4,870,000.00 USD | 45,580.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 4,910,000.00 USD | 4,910,000.00 USD | 17,240.00 USD | 5,840.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.25` | 11,860,000.00 USD | 11,860,000.00 USD | 277,290.00 USD | 61,940.00 USD | 61,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 4,910,000.00 USD | 4,910,000.00 USD | 574.60 USD | 0.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 4,940,000.00 USD | 4,940,000.00 USD | 23,430.00 USD | 1,360.00 USD | 6,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.27` | 12,160,000.00 USD | 12,160,000.00 USD | 156,190.00 USD | 102,670.00 USD | 37,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.28` | 1,750.00 USD | 564,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.28` | 4,950,000.00 USD | 4,950,000.00 USD | 1,610.00 USD | 8,760.00 USD | 169.17 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.29` | 4,990,000.00 USD | 4,990,000.00 USD | 16,070.00 USD | 4,140.00 USD | 17,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.29` | 12,880,000.00 USD | 12,880,000.00 USD | 392,980.00 USD | 82,050.00 USD | 244,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 3,860.00 USD | 568,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.30` | 5,050,000.00 USD | 5,050,000.00 USD | 39,880.00 USD | 7,520.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 5,100,000.00 USD | 5,100,000.00 USD | 28,930.00 USD | 5,500.00 USD | 12,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.31` | 13,450,000.00 USD | 13,450,000.00 USD | 308,150.00 USD | 55,090.00 USD | 209,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 5,120,000.00 USD | 5,120,000.00 USD | 17,660.00 USD | 1,330.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 5,150,000.00 USD | 5,150,000.00 USD | 12,710.00 USD | 6,000.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.33` | 13,780,000.00 USD | 13,780,000.00 USD | 134,040.00 USD | 57,370.00 USD | 139,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 5,200,000.00 USD | 5,200,000.00 USD | 46,100.00 USD | 3,660.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.35` | 5,230,000.00 USD | 5,230,000.00 USD | 13,620.00 USD | 1,320.00 USD | 14,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.35` | 14,060,000.00 USD | 14,060,000.00 USD | 114,090.00 USD | 67,130.00 USD | 96,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 5,250,000.00 USD | 5,250,000.00 USD | 4,730.00 USD | 6,760.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 5,280,000.00 USD | 5,280,000.00 USD | 13,170.00 USD | 6,780.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.37` | 14,390,000.00 USD | 14,390,000.00 USD | 211,790.00 USD | 34,660.00 USD | 85,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 5,310,000.00 USD | 5,310,000.00 USD | 15,290.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.39` | 5,320,000.00 USD | 5,320,000.00 USD | 8,850.00 USD | 1,600.00 USD | 12.83 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.39` | 14,720,000.00 USD | 14,720,000.00 USD | 206,980.00 USD | 32,960.00 USD | 87,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 5,340,000.00 USD | 5,340,000.00 USD | 22,270.00 USD | 0.00 USD | 12.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 5,360,000.00 USD | 5,360,000.00 USD | 4,410.00 USD | 378.69 USD | 10,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.41` | 15,120,000.00 USD | 15,120,000.00 USD | 265,720.00 USD | 30,790.00 USD | 99,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 440.06 USD | 568,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 5,380,000.00 USD | 5,380,000.00 USD | 9,240.00 USD | 3,010.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.43` | 5,380,000.00 USD | 5,380,000.00 USD | 5,380.00 USD | 1,380.00 USD | 25.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.43` | 15,210,000.00 USD | 15,210,000.00 USD | 33,890.00 USD | 13,430.00 USD | 42,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 1,320.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 1,240.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.45` | 15,290,000.00 USD | 15,290,000.00 USD | 68,680.00 USD | 9,040.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.46` | 5,410,000.00 USD | 5,410,000.00 USD | 16,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.47` | 15,360,000.00 USD | 15,360,000.00 USD | 44,170.00 USD | 5,760.00 USD | 12,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.49` | 15,400,000.00 USD | 15,400,000.00 USD | 25,360.00 USD | 10,200.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.51` | 15,530,000.00 USD | 15,530,000.00 USD | 57,130.00 USD | 21,130.00 USD | 54,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.53` | 15,590,000.00 USD | 15,590,000.00 USD | 50,200.00 USD | 9,410.00 USD | 1,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.55` | 15,620,000.00 USD | 15,620,000.00 USD | 11,560.00 USD | 11,570.00 USD | 880.26 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.57` | 15,670,000.00 USD | 15,670,000.00 USD | 31,530.00 USD | 2,130.00 USD | 24,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.59` | 15,710,000.00 USD | 15,710,000.00 USD | 14,070.00 USD | 7,840.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.61` | 15,760,000.00 USD | 15,760,000.00 USD | 37,000.00 USD | 0.00 USD | 11,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.62` | 138.98 USD | 568,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.64` | 1,930.00 USD | 570,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.68` | 319.28 USD | 571,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.69` | 2,600.00 USD | 573,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 573,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.88` | 371.77 USD | 574,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.10` | 119.83 USD | 574,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 2,650.00 USD | 577,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.43` | 20,850.00 USD | 597,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 598,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.78` | 173.91 USD | 598,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.81` | 1,150.00 USD | 599,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 606,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.04` | 55,230.00 USD | 662,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.26` | 112,550.00 USD | 774,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,670.00 USD | 786,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.36` | 4,270.00 USD | 790,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 802,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.69` | 297,090.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.71` | 280.45 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.93` | 505.74 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,050.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.38` | 57,090.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.46` | 1,700.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.65` | 240.49 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.94` | 321.85 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.96` | 75,340.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.09` | 219.34 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.10` | 4,190.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.30` | 549.30 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.39` | 20,010.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.77` | 185.55 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.82` | 1,700.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.16` | 240.86 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.39` | 265,570.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.57` | 23,450.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.59` | 117.92 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.73` | 1,940.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `Sell Stop` | `2.33` | 392,740.00 USD | 0.00 USD | 611.73 USD | `-72.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 392,120.00 USD | 0.00 USD | 793.75 USD | `-53.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 391,330.00 USD | 0.00 USD | 67,970.00 USD | `-41.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 323,360.00 USD | 0.00 USD | 205.30 USD | `-38.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 323,160.00 USD | 0.00 USD | 465.42 USD | `-36.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 322,690.00 USD | 0.00 USD | 349.35 USD | `-36.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 322,340.00 USD | 0.00 USD | 1,020.00 USD | `-35.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 321,330.00 USD | 0.00 USD | 1,330.00 USD | `-32.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 320,000.00 USD | 0.00 USD | 493.50 USD | `-31.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 319,510.00 USD | 0.00 USD | 100.98 USD | `-30.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 319,400.00 USD | 0.00 USD | 500.70 USD | `-30.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 318,900.00 USD | 0.00 USD | 4,160.00 USD | `-29.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 314,750.00 USD | 0.00 USD | 6,500.00 USD | `-28.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.21` | 308,250.00 USD | 0.00 USD | 906.18 USD | `-27.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.25` | 307,340.00 USD | 0.00 USD | 127.35 USD | `-27.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 307,210.00 USD | 0.00 USD | 864.38 USD | `-26.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 306,350.00 USD | 0.00 USD | 130.10 USD | `-24.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 306,220.00 USD | 0.00 USD | 4,340.00 USD | `-24.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 301,880.00 USD | 0.00 USD | 5,520.00 USD | `-22.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 296,360.00 USD | 0.00 USD | 203.67 USD | `-21.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 296,150.00 USD | 0.00 USD | 296.34 USD | `-21.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 295,860.00 USD | 0.00 USD | 921.19 USD | `-21.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 294,930.00 USD | 0.00 USD | 709.98 USD | `-19.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.91` | 294,220.00 USD | 0.00 USD | 4,630.00 USD | `-19.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 289,600.00 USD | 0.00 USD | 691.50 USD | `-19.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 288,910.00 USD | 0.00 USD | 262.44 USD | `-19.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 288,640.00 USD | 0.00 USD | 24,350.00 USD | `-18.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.04` | 264,290.00 USD | 0.00 USD | 653.69 USD | `-18.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.11` | 263,640.00 USD | 0.00 USD | 187.79 USD | `-17.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 263,450.00 USD | 0.00 USD | 6,790.00 USD | `-16.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 256,660.00 USD | 0.00 USD | 4,960.00 USD | `-16.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.21` | 251,700.00 USD | 0.00 USD | 7,210.00 USD | `-16.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 244,500.00 USD | 0.00 USD | 282.74 USD | `-15.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 244,210.00 USD | 0.00 USD | 603.44 USD | `-15.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 243,610.00 USD | 0.00 USD | 464.61 USD | `-15.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 243,140.00 USD | 0.00 USD | 2,090.00 USD | `-15.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 241,050.00 USD | 0.00 USD | 129.58 USD | `-14.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 240,920.00 USD | 0.00 USD | 114.65 USD | `-14.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.39` | 240,810.00 USD | 0.00 USD | 702.75 USD | `-14.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.41` | 240,100.00 USD | 0.00 USD | 4,630.00 USD | `-13.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 235,470.00 USD | 0.00 USD | 199.39 USD | `-13.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 235,270.00 USD | 0.00 USD | 6,270.00 USD | `-13.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 229,010.00 USD | 0.00 USD | 37,420.00 USD | `-12.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 191,580.00 USD | 0.00 USD | 2,120.00 USD | `-12.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 189,460.00 USD | 0.00 USD | 799.83 USD | `-12.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 188,660.00 USD | 0.00 USD | 820.44 USD | `-12.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 187,840.00 USD | 0.00 USD | 218.24 USD | `-11.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 187,620.00 USD | 0.00 USD | 113.78 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.61` | 187,510.00 USD | 0.00 USD | 152.10 USD | `-11.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 187,360.00 USD | 0.00 USD | 297.59 USD | `-11.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.68` | 187,060.00 USD | 0.00 USD | 528.88 USD | `-10.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 186,530.00 USD | 0.00 USD | 360.13 USD | `-10.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 186,170.00 USD | 0.00 USD | 578.04 USD | `-10.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 185,590.00 USD | 0.00 USD | 106.32 USD | `-9.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.79` | 185,480.00 USD | 0.00 USD | 424.05 USD | `-9.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 185,060.00 USD | 0.00 USD | 1,170.00 USD | `-9.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.82` | 183,890.00 USD | 0.00 USD | 3,940.00 USD | `-9.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.83` | 179,950.00 USD | 0.00 USD | 154.70 USD | `-9.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 179,800.00 USD | 0.00 USD | 115.23 USD | `-8.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 179,680.00 USD | 0.00 USD | 183.33 USD | `-8.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 179,500.00 USD | 0.00 USD | 1,890.00 USD | `-8.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 177,600.00 USD | 0.00 USD | 6,840.00 USD | `-8.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 170,760.00 USD | 0.00 USD | 5,710.00 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 165,060.00 USD | 0.00 USD | 1,590.00 USD | `-7.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 163,470.00 USD | 0.00 USD | 898.42 USD | `-7.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 162,570.00 USD | 0.00 USD | 7,960.00 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 154,620.00 USD | 0.00 USD | 246.52 USD | `-7.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.97` | 154,370.00 USD | 0.00 USD | 2,420.00 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 151,950.00 USD | 0.00 USD | 1,440.00 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 150,510.00 USD | 0.00 USD | 435.73 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 150,080.00 USD | 0.00 USD | 4,320.00 USD | `-6.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 145,760.00 USD | 0.00 USD | 123.58 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 145,630.00 USD | 0.00 USD | 796.62 USD | `-6.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 144,840.00 USD | 0.00 USD | 152.56 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.06` | 144,690.00 USD | 0.00 USD | 2,730.00 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 141,960.00 USD | 0.00 USD | 121.69 USD | `-6.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.09` | 141,830.00 USD | 0.00 USD | 5,230.00 USD | `-6.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 136,600.00 USD | 0.00 USD | 477.36 USD | `-5.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 136,120.00 USD | 0.00 USD | 16,210.00 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 119,910.00 USD | 0.00 USD | 744.88 USD | `-5.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 119,170.00 USD | 0.00 USD | 6,500.00 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 112,670.00 USD | 0.00 USD | 884.60 USD | `-5.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 111,780.00 USD | 0.00 USD | 5,550.00 USD | `-5.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 106,230.00 USD | 0.00 USD | 121.51 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 106,110.00 USD | 0.00 USD | 3,080.00 USD | `-5.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 103,030.00 USD | 0.00 USD | 520.75 USD | `-4.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 102,510.00 USD | 0.00 USD | 3,020.00 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 99,480.00 USD | 0.00 USD | 141.04 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 99,340.00 USD | 0.00 USD | 22,560.00 USD | `-4.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 76,780.00 USD | 0.00 USD | 515.66 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.22` | 76,260.00 USD | 0.00 USD | 139.74 USD | `-4.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 76,120.00 USD | 0.00 USD | 490.15 USD | `-4.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.24` | 75,630.00 USD | 0.00 USD | 197.96 USD | `-4.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.26` | 75,430.00 USD | 0.00 USD | 9,640.00 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.27` | 65,800.00 USD | 0.00 USD | 535.65 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 65,260.00 USD | 0.00 USD | 734.99 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 64,530.00 USD | 0.00 USD | 828.50 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 63,700.00 USD | 0.00 USD | 311.97 USD | `-3.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 63,390.00 USD | 0.00 USD | 5,380.00 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 58,010.00 USD | 0.00 USD | 245.13 USD | `-3.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.32` | 57,770.00 USD | 0.00 USD | 1,690.00 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 56,070.00 USD | 0.00 USD | 408.58 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 55,660.00 USD | 0.00 USD | 808.63 USD | `-2.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 54,860.00 USD | 0.00 USD | 4,070.00 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.37` | 50,790.00 USD | 0.00 USD | 24,090.00 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 26,700.00 USD | 0.00 USD | 1,140.00 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 25,550.00 USD | 0.00 USD | 419.25 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 25,130.00 USD | 0.00 USD | 376.68 USD | `-2.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 24,760.00 USD | 0.00 USD | 4,240.00 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 20,520.00 USD | 0.00 USD | 314.81 USD | `-2.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 20,210.00 USD | 0.00 USD | 198.83 USD | `-2.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 20,010.00 USD | 0.00 USD | 195.52 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 19,810.00 USD | 0.00 USD | 138.24 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 19,670.00 USD | 0.00 USD | 710.81 USD | `-1.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 18,960.00 USD | 0.00 USD | 769.61 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.48` | 18,190.00 USD | 0.00 USD | 777.14 USD | `-1.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.49` | 17,420.00 USD | 0.00 USD | 408.78 USD | `-1.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.51` | 17,010.00 USD | 0.00 USD | 122.47 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.52` | 16,890.00 USD | 0.00 USD | 1,160.00 USD | `-1.00%` | `TACTICAL (Retail Cluster)` |
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
| `Buy Stop` | `8.63` | 557.20 USD | 201.97 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 2,850.00 USD | 2,290.00 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 3,720.00 USD | 877.88 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 3,920.00 USD | 200.85 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 4,100.00 USD | 176.62 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 5,090.00 USD | 990.09 USD | 0.00 USD | `+0.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 5,920.00 USD | 830.81 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 24,880.00 USD | 18,950.00 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 25,280.00 USD | 399.67 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 25,700.00 USD | 421.85 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 25,940.00 USD | 239.51 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 30,310.00 USD | 4,370.00 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 34,050.00 USD | 3,740.00 USD | 0.00 USD | `+1.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 34,230.00 USD | 173.28 USD | 0.00 USD | `+1.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 34,440.00 USD | 215.16 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 34,830.00 USD | 388.12 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 35,540.00 USD | 711.78 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 36,100.00 USD | 563.87 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 36,350.00 USD | 243.40 USD | 0.00 USD | `+2.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 36,520.00 USD | 168.05 USD | 0.00 USD | `+2.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 36,860.00 USD | 339.94 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 37,170.00 USD | 310.98 USD | 0.00 USD | `+3.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 37,280.00 USD | 110.58 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 38,140.00 USD | 860.96 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 40,070.00 USD | 1,930.00 USD | 0.00 USD | `+3.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 40,860.00 USD | 788.72 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 42,660.00 USD | 1,800.00 USD | 0.00 USD | `+3.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 42,830.00 USD | 163.33 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 43,610.00 USD | 782.17 USD | 0.00 USD | `+3.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 43,830.00 USD | 223.62 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 581,140.00 USD | 537,310.00 USD | 0.00 USD | `+4.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 581,540.00 USD | 401.63 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 896,700.00 USD | 315,150.00 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 897,030.00 USD | 338.30 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 897,290.00 USD | 260.96 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 897,510.00 USD | 220.06 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 898,600.00 USD | 1,090.00 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 899,220.00 USD | 616.37 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 899,320.00 USD | 102.03 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 899,770.00 USD | 453.84 USD | 0.00 USD | `+5.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 899,940.00 USD | 160.99 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 900,150.00 USD | 215.98 USD | 0.00 USD | `+5.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 901,660.00 USD | 1,510.00 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 902,110.00 USD | 451.48 USD | 0.00 USD | `+5.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 902,250.00 USD | 139.58 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 903,540.00 USD | 1,290.00 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 903,710.00 USD | 166.53 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 905,710.00 USD | 2,000.00 USD | 0.00 USD | `+6.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 1,300,000.00 USD | 394,210.00 USD | 0.00 USD | `+6.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,300,000.00 USD | 119.24 USD | 0.00 USD | `+6.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,300,000.00 USD | 3,020.00 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,300,000.00 USD | 131.87 USD | 0.00 USD | `+7.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,300,000.00 USD | 149.17 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,310,000.00 USD | 2,220.00 USD | 0.00 USD | `+7.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,540,000.00 USD | 231,380.00 USD | 0.00 USD | `+7.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,540,000.00 USD | 1,960.00 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,540,000.00 USD | 434.45 USD | 0.00 USD | `+8.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,560,000.00 USD | 18,610.00 USD | 0.00 USD | `+8.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,560,000.00 USD | 166.83 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,560,000.00 USD | 674.29 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,560,000.00 USD | 101.58 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,560,000.00 USD | 109.36 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,560,000.00 USD | 116.69 USD | 0.00 USD | `+8.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,560,000.00 USD | 163.41 USD | 0.00 USD | `+8.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,560,000.00 USD | 102.01 USD | 0.00 USD | `+9.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,560,000.00 USD | 102.12 USD | 0.00 USD | `+9.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,560,000.00 USD | 714.59 USD | 0.00 USD | `+9.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,560,000.00 USD | 928.13 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,560,000.00 USD | 102.45 USD | 0.00 USD | `+9.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,560,000.00 USD | 219.84 USD | 0.00 USD | `+9.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,560,000.00 USD | 311.69 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,560,000.00 USD | 1,890.00 USD | 0.00 USD | `+9.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,560,000.00 USD | 1,130.00 USD | 0.00 USD | `+10.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,570,000.00 USD | 288.46 USD | 0.00 USD | `+10.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,570,000.00 USD | 119.92 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,570,000.00 USD | 231.00 USD | 0.00 USD | `+11.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,570,000.00 USD | 221.07 USD | 0.00 USD | `+11.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,570,000.00 USD | 992.00 USD | 0.00 USD | `+11.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,570,000.00 USD | 148.48 USD | 0.00 USD | `+12.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,570,000.00 USD | 191.36 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,570,000.00 USD | 4,440.00 USD | 0.00 USD | `+12.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,570,000.00 USD | 108.21 USD | 0.00 USD | `+12.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,570,000.00 USD | 169.68 USD | 0.00 USD | `+13.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,570,000.00 USD | 574.66 USD | 0.00 USD | `+13.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,570,000.00 USD | 121.87 USD | 0.00 USD | `+13.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,570,000.00 USD | 115.88 USD | 0.00 USD | `+14.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,570,000.00 USD | 340.05 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,570,000.00 USD | 742.12 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,570,000.00 USD | 899.47 USD | 0.00 USD | `+15.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,640,000.00 USD | 70,020.00 USD | 0.00 USD | `+15.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,640,000.00 USD | 373.97 USD | 0.00 USD | `+15.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,650,000.00 USD | 5,050.00 USD | 0.00 USD | `+16.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,660,000.00 USD | 6,370.00 USD | 0.00 USD | `+17.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,660,000.00 USD | 404.20 USD | 0.00 USD | `+17.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,870,000.00 USD | 210,980.00 USD | 0.00 USD | `+17.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,870,000.00 USD | 1,150.00 USD | 0.00 USD | `+17.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,870,000.00 USD | 172.16 USD | 0.00 USD | `+18.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,870,000.00 USD | 922.87 USD | 0.00 USD | `+19.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,870,000.00 USD | 489.40 USD | 0.00 USD | `+20.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,870,000.00 USD | 1,200.00 USD | 0.00 USD | `+20.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,870,000.00 USD | 118.01 USD | 0.00 USD | `+21.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.46` | 1,870,000.00 USD | 971.48 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.47` | 1,870,000.00 USD | 818.31 USD | 0.00 USD | `+21.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,870,000.00 USD | 312.31 USD | 0.00 USD | `+22.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,880,000.00 USD | 2,290.00 USD | 0.00 USD | `+22.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.53` | 1,880,000.00 USD | 1,890.00 USD | 0.00 USD | `+22.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,880,000.00 USD | 178.46 USD | 0.00 USD | `+23.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,880,000.00 USD | 173.42 USD | 0.00 USD | `+24.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,880,000.00 USD | 184.75 USD | 0.00 USD | `+24.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,880,000.00 USD | 135.78 USD | 0.00 USD | `+25.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,880,000.00 USD | 127.96 USD | 0.00 USD | `+25.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,880,000.00 USD | 476.43 USD | 0.00 USD | `+26.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,880,000.00 USD | 869.35 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,920,000.00 USD | 35,110.00 USD | 0.00 USD | `+26.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,920,000.00 USD | 251.06 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,920,000.00 USD | 552.44 USD | 0.00 USD | `+27.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,920,000.00 USD | 537.26 USD | 0.00 USD | `+27.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.11` | 1,920,000.00 USD | 1,110.00 USD | 0.00 USD | `+29.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,920,000.00 USD | 320.29 USD | 0.00 USD | `+29.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,920,000.00 USD | 1,100.00 USD | 0.00 USD | `+29.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,920,000.00 USD | 2,270.00 USD | 0.00 USD | `+30.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,920,000.00 USD | 1,270.00 USD | 0.00 USD | `+30.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,920,000.00 USD | 1,380.00 USD | 0.00 USD | `+32.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,930,000.00 USD | 2,410.00 USD | 0.00 USD | `+32.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,940,000.00 USD | 10,640.00 USD | 0.00 USD | `+33.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 1,940,000.00 USD | 2,050.00 USD | 0.00 USD | `+33.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,940,000.00 USD | 529.11 USD | 0.00 USD | `+33.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,950,000.00 USD | 7,700.00 USD | 0.00 USD | `+34.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,950,000.00 USD | 906.03 USD | 0.00 USD | `+37.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,950,000.00 USD | 434.61 USD | 0.00 USD | `+37.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,950,000.00 USD | 163.52 USD | 0.00 USD | `+38.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 1,960,000.00 USD | 10,370.00 USD | 0.00 USD | `+39.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.19` | 1,960,000.00 USD | 5,270.00 USD | 0.00 USD | `+41.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.28` | 1,960,000.00 USD | 115.02 USD | 0.00 USD | `+42.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 1,970,000.00 USD | 3,870.00 USD | 0.00 USD | `+47.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 1,970,000.00 USD | 197.97 USD | 0.00 USD | `+48.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 1,970,000.00 USD | 3,200.00 USD | 0.00 USD | `+50.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 1,970,000.00 USD | 179.58 USD | 0.00 USD | `+50.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 1,970,000.00 USD | 568.45 USD | 0.00 USD | `+51.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 1,970,000.00 USD | 169.57 USD | 0.00 USD | `+52.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 1,970,000.00 USD | 446.52 USD | 0.00 USD | `+55.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 1,980,000.00 USD | 5,320.00 USD | 0.00 USD | `+56.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,190,000.00 USD | 210,750.00 USD | 0.00 USD | `+57.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,190,000.00 USD | 407.95 USD | 0.00 USD | `+59.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,190,000.00 USD | 174.91 USD | 0.00 USD | `+60.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,190,000.00 USD | 4,680.00 USD | 0.00 USD | `+62.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,200,000.00 USD | 960.26 USD | 0.00 USD | `+65.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,200,000.00 USD | 2,710.00 USD | 0.00 USD | `+66.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,200,000.00 USD | 805.90 USD | 0.00 USD | `+68.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,200,000.00 USD | 655.55 USD | 0.00 USD | `+70.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,200,000.00 USD | 4,890.00 USD | 0.00 USD | `+71.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,210,000.00 USD | 471.09 USD | 0.00 USD | `+72.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,210,000.00 USD | 383.85 USD | 0.00 USD | `+73.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,860,000.00 USD | 653,420.00 USD | 0.00 USD | `+74.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 2,860,000.00 USD | 1,510.00 USD | 0.00 USD | `+75.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,860,000.00 USD | 111.87 USD | 0.00 USD | `+84.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,860,000.00 USD | 219.91 USD | 0.00 USD | `+86.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 2,860,000.00 USD | 121.74 USD | 0.00 USD | `+97.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.00` | 2,860,000.00 USD | 297.59 USD | 0.00 USD | `+97.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.20` | 2,980,000.00 USD | 120,270.00 USD | 0.00 USD | `+100.03%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.27` | 6,480,000.00 USD | 0.00 USD | 6,480,000.00 USD | 360.23 USD | 1,810.00 USD | 5,550.00 USD |
| `7D` | `7.31` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 5,840.00 USD |
| `7D` | `7.35` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 406.69 USD |
| `7D` | `7.37` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 45,620.00 USD | 0.00 USD | 457.98 USD |
| `7D` | `7.39` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 46,200.00 USD | 0.00 USD | 503.12 USD |
| `7D` | `7.45` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD |
| `7D` | `7.49` | 6,350,000.00 USD | 0.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD |
| `7D` | `7.51` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 2,070.00 USD | 0.00 USD | 18,280.00 USD |
| `7D` | `7.53` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 35,990.00 USD | 18,910.00 USD | 0.00 USD |
| `7D` | `7.55` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD |
| `1D` | `7.59` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 1,740.00 USD | 0.00 USD | 7,560.00 USD |
| `1D` | `7.60` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 706.40 USD | 4,900.00 USD | 351.13 USD |
| `1D` | `7.61` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 2,750.00 USD | 1,250.00 USD | 11,670.00 USD |
| `7D` | `7.61` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 626.55 USD | 0.00 USD | 301.55 USD |
| `1D` | `7.62` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 8,960.00 USD | 1,330.00 USD | 133.28 USD |
| `1D` | `7.63` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 5,940.00 USD | 0.00 USD | 9,660.00 USD |
| `7D` | `7.63` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 41,300.00 USD | 2,130.00 USD | 1,680.00 USD |
| `1D` | `7.64` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 33,010.00 USD | 812.96 USD | 2,390.00 USD |
| `1D` | `7.65` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 0.00 USD | 1,320.00 USD | 9,870.00 USD |
| `7D` | `7.65` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 4,870.00 USD | 2,350.00 USD | 0.00 USD |
| `1D` | `7.66` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 3,030.00 USD | 0.00 USD | 531.95 USD |
| `1D` | `7.67` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 1,410.00 USD | 1,110.00 USD | 1,790.00 USD |
| `7D` | `7.67` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 1,110.00 USD | 0.00 USD | 34,150.00 USD |
| `1D` | `7.68` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 892.30 USD | 0.00 USD | 5,300.00 USD |
| `1D` | `7.69` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 0.00 USD | 1,600.00 USD | 0.13 USD |
| `1D` | `7.70` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 4,140.00 USD | 3,380.00 USD | 16,770.00 USD |
| `1D` | `7.71` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 660.12 USD | 5,720.00 USD | 7,400.00 USD |
| `7D` | `7.71` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 393.33 USD | 0.00 USD | 33,140.00 USD |
| `1D` | `7.72` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 701.68 USD | 1,320.00 USD | 3,750.00 USD |
| `1D` | `7.73` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 4,120.00 USD | 1,240.00 USD | 5,600.00 USD |
| `7D` | `7.73` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 39,770.00 USD | 0.00 USD | 7,340.00 USD |
| `1D` | `7.74` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 16,520.00 USD | 0.00 USD | 184.39 USD |
| `1D` | `7.75` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 900.06 USD | 6,210.00 USD | 8,050.00 USD |
| `7D` | `7.75` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 29,320.00 USD | 13,360.00 USD | 10,360.00 USD |
| `1D` | `7.76` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 458.75 USD | 494.12 USD | 0.00 USD |
| `1D` | `7.77` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 13,020.00 USD | 689.91 USD | 3,430.00 USD |
| `7D` | `7.77` | 6,010,000.00 USD | 0.00 USD | 6,010,000.00 USD | 20,120.00 USD | 4,900.00 USD | 6,580.00 USD |
| `1D` | `7.78` | 5,660,000.00 USD | 0.00 USD | 5,660,000.00 USD | 2,730.00 USD | 6,250.00 USD | 0.00 USD |
| `1D` | `7.79` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 18,960.00 USD | 2,920.00 USD | 7,250.00 USD |
| `7D` | `7.79` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 70,950.00 USD | 7,170.00 USD | 23,040.00 USD |
| `1D` | `7.80` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 4,920.00 USD | 7,910.00 USD | 709.61 USD |
| `1D` | `7.81` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 349.70 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.81` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 3,970.00 USD | 11,570.00 USD | 1,770.00 USD |
| `1D` | `7.82` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 248.67 USD | 1,680.00 USD | 0.00 USD |
| `1D` | `7.83` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 27,230.00 USD | 5,360.00 USD | 0.00 USD |
| `7D` | `7.83` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 29,530.00 USD | 2,130.00 USD | 24,330.00 USD |
| `1D` | `7.84` | 5,580,000.00 USD | 0.00 USD | 5,580,000.00 USD | 978.04 USD | 1,240.00 USD | 0.00 USD |
| `1D` | `7.85` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 3,320.00 USD | 639.88 USD | 2,650.00 USD |
| `7D` | `7.85` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 17,330.00 USD | 7,840.00 USD | 13,000.00 USD |
| `1D` | `7.86` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 1,290.00 USD | 6,270.00 USD | 13,940.00 USD |
| `1D` | `7.87` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 10,980.00 USD | 10,860.00 USD | 22,910.00 USD |
| `7D` | `7.87` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 150,960.00 USD | 1,540.00 USD | 22,350.00 USD |
| `1D` | `7.88` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 158,960.00 USD | 4,280.00 USD | 33,710.00 USD |
| `1D` | `7.89` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 57,720.00 USD | 3,720.00 USD | 27,230.00 USD |
| `7D` | `7.89` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 150,040.00 USD | 18,320.00 USD | 24,270.00 USD |
| `1D` | `7.90` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 56,620.00 USD | 6,970.00 USD | 4,310.00 USD |
| `1D` | `7.91` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 14,180.00 USD | 10,370.00 USD | 28,300.00 USD |
| `7D` | `7.91` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 31,740.00 USD | 26,330.00 USD | 45,390.00 USD |
| `1D` | `7.92` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 15,830.00 USD | 2,040.00 USD | 6,930.00 USD |
| `1D` | `7.93` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,480.00 USD |
| `7D` | `7.93` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 78,470.00 USD | 7,330.00 USD | 14,550.00 USD |
| `1D` | `7.94` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 15,580.00 USD | 20,510.00 USD | 61,750.00 USD |
| `1D` | `7.95` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 28,200.00 USD | 9,190.00 USD | 86,980.00 USD |
| `7D` | `7.95` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 45,890.00 USD | 9,500.00 USD | 102,940.00 USD |
| `1D` | `7.96` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,330.00 USD |
| `1D` | `7.97` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD |
| `7D` | `7.97` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 37,150.00 USD | 18,700.00 USD | 40,570.00 USD |
| `1D` | `7.98` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 5,050.00 USD | 2,060.00 USD | 42,970.00 USD |
| `1D` | `7.99` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 3,450.00 USD | 10,180.00 USD | 4,660.00 USD |
| `7D` | `7.99` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 52,570.00 USD | 20,640.00 USD | 122,150.00 USD |
| `1D` | `8.00` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 50,430.00 USD | 8,950.00 USD | 21,810.00 USD |
| `1D` | `8.01` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 6,540.00 USD | 3,750.00 USD | 4,040.00 USD |
| `7D` | `8.01` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 47,380.00 USD | 17,990.00 USD | 46,600.00 USD |
| `1D` | `8.02` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 75,150.00 USD | 0.00 USD | 274.70 USD |
| `1D` | `8.03` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 9,070.00 USD | 12,540.00 USD | 12,890.00 USD |
| `7D` | `8.03` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 353,080.00 USD | 35,720.00 USD | 49,900.00 USD |
| `1D` | `8.04` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 49,540.00 USD | 0.00 USD | 10,010.00 USD |
| `1D` | `8.05` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 318,600.00 USD | 6,430.00 USD | 53,960.00 USD |
| `7D` | `8.05` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 390,130.00 USD | 0.00 USD | 63,560.00 USD |
| `1D` | `8.06` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 155,360.00 USD | 0.00 USD | 66,970.00 USD |
| `1D` | `8.07` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD |
| `7D` | `8.07` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 60,670.00 USD | 0.00 USD | 75,410.00 USD |
| `1D` | `8.08` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD |
| `1D` | `8.09` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 3,650.00 USD | 0.00 USD | 29,580.00 USD |
| `7D` | `8.09` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 32,760.00 USD | 0.00 USD | 81,280.00 USD |
| `1D` | `8.10` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD |
| `1D` | `8.11` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD |
| `7D` | `8.11` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 33,000.00 USD | 0.00 USD | 140,250.00 USD |
| `1D` | `8.12` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 19,930.00 USD | 11,230.00 USD | 126,250.00 USD |
| `1D` | `8.13` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 34,890.00 USD | 9,180.00 USD | 1,710.00 USD |
| `7D` | `8.13` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 47,290.00 USD | 12,740.00 USD | 20,310.00 USD |
| `1D` | `8.14` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 17,740.00 USD | 8,630.00 USD | 105,270.00 USD |
| `1D` | `8.15` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 47,020.00 USD | 12,240.00 USD | 53,660.00 USD |
| `7D` | `8.15` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 179,060.00 USD | 31,560.00 USD | 183,290.00 USD |
| `1D` | `8.16` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 192.50 USD | 22,250.00 USD | 165,460.00 USD |
| `1D` | `8.17` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 11,100.00 USD | 9,120.00 USD | 183,140.00 USD |
| `7D` | `8.17` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 1,590.00 USD | 13,650.00 USD | 149,580.00 USD |
| `1D` | `8.18` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 7,140.00 USD | 3,280.00 USD | 4,190.00 USD |
| `1D` | `8.19` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 18,260.00 USD | 545.08 USD | 19,120.00 USD |
| `7D` | `8.19` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 1,200.00 USD | 72,340.00 USD | 23,200.00 USD |
| `1D` | `8.20` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 25,900.00 USD | 4,000.00 USD | 11,560.00 USD |
| `1D` | `8.21` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 41,620.00 USD | 2,210.00 USD | 0.00 USD |
| `7D` | `8.21` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 174,220.00 USD | 22,240.00 USD | 0.00 USD |
| `1D` | `8.22` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 3,620.00 USD | 1,530.00 USD | 16,310.00 USD |
| `1D` | `8.23` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 0.00 USD | 3,450.00 USD | 2,380.00 USD |
| `7D` | `8.23` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 0.00 USD | 40,260.00 USD | 0.00 USD |
| `1D` | `8.24` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 168.44 USD | 5,100.00 USD | 9,270.00 USD |
| `1D` | `8.25` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 0.00 USD | 5,000.00 USD | 38,170.00 USD |
| `7D` | `8.25` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 129,050.00 USD | 5,750.00 USD | 17,610.00 USD |
| `1D` | `8.26` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 50,590.00 USD | 12,510.00 USD | 23,300.00 USD |
| `1D` | `8.27` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 13,860.00 USD | 12,270.00 USD | 20,120.00 USD |
| `7D` | `8.27` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 103,730.00 USD | 4,000.00 USD | 37,940.00 USD |
| `1D` | `8.28` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 0.00 USD | 13,760.00 USD | 4,240.00 USD |
| `1D` | `8.29` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 39,480.00 USD | 11,800.00 USD | 0.00 USD |
| `7D` | `8.29` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 166,800.00 USD | 6,550.00 USD | 21,950.00 USD |
| `1D` | `8.30` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 69,220.00 USD | 13,810.00 USD | 20,060.00 USD |
| `1D` | `8.31` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 82,900.00 USD | 11,920.00 USD | 56,400.00 USD |
| `7D` | `8.31` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 370,260.00 USD | 10,660.00 USD | 2,790.00 USD |
| `1D` | `8.32` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 80,060.00 USD | 6,080.00 USD | 14,060.00 USD |
| `1D` | `8.33` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 0.00 USD | 8,710.00 USD | 109.14 USD |
| `7D` | `8.33` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 14,600.00 USD | 11,770.00 USD | 4,900.00 USD |
| `1D` | `8.34` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 0.00 USD | 3,230.00 USD | 13.84 USD |
| `1D` | `8.35` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 0.00 USD | 23,440.00 USD | 25,350.00 USD |
| `7D` | `8.35` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 223,170.00 USD | 0.00 USD | 5,720.00 USD |
| `1D` | `8.36` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 0.00 USD | 1,090.00 USD | 25,130.00 USD |
| `1D` | `8.37` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 691.75 USD | 14,420.00 USD | 16.86 USD |
| `7D` | `8.37` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 36,530.00 USD |
| `1D` | `8.38` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 17,220.00 USD | 7,830.00 USD | 50,290.00 USD |
| `1D` | `8.39` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 107,990.00 USD | 16,670.00 USD | 32,610.00 USD |
| `7D` | `8.39` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 7,600.00 USD | 68,640.00 USD |
| `1D` | `8.40` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 10,500.00 USD | 10,400.00 USD | 56,580.00 USD |
| `1D` | `8.41` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 0.00 USD | 10,190.00 USD | 18,540.00 USD |
| `7D` | `8.41` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 194,850.00 USD | 0.00 USD | 89,020.00 USD |
| `1D` | `8.42` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 16,260.00 USD | 42,890.00 USD |
| `1D` | `8.43` | 977,590.00 USD | 0.00 USD | 977,590.00 USD | 81,350.00 USD | 7,730.00 USD | 7,540.00 USD |
| `7D` | `8.43` | 806,530.00 USD | 0.00 USD | 806,530.00 USD | 163,340.00 USD | 0.00 USD | 22,840.00 USD |
| `1D` | `8.44` | 880,970.00 USD | 0.00 USD | 880,970.00 USD | 11,130.00 USD | 32,380.00 USD | 160,460.00 USD |
| `1D` | `8.45` | 676,990.00 USD | 0.00 USD | 676,990.00 USD | 54,790.00 USD | 5,970.00 USD | 0.00 USD |
| `7D` | `8.45` | 620,350.00 USD | 0.00 USD | 620,350.00 USD | 156,410.00 USD | 8,000.00 USD | 171,560.00 USD |
| `1D` | `8.47` | 616,240.00 USD | 0.00 USD | 616,240.00 USD | 663.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.47` | 284,390.00 USD | 0.00 USD | 284,390.00 USD | 0.00 USD | 0.00 USD | 38,730.00 USD |
| `1D` | `8.48` | 615,570.00 USD | 0.00 USD | 615,570.00 USD | 749.80 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.49` | 614,820.00 USD | 0.00 USD | 614,820.00 USD | 0.00 USD | 0.00 USD | 12.70 USD |
| `7D` | `8.49` | 245,650.00 USD | 0.00 USD | 245,650.00 USD | 0.00 USD | 0.00 USD | 153,260.00 USD |
| `7D` | `8.51` | 92,390.00 USD | 0.00 USD | 92,390.00 USD | 0.00 USD | 0.00 USD | 92,390.00 USD |
| `1D` | `8.52` | 614,810.00 USD | 0.00 USD | 614,810.00 USD | 158,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.53` | 456,180.00 USD | 0.00 USD | 456,180.00 USD | 24,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.53` | 174,760.00 USD | 174,760.00 USD | 0.00 USD | 173,370.00 USD | 0.00 USD | 1,390.00 USD |
| `7D` | `8.53` | 349,520.00 USD | 349,520.00 USD | 0.00 USD | 173,370.00 USD | 0.00 USD | 1,390.00 USD |
| `1D` | `8.54` | 432,000.00 USD | 0.00 USD | 432,000.00 USD | 198,250.00 USD | 0.00 USD | 156.94 USD |
| `1D` | `8.55` | 233,590.00 USD | 0.00 USD | 233,590.00 USD | 1,650.00 USD | 0.00 USD | 25,120.00 USD |
| `7D` | `8.55` | 865,520.00 USD | 865,520.00 USD | 0.00 USD | 434,770.00 USD | 80,630.00 USD | 601.43 USD |
| `1D` | `8.56` | 206,810.00 USD | 0.00 USD | 206,810.00 USD | 686.73 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.57` | 206,130.00 USD | 0.00 USD | 206,130.00 USD | 147,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.57` | 991,800.00 USD | 991,800.00 USD | 0.00 USD | 9,740.00 USD | 115,860.00 USD | 678.07 USD |
| `1D` | `8.58` | 59,120.00 USD | 0.00 USD | 59,120.00 USD | 59,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.59` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.59` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 90,970.00 USD | 1,040.00 USD |
| `1D` | `8.60` | 2,040.00 USD | 2,040.00 USD | 0.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.61` | 3,230.00 USD | 3,230.00 USD | 0.00 USD | 497.00 USD | 0.00 USD | 699.64 USD |
| `7D` | `8.61` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 271.28 USD |
| `1D` | `8.62` | 170,510.00 USD | 170,510.00 USD | 0.00 USD | 41,980.00 USD | 0.00 USD | 125,290.00 USD |
| `1D` | `8.63` | 302,210.00 USD | 302,210.00 USD | 0.00 USD | 129,280.00 USD | 2,420.00 USD | 0.00 USD |
| `7D` | `8.63` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,520.00 USD |
| `1D` | `8.64` | 384,180.00 USD | 384,180.00 USD | 0.00 USD | 69,220.00 USD | 9,340.00 USD | 3,410.00 USD |
| `1D` | `8.65` | 446,290.00 USD | 446,290.00 USD | 0.00 USD | 35,830.00 USD | 9,010.00 USD | 17,260.00 USD |
| `7D` | `8.65` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 40,260.00 USD | 10,660.00 USD | 0.00 USD |
| `1D` | `8.66` | 475,590.00 USD | 475,590.00 USD | 0.00 USD | 13,240.00 USD | 2,020.00 USD | 14,040.00 USD |
| `1D` | `8.67` | 488,990.00 USD | 488,990.00 USD | 0.00 USD | 880.60 USD | 12,460.00 USD | 56.72 USD |
| `7D` | `8.67` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 11,770.00 USD | 1,570.00 USD |
| `1D` | `8.68` | 528,510.00 USD | 528,510.00 USD | 0.00 USD | 588.00 USD | 13,040.00 USD | 25,890.00 USD |
| `1D` | `8.69` | 604,370.00 USD | 604,370.00 USD | 0.00 USD | 10,820.00 USD | 22,830.00 USD | 42,210.00 USD |
| `7D` | `8.69` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 29,260.00 USD | 48,960.00 USD | 162,790.00 USD |
| `1D` | `8.70` | 698,890.00 USD | 698,890.00 USD | 0.00 USD | 62,600.00 USD | 1,090.00 USD | 30,830.00 USD |
| `1D` | `8.71` | 725,580.00 USD | 725,580.00 USD | 0.00 USD | 18,700.00 USD | 7,990.00 USD | 0.00 USD |
| `7D` | `8.71` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 87,110.00 USD | 11,120.00 USD | 0.00 USD |
| `1D` | `8.72` | 814,830.00 USD | 814,830.00 USD | 0.00 USD | 34,050.00 USD | 4,410.00 USD | 50,790.00 USD |
| `1D` | `8.73` | 899,130.00 USD | 899,130.00 USD | 0.00 USD | 19,820.00 USD | 31,860.00 USD | 32,610.00 USD |
| `7D` | `8.73` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 51,030.00 USD | 10,790.00 USD | 1,300.00 USD |
| `1D` | `8.74` | 962,120.00 USD | 962,120.00 USD | 0.00 USD | 38,500.00 USD | 6,910.00 USD | 17,580.00 USD |
| `1D` | `8.75` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 33,520.00 USD | 12,720.00 USD | 23,520.00 USD |
| `7D` | `8.75` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 196,960.00 USD | 19,690.00 USD | 35,220.00 USD |
| `1D` | `8.76` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 82,470.00 USD | 10,010.00 USD | 57,030.00 USD |
| `1D` | `8.77` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 155,740.00 USD | 2,060.00 USD | 43,030.00 USD |
| `7D` | `8.77` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 141,710.00 USD | 0.00 USD | 105,410.00 USD |
| `1D` | `8.78` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 41,500.00 USD | 25,510.00 USD | 50,110.00 USD |
| `1D` | `8.79` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 31,710.00 USD | 17,970.00 USD | 31,130.00 USD |
| `7D` | `8.79` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 29,660.00 USD | 33,300.00 USD | 65,190.00 USD |
| `1D` | `8.80` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 113,160.00 USD | 19,150.00 USD | 23,840.00 USD |
| `1D` | `8.81` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 53,290.00 USD | 9,030.00 USD | 1,750.00 USD |
| `7D` | `8.81` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 122,920.00 USD | 26,890.00 USD | 58,050.00 USD |
| `1D` | `8.82` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 19,950.00 USD | 4,510.00 USD | 61,490.00 USD |
| `1D` | `8.83` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 174,730.00 USD | 19,400.00 USD | 7,020.00 USD |
| `7D` | `8.83` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 242,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.84` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 1,500.00 USD | 4,360.00 USD | 59,130.00 USD |
| `1D` | `8.85` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 13,040.00 USD | 3,870.00 USD | 11,200.00 USD |
| `7D` | `8.85` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 29,310.00 USD | 5,880.00 USD | 58,190.00 USD |
| `1D` | `8.86` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 2,060.00 USD | 3,280.00 USD | 4,790.00 USD |
| `1D` | `8.87` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 1,410.00 USD | 545.08 USD | 12,570.00 USD |
| `7D` | `8.87` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD |
| `1D` | `8.88` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 803.70 USD | 14,670.00 USD | 186.36 USD |
| `1D` | `8.89` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 13,040.00 USD | 4,360.00 USD | 32,950.00 USD |
| `7D` | `8.89` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD | 73,830.00 USD |
| `1D` | `8.90` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 32,320.00 USD | 7,510.00 USD | 65,160.00 USD |
| `1D` | `8.91` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 32,240.00 USD | 13,320.00 USD | 15,860.00 USD |
| `7D` | `8.91` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 2,440.00 USD | 0.00 USD | 88,620.00 USD |
| `1D` | `8.92` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 1,110.00 USD | 5,100.00 USD | 9,340.00 USD |
| `1D` | `8.93` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 31,830.00 USD | 6,810.00 USD | 38,940.00 USD |
| `7D` | `8.93` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 157,480.00 USD | 0.00 USD | 17,610.00 USD |
| `1D` | `8.94` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 50,590.00 USD | 12,260.00 USD | 3,770.00 USD |
| `1D` | `8.95` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 3,080.00 USD | 6,630.00 USD | 20,340.00 USD |
| `7D` | `8.95` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 74,920.00 USD | 4,000.00 USD | 38,550.00 USD |
| `1D` | `8.96` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 1,260.00 USD | 2,980.00 USD | 175.90 USD |
| `1D` | `8.97` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.26 USD |
| `7D` | `8.97` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.98` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 35,320.00 USD | 9,420.00 USD | 19,670.00 USD |
| `1D` | `8.99` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 48,380.00 USD | 22,110.00 USD | 3,420.00 USD |
| `7D` | `8.99` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 145,880.00 USD | 6,550.00 USD | 28,870.00 USD |
| `1D` | `9.00` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 36,960.00 USD | 0.00 USD | 24,750.00 USD |
| `1D` | `9.01` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 49,510.00 USD | 14,940.00 USD | 16,240.00 USD |
| `7D` | `9.01` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 303,030.00 USD | 36,180.00 USD | 23,020.00 USD |
| `1D` | `9.02` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 39,170.00 USD | 29,440.00 USD | 5,010.00 USD |
| `1D` | `9.03` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 125,760.00 USD | 10,300.00 USD | 34,410.00 USD |
| `7D` | `9.03` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 107,490.00 USD | 101,140.00 USD | 15,640.00 USD |
| `1D` | `9.04` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 41,710.00 USD | 5,900.00 USD | 14,800.00 USD |
| `1D` | `9.05` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 21,980.00 USD | 7,560.00 USD | 22,410.00 USD |
| `7D` | `9.05` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 38,740.00 USD | 17,700.00 USD | 39,710.00 USD |
| `1D` | `9.06` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 28,180.00 USD | 5,480.00 USD | 10,490.00 USD |
| `1D` | `9.07` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 13,070.00 USD | 15,350.00 USD | 25,460.00 USD |
| `7D` | `9.07` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 3,990.00 USD | 14,140.00 USD | 36,530.00 USD |
| `1D` | `9.08` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 12,960.00 USD | 1,040.00 USD | 24,280.00 USD |
| `1D` | `9.09` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 71,230.00 USD | 9,730.00 USD | 25,300.00 USD |
| `7D` | `9.09` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 152,640.00 USD | 8,680.00 USD | 144,360.00 USD |
| `1D` | `9.10` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 16,320.00 USD | 10,640.00 USD | 30,930.00 USD |
| `1D` | `9.11` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 51,080.00 USD | 14,420.00 USD | 82,390.00 USD |
| `7D` | `9.11` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 877,120.00 USD | 37,620.00 USD | 570,050.00 USD |
| `1D` | `9.12` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 94,400.00 USD | 21,650.00 USD | 26,360.00 USD |
| `1D` | `9.13` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 75,260.00 USD | 15,960.00 USD | 35,980.00 USD |
| `7D` | `9.13` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 666,880.00 USD | 26,540.00 USD | 484,570.00 USD |
| `1D` | `9.14` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 30,520.00 USD | 2,600.00 USD | 29,600.00 USD |
| `1D` | `9.15` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 56,980.00 USD | 20,890.00 USD | 18,440.00 USD |
| `7D` | `9.15` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 357,020.00 USD | 38,700.00 USD | 270,200.00 USD |
| `1D` | `9.16` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 63,930.00 USD | 23,900.00 USD | 32,470.00 USD |
| `1D` | `9.17` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 74,820.00 USD | 3,200.00 USD | 49,540.00 USD |
| `7D` | `9.17` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 409,650.00 USD | 133,490.00 USD | 303,370.00 USD |
| `1D` | `9.18` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 28,310.00 USD | 26,430.00 USD | 31,220.00 USD |
| `1D` | `9.19` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 77,890.00 USD | 29,140.00 USD | 7,680.00 USD |
| `7D` | `9.19` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 504,150.00 USD | 108,440.00 USD | 193,800.00 USD |
| `1D` | `9.20` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 64,910.00 USD | 11,090.00 USD | 37,460.00 USD |
| `1D` | `9.21` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 30,000.00 USD | 2,950.00 USD | 4,760.00 USD |
| `7D` | `9.21` | 10,460,000.00 USD | 10,460,000.00 USD | 0.00 USD | 590,780.00 USD | 144,470.00 USD | 277,570.00 USD |
| `1D` | `9.22` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 58,470.00 USD | 2,850.00 USD | 11,100.00 USD |
| `1D` | `9.23` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 471.32 USD | 4,270.00 USD | 17.80 USD |
| `7D` | `9.23` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 582,450.00 USD | 92,780.00 USD | 331,960.00 USD |
| `1D` | `9.24` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 45,580.00 USD | 0.00 USD | 3,020.00 USD |
| `1D` | `9.25` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 17,240.00 USD | 5,840.00 USD | 9,510.00 USD |
| `7D` | `9.25` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 277,290.00 USD | 61,940.00 USD | 61,110.00 USD |
| `1D` | `9.26` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 574.60 USD | 0.00 USD | 3,540.00 USD |
| `1D` | `9.27` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 23,430.00 USD | 1,360.00 USD | 6,640.00 USD |
| `7D` | `9.27` | 12,160,000.00 USD | 12,160,000.00 USD | 0.00 USD | 156,190.00 USD | 102,670.00 USD | 37,770.00 USD |
| `1D` | `9.28` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 1,610.00 USD | 8,760.00 USD | 169.17 USD |
| `1D` | `9.29` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 16,070.00 USD | 4,140.00 USD | 17,910.00 USD |
| `7D` | `9.29` | 12,880,000.00 USD | 12,880,000.00 USD | 0.00 USD | 392,980.00 USD | 82,050.00 USD | 244,470.00 USD |
| `1D` | `9.30` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 39,880.00 USD | 7,520.00 USD | 11,600.00 USD |
| `1D` | `9.31` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 28,930.00 USD | 5,500.00 USD | 12,920.00 USD |
| `7D` | `9.31` | 13,450,000.00 USD | 13,450,000.00 USD | 0.00 USD | 308,150.00 USD | 55,090.00 USD | 209,900.00 USD |
| `1D` | `9.32` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 17,660.00 USD | 1,330.00 USD | 5,070.00 USD |
| `1D` | `9.33` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 12,710.00 USD | 6,000.00 USD | 9,780.00 USD |
| `7D` | `9.33` | 13,780,000.00 USD | 13,780,000.00 USD | 0.00 USD | 134,040.00 USD | 57,370.00 USD | 139,720.00 USD |
| `1D` | `9.34` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 46,100.00 USD | 3,660.00 USD | 5,580.00 USD |
| `1D` | `9.35` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 13,620.00 USD | 1,320.00 USD | 14,910.00 USD |
| `7D` | `9.35` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 114,090.00 USD | 67,130.00 USD | 96,310.00 USD |
| `1D` | `9.36` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 4,730.00 USD | 6,760.00 USD | 8,030.00 USD |
| `1D` | `9.37` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 13,170.00 USD | 6,780.00 USD | 4,400.00 USD |
| `7D` | `9.37` | 14,390,000.00 USD | 14,390,000.00 USD | 0.00 USD | 211,790.00 USD | 34,660.00 USD | 85,580.00 USD |
| `1D` | `9.38` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 15,290.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `9.39` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 8,850.00 USD | 1,600.00 USD | 12.83 USD |
| `7D` | `9.39` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 206,980.00 USD | 32,960.00 USD | 87,830.00 USD |
| `1D` | `9.40` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 22,270.00 USD | 0.00 USD | 12.64 USD |
| `1D` | `9.41` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 4,410.00 USD | 378.69 USD | 10,140.00 USD |
| `7D` | `9.41` | 15,120,000.00 USD | 15,120,000.00 USD | 0.00 USD | 265,720.00 USD | 30,790.00 USD | 99,880.00 USD |
| `1D` | `9.42` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 9,240.00 USD | 3,010.00 USD | 6,520.00 USD |
| `1D` | `9.43` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 5,380.00 USD | 1,380.00 USD | 25.44 USD |
| `7D` | `9.43` | 15,210,000.00 USD | 15,210,000.00 USD | 0.00 USD | 33,890.00 USD | 13,430.00 USD | 42,430.00 USD |
| `1D` | `9.44` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 1,320.00 USD | 3,750.00 USD |
| `1D` | `9.45` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 1,240.00 USD | 5,600.00 USD |
| `7D` | `9.45` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 68,680.00 USD | 9,040.00 USD | 8,600.00 USD |
| `1D` | `9.46` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 16,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.47` | 15,360,000.00 USD | 15,360,000.00 USD | 0.00 USD | 44,170.00 USD | 5,760.00 USD | 12,750.00 USD |
| `7D` | `9.49` | 15,400,000.00 USD | 15,400,000.00 USD | 0.00 USD | 25,360.00 USD | 10,200.00 USD | 6,210.00 USD |
| `7D` | `9.51` | 15,530,000.00 USD | 15,530,000.00 USD | 0.00 USD | 57,130.00 USD | 21,130.00 USD | 54,360.00 USD |
| `7D` | `9.53` | 15,590,000.00 USD | 15,590,000.00 USD | 0.00 USD | 50,200.00 USD | 9,410.00 USD | 1,270.00 USD |
| `7D` | `9.55` | 15,620,000.00 USD | 15,620,000.00 USD | 0.00 USD | 11,560.00 USD | 11,570.00 USD | 880.26 USD |
| `7D` | `9.57` | 15,670,000.00 USD | 15,670,000.00 USD | 0.00 USD | 31,530.00 USD | 2,130.00 USD | 24,130.00 USD |
| `7D` | `9.59` | 15,710,000.00 USD | 15,710,000.00 USD | 0.00 USD | 14,070.00 USD | 7,840.00 USD | 14,300.00 USD |
| `7D` | `9.61` | 15,760,000.00 USD | 15,760,000.00 USD | 0.00 USD | 37,000.00 USD | 0.00 USD | 11,290.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `355.89M` | Total OI Tokens: `41,464,351.8 AVAX`
  * 1h OI Change: `+1.14%` | 4h OI Change: `-0.83%` | 24h OI Change: `-6.39%`
  * Exchange Breakdown: Binance=`80.82M` | Bybit=`57.64M` | OKX=`11.66M` | Hyperliquid=`16.94M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `11.70K` | Last 24h: `16.67K` | Last 3d: `66.43K` | Last 7d: `105.12K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0064%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0092%` | **USDT Bitget** | `0.0037%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `57.07%` | `42.93%` | `1.33` | 5,910,000.00 USD |
| `15M` | `Binance` | `61.64%` | `38.36%` | `1.61` | 2,680,000.00 USD |
| `15M` | `OKX` | `49.49%` | `50.51%` | `0.98` | 546,060.00 USD |
| `15M` | `Bybit` | `71.6%` | `28.4%` | `2.52` | 477,850.00 USD |
| `15M` | `KuCoin` | `48.43%` | `51.57%` | `0.94` | 13,030.00 USD |
| `15M` | `Gate` | `36.33%` | `63.67%` | `0.57` | 92,330.00 USD |
| `15M` | `Bitget` | `59.47%` | `40.53%` | `1.47` | 217,870.00 USD |
| `15M` | `BingX` | `71.33%` | `28.67%` | `2.49` | 140,580.00 USD |
| `15M` | `MEXC` | `47.48%` | `52.52%` | `0.90` | 1,240,000.00 USD |
| `15M` | `Bitunix` | `52.58%` | `47.42%` | `1.11` | 123,560.00 USD |
| `15M` | `Hyperliquid` | `74.01%` | `25.99%` | `2.85` | 51,100.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.03%` | `49.97%` | `1.00` | 171,710.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 21,150.00 USD |
| `15M` | `HTX` | `51.98%` | `48.02%` | `1.08` | 1,070.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `26.44%` | `73.56%` | `0.36` | 100,960.00 USD |
| `15M` | `Aster` | `96.09%` | `3.91%` | `24.58` | 41,200.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `26.61%` | `73.39%` | `0.36` | 3,560.00 USD |
| `15M` | `Whale Positions` | `61.64%` | `38.36%` | `1.61` | 2,680,000.00 USD |
| `15M` | `Global Accounts` | `57.07%` | `42.93%` | `1.33` | 5,910,000.00 USD |
| `1H` | `AVAX` | `47.22%` | `52.78%` | `0.89` | 22,660,000.00 USD |
| `1H` | `Binance` | `53.33%` | `46.67%` | `1.14` | 7,460,000.00 USD |
| `1H` | `OKX` | `45.87%` | `54.13%` | `0.85` | 2,010,000.00 USD |
| `1H` | `Bybit` | `52.15%` | `47.85%` | `1.09` | 1,670,000.00 USD |
| `1H` | `KuCoin` | `36.72%` | `63.28%` | `0.58` | 90,550.00 USD |
| `1H` | `Gate` | `25.31%` | `74.69%` | `0.34` | 377,580.00 USD |
| `1H` | `Bitget` | `55.84%` | `44.16%` | `1.26` | 876,320.00 USD |
| `1H` | `BingX` | `12.17%` | `87.83%` | `0.14` | 2,440,000.00 USD |
| `1H` | `MEXC` | `49.44%` | `50.56%` | `0.98` | 5,120,000.00 USD |
| `1H` | `Bitunix` | `74.66%` | `25.34%` | `2.95` | 791,130.00 USD |
| `1H` | `Hyperliquid` | `33.25%` | `66.75%` | `0.50` | 350,390.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.17%` | `49.83%` | `1.01` | 1,020,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `43.1%` | `56.9%` | `0.76` | 55,530.00 USD |
| `1H` | `HTX` | `21.88%` | `78.12%` | `0.28` | 4,870.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `53.21%` | `46.79%` | `1.14` | 300,920.00 USD |
| `1H` | `Aster` | `87.68%` | `12.32%` | `7.12` | 78,750.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `51.02%` | `48.98%` | `1.04` | 16,300.00 USD |
| `1H` | `Whale Positions` | `53.33%` | `46.67%` | `1.14` | 7,460,000.00 USD |
| `1H` | `Global Accounts` | `47.22%` | `52.78%` | `0.89` | 22,660,000.00 USD |
| `4H` | `AVAX` | `44.27%` | `55.73%` | `0.79` | 61,620,000.00 USD |
| `4H` | `Binance` | `47.6%` | `52.4%` | `0.91` | 18,130,000.00 USD |
| `4H` | `OKX` | `49.81%` | `50.19%` | `0.99` | 3,330,000.00 USD |
| `4H` | `Bybit` | `42.35%` | `57.65%` | `0.73` | 3,050,000.00 USD |
| `4H` | `KuCoin` | `55.44%` | `44.56%` | `1.24` | 399,640.00 USD |
| `4H` | `Gate` | `53.39%` | `46.61%` | `1.15` | 883,340.00 USD |
| `4H` | `Bitget` | `36.8%` | `63.2%` | `0.58` | 1,060,000.00 USD |
| `4H` | `BingX` | `39.92%` | `60.08%` | `0.66` | 16,990,000.00 USD |
| `4H` | `MEXC` | `53.07%` | `46.93%` | `1.13` | 3,470,000.00 USD |
| `4H` | `Bitunix` | `62.66%` | `37.34%` | `1.68` | 1,320,000.00 USD |
| `4H` | `Hyperliquid` | `43.14%` | `56.86%` | `0.76` | 654,380.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.04%` | `47.96%` | `1.09` | 8,650,000.00 USD |
| `4H` | `Crypto.com` | `60.19%` | `39.81%` | `1.51` | 7,530.00 USD |
| `4H` | `WhiteBIT` | `7.14%` | `92.86%` | `0.08` | 3,120,000.00 USD |
| `4H` | `HTX` | `38.68%` | `61.32%` | `0.63` | 73,390.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `20.71%` | `79.29%` | `0.26` | 271,650.00 USD |
| `4H` | `Aster` | `9.95%` | `90.05%` | `0.11` | 47,630.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `42.68%` | `57.32%` | `0.74` | 179,200.00 USD |
| `4H` | `Whale Positions` | `47.6%` | `52.4%` | `0.91` | 18,130,000.00 USD |
| `4H` | `Global Accounts` | `44.27%` | `55.73%` | `0.79` | 61,620,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `8.46` | `8.47` | `8.46` | `8.49` | `8.46` | 681,089.39 USD | 260,569.06 USD | 420,520.33 USD | -159,951.27 USD | `-23.48%` | `1B / 5S` |
| `5:00 UTC` | `8.49` | `8.48` | `8.49` | `8.50` | `8.45` | 460,668.30 USD | 266,426.92 USD | 194,241.38 USD | 72,185.55 USD | `+15.67%` | `10B / 4S` |
| `0:00 UTC` | `8.48` | `8.48` | `8.48` | `8.51` | `8.46` | 702,848.74 USD | 346,932.98 USD | 355,915.76 USD | -8,982.78 USD | `-1.28%` | `2B / 6S` |
| `5:00 UTC` | `8.46` | `8.47` | `8.46` | `8.48` | `8.46` | 798,371.69 USD | 455,825.46 USD | 342,546.23 USD | 113,279.23 USD | `+14.19%` | `6B / 4S` |
| `0:00 UTC` | `8.47` | `8.46` | `8.47` | `8.48` | `8.44` | 1,028,869.35 USD | 429,609.02 USD | 599,260.32 USD | -169,651.30 USD | `-16.49%` | `4B / 8S` |
| `5:00 UTC` | `8.47` | `8.47` | `8.47` | `8.49` | `8.46` | 909,192.14 USD | 370,410.27 USD | 538,781.87 USD | -168,371.60 USD | `-18.52%` | `3B / 9S` |
| `0:00 UTC` | `8.47` | `8.48` | `8.47` | `8.49` | `8.46` | 824,624.01 USD | 408,080.13 USD | 416,543.88 USD | -8,463.75 USD | `-1.03%` | `2B / 3S` |
| `5:00 UTC` | `8.49` | `8.51` | `8.49` | `8.54` | `8.47` | 897,869.95 USD | 576,315.84 USD | 321,554.11 USD | 254,761.73 USD | `+28.37%` | `17B / 7S` |
| `0:00 UTC` | `8.56` | `8.54` | `8.56` | `8.56` | `8.50` | 1,085,360.20 USD | 616,505.04 USD | 468,855.16 USD | 147,649.89 USD | `+13.60%` | `20B / 10S` |
| `5:00 UTC` | `8.58` | `8.57` | `8.58` | `8.60` | `8.53` | 1,016,981.66 USD | 737,051.16 USD | 279,930.50 USD | 457,120.65 USD | `+44.95%` | `23B / 5S` |

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
| `5m` | 18,300.00 USD | 138,980.00 USD | **`ACCUMULATION`** |
| `15m` | 56,990.00 USD | 659,180.00 USD | **`ACCUMULATION`** |
| `30m` | 301.49 USD | 967,430.00 USD | **`ACCUMULATION`** |
| `1h` | -58,190.00 USD | 1,360,000.00 USD | **`ACCUMULATION`** |
| `2h` | -164,360.00 USD | 1,150,000.00 USD | **`ACCUMULATION`** |
| `4h` | -437,110.00 USD | -1,430,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -408,560.00 USD | -177,310.00 USD | **`DISTRIBUTION`** |
| `8h` | -136,210.00 USD | 1,750,000.00 USD | **`ACCUMULATION`** |
| `12h` | -1,390,000.00 USD | -2,420,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,760,000.00 USD | -10,990,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,900,000.00 USD | -49,510,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -57,260,000.00 USD | -266,790,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+18.30K` | 15m=`+56.99K` | 1h=`-58.19K` | 24h=`-2.76M`
* Futures Capital Netflows: 5m=`+138.98K` | 15m=`+659.18K` | 1h=`+1.36M` | 24h=`-10.99M`
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
  * `2026-10-30 16:26:21 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:29:21 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `7.01` (Risk Distance: `1.24` pts)
  * +2.5R Take Profit: `11.36`
  * Mathematical Lot Sizing: **`8.03 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.59` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `9.83` (Risk Distance: `1.24` pts)
  * +2.5R Take Profit: `5.48`
  * Mathematical Lot Sizing: **`8.03 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.65`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
