# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 07:39:18 IST` (`2026-10-30 02:09:18 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.16` | **Live Ask Quote**: `8.19` | **Mid Price**: `8.18`
- **Spread Points**: `3.00` | **Spread BPS**: `36.70 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.14` | VWAP Z-Score: `-1.43` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1058` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `35.64` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `9.33` | Lower -3.00σ Band: `7.77`
  * Upper +2.51σ Band: `9.20` | Lower -2.51σ Band: `7.90`
  * Upper +2.01σ Band: `9.07` | Lower -2.01σ Band: `8.03`
  * Upper +2.00σ Band: `9.07` | Lower -2.00σ Band: `8.03`
  * Upper +1.28σ Band: `8.88` | Lower -1.28σ Band: `8.22`
  * Upper +1.00σ Band: `8.81` | Lower -1.00σ Band: `8.29`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.21` | EMA-20=`8.31` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.50` (Slope: `+0.0000`) | EMA-100=`8.63`
  * Institutional Anchors: EMA-144=`8.68` | EMA-200=`8.72` (Slope: `-0.7270`) | EMA-233=`8.74`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`7.97` | Weekly High=`9.14` | Weekly Low=`7.97`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.40` (Distance: `-2.65%`)
  * Point of Control (POC) = `8.32` (Distance: `-1.70%`)
  * Value Area Low (VAL) = `8.12` (Distance: `+0.71%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`9.00` | Weekly POC=`8.92` | Weekly VAL=`8.73`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.58` | Low=`7.97`
  * London Session (08:00-16:00 UTC): High=`8.21` | Low=`8.14`
  * New York Session (13:00-21:00 UTC): High=`8.22` | Low=`8.13`
  * Initial Balance (First Hour): IB High=`8.20` | IB Low=`8.15`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.14` - `8.21`
  * Optimal Trade Entry (OTE 0.705): `8.19`
  * Structural Invalidation Anchor (0.786): `8.24`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.21` | `8.21` | `8.16` | `8.20` | `53,060` | 433,966.34 USD | -88,607.21 USD | `-20.42%` | -8,242,481.19 USD | `-0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `8.20` | `8.21` | `8.17` | `8.20` | `56,158` | 460,165.33 USD | 231,723.69 USD | `+50.36%` | -8,010,757.50 USD | `+0.50` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `8.20` | `8.22` | `8.19` | `8.19` | `17,032` | 139,703.28 USD | 8,177.37 USD | `+5.85%` | -8,002,580.13 USD | `-0.05` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `8.27` | `8.27` | `8.20` | `8.21` | `223,488` | 1,839,796.84 USD | -80,084.40 USD | `-4.35%` | -7,863,657.47 USD | `+0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `8.21` | `8.26` | `8.11` | `8.21` | `310,233` | 2,539,835.55 USD | -290,216.50 USD | `-11.43%` | -8,153,873.98 USD | `-0.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `8.21` | `8.22` | `8.16` | `8.19` | `126,250` | 1,033,834.95 USD | 151,293.84 USD | `+14.63%` | -8,002,580.14 USD | `+0.06` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `8.35` | `8.36` | `8.24` | `8.28` | `1,366,717` | 11,346,695.34 USD | -249,386.75 USD | `-2.20%` | -6,975,876.88 USD | `+0.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `8.28` | `8.30` | `7.99` | `8.21` | `2,821,552` | 22,964,413.15 USD | -1,514,352.98 USD | `-6.59%` | -8,490,229.86 USD | `-0.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `8.21` | `8.28` | `8.11` | `8.19` | `1,036,072` | 8,507,234.71 USD | 488,886.57 USD | `+5.75%` | -8,001,343.29 USD | `+0.51` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,242,979.60 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,578,925.42 USD | `-1.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.30` | `7.99` | `8.19` | `3,857,573` | 31,471,230.22 USD | -1,025,703.88 USD | `-3.26%` | -6,604,629.30 USD | `+0.05` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | 322,838.02 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | 269,016.05 USD | `-1.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,242,979.60 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,578,925.42 USD | `-1.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.30` | `7.99` | `8.19` | `3,857,573` | 31,471,230.22 USD | -1,025,703.88 USD | `-3.26%` | -6,604,629.30 USD | `+0.05` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`8.18`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BUY` | `8.03` | `2740.8500` | 21,999.98 USD | 3,597,218.67 USD | `STANDARD` | `-1.95%` | `0x0efb38a5fa` |
| `BUY` | `8.03` | `338.5200` | 2,716.96 USD | 4,750,692.86 USD | `STANDARD` | `-1.96%` | `0x6abc111bd2` |
| `BUY` | `8.03` | `202.7300` | 1,628.41 USD | 4,826,996.59 USD | `STANDARD` | `-1.88%` | `0x010461c14e` |
| `BUY` | `8.03` | `198.0000` | 1,590.42 USD | 4,828,587.01 USD | `STANDARD` | `-1.88%` | `0x31ca8395cf` |
| `BUY` | `8.04` | `13092.0600` | 105,288.96 USD | 2,955,388.02 USD | `LARGE (>= USD 100K)` | `-1.76%` | `0xecb63caa47` |
| `BUY` | `8.05` | `315.7300` | 2,542.57 USD | 4,768,795.25 USD | `STANDARD` | `-1.63%` | `0x07fd993f0f` |
| `BUY` | `8.06` | `11849.1800` | 95,452.25 USD | 3,251,232.66 USD | `MEDIUM (>= USD 25K)` | `-1.60%` | `0xecb63caa47` |
| `BUY` | `8.06` | `2356.4700` | 18,999.98 USD | 3,616,218.65 USD | `STANDARD` | `-1.51%` | `0x0efb38a5fa` |
| `BUY` | `8.06` | `2219.5100` | 17,896.35 USD | 3,709,631.03 USD | `STANDARD` | `-1.50%` | `0xd3943e4008` |
| `BUY` | `8.07` | `17983.3300` | 145,166.83 USD | 2,223,624.27 USD | `LARGE (>= USD 100K)` | `-1.39%` | `0x71d0e11ebb` |
| `BUY` | `8.07` | `217.9000` | 1,758.47 USD | 4,822,026.00 USD | `STANDARD` | `-1.42%` | `0x31ca8395cf` |
| `BUY` | `8.07` | `186.3700` | 1,503.65 USD | 4,830,090.66 USD | `STANDARD` | `-1.44%` | `0x010461c14e` |
| `BUY` | `8.08` | `14166.8000` | 114,419.58 USD | 2,850,099.05 USD | `LARGE (>= USD 100K)` | `-1.34%` | `0xecb63caa47` |
| `BUY` | `8.08` | `7825.0300` | 63,262.24 USD | 3,468,043.66 USD | `MEDIUM (>= USD 25K)` | `-1.24%` | `0x71d0e11ebb` |
| `BUY` | `8.08` | `4405.8200` | 35,614.01 USD | 3,544,079.12 USD | `MEDIUM (>= USD 25K)` | `-1.26%` | `0xa24c5ca26c` |
| `BUY` | `8.09` | `10962.5400` | 88,717.64 USD | 3,339,950.31 USD | `MEDIUM (>= USD 25K)` | `-1.14%` | `0xecb63caa47` |
| `BUY` | `8.09` | `1978.6300` | 15,999.99 USD | 3,725,631.03 USD | `STANDARD` | `-1.22%` | `0x0efb38a5fa` |
| `BUY` | `8.09` | `1855.9000` | 15,016.27 USD | 4,216,076.14 USD | `STANDARD` | `-1.16%` | `0xd3943e4008` |
| `BUY` | `8.10` | `39949.9200` | 323,698.22 USD | 1,300,700.20 USD | `LARGE (>= USD 100K)` | `-1.02%` | `0x71cfa5e263` |
| `BUY` | `8.10` | `1343.8600` | 10,888.76 USD | 4,323,694.73 USD | `STANDARD` | `-1.02%` | `0x33ad48ed92` |
| `BUY` | `8.10` | `93.3500` | 756.30 USD | 4,931,462.61 USD | `STANDARD` | `-1.03%` | `0x31ca8395cf` |
| `BUY` | `8.10` | `89.1300` | 721.83 USD | 4,940,306.19 USD | `STANDARD` | `-1.07%` | `0x010461c14e` |
| `BUY` | `8.11` | `17981.6900` | 145,840.50 USD | 2,078,457.43 USD | `LARGE (>= USD 100K)` | `-0.93%` | `0x71d0e11ebb` |
| `BUY` | `8.11` | `315.7300` | 2,560.57 USD | 4,761,143.92 USD | `STANDARD` | `-0.93%` | `0x07fd993f0f` |
| `BUY` | `8.12` | `12339.6200` | 100,195.25 USD | 3,155,780.41 USD | `LARGE (>= USD 100K)` | `-0.81%` | `0x881cd92459` |
| `BUY` | `8.12` | `2314.5100` | 18,792.20 USD | 3,672,942.51 USD | `STANDARD` | `-0.82%` | `0xa38f19c4cc` |
| `BUY` | `8.12` | `1460.7300` | 11,860.84 USD | 4,290,693.70 USD | `STANDARD` | `-0.81%` | `0xd3943e4008` |
| `BUY` | `8.12` | `92.5500` | 751.07 USD | 4,934,469.60 USD | `STANDARD` | `-0.87%` | `0x010461c14e` |
| `BUY` | `8.13` | `1476.1900` | 11,999.95 USD | 4,266,832.94 USD | `STANDARD` | `-0.70%` | `0x0efb38a5fa` |
| `BUY` | `8.13` | `1026.8300` | 8,351.31 USD | 4,480,073.86 USD | `STANDARD` | `-0.65%` | `0x33ad48ed92` |
| `BUY` | `8.14` | `20367.4400` | 165,874.47 USD | 1,634,444.30 USD | `LARGE (>= USD 100K)` | `-0.52%` | `0x71cfa5e263` |
| `BUY` | `8.14` | `15622.5100` | 127,168.79 USD | 2,735,679.48 USD | `LARGE (>= USD 100K)` | `-0.56%` | `0x71d0e11ebb` |
| `BUY` | `8.14` | `3825.6400` | 31,139.56 USD | 3,575,218.69 USD | `MEDIUM (>= USD 25K)` | `-0.57%` | `0x26934acbd3` |
| `BUY` | `8.14` | `1205.5600` | 9,813.74 USD | 4,425,342.57 USD | `STANDARD` | `-0.56%` | `0xd3943e4008` |
| `BUY` | `8.14` | `564.5200` | 4,597.85 USD | 4,639,902.32 USD | `STANDARD` | `-0.51%` | `0xcd7f60e943` |
| `BUY` | `8.14` | `467.8500` | 3,810.45 USD | 4,703,328.69 USD | `STANDARD` | `-0.51%` | `0x2a72b57dea` |
| `BUY` | `8.14` | `245.1000` | 1,996.09 USD | 4,801,287.14 USD | `STANDARD` | `-0.52%` | `0x39bac00809` |
| `BUY` | `8.14` | `107.0600` | 871.92 USD | 4,900,404.62 USD | `STANDARD` | `-0.51%` | `0xd0956a1eba` |
| `BUY` | `8.14` | `80.8600` | 658.39 USD | 4,947,811.94 USD | `STANDARD` | `-0.54%` | `0x010461c14e` |
| `BUY` | `8.14` | `80.2900` | 653.92 USD | 4,951,089.58 USD | `STANDARD` | `-0.51%` | `0x63f6411ca6` |
| `BUY` | `8.15` | `1866.9900` | 15,221.57 USD | 4,201,059.87 USD | `STANDARD` | `-0.41%` | `0x57d8e75f47` |
| `BUY` | `8.15` | `1238.0600` | 10,089.94 USD | 4,385,871.04 USD | `STANDARD` | `-0.45%` | `0xd3342d3b1e` |
| `BUY` | `8.15` | `1077.3600` | 8,778.44 USD | 4,463,258.29 USD | `STANDARD` | `-0.47%` | `0xd3943e4008` |
| `BUY` | `8.15` | `981.5400` | 7,999.94 USD | 4,520,573.25 USD | `STANDARD` | `-0.44%` | `0x0efb38a5fa` |
| `BUY` | `8.15` | `923.2000` | 7,524.17 USD | 4,535,985.83 USD | `STANDARD` | `-0.44%` | `0xecb63caa47` |
| `BUY` | `8.15` | `876.9500` | 7,150.91 USD | 4,550,287.70 USD | `STANDARD` | `-0.39%` | `0x47a4471457` |
| `BUY` | `8.15` | `762.4300` | 6,214.03 USD | 4,588,681.19 USD | `STANDARD` | `-0.44%` | `0xecb63caa47` |
| `BUY` | `8.15` | `467.8500` | 3,815.08 USD | 4,699,518.24 USD | `STANDARD` | `-0.39%` | `0x2a72b57dea` |
| `BUY` | `8.15` | `273.8400` | 2,233.11 USD | 4,790,879.36 USD | `STANDARD` | `-0.38%` | `0xecb63caa47` |
| `BUY` | `8.15` | `107.0800` | 872.31 USD | 4,896,044.04 USD | `STANDARD` | `-0.49%` | `0xf30120f048` |
| `BUY` | `8.15` | `107.0600` | 872.22 USD | 4,896,916.26 USD | `STANDARD` | `-0.48%` | `0xea0e878d5d` |
| `BUY` | `8.15` | `107.0600` | 872.16 USD | 4,897,788.43 USD | `STANDARD` | `-0.49%` | `0xea0e878d5d` |
| `BUY` | `8.15` | `107.0700` | 872.15 USD | 4,898,660.58 USD | `STANDARD` | `-0.50%` | `0xfd66e33095` |
| `BUY` | `8.15` | `107.0700` | 872.13 USD | 4,899,532.70 USD | `STANDARD` | `-0.50%` | `0xea0e878d5d` |
| `BUY` | `8.15` | `87.2300` | 710.64 USD | 4,941,732.26 USD | `STANDARD` | `-0.48%` | `0x31ca8395cf` |
| `BUY` | `8.16` | `15643.9400` | 127,646.73 USD | 2,608,510.68 USD | `LARGE (>= USD 100K)` | `-0.33%` | `0x71d0e11ebb` |
| `BUY` | `8.16` | `1866.9900` | 15,240.05 USD | 4,155,377.61 USD | `STANDARD` | `-0.29%` | `0x57d8e75f47` |
| `BUY` | `8.16` | `1866.9900` | 15,234.64 USD | 4,170,612.25 USD | `STANDARD` | `-0.32%` | `0x57d8e75f47` |
| `BUY` | `8.16` | `1866.9900` | 15,226.05 USD | 4,185,838.30 USD | `STANDARD` | `-0.38%` | `0x57d8e75f47` |
| `BUY` | `8.16` | `1036.9300` | 8,464.25 USD | 4,471,722.55 USD | `STANDARD` | `-0.29%` | `0xd3943e4008` |
| `BUY` | `8.16` | `796.6100` | 6,502.49 USD | 4,556,790.19 USD | `STANDARD` | `-0.29%` | `0xa38f19c4cc` |
| `BUY` | `8.16` | `672.8100` | 5,487.30 USD | 4,605,735.46 USD | `STANDARD` | `-0.37%` | `0x33ad48ed92` |
| `BUY` | `8.16` | `613.5000` | 5,004.01 USD | 4,615,753.58 USD | `STANDARD` | `-0.36%` | `0x3ca146d269` |
| `BUY` | `8.16` | `600.8100` | 4,903.03 USD | 4,630,656.55 USD | `STANDARD` | `-0.31%` | `0xecb63caa47` |
| `BUY` | `8.16` | `467.8500` | 3,817.94 USD | 4,695,703.15 USD | `STANDARD` | `-0.31%` | `0x2a72b57dea` |
| `BUY` | `8.16` | `366.8200` | 2,995.01 USD | 4,744,982.03 USD | `STANDARD` | `-0.26%` | `0xdd4f66125d` |
| `BUY` | `8.16` | `366.8200` | 2,993.87 USD | 4,747,975.90 USD | `STANDARD` | `-0.30%` | `0xdd4f66125d` |
| `BUY` | `8.16` | `107.0800` | 874.18 USD | 4,883,817.81 USD | `STANDARD` | `-0.27%` | `0x53136b4a7c` |
| `BUY` | `8.16` | `107.0600` | 874.10 USD | 4,884,691.92 USD | `STANDARD` | `-0.27%` | `0xa382fa9f4b` |
| `BUY` | `8.16` | `107.0600` | 874.03 USD | 4,885,565.94 USD | `STANDARD` | `-0.27%` | `0x63f6411ca6` |
| `BUY` | `8.16` | `107.0700` | 874.02 USD | 4,886,439.97 USD | `STANDARD` | `-0.28%` | `0xfd66e33095` |
| `BUY` | `8.16` | `107.0700` | 873.85 USD | 4,887,313.82 USD | `STANDARD` | `-0.30%` | `0xd0956a1eba` |
| `BUY` | `8.16` | `107.0500` | 873.68 USD | 4,888,187.50 USD | `STANDARD` | `-0.30%` | `0xea0e878d5d` |
| `BUY` | `8.16` | `107.0600` | 873.62 USD | 4,889,061.12 USD | `STANDARD` | `-0.32%` | `0x63f6411ca6` |
| `BUY` | `8.16` | `107.0500` | 873.60 USD | 4,889,934.72 USD | `STANDARD` | `-0.31%` | `0xa382fa9f4b` |
| `BUY` | `8.16` | `106.0300` | 865.52 USD | 4,929,941.72 USD | `STANDARD` | `-0.28%` | `0x9d81a3adf8` |
| `BUY` | `8.16` | `79.5400` | 649.19 USD | 4,953,042.54 USD | `STANDARD` | `-0.30%` | `0xd0956a1eba` |
| `BUY` | `8.17` | `1866.9900` | 15,257.79 USD | 4,094,390.51 USD | `STANDARD` | `-0.17%` | `0x57d8e75f47` |
| `BUY` | `8.17` | `1866.9900` | 15,253.49 USD | 4,109,644.01 USD | `STANDARD` | `-0.20%` | `0x57d8e75f47` |
| `BUY` | `8.17` | `1866.9900` | 15,249.20 USD | 4,124,893.21 USD | `STANDARD` | `-0.23%` | `0x57d8e75f47` |
| `BUY` | `8.17` | `1866.9900` | 15,244.35 USD | 4,140,137.56 USD | `STANDARD` | `-0.26%` | `0x57d8e75f47` |
| `BUY` | `8.17` | `1352.4300` | 11,054.22 USD | 4,312,805.97 USD | `STANDARD` | `-0.16%` | `0xa38f19c4cc` |
| `BUY` | `8.17` | `1320.2900` | 10,791.39 USD | 4,334,486.12 USD | `STANDARD` | `-0.16%` | `0x26934acbd3` |
| `BUY` | `8.17` | `1197.9600` | 9,784.94 USD | 4,444,922.15 USD | `STANDARD` | `-0.22%` | `0xaf9f722a67` |
| `BUY` | `8.17` | `788.8500` | 6,444.43 USD | 4,576,181.67 USD | `STANDARD` | `-0.21%` | `0x08a49e7f71` |
| `BUY` | `8.17` | `612.3300` | 4,999.98 USD | 4,620,753.56 USD | `STANDARD` | `-0.25%` | `0x0efb38a5fa` |
| `BUY` | `8.17` | `513.5800` | 4,197.39 USD | 4,652,829.39 USD | `STANDARD` | `-0.16%` | `0x71d0e11ebb` |
| `BUY` | `8.17` | `481.6400` | 3,934.13 USD | 4,668,881.27 USD | `STANDARD` | `-0.22%` | `0x7717a7a245` |
| `BUY` | `8.17` | `467.8500` | 3,822.57 USD | 4,691,885.22 USD | `STANDARD` | `-0.19%` | `0x2a72b57dea` |
| `BUY` | `8.17` | `385.2200` | 3,147.29 USD | 4,720,790.87 USD | `STANDARD` | `-0.20%` | `0xecb63caa47` |
| `BUY` | `8.17` | `385.1200` | 3,147.28 USD | 4,723,938.15 USD | `STANDARD` | `-0.17%` | `0xecb63caa47` |
| `BUY` | `8.17` | `366.8200` | 2,996.81 USD | 4,741,987.01 USD | `STANDARD` | `-0.20%` | `0xdd4f66125d` |
| `BUY` | `8.17` | `295.9900` | 2,416.91 USD | 4,786,229.35 USD | `STANDARD` | `-0.25%` | `0xecb63caa47` |
| `BUY` | `8.17` | `295.9100` | 2,416.90 USD | 4,788,646.25 USD | `STANDARD` | `-0.23%` | `0xecb63caa47` |
| `BUY` | `8.17` | `269.1200` | 2,198.98 USD | 4,793,078.34 USD | `STANDARD` | `-0.19%` | `0x33ad48ed92` |
| `BUY` | `8.17` | `107.0700` | 875.28 USD | 4,874,195.35 USD | `STANDARD` | `-0.14%` | `0x63f6411ca6` |
| `BUY` | `8.17` | `107.0700` | 875.25 USD | 4,875,070.61 USD | `STANDARD` | `-0.14%` | `0x63f6411ca6` |
| `BUY` | `8.17` | `107.0700` | 875.19 USD | 4,875,945.80 USD | `STANDARD` | `-0.15%` | `0x53136b4a7c` |
| `BUY` | `8.17` | `107.0800` | 875.15 USD | 4,876,820.95 USD | `STANDARD` | `-0.16%` | `0x9d81a3adf8` |
| `BUY` | `8.17` | `107.0800` | 875.03 USD | 4,877,695.98 USD | `STANDARD` | `-0.18%` | `0xfd66e33095` |
| `BUY` | `8.17` | `107.0600` | 874.80 USD | 4,878,570.78 USD | `STANDARD` | `-0.19%` | `0x63f6411ca6` |
| `BUY` | `8.17` | `107.0600` | 874.71 USD | 4,879,445.49 USD | `STANDARD` | `-0.20%` | `0x53136b4a7c` |
| `BUY` | `8.17` | `107.0700` | 874.71 USD | 4,880,320.20 USD | `STANDARD` | `-0.21%` | `0xfd66e33095` |
| `BUY` | `8.17` | `107.0800` | 874.66 USD | 4,881,194.86 USD | `STANDARD` | `-0.22%` | `0xa382fa9f4b` |
| `BUY` | `8.17` | `107.0600` | 874.56 USD | 4,882,069.42 USD | `STANDARD` | `-0.21%` | `0x9d81a3adf8` |
| `BUY` | `8.17` | `107.0500` | 874.21 USD | 4,882,943.63 USD | `STANDARD` | `-0.24%` | `0xfd66e33095` |
| `BUY` | `8.17` | `106.0600` | 866.89 USD | 4,925,611.26 USD | `STANDARD` | `-0.16%` | `0xd0956a1eba` |
| `BUY` | `8.17` | `106.0300` | 866.53 USD | 4,926,477.79 USD | `STANDARD` | `-0.17%` | `0x53136b4a7c` |
| `BUY` | `8.17` | `106.0600` | 866.29 USD | 4,927,344.08 USD | `STANDARD` | `-0.22%` | `0x9d81a3adf8` |
| `BUY` | `8.17` | `106.0600` | 866.21 USD | 4,928,210.29 USD | `STANDARD` | `-0.23%` | `0x9d81a3adf8` |
| `BUY` | `8.17` | `106.0300` | 865.90 USD | 4,929,076.19 USD | `STANDARD` | `-0.24%` | `0xa382fa9f4b` |
| `BUY` | `8.17` | `89.0000` | 726.79 USD | 4,937,411.85 USD | `STANDARD` | `-0.25%` | `0x010461c14e` |
| `BUY` | `8.17` | `86.5700` | 706.92 USD | 4,942,439.18 USD | `STANDARD` | `-0.25%` | `0x31ca8395cf` |
| `BUY` | `8.17` | `80.3000` | 655.71 USD | 4,949,781.18 USD | `STANDARD` | `-0.25%` | `0x53136b4a7c` |
| `BUY` | `8.17` | `78.6000` | 642.48 USD | 4,954,980.26 USD | `STANDARD` | `-0.15%` | `0x31ca8395cf` |
| `BID` | `8.18` | `107.0700` | 876.36 USD | 2,143.04 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.18` | `148.7200` | 1,217.21 USD | 3,360.26 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.18` | `106.0600` | 868.01 USD | 4,228.26 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.18` | `186.8800` | 1,529.35 USD | 5,757.61 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.18` | `123.0700` | 1,007.14 USD | 6,764.76 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.18` | `5.7100` | 46.73 USD | 6,811.48 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.18` | `107.0800` | 876.26 USD | 7,687.74 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.18` | `50.0000` | 409.15 USD | 8,096.90 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.18` | `122.2000` | 999.96 USD | 9,096.86 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.18` | `107.0700` | 876.10 USD | 9,972.96 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.18` | `120.0800` | 982.53 USD | 10,955.49 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.18` | `5.8000` | 47.46 USD | 11,002.95 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.18` | `1882.9900` | 15,406.62 USD | 26,409.57 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.18` | `200.5100` | 1,640.53 USD | 28,050.10 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.18` | `107.0800` | 876.03 USD | 28,926.14 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.18` | `60.3400` | 493.62 USD | 29,419.75 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.18` | `325.7800` | 2,665.04 USD | 32,084.80 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.18` | `107.0700` | 875.88 USD | 32,960.67 USD | `1 orders` | `-0.07%` | `-` |
| `BUY` | `8.18` | `1866.9900` | 15,275.71 USD | 4,048,596.61 USD | `STANDARD` | `-0.05%` | `0x57d8e75f47` |
| `BUY` | `8.18` | `1866.9900` | 15,270.48 USD | 4,063,867.09 USD | `STANDARD` | `-0.09%` | `0x57d8e75f47` |
| `BUY` | `8.18` | `1866.9900` | 15,265.63 USD | 4,079,132.72 USD | `STANDARD` | `-0.12%` | `0x57d8e75f47` |
| `BUY` | `8.18` | `1245.4400` | 10,186.83 USD | 4,365,604.12 USD | `STANDARD` | `-0.09%` | `0x621c555167` |
| `BUY` | `8.18` | `1197.9600` | 9,794.64 USD | 4,435,137.21 USD | `STANDARD` | `-0.12%` | `0xaf9f722a67` |
| `BUY` | `8.18` | `467.8500` | 3,825.47 USD | 4,688,062.65 USD | `STANDARD` | `-0.12%` | `0x2a72b57dea` |
| `BUY` | `8.18` | `312.0500` | 2,551.51 USD | 4,766,252.68 USD | `STANDARD` | `-0.12%` | `0x7717a7a245` |
| `BUY` | `8.18` | `305.6500` | 2,499.97 USD | 4,778,830.09 USD | `STANDARD` | `-0.09%` | `0x0efb38a5fa` |
| `BUY` | `8.18` | `230.8400` | 1,887.95 USD | 4,820,267.52 USD | `STANDARD` | `-0.09%` | `0xe86b057f5e` |
| `BUY` | `8.18` | `148.7200` | 1,217.21 USD | 4,834,028.26 USD | `STANDARD` | `-0.02%` | `0x727956612a` |
| `BUY` | `8.18` | `137.5600` | 1,125.21 USD | 4,836,280.83 USD | `STANDARD` | `-0.08%` | `0xdd4f66125d` |
| `BUY` | `8.18` | `137.5600` | 1,125.14 USD | 4,837,405.97 USD | `STANDARD` | `-0.09%` | `0xdd4f66125d` |
| `BUY` | `8.18` | `137.5600` | 1,125.09 USD | 4,838,531.06 USD | `STANDARD` | `-0.09%` | `0xdd4f66125d` |
| `BUY` | `8.18` | `127.6300` | 1,044.04 USD | 4,841,738.17 USD | `STANDARD` | `-0.07%` | `0xecb63caa47` |
| `BUY` | `8.18` | `122.2000` | 999.96 USD | 4,844,781.40 USD | `STANDARD` | `-0.04%` | `0x0eecd62efb` |
| `BUY` | `8.18` | `122.2700` | 999.96 USD | 4,845,781.36 USD | `STANDARD` | `-0.10%` | `0x27c9fa86c9` |
| `BUY` | `8.18` | `120.0800` | 982.53 USD | 4,848,747.29 USD | `STANDARD` | `-0.05%` | `0x7717a7a245` |
| `BUY` | `8.18` | `107.0700` | 876.36 USD | 4,863,686.66 USD | `STANDARD` | `-0.02%` | `0x9d81a3adf8` |
| `BUY` | `8.18` | `107.0800` | 876.26 USD | 4,864,562.92 USD | `STANDARD` | `-0.04%` | `0xa382fa9f4b` |
| `BUY` | `8.18` | `107.0700` | 876.10 USD | 4,865,439.02 USD | `STANDARD` | `-0.05%` | `0xea0e878d5d` |
| `BUY` | `8.18` | `107.0800` | 876.03 USD | 4,866,315.05 USD | `STANDARD` | `-0.06%` | `0xd0956a1eba` |
| `BUY` | `8.18` | `107.0600` | 875.94 USD | 4,867,190.99 USD | `STANDARD` | `-0.05%` | `0xf30120f048` |
| `BUY` | `8.18` | `107.0700` | 875.88 USD | 4,868,066.87 USD | `STANDARD` | `-0.07%` | `0xa382fa9f4b` |
| `BUY` | `8.18` | `107.0600` | 875.69 USD | 4,868,942.56 USD | `STANDARD` | `-0.08%` | `0xf30120f048` |
| `BUY` | `8.18` | `107.0600` | 875.60 USD | 4,869,818.16 USD | `STANDARD` | `-0.09%` | `0xd0956a1eba` |
| `BUY` | `8.18` | `107.0600` | 875.53 USD | 4,870,693.68 USD | `STANDARD` | `-0.10%` | `0x63f6411ca6` |
| `BUY` | `8.18` | `107.0700` | 875.49 USD | 4,871,569.17 USD | `STANDARD` | `-0.12%` | `0x53136b4a7c` |
| `BUY` | `8.18` | `107.0600` | 875.47 USD | 4,872,444.65 USD | `STANDARD` | `-0.11%` | `0x53136b4a7c` |
| `BUY` | `8.18` | `107.0800` | 875.43 USD | 4,873,320.08 USD | `STANDARD` | `-0.13%` | `0xea0e878d5d` |
| `BUY` | `8.18` | `106.0600` | 868.02 USD | 4,923,008.41 USD | `STANDARD` | `-0.03%` | `0xf30120f048` |
| `BUY` | `8.18` | `106.0600` | 868.01 USD | 4,923,876.41 USD | `STANDARD` | `-0.03%` | `0xf30120f048` |
| `BUY` | `8.18` | `106.0600` | 867.95 USD | 4,924,744.37 USD | `STANDARD` | `-0.03%` | `0x63f6411ca6` |
| `BUY` | `8.18` | `93.4500` | 764.59 USD | 4,930,706.31 USD | `STANDARD` | `-0.05%` | `0x31ca8395cf` |
| `BUY` | `8.18` | `88.6600` | 724.93 USD | 4,938,136.78 USD | `STANDARD` | `-0.12%` | `0x010461c14e` |
| `BUY` | `8.18` | `80.8200` | 661.40 USD | 4,945,833.40 USD | `STANDARD` | `-0.03%` | `0x010461c14e` |
| `BUY` | `8.18` | `80.2900` | 656.47 USD | 4,949,125.48 USD | `STANDARD` | `-0.12%` | `0x53136b4a7c` |
| `BUY` | `8.18` | `68.4600` | 559.80 USD | 4,956,167.71 USD | `STANDARD` | `-0.11%` | `0x33ad48ed92` |
| `ASK` | `8.19` | `30.5500` | 250.28 USD | 51,679.58 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.19` | `1552.1200` | 12,715.43 USD | 51,429.30 USD | `2 orders` | `+0.07%` | `-` |
| `ASK` | `8.19` | `5.8000` | 47.51 USD | 38,713.87 USD | `2 orders` | `+0.07%` | `-` |
| `ASK` | `8.19` | `107.0600` | 877.05 USD | 38,666.36 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.19` | `76.6200` | 627.65 USD | 37,789.31 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.19` | `122.0700` | 999.95 USD | 37,161.66 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.19` | `337.5500` | 2,765.01 USD | 36,161.71 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.19` | `137.8500` | 1,129.13 USD | 33,396.71 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.19` | `46.7900` | 383.22 USD | 32,267.58 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.19` | `1220.9700` | 9,999.99 USD | 31,884.35 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.19` | `106.0600` | 868.64 USD | 21,884.37 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.19` | `120.0800` | 983.46 USD | 21,015.72 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.19` | `106.0600` | 868.62 USD | 20,032.27 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.19` | `106.0300` | 868.30 USD | 19,163.65 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.19` | `61.0700` | 500.07 USD | 18,295.35 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.19` | `977.0500` | 8,000.48 USD | 17,795.27 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.19` | `106.0400` | 868.23 USD | 9,794.80 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.19` | `150.4300` | 1,231.68 USD | 8,926.56 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.19` | `812.4000` | 6,651.61 USD | 7,694.89 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `8.19` | `127.4300` | 1,043.28 USD | 1,043.28 USD | `1 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `8.19` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.19` | `0.00%` | `-` |
| `BID` | `8.19` | `106.0600` | 868.15 USD | 868.15 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.19` | `48.6900` | 398.53 USD | 1,266.69 USD | `2 orders` | `-0.01%` | `-` |
| `SELL` | `8.19` | `1464.7900` | 12,000.00 USD | 4,254,832.99 USD | `STANDARD` | `+0.07%` | `0x7d0c59691f` |
| `SELL` | `8.19` | `1220.9700` | 9,999.99 USD | 4,395,871.03 USD | `STANDARD` | `+0.05%` | `0x7d0c59691f` |
| `SELL` | `8.19` | `977.1600` | 8,000.01 USD | 4,504,573.31 USD | `STANDARD` | `+0.01%` | `0x7d0c59691f` |
| `SELL` | `8.19` | `733.0200` | 6,001.23 USD | 4,594,682.43 USD | `STANDARD` | `+0.01%` | `0x7d0c59691f` |
| `SELL` | `8.19` | `366.4700` | 3,002.64 USD | 4,738,990.20 USD | `STANDARD` | `+0.09%` | `0x83bec364a5` |
| `SELL` | `8.19` | `305.0900` | 2,499.97 USD | 4,781,330.06 USD | `STANDARD` | `+0.10%` | `0x0efb38a5fa` |
| `SELL` | `8.19` | `230.4800` | 1,887.95 USD | 4,818,379.57 USD | `STANDARD` | `+0.06%` | `0x414ade317c` |
| `SELL` | `8.19` | `150.4300` | 1,231.68 USD | 4,832,811.04 USD | `STANDARD` | `+0.02%` | `0x727956612a` |
| `SELL` | `8.19` | `130.9500` | 1,072.89 USD | 4,840,694.13 USD | `STANDARD` | `+0.08%` | `0x2eddf3aa5c` |
| `SELL` | `8.19` | `127.4300` | 1,043.28 USD | 4,842,781.45 USD | `STANDARD` | `+0.01%` | `0xecb63caa47` |
| `SELL` | `8.19` | `122.0700` | 999.95 USD | 4,846,781.31 USD | `STANDARD` | `+0.06%` | `0x0eecd62efb` |
| `SELL` | `8.19` | `120.0800` | 983.46 USD | 4,847,764.76 USD | `STANDARD` | `+0.05%` | `0x7717a7a245` |
| `SELL` | `8.19` | `107.0600` | 877.26 USD | 4,858,424.86 USD | `STANDARD` | `+0.10%` | `0xd0956a1eba` |
| `SELL` | `8.19` | `107.0700` | 877.21 USD | 4,859,302.07 USD | `STANDARD` | `+0.08%` | `0xf30120f048` |
| `SELL` | `8.19` | `107.0700` | 877.20 USD | 4,860,179.28 USD | `STANDARD` | `+0.08%` | `0x53136b4a7c` |
| `SELL` | `8.19` | `107.0700` | 877.05 USD | 4,861,056.33 USD | `STANDARD` | `+0.06%` | `0xa382fa9f4b` |
| `SELL` | `8.19` | `107.0600` | 877.05 USD | 4,861,933.38 USD | `STANDARD` | `+0.07%` | `0xd0956a1eba` |
| `SELL` | `8.19` | `107.0600` | 876.93 USD | 4,862,810.30 USD | `STANDARD` | `+0.06%` | `0xf30120f048` |
| `SELL` | `8.19` | `106.0600` | 869.14 USD | 4,915,192.73 USD | `STANDARD` | `+0.10%` | `0xd0956a1eba` |
| `SELL` | `8.19` | `106.0300` | 868.80 USD | 4,916,061.53 USD | `STANDARD` | `+0.09%` | `0xd0956a1eba` |
| `SELL` | `8.19` | `106.0600` | 868.64 USD | 4,916,930.17 USD | `STANDARD` | `+0.05%` | `0x53136b4a7c` |
| `SELL` | `8.19` | `106.0600` | 868.62 USD | 4,917,798.80 USD | `STANDARD` | `+0.04%` | `0x9d81a3adf8` |
| `SELL` | `8.19` | `106.0600` | 868.53 USD | 4,918,667.32 USD | `STANDARD` | `+0.03%` | `0xea0e878d5d` |
| `SELL` | `8.19` | `106.0600` | 868.45 USD | 4,919,535.77 USD | `STANDARD` | `+0.02%` | `0xea0e878d5d` |
| `SELL` | `8.19` | `106.0300` | 868.30 USD | 4,920,404.07 USD | `STANDARD` | `+0.04%` | `0xf30120f048` |
| `BUY` | `8.19` | `106.0600` | 868.16 USD | 4,921,272.24 USD | `STANDARD` | `-0.01%` | `0xea0e878d5d` |
| `BUY` | `8.19` | `106.0600` | 868.15 USD | 4,922,140.39 USD | `STANDARD` | `-0.01%` | `0xfd66e33095` |
| `SELL` | `8.19` | `87.3300` | 715.43 USD | 4,941,021.62 USD | `STANDARD` | `+0.07%` | `0x2eddf3aa5c` |
| `SELL` | `8.19` | `82.3200` | 674.41 USD | 4,944,499.63 USD | `STANDARD` | `+0.08%` | `0x31ca8395cf` |
| `SELL` | `8.19` | `82.0700` | 672.37 USD | 4,945,172.00 USD | `STANDARD` | `+0.08%` | `0x010461c14e` |
| `SELL` | `8.19` | `79.5400` | 651.24 USD | 4,952,393.35 USD | `STANDARD` | `+0.02%` | `0xfd66e33095` |
| `SELL` | `8.19` | `76.6200` | 627.65 USD | 4,955,607.91 USD | `STANDARD` | `+0.07%` | `0x2eddf3aa5c` |
| `SELL` | `8.19` | `61.0700` | 500.07 USD | 4,957,215.88 USD | `STANDARD` | `+0.03%` | `0xa6a1140c06` |
| `SELL` | `8.20` | `1866.9900` | 15,316.41 USD | 3,987,400.79 USD | `STANDARD` | `+0.21%` | `0x57d8e75f47` |
| `SELL` | `8.20` | `1866.9900` | 15,311.00 USD | 4,002,711.78 USD | `STANDARD` | `+0.18%` | `0x57d8e75f47` |
| `SELL` | `8.20` | `1866.9900` | 15,306.70 USD | 4,018,018.49 USD | `STANDARD` | `+0.15%` | `0x57d8e75f47` |
| `SELL` | `8.20` | `1866.9900` | 15,302.41 USD | 4,033,320.90 USD | `STANDARD` | `+0.12%` | `0x57d8e75f47` |
| `SELL` | `8.20` | `1245.4400` | 10,210.74 USD | 4,355,417.29 USD | `STANDARD` | `+0.15%` | `0x621c555167` |
| `SELL` | `8.20` | `1197.9600` | 9,823.99 USD | 4,415,528.83 USD | `STANDARD` | `+0.17%` | `0xaf9f722a67` |
| `SELL` | `8.20` | `961.5200` | 7,888.41 USD | 4,528,461.65 USD | `STANDARD` | `+0.22%` | `0xecb63caa47` |
| `SELL` | `8.20` | `792.6300` | 6,502.42 USD | 4,563,292.61 USD | `STANDARD` | `+0.21%` | `0xa38f19c4cc` |
| `SELL` | `8.20` | `785.7100` | 6,444.63 USD | 4,569,737.24 USD | `STANDARD` | `+0.20%` | `0x08a49e7f71` |
| `SELL` | `8.20` | `513.5100` | 4,208.93 USD | 4,648,632.00 USD | `STANDARD` | `+0.12%` | `0x71d0e11ebb` |
| `SELL` | `8.20` | `481.6400` | 3,951.42 USD | 4,664,947.13 USD | `STANDARD` | `+0.22%` | `0x7717a7a245` |
| `SELL` | `8.20` | `467.8500` | 3,837.49 USD | 4,680,402.59 USD | `STANDARD` | `+0.20%` | `0x2a72b57dea` |
| `SELL` | `8.20` | `467.8500` | 3,834.59 USD | 4,684,237.18 USD | `STANDARD` | `+0.12%` | `0x2a72b57dea` |
| `SELL` | `8.20` | `439.9000` | 3,605.33 USD | 4,710,734.58 USD | `STANDARD` | `+0.12%` | `0xecb63caa47` |
| `SELL` | `8.20` | `414.3000` | 3,397.55 USD | 4,717,643.59 USD | `STANDARD` | `+0.18%` | `0xecb63caa47` |
| `SELL` | `8.20` | `312.0500` | 2,557.25 USD | 4,763,701.17 USD | `STANDARD` | `+0.11%` | `0x7717a7a245` |
| `SELL` | `8.20` | `306.5800` | 2,513.34 USD | 4,771,308.59 USD | `STANDARD` | `+0.14%` | `0xecb63caa47` |
| `SELL` | `8.20` | `306.5000` | 2,513.33 USD | 4,773,821.92 USD | `STANDARD` | `+0.17%` | `0xecb63caa47` |
| `SELL` | `8.20` | `267.4800` | 2,194.08 USD | 4,795,272.43 USD | `STANDARD` | `+0.20%` | `0x33ad48ed92` |
| `SELL` | `8.20` | `137.5600` | 1,127.36 USD | 4,835,155.61 USD | `STANDARD` | `+0.11%` | `0xdd4f66125d` |
| `SELL` | `8.20` | `133.0200` | 1,090.18 USD | 4,839,621.24 USD | `STANDARD` | `+0.11%` | `0x2eddf3aa5c` |
| `SELL` | `8.20` | `122.0000` | 999.99 USD | 4,843,781.43 USD | `STANDARD` | `+0.13%` | `0x27c9fa86c9` |
| `SELL` | `8.20` | `107.0800` | 878.05 USD | 4,856,670.10 USD | `STANDARD` | `+0.17%` | `0xf30120f048` |
| `SELL` | `8.20` | `107.0700` | 877.50 USD | 4,857,547.60 USD | `STANDARD` | `+0.11%` | `0xa382fa9f4b` |
| `SELL` | `8.20` | `106.0600` | 870.05 USD | 4,905,627.04 USD | `STANDARD` | `+0.21%` | `0x9d81a3adf8` |
| `SELL` | `8.20` | `106.0600` | 870.03 USD | 4,906,497.07 USD | `STANDARD` | `+0.21%` | `0xd0956a1eba` |
| `SELL` | `8.20` | `106.0600` | 870.01 USD | 4,907,367.08 USD | `STANDARD` | `+0.20%` | `0xea0e878d5d` |
| `SELL` | `8.20` | `106.0600` | 869.88 USD | 4,908,236.96 USD | `STANDARD` | `+0.19%` | `0x9d81a3adf8` |
| `SELL` | `8.20` | `106.0600` | 869.75 USD | 4,909,106.70 USD | `STANDARD` | `+0.17%` | `0x9d81a3adf8` |
| `SELL` | `8.20` | `106.0300` | 869.62 USD | 4,909,976.32 USD | `STANDARD` | `+0.19%` | `0xd0956a1eba` |
| `SELL` | `8.20` | `106.0600` | 869.61 USD | 4,910,845.93 USD | `STANDARD` | `+0.16%` | `0xea0e878d5d` |
| `SELL` | `8.20` | `106.0600` | 869.52 USD | 4,911,715.45 USD | `STANDARD` | `+0.15%` | `0xa382fa9f4b` |
| `SELL` | `8.20` | `106.0600` | 869.49 USD | 4,912,584.94 USD | `STANDARD` | `+0.14%` | `0xea0e878d5d` |
| `SELL` | `8.20` | `106.0600` | 869.36 USD | 4,913,454.30 USD | `STANDARD` | `+0.13%` | `0x53136b4a7c` |
| `SELL` | `8.20` | `106.0600` | 869.29 USD | 4,914,323.59 USD | `STANDARD` | `+0.12%` | `0x63f6411ca6` |
| `SELL` | `8.20` | `91.7000` | 752.07 USD | 4,932,214.68 USD | `STANDARD` | `+0.18%` | `0xdd4f66125d` |
| `SELL` | `8.20` | `91.7000` | 751.95 USD | 4,932,966.63 USD | `STANDARD` | `+0.17%` | `0xdd4f66125d` |
| `SELL` | `8.20` | `91.7000` | 751.90 USD | 4,933,718.53 USD | `STANDARD` | `+0.16%` | `0xdd4f66125d` |
| `SELL` | `8.20` | `90.0700` | 738.55 USD | 4,935,955.96 USD | `STANDARD` | `+0.16%` | `0x2eddf3aa5c` |
| `SELL` | `8.20` | `86.1400` | 706.36 USD | 4,943,145.54 USD | `STANDARD` | `+0.17%` | `0x010461c14e` |
| `SELL` | `8.20` | `82.8500` | 679.68 USD | 4,943,825.22 USD | `STANDARD` | `+0.21%` | `0x31ca8395cf` |
| `SELL` | `8.20` | `66.8700` | 548.10 USD | 4,956,715.81 USD | `STANDARD` | `+0.12%` | `0x33ad48ed92` |
| `SELL` | `8.21` | `15642.8500` | 128,432.49 USD | 2,480,863.95 USD | `LARGE (>= USD 100K)` | `+0.29%` | `0x71d0e11ebb` |
| `SELL` | `8.21` | `1866.9900` | 15,333.22 USD | 3,941,438.29 USD | `STANDARD` | `+0.32%` | `0x57d8e75f47` |
| `SELL` | `8.21` | `1866.9900` | 15,325.19 USD | 3,956,763.48 USD | `STANDARD` | `+0.27%` | `0x57d8e75f47` |
| `SELL` | `8.21` | `1866.9900` | 15,320.89 USD | 3,972,084.37 USD | `STANDARD` | `+0.24%` | `0x57d8e75f47` |
| `SELL` | `8.21` | `1197.9600` | 9,833.81 USD | 4,405,704.84 USD | `STANDARD` | `+0.27%` | `0xaf9f722a67` |
| `SELL` | `8.21` | `609.1200` | 4,999.96 USD | 4,625,753.52 USD | `STANDARD` | `+0.27%` | `0x0efb38a5fa` |
| `SELL` | `8.21` | `467.8500` | 3,840.39 USD | 4,676,565.09 USD | `STANDARD` | `+0.27%` | `0x2a72b57dea` |
| `SELL` | `8.21` | `462.9800` | 3,800.56 USD | 4,707,129.24 USD | `STANDARD` | `+0.28%` | `0xecb63caa47` |
| `SELL` | `8.21` | `366.8200` | 3,010.64 USD | 4,732,977.70 USD | `STANDARD` | `+0.26%` | `0xdd4f66125d` |
| `SELL` | `8.21` | `321.8400` | 2,643.37 USD | 4,753,336.23 USD | `STANDARD` | `+0.33%` | `0xecb63caa47` |
| `SELL` | `8.21` | `231.2300` | 1,899.14 USD | 4,812,696.19 USD | `STANDARD` | `+0.33%` | `0x9d732bed51` |
| `SELL` | `8.21` | `231.2300` | 1,898.19 USD | 4,814,594.38 USD | `STANDARD` | `+0.28%` | `0x9d732bed51` |
| `SELL` | `8.21` | `231.2300` | 1,897.24 USD | 4,816,491.62 USD | `STANDARD` | `+0.23%` | `0x9d732bed51` |
| `SELL` | `8.21` | `107.0800` | 878.96 USD | 4,854,913.34 USD | `STANDARD` | `+0.27%` | `0xd0956a1eba` |
| `SELL` | `8.21` | `107.0700` | 878.71 USD | 4,855,792.05 USD | `STANDARD` | `+0.25%` | `0xf30120f048` |
| `SELL` | `8.21` | `106.0600` | 870.77 USD | 4,901,275.40 USD | `STANDARD` | `+0.29%` | `0x53136b4a7c` |
| `SELL` | `8.21` | `106.0600` | 870.72 USD | 4,902,146.12 USD | `STANDARD` | `+0.29%` | `0xf30120f048` |
| `SELL` | `8.21` | `106.0600` | 870.54 USD | 4,903,016.66 USD | `STANDARD` | `+0.27%` | `0xa382fa9f4b` |
| `SELL` | `8.21` | `106.0600` | 870.24 USD | 4,903,886.90 USD | `STANDARD` | `+0.23%` | `0xa382fa9f4b` |
| `SELL` | `8.21` | `106.0300` | 870.08 USD | 4,904,756.98 USD | `STANDARD` | `+0.24%` | `0xf30120f048` |
| `SELL` | `8.21` | `80.2900` | 658.96 USD | 4,947,153.54 USD | `STANDARD` | `+0.26%` | `0xea0e878d5d` |
| `SELL` | `8.21` | `79.5200` | 652.53 USD | 4,951,742.11 USD | `STANDARD` | `+0.24%` | `0xea0e878d5d` |
| `SELL` | `8.21` | `79.0200` | 648.81 USD | 4,953,691.35 USD | `STANDARD` | `+0.30%` | `0x31ca8395cf` |
| `SELL` | `8.21` | `78.7600` | 646.44 USD | 4,954,337.79 USD | `STANDARD` | `+0.26%` | `0x010461c14e` |
| `SELL` | `8.22` | `2285.0400` | 18,792.17 USD | 3,691,734.68 USD | `STANDARD` | `+0.46%` | `0xa38f19c4cc` |
| `SELL` | `8.22` | `1866.9900` | 15,355.06 USD | 3,880,072.01 USD | `STANDARD` | `+0.47%` | `0x57d8e75f47` |
| `SELL` | `8.22` | `1866.9900` | 15,350.58 USD | 3,895,422.59 USD | `STANDARD` | `+0.44%` | `0x57d8e75f47` |
| `SELL` | `8.22` | `1866.9900` | 15,343.67 USD | 3,910,766.26 USD | `STANDARD` | `+0.39%` | `0x57d8e75f47` |
| `SELL` | `8.22` | `1866.9900` | 15,338.82 USD | 3,926,105.08 USD | `STANDARD` | `+0.36%` | `0x57d8e75f47` |
| `SELL` | `8.22` | `1238.0600` | 10,176.98 USD | 4,375,781.10 USD | `STANDARD` | `+0.41%` | `0xd3342d3b1e` |
| `SELL` | `8.22` | `1000.9000` | 8,230.80 USD | 4,496,573.30 USD | `STANDARD` | `+0.45%` | `0xd3943e4008` |
| `SELL` | `8.22` | `869.6400` | 7,150.96 USD | 4,543,136.79 USD | `STANDARD` | `+0.45%` | `0x47a4471457` |
| `SELL` | `8.22` | `764.9000` | 6,285.49 USD | 4,582,467.16 USD | `STANDARD` | `+0.38%` | `0xecb63caa47` |
| `SELL` | `8.22` | `677.1700` | 5,565.73 USD | 4,600,248.16 USD | `STANDARD` | `+0.40%` | `0x33ad48ed92` |
| `SELL` | `8.22` | `610.1000` | 5,014.11 USD | 4,610,749.57 USD | `STANDARD` | `+0.39%` | `0x3ca146d269` |
| `SELL` | `8.22` | `467.8500` | 3,843.43 USD | 4,672,724.70 USD | `STANDARD` | `+0.35%` | `0x2a72b57dea` |
| `SELL` | `8.22` | `366.8200` | 3,014.82 USD | 4,726,952.97 USD | `STANDARD` | `+0.40%` | `0xdd4f66125d` |
| `SELL` | `8.22` | `366.8200` | 3,014.09 USD | 4,729,967.06 USD | `STANDARD` | `+0.37%` | `0xdd4f66125d` |
| `SELL` | `8.22` | `231.2300` | 1,901.03 USD | 4,808,896.96 USD | `STANDARD` | `+0.43%` | `0x9d732bed51` |
| `SELL` | `8.22` | `231.2300` | 1,900.09 USD | 4,810,797.05 USD | `STANDARD` | `+0.38%` | `0x9d732bed51` |
| `SELL` | `8.22` | `198.3300` | 1,630.59 USD | 4,825,368.18 USD | `STANDARD` | `+0.43%` | `0xfdba13d24c` |
| `SELL` | `8.23` | `1866.9900` | 15,372.98 USD | 3,833,992.46 USD | `STANDARD` | `+0.58%` | `0x57d8e75f47` |
| `SELL` | `8.23` | `1866.9900` | 15,364.39 USD | 3,849,356.85 USD | `STANDARD` | `+0.53%` | `0x57d8e75f47` |
| `SELL` | `8.23` | `1866.9900` | 15,360.10 USD | 3,864,716.95 USD | `STANDARD` | `+0.50%` | `0x57d8e75f47` |
| `SELL` | `8.23` | `1161.4100` | 9,557.71 USD | 4,454,479.86 USD | `STANDARD` | `+0.53%` | `0xd3943e4008` |
| `SELL` | `8.23` | `972.3600` | 7,999.99 USD | 4,512,573.30 USD | `STANDARD` | `+0.50%` | `0x0efb38a5fa` |
| `SELL` | `8.23` | `564.5200` | 4,647.92 USD | 4,635,304.47 USD | `STANDARD` | `+0.58%` | `0xcd7f60e943` |
| `SELL` | `8.23` | `244.5000` | 2,012.09 USD | 4,797,284.52 USD | `STANDARD` | `+0.53%` | `0x39bac00809` |
| `SELL` | `8.23` | `231.2300` | 1,903.88 USD | 4,803,191.02 USD | `STANDARD` | `+0.58%` | `0x9d732bed51` |
| `SELL` | `8.23` | `231.2300` | 1,902.93 USD | 4,805,093.95 USD | `STANDARD` | `+0.53%` | `0x9d732bed51` |
| `SELL` | `8.23` | `231.2300` | 1,901.98 USD | 4,806,995.93 USD | `STANDARD` | `+0.48%` | `0x9d732bed51` |
| `SELL` | `8.23` | `107.0700` | 881.41 USD | 4,849,628.70 USD | `STANDARD` | `+0.56%` | `0xa382fa9f4b` |
| `SELL` | `8.23` | `107.0700` | 881.34 USD | 4,850,510.04 USD | `STANDARD` | `+0.55%` | `0xf30120f048` |
| `SELL` | `8.23` | `107.0500` | 881.32 USD | 4,851,391.36 USD | `STANDARD` | `+0.57%` | `0x63f6411ca6` |
| `SELL` | `8.23` | `107.0700` | 881.11 USD | 4,852,272.47 USD | `STANDARD` | `+0.53%` | `0x9d81a3adf8` |
| `SELL` | `8.23` | `107.0600` | 880.98 USD | 4,853,153.45 USD | `STANDARD` | `+0.52%` | `0xfd66e33095` |
| `SELL` | `8.23` | `107.0800` | 880.94 USD | 4,854,034.38 USD | `STANDARD` | `+0.50%` | `0xfd66e33095` |
| `SELL` | `8.23` | `106.0600` | 873.30 USD | 4,890,808.02 USD | `STANDARD` | `+0.58%` | `0x63f6411ca6` |
| `SELL` | `8.23` | `106.0600` | 873.22 USD | 4,891,681.24 USD | `STANDARD` | `+0.57%` | `0xf30120f048` |
| `SELL` | `8.23` | `106.0600` | 872.98 USD | 4,892,554.22 USD | `STANDARD` | `+0.55%` | `0xfd66e33095` |
| `SELL` | `8.23` | `106.0600` | 872.57 USD | 4,893,426.79 USD | `STANDARD` | `+0.50%` | `0x9d81a3adf8` |
| `SELL` | `8.23` | `106.0600` | 872.48 USD | 4,894,299.27 USD | `STANDARD` | `+0.49%` | `0xa382fa9f4b` |
| `SELL` | `8.23` | `106.0600` | 872.47 USD | 4,895,171.74 USD | `STANDARD` | `+0.49%` | `0x9d81a3adf8` |
| `SELL` | `8.23` | `90.8600` | 747.81 USD | 4,935,217.41 USD | `STANDARD` | `+0.54%` | `0x31ca8395cf` |
| `SELL` | `8.23` | `88.6100` | 729.10 USD | 4,936,685.06 USD | `STANDARD` | `+0.51%` | `0x010461c14e` |
| `SELL` | `8.23` | `80.3000` | 661.18 USD | 4,946,494.58 USD | `STANDARD` | `+0.58%` | `0xfd66e33095` |
| `SELL` | `8.23` | `79.5400` | 654.48 USD | 4,950,435.66 USD | `STANDARD` | `+0.51%` | `0xfd66e33095` |
| `SELL` | `8.24` | `20382.6700` | 167,869.63 USD | 1,468,569.83 USD | `LARGE (>= USD 100K)` | `+0.61%` | `0x71cfa5e263` |
| `SELL` | `8.24` | `15632.5100` | 128,807.19 USD | 2,352,431.46 USD | `LARGE (>= USD 100K)` | `+0.65%` | `0x71d0e11ebb` |
| `SELL` | `8.24` | `1866.9900` | 15,388.85 USD | 3,803,237.90 USD | `STANDARD` | `+0.69%` | `0x57d8e75f47` |
| `SELL` | `8.24` | `1866.9900` | 15,381.57 USD | 3,818,619.47 USD | `STANDARD` | `+0.64%` | `0x57d8e75f47` |
| `SELL` | `8.24` | `1003.0500` | 8,268.64 USD | 4,488,342.50 USD | `STANDARD` | `+0.70%` | `0x33ad48ed92` |
| `SELL` | `8.25` | `1866.9900` | 15,406.03 USD | 3,772,451.61 USD | `STANDARD` | `+0.80%` | `0x57d8e75f47` |
| `SELL` | `8.25` | `1866.9900` | 15,397.44 USD | 3,787,849.05 USD | `STANDARD` | `+0.74%` | `0x57d8e75f47` |
| `SELL` | `8.25` | `1300.1400` | 10,720.43 USD | 4,345,206.55 USD | `STANDARD` | `+0.72%` | `0xd3943e4008` |
| `SELL` | `8.26` | `18002.3800` | 148,753.67 USD | 1,932,616.94 USD | `LARGE (>= USD 100K)` | `+0.94%` | `0x71d0e11ebb` |
| `SELL` | `8.26` | `12124.2400` | 100,197.14 USD | 3,055,585.16 USD | `LARGE (>= USD 100K)` | `+0.95%` | `0x881cd92459` |
| `SELL` | `8.26` | `1866.9900` | 15,414.62 USD | 3,757,045.58 USD | `STANDARD` | `+0.86%` | `0x57d8e75f47` |
| `SELL` | `8.26` | `1453.5500` | 11,999.93 USD | 4,278,832.87 USD | `STANDARD` | `+0.85%` | `0x0efb38a5fa` |
| `SELL` | `8.26` | `87.7000` | 724.59 USD | 4,938,861.38 USD | `STANDARD` | `+0.93%` | `0x31ca8395cf` |
| `SELL` | `8.27` | `1516.7000` | 12,549.33 USD | 4,242,832.99 USD | `STANDARD` | `+1.07%` | `0xd3943e4008` |
| `SELL` | `8.27` | `300.0000` | 2,482.38 USD | 4,783,812.44 USD | `STANDARD` | `+1.08%` | `0x6abc111bd2` |
| `SELL` | `8.27` | `87.4500` | 722.98 USD | 4,939,584.36 USD | `STANDARD` | `+0.99%` | `0x010461c14e` |
| `SELL` | `8.28` | `7825.9700` | 64,831.12 USD | 3,404,781.42 USD | `MEDIUM (>= USD 25K)` | `+1.19%` | `0x71d0e11ebb` |
| `SELL` | `8.28` | `1716.8800` | 14,207.53 USD | 4,230,283.67 USD | `STANDARD` | `+1.09%` | `0xd3943e4008` |
| `SELL` | `8.28` | `1336.1900` | 11,058.04 USD | 4,301,751.74 USD | `STANDARD` | `+1.09%` | `0x33ad48ed92` |
| `SELL` | `8.28` | `424.3100` | 3,511.46 USD | 4,714,246.04 USD | `STANDARD` | `+1.09%` | `0xd2ccf2ebc5` |
| `SELL` | `8.28` | `363.7000` | 3,009.87 USD | 4,735,987.57 USD | `STANDARD` | `+1.09%` | `0xd2ccf2ebc5` |
| `SELL` | `8.28` | `315.7300` | 2,614.56 USD | 4,758,583.35 USD | `STANDARD` | `+1.16%` | `0x07fd993f0f` |
| `SELL` | `8.28` | `303.0800` | 2,508.20 USD | 4,776,330.12 USD | `STANDARD` | `+1.09%` | `0xd2ccf2ebc5` |
| `SELL` | `8.28` | `242.4600` | 2,006.53 USD | 4,799,291.04 USD | `STANDARD` | `+1.09%` | `0xd2ccf2ebc5` |
| `SELL` | `8.29` | `39867.8600` | 330,420.84 USD | 977,001.98 USD | `LARGE (>= USD 100K)` | `+1.24%` | `0x71cfa5e263` |
| `SELL` | `8.29` | `1929.6100` | 15,999.94 USD | 3,741,630.97 USD | `STANDARD` | `+1.29%` | `0x0efb38a5fa` |
| `SELL` | `8.29` | `545.5500` | 4,520.75 USD | 4,644,423.07 USD | `STANDARD` | `+1.23%` | `0xd2ccf2ebc5` |
| `SELL` | `8.29` | `484.9300` | 4,018.42 USD | 4,660,995.71 USD | `STANDARD` | `+1.23%` | `0xd2ccf2ebc5` |
| `SELL` | `8.30` | `4868.5300` | 40,421.46 USD | 3,508,465.12 USD | `MEDIUM (>= USD 25K)` | `+1.42%` | `0xa24c5ca26c` |
| `SELL` | `8.30` | `500.0000` | 4,147.90 USD | 4,656,977.29 USD | `STANDARD` | `+1.34%` | `0x7b40d5c17a` |
| `SELL` | `8.31` | `2286.1500` | 18,999.96 USD | 3,635,218.61 USD | `STANDARD` | `+1.52%` | `0x0efb38a5fa` |
| `SELL` | `8.31` | `206.0400` | 1,711.59 USD | 4,823,737.59 USD | `STANDARD` | `+1.48%` | `0x010461c14e` |
| `SELL` | `8.31` | `179.2200` | 1,488.71 USD | 4,831,579.37 USD | `STANDARD` | `+1.47%` | `0x31ca8395cf` |
| `SELL` | `8.32` | `17961.1700` | 149,418.97 USD | 1,783,863.27 USD | `LARGE (>= USD 100K)` | `+1.62%` | `0x71d0e11ebb` |
| `SELL` | `8.32` | `2276.3200` | 18,931.70 USD | 3,654,150.31 USD | `STANDARD` | `+1.59%` | `0xd3943e4008` |
| `SELL` | `8.34` | `315.7300` | 2,632.56 USD | 4,755,968.79 USD | `STANDARD` | `+1.85%` | `0x07fd993f0f` |
| `SELL` | `8.35` | `77461.7700` | 646,581.14 USD | 646,581.14 USD | `LARGE (>= USD 100K)` | `+1.96%` | `0x71cfa5e263` |
| `SELL` | `8.35` | `78.7000` | 657.07 USD | 4,948,469.01 USD | `STANDARD` | `+1.99%` | `0xdd7587742e` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:28:02 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1502` | `0x7737...bf66` | `SHORT` | 1,406,600.74 USD | `171,568.06` | `7.43` | `8.21` | `103.14` | -131,055.72 USD | `-9.32%` | `10X Cross` |
| `1586` | `0xeadc...9d55` | `LONG` | 1,312,338.49 USD | `160,070.56` | `8.11` | `8.21` | `0.000000` | 14,700.91 USD | `+1.12%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `8.94` | 10,136.93 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 10.14K USD at 8.9443 USD [API] | `2026-10-28 19:39:23` |
| `ANNOUNCEMENT` | `INFO` | `9.03` | 10,191.71 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 10.19K USD at 9.0280 USD [API] | `2026-10-28 19:56:24` |
| `ANNOUNCEMENT` | `INFO` | `9.01` | 13,483.75 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 13.48K USD at 9.0123 USD [API] | `2026-10-28 22:45:26` |


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
| `Live` | `Long Liquidation` | `1.68` | 788.62 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 702.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.76` | 194.15 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 2,540.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 208.88 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 234.37 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 212.85 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 598.85 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 13,480.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 159.60 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 8,700.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 164.15 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 814.80 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 275.55 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 150.77 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 19,330.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 147.42 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 762.99 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 122.53 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 534.93 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 3,560.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 1,360.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 233.53 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.79` | 948.75 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 159.29 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.17` | 438.38 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.18` | 174.89 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 806.51 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.29` | 8,590.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.30` | 2,870.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.37` | 188.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 110.77 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.61` | 525.43 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 486.93 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 2,680.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.64` | 433.47 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,380.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,340.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.88` | 18,460.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 489.50 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 3,880.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 115.54 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 4,430.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 213.56 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 167.78 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 314.59 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 736.47 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 318.46 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.11` | 529.54 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.16` | 119.60 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 5,610.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 2,250.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 1,050.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 161,490.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 1,230.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 20,160.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.51` | 367.41 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 121.38 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 2,760.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.59` | 35,940.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 468.55 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.64` | 229.24 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.72` | 2,390.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 238.86 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 2,890.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 736.72 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 696.60 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.83` | 145.88 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.84` | 561.53 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.86` | 2,110.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 984.70 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.92` | 277.35 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.93` | 147.19 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.99` | 447.98 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 331.68 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 105.61 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 405.14 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,130.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 1,140.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 2,160.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 4,390.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.24` | 300.65 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 2,410.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 972.65 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.32` | 277.04 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 348,420.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 11,550.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 3,830.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 1,980.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 2,510.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.47` | 362,980.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 3,620.00 USD | 797,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 794,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.57` | 1,530.00 USD | 785,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 537.37 USD | 783,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 1,770.00 USD | 783,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.59` | 1,100.00 USD | 781,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 780,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 364.90 USD | 778,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.67` | 1,640.00 USD | 777,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.70` | 1,700.00 USD | 776,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 16,070.00 USD | 774,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 6,180.00 USD | 758,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 752,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 6,780.00 USD | 751,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 16,960.00 USD | 744,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 4,930.00 USD | 727,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 722,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 2,670.00 USD | 720,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 158.14 USD | 718,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 4,410.00 USD | 718,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.86` | 19,810.00 USD | 713,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 693,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 1,580.00 USD | 690,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.91` | 269.30 USD | 688,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,760.00 USD | 688,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 3,480.00 USD | 684,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 681,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.97` | 2,810.00 USD | 680,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.99` | 1,100.00 USD | 677,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 746.58 USD | 676,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 20,860.00 USD | 676,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.01` | 281.86 USD | 655,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.03` | 1,370.00 USD | 654,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.04` | 704.50 USD | 653,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 354.23 USD | 652,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.07` | 1,260.00 USD | 652,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 651,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,420.00 USD | 644,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.09` | 3,020.00 USD | 643,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,230.00 USD | 640,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 611,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 777.50 USD | 611,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,270.00 USD | 610,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.16` | 2,370.00 USD | 590,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.17` | 215.59 USD | 588,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.17` | 1,440.00 USD | 587,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 586,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 7,950.00 USD | 585,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 29,440.00 USD | 577,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.24` | 179.65 USD | 547,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 547,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 21,280.00 USD | 547,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.26` | 419.41 USD | 525,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 38,110.00 USD | 525,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 4,910.00 USD | 487,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 4,370.00 USD | 482,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.36` | 3,590,000.00 USD | 3,590,000.00 USD | 6,810.00 USD | 2,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.37` | 6,420.00 USD | 478,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 5,020.00 USD | 471,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 13,200.00 USD | 466,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.39` | 1,550.00 USD | 453,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.40` | 3,580,000.00 USD | 3,580,000.00 USD | 6,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 338.94 USD | 452,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.42` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 48.44 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 147.61 USD | 451,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 2,880.00 USD | 451,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.44` | 3,230,000.00 USD | 3,230,000.00 USD | 196.00 USD | 0.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.44` | 3,570,000.00 USD | 3,570,000.00 USD | 331.70 USD | 1,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.45` | 210.99 USD | 448,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 1,620.00 USD | 448,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.46` | 3,210,000.00 USD | 3,210,000.00 USD | 7,860.00 USD | 0.00 USD | 52,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.46` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 1,410.00 USD | 24,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 446,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 1,120.00 USD | 442,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.48` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.48` | 3,540,000.00 USD | 3,540,000.00 USD | 9,120.00 USD | 0.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.49` | 1,050.00 USD | 441,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 962.81 USD | 440,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.50` | 3,130,000.00 USD | 3,130,000.00 USD | 717.40 USD | 4,920.00 USD | 24,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 421.78 USD | 439,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.52` | 3,110,000.00 USD | 3,110,000.00 USD | 26,110.00 USD | 9,580.00 USD | 36,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.52` | 3,520,000.00 USD | 3,520,000.00 USD | 1,150.00 USD | 14,470.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 438,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.54` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 4,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.54` | 1,510.00 USD | 434,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 572.67 USD | 432,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.56` | 3,030,000.00 USD | 3,030,000.00 USD | 15,020.00 USD | 4,270.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.56` | 3,480,000.00 USD | 3,480,000.00 USD | 19,530.00 USD | 4,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.57` | 25,060.00 USD | 432,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 118.25 USD | 407,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.58` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 147.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.59` | 24,760.00 USD | 407,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.60` | 3,010,000.00 USD | 3,010,000.00 USD | 405.20 USD | 3,770.00 USD | 194.10 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.61` | 1,520.00 USD | 382,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 878.24 USD | 380,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 3,010,000.00 USD | 3,010,000.00 USD | 583.80 USD | 0.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 380,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 379,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 2,990,000.00 USD | 2,990,000.00 USD | 17,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.64` | 3,450,000.00 USD | 3,450,000.00 USD | 812.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 1,410.00 USD | 378,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.66` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 9,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.66` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 23,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 1,740.00 USD | 377,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.67` | 1,890.00 USD | 375,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.68` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.68` | 1,120.00 USD | 373,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.70` | 1,460.00 USD | 372,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 2,970,000.00 USD | 2,970,000.00 USD | 321.75 USD | 2,390.00 USD | 14,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.72` | 2,950,000.00 USD | 2,950,000.00 USD | 4,600.00 USD | 1,630.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.72` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.74` | 2,930,000.00 USD | 2,930,000.00 USD | 3,340.00 USD | 4,580.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.74` | 3,390,000.00 USD | 3,390,000.00 USD | 976.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.76` | 2,920,000.00 USD | 2,920,000.00 USD | 1,660.00 USD | 1,100.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.76` | 3,390,000.00 USD | 3,390,000.00 USD | 812.95 USD | 5,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 371,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.78` | 695.32 USD | 370,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 2,910,000.00 USD | 2,910,000.00 USD | 44,950.00 USD | 3,730.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.78` | 3,380,000.00 USD | 3,380,000.00 USD | 43,620.00 USD | 4,900.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 2,870.00 USD | 370,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 12,800.00 USD | 367,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 2,850,000.00 USD | 2,850,000.00 USD | 39,070.00 USD | 10,860.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.80` | 3,310,000.00 USD | 3,310,000.00 USD | 14,770.00 USD | 12,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.82` | 3,130.00 USD | 354,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.82` | 2,800,000.00 USD | 2,800,000.00 USD | 5,100.00 USD | 7,610.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.82` | 3,280,000.00 USD | 3,280,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.84` | 2,780,000.00 USD | 2,780,000.00 USD | 2,680.00 USD | 4,910.00 USD | 12,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 3,270,000.00 USD | 3,270,000.00 USD | 30,950.00 USD | 2,380.00 USD | 25,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 24,340.00 USD | 351,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.86` | 2,760,000.00 USD | 2,760,000.00 USD | 15,790.00 USD | 1,680.00 USD | 16,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.86` | 3,210,000.00 USD | 3,210,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 326,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 2,720,000.00 USD | 2,720,000.00 USD | 46,100.00 USD | 9,570.00 USD | 22,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.88` | 3,160,000.00 USD | 3,160,000.00 USD | 58,120.00 USD | 12,780.00 USD | 29,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.90` | 2,650,000.00 USD | 2,650,000.00 USD | 14,350.00 USD | 7,630.00 USD | 7,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 3,060,000.00 USD | 3,060,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 505.13 USD | 326,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.92` | 2,620,000.00 USD | 2,620,000.00 USD | 24,660.00 USD | 2,950.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.92` | 3,000,000.00 USD | 3,000,000.00 USD | 55,490.00 USD | 8,420.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 16,340.00 USD | 325,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 2,580,000.00 USD | 2,580,000.00 USD | 20,330.00 USD | 6,860.00 USD | 48,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.94` | 2,920,000.00 USD | 2,920,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 309,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.96` | 4,090.00 USD | 182,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 2,510,000.00 USD | 2,510,000.00 USD | 20,670.00 USD | 11,220.00 USD | 149,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.96` | 2,830,000.00 USD | 2,830,000.00 USD | 21,840.00 USD | 6,920.00 USD | 86,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 4,520.00 USD | 178,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.97` | 10,990.00 USD | 173,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.98` | 2,330,000.00 USD | 2,330,000.00 USD | 17,030.00 USD | 3,300.00 USD | 37,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.98` | 2,710,000.00 USD | 2,710,000.00 USD | 56,660.00 USD | 26,790.00 USD | 146,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 17,430.00 USD | 162,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.00` | 2,740.00 USD | 145,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 2,270,000.00 USD | 2,270,000.00 USD | 1,500.00 USD | 22,850.00 USD | 62,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.00` | 2,480,000.00 USD | 2,480,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.01` | 284.42 USD | 142,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.02` | 235.80 USD | 142,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.02` | 2,180,000.00 USD | 2,180,000.00 USD | 81,330.00 USD | 10,580.00 USD | 82,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.02` | 2,400,000.00 USD | 2,400,000.00 USD | 20,910.00 USD | 46,670.00 USD | 56,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 957.70 USD | 142,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.04` | 89,210.00 USD | 141,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.04` | 2,010,000.00 USD | 2,010,000.00 USD | 33,700.00 USD | 17,810.00 USD | 15,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.04` | 2,280,000.00 USD | 2,280,000.00 USD | 152,340.00 USD | 56,910.00 USD | 86,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 10,430.00 USD | 51,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 1,370.00 USD | 41,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.06` | 1,940,000.00 USD | 1,940,000.00 USD | 76,840.00 USD | 22,300.00 USD | 19,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.06` | 1,980,000.00 USD | 1,980,000.00 USD | 122,100.00 USD | 20,850.00 USD | 86,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 4,380.00 USD | 40,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.07` | 232.96 USD | 35,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.08` | 1,820,000.00 USD | 1,820,000.00 USD | 36,720.00 USD | 6,070.00 USD | 13,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.08` | 1,760,000.00 USD | 1,760,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 3,420.00 USD | 35,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.10` | 886.24 USD | 32,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.10` | 1,770,000.00 USD | 1,770,000.00 USD | 30,110.00 USD | 14,390.00 USD | 96,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.10` | 1,720,000.00 USD | 1,720,000.00 USD | 61,500.00 USD | 19,700.00 USD | 15,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.11` | 6,000.00 USD | 31,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.12` | 241.26 USD | 25,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 1,620,000.00 USD | 1,620,000.00 USD | 110,990.00 USD | 12,270.00 USD | 319,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.12` | 1,620,000.00 USD | 1,620,000.00 USD | 27,520.00 USD | 10,810.00 USD | 142,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 843.86 USD | 25,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.13` | 855.64 USD | 24,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.14` | 1,180,000.00 USD | 1,180,000.00 USD | 12,410.00 USD | 0.00 USD | 58,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.14` | 1,440,000.00 USD | 1,440,000.00 USD | 72,460.00 USD | 25,370.00 USD | 192,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 1,110,000.00 USD | 1,110,000.00 USD | 44,830.00 USD | 42,030.00 USD | 159,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 1,150,000.00 USD | 1,150,000.00 USD | 38,430.00 USD | 5,510.00 USD | 30,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.16` | 871.61 USD | 23,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.18` | 864,670.00 USD | 864,670.00 USD | 133,120.00 USD | 19,620.00 USD | 175,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 1,080,000.00 USD | 1,080,000.00 USD | 39,830.00 USD | 43,260.00 USD | 176,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.20` | 8,590.00 USD | 22,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.20` | 535,970.00 USD | 535,970.00 USD | 33,560.00 USD | 32,530.00 USD | 17,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.20` | 817,140.00 USD | 817,140.00 USD | 92,320.00 USD | 58,100.00 USD | 8,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 1,910.00 USD | 13,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.21` | 147.87 USD | 11,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.22` | 452,680.00 USD | 452,680.00 USD | 32,330.00 USD | 39,650.00 USD | 35,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.22` | 658,310.00 USD | 658,310.00 USD | 117,230.00 USD | 21,570.00 USD | 10,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.22` | 2,100.00 USD | 11,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.24` | 345,380.00 USD | 345,380.00 USD | 163,080.00 USD | 10,300.00 USD | 69,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 508,550.00 USD | 508,550.00 USD | 39,950.00 USD | 3,480.00 USD | 107,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.26` | 9,710.00 USD | 9,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `Short Liquidation` | `8.52` | 1,240,000.00 USD | 1,240,000.00 USD | 203,080.00 USD | 69,980.00 USD | 164,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.52` | 1,150,000.00 USD | 1,150,000.00 USD | 2,990.00 USD | 135,400.00 USD | 91,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.54` | 1,350,000.00 USD | 1,350,000.00 USD | 61,500.00 USD | 32,530.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.54` | 1,360,000.00 USD | 1,360,000.00 USD | 71,540.00 USD | 136,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.56` | 1,570,000.00 USD | 1,570,000.00 USD | 183,280.00 USD | 33,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.56` | 2,180,000.00 USD | 2,180,000.00 USD | 691,140.00 USD | 122,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.58` | 1,990,000.00 USD | 1,990,000.00 USD | 234,090.00 USD | 5,060.00 USD | 179,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.58` | 2,940,000.00 USD | 2,940,000.00 USD | 599,490.00 USD | 164,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.60` | 2,350.00 USD | 2,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.60` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 57,190.00 USD | 120,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.60` | 3,060,000.00 USD | 3,060,000.00 USD | 75,040.00 USD | 39,160.00 USD | 388.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.62` | 2,510,000.00 USD | 2,510,000.00 USD | 83,560.00 USD | 57,150.00 USD | 201,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.62` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 43,670.00 USD | 87,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 2,660,000.00 USD | 2,660,000.00 USD | 89,460.00 USD | 30,330.00 USD | 29,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.64` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 12,800.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.66` | 2,870,000.00 USD | 2,870,000.00 USD | 78,620.00 USD | 21,010.00 USD | 108,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.66` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 16,520.00 USD | 281.77 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 3,150,000.00 USD | 3,150,000.00 USD | 65,090.00 USD | 9,810.00 USD | 212,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.68` | 3,880,000.00 USD | 3,880,000.00 USD | 207,090.00 USD | 43,100.00 USD | 334,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.70` | 3,250,000.00 USD | 3,250,000.00 USD | 50,130.00 USD | 16,260.00 USD | 30,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.70` | 3,990,000.00 USD | 3,990,000.00 USD | 29,260.00 USD | 41,840.00 USD | 46,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 3,320,000.00 USD | 3,320,000.00 USD | 18,250.00 USD | 0.00 USD | 50,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 3,410,000.00 USD | 3,410,000.00 USD | 49,310.00 USD | 28,810.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.74` | 4,070,000.00 USD | 4,070,000.00 USD | 48,810.00 USD | 30,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.76` | 373.93 USD | 2,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.76` | 3,540,000.00 USD | 3,540,000.00 USD | 112,960.00 USD | 2,530.00 USD | 9,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.76` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.78` | 1,230.00 USD | 3,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.78` | 3,690,000.00 USD | 3,690,000.00 USD | 108,350.00 USD | 11,500.00 USD | 35,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.78` | 4,160,000.00 USD | 4,160,000.00 USD | 2,300.00 USD | 0.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.80` | 3,890,000.00 USD | 3,890,000.00 USD | 125,120.00 USD | 22,330.00 USD | 52,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.80` | 4,250,000.00 USD | 4,250,000.00 USD | 27,360.00 USD | 33,750.00 USD | 31,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.82` | 3,910,000.00 USD | 3,910,000.00 USD | 19,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.82` | 4,350,000.00 USD | 4,350,000.00 USD | 103,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.82` | 6,000.00 USD | 9,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.84` | 541.67 USD | 10,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `9.06` | 434.94 USD | 10,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `9.19` | 1,590.00 USD | 12,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.20` | 6,740,000.00 USD | 6,740,000.00 USD | 141,410.00 USD | 43,540.00 USD | 51,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 11,270,000.00 USD | 11,270,000.00 USD | 549,250.00 USD | 134,550.00 USD | 238,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.21` | 1,870.00 USD | 14,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.22` | 6,850,000.00 USD | 6,850,000.00 USD | 86,390.00 USD | 10,580.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.22` | 12,410,000.00 USD | 12,410,000.00 USD | 585,170.00 USD | 144,840.00 USD | 417,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 6,910,000.00 USD | 6,910,000.00 USD | 47,010.00 USD | 4,270.00 USD | 3,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 12,980,000.00 USD | 12,980,000.00 USD | 335,740.00 USD | 56,410.00 USD | 173,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 6,960,000.00 USD | 6,960,000.00 USD | 35,150.00 USD | 8,290.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 13,410,000.00 USD | 13,410,000.00 USD | 273,920.00 USD | 96,980.00 USD | 61,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 7,020,000.00 USD | 7,020,000.00 USD | 44,530.00 USD | 10,920.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 14,110,000.00 USD | 14,110,000.00 USD | 428,160.00 USD | 103,490.00 USD | 170,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 100.93 USD | 14,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `9.40` | 28,220.00 USD | 42,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.41` | 440.06 USD | 43,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 7,450,000.00 USD | 7,450,000.00 USD | 10,810.00 USD | 2,390.00 USD | 14,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.42` | 17,290,000.00 USD | 17,290,000.00 USD | 176,920.00 USD | 19,780.00 USD | 71,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 7,480,000.00 USD | 7,480,000.00 USD | 10,560.00 USD | 1,630.00 USD | 12,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 17,410,000.00 USD | 17,410,000.00 USD | 41,250.00 USD | 19,420.00 USD | 56,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.46` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 4,580.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 17,520,000.00 USD | 17,520,000.00 USD | 60,020.00 USD | 29,830.00 USD | 19,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.48` | 17,580,000.00 USD | 17,580,000.00 USD | 12,180.00 USD | 27,840.00 USD | 26,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 17,750,000.00 USD | 17,750,000.00 USD | 89,460.00 USD | 33,210.00 USD | 45,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 17,940,000.00 USD | 17,940,000.00 USD | 102,150.00 USD | 29,320.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 18,150,000.00 USD | 18,150,000.00 USD | 192,090.00 USD | 25,090.00 USD | 378.07 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 18,260,000.00 USD | 18,260,000.00 USD | 88,510.00 USD | 5,260.00 USD | 13,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 18,340,000.00 USD | 18,340,000.00 USD | 35,340.00 USD | 14,530.00 USD | 26,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 18,400,000.00 USD | 18,400,000.00 USD | 38,740.00 USD | 5,460.00 USD | 20,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 18,480,000.00 USD | 18,480,000.00 USD | 70,470.00 USD | 1,540.00 USD | 10,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.62` | 253.04 USD | 43,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.64` | 18,560,000.00 USD | 18,560,000.00 USD | 35,210.00 USD | 17,650.00 USD | 20,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.64` | 1,930.00 USD | 45,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.66` | 18,630,000.00 USD | 18,630,000.00 USD | 37,340.00 USD | 21,280.00 USD | 17,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.68` | 18,740,000.00 USD | 18,740,000.00 USD | 68,230.00 USD | 20,310.00 USD | 15,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.70` | 929.65 USD | 46,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.70` | 18,860,000.00 USD | 18,860,000.00 USD | 77,860.00 USD | 12,990.00 USD | 31,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.72` | 18,960,000.00 USD | 18,960,000.00 USD | 70,300.00 USD | 6,920.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 46,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `10.11` | 568.81 USD | 47,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.12` | 487.01 USD | 47,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.18` | 249,590.00 USD | 297,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.21` | 3,230.00 USD | 300,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.32` | 258,130.00 USD | 558,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 2,650.00 USD | 561,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 561,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.71` | 218.91 USD | 561,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.93` | 117.23 USD | 561,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.96` | 1,920.00 USD | 563,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 570,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.22` | 112,250.00 USD | 683,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,670.00 USD | 694,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 706,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.69` | 296,760.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.74` | 40,670.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.93` | 505.74 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,050.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.96` | 59,780.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.04` | 802.20 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.04` | 444.49 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.18` | 40,820.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.31` | 282.43 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 237.04 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.46` | 16,190.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.71` | 5,160.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.77` | 4,100.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.90` | 321.20 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.27` | 2,540.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 484.60 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.64` | 9,180.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.32` | 22,420.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.32` | 116.07 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.38` | 265,410.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.69` | 2,290,000.00 USD | 0.00 USD | 793.33 USD | `-79.48%` | `470.82` |
| `Live` | `Long` | `1.74` | 2,280,000.00 USD | 0.00 USD | 1,120.00 USD | `-78.87%` | `647.30` |
| `Live` | `Long` | `1.95` | 2,280,000.00 USD | 0.00 USD | 439.20 USD | `-76.32%` | `225.81` |
| `Live` | `Long` | `2.00` | 2,280,000.00 USD | 0.00 USD | 159.60 USD | `-75.71%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,280,000.00 USD | 0.00 USD | 110.52 USD | `-75.22%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,280,000.00 USD | 0.00 USD | 4,920.00 USD | `-74.86%` | `2,382.76` |
| `Live` | `Long` | `2.27` | 2,280,000.00 USD | 0.00 USD | 536.24 USD | `-72.42%` | `236.75` |
| `Live` | `Long` | `2.33` | 2,280,000.00 USD | 0.00 USD | 267.38 USD | `-71.69%` | `115.00` |
| `Live` | `Long` | `2.35` | 2,280,000.00 USD | 0.00 USD | 725.08 USD | `-71.32%` | `307.89` |
| `Live` | `Long` | `2.42` | 2,280,000.00 USD | 0.00 USD | 278.88 USD | `-70.47%` | `115.00` |
| `Live` | `Long` | `2.48` | 2,280,000.00 USD | 0.00 USD | 907.07 USD | `-69.74%` | `365.02` |
| `Live` | `Long` | `2.69` | 2,270,000.00 USD | 0.00 USD | 2,020.00 USD | `-67.31%` | `751.75` |
| `Live` | `Long` | `2.71` | 2,270,000.00 USD | 0.00 USD | 134.22 USD | `-67.06%` | `49.62` |
| `Live` | `Long` | `2.71` | 2,270,000.00 USD | 0.00 USD | 190.05 USD | `-66.94%` | `70.00` |
| `Live` | `Long` | `2.87` | 2,270,000.00 USD | 0.00 USD | 232.67 USD | `-65.11%` | `81.21` |
| `Live` | `Long` | `2.94` | 2,270,000.00 USD | 0.00 USD | 44,510.00 USD | `-64.26%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,230,000.00 USD | 0.00 USD | 111.12 USD | `-63.77%` | `37.35` |
| `Live` | `Long` | `2.98` | 2,230,000.00 USD | 0.00 USD | 343.28 USD | `-63.65%` | `115.00` |
| `Live` | `Long` | `3.04` | 2,230,000.00 USD | 0.00 USD | 578.52 USD | `-62.92%` | `189.99` |
| `Live` | `Long` | `3.23` | 2,230,000.00 USD | 0.00 USD | 368.55 USD | `-60.73%` | `114.28` |
| `Live` | `Long` | `3.23` | 2,230,000.00 USD | 0.00 USD | 102.45 USD | `-60.61%` | `31.67` |
| `Live` | `Long` | `3.29` | 2,230,000.00 USD | 0.00 USD | 22,960.00 USD | `-60.00%` | `6,990.57` |
| `Live` | `Long` | `3.29` | 2,200,000.00 USD | 0.00 USD | 171.34 USD | `-59.88%` | `52.00` |
| `Live` | `Long` | `3.33` | 2,200,000.00 USD | 0.00 USD | 111.42 USD | `-59.51%` | `33.51` |
| `Live` | `Long` | `3.35` | 2,200,000.00 USD | 0.00 USD | 24,970.00 USD | `-59.27%` | `7,465.11` |
| `Live` | `Long` | `3.37` | 2,180,000.00 USD | 0.00 USD | 389.53 USD | `-59.03%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,180,000.00 USD | 0.00 USD | 4,500.00 USD | `-58.90%` | `1,333.03` |
| `Live` | `Long` | `3.67` | 2,170,000.00 USD | 0.00 USD | 109.95 USD | `-55.37%` | `30.00` |
| `Live` | `Long` | `3.75` | 2,170,000.00 USD | 0.00 USD | 175.79 USD | `-54.40%` | `46.94` |
| `Live` | `Long` | `3.75` | 2,170,000.00 USD | 0.00 USD | 1,500.00 USD | `-54.28%` | `400.00` |
| `Live` | `Long` | `3.79` | 2,170,000.00 USD | 0.00 USD | 1,560.00 USD | `-53.91%` | `412.71` |
| `Live` | `Long` | `3.90` | 2,170,000.00 USD | 0.00 USD | 562.67 USD | `-52.57%` | `144.46` |
| `Live` | `Long` | `4.03` | 2,170,000.00 USD | 0.00 USD | 402.70 USD | `-50.99%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,170,000.00 USD | 0.00 USD | 152.29 USD | `-50.75%` | `37.65` |
| `Live` | `Long` | `4.07` | 2,170,000.00 USD | 0.00 USD | 511.58 USD | `-50.50%` | `125.85` |
| `Live` | `Long` | `4.11` | 2,170,000.00 USD | 0.00 USD | 1,640.00 USD | `-50.02%` | `400.00` |
| `Live` | `Long` | `4.13` | 2,170,000.00 USD | 0.00 USD | 673.34 USD | `-49.65%` | `162.84` |
| `Live` | `Long` | `4.14` | 2,170,000.00 USD | 0.00 USD | 159.29 USD | `-49.53%` | `38.43` |
| `Live` | `Long` | `4.16` | 2,170,000.00 USD | 0.00 USD | 208.41 USD | `-49.41%` | `50.16` |
| `Live` | `Long` | `4.18` | 2,170,000.00 USD | 0.00 USD | 174.89 USD | `-49.04%` | `41.79` |
| `Live` | `Long` | `4.21` | 2,170,000.00 USD | 0.00 USD | 194.57 USD | `-48.80%` | `46.27` |
| `Live` | `Long` | `4.24` | 2,170,000.00 USD | 0.00 USD | 169.40 USD | `-48.43%` | `40.00` |
| `Live` | `Long` | `4.45` | 2,170,000.00 USD | 0.00 USD | 110.77 USD | `-45.88%` | `24.92` |
| `Live` | `Long` | `4.50` | 2,160,000.00 USD | 0.00 USD | 17,940.00 USD | `-45.14%` | `3,981.48` |
| `Live` | `Long` | `4.59` | 2,150,000.00 USD | 0.00 USD | 30,970.00 USD | `-44.05%` | `6,740.93` |
| `Live` | `Long` | `4.61` | 2,120,000.00 USD | 0.00 USD | 429.74 USD | `-43.93%` | `93.32` |
| `Live` | `Long` | `4.62` | 2,120,000.00 USD | 0.00 USD | 486.93 USD | `-43.81%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,120,000.00 USD | 0.00 USD | 2,930.00 USD | `-43.68%` | `634.06` |
| `Live` | `Long` | `4.63` | 2,110,000.00 USD | 0.00 USD | 3,090.00 USD | `-43.56%` | `666.20` |
| `Live` | `Long` | `4.66` | 2,110,000.00 USD | 0.00 USD | 105.11 USD | `-43.32%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,110,000.00 USD | 0.00 USD | 3,280.00 USD | `-43.20%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,110,000.00 USD | 0.00 USD | 1,490.00 USD | `-43.07%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,100,000.00 USD | 0.00 USD | 8,380.00 USD | `-42.95%` | `1,787.97` |
| `Live` | `Long` | `4.70` | 2,100,000.00 USD | 0.00 USD | 7,040.00 USD | `-42.83%` | `1,500.00` |
| `Live` | `Long` | `4.71` | 2,090,000.00 USD | 0.00 USD | 517.55 USD | `-42.71%` | `110.00` |
| `Live` | `Long` | `4.76` | 2,090,000.00 USD | 0.00 USD | 105.64 USD | `-41.98%` | `22.17` |
| `Live` | `Long` | `4.83` | 2,090,000.00 USD | 0.00 USD | 467.01 USD | `-41.13%` | `96.59` |
| `Live` | `Long` | `4.88` | 2,090,000.00 USD | 0.00 USD | 2,440.00 USD | `-40.64%` | `500.00` |
| `Live` | `Long` | `4.89` | 2,090,000.00 USD | 0.00 USD | 16,080.00 USD | `-40.40%` | `3,286.00` |
| `Live` | `Long` | `4.91` | 2,070,000.00 USD | 0.00 USD | 3,880.00 USD | `-40.27%` | `790.61` |
| `Live` | `Long` | `4.92` | 2,070,000.00 USD | 0.00 USD | 1,230.00 USD | `-40.15%` | `251.00` |
| `Live` | `Long` | `4.96` | 2,060,000.00 USD | 0.00 USD | 945.36 USD | `-39.67%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,060,000.00 USD | 0.00 USD | 4,430.00 USD | `-39.54%` | `893.25` |
| `Live` | `Long` | `4.97` | 2,060,000.00 USD | 0.00 USD | 282.23 USD | `-39.42%` | `56.73` |
| `Live` | `Long` | `5.01` | 2,060,000.00 USD | 0.00 USD | 56,390.00 USD | `-38.93%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,000,000.00 USD | 0.00 USD | 384.21 USD | `-38.81%` | `76.46` |
| `Live` | `Long` | `5.04` | 2,000,000.00 USD | 0.00 USD | 314.59 USD | `-38.69%` | `62.48` |
| `Live` | `Long` | `5.05` | 2,000,000.00 USD | 0.00 USD | 504.74 USD | `-38.45%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,000,000.00 USD | 0.00 USD | 318.46 USD | `-38.20%` | `62.75` |
| `Live` | `Long` | `5.08` | 2,000,000.00 USD | 0.00 USD | 965.84 USD | `-38.08%` | `189.94` |
| `Live` | `Long` | `5.09` | 2,000,000.00 USD | 0.00 USD | 651.75 USD | `-37.96%` | `127.92` |
| `Live` | `Long` | `5.12` | 2,000,000.00 USD | 0.00 USD | 915.43 USD | `-37.72%` | `178.97` |
| `Live` | `Long` | `5.12` | 2,000,000.00 USD | 0.00 USD | 250.20 USD | `-37.60%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,000,000.00 USD | 0.00 USD | 396.06 USD | `-37.47%` | `77.13` |
| `Live` | `Long` | `5.16` | 2,000,000.00 USD | 0.00 USD | 752.53 USD | `-37.23%` | `145.98` |
| `Live` | `Long` | `5.17` | 2,000,000.00 USD | 0.00 USD | 1,620.00 USD | `-36.99%` | `312.94` |
| `Live` | `Long` | `5.18` | 2,000,000.00 USD | 0.00 USD | 150.57 USD | `-36.86%` | `29.04` |
| `Live` | `Long` | `5.20` | 1,990,000.00 USD | 0.00 USD | 480.07 USD | `-36.74%` | `92.41` |
| `Live` | `Long` | `5.21` | 1,990,000.00 USD | 0.00 USD | 300.91 USD | `-36.50%` | `57.70` |
| `Live` | `Long` | `5.25` | 1,990,000.00 USD | 0.00 USD | 6,580.00 USD | `-36.01%` | `1,253.00` |
| `Live` | `Long` | `5.26` | 1,990,000.00 USD | 0.00 USD | 2,230.00 USD | `-35.89%` | `423.54` |
| `Live` | `Long` | `5.29` | 1,990,000.00 USD | 0.00 USD | 640.70 USD | `-35.65%` | `121.23` |
| `Live` | `Long` | `5.32` | 1,980,000.00 USD | 0.00 USD | 628.18 USD | `-35.28%` | `118.19` |
| `Live` | `Long` | `5.33` | 1,980,000.00 USD | 0.00 USD | 716.11 USD | `-35.16%` | `134.48` |
| `Live` | `Long` | `5.34` | 1,980,000.00 USD | 0.00 USD | 162,680.00 USD | `-34.92%` | `30,435.20` |
| `Live` | `Long` | `5.38` | 1,820,000.00 USD | 0.00 USD | 517.23 USD | `-34.43%` | `96.05` |
| `Live` | `Long` | `5.39` | 1,820,000.00 USD | 0.00 USD | 660.46 USD | `-34.31%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,820,000.00 USD | 0.00 USD | 20,160.00 USD | `-34.06%` | `3,723.69` |
| `Live` | `Long` | `5.42` | 1,800,000.00 USD | 0.00 USD | 160,400.00 USD | `-33.94%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,640,000.00 USD | 0.00 USD | 1,360.00 USD | `-33.82%` | `250.00` |
| `Live` | `Long` | `5.45` | 1,640,000.00 USD | 0.00 USD | 10,890.00 USD | `-33.70%` | `2,000.00` |
| `Live` | `Long` | `5.46` | 1,630,000.00 USD | 0.00 USD | 264.72 USD | `-33.46%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,630,000.00 USD | 0.00 USD | 1,320.00 USD | `-33.33%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,630,000.00 USD | 0.00 USD | 354.06 USD | `-33.21%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,620,000.00 USD | 0.00 USD | 19,290.00 USD | `-33.09%` | `3,510.41` |
| `Live` | `Long` | `5.51` | 1,610,000.00 USD | 0.00 USD | 367.41 USD | `-32.85%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,610,000.00 USD | 0.00 USD | 121.38 USD | `-32.60%` | `21.93` |
| `Live` | `Long` | `5.54` | 1,600,000.00 USD | 0.00 USD | 2,760.00 USD | `-32.48%` | `497.70` |
| `Live` | `Long` | `5.58` | 1,600,000.00 USD | 0.00 USD | 63,260.00 USD | `-32.12%` | `11,347.58` |
| `Live` | `Long` | `5.59` | 1,540,000.00 USD | 0.00 USD | 34,430.00 USD | `-31.87%` | `6,153.60` |
| `Live` | `Long` | `5.63` | 1,500,000.00 USD | 0.00 USD | 468.55 USD | `-31.39%` | `83.15` |
| `Live` | `Long` | `5.67` | 1,500,000.00 USD | 0.00 USD | 133.14 USD | `-30.90%` | `23.46` |
| `Live` | `Long` | `5.72` | 1,500,000.00 USD | 0.00 USD | 2,390.00 USD | `-30.29%` | `417.17` |
| `Live` | `Long` | `5.74` | 1,500,000.00 USD | 0.00 USD | 238.86 USD | `-30.17%` | `41.65` |
| `Live` | `Long` | `5.75` | 1,500,000.00 USD | 0.00 USD | 125.70 USD | `-30.05%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,500,000.00 USD | 0.00 USD | 3,190.00 USD | `-29.92%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,500,000.00 USD | 0.00 USD | 10,850.00 USD | `-29.80%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,490,000.00 USD | 0.00 USD | 902.40 USD | `-29.68%` | `156.26` |
| `Live` | `Long` | `5.79` | 1,490,000.00 USD | 0.00 USD | 635.31 USD | `-29.44%` | `109.63` |
| `Live` | `Long` | `5.80` | 1,490,000.00 USD | 0.00 USD | 580.50 USD | `-29.32%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,480,000.00 USD | 0.00 USD | 106.65 USD | `-29.19%` | `18.34` |
| `Live` | `Long` | `5.83` | 1,480,000.00 USD | 0.00 USD | 145.88 USD | `-28.95%` | `25.00` |
| `Live` | `Long` | `5.86` | 1,480,000.00 USD | 0.00 USD | 2,110.00 USD | `-28.71%` | `360.33` |
| `Live` | `Long` | `5.89` | 1,480,000.00 USD | 0.00 USD | 984.70 USD | `-28.22%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,480,000.00 USD | 0.00 USD | 1,990.00 USD | `-28.10%` | `337.60` |
| `Live` | `Long` | `5.92` | 1,480,000.00 USD | 0.00 USD | 277.35 USD | `-27.98%` | `46.89` |
| `Live` | `Long` | `5.96` | 1,480,000.00 USD | 0.00 USD | 11,720.00 USD | `-27.49%` | `1,968.19` |
| `Live` | `Long` | `5.97` | 1,470,000.00 USD | 0.00 USD | 585.97 USD | `-27.25%` | `98.07` |
| `Live` | `Long` | `6.00` | 1,470,000.00 USD | 0.00 USD | 243.46 USD | `-27.00%` | `40.61` |
| `Live` | `Long` | `6.00` | 1,470,000.00 USD | 0.00 USD | 341.56 USD | `-26.88%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,470,000.00 USD | 0.00 USD | 446.85 USD | `-26.76%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,470,000.00 USD | 0.00 USD | 331.68 USD | `-26.51%` | `54.96` |
| `Live` | `Long` | `6.04` | 1,470,000.00 USD | 0.00 USD | 105.61 USD | `-26.39%` | `17.47` |
| `Live` | `Long` | `6.05` | 1,470,000.00 USD | 0.00 USD | 1,310.00 USD | `-26.27%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,460,000.00 USD | 0.00 USD | 265.10 USD | `-26.15%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,460,000.00 USD | 0.00 USD | 1,690.00 USD | `-26.03%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,460,000.00 USD | 0.00 USD | 405.14 USD | `-25.91%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,460,000.00 USD | 0.00 USD | 3,130.00 USD | `-25.78%` | `512.81` |
| `Live` | `Long` | `6.12` | 1,460,000.00 USD | 0.00 USD | 1,140.00 USD | `-25.54%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,460,000.00 USD | 0.00 USD | 2,160.00 USD | `-25.42%` | `353.02` |
| `Live` | `Long` | `6.14` | 1,460,000.00 USD | 0.00 USD | 238.61 USD | `-25.18%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,460,000.00 USD | 0.00 USD | 7,810.00 USD | `-25.05%` | `1,268.30` |
| `Live` | `Long` | `6.17` | 1,450,000.00 USD | 0.00 USD | 104.36 USD | `-24.81%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,450,000.00 USD | 0.00 USD | 310.25 USD | `-24.44%` | `50.00` |
| `Live` | `Long` | `6.25` | 1,450,000.00 USD | 0.00 USD | 1,570.00 USD | `-23.96%` | `251.60` |
| `Live` | `Long` | `6.25` | 1,450,000.00 USD | 0.00 USD | 972.65 USD | `-23.84%` | `155.50` |
| `Live` | `Long` | `6.26` | 1,440,000.00 USD | 0.00 USD | 399.39 USD | `-23.71%` | `63.75` |
| `Live` | `Long` | `6.28` | 1,440,000.00 USD | 0.00 USD | 2,510.00 USD | `-23.59%` | `400.00` |
| `Live` | `Long` | `6.29` | 1,440,000.00 USD | 0.00 USD | 1,460.00 USD | `-23.35%` | `232.17` |
| `Live` | `Long` | `6.30` | 1,440,000.00 USD | 0.00 USD | 654.02 USD | `-23.23%` | `103.73` |
| `Live` | `Long` | `6.32` | 1,440,000.00 USD | 0.00 USD | 277.04 USD | `-23.11%` | `43.87` |
| `Live` | `Long` | `6.33` | 1,440,000.00 USD | 0.00 USD | 2,450.00 USD | `-22.86%` | `386.46` |
| `Live` | `Long` | `6.36` | 1,440,000.00 USD | 0.00 USD | 4,470.00 USD | `-22.62%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,430,000.00 USD | 0.00 USD | 284,770.00 USD | `-22.50%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 1,150,000.00 USD | 0.00 USD | 5,890.00 USD | `-22.37%` | `924.50` |
| `Live` | `Long` | `6.42` | 1,140,000.00 USD | 0.00 USD | 306.32 USD | `-21.89%` | `47.75` |
| `Live` | `Long` | `6.42` | 1,140,000.00 USD | 0.00 USD | 484.64 USD | `-21.77%` | `75.43` |
| `Live` | `Long` | `6.43` | 1,140,000.00 USD | 0.00 USD | 6,780.00 USD | `-21.64%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 1,130,000.00 USD | 0.00 USD | 1,650.00 USD | `-21.28%` | `255.13` |
| `Live` | `Long` | `6.50` | 1,130,000.00 USD | 0.00 USD | 1,460.00 USD | `-20.79%` | `225.14` |
| `Live` | `Long` | `6.54` | 1,130,000.00 USD | 0.00 USD | 8,970.00 USD | `-20.30%` | `1,370.89` |
| `Live` | `Long` | `6.55` | 1,120,000.00 USD | 0.00 USD | 316.08 USD | `-20.18%` | `48.22` |
| `Live` | `Long` | `6.58` | 1,120,000.00 USD | 0.00 USD | 537.37 USD | `-19.94%` | `81.73` |
| `Live` | `Long` | `6.58` | 1,120,000.00 USD | 0.00 USD | 1,770.00 USD | `-19.82%` | `269.14` |
| `Live` | `Long` | `6.59` | 1,120,000.00 USD | 0.00 USD | 1,100.00 USD | `-19.70%` | `166.55` |
| `Live` | `Long` | `6.62` | 1,120,000.00 USD | 0.00 USD | 2,110.00 USD | `-19.45%` | `318.57` |
| `Live` | `Long` | `6.62` | 1,120,000.00 USD | 0.00 USD | 680.39 USD | `-19.33%` | `102.70` |
| `Live` | `Long` | `6.63` | 1,120,000.00 USD | 0.00 USD | 245.89 USD | `-19.21%` | `37.06` |
| `Live` | `Long` | `6.67` | 1,120,000.00 USD | 0.00 USD | 1,320.00 USD | `-18.72%` | `198.12` |
| `Live` | `Long` | `6.70` | 1,110,000.00 USD | 0.00 USD | 506.54 USD | `-18.48%` | `75.66` |
| `Live` | `Long` | `6.71` | 1,110,000.00 USD | 0.00 USD | 16,070.00 USD | `-18.36%` | `2,396.06` |
| `Live` | `Long` | `6.71` | 1,100,000.00 USD | 0.00 USD | 6,180.00 USD | `-18.23%` | `920.74` |
| `Live` | `Long` | `6.75` | 1,090,000.00 USD | 0.00 USD | 2,870.00 USD | `-17.87%` | `425.36` |
| `Live` | `Long` | `6.78` | 1,090,000.00 USD | 0.00 USD | 386,580.00 USD | `-17.50%` | `57,059.40` |
| `Live` | `Long` | `6.79` | 701,600.00 USD | 0.00 USD | 21,580.00 USD | `-17.38%` | `3,180.66` |
| `Live` | `Long` | `6.79` | 680,020.00 USD | 0.00 USD | 4,720.00 USD | `-17.26%` | `694.73` |
| `Live` | `Long` | `6.80` | 675,300.00 USD | 0.00 USD | 1,500.00 USD | `-17.14%` | `220.95` |
| `Live` | `Long` | `6.82` | 673,800.00 USD | 0.00 USD | 7,230.00 USD | `-17.02%` | `1,061.04` |
| `Live` | `Long` | `6.83` | 666,560.00 USD | 0.00 USD | 158.14 USD | `-16.89%` | `23.17` |
| `Live` | `Long` | `6.84` | 666,410.00 USD | 0.00 USD | 204.12 USD | `-16.65%` | `29.82` |
| `Live` | `Long` | `6.87` | 666,200.00 USD | 0.00 USD | 3,550.00 USD | `-16.41%` | `517.09` |
| `Live` | `Long` | `6.88` | 662,650.00 USD | 0.00 USD | 1,580.00 USD | `-16.16%` | `229.18` |
| `Live` | `Long` | `6.95` | 661,070.00 USD | 0.00 USD | 3,980.00 USD | `-15.43%` | `572.68` |
| `Live` | `Long` | `6.96` | 657,100.00 USD | 0.00 USD | 3,480.00 USD | `-15.31%` | `500.00` |
| `Live` | `Long` | `6.96` | 653,620.00 USD | 0.00 USD | 636.74 USD | `-15.19%` | `91.42` |
| `Live` | `Long` | `6.97` | 652,980.00 USD | 0.00 USD | 128,810.00 USD | `-15.07%` | `18,466.99` |
| `Live` | `Long` | `6.99` | 524,180.00 USD | 0.00 USD | 297.49 USD | `-14.95%` | `42.59` |
| `Live` | `Long` | `7.00` | 523,880.00 USD | 0.00 USD | 746.58 USD | `-14.82%` | `106.73` |
| `Live` | `Long` | `7.00` | 523,130.00 USD | 0.00 USD | 20,860.00 USD | `-14.70%` | `2,978.11` |
| `Live` | `Long` | `7.03` | 502,270.00 USD | 0.00 USD | 1,370.00 USD | `-14.46%` | `194.51` |
| `Live` | `Long` | `7.04` | 500,900.00 USD | 0.00 USD | 704.50 USD | `-14.22%` | `100.00` |
| `Live` | `Long` | `7.05` | 500,200.00 USD | 0.00 USD | 354.23 USD | `-14.09%` | `50.21` |
| `Live` | `Long` | `7.07` | 499,840.00 USD | 0.00 USD | 24,310.00 USD | `-13.97%` | `3,441.37` |
| `Live` | `Long` | `7.08` | 475,530.00 USD | 0.00 USD | 6,700.00 USD | `-13.85%` | `947.44` |
| `Live` | `Long` | `7.08` | 468,830.00 USD | 0.00 USD | 644.88 USD | `-13.73%` | `91.02` |
| `Live` | `Long` | `7.11` | 468,180.00 USD | 0.00 USD | 28,530.00 USD | `-13.49%` | `4,015.35` |
| `Live` | `Long` | `7.12` | 439,650.00 USD | 0.00 USD | 379.66 USD | `-13.36%` | `53.36` |
| `Live` | `Long` | `7.13` | 439,270.00 USD | 0.00 USD | 777.50 USD | `-13.12%` | `108.97` |
| `Live` | `Long` | `7.14` | 438,500.00 USD | 0.00 USD | 20,270.00 USD | `-13.00%` | `2,837.00` |
| `Live` | `Long` | `7.17` | 418,230.00 USD | 0.00 USD | 9,550.00 USD | `-12.63%` | `1,331.12` |
| `Live` | `Long` | `7.18` | 408,680.00 USD | 0.00 USD | 6,000.00 USD | `-12.51%` | `835.49` |
| `Live` | `Long` | `7.21` | 402,670.00 USD | 0.00 USD | 322.94 USD | `-12.15%` | `44.76` |
| `Live` | `Long` | `7.24` | 402,350.00 USD | 0.00 USD | 1,480.00 USD | `-11.90%` | `205.21` |
| `Live` | `Long` | `7.25` | 400,870.00 USD | 0.00 USD | 185.83 USD | `-11.78%` | `25.65` |
| `Live` | `Long` | `7.25` | 400,680.00 USD | 0.00 USD | 50,300.00 USD | `-11.66%` | `6,933.17` |
| `Live` | `Long` | `7.29` | 350,380.00 USD | 0.00 USD | 38,110.00 USD | `-11.29%` | `5,230.97` |
| `Live` | `Long` | `7.29` | 312,270.00 USD | 0.00 USD | 1,460.00 USD | `-11.17%` | `200.00` |
| `Live` | `Long` | `7.34` | 310,810.00 USD | 0.00 USD | 4,370.00 USD | `-10.56%` | `594.84` |
| `Live` | `Long` | `7.37` | 306,440.00 USD | 0.00 USD | 2,940.00 USD | `-10.32%` | `399.15` |
| `Live` | `Long` | `7.38` | 303,500.00 USD | 0.00 USD | 3,180.00 USD | `-10.20%` | `431.50` |
| `Live` | `Long` | `7.38` | 300,320.00 USD | 0.00 USD | 13,620.00 USD | `-10.08%` | `1,844.66` |
| `Live` | `Long` | `7.42` | 286,700.00 USD | 0.00 USD | 147.61 USD | `-9.59%` | `19.88` |
| `Live` | `Long` | `7.45` | 286,550.00 USD | 0.00 USD | 1,320.00 USD | `-9.35%` | `177.68` |
| `Live` | `Long` | `7.46` | 285,230.00 USD | 0.00 USD | 10,390.00 USD | `-9.22%` | `1,393.53` |
| `Live` | `Long` | `7.46` | 274,840.00 USD | 0.00 USD | 4,590.00 USD | `-9.10%` | `614.36` |
| `Live` | `Long` | `7.47` | 270,250.00 USD | 0.00 USD | 1,120.00 USD | `-8.98%` | `149.52` |
| `Live` | `Long` | `7.50` | 269,140.00 USD | 0.00 USD | 962.81 USD | `-8.74%` | `128.46` |
| `Live` | `Long` | `7.50` | 268,170.00 USD | 0.00 USD | 421.78 USD | `-8.61%` | `56.20` |
| `Live` | `Long` | `7.51` | 267,750.00 USD | 0.00 USD | 1,710.00 USD | `-8.49%` | `228.21` |
| `Live` | `Long` | `7.53` | 266,040.00 USD | 0.00 USD | 1,570.00 USD | `-8.37%` | `208.52` |
| `Live` | `Long` | `7.54` | 264,470.00 USD | 0.00 USD | 5,190.00 USD | `-8.25%` | `689.39` |
| `Live` | `Long` | `7.55` | 259,270.00 USD | 0.00 USD | 1,630.00 USD | `-8.01%` | `215.80` |
| `Live` | `Long` | `7.57` | 257,640.00 USD | 0.00 USD | 25,060.00 USD | `-7.88%` | `3,312.23` |
| `Live` | `Long` | `7.58` | 232,590.00 USD | 0.00 USD | 118.25 USD | `-7.76%` | `15.61` |
| `Live` | `Long` | `7.58` | 232,470.00 USD | 0.00 USD | 1,520.00 USD | `-7.64%` | `200.00` |
| `Live` | `Long` | `7.59` | 230,950.00 USD | 0.00 USD | 24,760.00 USD | `-7.52%` | `3,260.14` |
| `Live` | `Long` | `7.62` | 206,190.00 USD | 0.00 USD | 754.04 USD | `-7.28%` | `99.02` |
| `Live` | `Long` | `7.62` | 205,440.00 USD | 0.00 USD | 787.51 USD | `-7.15%` | `103.28` |
| `Live` | `Long` | `7.63` | 204,650.00 USD | 0.00 USD | 378.93 USD | `-7.03%` | `49.63` |
| `Live` | `Long` | `7.64` | 204,270.00 USD | 0.00 USD | 1,890.00 USD | `-6.91%` | `247.83` |
| `Live` | `Long` | `7.66` | 202,370.00 USD | 0.00 USD | 135.42 USD | `-6.79%` | `17.69` |
| `Live` | `Long` | `7.67` | 202,240.00 USD | 0.00 USD | 1,740.00 USD | `-6.67%` | `226.45` |
| `Live` | `Long` | `7.67` | 200,500.00 USD | 0.00 USD | 4,480.00 USD | `-6.54%` | `583.63` |
| `Live` | `Long` | `7.68` | 196,020.00 USD | 0.00 USD | 1,710.00 USD | `-6.42%` | `222.37` |
| `Live` | `Long` | `7.70` | 194,310.00 USD | 0.00 USD | 2,490.00 USD | `-6.30%` | `323.25` |
| `Live` | `Long` | `7.72` | 191,830.00 USD | 0.00 USD | 890.92 USD | `-5.94%` | `115.33` |
| `Live` | `Long` | `7.75` | 190,940.00 USD | 0.00 USD | 500.12 USD | `-5.57%` | `64.49` |
| `Live` | `Long` | `7.76` | 190,440.00 USD | 0.00 USD | 455.73 USD | `-5.45%` | `58.69` |
| `Live` | `Long` | `7.78` | 189,980.00 USD | 0.00 USD | 2,990.00 USD | `-5.33%` | `384.20` |
| `Live` | `Long` | `7.79` | 186,990.00 USD | 0.00 USD | 2,470.00 USD | `-5.21%` | `317.11` |
| `Live` | `Long` | `7.79` | 184,520.00 USD | 0.00 USD | 1,940.00 USD | `-5.08%` | `248.84` |
| `Live` | `Long` | `7.82` | 182,590.00 USD | 0.00 USD | 1,560.00 USD | `-4.84%` | `200.00` |
| `Live` | `Long` | `7.83` | 181,020.00 USD | 0.00 USD | 706.68 USD | `-4.72%` | `90.31` |
| `Live` | `Long` | `7.84` | 180,320.00 USD | 0.00 USD | 24,340.00 USD | `-4.47%` | `3,102.56` |
| `Live` | `Long` | `7.87` | 155,980.00 USD | 0.00 USD | 233.83 USD | `-4.23%` | `29.73` |
| `Live` | `Long` | `7.88` | 155,740.00 USD | 0.00 USD | 555.19 USD | `-4.11%` | `70.50` |
| `Live` | `Long` | `7.89` | 155,190.00 USD | 0.00 USD | 986.88 USD | `-3.87%` | `125.00` |
| `Live` | `Long` | `7.91` | 154,200.00 USD | 0.00 USD | 505.13 USD | `-3.74%` | `63.90` |
| `Live` | `Long` | `7.92` | 153,690.00 USD | 0.00 USD | 4,890.00 USD | `-3.50%` | `616.87` |
| `Live` | `Long` | `7.93` | 148,810.00 USD | 0.00 USD | 16,340.00 USD | `-3.38%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 132,460.00 USD | 0.00 USD | 127,110.00 USD | `-3.26%` | `15,999.24` |
| `Live` | `Long` | `7.96` | 5,350.00 USD | 0.00 USD | 467.91 USD | `-3.14%` | `58.82` |
| `Live` | `Long` | `7.97` | 4,880.00 USD | 0.00 USD | 2,950.00 USD | `-2.89%` | `369.52` |
| `Live` | `Long` | `7.99` | 1,930.00 USD | 0.00 USD | 1,720.00 USD | `-2.77%` | `215.86` |
| `Live` | `Long` | `8.00` | 210.99 USD | 0.00 USD | 210.99 USD | `-2.65%` | `26.39` |
| `Live` | `Short` | `8.18` | 2,930.00 USD | 2,930.00 USD | 0.00 USD | `-0.46%` | `358.92` |
| `Live` | `Short` | `8.49` | 9,150.00 USD | 6,210.00 USD | 0.00 USD | `+3.44%` | `731.54` |
| `Live` | `Short` | `8.57` | 9,370.00 USD | 221.06 USD | 0.00 USD | `+4.41%` | `25.78` |
| `Live` | `Short` | `8.66` | 13,740.00 USD | 4,370.00 USD | 0.00 USD | `+5.51%` | `504.07` |
| `Live` | `Short` | `8.69` | 13,950.00 USD | 209.31 USD | 0.00 USD | `+5.75%` | `24.10` |
| `Live` | `Short` | `8.82` | 19,950.00 USD | 6,000.00 USD | 0.00 USD | `+7.46%` | `680.16` |
| `Live` | `Short` | `8.91` | 20,390.00 USD | 440.40 USD | 0.00 USD | `+8.55%` | `49.40` |
| `Live` | `Short` | `9.19` | 22,140.00 USD | 1,750.00 USD | 0.00 USD | `+11.84%` | `190.60` |
| `Live` | `Short` | `9.21` | 24,010.00 USD | 1,870.00 USD | 0.00 USD | `+12.21%` | `202.76` |
| `Live` | `Short` | `9.41` | 24,450.00 USD | 440.06 USD | 0.00 USD | `+14.64%` | `46.74` |
| `Live` | `Short` | `9.62` | 24,590.00 USD | 138.98 USD | 0.00 USD | `+17.20%` | `14.44` |
| `Live` | `Short` | `9.64` | 26,520.00 USD | 1,930.00 USD | 0.00 USD | `+17.44%` | `200.61` |
| `Live` | `Short` | `9.73` | 26,720.00 USD | 192.95 USD | 0.00 USD | `+18.54%` | `19.82` |
| `Live` | `Short` | `10.35` | 29,370.00 USD | 2,650.00 USD | 0.00 USD | `+25.97%` | `256.58` |
| `Live` | `Short` | `10.56` | 29,890.00 USD | 523.81 USD | 0.00 USD | `+28.65%` | `49.58` |
| `Live` | `Short` | `10.69` | 136,740.00 USD | 106,850.00 USD | 0.00 USD | `+30.11%` | `10,000.00` |
| `Live` | `Short` | `10.89` | 136,840.00 USD | 100.13 USD | 0.00 USD | `+32.66%` | `9.19` |
| `Live` | `Short` | `10.97` | 356,350.00 USD | 219,510.00 USD | 0.00 USD | `+33.64%` | `20,000.94` |
| `Live` | `Short` | `11.01` | 363,320.00 USD | 6,970.00 USD | 0.00 USD | `+34.00%` | `633.00` |
| `Live` | `Short` | `11.06` | 418,650.00 USD | 55,330.00 USD | 0.00 USD | `+34.73%` | `5,000.00` |
| `Live` | `Short` | `11.27` | 430,310.00 USD | 11,670.00 USD | 0.00 USD | `+37.17%` | `1,035.87` |
| `Live` | `Short` | `11.62` | 442,450.00 USD | 12,140.00 USD | 0.00 USD | `+41.55%` | `1,043.90` |
| `Live` | `Short` | `11.69` | 739,210.00 USD | 296,760.00 USD | 0.00 USD | `+42.28%` | `25,397.02` |
| `Live` | `Short` | `11.80` | 739,330.00 USD | 114.27 USD | 0.00 USD | `+43.74%` | `9.68` |
| `Live` | `Short` | `11.90` | 739,610.00 USD | 285.24 USD | 0.00 USD | `+44.96%` | `23.96` |
| `Live` | `Short` | `11.93` | 740,120.00 USD | 505.74 USD | 0.00 USD | `+45.21%` | `42.41` |
| `Live` | `Short` | `11.95` | 741,500.00 USD | 1,380.00 USD | 0.00 USD | `+45.45%` | `115.69` |
| `Live` | `Short` | `12.30` | 743,230.00 USD | 1,730.00 USD | 0.00 USD | `+49.83%` | `140.71` |
| `Live` | `Short` | `12.40` | 743,580.00 USD | 343.62 USD | 0.00 USD | `+51.05%` | `27.70` |
| `Live` | `Short` | `12.66` | 744,520.00 USD | 946.71 USD | 0.00 USD | `+54.22%` | `74.75` |
| `Live` | `Short` | `13.20` | 832,470.00 USD | 87,940.00 USD | 0.00 USD | `+60.67%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 836,280.00 USD | 3,810.00 USD | 0.00 USD | `+61.89%` | `286.56` |
| `Live` | `Short` | `13.44` | 849,710.00 USD | 13,430.00 USD | 0.00 USD | `+63.59%` | `1,000.00` |
| `Live` | `Short` | `13.46` | 850,140.00 USD | 430.34 USD | 0.00 USD | `+63.96%` | `31.96` |
| `Live` | `Short` | `13.69` | 850,310.00 USD | 172.29 USD | 0.00 USD | `+66.64%` | `12.59` |
| `Live` | `Short` | `14.11` | 850,590.00 USD | 278.29 USD | 0.00 USD | `+71.75%` | `19.73` |
| `Live` | `Short` | `14.66` | 851,420.00 USD | 823.29 USD | 0.00 USD | `+78.57%` | `56.14` |
| `Live` | `Short` | `15.02` | 851,660.00 USD | 246.40 USD | 0.00 USD | `+82.83%` | `16.41` |
| `Live` | `Short` | `15.29` | 851,890.00 USD | 229.43 USD | 0.00 USD | `+86.24%` | `15.00` |
| `Live` | `Short` | `15.35` | 852,120.00 USD | 230.17 USD | 0.00 USD | `+86.85%` | `15.00` |
| `Live` | `Short` | `15.38` | 872,120.00 USD | 20,000.00 USD | 0.00 USD | `+87.34%` | `1,300.00` |
| `Live` | `Short` | `15.43` | 876,400.00 USD | 4,280.00 USD | 0.00 USD | `+87.82%` | `277.54` |
| `Live` | `Short` | `15.46` | 878,970.00 USD | 2,570.00 USD | 0.00 USD | `+88.31%` | `166.16` |
| `Live` | `Short` | `15.51` | 879,310.00 USD | 334.13 USD | 0.00 USD | `+88.80%` | `21.55` |
| `Live` | `Short` | `15.60` | 879,870.00 USD | 559.70 USD | 0.00 USD | `+89.89%` | `35.89` |
| `Live` | `Short` | `15.72` | 880,040.00 USD | 167.79 USD | 0.00 USD | `+91.48%` | `10.67` |
| `Live` | `Short` | `15.77` | 880,220.00 USD | 185.55 USD | 0.00 USD | `+91.96%` | `11.77` |
| `Live` | `Short` | `15.79` | 880,480.00 USD | 261.72 USD | 0.00 USD | `+92.21%` | `16.58` |
| `Live` | `Short` | `16.38` | 901,950.00 USD | 21,470.00 USD | 0.00 USD | `+99.39%` | `1,311.22` |
| `Live` | `Short` | `16.43` | 1,170,000.00 USD | 266,220.00 USD | 0.00 USD | `+100.00%` | `16,208.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 294,500.00 USD | 0.00 USD | 611.73 USD | `-71.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 293,890.00 USD | 0.00 USD | 793.75 USD | `-51.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 293,100.00 USD | 0.00 USD | 105.04 USD | `-45.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 292,990.00 USD | 0.00 USD | 67,970.00 USD | `-39.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 225,030.00 USD | 0.00 USD | 205.30 USD | `-35.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 224,820.00 USD | 0.00 USD | 465.42 USD | `-33.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 224,360.00 USD | 0.00 USD | 349.35 USD | `-32.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 224,010.00 USD | 0.00 USD | 1,020.00 USD | `-32.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 222,990.00 USD | 0.00 USD | 1,330.00 USD | `-29.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 221,660.00 USD | 0.00 USD | 493.50 USD | `-27.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 221,170.00 USD | 0.00 USD | 100.98 USD | `-27.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 221,070.00 USD | 0.00 USD | 500.70 USD | `-26.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 220,570.00 USD | 0.00 USD | 4,160.00 USD | `-25.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 216,410.00 USD | 0.00 USD | 6,500.00 USD | `-24.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.21` | 209,910.00 USD | 0.00 USD | 906.18 USD | `-24.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.25` | 209,000.00 USD | 0.00 USD | 127.35 USD | `-23.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 208,880.00 USD | 0.00 USD | 864.38 USD | `-23.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 208,010.00 USD | 0.00 USD | 130.10 USD | `-20.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 207,880.00 USD | 0.00 USD | 4,340.00 USD | `-20.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 203,540.00 USD | 0.00 USD | 5,520.00 USD | `-18.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 198,020.00 USD | 0.00 USD | 100.72 USD | `-18.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 197,920.00 USD | 0.00 USD | 296.34 USD | `-17.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 197,620.00 USD | 0.00 USD | 921.19 USD | `-17.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 196,700.00 USD | 0.00 USD | 709.98 USD | `-16.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 195,990.00 USD | 0.00 USD | 1,380.00 USD | `-15.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 194,610.00 USD | 0.00 USD | 262.44 USD | `-15.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 194,350.00 USD | 0.00 USD | 24,350.00 USD | `-14.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.11` | 169,990.00 USD | 0.00 USD | 187.79 USD | `-13.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 169,800.00 USD | 0.00 USD | 6,790.00 USD | `-12.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 163,020.00 USD | 0.00 USD | 9,770.00 USD | `-12.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.21` | 153,250.00 USD | 0.00 USD | 7,210.00 USD | `-12.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 146,040.00 USD | 0.00 USD | 282.74 USD | `-11.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 145,760.00 USD | 0.00 USD | 603.44 USD | `-11.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 145,160.00 USD | 0.00 USD | 464.61 USD | `-11.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 144,690.00 USD | 0.00 USD | 2,090.00 USD | `-11.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 142,600.00 USD | 0.00 USD | 129.58 USD | `-10.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 142,470.00 USD | 0.00 USD | 114.65 USD | `-10.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.39` | 142,350.00 USD | 0.00 USD | 702.75 USD | `-9.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 141,650.00 USD | 0.00 USD | 199.39 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 141,450.00 USD | 0.00 USD | 6,270.00 USD | `-8.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 135,190.00 USD | 0.00 USD | 37,420.00 USD | `-8.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 97,760.00 USD | 0.00 USD | 2,120.00 USD | `-8.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 95,640.00 USD | 0.00 USD | 799.83 USD | `-8.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 94,840.00 USD | 0.00 USD | 820.44 USD | `-8.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 94,020.00 USD | 0.00 USD | 103.41 USD | `-7.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 93,920.00 USD | 0.00 USD | 1,370.00 USD | `-7.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 92,540.00 USD | 0.00 USD | 297.59 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.68` | 92,250.00 USD | 0.00 USD | 528.88 USD | `-6.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 91,720.00 USD | 0.00 USD | 360.13 USD | `-6.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 91,360.00 USD | 0.00 USD | 578.04 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 90,780.00 USD | 0.00 USD | 175.42 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.79` | 90,600.00 USD | 0.00 USD | 424.05 USD | `-5.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 90,180.00 USD | 0.00 USD | 23,790.00 USD | `-4.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.82` | 66,390.00 USD | 0.00 USD | 3,940.00 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 62,450.00 USD | 0.00 USD | 143.51 USD | `-4.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 62,310.00 USD | 0.00 USD | 183.33 USD | `-4.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.88` | 62,130.00 USD | 0.00 USD | 194.52 USD | `-3.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 61,930.00 USD | 0.00 USD | 2,290.00 USD | `-3.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 59,640.00 USD | 0.00 USD | 6,520.00 USD | `-3.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 53,130.00 USD | 0.00 USD | 5,710.00 USD | `-3.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 47,420.00 USD | 0.00 USD | 1,590.00 USD | `-3.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 45,830.00 USD | 0.00 USD | 898.42 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 44,940.00 USD | 0.00 USD | 9,160.00 USD | `-2.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 35,770.00 USD | 0.00 USD | 3,430.00 USD | `-2.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 32,340.00 USD | 0.00 USD | 123.58 USD | `-2.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 32,220.00 USD | 0.00 USD | 2,110.00 USD | `-2.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 30,110.00 USD | 0.00 USD | 550.48 USD | `-1.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.06` | 29,560.00 USD | 0.00 USD | 2,730.00 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 26,830.00 USD | 0.00 USD | 121.69 USD | `-1.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 26,710.00 USD | 0.00 USD | 477.36 USD | `-1.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 26,230.00 USD | 0.00 USD | 924.78 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 25,310.00 USD | 0.00 USD | 329.06 USD | `-1.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 24,980.00 USD | 0.00 USD | 6,500.00 USD | `-1.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 18,480.00 USD | 0.00 USD | 884.60 USD | `-0.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 17,590.00 USD | 0.00 USD | 5,550.00 USD | `-0.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 12,040.00 USD | 0.00 USD | 1,430.00 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 10,600.00 USD | 0.00 USD | 3,080.00 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 7,520.00 USD | 0.00 USD | 520.75 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 7,000.00 USD | 0.00 USD | 3,020.00 USD | `-0.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 3,980.00 USD | 0.00 USD | 141.04 USD | `-0.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 3,840.00 USD | 0.00 USD | 3,840.00 USD | `-0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 515.66 USD | 515.66 USD | 0.00 USD | `+0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.23` | 1,540.00 USD | 1,030.00 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.24` | 5,050.00 USD | 3,510.00 USD | 0.00 USD | `+0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.26` | 14,170.00 USD | 9,110.00 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.27` | 14,520.00 USD | 353.00 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.28` | 14,930.00 USD | 408.78 USD | 0.00 USD | `+0.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.29` | 15,130.00 USD | 201.49 USD | 0.00 USD | `+0.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.29` | 19,280.00 USD | 4,150.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.30` | 19,520.00 USD | 242.42 USD | 0.00 USD | `+1.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.31` | 22,440.00 USD | 2,920.00 USD | 0.00 USD | `+1.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.32` | 24,130.00 USD | 1,690.00 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.34` | 26,130.00 USD | 2,000.00 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.35` | 26,890.00 USD | 756.06 USD | 0.00 USD | `+1.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.36` | 27,860.00 USD | 970.35 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 28,360.00 USD | 503.59 USD | 0.00 USD | `+1.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 28,780.00 USD | 419.25 USD | 0.00 USD | `+2.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 30,750.00 USD | 1,970.00 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 31,080.00 USD | 328.55 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.41` | 31,390.00 USD | 314.81 USD | 0.00 USD | `+2.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.43` | 33,280.00 USD | 1,880.00 USD | 0.00 USD | `+2.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.44` | 33,580.00 USD | 307.54 USD | 0.00 USD | `+2.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.45` | 33,720.00 USD | 138.24 USD | 0.00 USD | `+2.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 34,430.00 USD | 710.81 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.47` | 35,200.00 USD | 769.61 USD | 0.00 USD | `+3.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.48` | 35,350.00 USD | 146.79 USD | 0.00 USD | `+3.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.49` | 36,760.00 USD | 1,410.00 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 38,200.00 USD | 1,440.00 USD | 0.00 USD | `+3.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.52` | 38,610.00 USD | 408.55 USD | 0.00 USD | `+3.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.53` | 39,740.00 USD | 1,130.00 USD | 0.00 USD | `+3.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 39,900.00 USD | 162.68 USD | 0.00 USD | `+3.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 44,310.00 USD | 4,400.00 USD | 0.00 USD | `+4.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.55` | 44,550.00 USD | 243.82 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.56` | 46,150.00 USD | 1,600.00 USD | 0.00 USD | `+4.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.57` | 47,570.00 USD | 1,420.00 USD | 0.00 USD | `+4.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.59` | 50,080.00 USD | 2,500.00 USD | 0.00 USD | `+4.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.60` | 51,200.00 USD | 1,130.00 USD | 0.00 USD | `+4.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 51,960.00 USD | 751.56 USD | 0.00 USD | `+4.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 53,450.00 USD | 1,490.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 57,630.00 USD | 4,180.00 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 57,830.00 USD | 201.97 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 57,930.00 USD | 103.31 USD | 0.00 USD | `+5.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 59,840.00 USD | 1,900.00 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 59,950.00 USD | 107.97 USD | 0.00 USD | `+5.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 60,120.00 USD | 176.62 USD | 0.00 USD | `+5.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 61,110.00 USD | 990.09 USD | 0.00 USD | `+5.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 66,120.00 USD | 5,010.00 USD | 0.00 USD | `+5.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 66,700.00 USD | 575.14 USD | 0.00 USD | `+6.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 67,100.00 USD | 399.67 USD | 0.00 USD | `+6.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 67,920.00 USD | 819.28 USD | 0.00 USD | `+6.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 68,250.00 USD | 333.07 USD | 0.00 USD | `+6.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 72,620.00 USD | 4,370.00 USD | 0.00 USD | `+6.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 74,400.00 USD | 1,780.00 USD | 0.00 USD | `+6.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 114,210.00 USD | 39,810.00 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 114,420.00 USD | 215.16 USD | 0.00 USD | `+6.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 114,810.00 USD | 388.12 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 115,520.00 USD | 711.78 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 124,890.00 USD | 9,370.00 USD | 0.00 USD | `+7.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.82` | 126,920.00 USD | 2,030.00 USD | 0.00 USD | `+7.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 127,170.00 USD | 243.40 USD | 0.00 USD | `+7.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 132,930.00 USD | 5,760.00 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 133,170.00 USD | 234.04 USD | 0.00 USD | `+7.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 133,330.00 USD | 163.91 USD | 0.00 USD | `+7.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 133,440.00 USD | 110.58 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 134,550.00 USD | 1,100.00 USD | 0.00 USD | `+8.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 136,480.00 USD | 1,930.00 USD | 0.00 USD | `+8.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 137,270.00 USD | 788.72 USD | 0.00 USD | `+8.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 139,070.00 USD | 1,800.00 USD | 0.00 USD | `+8.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 139,230.00 USD | 163.33 USD | 0.00 USD | `+8.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 168,760.00 USD | 29,520.00 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 168,980.00 USD | 223.62 USD | 0.00 USD | `+8.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 169,160.00 USD | 180.53 USD | 0.00 USD | `+9.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 169,560.00 USD | 401.63 USD | 0.00 USD | `+9.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 484,720.00 USD | 315,150.00 USD | 0.00 USD | `+9.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 484,820.00 USD | 104.59 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 485,080.00 USD | 262.56 USD | 0.00 USD | `+9.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 485,210.00 USD | 130.03 USD | 0.00 USD | `+9.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 486,590.00 USD | 1,380.00 USD | 0.00 USD | `+9.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 487,680.00 USD | 1,090.00 USD | 0.00 USD | `+9.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 488,290.00 USD | 616.37 USD | 0.00 USD | `+10.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 488,400.00 USD | 102.03 USD | 0.00 USD | `+10.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 488,850.00 USD | 453.84 USD | 0.00 USD | `+10.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 489,010.00 USD | 160.99 USD | 0.00 USD | `+10.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 489,430.00 USD | 415.00 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 490,940.00 USD | 1,510.00 USD | 0.00 USD | `+10.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 491,540.00 USD | 606.18 USD | 0.00 USD | `+10.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 491,720.00 USD | 182.10 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 496,280.00 USD | 4,560.00 USD | 0.00 USD | `+10.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 496,450.00 USD | 166.53 USD | 0.00 USD | `+11.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 498,450.00 USD | 2,000.00 USD | 0.00 USD | `+11.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 892,660.00 USD | 394,210.00 USD | 0.00 USD | `+11.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 892,780.00 USD | 119.24 USD | 0.00 USD | `+11.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.20` | 894,370.00 USD | 1,590.00 USD | 0.00 USD | `+11.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 897,030.00 USD | 2,660.00 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 897,160.00 USD | 131.87 USD | 0.00 USD | `+12.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 897,310.00 USD | 149.17 USD | 0.00 USD | `+12.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 899,530.00 USD | 2,220.00 USD | 0.00 USD | `+12.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,130,000.00 USD | 231,380.00 USD | 0.00 USD | `+12.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,130,000.00 USD | 1,960.00 USD | 0.00 USD | `+12.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,130,000.00 USD | 434.45 USD | 0.00 USD | `+13.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,150,000.00 USD | 18,610.00 USD | 0.00 USD | `+13.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,150,000.00 USD | 166.83 USD | 0.00 USD | `+13.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,150,000.00 USD | 150.79 USD | 0.00 USD | `+13.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,150,000.00 USD | 101.58 USD | 0.00 USD | `+13.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,150,000.00 USD | 109.36 USD | 0.00 USD | `+13.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,150,000.00 USD | 116.69 USD | 0.00 USD | `+14.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,150,000.00 USD | 163.41 USD | 0.00 USD | `+14.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,150,000.00 USD | 1,150.00 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,150,000.00 USD | 660.84 USD | 0.00 USD | `+14.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,160,000.00 USD | 714.59 USD | 0.00 USD | `+14.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,160,000.00 USD | 928.13 USD | 0.00 USD | `+14.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,160,000.00 USD | 102.45 USD | 0.00 USD | `+14.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,160,000.00 USD | 219.84 USD | 0.00 USD | `+14.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,160,000.00 USD | 1,890.00 USD | 0.00 USD | `+15.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.47` | 1,160,000.00 USD | 1,780.00 USD | 0.00 USD | `+15.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,160,000.00 USD | 1,130.00 USD | 0.00 USD | `+15.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,160,000.00 USD | 288.46 USD | 0.00 USD | `+15.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.51` | 1,160,000.00 USD | 1,600.00 USD | 0.00 USD | `+15.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,160,000.00 USD | 119.92 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,160,000.00 USD | 231.00 USD | 0.00 USD | `+16.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,160,000.00 USD | 221.07 USD | 0.00 USD | `+16.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,160,000.00 USD | 992.00 USD | 0.00 USD | `+16.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,160,000.00 USD | 148.48 USD | 0.00 USD | `+17.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,170,000.00 USD | 191.36 USD | 0.00 USD | `+17.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,170,000.00 USD | 4,440.00 USD | 0.00 USD | `+17.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,170,000.00 USD | 108.21 USD | 0.00 USD | `+18.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,170,000.00 USD | 169.68 USD | 0.00 USD | `+18.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,170,000.00 USD | 574.66 USD | 0.00 USD | `+18.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,170,000.00 USD | 121.87 USD | 0.00 USD | `+18.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,170,000.00 USD | 115.88 USD | 0.00 USD | `+19.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,170,000.00 USD | 340.05 USD | 0.00 USD | `+20.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,170,000.00 USD | 742.12 USD | 0.00 USD | `+20.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,170,000.00 USD | 899.47 USD | 0.00 USD | `+20.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,240,000.00 USD | 70,020.00 USD | 0.00 USD | `+20.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,240,000.00 USD | 373.97 USD | 0.00 USD | `+20.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,250,000.00 USD | 5,050.00 USD | 0.00 USD | `+21.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,250,000.00 USD | 6,370.00 USD | 0.00 USD | `+22.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,250,000.00 USD | 404.20 USD | 0.00 USD | `+23.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,470,000.00 USD | 210,980.00 USD | 0.00 USD | `+23.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,470,000.00 USD | 1,150.00 USD | 0.00 USD | `+23.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,470,000.00 USD | 172.16 USD | 0.00 USD | `+24.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,470,000.00 USD | 895.21 USD | 0.00 USD | `+25.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,470,000.00 USD | 489.40 USD | 0.00 USD | `+25.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,470,000.00 USD | 1,200.00 USD | 0.00 USD | `+26.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,470,000.00 USD | 118.01 USD | 0.00 USD | `+26.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.47` | 1,470,000.00 USD | 818.31 USD | 0.00 USD | `+27.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,470,000.00 USD | 312.31 USD | 0.00 USD | `+27.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,470,000.00 USD | 2,290.00 USD | 0.00 USD | `+28.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,470,000.00 USD | 178.46 USD | 0.00 USD | `+28.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.62` | 1,470,000.00 USD | 153.11 USD | 0.00 USD | `+29.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,470,000.00 USD | 173.42 USD | 0.00 USD | `+30.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,470,000.00 USD | 184.75 USD | 0.00 USD | `+30.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,470,000.00 USD | 135.78 USD | 0.00 USD | `+31.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,470,000.00 USD | 127.96 USD | 0.00 USD | `+31.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,470,000.00 USD | 476.43 USD | 0.00 USD | `+32.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,480,000.00 USD | 869.35 USD | 0.00 USD | `+32.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,480,000.00 USD | 118.97 USD | 0.00 USD | `+32.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,480,000.00 USD | 251.06 USD | 0.00 USD | `+33.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,480,000.00 USD | 552.44 USD | 0.00 USD | `+33.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,480,000.00 USD | 537.26 USD | 0.00 USD | `+34.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,480,000.00 USD | 320.29 USD | 0.00 USD | `+35.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,480,000.00 USD | 1,100.00 USD | 0.00 USD | `+36.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,480,000.00 USD | 2,270.00 USD | 0.00 USD | `+36.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,480,000.00 USD | 1,270.00 USD | 0.00 USD | `+37.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,480,000.00 USD | 1,380.00 USD | 0.00 USD | `+38.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,490,000.00 USD | 2,410.00 USD | 0.00 USD | `+38.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,500,000.00 USD | 9,520.00 USD | 0.00 USD | `+39.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 1,500,000.00 USD | 2,050.00 USD | 0.00 USD | `+39.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,500,000.00 USD | 529.11 USD | 0.00 USD | `+40.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,510,000.00 USD | 7,700.00 USD | 0.00 USD | `+41.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,510,000.00 USD | 906.03 USD | 0.00 USD | `+43.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,510,000.00 USD | 434.61 USD | 0.00 USD | `+44.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,510,000.00 USD | 163.52 USD | 0.00 USD | `+44.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 1,570,000.00 USD | 62,880.00 USD | 0.00 USD | `+46.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.19` | 1,580,000.00 USD | 5,270.00 USD | 0.00 USD | `+48.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.51` | 1,580,000.00 USD | 2,770.00 USD | 0.00 USD | `+52.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 1,580,000.00 USD | 3,350.00 USD | 0.00 USD | `+54.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 1,580,000.00 USD | 197.97 USD | 0.00 USD | `+55.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 1,580,000.00 USD | 3,200.00 USD | 0.00 USD | `+57.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 1,580,000.00 USD | 179.58 USD | 0.00 USD | `+58.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 1,590,000.00 USD | 568.45 USD | 0.00 USD | `+58.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.07` | 1,590,000.00 USD | 504.17 USD | 0.00 USD | `+59.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 1,590,000.00 USD | 169.57 USD | 0.00 USD | `+59.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.30` | 1,590,000.00 USD | 159.66 USD | 0.00 USD | `+62.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 1,590,000.00 USD | 446.52 USD | 0.00 USD | `+62.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 1,590,000.00 USD | 5,320.00 USD | 0.00 USD | `+64.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 1,800,000.00 USD | 210,750.00 USD | 0.00 USD | `+64.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 1,800,000.00 USD | 407.95 USD | 0.00 USD | `+66.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 1,800,000.00 USD | 174.91 USD | 0.00 USD | `+68.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 1,810,000.00 USD | 4,650.00 USD | 0.00 USD | `+70.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 1,810,000.00 USD | 960.26 USD | 0.00 USD | `+72.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 1,810,000.00 USD | 2,710.00 USD | 0.00 USD | `+74.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 1,810,000.00 USD | 805.90 USD | 0.00 USD | `+76.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 1,810,000.00 USD | 655.55 USD | 0.00 USD | `+79.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 1,820,000.00 USD | 4,890.00 USD | 0.00 USD | `+80.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 1,820,000.00 USD | 471.09 USD | 0.00 USD | `+81.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 1,820,000.00 USD | 383.85 USD | 0.00 USD | `+82.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,470,000.00 USD | 653,420.00 USD | 0.00 USD | `+82.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 2,480,000.00 USD | 3,010.00 USD | 0.00 USD | `+83.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,480,000.00 USD | 111.87 USD | 0.00 USD | `+92.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,480,000.00 USD | 219.91 USD | 0.00 USD | `+94.89%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `340.51M` | Total OI Tokens: `41,473,707.4 AVAX`
  * 1h OI Change: `-0.10%` | 4h OI Change: `-4.99%` | 24h OI Change: `-10.75%`
  * Exchange Breakdown: Binance=`79.25M` | Bybit=`56.25M` | OKX=`11.32M` | Hyperliquid=`16.08M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-8.43K` | Last 24h: `18.18K` | Last 3d: `59.53K` | Last 7d: `106.20K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0031%` | **USDT OKX** | `0.0055%` |
| **USDT Bybit** | `-0.0211%` | **USDT KuCoin** | `0.0029%` |
| **USDT MEXC** | `0.0028%` | **USDT BingX** | `0.0049%` |
| **USDT Gate** | `-0.0055%` | **USDT Bitget** | `-0.0020%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `48.26%` | `51.74%` | `0.93` | 47,820,000.00 USD |
| `15M` | `Binance` | `45.44%` | `54.56%` | `0.83` | 33,050,000.00 USD |
| `15M` | `OKX` | `51.22%` | `48.78%` | `1.05` | 3,380,000.00 USD |
| `15M` | `Bybit` | `57.25%` | `42.75%` | `1.34` | 2,480,000.00 USD |
| `15M` | `KuCoin` | `60.98%` | `39.02%` | `1.56` | 235,320.00 USD |
| `15M` | `Gate` | `48.89%` | `51.11%` | `0.96` | 1,290,000.00 USD |
| `15M` | `Bitget` | `65.8%` | `34.2%` | `1.92` | 697,370.00 USD |
| `15M` | `BingX` | `28.23%` | `71.77%` | `0.39` | 825,470.00 USD |
| `15M` | `MEXC` | `51.28%` | `48.72%` | `1.05` | 178,100.00 USD |
| `15M` | `Bitunix` | `49.3%` | `50.7%` | `0.97` | 1,130,000.00 USD |
| `15M` | `Hyperliquid` | `54.19%` | `45.81%` | `1.18` | 1,620,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.05%` | `49.95%` | `1.00` | 283,880.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `29.01%` | `70.99%` | `0.41` | 11,990.00 USD |
| `15M` | `HTX` | `42.95%` | `57.05%` | `0.75` | 696,870.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `94.51%` | `5.49%` | `17.21` | 1,140,000.00 USD |
| `15M` | `Aster` | `48.6%` | `51.4%` | `0.95` | 685,970.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `52.22%` | `47.78%` | `1.09` | 98,550.00 USD |
| `15M` | `Whale Positions` | `45.44%` | `54.56%` | `0.83` | 33,050,000.00 USD |
| `15M` | `Global Accounts` | `48.26%` | `51.74%` | `0.93` | 47,820,000.00 USD |
| `1H` | `AVAX` | `46.65%` | `53.35%` | `0.87` | 477,020,000.00 USD |
| `1H` | `Binance` | `46.36%` | `53.64%` | `0.86` | 166,710,000.00 USD |
| `1H` | `OKX` | `46.19%` | `53.81%` | `0.86` | 107,620,000.00 USD |
| `1H` | `Bybit` | `46.87%` | `53.13%` | `0.88` | 42,270,000.00 USD |
| `1H` | `KuCoin` | `49.89%` | `50.11%` | `1.00` | 11,990,000.00 USD |
| `1H` | `Gate` | `47.65%` | `52.35%` | `0.91` | 23,840,000.00 USD |
| `1H` | `Bitget` | `53.1%` | `46.9%` | `1.13` | 19,360,000.00 USD |
| `1H` | `BingX` | `49.95%` | `50.05%` | `1.00` | 12,350,000.00 USD |
| `1H` | `MEXC` | `40.45%` | `59.55%` | `0.68` | 37,780,000.00 USD |
| `1H` | `Bitunix` | `39.54%` | `60.46%` | `0.65` | 17,810,000.00 USD |
| `1H` | `Hyperliquid` | `56.69%` | `43.31%` | `1.31` | 18,400,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.95%` | `46.05%` | `1.17` | 5,820,000.00 USD |
| `1H` | `Crypto.com` | `50.86%` | `49.14%` | `1.04` | 1,250,000.00 USD |
| `1H` | `WhiteBIT` | `18.29%` | `81.71%` | `0.22` | 2,670,000.00 USD |
| `1H` | `HTX` | `61.42%` | `38.58%` | `1.59` | 1,130,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `61.52%` | `38.48%` | `1.60` | 1,970,000.00 USD |
| `1H` | `Aster` | `46.95%` | `53.05%` | `0.89` | 3,050,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.57%` | `47.43%` | `1.11` | 3,020,000.00 USD |
| `1H` | `Whale Positions` | `46.36%` | `53.64%` | `0.86` | 166,710,000.00 USD |
| `1H` | `Global Accounts` | `46.65%` | `53.35%` | `0.87` | 477,020,000.00 USD |
| `4H` | `AVAX` | `48.12%` | `51.88%` | `0.93` | 935,510,000.00 USD |
| `4H` | `Binance` | `49.52%` | `50.48%` | `0.98` | 589,580,000.00 USD |
| `4H` | `OKX` | `49.39%` | `50.61%` | `0.98` | 70,660,000.00 USD |
| `4H` | `Bybit` | `42.06%` | `57.94%` | `0.73` | 77,010,000.00 USD |
| `4H` | `KuCoin` | `52.17%` | `47.83%` | `1.09` | 4,140,000.00 USD |
| `4H` | `Gate` | `46.69%` | `53.31%` | `0.88` | 19,620,000.00 USD |
| `4H` | `Bitget` | `48.71%` | `51.29%` | `0.95` | 15,930,000.00 USD |
| `4H` | `BingX` | `46.24%` | `53.76%` | `0.86` | 11,590,000.00 USD |
| `4H` | `MEXC` | `47.09%` | `52.91%` | `0.89` | 13,060,000.00 USD |
| `4H` | `Bitunix` | `51.71%` | `48.29%` | `1.07` | 22,240,000.00 USD |
| `4H` | `Hyperliquid` | `43.18%` | `56.82%` | `0.76` | 65,310,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.71%` | `50.29%` | `0.99` | 5,290,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `12.76%` | `87.24%` | `0.15` | 1,240,000.00 USD |
| `4H` | `HTX` | `46.78%` | `53.22%` | `0.88` | 2,270,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `68.42%` | `31.58%` | `2.17` | 4,630,000.00 USD |
| `4H` | `Aster` | `45.59%` | `54.41%` | `0.84` | 22,210,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `32.51%` | `67.49%` | `0.48` | 10,740,000.00 USD |
| `4H` | `Whale Positions` | `49.52%` | `50.48%` | `0.98` | 589,580,000.00 USD |
| `4H` | `Global Accounts` | `48.12%` | `51.88%` | `0.93` | 935,510,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

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
| `5m` | 31,320.00 USD | 31,590.00 USD | **`ACCUMULATION`** |
| `15m` | 35,680.00 USD | 146,930.00 USD | **`ACCUMULATION`** |
| `30m` | -17,280.00 USD | -249,320.00 USD | **`DISTRIBUTION`** |
| `1h` | -213,050.00 USD | 209,960.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,580,000.00 USD | -2,680,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -693,250.00 USD | -3,840,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -2,750,000.00 USD | -10,010,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,770,000.00 USD | -12,260,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,570,000.00 USD | -12,670,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,730,000.00 USD | -14,940,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,760,000.00 USD | -56,080,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -57,540,000.00 USD | -279,020,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+31.32K` | 15m=`+35.68K` | 1h=`-213.05K` | 24h=`-2.73M`
* Futures Capital Netflows: 5m=`+31.59K` | 15m=`+146.93K` | 1h=`+209.96K` | 24h=`-14.94M`
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
  * `2026-10-30 05:01:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:15:10 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:01:10 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:02:10 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `8.12` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `7.95` (Risk Distance: `0.1720` pts)
  * +2.5R Take Profit: `8.55`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.40` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.57` (Risk Distance: `0.1720` pts)
  * +2.5R Take Profit: `7.97`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.24`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
