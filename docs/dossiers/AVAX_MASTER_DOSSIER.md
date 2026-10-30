# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 15:39:17 IST` (`2026-10-30 10:09:17 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.46` | **Live Ask Quote**: `8.50` | **Mid Price**: `8.48`
- **Spread Points**: `4.00` | **Spread BPS**: `47.17 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.33` | VWAP Z-Score: `+0.68` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0580` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `47.77` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `8.87` | Lower -3.00σ Band: `7.79`
  * Upper +2.51σ Band: `8.78` | Lower -2.51σ Band: `7.88`
  * Upper +2.01σ Band: `8.69` | Lower -2.01σ Band: `7.97`
  * Upper +2.00σ Band: `8.69` | Lower -2.00σ Band: `7.97`
  * Upper +1.28σ Band: `8.56` | Lower -1.28σ Band: `8.10`
  * Upper +1.00σ Band: `8.51` | Lower -1.00σ Band: `8.15`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.46` | EMA-20=`8.47` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.48` (Slope: `+0.0000`) | EMA-100=`8.55`
  * Institutional Anchors: EMA-144=`8.60` | EMA-200=`8.66` (Slope: `-0.2569`) | EMA-233=`8.68`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`7.97` | Weekly High=`9.14` | Weekly Low=`7.97`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.59` (Distance: `-1.32%`)
  * Point of Control (POC) = `8.46` (Distance: `+0.25%`)
  * Value Area Low (VAL) = `8.24` (Distance: `+2.91%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`9.02` | Weekly POC=`8.92` | Weekly VAL=`8.69`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.58` | Low=`7.97`
  * London Session (08:00-16:00 UTC): High=`8.64` | Low=`8.42`
  * New York Session (13:00-21:00 UTC): High=`8.53` | Low=`8.43`
  * Initial Balance (First Hour): IB High=`8.59` | IB Low=`8.50`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.45` - `8.51`
  * Optimal Trade Entry (OTE 0.705): `8.50`
  * Structural Invalidation Anchor (0.786): `8.55`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.47` | `8.48` | `8.46` | `8.48` | `51,880` | 439,359.54 USD | -248,653.12 USD | `-56.59%` | -5,865,796.20 USD | `-2.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `8.48` | `8.48` | `8.46` | `8.48` | `22,356` | 189,458.93 USD | 17,310.16 USD | `+9.14%` | -5,848,486.04 USD | `+0.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `8.48` | `8.49` | `8.47` | `8.49` | `32,483` | 275,493.04 USD | 60,755.96 USD | `+22.05%` | -5,787,730.08 USD | `+0.86` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.46` | `8.48` | `8.46` | `8.47` | `94,312` | 798,371.69 USD | 113,279.23 USD | `+14.19%` | -5,447,491.78 USD | `+0.28` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `8.47` | `8.48` | `8.44` | `8.47` | `121,611` | 1,028,869.35 USD | -169,651.30 USD | `-16.49%` | -5,617,143.08 USD | `-0.37` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `8.47` | `8.49` | `8.46` | `8.49` | `106,719` | 904,311.51 USD | -170,587.00 USD | `-18.86%` | -5,787,730.08 USD | `-0.39` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `8.63` | `8.63` | `8.48` | `8.50` | `671,897` | 5,750,861.25 USD | -1,429,699.87 USD | `-24.86%` | -5,391,829.51 USD | `-0.68` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `8.50` | `8.52` | `8.45` | `8.48` | `439,030` | 3,723,872.89 USD | -159,958.73 USD | `-4.30%` | -5,551,788.23 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `8.48` | `8.51` | `8.44` | `8.49` | `405,529` | 3,434,409.77 USD | -235,950.33 USD | `-6.87%` | -5,787,738.57 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.52` | `8.44` | `8.49` | `844,558` | 7,158,274.17 USD | -395,900.58 USD | `-5.53%` | -5,800,740.58 USD | `+0.39` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,565,817.62 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,901,763.44 USD | `-0.98` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.52` | `8.44` | `8.49` | `844,558` | 7,158,274.17 USD | -395,900.58 USD | `-5.53%` | -5,800,740.58 USD | `+0.39` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`8.48`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BUY` | `8.32` | `2255.8600` | 18,770.11 USD | 3,492,321.28 USD | `STANDARD` | `-1.94%` | `0xd3943e4008` |
| `BUY` | `8.33` | `398.6500` | 3,321.27 USD | 4,351,608.75 USD | `STANDARD` | `-1.81%` | `0x14f8e04290` |
| `BUY` | `8.34` | `14306.3000` | 119,338.86 USD | 2,688,317.36 USD | `LARGE (>= USD 100K)` | `-1.69%` | `0xecb63caa47` |
| `BUY` | `8.34` | `315.7300` | 2,632.56 USD | 4,379,967.95 USD | `STANDARD` | `-1.73%` | `0x07fd993f0f` |
| `BUY` | `8.35` | `213.4300` | 1,782.23 USD | 4,428,636.88 USD | `STANDARD` | `-1.59%` | `0xdadbb4b2a0` |
| `BUY` | `8.35` | `177.6800` | 1,483.82 USD | 4,443,574.02 USD | `STANDARD` | `-1.58%` | `0x010461c14e` |
| `BUY` | `8.36` | `17382.5900` | 145,259.35 USD | 1,658,566.70 USD | `LARGE (>= USD 100K)` | `-1.51%` | `0x71d0e11ebb` |
| `BUY` | `8.36` | `9789.1100` | 81,826.19 USD | 3,060,752.36 USD | `MEDIUM (>= USD 25K)` | `-1.49%` | `0xecb63caa47` |
| `BUY` | `8.36` | `2273.1800` | 18,999.92 USD | 3,435,966.79 USD | `STANDARD` | `-1.49%` | `0x0efb38a5fa` |
| `BUY` | `8.36` | `190.1400` | 1,588.79 USD | 4,442,090.20 USD | `STANDARD` | `-1.52%` | `0x31ca8395cf` |
| `BUY` | `8.37` | `956.7600` | 8,012.10 USD | 4,152,592.56 USD | `STANDARD` | `-1.31%` | `0xd2ccf2ebc5` |
| `BUY` | `8.38` | `31739.4500` | 266,084.51 USD | 1,069,306.01 USD | `LARGE (>= USD 100K)` | `-1.20%` | `0x71cfa5e263` |
| `BUY` | `8.38` | `10784.3800` | 90,328.89 USD | 2,978,926.17 USD | `MEDIUM (>= USD 25K)` | `-1.29%` | `0xecb63caa47` |
| `BUY` | `8.38` | `7552.0600` | 63,265.87 USD | 3,188,820.04 USD | `MEDIUM (>= USD 25K)` | `-1.27%` | `0x71d0e11ebb` |
| `BUY` | `8.38` | `4249.2900` | 35,610.32 USD | 3,260,804.68 USD | `MEDIUM (>= USD 25K)` | `-1.23%` | `0xa24c5ca26c` |
| `BUY` | `8.38` | `1908.4600` | 15,999.96 USD | 3,544,500.33 USD | `STANDARD` | `-1.19%` | `0x0efb38a5fa` |
| `BUY` | `8.39` | `14719.7700` | 123,541.56 USD | 2,568,978.50 USD | `LARGE (>= USD 100K)` | `-1.08%` | `0xecb63caa47` |
| `BUY` | `8.39` | `1676.4600` | 14,063.15 USD | 3,659,766.90 USD | `STANDARD` | `-1.14%` | `0xd3943e4008` |
| `BUY` | `8.39` | `400.3400` | 3,360.65 USD | 4,344,942.92 USD | `STANDARD` | `-1.07%` | `0x14f8e04290` |
| `BUY` | `8.39` | `398.6500` | 3,344.55 USD | 4,348,287.47 USD | `STANDARD` | `-1.12%` | `0x14f8e04290` |
| `BUY` | `8.39` | `315.7300` | 2,650.55 USD | 4,374,690.65 USD | `STANDARD` | `-1.06%` | `0x07fd993f0f` |
| `BUY` | `8.39` | `77.4600` | 650.21 USD | 4,501,823.82 USD | `STANDARD` | `-1.07%` | `0x010461c14e` |
| `BUY` | `8.40` | `17372.0500` | 145,913.06 USD | 1,513,307.34 USD | `LARGE (>= USD 100K)` | `-1.01%` | `0x71d0e11ebb` |
| `BUY` | `8.40` | `1435.7400` | 12,060.07 USD | 3,922,012.41 USD | `STANDARD` | `-1.00%` | `0xd3943e4008` |
| `BUY` | `8.40` | `83.2400` | 699.04 USD | 4,497,780.14 USD | `STANDARD` | `-1.03%` | `0x31ca8395cf` |
| `BUY` | `8.41` | `11907.8300` | 100,141.28 USD | 2,788,458.64 USD | `LARGE (>= USD 100K)` | `-0.89%` | `0x881cd92459` |
| `BUY` | `8.41` | `2233.3100` | 18,792.19 USD | 3,473,551.17 USD | `STANDARD` | `-0.83%` | `0xa38f19c4cc` |
| `BUY` | `8.42` | `16193.6400` | 136,415.22 USD | 1,932,978.60 USD | `LARGE (>= USD 100K)` | `-0.72%` | `0x71cfa5e263` |
| `BUY` | `8.42` | `1424.8500` | 11,999.94 USD | 3,946,012.35 USD | `STANDARD` | `-0.74%` | `0x0efb38a5fa` |
| `BUY` | `8.42` | `1185.5200` | 9,987.77 USD | 4,091,645.23 USD | `STANDARD` | `-0.71%` | `0xd3943e4008` |
| `BUY` | `8.42` | `400.2800` | 3,372.00 USD | 4,341,582.27 USD | `STANDARD` | `-0.72%` | `0x14f8e04290` |
| `BUY` | `8.43` | `3644.3200` | 30,716.15 USD | 3,291,520.83 USD | `MEDIUM (>= USD 25K)` | `-0.67%` | `0x26934acbd3` |
| `BUY` | `8.43` | `1310.8700` | 11,054.17 USD | 3,957,066.52 USD | `STANDARD` | `-0.62%` | `0xa38f19c4cc` |
| `BUY` | `8.43` | `468.9500` | 3,952.36 USD | 4,284,256.75 USD | `STANDARD` | `-0.67%` | `0xcd7f60e943` |
| `BUY` | `8.44` | `15094.1600` | 127,335.84 USD | 2,445,436.94 USD | `LARGE (>= USD 100K)` | `-0.58%` | `0x71d0e11ebb` |
| `BUY` | `8.44` | `947.3200` | 7,999.93 USD | 4,168,592.44 USD | `STANDARD` | `-0.47%` | `0x0efb38a5fa` |
| `BUY` | `8.44` | `770.0600` | 6,502.46 USD | 4,190,531.24 USD | `STANDARD` | `-0.48%` | `0xa38f19c4cc` |
| `BUY` | `8.44` | `86.4100` | 729.49 USD | 4,463,083.64 USD | `STANDARD` | `-0.50%` | `0x010461c14e` |
| `BUY` | `8.44` | `76.9900` | 649.63 USD | 4,502,473.45 USD | `STANDARD` | `-0.55%` | `0x31ca8395cf` |
| `BUY` | `8.45` | `1652.6700` | 13,970.35 USD | 3,855,923.29 USD | `STANDARD` | `-0.37%` | `0x57d8e75f47` |
| `BUY` | `8.45` | `1652.6700` | 13,965.89 USD | 3,883,857.81 USD | `STANDARD` | `-0.41%` | `0x57d8e75f47` |
| `BUY` | `8.45` | `1652.6700` | 13,960.93 USD | 3,897,818.74 USD | `STANDARD` | `-0.44%` | `0x57d8e75f47` |
| `BUY` | `8.45` | `1122.7000` | 9,481.99 USD | 4,101,127.22 USD | `STANDARD` | `-0.46%` | `0xd3943e4008` |
| `BUY` | `8.45` | `1045.4700` | 8,834.95 USD | 4,127,855.41 USD | `STANDARD` | `-0.40%` | `0xd3342d3b1e` |
| `BUY` | `8.45` | `997.2500` | 8,430.95 USD | 4,136,286.36 USD | `STANDARD` | `-0.36%` | `0xd3943e4008` |
| `BUY` | `8.45` | `735.9200` | 6,221.47 USD | 4,203,255.14 USD | `STANDARD` | `-0.36%` | `0x47a4471457` |
| `BUY` | `8.45` | `682.7200` | 5,769.05 USD | 4,215,245.65 USD | `STANDARD` | `-0.41%` | `0xecb63caa47` |
| `BUY` | `8.45` | `611.1400` | 5,164.56 USD | 4,226,019.42 USD | `STANDARD` | `-0.40%` | `0xecb63caa47` |
| `BUY` | `8.45` | `427.4200` | 3,611.91 USD | 4,320,932.43 USD | `STANDARD` | `-0.41%` | `0x2a72b57dea` |
| `BUY` | `8.45` | `236.5000` | 1,998.52 USD | 4,423,039.72 USD | `STANDARD` | `-0.41%` | `0x39bac00809` |
| `BUY` | `8.46` | `15096.3500` | 127,749.84 USD | 2,318,101.10 USD | `LARGE (>= USD 100K)` | `-0.27%` | `0x71d0e11ebb` |
| `BUY` | `8.46` | `3591.7200` | 30,389.90 USD | 3,352,326.95 USD | `MEDIUM (>= USD 25K)` | `-0.28%` | `0x08a49e7f71` |
| `BUY` | `8.46` | `1652.6700` | 13,983.74 USD | 3,813,998.36 USD | `STANDARD` | `-0.28%` | `0x57d8e75f47` |
| `BUY` | `8.46` | `1652.6700` | 13,979.77 USD | 3,827,978.13 USD | `STANDARD` | `-0.31%` | `0x57d8e75f47` |
| `BUY` | `8.46` | `1652.6700` | 13,974.81 USD | 3,841,952.94 USD | `STANDARD` | `-0.34%` | `0x57d8e75f47` |
| `BUY` | `8.46` | `1239.3400` | 10,489.53 USD | 4,000,661.11 USD | `STANDARD` | `-0.25%` | `0x26934acbd3` |
| `BUY` | `8.46` | `1197.9600` | 10,133.30 USD | 4,051,448.86 USD | `STANDARD` | `-0.31%` | `0xaf9f722a67` |
| `BUY` | `8.46` | `905.4600` | 7,657.20 USD | 4,184,028.78 USD | `STANDARD` | `-0.33%` | `0xecb63caa47` |
| `BUY` | `8.46` | `590.7000` | 4,999.92 USD | 4,246,038.20 USD | `STANDARD` | `-0.24%` | `0x0efb38a5fa` |
| `BUY` | `8.46` | `451.8900` | 3,824.93 USD | 4,291,906.68 USD | `STANDARD` | `-0.24%` | `0xa38f19c4cc` |
| `BUY` | `8.46` | `427.4200` | 3,616.32 USD | 4,317,320.52 USD | `STANDARD` | `-0.28%` | `0x2a72b57dea` |
| `BUY` | `8.46` | `288.0700` | 2,436.27 USD | 4,397,452.28 USD | `STANDARD` | `-0.33%` | `0xdd4f66125d` |
| `BUY` | `8.46` | `239.2100` | 2,024.24 USD | 4,419,035.73 USD | `STANDARD` | `-0.27%` | `0xecb63caa47` |
| `BUY` | `8.46` | `90.7300` | 767.35 USD | 4,456,346.75 USD | `STANDARD` | `-0.32%` | `0x010461c14e` |
| `BUY` | `8.46` | `87.3800` | 739.30 USD | 4,461,618.02 USD | `STANDARD` | `-0.28%` | `0x31ca8395cf` |
| `BUY` | `8.46` | `85.3900` | 722.60 USD | 4,491,316.48 USD | `STANDARD` | `-0.27%` | `0x63f6411ca6` |
| `BUY` | `8.46` | `63.9700` | 541.47 USD | 4,505,294.84 USD | `STANDARD` | `-0.24%` | `0xf30120f048` |
| `BUY` | `8.46` | `63.9700` | 541.43 USD | 4,505,836.27 USD | `STANDARD` | `-0.25%` | `0xfd66e33095` |
| `BUY` | `8.46` | `63.9700` | 541.38 USD | 4,506,377.65 USD | `STANDARD` | `-0.26%` | `0x53136b4a7c` |
| `BUY` | `8.47` | `1652.6700` | 14,003.57 USD | 3,772,023.35 USD | `STANDARD` | `-0.14%` | `0x57d8e75f47` |
| `BUY` | `8.47` | `1652.6700` | 13,999.60 USD | 3,786,022.95 USD | `STANDARD` | `-0.17%` | `0x57d8e75f47` |
| `BUY` | `8.47` | `1652.6700` | 13,991.67 USD | 3,800,014.62 USD | `STANDARD` | `-0.22%` | `0x57d8e75f47` |
| `BUY` | `8.47` | `1301.3400` | 11,025.34 USD | 3,990,171.58 USD | `STANDARD` | `-0.15%` | `0x08a49e7f71` |
| `BUY` | `8.47` | `1197.9600` | 10,143.37 USD | 4,041,315.56 USD | `STANDARD` | `-0.21%` | `0xaf9f722a67` |
| `BUY` | `8.47` | `481.6400` | 4,078.67 USD | 4,272,247.71 USD | `STANDARD` | `-0.20%` | `0x7717a7a245` |
| `BUY` | `8.47` | `427.4200` | 3,621.66 USD | 4,313,704.21 USD | `STANDARD` | `-0.14%` | `0x2a72b57dea` |
| `BUY` | `8.47` | `301.0600` | 2,550.34 USD | 4,385,137.52 USD | `STANDARD` | `-0.16%` | `0x26934acbd3` |
| `BUY` | `8.47` | `295.0000` | 2,499.98 USD | 4,390,137.49 USD | `STANDARD` | `-0.12%` | `0x0efb38a5fa` |
| `BUY` | `8.47` | `288.0700` | 2,439.32 USD | 4,392,576.81 USD | `STANDARD` | `-0.20%` | `0xdd4f66125d` |
| `BUY` | `8.47` | `288.0700` | 2,439.20 USD | 4,395,016.01 USD | `STANDARD` | `-0.21%` | `0xdd4f66125d` |
| `BUY` | `8.47` | `270.3700` | 2,289.68 USD | 4,399,741.96 USD | `STANDARD` | `-0.19%` | `0xecb63caa47` |
| `BUY` | `8.47` | `267.4900` | 2,265.88 USD | 4,402,007.84 USD | `STANDARD` | `-0.17%` | `0xecb63caa47` |
| `BUY` | `8.47` | `265.5700` | 2,249.94 USD | 4,406,507.75 USD | `STANDARD` | `-0.15%` | `0xa38f19c4cc` |
| `BUY` | `8.47` | `240.9700` | 2,041.74 USD | 4,414,973.07 USD | `STANDARD` | `-0.14%` | `0xecb63caa47` |
| `BUY` | `8.47` | `240.7600` | 2,038.42 USD | 4,417,011.49 USD | `STANDARD` | `-0.22%` | `0xecb63caa47` |
| `BUY` | `8.47` | `200.0000` | 1,694.88 USD | 4,437,197.77 USD | `STANDARD` | `-0.12%` | `0xfc27136e42` |
| `BUY` | `8.47` | `200.0000` | 1,694.52 USD | 4,438,892.29 USD | `STANDARD` | `-0.15%` | `0xfc27136e42` |
| `BUY` | `8.47` | `85.3000` | 722.91 USD | 4,487,702.62 USD | `STANDARD` | `-0.12%` | `0xfd66e33095` |
| `BUY` | `8.47` | `85.3000` | 722.85 USD | 4,488,425.47 USD | `STANDARD` | `-0.13%` | `0x9d81a3adf8` |
| `BUY` | `8.47` | `85.3000` | 722.83 USD | 4,489,148.30 USD | `STANDARD` | `-0.13%` | `0x63f6411ca6` |
| `BUY` | `8.47` | `85.3000` | 722.78 USD | 4,490,593.88 USD | `STANDARD` | `-0.14%` | `0x53136b4a7c` |
| `BUY` | `8.47` | `85.3000` | 722.41 USD | 4,492,038.89 USD | `STANDARD` | `-0.19%` | `0xea0e878d5d` |
| `BUY` | `8.47` | `85.3000` | 722.39 USD | 4,492,761.28 USD | `STANDARD` | `-0.19%` | `0x53136b4a7c` |
| `BUY` | `8.47` | `85.3000` | 722.31 USD | 4,493,483.59 USD | `STANDARD` | `-0.20%` | `0xea0e878d5d` |
| `BUY` | `8.47` | `85.3000` | 722.26 USD | 4,494,205.85 USD | `STANDARD` | `-0.21%` | `0x9d81a3adf8` |
| `BUY` | `8.47` | `85.3000` | 722.19 USD | 4,494,928.05 USD | `STANDARD` | `-0.22%` | `0xfd66e33095` |
| `BUY` | `8.47` | `85.3000` | 722.17 USD | 4,495,650.21 USD | `STANDARD` | `-0.22%` | `0xf30120f048` |
| `BUY` | `8.47` | `79.7400` | 675.41 USD | 4,499,828.91 USD | `STANDARD` | `-0.17%` | `0x31ca8395cf` |
| `BUY` | `8.47` | `75.4300` | 638.91 USD | 4,503,112.36 USD | `STANDARD` | `-0.17%` | `0x010461c14e` |
| `BUY` | `8.47` | `60.3400` | 511.28 USD | 4,509,967.08 USD | `STANDARD` | `-0.14%` | `0x57d8e75f47` |
| `BUY` | `8.47` | `60.3400` | 510.87 USD | 4,510,477.95 USD | `STANDARD` | `-0.22%` | `0x57d8e75f47` |
| `MID_SPREAD` | `8.48` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.48` | `0.00%` | `-` |
| `BID` | `8.48` | `270.2700` | 2,292.94 USD | 2,292.94 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `8.48` | `85.3000` | 723.67 USD | 3,016.61 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.48` | `120.0800` | 1,018.69 USD | 4,035.30 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.48` | `85.3000` | 723.63 USD | 4,758.92 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.48` | `117.8800` | 999.94 USD | 5,758.86 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.48` | `85.3000` | 723.57 USD | 6,482.43 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.48` | `153.6700` | 1,303.48 USD | 7,785.91 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.48` | `50.0000` | 424.11 USD | 8,210.01 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.48` | `85.3000` | 723.51 USD | 8,933.52 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.48` | `126.0200` | 1,068.86 USD | 10,002.38 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `8.48` | `5.5100` | 46.73 USD | 10,049.11 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.48` | `85.3000` | 723.43 USD | 10,772.54 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.48` | `19.6200` | 166.40 USD | 10,938.94 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.48` | `50.0000` | 424.04 USD | 11,362.98 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.48` | `50.0000` | 424.04 USD | 11,787.01 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.48` | `50.0000` | 424.03 USD | 12,211.04 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.48` | `141.1000` | 1,196.60 USD | 13,407.64 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `8.48` | `1713.0100` | 14,527.01 USD | 27,934.65 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.48` | `85.3000` | 723.33 USD | 28,657.98 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.48` | `85.3000` | 723.31 USD | 29,381.29 USD | `1 orders` | `-0.06%` | `-` |
| `BUY` | `8.48` | `1652.6700` | 14,015.30 USD | 3,744,010.26 USD | `STANDARD` | `-0.05%` | `0x57d8e75f47` |
| `BUY` | `8.48` | `1652.6700` | 14,009.52 USD | 3,758,019.78 USD | `STANDARD` | `-0.09%` | `0x57d8e75f47` |
| `BUY` | `8.48` | `1197.9600` | 10,153.55 USD | 4,031,172.19 USD | `STANDARD` | `-0.11%` | `0xaf9f722a67` |
| `BUY` | `8.48` | `1186.1000` | 10,055.99 USD | 4,081,657.46 USD | `STANDARD` | `-0.08%` | `0x621c555167` |
| `BUY` | `8.48` | `589.7000` | 4,999.95 USD | 4,241,038.28 USD | `STANDARD` | `-0.07%` | `0x44f481f406` |
| `BUY` | `8.48` | `495.4000` | 4,199.21 USD | 4,264,073.60 USD | `STANDARD` | `-0.10%` | `0x71d0e11ebb` |
| `BUY` | `8.48` | `312.0500` | 2,644.75 USD | 4,377,335.40 USD | `STANDARD` | `-0.11%` | `0x7717a7a245` |
| `BUY` | `8.48` | `222.5700` | 1,887.97 USD | 4,426,854.65 USD | `STANDARD` | `-0.03%` | `0x414ade317c` |
| `BUY` | `8.48` | `200.0000` | 1,695.06 USD | 4,435,502.89 USD | `STANDARD` | `-0.11%` | `0xfc27136e42` |
| `BUY` | `8.48` | `153.6700` | 1,303.48 USD | 4,444,877.50 USD | `STANDARD` | `-0.03%` | `0xecb63caa47` |
| `BUY` | `8.48` | `150.1900` | 1,274.20 USD | 4,446,151.70 USD | `STANDARD` | `-0.01%` | `0x727956612a` |
| `BUY` | `8.48` | `120.0800` | 1,018.75 USD | 4,449,425.09 USD | `STANDARD` | `-0.01%` | `0x7717a7a245` |
| `BUY` | `8.48` | `117.8800` | 999.94 USD | 4,450,425.03 USD | `STANDARD` | `-0.03%` | `0x0eecd62efb` |
| `BUY` | `8.48` | `85.3900` | 723.98 USD | 4,474,681.18 USD | `STANDARD` | `-0.08%` | `0xf30120f048` |
| `BUY` | `8.48` | `85.3900` | 723.84 USD | 4,476,852.81 USD | `STANDARD` | `-0.09%` | `0x63f6411ca6` |
| `BUY` | `8.48` | `85.3000` | 723.67 USD | 4,477,576.48 USD | `STANDARD` | `-0.01%` | `0xf30120f048` |
| `BUY` | `8.48` | `85.3000` | 723.63 USD | 4,478,300.11 USD | `STANDARD` | `-0.02%` | `0xfd66e33095` |
| `BUY` | `8.48` | `85.3000` | 723.57 USD | 4,479,023.67 USD | `STANDARD` | `-0.03%` | `0xfd66e33095` |
| `BUY` | `8.48` | `85.3000` | 723.51 USD | 4,479,747.18 USD | `STANDARD` | `-0.04%` | `0xf30120f048` |
| `BUY` | `8.48` | `85.3000` | 723.49 USD | 4,480,470.67 USD | `STANDARD` | `-0.04%` | `0xfd66e33095` |
| `BUY` | `8.48` | `85.3000` | 723.43 USD | 4,481,194.10 USD | `STANDARD` | `-0.05%` | `0xfd66e33095` |
| `BUY` | `8.48` | `85.3000` | 723.39 USD | 4,481,917.49 USD | `STANDARD` | `-0.05%` | `0xea0e878d5d` |
| `BUY` | `8.48` | `85.3000` | 723.33 USD | 4,482,640.81 USD | `STANDARD` | `-0.06%` | `0xea0e878d5d` |
| `BUY` | `8.48` | `85.3000` | 723.31 USD | 4,483,364.12 USD | `STANDARD` | `-0.06%` | `0xd0956a1eba` |
| `BUY` | `8.48` | `85.3000` | 723.25 USD | 4,484,087.37 USD | `STANDARD` | `-0.07%` | `0xd0956a1eba` |
| `BUY` | `8.48` | `85.3000` | 723.20 USD | 4,484,810.57 USD | `STANDARD` | `-0.08%` | `0xf30120f048` |
| `BUY` | `8.48` | `85.3000` | 723.14 USD | 4,485,533.71 USD | `STANDARD` | `-0.09%` | `0xfd66e33095` |
| `BUY` | `8.48` | `85.3000` | 723.01 USD | 4,486,256.72 USD | `STANDARD` | `-0.10%` | `0xd0956a1eba` |
| `BUY` | `8.48` | `85.3000` | 722.99 USD | 4,486,979.71 USD | `STANDARD` | `-0.11%` | `0xea0e878d5d` |
| `BUY` | `8.48` | `84.7900` | 718.95 USD | 4,496,369.17 USD | `STANDARD` | `-0.07%` | `0x31ca8395cf` |
| `BUY` | `8.48` | `79.2500` | 671.98 USD | 4,501,173.60 USD | `STANDARD` | `-0.07%` | `0x010461c14e` |
| `BUY` | `8.48` | `60.3400` | 511.71 USD | 4,508,944.31 USD | `STANDARD` | `-0.05%` | `0x57d8e75f47` |
| `BUY` | `8.48` | `60.3400` | 511.50 USD | 4,509,455.80 USD | `STANDARD` | `-0.09%` | `0x57d8e75f47` |
| `ASK` | `8.49` | `91.7000` | 778.62 USD | 33,139.33 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.49` | `120.0800` | 1,019.54 USD | 32,360.72 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.49` | `91.7000` | 778.57 USD | 31,341.18 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.49` | `1737.9700` | 14,755.54 USD | 30,562.61 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.49` | `200.0000` | 1,697.94 USD | 15,807.07 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.49` | `174.9900` | 1,485.60 USD | 14,109.13 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.49` | `85.3900` | 724.91 USD | 12,623.54 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.49` | `66.5800` | 565.22 USD | 11,898.63 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.49` | `8.8300` | 74.96 USD | 11,333.41 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.49` | `56.6000` | 480.47 USD | 11,258.45 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.49` | `85.3800` | 724.77 USD | 10,777.98 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.49` | `539.5200` | 4,579.77 USD | 10,053.22 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.49` | `60.9400` | 517.27 USD | 5,473.45 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.49` | `50.0000` | 424.40 USD | 4,956.18 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.49` | `22.0900` | 187.50 USD | 4,531.77 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.49` | `85.3000` | 724.00 USD | 4,344.28 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.49` | `131.7800` | 1,118.42 USD | 3,620.28 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `8.49` | `63.9700` | 542.89 USD | 2,501.86 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.49` | `145.5400` | 1,235.11 USD | 1,958.97 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.49` | `85.3000` | 723.86 USD | 723.86 USD | `1 orders` | `+0.01%` | `-` |
| `SELL` | `8.49` | `1652.6700` | 14,037.28 USD | 3,715,963.63 USD | `STANDARD` | `+0.10%` | `0x57d8e75f47` |
| `SELL` | `8.49` | `1652.6700` | 14,031.33 USD | 3,729,994.96 USD | `STANDARD` | `+0.06%` | `0x57d8e75f47` |
| `SELL` | `8.49` | `1298.0400` | 11,025.55 USD | 3,979,146.24 USD | `STANDARD` | `+0.11%` | `0x08a49e7f71` |
| `SELL` | `8.49` | `1197.9600` | 10,173.68 USD | 4,021,018.64 USD | `STANDARD` | `+0.09%` | `0xaf9f722a67` |
| `SELL` | `8.49` | `1186.1000` | 10,074.73 USD | 4,071,601.47 USD | `STANDARD` | `+0.11%` | `0x621c555167` |
| `SELL` | `8.49` | `427.4200` | 3,630.38 USD | 4,306,454.35 USD | `STANDARD` | `+0.10%` | `0x2a72b57dea` |
| `SELL` | `8.49` | `427.4200` | 3,628.20 USD | 4,310,082.55 USD | `STANDARD` | `+0.04%` | `0x2a72b57dea` |
| `SELL` | `8.49` | `294.4000` | 2,499.99 USD | 4,387,637.51 USD | `STANDARD` | `+0.08%` | `0x0efb38a5fa` |
| `SELL` | `8.49` | `264.9300` | 2,249.97 USD | 4,404,257.81 USD | `STANDARD` | `+0.09%` | `0xa38f19c4cc` |
| `SELL` | `8.49` | `200.0000` | 1,697.94 USD | 4,433,807.83 USD | `STANDARD` | `+0.06%` | `0xfc27136e42` |
| `SELL` | `8.49` | `145.5400` | 1,235.11 USD | 4,447,386.81 USD | `STANDARD` | `+0.02%` | `0x727956612a` |
| `SELL` | `8.49` | `120.0800` | 1,019.54 USD | 4,448,406.35 USD | `STANDARD` | `+0.07%` | `0x7717a7a245` |
| `SELL` | `8.49` | `117.7400` | 999.92 USD | 4,451,424.95 USD | `STANDARD` | `+0.09%` | `0x0eecd62efb` |
| `SELL` | `8.49` | `112.1000` | 951.57 USD | 4,452,376.52 USD | `STANDARD` | `+0.04%` | `0xecb63caa47` |
| `SELL` | `8.49` | `102.0900` | 866.99 USD | 4,453,243.51 USD | `STANDARD` | `+0.09%` | `0x44f481f406` |
| `SELL` | `8.49` | `91.7000` | 778.70 USD | 4,454,022.21 USD | `STANDARD` | `+0.08%` | `0xdd4f66125d` |
| `SELL` | `8.49` | `91.7000` | 778.62 USD | 4,454,800.83 USD | `STANDARD` | `+0.07%` | `0xdd4f66125d` |
| `SELL` | `8.49` | `91.7000` | 778.57 USD | 4,455,579.40 USD | `STANDARD` | `+0.06%` | `0xdd4f66125d` |
| `SELL` | `8.49` | `89.8500` | 762.79 USD | 4,457,874.50 USD | `STANDARD` | `+0.05%` | `0x31ca8395cf` |
| `SELL` | `8.49` | `85.3900` | 724.91 USD | 4,466,712.99 USD | `STANDARD` | `+0.05%` | `0xf30120f048` |
| `SELL` | `8.49` | `85.3800` | 724.77 USD | 4,468,162.60 USD | `STANDARD` | `+0.04%` | `0xea0e878d5d` |
| `SELL` | `8.49` | `85.3000` | 724.50 USD | 4,468,887.10 USD | `STANDARD` | `+0.10%` | `0xfd66e33095` |
| `SELL` | `8.49` | `85.3000` | 724.46 USD | 4,469,611.56 USD | `STANDARD` | `+0.10%` | `0x9d81a3adf8` |
| `SELL` | `8.49` | `85.3000` | 724.40 USD | 4,470,335.96 USD | `STANDARD` | `+0.09%` | `0x63f6411ca6` |
| `SELL` | `8.49` | `85.3000` | 724.39 USD | 4,471,060.36 USD | `STANDARD` | `+0.09%` | `0xea0e878d5d` |
| `SELL` | `8.49` | `85.3000` | 724.34 USD | 4,471,784.70 USD | `STANDARD` | `+0.08%` | `0x63f6411ca6` |
| `SELL` | `8.49` | `85.3000` | 724.29 USD | 4,472,508.99 USD | `STANDARD` | `+0.07%` | `0x9d81a3adf8` |
| `SELL` | `8.49` | `85.3000` | 724.21 USD | 4,473,233.20 USD | `STANDARD` | `+0.06%` | `0x53136b4a7c` |
| `SELL` | `8.49` | `85.3000` | 724.00 USD | 4,473,957.20 USD | `STANDARD` | `+0.03%` | `0x63f6411ca6` |
| `SELL` | `8.49` | `85.3000` | 723.94 USD | 4,475,405.12 USD | `STANDARD` | `+0.02%` | `0x53136b4a7c` |
| `SELL` | `8.49` | `85.3000` | 723.86 USD | 4,476,128.97 USD | `STANDARD` | `+0.01%` | `0xf30120f048` |
| `SELL` | `8.49` | `85.1400` | 722.80 USD | 4,489,871.10 USD | `STANDARD` | `+0.05%` | `0x010461c14e` |
| `SELL` | `8.49` | `83.8400` | 711.94 USD | 4,497,081.10 USD | `STANDARD` | `+0.08%` | `0x47472cd62c` |
| `SELL` | `8.49` | `63.9700` | 542.89 USD | 4,504,753.37 USD | `STANDARD` | `+0.02%` | `0x63f6411ca6` |
| `SELL` | `8.49` | `60.9400` | 517.27 USD | 4,506,894.92 USD | `STANDARD` | `+0.04%` | `0xf30120f048` |
| `SELL` | `8.49` | `60.3400` | 512.51 USD | 4,507,920.35 USD | `STANDARD` | `+0.10%` | `0x57d8e75f47` |
| `SELL` | `8.49` | `60.3400` | 512.24 USD | 4,508,432.60 USD | `STANDARD` | `+0.05%` | `0x57d8e75f47` |
| `SELL` | `8.50` | `3578.2100` | 30,416.22 USD | 3,321,937.05 USD | `MEDIUM (>= USD 25K)` | `+0.18%` | `0x08a49e7f71` |
| `SELL` | `8.50` | `1652.6700` | 14,053.15 USD | 3,687,881.13 USD | `STANDARD` | `+0.22%` | `0x57d8e75f47` |
| `SELL` | `8.50` | `1652.6700` | 14,045.22 USD | 3,701,926.34 USD | `STANDARD` | `+0.16%` | `0x57d8e75f47` |
| `SELL` | `8.50` | `1197.9600` | 10,183.86 USD | 4,010,844.97 USD | `STANDARD` | `+0.19%` | `0xaf9f722a67` |
| `SELL` | `8.50` | `764.7400` | 6,502.43 USD | 4,197,033.67 USD | `STANDARD` | `+0.21%` | `0xa38f19c4cc` |
| `SELL` | `8.50` | `588.0900` | 4,996.30 USD | 4,251,034.50 USD | `STANDARD` | `+0.13%` | `0x44f481f406` |
| `SELL` | `8.50` | `495.5300` | 4,210.37 USD | 4,259,874.40 USD | `STANDARD` | `+0.14%` | `0x71d0e11ebb` |
| `SELL` | `8.50` | `481.6400` | 4,095.43 USD | 4,268,169.04 USD | `STANDARD` | `+0.21%` | `0x7717a7a245` |
| `SELL` | `8.50` | `450.1800` | 3,825.00 USD | 4,288,081.75 USD | `STANDARD` | `+0.14%` | `0xa38f19c4cc` |
| `SELL` | `8.50` | `427.4200` | 3,634.74 USD | 4,302,823.97 USD | `STANDARD` | `+0.22%` | `0x2a72b57dea` |
| `SELL` | `8.50` | `420.7900` | 3,574.78 USD | 4,324,507.21 USD | `STANDARD` | `+0.12%` | `0xecb63caa47` |
| `SELL` | `8.50` | `366.8200` | 3,118.67 USD | 4,357,848.72 USD | `STANDARD` | `+0.20%` | `0xdd4f66125d` |
| `SELL` | `8.50` | `366.8200` | 3,118.19 USD | 4,360,966.91 USD | `STANDARD` | `+0.18%` | `0xdd4f66125d` |
| `SELL` | `8.50` | `312.0500` | 2,650.99 USD | 4,372,040.10 USD | `STANDARD` | `+0.12%` | `0x7717a7a245` |
| `SELL` | `8.50` | `308.2100` | 2,619.23 USD | 4,382,587.18 USD | `STANDARD` | `+0.16%` | `0xecb63caa47` |
| `SELL` | `8.50` | `262.2900` | 2,229.70 USD | 4,408,737.45 USD | `STANDARD` | `+0.19%` | `0xecb63caa47` |
| `SELL` | `8.50` | `252.7700` | 2,149.05 USD | 4,410,886.50 USD | `STANDARD` | `+0.20%` | `0xecb63caa47` |
| `SELL` | `8.50` | `240.4300` | 2,044.83 USD | 4,412,931.33 USD | `STANDARD` | `+0.24%` | `0xecb63caa47` |
| `SELL` | `8.50` | `89.3300` | 759.00 USD | 4,458,633.50 USD | `STANDARD` | `+0.14%` | `0x31ca8395cf` |
| `SELL` | `8.50` | `85.6000` | 727.31 USD | 4,463,810.95 USD | `STANDARD` | `+0.14%` | `0x010461c14e` |
| `SELL` | `8.50` | `85.3900` | 725.82 USD | 4,464,536.77 USD | `STANDARD` | `+0.18%` | `0x9d81a3adf8` |
| `SELL` | `8.50` | `85.3900` | 725.67 USD | 4,465,262.44 USD | `STANDARD` | `+0.16%` | `0xa382fa9f4b` |
| `SELL` | `8.50` | `85.3900` | 725.64 USD | 4,465,988.08 USD | `STANDARD` | `+0.15%` | `0xea0e878d5d` |
| `SELL` | `8.50` | `85.3000` | 724.84 USD | 4,467,437.83 USD | `STANDARD` | `+0.15%` | `0xa382fa9f4b` |
| `SELL` | `8.50` | `79.1400` | 672.71 USD | 4,500,501.63 USD | `STANDARD` | `+0.18%` | `0x31ca8395cf` |
| `SELL` | `8.50` | `63.9700` | 543.75 USD | 4,504,210.47 USD | `STANDARD` | `+0.18%` | `0x53136b4a7c` |
| `SELL` | `8.50` | `60.3400` | 512.92 USD | 4,507,407.85 USD | `STANDARD` | `+0.18%` | `0x57d8e75f47` |
| `SELL` | `8.51` | `15104.7200` | 128,498.87 USD | 2,190,351.26 USD | `LARGE (>= USD 100K)` | `+0.26%` | `0x71d0e11ebb` |
| `SELL` | `8.51` | `1652.6700` | 14,069.01 USD | 3,645,703.74 USD | `STANDARD` | `+0.33%` | `0x57d8e75f47` |
| `SELL` | `8.51` | `1652.6700` | 14,061.08 USD | 3,673,827.98 USD | `STANDARD` | `+0.27%` | `0x57d8e75f47` |
| `SELL` | `8.51` | `1298.5500` | 11,054.17 USD | 3,968,120.69 USD | `STANDARD` | `+0.33%` | `0xa38f19c4cc` |
| `SELL` | `8.51` | `1054.8900` | 8,981.86 USD | 4,110,109.08 USD | `STANDARD` | `+0.35%` | `0xd3943e4008` |
| `SELL` | `8.51` | `975.1000` | 8,294.10 USD | 4,144,580.46 USD | `STANDARD` | `+0.25%` | `0xd3943e4008` |
| `SELL` | `8.51` | `587.7700` | 4,999.98 USD | 4,236,038.33 USD | `STANDARD` | `+0.26%` | `0x0efb38a5fa` |
| `SELL` | `8.51` | `543.9400` | 4,629.53 USD | 4,255,664.03 USD | `STANDARD` | `+0.31%` | `0xecb63caa47` |
| `SELL` | `8.51` | `477.0200` | 4,059.92 USD | 4,276,307.63 USD | `STANDARD` | `+0.31%` | `0x6abc111bd2` |
| `SELL` | `8.51` | `427.4200` | 3,639.10 USD | 4,299,189.24 USD | `STANDARD` | `+0.34%` | `0x2a72b57dea` |
| `SELL` | `8.51` | `366.8200` | 3,121.31 USD | 4,354,730.05 USD | `STANDARD` | `+0.28%` | `0xdd4f66125d` |
| `SELL` | `8.51` | `86.5100` | 736.13 USD | 4,462,354.15 USD | `STANDARD` | `+0.29%` | `0x31ca8395cf` |
| `SELL` | `8.51` | `81.1100` | 689.91 USD | 4,498,470.05 USD | `STANDARD` | `+0.25%` | `0x010461c14e` |
| `SELL` | `8.52` | `2132.5200` | 18,171.20 USD | 3,510,492.48 USD | `STANDARD` | `+0.42%` | `0xb45f5c538d` |
| `SELL` | `8.52` | `1652.6700` | 14,084.88 USD | 3,617,557.78 USD | `STANDARD` | `+0.44%` | `0x57d8e75f47` |
| `SELL` | `8.52` | `1652.6700` | 14,076.95 USD | 3,631,634.73 USD | `STANDARD` | `+0.39%` | `0x57d8e75f47` |
| `SELL` | `8.52` | `1640.3000` | 13,968.63 USD | 3,869,891.92 USD | `STANDARD` | `+0.36%` | `0xb45f5c538d` |
| `SELL` | `8.52` | `1045.4700` | 8,911.38 USD | 4,119,020.46 USD | `STANDARD` | `+0.46%` | `0xd3342d3b1e` |
| `SELL` | `8.52` | `913.5800` | 7,779.13 USD | 4,176,371.57 USD | `STANDARD` | `+0.35%` | `0xecb63caa47` |
| `SELL` | `8.52` | `730.4500` | 6,221.46 USD | 4,209,476.60 USD | `STANDARD` | `+0.38%` | `0x47a4471457` |
| `SELL` | `8.52` | `658.2800` | 5,609.20 USD | 4,220,854.86 USD | `STANDARD` | `+0.42%` | `0xecb63caa47` |
| `SELL` | `8.52` | `468.9500` | 3,996.77 USD | 4,280,304.39 USD | `STANDARD` | `+0.45%` | `0xcd7f60e943` |
| `SELL` | `8.52` | `427.4200` | 3,643.46 USD | 4,295,550.14 USD | `STANDARD` | `+0.46%` | `0x2a72b57dea` |
| `SELL` | `8.52` | `88.5800` | 755.12 USD | 4,459,388.61 USD | `STANDARD` | `+0.47%` | `0x31ca8395cf` |
| `SELL` | `8.52` | `86.9700` | 741.38 USD | 4,460,878.71 USD | `STANDARD` | `+0.47%` | `0x010461c14e` |
| `SELL` | `8.53` | `16181.6000` | 137,996.68 USD | 1,796,563.38 USD | `LARGE (>= USD 100K)` | `+0.51%` | `0x71cfa5e263` |
| `SELL` | `8.53` | `15101.5700` | 128,873.78 USD | 2,061,852.38 USD | `LARGE (>= USD 100K)` | `+0.58%` | `0x71d0e11ebb` |
| `SELL` | `8.53` | `2772.6700` | 23,640.06 USD | 3,375,967.01 USD | `STANDARD` | `+0.48%` | `0xb45f5c538d` |
| `SELL` | `8.53` | `2203.5100` | 18,792.19 USD | 3,454,758.99 USD | `STANDARD` | `+0.51%` | `0xa38f19c4cc` |
| `SELL` | `8.53` | `1652.6700` | 14,100.75 USD | 3,589,380.09 USD | `STANDARD` | `+0.56%` | `0x57d8e75f47` |
| `SELL` | `8.53` | `1652.6700` | 14,092.81 USD | 3,603,472.90 USD | `STANDARD` | `+0.50%` | `0x57d8e75f47` |
| `SELL` | `8.53` | `938.0800` | 7,999.95 USD | 4,160,592.51 USD | `STANDARD` | `+0.51%` | `0x0efb38a5fa` |
| `SELL` | `8.53` | `588.4000` | 5,018.93 USD | 4,231,038.35 USD | `STANDARD` | `+0.53%` | `0x3ca146d269` |
| `SELL` | `8.54` | `11723.6400` | 100,138.64 USD | 2,888,597.28 USD | `LARGE (>= USD 100K)` | `+0.67%` | `0x881cd92459` |
| `SELL` | `8.54` | `1420.7800` | 12,133.60 USD | 3,909,952.34 USD | `STANDARD` | `+0.65%` | `0xd3943e4008` |
| `SELL` | `8.54` | `1180.7700` | 10,077.87 USD | 4,061,526.74 USD | `STANDARD` | `+0.59%` | `0xd3943e4008` |
| `SELL` | `8.54` | `350.6500` | 2,994.48 USD | 4,363,961.39 USD | `STANDARD` | `+0.65%` | `0xd890331e75` |
| `SELL` | `8.55` | `31765.0600` | 271,683.38 USD | 803,221.50 USD | `LARGE (>= USD 100K)` | `+0.80%` | `0x71cfa5e263` |
| `SELL` | `8.55` | `1403.3600` | 11,999.99 USD | 3,934,012.41 USD | `STANDARD` | `+0.78%` | `0x0efb38a5fa` |
| `SELL` | `8.55` | `398.7500` | 3,409.91 USD | 4,338,210.27 USD | `STANDARD` | `+0.78%` | `0x14f8e04290` |
| `SELL` | `8.56` | `17364.9800` | 148,727.58 USD | 1,367,394.28 USD | `LARGE (>= USD 100K)` | `+0.94%` | `0x71d0e11ebb` |
| `SELL` | `8.56` | `4248.7900` | 36,374.32 USD | 3,225,194.36 USD | `MEDIUM (>= USD 25K)` | `+0.90%` | `0xa24c5ca26c` |
| `SELL` | `8.56` | `89.3300` | 764.96 USD | 4,457,111.70 USD | `STANDARD` | `+0.92%` | `0x010461c14e` |
| `SELL` | `8.56` | `87.4900` | 748.72 USD | 4,460,137.34 USD | `STANDARD` | `+0.86%` | `0x31ca8395cf` |
| `SELL` | `8.57` | `1724.1100` | 14,779.07 USD | 3,575,279.34 USD | `STANDARD` | `+1.03%` | `0xd3943e4008` |
| `SELL` | `8.57` | `398.6500` | 3,416.59 USD | 4,334,800.36 USD | `STANDARD` | `+1.01%` | `0x14f8e04290` |
| `SELL` | `8.57` | `315.7300` | 2,704.86 USD | 4,369,389.11 USD | `STANDARD` | `+0.97%` | `0x07fd993f0f` |
| `SELL` | `8.58` | `7555.7400` | 64,801.80 USD | 3,125,554.17 USD | `MEDIUM (>= USD 25K)` | `+1.08%` | `0x71d0e11ebb` |
| `SELL` | `8.58` | `2099.8000` | 18,007.88 USD | 3,528,500.37 USD | `STANDARD` | `+1.07%` | `0xd3943e4008` |
| `SELL` | `8.59` | `17382.4800` | 149,360.70 USD | 1,218,666.70 USD | `LARGE (>= USD 100K)` | `+1.27%` | `0x71d0e11ebb` |
| `SELL` | `8.59` | `1862.8200` | 15,999.95 USD | 3,560,500.27 USD | `STANDARD` | `+1.23%` | `0x0efb38a5fa` |
| `SELL` | `8.59` | `224.3200` | 1,926.95 USD | 4,424,966.68 USD | `STANDARD` | `+1.24%` | `0xdadbb4b2a0` |
| `SELL` | `8.60` | `398.6500` | 3,428.47 USD | 4,331,383.77 USD | `STANDARD` | `+1.36%` | `0x14f8e04290` |
| `SELL` | `8.60` | `233.2000` | 2,005.47 USD | 4,421,041.20 USD | `STANDARD` | `+1.35%` | `0x39bac00809` |
| `SELL` | `8.60` | `201.6300` | 1,734.93 USD | 4,432,109.89 USD | `STANDARD` | `+1.41%` | `0x010461c14e` |
| `SELL` | `8.61` | `2205.7800` | 18,999.93 USD | 3,416,966.87 USD | `STANDARD` | `+1.52%` | `0x0efb38a5fa` |
| `SELL` | `8.62` | `315.7300` | 2,722.86 USD | 4,366,684.25 USD | `STANDARD` | `+1.64%` | `0x07fd993f0f` |
| `SELL` | `8.62` | `186.7700` | 1,609.12 USD | 4,440,501.41 USD | `STANDARD` | `+1.54%` | `0x31ca8395cf` |
| `SELL` | `8.63` | `61585.4800` | 531,538.12 USD | 531,538.12 USD | `LARGE (>= USD 100K)` | `+1.72%` | `0x71cfa5e263` |
| `SELL` | `8.63` | `64.2000` | 554.37 USD | 4,503,666.73 USD | `STANDARD` | `+1.77%` | `0x18c0b7b9fe` |
| `SELL` | `8.65` | `2543.5800` | 21,999.93 USD | 3,397,966.94 USD | `STANDARD` | `+1.94%` | `0x0efb38a5fa` |
| `SELL` | `8.65` | `398.6500` | 3,448.08 USD | 4,327,955.30 USD | `STANDARD` | `+1.94%` | `0x14f8e04290` |
| `SELL` | `8.65` | `200.9400` | 1,738.09 USD | 4,430,374.97 USD | `STANDARD` | `+1.94%` | `0x31ca8395cf` |
| `SELL` | `8.65` | `79.0100` | 683.45 USD | 4,499,153.50 USD | `STANDARD` | `+1.95%` | `0xdadbb4b2a0` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:30:10 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1474` | `0x7737...bf66` | `SHORT` | 1,455,960.87 USD | `171,568.06` | `7.43` | `8.48` | `112.54` | -180,415.85 USD | `-12.39%` | `10X Cross` |
| `1578` | `0xeadc...9d55` | `LONG` | 1,358,390.79 USD | `160,070.56` | `8.11` | `8.48` | `0.000000` | 60,753.21 USD | `+4.47%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `8.78` | 14,595.44 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 14.60K USD at 8.7827 USD [API] | `2026-10-29 10:57:18` |
| `ANNOUNCEMENT` | `INFO` | `8.79` | 5,023.36 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 5.02K USD at 8.7907 USD [API] | `2026-10-29 11:52:34` |
| `ANNOUNCEMENT` | `INFO` | `8.81` | 5,295.54 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 5.30K USD at 8.8074 USD [API] | `2026-10-29 13:20:34` |
| `ANNOUNCEMENT` | `INFO` | `8.80` | 7,335.21 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 7.34K USD at 8.8043 USD [API] | `2026-10-29 13:27:49` |
| `ANNOUNCEMENT` | `INFO` | `8.81` | 5,999.91 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 6.00K USD at 8.8138 USD [API] | `2026-10-29 14:01:56` |
| `ANNOUNCEMENT` | `INFO` | `8.81` | 5,668.07 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 5.67K USD at 8.8149 USD [API] | `2026-10-29 14:01:46` |
| `ANNOUNCEMENT` | `INFO` | `8.82` | 9,104.31 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 9.10K USD at 8.8185 USD [API] | `2026-10-29 14:07:26` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+3.41%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.94%`)
  * 48H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+3.34%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.96%`)
  * 3D Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+3.34%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.96%`)
  * 7D Horizon: Short MP=`9.23` (Vol: 459,400.00 USD, Dist: `+8.89%`) | Long MP=`8.31` (Vol: 454,800.00 USD, Dist: `--1.92%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.77` | 215.89 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 127.05 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 220.22 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 2,520.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 217.74 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 160.40 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 1,430.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 247.83 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 252.43 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 808.52 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 263.93 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 110.07 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 942.44 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 328.32 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 381.65 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 11,810.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 21,010.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 102.71 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 1,200.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 24,670.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 392.22 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 583.78 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.98` | 7,970.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.08` | 1,630.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 159.29 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.21` | 393.34 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 196.42 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 110.77 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 3,420.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,380.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,040.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 474.50 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.87` | 2,430.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 16,080.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 3,880.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.93` | 314.61 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 565.66 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 4,090.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 269.53 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 550.55 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 482.71 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 213.20 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 105.46 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.09` | 1,270.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.11` | 118.44 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 1,040.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 5,790.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.24` | 502.82 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 213.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 1,050.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.26` | 2,230.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 161,490.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.41` | 260.63 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 20,560.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 299.48 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 1,490.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 2,880.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.61` | 34,490.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.62` | 139.36 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 468.55 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.72` | 2,390.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 661.65 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 635.31 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 580.50 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.83` | 1,360.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.84` | 146.13 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.86` | 2,110.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 984.70 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 6,320.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 437.84 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,530.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 1,140.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.13` | 2,030.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 7,810.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 972.65 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.29` | 2,430.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 277.48 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 1,430.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 1,310.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 5,120.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.39` | 5,940.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 484.64 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 363,480.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.50` | 1,520.00 USD | 796,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 852.03 USD | 794,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 793,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.59` | 2,870.00 USD | 784,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 782,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 1,880.00 USD | 779,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.63` | 1,780.00 USD | 778,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.67` | 1,320.00 USD | 776,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.68` | 3,160.00 USD | 774,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 11,000.00 USD | 771,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 6,180.00 USD | 760,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 754,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 7,990.00 USD | 753,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 22,020.00 USD | 745,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 5,170.00 USD | 723,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 718,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 7,230.00 USD | 716,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 271.02 USD | 709,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 709,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 263.66 USD | 705,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 1,580.00 USD | 705,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 579.62 USD | 703,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.93` | 3,500.00 USD | 703,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 215.30 USD | 699,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 7,240.00 USD | 699,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 692,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.97` | 128,810.00 USD | 691,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 1,040.00 USD | 562,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.01` | 20,890.00 USD | 561,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.03` | 1,370.00 USD | 540,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.07` | 23,960.00 USD | 539,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 515,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,050.00 USD | 508,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.09` | 2,130.00 USD | 507,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,530.00 USD | 505,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 477,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 777.50 USD | 476,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.14` | 6,480,000.00 USD | 6,480,000.00 USD | 45,760.00 USD | 20,580.00 USD | 41,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,270.00 USD | 476,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.16` | 6,370,000.00 USD | 6,370,000.00 USD | 29,500.00 USD | 4,260.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.17` | 2,380.00 USD | 455,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.18` | 6,310,000.00 USD | 6,310,000.00 USD | 5,030.00 USD | 3,780.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 453,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.20` | 2,520.00 USD | 451,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.20` | 6,290,000.00 USD | 6,290,000.00 USD | 11,960.00 USD | 7,300.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.21` | 322.94 USD | 449,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.22` | 6,260,000.00 USD | 6,260,000.00 USD | 12,260.00 USD | 6,540.00 USD | 6,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.24` | 1,480.00 USD | 449,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.24` | 6,240,000.00 USD | 6,240,000.00 USD | 39,910.00 USD | 0.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.25` | 29,170.00 USD | 447,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 24,850.00 USD | 418,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.26` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 1,810.00 USD | 58.08 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,420.00 USD | 393,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 1,680.00 USD | 357,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.30` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 4,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.32` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 5,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.34` | 552.42 USD | 355,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.36` | 3,820.00 USD | 354,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.36` | 6,180,000.00 USD | 6,180,000.00 USD | 983.83 USD | 0.00 USD | 864.67 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.37` | 3,970.00 USD | 351,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 1,100.00 USD | 347,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.38` | 6,170,000.00 USD | 6,170,000.00 USD | 46,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.38` | 13,430.00 USD | 346,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.40` | 6,130,000.00 USD | 6,130,000.00 USD | 44,790.00 USD | 0.00 USD | 503.12 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 147.61 USD | 332,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 3,290.00 USD | 332,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 2,410.00 USD | 329,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 10,390.00 USD | 326,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.46` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 316,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 1,120.00 USD | 311,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.48` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 962.81 USD | 310,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 421.78 USD | 309,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.51` | 1,710.00 USD | 309,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.52` | 6,040,000.00 USD | 6,040,000.00 USD | 3,220.00 USD | 14,470.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.53` | 1,570.00 USD | 307,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 306,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.54` | 6,000,000.00 USD | 6,000,000.00 USD | 34,840.00 USD | 4,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.55` | 2,580.00 USD | 301,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.56` | 5,960,000.00 USD | 5,960,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.57` | 25,060.00 USD | 299,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 118.25 USD | 274,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.59` | 1,630.00 USD | 274,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.60` | 5,180,000.00 USD | 5,180,000.00 USD | 2,760.00 USD | 4,900.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.60` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 301.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.61` | 5,160,000.00 USD | 5,160,000.00 USD | 3,160.00 USD | 1,250.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 754.04 USD | 272,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 5,150,000.00 USD | 5,150,000.00 USD | 5,860.00 USD | 1,330.00 USD | 133.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.62` | 5,940,000.00 USD | 5,940,000.00 USD | 626.55 USD | 2,130.00 USD | 996.08 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 271,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.63` | 5,140,000.00 USD | 5,140,000.00 USD | 6,700.00 USD | 0.00 USD | 9,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 270,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 5,120,000.00 USD | 5,120,000.00 USD | 29,090.00 USD | 812.96 USD | 2,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.64` | 5,930,000.00 USD | 5,930,000.00 USD | 41,300.00 USD | 0.00 USD | 686.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.65` | 5,090,000.00 USD | 5,090,000.00 USD | 3,840.00 USD | 817.75 USD | 9,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 270,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.66` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 531.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.66` | 5,890,000.00 USD | 5,890,000.00 USD | 4,870.00 USD | 2,350.00 USD | 24,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 256.09 USD | 270,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.67` | 5,080,000.00 USD | 5,080,000.00 USD | 687.87 USD | 587.20 USD | 114.38 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 4,480.00 USD | 270,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.68` | 5,080,000.00 USD | 5,080,000.00 USD | 2,670.00 USD | 0.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.68` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.68` | 739.30 USD | 265,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.69` | 5,070,000.00 USD | 5,070,000.00 USD | 485.15 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.70` | 6,690.00 USD | 264,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 5,070,000.00 USD | 5,070,000.00 USD | 4,840.00 USD | 2,390.00 USD | 16,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.70` | 5,850,000.00 USD | 5,850,000.00 USD | 393.33 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.71` | 5,040,000.00 USD | 5,040,000.00 USD | 1,050.00 USD | 5,040.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.72` | 5,030,000.00 USD | 5,030,000.00 USD | 1,310.00 USD | 568.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.72` | 5,850,000.00 USD | 5,850,000.00 USD | 38,970.00 USD | 0.00 USD | 40,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.73` | 5,030,000.00 USD | 5,030,000.00 USD | 472.98 USD | 1,240.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.74` | 5,020,000.00 USD | 5,020,000.00 USD | 16,520.00 USD | 0.00 USD | 184.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.74` | 5,770,000.00 USD | 5,770,000.00 USD | 30,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.75` | 5,000,000.00 USD | 5,000,000.00 USD | 252.25 USD | 6,210.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 500.12 USD | 258,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.76` | 4,990,000.00 USD | 4,990,000.00 USD | 329.46 USD | 494.12 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.76` | 5,740,000.00 USD | 5,740,000.00 USD | 812.95 USD | 13,360.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 257,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.77` | 4,990,000.00 USD | 4,990,000.00 USD | 13,620.00 USD | 689.91 USD | 3,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.78` | 6,310.00 USD | 257,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 4,970,000.00 USD | 4,970,000.00 USD | 430.17 USD | 6,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.78` | 5,720,000.00 USD | 5,720,000.00 USD | 46,570.00 USD | 7,520.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,750.00 USD | 250,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.79` | 4,960,000.00 USD | 4,960,000.00 USD | 24,880.00 USD | 2,920.00 USD | 7,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 4,480.00 USD | 247,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 4,930,000.00 USD | 4,930,000.00 USD | 2,950.00 USD | 7,910.00 USD | 709.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.80` | 5,630,000.00 USD | 5,630,000.00 USD | 46,450.00 USD | 12,980.00 USD | 1,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 6,380.00 USD | 242,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.81` | 4,910,000.00 USD | 4,910,000.00 USD | 882.10 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.82` | 4,910,000.00 USD | 4,910,000.00 USD | 2,170.00 USD | 1,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.82` | 5,570,000.00 USD | 5,570,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.83` | 1,940.00 USD | 236,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.83` | 4,910,000.00 USD | 4,910,000.00 USD | 25,990.00 USD | 6,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.84` | 4,880,000.00 USD | 4,880,000.00 USD | 328.00 USD | 1,800.00 USD | 10.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 5,560,000.00 USD | 5,560,000.00 USD | 32,340.00 USD | 2,380.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 22,560.00 USD | 234,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.85` | 4,880,000.00 USD | 4,880,000.00 USD | 5,110.00 USD | 1,250.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.86` | 4,870,000.00 USD | 4,870,000.00 USD | 345.80 USD | 6,690.00 USD | 17,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.86` | 5,500,000.00 USD | 5,500,000.00 USD | 137,360.00 USD | 5,460.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 233.83 USD | 211,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.87` | 4,840,000.00 USD | 4,840,000.00 USD | 12,370.00 USD | 10,860.00 USD | 22,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 211,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 4,800,000.00 USD | 4,800,000.00 USD | 159,870.00 USD | 5,030.00 USD | 33,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.88` | 5,340,000.00 USD | 5,340,000.00 USD | 170,100.00 USD | 12,780.00 USD | 30,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.89` | 4,600,000.00 USD | 4,600,000.00 USD | 59,440.00 USD | 3,720.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.89` | 15,880.00 USD | 211,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.90` | 4,510,000.00 USD | 4,510,000.00 USD | 56,650.00 USD | 6,970.00 USD | 5,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 5,130,000.00 USD | 5,130,000.00 USD | 34,620.00 USD | 12,890.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 2,930.00 USD | 195,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 4,440,000.00 USD | 4,440,000.00 USD | 10,790.00 USD | 10,370.00 USD | 28,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.92` | 4,390,000.00 USD | 4,390,000.00 USD | 12,800.00 USD | 2,950.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.92` | 5,060,000.00 USD | 5,060,000.00 USD | 55,490.00 USD | 23,630.00 USD | 41,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 4,600.00 USD | 192,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 4,360,000.00 USD | 4,360,000.00 USD | 11,170.00 USD | 6,570.00 USD | 4,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 16,340.00 USD | 187,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 4,340,000.00 USD | 4,340,000.00 USD | 20,380.00 USD | 20,510.00 USD | 61,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.94` | 4,940,000.00 USD | 4,940,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 141.74 USD | 171,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 4,240,000.00 USD | 4,240,000.00 USD | 28,070.00 USD | 9,190.00 USD | 86,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 127,900.00 USD | 171,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 4,110,000.00 USD | 4,110,000.00 USD | 3,830.00 USD | 15,680.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.96` | 4,850,000.00 USD | 4,850,000.00 USD | 21,840.00 USD | 6,920.00 USD | 87,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.97` | 4,030,000.00 USD | 4,030,000.00 USD | 10,880.00 USD | 9,820.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.97` | 1,580.00 USD | 43,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.98` | 4,010,000.00 USD | 4,010,000.00 USD | 4,290.00 USD | 2,060.00 USD | 42,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.98` | 4,730,000.00 USD | 4,730,000.00 USD | 59,410.00 USD | 26,790.00 USD | 146,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,280.00 USD | 41,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 3,960,000.00 USD | 3,960,000.00 USD | 3,640.00 USD | 10,180.00 USD | 4,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 530.79 USD | 40,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 3,940,000.00 USD | 3,940,000.00 USD | 50,890.00 USD | 8,950.00 USD | 21,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.00` | 4,500,000.00 USD | 4,500,000.00 USD | 60,980.00 USD | 16,420.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 3,860,000.00 USD | 3,860,000.00 USD | 6,080.00 USD | 3,750.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 3,840,000.00 USD | 3,840,000.00 USD | 75,000.00 USD | 0.00 USD | 274.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.02` | 4,410,000.00 USD | 4,410,000.00 USD | 15,300.00 USD | 46,670.00 USD | 58,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 14,210.00 USD | 39,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 3,770,000.00 USD | 3,770,000.00 USD | 11,150.00 USD | 12,540.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.04` | 3,730,000.00 USD | 3,730,000.00 USD | 49,150.00 USD | 0.00 USD | 10,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.04` | 4,290,000.00 USD | 4,290,000.00 USD | 462,240.00 USD | 0.00 USD | 86,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 823.33 USD | 25,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.05` | 3,670,000.00 USD | 3,670,000.00 USD | 318,310.00 USD | 6,430.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.05` | 265.81 USD | 265.81 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.06` | 3,290,000.00 USD | 3,290,000.00 USD | 155,740.00 USD | 0.00 USD | 66,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.06` | 3,750,000.00 USD | 3,750,000.00 USD | 336,530.00 USD | 0.00 USD | 86,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 439.54 USD | 24,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 3,070,000.00 USD | 3,070,000.00 USD | 129,880.00 USD | 9,310.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.07` | 21,710.00 USD | 24,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.08` | 2,930,000.00 USD | 2,930,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.08` | 3,320,000.00 USD | 3,320,000.00 USD | 5,100.00 USD | 0.00 USD | 73,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.09` | 2,850,000.00 USD | 2,850,000.00 USD | 3,110.00 USD | 0.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.10` | 2,820,000.00 USD | 2,820,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.10` | 3,240,000.00 USD | 3,240,000.00 USD | 56,590.00 USD | 0.00 USD | 14,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.11` | 2,660,000.00 USD | 2,660,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 738.14 USD | 2,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 2,380,000.00 USD | 2,380,000.00 USD | 20,210.00 USD | 11,230.00 USD | 126,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.12` | 3,170,000.00 USD | 3,170,000.00 USD | 23,240.00 USD | 0.00 USD | 141,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 521.62 USD | 1,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.13` | 2,230,000.00 USD | 2,230,000.00 USD | 29,110.00 USD | 9,180.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 2,190,000.00 USD | 2,190,000.00 USD | 17,740.00 USD | 8,630.00 USD | 105,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.14` | 3,010,000.00 USD | 3,010,000.00 USD | 180,540.00 USD | 30,700.00 USD | 183,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 2,050,000.00 USD | 2,050,000.00 USD | 43,730.00 USD | 12,240.00 USD | 53,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.15` | 1,420.00 USD | 1,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.16` | 1,940,000.00 USD | 1,940,000.00 USD | 364.84 USD | 21,000.00 USD | 165,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 2,610,000.00 USD | 2,610,000.00 USD | 30,670.00 USD | 23,640.00 USD | 14,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.17` | 1,760,000.00 USD | 1,760,000.00 USD | 11,690.00 USD | 8,610.00 USD | 183,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 1,550,000.00 USD | 1,550,000.00 USD | 7,250.00 USD | 1,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 2,540,000.00 USD | 2,540,000.00 USD | 1,200.00 USD | 40,090.00 USD | 172,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.19` | 1,550,000.00 USD | 1,550,000.00 USD | 19,780.00 USD | 0.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.20` | 1,510,000.00 USD | 1,510,000.00 USD | 25,530.00 USD | 4,000.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.20` | 2,330,000.00 USD | 2,330,000.00 USD | 174,220.00 USD | 58,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.21` | 1,470,000.00 USD | 1,470,000.00 USD | 41,990.00 USD | 1,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.22` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.22` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.23` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 1,750.00 USD | 2,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.24` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 3,220.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 2,070,000.00 USD | 2,070,000.00 USD | 106,990.00 USD | 18,690.00 USD | 17,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.25` | 1,400,000.00 USD | 1,400,000.00 USD | 168.44 USD | 5,000.00 USD | 38,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.26` | 1,350,000.00 USD | 1,350,000.00 USD | 50,590.00 USD | 12,510.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.26` | 1,930,000.00 USD | 1,930,000.00 USD | 100,930.00 USD | 5,750.00 USD | 11,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.27` | 1,270,000.00 USD | 1,270,000.00 USD | 14,470.00 USD | 12,270.00 USD | 20,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.28` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 13,760.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.28` | 1,810,000.00 USD | 1,810,000.00 USD | 91,120.00 USD | 4,000.00 USD | 27,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.29` | 1,200,000.00 USD | 1,200,000.00 USD | 39,670.00 USD | 11,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.30` | 1,150,000.00 USD | 1,150,000.00 USD | 58,950.00 USD | 13,810.00 USD | 20,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.30` | 1,690,000.00 USD | 1,690,000.00 USD | 264,780.00 USD | 17,210.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.31` | 1,060,000.00 USD | 1,060,000.00 USD | 83,770.00 USD | 11,920.00 USD | 56,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.32` | 905,060.00 USD | 905,060.00 USD | 73,050.00 USD | 6,080.00 USD | 14,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.32` | 1,390,000.00 USD | 1,390,000.00 USD | 220,640.00 USD | 0.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 811,860.00 USD | 811,860.00 USD | 0.00 USD | 6,210.00 USD | 109.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.34` | 805,550.00 USD | 805,550.00 USD | 0.00 USD | 2,210.00 USD | 13.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.34` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 11,770.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 803,320.00 USD | 803,320.00 USD | 0.00 USD | 19,810.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.36` | 766,540.00 USD | 766,540.00 USD | 0.00 USD | 0.00 USD | 17,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.36` | 1,150,000.00 USD | 1,150,000.00 USD | 223,170.00 USD | 0.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.37` | 748,740.00 USD | 748,740.00 USD | 0.00 USD | 14,420.00 USD | 16.86 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.38` | 734,300.00 USD | 734,300.00 USD | 17,220.00 USD | 5,940.00 USD | 50,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.38` | 904,500.00 USD | 904,500.00 USD | 0.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.39` | 660,860.00 USD | 660,860.00 USD | 100,740.00 USD | 13,620.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.40` | 513,890.00 USD | 513,890.00 USD | 10,500.00 USD | 7,000.00 USD | 56,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.40` | 846,760.00 USD | 846,760.00 USD | 0.00 USD | 7,600.00 USD | 86,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.41` | 439,800.00 USD | 439,800.00 USD | 916.10 USD | 6,440.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.42` | 420,500.00 USD | 420,500.00 USD | 0.00 USD | 16,260.00 USD | 42,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.42` | 752,220.00 USD | 752,220.00 USD | 209,760.00 USD | 0.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.43` | 361,350.00 USD | 361,350.00 USD | 81,350.00 USD | 7,730.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.44` | 264,730.00 USD | 264,730.00 USD | 10,010.00 USD | 32,380.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.44` | 507,240.00 USD | 507,240.00 USD | 152,190.00 USD | 8,000.00 USD | 74,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.45` | 61,880.00 USD | 61,880.00 USD | 55,910.00 USD | 5,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.46` | 272,390.00 USD | 272,390.00 USD | 152,650.00 USD | 0.00 USD | 119,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.47` | 769.90 USD | 769.90 USD | 769.90 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.48` | 3,000.00 USD | 3,000.00 USD | 2,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.48` | 191,210.00 USD | 191,210.00 USD | 0.00 USD | 0.00 USD | 191,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.49` | 3,300.00 USD | 3,300.00 USD | 282.10 USD | 0.00 USD | 12.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.50` | 3,570.00 USD | 3,570.00 USD | 272.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.50` | 192,390.00 USD | 192,390.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.51` | 176,010.00 USD | 176,010.00 USD | 0.00 USD | 0.00 USD | 172,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.52` | 339,850.00 USD | 339,850.00 USD | 159,040.00 USD | 0.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.52` | 398,210.00 USD | 398,210.00 USD | 113,820.00 USD | 0.00 USD | 92,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.53` | 364,030.00 USD | 364,030.00 USD | 24,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.54` | 567,560.00 USD | 567,560.00 USD | 203,370.00 USD | 0.00 USD | 156.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.54` | 757,830.00 USD | 757,830.00 USD | 357,740.00 USD | 0.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.55` | 593,370.00 USD | 593,370.00 USD | 686.73 USD | 0.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.56` | 632,240.00 USD | 632,240.00 USD | 555.70 USD | 38,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.56` | 1,030,000.00 USD | 1,030,000.00 USD | 144,180.00 USD | 122,650.00 USD | 790.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.57` | 782,090.00 USD | 782,090.00 USD | 149,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.58` | 840,360.00 USD | 840,360.00 USD | 58,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.58` | 1,190,000.00 USD | 1,190,000.00 USD | 4,370.00 USD | 164,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.59` | 843,470.00 USD | 843,470.00 USD | 3,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.60` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.61` | 847,790.00 USD | 847,790.00 USD | 3,630.00 USD | 0.00 USD | 699.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.62` | 1,010,000.00 USD | 1,010,000.00 USD | 38,440.00 USD | 0.00 USD | 125,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.62` | 1,230,000.00 USD | 1,230,000.00 USD | 2,810.00 USD | 0.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.63` | 1,140,000.00 USD | 1,140,000.00 USD | 129,560.00 USD | 2,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 1,220,000.00 USD | 1,220,000.00 USD | 59,700.00 USD | 9,340.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.64` | 1,280,000.00 USD | 1,280,000.00 USD | 40,260.00 USD | 10,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.65` | 1,280,000.00 USD | 1,280,000.00 USD | 36,130.00 USD | 9,010.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.66` | 1,300,000.00 USD | 1,300,000.00 USD | 6,230.00 USD | 2,020.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.66` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 416.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.67` | 1,310,000.00 USD | 1,310,000.00 USD | 2,210.00 USD | 9,960.00 USD | 56.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 12,020.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.68` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 30,000.00 USD | 117,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.69` | 209.31 USD | 475.12 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.69` | 1,410,000.00 USD | 1,410,000.00 USD | 9,290.00 USD | 19,200.00 USD | 33,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.70` | 1,500,000.00 USD | 1,500,000.00 USD | 60,200.00 USD | 0.00 USD | 23,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.70` | 1,630,000.00 USD | 1,630,000.00 USD | 116,370.00 USD | 41,840.00 USD | 46,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.71` | 1,520,000.00 USD | 1,520,000.00 USD | 18,250.00 USD | 7,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 1,610,000.00 USD | 1,610,000.00 USD | 34,050.00 USD | 2,520.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.72` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 609.73 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.73` | 1,690,000.00 USD | 1,690,000.00 USD | 14,030.00 USD | 28,810.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 1,740,000.00 USD | 1,740,000.00 USD | 37,210.00 USD | 3,500.00 USD | 17,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.74` | 1,710,000.00 USD | 1,710,000.00 USD | 51,030.00 USD | 30,470.00 USD | 686.63 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.75` | 1,800,000.00 USD | 1,800,000.00 USD | 34,030.00 USD | 8,970.00 USD | 16,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.76` | 1,950,000.00 USD | 1,950,000.00 USD | 78,530.00 USD | 10,010.00 USD | 57,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.76` | 1,970,000.00 USD | 1,970,000.00 USD | 196,960.00 USD | 0.00 USD | 58,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.77` | 2,150,000.00 USD | 2,150,000.00 USD | 159,000.00 USD | 2,060.00 USD | 43,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.78` | 2,270,000.00 USD | 2,270,000.00 USD | 45,370.00 USD | 25,510.00 USD | 50,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.78` | 2,250,000.00 USD | 2,250,000.00 USD | 144,010.00 USD | 8,000.00 USD | 133,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.79` | 2,360,000.00 USD | 2,360,000.00 USD | 32,530.00 USD | 17,970.00 USD | 31,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.80` | 2,510,000.00 USD | 2,510,000.00 USD | 114,070.00 USD | 19,150.00 USD | 23,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.80` | 2,350,000.00 USD | 2,350,000.00 USD | 27,360.00 USD | 33,750.00 USD | 32,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.81` | 2,570,000.00 USD | 2,570,000.00 USD | 46,510.00 USD | 9,030.00 USD | 1,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.82` | 2,650,000.00 USD | 2,650,000.00 USD | 18,070.00 USD | 4,510.00 USD | 61,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.82` | 2,770,000.00 USD | 2,770,000.00 USD | 365,470.00 USD | 18,440.00 USD | 39,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.82` | 6,000.00 USD | 6,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.83` | 2,850,000.00 USD | 2,850,000.00 USD | 172,310.00 USD | 19,400.00 USD | 7,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 2,920,000.00 USD | 2,920,000.00 USD | 461.30 USD | 3,110.00 USD | 59,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.84` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 5,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 2,940,000.00 USD | 2,940,000.00 USD | 11,710.00 USD | 3,360.00 USD | 11,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 2,950,000.00 USD | 2,950,000.00 USD | 4,400.00 USD | 1,470.00 USD | 607.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.86` | 2,890,000.00 USD | 2,890,000.00 USD | 29,310.00 USD | 0.00 USD | 83,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.87` | 1,160.00 USD | 7,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.87` | 2,960,000.00 USD | 2,960,000.00 USD | 1,760.00 USD | 0.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 2,970,000.00 USD | 2,970,000.00 USD | 450.96 USD | 14,670.00 USD | 186.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.88` | 2,920,000.00 USD | 2,920,000.00 USD | 1,250.00 USD | 0.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.88` | 691.70 USD | 8,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.89` | 3,020,000.00 USD | 3,020,000.00 USD | 11,710.00 USD | 3,410.00 USD | 32,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.89` | 808.47 USD | 9,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.90` | 3,140,000.00 USD | 3,140,000.00 USD | 26,130.00 USD | 5,990.00 USD | 81,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.90` | 3,040,000.00 USD | 3,040,000.00 USD | 2,440.00 USD | 0.00 USD | 116,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.90` | 8,910.00 USD | 18,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.91` | 3,200,000.00 USD | 3,200,000.00 USD | 32,000.00 USD | 11,620.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 3,210,000.00 USD | 3,210,000.00 USD | 2,950.00 USD | 3,220.00 USD | 6,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.92` | 3,170,000.00 USD | 3,170,000.00 USD | 99,150.00 USD | 0.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 3,290,000.00 USD | 3,290,000.00 USD | 32,090.00 USD | 6,810.00 USD | 38,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 3,350,000.00 USD | 3,350,000.00 USD | 51,500.00 USD | 12,260.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.94` | 3,310,000.00 USD | 3,310,000.00 USD | 129,180.00 USD | 0.00 USD | 11,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.95` | 3,380,000.00 USD | 3,380,000.00 USD | 439.30 USD | 6,630.00 USD | 20,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.96` | 3,380,000.00 USD | 3,380,000.00 USD | 532.00 USD | 2,980.00 USD | 175.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.96` | 3,350,000.00 USD | 3,350,000.00 USD | 3,320.00 USD | 4,000.00 USD | 26,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.97` | 3,390,000.00 USD | 3,390,000.00 USD | 978.04 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.97` | 10,480.00 USD | 28,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.98` | 3,450,000.00 USD | 3,450,000.00 USD | 37,560.00 USD | 9,420.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.98` | 3,360,000.00 USD | 3,360,000.00 USD | 1,180.00 USD | 0.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 3,530,000.00 USD | 3,530,000.00 USD | 48,460.00 USD | 22,110.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.99` | 539,710.00 USD | 568,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.00` | 3,590,000.00 USD | 3,590,000.00 USD | 37,680.00 USD | 0.00 USD | 24,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.00` | 3,790,000.00 USD | 3,790,000.00 USD | 370,780.00 USD | 17,920.00 USD | 41,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 3,670,000.00 USD | 3,670,000.00 USD | 50,570.00 USD | 14,940.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 3,750,000.00 USD | 3,750,000.00 USD | 40,370.00 USD | 29,440.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.02` | 3,930,000.00 USD | 3,930,000.00 USD | 82,280.00 USD | 56,120.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 3,910,000.00 USD | 3,910,000.00 USD | 124,130.00 USD | 10,300.00 USD | 34,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 3,980,000.00 USD | 3,980,000.00 USD | 41,880.00 USD | 5,900.00 USD | 14,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.04` | 4,160,000.00 USD | 4,160,000.00 USD | 137,460.00 USD | 74,750.00 USD | 16,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 4,030,000.00 USD | 4,030,000.00 USD | 21,080.00 USD | 9,980.00 USD | 24,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.05` | 213.70 USD | 568,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.06` | 4,080,000.00 USD | 4,080,000.00 USD | 26,230.00 USD | 6,890.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.06` | 4,230,000.00 USD | 4,230,000.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.06` | 6,040.00 USD | 574,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.07` | 4,130,000.00 USD | 4,130,000.00 USD | 14,180.00 USD | 17,440.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 4,180,000.00 USD | 4,180,000.00 USD | 12,960.00 USD | 2,110.00 USD | 32,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.08` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 4,290,000.00 USD | 4,290,000.00 USD | 73,020.00 USD | 9,730.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.10` | 3,890.00 USD | 578,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.10` | 4,350,000.00 USD | 4,350,000.00 USD | 16,130.00 USD | 12,520.00 USD | 34,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.10` | 5,510,000.00 USD | 5,510,000.00 USD | 826,500.00 USD | 35,760.00 USD | 334,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 4,510,000.00 USD | 4,510,000.00 USD | 60,270.00 USD | 14,420.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 4,660,000.00 USD | 4,660,000.00 USD | 102,270.00 USD | 22,410.00 USD | 26,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.12` | 6,500,000.00 USD | 6,500,000.00 USD | 466,670.00 USD | 24,170.00 USD | 503,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 4,790,000.00 USD | 4,790,000.00 USD | 75,050.00 USD | 15,960.00 USD | 40,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.14` | 4,850,000.00 USD | 4,850,000.00 USD | 29,800.00 USD | 3,380.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.14` | 7,560,000.00 USD | 7,560,000.00 USD | 536,560.00 USD | 18,540.00 USD | 500,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.14` | 180.80 USD | 578,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.15` | 4,960,000.00 USD | 4,960,000.00 USD | 57,220.00 USD | 23,170.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 5,080,000.00 USD | 5,080,000.00 USD | 64,660.00 USD | 23,900.00 USD | 32,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.16` | 8,150,000.00 USD | 8,150,000.00 USD | 358,370.00 USD | 44,360.00 USD | 196,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 5,210,000.00 USD | 5,210,000.00 USD | 79,780.00 USD | 3,200.00 USD | 49,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 5,300,000.00 USD | 5,300,000.00 USD | 28,670.00 USD | 26,430.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.18` | 9,180,000.00 USD | 9,180,000.00 USD | 566,340.00 USD | 162,460.00 USD | 292,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 5,410,000.00 USD | 5,410,000.00 USD | 77,860.00 USD | 29,140.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.20` | 5,530,000.00 USD | 5,530,000.00 USD | 66,540.00 USD | 11,090.00 USD | 37,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 10,100,000.00 USD | 10,100,000.00 USD | 550,150.00 USD | 134,550.00 USD | 238,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 5,560,000.00 USD | 5,560,000.00 USD | 29,910.00 USD | 2,950.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.22` | 5,640,000.00 USD | 5,640,000.00 USD | 58,820.00 USD | 2,850.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.22` | 11,240,000.00 USD | 11,240,000.00 USD | 620,010.00 USD | 144,840.00 USD | 376,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 5,640,000.00 USD | 5,640,000.00 USD | 427.70 USD | 4,270.00 USD | 17.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 5,690,000.00 USD | 5,690,000.00 USD | 45,120.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 11,760,000.00 USD | 11,760,000.00 USD | 336,360.00 USD | 44,660.00 USD | 136,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 5,720,000.00 USD | 5,720,000.00 USD | 17,750.00 USD | 5,840.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 5,730,000.00 USD | 5,730,000.00 USD | 539.67 USD | 0.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 12,150,000.00 USD | 12,150,000.00 USD | 273,920.00 USD | 96,980.00 USD | 19,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 5,760,000.00 USD | 5,760,000.00 USD | 22,500.00 USD | 1,360.00 USD | 6,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 5,770,000.00 USD | 5,770,000.00 USD | 2,210.00 USD | 8,760.00 USD | 169.17 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 12,710,000.00 USD | 12,710,000.00 USD | 352,980.00 USD | 69,460.00 USD | 136,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.29` | 5,810,000.00 USD | 5,810,000.00 USD | 16,190.00 USD | 4,140.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 3,860.00 USD | 582,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.30` | 5,870,000.00 USD | 5,870,000.00 USD | 40,750.00 USD | 7,520.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.30` | 13,240,000.00 USD | 13,240,000.00 USD | 199,810.00 USD | 97,780.00 USD | 233,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 5,910,000.00 USD | 5,910,000.00 USD | 28,720.00 USD | 5,500.00 USD | 12,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 5,940,000.00 USD | 5,940,000.00 USD | 15,740.00 USD | 1,330.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.32` | 13,840,000.00 USD | 13,840,000.00 USD | 242,590.00 USD | 51,970.00 USD | 309,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 5,960,000.00 USD | 5,960,000.00 USD | 11,780.00 USD | 6,000.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 6,020,000.00 USD | 6,020,000.00 USD | 44,670.00 USD | 3,660.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.34` | 14,040,000.00 USD | 14,040,000.00 USD | 98,640.00 USD | 41,250.00 USD | 59,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.35` | 6,050,000.00 USD | 6,050,000.00 USD | 14,420.00 USD | 817.75 USD | 14,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 6,070,000.00 USD | 6,070,000.00 USD | 5,440.00 USD | 6,760.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.36` | 14,420,000.00 USD | 14,420,000.00 USD | 215,620.00 USD | 64,120.00 USD | 97,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 6,090,000.00 USD | 6,090,000.00 USD | 10,930.00 USD | 6,260.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 6,120,000.00 USD | 6,120,000.00 USD | 14,740.00 USD | 0.00 USD | 13,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.38` | 14,750,000.00 USD | 14,750,000.00 USD | 224,850.00 USD | 31,100.00 USD | 77,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.40` | 15,130,000.00 USD | 15,130,000.00 USD | 234,760.00 USD | 42,520.00 USD | 105,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 440.06 USD | 582,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.42` | 15,310,000.00 USD | 15,310,000.00 USD | 109,230.00 USD | 13,910.00 USD | 51,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 15,450,000.00 USD | 15,450,000.00 USD | 80,230.00 USD | 19,420.00 USD | 43,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 15,510,000.00 USD | 15,510,000.00 USD | 51,570.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.48` | 15,550,000.00 USD | 15,550,000.00 USD | 10,620.00 USD | 11,060.00 USD | 20,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 15,680,000.00 USD | 15,680,000.00 USD | 65,230.00 USD | 12,050.00 USD | 52,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 15,790,000.00 USD | 15,790,000.00 USD | 57,650.00 USD | 18,520.00 USD | 31,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 15,810,000.00 USD | 15,810,000.00 USD | 11,650.00 USD | 13,310.00 USD | 930.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 15,830,000.00 USD | 15,830,000.00 USD | 7,430.00 USD | 5,260.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 15,890,000.00 USD | 15,890,000.00 USD | 35,340.00 USD | 2,380.00 USD | 26,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 15,950,000.00 USD | 15,950,000.00 USD | 31,720.00 USD | 5,460.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 15,990,000.00 USD | 15,990,000.00 USD | 26,870.00 USD | 1,540.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.62` | 138.98 USD | 582,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.64` | 1,930.00 USD | 584,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.69` | 285.51 USD | 585,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 585,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.88` | 371.77 USD | 585,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 2,650.00 USD | 588,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.47` | 20,950.00 USD | 609,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 609,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.78` | 173.91 USD | 610,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.81` | 1,150.00 USD | 611,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.98` | 54,920.00 USD | 666,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 673,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.19` | 4,210.00 USD | 677,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 124,320.00 USD | 801,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.46` | 322.74 USD | 801,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.48` | 275.18 USD | 802,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 814,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.69` | 296,760.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.93` | 505.74 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,050.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.96` | 1,530.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.49` | 61,470.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.54` | 111.48 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.78` | 242.46 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.06` | 324.65 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.09` | 219.34 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.12` | 542.84 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.23` | 4,230.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.77` | 185.55 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.82` | 1,700.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.38` | 265,410.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.50` | 23,330.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.62` | 118.20 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.64` | 24,270.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.91` | 1,960.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.93` | 85,310.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.77` | 2,300,000.00 USD | 0.00 USD | 215.89 USD | `-79.04%` | `121.63` |
| `Live` | `Long` | `1.81` | 2,300,000.00 USD | 0.00 USD | 127.05 USD | `-78.57%` | `70.00` |
| `Live` | `Long` | `1.92` | 2,300,000.00 USD | 0.00 USD | 220.22 USD | `-77.39%` | `115.00` |
| `Live` | `Long` | `1.96` | 2,300,000.00 USD | 0.00 USD | 2,520.00 USD | `-76.91%` | `1,288.03` |
| `Live` | `Long` | `1.97` | 2,300,000.00 USD | 0.00 USD | 217.74 USD | `-76.79%` | `110.81` |
| `Live` | `Long` | `2.00` | 2,300,000.00 USD | 0.00 USD | 160.40 USD | `-76.32%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,300,000.00 USD | 0.00 USD | 1,430.00 USD | `-75.97%` | `701.61` |
| `Live` | `Long` | `2.06` | 2,290,000.00 USD | 0.00 USD | 4,920.00 USD | `-75.61%` | `2,382.76` |
| `Live` | `Long` | `2.15` | 2,290,000.00 USD | 0.00 USD | 247.83 USD | `-74.55%` | `115.00` |
| `Live` | `Long` | `2.19` | 2,290,000.00 USD | 0.00 USD | 252.43 USD | `-74.08%` | `115.00` |
| `Live` | `Long` | `2.21` | 2,290,000.00 USD | 0.00 USD | 808.52 USD | `-73.84%` | `365.02` |
| `Live` | `Long` | `2.29` | 2,290,000.00 USD | 0.00 USD | 263.93 USD | `-72.90%` | `115.00` |
| `Live` | `Long` | `2.35` | 2,290,000.00 USD | 0.00 USD | 110.07 USD | `-72.31%` | `46.94` |
| `Live` | `Long` | `2.69` | 2,290,000.00 USD | 0.00 USD | 942.44 USD | `-68.29%` | `351.00` |
| `Live` | `Long` | `2.85` | 2,290,000.00 USD | 0.00 USD | 328.32 USD | `-66.28%` | `115.00` |
| `Live` | `Long` | `2.87` | 2,290,000.00 USD | 0.00 USD | 381.65 USD | `-66.17%` | `133.21` |
| `Live` | `Long` | `2.94` | 2,290,000.00 USD | 0.00 USD | 44,510.00 USD | `-65.34%` | `15,165.76` |
| `Live` | `Long` | `2.96` | 2,240,000.00 USD | 0.00 USD | 11,810.00 USD | `-64.99%` | `3,981.48` |
| `Live` | `Long` | `2.98` | 2,230,000.00 USD | 0.00 USD | 111.12 USD | `-64.87%` | `37.35` |
| `Live` | `Long` | `3.00` | 2,230,000.00 USD | 0.00 USD | 21,010.00 USD | `-64.51%` | `6,990.57` |
| `Live` | `Long` | `3.06` | 2,210,000.00 USD | 0.00 USD | 102.71 USD | `-63.80%` | `33.51` |
| `Live` | `Long` | `3.17` | 2,210,000.00 USD | 0.00 USD | 1,200.00 USD | `-62.62%` | `377.71` |
| `Live` | `Long` | `3.31` | 2,210,000.00 USD | 0.00 USD | 24,670.00 USD | `-60.97%` | `7,465.11` |
| `Live` | `Long` | `3.37` | 2,180,000.00 USD | 0.00 USD | 389.53 USD | `-60.26%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,180,000.00 USD | 0.00 USD | 151.88 USD | `-60.14%` | `45.00` |
| `Live` | `Long` | `3.54` | 2,180,000.00 USD | 0.00 USD | 392.22 USD | `-58.14%` | `110.64` |
| `Live` | `Long` | `3.58` | 2,180,000.00 USD | 0.00 USD | 583.78 USD | `-57.66%` | `162.84` |
| `Live` | `Long` | `3.67` | 2,180,000.00 USD | 0.00 USD | 109.95 USD | `-56.72%` | `30.00` |
| `Live` | `Long` | `3.75` | 2,180,000.00 USD | 0.00 USD | 1,500.00 USD | `-55.66%` | `400.00` |
| `Live` | `Long` | `3.90` | 2,180,000.00 USD | 0.00 USD | 131.73 USD | `-54.00%` | `33.82` |
| `Live` | `Long` | `3.98` | 2,180,000.00 USD | 0.00 USD | 7,970.00 USD | `-52.94%` | `2,000.00` |
| `Live` | `Long` | `4.03` | 2,170,000.00 USD | 0.00 USD | 402.70 USD | `-52.47%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,170,000.00 USD | 0.00 USD | 152.29 USD | `-52.23%` | `37.65` |
| `Live` | `Long` | `4.08` | 2,170,000.00 USD | 0.00 USD | 1,630.00 USD | `-51.76%` | `400.00` |
| `Live` | `Long` | `4.14` | 2,170,000.00 USD | 0.00 USD | 159.29 USD | `-51.05%` | `38.43` |
| `Live` | `Long` | `4.21` | 2,170,000.00 USD | 0.00 USD | 393.34 USD | `-50.22%` | `93.32` |
| `Live` | `Long` | `4.24` | 2,170,000.00 USD | 0.00 USD | 169.40 USD | `-49.99%` | `40.00` |
| `Live` | `Long` | `4.25` | 2,170,000.00 USD | 0.00 USD | 196.42 USD | `-49.87%` | `46.27` |
| `Live` | `Long` | `4.45` | 2,170,000.00 USD | 0.00 USD | 110.77 USD | `-47.51%` | `24.92` |
| `Live` | `Long` | `4.59` | 2,170,000.00 USD | 0.00 USD | 30,970.00 USD | `-45.74%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,140,000.00 USD | 0.00 USD | 3,420.00 USD | `-45.38%` | `739.57` |
| `Live` | `Long` | `4.66` | 2,130,000.00 USD | 0.00 USD | 105.11 USD | `-45.03%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,130,000.00 USD | 0.00 USD | 3,280.00 USD | `-44.91%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,130,000.00 USD | 0.00 USD | 1,490.00 USD | `-44.79%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,130,000.00 USD | 0.00 USD | 8,380.00 USD | `-44.67%` | `1,787.97` |
| `Live` | `Long` | `4.70` | 2,120,000.00 USD | 0.00 USD | 7,040.00 USD | `-44.56%` | `1,500.00` |
| `Live` | `Long` | `4.75` | 2,110,000.00 USD | 0.00 USD | 474.50 USD | `-43.97%` | `100.00` |
| `Live` | `Long` | `4.76` | 2,110,000.00 USD | 0.00 USD | 105.64 USD | `-43.73%` | `22.17` |
| `Live` | `Long` | `4.83` | 2,110,000.00 USD | 0.00 USD | 467.01 USD | `-42.90%` | `96.59` |
| `Live` | `Long` | `4.87` | 2,110,000.00 USD | 0.00 USD | 2,430.00 USD | `-42.55%` | `500.00` |
| `Live` | `Long` | `4.89` | 2,110,000.00 USD | 0.00 USD | 16,080.00 USD | `-42.19%` | `3,286.00` |
| `Live` | `Long` | `4.91` | 2,090,000.00 USD | 0.00 USD | 3,880.00 USD | `-42.08%` | `790.61` |
| `Live` | `Long` | `4.92` | 2,090,000.00 USD | 0.00 USD | 1,230.00 USD | `-41.96%` | `251.00` |
| `Live` | `Long` | `4.93` | 2,090,000.00 USD | 0.00 USD | 314.61 USD | `-41.72%` | `63.75` |
| `Live` | `Long` | `4.95` | 2,090,000.00 USD | 0.00 USD | 565.66 USD | `-41.60%` | `114.39` |
| `Live` | `Long` | `4.96` | 2,090,000.00 USD | 0.00 USD | 945.36 USD | `-41.49%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,090,000.00 USD | 0.00 USD | 4,090.00 USD | `-41.37%` | `824.62` |
| `Live` | `Long` | `4.97` | 2,080,000.00 USD | 0.00 USD | 282.23 USD | `-41.25%` | `56.73` |
| `Live` | `Long` | `5.00` | 2,080,000.00 USD | 0.00 USD | 269.53 USD | `-41.01%` | `53.96` |
| `Live` | `Long` | `5.00` | 2,080,000.00 USD | 0.00 USD | 550.55 USD | `-40.90%` | `110.00` |
| `Live` | `Long` | `5.01` | 2,080,000.00 USD | 0.00 USD | 56,390.00 USD | `-40.78%` | `11,243.48` |
| `Live` | `Long` | `5.04` | 2,030,000.00 USD | 0.00 USD | 482.71 USD | `-40.54%` | `95.87` |
| `Live` | `Long` | `5.05` | 2,020,000.00 USD | 0.00 USD | 504.74 USD | `-40.30%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,020,000.00 USD | 0.00 USD | 213.20 USD | `-40.07%` | `42.01` |
| `Live` | `Long` | `5.08` | 2,020,000.00 USD | 0.00 USD | 105.46 USD | `-39.95%` | `20.74` |
| `Live` | `Long` | `5.09` | 2,020,000.00 USD | 0.00 USD | 1,270.00 USD | `-39.83%` | `249.71` |
| `Live` | `Long` | `5.11` | 2,020,000.00 USD | 0.00 USD | 118.44 USD | `-39.71%` | `23.20` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 1,040.00 USD | `-39.60%` | `202.43` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 250.20 USD | `-39.48%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,020,000.00 USD | 0.00 USD | 396.06 USD | `-39.36%` | `77.13` |
| `Live` | `Long` | `5.17` | 2,020,000.00 USD | 0.00 USD | 1,620.00 USD | `-38.89%` | `312.94` |
| `Live` | `Long` | `5.18` | 2,020,000.00 USD | 0.00 USD | 150.57 USD | `-38.77%` | `29.04` |
| `Live` | `Long` | `5.21` | 2,020,000.00 USD | 0.00 USD | 5,790.00 USD | `-38.42%` | `1,110.70` |
| `Live` | `Long` | `5.24` | 2,010,000.00 USD | 0.00 USD | 502.82 USD | `-38.18%` | `96.05` |
| `Live` | `Long` | `5.25` | 2,010,000.00 USD | 0.00 USD | 213.00 USD | `-38.06%` | `40.61` |
| `Live` | `Long` | `5.25` | 2,010,000.00 USD | 0.00 USD | 1,050.00 USD | `-37.94%` | `200.00` |
| `Live` | `Long` | `5.26` | 2,010,000.00 USD | 0.00 USD | 2,230.00 USD | `-37.82%` | `423.54` |
| `Live` | `Long` | `5.29` | 2,010,000.00 USD | 0.00 USD | 161,490.00 USD | `-37.59%` | `30,556.43` |
| `Live` | `Long` | `5.32` | 1,850,000.00 USD | 0.00 USD | 232.85 USD | `-37.23%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,850,000.00 USD | 0.00 USD | 716.11 USD | `-37.12%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,850,000.00 USD | 0.00 USD | 660.46 USD | `-36.29%` | `122.42` |
| `Live` | `Long` | `5.41` | 1,850,000.00 USD | 0.00 USD | 260.63 USD | `-36.17%` | `48.22` |
| `Live` | `Long` | `5.42` | 1,850,000.00 USD | 0.00 USD | 20,560.00 USD | `-36.05%` | `3,797.34` |
| `Live` | `Long` | `5.42` | 1,830,000.00 USD | 0.00 USD | 160,400.00 USD | `-35.94%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,660,000.00 USD | 0.00 USD | 1,360.00 USD | `-35.82%` | `250.00` |
| `Live` | `Long` | `5.45` | 1,660,000.00 USD | 0.00 USD | 299.48 USD | `-35.70%` | `55.00` |
| `Live` | `Long` | `5.46` | 1,660,000.00 USD | 0.00 USD | 264.72 USD | `-35.46%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-35.34%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,660,000.00 USD | 0.00 USD | 354.06 USD | `-35.23%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,660,000.00 USD | 0.00 USD | 19,290.00 USD | `-35.11%` | `3,510.41` |
| `Live` | `Long` | `5.54` | 1,640,000.00 USD | 0.00 USD | 1,490.00 USD | `-34.64%` | `270.00` |
| `Live` | `Long` | `5.54` | 1,640,000.00 USD | 0.00 USD | 2,880.00 USD | `-34.52%` | `519.63` |
| `Live` | `Long` | `5.58` | 1,640,000.00 USD | 0.00 USD | 63,260.00 USD | `-34.16%` | `11,347.58` |
| `Live` | `Long` | `5.61` | 1,570,000.00 USD | 0.00 USD | 34,490.00 USD | `-33.81%` | `6,153.60` |
| `Live` | `Long` | `5.62` | 1,540,000.00 USD | 0.00 USD | 139.36 USD | `-33.69%` | `24.82` |
| `Live` | `Long` | `5.63` | 1,540,000.00 USD | 0.00 USD | 468.55 USD | `-33.46%` | `83.15` |
| `Live` | `Long` | `5.72` | 1,540,000.00 USD | 0.00 USD | 2,390.00 USD | `-32.39%` | `417.17` |
| `Live` | `Long` | `5.74` | 1,540,000.00 USD | 0.00 USD | 661.65 USD | `-32.27%` | `115.37` |
| `Live` | `Long` | `5.75` | 1,540,000.00 USD | 0.00 USD | 125.70 USD | `-32.16%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,540,000.00 USD | 0.00 USD | 3,190.00 USD | `-32.04%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,530,000.00 USD | 0.00 USD | 10,850.00 USD | `-31.92%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,520,000.00 USD | 0.00 USD | 801.40 USD | `-31.80%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,520,000.00 USD | 0.00 USD | 635.31 USD | `-31.57%` | `109.63` |
| `Live` | `Long` | `5.80` | 1,520,000.00 USD | 0.00 USD | 580.50 USD | `-31.45%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,520,000.00 USD | 0.00 USD | 106.65 USD | `-31.33%` | `18.34` |
| `Live` | `Long` | `5.83` | 1,520,000.00 USD | 0.00 USD | 1,360.00 USD | `-31.21%` | `233.60` |
| `Live` | `Long` | `5.84` | 1,520,000.00 USD | 0.00 USD | 146.13 USD | `-30.98%` | `25.00` |
| `Live` | `Long` | `5.86` | 1,520,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.86%` | `360.33` |
| `Live` | `Long` | `5.89` | 1,520,000.00 USD | 0.00 USD | 984.70 USD | `-30.38%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,520,000.00 USD | 0.00 USD | 399.18 USD | `-30.27%` | `67.60` |
| `Live` | `Long` | `5.96` | 1,510,000.00 USD | 0.00 USD | 11,720.00 USD | `-29.68%` | `1,968.19` |
| `Live` | `Long` | `5.96` | 1,500,000.00 USD | 0.00 USD | 6,320.00 USD | `-29.56%` | `1,060.32` |
| `Live` | `Long` | `5.97` | 1,500,000.00 USD | 0.00 USD | 585.97 USD | `-29.44%` | `98.07` |
| `Live` | `Long` | `6.00` | 1,500,000.00 USD | 0.00 USD | 341.56 USD | `-29.09%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,500,000.00 USD | 0.00 USD | 446.85 USD | `-28.97%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,500,000.00 USD | 0.00 USD | 437.84 USD | `-28.61%` | `72.43` |
| `Live` | `Long` | `6.05` | 1,500,000.00 USD | 0.00 USD | 1,310.00 USD | `-28.50%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,490,000.00 USD | 0.00 USD | 265.10 USD | `-28.38%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,490,000.00 USD | 0.00 USD | 1,690.00 USD | `-28.26%` | `278.94` |
| `Live` | `Long` | `6.09` | 1,490,000.00 USD | 0.00 USD | 3,530.00 USD | `-28.02%` | `579.39` |
| `Live` | `Long` | `6.12` | 1,490,000.00 USD | 0.00 USD | 1,140.00 USD | `-27.79%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,490,000.00 USD | 0.00 USD | 137.02 USD | `-27.67%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,490,000.00 USD | 0.00 USD | 2,030.00 USD | `-27.55%` | `330.65` |
| `Live` | `Long` | `6.14` | 1,480,000.00 USD | 0.00 USD | 238.61 USD | `-27.43%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,480,000.00 USD | 0.00 USD | 7,810.00 USD | `-27.31%` | `1,268.30` |
| `Live` | `Long` | `6.17` | 1,480,000.00 USD | 0.00 USD | 104.36 USD | `-27.08%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,480,000.00 USD | 0.00 USD | 310.25 USD | `-26.72%` | `50.00` |
| `Live` | `Long` | `6.25` | 1,480,000.00 USD | 0.00 USD | 972.65 USD | `-26.13%` | `155.50` |
| `Live` | `Long` | `6.28` | 1,480,000.00 USD | 0.00 USD | 2,510.00 USD | `-25.90%` | `400.00` |
| `Live` | `Long` | `6.29` | 1,470,000.00 USD | 0.00 USD | 2,430.00 USD | `-25.66%` | `386.46` |
| `Live` | `Long` | `6.33` | 1,470,000.00 USD | 0.00 USD | 277.48 USD | `-25.31%` | `43.87` |
| `Live` | `Long` | `6.33` | 1,470,000.00 USD | 0.00 USD | 1,430.00 USD | `-25.19%` | `225.14` |
| `Live` | `Long` | `6.36` | 1,470,000.00 USD | 0.00 USD | 4,470.00 USD | `-24.95%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,460,000.00 USD | 0.00 USD | 284,770.00 USD | `-24.83%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 1,180,000.00 USD | 0.00 USD | 1,310.00 USD | `-24.72%` | `204.92` |
| `Live` | `Long` | `6.38` | 1,180,000.00 USD | 0.00 USD | 5,120.00 USD | `-24.60%` | `801.31` |
| `Live` | `Long` | `6.39` | 1,170,000.00 USD | 0.00 USD | 5,940.00 USD | `-24.48%` | `928.10` |
| `Live` | `Long` | `6.42` | 1,170,000.00 USD | 0.00 USD | 306.32 USD | `-24.24%` | `47.75` |
| `Live` | `Long` | `6.42` | 1,170,000.00 USD | 0.00 USD | 484.64 USD | `-24.13%` | `75.43` |
| `Live` | `Long` | `6.43` | 1,170,000.00 USD | 0.00 USD | 6,780.00 USD | `-24.01%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 1,160,000.00 USD | 0.00 USD | 363,480.00 USD | `-23.65%` | `56,222.15` |
| `Live` | `Long` | `6.50` | 796,220.00 USD | 0.00 USD | 1,520.00 USD | `-23.18%` | `234.11` |
| `Live` | `Long` | `6.54` | 794,700.00 USD | 0.00 USD | 852.03 USD | `-22.83%` | `130.38` |
| `Live` | `Long` | `6.54` | 793,840.00 USD | 0.00 USD | 8,970.00 USD | `-22.71%` | `1,370.89` |
| `Live` | `Long` | `6.59` | 784,870.00 USD | 0.00 USD | 2,870.00 USD | `-22.12%` | `435.69` |
| `Live` | `Long` | `6.62` | 782,000.00 USD | 0.00 USD | 2,110.00 USD | `-21.88%` | `318.57` |
| `Live` | `Long` | `6.62` | 779,890.00 USD | 0.00 USD | 1,880.00 USD | `-21.76%` | `283.49` |
| `Live` | `Long` | `6.63` | 778,010.00 USD | 0.00 USD | 1,780.00 USD | `-21.65%` | `268.08` |
| `Live` | `Long` | `6.67` | 776,230.00 USD | 0.00 USD | 1,320.00 USD | `-21.17%` | `198.12` |
| `Live` | `Long` | `6.68` | 774,910.00 USD | 0.00 USD | 3,160.00 USD | `-21.06%` | `472.28` |
| `Live` | `Long` | `6.71` | 771,750.00 USD | 0.00 USD | 11,000.00 USD | `-20.82%` | `1,641.31` |
| `Live` | `Long` | `6.71` | 760,750.00 USD | 0.00 USD | 6,180.00 USD | `-20.70%` | `920.74` |
| `Live` | `Long` | `6.75` | 754,570.00 USD | 0.00 USD | 1,330.00 USD | `-20.23%` | `196.95` |
| `Live` | `Long` | `6.78` | 753,240.00 USD | 0.00 USD | 7,990.00 USD | `-19.99%` | `1,179.83` |
| `Live` | `Long` | `6.79` | 745,240.00 USD | 0.00 USD | 22,020.00 USD | `-19.87%` | `3,245.57` |
| `Live` | `Long` | `6.79` | 723,220.00 USD | 0.00 USD | 5,170.00 USD | `-19.76%` | `761.18` |
| `Live` | `Long` | `6.80` | 718,050.00 USD | 0.00 USD | 1,500.00 USD | `-19.64%` | `220.95` |
| `Live` | `Long` | `6.82` | 716,550.00 USD | 0.00 USD | 7,230.00 USD | `-19.52%` | `1,061.04` |
| `Live` | `Long` | `6.83` | 709,310.00 USD | 0.00 USD | 271.02 USD | `-19.40%` | `39.71` |
| `Live` | `Long` | `6.87` | 709,040.00 USD | 0.00 USD | 3,340.00 USD | `-18.93%` | `486.46` |
| `Live` | `Long` | `6.88` | 705,700.00 USD | 0.00 USD | 263.66 USD | `-18.81%` | `38.35` |
| `Live` | `Long` | `6.88` | 705,440.00 USD | 0.00 USD | 1,580.00 USD | `-18.69%` | `229.18` |
| `Live` | `Long` | `6.92` | 703,860.00 USD | 0.00 USD | 579.62 USD | `-18.22%` | `83.70` |
| `Live` | `Long` | `6.93` | 703,280.00 USD | 0.00 USD | 3,500.00 USD | `-18.10%` | `504.07` |
| `Live` | `Long` | `6.95` | 699,790.00 USD | 0.00 USD | 215.30 USD | `-17.99%` | `31.00` |
| `Live` | `Long` | `6.96` | 699,570.00 USD | 0.00 USD | 7,240.00 USD | `-17.87%` | `1,041.68` |
| `Live` | `Long` | `6.96` | 692,330.00 USD | 0.00 USD | 636.74 USD | `-17.75%` | `91.42` |
| `Live` | `Long` | `6.97` | 691,690.00 USD | 0.00 USD | 128,810.00 USD | `-17.63%` | `18,466.99` |
| `Live` | `Long` | `7.00` | 562,880.00 USD | 0.00 USD | 1,040.00 USD | `-17.39%` | `149.32` |
| `Live` | `Long` | `7.01` | 561,840.00 USD | 0.00 USD | 20,890.00 USD | `-17.16%` | `2,978.11` |
| `Live` | `Long` | `7.03` | 540,950.00 USD | 0.00 USD | 1,370.00 USD | `-17.04%` | `194.51` |
| `Live` | `Long` | `7.07` | 539,580.00 USD | 0.00 USD | 23,960.00 USD | `-16.57%` | `3,390.75` |
| `Live` | `Long` | `7.08` | 515,620.00 USD | 0.00 USD | 6,700.00 USD | `-16.45%` | `947.44` |
| `Live` | `Long` | `7.08` | 508,920.00 USD | 0.00 USD | 1,050.00 USD | `-16.33%` | `148.63` |
| `Live` | `Long` | `7.09` | 507,870.00 USD | 0.00 USD | 2,130.00 USD | `-16.21%` | `300.00` |
| `Live` | `Long` | `7.11` | 505,740.00 USD | 0.00 USD | 28,530.00 USD | `-16.10%` | `4,015.35` |
| `Live` | `Long` | `7.12` | 477,210.00 USD | 0.00 USD | 379.66 USD | `-15.98%` | `53.36` |
| `Live` | `Long` | `7.13` | 476,830.00 USD | 0.00 USD | 777.50 USD | `-15.74%` | `108.97` |
| `Live` | `Long` | `7.14` | 476,050.00 USD | 0.00 USD | 20,270.00 USD | `-15.62%` | `2,837.00` |
| `Live` | `Long` | `7.17` | 455,780.00 USD | 0.00 USD | 2,380.00 USD | `-15.27%` | `331.12` |
| `Live` | `Long` | `7.18` | 453,410.00 USD | 0.00 USD | 1,440.00 USD | `-15.15%` | `200.95` |
| `Live` | `Long` | `7.20` | 451,960.00 USD | 0.00 USD | 2,520.00 USD | `-15.03%` | `350.58` |
| `Live` | `Long` | `7.21` | 449,440.00 USD | 0.00 USD | 322.94 USD | `-14.80%` | `44.76` |
| `Live` | `Long` | `7.24` | 449,120.00 USD | 0.00 USD | 1,480.00 USD | `-14.56%` | `205.21` |
| `Live` | `Long` | `7.25` | 447,630.00 USD | 0.00 USD | 29,170.00 USD | `-14.44%` | `4,025.65` |
| `Live` | `Long` | `7.25` | 418,470.00 USD | 0.00 USD | 24,850.00 USD | `-14.32%` | `3,424.57` |
| `Live` | `Long` | `7.29` | 393,620.00 USD | 0.00 USD | 36,420.00 USD | `-13.97%` | `5,000.00` |
| `Live` | `Long` | `7.29` | 357,200.00 USD | 0.00 USD | 1,680.00 USD | `-13.85%` | `230.97` |
| `Live` | `Long` | `7.34` | 355,510.00 USD | 0.00 USD | 552.42 USD | `-13.26%` | `75.21` |
| `Live` | `Long` | `7.36` | 354,960.00 USD | 0.00 USD | 3,820.00 USD | `-13.14%` | `519.63` |
| `Live` | `Long` | `7.37` | 351,140.00 USD | 0.00 USD | 3,970.00 USD | `-13.03%` | `539.15` |
| `Live` | `Long` | `7.38` | 347,170.00 USD | 0.00 USD | 1,100.00 USD | `-12.91%` | `148.75` |
| `Live` | `Long` | `7.38` | 346,070.00 USD | 0.00 USD | 13,430.00 USD | `-12.79%` | `1,817.92` |
| `Live` | `Long` | `7.42` | 332,650.00 USD | 0.00 USD | 147.61 USD | `-12.32%` | `19.88` |
| `Live` | `Long` | `7.43` | 332,500.00 USD | 0.00 USD | 3,290.00 USD | `-12.20%` | `442.38` |
| `Live` | `Long` | `7.45` | 329,210.00 USD | 0.00 USD | 2,410.00 USD | `-12.08%` | `324.35` |
| `Live` | `Long` | `7.46` | 326,790.00 USD | 0.00 USD | 10,390.00 USD | `-11.96%` | `1,393.53` |
| `Live` | `Long` | `7.46` | 316,410.00 USD | 0.00 USD | 4,590.00 USD | `-11.84%` | `614.36` |
| `Live` | `Long` | `7.47` | 311,820.00 USD | 0.00 USD | 1,120.00 USD | `-11.73%` | `149.52` |
| `Live` | `Long` | `7.50` | 310,700.00 USD | 0.00 USD | 962.81 USD | `-11.49%` | `128.46` |
| `Live` | `Long` | `7.50` | 309,740.00 USD | 0.00 USD | 421.78 USD | `-11.37%` | `56.20` |
| `Live` | `Long` | `7.51` | 309,320.00 USD | 0.00 USD | 1,710.00 USD | `-11.25%` | `228.21` |
| `Live` | `Long` | `7.53` | 307,600.00 USD | 0.00 USD | 1,570.00 USD | `-11.14%` | `208.52` |
| `Live` | `Long` | `7.54` | 306,030.00 USD | 0.00 USD | 4,210.00 USD | `-11.02%` | `559.01` |
| `Live` | `Long` | `7.55` | 301,820.00 USD | 0.00 USD | 2,580.00 USD | `-10.78%` | `341.09` |
| `Live` | `Long` | `7.57` | 299,240.00 USD | 0.00 USD | 25,060.00 USD | `-10.66%` | `3,312.23` |
| `Live` | `Long` | `7.58` | 274,190.00 USD | 0.00 USD | 118.25 USD | `-10.55%` | `15.61` |
| `Live` | `Long` | `7.59` | 274,070.00 USD | 0.00 USD | 1,630.00 USD | `-10.31%` | `214.22` |
| `Live` | `Long` | `7.62` | 272,440.00 USD | 0.00 USD | 754.04 USD | `-10.07%` | `99.02` |
| `Live` | `Long` | `7.62` | 271,690.00 USD | 0.00 USD | 787.51 USD | `-9.96%` | `103.28` |
| `Live` | `Long` | `7.63` | 270,900.00 USD | 0.00 USD | 378.93 USD | `-9.84%` | `49.63` |
| `Live` | `Long` | `7.66` | 270,520.00 USD | 0.00 USD | 135.42 USD | `-9.60%` | `17.69` |
| `Live` | `Long` | `7.67` | 270,390.00 USD | 0.00 USD | 256.09 USD | `-9.48%` | `33.41` |
| `Live` | `Long` | `7.67` | 270,130.00 USD | 0.00 USD | 4,480.00 USD | `-9.36%` | `583.63` |
| `Live` | `Long` | `7.68` | 265,650.00 USD | 0.00 USD | 739.30 USD | `-9.25%` | `96.20` |
| `Live` | `Long` | `7.70` | 264,910.00 USD | 0.00 USD | 6,690.00 USD | `-9.13%` | `869.22` |
| `Live` | `Long` | `7.75` | 258,220.00 USD | 0.00 USD | 500.12 USD | `-8.42%` | `64.49` |
| `Live` | `Long` | `7.76` | 257,720.00 USD | 0.00 USD | 455.73 USD | `-8.30%` | `58.69` |
| `Live` | `Long` | `7.78` | 257,270.00 USD | 0.00 USD | 6,310.00 USD | `-8.18%` | `812.08` |
| `Live` | `Long` | `7.79` | 250,950.00 USD | 0.00 USD | 3,750.00 USD | `-8.07%` | `481.06` |
| `Live` | `Long` | `7.79` | 247,210.00 USD | 0.00 USD | 4,480.00 USD | `-7.95%` | `574.50` |
| `Live` | `Long` | `7.80` | 242,730.00 USD | 0.00 USD | 6,380.00 USD | `-7.83%` | `817.06` |
| `Live` | `Long` | `7.83` | 236,350.00 USD | 0.00 USD | 1,940.00 USD | `-7.59%` | `247.42` |
| `Live` | `Long` | `7.84` | 234,420.00 USD | 0.00 USD | 22,560.00 USD | `-7.36%` | `2,875.86` |
| `Live` | `Long` | `7.87` | 211,850.00 USD | 0.00 USD | 233.83 USD | `-7.12%` | `29.73` |
| `Live` | `Long` | `7.88` | 211,620.00 USD | 0.00 USD | 555.19 USD | `-7.00%` | `70.50` |
| `Live` | `Long` | `7.89` | 211,070.00 USD | 0.00 USD | 15,880.00 USD | `-6.77%` | `2,011.99` |
| `Live` | `Long` | `7.91` | 195,180.00 USD | 0.00 USD | 2,930.00 USD | `-6.65%` | `370.74` |
| `Live` | `Long` | `7.92` | 192,250.00 USD | 0.00 USD | 4,600.00 USD | `-6.41%` | `580.78` |
| `Live` | `Long` | `7.93` | 187,650.00 USD | 0.00 USD | 16,340.00 USD | `-6.29%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 171,300.00 USD | 0.00 USD | 141.74 USD | `-6.18%` | `17.84` |
| `Live` | `Long` | `7.96` | 171,160.00 USD | 0.00 USD | 127,900.00 USD | `-6.06%` | `16,078.30` |
| `Live` | `Long` | `7.97` | 43,260.00 USD | 0.00 USD | 1,580.00 USD | `-5.82%` | `198.26` |
| `Live` | `Long` | `7.99` | 41,680.00 USD | 0.00 USD | 1,280.00 USD | `-5.70%` | `160.68` |
| `Live` | `Long` | `8.00` | 40,400.00 USD | 0.00 USD | 530.79 USD | `-5.59%` | `66.39` |
| `Live` | `Long` | `8.03` | 39,870.00 USD | 0.00 USD | 14,210.00 USD | `-5.23%` | `1,770.35` |
| `Live` | `Long` | `8.04` | 25,660.00 USD | 0.00 USD | 823.33 USD | `-5.00%` | `102.34` |
| `Live` | `Short` | `8.05` | 265.81 USD | 265.81 USD | 0.00 USD | `-4.88%` | `33.00` |
| `Live` | `Long` | `8.06` | 24,830.00 USD | 0.00 USD | 439.54 USD | `-4.76%` | `54.50` |
| `Live` | `Long` | `8.07` | 24,400.00 USD | 0.00 USD | 21,710.00 USD | `-4.64%` | `2,688.93` |
| `Live` | `Long` | `8.12` | 2,680.00 USD | 0.00 USD | 738.14 USD | `-4.17%` | `90.96` |
| `Live` | `Long` | `8.12` | 1,940.00 USD | 0.00 USD | 521.62 USD | `-4.05%` | `64.20` |
| `Live` | `Long` | `8.15` | 1,420.00 USD | 0.00 USD | 1,420.00 USD | `-3.70%` | `174.44` |
| `Live` | `Short` | `8.69` | 475.12 USD | 209.31 USD | 0.00 USD | `+2.56%` | `24.10` |
| `Live` | `Short` | `8.82` | 6,480.00 USD | 6,000.00 USD | 0.00 USD | `+4.22%` | `680.16` |
| `Live` | `Short` | `8.87` | 7,640.00 USD | 1,160.00 USD | 0.00 USD | `+4.69%` | `130.57` |
| `Live` | `Short` | `8.88` | 8,330.00 USD | 691.70 USD | 0.00 USD | `+4.92%` | `77.85` |
| `Live` | `Short` | `8.89` | 9,140.00 USD | 808.47 USD | 0.00 USD | `+5.04%` | `90.89` |
| `Live` | `Short` | `8.90` | 18,040.00 USD | 8,910.00 USD | 0.00 USD | `+5.16%` | `1,000.45` |
| `Live` | `Short` | `8.97` | 28,520.00 USD | 10,480.00 USD | 0.00 USD | `+5.99%` | `1,167.41` |
| `Live` | `Short` | `8.99` | 568,230.00 USD | 539,710.00 USD | 0.00 USD | `+6.22%` | `60,000.94` |
| `Live` | `Short` | `9.05` | 568,440.00 USD | 213.70 USD | 0.00 USD | `+6.93%` | `23.60` |
| `Live` | `Short` | `9.06` | 574,480.00 USD | 6,040.00 USD | 0.00 USD | `+7.05%` | `666.20` |
| `Live` | `Short` | `9.10` | 578,370.00 USD | 3,890.00 USD | 0.00 USD | `+7.40%` | `427.53` |
| `Live` | `Short` | `9.14` | 578,550.00 USD | 180.80 USD | 0.00 USD | `+7.99%` | `19.77` |
| `Live` | `Short` | `9.29` | 582,410.00 USD | 3,860.00 USD | 0.00 USD | `+9.77%` | `415.00` |
| `Live` | `Short` | `9.41` | 582,850.00 USD | 440.06 USD | 0.00 USD | `+11.18%` | `46.74` |
| `Live` | `Short` | `9.62` | 582,990.00 USD | 138.98 USD | 0.00 USD | `+13.66%` | `14.44` |
| `Live` | `Short` | `9.64` | 584,920.00 USD | 1,930.00 USD | 0.00 USD | `+13.90%` | `200.61` |
| `Live` | `Short` | `9.69` | 585,210.00 USD | 285.51 USD | 0.00 USD | `+14.37%` | `29.48` |
| `Live` | `Short` | `9.73` | 585,400.00 USD | 192.95 USD | 0.00 USD | `+14.96%` | `19.82` |
| `Live` | `Short` | `9.88` | 585,770.00 USD | 371.77 USD | 0.00 USD | `+16.73%` | `37.61` |
| `Live` | `Short` | `10.35` | 588,430.00 USD | 2,650.00 USD | 0.00 USD | `+22.17%` | `256.58` |
| `Live` | `Short` | `10.47` | 609,380.00 USD | 20,950.00 USD | 0.00 USD | `+23.70%` | `2,000.00` |
| `Live` | `Short` | `10.56` | 609,900.00 USD | 523.81 USD | 0.00 USD | `+24.76%` | `49.58` |
| `Live` | `Short` | `10.78` | 610,080.00 USD | 173.91 USD | 0.00 USD | `+27.24%` | `16.14` |
| `Live` | `Short` | `10.81` | 611,220.00 USD | 1,150.00 USD | 0.00 USD | `+27.72%` | `106.17` |
| `Live` | `Short` | `10.98` | 666,150.00 USD | 54,920.00 USD | 0.00 USD | `+29.72%` | `5,000.00` |
| `Live` | `Short` | `11.01` | 673,120.00 USD | 6,970.00 USD | 0.00 USD | `+29.96%` | `633.00` |
| `Live` | `Short` | `11.19` | 677,330.00 USD | 4,210.00 USD | 0.00 USD | `+32.09%` | `376.48` |
| `Live` | `Short` | `11.27` | 801,650.00 USD | 124,320.00 USD | 0.00 USD | `+33.03%` | `11,035.87` |
| `Live` | `Short` | `11.46` | 801,970.00 USD | 322.74 USD | 0.00 USD | `+35.39%` | `28.15` |
| `Live` | `Short` | `11.48` | 802,240.00 USD | 275.18 USD | 0.00 USD | `+35.63%` | `23.96` |
| `Live` | `Short` | `11.62` | 814,380.00 USD | 12,140.00 USD | 0.00 USD | `+37.28%` | `1,043.90` |
| `Live` | `Short` | `11.69` | 1,110,000.00 USD | 296,760.00 USD | 0.00 USD | `+37.99%` | `25,397.02` |
| `Live` | `Short` | `11.93` | 1,110,000.00 USD | 505.74 USD | 0.00 USD | `+40.82%` | `42.41` |
| `Live` | `Short` | `11.95` | 1,110,000.00 USD | 1,050.00 USD | 0.00 USD | `+41.06%` | `87.54` |
| `Live` | `Short` | `12.30` | 1,110,000.00 USD | 1,730.00 USD | 0.00 USD | `+45.31%` | `140.71` |
| `Live` | `Short` | `12.40` | 1,110,000.00 USD | 343.62 USD | 0.00 USD | `+46.49%` | `27.70` |
| `Live` | `Short` | `12.96` | 1,120,000.00 USD | 1,530.00 USD | 0.00 USD | `+52.99%` | `117.87` |
| `Live` | `Short` | `13.20` | 1,200,000.00 USD | 87,940.00 USD | 0.00 USD | `+55.82%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 1,210,000.00 USD | 3,810.00 USD | 0.00 USD | `+57.00%` | `286.56` |
| `Live` | `Short` | `13.46` | 1,210,000.00 USD | 430.34 USD | 0.00 USD | `+59.01%` | `31.96` |
| `Live` | `Short` | `13.49` | 1,270,000.00 USD | 61,470.00 USD | 0.00 USD | `+59.36%` | `4,555.14` |
| `Live` | `Short` | `13.54` | 1,270,000.00 USD | 111.48 USD | 0.00 USD | `+59.96%` | `8.23` |
| `Live` | `Short` | `13.69` | 1,270,000.00 USD | 172.29 USD | 0.00 USD | `+61.61%` | `12.59` |
| `Live` | `Short` | `14.66` | 1,270,000.00 USD | 823.29 USD | 0.00 USD | `+73.18%` | `56.14` |
| `Live` | `Short` | `14.78` | 1,270,000.00 USD | 242.46 USD | 0.00 USD | `+74.48%` | `16.41` |
| `Live` | `Short` | `15.06` | 1,270,000.00 USD | 324.65 USD | 0.00 USD | `+77.91%` | `21.55` |
| `Live` | `Short` | `15.09` | 1,270,000.00 USD | 219.34 USD | 0.00 USD | `+78.14%` | `14.54` |
| `Live` | `Short` | `15.12` | 1,270,000.00 USD | 542.84 USD | 0.00 USD | `+78.61%` | `35.89` |
| `Live` | `Short` | `15.23` | 1,280,000.00 USD | 4,230.00 USD | 0.00 USD | `+79.91%` | `277.54` |
| `Live` | `Short` | `15.29` | 1,280,000.00 USD | 229.43 USD | 0.00 USD | `+80.62%` | `15.00` |
| `Live` | `Short` | `15.35` | 1,280,000.00 USD | 230.17 USD | 0.00 USD | `+81.21%` | `15.00` |
| `Live` | `Short` | `15.38` | 1,300,000.00 USD | 20,000.00 USD | 0.00 USD | `+81.68%` | `1,300.00` |
| `Live` | `Short` | `15.77` | 1,300,000.00 USD | 185.55 USD | 0.00 USD | `+86.17%` | `11.77` |
| `Live` | `Short` | `15.82` | 1,300,000.00 USD | 1,700.00 USD | 0.00 USD | `+86.88%` | `107.48` |
| `Live` | `Short` | `16.38` | 1,560,000.00 USD | 265,410.00 USD | 0.00 USD | `+93.38%` | `16,208.00` |
| `Live` | `Short` | `16.50` | 1,590,000.00 USD | 23,330.00 USD | 0.00 USD | `+94.79%` | `1,414.55` |
| `Live` | `Short` | `16.52` | 1,590,000.00 USD | 190.91 USD | 0.00 USD | `+95.03%` | `11.56` |
| `Live` | `Short` | `16.62` | 1,590,000.00 USD | 118.20 USD | 0.00 USD | `+96.33%` | `7.11` |
| `Live` | `Short` | `16.64` | 1,610,000.00 USD | 24,270.00 USD | 0.00 USD | `+96.45%` | `1,459.25` |
| `Live` | `Short` | `16.91` | 1,610,000.00 USD | 1,960.00 USD | 0.00 USD | `+99.63%` | `115.73` |
| `Live` | `Short` | `16.93` | 1,700,000.00 USD | 85,310.00 USD | 0.00 USD | `+99.99%` | `5,037.66` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 359,270.00 USD | 0.00 USD | 611.73 USD | `-72.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 358,660.00 USD | 0.00 USD | 793.75 USD | `-52.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 357,870.00 USD | 0.00 USD | 67,970.00 USD | `-40.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 289,900.00 USD | 0.00 USD | 205.30 USD | `-37.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 289,690.00 USD | 0.00 USD | 465.42 USD | `-35.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 289,230.00 USD | 0.00 USD | 349.35 USD | `-34.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 288,880.00 USD | 0.00 USD | 1,020.00 USD | `-34.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 287,860.00 USD | 0.00 USD | 1,330.00 USD | `-31.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 286,530.00 USD | 0.00 USD | 493.50 USD | `-29.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 286,040.00 USD | 0.00 USD | 100.98 USD | `-29.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 285,940.00 USD | 0.00 USD | 500.70 USD | `-29.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 285,440.00 USD | 0.00 USD | 4,160.00 USD | `-27.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 281,280.00 USD | 0.00 USD | 6,500.00 USD | `-27.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.21` | 274,780.00 USD | 0.00 USD | 906.18 USD | `-26.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.25` | 273,880.00 USD | 0.00 USD | 127.35 USD | `-26.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 273,750.00 USD | 0.00 USD | 864.38 USD | `-25.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 272,880.00 USD | 0.00 USD | 130.10 USD | `-23.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 272,750.00 USD | 0.00 USD | 4,340.00 USD | `-22.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 268,410.00 USD | 0.00 USD | 5,520.00 USD | `-20.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 262,890.00 USD | 0.00 USD | 203.67 USD | `-20.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 262,690.00 USD | 0.00 USD | 296.34 USD | `-20.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 262,390.00 USD | 0.00 USD | 921.19 USD | `-20.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 261,470.00 USD | 0.00 USD | 709.98 USD | `-18.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.91` | 260,760.00 USD | 0.00 USD | 4,630.00 USD | `-18.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 256,130.00 USD | 0.00 USD | 691.50 USD | `-18.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 255,440.00 USD | 0.00 USD | 262.44 USD | `-17.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 255,180.00 USD | 0.00 USD | 24,350.00 USD | `-17.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.04` | 230,830.00 USD | 0.00 USD | 653.69 USD | `-16.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.11` | 230,170.00 USD | 0.00 USD | 187.79 USD | `-16.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 229,990.00 USD | 0.00 USD | 6,790.00 USD | `-15.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 223,200.00 USD | 0.00 USD | 4,960.00 USD | `-15.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.21` | 218,240.00 USD | 0.00 USD | 7,210.00 USD | `-14.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 211,030.00 USD | 0.00 USD | 282.74 USD | `-14.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 210,750.00 USD | 0.00 USD | 603.44 USD | `-14.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 210,140.00 USD | 0.00 USD | 464.61 USD | `-14.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 209,680.00 USD | 0.00 USD | 2,090.00 USD | `-13.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 207,590.00 USD | 0.00 USD | 129.58 USD | `-13.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 207,460.00 USD | 0.00 USD | 114.65 USD | `-13.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.39` | 207,340.00 USD | 0.00 USD | 702.75 USD | `-12.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.41` | 206,640.00 USD | 0.00 USD | 4,630.00 USD | `-12.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 202,010.00 USD | 0.00 USD | 199.39 USD | `-11.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 201,810.00 USD | 0.00 USD | 6,270.00 USD | `-11.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 195,540.00 USD | 0.00 USD | 37,420.00 USD | `-11.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 158,120.00 USD | 0.00 USD | 2,120.00 USD | `-11.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 156,000.00 USD | 0.00 USD | 799.83 USD | `-11.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 155,200.00 USD | 0.00 USD | 820.44 USD | `-10.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 154,380.00 USD | 0.00 USD | 218.24 USD | `-10.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 154,160.00 USD | 0.00 USD | 113.78 USD | `-10.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.61` | 154,040.00 USD | 0.00 USD | 152.10 USD | `-10.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 153,890.00 USD | 0.00 USD | 297.59 USD | `-10.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.68` | 153,590.00 USD | 0.00 USD | 528.88 USD | `-9.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 153,060.00 USD | 0.00 USD | 360.13 USD | `-9.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 152,700.00 USD | 0.00 USD | 578.04 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 152,130.00 USD | 0.00 USD | 106.32 USD | `-8.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.79` | 152,020.00 USD | 0.00 USD | 424.05 USD | `-7.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 151,600.00 USD | 0.00 USD | 1,170.00 USD | `-7.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.82` | 150,430.00 USD | 0.00 USD | 3,940.00 USD | `-7.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.83` | 146,490.00 USD | 0.00 USD | 154.70 USD | `-7.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 146,330.00 USD | 0.00 USD | 115.23 USD | `-7.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 146,220.00 USD | 0.00 USD | 183.33 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 146,030.00 USD | 0.00 USD | 1,890.00 USD | `-6.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 144,140.00 USD | 0.00 USD | 6,840.00 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 137,300.00 USD | 0.00 USD | 5,710.00 USD | `-6.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 131,590.00 USD | 0.00 USD | 1,590.00 USD | `-6.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 130,010.00 USD | 0.00 USD | 898.42 USD | `-6.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 129,110.00 USD | 0.00 USD | 7,960.00 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 121,150.00 USD | 0.00 USD | 246.52 USD | `-5.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.97` | 120,910.00 USD | 0.00 USD | 2,420.00 USD | `-5.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 118,480.00 USD | 0.00 USD | 1,440.00 USD | `-5.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 117,050.00 USD | 0.00 USD | 435.73 USD | `-5.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 116,610.00 USD | 0.00 USD | 4,320.00 USD | `-5.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 112,290.00 USD | 0.00 USD | 123.58 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 112,170.00 USD | 0.00 USD | 796.62 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 111,370.00 USD | 0.00 USD | 152.56 USD | `-4.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.06` | 111,220.00 USD | 0.00 USD | 2,730.00 USD | `-4.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 108,490.00 USD | 0.00 USD | 121.69 USD | `-4.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.09` | 108,370.00 USD | 0.00 USD | 5,230.00 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 103,140.00 USD | 0.00 USD | 477.36 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 102,660.00 USD | 0.00 USD | 924.78 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 101,740.00 USD | 0.00 USD | 744.88 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 100,990.00 USD | 0.00 USD | 6,500.00 USD | `-4.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 94,490.00 USD | 0.00 USD | 884.60 USD | `-3.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 93,600.00 USD | 0.00 USD | 5,550.00 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 88,050.00 USD | 0.00 USD | 1,540.00 USD | `-3.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 86,510.00 USD | 0.00 USD | 3,080.00 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 83,430.00 USD | 0.00 USD | 520.75 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 82,900.00 USD | 0.00 USD | 3,020.00 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 79,880.00 USD | 0.00 USD | 141.04 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 79,740.00 USD | 0.00 USD | 22,560.00 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 57,180.00 USD | 0.00 USD | 515.66 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.22` | 56,660.00 USD | 0.00 USD | 139.74 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 56,520.00 USD | 0.00 USD | 490.15 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.24` | 56,030.00 USD | 0.00 USD | 197.96 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.26` | 55,830.00 USD | 0.00 USD | 9,640.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.27` | 46,200.00 USD | 0.00 USD | 535.65 USD | `-2.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 45,660.00 USD | 0.00 USD | 734.99 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 44,920.00 USD | 0.00 USD | 828.50 USD | `-2.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 44,100.00 USD | 0.00 USD | 311.97 USD | `-2.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 43,780.00 USD | 0.00 USD | 5,380.00 USD | `-1.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 38,410.00 USD | 0.00 USD | 245.13 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.32` | 38,160.00 USD | 0.00 USD | 1,690.00 USD | `-1.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 36,470.00 USD | 0.00 USD | 408.58 USD | `-1.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 36,060.00 USD | 0.00 USD | 808.63 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 35,250.00 USD | 0.00 USD | 4,070.00 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.37` | 31,180.00 USD | 0.00 USD | 24,090.00 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 7,090.00 USD | 0.00 USD | 503.59 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 6,590.00 USD | 0.00 USD | 419.25 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 6,170.00 USD | 0.00 USD | 376.68 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 5,790.00 USD | 0.00 USD | 4,240.00 USD | `-0.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 1,560.00 USD | 0.00 USD | 314.81 USD | `-0.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 1,240.00 USD | 0.00 USD | 198.83 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 1,040.00 USD | 0.00 USD | 195.52 USD | `-0.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 849.06 USD | 0.00 USD | 138.24 USD | `-0.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 710.81 USD | 0.00 USD | 710.81 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.47` | 769.61 USD | 769.61 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.48` | 1,550.00 USD | 777.14 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.49` | 1,960.00 USD | 408.78 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 18,970.00 USD | 17,010.00 USD | 0.00 USD | `+0.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.52` | 19,370.00 USD | 408.55 USD | 0.00 USD | `+0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.53` | 21,540.00 USD | 2,160.00 USD | 0.00 USD | `+0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 23,710.00 USD | 2,170.00 USD | 0.00 USD | `+0.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 23,830.00 USD | 123.56 USD | 0.00 USD | `+0.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.55` | 33,820.00 USD | 9,990.00 USD | 0.00 USD | `+1.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.56` | 35,410.00 USD | 1,600.00 USD | 0.00 USD | `+1.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.57` | 35,980.00 USD | 566.55 USD | 0.00 USD | `+1.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.59` | 36,120.00 USD | 143.28 USD | 0.00 USD | `+1.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.60` | 36,250.00 USD | 124.28 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 36,350.00 USD | 102.14 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 36,480.00 USD | 124.57 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 36,600.00 USD | 128.51 USD | 0.00 USD | `+1.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 36,810.00 USD | 201.97 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 38,690.00 USD | 1,880.00 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 39,560.00 USD | 877.88 USD | 0.00 USD | `+2.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 39,760.00 USD | 200.85 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 39,940.00 USD | 176.62 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 40,930.00 USD | 990.09 USD | 0.00 USD | `+2.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 41,760.00 USD | 830.81 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 42,340.00 USD | 575.14 USD | 0.00 USD | `+2.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 42,740.00 USD | 399.67 USD | 0.00 USD | `+2.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 43,160.00 USD | 421.85 USD | 0.00 USD | `+3.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 43,400.00 USD | 239.51 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 47,770.00 USD | 4,370.00 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 51,510.00 USD | 3,740.00 USD | 0.00 USD | `+3.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 51,690.00 USD | 173.28 USD | 0.00 USD | `+3.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 51,900.00 USD | 215.16 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 52,290.00 USD | 388.12 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 53,000.00 USD | 711.78 USD | 0.00 USD | `+3.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 71,180.00 USD | 18,170.00 USD | 0.00 USD | `+3.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.82` | 73,210.00 USD | 2,030.00 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 73,450.00 USD | 243.40 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 73,620.00 USD | 168.05 USD | 0.00 USD | `+4.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 73,960.00 USD | 339.94 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 74,270.00 USD | 310.98 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 74,380.00 USD | 110.58 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 75,240.00 USD | 860.96 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 77,170.00 USD | 1,930.00 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 77,960.00 USD | 788.72 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 79,770.00 USD | 1,800.00 USD | 0.00 USD | `+5.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 79,930.00 USD | 163.33 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 80,710.00 USD | 782.17 USD | 0.00 USD | `+5.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 80,940.00 USD | 223.62 USD | 0.00 USD | `+5.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 618,240.00 USD | 537,310.00 USD | 0.00 USD | `+5.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 618,650.00 USD | 401.63 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 933,800.00 USD | 315,150.00 USD | 0.00 USD | `+5.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 934,140.00 USD | 338.30 USD | 0.00 USD | `+6.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 934,400.00 USD | 260.96 USD | 0.00 USD | `+6.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 935,770.00 USD | 1,380.00 USD | 0.00 USD | `+6.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 936,860.00 USD | 1,090.00 USD | 0.00 USD | `+6.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 937,480.00 USD | 616.37 USD | 0.00 USD | `+6.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 937,580.00 USD | 102.03 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 938,030.00 USD | 453.84 USD | 0.00 USD | `+6.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 938,200.00 USD | 160.99 USD | 0.00 USD | `+7.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 938,410.00 USD | 215.98 USD | 0.00 USD | `+7.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 939,920.00 USD | 1,510.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 940,370.00 USD | 451.48 USD | 0.00 USD | `+7.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 940,510.00 USD | 139.58 USD | 0.00 USD | `+7.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 941,800.00 USD | 1,290.00 USD | 0.00 USD | `+7.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 941,970.00 USD | 166.53 USD | 0.00 USD | `+7.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 943,970.00 USD | 2,000.00 USD | 0.00 USD | `+7.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 1,340,000.00 USD | 394,210.00 USD | 0.00 USD | `+8.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,340,000.00 USD | 119.24 USD | 0.00 USD | `+8.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,340,000.00 USD | 3,020.00 USD | 0.00 USD | `+8.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,340,000.00 USD | 131.87 USD | 0.00 USD | `+8.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,340,000.00 USD | 149.17 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,340,000.00 USD | 2,220.00 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,580,000.00 USD | 231,380.00 USD | 0.00 USD | `+9.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,580,000.00 USD | 1,960.00 USD | 0.00 USD | `+9.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,580,000.00 USD | 434.45 USD | 0.00 USD | `+9.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,600,000.00 USD | 18,610.00 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,600,000.00 USD | 166.83 USD | 0.00 USD | `+10.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,600,000.00 USD | 674.29 USD | 0.00 USD | `+10.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,600,000.00 USD | 101.58 USD | 0.00 USD | `+10.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,600,000.00 USD | 109.36 USD | 0.00 USD | `+10.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,600,000.00 USD | 116.69 USD | 0.00 USD | `+10.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,600,000.00 USD | 163.41 USD | 0.00 USD | `+10.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,600,000.00 USD | 102.01 USD | 0.00 USD | `+10.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,600,000.00 USD | 102.12 USD | 0.00 USD | `+10.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,600,000.00 USD | 714.59 USD | 0.00 USD | `+11.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,600,000.00 USD | 928.13 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,600,000.00 USD | 102.45 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,600,000.00 USD | 219.84 USD | 0.00 USD | `+11.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,600,000.00 USD | 311.69 USD | 0.00 USD | `+11.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,600,000.00 USD | 1,890.00 USD | 0.00 USD | `+11.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,600,000.00 USD | 1,130.00 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,600,000.00 USD | 288.46 USD | 0.00 USD | `+12.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,600,000.00 USD | 119.92 USD | 0.00 USD | `+12.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,600,000.00 USD | 231.00 USD | 0.00 USD | `+13.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,600,000.00 USD | 221.07 USD | 0.00 USD | `+13.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,600,000.00 USD | 992.00 USD | 0.00 USD | `+13.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,610,000.00 USD | 148.48 USD | 0.00 USD | `+13.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,610,000.00 USD | 191.36 USD | 0.00 USD | `+14.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,610,000.00 USD | 4,440.00 USD | 0.00 USD | `+14.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,610,000.00 USD | 108.21 USD | 0.00 USD | `+14.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,610,000.00 USD | 169.68 USD | 0.00 USD | `+14.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,610,000.00 USD | 574.66 USD | 0.00 USD | `+15.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,610,000.00 USD | 121.87 USD | 0.00 USD | `+15.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,610,000.00 USD | 115.88 USD | 0.00 USD | `+16.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,610,000.00 USD | 340.05 USD | 0.00 USD | `+16.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,610,000.00 USD | 742.12 USD | 0.00 USD | `+16.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,610,000.00 USD | 899.47 USD | 0.00 USD | `+16.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,680,000.00 USD | 70,020.00 USD | 0.00 USD | `+17.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,680,000.00 USD | 373.97 USD | 0.00 USD | `+17.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,690,000.00 USD | 5,050.00 USD | 0.00 USD | `+18.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,690,000.00 USD | 6,370.00 USD | 0.00 USD | `+18.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,690,000.00 USD | 404.20 USD | 0.00 USD | `+19.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,910,000.00 USD | 210,980.00 USD | 0.00 USD | `+19.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,910,000.00 USD | 1,150.00 USD | 0.00 USD | `+19.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,910,000.00 USD | 172.16 USD | 0.00 USD | `+20.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,910,000.00 USD | 922.87 USD | 0.00 USD | `+21.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,910,000.00 USD | 489.40 USD | 0.00 USD | `+21.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,910,000.00 USD | 1,200.00 USD | 0.00 USD | `+22.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,910,000.00 USD | 118.01 USD | 0.00 USD | `+23.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.46` | 1,910,000.00 USD | 971.48 USD | 0.00 USD | `+23.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.47` | 1,910,000.00 USD | 818.31 USD | 0.00 USD | `+23.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,910,000.00 USD | 312.31 USD | 0.00 USD | `+24.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,910,000.00 USD | 2,290.00 USD | 0.00 USD | `+24.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.53` | 1,920,000.00 USD | 1,890.00 USD | 0.00 USD | `+24.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,920,000.00 USD | 178.46 USD | 0.00 USD | `+25.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,920,000.00 USD | 173.42 USD | 0.00 USD | `+26.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,920,000.00 USD | 184.75 USD | 0.00 USD | `+26.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,920,000.00 USD | 135.78 USD | 0.00 USD | `+27.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,920,000.00 USD | 127.96 USD | 0.00 USD | `+27.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,920,000.00 USD | 476.43 USD | 0.00 USD | `+28.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,920,000.00 USD | 869.35 USD | 0.00 USD | `+28.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,950,000.00 USD | 35,110.00 USD | 0.00 USD | `+28.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,950,000.00 USD | 251.06 USD | 0.00 USD | `+29.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,950,000.00 USD | 552.44 USD | 0.00 USD | `+29.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,950,000.00 USD | 537.26 USD | 0.00 USD | `+29.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.11` | 1,960,000.00 USD | 1,110.00 USD | 0.00 USD | `+31.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,960,000.00 USD | 320.29 USD | 0.00 USD | `+31.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,960,000.00 USD | 1,100.00 USD | 0.00 USD | `+31.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,960,000.00 USD | 2,270.00 USD | 0.00 USD | `+32.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,960,000.00 USD | 1,270.00 USD | 0.00 USD | `+32.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,960,000.00 USD | 1,380.00 USD | 0.00 USD | `+34.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,960,000.00 USD | 2,410.00 USD | 0.00 USD | `+34.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,980,000.00 USD | 10,640.00 USD | 0.00 USD | `+35.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 1,980,000.00 USD | 2,050.00 USD | 0.00 USD | `+35.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,980,000.00 USD | 529.11 USD | 0.00 USD | `+35.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,990,000.00 USD | 7,700.00 USD | 0.00 USD | `+36.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,990,000.00 USD | 906.03 USD | 0.00 USD | `+39.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,990,000.00 USD | 434.61 USD | 0.00 USD | `+40.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,990,000.00 USD | 163.52 USD | 0.00 USD | `+40.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 2,000,000.00 USD | 10,370.00 USD | 0.00 USD | `+41.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.19` | 2,000,000.00 USD | 5,270.00 USD | 0.00 USD | `+43.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.28` | 2,000,000.00 USD | 115.02 USD | 0.00 USD | `+44.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 2,010,000.00 USD | 3,870.00 USD | 0.00 USD | `+50.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 2,010,000.00 USD | 197.97 USD | 0.00 USD | `+51.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 2,010,000.00 USD | 3,200.00 USD | 0.00 USD | `+52.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 2,010,000.00 USD | 179.58 USD | 0.00 USD | `+53.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 2,010,000.00 USD | 568.45 USD | 0.00 USD | `+53.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 2,010,000.00 USD | 169.57 USD | 0.00 USD | `+55.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 2,010,000.00 USD | 446.52 USD | 0.00 USD | `+57.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 2,020,000.00 USD | 5,320.00 USD | 0.00 USD | `+59.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,230,000.00 USD | 210,750.00 USD | 0.00 USD | `+59.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,230,000.00 USD | 407.95 USD | 0.00 USD | `+61.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,230,000.00 USD | 174.91 USD | 0.00 USD | `+63.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,230,000.00 USD | 4,680.00 USD | 0.00 USD | `+65.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,230,000.00 USD | 960.26 USD | 0.00 USD | `+67.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,240,000.00 USD | 2,710.00 USD | 0.00 USD | `+69.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,240,000.00 USD | 805.90 USD | 0.00 USD | `+71.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,240,000.00 USD | 655.55 USD | 0.00 USD | `+73.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,240,000.00 USD | 4,890.00 USD | 0.00 USD | `+74.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,240,000.00 USD | 471.09 USD | 0.00 USD | `+75.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,240,000.00 USD | 383.85 USD | 0.00 USD | `+76.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,900,000.00 USD | 653,420.00 USD | 0.00 USD | `+77.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 2,900,000.00 USD | 1,510.00 USD | 0.00 USD | `+77.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,900,000.00 USD | 111.87 USD | 0.00 USD | `+87.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,900,000.00 USD | 219.91 USD | 0.00 USD | `+89.01%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.14` | 6,480,000.00 USD | 0.00 USD | 6,480,000.00 USD | 45,760.00 USD | 20,580.00 USD | 41,320.00 USD |
| `7D` | `7.16` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 29,500.00 USD | 4,260.00 USD | 21,980.00 USD |
| `7D` | `7.18` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 5,030.00 USD | 3,780.00 USD | 19,650.00 USD |
| `7D` | `7.20` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 11,960.00 USD | 7,300.00 USD | 2,050.00 USD |
| `7D` | `7.22` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 12,260.00 USD | 6,540.00 USD | 6,980.00 USD |
| `7D` | `7.24` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 39,910.00 USD | 0.00 USD | 10,700.00 USD |
| `7D` | `7.26` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 0.00 USD | 1,810.00 USD | 58.08 USD |
| `7D` | `7.30` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 4,770.00 USD |
| `7D` | `7.32` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 5,740.00 USD |
| `7D` | `7.36` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 983.83 USD | 0.00 USD | 864.67 USD |
| `7D` | `7.38` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 46,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.40` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 44,790.00 USD | 0.00 USD | 503.12 USD |
| `7D` | `7.46` | 6,080,000.00 USD | 0.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD |
| `7D` | `7.48` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD |
| `7D` | `7.52` | 6,040,000.00 USD | 0.00 USD | 6,040,000.00 USD | 3,220.00 USD | 14,470.00 USD | 18,280.00 USD |
| `7D` | `7.54` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 34,840.00 USD | 4,450.00 USD | 0.00 USD |
| `7D` | `7.56` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD |
| `1D` | `7.60` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 2,760.00 USD | 4,900.00 USD | 4,570.00 USD |
| `7D` | `7.60` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 301.55 USD |
| `1D` | `7.61` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 3,160.00 USD | 1,250.00 USD | 11,670.00 USD |
| `1D` | `7.62` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 5,860.00 USD | 1,330.00 USD | 133.28 USD |
| `7D` | `7.62` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 626.55 USD | 2,130.00 USD | 996.08 USD |
| `1D` | `7.63` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 6,700.00 USD | 0.00 USD | 9,660.00 USD |
| `1D` | `7.64` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 29,090.00 USD | 812.96 USD | 2,390.00 USD |
| `7D` | `7.64` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 41,300.00 USD | 0.00 USD | 686.63 USD |
| `1D` | `7.65` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 3,840.00 USD | 817.75 USD | 9,870.00 USD |
| `1D` | `7.66` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 531.95 USD |
| `7D` | `7.66` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 4,870.00 USD | 2,350.00 USD | 24,600.00 USD |
| `1D` | `7.67` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 687.87 USD | 587.20 USD | 114.38 USD |
| `1D` | `7.68` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 2,670.00 USD | 0.00 USD | 3,830.00 USD |
| `7D` | `7.68` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD |
| `1D` | `7.69` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 485.15 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `7.70` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 4,840.00 USD | 2,390.00 USD | 16,770.00 USD |
| `7D` | `7.70` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 393.33 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.71` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 1,050.00 USD | 5,040.00 USD | 7,390.00 USD |
| `1D` | `7.72` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 1,310.00 USD | 568.00 USD | 2,430.00 USD |
| `7D` | `7.72` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 38,970.00 USD | 0.00 USD | 40,470.00 USD |
| `1D` | `7.73` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 472.98 USD | 1,240.00 USD | 5,600.00 USD |
| `1D` | `7.74` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 16,520.00 USD | 0.00 USD | 184.39 USD |
| `7D` | `7.74` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 30,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.75` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 252.25 USD | 6,210.00 USD | 8,050.00 USD |
| `1D` | `7.76` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 329.46 USD | 494.12 USD | 0.00 USD |
| `7D` | `7.76` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 812.95 USD | 13,360.00 USD | 11,180.00 USD |
| `1D` | `7.77` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 13,620.00 USD | 689.91 USD | 3,430.00 USD |
| `1D` | `7.78` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 430.17 USD | 6,250.00 USD | 0.00 USD |
| `7D` | `7.78` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 46,570.00 USD | 7,520.00 USD | 28,810.00 USD |
| `1D` | `7.79` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 24,880.00 USD | 2,920.00 USD | 7,250.00 USD |
| `1D` | `7.80` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 2,950.00 USD | 7,910.00 USD | 709.61 USD |
| `7D` | `7.80` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 46,450.00 USD | 12,980.00 USD | 1,770.00 USD |
| `1D` | `7.81` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 882.10 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.82` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 2,170.00 USD | 1,680.00 USD | 0.00 USD |
| `7D` | `7.82` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,710.00 USD |
| `1D` | `7.83` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 25,990.00 USD | 6,330.00 USD | 0.00 USD |
| `1D` | `7.84` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 328.00 USD | 1,800.00 USD | 10.76 USD |
| `7D` | `7.84` | 5,560,000.00 USD | 0.00 USD | 5,560,000.00 USD | 32,340.00 USD | 2,380.00 USD | 25,450.00 USD |
| `1D` | `7.85` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 5,110.00 USD | 1,250.00 USD | 2,650.00 USD |
| `1D` | `7.86` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 345.80 USD | 6,690.00 USD | 17,220.00 USD |
| `7D` | `7.86` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 137,360.00 USD | 5,460.00 USD | 18,470.00 USD |
| `1D` | `7.87` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 12,370.00 USD | 10,860.00 USD | 22,910.00 USD |
| `1D` | `7.88` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 159,870.00 USD | 5,030.00 USD | 33,710.00 USD |
| `7D` | `7.88` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 170,100.00 USD | 12,780.00 USD | 30,610.00 USD |
| `1D` | `7.89` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 59,440.00 USD | 3,720.00 USD | 27,230.00 USD |
| `1D` | `7.90` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 56,650.00 USD | 6,970.00 USD | 5,990.00 USD |
| `7D` | `7.90` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 34,620.00 USD | 12,890.00 USD | 18,230.00 USD |
| `1D` | `7.91` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 10,790.00 USD | 10,370.00 USD | 28,300.00 USD |
| `1D` | `7.92` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 12,800.00 USD | 2,950.00 USD | 8,770.00 USD |
| `7D` | `7.92` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 55,490.00 USD | 23,630.00 USD | 41,800.00 USD |
| `1D` | `7.93` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 11,170.00 USD | 6,570.00 USD | 4,480.00 USD |
| `1D` | `7.94` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 20,380.00 USD | 20,510.00 USD | 61,750.00 USD |
| `7D` | `7.94` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,670.00 USD |
| `1D` | `7.95` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 28,070.00 USD | 9,190.00 USD | 86,980.00 USD |
| `1D` | `7.96` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 3,830.00 USD | 15,680.00 USD | 62,330.00 USD |
| `7D` | `7.96` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 21,840.00 USD | 6,920.00 USD | 87,430.00 USD |
| `1D` | `7.97` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 10,880.00 USD | 9,820.00 USD | 4,040.00 USD |
| `1D` | `7.98` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 4,290.00 USD | 2,060.00 USD | 42,970.00 USD |
| `7D` | `7.98` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 59,410.00 USD | 26,790.00 USD | 146,450.00 USD |
| `1D` | `7.99` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 3,640.00 USD | 10,180.00 USD | 4,660.00 USD |
| `1D` | `8.00` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 50,890.00 USD | 8,950.00 USD | 21,810.00 USD |
| `7D` | `8.00` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 60,980.00 USD | 16,420.00 USD | 5,130.00 USD |
| `1D` | `8.01` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 6,080.00 USD | 3,750.00 USD | 4,040.00 USD |
| `1D` | `8.02` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 75,000.00 USD | 0.00 USD | 274.70 USD |
| `7D` | `8.02` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 15,300.00 USD | 46,670.00 USD | 58,100.00 USD |
| `1D` | `8.03` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 11,150.00 USD | 12,540.00 USD | 12,890.00 USD |
| `1D` | `8.04` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 49,150.00 USD | 0.00 USD | 10,010.00 USD |
| `7D` | `8.04` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 462,240.00 USD | 0.00 USD | 86,550.00 USD |
| `1D` | `8.05` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 318,310.00 USD | 6,430.00 USD | 53,960.00 USD |
| `1D` | `8.06` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 155,740.00 USD | 0.00 USD | 66,970.00 USD |
| `7D` | `8.06` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 336,530.00 USD | 0.00 USD | 86,670.00 USD |
| `1D` | `8.07` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 129,880.00 USD | 9,310.00 USD | 4,540.00 USD |
| `1D` | `8.08` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD |
| `7D` | `8.08` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 5,100.00 USD | 0.00 USD | 73,960.00 USD |
| `1D` | `8.09` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 3,110.00 USD | 0.00 USD | 29,580.00 USD |
| `1D` | `8.10` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD |
| `7D` | `8.10` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 56,590.00 USD | 0.00 USD | 14,820.00 USD |
| `1D` | `8.11` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD |
| `1D` | `8.12` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 20,210.00 USD | 11,230.00 USD | 126,250.00 USD |
| `7D` | `8.12` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 23,240.00 USD | 0.00 USD | 141,990.00 USD |
| `1D` | `8.13` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 29,110.00 USD | 9,180.00 USD | 1,710.00 USD |
| `1D` | `8.14` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 17,740.00 USD | 8,630.00 USD | 105,260.00 USD |
| `7D` | `8.14` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 180,540.00 USD | 30,700.00 USD | 183,790.00 USD |
| `1D` | `8.15` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 43,730.00 USD | 12,240.00 USD | 53,660.00 USD |
| `1D` | `8.16` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 364.84 USD | 21,000.00 USD | 165,460.00 USD |
| `7D` | `8.16` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 30,670.00 USD | 23,640.00 USD | 14,310.00 USD |
| `1D` | `8.17` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 11,690.00 USD | 8,610.00 USD | 183,140.00 USD |
| `1D` | `8.18` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 7,250.00 USD | 1,470.00 USD | 0.00 USD |
| `7D` | `8.18` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 1,200.00 USD | 40,090.00 USD | 172,780.00 USD |
| `1D` | `8.19` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 19,780.00 USD | 0.00 USD | 15,460.00 USD |
| `1D` | `8.20` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 25,530.00 USD | 4,000.00 USD | 11,560.00 USD |
| `7D` | `8.20` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 174,220.00 USD | 58,100.00 USD | 0.00 USD |
| `1D` | `8.21` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 41,990.00 USD | 1,260.00 USD | 0.00 USD |
| `1D` | `8.22` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 16,310.00 USD |
| `7D` | `8.22` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD |
| `1D` | `8.23` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 1,750.00 USD | 2,380.00 USD |
| `1D` | `8.24` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 3,220.00 USD | 5,970.00 USD |
| `7D` | `8.24` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 106,990.00 USD | 18,690.00 USD | 17,610.00 USD |
| `1D` | `8.25` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 168.44 USD | 5,000.00 USD | 38,170.00 USD |
| `1D` | `8.26` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 50,590.00 USD | 12,510.00 USD | 23,300.00 USD |
| `7D` | `8.26` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 100,930.00 USD | 5,750.00 USD | 11,420.00 USD |
| `1D` | `8.27` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 14,470.00 USD | 12,270.00 USD | 20,140.00 USD |
| `1D` | `8.28` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 0.00 USD | 13,760.00 USD | 4,240.00 USD |
| `7D` | `8.28` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 91,120.00 USD | 4,000.00 USD | 27,800.00 USD |
| `1D` | `8.29` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 39,670.00 USD | 11,800.00 USD | 0.00 USD |
| `1D` | `8.30` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 58,950.00 USD | 13,810.00 USD | 20,060.00 USD |
| `7D` | `8.30` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 264,780.00 USD | 17,210.00 USD | 21,020.00 USD |
| `1D` | `8.31` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 83,770.00 USD | 11,920.00 USD | 56,400.00 USD |
| `1D` | `8.32` | 905,060.00 USD | 0.00 USD | 905,060.00 USD | 73,050.00 USD | 6,080.00 USD | 14,060.00 USD |
| `7D` | `8.32` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 220,640.00 USD | 0.00 USD | 5,060.00 USD |
| `1D` | `8.33` | 811,860.00 USD | 0.00 USD | 811,860.00 USD | 0.00 USD | 6,210.00 USD | 109.14 USD |
| `1D` | `8.34` | 805,550.00 USD | 0.00 USD | 805,550.00 USD | 0.00 USD | 2,210.00 USD | 13.84 USD |
| `7D` | `8.34` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 11,770.00 USD | 4,430.00 USD |
| `1D` | `8.35` | 803,320.00 USD | 0.00 USD | 803,320.00 USD | 0.00 USD | 19,810.00 USD | 16,970.00 USD |
| `1D` | `8.36` | 766,540.00 USD | 0.00 USD | 766,540.00 USD | 0.00 USD | 0.00 USD | 17,800.00 USD |
| `7D` | `8.36` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 223,170.00 USD | 0.00 USD | 17,870.00 USD |
| `1D` | `8.37` | 748,740.00 USD | 0.00 USD | 748,740.00 USD | 0.00 USD | 14,420.00 USD | 16.86 USD |
| `1D` | `8.38` | 734,300.00 USD | 0.00 USD | 734,300.00 USD | 17,220.00 USD | 5,940.00 USD | 50,290.00 USD |
| `7D` | `8.38` | 904,500.00 USD | 0.00 USD | 904,500.00 USD | 0.00 USD | 0.00 USD | 57,740.00 USD |
| `1D` | `8.39` | 660,860.00 USD | 0.00 USD | 660,860.00 USD | 100,740.00 USD | 13,620.00 USD | 32,610.00 USD |
| `1D` | `8.40` | 513,890.00 USD | 0.00 USD | 513,890.00 USD | 10,500.00 USD | 7,000.00 USD | 56,580.00 USD |
| `7D` | `8.40` | 846,760.00 USD | 0.00 USD | 846,760.00 USD | 0.00 USD | 7,600.00 USD | 86,940.00 USD |
| `1D` | `8.41` | 439,800.00 USD | 0.00 USD | 439,800.00 USD | 916.10 USD | 6,440.00 USD | 11,940.00 USD |
| `1D` | `8.42` | 420,500.00 USD | 0.00 USD | 420,500.00 USD | 0.00 USD | 16,260.00 USD | 42,890.00 USD |
| `7D` | `8.42` | 752,220.00 USD | 0.00 USD | 752,220.00 USD | 209,760.00 USD | 0.00 USD | 35,220.00 USD |
| `1D` | `8.43` | 361,350.00 USD | 0.00 USD | 361,350.00 USD | 81,350.00 USD | 7,730.00 USD | 7,540.00 USD |
| `1D` | `8.44` | 264,730.00 USD | 0.00 USD | 264,730.00 USD | 10,010.00 USD | 32,380.00 USD | 160,460.00 USD |
| `7D` | `8.44` | 507,240.00 USD | 0.00 USD | 507,240.00 USD | 152,190.00 USD | 8,000.00 USD | 74,660.00 USD |
| `1D` | `8.45` | 61,880.00 USD | 0.00 USD | 61,880.00 USD | 55,910.00 USD | 5,970.00 USD | 0.00 USD |
| `1D` | `8.46` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.46` | 272,390.00 USD | 0.00 USD | 272,390.00 USD | 152,650.00 USD | 0.00 USD | 119,740.00 USD |
| `1D` | `8.47` | 769.90 USD | 769.90 USD | 0.00 USD | 769.90 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.47` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.48` | 3,000.00 USD | 3,000.00 USD | 0.00 USD | 2,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.48` | 191,210.00 USD | 191,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 191,210.00 USD |
| `1D` | `8.49` | 3,300.00 USD | 3,300.00 USD | 0.00 USD | 282.10 USD | 0.00 USD | 12.70 USD |
| `1D` | `8.50` | 3,570.00 USD | 3,570.00 USD | 0.00 USD | 272.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.50` | 192,390.00 USD | 192,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD |
| `1D` | `8.51` | 176,010.00 USD | 176,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 172,440.00 USD |
| `1D` | `8.52` | 339,850.00 USD | 339,850.00 USD | 0.00 USD | 159,040.00 USD | 0.00 USD | 4,800.00 USD |
| `7D` | `8.52` | 398,210.00 USD | 398,210.00 USD | 0.00 USD | 113,820.00 USD | 0.00 USD | 92,000.00 USD |
| `1D` | `8.53` | 364,030.00 USD | 364,030.00 USD | 0.00 USD | 24,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.54` | 567,560.00 USD | 567,560.00 USD | 0.00 USD | 203,370.00 USD | 0.00 USD | 156.94 USD |
| `7D` | `8.54` | 757,830.00 USD | 757,830.00 USD | 0.00 USD | 357,740.00 USD | 0.00 USD | 1,880.00 USD |
| `1D` | `8.55` | 593,370.00 USD | 593,370.00 USD | 0.00 USD | 686.73 USD | 0.00 USD | 25,120.00 USD |
| `1D` | `8.56` | 632,240.00 USD | 632,240.00 USD | 0.00 USD | 555.70 USD | 38,320.00 USD | 0.00 USD |
| `7D` | `8.56` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 144,180.00 USD | 122,650.00 USD | 790.79 USD |
| `1D` | `8.57` | 782,090.00 USD | 782,090.00 USD | 0.00 USD | 149,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.58` | 840,360.00 USD | 840,360.00 USD | 0.00 USD | 58,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.58` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 4,370.00 USD | 164,810.00 USD | 0.00 USD |
| `1D` | `8.59` | 843,470.00 USD | 843,470.00 USD | 0.00 USD | 3,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.60` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `1D` | `8.61` | 847,790.00 USD | 847,790.00 USD | 0.00 USD | 3,630.00 USD | 0.00 USD | 699.64 USD |
| `1D` | `8.62` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 38,440.00 USD | 0.00 USD | 125,290.00 USD |
| `7D` | `8.62` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 28,520.00 USD |
| `1D` | `8.63` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 129,560.00 USD | 2,420.00 USD | 0.00 USD |
| `1D` | `8.64` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 59,700.00 USD | 9,340.00 USD | 3,410.00 USD |
| `7D` | `8.64` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 40,260.00 USD | 10,660.00 USD | 0.00 USD |
| `1D` | `8.65` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 36,130.00 USD | 9,010.00 USD | 17,260.00 USD |
| `1D` | `8.66` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 6,230.00 USD | 2,020.00 USD | 14,040.00 USD |
| `7D` | `8.66` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 416.16 USD |
| `1D` | `8.67` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 2,210.00 USD | 9,960.00 USD | 56.72 USD |
| `1D` | `8.68` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 12,020.00 USD | 25,890.00 USD |
| `7D` | `8.68` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 30,000.00 USD | 117,540.00 USD |
| `1D` | `8.69` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 9,290.00 USD | 19,200.00 USD | 33,840.00 USD |
| `1D` | `8.70` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 60,200.00 USD | 0.00 USD | 23,500.00 USD |
| `7D` | `8.70` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 116,370.00 USD | 41,840.00 USD | 46,400.00 USD |
| `1D` | `8.71` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 18,250.00 USD | 7,990.00 USD | 0.00 USD |
| `1D` | `8.72` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 34,050.00 USD | 2,520.00 USD | 50,790.00 USD |
| `7D` | `8.72` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 609.73 USD |
| `1D` | `8.73` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 14,030.00 USD | 28,810.00 USD | 32,610.00 USD |
| `1D` | `8.74` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 37,210.00 USD | 3,500.00 USD | 17,580.00 USD |
| `7D` | `8.74` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 51,030.00 USD | 30,470.00 USD | 686.63 USD |
| `1D` | `8.75` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 34,030.00 USD | 8,970.00 USD | 16,930.00 USD |
| `1D` | `8.76` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 78,530.00 USD | 10,010.00 USD | 57,030.00 USD |
| `7D` | `8.76` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 196,960.00 USD | 0.00 USD | 58,950.00 USD |
| `1D` | `8.77` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 159,000.00 USD | 2,060.00 USD | 43,030.00 USD |
| `1D` | `8.78` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 45,370.00 USD | 25,510.00 USD | 50,110.00 USD |
| `7D` | `8.78` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 144,010.00 USD | 8,000.00 USD | 133,500.00 USD |
| `1D` | `8.79` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 32,530.00 USD | 17,970.00 USD | 31,130.00 USD |
| `1D` | `8.80` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 114,070.00 USD | 19,150.00 USD | 23,840.00 USD |
| `7D` | `8.80` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 27,360.00 USD | 33,750.00 USD | 32,140.00 USD |
| `1D` | `8.81` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 46,510.00 USD | 9,030.00 USD | 1,750.00 USD |
| `1D` | `8.82` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 18,070.00 USD | 4,510.00 USD | 61,490.00 USD |
| `7D` | `8.82` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 365,470.00 USD | 18,440.00 USD | 39,280.00 USD |
| `1D` | `8.83` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 172,310.00 USD | 19,400.00 USD | 7,020.00 USD |
| `1D` | `8.84` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 461.30 USD | 3,110.00 USD | 59,130.00 USD |
| `7D` | `8.84` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 5,880.00 USD | 0.00 USD |
| `1D` | `8.85` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 11,710.00 USD | 3,360.00 USD | 11,200.00 USD |
| `1D` | `8.86` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 4,400.00 USD | 1,470.00 USD | 607.55 USD |
| `7D` | `8.86` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 29,310.00 USD | 0.00 USD | 83,000.00 USD |
| `1D` | `8.87` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD | 8,900.00 USD |
| `1D` | `8.88` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 450.96 USD | 14,670.00 USD | 186.36 USD |
| `7D` | `8.88` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD | 28,570.00 USD |
| `1D` | `8.89` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 11,710.00 USD | 3,410.00 USD | 32,950.00 USD |
| `1D` | `8.90` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 26,130.00 USD | 5,990.00 USD | 81,550.00 USD |
| `7D` | `8.90` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 2,440.00 USD | 0.00 USD | 116,250.00 USD |
| `1D` | `8.91` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 32,000.00 USD | 11,620.00 USD | 15,860.00 USD |
| `1D` | `8.92` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 2,950.00 USD | 3,220.00 USD | 6,040.00 USD |
| `7D` | `8.92` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 99,150.00 USD | 0.00 USD | 35,230.00 USD |
| `1D` | `8.93` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 32,090.00 USD | 6,810.00 USD | 38,940.00 USD |
| `1D` | `8.94` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 51,500.00 USD | 12,260.00 USD | 3,770.00 USD |
| `7D` | `8.94` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 129,180.00 USD | 0.00 USD | 11,850.00 USD |
| `1D` | `8.95` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 439.30 USD | 6,630.00 USD | 20,340.00 USD |
| `1D` | `8.96` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 532.00 USD | 2,980.00 USD | 175.90 USD |
| `7D` | `8.96` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 3,320.00 USD | 4,000.00 USD | 26,700.00 USD |
| `1D` | `8.97` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 978.04 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.98` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 37,560.00 USD | 9,420.00 USD | 19,670.00 USD |
| `7D` | `8.98` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 1,180.00 USD | 0.00 USD | 9,090.00 USD |
| `1D` | `8.99` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 48,460.00 USD | 22,110.00 USD | 3,420.00 USD |
| `1D` | `9.00` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 37,680.00 USD | 0.00 USD | 24,740.00 USD |
| `7D` | `9.00` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 370,780.00 USD | 17,920.00 USD | 41,010.00 USD |
| `1D` | `9.01` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 50,570.00 USD | 14,940.00 USD | 16,240.00 USD |
| `1D` | `9.02` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 40,370.00 USD | 29,440.00 USD | 5,010.00 USD |
| `7D` | `9.02` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 82,280.00 USD | 56,120.00 USD | 1,780.00 USD |
| `1D` | `9.03` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 124,130.00 USD | 10,300.00 USD | 34,410.00 USD |
| `1D` | `9.04` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 41,880.00 USD | 5,900.00 USD | 14,800.00 USD |
| `7D` | `9.04` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 137,460.00 USD | 74,750.00 USD | 16,220.00 USD |
| `1D` | `9.05` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 21,080.00 USD | 9,980.00 USD | 24,060.00 USD |
| `1D` | `9.06` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 26,230.00 USD | 6,890.00 USD | 10,490.00 USD |
| `7D` | `9.06` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD |
| `1D` | `9.07` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 14,180.00 USD | 17,440.00 USD | 25,460.00 USD |
| `1D` | `9.08` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 12,960.00 USD | 2,110.00 USD | 32,470.00 USD |
| `7D` | `9.08` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD |
| `1D` | `9.09` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 73,020.00 USD | 9,730.00 USD | 25,300.00 USD |
| `1D` | `9.10` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 16,130.00 USD | 12,520.00 USD | 34,160.00 USD |
| `7D` | `9.10` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 826,500.00 USD | 35,760.00 USD | 334,610.00 USD |
| `1D` | `9.11` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 60,270.00 USD | 14,420.00 USD | 82,390.00 USD |
| `1D` | `9.12` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 102,270.00 USD | 22,410.00 USD | 26,360.00 USD |
| `7D` | `9.12` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 466,670.00 USD | 24,170.00 USD | 503,360.00 USD |
| `1D` | `9.13` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 75,050.00 USD | 15,960.00 USD | 40,180.00 USD |
| `1D` | `9.14` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 29,800.00 USD | 3,380.00 USD | 29,600.00 USD |
| `7D` | `9.14` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 536,560.00 USD | 18,540.00 USD | 500,290.00 USD |
| `1D` | `9.15` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 57,220.00 USD | 23,170.00 USD | 23,060.00 USD |
| `1D` | `9.16` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 64,660.00 USD | 23,900.00 USD | 32,470.00 USD |
| `7D` | `9.16` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 358,370.00 USD | 44,360.00 USD | 196,240.00 USD |
| `1D` | `9.17` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 79,780.00 USD | 3,200.00 USD | 49,540.00 USD |
| `1D` | `9.18` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 28,670.00 USD | 26,430.00 USD | 31,220.00 USD |
| `7D` | `9.18` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 566,340.00 USD | 162,460.00 USD | 292,040.00 USD |
| `1D` | `9.19` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 77,860.00 USD | 29,140.00 USD | 7,680.00 USD |
| `1D` | `9.20` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 66,540.00 USD | 11,090.00 USD | 37,460.00 USD |
| `7D` | `9.20` | 10,100,000.00 USD | 10,100,000.00 USD | 0.00 USD | 550,150.00 USD | 134,550.00 USD | 238,840.00 USD |
| `1D` | `9.21` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 29,910.00 USD | 2,950.00 USD | 4,760.00 USD |
| `1D` | `9.22` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 58,820.00 USD | 2,850.00 USD | 11,100.00 USD |
| `7D` | `9.22` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 620,010.00 USD | 144,840.00 USD | 376,830.00 USD |
| `1D` | `9.23` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 427.70 USD | 4,270.00 USD | 17.80 USD |
| `1D` | `9.24` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 45,120.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `9.24` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 336,360.00 USD | 44,660.00 USD | 136,520.00 USD |
| `1D` | `9.25` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 17,750.00 USD | 5,840.00 USD | 9,510.00 USD |
| `1D` | `9.26` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 539.67 USD | 0.00 USD | 3,540.00 USD |
| `7D` | `9.26` | 12,150,000.00 USD | 12,150,000.00 USD | 0.00 USD | 273,920.00 USD | 96,980.00 USD | 19,160.00 USD |
| `1D` | `9.27` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 22,500.00 USD | 1,360.00 USD | 6,640.00 USD |
| `1D` | `9.28` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 2,210.00 USD | 8,760.00 USD | 169.17 USD |
| `7D` | `9.28` | 12,710,000.00 USD | 12,710,000.00 USD | 0.00 USD | 352,980.00 USD | 69,460.00 USD | 136,920.00 USD |
| `1D` | `9.29` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 16,190.00 USD | 4,140.00 USD | 17,930.00 USD |
| `1D` | `9.30` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 40,750.00 USD | 7,520.00 USD | 11,600.00 USD |
| `7D` | `9.30` | 13,240,000.00 USD | 13,240,000.00 USD | 0.00 USD | 199,810.00 USD | 97,780.00 USD | 233,360.00 USD |
| `1D` | `9.31` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 28,720.00 USD | 5,500.00 USD | 12,920.00 USD |
| `1D` | `9.32` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 15,740.00 USD | 1,330.00 USD | 5,070.00 USD |
| `7D` | `9.32` | 13,840,000.00 USD | 13,840,000.00 USD | 0.00 USD | 242,590.00 USD | 51,970.00 USD | 309,560.00 USD |
| `1D` | `9.33` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 11,780.00 USD | 6,000.00 USD | 9,780.00 USD |
| `1D` | `9.34` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 44,670.00 USD | 3,660.00 USD | 5,580.00 USD |
| `7D` | `9.34` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 98,640.00 USD | 41,250.00 USD | 59,540.00 USD |
| `1D` | `9.35` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 14,420.00 USD | 817.75 USD | 14,910.00 USD |
| `1D` | `9.36` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 5,440.00 USD | 6,760.00 USD | 8,030.00 USD |
| `7D` | `9.36` | 14,420,000.00 USD | 14,420,000.00 USD | 0.00 USD | 215,620.00 USD | 64,120.00 USD | 97,710.00 USD |
| `1D` | `9.37` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 10,930.00 USD | 6,260.00 USD | 2,610.00 USD |
| `1D` | `9.38` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 14,740.00 USD | 0.00 USD | 13,750.00 USD |
| `7D` | `9.38` | 14,750,000.00 USD | 14,750,000.00 USD | 0.00 USD | 224,850.00 USD | 31,100.00 USD | 77,300.00 USD |
| `7D` | `9.40` | 15,130,000.00 USD | 15,130,000.00 USD | 0.00 USD | 234,760.00 USD | 42,520.00 USD | 105,030.00 USD |
| `7D` | `9.42` | 15,310,000.00 USD | 15,310,000.00 USD | 0.00 USD | 109,230.00 USD | 13,910.00 USD | 51,440.00 USD |
| `7D` | `9.44` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 80,230.00 USD | 19,420.00 USD | 43,220.00 USD |
| `7D` | `9.46` | 15,510,000.00 USD | 15,510,000.00 USD | 0.00 USD | 51,570.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `9.48` | 15,550,000.00 USD | 15,550,000.00 USD | 0.00 USD | 10,620.00 USD | 11,060.00 USD | 20,880.00 USD |
| `7D` | `9.50` | 15,680,000.00 USD | 15,680,000.00 USD | 0.00 USD | 65,230.00 USD | 12,050.00 USD | 52,470.00 USD |
| `7D` | `9.52` | 15,790,000.00 USD | 15,790,000.00 USD | 0.00 USD | 57,650.00 USD | 18,520.00 USD | 31,860.00 USD |
| `7D` | `9.54` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 11,650.00 USD | 13,310.00 USD | 930.52 USD |
| `7D` | `9.56` | 15,830,000.00 USD | 15,830,000.00 USD | 0.00 USD | 7,430.00 USD | 5,260.00 USD | 4,800.00 USD |
| `7D` | `9.58` | 15,890,000.00 USD | 15,890,000.00 USD | 0.00 USD | 35,340.00 USD | 2,380.00 USD | 26,910.00 USD |
| `7D` | `9.60` | 15,950,000.00 USD | 15,950,000.00 USD | 0.00 USD | 31,720.00 USD | 5,460.00 USD | 18,390.00 USD |
| `7D` | `9.62` | 15,990,000.00 USD | 15,990,000.00 USD | 0.00 USD | 26,870.00 USD | 1,540.00 USD | 9,730.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `352.66M` | Total OI Tokens: `41,596,530.4 AVAX`
  * 1h OI Change: `+0.01%` | 4h OI Change: `-0.88%` | 24h OI Change: `-6.96%`
  * Exchange Breakdown: Binance=`80.10M` | Bybit=`57.18M` | OKX=`11.48M` | Hyperliquid=`16.74M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.73K` | Last 24h: `16.67K` | Last 3d: `66.43K` | Last 7d: `105.12K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0099%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0093%` | **USDT Bitget** | `0.0053%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `51.02%` | `48.98%` | `1.04` | 5,060,000.00 USD |
| `15M` | `Binance` | `48.38%` | `51.62%` | `0.94` | 1,190,000.00 USD |
| `15M` | `OKX` | `67.91%` | `32.09%` | `2.12` | 234,340.00 USD |
| `15M` | `Bybit` | `47.98%` | `52.02%` | `0.92` | 179,480.00 USD |
| `15M` | `KuCoin` | `78.3%` | `21.7%` | `3.61` | 38,660.00 USD |
| `15M` | `Gate` | `16.35%` | `83.65%` | `0.20` | 171,200.00 USD |
| `15M` | `Bitget` | `46.65%` | `53.35%` | `0.87` | 68,340.00 USD |
| `15M` | `BingX` | `62.42%` | `37.58%` | `1.66` | 131,850.00 USD |
| `15M` | `MEXC` | `54.93%` | `45.07%` | `1.22` | 1,320,000.00 USD |
| `15M` | `Bitunix` | `57.72%` | `42.28%` | `1.37` | 872,300.00 USD |
| `15M` | `Hyperliquid` | `8.1%` | `91.9%` | `0.09` | 126,310.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.99%` | `50.01%` | `1.00` | 432,930.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `39.7%` | `60.3%` | `0.66` | 209,730.00 USD |
| `15M` | `HTX` | `36.55%` | `63.45%` | `0.58` | 781.68 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `58.79%` | `41.21%` | `1.43` | 78,520.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 116.15 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `59.56%` | `40.44%` | `1.47` | 5,780.00 USD |
| `15M` | `Whale Positions` | `48.38%` | `51.62%` | `0.94` | 1,190,000.00 USD |
| `15M` | `Global Accounts` | `51.02%` | `48.98%` | `1.04` | 5,060,000.00 USD |
| `1H` | `AVAX` | `47.62%` | `52.38%` | `0.91` | 28,760,000.00 USD |
| `1H` | `Binance` | `46.38%` | `53.62%` | `0.86` | 9,530,000.00 USD |
| `1H` | `OKX` | `42.74%` | `57.26%` | `0.75` | 4,890,000.00 USD |
| `1H` | `Bybit` | `44.05%` | `55.95%` | `0.79` | 6,130,000.00 USD |
| `1H` | `KuCoin` | `49.91%` | `50.09%` | `1.00` | 764,250.00 USD |
| `1H` | `Gate` | `47.23%` | `52.77%` | `0.90` | 1,690,000.00 USD |
| `1H` | `Bitget` | `31.92%` | `68.08%` | `0.47` | 885,060.00 USD |
| `1H` | `BingX` | `46.83%` | `53.17%` | `0.88` | 1,030,000.00 USD |
| `1H` | `MEXC` | `51.67%` | `48.33%` | `1.07` | 220,140.00 USD |
| `1H` | `Bitunix` | `60.25%` | `39.75%` | `1.52` | 370,900.00 USD |
| `1H` | `Hyperliquid` | `26.18%` | `73.82%` | `0.35` | 1,810,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.34%` | `50.66%` | `0.97` | 263,560.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `27.32%` | `72.68%` | `0.38` | 373,700.00 USD |
| `1H` | `HTX` | `68.53%` | `31.47%` | `2.18` | 70,570.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `49.02%` | `50.98%` | `0.96` | 323,600.00 USD |
| `1H` | `Aster` | `29.09%` | `70.91%` | `0.41` | 41,960.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `58.61%` | `41.39%` | `1.42` | 351,700.00 USD |
| `1H` | `Whale Positions` | `46.38%` | `53.62%` | `0.86` | 9,530,000.00 USD |
| `1H` | `Global Accounts` | `47.62%` | `52.38%` | `0.91` | 28,760,000.00 USD |
| `4H` | `AVAX` | `50.23%` | `49.77%` | `1.01` | 163,560,000.00 USD |
| `4H` | `Binance` | `48.84%` | `51.16%` | `0.95` | 77,030,000.00 USD |
| `4H` | `OKX` | `48.55%` | `51.45%` | `0.94` | 19,870,000.00 USD |
| `4H` | `Bybit` | `55.59%` | `44.41%` | `1.25` | 23,460,000.00 USD |
| `4H` | `KuCoin` | `50.63%` | `49.37%` | `1.03` | 3,070,000.00 USD |
| `4H` | `Gate` | `43.2%` | `56.8%` | `0.76` | 5,850,000.00 USD |
| `4H` | `Bitget` | `54.65%` | `45.35%` | `1.21` | 4,960,000.00 USD |
| `4H` | `BingX` | `25.5%` | `74.5%` | `0.34` | 2,730,000.00 USD |
| `4H` | `MEXC` | `49.19%` | `50.81%` | `0.97` | 1,920,000.00 USD |
| `4H` | `Bitunix` | `51.37%` | `48.63%` | `1.06` | 2,960,000.00 USD |
| `4H` | `Hyperliquid` | `56.01%` | `43.99%` | `1.27` | 14,480,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.3%` | `49.7%` | `1.01` | 2,750,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `54.99%` | `45.01%` | `1.22` | 1,090,000.00 USD |
| `4H` | `HTX` | `52.89%` | `47.11%` | `1.12` | 583,810.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `75.84%` | `24.16%` | `3.14` | 592,840.00 USD |
| `4H` | `Aster` | `40.2%` | `59.8%` | `0.67` | 1,080,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.6%` | `46.4%` | `1.16` | 1,120,000.00 USD |
| `4H` | `Whale Positions` | `48.84%` | `51.16%` | `0.95` | 77,030,000.00 USD |
| `4H` | `Global Accounts` | `50.23%` | `49.77%` | `1.01` | 163,560,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `8.49` | `8.51` | `8.49` | `8.55` | `8.48` | 1,276,824.26 USD | 505,302.94 USD | 771,521.32 USD | -266,218.38 USD | `-20.85%` | `4B / 18S` |
| `0:00 UTC` | `8.48` | `8.48` | `8.48` | `8.52` | `8.45` | 1,829,814.14 USD | 869,168.19 USD | 960,645.95 USD | -91,477.76 USD | `-5.00%` | `11B / 14S` |
| `5:00 UTC` | `8.51` | `8.50` | `8.51` | `8.52` | `8.48` | 752,301.06 USD | 385,792.91 USD | 366,508.15 USD | 19,284.76 USD | `+2.56%` | `8B / 9S` |
| `0:00 UTC` | `8.46` | `8.47` | `8.46` | `8.49` | `8.46` | 681,089.39 USD | 260,569.06 USD | 420,520.33 USD | -159,951.27 USD | `-23.48%` | `1B / 5S` |
| `5:00 UTC` | `8.49` | `8.48` | `8.49` | `8.50` | `8.45` | 460,668.30 USD | 266,426.92 USD | 194,241.38 USD | 72,185.55 USD | `+15.67%` | `10B / 4S` |
| `0:00 UTC` | `8.48` | `8.48` | `8.48` | `8.51` | `8.46` | 702,848.74 USD | 346,932.98 USD | 355,915.76 USD | -8,982.78 USD | `-1.28%` | `2B / 6S` |
| `5:00 UTC` | `8.46` | `8.47` | `8.46` | `8.48` | `8.46` | 798,371.69 USD | 455,825.46 USD | 342,546.23 USD | 113,279.23 USD | `+14.19%` | `6B / 4S` |
| `0:00 UTC` | `8.47` | `8.46` | `8.47` | `8.48` | `8.44` | 1,028,869.35 USD | 429,609.02 USD | 599,260.32 USD | -169,651.30 USD | `-16.49%` | `4B / 8S` |
| `5:00 UTC` | `8.47` | `8.47` | `8.47` | `8.49` | `8.46` | 909,192.14 USD | 370,410.27 USD | 538,781.87 USD | -168,371.60 USD | `-18.52%` | `3B / 9S` |
| `0:00 UTC` | `8.47` | `8.48` | `8.47` | `8.49` | `8.46` | 516,046.70 USD | 229,934.61 USD | 286,112.09 USD | -56,177.48 USD | `-10.89%` | `3B / 5S` |

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
| `5m` | 4,850.00 USD | 101,250.00 USD | **`ACCUMULATION`** |
| `15m` | -20,330.00 USD | -112,140.00 USD | **`DISTRIBUTION`** |
| `30m` | -133,290.00 USD | -293,960.00 USD | **`DISTRIBUTION`** |
| `1h` | -132,460.00 USD | -209,190.00 USD | **`DISTRIBUTION`** |
| `2h` | -354,820.00 USD | -624,180.00 USD | **`DISTRIBUTION`** |
| `4h` | -394,940.00 USD | -732,530.00 USD | **`DISTRIBUTION`** |
| `6h` | -80,760.00 USD | -1,210,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 376,740.00 USD | 1,760,000.00 USD | **`ACCUMULATION`** |
| `12h` | 234,740.00 USD | -3,610,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,890,000.00 USD | -12,520,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,830,000.00 USD | -51,050,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -57,370,000.00 USD | -267,290,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+4.85K` | 15m=`-20.33K` | 1h=`-132.46K` | 24h=`-2.89M`
* Futures Capital Netflows: 5m=`+101.25K` | 15m=`-112.14K` | 1h=`-209.19K` | 24h=`-12.52M`
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
  * Execution Entry: `8.24` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.11` (Risk Distance: `0.1296` pts)
  * +2.5R Take Profit: `8.56`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.59` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.72` (Risk Distance: `0.1296` pts)
  * +2.5R Take Profit: `8.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.55`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
