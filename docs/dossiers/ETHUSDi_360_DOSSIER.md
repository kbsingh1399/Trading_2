# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 02:36:43 IST` (`2026-10-29 21:06:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2252.70` | **Live Ask Quote**: `2256.20` | **Mid Price**: `2254.45`
- **Spread Points**: `350.00` | **Spread BPS**: `15.52 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `0.01 USD` | Point Value (0.01 Lot): `0.0001 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `2321.71` | VWAP Z-Score: `-3.55` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `16.70` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `18.45` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2382.54` | Lower -3.00σ Band: `2260.88`
  * Upper +2.51σ Band: `2372.60` | Lower -2.51σ Band: `2270.82`
  * Upper +2.01σ Band: `2362.47` | Lower -2.01σ Band: `2280.96`
  * Upper +2.00σ Band: `2362.26` | Lower -2.00σ Band: `2281.16`
  * Upper +1.28σ Band: `2347.66` | Lower -1.28σ Band: `2295.76`
  * Upper +1.00σ Band: `2341.99` | Lower -1.00σ Band: `2301.43`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2309.73` | EMA-20=`2322.89` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2327.43` (Slope: `+0.0000`) | EMA-100=`2329.28`
  * Institutional Anchors: EMA-144=`2329.74` | EMA-200=`2329.17` (Slope: `-0.0512`) | EMA-233=`2329.15`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2234.80` | Weekly High=`2387.80` | Weekly Low=`2234.80`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2339.52` (Distance: `-3.64%`)
  * Point of Control (POC) = `2321.58` (Distance: `-2.89%`)
  * Value Area Low (VAL) = `2296.66` (Distance: `-1.84%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2367.21` | POC=`2350.17` | VAL=`2335.02`
  * Prior Day Extremes: PDH=`2387.80` | PDL=`2316.80` | PDC=`2356.60`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2340.70` | Weekly POC=`2310.39` | Weekly VAL=`2299.56`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2367.70` | Low=`2288.80`
  * London Session (08:00-16:00 UTC): High=`2331.00` | Low=`2299.00`
  * New York Session (13:00-21:00 UTC): High=`2374.90` | Low=`2307.50`
  * Initial Balance (First Hour): IB High=`2331.00` | IB Low=`2299.30`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2245.43` - `2263.47`
  * Optimal Trade Entry (OTE 0.705): `2258.96`
  * Structural Invalidation Anchor (0.786): `2272.49`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2263.86` | `2264.43` | `2255.20` | `2256.63` | `51,751` | 116,977,732.08 USD | -16,046,748.94 USD | `-13.72%` | -808,756,921.07 USD | `+0.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `2256.63` | `2265.97` | `2245.02` | `2249.49` | `126,353` | 284,807,641.19 USD | -32,664,021.25 USD | `-11.47%` | -841,420,942.32 USD | `-0.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `2249.49` | `2250.40` | `2246.04` | `2250.04` | `5,456` | 12,267,650.78 USD | 871,392.82 USD | `+7.10%` | -840,549,549.50 USD | `+0.53` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `2316.30` | `2319.33` | `2238.27` | `2254.25` | `730,735` | 1,664,912,417.71 USD | -298,389,298.86 USD | `-17.92%` | -728,695,930.32 USD | `-4.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2254.29` | `2277.10` | `2230.20` | `2256.63` | `375,405` | 846,756,637.45 USD | -79,128,177.15 USD | `-9.34%` | -807,824,107.47 USD | `-0.68` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2256.63` | `2265.97` | `2245.02` | `2249.40` | `131,145` | 295,581,668.13 USD | -31,848,260.96 USD | `-10.77%` | -839,672,368.43 USD | `+0.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2330.22` | `2338.58` | `2325.76` | `2335.68` | `63,571` | 148,285,696.23 USD | -15,505,202.15 USD | `-10.46%` | -370,400,580.93 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2335.68` | `2335.92` | `2230.20` | `2256.63` | `1,357,980` | 3,094,453,113.46 USD | -457,917,547.62 USD | `-14.80%` | -828,318,128.55 USD | `-3.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2256.63` | `2265.97` | `2245.02` | `2250.04` | `131,809` | 297,075,291.97 USD | -31,792,628.43 USD | `-10.70%` | -860,110,756.98 USD | `+0.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2250.04` | `1,489,789` | 3,391,528,405.43 USD | -489,710,176.05 USD | `-14.44%` | -855,477,698.06 USD | `-1.87` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2308.03` | `2334.83` | `2303.75` | `2309.10` | `525,175` | 1,216,920,375.04 USD | -34,916,746.14 USD | `-2.87%` | -218,489,329.59 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -267,651,577.31 USD | `+0.60` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2250.04` | `1,489,789` | 3,391,528,405.43 USD | -489,710,176.05 USD | `-14.44%` | -855,477,698.06 USD | `-1.87` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2254.45`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2248.20` | `94.0118` | 211,357.33 USD | 2,488,060.06 USD | `5 orders` | `-0.11%` | `-` |
| `BID` | `2248.30` | `78.6980` | 176,936.71 USD | 2,276,702.74 USD | `4 orders` | `-0.10%` | `-` |
| `BID` | `2248.40` | `102.4762` | 230,407.49 USD | 2,099,766.02 USD | `8 orders` | `-0.10%` | `-` |
| `BID` | `2248.50` | `86.9613` | 195,532.48 USD | 1,869,358.53 USD | `3 orders` | `-0.10%` | `-` |
| `BID` | `2248.60` | `354.8825` | 797,988.79 USD | 1,673,826.05 USD | `9 orders` | `-0.09%` | `-` |
| `BID` | `2248.70` | `12.0195` | 27,028.25 USD | 875,837.26 USD | `3 orders` | `-0.09%` | `-` |
| `BID` | `2248.80` | `340.3205` | 765,312.74 USD | 848,809.01 USD | `8 orders` | `-0.08%` | `-` |
| `BID` | `2248.90` | `1.1292` | 2,539.46 USD | 83,496.27 USD | `3 orders` | `-0.08%` | `-` |
| `BID` | `2249.00` | `2.6190` | 5,890.13 USD | 80,956.81 USD | `3 orders` | `-0.07%` | `-` |
| `BID` | `2249.20` | `4.8958` | 11,011.63 USD | 75,066.68 USD | `5 orders` | `-0.06%` | `-` |
| `BID` | `2249.30` | `0.2230` | 501.59 USD | 64,055.05 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `2249.40` | `0.3273` | 736.23 USD | 63,553.45 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `2249.50` | `18.9619` | 42,654.79 USD | 62,817.23 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `2249.60` | `0.4442` | 999.27 USD | 20,162.43 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `2249.70` | `0.3342` | 751.85 USD | 19,163.16 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `2249.80` | `0.0053` | 11.92 USD | 18,411.31 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `2250.00` | `0.0072` | 16.20 USD | 18,399.39 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `2250.30` | `7.9458` | 17,880.43 USD | 18,383.19 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `2250.40` | `0.0928` | 208.84 USD | 502.75 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `2250.50` | `0.1306` | 293.92 USD | 293.92 USD | `2 orders` | `-0.01%` | `-` |
| `MID_SPREAD` | `2250.65` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,250.65` | `0.00%` | `-` |
| `ASK` | `2250.80` | `299.2842` | 673,628.88 USD | 673,628.88 USD | `31 orders` | `+0.01%` | `-` |
| `ASK` | `2250.90` | `141.0183` | 317,418.09 USD | 991,046.97 USD | `15 orders` | `+0.01%` | `-` |
| `ASK` | `2251.00` | `99.7969` | 224,642.82 USD | 1,215,689.79 USD | `11 orders` | `+0.02%` | `-` |
| `ASK` | `2251.10` | `56.4776` | 127,136.73 USD | 1,342,826.52 USD | `8 orders` | `+0.02%` | `-` |
| `ASK` | `2251.20` | `317.1662` | 714,004.55 USD | 2,056,831.07 USD | `22 orders` | `+0.02%` | `-` |
| `ASK` | `2251.30` | `357.7189` | 805,332.56 USD | 2,862,163.63 USD | `17 orders` | `+0.03%` | `-` |
| `ASK` | `2251.40` | `59.3752` | 133,677.33 USD | 2,995,840.95 USD | `8 orders` | `+0.03%` | `-` |
| `ASK` | `2251.50` | `84.7420` | 190,796.61 USD | 3,186,637.56 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `2251.60` | `152.7808` | 344,001.25 USD | 3,530,638.81 USD | `9 orders` | `+0.04%` | `-` |
| `ASK` | `2251.70` | `154.6255` | 348,170.24 USD | 3,878,809.05 USD | `8 orders` | `+0.05%` | `-` |
| `ASK` | `2251.80` | `62.3696` | 140,443.87 USD | 4,019,252.92 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `2251.90` | `287.1356` | 646,600.66 USD | 4,665,853.57 USD | `4 orders` | `+0.06%` | `-` |
| `ASK` | `2252.00` | `94.1271` | 211,974.23 USD | 4,877,827.80 USD | `8 orders` | `+0.06%` | `-` |
| `ASK` | `2252.10` | `133.2146` | 300,012.60 USD | 5,177,840.40 USD | `6 orders` | `+0.06%` | `-` |
| `ASK` | `2252.20` | `26.8626` | 60,499.95 USD | 5,238,340.35 USD | `4 orders` | `+0.07%` | `-` |
| `ASK` | `2252.30` | `147.7260` | 332,723.27 USD | 5,571,063.62 USD | `5 orders` | `+0.07%` | `-` |
| `ASK` | `2252.40` | `46.3358` | 104,366.76 USD | 5,675,430.38 USD | `6 orders` | `+0.08%` | `-` |
| `ASK` | `2252.50` | `3.9172` | 8,823.49 USD | 5,684,253.87 USD | `3 orders` | `+0.08%` | `-` |
| `ASK` | `2252.60` | `113.0442` | 254,643.36 USD | 5,938,897.24 USD | `6 orders` | `+0.09%` | `-` |
| `ASK` | `2252.70` | `153.9746` | 346,858.58 USD | 6,285,755.82 USD | `7 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:35:51 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 02:35:51 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1918.00` | `4,184.01` | 8,024,935.59 USD | `TRIGGER_STOP` | `0x6ea486a342` | `2026-10-30 02:35:51 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `8,500.00` | 16,371,850.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 02:35:51 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1926.37` | `8,092.45` | 15,589,061.68 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 02:35:51 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2040.74` | `7,964.66` | 16,253,781.36 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 02:35:51 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2148.53` | `6,615.35` | 14,213,296.10 USD | `AT_RISK_LIQ` | `0x0c4a3a7ac7` | `2026-10-30 02:35:51 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2171.20` | `48,499.51` | 105,302,149.66 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 02:35:51 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2180.26` | `44,734.81` | 97,533,620.73 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2224.40` | `2,002.49` | 4,454,346.54 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.40` | `5,456.48` | 12,148,317.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2227.00` | `734.73` | 1,636,235.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x646be0d5f9` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2232.90` | `343.82` | 767,714.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2233.40` | `1,534.63` | 3,427,451.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2235.30` | `358.62` | 801,627.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2238.20` | `549.52` | 1,229,926.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2242.60` | `1,006.30` | 2,256,723.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2242.90` | `396.67` | 889,700.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2245.90` | `2,804.81` | 6,299,314.92 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2245.90` | `329.23` | 739,424.17 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2246.20` | `549.52` | 1,234,322.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2247.80` | `549.79` | 1,235,820.21 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2248.40` | `1,781.29` | 4,005,059.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:35:51 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2250.00` | `6,500.00` | 14,625,000.00 USD | `TRIGGER_STOP` | `0x6eae4120a8` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2250.40` | `1,334.75` | 3,003,711.05 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2250.60` | `396.67` | 892,754.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2250.90` | `1,433.94` | 3,227,654.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2250.90` | `889.63` | 2,002,462.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2253.80` | `366.62` | 826,281.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2253.90` | `479.90` | 1,081,654.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2254.90` | `666.04` | 1,501,842.55 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2254.90` | `444.02` | 1,001,226.34 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2255.10` | `297.58` | 671,063.64 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2256.20` | `332.83` | 750,929.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2261.30` | `332.08` | 750,935.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2263.10` | `297.59` | 673,480.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2263.40` | `314.56` | 711,964.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2264.40` | `366.65` | 830,246.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2264.50` | `663.21` | 1,501,848.33 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2264.80` | `442.09` | 1,001,244.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2266.20` | `396.82` | 899,271.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2266.90` | `500.06` | 1,133,586.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2267.00` | `883.33` | 2,002,498.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2268.20` | `1,434.46` | 3,253,649.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2268.50` | `549.99` | 1,247,656.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.00` | `1,323.79` | 3,003,670.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.60` | `706.51` | 1,603,491.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2271.50` | `1,763.13` | 4,004,960.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2273.30` | `312.70` | 710,864.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2276.60` | `1,021.14` | 2,324,719.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2277.50` | `549.22` | 1,250,841.72 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2278.60` | `396.26` | 902,918.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2279.00` | `2,807.32` | 6,397,882.74 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2284.10` | `350.96` | 801,627.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2284.80` | `336.01` | 767,714.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2285.00` | `300.00` | 685,500.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xe47f539d76` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2285.40` | `549.22` | 1,255,180.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2287.30` | `5,456.48` | 12,480,617.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2291.00` | `1,455.02` | 3,333,441.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:35:51 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2292.00` | `2,500.00` | 5,730,000.00 USD | `TRIGGER_STOP` | `0x934de82f50` | `2026-10-30 02:35:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2296.70` | `1,304.45` | 2,995,923.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xbc76170c8a` | `2026-10-30 02:35:51 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2307.20` | `599,999.99` | 1,384,319,976.93 USD | `TRIGGER_STOP` | `0x069604ebfb` | `2026-10-30 02:35:51 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2310.00` | `2,000.00` | 4,620,000.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-30 02:35:51 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2319.00` | `2,500.00` | 5,797,500.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-30 02:35:51 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2440.00` | `4,002.10` | 9,765,127.17 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 02:35:51 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2585.96` | `6,224.05` | 16,095,121.81 USD | `AT_RISK_LIQ` | `0x08bf75d170` | `2026-10-30 02:35:51 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.71` | `9,700.00` | 25,789,475.87 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 02:35:51 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2709.06` | `8,500.00` | 23,027,017.58 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 02:35:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 239,993,222.30 USD | `106,417.71` | `2322.74` | `2259.00` | `3969.21` | 7,187,789.86 USD | `+2.99%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 149,574,138.55 USD | `65,205.17` | `2375.30` | `2259.00` | `4515.38` | 5,308,124.55 USD | `+3.55%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 109,773,795.23 USD | `48,499.51` | `2610.31` | `2259.00` | `2171.20` | -16,825,088.63 USD | `-15.33%` | `10X Cross` |
| `7` | `0x0392...d7d9` | `LONG` | 103,511,884.73 USD | `44,734.81` | `2518.71` | `2259.00` | `2180.26` | -9,162,421.85 USD | `-8.85%` | `9X Cross` |
| `14` | `0xde8d...9524` | `LONG` | 70,197,639.55 USD | `30,282.40` | `2134.45` | `2259.00` | `1787.15` | 5,561,308.98 USD | `+7.92%` | `20X Cross` |
| `20` | `0x7fda...17d1` | `SHORT` | 55,105,767.66 USD | `24,401.44` | `2434.65` | `2259.00` | `3977.88` | 4,303,220.15 USD | `+7.81%` | `25X Cross` |
| `23` | `0xdf95...7d72` | `SHORT` | 51,046,973.85 USD | `22,635.23` | `2402.54` | `2259.00` | `4059.78` | 3,335,075.81 USD | `+6.53%` | `25X Cross` |
| `27` | `0xeced...6210` | `SHORT` | 43,211,095.80 USD | `18,687.58` | `2522.09` | `2259.00` | `3345.81` | 3,920,816.65 USD | `+9.07%` | `20X Cross` |
| `33` | `0xb695...a92d` | `SHORT` | 37,672,257.90 USD | `16,704.62` | `2557.74` | `2259.00` | `4146.52` | 5,053,907.15 USD | `+13.42%` | `20X Cross` |
| `34` | `0x6046...b21d` | `LONG` | 36,829,365.66 USD | `15,927.59` | `2410.19` | `2259.00` | `1592.19` | -1,559,253.99 USD | `-4.23%` | `6X Cross` |
| `38` | `0x45d2...4029` | `SHORT` | 31,487,940.00 USD | `13,950.00` | `2443.60` | `2259.00` | `5252.87` | 2,600,342.46 USD | `+8.26%` | `20X Cross` |
| `43` | `0x2371...0883` | `LONG` | 27,526,800.00 USD | `12,000.00` | `2421.77` | `2259.00` | `1280.13` | -1,534,494.85 USD | `-5.57%` | `20X Cross` |
| `44` | `0xbd1c...ff0e` | `LONG` | 27,102,000.00 USD | `12,000.00` | `2419.91` | `2259.00` | `1521.03` | -1,937,032.39 USD | `-7.15%` | `20X Cross` |
| `47` | `0x0622...8088` | `LONG` | 26,643,587.71 USD | `11,814.29` | `2266.11` | `2259.00` | `1455.60` | -128,973.80 USD | `-0.48%` | `5X Cross` |
| `50` | `0xa9de...e049` | `LONG` | 25,510,100.00 USD | `11,000.00` | `2481.81` | `2259.00` | `1644.77` | -1,789,879.46 USD | `-7.02%` | `20X Cross` |
| `51` | `0x0c5d...36b3` | `LONG` | 25,510,100.00 USD | `11,000.00` | `2482.20` | `2259.00` | `1645.10` | -1,794,153.24 USD | `-7.03%` | `20X Cross` |
| `52` | `0x09dc...c094` | `LONG` | 25,485,900.00 USD | `11,000.00` | `2465.31` | `2259.00` | `1638.10` | -1,632,523.04 USD | `-6.41%` | `20X Cross` |
| `55` | `0x6c93...59a4` | `LONG` | 24,893,000.00 USD | `11,000.00` | `2441.15` | `2259.00` | `1603.06` | -1,959,672.73 USD | `-7.87%` | `20X Cross` |
| `57` | `0xa61c...66b9` | `LONG` | 24,698,339.20 USD | `10,888.00` | `2398.32` | `2259.00` | `1489.32` | -1,414,618.19 USD | `-5.73%` | `10X Cross` |
| `65` | `0x15a4...dfdb` | `LONG` | 23,191,000.00 USD | `10,000.00` | `1761.94` | `2259.00` | `55.52` | 5,571,518.97 USD | `+24.02%` | `20X Cross` |
| `66` | `0xec7f...df39` | `LONG` | 23,165,000.00 USD | `10,000.00` | `2719.35` | `2259.00` | `1721.62` | -4,028,548.52 USD | `-17.39%` | `20X Cross` |
| `72` | `0xa2ce...3126` | `LONG` | 22,621,109.26 USD | `10,016.88` | `2162.83` | `2259.00` | `1516.15` | 956,307.21 USD | `+4.23%` | `10X Cross` |
| `73` | `0x6646...6de5` | `LONG` | 22,585,000.00 USD | `10,000.00` | `1765.80` | `2259.00` | `1721.15` | 4,926,942.55 USD | `+21.82%` | `25X Cross` |
| `77` | `0xaeaa...2416` | `SHORT` | 21,896,780.00 USD | `9,700.00` | `2311.92` | `2259.00` | `2658.71` | 528,902.40 USD | `+2.42%` | `25X Cross` |
| `80` | `0x4487...c92d` | `SHORT` | 21,680,021.76 USD | `9,599.30` | `2368.57` | `2259.00` | `2785.19` | 1,056,644.31 USD | `+4.87%` | `10X Cross` |
| `82` | `0xba5d...a352` | `SHORT` | 20,970,252.20 USD | `9,054.12` | `2493.89` | `2259.00` | `2940.24` | 1,609,755.06 USD | `+7.68%` | `20X Cross` |
| `84` | `0xca49...53c8` | `SHORT` | 20,921,481.52 USD | `9,264.26` | `2549.47` | `2259.00` | `3855.66` | 2,697,543.22 USD | `+12.89%` | `25X Cross` |
| `85` | `0xea00...a918` | `LONG` | 20,833,953.68 USD | `9,003.83` | `2003.01` | `2259.00` | `1293.48` | 2,799,174.81 USD | `+13.44%` | `5X Cross` |
| `100` | `0xb37f...66ca` | `SHORT` | 19,238,900.00 USD | `8,500.00` | `2308.30` | `2259.00` | `2709.06` | 381,654.19 USD | `+1.98%` | `25X Cross` |
| `108` | `0x218a...7da2` | `SHORT` | 18,547,659.48 USD | `7,997.78` | `2208.16` | `2259.00` | `2877.27` | -887,264.27 USD | `-4.78%` | `10X Cross` |
| `110` | `0x5f91...65aa` | `LONG` | 18,418,266.77 USD | `7,964.66` | `1626.99` | `2259.00` | `2040.74` | 5,459,823.70 USD | `+29.64%` | `16X Cross` |
| `111` | `0x9eec...daab` | `LONG` | 18,388,478.91 USD | `8,092.45` | `1658.44` | `2259.00` | `1924.77` | 4,967,614.38 USD | `+27.01%` | `15X Cross` |
| `116` | `0xcf53...ee11` | `SHORT` | 17,203,208.12 USD | `7,603.63` | `1862.69` | `2259.00` | `4009.75` | -3,039,944.18 USD | `-17.67%` | `7X Cross` |
| `121` | `0x939f...04d2` | `LONG` | 16,291,142.85 USD | `7,223.81` | `2500.18` | `2259.00` | `1666.90` | -1,769,747.32 USD | `-10.86%` | `25X Cross` |
| `125` | `0xec0b...b078` | `LONG` | 15,836,223.95 USD | `7,007.80` | `2065.97` | `2259.00` | `1038.45` | 1,358,294.37 USD | `+8.58%` | `25X Cross` |
| `130` | `0x0c4a...1b19` | `LONG` | 15,317,192.27 USD | `6,615.35` | `2373.06` | `2259.00` | `2197.06` | -381,449.72 USD | `-2.49%` | `25X Isolated` |
| `131` | `0x418a...8888` | `SHORT` | 15,208,536.58 USD | `6,724.38` | `2494.55` | `2259.00` | `3000.08` | 1,565,786.60 USD | `+10.30%` | `25X Cross` |
| `132` | `0x4ff9...38d3` | `LONG` | 15,208,360.28 USD | `6,564.10` | `2447.40` | `2259.00` | `1670.72` | -856,662.47 USD | `-5.63%` | `3X Isolated` |
| `133` | `0xf78c...c581` | `LONG` | 15,043,462.62 USD | `6,500.22` | `2521.53` | `2259.00` | `1914.20` | -1,347,078.33 USD | `-8.95%` | `20X Cross` |
| `139` | `0x799f...5f4c` | `LONG` | 14,261,379.28 USD | `6,310.90` | `2390.33` | `2259.00` | `1801.39` | -823,785.34 USD | `-5.78%` | `20X Cross` |
| `144` | `0x08bf...7872` | `SHORT` | 14,085,019.27 USD | `6,224.05` | `2258.00` | `2259.00` | `2585.96` | -31,103.16 USD | `-0.22%` | `20X Cross` |
| `149` | `0xd9e7...4aff` | `LONG` | 13,873,800.00 USD | `6,000.00` | `2480.18` | `2259.00` | `1408.49` | -1,007,324.33 USD | `-7.26%` | `20X Cross` |
| `160` | `0xecb6...2b00` | `SHORT` | 12,616,260.17 USD | `5,594.30` | `2286.93` | `2259.00` | `7077.79` | 177,527.63 USD | `+1.41%` | `15X Cross` |
| `178` | `0x645b...87b8` | `SHORT` | 11,335,479.01 USD | `5,011.04` | `2421.66` | `2259.00` | `6398.30` | 799,573.81 USD | `+7.05%` | `10X Cross` |
| `179` | `0x45ab...6cbc` | `LONG` | 11,296,068.73 USD | `4,920.96` | `2727.66` | `2259.00` | `1374.16` | -2,126,675.07 USD | `-18.83%` | `7X Cross` |
| `188` | `0x64b7...9da9` | `LONG` | 11,017,254.04 USD | `4,856.84` | `2604.61` | `2259.00` | `1557.40` | -1,632,960.37 USD | `-14.82%` | `25X Cross` |
| `190` | `0x5559...d43b` | `SHORT` | 10,997,126.07 USD | `4,755.93` | `2262.69` | `2259.00` | `2843.73` | -235,920.19 USD | `-2.15%` | `25X Cross` |
| `194` | `0xfb18...eb17` | `SHORT` | 10,943,475.65 USD | `4,845.89` | `2315.54` | `2259.00` | `2589.82` | 277,407.14 USD | `+2.53%` | `25X Cross` |
| `199` | `0x1ee7...edf5` | `LONG` | 10,694,767.50 USD | `4,750.00` | `2330.22` | `2259.00` | `2091.22` | -373,792.57 USD | `-3.50%` | `25X Cross` |
| `201` | `0x12d2...f97f` | `LONG` | 10,685,646.03 USD | `4,708.79` | `2588.61` | `2259.00` | `1977.39` | -1,503,588.29 USD | `-14.07%` | `20X Cross` |
| `212` | `0xe091...6705` | `SHORT` | 10,405,350.46 USD | `4,500.00` | `2467.33` | `2259.00` | `2573.01` | 697,658.05 USD | `+6.70%` | `20X Cross` |
| `227` | `0xfe7c...b7ae` | `SHORT` | 9,943,232.80 USD | `4,402.58` | `2440.17` | `2259.00` | `4443.27` | 799,855.07 USD | `+8.04%` | `25X Cross` |
| `233` | `0xc179...e0c8` | `LONG` | 9,774,456.51 USD | `4,309.16` | `2342.89` | `2259.00` | `543.10` | -321,422.28 USD | `-3.29%` | `10X Cross` |
| `236` | `0x6ea4...0ea7` | `SHORT` | 9,690,590.89 USD | `4,184.01` | `2602.13` | `2259.00` | `3426.02` | 1,196,755.78 USD | `+12.35%` | `20X Cross` |
| `239` | `0x28bb...fca6` | `SHORT` | 9,549,088.85 USD | `4,209.61` | `1896.10` | `2259.00` | `3041.18` | -1,567,206.29 USD | `-16.41%` | `20X Cross` |
| `246` | `0x3dc9...54b0` | `SHORT` | 9,274,081.67 USD | `3,999.69` | `2480.32` | `2259.00` | `6122.25` | 646,454.89 USD | `+6.97%` | `20X Cross` |
| `248` | `0xfb94...0ddf` | `SHORT` | 9,254,859.26 USD | `4,002.10` | `2382.44` | `2259.00` | `5105.41` | 279,924.89 USD | `+3.02%` | `20X Cross` |
| `250` | `0x77ee...2902` | `SHORT` | 9,220,453.26 USD | `3,982.23` | `2476.53` | `2259.00` | `4294.33` | 641,668.32 USD | `+6.96%` | `25X Cross` |
| `254` | `0x95fe...f8fa` | `LONG` | 9,179,200.00 USD | `4,000.00` | `2341.35` | `2259.00` | `2259.02` | -186,216.51 USD | `-2.03%` | `20X Isolated` |
| `258` | `0x5e9e...35ee` | `SHORT` | 9,050,263.04 USD | `4,007.56` | `1796.39` | `2259.00` | `2586.51` | -1,851,112.95 USD | `-20.45%` | `20X Cross` |
| `260` | `0x8cc9...2b6a` | `SHORT` | 9,020,800.00 USD | `4,000.00` | `1791.18` | `2259.00` | `3824.64` | -1,856,053.33 USD | `-20.58%` | `25X Cross` |
| `267` | `0x4b67...f4e7` | `LONG` | 8,857,093.61 USD | `3,820.84` | `2591.51` | `2259.00` | `1600.62` | -1,044,679.93 USD | `-11.79%` | `20X Cross` |
| `272` | `0xf02d...5eb3` | `LONG` | 8,726,095.19 USD | `3,855.99` | `2513.67` | `2259.00` | `296.94` | -966,617.13 USD | `-11.08%` | `20X Cross` |
| `289` | `0x8ae4...3d60` | `LONG` | 8,241,143.08 USD | `3,558.20` | `2482.21` | `2259.00` | `384.40` | -591,054.95 USD | `-7.17%` | `10X Cross` |
| `316` | `0x9c06...0560` | `SHORT` | 7,658,359.16 USD | `3,303.58` | `2270.55` | `2259.00` | `3340.13` | -157,395.21 USD | `-2.06%` | `25X Cross` |
| `330` | `0x9c2a...f6a8` | `SHORT` | 7,078,235.87 USD | `3,058.48` | `2543.83` | `2259.00` | `2590.00` | 702,024.76 USD | `+9.92%` | `20X Cross` |
| `340` | `0x4a20...3c26` | `LONG` | 6,790,200.00 USD | `3,000.00` | `2428.72` | `2259.00` | `555.40` | -495,960.28 USD | `-7.30%` | `20X Cross` |
| `341` | `0x007d...67a0` | `LONG` | 6,774,900.00 USD | `3,000.00` | `2400.00` | `2259.00` | `1471.75` | -425,100.00 USD | `-6.27%` | `25X Cross` |
| `375` | `0xb15b...dbae` | `SHORT` | 6,319,336.40 USD | `2,808.87` | `2294.54` | `2259.00` | `2281.38` | 125,731.96 USD | `+1.99%` | `25X Cross` |
| `384` | `0xf517...c032` | `SHORT` | 6,189,681.72 USD | `2,738.07` | `2053.90` | `2259.00` | `5546.48` | -565,939.81 USD | `-9.14%` | `25X Cross` |
| `387` | `0xab81...c608` | `SHORT` | 6,147,731.76 USD | `2,716.75` | `2307.68` | `2259.00` | `3021.46` | 121,672.65 USD | `+1.98%` | `20X Cross` |
| `392` | `0xbb34...1696` | `LONG` | 6,028,620.00 USD | `2,600.00` | `2318.80` | `2259.00` | `1996.74` | -280.85 USD | `-0.00%` | `25X Cross` |
| `393` | `0xc619...10f5` | `LONG` | 6,021,860.00 USD | `2,600.00` | `2318.40` | `2259.00` | `1881.22` | -5,988.91 USD | `-0.10%` | `25X Cross` |
| `394` | `0x8328...f54a` | `SHORT` | 5,975,047.75 USD | `2,576.45` | `2292.01` | `2259.00` | `3280.25` | -69,776.46 USD | `-1.17%` | `25X Cross` |
| `398` | `0xbc76...417c` | `LONG` | 5,895,578.89 USD | `2,608.89` | `2261.38` | `2259.00` | `2191.03` | -4,145.99 USD | `-0.07%` | `25X Cross` |
| `402` | `0xed48...7c9b` | `SHORT` | 5,755,350.41 USD | `2,551.13` | `2460.02` | `2259.00` | `3239.97` | 520,496.00 USD | `+9.04%` | `20X Cross` |
| `420` | `0x1c98...7fc7` | `LONG` | 5,459,723.62 USD | `2,358.00` | `2467.15` | `2259.00` | `1897.24` | -357,847.86 USD | `-6.55%` | `10X Cross` |
| `424` | `0xfbe2...c8ea` | `SHORT` | 5,441,387.43 USD | `2,404.08` | `2041.57` | `2259.00` | `2606.31` | -533,294.70 USD | `-9.80%` | `20X Cross` |
| `442` | `0x023a...2355` | `LONG` | 5,034,402.03 USD | `2,232.35` | `2330.15` | `2259.00` | `0.000000` | -167,326.70 USD | `-3.32%` | `25X Cross` |
| `444` | `0x6859...7e1e` | `SHORT` | 5,029,105.75 USD | `2,224.58` | `2200.39` | `2259.00` | `3922.87` | -134,153.02 USD | `-2.67%` | `25X Cross` |
| `445` | `0xb829...3a81` | `LONG` | 4,988,673.27 USD | `2,153.91` | `2537.61` | `2259.00` | `757.55` | -477,123.47 USD | `-9.56%` | `20X Cross` |
| `452` | `0xd507...c948` | `SHORT` | 4,908,285.37 USD | `2,172.00` | `2387.49` | `2259.00` | `2707.44` | 277,355.65 USD | `+5.65%` | `5X Isolated` |
| `468` | `0x382b...3e39` | `SHORT` | 4,807,653.12 USD | `2,129.54` | `2296.66` | `2259.00` | `4610.25` | 83,184.10 USD | `+1.73%` | `25X Cross` |
| `479` | `0xf929...d1f9` | `SHORT` | 4,638,200.00 USD | `2,000.00` | `2423.37` | `2259.00` | `2548.84` | 208,540.34 USD | `+4.50%` | `25X Cross` |
| `489` | `0x7a6d...f79c` | `SHORT` | 4,523,600.00 USD | `2,000.00` | `2418.41` | `2259.00` | `2651.63` | 313,232.11 USD | `+6.92%` | `25X Cross` |
| `490` | `0x3440...32c5` | `SHORT` | 4,520,877.24 USD | `2,000.57` | `2198.21` | `2259.00` | `3714.20` | -123,214.11 USD | `-2.73%` | `25X Cross` |
| `500` | `0x8376...9a1e` | `SHORT` | 4,428,720.78 USD | `1,910.50` | `2477.72` | `2259.00` | `3162.12` | 304,967.39 USD | `+6.89%` | `20X Cross` |
| `505` | `0x0514...bdfe` | `SHORT` | 4,411,875.00 USD | `1,950.00` | `1988.74` | `2259.00` | `3028.97` | -533,815.37 USD | `-12.10%` | `25X Cross` |
| `530` | `0x7265...91a5` | `LONG` | 4,166,462.61 USD | `1,801.87` | `2533.96` | `2259.00` | `1988.16` | -399,403.84 USD | `-9.59%` | `20X Cross` |
| `531` | `0x739c...cfb2` | `SHORT` | 4,165,020.00 USD | `1,800.00` | `2427.60` | `2259.00` | `2604.56` | 204,676.38 USD | `+4.91%` | `25X Cross` |
| `541` | `0x541e...071d` | `SHORT` | 4,085,437.00 USD | `1,805.00` | `2648.19` | `2259.00` | `3139.04` | 694,547.84 USD | `+17.00%` | `25X Cross` |
| `544` | `0x91a9...3f70` | `SHORT` | 4,053,538.63 USD | `1,767.48` | `2156.23` | `2259.00` | `3663.93` | -242,434.55 USD | `-5.98%` | `4X Cross` |
| `545` | `0x3453...b323` | `SHORT` | 4,049,609.84 USD | `1,750.12` | `2328.82` | `2259.00` | `2399.97` | 26,122.29 USD | `+0.65%` | `25X Cross` |
| `557` | `0xa445...329d` | `LONG` | 4,008,346.42 USD | `1,776.75` | `2398.85` | `2259.00` | `1928.79` | -253,822.93 USD | `-6.33%` | `25X Cross` |
| `579` | `0x39b4...5c34` | `SHORT` | 3,892,730.18 USD | `1,717.05` | `2329.97` | `2259.00` | `2547.87` | 107,956.82 USD | `+2.77%` | `25X Cross` |
| `592` | `0xfeec...4e9c` | `SHORT` | 3,827,040.69 USD | `1,691.81` | `2566.49` | `2259.00` | `2654.66` | 514,983.83 USD | `+13.46%` | `10X Cross` |
| `595` | `0x936c...bb0f` | `SHORT` | 3,811,533.17 USD | `1,688.69` | `2434.60` | `2259.00` | `8661.64` | 299,753.94 USD | `+7.86%` | `20X Cross` |
| `600` | `0xeee0...0b53` | `LONG` | 3,785,521.59 USD | `1,637.12` | `2468.64` | `2259.00` | `158.25` | -255,954.47 USD | `-6.76%` | `7X Cross` |
| `603` | `0x27b8...12fc` | `LONG` | 3,769,749.28 USD | `1,628.12` | `2468.73` | `2259.00` | `476.68` | -249,645.35 USD | `-6.62%` | `10X Cross` |
| `606` | `0x982b...4606` | `LONG` | 3,762,015.01 USD | `1,626.82` | `2575.24` | `2259.00` | `1548.44` | -427,438.07 USD | `-11.36%` | `5X Isolated` |
| `630` | `0x73d7...8be1` | `LONG` | 3,616,589.54 USD | `1,601.47` | `2410.40` | `2259.00` | `2083.65` | -243,589.38 USD | `-6.74%` | `25X Cross` |
| `638` | `0xe170...9300` | `SHORT` | 3,545,527.48 USD | `1,533.40` | `2076.39` | `2259.00` | `3240.60` | -361,577.98 USD | `-10.20%` | `25X Cross` |
| `649` | `0x2e2b...2fab` | `LONG` | 3,488,522.59 USD | `1,507.38` | `2245.53` | `2259.00` | `1164.16` | 103,649.49 USD | `+2.97%` | `25X Cross` |
| `664` | `0x251f...6e5d` | `LONG` | 3,390,900.00 USD | `1,500.00` | `2346.68` | `2259.00` | `1861.18` | -129,130.49 USD | `-3.81%` | `20X Cross` |
| `668` | `0xad54...6203` | `LONG` | 3,371,604.49 USD | `1,458.18` | `2627.45` | `2259.00` | `2145.32` | -459,702.19 USD | `-13.63%` | `10X Isolated` |
| `677` | `0xbadb...9ee6` | `LONG` | 3,310,760.51 USD | `1,428.16` | `1936.00` | `2259.00` | `1059.83` | 545,838.87 USD | `+16.49%` | `20X Cross` |
| `681` | `0x4b5f...0dd8` | `LONG` | 3,291,352.70 USD | `1,431.96` | `2339.45` | `2259.00` | `2148.73` | -58,640.24 USD | `-1.78%` | `10X Cross` |
| `691` | `0xef70...a84c` | `SHORT` | 3,255,550.48 USD | `1,442.74` | `2424.73` | `2259.00` | `3322.11` | 242,720.34 USD | `+7.46%` | `25X Cross` |
| `742` | `0xd4c1...3d1d` | `SHORT` | 3,064,840.75 USD | `1,358.53` | `2336.05` | `2259.00` | `6004.35` | 108,760.33 USD | `+3.55%` | `12X Cross` |
| `764` | `0x880a...311c` | `SHORT` | 2,976,046.91 USD | `1,320.22` | `2425.76` | `2259.00` | `8420.64` | 226,502.24 USD | `+7.61%` | `9X Cross` |
| `765` | `0x0dd5...f6ee` | `LONG` | 2,974,592.05 USD | `1,314.97` | `2310.91` | `2259.00` | `1655.68` | -64,195.42 USD | `-2.16%` | `5X Cross` |
| `770` | `0xfc66...ca06` | `LONG` | 2,955,429.74 USD | `1,313.23` | `2303.59` | `2259.00` | `0.000000` | -69,722.37 USD | `-2.36%` | `20X Cross` |
| `785` | `0xc435...c905` | `SHORT` | 2,894,236.80 USD | `1,248.00` | `2704.38` | `2259.00` | `4945.84` | 480,833.55 USD | `+16.61%` | `20X Cross` |
| `802` | `0x2577...4897` | `LONG` | 2,833,578.22 USD | `1,253.57` | `2315.75` | `2259.00` | `0.000000` | -69,386.90 USD | `-2.45%` | `15X Cross` |
| `805` | `0x7178...0854` | `LONG` | 2,824,178.50 USD | `1,218.63` | `2461.81` | `2259.00` | `1079.20` | -175,867.90 USD | `-6.23%` | `10X Cross` |
| `846` | `0xfc27...9d9d` | `SHORT` | 2,658,831.19 USD | `1,178.98` | `2385.48` | `2259.00` | `17132.37` | 153,603.99 USD | `+5.78%` | `25X Cross` |
| `852` | `0x07fd...689d` | `LONG` | 2,630,677.72 USD | `1,166.49` | `2419.97` | `2259.00` | `0.000000` | -192,214.08 USD | `-7.31%` | `25X Cross` |
| `887` | `0x2f80...f203` | `SHORT` | 2,522,096.48 USD | `1,088.94` | `1984.00` | `2259.00` | `3071.71` | -361,629.29 USD | `-14.34%` | `20X Cross` |
| `896` | `0x2b61...2f6c` | `SHORT` | 2,493,506.77 USD | `1,076.60` | `2681.75` | `2259.00` | `6327.25` | 393,665.96 USD | `+15.79%` | `10X Cross` |
| `904` | `0x6f11...0389` | `SHORT` | 2,475,118.10 USD | `1,079.00` | `2333.39` | `2259.00` | `3199.71` | 42,610.81 USD | `+1.72%` | `25X Cross` |
| `911` | `0xa0fb...96be` | `LONG` | 2,447,921.93 USD | `1,078.28` | `2300.07` | `2259.00` | `1432.27` | -32,210.54 USD | `-1.32%` | `3X Cross` |
| `939` | `0x1b2a...f7a6` | `LONG` | 2,370,958.43 USD | `1,025.37` | `2737.51` | `2259.00` | `883.11` | -436,001.51 USD | `-18.39%` | `10X Cross` |
| `959` | `0x9599...c60a` | `LONG` | 2,325,179.85 USD | `1,027.28` | `2269.43` | `2259.00` | `0.000000` | -6,154.66 USD | `-0.26%` | `20X Cross` |
| `960` | `0x4044...794c` | `LONG` | 2,318,700.00 USD | `1,000.00` | `2332.68` | `2259.00` | `0.000000` | -13,989.84 USD | `-0.60%` | `25X Cross` |
| `963` | `0x5986...89d9` | `LONG` | 2,312,800.00 USD | `1,000.00` | `2346.34` | `2259.00` | `1283.38` | -33,549.54 USD | `-1.45%` | `25X Cross` |
| `965` | `0x2828...93a0` | `LONG` | 2,312,300.00 USD | `1,000.00` | `2393.30` | `2259.00` | `2283.50` | -81,009.16 USD | `-3.50%` | `25X Cross` |
| `970` | `0xfe82...ce65` | `SHORT` | 2,298,500.00 USD | `1,000.00` | `2300.50` | `2259.00` | `2718.45` | 2,007.93 USD | `+0.09%` | `25X Cross` |
| `974` | `0xdf60...d3c7` | `LONG` | 2,294,800.00 USD | `1,000.00` | `2736.24` | `2259.00` | `2246.10` | -441,442.88 USD | `-19.24%` | `10X Isolated` |
| `979` | `0x02aa...1806` | `SHORT` | 2,285,412.26 USD | `1,007.10` | `2654.68` | `2259.00` | `3613.71` | 388,119.84 USD | `+16.98%` | `20X Cross` |
| `981` | `0x001a...fef6` | `SHORT` | 2,277,763.29 USD | `1,007.33` | `2022.19` | `2259.00` | `3070.41` | -240,755.33 USD | `-10.57%` | `10X Cross` |
| `989` | `0xdb3a...cf3b` | `LONG` | 2,264,657.77 USD | `1,003.22` | `2705.01` | `2259.00` | `0.000000` | -449,049.13 USD | `-19.83%` | `4X Cross` |
| `991` | `0x6a41...a3b9` | `LONG` | 2,260,271.99 USD | `999.06` | `2318.53` | `2259.00` | `2148.19` | -56,081.27 USD | `-2.48%` | `20X Cross` |
| `993` | `0x5272...fcd9` | `SHORT` | 2,255,200.00 USD | `1,000.00` | `2241.82` | `2259.00` | `2880.78` | -13,375.51 USD | `-0.59%` | `5X Cross` |
| `998` | `0xb002...ed8a` | `SHORT` | 2,231,829.59 USD | `962.78` | `2299.66` | `2259.00` | `4195.93` | -17,751.68 USD | `-0.80%` | `25X Cross` |
| `1007` | `0xb7bd...2f3a` | `LONG` | 2,209,866.57 USD | `977.00` | `2262.44` | `2259.00` | `1423.72` | -531.88 USD | `-0.02%` | `20X Cross` |
| `1042` | `0x9606...4e5d` | `SHORT` | 2,116,508.95 USD | `913.00` | `2478.70` | `2259.00` | `4054.78` | 146,544.65 USD | `+6.92%` | `20X Cross` |
| `1044` | `0xc8fe...afa4` | `LONG` | 2,112,922.97 USD | `936.37` | `2331.34` | `2259.00` | `2145.83` | -70,081.27 USD | `-3.32%` | `10X Isolated` |
| `1045` | `0x2e30...4cb5` | `SHORT` | 2,110,814.49 USD | `934.69` | `2340.08` | `2259.00` | `7575.78` | 76,446.89 USD | `+3.62%` | `2X Cross` |
| `1080` | `0x5238...54e5` | `SHORT` | 2,042,370.00 USD | `900.00` | `2289.53` | `2259.00` | `5338.95` | 18,212.42 USD | `+0.89%` | `25X Cross` |
| `1089` | `0x5f10...d49d` | `LONG` | 2,029,680.00 USD | `900.00` | `2249.83` | `2259.00` | `1817.99` | 4,826.53 USD | `+0.24%` | `25X Cross` |
| `1093` | `0xbef3...0d3e` | `LONG` | 2,025,314.81 USD | `880.99` | `2330.82` | `2259.00` | `2123.97` | -28,125.97 USD | `-1.39%` | `20X Cross` |
| `1132` | `0x20ad...8183` | `SHORT` | 1,977,144.86 USD | `876.39` | `2308.01` | `2259.00` | `2352.21` | 45,583.41 USD | `+2.31%` | `25X Isolated` |
| `1168` | `0xcd27...52a8` | `LONG` | 1,920,472.12 USD | `837.21` | `2553.56` | `2259.00` | `1404.25` | -217,392.66 USD | `-11.32%` | `2X Cross` |
| `1213` | `0x7737...bf66` | `SHORT` | 1,852,557.98 USD | `799.79` | `2494.83` | `2259.00` | `24700.47` | 142,788.05 USD | `+7.71%` | `15X Cross` |
| `1217` | `0x8923...1bac` | `SHORT` | 1,849,912.49 USD | `818.26` | `2329.67` | `2259.00` | `2787.72` | 56,356.86 USD | `+3.05%` | `25X Cross` |
| `1231` | `0x04a9...95aa` | `LONG` | 1,835,120.00 USD | `800.00` | `2595.13` | `2259.00` | `1872.22` | -240,986.74 USD | `-13.13%` | `5X Cross` |
| `1245` | `0x3fc5...c0c1` | `SHORT` | 1,815,371.61 USD | `804.26` | `2702.11` | `2259.00` | `4935.40` | 357,829.92 USD | `+19.71%` | `25X Cross` |
| `1249` | `0xf83f...625f` | `SHORT` | 1,813,686.84 USD | `803.05` | `2601.00` | `2259.00` | `6128.70` | 275,049.61 USD | `+15.17%` | `20X Cross` |
| `1260` | `0x458d...ab3b` | `LONG` | 1,796,715.77 USD | `774.75` | `2740.41` | `2259.00` | `1888.01` | -326,413.42 USD | `-18.17%` | `3X Isolated` |
| `1327` | `0x51a0...3543` | `SHORT` | 1,665,585.89 USD | `724.55` | `2627.71` | `2259.00` | `7570.18` | 238,310.87 USD | `+14.31%` | `20X Cross` |
| `1337` | `0xaa53...9cb7` | `LONG` | 1,651,437.35 USD | `730.34` | `2389.70` | `2259.00` | `1973.95` | -93,852.29 USD | `-5.68%` | `20X Cross` |
| `1347` | `0x621c...63ab` | `LONG` | 1,644,675.85 USD | `728.28` | `2281.90` | `2259.00` | `0.000000` | -17,194.45 USD | `-1.05%` | `20X Cross` |
| `1362` | `0x5605...fe0f` | `SHORT` | 1,625,813.51 USD | `702.14` | `2566.90` | `2259.00` | `3072.22` | 176,519.14 USD | `+10.86%` | `20X Cross` |
| `1363` | `0xa189...94d7` | `SHORT` | 1,625,136.60 USD | `719.98` | `2691.84` | `2259.00` | `3051.96` | 312,936.06 USD | `+19.26%` | `25X Cross` |
| `1387` | `0x4b1c...bc38` | `SHORT` | 1,606,513.60 USD | `712.36` | `2529.31` | `2259.00` | `4440.62` | 195,270.38 USD | `+12.15%` | `10X Cross` |
| `1398` | `0x2f93...4404` | `LONG` | 1,597,399.90 USD | `707.47` | `1700.45` | `2259.00` | `1369.64` | 394,373.53 USD | `+24.69%` | `4X Isolated` |
| `1401` | `0xd911...961e` | `LONG` | 1,593,676.32 USD | `706.67` | `2268.18` | `2259.00` | `0.000000` | -9,178.17 USD | `-0.58%` | `25X Cross` |
| `1410` | `0x7743...e4fe` | `SHORT` | 1,581,435.57 USD | `700.56` | `2326.87` | `2259.00` | `6154.41` | 48,674.57 USD | `+3.08%` | `25X Cross` |
| `1422` | `0x71d0...8c26` | `LONG` | 1,568,096.04 USD | `695.32` | `2268.14` | `2259.00` | `0.000000` | -9,004.06 USD | `-0.57%` | `25X Cross` |
| `1428` | `0x07fd...082a` | `LONG` | 1,563,436.54 USD | `680.45` | `2308.98` | `2259.00` | `1968.63` | -7,705.84 USD | `-0.49%` | `25X Cross` |
| `1433` | `0x0b23...f37b` | `LONG` | 1,560,795.75 USD | `675.00` | `2238.15` | `2259.00` | `588.25` | 50,039.11 USD | `+3.21%` | `5X Cross` |
| `1441` | `0x3bca...66f3` | `SHORT` | 1,550,234.99 USD | `687.16` | `2313.35` | `2259.00` | `14196.38` | 39,413.15 USD | `+2.54%` | `25X Cross` |
| `1456` | `0xdbd1...29dd` | `SHORT` | 1,536,958.17 USD | `680.70` | `3030.57` | `2259.00` | `4105.97` | 525,962.95 USD | `+34.22%` | `6X Cross` |
| `1461` | `0x71e5...be04` | `LONG` | 1,528,274.17 USD | `677.67` | `2727.27` | `2259.00` | `1471.79` | -319,911.44 USD | `-20.93%` | `20X Cross` |
| `1471` | `0x0082...1ae3` | `LONG` | 1,515,030.00 USD | `660.00` | `2448.58` | `2259.00` | `2244.99` | -101,038.64 USD | `-6.67%` | `25X Cross` |
| `1495` | `0x0cac...6170` | `SHORT` | 1,484,832.25 USD | `657.50` | `2146.55` | `2259.00` | `2840.20` | -73,470.05 USD | `-4.95%` | `20X Cross` |
| `1499` | `0xffb2...5ed6` | `SHORT` | 1,481,638.66 USD | `640.77` | `2672.96` | `2259.00` | `2546.12` | 231,109.68 USD | `+15.60%` | `20X Cross` |
| `1522` | `0xfce0...f4c0` | `SHORT` | 1,444,257.60 USD | `623.60` | `3129.61` | `2259.00` | `2788.45` | 507,368.98 USD | `+35.13%` | `20X Cross` |
| `1557` | `0x72d0...62ea` | `LONG` | 1,413,480.66 USD | `626.24` | `2263.15` | `2259.00` | `109.09` | -3,794.21 USD | `-0.27%` | `5X Cross` |
| `1576` | `0x67c3...609d` | `SHORT` | 1,389,240.00 USD | `600.00` | `2386.55` | `2259.00` | `2560.80` | 42,691.89 USD | `+3.07%` | `25X Cross` |
| `1581` | `0x7663...cb5a` | `SHORT` | 1,385,675.12 USD | `613.54` | `2342.35` | `2259.00` | `3746.15` | 51,445.37 USD | `+3.71%` | `3X Cross` |
| `1589` | `0x26e6...6b28` | `LONG` | 1,377,300.00 USD | `600.00` | `1769.78` | `2259.00` | `2005.51` | 315,428.47 USD | `+22.90%` | `20X Cross` |
| `1593` | `0xb8eb...1dd5` | `LONG` | 1,370,140.22 USD | `607.55` | `2268.63` | `2259.00` | `0.000000` | -8,162.73 USD | `-0.60%` | `25X Cross` |
| `1603` | `0xad02...eb65` | `LONG` | 1,356,981.22 USD | `600.62` | `2460.69` | `2259.00` | `1079.70` | -120,959.34 USD | `-8.91%` | `5X Cross` |
| `1604` | `0x0deb...0bc5` | `LONG` | 1,356,720.00 USD | `600.00` | `2038.23` | `2259.00` | `1478.72` | 133,781.36 USD | `+9.86%` | `20X Cross` |
| `1605` | `0x638f...f5f0` | `LONG` | 1,354,980.00 USD | `600.00` | `4011.50` | `2259.00` | `342.52` | -1,051,923.53 USD | `-77.63%` | `25X Cross` |
| `1634` | `0x34fb...93de` | `LONG` | 1,319,337.68 USD | `584.81` | `2269.22` | `2259.00` | `0.000000` | -7,736.33 USD | `-0.59%` | `20X Cross` |
| `1638` | `0xca8e...507d` | `LONG` | 1,315,672.00 USD | `580.00` | `2253.46` | `2259.00` | `2069.76` | 8,661.65 USD | `+0.66%` | `10X Isolated` |
| `1642` | `0xfb99...37f3` | `LONG` | 1,310,856.41 USD | `565.34` | `2362.35` | `2259.00` | `1213.80` | -24,679.95 USD | `-1.88%` | `3X Cross` |
| `1658` | `0x844b...7f42` | `SHORT` | 1,297,144.20 USD | `561.00` | `2026.17` | `2259.00` | `3089.67` | -160,460.79 USD | `-12.37%` | `25X Cross` |
| `1697` | `0xabe6...1d99` | `SHORT` | 1,256,457.84 USD | `556.00` | `2484.68` | `2259.00` | `3074.06` | 125,038.05 USD | `+9.95%` | `20X Cross` |
| `1736` | `0x31de...13f2` | `LONG` | 1,206,522.75 USD | `535.00` | `2285.81` | `2259.00` | `0.000000` | -16,380.35 USD | `-1.36%` | `20X Cross` |
| `1746` | `0xad21...fb6a` | `LONG` | 1,199,897.14 USD | `531.87` | `2574.89` | `2259.00` | `1705.35` | -169,608.36 USD | `-14.14%` | `7X Cross` |
| `1753` | `0xf910...0a2d` | `LONG` | 1,194,604.25 USD | `529.71` | `2265.06` | `2259.00` | `0.000000` | -5,223.77 USD | `-0.44%` | `5X Cross` |
| `1801` | `0x7298...7d6c` | `SHORT` | 1,151,970.26 USD | `498.15` | `3426.75` | `2259.00` | `5422.42` | 555,065.57 USD | `+48.18%` | `20X Cross` |
| `1804` | `0x0c7a...2f50` | `SHORT` | 1,149,162.94 USD | `509.25` | `2122.56` | `2259.00` | `4111.24` | -68,257.51 USD | `-5.94%` | `20X Cross` |
| `1822` | `0xa559...ff95` | `LONG` | 1,131,720.00 USD | `500.00` | `2260.68` | `2259.00` | `1326.24` | 1,375.64 USD | `+0.12%` | `20X Cross` |
| `1824` | `0x89b2...9ca6` | `LONG` | 1,131,250.00 USD | `500.00` | `2484.03` | `2259.00` | `1954.23` | -110,769.35 USD | `-9.79%` | `25X Cross` |
| `1825` | `0x6463...42f5` | `LONG` | 1,128,900.00 USD | `500.00` | `2256.58` | `2259.00` | `0.000000` | 605.08 USD | `+0.05%` | `5X Cross` |
| `1826` | `0x321f...1c84` | `SHORT` | 1,128,389.21 USD | `488.02` | `2370.09` | `2259.00` | `3022.61` | 28,255.39 USD | `+2.50%` | `10X Cross` |
| `1852` | `0x404c...5f03` | `SHORT` | 1,106,082.14 USD | `489.79` | `2671.94` | `2259.00` | `4940.11` | 202,597.41 USD | `+18.32%` | `20X Cross` |
| `1853` | `0xc10f...23b3` | `LONG` | 1,105,440.00 USD | `490.00` | `2394.36` | `2259.00` | `2096.38` | -67,798.12 USD | `-6.13%` | `25X Cross` |
| `1908` | `0x82c6...fe42` | `LONG` | 1,061,622.50 USD | `462.50` | `2501.38` | `2259.00` | `2054.49` | -95,268.07 USD | `-8.97%` | `5X Isolated` |
| `1931` | `0xaf9f...a4fa` | `LONG` | 1,038,100.81 USD | `460.31` | `2268.76` | `2259.00` | `0.000000` | -6,244.51 USD | `-0.60%` | `20X Cross` |
| `1934` | `0x617e...0f97` | `SHORT` | 1,035,300.37 USD | `457.85` | `2205.60` | `2259.00` | `3828.75` | -25,456.53 USD | `-2.46%` | `10X Cross` |
| `1939` | `0x3ee5...4fab` | `SHORT` | 1,031,299.58 USD | `457.30` | `2759.35` | `2259.00` | `3579.76` | 230,549.71 USD | `+22.36%` | `20X Cross` |
| `1940` | `0x53f8...ceff` | `LONG` | 1,031,246.29 USD | `445.60` | `2399.81` | `2259.00` | `0.000000` | -38,104.31 USD | `-3.69%` | `20X Cross` |
| `1962` | `0xae55...2236` | `LONG` | 1,015,740.00 USD | `450.00` | `2510.21` | `2259.00` | `0.000000` | -113,857.50 USD | `-11.21%` | `25X Cross` |
| `1969` | `0x248e...6be2` | `SHORT` | 1,010,737.01 USD | `436.40` | `2314.49` | `2259.00` | `4423.77` | -702.29 USD | `-0.07%` | `20X Cross` |
| `1978` | `0xac26...a9c7` | `SHORT` | 1,006,800.69 USD | `446.28` | `2192.58` | `2259.00` | `8707.60` | -28,300.99 USD | `-2.81%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `2358.70` | 40,060.63 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.06K USD at 2358.7000 USD [API] | `2026-10-28 02:49:29` |
| `ANNOUNCEMENT` | `INFO` | `2358.30` | 40,591.06 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.59K USD at 2358.3000 USD [API] | `2026-10-28 02:58:44` |
| `ANNOUNCEMENT` | `INFO` | `2363.90` | 49,342.16 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 49.34K USD at 2363.9000 USD [API] | `2026-10-28 03:50:11` |
| `ANNOUNCEMENT` | `INFO` | `2362.10` | 54,053.59 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 54.05K USD at 2362.1000 USD [API] | `2026-10-28 03:54:16` |
| `ANNOUNCEMENT` | `INFO` | `2362.10` | 40,060.27 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 40.06K USD at 2362.1000 USD [API] | `2026-10-28 03:54:16` |
| `ANNOUNCEMENT` | `INFO` | `2362.10` | 95,323.96 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 95.32K USD at 2362.1000 USD [API] | `2026-10-28 03:54:16` |
| `ANNOUNCEMENT` | `INFO` | `2355.00` | 95,995.45 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 96.00K USD at 2355.0000 USD [API] | `2026-10-28 04:11:37` |
| `ANNOUNCEMENT` | `INFO` | `2368.70` | 851.55 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.85K USD at 2368.7000 USD [API] | `2026-10-25 02:38:02` |
| `ANNOUNCEMENT` | `INFO` | `2368.70` | 916.21 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.92K USD at 2368.7000 USD [API] | `2026-10-25 02:38:02` |
| `ANNOUNCEMENT` | `INFO` | `2333.60` | 1,022.82 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.02K USD at 2333.6000 USD [API] | `2026-10-24 18:29:59` |
| `ANNOUNCEMENT` | `INFO` | `2333.60` | 1,211.37 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.21K USD at 2333.6000 USD [API] | `2026-10-24 18:29:59` |
| `ANNOUNCEMENT` | `INFO` | `2360.40` | 59,588.77 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 59.59K USD at 2360.4000 USD [API] | `2026-10-23 22:53:38` |
| `ANNOUNCEMENT` | `INFO` | `2368.10` | 88.33 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.09K USD at 2368.1000 USD [API] | `2026-10-23 22:48:54` |
| `ANNOUNCEMENT` | `INFO` | `2368.10` | 700.25 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.70K USD at 2368.1000 USD [API] | `2026-10-23 22:48:54` |
| `ANNOUNCEMENT` | `INFO` | `2368.10` | 1,170.79 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.17K USD at 2368.1000 USD [API] | `2026-10-23 22:48:54` |
| `ANNOUNCEMENT` | `INFO` | `2368.10` | 1,856.12 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.86K USD at 2368.1000 USD [API] | `2026-10-23 22:48:54` |
| `ANNOUNCEMENT` | `INFO` | `2368.10` | 518.14 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.52K USD at 2368.1000 USD [API] | `2026-10-23 22:48:54` |
| `ANNOUNCEMENT` | `INFO` | `2402.20` | 7,572.46 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 7.57K USD at 2402.2000 USD [API] | `2026-10-22 09:03:55` |
| `ANNOUNCEMENT` | `INFO` | `2402.20` | 613.76 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.61K USD at 2402.2000 USD [API] | `2026-10-22 09:03:55` |
| `ANNOUNCEMENT` | `INFO` | `2403.00` | 698.55 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.70K USD at 2403.0000 USD [API] | `2026-10-22 09:03:52` |
| `ANNOUNCEMENT` | `INFO` | `2357.80` | 299,004.41 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 299.00K USD at 2357.8000 USD [API] | `2026-10-28 04:33:41` |
| `ANNOUNCEMENT` | `INFO` | `2357.80` | 75,685.38 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 75.69K USD at 2357.8000 USD [API] | `2026-10-28 04:33:41` |
| `ANNOUNCEMENT` | `INFO` | `2357.80` | 401,086.30 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 401.09K USD at 2357.8000 USD [API] | `2026-10-28 04:33:41` |
| `ANNOUNCEMENT` | `INFO` | `2356.90` | 40,997.80 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 41.00K USD at 2356.9000 USD [API] | `2026-10-28 04:38:32` |
| `ANNOUNCEMENT` | `INFO` | `2412.30` | 18,405.85 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 18.41K USD at 2412.3000 USD [API] | `2026-10-18 23:27:51` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 8,952.63 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 8.95K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 2,202.60 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 2.20K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 864.80 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.86K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 1,940.50 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.94K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 257.42 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.26K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 121.82 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.12K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 603.68 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.60K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 22.40 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.10` | 7,183.46 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 7.18K USD at 2461.1000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2479.30` | 27,091.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 27.09K USD at 2479.3000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2355.90` | 40,059.72 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.06K USD at 2355.9000 USD [API] | `2026-10-28 04:50:04` |
| `ANNOUNCEMENT` | `INFO` | `2356.30` | 59,045.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 59.05K USD at 2356.3000 USD [API] | `2026-10-28 05:25:04` |
| `ANNOUNCEMENT` | `INFO` | `2352.60` | 62,319.90 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 62.32K USD at 2352.6000 USD [API] | `2026-10-28 05:41:41` |
| `ANNOUNCEMENT` | `INFO` | `2351.50` | 43,963.64 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 43.96K USD at 2351.5000 USD [API] | `2026-10-28 05:47:15` |
| `ANNOUNCEMENT` | `INFO` | `2351.50` | 196,291.46 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 196.29K USD at 2351.5000 USD [API] | `2026-10-28 05:47:15` |
| `ANNOUNCEMENT` | `INFO` | `2351.50` | 125,986.08 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 125.99K USD at 2351.5000 USD [API] | `2026-10-28 05:47:15` |
| `ANNOUNCEMENT` | `INFO` | `2353.50` | 45,509.63 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 45.51K USD at 2353.5000 USD [API] | `2026-10-28 07:28:55` |
| `ANNOUNCEMENT` | `INFO` | `2108.70` | 16,062.60 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 16.06K USD at 2108.7000 USD [API] | `2026-04-05 23:15:08` |
| `ANNOUNCEMENT` | `INFO` | `1825.00` | 900.82 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.90K USD at 1825.0000 USD [API] | `2026-02-05 22:17:53` |
| `ANNOUNCEMENT` | `INFO` | `1921.90` | 4,169.18 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 4.17K USD at 1921.9000 USD [API] | `2026-02-05 18:32:59` |
| `ANNOUNCEMENT` | `INFO` | `2464.20` | 1,791.47 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.79K USD at 2464.2000 USD [API] | `2026-01-31 17:06:07` |
| `ANNOUNCEMENT` | `INFO` | `2464.20` | 278.70 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.28K USD at 2464.2000 USD [API] | `2026-01-31 17:06:07` |
| `ANNOUNCEMENT` | `INFO` | `2556.30` | 6,274.95 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 6.27K USD at 2556.3000 USD [API] | `2026-01-31 14:26:23` |
| `ANNOUNCEMENT` | `INFO` | `2629.80` | 1,391.69 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.39K USD at 2629.8000 USD [API] | `2026-01-31 08:37:08` |
| `ANNOUNCEMENT` | `INFO` | `2629.80` | 1,050.34 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.05K USD at 2629.8000 USD [API] | `2026-01-31 08:37:08` |
| `ANNOUNCEMENT` | `INFO` | `2629.80` | 5,410.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 5.41K USD at 2629.8000 USD [API] | `2026-01-31 08:37:08` |
| `ANNOUNCEMENT` | `INFO` | `2629.80` | 10,256.22 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 10.26K USD at 2629.8000 USD [API] | `2026-01-31 08:37:08` |
| `ANNOUNCEMENT` | `INFO` | `2629.80` | 1,274.66 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.27K USD at 2629.8000 USD [API] | `2026-01-31 08:37:08` |
| `ANNOUNCEMENT` | `INFO` | `2643.60` | 112.88 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.11K USD at 2643.6000 USD [API] | `2026-01-30 18:22:38` |
| `ANNOUNCEMENT` | `INFO` | `2643.60` | 1,984.02 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.98K USD at 2643.6000 USD [API] | `2026-01-30 18:22:38` |
| `ANNOUNCEMENT` | `INFO` | `2643.60` | 12,775.20 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 12.78K USD at 2643.6000 USD [API] | `2026-01-30 18:22:38` |
| `ANNOUNCEMENT` | `INFO` | `2643.60` | 2,252.61 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 2.25K USD at 2643.6000 USD [API] | `2026-01-30 18:22:38` |
| `ANNOUNCEMENT` | `INFO` | `2643.60` | 1,890.70 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.89K USD at 2643.6000 USD [API] | `2026-01-30 18:22:38` |
| `ANNOUNCEMENT` | `INFO` | `2782.10` | 75,046.59 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 75.05K USD at 2782.1000 USD [API] | `2026-01-29 18:30:51` |
| `ANNOUNCEMENT` | `INFO` | `2941.40` | 27,825.94 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 27.83K USD at 2941.4000 USD [API] | `2026-01-26 15:10:57` |
| `ANNOUNCEMENT` | `INFO` | `2941.40` | 64.42 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.06K USD at 2941.4000 USD [API] | `2026-01-26 15:10:57` |
| `ANNOUNCEMENT` | `INFO` | `2941.40` | 2,001.92 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.00K USD at 2941.4000 USD [API] | `2026-01-26 15:10:57` |
| `ANNOUNCEMENT` | `INFO` | `2941.40` | 1,986.62 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.99K USD at 2941.4000 USD [API] | `2026-01-26 15:10:57` |
| `ANNOUNCEMENT` | `INFO` | `2941.40` | 20,295.37 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 20.30K USD at 2941.4000 USD [API] | `2026-01-26 15:10:57` |
| `ANNOUNCEMENT` | `INFO` | `2941.40` | 17,554.28 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 17.55K USD at 2941.4000 USD [API] | `2026-01-26 15:10:57` |
| `ANNOUNCEMENT` | `INFO` | `2941.40` | 2,719.91 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.72K USD at 2941.4000 USD [API] | `2026-01-26 15:10:57` |
| `ANNOUNCEMENT` | `INFO` | `2941.40` | 16,063.28 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 16.06K USD at 2941.4000 USD [API] | `2026-01-26 15:10:57` |
| `ANNOUNCEMENT` | `INFO` | `2941.40` | 7,763.24 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 7.76K USD at 2941.4000 USD [API] | `2026-01-26 15:10:57` |
| `ANNOUNCEMENT` | `INFO` | `2945.80` | 24,104.60 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 24.10K USD at 2945.8000 USD [API] | `2026-01-26 15:10:54` |
| `ANNOUNCEMENT` | `INFO` | `3261.40` | 12,277.87 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 12.28K USD at 3261.4000 USD [API] | `2026-01-13 22:08:58` |
| `ANNOUNCEMENT` | `INFO` | `3299.60` | 3,192.69 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 3.19K USD at 3299.6000 USD [API] | `2026-01-06 14:23:46` |
| `ANNOUNCEMENT` | `INFO` | `3254.00` | 6,635.23 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 6.64K USD at 3254.0000 USD [API] | `2026-01-05 20:28:13` |
| `ANNOUNCEMENT` | `INFO` | `3212.10` | 16,963.42 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 16.96K USD at 3212.1000 USD [API] | `2026-01-05 01:37:45` |
| `ANNOUNCEMENT` | `INFO` | `2375.20` | 263,683.54 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 263.68K USD at 2375.2000 USD [API] | `2026-10-28 08:26:36` |
| `ANNOUNCEMENT` | `INFO` | `2375.20` | 29.45 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.03K USD at 2375.2000 USD [API] | `2026-10-28 08:26:36` |
| `ANNOUNCEMENT` | `INFO` | `2375.20` | 148.69 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.15K USD at 2375.2000 USD [API] | `2026-10-28 08:26:36` |
| `ANNOUNCEMENT` | `INFO` | `2375.20` | 12.35 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.01K USD at 2375.2000 USD [API] | `2026-10-28 08:26:36` |
| `ANNOUNCEMENT` | `INFO` | `2373.30` | 62,975.99 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 62.98K USD at 2373.3000 USD [API] | `2026-10-28 08:34:05` |
| `ANNOUNCEMENT` | `INFO` | `2381.80` | 61.69 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.06K USD at 2381.8000 USD [API] | `2026-10-28 08:35:59` |
| `ANNOUNCEMENT` | `INFO` | `2381.80` | 12.39 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.01K USD at 2381.8000 USD [API] | `2026-10-28 08:35:59` |
| `ANNOUNCEMENT` | `INFO` | `2381.80` | 131.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.13K USD at 2381.8000 USD [API] | `2026-10-28 08:35:59` |
| `ANNOUNCEMENT` | `INFO` | `2379.60` | 1,280.70 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.28K USD at 2379.6000 USD [API] | `2026-10-28 08:35:40` |
| `ANNOUNCEMENT` | `INFO` | `2379.60` | 27.84 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.03K USD at 2379.6000 USD [API] | `2026-10-28 08:35:40` |
| `ANNOUNCEMENT` | `INFO` | `2379.60` | 1,942.94 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.94K USD at 2379.6000 USD [API] | `2026-10-28 08:35:40` |
| `ANNOUNCEMENT` | `INFO` | `2377.40` | 133,818.85 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 133.82K USD at 2377.4000 USD [API] | `2026-10-28 08:38:08` |
| `ANNOUNCEMENT` | `INFO` | `2377.40` | 133,369.05 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 133.37K USD at 2377.4000 USD [API] | `2026-10-28 08:38:08` |
| `ANNOUNCEMENT` | `INFO` | `2377.40` | 114,509.85 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 114.51K USD at 2377.4000 USD [API] | `2026-10-28 08:38:08` |
| `ANNOUNCEMENT` | `INFO` | `2375.60` | 256,016.04 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 256.02K USD at 2375.6000 USD [API] | `2026-10-28 08:26:36` |
| `ANNOUNCEMENT` | `INFO` | `2375.60` | 192,432.63 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 192.43K USD at 2375.6000 USD [API] | `2026-10-28 08:26:36` |
| `ANNOUNCEMENT` | `INFO` | `2378.90` | 122.28 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.12K USD at 2378.9000 USD [API] | `2026-10-28 08:35:38` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 24.71 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2375.8000 USD [API] | `2026-10-28 08:26:39` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 1,544.98 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.54K USD at 2375.8000 USD [API] | `2026-10-28 08:26:39` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 54.88 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.05K USD at 2375.8000 USD [API] | `2026-10-28 08:26:39` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 1,207.14 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.21K USD at 2375.8000 USD [API] | `2026-10-28 08:26:39` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 15.44 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2375.8000 USD [API] | `2026-10-28 08:26:39` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 26,474.01 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 26.47K USD at 2375.8000 USD [API] | `2026-10-28 08:26:39` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 3,350.83 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 3.35K USD at 2375.8000 USD [API] | `2026-10-28 08:26:39` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 12.35 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.01K USD at 2375.8000 USD [API] | `2026-10-28 08:26:39` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 3,029.62 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 3.03K USD at 2375.8000 USD [API] | `2026-10-28 08:26:39` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 25.42 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.03K USD at 2375.8000 USD [API] | `2026-10-28 08:26:39` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 119.50 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.12K USD at 2375.8000 USD [API] | `2026-10-28 08:26:39` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 74.36 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.07K USD at 2375.8000 USD [API] | `2026-10-28 08:26:39` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 89.09 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.09K USD at 2375.8000 USD [API] | `2026-10-28 08:26:39` |
| `ANNOUNCEMENT` | `INFO` | `2367.90` | 59,163.64 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 59.16K USD at 2367.9000 USD [API] | `2026-10-28 09:21:32` |
| `ANNOUNCEMENT` | `INFO` | `2372.20` | 228,334.69 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 228.33K USD at 2372.2000 USD [API] | `2026-10-28 09:58:22` |
| `ANNOUNCEMENT` | `INFO` | `2372.50` | 120,157.40 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 120.16K USD at 2372.5000 USD [API] | `2026-10-28 09:59:38` |
| `ANNOUNCEMENT` | `INFO` | `2372.40` | 73,511.19 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 73.51K USD at 2372.4000 USD [API] | `2026-10-28 10:00:58` |
| `ANNOUNCEMENT` | `INFO` | `2372.40` | 40,053.70 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.05K USD at 2372.4000 USD [API] | `2026-10-28 10:00:58` |
| `ANNOUNCEMENT` | `INFO` | `2371.00` | 89,100.76 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 89.10K USD at 2371.0000 USD [API] | `2026-10-28 10:25:19` |
| `ANNOUNCEMENT` | `INFO` | `2371.00` | 60,980.70 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 60.98K USD at 2371.0000 USD [API] | `2026-10-28 10:25:19` |
| `ANNOUNCEMENT` | `INFO` | `2362.60` | 110,112.52 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 110.11K USD at 2362.6000 USD [API] | `2026-10-28 11:06:26` |
| `ANNOUNCEMENT` | `INFO` | `2362.60` | 83,017.98 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 83.02K USD at 2362.6000 USD [API] | `2026-10-28 11:06:26` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2403.57` (Vol: 16,800,000.00 USD, Dist: `+3.87%`) | Long MP=`2294.75` (Vol: 27,100,000.00 USD, Dist: `--0.83%`)
  * 48H Horizon: Short MP=`2401.93` (Vol: 25,300,000.00 USD, Dist: `+3.80%`) | Long MP=`2284.33` (Vol: 30,000,000.00 USD, Dist: `--1.28%`)
  * 3D Horizon: Short MP=`2401.93` (Vol: 26,700,000.00 USD, Dist: `+3.80%`) | Long MP=`2286.29` (Vol: 37,900,000.00 USD, Dist: `--1.20%`)
  * 7D Horizon: Short MP=`2402.93` (Vol: 47,100,000.00 USD, Dist: `+3.84%`) | Long MP=`2284.60` (Vol: 72,300,000.00 USD, Dist: `--1.27%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `455.00` | 81,350.00 USD | 871,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `465.00` | 8,890.00 USD | 871,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 18,650.00 USD | 871,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 10,700.00 USD | 871,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 3,170.00 USD | 871,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 40,200.00 USD | 871,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 8,310.00 USD | 871,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 5,110.00 USD | 871,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 16,270.00 USD | 871,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 22,070.00 USD | 871,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 144,570.00 USD | 871,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 113,200.00 USD | 871,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 17,490.00 USD | 871,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 396,730.00 USD | 871,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 8,390.00 USD | 870,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 21,280.00 USD | 870,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 90,210.00 USD | 870,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 12,690.00 USD | 870,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 2,240.00 USD | 870,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 4,850.00 USD | 870,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 54,920.00 USD | 870,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 99,080.00 USD | 870,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 123,080.00 USD | 870,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 35,700.00 USD | 870,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 107,880.00 USD | 870,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 4,070.00 USD | 870,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 15,690.00 USD | 870,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 383,190.00 USD | 870,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 52,700.00 USD | 869,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 1,820.00 USD | 869,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 27,110.00 USD | 869,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 87,060.00 USD | 869,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 1,710,000.00 USD | 869,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 62,570.00 USD | 867,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 468,490.00 USD | 867,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 2,400.00 USD | 867,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 444,920.00 USD | 867,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 93,820.00 USD | 866,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 264,560.00 USD | 866,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 19,780.00 USD | 866,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 5,300.00 USD | 866,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 3,780,000.00 USD | 866,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 35,210.00 USD | 862,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 422,370.00 USD | 862,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 28,550.00 USD | 862,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 77,340.00 USD | 862,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 233,800.00 USD | 862,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 131,200.00 USD | 861,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 31,510.00 USD | 861,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 23,750.00 USD | 861,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 1,140,000.00 USD | 861,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 23,360.00 USD | 860,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 74,510.00 USD | 860,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 21,080.00 USD | 860,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 54,120.00 USD | 860,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 7,080,000.00 USD | 860,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 63,250.00 USD | 853,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 122,850.00 USD | 853,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 29,510.00 USD | 853,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 1,900,000.00 USD | 853,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 31,060.00 USD | 851,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 1,500,000.00 USD | 851,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 872,800.00 USD | 849,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 35,080.00 USD | 848,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 117,660.00 USD | 848,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 144,030.00 USD | 848,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 145,270.00 USD | 848,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 1,760,000.00 USD | 848,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 76,690.00 USD | 846,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 217,980.00 USD | 846,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 345,860.00 USD | 846,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 14,960.00 USD | 845,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 337,640.00 USD | 845,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 123,330.00 USD | 845,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 305,420.00 USD | 845,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 1,230,000.00 USD | 845,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 118,830.00 USD | 843,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 250,230.00 USD | 843,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 247,580.00 USD | 843,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 11,610,000.00 USD | 843,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 439,960.00 USD | 831,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 1,550,000.00 USD | 831,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 94,640.00 USD | 829,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 16,260,000.00 USD | 829,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 413,680.00 USD | 813,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 160,590.00 USD | 812,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 92,010.00 USD | 812,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 565,280.00 USD | 812,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 410,380.00 USD | 812,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 569,800.00 USD | 811,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 112,370.00 USD | 811,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 7,800,000.00 USD | 811,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 343,870.00 USD | 803,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 136,090.00 USD | 802,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 321,060.00 USD | 802,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 25,310,000.00 USD | 802,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 60,360.00 USD | 777,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 1,110,000.00 USD | 777,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 14,830,000.00 USD | 775,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 164,980.00 USD | 761,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 7,350,000.00 USD | 760,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 413,140.00 USD | 753,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 2,070,000.00 USD | 753,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 5,120,000.00 USD | 751,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 510,410.00 USD | 746,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 457,390.00 USD | 745,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 18,940,000.00 USD | 745,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 18,620,000.00 USD | 726,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 646,040.00 USD | 707,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 27,510,000.00 USD | 706,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 974,100.00 USD | 679,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 264,610.00 USD | 678,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 204,780.00 USD | 678,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 262,710.00 USD | 677,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 7,660,000.00 USD | 677,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 18,380,000.00 USD | 669,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 278,310.00 USD | 651,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 3,020,000.00 USD | 651,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 18,260,000.00 USD | 648,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 36,410,000.00 USD | 630,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 997,270.00 USD | 593,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 845,700.00 USD | 592,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 11,660,000.00 USD | 591,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 2,030,000.00 USD | 580,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 444,640.00 USD | 578,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 1,240,000.00 USD | 577,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 11,040,000.00 USD | 576,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 18,000,000.00 USD | 565,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 18,130,000.00 USD | 547,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 2,120,000.00 USD | 529,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 968,460.00 USD | 527,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 1,060,000.00 USD | 526,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 14,310,000.00 USD | 525,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 54,670,000.00 USD | 510,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 337,900.00 USD | 456,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 1,610,000.00 USD | 455,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 4,520,000.00 USD | 454,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 9,600,000.00 USD | 449,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 1,310,000.00 USD | 440,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 290,390.00 USD | 438,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 1,020,000.00 USD | 438,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 6,820,000.00 USD | 437,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 5,580,000.00 USD | 430,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 2,730,000.00 USD | 425,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 5,510,000.00 USD | 422,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 1,280,000.00 USD | 416,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 30,800,000.00 USD | 415,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 2,930,000.00 USD | 384,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 1,570,000.00 USD | 381,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 789,440.00 USD | 380,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 3,430,000.00 USD | 379,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 748,720.00 USD | 375,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1975.00` | 6,210,000.00 USD | 375,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1985.00` | 4,430,000.00 USD | 369,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1995.00` | 926,340.00 USD | 364,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2005.00` | 2,840,000.00 USD | 363,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2015.00` | 3,290,000.00 USD | 360,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2017.30` | 319,390,000.00 USD | 319,390,000.00 USD | 83,300.00 USD | 176,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2020.30` | 319,130,000.00 USD | 319,130,000.00 USD | 0.00 USD | 558,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,470,000.00 USD | 357,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2025.30` | 700,940,000.00 USD | 700,940,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.60` | 700,760,000.00 USD | 700,760,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2029.30` | 318,570,000.00 USD | 318,570,000.00 USD | 0.00 USD | 0.00 USD | 43,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.90` | 699,580,000.00 USD | 699,580,000.00 USD | 0.00 USD | 201,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.30` | 318,530,000.00 USD | 318,530,000.00 USD | 937,190.00 USD | 1,470,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 1,050,000.00 USD | 356,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2035.20` | 699,380,000.00 USD | 699,380,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2035.30` | 316,130,000.00 USD | 316,130,000.00 USD | 167,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2038.30` | 315,960,000.00 USD | 315,960,000.00 USD | 138,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.50` | 699,050,000.00 USD | 699,050,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2041.30` | 315,820,000.00 USD | 315,820,000.00 USD | 0.00 USD | 134,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 20,110,000.00 USD | 355,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2045.10` | 697,590,000.00 USD | 697,590,000.00 USD | 0.00 USD | 149,500.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2053.30` | 315,690,000.00 USD | 315,690,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 4,320,000.00 USD | 334,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2056.30` | 315,660,000.00 USD | 315,660,000.00 USD | 0.00 USD | 88,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2058.30` | 697,400,000.00 USD | 697,400,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.60` | 697,050,000.00 USD | 697,050,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2062.30` | 315,570,000.00 USD | 315,570,000.00 USD | 80,610.00 USD | 121,470.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.90` | 692,610,000.00 USD | 692,610,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 1,360,000.00 USD | 330,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2065.30` | 315,320,000.00 USD | 315,320,000.00 USD | 984,680.00 USD | 537,030.00 USD | 598,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2068.20` | 690,090,000.00 USD | 690,090,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2068.30` | 313,200,000.00 USD | 313,200,000.00 USD | 444,700.00 USD | 1,330,000.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2071.30` | 311,370,000.00 USD | 311,370,000.00 USD | 1,040,000.00 USD | 534,600.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.50` | 685,590,000.00 USD | 685,590,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2074.30` | 309,360,000.00 USD | 309,360,000.00 USD | 614,280.00 USD | 62,630.00 USD | 930,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.80` | 679,130,000.00 USD | 679,130,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 921,260.00 USD | 329,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2077.30` | 307,750,000.00 USD | 307,750,000.00 USD | 3,000,000.00 USD | 1,520,000.00 USD | 2,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.10` | 667,430,000.00 USD | 667,430,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2080.30` | 301,050,000.00 USD | 301,050,000.00 USD | 1,670,000.00 USD | 1,590,000.00 USD | 280,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.40` | 655,140,000.00 USD | 655,140,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2083.30` | 297,510,000.00 USD | 297,510,000.00 USD | 2,180,000.00 USD | 1,420,000.00 USD | 775,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.70` | 644,500,000.00 USD | 644,500,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 2,640,000.00 USD | 328,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2086.30` | 293,140,000.00 USD | 293,140,000.00 USD | 1,580,000.00 USD | 1,500,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.00` | 635,710,000.00 USD | 635,710,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2089.30` | 288,420,000.00 USD | 288,420,000.00 USD | 1,470,000.00 USD | 430,310.00 USD | 228,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.30` | 627,280,000.00 USD | 627,280,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.30` | 286,290,000.00 USD | 286,290,000.00 USD | 1,150,000.00 USD | 514,440.00 USD | 957,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.60` | 614,330,000.00 USD | 614,330,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,420,000.00 USD | 325,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2095.30` | 283,670,000.00 USD | 283,670,000.00 USD | 2,180,000.00 USD | 1,320,000.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.90` | 604,110,000.00 USD | 604,110,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2098.30` | 278,060,000.00 USD | 278,060,000.00 USD | 474,990.00 USD | 1,170,000.00 USD | 309,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.20` | 597,270,000.00 USD | 597,270,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2101.30` | 276,110,000.00 USD | 276,110,000.00 USD | 207,380.00 USD | 44,780.00 USD | 304,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2104.30` | 275,550,000.00 USD | 275,550,000.00 USD | 1,070,000.00 USD | 961,080.00 USD | 190,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2104.50` | 590,670,000.00 USD | 590,670,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,220,000.00 USD | 324,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2107.30` | 273,330,000.00 USD | 273,330,000.00 USD | 546,100.00 USD | 0.00 USD | 502,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.80` | 585,230,000.00 USD | 585,230,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.30` | 272,280,000.00 USD | 272,280,000.00 USD | 118,210.00 USD | 31,550.00 USD | 196,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2111.10` | 580,750,000.00 USD | 580,750,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2113.30` | 271,930,000.00 USD | 271,930,000.00 USD | 911,810.00 USD | 643,210.00 USD | 224,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2114.40` | 572,700,000.00 USD | 572,700,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 20,470,000.00 USD | 323,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2116.30` | 270,150,000.00 USD | 270,150,000.00 USD | 0.00 USD | 13,230.00 USD | 426,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.70` | 565,970,000.00 USD | 565,970,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2119.30` | 269,710,000.00 USD | 269,710,000.00 USD | 218,200.00 USD | 256,720.00 USD | 937,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2121.00` | 557,140,000.00 USD | 557,140,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2122.30` | 268,300,000.00 USD | 268,300,000.00 USD | 926,060.00 USD | 689,080.00 USD | 1,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.30` | 550,330,000.00 USD | 550,330,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 1,030,000.00 USD | 302,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.30` | 265,370,000.00 USD | 265,370,000.00 USD | 1,010,000.00 USD | 1,130,000.00 USD | 707,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.60` | 547,010,000.00 USD | 547,010,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.30` | 262,520,000.00 USD | 262,520,000.00 USD | 365,910.00 USD | 1,040,000.00 USD | 301,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.90` | 538,710,000.00 USD | 538,710,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2131.30` | 260,820,000.00 USD | 260,820,000.00 USD | 0.00 USD | 644,330.00 USD | 654,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.20` | 532,290,000.00 USD | 532,290,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2134.30` | 259,520,000.00 USD | 259,520,000.00 USD | 0.00 USD | 312,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 3,440,000.00 USD | 301,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2137.30` | 259,210,000.00 USD | 259,210,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.50` | 529,260,000.00 USD | 529,260,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.80` | 527,300,000.00 USD | 527,300,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.10` | 523,370,000.00 USD | 523,370,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 9,300,000.00 USD | 298,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2147.40` | 521,520,000.00 USD | 521,520,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.70` | 520,440,000.00 USD | 520,440,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2152.30` | 258,930,000.00 USD | 258,930,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.00` | 519,480,000.00 USD | 519,480,000.00 USD | 128,430.00 USD | 331,520.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 23,380,000.00 USD | 288,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2155.30` | 258,280,000.00 USD | 258,280,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2157.30` | 518,990,000.00 USD | 518,990,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2158.30` | 256,880,000.00 USD | 256,880,000.00 USD | 0.00 USD | 0.00 USD | 37,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.60` | 516,500,000.00 USD | 516,500,000.00 USD | 646,940.00 USD | 1,900,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2161.30` | 256,850,000.00 USD | 256,850,000.00 USD | 0.00 USD | 860,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.90` | 511,950,000.00 USD | 511,950,000.00 USD | 566,120.00 USD | 3,280,000.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2164.30` | 255,990,000.00 USD | 255,990,000.00 USD | 0.00 USD | 0.00 USD | 55,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 904,350.00 USD | 265,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2167.20` | 506,900,000.00 USD | 506,900,000.00 USD | 25,540.00 USD | 503,000.00 USD | 50,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.30` | 255,930,000.00 USD | 255,930,000.00 USD | 2,340,000.00 USD | 341,240.00 USD | 52,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.30` | 253,190,000.00 USD | 253,190,000.00 USD | 2,860,000.00 USD | 3,520,000.00 USD | 873,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.50` | 506,320,000.00 USD | 506,320,000.00 USD | 3,500,000.00 USD | 1,190,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2173.30` | 245,940,000.00 USD | 245,940,000.00 USD | 0.00 USD | 190,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.80` | 499,800,000.00 USD | 499,800,000.00 USD | 4,110,000.00 USD | 363,040.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 109,710,000.00 USD | 264,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2176.30` | 245,750,000.00 USD | 245,750,000.00 USD | 345,940.00 USD | 1,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2179.30` | 244,000,000.00 USD | 244,000,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2180.40` | 494,310,000.00 USD | 494,310,000.00 USD | 0.00 USD | 373,740.00 USD | 119,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 112,420,000.00 USD | 154,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2191.30` | 242,820,000.00 USD | 242,820,000.00 USD | 0.00 USD | 222,200.00 USD | 70,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 909,930.00 USD | 42,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2196.90` | 493,820,000.00 USD | 493,820,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2197.30` | 242,530,000.00 USD | 242,530,000.00 USD | 416,500.00 USD | 881,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.20` | 490,770,000.00 USD | 490,770,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.30` | 241,230,000.00 USD | 241,230,000.00 USD | 284,470.00 USD | 3,100,000.00 USD | 220,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.30` | 237,630,000.00 USD | 237,630,000.00 USD | 3,540,000.00 USD | 1,410,000.00 USD | 2,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.50` | 479,490,000.00 USD | 479,490,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 1,470,000.00 USD | 41,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2206.30` | 230,580,000.00 USD | 230,580,000.00 USD | 755,060.00 USD | 6,310,000.00 USD | 802,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2206.80` | 470,380,000.00 USD | 470,380,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2209.30` | 222,710,000.00 USD | 222,710,000.00 USD | 2,720,000.00 USD | 2,010,000.00 USD | 3,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2210.10` | 450,010,000.00 USD | 450,010,000.00 USD | 12,800,000.00 USD | 14,160,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.30` | 214,940,000.00 USD | 214,940,000.00 USD | 7,970,000.00 USD | 2,320,000.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2213.40` | 416,750,000.00 USD | 416,750,000.00 USD | 10,920,000.00 USD | 11,890,000.00 USD | 13,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 1,830,000.00 USD | 39,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2215.30` | 201,600,000.00 USD | 201,600,000.00 USD | 13,360,000.00 USD | 12,530,000.00 USD | 7,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2216.70` | 380,770,000.00 USD | 380,770,000.00 USD | 25,210,000.00 USD | 14,660,000.00 USD | 9,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2218.30` | 168,460,000.00 USD | 168,460,000.00 USD | 7,390,000.00 USD | 7,700,000.00 USD | 2,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2220.00` | 331,510,000.00 USD | 331,510,000.00 USD | 24,310,000.00 USD | 12,300,000.00 USD | 10,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2221.30` | 151,100,000.00 USD | 151,100,000.00 USD | 6,130,000.00 USD | 12,360,000.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2223.30` | 284,780,000.00 USD | 284,780,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2224.30` | 131,350,000.00 USD | 131,350,000.00 USD | 9,430,000.00 USD | 5,550,000.00 USD | 5,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 1,590,000.00 USD | 38,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2226.60` | 254,500,000.00 USD | 254,500,000.00 USD | 12,840,000.00 USD | 11,030,000.00 USD | 9,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.30` | 110,820,000.00 USD | 110,820,000.00 USD | 5,860,000.00 USD | 3,900,000.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.90` | 220,790,000.00 USD | 220,790,000.00 USD | 12,730,000.00 USD | 9,180,000.00 USD | 20,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.30` | 98,450,000.00 USD | 98,450,000.00 USD | 4,210,000.00 USD | 5,550,000.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2233.20` | 178,220,000.00 USD | 178,220,000.00 USD | 15,490,000.00 USD | 11,810,000.00 USD | 9,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2233.30` | 86,380,000.00 USD | 86,380,000.00 USD | 6,390,000.00 USD | 2,520,000.00 USD | 5,380,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2235.00` | 1,290,000.00 USD | 36,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2236.30` | 72,080,000.00 USD | 72,080,000.00 USD | 18,610,000.00 USD | 0.00 USD | 4,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2236.50` | 140,960,000.00 USD | 140,960,000.00 USD | 10,580,000.00 USD | 2,010,000.00 USD | 5,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2239.30` | 49,090,000.00 USD | 49,090,000.00 USD | 6,170,000.00 USD | 783,290.00 USD | 4,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.80` | 122,540,000.00 USD | 122,540,000.00 USD | 15,710,000.00 USD | 1,860,000.00 USD | 13,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2242.30` | 37,800,000.00 USD | 37,800,000.00 USD | 2,420,000.00 USD | 760,920.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2243.10` | 91,230,000.00 USD | 91,230,000.00 USD | 22,920,000.00 USD | 0.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 4,640,000.00 USD | 35,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2245.30` | 33,160,000.00 USD | 33,160,000.00 USD | 2,360,000.00 USD | 4,260,000.00 USD | 482,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2246.40` | 59,340,000.00 USD | 59,340,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2248.30` | 26,060,000.00 USD | 26,060,000.00 USD | 8,900,000.00 USD | 0.00 USD | 4,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2249.70` | 31,080,000.00 USD | 31,080,000.00 USD | 18,000,000.00 USD | 0.00 USD | 13,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2251.30` | 13,060,000.00 USD | 13,060,000.00 USD | 4,190,000.00 USD | 506,110.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2253.00` | 44,620,000.00 USD | 44,620,000.00 USD | 26,890,000.00 USD | 0.00 USD | 17,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2254.30` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 5,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 10,910,000.00 USD | 30,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2256.30` | 63,150,000.00 USD | 63,150,000.00 USD | 15,220,000.00 USD | 0.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2265.00` | 3,260,000.00 USD | 19,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2266.30` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 4,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2269.30` | 12,840,000.00 USD | 12,840,000.00 USD | 0.00 USD | 0.00 USD | 7,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2269.50` | 67,510,000.00 USD | 67,510,000.00 USD | 0.00 USD | 4,370,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2272.30` | 33,060,000.00 USD | 33,060,000.00 USD | 0.00 USD | 0.00 USD | 20,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2272.80` | 98,780,000.00 USD | 98,780,000.00 USD | 0.00 USD | 31,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2275.00` | 6,850,000.00 USD | 16,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2275.30` | 59,740,000.00 USD | 59,740,000.00 USD | 1,020,000.00 USD | 21,680,000.00 USD | 3,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2276.10` | 156,280,000.00 USD | 156,280,000.00 USD | 3,340,000.00 USD | 54,160,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2278.30` | 99,940,000.00 USD | 99,940,000.00 USD | 5,630,000.00 USD | 15,600,000.00 USD | 18,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2279.40` | 326,780,000.00 USD | 326,780,000.00 USD | 77,990,000.00 USD | 55,080,000.00 USD | 37,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2281.30` | 189,030,000.00 USD | 189,030,000.00 USD | 41,300,000.00 USD | 26,130,000.00 USD | 21,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.70` | 549,710,000.00 USD | 549,710,000.00 USD | 78,190,000.00 USD | 76,930,000.00 USD | 67,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2284.30` | 249,990,000.00 USD | 249,990,000.00 USD | 29,150,000.00 USD | 16,670,000.00 USD | 15,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2285.00` | 4,100,000.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2286.00` | 690,170,000.00 USD | 690,170,000.00 USD | 89,380,000.00 USD | 9,400,000.00 USD | 41,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2287.30` | 252,550,000.00 USD | 252,550,000.00 USD | 1,800,000.00 USD | 760,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2289.30` | 778,460,000.00 USD | 778,460,000.00 USD | 84,260,000.00 USD | 0.00 USD | 4,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2290.30` | 260,950,000.00 USD | 260,950,000.00 USD | 0.00 USD | 8,390,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2292.60` | 811,940,000.00 USD | 811,940,000.00 USD | 33,480,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2293.30` | 265,740,000.00 USD | 265,740,000.00 USD | 4,720,000.00 USD | 0.00 USD | 75,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2295.00` | 3,310,000.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2295.90` | 839,920,000.00 USD | 839,920,000.00 USD | 25,120,000.00 USD | 2,380,000.00 USD | 479,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2296.30` | 267,460,000.00 USD | 267,460,000.00 USD | 0.00 USD | 1,720,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.20` | 855,330,000.00 USD | 855,330,000.00 USD | 9,500,000.00 USD | 5,900,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2299.30` | 267,470,000.00 USD | 267,470,000.00 USD | 0.00 USD | 10,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.30` | 278,000,000.00 USD | 278,000,000.00 USD | 9,550,000.00 USD | 682,490.00 USD | 298,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.50` | 868,480,000.00 USD | 868,480,000.00 USD | 12,090,000.00 USD | 1,010,000.00 USD | 63,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2305.00` | 940,780.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.30` | 301,160,000.00 USD | 301,160,000.00 USD | 9,200,000.00 USD | 11,910,000.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.80` | 877,400,000.00 USD | 877,400,000.00 USD | 2,980,000.00 USD | 3,740,000.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2308.30` | 303,910,000.00 USD | 303,910,000.00 USD | 0.00 USD | 2,750,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2309.10` | 881,170,000.00 USD | 881,170,000.00 USD | 732,090.00 USD | 930,630.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2311.30` | 304,600,000.00 USD | 304,600,000.00 USD | 691,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2312.40` | 888,520,000.00 USD | 888,520,000.00 USD | 7,270,000.00 USD | 0.00 USD | 70,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2314.30` | 316,060,000.00 USD | 316,060,000.00 USD | 0.00 USD | 11,260,000.00 USD | 203,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2315.00` | 932,620.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2315.70` | 896,090,000.00 USD | 896,090,000.00 USD | 0.00 USD | 7,460,000.00 USD | 117,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2317.30` | 342,990,000.00 USD | 342,990,000.00 USD | 8,430,000.00 USD | 13,390,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.00` | 902,080,000.00 USD | 902,080,000.00 USD | 1,020,000.00 USD | 4,550,000.00 USD | 411,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.30` | 355,360,000.00 USD | 355,360,000.00 USD | 3,870,000.00 USD | 8,340,000.00 USD | 147,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.30` | 915,400,000.00 USD | 915,400,000.00 USD | 0.00 USD | 13,320,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2323.30` | 363,440,000.00 USD | 363,440,000.00 USD | 572,970.00 USD | 7,510,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2325.00` | 321,320.00 USD | 329,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.60` | 922,190,000.00 USD | 922,190,000.00 USD | 4,250,000.00 USD | 2,540,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2326.30` | 373,740,000.00 USD | 373,740,000.00 USD | 479,120.00 USD | 5,550,000.00 USD | 4,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.90` | 934,020,000.00 USD | 934,020,000.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2329.30` | 383,760,000.00 USD | 383,760,000.00 USD | 8,790,000.00 USD | 884,940.00 USD | 344,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2332.20` | 963,250,000.00 USD | 963,250,000.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2332.30` | 395,720,000.00 USD | 395,720,000.00 USD | 11,600,000.00 USD | 251,940.00 USD | 107,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2335.00` | 7,680.00 USD | 7,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2335.30` | 419,640,000.00 USD | 419,640,000.00 USD | 17,430,000.00 USD | 3,070,000.00 USD | 3,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2335.50` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 6,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2338.30` | 432,540,000.00 USD | 432,540,000.00 USD | 6,030,000.00 USD | 688,030.00 USD | 6,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.80` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2341.30` | 455,400,000.00 USD | 455,400,000.00 USD | 9,780,000.00 USD | 3,290,000.00 USD | 9,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2342.10` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2344.30` | 468,660,000.00 USD | 468,660,000.00 USD | 1,370,000.00 USD | 6,180,000.00 USD | 5,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2345.40` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 1,350,000.00 USD | 10,870,000.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2347.30` | 480,500,000.00 USD | 480,500,000.00 USD | 3,220,000.00 USD | 3,010,000.00 USD | 5,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.70` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 847,620.00 USD | 8,140,000.00 USD | 24,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.30` | 526,570,000.00 USD | 526,570,000.00 USD | 30,920,000.00 USD | 6,290,000.00 USD | 8,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2352.00` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 2,930,000.00 USD | 21,880,000.00 USD | 10,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2353.30` | 535,760,000.00 USD | 535,760,000.00 USD | 4,170,000.00 USD | 3,800,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2355.30` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 16,520,000.00 USD | 36,690,000.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2356.30` | 558,510,000.00 USD | 558,510,000.00 USD | 3,710,000.00 USD | 16,640,000.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.60` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 7,110,000.00 USD | 512,220.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2359.30` | 576,550,000.00 USD | 576,550,000.00 USD | 4,140,000.00 USD | 6,970,000.00 USD | 6,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.90` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 119,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.30` | 595,190,000.00 USD | 595,190,000.00 USD | 10,460,000.00 USD | 6,710,000.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 1,020.00 USD | 1,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2365.20` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 8,440,000.00 USD | 0.00 USD | 6,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2365.30` | 610,310,000.00 USD | 610,310,000.00 USD | 3,460,000.00 USD | 3,710,000.00 USD | 7,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2368.30` | 622,320,000.00 USD | 622,320,000.00 USD | 7,910,000.00 USD | 2,500,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.50` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 10,270,000.00 USD | 475,460.00 USD | 404,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2371.30` | 662,960,000.00 USD | 662,960,000.00 USD | 18,140,000.00 USD | 13,710,000.00 USD | 8,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.80` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 23,260,000.00 USD | 0.00 USD | 50,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2374.30` | 685,400,000.00 USD | 685,400,000.00 USD | 14,690,000.00 USD | 1,320,000.00 USD | 6,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 47,010.00 USD | 48,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2375.10` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2377.30` | 708,550,000.00 USD | 708,550,000.00 USD | 6,500,000.00 USD | 8,030,000.00 USD | 8,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.40` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.30` | 750,520,000.00 USD | 750,520,000.00 USD | 14,000,000.00 USD | 11,640,000.00 USD | 16,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.70` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 22,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.30` | 811,140,000.00 USD | 811,140,000.00 USD | 24,350,000.00 USD | 17,830,000.00 USD | 18,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2385.00` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 3,730,000.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2386.30` | 853,280,000.00 USD | 853,280,000.00 USD | 14,350,000.00 USD | 16,360,000.00 USD | 11,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.30` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2389.30` | 882,180,000.00 USD | 882,180,000.00 USD | 13,790,000.00 USD | 7,220,000.00 USD | 7,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.60` | 1,740,000,000.00 USD | 1,740,000,000.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.30` | 904,860,000.00 USD | 904,860,000.00 USD | 3,240,000.00 USD | 12,680,000.00 USD | 6,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.90` | 1,860,000,000.00 USD | 1,860,000,000.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,420,000.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2395.30` | 927,470,000.00 USD | 927,470,000.00 USD | 8,480,000.00 USD | 10,370,000.00 USD | 3,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2398.20` | 1,970,000,000.00 USD | 1,970,000,000.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.30` | 947,680,000.00 USD | 947,680,000.00 USD | 5,950,000.00 USD | 6,860,000.00 USD | 7,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2401.30` | 973,220,000.00 USD | 973,220,000.00 USD | 8,760,000.00 USD | 7,400,000.00 USD | 9,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.50` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2404.30` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 10,010,000.00 USD | 11,420,000.00 USD | 8,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.80` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 9,120,000.00 USD | 17,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2407.30` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 16,500,000.00 USD | 9,310,000.00 USD | 9,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2408.10` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.30` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 9,560,000.00 USD | 9,260,000.00 USD | 9,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.40` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.30` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 8,610,000.00 USD | 5,530,000.00 USD | 3,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.70` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 24,010,000.00 USD | 21,950,000.00 USD | 23,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 459,730.00 USD | 17,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2416.30` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 5,470,000.00 USD | 7,950,000.00 USD | 4,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.00` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2419.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 5,120,000.00 USD | 3,350,000.00 USD | 3,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.30` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 25,700,000.00 USD | 27,890,000.00 USD | 21,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.30` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 4,560,000.00 USD | 5,190,000.00 USD | 6,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.60` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 24,180,000.00 USD | 35,050,000.00 USD | 34,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 816,560.00 USD | 18,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.30` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 1,810,000.00 USD | 2,670,000.00 USD | 844,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.90` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 25,390,000.00 USD | 18,380,000.00 USD | 26,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.30` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 466,170.00 USD | 542,280.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.20` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 10,580,000.00 USD | 18,750,000.00 USD | 9,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2431.30` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 2,890,000.00 USD | 2,960,000.00 USD | 347,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2434.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 1,930,000.00 USD | 510,300.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.50` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 8,040,000.00 USD | 26,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2437.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 1,250,000.00 USD | 531,390.00 USD | 205,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.80` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 12,000,000.00 USD | 12,820,000.00 USD | 5,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 1,540,000.00 USD | 1,250,000.00 USD | 479,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.10` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2443.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 1,050,000.00 USD | 1,850,000.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 8,860,000.00 USD | 15,160,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 143,630.00 USD | 26,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2446.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 648,280.00 USD | 347,060.00 USD | 404,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.70` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 11,650,000.00 USD | 8,510,000.00 USD | 17,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2449.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 408,380.00 USD | 744,230.00 USD | 2,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.00` | 3,030,000,000.00 USD | 3,030,000,000.00 USD | 16,710,000.00 USD | 14,100,000.00 USD | 16,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2452.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 3,750,000.00 USD | 2,930,000.00 USD | 4,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2454.30` | 3,040,000,000.00 USD | 3,040,000,000.00 USD | 4,710,000.00 USD | 5,780,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 106,960.00 USD | 26,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 4,330,000.00 USD | 3,510,000.00 USD | 2,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.60` | 3,080,000,000.00 USD | 3,080,000,000.00 USD | 15,240,000.00 USD | 12,540,000.00 USD | 12,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2458.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 2,260,000.00 USD | 1,790,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.90` | 3,100,000,000.00 USD | 3,100,000,000.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2461.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 1,260,000.00 USD | 1,180,000.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.20` | 3,120,000,000.00 USD | 3,120,000,000.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2464.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 352,200.00 USD | 2,960,000.00 USD | 829,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 483,330.00 USD | 27,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2467.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 83,300.00 USD | 68,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.50` | 3,130,000,000.00 USD | 3,130,000,000.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 1,190,000.00 USD | 391,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.80` | 3,140,000,000.00 USD | 3,140,000,000.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.10` | 3,150,000,000.00 USD | 3,150,000,000.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 386,010.00 USD | 27,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2477.40` | 3,160,000,000.00 USD | 3,160,000,000.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.70` | 3,160,000,000.00 USD | 3,160,000,000.00 USD | 2,110,000.00 USD | 2,920,000.00 USD | 505,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2482.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 239,600.00 USD | 136,500.00 USD | 43,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.00` | 3,160,000,000.00 USD | 3,160,000,000.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 2,000,000.00 USD | 29,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2485.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 865,140.00 USD | 1,330,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2487.30` | 3,160,000,000.00 USD | 3,160,000,000.00 USD | 325,140.00 USD | 262,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.60` | 3,170,000,000.00 USD | 3,170,000,000.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 279,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2491.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 138,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.90` | 3,180,000,000.00 USD | 3,180,000,000.00 USD | 1,660,000.00 USD | 1,790,000.00 USD | 3,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2494.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 134,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 941,300.00 USD | 30,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.20` | 3,190,000,000.00 USD | 3,190,000,000.00 USD | 2,940,000.00 USD | 5,270,000.00 USD | 8,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.50` | 3,200,000,000.00 USD | 3,200,000,000.00 USD | 1,160,000.00 USD | 2,280,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.80` | 3,200,000,000.00 USD | 3,200,000,000.00 USD | 111,800.00 USD | 1,900,000.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 119,320.00 USD | 30,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2507.10` | 3,210,000,000.00 USD | 3,210,000,000.00 USD | 4,110,000.00 USD | 3,090,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2509.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2510.40` | 3,210,000,000.00 USD | 3,210,000,000.00 USD | 1,200,000.00 USD | 1,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2512.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 88,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.70` | 3,210,000,000.00 USD | 3,210,000,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 139,000.00 USD | 30,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2517.00` | 3,210,000,000.00 USD | 3,210,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2520.30` | 3,220,000,000.00 USD | 3,220,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2521.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 80,610.00 USD | 121,470.00 USD | 110,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.60` | 3,220,000,000.00 USD | 3,220,000,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2524.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 984,680.00 USD | 537,030.00 USD | 540,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 1,160,000.00 USD | 32,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2526.90` | 3,220,000,000.00 USD | 3,220,000,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2527.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 387,410.00 USD | 362,000.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.20` | 3,230,000,000.00 USD | 3,230,000,000.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2530.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 1,050,000.00 USD | 965,400.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2533.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 407,340.00 USD | 555,250.00 USD | 436,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.50` | 3,240,000,000.00 USD | 3,240,000,000.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 663,280.00 USD | 32,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2536.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 1,260,000.00 USD | 698,510.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2536.80` | 3,250,000,000.00 USD | 3,250,000,000.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2539.30` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 2,370,000.00 USD | 1,090,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2540.10` | 3,260,000,000.00 USD | 3,260,000,000.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2542.30` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 1,300,000.00 USD | 1,350,000.00 USD | 218,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2543.40` | 3,260,000,000.00 USD | 3,260,000,000.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 6,460,000.00 USD | 39,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2545.30` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 1,030,000.00 USD | 336,450.00 USD | 212,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2546.70` | 3,270,000,000.00 USD | 3,270,000,000.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2548.30` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 2,050,000.00 USD | 1,680,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.00` | 3,280,000,000.00 USD | 3,280,000,000.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2551.30` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 1,480,000.00 USD | 1,120,000.00 USD | 698,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.30` | 3,290,000,000.00 USD | 3,290,000,000.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2554.30` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 1,100,000.00 USD | 228,660.00 USD | 236,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 2,830,000.00 USD | 42,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2556.60` | 3,300,000,000.00 USD | 3,300,000,000.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2557.30` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 717,260.00 USD | 506,330.00 USD | 740,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.90` | 3,310,000,000.00 USD | 3,310,000,000.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2560.30` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 2,020,000.00 USD | 1,140,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2563.20` | 3,310,000,000.00 USD | 3,310,000,000.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2563.30` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 617,040.00 USD | 998,570.00 USD | 984,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 1,790,000.00 USD | 43,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2566.30` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 172,210.00 USD | 403,100.00 USD | 11,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2566.50` | 3,320,000,000.00 USD | 3,320,000,000.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2569.30` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 327,300.00 USD | 119,690.00 USD | 466,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.80` | 3,320,000,000.00 USD | 3,320,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2572.30` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 792,480.00 USD | 841,400.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2573.10` | 3,320,000,000.00 USD | 3,320,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 11,830,000.00 USD | 55,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2575.30` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 546,100.00 USD | 0.00 USD | 502,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2576.40` | 3,330,000,000.00 USD | 3,330,000,000.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2578.30` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 118,210.00 USD | 31,550.00 USD | 8,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2579.70` | 3,340,000,000.00 USD | 3,340,000,000.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2581.30` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 450,470.00 USD | 405,480.00 USD | 409,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2583.00` | 3,340,000,000.00 USD | 3,340,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2583.80` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 411,740.00 USD | 226,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,470,000.00 USD | 82,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.30` | 3,350,000,000.00 USD | 3,350,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.60` | 3,350,000,000.00 USD | 3,350,000,000.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.90` | 3,360,000,000.00 USD | 3,360,000,000.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 8,180,000.00 USD | 90,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2596.20` | 3,360,000,000.00 USD | 3,360,000,000.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2599.50` | 3,370,000,000.00 USD | 3,370,000,000.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2602.80` | 3,370,000,000.00 USD | 3,370,000,000.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 660,550.00 USD | 91,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.10` | 3,380,000,000.00 USD | 3,380,000,000.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.40` | 3,380,000,000.00 USD | 3,380,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.70` | 3,380,000,000.00 USD | 3,380,000,000.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 1,190,000.00 USD | 92,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2616.00` | 3,390,000,000.00 USD | 3,390,000,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2619.30` | 3,390,000,000.00 USD | 3,390,000,000.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2622.60` | 3,390,000,000.00 USD | 3,390,000,000.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2625.00` | 453,080.00 USD | 92,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2625.90` | 3,390,000,000.00 USD | 3,390,000,000.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2629.20` | 3,390,000,000.00 USD | 3,390,000,000.00 USD | 0.00 USD | 20,460.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2632.40` | 3,390,000,000.00 USD | 3,390,000,000.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2635.00` | 175,730.00 USD | 92,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 163,860.00 USD | 92,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 35,640,000.00 USD | 128,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 68,220.00 USD | 128,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 121,140.00 USD | 128,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 7,680,000.00 USD | 136,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 132,910.00 USD | 136,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 42,520,000.00 USD | 179,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 3,460,000.00 USD | 182,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 347,630.00 USD | 182,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 3,610,000.00 USD | 186,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 937,840.00 USD | 187,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 632,790.00 USD | 188,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 299,800.00 USD | 188,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 97,340.00 USD | 188,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 6,920,000.00 USD | 195,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 115,010.00 USD | 195,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 859,600.00 USD | 196,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 284,990.00 USD | 196,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 83,990.00 USD | 196,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 3,370,000.00 USD | 200,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 2,360,000.00 USD | 202,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 188,540.00 USD | 202,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 44,730,000.00 USD | 247,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 23,070,000.00 USD | 270,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 3,890,000.00 USD | 274,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 1,400,000.00 USD | 275,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 453,700.00 USD | 276,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 447,640.00 USD | 276,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 26,510,000.00 USD | 303,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 1,440,000.00 USD | 304,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 7,480,000.00 USD | 312,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 21,080,000.00 USD | 333,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 1,420,000.00 USD | 334,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 221,010.00 USD | 334,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 818,270.00 USD | 335,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 814,800.00 USD | 336,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 3,520,000.00 USD | 340,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 363,690.00 USD | 340,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 8,280,000.00 USD | 348,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 3,640,000.00 USD | 352,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 13,150,000.00 USD | 365,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 4,830,000.00 USD | 370,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 632,420.00 USD | 370,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 4,010,000.00 USD | 374,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 110,980.00 USD | 375,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 1,790,000.00 USD | 376,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 597,120.00 USD | 377,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 104,410.00 USD | 377,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 136,660.00 USD | 377,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 1,670,000.00 USD | 379,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 1,530,000.00 USD | 380,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 6,220,000.00 USD | 387,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 1,480.00 USD | 387,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 658,490.00 USD | 387,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 1,070,000.00 USD | 388,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 3,510,000.00 USD | 392,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 90,340.00 USD | 392,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 590,760.00 USD | 392,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 5,000,000.00 USD | 397,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 9,070,000.00 USD | 407,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 20,630.00 USD | 407,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 303,690.00 USD | 407,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 359,730.00 USD | 407,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 117,840.00 USD | 407,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 9,130,000.00 USD | 416,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 1,270,000.00 USD | 418,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 66,520.00 USD | 418,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 11,660,000.00 USD | 429,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 130,190.00 USD | 430,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 27,410.00 USD | 430,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 839,420.00 USD | 430,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 62,730,000.00 USD | 493,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 1,040,000.00 USD | 494,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 110,710.00 USD | 494,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 162,990.00 USD | 495,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 238,960.00 USD | 495,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 125,120.00 USD | 495,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 3,140,000.00 USD | 498,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 14,460,000.00 USD | 512,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 240,520.00 USD | 513,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 40,690.00 USD | 513,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 5,450,000.00 USD | 518,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 1,150,000.00 USD | 519,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 442,570.00 USD | 520,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 79,550.00 USD | 520,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 1,670,000.00 USD | 522,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 15,890.00 USD | 522,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 35,660.00 USD | 522,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 78,800.00 USD | 522,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 39,410.00 USD | 522,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 7,150,000.00 USD | 529,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 143,600.00 USD | 529,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 310,340.00 USD | 529,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 78,340.00 USD | 529,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 477,460.00 USD | 530,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 302,580.00 USD | 530,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 71,590.00 USD | 530,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 3,830,000.00 USD | 534,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 539,240.00 USD | 535,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 103,240,000.00 USD | 638,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 6,570,000.00 USD | 644,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 378,780.00 USD | 645,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 1,100,000.00 USD | 646,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 367,730.00 USD | 646,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 1,900,000.00 USD | 648,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 1,090,000.00 USD | 649,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 305,070.00 USD | 650,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 8,320,000.00 USD | 658,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 249,910.00 USD | 658,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 34,780,000.00 USD | 693,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 841,120.00 USD | 694,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 13,450,000.00 USD | 707,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 84,490.00 USD | 707,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 351,950.00 USD | 708,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 45,720.00 USD | 708,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 271,140.00 USD | 708,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 81,730.00 USD | 708,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 211,350.00 USD | 708,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 338,010.00 USD | 709,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 408,410,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 1,590,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 1,780,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 15,960,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 1,420,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 130,520.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 1,430,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 4,700.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 199,870.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 1,640,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 25,640.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 404,950.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 680,870.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 90,050,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 3,920,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 30,460,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 216,180.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 117,490.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 824,230.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 67,410,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 1,580,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 470,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 2,090,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 2,430,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 287,790.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 2,890,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 83,350.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 27,910.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 864,500.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 169,420.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 492,990.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 280,240.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 4,130,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 84,530.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 674.90 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 6,950.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4225.00` | 18,600,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 1,420.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 4,670.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 99,390.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 68,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 17,020,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 217,490.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 2,460.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 8,250.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 328,280.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 31,660.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 19,940.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 2,270,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 43,740.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 598,460.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 849,070.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 285,930,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 93,330.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 26,050.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 633,470.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 1,930,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4445.00` | 685,460.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4455.00` | 490,070.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4465.00` | 80,330.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4475.00` | 36,810.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4485.00` | 20,940.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4495.00` | 12,800.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4505.00` | 2,440,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4515.00` | 3,840,000.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4525.00` | 981,310.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4535.00` | 86,800.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4545.00` | 23,190.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4555.00` | 43,530.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4565.00` | 265,340.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4575.00` | 137,500.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4585.00` | 35,590.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4595.00` | 251,050.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4605.00` | 37,010.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4615.00` | 52,010.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4625.00` | 406,220.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4635.00` | 231,230.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4645.00` | 175,430.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4655.00` | 1,360,000.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4665.00` | 35,090.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4675.00` | 50,490.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `455.00` | 846,000,000.00 USD | 0.00 USD | 80,200.00 USD | `-79.83%` | `176.27` |
| `Live` | `Long` | `465.00` | 845,920,000.00 USD | 0.00 USD | 14,510.00 USD | `-79.39%` | `31.21` |
| `Live` | `Long` | `475.00` | 845,910,000.00 USD | 0.00 USD | 3,720.00 USD | `-78.94%` | `7.83` |
| `Live` | `Long` | `485.00` | 845,900,000.00 USD | 0.00 USD | 43,950.00 USD | `-78.50%` | `90.61` |
| `Live` | `Long` | `495.00` | 845,860,000.00 USD | 0.00 USD | 5,270.00 USD | `-78.06%` | `10.64` |
| `Live` | `Long` | `505.00` | 845,850,000.00 USD | 0.00 USD | 1,810,000.00 USD | `-77.61%` | `3,576.25` |
| `Live` | `Long` | `515.00` | 844,050,000.00 USD | 0.00 USD | 2,140.00 USD | `-77.17%` | `4.15` |
| `Live` | `Long` | `525.00` | 844,050,000.00 USD | 0.00 USD | 10,400.00 USD | `-76.73%` | `19.80` |
| `Live` | `Long` | `535.00` | 844,040,000.00 USD | 0.00 USD | 15,310.00 USD | `-76.28%` | `28.61` |
| `Live` | `Long` | `545.00` | 844,020,000.00 USD | 0.00 USD | 49,430.00 USD | `-75.84%` | `90.69` |
| `Live` | `Long` | `555.00` | 843,970,000.00 USD | 0.00 USD | 174,920.00 USD | `-75.40%` | `315.17` |
| `Live` | `Long` | `565.00` | 843,800,000.00 USD | 0.00 USD | 214.70 USD | `-74.95%` | `0.38` |
| `Live` | `Long` | `575.00` | 843,800,000.00 USD | 0.00 USD | 30,880.00 USD | `-74.51%` | `53.71` |
| `Live` | `Long` | `585.00` | 843,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | `-74.07%` | `3,012.88` |
| `Live` | `Long` | `595.00` | 842,000,000.00 USD | 0.00 USD | 990,010.00 USD | `-73.62%` | `1,663.88` |
| `Live` | `Long` | `605.00` | 841,010,000.00 USD | 0.00 USD | 433,350.00 USD | `-73.18%` | `716.28` |
| `Live` | `Long` | `615.00` | 840,580,000.00 USD | 0.00 USD | 2,450.00 USD | `-72.74%` | `3.98` |
| `Live` | `Long` | `625.00` | 840,580,000.00 USD | 0.00 USD | 17,370.00 USD | `-72.29%` | `27.80` |
| `Live` | `Long` | `635.00` | 840,560,000.00 USD | 0.00 USD | 6,490.00 USD | `-71.85%` | `10.22` |
| `Live` | `Long` | `645.00` | 840,550,000.00 USD | 0.00 USD | 2,780,000.00 USD | `-71.41%` | `4,314.07` |
| `Live` | `Long` | `655.00` | 837,770,000.00 USD | 0.00 USD | 50,740.00 USD | `-70.96%` | `77.46` |
| `Live` | `Long` | `665.00` | 837,720,000.00 USD | 0.00 USD | 26,820.00 USD | `-70.52%` | `40.33` |
| `Live` | `Long` | `675.00` | 837,690,000.00 USD | 0.00 USD | 20,070.00 USD | `-70.08%` | `29.74` |
| `Live` | `Long` | `685.00` | 837,670,000.00 USD | 0.00 USD | 28,680.00 USD | `-69.63%` | `41.87` |
| `Live` | `Long` | `695.00` | 837,640,000.00 USD | 0.00 USD | 668.59 USD | `-69.19%` | `0.96` |
| `Live` | `Long` | `705.00` | 837,640,000.00 USD | 0.00 USD | 32,420.00 USD | `-68.75%` | `45.98` |
| `Live` | `Long` | `715.00` | 837,610,000.00 USD | 0.00 USD | 1,570,000.00 USD | `-68.30%` | `2,194.63` |
| `Live` | `Long` | `725.00` | 836,040,000.00 USD | 0.00 USD | 393,960.00 USD | `-67.86%` | `543.39` |
| `Live` | `Long` | `735.00` | 835,650,000.00 USD | 0.00 USD | 39,690.00 USD | `-67.42%` | `54.01` |
| `Live` | `Long` | `745.00` | 835,610,000.00 USD | 0.00 USD | 2,170.00 USD | `-66.97%` | `2.91` |
| `Live` | `Long` | `755.00` | 835,610,000.00 USD | 0.00 USD | 27,360.00 USD | `-66.53%` | `36.24` |
| `Live` | `Long` | `765.00` | 835,580,000.00 USD | 0.00 USD | 17,180.00 USD | `-66.09%` | `22.46` |
| `Live` | `Long` | `775.00` | 835,560,000.00 USD | 0.00 USD | 58,650.00 USD | `-65.64%` | `75.68` |
| `Live` | `Long` | `785.00` | 835,500,000.00 USD | 0.00 USD | 21,990.00 USD | `-65.20%` | `28.01` |
| `Live` | `Long` | `795.00` | 835,480,000.00 USD | 0.00 USD | 41,860.00 USD | `-64.76%` | `52.66` |
| `Live` | `Long` | `805.00` | 835,440,000.00 USD | 0.00 USD | 56,280.00 USD | `-64.31%` | `69.92` |
| `Live` | `Long` | `815.00` | 835,380,000.00 USD | 0.00 USD | 18,470.00 USD | `-63.87%` | `22.66` |
| `Live` | `Long` | `825.00` | 835,360,000.00 USD | 0.00 USD | 309,280.00 USD | `-63.43%` | `374.89` |
| `Live` | `Long` | `835.00` | 835,050,000.00 USD | 0.00 USD | 22,040.00 USD | `-62.98%` | `26.40` |
| `Live` | `Long` | `845.00` | 835,030,000.00 USD | 0.00 USD | 34,180.00 USD | `-62.54%` | `40.46` |
| `Live` | `Long` | `855.00` | 835,000,000.00 USD | 0.00 USD | 134,590.00 USD | `-62.10%` | `157.42` |
| `Live` | `Long` | `865.00` | 834,860,000.00 USD | 0.00 USD | 455,230.00 USD | `-61.65%` | `526.28` |
| `Live` | `Long` | `875.00` | 834,410,000.00 USD | 0.00 USD | 100,450.00 USD | `-61.21%` | `114.80` |
| `Live` | `Long` | `885.00` | 834,310,000.00 USD | 0.00 USD | 1,010,000.00 USD | `-60.77%` | `1,137.36` |
| `Live` | `Long` | `895.00` | 833,300,000.00 USD | 0.00 USD | 159,890.00 USD | `-60.32%` | `178.65` |
| `Live` | `Long` | `905.00` | 833,140,000.00 USD | 0.00 USD | 67,390.00 USD | `-59.88%` | `74.47` |
| `Live` | `Long` | `915.00` | 833,070,000.00 USD | 0.00 USD | 421,100.00 USD | `-59.44%` | `460.21` |
| `Live` | `Long` | `925.00` | 832,650,000.00 USD | 0.00 USD | 117,910.00 USD | `-58.99%` | `127.47` |
| `Live` | `Long` | `935.00` | 832,530,000.00 USD | 0.00 USD | 41,570.00 USD | `-58.55%` | `44.46` |
| `Live` | `Long` | `945.00` | 832,490,000.00 USD | 0.00 USD | 29,180.00 USD | `-58.11%` | `30.88` |
| `Live` | `Long` | `955.00` | 832,460,000.00 USD | 0.00 USD | 346,950.00 USD | `-57.66%` | `363.30` |
| `Live` | `Long` | `965.00` | 832,120,000.00 USD | 0.00 USD | 158,530.00 USD | `-57.22%` | `164.28` |
| `Live` | `Long` | `975.00` | 831,960,000.00 USD | 0.00 USD | 92,680.00 USD | `-56.78%` | `95.05` |
| `Live` | `Long` | `985.00` | 831,870,000.00 USD | 0.00 USD | 91,750.00 USD | `-56.33%` | `93.15` |
| `Live` | `Long` | `995.00` | 831,770,000.00 USD | 0.00 USD | 19,850.00 USD | `-55.89%` | `19.94` |
| `Live` | `Long` | `1005.00` | 831,750,000.00 USD | 0.00 USD | 33,640.00 USD | `-55.45%` | `33.47` |
| `Live` | `Long` | `1015.00` | 831,720,000.00 USD | 0.00 USD | 58,220.00 USD | `-55.00%` | `57.36` |
| `Live` | `Long` | `1025.00` | 831,660,000.00 USD | 0.00 USD | 131,090.00 USD | `-54.56%` | `127.90` |
| `Live` | `Long` | `1035.00` | 831,530,000.00 USD | 0.00 USD | 213,680.00 USD | `-54.12%` | `206.46` |
| `Live` | `Long` | `1045.00` | 831,320,000.00 USD | 0.00 USD | 7,730,000.00 USD | `-53.67%` | `7,394.22` |
| `Live` | `Long` | `1055.00` | 823,590,000.00 USD | 0.00 USD | 1,540,000.00 USD | `-53.23%` | `1,455.85` |
| `Live` | `Long` | `1065.00` | 822,050,000.00 USD | 0.00 USD | 133,980.00 USD | `-52.79%` | `125.80` |
| `Live` | `Long` | `1075.00` | 821,920,000.00 USD | 0.00 USD | 670,060.00 USD | `-52.35%` | `623.31` |
| `Live` | `Long` | `1085.00` | 821,250,000.00 USD | 0.00 USD | 60,670.00 USD | `-51.90%` | `55.92` |
| `Live` | `Long` | `1095.00` | 821,190,000.00 USD | 0.00 USD | 168,380.00 USD | `-51.46%` | `153.77` |
| `Live` | `Long` | `1105.00` | 821,020,000.00 USD | 0.00 USD | 132,910.00 USD | `-51.02%` | `120.28` |
| `Live` | `Long` | `1115.00` | 820,890,000.00 USD | 0.00 USD | 88,340.00 USD | `-50.57%` | `79.23` |
| `Live` | `Long` | `1125.00` | 820,800,000.00 USD | 0.00 USD | 43,820.00 USD | `-50.13%` | `38.95` |
| `Live` | `Long` | `1135.00` | 820,760,000.00 USD | 0.00 USD | 193,380.00 USD | `-49.69%` | `170.38` |
| `Live` | `Long` | `1145.00` | 820,560,000.00 USD | 0.00 USD | 312,170.00 USD | `-49.24%` | `272.64` |
| `Live` | `Long` | `1155.00` | 820,250,000.00 USD | 0.00 USD | 401,010.00 USD | `-48.80%` | `347.19` |
| `Live` | `Long` | `1165.00` | 819,850,000.00 USD | 0.00 USD | 194,270.00 USD | `-48.36%` | `166.76` |
| `Live` | `Long` | `1175.00` | 819,660,000.00 USD | 0.00 USD | 1,560,000.00 USD | `-47.91%` | `1,324.68` |
| `Live` | `Long` | `1185.00` | 818,100,000.00 USD | 0.00 USD | 159,620.00 USD | `-47.47%` | `134.70` |
| `Live` | `Long` | `1195.00` | 817,940,000.00 USD | 0.00 USD | 452,850.00 USD | `-47.03%` | `378.95` |
| `Live` | `Long` | `1205.00` | 817,490,000.00 USD | 0.00 USD | 242,850.00 USD | `-46.58%` | `201.54` |
| `Live` | `Long` | `1215.00` | 817,240,000.00 USD | 0.00 USD | 287,380.00 USD | `-46.14%` | `236.53` |
| `Live` | `Long` | `1225.00` | 816,960,000.00 USD | 0.00 USD | 2,890,000.00 USD | `-45.70%` | `2,356.53` |
| `Live` | `Long` | `1235.00` | 814,070,000.00 USD | 0.00 USD | 2,680,000.00 USD | `-45.25%` | `2,172.86` |
| `Live` | `Long` | `1245.00` | 811,390,000.00 USD | 0.00 USD | 290,450.00 USD | `-44.81%` | `233.29` |
| `Live` | `Long` | `1255.00` | 811,100,000.00 USD | 0.00 USD | 369,450.00 USD | `-44.37%` | `294.39` |
| `Live` | `Long` | `1265.00` | 810,730,000.00 USD | 0.00 USD | 249,220.00 USD | `-43.92%` | `197.01` |
| `Live` | `Long` | `1275.00` | 810,480,000.00 USD | 0.00 USD | 118,280.00 USD | `-43.48%` | `92.77` |
| `Live` | `Long` | `1285.00` | 810,360,000.00 USD | 0.00 USD | 15,610,000.00 USD | `-43.04%` | `12,144.04` |
| `Live` | `Long` | `1295.00` | 794,750,000.00 USD | 0.00 USD | 271,050.00 USD | `-42.59%` | `209.30` |
| `Live` | `Long` | `1305.00` | 794,480,000.00 USD | 0.00 USD | 257,050.00 USD | `-42.15%` | `196.98` |
| `Live` | `Long` | `1315.00` | 794,230,000.00 USD | 0.00 USD | 580,470.00 USD | `-41.71%` | `441.42` |
| `Live` | `Long` | `1325.00` | 793,650,000.00 USD | 0.00 USD | 1,550,000.00 USD | `-41.26%` | `1,170.96` |
| `Live` | `Long` | `1335.00` | 792,090,000.00 USD | 0.00 USD | 298,460.00 USD | `-40.82%` | `223.57` |
| `Live` | `Long` | `1345.00` | 791,800,000.00 USD | 0.00 USD | 497,840.00 USD | `-40.38%` | `370.14` |
| `Live` | `Long` | `1355.00` | 791,300,000.00 USD | 0.00 USD | 359,190.00 USD | `-39.93%` | `265.09` |
| `Live` | `Long` | `1365.00` | 790,940,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-39.49%` | `785.38` |
| `Live` | `Long` | `1375.00` | 789,870,000.00 USD | 0.00 USD | 12,800,000.00 USD | `-39.05%` | `9,311.32` |
| `Live` | `Long` | `1385.00` | 777,060,000.00 USD | 0.00 USD | 6,970,000.00 USD | `-38.60%` | `5,030.70` |
| `Live` | `Long` | `1395.00` | 770,100,000.00 USD | 0.00 USD | 153,570.00 USD | `-38.16%` | `110.08` |
| `Live` | `Long` | `1405.00` | 769,940,000.00 USD | 0.00 USD | 10,020,000.00 USD | `-37.72%` | `7,128.52` |
| `Live` | `Long` | `1415.00` | 759,930,000.00 USD | 0.00 USD | 1,460,000.00 USD | `-37.27%` | `1,031.29` |
| `Live` | `Long` | `1425.00` | 758,470,000.00 USD | 0.00 USD | 875,640.00 USD | `-36.83%` | `614.48` |
| `Live` | `Long` | `1435.00` | 757,590,000.00 USD | 0.00 USD | 245,420.00 USD | `-36.39%` | `171.03` |
| `Live` | `Long` | `1445.00` | 757,350,000.00 USD | 0.00 USD | 287,790.00 USD | `-35.94%` | `199.16` |
| `Live` | `Long` | `1455.00` | 757,060,000.00 USD | 0.00 USD | 69,520.00 USD | `-35.50%` | `47.78` |
| `Live` | `Long` | `1465.00` | 756,990,000.00 USD | 0.00 USD | 1,190,000.00 USD | `-35.06%` | `813.36` |
| `Live` | `Long` | `1475.00` | 755,800,000.00 USD | 0.00 USD | 5,640,000.00 USD | `-34.61%` | `3,820.96` |
| `Live` | `Long` | `1485.00` | 750,160,000.00 USD | 0.00 USD | 17,690,000.00 USD | `-34.17%` | `11,910.45` |
| `Live` | `Long` | `1495.00` | 732,470,000.00 USD | 0.00 USD | 16,380,000.00 USD | `-33.73%` | `10,956.05` |
| `Live` | `Long` | `1505.00` | 716,090,000.00 USD | 0.00 USD | 137,450.00 USD | `-33.28%` | `91.33` |
| `Live` | `Long` | `1515.00` | 715,960,000.00 USD | 0.00 USD | 15,520,000.00 USD | `-32.84%` | `10,241.44` |
| `Live` | `Long` | `1525.00` | 700,440,000.00 USD | 0.00 USD | 18,750,000.00 USD | `-32.40%` | `12,291.97` |
| `Live` | `Long` | `1535.00` | 681,700,000.00 USD | 0.00 USD | 10,250,000.00 USD | `-31.95%` | `6,677.74` |
| `Live` | `Long` | `1545.00` | 671,450,000.00 USD | 0.00 USD | 3,890,000.00 USD | `-31.51%` | `2,519.70` |
| `Live` | `Long` | `1555.00` | 667,550,000.00 USD | 0.00 USD | 536,530.00 USD | `-31.07%` | `345.03` |
| `Live` | `Long` | `1565.00` | 667,020,000.00 USD | 0.00 USD | 257,330.00 USD | `-30.62%` | `164.43` |
| `Live` | `Long` | `1575.00` | 666,760,000.00 USD | 0.00 USD | 458,760.00 USD | `-30.18%` | `291.28` |
| `Live` | `Long` | `1585.00` | 666,300,000.00 USD | 0.00 USD | 546,140.00 USD | `-29.74%` | `344.57` |
| `Live` | `Long` | `1595.00` | 665,750,000.00 USD | 0.00 USD | 947,400.00 USD | `-29.29%` | `593.98` |
| `Live` | `Long` | `1605.00` | 664,810,000.00 USD | 0.00 USD | 18,700,000.00 USD | `-28.85%` | `11,652.44` |
| `Live` | `Long` | `1615.00` | 646,100,000.00 USD | 0.00 USD | 513,600.00 USD | `-28.41%` | `318.02` |
| `Live` | `Long` | `1625.00` | 645,590,000.00 USD | 0.00 USD | 959,010.00 USD | `-27.96%` | `590.16` |
| `Live` | `Long` | `1635.00` | 644,630,000.00 USD | 0.00 USD | 18,460,000.00 USD | `-27.52%` | `11,292.26` |
| `Live` | `Long` | `1645.00` | 626,170,000.00 USD | 0.00 USD | 36,440,000.00 USD | `-27.08%` | `22,152.48` |
| `Live` | `Long` | `1655.00` | 589,730,000.00 USD | 0.00 USD | 14,670,000.00 USD | `-26.63%` | `8,865.13` |
| `Live` | `Long` | `1665.00` | 575,060,000.00 USD | 0.00 USD | 1,250,000.00 USD | `-26.19%` | `750.55` |
| `Live` | `Long` | `1675.00` | 573,810,000.00 USD | 0.00 USD | 11,600,000.00 USD | `-25.75%` | `6,922.70` |
| `Live` | `Long` | `1685.00` | 562,210,000.00 USD | 0.00 USD | 7,480,000.00 USD | `-25.30%` | `4,439.36` |
| `Live` | `Long` | `1695.00` | 554,730,000.00 USD | 0.00 USD | 878,130.00 USD | `-24.86%` | `518.07` |
| `Live` | `Long` | `1705.00` | 553,850,000.00 USD | 0.00 USD | 29,770,000.00 USD | `-24.42%` | `17,457.89` |
| `Live` | `Long` | `1715.00` | 524,090,000.00 USD | 0.00 USD | 482,750.00 USD | `-23.97%` | `281.49` |
| `Live` | `Long` | `1725.00` | 523,600,000.00 USD | 0.00 USD | 35,080,000.00 USD | `-23.53%` | `20,336.23` |
| `Live` | `Long` | `1735.00` | 488,520,000.00 USD | 0.00 USD | 634,090.00 USD | `-23.09%` | `365.47` |
| `Live` | `Long` | `1745.00` | 487,890,000.00 USD | 0.00 USD | 1,040,000.00 USD | `-22.64%` | `597.70` |
| `Live` | `Long` | `1755.00` | 486,850,000.00 USD | 0.00 USD | 204,030.00 USD | `-22.20%` | `116.25` |
| `Live` | `Long` | `1765.00` | 486,640,000.00 USD | 0.00 USD | 713,160.00 USD | `-21.76%` | `404.06` |
| `Live` | `Long` | `1775.00` | 485,930,000.00 USD | 0.00 USD | 1,200,000.00 USD | `-21.31%` | `674.68` |
| `Live` | `Long` | `1785.00` | 484,730,000.00 USD | 0.00 USD | 54,930,000.00 USD | `-20.87%` | `30,771.35` |
| `Live` | `Long` | `1795.00` | 429,810,000.00 USD | 0.00 USD | 4,280,000.00 USD | `-20.43%` | `2,383.92` |
| `Live` | `Long` | `1805.00` | 425,530,000.00 USD | 0.00 USD | 12,700,000.00 USD | `-19.98%` | `7,035.00` |
| `Live` | `Long` | `1815.00` | 412,830,000.00 USD | 0.00 USD | 2,280,000.00 USD | `-19.54%` | `1,256.57` |
| `Live` | `Long` | `1825.00` | 410,550,000.00 USD | 0.00 USD | 461,220.00 USD | `-19.10%` | `252.72` |
| `Live` | `Long` | `1835.00` | 410,090,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-18.65%` | `954.91` |
| `Live` | `Long` | `1845.00` | 408,330,000.00 USD | 0.00 USD | 847,540.00 USD | `-18.21%` | `459.37` |
| `Live` | `Long` | `1855.00` | 407,490,000.00 USD | 0.00 USD | 2,070,000.00 USD | `-17.77%` | `1,115.41` |
| `Live` | `Long` | `1865.00` | 405,420,000.00 USD | 0.00 USD | 772,330.00 USD | `-17.32%` | `414.12` |
| `Live` | `Long` | `1875.00` | 404,650,000.00 USD | 0.00 USD | 9,890,000.00 USD | `-16.88%` | `5,275.80` |
| `Live` | `Long` | `1885.00` | 394,750,000.00 USD | 0.00 USD | 2,690,000.00 USD | `-16.44%` | `1,426.77` |
| `Live` | `Long` | `1895.00` | 392,060,000.00 USD | 0.00 USD | 6,610,000.00 USD | `-15.99%` | `3,485.52` |
| `Live` | `Long` | `1905.00` | 385,460,000.00 USD | 0.00 USD | 765,450.00 USD | `-15.55%` | `401.81` |
| `Live` | `Long` | `1915.00` | 384,690,000.00 USD | 0.00 USD | 13,520,000.00 USD | `-15.11%` | `7,061.29` |
| `Live` | `Long` | `1925.00` | 371,170,000.00 USD | 0.00 USD | 19,280,000.00 USD | `-14.66%` | `10,015.40` |
| `Live` | `Long` | `1935.00` | 351,890,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-14.22%` | `680.01` |
| `Live` | `Long` | `1945.00` | 350,580,000.00 USD | 0.00 USD | 7,380,000.00 USD | `-13.78%` | `3,792.49` |
| `Live` | `Long` | `1955.00` | 343,200,000.00 USD | 0.00 USD | 1,720,000.00 USD | `-13.33%` | `878.33` |
| `Live` | `Long` | `1965.00` | 341,480,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-12.89%` | `558.81` |
| `Live` | `Long` | `1975.00` | 340,380,000.00 USD | 0.00 USD | 2,900,000.00 USD | `-12.45%` | `1,468.82` |
| `Live` | `Long` | `1985.00` | 337,480,000.00 USD | 0.00 USD | 5,730,000.00 USD | `-12.00%` | `2,888.18` |
| `Live` | `Long` | `1995.00` | 331,750,000.00 USD | 0.00 USD | 9,670,000.00 USD | `-11.56%` | `4,847.47` |
| `Live` | `Long` | `2005.00` | 322,080,000.00 USD | 0.00 USD | 1,540,000.00 USD | `-11.12%` | `767.36` |
| `Live` | `Long` | `2015.00` | 320,540,000.00 USD | 0.00 USD | 2,450,000.00 USD | `-10.67%` | `1,216.74` |
| `Live` | `Long` | `2025.00` | 318,090,000.00 USD | 0.00 USD | 2,210,000.00 USD | `-10.23%` | `1,093.32` |
| `Live` | `Long` | `2035.00` | 315,880,000.00 USD | 0.00 USD | 538,430.00 USD | `-9.79%` | `264.59` |
| `Live` | `Long` | `2045.00` | 315,340,000.00 USD | 0.00 USD | 16,630,000.00 USD | `-9.34%` | `8,133.37` |
| `Live` | `Long` | `2055.00` | 298,700,000.00 USD | 0.00 USD | 13,190,000.00 USD | `-8.90%` | `6,418.25` |
| `Live` | `Long` | `2065.00` | 285,510,000.00 USD | 0.00 USD | 2,230,000.00 USD | `-8.46%` | `1,078.92` |
| `Live` | `Long` | `2075.00` | 283,290,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-8.01%` | `631.42` |
| `Live` | `Long` | `2085.00` | 281,980,000.00 USD | 0.00 USD | 4,940,000.00 USD | `-7.57%` | `2,370.40` |
| `Live` | `Long` | `2095.00` | 277,030,000.00 USD | 0.00 USD | 2,440,000.00 USD | `-7.13%` | `1,163.07` |
| `Live` | `Long` | `2105.00` | 274,600,000.00 USD | 0.00 USD | 1,530,000.00 USD | `-6.68%` | `726.92` |
| `Live` | `Long` | `2115.00` | 273,070,000.00 USD | 0.00 USD | 938,020.00 USD | `-6.24%` | `443.51` |
| `Live` | `Long` | `2125.00` | 272,130,000.00 USD | 0.00 USD | 2,800,000.00 USD | `-5.80%` | `1,315.35` |
| `Live` | `Long` | `2135.00` | 269,330,000.00 USD | 0.00 USD | 4,780,000.00 USD | `-5.36%` | `2,238.90` |
| `Live` | `Long` | `2145.00` | 264,550,000.00 USD | 0.00 USD | 26,580,000.00 USD | `-4.91%` | `12,393.69` |
| `Live` | `Long` | `2155.00` | 237,970,000.00 USD | 0.00 USD | 2,870,000.00 USD | `-4.47%` | `1,330.37` |
| `Live` | `Long` | `2165.00` | 235,100,000.00 USD | 0.00 USD | 1,870,000.00 USD | `-4.03%` | `864.18` |
| `Live` | `Long` | `2175.00` | 233,230,000.00 USD | 0.00 USD | 110,260,000.00 USD | `-3.58%` | `50,693.71` |
| `Live` | `Long` | `2185.00` | 122,970,000.00 USD | 0.00 USD | 101,640,000.00 USD | `-3.14%` | `46,515.50` |
| `Live` | `Long` | `2195.00` | 21,340,000.00 USD | 0.00 USD | 7,900,000.00 USD | `-2.70%` | `3,597.98` |
| `Live` | `Long` | `2205.00` | 13,440,000.00 USD | 0.00 USD | 1,760,000.00 USD | `-2.25%` | `798.27` |
| `Live` | `Long` | `2215.00` | 11,680,000.00 USD | 0.00 USD | 4,410,000.00 USD | `-1.81%` | `1,989.98` |
| `Live` | `Long` | `2225.00` | 7,270,000.00 USD | 0.00 USD | 5,180,000.00 USD | `-1.37%` | `2,328.80` |
| `Live` | `Long` | `2235.00` | 2,090,000.00 USD | 0.00 USD | 1,910,000.00 USD | `-0.92%` | `854.51` |
| `Live` | `Long` | `2245.00` | 179,470.00 USD | 0.00 USD | 160,900.00 USD | `-0.48%` | `71.67` |
| `Live` | `Long` | `2255.00` | 18,560.00 USD | 0.00 USD | 18,560.00 USD | `-0.04%` | `8.23` |
| `Live` | `Short` | `2265.00` | 7,250.00 USD | 7,250.00 USD | 0.00 USD | `+0.41%` | `3.20` |
| `Live` | `Short` | `2275.00` | 55,840.00 USD | 48,600.00 USD | 0.00 USD | `+0.85%` | `21.36` |
| `Live` | `Short` | `2285.00` | 6,280,000.00 USD | 6,220,000.00 USD | 0.00 USD | `+1.29%` | `2,721.88` |
| `Live` | `Short` | `2295.00` | 6,290,000.00 USD | 12,310.00 USD | 0.00 USD | `+1.74%` | `5.37` |
| `Live` | `Short` | `2305.00` | 7,500,000.00 USD | 1,210,000.00 USD | 0.00 USD | `+2.18%` | `524.92` |
| `Live` | `Short` | `2315.00` | 12,220,000.00 USD | 4,720,000.00 USD | 0.00 USD | `+2.62%` | `2,038.34` |
| `Live` | `Short` | `2325.00` | 12,350,000.00 USD | 134,130.00 USD | 0.00 USD | `+3.07%` | `57.69` |
| `Live` | `Short` | `2335.00` | 12,690,000.00 USD | 343,060.00 USD | 0.00 USD | `+3.51%` | `146.92` |
| `Live` | `Short` | `2345.00` | 13,290,000.00 USD | 597,120.00 USD | 0.00 USD | `+3.95%` | `254.63` |
| `Live` | `Short` | `2355.00` | 16,540,000.00 USD | 3,250,000.00 USD | 0.00 USD | `+4.40%` | `1,381.37` |
| `Live` | `Short` | `2365.00` | 16,590,000.00 USD | 47,670.00 USD | 0.00 USD | `+4.84%` | `20.16` |
| `Live` | `Short` | `2375.00` | 17,630,000.00 USD | 1,040,000.00 USD | 0.00 USD | `+5.28%` | `439.24` |
| `Live` | `Short` | `2385.00` | 18,240,000.00 USD | 610,200.00 USD | 0.00 USD | `+5.73%` | `255.85` |
| `Live` | `Short` | `2395.00` | 19,070,000.00 USD | 823,610.00 USD | 0.00 USD | `+6.17%` | `343.89` |
| `Live` | `Short` | `2405.00` | 20,710,000.00 USD | 1,640,000.00 USD | 0.00 USD | `+6.61%` | `683.61` |
| `Live` | `Short` | `2415.00` | 20,760,000.00 USD | 51,630.00 USD | 0.00 USD | `+7.06%` | `21.38` |
| `Live` | `Short` | `2425.00` | 21,100,000.00 USD | 334,040.00 USD | 0.00 USD | `+7.50%` | `137.75` |
| `Live` | `Short` | `2435.00` | 25,710,000.00 USD | 4,610,000.00 USD | 0.00 USD | `+7.94%` | `1,893.84` |
| `Live` | `Short` | `2445.00` | 25,840,000.00 USD | 130,990.00 USD | 0.00 USD | `+8.39%` | `53.57` |
| `Live` | `Short` | `2455.00` | 26,360,000.00 USD | 516,490.00 USD | 0.00 USD | `+8.83%` | `210.38` |
| `Live` | `Short` | `2465.00` | 27,120,000.00 USD | 759,490.00 USD | 0.00 USD | `+9.27%` | `308.11` |
| `Live` | `Short` | `2475.00` | 27,650,000.00 USD | 534,310.00 USD | 0.00 USD | `+9.72%` | `215.88` |
| `Live` | `Short` | `2485.00` | 29,840,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+10.16%` | `880.79` |
| `Live` | `Short` | `2495.00` | 34,570,000.00 USD | 4,730,000.00 USD | 0.00 USD | `+10.60%` | `1,896.93` |
| `Live` | `Short` | `2505.00` | 35,230,000.00 USD | 660,180.00 USD | 0.00 USD | `+11.05%` | `263.54` |
| `Live` | `Short` | `2515.00` | 35,330,000.00 USD | 98,210.00 USD | 0.00 USD | `+11.49%` | `39.05` |
| `Live` | `Short` | `2525.00` | 35,880,000.00 USD | 544,410.00 USD | 0.00 USD | `+11.93%` | `215.61` |
| `Live` | `Short` | `2535.00` | 36,810,000.00 USD | 931,980.00 USD | 0.00 USD | `+12.38%` | `367.64` |
| `Live` | `Short` | `2545.00` | 52,600,000.00 USD | 15,790,000.00 USD | 0.00 USD | `+12.82%` | `6,204.42` |
| `Live` | `Short` | `2555.00` | 53,030,000.00 USD | 427,790.00 USD | 0.00 USD | `+13.26%` | `167.43` |
| `Live` | `Short` | `2565.00` | 55,490,000.00 USD | 2,460,000.00 USD | 0.00 USD | `+13.71%` | `959.39` |
| `Live` | `Short` | `2575.00` | 67,100,000.00 USD | 11,610,000.00 USD | 0.00 USD | `+14.15%` | `4,508.33` |
| `Live` | `Short` | `2585.00` | 106,290,000.00 USD | 39,190,000.00 USD | 0.00 USD | `+14.59%` | `15,161.41` |
| `Live` | `Short` | `2595.00` | 106,940,000.00 USD | 657,040.00 USD | 0.00 USD | `+15.04%` | `253.20` |
| `Live` | `Short` | `2605.00` | 115,000,000.00 USD | 8,050,000.00 USD | 0.00 USD | `+15.48%` | `3,090.59` |
| `Live` | `Short` | `2615.00` | 121,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | `+15.92%` | `2,414.20` |
| `Live` | `Short` | `2625.00` | 121,690,000.00 USD | 377,520.00 USD | 0.00 USD | `+16.37%` | `143.82` |
| `Live` | `Short` | `2635.00` | 121,790,000.00 USD | 101,720.00 USD | 0.00 USD | `+16.81%` | `38.60` |
| `Live` | `Short` | `2645.00` | 121,920,000.00 USD | 130,220.00 USD | 0.00 USD | `+17.25%` | `49.23` |
| `Live` | `Short` | `2655.00` | 157,750,000.00 USD | 35,830,000.00 USD | 0.00 USD | `+17.70%` | `13,494.24` |
| `Live` | `Short` | `2665.00` | 158,080,000.00 USD | 332,690.00 USD | 0.00 USD | `+18.14%` | `124.84` |
| `Live` | `Short` | `2675.00` | 158,160,000.00 USD | 81,960.00 USD | 0.00 USD | `+18.58%` | `30.64` |
| `Live` | `Short` | `2685.00` | 159,070,000.00 USD | 907,340.00 USD | 0.00 USD | `+19.03%` | `337.93` |
| `Live` | `Short` | `2695.00` | 159,330,000.00 USD | 264,970.00 USD | 0.00 USD | `+19.47%` | `98.32` |
| `Live` | `Short` | `2705.00` | 188,820,000.00 USD | 29,490,000.00 USD | 0.00 USD | `+19.91%` | `10,901.03` |
| `Live` | `Short` | `2715.00` | 191,730,000.00 USD | 2,910,000.00 USD | 0.00 USD | `+20.36%` | `1,073.34` |
| `Live` | `Short` | `2725.00` | 193,250,000.00 USD | 1,510,000.00 USD | 0.00 USD | `+20.80%` | `555.22` |
| `Live` | `Short` | `2735.00` | 195,250,000.00 USD | 2,000,000.00 USD | 0.00 USD | `+21.24%` | `731.52` |
| `Live` | `Short` | `2745.00` | 196,130,000.00 USD | 883,220.00 USD | 0.00 USD | `+21.69%` | `321.76` |
| `Live` | `Short` | `2755.00` | 196,710,000.00 USD | 582,750.00 USD | 0.00 USD | `+22.13%` | `211.52` |
| `Live` | `Short` | `2765.00` | 199,130,000.00 USD | 2,410,000.00 USD | 0.00 USD | `+22.57%` | `873.34` |
| `Live` | `Short` | `2775.00` | 199,620,000.00 USD | 490,200.00 USD | 0.00 USD | `+23.02%` | `176.65` |
| `Live` | `Short` | `2785.00` | 201,460,000.00 USD | 1,850,000.00 USD | 0.00 USD | `+23.46%` | `663.04` |
| `Live` | `Short` | `2795.00` | 228,980,000.00 USD | 27,520,000.00 USD | 0.00 USD | `+23.90%` | `9,845.03` |
| `Live` | `Short` | `2805.00` | 246,420,000.00 USD | 17,440,000.00 USD | 0.00 USD | `+24.35%` | `6,216.59` |
| `Live` | `Short` | `2815.00` | 246,760,000.00 USD | 343,360.00 USD | 0.00 USD | `+24.79%` | `121.97` |
| `Live` | `Short` | `2825.00` | 246,830,000.00 USD | 63,940.00 USD | 0.00 USD | `+25.23%` | `22.63` |
| `Live` | `Short` | `2835.00` | 248,350,000.00 USD | 1,520,000.00 USD | 0.00 USD | `+25.68%` | `537.76` |
| `Live` | `Short` | `2845.00` | 250,380,000.00 USD | 2,030,000.00 USD | 0.00 USD | `+26.12%` | `713.07` |
| `Live` | `Short` | `2855.00` | 251,240,000.00 USD | 858,900.00 USD | 0.00 USD | `+26.56%` | `300.84` |
| `Live` | `Short` | `2865.00` | 251,340,000.00 USD | 102,680.00 USD | 0.00 USD | `+27.01%` | `35.84` |
| `Live` | `Short` | `2875.00` | 274,460,000.00 USD | 23,120,000.00 USD | 0.00 USD | `+27.45%` | `8,040.72` |
| `Live` | `Short` | `2885.00` | 279,230,000.00 USD | 4,770,000.00 USD | 0.00 USD | `+27.89%` | `1,652.91` |
| `Live` | `Short` | `2895.00` | 279,580,000.00 USD | 356,200.00 USD | 0.00 USD | `+28.34%` | `123.04` |
| `Live` | `Short` | `2905.00` | 280,510,000.00 USD | 925,630.00 USD | 0.00 USD | `+28.78%` | `318.63` |
| `Live` | `Short` | `2915.00` | 281,450,000.00 USD | 936,420.00 USD | 0.00 USD | `+29.22%` | `321.24` |
| `Live` | `Short` | `2925.00` | 281,450,000.00 USD | 4,770.00 USD | 0.00 USD | `+29.67%` | `1.63` |
| `Live` | `Short` | `2935.00` | 282,510,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+30.11%` | `360.71` |
| `Live` | `Short` | `2945.00` | 283,310,000.00 USD | 800,420.00 USD | 0.00 USD | `+30.55%` | `271.79` |
| `Live` | `Short` | `2955.00` | 283,430,000.00 USD | 120,380.00 USD | 0.00 USD | `+31.00%` | `40.74` |
| `Live` | `Short` | `2965.00` | 283,870,000.00 USD | 439,680.00 USD | 0.00 USD | `+31.44%` | `148.29` |
| `Live` | `Short` | `2975.00` | 284,310,000.00 USD | 445,190.00 USD | 0.00 USD | `+31.88%` | `149.64` |
| `Live` | `Short` | `2985.00` | 284,430,000.00 USD | 116,640.00 USD | 0.00 USD | `+32.33%` | `39.08` |
| `Live` | `Short` | `2995.00` | 313,330,000.00 USD | 28,900,000.00 USD | 0.00 USD | `+32.77%` | `9,648.62` |
| `Live` | `Short` | `3005.00` | 334,670,000.00 USD | 21,340,000.00 USD | 0.00 USD | `+33.21%` | `7,102.73` |
| `Live` | `Short` | `3015.00` | 334,980,000.00 USD | 311,790.00 USD | 0.00 USD | `+33.66%` | `103.41` |
| `Live` | `Short` | `3025.00` | 346,860,000.00 USD | 11,880,000.00 USD | 0.00 USD | `+34.10%` | `3,926.17` |
| `Live` | `Short` | `3035.00` | 352,910,000.00 USD | 6,050,000.00 USD | 0.00 USD | `+34.54%` | `1,993.91` |
| `Live` | `Short` | `3045.00` | 366,940,000.00 USD | 14,030,000.00 USD | 0.00 USD | `+34.99%` | `4,607.22` |
| `Live` | `Short` | `3055.00` | 369,150,000.00 USD | 2,210,000.00 USD | 0.00 USD | `+35.43%` | `723.11` |
| `Live` | `Short` | `3065.00` | 375,350,000.00 USD | 6,200,000.00 USD | 0.00 USD | `+35.87%` | `2,022.57` |
| `Live` | `Short` | `3075.00` | 380,260,000.00 USD | 4,910,000.00 USD | 0.00 USD | `+36.32%` | `1,595.66` |
| `Live` | `Short` | `3085.00` | 380,900,000.00 USD | 641,160.00 USD | 0.00 USD | `+36.76%` | `207.83` |
| `Live` | `Short` | `3095.00` | 381,280,000.00 USD | 378,770.00 USD | 0.00 USD | `+37.20%` | `122.38` |
| `Live` | `Short` | `3105.00` | 382,890,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+37.65%` | `519.79` |
| `Live` | `Short` | `3115.00` | 382,980,000.00 USD | 91,040.00 USD | 0.00 USD | `+38.09%` | `29.23` |
| `Live` | `Short` | `3125.00` | 383,420,000.00 USD | 435,030.00 USD | 0.00 USD | `+38.53%` | `139.21` |
| `Live` | `Short` | `3135.00` | 383,560,000.00 USD | 146,570.00 USD | 0.00 USD | `+38.98%` | `46.75` |
| `Live` | `Short` | `3145.00` | 389,520,000.00 USD | 5,960,000.00 USD | 0.00 USD | `+39.42%` | `1,895.12` |
| `Live` | `Short` | `3155.00` | 389,660,000.00 USD | 136,700.00 USD | 0.00 USD | `+39.86%` | `43.33` |
| `Live` | `Short` | `3165.00` | 389,700,000.00 USD | 39,870.00 USD | 0.00 USD | `+40.30%` | `12.60` |
| `Live` | `Short` | `3175.00` | 390,360,000.00 USD | 665,110.00 USD | 0.00 USD | `+40.75%` | `209.48` |
| `Live` | `Short` | `3185.00` | 397,430,000.00 USD | 7,060,000.00 USD | 0.00 USD | `+41.19%` | `2,217.05` |
| `Live` | `Short` | `3195.00` | 404,900,000.00 USD | 7,470,000.00 USD | 0.00 USD | `+41.63%` | `2,338.12` |
| `Live` | `Short` | `3205.00` | 405,170,000.00 USD | 269,580.00 USD | 0.00 USD | `+42.08%` | `84.11` |
| `Live` | `Short` | `3215.00` | 405,720,000.00 USD | 559,270.00 USD | 0.00 USD | `+42.52%` | `173.96` |
| `Live` | `Short` | `3225.00` | 406,180,000.00 USD | 450,020.00 USD | 0.00 USD | `+42.96%` | `139.54` |
| `Live` | `Short` | `3235.00` | 414,830,000.00 USD | 8,650,000.00 USD | 0.00 USD | `+43.41%` | `2,674.68` |
| `Live` | `Short` | `3245.00` | 420,030,000.00 USD | 5,200,000.00 USD | 0.00 USD | `+43.85%` | `1,602.01` |
| `Live` | `Short` | `3255.00` | 420,080,000.00 USD | 49,820.00 USD | 0.00 USD | `+44.29%` | `15.31` |
| `Live` | `Short` | `3265.00` | 420,110,000.00 USD | 36,160.00 USD | 0.00 USD | `+44.74%` | `11.07` |
| `Live` | `Short` | `3275.00` | 420,140,000.00 USD | 28,270.00 USD | 0.00 USD | `+45.18%` | `8.63` |
| `Live` | `Short` | `3285.00` | 429,230,000.00 USD | 9,090,000.00 USD | 0.00 USD | `+45.62%` | `2,766.81` |
| `Live` | `Short` | `3295.00` | 429,360,000.00 USD | 135,520.00 USD | 0.00 USD | `+46.07%` | `41.13` |
| `Live` | `Short` | `3305.00` | 431,250,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+46.51%` | `571.69` |
| `Live` | `Short` | `3315.00` | 431,930,000.00 USD | 680,260.00 USD | 0.00 USD | `+46.95%` | `205.21` |
| `Live` | `Short` | `3325.00` | 437,040,000.00 USD | 5,100,000.00 USD | 0.00 USD | `+47.40%` | `1,535.33` |
| `Live` | `Short` | `3335.00` | 437,040,000.00 USD | 1,250.00 USD | 0.00 USD | `+47.84%` | `0.37` |
| `Live` | `Short` | `3345.00` | 501,000,000.00 USD | 63,960,000.00 USD | 0.00 USD | `+48.28%` | `19,119.85` |
| `Live` | `Short` | `3355.00` | 501,250,000.00 USD | 250,060.00 USD | 0.00 USD | `+48.73%` | `74.53` |
| `Live` | `Short` | `3365.00` | 501,690,000.00 USD | 443,200.00 USD | 0.00 USD | `+49.17%` | `131.71` |
| `Live` | `Short` | `3375.00` | 501,750,000.00 USD | 56,640.00 USD | 0.00 USD | `+49.61%` | `16.78` |
| `Live` | `Short` | `3385.00` | 501,920,000.00 USD | 169,370.00 USD | 0.00 USD | `+50.06%` | `50.04` |
| `Live` | `Short` | `3395.00` | 501,940,000.00 USD | 22,730.00 USD | 0.00 USD | `+50.50%` | `6.69` |
| `Live` | `Short` | `3405.00` | 502,290,000.00 USD | 348,080.00 USD | 0.00 USD | `+50.94%` | `102.23` |
| `Live` | `Short` | `3415.00` | 502,300,000.00 USD | 16,120.00 USD | 0.00 USD | `+51.39%` | `4.72` |
| `Live` | `Short` | `3425.00` | 517,280,000.00 USD | 14,980,000.00 USD | 0.00 USD | `+51.83%` | `4,374.35` |
| `Live` | `Short` | `3435.00` | 517,410,000.00 USD | 129,440.00 USD | 0.00 USD | `+52.27%` | `37.68` |
| `Live` | `Short` | `3445.00` | 517,770,000.00 USD | 353,520.00 USD | 0.00 USD | `+52.72%` | `102.62` |
| `Live` | `Short` | `3455.00` | 518,420,000.00 USD | 653,270.00 USD | 0.00 USD | `+53.16%` | `189.08` |
| `Live` | `Short` | `3465.00` | 518,840,000.00 USD | 419,220.00 USD | 0.00 USD | `+53.60%` | `120.99` |
| `Live` | `Short` | `3475.00` | 519,160,000.00 USD | 314,730.00 USD | 0.00 USD | `+54.05%` | `90.57` |
| `Live` | `Short` | `3485.00` | 520,980,000.00 USD | 1,820,000.00 USD | 0.00 USD | `+54.49%` | `522.47` |
| `Live` | `Short` | `3495.00` | 522,100,000.00 USD | 1,120,000.00 USD | 0.00 USD | `+54.93%` | `320.37` |
| `Live` | `Short` | `3505.00` | 522,130,000.00 USD | 30,560.00 USD | 0.00 USD | `+55.38%` | `8.72` |
| `Live` | `Short` | `3515.00` | 522,230,000.00 USD | 100,980.00 USD | 0.00 USD | `+55.82%` | `28.73` |
| `Live` | `Short` | `3525.00` | 522,340,000.00 USD | 114,170.00 USD | 0.00 USD | `+56.26%` | `32.39` |
| `Live` | `Short` | `3535.00` | 522,790,000.00 USD | 452,410.00 USD | 0.00 USD | `+56.71%` | `127.98` |
| `Live` | `Short` | `3545.00` | 523,120,000.00 USD | 322,810.00 USD | 0.00 USD | `+57.15%` | `91.06` |
| `Live` | `Short` | `3555.00` | 523,280,000.00 USD | 166,730.00 USD | 0.00 USD | `+57.59%` | `46.90` |
| `Live` | `Short` | `3565.00` | 523,320,000.00 USD | 41,050.00 USD | 0.00 USD | `+58.04%` | `11.51` |
| `Live` | `Short` | `3575.00` | 523,580,000.00 USD | 259,380.00 USD | 0.00 USD | `+58.48%` | `72.55` |
| `Live` | `Short` | `3585.00` | 524,240,000.00 USD | 653,660.00 USD | 0.00 USD | `+58.92%` | `182.33` |
| `Live` | `Short` | `3595.00` | 524,830,000.00 USD | 594,390.00 USD | 0.00 USD | `+59.37%` | `165.34` |
| `Live` | `Short` | `3605.00` | 525,280,000.00 USD | 451,440.00 USD | 0.00 USD | `+59.81%` | `125.23` |
| `Live` | `Short` | `3615.00` | 529,120,000.00 USD | 3,840,000.00 USD | 0.00 USD | `+60.25%` | `1,061.91` |
| `Live` | `Short` | `3625.00` | 529,680,000.00 USD | 561,790.00 USD | 0.00 USD | `+60.70%` | `154.98` |
| `Live` | `Short` | `3635.00` | 529,760,000.00 USD | 78,000.00 USD | 0.00 USD | `+61.14%` | `21.46` |
| `Live` | `Short` | `3645.00` | 529,820,000.00 USD | 58,500.00 USD | 0.00 USD | `+61.58%` | `16.05` |
| `Live` | `Short` | `3655.00` | 536,310,000.00 USD | 6,490,000.00 USD | 0.00 USD | `+62.03%` | `1,774.53` |
| `Live` | `Short` | `3665.00` | 536,310,000.00 USD | 1,080.00 USD | 0.00 USD | `+62.47%` | `0.30` |
| `Live` | `Short` | `3675.00` | 536,650,000.00 USD | 345,650.00 USD | 0.00 USD | `+62.91%` | `94.05` |
| `Live` | `Short` | `3685.00` | 536,850,000.00 USD | 199,270.00 USD | 0.00 USD | `+63.36%` | `54.08` |
| `Live` | `Short` | `3695.00` | 537,030,000.00 USD | 177,010.00 USD | 0.00 USD | `+63.80%` | `47.90` |
| `Live` | `Short` | `3705.00` | 537,120,000.00 USD | 91,260.00 USD | 0.00 USD | `+64.24%` | `24.63` |
| `Live` | `Short` | `3715.00` | 537,120,000.00 USD | 1,460.00 USD | 0.00 USD | `+64.69%` | `0.39` |
| `Live` | `Short` | `3725.00` | 544,860,000.00 USD | 7,730,000.00 USD | 0.00 USD | `+65.13%` | `2,076.21` |
| `Live` | `Short` | `3735.00` | 545,110,000.00 USD | 253,270.00 USD | 0.00 USD | `+65.57%` | `67.81` |
| `Live` | `Short` | `3745.00` | 548,250,000.00 USD | 3,140,000.00 USD | 0.00 USD | `+66.02%` | `838.14` |
| `Live` | `Short` | `3755.00` | 548,690,000.00 USD | 441,280.00 USD | 0.00 USD | `+66.46%` | `117.52` |
| `Live` | `Short` | `3765.00` | 548,750,000.00 USD | 60,370.00 USD | 0.00 USD | `+66.90%` | `16.03` |
| `Live` | `Short` | `3775.00` | 550,200,000.00 USD | 1,450,000.00 USD | 0.00 USD | `+67.35%` | `385.10` |
| `Live` | `Short` | `3785.00` | 550,200,000.00 USD | 302.04 USD | 0.00 USD | `+67.79%` | `0.08` |
| `Live` | `Short` | `3795.00` | 550,400,000.00 USD | 201,250.00 USD | 0.00 USD | `+68.23%` | `53.03` |
| `Live` | `Short` | `3805.00` | 551,600,000.00 USD | 1,190,000.00 USD | 0.00 USD | `+68.68%` | `313.97` |
| `Live` | `Short` | `3815.00` | 551,650,000.00 USD | 50,430.00 USD | 0.00 USD | `+69.12%` | `13.22` |
| `Live` | `Short` | `3825.00` | 567,040,000.00 USD | 15,390,000.00 USD | 0.00 USD | `+69.56%` | `4,023.96` |
| `Live` | `Short` | `3835.00` | 567,340,000.00 USD | 303,210.00 USD | 0.00 USD | `+70.01%` | `79.06` |
| `Live` | `Short` | `3845.00` | 567,350,000.00 USD | 6,310.00 USD | 0.00 USD | `+70.45%` | `1.64` |
| `Live` | `Short` | `3855.00` | 604,310,000.00 USD | 36,960,000.00 USD | 0.00 USD | `+70.89%` | `9,587.09` |
| `Live` | `Short` | `3865.00` | 606,630,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+71.34%` | `599.82` |
| `Live` | `Short` | `3875.00` | 607,770,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+71.78%` | `295.65` |
| `Live` | `Short` | `3885.00` | 609,220,000.00 USD | 1,450,000.00 USD | 0.00 USD | `+72.22%` | `371.95` |
| `Live` | `Short` | `3895.00` | 609,970,000.00 USD | 754,120.00 USD | 0.00 USD | `+72.67%` | `193.61` |
| `Live` | `Short` | `3905.00` | 610,590,000.00 USD | 614,900.00 USD | 0.00 USD | `+73.11%` | `157.46` |
| `Live` | `Short` | `3915.00` | 610,630,000.00 USD | 37,820.00 USD | 0.00 USD | `+73.55%` | `9.66` |
| `Live` | `Short` | `3925.00` | 610,790,000.00 USD | 167,860.00 USD | 0.00 USD | `+74.00%` | `42.77` |
| `Live` | `Short` | `3935.00` | 619,950,000.00 USD | 9,160,000.00 USD | 0.00 USD | `+74.44%` | `2,326.65` |
| `Live` | `Short` | `3945.00` | 621,910,000.00 USD | 1,960,000.00 USD | 0.00 USD | `+74.88%` | `497.84` |
| `Live` | `Short` | `3955.00` | 622,260,000.00 USD | 344,680.00 USD | 0.00 USD | `+75.33%` | `87.15` |
| `Live` | `Short` | `3965.00` | 1,040,000,000.00 USD | 422,490,000.00 USD | 0.00 USD | `+75.77%` | `106,554.48` |
| `Live` | `Short` | `3975.00` | 1,050,000,000.00 USD | 638,270.00 USD | 0.00 USD | `+76.21%` | `160.57` |
| `Live` | `Short` | `3985.00` | 1,050,000,000.00 USD | 651,130.00 USD | 0.00 USD | `+76.66%` | `163.39` |
| `Live` | `Short` | `3995.00` | 1,140,000,000.00 USD | 97,130,000.00 USD | 0.00 USD | `+77.10%` | `24,311.92` |
| `Live` | `Short` | `4005.00` | 1,140,000,000.00 USD | 137,710.00 USD | 0.00 USD | `+77.54%` | `34.38` |
| `Live` | `Short` | `4015.00` | 1,170,000,000.00 USD | 30,620,000.00 USD | 0.00 USD | `+77.99%` | `7,625.56` |
| `Live` | `Short` | `4025.00` | 1,170,000,000.00 USD | 173,310.00 USD | 0.00 USD | `+78.43%` | `43.06` |
| `Live` | `Short` | `4035.00` | 1,170,000,000.00 USD | 75,870.00 USD | 0.00 USD | `+78.87%` | `18.80` |
| `Live` | `Short` | `4045.00` | 1,170,000,000.00 USD | 283,770.00 USD | 0.00 USD | `+79.32%` | `70.15` |
| `Live` | `Short` | `4055.00` | 1,180,000,000.00 USD | 1,620,000.00 USD | 0.00 USD | `+79.76%` | `398.54` |
| `Live` | `Short` | `4065.00` | 1,270,000,000.00 USD | 92,190,000.00 USD | 0.00 USD | `+80.20%` | `22,679.74` |
| `Live` | `Short` | `4075.00` | 1,270,000,000.00 USD | 67,510.00 USD | 0.00 USD | `+80.65%` | `16.57` |
| `Live` | `Short` | `4085.00` | 1,270,000,000.00 USD | 2,950.00 USD | 0.00 USD | `+81.09%` | `0.72` |
| `Live` | `Short` | `4095.00` | 1,270,000,000.00 USD | 3,610.00 USD | 0.00 USD | `+81.53%` | `0.88` |
| `Live` | `Short` | `4105.00` | 1,270,000,000.00 USD | 2,860,000.00 USD | 0.00 USD | `+81.98%` | `696.12` |
| `Live` | `Short` | `4115.00` | 1,270,000,000.00 USD | 2,770,000.00 USD | 0.00 USD | `+82.42%` | `672.00` |
| `Live` | `Short` | `4125.00` | 1,280,000,000.00 USD | 1,840,000.00 USD | 0.00 USD | `+82.86%` | `446.26` |
| `Live` | `Short` | `4135.00` | 1,280,000,000.00 USD | 38,810.00 USD | 0.00 USD | `+83.31%` | `9.39` |
| `Live` | `Short` | `4145.00` | 1,350,000,000.00 USD | 69,260,000.00 USD | 0.00 USD | `+83.75%` | `16,709.46` |
| `Live` | `Short` | `4155.00` | 1,350,000,000.00 USD | 1,300,000.00 USD | 0.00 USD | `+84.19%` | `312.39` |
| `Live` | `Short` | `4165.00` | 1,350,000,000.00 USD | 119,050.00 USD | 0.00 USD | `+84.64%` | `28.58` |
| `Live` | `Short` | `4175.00` | 1,350,000,000.00 USD | 74,620.00 USD | 0.00 USD | `+85.08%` | `17.87` |
| `Live` | `Short` | `4185.00` | 1,350,000,000.00 USD | 912,150.00 USD | 0.00 USD | `+85.52%` | `217.96` |
| `Live` | `Short` | `4195.00` | 1,350,000,000.00 USD | 4,040,000.00 USD | 0.00 USD | `+85.97%` | `962.89` |
| `Live` | `Short` | `4205.00` | 1,350,000,000.00 USD | 474,120.00 USD | 0.00 USD | `+86.41%` | `112.75` |
| `Live` | `Short` | `4215.00` | 1,350,000,000.00 USD | 134,220.00 USD | 0.00 USD | `+86.85%` | `31.84` |
| `Live` | `Short` | `4225.00` | 1,350,000,000.00 USD | 426,730.00 USD | 0.00 USD | `+87.29%` | `101.00` |
| `Live` | `Short` | `4235.00` | 1,350,000,000.00 USD | 1,770.00 USD | 0.00 USD | `+87.74%` | `0.42` |
| `Live` | `Short` | `4245.00` | 1,350,000,000.00 USD | 183,240.00 USD | 0.00 USD | `+88.18%` | `43.16` |
| `Live` | `Short` | `4255.00` | 1,350,000,000.00 USD | 7,960.00 USD | 0.00 USD | `+88.62%` | `1.87` |
| `Live` | `Short` | `4265.00` | 1,350,000,000.00 USD | 54,700.00 USD | 0.00 USD | `+89.07%` | `12.83` |
| `Live` | `Short` | `4275.00` | 1,360,000,000.00 USD | 3,930,000.00 USD | 0.00 USD | `+89.51%` | `919.98` |
| `Live` | `Short` | `4285.00` | 1,360,000,000.00 USD | 2,340.00 USD | 0.00 USD | `+89.95%` | `0.55` |
| `Live` | `Short` | `4295.00` | 1,360,000,000.00 USD | 5,130.00 USD | 0.00 USD | `+90.40%` | `1.20` |
| `Live` | `Short` | `4305.00` | 1,360,000,000.00 USD | 86,350.00 USD | 0.00 USD | `+90.84%` | `20.06` |
| `Live` | `Short` | `4315.00` | 1,370,000,000.00 USD | 17,190,000.00 USD | 0.00 USD | `+91.28%` | `3,983.61` |
| `Live` | `Short` | `4325.00` | 1,370,000,000.00 USD | 665,130.00 USD | 0.00 USD | `+91.73%` | `153.79` |
| `Live` | `Short` | `4335.00` | 1,370,000,000.00 USD | 19,070.00 USD | 0.00 USD | `+92.17%` | `4.40` |
| `Live` | `Short` | `4345.00` | 1,370,000,000.00 USD | 9,010.00 USD | 0.00 USD | `+92.61%` | `2.07` |
| `Live` | `Short` | `4355.00` | 1,370,000,000.00 USD | 6,290.00 USD | 0.00 USD | `+93.06%` | `1.45` |
| `Live` | `Short` | `4365.00` | 1,380,000,000.00 USD | 561,310.00 USD | 0.00 USD | `+93.50%` | `128.59` |
| `Live` | `Short` | `4375.00` | 1,380,000,000.00 USD | 183,960.00 USD | 0.00 USD | `+93.94%` | `42.05` |
| `Live` | `Short` | `4385.00` | 1,380,000,000.00 USD | 9,140.00 USD | 0.00 USD | `+94.39%` | `2.08` |
| `Live` | `Short` | `4395.00` | 1,380,000,000.00 USD | 14,870.00 USD | 0.00 USD | `+94.83%` | `3.38` |
| `Live` | `Short` | `4405.00` | 1,380,000,000.00 USD | 27,690.00 USD | 0.00 USD | `+95.27%` | `6.29` |
| `Live` | `Short` | `4415.00` | 1,380,000,000.00 USD | 107,920.00 USD | 0.00 USD | `+95.72%` | `24.44` |
| `Live` | `Short` | `4425.00` | 1,380,000,000.00 USD | 89,600.00 USD | 0.00 USD | `+96.16%` | `20.25` |
| `Live` | `Short` | `4435.00` | 1,380,000,000.00 USD | 3,160,000.00 USD | 0.00 USD | `+96.60%` | `712.58` |
| `Live` | `Short` | `4445.00` | 1,380,000,000.00 USD | 400,050.00 USD | 0.00 USD | `+97.05%` | `90.00` |
| `Live` | `Short` | `4455.00` | 1,400,000,000.00 USD | 19,610,000.00 USD | 0.00 USD | `+97.49%` | `4,402.58` |
| `Live` | `Short` | `4465.00` | 1,400,000,000.00 USD | 784,700.00 USD | 0.00 USD | `+97.93%` | `175.74` |
| `Live` | `Short` | `4475.00` | 1,400,000,000.00 USD | 141,570.00 USD | 0.00 USD | `+98.38%` | `31.64` |
| `Live` | `Short` | `4485.00` | 1,400,000,000.00 USD | 1,660,000.00 USD | 0.00 USD | `+98.82%` | `370.90` |
| `Live` | `Short` | `4495.00` | 1,400,000,000.00 USD | 157,460.00 USD | 0.00 USD | `+99.26%` | `35.03` |
| `Live` | `Short` | `4505.00` | 1,400,000,000.00 USD | 94,780.00 USD | 0.00 USD | `+99.71%` | `21.04` |
| `Live` | `Short` | `4515.00` | 1,400,000,000.00 USD | 26,640.00 USD | 0.00 USD | `+100.15%` | `5.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `505.00` | 64,070,000.00 USD | 0.00 USD | 16,090.00 USD | `-77.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 64,050,000.00 USD | 0.00 USD | 563.16 USD | `-75.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 64,050,000.00 USD | 0.00 USD | 885.90 USD | `-68.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 64,050,000.00 USD | 0.00 USD | 177.27 USD | `-66.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `795.00` | 64,050,000.00 USD | 0.00 USD | 104.22 USD | `-64.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 64,050,000.00 USD | 0.00 USD | 2,090.00 USD | `-64.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 64,050,000.00 USD | 0.00 USD | 1,670.00 USD | `-62.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 64,050,000.00 USD | 0.00 USD | 139,280.00 USD | `-61.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 63,910,000.00 USD | 0.00 USD | 3,130.00 USD | `-60.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 63,900,000.00 USD | 0.00 USD | 2,780.00 USD | `-59.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 63,900,000.00 USD | 0.00 USD | 516.34 USD | `-56.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 63,900,000.00 USD | 0.00 USD | 100.50 USD | `-55.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 63,900,000.00 USD | 0.00 USD | 222,040.00 USD | `-55.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 63,680,000.00 USD | 0.00 USD | 438.28 USD | `-55.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 63,680,000.00 USD | 0.00 USD | 112.03 USD | `-54.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 63,680,000.00 USD | 0.00 USD | 1,060.00 USD | `-52.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 63,680,000.00 USD | 0.00 USD | 995.34 USD | `-52.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 63,680,000.00 USD | 0.00 USD | 1,610.00 USD | `-51.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 63,670,000.00 USD | 0.00 USD | 11,050.00 USD | `-50.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 63,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-50.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 63,660,000.00 USD | 0.00 USD | 1,000.00 USD | `-48.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 63,660,000.00 USD | 0.00 USD | 203.98 USD | `-47.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 63,660,000.00 USD | 0.00 USD | 228.47 USD | `-47.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 63,660,000.00 USD | 0.00 USD | 3,110.00 USD | `-46.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 63,660,000.00 USD | 0.00 USD | 995.93 USD | `-45.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 63,660,000.00 USD | 0.00 USD | 951.93 USD | `-44.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 63,660,000.00 USD | 0.00 USD | 6,810.00 USD | `-44.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 63,650,000.00 USD | 0.00 USD | 9,050.00 USD | `-43.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 63,640,000.00 USD | 0.00 USD | 7,030.00 USD | `-42.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 63,630,000.00 USD | 0.00 USD | 23,030.00 USD | `-42.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 63,610,000.00 USD | 0.00 USD | 1,440.00 USD | `-41.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 63,610,000.00 USD | 0.00 USD | 141,950.00 USD | `-40.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 63,470,000.00 USD | 0.00 USD | 128.86 USD | `-39.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 63,470,000.00 USD | 0.00 USD | 1,270.00 USD | `-39.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 63,460,000.00 USD | 0.00 USD | 4,160.00 USD | `-39.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 63,460,000.00 USD | 0.00 USD | 535,600.00 USD | `-38.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 62,920,000.00 USD | 0.00 USD | 20,270.00 USD | `-37.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 62,900,000.00 USD | 0.00 USD | 6,450.00 USD | `-36.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 62,900,000.00 USD | 0.00 USD | 852.10 USD | `-36.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 62,900,000.00 USD | 0.00 USD | 1,490.00 USD | `-35.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 62,900,000.00 USD | 0.00 USD | 5,680.00 USD | `-35.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 62,890,000.00 USD | 0.00 USD | 19,460.00 USD | `-35.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 62,870,000.00 USD | 0.00 USD | 2,600.00 USD | `-34.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 62,870,000.00 USD | 0.00 USD | 18,710.00 USD | `-34.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 62,850,000.00 USD | 0.00 USD | 11,570.00 USD | `-33.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 62,840,000.00 USD | 0.00 USD | 89,400.00 USD | `-33.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 62,750,000.00 USD | 0.00 USD | 11,140.00 USD | `-32.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 62,740,000.00 USD | 0.00 USD | 32,310.00 USD | `-32.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 62,710,000.00 USD | 0.00 USD | 983.78 USD | `-31.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 62,700,000.00 USD | 0.00 USD | 17,470.00 USD | `-31.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 62,690,000.00 USD | 0.00 USD | 25,980.00 USD | `-31.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 62,660,000.00 USD | 0.00 USD | 6,260.00 USD | `-30.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 62,650,000.00 USD | 0.00 USD | 190,890.00 USD | `-30.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 62,460,000.00 USD | 0.00 USD | 3,390.00 USD | `-29.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 62,460,000.00 USD | 0.00 USD | 4,040.00 USD | `-29.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 62,460,000.00 USD | 0.00 USD | 437,510.00 USD | `-28.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 62,020,000.00 USD | 0.00 USD | 25,840.00 USD | `-28.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 61,990,000.00 USD | 0.00 USD | 13,590.00 USD | `-27.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 61,980,000.00 USD | 0.00 USD | 5,510.00 USD | `-27.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 61,970,000.00 USD | 0.00 USD | 328,140.00 USD | `-27.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 61,650,000.00 USD | 0.00 USD | 35,070.00 USD | `-26.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 61,610,000.00 USD | 0.00 USD | 3,110.00 USD | `-26.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 61,610,000.00 USD | 0.00 USD | 3,440.00 USD | `-25.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 61,600,000.00 USD | 0.00 USD | 35,300.00 USD | `-25.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 61,570,000.00 USD | 0.00 USD | 8,490.00 USD | `-24.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 61,560,000.00 USD | 0.00 USD | 81,450.00 USD | `-24.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 61,480,000.00 USD | 0.00 USD | 18,650.00 USD | `-23.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 61,460,000.00 USD | 0.00 USD | 47,500.00 USD | `-23.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 61,410,000.00 USD | 0.00 USD | 28,150.00 USD | `-23.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 61,380,000.00 USD | 0.00 USD | 3,180.00 USD | `-22.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 61,380,000.00 USD | 0.00 USD | 502,310.00 USD | `-22.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 60,880,000.00 USD | 0.00 USD | 76,460.00 USD | `-21.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 60,800,000.00 USD | 0.00 USD | 3,090.00 USD | `-21.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 60,800,000.00 USD | 0.00 USD | 8,500.00 USD | `-20.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 60,790,000.00 USD | 0.00 USD | 184,330.00 USD | `-20.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 60,610,000.00 USD | 0.00 USD | 318,970.00 USD | `-19.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 60,290,000.00 USD | 0.00 USD | 114,830.00 USD | `-19.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 60,170,000.00 USD | 0.00 USD | 26,810.00 USD | `-19.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 60,150,000.00 USD | 0.00 USD | 2,110.00 USD | `-18.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 60,140,000.00 USD | 0.00 USD | 14,290.00 USD | `-18.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 60,130,000.00 USD | 0.00 USD | 466,540.00 USD | `-17.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 59,660,000.00 USD | 0.00 USD | 33,750.00 USD | `-17.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 59,630,000.00 USD | 0.00 USD | 18,210,000.00 USD | `-16.88%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 41,420,000.00 USD | 0.00 USD | 2,500.00 USD | `-16.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 41,420,000.00 USD | 0.00 USD | 64,540.00 USD | `-15.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 41,350,000.00 USD | 0.00 USD | 151,500.00 USD | `-15.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 41,200,000.00 USD | 0.00 USD | 8,130,000.00 USD | `-15.11%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1925.00` | 33,070,000.00 USD | 0.00 USD | 16,410,000.00 USD | `-14.66%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 16,660,000.00 USD | 0.00 USD | 79,950.00 USD | `-14.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 16,580,000.00 USD | 0.00 USD | 46,890.00 USD | `-13.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 16,530,000.00 USD | 0.00 USD | 54,590.00 USD | `-13.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 16,480,000.00 USD | 0.00 USD | 17,890.00 USD | `-12.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 16,460,000.00 USD | 0.00 USD | 91,390.00 USD | `-12.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 16,370,000.00 USD | 0.00 USD | 112,950.00 USD | `-12.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 16,260,000.00 USD | 0.00 USD | 232,340.00 USD | `-11.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 16,020,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-11.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 14,610,000.00 USD | 0.00 USD | 67,680.00 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 14,540,000.00 USD | 0.00 USD | 535,570.00 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 14,010,000.00 USD | 0.00 USD | 99,030.00 USD | `-9.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 13,910,000.00 USD | 0.00 USD | 96,580.00 USD | `-9.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 13,810,000.00 USD | 0.00 USD | 270,770.00 USD | `-8.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 13,540,000.00 USD | 0.00 USD | 48,870.00 USD | `-8.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 13,490,000.00 USD | 0.00 USD | 29,190.00 USD | `-8.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 13,460,000.00 USD | 0.00 USD | 65,010.00 USD | `-7.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 13,400,000.00 USD | 0.00 USD | 55,120.00 USD | `-7.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 13,340,000.00 USD | 0.00 USD | 208,210.00 USD | `-6.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 13,130,000.00 USD | 0.00 USD | 128,360.00 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 13,000,000.00 USD | 0.00 USD | 203,330.00 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 12,800,000.00 USD | 0.00 USD | 36,510.00 USD | `-5.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 12,760,000.00 USD | 0.00 USD | 60,600.00 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 12,700,000.00 USD | 0.00 USD | 141,880.00 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 12,560,000.00 USD | 0.00 USD | 925,420.00 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 11,640,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2185.00` | 10,270,000.00 USD | 0.00 USD | 401,770.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 9,870,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 8,750,000.00 USD | 0.00 USD | 3,990,000.00 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 4,760,000.00 USD | 0.00 USD | 865,000.00 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 3,890,000.00 USD | 0.00 USD | 2,270,000.00 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2235.00` | 1,620,000.00 USD | 0.00 USD | 1,240,000.00 USD | `-0.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2245.00` | 385,420.00 USD | 0.00 USD | 359,100.00 USD | `-0.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2255.00` | 26,320.00 USD | 0.00 USD | 26,320.00 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2265.00` | 4,550.00 USD | 4,550.00 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 2,000,000.00 USD | 1,990,000.00 USD | 0.00 USD | `+0.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 2,830,000.00 USD | 833,160.00 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 5,290,000.00 USD | 2,460,000.00 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 5,950,000.00 USD | 661,450.00 USD | 0.00 USD | `+2.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2315.00` | 7,220,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+2.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 7,460,000.00 USD | 231,480.00 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 7,480,000.00 USD | 25,140.00 USD | 0.00 USD | `+3.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 8,830,000.00 USD | 1,350,000.00 USD | 0.00 USD | `+3.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 11,950,000.00 USD | 3,120,000.00 USD | 0.00 USD | `+4.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 12,250,000.00 USD | 299,370.00 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 12,450,000.00 USD | 205,540.00 USD | 0.00 USD | `+5.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 13,050,000.00 USD | 598,090.00 USD | 0.00 USD | `+5.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 14,500,000.00 USD | 1,450,000.00 USD | 0.00 USD | `+6.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 16,440,000.00 USD | 1,950,000.00 USD | 0.00 USD | `+6.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 16,840,000.00 USD | 393,820.00 USD | 0.00 USD | `+7.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 19,840,000.00 USD | 3,000,000.00 USD | 0.00 USD | `+7.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 20,060,000.00 USD | 222,810.00 USD | 0.00 USD | `+7.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 30,420,000.00 USD | 10,360,000.00 USD | 0.00 USD | `+8.39%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2455.00` | 30,600,000.00 USD | 176,000.00 USD | 0.00 USD | `+8.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 32,740,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+9.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 32,930,000.00 USD | 190,740.00 USD | 0.00 USD | `+9.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 35,060,000.00 USD | 2,130,000.00 USD | 0.00 USD | `+10.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 35,500,000.00 USD | 439,220.00 USD | 0.00 USD | `+10.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 40,550,000.00 USD | 5,050,000.00 USD | 0.00 USD | `+11.05%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2515.00` | 48,280,000.00 USD | 7,740,000.00 USD | 0.00 USD | `+11.49%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 51,650,000.00 USD | 3,370,000.00 USD | 0.00 USD | `+11.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 51,720,000.00 USD | 73,340.00 USD | 0.00 USD | `+12.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 53,870,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+12.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 54,180,000.00 USD | 303,910.00 USD | 0.00 USD | `+13.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 56,550,000.00 USD | 2,370,000.00 USD | 0.00 USD | `+13.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 56,670,000.00 USD | 123,300.00 USD | 0.00 USD | `+14.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 59,360,000.00 USD | 2,690,000.00 USD | 0.00 USD | `+14.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 59,370,000.00 USD | 14,370.00 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 62,370,000.00 USD | 3,000,000.00 USD | 0.00 USD | `+15.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 62,510,000.00 USD | 144,740.00 USD | 0.00 USD | `+15.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 64,680,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+16.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 64,850,000.00 USD | 172,380.00 USD | 0.00 USD | `+16.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 67,000,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+17.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 67,250,000.00 USD | 251,180.00 USD | 0.00 USD | `+17.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 69,390,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+18.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 69,740,000.00 USD | 351,060.00 USD | 0.00 USD | `+18.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 71,930,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+19.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 72,020,000.00 USD | 95,970.00 USD | 0.00 USD | `+19.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 76,490,000.00 USD | 4,470,000.00 USD | 0.00 USD | `+19.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 76,570,000.00 USD | 76,590.00 USD | 0.00 USD | `+20.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 79,040,000.00 USD | 2,470,000.00 USD | 0.00 USD | `+20.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 79,090,000.00 USD | 55,230.00 USD | 0.00 USD | `+21.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 81,350,000.00 USD | 2,260,000.00 USD | 0.00 USD | `+21.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 82,030,000.00 USD | 681,740.00 USD | 0.00 USD | `+22.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 84,420,000.00 USD | 2,380,000.00 USD | 0.00 USD | `+22.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 84,990,000.00 USD | 577,690.00 USD | 0.00 USD | `+23.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 87,260,000.00 USD | 2,270,000.00 USD | 0.00 USD | `+23.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 87,280,000.00 USD | 17,550.00 USD | 0.00 USD | `+23.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 91,530,000.00 USD | 4,240,000.00 USD | 0.00 USD | `+24.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 91,580,000.00 USD | 52,670.00 USD | 0.00 USD | `+24.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 91,640,000.00 USD | 63,490.00 USD | 0.00 USD | `+25.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 91,930,000.00 USD | 289,000.00 USD | 0.00 USD | `+25.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 92,940,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+26.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 94,330,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+26.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 94,340,000.00 USD | 10,290.00 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 94,340,000.00 USD | 2,460.00 USD | 0.00 USD | `+27.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 94,650,000.00 USD | 303,660.00 USD | 0.00 USD | `+27.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 94,670,000.00 USD | 21,290.00 USD | 0.00 USD | `+28.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 96,140,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+28.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 96,160,000.00 USD | 10,340.00 USD | 0.00 USD | `+29.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 96,160,000.00 USD | 3,050.00 USD | 0.00 USD | `+29.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 96,210,000.00 USD | 52,910.00 USD | 0.00 USD | `+30.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 96,250,000.00 USD | 34,650.00 USD | 0.00 USD | `+30.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 96,320,000.00 USD | 74,770.00 USD | 0.00 USD | `+31.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 96,430,000.00 USD | 111,790.00 USD | 0.00 USD | `+31.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 96,580,000.00 USD | 147,920.00 USD | 0.00 USD | `+31.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 96,760,000.00 USD | 177,120.00 USD | 0.00 USD | `+32.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 98,670,000.00 USD | 1,910,000.00 USD | 0.00 USD | `+32.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 100,610,000.00 USD | 1,930,000.00 USD | 0.00 USD | `+33.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 100,610,000.00 USD | 6,950.00 USD | 0.00 USD | `+33.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 100,650,000.00 USD | 37,610.00 USD | 0.00 USD | `+34.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 100,720,000.00 USD | 73,700.00 USD | 0.00 USD | `+34.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 100,750,000.00 USD | 22,460.00 USD | 0.00 USD | `+34.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 101,530,000.00 USD | 783,940.00 USD | 0.00 USD | `+35.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 101,530,000.00 USD | 3,080.00 USD | 0.00 USD | `+35.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 101,580,000.00 USD | 49,330.00 USD | 0.00 USD | `+36.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 101,600,000.00 USD | 19,570.00 USD | 0.00 USD | `+36.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 101,600,000.00 USD | 928.50 USD | 0.00 USD | `+37.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 116,350,000.00 USD | 14,750,000.00 USD | 0.00 USD | `+37.65%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 116,490,000.00 USD | 135,050.00 USD | 0.00 USD | `+38.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 116,900,000.00 USD | 414,660.00 USD | 0.00 USD | `+38.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 116,910,000.00 USD | 2,530.00 USD | 0.00 USD | `+39.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 116,980,000.00 USD | 68,940.00 USD | 0.00 USD | `+39.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 117,000,000.00 USD | 21,490.00 USD | 0.00 USD | `+40.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 117,010,000.00 USD | 17,040.00 USD | 0.00 USD | `+40.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 117,010,000.00 USD | 1,330.00 USD | 0.00 USD | `+41.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 117,040,000.00 USD | 29,450.00 USD | 0.00 USD | `+41.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 117,810,000.00 USD | 766,520.00 USD | 0.00 USD | `+42.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 117,810,000.00 USD | 1,290.00 USD | 0.00 USD | `+42.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 117,820,000.00 USD | 3,740.00 USD | 0.00 USD | `+42.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 117,850,000.00 USD | 30,790.00 USD | 0.00 USD | `+43.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 117,900,000.00 USD | 56,110.00 USD | 0.00 USD | `+43.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 118,140,000.00 USD | 236,580.00 USD | 0.00 USD | `+44.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 118,160,000.00 USD | 15,710.00 USD | 0.00 USD | `+44.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 118,160,000.00 USD | 1,630.00 USD | 0.00 USD | `+45.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 118,300,000.00 USD | 141,980.00 USD | 0.00 USD | `+45.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 118,310,000.00 USD | 15,350.00 USD | 0.00 USD | `+46.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 119,710,000.00 USD | 1,400,000.00 USD | 0.00 USD | `+46.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 120,100,000.00 USD | 385,510.00 USD | 0.00 USD | `+46.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 120,110,000.00 USD | 18,270.00 USD | 0.00 USD | `+47.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 120,130,000.00 USD | 18,080.00 USD | 0.00 USD | `+47.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 120,130,000.00 USD | 617.15 USD | 0.00 USD | `+48.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 120,140,000.00 USD | 2,520.00 USD | 0.00 USD | `+48.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 120,140,000.00 USD | 597.29 USD | 0.00 USD | `+49.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 120,160,000.00 USD | 21,260.00 USD | 0.00 USD | `+49.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 120,210,000.00 USD | 58,010.00 USD | 0.00 USD | `+50.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 120,570,000.00 USD | 355,050.00 USD | 0.00 USD | `+50.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 121,910,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+50.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 121,920,000.00 USD | 3,510.00 USD | 0.00 USD | `+51.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 121,930,000.00 USD | 16,310.00 USD | 0.00 USD | `+51.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 121,950,000.00 USD | 15,030.00 USD | 0.00 USD | `+52.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 121,970,000.00 USD | 18,600.00 USD | 0.00 USD | `+53.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 121,970,000.00 USD | 495.50 USD | 0.00 USD | `+53.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 121,970,000.00 USD | 2,980.00 USD | 0.00 USD | `+54.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 122,010,000.00 USD | 43,610.00 USD | 0.00 USD | `+54.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 122,010,000.00 USD | 158.32 USD | 0.00 USD | `+54.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 122,460,000.00 USD | 444,410.00 USD | 0.00 USD | `+55.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 122,500,000.00 USD | 43,460.00 USD | 0.00 USD | `+55.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 122,510,000.00 USD | 3,690.00 USD | 0.00 USD | `+56.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 122,520,000.00 USD | 9,810.00 USD | 0.00 USD | `+56.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3545.00` | 122,520,000.00 USD | 179.38 USD | 0.00 USD | `+57.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 122,610,000.00 USD | 90,810.00 USD | 0.00 USD | `+57.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 122,610,000.00 USD | 2,300.00 USD | 0.00 USD | `+58.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 122,610,000.00 USD | 354.92 USD | 0.00 USD | `+58.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 122,620,000.00 USD | 13,160.00 USD | 0.00 USD | `+59.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 122,730,000.00 USD | 105,860.00 USD | 0.00 USD | `+59.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 122,740,000.00 USD | 10,210.00 USD | 0.00 USD | `+60.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 122,750,000.00 USD | 7,790.00 USD | 0.00 USD | `+61.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 122,750,000.00 USD | 3,860.00 USD | 0.00 USD | `+61.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 122,760,000.00 USD | 7,740.00 USD | 0.00 USD | `+62.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 122,770,000.00 USD | 8,130.00 USD | 0.00 USD | `+62.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 122,820,000.00 USD | 55,120.00 USD | 0.00 USD | `+62.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 122,820,000.00 USD | 3,550.00 USD | 0.00 USD | `+63.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 122,830,000.00 USD | 819.92 USD | 0.00 USD | `+64.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 122,830,000.00 USD | 323.58 USD | 0.00 USD | `+64.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 122,830,000.00 USD | 1,400.00 USD | 0.00 USD | `+65.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 122,830,000.00 USD | 6,490.00 USD | 0.00 USD | `+65.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 122,830,000.00 USD | 751.00 USD | 0.00 USD | `+66.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 122,830,000.00 USD | 286.90 USD | 0.00 USD | `+67.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 122,840,000.00 USD | 1,560.00 USD | 0.00 USD | `+68.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 123,570,000.00 USD | 734,090.00 USD | 0.00 USD | `+68.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 123,590,000.00 USD | 20,930.00 USD | 0.00 USD | `+69.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 123,600,000.00 USD | 8,380.00 USD | 0.00 USD | `+69.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 123,600,000.00 USD | 711.78 USD | 0.00 USD | `+70.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 123,600,000.00 USD | 355.28 USD | 0.00 USD | `+70.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 123,610,000.00 USD | 5,170.00 USD | 0.00 USD | `+70.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 123,630,000.00 USD | 19,430.00 USD | 0.00 USD | `+72.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 123,640,000.00 USD | 12,120.00 USD | 0.00 USD | `+73.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 124,280,000.00 USD | 646,840.00 USD | 0.00 USD | `+73.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3925.00` | 124,290,000.00 USD | 3,260.00 USD | 0.00 USD | `+74.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 124,330,000.00 USD | 42,570.00 USD | 0.00 USD | `+74.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 124,390,000.00 USD | 59,170.00 USD | 0.00 USD | `+74.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 124,390,000.00 USD | 1,380.00 USD | 0.00 USD | `+75.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3965.00` | 124,390,000.00 USD | 323.54 USD | 0.00 USD | `+75.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 124,400,000.00 USD | 6,960.00 USD | 0.00 USD | `+76.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 124,410,000.00 USD | 14,610.00 USD | 0.00 USD | `+76.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 124,420,000.00 USD | 4,280.00 USD | 0.00 USD | `+77.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 127,070,000.00 USD | 2,660,000.00 USD | 0.00 USD | `+77.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 127,070,000.00 USD | 898.59 USD | 0.00 USD | `+78.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 127,080,000.00 USD | 811.00 USD | 0.00 USD | `+79.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 127,080,000.00 USD | 4,310.00 USD | 0.00 USD | `+80.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 127,080,000.00 USD | 2,800.00 USD | 0.00 USD | `+81.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 127,120,000.00 USD | 39,390.00 USD | 0.00 USD | `+81.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 127,130,000.00 USD | 5,990.00 USD | 0.00 USD | `+82.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 127,130,000.00 USD | 372.90 USD | 0.00 USD | `+82.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 127,130,000.00 USD | 395.43 USD | 0.00 USD | `+83.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 127,130,000.00 USD | 376.65 USD | 0.00 USD | `+85.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 127,170,000.00 USD | 41,200.00 USD | 0.00 USD | `+86.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 127,170,000.00 USD | 460.70 USD | 0.00 USD | `+86.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 127,170,000.00 USD | 1,270.00 USD | 0.00 USD | `+87.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 127,180,000.00 USD | 4,300.00 USD | 0.00 USD | `+88.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 127,180,000.00 USD | 437.16 USD | 0.00 USD | `+89.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 127,240,000.00 USD | 64,550.00 USD | 0.00 USD | `+89.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 127,240,000.00 USD | 1,610.00 USD | 0.00 USD | `+89.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 127,340,000.00 USD | 97,670.00 USD | 0.00 USD | `+90.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 127,340,000.00 USD | 1,070.00 USD | 0.00 USD | `+91.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 127,350,000.00 USD | 11,270.00 USD | 0.00 USD | `+92.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 127,360,000.00 USD | 3,250.00 USD | 0.00 USD | `+93.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 127,400,000.00 USD | 43,750.00 USD | 0.00 USD | `+93.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 127,460,000.00 USD | 64,570.00 USD | 0.00 USD | `+94.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 127,470,000.00 USD | 1,050.00 USD | 0.00 USD | `+94.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 127,510,000.00 USD | 44,050.00 USD | 0.00 USD | `+95.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 127,520,000.00 USD | 11,480.00 USD | 0.00 USD | `+95.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 127,520,000.00 USD | 2,510.00 USD | 0.00 USD | `+96.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 127,700,000.00 USD | 177,400.00 USD | 0.00 USD | `+96.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 127,700,000.00 USD | 641.97 USD | 0.00 USD | `+97.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4465.00` | 127,700,000.00 USD | 1,030.00 USD | 0.00 USD | `+97.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4505.00` | 128,080,000.00 USD | 376,800.00 USD | 0.00 USD | `+99.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4515.00` | 128,080,000.00 USD | 2,280.00 USD | 0.00 USD | `+100.15%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `2017.30` | 319,390,000.00 USD | 0.00 USD | 319,390,000.00 USD | 83,300.00 USD | 176,210.00 USD | 0.00 USD |
| `1D` | `2020.30` | 319,130,000.00 USD | 0.00 USD | 319,130,000.00 USD | 0.00 USD | 558,730.00 USD | 0.00 USD |
| `7D` | `2025.30` | 700,940,000.00 USD | 0.00 USD | 700,940,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `7D` | `2028.60` | 700,760,000.00 USD | 0.00 USD | 700,760,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD |
| `1D` | `2029.30` | 318,570,000.00 USD | 0.00 USD | 318,570,000.00 USD | 0.00 USD | 0.00 USD | 43,160.00 USD |
| `7D` | `2031.90` | 699,580,000.00 USD | 0.00 USD | 699,580,000.00 USD | 0.00 USD | 201,200.00 USD | 0.00 USD |
| `1D` | `2032.30` | 318,530,000.00 USD | 0.00 USD | 318,530,000.00 USD | 937,190.00 USD | 1,470,000.00 USD | 0.00 USD |
| `7D` | `2035.20` | 699,380,000.00 USD | 0.00 USD | 699,380,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD |
| `1D` | `2035.30` | 316,130,000.00 USD | 0.00 USD | 316,130,000.00 USD | 167,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2038.30` | 315,960,000.00 USD | 0.00 USD | 315,960,000.00 USD | 138,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2038.50` | 699,050,000.00 USD | 0.00 USD | 699,050,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2041.30` | 315,820,000.00 USD | 0.00 USD | 315,820,000.00 USD | 0.00 USD | 134,080.00 USD | 0.00 USD |
| `7D` | `2045.10` | 697,590,000.00 USD | 0.00 USD | 697,590,000.00 USD | 0.00 USD | 149,500.00 USD | 47,970.00 USD |
| `1D` | `2053.30` | 315,690,000.00 USD | 0.00 USD | 315,690,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD |
| `1D` | `2056.30` | 315,660,000.00 USD | 0.00 USD | 315,660,000.00 USD | 0.00 USD | 88,880.00 USD | 0.00 USD |
| `7D` | `2058.30` | 697,400,000.00 USD | 0.00 USD | 697,400,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2061.60` | 697,050,000.00 USD | 0.00 USD | 697,050,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2062.30` | 315,570,000.00 USD | 0.00 USD | 315,570,000.00 USD | 80,610.00 USD | 121,470.00 USD | 52,590.00 USD |
| `7D` | `2064.90` | 692,610,000.00 USD | 0.00 USD | 692,610,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD |
| `1D` | `2065.30` | 315,320,000.00 USD | 0.00 USD | 315,320,000.00 USD | 984,680.00 USD | 537,030.00 USD | 598,250.00 USD |
| `7D` | `2068.20` | 690,090,000.00 USD | 0.00 USD | 690,090,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD |
| `1D` | `2068.30` | 313,200,000.00 USD | 0.00 USD | 313,200,000.00 USD | 444,700.00 USD | 1,330,000.00 USD | 50,470.00 USD |
| `1D` | `2071.30` | 311,370,000.00 USD | 0.00 USD | 311,370,000.00 USD | 1,040,000.00 USD | 534,600.00 USD | 437,490.00 USD |
| `7D` | `2071.50` | 685,590,000.00 USD | 0.00 USD | 685,590,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD |
| `1D` | `2074.30` | 309,360,000.00 USD | 0.00 USD | 309,360,000.00 USD | 614,280.00 USD | 62,630.00 USD | 930,220.00 USD |
| `7D` | `2074.80` | 679,130,000.00 USD | 0.00 USD | 679,130,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD |
| `1D` | `2077.30` | 307,750,000.00 USD | 0.00 USD | 307,750,000.00 USD | 3,000,000.00 USD | 1,520,000.00 USD | 2,180,000.00 USD |
| `7D` | `2078.10` | 667,430,000.00 USD | 0.00 USD | 667,430,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD |
| `1D` | `2080.30` | 301,050,000.00 USD | 0.00 USD | 301,050,000.00 USD | 1,670,000.00 USD | 1,590,000.00 USD | 280,750.00 USD |
| `7D` | `2081.40` | 655,140,000.00 USD | 0.00 USD | 655,140,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD |
| `1D` | `2083.30` | 297,510,000.00 USD | 0.00 USD | 297,510,000.00 USD | 2,180,000.00 USD | 1,420,000.00 USD | 775,480.00 USD |
| `7D` | `2084.70` | 644,500,000.00 USD | 0.00 USD | 644,500,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD |
| `1D` | `2086.30` | 293,140,000.00 USD | 0.00 USD | 293,140,000.00 USD | 1,580,000.00 USD | 1,500,000.00 USD | 1,650,000.00 USD |
| `7D` | `2088.00` | 635,710,000.00 USD | 0.00 USD | 635,710,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD |
| `1D` | `2089.30` | 288,420,000.00 USD | 0.00 USD | 288,420,000.00 USD | 1,470,000.00 USD | 430,310.00 USD | 228,930.00 USD |
| `7D` | `2091.30` | 627,280,000.00 USD | 0.00 USD | 627,280,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD |
| `1D` | `2092.30` | 286,290,000.00 USD | 0.00 USD | 286,290,000.00 USD | 1,150,000.00 USD | 514,440.00 USD | 957,110.00 USD |
| `7D` | `2094.60` | 614,330,000.00 USD | 0.00 USD | 614,330,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD |
| `1D` | `2095.30` | 283,670,000.00 USD | 0.00 USD | 283,670,000.00 USD | 2,180,000.00 USD | 1,320,000.00 USD | 2,110,000.00 USD |
| `7D` | `2097.90` | 604,110,000.00 USD | 0.00 USD | 604,110,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD |
| `1D` | `2098.30` | 278,060,000.00 USD | 0.00 USD | 278,060,000.00 USD | 474,990.00 USD | 1,170,000.00 USD | 309,770.00 USD |
| `7D` | `2101.20` | 597,270,000.00 USD | 0.00 USD | 597,270,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD |
| `1D` | `2101.30` | 276,110,000.00 USD | 0.00 USD | 276,110,000.00 USD | 207,380.00 USD | 44,780.00 USD | 304,180.00 USD |
| `1D` | `2104.30` | 275,550,000.00 USD | 0.00 USD | 275,550,000.00 USD | 1,070,000.00 USD | 961,080.00 USD | 190,690.00 USD |
| `7D` | `2104.50` | 590,670,000.00 USD | 0.00 USD | 590,670,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD |
| `1D` | `2107.30` | 273,330,000.00 USD | 0.00 USD | 273,330,000.00 USD | 546,100.00 USD | 0.00 USD | 502,840.00 USD |
| `7D` | `2107.80` | 585,230,000.00 USD | 0.00 USD | 585,230,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD |
| `1D` | `2110.30` | 272,280,000.00 USD | 0.00 USD | 272,280,000.00 USD | 118,210.00 USD | 31,550.00 USD | 196,840.00 USD |
| `7D` | `2111.10` | 580,750,000.00 USD | 0.00 USD | 580,750,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD |
| `1D` | `2113.30` | 271,930,000.00 USD | 0.00 USD | 271,930,000.00 USD | 911,810.00 USD | 643,210.00 USD | 224,810.00 USD |
| `7D` | `2114.40` | 572,700,000.00 USD | 0.00 USD | 572,700,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD |
| `1D` | `2116.30` | 270,150,000.00 USD | 0.00 USD | 270,150,000.00 USD | 0.00 USD | 13,230.00 USD | 426,410.00 USD |
| `7D` | `2117.70` | 565,970,000.00 USD | 0.00 USD | 565,970,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD |
| `1D` | `2119.30` | 269,710,000.00 USD | 0.00 USD | 269,710,000.00 USD | 218,200.00 USD | 256,720.00 USD | 937,660.00 USD |
| `7D` | `2121.00` | 557,140,000.00 USD | 0.00 USD | 557,140,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD |
| `1D` | `2122.30` | 268,300,000.00 USD | 0.00 USD | 268,300,000.00 USD | 926,060.00 USD | 689,080.00 USD | 1,310,000.00 USD |
| `7D` | `2124.30` | 550,330,000.00 USD | 0.00 USD | 550,330,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD |
| `1D` | `2125.30` | 265,370,000.00 USD | 0.00 USD | 265,370,000.00 USD | 1,010,000.00 USD | 1,130,000.00 USD | 707,090.00 USD |
| `7D` | `2127.60` | 547,010,000.00 USD | 0.00 USD | 547,010,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD |
| `1D` | `2128.30` | 262,520,000.00 USD | 0.00 USD | 262,520,000.00 USD | 365,910.00 USD | 1,040,000.00 USD | 301,140.00 USD |
| `7D` | `2130.90` | 538,710,000.00 USD | 0.00 USD | 538,710,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD |
| `1D` | `2131.30` | 260,820,000.00 USD | 0.00 USD | 260,820,000.00 USD | 0.00 USD | 644,330.00 USD | 654,700.00 USD |
| `7D` | `2134.20` | 532,290,000.00 USD | 0.00 USD | 532,290,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD |
| `1D` | `2134.30` | 259,520,000.00 USD | 0.00 USD | 259,520,000.00 USD | 0.00 USD | 312,000.00 USD | 0.00 USD |
| `1D` | `2137.30` | 259,210,000.00 USD | 0.00 USD | 259,210,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD |
| `7D` | `2137.50` | 529,260,000.00 USD | 0.00 USD | 529,260,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD |
| `7D` | `2140.80` | 527,300,000.00 USD | 0.00 USD | 527,300,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2144.10` | 523,370,000.00 USD | 0.00 USD | 523,370,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD |
| `7D` | `2147.40` | 521,520,000.00 USD | 0.00 USD | 521,520,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD |
| `7D` | `2150.70` | 520,440,000.00 USD | 0.00 USD | 520,440,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD |
| `1D` | `2152.30` | 258,930,000.00 USD | 0.00 USD | 258,930,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD |
| `7D` | `2154.00` | 519,480,000.00 USD | 0.00 USD | 519,480,000.00 USD | 128,430.00 USD | 331,520.00 USD | 32,590.00 USD |
| `1D` | `2155.30` | 258,280,000.00 USD | 0.00 USD | 258,280,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD |
| `7D` | `2157.30` | 518,990,000.00 USD | 0.00 USD | 518,990,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD |
| `1D` | `2158.30` | 256,880,000.00 USD | 0.00 USD | 256,880,000.00 USD | 0.00 USD | 0.00 USD | 37,580.00 USD |
| `7D` | `2160.60` | 516,500,000.00 USD | 0.00 USD | 516,500,000.00 USD | 646,940.00 USD | 1,900,000.00 USD | 1,990,000.00 USD |
| `1D` | `2161.30` | 256,850,000.00 USD | 0.00 USD | 256,850,000.00 USD | 0.00 USD | 860,710.00 USD | 0.00 USD |
| `7D` | `2163.90` | 511,950,000.00 USD | 0.00 USD | 511,950,000.00 USD | 566,120.00 USD | 3,280,000.00 USD | 1,210,000.00 USD |
| `1D` | `2164.30` | 255,990,000.00 USD | 0.00 USD | 255,990,000.00 USD | 0.00 USD | 0.00 USD | 55,900.00 USD |
| `7D` | `2167.20` | 506,900,000.00 USD | 0.00 USD | 506,900,000.00 USD | 25,540.00 USD | 503,000.00 USD | 50,240.00 USD |
| `1D` | `2167.30` | 255,930,000.00 USD | 0.00 USD | 255,930,000.00 USD | 2,340,000.00 USD | 341,240.00 USD | 52,000.00 USD |
| `1D` | `2170.30` | 253,190,000.00 USD | 0.00 USD | 253,190,000.00 USD | 2,860,000.00 USD | 3,520,000.00 USD | 873,550.00 USD |
| `7D` | `2170.50` | 506,320,000.00 USD | 0.00 USD | 506,320,000.00 USD | 3,500,000.00 USD | 1,190,000.00 USD | 1,830,000.00 USD |
| `1D` | `2173.30` | 245,940,000.00 USD | 0.00 USD | 245,940,000.00 USD | 0.00 USD | 190,230.00 USD | 0.00 USD |
| `7D` | `2173.80` | 499,800,000.00 USD | 0.00 USD | 499,800,000.00 USD | 4,110,000.00 USD | 363,040.00 USD | 1,010,000.00 USD |
| `1D` | `2176.30` | 245,750,000.00 USD | 0.00 USD | 245,750,000.00 USD | 345,940.00 USD | 1,400,000.00 USD | 0.00 USD |
| `1D` | `2179.30` | 244,000,000.00 USD | 0.00 USD | 244,000,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2180.40` | 494,310,000.00 USD | 0.00 USD | 494,310,000.00 USD | 0.00 USD | 373,740.00 USD | 119,920.00 USD |
| `1D` | `2191.30` | 242,820,000.00 USD | 0.00 USD | 242,820,000.00 USD | 0.00 USD | 222,200.00 USD | 70,390.00 USD |
| `7D` | `2196.90` | 493,820,000.00 USD | 0.00 USD | 493,820,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 0.00 USD |
| `1D` | `2197.30` | 242,530,000.00 USD | 0.00 USD | 242,530,000.00 USD | 416,500.00 USD | 881,070.00 USD | 0.00 USD |
| `7D` | `2200.20` | 490,770,000.00 USD | 0.00 USD | 490,770,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD |
| `1D` | `2200.30` | 241,230,000.00 USD | 0.00 USD | 241,230,000.00 USD | 284,470.00 USD | 3,100,000.00 USD | 220,720.00 USD |
| `1D` | `2203.30` | 237,630,000.00 USD | 0.00 USD | 237,630,000.00 USD | 3,540,000.00 USD | 1,410,000.00 USD | 2,100,000.00 USD |
| `7D` | `2203.50` | 479,490,000.00 USD | 0.00 USD | 479,490,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD |
| `1D` | `2206.30` | 230,580,000.00 USD | 0.00 USD | 230,580,000.00 USD | 755,060.00 USD | 6,310,000.00 USD | 802,740.00 USD |
| `7D` | `2206.80` | 470,380,000.00 USD | 0.00 USD | 470,380,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD |
| `1D` | `2209.30` | 222,710,000.00 USD | 0.00 USD | 222,710,000.00 USD | 2,720,000.00 USD | 2,010,000.00 USD | 3,050,000.00 USD |
| `7D` | `2210.10` | 450,010,000.00 USD | 0.00 USD | 450,010,000.00 USD | 12,800,000.00 USD | 14,160,000.00 USD | 6,290,000.00 USD |
| `1D` | `2212.30` | 214,940,000.00 USD | 0.00 USD | 214,940,000.00 USD | 7,970,000.00 USD | 2,320,000.00 USD | 3,060,000.00 USD |
| `7D` | `2213.40` | 416,750,000.00 USD | 0.00 USD | 416,750,000.00 USD | 10,920,000.00 USD | 11,890,000.00 USD | 13,170,000.00 USD |
| `1D` | `2215.30` | 201,600,000.00 USD | 0.00 USD | 201,600,000.00 USD | 13,360,000.00 USD | 12,530,000.00 USD | 7,240,000.00 USD |
| `7D` | `2216.70` | 380,770,000.00 USD | 0.00 USD | 380,770,000.00 USD | 25,210,000.00 USD | 14,660,000.00 USD | 9,390,000.00 USD |
| `1D` | `2218.30` | 168,460,000.00 USD | 0.00 USD | 168,460,000.00 USD | 7,390,000.00 USD | 7,700,000.00 USD | 2,280,000.00 USD |
| `7D` | `2220.00` | 331,510,000.00 USD | 0.00 USD | 331,510,000.00 USD | 24,310,000.00 USD | 12,300,000.00 USD | 10,120,000.00 USD |
| `1D` | `2221.30` | 151,100,000.00 USD | 0.00 USD | 151,100,000.00 USD | 6,130,000.00 USD | 12,360,000.00 USD | 1,260,000.00 USD |
| `7D` | `2223.30` | 284,780,000.00 USD | 0.00 USD | 284,780,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD |
| `1D` | `2224.30` | 131,350,000.00 USD | 0.00 USD | 131,350,000.00 USD | 9,430,000.00 USD | 5,550,000.00 USD | 5,550,000.00 USD |
| `7D` | `2226.60` | 254,500,000.00 USD | 0.00 USD | 254,500,000.00 USD | 12,840,000.00 USD | 11,030,000.00 USD | 9,840,000.00 USD |
| `1D` | `2227.30` | 110,820,000.00 USD | 0.00 USD | 110,820,000.00 USD | 5,860,000.00 USD | 3,900,000.00 USD | 2,610,000.00 USD |
| `7D` | `2229.90` | 220,790,000.00 USD | 0.00 USD | 220,790,000.00 USD | 12,730,000.00 USD | 9,180,000.00 USD | 20,660,000.00 USD |
| `1D` | `2230.30` | 98,450,000.00 USD | 0.00 USD | 98,450,000.00 USD | 4,210,000.00 USD | 5,550,000.00 USD | 2,320,000.00 USD |
| `7D` | `2233.20` | 178,220,000.00 USD | 0.00 USD | 178,220,000.00 USD | 15,490,000.00 USD | 11,810,000.00 USD | 9,960,000.00 USD |
| `1D` | `2233.30` | 86,380,000.00 USD | 0.00 USD | 86,380,000.00 USD | 6,390,000.00 USD | 2,520,000.00 USD | 5,380,000.00 USD |
| `1D` | `2236.30` | 72,080,000.00 USD | 0.00 USD | 72,080,000.00 USD | 18,610,000.00 USD | 0.00 USD | 4,380,000.00 USD |
| `7D` | `2236.50` | 140,960,000.00 USD | 0.00 USD | 140,960,000.00 USD | 10,580,000.00 USD | 2,010,000.00 USD | 5,830,000.00 USD |
| `1D` | `2239.30` | 49,090,000.00 USD | 0.00 USD | 49,090,000.00 USD | 6,170,000.00 USD | 783,290.00 USD | 4,340,000.00 USD |
| `7D` | `2239.80` | 122,540,000.00 USD | 0.00 USD | 122,540,000.00 USD | 15,710,000.00 USD | 1,860,000.00 USD | 13,750,000.00 USD |
| `1D` | `2242.30` | 37,800,000.00 USD | 0.00 USD | 37,800,000.00 USD | 2,420,000.00 USD | 760,920.00 USD | 1,460,000.00 USD |
| `7D` | `2243.10` | 91,230,000.00 USD | 0.00 USD | 91,230,000.00 USD | 22,920,000.00 USD | 0.00 USD | 8,970,000.00 USD |
| `1D` | `2245.30` | 33,160,000.00 USD | 0.00 USD | 33,160,000.00 USD | 2,360,000.00 USD | 4,260,000.00 USD | 482,700.00 USD |
| `7D` | `2246.40` | 59,340,000.00 USD | 0.00 USD | 59,340,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD |
| `1D` | `2248.30` | 26,060,000.00 USD | 0.00 USD | 26,060,000.00 USD | 8,900,000.00 USD | 0.00 USD | 4,100,000.00 USD |
| `7D` | `2249.70` | 31,080,000.00 USD | 0.00 USD | 31,080,000.00 USD | 18,000,000.00 USD | 0.00 USD | 13,070,000.00 USD |
| `1D` | `2251.30` | 13,060,000.00 USD | 0.00 USD | 13,060,000.00 USD | 4,190,000.00 USD | 506,110.00 USD | 2,950,000.00 USD |
| `7D` | `2252.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2253.00` | 44,620,000.00 USD | 44,620,000.00 USD | 0.00 USD | 26,890,000.00 USD | 0.00 USD | 17,730,000.00 USD |
| `1D` | `2254.30` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 5,410,000.00 USD |
| `7D` | `2256.30` | 63,150,000.00 USD | 63,150,000.00 USD | 0.00 USD | 15,220,000.00 USD | 0.00 USD | 3,310,000.00 USD |
| `1D` | `2260.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2266.30` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,860,000.00 USD |
| `1D` | `2269.30` | 12,840,000.00 USD | 12,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,980,000.00 USD |
| `7D` | `2269.50` | 67,510,000.00 USD | 67,510,000.00 USD | 0.00 USD | 0.00 USD | 4,370,000.00 USD | 0.00 USD |
| `1D` | `2272.30` | 33,060,000.00 USD | 33,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,220,000.00 USD |
| `7D` | `2272.80` | 98,780,000.00 USD | 98,780,000.00 USD | 0.00 USD | 0.00 USD | 31,270,000.00 USD | 0.00 USD |
| `1D` | `2275.30` | 59,740,000.00 USD | 59,740,000.00 USD | 0.00 USD | 1,020,000.00 USD | 21,680,000.00 USD | 3,980,000.00 USD |
| `7D` | `2276.10` | 156,280,000.00 USD | 156,280,000.00 USD | 0.00 USD | 3,340,000.00 USD | 54,160,000.00 USD | 0.00 USD |
| `1D` | `2278.30` | 99,940,000.00 USD | 99,940,000.00 USD | 0.00 USD | 5,630,000.00 USD | 15,600,000.00 USD | 18,970,000.00 USD |
| `7D` | `2279.40` | 326,780,000.00 USD | 326,780,000.00 USD | 0.00 USD | 77,990,000.00 USD | 55,080,000.00 USD | 37,430,000.00 USD |
| `1D` | `2281.30` | 189,030,000.00 USD | 189,030,000.00 USD | 0.00 USD | 41,300,000.00 USD | 26,130,000.00 USD | 21,660,000.00 USD |
| `7D` | `2282.70` | 549,710,000.00 USD | 549,710,000.00 USD | 0.00 USD | 78,190,000.00 USD | 76,930,000.00 USD | 67,810,000.00 USD |
| `1D` | `2284.30` | 249,990,000.00 USD | 249,990,000.00 USD | 0.00 USD | 29,150,000.00 USD | 16,670,000.00 USD | 15,140,000.00 USD |
| `7D` | `2286.00` | 690,170,000.00 USD | 690,170,000.00 USD | 0.00 USD | 89,380,000.00 USD | 9,400,000.00 USD | 41,680,000.00 USD |
| `1D` | `2287.30` | 252,550,000.00 USD | 252,550,000.00 USD | 0.00 USD | 1,800,000.00 USD | 760,920.00 USD | 0.00 USD |
| `7D` | `2289.30` | 778,460,000.00 USD | 778,460,000.00 USD | 0.00 USD | 84,260,000.00 USD | 0.00 USD | 4,030,000.00 USD |
| `1D` | `2290.30` | 260,950,000.00 USD | 260,950,000.00 USD | 0.00 USD | 0.00 USD | 8,390,000.00 USD | 0.00 USD |
| `7D` | `2292.60` | 811,940,000.00 USD | 811,940,000.00 USD | 0.00 USD | 33,480,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2293.30` | 265,740,000.00 USD | 265,740,000.00 USD | 0.00 USD | 4,720,000.00 USD | 0.00 USD | 75,150.00 USD |
| `7D` | `2295.90` | 839,920,000.00 USD | 839,920,000.00 USD | 0.00 USD | 25,120,000.00 USD | 2,380,000.00 USD | 479,670.00 USD |
| `1D` | `2296.30` | 267,460,000.00 USD | 267,460,000.00 USD | 0.00 USD | 0.00 USD | 1,720,000.00 USD | 0.00 USD |
| `7D` | `2299.20` | 855,330,000.00 USD | 855,330,000.00 USD | 0.00 USD | 9,500,000.00 USD | 5,900,000.00 USD | 0.00 USD |
| `1D` | `2299.30` | 267,470,000.00 USD | 267,470,000.00 USD | 0.00 USD | 0.00 USD | 10,910.00 USD | 0.00 USD |
| `1D` | `2302.30` | 278,000,000.00 USD | 278,000,000.00 USD | 0.00 USD | 9,550,000.00 USD | 682,490.00 USD | 298,370.00 USD |
| `7D` | `2302.50` | 868,480,000.00 USD | 868,480,000.00 USD | 0.00 USD | 12,090,000.00 USD | 1,010,000.00 USD | 63,260.00 USD |
| `1D` | `2305.30` | 301,160,000.00 USD | 301,160,000.00 USD | 0.00 USD | 9,200,000.00 USD | 11,910,000.00 USD | 2,040,000.00 USD |
| `7D` | `2305.80` | 877,400,000.00 USD | 877,400,000.00 USD | 0.00 USD | 2,980,000.00 USD | 3,740,000.00 USD | 2,200,000.00 USD |
| `1D` | `2308.30` | 303,910,000.00 USD | 303,910,000.00 USD | 0.00 USD | 0.00 USD | 2,750,000.00 USD | 0.00 USD |
| `7D` | `2309.10` | 881,170,000.00 USD | 881,170,000.00 USD | 0.00 USD | 732,090.00 USD | 930,630.00 USD | 2,110,000.00 USD |
| `1D` | `2311.30` | 304,600,000.00 USD | 304,600,000.00 USD | 0.00 USD | 691,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2312.40` | 888,520,000.00 USD | 888,520,000.00 USD | 0.00 USD | 7,270,000.00 USD | 0.00 USD | 70,770.00 USD |
| `1D` | `2314.30` | 316,060,000.00 USD | 316,060,000.00 USD | 0.00 USD | 0.00 USD | 11,260,000.00 USD | 203,330.00 USD |
| `7D` | `2315.70` | 896,090,000.00 USD | 896,090,000.00 USD | 0.00 USD | 0.00 USD | 7,460,000.00 USD | 117,510.00 USD |
| `1D` | `2317.30` | 342,990,000.00 USD | 342,990,000.00 USD | 0.00 USD | 8,430,000.00 USD | 13,390,000.00 USD | 5,100,000.00 USD |
| `7D` | `2319.00` | 902,080,000.00 USD | 902,080,000.00 USD | 0.00 USD | 1,020,000.00 USD | 4,550,000.00 USD | 411,830.00 USD |
| `1D` | `2320.30` | 355,360,000.00 USD | 355,360,000.00 USD | 0.00 USD | 3,870,000.00 USD | 8,340,000.00 USD | 147,610.00 USD |
| `7D` | `2322.30` | 915,400,000.00 USD | 915,400,000.00 USD | 0.00 USD | 0.00 USD | 13,320,000.00 USD | 0.00 USD |
| `1D` | `2323.30` | 363,440,000.00 USD | 363,440,000.00 USD | 0.00 USD | 572,970.00 USD | 7,510,000.00 USD | 0.00 USD |
| `7D` | `2325.60` | 922,190,000.00 USD | 922,190,000.00 USD | 0.00 USD | 4,250,000.00 USD | 2,540,000.00 USD | 0.00 USD |
| `1D` | `2326.30` | 373,740,000.00 USD | 373,740,000.00 USD | 0.00 USD | 479,120.00 USD | 5,550,000.00 USD | 4,270,000.00 USD |
| `7D` | `2328.90` | 934,020,000.00 USD | 934,020,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD |
| `1D` | `2329.30` | 383,760,000.00 USD | 383,760,000.00 USD | 0.00 USD | 8,790,000.00 USD | 884,940.00 USD | 344,170.00 USD |
| `7D` | `2332.20` | 963,250,000.00 USD | 963,250,000.00 USD | 0.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2332.30` | 395,720,000.00 USD | 395,720,000.00 USD | 0.00 USD | 11,600,000.00 USD | 251,940.00 USD | 107,090.00 USD |
| `1D` | `2335.30` | 419,640,000.00 USD | 419,640,000.00 USD | 0.00 USD | 17,430,000.00 USD | 3,070,000.00 USD | 3,420,000.00 USD |
| `7D` | `2335.50` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 6,520,000.00 USD |
| `1D` | `2338.30` | 432,540,000.00 USD | 432,540,000.00 USD | 0.00 USD | 6,030,000.00 USD | 688,030.00 USD | 6,180,000.00 USD |
| `7D` | `2338.80` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 0.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD |
| `1D` | `2341.30` | 455,400,000.00 USD | 455,400,000.00 USD | 0.00 USD | 9,780,000.00 USD | 3,290,000.00 USD | 9,800,000.00 USD |
| `7D` | `2342.10` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD |
| `1D` | `2344.30` | 468,660,000.00 USD | 468,660,000.00 USD | 0.00 USD | 1,370,000.00 USD | 6,180,000.00 USD | 5,710,000.00 USD |
| `7D` | `2345.40` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 1,350,000.00 USD | 10,870,000.00 USD | 5,940,000.00 USD |
| `1D` | `2347.30` | 480,500,000.00 USD | 480,500,000.00 USD | 0.00 USD | 3,220,000.00 USD | 3,010,000.00 USD | 5,600,000.00 USD |
| `7D` | `2348.70` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 847,620.00 USD | 8,140,000.00 USD | 24,140,000.00 USD |
| `1D` | `2350.30` | 526,570,000.00 USD | 526,570,000.00 USD | 0.00 USD | 30,920,000.00 USD | 6,290,000.00 USD | 8,860,000.00 USD |
| `7D` | `2352.00` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 2,930,000.00 USD | 21,880,000.00 USD | 10,630,000.00 USD |
| `1D` | `2353.30` | 535,760,000.00 USD | 535,760,000.00 USD | 0.00 USD | 4,170,000.00 USD | 3,800,000.00 USD | 1,220,000.00 USD |
| `7D` | `2355.30` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 16,520,000.00 USD | 36,690,000.00 USD | 1,380,000.00 USD |
| `1D` | `2356.30` | 558,510,000.00 USD | 558,510,000.00 USD | 0.00 USD | 3,710,000.00 USD | 16,640,000.00 USD | 2,390,000.00 USD |
| `7D` | `2358.60` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 7,110,000.00 USD | 512,220.00 USD | 3,190,000.00 USD |
| `1D` | `2359.30` | 576,550,000.00 USD | 576,550,000.00 USD | 0.00 USD | 4,140,000.00 USD | 6,970,000.00 USD | 6,920,000.00 USD |
| `7D` | `2361.90` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 119,920.00 USD |
| `1D` | `2362.30` | 595,190,000.00 USD | 595,190,000.00 USD | 0.00 USD | 10,460,000.00 USD | 6,710,000.00 USD | 1,470,000.00 USD |
| `7D` | `2365.20` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 8,440,000.00 USD | 0.00 USD | 6,920,000.00 USD |
| `1D` | `2365.30` | 610,310,000.00 USD | 610,310,000.00 USD | 0.00 USD | 3,460,000.00 USD | 3,710,000.00 USD | 7,940,000.00 USD |
| `1D` | `2368.30` | 622,320,000.00 USD | 622,320,000.00 USD | 0.00 USD | 7,910,000.00 USD | 2,500,000.00 USD | 1,610,000.00 USD |
| `7D` | `2368.50` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 10,270,000.00 USD | 475,460.00 USD | 404,380.00 USD |
| `1D` | `2371.30` | 662,960,000.00 USD | 662,960,000.00 USD | 0.00 USD | 18,140,000.00 USD | 13,710,000.00 USD | 8,790,000.00 USD |
| `7D` | `2371.80` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 23,260,000.00 USD | 0.00 USD | 50,750,000.00 USD |
| `1D` | `2374.30` | 685,400,000.00 USD | 685,400,000.00 USD | 0.00 USD | 14,690,000.00 USD | 1,320,000.00 USD | 6,430,000.00 USD |
| `7D` | `2375.10` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD |
| `1D` | `2377.30` | 708,550,000.00 USD | 708,550,000.00 USD | 0.00 USD | 6,500,000.00 USD | 8,030,000.00 USD | 8,620,000.00 USD |
| `7D` | `2378.40` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD |
| `1D` | `2380.30` | 750,520,000.00 USD | 750,520,000.00 USD | 0.00 USD | 14,000,000.00 USD | 11,640,000.00 USD | 16,340,000.00 USD |
| `7D` | `2381.70` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 22,490,000.00 USD |
| `1D` | `2383.30` | 811,140,000.00 USD | 811,140,000.00 USD | 0.00 USD | 24,350,000.00 USD | 17,830,000.00 USD | 18,440,000.00 USD |
| `7D` | `2385.00` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD |
| `1D` | `2386.30` | 853,280,000.00 USD | 853,280,000.00 USD | 0.00 USD | 14,350,000.00 USD | 16,360,000.00 USD | 11,430,000.00 USD |
| `7D` | `2388.30` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD |
| `1D` | `2389.30` | 882,180,000.00 USD | 882,180,000.00 USD | 0.00 USD | 13,790,000.00 USD | 7,220,000.00 USD | 7,880,000.00 USD |
| `7D` | `2391.60` | 1,740,000,000.00 USD | 1,740,000,000.00 USD | 0.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD |
| `1D` | `2392.30` | 904,860,000.00 USD | 904,860,000.00 USD | 0.00 USD | 3,240,000.00 USD | 12,680,000.00 USD | 6,770,000.00 USD |
| `7D` | `2394.90` | 1,860,000,000.00 USD | 1,860,000,000.00 USD | 0.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD |
| `1D` | `2395.30` | 927,470,000.00 USD | 927,470,000.00 USD | 0.00 USD | 8,480,000.00 USD | 10,370,000.00 USD | 3,760,000.00 USD |
| `7D` | `2398.20` | 1,970,000,000.00 USD | 1,970,000,000.00 USD | 0.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD |
| `1D` | `2398.30` | 947,680,000.00 USD | 947,680,000.00 USD | 0.00 USD | 5,950,000.00 USD | 6,860,000.00 USD | 7,410,000.00 USD |
| `1D` | `2401.30` | 973,220,000.00 USD | 973,220,000.00 USD | 0.00 USD | 8,760,000.00 USD | 7,400,000.00 USD | 9,390,000.00 USD |
| `7D` | `2401.50` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 0.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD |
| `1D` | `2404.30` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 10,010,000.00 USD | 11,420,000.00 USD | 8,840,000.00 USD |
| `7D` | `2404.80` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD |
| `1D` | `2407.30` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 0.00 USD | 16,500,000.00 USD | 9,310,000.00 USD | 9,360,000.00 USD |
| `7D` | `2408.10` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD |
| `1D` | `2410.30` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 9,560,000.00 USD | 9,260,000.00 USD | 9,620,000.00 USD |
| `7D` | `2411.40` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD |
| `1D` | `2413.30` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 8,610,000.00 USD | 5,530,000.00 USD | 3,130,000.00 USD |
| `7D` | `2414.70` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 0.00 USD | 24,010,000.00 USD | 21,950,000.00 USD | 23,130,000.00 USD |
| `1D` | `2416.30` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 5,470,000.00 USD | 7,950,000.00 USD | 4,410,000.00 USD |
| `7D` | `2418.00` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 0.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,610,000.00 USD |
| `1D` | `2419.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 5,120,000.00 USD | 3,350,000.00 USD | 3,480,000.00 USD |
| `7D` | `2421.30` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 0.00 USD | 25,700,000.00 USD | 27,890,000.00 USD | 21,590,000.00 USD |
| `1D` | `2422.30` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 4,560,000.00 USD | 5,190,000.00 USD | 6,060,000.00 USD |
| `7D` | `2424.60` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 24,180,000.00 USD | 35,050,000.00 USD | 34,520,000.00 USD |
| `1D` | `2425.30` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 1,810,000.00 USD | 2,670,000.00 USD | 844,590.00 USD |
| `7D` | `2427.90` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 25,390,000.00 USD | 18,380,000.00 USD | 26,460,000.00 USD |
| `1D` | `2428.30` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 466,170.00 USD | 542,280.00 USD | 1,500,000.00 USD |
| `7D` | `2431.20` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 10,580,000.00 USD | 18,750,000.00 USD | 9,300,000.00 USD |
| `1D` | `2431.30` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 2,890,000.00 USD | 2,960,000.00 USD | 347,720.00 USD |
| `1D` | `2434.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 1,930,000.00 USD | 510,300.00 USD | 1,580,000.00 USD |
| `7D` | `2434.50` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,240,000.00 USD |
| `1D` | `2437.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 1,250,000.00 USD | 531,390.00 USD | 205,600.00 USD |
| `7D` | `2437.80` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 12,000,000.00 USD | 12,820,000.00 USD | 5,470,000.00 USD |
| `1D` | `2440.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 1,540,000.00 USD | 1,250,000.00 USD | 479,040.00 USD |
| `7D` | `2441.10` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,680,000.00 USD |
| `1D` | `2443.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 1,850,000.00 USD | 2,060,000.00 USD |
| `7D` | `2444.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 8,860,000.00 USD | 15,160,000.00 USD | 14,000,000.00 USD |
| `1D` | `2446.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 648,280.00 USD | 347,060.00 USD | 404,470.00 USD |
| `7D` | `2447.70` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 0.00 USD | 11,650,000.00 USD | 8,510,000.00 USD | 17,330,000.00 USD |
| `1D` | `2449.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 408,380.00 USD | 744,230.00 USD | 2,770,000.00 USD |
| `7D` | `2451.00` | 3,030,000,000.00 USD | 3,030,000,000.00 USD | 0.00 USD | 16,710,000.00 USD | 14,100,000.00 USD | 16,480,000.00 USD |
| `1D` | `2452.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 3,750,000.00 USD | 2,930,000.00 USD | 4,440,000.00 USD |
| `7D` | `2454.30` | 3,040,000,000.00 USD | 3,040,000,000.00 USD | 0.00 USD | 4,710,000.00 USD | 5,780,000.00 USD | 3,880,000.00 USD |
| `1D` | `2455.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 4,330,000.00 USD | 3,510,000.00 USD | 2,620,000.00 USD |
| `7D` | `2457.60` | 3,080,000,000.00 USD | 3,080,000,000.00 USD | 0.00 USD | 15,240,000.00 USD | 12,540,000.00 USD | 12,640,000.00 USD |
| `1D` | `2458.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 2,260,000.00 USD | 1,790,000.00 USD | 1,230,000.00 USD |
| `7D` | `2460.90` | 3,100,000,000.00 USD | 3,100,000,000.00 USD | 0.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD |
| `1D` | `2461.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 1,260,000.00 USD | 1,180,000.00 USD | 1,170,000.00 USD |
| `7D` | `2464.20` | 3,120,000,000.00 USD | 3,120,000,000.00 USD | 0.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD |
| `1D` | `2464.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 352,200.00 USD | 2,960,000.00 USD | 829,050.00 USD |
| `1D` | `2467.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 83,300.00 USD | 68,070.00 USD | 0.00 USD |
| `7D` | `2467.50` | 3,130,000,000.00 USD | 3,130,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD |
| `1D` | `2470.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 1,190,000.00 USD | 391,890.00 USD |
| `7D` | `2470.80` | 3,140,000,000.00 USD | 3,140,000,000.00 USD | 0.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD |
| `7D` | `2474.10` | 3,150,000,000.00 USD | 3,150,000,000.00 USD | 0.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD |
| `7D` | `2477.40` | 3,160,000,000.00 USD | 3,160,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD |
| `7D` | `2480.70` | 3,160,000,000.00 USD | 3,160,000,000.00 USD | 0.00 USD | 2,110,000.00 USD | 2,920,000.00 USD | 505,810.00 USD |
| `1D` | `2482.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 239,600.00 USD | 136,500.00 USD | 43,160.00 USD |
| `7D` | `2484.00` | 3,160,000,000.00 USD | 3,160,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 77,610.00 USD |
| `1D` | `2485.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 865,140.00 USD | 1,330,000.00 USD | 0.00 USD |
| `7D` | `2487.30` | 3,160,000,000.00 USD | 3,160,000,000.00 USD | 0.00 USD | 325,140.00 USD | 262,280.00 USD | 0.00 USD |
| `7D` | `2490.60` | 3,170,000,000.00 USD | 3,170,000,000.00 USD | 0.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 279,750.00 USD |
| `1D` | `2491.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 138,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2493.90` | 3,180,000,000.00 USD | 3,180,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 1,790,000.00 USD | 3,940,000.00 USD |
| `1D` | `2494.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 134,080.00 USD | 0.00 USD |
| `7D` | `2497.20` | 3,190,000,000.00 USD | 3,190,000,000.00 USD | 0.00 USD | 2,940,000.00 USD | 5,270,000.00 USD | 8,250,000.00 USD |
| `7D` | `2500.50` | 3,200,000,000.00 USD | 3,200,000,000.00 USD | 0.00 USD | 1,160,000.00 USD | 2,280,000.00 USD | 1,130,000.00 USD |
| `7D` | `2503.80` | 3,200,000,000.00 USD | 3,200,000,000.00 USD | 0.00 USD | 111,800.00 USD | 1,900,000.00 USD | 125,600.00 USD |
| `7D` | `2507.10` | 3,210,000,000.00 USD | 3,210,000,000.00 USD | 0.00 USD | 4,110,000.00 USD | 3,090,000.00 USD | 2,000,000.00 USD |
| `1D` | `2509.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD |
| `7D` | `2510.40` | 3,210,000,000.00 USD | 3,210,000,000.00 USD | 0.00 USD | 1,200,000.00 USD | 1,270,000.00 USD | 0.00 USD |
| `1D` | `2512.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 88,880.00 USD | 0.00 USD |
| `7D` | `2513.70` | 3,210,000,000.00 USD | 3,210,000,000.00 USD | 0.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2517.00` | 3,210,000,000.00 USD | 3,210,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2520.30` | 3,220,000,000.00 USD | 3,220,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2521.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 80,610.00 USD | 121,470.00 USD | 110,470.00 USD |
| `7D` | `2523.60` | 3,220,000,000.00 USD | 3,220,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `1D` | `2524.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 984,680.00 USD | 537,030.00 USD | 540,380.00 USD |
| `7D` | `2526.90` | 3,220,000,000.00 USD | 3,220,000,000.00 USD | 0.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD |
| `1D` | `2527.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 387,410.00 USD | 362,000.00 USD | 50,470.00 USD |
| `7D` | `2530.20` | 3,230,000,000.00 USD | 3,230,000,000.00 USD | 0.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `1D` | `2530.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 965,400.00 USD | 437,490.00 USD |
| `1D` | `2533.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 407,340.00 USD | 555,250.00 USD | 436,900.00 USD |
| `7D` | `2533.50` | 3,240,000,000.00 USD | 3,240,000,000.00 USD | 0.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD |
| `1D` | `2536.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 1,260,000.00 USD | 698,510.00 USD | 1,080,000.00 USD |
| `7D` | `2536.80` | 3,250,000,000.00 USD | 3,250,000,000.00 USD | 0.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD |
| `1D` | `2539.30` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,090,000.00 USD | 1,660,000.00 USD |
| `7D` | `2540.10` | 3,260,000,000.00 USD | 3,260,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD |
| `1D` | `2542.30` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,350,000.00 USD | 218,810.00 USD |
| `7D` | `2543.40` | 3,260,000,000.00 USD | 3,260,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD |
| `1D` | `2545.30` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 1,030,000.00 USD | 336,450.00 USD | 212,140.00 USD |
| `7D` | `2546.70` | 3,270,000,000.00 USD | 3,270,000,000.00 USD | 0.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD |
| `1D` | `2548.30` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 2,050,000.00 USD | 1,680,000.00 USD | 1,720,000.00 USD |
| `7D` | `2550.00` | 3,280,000,000.00 USD | 3,280,000,000.00 USD | 0.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD |
| `1D` | `2551.30` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 1,120,000.00 USD | 698,070.00 USD |
| `7D` | `2553.30` | 3,290,000,000.00 USD | 3,290,000,000.00 USD | 0.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD |
| `1D` | `2554.30` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 1,100,000.00 USD | 228,660.00 USD | 236,190.00 USD |
| `7D` | `2556.60` | 3,300,000,000.00 USD | 3,300,000,000.00 USD | 0.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD |
| `1D` | `2557.30` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 717,260.00 USD | 506,330.00 USD | 740,260.00 USD |
| `7D` | `2559.90` | 3,310,000,000.00 USD | 3,310,000,000.00 USD | 0.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD |
| `1D` | `2560.30` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 2,020,000.00 USD | 1,140,000.00 USD | 1,430,000.00 USD |
| `7D` | `2563.20` | 3,310,000,000.00 USD | 3,310,000,000.00 USD | 0.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD |
| `1D` | `2563.30` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 617,040.00 USD | 998,570.00 USD | 984,190.00 USD |
| `1D` | `2566.30` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 172,210.00 USD | 403,100.00 USD | 11,930.00 USD |
| `7D` | `2566.50` | 3,320,000,000.00 USD | 3,320,000,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD |
| `1D` | `2569.30` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 327,300.00 USD | 119,690.00 USD | 466,670.00 USD |
| `7D` | `2569.80` | 3,320,000,000.00 USD | 3,320,000,000.00 USD | 0.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD |
| `1D` | `2572.30` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 792,480.00 USD | 841,400.00 USD | 16,280.00 USD |
| `7D` | `2573.10` | 3,320,000,000.00 USD | 3,320,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD |
| `1D` | `2575.30` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 546,100.00 USD | 0.00 USD | 502,840.00 USD |
| `7D` | `2576.40` | 3,330,000,000.00 USD | 3,330,000,000.00 USD | 0.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD |
| `1D` | `2578.30` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 118,210.00 USD | 31,550.00 USD | 8,540.00 USD |
| `7D` | `2579.70` | 3,340,000,000.00 USD | 3,340,000,000.00 USD | 0.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD |
| `1D` | `2581.30` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 450,470.00 USD | 405,480.00 USD | 409,780.00 USD |
| `7D` | `2583.00` | 3,340,000,000.00 USD | 3,340,000,000.00 USD | 0.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD |
| `1D` | `2583.80` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 411,740.00 USD | 226,990.00 USD | 0.00 USD |
| `7D` | `2586.30` | 3,350,000,000.00 USD | 3,350,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD |
| `7D` | `2589.60` | 3,350,000,000.00 USD | 3,350,000,000.00 USD | 0.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD |
| `7D` | `2592.90` | 3,360,000,000.00 USD | 3,360,000,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD |
| `7D` | `2596.20` | 3,360,000,000.00 USD | 3,360,000,000.00 USD | 0.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD |
| `7D` | `2599.50` | 3,370,000,000.00 USD | 3,370,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD |
| `7D` | `2602.80` | 3,370,000,000.00 USD | 3,370,000,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD |
| `7D` | `2606.10` | 3,380,000,000.00 USD | 3,380,000,000.00 USD | 0.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD |
| `7D` | `2609.40` | 3,380,000,000.00 USD | 3,380,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD |
| `7D` | `2612.70` | 3,380,000,000.00 USD | 3,380,000,000.00 USD | 0.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD |
| `7D` | `2616.00` | 3,390,000,000.00 USD | 3,390,000,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2619.30` | 3,390,000,000.00 USD | 3,390,000,000.00 USD | 0.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD |
| `7D` | `2622.60` | 3,390,000,000.00 USD | 3,390,000,000.00 USD | 0.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD |
| `7D` | `2625.90` | 3,390,000,000.00 USD | 3,390,000,000.00 USD | 0.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD |
| `7D` | `2629.20` | 3,390,000,000.00 USD | 3,390,000,000.00 USD | 0.00 USD | 0.00 USD | 20,460.00 USD | 31,040.00 USD |
| `7D` | `2632.40` | 3,390,000,000.00 USD | 3,390,000,000.00 USD | 0.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `28.80B` | Total OI Tokens: `12,743,873.1 ETH`
  * 1h OI Change: `-3.27%` | 4h OI Change: `-5.08%` | 24h OI Change: `-3.65%`
  * Exchange Breakdown: Binance=`8.54B` | Bybit=`2.05B` | OKX=`1.73B` | Hyperliquid=`2.43B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `591.27K` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0052%` | **USDT OKX** | `0.0099%` |
| **USDT Bybit** | `0.0027%` | **USDT KuCoin** | `0.0041%` |
| **USDT MEXC** | `0.0053%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0088%` | **USDT Bitget** | `0.0061%` |
| **CoinM Binance** | `0.0066%` | **CoinM OKX** | `0.0064%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `44.21%` | `55.79%` | `0.79` | 8,510,000,000.00 USD |
| `15M` | `Binance` | `44.08%` | `55.92%` | `0.79` | 2,720,000,000.00 USD |
| `15M` | `OKX` | `45.03%` | `54.97%` | `0.82` | 1,110,000,000.00 USD |
| `15M` | `Bybit` | `43.38%` | `56.62%` | `0.77` | 1,050,000,000.00 USD |
| `15M` | `KuCoin` | `56.53%` | `43.47%` | `1.30` | 57,410,000.00 USD |
| `15M` | `Gate` | `47.33%` | `52.67%` | `0.90` | 210,130,000.00 USD |
| `15M` | `Bitget` | `53.24%` | `46.76%` | `1.14` | 361,300,000.00 USD |
| `15M` | `BingX` | `45.57%` | `54.43%` | `0.84` | 131,940,000.00 USD |
| `15M` | `MEXC` | `45.57%` | `54.43%` | `0.84` | 409,410,000.00 USD |
| `15M` | `Bitunix` | `45.38%` | `54.62%` | `0.83` | 379,130,000.00 USD |
| `15M` | `Hyperliquid` | `48.29%` | `51.71%` | `0.93` | 571,150,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.24%` | `48.76%` | `1.05` | 53,530,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 40,800,000.00 USD |
| `15M` | `WhiteBIT` | `39.39%` | `60.61%` | `0.65` | 1,000,000,000.00 USD |
| `15M` | `HTX` | `42.58%` | `57.42%` | `0.74` | 32,340,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `45.99%` | `54.01%` | `0.85` | 145,870,000.00 USD |
| `15M` | `Bitfinex` | `28.98%` | `71.02%` | `0.41` | 3,980,000.00 USD |
| `15M` | `Kraken` | `47.92%` | `52.08%` | `0.92` | 78,240,000.00 USD |
| `15M` | `Aster` | `47.4%` | `52.6%` | `0.90` | 92,860,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `49.59%` | `50.41%` | `0.98` | 70,830,000.00 USD |
| `15M` | `Whale Positions` | `44.08%` | `55.92%` | `0.79` | 2,720,000,000.00 USD |
| `15M` | `Global Accounts` | `44.21%` | `55.79%` | `0.79` | 8,510,000,000.00 USD |
| `1H` | `ETH` | `40.33%` | `59.67%` | `0.68` | 14,160,000,000.00 USD |
| `1H` | `Binance` | `41.74%` | `58.26%` | `0.72` | 4,400,000,000.00 USD |
| `1H` | `OKX` | `39.29%` | `60.71%` | `0.65` | 1,880,000,000.00 USD |
| `1H` | `Bybit` | `37.93%` | `62.07%` | `0.61` | 1,740,000,000.00 USD |
| `1H` | `KuCoin` | `40.53%` | `59.47%` | `0.68` | 76,880,000.00 USD |
| `1H` | `Gate` | `49.68%` | `50.32%` | `0.99` | 831,910,000.00 USD |
| `1H` | `Bitget` | `48.21%` | `51.79%` | `0.93` | 626,390,000.00 USD |
| `1H` | `BingX` | `48.17%` | `51.83%` | `0.93` | 207,090,000.00 USD |
| `1H` | `MEXC` | `46.95%` | `53.05%` | `0.89` | 702,380,000.00 USD |
| `1H` | `Bitunix` | `48.57%` | `51.43%` | `0.94` | 710,320,000.00 USD |
| `1H` | `Hyperliquid` | `38.41%` | `61.59%` | `0.62` | 893,230,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.52%` | `46.48%` | `1.15` | 79,680,000.00 USD |
| `1H` | `Crypto.com` | `50.13%` | `49.87%` | `1.01` | 70,680,000.00 USD |
| `1H` | `WhiteBIT` | `18.69%` | `81.31%` | `0.23` | 1,220,000,000.00 USD |
| `1H` | `HTX` | `39.89%` | `60.11%` | `0.66` | 56,370,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `44.96%` | `55.04%` | `0.82` | 255,380,000.00 USD |
| `1H` | `Bitfinex` | `22.35%` | `77.65%` | `0.29` | 7,300,000.00 USD |
| `1H` | `Kraken` | `37.05%` | `62.95%` | `0.59` | 136,990,000.00 USD |
| `1H` | `Aster` | `40.73%` | `59.27%` | `0.69` | 147,030,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `46.76%` | `53.24%` | `0.88` | 129,970,000.00 USD |
| `1H` | `Whale Positions` | `41.74%` | `58.26%` | `0.72` | 4,400,000,000.00 USD |
| `1H` | `Global Accounts` | `40.33%` | `59.67%` | `0.68` | 14,160,000,000.00 USD |
| `4H` | `ETH` | `42.86%` | `57.14%` | `0.75` | 20,460,000,000.00 USD |
| `4H` | `Binance` | `42.57%` | `57.43%` | `0.74` | 6,200,000,000.00 USD |
| `4H` | `OKX` | `42.24%` | `57.76%` | `0.73` | 2,720,000,000.00 USD |
| `4H` | `Bybit` | `40.06%` | `59.94%` | `0.67` | 2,320,000,000.00 USD |
| `4H` | `KuCoin` | `39.68%` | `60.32%` | `0.66` | 100,700,000.00 USD |
| `4H` | `Gate` | `51.07%` | `48.93%` | `1.04` | 1,580,000,000.00 USD |
| `4H` | `Bitget` | `48.76%` | `51.24%` | `0.95` | 947,570,000.00 USD |
| `4H` | `BingX` | `51.35%` | `48.65%` | `1.06` | 323,700,000.00 USD |
| `4H` | `MEXC` | `48.57%` | `51.43%` | `0.94` | 1,090,000,000.00 USD |
| `4H` | `Bitunix` | `50.28%` | `49.72%` | `1.01` | 1,030,000,000.00 USD |
| `4H` | `Hyperliquid` | `42.01%` | `57.99%` | `0.72` | 1,240,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `54.52%` | `45.48%` | `1.20` | 123,450,000.00 USD |
| `4H` | `Crypto.com` | `50.49%` | `49.51%` | `1.02` | 129,600,000.00 USD |
| `4H` | `WhiteBIT` | `22.12%` | `77.88%` | `0.28` | 1,420,000,000.00 USD |
| `4H` | `HTX` | `42.54%` | `57.46%` | `0.74` | 83,260,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `50%` | `50%` | `1.00` | 444,300,000.00 USD |
| `4H` | `Bitfinex` | `27.35%` | `72.65%` | `0.38` | 11,680,000.00 USD |
| `4H` | `Kraken` | `38.69%` | `61.31%` | `0.63` | 184,960,000.00 USD |
| `4H` | `Aster` | `42.18%` | `57.82%` | `0.73` | 215,400,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.04%` | `52.96%` | `0.89` | 266,530,000.00 USD |
| `4H` | `Whale Positions` | `42.57%` | `57.43%` | `0.74` | 6,200,000,000.00 USD |
| `4H` | `Global Accounts` | `42.86%` | `57.14%` | `0.75` | 20,460,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2331.25` | `2330.55` | `2331.25` | `2334.25` | `2325.75` | 53,213,391.28 USD | 35,445,824.71 USD | 17,767,566.57 USD | 17,678,258.14 USD | `+33.22%` | `4B / 0S` |
| `0:00 UTC` | `2327.75` | `2328.10` | `2327.75` | `2331.25` | `2326.25` | 28,953,047.89 USD | 13,068,031.79 USD | 15,885,016.10 USD | -2,816,984.30 USD | `-9.73%` | `0B / 1S` |
| `5:00 UTC` | `2326.75` | `2328.61` | `2326.75` | `2331.75` | `2325.75` | 28,646,242.16 USD | 14,157,941.65 USD | 14,488,300.51 USD | -330,358.86 USD | `-1.15%` | `0B / 1S` |
| `0:00 UTC` | `2334.75` | `2334.23` | `2334.75` | `2336.25` | `2330.25` | 36,369,004.25 USD | 19,887,478.26 USD | 16,481,525.99 USD | 3,405,952.27 USD | `+9.36%` | `1B / 1S` |
| `5:00 UTC` | `2335.75` | `2336.07` | `2335.75` | `2338.75` | `2332.75` | 54,317,401.94 USD | 19,276,795.34 USD | 35,040,606.60 USD | -15,763,811.25 USD | `-29.02%` | `0B / 1S` |
| `0:00 UTC` | `2309.25` | `2313.87` | `2309.25` | `2335.75` | `2302.25` | 493,849,561.51 USD | 204,343,201.57 USD | 289,506,359.94 USD | -85,163,158.37 USD | `-17.24%` | `0B / 20S` |
| `5:00 UTC` | `2315.25` | `2315.75` | `2315.25` | `2318.75` | `2312.25` | 88,922,002.19 USD | 46,836,385.14 USD | 42,085,617.06 USD | 4,750,768.08 USD | `+5.34%` | `3B / 0S` |
| `0:00 UTC` | `2300.25` | `2278.61` | `2300.25` | `2319.25` | `2238.25` | 1,664,912,417.71 USD | 683,261,559.43 USD | 981,650,858.29 USD | -298,389,298.86 USD | `-17.92%` | `1B / 31S` |
| `5:00 UTC` | `2259.25` | `2255.66` | `2259.25` | `2277.25` | `2230.25` | 846,756,637.45 USD | 383,814,230.15 USD | 462,942,407.30 USD | -79,128,177.15 USD | `-9.34%` | `0B / 6S` |
| `0:00 UTC` | `2253.75` | `2255.52` | `2253.75` | `2265.75` | `2245.25` | 171,329,289.59 USD | 76,625,515.54 USD | 94,703,774.05 USD | -18,078,258.51 USD | `-10.55%` | `4B / 5S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 19:32` | `Volume 100K ETH` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `2340.90` | 17,000.00 USD | 0.00 USD |
| `10-28 19:06` | `Volume 100K ETH` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `2345.80` | 17,000.00 USD | 0.00 USD |
| `10-28 17:52` | `Volume 100K ETH` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `2349.00` | 30,000.00 USD | 0.00 USD |
| `10-28 17:43` | `Range 10` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `2349.90` | 49,000.00 USD | 0.00 USD |
| `10-28 14:06` | `Volume 100K ETH` | `Divergence` | **`BULLISH`** | Drop without taker selling | `2377.20` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 286,070.00 USD | -46,270,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -9,390,000.00 USD | -125,570,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -55,000,000.00 USD | -903,880,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -74,260,000.00 USD | -1,080,000,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -88,110,000.00 USD | -1,130,000,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -92,140,000.00 USD | -1,340,000,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -64,580,000.00 USD | -1,390,000,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -69,810,000.00 USD | -1,230,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -73,990,000.00 USD | -1,250,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -113,820,000.00 USD | -1,620,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -102,880,000.00 USD | -2,290,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,100,000,000.00 USD | -9,240,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+286.07K` | 15m=`-9.39M` | 1h=`-74.26M` | 24h=`-113.82M`
* Futures Capital Netflows: 5m=`-46.27M` | 15m=`-125.57M` | 1h=`-1.08B` | 24h=`-1.62B`
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
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:30:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2296.66` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2271.37` (Risk Distance: `25.29` pts)
  * +2.5R Take Profit: `2359.88`
  * Mathematical Lot Sizing: **`0.39 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2339.52` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2364.81` (Risk Distance: `25.29` pts)
  * +2.5R Take Profit: `2276.30`
  * Mathematical Lot Sizing: **`0.39 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2272.49`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
