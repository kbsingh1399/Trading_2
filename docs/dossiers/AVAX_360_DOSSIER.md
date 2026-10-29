# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:00:21 IST` (`2026-10-29 20:30:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.74` | **Live Ask Quote**: `8.77` | **Mid Price**: `8.75`
- **Spread Points**: `3.00` | **Spread BPS**: `34.27 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.76` | VWAP Z-Score: `-0.35` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0599` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `37.27` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `9.12` | Lower -3.00σ Band: `8.40`
  * Upper +2.51σ Band: `9.06` | Lower -2.51σ Band: `8.46`
  * Upper +2.01σ Band: `9.00` | Lower -2.01σ Band: `8.52`
  * Upper +2.00σ Band: `9.00` | Lower -2.00σ Band: `8.52`
  * Upper +1.28σ Band: `8.92` | Lower -1.28σ Band: `8.61`
  * Upper +1.00σ Band: `8.88` | Lower -1.00σ Band: `8.64`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.81` | EMA-20=`8.83` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.81` (Slope: `+0.0000`) | EMA-100=`8.81`
  * Institutional Anchors: EMA-144=`8.82` | EMA-200=`8.82` (Slope: `-0.0068`) | EMA-233=`8.83`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`8.53` | Weekly High=`9.14` | Weekly Low=`8.53`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.90` (Distance: `-1.73%`)
  * Point of Control (POC) = `8.74` (Distance: `+0.05%`)
  * Value Area Low (VAL) = `8.58` (Distance: `+1.91%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `8.72` - `8.79`
  * Optimal Trade Entry (OTE 0.705): `8.77`
  * Structural Invalidation Anchor (0.786): `8.83`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.71` | `8.74` | `8.68` | `8.74` | `85,705` | 747,121.46 USD | 135,503.73 USD | `+18.14%` | -4,153,475.03 USD | `+0.66` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `8.74` | `8.76` | `8.73` | `8.76` | `98,679` | 863,312.00 USD | 269,329.80 USD | `+31.20%` | -3,884,145.23 USD | `+1.16` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `8.76` | `8.78` | `8.73` | `8.75` | `91,705` | 803,609.41 USD | 491,898.53 USD | `+61.21%` | -3,392,246.70 USD | `+1.85` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `8.85` | `8.87` | `8.84` | `8.85` | `48,790` | 431,773.06 USD | -50,732.69 USD | `-11.75%` | -3,709,962.02 USD | `+0.20` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `8.85` | `8.86` | `8.65` | `8.74` | `637,654` | 5,568,654.07 USD | -390,173.77 USD | `-7.01%` | -4,100,135.79 USD | `-0.75` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `8.74` | `8.78` | `8.73` | `8.75` | `190,384` | 1,666,921.41 USD | 761,228.32 USD | `+45.67%` | -3,338,907.46 USD | `+2.21` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `8.87` | `8.89` | `8.79` | `8.84` | `435,467` | 3,847,058.68 USD | -67,411.45 USD | `-1.75%` | -4,291,060.73 USD | `+0.32` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `8.84` | `8.87` | `8.80` | `8.85` | `249,668` | 2,205,666.85 USD | 221,936.79 USD | `+10.06%` | -4,069,123.94 USD | `+0.91` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `8.85` | `8.86` | `8.65` | `8.75` | `828,060` | 7,235,768.06 USD | 370,949.52 USD | `+5.13%` | -3,698,174.42 USD | `+1.09` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -2,154,015.33 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -4,666,010.97 USD | `-1.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.65` | `8.75` | `828,063` | 7,235,794.33 USD | 370,923.25 USD | `+5.13%` | -4,295,087.72 USD | `+0.87` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `8.59` | `8.80` | `8.57` | `8.62` | `1,816,830` | 15,790,058.74 USD | 58,580.54 USD | `+0.37%` | -2,364,450.84 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -2,100,193.35 USD | `+0.79` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -2,154,015.33 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -4,666,010.97 USD | `-1.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.65` | `8.75` | `828,063` | 7,235,794.33 USD | 370,923.25 USD | `+5.13%` | -4,295,087.72 USD | `+0.87` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`8.75`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BUY` | `8.58` | `2563.2600` | 21,999.95 USD | 4,966,232.81 USD | `STANDARD` | `-1.98%` | `0x0efb38a5fa` |
| `BUY` | `8.59` | `383.1700` | 3,289.82 USD | 6,075,162.09 USD | `STANDARD` | `-1.95%` | `0x14f8e04290` |
| `BUY` | `8.60` | `14965.6400` | 128,735.93 USD | 3,561,302.72 USD | `LARGE (>= USD 100K)` | `-1.76%` | `0xecb63caa47` |
| `BUY` | `8.60` | `383.5300` | 3,298.24 USD | 6,071,872.27 USD | `STANDARD` | `-1.79%` | `0x14f8e04290` |
| `BUY` | `8.60` | `100.0000` | 860.00 USD | 6,314,667.33 USD | `STANDARD` | `-1.79%` | `0x2ea69a6a67` |
| `BUY` | `8.62` | `12986.5500` | 111,979.12 USD | 4,146,706.84 USD | `LARGE (>= USD 100K)` | `-1.53%` | `0x71d0e11ebb` |
| `BUY` | `8.62` | `10908.8800` | 94,031.27 USD | 4,541,529.88 USD | `MEDIUM (>= USD 25K)` | `-1.56%` | `0xecb63caa47` |
| `BUY` | `8.62` | `3707.9200` | 31,946.70 USD | 4,825,124.16 USD | `MEDIUM (>= USD 25K)` | `-1.61%` | `0xa38f19c4cc` |
| `BUY` | `8.62` | `2203.0500` | 18,999.98 USD | 5,023,496.71 USD | `STANDARD` | `-1.51%` | `0x0efb38a5fa` |
| `BUY` | `8.62` | `315.7300` | 2,722.86 USD | 6,190,850.35 USD | `STANDARD` | `-1.51%` | `0x07fd993f0f` |
| `BUY` | `8.62` | `197.3100` | 1,701.46 USD | 6,276,930.36 USD | `STANDARD` | `-1.52%` | `0x31ca8395cf` |
| `BUY` | `8.62` | `181.8800` | 1,568.53 USD | 6,283,388.66 USD | `STANDARD` | `-1.51%` | `0x010461c14e` |
| `BUY` | `8.64` | `8613.9900` | 74,398.17 USD | 4,615,928.05 USD | `MEDIUM (>= USD 25K)` | `-1.37%` | `0xecb63caa47` |
| `BUY` | `8.64` | `4123.2300` | 35,629.24 USD | 4,761,230.71 USD | `MEDIUM (>= USD 25K)` | `-1.32%` | `0xa24c5ca26c` |
| `BUY` | `8.64` | `2140.7500` | 18,494.58 USD | 5,079,575.68 USD | `STANDARD` | `-1.34%` | `0xd3943e4008` |
| `BUY` | `8.64` | `389.3900` | 3,363.43 USD | 6,065,215.17 USD | `STANDARD` | `-1.36%` | `0x14f8e04290` |
| `BUY` | `8.64` | `366.8200` | 3,169.03 USD | 6,142,931.13 USD | `STANDARD` | `-1.34%` | `0xdd4f66125d` |
| `BUY` | `8.65` | `17660.1400` | 152,742.55 USD | 2,875,242.62 USD | `LARGE (>= USD 100K)` | `-1.23%` | `0x71d0e11ebb` |
| `BUY` | `8.65` | `7867.3700` | 68,086.58 USD | 4,684,014.63 USD | `MEDIUM (>= USD 25K)` | `-1.17%` | `0xecb63caa47` |
| `BUY` | `8.65` | `1849.4900` | 15,999.94 USD | 5,111,575.58 USD | `STANDARD` | `-1.21%` | `0x0efb38a5fa` |
| `BUY` | `8.66` | `47157.9800` | 408,609.75 USD | 1,641,572.25 USD | `LARGE (>= USD 100K)` | `-1.05%` | `0x71cfa5e263` |
| `BUY` | `8.66` | `229.4000` | 1,986.54 USD | 6,264,409.41 USD | `STANDARD` | `-1.11%` | `0x39bac00809` |
| `BUY` | `8.66` | `80.9900` | 701.75 USD | 6,328,851.57 USD | `STANDARD` | `-1.05%` | `0x010461c14e` |
| `BUY` | `8.67` | `1742.8700` | 15,118.35 USD | 5,142,048.92 USD | `STANDARD` | `-0.94%` | `0xd3943e4008` |
| `BUY` | `8.67` | `1359.8300` | 11,785.37 USD | 5,625,532.99 USD | `STANDARD` | `-1.02%` | `0x33ad48ed92` |
| `BUY` | `8.67` | `389.3900` | 3,375.35 USD | 6,061,851.74 USD | `STANDARD` | `-1.01%` | `0x14f8e04290` |
| `BUY` | `8.67` | `366.8200` | 3,180.59 USD | 6,130,242.73 USD | `STANDARD` | `-0.98%` | `0xdd4f66125d` |
| `BUY` | `8.67` | `77.3500` | 670.67 USD | 6,330,915.66 USD | `STANDARD` | `-0.98%` | `0x31ca8395cf` |
| `BUY` | `8.68` | `22398.7000` | 194,398.32 USD | 2,256,765.55 USD | `LARGE (>= USD 100K)` | `-0.89%` | `0xa20fb0c9e0` |
| `BUY` | `8.68` | `1479.6000` | 12,841.30 USD | 5,167,896.58 USD | `STANDARD` | `-0.89%` | `0xd3943e4008` |
| `BUY` | `8.68` | `131.2700` | 1,139.76 USD | 6,300,433.38 USD | `STANDARD` | `-0.84%` | `0xe34d21d198` |
| `BUY` | `8.69` | `17664.6400` | 153,470.39 USD | 2,722,500.07 USD | `LARGE (>= USD 100K)` | `-0.78%` | `0x71d0e11ebb` |
| `BUY` | `8.69` | `11522.7500` | 100,117.72 USD | 4,347,381.28 USD | `LARGE (>= USD 100K)` | `-0.77%` | `0x881cd92459` |
| `BUY` | `8.69` | `3559.0100` | 30,935.98 USD | 4,856,060.14 USD | `MEDIUM (>= USD 25K)` | `-0.73%` | `0x26934acbd3` |
| `BUY` | `8.69` | `1380.8300` | 11,999.97 USD | 5,554,211.35 USD | `STANDARD` | `-0.76%` | `0x0efb38a5fa` |
| `BUY` | `8.69` | `1250.0000` | 10,858.00 USD | 5,691,910.09 USD | `STANDARD` | `-0.80%` | `0xb7bd9cef0e` |
| `BUY` | `8.70` | `2159.1800` | 18,792.21 USD | 5,042,288.92 USD | `STANDARD` | `-0.61%` | `0xa38f19c4cc` |
| `BUY` | `8.70` | `1380.2000` | 12,011.60 USD | 5,530,211.23 USD | `STANDARD` | `-0.61%` | `0x57d8e75f47` |
| `BUY` | `8.70` | `1307.0600` | 11,367.89 USD | 5,636,900.89 USD | `STANDARD` | `-0.68%` | `0xd3943e4008` |
| `BUY` | `8.70` | `1026.8300` | 8,931.06 USD | 5,828,712.11 USD | `STANDARD` | `-0.67%` | `0x33ad48ed92` |
| `BUY` | `8.70` | `492.5700` | 4,284.18 USD | 6,004,526.49 USD | `STANDARD` | `-0.67%` | `0xcd7f60e943` |
| `BUY` | `8.70` | `231.2300` | 2,012.53 USD | 6,260,411.50 USD | `STANDARD` | `-0.60%` | `0x9d732bed51` |
| `BUY` | `8.70` | `231.2300` | 2,011.38 USD | 6,262,422.87 USD | `STANDARD` | `-0.66%` | `0x9d732bed51` |
| `BUY` | `8.70` | `81.8200` | 712.14 USD | 6,327,444.95 USD | `STANDARD` | `-0.60%` | `0x31ca8395cf` |
| `BUY` | `8.70` | `79.5300` | 692.22 USD | 6,330,244.99 USD | `STANDARD` | `-0.60%` | `0x010461c14e` |
| `BUY` | `8.71` | `24028.1100` | 209,191.13 USD | 2,062,367.24 USD | `LARGE (>= USD 100K)` | `-0.58%` | `0x71cfa5e263` |
| `BUY` | `8.71` | `14933.8500` | 130,081.30 USD | 3,432,566.79 USD | `LARGE (>= USD 100K)` | `-0.53%` | `0x71d0e11ebb` |
| `BUY` | `8.71` | `1380.2000` | 12,025.54 USD | 5,494,159.44 USD | `STANDARD` | `-0.50%` | `0x57d8e75f47` |
| `BUY` | `8.71` | `1380.2000` | 12,021.82 USD | 5,506,181.25 USD | `STANDARD` | `-0.53%` | `0x57d8e75f47` |
| `BUY` | `8.71` | `1380.2000` | 12,018.37 USD | 5,518,199.62 USD | `STANDARD` | `-0.56%` | `0x57d8e75f47` |
| `BUY` | `8.71` | `1041.5000` | 9,073.55 USD | 5,810,827.01 USD | `STANDARD` | `-0.51%` | `0xd3943e4008` |
| `BUY` | `8.71` | `918.0500` | 7,999.98 USD | 5,869,474.18 USD | `STANDARD` | `-0.48%` | `0x0efb38a5fa` |
| `BUY` | `8.71` | `830.0000` | 7,230.96 USD | 5,899,712.66 USD | `STANDARD` | `-0.51%` | `0xb7bd9cef0e` |
| `BUY` | `8.71` | `760.2300` | 6,622.06 USD | 5,906,334.71 USD | `STANDARD` | `-0.52%` | `0x26934acbd3` |
| `BUY` | `8.71` | `372.2400` | 3,242.28 USD | 6,111,001.51 USD | `STANDARD` | `-0.53%` | `0x2a72b57dea` |
| `BUY` | `8.71` | `366.8200` | 3,196.10 USD | 6,127,062.14 USD | `STANDARD` | `-0.50%` | `0xdd4f66125d` |
| `BUY` | `8.71` | `231.2300` | 2,014.48 USD | 6,254,372.41 USD | `STANDARD` | `-0.51%` | `0x9d732bed51` |
| `BUY` | `8.71` | `231.2300` | 2,013.55 USD | 6,256,385.96 USD | `STANDARD` | `-0.55%` | `0x9d732bed51` |
| `BUY` | `8.71` | `131.2700` | 1,142.72 USD | 6,299,293.61 USD | `STANDARD` | `-0.59%` | `0xe34d21d198` |
| `BUY` | `8.72` | `1380.2000` | 12,041.42 USD | 5,446,033.79 USD | `STANDARD` | `-0.37%` | `0x57d8e75f47` |
| `BUY` | `8.72` | `1380.2000` | 12,037.41 USD | 5,458,071.21 USD | `STANDARD` | `-0.40%` | `0x57d8e75f47` |
| `BUY` | `8.72` | `1380.2000` | 12,033.41 USD | 5,470,104.62 USD | `STANDARD` | `-0.43%` | `0x57d8e75f47` |
| `BUY` | `8.72` | `1380.2000` | 12,029.27 USD | 5,482,133.89 USD | `STANDARD` | `-0.47%` | `0x57d8e75f47` |
| `BUY` | `8.72` | `1267.2200` | 11,054.21 USD | 5,659,009.32 USD | `STANDARD` | `-0.38%` | `0xa38f19c4cc` |
| `BUY` | `8.72` | `953.4400` | 8,316.38 USD | 5,845,473.65 USD | `STANDARD` | `-0.39%` | `0xd3943e4008` |
| `BUY` | `8.72` | `672.8100` | 5,868.52 USD | 5,955,870.56 USD | `STANDARD` | `-0.39%` | `0x33ad48ed92` |
| `BUY` | `8.72` | `619.4000` | 5,401.23 USD | 5,966,805.19 USD | `STANDARD` | `-0.42%` | `0xecb63caa47` |
| `BUY` | `8.72` | `372.2400` | 3,244.89 USD | 6,107,759.22 USD | `STANDARD` | `-0.45%` | `0x2a72b57dea` |
| `BUY` | `8.72` | `277.8400` | 2,424.15 USD | 6,206,217.34 USD | `STANDARD` | `-0.36%` | `0xecb63caa47` |
| `BUY` | `8.72` | `254.0300` | 2,214.89 USD | 6,219,924.55 USD | `STANDARD` | `-0.43%` | `0xecb63caa47` |
| `BUY` | `8.72` | `231.2300` | 2,016.51 USD | 6,250,342.39 USD | `STANDARD` | `-0.41%` | `0x9d732bed51` |
| `BUY` | `8.72` | `231.2300` | 2,015.54 USD | 6,252,357.93 USD | `STANDARD` | `-0.46%` | `0x9d732bed51` |
| `BUY` | `8.72` | `111.9000` | 976.24 USD | 6,312,833.48 USD | `STANDARD` | `-0.37%` | `0x23cc6b8202` |
| `BUY` | `8.72` | `83.5700` | 728.97 USD | 6,324,578.22 USD | `STANDARD` | `-0.38%` | `0x31ca8395cf` |
| `BUY` | `8.72` | `75.5000` | 658.58 USD | 6,332,236.92 USD | `STANDARD` | `-0.38%` | `0x010461c14e` |
| `BUY` | `8.73` | `3453.2000` | 30,156.80 USD | 4,916,374.14 USD | `MEDIUM (>= USD 25K)` | `-0.27%` | `0x08a49e7f71` |
| `BUY` | `8.73` | `1380.2000` | 12,055.22 USD | 5,409,894.09 USD | `STANDARD` | `-0.25%` | `0x57d8e75f47` |
| `BUY` | `8.73` | `1380.2000` | 12,051.77 USD | 5,421,945.85 USD | `STANDARD` | `-0.28%` | `0x57d8e75f47` |
| `BUY` | `8.73` | `1380.2000` | 12,046.52 USD | 5,433,992.38 USD | `STANDARD` | `-0.32%` | `0x57d8e75f47` |
| `BUY` | `8.73` | `1261.3300` | 11,010.02 USD | 5,681,052.09 USD | `STANDARD` | `-0.32%` | `0x26934acbd3` |
| `BUY` | `8.73` | `1137.9700` | 9,938.69 USD | 5,782,433.21 USD | `STANDARD` | `-0.26%` | `0xaf9f722a67` |
| `BUY` | `8.73` | `744.6000` | 6,502.44 USD | 5,912,837.16 USD | `STANDARD` | `-0.27%` | `0xa38f19c4cc` |
| `BUY` | `8.73` | `742.4300` | 6,481.86 USD | 5,925,821.43 USD | `STANDARD` | `-0.30%` | `0xecb63caa47` |
| `BUY` | `8.73` | `571.5000` | 4,990.74 USD | 5,986,809.84 USD | `STANDARD` | `-0.27%` | `0x3ca146d269` |
| `BUY` | `8.73` | `420.0000` | 3,668.28 USD | 6,048,251.24 USD | `STANDARD` | `-0.26%` | `0xb7bd9cef0e` |
| `BUY` | `8.73` | `372.2400` | 3,250.47 USD | 6,101,265.98 USD | `STANDARD` | `-0.28%` | `0x2a72b57dea` |
| `BUY` | `8.73` | `372.2400` | 3,248.35 USD | 6,104,514.33 USD | `STANDARD` | `-0.34%` | `0x2a72b57dea` |
| `BUY` | `8.73` | `363.0200` | 3,170.58 USD | 6,139,762.10 USD | `STANDARD` | `-0.26%` | `0xecb63caa47` |
| `BUY` | `8.73` | `231.2300` | 2,019.63 USD | 6,244,289.67 USD | `STANDARD` | `-0.25%` | `0x9d732bed51` |
| `BUY` | `8.73` | `231.2300` | 2,018.68 USD | 6,246,308.36 USD | `STANDARD` | `-0.30%` | `0x9d732bed51` |
| `BUY` | `8.73` | `231.2300` | 2,017.53 USD | 6,248,325.88 USD | `STANDARD` | `-0.36%` | `0x9d732bed51` |
| `BUY` | `8.73` | `131.2700` | 1,145.53 USD | 6,298,150.89 USD | `STANDARD` | `-0.34%` | `0xe34d21d198` |
| `BUY` | `8.73` | `85.7800` | 749.28 USD | 6,319,396.99 USD | `STANDARD` | `-0.25%` | `0x31ca8395cf` |
| `BUY` | `8.74` | `16888.3800` | 147,530.13 USD | 3,171,014.22 USD | `LARGE (>= USD 100K)` | `-0.24%` | `0x71d0e11ebb` |
| `BUY` | `8.74` | `1380.2000` | 12,066.54 USD | 5,373,718.08 USD | `STANDARD` | `-0.16%` | `0x57d8e75f47` |
| `BUY` | `8.74` | `1380.2000` | 12,062.12 USD | 5,385,780.20 USD | `STANDARD` | `-0.20%` | `0x57d8e75f47` |
| `BUY` | `8.74` | `1380.2000` | 12,058.67 USD | 5,397,838.87 USD | `STANDARD` | `-0.22%` | `0x57d8e75f47` |
| `BUY` | `8.74` | `1372.2200` | 11,999.79 USD | 5,578,211.10 USD | `STANDARD` | `-0.13%` | `0x7d0c59691f` |
| `BUY` | `8.74` | `1137.9700` | 9,948.59 USD | 5,772,494.52 USD | `STANDARD` | `-0.16%` | `0xaf9f722a67` |
| `BUY` | `8.74` | `572.3300` | 4,999.93 USD | 5,981,819.11 USD | `STANDARD` | `-0.23%` | `0x0efb38a5fa` |
| `BUY` | `8.74` | `481.6400` | 4,208.81 USD | 6,021,494.95 USD | `STANDARD` | `-0.21%` | `0x7717a7a245` |
| `BUY` | `8.74` | `454.7200` | 3,975.75 USD | 6,025,470.70 USD | `STANDARD` | `-0.15%` | `0xecb63caa47` |
| `BUY` | `8.74` | `442.5100` | 3,867.98 USD | 6,033,245.39 USD | `STANDARD` | `-0.18%` | `0xecb63caa47` |
| `BUY` | `8.74` | `437.5000` | 3,824.98 USD | 6,037,070.37 USD | `STANDARD` | `-0.16%` | `0xa38f19c4cc` |
| `BUY` | `8.74` | `384.3700` | 3,358.86 USD | 6,068,574.03 USD | `STANDARD` | `-0.20%` | `0xecb63caa47` |
| `BUY` | `8.74` | `372.2400` | 3,253.04 USD | 6,098,015.51 USD | `STANDARD` | `-0.20%` | `0x2a72b57dea` |
| `BUY` | `8.74` | `363.3700` | 3,176.33 USD | 6,133,419.05 USD | `STANDARD` | `-0.17%` | `0x6ba889db7f` |
| `BUY` | `8.74` | `360.4700` | 3,149.93 USD | 6,168,206.59 USD | `STANDARD` | `-0.21%` | `0x6ba889db7f` |
| `BUY` | `8.74` | `360.4300` | 3,148.61 USD | 6,171,355.20 USD | `STANDARD` | `-0.24%` | `0x6ba889db7f` |
| `BUY` | `8.74` | `301.4100` | 2,633.90 USD | 6,198,793.33 USD | `STANDARD` | `-0.20%` | `0x26934acbd3` |
| `BUY` | `8.74` | `269.1200` | 2,351.81 USD | 6,210,945.36 USD | `STANDARD` | `-0.20%` | `0x33ad48ed92` |
| `BUY` | `8.74` | `231.2300` | 2,020.63 USD | 6,242,270.04 USD | `STANDARD` | `-0.20%` | `0x9d732bed51` |
| `BUY` | `8.74` | `211.1800` | 1,846.66 USD | 6,268,147.85 USD | `STANDARD` | `-0.14%` | `0x023a3d0580` |
| `BUY` | `8.74` | `137.5600` | 1,202.47 USD | 6,291,131.47 USD | `STANDARD` | `-0.17%` | `0xdd4f66125d` |
| `BUY` | `8.74` | `137.5600` | 1,202.14 USD | 6,292,333.61 USD | `STANDARD` | `-0.20%` | `0xdd4f66125d` |
| `BUY` | `8.74` | `137.5600` | 1,202.11 USD | 6,293,535.71 USD | `STANDARD` | `-0.20%` | `0xdd4f66125d` |
| `BUY` | `8.74` | `114.3500` | 999.96 USD | 6,310,857.30 USD | `STANDARD` | `-0.14%` | `0x27c9fa86c9` |
| `BUY` | `8.74` | `85.2300` | 744.64 USD | 6,322,383.55 USD | `STANDARD` | `-0.23%` | `0x010461c14e` |
| `BUY` | `8.74` | `83.4800` | 729.81 USD | 6,323,849.25 USD | `STANDARD` | `-0.16%` | `0x2eddf3aa5c` |
| `BUY` | `8.74` | `57.3100` | 501.02 USD | 6,341,912.57 USD | `STANDARD` | `-0.16%` | `0x57d8e75f47` |
| `BUY` | `8.74` | `57.3100` | 500.74 USD | 6,342,413.31 USD | `STANDARD` | `-0.22%` | `0x57d8e75f47` |
| `BID` | `8.75` | `143.1000` | 1,252.80 USD | 1,392.90 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.75` | `46.8200` | 409.79 USD | 1,802.69 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.75` | `360.2900` | 3,153.37 USD | 4,956.06 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.75` | `46.8300` | 409.87 USD | 5,365.92 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.75` | `138.6200` | 1,213.20 USD | 6,579.12 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.75` | `52.6300` | 460.60 USD | 7,039.72 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `8.75` | `1380.2000` | 12,078.96 USD | 19,118.68 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.75` | `29.0300` | 254.05 USD | 19,372.73 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.75` | `95.9000` | 839.18 USD | 20,211.91 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `8.75` | `685.6600` | 5,999.87 USD | 26,211.78 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.75` | `62.6500` | 548.21 USD | 26,759.99 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `8.75` | `46.8400` | 409.86 USD | 27,169.86 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.75` | `49.8800` | 436.46 USD | 27,606.32 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `8.75` | `150.2800` | 1,314.89 USD | 28,921.21 USD | `3 orders` | `-0.08%` | `-` |
| `BID` | `8.75` | `111.6500` | 976.85 USD | 29,898.06 USD | `2 orders` | `-0.08%` | `-` |
| `BID` | `8.75` | `1494.4900` | 13,075.44 USD | 42,973.50 USD | `2 orders` | `-0.09%` | `-` |
| `BID` | `8.75` | `360.4100` | 3,153.19 USD | 46,126.69 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `8.75` | `914.4100` | 7,999.99 USD | 54,126.68 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `8.75` | `123.1500` | 1,077.40 USD | 55,204.08 USD | `1 orders` | `-0.09%` | `-` |
| `BUY` | `8.75` | `1380.2000` | 12,078.96 USD | 5,337,503.98 USD | `STANDARD` | `-0.06%` | `0x57d8e75f47` |
| `BUY` | `8.75` | `1380.2000` | 12,075.51 USD | 5,349,579.48 USD | `STANDARD` | `-0.09%` | `0x57d8e75f47` |
| `BUY` | `8.75` | `1380.2000` | 12,072.06 USD | 5,361,651.54 USD | `STANDARD` | `-0.11%` | `0x57d8e75f47` |
| `BUY` | `8.75` | `1354.5800` | 11,849.32 USD | 5,601,909.89 USD | `STANDARD` | `-0.10%` | `0x08a49e7f71` |
| `BUY` | `8.75` | `1143.2500` | 9,999.89 USD | 5,722,652.23 USD | `STANDARD` | `-0.11%` | `0x7d0c59691f` |
| `BUY` | `8.75` | `1137.9700` | 9,954.28 USD | 5,762,545.94 USD | `STANDARD` | `-0.10%` | `0x621c555167` |
| `BUY` | `8.75` | `914.4100` | 7,999.99 USD | 5,861,474.20 USD | `STANDARD` | `-0.09%` | `0x7d0c59691f` |
| `BUY` | `8.75` | `685.7500` | 5,999.83 USD | 5,944,049.99 USD | `STANDARD` | `-0.08%` | `0x7d0c59691f` |
| `BUY` | `8.75` | `487.0100` | 4,260.46 USD | 6,013,060.42 USD | `STANDARD` | `-0.10%` | `0x71d0e11ebb` |
| `BUY` | `8.75` | `372.2400` | 3,255.57 USD | 6,094,762.46 USD | `STANDARD` | `-0.12%` | `0x2a72b57dea` |
| `BUY` | `8.75` | `361.0700` | 3,157.95 USD | 6,158,750.10 USD | `STANDARD` | `-0.12%` | `0x6ba889db7f` |
| `BUY` | `8.75` | `360.2900` | 3,153.37 USD | 6,161,903.47 USD | `STANDARD` | `-0.05%` | `0x6ba889db7f` |
| `BUY` | `8.75` | `360.4100` | 3,153.19 USD | 6,165,056.66 USD | `STANDARD` | `-0.09%` | `0x6ba889db7f` |
| `BUY` | `8.75` | `312.0500` | 2,728.97 USD | 6,188,127.49 USD | `STANDARD` | `-0.13%` | `0x7717a7a245` |
| `BUY` | `8.75` | `285.8100` | 2,499.92 USD | 6,203,793.19 USD | `STANDARD` | `-0.11%` | `0x0efb38a5fa` |
| `BUY` | `8.75` | `257.2200` | 2,249.95 USD | 6,215,459.75 USD | `STANDARD` | `-0.11%` | `0xa38f19c4cc` |
| `BUY` | `8.75` | `200.0000` | 1,749.24 USD | 6,275,228.90 USD | `STANDARD` | `-0.12%` | `0xfc27136e42` |
| `BUY` | `8.75` | `143.1000` | 1,252.64 USD | 6,287,510.66 USD | `STANDARD` | `-0.03%` | `0x727956612a` |
| `BUY` | `8.75` | `138.6300` | 1,213.12 USD | 6,288,723.78 USD | `STANDARD` | `-0.07%` | `0xecb63caa47` |
| `BUY` | `8.75` | `123.1500` | 1,077.40 USD | 6,302,591.05 USD | `STANDARD` | `-0.09%` | `0x2eddf3aa5c` |
| `BUY` | `8.75` | `122.6800` | 1,073.05 USD | 6,303,664.10 USD | `STANDARD` | `-0.11%` | `0x2eddf3aa5c` |
| `BUY` | `8.75` | `120.0800` | 1,050.76 USD | 6,306,818.01 USD | `STANDARD` | `-0.07%` | `0x7717a7a245` |
| `BUY` | `8.75` | `114.2900` | 999.93 USD | 6,311,857.24 USD | `STANDARD` | `-0.09%` | `0x0eecd62efb` |
| `BUY` | `8.75` | `85.6700` | 749.27 USD | 6,320,146.26 USD | `STANDARD` | `-0.12%` | `0x010461c14e` |
| `BUY` | `8.75` | `83.2300` | 727.93 USD | 6,325,306.15 USD | `STANDARD` | `-0.12%` | `0x31ca8395cf` |
| `BUY` | `8.75` | `80.5600` | 704.87 USD | 6,328,149.82 USD | `STANDARD` | `-0.08%` | `0x2eddf3aa5c` |
| `BUY` | `8.75` | `71.5600` | 626.19 USD | 6,336,095.00 USD | `STANDARD` | `-0.07%` | `0x2eddf3aa5c` |
| `BUY` | `8.75` | `67.2800` | 588.40 USD | 6,337,277.01 USD | `STANDARD` | `-0.13%` | `0x33ad48ed92` |
| `BUY` | `8.75` | `64.8300` | 567.21 USD | 6,337,844.22 USD | `STANDARD` | `-0.08%` | `0x023a3d0580` |
| `BUY` | `8.75` | `57.3100` | 501.49 USD | 6,340,910.32 USD | `STANDARD` | `-0.07%` | `0x57d8e75f47` |
| `BUY` | `8.75` | `57.3100` | 501.23 USD | 6,341,411.55 USD | `STANDARD` | `-0.12%` | `0x57d8e75f47` |
| `ASK` | `8.76` | `5.8000` | 50.81 USD | 27,113.49 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.76` | `76.8900` | 673.58 USD | 27,062.67 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `8.76` | `46.8200` | 410.13 USD | 26,389.10 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.76` | `221.9000` | 1,943.78 USD | 25,978.96 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.76` | `5.3400` | 46.78 USD | 24,035.18 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.76` | `21.0800` | 184.65 USD | 23,988.41 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.76` | `169.7900` | 1,487.24 USD | 23,803.76 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `8.76` | `46.8200` | 410.10 USD | 22,316.52 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.76` | `28.5600` | 250.16 USD | 21,906.42 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.76` | `46.8200` | 410.07 USD | 21,656.26 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.76` | `1598.6400` | 14,001.37 USD | 21,246.19 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `8.76` | `63.3000` | 554.38 USD | 7,244.82 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.76` | `152.4900` | 1,335.48 USD | 6,690.44 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.76` | `187.7000` | 1,643.82 USD | 5,354.96 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `8.76` | `26.2800` | 230.15 USD | 3,711.14 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.76` | `93.6400` | 820.01 USD | 3,480.99 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `8.76` | `52.5600` | 460.26 USD | 2,660.99 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `8.76` | `52.5600` | 460.26 USD | 2,200.72 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `8.76` | `52.5600` | 460.25 USD | 1,740.47 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `8.76` | `146.2000` | 1,280.21 USD | 1,280.21 USD | `4 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `8.76` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.76` | `0.00%` | `-` |
| `BID` | `8.76` | `16.0000` | 140.10 USD | 140.10 USD | `1 orders` | `-0.00%` | `-` |
| `SELL` | `8.76` | `1380.2000` | 12,096.21 USD | 5,313,332.26 USD | `STANDARD` | `+0.09%` | `0x57d8e75f47` |
| `SELL` | `8.76` | `1380.2000` | 12,092.76 USD | 5,325,425.02 USD | `STANDARD` | `+0.06%` | `0x57d8e75f47` |
| `SELL` | `8.76` | `1369.8500` | 12,000.16 USD | 5,542,211.39 USD | `STANDARD` | `+0.04%` | `0x7d0c59691f` |
| `SELL` | `8.76` | `1141.7900` | 10,000.14 USD | 5,712,652.34 USD | `STANDARD` | `+0.02%` | `0x7d0c59691f` |
| `SELL` | `8.76` | `1137.9700` | 9,972.71 USD | 5,752,591.66 USD | `STANDARD` | `+0.08%` | `0x621c555167` |
| `SELL` | `8.76` | `913.6300` | 8,000.57 USD | 5,853,474.21 USD | `STANDARD` | `+0.00%` | `0x7d0c59691f` |
| `SELL` | `8.76` | `685.3100` | 6,000.99 USD | 5,938,050.16 USD | `STANDARD` | `+0.00%` | `0x7d0c59691f` |
| `SELL` | `8.76` | `360.8000` | 3,161.22 USD | 6,155,592.15 USD | `STANDARD` | `+0.06%` | `0x6ba889db7f` |
| `SELL` | `8.76` | `285.2900` | 2,499.94 USD | 6,201,293.27 USD | `STANDARD` | `+0.07%` | `0x0efb38a5fa` |
| `SELL` | `8.76` | `215.8600` | 1,891.78 USD | 6,266,301.18 USD | `STANDARD` | `+0.08%` | `0x023a3d0580` |
| `SELL` | `8.76` | `200.0000` | 1,751.94 USD | 6,271,728.08 USD | `STANDARD` | `+0.04%` | `0xfc27136e42` |
| `SELL` | `8.76` | `200.0000` | 1,751.58 USD | 6,273,479.66 USD | `STANDARD` | `+0.02%` | `0xfc27136e42` |
| `SELL` | `8.76` | `152.4900` | 1,335.35 USD | 6,286,258.02 USD | `STANDARD` | `+0.01%` | `0x727956612a` |
| `SELL` | `8.76` | `137.5600` | 1,205.22 USD | 6,289,929.00 USD | `STANDARD` | `+0.06%` | `0xdd4f66125d` |
| `SELL` | `8.76` | `123.2700` | 1,080.28 USD | 6,301,513.65 USD | `STANDARD` | `+0.08%` | `0x2eddf3aa5c` |
| `SELL` | `8.76` | `120.0800` | 1,051.62 USD | 6,304,715.72 USD | `STANDARD` | `+0.01%` | `0x7717a7a245` |
| `SELL` | `8.76` | `120.0800` | 1,051.53 USD | 6,305,767.25 USD | `STANDARD` | `+0.00%` | `0x7717a7a245` |
| `SELL` | `8.76` | `118.6300` | 1,039.39 USD | 6,307,857.40 USD | `STANDARD` | `+0.06%` | `0x2eddf3aa5c` |
| `SELL` | `8.76` | `114.1000` | 999.98 USD | 6,308,857.39 USD | `STANDARD` | `+0.09%` | `0x27c9fa86c9` |
| `SELL` | `8.76` | `114.1600` | 999.96 USD | 6,309,857.35 USD | `STANDARD` | `+0.03%` | `0x0eecd62efb` |
| `SELL` | `8.76` | `92.4400` | 809.48 USD | 6,315,476.81 USD | `STANDARD` | `+0.00%` | `0xecb63caa47` |
| `SELL` | `8.76` | `91.7000` | 803.72 USD | 6,317,084.34 USD | `STANDARD` | `+0.09%` | `0xdd4f66125d` |
| `SELL` | `8.76` | `91.7000` | 803.70 USD | 6,317,888.04 USD | `STANDARD` | `+0.09%` | `0xdd4f66125d` |
| `SELL` | `8.76` | `81.3900` | 713.20 USD | 6,326,732.81 USD | `STANDARD` | `+0.07%` | `0x010461c14e` |
| `SELL` | `8.76` | `80.0400` | 701.20 USD | 6,329,552.77 USD | `STANDARD` | `+0.05%` | `0x2eddf3aa5c` |
| `SELL` | `8.76` | `74.6300` | 653.97 USD | 6,333,546.19 USD | `STANDARD` | `+0.07%` | `0x31ca8395cf` |
| `SELL` | `8.76` | `72.2300` | 632.87 USD | 6,335,468.81 USD | `STANDARD` | `+0.06%` | `0x2eddf3aa5c` |
| `SELL` | `8.76` | `63.3000` | 554.38 USD | 6,338,398.61 USD | `STANDARD` | `+0.02%` | `0x023a3d0580` |
| `SELL` | `8.76` | `57.3100` | 502.12 USD | 6,340,408.83 USD | `STANDARD` | `+0.06%` | `0x57d8e75f47` |
| `SELL` | `8.77` | `1380.2000` | 12,108.08 USD | 5,277,031.62 USD | `STANDARD` | `+0.18%` | `0x57d8e75f47` |
| `SELL` | `8.77` | `1380.2000` | 12,104.63 USD | 5,289,136.25 USD | `STANDARD` | `+0.16%` | `0x57d8e75f47` |
| `SELL` | `8.77` | `1380.2000` | 12,099.80 USD | 5,301,236.05 USD | `STANDARD` | `+0.12%` | `0x57d8e75f47` |
| `SELL` | `8.77` | `1351.2600` | 11,849.47 USD | 5,590,060.57 USD | `STANDARD` | `+0.14%` | `0x08a49e7f71` |
| `SELL` | `8.77` | `1259.9700` | 11,054.22 USD | 5,647,955.11 USD | `STANDARD` | `+0.19%` | `0xa38f19c4cc` |
| `SELL` | `8.77` | `1137.9700` | 9,978.40 USD | 5,742,618.94 USD | `STANDARD` | `+0.14%` | `0xaf9f722a67` |
| `SELL` | `8.77` | `741.6500` | 6,502.42 USD | 5,919,339.57 USD | `STANDARD` | `+0.13%` | `0xa38f19c4cc` |
| `SELL` | `8.77` | `571.6000` | 5,014.02 USD | 5,971,819.21 USD | `STANDARD` | `+0.18%` | `0x3ca146d269` |
| `SELL` | `8.77` | `487.4100` | 4,273.46 USD | 6,008,799.96 USD | `STANDARD` | `+0.13%` | `0x71d0e11ebb` |
| `SELL` | `8.77` | `481.6400` | 4,225.72 USD | 6,017,286.14 USD | `STANDARD` | `+0.19%` | `0x7717a7a245` |
| `SELL` | `8.77` | `445.5600` | 3,906.71 USD | 6,029,377.41 USD | `STANDARD` | `+0.13%` | `0xecb63caa47` |
| `SELL` | `8.77` | `436.2000` | 3,824.95 USD | 6,040,895.32 USD | `STANDARD` | `+0.14%` | `0xa38f19c4cc` |
| `SELL` | `8.77` | `372.2400` | 3,265.48 USD | 6,088,243.65 USD | `STANDARD` | `+0.18%` | `0x2a72b57dea` |
| `SELL` | `8.77` | `372.2400` | 3,263.24 USD | 6,091,506.89 USD | `STANDARD` | `+0.11%` | `0x2a72b57dea` |
| `SELL` | `8.77` | `366.8200` | 3,218.15 USD | 6,120,662.30 USD | `STANDARD` | `+0.19%` | `0xdd4f66125d` |
| `SELL` | `8.77` | `365.4900` | 3,203.74 USD | 6,123,866.04 USD | `STANDARD` | `+0.10%` | `0x6ba889db7f` |
| `SELL` | `8.77` | `361.7700` | 3,172.47 USD | 6,136,591.52 USD | `STANDARD` | `+0.15%` | `0x6ba889db7f` |
| `SELL` | `8.77` | `361.1700` | 3,168.26 USD | 6,149,268.24 USD | `STANDARD` | `+0.18%` | `0x6ba889db7f` |
| `SELL` | `8.77` | `312.0500` | 2,735.59 USD | 6,185,398.52 USD | `STANDARD` | `+0.11%` | `0x7717a7a245` |
| `SELL` | `8.77` | `303.7300` | 2,662.38 USD | 6,193,512.73 USD | `STANDARD` | `+0.10%` | `0xecb63caa47` |
| `SELL` | `8.77` | `301.7800` | 2,646.70 USD | 6,196,159.43 USD | `STANDARD` | `+0.16%` | `0xecb63caa47` |
| `SELL` | `8.77` | `270.8700` | 2,376.21 USD | 6,208,593.55 USD | `STANDARD` | `+0.18%` | `0x33ad48ed92` |
| `SELL` | `8.77` | `258.0900` | 2,264.43 USD | 6,213,209.79 USD | `STANDARD` | `+0.20%` | `0xecb63caa47` |
| `SELL` | `8.77` | `256.6900` | 2,249.91 USD | 6,217,709.66 USD | `STANDARD` | `+0.10%` | `0xa38f19c4cc` |
| `SELL` | `8.77` | `231.2300` | 2,028.88 USD | 6,238,221.39 USD | `STANDARD` | `+0.20%` | `0x9d732bed51` |
| `SELL` | `8.77` | `231.2300` | 2,028.03 USD | 6,240,249.41 USD | `STANDARD` | `+0.16%` | `0x9d732bed51` |
| `SELL` | `8.77` | `208.5000` | 1,828.29 USD | 6,269,976.14 USD | `STANDARD` | `+0.14%` | `0x26934acbd3` |
| `SELL` | `8.77` | `91.7000` | 803.81 USD | 6,316,280.62 USD | `STANDARD` | `+0.10%` | `0xdd4f66125d` |
| `SELL` | `8.77` | `83.9100` | 735.89 USD | 6,323,119.44 USD | `STANDARD` | `+0.15%` | `0x2eddf3aa5c` |
| `SELL` | `8.77` | `74.6900` | 655.30 USD | 6,332,892.22 USD | `STANDARD` | `+0.19%` | `0x31ca8395cf` |
| `SELL` | `8.77` | `73.9100` | 648.25 USD | 6,334,194.44 USD | `STANDARD` | `+0.16%` | `0x010461c14e` |
| `SELL` | `8.77` | `67.7200` | 593.61 USD | 6,336,688.62 USD | `STANDARD` | `+0.10%` | `0x33ad48ed92` |
| `SELL` | `8.77` | `57.3100` | 502.75 USD | 6,339,404.37 USD | `STANDARD` | `+0.18%` | `0x57d8e75f47` |
| `SELL` | `8.77` | `57.3100` | 502.35 USD | 6,339,906.72 USD | `STANDARD` | `+0.10%` | `0x57d8e75f47` |
| `SELL` | `8.78` | `16891.6900` | 148,241.47 USD | 3,023,484.09 USD | `LARGE (>= USD 100K)` | `+0.22%` | `0x71d0e11ebb` |
| `SELL` | `8.78` | `3434.8000` | 30,157.20 USD | 4,886,217.34 USD | `MEDIUM (>= USD 25K)` | `+0.27%` | `0x08a49e7f71` |
| `SELL` | `8.78` | `2139.3400` | 18,792.18 USD | 5,061,081.10 USD | `STANDARD` | `+0.31%` | `0xa38f19c4cc` |
| `SELL` | `8.78` | `1380.2000` | 12,119.81 USD | 5,240,695.64 USD | `STANDARD` | `+0.28%` | `0x57d8e75f47` |
| `SELL` | `8.78` | `1380.2000` | 12,116.22 USD | 5,252,811.87 USD | `STANDARD` | `+0.25%` | `0x57d8e75f47` |
| `SELL` | `8.78` | `1380.2000` | 12,111.67 USD | 5,264,923.54 USD | `STANDARD` | `+0.21%` | `0x57d8e75f47` |
| `SELL` | `8.78` | `1137.9700` | 9,988.30 USD | 5,732,640.54 USD | `STANDARD` | `+0.24%` | `0xaf9f722a67` |
| `SELL` | `8.78` | `961.3700` | 8,445.15 USD | 5,837,157.27 USD | `STANDARD` | `+0.32%` | `0xd3943e4008` |
| `SELL` | `8.78` | `877.1500` | 7,699.10 USD | 5,885,173.21 USD | `STANDARD` | `+0.24%` | `0xecb63caa47` |
| `SELL` | `8.78` | `709.1400` | 6,227.74 USD | 5,932,049.17 USD | `STANDARD` | `+0.29%` | `0xecb63caa47` |
| `SELL` | `8.78` | `569.2900` | 4,999.96 USD | 5,976,819.17 USD | `STANDARD` | `+0.30%` | `0x0efb38a5fa` |
| `SELL` | `8.78` | `420.0000` | 3,687.64 USD | 6,044,582.96 USD | `STANDARD` | `+0.27%` | `0xb7bd9cef0e` |
| `SELL` | `8.78` | `372.2400` | 3,268.56 USD | 6,084,978.17 USD | `STANDARD` | `+0.28%` | `0x2a72b57dea` |
| `SELL` | `8.78` | `366.8200` | 3,221.89 USD | 6,114,223.40 USD | `STANDARD` | `+0.31%` | `0xdd4f66125d` |
| `SELL` | `8.78` | `366.8200` | 3,220.75 USD | 6,117,444.15 USD | `STANDARD` | `+0.27%` | `0xdd4f66125d` |
| `SELL` | `8.78` | `361.0900` | 3,168.85 USD | 6,146,099.99 USD | `STANDARD` | `+0.22%` | `0x6ba889db7f` |
| `SELL` | `8.78` | `360.2800` | 3,162.68 USD | 6,152,430.93 USD | `STANDARD` | `+0.25%` | `0x6ba889db7f` |
| `SELL` | `8.78` | `231.2300` | 2,031.01 USD | 6,234,162.63 USD | `STANDARD` | `+0.31%` | `0x9d732bed51` |
| `SELL` | `8.78` | `231.2300` | 2,029.88 USD | 6,236,192.51 USD | `STANDARD` | `+0.25%` | `0x9d732bed51` |
| `SELL` | `8.78` | `84.8400` | 744.99 USD | 6,321,638.91 USD | `STANDARD` | `+0.28%` | `0x010461c14e` |
| `SELL` | `8.78` | `81.2500` | 713.46 USD | 6,326,019.61 USD | `STANDARD` | `+0.28%` | `0x31ca8395cf` |
| `SELL` | `8.78` | `57.3100` | 503.01 USD | 6,338,901.62 USD | `STANDARD` | `+0.23%` | `0x57d8e75f47` |
| `SELL` | `8.79` | `1380.2000` | 12,134.30 USD | 5,204,319.92 USD | `STANDARD` | `+0.40%` | `0x57d8e75f47` |
| `SELL` | `8.79` | `1380.2000` | 12,130.72 USD | 5,216,450.64 USD | `STANDARD` | `+0.37%` | `0x57d8e75f47` |
| `SELL` | `8.79` | `1380.2000` | 12,125.20 USD | 5,228,575.83 USD | `STANDARD` | `+0.33%` | `0x57d8e75f47` |
| `SELL` | `8.79` | `1109.1500` | 9,752.76 USD | 5,792,185.97 USD | `STANDARD` | `+0.42%` | `0xd3943e4008` |
| `SELL` | `8.79` | `1089.0100` | 9,567.50 USD | 5,801,753.47 USD | `STANDARD` | `+0.33%` | `0x26934acbd3` |
| `SELL` | `8.79` | `677.1700` | 5,952.05 USD | 5,950,002.04 USD | `STANDARD` | `+0.38%` | `0x33ad48ed92` |
| `SELL` | `8.79` | `629.5900` | 5,533.40 USD | 5,961,403.96 USD | `STANDARD` | `+0.37%` | `0xecb63caa47` |
| `SELL` | `8.79` | `506.8400` | 4,456.04 USD | 5,995,909.67 USD | `STANDARD` | `+0.40%` | `0xecb63caa47` |
| `SELL` | `8.79` | `372.2400` | 3,272.21 USD | 6,081,709.61 USD | `STANDARD` | `+0.39%` | `0x2a72b57dea` |
| `SELL` | `8.79` | `332.6900` | 2,923.21 USD | 6,174,278.41 USD | `STANDARD` | `+0.34%` | `0x26934acbd3` |
| `SELL` | `8.79` | `315.7300` | 2,776.85 USD | 6,182,662.94 USD | `STANDARD` | `+0.44%` | `0x07fd993f0f` |
| `SELL` | `8.79` | `231.2300` | 2,032.93 USD | 6,230,099.66 USD | `STANDARD` | `+0.40%` | `0x9d732bed51` |
| `SELL` | `8.79` | `231.2300` | 2,031.96 USD | 6,232,131.62 USD | `STANDARD` | `+0.35%` | `0x9d732bed51` |
| `SELL` | `8.79` | `229.0000` | 2,013.00 USD | 6,258,398.96 USD | `STANDARD` | `+0.39%` | `0x39bac00809` |
| `SELL` | `8.79` | `131.2700` | 1,153.69 USD | 6,297,005.36 USD | `STANDARD` | `+0.37%` | `0xe34d21d198` |
| `SELL` | `8.80` | `24054.6400` | 211,603.86 USD | 1,853,176.11 USD | `LARGE (>= USD 100K)` | `+0.46%` | `0x71cfa5e263` |
| `SELL` | `8.80` | `14947.3900` | 131,471.26 USD | 3,302,485.48 USD | `LARGE (>= USD 100K)` | `+0.45%` | `0x71d0e11ebb` |
| `SELL` | `8.80` | `1380.2000` | 12,147.97 USD | 5,180,044.55 USD | `STANDARD` | `+0.51%` | `0x57d8e75f47` |
| `SELL` | `8.80` | `1380.2000` | 12,141.07 USD | 5,192,185.62 USD | `STANDARD` | `+0.46%` | `0x57d8e75f47` |
| `SELL` | `8.80` | `908.9800` | 7,999.93 USD | 5,877,474.12 USD | `STANDARD` | `+0.51%` | `0x0efb38a5fa` |
| `SELL` | `8.80` | `492.5700` | 4,332.65 USD | 6,000,242.32 USD | `STANDARD` | `+0.45%` | `0xcd7f60e943` |
| `SELL` | `8.80` | `372.2400` | 3,275.30 USD | 6,078,437.39 USD | `STANDARD` | `+0.48%` | `0x2a72b57dea` |
| `SELL` | `8.80` | `231.2300` | 2,035.03 USD | 6,226,032.79 USD | `STANDARD` | `+0.51%` | `0x9d732bed51` |
| `SELL` | `8.80` | `231.2300` | 2,033.95 USD | 6,228,066.74 USD | `STANDARD` | `+0.45%` | `0x9d732bed51` |
| `SELL` | `8.80` | `84.9200` | 747.66 USD | 6,320,893.93 USD | `STANDARD` | `+0.55%` | `0x010461c14e` |
| `SELL` | `8.81` | `1219.3500` | 10,742.11 USD | 5,702,652.20 USD | `STANDARD` | `+0.61%` | `0xd3943e4008` |
| `SELL` | `8.81` | `830.0000` | 7,308.48 USD | 5,892,481.70 USD | `STANDARD` | `+0.56%` | `0xb7bd9cef0e` |
| `SELL` | `8.81` | `527.3800` | 4,643.79 USD | 5,991,453.63 USD | `STANDARD` | `+0.56%` | `0x26934acbd3` |
| `SELL` | `8.81` | `231.2300` | 2,037.11 USD | 6,221,961.66 USD | `STANDARD` | `+0.61%` | `0x9d732bed51` |
| `SELL` | `8.81` | `231.2300` | 2,036.10 USD | 6,223,997.76 USD | `STANDARD` | `+0.56%` | `0x9d732bed51` |
| `SELL` | `8.81` | `131.2700` | 1,156.50 USD | 6,295,851.67 USD | `STANDARD` | `+0.61%` | `0xe34d21d198` |
| `SELL` | `8.81` | `75.2500` | 662.68 USD | 6,331,578.34 USD | `STANDARD` | `+0.57%` | `0x31ca8395cf` |
| `SELL` | `8.82` | `17661.6200` | 155,812.58 USD | 2,569,029.67 USD | `LARGE (>= USD 100K)` | `+0.75%` | `0x71d0e11ebb` |
| `SELL` | `8.82` | `11353.3600` | 100,117.33 USD | 4,447,498.61 USD | `LARGE (>= USD 100K)` | `+0.71%` | `0x881cd92459` |
| `SELL` | `8.82` | `3158.1200` | 27,858.72 USD | 4,944,232.86 USD | `MEDIUM (>= USD 25K)` | `+0.74%` | `0x26934acbd3` |
| `SELL` | `8.82` | `1474.3600` | 13,006.36 USD | 5,155,055.28 USD | `STANDARD` | `+0.74%` | `0xd3943e4008` |
| `SELL` | `8.82` | `1359.8300` | 11,999.96 USD | 5,566,211.31 USD | `STANDARD` | `+0.78%` | `0x0efb38a5fa` |
| `SELL` | `8.82` | `1015.7500` | 8,954.04 USD | 5,819,781.05 USD | `STANDARD` | `+0.67%` | `0x33ad48ed92` |
| `SELL` | `8.83` | `11385.2400` | 100,556.72 USD | 4,247,263.56 USD | `LARGE (>= USD 100K)` | `+0.86%` | `0xecb63caa47` |
| `SELL` | `8.83` | `1250.0000` | 11,032.75 USD | 5,670,042.07 USD | `STANDARD` | `+0.80%` | `0xb7bd9cef0e` |
| `SELL` | `8.83` | `386.4900` | 3,412.36 USD | 6,055,079.39 USD | `STANDARD` | `+0.83%` | `0x14f8e04290` |
| `SELL` | `8.83` | `131.2700` | 1,159.46 USD | 6,294,695.17 USD | `STANDARD` | `+0.87%` | `0xe34d21d198` |
| `SELL` | `8.84` | `3614.5000` | 31,946.76 USD | 4,793,177.46 USD | `MEDIUM (>= USD 25K)` | `+0.94%` | `0xa38f19c4cc` |
| `SELL` | `8.84` | `85.9500` | 759.68 USD | 6,318,647.71 USD | `STANDARD` | `+0.94%` | `0x31ca8395cf` |
| `SELL` | `8.84` | `72.5800` | 641.50 USD | 6,334,835.94 USD | `STANDARD` | `+0.94%` | `0x010461c14e` |
| `SELL` | `8.85` | `47157.9800` | 417,348.12 USD | 1,232,962.50 USD | `LARGE (>= USD 100K)` | `+1.07%` | `0x71cfa5e263` |
| `SELL` | `8.85` | `13310.4700` | 117,795.00 USD | 3,802,168.15 USD | `LARGE (>= USD 100K)` | `+1.06%` | `0xecb63caa47` |
| `SELL` | `8.85` | `1337.4000` | 11,837.73 USD | 5,613,747.62 USD | `STANDARD` | `+1.08%` | `0x33ad48ed92` |
| `SELL` | `8.85` | `315.7300` | 2,794.84 USD | 6,179,886.09 USD | `STANDARD` | `+1.09%` | `0x07fd993f0f` |
| `SELL` | `8.86` | `17663.7700` | 156,451.54 USD | 2,413,217.10 USD | `LARGE (>= USD 100K)` | `+1.15%` | `0x71d0e11ebb` |
| `SELL` | `8.86` | `1805.0300` | 15,999.97 USD | 5,095,575.65 USD | `STANDARD` | `+1.23%` | `0x0efb38a5fa` |
| `SELL` | `8.87` | `13878.3500` | 123,070.43 USD | 3,684,373.15 USD | `LARGE (>= USD 100K)` | `+1.27%` | `0xecb63caa47` |
| `SELL` | `8.87` | `4687.9000` | 41,586.83 USD | 4,725,601.46 USD | `MEDIUM (>= USD 25K)` | `+1.31%` | `0xa24c5ca26c` |
| `SELL` | `8.87` | `383.1700` | 3,396.99 USD | 6,058,476.39 USD | `STANDARD` | `+1.24%` | `0x14f8e04290` |
| `SELL` | `8.88` | `1730.1000` | 15,354.98 USD | 5,126,930.57 USD | `STANDARD` | `+1.35%` | `0xd3943e4008` |
| `SELL` | `8.88` | `188.8300` | 1,676.02 USD | 6,278,606.38 USD | `STANDARD` | `+1.36%` | `0x31ca8395cf` |
| `SELL` | `8.88` | `172.7000` | 1,534.01 USD | 6,284,922.66 USD | `STANDARD` | `+1.44%` | `0x010461c14e` |
| `SELL` | `8.89` | `13183.0800` | 117,140.89 USD | 3,919,309.04 USD | `LARGE (>= USD 100K)` | `+1.47%` | `0xecb63caa47` |
| `SELL` | `8.89` | `12988.5300` | 115,418.68 USD | 4,034,727.72 USD | `LARGE (>= USD 100K)` | `+1.48%` | `0x71d0e11ebb` |
| `SELL` | `8.89` | `2137.1600` | 18,999.99 USD | 5,004,496.73 USD | `STANDARD` | `+1.53%` | `0x0efb38a5fa` |
| `SELL` | `8.90` | `91616.3300` | 815,614.38 USD | 815,614.38 USD | `LARGE (>= USD 100K)` | `+1.67%` | `0x71cfa5e263` |
| `SELL` | `8.90` | `2164.3400` | 19,263.92 USD | 4,985,496.74 USD | `STANDARD` | `+1.65%` | `0xd3943e4008` |
| `SELL` | `8.91` | `383.2200` | 3,415.79 USD | 6,051,667.04 USD | `STANDARD` | `+1.79%` | `0x14f8e04290` |
| `SELL` | `8.91` | `315.7300` | 2,812.84 USD | 6,177,091.25 USD | `STANDARD` | `+1.74%` | `0x07fd993f0f` |
| `SELL` | `8.91` | `182.0000` | 1,622.13 USD | 6,280,228.51 USD | `STANDARD` | `+1.78%` | `0x31ca8395cf` |
| `SELL` | `8.91` | `178.5700` | 1,591.61 USD | 6,281,820.12 USD | `STANDARD` | `+1.79%` | `0x010461c14e` |
| `SELL` | `8.91` | `109.3400` | 973.86 USD | 6,313,807.33 USD | `STANDARD` | `+1.71%` | `0xdadbb4b2a0` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:54:30 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1505` | `0x7737...bf66` | `SHORT` | 1,499,316.12 USD | `171,568.06` | `7.43` | `8.75` | `109.83` | -223,771.10 USD | `-14.92%` | `10X Cross` |
| `1587` | `0xeadc...9d55` | `LONG` | 1,399,048.71 USD | `160,070.56` | `8.11` | `8.75` | `0.000000` | 101,411.13 USD | `+7.25%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


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
| `Live` | `Long Liquidation` | `7.46` | 9,160.00 USD | 544,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 3,210.00 USD | 535,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,580.00 USD | 531,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,080.00 USD | 530,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.53` | 995.86 USD | 529,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 528,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 157.14 USD | 523,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 4,380.00 USD | 523,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.59` | 25,140.00 USD | 519,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 312.22 USD | 494,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 493,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.63` | 514.52 USD | 493,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 492,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.67` | 1,740.00 USD | 492,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.68` | 1,120.00 USD | 490,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.70` | 1,460.00 USD | 489,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.71` | 19,760.00 USD | 488,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.72` | 2,550.00 USD | 468,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 893.76 USD | 465,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 465,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.77` | 9,570,000.00 USD | 9,570,000.00 USD | 18,150.00 USD | 10,660.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.78` | 695.32 USD | 464,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,900.00 USD | 463,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.79` | 4,870,000.00 USD | 4,870,000.00 USD | 65,890.00 USD | 11,370.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.79` | 9,530,000.00 USD | 9,530,000.00 USD | 19,090.00 USD | 4,540.00 USD | 15,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 1,940.00 USD | 459,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.80` | 633.77 USD | 458,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.81` | 4,770,000.00 USD | 4,770,000.00 USD | 6,130.00 USD | 7,800.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.81` | 9,490,000.00 USD | 9,490,000.00 USD | 2,240.00 USD | 11,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.82` | 5,280.00 USD | 457,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.83` | 4,750,000.00 USD | 4,750,000.00 USD | 4,450.00 USD | 4,390.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.83` | 9,480,000.00 USD | 9,480,000.00 USD | 28,130.00 USD | 2,130.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 10,930.00 USD | 452,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.85` | 4,740,000.00 USD | 4,740,000.00 USD | 4,570.00 USD | 3,060.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.85` | 9,430,000.00 USD | 9,430,000.00 USD | 15,410.00 USD | 7,840.00 USD | 12,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.86` | 2,110.00 USD | 441,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.87` | 176.18 USD | 439,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.87` | 4,720,000.00 USD | 4,720,000.00 USD | 29,410.00 USD | 4,570.00 USD | 25,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.87` | 9,390,000.00 USD | 9,390,000.00 USD | 50,960.00 USD | 1,540.00 USD | 21,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 438,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.89` | 4,660,000.00 USD | 4,660,000.00 USD | 21,240.00 USD | 9,580.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.89` | 9,320,000.00 USD | 9,320,000.00 USD | 25,450.00 USD | 18,320.00 USD | 24,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 505.13 USD | 438,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 4,620,000.00 USD | 4,620,000.00 USD | 11,920.00 USD | 3,480.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.91` | 9,250,000.00 USD | 9,250,000.00 USD | 29,920.00 USD | 11,120.00 USD | 17,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.93` | 4,600,000.00 USD | 4,600,000.00 USD | 21,130.00 USD | 5,660.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.93` | 9,190,000.00 USD | 9,190,000.00 USD | 78,470.00 USD | 7,330.00 USD | 14,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 1,820.00 USD | 437,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 436,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 4,570,000.00 USD | 4,570,000.00 USD | 11,610.00 USD | 9,310.00 USD | 8,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.95` | 9,090,000.00 USD | 9,090,000.00 USD | 41,590.00 USD | 9,500.00 USD | 42,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 843.15 USD | 308,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.97` | 4,540,000.00 USD | 4,540,000.00 USD | 13,510.00 USD | 5,620.00 USD | 4,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.97` | 9,000,000.00 USD | 9,000,000.00 USD | 35,290.00 USD | 18,700.00 USD | 39,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,600.00 USD | 308,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 4,520,000.00 USD | 4,520,000.00 USD | 4,090.00 USD | 1,380.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.99` | 8,900,000.00 USD | 8,900,000.00 USD | 49,120.00 USD | 7,410.00 USD | 45,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 210.99 USD | 306,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.01` | 4,510,000.00 USD | 4,510,000.00 USD | 6,600.00 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.01` | 8,800,000.00 USD | 8,800,000.00 USD | 49,240.00 USD | 17,990.00 USD | 470.04 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 957.70 USD | 306,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 4,500,000.00 USD | 4,500,000.00 USD | 17,700.00 USD | 2,310.00 USD | 297.55 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.03` | 8,730,000.00 USD | 8,730,000.00 USD | 104,360.00 USD | 23,930.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 88,380.00 USD | 305,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.04` | 6,890.00 USD | 216,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.05` | 4,480,000.00 USD | 4,480,000.00 USD | 24,220.00 USD | 3,770.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.05` | 8,560,000.00 USD | 8,560,000.00 USD | 36,050.00 USD | 29,270.00 USD | 62,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.05` | 3,340.00 USD | 210,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.06` | 37,830.00 USD | 206,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 4,440,000.00 USD | 4,440,000.00 USD | 13,130.00 USD | 4,100.00 USD | 7,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.07` | 8,430,000.00 USD | 8,430,000.00 USD | 63,920.00 USD | 10,930.00 USD | 75,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 617.61 USD | 168,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.09` | 4,420,000.00 USD | 4,420,000.00 USD | 14,060.00 USD | 2,630.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.09` | 8,280,000.00 USD | 8,280,000.00 USD | 36,390.00 USD | 16,210.00 USD | 27,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.10` | 11,700.00 USD | 168,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.11` | 4,390,000.00 USD | 4,390,000.00 USD | 13,850.00 USD | 6,970.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.11` | 8,200,000.00 USD | 8,200,000.00 USD | 36,560.00 USD | 10,160.00 USD | 7,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 241.26 USD | 156,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.13` | 4,370,000.00 USD | 4,370,000.00 USD | 10,930.00 USD | 0.00 USD | 7,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.13` | 8,140,000.00 USD | 8,140,000.00 USD | 32,750.00 USD | 11,560.00 USD | 20,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 4,350,000.00 USD | 4,350,000.00 USD | 28,020.00 USD | 662.47 USD | 5,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.15` | 8,080,000.00 USD | 8,080,000.00 USD | 91,880.00 USD | 5,090.00 USD | 46,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.16` | 871.61 USD | 156,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.17` | 4,320,000.00 USD | 4,320,000.00 USD | 3,360.00 USD | 0.00 USD | 59.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.17` | 7,930,000.00 USD | 7,930,000.00 USD | 6,560.00 USD | 7,770.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.18` | 235.36 USD | 155,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.19` | 4,310,000.00 USD | 4,310,000.00 USD | 5,590.00 USD | 0.00 USD | 469.45 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.19` | 7,910,000.00 USD | 7,910,000.00 USD | 30,430.00 USD | 3,170.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.20` | 1,050.00 USD | 155,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.21` | 1,910.00 USD | 154,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.21` | 4,310,000.00 USD | 4,310,000.00 USD | 3,540.00 USD | 0.00 USD | 445.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.21` | 7,870,000.00 USD | 7,870,000.00 USD | 22,220.00 USD | 0.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 147.87 USD | 152,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.22` | 2,100.00 USD | 152,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.23` | 4,300,000.00 USD | 4,300,000.00 USD | 26,390.00 USD | 4,080.00 USD | 41,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.23` | 7,840,000.00 USD | 7,840,000.00 USD | 14,630.00 USD | 3,480.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.23` | 1,160.00 USD | 149,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.24` | 1,300.00 USD | 148,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.25` | 4,230,000.00 USD | 4,230,000.00 USD | 18,270.00 USD | 1,150.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.25` | 7,710,000.00 USD | 7,710,000.00 USD | 55,820.00 USD | 5,750.00 USD | 9,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.26` | 13,810.00 USD | 147,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.27` | 4,200,000.00 USD | 4,200,000.00 USD | 12,140.00 USD | 14,210.00 USD | 21.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.27` | 7,640,000.00 USD | 7,640,000.00 USD | 65,020.00 USD | 14,400.00 USD | 1,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.28` | 9,740.00 USD | 133,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.29` | 498.26 USD | 123,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.29` | 4,170,000.00 USD | 4,170,000.00 USD | 109,350.00 USD | 16,540.00 USD | 45,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.29` | 7,560,000.00 USD | 7,560,000.00 USD | 116,340.00 USD | 19,520.00 USD | 52,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 18,970.00 USD | 123,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.30` | 33,500.00 USD | 104,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.31` | 4,000,000.00 USD | 4,000,000.00 USD | 109,200.00 USD | 24,540.00 USD | 20,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.31` | 7,370,000.00 USD | 7,370,000.00 USD | 80,550.00 USD | 13,500.00 USD | 11,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.31` | 4,550.00 USD | 71,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.33` | 3,850,000.00 USD | 3,850,000.00 USD | 27,740.00 USD | 27,890.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.33` | 7,270,000.00 USD | 7,270,000.00 USD | 58,510.00 USD | 36,210.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.34` | 4,760.00 USD | 66,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.35` | 3,780,000.00 USD | 3,780,000.00 USD | 21,290.00 USD | 16,080.00 USD | 22,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.35` | 7,150,000.00 USD | 7,150,000.00 USD | 95,370.00 USD | 5,340.00 USD | 82,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.36` | 3,180.00 USD | 61,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.37` | 7,390.00 USD | 58,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.37` | 3,720,000.00 USD | 3,720,000.00 USD | 26,050.00 USD | 15,950.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.37` | 6,970,000.00 USD | 6,970,000.00 USD | 92,990.00 USD | 31,220.00 USD | 38,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.38` | 4,620.00 USD | 51,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.39` | 3,640,000.00 USD | 3,640,000.00 USD | 119,840.00 USD | 18,300.00 USD | 96,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.39` | 6,810,000.00 USD | 6,810,000.00 USD | 226,860.00 USD | 8,930.00 USD | 77,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.39` | 1,680.00 USD | 46,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.40` | 1,380.00 USD | 44,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.41` | 3,410,000.00 USD | 3,410,000.00 USD | 100,070.00 USD | 29,160.00 USD | 88,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.41` | 6,500,000.00 USD | 6,500,000.00 USD | 122,320.00 USD | 32,690.00 USD | 244,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.41` | 681.03 USD | 43,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.43` | 3,190,000.00 USD | 3,190,000.00 USD | 62,760.00 USD | 47,320.00 USD | 32,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.43` | 6,100,000.00 USD | 6,100,000.00 USD | 179,770.00 USD | 62,350.00 USD | 73,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.44` | 188.61 USD | 42,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 588.70 USD | 42,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.45` | 3,050,000.00 USD | 3,050,000.00 USD | 108,590.00 USD | 25,950.00 USD | 54,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.45` | 5,780,000.00 USD | 5,780,000.00 USD | 210,670.00 USD | 59,180.00 USD | 89,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.46` | 422.16 USD | 41,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.46` | 1,860.00 USD | 41,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.47` | 2,860,000.00 USD | 2,860,000.00 USD | 274,020.00 USD | 47,840.00 USD | 68,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.47` | 5,420,000.00 USD | 5,420,000.00 USD | 426,960.00 USD | 70,760.00 USD | 200,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.47` | 12,430.00 USD | 39,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.48` | 1,160.00 USD | 27,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.49` | 2,470,000.00 USD | 2,470,000.00 USD | 267,220.00 USD | 76,720.00 USD | 60,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.49` | 4,720,000.00 USD | 4,720,000.00 USD | 283,720.00 USD | 54,550.00 USD | 118,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.49` | 403.51 USD | 26,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.51` | 6,380.00 USD | 25,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.51` | 2,060,000.00 USD | 2,060,000.00 USD | 96,210.00 USD | 63,330.00 USD | 50,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.51` | 4,270,000.00 USD | 4,270,000.00 USD | 227,050.00 USD | 129,490.00 USD | 139,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.52` | 7,770.00 USD | 19,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.53` | 1,850,000.00 USD | 1,850,000.00 USD | 66,040.00 USD | 46,880.00 USD | 65,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.53` | 3,770,000.00 USD | 3,770,000.00 USD | 414,730.00 USD | 72,650.00 USD | 328,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 6,350.00 USD | 11,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.54` | 1,550.00 USD | 5,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.55` | 1,670,000.00 USD | 1,670,000.00 USD | 82,660.00 USD | 36,390.00 USD | 70,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.55` | 2,950,000.00 USD | 2,950,000.00 USD | 279,560.00 USD | 136,440.00 USD | 45,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.55` | 684.40 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.57` | 1,480,000.00 USD | 1,480,000.00 USD | 183,160.00 USD | 30,520.00 USD | 153,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.57` | 2,490,000.00 USD | 2,490,000.00 USD | 767,620.00 USD | 94,290.00 USD | 93,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.59` | 1,120,000.00 USD | 1,120,000.00 USD | 158,140.00 USD | 56,580.00 USD | 65,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.59` | 1,540,000.00 USD | 1,540,000.00 USD | 279,060.00 USD | 118,220.00 USD | 87,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.61` | 2,980.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.61` | 836,080.00 USD | 836,080.00 USD | 103,430.00 USD | 36,000.00 USD | 55,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.61` | 1,050,000.00 USD | 1,050,000.00 USD | 88,710.00 USD | 35,810.00 USD | 229,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.63` | 641,340.00 USD | 641,340.00 USD | 180,480.00 USD | 44,210.00 USD | 42,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.63` | 698,910.00 USD | 698,910.00 USD | 51,260.00 USD | 25,450.00 USD | 23,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.65` | 373,680.00 USD | 373,680.00 USD | 156,430.00 USD | 43,300.00 USD | 52,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.65` | 598,360.00 USD | 598,360.00 USD | 163,720.00 USD | 16,520.00 USD | 57,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.67` | 121,760.00 USD | 121,760.00 USD | 0.00 USD | 0.00 USD | 42,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.67` | 360,310.00 USD | 360,310.00 USD | 77,920.00 USD | 24,870.00 USD | 173,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.69` | 79,330.00 USD | 79,330.00 USD | 0.00 USD | 0.00 USD | 26,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.69` | 83,610.00 USD | 83,610.00 USD | 70,550.00 USD | 12,790.00 USD | 270.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.71` | 52,630.00 USD | 52,630.00 USD | 52,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.75` | 67,910.00 USD | 67,910.00 USD | 32,080.00 USD | 0.00 USD | 35,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.75` | 135,820.00 USD | 135,820.00 USD | 32,080.00 USD | 0.00 USD | 35,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.75` | 19,690.00 USD | 19,690.00 USD | 0.00 USD | 19,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.75` | 39,370.00 USD | 39,370.00 USD | 0.00 USD | 19,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.77` | 294,360.00 USD | 294,360.00 USD | 132,830.00 USD | 0.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.77` | 120,610.00 USD | 120,610.00 USD | 0.00 USD | 0.00 USD | 81,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.79` | 348,480.00 USD | 348,480.00 USD | 32,240.00 USD | 12,000.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.79` | 173,270.00 USD | 173,270.00 USD | 27,360.00 USD | 25,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.81` | 354,180.00 USD | 354,180.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.81` | 181,720.00 USD | 181,720.00 USD | 0.00 USD | 8,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 432,100.00 USD | 432,100.00 USD | 10,770.00 USD | 2,250.00 USD | 64,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.89` | 450,570.00 USD | 450,570.00 USD | 0.00 USD | 11,100.00 USD | 7,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.89` | 254,770.00 USD | 254,770.00 USD | 0.00 USD | 0.00 USD | 73,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.91` | 588,840.00 USD | 588,840.00 USD | 40,950.00 USD | 7,360.00 USD | 89,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.91` | 401,370.00 USD | 401,370.00 USD | 57,910.00 USD | 0.00 USD | 88,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 600,410.00 USD | 600,410.00 USD | 8,060.00 USD | 0.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.95` | 605,710.00 USD | 605,710.00 USD | 0.00 USD | 5,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 692,760.00 USD | 692,760.00 USD | 40,450.00 USD | 36,070.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.99` | 495,610.00 USD | 495,610.00 USD | 94,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 757,920.00 USD | 757,920.00 USD | 38,030.00 USD | 5,120.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.01` | 737,830.00 USD | 737,830.00 USD | 185,270.00 USD | 36,180.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 963,300.00 USD | 963,300.00 USD | 106,640.00 USD | 66,510.00 USD | 32,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.03` | 912,880.00 USD | 912,880.00 USD | 58,760.00 USD | 101,140.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 1,070,000.00 USD | 1,070,000.00 USD | 22,480.00 USD | 37,250.00 USD | 49,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.05` | 1,010,000.00 USD | 1,010,000.00 USD | 35,720.00 USD | 17,700.00 USD | 39,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 1,200,000.00 USD | 1,200,000.00 USD | 41,700.00 USD | 30,110.00 USD | 52,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.07` | 1,060,000.00 USD | 1,060,000.00 USD | 3,990.00 USD | 14,140.00 USD | 36,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 1,430,000.00 USD | 1,430,000.00 USD | 121,690.00 USD | 27,290.00 USD | 81,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.09` | 1,390,000.00 USD | 1,390,000.00 USD | 179,590.00 USD | 8,680.00 USD | 143,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 1,640,000.00 USD | 1,640,000.00 USD | 118,620.00 USD | 34,700.00 USD | 55,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.11` | 2,820,000.00 USD | 2,820,000.00 USD | 847,950.00 USD | 37,620.00 USD | 546,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 1,930,000.00 USD | 1,930,000.00 USD | 190,770.00 USD | 51,740.00 USD | 46,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.13` | 4,030,000.00 USD | 4,030,000.00 USD | 690,230.00 USD | 26,540.00 USD | 484,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.13` | 314.34 USD | 314.34 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.15` | 2,100,000.00 USD | 2,100,000.00 USD | 92,380.00 USD | 30,600.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.15` | 4,670,000.00 USD | 4,670,000.00 USD | 357,020.00 USD | 38,700.00 USD | 249,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 2,390,000.00 USD | 2,390,000.00 USD | 170,750.00 USD | 37,660.00 USD | 80,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.17` | 5,500,000.00 USD | 5,500,000.00 USD | 408,450.00 USD | 133,490.00 USD | 285,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 2,700,000.00 USD | 2,700,000.00 USD | 178,200.00 USD | 76,590.00 USD | 58,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.19` | 6,300,000.00 USD | 6,300,000.00 USD | 503,250.00 USD | 101,150.00 USD | 193,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 2,900,000.00 USD | 2,900,000.00 USD | 121,150.00 USD | 15,610.00 USD | 66,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.21` | 7,260,000.00 USD | 7,260,000.00 USD | 554,780.00 USD | 132,850.00 USD | 277,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.21` | 3,810.00 USD | 4,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.23` | 3,090,000.00 USD | 3,090,000.00 USD | 134,640.00 USD | 13,360.00 USD | 39,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.23` | 8,280,000.00 USD | 8,280,000.00 USD | 562,300.00 USD | 88,460.00 USD | 371,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 3,160,000.00 USD | 3,160,000.00 USD | 49,760.00 USD | 8,330.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.25` | 8,770,000.00 USD | 8,770,000.00 USD | 277,290.00 USD | 73,690.00 USD | 141,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 3,200,000.00 USD | 3,200,000.00 USD | 39,300.00 USD | 4,490.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.27` | 9,100,000.00 USD | 9,100,000.00 USD | 156,190.00 USD | 118,550.00 USD | 54,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 100.93 USD | 4,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.29` | 3,270,000.00 USD | 3,270,000.00 USD | 37,140.00 USD | 8,000.00 USD | 17,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.29` | 9,960,000.00 USD | 9,960,000.00 USD | 468,150.00 USD | 100,200.00 USD | 290,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 3,360,000.00 USD | 3,360,000.00 USD | 70,040.00 USD | 13,670.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.31` | 10,600,000.00 USD | 10,600,000.00 USD | 307,520.00 USD | 55,090.00 USD | 275,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 3,400,000.00 USD | 3,400,000.00 USD | 16,620.00 USD | 8,530.00 USD | 15,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.33` | 10,970,000.00 USD | 10,970,000.00 USD | 124,660.00 USD | 64,710.00 USD | 179,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.35` | 3,930.00 USD | 8,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.35` | 3,490,000.00 USD | 3,490,000.00 USD | 44,830.00 USD | 8,000.00 USD | 33,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.35` | 11,440,000.00 USD | 11,440,000.00 USD | 289,480.00 USD | 88,340.00 USD | 96,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 3,600,000.00 USD | 3,600,000.00 USD | 67,060.00 USD | 24,480.00 USD | 19,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.37` | 11,920,000.00 USD | 11,920,000.00 USD | 369,360.00 USD | 34,660.00 USD | 70,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.38` | 404,120.00 USD | 412,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.39` | 3,670,000.00 USD | 3,670,000.00 USD | 38,740.00 USD | 4,040.00 USD | 25,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.39` | 12,270,000.00 USD | 12,270,000.00 USD | 206,980.00 USD | 57,260.00 USD | 87,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 3,750,000.00 USD | 3,750,000.00 USD | 65,590.00 USD | 2,860.00 USD | 13,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.41` | 12,730,000.00 USD | 12,730,000.00 USD | 265,320.00 USD | 41,500.00 USD | 147,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 2,470.00 USD | 414,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.43` | 3,790,000.00 USD | 3,790,000.00 USD | 20,770.00 USD | 2,260.00 USD | 16,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.43` | 12,970,000.00 USD | 12,970,000.00 USD | 101,970.00 USD | 43,920.00 USD | 95,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 3,800,000.00 USD | 3,800,000.00 USD | 1,540.00 USD | 0.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.45` | 13,100,000.00 USD | 13,100,000.00 USD | 105,560.00 USD | 16,970.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.47` | 3,800,000.00 USD | 3,800,000.00 USD | 2,610.00 USD | 5,690.00 USD | 192.20 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.47` | 13,210,000.00 USD | 13,210,000.00 USD | 53,420.00 USD | 27,650.00 USD | 25,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 3,840,000.00 USD | 3,840,000.00 USD | 22,170.00 USD | 572.85 USD | 10,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.49` | 13,290,000.00 USD | 13,290,000.00 USD | 26,920.00 USD | 36,710.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.49` | 428.79 USD | 415,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.51` | 3,850,000.00 USD | 3,850,000.00 USD | 12,280.00 USD | 3,160.00 USD | 124.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.51` | 13,580,000.00 USD | 13,580,000.00 USD | 131,270.00 USD | 43,360.00 USD | 122,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.53` | 3,900,000.00 USD | 3,900,000.00 USD | 35,960.00 USD | 7,630.00 USD | 5,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.53` | 13,790,000.00 USD | 13,790,000.00 USD | 187,750.00 USD | 15,360.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.55` | 3,920,000.00 USD | 3,920,000.00 USD | 8,810.00 USD | 7,800.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.55` | 13,840,000.00 USD | 13,840,000.00 USD | 28,850.00 USD | 17,400.00 USD | 880.26 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.57` | 3,940,000.00 USD | 3,940,000.00 USD | 6,420.00 USD | 4,390.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.57` | 14,000,000.00 USD | 14,000,000.00 USD | 114,070.00 USD | 14,280.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.59` | 3,960,000.00 USD | 3,960,000.00 USD | 5,940.00 USD | 3,060.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.59` | 14,070,000.00 USD | 14,070,000.00 USD | 26,920.00 USD | 13,200.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.61` | 4,020,000.00 USD | 4,020,000.00 USD | 29,640.00 USD | 4,570.00 USD | 25,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.61` | 14,210,000.00 USD | 14,210,000.00 USD | 93,670.00 USD | 13,850.00 USD | 29,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.63` | 4,040,000.00 USD | 4,040,000.00 USD | 11,160.00 USD | 4,370.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.63` | 14,260,000.00 USD | 14,260,000.00 USD | 42,830.00 USD | 4,500.00 USD | 6,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.65` | 4,060,000.00 USD | 4,060,000.00 USD | 11,480.00 USD | 5,210.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.65` | 14,330,000.00 USD | 14,330,000.00 USD | 33,020.00 USD | 20,230.00 USD | 18,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.67` | 4,080,000.00 USD | 4,080,000.00 USD | 11,920.00 USD | 3,480.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.67` | 14,410,000.00 USD | 14,410,000.00 USD | 31,000.00 USD | 24,380.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.69` | 4,110,000.00 USD | 4,110,000.00 USD | 21,130.00 USD | 5,660.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.69` | 14,580,000.00 USD | 14,580,000.00 USD | 121,550.00 USD | 17,380.00 USD | 33,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.71` | 4,140,000.00 USD | 4,140,000.00 USD | 11,610.00 USD | 9,310.00 USD | 8,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.71` | 14,720,000.00 USD | 14,720,000.00 USD | 92,070.00 USD | 9,500.00 USD | 42,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.73` | 4,150,000.00 USD | 4,150,000.00 USD | 2,760.00 USD | 3,700.00 USD | 13.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.73` | 14,740,000.00 USD | 14,740,000.00 USD | 3,060.00 USD | 3,160.00 USD | 11,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 415,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.75` | 4,170,000.00 USD | 4,170,000.00 USD | 10,750.00 USD | 1,920.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.75` | 14,820,000.00 USD | 14,820,000.00 USD | 35,970.00 USD | 15,540.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.76` | 549.11 USD | 415,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.77` | 4,180,000.00 USD | 4,180,000.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.77` | 14,930,000.00 USD | 14,930,000.00 USD | 51,320.00 USD | 7,410.00 USD | 46,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.78` | 470.18 USD | 416,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.79` | 4,190,000.00 USD | 4,190,000.00 USD | 5,640.00 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.79` | 15,000,000.00 USD | 15,000,000.00 USD | 48,830.00 USD | 17,990.00 USD | 729.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.80` | 4,190,000.00 USD | 4,190,000.00 USD | 6,680.00 USD | 770.83 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.81` | 15,170,000.00 USD | 15,170,000.00 USD | 103,830.00 USD | 23,930.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.83` | 15,300,000.00 USD | 15,300,000.00 USD | 31,840.00 USD | 29,270.00 USD | 62,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.85` | 15,400,000.00 USD | 15,400,000.00 USD | 50,490.00 USD | 2,210.00 USD | 49,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.87` | 15,450,000.00 USD | 15,450,000.00 USD | 15,580.00 USD | 8,710.00 USD | 25,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.89` | 15,530,000.00 USD | 15,530,000.00 USD | 33,970.00 USD | 16,210.00 USD | 27,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.91` | 15,580,000.00 USD | 15,580,000.00 USD | 32,670.00 USD | 10,160.00 USD | 7,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.93` | 15,640,000.00 USD | 15,640,000.00 USD | 31,960.00 USD | 11,560.00 USD | 20,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.95` | 15,730,000.00 USD | 15,730,000.00 USD | 55,780.00 USD | 3,730.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.97` | 15,780,000.00 USD | 15,780,000.00 USD | 29,800.00 USD | 1,360.00 USD | 21,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.99` | 15,800,000.00 USD | 15,800,000.00 USD | 840.10 USD | 7,770.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.01` | 15,810,000.00 USD | 15,810,000.00 USD | 15,620.00 USD | 3,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.03` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD | `Tier 1 CEX` |
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
| `7D` | `7.77` | 9,560,000.00 USD | 0.00 USD | 9,560,000.00 USD | 18,150.00 USD | 10,660.00 USD | 4,850.00 USD |
| `1D` | `7.79` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 65,480.00 USD | 11,370.00 USD | 16,150.00 USD |
| `7D` | `7.79` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 19,090.00 USD | 4,540.00 USD | 15,300.00 USD |
| `1D` | `7.81` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 5,220.00 USD | 7,800.00 USD | 6,020.00 USD |
| `7D` | `7.81` | 9,490,000.00 USD | 0.00 USD | 9,490,000.00 USD | 2,240.00 USD | 11,570.00 USD | 54.78 USD |
| `1D` | `7.83` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 4,630.00 USD | 4,390.00 USD | 7,390.00 USD |
| `7D` | `7.83` | 9,480,000.00 USD | 0.00 USD | 9,480,000.00 USD | 28,130.00 USD | 2,130.00 USD | 24,010.00 USD |
| `1D` | `7.85` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 4,860.00 USD | 3,060.00 USD | 10,340.00 USD |
| `7D` | `7.85` | 9,420,000.00 USD | 0.00 USD | 9,420,000.00 USD | 15,410.00 USD | 7,840.00 USD | 12,220.00 USD |
| `1D` | `7.87` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 29,470.00 USD | 4,570.00 USD | 28,070.00 USD |
| `7D` | `7.87` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 39,380.00 USD | 1,540.00 USD | 21,020.00 USD |
| `1D` | `7.89` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 27,740.00 USD | 9,580.00 USD | 9,770.00 USD |
| `7D` | `7.89` | 9,320,000.00 USD | 0.00 USD | 9,320,000.00 USD | 37,110.00 USD | 18,320.00 USD | 24,630.00 USD |
| `1D` | `7.91` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 11,710.00 USD | 3,480.00 USD | 7,980.00 USD |
| `7D` | `7.91` | 9,240,000.00 USD | 0.00 USD | 9,240,000.00 USD | 29,920.00 USD | 11,120.00 USD | 16,810.00 USD |
| `1D` | `7.93` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 21,210.00 USD | 5,660.00 USD | 3,970.00 USD |
| `7D` | `7.93` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 78,470.00 USD | 7,330.00 USD | 15,150.00 USD |
| `1D` | `7.95` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 11,360.00 USD | 9,310.00 USD | 8,590.00 USD |
| `7D` | `7.95` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 41,590.00 USD | 9,500.00 USD | 42,700.00 USD |
| `1D` | `7.97` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 13,450.00 USD | 5,620.00 USD | 4,050.00 USD |
| `7D` | `7.97` | 8,990,000.00 USD | 0.00 USD | 8,990,000.00 USD | 35,290.00 USD | 18,700.00 USD | 39,910.00 USD |
| `1D` | `7.99` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 4,460.00 USD | 1,380.00 USD | 4,440.00 USD |
| `7D` | `7.99` | 8,900,000.00 USD | 0.00 USD | 8,900,000.00 USD | 49,120.00 USD | 7,410.00 USD | 45,790.00 USD |
| `1D` | `8.01` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 9,360.00 USD | 1,840.00 USD | 1,790.00 USD |
| `7D` | `8.01` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 49,240.00 USD | 17,990.00 USD | 1,250.00 USD |
| `1D` | `8.03` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 16,800.00 USD | 2,310.00 USD | 297.55 USD |
| `7D` | `8.03` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 104,360.00 USD | 23,930.00 USD | 47,690.00 USD |
| `1D` | `8.05` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 25,050.00 USD | 3,770.00 USD | 6,520.00 USD |
| `7D` | `8.05` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 36,050.00 USD | 29,270.00 USD | 62,300.00 USD |
| `1D` | `8.07` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 11,060.00 USD | 4,100.00 USD | 7,410.00 USD |
| `7D` | `8.07` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 63,920.00 USD | 10,930.00 USD | 75,620.00 USD |
| `1D` | `8.09` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 13,660.00 USD | 2,630.00 USD | 7,810.00 USD |
| `7D` | `8.09` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 36,390.00 USD | 16,210.00 USD | 27,720.00 USD |
| `1D` | `8.11` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 13,300.00 USD | 6,970.00 USD | 4,610.00 USD |
| `7D` | `8.11` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 36,560.00 USD | 10,160.00 USD | 7,800.00 USD |
| `1D` | `8.13` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 10,710.00 USD | 0.00 USD | 7,260.00 USD |
| `7D` | `8.13` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 32,750.00 USD | 11,560.00 USD | 21,220.00 USD |
| `1D` | `8.15` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 31,100.00 USD | 662.47 USD | 5,150.00 USD |
| `7D` | `8.15` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 91,880.00 USD | 5,090.00 USD | 46,150.00 USD |
| `1D` | `8.17` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 2,150.00 USD | 0.00 USD | 59.50 USD |
| `7D` | `8.17` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 6,560.00 USD | 7,770.00 USD | 10,020.00 USD |
| `1D` | `8.19` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 4,000.00 USD | 0.00 USD | 469.45 USD |
| `7D` | `8.19` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 30,430.00 USD | 3,170.00 USD | 3,440.00 USD |
| `1D` | `8.21` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 5,670.00 USD | 0.00 USD | 445.22 USD |
| `7D` | `8.21` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 22,220.00 USD | 0.00 USD | 8,330.00 USD |
| `1D` | `8.23` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 24,920.00 USD | 4,080.00 USD | 41,050.00 USD |
| `7D` | `8.23` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 14,630.00 USD | 3,480.00 USD | 108,910.00 USD |
| `1D` | `8.25` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 16,120.00 USD | 1,150.00 USD | 9,610.00 USD |
| `7D` | `8.25` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 55,820.00 USD | 5,750.00 USD | 9,210.00 USD |
| `1D` | `8.27` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 12,930.00 USD | 14,210.00 USD | 21.52 USD |
| `7D` | `8.27` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 65,020.00 USD | 14,400.00 USD | 2,500.00 USD |
| `1D` | `8.29` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 110,170.00 USD | 16,540.00 USD | 45,430.00 USD |
| `7D` | `8.29` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 116,340.00 USD | 19,520.00 USD | 52,160.00 USD |
| `1D` | `8.31` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 109,460.00 USD | 24,540.00 USD | 20,740.00 USD |
| `7D` | `8.31` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 80,250.00 USD | 13,500.00 USD | 10,710.00 USD |
| `1D` | `8.33` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 27,800.00 USD | 27,890.00 USD | 17,260.00 USD |
| `7D` | `8.33` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 58,510.00 USD | 33,340.00 USD | 20,150.00 USD |
| `1D` | `8.35` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 21,480.00 USD | 16,080.00 USD | 22,350.00 USD |
| `7D` | `8.35` | 7,150,000.00 USD | 0.00 USD | 7,150,000.00 USD | 95,370.00 USD | 5,340.00 USD | 81,280.00 USD |
| `1D` | `8.37` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 25,290.00 USD | 15,950.00 USD | 33,810.00 USD |
| `7D` | `8.37` | 6,970,000.00 USD | 0.00 USD | 6,970,000.00 USD | 92,990.00 USD | 31,220.00 USD | 38,420.00 USD |
| `1D` | `8.39` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 118,930.00 USD | 18,300.00 USD | 103,200.00 USD |
| `7D` | `8.39` | 6,810,000.00 USD | 0.00 USD | 6,810,000.00 USD | 197,900.00 USD | 8,930.00 USD | 78,310.00 USD |
| `1D` | `8.41` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 116,500.00 USD | 32,640.00 USD | 97,670.00 USD |
| `7D` | `8.41` | 6,520,000.00 USD | 0.00 USD | 6,520,000.00 USD | 151,490.00 USD | 32,690.00 USD | 245,330.00 USD |
| `1D` | `8.43` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 62,580.00 USD | 47,320.00 USD | 32,810.00 USD |
| `7D` | `8.43` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 179,770.00 USD | 62,350.00 USD | 72,590.00 USD |
| `1D` | `8.45` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 108,590.00 USD | 25,950.00 USD | 54,950.00 USD |
| `7D` | `8.45` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 210,670.00 USD | 59,180.00 USD | 89,470.00 USD |
| `1D` | `8.47` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 274,530.00 USD | 47,840.00 USD | 68,540.00 USD |
| `7D` | `8.47` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 426,960.00 USD | 70,760.00 USD | 201,020.00 USD |
| `1D` | `8.49` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 269,970.00 USD | 76,720.00 USD | 60,910.00 USD |
| `7D` | `8.49` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 283,720.00 USD | 54,550.00 USD | 117,970.00 USD |
| `1D` | `8.51` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 93,450.00 USD | 63,330.00 USD | 50,250.00 USD |
| `7D` | `8.51` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 227,050.00 USD | 129,490.00 USD | 139,250.00 USD |
| `1D` | `8.53` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 64,420.00 USD | 46,880.00 USD | 65,220.00 USD |
| `7D` | `8.53` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 414,730.00 USD | 72,650.00 USD | 328,820.00 USD |
| `1D` | `8.55` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 83,770.00 USD | 36,390.00 USD | 70,150.00 USD |
| `7D` | `8.55` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 279,560.00 USD | 136,440.00 USD | 45,630.00 USD |
| `1D` | `8.57` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 181,870.00 USD | 30,520.00 USD | 167,010.00 USD |
| `7D` | `8.57` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 709,710.00 USD | 94,290.00 USD | 93,710.00 USD |
| `1D` | `8.59` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 189,970.00 USD | 63,530.00 USD | 82,790.00 USD |
| `7D` | `8.59` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 337,380.00 USD | 118,220.00 USD | 87,470.00 USD |
| `1D` | `8.61` | 836,080.00 USD | 0.00 USD | 836,080.00 USD | 103,430.00 USD | 36,000.00 USD | 55,320.00 USD |
| `7D` | `8.61` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 88,710.00 USD | 35,810.00 USD | 228,930.00 USD |
| `1D` | `8.63` | 641,340.00 USD | 0.00 USD | 641,340.00 USD | 180,480.00 USD | 44,210.00 USD | 42,960.00 USD |
| `7D` | `8.63` | 697,040.00 USD | 0.00 USD | 697,040.00 USD | 51,260.00 USD | 25,450.00 USD | 24,090.00 USD |
| `1D` | `8.65` | 373,680.00 USD | 0.00 USD | 373,680.00 USD | 156,430.00 USD | 43,300.00 USD | 52,200.00 USD |
| `7D` | `8.65` | 596,240.00 USD | 0.00 USD | 596,240.00 USD | 163,720.00 USD | 16,520.00 USD | 57,270.00 USD |
| `1D` | `8.67` | 121,760.00 USD | 0.00 USD | 121,760.00 USD | 0.00 USD | 0.00 USD | 42,430.00 USD |
| `7D` | `8.67` | 358,730.00 USD | 0.00 USD | 358,730.00 USD | 77,920.00 USD | 24,870.00 USD | 172,600.00 USD |
| `1D` | `8.69` | 79,330.00 USD | 0.00 USD | 79,330.00 USD | 0.00 USD | 0.00 USD | 26,700.00 USD |
| `7D` | `8.69` | 83,340.00 USD | 0.00 USD | 83,340.00 USD | 70,550.00 USD | 12,790.00 USD | 0.00 USD |
| `1D` | `8.71` | 52,630.00 USD | 0.00 USD | 52,630.00 USD | 52,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.74` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.75` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.75` | 19,690.00 USD | 19,690.00 USD | 0.00 USD | 0.00 USD | 19,690.00 USD | 0.00 USD |
| `1D` | `8.77` | 158,550.00 USD | 158,550.00 USD | 0.00 USD | 132,830.00 USD | 0.00 USD | 25,720.00 USD |
| `7D` | `8.77` | 101,000.00 USD | 101,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 81,310.00 USD |
| `1D` | `8.79` | 212,670.00 USD | 212,670.00 USD | 0.00 USD | 32,240.00 USD | 12,000.00 USD | 9,880.00 USD |
| `7D` | `8.79` | 153,650.00 USD | 153,650.00 USD | 0.00 USD | 27,360.00 USD | 25,300.00 USD | 0.00 USD |
| `1D` | `8.81` | 218,360.00 USD | 218,360.00 USD | 0.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD |
| `7D` | `8.81` | 162,100.00 USD | 162,100.00 USD | 0.00 USD | 0.00 USD | 8,450.00 USD | 0.00 USD |
| `1D` | `8.85` | 296,290.00 USD | 296,290.00 USD | 0.00 USD | 10,770.00 USD | 2,250.00 USD | 64,900.00 USD |
| `1D` | `8.89` | 314,760.00 USD | 314,760.00 USD | 0.00 USD | 0.00 USD | 11,100.00 USD | 7,370.00 USD |
| `7D` | `8.89` | 235,160.00 USD | 235,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 73,050.00 USD |
| `1D` | `8.91` | 466,550.00 USD | 466,550.00 USD | 0.00 USD | 40,950.00 USD | 7,360.00 USD | 103,480.00 USD |
| `7D` | `8.91` | 323,770.00 USD | 323,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 88,620.00 USD |
| `1D` | `8.93` | 527,440.00 USD | 527,440.00 USD | 0.00 USD | 39,890.00 USD | 0.00 USD | 21,000.00 USD |
| `7D` | `8.93` | 382,100.00 USD | 382,100.00 USD | 0.00 USD | 58,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.95` | 539,700.00 USD | 539,700.00 USD | 0.00 USD | 0.00 USD | 12,260.00 USD | 0.00 USD |
| `1D` | `8.99` | 626,100.00 USD | 626,100.00 USD | 0.00 USD | 39,810.00 USD | 36,070.00 USD | 10,530.00 USD |
| `7D` | `8.99` | 476,340.00 USD | 476,340.00 USD | 0.00 USD | 94,240.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.01` | 693,910.00 USD | 693,910.00 USD | 0.00 USD | 40,680.00 USD | 5,120.00 USD | 22,000.00 USD |
| `7D` | `9.01` | 718,560.00 USD | 718,560.00 USD | 0.00 USD | 185,270.00 USD | 36,180.00 USD | 20,780.00 USD |
| `1D` | `9.03` | 897,860.00 USD | 897,860.00 USD | 0.00 USD | 105,200.00 USD | 66,510.00 USD | 32,240.00 USD |
| `7D` | `9.03` | 893,610.00 USD | 893,610.00 USD | 0.00 USD | 58,760.00 USD | 101,140.00 USD | 15,140.00 USD |
| `1D` | `9.05` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 21,580.00 USD | 37,250.00 USD | 49,400.00 USD |
| `7D` | `9.05` | 985,810.00 USD | 985,810.00 USD | 0.00 USD | 35,720.00 USD | 17,700.00 USD | 38,790.00 USD |
| `1D` | `9.07` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 43,770.00 USD | 30,110.00 USD | 52,770.00 USD |
| `7D` | `9.07` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 3,990.00 USD | 14,140.00 USD | 36,530.00 USD |
| `1D` | `9.09` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 120,330.00 USD | 27,290.00 USD | 88,210.00 USD |
| `7D` | `9.09` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 150,640.00 USD | 8,680.00 USD | 144,110.00 USD |
| `1D` | `9.11` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 132,730.00 USD | 38,180.00 USD | 64,530.00 USD |
| `7D` | `9.11` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 877,120.00 USD | 37,620.00 USD | 546,100.00 USD |
| `1D` | `9.13` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 191,440.00 USD | 51,740.00 USD | 46,370.00 USD |
| `7D` | `9.13` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 690,230.00 USD | 26,540.00 USD | 484,570.00 USD |
| `1D` | `9.15` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 94,350.00 USD | 30,600.00 USD | 49,860.00 USD |
| `7D` | `9.15` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 357,020.00 USD | 38,700.00 USD | 249,300.00 USD |
| `1D` | `9.17` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 172,070.00 USD | 37,660.00 USD | 80,240.00 USD |
| `7D` | `9.17` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 408,450.00 USD | 133,490.00 USD | 284,660.00 USD |
| `1D` | `9.19` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 176,910.00 USD | 76,590.00 USD | 58,200.00 USD |
| `7D` | `9.19` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 503,250.00 USD | 101,150.00 USD | 193,350.00 USD |
| `1D` | `9.21` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 122,640.00 USD | 15,610.00 USD | 66,720.00 USD |
| `7D` | `9.21` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 554,780.00 USD | 132,850.00 USD | 277,090.00 USD |
| `1D` | `9.23` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 132,180.00 USD | 13,360.00 USD | 39,000.00 USD |
| `7D` | `9.23` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 562,300.00 USD | 88,460.00 USD | 371,150.00 USD |
| `1D` | `9.25` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 50,400.00 USD | 8,330.00 USD | 9,510.00 USD |
| `7D` | `9.25` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 277,290.00 USD | 73,690.00 USD | 141,190.00 USD |
| `1D` | `9.27` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 37,430.00 USD | 4,490.00 USD | 2,610.00 USD |
| `7D` | `9.27` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 156,190.00 USD | 118,550.00 USD | 55,270.00 USD |
| `1D` | `9.29` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 36,860.00 USD | 8,000.00 USD | 17,960.00 USD |
| `7D` | `9.29` | 9,940,000.00 USD | 9,940,000.00 USD | 0.00 USD | 468,150.00 USD | 100,200.00 USD | 291,150.00 USD |
| `1D` | `9.31` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 71,130.00 USD | 13,670.00 USD | 12,890.00 USD |
| `7D` | `9.31` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 307,520.00 USD | 55,090.00 USD | 275,010.00 USD |
| `1D` | `9.33` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 16,940.00 USD | 8,530.00 USD | 15,420.00 USD |
| `7D` | `9.33` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 124,660.00 USD | 64,710.00 USD | 179,140.00 USD |
| `1D` | `9.35` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 44,970.00 USD | 8,000.00 USD | 33,470.00 USD |
| `7D` | `9.35` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 289,480.00 USD | 88,340.00 USD | 98,320.00 USD |
| `1D` | `9.37` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 66,970.00 USD | 24,480.00 USD | 19,020.00 USD |
| `7D` | `9.37` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 369,360.00 USD | 34,660.00 USD | 69,490.00 USD |
| `1D` | `9.39` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 41,550.00 USD | 4,040.00 USD | 25,180.00 USD |
| `7D` | `9.39` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 206,980.00 USD | 57,260.00 USD | 85,810.00 USD |
| `1D` | `9.41` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 62,730.00 USD | 2,860.00 USD | 13,990.00 USD |
| `7D` | `9.41` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 265,320.00 USD | 41,500.00 USD | 147,930.00 USD |
| `1D` | `9.43` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 20,670.00 USD | 2,260.00 USD | 16,420.00 USD |
| `7D` | `9.43` | 12,930,000.00 USD | 12,930,000.00 USD | 0.00 USD | 101,970.00 USD | 29,590.00 USD | 95,930.00 USD |
| `1D` | `9.45` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | 2,430.00 USD |
| `7D` | `9.45` | 13,070,000.00 USD | 13,070,000.00 USD | 0.00 USD | 105,560.00 USD | 16,970.00 USD | 11,190.00 USD |
| `1D` | `9.47` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 1,720.00 USD | 5,690.00 USD | 192.20 USD |
| `7D` | `9.47` | 13,170,000.00 USD | 13,170,000.00 USD | 0.00 USD | 53,420.00 USD | 27,650.00 USD | 25,420.00 USD |
| `1D` | `9.49` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 21,720.00 USD | 572.85 USD | 10,750.00 USD |
| `7D` | `9.49` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 26,920.00 USD | 36,710.00 USD | 15,730.00 USD |
| `1D` | `9.51` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 12,440.00 USD | 3,160.00 USD | 124.70 USD |
| `7D` | `9.51` | 13,550,000.00 USD | 13,550,000.00 USD | 0.00 USD | 131,270.00 USD | 43,360.00 USD | 122,690.00 USD |
| `1D` | `9.53` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 34,450.00 USD | 7,630.00 USD | 5,400.00 USD |
| `7D` | `9.53` | 13,760,000.00 USD | 13,760,000.00 USD | 0.00 USD | 187,750.00 USD | 15,360.00 USD | 6,960.00 USD |
| `1D` | `9.55` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 9,250.00 USD | 7,800.00 USD | 6,030.00 USD |
| `7D` | `9.55` | 13,810,000.00 USD | 13,810,000.00 USD | 0.00 USD | 28,850.00 USD | 17,400.00 USD | 398.17 USD |
| `1D` | `9.57` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 5,330.00 USD | 4,390.00 USD | 7,390.00 USD |
| `7D` | `9.57` | 13,970,000.00 USD | 13,970,000.00 USD | 0.00 USD | 114,070.00 USD | 14,280.00 USD | 33,860.00 USD |
| `1D` | `9.59` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 6,120.00 USD | 3,060.00 USD | 10,340.00 USD |
| `7D` | `9.59` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 26,920.00 USD | 13,200.00 USD | 29,220.00 USD |
| `1D` | `9.61` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 30,490.00 USD | 4,570.00 USD | 28,070.00 USD |
| `7D` | `9.61` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 82,080.00 USD | 6,680.00 USD | 28,720.00 USD |
| `1D` | `9.63` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 16,910.00 USD | 4,370.00 USD | 4,650.00 USD |
| `7D` | `9.63` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 54,490.00 USD | 4,500.00 USD | 7,110.00 USD |
| `1D` | `9.65` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 11,260.00 USD | 5,210.00 USD | 5,130.00 USD |
| `7D` | `9.65` | 14,290,000.00 USD | 14,290,000.00 USD | 0.00 USD | 33,020.00 USD | 20,230.00 USD | 18,580.00 USD |
| `1D` | `9.67` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 11,710.00 USD | 3,480.00 USD | 8,060.00 USD |
| `7D` | `9.67` | 14,360,000.00 USD | 14,360,000.00 USD | 0.00 USD | 31,000.00 USD | 24,380.00 USD | 17,110.00 USD |
| `1D` | `9.69` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 21,210.00 USD | 5,660.00 USD | 3,970.00 USD |
| `7D` | `9.69` | 14,540,000.00 USD | 14,540,000.00 USD | 0.00 USD | 120,650.00 USD | 17,380.00 USD | 34,490.00 USD |
| `1D` | `9.71` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 11,360.00 USD | 9,310.00 USD | 8,590.00 USD |
| `7D` | `9.71` | 14,680,000.00 USD | 14,680,000.00 USD | 0.00 USD | 92,070.00 USD | 9,500.00 USD | 43,100.00 USD |
| `1D` | `9.73` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 2,640.00 USD | 3,700.00 USD | 13.70 USD |
| `7D` | `9.73` | 14,700,000.00 USD | 14,700,000.00 USD | 0.00 USD | 3,060.00 USD | 3,160.00 USD | 11,680.00 USD |
| `1D` | `9.75` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 10,810.00 USD | 1,920.00 USD | 4,040.00 USD |
| `7D` | `9.75` | 14,780,000.00 USD | 14,780,000.00 USD | 0.00 USD | 35,970.00 USD | 15,540.00 USD | 29,960.00 USD |
| `1D` | `9.77` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 3,890.00 USD | 1,380.00 USD | 4,440.00 USD |
| `7D` | `9.77` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 51,320.00 USD | 7,410.00 USD | 45,920.00 USD |
| `1D` | `9.78` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,790.00 USD |
| `7D` | `9.79` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 48,830.00 USD | 17,990.00 USD | 1,510.00 USD |
| `7D` | `9.81` | 15,130,000.00 USD | 15,130,000.00 USD | 0.00 USD | 103,830.00 USD | 23,930.00 USD | 47,810.00 USD |
| `7D` | `9.83` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 31,840.00 USD | 29,270.00 USD | 62,300.00 USD |
| `7D` | `9.85` | 15,360,000.00 USD | 15,360,000.00 USD | 0.00 USD | 49,820.00 USD | 2,210.00 USD | 49,870.00 USD |
| `7D` | `9.87` | 15,410,000.00 USD | 15,410,000.00 USD | 0.00 USD | 15,580.00 USD | 8,710.00 USD | 25,960.00 USD |
| `7D` | `9.89` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 33,970.00 USD | 16,210.00 USD | 27,580.00 USD |
| `7D` | `9.91` | 15,530,000.00 USD | 15,530,000.00 USD | 0.00 USD | 32,670.00 USD | 10,160.00 USD | 7,780.00 USD |
| `7D` | `9.93` | 15,600,000.00 USD | 15,600,000.00 USD | 0.00 USD | 31,960.00 USD | 11,560.00 USD | 20,680.00 USD |
| `7D` | `9.95` | 15,680,000.00 USD | 15,680,000.00 USD | 0.00 USD | 55,780.00 USD | 3,730.00 USD | 24,700.00 USD |
| `7D` | `9.97` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 29,800.00 USD | 1,360.00 USD | 21,690.00 USD |
| `7D` | `9.99` | 15,750,000.00 USD | 15,750,000.00 USD | 0.00 USD | 840.10 USD | 7,770.00 USD | 8,400.00 USD |
| `7D` | `10.01` | 15,770,000.00 USD | 15,770,000.00 USD | 0.00 USD | 15,620.00 USD | 3,170.00 USD | 184.07 USD |
| `7D` | `10.03` | 15,780,000.00 USD | 15,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `375.34M` | Total OI Tokens: `42,881,220.7 AVAX`
  * 1h OI Change: `-1.58%` | 4h OI Change: `-2.73%` | 24h OI Change: `-4.94%`
  * Exchange Breakdown: Binance=`88.08M` | Bybit=`58.83M` | OKX=`12.53M` | Hyperliquid=`17.37M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `10.90K` | Last 24h: `33.77K` | Last 3d: `72.05K` | Last 7d: `92.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0028%` | **USDT KuCoin** | `0.0086%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0038%` | **USDT Bitget** | `0.0083%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `56.71%` | `43.29%` | `1.31` | 11,010,000.00 USD |
| `15M` | `Binance` | `66.25%` | `33.75%` | `1.96` | 3,010,000.00 USD |
| `15M` | `OKX` | `80.48%` | `19.52%` | `4.12` | 806,860.00 USD |
| `15M` | `Bybit` | `61.47%` | `38.53%` | `1.60` | 921,860.00 USD |
| `15M` | `KuCoin` | `49.67%` | `50.33%` | `0.99` | 97,120.00 USD |
| `15M` | `Gate` | `54.38%` | `45.62%` | `1.19` | 90,560.00 USD |
| `15M` | `Bitget` | `73.2%` | `26.8%` | `2.73` | 328,360.00 USD |
| `15M` | `BingX` | `50.02%` | `49.98%` | `1.00` | 315,340.00 USD |
| `15M` | `MEXC` | `50.3%` | `49.7%` | `1.01` | 3,900,000.00 USD |
| `15M` | `Bitunix` | `30.68%` | `69.32%` | `0.44` | 313,730.00 USD |
| `15M` | `Hyperliquid` | `42.52%` | `57.48%` | `0.74` | 226,510.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `38.88%` | `61.12%` | `0.64` | 568,350.00 USD |
| `15M` | `Crypto.com` | `99.21%` | `0.79%` | `125.58` | 0.00 USD |
| `15M` | `WhiteBIT` | `4.85%` | `95.15%` | `0.05` | 209,680.00 USD |
| `15M` | `HTX` | `86.53%` | `13.47%` | `6.42` | 1,170.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `77.13%` | `22.87%` | `3.37` | 58,150.00 USD |
| `15M` | `Aster` | `75.69%` | `24.31%` | `3.11` | 164,200.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `89.31%` | `10.69%` | `8.35` | 1,630.00 USD |
| `15M` | `Whale Positions` | `66.25%` | `33.75%` | `1.96` | 3,010,000.00 USD |
| `15M` | `Global Accounts` | `56.71%` | `43.29%` | `1.31` | 11,010,000.00 USD |
| `1H` | `AVAX` | `45.62%` | `54.38%` | `0.84` | 26,240,000.00 USD |
| `1H` | `Binance` | `52.27%` | `47.73%` | `1.10` | 9,120,000.00 USD |
| `1H` | `OKX` | `60.87%` | `39.13%` | `1.56` | 1,900,000.00 USD |
| `1H` | `Bybit` | `42.79%` | `57.21%` | `0.75` | 1,920,000.00 USD |
| `1H` | `KuCoin` | `44.26%` | `55.74%` | `0.79` | 153,230.00 USD |
| `1H` | `Gate` | `44.72%` | `55.28%` | `0.81` | 631,530.00 USD |
| `1H` | `Bitget` | `50.52%` | `49.48%` | `1.02` | 459,310.00 USD |
| `1H` | `BingX` | `41.21%` | `58.79%` | `0.70` | 3,790,000.00 USD |
| `1H` | `MEXC` | `40.74%` | `59.26%` | `0.69` | 1,360,000.00 USD |
| `1H` | `Bitunix` | `40.42%` | `59.58%` | `0.68` | 753,960.00 USD |
| `1H` | `Hyperliquid` | `44.88%` | `55.12%` | `0.81` | 405,350.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `44.82%` | `55.18%` | `0.81` | 4,260,000.00 USD |
| `1H` | `Crypto.com` | `85.15%` | `14.85%` | `5.73` | 7,020.00 USD |
| `1H` | `WhiteBIT` | `0.8%` | `99.2%` | `0.01` | 1,240,000.00 USD |
| `1H` | `HTX` | `73.95%` | `26.05%` | `2.84` | 10,760.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `60.76%` | `39.24%` | `1.55` | 119,860.00 USD |
| `1H` | `Aster` | `45.87%` | `54.13%` | `0.85` | 41,480.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `24.48%` | `75.52%` | `0.32` | 75,900.00 USD |
| `1H` | `Whale Positions` | `52.27%` | `47.73%` | `1.10` | 9,120,000.00 USD |
| `1H` | `Global Accounts` | `45.62%` | `54.38%` | `0.84` | 26,240,000.00 USD |
| `4H` | `AVAX` | `43.30%` | `56.70%` | `0.76` | 107,770,000.00 USD |
| `4H` | `Binance` | `45.64%` | `54.36%` | `0.84` | 29,920,000.00 USD |
| `4H` | `OKX` | `47.56%` | `52.44%` | `0.91` | 10,250,000.00 USD |
| `4H` | `Bybit` | `46.38%` | `53.62%` | `0.86` | 8,600,000.00 USD |
| `4H` | `KuCoin` | `46%` | `54%` | `0.85` | 791,700.00 USD |
| `4H` | `Gate` | `48.83%` | `51.17%` | `0.95` | 1,320,000.00 USD |
| `4H` | `Bitget` | `41.39%` | `58.61%` | `0.71` | 3,280,000.00 USD |
| `4H` | `BingX` | `44.88%` | `55.12%` | `0.81` | 3,680,000.00 USD |
| `4H` | `MEXC` | `50.93%` | `49.07%` | `1.04` | 37,030,000.00 USD |
| `4H` | `Bitunix` | `45.89%` | `54.11%` | `0.85` | 3,540,000.00 USD |
| `4H` | `Hyperliquid` | `37.75%` | `62.25%` | `0.61` | 2,680,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.1%` | `51.9%` | `0.93` | 2,570,000.00 USD |
| `4H` | `Crypto.com` | `81.05%` | `18.95%` | `4.28` | 0.00 USD |
| `4H` | `WhiteBIT` | `0.2%` | `99.8%` | `0.00` | 2,780,000.00 USD |
| `4H` | `HTX` | `60.3%` | `39.7%` | `1.52` | 43,470.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `55.39%` | `44.61%` | `1.24` | 691,510.00 USD |
| `4H` | `Aster` | `44.37%` | `55.63%` | `0.80` | 469,670.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `33.02%` | `66.98%` | `0.49` | 143,790.00 USD |
| `4H` | `Whale Positions` | `45.64%` | `54.36%` | `0.84` | 29,920,000.00 USD |
| `4H` | `Global Accounts` | `43.30%` | `56.70%` | `0.76` | 107,770,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `8.87` | `8.87` | `8.87` | `8.88` | `8.86` | 651,856.32 USD | 369,195.26 USD | 282,661.06 USD | 86,534.20 USD | `+13.28%` | `5B / 4S` |
| `5:00 UTC` | `8.84` | `8.86` | `8.84` | `8.89` | `8.84` | 682,076.12 USD | 288,770.26 USD | 393,305.86 USD | -104,535.61 USD | `-15.33%` | `9B / 13S` |
| `0:00 UTC` | `8.81` | `8.81` | `8.81` | `8.84` | `8.80` | 1,762,248.06 USD | 773,632.57 USD | 988,615.48 USD | -214,982.91 USD | `-12.20%` | `7B / 6S` |
| `5:00 UTC` | `8.84` | `8.83` | `8.84` | `8.86` | `8.79` | 750,878.19 USD | 458,225.53 USD | 292,652.66 USD | 165,572.87 USD | `+22.05%` | `19B / 3S` |
| `0:00 UTC` | `8.82` | `8.82` | `8.82` | `8.84` | `8.80` | 637,816.13 USD | 328,825.06 USD | 308,991.07 USD | 19,833.99 USD | `+3.11%` | `4B / 4S` |
| `5:00 UTC` | `8.81` | `8.82` | `8.81` | `8.84` | `8.80` | 548,929.60 USD | 300,754.28 USD | 248,175.32 USD | 52,578.96 USD | `+9.58%` | `18B / 4S` |
| `0:00 UTC` | `8.86` | `8.86` | `8.86` | `8.87` | `8.83` | 587,148.06 USD | 393,702.30 USD | 193,445.76 USD | 200,256.54 USD | `+34.11%` | `5B / 1S` |
| `5:00 UTC` | `8.85` | `8.85` | `8.85` | `8.87` | `8.84` | 431,773.06 USD | 190,520.19 USD | 241,252.88 USD | -50,732.69 USD | `-11.75%` | `8B / 6S` |
| `0:00 UTC` | `8.73` | `8.73` | `8.73` | `8.86` | `8.66` | 5,568,654.06 USD | 2,589,240.15 USD | 2,979,413.92 USD | -390,173.77 USD | `-7.01%` | `5B / 25S` |
| `5:00 UTC` | `8.77` | `8.76` | `8.77` | `8.78` | `8.73` | 1,496,370.02 USD | 1,124,892.94 USD | 371,477.08 USD | 753,415.87 USD | `+50.35%` | `22B / 3S` |

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
| `5m` | -24,970.00 USD | 435,570.00 USD | **`ACCUMULATION`** |
| `15m` | 85,730.00 USD | 1,480,000.00 USD | **`ACCUMULATION`** |
| `30m` | -70,510.00 USD | 282,070.00 USD | **`ACCUMULATION`** |
| `1h` | -162,630.00 USD | 731,770.00 USD | **`ACCUMULATION`** |
| `2h` | -110,760.00 USD | 766,580.00 USD | **`ACCUMULATION`** |
| `4h` | -464,480.00 USD | -2,590,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 36,810.00 USD | -2,630,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -148,200.00 USD | -2,230,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -309,200.00 USD | -2,450,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,840.00 USD | -5,390,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,990,000.00 USD | -41,770,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -53,780,000.00 USD | -272,550,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-24.97K` | 15m=`+85.73K` | 1h=`-162.63K` | 24h=`-8.84K`
* Futures Capital Netflows: 5m=`+435.57K` | 15m=`+1.48M` | 1h=`+731.77K` | 24h=`-5.39M`
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
  * `2026-10-30 01:36:09 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:09 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:51:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `8.46` (Risk Distance: `0.1169` pts)
  * +2.5R Take Profit: `8.87`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.90` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `9.02` (Risk Distance: `0.1169` pts)
  * +2.5R Take Profit: `8.61`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.83`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
