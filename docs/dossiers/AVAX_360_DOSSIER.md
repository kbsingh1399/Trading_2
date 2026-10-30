# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 08:45:54 IST` (`2026-10-30 03:15:54 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.32` | **Live Ask Quote**: `8.36` | **Mid Price**: `8.34`
- **Spread Points**: `4.00` | **Spread BPS**: `47.96 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.16` | VWAP Z-Score: `+1.68` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0944` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `45.27` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `8.37` | Lower -3.00σ Band: `7.95`
  * Upper +2.51σ Band: `8.34` | Lower -2.51σ Band: `7.98`
  * Upper +2.01σ Band: `8.30` | Lower -2.01σ Band: `8.02`
  * Upper +2.00σ Band: `8.30` | Lower -2.00σ Band: `8.02`
  * Upper +1.28σ Band: `8.25` | Lower -1.28σ Band: `8.07`
  * Upper +1.00σ Band: `8.23` | Lower -1.00σ Band: `8.09`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.25` | EMA-20=`8.29` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.46` (Slope: `+0.0000`) | EMA-100=`8.59`
  * Institutional Anchors: EMA-144=`8.65` | EMA-200=`8.69` (Slope: `-0.7108`) | EMA-233=`8.73`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`7.97` | Weekly High=`9.14` | Weekly Low=`7.97`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.40` (Distance: `-0.75%`)
  * Point of Control (POC) = `8.32` (Distance: `+0.22%`)
  * Value Area Low (VAL) = `8.13` (Distance: `+2.52%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`9.01` | Weekly POC=`8.92` | Weekly VAL=`8.73`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.58` | Low=`7.97`
  * London Session (08:00-16:00 UTC): High=`8.37` | Low=`8.31`
  * New York Session (13:00-21:00 UTC): High=`8.39` | Low=`8.29`
  * Initial Balance (First Hour): IB High=`8.37` | IB Low=`8.31`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.31` - `8.37`
  * Optimal Trade Entry (OTE 0.705): `8.36`
  * Structural Invalidation Anchor (0.786): `8.41`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.32` | `8.33` | `8.31` | `8.31` | `35,598` | 296,098.10 USD | -85,003.86 USD | `-28.71%` | -6,238,043.61 USD | `-0.91` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `8.31` | `8.35` | `8.31` | `8.34` | `34,982` | 291,711.35 USD | 54,304.69 USD | `+18.62%` | -6,183,738.93 USD | `+0.30` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `8.34` | `8.36` | `8.33` | `8.36` | `28,185` | 235,195.70 USD | 40,027.82 USD | `+17.02%` | -6,143,711.10 USD | `+0.16` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.32` | `8.35` | `8.30` | `8.35` | `105,169` | 876,108.07 USD | 62,398.85 USD | `+7.12%` | -6,096,681.41 USD | `-0.03` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `8.35` | `8.35` | `8.30` | `8.31` | `101,385` | 843,379.31 USD | -94,068.04 USD | `-11.15%` | -6,190,749.45 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `8.31` | `8.36` | `8.31` | `8.36` | `63,167` | 526,907.05 USD | 94,332.51 USD | `+17.90%` | -6,096,416.94 USD | `+0.14` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `8.21` | `8.28` | `8.11` | `8.21` | `1,052,344` | 8,640,631.11 USD | 498,870.95 USD | `+5.77%` | -6,594,407.45 USD | `+0.51` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `8.21` | `8.35` | `8.15` | `8.31` | `481,486` | 3,984,789.43 USD | 490,929.32 USD | `+12.32%` | -6,103,478.13 USD | `+0.49` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `8.31` | `8.36` | `8.31` | `8.36` | `63,167` | 526,907.05 USD | 94,332.51 USD | `+17.90%` | -6,009,145.62 USD | `+0.25` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,242,979.60 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,578,925.42 USD | `-1.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.36` | `7.99` | `8.36` | `4,418,549` | 36,116,740.73 USD | -430,220.20 USD | `-1.19%` | -6,009,145.62 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | 322,838.02 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | 269,016.05 USD | `-1.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,242,979.60 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,578,925.42 USD | `-1.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.36` | `7.99` | `8.36` | `4,418,549` | 36,116,740.73 USD | -430,220.20 USD | `-1.19%` | -6,009,145.62 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`8.34`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BUY` | `8.19` | `2223.5100` | 18,213.88 USD | 3,831,581.15 USD | `STANDARD` | `-1.96%` | `0xd3943e4008` |
| `BUY` | `8.19` | `250.0000` | 2,048.70 USD | 4,884,638.88 USD | `STANDARD` | `-1.92%` | `0x6abc111bd2` |
| `BUY` | `8.21` | `15570.4600` | 127,808.56 USD | 2,609,132.07 USD | `LARGE (>= USD 100K)` | `-1.76%` | `0xecb63caa47` |
| `BUY` | `8.21` | `4339.9600` | 35,615.88 USD | 3,662,608.24 USD | `MEDIUM (>= USD 25K)` | `-1.78%` | `0xa24c5ca26c` |
| `BUY` | `8.21` | `500.0000` | 4,103.60 USD | 4,748,409.98 USD | `STANDARD` | `-1.77%` | `0x6abc111bd2` |
| `BUY` | `8.22` | `13727.6000` | 112,908.14 USD | 2,977,123.25 USD | `LARGE (>= USD 100K)` | `-1.56%` | `0xecb63caa47` |
| `BUY` | `8.22` | `500.0000` | 4,109.25 USD | 4,744,306.38 USD | `STANDARD` | `-1.64%` | `0x6abc111bd2` |
| `BUY` | `8.22` | `315.7300` | 2,596.56 USD | 4,863,670.85 USD | `STANDARD` | `-1.57%` | `0x07fd993f0f` |
| `BUY` | `8.22` | `210.8900` | 1,733.73 USD | 4,888,384.99 USD | `STANDARD` | `-1.61%` | `0x31ca8395cf` |
| `BUY` | `8.22` | `186.7400` | 1,535.19 USD | 4,891,480.28 USD | `STANDARD` | `-1.61%` | `0x010461c14e` |
| `BUY` | `8.23` | `17664.8000` | 145,298.28 USD | 2,223,893.06 USD | `LARGE (>= USD 100K)` | `-1.56%` | `0x71d0e11ebb` |
| `BUY` | `8.23` | `2308.7300` | 18,999.92 USD | 3,775,782.96 USD | `STANDARD` | `-1.51%` | `0x0efb38a5fa` |
| `BUY` | `8.23` | `500.0000` | 4,117.40 USD | 4,740,197.13 USD | `STANDARD` | `-1.44%` | `0x6abc111bd2` |
| `BUY` | `8.24` | `39247.0700` | 323,580.32 USD | 1,300,810.71 USD | `LARGE (>= USD 100K)` | `-1.33%` | `0x71cfa5e263` |
| `BUY` | `8.24` | `11809.8100` | 97,332.91 USD | 3,379,843.85 USD | `MEDIUM (>= USD 25K)` | `-1.36%` | `0xecb63caa47` |
| `BUY` | `8.25` | `7678.0500` | 63,315.50 USD | 3,586,529.16 USD | `MEDIUM (>= USD 25K)` | `-1.31%` | `0x71d0e11ebb` |
| `BUY` | `8.25` | `1939.4400` | 15,999.99 USD | 3,865,410.48 USD | `STANDARD` | `-1.26%` | `0x0efb38a5fa` |
| `BUY` | `8.25` | `962.0800` | 7,941.39 USD | 4,650,901.48 USD | `STANDARD` | `-1.21%` | `0xd2ccf2ebc5` |
| `BUY` | `8.25` | `150.0000` | 1,237.20 USD | 4,895,744.24 USD | `STANDARD` | `-1.29%` | `0x6abc111bd2` |
| `BUY` | `8.25` | `81.0000` | 668.58 USD | 4,943,319.19 USD | `STANDARD` | `-1.21%` | `0x010461c14e` |
| `BUY` | `8.25` | `77.3900` | 638.80 USD | 4,947,834.58 USD | `STANDARD` | `-1.21%` | `0x31ca8395cf` |
| `BUY` | `8.26` | `12715.9900` | 105,012.46 USD | 3,082,135.71 USD | `LARGE (>= USD 100K)` | `-1.16%` | `0xecb63caa47` |
| `BUY` | `8.26` | `1855.9800` | 15,328.54 USD | 4,364,369.41 USD | `STANDARD` | `-1.15%` | `0xd3943e4008` |
| `BUY` | `8.27` | `17643.4600` | 145,902.59 USD | 2,078,594.79 USD | `LARGE (>= USD 100K)` | `-1.03%` | `0x71d0e11ebb` |
| `BUY` | `8.27` | `2271.7800` | 18,792.16 USD | 3,794,575.13 USD | `STANDARD` | `-1.00%` | `0xa38f19c4cc` |
| `BUY` | `8.27` | `1398.1500` | 11,563.96 USD | 4,438,417.60 USD | `STANDARD` | `-1.01%` | `0xd3943e4008` |
| `BUY` | `8.29` | `12088.9200` | 100,183.30 USD | 3,282,510.94 USD | `LARGE (>= USD 100K)` | `-0.82%` | `0x881cd92459` |
| `BUY` | `8.29` | `1446.8100` | 11,999.99 USD | 4,391,012.37 USD | `STANDARD` | `-0.73%` | `0x0efb38a5fa` |
| `BUY` | `8.29` | `1332.6700` | 11,054.23 USD | 4,449,471.83 USD | `STANDARD` | `-0.73%` | `0xa38f19c4cc` |
| `BUY` | `8.29` | `1306.8300` | 10,834.80 USD | 4,482,344.73 USD | `STANDARD` | `-0.77%` | `0xd3943e4008` |
| `BUY` | `8.30` | `19993.9900` | 165,930.12 USD | 1,634,532.34 USD | `LARGE (>= USD 100K)` | `-0.68%` | `0x71cfa5e263` |
| `BUY` | `8.30` | `15345.2000` | 127,369.76 USD | 2,864,215.11 USD | `LARGE (>= USD 100K)` | `-0.66%` | `0x71d0e11ebb` |
| `BUY` | `8.30` | `3574.7000` | 29,679.66 USD | 3,692,287.90 USD | `MEDIUM (>= USD 25K)` | `-0.63%` | `0x26934acbd3` |
| `BUY` | `8.30` | `1866.9900` | 15,501.43 USD | 4,333,543.92 USD | `STANDARD` | `-0.63%` | `0x57d8e75f47` |
| `BUY` | `8.30` | `1866.9900` | 15,496.95 USD | 4,349,040.87 USD | `STANDARD` | `-0.66%` | `0x57d8e75f47` |
| `BUY` | `8.30` | `477.1600` | 3,960.24 USD | 4,764,422.79 USD | `STANDARD` | `-0.67%` | `0xcd7f60e943` |
| `BUY` | `8.31` | `1866.9900` | 15,522.71 USD | 4,271,505.90 USD | `STANDARD` | `-0.49%` | `0x57d8e75f47` |
| `BUY` | `8.31` | `1866.9900` | 15,517.67 USD | 4,287,023.57 USD | `STANDARD` | `-0.52%` | `0x57d8e75f47` |
| `BUY` | `8.31` | `1866.9900` | 15,512.26 USD | 4,302,535.83 USD | `STANDARD` | `-0.56%` | `0x57d8e75f47` |
| `BUY` | `8.31` | `1866.9900` | 15,506.66 USD | 4,318,042.49 USD | `STANDARD` | `-0.60%` | `0x57d8e75f47` |
| `BUY` | `8.31` | `1093.4600` | 9,089.39 USD | 4,592,216.72 USD | `STANDARD` | `-0.51%` | `0xd3943e4008` |
| `BUY` | `8.31` | `962.7300` | 8,000.00 USD | 4,626,960.41 USD | `STANDARD` | `-0.55%` | `0x0efb38a5fa` |
| `BUY` | `8.31` | `87.8000` | 729.78 USD | 4,937,046.26 USD | `STANDARD` | `-0.52%` | `0x010461c14e` |
| `BUY` | `8.31` | `77.5100` | 643.93 USD | 4,945,915.18 USD | `STANDARD` | `-0.57%` | `0x31ca8395cf` |
| `BUY` | `8.32` | `1866.9900` | 15,542.69 USD | 4,209,383.11 USD | `STANDARD` | `-0.36%` | `0x57d8e75f47` |
| `BUY` | `8.32` | `1866.9900` | 15,538.21 USD | 4,224,921.32 USD | `STANDARD` | `-0.39%` | `0x57d8e75f47` |
| `BUY` | `8.32` | `1866.9900` | 15,533.73 USD | 4,240,455.05 USD | `STANDARD` | `-0.42%` | `0x57d8e75f47` |
| `BUY` | `8.32` | `1866.9900` | 15,528.13 USD | 4,255,983.18 USD | `STANDARD` | `-0.46%` | `0x57d8e75f47` |
| `BUY` | `8.32` | `1060.1600` | 8,820.53 USD | 4,618,960.41 USD | `STANDARD` | `-0.42%` | `0xd3342d3b1e` |
| `BUY` | `8.32` | `764.1400` | 6,356.80 USD | 4,685,926.36 USD | `STANDARD` | `-0.44%` | `0x47a4471457` |
| `BUY` | `8.32` | `632.1400` | 5,261.62 USD | 4,708,969.01 USD | `STANDARD` | `-0.38%` | `0xecb63caa47` |
| `BUY` | `8.32` | `512.0200` | 4,260.57 USD | 4,727,671.38 USD | `STANDARD` | `-0.41%` | `0xecb63caa47` |
| `BUY` | `8.33` | `15338.1700` | 127,713.27 USD | 2,736,845.35 USD | `LARGE (>= USD 100K)` | `-0.35%` | `0x71d0e11ebb` |
| `BUY` | `8.33` | `2730.6900` | 22,747.47 USD | 3,737,783.10 USD | `STANDARD` | `-0.30%` | `0x08a49e7f71` |
| `BUY` | `8.33` | `1866.9900` | 15,552.96 USD | 4,178,291.94 USD | `STANDARD` | `-0.30%` | `0x57d8e75f47` |
| `BUY` | `8.33` | `1866.9900` | 15,548.48 USD | 4,193,840.42 USD | `STANDARD` | `-0.33%` | `0x57d8e75f47` |
| `BUY` | `8.33` | `1197.9600` | 9,982.48 USD | 4,573,588.47 USD | `STANDARD` | `-0.27%` | `0xaf9f722a67` |
| `BUY` | `8.33` | `946.1900` | 7,880.15 USD | 4,658,781.63 USD | `STANDARD` | `-0.32%` | `0xd3943e4008` |
| `BUY` | `8.33` | `780.6600` | 6,502.43 USD | 4,679,569.56 USD | `STANDARD` | `-0.31%` | `0xa38f19c4cc` |
| `BUY` | `8.33` | `599.9400` | 4,999.96 USD | 4,718,968.96 USD | `STANDARD` | `-0.26%` | `0x0efb38a5fa` |
| `BUY` | `8.33` | `467.8500` | 3,897.61 USD | 4,799,642.44 USD | `STANDARD` | `-0.29%` | `0x2a72b57dea` |
| `BUY` | `8.33` | `467.8500` | 3,894.94 USD | 4,803,537.39 USD | `STANDARD` | `-0.36%` | `0x2a72b57dea` |
| `BUY` | `8.33` | `459.1300` | 3,824.92 USD | 4,811,187.23 USD | `STANDARD` | `-0.30%` | `0xa38f19c4cc` |
| `BUY` | `8.33` | `414.0000` | 3,448.21 USD | 4,818,197.09 USD | `STANDARD` | `-0.32%` | `0xecb63caa47` |
| `BUY` | `8.33` | `366.8200` | 3,056.45 USD | 4,839,898.04 USD | `STANDARD` | `-0.28%` | `0xdd4f66125d` |
| `BUY` | `8.33` | `313.8000` | 2,613.89 USD | 4,855,859.46 USD | `STANDARD` | `-0.31%` | `0x26934acbd3` |
| `BUY` | `8.33` | `291.5000` | 2,429.13 USD | 4,873,569.46 USD | `STANDARD` | `-0.27%` | `0xecb63caa47` |
| `BUY` | `8.33` | `90.8100` | 756.33 USD | 4,934,070.02 USD | `STANDARD` | `-0.32%` | `0x010461c14e` |
| `BUY` | `8.33` | `81.2900` | 677.28 USD | 4,941,976.06 USD | `STANDARD` | `-0.28%` | `0x31ca8395cf` |
| `BUY` | `8.34` | `1866.9900` | 15,575.36 USD | 4,116,039.77 USD | `STANDARD` | `-0.15%` | `0x57d8e75f47` |
| `BUY` | `8.34` | `1866.9900` | 15,570.88 USD | 4,131,610.66 USD | `STANDARD` | `-0.18%` | `0x57d8e75f47` |
| `BUY` | `8.34` | `1866.9900` | 15,566.40 USD | 4,147,177.06 USD | `STANDARD` | `-0.21%` | `0x57d8e75f47` |
| `BUY` | `8.34` | `1866.9900` | 15,561.92 USD | 4,162,738.98 USD | `STANDARD` | `-0.24%` | `0x57d8e75f47` |
| `BUY` | `8.34` | `1246.5500` | 10,393.73 USD | 4,513,556.49 USD | `STANDARD` | `-0.21%` | `0x26934acbd3` |
| `BUY` | `8.34` | `1197.9600` | 9,992.42 USD | 4,563,605.99 USD | `STANDARD` | `-0.17%` | `0xaf9f722a67` |
| `BUY` | `8.34` | `1143.3100` | 9,538.86 USD | 4,583,127.34 USD | `STANDARD` | `-0.15%` | `0x08a49e7f71` |
| `BUY` | `8.34` | `503.3000` | 4,198.03 USD | 4,736,079.73 USD | `STANDARD` | `-0.17%` | `0x71d0e11ebb` |
| `BUY` | `8.34` | `481.6400` | 4,015.91 USD | 4,756,457.46 USD | `STANDARD` | `-0.21%` | `0x7717a7a245` |
| `BUY` | `8.34` | `467.8500` | 3,902.52 USD | 4,791,844.83 USD | `STANDARD` | `-0.17%` | `0x2a72b57dea` |
| `BUY` | `8.34` | `467.8500` | 3,900.00 USD | 4,795,744.83 USD | `STANDARD` | `-0.23%` | `0x2a72b57dea` |
| `BUY` | `8.34` | `427.1900` | 3,561.65 USD | 4,814,748.89 USD | `STANDARD` | `-0.22%` | `0xecb63caa47` |
| `BUY` | `8.34` | `396.7300` | 3,310.28 USD | 4,821,507.37 USD | `STANDARD` | `-0.14%` | `0xecb63caa47` |
| `BUY` | `8.34` | `366.8200` | 3,060.27 USD | 4,833,783.99 USD | `STANDARD` | `-0.15%` | `0xdd4f66125d` |
| `BUY` | `8.34` | `366.8200` | 3,057.59 USD | 4,836,841.58 USD | `STANDARD` | `-0.24%` | `0xdd4f66125d` |
| `BUY` | `8.34` | `320.2800` | 2,671.04 USD | 4,845,255.94 USD | `STANDARD` | `-0.19%` | `0xecb63caa47` |
| `BUY` | `8.34` | `320.1000` | 2,670.21 USD | 4,847,926.15 USD | `STANDARD` | `-0.16%` | `0xecb63caa47` |
| `BUY` | `8.34` | `271.9700` | 2,267.99 USD | 4,875,837.44 USD | `STANDARD` | `-0.20%` | `0x33ad48ed92` |
| `BUY` | `8.34` | `269.7400` | 2,249.98 USD | 4,880,340.23 USD | `STANDARD` | `-0.17%` | `0xa38f19c4cc` |
| `BUY` | `8.34` | `81.6400` | 681.05 USD | 4,941,298.78 USD | `STANDARD` | `-0.16%` | `0x010461c14e` |
| `BUY` | `8.34` | `80.8600` | 674.54 USD | 4,942,650.60 USD | `STANDARD` | `-0.16%` | `0x31ca8395cf` |
| `BUY` | `8.34` | `60.3400` | 503.32 USD | 4,952,121.82 USD | `STANDARD` | `-0.17%` | `0x57d8e75f47` |
| `BID` | `8.35` | `128.8700` | 1,076.61 USD | 1,076.61 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.35` | `718.1900` | 5,999.54 USD | 7,076.15 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.35` | `187.6000` | 1,567.14 USD | 8,643.28 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `8.35` | `103.1000` | 861.25 USD | 9,504.53 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.35` | `16.4600` | 137.50 USD | 9,642.03 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.35` | `957.7200` | 7,999.74 USD | 17,641.77 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.35` | `103.1000` | 861.17 USD | 18,502.94 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.35` | `120.0800` | 1,002.94 USD | 19,505.88 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.35` | `77.3200` | 645.79 USD | 20,151.68 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.35` | `19.5200` | 163.03 USD | 20,314.71 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.35` | `153.1000` | 1,278.68 USD | 21,593.38 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `8.35` | `94.7700` | 791.47 USD | 22,384.85 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.35` | `164.4100` | 1,373.02 USD | 23,757.87 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.35` | `103.1000` | 860.97 USD | 24,618.84 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.35` | `153.1000` | 1,278.49 USD | 25,897.33 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `8.35` | `103.1000` | 860.95 USD | 26,758.28 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.35` | `1197.5500` | 9,999.90 USD | 36,758.18 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.35` | `5.8000` | 48.43 USD | 36,806.61 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `8.35` | `29.9200` | 249.83 USD | 37,056.45 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.35` | `5.6000` | 46.76 USD | 37,103.21 USD | `1 orders` | `-0.07%` | `-` |
| `BUY` | `8.35` | `1866.9900` | 15,586.75 USD | 4,084,883.44 USD | `STANDARD` | `-0.08%` | `0x57d8e75f47` |
| `BUY` | `8.35` | `1866.9900` | 15,580.97 USD | 4,100,464.41 USD | `STANDARD` | `-0.12%` | `0x57d8e75f47` |
| `BUY` | `8.35` | `1437.5500` | 11,998.94 USD | 4,415,011.23 USD | `STANDARD` | `-0.10%` | `0x7d0c59691f` |
| `BUY` | `8.35` | `1245.4400` | 10,398.30 USD | 4,503,162.75 USD | `STANDARD` | `-0.08%` | `0x621c555167` |
| `BUY` | `8.35` | `1197.9600` | 10,002.49 USD | 4,543,613.66 USD | `STANDARD` | `-0.07%` | `0xaf9f722a67` |
| `BUY` | `8.35` | `1197.5500` | 9,999.90 USD | 4,553,613.57 USD | `STANDARD` | `-0.06%` | `0x7d0c59691f` |
| `BUY` | `8.35` | `957.7200` | 7,999.74 USD | 4,642,960.08 USD | `STANDARD` | `-0.03%` | `0x7d0c59691f` |
| `BUY` | `8.35` | `718.1900` | 5,999.54 USD | 4,698,282.70 USD | `STANDARD` | `-0.02%` | `0x7d0c59691f` |
| `BUY` | `8.35` | `467.8500` | 3,904.91 USD | 4,787,942.31 USD | `STANDARD` | `-0.11%` | `0x2a72b57dea` |
| `BUY` | `8.35` | `312.0500` | 2,604.53 USD | 4,861,074.28 USD | `STANDARD` | `-0.11%` | `0x7717a7a245` |
| `BUY` | `8.35` | `299.5500` | 2,499.92 USD | 4,868,670.76 USD | `STANDARD` | `-0.12%` | `0x0efb38a5fa` |
| `BUY` | `8.35` | `145.5000` | 1,215.45 USD | 4,896,959.69 USD | `STANDARD` | `-0.02%` | `0x727956612a` |
| `BUY` | `8.35` | `137.5600` | 1,148.50 USD | 4,900,429.21 USD | `STANDARD` | `-0.08%` | `0xdd4f66125d` |
| `BUY` | `8.35` | `137.5600` | 1,148.36 USD | 4,901,577.58 USD | `STANDARD` | `-0.09%` | `0xdd4f66125d` |
| `BUY` | `8.35` | `137.5600` | 1,148.35 USD | 4,902,725.93 USD | `STANDARD` | `-0.09%` | `0xdd4f66125d` |
| `BUY` | `8.35` | `128.8700` | 1,076.61 USD | 4,903,802.53 USD | `STANDARD` | `-0.01%` | `0xea0e878d5d` |
| `BUY` | `8.35` | `120.0800` | 1,002.94 USD | 4,905,809.25 USD | `STANDARD` | `-0.04%` | `0x7717a7a245` |
| `BUY` | `8.35` | `103.1000` | 861.25 USD | 4,925,915.73 USD | `STANDARD` | `-0.02%` | `0xd0956a1eba` |
| `BUY` | `8.35` | `103.1000` | 861.17 USD | 4,926,776.90 USD | `STANDARD` | `-0.03%` | `0x63f6411ca6` |
| `BUY` | `8.35` | `103.1000` | 861.08 USD | 4,927,637.98 USD | `STANDARD` | `-0.04%` | `0xf30120f048` |
| `BUY` | `8.35` | `103.1000` | 860.97 USD | 4,928,498.95 USD | `STANDARD` | `-0.06%` | `0x53136b4a7c` |
| `BUY` | `8.35` | `103.1000` | 860.96 USD | 4,929,359.91 USD | `STANDARD` | `-0.06%` | `0x9d81a3adf8` |
| `BUY` | `8.35` | `103.0800` | 860.82 USD | 4,930,220.73 USD | `STANDARD` | `-0.05%` | `0xa382fa9f4b` |
| `BUY` | `8.35` | `94.7700` | 791.47 USD | 4,931,012.20 USD | `STANDARD` | `-0.05%` | `0xecb63caa47` |
| `BUY` | `8.35` | `88.2600` | 737.08 USD | 4,936,316.48 USD | `STANDARD` | `-0.05%` | `0x010461c14e` |
| `BUY` | `8.35` | `77.3200` | 645.79 USD | 4,945,271.25 USD | `STANDARD` | `-0.04%` | `0xd0956a1eba` |
| `BUY` | `8.35` | `76.1500` | 635.94 USD | 4,948,470.52 USD | `STANDARD` | `-0.05%` | `0x31ca8395cf` |
| `BUY` | `8.35` | `67.9900` | 567.40 USD | 4,949,037.92 USD | `STANDARD` | `-0.12%` | `0x33ad48ed92` |
| `BUY` | `8.35` | `60.3400` | 503.64 USD | 4,951,618.50 USD | `STANDARD` | `-0.10%` | `0x57d8e75f47` |
| `ASK` | `8.36` | `194.8000` | 1,628.98 USD | 15,786.72 USD | `2 orders` | `+0.08%` | `-` |
| `ASK` | `8.36` | `103.1000` | 862.11 USD | 14,157.74 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `8.36` | `5.8000` | 48.50 USD | 13,295.63 USD | `2 orders` | `+0.07%` | `-` |
| `ASK` | `8.36` | `103.0800` | 861.88 USD | 13,247.14 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.36` | `165.6900` | 1,385.37 USD | 12,385.25 USD | `3 orders` | `+0.07%` | `-` |
| `ASK` | `8.36` | `11.4300` | 95.57 USD | 10,999.89 USD | `2 orders` | `+0.07%` | `-` |
| `ASK` | `8.36` | `60.3400` | 504.49 USD | 10,904.32 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.36` | `125.1900` | 1,046.68 USD | 10,399.83 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.36` | `133.0000` | 1,111.96 USD | 9,353.15 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.36` | `103.1000` | 861.87 USD | 8,241.19 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.36` | `76.4200` | 638.83 USD | 7,379.32 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.36` | `5.9800` | 49.99 USD | 6,740.49 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.36` | `120.0800` | 1,003.77 USD | 6,690.50 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.36` | `100.3100` | 838.48 USD | 5,686.72 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.36` | `22.6800` | 189.58 USD | 4,848.24 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.36` | `103.1000` | 861.77 USD | 4,658.67 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.36` | `103.1000` | 861.70 USD | 3,796.89 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.36` | `103.0800` | 861.52 USD | 2,935.19 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.36` | `103.0800` | 861.45 USD | 2,073.67 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.36` | `145.0600` | 1,212.22 USD | 1,212.22 USD | `1 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `8.36` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.36` | `0.00%` | `-` |
| `SELL` | `8.36` | `1866.9900` | 15,612.52 USD | 4,069,296.69 USD | `STANDARD` | `+0.08%` | `0x57d8e75f47` |
| `SELL` | `8.36` | `467.8500` | 3,913.47 USD | 4,784,037.40 USD | `STANDARD` | `+0.11%` | `0x2a72b57dea` |
| `SELL` | `8.36` | `298.9100` | 2,499.99 USD | 4,866,170.84 USD | `STANDARD` | `+0.10%` | `0x0efb38a5fa` |
| `SELL` | `8.36` | `269.0100` | 2,249.95 USD | 4,882,590.18 USD | `STANDARD` | `+0.10%` | `0xa38f19c4cc` |
| `SELL` | `8.36` | `140.0900` | 1,170.68 USD | 4,898,130.36 USD | `STANDARD` | `+0.01%` | `0x727956612a` |
| `SELL` | `8.36` | `137.5600` | 1,150.35 USD | 4,899,280.71 USD | `STANDARD` | `+0.08%` | `0xdd4f66125d` |
| `SELL` | `8.36` | `120.0800` | 1,003.77 USD | 4,904,806.31 USD | `STANDARD` | `+0.04%` | `0x7717a7a245` |
| `SELL` | `8.36` | `119.5700` | 999.94 USD | 4,906,809.19 USD | `STANDARD` | `+0.09%` | `0x27c9fa86c9` |
| `SELL` | `8.36` | `119.6000` | 999.94 USD | 4,907,809.13 USD | `STANDARD` | `+0.06%` | `0x0eecd62efb` |
| `SELL` | `8.36` | `103.1000` | 862.40 USD | 4,912,986.99 USD | `STANDARD` | `+0.11%` | `0x9d81a3adf8` |
| `SELL` | `8.36` | `103.0800` | 862.25 USD | 4,915,573.93 USD | `STANDARD` | `+0.11%` | `0x63f6411ca6` |
| `SELL` | `8.36` | `103.0800` | 862.17 USD | 4,916,436.11 USD | `STANDARD` | `+0.10%` | `0xfd66e33095` |
| `SELL` | `8.36` | `103.1000` | 862.15 USD | 4,917,298.26 USD | `STANDARD` | `+0.08%` | `0xf30120f048` |
| `SELL` | `8.36` | `103.1000` | 862.11 USD | 4,918,160.37 USD | `STANDARD` | `+0.08%` | `0xa382fa9f4b` |
| `SELL` | `8.36` | `103.0800` | 862.10 USD | 4,919,022.47 USD | `STANDARD` | `+0.10%` | `0x53136b4a7c` |
| `SELL` | `8.36` | `103.0800` | 861.88 USD | 4,919,884.35 USD | `STANDARD` | `+0.07%` | `0xf30120f048` |
| `SELL` | `8.36` | `103.1000` | 861.87 USD | 4,920,746.23 USD | `STANDARD` | `+0.05%` | `0xa382fa9f4b` |
| `SELL` | `8.36` | `103.0800` | 861.81 USD | 4,921,608.04 USD | `STANDARD` | `+0.06%` | `0xa382fa9f4b` |
| `SELL` | `8.36` | `103.1000` | 861.77 USD | 4,922,469.81 USD | `STANDARD` | `+0.04%` | `0xfd66e33095` |
| `SELL` | `8.36` | `103.1000` | 861.70 USD | 4,923,331.51 USD | `STANDARD` | `+0.03%` | `0xea0e878d5d` |
| `SELL` | `8.36` | `103.0800` | 861.52 USD | 4,924,193.03 USD | `STANDARD` | `+0.03%` | `0x9d81a3adf8` |
| `SELL` | `8.36` | `103.0800` | 861.45 USD | 4,925,054.48 USD | `STANDARD` | `+0.02%` | `0x9d81a3adf8` |
| `SELL` | `8.36` | `91.7000` | 766.82 USD | 4,933,313.69 USD | `STANDARD` | `+0.08%` | `0xdd4f66125d` |
| `SELL` | `8.36` | `87.2000` | 729.10 USD | 4,937,775.36 USD | `STANDARD` | `+0.07%` | `0x31ca8395cf` |
| `SELL` | `8.36` | `77.3300` | 646.39 USD | 4,944,625.46 USD | `STANDARD` | `+0.04%` | `0x9d81a3adf8` |
| `SELL` | `8.36` | `76.5400` | 639.97 USD | 4,947,195.78 USD | `STANDARD` | `+0.07%` | `0x010461c14e` |
| `SELL` | `8.36` | `67.2800` | 562.74 USD | 4,949,600.66 USD | `STANDARD` | `+0.10%` | `0x33ad48ed92` |
| `SELL` | `8.36` | `60.3400` | 504.74 USD | 4,950,610.37 USD | `STANDARD` | `+0.11%` | `0x57d8e75f47` |
| `SELL` | `8.36` | `60.3400` | 504.49 USD | 4,951,114.86 USD | `STANDARD` | `+0.06%` | `0x57d8e75f47` |
| `SELL` | `8.37` | `1866.9900` | 15,634.92 USD | 4,022,440.66 USD | `STANDARD` | `+0.23%` | `0x57d8e75f47` |
| `SELL` | `8.37` | `1866.9900` | 15,626.15 USD | 4,038,066.80 USD | `STANDARD` | `+0.17%` | `0x57d8e75f47` |
| `SELL` | `8.37` | `1866.9900` | 15,617.37 USD | 4,053,684.17 USD | `STANDARD` | `+0.11%` | `0x57d8e75f47` |
| `SELL` | `8.37` | `1245.4400` | 10,419.72 USD | 4,492,764.45 USD | `STANDARD` | `+0.13%` | `0x621c555167` |
| `SELL` | `8.37` | `1197.9600` | 10,032.32 USD | 4,523,588.80 USD | `STANDARD` | `+0.23%` | `0xaf9f722a67` |
| `SELL` | `8.37` | `1197.9600` | 10,022.37 USD | 4,533,611.18 USD | `STANDARD` | `+0.13%` | `0xaf9f722a67` |
| `SELL` | `8.37` | `776.4400` | 6,502.45 USD | 4,673,067.13 USD | `STANDARD` | `+0.23%` | `0xa38f19c4cc` |
| `SELL` | `8.37` | `503.2600` | 4,210.32 USD | 4,731,881.70 USD | `STANDARD` | `+0.13%` | `0x71d0e11ebb` |
| `SELL` | `8.37` | `481.6400` | 4,031.57 USD | 4,752,441.54 USD | `STANDARD` | `+0.18%` | `0x7717a7a245` |
| `SELL` | `8.37` | `467.8500` | 3,918.20 USD | 4,780,123.93 USD | `STANDARD` | `+0.23%` | `0x2a72b57dea` |
| `SELL` | `8.37` | `457.0900` | 3,824.93 USD | 4,807,362.31 USD | `STANDARD` | `+0.15%` | `0xa38f19c4cc` |
| `SELL` | `8.37` | `366.8200` | 3,071.53 USD | 4,827,653.26 USD | `STANDARD` | `+0.21%` | `0xdd4f66125d` |
| `SELL` | `8.37` | `366.8200` | 3,070.47 USD | 4,830,723.72 USD | `STANDARD` | `+0.18%` | `0xdd4f66125d` |
| `SELL` | `8.37` | `312.0500` | 2,610.30 USD | 4,858,469.76 USD | `STANDARD` | `+0.11%` | `0x7717a7a245` |
| `SELL` | `8.37` | `295.0600` | 2,469.56 USD | 4,871,140.33 USD | `STANDARD` | `+0.17%` | `0xecb63caa47` |
| `SELL` | `8.37` | `269.1300` | 2,252.81 USD | 4,878,090.25 USD | `STANDARD` | `+0.18%` | `0x33ad48ed92` |
| `SELL` | `8.37` | `240.4000` | 2,012.39 USD | 4,886,651.26 USD | `STANDARD` | `+0.19%` | `0x39bac00809` |
| `SELL` | `8.37` | `103.1000` | 863.39 USD | 4,908,672.52 USD | `STANDARD` | `+0.23%` | `0xd0956a1eba` |
| `SELL` | `8.37` | `103.0800` | 863.18 USD | 4,909,535.70 USD | `STANDARD` | `+0.22%` | `0x53136b4a7c` |
| `SELL` | `8.37` | `103.0800` | 863.11 USD | 4,910,398.81 USD | `STANDARD` | `+0.21%` | `0xa382fa9f4b` |
| `SELL` | `8.37` | `103.0800` | 863.04 USD | 4,911,261.85 USD | `STANDARD` | `+0.20%` | `0xf30120f048` |
| `SELL` | `8.37` | `103.0800` | 862.74 USD | 4,912,124.59 USD | `STANDARD` | `+0.17%` | `0xea0e878d5d` |
| `SELL` | `8.37` | `103.0800` | 862.37 USD | 4,913,849.35 USD | `STANDARD` | `+0.13%` | `0x9d81a3adf8` |
| `SELL` | `8.37` | `103.0800` | 862.33 USD | 4,914,711.68 USD | `STANDARD` | `+0.12%` | `0xfd66e33095` |
| `SELL` | `8.37` | `91.7000` | 767.38 USD | 4,931,779.58 USD | `STANDARD` | `+0.15%` | `0xdd4f66125d` |
| `SELL` | `8.37` | `91.7000` | 767.29 USD | 4,932,546.87 USD | `STANDARD` | `+0.14%` | `0xdd4f66125d` |
| `SELL` | `8.37` | `85.0200` | 711.33 USD | 4,939,210.50 USD | `STANDARD` | `+0.13%` | `0x31ca8395cf` |
| `SELL` | `8.37` | `84.9100` | 710.54 USD | 4,939,921.04 USD | `STANDARD` | `+0.15%` | `0x010461c14e` |
| `SELL` | `8.37` | `60.3400` | 504.97 USD | 4,950,105.63 USD | `STANDARD` | `+0.16%` | `0x57d8e75f47` |
| `SELL` | `8.38` | `15343.3300` | 128,520.34 USD | 2,481,323.51 USD | `LARGE (>= USD 100K)` | `+0.25%` | `0x71d0e11ebb` |
| `SELL` | `8.38` | `2714.0400` | 22,747.73 USD | 3,715,035.63 USD | `STANDARD` | `+0.31%` | `0x08a49e7f71` |
| `SELL` | `8.38` | `1866.9900` | 15,652.47 USD | 3,991,162.04 USD | `STANDARD` | `+0.34%` | `0x57d8e75f47` |
| `SELL` | `8.38` | `1866.9900` | 15,643.70 USD | 4,006,805.73 USD | `STANDARD` | `+0.28%` | `0x57d8e75f47` |
| `SELL` | `8.38` | `1318.3300` | 11,054.20 USD | 4,460,526.02 USD | `STANDARD` | `+0.35%` | `0xa38f19c4cc` |
| `SELL` | `8.38` | `928.7200` | 7,783.05 USD | 4,666,564.68 USD | `STANDARD` | `+0.30%` | `0xd3943e4008` |
| `SELL` | `8.38` | `647.5700` | 5,424.69 USD | 4,703,707.40 USD | `STANDARD` | `+0.26%` | `0xecb63caa47` |
| `SELL` | `8.38` | `596.8500` | 4,999.99 USD | 4,713,969.00 USD | `STANDARD` | `+0.26%` | `0x0efb38a5fa` |
| `SELL` | `8.38` | `529.9200` | 4,441.84 USD | 4,723,410.81 USD | `STANDARD` | `+0.32%` | `0xecb63caa47` |
| `SELL` | `8.38` | `467.8500` | 3,922.92 USD | 4,776,205.73 USD | `STANDARD` | `+0.35%` | `0x2a72b57dea` |
| `SELL` | `8.38` | `366.8200` | 3,074.36 USD | 4,824,581.73 USD | `STANDARD` | `+0.31%` | `0xdd4f66125d` |
| `SELL` | `8.38` | `89.9600` | 753.86 USD | 4,935,579.40 USD | `STANDARD` | `+0.29%` | `0x31ca8395cf` |
| `SELL` | `8.38` | `78.7700` | 659.88 USD | 4,943,979.07 USD | `STANDARD` | `+0.26%` | `0x010461c14e` |
| `SELL` | `8.39` | `1866.9900` | 15,670.02 USD | 3,959,848.32 USD | `STANDARD` | `+0.45%` | `0x57d8e75f47` |
| `SELL` | `8.39` | `1866.9900` | 15,661.25 USD | 3,975,509.57 USD | `STANDARD` | `+0.40%` | `0x57d8e75f47` |
| `SELL` | `8.39` | `1076.4300` | 9,026.40 USD | 4,601,243.13 USD | `STANDARD` | `+0.36%` | `0xd3943e4008` |
| `SELL` | `8.39` | `1060.1600` | 8,896.76 USD | 4,610,139.88 USD | `STANDARD` | `+0.44%` | `0xd3342d3b1e` |
| `SELL` | `8.39` | `757.5100` | 6,356.80 USD | 4,692,283.16 USD | `STANDARD` | `+0.43%` | `0x47a4471457` |
| `SELL` | `8.39` | `477.2000` | 4,005.09 USD | 4,760,462.55 USD | `STANDARD` | `+0.45%` | `0xcd7f60e943` |
| `SELL` | `8.39` | `315.7300` | 2,650.55 USD | 4,853,245.57 USD | `STANDARD` | `+0.47%` | `0x07fd993f0f` |
| `SELL` | `8.40` | `19981.8400` | 167,791.51 USD | 1,468,602.21 USD | `LARGE (>= USD 100K)` | `+0.50%` | `0x71cfa5e263` |
| `SELL` | `8.40` | `15353.5700` | 128,910.11 USD | 2,352,803.17 USD | `LARGE (>= USD 100K)` | `+0.49%` | `0x71d0e11ebb` |
| `SELL` | `8.40` | `2237.0000` | 18,792.14 USD | 3,813,367.27 USD | `STANDARD` | `+0.54%` | `0xa38f19c4cc` |
| `SELL` | `8.40` | `1866.9900` | 15,687.57 USD | 3,928,499.51 USD | `STANDARD` | `+0.56%` | `0x57d8e75f47` |
| `SELL` | `8.40` | `1866.9900` | 15,678.80 USD | 3,944,178.30 USD | `STANDARD` | `+0.51%` | `0x57d8e75f47` |
| `SELL` | `8.40` | `1409.3400` | 11,842.40 USD | 4,426,853.64 USD | `STANDARD` | `+0.57%` | `0xd3943e4008` |
| `SELL` | `8.40` | `1307.2500` | 10,983.91 USD | 4,471,509.93 USD | `STANDARD` | `+0.56%` | `0xd3943e4008` |
| `SELL` | `8.40` | `952.7700` | 7,999.93 USD | 4,634,960.34 USD | `STANDARD` | `+0.49%` | `0x0efb38a5fa` |
| `SELL` | `8.40` | `467.8500` | 3,927.65 USD | 4,772,282.81 USD | `STANDARD` | `+0.47%` | `0x2a72b57dea` |
| `SELL` | `8.40` | `86.1600` | 723.81 USD | 4,938,499.17 USD | `STANDARD` | `+0.54%` | `0x010461c14e` |
| `SELL` | `8.40` | `82.9100` | 696.68 USD | 4,940,617.73 USD | `STANDARD` | `+0.57%` | `0x31ca8395cf` |
| `SELL` | `8.41` | `39295.5300` | 330,660.10 USD | 977,230.39 USD | `LARGE (>= USD 100K)` | `+0.71%` | `0x71cfa5e263` |
| `SELL` | `8.41` | `1866.9900` | 15,705.12 USD | 3,897,115.59 USD | `STANDARD` | `+0.68%` | `0x57d8e75f47` |
| `SELL` | `8.41` | `1866.9900` | 15,696.35 USD | 3,912,811.94 USD | `STANDARD` | `+0.62%` | `0x57d8e75f47` |
| `SELL` | `8.41` | `467.8500` | 3,932.37 USD | 4,768,355.16 USD | `STANDARD` | `+0.60%` | `0x2a72b57dea` |
| `SELL` | `8.42` | `11893.6300` | 100,191.94 USD | 3,182,327.65 USD | `LARGE (>= USD 100K)` | `+0.82%` | `0x881cd92459` |
| `SELL` | `8.42` | `1425.4400` | 11,999.92 USD | 4,403,012.29 USD | `STANDARD` | `+0.75%` | `0x0efb38a5fa` |
| `SELL` | `8.43` | `17643.4600` | 148,750.25 USD | 1,932,692.19 USD | `LARGE (>= USD 100K)` | `+0.90%` | `0x71d0e11ebb` |
| `SELL` | `8.43` | `9316.6000` | 78,519.37 USD | 3,458,363.23 USD | `MEDIUM (>= USD 25K)` | `+0.87%` | `0xecb63caa47` |
| `SELL` | `8.43` | `4802.6400` | 40,463.20 USD | 3,626,992.36 USD | `MEDIUM (>= USD 25K)` | `+0.83%` | `0xa24c5ca26c` |
| `SELL` | `8.43` | `89.6400` | 755.51 USD | 4,934,825.54 USD | `STANDARD` | `+0.87%` | `0x010461c14e` |
| `SELL` | `8.43` | `75.9500` | 640.63 USD | 4,946,555.81 USD | `STANDARD` | `+0.95%` | `0x31ca8395cf` |
| `SELL` | `8.44` | `2111.3800` | 17,829.34 USD | 3,849,410.49 USD | `STANDARD` | `+1.06%` | `0xd3943e4008` |
| `SELL` | `8.44` | `1734.2300` | 14,642.97 USD | 4,379,012.38 USD | `STANDARD` | `+1.05%` | `0xd3943e4008` |
| `SELL` | `8.45` | `7674.9700` | 64,850.43 USD | 3,523,213.65 USD | `MEDIUM (>= USD 25K)` | `+1.13%` | `0x71d0e11ebb` |
| `SELL` | `8.45` | `315.7300` | 2,668.87 USD | 4,850,595.01 USD | `STANDARD` | `+1.17%` | `0x07fd993f0f` |
| `SELL` | `8.46` | `17654.4500` | 149,409.61 USD | 1,783,941.95 USD | `LARGE (>= USD 100K)` | `+1.29%` | `0x71d0e11ebb` |
| `SELL` | `8.46` | `1891.9900` | 15,999.99 USD | 3,881,410.47 USD | `STANDARD` | `+1.21%` | `0x0efb38a5fa` |
| `SELL` | `8.47` | `76292.3800` | 646,570.29 USD | 646,570.29 USD | `LARGE (>= USD 100K)` | `+1.43%` | `0x71cfa5e263` |
| `SELL` | `8.47` | `184.2200` | 1,560.10 USD | 4,889,945.09 USD | `STANDARD` | `+1.36%` | `0x010461c14e` |
| `SELL` | `8.47` | `178.6600` | 1,513.75 USD | 4,892,994.03 USD | `STANDARD` | `+1.40%` | `0x31ca8395cf` |
| `SELL` | `8.48` | `2240.1100` | 18,999.94 USD | 3,756,783.04 USD | `STANDARD` | `+1.51%` | `0x0efb38a5fa` |
| `SELL` | `8.49` | `178.2500` | 1,513.00 USD | 4,894,507.04 USD | `STANDARD` | `+1.59%` | `0xdadbb4b2a0` |
| `SELL` | `8.51` | `315.7300` | 2,686.86 USD | 4,842,584.90 USD | `STANDARD` | `+1.85%` | `0x07fd993f0f` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:40:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1501` | `0x7737...bf66` | `SHORT` | 1,431,529.58 USD | `171,568.06` | `7.43` | `8.35` | `104.56` | -155,984.56 USD | `-10.90%` | `10X Cross` |
| `1579` | `0xeadc...9d55` | `LONG` | 1,335,116.53 USD | `160,070.56` | `8.11` | `8.35` | `0.000000` | 37,478.95 USD | `+2.81%` | `10X Cross` |

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
| `Live` | `Long` | `1.69` | 2,290,000.00 USD | 0.00 USD | 793.33 USD | `-79.72%` | `470.82` |
| `Live` | `Long` | `1.93` | 2,290,000.00 USD | 0.00 USD | 221.37 USD | `-76.83%` | `115.00` |
| `Live` | `Long` | `1.94` | 2,290,000.00 USD | 0.00 USD | 595.77 USD | `-76.71%` | `307.89` |
| `Live` | `Long` | `1.98` | 2,290,000.00 USD | 0.00 USD | 218.85 USD | `-76.23%` | `110.81` |
| `Live` | `Long` | `2.00` | 2,290,000.00 USD | 0.00 USD | 160.40 USD | `-75.87%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,290,000.00 USD | 0.00 USD | 110.52 USD | `-75.51%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,290,000.00 USD | 0.00 USD | 4,920.00 USD | `-75.15%` | `2,382.76` |
| `Live` | `Long` | `2.08` | 2,280,000.00 USD | 0.00 USD | 1,350.00 USD | `-74.91%` | `647.30` |
| `Live` | `Long` | `2.23` | 2,280,000.00 USD | 0.00 USD | 257.03 USD | `-73.10%` | `115.00` |
| `Live` | `Long` | `2.25` | 2,280,000.00 USD | 0.00 USD | 903.69 USD | `-72.86%` | `400.75` |
| `Live` | `Long` | `2.31` | 2,280,000.00 USD | 0.00 USD | 265.08 USD | `-72.26%` | `115.00` |
| `Live` | `Long` | `2.33` | 2,280,000.00 USD | 0.00 USD | 583.75 USD | `-71.90%` | `250.00` |
| `Live` | `Long` | `2.35` | 2,280,000.00 USD | 0.00 USD | 164.85 USD | `-71.66%` | `70.00` |
| `Live` | `Long` | `2.40` | 2,280,000.00 USD | 0.00 USD | 275.43 USD | `-71.18%` | `115.00` |
| `Live` | `Long` | `2.52` | 2,280,000.00 USD | 0.00 USD | 126.65 USD | `-69.61%` | `50.16` |
| `Live` | `Long` | `2.60` | 2,280,000.00 USD | 0.00 USD | 128.76 USD | `-68.77%` | `49.62` |
| `Live` | `Long` | `2.69` | 2,280,000.00 USD | 0.00 USD | 942.44 USD | `-67.69%` | `351.00` |
| `Live` | `Long` | `2.87` | 2,280,000.00 USD | 0.00 USD | 3,920.00 USD | `-65.52%` | `1,369.24` |
| `Live` | `Long` | `2.94` | 2,270,000.00 USD | 0.00 USD | 44,510.00 USD | `-64.68%` | `15,165.76` |
| `Live` | `Long` | `2.96` | 2,230,000.00 USD | 0.00 USD | 340.97 USD | `-64.32%` | `115.00` |
| `Live` | `Long` | `2.98` | 2,230,000.00 USD | 0.00 USD | 111.12 USD | `-64.20%` | `37.35` |
| `Live` | `Long` | `3.02` | 2,230,000.00 USD | 0.00 USD | 574.72 USD | `-63.60%` | `189.99` |
| `Live` | `Long` | `3.10` | 2,230,000.00 USD | 0.00 USD | 161.46 USD | `-62.63%` | `52.00` |
| `Live` | `Long` | `3.15` | 2,230,000.00 USD | 0.00 USD | 1,150.00 USD | `-62.15%` | `365.02` |
| `Live` | `Long` | `3.19` | 2,230,000.00 USD | 0.00 USD | 107.06 USD | `-61.55%` | `33.51` |
| `Live` | `Long` | `3.33` | 2,230,000.00 USD | 0.00 USD | 23,310.00 USD | `-59.86%` | `6,990.57` |
| `Live` | `Long` | `3.37` | 2,200,000.00 USD | 0.00 USD | 389.53 USD | `-59.50%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,200,000.00 USD | 0.00 USD | 151.88 USD | `-59.38%` | `45.00` |
| `Live` | `Long` | `3.42` | 2,200,000.00 USD | 0.00 USD | 25,570.00 USD | `-58.78%` | `7,465.11` |
| `Live` | `Long` | `3.46` | 2,180,000.00 USD | 0.00 USD | 582.41 USD | `-58.42%` | `168.57` |
| `Live` | `Long` | `3.54` | 2,180,000.00 USD | 0.00 USD | 392.22 USD | `-57.34%` | `110.64` |
| `Live` | `Long` | `3.67` | 2,180,000.00 USD | 0.00 USD | 1,490.00 USD | `-55.89%` | `407.71` |
| `Live` | `Long` | `3.75` | 2,170,000.00 USD | 0.00 USD | 1,500.00 USD | `-54.81%` | `400.00` |
| `Live` | `Long` | `3.81` | 2,170,000.00 USD | 0.00 USD | 133.53 USD | `-54.09%` | `35.00` |
| `Live` | `Long` | `3.87` | 2,170,000.00 USD | 0.00 USD | 15,390.00 USD | `-53.49%` | `3,981.48` |
| `Live` | `Long` | `3.90` | 2,160,000.00 USD | 0.00 USD | 131.73 USD | `-53.12%` | `33.82` |
| `Live` | `Long` | `4.03` | 2,160,000.00 USD | 0.00 USD | 402.70 USD | `-51.56%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,160,000.00 USD | 0.00 USD | 152.29 USD | `-51.32%` | `37.65` |
| `Live` | `Long` | `4.14` | 2,160,000.00 USD | 0.00 USD | 159.29 USD | `-50.12%` | `38.43` |
| `Live` | `Long` | `4.21` | 2,160,000.00 USD | 0.00 USD | 686.37 USD | `-49.27%` | `162.84` |
| `Live` | `Long` | `4.24` | 2,160,000.00 USD | 0.00 USD | 169.40 USD | `-49.03%` | `40.00` |
| `Live` | `Long` | `4.29` | 2,160,000.00 USD | 0.00 USD | 198.27 USD | `-48.43%` | `46.27` |
| `Live` | `Long` | `4.42` | 2,160,000.00 USD | 0.00 USD | 2,940.00 USD | `-46.87%` | `666.20` |
| `Live` | `Long` | `4.45` | 2,150,000.00 USD | 0.00 USD | 110.77 USD | `-46.51%` | `24.92` |
| `Live` | `Long` | `4.58` | 2,150,000.00 USD | 0.00 USD | 426.94 USD | `-44.94%` | `93.32` |
| `Live` | `Long` | `4.59` | 2,150,000.00 USD | 0.00 USD | 30,970.00 USD | `-44.70%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,120,000.00 USD | 0.00 USD | 486.93 USD | `-44.46%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,120,000.00 USD | 0.00 USD | 2,930.00 USD | `-44.34%` | `634.06` |
| `Live` | `Long` | `4.66` | 2,120,000.00 USD | 0.00 USD | 105.11 USD | `-43.98%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,120,000.00 USD | 0.00 USD | 3,280.00 USD | `-43.86%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,110,000.00 USD | 0.00 USD | 2,000.00 USD | `-43.74%` | `427.75` |
| `Live` | `Long` | `4.68` | 2,110,000.00 USD | 0.00 USD | 8,380.00 USD | `-43.62%` | `1,787.97` |
| `Live` | `Long` | `4.70` | 2,100,000.00 USD | 0.00 USD | 7,040.00 USD | `-43.50%` | `1,500.00` |
| `Live` | `Long` | `4.76` | 2,100,000.00 USD | 0.00 USD | 105.64 USD | `-42.65%` | `22.17` |
| `Live` | `Long` | `4.79` | 2,100,000.00 USD | 0.00 USD | 2,390.00 USD | `-42.41%` | `500.00` |
| `Live` | `Long` | `4.83` | 2,090,000.00 USD | 0.00 USD | 467.01 USD | `-41.81%` | `96.59` |
| `Live` | `Long` | `4.91` | 2,090,000.00 USD | 0.00 USD | 3,880.00 USD | `-40.97%` | `790.61` |
| `Live` | `Long` | `4.92` | 2,090,000.00 USD | 0.00 USD | 17,380.00 USD | `-40.85%` | `3,537.00` |
| `Live` | `Long` | `4.95` | 2,070,000.00 USD | 0.00 USD | 352.68 USD | `-40.49%` | `71.32` |
| `Live` | `Long` | `4.96` | 2,070,000.00 USD | 0.00 USD | 945.36 USD | `-40.37%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,070,000.00 USD | 0.00 USD | 4,090.00 USD | `-40.25%` | `824.62` |
| `Live` | `Long` | `4.97` | 2,070,000.00 USD | 0.00 USD | 282.23 USD | `-40.13%` | `56.73` |
| `Live` | `Long` | `5.00` | 2,070,000.00 USD | 0.00 USD | 269.53 USD | `-39.89%` | `53.96` |
| `Live` | `Long` | `5.01` | 2,070,000.00 USD | 0.00 USD | 56,390.00 USD | `-39.65%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,010,000.00 USD | 0.00 USD | 167.78 USD | `-39.53%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,010,000.00 USD | 0.00 USD | 10,380.00 USD | `-39.41%` | `2,062.48` |
| `Live` | `Long` | `5.05` | 2,000,000.00 USD | 0.00 USD | 2,530.00 USD | `-39.16%` | `499.85` |
| `Live` | `Long` | `5.07` | 2,000,000.00 USD | 0.00 USD | 506.50 USD | `-39.04%` | `100.00` |
| `Live` | `Long` | `5.08` | 2,000,000.00 USD | 0.00 USD | 318.46 USD | `-38.92%` | `62.75` |
| `Live` | `Long` | `5.09` | 2,000,000.00 USD | 0.00 USD | 651.75 USD | `-38.68%` | `127.92` |
| `Live` | `Long` | `5.12` | 2,000,000.00 USD | 0.00 USD | 915.43 USD | `-38.44%` | `178.97` |
| `Live` | `Long` | `5.12` | 1,990,000.00 USD | 0.00 USD | 1,220.00 USD | `-38.32%` | `237.87` |
| `Live` | `Long` | `5.13` | 1,990,000.00 USD | 0.00 USD | 396.06 USD | `-38.20%` | `77.13` |
| `Live` | `Long` | `5.17` | 1,990,000.00 USD | 0.00 USD | 1,620.00 USD | `-37.72%` | `312.94` |
| `Live` | `Long` | `5.18` | 1,990,000.00 USD | 0.00 USD | 150.57 USD | `-37.60%` | `29.04` |
| `Live` | `Long` | `5.20` | 1,990,000.00 USD | 0.00 USD | 480.07 USD | `-37.48%` | `92.41` |
| `Live` | `Long` | `5.21` | 1,990,000.00 USD | 0.00 USD | 300.91 USD | `-37.24%` | `57.70` |
| `Live` | `Long` | `5.25` | 1,990,000.00 USD | 0.00 USD | 121.68 USD | `-36.88%` | `23.20` |
| `Live` | `Long` | `5.25` | 1,990,000.00 USD | 0.00 USD | 1,050.00 USD | `-36.76%` | `200.00` |
| `Live` | `Long` | `5.26` | 1,990,000.00 USD | 0.00 USD | 2,230.00 USD | `-36.64%` | `423.54` |
| `Live` | `Long` | `5.29` | 1,990,000.00 USD | 0.00 USD | 6,210.00 USD | `-36.40%` | `1,174.23` |
| `Live` | `Long` | `5.32` | 1,980,000.00 USD | 0.00 USD | 232.85 USD | `-36.04%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,980,000.00 USD | 0.00 USD | 162,780.00 USD | `-35.92%` | `30,569.68` |
| `Live` | `Long` | `5.33` | 1,820,000.00 USD | 0.00 USD | 512.43 USD | `-35.79%` | `96.05` |
| `Live` | `Long` | `5.39` | 1,820,000.00 USD | 0.00 USD | 660.46 USD | `-35.07%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,820,000.00 USD | 0.00 USD | 20,160.00 USD | `-34.83%` | `3,723.69` |
| `Live` | `Long` | `5.42` | 1,800,000.00 USD | 0.00 USD | 160,400.00 USD | `-34.71%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,640,000.00 USD | 0.00 USD | 1,360.00 USD | `-34.59%` | `250.00` |
| `Live` | `Long` | `5.46` | 1,640,000.00 USD | 0.00 USD | 264.72 USD | `-34.23%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,630,000.00 USD | 0.00 USD | 1,320.00 USD | `-34.11%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,630,000.00 USD | 0.00 USD | 354.06 USD | `-33.99%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,630,000.00 USD | 0.00 USD | 19,290.00 USD | `-33.87%` | `3,510.41` |
| `Live` | `Long` | `5.51` | 1,610,000.00 USD | 0.00 USD | 367.41 USD | `-33.63%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,610,000.00 USD | 0.00 USD | 121.38 USD | `-33.39%` | `21.93` |
| `Live` | `Long` | `5.54` | 1,610,000.00 USD | 0.00 USD | 2,760.00 USD | `-33.27%` | `497.70` |
| `Live` | `Long` | `5.58` | 1,610,000.00 USD | 0.00 USD | 63,260.00 USD | `-32.91%` | `11,347.58` |
| `Live` | `Long` | `5.59` | 1,550,000.00 USD | 0.00 USD | 34,430.00 USD | `-32.67%` | `6,153.60` |
| `Live` | `Long` | `5.62` | 1,510,000.00 USD | 0.00 USD | 2,810.00 USD | `-32.43%` | `500.00` |
| `Live` | `Long` | `5.63` | 1,510,000.00 USD | 0.00 USD | 468.55 USD | `-32.18%` | `83.15` |
| `Live` | `Long` | `5.66` | 1,510,000.00 USD | 0.00 USD | 132.67 USD | `-31.94%` | `23.46` |
| `Live` | `Long` | `5.71` | 1,510,000.00 USD | 0.00 USD | 231.68 USD | `-31.34%` | `40.61` |
| `Live` | `Long` | `5.71` | 1,510,000.00 USD | 0.00 USD | 147.33 USD | `-31.22%` | `25.78` |
| `Live` | `Long` | `5.72` | 1,510,000.00 USD | 0.00 USD | 2,970.00 USD | `-31.10%` | `517.94` |
| `Live` | `Long` | `5.74` | 1,510,000.00 USD | 0.00 USD | 661.65 USD | `-30.98%` | `115.37` |
| `Live` | `Long` | `5.75` | 1,510,000.00 USD | 0.00 USD | 125.70 USD | `-30.86%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,510,000.00 USD | 0.00 USD | 3,190.00 USD | `-30.74%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,500,000.00 USD | 0.00 USD | 10,850.00 USD | `-30.62%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,490,000.00 USD | 0.00 USD | 902.40 USD | `-30.50%` | `156.26` |
| `Live` | `Long` | `5.79` | 1,490,000.00 USD | 0.00 USD | 635.31 USD | `-30.26%` | `109.63` |
| `Live` | `Long` | `5.80` | 1,490,000.00 USD | 0.00 USD | 2,150.00 USD | `-30.14%` | `370.00` |
| `Live` | `Long` | `5.82` | 1,490,000.00 USD | 0.00 USD | 106.65 USD | `-30.02%` | `18.34` |
| `Live` | `Long` | `5.83` | 1,490,000.00 USD | 0.00 USD | 145.88 USD | `-29.78%` | `25.00` |
| `Live` | `Long` | `5.86` | 1,490,000.00 USD | 0.00 USD | 2,110.00 USD | `-29.54%` | `360.33` |
| `Live` | `Long` | `5.88` | 1,490,000.00 USD | 0.00 USD | 375.17 USD | `-29.18%` | `63.75` |
| `Live` | `Long` | `5.89` | 1,480,000.00 USD | 0.00 USD | 984.70 USD | `-29.06%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,480,000.00 USD | 0.00 USD | 399.18 USD | `-28.94%` | `67.60` |
| `Live` | `Long` | `5.92` | 1,480,000.00 USD | 0.00 USD | 277.35 USD | `-28.81%` | `46.89` |
| `Live` | `Long` | `5.96` | 1,480,000.00 USD | 0.00 USD | 11,720.00 USD | `-28.33%` | `1,968.19` |
| `Live` | `Long` | `5.97` | 1,470,000.00 USD | 0.00 USD | 585.97 USD | `-28.09%` | `98.07` |
| `Live` | `Long` | `6.00` | 1,470,000.00 USD | 0.00 USD | 341.56 USD | `-27.73%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,470,000.00 USD | 0.00 USD | 446.85 USD | `-27.61%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,470,000.00 USD | 0.00 USD | 957.69 USD | `-27.37%` | `158.69` |
| `Live` | `Long` | `6.04` | 1,470,000.00 USD | 0.00 USD | 105.61 USD | `-27.25%` | `17.47` |
| `Live` | `Long` | `6.05` | 1,470,000.00 USD | 0.00 USD | 1,310.00 USD | `-27.13%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,470,000.00 USD | 0.00 USD | 265.10 USD | `-27.01%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,470,000.00 USD | 0.00 USD | 1,690.00 USD | `-26.89%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,470,000.00 USD | 0.00 USD | 405.14 USD | `-26.77%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,470,000.00 USD | 0.00 USD | 3,130.00 USD | `-26.65%` | `512.81` |
| `Live` | `Long` | `6.12` | 1,460,000.00 USD | 0.00 USD | 1,140.00 USD | `-26.41%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,460,000.00 USD | 0.00 USD | 137.02 USD | `-26.29%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,460,000.00 USD | 0.00 USD | 2,030.00 USD | `-26.17%` | `330.65` |
| `Live` | `Long` | `6.14` | 1,460,000.00 USD | 0.00 USD | 238.61 USD | `-26.05%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,460,000.00 USD | 0.00 USD | 7,810.00 USD | `-25.93%` | `1,268.30` |
| `Live` | `Long` | `6.17` | 1,450,000.00 USD | 0.00 USD | 104.36 USD | `-25.69%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,450,000.00 USD | 0.00 USD | 310.25 USD | `-25.32%` | `50.00` |
| `Live` | `Long` | `6.25` | 1,450,000.00 USD | 0.00 USD | 2,420.00 USD | `-24.72%` | `387.67` |
| `Live` | `Long` | `6.28` | 1,450,000.00 USD | 0.00 USD | 2,510.00 USD | `-24.48%` | `400.00` |
| `Live` | `Long` | `6.33` | 1,450,000.00 USD | 0.00 USD | 277.48 USD | `-23.88%` | `43.87` |
| `Live` | `Long` | `6.33` | 1,450,000.00 USD | 0.00 USD | 2,450.00 USD | `-23.76%` | `386.46` |
| `Live` | `Long` | `6.36` | 1,440,000.00 USD | 0.00 USD | 4,470.00 USD | `-23.52%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,440,000.00 USD | 0.00 USD | 284,770.00 USD | `-23.40%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 1,150,000.00 USD | 0.00 USD | 6,410.00 USD | `-23.28%` | `1,006.23` |
| `Live` | `Long` | `6.42` | 1,150,000.00 USD | 0.00 USD | 306.32 USD | `-22.80%` | `47.75` |
| `Live` | `Long` | `6.42` | 1,150,000.00 USD | 0.00 USD | 484.64 USD | `-22.68%` | `75.43` |
| `Live` | `Long` | `6.43` | 1,150,000.00 USD | 0.00 USD | 7,090.00 USD | `-22.56%` | `1,101.11` |
| `Live` | `Long` | `6.46` | 1,140,000.00 USD | 0.00 USD | 1,050.00 USD | `-22.20%` | `162.75` |
| `Live` | `Long` | `6.50` | 1,140,000.00 USD | 0.00 USD | 1,460.00 USD | `-21.83%` | `225.14` |
| `Live` | `Long` | `6.50` | 1,140,000.00 USD | 0.00 USD | 257.99 USD | `-21.71%` | `39.66` |
| `Live` | `Long` | `6.51` | 1,140,000.00 USD | 0.00 USD | 651.50 USD | `-21.59%` | `100.00` |
| `Live` | `Long` | `6.54` | 1,140,000.00 USD | 0.00 USD | 852.03 USD | `-21.35%` | `130.38` |
| `Live` | `Long` | `6.54` | 1,140,000.00 USD | 0.00 USD | 8,970.00 USD | `-21.23%` | `1,370.89` |
| `Live` | `Long` | `6.58` | 1,130,000.00 USD | 0.00 USD | 1,770.00 USD | `-20.75%` | `269.14` |
| `Live` | `Long` | `6.59` | 1,120,000.00 USD | 0.00 USD | 1,100.00 USD | `-20.63%` | `166.55` |
| `Live` | `Long` | `6.62` | 1,120,000.00 USD | 0.00 USD | 2,110.00 USD | `-20.39%` | `318.57` |
| `Live` | `Long` | `6.62` | 1,120,000.00 USD | 0.00 USD | 364.90 USD | `-20.27%` | `55.08` |
| `Live` | `Long` | `6.63` | 1,120,000.00 USD | 0.00 USD | 245.89 USD | `-20.15%` | `37.06` |
| `Live` | `Long` | `6.66` | 1,120,000.00 USD | 0.00 USD | 373,080.00 USD | `-19.91%` | `56,059.40` |
| `Live` | `Long` | `6.67` | 747,370.00 USD | 0.00 USD | 1,320.00 USD | `-19.67%` | `198.12` |
| `Live` | `Long` | `6.71` | 746,050.00 USD | 0.00 USD | 16,570.00 USD | `-19.31%` | `2,471.72` |
| `Live` | `Long` | `6.71` | 729,480.00 USD | 0.00 USD | 6,180.00 USD | `-19.19%` | `920.74` |
| `Live` | `Long` | `6.75` | 723,300.00 USD | 0.00 USD | 2,900.00 USD | `-18.83%` | `430.55` |
| `Live` | `Long` | `6.78` | 720,390.00 USD | 0.00 USD | 6,780.00 USD | `-18.46%` | `1,000.00` |
| `Live` | `Long` | `6.79` | 713,620.00 USD | 0.00 USD | 21,580.00 USD | `-18.34%` | `3,180.66` |
| `Live` | `Long` | `6.79` | 692,040.00 USD | 0.00 USD | 6,270.00 USD | `-18.22%` | `923.14` |
| `Live` | `Long` | `6.80` | 685,760.00 USD | 0.00 USD | 1,500.00 USD | `-18.10%` | `220.95` |
| `Live` | `Long` | `6.82` | 684,260.00 USD | 0.00 USD | 7,230.00 USD | `-17.98%` | `1,061.04` |
| `Live` | `Long` | `6.83` | 677,030.00 USD | 0.00 USD | 410.80 USD | `-17.86%` | `60.19` |
| `Live` | `Long` | `6.87` | 676,620.00 USD | 0.00 USD | 3,710.00 USD | `-17.38%` | `540.58` |
| `Live` | `Long` | `6.88` | 672,910.00 USD | 0.00 USD | 1,580.00 USD | `-17.14%` | `229.18` |
| `Live` | `Long` | `6.92` | 671,330.00 USD | 0.00 USD | 579.62 USD | `-16.66%` | `83.70` |
| `Live` | `Long` | `6.93` | 670,750.00 USD | 0.00 USD | 3,500.00 USD | `-16.54%` | `504.07` |
| `Live` | `Long` | `6.95` | 667,250.00 USD | 0.00 USD | 3,980.00 USD | `-16.42%` | `572.68` |
| `Live` | `Long` | `6.96` | 663,280.00 USD | 0.00 USD | 3,480.00 USD | `-16.30%` | `500.00` |
| `Live` | `Long` | `6.96` | 659,800.00 USD | 0.00 USD | 636.74 USD | `-16.18%` | `91.42` |
| `Live` | `Long` | `6.97` | 659,160.00 USD | 0.00 USD | 128,810.00 USD | `-16.06%` | `18,466.99` |
| `Live` | `Long` | `6.99` | 530,350.00 USD | 0.00 USD | 297.49 USD | `-15.94%` | `42.59` |
| `Live` | `Long` | `7.00` | 530,060.00 USD | 0.00 USD | 746.58 USD | `-15.82%` | `106.73` |
| `Live` | `Long` | `7.00` | 529,310.00 USD | 0.00 USD | 21,670.00 USD | `-15.70%` | `3,093.44` |
| `Live` | `Long` | `7.03` | 507,640.00 USD | 0.00 USD | 1,370.00 USD | `-15.46%` | `194.51` |
| `Live` | `Long` | `7.05` | 506,270.00 USD | 0.00 USD | 354.23 USD | `-15.10%` | `50.21` |
| `Live` | `Long` | `7.07` | 505,920.00 USD | 0.00 USD | 23,600.00 USD | `-14.97%` | `3,340.54` |
| `Live` | `Long` | `7.08` | 482,320.00 USD | 0.00 USD | 7,420.00 USD | `-14.85%` | `1,048.27` |
| `Live` | `Long` | `7.08` | 474,900.00 USD | 0.00 USD | 644.88 USD | `-14.73%` | `91.02` |
| `Live` | `Long` | `7.09` | 474,260.00 USD | 0.00 USD | 2,130.00 USD | `-14.61%` | `300.00` |
| `Live` | `Long` | `7.11` | 472,130.00 USD | 0.00 USD | 28,530.00 USD | `-14.49%` | `4,015.35` |
| `Live` | `Long` | `7.12` | 443,600.00 USD | 0.00 USD | 379.66 USD | `-14.37%` | `53.36` |
| `Live` | `Long` | `7.13` | 443,220.00 USD | 0.00 USD | 777.50 USD | `-14.13%` | `108.97` |
| `Live` | `Long` | `7.14` | 442,440.00 USD | 0.00 USD | 20,270.00 USD | `-14.01%` | `2,837.00` |
| `Live` | `Long` | `7.17` | 422,170.00 USD | 0.00 USD | 2,380.00 USD | `-13.65%` | `331.12` |
| `Live` | `Long` | `7.18` | 419,800.00 USD | 0.00 USD | 2,890.00 USD | `-13.53%` | `401.89` |
| `Live` | `Long` | `7.21` | 416,910.00 USD | 0.00 USD | 29,180.00 USD | `-13.17%` | `4,044.76` |
| `Live` | `Long` | `7.24` | 387,730.00 USD | 0.00 USD | 1,480.00 USD | `-12.93%` | `205.21` |
| `Live` | `Long` | `7.25` | 386,240.00 USD | 0.00 USD | 185.83 USD | `-12.81%` | `25.65` |
| `Live` | `Long` | `7.25` | 386,060.00 USD | 0.00 USD | 21,280.00 USD | `-12.69%` | `2,933.17` |
| `Live` | `Long` | `7.28` | 364,780.00 USD | 0.00 USD | 1,460.00 USD | `-12.45%` | `200.00` |
| `Live` | `Long` | `7.29` | 363,320.00 USD | 0.00 USD | 36,840.00 USD | `-12.33%` | `5,057.61` |
| `Live` | `Long` | `7.29` | 326,480.00 USD | 0.00 USD | 1,680.00 USD | `-12.21%` | `230.97` |
| `Live` | `Long` | `7.34` | 324,790.00 USD | 0.00 USD | 4,370.00 USD | `-11.61%` | `594.84` |
| `Live` | `Long` | `7.37` | 320,420.00 USD | 0.00 USD | 2,940.00 USD | `-11.36%` | `399.15` |
| `Live` | `Long` | `7.38` | 317,480.00 USD | 0.00 USD | 1,100.00 USD | `-11.24%` | `148.75` |
| `Live` | `Long` | `7.41` | 316,390.00 USD | 0.00 USD | 13,230.00 USD | `-10.88%` | `1,787.05` |
| `Live` | `Long` | `7.42` | 303,150.00 USD | 0.00 USD | 147.61 USD | `-10.64%` | `19.88` |
| `Live` | `Long` | `7.43` | 303,000.00 USD | 0.00 USD | 2,430.00 USD | `-10.52%` | `327.05` |
| `Live` | `Long` | `7.45` | 300,570.00 USD | 0.00 USD | 210.99 USD | `-10.40%` | `28.34` |
| `Live` | `Long` | `7.46` | 300,360.00 USD | 0.00 USD | 10,390.00 USD | `-10.28%` | `1,393.53` |
| `Live` | `Long` | `7.46` | 289,970.00 USD | 0.00 USD | 4,590.00 USD | `-10.16%` | `614.36` |
| `Live` | `Long` | `7.47` | 285,390.00 USD | 0.00 USD | 1,120.00 USD | `-10.04%` | `149.52` |
| `Live` | `Long` | `7.50` | 284,270.00 USD | 0.00 USD | 2,010.00 USD | `-9.80%` | `268.46` |
| `Live` | `Long` | `7.50` | 282,260.00 USD | 0.00 USD | 421.78 USD | `-9.68%` | `56.20` |
| `Live` | `Long` | `7.51` | 281,840.00 USD | 0.00 USD | 1,710.00 USD | `-9.56%` | `228.21` |
| `Live` | `Long` | `7.53` | 280,120.00 USD | 0.00 USD | 1,570.00 USD | `-9.44%` | `208.52` |
| `Live` | `Long` | `7.54` | 278,550.00 USD | 0.00 USD | 4,210.00 USD | `-9.32%` | `559.01` |
| `Live` | `Long` | `7.55` | 274,340.00 USD | 0.00 USD | 415.52 USD | `-9.08%` | `55.00` |
| `Live` | `Long` | `7.57` | 273,920.00 USD | 0.00 USD | 25,060.00 USD | `-8.96%` | `3,312.23` |
| `Live` | `Long` | `7.58` | 248,870.00 USD | 0.00 USD | 118.25 USD | `-8.84%` | `15.61` |
| `Live` | `Long` | `7.59` | 248,750.00 USD | 0.00 USD | 26,280.00 USD | `-8.60%` | `3,460.14` |
| `Live` | `Long` | `7.61` | 222,470.00 USD | 0.00 USD | 1,140.00 USD | `-8.48%` | `149.34` |
| `Live` | `Long` | `7.62` | 221,330.00 USD | 0.00 USD | 754.04 USD | `-8.36%` | `99.02` |
| `Live` | `Long` | `7.62` | 220,580.00 USD | 0.00 USD | 787.51 USD | `-8.24%` | `103.28` |
| `Live` | `Long` | `7.63` | 219,790.00 USD | 0.00 USD | 378.93 USD | `-8.12%` | `49.63` |
| `Live` | `Long` | `7.66` | 219,410.00 USD | 0.00 USD | 135.42 USD | `-7.87%` | `17.69` |
| `Live` | `Long` | `7.67` | 219,280.00 USD | 0.00 USD | 256.09 USD | `-7.75%` | `33.41` |
| `Live` | `Long` | `7.67` | 219,020.00 USD | 0.00 USD | 4,480.00 USD | `-7.63%` | `583.63` |
| `Live` | `Long` | `7.68` | 214,540.00 USD | 0.00 USD | 739.30 USD | `-7.51%` | `96.20` |
| `Live` | `Long` | `7.70` | 213,800.00 USD | 0.00 USD | 3,250.00 USD | `-7.39%` | `422.01` |
| `Live` | `Long` | `7.75` | 210,550.00 USD | 0.00 USD | 500.12 USD | `-6.67%` | `64.49` |
| `Live` | `Long` | `7.76` | 210,050.00 USD | 0.00 USD | 455.73 USD | `-6.55%` | `58.69` |
| `Live` | `Long` | `7.78` | 209,600.00 USD | 0.00 USD | 8,670.00 USD | `-6.43%` | `1,115.74` |
| `Live` | `Long` | `7.79` | 200,920.00 USD | 0.00 USD | 2,470.00 USD | `-6.31%` | `317.11` |
| `Live` | `Long` | `7.79` | 198,460.00 USD | 0.00 USD | 4,480.00 USD | `-6.19%` | `574.50` |
| `Live` | `Long` | `7.80` | 193,980.00 USD | 0.00 USD | 6,380.00 USD | `-6.07%` | `817.06` |
| `Live` | `Long` | `7.82` | 187,600.00 USD | 0.00 USD | 2,070.00 USD | `-5.95%` | `265.35` |
| `Live` | `Long` | `7.83` | 185,530.00 USD | 0.00 USD | 2,270.00 USD | `-5.83%` | `290.31` |
| `Live` | `Long` | `7.84` | 183,250.00 USD | 0.00 USD | 22,560.00 USD | `-5.59%` | `2,875.86` |
| `Live` | `Long` | `7.87` | 160,690.00 USD | 0.00 USD | 233.83 USD | `-5.35%` | `29.73` |
| `Live` | `Long` | `7.88` | 160,460.00 USD | 0.00 USD | 555.19 USD | `-5.23%` | `70.50` |
| `Live` | `Long` | `7.89` | 159,900.00 USD | 0.00 USD | 1,430.00 USD | `-4.99%` | `180.69` |
| `Live` | `Long` | `7.91` | 158,480.00 USD | 0.00 USD | 505.13 USD | `-4.87%` | `63.90` |
| `Live` | `Long` | `7.92` | 157,970.00 USD | 0.00 USD | 4,600.00 USD | `-4.62%` | `580.78` |
| `Live` | `Long` | `7.93` | 153,370.00 USD | 0.00 USD | 16,340.00 USD | `-4.50%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 137,030.00 USD | 0.00 USD | 127,110.00 USD | `-4.38%` | `15,999.24` |
| `Live` | `Long` | `7.96` | 9,910.00 USD | 0.00 USD | 245.57 USD | `-4.26%` | `30.87` |
| `Live` | `Long` | `7.97` | 9,670.00 USD | 0.00 USD | 1,580.00 USD | `-4.02%` | `198.26` |
| `Live` | `Long` | `7.99` | 8,090.00 USD | 0.00 USD | 1,600.00 USD | `-3.90%` | `200.68` |
| `Live` | `Long` | `8.00` | 6,480.00 USD | 0.00 USD | 210.99 USD | `-3.78%` | `26.39` |
| `Live` | `Long` | `8.21` | 6,270.00 USD | 0.00 USD | 6,270.00 USD | `-1.13%` | `763.67` |
| `Live` | `Short` | `8.31` | 3,720.00 USD | 3,720.00 USD | 0.00 USD | `+0.07%` | `447.21` |
| `Live` | `Short` | `8.52` | 5,870.00 USD | 2,150.00 USD | 0.00 USD | `+2.48%` | `252.58` |
| `Live` | `Short` | `8.54` | 6,060.00 USD | 190.93 USD | 0.00 USD | `+2.72%` | `22.37` |
| `Live` | `Short` | `8.55` | 9,280.00 USD | 3,220.00 USD | 0.00 USD | `+2.96%` | `376.02` |
| `Live` | `Short` | `8.69` | 9,490.00 USD | 209.31 USD | 0.00 USD | `+4.52%` | `24.10` |
| `Live` | `Short` | `8.78` | 9,590.00 USD | 105.04 USD | 0.00 USD | `+5.60%` | `11.97` |
| `Live` | `Short` | `8.79` | 10,010.00 USD | 423.22 USD | 0.00 USD | `+5.85%` | `48.12` |
| `Live` | `Short` | `8.82` | 16,020.00 USD | 6,000.00 USD | 0.00 USD | `+6.21%` | `680.16` |
| `Live` | `Short` | `9.19` | 17,610.00 USD | 1,590.00 USD | 0.00 USD | `+10.54%` | `173.30` |
| `Live` | `Short` | `9.21` | 19,480.00 USD | 1,870.00 USD | 0.00 USD | `+10.90%` | `202.76` |
| `Live` | `Short` | `9.38` | 19,610.00 USD | 128.44 USD | 0.00 USD | `+12.83%` | `13.70` |
| `Live` | `Short` | `9.41` | 20,050.00 USD | 440.06 USD | 0.00 USD | `+13.31%` | `46.74` |
| `Live` | `Short` | `9.46` | 20,180.00 USD | 138.85 USD | 0.00 USD | `+13.91%` | `14.67` |
| `Live` | `Short` | `9.62` | 20,320.00 USD | 138.98 USD | 0.00 USD | `+15.83%` | `14.44` |
| `Live` | `Short` | `9.64` | 22,260.00 USD | 1,930.00 USD | 0.00 USD | `+16.07%` | `200.61` |
| `Live` | `Short` | `9.73` | 22,450.00 USD | 192.95 USD | 0.00 USD | `+17.16%` | `19.82` |
| `Live` | `Short` | `9.96` | 321,110.00 USD | 298,660.00 USD | 0.00 USD | `+19.81%` | `30,000.94` |
| `Live` | `Short` | `10.35` | 323,770.00 USD | 2,650.00 USD | 0.00 USD | `+24.50%` | `256.58` |
| `Live` | `Short` | `10.56` | 324,290.00 USD | 523.81 USD | 0.00 USD | `+27.15%` | `49.58` |
| `Live` | `Short` | `10.71` | 431,340.00 USD | 107,050.00 USD | 0.00 USD | `+28.83%` | `10,000.00` |
| `Live` | `Short` | `10.89` | 431,440.00 USD | 100.13 USD | 0.00 USD | `+31.12%` | `9.19` |
| `Live` | `Short` | `10.97` | 486,310.00 USD | 54,880.00 USD | 0.00 USD | `+32.08%` | `5,000.00` |
| `Live` | `Short` | `11.01` | 493,280.00 USD | 6,970.00 USD | 0.00 USD | `+32.44%` | `633.00` |
| `Live` | `Short` | `11.10` | 493,700.00 USD | 415.06 USD | 0.00 USD | `+33.53%` | `37.41` |
| `Live` | `Short` | `11.27` | 505,360.00 USD | 11,670.00 USD | 0.00 USD | `+35.57%` | `1,035.87` |
| `Live` | `Short` | `11.29` | 505,630.00 USD | 270.63 USD | 0.00 USD | `+35.93%` | `23.96` |
| `Live` | `Short` | `11.34` | 505,950.00 USD | 319.08 USD | 0.00 USD | `+36.41%` | `28.15` |
| `Live` | `Short` | `11.62` | 518,090.00 USD | 12,140.00 USD | 0.00 USD | `+39.90%` | `1,043.90` |
| `Live` | `Short` | `11.69` | 814,850.00 USD | 296,760.00 USD | 0.00 USD | `+40.63%` | `25,397.02` |
| `Live` | `Short` | `11.80` | 814,970.00 USD | 114.27 USD | 0.00 USD | `+42.07%` | `9.68` |
| `Live` | `Short` | `11.93` | 815,470.00 USD | 505.74 USD | 0.00 USD | `+43.51%` | `42.41` |
| `Live` | `Short` | `11.95` | 816,520.00 USD | 1,050.00 USD | 0.00 USD | `+43.75%` | `87.54` |
| `Live` | `Short` | `12.30` | 818,250.00 USD | 1,730.00 USD | 0.00 USD | `+48.09%` | `140.71` |
| `Live` | `Short` | `12.40` | 818,590.00 USD | 343.62 USD | 0.00 USD | `+49.29%` | `27.70` |
| `Live` | `Short` | `13.20` | 906,540.00 USD | 87,940.00 USD | 0.00 USD | `+58.80%` | `6,665.00` |
| `Live` | `Short` | `13.28` | 967,010.00 USD | 60,470.00 USD | 0.00 USD | `+59.76%` | `4,555.14` |
| `Live` | `Short` | `13.29` | 970,820.00 USD | 3,810.00 USD | 0.00 USD | `+60.00%` | `286.56` |
| `Live` | `Short` | `13.46` | 971,250.00 USD | 430.34 USD | 0.00 USD | `+62.05%` | `31.96` |
| `Live` | `Short` | `13.69` | 971,420.00 USD | 172.29 USD | 0.00 USD | `+64.69%` | `12.59` |
| `Live` | `Short` | `14.34` | 971,700.00 USD | 282.83 USD | 0.00 USD | `+72.52%` | `19.73` |
| `Live` | `Short` | `14.66` | 972,530.00 USD | 823.29 USD | 0.00 USD | `+76.49%` | `56.14` |
| `Live` | `Short` | `15.04` | 972,770.00 USD | 246.72 USD | 0.00 USD | `+80.94%` | `16.41` |
| `Live` | `Short` | `15.18` | 973,320.00 USD | 544.63 USD | 0.00 USD | `+82.63%` | `35.89` |
| `Live` | `Short` | `15.22` | 977,540.00 USD | 4,230.00 USD | 0.00 USD | `+83.23%` | `277.54` |
| `Live` | `Short` | `15.29` | 977,770.00 USD | 229.43 USD | 0.00 USD | `+84.07%` | `15.00` |
| `Live` | `Short` | `15.35` | 978,000.00 USD | 230.17 USD | 0.00 USD | `+84.67%` | `15.00` |
| `Live` | `Short` | `15.38` | 998,000.00 USD | 20,000.00 USD | 0.00 USD | `+85.15%` | `1,300.00` |
| `Live` | `Short` | `15.39` | 1,000,000.00 USD | 6,130.00 USD | 0.00 USD | `+85.27%` | `398.03` |
| `Live` | `Short` | `15.72` | 1,000,000.00 USD | 167.79 USD | 0.00 USD | `+89.25%` | `10.67` |
| `Live` | `Short` | `15.77` | 1,000,000.00 USD | 185.55 USD | 0.00 USD | `+89.73%` | `11.77` |
| `Live` | `Short` | `16.39` | 1,030,000.00 USD | 23,920.00 USD | 0.00 USD | `+97.31%` | `1,459.25` |
| `Live` | `Short` | `16.41` | 1,290,000.00 USD | 266,050.00 USD | 0.00 USD | `+97.55%` | `16,208.00` |
| `Live` | `Short` | `16.46` | 1,320,000.00 USD | 23,290.00 USD | 0.00 USD | `+98.15%` | `1,414.55` |
| `Live` | `Short` | `16.52` | 1,320,000.00 USD | 190.91 USD | 0.00 USD | `+98.75%` | `11.56` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 345,840.00 USD | 0.00 USD | 611.73 USD | `-72.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 345,220.00 USD | 0.00 USD | 793.75 USD | `-51.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 344,430.00 USD | 0.00 USD | 105.04 USD | `-46.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 344,320.00 USD | 0.00 USD | 67,970.00 USD | `-39.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 276,360.00 USD | 0.00 USD | 205.30 USD | `-36.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 276,150.00 USD | 0.00 USD | 465.42 USD | `-34.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 275,690.00 USD | 0.00 USD | 349.35 USD | `-33.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 275,340.00 USD | 0.00 USD | 1,020.00 USD | `-33.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 274,320.00 USD | 0.00 USD | 1,330.00 USD | `-30.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 272,990.00 USD | 0.00 USD | 493.50 USD | `-28.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 272,500.00 USD | 0.00 USD | 100.98 USD | `-28.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 272,400.00 USD | 0.00 USD | 500.70 USD | `-27.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 271,900.00 USD | 0.00 USD | 4,160.00 USD | `-26.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 267,740.00 USD | 0.00 USD | 6,500.00 USD | `-25.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.21` | 261,240.00 USD | 0.00 USD | 906.18 USD | `-25.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.25` | 260,330.00 USD | 0.00 USD | 127.35 USD | `-24.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 260,210.00 USD | 0.00 USD | 864.38 USD | `-24.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 259,340.00 USD | 0.00 USD | 130.10 USD | `-21.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 259,210.00 USD | 0.00 USD | 4,340.00 USD | `-21.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 254,870.00 USD | 0.00 USD | 5,520.00 USD | `-19.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 249,350.00 USD | 0.00 USD | 100.72 USD | `-19.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 249,250.00 USD | 0.00 USD | 296.34 USD | `-18.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 248,950.00 USD | 0.00 USD | 921.19 USD | `-18.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 248,030.00 USD | 0.00 USD | 709.98 USD | `-17.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 247,320.00 USD | 0.00 USD | 1,380.00 USD | `-16.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 245,940.00 USD | 0.00 USD | 262.44 USD | `-16.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 245,680.00 USD | 0.00 USD | 24,350.00 USD | `-15.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.11` | 221,320.00 USD | 0.00 USD | 187.79 USD | `-14.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 221,140.00 USD | 0.00 USD | 6,790.00 USD | `-13.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 214,350.00 USD | 0.00 USD | 9,770.00 USD | `-13.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.21` | 204,580.00 USD | 0.00 USD | 7,210.00 USD | `-13.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 197,370.00 USD | 0.00 USD | 282.74 USD | `-12.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 197,090.00 USD | 0.00 USD | 603.44 USD | `-12.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 196,490.00 USD | 0.00 USD | 464.61 USD | `-12.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 196,020.00 USD | 0.00 USD | 2,090.00 USD | `-12.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 193,930.00 USD | 0.00 USD | 129.58 USD | `-11.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 193,800.00 USD | 0.00 USD | 114.65 USD | `-11.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.39` | 193,690.00 USD | 0.00 USD | 702.75 USD | `-11.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.41` | 192,980.00 USD | 0.00 USD | 4,630.00 USD | `-10.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 188,350.00 USD | 0.00 USD | 199.39 USD | `-10.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 188,150.00 USD | 0.00 USD | 6,270.00 USD | `-10.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 181,880.00 USD | 0.00 USD | 37,420.00 USD | `-9.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 144,460.00 USD | 0.00 USD | 2,120.00 USD | `-9.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 142,340.00 USD | 0.00 USD | 799.83 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 141,540.00 USD | 0.00 USD | 820.44 USD | `-9.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 140,720.00 USD | 0.00 USD | 103.41 USD | `-8.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 140,610.00 USD | 0.00 USD | 218.24 USD | `-8.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 140,400.00 USD | 0.00 USD | 113.78 USD | `-8.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.61` | 140,280.00 USD | 0.00 USD | 152.10 USD | `-8.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 140,130.00 USD | 0.00 USD | 297.59 USD | `-8.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.68` | 139,830.00 USD | 0.00 USD | 528.88 USD | `-7.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 139,300.00 USD | 0.00 USD | 360.13 USD | `-7.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 138,940.00 USD | 0.00 USD | 578.04 USD | `-6.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.79` | 138,370.00 USD | 0.00 USD | 424.05 USD | `-6.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 137,940.00 USD | 0.00 USD | 23,790.00 USD | `-6.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.82` | 114,160.00 USD | 0.00 USD | 3,940.00 USD | `-5.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 110,220.00 USD | 0.00 USD | 115.23 USD | `-5.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 110,100.00 USD | 0.00 USD | 183.33 USD | `-5.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.88` | 109,920.00 USD | 0.00 USD | 194.52 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 109,720.00 USD | 0.00 USD | 1,890.00 USD | `-4.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 107,830.00 USD | 0.00 USD | 6,520.00 USD | `-4.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 101,310.00 USD | 0.00 USD | 5,710.00 USD | `-4.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 95,610.00 USD | 0.00 USD | 1,590.00 USD | `-4.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 94,020.00 USD | 0.00 USD | 898.42 USD | `-4.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 93,120.00 USD | 0.00 USD | 7,960.00 USD | `-4.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 85,170.00 USD | 0.00 USD | 9,160.00 USD | `-3.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 76,010.00 USD | 0.00 USD | 3,430.00 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 72,570.00 USD | 0.00 USD | 123.58 USD | `-3.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 72,450.00 USD | 0.00 USD | 2,110.00 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 70,340.00 USD | 0.00 USD | 152.56 USD | `-3.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.06` | 70,190.00 USD | 0.00 USD | 2,730.00 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 67,460.00 USD | 0.00 USD | 121.69 USD | `-2.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.09` | 67,340.00 USD | 0.00 USD | 5,230.00 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 62,100.00 USD | 0.00 USD | 477.36 USD | `-2.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 61,630.00 USD | 0.00 USD | 924.78 USD | `-2.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 60,700.00 USD | 0.00 USD | 744.88 USD | `-2.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 59,960.00 USD | 0.00 USD | 6,500.00 USD | `-2.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 53,460.00 USD | 0.00 USD | 884.60 USD | `-2.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 52,570.00 USD | 0.00 USD | 5,550.00 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 47,020.00 USD | 0.00 USD | 1,430.00 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 45,580.00 USD | 0.00 USD | 3,080.00 USD | `-1.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 42,500.00 USD | 0.00 USD | 520.75 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 41,980.00 USD | 0.00 USD | 3,020.00 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 38,960.00 USD | 0.00 USD | 141.04 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 38,820.00 USD | 0.00 USD | 22,560.00 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 16,250.00 USD | 0.00 USD | 515.66 USD | `-1.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 15,740.00 USD | 0.00 USD | 1,030.00 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.24` | 14,710.00 USD | 0.00 USD | 197.96 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.26` | 14,510.00 USD | 0.00 USD | 9,110.00 USD | `-0.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.27` | 5,400.00 USD | 0.00 USD | 397.71 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 5,000.00 USD | 0.00 USD | 408.78 USD | `-0.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 4,590.00 USD | 0.00 USD | 201.49 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 4,390.00 USD | 0.00 USD | 4,150.00 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 242.42 USD | 0.00 USD | 242.42 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.31` | 2,920.00 USD | 2,920.00 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.32` | 4,610.00 USD | 1,690.00 USD | 0.00 USD | `+0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.34` | 5,020.00 USD | 408.58 USD | 0.00 USD | `+0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.35` | 5,770.00 USD | 756.06 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.36` | 6,740.00 USD | 970.35 USD | 0.00 USD | `+0.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 7,250.00 USD | 503.59 USD | 0.00 USD | `+0.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 7,670.00 USD | 419.25 USD | 0.00 USD | `+0.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 9,630.00 USD | 1,970.00 USD | 0.00 USD | `+1.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 9,960.00 USD | 328.55 USD | 0.00 USD | `+1.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.41` | 10,280.00 USD | 314.81 USD | 0.00 USD | `+1.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.43` | 12,160.00 USD | 1,880.00 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.44` | 12,470.00 USD | 307.54 USD | 0.00 USD | `+1.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.45` | 12,610.00 USD | 138.24 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 13,320.00 USD | 710.81 USD | 0.00 USD | `+1.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.47` | 14,090.00 USD | 769.61 USD | 0.00 USD | `+1.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.48` | 14,230.00 USD | 146.79 USD | 0.00 USD | `+2.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.49` | 14,640.00 USD | 408.78 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 31,650.00 USD | 17,010.00 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.52` | 32,060.00 USD | 408.55 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.53` | 33,190.00 USD | 1,130.00 USD | 0.00 USD | `+2.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 33,480.00 USD | 290.10 USD | 0.00 USD | `+2.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 37,880.00 USD | 4,400.00 USD | 0.00 USD | `+2.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.55` | 38,130.00 USD | 243.82 USD | 0.00 USD | `+2.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.56` | 39,720.00 USD | 1,600.00 USD | 0.00 USD | `+3.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.57` | 41,150.00 USD | 1,420.00 USD | 0.00 USD | `+3.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.60` | 42,280.00 USD | 1,130.00 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 43,030.00 USD | 751.56 USD | 0.00 USD | `+3.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 44,520.00 USD | 1,490.00 USD | 0.00 USD | `+3.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 48,810.00 USD | 4,290.00 USD | 0.00 USD | `+3.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 49,010.00 USD | 201.97 USD | 0.00 USD | `+3.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 49,120.00 USD | 103.31 USD | 0.00 USD | `+4.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 49,220.00 USD | 107.84 USD | 0.00 USD | `+4.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 49,330.00 USD | 107.97 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 49,510.00 USD | 176.62 USD | 0.00 USD | `+4.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 50,500.00 USD | 990.09 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 55,510.00 USD | 5,010.00 USD | 0.00 USD | `+4.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 56,080.00 USD | 575.14 USD | 0.00 USD | `+4.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 56,480.00 USD | 399.67 USD | 0.00 USD | `+4.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 57,300.00 USD | 819.28 USD | 0.00 USD | `+5.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 57,640.00 USD | 333.07 USD | 0.00 USD | `+5.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 62,010.00 USD | 4,370.00 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 63,780.00 USD | 1,780.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 103,590.00 USD | 39,810.00 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 103,810.00 USD | 215.16 USD | 0.00 USD | `+5.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 104,200.00 USD | 388.12 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 104,910.00 USD | 711.78 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 105,470.00 USD | 563.87 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.82` | 107,510.00 USD | 2,030.00 USD | 0.00 USD | `+6.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 107,750.00 USD | 243.40 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 113,510.00 USD | 5,760.00 USD | 0.00 USD | `+6.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 113,750.00 USD | 234.04 USD | 0.00 USD | `+6.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 113,910.00 USD | 163.91 USD | 0.00 USD | `+6.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 114,020.00 USD | 110.58 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 115,130.00 USD | 1,100.00 USD | 0.00 USD | `+6.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 117,060.00 USD | 1,930.00 USD | 0.00 USD | `+7.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 117,850.00 USD | 788.72 USD | 0.00 USD | `+7.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 119,650.00 USD | 1,800.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 119,820.00 USD | 163.33 USD | 0.00 USD | `+7.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 149,340.00 USD | 29,520.00 USD | 0.00 USD | `+7.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 149,560.00 USD | 223.62 USD | 0.00 USD | `+7.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 149,740.00 USD | 180.53 USD | 0.00 USD | `+7.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 150,140.00 USD | 401.63 USD | 0.00 USD | `+7.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 465,300.00 USD | 315,150.00 USD | 0.00 USD | `+8.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 465,400.00 USD | 104.59 USD | 0.00 USD | `+8.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 465,660.00 USD | 262.56 USD | 0.00 USD | `+8.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 465,790.00 USD | 130.03 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 467,170.00 USD | 1,380.00 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 468,260.00 USD | 1,090.00 USD | 0.00 USD | `+8.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 468,870.00 USD | 616.37 USD | 0.00 USD | `+8.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 468,980.00 USD | 102.03 USD | 0.00 USD | `+8.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 469,430.00 USD | 453.84 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 469,590.00 USD | 160.99 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 470,010.00 USD | 415.00 USD | 0.00 USD | `+9.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 471,520.00 USD | 1,510.00 USD | 0.00 USD | `+9.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 472,120.00 USD | 606.18 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 745,280.00 USD | 273,160.00 USD | 0.00 USD | `+9.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 749,840.00 USD | 4,560.00 USD | 0.00 USD | `+9.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 750,010.00 USD | 166.53 USD | 0.00 USD | `+9.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 752,000.00 USD | 2,000.00 USD | 0.00 USD | `+10.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 1,150,000.00 USD | 394,210.00 USD | 0.00 USD | `+10.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,150,000.00 USD | 119.24 USD | 0.00 USD | `+10.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,150,000.00 USD | 2,660.00 USD | 0.00 USD | `+10.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,150,000.00 USD | 131.87 USD | 0.00 USD | `+10.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,150,000.00 USD | 149.17 USD | 0.00 USD | `+11.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,150,000.00 USD | 2,220.00 USD | 0.00 USD | `+11.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,380,000.00 USD | 231,380.00 USD | 0.00 USD | `+11.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,380,000.00 USD | 1,960.00 USD | 0.00 USD | `+11.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,390,000.00 USD | 434.45 USD | 0.00 USD | `+11.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,400,000.00 USD | 18,610.00 USD | 0.00 USD | `+11.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,400,000.00 USD | 166.83 USD | 0.00 USD | `+12.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,400,000.00 USD | 150.79 USD | 0.00 USD | `+12.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,400,000.00 USD | 101.58 USD | 0.00 USD | `+12.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,400,000.00 USD | 109.36 USD | 0.00 USD | `+12.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,400,000.00 USD | 116.69 USD | 0.00 USD | `+12.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,400,000.00 USD | 163.41 USD | 0.00 USD | `+12.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,410,000.00 USD | 1,150.00 USD | 0.00 USD | `+12.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,410,000.00 USD | 660.84 USD | 0.00 USD | `+13.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,410,000.00 USD | 714.59 USD | 0.00 USD | `+13.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,410,000.00 USD | 928.13 USD | 0.00 USD | `+13.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,410,000.00 USD | 102.45 USD | 0.00 USD | `+13.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,410,000.00 USD | 219.84 USD | 0.00 USD | `+13.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,410,000.00 USD | 1,890.00 USD | 0.00 USD | `+13.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,410,000.00 USD | 1,130.00 USD | 0.00 USD | `+14.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,410,000.00 USD | 288.46 USD | 0.00 USD | `+14.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,410,000.00 USD | 119.92 USD | 0.00 USD | `+14.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,410,000.00 USD | 231.00 USD | 0.00 USD | `+15.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,410,000.00 USD | 221.07 USD | 0.00 USD | `+15.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,410,000.00 USD | 992.00 USD | 0.00 USD | `+15.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,410,000.00 USD | 148.48 USD | 0.00 USD | `+15.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,410,000.00 USD | 191.36 USD | 0.00 USD | `+16.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,420,000.00 USD | 4,440.00 USD | 0.00 USD | `+16.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,420,000.00 USD | 108.21 USD | 0.00 USD | `+16.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,420,000.00 USD | 169.68 USD | 0.00 USD | `+17.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,420,000.00 USD | 574.66 USD | 0.00 USD | `+17.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,420,000.00 USD | 121.87 USD | 0.00 USD | `+17.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,420,000.00 USD | 115.88 USD | 0.00 USD | `+18.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,420,000.00 USD | 340.05 USD | 0.00 USD | `+18.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,420,000.00 USD | 742.12 USD | 0.00 USD | `+19.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,420,000.00 USD | 899.47 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,490,000.00 USD | 70,020.00 USD | 0.00 USD | `+19.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,490,000.00 USD | 373.97 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,500,000.00 USD | 5,050.00 USD | 0.00 USD | `+20.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,500,000.00 USD | 6,370.00 USD | 0.00 USD | `+21.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,500,000.00 USD | 404.20 USD | 0.00 USD | `+21.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,710,000.00 USD | 210,980.00 USD | 0.00 USD | `+21.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,720,000.00 USD | 1,150.00 USD | 0.00 USD | `+21.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,720,000.00 USD | 172.16 USD | 0.00 USD | `+22.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,720,000.00 USD | 922.87 USD | 0.00 USD | `+23.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,720,000.00 USD | 489.40 USD | 0.00 USD | `+24.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,720,000.00 USD | 1,200.00 USD | 0.00 USD | `+24.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,720,000.00 USD | 118.01 USD | 0.00 USD | `+25.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.47` | 1,720,000.00 USD | 818.31 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,720,000.00 USD | 312.31 USD | 0.00 USD | `+26.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,720,000.00 USD | 2,290.00 USD | 0.00 USD | `+26.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,720,000.00 USD | 178.46 USD | 0.00 USD | `+27.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,720,000.00 USD | 173.42 USD | 0.00 USD | `+29.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,720,000.00 USD | 184.75 USD | 0.00 USD | `+29.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,720,000.00 USD | 135.78 USD | 0.00 USD | `+29.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,720,000.00 USD | 127.96 USD | 0.00 USD | `+30.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,720,000.00 USD | 476.43 USD | 0.00 USD | `+30.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,720,000.00 USD | 869.35 USD | 0.00 USD | `+31.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,720,000.00 USD | 118.97 USD | 0.00 USD | `+31.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,720,000.00 USD | 251.06 USD | 0.00 USD | `+31.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,720,000.00 USD | 552.44 USD | 0.00 USD | `+31.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,730,000.00 USD | 537.26 USD | 0.00 USD | `+32.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,730,000.00 USD | 320.29 USD | 0.00 USD | `+33.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,730,000.00 USD | 1,100.00 USD | 0.00 USD | `+34.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,730,000.00 USD | 2,270.00 USD | 0.00 USD | `+34.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,730,000.00 USD | 1,270.00 USD | 0.00 USD | `+35.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,730,000.00 USD | 1,380.00 USD | 0.00 USD | `+36.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,730,000.00 USD | 2,410.00 USD | 0.00 USD | `+37.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,740,000.00 USD | 9,520.00 USD | 0.00 USD | `+37.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 1,750,000.00 USD | 2,050.00 USD | 0.00 USD | `+38.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,750,000.00 USD | 529.11 USD | 0.00 USD | `+38.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,750,000.00 USD | 7,700.00 USD | 0.00 USD | `+39.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,750,000.00 USD | 906.03 USD | 0.00 USD | `+42.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,760,000.00 USD | 434.61 USD | 0.00 USD | `+42.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,760,000.00 USD | 163.52 USD | 0.00 USD | `+42.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 1,770,000.00 USD | 10,370.00 USD | 0.00 USD | `+44.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.19` | 1,770,000.00 USD | 5,270.00 USD | 0.00 USD | `+46.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.28` | 1,770,000.00 USD | 115.02 USD | 0.00 USD | `+47.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 1,770,000.00 USD | 3,350.00 USD | 0.00 USD | `+52.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 1,770,000.00 USD | 197.97 USD | 0.00 USD | `+54.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 1,780,000.00 USD | 3,200.00 USD | 0.00 USD | `+55.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 1,780,000.00 USD | 179.58 USD | 0.00 USD | `+56.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 1,780,000.00 USD | 568.45 USD | 0.00 USD | `+56.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 1,780,000.00 USD | 169.57 USD | 0.00 USD | `+58.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 1,780,000.00 USD | 446.52 USD | 0.00 USD | `+60.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 1,780,000.00 USD | 5,320.00 USD | 0.00 USD | `+62.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,000,000.00 USD | 210,750.00 USD | 0.00 USD | `+62.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,000,000.00 USD | 407.95 USD | 0.00 USD | `+64.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,000,000.00 USD | 174.91 USD | 0.00 USD | `+66.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,000,000.00 USD | 4,650.00 USD | 0.00 USD | `+68.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,000,000.00 USD | 960.26 USD | 0.00 USD | `+70.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,000,000.00 USD | 2,710.00 USD | 0.00 USD | `+72.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,010,000.00 USD | 805.90 USD | 0.00 USD | `+74.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,010,000.00 USD | 655.55 USD | 0.00 USD | `+76.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,010,000.00 USD | 4,890.00 USD | 0.00 USD | `+77.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,010,000.00 USD | 471.09 USD | 0.00 USD | `+79.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,010,000.00 USD | 383.85 USD | 0.00 USD | `+80.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,660,000.00 USD | 653,420.00 USD | 0.00 USD | `+80.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 2,670,000.00 USD | 3,010.00 USD | 0.00 USD | `+81.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,670,000.00 USD | 111.87 USD | 0.00 USD | `+90.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,670,000.00 USD | 219.91 USD | 0.00 USD | `+92.62%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `347.87M` | Total OI Tokens: `41,676,517.4 AVAX`
  * 1h OI Change: `+1.69%` | 4h OI Change: `-1.15%` | 24h OI Change: `-8.62%`
  * Exchange Breakdown: Binance=`80.25M` | Bybit=`57.05M` | OKX=`11.56M` | Hyperliquid=`16.21M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-7.05K` | Last 24h: `18.18K` | Last 3d: `59.53K` | Last 7d: `106.20K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0053%` | **USDT OKX** | `0.0080%` |
| **USDT Bybit** | `-0.0215%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0051%` | **USDT BingX** | `0.0073%` |
| **USDT Gate** | `-0.0008%` | **USDT Bitget** | `-0.0012%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `50.63%` | `49.37%` | `1.03` | 2,990,000.00 USD |
| `15M` | `Binance` | `54.18%` | `45.82%` | `1.18` | 967,690.00 USD |
| `15M` | `OKX` | `44.06%` | `55.94%` | `0.79` | 221,610.00 USD |
| `15M` | `Bybit` | `44.71%` | `55.29%` | `0.81` | 321,210.00 USD |
| `15M` | `KuCoin` | `48.81%` | `51.19%` | `0.95` | 23,520.00 USD |
| `15M` | `Gate` | `40.75%` | `59.25%` | `0.69` | 44,690.00 USD |
| `15M` | `Bitget` | `70.8%` | `29.2%` | `2.42` | 62,230.00 USD |
| `15M` | `BingX` | `50.13%` | `49.87%` | `1.01` | 726,710.00 USD |
| `15M` | `MEXC` | `49.04%` | `50.96%` | `0.96` | 77,490.00 USD |
| `15M` | `Bitunix` | `64.14%` | `35.86%` | `1.79` | 58,120.00 USD |
| `15M` | `Hyperliquid` | `19.17%` | `80.83%` | `0.24` | 27,090.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.72%` | `49.28%` | `1.03` | 410,520.00 USD |
| `15M` | `Crypto.com` | `46.42%` | `53.58%` | `0.87` | 23.33 USD |
| `15M` | `WhiteBIT` | `32.34%` | `67.66%` | `0.48` | 27,990.00 USD |
| `15M` | `HTX` | `91.61%` | `8.39%` | `10.92` | 6,860.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `25.92%` | `74.08%` | `0.35` | 225.19 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `43.13%` | `56.87%` | `0.76` | 14,370.00 USD |
| `15M` | `Whale Positions` | `54.18%` | `45.82%` | `1.18` | 967,690.00 USD |
| `15M` | `Global Accounts` | `50.63%` | `49.37%` | `1.03` | 2,990,000.00 USD |
| `1H` | `AVAX` | `46.90%` | `53.10%` | `0.88` | 34,710,000.00 USD |
| `1H` | `Binance` | `58.37%` | `41.63%` | `1.40` | 14,800,000.00 USD |
| `1H` | `OKX` | `60.08%` | `39.92%` | `1.51` | 4,850,000.00 USD |
| `1H` | `Bybit` | `59.41%` | `40.59%` | `1.46` | 6,420,000.00 USD |
| `1H` | `KuCoin` | `46.22%` | `53.78%` | `0.86` | 771,530.00 USD |
| `1H` | `Gate` | `48.37%` | `51.63%` | `0.94` | 1,360,000.00 USD |
| `1H` | `Bitget` | `53.43%` | `46.57%` | `1.15` | 986,490.00 USD |
| `1H` | `BingX` | `28.57%` | `71.43%` | `0.40` | 374,350.00 USD |
| `1H` | `MEXC` | `54.78%` | `45.22%` | `1.21` | 751,170.00 USD |
| `1H` | `Bitunix` | `68.76%` | `31.24%` | `2.20` | 539,800.00 USD |
| `1H` | `Hyperliquid` | `31.67%` | `68.33%` | `0.46` | 1,810,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.89%` | `48.11%` | `1.08` | 423,200.00 USD |
| `1H` | `Crypto.com` | `53.05%` | `46.95%` | `1.13` | 0.00 USD |
| `1H` | `WhiteBIT` | `10.96%` | `89.04%` | `0.12` | 1,120,000.00 USD |
| `1H` | `HTX` | `79.71%` | `20.29%` | `3.93` | 191,500.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `65.3%` | `34.7%` | `1.88` | 40,690.00 USD |
| `1H` | `Aster` | `75.6%` | `24.4%` | `3.10` | 67,290.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54.15%` | `45.85%` | `1.18` | 192,300.00 USD |
| `1H` | `Whale Positions` | `58.37%` | `41.63%` | `1.40` | 14,800,000.00 USD |
| `1H` | `Global Accounts` | `46.90%` | `53.10%` | `0.88` | 34,710,000.00 USD |
| `4H` | `AVAX` | `47.20%` | `52.80%` | `0.89` | 126,190,000.00 USD |
| `4H` | `Binance` | `48.74%` | `51.26%` | `0.95` | 47,870,000.00 USD |
| `4H` | `OKX` | `48.61%` | `51.39%` | `0.95` | 7,980,000.00 USD |
| `4H` | `Bybit` | `47.37%` | `52.63%` | `0.90` | 10,750,000.00 USD |
| `4H` | `KuCoin` | `44.56%` | `55.44%` | `0.80` | 2,170,000.00 USD |
| `4H` | `Gate` | `43.95%` | `56.05%` | `0.78` | 3,250,000.00 USD |
| `4H` | `Bitget` | `44.06%` | `55.94%` | `0.79` | 4,450,000.00 USD |
| `4H` | `BingX` | `40.22%` | `59.78%` | `0.67` | 15,990,000.00 USD |
| `4H` | `MEXC` | `43.4%` | `56.6%` | `0.77` | 4,630,000.00 USD |
| `4H` | `Bitunix` | `48.01%` | `51.99%` | `0.92` | 3,520,000.00 USD |
| `4H` | `Hyperliquid` | `45.52%` | `54.48%` | `0.84` | 3,930,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.76%` | `49.24%` | `1.03` | 19,030,000.00 USD |
| `4H` | `Crypto.com` | `28.87%` | `71.13%` | `0.41` | 24,090.00 USD |
| `4H` | `WhiteBIT` | `52.11%` | `47.89%` | `1.09` | 1,250,000.00 USD |
| `4H` | `HTX` | `55.94%` | `44.06%` | `1.27` | 61,050.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `53.92%` | `46.08%` | `1.17` | 625,750.00 USD |
| `4H` | `Aster` | `50.21%` | `49.79%` | `1.01` | 243,690.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.35%` | `58.65%` | `0.71` | 428,830.00 USD |
| `4H` | `Whale Positions` | `48.74%` | `51.26%` | `0.95` | 47,870,000.00 USD |
| `4H` | `Global Accounts` | `47.20%` | `52.80%` | `0.89` | 126,190,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `8.24` | `8.20` | `8.24` | `8.24` | `8.11` | 3,101,647.59 USD | 2,221,188.12 USD | 880,459.47 USD | 1,340,728.65 USD | `+43.23%` | `44B / 11S` |
| `0:00 UTC` | `8.21` | `8.23` | `8.21` | `8.28` | `8.19` | 3,097,134.32 USD | 1,901,895.55 USD | 1,195,238.77 USD | 706,656.79 USD | `+22.82%` | `14B / 3S` |
| `5:00 UTC` | `8.25` | `8.23` | `8.25` | `8.27` | `8.20` | 1,839,796.84 USD | 879,856.22 USD | 959,940.62 USD | -80,084.40 USD | `-4.35%` | `8B / 14S` |
| `0:00 UTC` | `8.21` | `8.19` | `8.21` | `8.26` | `8.11` | 2,539,835.55 USD | 1,124,809.52 USD | 1,415,026.03 USD | -290,216.50 USD | `-11.43%` | `12B / 26S` |
| `5:00 UTC` | `8.21` | `8.19` | `8.21` | `8.22` | `8.16` | 1,163,864.40 USD | 663,189.73 USD | 500,674.67 USD | 162,515.06 USD | `+13.96%` | `9B / 6S` |
| `0:00 UTC` | `8.17` | `8.20` | `8.17` | `8.25` | `8.15` | 1,223,062.19 USD | 718,965.78 USD | 504,096.41 USD | 214,869.37 USD | `+17.57%` | `26B / 17S` |
| `5:00 UTC` | `8.30` | `8.29` | `8.30` | `8.33` | `8.24` | 1,042,239.86 USD | 674,984.50 USD | 367,255.36 USD | 307,729.14 USD | `+29.53%` | `28B / 5S` |
| `0:00 UTC` | `8.34` | `8.33` | `8.34` | `8.35` | `8.30` | 876,108.07 USD | 469,253.46 USD | 406,854.61 USD | 62,398.85 USD | `+7.12%` | `5B / 6S` |
| `5:00 UTC` | `8.33` | `8.32` | `8.33` | `8.35` | `8.30` | 843,379.31 USD | 374,655.63 USD | 468,723.68 USD | -94,068.04 USD | `-11.15%` | `5B / 8S` |
| `0:00 UTC` | `8.34` | `8.34` | `8.34` | `8.35` | `8.31` | 387,574.94 USD | 237,117.71 USD | 150,457.23 USD | 86,660.47 USD | `+22.36%` | `17B / 6S` |

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
| `5m` | -7,390.00 USD | 15,550.00 USD | **`ACCUMULATION`** |
| `15m` | 15,530.00 USD | -43,160.00 USD | **`DISTRIBUTION`** |
| `30m` | 44,200.00 USD | 74,080.00 USD | **`ACCUMULATION`** |
| `1h` | 156,100.00 USD | 1,220,000.00 USD | **`ACCUMULATION`** |
| `2h` | -78,260.00 USD | 836,470.00 USD | **`ACCUMULATION`** |
| `4h` | -1,190,000.00 USD | -2,260,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -687,350.00 USD | -1,150,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,700,000.00 USD | -8,170,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,640,000.00 USD | -11,760,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,420,000.00 USD | -11,680,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,600,000.00 USD | -55,690,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -57,930,000.00 USD | -270,220,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-7.39K` | 15m=`+15.53K` | 1h=`+156.10K` | 24h=`-2.42M`
* Futures Capital Netflows: 5m=`+15.55K` | 15m=`-43.16K` | 1h=`+1.22M` | 24h=`-11.68M`
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
  * `2026-10-30 08:34:38 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:38 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:00:38 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:35:38 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:36:38 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:36:38 IST`: [investinglive.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `7.96` (Risk Distance: `0.1732` pts)
  * +2.5R Take Profit: `8.56`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.40` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.57` (Risk Distance: `0.1732` pts)
  * +2.5R Take Profit: `7.97`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.41`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
