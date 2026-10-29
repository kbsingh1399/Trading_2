# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 00:47:28 IST` (`2026-10-29 19:17:28 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `8.81` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `8.87` | Lower -3.00σ Band: `8.75`
  * Upper +2.51σ Band: `8.86` | Lower -2.51σ Band: `8.76`
  * Upper +2.01σ Band: `8.85` | Lower -2.01σ Band: `8.77`
  * Upper +2.00σ Band: `8.85` | Lower -2.00σ Band: `8.77`
  * Upper +1.28σ Band: `8.83` | Lower -1.28σ Band: `8.79`
  * Upper +1.00σ Band: `8.83` | Lower -1.00σ Band: `8.79`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.81` | EMA-20=`8.81` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.81` (Slope: `+0.0000`) | EMA-100=`8.81`
  * Institutional Anchors: EMA-144=`8.81` | EMA-200=`8.81` (Slope: `+0.0000`) | EMA-233=`8.81`
- **Range Boundaries**: 24H High=`8.90` | 24H Low=`8.72` | Weekly High=`8.99` | Weekly Low=`8.63`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.91` (Distance: `-1.12%`)
  * Point of Control (POC) = `8.74` (Distance: `+0.80%`)
  * Value Area Low (VAL) = `8.58` (Distance: `+2.67%`)
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
| `5m` | `8.81` | `8.85` | `8.81` | `8.84` | `32,356` | 285,894.34 USD | 88,056.98 USD | `+30.80%` | -2,442,861.42 USD | `+1.09` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `8.84` | `8.86` | `8.84` | `8.84` | `18,867` | 166,884.56 USD | 32,695.81 USD | `+19.59%` | -2,410,165.61 USD | `+0.54` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `8.84` | `8.84` | `8.81` | `8.82` | `38,644` | 340,917.26 USD | -18,417.41 USD | `-5.40%` | -2,428,583.03 USD | `+0.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `8.84` | `8.84` | `8.79` | `8.81` | `199,951` | 1,762,248.06 USD | -214,982.91 USD | `-12.20%` | -2,649,812.84 USD | `-0.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `8.81` | `8.86` | `8.79` | `8.84` | `85,070` | 750,878.19 USD | 165,572.87 USD | `+22.05%` | -2,484,239.97 USD | `+0.83` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.84` | `8.84` | `8.80` | `8.81` | `69,145` | 609,745.76 USD | 29,551.70 USD | `+4.85%` | -2,454,688.27 USD | `+0.45` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `8.96` | `8.96` | `8.82` | `8.87` | `732,279` | 6,517,786.37 USD | -1,600,470.16 USD | `-24.56%` | -3,146,829.78 USD | `-2.72` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `8.87` | `8.89` | `8.79` | `8.84` | `435,467` | 3,847,058.68 USD | -67,411.45 USD | `-1.75%` | -3,214,241.23 USD | `+0.32` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `8.84` | `8.84` | `8.80` | `8.81` | `69,145` | 609,745.76 USD | 29,551.70 USD | `+4.85%` | -3,184,689.52 USD | `+0.55` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -426,486.82 USD | `+0.25` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -480,308.79 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.81` | `2,077,327` | 18,532,872.59 USD | -2,704,380.73 USD | `-14.59%` | -3,184,689.52 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `9.00` | `9.02` | `8.55` | `8.59` | `3,515,330` | 30,612,875.98 USD | -2,423,031.38 USD | `-7.92%` | -749,324.84 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.59` | `8.80` | `8.57` | `8.62` | `1,816,830` | 15,790,058.74 USD | 58,580.54 USD | `+0.37%` | -690,744.30 USD | `+0.17` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -426,486.82 USD | `+0.25` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -480,308.79 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.81` | `2,077,327` | 18,532,872.59 USD | -2,704,380.73 USD | `-14.59%` | -3,184,689.52 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `BUY` | `8.64` | `2546.0600` | 22,000.00 USD | 4,900,854.62 USD | `STANDARD` | `-1.95%` | `0x0efb38a5fa` |
| `BUY` | `8.66` | `383.1600` | 3,319.58 USD | 6,214,833.06 USD | `STANDARD` | `-1.69%` | `0x14f8e04290` |
| `BUY` | `8.67` | `13275.9100` | 115,164.54 USD | 3,900,817.44 USD | `LARGE (>= USD 100K)` | `-1.57%` | `0xecb63caa47` |
| `BUY` | `8.67` | `186.1300` | 1,613.93 USD | 6,359,997.78 USD | `STANDARD` | `-1.61%` | `0x0ad81cbc47` |
| `BUY` | `8.67` | `76.4300` | 662.72 USD | 6,415,896.16 USD | `STANDARD` | `-1.61%` | `0xdadbb4b2a0` |
| `BUY` | `8.68` | `12900.0700` | 111,953.26 USD | 4,012,770.70 USD | `LARGE (>= USD 100K)` | `-1.52%` | `0x71d0e11ebb` |
| `BUY` | `8.68` | `2119.6200` | 18,405.30 USD | 5,015,091.37 USD | `STANDARD` | `-1.47%` | `0xd3943e4008` |
| `BUY` | `8.68` | `315.7300` | 2,740.85 USD | 6,266,243.55 USD | `STANDARD` | `-1.50%` | `0x07fd993f0f` |
| `BUY` | `8.68` | `178.3300` | 1,548.55 USD | 6,364,703.15 USD | `STANDARD` | `-1.47%` | `0x010461c14e` |
| `BUY` | `8.68` | `177.9600` | 1,544.96 USD | 6,366,248.11 USD | `STANDARD` | `-1.49%` | `0x31ca8395cf` |
| `BUY` | `8.69` | `10268.7300` | 89,255.80 USD | 4,508,152.26 USD | `MEDIUM (>= USD 25K)` | `-1.37%` | `0xecb63caa47` |
| `BUY` | `8.69` | `2187.4200` | 18,999.93 USD | 4,940,101.85 USD | `STANDARD` | `-1.44%` | `0x0efb38a5fa` |
| `BUY` | `8.70` | `383.1600` | 3,332.88 USD | 6,211,513.47 USD | `STANDARD` | `-1.30%` | `0x14f8e04290` |
| `BUY` | `8.70` | `176.6200` | 1,536.36 USD | 6,367,784.47 USD | `STANDARD` | `-1.29%` | `0xdadbb4b2a0` |
| `BUY` | `8.71` | `46845.7800` | 408,143.86 USD | 1,640,033.08 USD | `LARGE (>= USD 100K)` | `-1.14%` | `0x71cfa5e263` |
| `BUY` | `8.71` | `17540.9800` | 152,776.67 USD | 2,875,202.07 USD | `LARGE (>= USD 100K)` | `-1.17%` | `0x71d0e11ebb` |
| `BUY` | `8.71` | `10225.9400` | 89,059.76 USD | 4,597,212.02 USD | `MEDIUM (>= USD 25K)` | `-1.18%` | `0xecb63caa47` |
| `BUY` | `8.71` | `1837.1500` | 15,999.92 USD | 5,031,091.30 USD | `STANDARD` | `-1.18%` | `0x0efb38a5fa` |
| `BUY` | `8.71` | `186.1300` | 1,621.19 USD | 6,358,383.84 USD | `STANDARD` | `-1.17%` | `0x0ad81cbc47` |
| `BUY` | `8.72` | `4082.5500` | 35,617.39 USD | 4,814,961.11 USD | `MEDIUM (>= USD 25K)` | `-1.00%` | `0xa24c5ca26c` |
| `BUY` | `8.72` | `1650.1800` | 14,387.26 USD | 5,532,109.29 USD | `STANDARD` | `-1.07%` | `0xd3943e4008` |
| `BUY` | `8.73` | `13440.3700` | 117,290.08 USD | 3,670,213.17 USD | `LARGE (>= USD 100K)` | `-0.98%` | `0xecb63caa47` |
| `BUY` | `8.73` | `1405.8300` | 12,277.39 USD | 5,583,997.39 USD | `STANDARD` | `-0.90%` | `0xd3943e4008` |
| `BUY` | `8.73` | `1343.8600` | 11,726.39 USD | 5,655,633.01 USD | `STANDARD` | `-0.99%` | `0x33ad48ed92` |
| `BUY` | `8.73` | `366.8200` | 3,204.10 USD | 6,240,622.06 USD | `STANDARD` | `-0.89%` | `0xdd4f66125d` |
| `BUY` | `8.73` | `131.2700` | 1,146.01 USD | 6,384,579.99 USD | `STANDARD` | `-0.94%` | `0xe34d21d198` |
| `BUY` | `8.73` | `79.6000` | 694.53 USD | 6,411,131.71 USD | `STANDARD` | `-0.99%` | `0x010461c14e` |
| `BUY` | `8.73` | `78.5000` | 685.34 USD | 6,413,194.94 USD | `STANDARD` | `-0.94%` | `0x31ca8395cf` |
| `BUY` | `8.74` | `22398.7000` | 195,753.44 USD | 2,256,608.94 USD | `LARGE (>= USD 100K)` | `-0.83%` | `0xa20fb0c9e0` |
| `BUY` | `8.74` | `11449.4900` | 100,117.78 USD | 4,220,713.86 USD | `LARGE (>= USD 100K)` | `-0.78%` | `0x881cd92459` |
| `BUY` | `8.74` | `383.1600` | 3,349.39 USD | 6,204,833.54 USD | `STANDARD` | `-0.81%` | `0x14f8e04290` |
| `BUY` | `8.74` | `383.1600` | 3,347.06 USD | 6,208,180.59 USD | `STANDARD` | `-0.88%` | `0x14f8e04290` |
| `BUY` | `8.74` | `366.8200` | 3,206.52 USD | 6,237,417.97 USD | `STANDARD` | `-0.81%` | `0xdd4f66125d` |
| `BUY` | `8.74` | `315.7300` | 2,758.85 USD | 6,258,002.07 USD | `STANDARD` | `-0.85%` | `0x07fd993f0f` |
| `BUY` | `8.75` | `17547.7700` | 153,521.93 USD | 2,722,425.40 USD | `LARGE (>= USD 100K)` | `-0.73%` | `0x71d0e11ebb` |
| `BUY` | `8.75` | `3649.3500` | 31,946.77 USD | 4,846,907.89 USD | `MEDIUM (>= USD 25K)` | `-0.67%` | `0xa38f19c4cc` |
| `BUY` | `8.75` | `1370.9400` | 11,999.97 USD | 5,607,999.71 USD | `STANDARD` | `-0.68%` | `0x0efb38a5fa` |
| `BUY` | `8.75` | `1305.8200` | 11,431.93 USD | 5,667,064.94 USD | `STANDARD` | `-0.66%` | `0xd3943e4008` |
| `BUY` | `8.75` | `1250.0000` | 10,933.00 USD | 5,722,614.26 USD | `STANDARD` | `-0.75%` | `0xb7bd9cef0e` |
| `BUY` | `8.75` | `366.8200` | 3,209.86 USD | 6,231,002.65 USD | `STANDARD` | `-0.71%` | `0xdd4f66125d` |
| `BUY` | `8.75` | `142.8700` | 1,249.97 USD | 6,371,566.34 USD | `STANDARD` | `-0.72%` | `0x0ad81cbc47` |
| `BUY` | `8.75` | `131.2700` | 1,148.95 USD | 6,383,433.98 USD | `STANDARD` | `-0.68%` | `0xe34d21d198` |
| `BUY` | `8.76` | `1666.8600` | 14,607.36 USD | 5,503,123.00 USD | `STANDARD` | `-0.56%` | `0x57d8e75f47` |
| `BUY` | `8.76` | `1666.8600` | 14,599.03 USD | 5,517,722.03 USD | `STANDARD` | `-0.62%` | `0x57d8e75f47` |
| `BUY` | `8.76` | `1009.2100` | 8,836.34 USD | 5,879,528.55 USD | `STANDARD` | `-0.65%` | `0x33ad48ed92` |
| `BUY` | `8.76` | `485.1200` | 4,251.06 USD | 6,080,811.29 USD | `STANDARD` | `-0.57%` | `0xcd7f60e943` |
| `BUY` | `8.76` | `231.2300` | 2,026.41 USD | 6,330,515.38 USD | `STANDARD` | `-0.56%` | `0x9d732bed51` |
| `BUY` | `8.76` | `231.2300` | 2,025.23 USD | 6,332,540.61 USD | `STANDARD` | `-0.62%` | `0x9d732bed51` |
| `BUY` | `8.77` | `23858.4800` | 209,129.12 USD | 2,060,855.50 USD | `LARGE (>= USD 100K)` | `-0.54%` | `0x71cfa5e263` |
| `BUY` | `8.77` | `14831.6800` | 130,102.01 USD | 3,432,182.26 USD | `LARGE (>= USD 100K)` | `-0.46%` | `0x71d0e11ebb` |
| `BUY` | `8.77` | `1666.8600` | 14,624.03 USD | 5,473,899.95 USD | `STANDARD` | `-0.45%` | `0x57d8e75f47` |
| `BUY` | `8.77` | `1666.8600` | 14,615.70 USD | 5,488,515.64 USD | `STANDARD` | `-0.50%` | `0x57d8e75f47` |
| `BUY` | `8.77` | `1260.6400` | 11,054.17 USD | 5,700,627.09 USD | `STANDARD` | `-0.50%` | `0xa38f19c4cc` |
| `BUY` | `8.77` | `1047.4700` | 9,186.73 USD | 5,861,735.59 USD | `STANDARD` | `-0.48%` | `0xd3943e4008` |
| `BUY` | `8.77` | `911.9300` | 8,000.00 USD | 5,912,889.56 USD | `STANDARD` | `-0.46%` | `0x0efb38a5fa` |
| `BUY` | `8.77` | `830.0000` | 7,278.35 USD | 5,966,103.32 USD | `STANDARD` | `-0.50%` | `0xb7bd9cef0e` |
| `BUY` | `8.77` | `741.0400` | 6,502.48 USD | 5,993,738.75 USD | `STANDARD` | `-0.43%` | `0xa38f19c4cc` |
| `BUY` | `8.77` | `403.9300` | 3,541.58 USD | 6,187,817.75 USD | `STANDARD` | `-0.51%` | `0x2a72b57dea` |
| `BUY` | `8.77` | `231.2300` | 2,028.33 USD | 6,326,461.67 USD | `STANDARD` | `-0.46%` | `0x9d732bed51` |
| `BUY` | `8.77` | `231.2300` | 2,027.31 USD | 6,328,488.97 USD | `STANDARD` | `-0.51%` | `0x9d732bed51` |
| `BUY` | `8.77` | `131.2700` | 1,151.87 USD | 6,382,285.03 USD | `STANDARD` | `-0.43%` | `0xe34d21d198` |
| `BUY` | `8.77` | `81.6400` | 716.02 USD | 6,408,326.36 USD | `STANDARD` | `-0.48%` | `0x31ca8395cf` |
| `BUY` | `8.77` | `76.4200` | 670.24 USD | 6,415,233.44 USD | `STANDARD` | `-0.48%` | `0x010461c14e` |
| `BUY` | `8.78` | `2139.3600` | 18,792.14 USD | 4,996,686.08 USD | `STANDARD` | `-0.33%` | `0xa38f19c4cc` |
| `BUY` | `8.78` | `1666.8600` | 14,640.70 USD | 5,444,643.55 USD | `STANDARD` | `-0.33%` | `0x57d8e75f47` |
| `BUY` | `8.78` | `1666.8600` | 14,632.36 USD | 5,459,275.92 USD | `STANDARD` | `-0.39%` | `0x57d8e75f47` |
| `BUY` | `8.78` | `1106.8100` | 9,716.46 USD | 5,843,099.42 USD | `STANDARD` | `-0.39%` | `0xd3342d3b1e` |
| `BUY` | `8.78` | `980.7400` | 8,611.68 USD | 5,896,889.32 USD | `STANDARD` | `-0.36%` | `0xd3943e4008` |
| `BUY` | `8.78` | `862.5900` | 7,572.59 USD | 5,936,461.48 USD | `STANDARD` | `-0.38%` | `0xecb63caa47` |
| `BUY` | `8.78` | `823.0800` | 7,226.81 USD | 5,973,330.13 USD | `STANDARD` | `-0.37%` | `0xecb63caa47` |
| `BUY` | `8.78` | `792.3000` | 6,953.07 USD | 5,987,236.28 USD | `STANDARD` | `-0.42%` | `0x47a4471457` |
| `BUY` | `8.78` | `679.9200` | 5,971.06 USD | 6,024,454.26 USD | `STANDARD` | `-0.35%` | `0x33ad48ed92` |
| `BUY` | `8.78` | `568.9000` | 4,995.80 USD | 6,050,433.11 USD | `STANDARD` | `-0.36%` | `0x3ca146d269` |
| `BUY` | `8.78` | `403.9300` | 3,545.86 USD | 6,184,276.17 USD | `STANDARD` | `-0.39%` | `0x2a72b57dea` |
| `BUY` | `8.78` | `231.2300` | 2,030.45 USD | 6,322,403.97 USD | `STANDARD` | `-0.36%` | `0x9d732bed51` |
| `BUY` | `8.78` | `231.2300` | 2,029.37 USD | 6,324,433.34 USD | `STANDARD` | `-0.41%` | `0x9d732bed51` |
| `BUY` | `8.78` | `227.5000` | 1,997.40 USD | 6,338,540.16 USD | `STANDARD` | `-0.37%` | `0x39bac00809` |
| `BUY` | `8.78` | `62.6400` | 550.03 USD | 6,421,930.77 USD | `STANDARD` | `-0.36%` | `0x5cc518f6e6` |
| `BUY` | `8.78` | `57.0000` | 500.41 USD | 6,428,482.93 USD | `STANDARD` | `-0.38%` | `0x667b8184fc` |
| `BUY` | `8.79` | `16765.5800` | 147,408.01 USD | 3,170,690.18 USD | `LARGE (>= USD 100K)` | `-0.23%` | `0x71d0e11ebb` |
| `BUY` | `8.79` | `4173.1400` | 36,693.59 USD | 4,779,343.72 USD | `MEDIUM (>= USD 25K)` | `-0.23%` | `0x08a49e7f71` |
| `BUY` | `8.79` | `1666.8600` | 14,653.53 USD | 5,415,353.82 USD | `STANDARD` | `-0.25%` | `0x57d8e75f47` |
| `BUY` | `8.79` | `1666.8600` | 14,649.03 USD | 5,430,002.85 USD | `STANDARD` | `-0.28%` | `0x57d8e75f47` |
| `BUY` | `8.79` | `1137.9700` | 10,008.45 USD | 5,793,622.20 USD | `STANDARD` | `-0.20%` | `0xaf9f722a67` |
| `BUY` | `8.79` | `846.4400` | 7,441.65 USD | 5,951,469.92 USD | `STANDARD` | `-0.24%` | `0xecb63caa47` |
| `BUY` | `8.79` | `568.6200` | 4,999.99 USD | 6,045,437.32 USD | `STANDARD` | `-0.22%` | `0x0efb38a5fa` |
| `BUY` | `8.79` | `420.0000` | 3,692.18 USD | 6,152,241.69 USD | `STANDARD` | `-0.25%` | `0xb7bd9cef0e` |
| `BUY` | `8.79` | `403.9300` | 3,549.90 USD | 6,180,730.31 USD | `STANDARD` | `-0.28%` | `0x2a72b57dea` |
| `BUY` | `8.79` | `329.6400` | 2,896.35 USD | 6,249,599.23 USD | `STANDARD` | `-0.30%` | `0xecb63caa47` |
| `BUY` | `8.79` | `231.2300` | 2,033.62 USD | 6,316,309.42 USD | `STANDARD` | `-0.20%` | `0x9d732bed51` |
| `BUY` | `8.79` | `231.2300` | 2,032.60 USD | 6,318,342.02 USD | `STANDARD` | `-0.25%` | `0x9d732bed51` |
| `BUY` | `8.79` | `231.2300` | 2,031.49 USD | 6,320,373.52 USD | `STANDARD` | `-0.31%` | `0x9d732bed51` |
| `BUY` | `8.79` | `142.2200` | 1,249.97 USD | 6,370,316.37 USD | `STANDARD` | `-0.27%` | `0x0ad81cbc47` |
| `BUY` | `8.79` | `82.9700` | 729.23 USD | 6,405,453.04 USD | `STANDARD` | `-0.27%` | `0x010461c14e` |
| `BUY` | `8.79` | `80.0800` | 703.56 USD | 6,409,734.96 USD | `STANDARD` | `-0.31%` | `0x31ca8395cf` |
| `BUY` | `8.80` | `1666.8600` | 14,670.53 USD | 5,371,372.05 USD | `STANDARD` | `-0.13%` | `0x57d8e75f47` |
| `BUY` | `8.80` | `1666.8600` | 14,666.37 USD | 5,386,038.42 USD | `STANDARD` | `-0.16%` | `0x57d8e75f47` |
| `BUY` | `8.80` | `1666.8600` | 14,661.87 USD | 5,400,700.29 USD | `STANDARD` | `-0.19%` | `0x57d8e75f47` |
| `BUY` | `8.80` | `1484.0500` | 13,064.83 USD | 5,571,720.00 USD | `STANDARD` | `-0.11%` | `0x08a49e7f71` |
| `BUY` | `8.80` | `1229.4000` | 10,816.38 USD | 5,733,430.64 USD | `STANDARD` | `-0.17%` | `0x26934acbd3` |
| `BUY` | `8.80` | `1137.9700` | 10,018.46 USD | 5,773,597.00 USD | `STANDARD` | `-0.10%` | `0xaf9f722a67` |
| `BUY` | `8.80` | `1137.9700` | 10,016.75 USD | 5,783,613.75 USD | `STANDARD` | `-0.12%` | `0x621c555167` |
| `BUY` | `8.80` | `481.6400` | 4,237.57 USD | 6,085,048.85 USD | `STANDARD` | `-0.17%` | `0x7717a7a245` |
| `BUY` | `8.80` | `457.0400` | 4,021.95 USD | 6,125,358.98 USD | `STANDARD` | `-0.15%` | `0x6ba889db7f` |
| `BUY` | `8.80` | `456.8000` | 4,020.84 USD | 6,133,401.55 USD | `STANDARD` | `-0.12%` | `0x6ba889db7f` |
| `BUY` | `8.80` | `434.7500` | 3,824.97 USD | 6,137,226.53 USD | `STANDARD` | `-0.17%` | `0xa38f19c4cc` |
| `BUY` | `8.80` | `430.3500` | 3,786.91 USD | 6,144,838.40 USD | `STANDARD` | `-0.15%` | `0xecb63caa47` |
| `BUY` | `8.80` | `403.9300` | 3,556.00 USD | 6,173,627.20 USD | `STANDARD` | `-0.11%` | `0x2a72b57dea` |
| `BUY` | `8.80` | `403.9300` | 3,553.21 USD | 6,177,180.41 USD | `STANDARD` | `-0.18%` | `0x2a72b57dea` |
| `BUY` | `8.80` | `364.7600` | 3,208.79 USD | 6,234,211.44 USD | `STANDARD` | `-0.18%` | `0xecb63caa47` |
| `BUY` | `8.80` | `312.0500` | 2,747.13 USD | 6,263,502.70 USD | `STANDARD` | `-0.11%` | `0x7717a7a245` |
| `BUY` | `8.80` | `302.4300` | 2,662.29 USD | 6,268,905.84 USD | `STANDARD` | `-0.11%` | `0x26934acbd3` |
| `BUY` | `8.80` | `269.1200` | 2,367.50 USD | 6,276,273.32 USD | `STANDARD` | `-0.18%` | `0x33ad48ed92` |
| `BUY` | `8.80` | `255.5700` | 2,249.99 USD | 6,280,885.42 USD | `STANDARD` | `-0.10%` | `0xa38f19c4cc` |
| `BUY` | `8.80` | `244.1800` | 2,149.27 USD | 6,289,636.49 USD | `STANDARD` | `-0.12%` | `0xecb63caa47` |
| `BUY` | `8.80` | `243.9500` | 2,145.86 USD | 6,291,782.34 USD | `STANDARD` | `-0.19%` | `0xecb63caa47` |
| `BUY` | `8.80` | `231.2300` | 2,034.57 USD | 6,314,275.80 USD | `STANDARD` | `-0.16%` | `0x9d732bed51` |
| `BUY` | `8.80` | `200.0000` | 1,760.58 USD | 6,355,025.81 USD | `STANDARD` | `-0.11%` | `0xfc27136e42` |
| `BUY` | `8.80` | `137.5600` | 1,210.51 USD | 6,375,218.52 USD | `STANDARD` | `-0.15%` | `0xdd4f66125d` |
| `BUY` | `8.80` | `137.5600` | 1,210.42 USD | 6,376,428.94 USD | `STANDARD` | `-0.15%` | `0xdd4f66125d` |
| `BUY` | `8.80` | `137.5600` | 1,210.38 USD | 6,377,639.32 USD | `STANDARD` | `-0.16%` | `0xdd4f66125d` |
| `BUY` | `8.80` | `84.4500` | 743.33 USD | 6,402,521.12 USD | `STANDARD` | `-0.12%` | `0x2eddf3aa5c` |
| `BUY` | `8.80` | `80.1100` | 705.04 USD | 6,409,031.40 USD | `STANDARD` | `-0.14%` | `0x31ca8395cf` |
| `BUY` | `8.80` | `78.0600` | 687.00 USD | 6,412,509.60 USD | `STANDARD` | `-0.14%` | `0x010461c14e` |
| `BUY` | `8.80` | `67.9900` | 598.58 USD | 6,419,678.22 USD | `STANDARD` | `-0.10%` | `0x33ad48ed92` |
| `BUY` | `8.80` | `57.3100` | 504.41 USD | 6,425,467.44 USD | `STANDARD` | `-0.13%` | `0x57d8e75f47` |
| `BUY` | `8.80` | `57.3100` | 504.11 USD | 6,425,971.55 USD | `STANDARD` | `-0.19%` | `0x57d8e75f47` |
| `BUY` | `8.80` | `57.0000` | 501.59 USD | 6,427,982.53 USD | `STANDARD` | `-0.15%` | `0x667b8184fc` |
| `ASK` | `8.81` | `54.7800` | 482.87 USD | 2,430.97 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.81` | `221.0200` | 1,948.09 USD | 1,948.09 USD | `3 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `8.81` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.81` | `0.00%` | `-` |
| `BID` | `8.81` | `751.6200` | 6,622.90 USD | 6,622.90 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `8.81` | `457.2500` | 4,029.01 USD | 10,651.91 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.81` | `28.2600` | 249.01 USD | 10,900.92 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.81` | `54.7800` | 482.68 USD | 11,383.60 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.81` | `69.8200` | 615.18 USD | 11,998.77 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.81` | `139.4500` | 1,228.67 USD | 13,227.44 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.81` | `120.4600` | 1,061.34 USD | 14,288.78 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.81` | `43.3800` | 382.20 USD | 14,670.98 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `8.81` | `22.6000` | 199.12 USD | 14,870.10 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.81` | `962.7600` | 8,482.01 USD | 23,352.11 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.81` | `81.3600` | 716.78 USD | 24,068.89 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.81` | `41.0800` | 361.89 USD | 24,430.78 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.81` | `120.0800` | 1,057.83 USD | 25,488.62 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.81` | `5.3100` | 46.78 USD | 25,535.39 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.81` | `112.0900` | 987.42 USD | 26,522.82 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `8.81` | `176.5600` | 1,555.33 USD | 28,078.15 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `8.81` | `403.9300` | 3,558.22 USD | 31,636.37 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.81` | `55.1600` | 485.90 USD | 32,122.27 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.81` | `83.1500` | 732.42 USD | 32,854.69 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.81` | `457.1800` | 4,026.93 USD | 36,881.62 USD | `1 orders` | `-0.05%` | `-` |
| `BUY` | `8.81` | `1666.8600` | 14,685.37 USD | 5,327,343.45 USD | `STANDARD` | `-0.03%` | `0x57d8e75f47` |
| `BUY` | `8.81` | `1666.8600` | 14,681.20 USD | 5,342,024.65 USD | `STANDARD` | `-0.06%` | `0x57d8e75f47` |
| `BUY` | `8.81` | `1666.8600` | 14,676.87 USD | 5,356,701.52 USD | `STANDARD` | `-0.09%` | `0x57d8e75f47` |
| `BUY` | `8.81` | `1362.7900` | 11,999.91 USD | 5,631,999.56 USD | `STANDARD` | `-0.08%` | `0x7d0c59691f` |
| `BUY` | `8.81` | `1135.3800` | 9,999.86 USD | 5,813,622.40 USD | `STANDARD` | `-0.06%` | `0x7d0c59691f` |
| `BUY` | `8.81` | `907.9800` | 7,999.39 USD | 5,928,888.89 USD | `STANDARD` | `-0.03%` | `0x7d0c59691f` |
| `BUY` | `8.81` | `680.8400` | 5,999.22 USD | 6,018,483.20 USD | `STANDARD` | `-0.01%` | `0x7d0c59691f` |
| `BUY` | `8.81` | `483.6300` | 4,258.70 USD | 6,072,306.48 USD | `STANDARD` | `-0.08%` | `0x71d0e11ebb` |
| `BUY` | `8.81` | `457.2500` | 4,029.56 USD | 6,113,281.54 USD | `STANDARD` | `-0.00%` | `0x6ba889db7f` |
| `BUY` | `8.81` | `457.2500` | 4,028.56 USD | 6,117,310.10 USD | `STANDARD` | `-0.03%` | `0x6ba889db7f` |
| `BUY` | `8.81` | `457.1800` | 4,026.93 USD | 6,121,337.03 USD | `STANDARD` | `-0.05%` | `0x6ba889db7f` |
| `BUY` | `8.81` | `456.7500` | 4,021.73 USD | 6,129,380.71 USD | `STANDARD` | `-0.09%` | `0x6ba889db7f` |
| `BUY` | `8.81` | `403.9300` | 3,558.22 USD | 6,170,071.20 USD | `STANDARD` | `-0.04%` | `0x2a72b57dea` |
| `BUY` | `8.81` | `283.8400` | 2,499.98 USD | 6,273,905.81 USD | `STANDARD` | `-0.06%` | `0x0efb38a5fa` |
| `BUY` | `8.81` | `215.5600` | 1,898.05 USD | 6,340,438.21 USD | `STANDARD` | `-0.09%` | `0x023a3d0580` |
| `BUY` | `8.81` | `214.4000` | 1,887.92 USD | 6,342,326.13 USD | `STANDARD` | `-0.08%` | `0xe86b057f5e` |
| `SELL` | `8.81` | `145.4400` | 1,281.92 USD | 6,369,066.40 USD | `STANDARD` | `+0.01%` | `0x727956612a` |
| `BUY` | `8.81` | `139.4500` | 1,228.67 USD | 6,372,795.00 USD | `STANDARD` | `-0.02%` | `0x727956612a` |
| `BUY` | `8.81` | `124.5900` | 1,097.19 USD | 6,385,677.18 USD | `STANDARD` | `-0.07%` | `0x2eddf3aa5c` |
| `BUY` | `8.81` | `121.7800` | 1,072.77 USD | 6,387,823.70 USD | `STANDARD` | `-0.04%` | `0x2eddf3aa5c` |
| `BUY` | `8.81` | `120.4600` | 1,061.34 USD | 6,389,946.91 USD | `STANDARD` | `-0.02%` | `0xecb63caa47` |
| `BUY` | `8.81` | `120.0800` | 1,057.83 USD | 6,392,063.69 USD | `STANDARD` | `-0.04%` | `0x7717a7a245` |
| `BUY` | `8.81` | `113.5700` | 1,000.00 USD | 6,393,063.69 USD | `STANDARD` | `-0.09%` | `0x27c9fa86c9` |
| `BUY` | `8.81` | `113.5300` | 999.96 USD | 6,394,063.65 USD | `STANDARD` | `-0.06%` | `0x0eecd62efb` |
| `BUY` | `8.81` | `85.8800` | 756.36 USD | 6,401,032.08 USD | `STANDARD` | `-0.06%` | `0x010461c14e` |
| `BUY` | `8.81` | `81.3600` | 716.78 USD | 6,407,610.34 USD | `STANDARD` | `-0.03%` | `0x2eddf3aa5c` |
| `BUY` | `8.81` | `79.7300` | 702.22 USD | 6,410,437.18 USD | `STANDARD` | `-0.06%` | `0x31ca8395cf` |
| `BUY` | `8.81` | `69.8200` | 615.18 USD | 6,419,079.64 USD | `STANDARD` | `-0.02%` | `0x2eddf3aa5c` |
| `BUY` | `8.81` | `62.5400` | 550.97 USD | 6,421,380.75 USD | `STANDARD` | `-0.03%` | `0x023a3d0580` |
| `BUY` | `8.81` | `57.3100` | 504.86 USD | 6,424,458.40 USD | `STANDARD` | `-0.04%` | `0x57d8e75f47` |
| `BUY` | `8.81` | `57.3100` | 504.62 USD | 6,424,963.02 USD | `STANDARD` | `-0.09%` | `0x57d8e75f47` |
| `ASK` | `8.82` | `29.4000` | 259.27 USD | 43,780.01 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.82` | `183.7500` | 1,620.44 USD | 43,520.74 USD | `2 orders` | `+0.07%` | `-` |
| `ASK` | `8.82` | `907.2000` | 8,000.23 USD | 41,900.30 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.82` | `23.1900` | 204.49 USD | 33,900.07 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.82` | `137.5600` | 1,213.00 USD | 33,695.58 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.82` | `54.7800` | 483.04 USD | 32,482.57 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.82` | `680.4600` | 6,000.16 USD | 31,999.53 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.82` | `1672.6600` | 14,748.85 USD | 25,999.37 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `8.82` | `54.7900` | 483.09 USD | 11,250.52 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.82` | `54.7800` | 482.99 USD | 10,767.43 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.82` | `44.6800` | 393.93 USD | 10,284.44 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.82` | `57.3100` | 505.29 USD | 9,890.50 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.82` | `89.5700` | 789.68 USD | 9,385.22 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.82` | `54.7800` | 482.95 USD | 8,595.54 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.82` | `457.2400` | 4,031.03 USD | 8,112.59 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.82` | `54.7800` | 482.91 USD | 4,081.56 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.82` | `82.4600` | 726.92 USD | 3,598.65 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `8.82` | `50.0000` | 440.77 USD | 2,871.73 USD | `1 orders` | `+0.03%` | `-` |
| `SELL` | `8.82` | `1666.8600` | 14,708.37 USD | 5,283,258.50 USD | `STANDARD` | `+0.13%` | `0x57d8e75f47` |
| `SELL` | `8.82` | `1666.8600` | 14,701.87 USD | 5,297,960.37 USD | `STANDARD` | `+0.08%` | `0x57d8e75f47` |
| `SELL` | `8.82` | `1666.8600` | 14,697.70 USD | 5,312,658.08 USD | `STANDARD` | `+0.05%` | `0x57d8e75f47` |
| `SELL` | `8.82` | `1480.6900` | 13,064.87 USD | 5,558,655.16 USD | `STANDARD` | `+0.12%` | `0x08a49e7f71` |
| `SELL` | `8.82` | `1360.1000` | 12,002.34 USD | 5,595,999.73 USD | `STANDARD` | `+0.13%` | `0x7d0c59691f` |
| `SELL` | `8.82` | `1137.9700` | 10,040.99 USD | 5,763,578.54 USD | `STANDARD` | `+0.12%` | `0x621c555167` |
| `SELL` | `8.82` | `1133.6200` | 10,000.34 USD | 5,803,622.54 USD | `STANDARD` | `+0.10%` | `0x7d0c59691f` |
| `SELL` | `8.82` | `907.2000` | 8,000.23 USD | 5,904,889.56 USD | `STANDARD` | `+0.07%` | `0x7d0c59691f` |
| `SELL` | `8.82` | `680.4600` | 6,000.16 USD | 6,012,483.98 USD | `STANDARD` | `+0.06%` | `0x7d0c59691f` |
| `SELL` | `8.82` | `457.0500` | 4,031.14 USD | 6,101,189.98 USD | `STANDARD` | `+0.08%` | `0x6ba889db7f` |
| `SELL` | `8.82` | `457.2400` | 4,031.03 USD | 6,105,221.01 USD | `STANDARD` | `+0.04%` | `0x6ba889db7f` |
| `SELL` | `8.82` | `456.8600` | 4,030.97 USD | 6,109,251.98 USD | `STANDARD` | `+0.12%` | `0x6ba889db7f` |
| `SELL` | `8.82` | `403.9300` | 3,563.15 USD | 6,166,512.99 USD | `STANDARD` | `+0.10%` | `0x2a72b57dea` |
| `SELL` | `8.82` | `366.8200` | 3,237.11 USD | 6,227,792.79 USD | `STANDARD` | `+0.14%` | `0xdd4f66125d` |
| `SELL` | `8.82` | `312.0500` | 2,753.50 USD | 6,260,755.57 USD | `STANDARD` | `+0.13%` | `0x7717a7a245` |
| `SELL` | `8.82` | `283.4300` | 2,499.99 USD | 6,271,405.84 USD | `STANDARD` | `+0.09%` | `0x0efb38a5fa` |
| `SELL` | `8.82` | `254.9700` | 2,249.93 USD | 6,283,135.35 USD | `STANDARD` | `+0.13%` | `0xa38f19c4cc` |
| `SELL` | `8.82` | `209.0700` | 1,844.79 USD | 6,347,920.85 USD | `STANDARD` | `+0.12%` | `0x023a3d0580` |
| `SELL` | `8.82` | `200.0000` | 1,763.82 USD | 6,351,501.59 USD | `STANDARD` | `+0.07%` | `0xfc27136e42` |
| `SELL` | `8.82` | `200.0000` | 1,763.64 USD | 6,353,265.23 USD | `STANDARD` | `+0.06%` | `0xfc27136e42` |
| `SELL` | `8.82` | `137.5600` | 1,213.00 USD | 6,374,008.01 USD | `STANDARD` | `+0.06%` | `0xdd4f66125d` |
| `SELL` | `8.82` | `121.6900` | 1,073.74 USD | 6,386,750.93 USD | `STANDARD` | `+0.12%` | `0x2eddf3aa5c` |
| `SELL` | `8.82` | `120.3600` | 1,061.88 USD | 6,388,885.58 USD | `STANDARD` | `+0.11%` | `0x2eddf3aa5c` |
| `SELL` | `8.82` | `120.0800` | 1,058.95 USD | 6,391,005.86 USD | `STANDARD` | `+0.07%` | `0x7717a7a245` |
| `SELL` | `8.82` | `113.3800` | 999.94 USD | 6,395,063.59 USD | `STANDARD` | `+0.07%` | `0x27c9fa86c9` |
| `SELL` | `8.82` | `113.3800` | 999.93 USD | 6,396,063.53 USD | `STANDARD` | `+0.07%` | `0x0eecd62efb` |
| `SELL` | `8.82` | `91.7000` | 809.06 USD | 6,397,868.18 USD | `STANDARD` | `+0.11%` | `0xdd4f66125d` |
| `SELL` | `8.82` | `91.7000` | 808.98 USD | 6,398,677.16 USD | `STANDARD` | `+0.10%` | `0xdd4f66125d` |
| `SELL` | `8.82` | `91.7000` | 808.89 USD | 6,399,486.04 USD | `STANDARD` | `+0.09%` | `0xdd4f66125d` |
| `SELL` | `8.82` | `89.5700` | 789.68 USD | 6,400,275.72 USD | `STANDARD` | `+0.04%` | `0xecb63caa47` |
| `SELL` | `8.82` | `84.5400` | 745.71 USD | 6,401,777.79 USD | `STANDARD` | `+0.09%` | `0x010461c14e` |
| `SELL` | `8.82` | `78.3300` | 690.89 USD | 6,411,822.60 USD | `STANDARD` | `+0.09%` | `0x2eddf3aa5c` |
| `SELL` | `8.82` | `77.5800` | 684.33 USD | 6,413,879.26 USD | `STANDARD` | `+0.09%` | `0x31ca8395cf` |
| `SELL` | `8.82` | `72.4800` | 639.30 USD | 6,417,833.49 USD | `STANDARD` | `+0.09%` | `0x2eddf3aa5c` |
| `SELL` | `8.82` | `66.8700` | 590.07 USD | 6,420,268.29 USD | `STANDARD` | `+0.13%` | `0x33ad48ed92` |
| `SELL` | `8.82` | `63.6700` | 561.49 USD | 6,420,829.77 USD | `STANDARD` | `+0.07%` | `0x023a3d0580` |
| `SELL` | `8.82` | `57.3100` | 505.49 USD | 6,423,448.26 USD | `STANDARD` | `+0.09%` | `0x57d8e75f47` |
| `SELL` | `8.82` | `57.3100` | 505.29 USD | 6,423,953.55 USD | `STANDARD` | `+0.04%` | `0x57d8e75f47` |
| `SELL` | `8.83` | `16762.1400` | 148,080.10 USD | 3,023,282.17 USD | `LARGE (>= USD 100K)` | `+0.24%` | `0x71d0e11ebb` |
| `SELL` | `8.83` | `1666.8600` | 14,722.71 USD | 5,239,120.55 USD | `STANDARD` | `+0.22%` | `0x57d8e75f47` |
| `SELL` | `8.83` | `1666.8600` | 14,717.04 USD | 5,253,837.59 USD | `STANDARD` | `+0.19%` | `0x57d8e75f47` |
| `SELL` | `8.83` | `1666.8600` | 14,712.54 USD | 5,268,550.13 USD | `STANDARD` | `+0.16%` | `0x57d8e75f47` |
| `SELL` | `8.83` | `1137.9700` | 10,048.39 USD | 5,753,537.55 USD | `STANDARD` | `+0.20%` | `0xaf9f722a67` |
| `SELL` | `8.83` | `1069.8000` | 9,449.44 USD | 5,852,548.86 USD | `STANDARD` | `+0.23%` | `0x26934acbd3` |
| `SELL` | `8.83` | `483.4500` | 4,267.80 USD | 6,068,047.78 USD | `STANDARD` | `+0.17%` | `0x71d0e11ebb` |
| `SELL` | `8.83` | `481.6400` | 4,253.75 USD | 6,076,560.23 USD | `STANDARD` | `+0.22%` | `0x7717a7a245` |
| `SELL` | `8.83` | `457.2500` | 4,037.65 USD | 6,089,086.51 USD | `STANDARD` | `+0.20%` | `0x6ba889db7f` |
| `SELL` | `8.83` | `457.2100` | 4,036.30 USD | 6,093,122.80 USD | `STANDARD` | `+0.17%` | `0x6ba889db7f` |
| `SELL` | `8.83` | `457.2800` | 4,036.04 USD | 6,097,158.85 USD | `STANDARD` | `+0.15%` | `0x6ba889db7f` |
| `SELL` | `8.83` | `433.0600` | 3,824.96 USD | 6,141,051.49 USD | `STANDARD` | `+0.22%` | `0xa38f19c4cc` |
| `SELL` | `8.83` | `403.9300` | 3,566.10 USD | 6,162,949.84 USD | `STANDARD` | `+0.18%` | `0x2a72b57dea` |
| `SELL` | `8.83` | `367.5500` | 3,243.78 USD | 6,218,076.83 USD | `STANDARD` | `+0.14%` | `0xecb63caa47` |
| `SELL` | `8.83` | `366.8200` | 3,240.67 USD | 6,221,317.50 USD | `STANDARD` | `+0.25%` | `0xdd4f66125d` |
| `SELL` | `8.83` | `366.8200` | 3,238.18 USD | 6,224,555.68 USD | `STANDARD` | `+0.17%` | `0xdd4f66125d` |
| `SELL` | `8.83` | `354.9800` | 3,133.62 USD | 6,243,755.69 USD | `STANDARD` | `+0.17%` | `0xecb63caa47` |
| `SELL` | `8.83` | `333.6800` | 2,947.20 USD | 6,246,702.88 USD | `STANDARD` | `+0.22%` | `0xecb63caa47` |
| `SELL` | `8.83` | `267.4800` | 2,362.12 USD | 6,278,635.43 USD | `STANDARD` | `+0.21%` | `0x33ad48ed92` |
| `SELL` | `8.83` | `246.1500` | 2,173.55 USD | 6,287,487.21 USD | `STANDARD` | `+0.20%` | `0xecb63caa47` |
| `SELL` | `8.83` | `231.2300` | 2,042.20 USD | 6,310,199.95 USD | `STANDARD` | `+0.22%` | `0x9d732bed51` |
| `SELL` | `8.83` | `231.2300` | 2,041.28 USD | 6,312,241.23 USD | `STANDARD` | `+0.17%` | `0x9d732bed51` |
| `SELL` | `8.83` | `205.8700` | 1,816.93 USD | 6,349,737.77 USD | `STANDARD` | `+0.15%` | `0x26934acbd3` |
| `SELL` | `8.83` | `83.2600` | 735.02 USD | 6,403,256.14 USD | `STANDARD` | `+0.17%` | `0x010461c14e` |
| `SELL` | `8.83` | `83.1700` | 734.21 USD | 6,403,990.35 USD | `STANDARD` | `+0.17%` | `0x2eddf3aa5c` |
| `SELL` | `8.83` | `81.4200` | 718.77 USD | 6,406,893.56 USD | `STANDARD` | `+0.17%` | `0x31ca8395cf` |
| `SELL` | `8.83` | `57.3100` | 506.19 USD | 6,422,436.97 USD | `STANDARD` | `+0.22%` | `0x57d8e75f47` |
| `SELL` | `8.83` | `57.3100` | 505.81 USD | 6,422,942.77 USD | `STANDARD` | `+0.15%` | `0x57d8e75f47` |
| `SELL` | `8.83` | `57.0000` | 503.36 USD | 6,426,474.90 USD | `STANDARD` | `+0.20%` | `0x667b8184fc` |
| `SELL` | `8.83` | `57.0000` | 503.32 USD | 6,426,978.23 USD | `STANDARD` | `+0.20%` | `0x940587add0` |
| `SELL` | `8.84` | `4151.1300` | 36,693.91 USD | 4,742,650.14 USD | `MEDIUM (>= USD 25K)` | `+0.30%` | `0x08a49e7f71` |
| `SELL` | `8.84` | `1666.8600` | 14,739.88 USD | 5,180,204.71 USD | `STANDARD` | `+0.34%` | `0x57d8e75f47` |
| `SELL` | `8.84` | `1666.8600` | 14,735.21 USD | 5,194,939.92 USD | `STANDARD` | `+0.31%` | `0x57d8e75f47` |
| `SELL` | `8.84` | `1666.8600` | 14,731.04 USD | 5,209,670.97 USD | `STANDARD` | `+0.28%` | `0x57d8e75f47` |
| `SELL` | `8.84` | `1666.8600` | 14,726.87 USD | 5,224,397.84 USD | `STANDARD` | `+0.25%` | `0x57d8e75f47` |
| `SELL` | `8.84` | `1250.5000` | 11,054.17 USD | 5,711,681.26 USD | `STANDARD` | `+0.31%` | `0xa38f19c4cc` |
| `SELL` | `8.84` | `1137.9700` | 10,058.52 USD | 5,743,489.16 USD | `STANDARD` | `+0.30%` | `0xaf9f722a67` |
| `SELL` | `8.84` | `735.6600` | 6,502.43 USD | 6,000,241.18 USD | `STANDARD` | `+0.30%` | `0xa38f19c4cc` |
| `SELL` | `8.84` | `565.7000` | 5,000.00 USD | 6,040,437.33 USD | `STANDARD` | `+0.29%` | `0x0efb38a5fa` |
| `SELL` | `8.84` | `502.0500` | 4,439.33 USD | 6,059,481.09 USD | `STANDARD` | `+0.34%` | `0xecb63caa47` |
| `SELL` | `8.84` | `420.0000` | 3,711.12 USD | 6,148,549.52 USD | `STANDARD` | `+0.26%` | `0xb7bd9cef0e` |
| `SELL` | `8.84` | `403.9300` | 3,568.84 USD | 6,159,383.74 USD | `STANDARD` | `+0.26%` | `0x2a72b57dea` |
| `SELL` | `8.84` | `246.5100` | 2,178.31 USD | 6,285,313.66 USD | `STANDARD` | `+0.27%` | `0xecb63caa47` |
| `SELL` | `8.84` | `231.2300` | 2,044.40 USD | 6,306,114.54 USD | `STANDARD` | `+0.32%` | `0x9d732bed51` |
| `SELL` | `8.84` | `231.2300` | 2,043.22 USD | 6,308,157.75 USD | `STANDARD` | `+0.27%` | `0x9d732bed51` |
| `SELL` | `8.84` | `81.6500` | 721.75 USD | 6,406,174.79 USD | `STANDARD` | `+0.30%` | `0x010461c14e` |
| `SELL` | `8.84` | `73.7600` | 651.99 USD | 6,416,548.14 USD | `STANDARD` | `+0.30%` | `0x31ca8395cf` |
| `SELL` | `8.85` | `1666.8600` | 14,755.38 USD | 5,135,969.08 USD | `STANDARD` | `+0.45%` | `0x57d8e75f47` |
| `SELL` | `8.85` | `1666.8600` | 14,750.38 USD | 5,150,719.46 USD | `STANDARD` | `+0.41%` | `0x57d8e75f47` |
| `SELL` | `8.85` | `1666.8600` | 14,745.38 USD | 5,165,464.84 USD | `STANDARD` | `+0.38%` | `0x57d8e75f47` |
| `SELL` | `8.85` | `1106.4200` | 9,792.37 USD | 5,833,382.96 USD | `STANDARD` | `+0.43%` | `0xd3342d3b1e` |
| `SELL` | `8.85` | `988.6200` | 8,749.09 USD | 5,888,277.64 USD | `STANDARD` | `+0.42%` | `0xd3943e4008` |
| `SELL` | `8.85` | `854.5800` | 7,566.79 USD | 5,944,028.27 USD | `STANDARD` | `+0.47%` | `0xecb63caa47` |
| `SELL` | `8.85` | `785.2600` | 6,953.08 USD | 5,980,283.21 USD | `STANDARD` | `+0.47%` | `0x47a4471457` |
| `SELL` | `8.85` | `705.6300` | 6,242.64 USD | 6,006,483.82 USD | `STANDARD` | `+0.39%` | `0xecb63caa47` |
| `SELL` | `8.85` | `672.8200` | 5,953.78 USD | 6,030,408.04 USD | `STANDARD` | `+0.41%` | `0x33ad48ed92` |
| `SELL` | `8.85` | `403.9300` | 3,573.21 USD | 6,155,814.90 USD | `STANDARD` | `+0.38%` | `0x2a72b57dea` |
| `SELL` | `8.85` | `231.2300` | 2,047.47 USD | 6,299,978.29 USD | `STANDARD` | `+0.48%` | `0x9d732bed51` |
| `SELL` | `8.85` | `231.2300` | 2,046.45 USD | 6,302,024.75 USD | `STANDARD` | `+0.43%` | `0x9d732bed51` |
| `SELL` | `8.85` | `231.2300` | 2,045.39 USD | 6,304,070.14 USD | `STANDARD` | `+0.37%` | `0x9d732bed51` |
| `SELL` | `8.85` | `131.2700` | 1,161.71 USD | 6,381,133.16 USD | `STANDARD` | `+0.42%` | `0xe34d21d198` |
| `SELL` | `8.86` | `14833.4300` | 131,390.07 USD | 3,302,080.25 USD | `LARGE (>= USD 100K)` | `+0.51%` | `0x71d0e11ebb` |
| `SELL` | `8.86` | `1666.8600` | 14,769.38 USD | 5,091,688.78 USD | `STANDARD` | `+0.54%` | `0x57d8e75f47` |
| `SELL` | `8.86` | `1666.8600` | 14,764.88 USD | 5,106,453.66 USD | `STANDARD` | `+0.51%` | `0x57d8e75f47` |
| `SELL` | `8.86` | `1666.8600` | 14,760.05 USD | 5,121,213.71 USD | `STANDARD` | `+0.48%` | `0x57d8e75f47` |
| `SELL` | `8.86` | `1125.2300` | 9,968.19 USD | 5,823,590.59 USD | `STANDARD` | `+0.52%` | `0xd3943e4008` |
| `SELL` | `8.86` | `903.0500` | 7,999.94 USD | 5,920,889.49 USD | `STANDARD` | `+0.52%` | `0x0efb38a5fa` |
| `SELL` | `8.86` | `830.0000` | 7,355.04 USD | 5,958,824.97 USD | `STANDARD` | `+0.55%` | `0xb7bd9cef0e` |
| `SELL` | `8.86` | `520.3400` | 4,608.65 USD | 6,055,041.76 USD | `STANDARD` | `+0.50%` | `0x26934acbd3` |
| `SELL` | `8.86` | `485.1200` | 4,298.89 USD | 6,063,779.98 USD | `STANDARD` | `+0.55%` | `0xcd7f60e943` |
| `SELL` | `8.86` | `231.2300` | 2,049.55 USD | 6,295,882.38 USD | `STANDARD` | `+0.58%` | `0x9d732bed51` |
| `SELL` | `8.86` | `231.2300` | 2,048.44 USD | 6,297,930.82 USD | `STANDARD` | `+0.52%` | `0x9d732bed51` |
| `SELL` | `8.86` | `77.1900` | 683.93 USD | 6,414,563.20 USD | `STANDARD` | `+0.54%` | `0x31ca8395cf` |
| `SELL` | `8.86` | `71.2000` | 630.97 USD | 6,418,464.47 USD | `STANDARD` | `+0.56%` | `0x010461c14e` |
| `SELL` | `8.87` | `23861.3700` | 211,693.30 USD | 1,851,726.38 USD | `LARGE (>= USD 100K)` | `+0.67%` | `0x71cfa5e263` |
| `SELL` | `8.87` | `2117.5000` | 18,792.18 USD | 4,977,893.94 USD | `STANDARD` | `+0.70%` | `0xa38f19c4cc` |
| `SELL` | `8.87` | `1666.8600` | 14,777.71 USD | 5,076,919.40 USD | `STANDARD` | `+0.60%` | `0x57d8e75f47` |
| `SELL` | `8.87` | `1286.3700` | 11,405.47 USD | 5,678,470.41 USD | `STANDARD` | `+0.61%` | `0xd3943e4008` |
| `SELL` | `8.87` | `1009.2200` | 8,956.63 USD | 5,870,692.21 USD | `STANDARD` | `+0.70%` | `0x33ad48ed92` |
| `SELL` | `8.87` | `231.2300` | 2,050.48 USD | 6,293,832.82 USD | `STANDARD` | `+0.62%` | `0x9d732bed51` |
| `SELL` | `8.87` | `225.3700` | 1,998.90 USD | 6,336,542.76 USD | `STANDARD` | `+0.64%` | `0xd2ccf2ebc5` |
| `SELL` | `8.87` | `131.2700` | 1,164.60 USD | 6,379,971.45 USD | `STANDARD` | `+0.67%` | `0xe34d21d198` |
| `SELL` | `8.88` | `17551.4100` | 155,853.01 USD | 2,568,903.47 USD | `LARGE (>= USD 100K)` | `+0.76%` | `0x71d0e11ebb` |
| `SELL` | `8.88` | `1518.7300` | 13,481.01 USD | 5,545,590.29 USD | `STANDARD` | `+0.72%` | `0xd3943e4008` |
| `SELL` | `8.88` | `1350.9500` | 11,999.95 USD | 5,619,999.65 USD | `STANDARD` | `+0.79%` | `0x0efb38a5fa` |
| `SELL` | `8.88` | `1250.0000` | 11,102.50 USD | 5,689,572.91 USD | `STANDARD` | `+0.79%` | `0xb7bd9cef0e` |
| `SELL` | `8.88` | `383.6100` | 3,406.23 USD | 6,198,078.10 USD | `STANDARD` | `+0.76%` | `0x14f8e04290` |
| `SELL` | `8.89` | `11268.0500` | 100,117.75 USD | 4,320,831.62 USD | `LARGE (>= USD 100K)` | `+0.82%` | `0x881cd92459` |
| `SELL` | `8.89` | `3591.7000` | 31,946.73 USD | 4,878,854.62 USD | `MEDIUM (>= USD 25K)` | `+0.93%` | `0xa38f19c4cc` |
| `SELL` | `8.89` | `131.2700` | 1,167.53 USD | 6,378,806.84 USD | `STANDARD` | `+0.92%` | `0xe34d21d198` |
| `SELL` | `8.90` | `11015.1800` | 98,064.84 USD | 4,418,896.46 USD | `MEDIUM (>= USD 25K)` | `+1.02%` | `0xecb63caa47` |
| `SELL` | `8.90` | `565.0000` | 5,029.29 USD | 6,035,437.33 USD | `STANDARD` | `+1.01%` | `0x3ca146d269` |
| `SELL` | `8.90` | `382.5000` | 3,406.05 USD | 6,201,484.14 USD | `STANDARD` | `+1.04%` | `0x14f8e04290` |
| `SELL` | `8.90` | `82.3700` | 733.46 USD | 6,404,723.81 USD | `STANDARD` | `+1.04%` | `0x010461c14e` |
| `SELL` | `8.91` | `46727.4000` | 416,504.68 USD | 1,231,889.22 USD | `LARGE (>= USD 100K)` | `+1.14%` | `0x71cfa5e263` |
| `SELL` | `8.91` | `17551.4700` | 156,441.52 USD | 2,413,050.46 USD | `LARGE (>= USD 100K)` | `+1.14%` | `0x71d0e11ebb` |
| `SELL` | `8.91` | `4647.3700` | 41,402.95 USD | 4,705,956.22 USD | `MEDIUM (>= USD 25K)` | `+1.09%` | `0xa24c5ca26c` |
| `SELL` | `8.91` | `1336.1900` | 11,907.06 USD | 5,643,906.62 USD | `STANDARD` | `+1.12%` | `0x33ad48ed92` |
| `SELL` | `8.91` | `315.7300` | 2,812.84 USD | 6,255,243.22 USD | `STANDARD` | `+1.09%` | `0x07fd993f0f` |
| `SELL` | `8.91` | `224.9000` | 2,003.25 USD | 6,334,543.86 USD | `STANDARD` | `+1.07%` | `0x39bac00809` |
| `SELL` | `8.91` | `210.4600` | 1,874.99 USD | 6,344,201.12 USD | `STANDARD` | `+1.09%` | `0x0ad81cbc47` |
| `SELL` | `8.92` | `7548.9600` | 67,341.25 USD | 4,664,553.27 USD | `MEDIUM (>= USD 25K)` | `+1.22%` | `0xecb63caa47` |
| `SELL` | `8.92` | `1793.2500` | 15,999.91 USD | 5,047,091.21 USD | `STANDARD` | `+1.24%` | `0x0efb38a5fa` |
| `SELL` | `8.92` | `1687.5000` | 15,050.47 USD | 5,062,141.69 USD | `STANDARD` | `+1.20%` | `0xd3943e4008` |
| `SELL` | `8.92` | `72.4300` | 646.05 USD | 6,417,194.19 USD | `STANDARD` | `+1.21%` | `0x31ca8395cf` |
| `SELL` | `8.93` | `111.4300` | 995.59 USD | 6,397,059.12 USD | `STANDARD` | `+1.38%` | `0x23cc6b8202` |
| `SELL` | `8.94` | `13507.6500` | 120,740.83 USD | 3,552,923.10 USD | `LARGE (>= USD 100K)` | `+1.43%` | `0xecb63caa47` |
| `SELL` | `8.94` | `2263.7100` | 20,247.30 USD | 4,921,101.92 USD | `STANDARD` | `+1.49%` | `0xd3943e4008` |
| `SELL` | `8.94` | `382.5900` | 3,418.75 USD | 6,194,671.87 USD | `STANDARD` | `+1.40%` | `0x14f8e04290` |
| `SELL` | `8.94` | `177.3800` | 1,586.59 USD | 6,361,584.37 USD | `STANDARD` | `+1.50%` | `0xdadbb4b2a0` |
| `SELL` | `8.95` | `12893.5400` | 115,439.73 USD | 3,785,652.90 USD | `LARGE (>= USD 100K)` | `+1.59%` | `0x71d0e11ebb` |
| `SELL` | `8.95` | `2123.1800` | 18,999.91 USD | 4,959,101.76 USD | `STANDARD` | `+1.54%` | `0x0efb38a5fa` |
| `SELL` | `8.95` | `209.4900` | 1,874.94 USD | 6,346,076.06 USD | `STANDARD` | `+1.56%` | `0x0ad81cbc47` |
| `SELL` | `8.96` | `12037.9800` | 107,825.39 USD | 4,120,596.09 USD | `LARGE (>= USD 100K)` | `+1.64%` | `0xecb63caa47` |
| `SELL` | `8.97` | `383.1600` | 3,435.37 USD | 6,191,253.12 USD | `STANDARD` | `+1.74%` | `0x14f8e04290` |
| `SELL` | `8.97` | `315.7300` | 2,831.15 USD | 6,252,430.38 USD | `STANDARD` | `+1.75%` | `0x07fd993f0f` |
| `SELL` | `8.97` | `193.6100` | 1,736.84 USD | 6,356,762.65 USD | `STANDARD` | `+1.79%` | `0x31ca8395cf` |
| `SELL` | `8.97` | `175.0500` | 1,570.23 USD | 6,363,154.60 USD | `STANDARD` | `+1.79%` | `0x010461c14e` |
| `SELL` | `8.98` | `90808.1500` | 815,384.54 USD | 815,384.54 USD | `LARGE (>= USD 100K)` | `+1.89%` | `0x71cfa5e263` |
| `SELL` | `8.98` | `56.0000` | 502.71 USD | 6,427,480.94 USD | `STANDARD` | `+1.86%` | `0x6628f82999` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:43:50 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1495` | `0x7737...bf66` | `SHORT` | 1,510,485.20 USD | `171,568.06` | `7.43` | `8.81` | `110.44` | -234,940.18 USD | `-15.55%` | `10X Cross` |
| `1578` | `0xeadc...9d55` | `LONG` | 1,409,261.21 USD | `160,070.56` | `8.11` | `8.81` | `0.000000` | 111,623.64 USD | `+7.92%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`9.22` (Vol: 276,800.00 USD, Dist: `+4.36%`) | Long MP=`8.46` (Vol: 190,100.00 USD, Dist: `--4.29%`)
  * 48H Horizon: Short MP=`9.22` (Vol: 221,300.00 USD, Dist: `+4.36%`) | Long MP=`8.46` (Vol: 190,100.00 USD, Dist: `--4.29%`)
  * 3D Horizon: Short MP=`9.22` (Vol: 264,100.00 USD, Dist: `+4.36%`) | Long MP=`8.75` (Vol: 159,700.00 USD, Dist: `--0.96%`)
  * 7D Horizon: Short MP=`9.28` (Vol: 419,200.00 USD, Dist: `+5.04%`) | Long MP=`8.54` (Vol: 343,100.00 USD, Dist: `--3.39%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.85` | 204.05 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 481.25 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 159.60 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 104.26 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 375.35 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 2,170.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 290.37 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 265.65 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 814.80 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 17,370.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 109.88 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 133.73 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 45,470.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 1,130.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 1,460.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 404.38 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 114.82 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 152.25 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 775.18 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 341.01 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.98` | 371.88 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.08` | 9,290.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 1,130.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.18` | 174.89 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.20` | 419.50 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.29` | 2,440.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.30` | 174.83 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.32` | 852.47 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.33` | 2,190.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.37` | 117.86 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.51` | 217.71 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 486.93 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 2,680.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,490.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,730.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 240.48 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.80` | 15,790.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 6,380.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 146.85 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 527.19 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,350.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.99` | 329.11 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 167.78 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 314.59 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 318.46 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.09` | 4,690.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.16` | 156,890.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 2,300.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 300.91 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 640.70 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 21,080.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 163,110.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.51` | 367.41 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 121.38 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.57` | 967.98 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.59` | 34,430.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 22,270.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.66` | 4,160.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.70` | 405.03 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 2,340.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 238.86 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 2,890.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 736.72 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 580.50 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.88` | 329,350.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 640.67 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 12,380.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.99` | 447.98 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.03` | 404.46 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 331.68 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 448.72 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 1,630.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 405.14 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,550.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.11` | 3,200.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.13` | 2,370.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 4,390.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 187.29 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 2,560.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.22` | 715.31 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 972.65 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.29` | 1,610.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.32` | 277.04 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 105.25 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 5,110.00 USD | 896,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.41` | 1,640.00 USD | 891,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 890,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 889,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 883,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.50` | 1,720.00 USD | 882,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 3,620.00 USD | 880,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 876,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 2,170.00 USD | 867,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 1,100.00 USD | 865,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 864,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.70` | 506.54 USD | 862,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 16,610.00 USD | 861,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 845,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 6,780.00 USD | 843,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 16,960.00 USD | 837,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 4,260.00 USD | 820,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 815,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 2,670.00 USD | 814,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 158.14 USD | 811,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 4,830.00 USD | 811,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.86` | 18,930.00 USD | 806,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 787,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.89` | 5,250.00 USD | 784,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.91` | 269.30 USD | 779,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 1,510.00 USD | 778,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,760.00 USD | 777,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 3,480.00 USD | 773,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 28,500.00 USD | 770,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.99` | 1,400.00 USD | 741,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 1,550.00 USD | 740,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 24,240.00 USD | 738,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.04` | 4,100.00 USD | 714,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 710,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,670.00 USD | 703,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,230.00 USD | 702,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 673,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 2,300.00 USD | 673,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,950.00 USD | 671,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.16` | 1,630.00 USD | 650,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 648,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 581.02 USD | 647,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.24` | 179.65 USD | 646,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 646,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,560.00 USD | 646,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 19,790.00 USD | 609,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.32` | 168.76 USD | 589,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 4,910.00 USD | 589,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 2,450.00 USD | 584,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 4,370.00 USD | 582,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.37` | 5,720.00 USD | 577,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 3,920.00 USD | 572,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 17,770.00 USD | 568,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.39` | 1,550.00 USD | 550,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.42` | 1,540.00 USD | 548,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 1,700.00 USD | 547,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 1,370.00 USD | 545,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 5,430.00 USD | 544,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 3,210.00 USD | 538,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,580.00 USD | 535,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,080.00 USD | 534,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.53` | 995.86 USD | 533,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 532,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 157.14 USD | 527,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.57` | 118.09 USD | 527,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 4,260.00 USD | 527,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.59` | 25,140.00 USD | 523,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 312.22 USD | 498,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 497,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.63` | 514.52 USD | 497,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 496,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.67` | 1,740.00 USD | 496,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.68` | 1,120.00 USD | 494,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.70` | 1,460.00 USD | 493,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.71` | 19,410.00 USD | 492,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.72` | 2,550.00 USD | 472,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 893.76 USD | 470,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 469,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.78` | 695.32 USD | 468,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,900.00 USD | 468,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 1,940.00 USD | 464,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.80` | 9,610,000.00 USD | 9,610,000.00 USD | 22,120.00 USD | 12,980.00 USD | 15,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 633.77 USD | 462,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.82` | 5,280.00 USD | 461,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.82` | 9,560,000.00 USD | 9,560,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 9,550,000.00 USD | 9,550,000.00 USD | 29,020.00 USD | 2,380.00 USD | 19,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 10,930.00 USD | 456,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.86` | 2,110.00 USD | 445,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.86` | 9,500,000.00 USD | 9,500,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 176.18 USD | 443,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 443,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.88` | 9,450,000.00 USD | 9,450,000.00 USD | 46,450.00 USD | 12,780.00 USD | 29,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 9,360,000.00 USD | 9,360,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 2,410.00 USD | 442,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 5,010,000.00 USD | 5,010,000.00 USD | 11,920.00 USD | 3,480.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.92` | 4,980,000.00 USD | 4,980,000.00 USD | 13,160.00 USD | 2,950.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.92` | 9,300,000.00 USD | 9,300,000.00 USD | 53,660.00 USD | 8,420.00 USD | 14,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 923.42 USD | 440,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 4,960,000.00 USD | 4,960,000.00 USD | 7,960.00 USD | 2,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 1,820.00 USD | 439,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 4,950,000.00 USD | 4,950,000.00 USD | 7,590.00 USD | 4,150.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.94` | 9,220,000.00 USD | 9,220,000.00 USD | 49,080.00 USD | 9,960.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 437,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 4,940,000.00 USD | 4,940,000.00 USD | 74.90 USD | 5,170.00 USD | 3,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 843.15 USD | 310,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 4,930,000.00 USD | 4,930,000.00 USD | 2,760.00 USD | 3,170.00 USD | 13.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.96` | 9,130,000.00 USD | 9,130,000.00 USD | 21,840.00 USD | 6,920.00 USD | 26,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.97` | 4,920,000.00 USD | 4,920,000.00 USD | 5,250.00 USD | 0.00 USD | 2,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.98` | 4,920,000.00 USD | 4,920,000.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.98` | 9,070,000.00 USD | 9,070,000.00 USD | 43,200.00 USD | 19,680.00 USD | 70,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,600.00 USD | 309,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 4,910,000.00 USD | 4,910,000.00 USD | 482.38 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 210.99 USD | 307,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 4,910,000.00 USD | 4,910,000.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.00` | 8,940,000.00 USD | 8,940,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 4,900,000.00 USD | 4,900,000.00 USD | 6,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 4,900,000.00 USD | 4,900,000.00 USD | 9,100.00 USD | 770.83 USD | 9.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.02` | 8,860,000.00 USD | 8,860,000.00 USD | 20,910.00 USD | 28,440.00 USD | 10,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 957.70 USD | 307,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 4,890,000.00 USD | 4,890,000.00 USD | 8,600.00 USD | 1,540.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 88,380.00 USD | 306,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.04` | 4,870,000.00 USD | 4,870,000.00 USD | 9,860.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.04` | 8,800,000.00 USD | 8,800,000.00 USD | 123,080.00 USD | 27,860.00 USD | 86,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 6,890.00 USD | 218,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.05` | 4,860,000.00 USD | 4,860,000.00 USD | 17,150.00 USD | 4,800.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.05` | 3,340.00 USD | 211,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.06` | 4,830,000.00 USD | 4,830,000.00 USD | 16,840.00 USD | 1,700.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.06` | 8,570,000.00 USD | 8,570,000.00 USD | 70,840.00 USD | 10,070.00 USD | 86,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 37,830.00 USD | 208,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 4,810,000.00 USD | 4,810,000.00 USD | 1,100.00 USD | 2,400.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.08` | 4,800,000.00 USD | 4,800,000.00 USD | 4,700.00 USD | 1,410.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.08` | 8,400,000.00 USD | 8,400,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 617.61 USD | 170,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.09` | 4,790,000.00 USD | 4,790,000.00 USD | 9,630.00 USD | 1,220.00 USD | 6,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.10` | 165.46 USD | 169,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.10` | 4,770,000.00 USD | 4,770,000.00 USD | 23,830.00 USD | 3,750.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.10` | 8,360,000.00 USD | 8,360,000.00 USD | 61,500.00 USD | 19,700.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.11` | 11,550.00 USD | 169,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.11` | 4,740,000.00 USD | 4,740,000.00 USD | 4,510.00 USD | 4,240.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 241.26 USD | 157,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 4,730,000.00 USD | 4,730,000.00 USD | 9,910.00 USD | 0.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.12` | 8,270,000.00 USD | 8,270,000.00 USD | 27,520.00 USD | 10,810.00 USD | 9,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.13` | 4,710,000.00 USD | 4,710,000.00 USD | 7,130.00 USD | 693.45 USD | 1,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 4,700,000.00 USD | 4,700,000.00 USD | 16,900.00 USD | 0.00 USD | 26.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.14` | 8,220,000.00 USD | 8,220,000.00 USD | 72,460.00 USD | 11,150.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 4,680,000.00 USD | 4,680,000.00 USD | 14,590.00 USD | 662.47 USD | 5,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 4,660,000.00 USD | 4,660,000.00 USD | 385.98 USD | 2,120.00 USD | 47.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 8,100,000.00 USD | 8,100,000.00 USD | 38,430.00 USD | 5,510.00 USD | 30,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.16` | 871.61 USD | 157,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.17` | 4,660,000.00 USD | 4,660,000.00 USD | 2,970.00 USD | 0.00 USD | 12.32 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 4,660,000.00 USD | 4,660,000.00 USD | 1,150.00 USD | 1,980.00 USD | 466.21 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 8,020,000.00 USD | 8,020,000.00 USD | 10,520.00 USD | 6,790.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.19` | 4,650,000.00 USD | 4,650,000.00 USD | 4,450.00 USD | 0.00 USD | 19.88 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.20` | 1,290.00 USD | 156,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.20` | 4,650,000.00 USD | 4,650,000.00 USD | 7,720.00 USD | 2,310.00 USD | 445.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.20` | 8,000,000.00 USD | 8,000,000.00 USD | 34,140.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 1,910.00 USD | 155,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.21` | 4,640,000.00 USD | 4,640,000.00 USD | 2,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 147.87 USD | 153,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.22` | 4,640,000.00 USD | 4,640,000.00 USD | 5,330.00 USD | 0.00 USD | 12,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.22` | 7,960,000.00 USD | 7,960,000.00 USD | 19,610.00 USD | 0.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.22` | 2,100.00 USD | 153,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.23` | 4,620,000.00 USD | 4,620,000.00 USD | 20,920.00 USD | 4,080.00 USD | 31,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.23` | 1,160.00 USD | 151,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.24` | 4,560,000.00 USD | 4,560,000.00 USD | 10,190.00 USD | 1,150.00 USD | 3,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 7,930,000.00 USD | 7,930,000.00 USD | 39,950.00 USD | 3,480.00 USD | 107,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.24` | 1,300.00 USD | 150,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.25` | 4,550,000.00 USD | 4,550,000.00 USD | 8,080.00 USD | 0.00 USD | 6,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.26` | 13,810.00 USD | 148,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.26` | 4,530,000.00 USD | 4,530,000.00 USD | 192.60 USD | 11,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.26` | 7,780,000.00 USD | 7,780,000.00 USD | 30,490.00 USD | 5,750.00 USD | 9,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.27` | 4,520,000.00 USD | 4,520,000.00 USD | 11,310.00 USD | 2,760.00 USD | 21.52 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.28` | 9,860.00 USD | 135,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.28` | 4,510,000.00 USD | 4,510,000.00 USD | 74,500.00 USD | 7,070.00 USD | 40,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.28` | 7,730,000.00 USD | 7,730,000.00 USD | 122,850.00 USD | 33,920.00 USD | 14,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 498.26 USD | 125,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.29` | 4,390,000.00 USD | 4,390,000.00 USD | 34,850.00 USD | 9,470.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 18,970.00 USD | 124,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.30` | 4,340,000.00 USD | 4,340,000.00 USD | 53,200.00 USD | 13,130.00 USD | 19,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.30` | 7,560,000.00 USD | 7,560,000.00 USD | 101,900.00 USD | 13,500.00 USD | 47,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.30` | 33,500.00 USD | 105,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.31` | 4,250,000.00 USD | 4,250,000.00 USD | 56,000.00 USD | 11,410.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.31` | 4,550.00 USD | 72,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.32` | 4,180,000.00 USD | 4,180,000.00 USD | 19,380.00 USD | 4,190.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.32` | 7,400,000.00 USD | 7,400,000.00 USD | 61,880.00 USD | 26,020.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 4,150,000.00 USD | 4,150,000.00 USD | 2,970.00 USD | 22,580.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.34` | 4,630.00 USD | 67,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.34` | 4,120,000.00 USD | 4,120,000.00 USD | 14,500.00 USD | 4,810.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.34` | 7,300,000.00 USD | 7,300,000.00 USD | 37,760.00 USD | 15,520.00 USD | 30,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 4,090,000.00 USD | 4,090,000.00 USD | 6,790.00 USD | 11,270.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.36` | 3,410.00 USD | 63,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.36` | 4,060,000.00 USD | 4,060,000.00 USD | 4,390.00 USD | 2,420.00 USD | 21,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.36` | 7,220,000.00 USD | 7,220,000.00 USD | 107,760.00 USD | 13,470.00 USD | 71,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.37` | 7,160.00 USD | 59,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.37` | 4,030,000.00 USD | 4,030,000.00 USD | 21,970.00 USD | 7,980.00 USD | 8,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.38` | 3,410.00 USD | 52,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.38` | 3,990,000.00 USD | 3,990,000.00 USD | 36,140.00 USD | 4,080.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.38` | 7,030,000.00 USD | 7,030,000.00 USD | 143,540.00 USD | 20,560.00 USD | 66,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.38` | 1,870.00 USD | 49,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.39` | 3,920,000.00 USD | 3,920,000.00 USD | 63,440.00 USD | 10,540.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.39` | 1,680.00 USD | 47,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.40` | 3,790,000.00 USD | 3,790,000.00 USD | 67,650.00 USD | 22,890.00 USD | 68,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.40` | 6,800,000.00 USD | 6,800,000.00 USD | 150,350.00 USD | 19,710.00 USD | 220,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.40` | 710.22 USD | 45,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.41` | 3,630,000.00 USD | 3,630,000.00 USD | 33,190.00 USD | 3,620.00 USD | 20,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.41` | 681.03 USD | 44,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.42` | 3,570,000.00 USD | 3,570,000.00 USD | 33,600.00 USD | 12,790.00 USD | 18,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.42` | 6,410,000.00 USD | 6,410,000.00 USD | 178,300.00 USD | 57,340.00 USD | 72,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.43` | 674.00 USD | 44,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.43` | 3,500,000.00 USD | 3,500,000.00 USD | 29,980.00 USD | 34,530.00 USD | 14,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.44` | 188.61 USD | 43,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.44` | 3,430,000.00 USD | 3,430,000.00 USD | 35,570.00 USD | 8,900.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.44` | 6,100,000.00 USD | 6,100,000.00 USD | 155,040.00 USD | 68,350.00 USD | 76,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.45` | 1,470.00 USD | 43,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.45` | 3,380,000.00 USD | 3,380,000.00 USD | 73,020.00 USD | 17,050.00 USD | 49,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.46` | 226.93 USD | 41,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.46` | 3,240,000.00 USD | 3,240,000.00 USD | 153,340.00 USD | 16,420.00 USD | 47,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.46` | 5,800,000.00 USD | 5,800,000.00 USD | 392,550.00 USD | 59,170.00 USD | 107,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.46` | 1,860.00 USD | 41,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.47` | 3,020,000.00 USD | 3,020,000.00 USD | 107,260.00 USD | 30,070.00 USD | 15,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.47` | 12,430.00 USD | 39,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.48` | 2,870,000.00 USD | 2,870,000.00 USD | 126,360.00 USD | 39,180.00 USD | 48,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.48` | 5,240,000.00 USD | 5,240,000.00 USD | 360,640.00 USD | 61,660.00 USD | 220,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.48` | 1,160.00 USD | 27,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.49` | 2,650,000.00 USD | 2,650,000.00 USD | 137,160.00 USD | 36,190.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.49` | 403.51 USD | 26,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.50` | 2,470,000.00 USD | 2,470,000.00 USD | 51,910.00 USD | 11,120.00 USD | 26,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.50` | 4,600,000.00 USD | 4,600,000.00 USD | 191,430.00 USD | 100,070.00 USD | 112,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.51` | 6,380.00 USD | 25,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.51` | 2,380,000.00 USD | 2,380,000.00 USD | 7,460.00 USD | 45,150.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.52` | 7,770.00 USD | 19,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.52` | 2,310,000.00 USD | 2,310,000.00 USD | 48,940.00 USD | 17,250.00 USD | 23,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.52` | 4,190,000.00 USD | 4,190,000.00 USD | 270,540.00 USD | 98,920.00 USD | 250,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.53` | 2,220,000.00 USD | 2,220,000.00 USD | 17,330.00 USD | 29,630.00 USD | 41,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 6,350.00 USD | 11,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.54` | 2,130,000.00 USD | 2,130,000.00 USD | 19,400.00 USD | 6,040.00 USD | 43,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.54` | 3,570,000.00 USD | 3,570,000.00 USD | 379,850.00 USD | 78,380.00 USD | 152,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 1,550.00 USD | 5,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.55` | 2,060,000.00 USD | 2,060,000.00 USD | 64,630.00 USD | 19,250.00 USD | 19,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.55` | 684.40 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.56` | 1,960,000.00 USD | 1,960,000.00 USD | 69,420.00 USD | 12,010.00 USD | 67,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.56` | 2,960,000.00 USD | 2,960,000.00 USD | 593,510.00 USD | 101,070.00 USD | 88,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.57` | 1,810,000.00 USD | 1,810,000.00 USD | 73,460.00 USD | 11,140.00 USD | 73,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.58` | 1,650,000.00 USD | 1,650,000.00 USD | 87,680.00 USD | 21,440.00 USD | 39,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.58` | 2,180,000.00 USD | 2,180,000.00 USD | 541,170.00 USD | 164,810.00 USD | 45,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.59` | 1,500,000.00 USD | 1,500,000.00 USD | 70,460.00 USD | 29,830.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.60` | 1,380,000.00 USD | 1,380,000.00 USD | 68,090.00 USD | 23,230.00 USD | 39,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.60` | 1,430,000.00 USD | 1,430,000.00 USD | 75,040.00 USD | 39,160.00 USD | 206,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.61` | 2,980.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.61` | 1,250,000.00 USD | 1,250,000.00 USD | 35,340.00 USD | 12,770.00 USD | 26,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.62` | 1,170,000.00 USD | 1,170,000.00 USD | 102,610.00 USD | 23,160.00 USD | 30,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.62` | 1,110,000.00 USD | 1,110,000.00 USD | 13,680.00 USD | 43,670.00 USD | 78,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.63` | 1,010,000.00 USD | 1,010,000.00 USD | 77,860.00 USD | 18,340.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.64` | 908,110.00 USD | 908,110.00 USD | 78,760.00 USD | 11,790.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.64` | 971,000.00 USD | 971,000.00 USD | 127,570.00 USD | 5,680.00 USD | 10,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.65` | 806,460.00 USD | 806,460.00 USD | 50,810.00 USD | 31,510.00 USD | 24,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.66` | 699,780.00 USD | 699,780.00 USD | 66,700.00 USD | 26,760.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.66` | 827,110.00 USD | 827,110.00 USD | 55,380.00 USD | 16,520.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.67` | 591,320.00 USD | 591,320.00 USD | 33,710.00 USD | 5,480.00 USD | 23,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.68` | 528,960.00 USD | 528,960.00 USD | 21,030.00 USD | 0.00 USD | 56.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.68` | 717,720.00 USD | 717,720.00 USD | 93,990.00 USD | 24,870.00 USD | 173,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.69` | 507,870.00 USD | 507,870.00 USD | 18,040.00 USD | 5,700.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.70` | 461,960.00 USD | 461,960.00 USD | 34,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.70` | 425,190.00 USD | 425,190.00 USD | 0.00 USD | 12,790.00 USD | 22,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.71` | 427,590.00 USD | 427,590.00 USD | 18,250.00 USD | 11,690.00 USD | 18,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.73` | 378,660.00 USD | 378,660.00 USD | 44,990.00 USD | 2,720.00 USD | 5,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.74` | 325,830.00 USD | 325,830.00 USD | 0.00 USD | 7,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.74` | 390,110.00 USD | 390,110.00 USD | 144,660.00 USD | 19,690.00 USD | 56,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.75` | 318,110.00 USD | 318,110.00 USD | 32,080.00 USD | 8,290.00 USD | 35,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.76` | 241,920.00 USD | 241,920.00 USD | 78,530.00 USD | 15,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.76` | 169,160.00 USD | 169,160.00 USD | 26,810.00 USD | 0.00 USD | 22,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.77` | 148,340.00 USD | 148,340.00 USD | 54,300.00 USD | 8,510.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.78` | 59,810.00 USD | 59,810.00 USD | 19,230.00 USD | 0.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.78` | 119,940.00 USD | 119,940.00 USD | 0.00 USD | 0.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.79` | 30,700.00 USD | 30,700.00 USD | 13,010.00 USD | 12,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.80` | 5,690.00 USD | 5,690.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.80` | 61,100.00 USD | 61,100.00 USD | 27,360.00 USD | 33,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.81` | 10,950.00 USD | 10,950.00 USD | 0.00 USD | 0.00 USD | 10,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.81` | 21,900.00 USD | 21,900.00 USD | 0.00 USD | 0.00 USD | 10,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.82` | 21,290.00 USD | 21,290.00 USD | 0.00 USD | 0.00 USD | 21,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 90,540.00 USD | 90,540.00 USD | 0.00 USD | 0.00 USD | 68,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 157,910.00 USD | 157,910.00 USD | 67,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 235,680.00 USD | 235,680.00 USD | 0.00 USD | 0.00 USD | 77,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.90` | 136,770.00 USD | 136,770.00 USD | 0.00 USD | 0.00 USD | 115,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 247,240.00 USD | 247,240.00 USD | 8,060.00 USD | 0.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.98` | 260,290.00 USD | 260,290.00 USD | 0.00 USD | 5,550.00 USD | 7,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 328,540.00 USD | 328,540.00 USD | 40,450.00 USD | 27,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.00` | 338,640.00 USD | 338,640.00 USD | 10,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.00` | 363,280.00 USD | 363,280.00 USD | 215,150.00 USD | 11,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 350,010.00 USD | 350,010.00 USD | 1,080.00 USD | 5,120.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 416,420.00 USD | 416,420.00 USD | 30,650.00 USD | 30,950.00 USD | 4,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.02` | 454,060.00 USD | 454,060.00 USD | 34,650.00 USD | 56,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 496,860.00 USD | 496,860.00 USD | 29,210.00 USD | 28,060.00 USD | 23,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 508,310.00 USD | 508,310.00 USD | 0.00 USD | 4,810.00 USD | 6,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.04` | 579,990.00 USD | 579,990.00 USD | 36,040.00 USD | 74,750.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 576,610.00 USD | 576,610.00 USD | 3,520.00 USD | 26,530.00 USD | 38,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.06` | 627,940.00 USD | 627,940.00 USD | 27,120.00 USD | 2,420.00 USD | 21,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.06` | 639,700.00 USD | 639,700.00 USD | 5,610.00 USD | 14,960.00 USD | 39,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 691,950.00 USD | 691,950.00 USD | 14,580.00 USD | 22,140.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 733,570.00 USD | 733,570.00 USD | 1,260.00 USD | 6,490.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.08` | 716,750.00 USD | 716,750.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 892,130.00 USD | 892,130.00 USD | 99,950.00 USD | 17,120.00 USD | 41,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.10` | 995,780.00 USD | 995,780.00 USD | 66,840.00 USD | 22,440.00 USD | 14,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.10` | 1,880,000.00 USD | 1,880,000.00 USD | 797,340.00 USD | 35,760.00 USD | 325,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 1,110,000.00 USD | 1,110,000.00 USD | 51,780.00 USD | 9,610.00 USD | 49,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 1,250,000.00 USD | 1,250,000.00 USD | 106,750.00 USD | 31,620.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.12` | 2,870,000.00 USD | 2,870,000.00 USD | 490,020.00 USD | 24,170.00 USD | 479,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 1,400,000.00 USD | 1,400,000.00 USD | 84,020.00 USD | 20,120.00 USD | 40,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.13` | 314.34 USD | 314.34 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.14` | 1,470,000.00 USD | 1,470,000.00 USD | 33,890.00 USD | 8,440.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.14` | 3,900,000.00 USD | 3,900,000.00 USD | 536,560.00 USD | 18,540.00 USD | 479,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.15` | 1,570,000.00 USD | 1,570,000.00 USD | 57,880.00 USD | 22,150.00 USD | 22,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 1,680,000.00 USD | 1,680,000.00 USD | 63,210.00 USD | 17,550.00 USD | 27,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.16` | 4,500,000.00 USD | 4,500,000.00 USD | 358,370.00 USD | 44,360.00 USD | 195,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 1,850,000.00 USD | 1,850,000.00 USD | 94,110.00 USD | 18,740.00 USD | 55,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 2,100,000.00 USD | 2,100,000.00 USD | 151,850.00 USD | 40,170.00 USD | 60,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.18` | 5,480,000.00 USD | 5,480,000.00 USD | 549,130.00 USD | 162,460.00 USD | 263,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 2,250,000.00 USD | 2,250,000.00 USD | 94,190.00 USD | 40,200.00 USD | 17,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.20` | 3,800.00 USD | 4,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.20` | 2,430,000.00 USD | 2,430,000.00 USD | 106,980.00 USD | 10,810.00 USD | 65,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 6,360,000.00 USD | 6,360,000.00 USD | 520,860.00 USD | 120,080.00 USD | 238,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 2,480,000.00 USD | 2,480,000.00 USD | 39,120.00 USD | 3,470.00 USD | 6,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.22` | 2,600,000.00 USD | 2,600,000.00 USD | 93,870.00 USD | 10,040.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.22` | 7,500,000.00 USD | 7,500,000.00 USD | 585,170.00 USD | 140,390.00 USD | 416,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 2,690,000.00 USD | 2,690,000.00 USD | 57,020.00 USD | 3,310.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 2,720,000.00 USD | 2,720,000.00 USD | 31,050.00 USD | 1,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 8,040,000.00 USD | 8,040,000.00 USD | 316,220.00 USD | 52,090.00 USD | 174,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 2,770,000.00 USD | 2,770,000.00 USD | 18,710.00 USD | 17,700.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 2,790,000.00 USD | 2,790,000.00 USD | 16,250.00 USD | 1,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 8,470,000.00 USD | 8,470,000.00 USD | 273,920.00 USD | 96,980.00 USD | 60,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 2,830,000.00 USD | 2,830,000.00 USD | 22,870.00 USD | 13,170.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 2,850,000.00 USD | 2,850,000.00 USD | 20,250.00 USD | 3,860.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 9,180,000.00 USD | 9,180,000.00 USD | 428,160.00 USD | 103,490.00 USD | 170,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 100.93 USD | 4,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.29` | 2,940,000.00 USD | 2,940,000.00 USD | 48,940.00 USD | 15,680.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.30` | 3,010,000.00 USD | 3,010,000.00 USD | 49,420.00 USD | 13,550.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.30` | 9,740,000.00 USD | 9,740,000.00 USD | 199,810.00 USD | 97,780.00 USD | 262,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 3,080,000.00 USD | 3,080,000.00 USD | 39,620.00 USD | 4,250.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 3,100,000.00 USD | 3,100,000.00 USD | 9,610.00 USD | 2,530.00 USD | 10,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.32` | 10,400,000.00 USD | 10,400,000.00 USD | 271,660.00 USD | 59,310.00 USD | 337,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 3,140,000.00 USD | 3,140,000.00 USD | 16,620.00 USD | 6,000.00 USD | 15,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 3,170,000.00 USD | 3,170,000.00 USD | 15,860.00 USD | 4,190.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.34` | 10,730,000.00 USD | 10,730,000.00 USD | 203,440.00 USD | 53,150.00 USD | 70,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.35` | 3,930.00 USD | 8,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.35` | 3,230,000.00 USD | 3,230,000.00 USD | 28,980.00 USD | 3,810.00 USD | 24,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 3,330,000.00 USD | 3,330,000.00 USD | 66,220.00 USD | 13,630.00 USD | 25,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.36` | 11,170,000.00 USD | 11,170,000.00 USD | 247,120.00 USD | 78,550.00 USD | 112,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 3,390,000.00 USD | 3,390,000.00 USD | 36,610.00 USD | 13,410.00 USD | 6,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 3,470,000.00 USD | 3,470,000.00 USD | 47,540.00 USD | 4,040.00 USD | 27,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.38` | 11,690,000.00 USD | 11,690,000.00 USD | 383,530.00 USD | 55,400.00 USD | 85,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.38` | 404,120.00 USD | 412,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.39` | 3,490,000.00 USD | 3,490,000.00 USD | 16,910.00 USD | 1,730.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 3,530,000.00 USD | 3,530,000.00 USD | 44,280.00 USD | 1,210.00 USD | 12.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.40` | 12,140,000.00 USD | 12,140,000.00 USD | 234,760.00 USD | 58,130.00 USD | 153,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 3,580,000.00 USD | 3,580,000.00 USD | 29,700.00 USD | 1,660.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 2,470.00 USD | 414,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 3,600,000.00 USD | 3,600,000.00 USD | 10,620.00 USD | 622.99 USD | 4,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.42` | 12,450,000.00 USD | 12,450,000.00 USD | 176,920.00 USD | 44,410.00 USD | 84,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.43` | 3,630,000.00 USD | 3,630,000.00 USD | 10,390.00 USD | 6,940.00 USD | 12,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 3,630,000.00 USD | 3,630,000.00 USD | 1,500.00 USD | 0.00 USD | 48.84 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 12,560,000.00 USD | 12,560,000.00 USD | 41,250.00 USD | 19,420.00 USD | 56,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 3,640,000.00 USD | 3,640,000.00 USD | 1,380.00 USD | 4,940.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.46` | 3,010.00 USD | 417,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.46` | 3,640,000.00 USD | 3,640,000.00 USD | 1,320.00 USD | 4,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 12,750,000.00 USD | 12,750,000.00 USD | 136,670.00 USD | 29,830.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.47` | 3,670,000.00 USD | 3,670,000.00 USD | 18,220.00 USD | 6,870.00 USD | 192.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.48` | 3,680,000.00 USD | 3,680,000.00 USD | 1,510.00 USD | 0.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.48` | 12,820,000.00 USD | 12,820,000.00 USD | 12,180.00 USD | 30,160.00 USD | 25,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 3,700,000.00 USD | 3,700,000.00 USD | 21,080.00 USD | 572.85 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.50` | 3,720,000.00 USD | 3,720,000.00 USD | 11,990.00 USD | 3,160.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 13,000,000.00 USD | 13,000,000.00 USD | 69,270.00 USD | 33,210.00 USD | 83,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.51` | 3,730,000.00 USD | 3,730,000.00 USD | 295.05 USD | 0.00 USD | 124.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.52` | 3,750,000.00 USD | 3,750,000.00 USD | 17,180.00 USD | 3,070.00 USD | 5,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 13,190,000.00 USD | 13,190,000.00 USD | 102,150.00 USD | 29,320.00 USD | 51,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.53` | 3,770,000.00 USD | 3,770,000.00 USD | 18,780.00 USD | 4,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.54` | 3,780,000.00 USD | 3,780,000.00 USD | 5,910.00 USD | 1,470.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 13,410,000.00 USD | 13,410,000.00 USD | 192,090.00 USD | 27,650.00 USD | 930.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.55` | 3,800,000.00 USD | 3,800,000.00 USD | 2,910.00 USD | 6,330.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.56` | 3,810,000.00 USD | 3,810,000.00 USD | 5,060.00 USD | 1,280.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 13,530,000.00 USD | 13,530,000.00 USD | 89,210.00 USD | 5,260.00 USD | 32,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.57` | 3,820,000.00 USD | 3,820,000.00 USD | 1,370.00 USD | 3,100.00 USD | 4,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.58` | 3,820,000.00 USD | 3,820,000.00 USD | 1,290.00 USD | 563.17 USD | 7,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 13,610,000.00 USD | 13,610,000.00 USD | 35,340.00 USD | 16,980.00 USD | 21,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.59` | 3,830,000.00 USD | 3,830,000.00 USD | 5,050.00 USD | 1,250.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.60` | 3,860,000.00 USD | 3,860,000.00 USD | 11,210.00 USD | 424.36 USD | 11,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 13,690,000.00 USD | 13,690,000.00 USD | 38,740.00 USD | 10,820.00 USD | 33,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.61` | 3,880,000.00 USD | 3,880,000.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.62` | 3,880,000.00 USD | 3,880,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 13,790,000.00 USD | 13,790,000.00 USD | 70,470.00 USD | 13,850.00 USD | 17,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.63` | 3,900,000.00 USD | 3,900,000.00 USD | 10,190.00 USD | 4,370.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.64` | 3,910,000.00 USD | 3,910,000.00 USD | 5,830.00 USD | 0.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.64` | 13,890,000.00 USD | 13,890,000.00 USD | 61,870.00 USD | 17,650.00 USD | 19,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.65` | 3,920,000.00 USD | 3,920,000.00 USD | 5,960.00 USD | 4,150.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.66` | 3,940,000.00 USD | 3,940,000.00 USD | 8,930.00 USD | 3,480.00 USD | 5,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.66` | 13,970,000.00 USD | 13,970,000.00 USD | 37,340.00 USD | 21,280.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.67` | 3,940,000.00 USD | 3,940,000.00 USD | 2,990.00 USD | 0.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.68` | 3,960,000.00 USD | 3,960,000.00 USD | 13,160.00 USD | 2,950.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.68` | 14,090,000.00 USD | 14,090,000.00 USD | 68,230.00 USD | 20,310.00 USD | 34,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.69` | 3,980,000.00 USD | 3,980,000.00 USD | 7,960.00 USD | 2,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.70` | 3,990,000.00 USD | 3,990,000.00 USD | 7,590.00 USD | 4,150.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.70` | 14,220,000.00 USD | 14,220,000.00 USD | 79,760.00 USD | 12,990.00 USD | 31,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.71` | 4,000,000.00 USD | 4,000,000.00 USD | 74.90 USD | 5,170.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.72` | 4,000,000.00 USD | 4,000,000.00 USD | 2,760.00 USD | 3,170.00 USD | 57.27 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.72` | 14,320,000.00 USD | 14,320,000.00 USD | 71,790.00 USD | 6,920.00 USD | 26,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 417,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.74` | 4,010,000.00 USD | 4,010,000.00 USD | 5,250.00 USD | 0.00 USD | 2,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.74` | 14,360,000.00 USD | 14,360,000.00 USD | 10,330.00 USD | 7,200.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.75` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 42.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.76` | 4,020,000.00 USD | 4,020,000.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.76` | 14,460,000.00 USD | 14,460,000.00 USD | 35,520.00 USD | 12,480.00 USD | 52,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.78` | 4,020,000.00 USD | 4,020,000.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.78` | 14,540,000.00 USD | 14,540,000.00 USD | 65,390.00 USD | 10,300.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.79` | 4,030,000.00 USD | 4,030,000.00 USD | 5,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.79` | 551.36 USD | 418,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.80` | 4,040,000.00 USD | 4,040,000.00 USD | 6,870.00 USD | 770.83 USD | 9.39 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.80` | 14,600,000.00 USD | 14,600,000.00 USD | 18,630.00 USD | 28,440.00 USD | 10,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.81` | 4,050,000.00 USD | 4,050,000.00 USD | 8,600.00 USD | 1,540.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.81` | 472.10 USD | 418,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.82` | 4,060,000.00 USD | 4,060,000.00 USD | 7,220.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.82` | 14,830,000.00 USD | 14,830,000.00 USD | 121,860.00 USD | 27,860.00 USD | 86,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.83` | 4,090,000.00 USD | 4,090,000.00 USD | 16,240.00 USD | 4,800.00 USD | 1,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.84` | 14,860,000.00 USD | 14,860,000.00 USD | 9,730.00 USD | 7,850.00 USD | 14,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.85` | 4,100,000.00 USD | 4,100,000.00 USD | 10,690.00 USD | 1,700.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.86` | 15,000,000.00 USD | 15,000,000.00 USD | 59,550.00 USD | 2,210.00 USD | 72,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.88` | 15,040,000.00 USD | 15,040,000.00 USD | 7,900.00 USD | 8,710.00 USD | 20,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.90` | 15,130,000.00 USD | 15,130,000.00 USD | 55,970.00 USD | 19,700.00 USD | 14,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.92` | 15,170,000.00 USD | 15,170,000.00 USD | 27,710.00 USD | 10,810.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.94` | 15,290,000.00 USD | 15,290,000.00 USD | 69,320.00 USD | 11,150.00 USD | 39,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.96` | 15,340,000.00 USD | 15,340,000.00 USD | 29,800.00 USD | 1,360.00 USD | 11,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.98` | 15,360,000.00 USD | 15,360,000.00 USD | 840.10 USD | 4,150.00 USD | 18,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.00` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 6,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.02` | 15,390,000.00 USD | 15,390,000.00 USD | 15,960.00 USD | 0.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.09` | 113.76 USD | 419,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.15` | 22,320.00 USD | 441,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.21` | 7,330.00 USD | 448,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.23` | 114.12 USD | 448,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 3,380.00 USD | 452,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 452,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.70` | 37,030.00 USD | 489,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.71` | 218.91 USD | 489,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.96` | 1,920.00 USD | 491,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 498,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,810.00 USD | 510,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.47` | 720.29 USD | 511,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 523,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.70` | 778.89 USD | 524,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.81` | 59,080.00 USD | 583,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.04` | 1,370.00 USD | 584,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 586,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 586,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.68` | 432.22 USD | 587,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.76` | 36,730.00 USD | 624,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.79` | 953.38 USD | 624,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.96` | 102.68 USD | 625,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.97` | 14,530.00 USD | 639,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 727,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 234,840.00 USD | 962,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 966,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 966,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 966,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.14` | 164.79 USD | 966,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.43` | 4,000.00 USD | 970,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.62` | 288.35 USD | 971,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 972,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.84` | 243.44 USD | 972,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.86` | 2,470.00 USD | 974,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 322.06 USD | 975,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 975,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 975,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 995,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.49` | 154,950.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.74` | 111.95 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.29` | 263,950.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.46` | 22,620.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 84,520.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.77` | 340.87 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.02` | 191.87 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.14` | 1,710.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.46` | 101.47 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.62` | 4,120.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.64` | 4,930.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.66` | 2,660.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.85` | 2,320,000.00 USD | 0.00 USD | 204.05 USD | `-79.01%` | `110.00` |
