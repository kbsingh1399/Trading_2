# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 10:56:00 IST` (`2026-10-30 05:26:00 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2239.80` | **Live Ask Quote**: `2242.90` | **Mid Price**: `2241.35`
- **Spread Points**: `310.00` | **Spread BPS**: `13.83 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2213.17` | VWAP Z-Score: `+1.75` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `15.97` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `53.62` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2260.99` | Lower -3.00σ Band: `2165.35`
  * Upper +2.51σ Band: `2253.18` | Lower -2.51σ Band: `2173.16`
  * Upper +2.01σ Band: `2245.21` | Lower -2.01σ Band: `2181.13`
  * Upper +2.00σ Band: `2245.05` | Lower -2.00σ Band: `2181.29`
  * Upper +1.28σ Band: `2233.57` | Lower -1.28σ Band: `2192.76`
  * Upper +1.00σ Band: `2229.11` | Lower -1.00σ Band: `2197.23`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2230.56` | EMA-20=`2229.92` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2254.57` (Slope: `+0.0000`) | EMA-100=`2281.04`
  * Institutional Anchors: EMA-144=`2293.06` | EMA-200=`2302.48` (Slope: `-0.4331`) | EMA-233=`2307.52`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2275.75` (Distance: `-1.48%`)
  * Point of Control (POC) = `2264.42` (Distance: `-0.98%`)
  * Value Area Low (VAL) = `2206.95` (Distance: `+1.59%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2351.85` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2246.50` | Low=`2235.00`
  * New York Session (13:00-21:00 UTC): High=`2254.80` | Low=`2227.90`
  * Initial Balance (First Hour): IB High=`2246.50` | IB Low=`2235.00`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2232.38` - `2250.32`
  * Optimal Trade Entry (OTE 0.705): `2245.83`
  * Structural Invalidation Anchor (0.786): `2259.28`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2247.14` | `2252.87` | `2246.99` | `2247.18` | `22,744` | 51,184,112.41 USD | 10,629,656.00 USD | `+20.77%` | -1,042,285,507.37 USD | `+1.56` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `2247.18` | `2249.00` | `2246.50` | `2247.88` | `9,361` | 21,038,975.52 USD | -2,868,689.83 USD | `-13.64%` | -1,045,154,197.20 USD | `-0.62` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `2247.90` | `2249.00` | `2244.60` | `2245.80` | `8,476` | 19,038,681.76 USD | -7,339,851.49 USD | `-38.55%` | -1,052,494,048.69 USD | `-1.29` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2245.13` | `2246.94` | `2241.38` | `2242.81` | `37,225` | 83,556,134.35 USD | 4,187,969.92 USD | `+5.01%` | -1,046,107,050.80 USD | `+0.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `2242.81` | `2252.87` | `2241.55` | `2247.18` | `47,793` | 107,425,896.61 USD | 12,910,248.16 USD | `+12.02%` | -1,033,196,802.65 USD | `+0.55` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `2247.18` | `2249.00` | `2244.60` | `2245.80` | `17,837` | 40,077,657.28 USD | -10,208,541.32 USD | `-25.47%` | -1,043,405,343.97 USD | `-0.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `2209.27` | `2238.00` | `2208.12` | `2236.82` | `225,707` | 502,124,659.31 USD | 34,201,688.52 USD | `+6.81%` | -1,027,139,167.10 USD | `+0.73` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2236.81` | `2246.94` | `2225.47` | `2242.81` | `206,764` | 463,074,415.24 USD | -1,345,167.52 USD | `-0.29%` | -1,028,484,334.62 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2242.81` | `2252.87` | `2241.55` | `2245.80` | `65,668` | 147,588,299.25 USD | 2,713,455.65 USD | `+1.84%` | -1,025,770,878.97 USD | `+0.45` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -701,515,761.74 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -963,151,175.97 USD | `-0.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2252.87` | `2225.47` | `2245.80` | `272,432` | 610,662,714.49 USD | 1,368,288.13 USD | `+0.22%` | -961,782,887.84 USD | `+0.75` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | 54,877,924.52 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -147,278,192.42 USD | `-1.22` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -701,515,761.74 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -963,151,175.97 USD | `-0.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2252.87` | `2225.47` | `2245.80` | `272,432` | 610,662,714.49 USD | 1,368,288.13 USD | `+0.22%` | -961,782,887.84 USD | `+0.75` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`2241.35`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2243.30` | `412.6264` | 925,644.80 USD | 10,916,589.19 USD | `10 orders` | `-0.09%` | `-` |
| `BID` | `2243.40` | `183.0962` | 410,758.02 USD | 9,990,944.39 USD | `4 orders` | `-0.08%` | `-` |
| `BID` | `2243.50` | `630.5391` | 1,414,614.47 USD | 9,580,186.37 USD | `12 orders` | `-0.08%` | `-` |
| `BID` | `2243.60` | `295.8210` | 663,704.00 USD | 8,165,571.90 USD | `8 orders` | `-0.07%` | `-` |
| `BID` | `2243.70` | `311.2621` | 698,378.77 USD | 7,501,867.91 USD | `8 orders` | `-0.07%` | `-` |
| `BID` | `2243.80` | `253.3583` | 568,485.35 USD | 6,803,489.13 USD | `5 orders` | `-0.06%` | `-` |
| `BID` | `2243.90` | `282.1510` | 633,118.63 USD | 6,235,003.78 USD | `11 orders` | `-0.06%` | `-` |
| `BID` | `2244.00` | `277.7647` | 623,303.99 USD | 5,601,885.15 USD | `10 orders` | `-0.06%` | `-` |
| `BID` | `2244.10` | `276.6774` | 620,891.75 USD | 4,978,581.16 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `2244.20` | `79.7237` | 178,915.93 USD | 4,357,689.41 USD | `10 orders` | `-0.05%` | `-` |
| `BID` | `2244.30` | `369.2045` | 828,605.66 USD | 4,178,773.48 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `2244.40` | `123.1107` | 276,309.66 USD | 3,350,167.82 USD | `8 orders` | `-0.04%` | `-` |
| `BID` | `2244.50` | `767.7798` | 1,723,281.76 USD | 3,073,858.17 USD | `9 orders` | `-0.03%` | `-` |
| `BID` | `2244.60` | `203.9174` | 457,713.00 USD | 1,350,576.41 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `2244.70` | `121.8153` | 273,438.80 USD | 892,863.41 USD | `11 orders` | `-0.02%` | `-` |
| `BID` | `2244.80` | `94.5418` | 212,227.43 USD | 619,424.61 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `2244.90` | `101.6486` | 228,190.94 USD | 407,197.17 USD | `8 orders` | `-0.02%` | `-` |
| `BID` | `2245.00` | `31.1893` | 70,019.98 USD | 179,006.23 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `2245.10` | `20.4116` | 45,826.08 USD | 108,986.25 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `2245.20` | `28.1312` | 63,160.17 USD | 63,160.17 USD | `7 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2245.25` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,245.25` | `0.00%` | `-` |
| `ASK` | `2245.30` | `139.6797` | 313,622.83 USD | 313,622.83 USD | `21 orders` | `+0.00%` | `-` |
| `ASK` | `2245.40` | `25.9436` | 58,253.76 USD | 371,876.59 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `2245.50` | `28.9171` | 64,933.35 USD | 436,809.94 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `2245.60` | `62.2057` | 139,689.12 USD | 576,499.06 USD | `9 orders` | `+0.02%` | `-` |
| `ASK` | `2245.70` | `95.1909` | 213,770.20 USD | 790,269.26 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `2245.80` | `37.1828` | 83,505.13 USD | 873,774.39 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `2245.90` | `136.5344` | 306,642.61 USD | 1,180,417.00 USD | `8 orders` | `+0.03%` | `-` |
| `ASK` | `2246.00` | `332.2299` | 746,188.36 USD | 1,926,605.36 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `2246.10` | `576.7640` | 1,295,469.62 USD | 3,222,074.98 USD | `9 orders` | `+0.04%` | `-` |
| `ASK` | `2246.20` | `192.6869` | 432,813.31 USD | 3,654,888.29 USD | `8 orders` | `+0.04%` | `-` |
| `ASK` | `2246.30` | `415.3837` | 933,076.41 USD | 4,587,964.70 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `2246.40` | `161.5425` | 362,889.07 USD | 4,950,853.77 USD | `9 orders` | `+0.05%` | `-` |
| `ASK` | `2246.50` | `123.8758` | 278,286.98 USD | 5,229,140.76 USD | `12 orders` | `+0.06%` | `-` |
| `ASK` | `2246.60` | `407.6583` | 915,845.14 USD | 6,144,985.89 USD | `9 orders` | `+0.06%` | `-` |
| `ASK` | `2246.70` | `348.1294` | 782,142.32 USD | 6,927,128.22 USD | `13 orders` | `+0.06%` | `-` |
| `ASK` | `2246.80` | `679.8984` | 1,527,595.73 USD | 8,454,723.94 USD | `20 orders` | `+0.07%` | `-` |
| `ASK` | `2246.90` | `145.1233` | 326,077.54 USD | 8,780,801.48 USD | `7 orders` | `+0.07%` | `-` |
| `ASK` | `2247.00` | `413.5961` | 929,350.44 USD | 9,710,151.92 USD | `6 orders` | `+0.08%` | `-` |
| `ASK` | `2247.10` | `157.5597` | 354,052.40 USD | 10,064,204.32 USD | `8 orders` | `+0.08%` | `-` |
| `ASK` | `2247.20` | `481.0218` | 1,080,952.19 USD | 11,145,156.51 USD | `13 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:53:16 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1844.19` | `7,964.66` | 14,688,299.29 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 10:53:16 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 10:53:16 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1913.44` | `6,500.22` | 12,437,784.60 USD | `AT_RISK_LIQ` | `0xf78c5d8d4b` | `2026-10-30 10:53:16 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `10,000.00` | 19,261,000.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 10:53:16 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1927.82` | `8,092.45` | 15,600,828.40 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 10:53:16 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2122.13` | `30,641.99` | 65,026,386.86 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 10:53:16 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.41` | `26,025.05` | 55,418,031.50 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 10:53:16 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,000.00` | 6,525,000.00 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2200.00` | `1,524.00` | 3,352,800.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x4b8600a785` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2208.20` | `2,077.83` | 4,588,254.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2214.50` | `503.85` | 1,115,778.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2218.80` | `401.99` | 891,943.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc86781f990` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2219.50` | `1,464.77` | 3,251,053.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2220.20` | `4,681.76` | 10,394,435.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.00` | `458.19` | 1,017,637.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9362ca4dfd` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2225.00` | `400.00` | 890,000.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x06bc596fb1` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.00` | `357.02` | 794,719.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.00` | `342.28` | 761,925.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2227.90` | `994.98` | 2,216,724.41 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2228.20` | `504.24` | 1,123,556.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2231.40` | `504.48` | 1,125,696.67 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2232.00` | `2,417.43` | 5,395,711.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2233.70` | `1,794.55` | 4,008,481.87 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.90` | `346.36` | 774,070.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2235.50` | `471.76` | 1,054,612.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2236.20` | `687.84` | 1,538,138.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2237.20` | `1,343.72` | 3,006,176.87 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2237.80` | `895.64` | 2,004,256.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2239.50` | `1,233.54` | 2,762,507.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2239.80` | `671.11` | 1,503,141.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2239.90` | `473.26` | 1,060,062.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2241.40` | `345.37` | 774,105.15 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2241.70` | `447.01` | 1,002,060.75 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2242.80` | `335.12` | 751,610.28 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2246.80` | `334.53` | 751,628.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2247.80` | `335.64` | 754,440.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2248.10` | `445.77` | 1,002,140.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2250.30` | `667.99` | 1,503,183.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2251.00` | `496.76` | 1,118,198.88 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2252.90` | `889.64` | 2,004,278.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2254.10` | `472.02` | 1,063,989.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2254.40` | `334.56` | 754,240.41 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2254.70` | `1,234.81` | 2,784,124.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2257.30` | `1,775.86` | 4,008,646.75 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2257.60` | `1,331.60` | 3,006,228.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2258.40` | `504.24` | 1,138,784.65 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2258.90` | `720.86` | 1,628,351.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2262.20` | `2,420.23` | 5,475,034.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2263.70` | `504.39` | 1,141,778.59 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2264.10` | `987.25` | 2,235,242.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.70` | `620.97` | 1,409,408.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.70` | `335.69` | 761,925.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.80` | `350.13` | 794,719.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.20` | `2,200.51` | 4,999,999.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb1ec7febea` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.80` | `1,371.68` | 3,117,562.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2275.70` | `4,696.65` | 10,688,176.87 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2282.20` | `503.86` | 1,149,904.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:53:16 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2283.80` | `2,015.35` | 4,602,650.62 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:53:16 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2300.00` | `4,002.10` | 9,204,832.99 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 10:53:16 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2457.31` | `22,046.99` | 54,176,241.78 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 10:53:16 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `2,733.67` | 6,872,176.53 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 10:53:16 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2624.15` | `10,000.00` | 26,241,459.22 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 10:53:16 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.00` | `9,700.00` | 25,782,604.68 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 10:53:16 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 238,971,612.27 USD | `106,417.71` | `2322.74` | `2247.30` | `3769.12` | 8,209,399.88 USD | `+3.44%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 145,402,034.21 USD | `64,680.62` | `2375.30` | `2247.30` | `4299.05` | 8,234,263.29 USD | `+5.66%` | `5X Cross` |
| `10` | `0x77dd...e0e9` | `LONG` | 68,892,389.94 USD | `30,641.99` | `2610.31` | `2247.30` | `2122.05` | -11,092,785.10 USD | `-16.10%` | `10X Cross` |
| `12` | `0xde8d...9524` | `LONG` | 68,056,673.63 USD | `30,282.40` | `2134.45` | `2247.30` | `1786.31` | 3,420,343.05 USD | `+5.03%` | `20X Cross` |
| `17` | `0x0392...d7d9` | `LONG` | 58,488,699.84 USD | `26,025.05` | `2518.71` | `2247.30` | `2129.33` | -7,061,022.25 USD | `-12.07%` | `9X Cross` |
| `23` | `0x8add...7d2c` | `SHORT` | 49,497,694.55 USD | `22,046.99` | `2271.09` | `2247.30` | `2451.60` | 573,202.75 USD | `+1.16%` | `25X Cross` |
| `27` | `0xdf95...7d72` | `SHORT` | 44,904,415.24 USD | `19,972.61` | `2402.53` | `2247.30` | `4170.68` | 3,080,466.58 USD | `+6.86%` | `25X Cross` |
| `34` | `0xeced...6210` | `SHORT` | 37,470,283.82 USD | `16,687.58` | `2522.09` | `2247.30` | `3479.14` | 4,617,431.17 USD | `+12.32%` | `20X Cross` |
| `35` | `0xb695...a92d` | `SHORT` | 35,902,291.29 USD | `15,968.64` | `2557.74` | `2247.30` | `3922.76` | 4,941,423.22 USD | `+13.76%` | `20X Cross` |
| `36` | `0x6046...b21d` | `LONG` | 35,809,999.92 USD | `15,927.59` | `2410.19` | `2247.30` | `1744.07` | -2,578,619.73 USD | `-7.20%` | `6X Cross` |
| `39` | `0x45d2...4029` | `SHORT` | 31,363,785.00 USD | `13,950.00` | `2443.60` | `2247.30` | `5221.42` | 2,724,497.46 USD | `+8.69%` | `20X Cross` |
| `44` | `0xa61c...66b9` | `LONG` | 28,973,899.44 USD | `12,888.00` | `2369.69` | `2247.30` | `1430.73` | -1,566,755.10 USD | `-5.41%` | `10X Cross` |
| `47` | `0xbd1c...ff0e` | `LONG` | 26,978,400.00 USD | `12,000.00` | `2419.91` | `2247.30` | `1520.19` | -2,060,632.39 USD | `-7.64%` | `20X Cross` |
| `48` | `0x2371...0883` | `LONG` | 26,976,000.00 USD | `12,000.00` | `2421.77` | `2247.30` | `1279.29` | -2,085,294.85 USD | `-7.73%` | `20X Cross` |
| `55` | `0x0c5d...36b3` | `LONG` | 24,731,300.00 USD | `11,000.00` | `2482.20` | `2247.30` | `1644.26` | -2,572,953.24 USD | `-10.40%` | `20X Cross` |
| `56` | `0x09dc...c094` | `LONG` | 24,731,300.00 USD | `11,000.00` | `2465.31` | `2247.30` | `1637.26` | -2,387,123.04 USD | `-9.65%` | `20X Cross` |
| `57` | `0x6c93...59a4` | `LONG` | 24,729,430.00 USD | `11,000.00` | `2441.15` | `2247.30` | `1602.22` | -2,123,242.73 USD | `-8.59%` | `20X Cross` |
| `58` | `0xa9de...e049` | `LONG` | 24,701,600.00 USD | `11,000.00` | `2481.81` | `2247.30` | `1643.93` | -2,598,379.46 USD | `-10.52%` | `20X Cross` |
| `71` | `0xa2ce...3126` | `LONG` | 22,520,940.51 USD | `10,016.88` | `2162.83` | `2247.30` | `1520.19` | 856,138.46 USD | `+3.80%` | `10X Cross` |
| `72` | `0xec7f...df39` | `LONG` | 22,483,000.00 USD | `10,000.00` | `2719.35` | `2247.30` | `1720.78` | -4,710,548.52 USD | `-20.95%` | `20X Cross` |
| `73` | `0xb37f...66ca` | `SHORT` | 22,483,000.00 USD | `10,000.00` | `2290.69` | `2247.30` | `2624.07` | 423,991.85 USD | `+1.89%` | `25X Cross` |
| `74` | `0x6646...6de5` | `LONG` | 22,482,000.00 USD | `10,000.00` | `1765.80` | `2247.30` | `1724.74` | 4,823,942.55 USD | `+21.46%` | `25X Cross` |
| `75` | `0x15a4...dfdb` | `LONG` | 22,456,000.00 USD | `10,000.00` | `1761.94` | `2247.30` | `242.39` | 4,836,518.97 USD | `+21.54%` | `20X Cross` |
| `76` | `0x939f...04d2` | `LONG` | 22,057,407.10 USD | `9,823.81` | `2427.28` | `2247.30` | `1793.63` | -1,787,743.50 USD | `-8.10%` | `25X Cross` |
| `78` | `0xaeaa...2416` | `SHORT` | 21,805,600.00 USD | `9,700.00` | `2311.92` | `2247.30` | `2657.93` | 620,082.40 USD | `+2.84%` | `25X Cross` |
| `83` | `0xf517...c032` | `SHORT` | 20,966,840.71 USD | `9,326.35` | `2202.91` | `2247.30` | `3176.17` | -421,702.49 USD | `-2.01%` | `25X Cross` |
| `85` | `0xca49...53c8` | `SHORT` | 20,669,580.07 USD | `9,193.84` | `2549.39` | `2247.30` | `3849.99` | 2,769,158.03 USD | `+13.40%` | `25X Cross` |
| `88` | `0xba5d...a352` | `SHORT` | 20,330,125.76 USD | `9,054.12` | `2493.89` | `2247.30` | `2898.05` | 2,249,881.50 USD | `+11.07%` | `20X Cross` |
| `89` | `0xea00...a918` | `LONG` | 20,235,199.23 USD | `9,003.83` | `2003.01` | `2247.30` | `1342.13` | 2,200,420.36 USD | `+10.87%` | `5X Cross` |
| `93` | `0xefe4...194b` | `SHORT` | 19,822,475.28 USD | `8,820.57` | `2267.42` | `2247.30` | `3520.24` | 177,539.12 USD | `+0.90%` | `20X Cross` |
| `106` | `0xecb6...2b00` | `SHORT` | 19,015,192.53 USD | `8,461.35` | `2242.92` | `2247.30` | `5847.65` | -37,035.45 USD | `-0.19%` | `15X Cross` |
| `115` | `0x9eec...daab` | `LONG` | 18,194,260.06 USD | `8,092.45` | `1658.44` | `2247.30` | `1926.76` | 4,773,395.53 USD | `+26.24%` | `15X Cross` |
| `116` | `0x5f91...65aa` | `LONG` | 17,899,767.67 USD | `7,964.66` | `1626.99` | `2247.30` | `1844.11` | 4,941,324.60 USD | `+27.61%` | `16X Cross` |
| `126` | `0xec0b...b078` | `LONG` | 15,754,442.94 USD | `7,007.80` | `2065.97` | `2247.30` | `1049.04` | 1,276,513.35 USD | `+8.10%` | `25X Cross` |
| `130` | `0xf02d...5eb3` | `LONG` | 15,413,146.68 USD | `6,855.99` | `2383.33` | `2247.30` | `1115.78` | -926,942.09 USD | `-6.01%` | `20X Cross` |
| `134` | `0xcf53...ee11` | `SHORT` | 15,296,596.61 USD | `6,803.63` | `1862.69` | `2247.30` | `4200.13` | -2,623,491.22 USD | `-17.15%` | `7X Cross` |
| `135` | `0x418a...8888` | `SHORT` | 15,118,429.85 USD | `6,724.38` | `2494.55` | `2247.30` | `3005.90` | 1,655,893.33 USD | `+10.95%` | `25X Cross` |
| `139` | `0x4ff9...38d3` | `LONG` | 14,739,027.22 USD | `6,564.10` | `2447.40` | `2247.30` | `1669.88` | -1,325,995.52 USD | `-9.00%` | `3X Isolated` |
| `142` | `0xf78c...c581` | `LONG` | 14,611,847.91 USD | `6,500.22` | `2521.53` | `2247.30` | `1913.36` | -1,778,693.04 USD | `-12.17%` | `20X Cross` |
| `143` | `0x1ee7...edf5` | `LONG` | 14,608,100.00 USD | `6,500.00` | `2301.55` | `2247.30` | `2069.10` | -351,993.66 USD | `-2.41%` | `25X Cross` |
| `145` | `0x799f...5f4c` | `LONG` | 14,187,731.04 USD | `6,310.90` | `2390.33` | `2247.30` | `1821.99` | -897,433.58 USD | `-6.33%` | `20X Cross` |
| `147` | `0xc179...e0c8` | `LONG` | 14,154,932.10 USD | `6,298.64` | `2294.94` | `2247.30` | `1217.04` | -300,085.18 USD | `-2.12%` | `10X Cross` |
| `150` | `0x08bf...7872` | `SHORT` | 13,992,280.96 USD | `6,224.05` | `2258.00` | `2247.30` | `2585.15` | 61,635.15 USD | `+0.44%` | `20X Cross` |
| `155` | `0xd9e7...4aff` | `LONG` | 13,489,800.00 USD | `6,000.00` | `2480.18` | `2247.30` | `1407.65` | -1,391,324.33 USD | `-10.31%` | `20X Cross` |
| `163` | `0x0c4a...1b19` | `LONG` | 12,709,182.93 USD | `5,660.10` | `2373.06` | `2247.30` | `2081.70` | -722,575.20 USD | `-5.69%` | `25X Isolated` |
| `168` | `0x7fda...17d1` | `LONG` | 11,951,951.64 USD | `5,315.76` | `2211.05` | `2247.30` | `0.000000` | 198,509.39 USD | `+1.66%` | `25X Cross` |
| `179` | `0x218a...7da2` | `SHORT` | 11,742,574.57 USD | `5,222.87` | `2208.16` | `2247.30` | `2792.80` | -209,639.51 USD | `-1.79%` | `10X Cross` |
| `188` | `0x45ab...6cbc` | `LONG` | 11,059,370.45 USD | `4,920.96` | `2727.66` | `2247.30` | `1368.20` | -2,363,373.35 USD | `-21.37%` | `7X Cross` |
| `193` | `0x64b7...9da9` | `LONG` | 10,918,805.91 USD | `4,856.84` | `2604.61` | `2247.30` | `566.55` | -1,731,408.50 USD | `-15.86%` | `25X Cross` |
| `198` | `0xfb18...eb17` | `SHORT` | 10,719,829.25 USD | `4,768.18` | `2315.53` | `2247.30` | `2597.54` | 321,052.55 USD | `+2.99%` | `25X Cross` |
| `200` | `0x5559...d43b` | `SHORT` | 10,678,479.08 USD | `4,755.93` | `2262.69` | `2247.30` | `2786.56` | 82,726.80 USD | `+0.77%` | `25X Cross` |
| `212` | `0xe091...6705` | `SHORT` | 10,117,350.45 USD | `4,500.00` | `2467.33` | `2247.30` | `2463.27` | 985,658.06 USD | `+9.74%` | `20X Cross` |
| `221` | `0xb829...3a81` | `LONG` | 9,881,078.40 USD | `4,394.91` | `2398.60` | `2247.30` | `1472.66` | -660,563.55 USD | `-6.69%` | `20X Cross` |
| `237` | `0x28bb...fca6` | `SHORT` | 9,463,759.97 USD | `4,209.61` | `1896.10` | `2247.30` | `3037.13` | -1,481,877.41 USD | `-15.66%` | `20X Cross` |
| `239` | `0x6ea4...0ea7` | `SHORT` | 9,404,404.45 USD | `4,184.01` | `2602.13` | `2247.30` | `3425.22` | 1,482,942.22 USD | `+15.77%` | `20X Cross` |
| `253` | `0x5e9e...35ee` | `SHORT` | 9,009,786.72 USD | `4,007.56` | `1796.39` | `2247.30` | `2585.71` | -1,810,636.63 USD | `-20.10%` | `20X Cross` |
| `254` | `0xfb94...0ddf` | `SHORT` | 8,994,322.46 USD | `4,002.10` | `2382.44` | `2247.30` | `5104.61` | 540,461.69 USD | `+6.01%` | `20X Cross` |
| `255` | `0x3dc9...54b0` | `SHORT` | 8,988,903.76 USD | `3,999.69` | `2480.32` | `2247.30` | `6436.47` | 931,632.80 USD | `+10.36%` | `20X Cross` |
| `256` | `0x8cc9...2b6a` | `SHORT` | 8,988,880.00 USD | `4,000.00` | `1791.18` | `2247.30` | `3531.21` | -1,824,133.33 USD | `-20.29%` | `25X Cross` |
| `273` | `0x4b67...f4e7` | `LONG` | 8,586,960.09 USD | `3,820.84` | `2591.51` | `2247.30` | `1333.67` | -1,314,813.46 USD | `-15.31%` | `20X Cross` |
| `277` | `0x12d2...f97f` | `LONG` | 8,446,811.62 USD | `3,757.26` | `2446.50` | `2247.30` | `1756.82` | -745,354.77 USD | `-8.82%` | `20X Cross` |
| `296` | `0x8ae4...3d60` | `LONG` | 7,988,511.00 USD | `3,558.20` | `2482.21` | `2247.30` | `478.89` | -843,687.03 USD | `-10.56%` | `10X Cross` |
| `336` | `0x4a20...3c26` | `LONG` | 6,744,900.00 USD | `3,000.00` | `2428.72` | `2247.30` | `505.82` | -541,260.28 USD | `-8.02%` | `20X Cross` |
| `337` | `0xb823...9763` | `SHORT` | 6,744,900.00 USD | `3,000.00` | `2229.66` | `2247.30` | `3233.61` | -55,903.32 USD | `-0.83%` | `25X Cross` |
| `338` | `0x007d...67a0` | `LONG` | 6,744,600.00 USD | `3,000.00` | `2400.00` | `2247.30` | `1474.53` | -455,400.00 USD | `-6.75%` | `25X Cross` |
| `339` | `0x469e...58a5` | `SHORT` | 6,743,100.00 USD | `3,000.00` | `2195.70` | `2247.30` | `3246.94` | -155,992.76 USD | `-2.31%` | `25X Cross` |
| `364` | `0x0622...8088` | `LONG` | 6,371,533.86 USD | `2,837.97` | `2213.38` | `2247.30` | `0.000000` | 90,006.84 USD | `+1.41%` | `5X Cross` |
| `365` | `0x9c2a...f6a8` | `SHORT` | 6,346,742.89 USD | `2,823.41` | `2533.78` | `2247.30` | `2626.89` | 807,167.93 USD | `+12.72%` | `20X Cross` |
| `391` | `0x8328...f54a` | `SHORT` | 5,792,635.01 USD | `2,576.45` | `2292.01` | `2247.30` | `3279.45` | 112,636.28 USD | `+1.94%` | `25X Cross` |
| `394` | `0xed48...7c9b` | `SHORT` | 5,735,706.70 USD | `2,551.13` | `2460.02` | `2247.30` | `3245.90` | 540,139.71 USD | `+9.42%` | `20X Cross` |
| `398` | `0x1c98...7fc7` | `LONG` | 5,619,260.11 USD | `2,500.00` | `2452.60` | `2247.30` | `1916.85` | -512,261.45 USD | `-9.12%` | `10X Cross` |
| `399` | `0x970c...2a93` | `SHORT` | 5,619,250.00 USD | `2,500.00` | `2229.57` | `2247.30` | `5045.02` | -45,305.51 USD | `-0.81%` | `20X Cross` |
| `414` | `0xa445...329d` | `LONG` | 5,409,715.12 USD | `2,406.14` | `2354.86` | `2247.30` | `1685.32` | -256,400.16 USD | `-4.74%` | `25X Cross` |
| `416` | `0xfbe2...c8ea` | `SHORT` | 5,362,658.65 USD | `2,385.21` | `2041.57` | `2247.30` | `2624.18` | -493,091.99 USD | `-9.19%` | `20X Cross` |
| `417` | `0x6749...ce07` | `SHORT` | 5,361,480.65 USD | `2,384.89` | `2220.92` | `2247.30` | `3630.75` | -64,817.62 USD | `-1.21%` | `20X Cross` |
| `419` | `0x645b...87b8` | `SHORT` | 5,351,137.14 USD | `2,379.98` | `2421.64` | `2247.30` | `11197.46` | 412,309.82 USD | `+7.71%` | `10X Cross` |
| `429` | `0x77ee...2902` | `SHORT` | 5,148,786.61 USD | `2,290.69` | `2476.53` | `2247.30` | `5933.13` | 524,185.63 USD | `+10.18%` | `25X Cross` |
| `437` | `0xbcd4...0dd2` | `SHORT` | 5,088,120.98 USD | `2,263.50` | `2233.24` | `2247.30` | `2656.74` | -33,163.41 USD | `-0.65%` | `25X Cross` |
| `453` | `0xd507...c948` | `SHORT` | 4,882,938.14 USD | `2,172.00` | `2387.49` | `2247.30` | `2600.45` | 302,702.89 USD | `+6.20%` | `5X Isolated` |
| `463` | `0x382b...3e39` | `SHORT` | 4,785,718.84 USD | `2,129.54` | `2296.66` | `2247.30` | `4641.78` | 105,118.38 USD | `+2.20%` | `25X Cross` |
| `464` | `0x023a...2355` | `LONG` | 4,772,439.75 USD | `2,123.54` | `2330.15` | `2247.30` | `0.000000` | -175,734.06 USD | `-3.68%` | `25X Cross` |
| `499` | `0x7a6d...f79c` | `SHORT` | 4,496,600.00 USD | `2,000.00` | `2418.41` | `2247.30` | `2543.43` | 340,232.11 USD | `+7.57%` | `25X Cross` |
| `500` | `0xe02e...d78b` | `LONG` | 4,496,600.00 USD | `2,000.00` | `2228.11` | `2247.30` | `2171.80` | 40,376.53 USD | `+0.90%` | `25X Cross` |
| `501` | `0x3453...b323` | `SHORT` | 4,495,076.65 USD | `2,000.12` | `2322.47` | `2247.30` | `2373.88` | 150,159.19 USD | `+3.34%` | `25X Cross` |
| `509` | `0xf3dc...1672` | `SHORT` | 4,451,654.17 USD | `1,980.36` | `2240.44` | `2247.30` | `2772.59` | -14,766.61 USD | `-0.33%` | `20X Cross` |
| `515` | `0xac48...3201` | `SHORT` | 4,414,724.01 USD | `1,964.37` | `2272.04` | `2247.30` | `3111.83` | 48,418.29 USD | `+1.10%` | `20X Cross` |
| `524` | `0x8376...9a1e` | `SHORT` | 4,293,648.71 USD | `1,910.50` | `2477.72` | `2247.30` | `3177.48` | 440,039.46 USD | `+10.25%` | `20X Cross` |
| `526` | `0x739c...cfb2` | `SHORT` | 4,271,010.00 USD | `1,900.00` | `2418.12` | `2247.30` | `2508.39` | 323,436.38 USD | `+7.57%` | `25X Cross` |
| `559` | `0x7265...91a5` | `LONG` | 4,046,277.92 USD | `1,801.87` | `2533.96` | `2247.30` | `1987.33` | -519,588.53 USD | `-12.84%` | `20X Cross` |
| `560` | `0xbb34...1696` | `LONG` | 4,045,320.00 USD | `1,800.00` | `2313.95` | `2247.30` | `1938.95` | -119,798.23 USD | `-2.96%` | `25X Cross` |
| `562` | `0xc619...10f5` | `LONG` | 4,041,180.00 USD | `1,800.00` | `2313.55` | `2247.30` | `1773.16` | -123,215.83 USD | `-3.05%` | `25X Cross` |
| `570` | `0x91a9...3f70` | `SHORT` | 3,973,118.29 USD | `1,767.48` | `2156.23` | `2247.30` | `3647.38` | -162,014.21 USD | `-4.08%` | `4X Cross` |
| `601` | `0xfeec...4e9c` | `SHORT` | 3,803,406.12 USD | `1,691.81` | `2566.49` | `2247.30` | `2508.53` | 538,618.40 USD | `+14.16%` | `10X Cross` |
| `616` | `0xeee0...0b53` | `LONG` | 3,679,108.54 USD | `1,637.12` | `2468.64` | `2247.30` | `145.31` | -362,367.52 USD | `-9.85%` | `7X Cross` |
| `620` | `0x982b...4606` | `LONG` | 3,656,109.20 USD | `1,626.82` | `2575.24` | `2247.30` | `1547.61` | -533,343.87 USD | `-14.59%` | `5X Isolated` |
| `621` | `0x27b8...12fc` | `LONG` | 3,655,292.44 USD | `1,628.12` | `2468.73` | `2247.30` | `581.32` | -364,102.20 USD | `-9.96%` | `10X Cross` |
| `630` | `0x73d7...8be1` | `LONG` | 3,600,414.74 USD | `1,601.47` | `2410.40` | `2247.30` | `1756.34` | -259,764.18 USD | `-7.21%` | `25X Cross` |
| `632` | `0xad54...6203` | `LONG` | 3,587,237.54 USD | `1,597.45` | `2591.98` | `2247.30` | `2051.96` | -553,340.51 USD | `-15.43%` | `10X Isolated` |
| `638` | `0x880a...311c` | `LONG` | 3,548,716.05 USD | `1,578.40` | `2209.72` | `2247.30` | `0.000000` | 60,892.19 USD | `+1.72%` | `9X Cross` |
| `658` | `0xe170...9300` | `SHORT` | 3,446,929.86 USD | `1,533.40` | `2076.39` | `2247.30` | `3141.35` | -262,980.36 USD | `-7.63%` | `25X Cross` |
| `663` | `0x4b86...df9d` | `SHORT` | 3,426,409.20 USD | `1,524.00` | `2287.40` | `2247.30` | `2759.80` | 59,588.40 USD | `+1.74%` | `9X Isolated` |
| `668` | `0x2e2b...2fab` | `LONG` | 3,388,432.76 USD | `1,507.38` | `2245.53` | `2247.30` | `1189.09` | 3,559.66 USD | `+0.11%` | `25X Cross` |
| `671` | `0xf929...d1f9` | `SHORT` | 3,372,450.00 USD | `1,500.00` | `2423.37` | `2247.30` | `2677.84` | 262,605.26 USD | `+7.79%` | `25X Cross` |
| `672` | `0x251f...6e5d` | `LONG` | 3,372,195.00 USD | `1,500.00` | `2346.68` | `2247.30` | `1804.99` | -147,835.49 USD | `-4.38%` | `20X Cross` |
| `674` | `0xde6b...3361` | `LONG` | 3,368,100.00 USD | `1,500.00` | `2216.98` | `2247.30` | `2168.73` | 42,619.26 USD | `+1.27%` | `25X Cross` |
| `692` | `0xb885...3c54` | `LONG` | 3,259,894.95 USD | `1,450.00` | `2274.34` | `2247.30` | `18.77` | -37,913.19 USD | `-1.16%` | `20X Cross` |
| `693` | `0x3440...32c5` | `SHORT` | 3,257,483.27 USD | `1,448.97` | `2198.21` | `2247.30` | `3771.71` | -72,332.30 USD | `-2.22%` | `25X Cross` |
| `697` | `0xef70...a84c` | `SHORT` | 3,243,431.44 USD | `1,442.74` | `2424.73` | `2247.30` | `3286.47` | 254,839.39 USD | `+7.86%` | `25X Cross` |
| `705` | `0x4b5f...0dd8` | `LONG` | 3,218,895.69 USD | `1,431.96` | `2339.45` | `2247.30` | `2147.89` | -131,097.25 USD | `-4.07%` | `10X Cross` |
| `707` | `0xbadb...9ee6` | `LONG` | 3,210,932.13 USD | `1,428.16` | `1936.00` | `2247.30` | `1052.01` | 446,010.48 USD | `+13.89%` | `20X Cross` |
| `763` | `0x53f8...ceff` | `LONG` | 3,031,640.00 USD | `1,348.65` | `2276.73` | `2247.30` | `0.000000` | -38,884.47 USD | `-1.28%` | `20X Cross` |
| `780` | `0x0dd5...f6ee` | `LONG` | 2,952,964.00 USD | `1,315.00` | `2306.05` | `2247.30` | `1560.23` | -79,500.38 USD | `-2.69%` | `5X Cross` |
| `805` | `0x1f16...6d07` | `LONG` | 2,846,347.80 USD | `1,266.00` | `2261.43` | `2247.30` | `1385.71` | -16,623.43 USD | `-0.58%` | `7X Cross` |
| `816` | `0xc435...c905` | `SHORT` | 2,802,508.80 USD | `1,248.00` | `2704.38` | `2247.30` | `4218.41` | 572,561.55 USD | `+20.43%` | `20X Cross` |
| `823` | `0x6859...7e1e` | `SHORT` | 2,781,282.57 USD | `1,237.15` | `2200.39` | `2247.30` | `4604.82` | -59,055.42 USD | `-2.12%` | `25X Cross` |
| `832` | `0x7277...0b98` | `SHORT` | 2,741,454.31 USD | `1,219.45` | `2206.05` | `2247.30` | `3338.96` | -51,266.51 USD | `-1.87%` | `20X Cross` |
| `835` | `0x7178...0854` | `LONG` | 2,739,361.75 USD | `1,218.63` | `2461.81` | `2247.30` | `1146.35` | -260,684.65 USD | `-9.52%` | `10X Cross` |
| `851` | `0xaaa1...ab8c` | `SHORT` | 2,696,880.00 USD | `1,200.00` | `2276.29` | `2247.30` | `2365.42` | 34,677.58 USD | `+1.29%` | `25X Isolated` |
| `862` | `0x07fd...689d` | `LONG` | 2,645,204.52 USD | `1,176.69` | `2416.34` | `2247.30` | `0.000000` | -198,095.42 USD | `-7.49%` | `25X Cross` |
| `902` | `0x6e6f...82a6` | `LONG` | 2,502,191.93 USD | `1,113.07` | `2266.07` | `2247.30` | `1356.85` | -20,124.36 USD | `-0.80%` | `20X Cross` |
| `906` | `0x0a97...347d` | `LONG` | 2,494,644.42 USD | `1,109.65` | `2267.88` | `2247.30` | `1494.73` | -21,917.96 USD | `-0.88%` | `20X Cross` |
| `913` | `0xbef3...0d3e` | `LONG` | 2,478,361.79 USD | `1,102.33` | `2233.44` | `2247.30` | `2174.44` | 16,377.38 USD | `+0.66%` | `20X Cross` |
| `916` | `0x6a41...a3b9` | `LONG` | 2,474,501.40 USD | `1,100.69` | `2233.05` | `2247.30` | `2177.22` | 16,596.65 USD | `+0.67%` | `20X Cross` |
| `925` | `0x2f80...f203` | `SHORT` | 2,448,266.28 USD | `1,088.94` | `1984.00` | `2247.30` | `2965.14` | -287,799.09 USD | `-11.76%` | `20X Cross` |
| `931` | `0x6f11...0389` | `SHORT` | 2,425,592.00 USD | `1,079.00` | `2333.39` | `2247.30` | `3198.91` | 92,136.91 USD | `+3.80%` | `25X Cross` |
| `935` | `0x8eb7...b90f` | `LONG` | 2,422,111.08 USD | `1,077.74` | `2396.38` | `2247.30` | `1881.14` | -160,566.96 USD | `-6.63%` | `5X Isolated` |
| `937` | `0x2b61...2f6c` | `SHORT` | 2,417,391.35 USD | `1,076.60` | `2681.75` | `2247.30` | `6341.34` | 469,781.39 USD | `+19.43%` | `10X Cross` |
| `960` | `0x30af...393e` | `SHORT` | 2,340,538.70 USD | `1,041.16` | `2252.26` | `2247.30` | `2297.11` | 4,443.63 USD | `+0.19%` | `25X Cross` |
| `966` | `0xa70a...4be9` | `LONG` | 2,324,980.30 USD | `1,034.15` | `2259.47` | `2247.30` | `850.27` | -11,660.18 USD | `-0.50%` | `20X Cross` |
| `974` | `0x4487...c92d` | `LONG` | 2,308,455.13 USD | `1,026.80` | `2229.14` | `2247.30` | `1567.59` | 19,561.47 USD | `+0.85%` | `10X Cross` |
| `975` | `0x1b2a...f7a6` | `LONG` | 2,304,412.04 USD | `1,025.37` | `2737.51` | `2247.30` | `882.27` | -502,547.90 USD | `-21.81%` | `10X Cross` |
| `984` | `0x001a...fef6` | `SHORT` | 2,264,567.33 USD | `1,007.33` | `2022.19` | `2247.30` | `3071.11` | -227,559.38 USD | `-10.05%` | `10X Cross` |
| `985` | `0x02aa...1806` | `SHORT` | 2,264,061.73 USD | `1,007.10` | `2654.68` | `2247.30` | `3612.90` | 409,470.37 USD | `+18.09%` | `20X Cross` |
| `988` | `0xdb3a...cf3b` | `LONG` | 2,255,227.54 USD | `1,003.22` | `2705.01` | `2247.30` | `0.000000` | -458,479.35 USD | `-20.33%` | `4X Cross` |
| `993` | `0x5272...fcd9` | `SHORT` | 2,248,100.00 USD | `1,000.00` | `2241.82` | `2247.30` | `2830.96` | -6,275.51 USD | `-0.28%` | `5X Cross` |
| `994` | `0x8c02...b73f` | `SHORT` | 2,247,900.00 USD | `1,000.00` | `2250.37` | `2247.30` | `8098.58` | 2,471.47 USD | `+0.11%` | `20X Cross` |
| `995` | `0xd7b8...9f55` | `LONG` | 2,243,054.70 USD | `999.00` | `2195.00` | `2247.30` | `0.000000` | 50,249.70 USD | `+2.24%` | `15X Cross` |
| `1016` | `0xb002...ed8a` | `SHORT` | 2,163,664.48 USD | `962.78` | `2299.66` | `2247.30` | `4199.47` | 50,413.42 USD | `+2.33%` | `25X Cross` |
| `1034` | `0xb812...b5e0` | `LONG` | 2,111,837.60 USD | `940.64` | `2263.21` | `2247.30` | `1185.00` | -17,039.22 USD | `-0.81%` | `25X Cross` |
| `1039` | `0xb1ec...e86a` | `SHORT` | 2,098,725.76 USD | `933.64` | `2272.72` | `2247.30` | `12733.86` | 23,181.20 USD | `+1.10%` | `25X Cross` |
| `1061` | `0xef96...9383` | `LONG` | 2,062,066.07 USD | `917.57` | `2235.00` | `2247.30` | `0.000000` | 11,282.42 USD | `+0.55%` | `25X Cross` |
| `1064` | `0xede2...f971` | `LONG` | 2,055,648.34 USD | `914.31` | `2208.16` | `2247.30` | `1463.18` | 36,691.36 USD | `+1.78%` | `5X Cross` |
| `1066` | `0x9606...4e5d` | `SHORT` | 2,052,325.28 USD | `913.00` | `2478.70` | `2247.30` | `4257.47` | 210,728.32 USD | `+10.27%` | `20X Cross` |
| `1080` | `0x5f10...d49d` | `LONG` | 2,023,290.00 USD | `900.00` | `2249.83` | `2247.30` | `1790.60` | -1,563.47 USD | `-0.08%` | `25X Cross` |
| `1142` | `0xa0fb...96be` | `LONG` | 1,952,307.26 USD | `868.35` | `2293.96` | `2247.30` | `1121.99` | -39,651.42 USD | `-2.03%` | `3X Cross` |
| `1180` | `0xcd27...52a8` | `LONG` | 1,882,044.26 USD | `837.21` | `2553.56` | `2247.30` | `1403.42` | -255,820.52 USD | `-13.59%` | `2X Cross` |
| `1204` | `0xd911...961e` | `LONG` | 1,850,188.38 USD | `823.29` | `2215.85` | `2247.30` | `0.000000` | 25,890.97 USD | `+1.40%` | `25X Cross` |
| `1229` | `0xb15b...dbae` | `SHORT` | 1,803,497.81 USD | `803.30` | `2290.80` | `2247.30` | `2257.16` | 36,711.54 USD | `+2.04%` | `25X Cross` |
| `1233` | `0x04a9...95aa` | `LONG` | 1,798,400.00 USD | `800.00` | `2595.13` | `2247.30` | `1863.22` | -277,706.74 USD | `-15.44%` | `5X Cross` |
| `1235` | `0x7737...bf66` | `SHORT` | 1,795,932.71 USD | `799.79` | `2494.83` | `2247.30` | `24409.75` | 199,413.32 USD | `+11.10%` | `15X Cross` |
| `1268` | `0x458d...ab3b` | `LONG` | 1,741,863.68 USD | `774.75` | `2740.41` | `2247.30` | `1887.17` | -381,265.50 USD | `-21.89%` | `3X Isolated` |
| `1286` | `0xb8eb...1dd5` | `LONG` | 1,696,644.74 USD | `754.94` | `2229.32` | `2247.30` | `0.000000` | 13,643.56 USD | `+0.80%` | `25X Cross` |
| `1326` | `0xaa53...9cb7` | `LONG` | 1,641,869.94 USD | `730.34` | `2389.70` | `2247.30` | `1969.14` | -103,419.70 USD | `-6.30%` | `20X Cross` |
| `1327` | `0x3fc5...c0c1` | `SHORT` | 1,640,796.61 USD | `729.92` | `2702.11` | `2247.30` | `4499.49` | 331,545.59 USD | `+20.21%` | `25X Cross` |
| `1331` | `0x6463...42f5` | `LONG` | 1,634,247.68 USD | `726.88` | `2214.40` | `2247.30` | `0.000000` | 24,637.01 USD | `+1.51%` | `1X Cross` |
| `1335` | `0x2e30...4cb5` | `SHORT` | 1,629,821.12 USD | `724.94` | `2334.43` | `2247.30` | `9031.88` | 62,514.93 USD | `+3.84%` | `2X Cross` |
| `1339` | `0xa189...94d7` | `SHORT` | 1,618,728.79 USD | `719.98` | `2691.84` | `2247.30` | `2915.03` | 319,343.88 USD | `+19.73%` | `25X Cross` |
| `1358` | `0x2f93...4404` | `LONG` | 1,590,608.17 USD | `707.47` | `1700.45` | `2247.30` | `1368.80` | 387,581.80 USD | `+24.37%` | `4X Isolated` |
| `1366` | `0x5605...fe0f` | `SHORT` | 1,578,629.46 USD | `702.14` | `2566.90` | `2247.30` | `3059.23` | 223,703.19 USD | `+14.17%` | `20X Cross` |
| `1371` | `0x7743...e4fe` | `SHORT` | 1,574,920.39 USD | `700.56` | `2298.56` | `2247.30` | `6178.18` | 35,354.70 USD | `+2.24%` | `25X Cross` |
| `1374` | `0x0deb...0bc5` | `LONG` | 1,573,691.00 USD | `700.00` | `2071.05` | `2247.30` | `1597.39` | 123,955.21 USD | `+7.88%` | `20X Cross` |
| `1403` | `0x51f6...2b39` | `LONG` | 1,554,432.35 USD | `691.38` | `2223.60` | `2247.30` | `369.40` | 17,071.33 USD | `+1.10%` | `25X Cross` |
| `1426` | `0x248e...6be2` | `SHORT` | 1,530,931.10 USD | `680.93` | `2282.89` | `2247.30` | `3455.31` | 23,554.57 USD | `+1.54%` | `20X Cross` |
| `1430` | `0xdbd1...29dd` | `SHORT` | 1,530,423.43 USD | `680.70` | `3030.57` | `2247.30` | `3775.25` | 532,497.69 USD | `+34.79%` | `6X Cross` |
| `1436` | `0x71e5...be04` | `LONG` | 1,523,462.73 USD | `677.67` | `2727.27` | `2247.30` | `1470.95` | -324,722.87 USD | `-21.31%` | `20X Cross` |
| `1444` | `0x0b23...f37b` | `LONG` | 1,517,197.50 USD | `675.00` | `2238.15` | `2247.30` | `591.26` | 6,440.86 USD | `+0.42%` | `5X Cross` |
| `1473` | `0x0cac...6170` | `SHORT` | 1,478,191.50 USD | `657.50` | `2146.55` | `2247.30` | `2839.40` | -66,829.30 USD | `-4.52%` | `20X Cross` |
| `1505` | `0xf00e...fe3d` | `SHORT` | 1,445,277.81 USD | `642.88` | `2333.21` | `2247.30` | `2476.06` | 54,700.16 USD | `+3.78%` | `20X Cross` |
| `1510` | `0xffb2...5ed6` | `SHORT` | 1,440,251.54 USD | `640.77` | `2672.96` | `2247.30` | `2515.98` | 272,496.81 USD | `+18.92%` | `20X Cross` |
| `1518` | `0x8505...1821` | `SHORT` | 1,425,206.15 USD | `633.96` | `2239.93` | `2247.30` | `3905.86` | -5,174.55 USD | `-0.36%` | `20X Cross` |
| `1539` | `0xfce0...f4c0` | `SHORT` | 1,401,478.64 USD | `623.60` | `3129.61` | `2247.30` | `2801.83` | 550,147.94 USD | `+39.25%` | `20X Cross` |
| `1587` | `0xad02...eb65` | `LONG` | 1,350,254.27 USD | `600.62` | `2460.69` | `2247.30` | `1078.87` | -127,686.29 USD | `-9.46%` | `5X Cross` |
| `1588` | `0x24fb...ed0f` | `LONG` | 1,348,955.80 USD | `600.10` | `2199.85` | `2247.30` | `0.000000` | 28,832.36 USD | `+2.14%` | `15X Cross` |
| `1589` | `0x638f...f5f0` | `LONG` | 1,348,920.00 USD | `600.00` | `4011.50` | `2247.30` | `305.99` | -1,057,983.53 USD | `-78.43%` | `25X Cross` |
| `1590` | `0x26e6...6b28` | `LONG` | 1,348,440.00 USD | `600.00` | `1769.78` | `2247.30` | `2004.67` | 286,568.47 USD | `+21.25%` | `20X Cross` |
| `1659` | `0xfc66...ca06` | `SHORT` | 1,275,759.39 USD | `567.43` | `2275.19` | `2247.30` | `7322.06` | 15,263.82 USD | `+1.20%` | `20X Cross` |
| `1661` | `0x9362...7d7c` | `SHORT` | 1,273,127.20 USD | `566.99` | `2226.19` | `2247.30` | `2518.85` | -10,891.39 USD | `-0.86%` | `20X Cross` |
| `1668` | `0xfb99...37f3` | `LONG` | 1,270,547.59 USD | `565.34` | `2362.35` | `2247.30` | `1241.68` | -64,988.77 USD | `-5.12%` | `3X Cross` |
| `1678` | `0x844b...7f42` | `SHORT` | 1,259,669.40 USD | `561.00` | `2026.17` | `2247.30` | `2987.91` | -122,985.99 USD | `-9.76%` | `25X Cross` |
| `1689` | `0xabe6...1d99` | `SHORT` | 1,249,969.27 USD | `556.00` | `2484.68` | `2247.30` | `3091.66` | 131,526.62 USD | `+10.52%` | `20X Cross` |
| `1691` | `0x2a76...9a53` | `LONG` | 1,247,562.02 USD | `554.99` | `2231.40` | `2247.30` | `0.000000` | 9,154.96 USD | `+0.73%` | `25X Cross` |
| `1706` | `0x7a76...b16d` | `LONG` | 1,238,184.54 USD | `550.97` | `2238.40` | `2247.30` | `2073.07` | 4,902.69 USD | `+0.40%` | `25X Cross` |
| `1709` | `0x825c...465e` | `LONG` | 1,236,471.50 USD | `550.00` | `2208.12` | `2247.30` | `1189.46` | 22,002.00 USD | `+1.78%` | `4X Cross` |
| `1710` | `0x936c...bb0f` | `LONG` | 1,236,214.11 USD | `550.09` | `2218.31` | `2247.30` | `0.000000` | 15,946.84 USD | `+1.29%` | `20X Cross` |
| `1716` | `0xad21...fb6a` | `LONG` | 1,230,395.44 USD | `547.26` | `2565.80` | `2247.30` | `1729.44` | -173,757.56 USD | `-14.12%` | `6X Cross` |
| `1817` | `0x0c7a...2f50` | `SHORT` | 1,144,936.21 USD | `509.25` | `2122.56` | `2247.30` | `4102.69` | -64,030.78 USD | `-5.59%` | `20X Cross` |
| `1824` | `0x0089...2410` | `SHORT` | 1,140,563.64 USD | `507.35` | `2308.88` | `2247.30` | `3417.06` | 30,836.62 USD | `+2.70%` | `20X Cross` |
| `1827` | `0x31de...13f2` | `LONG` | 1,137,580.66 USD | `506.00` | `2251.82` | `2247.30` | `0.000000` | -1,831.93 USD | `-0.16%` | `20X Cross` |
| `1840` | `0x89b2...9ca6` | `LONG` | 1,124,150.00 USD | `500.00` | `2363.45` | `2247.30` | `1622.65` | -57,577.42 USD | `-5.12%` | `25X Cross` |
| `1841` | `0xb322...d51f` | `SHORT` | 1,124,065.00 USD | `500.00` | `2268.03` | `2247.30` | `3783.70` | 9,951.32 USD | `+0.89%` | `20X Cross` |
| `1842` | `0xe282...df29` | `LONG` | 1,124,000.00 USD | `500.00` | `2309.84` | `2247.30` | `2045.31` | -30,924.21 USD | `-2.75%` | `10X Isolated` |
| `1843` | `0x6936...9417` | `SHORT` | 1,123,950.00 USD | `500.00` | `2315.11` | `2247.30` | `2358.91` | 33,605.21 USD | `+2.99%` | `25X Isolated` |
| `1844` | `0x4044...794c` | `LONG` | 1,123,700.00 USD | `500.00` | `2260.80` | `2247.30` | `0.000000` | -6,700.00 USD | `-0.60%` | `25X Cross` |
| `1845` | `0xa559...ff95` | `LONG` | 1,123,650.00 USD | `500.00` | `2260.68` | `2247.30` | `1046.04` | -6,694.36 USD | `-0.60%` | `20X Cross` |
| `1851` | `0x7298...7d6c` | `SHORT` | 1,119,540.74 USD | `498.15` | `3426.75` | `2247.30` | `5421.61` | 587,495.08 USD | `+52.48%` | `20X Cross` |
| `1862` | `0xfc27...9d9d` | `LONG` | 1,110,418.99 USD | `494.09` | `2242.73` | `2247.30` | `0.000000` | 2,306.97 USD | `+0.21%` | `25X Cross` |
| `1865` | `0x9c68...7783` | `SHORT` | 1,108,610.62 USD | `493.31` | `2273.58` | `2247.30` | `3946.93` | 12,968.63 USD | `+1.17%` | `25X Cross` |
| `1872` | `0x404c...5f03` | `SHORT` | 1,101,184.29 USD | `489.79` | `2671.94` | `2247.30` | `4911.59` | 207,495.27 USD | `+18.84%` | `20X Cross` |
| `1877` | `0x321f...1c84` | `SHORT` | 1,095,838.58 USD | `488.02` | `2370.09` | `2247.30` | `3047.48` | 60,806.02 USD | `+5.55%` | `10X Cross` |
| `1904` | `0x34fb...93de` | `LONG` | 1,068,206.44 USD | `475.18` | `2219.83` | `2247.30` | `0.000000` | 13,383.59 USD | `+1.25%` | `20X Cross` |
| `1929` | `0xe86b...3664` | `LONG` | 1,050,407.79 USD | `467.39` | `2231.29` | `2247.30` | `0.000000` | 7,526.86 USD | `+0.72%` | `25X Cross` |
| `1945` | `0x94b6...e5b3` | `SHORT` | 1,042,845.56 USD | `463.86` | `2261.12` | `2247.30` | `2410.81` | 5,997.11 USD | `+0.58%` | `25X Cross` |
| `1950` | `0x82c6...fe42` | `LONG` | 1,039,422.50 USD | `462.50` | `2501.38` | `2247.30` | `2053.65` | -117,468.07 USD | `-11.30%` | `5X Isolated` |
| `1952` | `0x71d0...8c26` | `LONG` | 1,037,952.81 USD | `461.87` | `2225.97` | `2247.30` | `0.000000` | 9,847.81 USD | `+0.95%` | `25X Cross` |
| `1955` | `0xe330...77a1` | `SHORT` | 1,036,641.49 USD | `461.20` | `2206.97` | `2247.30` | `6421.27` | -18,784.12 USD | `-1.81%` | `20X Cross` |
| `1958` | `0x2de3...486d` | `LONG` | 1,035,025.24 USD | `460.40` | `2286.27` | `2247.30` | `1223.93` | -17,575.67 USD | `-1.70%` | `25X Cross` |
| `1965` | `0x617e...0f97` | `SHORT` | 1,029,302.48 USD | `457.85` | `2205.60` | `2247.30` | `3327.18` | -19,458.64 USD | `-1.89%` | `10X Cross` |
| `2005` | `0x0514...bdfe` | `SHORT` | 1,011,735.00 USD | `450.00` | `1988.74` | `2247.30` | `3698.73` | -116,798.16 USD | `-11.54%` | `25X Cross` |
| `2006` | `0xae55...2236` | `LONG` | 1,011,735.00 USD | `450.00` | `2510.21` | `2247.30` | `0.000000` | -117,862.50 USD | `-11.65%` | `25X Cross` |
| `2009` | `0xc10f...23b3` | `LONG` | 1,010,430.00 USD | `450.00` | `2366.44` | `2247.30` | `2016.72` | -54,468.27 USD | `-5.39%` | `25X Cross` |
| `2019` | `0xac26...a9c7` | `SHORT` | 1,003,047.34 USD | `446.14` | `2192.58` | `2247.30` | `8640.78` | -24,856.80 USD | `-2.48%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 10,204.16 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 10.20K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 79.74 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.08K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 281.98 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.28K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 16.18 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 353.86 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.35K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 979.76 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.98K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 477.98 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.48K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 159.02 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.16K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 2,234.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.23K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 3,374.27 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 3.37K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 509.87 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.51K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 2,320.55 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.32K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 122.96 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.12K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 2,462.69 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.46K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 11.79 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.01K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 306.71 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.31K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 1,968.07 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.97K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 3,369.18 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 3.37K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 331.67 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.33K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 1,642.64 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.64K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 870.20 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.87K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 2,646.67 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.65K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 4,964.44 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 4.96K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2311.30` | 13,824.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 13.82K USD at 2311.3000 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2323.10` | 1,557.17 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.56K USD at 2323.1000 USD [API] | `2026-10-29 01:48:11` |
| `ANNOUNCEMENT` | `INFO` | `2308.10` | 108,950.17 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 108.95K USD at 2308.1000 USD [API] | `2026-10-29 02:18:56` |
| `ANNOUNCEMENT` | `INFO` | `2300.40` | 41,119.19 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 41.12K USD at 2300.4000 USD [API] | `2026-10-29 02:34:40` |
| `ANNOUNCEMENT` | `INFO` | `2298.30` | 19.08 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2298.3000 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `2298.30` | 29.42 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.03K USD at 2298.3000 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `2332.40` | 222.74 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.22K USD at 2332.4000 USD [API] | `2026-10-29 01:39:01` |
| `ANNOUNCEMENT` | `INFO` | `2307.70` | 47,348.47 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 47.35K USD at 2307.7000 USD [API] | `2026-10-29 03:08:30` |
| `ANNOUNCEMENT` | `INFO` | `2307.70` | 59,998.35 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 60.00K USD at 2307.7000 USD [API] | `2026-10-29 03:08:30` |
| `ANNOUNCEMENT` | `INFO` | `2307.70` | 69,999.46 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 70.00K USD at 2307.7000 USD [API] | `2026-10-29 03:08:30` |
| `ANNOUNCEMENT` | `INFO` | `2315.20` | 7,711.93 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 7.71K USD at 2315.2000 USD [API] | `2026-10-29 01:48:20` |
| `ANNOUNCEMENT` | `INFO` | `2315.20` | 5,769.48 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 5.77K USD at 2315.2000 USD [API] | `2026-10-29 01:48:20` |
| `ANNOUNCEMENT` | `INFO` | `2315.20` | 128.49 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.13K USD at 2315.2000 USD [API] | `2026-10-29 01:48:20` |
| `ANNOUNCEMENT` | `INFO` | `2315.20` | 206.28 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.21K USD at 2315.2000 USD [API] | `2026-10-29 01:48:20` |
| `ANNOUNCEMENT` | `INFO` | `2315.20` | 35.65 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.04K USD at 2315.2000 USD [API] | `2026-10-29 01:48:20` |
| `ANNOUNCEMENT` | `INFO` | `2315.20` | 629.73 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.63K USD at 2315.2000 USD [API] | `2026-10-29 01:48:20` |
| `ANNOUNCEMENT` | `INFO` | `2315.20` | 2,317.98 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.32K USD at 2315.2000 USD [API] | `2026-10-29 01:48:20` |
| `ANNOUNCEMENT` | `INFO` | `2315.20` | 863.80 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.86K USD at 2315.2000 USD [API] | `2026-10-29 01:48:20` |
| `ANNOUNCEMENT` | `INFO` | `2377.70` | 76,324.17 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 76.32K USD at 2377.7000 USD [API] | `2026-10-28 20:00:18` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2251.83` (Vol: 25,800,000.00 USD, Dist: `+0.39%`) | Long MP=`2174.37` (Vol: 35,800,000.00 USD, Dist: `--3.06%`)
  * 48H Horizon: Short MP=`2402.29` (Vol: 25,600,000.00 USD, Dist: `+7.10%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--3.08%`)
  * 3D Horizon: Short MP=`2402.29` (Vol: 31,100,000.00 USD, Dist: `+7.10%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--3.08%`)
  * 7D Horizon: Short MP=`2401.80` (Vol: 50,700,000.00 USD, Dist: `+7.08%`) | Long MP=`2175.27` (Vol: 44,800,000.00 USD, Dist: `--3.02%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `455.00` | 70,210.00 USD | 758,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `465.00` | 39,370.00 USD | 758,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 105,690.00 USD | 758,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 5,010.00 USD | 758,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 1,870,000.00 USD | 758,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 21,630.00 USD | 756,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 131,890.00 USD | 756,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 2,050.00 USD | 756,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 10,240.00 USD | 756,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 13,990.00 USD | 756,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 252,780.00 USD | 756,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 1,760,000.00 USD | 756,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 44,530.00 USD | 754,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 2,860,000.00 USD | 754,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 447,610.00 USD | 751,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 1,130,000.00 USD | 750,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 59,650.00 USD | 749,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 26,610.00 USD | 749,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 7,190.00 USD | 749,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 65,540.00 USD | 749,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 179,860.00 USD | 749,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 30,530.00 USD | 749,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 58,400.00 USD | 749,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 61,280.00 USD | 749,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 1,170,000.00 USD | 749,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 2,950.00 USD | 748,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 11,530.00 USD | 748,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 415,590.00 USD | 748,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 116,150.00 USD | 747,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 958.22 USD | 747,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 35,090.00 USD | 747,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 74,190.00 USD | 747,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 75,950.00 USD | 747,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 34,790.00 USD | 747,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 104,970.00 USD | 747,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 44,510.00 USD | 747,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 86,380.00 USD | 747,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 356,620.00 USD | 747,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 39,330.00 USD | 746,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 172,470.00 USD | 746,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 489,100.00 USD | 746,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 138,490.00 USD | 746,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 282,060.00 USD | 745,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 991,570.00 USD | 745,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 253,960.00 USD | 744,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 321,510.00 USD | 744,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 191,390.00 USD | 744,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 201,010.00 USD | 743,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 135,060.00 USD | 743,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 230,060.00 USD | 743,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 20,590.00 USD | 743,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 28,020.00 USD | 743,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 532,060.00 USD | 743,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 5,370,000.00 USD | 742,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 1,180,000.00 USD | 737,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 161,470.00 USD | 736,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 229,050.00 USD | 736,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 160,140.00 USD | 735,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 39,300.00 USD | 735,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 925,460.00 USD | 735,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 7,410,000.00 USD | 734,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 1,540,000.00 USD | 727,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 753,780.00 USD | 725,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 328,160.00 USD | 724,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 61,260.00 USD | 724,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 158,010.00 USD | 724,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 7,660,000.00 USD | 724,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 1,310,000.00 USD | 716,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 565,980.00 USD | 715,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 226,120.00 USD | 714,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 755,360.00 USD | 714,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 1,450,000.00 USD | 713,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 219,750.00 USD | 712,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 2,730,000.00 USD | 712,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 323,550.00 USD | 709,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 200,180.00 USD | 709,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 112,000.00 USD | 708,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 2,260,000.00 USD | 708,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 94,510.00 USD | 706,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 768,060.00 USD | 706,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 461,080.00 USD | 705,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 205,060.00 USD | 705,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 15,430,000.00 USD | 705,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 264,370.00 USD | 689,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 176,850.00 USD | 689,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 654,450.00 USD | 689,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 125,690.00 USD | 688,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 460,240.00 USD | 688,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 5,400,000.00 USD | 687,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 436,480.00 USD | 682,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 12,690,000.00 USD | 682,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 1,070,000.00 USD | 669,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 7,070,000.00 USD | 668,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 2,570,000.00 USD | 661,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 2,050,000.00 USD | 658,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 10,660,000.00 USD | 656,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 45,260.00 USD | 646,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 18,640,000.00 USD | 645,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 1,310,000.00 USD | 627,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 56,350.00 USD | 626,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 6,870,000.00 USD | 625,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 1,990,000.00 USD | 619,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 5,640,000.00 USD | 617,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 149,240.00 USD | 611,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 876,920.00 USD | 611,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 437,140.00 USD | 610,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 582,560.00 USD | 610,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 20,580,000.00 USD | 609,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 16,240,000.00 USD | 588,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 2,850,000.00 USD | 572,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 1,120,000.00 USD | 569,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 2,660,000.00 USD | 568,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 587,950.00 USD | 565,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 803,000.00 USD | 565,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 1,520,000.00 USD | 564,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 18,380,000.00 USD | 563,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 707,630.00 USD | 544,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 2,070,000.00 USD | 543,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 18,720,000.00 USD | 541,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 38,610,000.00 USD | 523,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 745,590.00 USD | 484,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 11,980,000.00 USD | 483,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 1,340,000.00 USD | 471,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 784,890.00 USD | 470,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 341,360.00 USD | 469,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 4,840,000.00 USD | 469,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 250,360.00 USD | 464,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 36,980,000.00 USD | 464,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 1,750,000.00 USD | 427,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 1,350,000.00 USD | 425,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 28,620,000.00 USD | 424,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 20,810,000.00 USD | 395,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 3,780,000.00 USD | 374,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 61,330,000.00 USD | 370,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 408,110.00 USD | 309,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 3,060,000.00 USD | 309,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 769,970.00 USD | 306,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 1,630,000.00 USD | 305,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 12,510,000.00 USD | 303,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 19,230,000.00 USD | 291,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 2,430,000.00 USD | 272,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 1,940,000.00 USD | 269,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 6,110,000.00 USD | 267,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 5,450,000.00 USD | 261,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 653,900.00 USD | 256,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 494,920.00 USD | 255,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 18,350,000.00 USD | 254,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 16,610,000.00 USD | 236,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 1,270,000.00 USD | 220,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 5,010,000.00 USD | 218,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 2,760,000.00 USD | 213,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 1,110,000.00 USD | 210,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1972.00` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,810,000.00 USD | 209,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1975.30` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1978.60` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1981.90` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1985.00` | 5,620,000.00 USD | 208,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1988.50` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 3,730,000.00 USD | 1,780,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1988.60` | 676,050,000.00 USD | 676,050,000.00 USD | 1,210,000.00 USD | 1,370,000.00 USD | 374,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1991.10` | 673,090,000.00 USD | 673,090,000.00 USD | 1,580,000.00 USD | 0.00 USD | 438,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1991.80` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1993.60` | 671,070,000.00 USD | 671,070,000.00 USD | 202,370.00 USD | 596,570.00 USD | 21,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1995.00` | 1,490,000.00 USD | 202,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1995.10` | 999,730,000.00 USD | 999,730,000.00 USD | 1,340,000.00 USD | 0.00 USD | 808,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1996.10` | 670,250,000.00 USD | 670,250,000.00 USD | 412,250.00 USD | 61,370.00 USD | 304,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2001.10` | 669,470,000.00 USD | 669,470,000.00 USD | 0.00 USD | 18,870.00 USD | 487,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2003.60` | 668,960,000.00 USD | 668,960,000.00 USD | 0.00 USD | 198,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2005.00` | 997,580,000.00 USD | 997,580,000.00 USD | 0.00 USD | 266,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2005.00` | 2,050,000.00 USD | 200,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2006.10` | 668,770,000.00 USD | 668,770,000.00 USD | 14,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2008.60` | 668,750,000.00 USD | 668,750,000.00 USD | 0.00 USD | 224,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2011.10` | 668,530,000.00 USD | 668,530,000.00 USD | 48,560.00 USD | 320,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2011.60` | 997,320,000.00 USD | 997,320,000.00 USD | 170,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2013.60` | 668,160,000.00 USD | 668,160,000.00 USD | 250,530.00 USD | 229,750.00 USD | 17,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2015.00` | 2,810,000.00 USD | 198,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2016.10` | 667,660,000.00 USD | 667,660,000.00 USD | 330,880.00 USD | 497,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2018.60` | 666,830,000.00 USD | 666,830,000.00 USD | 737,290.00 USD | 1,100,000.00 USD | 714,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2021.10` | 664,270,000.00 USD | 664,270,000.00 USD | 973,110.00 USD | 952,000.00 USD | 794,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2023.60` | 661,560,000.00 USD | 661,560,000.00 USD | 0.00 USD | 0.00 USD | 323,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2024.80` | 997,140,000.00 USD | 997,140,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 834,860.00 USD | 196,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2026.10` | 661,230,000.00 USD | 661,230,000.00 USD | 0.00 USD | 1,100,000.00 USD | 28,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.10` | 996,970,000.00 USD | 996,970,000.00 USD | 0.00 USD | 0.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2028.60` | 660,100,000.00 USD | 660,100,000.00 USD | 1,430,000.00 USD | 1,210,000.00 USD | 598,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2031.10` | 656,870,000.00 USD | 656,870,000.00 USD | 677,540.00 USD | 293,350.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.40` | 996,930,000.00 USD | 996,930,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2033.60` | 654,820,000.00 USD | 654,820,000.00 USD | 941,100.00 USD | 1,330,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2034.70` | 992,370,000.00 USD | 992,370,000.00 USD | 0.00 USD | 186,130.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 588,290.00 USD | 195,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2036.10` | 652,550,000.00 USD | 652,550,000.00 USD | 985,830.00 USD | 159,790.00 USD | 176,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.00` | 990,820,000.00 USD | 990,820,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2038.60` | 651,230,000.00 USD | 651,230,000.00 USD | 939,380.00 USD | 317,820.00 USD | 377,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2041.10` | 649,590,000.00 USD | 649,590,000.00 USD | 626,840.00 USD | 178,560.00 USD | 176,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2043.60` | 648,610,000.00 USD | 648,610,000.00 USD | 0.00 USD | 0.00 USD | 28,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2044.60` | 989,220,000.00 USD | 989,220,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 1,980,000.00 USD | 194,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2046.10` | 648,580,000.00 USD | 648,580,000.00 USD | 0.00 USD | 0.00 USD | 19,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2048.60` | 648,560,000.00 USD | 648,560,000.00 USD | 518,440.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2051.10` | 647,690,000.00 USD | 647,690,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2051.20` | 988,920,000.00 USD | 988,920,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2053.60` | 646,630,000.00 USD | 646,630,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2054.50` | 988,700,000.00 USD | 988,700,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 7,180,000.00 USD | 192,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2056.10` | 646,510,000.00 USD | 646,510,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2057.80` | 986,420,000.00 USD | 986,420,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2058.60` | 646,270,000.00 USD | 646,270,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2061.10` | 645,520,000.00 USD | 645,520,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.10` | 986,360,000.00 USD | 986,360,000.00 USD | 1,700,000.00 USD | 1,310,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2063.60` | 645,440,000.00 USD | 645,440,000.00 USD | 563,140.00 USD | 494,150.00 USD | 510,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.40` | 981,640,000.00 USD | 981,640,000.00 USD | 1,230,000.00 USD | 1,080,000.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 14,780,000.00 USD | 185,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2066.10` | 643,870,000.00 USD | 643,870,000.00 USD | 387,410.00 USD | 42,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2067.70` | 978,390,000.00 USD | 978,390,000.00 USD | 292,400.00 USD | 1,180,000.00 USD | 927,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2068.60` | 643,440,000.00 USD | 643,440,000.00 USD | 57,300.00 USD | 624,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.00` | 975,980,000.00 USD | 975,980,000.00 USD | 4,230,000.00 USD | 3,040,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2071.10` | 642,760,000.00 USD | 642,760,000.00 USD | 47,910.00 USD | 534,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.60` | 642,180,000.00 USD | 642,180,000.00 USD | 65,350.00 USD | 20,640.00 USD | 428,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.30` | 967,480,000.00 USD | 967,480,000.00 USD | 4,000,000.00 USD | 2,720,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 1,590,000.00 USD | 170,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2076.10` | 641,660,000.00 USD | 641,660,000.00 USD | 574,450.00 USD | 398,450.00 USD | 178,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2077.60` | 957,040,000.00 USD | 957,040,000.00 USD | 4,430,000.00 USD | 4,400,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2078.60` | 640,510,000.00 USD | 640,510,000.00 USD | 1,040,000.00 USD | 738,020.00 USD | 526,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2080.90` | 945,940,000.00 USD | 945,940,000.00 USD | 5,690,000.00 USD | 3,540,000.00 USD | 2,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2081.10` | 638,210,000.00 USD | 638,210,000.00 USD | 926,700.00 USD | 785,280.00 USD | 222,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2083.60` | 636,270,000.00 USD | 636,270,000.00 USD | 1,330,000.00 USD | 896,260.00 USD | 293,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.20` | 933,730,000.00 USD | 933,730,000.00 USD | 1,660,000.00 USD | 1,490,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 13,710,000.00 USD | 169,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2086.10` | 633,760,000.00 USD | 633,760,000.00 USD | 767,520.00 USD | 475,350.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2087.50` | 927,090,000.00 USD | 927,090,000.00 USD | 5,220,000.00 USD | 3,230,000.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2088.60` | 631,070,000.00 USD | 631,070,000.00 USD | 1,270,000.00 USD | 417,850.00 USD | 216,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2090.80` | 915,580,000.00 USD | 915,580,000.00 USD | 4,410,000.00 USD | 976,840.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2091.10` | 629,160,000.00 USD | 629,160,000.00 USD | 1,250,000.00 USD | 302,520.00 USD | 547,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2093.60` | 627,070,000.00 USD | 627,070,000.00 USD | 1,240,000.00 USD | 595,640.00 USD | 699,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.10` | 903,220,000.00 USD | 903,220,000.00 USD | 5,350,000.00 USD | 1,660,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,700,000.00 USD | 155,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2096.10` | 624,530,000.00 USD | 624,530,000.00 USD | 1,190,000.00 USD | 1,190,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.40` | 893,260,000.00 USD | 893,260,000.00 USD | 2,280,000.00 USD | 3,580,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2098.60` | 620,790,000.00 USD | 620,790,000.00 USD | 296,850.00 USD | 1,460,000.00 USD | 248,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2100.70` | 886,110,000.00 USD | 886,110,000.00 USD | 1,830,000.00 USD | 1,850,000.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2101.10` | 618,780,000.00 USD | 618,780,000.00 USD | 145,240.00 USD | 353,390.00 USD | 231,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2103.60` | 618,050,000.00 USD | 618,050,000.00 USD | 268,400.00 USD | 297,810.00 USD | 306,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2104.00` | 879,120,000.00 USD | 879,120,000.00 USD | 1,190,000.00 USD | 738,240.00 USD | 3,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 2,250,000.00 USD | 153,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2106.10` | 617,180,000.00 USD | 617,180,000.00 USD | 3,610,000.00 USD | 980,320.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.30` | 874,160,000.00 USD | 874,160,000.00 USD | 8,720,000.00 USD | 1,150,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2108.60` | 611,410,000.00 USD | 611,410,000.00 USD | 656,240.00 USD | 21,400.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2110.60` | 863,100,000.00 USD | 863,100,000.00 USD | 2,970,000.00 USD | 2,360,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2111.10` | 610,730,000.00 USD | 610,730,000.00 USD | 450,470.00 USD | 81,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2113.60` | 610,200,000.00 USD | 610,200,000.00 USD | 452,130.00 USD | 520,660.00 USD | 249,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2113.90` | 855,240,000.00 USD | 855,240,000.00 USD | 1,780,000.00 USD | 1,810,000.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,830,000.00 USD | 151,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2116.10` | 608,980,000.00 USD | 608,980,000.00 USD | 1,130,000.00 USD | 1,180,000.00 USD | 935,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.20` | 848,060,000.00 USD | 848,060,000.00 USD | 2,410,000.00 USD | 2,380,000.00 USD | 2,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2118.60` | 605,730,000.00 USD | 605,730,000.00 USD | 5,240,000.00 USD | 3,070,000.00 USD | 888,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2120.50` | 840,800,000.00 USD | 840,800,000.00 USD | 13,880,000.00 USD | 5,790,000.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2121.10` | 596,530,000.00 USD | 596,530,000.00 USD | 4,600,000.00 USD | 2,330,000.00 USD | 920,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.60` | 588,670,000.00 USD | 588,670,000.00 USD | 8,080,000.00 USD | 2,950,000.00 USD | 2,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2123.80` | 818,330,000.00 USD | 818,330,000.00 USD | 7,610,000.00 USD | 7,900,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,520,000.00 USD | 149,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2126.10` | 575,340,000.00 USD | 575,340,000.00 USD | 3,480,000.00 USD | 2,840,000.00 USD | 837,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.10` | 801,000,000.00 USD | 801,000,000.00 USD | 2,760,000.00 USD | 4,420,000.00 USD | 5,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.60` | 568,180,000.00 USD | 568,180,000.00 USD | 3,180,000.00 USD | 1,860,000.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.40` | 788,280,000.00 USD | 788,280,000.00 USD | 5,410,000.00 USD | 2,580,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2131.10` | 561,620,000.00 USD | 561,620,000.00 USD | 296,080.00 USD | 196,420.00 USD | 344,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2133.60` | 560,790,000.00 USD | 560,790,000.00 USD | 20,600.00 USD | 460,010.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2133.70` | 778,600,000.00 USD | 778,600,000.00 USD | 2,550,000.00 USD | 715,940.00 USD | 323,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 4,970,000.00 USD | 26,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2136.10` | 559,020,000.00 USD | 559,020,000.00 USD | 21,090.00 USD | 958,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.00` | 775,010,000.00 USD | 775,010,000.00 USD | 746,340.00 USD | 1,510,000.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2138.60` | 558,040,000.00 USD | 558,040,000.00 USD | 36,740.00 USD | 142,010.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.30` | 772,710,000.00 USD | 772,710,000.00 USD | 2,260,000.00 USD | 1,200,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2141.10` | 557,800,000.00 USD | 557,800,000.00 USD | 130,510.00 USD | 830,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2143.60` | 556,840,000.00 USD | 556,840,000.00 USD | 539,840.00 USD | 2,100,000.00 USD | 17,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2143.60` | 768,440,000.00 USD | 768,440,000.00 USD | 1,200,000.00 USD | 1,420,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 4,040,000.00 USD | 21,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2146.10` | 554,180,000.00 USD | 554,180,000.00 USD | 1,360,000.00 USD | 1,750,000.00 USD | 124,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2146.90` | 765,560,000.00 USD | 765,560,000.00 USD | 1,060,000.00 USD | 938,520.00 USD | 134,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2148.60` | 550,950,000.00 USD | 550,950,000.00 USD | 6,260,000.00 USD | 1,490,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.20` | 763,420,000.00 USD | 763,420,000.00 USD | 485,890.00 USD | 838,260.00 USD | 331,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2151.10` | 541,840,000.00 USD | 541,840,000.00 USD | 3,200,000.00 USD | 2,580,000.00 USD | 359,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2153.50` | 761,770,000.00 USD | 761,770,000.00 USD | 11,310,000.00 USD | 311,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2153.60` | 535,710,000.00 USD | 535,710,000.00 USD | 830,850.00 USD | 2,460,000.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 4,230,000.00 USD | 17,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2156.10` | 530,410,000.00 USD | 530,410,000.00 USD | 3,780,000.00 USD | 2,720,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2156.80` | 750,150,000.00 USD | 750,150,000.00 USD | 2,560,000.00 USD | 2,010,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2158.60` | 521,570,000.00 USD | 521,570,000.00 USD | 774,060.00 USD | 1,020,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.10` | 742,370,000.00 USD | 742,370,000.00 USD | 2,190,000.00 USD | 2,550,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2161.10` | 517,540,000.00 USD | 517,540,000.00 USD | 6,010,000.00 USD | 7,640,000.00 USD | 549,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.40` | 736,370,000.00 USD | 736,370,000.00 USD | 21,210,000.00 USD | 11,130,000.00 USD | 518,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2163.60` | 503,340,000.00 USD | 503,340,000.00 USD | 12,520,000.00 USD | 8,970,000.00 USD | 3,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 5,990,000.00 USD | 12,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2166.10` | 478,840,000.00 USD | 478,840,000.00 USD | 11,060,000.00 USD | 12,030,000.00 USD | 5,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2166.70` | 703,510,000.00 USD | 703,510,000.00 USD | 5,300,000.00 USD | 15,400,000.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2168.60` | 450,010,000.00 USD | 450,010,000.00 USD | 17,790,000.00 USD | 6,160,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.00` | 679,840,000.00 USD | 679,840,000.00 USD | 10,280,000.00 USD | 15,310,000.00 USD | 5,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2171.10` | 422,310,000.00 USD | 422,310,000.00 USD | 21,940,000.00 USD | 10,800,000.00 USD | 6,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.30` | 648,760,000.00 USD | 648,760,000.00 USD | 30,550,000.00 USD | 828,350.00 USD | 5,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2173.60` | 383,280,000.00 USD | 383,280,000.00 USD | 8,030,000.00 USD | 1,390,000.00 USD | 3,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 5,790,000.00 USD | 6,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2176.10` | 370,050,000.00 USD | 370,050,000.00 USD | 1,660,000.00 USD | 355,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2176.60` | 611,830,000.00 USD | 611,830,000.00 USD | 5,390,000.00 USD | 1,330,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2178.60` | 368,040,000.00 USD | 368,040,000.00 USD | 771,300.00 USD | 94,350.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2181.10` | 364,350,000.00 USD | 364,350,000.00 USD | 853,380.00 USD | 1,360,000.00 USD | 4,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2183.20` | 602,290,000.00 USD | 602,290,000.00 USD | 1,760,000.00 USD | 0.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2183.60` | 358,090,000.00 USD | 358,090,000.00 USD | 73,470.00 USD | 54,020.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 800,690.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2186.10` | 356,700,000.00 USD | 356,700,000.00 USD | 310,640.00 USD | 1,630,000.00 USD | 4,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2186.50` | 596,590,000.00 USD | 596,590,000.00 USD | 37,310,000.00 USD | 19,060,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2188.60` | 350,540,000.00 USD | 350,540,000.00 USD | 3,960,000.00 USD | 3,040,000.00 USD | 6,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2189.80` | 540,230,000.00 USD | 540,230,000.00 USD | 12,430,000.00 USD | 19,940,000.00 USD | 4,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2191.10` | 337,370,000.00 USD | 337,370,000.00 USD | 5,610,000.00 USD | 3,650,000.00 USD | 3,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2193.10` | 503,290,000.00 USD | 503,290,000.00 USD | 0.00 USD | 14,900,000.00 USD | 8,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2193.60` | 324,580,000.00 USD | 324,580,000.00 USD | 5,070,000.00 USD | 4,430,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 152,660.00 USD | 292,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2196.10` | 314,070,000.00 USD | 314,070,000.00 USD | 8,490,000.00 USD | 745,290.00 USD | 2,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.40` | 480,300,000.00 USD | 480,300,000.00 USD | 383,690.00 USD | 243,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2198.60` | 301,850,000.00 USD | 301,850,000.00 USD | 0.00 USD | 3,190,000.00 USD | 9,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2199.70` | 479,670,000.00 USD | 479,670,000.00 USD | 0.00 USD | 0.00 USD | 7,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2201.10` | 289,310,000.00 USD | 289,310,000.00 USD | 7,230,000.00 USD | 2,000,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.00` | 472,230,000.00 USD | 472,230,000.00 USD | 4,310,000.00 USD | 0.00 USD | 5,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.60` | 276,020,000.00 USD | 276,020,000.00 USD | 821,280.00 USD | 3,500,000.00 USD | 128,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 140,270.00 USD | 140,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2206.10` | 271,570,000.00 USD | 271,570,000.00 USD | 146,940.00 USD | 1,570,000.00 USD | 553,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2206.30` | 462,270,000.00 USD | 462,270,000.00 USD | 1,490,000.00 USD | 588,950.00 USD | 4,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2208.60` | 269,300,000.00 USD | 269,300,000.00 USD | 0.00 USD | 2,800,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2209.60` | 455,550,000.00 USD | 455,550,000.00 USD | 0.00 USD | 0.00 USD | 9,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2211.10` | 266,500,000.00 USD | 266,500,000.00 USD | 104,760.00 USD | 3,410,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2212.90` | 446,400,000.00 USD | 446,400,000.00 USD | 1,710,000.00 USD | 1,060,000.00 USD | 4,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2213.60` | 262,980,000.00 USD | 262,980,000.00 USD | 5,680,000.00 USD | 4,750,000.00 USD | 63,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2216.10` | 252,480,000.00 USD | 252,480,000.00 USD | 272,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2216.20` | 439,530,000.00 USD | 439,530,000.00 USD | 0.00 USD | 0.00 USD | 495,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2218.60` | 252,210,000.00 USD | 252,210,000.00 USD | 7,370,000.00 USD | 1,490,000.00 USD | 64,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2219.50` | 439,030,000.00 USD | 439,030,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 3,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2221.10` | 243,290,000.00 USD | 243,290,000.00 USD | 932,330.00 USD | 5,240,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2222.80` | 412,450,000.00 USD | 412,450,000.00 USD | 815,570.00 USD | 12,070,000.00 USD | 17,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2223.60` | 233,650,000.00 USD | 233,650,000.00 USD | 16,290,000.00 USD | 3,630,000.00 USD | 7,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2226.10` | 205,830,000.00 USD | 205,830,000.00 USD | 9,900,000.00 USD | 6,070,000.00 USD | 2,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2226.10` | 381,870,000.00 USD | 381,870,000.00 USD | 9,390,000.00 USD | 15,470,000.00 USD | 18,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2228.60` | 187,090,000.00 USD | 187,090,000.00 USD | 20,450,000.00 USD | 13,090,000.00 USD | 4,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.40` | 338,760,000.00 USD | 338,760,000.00 USD | 47,950,000.00 USD | 33,560,000.00 USD | 21,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2231.10` | 149,210,000.00 USD | 149,210,000.00 USD | 40,890,000.00 USD | 6,600,000.00 USD | 12,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2232.70` | 236,220,000.00 USD | 236,220,000.00 USD | 24,580,000.00 USD | 46,390,000.00 USD | 28,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2233.60` | 88,960,000.00 USD | 88,960,000.00 USD | 30,060,000.00 USD | 0.00 USD | 21,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2236.00` | 137,250,000.00 USD | 137,250,000.00 USD | 30,150,000.00 USD | 23,260,000.00 USD | 26,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2236.10` | 37,250,000.00 USD | 37,250,000.00 USD | 0.00 USD | 0.00 USD | 14,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2238.60` | 23,040,000.00 USD | 23,040,000.00 USD | 15,220,000.00 USD | 0.00 USD | 2,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.30` | 57,360,000.00 USD | 57,360,000.00 USD | 39,050,000.00 USD | 0.00 USD | 8,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2241.10` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2242.60` | 9,970,000.00 USD | 9,970,000.00 USD | 6,760,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2243.60` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 141,810.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2245.00` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2245.90` | 3,210,000.00 USD | 3,210,000.00 USD | 2,070,000.00 USD | 1,030,000.00 USD | 102,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2246.10` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 1,650,000.00 USD | 45,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2248.60` | 3,210,000.00 USD | 3,210,000.00 USD | 1,860,000.00 USD | 0.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2249.20` | 7,260,000.00 USD | 7,260,000.00 USD | 3,350,000.00 USD | 2,660,000.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2251.10` | 15,190,000.00 USD | 15,190,000.00 USD | 10,500,000.00 USD | 221,820.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2252.50` | 37,060,000.00 USD | 37,060,000.00 USD | 20,930,000.00 USD | 8,880,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2253.60` | 29,760,000.00 USD | 29,760,000.00 USD | 8,730,000.00 USD | 4,050,000.00 USD | 1,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 202,140.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2255.80` | 55,100,000.00 USD | 55,100,000.00 USD | 7,010,000.00 USD | 10,520,000.00 USD | 514,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2256.10` | 56,370,000.00 USD | 56,370,000.00 USD | 15,350,000.00 USD | 8,100,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2258.60` | 79,550,000.00 USD | 79,550,000.00 USD | 12,840,000.00 USD | 8,430,000.00 USD | 1,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2259.10` | 85,400,000.00 USD | 85,400,000.00 USD | 18,800,000.00 USD | 7,450,000.00 USD | 4,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2261.10` | 93,590,000.00 USD | 93,590,000.00 USD | 8,030,000.00 USD | 4,330,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2262.40` | 93,780,000.00 USD | 93,780,000.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 210,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2263.60` | 119,070,000.00 USD | 119,070,000.00 USD | 10,590,000.00 USD | 8,540,000.00 USD | 6,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 4,500,000.00 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2265.70` | 100,110,000.00 USD | 100,110,000.00 USD | 0.00 USD | 0.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2266.10` | 141,460,000.00 USD | 141,460,000.00 USD | 4,250,000.00 USD | 10,210,000.00 USD | 7,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2268.60` | 171,310,000.00 USD | 171,310,000.00 USD | 13,820,000.00 USD | 7,980,000.00 USD | 8,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2269.00` | 119,040,000.00 USD | 119,040,000.00 USD | 8,610,000.00 USD | 5,650,000.00 USD | 4,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2271.10` | 177,430,000.00 USD | 177,430,000.00 USD | 1,520,000.00 USD | 1,310,000.00 USD | 3,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2272.30` | 128,070,000.00 USD | 128,070,000.00 USD | 7,540,000.00 USD | 1,480,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2273.60` | 183,110,000.00 USD | 183,110,000.00 USD | 395,550.00 USD | 4,190,000.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 79,460.00 USD | 6,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2275.60` | 133,560,000.00 USD | 133,560,000.00 USD | 0.00 USD | 5,500,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2276.10` | 218,340,000.00 USD | 218,340,000.00 USD | 16,020,000.00 USD | 14,780,000.00 USD | 4,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2278.60` | 232,070,000.00 USD | 232,070,000.00 USD | 0.00 USD | 7,190,000.00 USD | 6,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2278.90` | 157,510,000.00 USD | 157,510,000.00 USD | 854,200.00 USD | 12,550,000.00 USD | 10,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2281.10` | 297,580,000.00 USD | 297,580,000.00 USD | 32,540,000.00 USD | 25,110,000.00 USD | 7,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.20` | 255,060,000.00 USD | 255,060,000.00 USD | 0.00 USD | 83,870,000.00 USD | 13,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2283.60` | 354,830,000.00 USD | 354,830,000.00 USD | 29,580,000.00 USD | 15,340,000.00 USD | 12,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 167,510.00 USD | 6,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2285.50` | 288,720,000.00 USD | 288,720,000.00 USD | 6,610,000.00 USD | 26,950,000.00 USD | 105,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2286.10` | 376,960,000.00 USD | 376,960,000.00 USD | 4,320,000.00 USD | 11,590,000.00 USD | 6,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2288.60` | 400,740,000.00 USD | 400,740,000.00 USD | 12,530,000.00 USD | 8,240,000.00 USD | 3,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2288.80` | 320,170,000.00 USD | 320,170,000.00 USD | 8,380,000.00 USD | 8,140,000.00 USD | 14,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2291.10` | 434,490,000.00 USD | 434,490,000.00 USD | 17,120,000.00 USD | 10,130,000.00 USD | 6,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2292.10` | 331,560,000.00 USD | 331,560,000.00 USD | 7,890,000.00 USD | 517,070.00 USD | 2,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2293.60` | 457,790,000.00 USD | 457,790,000.00 USD | 11,320,000.00 USD | 4,560,000.00 USD | 7,420,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 2,440,000.00 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2295.40` | 368,030,000.00 USD | 368,030,000.00 USD | 22,930,000.00 USD | 6,820,000.00 USD | 6,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2296.10` | 478,560,000.00 USD | 478,560,000.00 USD | 4,070,000.00 USD | 13,690,000.00 USD | 3,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2298.60` | 526,740,000.00 USD | 526,740,000.00 USD | 26,500,000.00 USD | 14,510,000.00 USD | 7,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2298.70` | 390,870,000.00 USD | 390,870,000.00 USD | 897,290.00 USD | 11,270,000.00 USD | 10,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2301.10` | 553,800,000.00 USD | 553,800,000.00 USD | 7,640,000.00 USD | 7,330,000.00 USD | 12,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.00` | 466,190,000.00 USD | 466,190,000.00 USD | 29,960,000.00 USD | 23,280,000.00 USD | 22,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2303.60` | 588,500,000.00 USD | 588,500,000.00 USD | 17,880,000.00 USD | 10,150,000.00 USD | 6,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 158,470.00 USD | 9,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2305.30` | 501,350,000.00 USD | 501,350,000.00 USD | 17,280,000.00 USD | 6,960,000.00 USD | 10,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2306.10` | 626,730,000.00 USD | 626,730,000.00 USD | 16,140,000.00 USD | 12,830,000.00 USD | 9,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2308.60` | 630,610,000.00 USD | 630,610,000.00 USD | 423,370.00 USD | 3,270,000.00 USD | 182,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2308.60` | 505,600,000.00 USD | 505,600,000.00 USD | 1,240,000.00 USD | 2,780,000.00 USD | 231,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2311.10` | 647,880,000.00 USD | 647,880,000.00 USD | 5,900,000.00 USD | 813,020.00 USD | 10,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2311.90` | 535,840,000.00 USD | 535,840,000.00 USD | 11,460,000.00 USD | 2,650,000.00 USD | 16,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2313.60` | 660,980,000.00 USD | 660,980,000.00 USD | 4,690,000.00 USD | 7,240,000.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 1,160,000.00 USD | 10,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2315.20` | 544,590,000.00 USD | 544,590,000.00 USD | 0.00 USD | 8,120,000.00 USD | 627,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2316.10` | 694,120,000.00 USD | 694,120,000.00 USD | 9,820,000.00 USD | 16,730,000.00 USD | 6,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2318.50` | 559,510,000.00 USD | 559,510,000.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 5,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2318.60` | 706,110,000.00 USD | 706,110,000.00 USD | 4,440,000.00 USD | 5,330,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2321.10` | 729,100,000.00 USD | 729,100,000.00 USD | 6,390,000.00 USD | 14,670,000.00 USD | 1,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2321.80` | 579,250,000.00 USD | 579,250,000.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2323.60` | 740,300,000.00 USD | 740,300,000.00 USD | 1,250,000.00 USD | 6,360,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,790,000.00 USD | 12,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.10` | 600,330,000.00 USD | 600,330,000.00 USD | 10,150,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2326.10` | 754,830,000.00 USD | 754,830,000.00 USD | 1,830,000.00 USD | 6,990,000.00 USD | 5,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.40` | 612,330,000.00 USD | 612,330,000.00 USD | 3,860,000.00 USD | 121,880.00 USD | 8,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2328.60` | 758,700,000.00 USD | 758,700,000.00 USD | 3,080,000.00 USD | 524,360.00 USD | 261,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2331.10` | 782,680,000.00 USD | 782,680,000.00 USD | 19,380,000.00 USD | 3,300,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2331.70` | 641,800,000.00 USD | 641,800,000.00 USD | 29,230,000.00 USD | 241,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2333.60` | 801,100,000.00 USD | 801,100,000.00 USD | 5,160,000.00 USD | 4,720,000.00 USD | 8,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2335.00` | 694,070,000.00 USD | 694,070,000.00 USD | 20,390,000.00 USD | 19,830,000.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 1,390,000.00 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2336.10` | 821,930,000.00 USD | 821,930,000.00 USD | 14,690,000.00 USD | 1,960,000.00 USD | 4,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.30` | 725,800,000.00 USD | 725,800,000.00 USD | 22,110,000.00 USD | 0.00 USD | 9,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2338.60` | 836,980,000.00 USD | 836,980,000.00 USD | 8,670,000.00 USD | 2,930,000.00 USD | 3,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2341.10` | 858,340,000.00 USD | 858,340,000.00 USD | 7,140,000.00 USD | 4,080,000.00 USD | 10,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2341.60` | 762,330,000.00 USD | 762,330,000.00 USD | 4,720,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2343.60` | 875,500,000.00 USD | 875,500,000.00 USD | 4,110,000.00 USD | 7,890,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2344.90` | 789,170,000.00 USD | 789,170,000.00 USD | 1,350,000.00 USD | 16,920,000.00 USD | 8,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 416,450.00 USD | 14,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2346.10` | 887,630,000.00 USD | 887,630,000.00 USD | 3,680,000.00 USD | 3,010,000.00 USD | 5,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.20` | 825,300,000.00 USD | 825,300,000.00 USD | 561,950.00 USD | 12,390,000.00 USD | 23,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2348.60` | 905,740,000.00 USD | 905,740,000.00 USD | 8,700,000.00 USD | 6,650,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2351.10` | 946,300,000.00 USD | 946,300,000.00 USD | 24,430,000.00 USD | 4,950,000.00 USD | 11,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2351.50` | 863,960,000.00 USD | 863,960,000.00 USD | 2,930,000.00 USD | 20,680,000.00 USD | 15,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2353.60` | 957,330,000.00 USD | 957,330,000.00 USD | 3,230,000.00 USD | 7,140,000.00 USD | 652,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2354.80` | 920,810,000.00 USD | 920,810,000.00 USD | 17,130,000.00 USD | 38,220,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,230,000.00 USD | 15,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2356.10` | 972,610,000.00 USD | 972,610,000.00 USD | 5,940,000.00 USD | 6,670,000.00 USD | 2,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.10` | 937,970,000.00 USD | 937,970,000.00 USD | 7,110,000.00 USD | 4,040,000.00 USD | 6,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2358.60` | 990,110,000.00 USD | 990,110,000.00 USD | 4,520,000.00 USD | 5,630,000.00 USD | 7,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2361.10` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 8,670,000.00 USD | 4,820,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.40` | 946,240,000.00 USD | 946,240,000.00 USD | 4,470,000.00 USD | 3,430,000.00 USD | 374,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2363.60` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 5,260,000.00 USD | 6,820,000.00 USD | 8,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2364.70` | 962,110,000.00 USD | 962,110,000.00 USD | 4,570,000.00 USD | 373,740.00 USD | 10,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 4,040,000.00 USD | 19,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2366.10` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 4,830,000.00 USD | 827,140.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.00` | 975,950,000.00 USD | 975,950,000.00 USD | 11,660,000.00 USD | 1,780,000.00 USD | 396,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2368.60` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 7,050,000.00 USD | 4,420,000.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2371.10` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 14,820,000.00 USD | 6,060,000.00 USD | 6,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.30` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 25,000,000.00 USD | 0.00 USD | 54,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2373.60` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 13,760,000.00 USD | 1,630,000.00 USD | 5,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2374.60` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 19,920,000.00 USD | 121,480.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 5,640,000.00 USD | 25,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2376.10` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 5,860,000.00 USD | 4,290,000.00 USD | 4,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2377.90` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 11,180,000.00 USD | 6,190,000.00 USD | 29,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.60` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 1,650,000.00 USD | 2,490,000.00 USD | 3,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2381.10` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 10,120,000.00 USD | 7,600,000.00 USD | 10,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.20` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 4,540,000.00 USD | 4,150,000.00 USD | 19,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 12,240,000.00 USD | 8,580,000.00 USD | 5,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2384.50` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 22,580,000.00 USD | 22,660,000.00 USD | 45,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 1,180,000.00 USD | 26,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2386.10` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 10,140,000.00 USD | 10,450,000.00 USD | 4,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2387.80` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 5,540,000.00 USD | 49,830,000.00 USD | 47,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2388.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 9,760,000.00 USD | 6,510,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2391.10` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 1,410,000.00 USD | 4,340,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.10` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 5,910,000.00 USD | 52,770,000.00 USD | 41,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2393.60` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 2,570,000.00 USD | 3,590,000.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.40` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 60,000,000.00 USD | 32,420,000.00 USD | 40,070,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 17,990.00 USD | 26,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2396.10` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 2,220,000.00 USD | 331,850.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2397.70` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 31,080,000.00 USD | 41,130,000.00 USD | 26,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.60` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 1,760,000.00 USD | 4,590,000.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.00` | 1,790,000,000.00 USD | 1,790,000,000.00 USD | 51,130,000.00 USD | 28,060,000.00 USD | 25,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2401.10` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 4,570,000.00 USD | 3,010,000.00 USD | 2,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2403.60` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 5,500,000.00 USD | 3,040,000.00 USD | 2,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.30` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 61,130,000.00 USD | 29,350,000.00 USD | 31,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 190,150.00 USD | 26,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2406.10` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 10,520,000.00 USD | 5,000,000.00 USD | 5,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2407.60` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 29,050,000.00 USD | 35,150,000.00 USD | 19,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2408.60` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 4,880,000.00 USD | 6,000,000.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2410.90` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 25,670,000.00 USD | 27,460,000.00 USD | 31,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2411.10` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 7,010,000.00 USD | 5,090,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.60` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 4,430,000.00 USD | 3,130,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.20` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 21,950,000.00 USD | 25,190,000.00 USD | 22,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 220,420.00 USD | 26,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2416.10` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 3,760,000.00 USD | 2,230,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2417.50` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 31,300,000.00 USD | 11,500,000.00 USD | 24,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2418.60` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 3,250,000.00 USD | 1,840,000.00 USD | 1,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2420.80` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 32,960,000.00 USD | 25,400,000.00 USD | 14,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2421.10` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 6,230,000.00 USD | 5,070,000.00 USD | 4,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2423.60` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 908,650.00 USD | 2,650,000.00 USD | 2,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.10` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 20,380,000.00 USD | 29,890,000.00 USD | 23,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 69,910.00 USD | 26,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2426.10` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 1,470,000.00 USD | 1,010,000.00 USD | 40,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.40` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 22,390,000.00 USD | 17,570,000.00 USD | 20,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.60` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 1,290,000.00 USD | 1,450,000.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2430.70` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 8,890,000.00 USD | 15,370,000.00 USD | 9,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2431.10` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 3,120,000.00 USD | 2,370,000.00 USD | 677,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2433.60` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 1,770,000.00 USD | 1,450,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.00` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 19,530,000.00 USD | 9,570,000.00 USD | 13,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 1,310,000.00 USD | 28,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2436.10` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 2,490,000.00 USD | 1,070,000.00 USD | 161,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 15,680,000.00 USD | 15,080,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2438.60` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 476,020.00 USD | 535,870.00 USD | 15,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2440.60` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 16,940,000.00 USD | 10,790,000.00 USD | 9,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2441.10` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 2,260,000.00 USD | 723,100.00 USD | 858,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2443.60` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 412,840.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2443.90` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 5,830,000.00 USD | 12,110,000.00 USD | 6,990,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 40,510.00 USD | 28,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2446.10` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 472,100.00 USD | 360,870.00 USD | 10,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.20` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 13,820,000.00 USD | 7,510,000.00 USD | 16,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2448.60` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 321,220.00 USD | 198,200.00 USD | 687,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2450.50` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 10,570,000.00 USD | 11,560,000.00 USD | 10,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2451.10` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 1,380,000.00 USD | 1,300,000.00 USD | 709,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2453.60` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 3,640,000.00 USD | 1,900,000.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2453.80` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 7,240,000.00 USD | 4,290,000.00 USD | 6,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 54,300,000.00 USD | 82,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2456.10` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 622,030.00 USD | 1,890,000.00 USD | 797,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.10` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 8,340,000.00 USD | 8,890,000.00 USD | 7,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2458.60` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 1,660,000.00 USD | 1,430,000.00 USD | 9,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.40` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 7,080,000.00 USD | 8,140,000.00 USD | 9,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2461.10` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 515,180.00 USD | 242,570.00 USD | 375,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2463.60` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 330,880.00 USD | 940,830.00 USD | 829,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2463.70` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 9,430,000.00 USD | 8,280,000.00 USD | 6,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 11,530,000.00 USD | 94,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2466.10` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 448,360.00 USD | 872,060.00 USD | 550,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.00` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 4,840,000.00 USD | 2,920,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2468.60` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 288,920.00 USD | 1,680,000.00 USD | 558,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.30` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 3,190,000.00 USD | 3,080,000.00 USD | 496,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2471.10` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 973,110.00 USD | 199,120.00 USD | 798,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2473.60` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 0.00 USD | 316,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2473.60` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 5,860,000.00 USD | 2,920,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 249,030.00 USD | 94,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2476.10` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 1,100,000.00 USD | 28,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2476.90` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 2,660,000.00 USD | 2,410,000.00 USD | 872,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2478.60` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 1,430,000.00 USD | 933,460.00 USD | 302,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.20` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 1,580,000.00 USD | 6,190,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2481.10` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 229,630.00 USD | 611,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2482.40` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 437,940.00 USD | 156,850.00 USD | 707,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2483.50` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 1,750,000.00 USD | 2,280,000.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 63,020.00 USD | 94,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2486.80` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 30,880.00 USD | 0.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.10` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 1,480,000.00 USD | 1,010,000.00 USD | 167,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.40` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 3,210,000.00 USD | 1,830,000.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 2,080,000.00 USD | 96,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2496.70` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 1,370,000.00 USD | 3,690,000.00 USD | 4,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.00` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 358,770.00 USD | 1,980,000.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.30` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 27,220.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 16,160,000.00 USD | 112,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2506.60` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 2,540,000.00 USD | 903,900.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2509.90` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 2,290,000.00 USD | 2,160,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 148,280.00 USD | 112,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2516.50` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2519.80` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.10` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 77,380.00 USD | 112,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2526.40` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 292,400.00 USD | 1,090,000.00 USD | 200,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2529.70` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 1,510,000.00 USD | 2,770,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.00` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 4,460,000.00 USD | 1,850,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 961,350.00 USD | 113,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2536.30` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 3,170,000.00 USD | 2,460,000.00 USD | 4,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2539.60` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 4,190,000.00 USD | 3,730,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2542.90` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 4,070,000.00 USD | 2,950,000.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 12,650.00 USD | 113,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2546.20` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 1,900,000.00 USD | 1,140,000.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2549.50` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 4,150,000.00 USD | 3,470,000.00 USD | 4,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2552.80` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 1,920,000.00 USD | 580,780.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 197,130.00 USD | 114,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2556.10` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 4,340,000.00 USD | 549,010.00 USD | 7,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.40` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 5,200,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2562.70` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 1,940,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 60,800.00 USD | 114,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2566.00` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 1,880,000.00 USD | 1,520,000.00 USD | 2,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.30` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 125,250.00 USD | 739,480.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2572.60` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 2,000,000.00 USD | 890,480.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 50,100.00 USD | 114,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2575.90` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 2,180,000.00 USD | 440,740.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2579.20` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 1,870,000.00 USD | 1,940,000.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2582.50` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 2,830,000.00 USD | 1,030,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,510,000.00 USD | 140,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2585.80` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 883,660.00 USD | 2,700,000.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.10` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 2,540,000.00 USD | 536,380.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2590.30` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 1,180,000.00 USD | 304,000.00 USD | 447,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 13,590,000.00 USD | 154,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2605.00` | 6,080,000.00 USD | 160,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2615.00` | 707,260.00 USD | 161,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2625.00` | 40,190,000.00 USD | 201,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2635.00` | 1,540,000.00 USD | 202,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 1,070,000.00 USD | 203,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 26,090,000.00 USD | 229,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 55,570.00 USD | 230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 10,520,000.00 USD | 240,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 26,860.00 USD | 240,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 185,300.00 USD | 240,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 525,220.00 USD | 241,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 131,390.00 USD | 241,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 707,680.00 USD | 242,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 20,100.00 USD | 242,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 886,230.00 USD | 243,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 5,790,000.00 USD | 248,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 5,540,000.00 USD | 254,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 13,310,000.00 USD | 267,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 29,890.00 USD | 267,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 16,710,000.00 USD | 284,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 4,370,000.00 USD | 288,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 1,160,000.00 USD | 289,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 666,320.00 USD | 290,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 6,070,000.00 USD | 296,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 533,510.00 USD | 297,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 127,560.00 USD | 297,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 331,830.00 USD | 297,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 119,980.00 USD | 297,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 1,280,000.00 USD | 299,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 1,640,000.00 USD | 300,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 27,600,000.00 USD | 328,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 2,330,000.00 USD | 330,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 148,030.00 USD | 330,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 32,590.00 USD | 330,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 721,780.00 USD | 331,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 309,780.00 USD | 331,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 3,770,000.00 USD | 335,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 52,160.00 USD | 335,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 703,430.00 USD | 336,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 1,590,000.00 USD | 337,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 20,760,000.00 USD | 358,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 3,060,000.00 USD | 361,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 822,110.00 USD | 362,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 12,820,000.00 USD | 375,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 1,510,000.00 USD | 376,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 640,770.00 USD | 377,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 13,620.00 USD | 377,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 5,430,000.00 USD | 382,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 32,360.00 USD | 383,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 678,510.00 USD | 383,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 3,740,000.00 USD | 387,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 150,800.00 USD | 387,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 126,640.00 USD | 387,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 6,420,000.00 USD | 394,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 29,710,000.00 USD | 423,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 4,960,000.00 USD | 428,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 151,290.00 USD | 428,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 681,290.00 USD | 429,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 6,860,000.00 USD | 436,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 3,660,000.00 USD | 440,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 141,980.00 USD | 440,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 173,450.00 USD | 440,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 9,800,000.00 USD | 450,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 9,910,000.00 USD | 460,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 8,440,000.00 USD | 468,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 28,620.00 USD | 468,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 4,860,000.00 USD | 473,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 8,490,000.00 USD | 482,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 260,070.00 USD | 482,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 128,500.00 USD | 482,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 2,880,000.00 USD | 485,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 687,300.00 USD | 485,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 71,450.00 USD | 486,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 663,170.00 USD | 486,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 41,930.00 USD | 486,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 98,520.00 USD | 486,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 7,380,000.00 USD | 494,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 70,280.00 USD | 494,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 101,040.00 USD | 494,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 2,890,000.00 USD | 497,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 207,160.00 USD | 497,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 20,980.00 USD | 497,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 14,880,000.00 USD | 512,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 2,920,000.00 USD | 515,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 300,130.00 USD | 515,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 1,090,000.00 USD | 516,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 85,780.00 USD | 516,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 58,020,000.00 USD | 574,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 466,100.00 USD | 575,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 2,950,000.00 USD | 578,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 269,580.00 USD | 578,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 11,740.00 USD | 578,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 103,940.00 USD | 578,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 255,300.00 USD | 578,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 14,280,000.00 USD | 593,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 31,660,000.00 USD | 624,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 61,200.00 USD | 624,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 100,020.00 USD | 624,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 942,290.00 USD | 625,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 108,260.00 USD | 626,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 53,170.00 USD | 626,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 4,100,000.00 USD | 630,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 675,620.00 USD | 630,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 10,370,000.00 USD | 641,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 6,300.00 USD | 641,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 6,490,000.00 USD | 647,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 1,100,000.00 USD | 648,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 2,700.00 USD | 648,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 335,730.00 USD | 649,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 55,280.00 USD | 649,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 16,530.00 USD | 649,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 116,670.00 USD | 649,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 483,880.00 USD | 649,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 523,550.00 USD | 650,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 997,440.00 USD | 651,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 263,400.00 USD | 651,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 1,990,000.00 USD | 653,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 275,200.00 USD | 653,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 405,370,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 17,510.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 5,810,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 2,150.00 USD | 1,070,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 10,200.00 USD | 1,070,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 2,120,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 1,780,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 93,210.00 USD | 1,070,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 36,210,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3875.00` | 130,230.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 3,300,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 2,490,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 1,210,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 63,500,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 227,870.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 5,330.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 2,300.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 9,170.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 704,760.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 164,680.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 1,340,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 659,290.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 117,770.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 71,130.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 193,370.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 90,590.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 94,540.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 2,040,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 258,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 118,270.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 7,110.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 487,730.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 2,140,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 3,300.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 651,180.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 813,500.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 1,260,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 203,830.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 373,370.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 886,910.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 85,130,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 4,080,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 28,630,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 46,920.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 5,290,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 168,620.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 36,710.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 62,090.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 132,310.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 2,340.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 4,510,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 165,270.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 82,370.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 279,930,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 533,120.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 14,440.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 7,030.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 1,010,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 72,940.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 216,340.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 20,260.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 40,640.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 45,440.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 8,480.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4435.00` | 107,760.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4445.00` | 106,870.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4455.00` | 110,070.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4465.00` | 29,380.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4475.00` | 424,260.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4485.00` | 322,780.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `455.00` | 758,550,000.00 USD | 0.00 USD | 70,210.00 USD | `-79.71%` | `154.31` |
| `Live` | `Long` | `465.00` | 758,480,000.00 USD | 0.00 USD | 39,370.00 USD | `-79.26%` | `84.66` |
| `Live` | `Long` | `475.00` | 758,440,000.00 USD | 0.00 USD | 105,690.00 USD | `-78.82%` | `222.51` |
| `Live` | `Long` | `485.00` | 758,330,000.00 USD | 0.00 USD | 5,010.00 USD | `-78.37%` | `10.34` |
| `Live` | `Long` | `495.00` | 758,330,000.00 USD | 0.00 USD | 1,870,000.00 USD | `-77.93%` | `3,770.54` |
| `Live` | `Long` | `505.00` | 756,460,000.00 USD | 0.00 USD | 21,630.00 USD | `-77.48%` | `42.82` |
| `Live` | `Long` | `515.00` | 756,440,000.00 USD | 0.00 USD | 131,890.00 USD | `-77.03%` | `256.10` |
| `Live` | `Long` | `525.00` | 756,310,000.00 USD | 0.00 USD | 2,050.00 USD | `-76.59%` | `3.91` |
| `Live` | `Long` | `535.00` | 756,310,000.00 USD | 0.00 USD | 10,240.00 USD | `-76.14%` | `19.13` |
| `Live` | `Long` | `545.00` | 756,300,000.00 USD | 0.00 USD | 13,990.00 USD | `-75.70%` | `25.68` |
| `Live` | `Long` | `555.00` | 756,280,000.00 USD | 0.00 USD | 252,780.00 USD | `-75.25%` | `455.46` |
| `Live` | `Long` | `565.00` | 756,030,000.00 USD | 0.00 USD | 1,760,000.00 USD | `-74.80%` | `3,112.27` |
| `Live` | `Long` | `575.00` | 754,270,000.00 USD | 0.00 USD | 44,530.00 USD | `-74.36%` | `77.44` |
| `Live` | `Long` | `585.00` | 754,230,000.00 USD | 0.00 USD | 2,860,000.00 USD | `-73.91%` | `4,891.16` |
| `Live` | `Long` | `595.00` | 751,360,000.00 USD | 0.00 USD | 447,610.00 USD | `-73.47%` | `752.28` |
| `Live` | `Long` | `605.00` | 750,920,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-73.02%` | `1,861.35` |
| `Live` | `Long` | `615.00` | 749,790,000.00 USD | 0.00 USD | 59,650.00 USD | `-72.58%` | `96.99` |
| `Live` | `Long` | `625.00` | 749,730,000.00 USD | 0.00 USD | 26,610.00 USD | `-72.13%` | `42.58` |
| `Live` | `Long` | `635.00` | 749,700,000.00 USD | 0.00 USD | 7,190.00 USD | `-71.68%` | `11.32` |
| `Live` | `Long` | `645.00` | 749,700,000.00 USD | 0.00 USD | 65,540.00 USD | `-71.24%` | `101.61` |
| `Live` | `Long` | `655.00` | 749,630,000.00 USD | 0.00 USD | 179,860.00 USD | `-70.79%` | `274.59` |
| `Live` | `Long` | `665.00` | 749,450,000.00 USD | 0.00 USD | 30,530.00 USD | `-70.35%` | `45.90` |
| `Live` | `Long` | `675.00` | 749,420,000.00 USD | 0.00 USD | 58,400.00 USD | `-69.90%` | `86.52` |
| `Live` | `Long` | `685.00` | 749,360,000.00 USD | 0.00 USD | 61,280.00 USD | `-69.45%` | `89.46` |
| `Live` | `Long` | `695.00` | 749,300,000.00 USD | 0.00 USD | 1,170,000.00 USD | `-69.01%` | `1,688.99` |
| `Live` | `Long` | `705.00` | 748,130,000.00 USD | 0.00 USD | 2,950.00 USD | `-68.56%` | `4.18` |
| `Live` | `Long` | `715.00` | 748,120,000.00 USD | 0.00 USD | 11,530.00 USD | `-68.12%` | `16.13` |
| `Live` | `Long` | `725.00` | 748,110,000.00 USD | 0.00 USD | 415,590.00 USD | `-67.67%` | `573.23` |
| `Live` | `Long` | `735.00` | 747,700,000.00 USD | 0.00 USD | 116,150.00 USD | `-67.22%` | `158.03` |
| `Live` | `Long` | `745.00` | 747,580,000.00 USD | 0.00 USD | 958.22 USD | `-66.78%` | `1.29` |
| `Live` | `Long` | `755.00` | 747,580,000.00 USD | 0.00 USD | 35,090.00 USD | `-66.33%` | `46.48` |
| `Live` | `Long` | `765.00` | 747,550,000.00 USD | 0.00 USD | 74,190.00 USD | `-65.89%` | `96.98` |
| `Live` | `Long` | `775.00` | 747,470,000.00 USD | 0.00 USD | 75,950.00 USD | `-65.44%` | `98.00` |
| `Live` | `Long` | `785.00` | 747,390,000.00 USD | 0.00 USD | 34,790.00 USD | `-64.99%` | `44.31` |
| `Live` | `Long` | `795.00` | 747,360,000.00 USD | 0.00 USD | 104,970.00 USD | `-64.55%` | `132.04` |
| `Live` | `Long` | `805.00` | 747,260,000.00 USD | 0.00 USD | 44,510.00 USD | `-64.10%` | `55.29` |
| `Live` | `Long` | `815.00` | 747,210,000.00 USD | 0.00 USD | 86,380.00 USD | `-63.66%` | `105.99` |
| `Live` | `Long` | `825.00` | 747,120,000.00 USD | 0.00 USD | 356,620.00 USD | `-63.21%` | `432.27` |
| `Live` | `Long` | `835.00` | 746,770,000.00 USD | 0.00 USD | 39,330.00 USD | `-62.76%` | `47.11` |
| `Live` | `Long` | `845.00` | 746,730,000.00 USD | 0.00 USD | 172,470.00 USD | `-62.32%` | `204.11` |
| `Live` | `Long` | `855.00` | 746,560,000.00 USD | 0.00 USD | 489,100.00 USD | `-61.87%` | `572.05` |
| `Live` | `Long` | `865.00` | 746,070,000.00 USD | 0.00 USD | 138,490.00 USD | `-61.43%` | `160.11` |
| `Live` | `Long` | `875.00` | 745,930,000.00 USD | 0.00 USD | 282,060.00 USD | `-60.98%` | `322.35` |
| `Live` | `Long` | `885.00` | 745,650,000.00 USD | 0.00 USD | 991,570.00 USD | `-60.54%` | `1,120.42` |
| `Live` | `Long` | `895.00` | 744,650,000.00 USD | 0.00 USD | 253,960.00 USD | `-60.09%` | `283.75` |
| `Live` | `Long` | `905.00` | 744,400,000.00 USD | 0.00 USD | 321,510.00 USD | `-59.64%` | `355.26` |
| `Live` | `Long` | `915.00` | 744,080,000.00 USD | 0.00 USD | 191,390.00 USD | `-59.20%` | `209.17` |
| `Live` | `Long` | `925.00` | 743,890,000.00 USD | 0.00 USD | 201,010.00 USD | `-58.75%` | `217.31` |
| `Live` | `Long` | `935.00` | 743,690,000.00 USD | 0.00 USD | 135,060.00 USD | `-58.31%` | `144.45` |
| `Live` | `Long` | `945.00` | 743,550,000.00 USD | 0.00 USD | 230,060.00 USD | `-57.86%` | `243.45` |
| `Live` | `Long` | `955.00` | 743,320,000.00 USD | 0.00 USD | 20,590.00 USD | `-57.41%` | `21.57` |
| `Live` | `Long` | `965.00` | 743,300,000.00 USD | 0.00 USD | 28,020.00 USD | `-56.97%` | `29.04` |
| `Live` | `Long` | `975.00` | 743,270,000.00 USD | 0.00 USD | 532,060.00 USD | `-56.52%` | `545.71` |
| `Live` | `Long` | `985.00` | 742,740,000.00 USD | 0.00 USD | 5,370,000.00 USD | `-56.08%` | `5,451.45` |
| `Live` | `Long` | `995.00` | 737,370,000.00 USD | 0.00 USD | 1,180,000.00 USD | `-55.63%` | `1,190.51` |
| `Live` | `Long` | `1005.00` | 736,190,000.00 USD | 0.00 USD | 161,470.00 USD | `-55.18%` | `160.67` |
| `Live` | `Long` | `1015.00` | 736,030,000.00 USD | 0.00 USD | 229,050.00 USD | `-54.74%` | `225.67` |
| `Live` | `Long` | `1025.00` | 735,800,000.00 USD | 0.00 USD | 160,140.00 USD | `-54.29%` | `156.24` |
| `Live` | `Long` | `1035.00` | 735,640,000.00 USD | 0.00 USD | 39,300.00 USD | `-53.85%` | `37.97` |
| `Live` | `Long` | `1045.00` | 735,600,000.00 USD | 0.00 USD | 925,460.00 USD | `-53.40%` | `885.61` |
| `Live` | `Long` | `1055.00` | 734,670,000.00 USD | 0.00 USD | 7,410,000.00 USD | `-52.95%` | `7,026.85` |
| `Live` | `Long` | `1065.00` | 727,260,000.00 USD | 0.00 USD | 1,540,000.00 USD | `-52.51%` | `1,447.94` |
| `Live` | `Long` | `1075.00` | 725,720,000.00 USD | 0.00 USD | 753,780.00 USD | `-52.06%` | `701.19` |
| `Live` | `Long` | `1085.00` | 724,960,000.00 USD | 0.00 USD | 328,160.00 USD | `-51.62%` | `302.45` |
| `Live` | `Long` | `1095.00` | 724,630,000.00 USD | 0.00 USD | 61,260.00 USD | `-51.17%` | `55.94` |
| `Live` | `Long` | `1105.00` | 724,570,000.00 USD | 0.00 USD | 158,010.00 USD | `-50.72%` | `143.00` |
| `Live` | `Long` | `1115.00` | 724,410,000.00 USD | 0.00 USD | 7,660,000.00 USD | `-50.28%` | `6,871.09` |
| `Live` | `Long` | `1125.00` | 716,750,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-49.83%` | `1,167.46` |
| `Live` | `Long` | `1135.00` | 715,440,000.00 USD | 0.00 USD | 565,980.00 USD | `-49.39%` | `498.66` |
| `Live` | `Long` | `1145.00` | 714,870,000.00 USD | 0.00 USD | 226,120.00 USD | `-48.94%` | `197.49` |
| `Live` | `Long` | `1155.00` | 714,650,000.00 USD | 0.00 USD | 755,360.00 USD | `-48.49%` | `653.99` |
| `Live` | `Long` | `1165.00` | 713,890,000.00 USD | 0.00 USD | 1,450,000.00 USD | `-48.05%` | `1,246.33` |
| `Live` | `Long` | `1175.00` | 712,440,000.00 USD | 0.00 USD | 219,750.00 USD | `-47.60%` | `187.02` |
| `Live` | `Long` | `1185.00` | 712,220,000.00 USD | 0.00 USD | 2,730,000.00 USD | `-47.16%` | `2,302.10` |
| `Live` | `Long` | `1195.00` | 709,490,000.00 USD | 0.00 USD | 323,550.00 USD | `-46.71%` | `270.76` |
| `Live` | `Long` | `1205.00` | 709,170,000.00 USD | 0.00 USD | 200,180.00 USD | `-46.27%` | `166.12` |
| `Live` | `Long` | `1215.00` | 708,970,000.00 USD | 0.00 USD | 112,000.00 USD | `-45.82%` | `92.18` |
| `Live` | `Long` | `1225.00` | 708,860,000.00 USD | 0.00 USD | 2,260,000.00 USD | `-45.37%` | `1,842.12` |
| `Live` | `Long` | `1235.00` | 706,600,000.00 USD | 0.00 USD | 94,510.00 USD | `-44.93%` | `76.53` |
| `Live` | `Long` | `1245.00` | 706,510,000.00 USD | 0.00 USD | 768,060.00 USD | `-44.48%` | `616.92` |
| `Live` | `Long` | `1255.00` | 705,740,000.00 USD | 0.00 USD | 461,080.00 USD | `-44.04%` | `367.40` |
| `Live` | `Long` | `1265.00` | 705,280,000.00 USD | 0.00 USD | 205,060.00 USD | `-43.59%` | `162.10` |
| `Live` | `Long` | `1275.00` | 705,070,000.00 USD | 0.00 USD | 15,430,000.00 USD | `-43.14%` | `12,101.72` |
| `Live` | `Long` | `1285.00` | 689,640,000.00 USD | 0.00 USD | 264,370.00 USD | `-42.70%` | `205.73` |
| `Live` | `Long` | `1295.00` | 689,380,000.00 USD | 0.00 USD | 176,850.00 USD | `-42.25%` | `136.57` |
| `Live` | `Long` | `1305.00` | 689,200,000.00 USD | 0.00 USD | 654,450.00 USD | `-41.81%` | `501.49` |
| `Live` | `Long` | `1315.00` | 688,550,000.00 USD | 0.00 USD | 125,690.00 USD | `-41.36%` | `95.58` |
| `Live` | `Long` | `1325.00` | 688,420,000.00 USD | 0.00 USD | 460,240.00 USD | `-40.91%` | `347.35` |
| `Live` | `Long` | `1335.00` | 687,960,000.00 USD | 0.00 USD | 5,400,000.00 USD | `-40.47%` | `4,043.62` |
| `Live` | `Long` | `1345.00` | 682,560,000.00 USD | 0.00 USD | 436,480.00 USD | `-40.02%` | `324.52` |
| `Live` | `Long` | `1355.00` | 682,130,000.00 USD | 0.00 USD | 12,690,000.00 USD | `-39.58%` | `9,362.11` |
| `Live` | `Long` | `1365.00` | 669,440,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-39.13%` | `780.27` |
| `Live` | `Long` | `1375.00` | 668,380,000.00 USD | 0.00 USD | 7,070,000.00 USD | `-38.68%` | `5,140.64` |
| `Live` | `Long` | `1385.00` | 661,310,000.00 USD | 0.00 USD | 2,570,000.00 USD | `-38.24%` | `1,856.66` |
| `Live` | `Long` | `1395.00` | 658,740,000.00 USD | 0.00 USD | 2,050,000.00 USD | `-37.79%` | `1,466.68` |
| `Live` | `Long` | `1405.00` | 656,690,000.00 USD | 0.00 USD | 10,660,000.00 USD | `-37.35%` | `7,588.83` |
| `Live` | `Long` | `1415.00` | 646,030,000.00 USD | 0.00 USD | 45,260.00 USD | `-36.90%` | `31.99` |
| `Live` | `Long` | `1425.00` | 645,980,000.00 USD | 0.00 USD | 18,640,000.00 USD | `-36.45%` | `13,077.67` |
| `Live` | `Long` | `1435.00` | 627,350,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-36.01%` | `910.50` |
| `Live` | `Long` | `1445.00` | 626,040,000.00 USD | 0.00 USD | 56,350.00 USD | `-35.56%` | `39.00` |
| `Live` | `Long` | `1455.00` | 625,980,000.00 USD | 0.00 USD | 6,870,000.00 USD | `-35.12%` | `4,719.31` |
| `Live` | `Long` | `1465.00` | 619,120,000.00 USD | 0.00 USD | 1,990,000.00 USD | `-34.67%` | `1,361.20` |
| `Live` | `Long` | `1475.00` | 617,120,000.00 USD | 0.00 USD | 5,640,000.00 USD | `-34.23%` | `3,826.00` |
| `Live` | `Long` | `1485.00` | 611,480,000.00 USD | 0.00 USD | 149,240.00 USD | `-33.78%` | `100.50` |
| `Live` | `Long` | `1495.00` | 611,330,000.00 USD | 0.00 USD | 876,920.00 USD | `-33.33%` | `586.57` |
| `Live` | `Long` | `1505.00` | 610,450,000.00 USD | 0.00 USD | 437,140.00 USD | `-32.89%` | `290.46` |
| `Live` | `Long` | `1515.00` | 610,020,000.00 USD | 0.00 USD | 582,560.00 USD | `-32.44%` | `384.53` |
| `Live` | `Long` | `1525.00` | 609,430,000.00 USD | 0.00 USD | 20,580,000.00 USD | `-32.00%` | `13,496.52` |
| `Live` | `Long` | `1535.00` | 588,850,000.00 USD | 0.00 USD | 16,240,000.00 USD | `-31.55%` | `10,579.30` |
| `Live` | `Long` | `1545.00` | 572,610,000.00 USD | 0.00 USD | 2,850,000.00 USD | `-31.10%` | `1,846.02` |
| `Live` | `Long` | `1555.00` | 569,760,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-30.66%` | `722.76` |
| `Live` | `Long` | `1565.00` | 568,640,000.00 USD | 0.00 USD | 2,660,000.00 USD | `-30.21%` | `1,701.64` |
| `Live` | `Long` | `1575.00` | 565,970,000.00 USD | 0.00 USD | 587,950.00 USD | `-29.77%` | `373.30` |
| `Live` | `Long` | `1585.00` | 565,380,000.00 USD | 0.00 USD | 803,000.00 USD | `-29.32%` | `506.63` |
| `Live` | `Long` | `1595.00` | 564,580,000.00 USD | 0.00 USD | 1,520,000.00 USD | `-28.87%` | `954.16` |
| `Live` | `Long` | `1605.00` | 563,060,000.00 USD | 0.00 USD | 18,380,000.00 USD | `-28.43%` | `11,454.29` |
| `Live` | `Long` | `1615.00` | 544,680,000.00 USD | 0.00 USD | 707,630.00 USD | `-27.98%` | `438.16` |
| `Live` | `Long` | `1625.00` | 543,970,000.00 USD | 0.00 USD | 2,070,000.00 USD | `-27.54%` | `1,273.75` |
| `Live` | `Long` | `1635.00` | 541,900,000.00 USD | 0.00 USD | 18,720,000.00 USD | `-27.09%` | `11,447.84` |
| `Live` | `Long` | `1645.00` | 523,180,000.00 USD | 0.00 USD | 38,610,000.00 USD | `-26.64%` | `23,473.92` |
| `Live` | `Long` | `1655.00` | 484,570,000.00 USD | 0.00 USD | 745,590.00 USD | `-26.20%` | `450.51` |
| `Live` | `Long` | `1665.00` | 483,820,000.00 USD | 0.00 USD | 11,980,000.00 USD | `-25.75%` | `7,197.46` |
| `Live` | `Long` | `1675.00` | 471,840,000.00 USD | 0.00 USD | 1,340,000.00 USD | `-25.31%` | `801.18` |
| `Live` | `Long` | `1685.00` | 470,500,000.00 USD | 0.00 USD | 784,890.00 USD | `-24.86%` | `465.81` |
| `Live` | `Long` | `1695.00` | 469,710,000.00 USD | 0.00 USD | 341,360.00 USD | `-24.41%` | `201.40` |
| `Live` | `Long` | `1705.00` | 469,370,000.00 USD | 0.00 USD | 4,840,000.00 USD | `-23.97%` | `2,838.87` |
| `Live` | `Long` | `1715.00` | 464,530,000.00 USD | 0.00 USD | 250,360.00 USD | `-23.52%` | `145.99` |
| `Live` | `Long` | `1725.00` | 464,280,000.00 USD | 0.00 USD | 36,980,000.00 USD | `-23.08%` | `21,438.82` |
| `Live` | `Long` | `1735.00` | 427,300,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-22.63%` | `1,008.82` |
| `Live` | `Long` | `1745.00` | 425,550,000.00 USD | 0.00 USD | 1,350,000.00 USD | `-22.19%` | `776.26` |
| `Live` | `Long` | `1755.00` | 424,190,000.00 USD | 0.00 USD | 28,620,000.00 USD | `-21.74%` | `16,309.79` |
| `Live` | `Long` | `1765.00` | 395,570,000.00 USD | 0.00 USD | 20,810,000.00 USD | `-21.29%` | `11,790.97` |
| `Live` | `Long` | `1775.00` | 374,760,000.00 USD | 0.00 USD | 3,780,000.00 USD | `-20.85%` | `2,127.39` |
| `Live` | `Long` | `1785.00` | 370,980,000.00 USD | 0.00 USD | 61,330,000.00 USD | `-20.40%` | `34,357.11` |
| `Live` | `Long` | `1795.00` | 309,650,000.00 USD | 0.00 USD | 408,110.00 USD | `-19.96%` | `227.36` |
| `Live` | `Long` | `1805.00` | 309,240,000.00 USD | 0.00 USD | 3,060,000.00 USD | `-19.51%` | `1,694.62` |
| `Live` | `Long` | `1815.00` | 306,190,000.00 USD | 0.00 USD | 769,970.00 USD | `-19.06%` | `424.23` |
| `Live` | `Long` | `1825.00` | 305,420,000.00 USD | 0.00 USD | 1,630,000.00 USD | `-18.62%` | `892.83` |
| `Live` | `Long` | `1835.00` | 303,790,000.00 USD | 0.00 USD | 12,510,000.00 USD | `-18.17%` | `6,816.06` |
| `Live` | `Long` | `1845.00` | 291,280,000.00 USD | 0.00 USD | 19,230,000.00 USD | `-17.73%` | `10,423.25` |
| `Live` | `Long` | `1855.00` | 272,050,000.00 USD | 0.00 USD | 2,430,000.00 USD | `-17.28%` | `1,310.77` |
| `Live` | `Long` | `1865.00` | 269,620,000.00 USD | 0.00 USD | 1,940,000.00 USD | `-16.83%` | `1,042.42` |
| `Live` | `Long` | `1875.00` | 267,670,000.00 USD | 0.00 USD | 6,110,000.00 USD | `-16.39%` | `3,258.37` |
| `Live` | `Long` | `1885.00` | 261,560,000.00 USD | 0.00 USD | 5,450,000.00 USD | `-15.94%` | `2,888.77` |
| `Live` | `Long` | `1895.00` | 256,120,000.00 USD | 0.00 USD | 653,900.00 USD | `-15.50%` | `345.07` |
| `Live` | `Long` | `1905.00` | 255,460,000.00 USD | 0.00 USD | 494,920.00 USD | `-15.05%` | `259.80` |
| `Live` | `Long` | `1915.00` | 254,970,000.00 USD | 0.00 USD | 18,350,000.00 USD | `-14.60%` | `9,584.31` |
| `Live` | `Long` | `1925.00` | 236,620,000.00 USD | 0.00 USD | 16,610,000.00 USD | `-14.16%` | `8,626.26` |
| `Live` | `Long` | `1935.00` | 220,010,000.00 USD | 0.00 USD | 1,270,000.00 USD | `-13.71%` | `656.86` |
| `Live` | `Long` | `1945.00` | 218,740,000.00 USD | 0.00 USD | 5,010,000.00 USD | `-13.27%` | `2,574.81` |
| `Live` | `Long` | `1955.00` | 213,730,000.00 USD | 0.00 USD | 2,760,000.00 USD | `-12.82%` | `1,411.63` |
| `Live` | `Long` | `1965.00` | 210,970,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-12.37%` | `563.22` |
| `Live` | `Long` | `1975.00` | 209,860,000.00 USD | 0.00 USD | 1,810,000.00 USD | `-11.93%` | `918.39` |
| `Live` | `Long` | `1985.00` | 208,050,000.00 USD | 0.00 USD | 5,620,000.00 USD | `-11.48%` | `2,829.98` |
| `Live` | `Long` | `1995.00` | 202,430,000.00 USD | 0.00 USD | 1,490,000.00 USD | `-11.04%` | `748.29` |
| `Live` | `Long` | `2005.00` | 200,940,000.00 USD | 0.00 USD | 2,050,000.00 USD | `-10.59%` | `1,022.56` |
| `Live` | `Long` | `2015.00` | 198,890,000.00 USD | 0.00 USD | 2,810,000.00 USD | `-10.14%` | `1,394.12` |
| `Live` | `Long` | `2025.00` | 196,080,000.00 USD | 0.00 USD | 834,860.00 USD | `-9.70%` | `412.28` |
| `Live` | `Long` | `2035.00` | 195,250,000.00 USD | 0.00 USD | 588,290.00 USD | `-9.25%` | `289.09` |
| `Live` | `Long` | `2045.00` | 194,660,000.00 USD | 0.00 USD | 1,980,000.00 USD | `-8.81%` | `965.78` |
| `Live` | `Long` | `2055.00` | 192,680,000.00 USD | 0.00 USD | 7,180,000.00 USD | `-8.36%` | `3,493.29` |
| `Live` | `Long` | `2065.00` | 185,500,000.00 USD | 0.00 USD | 14,780,000.00 USD | `-7.92%` | `7,158.61` |
| `Live` | `Long` | `2075.00` | 170,720,000.00 USD | 0.00 USD | 1,590,000.00 USD | `-7.47%` | `764.94` |
| `Live` | `Long` | `2085.00` | 169,130,000.00 USD | 0.00 USD | 13,710,000.00 USD | `-7.02%` | `6,577.79` |
| `Live` | `Long` | `2095.00` | 155,420,000.00 USD | 0.00 USD | 1,700,000.00 USD | `-6.58%` | `811.52` |
| `Live` | `Long` | `2105.00` | 153,720,000.00 USD | 0.00 USD | 2,250,000.00 USD | `-6.13%` | `1,069.09` |
| `Live` | `Long` | `2115.00` | 151,470,000.00 USD | 0.00 USD | 1,830,000.00 USD | `-5.69%` | `864.14` |
| `Live` | `Long` | `2125.00` | 149,640,000.00 USD | 0.00 USD | 123,520,000.00 USD | `-5.24%` | `58,125.80` |
| `Live` | `Long` | `2135.00` | 26,120,000.00 USD | 0.00 USD | 4,970,000.00 USD | `-4.79%` | `2,329.22` |
| `Live` | `Long` | `2145.00` | 21,150,000.00 USD | 0.00 USD | 4,040,000.00 USD | `-4.35%` | `1,884.88` |
| `Live` | `Long` | `2155.00` | 17,110,000.00 USD | 0.00 USD | 4,230,000.00 USD | `-3.90%` | `1,962.95` |
| `Live` | `Long` | `2165.00` | 12,880,000.00 USD | 0.00 USD | 5,990,000.00 USD | `-3.46%` | `2,768.94` |
| `Live` | `Long` | `2175.00` | 6,880,000.00 USD | 0.00 USD | 5,790,000.00 USD | `-3.01%` | `2,661.67` |
| `Live` | `Long` | `2185.00` | 1,090,000.00 USD | 0.00 USD | 800,690.00 USD | `-2.56%` | `366.45` |
| `Live` | `Long` | `2195.00` | 292,940.00 USD | 0.00 USD | 152,660.00 USD | `-2.12%` | `69.55` |
| `Live` | `Long` | `2205.00` | 140,270.00 USD | 0.00 USD | 140,270.00 USD | `-1.67%` | `63.61` |
| `Live` | `Short` | `2245.00` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | `+0.11%` | `903.72` |
| `Live` | `Short` | `2255.00` | 2,230,000.00 USD | 202,140.00 USD | 0.00 USD | `+0.56%` | `89.64` |
| `Live` | `Short` | `2265.00` | 6,740,000.00 USD | 4,500,000.00 USD | 0.00 USD | `+1.00%` | `1,988.96` |
| `Live` | `Short` | `2275.00` | 6,820,000.00 USD | 79,460.00 USD | 0.00 USD | `+1.45%` | `34.93` |
| `Live` | `Short` | `2285.00` | 6,980,000.00 USD | 167,510.00 USD | 0.00 USD | `+1.90%` | `73.31` |
| `Live` | `Short` | `2295.00` | 9,420,000.00 USD | 2,440,000.00 USD | 0.00 USD | `+2.34%` | `1,062.58` |
| `Live` | `Short` | `2305.00` | 9,580,000.00 USD | 158,470.00 USD | 0.00 USD | `+2.79%` | `68.75` |
| `Live` | `Short` | `2315.00` | 10,740,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+3.23%` | `501.08` |
| `Live` | `Short` | `2325.00` | 12,530,000.00 USD | 1,790,000.00 USD | 0.00 USD | `+3.68%` | `769.45` |
| `Live` | `Short` | `2335.00` | 13,920,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+4.12%` | `596.93` |
| `Live` | `Short` | `2345.00` | 14,340,000.00 USD | 416,450.00 USD | 0.00 USD | `+4.57%` | `177.59` |
| `Live` | `Short` | `2355.00` | 15,570,000.00 USD | 1,230,000.00 USD | 0.00 USD | `+5.02%` | `521.61` |
| `Live` | `Short` | `2365.00` | 19,610,000.00 USD | 4,040,000.00 USD | 0.00 USD | `+5.46%` | `1,709.33` |
| `Live` | `Short` | `2375.00` | 25,250,000.00 USD | 5,640,000.00 USD | 0.00 USD | `+5.91%` | `2,376.34` |
| `Live` | `Short` | `2385.00` | 26,440,000.00 USD | 1,180,000.00 USD | 0.00 USD | `+6.35%` | `496.75` |
| `Live` | `Short` | `2395.00` | 26,460,000.00 USD | 17,990.00 USD | 0.00 USD | `+6.80%` | `7.51` |
| `Live` | `Short` | `2405.00` | 26,650,000.00 USD | 190,150.00 USD | 0.00 USD | `+7.25%` | `79.06` |
| `Live` | `Short` | `2415.00` | 26,870,000.00 USD | 220,420.00 USD | 0.00 USD | `+7.69%` | `91.27` |
| `Live` | `Short` | `2425.00` | 26,940,000.00 USD | 69,910.00 USD | 0.00 USD | `+8.14%` | `28.83` |
| `Live` | `Short` | `2435.00` | 28,250,000.00 USD | 1,310,000.00 USD | 0.00 USD | `+8.58%` | `537.37` |
| `Live` | `Short` | `2445.00` | 28,290,000.00 USD | 40,510.00 USD | 0.00 USD | `+9.03%` | `16.57` |
| `Live` | `Short` | `2455.00` | 82,580,000.00 USD | 54,300,000.00 USD | 0.00 USD | `+9.48%` | `22,116.18` |
| `Live` | `Short` | `2465.00` | 94,120,000.00 USD | 11,530,000.00 USD | 0.00 USD | `+9.92%` | `4,679.17` |
| `Live` | `Short` | `2475.00` | 94,360,000.00 USD | 249,030.00 USD | 0.00 USD | `+10.37%` | `100.62` |
| `Live` | `Short` | `2485.00` | 94,430,000.00 USD | 63,020.00 USD | 0.00 USD | `+10.81%` | `25.36` |
| `Live` | `Short` | `2495.00` | 96,510,000.00 USD | 2,080,000.00 USD | 0.00 USD | `+11.26%` | `833.70` |
| `Live` | `Short` | `2505.00` | 112,670,000.00 USD | 16,160,000.00 USD | 0.00 USD | `+11.71%` | `6,451.49` |
| `Live` | `Short` | `2515.00` | 112,820,000.00 USD | 148,280.00 USD | 0.00 USD | `+12.15%` | `58.96` |
| `Live` | `Short` | `2525.00` | 112,890,000.00 USD | 77,380.00 USD | 0.00 USD | `+12.60%` | `30.65` |
| `Live` | `Short` | `2535.00` | 113,860,000.00 USD | 961,350.00 USD | 0.00 USD | `+13.04%` | `379.23` |
| `Live` | `Short` | `2545.00` | 113,870,000.00 USD | 12,650.00 USD | 0.00 USD | `+13.49%` | `4.97` |
| `Live` | `Short` | `2555.00` | 114,070,000.00 USD | 197,130.00 USD | 0.00 USD | `+13.94%` | `77.16` |
| `Live` | `Short` | `2565.00` | 114,130,000.00 USD | 60,800.00 USD | 0.00 USD | `+14.38%` | `23.70` |
| `Live` | `Short` | `2575.00` | 114,180,000.00 USD | 50,100.00 USD | 0.00 USD | `+14.83%` | `19.46` |
| `Live` | `Short` | `2585.00` | 140,680,000.00 USD | 26,510,000.00 USD | 0.00 USD | `+15.27%` | `10,254.25` |
| `Live` | `Short` | `2595.00` | 154,270,000.00 USD | 13,590,000.00 USD | 0.00 USD | `+15.72%` | `5,237.47` |
| `Live` | `Short` | `2605.00` | 160,350,000.00 USD | 6,080,000.00 USD | 0.00 USD | `+16.16%` | `2,333.44` |
| `Live` | `Short` | `2615.00` | 161,060,000.00 USD | 707,260.00 USD | 0.00 USD | `+16.61%` | `270.46` |
| `Live` | `Short` | `2625.00` | 201,250,000.00 USD | 40,190,000.00 USD | 0.00 USD | `+17.06%` | `15,310.14` |
| `Live` | `Short` | `2635.00` | 202,790,000.00 USD | 1,540,000.00 USD | 0.00 USD | `+17.50%` | `582.75` |
| `Live` | `Short` | `2645.00` | 203,850,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+17.95%` | `404.20` |
| `Live` | `Short` | `2655.00` | 229,940,000.00 USD | 26,090,000.00 USD | 0.00 USD | `+18.39%` | `9,825.27` |
| `Live` | `Short` | `2665.00` | 230,000,000.00 USD | 55,570.00 USD | 0.00 USD | `+18.84%` | `20.85` |
| `Live` | `Short` | `2675.00` | 240,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | `+19.29%` | `3,933.31` |
| `Live` | `Short` | `2685.00` | 240,540,000.00 USD | 26,860.00 USD | 0.00 USD | `+19.73%` | `10.00` |
| `Live` | `Short` | `2695.00` | 240,730,000.00 USD | 185,300.00 USD | 0.00 USD | `+20.18%` | `68.76` |
| `Live` | `Short` | `2705.00` | 241,260,000.00 USD | 525,220.00 USD | 0.00 USD | `+20.62%` | `194.17` |
| `Live` | `Short` | `2715.00` | 241,390,000.00 USD | 131,390.00 USD | 0.00 USD | `+21.07%` | `48.39` |
| `Live` | `Short` | `2725.00` | 242,090,000.00 USD | 707,680.00 USD | 0.00 USD | `+21.52%` | `259.70` |
| `Live` | `Short` | `2735.00` | 242,110,000.00 USD | 20,100.00 USD | 0.00 USD | `+21.96%` | `7.35` |
| `Live` | `Short` | `2745.00` | 243,000,000.00 USD | 886,230.00 USD | 0.00 USD | `+22.41%` | `322.85` |
| `Live` | `Short` | `2755.00` | 248,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | `+22.85%` | `2,101.21` |
| `Live` | `Short` | `2765.00` | 254,330,000.00 USD | 5,540,000.00 USD | 0.00 USD | `+23.30%` | `2,003.46` |
| `Live` | `Short` | `2775.00` | 267,640,000.00 USD | 13,310,000.00 USD | 0.00 USD | `+23.75%` | `4,795.56` |
| `Live` | `Short` | `2785.00` | 267,670,000.00 USD | 29,890.00 USD | 0.00 USD | `+24.19%` | `10.73` |
| `Live` | `Short` | `2795.00` | 284,380,000.00 USD | 16,710,000.00 USD | 0.00 USD | `+24.64%` | `5,978.68` |
| `Live` | `Short` | `2805.00` | 288,740,000.00 USD | 4,370,000.00 USD | 0.00 USD | `+25.08%` | `1,557.25` |
| `Live` | `Short` | `2815.00` | 289,910,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+25.53%` | `412.23` |
| `Live` | `Short` | `2825.00` | 290,570,000.00 USD | 666,320.00 USD | 0.00 USD | `+25.98%` | `235.87` |
| `Live` | `Short` | `2835.00` | 296,650,000.00 USD | 6,070,000.00 USD | 0.00 USD | `+26.42%` | `2,142.74` |
| `Live` | `Short` | `2845.00` | 297,180,000.00 USD | 533,510.00 USD | 0.00 USD | `+26.87%` | `187.53` |
| `Live` | `Short` | `2855.00` | 297,310,000.00 USD | 127,560.00 USD | 0.00 USD | `+27.31%` | `44.68` |
| `Live` | `Short` | `2865.00` | 297,640,000.00 USD | 331,830.00 USD | 0.00 USD | `+27.76%` | `115.82` |
| `Live` | `Short` | `2875.00` | 297,760,000.00 USD | 119,980.00 USD | 0.00 USD | `+28.21%` | `41.73` |
| `Live` | `Short` | `2885.00` | 299,040,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+28.65%` | `443.27` |
| `Live` | `Short` | `2895.00` | 300,680,000.00 USD | 1,640,000.00 USD | 0.00 USD | `+29.10%` | `565.65` |
| `Live` | `Short` | `2905.00` | 328,270,000.00 USD | 27,600,000.00 USD | 0.00 USD | `+29.54%` | `9,500.15` |
| `Live` | `Short` | `2915.00` | 330,600,000.00 USD | 2,330,000.00 USD | 0.00 USD | `+29.99%` | `799.06` |
| `Live` | `Short` | `2925.00` | 330,750,000.00 USD | 148,030.00 USD | 0.00 USD | `+30.43%` | `50.61` |
| `Live` | `Short` | `2935.00` | 330,780,000.00 USD | 32,590.00 USD | 0.00 USD | `+30.88%` | `11.10` |
| `Live` | `Short` | `2945.00` | 331,510,000.00 USD | 721,780.00 USD | 0.00 USD | `+31.33%` | `245.09` |
| `Live` | `Short` | `2955.00` | 331,820,000.00 USD | 309,780.00 USD | 0.00 USD | `+31.77%` | `104.83` |
| `Live` | `Short` | `2965.00` | 335,590,000.00 USD | 3,770,000.00 USD | 0.00 USD | `+32.22%` | `1,272.89` |
| `Live` | `Short` | `2975.00` | 335,640,000.00 USD | 52,160.00 USD | 0.00 USD | `+32.66%` | `17.53` |
| `Live` | `Short` | `2985.00` | 336,340,000.00 USD | 703,430.00 USD | 0.00 USD | `+33.11%` | `235.65` |
| `Live` | `Short` | `2995.00` | 337,940,000.00 USD | 1,590,000.00 USD | 0.00 USD | `+33.56%` | `532.30` |
| `Live` | `Short` | `3005.00` | 358,700,000.00 USD | 20,760,000.00 USD | 0.00 USD | `+34.00%` | `6,909.27` |
| `Live` | `Short` | `3015.00` | 361,760,000.00 USD | 3,060,000.00 USD | 0.00 USD | `+34.45%` | `1,014.79` |
| `Live` | `Short` | `3025.00` | 362,580,000.00 USD | 822,110.00 USD | 0.00 USD | `+34.89%` | `271.77` |
| `Live` | `Short` | `3035.00` | 375,400,000.00 USD | 12,820,000.00 USD | 0.00 USD | `+35.34%` | `4,223.99` |
| `Live` | `Short` | `3045.00` | 376,910,000.00 USD | 1,510,000.00 USD | 0.00 USD | `+35.79%` | `494.68` |
| `Live` | `Short` | `3055.00` | 377,550,000.00 USD | 640,770.00 USD | 0.00 USD | `+36.23%` | `209.74` |
| `Live` | `Short` | `3065.00` | 377,560,000.00 USD | 13,620.00 USD | 0.00 USD | `+36.68%` | `4.44` |
| `Live` | `Short` | `3075.00` | 382,990,000.00 USD | 5,430,000.00 USD | 0.00 USD | `+37.12%` | `1,766.24` |
| `Live` | `Short` | `3085.00` | 383,030,000.00 USD | 32,360.00 USD | 0.00 USD | `+37.57%` | `10.49` |
| `Live` | `Short` | `3095.00` | 383,710,000.00 USD | 678,510.00 USD | 0.00 USD | `+38.02%` | `219.23` |
| `Live` | `Short` | `3105.00` | 387,440,000.00 USD | 3,740,000.00 USD | 0.00 USD | `+38.46%` | `1,203.51` |
| `Live` | `Short` | `3115.00` | 387,590,000.00 USD | 150,800.00 USD | 0.00 USD | `+38.91%` | `48.41` |
| `Live` | `Short` | `3125.00` | 387,720,000.00 USD | 126,640.00 USD | 0.00 USD | `+39.35%` | `40.52` |
| `Live` | `Short` | `3135.00` | 394,140,000.00 USD | 6,420,000.00 USD | 0.00 USD | `+39.80%` | `2,049.00` |
| `Live` | `Short` | `3145.00` | 423,850,000.00 USD | 29,710,000.00 USD | 0.00 USD | `+40.25%` | `9,446.91` |
| `Live` | `Short` | `3155.00` | 428,820,000.00 USD | 4,960,000.00 USD | 0.00 USD | `+40.69%` | `1,572.40` |
| `Live` | `Short` | `3165.00` | 428,970,000.00 USD | 151,290.00 USD | 0.00 USD | `+41.14%` | `47.80` |
| `Live` | `Short` | `3175.00` | 429,650,000.00 USD | 681,290.00 USD | 0.00 USD | `+41.58%` | `214.58` |
| `Live` | `Short` | `3185.00` | 436,500,000.00 USD | 6,860,000.00 USD | 0.00 USD | `+42.03%` | `2,152.53` |
| `Live` | `Short` | `3195.00` | 440,160,000.00 USD | 3,660,000.00 USD | 0.00 USD | `+42.47%` | `1,144.63` |
| `Live` | `Short` | `3205.00` | 440,300,000.00 USD | 141,980.00 USD | 0.00 USD | `+42.92%` | `44.30` |
| `Live` | `Short` | `3215.00` | 440,480,000.00 USD | 173,450.00 USD | 0.00 USD | `+43.37%` | `53.95` |
| `Live` | `Short` | `3225.00` | 450,270,000.00 USD | 9,800,000.00 USD | 0.00 USD | `+43.81%` | `3,038.34` |
| `Live` | `Short` | `3235.00` | 460,180,000.00 USD | 9,910,000.00 USD | 0.00 USD | `+44.26%` | `3,062.15` |
| `Live` | `Short` | `3245.00` | 468,630,000.00 USD | 8,440,000.00 USD | 0.00 USD | `+44.70%` | `2,602.33` |
| `Live` | `Short` | `3255.00` | 468,650,000.00 USD | 28,620.00 USD | 0.00 USD | `+45.15%` | `8.79` |
| `Live` | `Short` | `3265.00` | 473,510,000.00 USD | 4,860,000.00 USD | 0.00 USD | `+45.60%` | `1,488.50` |
| `Live` | `Short` | `3275.00` | 482,010,000.00 USD | 8,490,000.00 USD | 0.00 USD | `+46.04%` | `2,593.84` |
| `Live` | `Short` | `3285.00` | 482,270,000.00 USD | 260,070.00 USD | 0.00 USD | `+46.49%` | `79.17` |
| `Live` | `Short` | `3295.00` | 482,400,000.00 USD | 128,500.00 USD | 0.00 USD | `+46.93%` | `39.00` |
| `Live` | `Short` | `3305.00` | 485,280,000.00 USD | 2,880,000.00 USD | 0.00 USD | `+47.38%` | `872.77` |
| `Live` | `Short` | `3315.00` | 485,970,000.00 USD | 687,300.00 USD | 0.00 USD | `+47.83%` | `207.33` |
| `Live` | `Short` | `3325.00` | 486,040,000.00 USD | 71,450.00 USD | 0.00 USD | `+48.27%` | `21.49` |
| `Live` | `Short` | `3335.00` | 486,700,000.00 USD | 663,170.00 USD | 0.00 USD | `+48.72%` | `198.85` |
| `Live` | `Short` | `3345.00` | 486,750,000.00 USD | 41,930.00 USD | 0.00 USD | `+49.16%` | `12.53` |
| `Live` | `Short` | `3355.00` | 486,840,000.00 USD | 98,520.00 USD | 0.00 USD | `+49.61%` | `29.37` |
| `Live` | `Short` | `3365.00` | 494,230,000.00 USD | 7,380,000.00 USD | 0.00 USD | `+50.06%` | `2,194.02` |
| `Live` | `Short` | `3375.00` | 494,300,000.00 USD | 70,280.00 USD | 0.00 USD | `+50.50%` | `20.82` |
| `Live` | `Short` | `3385.00` | 494,400,000.00 USD | 101,040.00 USD | 0.00 USD | `+50.95%` | `29.85` |
| `Live` | `Short` | `3395.00` | 497,280,000.00 USD | 2,890,000.00 USD | 0.00 USD | `+51.39%` | `850.00` |
| `Live` | `Short` | `3405.00` | 497,490,000.00 USD | 207,160.00 USD | 0.00 USD | `+51.84%` | `60.84` |
| `Live` | `Short` | `3415.00` | 497,510,000.00 USD | 20,980.00 USD | 0.00 USD | `+52.29%` | `6.14` |
| `Live` | `Short` | `3425.00` | 512,390,000.00 USD | 14,880,000.00 USD | 0.00 USD | `+52.73%` | `4,343.56` |
| `Live` | `Short` | `3435.00` | 515,310,000.00 USD | 2,920,000.00 USD | 0.00 USD | `+53.18%` | `850.44` |
| `Live` | `Short` | `3445.00` | 515,610,000.00 USD | 300,130.00 USD | 0.00 USD | `+53.62%` | `87.12` |
| `Live` | `Short` | `3455.00` | 516,700,000.00 USD | 1,090,000.00 USD | 0.00 USD | `+54.07%` | `316.08` |
| `Live` | `Short` | `3465.00` | 516,790,000.00 USD | 85,780.00 USD | 0.00 USD | `+54.52%` | `24.76` |
| `Live` | `Short` | `3475.00` | 574,810,000.00 USD | 58,020,000.00 USD | 0.00 USD | `+54.96%` | `16,697.40` |
| `Live` | `Short` | `3485.00` | 575,280,000.00 USD | 466,100.00 USD | 0.00 USD | `+55.41%` | `133.74` |
| `Live` | `Short` | `3495.00` | 578,230,000.00 USD | 2,950,000.00 USD | 0.00 USD | `+55.85%` | `843.48` |
| `Live` | `Short` | `3505.00` | 578,500,000.00 USD | 269,580.00 USD | 0.00 USD | `+56.30%` | `76.91` |
| `Live` | `Short` | `3515.00` | 578,510,000.00 USD | 11,740.00 USD | 0.00 USD | `+56.74%` | `3.34` |
| `Live` | `Short` | `3525.00` | 578,610,000.00 USD | 103,940.00 USD | 0.00 USD | `+57.19%` | `29.49` |
| `Live` | `Short` | `3535.00` | 578,870,000.00 USD | 255,300.00 USD | 0.00 USD | `+57.64%` | `72.22` |
| `Live` | `Short` | `3545.00` | 593,150,000.00 USD | 14,280,000.00 USD | 0.00 USD | `+58.08%` | `4,028.02` |
| `Live` | `Short` | `3555.00` | 624,810,000.00 USD | 31,660,000.00 USD | 0.00 USD | `+58.53%` | `8,906.14` |
| `Live` | `Short` | `3565.00` | 624,870,000.00 USD | 61,200.00 USD | 0.00 USD | `+58.97%` | `17.17` |
| `Live` | `Short` | `3575.00` | 624,970,000.00 USD | 100,020.00 USD | 0.00 USD | `+59.42%` | `27.98` |
| `Live` | `Short` | `3585.00` | 625,910,000.00 USD | 942,290.00 USD | 0.00 USD | `+59.87%` | `262.84` |
| `Live` | `Short` | `3595.00` | 626,020,000.00 USD | 108,260.00 USD | 0.00 USD | `+60.31%` | `30.11` |
| `Live` | `Short` | `3605.00` | 626,070,000.00 USD | 53,170.00 USD | 0.00 USD | `+60.76%` | `14.75` |
| `Live` | `Short` | `3615.00` | 630,170,000.00 USD | 4,100,000.00 USD | 0.00 USD | `+61.20%` | `1,132.95` |
| `Live` | `Short` | `3625.00` | 630,840,000.00 USD | 675,620.00 USD | 0.00 USD | `+61.65%` | `186.38` |
| `Live` | `Short` | `3635.00` | 641,210,000.00 USD | 10,370,000.00 USD | 0.00 USD | `+62.10%` | `2,852.03` |
| `Live` | `Short` | `3645.00` | 641,220,000.00 USD | 6,300.00 USD | 0.00 USD | `+62.54%` | `1.73` |
| `Live` | `Short` | `3655.00` | 647,710,000.00 USD | 6,490,000.00 USD | 0.00 USD | `+62.99%` | `1,776.90` |
| `Live` | `Short` | `3665.00` | 648,810,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+63.43%` | `299.50` |
| `Live` | `Short` | `3675.00` | 648,810,000.00 USD | 2,700.00 USD | 0.00 USD | `+63.88%` | `0.73` |
| `Live` | `Short` | `3685.00` | 649,150,000.00 USD | 335,730.00 USD | 0.00 USD | `+64.33%` | `91.11` |
| `Live` | `Short` | `3695.00` | 649,200,000.00 USD | 55,280.00 USD | 0.00 USD | `+64.77%` | `14.96` |
| `Live` | `Short` | `3705.00` | 649,220,000.00 USD | 16,530.00 USD | 0.00 USD | `+65.22%` | `4.46` |
| `Live` | `Short` | `3715.00` | 649,340,000.00 USD | 116,670.00 USD | 0.00 USD | `+65.66%` | `31.41` |
| `Live` | `Short` | `3725.00` | 649,820,000.00 USD | 483,880.00 USD | 0.00 USD | `+66.11%` | `129.90` |
| `Live` | `Short` | `3735.00` | 650,340,000.00 USD | 523,550.00 USD | 0.00 USD | `+66.56%` | `140.17` |
| `Live` | `Short` | `3745.00` | 651,340,000.00 USD | 997,440.00 USD | 0.00 USD | `+67.00%` | `266.34` |
| `Live` | `Short` | `3755.00` | 651,600,000.00 USD | 263,400.00 USD | 0.00 USD | `+67.45%` | `70.15` |
| `Live` | `Short` | `3765.00` | 653,590,000.00 USD | 1,990,000.00 USD | 0.00 USD | `+67.89%` | `528.00` |
| `Live` | `Short` | `3775.00` | 653,870,000.00 USD | 275,200.00 USD | 0.00 USD | `+68.34%` | `72.90` |
| `Live` | `Short` | `3785.00` | 1,060,000,000.00 USD | 405,370,000.00 USD | 0.00 USD | `+68.78%` | `107,098.41` |
| `Live` | `Short` | `3795.00` | 1,060,000,000.00 USD | 17,510.00 USD | 0.00 USD | `+69.23%` | `4.62` |
| `Live` | `Short` | `3805.00` | 1,070,000,000.00 USD | 5,810,000.00 USD | 0.00 USD | `+69.68%` | `1,526.10` |
| `Live` | `Short` | `3815.00` | 1,070,000,000.00 USD | 2,150.00 USD | 0.00 USD | `+70.12%` | `0.56` |
| `Live` | `Short` | `3825.00` | 1,070,000,000.00 USD | 10,200.00 USD | 0.00 USD | `+70.57%` | `2.67` |
| `Live` | `Short` | `3835.00` | 1,070,000,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+71.01%` | `553.24` |
| `Live` | `Short` | `3845.00` | 1,070,000,000.00 USD | 1,780,000.00 USD | 0.00 USD | `+71.46%` | `463.76` |
| `Live` | `Short` | `3855.00` | 1,070,000,000.00 USD | 93,210.00 USD | 0.00 USD | `+71.91%` | `24.18` |
| `Live` | `Short` | `3865.00` | 1,110,000,000.00 USD | 36,210,000.00 USD | 0.00 USD | `+72.35%` | `9,367.56` |
| `Live` | `Short` | `3875.00` | 1,110,000,000.00 USD | 130,230.00 USD | 0.00 USD | `+72.80%` | `33.61` |
| `Live` | `Short` | `3885.00` | 1,110,000,000.00 USD | 3,300,000.00 USD | 0.00 USD | `+73.24%` | `849.79` |
| `Live` | `Short` | `3895.00` | 1,110,000,000.00 USD | 2,490,000.00 USD | 0.00 USD | `+73.69%` | `640.36` |
| `Live` | `Short` | `3905.00` | 1,110,000,000.00 USD | 1,210,000.00 USD | 0.00 USD | `+74.14%` | `309.91` |
| `Live` | `Short` | `3915.00` | 1,180,000,000.00 USD | 63,500,000.00 USD | 0.00 USD | `+74.58%` | `16,218.98` |
| `Live` | `Short` | `3925.00` | 1,180,000,000.00 USD | 227,870.00 USD | 0.00 USD | `+75.03%` | `58.06` |
| `Live` | `Short` | `3935.00` | 1,180,000,000.00 USD | 5,330.00 USD | 0.00 USD | `+75.47%` | `1.35` |
| `Live` | `Short` | `3945.00` | 1,180,000,000.00 USD | 2,300.00 USD | 0.00 USD | `+75.92%` | `0.58` |
| `Live` | `Short` | `3955.00` | 1,180,000,000.00 USD | 9,170.00 USD | 0.00 USD | `+76.37%` | `2.32` |
| `Live` | `Short` | `3965.00` | 1,180,000,000.00 USD | 704,760.00 USD | 0.00 USD | `+76.81%` | `177.75` |
| `Live` | `Short` | `3975.00` | 1,180,000,000.00 USD | 164,680.00 USD | 0.00 USD | `+77.26%` | `41.43` |
| `Live` | `Short` | `3985.00` | 1,180,000,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+77.70%` | `335.80` |
| `Live` | `Short` | `3995.00` | 1,180,000,000.00 USD | 659,290.00 USD | 0.00 USD | `+78.15%` | `165.03` |
| `Live` | `Short` | `4005.00` | 1,180,000,000.00 USD | 117,770.00 USD | 0.00 USD | `+78.60%` | `29.40` |
| `Live` | `Short` | `4015.00` | 1,180,000,000.00 USD | 71,130.00 USD | 0.00 USD | `+79.04%` | `17.72` |
| `Live` | `Short` | `4025.00` | 1,180,000,000.00 USD | 193,370.00 USD | 0.00 USD | `+79.49%` | `48.04` |
| `Live` | `Short` | `4035.00` | 1,180,000,000.00 USD | 90,590.00 USD | 0.00 USD | `+79.93%` | `22.45` |
| `Live` | `Short` | `4045.00` | 1,180,000,000.00 USD | 94,540.00 USD | 0.00 USD | `+80.38%` | `23.37` |
| `Live` | `Short` | `4055.00` | 1,180,000,000.00 USD | 2,040,000.00 USD | 0.00 USD | `+80.82%` | `503.84` |
| `Live` | `Short` | `4065.00` | 1,180,000,000.00 USD | 258,000.00 USD | 0.00 USD | `+81.27%` | `63.47` |
| `Live` | `Short` | `4075.00` | 1,180,000,000.00 USD | 118,270.00 USD | 0.00 USD | `+81.72%` | `29.02` |
| `Live` | `Short` | `4085.00` | 1,180,000,000.00 USD | 7,110.00 USD | 0.00 USD | `+82.16%` | `1.74` |
| `Live` | `Short` | `4095.00` | 1,180,000,000.00 USD | 487,730.00 USD | 0.00 USD | `+82.61%` | `119.10` |
| `Live` | `Short` | `4105.00` | 1,180,000,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+83.05%` | `521.25` |
| `Live` | `Short` | `4115.00` | 1,180,000,000.00 USD | 3,300.00 USD | 0.00 USD | `+83.50%` | `0.80` |
| `Live` | `Short` | `4125.00` | 1,190,000,000.00 USD | 651,180.00 USD | 0.00 USD | `+83.95%` | `157.86` |
| `Live` | `Short` | `4135.00` | 1,190,000,000.00 USD | 813,500.00 USD | 0.00 USD | `+84.39%` | `196.74` |
| `Live` | `Short` | `4145.00` | 1,190,000,000.00 USD | 1,260,000.00 USD | 0.00 USD | `+84.84%` | `304.52` |
| `Live` | `Short` | `4155.00` | 1,190,000,000.00 USD | 203,830.00 USD | 0.00 USD | `+85.28%` | `49.06` |
| `Live` | `Short` | `4165.00` | 1,190,000,000.00 USD | 373,370.00 USD | 0.00 USD | `+85.73%` | `89.65` |
| `Live` | `Short` | `4175.00` | 1,190,000,000.00 USD | 886,910.00 USD | 0.00 USD | `+86.18%` | `212.43` |
| `Live` | `Short` | `4185.00` | 1,270,000,000.00 USD | 85,130,000.00 USD | 0.00 USD | `+86.62%` | `20,342.54` |
| `Live` | `Short` | `4195.00` | 1,280,000,000.00 USD | 4,080,000.00 USD | 0.00 USD | `+87.07%` | `972.12` |
| `Live` | `Short` | `4205.00` | 1,310,000,000.00 USD | 28,630,000.00 USD | 0.00 USD | `+87.51%` | `6,809.54` |
| `Live` | `Short` | `4215.00` | 1,310,000,000.00 USD | 46,920.00 USD | 0.00 USD | `+87.96%` | `11.13` |
| `Live` | `Short` | `4235.00` | 1,310,000,000.00 USD | 5,290,000.00 USD | 0.00 USD | `+88.85%` | `1,248.32` |
| `Live` | `Short` | `4245.00` | 1,310,000,000.00 USD | 168,620.00 USD | 0.00 USD | `+89.30%` | `39.72` |
| `Live` | `Short` | `4255.00` | 1,310,000,000.00 USD | 36,710.00 USD | 0.00 USD | `+89.74%` | `8.63` |
| `Live` | `Short` | `4265.00` | 1,310,000,000.00 USD | 62,090.00 USD | 0.00 USD | `+90.19%` | `14.56` |
| `Live` | `Short` | `4275.00` | 1,310,000,000.00 USD | 132,310.00 USD | 0.00 USD | `+90.64%` | `30.95` |
| `Live` | `Short` | `4285.00` | 1,310,000,000.00 USD | 2,340.00 USD | 0.00 USD | `+91.08%` | `0.55` |
| `Live` | `Short` | `4295.00` | 1,320,000,000.00 USD | 4,510,000.00 USD | 0.00 USD | `+91.53%` | `1,050.19` |
| `Live` | `Short` | `4305.00` | 1,320,000,000.00 USD | 165,270.00 USD | 0.00 USD | `+91.97%` | `38.39` |
| `Live` | `Short` | `4315.00` | 1,320,000,000.00 USD | 82,370.00 USD | 0.00 USD | `+92.42%` | `19.09` |
| `Live` | `Short` | `4325.00` | 1,600,000,000.00 USD | 279,930,000.00 USD | 0.00 USD | `+92.87%` | `64,724.82` |
| `Live` | `Short` | `4335.00` | 1,600,000,000.00 USD | 533,120.00 USD | 0.00 USD | `+93.31%` | `122.98` |
| `Live` | `Short` | `4345.00` | 1,600,000,000.00 USD | 14,440.00 USD | 0.00 USD | `+93.76%` | `3.32` |
| `Live` | `Short` | `4355.00` | 1,600,000,000.00 USD | 7,030.00 USD | 0.00 USD | `+94.20%` | `1.61` |
| `Live` | `Short` | `4365.00` | 1,600,000,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+94.65%` | `232.07` |
| `Live` | `Short` | `4375.00` | 1,600,000,000.00 USD | 72,940.00 USD | 0.00 USD | `+95.09%` | `16.67` |
| `Live` | `Short` | `4385.00` | 1,600,000,000.00 USD | 216,340.00 USD | 0.00 USD | `+95.54%` | `49.34` |
| `Live` | `Short` | `4395.00` | 1,600,000,000.00 USD | 20,260.00 USD | 0.00 USD | `+95.99%` | `4.61` |
| `Live` | `Short` | `4405.00` | 1,600,000,000.00 USD | 40,640.00 USD | 0.00 USD | `+96.43%` | `9.23` |
| `Live` | `Short` | `4415.00` | 1,600,000,000.00 USD | 45,440.00 USD | 0.00 USD | `+96.88%` | `10.29` |
| `Live` | `Short` | `4425.00` | 1,600,000,000.00 USD | 8,480.00 USD | 0.00 USD | `+97.32%` | `1.92` |
| `Live` | `Short` | `4435.00` | 1,600,000,000.00 USD | 107,760.00 USD | 0.00 USD | `+97.77%` | `24.30` |
| `Live` | `Short` | `4445.00` | 1,600,000,000.00 USD | 106,870.00 USD | 0.00 USD | `+98.22%` | `24.04` |
| `Live` | `Short` | `4455.00` | 1,600,000,000.00 USD | 110,070.00 USD | 0.00 USD | `+98.66%` | `24.71` |
| `Live` | `Short` | `4465.00` | 1,600,000,000.00 USD | 29,380.00 USD | 0.00 USD | `+99.11%` | `6.58` |
| `Live` | `Short` | `4475.00` | 1,600,000,000.00 USD | 424,260.00 USD | 0.00 USD | `+99.55%` | `94.81` |
| `Live` | `Short` | `4485.00` | 1,600,000,000.00 USD | 322,780.00 USD | 0.00 USD | `+100.00%` | `71.97` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `485.00` | 69,140,000.00 USD | 0.00 USD | 278.83 USD | `-78.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `505.00` | 69,140,000.00 USD | 0.00 USD | 15,910.00 USD | `-77.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 69,120,000.00 USD | 0.00 USD | 563.16 USD | `-75.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.00` | 69,120,000.00 USD | 0.00 USD | 583.40 USD | `-71.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.00` | 69,120,000.00 USD | 0.00 USD | 16,690.00 USD | `-70.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.00` | 69,110,000.00 USD | 0.00 USD | 578.54 USD | `-69.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.00` | 69,110,000.00 USD | 0.00 USD | 242.21 USD | `-69.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 69,110,000.00 USD | 0.00 USD | 885.90 USD | `-68.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 69,100,000.00 USD | 0.00 USD | 177.27 USD | `-66.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 69,100,000.00 USD | 0.00 USD | 2,090.00 USD | `-64.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 69,100,000.00 USD | 0.00 USD | 1,670.00 USD | `-62.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 69,100,000.00 USD | 0.00 USD | 139,430.00 USD | `-61.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `875.00` | 68,960,000.00 USD | 0.00 USD | 918.49 USD | `-60.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 68,960,000.00 USD | 0.00 USD | 3,130.00 USD | `-60.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 68,960,000.00 USD | 0.00 USD | 2,780.00 USD | `-59.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 68,950,000.00 USD | 0.00 USD | 516.34 USD | `-56.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 68,950,000.00 USD | 0.00 USD | 100.50 USD | `-55.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 68,950,000.00 USD | 0.00 USD | 223,740.00 USD | `-55.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 68,730,000.00 USD | 0.00 USD | 445.08 USD | `-54.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 68,730,000.00 USD | 0.00 USD | 112.03 USD | `-54.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1045.00` | 68,730,000.00 USD | 0.00 USD | 1,260.00 USD | `-53.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 68,730,000.00 USD | 0.00 USD | 1,060.00 USD | `-52.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 68,730,000.00 USD | 0.00 USD | 995.34 USD | `-52.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 68,730,000.00 USD | 0.00 USD | 1,610.00 USD | `-50.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 68,720,000.00 USD | 0.00 USD | 11,050.00 USD | `-50.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 68,710,000.00 USD | 0.00 USD | 1,320.00 USD | `-49.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 68,710,000.00 USD | 0.00 USD | 1,000.00 USD | `-48.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 68,710,000.00 USD | 0.00 USD | 476.46 USD | `-47.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 68,710,000.00 USD | 0.00 USD | 972.41 USD | `-47.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1195.00` | 68,710,000.00 USD | 0.00 USD | 221.55 USD | `-46.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 68,710,000.00 USD | 0.00 USD | 3,110.00 USD | `-46.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 68,710,000.00 USD | 0.00 USD | 995.93 USD | `-45.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 68,710,000.00 USD | 0.00 USD | 951.93 USD | `-44.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 68,700,000.00 USD | 0.00 USD | 2,290.00 USD | `-44.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 68,700,000.00 USD | 0.00 USD | 9,050.00 USD | `-42.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 68,690,000.00 USD | 0.00 USD | 7,030.00 USD | `-42.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 68,690,000.00 USD | 0.00 USD | 25,040.00 USD | `-41.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 68,660,000.00 USD | 0.00 USD | 1,440.00 USD | `-41.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 68,660,000.00 USD | 0.00 USD | 141,950.00 USD | `-40.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 68,520,000.00 USD | 0.00 USD | 128.86 USD | `-39.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 68,520,000.00 USD | 0.00 USD | 1,270.00 USD | `-39.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 68,520,000.00 USD | 0.00 USD | 4,160.00 USD | `-38.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1385.00` | 68,510,000.00 USD | 0.00 USD | 100,800.00 USD | `-38.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 68,410,000.00 USD | 0.00 USD | 535,600.00 USD | `-37.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 67,880,000.00 USD | 0.00 USD | 18,840.00 USD | `-37.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 67,860,000.00 USD | 0.00 USD | 6,450.00 USD | `-36.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 67,850,000.00 USD | 0.00 USD | 852.10 USD | `-36.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 67,850,000.00 USD | 0.00 USD | 1,610.00 USD | `-35.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 67,850,000.00 USD | 0.00 USD | 5,090.00 USD | `-35.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 67,840,000.00 USD | 0.00 USD | 19,730.00 USD | `-34.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 67,820,000.00 USD | 0.00 USD | 2,600.00 USD | `-34.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 67,820,000.00 USD | 0.00 USD | 19,050.00 USD | `-33.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 67,800,000.00 USD | 0.00 USD | 11,460.00 USD | `-33.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 67,790,000.00 USD | 0.00 USD | 84,170.00 USD | `-32.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 67,710,000.00 USD | 0.00 USD | 11,140.00 USD | `-32.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 67,700,000.00 USD | 0.00 USD | 31,900.00 USD | `-32.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 67,660,000.00 USD | 0.00 USD | 2,090.00 USD | `-31.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 67,660,000.00 USD | 0.00 USD | 960.99 USD | `-31.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 67,660,000.00 USD | 0.00 USD | 58,080.00 USD | `-30.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 67,600,000.00 USD | 0.00 USD | 10,660.00 USD | `-30.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 67,590,000.00 USD | 0.00 USD | 198,620.00 USD | `-29.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 67,390,000.00 USD | 0.00 USD | 4,990.00 USD | `-29.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 67,390,000.00 USD | 0.00 USD | 7,240.00 USD | `-28.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 67,380,000.00 USD | 0.00 USD | 431,660.00 USD | `-28.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 66,950,000.00 USD | 0.00 USD | 25,700.00 USD | `-27.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 66,920,000.00 USD | 0.00 USD | 15,920.00 USD | `-27.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 66,910,000.00 USD | 0.00 USD | 10,560.00 USD | `-27.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 66,900,000.00 USD | 0.00 USD | 323,930.00 USD | `-26.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 66,570,000.00 USD | 0.00 USD | 80,080.00 USD | `-26.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 66,490,000.00 USD | 0.00 USD | 744.09 USD | `-25.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 66,490,000.00 USD | 0.00 USD | 289.27 USD | `-25.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 66,490,000.00 USD | 0.00 USD | 35,320.00 USD | `-24.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 66,460,000.00 USD | 0.00 USD | 42,680.00 USD | `-24.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 66,410,000.00 USD | 0.00 USD | 84,490.00 USD | `-23.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 66,330,000.00 USD | 0.00 USD | 16,350.00 USD | `-23.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 66,310,000.00 USD | 0.00 USD | 47,500.00 USD | `-23.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 66,270,000.00 USD | 0.00 USD | 28,150.00 USD | `-22.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 66,240,000.00 USD | 0.00 USD | 3,180.00 USD | `-22.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 66,230,000.00 USD | 0.00 USD | 466,520.00 USD | `-21.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 65,770,000.00 USD | 0.00 USD | 77,220.00 USD | `-21.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 65,690,000.00 USD | 0.00 USD | 8,070.00 USD | `-20.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 65,680,000.00 USD | 0.00 USD | 8,500.00 USD | `-20.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 65,670,000.00 USD | 0.00 USD | 189,720.00 USD | `-19.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 65,480,000.00 USD | 0.00 USD | 738,880.00 USD | `-19.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 64,750,000.00 USD | 0.00 USD | 262,190.00 USD | `-19.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 64,480,000.00 USD | 0.00 USD | 27,250.00 USD | `-18.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 64,460,000.00 USD | 0.00 USD | 17,460.00 USD | `-18.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 64,440,000.00 USD | 0.00 USD | 31,580.00 USD | `-17.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 64,410,000.00 USD | 0.00 USD | 790,920.00 USD | `-17.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 63,620,000.00 USD | 0.00 USD | 33,750.00 USD | `-16.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 63,580,000.00 USD | 0.00 USD | 18,240,000.00 USD | `-16.39%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 45,340,000.00 USD | 0.00 USD | 20,990.00 USD | `-15.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 45,320,000.00 USD | 0.00 USD | 64,600.00 USD | `-15.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 45,260,000.00 USD | 0.00 USD | 159,840.00 USD | `-15.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 45,100,000.00 USD | 0.00 USD | 98,060.00 USD | `-14.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1925.00` | 45,000,000.00 USD | 0.00 USD | 19,300,000.00 USD | `-14.16%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 25,700,000.00 USD | 0.00 USD | 107,510.00 USD | `-13.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 25,590,000.00 USD | 0.00 USD | 63,130.00 USD | `-13.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 25,530,000.00 USD | 0.00 USD | 63,530.00 USD | `-12.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 25,470,000.00 USD | 0.00 USD | 139,850.00 USD | `-12.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 25,330,000.00 USD | 0.00 USD | 334,160.00 USD | `-11.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 24,990,000.00 USD | 0.00 USD | 99,900.00 USD | `-11.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 24,890,000.00 USD | 0.00 USD | 248,710.00 USD | `-11.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 24,640,000.00 USD | 0.00 USD | 1,800,000.00 USD | `-10.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 22,840,000.00 USD | 0.00 USD | 481,780.00 USD | `-10.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 22,360,000.00 USD | 0.00 USD | 15,390.00 USD | `-9.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 22,340,000.00 USD | 0.00 USD | 311,020.00 USD | `-9.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 22,030,000.00 USD | 0.00 USD | 801,210.00 USD | `-8.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 21,230,000.00 USD | 0.00 USD | 318,040.00 USD | `-8.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 20,910,000.00 USD | 0.00 USD | 134,110.00 USD | `-7.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 20,780,000.00 USD | 0.00 USD | 36,260.00 USD | `-7.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 20,740,000.00 USD | 0.00 USD | 143,690.00 USD | `-7.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 20,600,000.00 USD | 0.00 USD | 29,280.00 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 20,570,000.00 USD | 0.00 USD | 716,620.00 USD | `-6.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 19,850,000.00 USD | 0.00 USD | 165,900.00 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 19,690,000.00 USD | 0.00 USD | 304,460.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 19,380,000.00 USD | 0.00 USD | 608,350.00 USD | `-4.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 18,770,000.00 USD | 0.00 USD | 248,440.00 USD | `-4.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 18,530,000.00 USD | 0.00 USD | 4,740,000.00 USD | `-3.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 13,790,000.00 USD | 0.00 USD | 1,640,000.00 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 12,150,000.00 USD | 0.00 USD | 8,050,000.00 USD | `-3.01%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2185.00` | 4,100,000.00 USD | 0.00 USD | 1,550,000.00 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 2,540,000.00 USD | 0.00 USD | 808,730.00 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 1,730,000.00 USD | 0.00 USD | 346,930.00 USD | `-1.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 1,390,000.00 USD | 0.00 USD | 679,200.00 USD | `-1.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 707,820.00 USD | 0.00 USD | 469,250.00 USD | `-0.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2235.00` | 238,580.00 USD | 0.00 USD | 238,580.00 USD | `-0.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2245.00` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | `+0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2255.00` | 5,440,000.00 USD | 2,590,000.00 USD | 0.00 USD | `+0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2265.00` | 8,350,000.00 USD | 2,910,000.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 9,000,000.00 USD | 650,100.00 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 10,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | `+1.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 10,390,000.00 USD | 249,730.00 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 19,920,000.00 USD | 9,520,000.00 USD | 0.00 USD | `+2.79%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2315.00` | 21,240,000.00 USD | 1,330,000.00 USD | 0.00 USD | `+3.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 21,640,000.00 USD | 399,800.00 USD | 0.00 USD | `+3.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 21,850,000.00 USD | 201,930.00 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 22,820,000.00 USD | 972,770.00 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 24,250,000.00 USD | 1,430,000.00 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 24,540,000.00 USD | 292,460.00 USD | 0.00 USD | `+5.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 24,700,000.00 USD | 161,070.00 USD | 0.00 USD | `+5.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 24,750,000.00 USD | 55,350.00 USD | 0.00 USD | `+6.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 25,910,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+6.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 27,540,000.00 USD | 1,620,000.00 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 27,770,000.00 USD | 238,510.00 USD | 0.00 USD | `+7.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 30,710,000.00 USD | 2,940,000.00 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 30,900,000.00 USD | 188,860.00 USD | 0.00 USD | `+8.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 31,380,000.00 USD | 482,610.00 USD | 0.00 USD | `+9.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2455.00` | 31,530,000.00 USD | 148,310.00 USD | 0.00 USD | `+9.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 33,630,000.00 USD | 2,100,000.00 USD | 0.00 USD | `+9.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 33,820,000.00 USD | 188,440.00 USD | 0.00 USD | `+10.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 35,930,000.00 USD | 2,110,000.00 USD | 0.00 USD | `+10.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 36,340,000.00 USD | 411,640.00 USD | 0.00 USD | `+11.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 41,230,000.00 USD | 4,890,000.00 USD | 0.00 USD | `+11.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2515.00` | 48,150,000.00 USD | 6,920,000.00 USD | 0.00 USD | `+12.15%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 51,200,000.00 USD | 3,050,000.00 USD | 0.00 USD | `+12.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 51,270,000.00 USD | 64,370.00 USD | 0.00 USD | `+13.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 53,460,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+13.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 53,700,000.00 USD | 235,090.00 USD | 0.00 USD | `+13.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 56,800,000.00 USD | 3,110,000.00 USD | 0.00 USD | `+14.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 56,890,000.00 USD | 80,760.00 USD | 0.00 USD | `+14.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 59,590,000.00 USD | 2,700,000.00 USD | 0.00 USD | `+15.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 59,600,000.00 USD | 10,500.00 USD | 0.00 USD | `+15.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 62,460,000.00 USD | 2,860,000.00 USD | 0.00 USD | `+16.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 62,550,000.00 USD | 93,420.00 USD | 0.00 USD | `+16.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 64,740,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+17.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 64,880,000.00 USD | 148,510.00 USD | 0.00 USD | `+17.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 67,010,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+17.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 67,330,000.00 USD | 318,690.00 USD | 0.00 USD | `+18.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 69,470,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+18.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 69,680,000.00 USD | 208,460.00 USD | 0.00 USD | `+19.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 71,850,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+19.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 71,930,000.00 USD | 76,240.00 USD | 0.00 USD | `+20.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 76,940,000.00 USD | 5,010,000.00 USD | 0.00 USD | `+20.62%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2715.00` | 77,010,000.00 USD | 76,900.00 USD | 0.00 USD | `+21.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 79,480,000.00 USD | 2,470,000.00 USD | 0.00 USD | `+21.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 79,520,000.00 USD | 43,050.00 USD | 0.00 USD | `+21.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 81,890,000.00 USD | 2,370,000.00 USD | 0.00 USD | `+22.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 82,580,000.00 USD | 684,550.00 USD | 0.00 USD | `+22.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 84,920,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+23.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 85,490,000.00 USD | 577,610.00 USD | 0.00 USD | `+23.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 87,760,000.00 USD | 2,260,000.00 USD | 0.00 USD | `+24.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 87,770,000.00 USD | 17,550.00 USD | 0.00 USD | `+24.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 90,910,000.00 USD | 3,130,000.00 USD | 0.00 USD | `+25.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 90,960,000.00 USD | 52,490.00 USD | 0.00 USD | `+25.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 91,000,000.00 USD | 43,930.00 USD | 0.00 USD | `+25.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 91,290,000.00 USD | 286,140.00 USD | 0.00 USD | `+26.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 92,290,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+26.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 93,560,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+27.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 93,570,000.00 USD | 10,470.00 USD | 0.00 USD | `+27.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 93,580,000.00 USD | 2,460.00 USD | 0.00 USD | `+28.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 93,880,000.00 USD | 305,820.00 USD | 0.00 USD | `+28.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 93,900,000.00 USD | 16,190.00 USD | 0.00 USD | `+29.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 95,380,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+29.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 95,390,000.00 USD | 10,340.00 USD | 0.00 USD | `+29.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 95,400,000.00 USD | 3,050.00 USD | 0.00 USD | `+30.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 95,450,000.00 USD | 52,370.00 USD | 0.00 USD | `+30.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 95,480,000.00 USD | 34,650.00 USD | 0.00 USD | `+31.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 95,530,000.00 USD | 43,460.00 USD | 0.00 USD | `+31.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 95,640,000.00 USD | 113,340.00 USD | 0.00 USD | `+32.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 95,790,000.00 USD | 145,510.00 USD | 0.00 USD | `+32.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 95,960,000.00 USD | 177,120.00 USD | 0.00 USD | `+33.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 100,880,000.00 USD | 4,920,000.00 USD | 0.00 USD | `+33.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 103,900,000.00 USD | 3,010,000.00 USD | 0.00 USD | `+34.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 103,900,000.00 USD | 6,950.00 USD | 0.00 USD | `+34.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 103,940,000.00 USD | 35,380.00 USD | 0.00 USD | `+34.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 104,010,000.00 USD | 74,910.00 USD | 0.00 USD | `+35.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 104,040,000.00 USD | 22,460.00 USD | 0.00 USD | `+35.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 104,810,000.00 USD | 771,720.00 USD | 0.00 USD | `+36.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 104,810,000.00 USD | 612.69 USD | 0.00 USD | `+36.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 104,860,000.00 USD | 49,500.00 USD | 0.00 USD | `+37.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 104,880,000.00 USD | 19,570.00 USD | 0.00 USD | `+37.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 104,880,000.00 USD | 928.50 USD | 0.00 USD | `+38.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 116,830,000.00 USD | 11,950,000.00 USD | 0.00 USD | `+38.46%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 116,940,000.00 USD | 111,160.00 USD | 0.00 USD | `+38.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 117,330,000.00 USD | 381,020.00 USD | 0.00 USD | `+39.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 117,330,000.00 USD | 2,660.00 USD | 0.00 USD | `+40.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 117,390,000.00 USD | 58,930.00 USD | 0.00 USD | `+40.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 117,400,000.00 USD | 9,860.00 USD | 0.00 USD | `+41.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 117,400,000.00 USD | 149.22 USD | 0.00 USD | `+41.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 117,400,000.00 USD | 1,330.00 USD | 0.00 USD | `+42.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 117,440,000.00 USD | 41,120.00 USD | 0.00 USD | `+42.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 118,100,000.00 USD | 661,330.00 USD | 0.00 USD | `+42.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 118,100,000.00 USD | 1,760.00 USD | 0.00 USD | `+43.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 118,110,000.00 USD | 3,740.00 USD | 0.00 USD | `+43.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 118,110,000.00 USD | 167.25 USD | 0.00 USD | `+44.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 118,160,000.00 USD | 56,110.00 USD | 0.00 USD | `+44.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 118,400,000.00 USD | 236,580.00 USD | 0.00 USD | `+45.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 118,420,000.00 USD | 15,710.00 USD | 0.00 USD | `+45.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 118,420,000.00 USD | 1,630.00 USD | 0.00 USD | `+46.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 118,560,000.00 USD | 141,980.00 USD | 0.00 USD | `+46.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 118,570,000.00 USD | 15,350.00 USD | 0.00 USD | `+46.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 119,990,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+47.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 120,380,000.00 USD | 389,970.00 USD | 0.00 USD | `+47.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 120,400,000.00 USD | 18,270.00 USD | 0.00 USD | `+48.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 120,400,000.00 USD | 4,350.00 USD | 0.00 USD | `+48.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 120,400,000.00 USD | 2,170.00 USD | 0.00 USD | `+49.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 120,400,000.00 USD | 837.74 USD | 0.00 USD | `+49.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 120,410,000.00 USD | 2,780.00 USD | 0.00 USD | `+50.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 120,430,000.00 USD | 21,260.00 USD | 0.00 USD | `+50.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 120,490,000.00 USD | 58,010.00 USD | 0.00 USD | `+50.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 120,810,000.00 USD | 322,160.00 USD | 0.00 USD | `+51.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 122,300,000.00 USD | 1,490,000.00 USD | 0.00 USD | `+51.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 122,310,000.00 USD | 5,700.00 USD | 0.00 USD | `+52.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 122,320,000.00 USD | 16,310.00 USD | 0.00 USD | `+52.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 122,340,000.00 USD | 15,030.00 USD | 0.00 USD | `+53.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 122,360,000.00 USD | 18,600.00 USD | 0.00 USD | `+54.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 122,360,000.00 USD | 495.50 USD | 0.00 USD | `+54.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 122,360,000.00 USD | 3,190.00 USD | 0.00 USD | `+54.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 122,400,000.00 USD | 43,610.00 USD | 0.00 USD | `+55.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 122,400,000.00 USD | 158.32 USD | 0.00 USD | `+55.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 122,850,000.00 USD | 444,280.00 USD | 0.00 USD | `+56.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 122,890,000.00 USD | 43,620.00 USD | 0.00 USD | `+56.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 122,890,000.00 USD | 3,690.00 USD | 0.00 USD | `+57.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 122,900,000.00 USD | 9,810.00 USD | 0.00 USD | `+57.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 122,990,000.00 USD | 90,810.00 USD | 0.00 USD | `+58.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 123,000,000.00 USD | 2,300.00 USD | 0.00 USD | `+58.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3575.00` | 123,000,000.00 USD | 2,870.00 USD | 0.00 USD | `+59.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 123,000,000.00 USD | 354.92 USD | 0.00 USD | `+59.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 123,010,000.00 USD | 13,160.00 USD | 0.00 USD | `+60.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 123,110,000.00 USD | 101,080.00 USD | 0.00 USD | `+60.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 123,120,000.00 USD | 10,210.00 USD | 0.00 USD | `+61.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 123,130,000.00 USD | 7,790.00 USD | 0.00 USD | `+62.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 123,140,000.00 USD | 3,860.00 USD | 0.00 USD | `+62.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 123,140,000.00 USD | 8,090.00 USD | 0.00 USD | `+62.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 123,150,000.00 USD | 8,130.00 USD | 0.00 USD | `+63.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 123,210,000.00 USD | 55,120.00 USD | 0.00 USD | `+63.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 123,210,000.00 USD | 1,410.00 USD | 0.00 USD | `+64.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 123,210,000.00 USD | 819.92 USD | 0.00 USD | `+65.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 123,210,000.00 USD | 323.58 USD | 0.00 USD | `+65.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 123,210,000.00 USD | 1,400.00 USD | 0.00 USD | `+66.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 123,220,000.00 USD | 6,490.00 USD | 0.00 USD | `+66.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3745.00` | 123,220,000.00 USD | 165.90 USD | 0.00 USD | `+67.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 123,220,000.00 USD | 751.00 USD | 0.00 USD | `+67.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 123,220,000.00 USD | 286.90 USD | 0.00 USD | `+68.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 123,220,000.00 USD | 1,560.00 USD | 0.00 USD | `+69.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 123,960,000.00 USD | 734,530.00 USD | 0.00 USD | `+69.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 123,980,000.00 USD | 20,930.00 USD | 0.00 USD | `+70.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 123,980,000.00 USD | 8,380.00 USD | 0.00 USD | `+70.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 123,990,000.00 USD | 711.78 USD | 0.00 USD | `+71.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 123,990,000.00 USD | 355.28 USD | 0.00 USD | `+71.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 123,990,000.00 USD | 5,170.00 USD | 0.00 USD | `+71.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 124,010,000.00 USD | 19,430.00 USD | 0.00 USD | `+73.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 124,020,000.00 USD | 12,120.00 USD | 0.00 USD | `+74.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 124,670,000.00 USD | 646,840.00 USD | 0.00 USD | `+74.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 124,710,000.00 USD | 42,570.00 USD | 0.00 USD | `+75.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 124,770,000.00 USD | 59,170.00 USD | 0.00 USD | `+75.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 124,770,000.00 USD | 1,380.00 USD | 0.00 USD | `+76.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 124,780,000.00 USD | 6,960.00 USD | 0.00 USD | `+77.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 124,790,000.00 USD | 14,610.00 USD | 0.00 USD | `+77.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 124,800,000.00 USD | 4,280.00 USD | 0.00 USD | `+78.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 127,550,000.00 USD | 2,750,000.00 USD | 0.00 USD | `+78.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 127,550,000.00 USD | 898.59 USD | 0.00 USD | `+79.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 127,550,000.00 USD | 811.00 USD | 0.00 USD | `+80.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 127,550,000.00 USD | 4,310.00 USD | 0.00 USD | `+81.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 127,560,000.00 USD | 3,050.00 USD | 0.00 USD | `+82.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 127,590,000.00 USD | 36,740.00 USD | 0.00 USD | `+83.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 127,600,000.00 USD | 5,990.00 USD | 0.00 USD | `+83.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 127,600,000.00 USD | 372.90 USD | 0.00 USD | `+83.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 127,600,000.00 USD | 395.43 USD | 0.00 USD | `+84.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 127,600,000.00 USD | 376.65 USD | 0.00 USD | `+86.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 127,640,000.00 USD | 42,260.00 USD | 0.00 USD | `+87.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 127,640,000.00 USD | 460.70 USD | 0.00 USD | `+87.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 127,650,000.00 USD | 1,270.00 USD | 0.00 USD | `+88.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 127,650,000.00 USD | 4,300.00 USD | 0.00 USD | `+89.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 127,650,000.00 USD | 437.16 USD | 0.00 USD | `+90.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 127,720,000.00 USD | 64,550.00 USD | 0.00 USD | `+90.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 127,720,000.00 USD | 1,610.00 USD | 0.00 USD | `+91.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 127,810,000.00 USD | 97,670.00 USD | 0.00 USD | `+91.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 127,820,000.00 USD | 1,070.00 USD | 0.00 USD | `+92.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 127,830,000.00 USD | 11,270.00 USD | 0.00 USD | `+93.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 127,830,000.00 USD | 2,400.00 USD | 0.00 USD | `+94.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 127,870,000.00 USD | 43,750.00 USD | 0.00 USD | `+95.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 127,940,000.00 USD | 64,570.00 USD | 0.00 USD | `+95.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 127,940,000.00 USD | 1,050.00 USD | 0.00 USD | `+95.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 128,210,000.00 USD | 269,710.00 USD | 0.00 USD | `+96.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 128,220,000.00 USD | 11,480.00 USD | 0.00 USD | `+96.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 128,220,000.00 USD | 2,510.00 USD | 0.00 USD | `+97.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 128,400,000.00 USD | 177,400.00 USD | 0.00 USD | `+97.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 128,400,000.00 USD | 2,040.00 USD | 0.00 USD | `+98.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4465.00` | 128,400,000.00 USD | 1,030.00 USD | 0.00 USD | `+99.11%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1972.00` | 1,010,000,000.00 USD | 0.00 USD | 1,010,000,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD |
| `7D` | `1975.30` | 1,010,000,000.00 USD | 0.00 USD | 1,010,000,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD |
| `7D` | `1978.60` | 1,010,000,000.00 USD | 0.00 USD | 1,010,000,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1981.90` | 1,010,000,000.00 USD | 0.00 USD | 1,010,000,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD |
| `7D` | `1988.50` | 1,010,000,000.00 USD | 0.00 USD | 1,010,000,000.00 USD | 3,730,000.00 USD | 1,780,000.00 USD | 0.00 USD |
| `1D` | `1988.60` | 676,050,000.00 USD | 0.00 USD | 676,050,000.00 USD | 1,210,000.00 USD | 1,370,000.00 USD | 374,980.00 USD |
| `1D` | `1991.10` | 673,090,000.00 USD | 0.00 USD | 673,090,000.00 USD | 1,580,000.00 USD | 0.00 USD | 438,380.00 USD |
| `7D` | `1991.80` | 1,000,000,000.00 USD | 0.00 USD | 1,000,000,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 38,060.00 USD |
| `1D` | `1993.60` | 671,070,000.00 USD | 0.00 USD | 671,070,000.00 USD | 202,370.00 USD | 596,570.00 USD | 21,590.00 USD |
| `7D` | `1995.10` | 999,730,000.00 USD | 0.00 USD | 999,730,000.00 USD | 1,340,000.00 USD | 0.00 USD | 808,380.00 USD |
| `1D` | `1996.10` | 670,250,000.00 USD | 0.00 USD | 670,250,000.00 USD | 412,250.00 USD | 61,370.00 USD | 304,820.00 USD |
| `1D` | `2001.10` | 669,470,000.00 USD | 0.00 USD | 669,470,000.00 USD | 0.00 USD | 18,870.00 USD | 487,740.00 USD |
| `1D` | `2003.60` | 668,960,000.00 USD | 0.00 USD | 668,960,000.00 USD | 0.00 USD | 198,200.00 USD | 0.00 USD |
| `7D` | `2005.00` | 997,580,000.00 USD | 0.00 USD | 997,580,000.00 USD | 0.00 USD | 266,430.00 USD | 0.00 USD |
| `1D` | `2006.10` | 668,770,000.00 USD | 0.00 USD | 668,770,000.00 USD | 14,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2008.60` | 668,750,000.00 USD | 0.00 USD | 668,750,000.00 USD | 0.00 USD | 224,500.00 USD | 0.00 USD |
| `1D` | `2011.10` | 668,530,000.00 USD | 0.00 USD | 668,530,000.00 USD | 48,560.00 USD | 320,230.00 USD | 0.00 USD |
| `7D` | `2011.60` | 997,320,000.00 USD | 0.00 USD | 997,320,000.00 USD | 170,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2013.60` | 668,160,000.00 USD | 0.00 USD | 668,160,000.00 USD | 250,530.00 USD | 229,750.00 USD | 17,710.00 USD |
| `1D` | `2016.10` | 667,660,000.00 USD | 0.00 USD | 667,660,000.00 USD | 330,880.00 USD | 497,090.00 USD | 0.00 USD |
| `1D` | `2018.60` | 666,830,000.00 USD | 0.00 USD | 666,830,000.00 USD | 737,290.00 USD | 1,100,000.00 USD | 714,280.00 USD |
| `1D` | `2021.10` | 664,270,000.00 USD | 0.00 USD | 664,270,000.00 USD | 973,110.00 USD | 952,000.00 USD | 794,390.00 USD |
| `1D` | `2023.60` | 661,560,000.00 USD | 0.00 USD | 661,560,000.00 USD | 0.00 USD | 0.00 USD | 323,080.00 USD |
| `7D` | `2024.80` | 997,140,000.00 USD | 0.00 USD | 997,140,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2026.10` | 661,230,000.00 USD | 0.00 USD | 661,230,000.00 USD | 0.00 USD | 1,100,000.00 USD | 28,770.00 USD |
| `7D` | `2028.10` | 996,970,000.00 USD | 0.00 USD | 996,970,000.00 USD | 0.00 USD | 0.00 USD | 35,180.00 USD |
| `1D` | `2028.60` | 660,100,000.00 USD | 0.00 USD | 660,100,000.00 USD | 1,430,000.00 USD | 1,210,000.00 USD | 598,090.00 USD |
| `1D` | `2031.10` | 656,870,000.00 USD | 0.00 USD | 656,870,000.00 USD | 677,540.00 USD | 293,350.00 USD | 1,080,000.00 USD |
| `7D` | `2031.40` | 996,930,000.00 USD | 0.00 USD | 996,930,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD |
| `1D` | `2033.60` | 654,820,000.00 USD | 0.00 USD | 654,820,000.00 USD | 941,100.00 USD | 1,330,000.00 USD | 0.00 USD |
| `7D` | `2034.70` | 992,370,000.00 USD | 0.00 USD | 992,370,000.00 USD | 0.00 USD | 186,130.00 USD | 1,350,000.00 USD |
| `1D` | `2036.10` | 652,550,000.00 USD | 0.00 USD | 652,550,000.00 USD | 985,830.00 USD | 159,790.00 USD | 176,820.00 USD |
| `7D` | `2038.00` | 990,820,000.00 USD | 0.00 USD | 990,820,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2038.60` | 651,230,000.00 USD | 0.00 USD | 651,230,000.00 USD | 939,380.00 USD | 317,820.00 USD | 377,350.00 USD |
| `1D` | `2041.10` | 649,590,000.00 USD | 0.00 USD | 649,590,000.00 USD | 626,840.00 USD | 178,560.00 USD | 176,570.00 USD |
| `1D` | `2043.60` | 648,610,000.00 USD | 0.00 USD | 648,610,000.00 USD | 0.00 USD | 0.00 USD | 28,960.00 USD |
| `7D` | `2044.60` | 989,220,000.00 USD | 0.00 USD | 989,220,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD |
| `1D` | `2046.10` | 648,580,000.00 USD | 0.00 USD | 648,580,000.00 USD | 0.00 USD | 0.00 USD | 19,040.00 USD |
| `1D` | `2048.60` | 648,560,000.00 USD | 0.00 USD | 648,560,000.00 USD | 518,440.00 USD | 0.00 USD | 357,950.00 USD |
| `1D` | `2051.10` | 647,690,000.00 USD | 0.00 USD | 647,690,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2051.20` | 988,920,000.00 USD | 0.00 USD | 988,920,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2053.60` | 646,630,000.00 USD | 0.00 USD | 646,630,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD |
| `7D` | `2054.50` | 988,700,000.00 USD | 0.00 USD | 988,700,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2056.10` | 646,510,000.00 USD | 0.00 USD | 646,510,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2057.80` | 986,420,000.00 USD | 0.00 USD | 986,420,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2058.60` | 646,270,000.00 USD | 0.00 USD | 646,270,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `1D` | `2061.10` | 645,520,000.00 USD | 0.00 USD | 645,520,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD |
| `7D` | `2061.10` | 986,360,000.00 USD | 0.00 USD | 986,360,000.00 USD | 1,700,000.00 USD | 1,310,000.00 USD | 1,710,000.00 USD |
| `1D` | `2063.60` | 645,440,000.00 USD | 0.00 USD | 645,440,000.00 USD | 563,140.00 USD | 494,150.00 USD | 510,200.00 USD |
| `7D` | `2064.40` | 981,640,000.00 USD | 0.00 USD | 981,640,000.00 USD | 1,230,000.00 USD | 1,080,000.00 USD | 945,860.00 USD |
| `1D` | `2066.10` | 643,870,000.00 USD | 0.00 USD | 643,870,000.00 USD | 387,410.00 USD | 42,880.00 USD | 0.00 USD |
| `7D` | `2067.70` | 978,390,000.00 USD | 0.00 USD | 978,390,000.00 USD | 292,400.00 USD | 1,180,000.00 USD | 927,620.00 USD |
| `1D` | `2068.60` | 643,440,000.00 USD | 0.00 USD | 643,440,000.00 USD | 57,300.00 USD | 624,040.00 USD | 0.00 USD |
| `7D` | `2071.00` | 975,980,000.00 USD | 0.00 USD | 975,980,000.00 USD | 4,230,000.00 USD | 3,040,000.00 USD | 1,230,000.00 USD |
| `1D` | `2071.10` | 642,760,000.00 USD | 0.00 USD | 642,760,000.00 USD | 47,910.00 USD | 534,600.00 USD | 0.00 USD |
| `1D` | `2073.60` | 642,180,000.00 USD | 0.00 USD | 642,180,000.00 USD | 65,350.00 USD | 20,640.00 USD | 428,640.00 USD |
| `7D` | `2074.30` | 967,480,000.00 USD | 0.00 USD | 967,480,000.00 USD | 4,000,000.00 USD | 2,720,000.00 USD | 3,720,000.00 USD |
| `1D` | `2076.10` | 641,660,000.00 USD | 0.00 USD | 641,660,000.00 USD | 574,450.00 USD | 398,450.00 USD | 178,780.00 USD |
| `7D` | `2077.60` | 957,040,000.00 USD | 0.00 USD | 957,040,000.00 USD | 4,430,000.00 USD | 4,400,000.00 USD | 2,270,000.00 USD |
| `1D` | `2078.60` | 640,510,000.00 USD | 0.00 USD | 640,510,000.00 USD | 1,040,000.00 USD | 738,020.00 USD | 526,420.00 USD |
| `7D` | `2080.90` | 945,940,000.00 USD | 0.00 USD | 945,940,000.00 USD | 5,690,000.00 USD | 3,540,000.00 USD | 2,980,000.00 USD |
| `1D` | `2081.10` | 638,210,000.00 USD | 0.00 USD | 638,210,000.00 USD | 926,700.00 USD | 785,280.00 USD | 222,010.00 USD |
| `1D` | `2083.60` | 636,270,000.00 USD | 0.00 USD | 636,270,000.00 USD | 1,330,000.00 USD | 896,260.00 USD | 293,380.00 USD |
| `7D` | `2084.20` | 933,730,000.00 USD | 0.00 USD | 933,730,000.00 USD | 1,660,000.00 USD | 1,490,000.00 USD | 3,500,000.00 USD |
| `1D` | `2086.10` | 633,760,000.00 USD | 0.00 USD | 633,760,000.00 USD | 767,520.00 USD | 475,350.00 USD | 1,450,000.00 USD |
| `7D` | `2087.50` | 927,090,000.00 USD | 0.00 USD | 927,090,000.00 USD | 5,220,000.00 USD | 3,230,000.00 USD | 3,060,000.00 USD |
| `1D` | `2088.60` | 631,070,000.00 USD | 0.00 USD | 631,070,000.00 USD | 1,270,000.00 USD | 417,850.00 USD | 216,910.00 USD |
| `7D` | `2090.80` | 915,580,000.00 USD | 0.00 USD | 915,580,000.00 USD | 4,410,000.00 USD | 976,840.00 USD | 6,980,000.00 USD |
| `1D` | `2091.10` | 629,160,000.00 USD | 0.00 USD | 629,160,000.00 USD | 1,250,000.00 USD | 302,520.00 USD | 547,370.00 USD |
| `1D` | `2093.60` | 627,070,000.00 USD | 0.00 USD | 627,070,000.00 USD | 1,240,000.00 USD | 595,640.00 USD | 699,120.00 USD |
| `7D` | `2094.10` | 903,220,000.00 USD | 0.00 USD | 903,220,000.00 USD | 5,350,000.00 USD | 1,660,000.00 USD | 2,950,000.00 USD |
| `1D` | `2096.10` | 624,530,000.00 USD | 0.00 USD | 624,530,000.00 USD | 1,190,000.00 USD | 1,190,000.00 USD | 1,360,000.00 USD |
| `7D` | `2097.40` | 893,260,000.00 USD | 0.00 USD | 893,260,000.00 USD | 2,280,000.00 USD | 3,580,000.00 USD | 1,290,000.00 USD |
| `1D` | `2098.60` | 620,790,000.00 USD | 0.00 USD | 620,790,000.00 USD | 296,850.00 USD | 1,460,000.00 USD | 248,570.00 USD |
| `7D` | `2100.70` | 886,110,000.00 USD | 0.00 USD | 886,110,000.00 USD | 1,830,000.00 USD | 1,850,000.00 USD | 3,310,000.00 USD |
| `1D` | `2101.10` | 618,780,000.00 USD | 0.00 USD | 618,780,000.00 USD | 145,240.00 USD | 353,390.00 USD | 231,410.00 USD |
| `1D` | `2103.60` | 618,050,000.00 USD | 0.00 USD | 618,050,000.00 USD | 268,400.00 USD | 297,810.00 USD | 306,410.00 USD |
| `7D` | `2104.00` | 879,120,000.00 USD | 0.00 USD | 879,120,000.00 USD | 1,190,000.00 USD | 738,240.00 USD | 3,030,000.00 USD |
| `1D` | `2106.10` | 617,180,000.00 USD | 0.00 USD | 617,180,000.00 USD | 3,610,000.00 USD | 980,320.00 USD | 1,180,000.00 USD |
| `7D` | `2107.30` | 874,160,000.00 USD | 0.00 USD | 874,160,000.00 USD | 8,720,000.00 USD | 1,150,000.00 USD | 1,190,000.00 USD |
| `1D` | `2108.60` | 611,410,000.00 USD | 0.00 USD | 611,410,000.00 USD | 656,240.00 USD | 21,400.00 USD | 6,190.00 USD |
| `7D` | `2110.60` | 863,100,000.00 USD | 0.00 USD | 863,100,000.00 USD | 2,970,000.00 USD | 2,360,000.00 USD | 2,530,000.00 USD |
| `1D` | `2111.10` | 610,730,000.00 USD | 0.00 USD | 610,730,000.00 USD | 450,470.00 USD | 81,050.00 USD | 0.00 USD |
| `1D` | `2113.60` | 610,200,000.00 USD | 0.00 USD | 610,200,000.00 USD | 452,130.00 USD | 520,660.00 USD | 249,040.00 USD |
| `7D` | `2113.90` | 855,240,000.00 USD | 0.00 USD | 855,240,000.00 USD | 1,780,000.00 USD | 1,810,000.00 USD | 3,580,000.00 USD |
| `1D` | `2116.10` | 608,980,000.00 USD | 0.00 USD | 608,980,000.00 USD | 1,130,000.00 USD | 1,180,000.00 USD | 935,080.00 USD |
| `7D` | `2117.20` | 848,060,000.00 USD | 0.00 USD | 848,060,000.00 USD | 2,410,000.00 USD | 2,380,000.00 USD | 2,470,000.00 USD |
| `1D` | `2118.60` | 605,730,000.00 USD | 0.00 USD | 605,730,000.00 USD | 5,240,000.00 USD | 3,070,000.00 USD | 888,380.00 USD |
| `7D` | `2120.50` | 840,800,000.00 USD | 0.00 USD | 840,800,000.00 USD | 13,880,000.00 USD | 5,790,000.00 USD | 2,800,000.00 USD |
| `1D` | `2121.10` | 596,530,000.00 USD | 0.00 USD | 596,530,000.00 USD | 4,600,000.00 USD | 2,330,000.00 USD | 920,270.00 USD |
| `1D` | `2123.60` | 588,670,000.00 USD | 0.00 USD | 588,670,000.00 USD | 8,080,000.00 USD | 2,950,000.00 USD | 2,310,000.00 USD |
| `7D` | `2123.80` | 818,330,000.00 USD | 0.00 USD | 818,330,000.00 USD | 7,610,000.00 USD | 7,900,000.00 USD | 1,820,000.00 USD |
| `1D` | `2126.10` | 575,340,000.00 USD | 0.00 USD | 575,340,000.00 USD | 3,480,000.00 USD | 2,840,000.00 USD | 837,670.00 USD |
| `7D` | `2127.10` | 801,000,000.00 USD | 0.00 USD | 801,000,000.00 USD | 2,760,000.00 USD | 4,420,000.00 USD | 5,540,000.00 USD |
| `1D` | `2128.60` | 568,180,000.00 USD | 0.00 USD | 568,180,000.00 USD | 3,180,000.00 USD | 1,860,000.00 USD | 1,510,000.00 USD |
| `7D` | `2130.40` | 788,280,000.00 USD | 0.00 USD | 788,280,000.00 USD | 5,410,000.00 USD | 2,580,000.00 USD | 1,690,000.00 USD |
| `1D` | `2131.10` | 561,620,000.00 USD | 0.00 USD | 561,620,000.00 USD | 296,080.00 USD | 196,420.00 USD | 344,350.00 USD |
| `1D` | `2133.60` | 560,790,000.00 USD | 0.00 USD | 560,790,000.00 USD | 20,600.00 USD | 460,010.00 USD | 1,280,000.00 USD |
| `7D` | `2133.70` | 778,600,000.00 USD | 0.00 USD | 778,600,000.00 USD | 2,550,000.00 USD | 715,940.00 USD | 323,430.00 USD |
| `1D` | `2136.10` | 559,020,000.00 USD | 0.00 USD | 559,020,000.00 USD | 21,090.00 USD | 958,750.00 USD | 0.00 USD |
| `7D` | `2137.00` | 775,010,000.00 USD | 0.00 USD | 775,010,000.00 USD | 746,340.00 USD | 1,510,000.00 USD | 43,560.00 USD |
| `1D` | `2138.60` | 558,040,000.00 USD | 0.00 USD | 558,040,000.00 USD | 36,740.00 USD | 142,010.00 USD | 64,360.00 USD |
| `7D` | `2140.30` | 772,710,000.00 USD | 0.00 USD | 772,710,000.00 USD | 2,260,000.00 USD | 1,200,000.00 USD | 801,910.00 USD |
| `1D` | `2141.10` | 557,800,000.00 USD | 0.00 USD | 557,800,000.00 USD | 130,510.00 USD | 830,230.00 USD | 0.00 USD |
| `1D` | `2143.60` | 556,840,000.00 USD | 0.00 USD | 556,840,000.00 USD | 539,840.00 USD | 2,100,000.00 USD | 17,490.00 USD |
| `7D` | `2143.60` | 768,440,000.00 USD | 0.00 USD | 768,440,000.00 USD | 1,200,000.00 USD | 1,420,000.00 USD | 268,500.00 USD |
| `1D` | `2146.10` | 554,180,000.00 USD | 0.00 USD | 554,180,000.00 USD | 1,360,000.00 USD | 1,750,000.00 USD | 124,070.00 USD |
| `7D` | `2146.90` | 765,560,000.00 USD | 0.00 USD | 765,560,000.00 USD | 1,060,000.00 USD | 938,520.00 USD | 134,420.00 USD |
| `1D` | `2148.60` | 550,950,000.00 USD | 0.00 USD | 550,950,000.00 USD | 6,260,000.00 USD | 1,490,000.00 USD | 1,360,000.00 USD |
| `7D` | `2150.20` | 763,420,000.00 USD | 0.00 USD | 763,420,000.00 USD | 485,890.00 USD | 838,260.00 USD | 331,330.00 USD |
| `1D` | `2151.10` | 541,840,000.00 USD | 0.00 USD | 541,840,000.00 USD | 3,200,000.00 USD | 2,580,000.00 USD | 359,110.00 USD |
| `7D` | `2153.50` | 761,770,000.00 USD | 0.00 USD | 761,770,000.00 USD | 11,310,000.00 USD | 311,060.00 USD | 0.00 USD |
| `1D` | `2153.60` | 535,710,000.00 USD | 0.00 USD | 535,710,000.00 USD | 830,850.00 USD | 2,460,000.00 USD | 2,010,000.00 USD |
| `1D` | `2156.10` | 530,410,000.00 USD | 0.00 USD | 530,410,000.00 USD | 3,780,000.00 USD | 2,720,000.00 USD | 2,340,000.00 USD |
| `7D` | `2156.80` | 750,150,000.00 USD | 0.00 USD | 750,150,000.00 USD | 2,560,000.00 USD | 2,010,000.00 USD | 3,200,000.00 USD |
| `1D` | `2158.60` | 521,570,000.00 USD | 0.00 USD | 521,570,000.00 USD | 774,060.00 USD | 1,020,000.00 USD | 2,240,000.00 USD |
| `7D` | `2160.10` | 742,370,000.00 USD | 0.00 USD | 742,370,000.00 USD | 2,190,000.00 USD | 2,550,000.00 USD | 1,270,000.00 USD |
| `1D` | `2161.10` | 517,540,000.00 USD | 0.00 USD | 517,540,000.00 USD | 6,010,000.00 USD | 7,640,000.00 USD | 549,880.00 USD |
| `7D` | `2163.40` | 736,370,000.00 USD | 0.00 USD | 736,370,000.00 USD | 21,210,000.00 USD | 11,130,000.00 USD | 518,640.00 USD |
| `1D` | `2163.60` | 503,340,000.00 USD | 0.00 USD | 503,340,000.00 USD | 12,520,000.00 USD | 8,970,000.00 USD | 3,010,000.00 USD |
| `1D` | `2166.10` | 478,840,000.00 USD | 0.00 USD | 478,840,000.00 USD | 11,060,000.00 USD | 12,030,000.00 USD | 5,730,000.00 USD |
| `7D` | `2166.70` | 703,510,000.00 USD | 0.00 USD | 703,510,000.00 USD | 5,300,000.00 USD | 15,400,000.00 USD | 2,970,000.00 USD |
| `1D` | `2168.60` | 450,010,000.00 USD | 0.00 USD | 450,010,000.00 USD | 17,790,000.00 USD | 6,160,000.00 USD | 3,750,000.00 USD |
| `7D` | `2170.00` | 679,840,000.00 USD | 0.00 USD | 679,840,000.00 USD | 10,280,000.00 USD | 15,310,000.00 USD | 5,480,000.00 USD |
| `1D` | `2171.10` | 422,310,000.00 USD | 0.00 USD | 422,310,000.00 USD | 21,940,000.00 USD | 10,800,000.00 USD | 6,300,000.00 USD |
| `7D` | `2173.30` | 648,760,000.00 USD | 0.00 USD | 648,760,000.00 USD | 30,550,000.00 USD | 828,350.00 USD | 5,540,000.00 USD |
| `1D` | `2173.60` | 383,280,000.00 USD | 0.00 USD | 383,280,000.00 USD | 8,030,000.00 USD | 1,390,000.00 USD | 3,800,000.00 USD |
| `1D` | `2176.10` | 370,050,000.00 USD | 0.00 USD | 370,050,000.00 USD | 1,660,000.00 USD | 355,620.00 USD | 0.00 USD |
| `7D` | `2176.60` | 611,830,000.00 USD | 0.00 USD | 611,830,000.00 USD | 5,390,000.00 USD | 1,330,000.00 USD | 2,820,000.00 USD |
| `1D` | `2178.60` | 368,040,000.00 USD | 0.00 USD | 368,040,000.00 USD | 771,300.00 USD | 94,350.00 USD | 2,830,000.00 USD |
| `1D` | `2181.10` | 364,350,000.00 USD | 0.00 USD | 364,350,000.00 USD | 853,380.00 USD | 1,360,000.00 USD | 4,040,000.00 USD |
| `7D` | `2183.20` | 602,290,000.00 USD | 0.00 USD | 602,290,000.00 USD | 1,760,000.00 USD | 0.00 USD | 3,950,000.00 USD |
| `1D` | `2183.60` | 358,090,000.00 USD | 0.00 USD | 358,090,000.00 USD | 73,470.00 USD | 54,020.00 USD | 1,260,000.00 USD |
| `1D` | `2186.10` | 356,700,000.00 USD | 0.00 USD | 356,700,000.00 USD | 310,640.00 USD | 1,630,000.00 USD | 4,220,000.00 USD |
| `7D` | `2186.50` | 596,590,000.00 USD | 0.00 USD | 596,590,000.00 USD | 37,310,000.00 USD | 19,060,000.00 USD | 0.00 USD |
| `1D` | `2188.60` | 350,540,000.00 USD | 0.00 USD | 350,540,000.00 USD | 3,960,000.00 USD | 3,040,000.00 USD | 6,170,000.00 USD |
| `7D` | `2189.80` | 540,230,000.00 USD | 0.00 USD | 540,230,000.00 USD | 12,430,000.00 USD | 19,940,000.00 USD | 4,580,000.00 USD |
| `1D` | `2191.10` | 337,370,000.00 USD | 0.00 USD | 337,370,000.00 USD | 5,610,000.00 USD | 3,650,000.00 USD | 3,530,000.00 USD |
| `7D` | `2193.10` | 503,290,000.00 USD | 0.00 USD | 503,290,000.00 USD | 0.00 USD | 14,900,000.00 USD | 8,080,000.00 USD |
| `1D` | `2193.60` | 324,580,000.00 USD | 0.00 USD | 324,580,000.00 USD | 5,070,000.00 USD | 4,430,000.00 USD | 1,020,000.00 USD |
| `1D` | `2196.10` | 314,070,000.00 USD | 0.00 USD | 314,070,000.00 USD | 8,490,000.00 USD | 745,290.00 USD | 2,990,000.00 USD |
| `7D` | `2196.40` | 480,300,000.00 USD | 0.00 USD | 480,300,000.00 USD | 383,690.00 USD | 243,760.00 USD | 0.00 USD |
| `1D` | `2198.60` | 301,850,000.00 USD | 0.00 USD | 301,850,000.00 USD | 0.00 USD | 3,190,000.00 USD | 9,350,000.00 USD |
| `7D` | `2199.70` | 479,670,000.00 USD | 0.00 USD | 479,670,000.00 USD | 0.00 USD | 0.00 USD | 7,440,000.00 USD |
| `1D` | `2201.10` | 289,310,000.00 USD | 0.00 USD | 289,310,000.00 USD | 7,230,000.00 USD | 2,000,000.00 USD | 4,050,000.00 USD |
| `7D` | `2203.00` | 472,230,000.00 USD | 0.00 USD | 472,230,000.00 USD | 4,310,000.00 USD | 0.00 USD | 5,660,000.00 USD |
| `1D` | `2203.60` | 276,020,000.00 USD | 0.00 USD | 276,020,000.00 USD | 821,280.00 USD | 3,500,000.00 USD | 128,720.00 USD |
| `1D` | `2206.10` | 271,570,000.00 USD | 0.00 USD | 271,570,000.00 USD | 146,940.00 USD | 1,570,000.00 USD | 553,040.00 USD |
| `7D` | `2206.30` | 462,270,000.00 USD | 0.00 USD | 462,270,000.00 USD | 1,490,000.00 USD | 588,950.00 USD | 4,640,000.00 USD |
| `1D` | `2208.60` | 269,300,000.00 USD | 0.00 USD | 269,300,000.00 USD | 0.00 USD | 2,800,000.00 USD | 0.00 USD |
| `7D` | `2209.60` | 455,550,000.00 USD | 0.00 USD | 455,550,000.00 USD | 0.00 USD | 0.00 USD | 9,150,000.00 USD |
| `1D` | `2211.10` | 266,500,000.00 USD | 0.00 USD | 266,500,000.00 USD | 104,760.00 USD | 3,410,000.00 USD | 0.00 USD |
| `7D` | `2212.90` | 446,400,000.00 USD | 0.00 USD | 446,400,000.00 USD | 1,710,000.00 USD | 1,060,000.00 USD | 4,100,000.00 USD |
| `1D` | `2213.60` | 262,980,000.00 USD | 0.00 USD | 262,980,000.00 USD | 5,680,000.00 USD | 4,750,000.00 USD | 63,100.00 USD |
| `1D` | `2216.10` | 252,480,000.00 USD | 0.00 USD | 252,480,000.00 USD | 272,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2216.20` | 439,530,000.00 USD | 0.00 USD | 439,530,000.00 USD | 0.00 USD | 0.00 USD | 495,340.00 USD |
| `1D` | `2218.60` | 252,210,000.00 USD | 0.00 USD | 252,210,000.00 USD | 7,370,000.00 USD | 1,490,000.00 USD | 64,320.00 USD |
| `7D` | `2219.50` | 439,030,000.00 USD | 0.00 USD | 439,030,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 3,700,000.00 USD |
| `1D` | `2221.10` | 243,290,000.00 USD | 0.00 USD | 243,290,000.00 USD | 932,330.00 USD | 5,240,000.00 USD | 3,470,000.00 USD |
| `7D` | `2222.80` | 412,450,000.00 USD | 0.00 USD | 412,450,000.00 USD | 815,570.00 USD | 12,070,000.00 USD | 17,700,000.00 USD |
| `1D` | `2223.60` | 233,650,000.00 USD | 0.00 USD | 233,650,000.00 USD | 16,290,000.00 USD | 3,630,000.00 USD | 7,890,000.00 USD |
| `1D` | `2226.10` | 205,830,000.00 USD | 0.00 USD | 205,830,000.00 USD | 9,900,000.00 USD | 6,070,000.00 USD | 2,770,000.00 USD |
| `7D` | `2226.10` | 381,870,000.00 USD | 0.00 USD | 381,870,000.00 USD | 9,390,000.00 USD | 15,470,000.00 USD | 18,240,000.00 USD |
| `1D` | `2228.60` | 187,090,000.00 USD | 0.00 USD | 187,090,000.00 USD | 20,450,000.00 USD | 13,090,000.00 USD | 4,340,000.00 USD |
| `7D` | `2229.40` | 338,760,000.00 USD | 0.00 USD | 338,760,000.00 USD | 47,950,000.00 USD | 33,560,000.00 USD | 21,030,000.00 USD |
| `1D` | `2231.10` | 149,210,000.00 USD | 0.00 USD | 149,210,000.00 USD | 40,890,000.00 USD | 6,600,000.00 USD | 12,760,000.00 USD |
| `7D` | `2232.70` | 236,220,000.00 USD | 0.00 USD | 236,220,000.00 USD | 24,580,000.00 USD | 46,390,000.00 USD | 28,000,000.00 USD |
| `1D` | `2233.60` | 88,960,000.00 USD | 0.00 USD | 88,960,000.00 USD | 30,060,000.00 USD | 0.00 USD | 21,650,000.00 USD |
| `7D` | `2236.00` | 137,250,000.00 USD | 0.00 USD | 137,250,000.00 USD | 30,150,000.00 USD | 23,260,000.00 USD | 26,480,000.00 USD |
| `1D` | `2236.10` | 37,250,000.00 USD | 0.00 USD | 37,250,000.00 USD | 0.00 USD | 0.00 USD | 14,200,000.00 USD |
| `1D` | `2238.60` | 23,040,000.00 USD | 0.00 USD | 23,040,000.00 USD | 15,220,000.00 USD | 0.00 USD | 2,980,000.00 USD |
| `7D` | `2239.30` | 57,360,000.00 USD | 0.00 USD | 57,360,000.00 USD | 39,050,000.00 USD | 0.00 USD | 8,330,000.00 USD |
| `1D` | `2241.10` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 2,950,000.00 USD |
| `7D` | `2242.60` | 9,970,000.00 USD | 0.00 USD | 9,970,000.00 USD | 6,760,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2243.60` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 0.00 USD | 141,810.00 USD | 50,930.00 USD |
| `7D` | `2245.90` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 2,070,000.00 USD | 1,030,000.00 USD | 102,060.00 USD |
| `1D` | `2246.10` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 0.00 USD | 1,650,000.00 USD | 45,350.00 USD |
| `1D` | `2248.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2248.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2248.60` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 1,860,000.00 USD | 0.00 USD | 1,350,000.00 USD |
| `7D` | `2249.20` | 7,260,000.00 USD | 7,260,000.00 USD | 0.00 USD | 3,350,000.00 USD | 2,660,000.00 USD | 1,250,000.00 USD |
| `1D` | `2251.10` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 10,500,000.00 USD | 221,820.00 USD | 1,260,000.00 USD |
| `7D` | `2252.50` | 37,060,000.00 USD | 37,060,000.00 USD | 0.00 USD | 20,930,000.00 USD | 8,880,000.00 USD | 0.00 USD |
| `1D` | `2253.60` | 29,760,000.00 USD | 29,760,000.00 USD | 0.00 USD | 8,730,000.00 USD | 4,050,000.00 USD | 1,780,000.00 USD |
| `7D` | `2255.80` | 55,100,000.00 USD | 55,100,000.00 USD | 0.00 USD | 7,010,000.00 USD | 10,520,000.00 USD | 514,610.00 USD |
| `1D` | `2256.10` | 56,370,000.00 USD | 56,370,000.00 USD | 0.00 USD | 15,350,000.00 USD | 8,100,000.00 USD | 3,160,000.00 USD |
| `1D` | `2258.60` | 79,550,000.00 USD | 79,550,000.00 USD | 0.00 USD | 12,840,000.00 USD | 8,430,000.00 USD | 1,920,000.00 USD |
| `7D` | `2259.10` | 85,400,000.00 USD | 85,400,000.00 USD | 0.00 USD | 18,800,000.00 USD | 7,450,000.00 USD | 4,040,000.00 USD |
| `1D` | `2261.10` | 93,590,000.00 USD | 93,590,000.00 USD | 0.00 USD | 8,030,000.00 USD | 4,330,000.00 USD | 1,680,000.00 USD |
| `7D` | `2262.40` | 93,780,000.00 USD | 93,780,000.00 USD | 0.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 210,470.00 USD |
| `1D` | `2263.60` | 119,070,000.00 USD | 119,070,000.00 USD | 0.00 USD | 10,590,000.00 USD | 8,540,000.00 USD | 6,350,000.00 USD |
| `7D` | `2265.70` | 100,110,000.00 USD | 100,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,330,000.00 USD |
| `1D` | `2266.10` | 141,460,000.00 USD | 141,460,000.00 USD | 0.00 USD | 4,250,000.00 USD | 10,210,000.00 USD | 7,930,000.00 USD |
| `1D` | `2268.60` | 171,310,000.00 USD | 171,310,000.00 USD | 0.00 USD | 13,820,000.00 USD | 7,980,000.00 USD | 8,050,000.00 USD |
| `7D` | `2269.00` | 119,040,000.00 USD | 119,040,000.00 USD | 0.00 USD | 8,610,000.00 USD | 5,650,000.00 USD | 4,660,000.00 USD |
| `1D` | `2271.10` | 177,430,000.00 USD | 177,430,000.00 USD | 0.00 USD | 1,520,000.00 USD | 1,310,000.00 USD | 3,290,000.00 USD |
| `7D` | `2272.30` | 128,070,000.00 USD | 128,070,000.00 USD | 0.00 USD | 7,540,000.00 USD | 1,480,000.00 USD | 0.00 USD |
| `1D` | `2273.60` | 183,110,000.00 USD | 183,110,000.00 USD | 0.00 USD | 395,550.00 USD | 4,190,000.00 USD | 1,110,000.00 USD |
| `7D` | `2275.60` | 133,560,000.00 USD | 133,560,000.00 USD | 0.00 USD | 0.00 USD | 5,500,000.00 USD | 0.00 USD |
| `1D` | `2276.10` | 218,340,000.00 USD | 218,340,000.00 USD | 0.00 USD | 16,020,000.00 USD | 14,780,000.00 USD | 4,440,000.00 USD |
| `1D` | `2278.60` | 232,070,000.00 USD | 232,070,000.00 USD | 0.00 USD | 0.00 USD | 7,190,000.00 USD | 6,540,000.00 USD |
| `7D` | `2278.90` | 157,510,000.00 USD | 157,510,000.00 USD | 0.00 USD | 854,200.00 USD | 12,550,000.00 USD | 10,540,000.00 USD |
| `1D` | `2281.10` | 297,580,000.00 USD | 297,580,000.00 USD | 0.00 USD | 32,540,000.00 USD | 25,110,000.00 USD | 7,850,000.00 USD |
| `7D` | `2282.20` | 255,060,000.00 USD | 255,060,000.00 USD | 0.00 USD | 0.00 USD | 83,870,000.00 USD | 13,670,000.00 USD |
| `1D` | `2283.60` | 354,830,000.00 USD | 354,830,000.00 USD | 0.00 USD | 29,580,000.00 USD | 15,340,000.00 USD | 12,330,000.00 USD |
| `7D` | `2285.50` | 288,720,000.00 USD | 288,720,000.00 USD | 0.00 USD | 6,610,000.00 USD | 26,950,000.00 USD | 105,230.00 USD |
| `1D` | `2286.10` | 376,960,000.00 USD | 376,960,000.00 USD | 0.00 USD | 4,320,000.00 USD | 11,590,000.00 USD | 6,200,000.00 USD |
| `1D` | `2288.60` | 400,740,000.00 USD | 400,740,000.00 USD | 0.00 USD | 12,530,000.00 USD | 8,240,000.00 USD | 3,010,000.00 USD |
| `7D` | `2288.80` | 320,170,000.00 USD | 320,170,000.00 USD | 0.00 USD | 8,380,000.00 USD | 8,140,000.00 USD | 14,930,000.00 USD |
| `1D` | `2291.10` | 434,490,000.00 USD | 434,490,000.00 USD | 0.00 USD | 17,120,000.00 USD | 10,130,000.00 USD | 6,500,000.00 USD |
| `7D` | `2292.10` | 331,560,000.00 USD | 331,560,000.00 USD | 0.00 USD | 7,890,000.00 USD | 517,070.00 USD | 2,990,000.00 USD |
| `1D` | `2293.60` | 457,790,000.00 USD | 457,790,000.00 USD | 0.00 USD | 11,320,000.00 USD | 4,560,000.00 USD | 7,420,000.00 USD |
| `7D` | `2295.40` | 368,030,000.00 USD | 368,030,000.00 USD | 0.00 USD | 22,930,000.00 USD | 6,820,000.00 USD | 6,720,000.00 USD |
| `1D` | `2296.10` | 478,560,000.00 USD | 478,560,000.00 USD | 0.00 USD | 4,070,000.00 USD | 13,690,000.00 USD | 3,000,000.00 USD |
| `1D` | `2298.60` | 526,740,000.00 USD | 526,740,000.00 USD | 0.00 USD | 26,500,000.00 USD | 14,510,000.00 USD | 7,170,000.00 USD |
| `7D` | `2298.70` | 390,870,000.00 USD | 390,870,000.00 USD | 0.00 USD | 897,290.00 USD | 11,270,000.00 USD | 10,670,000.00 USD |
| `1D` | `2301.10` | 553,800,000.00 USD | 553,800,000.00 USD | 0.00 USD | 7,640,000.00 USD | 7,330,000.00 USD | 12,090,000.00 USD |
| `7D` | `2302.00` | 466,190,000.00 USD | 466,190,000.00 USD | 0.00 USD | 29,960,000.00 USD | 23,280,000.00 USD | 22,080,000.00 USD |
| `1D` | `2303.60` | 588,500,000.00 USD | 588,500,000.00 USD | 0.00 USD | 17,880,000.00 USD | 10,150,000.00 USD | 6,670,000.00 USD |
| `7D` | `2305.30` | 501,350,000.00 USD | 501,350,000.00 USD | 0.00 USD | 17,280,000.00 USD | 6,960,000.00 USD | 10,920,000.00 USD |
| `1D` | `2306.10` | 626,730,000.00 USD | 626,730,000.00 USD | 0.00 USD | 16,140,000.00 USD | 12,830,000.00 USD | 9,260,000.00 USD |
| `1D` | `2308.60` | 630,610,000.00 USD | 630,610,000.00 USD | 0.00 USD | 423,370.00 USD | 3,270,000.00 USD | 182,210.00 USD |
| `7D` | `2308.60` | 505,600,000.00 USD | 505,600,000.00 USD | 0.00 USD | 1,240,000.00 USD | 2,780,000.00 USD | 231,420.00 USD |
| `1D` | `2311.10` | 647,880,000.00 USD | 647,880,000.00 USD | 0.00 USD | 5,900,000.00 USD | 813,020.00 USD | 10,560,000.00 USD |
| `7D` | `2311.90` | 535,840,000.00 USD | 535,840,000.00 USD | 0.00 USD | 11,460,000.00 USD | 2,650,000.00 USD | 16,120,000.00 USD |
| `1D` | `2313.60` | 660,980,000.00 USD | 660,980,000.00 USD | 0.00 USD | 4,690,000.00 USD | 7,240,000.00 USD | 1,170,000.00 USD |
| `7D` | `2315.20` | 544,590,000.00 USD | 544,590,000.00 USD | 0.00 USD | 0.00 USD | 8,120,000.00 USD | 627,210.00 USD |
| `1D` | `2316.10` | 694,120,000.00 USD | 694,120,000.00 USD | 0.00 USD | 9,820,000.00 USD | 16,730,000.00 USD | 6,590,000.00 USD |
| `7D` | `2318.50` | 559,510,000.00 USD | 559,510,000.00 USD | 0.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 5,830,000.00 USD |
| `1D` | `2318.60` | 706,110,000.00 USD | 706,110,000.00 USD | 0.00 USD | 4,440,000.00 USD | 5,330,000.00 USD | 2,210,000.00 USD |
| `1D` | `2321.10` | 729,100,000.00 USD | 729,100,000.00 USD | 0.00 USD | 6,390,000.00 USD | 14,670,000.00 USD | 1,940,000.00 USD |
| `7D` | `2321.80` | 579,250,000.00 USD | 579,250,000.00 USD | 0.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 2,690,000.00 USD |
| `1D` | `2323.60` | 740,300,000.00 USD | 740,300,000.00 USD | 0.00 USD | 1,250,000.00 USD | 6,360,000.00 USD | 3,590,000.00 USD |
| `7D` | `2325.10` | 600,330,000.00 USD | 600,330,000.00 USD | 0.00 USD | 10,150,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD |
| `1D` | `2326.10` | 754,830,000.00 USD | 754,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 6,990,000.00 USD | 5,720,000.00 USD |
| `7D` | `2328.40` | 612,330,000.00 USD | 612,330,000.00 USD | 0.00 USD | 3,860,000.00 USD | 121,880.00 USD | 8,020,000.00 USD |
| `1D` | `2328.60` | 758,700,000.00 USD | 758,700,000.00 USD | 0.00 USD | 3,080,000.00 USD | 524,360.00 USD | 261,590.00 USD |
| `1D` | `2331.10` | 782,680,000.00 USD | 782,680,000.00 USD | 0.00 USD | 19,380,000.00 USD | 3,300,000.00 USD | 1,300,000.00 USD |
| `7D` | `2331.70` | 641,800,000.00 USD | 641,800,000.00 USD | 0.00 USD | 29,230,000.00 USD | 241,890.00 USD | 0.00 USD |
| `1D` | `2333.60` | 801,100,000.00 USD | 801,100,000.00 USD | 0.00 USD | 5,160,000.00 USD | 4,720,000.00 USD | 8,530,000.00 USD |
| `7D` | `2335.00` | 694,070,000.00 USD | 694,070,000.00 USD | 0.00 USD | 20,390,000.00 USD | 19,830,000.00 USD | 12,040,000.00 USD |
| `1D` | `2336.10` | 821,930,000.00 USD | 821,930,000.00 USD | 0.00 USD | 14,690,000.00 USD | 1,960,000.00 USD | 4,190,000.00 USD |
| `7D` | `2338.30` | 725,800,000.00 USD | 725,800,000.00 USD | 0.00 USD | 22,110,000.00 USD | 0.00 USD | 9,610,000.00 USD |
| `1D` | `2338.60` | 836,980,000.00 USD | 836,980,000.00 USD | 0.00 USD | 8,670,000.00 USD | 2,930,000.00 USD | 3,440,000.00 USD |
| `1D` | `2341.10` | 858,340,000.00 USD | 858,340,000.00 USD | 0.00 USD | 7,140,000.00 USD | 4,080,000.00 USD | 10,140,000.00 USD |
| `7D` | `2341.60` | 762,330,000.00 USD | 762,330,000.00 USD | 0.00 USD | 4,720,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD |
| `1D` | `2343.60` | 875,500,000.00 USD | 875,500,000.00 USD | 0.00 USD | 4,110,000.00 USD | 7,890,000.00 USD | 5,150,000.00 USD |
| `7D` | `2344.90` | 789,170,000.00 USD | 789,170,000.00 USD | 0.00 USD | 1,350,000.00 USD | 16,920,000.00 USD | 8,580,000.00 USD |
| `1D` | `2346.10` | 887,630,000.00 USD | 887,630,000.00 USD | 0.00 USD | 3,680,000.00 USD | 3,010,000.00 USD | 5,440,000.00 USD |
| `7D` | `2348.20` | 825,300,000.00 USD | 825,300,000.00 USD | 0.00 USD | 561,950.00 USD | 12,390,000.00 USD | 23,170,000.00 USD |
| `1D` | `2348.60` | 905,740,000.00 USD | 905,740,000.00 USD | 0.00 USD | 8,700,000.00 USD | 6,650,000.00 USD | 2,760,000.00 USD |
| `1D` | `2351.10` | 946,300,000.00 USD | 946,300,000.00 USD | 0.00 USD | 24,430,000.00 USD | 4,950,000.00 USD | 11,190,000.00 USD |
| `7D` | `2351.50` | 863,960,000.00 USD | 863,960,000.00 USD | 0.00 USD | 2,930,000.00 USD | 20,680,000.00 USD | 15,060,000.00 USD |
| `1D` | `2353.60` | 957,330,000.00 USD | 957,330,000.00 USD | 0.00 USD | 3,230,000.00 USD | 7,140,000.00 USD | 652,430.00 USD |
| `7D` | `2354.80` | 920,810,000.00 USD | 920,810,000.00 USD | 0.00 USD | 17,130,000.00 USD | 38,220,000.00 USD | 1,500,000.00 USD |
| `1D` | `2356.10` | 972,610,000.00 USD | 972,610,000.00 USD | 0.00 USD | 5,940,000.00 USD | 6,670,000.00 USD | 2,680,000.00 USD |
| `7D` | `2358.10` | 937,970,000.00 USD | 937,970,000.00 USD | 0.00 USD | 7,110,000.00 USD | 4,040,000.00 USD | 6,010,000.00 USD |
| `1D` | `2358.60` | 990,110,000.00 USD | 990,110,000.00 USD | 0.00 USD | 4,520,000.00 USD | 5,630,000.00 USD | 7,360,000.00 USD |
| `1D` | `2361.10` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 8,670,000.00 USD | 4,820,000.00 USD | 1,300,000.00 USD |
| `7D` | `2361.40` | 946,240,000.00 USD | 946,240,000.00 USD | 0.00 USD | 4,470,000.00 USD | 3,430,000.00 USD | 374,770.00 USD |
| `1D` | `2363.60` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 5,260,000.00 USD | 6,820,000.00 USD | 8,490,000.00 USD |
| `7D` | `2364.70` | 962,110,000.00 USD | 962,110,000.00 USD | 0.00 USD | 4,570,000.00 USD | 373,740.00 USD | 10,920,000.00 USD |
| `1D` | `2366.10` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 4,830,000.00 USD | 827,140.00 USD | 2,400,000.00 USD |
| `7D` | `2368.00` | 975,950,000.00 USD | 975,950,000.00 USD | 0.00 USD | 11,660,000.00 USD | 1,780,000.00 USD | 396,420.00 USD |
| `1D` | `2368.60` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 7,050,000.00 USD | 4,420,000.00 USD | 3,400,000.00 USD |
| `1D` | `2371.10` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 14,820,000.00 USD | 6,060,000.00 USD | 6,700,000.00 USD |
| `7D` | `2371.30` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 25,000,000.00 USD | 0.00 USD | 54,480,000.00 USD |
| `1D` | `2373.60` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 13,760,000.00 USD | 1,630,000.00 USD | 5,900,000.00 USD |
| `7D` | `2374.60` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 19,920,000.00 USD | 121,480.00 USD | 6,980,000.00 USD |
| `1D` | `2376.10` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 5,860,000.00 USD | 4,290,000.00 USD | 4,130,000.00 USD |
| `7D` | `2377.90` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 11,180,000.00 USD | 6,190,000.00 USD | 29,810,000.00 USD |
| `1D` | `2378.60` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 1,650,000.00 USD | 2,490,000.00 USD | 3,240,000.00 USD |
| `1D` | `2381.10` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 10,120,000.00 USD | 7,600,000.00 USD | 10,030,000.00 USD |
| `7D` | `2381.20` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 4,150,000.00 USD | 19,270,000.00 USD |
| `1D` | `2383.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 12,240,000.00 USD | 8,580,000.00 USD | 5,790,000.00 USD |
| `7D` | `2384.50` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 22,580,000.00 USD | 22,660,000.00 USD | 45,970,000.00 USD |
| `1D` | `2386.10` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 10,140,000.00 USD | 10,450,000.00 USD | 4,380,000.00 USD |
| `7D` | `2387.80` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 5,540,000.00 USD | 49,830,000.00 USD | 47,300,000.00 USD |
| `1D` | `2388.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 9,760,000.00 USD | 6,510,000.00 USD | 3,500,000.00 USD |
| `1D` | `2391.10` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 1,410,000.00 USD | 4,340,000.00 USD | 3,350,000.00 USD |
| `7D` | `2391.10` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 5,910,000.00 USD | 52,770,000.00 USD | 41,810,000.00 USD |
| `1D` | `2393.60` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 2,570,000.00 USD | 3,590,000.00 USD | 1,110,000.00 USD |
| `7D` | `2394.40` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 60,000,000.00 USD | 32,420,000.00 USD | 40,070,000.00 USD |
| `1D` | `2396.10` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 2,220,000.00 USD | 331,850.00 USD | 1,620,000.00 USD |
| `7D` | `2397.70` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 31,080,000.00 USD | 41,130,000.00 USD | 26,250,000.00 USD |
| `1D` | `2398.60` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 1,760,000.00 USD | 4,590,000.00 USD | 3,310,000.00 USD |
| `7D` | `2401.00` | 1,790,000,000.00 USD | 1,790,000,000.00 USD | 0.00 USD | 51,130,000.00 USD | 28,060,000.00 USD | 25,770,000.00 USD |
| `1D` | `2401.10` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 4,570,000.00 USD | 3,010,000.00 USD | 2,310,000.00 USD |
| `1D` | `2403.60` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 5,500,000.00 USD | 3,040,000.00 USD | 2,190,000.00 USD |
| `7D` | `2404.30` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 0.00 USD | 61,130,000.00 USD | 29,350,000.00 USD | 31,410,000.00 USD |
| `1D` | `2406.10` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 0.00 USD | 10,520,000.00 USD | 5,000,000.00 USD | 5,170,000.00 USD |
| `7D` | `2407.60` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 0.00 USD | 29,050,000.00 USD | 35,150,000.00 USD | 19,040,000.00 USD |
| `1D` | `2408.60` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 0.00 USD | 4,880,000.00 USD | 6,000,000.00 USD | 2,130,000.00 USD |
| `7D` | `2410.90` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 0.00 USD | 25,670,000.00 USD | 27,460,000.00 USD | 31,240,000.00 USD |
| `1D` | `2411.10` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 7,010,000.00 USD | 5,090,000.00 USD | 5,150,000.00 USD |
| `1D` | `2413.60` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 4,430,000.00 USD | 3,130,000.00 USD | 1,630,000.00 USD |
| `7D` | `2414.20` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 21,950,000.00 USD | 25,190,000.00 USD | 22,860,000.00 USD |
| `1D` | `2416.10` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 3,760,000.00 USD | 2,230,000.00 USD | 3,950,000.00 USD |
| `7D` | `2417.50` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 31,300,000.00 USD | 11,500,000.00 USD | 24,160,000.00 USD |
| `1D` | `2418.60` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 3,250,000.00 USD | 1,840,000.00 USD | 1,970,000.00 USD |
| `7D` | `2420.80` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 32,960,000.00 USD | 25,400,000.00 USD | 14,740,000.00 USD |
| `1D` | `2421.10` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 6,230,000.00 USD | 5,070,000.00 USD | 4,340,000.00 USD |
| `1D` | `2423.60` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 908,650.00 USD | 2,650,000.00 USD | 2,860,000.00 USD |
| `7D` | `2424.10` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 20,380,000.00 USD | 29,890,000.00 USD | 23,700,000.00 USD |
| `1D` | `2426.10` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 1,470,000.00 USD | 1,010,000.00 USD | 40,970.00 USD |
| `7D` | `2427.40` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 22,390,000.00 USD | 17,570,000.00 USD | 20,240,000.00 USD |
| `1D` | `2428.60` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 1,290,000.00 USD | 1,450,000.00 USD | 1,470,000.00 USD |
| `7D` | `2430.70` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 0.00 USD | 8,890,000.00 USD | 15,370,000.00 USD | 9,660,000.00 USD |
| `1D` | `2431.10` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 3,120,000.00 USD | 2,370,000.00 USD | 677,240.00 USD |
| `1D` | `2433.60` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 1,770,000.00 USD | 1,450,000.00 USD | 1,680,000.00 USD |
| `7D` | `2434.00` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 0.00 USD | 19,530,000.00 USD | 9,570,000.00 USD | 13,090,000.00 USD |
| `1D` | `2436.10` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 2,490,000.00 USD | 1,070,000.00 USD | 161,010.00 USD |
| `7D` | `2437.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 0.00 USD | 15,680,000.00 USD | 15,080,000.00 USD | 6,290,000.00 USD |
| `1D` | `2438.60` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 476,020.00 USD | 535,870.00 USD | 15,480.00 USD |
| `7D` | `2440.60` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 0.00 USD | 16,940,000.00 USD | 10,790,000.00 USD | 9,240,000.00 USD |
| `1D` | `2441.10` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 2,260,000.00 USD | 723,100.00 USD | 858,540.00 USD |
| `1D` | `2443.60` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 0.00 USD | 412,840.00 USD | 1,390,000.00 USD |
| `7D` | `2443.90` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 5,830,000.00 USD | 12,110,000.00 USD | 6,990,000.00 USD |
| `1D` | `2446.10` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 472,100.00 USD | 360,870.00 USD | 10,310.00 USD |
| `7D` | `2447.20` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 13,820,000.00 USD | 7,510,000.00 USD | 16,330,000.00 USD |
| `1D` | `2448.60` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 321,220.00 USD | 198,200.00 USD | 687,270.00 USD |
| `7D` | `2450.50` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 10,570,000.00 USD | 11,560,000.00 USD | 10,410,000.00 USD |
| `1D` | `2451.10` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 1,380,000.00 USD | 1,300,000.00 USD | 709,270.00 USD |
| `1D` | `2453.60` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 3,640,000.00 USD | 1,900,000.00 USD | 2,150,000.00 USD |
| `7D` | `2453.80` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 0.00 USD | 7,240,000.00 USD | 4,290,000.00 USD | 6,910,000.00 USD |
| `1D` | `2456.10` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 622,030.00 USD | 1,890,000.00 USD | 797,640.00 USD |
| `7D` | `2457.10` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 8,340,000.00 USD | 8,890,000.00 USD | 7,910,000.00 USD |
| `1D` | `2458.60` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 1,430,000.00 USD | 9,120.00 USD |
| `7D` | `2460.40` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 7,080,000.00 USD | 8,140,000.00 USD | 9,350,000.00 USD |
| `1D` | `2461.10` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 515,180.00 USD | 242,570.00 USD | 375,380.00 USD |
| `1D` | `2463.60` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 330,880.00 USD | 940,830.00 USD | 829,050.00 USD |
| `7D` | `2463.70` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 0.00 USD | 9,430,000.00 USD | 8,280,000.00 USD | 6,170,000.00 USD |
| `1D` | `2466.10` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 448,360.00 USD | 872,060.00 USD | 550,280.00 USD |
| `7D` | `2467.00` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 4,840,000.00 USD | 2,920,000.00 USD | 1,330,000.00 USD |
| `1D` | `2468.60` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 288,920.00 USD | 1,680,000.00 USD | 558,540.00 USD |
| `7D` | `2470.30` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 3,190,000.00 USD | 3,080,000.00 USD | 496,280.00 USD |
| `1D` | `2471.10` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 973,110.00 USD | 199,120.00 USD | 798,020.00 USD |
| `1D` | `2473.60` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 316,810.00 USD |
| `7D` | `2473.60` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 5,860,000.00 USD | 2,920,000.00 USD | 2,270,000.00 USD |
| `1D` | `2476.10` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 0.00 USD | 1,100,000.00 USD | 28,770.00 USD |
| `7D` | `2476.90` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 2,660,000.00 USD | 2,410,000.00 USD | 872,130.00 USD |
| `1D` | `2478.60` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 1,430,000.00 USD | 933,460.00 USD | 302,890.00 USD |
| `7D` | `2480.20` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 1,580,000.00 USD | 6,190,000.00 USD | 1,590,000.00 USD |
| `1D` | `2481.10` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 0.00 USD | 229,630.00 USD | 611,090.00 USD |
| `1D` | `2482.40` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 437,940.00 USD | 156,850.00 USD | 707,170.00 USD |
| `7D` | `2483.50` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 1,750,000.00 USD | 2,280,000.00 USD | 77,610.00 USD |
| `7D` | `2486.80` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 30,880.00 USD | 0.00 USD | 1,350,000.00 USD |
| `7D` | `2490.10` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 1,010,000.00 USD | 167,620.00 USD |
| `7D` | `2493.40` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 3,210,000.00 USD | 1,830,000.00 USD | 1,470,000.00 USD |
| `7D` | `2496.70` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 1,370,000.00 USD | 3,690,000.00 USD | 4,660,000.00 USD |
| `7D` | `2500.00` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 358,770.00 USD | 1,980,000.00 USD | 1,170,000.00 USD |
| `7D` | `2503.30` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 0.00 USD | 27,220.00 USD | 125,600.00 USD |
| `7D` | `2506.60` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 2,540,000.00 USD | 903,900.00 USD | 1,990,000.00 USD |
| `7D` | `2509.90` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 2,290,000.00 USD | 2,160,000.00 USD | 1,190,000.00 USD |
| `7D` | `2516.50` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2519.80` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `7D` | `2523.10` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 249,960.00 USD | 945,860.00 USD |
| `7D` | `2526.40` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 292,400.00 USD | 1,090,000.00 USD | 200,040.00 USD |
| `7D` | `2529.70` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 0.00 USD | 1,510,000.00 USD | 2,770,000.00 USD | 1,300,000.00 USD |
| `7D` | `2533.00` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 0.00 USD | 4,460,000.00 USD | 1,850,000.00 USD | 1,550,000.00 USD |
| `7D` | `2536.30` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 3,170,000.00 USD | 2,460,000.00 USD | 4,010,000.00 USD |
| `7D` | `2539.60` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 4,190,000.00 USD | 3,730,000.00 USD | 1,140,000.00 USD |
| `7D` | `2542.90` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 4,070,000.00 USD | 2,950,000.00 USD | 2,920,000.00 USD |
| `7D` | `2546.20` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 1,140,000.00 USD | 1,850,000.00 USD |
| `7D` | `2549.50` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 3,470,000.00 USD | 4,160,000.00 USD |
| `7D` | `2552.80` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 1,920,000.00 USD | 580,780.00 USD | 1,140,000.00 USD |
| `7D` | `2556.10` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 4,340,000.00 USD | 549,010.00 USD | 7,010,000.00 USD |
| `7D` | `2559.40` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 0.00 USD | 5,200,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD |
| `7D` | `2562.70` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 1,940,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD |
| `7D` | `2566.00` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 0.00 USD | 1,880,000.00 USD | 1,520,000.00 USD | 2,070,000.00 USD |
| `7D` | `2569.30` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 0.00 USD | 125,250.00 USD | 739,480.00 USD | 2,000,000.00 USD |
| `7D` | `2572.60` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 890,480.00 USD | 2,220,000.00 USD |
| `7D` | `2575.90` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 2,180,000.00 USD | 440,740.00 USD | 1,090,000.00 USD |
| `7D` | `2579.20` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 1,870,000.00 USD | 1,940,000.00 USD | 1,730,000.00 USD |
| `7D` | `2582.50` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 0.00 USD | 2,830,000.00 USD | 1,030,000.00 USD | 3,720,000.00 USD |
| `7D` | `2585.80` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 0.00 USD | 883,660.00 USD | 2,700,000.00 USD | 1,870,000.00 USD |
| `7D` | `2589.10` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 0.00 USD | 2,540,000.00 USD | 536,380.00 USD | 2,830,000.00 USD |
| `7D` | `2590.30` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 0.00 USD | 1,180,000.00 USD | 304,000.00 USD | 447,590.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `29.14B` | Total OI Tokens: `12,971,138.4 ETH`
  * 1h OI Change: `+0.43%` | 4h OI Change: `+0.14%` | 24h OI Change: `-3.20%`
  * Exchange Breakdown: Binance=`8.48B` | Bybit=`2.10B` | OKX=`1.80B` | Hyperliquid=`2.36B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-180.86K` | Last 24h: `1.05M` | Last 3d: `6.29M` | Last 7d: `12.86M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0020%` | **USDT OKX** | `-0.0089%` |
| **USDT Bybit** | `-0.0156%` | **USDT KuCoin** | `-0.0104%` |
| **USDT MEXC** | `0.0020%` | **USDT BingX** | `0.0019%` |
| **USDT Gate** | `-0.0120%` | **USDT Bitget** | `0.0002%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0073%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `53.39%` | `46.61%` | `1.15` | 718,670,000.00 USD |
| `15M` | `Binance` | `49.95%` | `50.05%` | `1.00` | 239,550,000.00 USD |
| `15M` | `OKX` | `56.64%` | `43.36%` | `1.31` | 118,370,000.00 USD |
| `15M` | `Bybit` | `65.31%` | `34.69%` | `1.88` | 72,030,000.00 USD |
| `15M` | `KuCoin` | `77.99%` | `22.01%` | `3.54` | 1,630,000.00 USD |
| `15M` | `Gate` | `51.22%` | `48.78%` | `1.05` | 81,890,000.00 USD |
| `15M` | `Bitget` | `49.93%` | `50.07%` | `1.00` | 48,490,000.00 USD |
| `15M` | `BingX` | `46.89%` | `53.11%` | `0.88` | 11,390,000.00 USD |
| `15M` | `MEXC` | `51.12%` | `48.88%` | `1.05` | 31,320,000.00 USD |
| `15M` | `Bitunix` | `58.88%` | `41.12%` | `1.43` | 34,060,000.00 USD |
| `15M` | `Hyperliquid` | `56.7%` | `43.3%` | `1.31` | 25,770,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.4%` | `52.6%` | `0.90` | 3,480,000.00 USD |
| `15M` | `Crypto.com` | `47.58%` | `52.42%` | `0.91` | 1,380,000.00 USD |
| `15M` | `WhiteBIT` | `0.4%` | `99.6%` | `0.00` | 4,030,000.00 USD |
| `15M` | `HTX` | `52.88%` | `47.12%` | `1.12` | 2,180,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `54.74%` | `45.26%` | `1.21` | 28,110,000.00 USD |
| `15M` | `Bitfinex` | `43.5%` | `56.5%` | `0.77` | 549,180.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `53.68%` | `46.32%` | `1.16` | 6,780,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `49.21%` | `50.79%` | `0.97` | 7,660,000.00 USD |
| `15M` | `Whale Positions` | `49.95%` | `50.05%` | `1.00` | 239,550,000.00 USD |
| `15M` | `Global Accounts` | `53.39%` | `46.61%` | `1.15` | 718,670,000.00 USD |
| `1H` | `ETH` | `53.93%` | `46.07%` | `1.17` | 2,510,000,000.00 USD |
| `1H` | `Binance` | `52.11%` | `47.89%` | `1.09` | 799,980,000.00 USD |
| `1H` | `OKX` | `51.11%` | `48.89%` | `1.05` | 378,200,000.00 USD |
| `1H` | `Bybit` | `61.93%` | `38.07%` | `1.63` | 224,710,000.00 USD |
| `1H` | `KuCoin` | `71.37%` | `28.63%` | `2.49` | 7,470,000.00 USD |
| `1H` | `Gate` | `49.38%` | `50.62%` | `0.98` | 280,810,000.00 USD |
| `1H` | `Bitget` | `52.75%` | `47.25%` | `1.12` | 163,430,000.00 USD |
| `1H` | `BingX` | `46.3%` | `53.7%` | `0.86` | 36,860,000.00 USD |
| `1H` | `MEXC` | `48.42%` | `51.58%` | `0.94` | 115,500,000.00 USD |
| `1H` | `Bitunix` | `53.25%` | `46.75%` | `1.14` | 121,110,000.00 USD |
| `1H` | `Hyperliquid` | `56.97%` | `43.03%` | `1.32` | 128,230,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `45.25%` | `54.75%` | `0.83` | 13,390,000.00 USD |
| `1H` | `Crypto.com` | `50.24%` | `49.76%` | `1.01` | 5,060,000.00 USD |
| `1H` | `WhiteBIT` | `86.63%` | `13.37%` | `6.48` | 90,840,000.00 USD |
| `1H` | `HTX` | `51.52%` | `48.48%` | `1.06` | 8,540,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `50.81%` | `49.19%` | `1.03` | 83,030,000.00 USD |
| `1H` | `Bitfinex` | `46.72%` | `53.28%` | `0.88` | 1,630,000.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `60.57%` | `39.43%` | `1.54` | 27,900,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `51.9%` | `48.1%` | `1.08` | 24,720,000.00 USD |
| `1H` | `Whale Positions` | `52.11%` | `47.89%` | `1.09` | 799,980,000.00 USD |
| `1H` | `Global Accounts` | `53.93%` | `46.07%` | `1.17` | 2,510,000,000.00 USD |
| `4H` | `ETH` | `52.87%` | `47.13%` | `1.12` | 15,510,000,000.00 USD |
| `4H` | `Binance` | `51.89%` | `48.11%` | `1.08` | 4,840,000,000.00 USD |
| `4H` | `OKX` | `51.17%` | `48.83%` | `1.05` | 2,190,000,000.00 USD |
| `4H` | `Bybit` | `54.87%` | `45.13%` | `1.22` | 1,460,000,000.00 USD |
| `4H` | `KuCoin` | `64.93%` | `35.07%` | `1.85` | 53,180,000.00 USD |
| `4H` | `Gate` | `48.28%` | `51.72%` | `0.93` | 1,750,000,000.00 USD |
| `4H` | `Bitget` | `50.35%` | `49.65%` | `1.01` | 812,020,000.00 USD |
| `4H` | `BingX` | `48.24%` | `51.76%` | `0.93` | 221,450,000.00 USD |
| `4H` | `MEXC` | `47.34%` | `52.66%` | `0.90` | 635,380,000.00 USD |
| `4H` | `Bitunix` | `51.92%` | `48.08%` | `1.08` | 679,870,000.00 USD |
| `4H` | `Hyperliquid` | `54.87%` | `45.13%` | `1.22` | 1,030,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `63.52%` | `36.48%` | `1.74` | 113,840,000.00 USD |
| `4H` | `Crypto.com` | `49.91%` | `50.09%` | `1.00` | 49,270,000.00 USD |
| `4H` | `WhiteBIT` | `79.5%` | `20.5%` | `3.88` | 726,190,000.00 USD |
| `4H` | `HTX` | `48.93%` | `51.07%` | `0.96` | 62,480,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `50.71%` | `49.29%` | `1.03` | 530,420,000.00 USD |
| `4H` | `Bitfinex` | `52.27%` | `47.73%` | `1.10` | 12,050,000.00 USD |
| `4H` | `Kraken` | `50.17%` | `49.83%` | `1.01` | 24,960,000.00 USD |
| `4H` | `Aster` | `51.35%` | `48.65%` | `1.06` | 158,450,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.89%` | `51.11%` | `0.96` | 157,590,000.00 USD |
| `4H` | `Whale Positions` | `51.89%` | `48.11%` | `1.08` | 4,840,000,000.00 USD |
| `4H` | `Global Accounts` | `52.87%` | `47.13%` | `1.12` | 15,510,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `2215.25` | `2214.70` | `2215.25` | `2218.75` | `2208.25` | 100,318,327.91 USD | 51,517,721.13 USD | 48,800,606.78 USD | 2,717,114.35 USD | `+2.71%` | `2B / 2S` |
| `5:00 UTC` | `2219.75` | `2216.05` | `2219.75` | `2221.25` | `2210.25` | 81,002,689.38 USD | 47,369,805.78 USD | 33,632,883.60 USD | 13,736,922.17 USD | `+16.96%` | `0B / 0S` |
| `0:00 UTC` | `2229.75` | `2226.55` | `2229.75` | `2232.75` | `2219.75` | 182,767,345.67 USD | 98,774,699.85 USD | 83,992,645.82 USD | 14,782,054.04 USD | `+8.09%` | `1B / 2S` |
| `5:00 UTC` | `2234.75` | `2234.69` | `2234.75` | `2238.25` | `2230.25` | 138,036,296.36 USD | 70,500,947.16 USD | 67,535,349.20 USD | 2,965,597.96 USD | `+2.15%` | `1B / 0S` |
| `0:00 UTC` | `2229.75` | `2230.64` | `2229.75` | `2236.75` | `2225.25` | 125,588,915.24 USD | 57,499,740.21 USD | 68,089,175.03 USD | -10,589,434.83 USD | `-8.43%` | `0B / 2S` |
| `5:00 UTC` | `2241.25` | `2240.18` | `2241.25` | `2243.25` | `2233.75` | 123,392,803.54 USD | 67,738,859.18 USD | 55,653,944.36 USD | 12,084,914.83 USD | `+9.79%` | `1B / 2S` |
| `0:00 UTC` | `2245.25` | `2244.67` | `2245.25` | `2246.25` | `2242.75` | 130,536,562.11 USD | 61,753,972.34 USD | 68,782,589.78 USD | -7,028,617.44 USD | `-5.38%` | `0B / 0S` |
| `5:00 UTC` | `2246.25` | `2244.65` | `2246.25` | `2246.75` | `2241.25` | 83,556,134.35 USD | 43,872,052.14 USD | 39,684,082.21 USD | 4,187,969.92 USD | `+5.01%` | `0B / 0S` |
| `0:00 UTC` | `2250.25` | `2247.75` | `2250.25` | `2252.75` | `2241.75` | 107,425,896.61 USD | 60,168,072.38 USD | 47,257,824.22 USD | 12,910,248.16 USD | `+12.02%` | `3B / 0S` |
| `5:00 UTC` | `2247.25` | `2247.58` | `2247.25` | `2249.25` | `2246.75` | 19,670,451.83 USD | 8,842,187.36 USD | 10,828,264.47 USD | -1,986,077.11 USD | `-10.10%` | `0B / 0S` |

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
| `5m` | 783,380.00 USD | -14,310,000.00 USD | **`DISTRIBUTION`** |
| `15m` | 1,210,000.00 USD | 12,810,000.00 USD | **`ACCUMULATION`** |
| `30m` | 470,790.00 USD | 2,800,000.00 USD | **`ACCUMULATION`** |
| `1h` | -3,000,000.00 USD | -3,480,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 9,290,000.00 USD | 87,770,000.00 USD | **`ACCUMULATION`** |
| `4h` | -25,060,000.00 USD | -57,050,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -54,340,000.00 USD | -579,350,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -62,920,000.00 USD | -1,620,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -156,490,000.00 USD | -1,910,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -133,940,000.00 USD | -1,970,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -154,480,000.00 USD | -3,050,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,160,000,000.00 USD | -9,630,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+783.38K` | 15m=`+1.21M` | 1h=`-3.00M` | 24h=`-133.94M`
* Futures Capital Netflows: 5m=`-14.31M` | 15m=`+12.81M` | 1h=`-3.48M` | 24h=`-1.97B`
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
  * `2026-10-30 09:50:40 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:48:40 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:49:40 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2206.95` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2183.13` (Risk Distance: `23.82` pts)
  * +2.5R Take Profit: `2266.50`
  * Mathematical Lot Sizing: **`0.41 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2275.75` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2299.57` (Risk Distance: `23.82` pts)
  * +2.5R Take Profit: `2216.20`
  * Mathematical Lot Sizing: **`0.41 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2259.28`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
