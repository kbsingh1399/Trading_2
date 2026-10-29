# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:27:38 IST` (`2026-10-29 20:57:38 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.37` | **Live Ask Quote**: `8.41` | **Mid Price**: `8.39`
- **Spread Points**: `4.00` | **Spread BPS**: `47.68 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.75` | VWAP Z-Score: `-2.79` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0807` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `19.97` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `9.14` | Lower -3.00σ Band: `8.35`
  * Upper +2.51σ Band: `9.07` | Lower -2.51σ Band: `8.42`
  * Upper +2.01σ Band: `9.01` | Lower -2.01σ Band: `8.48`
  * Upper +2.00σ Band: `9.01` | Lower -2.00σ Band: `8.48`
  * Upper +1.28σ Band: `8.91` | Lower -1.28σ Band: `8.58`
  * Upper +1.00σ Band: `8.88` | Lower -1.00σ Band: `8.61`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.71` | EMA-20=`8.78` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.79` (Slope: `+0.0000`) | EMA-100=`8.80`
  * Institutional Anchors: EMA-144=`8.81` | EMA-200=`8.82` (Slope: `-0.0778`) | EMA-233=`8.82`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`8.37` | Weekly High=`9.14` | Weekly Low=`8.37`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.90` (Distance: `-5.66%`)
  * Point of Control (POC) = `8.74` (Distance: `-3.89%`)
  * Value Area Low (VAL) = `8.55` (Distance: `-1.74%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`9.02` | POC=`8.99` | VAL=`8.86`
  * Prior Day Extremes: PDH=`9.14` | PDL=`8.76` | PDC=`8.99`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`8.96` | Weekly POC=`8.91` | Weekly VAL=`8.74`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`9.04` | Low=`8.53`
  * London Session (08:00-16:00 UTC): High=`8.81` | Low=`8.59`
  * New York Session (13:00-21:00 UTC): High=`9.06` | Low=`8.68`
  * Initial Balance (First Hour): IB High=`8.78` | IB Low=`8.65`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.36` - `8.42`
  * Optimal Trade Entry (OTE 0.705): `8.41`
  * Structural Invalidation Anchor (0.786): `8.46`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.40` | `8.41` | `8.25` | `8.35` | `1,317,990` | 10,978,235.09 USD | -2,615,252.38 USD | `-23.82%` | -10,467,625.13 USD | `-2.59` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `8.35` | `8.48` | `8.35` | `8.39` | `554,718` | 4,657,585.06 USD | -13,053.38 USD | `-0.28%` | -10,480,678.51 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `8.39` | `8.40` | `8.38` | `8.40` | `27,641` | 231,914.67 USD | 24,220.83 USD | `+10.44%` | -10,456,457.68 USD | `+0.37` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `8.74` | `8.78` | `8.73` | `8.73` | `239,615` | 2,097,434.25 USD | 675,324.06 USD | `+32.20%` | -3,783,973.65 USD | `+2.04` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `8.73` | `8.76` | `8.39` | `8.40` | `1,542,699` | 13,163,243.09 USD | -4,068,399.10 USD | `-30.91%` | -7,852,372.75 USD | `-4.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `8.40` | `8.48` | `8.25` | `8.39` | `1,899,679` | 15,862,108.75 USD | -2,603,312.47 USD | `-16.41%` | -10,455,685.23 USD | `-2.04` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `8.87` | `8.89` | `8.79` | `8.84` | `435,467` | 3,847,058.68 USD | -67,411.45 USD | `-1.75%` | -4,291,060.73 USD | `+0.32` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `8.84` | `8.87` | `8.80` | `8.85` | `249,668` | 2,205,666.85 USD | 221,936.79 USD | `+10.06%` | -4,069,123.94 USD | `+0.91` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `8.85` | `8.86` | `8.25` | `8.39` | `4,318,829` | 36,684,574.90 USD | -6,384,983.17 USD | `-17.41%` | -10,454,107.11 USD | `-4.09` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -2,154,015.33 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -4,666,010.97 USD | `-1.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.25` | `8.39` | `4,319,330` | 36,688,779.80 USD | -6,389,188.08 USD | `-17.41%` | -11,055,199.05 USD | `-1.95` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `8.59` | `8.80` | `8.57` | `8.62` | `1,816,830` | 15,790,058.74 USD | 58,580.54 USD | `+0.37%` | -2,364,450.84 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -2,100,193.35 USD | `+0.79` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -2,154,015.33 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -4,666,010.97 USD | `-1.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.25` | `8.39` | `4,319,330` | 36,688,779.80 USD | -6,389,188.08 USD | `-17.41%` | -11,055,199.05 USD | `-1.95` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BUY` | `8.23` | `14495.9100` | 119,328.88 USD | 2,224,035.61 USD | `LARGE (>= USD 100K)` | `-1.99%` | `0x71d0e11ebb` |
| `BUY` | `8.24` | `153.7500` | 1,267.01 USD | 4,589,117.40 USD | `STANDARD` | `-1.88%` | `0x31ca8395cf` |
| `BUY` | `8.25` | `400.5300` | 3,304.93 USD | 4,430,063.84 USD | `STANDARD` | `-1.75%` | `0x14f8e04290` |
| `BUY` | `8.25` | `161.6200` | 1,333.20 USD | 4,583,952.02 USD | `STANDARD` | `-1.78%` | `0x010461c14e` |
| `BUY` | `8.26` | `74.3000` | 613.68 USD | 4,689,387.22 USD | `STANDARD` | `-1.66%` | `0x32a5bf2d10` |
| `BUY` | `8.27` | `14963.3600` | 123,718.56 USD | 1,740,892.70 USD | `LARGE (>= USD 100K)` | `-1.56%` | `0xecb63caa47` |
| `BUY` | `8.27` | `10678.3400` | 88,270.36 USD | 3,127,139.47 USD | `MEDIUM (>= USD 25K)` | `-1.58%` | `0x71d0e11ebb` |
| `BUY` | `8.27` | `2297.8200` | 18,999.98 USD | 3,400,928.60 USD | `STANDARD` | `-1.55%` | `0x0efb38a5fa` |
| `BUY` | `8.27` | `2222.4400` | 18,380.25 USD | 3,476,047.46 USD | `STANDARD` | `-1.53%` | `0xd3943e4008` |
| `BUY` | `8.28` | `11255.0100` | 93,213.99 USD | 2,947,584.41 USD | `MEDIUM (>= USD 25K)` | `-1.39%` | `0xecb63caa47` |
| `BUY` | `8.28` | `315.7300` | 2,614.56 USD | 4,505,474.54 USD | `STANDARD` | `-1.40%` | `0x07fd993f0f` |
| `BUY` | `8.29` | `1929.1500` | 15,999.98 USD | 3,541,250.30 USD | `STANDARD` | `-1.25%` | `0x0efb38a5fa` |
| `BUY` | `8.29` | `82.9400` | 687.67 USD | 4,678,875.29 USD | `STANDARD` | `-1.28%` | `0x010461c14e` |
| `BUY` | `8.29` | `80.2400` | 665.08 USD | 4,683,581.28 USD | `STANDARD` | `-1.31%` | `0x31ca8395cf` |
| `BUY` | `8.30` | `14497.0200` | 120,374.56 USD | 2,104,706.72 USD | `LARGE (>= USD 100K)` | `-1.13%` | `0x71d0e11ebb` |
| `BUY` | `8.30` | `13797.0600` | 114,496.28 USD | 2,338,531.89 USD | `LARGE (>= USD 100K)` | `-1.19%` | `0xecb63caa47` |
| `BUY` | `8.30` | `1739.0900` | 14,431.49 USD | 3,570,797.93 USD | `STANDARD` | `-1.20%` | `0xd3943e4008` |
| `BUY` | `8.30` | `404.9300` | 3,359.26 USD | 4,426,758.91 USD | `STANDARD` | `-1.22%` | `0x14f8e04290` |
| `BUY` | `8.31` | `49113.5800` | 408,109.29 USD | 824,430.07 USD | `LARGE (>= USD 100K)` | `-1.06%` | `0x71cfa5e263` |
| `BUY` | `8.31` | `1359.8300` | 11,303.72 USD | 4,061,214.45 USD | `STANDARD` | `-1.03%` | `0x33ad48ed92` |
| `BUY` | `8.31` | `1330.5500` | 11,054.21 USD | 4,094,451.42 USD | `STANDARD` | `-1.08%` | `0xa38f19c4cc` |
| `BUY` | `8.32` | `12025.4100` | 100,111.54 USD | 2,854,370.42 USD | `LARGE (>= USD 100K)` | `-0.88%` | `0x881cd92459` |
| `BUY` | `8.32` | `8961.1600` | 74,513.84 USD | 3,359,928.65 USD | `MEDIUM (>= USD 25K)` | `-0.99%` | `0xecb63caa47` |
| `BUY` | `8.32` | `366.8200` | 3,050.33 USD | 4,489,079.71 USD | `STANDARD` | `-0.99%` | `0xdd4f66125d` |
| `BUY` | `8.33` | `14496.5000` | 120,732.65 USD | 1,984,332.17 USD | `LARGE (>= USD 100K)` | `-0.84%` | `0x71d0e11ebb` |
| `BUY` | `8.33` | `1440.2900` | 11,999.92 USD | 4,026,487.94 USD | `STANDARD` | `-0.80%` | `0x0efb38a5fa` |
| `BUY` | `8.33` | `404.9300` | 3,372.82 USD | 4,423,399.65 USD | `STANDARD` | `-0.83%` | `0x14f8e04290` |
| `BUY` | `8.33` | `107.6500` | 897.00 USD | 4,655,512.91 USD | `STANDARD` | `-0.79%` | `0x9d81a3adf8` |
| `BUY` | `8.33` | `107.6500` | 896.98 USD | 4,656,409.89 USD | `STANDARD` | `-0.79%` | `0x63f6411ca6` |
| `BUY` | `8.33` | `107.6300` | 896.75 USD | 4,657,306.64 USD | `STANDARD` | `-0.80%` | `0xf30120f048` |
| `BUY` | `8.33` | `107.5800` | 896.64 USD | 4,659,996.69 USD | `STANDARD` | `-0.76%` | `0xfd66e33095` |
| `BUY` | `8.33` | `107.6300` | 896.63 USD | 4,660,893.33 USD | `STANDARD` | `-0.81%` | `0xd0956a1eba` |
| `BUY` | `8.33` | `107.5800` | 896.53 USD | 4,661,789.85 USD | `STANDARD` | `-0.78%` | `0xea0e878d5d` |
| `BUY` | `8.33` | `107.6300` | 896.41 USD | 4,662,686.26 USD | `STANDARD` | `-0.83%` | `0xfd66e33095` |
| `BUY` | `8.33` | `107.6300` | 896.40 USD | 4,663,582.66 USD | `STANDARD` | `-0.84%` | `0x63f6411ca6` |
| `BUY` | `8.33` | `107.5800` | 896.32 USD | 4,664,478.98 USD | `STANDARD` | `-0.80%` | `0xa382fa9f4b` |
| `BUY` | `8.33` | `107.5800` | 896.11 USD | 4,665,375.09 USD | `STANDARD` | `-0.82%` | `0xd0956a1eba` |
| `BUY` | `8.33` | `107.5700` | 895.92 USD | 4,666,271.01 USD | `STANDARD` | `-0.83%` | `0xea0e878d5d` |
| `BUY` | `8.33` | `77.1100` | 642.30 USD | 4,687,508.73 USD | `STANDARD` | `-0.82%` | `0x31ca8395cf` |
| `BUY` | `8.34` | `1477.9500` | 12,327.88 USD | 4,002,488.05 USD | `STANDARD` | `-0.68%` | `0xd3943e4008` |
| `BUY` | `8.34` | `1334.2300` | 11,128.55 USD | 4,072,343.00 USD | `STANDARD` | `-0.69%` | `0xd3943e4008` |
| `BUY` | `8.34` | `1019.8700` | 8,510.10 USD | 4,247,823.68 USD | `STANDARD` | `-0.65%` | `0x33ad48ed92` |
| `BUY` | `8.34` | `366.8200` | 3,060.12 USD | 4,486,029.38 USD | `STANDARD` | `-0.67%` | `0xdd4f66125d` |
| `BUY` | `8.34` | `315.7300` | 2,632.56 USD | 4,500,242.63 USD | `STANDARD` | `-0.72%` | `0x07fd993f0f` |
| `BUY` | `8.34` | `239.1000` | 1,994.69 USD | 4,525,540.27 USD | `STANDARD` | `-0.67%` | `0x39bac00809` |
| `BUY` | `8.34` | `107.6500` | 897.41 USD | 4,653,718.72 USD | `STANDARD` | `-0.74%` | `0x53136b4a7c` |
| `BUY` | `8.34` | `107.6300` | 897.18 USD | 4,654,615.90 USD | `STANDARD` | `-0.75%` | `0x63f6411ca6` |
| `BUY` | `8.34` | `107.5800` | 896.74 USD | 4,658,203.39 USD | `STANDARD` | `-0.75%` | `0xa382fa9f4b` |
| `BUY` | `8.34` | `107.5700` | 896.67 USD | 4,659,100.06 USD | `STANDARD` | `-0.75%` | `0xea0e878d5d` |
| `BUY` | `8.34` | `88.7400` | 739.71 USD | 4,671,711.48 USD | `STANDARD` | `-0.75%` | `0x010461c14e` |
| `BUY` | `8.34` | `80.7300` | 673.03 USD | 4,681,580.15 USD | `STANDARD` | `-0.74%` | `0xd0956a1eba` |
| `BUY` | `8.35` | `12273.8200` | 102,470.44 USD | 2,654,146.76 USD | `LARGE (>= USD 100K)` | `-0.60%` | `0x71d0e11ebb` |
| `BUY` | `8.35` | `1663.1800` | 13,893.54 USD | 3,821,955.07 USD | `STANDARD` | `-0.54%` | `0x57d8e75f47` |
| `BUY` | `8.35` | `957.5900` | 7,999.99 USD | 4,264,089.79 USD | `STANDARD` | `-0.53%` | `0x0efb38a5fa` |
| `BUY` | `8.35` | `778.4800` | 6,502.49 USD | 4,308,060.37 USD | `STANDARD` | `-0.55%` | `0xa38f19c4cc` |
| `BUY` | `8.35` | `484.3300` | 4,042.61 USD | 4,394,619.90 USD | `STANDARD` | `-0.62%` | `0xcd7f60e943` |
| `BUY` | `8.35` | `231.2300` | 1,931.79 USD | 4,560,522.80 USD | `STANDARD` | `-0.53%` | `0x9d732bed51` |
| `BUY` | `8.35` | `231.2300` | 1,930.79 USD | 4,562,453.60 USD | `STANDARD` | `-0.58%` | `0x9d732bed51` |
| `BUY` | `8.35` | `231.2300` | 1,929.85 USD | 4,564,383.44 USD | `STANDARD` | `-0.63%` | `0x9d732bed51` |
| `BUY` | `8.36` | `1663.1800` | 13,909.01 USD | 3,780,258.81 USD | `STANDARD` | `-0.43%` | `0x57d8e75f47` |
| `BUY` | `8.36` | `1663.1800` | 13,904.85 USD | 3,794,163.66 USD | `STANDARD` | `-0.46%` | `0x57d8e75f47` |
| `BUY` | `8.36` | `1663.1800` | 13,897.86 USD | 3,808,061.53 USD | `STANDARD` | `-0.51%` | `0x57d8e75f47` |
| `BUY` | `8.36` | `1080.1000` | 9,033.42 USD | 4,204,402.34 USD | `STANDARD` | `-0.42%` | `0xd3943e4008` |
| `BUY` | `8.36` | `688.4000` | 5,754.54 USD | 4,343,467.39 USD | `STANDARD` | `-0.47%` | `0xecb63caa47` |
| `BUY` | `8.36` | `457.2700` | 3,824.97 USD | 4,402,480.05 USD | `STANDARD` | `-0.40%` | `0xa38f19c4cc` |
| `BUY` | `8.36` | `368.9700` | 3,083.85 USD | 4,479,903.67 USD | `STANDARD` | `-0.48%` | `0x2a72b57dea` |
| `BUY` | `8.36` | `366.8200` | 3,065.59 USD | 4,482,969.26 USD | `STANDARD` | `-0.49%` | `0xdd4f66125d` |
| `BUY` | `8.36` | `269.1900` | 2,249.97 USD | 4,517,260.82 USD | `STANDARD` | `-0.48%` | `0xa38f19c4cc` |
| `BUY` | `8.36` | `231.2300` | 1,933.73 USD | 4,556,658.23 USD | `STANDARD` | `-0.43%` | `0x9d732bed51` |
| `BUY` | `8.36` | `231.2300` | 1,932.78 USD | 4,558,591.02 USD | `STANDARD` | `-0.48%` | `0x9d732bed51` |
| `BUY` | `8.36` | `91.0800` | 761.06 USD | 4,670,220.09 USD | `STANDARD` | `-0.51%` | `0x31ca8395cf` |
| `BUY` | `8.36` | `79.9100` | 667.87 USD | 4,682,916.20 USD | `STANDARD` | `-0.49%` | `0x010461c14e` |
| `BUY` | `8.37` | `19820.4900` | 165,891.56 USD | 1,368,746.76 USD | `LARGE (>= USD 100K)` | `-0.35%` | `0x71d0e11ebb` |
| `BUY` | `8.37` | `1983.7000` | 16,601.39 USD | 3,509,250.33 USD | `STANDARD` | `-0.35%` | `0x08a49e7f71` |
| `BUY` | `8.37` | `1663.1800` | 13,925.64 USD | 3,738,512.00 USD | `STANDARD` | `-0.31%` | `0x57d8e75f47` |
| `BUY` | `8.37` | `1663.1800` | 13,920.98 USD | 3,752,432.98 USD | `STANDARD` | `-0.34%` | `0x57d8e75f47` |
| `BUY` | `8.37` | `1663.1800` | 13,916.82 USD | 3,766,349.81 USD | `STANDARD` | `-0.37%` | `0x57d8e75f47` |
| `BUY` | `8.37` | `1197.9600` | 10,032.44 USD | 4,175,837.87 USD | `STANDARD` | `-0.29%` | `0xaf9f722a67` |
| `BUY` | `8.37` | `988.1200` | 8,266.12 USD | 4,256,089.79 USD | `STANDARD` | `-0.40%` | `0xd3943e4008` |
| `BUY` | `8.37` | `913.8200` | 7,644.10 USD | 4,287,733.22 USD | `STANDARD` | `-0.40%` | `0xecb63caa47` |
| `BUY` | `8.37` | `874.7900` | 7,322.17 USD | 4,295,055.38 USD | `STANDARD` | `-0.34%` | `0xecb63caa47` |
| `BUY` | `8.37` | `672.8100` | 5,630.01 USD | 4,354,735.94 USD | `STANDARD` | `-0.37%` | `0x33ad48ed92` |
| `BUY` | `8.37` | `368.9700` | 3,087.39 USD | 4,476,819.82 USD | `STANDARD` | `-0.37%` | `0x2a72b57dea` |
| `BUY` | `8.37` | `231.2300` | 1,935.77 USD | 4,552,789.73 USD | `STANDARD` | `-0.32%` | `0x9d732bed51` |
| `BUY` | `8.37` | `231.2300` | 1,934.77 USD | 4,554,724.50 USD | `STANDARD` | `-0.37%` | `0x9d732bed51` |
| `BUY` | `8.37` | `179.8400` | 1,505.76 USD | 4,581,187.09 USD | `STANDARD` | `-0.31%` | `0x6ba889db7f` |
| `BUY` | `8.37` | `107.6500` | 901.36 USD | 4,646,513.69 USD | `STANDARD` | `-0.30%` | `0xea0e878d5d` |
| `BUY` | `8.37` | `107.6300` | 901.27 USD | 4,647,414.96 USD | `STANDARD` | `-0.30%` | `0x53136b4a7c` |
| `BUY` | `8.37` | `107.6100` | 901.20 USD | 4,648,316.16 USD | `STANDARD` | `-0.29%` | `0x9d81a3adf8` |
| `BUY` | `8.37` | `107.6500` | 901.18 USD | 4,649,217.34 USD | `STANDARD` | `-0.33%` | `0xa382fa9f4b` |
| `BUY` | `8.37` | `107.6500` | 901.15 USD | 4,650,118.49 USD | `STANDARD` | `-0.33%` | `0xd0956a1eba` |
| `BUY` | `8.37` | `107.6400` | 901.04 USD | 4,651,019.53 USD | `STANDARD` | `-0.33%` | `0x53136b4a7c` |
| `BUY` | `8.37` | `107.6300` | 900.90 USD | 4,651,920.43 USD | `STANDARD` | `-0.34%` | `0x53136b4a7c` |
| `BUY` | `8.37` | `107.6100` | 900.88 USD | 4,652,821.31 USD | `STANDARD` | `-0.32%` | `0xf30120f048` |
| `BUY` | `8.37` | `86.5900` | 725.04 USD | 4,674,631.97 USD | `STANDARD` | `-0.30%` | `0x31ca8395cf` |
| `BUY` | `8.37` | `79.2000` | 663.00 USD | 4,685,571.51 USD | `STANDARD` | `-0.33%` | `0x010461c14e` |
| `BUY` | `8.38` | `1537.3500` | 12,887.61 USD | 3,938,633.63 USD | `STANDARD` | `-0.19%` | `0x57d8e75f47` |
| `BUY` | `8.38` | `1537.3500` | 12,883.92 USD | 3,964,403.41 USD | `STANDARD` | `-0.22%` | `0x57d8e75f47` |
| `BUY` | `8.38` | `1537.3500` | 12,880.23 USD | 3,977,283.64 USD | `STANDARD` | `-0.24%` | `0x57d8e75f47` |
| `BUY` | `8.38` | `1537.3500` | 12,876.54 USD | 3,990,160.17 USD | `STANDARD` | `-0.27%` | `0x57d8e75f47` |
| `BUY` | `8.38` | `1197.9600` | 10,042.50 USD | 4,165,805.44 USD | `STANDARD` | `-0.19%` | `0xaf9f722a67` |
| `BUY` | `8.38` | `1051.3100` | 8,812.08 USD | 4,222,026.67 USD | `STANDARD` | `-0.20%` | `0x08a49e7f71` |
| `BUY` | `8.38` | `714.6200` | 5,985.94 USD | 4,326,112.46 USD | `STANDARD` | `-0.27%` | `0xecb63caa47` |
| `BUY` | `8.38` | `596.9700` | 4,999.92 USD | 4,364,735.83 USD | `STANDARD` | `-0.28%` | `0x0efb38a5fa` |
| `BUY` | `8.38` | `481.6400` | 4,035.18 USD | 4,398,655.08 USD | `STANDARD` | `-0.25%` | `0x7717a7a245` |
| `BUY` | `8.38` | `368.9700` | 3,093.15 USD | 4,467,550.27 USD | `STANDARD` | `-0.18%` | `0x2a72b57dea` |
| `BUY` | `8.38` | `368.9700` | 3,090.53 USD | 4,473,732.43 USD | `STANDARD` | `-0.27%` | `0x2a72b57dea` |
| `BUY` | `8.38` | `269.1200` | 2,256.22 USD | 4,515,010.85 USD | `STANDARD` | `-0.18%` | `0x33ad48ed92` |
| `BUY` | `8.38` | `231.2300` | 1,938.59 USD | 4,546,979.57 USD | `STANDARD` | `-0.18%` | `0x9d732bed51` |
| `BUY` | `8.38` | `231.2300` | 1,937.64 USD | 4,548,917.21 USD | `STANDARD` | `-0.23%` | `0x9d732bed51` |
| `BUY` | `8.38` | `231.2300` | 1,936.76 USD | 4,550,853.97 USD | `STANDARD` | `-0.27%` | `0x9d732bed51` |
| `BUY` | `8.38` | `179.8900` | 1,507.71 USD | 4,578,175.50 USD | `STANDARD` | `-0.21%` | `0x6ba889db7f` |
| `BUY` | `8.38` | `179.7600` | 1,505.83 USD | 4,579,681.33 USD | `STANDARD` | `-0.26%` | `0x6ba889db7f` |
| `BUY` | `8.38` | `137.5600` | 1,153.39 USD | 4,592,578.87 USD | `STANDARD` | `-0.17%` | `0xdd4f66125d` |
| `BUY` | `8.38` | `107.6500` | 902.46 USD | 4,641,102.32 USD | `STANDARD` | `-0.18%` | `0x63f6411ca6` |
| `BUY` | `8.38` | `107.6100` | 902.27 USD | 4,642,004.59 USD | `STANDARD` | `-0.17%` | `0xf30120f048` |
| `BUY` | `8.38` | `107.6500` | 902.18 USD | 4,642,906.77 USD | `STANDARD` | `-0.21%` | `0xf30120f048` |
| `BUY` | `8.38` | `107.6500` | 902.04 USD | 4,643,808.81 USD | `STANDARD` | `-0.23%` | `0xea0e878d5d` |
| `BUY` | `8.38` | `107.6300` | 901.81 USD | 4,644,710.62 USD | `STANDARD` | `-0.24%` | `0xd0956a1eba` |
| `BUY` | `8.38` | `107.6500` | 901.70 USD | 4,645,612.32 USD | `STANDARD` | `-0.27%` | `0xfd66e33095` |
| `BUY` | `8.38` | `80.7500` | 676.55 USD | 4,680,230.71 USD | `STANDARD` | `-0.24%` | `0x63f6411ca6` |
| `BUY` | `8.38` | `80.7500` | 676.41 USD | 4,680,907.13 USD | `STANDARD` | `-0.26%` | `0xd0956a1eba` |
| `BUY` | `8.38` | `60.3400` | 505.71 USD | 4,694,695.21 USD | `STANDARD` | `-0.21%` | `0x57d8e75f47` |
| `BID` | `8.39` | `123.5800` | 1,037.43 USD | 7,330.86 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.39` | `50.0000` | 419.73 USD | 7,750.59 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.39` | `154.0400` | 1,293.01 USD | 9,043.60 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.39` | `5.5700` | 46.75 USD | 9,090.36 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.39` | `107.5700` | 902.91 USD | 9,993.27 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.39` | `107.5800` | 902.98 USD | 10,896.25 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.39` | `1044.0700` | 8,763.40 USD | 19,659.65 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `8.39` | `16.0000` | 134.29 USD | 19,793.94 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.39` | `107.5800` | 902.88 USD | 20,696.81 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.39` | `82.0100` | 688.27 USD | 21,385.08 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.39` | `1905.6200` | 15,992.73 USD | 37,377.81 USD | `2 orders` | `-0.08%` | `-` |
| `BID` | `8.39` | `632.3400` | 5,306.66 USD | 42,684.47 USD | `4 orders` | `-0.08%` | `-` |
| `BID` | `8.39` | `21.6100` | 181.35 USD | 42,865.82 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.39` | `58.9500` | 494.70 USD | 43,360.52 USD | `1 orders` | `-0.08%` | `-` |
| `BUY` | `8.39` | `1663.1800` | 13,962.23 USD | 3,682,732.77 USD | `STANDARD` | `-0.05%` | `0x57d8e75f47` |
| `BUY` | `8.39` | `1663.1800` | 13,955.91 USD | 3,696,688.68 USD | `STANDARD` | `-0.09%` | `0x57d8e75f47` |
| `BUY` | `8.39` | `1663.1800` | 13,951.09 USD | 3,710,639.76 USD | `STANDARD` | `-0.13%` | `0x57d8e75f47` |
| `BUY` | `8.39` | `1663.1800` | 13,946.60 USD | 3,724,586.36 USD | `STANDARD` | `-0.16%` | `0x57d8e75f47` |
| `BUY` | `8.39` | `1430.1900` | 11,999.87 USD | 4,038,487.81 USD | `STANDARD` | `-0.10%` | `0x7d0c59691f` |
| `BUY` | `8.39` | `1197.9600` | 10,052.56 USD | 4,145,716.13 USD | `STANDARD` | `-0.09%` | `0xaf9f722a67` |
| `BUY` | `8.39` | `1197.9600` | 10,046.81 USD | 4,155,762.94 USD | `STANDARD` | `-0.14%` | `0x621c555167` |
| `BUY` | `8.39` | `1191.2000` | 9,997.03 USD | 4,185,834.90 USD | `STANDARD` | `-0.08%` | `0x7d0c59691f` |
| `BUY` | `8.39` | `952.8800` | 7,999.33 USD | 4,280,089.11 USD | `STANDARD` | `-0.05%` | `0x7d0c59691f` |
| `BUY` | `8.39` | `571.8200` | 4,797.68 USD | 4,374,348.00 USD | `STANDARD` | `-0.10%` | `0x71d0e11ebb` |
| `BUY` | `8.39` | `383.6900` | 3,219.81 USD | 4,436,523.50 USD | `STANDARD` | `-0.08%` | `0x75f3665323` |
| `BUY` | `8.39` | `368.9700` | 3,097.47 USD | 4,461,362.09 USD | `STANDARD` | `-0.05%` | `0x2a72b57dea` |
| `BUY` | `8.39` | `368.9700` | 3,095.03 USD | 4,464,457.12 USD | `STANDARD` | `-0.12%` | `0x2a72b57dea` |
| `BUY` | `8.39` | `337.7700` | 2,832.81 USD | 4,494,923.22 USD | `STANDARD` | `-0.14%` | `0xecb63caa47` |
| `BUY` | `8.39` | `312.0500` | 2,617.35 USD | 4,502,859.98 USD | `STANDARD` | `-0.13%` | `0x7717a7a245` |
| `BUY` | `8.39` | `297.8900` | 2,499.92 USD | 4,510,474.39 USD | `STANDARD` | `-0.08%` | `0x0efb38a5fa` |
| `BUY` | `8.39` | `203.2800` | 1,706.52 USD | 4,566,089.96 USD | `STANDARD` | `-0.05%` | `0x57d8e75f47` |
| `BUY` | `8.39` | `179.9900` | 1,509.41 USD | 4,575,158.90 USD | `STANDARD` | `-0.15%` | `0x6ba889db7f` |
| `BUY` | `8.39` | `179.8200` | 1,508.89 USD | 4,576,667.78 USD | `STANDARD` | `-0.09%` | `0x6ba889db7f` |
| `BUY` | `8.39` | `154.0400` | 1,293.01 USD | 4,586,573.86 USD | `STANDARD` | `-0.06%` | `0x727956612a` |
| `BUY` | `8.39` | `137.5600` | 1,154.32 USD | 4,590,271.72 USD | `STANDARD` | `-0.09%` | `0xdd4f66125d` |
| `BUY` | `8.39` | `137.5600` | 1,153.77 USD | 4,591,425.49 USD | `STANDARD` | `-0.13%` | `0xdd4f66125d` |
| `BUY` | `8.39` | `129.6300` | 1,088.04 USD | 4,594,801.97 USD | `STANDARD` | `-0.06%` | `0x2eddf3aa5c` |
| `BUY` | `8.39` | `125.1800` | 1,050.42 USD | 4,598,006.41 USD | `STANDARD` | `-0.09%` | `0x2eddf3aa5c` |
| `BUY` | `8.39` | `120.0800` | 1,008.05 USD | 4,599,014.46 USD | `STANDARD` | `-0.05%` | `0x7717a7a245` |
| `BUY` | `8.39` | `120.0800` | 1,007.77 USD | 4,600,022.23 USD | `STANDARD` | `-0.07%` | `0x7717a7a245` |
| `BUY` | `8.39` | `119.2400` | 999.96 USD | 4,602,022.17 USD | `STANDARD` | `-0.15%` | `0x27c9fa86c9` |
| `BUY` | `8.39` | `119.1500` | 999.92 USD | 4,603,022.09 USD | `STANDARD` | `-0.08%` | `0x0eecd62efb` |
| `BUY` | `8.39` | `107.6500` | 903.41 USD | 4,632,072.60 USD | `STANDARD` | `-0.08%` | `0xa382fa9f4b` |
| `BUY` | `8.39` | `107.6500` | 903.12 USD | 4,635,685.36 USD | `STANDARD` | `-0.11%` | `0xfd66e33095` |
| `BUY` | `8.39` | `107.5800` | 903.11 USD | 4,636,588.47 USD | `STANDARD` | `-0.05%` | `0x9d81a3adf8` |
| `BUY` | `8.39` | `107.6500` | 903.00 USD | 4,637,491.47 USD | `STANDARD` | `-0.12%` | `0xd0956a1eba` |
| `BUY` | `8.39` | `107.5800` | 902.88 USD | 4,638,394.35 USD | `STANDARD` | `-0.07%` | `0xf30120f048` |
| `BUY` | `8.39` | `107.6500` | 902.87 USD | 4,639,297.22 USD | `STANDARD` | `-0.14%` | `0xa382fa9f4b` |
| `BUY` | `8.39` | `107.5700` | 902.64 USD | 4,640,199.86 USD | `STANDARD` | `-0.09%` | `0x53136b4a7c` |
| `BUY` | `8.39` | `86.5600` | 725.82 USD | 4,673,906.93 USD | `STANDARD` | `-0.16%` | `0x31ca8395cf` |
| `BUY` | `8.39` | `84.9900` | 712.67 USD | 4,677,499.35 USD | `STANDARD` | `-0.16%` | `0x010461c14e` |
| `BUY` | `8.39` | `82.0100` | 688.27 USD | 4,678,187.61 USD | `STANDARD` | `-0.07%` | `0x2eddf3aa5c` |
| `BUY` | `8.39` | `75.5900` | 634.46 USD | 4,688,143.19 USD | `STANDARD` | `-0.06%` | `0x2eddf3aa5c` |
| `BUY` | `8.39` | `67.2800` | 564.48 USD | 4,691,094.66 USD | `STANDARD` | `-0.10%` | `0x33ad48ed92` |
| `BUY` | `8.39` | `66.7400` | 560.18 USD | 4,691,654.84 USD | `STANDARD` | `-0.06%` | `0x023a3d0580` |
| `BUY` | `8.39` | `60.3400` | 506.55 USD | 4,693,683.51 USD | `STANDARD` | `-0.05%` | `0x57d8e75f47` |
| `BUY` | `8.39` | `60.3400` | 505.99 USD | 4,694,189.50 USD | `STANDARD` | `-0.15%` | `0x57d8e75f47` |
| `ASK` | `8.40` | `179.8200` | 1,511.37 USD | 8,900.96 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.40` | `157.5800` | 1,324.38 USD | 7,389.59 USD | `2 orders` | `+0.07%` | `-` |
| `ASK` | `8.40` | `78.9300` | 663.34 USD | 6,065.21 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.40` | `107.5700` | 904.00 USD | 5,401.88 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.40` | `129.5500` | 1,088.70 USD | 4,497.88 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.40` | `29.7800` | 250.26 USD | 3,409.18 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.40` | `84.3200` | 708.53 USD | 3,158.92 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.40` | `119.0100` | 999.98 USD | 2,450.39 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.40` | `5.5600` | 46.72 USD | 1,450.41 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.40` | `107.6300` | 904.29 USD | 1,403.69 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.40` | `18.6200` | 156.44 USD | 499.41 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.40` | `20.8000` | 174.72 USD | 342.97 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.40` | `20.0300` | 168.25 USD | 168.25 USD | `1 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `8.40` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.40` | `0.00%` | `-` |
| `BID` | `8.40` | `107.5800` | 903.42 USD | 903.42 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.40` | `215.2600` | 1,807.50 USD | 2,710.92 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `8.40` | `107.5800` | 903.32 USD | 3,614.24 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.40` | `107.5700` | 903.13 USD | 4,517.36 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.40` | `107.5800` | 903.20 USD | 5,420.56 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.40` | `103.9700` | 872.87 USD | 6,293.43 USD | `1 orders` | `-0.04%` | `-` |
| `BUY` | `8.40` | `714.5100` | 5,999.60 USD | 4,320,126.52 USD | `STANDARD` | `-0.02%` | `0x7d0c59691f` |
| `SELL` | `8.40` | `179.8200` | 1,511.37 USD | 4,572,139.73 USD | `STANDARD` | `+0.07%` | `0x6ba889db7f` |
| `BUY` | `8.40` | `179.8200` | 1,509.75 USD | 4,573,649.48 USD | `STANDARD` | `-0.03%` | `0x6ba889db7f` |
| `SELL` | `8.40` | `135.0800` | 1,135.06 USD | 4,593,713.94 USD | `STANDARD` | `+0.05%` | `0xecb63caa47` |
| `SELL` | `8.40` | `119.0100` | 999.98 USD | 4,601,022.21 USD | `STANDARD` | `+0.05%` | `0x0eecd62efb` |
| `SELL` | `8.40` | `107.6500` | 904.65 USD | 4,621,223.24 USD | `STANDARD` | `+0.06%` | `0xea0e878d5d` |
| `SELL` | `8.40` | `107.6500` | 904.63 USD | 4,622,127.87 USD | `STANDARD` | `+0.06%` | `0xf30120f048` |
| `SELL` | `8.40` | `107.6100` | 904.23 USD | 4,626,650.12 USD | `STANDARD` | `+0.05%` | `0x9d81a3adf8` |
| `SELL` | `8.40` | `107.5800` | 904.16 USD | 4,627,554.27 USD | `STANDARD` | `+0.07%` | `0xea0e878d5d` |
| `SELL` | `8.40` | `107.5700` | 904.00 USD | 4,628,458.27 USD | `STANDARD` | `+0.06%` | `0xf30120f048` |
| `BUY` | `8.40` | `107.6300` | 903.75 USD | 4,629,362.02 USD | `STANDARD` | `-0.02%` | `0x63f6411ca6` |
| `BUY` | `8.40` | `107.6300` | 903.75 USD | 4,630,265.76 USD | `STANDARD` | `-0.02%` | `0xa382fa9f4b` |
| `BUY` | `8.40` | `107.5800` | 903.42 USD | 4,631,169.19 USD | `STANDARD` | `-0.01%` | `0xf30120f048` |
| `BUY` | `8.40` | `107.5800` | 903.32 USD | 4,632,975.91 USD | `STANDARD` | `-0.02%` | `0xea0e878d5d` |
| `BUY` | `8.40` | `107.5800` | 903.20 USD | 4,633,879.11 USD | `STANDARD` | `-0.04%` | `0x9d81a3adf8` |
| `BUY` | `8.40` | `107.5700` | 903.13 USD | 4,634,782.24 USD | `STANDARD` | `-0.04%` | `0xfd66e33095` |
| `BUY` | `8.40` | `103.9600` | 872.86 USD | 4,667,143.87 USD | `STANDARD` | `-0.03%` | `0xecb63caa47` |
| `SELL` | `8.40` | `78.9300` | 663.34 USD | 4,684,908.51 USD | `STANDARD` | `+0.06%` | `0x010461c14e` |
| `ASK` | `8.41` | `87.5200` | 735.75 USD | 15,097.55 USD | `1 orders` | `+0.09%` | `-` |
| `ASK` | `8.41` | `297.3800` | 2,499.92 USD | 14,361.81 USD | `1 orders` | `+0.09%` | `-` |
| `ASK` | `8.41` | `107.5900` | 904.38 USD | 11,861.88 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `8.41` | `30.5200` | 256.54 USD | 10,957.50 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `8.41` | `151.8700` | 1,276.53 USD | 10,700.96 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `8.41` | `1.9400` | 16.31 USD | 9,424.43 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `8.41` | `60.3400` | 507.16 USD | 9,408.13 USD | `1 orders` | `+0.08%` | `-` |
| `SELL` | `8.41` | `1663.1800` | 13,995.66 USD | 3,626,809.34 USD | `STANDARD` | `+0.19%` | `0x57d8e75f47` |
| `SELL` | `8.41` | `1663.1800` | 13,991.50 USD | 3,640,800.84 USD | `STANDARD` | `+0.16%` | `0x57d8e75f47` |
| `SELL` | `8.41` | `1663.1800` | 13,986.84 USD | 3,654,787.68 USD | `STANDARD` | `+0.13%` | `0x57d8e75f47` |
| `SELL` | `8.41` | `1663.1800` | 13,982.85 USD | 3,668,770.54 USD | `STANDARD` | `+0.10%` | `0x57d8e75f47` |
| `SELL` | `8.41` | `1197.9600` | 10,073.17 USD | 4,125,591.00 USD | `STANDARD` | `+0.12%` | `0x621c555167` |
| `SELL` | `8.41` | `1197.9600` | 10,072.57 USD | 4,135,663.57 USD | `STANDARD` | `+0.11%` | `0xaf9f722a67` |
| `SELL` | `8.41` | `1047.4200` | 8,812.26 USD | 4,213,214.59 USD | `STANDARD` | `+0.17%` | `0x08a49e7f71` |
| `SELL` | `8.41` | `572.2000` | 4,814.49 USD | 4,369,550.32 USD | `STANDARD` | `+0.18%` | `0x71d0e11ebb` |
| `SELL` | `8.41` | `385.1100` | 3,239.85 USD | 4,433,303.69 USD | `STANDARD` | `+0.17%` | `0xecb63caa47` |
| `SELL` | `8.41` | `368.9700` | 3,103.37 USD | 4,452,063.93 USD | `STANDARD` | `+0.15%` | `0x2a72b57dea` |
| `SELL` | `8.41` | `357.9600` | 3,010.69 USD | 4,492,090.41 USD | `STANDARD` | `+0.14%` | `0xecb63caa47` |
| `SELL` | `8.41` | `297.3800` | 2,499.92 USD | 4,507,974.47 USD | `STANDARD` | `+0.09%` | `0x0efb38a5fa` |
| `SELL` | `8.41` | `267.4200` | 2,249.96 USD | 4,519,510.79 USD | `STANDARD` | `+0.18%` | `0xa38f19c4cc` |
| `SELL` | `8.41` | `231.2300` | 1,945.57 USD | 4,545,040.98 USD | `STANDARD` | `+0.18%` | `0x9d732bed51` |
| `SELL` | `8.41` | `179.7200` | 1,511.79 USD | 4,570,628.36 USD | `STANDARD` | `+0.16%` | `0x6ba889db7f` |
| `SELL` | `8.41` | `151.8700` | 1,276.53 USD | 4,587,850.39 USD | `STANDARD` | `+0.08%` | `0x727956612a` |
| `SELL` | `8.41` | `128.2600` | 1,078.35 USD | 4,595,880.32 USD | `STANDARD` | `+0.10%` | `0x2eddf3aa5c` |
| `SELL` | `8.41` | `127.9100` | 1,075.67 USD | 4,596,955.99 USD | `STANDARD` | `+0.13%` | `0x2eddf3aa5c` |
| `SELL` | `8.41` | `107.6500` | 905.68 USD | 4,609,457.01 USD | `STANDARD` | `+0.17%` | `0xfd66e33095` |
| `SELL` | `8.41` | `107.6500` | 905.40 USD | 4,612,173.70 USD | `STANDARD` | `+0.14%` | `0x9d81a3adf8` |
| `SELL` | `8.41` | `107.5900` | 905.36 USD | 4,613,079.06 USD | `STANDARD` | `+0.19%` | `0x9d81a3adf8` |
| `SELL` | `8.41` | `107.6500` | 905.27 USD | 4,613,984.33 USD | `STANDARD` | `+0.13%` | `0x63f6411ca6` |
| `SELL` | `8.41` | `107.5700` | 905.18 USD | 4,614,889.51 USD | `STANDARD` | `+0.19%` | `0xd0956a1eba` |
| `SELL` | `8.41` | `107.5700` | 905.07 USD | 4,615,794.58 USD | `STANDARD` | `+0.18%` | `0xea0e878d5d` |
| `SELL` | `8.41` | `107.5900` | 904.92 USD | 4,616,699.50 USD | `STANDARD` | `+0.14%` | `0xea0e878d5d` |
| `SELL` | `8.41` | `107.6500` | 904.86 USD | 4,617,604.36 USD | `STANDARD` | `+0.08%` | `0xea0e878d5d` |
| `SELL` | `8.41` | `107.5700` | 904.86 USD | 4,618,509.22 USD | `STANDARD` | `+0.16%` | `0xf30120f048` |
| `SELL` | `8.41` | `107.6100` | 904.70 USD | 4,619,413.92 USD | `STANDARD` | `+0.10%` | `0x63f6411ca6` |
| `SELL` | `8.41` | `107.6100` | 904.68 USD | 4,620,318.60 USD | `STANDARD` | `+0.10%` | `0xfd66e33095` |
| `SELL` | `8.41` | `107.5700` | 904.62 USD | 4,623,032.49 USD | `STANDARD` | `+0.13%` | `0xa382fa9f4b` |
| `SELL` | `8.41` | `107.5900` | 904.62 USD | 4,623,937.11 USD | `STANDARD` | `+0.11%` | `0xf30120f048` |
| `SELL` | `8.41` | `107.5800` | 904.40 USD | 4,624,841.51 USD | `STANDARD` | `+0.10%` | `0xf30120f048` |
| `SELL` | `8.41` | `107.5900` | 904.38 USD | 4,625,745.89 USD | `STANDARD` | `+0.08%` | `0xa382fa9f4b` |
| `SELL` | `8.41` | `91.7000` | 771.55 USD | 4,668,687.54 USD | `STANDARD` | `+0.18%` | `0xdd4f66125d` |
| `SELL` | `8.41` | `91.7000` | 771.49 USD | 4,669,459.03 USD | `STANDARD` | `+0.17%` | `0xdd4f66125d` |
| `SELL` | `8.41` | `85.9000` | 722.24 USD | 4,675,354.21 USD | `STANDARD` | `+0.11%` | `0x010461c14e` |
| `SELL` | `8.41` | `85.1800` | 716.64 USD | 4,676,070.85 USD | `STANDARD` | `+0.17%` | `0x31ca8395cf` |
| `SELL` | `8.41` | `80.7000` | 678.88 USD | 4,679,554.17 USD | `STANDARD` | `+0.16%` | `0xa382fa9f4b` |
| `SELL` | `8.41` | `74.9700` | 630.34 USD | 4,688,773.54 USD | `STANDARD` | `+0.11%` | `0x31ca8395cf` |
| `SELL` | `8.41` | `68.1600` | 573.32 USD | 4,689,960.54 USD | `STANDARD` | `+0.15%` | `0xdd4f66125d` |
| `SELL` | `8.41` | `67.7200` | 569.64 USD | 4,690,530.18 USD | `STANDARD` | `+0.15%` | `0x33ad48ed92` |
| `SELL` | `8.41` | `60.3400` | 507.58 USD | 4,692,162.42 USD | `STANDARD` | `+0.16%` | `0x57d8e75f47` |
| `SELL` | `8.41` | `60.3400` | 507.37 USD | 4,692,669.79 USD | `STANDARD` | `+0.12%` | `0x57d8e75f47` |
| `SELL` | `8.41` | `60.3400` | 507.16 USD | 4,693,176.96 USD | `STANDARD` | `+0.08%` | `0x57d8e75f47` |
| `SELL` | `8.42` | `19826.4100` | 166,934.41 USD | 1,202,855.20 USD | `LARGE (>= USD 100K)` | `+0.25%` | `0x71d0e11ebb` |
| `SELL` | `8.42` | `1663.1800` | 14,011.96 USD | 3,584,809.88 USD | `STANDARD` | `+0.31%` | `0x57d8e75f47` |
| `SELL` | `8.42` | `1663.1800` | 14,003.98 USD | 3,598,813.86 USD | `STANDARD` | `+0.25%` | `0x57d8e75f47` |
| `SELL` | `8.42` | `1663.1800` | 13,999.82 USD | 3,612,813.68 USD | `STANDARD` | `+0.22%` | `0x57d8e75f47` |
| `SELL` | `8.42` | `1197.9600` | 10,082.63 USD | 4,115,517.83 USD | `STANDARD` | `+0.21%` | `0xaf9f722a67` |
| `SELL` | `8.42` | `593.5800` | 4,999.96 USD | 4,359,735.91 USD | `STANDARD` | `+0.29%` | `0x0efb38a5fa` |
| `SELL` | `8.42` | `482.4700` | 4,061.19 USD | 4,382,472.21 USD | `STANDARD` | `+0.22%` | `0xecb63caa47` |
| `SELL` | `8.42` | `481.6400` | 4,055.12 USD | 4,386,527.33 USD | `STANDARD` | `+0.25%` | `0x7717a7a245` |
| `SELL` | `8.42` | `481.2500` | 4,049.96 USD | 4,390,577.29 USD | `STANDARD` | `+0.20%` | `0xecb63caa47` |
| `SELL` | `8.42` | `454.0800` | 3,824.94 USD | 4,406,304.99 USD | `STANDARD` | `+0.30%` | `0xa38f19c4cc` |
| `SELL` | `8.42` | `368.9700` | 3,107.83 USD | 4,445,854.61 USD | `STANDARD` | `+0.29%` | `0x2a72b57dea` |
| `SELL` | `8.42` | `368.9700` | 3,105.95 USD | 4,448,960.56 USD | `STANDARD` | `+0.23%` | `0x2a72b57dea` |
| `SELL` | `8.42` | `270.8700` | 2,280.24 USD | 4,512,754.63 USD | `STANDARD` | `+0.23%` | `0x33ad48ed92` |
| `SELL` | `8.42` | `239.1800` | 2,014.30 USD | 4,523,545.58 USD | `STANDARD` | `+0.27%` | `0xecb63caa47` |
| `SELL` | `8.42` | `231.2300` | 1,947.53 USD | 4,541,148.92 USD | `STANDARD` | `+0.28%` | `0x9d732bed51` |
| `SELL` | `8.42` | `231.2300` | 1,946.49 USD | 4,543,095.42 USD | `STANDARD` | `+0.23%` | `0x9d732bed51` |
| `SELL` | `8.42` | `179.8200` | 1,514.50 USD | 4,567,604.46 USD | `STANDARD` | `+0.28%` | `0x6ba889db7f` |
| `SELL` | `8.42` | `179.6400` | 1,512.12 USD | 4,569,116.58 USD | `STANDARD` | `+0.22%` | `0x6ba889db7f` |
| `SELL` | `8.42` | `107.6500` | 906.26 USD | 4,604,927.31 USD | `STANDARD` | `+0.24%` | `0xa382fa9f4b` |
| `SELL` | `8.42` | `107.6500` | 906.24 USD | 4,605,833.55 USD | `STANDARD` | `+0.23%` | `0xea0e878d5d` |
| `SELL` | `8.42` | `107.6100` | 906.03 USD | 4,606,739.58 USD | `STANDARD` | `+0.25%` | `0xfd66e33095` |
| `SELL` | `8.42` | `107.6500` | 905.97 USD | 4,607,645.55 USD | `STANDARD` | `+0.20%` | `0xd0956a1eba` |
| `SELL` | `8.42` | `107.5900` | 905.78 USD | 4,608,551.33 USD | `STANDARD` | `+0.24%` | `0x53136b4a7c` |
| `SELL` | `8.42` | `107.6100` | 905.66 USD | 4,610,362.67 USD | `STANDARD` | `+0.21%` | `0x9d81a3adf8` |
| `SELL` | `8.42` | `107.5900` | 905.63 USD | 4,611,268.30 USD | `STANDARD` | `+0.22%` | `0xfd66e33095` |
| `SELL` | `8.42` | `91.7000` | 772.12 USD | 4,667,915.99 USD | `STANDARD` | `+0.25%` | `0xdd4f66125d` |
| `SELL` | `8.42` | `89.2800` | 751.68 USD | 4,670,971.77 USD | `STANDARD` | `+0.25%` | `0x31ca8395cf` |
| `SELL` | `8.42` | `86.9900` | 732.26 USD | 4,673,181.11 USD | `STANDARD` | `+0.23%` | `0x010461c14e` |
| `SELL` | `8.43` | `1969.7300` | 16,601.48 USD | 3,492,648.94 USD | `STANDARD` | `+0.35%` | `0x08a49e7f71` |
| `SELL` | `8.43` | `1537.3500` | 12,966.78 USD | 3,899,827.84 USD | `STANDARD` | `+0.43%` | `0x57d8e75f47` |
| `SELL` | `8.43` | `1537.3500` | 12,960.94 USD | 3,912,788.78 USD | `STANDARD` | `+0.38%` | `0x57d8e75f47` |
| `SELL` | `8.43` | `1537.3500` | 12,957.25 USD | 3,925,746.03 USD | `STANDARD` | `+0.35%` | `0x57d8e75f47` |
| `SELL` | `8.43` | `1130.4400` | 9,534.02 USD | 4,195,368.92 USD | `STANDARD` | `+0.42%` | `0xd3943e4008` |
| `SELL` | `8.43` | `1031.3600` | 8,694.47 USD | 4,230,721.14 USD | `STANDARD` | `+0.37%` | `0xd3943e4008` |
| `SELL` | `8.43` | `719.3400` | 6,066.55 USD | 4,314,126.92 USD | `STANDARD` | `+0.41%` | `0xecb63caa47` |
| `SELL` | `8.43` | `688.3700` | 5,800.21 USD | 4,331,912.67 USD | `STANDARD` | `+0.33%` | `0xecb63caa47` |
| `SELL` | `8.43` | `688.0000` | 5,800.18 USD | 4,337,712.85 USD | `STANDARD` | `+0.38%` | `0xecb63caa47` |
| `SELL` | `8.43` | `668.7000` | 5,638.55 USD | 4,349,105.94 USD | `STANDARD` | `+0.40%` | `0x33ad48ed92` |
| `SELL` | `8.43` | `368.9700` | 3,110.64 USD | 4,442,746.77 USD | `STANDARD` | `+0.38%` | `0x2a72b57dea` |
| `SELL` | `8.43` | `366.8200` | 3,091.63 USD | 4,470,641.90 USD | `STANDARD` | `+0.35%` | `0xdd4f66125d` |
| `SELL` | `8.43` | `231.2300` | 1,949.66 USD | 4,537,252.88 USD | `STANDARD` | `+0.39%` | `0x9d732bed51` |
| `SELL` | `8.43` | `231.2300` | 1,948.51 USD | 4,539,201.39 USD | `STANDARD` | `+0.33%` | `0x9d732bed51` |
| `SELL` | `8.43` | `79.2600` | 668.18 USD | 4,682,248.33 USD | `STANDARD` | `+0.38%` | `0x010461c14e` |
| `SELL` | `8.43` | `77.2200` | 650.98 USD | 4,686,222.49 USD | `STANDARD` | `+0.38%` | `0x31ca8395cf` |
| `SELL` | `8.44` | `25052.8000` | 211,490.73 USD | 1,035,920.80 USD | `LARGE (>= USD 100K)` | `+0.51%` | `0x71cfa5e263` |
| `SELL` | `8.44` | `12277.5400` | 103,658.04 USD | 2,551,676.32 USD | `LARGE (>= USD 100K)` | `+0.53%` | `0x71d0e11ebb` |
| `SELL` | `8.44` | `1537.3500` | 12,979.54 USD | 3,860,915.82 USD | `STANDARD` | `+0.53%` | `0x57d8e75f47` |
| `SELL` | `8.44` | `1537.3500` | 12,974.62 USD | 3,873,890.44 USD | `STANDARD` | `+0.49%` | `0x57d8e75f47` |
| `SELL` | `8.44` | `1537.3500` | 12,970.62 USD | 3,886,861.06 USD | `STANDARD` | `+0.46%` | `0x57d8e75f47` |
| `SELL` | `8.44` | `947.8100` | 7,999.99 USD | 4,272,089.78 USD | `STANDARD` | `+0.50%` | `0x0efb38a5fa` |
| `SELL` | `8.44` | `770.0000` | 6,502.50 USD | 4,301,557.88 USD | `STANDARD` | `+0.55%` | `0xa38f19c4cc` |
| `SELL` | `8.44` | `368.9700` | 3,112.63 USD | 4,439,636.14 USD | `STANDARD` | `+0.44%` | `0x2a72b57dea` |
| `SELL` | `8.44` | `366.8200` | 3,097.68 USD | 4,458,264.62 USD | `STANDARD` | `+0.55%` | `0xdd4f66125d` |
| `SELL` | `8.44` | `231.2300` | 1,952.62 USD | 4,531,400.96 USD | `STANDARD` | `+0.55%` | `0x9d732bed51` |
| `SELL` | `8.44` | `231.2300` | 1,951.63 USD | 4,533,352.59 USD | `STANDARD` | `+0.49%` | `0x9d732bed51` |
| `SELL` | `8.44` | `231.2300` | 1,950.63 USD | 4,535,303.22 USD | `STANDARD` | `+0.44%` | `0x9d732bed51` |
| `SELL` | `8.45` | `14516.0200` | 122,706.82 USD | 1,863,599.52 USD | `LARGE (>= USD 100K)` | `+0.65%` | `0x71d0e11ebb` |
| `SELL` | `8.45` | `1537.3500` | 12,994.30 USD | 3,834,949.37 USD | `STANDARD` | `+0.64%` | `0x57d8e75f47` |
| `SELL` | `8.45` | `1537.3500` | 12,986.92 USD | 3,847,936.29 USD | `STANDARD` | `+0.58%` | `0x57d8e75f47` |
| `SELL` | `8.45` | `481.0300` | 4,063.02 USD | 4,378,411.02 USD | `STANDARD` | `+0.57%` | `0xcd7f60e943` |
| `SELL` | `8.45` | `404.9300` | 3,421.82 USD | 4,420,026.82 USD | `STANDARD` | `+0.62%` | `0x14f8e04290` |
| `SELL` | `8.45` | `239.1000` | 2,020.49 USD | 4,521,531.28 USD | `STANDARD` | `+0.62%` | `0x39bac00809` |
| `SELL` | `8.45` | `231.2300` | 1,954.43 USD | 4,527,494.70 USD | `STANDARD` | `+0.64%` | `0x9d732bed51` |
| `SELL` | `8.45` | `231.2300` | 1,953.64 USD | 4,529,448.34 USD | `STANDARD` | `+0.60%` | `0x9d732bed51` |
| `SELL` | `8.45` | `78.5300` | 663.89 USD | 4,684,245.17 USD | `STANDARD` | `+0.66%` | `0x010461c14e` |
| `SELL` | `8.46` | `1523.2600` | 12,885.87 USD | 3,951,519.50 USD | `STANDARD` | `+0.72%` | `0xd3943e4008` |
| `SELL` | `8.46` | `1417.9000` | 11,999.97 USD | 4,014,488.02 USD | `STANDARD` | `+0.77%` | `0x0efb38a5fa` |
| `SELL` | `8.46` | `1299.0100` | 10,983.78 USD | 4,105,435.20 USD | `STANDARD` | `+0.68%` | `0xd3943e4008` |
| `SELL` | `8.46` | `1015.7500` | 8,592.43 USD | 4,239,313.58 USD | `STANDARD` | `+0.72%` | `0x33ad48ed92` |
| `SELL` | `8.46` | `366.8200` | 3,103.00 USD | 4,455,166.93 USD | `STANDARD` | `+0.72%` | `0xdd4f66125d` |
| `SELL` | `8.46` | `118.0600` | 998.95 USD | 4,604,021.04 USD | `STANDARD` | `+0.75%` | `0x23cc6b8202` |
| `SELL` | `8.46` | `87.1800` | 737.37 USD | 4,672,448.85 USD | `STANDARD` | `+0.71%` | `0x31ca8395cf` |
| `SELL` | `8.47` | `404.9300` | 3,431.09 USD | 4,413,181.31 USD | `STANDARD` | `+0.89%` | `0x14f8e04290` |
| `SELL` | `8.48` | `11799.9700` | 100,112.13 USD | 2,754,258.88 USD | `LARGE (>= USD 100K)` | `+1.02%` | `0x881cd92459` |
| `SELL` | `8.48` | `75.9200` | 643.95 USD | 4,686,866.43 USD | `STANDARD` | `+0.99%` | `0x31ca8395cf` |
| `SELL` | `8.49` | `49008.3200` | 416,320.78 USD | 416,320.78 USD | `LARGE (>= USD 100K)` | `+1.15%` | `0x71cfa5e263` |
| `SELL` | `8.49` | `12903.3700` | 109,486.38 USD | 2,448,018.27 USD | `LARGE (>= USD 100K)` | `+1.03%` | `0xecb63caa47` |
| `SELL` | `8.49` | `1345.6300` | 11,422.92 USD | 4,049,910.73 USD | `STANDARD` | `+1.07%` | `0x33ad48ed92` |
| `SELL` | `8.49` | `84.3300` | 715.83 USD | 4,676,786.68 USD | `STANDARD` | `+1.07%` | `0x010461c14e` |
| `SELL` | `8.50` | `14660.8600` | 124,648.10 USD | 1,493,394.86 USD | `LARGE (>= USD 100K)` | `+1.23%` | `0xecb63caa47` |
| `SELL` | `8.50` | `1882.1300` | 15,999.99 USD | 3,525,250.31 USD | `STANDARD` | `+1.22%` | `0x0efb38a5fa` |
| `SELL` | `8.51` | `14541.9100` | 123,779.28 USD | 1,617,174.14 USD | `LARGE (>= USD 100K)` | `+1.35%` | `0x71d0e11ebb` |
| `SELL` | `8.51` | `1775.5700` | 15,116.14 USD | 3,556,366.44 USD | `STANDARD` | `+1.37%` | `0xd3943e4008` |
| `SELL` | `8.51` | `404.9300` | 3,445.23 USD | 4,409,750.22 USD | `STANDARD` | `+1.30%` | `0x14f8e04290` |
| `SELL` | `8.51` | `315.7300` | 2,686.86 USD | 4,497,610.08 USD | `STANDARD` | `+1.33%` | `0x07fd993f0f` |
| `SELL` | `8.52` | `8881.0200` | 75,658.30 USD | 3,285,414.81 USD | `MEDIUM (>= USD 25K)` | `+1.43%` | `0xecb63caa47` |
| `SELL` | `8.52` | `1297.8700` | 11,054.22 USD | 4,083,397.21 USD | `STANDARD` | `+1.41%` | `0xa38f19c4cc` |
| `SELL` | `8.53` | `2228.4200` | 18,999.95 USD | 3,419,928.56 USD | `STANDARD` | `+1.52%` | `0x0efb38a5fa` |
| `SELL` | `8.53` | `167.9300` | 1,431.72 USD | 4,582,618.81 USD | `STANDARD` | `+1.51%` | `0x31ca8395cf` |
| `SELL` | `8.53` | `155.8600` | 1,328.83 USD | 4,585,280.85 USD | `STANDARD` | `+1.51%` | `0x010461c14e` |
| `SELL` | `8.54` | `10692.5800` | 91,284.69 USD | 3,038,869.11 USD | `MEDIUM (>= USD 25K)` | `+1.65%` | `0x71d0e11ebb` |
| `SELL` | `8.54` | `9678.6600` | 82,617.04 USD | 3,209,756.51 USD | `MEDIUM (>= USD 25K)` | `+1.63%` | `0xecb63caa47` |
| `SELL` | `8.54` | `2218.9500` | 18,946.50 USD | 3,438,875.06 USD | `STANDARD` | `+1.66%` | `0xd3943e4008` |
| `SELL` | `8.55` | `400.5300` | 3,423.69 USD | 4,416,605.00 USD | `STANDARD` | `+1.78%` | `0x14f8e04290` |
| `SELL` | `8.56` | `2570.1200` | 21,999.97 USD | 3,381,928.62 USD | `STANDARD` | `+1.92%` | `0x0efb38a5fa` |
| `SELL` | `8.56` | `2195.9100` | 18,792.16 USD | 3,457,667.22 USD | `STANDARD` | `+1.89%` | `0xa38f19c4cc` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:26:17 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1502` | `0x7737...bf66` | `SHORT` | 1,498,389.65 USD | `171,568.06` | `7.43` | `8.29` | `110.10` | -222,844.63 USD | `-14.87%` | `10X Cross` |
| `1585` | `0xeadc...9d55` | `LONG` | 1,395,062.95 USD | `160,070.56` | `8.11` | `8.29` | `0.000000` | 97,425.38 USD | `+6.98%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `9.02` | 7,429.53 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 7.43K USD at 9.0174 USD [API] | `2026-10-28 01:54:48` |
| `ANNOUNCEMENT` | `INFO` | `9.02` | 8,000.34 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 8.00K USD at 9.0167 USD [API] | `2026-10-28 01:54:48` |
| `ANNOUNCEMENT` | `INFO` | `8.66` | 8,702.26 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Long: 8.70K USD at 8.6600 USD [API] | `2026-10-27 05:30:22` |
| `ANNOUNCEMENT` | `INFO` | `8.66` | 485.74 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Long: 0.49K USD at 8.6600 USD [API] | `2026-10-27 05:30:22` |
| `ANNOUNCEMENT` | `INFO` | `8.66` | 1,294.77 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Long: 1.29K USD at 8.6601 USD [API] | `2026-10-27 05:30:22` |
| `ANNOUNCEMENT` | `INFO` | `8.66` | 485.78 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Long: 0.49K USD at 8.6607 USD [API] | `2026-10-27 05:30:22` |
| `ANNOUNCEMENT` | `INFO` | `8.66` | 485.80 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Long: 0.49K USD at 8.6611 USD [API] | `2026-10-27 05:30:22` |
| `ANNOUNCEMENT` | `INFO` | `8.66` | 486.33 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Long: 0.49K USD at 8.6612 USD [API] | `2026-10-27 05:30:22` |
| `ANNOUNCEMENT` | `INFO` | `8.66` | 1,094.65 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Long: 1.09K USD at 8.6616 USD [API] | `2026-10-27 05:30:22` |
| `ANNOUNCEMENT` | `INFO` | `8.66` | 138.59 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Long: 0.14K USD at 8.6616 USD [API] | `2026-10-27 05:30:22` |
| `ANNOUNCEMENT` | `INFO` | `8.66` | 5,795.20 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Long: 5.80K USD at 8.6621 USD [API] | `2026-10-27 05:30:22` |
| `ANNOUNCEMENT` | `INFO` | `9.00` | 5,999.92 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 6.00K USD at 9.0047 USD [API] | `2026-10-28 04:40:18` |
| `ANNOUNCEMENT` | `INFO` | `8.97` | 13,999.97 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 14.00K USD at 8.9652 USD [API] | `2026-10-28 07:13:13` |
| `ANNOUNCEMENT` | `INFO` | `9.04` | 5,146.41 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 5.15K USD at 9.0426 USD [API] | `2026-10-28 10:00:14` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`9.22` (Vol: 293,800.00 USD, Dist: `+5.46%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`9.22` (Vol: 221,300.00 USD, Dist: `+5.49%`) | Long MP=`8.46` (Vol: 190,100.00 USD, Dist: `--3.26%`)
  * 3D Horizon: Short MP=`9.22` (Vol: 264,100.00 USD, Dist: `+5.49%`) | Long MP=`8.55` (Vol: 152,200.00 USD, Dist: `--2.20%`)
  * 7D Horizon: Short MP=`9.28` (Vol: 419,200.00 USD, Dist: `+6.17%`) | Long MP=`8.54` (Vol: 343,100.00 USD, Dist: `--2.36%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.85` | 204.05 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 102.18 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 159.60 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 1,910.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 262.35 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 391.63 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 918.27 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 17,160.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 282.66 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 270.19 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 627.44 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 140.18 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 1,230.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 1,520.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 404.38 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 109.42 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 712.82 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 297.24 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 325.98 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.96` | 8,990.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.98` | 371.88 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.01` | 401.50 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.08` | 2,320.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 1,130.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.18` | 174.89 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.22` | 171.58 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.26` | 106.63 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.29` | 115.97 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.32` | 852.47 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.42` | 2,230.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 486.93 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 2,680.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.64` | 223.98 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 9,060.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,040.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 240.48 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.79` | 5,050.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.82` | 17,120.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.88` | 113.33 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 146.85 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 527.19 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.99` | 329.11 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 167.78 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 314.59 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 805.91 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.09` | 4,200.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.14` | 156,590.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 2,300.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 300.91 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 640.70 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 2,650.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 21,080.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.51` | 367.41 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 121.38 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.57` | 967.98 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.59` | 34,430.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 22,270.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.66` | 4,160.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 2,340.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 406.45 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 869.71 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 2,890.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 736.72 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 580.50 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.84` | 327,670.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 640.67 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.92` | 336.30 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 12,120.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.99` | 447.98 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 331.68 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 105.61 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 3,060.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 405.14 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,550.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.11` | 3,200.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 2,500.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 4,390.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 187.29 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 4,150.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.22` | 715.31 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 972.65 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.29` | 147.51 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.32` | 1,740.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 105.25 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 5,110.00 USD | 894,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 889,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 1,700.00 USD | 889,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 887,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 881,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 3,620.00 USD | 880,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 876,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 1,100.00 USD | 867,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.61` | 409.51 USD | 866,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 865,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,190.00 USD | 863,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.70` | 506.54 USD | 861,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 16,610.00 USD | 861,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 844,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 6,780.00 USD | 843,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 16,960.00 USD | 836,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 4,260.00 USD | 819,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 815,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 2,670.00 USD | 813,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 158.14 USD | 811,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 4,410.00 USD | 810,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.86` | 18,930.00 USD | 806,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 787,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 1,380.00 USD | 784,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.89` | 5,250.00 USD | 782,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.91` | 269.30 USD | 777,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 27,700.00 USD | 777,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,760.00 USD | 749,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 3,480.00 USD | 745,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 742,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 746.58 USD | 741,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 20,860.00 USD | 740,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.01` | 1,530.00 USD | 720,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.03` | 3,390.00 USD | 718,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.04` | 4,100.00 USD | 715,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 711,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,670.00 USD | 704,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 29,850.00 USD | 702,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 672,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 2,300.00 USD | 672,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,950.00 USD | 670,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 649,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 581.02 USD | 647,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.22` | 833.26 USD | 647,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.24` | 179.65 USD | 646,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 646,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,420.00 USD | 646,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 19,790.00 USD | 609,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.32` | 168.76 USD | 589,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 5,050.00 USD | 589,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 2,450.00 USD | 584,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 4,370.00 USD | 582,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.37` | 5,720.00 USD | 577,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 3,920.00 USD | 572,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 17,770.00 USD | 568,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.39` | 2,590.00 USD | 550,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.42` | 500.00 USD | 547,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 1,490.00 USD | 547,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 210.99 USD | 545,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 1,370.00 USD | 545,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.46` | 1,510,000.00 USD | 1,510,000.00 USD | 723.17 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.46` | 1,450,000.00 USD | 1,450,000.00 USD | 723.17 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 9,160.00 USD | 544,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 3,210.00 USD | 535,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,580.00 USD | 531,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,080.00 USD | 530,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.52` | 1,500,000.00 USD | 1,500,000.00 USD | 9,830.00 USD | 3,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.52` | 1,450,000.00 USD | 1,450,000.00 USD | 9,830.00 USD | 3,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.53` | 995.86 USD | 529,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 528,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 157.14 USD | 523,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 4,380.00 USD | 523,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.59` | 25,140.00 USD | 519,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.60` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 74.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.60` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 74.23 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 312.22 USD | 494,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 5,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.62` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 5,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 493,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.63` | 514.52 USD | 493,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 1,490,000.00 USD | 1,490,000.00 USD | 986.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.64` | 1,430,000.00 USD | 1,430,000.00 USD | 986.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 492,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.67` | 1,740.00 USD | 492,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.68` | 1,120.00 USD | 490,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.70` | 1,460.00 USD | 489,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 1,490,000.00 USD | 1,490,000.00 USD | 321.75 USD | 2,390.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.70` | 1,430,000.00 USD | 1,430,000.00 USD | 321.75 USD | 2,390.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.71` | 19,760.00 USD | 488,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.72` | 1,480,000.00 USD | 1,480,000.00 USD | 4,160.00 USD | 1,630.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.72` | 1,420,000.00 USD | 1,420,000.00 USD | 4,160.00 USD | 1,630.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.72` | 2,550.00 USD | 468,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.74` | 1,460,000.00 USD | 1,460,000.00 USD | 2,950.00 USD | 4,580.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.74` | 1,400,000.00 USD | 1,400,000.00 USD | 2,950.00 USD | 4,580.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 893.76 USD | 465,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.76` | 1,450,000.00 USD | 1,450,000.00 USD | 1,510.00 USD | 1,100.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.76` | 1,390,000.00 USD | 1,390,000.00 USD | 1,510.00 USD | 1,100.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 465,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.78` | 695.32 USD | 464,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 1,440,000.00 USD | 1,440,000.00 USD | 40,980.00 USD | 3,730.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.78` | 1,390,000.00 USD | 1,390,000.00 USD | 42,650.00 USD | 3,730.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,900.00 USD | 463,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 1,940.00 USD | 459,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 1,390,000.00 USD | 1,390,000.00 USD | 38,450.00 USD | 10,860.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.80` | 1,330,000.00 USD | 1,330,000.00 USD | 38,450.00 USD | 10,860.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 633.77 USD | 458,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.82` | 5,280.00 USD | 457,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.82` | 1,330,000.00 USD | 1,330,000.00 USD | 5,100.00 USD | 7,610.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.82` | 1,270,000.00 USD | 1,270,000.00 USD | 5,100.00 USD | 7,610.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.84` | 1,310,000.00 USD | 1,310,000.00 USD | 671.45 USD | 4,910.00 USD | 12,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 1,250,000.00 USD | 1,250,000.00 USD | 671.45 USD | 4,910.00 USD | 12,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 10,930.00 USD | 452,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.86` | 2,110.00 USD | 441,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.86` | 1,290,000.00 USD | 1,290,000.00 USD | 14,500.00 USD | 1,680.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.86` | 1,240,000.00 USD | 1,240,000.00 USD | 14,500.00 USD | 1,680.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 176.18 USD | 439,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 438,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 1,260,000.00 USD | 1,260,000.00 USD | 43,790.00 USD | 9,570.00 USD | 22,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.88` | 1,200,000.00 USD | 1,200,000.00 USD | 43,790.00 USD | 9,570.00 USD | 22,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.90` | 1,190,000.00 USD | 1,190,000.00 USD | 14,150.00 USD | 7,630.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 1,130,000.00 USD | 1,130,000.00 USD | 14,150.00 USD | 7,630.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 505.13 USD | 438,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.92` | 1,160,000.00 USD | 1,160,000.00 USD | 17,630.00 USD | 2,950.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.92` | 1,100,000.00 USD | 1,100,000.00 USD | 19,860.00 USD | 2,950.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 1,820.00 USD | 437,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 1,130,000.00 USD | 1,130,000.00 USD | 19,500.00 USD | 6,860.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.94` | 1,070,000.00 USD | 1,070,000.00 USD | 19,500.00 USD | 6,860.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 436,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.96` | 843.15 USD | 308,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 1,100,000.00 USD | 1,100,000.00 USD | 2,830.00 USD | 8,870.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.96` | 1,040,000.00 USD | 1,040,000.00 USD | 2,830.00 USD | 8,870.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.98` | 1,080,000.00 USD | 1,080,000.00 USD | 14,350.00 USD | 3,300.00 USD | 8,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.98` | 1,020,000.00 USD | 1,020,000.00 USD | 14,350.00 USD | 3,300.00 USD | 8,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,600.00 USD | 308,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.00` | 210.99 USD | 306,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 1,060,000.00 USD | 1,060,000.00 USD | 570.55 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.00` | 997,370.00 USD | 997,370.00 USD | 570.55 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 1,050,000.00 USD | 1,050,000.00 USD | 40,190.00 USD | 8,470.00 USD | 157.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.02` | 993,160.00 USD | 993,160.00 USD | 40,190.00 USD | 8,470.00 USD | 157.85 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 957.70 USD | 306,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.04` | 88,380.00 USD | 305,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.04` | 1,000,000.00 USD | 1,000,000.00 USD | 19,460.00 USD | 1,540.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.04` | 944,340.00 USD | 944,340.00 USD | 19,460.00 USD | 1,540.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 6,890.00 USD | 216,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 3,340.00 USD | 210,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.06` | 977,000.00 USD | 977,000.00 USD | 27,730.00 USD | 5,470.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.06` | 916,850.00 USD | 916,850.00 USD | 27,730.00 USD | 5,470.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 37,830.00 USD | 206,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.08` | 937,600.00 USD | 937,600.00 USD | 5,270.00 USD | 3,810.00 USD | 4,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.08` | 877,450.00 USD | 877,450.00 USD | 5,270.00 USD | 3,810.00 USD | 4,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 617.61 USD | 168,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.10` | 11,700.00 USD | 168,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.10` | 923,770.00 USD | 923,770.00 USD | 32,980.00 USD | 3,950.00 USD | 7,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.10` | 863,620.00 USD | 863,620.00 USD | 32,980.00 USD | 3,950.00 USD | 7,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 241.26 USD | 156,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 879,000.00 USD | 879,000.00 USD | 12,010.00 USD | 4,240.00 USD | 22,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.12` | 818,850.00 USD | 818,850.00 USD | 12,010.00 USD | 4,240.00 USD | 22,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 840,560.00 USD | 840,560.00 USD | 20,690.00 USD | 0.00 USD | 42.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.14` | 780,410.00 USD | 780,410.00 USD | 20,690.00 USD | 0.00 USD | 42.96 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 819,830.00 USD | 819,830.00 USD | 11,720.00 USD | 662.47 USD | 9,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 759,680.00 USD | 759,680.00 USD | 11,720.00 USD | 662.47 USD | 9,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.16` | 871.61 USD | 156,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.18` | 235.36 USD | 155,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.18` | 798,430.00 USD | 798,430.00 USD | 53,280.00 USD | 15,390.00 USD | 478.53 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 738,280.00 USD | 738,280.00 USD | 53,280.00 USD | 15,390.00 USD | 478.53 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.20` | 1,050.00 USD | 155,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.20` | 729,280.00 USD | 729,280.00 USD | 7,430.00 USD | 0.00 USD | 448.46 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.20` | 669,130.00 USD | 669,130.00 USD | 7,430.00 USD | 0.00 USD | 448.46 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 1,910.00 USD | 154,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.21` | 147.87 USD | 152,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.22` | 721,400.00 USD | 721,400.00 USD | 7,650.00 USD | 5,990.00 USD | 10,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.22` | 661,250.00 USD | 661,250.00 USD | 7,650.00 USD | 5,990.00 USD | 10,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.22` | 2,100.00 USD | 152,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.23` | 1,160.00 USD | 149,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.24` | 697,710.00 USD | 697,710.00 USD | 31,250.00 USD | 5,230.00 USD | 34,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 637,560.00 USD | 637,560.00 USD | 31,250.00 USD | 5,230.00 USD | 34,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.24` | 1,300.00 USD | 148,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.26` | 13,810.00 USD | 147,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.26` | 626,710.00 USD | 626,710.00 USD | 15,150.00 USD | 11,460.00 USD | 6,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.26` | 566,570.00 USD | 566,570.00 USD | 15,150.00 USD | 11,460.00 USD | 6,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.28` | 9,740.00 USD | 133,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.28` | 594,000.00 USD | 594,000.00 USD | 137,750.00 USD | 9,830.00 USD | 79,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.28` | 533,850.00 USD | 533,850.00 USD | 137,750.00 USD | 9,830.00 USD | 79,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 498.26 USD | 123,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.29` | 18,970.00 USD | 123,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.30` | 366,520.00 USD | 366,520.00 USD | 94,260.00 USD | 22,600.00 USD | 23,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.30` | 306,370.00 USD | 306,370.00 USD | 94,260.00 USD | 22,600.00 USD | 23,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.30` | 33,500.00 USD | 104,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.31` | 4,550.00 USD | 71,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.32` | 225,850.00 USD | 225,850.00 USD | 74,570.00 USD | 20,010.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.32` | 165,700.00 USD | 165,700.00 USD | 73,190.00 USD | 20,010.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.34` | 4,760.00 USD | 66,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.34` | 122,380.00 USD | 122,380.00 USD | 4,100.00 USD | 0.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.34` | 63,610.00 USD | 63,610.00 USD | 0.00 USD | 0.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.36` | 3,180.00 USD | 61,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.36` | 94,360.00 USD | 94,360.00 USD | 2,940.00 USD | 0.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.36` | 39,690.00 USD | 39,690.00 USD | 1,810.00 USD | 0.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.37` | 7,390.00 USD | 58,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.38` | 53,540.00 USD | 53,540.00 USD | 1,510.00 USD | 0.00 USD | 52,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.38` | 53,540.00 USD | 53,540.00 USD | 1,510.00 USD | 0.00 USD | 52,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.38` | 4,620.00 USD | 51,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.39` | 1,680.00 USD | 46,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.40` | 87,300.00 USD | 87,300.00 USD | 1,220.00 USD | 22,890.00 USD | 63,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.40` | 140,840.00 USD | 140,840.00 USD | 1,220.00 USD | 22,890.00 USD | 63,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.40` | 1,380.00 USD | 44,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.41` | 681.03 USD | 43,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.42` | 110,830.00 USD | 110,830.00 USD | 995.87 USD | 22,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.42` | 164,370.00 USD | 164,370.00 USD | 995.87 USD | 22,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.44` | 188.61 USD | 42,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.44` | 154,690.00 USD | 154,690.00 USD | 427.96 USD | 43,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.44` | 208,230.00 USD | 208,230.00 USD | 427.96 USD | 43,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.45` | 588.70 USD | 42,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.46` | 422.16 USD | 41,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.46` | 189,530.00 USD | 189,530.00 USD | 0.00 USD | 34,820.00 USD | 18.78 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.46` | 243,070.00 USD | 243,070.00 USD | 0.00 USD | 34,820.00 USD | 18.78 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.46` | 1,860.00 USD | 41,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.47` | 12,430.00 USD | 39,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.48` | 258,780.00 USD | 258,780.00 USD | 0.00 USD | 69,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.48` | 312,320.00 USD | 312,320.00 USD | 0.00 USD | 69,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.48` | 1,160.00 USD | 27,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.49` | 403.51 USD | 26,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.50` | 524,290.00 USD | 524,290.00 USD | 206,180.00 USD | 59,320.00 USD | 12.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.50` | 577,830.00 USD | 577,830.00 USD | 206,180.00 USD | 59,320.00 USD | 12.70 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.51` | 6,380.00 USD | 25,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.52` | 7,770.00 USD | 19,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.52` | 713,290.00 USD | 713,290.00 USD | 123,250.00 USD | 65,750.00 USD | 1.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.52` | 766,830.00 USD | 766,830.00 USD | 123,250.00 USD | 65,750.00 USD | 1.32 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 6,350.00 USD | 11,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.54` | 748,660.00 USD | 748,660.00 USD | 35,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.54` | 802,200.00 USD | 802,200.00 USD | 35,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 1,550.00 USD | 5,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 684.40 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.56` | 1,010,000.00 USD | 1,010,000.00 USD | 158,900.00 USD | 0.00 USD | 106,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.56` | 1,070,000.00 USD | 1,070,000.00 USD | 158,900.00 USD | 0.00 USD | 106,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.58` | 1,260,000.00 USD | 1,260,000.00 USD | 102,500.00 USD | 0.00 USD | 144,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.58` | 1,310,000.00 USD | 1,310,000.00 USD | 102,500.00 USD | 0.00 USD | 144,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.60` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 53,060.00 USD | 65,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.60` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 53,060.00 USD | 65,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.61` | 2,980.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.62` | 1,470,000.00 USD | 1,470,000.00 USD | 28,330.00 USD | 35,930.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.62` | 1,520,000.00 USD | 1,520,000.00 USD | 28,330.00 USD | 35,930.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 21,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.64` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 21,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.66` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 48,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.66` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 48,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 1,610,000.00 USD | 1,610,000.00 USD | 24,580.00 USD | 7,700.00 USD | 39,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.68` | 1,670,000.00 USD | 1,670,000.00 USD | 24,580.00 USD | 7,700.00 USD | 39,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.70` | 1,670,000.00 USD | 1,670,000.00 USD | 36,540.00 USD | 0.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.70` | 1,720,000.00 USD | 1,720,000.00 USD | 36,540.00 USD | 0.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 1,690,000.00 USD | 1,690,000.00 USD | 18,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.72` | 1,740,000.00 USD | 1,740,000.00 USD | 18,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 11,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.74` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 11,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.76` | 1,780,000.00 USD | 1,780,000.00 USD | 78,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.76` | 1,830,000.00 USD | 1,830,000.00 USD | 80,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.78` | 1,920,000.00 USD | 1,920,000.00 USD | 107,520.00 USD | 0.00 USD | 35,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.78` | 1,980,000.00 USD | 1,980,000.00 USD | 107,520.00 USD | 0.00 USD | 35,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.80` | 2,040,000.00 USD | 2,040,000.00 USD | 61,700.00 USD | 17,690.00 USD | 37,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.80` | 2,090,000.00 USD | 2,090,000.00 USD | 61,700.00 USD | 17,690.00 USD | 37,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.82` | 2,050,000.00 USD | 2,050,000.00 USD | 15,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.82` | 2,110,000.00 USD | 2,110,000.00 USD | 15,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 8,820.00 USD | 68,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.84` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 8,820.00 USD | 68,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 2,150,000.00 USD | 2,150,000.00 USD | 12,400.00 USD | 2,250.00 USD | 148.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.86` | 2,200,000.00 USD | 2,200,000.00 USD | 12,400.00 USD | 2,250.00 USD | 148.46 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 8,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.88` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 8,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 2,290,000.00 USD | 2,290,000.00 USD | 27,890.00 USD | 8,140.00 USD | 97,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.90` | 2,350,000.00 USD | 2,350,000.00 USD | 29,560.00 USD | 8,140.00 USD | 97,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 2,350,000.00 USD | 2,350,000.00 USD | 37,770.00 USD | 7,360.00 USD | 17,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.92` | 2,410,000.00 USD | 2,410,000.00 USD | 37,770.00 USD | 7,360.00 USD | 17,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 2,420,000.00 USD | 2,420,000.00 USD | 41,740.00 USD | 12,260.00 USD | 17,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.94` | 2,480,000.00 USD | 2,480,000.00 USD | 41,740.00 USD | 12,260.00 USD | 17,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.98` | 2,470,000.00 USD | 2,470,000.00 USD | 24,340.00 USD | 5,550.00 USD | 19,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.98` | 2,530,000.00 USD | 2,530,000.00 USD | 24,340.00 USD | 5,550.00 USD | 19,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.00` | 2,600,000.00 USD | 2,600,000.00 USD | 85,360.00 USD | 30,520.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.00` | 2,660,000.00 USD | 2,660,000.00 USD | 85,360.00 USD | 30,520.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 2,700,000.00 USD | 2,700,000.00 USD | 39,130.00 USD | 43,160.00 USD | 18,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.02` | 2,760,000.00 USD | 2,760,000.00 USD | 39,130.00 USD | 43,160.00 USD | 18,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 2,870,000.00 USD | 2,870,000.00 USD | 87,540.00 USD | 43,590.00 USD | 38,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.04` | 2,930,000.00 USD | 2,930,000.00 USD | 87,540.00 USD | 43,590.00 USD | 38,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.06` | 3,000,000.00 USD | 3,000,000.00 USD | 33,880.00 USD | 33,420.00 USD | 60,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.06` | 3,060,000.00 USD | 3,060,000.00 USD | 33,880.00 USD | 33,420.00 USD | 60,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 3,130,000.00 USD | 3,130,000.00 USD | 28,800.00 USD | 29,710.00 USD | 70,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.08` | 3,180,000.00 USD | 3,180,000.00 USD | 28,800.00 USD | 29,710.00 USD | 70,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.10` | 3,430,000.00 USD | 3,430,000.00 USD | 197,560.00 USD | 43,240.00 USD | 63,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.10` | 3,490,000.00 USD | 3,490,000.00 USD | 197,560.00 USD | 43,240.00 USD | 63,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 3,690,000.00 USD | 3,690,000.00 USD | 160,000.00 USD | 47,350.00 USD | 56,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.12` | 3,750,000.00 USD | 3,750,000.00 USD | 160,000.00 USD | 47,350.00 USD | 56,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.13` | 314.34 USD | 314.34 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.14` | 3,900,000.00 USD | 3,900,000.00 USD | 118,520.00 USD | 23,510.00 USD | 67,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.14` | 3,960,000.00 USD | 3,960,000.00 USD | 118,520.00 USD | 23,510.00 USD | 67,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 4,120,000.00 USD | 4,120,000.00 USD | 121,090.00 USD | 41,060.00 USD | 51,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.16` | 4,180,000.00 USD | 4,180,000.00 USD | 121,090.00 USD | 41,060.00 USD | 51,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 4,450,000.00 USD | 4,450,000.00 USD | 187,840.00 USD | 53,800.00 USD | 92,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.18` | 4,510,000.00 USD | 4,510,000.00 USD | 187,840.00 USD | 53,800.00 USD | 92,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.20` | 4,790,000.00 USD | 4,790,000.00 USD | 197,260.00 USD | 57,280.00 USD | 81,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 4,840,000.00 USD | 4,840,000.00 USD | 197,260.00 USD | 57,280.00 USD | 81,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.21` | 3,810.00 USD | 4,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.22` | 4,940,000.00 USD | 4,940,000.00 USD | 126,810.00 USD | 12,990.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.22` | 5,000,000.00 USD | 5,000,000.00 USD | 126,810.00 USD | 12,990.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 5,050,000.00 USD | 5,050,000.00 USD | 71,810.00 USD | 4,560.00 USD | 27,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 5,100,000.00 USD | 5,100,000.00 USD | 71,810.00 USD | 4,560.00 USD | 27,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 5,100,000.00 USD | 5,100,000.00 USD | 35,150.00 USD | 8,290.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 5,160,000.00 USD | 5,160,000.00 USD | 35,150.00 USD | 8,290.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 5,150,000.00 USD | 5,150,000.00 USD | 44,130.00 USD | 7,140.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 5,210,000.00 USD | 5,210,000.00 USD | 44,130.00 USD | 7,140.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 100.93 USD | 4,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.30` | 5,250,000.00 USD | 5,250,000.00 USD | 58,890.00 USD | 13,560.00 USD | 23,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.30` | 5,310,000.00 USD | 5,310,000.00 USD | 58,890.00 USD | 13,560.00 USD | 23,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 5,310,000.00 USD | 5,310,000.00 USD | 37,200.00 USD | 4,250.00 USD | 23,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.32` | 5,370,000.00 USD | 5,370,000.00 USD | 37,200.00 USD | 4,250.00 USD | 23,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 5,360,000.00 USD | 5,360,000.00 USD | 23,850.00 USD | 10,190.00 USD | 17,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.34` | 5,420,000.00 USD | 5,420,000.00 USD | 23,850.00 USD | 10,190.00 USD | 17,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.35` | 3,930.00 USD | 8,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.36` | 5,470,000.00 USD | 5,470,000.00 USD | 59,430.00 USD | 14,870.00 USD | 33,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.36` | 5,530,000.00 USD | 5,530,000.00 USD | 59,430.00 USD | 14,870.00 USD | 33,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 5,590,000.00 USD | 5,590,000.00 USD | 65,320.00 USD | 17,450.00 USD | 31,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.38` | 5,640,000.00 USD | 5,640,000.00 USD | 65,320.00 USD | 17,450.00 USD | 31,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.38` | 404,120.00 USD | 412,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.40` | 5,640,000.00 USD | 5,640,000.00 USD | 52,090.00 USD | 1,210.00 USD | 25.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.40` | 5,700,000.00 USD | 5,700,000.00 USD | 52,090.00 USD | 1,210.00 USD | 25.34 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 2,470.00 USD | 414,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 5,690,000.00 USD | 5,690,000.00 USD | 30,730.00 USD | 4,670.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.42` | 5,750,000.00 USD | 5,750,000.00 USD | 30,730.00 USD | 4,670.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 5,720,000.00 USD | 5,720,000.00 USD | 10,560.00 USD | 1,630.00 USD | 12,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 5,780,000.00 USD | 5,780,000.00 USD | 10,560.00 USD | 1,630.00 USD | 12,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.46` | 5,730,000.00 USD | 5,730,000.00 USD | 1,630.00 USD | 4,580.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 5,780,000.00 USD | 5,780,000.00 USD | 1,630.00 USD | 4,580.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.48` | 5,740,000.00 USD | 5,740,000.00 USD | 2,800.00 USD | 1,100.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.48` | 5,790,000.00 USD | 5,790,000.00 USD | 2,800.00 USD | 1,100.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.49` | 428.79 USD | 415,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.50` | 5,790,000.00 USD | 5,790,000.00 USD | 42,390.00 USD | 3,730.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 5,850,000.00 USD | 5,850,000.00 USD | 42,390.00 USD | 3,730.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.52` | 5,820,000.00 USD | 5,820,000.00 USD | 17,470.00 USD | 3,070.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 5,870,000.00 USD | 5,870,000.00 USD | 17,470.00 USD | 3,070.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.54` | 5,850,000.00 USD | 5,850,000.00 USD | 23,980.00 USD | 7,790.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 5,910,000.00 USD | 5,910,000.00 USD | 23,980.00 USD | 7,790.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.56` | 5,870,000.00 USD | 5,870,000.00 USD | 6,950.00 USD | 7,610.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 5,930,000.00 USD | 5,930,000.00 USD | 6,950.00 USD | 7,610.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.58` | 5,890,000.00 USD | 5,890,000.00 USD | 1,270.00 USD | 4,910.00 USD | 12,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 5,950,000.00 USD | 5,950,000.00 USD | 1,270.00 USD | 4,910.00 USD | 12,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.60` | 5,920,000.00 USD | 5,920,000.00 USD | 15,230.00 USD | 1,680.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 5,980,000.00 USD | 5,980,000.00 USD | 15,230.00 USD | 1,680.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.62` | 5,960,000.00 USD | 5,960,000.00 USD | 20,200.00 USD | 4,140.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 6,020,000.00 USD | 6,020,000.00 USD | 20,200.00 USD | 4,140.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.64` | 6,000,000.00 USD | 6,000,000.00 USD | 22,380.00 USD | 5,430.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.64` | 6,060,000.00 USD | 6,060,000.00 USD | 22,380.00 USD | 5,430.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.66` | 6,030,000.00 USD | 6,030,000.00 USD | 14,580.00 USD | 7,630.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.66` | 6,090,000.00 USD | 6,090,000.00 USD | 14,580.00 USD | 7,630.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.68` | 6,050,000.00 USD | 6,050,000.00 USD | 16,150.00 USD | 2,950.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.68` | 6,110,000.00 USD | 6,110,000.00 USD | 16,150.00 USD | 2,950.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.70` | 6,080,000.00 USD | 6,080,000.00 USD | 19,500.00 USD | 6,860.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.70` | 6,140,000.00 USD | 6,140,000.00 USD | 19,500.00 USD | 6,860.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.72` | 6,100,000.00 USD | 6,100,000.00 USD | 2,830.00 USD | 8,870.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.72` | 6,160,000.00 USD | 6,160,000.00 USD | 2,830.00 USD | 8,870.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 415,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.74` | 6,110,000.00 USD | 6,110,000.00 USD | 6,960.00 USD | 738.05 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.74` | 6,170,000.00 USD | 6,170,000.00 USD | 6,960.00 USD | 738.05 USD | 3,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.76` | 549.11 USD | 415,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.76` | 6,130,000.00 USD | 6,130,000.00 USD | 7,400.00 USD | 2,560.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.76` | 6,180,000.00 USD | 6,180,000.00 USD | 7,400.00 USD | 2,560.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.78` | 470.18 USD | 416,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.78` | 6,130,000.00 USD | 6,130,000.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.78` | 6,190,000.00 USD | 6,190,000.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.80` | 6,140,000.00 USD | 6,140,000.00 USD | 12,580.00 USD | 770.83 USD | 9.39 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.80` | 6,200,000.00 USD | 6,200,000.00 USD | 12,580.00 USD | 770.83 USD | 9.39 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.82` | 6,170,000.00 USD | 6,170,000.00 USD | 14,340.00 USD | 1,540.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.82` | 6,220,000.00 USD | 6,220,000.00 USD | 14,340.00 USD | 1,540.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.09` | 113.76 USD | 416,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.15` | 6,890.00 USD | 423,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.21` | 7,330.00 USD | 430,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.23` | 114.12 USD | 430,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 3,380.00 USD | 434,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 434,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.71` | 218.91 USD | 434,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.74` | 37,210.00 USD | 472,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.96` | 1,920.00 USD | 474,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 481,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,810.00 USD | 492,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 504,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.65` | 776.22 USD | 505,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.78` | 58,870.00 USD | 564,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.96` | 1,360.00 USD | 566,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.12` | 620.17 USD | 566,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 568,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 568,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.63` | 430.85 USD | 569,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.79` | 953.38 USD | 570,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.79` | 36,850.00 USD | 606,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.95` | 14,500.00 USD | 621,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.96` | 102.68 USD | 621,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 709,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 234,840.00 USD | 944,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 948,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 948,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 948,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.73` | 160.01 USD | 948,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.10` | 3,910.00 USD | 952,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 953,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.71` | 241.31 USD | 953,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.81` | 292.30 USD | 954,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.84` | 2,460.00 USD | 956,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.86` | 320.13 USD | 956,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 957,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 957,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 977,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.45` | 154,450.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.70` | 111.59 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.29` | 263,950.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.48` | 22,650.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.70` | 84,150.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 162.26 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.77` | 340.87 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.02` | 191.87 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.14` | 1,710.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.46` | 101.47 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.62` | 4,120.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.64` | 4,930.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.66` | 2,660.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.70` | 108.89 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.85` | 2,320,000.00 USD | 0.00 USD | 204.05 USD | `-79.04%` | `110.00` |
| `Live` | `Long` | `1.97` | 2,320,000.00 USD | 0.00 USD | 102.18 USD | `-77.80%` | `52.00` |
| `Live` | `Long` | `2.00` | 2,320,000.00 USD | 0.00 USD | 159.60 USD | `-77.46%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,320,000.00 USD | 0.00 USD | 110.52 USD | `-77.01%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,320,000.00 USD | 0.00 USD | 1,910.00 USD | `-76.78%` | `929.47` |
| `Live` | `Long` | `2.06` | 2,310,000.00 USD | 0.00 USD | 4,920.00 USD | `-76.67%` | `2,382.76` |
| `Live` | `Long` | `2.38` | 2,310,000.00 USD | 0.00 USD | 262.35 USD | `-73.05%` | `110.00` |
| `Live` | `Long` | `2.40` | 2,310,000.00 USD | 0.00 USD | 391.63 USD | `-72.83%` | `162.84` |
| `Live` | `Long` | `2.42` | 2,310,000.00 USD | 0.00 USD | 918.27 USD | `-72.60%` | `378.67` |
| `Live` | `Long` | `2.46` | 2,310,000.00 USD | 0.00 USD | 17,160.00 USD | `-72.26%` | `6,990.57` |
| `Live` | `Long` | `2.73` | 2,290,000.00 USD | 0.00 USD | 282.66 USD | `-69.21%` | `103.73` |
| `Live` | `Long` | `2.75` | 2,290,000.00 USD | 0.00 USD | 270.19 USD | `-68.99%` | `98.43` |
| `Live` | `Long` | `2.81` | 2,290,000.00 USD | 0.00 USD | 627.44 USD | `-68.19%` | `222.89` |
| `Live` | `Long` | `2.83` | 2,290,000.00 USD | 0.00 USD | 140.18 USD | `-68.08%` | `49.62` |
| `Live` | `Long` | `2.87` | 2,290,000.00 USD | 0.00 USD | 232.67 USD | `-67.63%` | `81.21` |
| `Live` | `Long` | `2.94` | 2,290,000.00 USD | 0.00 USD | 44,510.00 USD | `-66.84%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,250,000.00 USD | 0.00 USD | 1,230.00 USD | `-66.39%` | `415.06` |
| `Live` | `Long` | `3.23` | 2,240,000.00 USD | 0.00 USD | 1,520.00 USD | `-63.56%` | `470.82` |
| `Live` | `Long` | `3.23` | 2,240,000.00 USD | 0.00 USD | 404.38 USD | `-63.45%` | `125.00` |
| `Live` | `Long` | `3.25` | 2,240,000.00 USD | 0.00 USD | 109.42 USD | `-63.34%` | `33.72` |
| `Live` | `Long` | `3.31` | 2,240,000.00 USD | 0.00 USD | 712.82 USD | `-62.55%` | `215.03` |
| `Live` | `Long` | `3.37` | 2,240,000.00 USD | 0.00 USD | 389.53 USD | `-61.98%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,240,000.00 USD | 0.00 USD | 297.24 USD | `-61.87%` | `88.07` |
| `Live` | `Long` | `3.67` | 2,240,000.00 USD | 0.00 USD | 109.95 USD | `-58.59%` | `30.00` |
| `Live` | `Long` | `3.69` | 2,240,000.00 USD | 0.00 USD | 325.98 USD | `-58.37%` | `88.46` |
| `Live` | `Long` | `3.75` | 2,240,000.00 USD | 0.00 USD | 1,500.00 USD | `-57.57%` | `400.00` |
| `Live` | `Long` | `3.90` | 2,240,000.00 USD | 0.00 USD | 131.73 USD | `-55.99%` | `33.82` |
| `Live` | `Long` | `3.96` | 2,240,000.00 USD | 0.00 USD | 8,990.00 USD | `-55.31%` | `2,273.34` |
| `Live` | `Long` | `3.98` | 2,230,000.00 USD | 0.00 USD | 371.88 USD | `-54.98%` | `93.32` |
| `Live` | `Long` | `4.01` | 2,230,000.00 USD | 0.00 USD | 401.50 USD | `-54.64%` | `100.00` |
| `Live` | `Long` | `4.03` | 2,230,000.00 USD | 0.00 USD | 402.70 USD | `-54.52%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,230,000.00 USD | 0.00 USD | 152.29 USD | `-54.30%` | `37.65` |
| `Live` | `Long` | `4.08` | 2,230,000.00 USD | 0.00 USD | 2,320.00 USD | `-53.85%` | `568.43` |
| `Live` | `Long` | `4.14` | 2,230,000.00 USD | 0.00 USD | 1,130.00 USD | `-53.17%` | `272.03` |
| `Live` | `Long` | `4.18` | 2,220,000.00 USD | 0.00 USD | 174.89 USD | `-52.72%` | `41.79` |
| `Live` | `Long` | `4.22` | 2,220,000.00 USD | 0.00 USD | 171.58 USD | `-52.26%` | `40.61` |
| `Live` | `Long` | `4.24` | 2,220,000.00 USD | 0.00 USD | 169.40 USD | `-52.15%` | `40.00` |
| `Live` | `Long` | `4.26` | 2,220,000.00 USD | 0.00 USD | 106.63 USD | `-51.81%` | `25.00` |
| `Live` | `Long` | `4.29` | 2,220,000.00 USD | 0.00 USD | 115.97 USD | `-51.47%` | `27.00` |
| `Live` | `Long` | `4.32` | 2,220,000.00 USD | 0.00 USD | 852.47 USD | `-51.25%` | `197.56` |
| `Live` | `Long` | `4.42` | 2,220,000.00 USD | 0.00 USD | 2,230.00 USD | `-50.00%` | `504.56` |
| `Live` | `Long` | `4.59` | 2,220,000.00 USD | 0.00 USD | 30,970.00 USD | `-48.08%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,190,000.00 USD | 0.00 USD | 486.93 USD | `-47.86%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,190,000.00 USD | 0.00 USD | 2,680.00 USD | `-47.74%` | `579.06` |
| `Live` | `Long` | `4.64` | 2,190,000.00 USD | 0.00 USD | 223.98 USD | `-47.52%` | `48.22` |
| `Live` | `Long` | `4.66` | 2,190,000.00 USD | 0.00 USD | 105.11 USD | `-47.41%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,190,000.00 USD | 0.00 USD | 3,280.00 USD | `-47.29%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,180,000.00 USD | 0.00 USD | 1,490.00 USD | `-47.18%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,180,000.00 USD | 0.00 USD | 9,060.00 USD | `-47.07%` | `1,933.95` |
| `Live` | `Long` | `4.70` | 2,170,000.00 USD | 0.00 USD | 7,040.00 USD | `-46.95%` | `1,500.00` |
| `Live` | `Long` | `4.75` | 2,170,000.00 USD | 0.00 USD | 240.48 USD | `-46.39%` | `50.68` |
| `Live` | `Long` | `4.76` | 2,170,000.00 USD | 0.00 USD | 105.64 USD | `-46.16%` | `22.17` |
| `Live` | `Long` | `4.79` | 2,170,000.00 USD | 0.00 USD | 5,050.00 USD | `-45.82%` | `1,053.00` |
| `Live` | `Long` | `4.82` | 2,160,000.00 USD | 0.00 USD | 17,120.00 USD | `-45.60%` | `3,556.00` |
| `Live` | `Long` | `4.83` | 2,140,000.00 USD | 0.00 USD | 467.01 USD | `-45.37%` | `96.59` |
| `Live` | `Long` | `4.88` | 2,140,000.00 USD | 0.00 USD | 113.33 USD | `-44.81%` | `23.20` |
| `Live` | `Long` | `4.89` | 2,140,000.00 USD | 0.00 USD | 146.85 USD | `-44.69%` | `30.00` |
| `Live` | `Long` | `4.91` | 2,140,000.00 USD | 0.00 USD | 527.19 USD | `-44.58%` | `107.48` |
| `Live` | `Long` | `4.92` | 2,140,000.00 USD | 0.00 USD | 1,230.00 USD | `-44.47%` | `251.00` |
| `Live` | `Long` | `4.96` | 2,140,000.00 USD | 0.00 USD | 945.36 USD | `-44.02%` | `190.79` |
| `Live` | `Long` | `4.97` | 2,140,000.00 USD | 0.00 USD | 282.23 USD | `-43.79%` | `56.73` |
| `Live` | `Long` | `4.99` | 2,140,000.00 USD | 0.00 USD | 329.11 USD | `-43.68%` | `66.02` |
| `Live` | `Long` | `5.01` | 2,140,000.00 USD | 0.00 USD | 56,390.00 USD | `-43.34%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,080,000.00 USD | 0.00 USD | 167.78 USD | `-43.23%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,080,000.00 USD | 0.00 USD | 314.59 USD | `-43.11%` | `62.48` |
| `Live` | `Long` | `5.05` | 2,080,000.00 USD | 0.00 USD | 504.74 USD | `-42.89%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,080,000.00 USD | 0.00 USD | 805.91 USD | `-42.66%` | `158.80` |
| `Live` | `Long` | `5.09` | 2,080,000.00 USD | 0.00 USD | 4,200.00 USD | `-42.43%` | `824.62` |
| `Live` | `Long` | `5.12` | 2,080,000.00 USD | 0.00 USD | 250.20 USD | `-42.10%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,080,000.00 USD | 0.00 USD | 396.06 USD | `-41.98%` | `77.13` |
| `Live` | `Long` | `5.14` | 2,080,000.00 USD | 0.00 USD | 156,590.00 USD | `-41.87%` | `30,435.20` |
| `Live` | `Long` | `5.17` | 1,920,000.00 USD | 0.00 USD | 2,300.00 USD | `-41.64%` | `445.16` |
| `Live` | `Long` | `5.17` | 1,920,000.00 USD | 0.00 USD | 1,620.00 USD | `-41.53%` | `312.94` |
| `Live` | `Long` | `5.18` | 1,920,000.00 USD | 0.00 USD | 150.57 USD | `-41.42%` | `29.04` |
| `Live` | `Long` | `5.21` | 1,920,000.00 USD | 0.00 USD | 300.91 USD | `-41.08%` | `57.70` |
| `Live` | `Long` | `5.29` | 1,910,000.00 USD | 0.00 USD | 640.70 USD | `-40.29%` | `121.23` |
| `Live` | `Long` | `5.29` | 1,910,000.00 USD | 0.00 USD | 2,650.00 USD | `-40.17%` | `500.00` |
| `Live` | `Long` | `5.32` | 1,910,000.00 USD | 0.00 USD | 232.85 USD | `-39.95%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,910,000.00 USD | 0.00 USD | 716.11 USD | `-39.84%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,910,000.00 USD | 0.00 USD | 660.46 USD | `-39.05%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,910,000.00 USD | 0.00 USD | 21,080.00 USD | `-38.82%` | `3,892.05` |
| `Live` | `Long` | `5.42` | 1,890,000.00 USD | 0.00 USD | 160,400.00 USD | `-38.71%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,730,000.00 USD | 0.00 USD | 1,360.00 USD | `-38.59%` | `250.00` |
| `Live` | `Long` | `5.46` | 1,730,000.00 USD | 0.00 USD | 264.72 USD | `-38.25%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,730,000.00 USD | 0.00 USD | 1,320.00 USD | `-38.14%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,730,000.00 USD | 0.00 USD | 354.06 USD | `-38.03%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,730,000.00 USD | 0.00 USD | 19,290.00 USD | `-37.92%` | `3,510.41` |
| `Live` | `Long` | `5.51` | 1,710,000.00 USD | 0.00 USD | 367.41 USD | `-37.69%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,710,000.00 USD | 0.00 USD | 121.38 USD | `-37.46%` | `21.93` |
| `Live` | `Long` | `5.57` | 1,710,000.00 USD | 0.00 USD | 967.98 USD | `-37.12%` | `173.94` |
| `Live` | `Long` | `5.58` | 1,700,000.00 USD | 0.00 USD | 63,260.00 USD | `-37.01%` | `11,347.58` |
| `Live` | `Long` | `5.59` | 1,640,000.00 USD | 0.00 USD | 34,430.00 USD | `-36.79%` | `6,153.60` |
| `Live` | `Long` | `5.63` | 1,610,000.00 USD | 0.00 USD | 22,270.00 USD | `-36.33%` | `3,952.96` |
| `Live` | `Long` | `5.66` | 1,580,000.00 USD | 0.00 USD | 4,160.00 USD | `-36.11%` | `734.88` |
| `Live` | `Long` | `5.71` | 1,580,000.00 USD | 0.00 USD | 2,340.00 USD | `-35.54%` | `409.39` |
| `Live` | `Long` | `5.71` | 1,580,000.00 USD | 0.00 USD | 406.45 USD | `-35.43%` | `71.12` |
| `Live` | `Long` | `5.74` | 1,580,000.00 USD | 0.00 USD | 869.71 USD | `-35.20%` | `151.65` |
| `Live` | `Long` | `5.75` | 1,580,000.00 USD | 0.00 USD | 125.70 USD | `-35.09%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,580,000.00 USD | 0.00 USD | 3,190.00 USD | `-34.98%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,570,000.00 USD | 0.00 USD | 10,850.00 USD | `-34.86%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,560,000.00 USD | 0.00 USD | 801.40 USD | `-34.75%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,560,000.00 USD | 0.00 USD | 2,890.00 USD | `-34.64%` | `500.00` |
| `Live` | `Long` | `5.79` | 1,560,000.00 USD | 0.00 USD | 736.72 USD | `-34.53%` | `127.13` |
| `Live` | `Long` | `5.80` | 1,560,000.00 USD | 0.00 USD | 580.50 USD | `-34.41%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,560,000.00 USD | 0.00 USD | 106.65 USD | `-34.30%` | `18.34` |
| `Live` | `Long` | `5.84` | 1,560,000.00 USD | 0.00 USD | 327,670.00 USD | `-33.96%` | `56,059.40` |
| `Live` | `Long` | `5.89` | 1,230,000.00 USD | 0.00 USD | 640.67 USD | `-33.40%` | `108.68` |
| `Live` | `Long` | `5.91` | 1,230,000.00 USD | 0.00 USD | 399.18 USD | `-33.28%` | `67.60` |
| `Live` | `Long` | `5.92` | 1,230,000.00 USD | 0.00 USD | 336.30 USD | `-33.06%` | `56.76` |
| `Live` | `Long` | `5.96` | 1,230,000.00 USD | 0.00 USD | 12,120.00 USD | `-32.72%` | `2,035.32` |
| `Live` | `Long` | `5.97` | 1,220,000.00 USD | 0.00 USD | 585.97 USD | `-32.49%` | `98.07` |
| `Live` | `Long` | `5.99` | 1,220,000.00 USD | 0.00 USD | 447.98 USD | `-32.38%` | `74.85` |
| `Live` | `Long` | `6.00` | 1,220,000.00 USD | 0.00 USD | 341.56 USD | `-32.15%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,210,000.00 USD | 0.00 USD | 446.85 USD | `-32.04%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,210,000.00 USD | 0.00 USD | 331.68 USD | `-31.81%` | `54.96` |
| `Live` | `Long` | `6.04` | 1,210,000.00 USD | 0.00 USD | 105.61 USD | `-31.70%` | `17.47` |
| `Live` | `Long` | `6.05` | 1,210,000.00 USD | 0.00 USD | 1,310.00 USD | `-31.59%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,210,000.00 USD | 0.00 USD | 265.10 USD | `-31.48%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,210,000.00 USD | 0.00 USD | 3,060.00 USD | `-31.36%` | `504.08` |
| `Live` | `Long` | `6.08` | 1,210,000.00 USD | 0.00 USD | 405.14 USD | `-31.25%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,210,000.00 USD | 0.00 USD | 3,550.00 USD | `-31.14%` | `582.81` |
| `Live` | `Long` | `6.11` | 1,210,000.00 USD | 0.00 USD | 3,200.00 USD | `-31.02%` | `524.73` |
| `Live` | `Long` | `6.12` | 1,200,000.00 USD | 0.00 USD | 2,500.00 USD | `-30.80%` | `408.83` |
| `Live` | `Long` | `6.14` | 1,200,000.00 USD | 0.00 USD | 238.61 USD | `-30.57%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,200,000.00 USD | 0.00 USD | 4,390.00 USD | `-30.46%` | `713.75` |
| `Live` | `Long` | `6.17` | 1,200,000.00 USD | 0.00 USD | 187.29 USD | `-30.35%` | `30.38` |
| `Live` | `Long` | `6.17` | 1,190,000.00 USD | 0.00 USD | 104.36 USD | `-30.23%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,190,000.00 USD | 0.00 USD | 310.25 USD | `-29.89%` | `50.00` |
| `Live` | `Long` | `6.21` | 1,190,000.00 USD | 0.00 USD | 4,150.00 USD | `-29.78%` | `667.50` |
| `Live` | `Long` | `6.22` | 1,190,000.00 USD | 0.00 USD | 715.31 USD | `-29.67%` | `114.91` |
| `Live` | `Long` | `6.25` | 1,190,000.00 USD | 0.00 USD | 972.65 USD | `-29.33%` | `155.50` |
| `Live` | `Long` | `6.28` | 1,190,000.00 USD | 0.00 USD | 2,510.00 USD | `-29.10%` | `400.00` |
| `Live` | `Long` | `6.29` | 1,190,000.00 USD | 0.00 USD | 147.51 USD | `-28.99%` | `23.47` |
| `Live` | `Long` | `6.32` | 1,190,000.00 USD | 0.00 USD | 1,740.00 USD | `-28.65%` | `276.04` |
| `Live` | `Long` | `6.33` | 1,180,000.00 USD | 0.00 USD | 105.25 USD | `-28.54%` | `16.64` |
| `Live` | `Long` | `6.36` | 1,180,000.00 USD | 0.00 USD | 4,470.00 USD | `-28.20%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,180,000.00 USD | 0.00 USD | 284,770.00 USD | `-28.09%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 894,990.00 USD | 0.00 USD | 5,110.00 USD | `-27.97%` | `801.31` |
| `Live` | `Long` | `6.42` | 889,880.00 USD | 0.00 USD | 306.32 USD | `-27.52%` | `47.75` |
| `Live` | `Long` | `6.42` | 889,580.00 USD | 0.00 USD | 1,700.00 USD | `-27.41%` | `265.15` |
| `Live` | `Long` | `6.43` | 887,870.00 USD | 0.00 USD | 6,780.00 USD | `-27.29%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 881,100.00 USD | 0.00 USD | 1,050.00 USD | `-26.96%` | `162.75` |
| `Live` | `Long` | `6.54` | 880,040.00 USD | 0.00 USD | 3,620.00 USD | `-26.16%` | `554.55` |
| `Live` | `Long` | `6.54` | 876,420.00 USD | 0.00 USD | 8,970.00 USD | `-26.05%` | `1,370.89` |
| `Live` | `Long` | `6.58` | 867,450.00 USD | 0.00 USD | 1,100.00 USD | `-25.60%` | `166.55` |
| `Live` | `Long` | `6.61` | 866,350.00 USD | 0.00 USD | 409.51 USD | `-25.37%` | `62.00` |
| `Live` | `Long` | `6.62` | 865,940.00 USD | 0.00 USD | 2,110.00 USD | `-25.26%` | `318.57` |
| `Live` | `Long` | `6.62` | 863,830.00 USD | 0.00 USD | 2,190.00 USD | `-25.15%` | `330.00` |
| `Live` | `Long` | `6.70` | 861,650.00 USD | 0.00 USD | 506.54 USD | `-24.36%` | `75.66` |
| `Live` | `Long` | `6.71` | 861,140.00 USD | 0.00 USD | 16,610.00 USD | `-24.24%` | `2,477.79` |
| `Live` | `Long` | `6.75` | 844,530.00 USD | 0.00 USD | 1,330.00 USD | `-23.79%` | `196.95` |
| `Live` | `Long` | `6.78` | 843,200.00 USD | 0.00 USD | 6,780.00 USD | `-23.45%` | `1,000.00` |
| `Live` | `Long` | `6.79` | 836,420.00 USD | 0.00 USD | 16,960.00 USD | `-23.34%` | `2,500.00` |
| `Live` | `Long` | `6.79` | 819,460.00 USD | 0.00 USD | 4,260.00 USD | `-23.23%` | `626.24` |
| `Live` | `Long` | `6.80` | 815,210.00 USD | 0.00 USD | 1,500.00 USD | `-23.11%` | `220.95` |
| `Live` | `Long` | `6.82` | 813,700.00 USD | 0.00 USD | 2,670.00 USD | `-23.00%` | `391.11` |
| `Live` | `Long` | `6.83` | 811,040.00 USD | 0.00 USD | 158.14 USD | `-22.89%` | `23.17` |
| `Live` | `Long` | `6.83` | 810,880.00 USD | 0.00 USD | 4,410.00 USD | `-22.78%` | `644.73` |
| `Live` | `Long` | `6.86` | 806,470.00 USD | 0.00 USD | 18,930.00 USD | `-22.55%` | `2,761.63` |
| `Live` | `Long` | `6.87` | 787,540.00 USD | 0.00 USD | 3,340.00 USD | `-22.44%` | `486.46` |
| `Live` | `Long` | `6.88` | 784,200.00 USD | 0.00 USD | 1,380.00 USD | `-22.32%` | `200.00` |
| `Live` | `Long` | `6.89` | 782,830.00 USD | 0.00 USD | 5,250.00 USD | `-22.10%` | `761.63` |
| `Live` | `Long` | `6.91` | 777,580.00 USD | 0.00 USD | 269.30 USD | `-21.98%` | `39.00` |
| `Live` | `Long` | `6.92` | 777,310.00 USD | 0.00 USD | 27,700.00 USD | `-21.76%` | `4,000.00` |
| `Live` | `Long` | `6.95` | 749,610.00 USD | 0.00 USD | 3,760.00 USD | `-21.53%` | `541.68` |
| `Live` | `Long` | `6.96` | 745,840.00 USD | 0.00 USD | 3,480.00 USD | `-21.42%` | `500.00` |
| `Live` | `Long` | `6.96` | 742,370.00 USD | 0.00 USD | 636.74 USD | `-21.31%` | `91.42` |
| `Live` | `Long` | `7.00` | 741,730.00 USD | 0.00 USD | 746.58 USD | `-20.97%` | `106.73` |
| `Live` | `Long` | `7.00` | 740,980.00 USD | 0.00 USD | 20,860.00 USD | `-20.85%` | `2,978.11` |
| `Live` | `Long` | `7.01` | 720,120.00 USD | 0.00 USD | 1,530.00 USD | `-20.74%` | `217.70` |
| `Live` | `Long` | `7.03` | 718,590.00 USD | 0.00 USD | 3,390.00 USD | `-20.63%` | `482.43` |
| `Live` | `Long` | `7.04` | 715,210.00 USD | 0.00 USD | 4,100.00 USD | `-20.40%` | `581.44` |
| `Live` | `Long` | `7.08` | 711,110.00 USD | 0.00 USD | 6,700.00 USD | `-20.06%` | `947.44` |
| `Live` | `Long` | `7.08` | 704,410.00 USD | 0.00 USD | 1,670.00 USD | `-19.95%` | `236.20` |
| `Live` | `Long` | `7.11` | 702,730.00 USD | 0.00 USD | 29,850.00 USD | `-19.72%` | `4,201.02` |
| `Live` | `Long` | `7.12` | 672,880.00 USD | 0.00 USD | 379.66 USD | `-19.61%` | `53.36` |
| `Live` | `Long` | `7.13` | 672,500.00 USD | 0.00 USD | 2,300.00 USD | `-19.39%` | `322.72` |
| `Live` | `Long` | `7.14` | 670,200.00 USD | 0.00 USD | 20,950.00 USD | `-19.27%` | `2,931.56` |
| `Live` | `Long` | `7.18` | 649,260.00 USD | 0.00 USD | 1,440.00 USD | `-18.82%` | `200.00` |
| `Live` | `Long` | `7.21` | 647,820.00 USD | 0.00 USD | 581.02 USD | `-18.48%` | `80.53` |
| `Live` | `Long` | `7.22` | 647,240.00 USD | 0.00 USD | 833.26 USD | `-18.37%` | `115.33` |
| `Live` | `Long` | `7.24` | 646,400.00 USD | 0.00 USD | 179.65 USD | `-18.26%` | `24.83` |
| `Live` | `Long` | `7.25` | 646,230.00 USD | 0.00 USD | 185.83 USD | `-18.14%` | `25.65` |
| `Live` | `Long` | `7.29` | 646,040.00 USD | 0.00 USD | 36,420.00 USD | `-17.69%` | `5,000.00` |
| `Live` | `Long` | `7.29` | 609,610.00 USD | 0.00 USD | 19,790.00 USD | `-17.58%` | `2,712.69` |
| `Live` | `Long` | `7.32` | 589,830.00 USD | 0.00 USD | 168.76 USD | `-17.35%` | `23.07` |
| `Live` | `Long` | `7.33` | 589,660.00 USD | 0.00 USD | 5,050.00 USD | `-17.24%` | `688.93` |
| `Live` | `Long` | `7.33` | 584,610.00 USD | 0.00 USD | 2,450.00 USD | `-17.13%` | `333.54` |
| `Live` | `Long` | `7.34` | 582,160.00 USD | 0.00 USD | 4,370.00 USD | `-17.01%` | `594.84` |
| `Live` | `Long` | `7.37` | 577,790.00 USD | 0.00 USD | 5,720.00 USD | `-16.79%` | `776.95` |
| `Live` | `Long` | `7.38` | 572,070.00 USD | 0.00 USD | 3,920.00 USD | `-16.67%` | `531.65` |
| `Live` | `Long` | `7.38` | 568,150.00 USD | 0.00 USD | 17,770.00 USD | `-16.56%` | `2,406.10` |
| `Live` | `Long` | `7.39` | 550,380.00 USD | 0.00 USD | 2,590.00 USD | `-16.45%` | `350.17` |
| `Live` | `Long` | `7.42` | 547,790.00 USD | 0.00 USD | 500.00 USD | `-16.11%` | `67.34` |
| `Live` | `Long` | `7.43` | 547,290.00 USD | 0.00 USD | 1,490.00 USD | `-16.00%` | `200.00` |
| `Live` | `Long` | `7.45` | 545,810.00 USD | 0.00 USD | 210.99 USD | `-15.88%` | `28.34` |
| `Live` | `Long` | `7.46` | 545,590.00 USD | 0.00 USD | 1,370.00 USD | `-15.77%` | `183.84` |
| `Live` | `Long` | `7.46` | 544,220.00 USD | 0.00 USD | 9,160.00 USD | `-15.66%` | `1,227.40` |
| `Live` | `Long` | `7.47` | 535,060.00 USD | 0.00 USD | 3,210.00 USD | `-15.54%` | `430.09` |
| `Live` | `Long` | `7.50` | 531,850.00 USD | 0.00 USD | 1,580.00 USD | `-15.32%` | `211.22` |
| `Live` | `Long` | `7.50` | 530,260.00 USD | 0.00 USD | 1,080.00 USD | `-15.21%` | `143.74` |
| `Live` | `Long` | `7.53` | 529,190.00 USD | 0.00 USD | 995.86 USD | `-14.98%` | `132.34` |
| `Live` | `Long` | `7.54` | 528,190.00 USD | 0.00 USD | 4,210.00 USD | `-14.87%` | `559.01` |
| `Live` | `Long` | `7.55` | 523,980.00 USD | 0.00 USD | 157.14 USD | `-14.64%` | `20.80` |
| `Live` | `Long` | `7.58` | 523,820.00 USD | 0.00 USD | 4,380.00 USD | `-14.41%` | `578.50` |
| `Live` | `Long` | `7.59` | 519,440.00 USD | 0.00 USD | 25,140.00 USD | `-14.19%` | `3,310.14` |
| `Live` | `Long` | `7.62` | 494,300.00 USD | 0.00 USD | 312.22 USD | `-13.96%` | `41.00` |
| `Live` | `Long` | `7.62` | 493,990.00 USD | 0.00 USD | 787.51 USD | `-13.85%` | `103.28` |
| `Live` | `Long` | `7.63` | 493,200.00 USD | 0.00 USD | 514.52 USD | `-13.74%` | `67.39` |
| `Live` | `Long` | `7.66` | 492,680.00 USD | 0.00 USD | 135.42 USD | `-13.51%` | `17.69` |
| `Live` | `Long` | `7.67` | 492,550.00 USD | 0.00 USD | 1,740.00 USD | `-13.40%` | `226.45` |
| `Live` | `Long` | `7.68` | 490,810.00 USD | 0.00 USD | 1,120.00 USD | `-13.17%` | `145.25` |
| `Live` | `Long` | `7.70` | 489,700.00 USD | 0.00 USD | 1,460.00 USD | `-13.06%` | `190.36` |
| `Live` | `Long` | `7.71` | 488,230.00 USD | 0.00 USD | 19,760.00 USD | `-12.95%` | `2,564.20` |
| `Live` | `Long` | `7.72` | 468,470.00 USD | 0.00 USD | 2,550.00 USD | `-12.72%` | `330.65` |
| `Live` | `Long` | `7.75` | 465,920.00 USD | 0.00 USD | 893.76 USD | `-12.38%` | `115.25` |
| `Live` | `Long` | `7.76` | 465,030.00 USD | 0.00 USD | 455.73 USD | `-12.27%` | `58.69` |
| `Live` | `Long` | `7.78` | 464,570.00 USD | 0.00 USD | 695.32 USD | `-12.15%` | `89.43` |
| `Live` | `Long` | `7.79` | 463,870.00 USD | 0.00 USD | 3,900.00 USD | `-12.04%` | `500.57` |
| `Live` | `Long` | `7.79` | 459,980.00 USD | 0.00 USD | 1,940.00 USD | `-11.93%` | `248.84` |
| `Live` | `Long` | `7.80` | 458,040.00 USD | 0.00 USD | 633.77 USD | `-11.82%` | `81.20` |
| `Live` | `Long` | `7.82` | 457,400.00 USD | 0.00 USD | 5,280.00 USD | `-11.70%` | `675.43` |
| `Live` | `Long` | `7.84` | 452,130.00 USD | 0.00 USD | 10,930.00 USD | `-11.36%` | `1,393.53` |
| `Live` | `Long` | `7.86` | 441,190.00 USD | 0.00 USD | 2,110.00 USD | `-11.25%` | `269.14` |
| `Live` | `Long` | `7.87` | 439,080.00 USD | 0.00 USD | 176.18 USD | `-11.14%` | `22.40` |
| `Live` | `Long` | `7.88` | 438,900.00 USD | 0.00 USD | 555.19 USD | `-11.02%` | `70.50` |
| `Live` | `Long` | `7.91` | 438,350.00 USD | 0.00 USD | 505.13 USD | `-10.69%` | `63.90` |
| `Live` | `Long` | `7.93` | 437,840.00 USD | 0.00 USD | 1,820.00 USD | `-10.35%` | `228.88` |
| `Live` | `Long` | `7.95` | 436,030.00 USD | 0.00 USD | 127,110.00 USD | `-10.23%` | `15,999.24` |
| `Live` | `Long` | `7.96` | 308,910.00 USD | 0.00 USD | 843.15 USD | `-10.12%` | `105.99` |
| `Live` | `Long` | `7.99` | 308,070.00 USD | 0.00 USD | 1,600.00 USD | `-9.78%` | `200.68` |
| `Live` | `Long` | `8.00` | 306,470.00 USD | 0.00 USD | 210.99 USD | `-9.67%` | `26.39` |
| `Live` | `Long` | `8.03` | 306,260.00 USD | 0.00 USD | 957.70 USD | `-9.33%` | `119.34` |
| `Live` | `Long` | `8.04` | 305,300.00 USD | 0.00 USD | 88,380.00 USD | `-9.22%` | `10,999.50` |
| `Live` | `Long` | `8.04` | 216,920.00 USD | 0.00 USD | 6,890.00 USD | `-9.10%` | `856.44` |
| `Live` | `Long` | `8.05` | 210,030.00 USD | 0.00 USD | 3,340.00 USD | `-8.99%` | `414.27` |
| `Live` | `Long` | `8.06` | 206,690.00 USD | 0.00 USD | 37,830.00 USD | `-8.88%` | `4,690.67` |
| `Live` | `Long` | `8.09` | 168,860.00 USD | 0.00 USD | 617.61 USD | `-8.65%` | `76.39` |
| `Live` | `Long` | `8.10` | 168,240.00 USD | 0.00 USD | 11,700.00 USD | `-8.54%` | `1,445.70` |
| `Live` | `Long` | `8.12` | 156,540.00 USD | 0.00 USD | 241.26 USD | `-8.31%` | `29.73` |
| `Live` | `Long` | `8.16` | 156,300.00 USD | 0.00 USD | 871.61 USD | `-7.75%` | `106.75` |
| `Live` | `Long` | `8.18` | 155,430.00 USD | 0.00 USD | 235.36 USD | `-7.64%` | `28.79` |
| `Live` | `Long` | `8.20` | 155,190.00 USD | 0.00 USD | 1,050.00 USD | `-7.41%` | `128.30` |
| `Live` | `Long` | `8.21` | 154,140.00 USD | 0.00 USD | 1,910.00 USD | `-7.30%` | `232.19` |
| `Live` | `Long` | `8.21` | 152,230.00 USD | 0.00 USD | 147.87 USD | `-7.18%` | `18.00` |
| `Live` | `Long` | `8.22` | 152,090.00 USD | 0.00 USD | 2,100.00 USD | `-7.07%` | `255.16` |
| `Live` | `Long` | `8.23` | 149,990.00 USD | 0.00 USD | 1,160.00 USD | `-6.96%` | `140.81` |
| `Live` | `Long` | `8.24` | 148,830.00 USD | 0.00 USD | 1,300.00 USD | `-6.84%` | `158.06` |
| `Live` | `Long` | `8.26` | 147,530.00 USD | 0.00 USD | 13,810.00 USD | `-6.73%` | `1,673.14` |
| `Live` | `Long` | `8.28` | 133,710.00 USD | 0.00 USD | 9,740.00 USD | `-6.51%` | `1,176.86` |
| `Live` | `Long` | `8.29` | 123,980.00 USD | 0.00 USD | 498.26 USD | `-6.39%` | `60.14` |
| `Live` | `Long` | `8.29` | 123,480.00 USD | 0.00 USD | 18,970.00 USD | `-6.28%` | `2,286.62` |
| `Live` | `Long` | `8.30` | 104,510.00 USD | 0.00 USD | 33,500.00 USD | `-6.17%` | `4,033.57` |
| `Live` | `Long` | `8.31` | 71,010.00 USD | 0.00 USD | 4,550.00 USD | `-6.05%` | `547.70` |
| `Live` | `Long` | `8.34` | 66,460.00 USD | 0.00 USD | 4,760.00 USD | `-5.83%` | `571.65` |
| `Live` | `Long` | `8.36` | 61,690.00 USD | 0.00 USD | 3,180.00 USD | `-5.60%` | `380.92` |
| `Live` | `Long` | `8.37` | 58,510.00 USD | 0.00 USD | 7,390.00 USD | `-5.49%` | `883.19` |
| `Live` | `Long` | `8.38` | 51,120.00 USD | 0.00 USD | 4,620.00 USD | `-5.26%` | `550.46` |
| `Live` | `Long` | `8.39` | 46,510.00 USD | 0.00 USD | 1,680.00 USD | `-5.15%` | `200.00` |
| `Live` | `Long` | `8.40` | 44,830.00 USD | 0.00 USD | 1,380.00 USD | `-5.04%` | `164.50` |
| `Live` | `Long` | `8.41` | 43,440.00 USD | 0.00 USD | 681.03 USD | `-4.92%` | `80.93` |
| `Live` | `Long` | `8.44` | 42,760.00 USD | 0.00 USD | 188.61 USD | `-4.70%` | `22.36` |
| `Live` | `Long` | `8.45` | 42,570.00 USD | 0.00 USD | 588.70 USD | `-4.58%` | `69.71` |
| `Live` | `Long` | `8.46` | 41,990.00 USD | 0.00 USD | 422.16 USD | `-4.47%` | `49.93` |
| `Live` | `Long` | `8.46` | 41,560.00 USD | 0.00 USD | 1,860.00 USD | `-4.36%` | `220.00` |
| `Live` | `Long` | `8.47` | 39,700.00 USD | 0.00 USD | 12,430.00 USD | `-4.25%` | `1,466.22` |
| `Live` | `Long` | `8.48` | 27,280.00 USD | 0.00 USD | 1,160.00 USD | `-4.13%` | `136.39` |
| `Live` | `Long` | `8.49` | 26,120.00 USD | 0.00 USD | 403.51 USD | `-4.02%` | `47.50` |
| `Live` | `Long` | `8.51` | 25,710.00 USD | 0.00 USD | 6,380.00 USD | `-3.91%` | `750.34` |
| `Live` | `Long` | `8.52` | 19,330.00 USD | 0.00 USD | 7,770.00 USD | `-3.79%` | `912.98` |
| `Live` | `Long` | `8.54` | 11,560.00 USD | 0.00 USD | 6,350.00 USD | `-3.57%` | `743.78` |
| `Live` | `Long` | `8.54` | 5,210.00 USD | 0.00 USD | 1,550.00 USD | `-3.46%` | `180.95` |
| `Live` | `Long` | `8.55` | 3,660.00 USD | 0.00 USD | 684.40 USD | `-3.34%` | `80.00` |
| `Live` | `Long` | `8.61` | 2,980.00 USD | 0.00 USD | 2,980.00 USD | `-2.78%` | `346.30` |
| `Live` | `Short` | `9.13` | 314.34 USD | 314.34 USD | 0.00 USD | `+3.21%` | `34.41` |
| `Live` | `Short` | `9.21` | 4,130.00 USD | 3,810.00 USD | 0.00 USD | `+4.11%` | `413.79` |
| `Live` | `Short` | `9.29` | 4,230.00 USD | 100.93 USD | 0.00 USD | `+4.91%` | `10.87` |
| `Live` | `Short` | `9.35` | 8,150.00 USD | 3,930.00 USD | 0.00 USD | `+5.58%` | `420.07` |
| `Live` | `Short` | `9.38` | 412,270.00 USD | 404,120.00 USD | 0.00 USD | `+6.04%` | `43,059.94` |
| `Live` | `Short` | `9.41` | 414,740.00 USD | 2,470.00 USD | 0.00 USD | `+6.37%` | `262.71` |
| `Live` | `Short` | `9.49` | 415,170.00 USD | 428.79 USD | 0.00 USD | `+7.28%` | `45.16` |
| `Live` | `Short` | `9.73` | 415,370.00 USD | 192.95 USD | 0.00 USD | `+9.99%` | `19.82` |
| `Live` | `Short` | `9.76` | 415,920.00 USD | 549.11 USD | 0.00 USD | `+10.22%` | `56.29` |
| `Live` | `Short` | `9.78` | 416,390.00 USD | 470.18 USD | 0.00 USD | `+10.44%` | `48.10` |
| `Live` | `Short` | `10.09` | 416,500.00 USD | 113.76 USD | 0.00 USD | `+13.94%` | `11.28` |
| `Live` | `Short` | `10.15` | 423,390.00 USD | 6,890.00 USD | 0.00 USD | `+14.74%` | `678.64` |
| `Live` | `Short` | `10.21` | 430,720.00 USD | 7,330.00 USD | 0.00 USD | `+15.41%` | `717.30` |
| `Live` | `Short` | `10.23` | 430,830.00 USD | 114.12 USD | 0.00 USD | `+15.64%` | `11.15` |
| `Live` | `Short` | `10.35` | 434,210.00 USD | 3,380.00 USD | 0.00 USD | `+16.88%` | `326.92` |
| `Live` | `Short` | `10.56` | 434,740.00 USD | 523.81 USD | 0.00 USD | `+19.37%` | `49.58` |
| `Live` | `Short` | `10.71` | 434,960.00 USD | 218.91 USD | 0.00 USD | `+21.06%` | `20.43` |
| `Live` | `Short` | `10.74` | 472,160.00 USD | 37,210.00 USD | 0.00 USD | `+21.40%` | `3,462.73` |
| `Live` | `Short` | `10.96` | 474,080.00 USD | 1,920.00 USD | 0.00 USD | `+23.89%` | `174.67` |
| `Live` | `Short` | `11.01` | 481,050.00 USD | 6,970.00 USD | 0.00 USD | `+24.34%` | `633.00` |
| `Live` | `Short` | `11.27` | 492,850.00 USD | 11,810.00 USD | 0.00 USD | `+27.28%` | `1,048.25` |
| `Live` | `Short` | `11.62` | 504,990.00 USD | 12,140.00 USD | 0.00 USD | `+31.34%` | `1,043.90` |
| `Live` | `Short` | `11.65` | 505,770.00 USD | 776.22 USD | 0.00 USD | `+31.68%` | `66.60` |
| `Live` | `Short` | `11.78` | 564,640.00 USD | 58,870.00 USD | 0.00 USD | `+33.04%` | `5,000.00` |
| `Live` | `Short` | `11.96` | 566,000.00 USD | 1,360.00 USD | 0.00 USD | `+35.19%` | `113.77` |
| `Live` | `Short` | `12.12` | 566,620.00 USD | 620.17 USD | 0.00 USD | `+36.88%` | `51.19` |
| `Live` | `Short` | `12.30` | 568,350.00 USD | 1,730.00 USD | 0.00 USD | `+39.03%` | `140.71` |
| `Live` | `Short` | `12.40` | 568,700.00 USD | 343.62 USD | 0.00 USD | `+40.16%` | `27.70` |
| `Live` | `Short` | `12.63` | 569,130.00 USD | 430.85 USD | 0.00 USD | `+42.76%` | `34.10` |
| `Live` | `Short` | `12.79` | 570,080.00 USD | 953.38 USD | 0.00 USD | `+44.45%` | `74.57` |
| `Live` | `Short` | `12.79` | 606,930.00 USD | 36,850.00 USD | 0.00 USD | `+44.56%` | `2,879.71` |
| `Live` | `Short` | `12.95` | 621,430.00 USD | 14,500.00 USD | 0.00 USD | `+46.26%` | `1,120.14` |
| `Live` | `Short` | `12.96` | 621,530.00 USD | 102.68 USD | 0.00 USD | `+46.48%` | `7.92` |
| `Live` | `Short` | `13.20` | 709,470.00 USD | 87,940.00 USD | 0.00 USD | `+49.08%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 944,310.00 USD | 234,840.00 USD | 0.00 USD | `+50.10%` | `17,677.02` |
| `Live` | `Short` | `13.29` | 948,120.00 USD | 3,810.00 USD | 0.00 USD | `+50.21%` | `286.56` |
| `Live` | `Short` | `13.46` | 948,550.00 USD | 430.34 USD | 0.00 USD | `+52.13%` | `31.96` |
| `Live` | `Short` | `13.69` | 948,730.00 USD | 172.29 USD | 0.00 USD | `+54.62%` | `12.59` |
| `Live` | `Short` | `13.73` | 948,890.00 USD | 160.01 USD | 0.00 USD | `+55.18%` | `11.65` |
| `Live` | `Short` | `14.10` | 952,800.00 USD | 3,910.00 USD | 0.00 USD | `+59.25%` | `277.54` |
| `Live` | `Short` | `14.66` | 953,620.00 USD | 823.29 USD | 0.00 USD | `+65.69%` | `56.14` |
| `Live` | `Short` | `14.71` | 953,860.00 USD | 241.31 USD | 0.00 USD | `+66.14%` | `16.41` |
| `Live` | `Short` | `14.81` | 954,160.00 USD | 292.30 USD | 0.00 USD | `+67.39%` | `19.73` |
| `Live` | `Short` | `14.84` | 956,620.00 USD | 2,460.00 USD | 0.00 USD | `+67.61%` | `166.16` |
| `Live` | `Short` | `14.86` | 956,940.00 USD | 320.13 USD | 0.00 USD | `+67.84%` | `21.55` |
| `Live` | `Short` | `15.29` | 957,170.00 USD | 229.43 USD | 0.00 USD | `+72.81%` | `15.00` |
| `Live` | `Short` | `15.35` | 957,400.00 USD | 230.17 USD | 0.00 USD | `+73.37%` | `15.00` |
| `Live` | `Short` | `15.38` | 977,400.00 USD | 20,000.00 USD | 0.00 USD | `+73.83%` | `1,300.00` |
| `Live` | `Short` | `15.45` | 1,130,000.00 USD | 154,450.00 USD | 0.00 USD | `+74.50%` | `10,000.00` |
| `Live` | `Short` | `15.70` | 1,130,000.00 USD | 111.59 USD | 0.00 USD | `+77.33%` | `7.11` |
| `Live` | `Short` | `16.29` | 1,400,000.00 USD | 263,950.00 USD | 0.00 USD | `+83.99%` | `16,208.00` |
| `Live` | `Short` | `16.48` | 1,420,000.00 USD | 22,650.00 USD | 0.00 USD | `+86.25%` | `1,373.91` |
| `Live` | `Short` | `16.52` | 1,420,000.00 USD | 190.91 USD | 0.00 USD | `+86.59%` | `11.56` |
| `Live` | `Short` | `16.70` | 1,500,000.00 USD | 84,150.00 USD | 0.00 USD | `+88.74%` | `5,037.66` |
| `Live` | `Short` | `16.75` | 1,500,000.00 USD | 162.26 USD | 0.00 USD | `+89.19%` | `9.69` |
| `Live` | `Short` | `16.77` | 1,500,000.00 USD | 340.87 USD | 0.00 USD | `+89.53%` | `20.32` |
| `Live` | `Short` | `17.02` | 1,500,000.00 USD | 191.87 USD | 0.00 USD | `+92.36%` | `11.27` |
| `Live` | `Short` | `17.14` | 1,510,000.00 USD | 1,710.00 USD | 0.00 USD | `+93.60%` | `100.00` |
| `Live` | `Short` | `17.46` | 1,510,000.00 USD | 101.47 USD | 0.00 USD | `+97.33%` | `5.81` |
| `Live` | `Short` | `17.62` | 1,510,000.00 USD | 4,120.00 USD | 0.00 USD | `+99.13%` | `233.67` |
| `Live` | `Short` | `17.64` | 1,510,000.00 USD | 4,930.00 USD | 0.00 USD | `+99.36%` | `279.46` |
| `Live` | `Short` | `17.66` | 1,520,000.00 USD | 2,660.00 USD | 0.00 USD | `+99.59%` | `150.82` |
| `Live` | `Short` | `17.70` | 1,520,000.00 USD | 108.89 USD | 0.00 USD | `+100.04%` | `6.15` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 327,240.00 USD | 0.00 USD | 611.73 USD | `-73.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 326,630.00 USD | 0.00 USD | 793.75 USD | `-54.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 325,840.00 USD | 0.00 USD | 105.04 USD | `-49.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 325,730.00 USD | 0.00 USD | 67,970.00 USD | `-43.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 257,760.00 USD | 0.00 USD | 205.30 USD | `-40.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 257,560.00 USD | 0.00 USD | 465.42 USD | `-38.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 257,090.00 USD | 0.00 USD | 349.35 USD | `-37.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 256,740.00 USD | 0.00 USD | 1,330.00 USD | `-34.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 255,420.00 USD | 0.00 USD | 493.50 USD | `-32.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 254,920.00 USD | 0.00 USD | 100.98 USD | `-32.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 254,820.00 USD | 0.00 USD | 620.80 USD | `-32.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 254,200.00 USD | 0.00 USD | 4,160.00 USD | `-31.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 250,050.00 USD | 0.00 USD | 6,500.00 USD | `-30.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 243,540.00 USD | 0.00 USD | 864.38 USD | `-28.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 242,680.00 USD | 0.00 USD | 1,430.00 USD | `-26.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 241,250.00 USD | 0.00 USD | 4,340.00 USD | `-26.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 236,910.00 USD | 0.00 USD | 5,520.00 USD | `-24.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 231,380.00 USD | 0.00 USD | 100.72 USD | `-24.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 231,280.00 USD | 0.00 USD | 296.34 USD | `-23.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 230,990.00 USD | 0.00 USD | 921.19 USD | `-23.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 230,070.00 USD | 0.00 USD | 709.98 USD | `-22.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 229,360.00 USD | 0.00 USD | 262.44 USD | `-21.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 229,090.00 USD | 0.00 USD | 3,610.00 USD | `-20.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 225,480.00 USD | 0.00 USD | 6,790.00 USD | `-19.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 218,690.00 USD | 0.00 USD | 9,770.00 USD | `-18.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 208,920.00 USD | 0.00 USD | 103.46 USD | `-18.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 208,820.00 USD | 0.00 USD | 603.44 USD | `-18.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 208,220.00 USD | 0.00 USD | 891.57 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 207,320.00 USD | 0.00 USD | 2,300.00 USD | `-17.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 205,020.00 USD | 0.00 USD | 129.58 USD | `-17.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 204,890.00 USD | 0.00 USD | 236.19 USD | `-17.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 204,650.00 USD | 0.00 USD | 199.39 USD | `-15.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 204,460.00 USD | 0.00 USD | 4,730.00 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 199,720.00 USD | 0.00 USD | 37,420.00 USD | `-15.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 162,300.00 USD | 0.00 USD | 778.49 USD | `-15.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 161,520.00 USD | 0.00 USD | 799.83 USD | `-14.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 160,720.00 USD | 0.00 USD | 103.41 USD | `-14.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 160,620.00 USD | 0.00 USD | 1,370.00 USD | `-14.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 159,240.00 USD | 0.00 USD | 360.13 USD | `-12.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 158,880.00 USD | 0.00 USD | 578.04 USD | `-12.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 158,300.00 USD | 0.00 USD | 175.42 USD | `-12.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 158,130.00 USD | 0.00 USD | 2,990.00 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 155,130.00 USD | 0.00 USD | 143.51 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 154,990.00 USD | 0.00 USD | 183.33 USD | `-11.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.88` | 154,810.00 USD | 0.00 USD | 194.52 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 154,610.00 USD | 0.00 USD | 394.75 USD | `-10.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 154,220.00 USD | 0.00 USD | 1,350.00 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 152,870.00 USD | 0.00 USD | 1,590.00 USD | `-10.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 151,290.00 USD | 0.00 USD | 898.42 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 150,390.00 USD | 0.00 USD | 1,350.00 USD | `-9.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 149,040.00 USD | 0.00 USD | 7,400.00 USD | `-9.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 141,640.00 USD | 0.00 USD | 123.58 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 141,520.00 USD | 0.00 USD | 2,110.00 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 139,410.00 USD | 0.00 USD | 563.85 USD | `-8.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 138,850.00 USD | 0.00 USD | 105.14 USD | `-8.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 138,740.00 USD | 0.00 USD | 367.76 USD | `-8.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 138,370.00 USD | 0.00 USD | 2,330.00 USD | `-8.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 136,040.00 USD | 0.00 USD | 184.13 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 135,860.00 USD | 0.00 USD | 6,920.00 USD | `-8.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 128,940.00 USD | 0.00 USD | 462.15 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 128,480.00 USD | 0.00 USD | 654.53 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 127,820.00 USD | 0.00 USD | 367.91 USD | `-7.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 127,450.00 USD | 0.00 USD | 520.75 USD | `-7.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 126,930.00 USD | 0.00 USD | 2,900.00 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 124,030.00 USD | 0.00 USD | 141.04 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 123,890.00 USD | 0.00 USD | 1,780.00 USD | `-7.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 122,100.00 USD | 0.00 USD | 515.66 USD | `-7.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 121,590.00 USD | 0.00 USD | 143.54 USD | `-6.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 121,450.00 USD | 0.00 USD | 168.64 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 121,280.00 USD | 0.00 USD | 201.49 USD | `-6.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 121,080.00 USD | 0.00 USD | 6,530.00 USD | `-6.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 114,550.00 USD | 0.00 USD | 1,140.00 USD | `-6.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 113,400.00 USD | 0.00 USD | 2,000.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 111,400.00 USD | 0.00 USD | 756.06 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 110,640.00 USD | 0.00 USD | 970.35 USD | `-5.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 109,670.00 USD | 0.00 USD | 5,470.00 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 104,210.00 USD | 0.00 USD | 1,970.00 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 102,240.00 USD | 0.00 USD | 3,290.00 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 98,960.00 USD | 0.00 USD | 358.56 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 98,600.00 USD | 0.00 USD | 1,880.00 USD | `-4.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 96,710.00 USD | 0.00 USD | 140.36 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 96,570.00 USD | 0.00 USD | 138.24 USD | `-4.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 96,440.00 USD | 0.00 USD | 954.23 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 95,480.00 USD | 0.00 USD | 769.61 USD | `-4.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.48` | 94,710.00 USD | 0.00 USD | 489.58 USD | `-4.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.51` | 94,220.00 USD | 0.00 USD | 1,440.00 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.52` | 92,780.00 USD | 0.00 USD | 198.74 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.53` | 92,580.00 USD | 0.00 USD | 1,130.00 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 91,450.00 USD | 0.00 USD | 4,400.00 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 87,050.00 USD | 0.00 USD | 243.82 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.57` | 86,800.00 USD | 0.00 USD | 428.58 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.59` | 86,370.00 USD | 0.00 USD | 2,500.00 USD | `-3.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.60` | 83,870.00 USD | 0.00 USD | 435.59 USD | `-2.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.61` | 83,440.00 USD | 0.00 USD | 1,080.00 USD | `-2.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 82,360.00 USD | 0.00 USD | 1,980.00 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 80,380.00 USD | 0.00 USD | 2,740.00 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.63` | 77,640.00 USD | 0.00 USD | 103.19 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.64` | 77,540.00 USD | 0.00 USD | 103.31 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 77,430.00 USD | 0.00 USD | 1,900.00 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.66` | 75,530.00 USD | 0.00 USD | 196.87 USD | `-2.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.68` | 75,330.00 USD | 0.00 USD | 223.82 USD | `-1.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.69` | 75,110.00 USD | 0.00 USD | 990.09 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.70` | 74,120.00 USD | 0.00 USD | 5,010.00 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 69,110.00 USD | 0.00 USD | 6,880.00 USD | `-1.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 62,220.00 USD | 0.00 USD | 134.30 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.72` | 62,090.00 USD | 0.00 USD | 390.88 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.73` | 61,700.00 USD | 0.00 USD | 1,390.00 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.74` | 60,310.00 USD | 0.00 USD | 933.70 USD | `-1.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.76` | 59,370.00 USD | 0.00 USD | 6,300.00 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.77` | 53,080.00 USD | 0.00 USD | 39,810.00 USD | `-0.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.78` | 13,270.00 USD | 0.00 USD | 114.25 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 13,150.00 USD | 0.00 USD | 1,930.00 USD | `-0.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 11,220.00 USD | 0.00 USD | 711.78 USD | `-0.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.80` | 10,510.00 USD | 0.00 USD | 1,760.00 USD | `-0.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.81` | 8,750.00 USD | 0.00 USD | 705.20 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.82` | 8,040.00 USD | 0.00 USD | 2,030.00 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.84` | 6,010.00 USD | 0.00 USD | 243.40 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 5,760.00 USD | 0.00 USD | 5,760.00 USD | `-0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 192.86 USD | 192.86 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 807.74 USD | 614.88 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 6,830.00 USD | 6,020.00 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 7,930.00 USD | 1,100.00 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 8,120.00 USD | 188.66 USD | 0.00 USD | `+0.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 8,910.00 USD | 788.72 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 12,270.00 USD | 3,360.00 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 12,380.00 USD | 110.58 USD | 0.00 USD | `+0.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 13,400.00 USD | 1,020.00 USD | 0.00 USD | `+0.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 13,620.00 USD | 223.62 USD | 0.00 USD | `+1.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 13,760.00 USD | 137.73 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 14,160.00 USD | 401.63 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 329,310.00 USD | 315,150.00 USD | 0.00 USD | `+1.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 329,420.00 USD | 104.59 USD | 0.00 USD | `+1.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 330,200.00 USD | 776.54 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 330,730.00 USD | 531.20 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 332,100.00 USD | 1,380.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 333,190.00 USD | 1,090.00 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 333,810.00 USD | 616.37 USD | 0.00 USD | `+2.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 333,910.00 USD | 102.03 USD | 0.00 USD | `+2.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 334,360.00 USD | 453.84 USD | 0.00 USD | `+2.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 334,520.00 USD | 160.99 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 334,940.00 USD | 415.00 USD | 0.00 USD | `+2.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 336,450.00 USD | 1,510.00 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 338,490.00 USD | 2,040.00 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 566,120.00 USD | 227,630.00 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 569,160.00 USD | 3,030.00 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 571,160.00 USD | 2,000.00 USD | 0.00 USD | `+3.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 965,370.00 USD | 394,210.00 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,000,000.00 USD | 39,240.00 USD | 0.00 USD | `+3.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.20` | 1,010,000.00 USD | 1,590.00 USD | 0.00 USD | `+3.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,010,000.00 USD | 3,320.00 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,010,000.00 USD | 131.87 USD | 0.00 USD | `+4.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,010,000.00 USD | 687.91 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,010,000.00 USD | 954.71 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,410,000.00 USD | 398,520.00 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.27` | 1,410,000.00 USD | 205.87 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,410,000.00 USD | 1,960.00 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,410,000.00 USD | 434.45 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,430,000.00 USD | 18,610.00 USD | 0.00 USD | `+5.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,430,000.00 USD | 354.81 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,430,000.00 USD | 2,180.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,430,000.00 USD | 579.86 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,760,000.00 USD | 327,430.00 USD | 0.00 USD | `+5.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,760,000.00 USD | 233.38 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,760,000.00 USD | 163.41 USD | 0.00 USD | `+5.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,760,000.00 USD | 1,150.00 USD | 0.00 USD | `+6.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,760,000.00 USD | 660.84 USD | 0.00 USD | `+6.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,760,000.00 USD | 833.66 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,770,000.00 USD | 1,010.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,770,000.00 USD | 102.45 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,770,000.00 USD | 219.84 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,770,000.00 USD | 140.35 USD | 0.00 USD | `+6.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,770,000.00 USD | 1,890.00 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.47` | 1,770,000.00 USD | 1,780.00 USD | 0.00 USD | `+7.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,770,000.00 USD | 2,210.00 USD | 0.00 USD | `+7.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,770,000.00 USD | 288.46 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.51` | 1,770,000.00 USD | 1,600.00 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,770,000.00 USD | 103.54 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.56` | 1,770,000.00 USD | 535.35 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,770,000.00 USD | 231.00 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,770,000.00 USD | 221.07 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,780,000.00 USD | 1,470.00 USD | 0.00 USD | `+8.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,780,000.00 USD | 148.48 USD | 0.00 USD | `+8.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,780,000.00 USD | 329.43 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,780,000.00 USD | 446.58 USD | 0.00 USD | `+9.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,780,000.00 USD | 108.21 USD | 0.00 USD | `+9.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,780,000.00 USD | 169.68 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,780,000.00 USD | 121.87 USD | 0.00 USD | `+10.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.80` | 1,780,000.00 USD | 619.28 USD | 0.00 USD | `+10.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,780,000.00 USD | 5,030.00 USD | 0.00 USD | `+11.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,780,000.00 USD | 340.05 USD | 0.00 USD | `+11.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,780,000.00 USD | 742.12 USD | 0.00 USD | `+11.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,790,000.00 USD | 899.47 USD | 0.00 USD | `+11.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,860,000.00 USD | 70,020.00 USD | 0.00 USD | `+12.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,860,000.00 USD | 373.97 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,860,000.00 USD | 7,500.00 USD | 0.00 USD | `+13.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,870,000.00 USD | 6,370.00 USD | 0.00 USD | `+13.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,870,000.00 USD | 202.10 USD | 0.00 USD | `+14.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,080,000.00 USD | 210,980.00 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,080,000.00 USD | 1,150.00 USD | 0.00 USD | `+14.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 2,080,000.00 USD | 172.16 USD | 0.00 USD | `+15.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 2,080,000.00 USD | 868.36 USD | 0.00 USD | `+16.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 2,080,000.00 USD | 489.40 USD | 0.00 USD | `+16.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 2,080,000.00 USD | 1,200.00 USD | 0.00 USD | `+17.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 2,080,000.00 USD | 118.01 USD | 0.00 USD | `+17.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 2,090,000.00 USD | 312.31 USD | 0.00 USD | `+18.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 2,090,000.00 USD | 2,290.00 USD | 0.00 USD | `+18.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 2,090,000.00 USD | 178.46 USD | 0.00 USD | `+19.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.62` | 2,090,000.00 USD | 153.11 USD | 0.00 USD | `+20.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 2,090,000.00 USD | 173.42 USD | 0.00 USD | `+21.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 2,090,000.00 USD | 184.75 USD | 0.00 USD | `+21.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 2,090,000.00 USD | 135.78 USD | 0.00 USD | `+21.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 2,090,000.00 USD | 127.96 USD | 0.00 USD | `+22.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 2,090,000.00 USD | 476.43 USD | 0.00 USD | `+22.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 2,090,000.00 USD | 1,730.00 USD | 0.00 USD | `+23.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 2,090,000.00 USD | 118.97 USD | 0.00 USD | `+23.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 2,090,000.00 USD | 251.06 USD | 0.00 USD | `+23.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 2,090,000.00 USD | 552.44 USD | 0.00 USD | `+23.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 2,090,000.00 USD | 1,750.00 USD | 0.00 USD | `+24.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 2,090,000.00 USD | 320.29 USD | 0.00 USD | `+25.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 2,090,000.00 USD | 1,100.00 USD | 0.00 USD | `+26.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 2,100,000.00 USD | 2,610.00 USD | 0.00 USD | `+26.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 2,100,000.00 USD | 1,270.00 USD | 0.00 USD | `+27.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 2,100,000.00 USD | 1,380.00 USD | 0.00 USD | `+28.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 2,100,000.00 USD | 2,410.00 USD | 0.00 USD | `+28.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 2,110,000.00 USD | 9,520.00 USD | 0.00 USD | `+29.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 2,120,000.00 USD | 3,530.00 USD | 0.00 USD | `+29.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 2,120,000.00 USD | 7,700.00 USD | 0.00 USD | `+31.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 2,120,000.00 USD | 1,130.00 USD | 0.00 USD | `+33.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 2,120,000.00 USD | 434.61 USD | 0.00 USD | `+34.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 2,120,000.00 USD | 163.52 USD | 0.00 USD | `+34.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 2,250,000.00 USD | 124,300.00 USD | 0.00 USD | `+35.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.51` | 2,250,000.00 USD | 2,770.00 USD | 0.00 USD | `+41.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 2,260,000.00 USD | 3,350.00 USD | 0.00 USD | `+43.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 2,260,000.00 USD | 197.97 USD | 0.00 USD | `+44.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 2,260,000.00 USD | 3,200.00 USD | 0.00 USD | `+45.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 2,260,000.00 USD | 179.58 USD | 0.00 USD | `+46.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 2,260,000.00 USD | 720.74 USD | 0.00 USD | `+46.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.07` | 2,260,000.00 USD | 504.17 USD | 0.00 USD | `+47.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 2,260,000.00 USD | 169.57 USD | 0.00 USD | `+48.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.30` | 2,260,000.00 USD | 159.66 USD | 0.00 USD | `+50.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 2,260,000.00 USD | 446.52 USD | 0.00 USD | `+51.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.46` | 2,260,000.00 USD | 1,710.00 USD | 0.00 USD | `+52.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 2,270,000.00 USD | 5,320.00 USD | 0.00 USD | `+52.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,480,000.00 USD | 207,980.00 USD | 0.00 USD | `+52.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,480,000.00 USD | 407.95 USD | 0.00 USD | `+54.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,480,000.00 USD | 174.91 USD | 0.00 USD | `+55.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,490,000.00 USD | 9,230.00 USD | 0.00 USD | `+58.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,490,000.00 USD | 960.26 USD | 0.00 USD | `+60.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,490,000.00 USD | 2,710.00 USD | 0.00 USD | `+62.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,490,000.00 USD | 805.90 USD | 0.00 USD | `+63.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,490,000.00 USD | 655.55 USD | 0.00 USD | `+66.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,500,000.00 USD | 4,890.00 USD | 0.00 USD | `+67.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,500,000.00 USD | 471.09 USD | 0.00 USD | `+68.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,500,000.00 USD | 383.85 USD | 0.00 USD | `+69.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 3,150,000.00 USD | 652,070.00 USD | 0.00 USD | `+69.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 3,150,000.00 USD | 111.87 USD | 0.00 USD | `+79.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 3,150,000.00 USD | 219.91 USD | 0.00 USD | `+80.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 3,150,000.00 USD | 121.74 USD | 0.00 USD | `+91.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.00` | 3,150,000.00 USD | 297.59 USD | 0.00 USD | `+92.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.18` | 3,150,000.00 USD | 4,500.00 USD | 0.00 USD | `+94.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.20` | 3,270,000.00 USD | 120,270.00 USD | 0.00 USD | `+94.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.34` | 3,270,000.00 USD | 122.39 USD | 0.00 USD | `+95.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.50` | 3,270,000.00 USD | 586.59 USD | 0.00 USD | `+97.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.61` | 3,280,000.00 USD | 580.97 USD | 0.00 USD | `+98.91%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `7.46` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 723.17 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.46` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 723.17 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.52` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 9,830.00 USD | 3,080.00 USD | 0.00 USD |
| `7D` | `7.52` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 9,830.00 USD | 3,080.00 USD | 0.00 USD |
| `1D` | `7.60` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 74.23 USD |
| `7D` | `7.60` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 74.23 USD |
| `1D` | `7.62` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 5,440.00 USD |
| `7D` | `7.62` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 5,440.00 USD |
| `1D` | `7.64` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 986.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.64` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 986.95 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.70` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 321.75 USD | 2,390.00 USD | 4,010.00 USD |
| `7D` | `7.70` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 321.75 USD | 2,390.00 USD | 4,010.00 USD |
| `1D` | `7.72` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 4,160.00 USD | 1,630.00 USD | 12,390.00 USD |
| `7D` | `7.72` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 4,160.00 USD | 1,630.00 USD | 12,390.00 USD |
| `1D` | `7.74` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 2,950.00 USD | 4,580.00 USD | 2,430.00 USD |
| `7D` | `7.74` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 2,950.00 USD | 4,580.00 USD | 2,430.00 USD |
| `1D` | `7.76` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 1,510.00 USD | 1,100.00 USD | 5,380.00 USD |
| `7D` | `7.76` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 1,510.00 USD | 1,100.00 USD | 5,380.00 USD |
| `1D` | `7.78` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 40,980.00 USD | 3,730.00 USD | 8,950.00 USD |
| `7D` | `7.78` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 42,650.00 USD | 3,730.00 USD | 8,950.00 USD |
| `1D` | `7.80` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 38,450.00 USD | 10,860.00 USD | 8,320.00 USD |
| `7D` | `7.80` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 38,450.00 USD | 10,860.00 USD | 8,320.00 USD |
| `1D` | `7.82` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 5,100.00 USD | 7,610.00 USD | 5,600.00 USD |
| `7D` | `7.82` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 5,100.00 USD | 7,610.00 USD | 5,600.00 USD |
| `1D` | `7.84` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 671.45 USD | 4,910.00 USD | 12,620.00 USD |
| `7D` | `7.84` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 671.45 USD | 4,910.00 USD | 12,620.00 USD |
| `1D` | `7.86` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 14,500.00 USD | 1,680.00 USD | 16,260.00 USD |
| `7D` | `7.86` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 14,500.00 USD | 1,680.00 USD | 16,260.00 USD |
| `1D` | `7.88` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 43,790.00 USD | 9,570.00 USD | 22,590.00 USD |
| `7D` | `7.88` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 43,790.00 USD | 9,570.00 USD | 22,590.00 USD |
| `1D` | `7.90` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 14,150.00 USD | 7,630.00 USD | 7,480.00 USD |
| `7D` | `7.90` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 14,150.00 USD | 7,630.00 USD | 7,480.00 USD |
| `1D` | `7.92` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 17,630.00 USD | 2,950.00 USD | 6,190.00 USD |
| `7D` | `7.92` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 19,860.00 USD | 2,950.00 USD | 6,190.00 USD |
| `1D` | `7.94` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 19,500.00 USD | 6,860.00 USD | 3,370.00 USD |
| `7D` | `7.94` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 19,500.00 USD | 6,860.00 USD | 3,370.00 USD |
| `1D` | `7.96` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 2,830.00 USD | 8,870.00 USD | 5,230.00 USD |
| `7D` | `7.96` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 2,830.00 USD | 8,870.00 USD | 5,230.00 USD |
| `1D` | `7.98` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 14,350.00 USD | 3,300.00 USD | 8,480.00 USD |
| `7D` | `7.98` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 14,350.00 USD | 3,300.00 USD | 8,480.00 USD |
| `1D` | `8.00` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 570.55 USD | 1,840.00 USD | 1,790.00 USD |
| `7D` | `8.00` | 997,370.00 USD | 0.00 USD | 997,370.00 USD | 570.55 USD | 1,840.00 USD | 1,790.00 USD |
| `1D` | `8.02` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 40,190.00 USD | 8,470.00 USD | 157.85 USD |
| `7D` | `8.02` | 993,160.00 USD | 0.00 USD | 993,160.00 USD | 40,190.00 USD | 8,470.00 USD | 157.85 USD |
| `1D` | `8.04` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 19,460.00 USD | 1,540.00 USD | 6,480.00 USD |
| `7D` | `8.04` | 944,340.00 USD | 0.00 USD | 944,340.00 USD | 19,460.00 USD | 1,540.00 USD | 6,480.00 USD |
| `1D` | `8.06` | 977,000.00 USD | 0.00 USD | 977,000.00 USD | 27,730.00 USD | 5,470.00 USD | 6,210.00 USD |
| `7D` | `8.06` | 916,850.00 USD | 0.00 USD | 916,850.00 USD | 27,730.00 USD | 5,470.00 USD | 6,210.00 USD |
| `1D` | `8.08` | 937,600.00 USD | 0.00 USD | 937,600.00 USD | 5,270.00 USD | 3,810.00 USD | 4,750.00 USD |
| `7D` | `8.08` | 877,450.00 USD | 0.00 USD | 877,450.00 USD | 5,270.00 USD | 3,810.00 USD | 4,750.00 USD |
| `1D` | `8.10` | 923,770.00 USD | 0.00 USD | 923,770.00 USD | 32,980.00 USD | 3,950.00 USD | 7,840.00 USD |
| `7D` | `8.10` | 863,620.00 USD | 0.00 USD | 863,620.00 USD | 32,980.00 USD | 3,950.00 USD | 7,840.00 USD |
| `1D` | `8.12` | 879,000.00 USD | 0.00 USD | 879,000.00 USD | 12,010.00 USD | 4,240.00 USD | 22,190.00 USD |
| `7D` | `8.12` | 818,850.00 USD | 0.00 USD | 818,850.00 USD | 12,010.00 USD | 4,240.00 USD | 22,190.00 USD |
| `1D` | `8.14` | 840,560.00 USD | 0.00 USD | 840,560.00 USD | 20,690.00 USD | 0.00 USD | 42.96 USD |
| `7D` | `8.14` | 780,410.00 USD | 0.00 USD | 780,410.00 USD | 20,690.00 USD | 0.00 USD | 42.96 USD |
| `1D` | `8.16` | 819,830.00 USD | 0.00 USD | 819,830.00 USD | 11,720.00 USD | 662.47 USD | 9,020.00 USD |
| `7D` | `8.16` | 759,680.00 USD | 0.00 USD | 759,680.00 USD | 11,720.00 USD | 662.47 USD | 9,020.00 USD |
| `1D` | `8.18` | 798,430.00 USD | 0.00 USD | 798,430.00 USD | 53,280.00 USD | 15,390.00 USD | 478.53 USD |
| `7D` | `8.18` | 738,280.00 USD | 0.00 USD | 738,280.00 USD | 53,280.00 USD | 15,390.00 USD | 478.53 USD |
| `1D` | `8.20` | 729,280.00 USD | 0.00 USD | 729,280.00 USD | 7,430.00 USD | 0.00 USD | 448.46 USD |
| `7D` | `8.20` | 669,130.00 USD | 0.00 USD | 669,130.00 USD | 7,430.00 USD | 0.00 USD | 448.46 USD |
| `1D` | `8.22` | 721,400.00 USD | 0.00 USD | 721,400.00 USD | 7,650.00 USD | 5,990.00 USD | 10,040.00 USD |
| `7D` | `8.22` | 661,250.00 USD | 0.00 USD | 661,250.00 USD | 7,650.00 USD | 5,990.00 USD | 10,040.00 USD |
| `1D` | `8.24` | 697,710.00 USD | 0.00 USD | 697,710.00 USD | 31,250.00 USD | 5,230.00 USD | 34,520.00 USD |
| `7D` | `8.24` | 637,560.00 USD | 0.00 USD | 637,560.00 USD | 31,250.00 USD | 5,230.00 USD | 34,520.00 USD |
| `1D` | `8.26` | 626,710.00 USD | 0.00 USD | 626,710.00 USD | 15,150.00 USD | 11,460.00 USD | 6,100.00 USD |
| `7D` | `8.26` | 566,570.00 USD | 0.00 USD | 566,570.00 USD | 15,150.00 USD | 11,460.00 USD | 6,100.00 USD |
| `1D` | `8.28` | 594,000.00 USD | 0.00 USD | 594,000.00 USD | 137,750.00 USD | 9,830.00 USD | 79,900.00 USD |
| `7D` | `8.28` | 533,850.00 USD | 0.00 USD | 533,850.00 USD | 137,750.00 USD | 9,830.00 USD | 79,900.00 USD |
| `1D` | `8.30` | 366,520.00 USD | 0.00 USD | 366,520.00 USD | 94,260.00 USD | 22,600.00 USD | 23,810.00 USD |
| `7D` | `8.30` | 306,370.00 USD | 0.00 USD | 306,370.00 USD | 94,260.00 USD | 22,600.00 USD | 23,810.00 USD |
| `1D` | `8.32` | 225,850.00 USD | 0.00 USD | 225,850.00 USD | 74,570.00 USD | 20,010.00 USD | 8,890.00 USD |
| `7D` | `8.32` | 165,700.00 USD | 0.00 USD | 165,700.00 USD | 73,190.00 USD | 20,010.00 USD | 8,890.00 USD |
| `1D` | `8.34` | 122,380.00 USD | 0.00 USD | 122,380.00 USD | 4,100.00 USD | 0.00 USD | 23,920.00 USD |
| `7D` | `8.34` | 63,610.00 USD | 0.00 USD | 63,610.00 USD | 0.00 USD | 0.00 USD | 23,920.00 USD |
| `1D` | `8.36` | 94,360.00 USD | 0.00 USD | 94,360.00 USD | 2,940.00 USD | 0.00 USD | 37,880.00 USD |
| `7D` | `8.36` | 39,690.00 USD | 0.00 USD | 39,690.00 USD | 1,810.00 USD | 0.00 USD | 37,880.00 USD |
| `7D` | `8.37` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.38` | 53,540.00 USD | 0.00 USD | 53,540.00 USD | 1,510.00 USD | 0.00 USD | 52,030.00 USD |
| `7D` | `8.38` | 53,540.00 USD | 53,540.00 USD | 0.00 USD | 1,510.00 USD | 0.00 USD | 52,030.00 USD |
| `1D` | `8.39` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.40` | 87,300.00 USD | 87,300.00 USD | 0.00 USD | 1,220.00 USD | 22,890.00 USD | 63,190.00 USD |
| `7D` | `8.40` | 140,840.00 USD | 140,840.00 USD | 0.00 USD | 1,220.00 USD | 22,890.00 USD | 63,190.00 USD |
| `1D` | `8.42` | 110,830.00 USD | 110,830.00 USD | 0.00 USD | 995.87 USD | 22,540.00 USD | 0.00 USD |
| `7D` | `8.42` | 164,370.00 USD | 164,370.00 USD | 0.00 USD | 995.87 USD | 22,540.00 USD | 0.00 USD |
| `1D` | `8.44` | 154,690.00 USD | 154,690.00 USD | 0.00 USD | 427.96 USD | 43,430.00 USD | 0.00 USD |
| `7D` | `8.44` | 208,230.00 USD | 208,230.00 USD | 0.00 USD | 427.96 USD | 43,430.00 USD | 0.00 USD |
| `1D` | `8.46` | 189,530.00 USD | 189,530.00 USD | 0.00 USD | 0.00 USD | 34,820.00 USD | 18.78 USD |
| `7D` | `8.46` | 243,070.00 USD | 243,070.00 USD | 0.00 USD | 0.00 USD | 34,820.00 USD | 18.78 USD |
| `1D` | `8.48` | 258,780.00 USD | 258,780.00 USD | 0.00 USD | 0.00 USD | 69,250.00 USD | 0.00 USD |
| `7D` | `8.48` | 312,320.00 USD | 312,320.00 USD | 0.00 USD | 0.00 USD | 69,250.00 USD | 0.00 USD |
| `1D` | `8.50` | 524,290.00 USD | 524,290.00 USD | 0.00 USD | 206,180.00 USD | 59,320.00 USD | 12.70 USD |
| `7D` | `8.50` | 577,830.00 USD | 577,830.00 USD | 0.00 USD | 206,180.00 USD | 59,320.00 USD | 12.70 USD |
| `1D` | `8.52` | 713,290.00 USD | 713,290.00 USD | 0.00 USD | 123,250.00 USD | 65,750.00 USD | 1.32 USD |
| `7D` | `8.52` | 766,830.00 USD | 766,830.00 USD | 0.00 USD | 123,250.00 USD | 65,750.00 USD | 1.32 USD |
| `1D` | `8.54` | 748,660.00 USD | 748,660.00 USD | 0.00 USD | 35,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.54` | 802,200.00 USD | 802,200.00 USD | 0.00 USD | 35,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.56` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 158,900.00 USD | 0.00 USD | 106,490.00 USD |
| `7D` | `8.56` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 158,900.00 USD | 0.00 USD | 106,490.00 USD |
| `1D` | `8.58` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 102,500.00 USD | 0.00 USD | 144,480.00 USD |
| `7D` | `8.58` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 102,500.00 USD | 0.00 USD | 144,480.00 USD |
| `1D` | `8.60` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 53,060.00 USD | 65,000.00 USD |
| `7D` | `8.60` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 53,060.00 USD | 65,000.00 USD |
| `1D` | `8.62` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 28,330.00 USD | 35,930.00 USD | 27,290.00 USD |
| `7D` | `8.62` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 28,330.00 USD | 35,930.00 USD | 27,290.00 USD |
| `1D` | `8.64` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 21,050.00 USD | 0.00 USD |
| `7D` | `8.64` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 21,050.00 USD | 0.00 USD |
| `1D` | `8.66` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,010.00 USD |
| `7D` | `8.66` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,010.00 USD |
| `1D` | `8.68` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 24,580.00 USD | 7,700.00 USD | 39,650.00 USD |
| `7D` | `8.68` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 24,580.00 USD | 7,700.00 USD | 39,650.00 USD |
| `1D` | `8.70` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 36,540.00 USD | 0.00 USD | 22,180.00 USD |
| `7D` | `8.70` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 36,540.00 USD | 0.00 USD | 22,180.00 USD |
| `1D` | `8.72` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 18,250.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.72` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 18,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.74` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 11,970.00 USD | 0.00 USD |
| `7D` | `8.74` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 11,970.00 USD | 0.00 USD |
| `1D` | `8.76` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 78,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.76` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 80,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.78` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 107,520.00 USD | 0.00 USD | 35,600.00 USD |
| `7D` | `8.78` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 107,520.00 USD | 0.00 USD | 35,600.00 USD |
| `1D` | `8.80` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 61,700.00 USD | 17,690.00 USD | 37,430.00 USD |
| `7D` | `8.80` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 61,700.00 USD | 17,690.00 USD | 37,430.00 USD |
| `1D` | `8.82` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 15,900.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.82` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 15,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.84` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 8,820.00 USD | 68,750.00 USD |
| `7D` | `8.84` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 8,820.00 USD | 68,750.00 USD |
| `1D` | `8.86` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 12,400.00 USD | 2,250.00 USD | 148.46 USD |
| `7D` | `8.86` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 12,400.00 USD | 2,250.00 USD | 148.46 USD |
| `1D` | `8.88` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 8,950.00 USD | 0.00 USD |
| `7D` | `8.88` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 8,950.00 USD | 0.00 USD |
| `1D` | `8.90` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 27,890.00 USD | 8,140.00 USD | 97,330.00 USD |
| `7D` | `8.90` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 29,560.00 USD | 8,140.00 USD | 97,330.00 USD |
| `1D` | `8.92` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 37,770.00 USD | 7,360.00 USD | 17,020.00 USD |
| `7D` | `8.92` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 37,770.00 USD | 7,360.00 USD | 17,020.00 USD |
| `1D` | `8.94` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 41,740.00 USD | 12,260.00 USD | 17,500.00 USD |
| `7D` | `8.94` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 41,740.00 USD | 12,260.00 USD | 17,500.00 USD |
| `1D` | `8.98` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 24,340.00 USD | 5,550.00 USD | 19,410.00 USD |
| `7D` | `8.98` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 24,340.00 USD | 5,550.00 USD | 19,410.00 USD |
| `1D` | `9.00` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 85,360.00 USD | 30,520.00 USD | 11,130.00 USD |
| `7D` | `9.00` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 85,360.00 USD | 30,520.00 USD | 11,130.00 USD |
| `1D` | `9.02` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 39,130.00 USD | 43,160.00 USD | 18,840.00 USD |
| `7D` | `9.02` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 39,130.00 USD | 43,160.00 USD | 18,840.00 USD |
| `1D` | `9.04` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 87,540.00 USD | 43,590.00 USD | 38,590.00 USD |
| `7D` | `9.04` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 87,540.00 USD | 43,590.00 USD | 38,590.00 USD |
| `1D` | `9.06` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 33,880.00 USD | 33,420.00 USD | 60,040.00 USD |
| `7D` | `9.06` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 33,880.00 USD | 33,420.00 USD | 60,040.00 USD |
| `1D` | `9.08` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 28,800.00 USD | 29,710.00 USD | 70,940.00 USD |
| `7D` | `9.08` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 28,800.00 USD | 29,710.00 USD | 70,940.00 USD |
| `1D` | `9.10` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 197,560.00 USD | 43,240.00 USD | 63,030.00 USD |
| `7D` | `9.10` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 197,560.00 USD | 43,240.00 USD | 63,030.00 USD |
| `1D` | `9.12` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 160,000.00 USD | 47,350.00 USD | 56,020.00 USD |
| `7D` | `9.12` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 160,000.00 USD | 47,350.00 USD | 56,020.00 USD |
| `1D` | `9.14` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 118,520.00 USD | 23,510.00 USD | 67,330.00 USD |
| `7D` | `9.14` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 118,520.00 USD | 23,510.00 USD | 67,330.00 USD |
| `1D` | `9.16` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 121,090.00 USD | 41,060.00 USD | 51,890.00 USD |
| `7D` | `9.16` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 121,090.00 USD | 41,060.00 USD | 51,890.00 USD |
| `1D` | `9.18` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 187,840.00 USD | 53,800.00 USD | 92,160.00 USD |
| `7D` | `9.18` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 187,840.00 USD | 53,800.00 USD | 92,160.00 USD |
| `1D` | `9.20` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 197,260.00 USD | 57,280.00 USD | 81,060.00 USD |
| `7D` | `9.20` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 197,260.00 USD | 57,280.00 USD | 81,060.00 USD |
| `1D` | `9.22` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 126,810.00 USD | 12,990.00 USD | 13,790.00 USD |
| `7D` | `9.22` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 126,810.00 USD | 12,990.00 USD | 13,790.00 USD |
| `1D` | `9.24` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 71,810.00 USD | 4,560.00 USD | 27,900.00 USD |
| `7D` | `9.24` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 71,810.00 USD | 4,560.00 USD | 27,900.00 USD |
| `1D` | `9.26` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 35,150.00 USD | 8,290.00 USD | 9,560.00 USD |
| `7D` | `9.26` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 35,150.00 USD | 8,290.00 USD | 9,560.00 USD |
| `1D` | `9.28` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 44,130.00 USD | 7,140.00 USD | 2,660.00 USD |
| `7D` | `9.28` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 44,130.00 USD | 7,140.00 USD | 2,660.00 USD |
| `1D` | `9.30` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 58,890.00 USD | 13,560.00 USD | 23,390.00 USD |
| `7D` | `9.30` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 58,890.00 USD | 13,560.00 USD | 23,390.00 USD |
| `1D` | `9.32` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 37,200.00 USD | 4,250.00 USD | 23,700.00 USD |
| `7D` | `9.32` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 37,200.00 USD | 4,250.00 USD | 23,700.00 USD |
| `1D` | `9.34` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 23,850.00 USD | 10,190.00 USD | 17,530.00 USD |
| `7D` | `9.34` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 23,850.00 USD | 10,190.00 USD | 17,530.00 USD |
| `1D` | `9.36` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 59,430.00 USD | 14,870.00 USD | 33,530.00 USD |
| `7D` | `9.36` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 59,430.00 USD | 14,870.00 USD | 33,530.00 USD |
| `1D` | `9.38` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 65,320.00 USD | 17,450.00 USD | 31,170.00 USD |
| `7D` | `9.38` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 65,320.00 USD | 17,450.00 USD | 31,170.00 USD |
| `1D` | `9.40` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 52,090.00 USD | 1,210.00 USD | 25.34 USD |
| `7D` | `9.40` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 52,090.00 USD | 1,210.00 USD | 25.34 USD |
| `1D` | `9.42` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 30,730.00 USD | 4,670.00 USD | 17,990.00 USD |
| `7D` | `9.42` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 30,730.00 USD | 4,670.00 USD | 17,990.00 USD |
| `1D` | `9.44` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 10,560.00 USD | 1,630.00 USD | 12,410.00 USD |
| `7D` | `9.44` | 5,780,000.00 USD | 5,780,000.00 USD | 0.00 USD | 10,560.00 USD | 1,630.00 USD | 12,410.00 USD |
| `1D` | `9.46` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 1,630.00 USD | 4,580.00 USD | 2,430.00 USD |
| `7D` | `9.46` | 5,780,000.00 USD | 5,780,000.00 USD | 0.00 USD | 1,630.00 USD | 4,580.00 USD | 2,430.00 USD |
| `1D` | `9.48` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 2,800.00 USD | 1,100.00 USD | 5,380.00 USD |
| `7D` | `9.48` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 2,800.00 USD | 1,100.00 USD | 5,380.00 USD |
| `1D` | `9.50` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 42,390.00 USD | 3,730.00 USD | 8,950.00 USD |
| `7D` | `9.50` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 42,390.00 USD | 3,730.00 USD | 8,950.00 USD |
| `1D` | `9.52` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 17,470.00 USD | 3,070.00 USD | 5,520.00 USD |
| `7D` | `9.52` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 17,470.00 USD | 3,070.00 USD | 5,520.00 USD |
| `1D` | `9.54` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 23,980.00 USD | 7,790.00 USD | 2,930.00 USD |
| `7D` | `9.54` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 23,980.00 USD | 7,790.00 USD | 2,930.00 USD |
| `1D` | `9.56` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 6,950.00 USD | 7,610.00 USD | 5,600.00 USD |
| `7D` | `9.56` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 6,950.00 USD | 7,610.00 USD | 5,600.00 USD |
| `1D` | `9.58` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 1,270.00 USD | 4,910.00 USD | 12,620.00 USD |
| `7D` | `9.58` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 1,270.00 USD | 4,910.00 USD | 12,620.00 USD |
| `1D` | `9.60` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 15,230.00 USD | 1,680.00 USD | 16,260.00 USD |
| `7D` | `9.60` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 15,230.00 USD | 1,680.00 USD | 16,260.00 USD |
| `1D` | `9.62` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 20,200.00 USD | 4,140.00 USD | 14,420.00 USD |
| `7D` | `9.62` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 20,200.00 USD | 4,140.00 USD | 14,420.00 USD |
| `1D` | `9.64` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 22,380.00 USD | 5,430.00 USD | 8,050.00 USD |
| `7D` | `9.64` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 22,380.00 USD | 5,430.00 USD | 8,050.00 USD |
| `1D` | `9.66` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 14,580.00 USD | 7,630.00 USD | 7,480.00 USD |
| `7D` | `9.66` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 14,580.00 USD | 7,630.00 USD | 7,480.00 USD |
| `1D` | `9.68` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 16,150.00 USD | 2,950.00 USD | 6,270.00 USD |
| `7D` | `9.68` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 16,150.00 USD | 2,950.00 USD | 6,270.00 USD |
| `1D` | `9.70` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 19,500.00 USD | 6,860.00 USD | 3,370.00 USD |
| `7D` | `9.70` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 19,500.00 USD | 6,860.00 USD | 3,370.00 USD |
| `1D` | `9.72` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 2,830.00 USD | 8,870.00 USD | 5,230.00 USD |
| `7D` | `9.72` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 2,830.00 USD | 8,870.00 USD | 5,230.00 USD |
| `1D` | `9.74` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 6,960.00 USD | 738.05 USD | 3,140.00 USD |
| `7D` | `9.74` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 6,960.00 USD | 738.05 USD | 3,140.00 USD |
| `1D` | `9.76` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 7,400.00 USD | 2,560.00 USD | 5,340.00 USD |
| `7D` | `9.76` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 7,400.00 USD | 2,560.00 USD | 5,340.00 USD |
| `1D` | `9.78` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD |
| `7D` | `9.78` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD |
| `1D` | `9.80` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 12,580.00 USD | 770.83 USD | 9.39 USD |
| `7D` | `9.80` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 12,580.00 USD | 770.83 USD | 9.39 USD |
| `1D` | `9.82` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 14,340.00 USD | 1,540.00 USD | 6,190.00 USD |
| `7D` | `9.82` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 14,340.00 USD | 1,540.00 USD | 6,190.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `351.09M` | Total OI Tokens: `42,325,204.5 AVAX`
  * 1h OI Change: `-8.09%` | 4h OI Change: `-8.91%` | 24h OI Change: `-11.27%`
  * Exchange Breakdown: Binance=`82.99M` | Bybit=`55.90M` | OKX=`11.64M` | Hyperliquid=`16.35M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.89K` | Last 24h: `33.77K` | Last 3d: `72.05K` | Last 7d: `92.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0074%` | **USDT OKX** | `0.0093%` |
| **USDT Bybit** | `0.0000%` | **USDT KuCoin** | `0.0063%` |
| **USDT MEXC** | `0.0074%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0016%` | **USDT Bitget** | `0.0073%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `45.15%` | `54.85%` | `0.82` | 70,030,000.00 USD |
| `15M` | `Binance` | `44.25%` | `55.75%` | `0.79` | 25,740,000.00 USD |
| `15M` | `OKX` | `50.04%` | `49.96%` | `1.00` | 10,100,000.00 USD |
| `15M` | `Bybit` | `46.39%` | `53.61%` | `0.87` | 8,040,000.00 USD |
| `15M` | `KuCoin` | `59.41%` | `40.59%` | `1.46` | 543,280.00 USD |
| `15M` | `Gate` | `45.19%` | `54.81%` | `0.82` | 770,700.00 USD |
| `15M` | `Bitget` | `45.78%` | `54.22%` | `0.84` | 3,840,000.00 USD |
| `15M` | `BingX` | `36.35%` | `63.65%` | `0.57` | 1,860,000.00 USD |
| `15M` | `MEXC` | `48.97%` | `51.03%` | `0.96` | 9,680,000.00 USD |
| `15M` | `Bitunix` | `40.91%` | `59.09%` | `0.69` | 3,550,000.00 USD |
| `15M` | `Hyperliquid` | `36.33%` | `63.67%` | `0.57` | 2,840,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.97%` | `52.03%` | `0.92` | 1,240,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `14.46%` | `85.54%` | `0.17` | 1,110,000.00 USD |
| `15M` | `HTX` | `46.64%` | `53.36%` | `0.87` | 83,110.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `58.58%` | `41.42%` | `1.41` | 363,020.00 USD |
| `15M` | `Aster` | `43.55%` | `56.45%` | `0.77` | 104,570.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `38.71%` | `61.29%` | `0.63` | 177,660.00 USD |
| `15M` | `Whale Positions` | `44.25%` | `55.75%` | `0.79` | 25,740,000.00 USD |
| `15M` | `Global Accounts` | `45.15%` | `54.85%` | `0.82` | 70,030,000.00 USD |
| `1H` | `AVAX` | `41.36%` | `58.64%` | `0.71` | 61,830,000.00 USD |
| `1H` | `Binance` | `41.07%` | `58.93%` | `0.70` | 26,560,000.00 USD |
| `1H` | `OKX` | `50.19%` | `49.81%` | `1.01` | 4,280,000.00 USD |
| `1H` | `Bybit` | `40.79%` | `59.21%` | `0.69` | 5,520,000.00 USD |
| `1H` | `KuCoin` | `37.94%` | `62.06%` | `0.61` | 553,960.00 USD |
| `1H` | `Gate` | `41.4%` | `58.6%` | `0.71` | 1,420,000.00 USD |
| `1H` | `Bitget` | `45.77%` | `54.23%` | `0.84` | 1,270,000.00 USD |
| `1H` | `BingX` | `42.06%` | `57.94%` | `0.73` | 3,490,000.00 USD |
| `1H` | `MEXC` | `38.48%` | `61.52%` | `0.63` | 4,050,000.00 USD |
| `1H` | `Bitunix` | `32.41%` | `67.59%` | `0.48` | 1,950,000.00 USD |
| `1H` | `Hyperliquid` | `38.53%` | `61.47%` | `0.63` | 1,320,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.28%` | `51.72%` | `0.93` | 9,250,000.00 USD |
| `1H` | `Crypto.com` | `38.23%` | `61.77%` | `0.62` | 18,420.00 USD |
| `1H` | `WhiteBIT` | `1.46%` | `98.54%` | `0.01` | 1,560,000.00 USD |
| `1H` | `HTX` | `53.24%` | `46.76%` | `1.14` | 48,640.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `42.35%` | `57.65%` | `0.73` | 328,950.00 USD |
| `1H` | `Aster` | `22.84%` | `77.16%` | `0.30` | 92,020.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `31.88%` | `68.12%` | `0.47` | 120,120.00 USD |
| `1H` | `Whale Positions` | `41.07%` | `58.93%` | `0.70` | 26,560,000.00 USD |
| `1H` | `Global Accounts` | `41.36%` | `58.64%` | `0.71` | 61,830,000.00 USD |
| `4H` | `AVAX` | `44.39%` | `55.61%` | `0.80` | 163,070,000.00 USD |
| `4H` | `Binance` | `44.3%` | `55.7%` | `0.80` | 50,730,000.00 USD |
| `4H` | `OKX` | `45.42%` | `54.58%` | `0.83` | 18,170,000.00 USD |
| `4H` | `Bybit` | `43.78%` | `56.22%` | `0.78` | 15,850,000.00 USD |
| `4H` | `KuCoin` | `48.6%` | `51.4%` | `0.95` | 1,230,000.00 USD |
| `4H` | `Gate` | `42.59%` | `57.41%` | `0.74` | 1,810,000.00 USD |
| `4H` | `Bitget` | `44.11%` | `55.89%` | `0.79` | 6,830,000.00 USD |
| `4H` | `BingX` | `41.7%` | `58.3%` | `0.72` | 5,180,000.00 USD |
| `4H` | `MEXC` | `49.08%` | `50.92%` | `0.96` | 43,640,000.00 USD |
| `4H` | `Bitunix` | `43.84%` | `56.16%` | `0.78` | 6,480,000.00 USD |
| `4H` | `Hyperliquid` | `26.12%` | `73.88%` | `0.35` | 3,860,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.98%` | `50.02%` | `1.00` | 3,880,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `9.19%` | `90.81%` | `0.10` | 3,540,000.00 USD |
| `4H` | `HTX` | `50.74%` | `49.26%` | `1.03` | 105,190.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.45%` | `56.55%` | `0.77` | 891,000.00 USD |
| `4H` | `Aster` | `13.32%` | `86.68%` | `0.15` | 572,020.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.87%` | `58.13%` | `0.72` | 296,490.00 USD |
| `4H` | `Whale Positions` | `44.3%` | `55.7%` | `0.80` | 50,730,000.00 USD |
| `4H` | `Global Accounts` | `44.39%` | `55.61%` | `0.80` | 163,070,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `8.81` | `8.81` | `8.81` | `8.84` | `8.80` | 1,762,248.06 USD | 773,632.57 USD | 988,615.48 USD | -214,982.91 USD | `-12.20%` | `7B / 6S` |
| `5:00 UTC` | `8.84` | `8.83` | `8.84` | `8.86` | `8.79` | 750,878.19 USD | 458,225.53 USD | 292,652.66 USD | 165,572.87 USD | `+22.05%` | `19B / 3S` |
| `0:00 UTC` | `8.82` | `8.82` | `8.82` | `8.84` | `8.80` | 637,816.13 USD | 328,825.06 USD | 308,991.07 USD | 19,833.99 USD | `+3.11%` | `4B / 4S` |
| `5:00 UTC` | `8.81` | `8.82` | `8.81` | `8.84` | `8.80` | 548,929.60 USD | 300,754.28 USD | 248,175.32 USD | 52,578.96 USD | `+9.58%` | `18B / 4S` |
| `0:00 UTC` | `8.86` | `8.86` | `8.86` | `8.87` | `8.83` | 587,148.06 USD | 393,702.30 USD | 193,445.76 USD | 200,256.54 USD | `+34.11%` | `5B / 1S` |
| `5:00 UTC` | `8.85` | `8.85` | `8.85` | `8.87` | `8.84` | 431,773.06 USD | 190,520.19 USD | 241,252.88 USD | -50,732.69 USD | `-11.75%` | `8B / 6S` |
| `0:00 UTC` | `8.73` | `8.73` | `8.73` | `8.86` | `8.66` | 5,568,654.06 USD | 2,589,240.15 USD | 2,979,413.92 USD | -390,173.77 USD | `-7.01%` | `5B / 25S` |
| `5:00 UTC` | `8.77` | `8.75` | `8.77` | `8.78` | `8.73` | 2,097,434.25 USD | 1,386,379.16 USD | 711,055.10 USD | 675,324.06 USD | `+32.20%` | `14B / 3S` |
| `0:00 UTC` | `8.61` | `8.53` | `8.61` | `8.76` | `8.39` | 13,163,243.09 USD | 4,547,421.99 USD | 8,615,821.10 USD | -4,068,399.10 USD | `-30.91%` | `4B / 57S` |
| `5:00 UTC` | `8.26` | `8.35` | `8.26` | `8.48` | `8.25` | 14,213,574.24 USD | 5,739,575.32 USD | 8,473,998.93 USD | -2,734,423.61 USD | `-19.24%` | `8B / 16S` |

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
| `5m` | -9,970.00 USD | 194,360.00 USD | **`ACCUMULATION`** |
| `15m` | -1,230,000.00 USD | -7,980,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,560,000.00 USD | -8,740,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,650,000.00 USD | -8,490,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,760,000.00 USD | -7,880,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,830,000.00 USD | -10,440,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,650,000.00 USD | -11,560,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,570,000.00 USD | -10,640,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,900,000.00 USD | -11,280,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,650,000.00 USD | -14,230,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,520,000.00 USD | -50,360,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -55,180,000.00 USD | -281,140,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-9.97K` | 15m=`-1.23M` | 1h=`-1.65M` | 24h=`-1.65M`
* Futures Capital Netflows: 5m=`+194.36K` | 15m=`-7.98M` | 1h=`-8.49M` | 24h=`-14.23M`
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
  * `2026-10-30 02:14:39 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:39 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:39 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `8.55` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.39` (Risk Distance: `0.1569` pts)
  * +2.5R Take Profit: `8.94`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.90` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `9.06` (Risk Distance: `0.1569` pts)
  * +2.5R Take Profit: `8.51`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.46`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