| `Live` | `Long` | `1.93` | 2,320,000.00 USD | 0.00 USD | 481.25 USD | `-78.22%` | `250.00` |
| `Live` | `Long` | `2.00` | 2,320,000.00 USD | 0.00 USD | 159.60 USD | `-77.43%` | `80.00` |
| `Live` | `Long` | `2.00` | 2,320,000.00 USD | 0.00 USD | 104.26 USD | `-77.31%` | `52.00` |
| `Live` | `Long` | `2.04` | 2,320,000.00 USD | 0.00 USD | 110.52 USD | `-76.97%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,320,000.00 USD | 0.00 USD | 4,920.00 USD | `-76.64%` | `2,382.76` |
| `Live` | `Long` | `2.31` | 2,310,000.00 USD | 0.00 USD | 375.35 USD | `-73.92%` | `162.84` |
| `Live` | `Long` | `2.33` | 2,310,000.00 USD | 0.00 USD | 2,170.00 USD | `-73.58%` | `929.47` |
| `Live` | `Long` | `2.38` | 2,310,000.00 USD | 0.00 USD | 290.37 USD | `-73.01%` | `121.75` |
| `Live` | `Long` | `2.42` | 2,310,000.00 USD | 0.00 USD | 265.65 USD | `-72.68%` | `110.00` |
| `Live` | `Long` | `2.42` | 2,310,000.00 USD | 0.00 USD | 814.80 USD | `-72.56%` | `336.00` |
| `Live` | `Long` | `2.48` | 2,310,000.00 USD | 0.00 USD | 17,370.00 USD | `-71.88%` | `6,990.57` |
| `Live` | `Long` | `2.58` | 2,290,000.00 USD | 0.00 USD | 109.88 USD | `-70.87%` | `42.67` |
| `Live` | `Long` | `2.69` | 2,290,000.00 USD | 0.00 USD | 133.73 USD | `-69.51%` | `49.62` |
| `Live` | `Long` | `2.87` | 2,290,000.00 USD | 0.00 USD | 232.67 USD | `-67.58%` | `81.21` |
| `Live` | `Long` | `2.94` | 2,290,000.00 USD | 0.00 USD | 45,470.00 USD | `-66.79%` | `15,492.38` |
| `Live` | `Long` | `2.98` | 2,250,000.00 USD | 0.00 USD | 111.12 USD | `-66.34%` | `37.35` |
| `Live` | `Long` | `2.98` | 2,250,000.00 USD | 0.00 USD | 1,130.00 USD | `-66.23%` | `377.71` |
| `Live` | `Long` | `3.10` | 2,250,000.00 USD | 0.00 USD | 1,460.00 USD | `-64.98%` | `470.82` |
| `Live` | `Long` | `3.23` | 2,240,000.00 USD | 0.00 USD | 404.38 USD | `-63.40%` | `125.00` |
| `Live` | `Long` | `3.37` | 2,240,000.00 USD | 0.00 USD | 389.53 USD | `-61.93%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,240,000.00 USD | 0.00 USD | 151.88 USD | `-61.81%` | `45.00` |
| `Live` | `Long` | `3.40` | 2,240,000.00 USD | 0.00 USD | 114.82 USD | `-61.47%` | `33.72` |
| `Live` | `Long` | `3.54` | 2,240,000.00 USD | 0.00 USD | 152.25 USD | `-60.00%` | `43.07` |
| `Live` | `Long` | `3.60` | 2,240,000.00 USD | 0.00 USD | 775.18 USD | `-59.21%` | `215.03` |
| `Live` | `Long` | `3.67` | 2,240,000.00 USD | 0.00 USD | 109.95 USD | `-58.53%` | `30.00` |
| `Live` | `Long` | `3.75` | 2,240,000.00 USD | 0.00 USD | 1,500.00 USD | `-57.51%` | `400.00` |
| `Live` | `Long` | `3.85` | 2,240,000.00 USD | 0.00 USD | 341.01 USD | `-56.38%` | `88.46` |
| `Live` | `Long` | `3.90` | 2,240,000.00 USD | 0.00 USD | 131.73 USD | `-55.93%` | `33.82` |
| `Live` | `Long` | `3.98` | 2,240,000.00 USD | 0.00 USD | 371.88 USD | `-54.91%` | `93.32` |
| `Live` | `Long` | `4.03` | 2,240,000.00 USD | 0.00 USD | 402.70 USD | `-54.46%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,240,000.00 USD | 0.00 USD | 152.29 USD | `-54.23%` | `37.65` |
| `Live` | `Long` | `4.08` | 2,240,000.00 USD | 0.00 USD | 9,290.00 USD | `-53.78%` | `2,273.34` |
| `Live` | `Long` | `4.14` | 2,230,000.00 USD | 0.00 USD | 1,130.00 USD | `-53.10%` | `272.03` |
| `Live` | `Long` | `4.18` | 2,230,000.00 USD | 0.00 USD | 174.89 USD | `-52.65%` | `41.79` |
| `Live` | `Long` | `4.20` | 2,230,000.00 USD | 0.00 USD | 419.50 USD | `-52.54%` | `100.00` |
| `Live` | `Long` | `4.24` | 2,230,000.00 USD | 0.00 USD | 169.40 USD | `-52.08%` | `40.00` |
| `Live` | `Long` | `4.29` | 2,230,000.00 USD | 0.00 USD | 2,440.00 USD | `-51.52%` | `568.43` |
| `Live` | `Long` | `4.30` | 2,230,000.00 USD | 0.00 USD | 174.83 USD | `-51.29%` | `40.61` |
| `Live` | `Long` | `4.32` | 2,230,000.00 USD | 0.00 USD | 852.47 USD | `-51.18%` | `197.56` |
| `Live` | `Long` | `4.33` | 2,220,000.00 USD | 0.00 USD | 2,190.00 USD | `-50.95%` | `504.56` |
| `Live` | `Long` | `4.37` | 2,220,000.00 USD | 0.00 USD | 117.86 USD | `-50.61%` | `27.00` |
| `Live` | `Long` | `4.51` | 2,220,000.00 USD | 0.00 USD | 217.71 USD | `-48.91%` | `48.22` |
| `Live` | `Long` | `4.59` | 2,220,000.00 USD | 0.00 USD | 30,970.00 USD | `-48.01%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,190,000.00 USD | 0.00 USD | 486.93 USD | `-47.78%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,190,000.00 USD | 0.00 USD | 2,680.00 USD | `-47.67%` | `579.06` |
| `Live` | `Long` | `4.66` | 2,190,000.00 USD | 0.00 USD | 105.11 USD | `-47.33%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,190,000.00 USD | 0.00 USD | 3,280.00 USD | `-47.22%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,180,000.00 USD | 0.00 USD | 1,490.00 USD | `-47.10%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,180,000.00 USD | 0.00 USD | 8,490.00 USD | `-46.99%` | `1,812.97` |
| `Live` | `Long` | `4.70` | 2,170,000.00 USD | 0.00 USD | 7,730.00 USD | `-46.88%` | `1,645.98` |
| `Live` | `Long` | `4.75` | 2,170,000.00 USD | 0.00 USD | 240.48 USD | `-46.31%` | `50.68` |
| `Live` | `Long` | `4.76` | 2,170,000.00 USD | 0.00 USD | 105.64 USD | `-46.09%` | `22.17` |
| `Live` | `Long` | `4.80` | 2,170,000.00 USD | 0.00 USD | 15,790.00 USD | `-45.63%` | `3,286.00` |
| `Live` | `Long` | `4.83` | 2,150,000.00 USD | 0.00 USD | 6,380.00 USD | `-45.41%` | `1,323.00` |
| `Live` | `Long` | `4.83` | 2,140,000.00 USD | 0.00 USD | 467.01 USD | `-45.29%` | `96.59` |
| `Live` | `Long` | `4.89` | 2,140,000.00 USD | 0.00 USD | 146.85 USD | `-44.62%` | `30.00` |
| `Live` | `Long` | `4.91` | 2,140,000.00 USD | 0.00 USD | 527.19 USD | `-44.50%` | `107.48` |
| `Live` | `Long` | `4.92` | 2,140,000.00 USD | 0.00 USD | 1,350.00 USD | `-44.39%` | `274.20` |
| `Live` | `Long` | `4.96` | 2,140,000.00 USD | 0.00 USD | 945.36 USD | `-43.94%` | `190.79` |
| `Live` | `Long` | `4.97` | 2,140,000.00 USD | 0.00 USD | 282.23 USD | `-43.71%` | `56.73` |
| `Live` | `Long` | `4.99` | 2,140,000.00 USD | 0.00 USD | 329.11 USD | `-43.60%` | `66.02` |
| `Live` | `Long` | `5.01` | 2,140,000.00 USD | 0.00 USD | 56,390.00 USD | `-43.26%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,080,000.00 USD | 0.00 USD | 167.78 USD | `-43.14%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,080,000.00 USD | 0.00 USD | 314.59 USD | `-43.03%` | `62.48` |
| `Live` | `Long` | `5.05` | 2,080,000.00 USD | 0.00 USD | 504.74 USD | `-42.81%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,080,000.00 USD | 0.00 USD | 318.46 USD | `-42.58%` | `62.75` |
| `Live` | `Long` | `5.09` | 2,080,000.00 USD | 0.00 USD | 4,690.00 USD | `-42.35%` | `920.67` |
| `Live` | `Long` | `5.12` | 2,080,000.00 USD | 0.00 USD | 250.20 USD | `-42.01%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,080,000.00 USD | 0.00 USD | 396.06 USD | `-41.90%` | `77.13` |
| `Live` | `Long` | `5.16` | 2,080,000.00 USD | 0.00 USD | 156,890.00 USD | `-41.67%` | `30,435.20` |
| `Live` | `Long` | `5.17` | 1,920,000.00 USD | 0.00 USD | 2,300.00 USD | `-41.56%` | `445.16` |
| `Live` | `Long` | `5.17` | 1,920,000.00 USD | 0.00 USD | 1,620.00 USD | `-41.45%` | `312.94` |
| `Live` | `Long` | `5.18` | 1,920,000.00 USD | 0.00 USD | 150.57 USD | `-41.33%` | `29.04` |
| `Live` | `Long` | `5.21` | 1,920,000.00 USD | 0.00 USD | 300.91 USD | `-40.99%` | `57.70` |
| `Live` | `Long` | `5.29` | 1,920,000.00 USD | 0.00 USD | 640.70 USD | `-40.20%` | `121.23` |
| `Live` | `Long` | `5.32` | 1,920,000.00 USD | 0.00 USD | 232.85 USD | `-39.86%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,910,000.00 USD | 0.00 USD | 716.11 USD | `-39.75%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,910,000.00 USD | 0.00 USD | 660.46 USD | `-38.96%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,910,000.00 USD | 0.00 USD | 21,080.00 USD | `-38.73%` | `3,892.05` |
| `Live` | `Long` | `5.42` | 1,890,000.00 USD | 0.00 USD | 163,110.00 USD | `-38.62%` | `30,067.25` |
| `Live` | `Long` | `5.43` | 1,730,000.00 USD | 0.00 USD | 1,360.00 USD | `-38.51%` | `250.00` |
| `Live` | `Long` | `5.46` | 1,730,000.00 USD | 0.00 USD | 264.72 USD | `-38.17%` | `48.44` |
| `Live` | `Long` | `5.49` | 1,730,000.00 USD | 0.00 USD | 354.06 USD | `-37.94%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,730,000.00 USD | 0.00 USD | 19,290.00 USD | `-37.83%` | `3,510.41` |
| `Live` | `Long` | `5.51` | 1,710,000.00 USD | 0.00 USD | 367.41 USD | `-37.60%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,710,000.00 USD | 0.00 USD | 121.38 USD | `-37.37%` | `21.93` |
| `Live` | `Long` | `5.57` | 1,710,000.00 USD | 0.00 USD | 967.98 USD | `-37.03%` | `173.94` |
| `Live` | `Long` | `5.58` | 1,710,000.00 USD | 0.00 USD | 63,260.00 USD | `-36.92%` | `11,347.58` |
| `Live` | `Long` | `5.59` | 1,640,000.00 USD | 0.00 USD | 34,430.00 USD | `-36.70%` | `6,153.60` |
| `Live` | `Long` | `5.63` | 1,610,000.00 USD | 0.00 USD | 22,270.00 USD | `-36.24%` | `3,952.96` |
| `Live` | `Long` | `5.66` | 1,590,000.00 USD | 0.00 USD | 4,160.00 USD | `-36.02%` | `734.88` |
| `Live` | `Long` | `5.70` | 1,580,000.00 USD | 0.00 USD | 405.03 USD | `-35.56%` | `71.12` |
| `Live` | `Long` | `5.71` | 1,580,000.00 USD | 0.00 USD | 2,340.00 USD | `-35.45%` | `409.39` |
| `Live` | `Long` | `5.74` | 1,580,000.00 USD | 0.00 USD | 238.86 USD | `-35.11%` | `41.65` |
| `Live` | `Long` | `5.75` | 1,580,000.00 USD | 0.00 USD | 125.70 USD | `-35.00%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,580,000.00 USD | 0.00 USD | 3,190.00 USD | `-34.88%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,580,000.00 USD | 0.00 USD | 10,850.00 USD | `-34.77%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,570,000.00 USD | 0.00 USD | 801.40 USD | `-34.66%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,560,000.00 USD | 0.00 USD | 2,890.00 USD | `-34.55%` | `500.00` |
| `Live` | `Long` | `5.79` | 1,560,000.00 USD | 0.00 USD | 736.72 USD | `-34.43%` | `127.13` |
| `Live` | `Long` | `5.80` | 1,560,000.00 USD | 0.00 USD | 580.50 USD | `-34.32%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,560,000.00 USD | 0.00 USD | 106.65 USD | `-34.21%` | `18.34` |
| `Live` | `Long` | `5.88` | 1,560,000.00 USD | 0.00 USD | 329,350.00 USD | `-33.53%` | `56,059.40` |
| `Live` | `Long` | `5.89` | 1,230,000.00 USD | 0.00 USD | 640.67 USD | `-33.30%` | `108.68` |
| `Live` | `Long` | `5.91` | 1,230,000.00 USD | 0.00 USD | 399.18 USD | `-33.19%` | `67.60` |
| `Live` | `Long` | `5.96` | 1,230,000.00 USD | 0.00 USD | 12,380.00 USD | `-32.62%` | `2,078.19` |
| `Live` | `Long` | `5.97` | 1,220,000.00 USD | 0.00 USD | 585.97 USD | `-32.40%` | `98.07` |
| `Live` | `Long` | `5.99` | 1,220,000.00 USD | 0.00 USD | 447.98 USD | `-32.28%` | `74.85` |
| `Live` | `Long` | `6.00` | 1,220,000.00 USD | 0.00 USD | 341.56 USD | `-32.06%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,220,000.00 USD | 0.00 USD | 446.85 USD | `-31.94%` | `74.29` |
| `Live` | `Long` | `6.03` | 1,220,000.00 USD | 0.00 USD | 404.46 USD | `-31.83%` | `67.13` |
| `Live` | `Long` | `6.04` | 1,220,000.00 USD | 0.00 USD | 331.68 USD | `-31.72%` | `54.96` |
| `Live` | `Long` | `6.04` | 1,210,000.00 USD | 0.00 USD | 448.72 USD | `-31.60%` | `74.23` |
| `Live` | `Long` | `6.05` | 1,210,000.00 USD | 0.00 USD | 1,310.00 USD | `-31.49%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,210,000.00 USD | 0.00 USD | 1,630.00 USD | `-31.38%` | `268.85` |
| `Live` | `Long` | `6.08` | 1,210,000.00 USD | 0.00 USD | 1,690.00 USD | `-31.26%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,210,000.00 USD | 0.00 USD | 405.14 USD | `-31.15%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,210,000.00 USD | 0.00 USD | 3,550.00 USD | `-31.04%` | `582.81` |
| `Live` | `Long` | `6.11` | 1,210,000.00 USD | 0.00 USD | 3,200.00 USD | `-30.92%` | `524.73` |
| `Live` | `Long` | `6.12` | 1,200,000.00 USD | 0.00 USD | 137.02 USD | `-30.70%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,200,000.00 USD | 0.00 USD | 2,370.00 USD | `-30.59%` | `386.46` |
| `Live` | `Long` | `6.14` | 1,200,000.00 USD | 0.00 USD | 238.61 USD | `-30.47%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,200,000.00 USD | 0.00 USD | 4,390.00 USD | `-30.36%` | `713.75` |
| `Live` | `Long` | `6.17` | 1,200,000.00 USD | 0.00 USD | 187.29 USD | `-30.25%` | `30.38` |
| `Live` | `Long` | `6.17` | 1,200,000.00 USD | 0.00 USD | 104.36 USD | `-30.13%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,200,000.00 USD | 0.00 USD | 310.25 USD | `-29.79%` | `50.00` |
| `Live` | `Long` | `6.21` | 1,190,000.00 USD | 0.00 USD | 2,560.00 USD | `-29.68%` | `411.30` |
| `Live` | `Long` | `6.22` | 1,190,000.00 USD | 0.00 USD | 715.31 USD | `-29.57%` | `114.91` |
| `Live` | `Long` | `6.25` | 1,190,000.00 USD | 0.00 USD | 972.65 USD | `-29.23%` | `155.50` |
| `Live` | `Long` | `6.28` | 1,190,000.00 USD | 0.00 USD | 2,510.00 USD | `-29.00%` | `400.00` |
| `Live` | `Long` | `6.29` | 1,190,000.00 USD | 0.00 USD | 1,610.00 USD | `-28.89%` | `255.64` |
| `Live` | `Long` | `6.32` | 1,190,000.00 USD | 0.00 USD | 277.04 USD | `-28.55%` | `43.87` |
| `Live` | `Long` | `6.33` | 1,190,000.00 USD | 0.00 USD | 105.25 USD | `-28.44%` | `16.64` |
| `Live` | `Long` | `6.36` | 1,190,000.00 USD | 0.00 USD | 4,470.00 USD | `-28.10%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,180,000.00 USD | 0.00 USD | 284,770.00 USD | `-27.98%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 896,880.00 USD | 0.00 USD | 5,110.00 USD | `-27.87%` | `801.31` |
| `Live` | `Long` | `6.41` | 891,770.00 USD | 0.00 USD | 1,640.00 USD | `-27.53%` | `256.20` |
| `Live` | `Long` | `6.42` | 890,130.00 USD | 0.00 USD | 306.32 USD | `-27.42%` | `47.75` |
| `Live` | `Long` | `6.43` | 889,830.00 USD | 0.00 USD | 6,780.00 USD | `-27.19%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 883,050.00 USD | 0.00 USD | 1,050.00 USD | `-26.85%` | `162.75` |
| `Live` | `Long` | `6.50` | 882,000.00 USD | 0.00 USD | 1,720.00 USD | `-26.51%` | `265.15` |
| `Live` | `Long` | `6.54` | 880,280.00 USD | 0.00 USD | 3,620.00 USD | `-26.06%` | `554.55` |
| `Live` | `Long` | `6.54` | 876,650.00 USD | 0.00 USD | 8,970.00 USD | `-25.95%` | `1,370.89` |
| `Live` | `Long` | `6.58` | 867,680.00 USD | 0.00 USD | 2,170.00 USD | `-25.61%` | `330.00` |
| `Live` | `Long` | `6.58` | 865,510.00 USD | 0.00 USD | 1,100.00 USD | `-25.49%` | `166.55` |
| `Live` | `Long` | `6.62` | 864,410.00 USD | 0.00 USD | 2,110.00 USD | `-25.15%` | `318.57` |
| `Live` | `Long` | `6.70` | 862,310.00 USD | 0.00 USD | 506.54 USD | `-24.25%` | `75.66` |
| `Live` | `Long` | `6.71` | 861,800.00 USD | 0.00 USD | 16,610.00 USD | `-24.14%` | `2,477.79` |
| `Live` | `Long` | `6.75` | 845,190.00 USD | 0.00 USD | 1,330.00 USD | `-23.68%` | `196.95` |
| `Live` | `Long` | `6.78` | 843,860.00 USD | 0.00 USD | 6,780.00 USD | `-23.34%` | `1,000.00` |
| `Live` | `Long` | `6.79` | 837,080.00 USD | 0.00 USD | 16,960.00 USD | `-23.23%` | `2,500.00` |
| `Live` | `Long` | `6.79` | 820,120.00 USD | 0.00 USD | 4,260.00 USD | `-23.12%` | `626.24` |
| `Live` | `Long` | `6.80` | 815,870.00 USD | 0.00 USD | 1,500.00 USD | `-23.00%` | `220.95` |
| `Live` | `Long` | `6.82` | 814,360.00 USD | 0.00 USD | 2,670.00 USD | `-22.89%` | `391.11` |
| `Live` | `Long` | `6.83` | 811,700.00 USD | 0.00 USD | 158.14 USD | `-22.78%` | `23.17` |
| `Live` | `Long` | `6.83` | 811,540.00 USD | 0.00 USD | 4,830.00 USD | `-22.67%` | `706.73` |
| `Live` | `Long` | `6.86` | 806,710.00 USD | 0.00 USD | 18,930.00 USD | `-22.44%` | `2,761.63` |
| `Live` | `Long` | `6.87` | 787,780.00 USD | 0.00 USD | 3,340.00 USD | `-22.33%` | `486.46` |
| `Live` | `Long` | `6.89` | 784,440.00 USD | 0.00 USD | 5,250.00 USD | `-21.99%` | `761.63` |
| `Live` | `Long` | `6.91` | 779,190.00 USD | 0.00 USD | 269.30 USD | `-21.87%` | `39.00` |
| `Live` | `Long` | `6.92` | 778,920.00 USD | 0.00 USD | 1,510.00 USD | `-21.76%` | `217.70` |
| `Live` | `Long` | `6.95` | 777,410.00 USD | 0.00 USD | 3,760.00 USD | `-21.42%` | `541.68` |
| `Live` | `Long` | `6.96` | 773,650.00 USD | 0.00 USD | 3,480.00 USD | `-21.31%` | `500.00` |
| `Live` | `Long` | `6.96` | 770,170.00 USD | 0.00 USD | 28,500.00 USD | `-21.19%` | `4,091.42` |
| `Live` | `Long` | `6.99` | 741,680.00 USD | 0.00 USD | 1,400.00 USD | `-20.97%` | `200.00` |
| `Live` | `Long` | `7.00` | 740,280.00 USD | 0.00 USD | 1,550.00 USD | `-20.85%` | `222.06` |
| `Live` | `Long` | `7.00` | 738,730.00 USD | 0.00 USD | 24,240.00 USD | `-20.74%` | `3,460.54` |
| `Live` | `Long` | `7.04` | 714,480.00 USD | 0.00 USD | 4,100.00 USD | `-20.29%` | `581.44` |
| `Live` | `Long` | `7.08` | 710,390.00 USD | 0.00 USD | 6,700.00 USD | `-19.95%` | `947.44` |
| `Live` | `Long` | `7.08` | 703,680.00 USD | 0.00 USD | 1,670.00 USD | `-19.84%` | `236.20` |
| `Live` | `Long` | `7.11` | 702,010.00 USD | 0.00 USD | 28,230.00 USD | `-19.61%` | `3,972.61` |
| `Live` | `Long` | `7.12` | 673,790.00 USD | 0.00 USD | 379.66 USD | `-19.50%` | `53.36` |
| `Live` | `Long` | `7.13` | 673,410.00 USD | 0.00 USD | 2,300.00 USD | `-19.27%` | `322.72` |
| `Live` | `Long` | `7.14` | 671,100.00 USD | 0.00 USD | 20,950.00 USD | `-19.16%` | `2,931.56` |
| `Live` | `Long` | `7.16` | 650,160.00 USD | 0.00 USD | 1,630.00 USD | `-19.04%` | `228.41` |
| `Live` | `Long` | `7.18` | 648,520.00 USD | 0.00 USD | 1,440.00 USD | `-18.71%` | `200.00` |
| `Live` | `Long` | `7.21` | 647,090.00 USD | 0.00 USD | 581.02 USD | `-18.37%` | `80.53` |
| `Live` | `Long` | `7.24` | 646,510.00 USD | 0.00 USD | 179.65 USD | `-18.14%` | `24.83` |
| `Live` | `Long` | `7.25` | 646,330.00 USD | 0.00 USD | 185.83 USD | `-18.03%` | `25.65` |
| `Live` | `Long` | `7.29` | 646,140.00 USD | 0.00 USD | 36,560.00 USD | `-17.57%` | `5,019.00` |
| `Live` | `Long` | `7.29` | 609,580.00 USD | 0.00 USD | 19,790.00 USD | `-17.46%` | `2,712.69` |
| `Live` | `Long` | `7.32` | 589,790.00 USD | 0.00 USD | 168.76 USD | `-17.23%` | `23.07` |
| `Live` | `Long` | `7.33` | 589,620.00 USD | 0.00 USD | 4,910.00 USD | `-17.12%` | `669.93` |
| `Live` | `Long` | `7.33` | 584,710.00 USD | 0.00 USD | 2,450.00 USD | `-17.01%` | `333.54` |
| `Live` | `Long` | `7.34` | 582,260.00 USD | 0.00 USD | 4,370.00 USD | `-16.89%` | `594.84` |
| `Live` | `Long` | `7.37` | 577,900.00 USD | 0.00 USD | 5,720.00 USD | `-16.67%` | `776.95` |
| `Live` | `Long` | `7.38` | 572,170.00 USD | 0.00 USD | 3,920.00 USD | `-16.56%` | `531.65` |
| `Live` | `Long` | `7.38` | 568,250.00 USD | 0.00 USD | 17,770.00 USD | `-16.44%` | `2,406.10` |
| `Live` | `Long` | `7.39` | 550,480.00 USD | 0.00 USD | 1,550.00 USD | `-16.33%` | `210.17` |
| `Live` | `Long` | `7.42` | 548,930.00 USD | 0.00 USD | 1,540.00 USD | `-15.99%` | `207.34` |
| `Live` | `Long` | `7.45` | 547,390.00 USD | 0.00 USD | 1,700.00 USD | `-15.76%` | `228.34` |
| `Live` | `Long` | `7.46` | 545,690.00 USD | 0.00 USD | 1,370.00 USD | `-15.65%` | `183.84` |
| `Live` | `Long` | `7.46` | 544,320.00 USD | 0.00 USD | 5,430.00 USD | `-15.54%` | `727.40` |
| `Live` | `Long` | `7.47` | 538,890.00 USD | 0.00 USD | 3,210.00 USD | `-15.42%` | `430.09` |
| `Live` | `Long` | `7.50` | 535,670.00 USD | 0.00 USD | 1,580.00 USD | `-15.20%` | `211.22` |
| `Live` | `Long` | `7.50` | 534,090.00 USD | 0.00 USD | 1,080.00 USD | `-15.08%` | `143.74` |
| `Live` | `Long` | `7.53` | 533,010.00 USD | 0.00 USD | 995.86 USD | `-14.86%` | `132.34` |
| `Live` | `Long` | `7.54` | 532,020.00 USD | 0.00 USD | 4,210.00 USD | `-14.75%` | `559.01` |
| `Live` | `Long` | `7.55` | 527,800.00 USD | 0.00 USD | 157.14 USD | `-14.52%` | `20.80` |
| `Live` | `Long` | `7.57` | 527,650.00 USD | 0.00 USD | 118.09 USD | `-14.41%` | `15.61` |
| `Live` | `Long` | `7.58` | 527,530.00 USD | 0.00 USD | 4,260.00 USD | `-14.29%` | `562.89` |
| `Live` | `Long` | `7.59` | 523,270.00 USD | 0.00 USD | 25,140.00 USD | `-14.07%` | `3,310.14` |
| `Live` | `Long` | `7.62` | 498,120.00 USD | 0.00 USD | 312.22 USD | `-13.84%` | `41.00` |
| `Live` | `Long` | `7.62` | 497,810.00 USD | 0.00 USD | 787.51 USD | `-13.73%` | `103.28` |
| `Live` | `Long` | `7.63` | 497,030.00 USD | 0.00 USD | 514.52 USD | `-13.61%` | `67.39` |
| `Live` | `Long` | `7.66` | 496,510.00 USD | 0.00 USD | 135.42 USD | `-13.39%` | `17.69` |
| `Live` | `Long` | `7.67` | 496,380.00 USD | 0.00 USD | 1,740.00 USD | `-13.27%` | `226.45` |
| `Live` | `Long` | `7.68` | 494,640.00 USD | 0.00 USD | 1,120.00 USD | `-13.05%` | `145.25` |
| `Live` | `Long` | `7.70` | 493,520.00 USD | 0.00 USD | 1,460.00 USD | `-12.93%` | `190.36` |
| `Live` | `Long` | `7.71` | 492,060.00 USD | 0.00 USD | 19,410.00 USD | `-12.82%` | `2,518.82` |
| `Live` | `Long` | `7.72` | 472,650.00 USD | 0.00 USD | 2,550.00 USD | `-12.60%` | `330.65` |
| `Live` | `Long` | `7.75` | 470,100.00 USD | 0.00 USD | 893.76 USD | `-12.26%` | `115.25` |
| `Live` | `Long` | `7.76` | 469,200.00 USD | 0.00 USD | 455.73 USD | `-12.14%` | `58.69` |
| `Live` | `Long` | `7.78` | 468,750.00 USD | 0.00 USD | 695.32 USD | `-12.03%` | `89.43` |
| `Live` | `Long` | `7.79` | 468,050.00 USD | 0.00 USD | 3,900.00 USD | `-11.92%` | `500.57` |
| `Live` | `Long` | `7.79` | 464,150.00 USD | 0.00 USD | 1,940.00 USD | `-11.80%` | `248.84` |
| `Live` | `Long` | `7.80` | 462,220.00 USD | 0.00 USD | 633.77 USD | `-11.69%` | `81.20` |
| `Live` | `Long` | `7.82` | 461,580.00 USD | 0.00 USD | 5,280.00 USD | `-11.58%` | `675.43` |
| `Live` | `Long` | `7.84` | 456,300.00 USD | 0.00 USD | 10,930.00 USD | `-11.24%` | `1,393.53` |
| `Live` | `Long` | `7.86` | 445,370.00 USD | 0.00 USD | 2,110.00 USD | `-11.12%` | `269.14` |
| `Live` | `Long` | `7.87` | 443,260.00 USD | 0.00 USD | 176.18 USD | `-11.01%` | `22.40` |
| `Live` | `Long` | `7.88` | 443,080.00 USD | 0.00 USD | 555.19 USD | `-10.90%` | `70.50` |
| `Live` | `Long` | `7.91` | 442,530.00 USD | 0.00 USD | 2,410.00 USD | `-10.56%` | `304.85` |
| `Live` | `Long` | `7.92` | 440,120.00 USD | 0.00 USD | 923.42 USD | `-10.33%` | `116.52` |
| `Live` | `Long` | `7.93` | 439,190.00 USD | 0.00 USD | 1,820.00 USD | `-10.22%` | `228.88` |
| `Live` | `Long` | `7.95` | 437,380.00 USD | 0.00 USD | 127,110.00 USD | `-10.11%` | `15,999.24` |
| `Live` | `Long` | `7.96` | 310,260.00 USD | 0.00 USD | 843.15 USD | `-9.99%` | `105.99` |
| `Live` | `Long` | `7.99` | 309,420.00 USD | 0.00 USD | 1,600.00 USD | `-9.65%` | `200.68` |
| `Live` | `Long` | `8.00` | 307,820.00 USD | 0.00 USD | 210.99 USD | `-9.54%` | `26.39` |
| `Live` | `Long` | `8.03` | 307,610.00 USD | 0.00 USD | 957.70 USD | `-9.20%` | `119.34` |
| `Live` | `Long` | `8.04` | 306,650.00 USD | 0.00 USD | 88,380.00 USD | `-9.09%` | `10,999.50` |
| `Live` | `Long` | `8.04` | 218,270.00 USD | 0.00 USD | 6,890.00 USD | `-8.97%` | `856.44` |
| `Live` | `Long` | `8.05` | 211,380.00 USD | 0.00 USD | 3,340.00 USD | `-8.86%` | `414.27` |
| `Live` | `Long` | `8.06` | 208,040.00 USD | 0.00 USD | 37,830.00 USD | `-8.75%` | `4,690.67` |
| `Live` | `Long` | `8.09` | 170,210.00 USD | 0.00 USD | 617.61 USD | `-8.52%` | `76.39` |
| `Live` | `Long` | `8.10` | 169,590.00 USD | 0.00 USD | 165.46 USD | `-8.41%` | `20.44` |
| `Live` | `Long` | `8.11` | 169,430.00 USD | 0.00 USD | 11,550.00 USD | `-8.30%` | `1,425.26` |
| `Live` | `Long` | `8.12` | 157,870.00 USD | 0.00 USD | 241.26 USD | `-8.18%` | `29.73` |
| `Live` | `Long` | `8.16` | 157,630.00 USD | 0.00 USD | 871.61 USD | `-7.62%` | `106.75` |
| `Live` | `Long` | `8.20` | 156,760.00 USD | 0.00 USD | 1,290.00 USD | `-7.28%` | `157.09` |
| `Live` | `Long` | `8.21` | 155,470.00 USD | 0.00 USD | 1,910.00 USD | `-7.16%` | `232.19` |
| `Live` | `Long` | `8.21` | 153,570.00 USD | 0.00 USD | 147.87 USD | `-7.05%` | `18.00` |
| `Live` | `Long` | `8.22` | 153,420.00 USD | 0.00 USD | 2,100.00 USD | `-6.94%` | `255.16` |
| `Live` | `Long` | `8.23` | 151,320.00 USD | 0.00 USD | 1,160.00 USD | `-6.82%` | `140.81` |
| `Live` | `Long` | `8.24` | 150,160.00 USD | 0.00 USD | 1,300.00 USD | `-6.71%` | `158.06` |
| `Live` | `Long` | `8.26` | 148,860.00 USD | 0.00 USD | 13,810.00 USD | `-6.60%` | `1,673.14` |
| `Live` | `Long` | `8.28` | 135,050.00 USD | 0.00 USD | 9,860.00 USD | `-6.37%` | `1,191.23` |
| `Live` | `Long` | `8.29` | 125,190.00 USD | 0.00 USD | 498.26 USD | `-6.26%` | `60.14` |
| `Live` | `Long` | `8.29` | 124,690.00 USD | 0.00 USD | 18,970.00 USD | `-6.15%` | `2,286.62` |
| `Live` | `Long` | `8.30` | 105,720.00 USD | 0.00 USD | 33,500.00 USD | `-6.03%` | `4,033.57` |
| `Live` | `Long` | `8.31` | 72,230.00 USD | 0.00 USD | 4,550.00 USD | `-5.92%` | `547.70` |
| `Live` | `Long` | `8.34` | 67,670.00 USD | 0.00 USD | 4,630.00 USD | `-5.69%` | `555.62` |
| `Live` | `Long` | `8.36` | 63,040.00 USD | 0.00 USD | 3,410.00 USD | `-5.47%` | `407.63` |
| `Live` | `Long` | `8.37` | 59,640.00 USD | 0.00 USD | 7,160.00 USD | `-5.35%` | `856.48` |
| `Live` | `Long` | `8.38` | 52,470.00 USD | 0.00 USD | 3,410.00 USD | `-5.24%` | `406.80` |
| `Live` | `Long` | `8.38` | 49,060.00 USD | 0.00 USD | 1,870.00 USD | `-5.13%` | `222.50` |
| `Live` | `Long` | `8.39` | 47,200.00 USD | 0.00 USD | 1,680.00 USD | `-5.01%` | `200.00` |
| `Live` | `Long` | `8.40` | 45,520.00 USD | 0.00 USD | 710.22 USD | `-4.90%` | `84.50` |
| `Live` | `Long` | `8.41` | 44,810.00 USD | 0.00 USD | 681.03 USD | `-4.79%` | `80.93` |
| `Live` | `Long` | `8.43` | 44,130.00 USD | 0.00 USD | 674.00 USD | `-4.68%` | `80.00` |
| `Live` | `Long` | `8.44` | 43,450.00 USD | 0.00 USD | 188.61 USD | `-4.56%` | `22.36` |
| `Live` | `Long` | `8.45` | 43,270.00 USD | 0.00 USD | 1,470.00 USD | `-4.45%` | `174.62` |
| `Live` | `Long` | `8.46` | 41,790.00 USD | 0.00 USD | 226.93 USD | `-4.34%` | `26.84` |
| `Live` | `Long` | `8.46` | 41,560.00 USD | 0.00 USD | 1,860.00 USD | `-4.22%` | `220.00` |
| `Live` | `Long` | `8.47` | 39,700.00 USD | 0.00 USD | 12,430.00 USD | `-4.11%` | `1,466.22` |
| `Live` | `Long` | `8.48` | 27,280.00 USD | 0.00 USD | 1,160.00 USD | `-4.00%` | `136.39` |
| `Live` | `Long` | `8.49` | 26,120.00 USD | 0.00 USD | 403.51 USD | `-3.88%` | `47.50` |
| `Live` | `Long` | `8.51` | 25,710.00 USD | 0.00 USD | 6,380.00 USD | `-3.77%` | `750.34` |
| `Live` | `Long` | `8.52` | 19,330.00 USD | 0.00 USD | 7,770.00 USD | `-3.66%` | `912.98` |
| `Live` | `Long` | `8.54` | 11,560.00 USD | 0.00 USD | 6,350.00 USD | `-3.43%` | `743.78` |
| `Live` | `Long` | `8.54` | 5,210.00 USD | 0.00 USD | 1,550.00 USD | `-3.32%` | `180.95` |
| `Live` | `Long` | `8.55` | 3,660.00 USD | 0.00 USD | 684.40 USD | `-3.20%` | `80.00` |
| `Live` | `Long` | `8.61` | 2,980.00 USD | 0.00 USD | 2,980.00 USD | `-2.64%` | `346.30` |
| `Live` | `Short` | `9.13` | 314.34 USD | 314.34 USD | 0.00 USD | `+3.36%` | `34.41` |
| `Live` | `Short` | `9.20` | 4,120.00 USD | 3,800.00 USD | 0.00 USD | `+4.04%` | `413.79` |
| `Live` | `Short` | `9.29` | 4,220.00 USD | 100.93 USD | 0.00 USD | `+5.06%` | `10.87` |
| `Live` | `Short` | `9.35` | 8,150.00 USD | 3,930.00 USD | 0.00 USD | `+5.73%` | `420.07` |
| `Live` | `Short` | `9.38` | 412,260.00 USD | 404,120.00 USD | 0.00 USD | `+6.19%` | `43,059.94` |
| `Live` | `Short` | `9.41` | 414,740.00 USD | 2,470.00 USD | 0.00 USD | `+6.53%` | `262.71` |
| `Live` | `Short` | `9.46` | 417,740.00 USD | 3,010.00 USD | 0.00 USD | `+6.98%` | `318.12` |
| `Live` | `Short` | `9.73` | 417,940.00 USD | 192.95 USD | 0.00 USD | `+10.15%` | `19.82` |
| `Live` | `Short` | `9.79` | 418,490.00 USD | 551.36 USD | 0.00 USD | `+10.83%` | `56.29` |
| `Live` | `Short` | `9.81` | 418,960.00 USD | 472.10 USD | 0.00 USD | `+11.05%` | `48.10` |
| `Live` | `Short` | `10.09` | 419,070.00 USD | 113.76 USD | 0.00 USD | `+14.11%` | `11.28` |
| `Live` | `Short` | `10.15` | 441,390.00 USD | 22,320.00 USD | 0.00 USD | `+14.90%` | `2,197.71` |
| `Live` | `Short` | `10.21` | 448,720.00 USD | 7,330.00 USD | 0.00 USD | `+15.58%` | `717.30` |
| `Live` | `Short` | `10.23` | 448,830.00 USD | 114.12 USD | 0.00 USD | `+15.80%` | `11.15` |
| `Live` | `Short` | `10.35` | 452,220.00 USD | 3,380.00 USD | 0.00 USD | `+17.05%` | `326.92` |
| `Live` | `Short` | `10.56` | 452,740.00 USD | 523.81 USD | 0.00 USD | `+19.54%` | `49.58` |
| `Live` | `Short` | `10.70` | 489,770.00 USD | 37,030.00 USD | 0.00 USD | `+21.01%` | `3,462.73` |
| `Live` | `Short` | `10.71` | 489,990.00 USD | 218.91 USD | 0.00 USD | `+21.24%` | `20.43` |
| `Live` | `Short` | `10.96` | 491,910.00 USD | 1,920.00 USD | 0.00 USD | `+24.06%` | `174.67` |
| `Live` | `Short` | `11.01` | 498,870.00 USD | 6,970.00 USD | 0.00 USD | `+24.52%` | `633.00` |
| `Live` | `Short` | `11.27` | 510,680.00 USD | 11,810.00 USD | 0.00 USD | `+27.46%` | `1,048.25` |
| `Live` | `Short` | `11.47` | 511,400.00 USD | 720.29 USD | 0.00 USD | `+29.83%` | `62.77` |
| `Live` | `Short` | `11.62` | 523,540.00 USD | 12,140.00 USD | 0.00 USD | `+31.53%` | `1,043.90` |
| `Live` | `Short` | `11.70` | 524,320.00 USD | 778.89 USD | 0.00 USD | `+32.32%` | `66.60` |
| `Live` | `Short` | `11.81` | 583,390.00 USD | 59,080.00 USD | 0.00 USD | `+33.68%` | `5,000.00` |
| `Live` | `Short` | `12.04` | 584,760.00 USD | 1,370.00 USD | 0.00 USD | `+36.17%` | `113.77` |
| `Live` | `Short` | `12.30` | 586,490.00 USD | 1,730.00 USD | 0.00 USD | `+39.23%` | `140.71` |
| `Live` | `Short` | `12.40` | 586,840.00 USD | 343.62 USD | 0.00 USD | `+40.36%` | `27.70` |
| `Live` | `Short` | `12.68` | 587,270.00 USD | 432.22 USD | 0.00 USD | `+43.41%` | `34.10` |
| `Live` | `Short` | `12.76` | 624,000.00 USD | 36,730.00 USD | 0.00 USD | `+44.32%` | `2,879.71` |
| `Live` | `Short` | `12.79` | 624,950.00 USD | 953.38 USD | 0.00 USD | `+44.66%` | `74.57` |
| `Live` | `Short` | `12.96` | 625,050.00 USD | 102.68 USD | 0.00 USD | `+46.69%` | `7.92` |
| `Live` | `Short` | `12.97` | 639,590.00 USD | 14,530.00 USD | 0.00 USD | `+46.81%` | `1,120.14` |
| `Live` | `Short` | `13.20` | 727,530.00 USD | 87,940.00 USD | 0.00 USD | `+49.30%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 962,370.00 USD | 234,840.00 USD | 0.00 USD | `+50.31%` | `17,677.02` |
| `Live` | `Short` | `13.29` | 966,180.00 USD | 3,810.00 USD | 0.00 USD | `+50.43%` | `286.56` |
| `Live` | `Short` | `13.46` | 966,610.00 USD | 430.34 USD | 0.00 USD | `+52.35%` | `31.96` |
| `Live` | `Short` | `13.69` | 966,790.00 USD | 172.29 USD | 0.00 USD | `+54.84%` | `12.59` |
| `Live` | `Short` | `14.14` | 966,950.00 USD | 164.79 USD | 0.00 USD | `+60.04%` | `11.65` |
| `Live` | `Short` | `14.43` | 970,950.00 USD | 4,000.00 USD | 0.00 USD | `+63.21%` | `277.54` |
| `Live` | `Short` | `14.62` | 971,240.00 USD | 288.35 USD | 0.00 USD | `+65.36%` | `19.73` |
| `Live` | `Short` | `14.66` | 972,070.00 USD | 823.29 USD | 0.00 USD | `+65.93%` | `56.14` |
| `Live` | `Short` | `14.84` | 972,310.00 USD | 243.44 USD | 0.00 USD | `+67.85%` | `16.41` |
| `Live` | `Short` | `14.86` | 974,780.00 USD | 2,470.00 USD | 0.00 USD | `+68.08%` | `166.16` |
| `Live` | `Short` | `14.95` | 975,100.00 USD | 322.06 USD | 0.00 USD | `+69.10%` | `21.55` |
| `Live` | `Short` | `15.29` | 975,330.00 USD | 229.43 USD | 0.00 USD | `+73.06%` | `15.00` |
| `Live` | `Short` | `15.35` | 975,560.00 USD | 230.17 USD | 0.00 USD | `+73.62%` | `15.00` |
| `Live` | `Short` | `15.38` | 995,560.00 USD | 20,000.00 USD | 0.00 USD | `+74.07%` | `1,300.00` |
| `Live` | `Short` | `15.49` | 1,150,000.00 USD | 154,950.00 USD | 0.00 USD | `+75.32%` | `10,000.00` |
| `Live` | `Short` | `15.74` | 1,150,000.00 USD | 111.95 USD | 0.00 USD | `+78.15%` | `7.11` |
| `Live` | `Short` | `16.29` | 1,410,000.00 USD | 263,950.00 USD | 0.00 USD | `+84.26%` | `16,208.00` |
| `Live` | `Short` | `16.46` | 1,440,000.00 USD | 22,620.00 USD | 0.00 USD | `+86.29%` | `1,373.91` |
| `Live` | `Short` | `16.52` | 1,440,000.00 USD | 190.91 USD | 0.00 USD | `+86.86%` | `11.56` |
| `Live` | `Short` | `16.75` | 1,520,000.00 USD | 84,520.00 USD | 0.00 USD | `+89.46%` | `5,047.35` |
| `Live` | `Short` | `16.77` | 1,520,000.00 USD | 340.87 USD | 0.00 USD | `+89.80%` | `20.32` |
| `Live` | `Short` | `17.02` | 1,520,000.00 USD | 191.87 USD | 0.00 USD | `+92.63%` | `11.27` |
| `Live` | `Short` | `17.14` | 1,520,000.00 USD | 1,710.00 USD | 0.00 USD | `+93.87%` | `100.00` |
| `Live` | `Short` | `17.46` | 1,520,000.00 USD | 101.47 USD | 0.00 USD | `+97.61%` | `5.81` |
| `Live` | `Short` | `17.62` | 1,530,000.00 USD | 4,120.00 USD | 0.00 USD | `+99.42%` | `233.67` |
| `Live` | `Short` | `17.64` | 1,530,000.00 USD | 4,930.00 USD | 0.00 USD | `+99.64%` | `279.46` |
| `Live` | `Short` | `17.66` | 1,540,000.00 USD | 2,660.00 USD | 0.00 USD | `+99.87%` | `150.82` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 320,770.00 USD | 0.00 USD | 611.73 USD | `-73.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 320,160.00 USD | 0.00 USD | 793.75 USD | `-54.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 319,370.00 USD | 0.00 USD | 105.04 USD | `-49.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 319,260.00 USD | 0.00 USD | 67,970.00 USD | `-43.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 251,300.00 USD | 0.00 USD | 205.30 USD | `-39.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 251,090.00 USD | 0.00 USD | 465.42 USD | `-38.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 250,630.00 USD | 0.00 USD | 349.35 USD | `-37.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 250,280.00 USD | 0.00 USD | 1,330.00 USD | `-34.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 248,950.00 USD | 0.00 USD | 493.50 USD | `-32.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 248,450.00 USD | 0.00 USD | 100.98 USD | `-32.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 248,350.00 USD | 0.00 USD | 620.80 USD | `-32.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 247,730.00 USD | 0.00 USD | 4,160.00 USD | `-30.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 243,580.00 USD | 0.00 USD | 6,500.00 USD | `-30.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 237,070.00 USD | 0.00 USD | 864.38 USD | `-28.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 236,210.00 USD | 0.00 USD | 1,430.00 USD | `-26.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 234,780.00 USD | 0.00 USD | 4,340.00 USD | `-26.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 230,440.00 USD | 0.00 USD | 5,520.00 USD | `-24.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 224,920.00 USD | 0.00 USD | 100.72 USD | `-24.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 224,820.00 USD | 0.00 USD | 296.34 USD | `-23.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 224,520.00 USD | 0.00 USD | 921.19 USD | `-23.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 223,600.00 USD | 0.00 USD | 709.98 USD | `-21.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 222,890.00 USD | 0.00 USD | 262.44 USD | `-21.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 222,630.00 USD | 0.00 USD | 3,610.00 USD | `-20.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 219,010.00 USD | 0.00 USD | 6,790.00 USD | `-18.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 212,220.00 USD | 0.00 USD | 9,770.00 USD | `-18.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 202,450.00 USD | 0.00 USD | 103.46 USD | `-18.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 202,350.00 USD | 0.00 USD | 603.44 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 201,750.00 USD | 0.00 USD | 891.57 USD | `-17.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 200,860.00 USD | 0.00 USD | 2,300.00 USD | `-17.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 198,550.00 USD | 0.00 USD | 129.58 USD | `-17.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 198,420.00 USD | 0.00 USD | 236.19 USD | `-17.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 198,190.00 USD | 0.00 USD | 199.39 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 197,990.00 USD | 0.00 USD | 4,730.00 USD | `-15.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 193,260.00 USD | 0.00 USD | 37,420.00 USD | `-15.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 155,830.00 USD | 0.00 USD | 778.49 USD | `-15.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 155,050.00 USD | 0.00 USD | 799.83 USD | `-14.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 154,250.00 USD | 0.00 USD | 103.41 USD | `-14.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 154,150.00 USD | 0.00 USD | 1,370.00 USD | `-14.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 152,780.00 USD | 0.00 USD | 360.13 USD | `-12.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 152,420.00 USD | 0.00 USD | 578.04 USD | `-12.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 151,840.00 USD | 0.00 USD | 175.42 USD | `-12.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 151,660.00 USD | 0.00 USD | 2,990.00 USD | `-11.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 148,670.00 USD | 0.00 USD | 143.51 USD | `-11.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 148,520.00 USD | 0.00 USD | 183.33 USD | `-11.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.88` | 148,340.00 USD | 0.00 USD | 194.52 USD | `-10.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 148,150.00 USD | 0.00 USD | 394.75 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 147,750.00 USD | 0.00 USD | 1,350.00 USD | `-10.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 146,400.00 USD | 0.00 USD | 1,590.00 USD | `-10.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 144,820.00 USD | 0.00 USD | 898.42 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 143,920.00 USD | 0.00 USD | 1,350.00 USD | `-9.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 142,570.00 USD | 0.00 USD | 7,400.00 USD | `-9.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 135,180.00 USD | 0.00 USD | 123.58 USD | `-9.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 135,050.00 USD | 0.00 USD | 2,110.00 USD | `-8.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 132,940.00 USD | 0.00 USD | 563.85 USD | `-8.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 132,380.00 USD | 0.00 USD | 105.14 USD | `-8.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 132,270.00 USD | 0.00 USD | 367.76 USD | `-8.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 131,910.00 USD | 0.00 USD | 2,330.00 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 129,570.00 USD | 0.00 USD | 184.13 USD | `-8.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 129,390.00 USD | 0.00 USD | 6,500.00 USD | `-8.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 122,890.00 USD | 0.00 USD | 462.15 USD | `-7.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 122,420.00 USD | 0.00 USD | 654.53 USD | `-7.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 121,770.00 USD | 0.00 USD | 367.91 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 121,400.00 USD | 0.00 USD | 520.75 USD | `-7.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 120,880.00 USD | 0.00 USD | 2,900.00 USD | `-7.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 117,980.00 USD | 0.00 USD | 141.04 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 117,840.00 USD | 0.00 USD | 1,780.00 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 116,050.00 USD | 0.00 USD | 515.66 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 115,540.00 USD | 0.00 USD | 143.54 USD | `-6.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 115,390.00 USD | 0.00 USD | 168.64 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 115,220.00 USD | 0.00 USD | 201.49 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 115,020.00 USD | 0.00 USD | 6,530.00 USD | `-6.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 108,500.00 USD | 0.00 USD | 1,140.00 USD | `-5.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 107,350.00 USD | 0.00 USD | 2,000.00 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 105,350.00 USD | 0.00 USD | 756.06 USD | `-5.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 104,590.00 USD | 0.00 USD | 970.35 USD | `-5.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 103,620.00 USD | 0.00 USD | 5,470.00 USD | `-5.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 98,160.00 USD | 0.00 USD | 1,970.00 USD | `-5.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 96,190.00 USD | 0.00 USD | 3,290.00 USD | `-4.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 92,900.00 USD | 0.00 USD | 358.56 USD | `-4.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 92,540.00 USD | 0.00 USD | 1,880.00 USD | `-4.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 90,660.00 USD | 0.00 USD | 140.36 USD | `-4.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 90,520.00 USD | 0.00 USD | 138.24 USD | `-4.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 90,380.00 USD | 0.00 USD | 954.23 USD | `-4.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 89,430.00 USD | 0.00 USD | 769.61 USD | `-4.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.48` | 88,660.00 USD | 0.00 USD | 489.58 USD | `-4.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.51` | 88,170.00 USD | 0.00 USD | 1,440.00 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.52` | 86,730.00 USD | 0.00 USD | 198.74 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.53` | 86,530.00 USD | 0.00 USD | 1,130.00 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 85,400.00 USD | 0.00 USD | 132.45 USD | `-3.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.57` | 85,270.00 USD | 0.00 USD | 428.58 USD | `-2.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.59` | 84,840.00 USD | 0.00 USD | 2,500.00 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.60` | 82,340.00 USD | 0.00 USD | 435.59 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.61` | 81,900.00 USD | 0.00 USD | 1,080.00 USD | `-2.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 80,830.00 USD | 0.00 USD | 1,980.00 USD | `-2.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 78,850.00 USD | 0.00 USD | 2,740.00 USD | `-2.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.63` | 76,100.00 USD | 0.00 USD | 103.19 USD | `-2.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.64` | 76,000.00 USD | 0.00 USD | 103.31 USD | `-2.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 75,900.00 USD | 0.00 USD | 1,900.00 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.66` | 73,990.00 USD | 0.00 USD | 196.87 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.68` | 73,800.00 USD | 0.00 USD | 223.82 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.69` | 73,570.00 USD | 0.00 USD | 990.09 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.70` | 72,580.00 USD | 0.00 USD | 5,010.00 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 67,570.00 USD | 0.00 USD | 6,880.00 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 60,690.00 USD | 0.00 USD | 134.30 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.72` | 60,550.00 USD | 0.00 USD | 390.88 USD | `-1.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.73` | 60,160.00 USD | 0.00 USD | 1,390.00 USD | `-1.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.74` | 58,770.00 USD | 0.00 USD | 933.70 USD | `-1.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.76` | 57,840.00 USD | 0.00 USD | 6,300.00 USD | `-0.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.77` | 51,540.00 USD | 0.00 USD | 39,810.00 USD | `-0.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.78` | 11,730.00 USD | 0.00 USD | 114.25 USD | `-0.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 11,620.00 USD | 0.00 USD | 4,230.00 USD | `-0.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 7,390.00 USD | 0.00 USD | 2,650.00 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.80` | 4,740.00 USD | 0.00 USD | 1,760.00 USD | `-0.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.81` | 2,980.00 USD | 0.00 USD | 705.20 USD | `-0.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.82` | 2,280.00 USD | 0.00 USD | 2,030.00 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.84` | 243.40 USD | 0.00 USD | 243.40 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 5,760.00 USD | 5,760.00 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 5,960.00 USD | 192.86 USD | 0.00 USD | `+0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 6,570.00 USD | 614.88 USD | 0.00 USD | `+0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 7,120.00 USD | 543.33 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 8,220.00 USD | 1,100.00 USD | 0.00 USD | `+0.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 8,410.00 USD | 188.66 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 9,200.00 USD | 788.72 USD | 0.00 USD | `+0.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 12,560.00 USD | 3,360.00 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 12,670.00 USD | 110.58 USD | 0.00 USD | `+0.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 13,680.00 USD | 1,020.00 USD | 0.00 USD | `+1.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 13,910.00 USD | 223.62 USD | 0.00 USD | `+1.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 14,050.00 USD | 137.73 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 14,450.00 USD | 401.63 USD | 0.00 USD | `+1.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 329,600.00 USD | 315,150.00 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 329,700.00 USD | 104.59 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 330,480.00 USD | 776.54 USD | 0.00 USD | `+1.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 331,010.00 USD | 531.20 USD | 0.00 USD | `+1.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 332,390.00 USD | 1,380.00 USD | 0.00 USD | `+2.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 333,480.00 USD | 1,090.00 USD | 0.00 USD | `+2.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 334,090.00 USD | 616.37 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 334,190.00 USD | 102.03 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 334,650.00 USD | 453.84 USD | 0.00 USD | `+2.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 334,810.00 USD | 160.99 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 335,220.00 USD | 415.00 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 336,730.00 USD | 1,510.00 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 338,770.00 USD | 2,040.00 USD | 0.00 USD | `+2.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 566,410.00 USD | 227,630.00 USD | 0.00 USD | `+3.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 569,440.00 USD | 3,030.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 571,440.00 USD | 2,000.00 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 965,650.00 USD | 394,210.00 USD | 0.00 USD | `+3.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,000,000.00 USD | 39,130.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.20` | 1,010,000.00 USD | 1,590.00 USD | 0.00 USD | `+4.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,010,000.00 USD | 3,320.00 USD | 0.00 USD | `+4.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,010,000.00 USD | 131.87 USD | 0.00 USD | `+4.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,010,000.00 USD | 687.91 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,010,000.00 USD | 954.71 USD | 0.00 USD | `+4.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,410,000.00 USD | 398,520.00 USD | 0.00 USD | `+4.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.27` | 1,410,000.00 USD | 205.87 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,410,000.00 USD | 1,960.00 USD | 0.00 USD | `+4.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,410,000.00 USD | 434.45 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,430,000.00 USD | 18,610.00 USD | 0.00 USD | `+5.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,430,000.00 USD | 354.81 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,430,000.00 USD | 2,180.00 USD | 0.00 USD | `+5.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,430,000.00 USD | 579.86 USD | 0.00 USD | `+5.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,760,000.00 USD | 327,430.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,760,000.00 USD | 233.38 USD | 0.00 USD | `+5.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,760,000.00 USD | 163.41 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,760,000.00 USD | 1,150.00 USD | 0.00 USD | `+6.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,760,000.00 USD | 660.84 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,770,000.00 USD | 2,480.00 USD | 0.00 USD | `+6.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,770,000.00 USD | 1,110.00 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,770,000.00 USD | 219.84 USD | 0.00 USD | `+6.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,770,000.00 USD | 140.35 USD | 0.00 USD | `+6.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,770,000.00 USD | 1,890.00 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.47` | 1,770,000.00 USD | 1,780.00 USD | 0.00 USD | `+7.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,770,000.00 USD | 2,210.00 USD | 0.00 USD | `+7.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,770,000.00 USD | 288.46 USD | 0.00 USD | `+7.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.51` | 1,780,000.00 USD | 1,600.00 USD | 0.00 USD | `+7.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,780,000.00 USD | 103.54 USD | 0.00 USD | `+7.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.56` | 1,780,000.00 USD | 535.35 USD | 0.00 USD | `+8.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,780,000.00 USD | 231.00 USD | 0.00 USD | `+8.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,780,000.00 USD | 221.07 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,780,000.00 USD | 1,470.00 USD | 0.00 USD | `+8.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,780,000.00 USD | 148.48 USD | 0.00 USD | `+9.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,780,000.00 USD | 329.43 USD | 0.00 USD | `+9.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,780,000.00 USD | 446.58 USD | 0.00 USD | `+9.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,780,000.00 USD | 108.21 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,780,000.00 USD | 169.68 USD | 0.00 USD | `+10.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,780,000.00 USD | 121.87 USD | 0.00 USD | `+10.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.80` | 1,780,000.00 USD | 619.28 USD | 0.00 USD | `+10.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,790,000.00 USD | 5,030.00 USD | 0.00 USD | `+11.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,790,000.00 USD | 340.05 USD | 0.00 USD | `+11.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,790,000.00 USD | 742.12 USD | 0.00 USD | `+11.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,790,000.00 USD | 899.47 USD | 0.00 USD | `+12.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,860,000.00 USD | 70,020.00 USD | 0.00 USD | `+12.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,860,000.00 USD | 373.97 USD | 0.00 USD | `+12.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,870,000.00 USD | 7,500.00 USD | 0.00 USD | `+13.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,870,000.00 USD | 6,370.00 USD | 0.00 USD | `+13.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,870,000.00 USD | 202.10 USD | 0.00 USD | `+14.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,080,000.00 USD | 210,980.00 USD | 0.00 USD | `+14.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,080,000.00 USD | 1,150.00 USD | 0.00 USD | `+14.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 2,080,000.00 USD | 172.16 USD | 0.00 USD | `+15.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 2,080,000.00 USD | 868.36 USD | 0.00 USD | `+16.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 2,090,000.00 USD | 489.40 USD | 0.00 USD | `+16.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 2,090,000.00 USD | 1,200.00 USD | 0.00 USD | `+17.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 2,090,000.00 USD | 118.01 USD | 0.00 USD | `+17.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 2,090,000.00 USD | 312.31 USD | 0.00 USD | `+18.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 2,090,000.00 USD | 1,530.00 USD | 0.00 USD | `+18.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 2,090,000.00 USD | 178.46 USD | 0.00 USD | `+19.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.62` | 2,090,000.00 USD | 153.11 USD | 0.00 USD | `+20.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 2,090,000.00 USD | 173.42 USD | 0.00 USD | `+21.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 2,090,000.00 USD | 184.75 USD | 0.00 USD | `+21.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 2,090,000.00 USD | 135.78 USD | 0.00 USD | `+22.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 2,090,000.00 USD | 127.96 USD | 0.00 USD | `+22.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 2,090,000.00 USD | 476.43 USD | 0.00 USD | `+23.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 2,090,000.00 USD | 1,730.00 USD | 0.00 USD | `+23.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 2,090,000.00 USD | 118.97 USD | 0.00 USD | `+23.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 2,090,000.00 USD | 251.06 USD | 0.00 USD | `+23.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 2,090,000.00 USD | 552.44 USD | 0.00 USD | `+23.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 2,090,000.00 USD | 1,750.00 USD | 0.00 USD | `+24.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 2,090,000.00 USD | 320.29 USD | 0.00 USD | `+25.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 2,100,000.00 USD | 1,100.00 USD | 0.00 USD | `+26.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 2,100,000.00 USD | 2,610.00 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 2,100,000.00 USD | 1,270.00 USD | 0.00 USD | `+27.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 2,100,000.00 USD | 1,380.00 USD | 0.00 USD | `+28.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 2,100,000.00 USD | 2,410.00 USD | 0.00 USD | `+29.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 2,110,000.00 USD | 9,520.00 USD | 0.00 USD | `+29.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 2,120,000.00 USD | 3,530.00 USD | 0.00 USD | `+30.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 2,120,000.00 USD | 7,700.00 USD | 0.00 USD | `+31.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 2,130,000.00 USD | 1,130.00 USD | 0.00 USD | `+33.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 2,130,000.00 USD | 434.61 USD | 0.00 USD | `+34.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 2,130,000.00 USD | 163.52 USD | 0.00 USD | `+34.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 2,250,000.00 USD | 124,300.00 USD | 0.00 USD | `+35.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.51` | 2,250,000.00 USD | 2,770.00 USD | 0.00 USD | `+41.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 2,260,000.00 USD | 3,350.00 USD | 0.00 USD | `+43.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 2,260,000.00 USD | 197.97 USD | 0.00 USD | `+44.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 2,260,000.00 USD | 3,200.00 USD | 0.00 USD | `+46.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 2,260,000.00 USD | 179.58 USD | 0.00 USD | `+46.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 2,260,000.00 USD | 720.74 USD | 0.00 USD | `+47.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.07` | 2,260,000.00 USD | 504.17 USD | 0.00 USD | `+47.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 2,260,000.00 USD | 169.57 USD | 0.00 USD | `+48.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.30` | 2,260,000.00 USD | 159.66 USD | 0.00 USD | `+50.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 2,260,000.00 USD | 446.52 USD | 0.00 USD | `+51.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.46` | 2,260,000.00 USD | 1,710.00 USD | 0.00 USD | `+52.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 2,270,000.00 USD | 5,320.00 USD | 0.00 USD | `+52.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,480,000.00 USD | 207,980.00 USD | 0.00 USD | `+52.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,480,000.00 USD | 407.95 USD | 0.00 USD | `+54.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,480,000.00 USD | 174.91 USD | 0.00 USD | `+56.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,490,000.00 USD | 9,230.00 USD | 0.00 USD | `+58.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,490,000.00 USD | 960.26 USD | 0.00 USD | `+60.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,490,000.00 USD | 2,710.00 USD | 0.00 USD | `+62.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,490,000.00 USD | 805.90 USD | 0.00 USD | `+64.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,490,000.00 USD | 655.55 USD | 0.00 USD | `+66.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,500,000.00 USD | 4,890.00 USD | 0.00 USD | `+67.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,500,000.00 USD | 471.09 USD | 0.00 USD | `+68.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,500,000.00 USD | 383.85 USD | 0.00 USD | `+69.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 3,150,000.00 USD | 652,070.00 USD | 0.00 USD | `+69.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 3,150,000.00 USD | 111.87 USD | 0.00 USD | `+79.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 3,150,000.00 USD | 219.91 USD | 0.00 USD | `+81.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 3,150,000.00 USD | 121.74 USD | 0.00 USD | `+91.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.00` | 3,150,000.00 USD | 297.59 USD | 0.00 USD | `+92.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.18` | 3,150,000.00 USD | 4,500.00 USD | 0.00 USD | `+94.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.20` | 3,280,000.00 USD | 120,270.00 USD | 0.00 USD | `+94.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.34` | 3,280,000.00 USD | 122.39 USD | 0.00 USD | `+96.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.50` | 3,280,000.00 USD | 586.59 USD | 0.00 USD | `+98.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.61` | 3,280,000.00 USD | 580.97 USD | 0.00 USD | `+99.19%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.80` | 9,610,000.00 USD | 0.00 USD | 9,610,000.00 USD | 22,120.00 USD | 12,980.00 USD | 15,300.00 USD |
| `7D` | `7.82` | 9,560,000.00 USD | 0.00 USD | 9,560,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,280.00 USD |
| `7D` | `7.84` | 9,550,000.00 USD | 0.00 USD | 9,550,000.00 USD | 29,020.00 USD | 2,380.00 USD | 19,730.00 USD |
| `7D` | `7.86` | 9,500,000.00 USD | 0.00 USD | 9,500,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD |
| `7D` | `7.88` | 9,450,000.00 USD | 0.00 USD | 9,450,000.00 USD | 46,450.00 USD | 12,780.00 USD | 29,190.00 USD |
| `7D` | `7.90` | 9,360,000.00 USD | 0.00 USD | 9,360,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,650.00 USD |
| `1D` | `7.91` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 11,920.00 USD | 3,480.00 USD | 7,980.00 USD |
| `1D` | `7.92` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 13,160.00 USD | 2,950.00 USD | 3,970.00 USD |
| `7D` | `7.92` | 9,300,000.00 USD | 0.00 USD | 9,300,000.00 USD | 53,660.00 USD | 8,420.00 USD | 14,900.00 USD |
| `1D` | `7.93` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 7,960.00 USD | 2,710.00 USD | 0.00 USD |
| `1D` | `7.94` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 7,590.00 USD | 4,150.00 USD | 1,730.00 USD |
| `7D` | `7.94` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 49,080.00 USD | 9,960.00 USD | 31,670.00 USD |
| `1D` | `7.95` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 74.90 USD | 5,170.00 USD | 3,470.00 USD |
| `1D` | `7.96` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 2,760.00 USD | 3,170.00 USD | 13.70 USD |
| `7D` | `7.96` | 9,130,000.00 USD | 0.00 USD | 9,130,000.00 USD | 21,840.00 USD | 6,920.00 USD | 26,390.00 USD |
| `1D` | `7.97` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 5,250.00 USD | 0.00 USD | 2,280.00 USD |
| `1D` | `7.98` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD |
| `7D` | `7.98` | 9,070,000.00 USD | 0.00 USD | 9,070,000.00 USD | 43,200.00 USD | 19,680.00 USD | 70,210.00 USD |
| `1D` | `7.99` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 482.38 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.00` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD |
| `7D` | `8.00` | 8,940,000.00 USD | 0.00 USD | 8,940,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,130.00 USD |
| `1D` | `8.01` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 6,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.02` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 9,100.00 USD | 770.83 USD | 9.39 USD |
| `7D` | `8.02` | 8,860,000.00 USD | 0.00 USD | 8,860,000.00 USD | 20,910.00 USD | 28,440.00 USD | 10,370.00 USD |
| `1D` | `8.03` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 8,600.00 USD | 1,540.00 USD | 1,960.00 USD |
| `1D` | `8.04` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 9,860.00 USD | 0.00 USD | 6,190.00 USD |
| `7D` | `8.04` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 123,080.00 USD | 27,860.00 USD | 86,550.00 USD |
| `1D` | `8.05` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 17,150.00 USD | 4,800.00 USD | 2,250.00 USD |
| `1D` | `8.06` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 16,840.00 USD | 1,700.00 USD | 5,880.00 USD |
| `7D` | `8.06` | 8,570,000.00 USD | 0.00 USD | 8,570,000.00 USD | 70,840.00 USD | 10,070.00 USD | 86,170.00 USD |
| `1D` | `8.07` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 1,100.00 USD | 2,400.00 USD | 6,030.00 USD |
| `1D` | `8.08` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 4,700.00 USD | 1,410.00 USD | 3,220.00 USD |
| `7D` | `8.08` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,860.00 USD |
| `1D` | `8.09` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 9,630.00 USD | 1,220.00 USD | 6,380.00 USD |
| `1D` | `8.10` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 23,830.00 USD | 3,750.00 USD | 8,060.00 USD |
| `7D` | `8.10` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 61,500.00 USD | 19,700.00 USD | 14,170.00 USD |
| `1D` | `8.11` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 4,510.00 USD | 4,240.00 USD | 1,360.00 USD |
| `1D` | `8.12` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 9,910.00 USD | 0.00 USD | 7,240.00 USD |
| `7D` | `8.12` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 27,520.00 USD | 10,810.00 USD | 9,260.00 USD |
| `1D` | `8.13` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 7,130.00 USD | 693.45 USD | 1,310.00 USD |
| `1D` | `8.14` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 16,900.00 USD | 0.00 USD | 26.83 USD |
| `7D` | `8.14` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 72,460.00 USD | 11,150.00 USD | 39,780.00 USD |
| `1D` | `8.15` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 14,590.00 USD | 662.47 USD | 5,000.00 USD |
| `1D` | `8.16` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 385.98 USD | 2,120.00 USD | 47.18 USD |
| `7D` | `8.16` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 38,430.00 USD | 5,510.00 USD | 30,640.00 USD |
| `1D` | `8.17` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 2,970.00 USD | 0.00 USD | 12.32 USD |
| `1D` | `8.18` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 1,150.00 USD | 1,980.00 USD | 466.21 USD |
| `7D` | `8.18` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 10,520.00 USD | 6,790.00 USD | 2,750.00 USD |
| `1D` | `8.19` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 4,450.00 USD | 0.00 USD | 19.88 USD |
| `1D` | `8.20` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 7,720.00 USD | 2,310.00 USD | 445.22 USD |
| `7D` | `8.20` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 34,140.00 USD | 0.00 USD | 9,870.00 USD |
| `1D` | `8.21` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 2,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.22` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 5,330.00 USD | 0.00 USD | 12,570.00 USD |
| `7D` | `8.22` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 19,610.00 USD | 0.00 USD | 10,790.00 USD |
| `1D` | `8.23` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 20,920.00 USD | 4,080.00 USD | 31,000.00 USD |
| `1D` | `8.24` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 10,190.00 USD | 1,150.00 USD | 3,510.00 USD |
| `7D` | `8.24` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 39,950.00 USD | 3,480.00 USD | 107,080.00 USD |
| `1D` | `8.25` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 8,080.00 USD | 0.00 USD | 6,100.00 USD |
| `1D` | `8.26` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 192.60 USD | 11,460.00 USD | 0.00 USD |
| `7D` | `8.26` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 30,490.00 USD | 5,750.00 USD | 9,400.00 USD |
| `1D` | `8.27` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 11,310.00 USD | 2,760.00 USD | 21.52 USD |
| `1D` | `8.28` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 74,500.00 USD | 7,070.00 USD | 40,790.00 USD |
| `7D` | `8.28` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 122,850.00 USD | 33,920.00 USD | 14,010.00 USD |
| `1D` | `8.29` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 34,850.00 USD | 9,470.00 USD | 4,640.00 USD |
| `1D` | `8.30` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 53,200.00 USD | 13,130.00 USD | 19,010.00 USD |
| `7D` | `8.30` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 101,900.00 USD | 13,500.00 USD | 47,820.00 USD |
| `1D` | `8.31` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 56,000.00 USD | 11,410.00 USD | 1,570.00 USD |
| `1D` | `8.32` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 19,380.00 USD | 4,190.00 USD | 7,320.00 USD |
| `7D` | `8.32` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 61,880.00 USD | 26,020.00 USD | 4,900.00 USD |
| `1D` | `8.33` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 2,970.00 USD | 22,580.00 USD | 9,950.00 USD |
| `1D` | `8.34` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 14,500.00 USD | 4,810.00 USD | 6,270.00 USD |
| `7D` | `8.34` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 37,760.00 USD | 15,520.00 USD | 30,360.00 USD |
| `1D` | `8.35` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 6,790.00 USD | 11,270.00 USD | 16,090.00 USD |
| `1D` | `8.36` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 4,390.00 USD | 2,420.00 USD | 21,790.00 USD |
| `7D` | `8.36` | 7,220,000.00 USD | 0.00 USD | 7,220,000.00 USD | 107,760.00 USD | 13,470.00 USD | 71,060.00 USD |
| `1D` | `8.37` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 21,970.00 USD | 7,980.00 USD | 8,340.00 USD |
| `1D` | `8.38` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 36,140.00 USD | 4,080.00 USD | 33,870.00 USD |
| `7D` | `8.38` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 143,540.00 USD | 20,560.00 USD | 66,570.00 USD |
| `1D` | `8.39` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 63,440.00 USD | 10,540.00 USD | 56,460.00 USD |
| `1D` | `8.40` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 67,650.00 USD | 22,890.00 USD | 68,000.00 USD |
| `7D` | `8.40` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 150,350.00 USD | 19,710.00 USD | 220,190.00 USD |
| `1D` | `8.41` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 33,190.00 USD | 3,620.00 USD | 20,930.00 USD |
| `1D` | `8.42` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 33,600.00 USD | 12,790.00 USD | 18,430.00 USD |
| `7D` | `8.42` | 6,410,000.00 USD | 0.00 USD | 6,410,000.00 USD | 178,300.00 USD | 57,340.00 USD | 72,790.00 USD |
| `1D` | `8.43` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 29,980.00 USD | 34,530.00 USD | 14,410.00 USD |
| `1D` | `8.44` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 35,570.00 USD | 8,900.00 USD | 5,560.00 USD |
| `7D` | `8.44` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 155,040.00 USD | 68,350.00 USD | 76,630.00 USD |
| `1D` | `8.45` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 73,020.00 USD | 17,050.00 USD | 49,380.00 USD |
| `1D` | `8.46` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 153,340.00 USD | 16,420.00 USD | 47,800.00 USD |
| `7D` | `8.46` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 392,550.00 USD | 59,170.00 USD | 107,670.00 USD |
| `1D` | `8.47` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 107,260.00 USD | 30,070.00 USD | 15,180.00 USD |
| `1D` | `8.48` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 126,360.00 USD | 39,180.00 USD | 48,850.00 USD |
| `7D` | `8.48` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 360,640.00 USD | 61,660.00 USD | 220,080.00 USD |
| `1D` | `8.49` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 137,160.00 USD | 36,190.00 USD | 7,700.00 USD |
| `1D` | `8.50` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 51,910.00 USD | 11,120.00 USD | 26,230.00 USD |
| `7D` | `8.50` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 191,430.00 USD | 100,070.00 USD | 112,420.00 USD |
| `1D` | `8.51` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 7,460.00 USD | 45,150.00 USD | 19,680.00 USD |
| `1D` | `8.52` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 48,940.00 USD | 17,250.00 USD | 23,620.00 USD |
| `7D` | `8.52` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 270,540.00 USD | 98,920.00 USD | 250,640.00 USD |
| `1D` | `8.53` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 17,330.00 USD | 29,630.00 USD | 41,670.00 USD |
| `1D` | `8.54` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 19,400.00 USD | 6,040.00 USD | 43,640.00 USD |
| `7D` | `8.54` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 379,850.00 USD | 78,380.00 USD | 152,160.00 USD |
| `1D` | `8.55` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 64,630.00 USD | 19,250.00 USD | 19,190.00 USD |
| `1D` | `8.56` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 69,420.00 USD | 12,010.00 USD | 67,740.00 USD |
| `7D` | `8.56` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 593,510.00 USD | 101,070.00 USD | 88,350.00 USD |
| `1D` | `8.57` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 73,460.00 USD | 11,140.00 USD | 73,570.00 USD |
| `1D` | `8.58` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 87,680.00 USD | 21,440.00 USD | 39,900.00 USD |
| `7D` | `8.58` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 541,170.00 USD | 164,810.00 USD | 45,310.00 USD |
| `1D` | `8.59` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 70,460.00 USD | 29,830.00 USD | 25,420.00 USD |
| `1D` | `8.60` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 68,090.00 USD | 23,230.00 USD | 39,600.00 USD |
| `7D` | `8.60` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 75,040.00 USD | 39,160.00 USD | 206,190.00 USD |
| `1D` | `8.61` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 35,340.00 USD | 12,770.00 USD | 26,950.00 USD |
| `1D` | `8.62` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 102,610.00 USD | 23,160.00 USD | 30,620.00 USD |
| `7D` | `8.62` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 13,680.00 USD | 43,670.00 USD | 78,730.00 USD |
| `1D` | `8.63` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 77,860.00 USD | 18,340.00 USD | 9,310.00 USD |
| `1D` | `8.64` | 908,110.00 USD | 0.00 USD | 908,110.00 USD | 78,760.00 USD | 11,790.00 USD | 11,100.00 USD |
| `7D` | `8.64` | 971,000.00 USD | 0.00 USD | 971,000.00 USD | 127,570.00 USD | 5,680.00 USD | 10,650.00 USD |
| `1D` | `8.65` | 806,460.00 USD | 0.00 USD | 806,460.00 USD | 50,810.00 USD | 31,510.00 USD | 24,360.00 USD |
| `1D` | `8.66` | 699,780.00 USD | 0.00 USD | 699,780.00 USD | 66,700.00 USD | 26,760.00 USD | 15,000.00 USD |
| `7D` | `8.66` | 827,110.00 USD | 0.00 USD | 827,110.00 USD | 55,380.00 USD | 16,520.00 USD | 37,490.00 USD |
| `1D` | `8.67` | 591,320.00 USD | 0.00 USD | 591,320.00 USD | 33,710.00 USD | 5,480.00 USD | 23,170.00 USD |
| `1D` | `8.68` | 528,960.00 USD | 0.00 USD | 528,960.00 USD | 21,030.00 USD | 0.00 USD | 56.84 USD |
| `7D` | `8.68` | 717,720.00 USD | 0.00 USD | 717,720.00 USD | 93,990.00 USD | 24,870.00 USD | 173,670.00 USD |
| `1D` | `8.69` | 507,870.00 USD | 0.00 USD | 507,870.00 USD | 18,040.00 USD | 5,700.00 USD | 22,180.00 USD |
| `1D` | `8.70` | 461,960.00 USD | 0.00 USD | 461,960.00 USD | 34,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.70` | 425,190.00 USD | 0.00 USD | 425,190.00 USD | 0.00 USD | 12,790.00 USD | 22,290.00 USD |
| `1D` | `8.71` | 427,590.00 USD | 0.00 USD | 427,590.00 USD | 18,250.00 USD | 11,690.00 USD | 18,980.00 USD |
| `1D` | `8.73` | 378,660.00 USD | 0.00 USD | 378,660.00 USD | 44,990.00 USD | 2,720.00 USD | 5,120.00 USD |
| `1D` | `8.74` | 325,830.00 USD | 0.00 USD | 325,830.00 USD | 0.00 USD | 7,720.00 USD | 0.00 USD |
| `7D` | `8.74` | 390,110.00 USD | 0.00 USD | 390,110.00 USD | 144,660.00 USD | 19,690.00 USD | 56,610.00 USD |
| `1D` | `8.75` | 318,110.00 USD | 0.00 USD | 318,110.00 USD | 32,080.00 USD | 8,290.00 USD | 35,830.00 USD |
| `1D` | `8.76` | 241,920.00 USD | 0.00 USD | 241,920.00 USD | 78,530.00 USD | 15,050.00 USD | 0.00 USD |
| `7D` | `8.76` | 169,160.00 USD | 0.00 USD | 169,160.00 USD | 26,810.00 USD | 0.00 USD | 22,400.00 USD |
| `1D` | `8.77` | 148,340.00 USD | 0.00 USD | 148,340.00 USD | 54,300.00 USD | 8,510.00 USD | 25,720.00 USD |
| `1D` | `8.78` | 59,810.00 USD | 0.00 USD | 59,810.00 USD | 19,230.00 USD | 0.00 USD | 9,880.00 USD |
| `7D` | `8.78` | 119,940.00 USD | 0.00 USD | 119,940.00 USD | 0.00 USD | 0.00 USD | 58,840.00 USD |
| `1D` | `8.79` | 30,700.00 USD | 0.00 USD | 30,700.00 USD | 13,010.00 USD | 12,000.00 USD | 0.00 USD |
| `1D` | `8.80` | 5,690.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD |
| `7D` | `8.80` | 61,100.00 USD | 0.00 USD | 61,100.00 USD | 27,360.00 USD | 33,750.00 USD | 0.00 USD |
| `1D` | `8.81` | 10,950.00 USD | 10,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,950.00 USD |
| `1D` | `8.81` | 21,900.00 USD | 21,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,950.00 USD |
| `7D` | `8.81` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.82` | 21,290.00 USD | 21,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,290.00 USD |
| `1D` | `8.84` | 90,540.00 USD | 90,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 68,640.00 USD |
| `1D` | `8.86` | 157,910.00 USD | 157,910.00 USD | 0.00 USD | 67,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.90` | 235,680.00 USD | 235,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 77,770.00 USD |
| `7D` | `8.90` | 136,770.00 USD | 136,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 115,480.00 USD |
| `1D` | `8.92` | 247,240.00 USD | 247,240.00 USD | 0.00 USD | 8,060.00 USD | 0.00 USD | 3,500.00 USD |
| `1D` | `8.98` | 260,290.00 USD | 260,290.00 USD | 0.00 USD | 0.00 USD | 5,550.00 USD | 7,490.00 USD |
| `1D` | `8.99` | 328,540.00 USD | 328,540.00 USD | 0.00 USD | 40,450.00 USD | 27,810.00 USD | 0.00 USD |
| `1D` | `9.00` | 338,640.00 USD | 338,640.00 USD | 0.00 USD | 10,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.00` | 363,280.00 USD | 363,280.00 USD | 0.00 USD | 215,150.00 USD | 11,360.00 USD | 0.00 USD |
| `1D` | `9.01` | 350,010.00 USD | 350,010.00 USD | 0.00 USD | 1,080.00 USD | 5,120.00 USD | 5,170.00 USD |
| `1D` | `9.02` | 416,420.00 USD | 416,420.00 USD | 0.00 USD | 30,650.00 USD | 30,950.00 USD | 4,810.00 USD |
| `7D` | `9.02` | 454,060.00 USD | 454,060.00 USD | 0.00 USD | 34,650.00 USD | 56,120.00 USD | 0.00 USD |
| `1D` | `9.03` | 496,860.00 USD | 496,860.00 USD | 0.00 USD | 29,210.00 USD | 28,060.00 USD | 23,170.00 USD |
| `1D` | `9.04` | 508,310.00 USD | 508,310.00 USD | 0.00 USD | 0.00 USD | 4,810.00 USD | 6,640.00 USD |
| `7D` | `9.04` | 579,990.00 USD | 579,990.00 USD | 0.00 USD | 36,040.00 USD | 74,750.00 USD | 15,140.00 USD |
| `1D` | `9.05` | 576,610.00 USD | 576,610.00 USD | 0.00 USD | 3,520.00 USD | 26,530.00 USD | 38,250.00 USD |
| `1D` | `9.06` | 627,940.00 USD | 627,940.00 USD | 0.00 USD | 27,120.00 USD | 2,420.00 USD | 21,790.00 USD |
| `7D` | `9.06` | 639,700.00 USD | 639,700.00 USD | 0.00 USD | 5,610.00 USD | 14,960.00 USD | 39,130.00 USD |
| `1D` | `9.07` | 691,950.00 USD | 691,950.00 USD | 0.00 USD | 14,580.00 USD | 22,140.00 USD | 27,290.00 USD |
| `1D` | `9.08` | 733,570.00 USD | 733,570.00 USD | 0.00 USD | 1,260.00 USD | 6,490.00 USD | 33,870.00 USD |
| `7D` | `9.08` | 716,750.00 USD | 716,750.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD |
| `1D` | `9.09` | 892,130.00 USD | 892,130.00 USD | 0.00 USD | 99,950.00 USD | 17,120.00 USD | 41,490.00 USD |
| `1D` | `9.10` | 995,780.00 USD | 995,780.00 USD | 0.00 USD | 66,840.00 USD | 22,440.00 USD | 14,370.00 USD |
| `7D` | `9.10` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 797,340.00 USD | 35,760.00 USD | 325,210.00 USD |
| `1D` | `9.11` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 51,780.00 USD | 9,610.00 USD | 49,760.00 USD |
| `1D` | `9.12` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 106,750.00 USD | 31,620.00 USD | 6,270.00 USD |
| `7D` | `9.12` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 490,020.00 USD | 24,170.00 USD | 479,410.00 USD |
| `1D` | `9.13` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 84,020.00 USD | 20,120.00 USD | 40,100.00 USD |
| `1D` | `9.14` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 33,890.00 USD | 8,440.00 USD | 27,230.00 USD |
| `7D` | `9.14` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 536,560.00 USD | 18,540.00 USD | 479,710.00 USD |
| `1D` | `9.15` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 57,880.00 USD | 22,150.00 USD | 22,630.00 USD |
| `1D` | `9.16` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 63,210.00 USD | 17,550.00 USD | 27,740.00 USD |
| `7D` | `9.16` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 358,370.00 USD | 44,360.00 USD | 195,800.00 USD |
| `1D` | `9.17` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 94,110.00 USD | 18,740.00 USD | 55,730.00 USD |
| `1D` | `9.18` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 151,850.00 USD | 40,170.00 USD | 60,730.00 USD |
| `7D` | `9.18` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 549,130.00 USD | 162,460.00 USD | 263,140.00 USD |
| `1D` | `9.19` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 94,190.00 USD | 40,200.00 USD | 17,030.00 USD |
| `1D` | `9.20` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 106,980.00 USD | 10,810.00 USD | 65,640.00 USD |
| `7D` | `9.20` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 520,860.00 USD | 120,080.00 USD | 238,640.00 USD |
| `1D` | `9.21` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 39,120.00 USD | 3,470.00 USD | 6,900.00 USD |
| `1D` | `9.22` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 93,870.00 USD | 10,040.00 USD | 11,100.00 USD |
| `7D` | `9.22` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 585,170.00 USD | 140,390.00 USD | 416,230.00 USD |
| `1D` | `9.23` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 57,020.00 USD | 3,310.00 USD | 33,950.00 USD |
| `1D` | `9.24` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 31,050.00 USD | 1,250.00 USD | 0.00 USD |
| `7D` | `9.24` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 316,220.00 USD | 52,090.00 USD | 174,910.00 USD |
| `1D` | `9.25` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 18,710.00 USD | 17,700.00 USD | 9,510.00 USD |
| `1D` | `9.26` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 16,250.00 USD | 1,210.00 USD | 0.00 USD |
| `7D` | `9.26` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 273,920.00 USD | 96,980.00 USD | 60,730.00 USD |
| `1D` | `9.27` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 22,870.00 USD | 13,170.00 USD | 2,560.00 USD |
| `1D` | `9.28` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 20,250.00 USD | 3,860.00 USD | 4,200.00 USD |
| `7D` | `9.28` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 428,160.00 USD | 103,490.00 USD | 170,610.00 USD |
| `1D` | `9.29` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 48,940.00 USD | 15,680.00 USD | 17,930.00 USD |
| `1D` | `9.30` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 49,420.00 USD | 13,550.00 USD | 6,790.00 USD |
| `7D` | `9.30` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 199,810.00 USD | 97,780.00 USD | 262,830.00 USD |
| `1D` | `9.31` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 39,620.00 USD | 4,250.00 USD | 25,510.00 USD |
| `1D` | `9.32` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 9,610.00 USD | 2,530.00 USD | 10,830.00 USD |
| `7D` | `9.32` | 10,400,000.00 USD | 10,400,000.00 USD | 0.00 USD | 271,660.00 USD | 59,310.00 USD | 337,940.00 USD |
| `1D` | `9.33` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 16,620.00 USD | 6,000.00 USD | 15,710.00 USD |
| `1D` | `9.34` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 15,860.00 USD | 4,190.00 USD | 12,940.00 USD |
| `7D` | `9.34` | 10,730,000.00 USD | 10,730,000.00 USD | 0.00 USD | 203,440.00 USD | 53,150.00 USD | 70,360.00 USD |
| `1D` | `9.35` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 28,980.00 USD | 3,810.00 USD | 24,920.00 USD |
| `1D` | `9.36` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 66,220.00 USD | 13,630.00 USD | 25,050.00 USD |
| `7D` | `9.36` | 11,170,000.00 USD | 11,170,000.00 USD | 0.00 USD | 247,120.00 USD | 78,550.00 USD | 112,550.00 USD |
| `1D` | `9.37` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 36,610.00 USD | 13,410.00 USD | 6,010.00 USD |
| `1D` | `9.38` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 47,540.00 USD | 4,040.00 USD | 27,030.00 USD |
| `7D` | `9.38` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 383,530.00 USD | 55,400.00 USD | 85,250.00 USD |
| `1D` | `9.39` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 16,910.00 USD | 1,730.00 USD | 3,240.00 USD |
| `1D` | `9.40` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 44,280.00 USD | 1,210.00 USD | 12.64 USD |
| `7D` | `9.40` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 234,760.00 USD | 58,130.00 USD | 153,100.00 USD |
| `1D` | `9.41` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 29,700.00 USD | 1,660.00 USD | 16,970.00 USD |
| `1D` | `9.42` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 10,620.00 USD | 622.99 USD | 4,030.00 USD |
| `7D` | `9.42` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 176,920.00 USD | 44,410.00 USD | 84,120.00 USD |
| `1D` | `9.43` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 10,390.00 USD | 6,940.00 USD | 12,410.00 USD |
| `1D` | `9.44` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 1,500.00 USD | 0.00 USD | 48.84 USD |
| `7D` | `9.44` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 41,250.00 USD | 19,420.00 USD | 56,670.00 USD |
| `1D` | `9.45` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 1,380.00 USD | 4,940.00 USD | 2,430.00 USD |
| `1D` | `9.46` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 1,320.00 USD | 4,580.00 USD | 0.00 USD |
| `7D` | `9.46` | 12,750,000.00 USD | 12,750,000.00 USD | 0.00 USD | 136,670.00 USD | 29,830.00 USD | 19,460.00 USD |
| `1D` | `9.47` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 18,220.00 USD | 6,870.00 USD | 192.20 USD |
| `1D` | `9.48` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 1,510.00 USD | 0.00 USD | 5,190.00 USD |
| `7D` | `9.48` | 12,820,000.00 USD | 12,820,000.00 USD | 0.00 USD | 12,180.00 USD | 30,160.00 USD | 25,250.00 USD |
| `1D` | `9.49` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 21,080.00 USD | 572.85 USD | 5,600.00 USD |
| `1D` | `9.50` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 11,990.00 USD | 3,160.00 USD | 6,320.00 USD |
| `7D` | `9.50` | 13,000,000.00 USD | 13,000,000.00 USD | 0.00 USD | 69,270.00 USD | 33,210.00 USD | 83,550.00 USD |
| `1D` | `9.51` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 295.05 USD | 0.00 USD | 124.70 USD |
| `1D` | `9.52` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 17,180.00 USD | 3,070.00 USD | 5,400.00 USD |
| `7D` | `9.52` | 13,190,000.00 USD | 13,190,000.00 USD | 0.00 USD | 102,150.00 USD | 29,320.00 USD | 51,740.00 USD |
| `1D` | `9.53` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 18,780.00 USD | 4,560.00 USD | 0.00 USD |
| `1D` | `9.54` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 5,910.00 USD | 1,470.00 USD | 2,930.00 USD |
| `7D` | `9.54` | 13,410,000.00 USD | 13,410,000.00 USD | 0.00 USD | 192,090.00 USD | 27,650.00 USD | 930.52 USD |
| `1D` | `9.55` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 2,910.00 USD | 6,330.00 USD | 3,100.00 USD |
| `1D` | `9.56` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 5,060.00 USD | 1,280.00 USD | 2,530.00 USD |
| `7D` | `9.56` | 13,530,000.00 USD | 13,530,000.00 USD | 0.00 USD | 89,210.00 USD | 5,260.00 USD | 32,680.00 USD |
| `1D` | `9.57` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 1,370.00 USD | 3,100.00 USD | 4,960.00 USD |
| `1D` | `9.58` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 1,290.00 USD | 563.17 USD | 7,730.00 USD |
| `7D` | `9.58` | 13,610,000.00 USD | 13,610,000.00 USD | 0.00 USD | 35,340.00 USD | 16,980.00 USD | 21,580.00 USD |
| `1D` | `9.59` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 5,050.00 USD | 1,250.00 USD | 1,170.00 USD |
| `1D` | `9.60` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 11,210.00 USD | 424.36 USD | 11,260.00 USD |
| `7D` | `9.60` | 13,690,000.00 USD | 13,690,000.00 USD | 0.00 USD | 38,740.00 USD | 10,820.00 USD | 33,120.00 USD |
| `1D` | `9.61` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD |
| `1D` | `9.62` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.62` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 70,470.00 USD | 13,850.00 USD | 17,600.00 USD |
| `1D` | `9.63` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 10,190.00 USD | 4,370.00 USD | 1,150.00 USD |
| `1D` | `9.64` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 5,830.00 USD | 0.00 USD | 3,410.00 USD |
| `7D` | `9.64` | 13,890,000.00 USD | 13,890,000.00 USD | 0.00 USD | 61,870.00 USD | 17,650.00 USD | 19,900.00 USD |
| `1D` | `9.65` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 5,960.00 USD | 4,150.00 USD | 1,740.00 USD |
| `1D` | `9.66` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 8,930.00 USD | 3,480.00 USD | 5,760.00 USD |
| `7D` | `9.66` | 13,970,000.00 USD | 13,970,000.00 USD | 0.00 USD | 37,340.00 USD | 21,280.00 USD | 18,480.00 USD |
| `1D` | `9.67` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 2,990.00 USD | 0.00 USD | 2,310.00 USD |
| `1D` | `9.68` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 13,160.00 USD | 2,950.00 USD | 3,970.00 USD |
| `7D` | `9.68` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 68,230.00 USD | 20,310.00 USD | 34,130.00 USD |
| `1D` | `9.69` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 7,960.00 USD | 2,710.00 USD | 0.00 USD |
| `1D` | `9.70` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 7,590.00 USD | 4,150.00 USD | 1,730.00 USD |
| `7D` | `9.70` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 79,760.00 USD | 12,990.00 USD | 31,760.00 USD |
| `1D` | `9.71` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 74.90 USD | 5,170.00 USD | 3,500.00 USD |
| `1D` | `9.72` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 2,760.00 USD | 3,170.00 USD | 57.27 USD |
| `7D` | `9.72` | 14,320,000.00 USD | 14,320,000.00 USD | 0.00 USD | 71,790.00 USD | 6,920.00 USD | 26,830.00 USD |
| `1D` | `9.74` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 5,250.00 USD | 0.00 USD | 2,280.00 USD |
| `7D` | `9.74` | 14,360,000.00 USD | 14,360,000.00 USD | 0.00 USD | 10,330.00 USD | 7,200.00 USD | 19,560.00 USD |
| `1D` | `9.75` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 42.61 USD |
| `1D` | `9.76` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD |
| `7D` | `9.76` | 14,460,000.00 USD | 14,460,000.00 USD | 0.00 USD | 35,520.00 USD | 12,480.00 USD | 52,240.00 USD |
| `1D` | `9.78` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD |
| `7D` | `9.78` | 14,540,000.00 USD | 14,540,000.00 USD | 0.00 USD | 65,390.00 USD | 10,300.00 USD | 5,270.00 USD |
| `1D` | `9.79` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 5,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.80` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 6,870.00 USD | 770.83 USD | 9.39 USD |
| `7D` | `9.80` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 18,630.00 USD | 28,440.00 USD | 10,680.00 USD |
| `1D` | `9.81` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 8,600.00 USD | 1,540.00 USD | 1,670.00 USD |
| `1D` | `9.82` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 7,220.00 USD | 0.00 USD | 6,190.00 USD |
| `7D` | `9.82` | 14,830,000.00 USD | 14,830,000.00 USD | 0.00 USD | 121,860.00 USD | 27,860.00 USD | 86,290.00 USD |
| `1D` | `9.83` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 16,240.00 USD | 4,800.00 USD | 1,920.00 USD |
| `7D` | `9.84` | 14,860,000.00 USD | 14,860,000.00 USD | 0.00 USD | 9,730.00 USD | 7,850.00 USD | 14,230.00 USD |
| `1D` | `9.85` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 10,690.00 USD | 1,700.00 USD | 3,530.00 USD |
| `7D` | `9.86` | 15,000,000.00 USD | 15,000,000.00 USD | 0.00 USD | 59,550.00 USD | 2,210.00 USD | 72,010.00 USD |
| `7D` | `9.88` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 7,900.00 USD | 8,710.00 USD | 20,970.00 USD |
| `7D` | `9.90` | 15,130,000.00 USD | 15,130,000.00 USD | 0.00 USD | 55,970.00 USD | 19,700.00 USD | 14,360.00 USD |
| `7D` | `9.92` | 15,170,000.00 USD | 15,170,000.00 USD | 0.00 USD | 27,710.00 USD | 10,810.00 USD | 9,370.00 USD |
| `7D` | `9.94` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 69,320.00 USD | 11,150.00 USD | 39,810.00 USD |
| `7D` | `9.96` | 15,340,000.00 USD | 15,340,000.00 USD | 0.00 USD | 29,800.00 USD | 1,360.00 USD | 11,160.00 USD |
| `7D` | `9.98` | 15,360,000.00 USD | 15,360,000.00 USD | 0.00 USD | 840.10 USD | 4,150.00 USD | 18,990.00 USD |
| `7D` | `10.00` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 6,790.00 USD | 0.00 USD |
| `7D` | `10.02` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 15,960.00 USD | 0.00 USD | 5,890.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `379.84M` | Total OI Tokens: `43,136,524.0 AVAX`
  * 1h OI Change: `-1.18%` | 4h OI Change: `-1.33%` | 24h OI Change: `-3.03%`
  * Exchange Breakdown: Binance=`89.03M` | Bybit=`59.17M` | OKX=`12.71M` | Hyperliquid=`17.52M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.72K` | Last 24h: `33.77K` | Last 3d: `72.05K` | Last 7d: `92.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0070%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0073%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `43.80%` | `56.20%` | `0.78` | 3,900,000.00 USD |
| `15M` | `Binance` | `35.5%` | `64.5%` | `0.55` | 911,110.00 USD |
| `15M` | `OKX` | `24.71%` | `75.29%` | `0.33` | 313,970.00 USD |
| `15M` | `Bybit` | `30.66%` | `69.34%` | `0.44` | 181,610.00 USD |
| `15M` | `KuCoin` | `0.9%` | `99.1%` | `0.01` | 389.46 USD |
| `15M` | `Gate` | `62.93%` | `37.07%` | `1.70` | 21,690.00 USD |
| `15M` | `Bitget` | `47.61%` | `52.39%` | `0.91` | 67,160.00 USD |
| `15M` | `BingX` | `53.53%` | `46.47%` | `1.15` | 359,210.00 USD |
| `15M` | `MEXC` | `53%` | `47%` | `1.13` | 1,720,000.00 USD |
| `15M` | `Bitunix` | `63.65%` | `36.35%` | `1.75` | 71,400.00 USD |
| `15M` | `Hyperliquid` | `57.99%` | `42.01%` | `1.38` | 11,330.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.36%` | `50.64%` | `0.97` | 64,210.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 146,750.00 USD |
| `15M` | `HTX` | `35.25%` | `64.75%` | `0.54` | 303.96 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `68.5%` | `31.5%` | `2.17` | 20,410.00 USD |
| `15M` | `Aster` | `36.68%` | `63.32%` | `0.58` | 229.67 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `37.13%` | `62.87%` | `0.59` | 9,590.00 USD |
| `15M` | `Whale Positions` | `35.5%` | `64.5%` | `0.55` | 911,110.00 USD |
| `15M` | `Global Accounts` | `43.80%` | `56.20%` | `0.78` | 3,900,000.00 USD |
| `1H` | `AVAX` | `51.67%` | `48.33%` | `1.07` | 20,950,000.00 USD |
| `1H` | `Binance` | `62.81%` | `37.19%` | `1.69` | 6,030,000.00 USD |
| `1H` | `OKX` | `48.05%` | `51.95%` | `0.92` | 1,400,000.00 USD |
| `1H` | `Bybit` | `76.91%` | `23.09%` | `3.33` | 1,480,000.00 USD |
| `1H` | `KuCoin` | `45.12%` | `54.88%` | `0.82` | 117,480.00 USD |
| `1H` | `Gate` | `50.9%` | `49.1%` | `1.04` | 132,980.00 USD |
| `1H` | `Bitget` | `83%` | `17%` | `4.88` | 499,360.00 USD |
| `1H` | `BingX` | `51.16%` | `48.84%` | `1.05` | 889,170.00 USD |
| `1H` | `MEXC` | `57.85%` | `42.15%` | `1.37` | 7,860,000.00 USD |
| `1H` | `Bitunix` | `64.37%` | `35.63%` | `1.81` | 590,730.00 USD |
| `1H` | `Hyperliquid` | `83.02%` | `16.98%` | `4.89` | 496,840.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.03%` | `49.97%` | `1.00` | 548,420.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `18.64%` | `81.36%` | `0.23` | 718,450.00 USD |
| `1H` | `HTX` | `55.53%` | `44.47%` | `1.25` | 1,750.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `47.58%` | `52.42%` | `0.91` | 148,920.00 USD |
| `1H` | `Aster` | `13.48%` | `86.52%` | `0.16` | 2,320.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `5%` | `95%` | `0.05` | 24,260.00 USD |
| `1H` | `Whale Positions` | `62.81%` | `37.19%` | `1.69` | 6,030,000.00 USD |
| `1H` | `Global Accounts` | `51.67%` | `48.33%` | `1.07` | 20,950,000.00 USD |
| `4H` | `AVAX` | `44.56%` | `55.44%` | `0.80` | 11,510,000.00 USD |
| `4H` | `Binance` | `52.17%` | `47.83%` | `1.09` | 4,110,000.00 USD |
| `4H` | `OKX` | `44.76%` | `55.24%` | `0.81` | 718,840.00 USD |
| `4H` | `Bybit` | `52.4%` | `47.6%` | `1.10` | 541,110.00 USD |
| `4H` | `KuCoin` | `48.96%` | `51.04%` | `0.96` | 269,660.00 USD |
| `4H` | `Gate` | `58.51%` | `41.49%` | `1.41` | 286,980.00 USD |
| `4H` | `Bitget` | `54.19%` | `45.81%` | `1.18` | 147,140.00 USD |
| `4H` | `BingX` | `25.02%` | `74.98%` | `0.33` | 1,100,000.00 USD |
| `4H` | `MEXC` | `62.19%` | `37.81%` | `1.64` | 149,570.00 USD |
| `4H` | `Bitunix` | `51.42%` | `48.58%` | `1.06` | 120,620.00 USD |
| `4H` | `Hyperliquid` | `82.65%` | `17.35%` | `4.76` | 377,750.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.13%` | `49.87%` | `1.01` | 1,790,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `10.41%` | `89.59%` | `0.12` | 1,530,000.00 USD |
| `4H` | `HTX` | `53.8%` | `46.2%` | `1.16` | 195,270.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `77.85%` | `22.15%` | `3.51` | 95,790.00 USD |
| `4H` | `Aster` | `21.05%` | `78.95%` | `0.27` | 8,790.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `27.7%` | `72.3%` | `0.38` | 63,420.00 USD |
| `4H` | `Whale Positions` | `52.17%` | `47.83%` | `1.09` | 4,110,000.00 USD |
| `4H` | `Global Accounts` | `44.56%` | `55.44%` | `0.80` | 11,510,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `8.95` | `8.95` | `8.95` | `8.96` | `8.93` | 786,504.93 USD | 221,063.85 USD | 565,441.08 USD | -344,377.23 USD | `-43.79%` | `0B / 11S` |
| `0:00 UTC` | `8.93` | `8.93` | `8.93` | `8.96` | `8.91` | 1,932,405.67 USD | 423,821.82 USD | 1,508,583.84 USD | -1,084,762.02 USD | `-56.14%` | `2B / 26S` |
| `5:00 UTC` | `8.91` | `8.92` | `8.91` | `8.94` | `8.90` | 1,295,523.82 USD | 616,181.90 USD | 679,341.92 USD | -63,160.02 USD | `-4.88%` | `3B / 6S` |
| `0:00 UTC` | `8.94` | `8.90` | `8.94` | `8.94` | `8.85` | 1,871,719.04 USD | 766,811.36 USD | 1,104,907.68 USD | -338,096.31 USD | `-18.06%` | `8B / 28S` |
| `5:00 UTC` | `8.85` | `8.85` | `8.85` | `8.87` | `8.82` | 1,418,137.84 USD | 651,843.02 USD | 766,294.83 USD | -114,451.81 USD | `-8.07%` | `11B / 12S` |
| `0:00 UTC` | `8.87` | `8.87` | `8.87` | `8.88` | `8.86` | 651,856.32 USD | 369,195.26 USD | 282,661.06 USD | 86,534.20 USD | `+13.28%` | `5B / 4S` |
| `5:00 UTC` | `8.84` | `8.86` | `8.84` | `8.89` | `8.84` | 682,076.12 USD | 288,770.26 USD | 393,305.86 USD | -104,535.61 USD | `-15.33%` | `9B / 13S` |
| `0:00 UTC` | `8.81` | `8.81` | `8.81` | `8.84` | `8.80` | 1,762,248.06 USD | 773,632.57 USD | 988,615.48 USD | -214,982.91 USD | `-12.20%` | `7B / 6S` |
| `5:00 UTC` | `8.84` | `8.83` | `8.84` | `8.86` | `8.79` | 750,878.19 USD | 458,225.53 USD | 292,652.66 USD | 165,572.87 USD | `+22.05%` | `19B / 3S` |
| `0:00 UTC` | `8.82` | `8.82` | `8.82` | `8.84` | `8.80` | 503,349.03 USD | 235,599.90 USD | 267,749.13 USD | -32,149.22 USD | `-6.39%` | `5B / 5S` |

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
| `5m` | -5,630.00 USD | 46,590.00 USD | **`ACCUMULATION`** |
| `15m` | -10,270.00 USD | 64,350.00 USD | **`ACCUMULATION`** |
| `30m` | -31,400.00 USD | 383,090.00 USD | **`ACCUMULATION`** |
| `1h` | 64,310.00 USD | -60,150.00 USD | **`ACCUMULATION`** |
| `2h` | -69,890.00 USD | -1,280,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -43,940.00 USD | -3,860,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 220,560.00 USD | -3,070,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 70,080.00 USD | -3,340,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -75,950.00 USD | -2,830,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -194,900.00 USD | -4,380,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,690,000.00 USD | -42,780,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -52,860,000.00 USD | -273,380,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-5.63K` | 15m=`-10.27K` | 1h=`+64.31K` | 24h=`-194.90K`
* Futures Capital Netflows: 5m=`+46.59K` | 15m=`+64.35K` | 1h=`-60.15K` | 24h=`-4.38M`
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
  * `2026-10-30 00:17:29 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:38:29 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:40:29 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:40:29 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:40:29 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `7.32` (Risk Distance: `1.26` pts)
  * +2.5R Take Profit: `11.73`
  * Mathematical Lot Sizing: **`7.93 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.91` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `10.17` (Risk Distance: `1.26` pts)
  * +2.5R Take Profit: `5.76`
  * Mathematical Lot Sizing: **`7.93 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.88`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
