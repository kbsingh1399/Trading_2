# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 08:54:58 IST` (`2026-10-30 03:24:58 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2210.00` | **Live Ask Quote**: `2212.80` | **Mid Price**: `2211.40`
- **Spread Points**: `280.00` | **Spread BPS**: `12.66 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2207.08` | VWAP Z-Score: `-0.10` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `19.47` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `34.16` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2247.75` | Lower -3.00σ Band: `2166.40`
  * Upper +2.51σ Band: `2241.11` | Lower -2.51σ Band: `2173.04`
  * Upper +2.01σ Band: `2234.33` | Lower -2.01σ Band: `2179.82`
  * Upper +2.00σ Band: `2234.19` | Lower -2.00σ Band: `2179.96`
  * Upper +1.28σ Band: `2224.43` | Lower -1.28σ Band: `2189.72`
  * Upper +1.00σ Band: `2220.64` | Lower -1.00σ Band: `2193.52`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2208.31` | EMA-20=`2225.73` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2262.93` (Slope: `+0.0000`) | EMA-100=`2289.58`
  * Institutional Anchors: EMA-144=`2300.15` | EMA-200=`2307.62` (Slope: `-0.5646`) | EMA-233=`2312.41`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2288.70` (Distance: `-3.38%`)
  * Point of Control (POC) = `2264.42` (Distance: `-2.35%`)
  * Value Area Low (VAL) = `2206.95` (Distance: `+0.20%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2350.38` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2220.25` | Low=`2202.55`
  * New York Session (13:00-21:00 UTC): High=`2224.67` | Low=`2198.13`
  * Initial Balance (First Hour): IB High=`2218.03` | IB Low=`2204.77`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2202.55` - `2220.25`
  * Optimal Trade Entry (OTE 0.705): `2215.82`
  * Structural Invalidation Anchor (0.786): `2229.09`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2208.98` | `2210.00` | `2207.29` | `2209.27` | `8,574` | 18,936,798.67 USD | -2,959,452.02 USD | `-15.63%` | -1,026,855,256.96 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `2209.27` | `2215.81` | `2208.12` | `2213.93` | `13,024` | 28,826,765.01 USD | 7,857,019.89 USD | `+27.26%` | -1,018,998,237.07 USD | `+0.58` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `2213.94` | `2218.44` | `2212.24` | `2218.17` | `12,623` | 27,969,990.31 USD | 8,594,257.94 USD | `+30.73%` | -1,010,403,979.13 USD | `+0.59` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `2213.76` | `2218.96` | `2209.66` | `2215.49` | `46,102` | 102,137,358.80 USD | -620,766.68 USD | `-0.61%` | -1,009,536,458.77 USD | `+0.39` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2215.49` | `2215.50` | `2207.29` | `2209.27` | `31,390` | 69,365,754.50 USD | -19,272,000.77 USD | `-27.78%` | -1,028,808,459.54 USD | `-0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2209.27` | `2218.44` | `2208.12` | `2218.15` | `25,576` | 56,640,656.70 USD | 16,295,179.20 USD | `+28.77%` | -1,012,513,280.33 USD | `+0.76` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `2221.62` | `2227.62` | `2172.85` | `2194.70` | `610,884` | 1,342,330,424.04 USD | -132,826,407.64 USD | `-9.90%` | -1,075,617,565.11 USD | `-0.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2194.71` | `2218.96` | `2181.22` | `2209.27` | `270,460` | 596,517,649.16 USD | 43,347,954.49 USD | `+7.27%` | -1,032,269,610.63 USD | `+0.85` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2209.27` | `2218.44` | `2208.12` | `2218.15` | `25,576` | 56,640,656.70 USD | 16,295,179.20 USD | `+28.77%` | -1,015,974,431.42 USD | `+0.58` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -182,194,938.56 USD | `-1.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -736,432,507.87 USD | `-1.81` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2218.15` | `1,753,752` | 3,874,618,953.49 USD | -279,497,937.84 USD | `-7.21%` | -1,015,930,445.72 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -84,078,993.86 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | 19,961,178.38 USD | `+1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -182,194,938.56 USD | `-1.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -736,432,507.87 USD | `-1.81` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2218.15` | `1,753,752` | 3,874,618,953.49 USD | -279,497,937.84 USD | `-7.21%` | -1,015,930,445.72 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2211.40`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2213.40` | `323.8700` | 716,853.86 USD | 9,822,882.18 USD | `10 orders` | `-0.09%` | `-` |
| `BID` | `2213.50` | `96.2660` | 213,084.79 USD | 9,106,028.32 USD | `6 orders` | `-0.08%` | `-` |
| `BID` | `2213.60` | `419.6410` | 928,917.32 USD | 8,892,943.53 USD | `4 orders` | `-0.08%` | `-` |
| `BID` | `2213.70` | `155.6404` | 344,541.15 USD | 7,964,026.21 USD | `7 orders` | `-0.07%` | `-` |
| `BID` | `2213.80` | `267.6384` | 592,497.89 USD | 7,619,485.06 USD | `9 orders` | `-0.07%` | `-` |
| `BID` | `2213.90` | `460.9131` | 1,020,415.51 USD | 7,026,987.17 USD | `7 orders` | `-0.07%` | `-` |
| `BID` | `2214.00` | `413.0880` | 914,576.83 USD | 6,006,571.66 USD | `13 orders` | `-0.06%` | `-` |
| `BID` | `2214.10` | `265.8821` | 588,689.56 USD | 5,091,994.82 USD | `8 orders` | `-0.06%` | `-` |
| `BID` | `2214.20` | `288.8040` | 639,469.82 USD | 4,503,305.27 USD | `9 orders` | `-0.05%` | `-` |
| `BID` | `2214.30` | `663.8735` | 1,470,015.09 USD | 3,863,835.45 USD | `12 orders` | `-0.05%` | `-` |
| `BID` | `2214.40` | `139.5263` | 308,967.04 USD | 2,393,820.36 USD | `11 orders` | `-0.04%` | `-` |
| `BID` | `2214.50` | `245.3115` | 543,242.32 USD | 2,084,853.32 USD | `13 orders` | `-0.04%` | `-` |
| `BID` | `2214.60` | `284.6763` | 630,444.13 USD | 1,541,611.00 USD | `9 orders` | `-0.03%` | `-` |
| `BID` | `2214.70` | `176.2237` | 390,282.63 USD | 911,166.87 USD | `9 orders` | `-0.03%` | `-` |
| `BID` | `2214.80` | `84.4166` | 186,965.89 USD | 520,884.24 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `2214.90` | `70.2765` | 155,655.42 USD | 333,918.35 USD | `9 orders` | `-0.02%` | `-` |
| `BID` | `2215.00` | `17.0581` | 37,783.69 USD | 178,262.93 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `2215.10` | `15.9703` | 35,375.81 USD | 140,479.24 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `2215.20` | `25.8492` | 57,261.15 USD | 105,103.43 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `2215.30` | `21.5963` | 47,842.28 USD | 47,842.28 USD | `7 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2215.35` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,215.35` | `0.00%` | `-` |
| `ASK` | `2215.40` | `179.5139` | 397,695.09 USD | 397,695.09 USD | `30 orders` | `+0.00%` | `-` |
| `ASK` | `2215.50` | `32.8097` | 72,689.89 USD | 470,384.98 USD | `7 orders` | `+0.01%` | `-` |
| `ASK` | `2215.60` | `105.5970` | 233,960.71 USD | 704,345.70 USD | `8 orders` | `+0.01%` | `-` |
| `ASK` | `2215.70` | `43.6715` | 96,762.94 USD | 801,108.64 USD | `7 orders` | `+0.02%` | `-` |
| `ASK` | `2215.80` | `101.4961` | 224,895.06 USD | 1,026,003.70 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `2215.90` | `451.6616` | 1,000,836.94 USD | 2,026,840.64 USD | `9 orders` | `+0.02%` | `-` |
| `ASK` | `2216.00` | `145.7220` | 322,919.95 USD | 2,349,760.59 USD | `8 orders` | `+0.03%` | `-` |
| `ASK` | `2216.10` | `186.2243` | 412,691.67 USD | 2,762,452.26 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `2216.20` | `216.4062` | 479,599.42 USD | 3,242,051.68 USD | `8 orders` | `+0.04%` | `-` |
| `ASK` | `2216.30` | `111.9361` | 248,083.98 USD | 3,490,135.66 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `2216.40` | `397.4650` | 880,941.43 USD | 4,371,077.09 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `2216.50` | `46.8613` | 103,868.07 USD | 4,474,945.16 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `2216.60` | `251.0664` | 556,513.78 USD | 5,031,458.94 USD | `8 orders` | `+0.06%` | `-` |
| `ASK` | `2216.70` | `679.3377` | 1,505,887.88 USD | 6,537,346.82 USD | `11 orders` | `+0.06%` | `-` |
| `ASK` | `2216.80` | `221.6790` | 491,418.01 USD | 7,028,764.83 USD | `11 orders` | `+0.07%` | `-` |
| `ASK` | `2216.90` | `190.6468` | 422,644.89 USD | 7,451,409.72 USD | `14 orders` | `+0.07%` | `-` |
| `ASK` | `2217.00` | `248.4538` | 550,822.07 USD | 8,002,231.79 USD | `15 orders` | `+0.07%` | `-` |
| `ASK` | `2217.10` | `73.2779` | 162,464.43 USD | 8,164,696.22 USD | `13 orders` | `+0.08%` | `-` |
| `ASK` | `2217.20` | `327.7650` | 726,720.56 USD | 8,891,416.78 USD | `9 orders` | `+0.08%` | `-` |
| `ASK` | `2217.30` | `281.7344` | 624,689.69 USD | 9,516,106.47 USD | `13 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:53:31 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1786.57` | `30,282.40` | 54,101,711.67 USD | `AT_RISK_LIQ` | `0xde8d9e530b` | `2026-10-30 08:53:31 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1798.87` | `15,927.59` | 28,651,645.16 USD | `AT_RISK_LIQ` | `0x60468ba274` | `2026-10-30 08:53:31 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 08:53:31 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `10,000.00` | 19,261,000.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 08:53:31 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1931.99` | `8,092.45` | 15,634,532.33 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 08:53:31 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2122.31` | `30,641.99` | 65,031,888.12 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 08:53:31 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.59` | `26,025.05` | 55,422,703.86 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 08:53:31 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2150.00` | `1,500.00` | 3,225,000.00 USD | `TRIGGER_STOP` | `0x834cae1ec1` | `2026-10-30 08:53:31 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,000.00` | 6,525,000.00 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2175.10` | `2,140.64` | 4,656,113.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2176.80` | `471.46` | 1,026,278.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2181.90` | `4,764.46` | 10,395,575.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2186.20` | `1,473.87` | 3,222,183.78 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2194.30` | `471.10` | 1,033,741.31 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2194.50` | `1,024.89` | 2,249,130.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2195.30` | `362.01` | 794,719.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2195.50` | `347.04` | 761,925.44 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2196.20` | `2,457.46` | 5,397,069.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2200.60` | `470.75` | 1,035,936.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.00` | `239.72` | 527,621.08 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9362ca4dfd` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.80` | `1,820.51` | 4,008,408.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2202.10` | `351.13` | 773,213.68 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2203.30` | `1,364.51` | 3,006,423.12 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2203.50` | `705.97` | 1,555,615.03 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2203.60` | `1,253.81` | 2,762,885.36 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2203.70` | `440.61` | 970,976.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2207.00` | `908.17` | 2,004,340.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2207.90` | `497.75` | 1,098,977.15 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2208.50` | `234.05` | 516,906.05 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2208.90` | `680.42` | 1,502,979.08 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2210.20` | `349.92` | 773,392.74 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2210.40` | `453.39` | 1,002,168.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.60` | `339.83` | 751,562.28 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2212.50` | `249.13` | 551,190.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2215.30` | `248.81` | 551,197.88 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2216.10` | `339.17` | 751,631.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2217.10` | `338.01` | 749,400.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2218.30` | `451.96` | 1,002,588.64 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2218.60` | `254.59` | 564,828.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2219.10` | `488.64` | 1,084,348.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2219.20` | `677.44` | 1,503,366.64 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2221.30` | `902.35` | 2,004,383.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2222.20` | `478.74` | 1,063,849.36 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2223.10` | `1,352.38` | 3,006,484.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2223.10` | `1,252.34` | 2,784,077.28 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2223.90` | `336.90` | 749,230.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2224.20` | `511.98` | 1,138,737.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2224.80` | `691.74` | 1,538,986.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2225.00` | `1,801.70` | 4,008,771.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2227.80` | `2,457.46` | 5,474,725.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2229.20` | `511.84` | 1,141,002.64 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2230.60` | `982.17` | 2,190,819.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2231.60` | `356.12` | 794,719.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2233.80` | `341.09` | 761,925.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2238.30` | `392.01` | 877,439.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x6798a1b850` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2239.60` | `1,427.76` | 3,197,608.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2242.00` | `4,764.46` | 10,681,919.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2246.10` | `511.73` | 1,149,399.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:53:31 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2249.60` | `2,108.45` | 4,743,170.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:53:31 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2486.04` | `22,046.99` | 54,809,797.89 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 08:53:31 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,037.41` | 7,635,751.54 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 08:53:31 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2624.31` | `10,000.00` | 26,243,106.87 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 08:53:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 235,704,588.54 USD | `106,417.71` | `2322.74` | `2216.40` | `3841.54` | 11,476,423.62 USD | `+4.87%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 143,351,658.55 USD | `64,680.62` | `2375.30` | `2216.40` | `4417.92` | 10,284,638.95 USD | `+7.17%` | `5X Cross` |
| `10` | `0x77dd...e0e9` | `LONG` | 67,960,873.39 USD | `30,641.99` | `2610.31` | `2216.40` | `2122.22` | -12,024,301.65 USD | `-17.69%` | `10X Cross` |
| `11` | `0xde8d...9524` | `LONG` | 67,081,580.23 USD | `30,282.40` | `2134.45` | `2216.40` | `1786.48` | 2,445,249.66 USD | `+3.65%` | `20X Cross` |
| `16` | `0x0392...d7d9` | `LONG` | 57,666,308.23 USD | `26,025.05` | `2518.71` | `2216.40` | `2129.50` | -7,883,413.86 USD | `-13.67%` | `9X Cross` |
| `23` | `0x8add...7d2c` | `SHORT` | 48,871,560.07 USD | `22,046.99` | `2271.09` | `2216.40` | `2482.19` | 1,199,337.23 USD | `+2.45%` | `25X Cross` |
| `26` | `0xdf95...7d72` | `SHORT` | 44,300,691.04 USD | `19,982.27` | `2402.53` | `2216.40` | `4229.19` | 3,707,401.67 USD | `+8.37%` | `25X Cross` |
| `35` | `0xeced...6210` | `SHORT` | 36,991,350.38 USD | `16,687.58` | `2522.09` | `2216.40` | `3471.71` | 5,096,364.61 USD | `+13.78%` | `20X Cross` |
| `36` | `0xb695...a92d` | `SHORT` | 35,962,282.38 USD | `16,214.56` | `2557.74` | `2216.40` | `3958.59` | 5,510,446.45 USD | `+15.32%` | `20X Cross` |
| `37` | `0x6046...b21d` | `LONG` | 35,278,018.43 USD | `15,927.59` | `2410.19` | `2216.40` | `1794.34` | -3,110,601.22 USD | `-8.82%` | `6X Cross` |
| `40` | `0x45d2...4029` | `SHORT` | 30,939,705.00 USD | `13,950.00` | `2443.60` | `2216.40` | `5432.66` | 3,148,577.46 USD | `+10.18%` | `20X Cross` |
| `44` | `0xa61c...66b9` | `LONG` | 28,562,385.60 USD | `12,888.00` | `2369.69` | `2216.40` | `1472.41` | -1,978,268.94 USD | `-6.93%` | `10X Cross` |
| `46` | `0x2371...0883` | `LONG` | 26,595,600.00 USD | `12,000.00` | `2421.77` | `2216.40` | `1279.45` | -2,465,694.85 USD | `-9.27%` | `20X Cross` |
| `47` | `0xbd1c...ff0e` | `LONG` | 26,587,200.00 USD | `12,000.00` | `2419.91` | `2216.40` | `1520.36` | -2,451,832.39 USD | `-9.22%` | `20X Cross` |
| `54` | `0x6c93...59a4` | `LONG` | 24,388,100.00 USD | `11,000.00` | `2441.15` | `2216.40` | `1602.39` | -2,464,572.73 USD | `-10.11%` | `20X Cross` |
| `55` | `0x09dc...c094` | `LONG` | 24,378,200.00 USD | `11,000.00` | `2465.31` | `2216.40` | `1637.42` | -2,740,223.04 USD | `-11.24%` | `20X Cross` |
| `56` | `0xa9de...e049` | `LONG` | 24,363,900.00 USD | `11,000.00` | `2481.81` | `2216.40` | `1644.10` | -2,936,079.46 USD | `-12.05%` | `20X Cross` |
| `57` | `0x0c5d...36b3` | `LONG` | 24,363,900.00 USD | `11,000.00` | `2482.20` | `2216.40` | `1644.43` | -2,940,353.24 USD | `-12.07%` | `20X Cross` |
| `71` | `0xa2ce...3126` | `LONG` | 22,193,388.69 USD | `10,016.88` | `2162.83` | `2216.40` | `1566.08` | 528,586.64 USD | `+2.38%` | `10X Cross` |
| `72` | `0xb37f...66ca` | `SHORT` | 22,179,000.00 USD | `10,000.00` | `2290.69` | `2216.40` | `2624.22` | 727,991.85 USD | `+3.28%` | `25X Cross` |
| `73` | `0x6646...6de5` | `LONG` | 22,171,000.00 USD | `10,000.00` | `1765.80` | `2216.40` | `1723.73` | 4,512,942.55 USD | `+20.36%` | `25X Cross` |
| `74` | `0xec7f...df39` | `LONG` | 22,162,000.00 USD | `10,000.00` | `2719.35` | `2216.40` | `1720.95` | -5,031,548.52 USD | `-22.70%` | `20X Cross` |
| `75` | `0x15a4...dfdb` | `LONG` | 22,149,000.00 USD | `10,000.00` | `1761.94` | `2216.40` | `358.44` | 4,529,518.97 USD | `+20.45%` | `20X Cross` |
| `77` | `0x939f...04d2` | `LONG` | 21,758,763.19 USD | `9,823.81` | `2427.28` | `2216.40` | `1690.77` | -2,086,387.41 USD | `-9.59%` | `25X Cross` |
| `78` | `0xaeaa...2416` | `SHORT` | 21,498,110.00 USD | `9,700.00` | `2311.92` | `2216.40` | `2658.08` | 927,572.40 USD | `+4.31%` | `25X Cross` |
| `84` | `0xf517...c032` | `SHORT` | 20,676,511.52 USD | `9,326.35` | `2202.91` | `2216.40` | `3114.06` | -131,373.31 USD | `-0.64%` | `25X Cross` |
| `86` | `0xca49...53c8` | `SHORT` | 20,385,477.70 USD | `9,200.88` | `2549.39` | `2216.40` | `3920.98` | 3,071,229.82 USD | `+15.07%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 20,070,272.46 USD | `9,054.12` | `2493.89` | `2216.40` | `2946.18` | 2,509,734.80 USD | `+12.50%` | `20X Cross` |
| `89` | `0xea00...a918` | `LONG` | 19,945,276.02 USD | `9,003.83` | `2003.01` | `2216.40` | `1422.47` | 1,910,497.15 USD | `+9.58%` | `5X Cross` |
| `93` | `0xefe4...194b` | `SHORT` | 19,555,211.89 USD | `8,820.57` | `2267.42` | `2216.40` | `3607.15` | 444,802.50 USD | `+2.27%` | `20X Cross` |
| `114` | `0x9eec...daab` | `LONG` | 17,948,249.51 USD | `8,092.45` | `1658.44` | `2216.40` | `1931.24` | 4,527,384.98 USD | `+25.22%` | `15X Cross` |
| `117` | `0x5f91...65aa` | `LONG` | 17,643,305.75 USD | `7,964.66` | `1626.99` | `2216.40` | `1844.27` | 4,684,862.68 USD | `+26.55%` | `16X Cross` |
| `129` | `0xec0b...b078` | `LONG` | 15,536,290.16 USD | `7,007.80` | `2065.97` | `2216.40` | `1071.38` | 1,058,360.57 USD | `+6.81%` | `25X Cross` |
| `132` | `0xf02d...5eb3` | `LONG` | 15,199,719.85 USD | `6,855.99` | `2383.33` | `2216.40` | `1142.75` | -1,140,368.91 USD | `-7.50%` | `20X Cross` |
| `133` | `0xcf53...ee11` | `SHORT` | 15,074,117.98 USD | `6,803.63` | `1862.69` | `2216.40` | `4238.85` | -2,401,012.59 USD | `-15.93%` | `7X Cross` |
| `136` | `0x418a...8888` | `SHORT` | 14,902,577.16 USD | `6,724.38` | `2494.55` | `2216.40` | `3022.84` | 1,871,746.01 USD | `+12.56%` | `25X Cross` |
| `139` | `0x4ff9...38d3` | `LONG` | 14,550,637.59 USD | `6,564.10` | `2447.40` | `2216.40` | `1670.04` | -1,514,385.16 USD | `-10.41%` | `3X Isolated` |
| `141` | `0xf78c...c581` | `LONG` | 14,403,190.80 USD | `6,500.22` | `2521.53` | `2216.40` | `1913.52` | -1,987,350.15 USD | `-13.80%` | `20X Cross` |
| `146` | `0x799f...5f4c` | `LONG` | 13,991,272.62 USD | `6,310.90` | `2390.33` | `2216.40` | `1876.20` | -1,093,892.00 USD | `-7.82%` | `20X Cross` |
| `149` | `0x08bf...7872` | `SHORT` | 13,799,335.49 USD | `6,224.05` | `2258.00` | `2216.40` | `2585.31` | 254,580.62 USD | `+1.84%` | `20X Cross` |
| `153` | `0x1ee7...edf5` | `LONG` | 13,291,200.00 USD | `6,000.00` | `2308.18` | `2216.40` | `2052.69` | -557,880.40 USD | `-4.20%` | `25X Cross` |
| `154` | `0xd9e7...4aff` | `LONG` | 13,289,400.00 USD | `6,000.00` | `2480.18` | `2216.40` | `1407.81` | -1,591,724.33 USD | `-11.98%` | `20X Cross` |
| `162` | `0x0c4a...1b19` | `LONG` | 12,542,776.06 USD | `5,660.10` | `2373.06` | `2216.40` | `2081.86` | -888,982.07 USD | `-7.09%` | `25X Isolated` |
| `166` | `0xc179...e0c8` | `LONG` | 12,138,044.49 USD | `5,477.46` | `2307.01` | `2216.40` | `1012.26` | -498,524.92 USD | `-4.11%` | `10X Cross` |
| `169` | `0x7fda...17d1` | `LONG` | 11,785,036.82 USD | `5,315.76` | `2211.05` | `2216.40` | `0.000000` | 31,594.57 USD | `+0.27%` | `25X Cross` |
| `179` | `0x218a...7da2` | `SHORT` | 11,568,130.78 USD | `5,222.87` | `2208.16` | `2216.40` | `2792.96` | -35,195.72 USD | `-0.30%` | `10X Cross` |
| `187` | `0x45ab...6cbc` | `LONG` | 10,900,915.47 USD | `4,920.96` | `2727.66` | `2216.40` | `1392.74` | -2,521,828.33 USD | `-23.13%` | `7X Cross` |
| `191` | `0x64b7...9da9` | `LONG` | 10,768,098.19 USD | `4,856.84` | `2604.61` | `2216.40` | `1520.04` | -1,882,116.22 USD | `-17.48%` | `25X Cross` |
| `200` | `0xfb18...eb17` | `SHORT` | 10,575,353.30 USD | `4,768.18` | `2315.53` | `2216.40` | `2558.45` | 465,528.50 USD | `+4.40%` | `25X Cross` |
| `201` | `0x5559...d43b` | `SHORT` | 10,533,898.95 USD | `4,755.93` | `2262.69` | `2216.40` | `2742.06` | 227,306.93 USD | `+2.16%` | `25X Cross` |
| `207` | `0xecb6...2b00` | `SHORT` | 10,307,344.68 USD | `4,649.23` | `2249.48` | `2216.40` | `8449.42` | 151,027.25 USD | `+1.47%` | `15X Cross` |
| `209` | `0x0622...8088` | `LONG` | 10,098,480.98 USD | `4,555.64` | `2201.83` | `2216.40` | `15.82` | 67,724.93 USD | `+0.67%` | `5X Cross` |
| `214` | `0xe091...6705` | `SHORT` | 9,967,050.44 USD | `4,500.00` | `2467.33` | `2216.40` | `2463.43` | 1,135,958.07 USD | `+11.40%` | `20X Cross` |
| `223` | `0xb829...3a81` | `LONG` | 9,740,001.76 USD | `4,394.91` | `2398.60` | `2216.40` | `1493.16` | -801,640.19 USD | `-8.23%` | `20X Cross` |
| `240` | `0x28bb...fca6` | `SHORT` | 9,333,135.64 USD | `4,209.61` | `1896.10` | `2216.40` | `3035.16` | -1,351,253.08 USD | `-14.48%` | `20X Cross` |
| `244` | `0x6ea4...0ea7` | `SHORT` | 9,274,700.07 USD | `4,184.01` | `2602.13` | `2216.40` | `3425.37` | 1,612,646.60 USD | `+17.39%` | `20X Cross` |
| `255` | `0x5e9e...35ee` | `SHORT` | 8,882,346.45 USD | `4,007.56` | `1796.39` | `2216.40` | `2585.86` | -1,683,196.36 USD | `-18.95%` | `20X Cross` |
| `256` | `0xfb94...0ddf` | `SHORT` | 8,865,454.80 USD | `4,002.10` | `2382.44` | `2216.40` | `5104.76` | 669,329.35 USD | `+7.55%` | `20X Cross` |
| `257` | `0x8cc9...2b6a` | `SHORT` | 8,864,800.00 USD | `4,000.00` | `1791.18` | `2216.40` | `3629.97` | -1,700,053.33 USD | `-19.18%` | `25X Cross` |
| `258` | `0x3dc9...54b0` | `SHORT` | 8,862,513.55 USD | `3,999.69` | `2480.32` | `2216.40` | `6754.36` | 1,058,023.01 USD | `+11.94%` | `20X Cross` |
| `275` | `0x4b67...f4e7` | `LONG` | 8,463,928.98 USD | `3,820.84` | `2591.51` | `2216.40` | `1359.39` | -1,437,844.57 USD | `-16.99%` | `20X Cross` |
| `281` | `0x12d2...f97f` | `LONG` | 8,330,223.81 USD | `3,757.26` | `2446.50` | `2216.40` | `1828.99` | -861,942.58 USD | `-10.35%` | `20X Cross` |
| `299` | `0x8ae4...3d60` | `LONG` | 7,884,967.43 USD | `3,558.20` | `2482.21` | `2216.40` | `563.87` | -947,230.60 USD | `-12.01%` | `10X Cross` |
| `335` | `0x4a20...3c26` | `LONG` | 6,653,700.00 USD | `3,000.00` | `2428.72` | `2216.40` | `682.88` | -632,460.28 USD | `-9.51%` | `20X Cross` |
| `336` | `0x469e...58a5` | `SHORT` | 6,649,800.00 USD | `3,000.00` | `2195.70` | `2216.40` | `3209.87` | -62,692.76 USD | `-0.94%` | `25X Cross` |
| `337` | `0xb823...9763` | `SHORT` | 6,648,600.00 USD | `3,000.00` | `2229.66` | `2216.40` | `3233.76` | 40,396.68 USD | `+0.61%` | `25X Cross` |
| `338` | `0x007d...67a0` | `LONG` | 6,646,800.00 USD | `3,000.00` | `2400.00` | `2216.40` | `1467.36` | -553,200.00 USD | `-8.32%` | `25X Cross` |
| `377` | `0x9c2a...f6a8` | `SHORT` | 6,057,269.09 USD | `2,733.67` | `2543.83` | `2216.40` | `2643.36` | 896,737.20 USD | `+14.80%` | `20X Cross` |
| `393` | `0x8328...f54a` | `SHORT` | 5,706,581.54 USD | `2,576.45` | `2292.01` | `2216.40` | `3279.60` | 198,689.75 USD | `+3.48%` | `25X Cross` |
| `396` | `0xed48...7c9b` | `SHORT` | 5,657,897.22 USD | `2,551.13` | `2460.02` | `2216.40` | `3239.76` | 617,949.19 USD | `+10.92%` | `20X Cross` |
| `397` | `0x1c98...7fc7` | `LONG` | 5,541,509.97 USD | `2,500.00` | `2452.60` | `2216.40` | `1917.01` | -590,011.59 USD | `-10.65%` | `10X Cross` |
| `398` | `0x970c...2a93` | `SHORT` | 5,541,500.00 USD | `2,500.00` | `2229.57` | `2216.40` | `5084.47` | 32,444.49 USD | `+0.59%` | `20X Cross` |
| `411` | `0xfbe2...c8ea` | `SHORT` | 5,289,909.87 USD | `2,385.21` | `2041.57` | `2216.40` | `2621.43` | -420,343.21 USD | `-7.95%` | `20X Cross` |
| `412` | `0x6749...ce07` | `SHORT` | 5,287,548.93 USD | `2,384.89` | `2220.92` | `2216.40` | `3631.20` | 9,114.10 USD | `+0.17%` | `20X Cross` |
| `415` | `0x645b...87b8` | `SHORT` | 5,276,405.91 USD | `2,379.98` | `2421.64` | `2216.40` | `11676.41` | 487,041.05 USD | `+9.23%` | `10X Cross` |
| `422` | `0x77ee...2902` | `SHORT` | 5,077,775.18 USD | `2,290.69` | `2476.53` | `2216.40` | `5894.01` | 595,197.05 USD | `+11.72%` | `25X Cross` |
| `429` | `0xbcd4...0dd2` | `SHORT` | 5,016,594.39 USD | `2,263.50` | `2233.24` | `2216.40` | `2685.64` | 38,363.18 USD | `+0.76%` | `25X Cross` |
| `445` | `0xd507...c948` | `SHORT` | 4,815,323.78 USD | `2,172.00` | `2387.49` | `2216.40` | `2706.79` | 370,317.25 USD | `+7.69%` | `5X Isolated` |
| `457` | `0x382b...3e39` | `SHORT` | 4,719,490.09 USD | `2,129.54` | `2296.66` | `2216.40` | `4617.93` | 171,347.12 USD | `+3.63%` | `25X Cross` |
| `459` | `0x023a...2355` | `LONG` | 4,707,034.77 USD | `2,123.54` | `2330.15` | `2216.40` | `0.000000` | -241,139.04 USD | `-5.12%` | `25X Cross` |
| `463` | `0x5b5f...c052` | `SHORT` | 4,670,022.25 USD | `2,107.13` | `2237.36` | `2216.40` | `2254.11` | 44,381.16 USD | `+0.95%` | `25X Cross` |
| `491` | `0x3453...b323` | `SHORT` | 4,430,672.69 USD | `2,000.12` | `2322.47` | `2216.40` | `2396.59` | 214,563.15 USD | `+4.84%` | `25X Cross` |
| `492` | `0x7a6d...f79c` | `SHORT` | 4,429,800.00 USD | `2,000.00` | `2418.41` | `2216.40` | `2525.18` | 407,032.11 USD | `+9.19%` | `25X Cross` |
| `501` | `0xac48...3201` | `SHORT` | 4,351,471.32 USD | `1,964.37` | `2272.04` | `2216.40` | `3125.16` | 111,670.98 USD | `+2.57%` | `20X Cross` |
| `502` | `0xb15b...dbae` | `SHORT` | 4,345,803.14 USD | `1,961.19` | `2290.80` | `2216.40` | `2224.78` | 146,894.53 USD | `+3.38%` | `25X Cross` |
| `516` | `0x8376...9a1e` | `SHORT` | 4,232,130.74 USD | `1,910.50` | `2477.72` | `2216.40` | `3189.65` | 501,557.43 USD | `+11.85%` | `20X Cross` |
| `524` | `0xf3dc...1672` | `SHORT` | 4,166,504.57 USD | `1,880.36` | `2240.73` | `2216.40` | `2770.13` | 46,885.67 USD | `+1.13%` | `20X Cross` |
| `540` | `0x24fb...ed0f` | `LONG` | 4,046,263.52 USD | `1,826.10` | `2199.85` | `2216.40` | `914.23` | 29,119.39 USD | `+0.72%` | `15X Cross` |
| `547` | `0x7265...91a5` | `LONG` | 3,990,960.53 USD | `1,801.87` | `2533.96` | `2216.40` | `1987.49` | -574,905.92 USD | `-14.41%` | `20X Cross` |
| `548` | `0x739c...cfb2` | `SHORT` | 3,988,440.00 USD | `1,800.00` | `2427.60` | `2216.40` | `2443.76` | 381,256.38 USD | `+9.56%` | `25X Cross` |
| `554` | `0xa445...329d` | `LONG` | 3,940,652.27 USD | `1,776.75` | `2398.85` | `2216.40` | `2021.09` | -321,517.08 USD | `-8.16%` | `25X Cross` |
| `562` | `0x91a9...3f70` | `SHORT` | 3,917,265.92 USD | `1,767.48` | `2156.23` | `2216.40` | `3673.99` | -106,161.84 USD | `-2.71%` | `4X Cross` |
| `570` | `0xc619...10f5` | `LONG` | 3,879,050.00 USD | `1,750.00` | `2315.39` | `2216.40` | `1810.18` | -172,895.83 USD | `-4.46%` | `25X Cross` |
| `571` | `0xbb34...1696` | `LONG` | 3,876,600.00 USD | `1,750.00` | `2315.81` | `2216.40` | `1982.17` | -176,068.23 USD | `-4.54%` | `25X Cross` |
| `596` | `0xfeec...4e9c` | `SHORT` | 3,750,740.11 USD | `1,691.81` | `2566.49` | `2216.40` | `2510.69` | 591,284.40 USD | `+15.76%` | `10X Cross` |
| `598` | `0xd911...961e` | `LONG` | 3,748,556.59 USD | `1,690.82` | `2201.54` | `2216.40` | `889.67` | 26,129.43 USD | `+0.70%` | `25X Cross` |
| `605` | `0xb8eb...1dd5` | `LONG` | 3,704,916.27 USD | `1,671.14` | `2227.42` | `2216.40` | `1088.98` | -17,417.48 USD | `-0.47%` | `25X Cross` |
| `618` | `0xeee0...0b53` | `LONG` | 3,626,556.86 USD | `1,637.12` | `2468.64` | `2216.40` | `236.51` | -414,919.20 USD | `-11.44%` | `7X Cross` |
| `621` | `0x27b8...12fc` | `LONG` | 3,608,891.01 USD | `1,628.12` | `2468.73` | `2216.40` | `668.45` | -410,503.62 USD | `-11.37%` | `10X Cross` |
| `623` | `0x982b...4606` | `LONG` | 3,603,725.68 USD | `1,626.82` | `2575.24` | `2216.40` | `1547.77` | -585,727.39 USD | `-16.25%` | `5X Isolated` |
| `629` | `0x73d7...8be1` | `LONG` | 3,550,609.16 USD | `1,601.47` | `2410.40` | `2216.40` | `2030.88` | -309,569.76 USD | `-8.72%` | `25X Cross` |
| `631` | `0xad54...6203` | `LONG` | 3,538,195.77 USD | `1,597.45` | `2591.98` | `2216.40` | `2057.42` | -602,382.28 USD | `-17.03%` | `10X Isolated` |
| `635` | `0x880a...311c` | `LONG` | 3,498,680.77 USD | `1,578.40` | `2209.72` | `2216.40` | `0.000000` | 10,856.92 USD | `+0.31%` | `9X Cross` |
| `650` | `0xe170...9300` | `SHORT` | 3,397,861.06 USD | `1,533.40` | `2076.39` | `2216.40` | `3173.53` | -213,911.56 USD | `-6.30%` | `25X Cross` |
| `654` | `0x4b86...df9d` | `SHORT` | 3,375,507.60 USD | `1,524.00` | `2287.40` | `2216.40` | `2759.96` | 110,490.00 USD | `+3.27%` | `9X Isolated` |
| `662` | `0x2e2b...2fab` | `LONG` | 3,340,045.96 USD | `1,507.38` | `2245.53` | `2216.40` | `1288.32` | -44,827.14 USD | `-1.34%` | `25X Cross` |
| `665` | `0x251f...6e5d` | `LONG` | 3,325,500.00 USD | `1,500.00` | `2346.68` | `2216.40` | `1940.21` | -194,530.49 USD | `-5.85%` | `20X Cross` |
| `666` | `0xde6b...3361` | `LONG` | 3,324,900.00 USD | `1,500.00` | `2216.98` | `2216.40` | `2168.89` | -580.74 USD | `-0.02%` | `25X Cross` |
| `667` | `0xf929...d1f9` | `SHORT` | 3,322,350.00 USD | `1,500.00` | `2423.37` | `2216.40` | `2678.00` | 312,705.26 USD | `+9.41%` | `25X Cross` |
| `668` | `0x834c...dd93` | `SHORT` | 3,322,350.00 USD | `1,500.00` | `2191.89` | `2216.40` | `2237.94` | -34,511.05 USD | `-1.04%` | `25X Cross` |
| `686` | `0xb885...3c54` | `LONG` | 3,213,784.88 USD | `1,450.00` | `2274.34` | `2216.40` | `47.50` | -84,023.26 USD | `-2.61%` | `20X Cross` |
| `687` | `0x3440...32c5` | `SHORT` | 3,212,376.69 USD | `1,448.97` | `2198.21` | `2216.40` | `3912.24` | -27,225.72 USD | `-0.85%` | `25X Cross` |
| `692` | `0xef70...a84c` | `SHORT` | 3,198,706.39 USD | `1,442.74` | `2424.73` | `2216.40` | `3231.36` | 299,564.43 USD | `+9.37%` | `25X Cross` |
| `696` | `0x4b5f...0dd8` | `LONG` | 3,172,929.88 USD | `1,431.96` | `2339.45` | `2216.40` | `2148.05` | -177,063.07 USD | `-5.58%` | `10X Cross` |
| `704` | `0xbadb...9ee6` | `LONG` | 3,163,231.58 USD | `1,428.16` | `1936.00` | `2216.40` | `1085.67` | 398,309.94 USD | `+12.59%` | `20X Cross` |
| `744` | `0xa0fb...96be` | `LONG` | 3,050,053.23 USD | `1,376.25` | `2293.96` | `2216.40` | `1549.29` | -107,021.66 USD | `-3.51%` | `3X Cross` |
| `758` | `0x53f8...ceff` | `LONG` | 2,988,348.20 USD | `1,348.65` | `2276.73` | `2216.40` | `0.000000` | -82,176.27 USD | `-2.75%` | `20X Cross` |
| `778` | `0x0dd5...f6ee` | `LONG` | 2,912,593.50 USD | `1,315.00` | `2306.05` | `2216.40` | `1560.32` | -119,870.88 USD | `-4.12%` | `5X Cross` |
| `785` | `0x6e6f...82a6` | `LONG` | 2,887,802.10 USD | `1,303.22` | `2266.68` | `2216.40` | `1488.45` | -66,189.27 USD | `-2.29%` | `20X Cross` |
| `786` | `0x0a97...347d` | `LONG` | 2,887,533.87 USD | `1,302.45` | `2267.88` | `2216.40` | `1606.69` | -66,271.42 USD | `-2.30%` | `20X Cross` |
| `790` | `0xa70a...4be9` | `LONG` | 2,874,634.52 USD | `1,296.81` | `2259.47` | `2216.40` | `1133.06` | -55,471.75 USD | `-1.93%` | `20X Cross` |
| `810` | `0x1f16...6d07` | `LONG` | 2,807,481.60 USD | `1,266.00` | `2261.43` | `2216.40` | `1386.00` | -55,489.63 USD | `-1.98%` | `7X Cross` |
| `818` | `0xc435...c905` | `SHORT` | 2,764,195.20 USD | `1,248.00` | `2704.38` | `2216.40` | `4348.23` | 610,875.15 USD | `+22.10%` | `20X Cross` |
| `821` | `0x6859...7e1e` | `SHORT` | 2,742,769.97 USD | `1,237.15` | `2200.39` | `2216.40` | `4905.64` | -20,542.82 USD | `-0.75%` | `25X Cross` |
| `830` | `0x7277...0b98` | `SHORT` | 2,703,651.24 USD | `1,219.45` | `2206.05` | `2216.40` | `3376.84` | -13,463.44 USD | `-0.50%` | `20X Cross` |
| `831` | `0x7178...0854` | `LONG` | 2,700,365.54 USD | `1,218.63` | `2461.81` | `2216.40` | `1210.80` | -299,680.86 USD | `-11.10%` | `10X Cross` |
| `848` | `0xaaa1...ab8c` | `SHORT` | 2,658,240.00 USD | `1,200.00` | `2276.29` | `2216.40` | `2365.58` | 73,317.58 USD | `+2.76%` | `25X Isolated` |
| `857` | `0x07fd...689d` | `LONG` | 2,630,386.95 USD | `1,186.89` | `2416.34` | `2216.40` | `0.000000` | -237,555.40 USD | `-9.03%` | `25X Cross` |
| `929` | `0x2f80...f203` | `SHORT` | 2,413,311.27 USD | `1,088.94` | `1984.00` | `2216.40` | `2958.20` | -252,844.08 USD | `-10.48%` | `20X Cross` |
| `938` | `0x6f11...0389` | `SHORT` | 2,391,387.70 USD | `1,079.00` | `2333.39` | `2216.40` | `3199.06` | 126,341.21 USD | `+5.28%` | `25X Cross` |
| `941` | `0x8eb7...b90f` | `LONG` | 2,387,407.88 USD | `1,077.74` | `2396.38` | `2216.40` | `1881.30` | -195,270.17 USD | `-8.18%` | `5X Isolated` |
| `942` | `0x2b61...2f6c` | `SHORT` | 2,386,493.01 USD | `1,076.60` | `2681.75` | `2216.40` | `6453.99` | 500,679.73 USD | `+20.98%` | `10X Cross` |
| `962` | `0x30af...393e` | `SHORT` | 2,307,533.77 USD | `1,041.16` | `2252.26` | `2216.40` | `2297.27` | 37,448.56 USD | `+1.62%` | `25X Cross` |
| `976` | `0x1b2a...f7a6` | `LONG` | 2,271,395.19 USD | `1,025.37` | `2737.51` | `2216.40` | `882.43` | -535,564.74 USD | `-23.58%` | `10X Cross` |
| `984` | `0x001a...fef6` | `SHORT` | 2,233,340.26 USD | `1,007.33` | `2022.19` | `2216.40` | `3095.59` | -196,332.30 USD | `-8.79%` | `10X Cross` |
| `985` | `0x02aa...1806` | `SHORT` | 2,232,841.63 USD | `1,007.10` | `2654.68` | `2216.40` | `3613.06` | 440,690.47 USD | `+19.74%` | `20X Cross` |
| `986` | `0xdb3a...cf3b` | `LONG` | 2,224,228.20 USD | `1,003.22` | `2705.01` | `2216.40` | `0.000000` | -489,478.70 USD | `-22.01%` | `4X Cross` |
| `988` | `0x5272...fcd9` | `SHORT` | 2,217,100.00 USD | `1,000.00` | `2241.82` | `2216.40` | `2831.11` | 24,724.49 USD | `+1.12%` | `5X Cross` |
| `990` | `0x8c02...b73f` | `SHORT` | 2,215,800.00 USD | `1,000.00` | `2250.37` | `2216.40` | `8098.74` | 34,571.47 USD | `+1.56%` | `20X Cross` |
| `991` | `0xd7b8...9f55` | `LONG` | 2,212,685.10 USD | `999.00` | `2195.00` | `2216.40` | `0.000000` | 19,880.10 USD | `+0.90%` | `15X Cross` |
| `1001` | `0x2577...4897` | `LONG` | 2,186,818.87 USD | `986.39` | `2233.53` | `2216.40` | `0.000000` | -16,310.69 USD | `-0.75%` | `15X Cross` |
| `1018` | `0xb002...ed8a` | `SHORT` | 2,132,759.12 USD | `962.78` | `2299.66` | `2216.40` | `4201.80` | 81,318.79 USD | `+3.81%` | `25X Cross` |
| `1030` | `0xb812...b5e0` | `LONG` | 2,086,016.67 USD | `941.05` | `2263.21` | `2216.40` | `1187.32` | -43,772.23 USD | `-2.10%` | `25X Cross` |
| `1043` | `0xb1ec...e86a` | `SHORT` | 2,068,755.97 USD | `933.64` | `2272.72` | `2216.40` | `12538.67` | 53,150.99 USD | `+2.57%` | `25X Cross` |
| `1058` | `0xef96...9383` | `LONG` | 2,034,263.55 USD | `917.57` | `2235.00` | `2216.40` | `0.000000` | -16,520.10 USD | `-0.81%` | `25X Cross` |
| `1064` | `0xede2...f971` | `LONG` | 2,025,750.33 USD | `914.31` | `2208.16` | `2216.40` | `1463.34` | 6,793.34 USD | `+0.34%` | `5X Cross` |
| `1066` | `0x9606...4e5d` | `SHORT` | 2,023,109.39 USD | `913.00` | `2478.70` | `2216.40` | `4440.69` | 239,944.22 USD | `+11.86%` | `20X Cross` |
| `1085` | `0x5f10...d49d` | `LONG` | 1,995,390.00 USD | `900.00` | `2249.83` | `2216.40` | `1831.41` | -29,463.47 USD | `-1.48%` | `25X Cross` |
| `1106` | `0x82f6...12ec` | `SHORT` | 1,964,653.95 USD | `887.02` | `2199.66` | `2216.40` | `2249.63` | -13,511.13 USD | `-0.69%` | `25X Cross` |
| `1169` | `0x9599...c60a` | `LONG` | 1,867,822.45 USD | `842.80` | `2231.08` | `2216.40` | `0.000000` | -12,541.14 USD | `-0.67%` | `20X Cross` |
| `1175` | `0xcd27...52a8` | `LONG` | 1,855,504.76 USD | `837.21` | `2553.56` | `2216.40` | `1403.58` | -282,360.02 USD | `-15.22%` | `2X Cross` |
| `1234` | `0x04a9...95aa` | `LONG` | 1,773,040.00 USD | `800.00` | `2595.13` | `2216.40` | `1870.93` | -303,066.74 USD | `-17.09%` | `5X Cross` |
| `1236` | `0x7737...bf66` | `SHORT` | 1,772,258.87 USD | `799.79` | `2494.83` | `2216.40` | `23462.34` | 223,087.16 USD | `+12.59%` | `15X Cross` |
| `1243` | `0x2e30...4cb5` | `SHORT` | 1,755,259.98 USD | `791.83` | `2335.10` | `2216.40` | `8531.09` | 93,755.61 USD | `+5.34%` | `2X Cross` |
| `1263` | `0x458d...ab3b` | `LONG` | 1,715,987.13 USD | `774.75` | `2740.41` | `2216.40` | `1887.33` | -407,142.05 USD | `-23.73%` | `3X Isolated` |
| `1283` | `0x31de...13f2` | `LONG` | 1,681,263.50 USD | `758.35` | `2254.82` | `2216.40` | `0.000000` | -28,687.06 USD | `-1.71%` | `20X Cross` |
| `1324` | `0xaa53...9cb7` | `LONG` | 1,619,229.50 USD | `730.34` | `2389.70` | `2216.40` | `1944.09` | -126,060.14 USD | `-7.79%` | `20X Cross` |
| `1325` | `0x3fc5...c0c1` | `SHORT` | 1,617,366.04 USD | `729.92` | `2702.11` | `2216.40` | `4845.81` | 354,976.16 USD | `+21.95%` | `25X Cross` |
| `1327` | `0x6463...42f5` | `LONG` | 1,610,914.78 USD | `726.88` | `2214.40` | `2216.40` | `0.000000` | 1,304.12 USD | `+0.08%` | `1X Cross` |
| `1346` | `0xa189...94d7` | `SHORT` | 1,596,121.45 USD | `719.98` | `2691.84` | `2216.40` | `2915.17` | 341,951.22 USD | `+21.42%` | `25X Cross` |
| `1349` | `0xf71a...7215` | `LONG` | 1,593,559.59 USD | `719.02` | `2215.26` | `2216.40` | `1721.45` | 742.60 USD | `+0.05%` | `25X Cross` |
| `1361` | `0x2f93...4404` | `LONG` | 1,568,464.32 USD | `707.47` | `1700.45` | `2216.40` | `1368.97` | 365,437.94 USD | `+23.30%` | `4X Isolated` |
| `1365` | `0x71d0...8c26` | `LONG` | 1,559,003.05 USD | `703.20` | `2225.97` | `2216.40` | `0.000000` | -6,313.53 USD | `-0.40%` | `25X Cross` |
| `1367` | `0x5605...fe0f` | `SHORT` | 1,556,090.65 USD | `702.14` | `2566.90` | `2216.40` | `3091.61` | 246,242.00 USD | `+15.82%` | `20X Cross` |
| `1372` | `0x7743...e4fe` | `SHORT` | 1,553,203.15 USD | `700.56` | `2298.56` | `2216.40` | `6178.20` | 57,071.94 USD | `+3.67%` | `25X Cross` |
| `1374` | `0x0deb...0bc5` | `LONG` | 1,551,970.00 USD | `700.00` | `2071.05` | `2216.40` | `1597.56` | 102,234.21 USD | `+6.59%` | `20X Cross` |
| `1394` | `0xf910...0a2d` | `LONG` | 1,540,916.99 USD | `695.30` | `2224.32` | `2216.40` | `0.000000` | -5,648.08 USD | `-0.37%` | `5X Cross` |
| `1424` | `0x0c68...82d0` | `LONG` | 1,514,232.20 USD | `683.10` | `2207.13` | `2216.40` | `0.000000` | 6,535.58 USD | `+0.43%` | `6X Cross` |
| `1430` | `0xdbd1...29dd` | `SHORT` | 1,509,185.51 USD | `680.70` | `3030.57` | `2216.40` | `3771.55` | 553,735.61 USD | `+36.69%` | `6X Cross` |
| `1435` | `0x71e5...be04` | `LONG` | 1,502,455.06 USD | `677.67` | `2727.27` | `2216.40` | `1471.11` | -345,730.54 USD | `-23.01%` | `20X Cross` |
| `1438` | `0xbef3...0d3e` | `LONG` | 1,500,414.77 USD | `677.33` | `2228.39` | `2216.40` | `2103.35` | -8,934.73 USD | `-0.60%` | `20X Cross` |
| `1439` | `0x6a41...a3b9` | `LONG` | 1,498,079.39 USD | `675.69` | `2227.91` | `2216.40` | `2107.90` | -7,310.81 USD | `-0.49%` | `20X Cross` |
| `1442` | `0x0b23...f37b` | `LONG` | 1,496,947.50 USD | `675.00` | `2238.15` | `2216.40` | `605.86` | -13,809.14 USD | `-0.92%` | `5X Cross` |
| `1477` | `0x0cac...6170` | `SHORT` | 1,456,757.00 USD | `657.50` | `2146.55` | `2216.40` | `2839.55` | -45,394.80 USD | `-3.12%` | `20X Cross` |
| `1505` | `0xf00e...fe3d` | `SHORT` | 1,425,264.96 USD | `642.88` | `2333.21` | `2216.40` | `2506.62` | 74,713.01 USD | `+5.24%` | `20X Cross` |
| `1511` | `0xffb2...5ed6` | `SHORT` | 1,420,387.77 USD | `640.77` | `2672.96` | `2216.40` | `2470.46` | 292,360.58 USD | `+20.58%` | `20X Cross` |
| `1524` | `0x8505...1821` | `SHORT` | 1,405,553.38 USD | `633.96` | `2239.93` | `2216.40` | `3837.25` | 14,478.22 USD | `+1.03%` | `20X Cross` |
| `1543` | `0x51f6...2b39` | `LONG` | 1,387,517.61 USD | `626.08` | `2224.08` | `2216.40` | `53.34` | -4,934.17 USD | `-0.36%` | `25X Cross` |
| `1545` | `0xfce0...f4c0` | `SHORT` | 1,381,772.88 USD | `623.60` | `3129.61` | `2216.40` | `2784.94` | 569,853.70 USD | `+41.24%` | `20X Cross` |
| `1581` | `0xad02...eb65` | `LONG` | 1,331,635.05 USD | `600.62` | `2460.69` | `2216.40` | `1079.03` | -146,305.51 USD | `-10.99%` | `5X Cross` |
| `1583` | `0x816f...f299` | `LONG` | 1,330,740.00 USD | `600.00` | `2203.57` | `2216.40` | `1946.09` | 8,594.90 USD | `+0.65%` | `25X Cross` |
| `1586` | `0x638f...f5f0` | `LONG` | 1,329,360.00 USD | `600.00` | `4011.50` | `2216.40` | `485.37` | -1,077,543.53 USD | `-81.06%` | `25X Cross` |
| `1587` | `0x26e6...6b28` | `LONG` | 1,329,120.00 USD | `600.00` | `1769.78` | `2216.40` | `2004.83` | 267,248.47 USD | `+20.11%` | `20X Cross` |
| `1595` | `0x7c90...d129` | `LONG` | 1,317,337.63 USD | `594.17` | `2286.01` | `2216.40` | `1868.90` | -40,945.25 USD | `-3.11%` | `20X Cross` |
| `1655` | `0xfc66...ca06` | `SHORT` | 1,257,544.79 USD | `567.43` | `2275.19` | `2216.40` | `7329.10` | 33,478.42 USD | `+2.66%` | `20X Cross` |
| `1661` | `0xfb99...37f3` | `LONG` | 1,252,343.60 USD | `565.34` | `2362.35` | `2216.40` | `1258.42` | -83,192.75 USD | `-6.64%` | `3X Cross` |
| `1673` | `0x844b...7f42` | `SHORT` | 1,243,512.60 USD | `561.00` | `2026.17` | `2216.40` | `3121.73` | -106,829.19 USD | `-8.59%` | `25X Cross` |
| `1686` | `0xabe6...1d99` | `SHORT` | 1,232,660.87 USD | `556.00` | `2484.68` | `2216.40` | `3137.50` | 148,835.02 USD | `+12.07%` | `20X Cross` |
| `1689` | `0x2a76...9a53` | `LONG` | 1,230,412.83 USD | `554.99` | `2231.40` | `2216.40` | `0.000000` | -7,994.23 USD | `-0.65%` | `25X Cross` |
| `1701` | `0x936c...bb0f` | `LONG` | 1,219,546.43 USD | `550.09` | `2218.31` | `2216.40` | `0.000000` | -720.85 USD | `-0.06%` | `20X Cross` |
| `1702` | `0x825c...465e` | `LONG` | 1,219,350.00 USD | `550.00` | `2208.12` | `2216.40` | `1189.62` | 4,880.50 USD | `+0.40%` | `4X Cross` |
| `1708` | `0xad21...fb6a` | `LONG` | 1,213,594.68 USD | `547.26` | `2565.80` | `2216.40` | `1746.13` | -190,558.31 USD | `-15.70%` | `6X Cross` |
| `1802` | `0x0c7a...2f50` | `SHORT` | 1,129,302.38 USD | `509.25` | `2122.56` | `2216.40` | `4126.77` | -48,396.95 USD | `-4.29%` | `20X Cross` |
| `1810` | `0x0089...2410` | `SHORT` | 1,124,835.93 USD | `507.35` | `2308.88` | `2216.40` | `3363.35` | 46,564.33 USD | `+4.14%` | `20X Cross` |
| `1817` | `0xfc27...9d9d` | `SHORT` | 1,120,348.01 USD | `505.14` | `2284.97` | `2216.40` | `40778.06` | 33,884.69 USD | `+3.02%` | `25X Cross` |
| `1827` | `0xe282...df29` | `LONG` | 1,108,550.00 USD | `500.00` | `2309.84` | `2216.40` | `2045.47` | -46,374.21 USD | `-4.18%` | `10X Isolated` |
| `1828` | `0xb322...d51f` | `SHORT` | 1,108,550.00 USD | `500.00` | `2268.03` | `2216.40` | `3711.33` | 25,466.32 USD | `+2.30%` | `20X Cross` |
| `1829` | `0x89b2...9ca6` | `LONG` | 1,108,250.00 USD | `500.00` | `2363.45` | `2216.40` | `1622.81` | -73,477.42 USD | `-6.63%` | `25X Cross` |
| `1830` | `0x6936...9417` | `SHORT` | 1,107,900.00 USD | `500.00` | `2315.11` | `2216.40` | `2359.06` | 49,655.21 USD | `+4.48%` | `25X Isolated` |
| `1833` | `0xa559...ff95` | `LONG` | 1,107,600.00 USD | `500.00` | `2260.68` | `2216.40` | `1085.27` | -22,744.36 USD | `-2.05%` | `20X Cross` |
| `1834` | `0x4044...794c` | `LONG` | 1,107,600.00 USD | `500.00` | `2260.80` | `2216.40` | `0.000000` | -22,800.00 USD | `-2.06%` | `25X Cross` |
| `1836` | `0x7298...7d6c` | `SHORT` | 1,103,500.33 USD | `498.15` | `3426.75` | `2216.40` | `5421.77` | 603,535.49 USD | `+54.69%` | `20X Cross` |
| `1850` | `0x9c68...7783` | `SHORT` | 1,093,663.39 USD | `493.31` | `2273.58` | `2216.40` | `3933.22` | 27,915.86 USD | `+2.55%` | `25X Cross` |
| `1861` | `0x404c...5f03` | `SHORT` | 1,085,168.31 USD | `489.79` | `2671.94` | `2216.40` | `5309.15` | 223,511.25 USD | `+20.60%` | `20X Cross` |
| `1865` | `0x321f...1c84` | `SHORT` | 1,081,393.32 USD | `488.02` | `2370.09` | `2216.40` | `3054.47` | 75,251.28 USD | `+6.96%` | `10X Cross` |
| `1913` | `0xe86b...3664` | `LONG` | 1,035,438.09 USD | `467.42` | `2231.40` | `2216.40` | `0.000000` | -7,576.93 USD | `-0.73%` | `25X Cross` |
| `1915` | `0xaa7a...af37` | `LONG` | 1,033,797.97 USD | `466.14` | `2212.37` | `2216.40` | `0.000000` | 2,528.22 USD | `+0.24%` | `20X Cross` |
| `1929` | `0x94b6...e5b3` | `SHORT` | 1,027,723.78 USD | `463.86` | `2261.12` | `2216.40` | `2397.82` | 21,118.88 USD | `+2.05%` | `25X Cross` |
| `1933` | `0x82c6...fe42` | `LONG` | 1,024,530.00 USD | `462.50` | `2501.38` | `2216.40` | `2053.81` | -132,360.57 USD | `-12.92%` | `5X Isolated` |
| `1938` | `0xe330...77a1` | `SHORT` | 1,022,805.46 USD | `461.20` | `2206.97` | `2216.40` | `6451.94` | -4,948.09 USD | `-0.48%` | `20X Cross` |
| `1945` | `0x2de3...486d` | `LONG` | 1,020,752.84 USD | `460.40` | `2286.27` | `2216.40` | `1083.12` | -31,848.07 USD | `-3.12%` | `25X Cross` |
| `1948` | `0x617e...0f97` | `SHORT` | 1,015,108.99 USD | `457.85` | `2205.60` | `2216.40` | `3443.59` | -5,265.16 USD | `-0.52%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `2356.20` | 120,566.99 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 120.57K USD at 2356.2000 USD [API] | `2026-10-28 20:54:27` |
| `ANNOUNCEMENT` | `INFO` | `2356.20` | 112,381.08 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 112.38K USD at 2356.2000 USD [API] | `2026-10-28 20:54:27` |
| `ANNOUNCEMENT` | `INFO` | `2360.00` | 40,070.20 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 40.07K USD at 2360.0000 USD [API] | `2026-10-28 20:59:30` |
| `ANNOUNCEMENT` | `INFO` | `2371.40` | 160,915.38 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 160.92K USD at 2371.4000 USD [API] | `2026-10-15 02:23:20` |
| `ANNOUNCEMENT` | `INFO` | `2364.10` | 40,041.94 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 40.04K USD at 2364.1000 USD [API] | `2026-10-28 21:57:48` |
| `ANNOUNCEMENT` | `INFO` | `2360.30` | 71,355.65 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 71.36K USD at 2360.3000 USD [API] | `2026-10-28 22:14:06` |
| `ANNOUNCEMENT` | `INFO` | `2362.50` | 55,306.83 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 55.31K USD at 2362.5000 USD [API] | `2026-10-28 22:35:32` |
| `ANNOUNCEMENT` | `INFO` | `2359.60` | 88,044.70 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 88.04K USD at 2359.6000 USD [API] | `2026-10-28 22:53:16` |
| `ANNOUNCEMENT` | `INFO` | `2356.80` | 41,836.97 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 41.84K USD at 2356.8000 USD [API] | `2026-10-29 00:36:32` |
| `ANNOUNCEMENT` | `INFO` | `2343.30` | 46,866.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 46.87K USD at 2343.3000 USD [API] | `2026-10-29 01:10:12` |
| `ANNOUNCEMENT` | `INFO` | `2347.00` | 207,777.56 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 207.78K USD at 2347.0000 USD [API] | `2026-10-29 01:18:29` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2228.36` (Vol: 45,800,000.00 USD, Dist: `+0.73%`) | Long MP=`2174.37` (Vol: 35,800,000.00 USD, Dist: `--1.71%`)
  * 48H Horizon: Short MP=`2229.27` (Vol: 51,700,000.00 USD, Dist: `+0.78%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--1.72%`)
  * 3D Horizon: Short MP=`2229.27` (Vol: 51,700,000.00 USD, Dist: `+0.78%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--1.72%`)
  * 7D Horizon: Short MP=`2401.80` (Vol: 50,700,000.00 USD, Dist: `+8.58%`) | Long MP=`2175.27` (Vol: 44,800,000.00 USD, Dist: `--1.66%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `445.00` | 2,230.00 USD | 767,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `455.00` | 79,460.00 USD | 767,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `465.00` | 10,820.00 USD | 767,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 127,650.00 USD | 767,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 10,560.00 USD | 767,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 121,300.00 USD | 767,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 92,440.00 USD | 767,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 349,700.00 USD | 767,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 8,340.00 USD | 766,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 8,900.00 USD | 766,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 31,920.00 USD | 766,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 143,340.00 USD | 766,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 3,540,000.00 USD | 766,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 2,210,000.00 USD | 763,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 89,630.00 USD | 761,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 25,050.00 USD | 760,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 458,800.00 USD | 760,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 9,380.00 USD | 760,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 21,200.00 USD | 760,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 11,030.00 USD | 760,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 38,100.00 USD | 760,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 222,030.00 USD | 760,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 31,960.00 USD | 760,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 1,230,000.00 USD | 760,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 52,880.00 USD | 758,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 89,360.00 USD | 758,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 11,980.00 USD | 758,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 404,710.00 USD | 758,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 2,250,000.00 USD | 758,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 45,660.00 USD | 756,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 198,360.00 USD | 756,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 28,720.00 USD | 755,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 82,610.00 USD | 755,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 21,670.00 USD | 755,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 874.58 USD | 755,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 62,040.00 USD | 755,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 136,990.00 USD | 755,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 97,560.00 USD | 755,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 241,420.00 USD | 755,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 1,970,000.00 USD | 755,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 177,030.00 USD | 753,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 333,420.00 USD | 753,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 104,470.00 USD | 752,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 1,410,000.00 USD | 752,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 101,170.00 USD | 751,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 89,430.00 USD | 751,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 247,230.00 USD | 750,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 53,670.00 USD | 750,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 218,180.00 USD | 750,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 59,380.00 USD | 750,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 105,390.00 USD | 750,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 309,900.00 USD | 750,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 170,350.00 USD | 749,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 354,530.00 USD | 749,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 158,580.00 USD | 749,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 87,940.00 USD | 749,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 47,530.00 USD | 749,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 5,800,000.00 USD | 749,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 147,410.00 USD | 743,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 741,400.00 USD | 743,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 163,840.00 USD | 742,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 649,380.00 USD | 742,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 10,480,000.00 USD | 741,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 2,430,000.00 USD | 731,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 78,960.00 USD | 728,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 524,070.00 USD | 728,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 307,080.00 USD | 728,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 127,790.00 USD | 727,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 123,790.00 USD | 727,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 8,040,000.00 USD | 727,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 449,180.00 USD | 719,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 86,950.00 USD | 719,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 41,190.00 USD | 719,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 3,760,000.00 USD | 718,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 214,060.00 USD | 715,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 372,330.00 USD | 715,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 175,330.00 USD | 714,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 1,740,000.00 USD | 714,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 268,910.00 USD | 712,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 73,390.00 USD | 712,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 1,080,000.00 USD | 712,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 2,680,000.00 USD | 711,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 15,380,000.00 USD | 708,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 338,190.00 USD | 693,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 261,100.00 USD | 692,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 2,260,000.00 USD | 692,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 109,150.00 USD | 690,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 606,570.00 USD | 690,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 815,430.00 USD | 689,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 136,450.00 USD | 688,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 5,290,000.00 USD | 688,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 1,110,000.00 USD | 683,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 626,320.00 USD | 682,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 1,910,000.00 USD | 681,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 7,300,000.00 USD | 679,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 10,050,000.00 USD | 672,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 192,300.00 USD | 662,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 13,530,000.00 USD | 662,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 1,390,000.00 USD | 648,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 212,560.00 USD | 647,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 419,050.00 USD | 647,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 4,800,000.00 USD | 646,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 20,450,000.00 USD | 641,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 201,640.00 USD | 621,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 7,170,000.00 USD | 621,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 250,500.00 USD | 614,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 480,920.00 USD | 613,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 28,140,000.00 USD | 613,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 933,950.00 USD | 585,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 4,900,000.00 USD | 584,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 395,910.00 USD | 579,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 2,870,000.00 USD | 578,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 16,260,000.00 USD | 576,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 986,150.00 USD | 559,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 2,350,000.00 USD | 558,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 19,480,000.00 USD | 556,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 157,220.00 USD | 537,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 413,480.00 USD | 536,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 21,080,000.00 USD | 536,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 37,270,000.00 USD | 515,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 833,640.00 USD | 478,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 1,020,000.00 USD | 477,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 11,970,000.00 USD | 476,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 1,470,000.00 USD | 464,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 17,980,000.00 USD | 462,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 400,700.00 USD | 444,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 555,170.00 USD | 444,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 36,250,000.00 USD | 443,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 224,960.00 USD | 407,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 2,470,000.00 USD | 407,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 389,290.00 USD | 404,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 586,090.00 USD | 404,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 829,730.00 USD | 403,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 55,860,000.00 USD | 403,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 29,700,000.00 USD | 347,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 1,790,000.00 USD | 317,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 3,990,000.00 USD | 315,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 778,510.00 USD | 311,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 626,710.00 USD | 311,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 24,940,000.00 USD | 310,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 1,950,000.00 USD | 285,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 794,430.00 USD | 283,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 8,480,000.00 USD | 282,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 17,490,000.00 USD | 274,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 1,050,000.00 USD | 256,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 722,550.00 USD | 255,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 18,350,000.00 USD | 254,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 587,230.00 USD | 236,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 16,280,000.00 USD | 236,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 5,100,000.00 USD | 219,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 4,220,000.00 USD | 214,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 1,580,000.00 USD | 210,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,280,000.00 USD | 208,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1985.00` | 8,470,000.00 USD | 207,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1995.00` | 1,360,000.00 USD | 199,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2005.00` | 2,270,000.00 USD | 197,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2015.00` | 3,210,000.00 USD | 195,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2025.00` | 5,640,000.00 USD | 192,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2025.30` | 942,910,000.00 USD | 942,910,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2027.00` | 534,200,000.00 USD | 534,200,000.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.60` | 942,730,000.00 USD | 942,730,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2029.60` | 533,220,000.00 USD | 533,220,000.00 USD | 87,180.00 USD | 163,200.00 USD | 43,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.90` | 941,520,000.00 USD | 941,520,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.20` | 532,920,000.00 USD | 532,920,000.00 USD | 1,360,000.00 USD | 542,800.00 USD | 408,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2034.80` | 530,610,000.00 USD | 530,610,000.00 USD | 1,030,000.00 USD | 787,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 4,000,000.00 USD | 186,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2035.20` | 940,070,000.00 USD | 940,070,000.00 USD | 146,420.00 USD | 186,130.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2037.40` | 528,790,000.00 USD | 528,790,000.00 USD | 202,200.00 USD | 317,820.00 USD | 378,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.50` | 938,380,000.00 USD | 938,380,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2040.00` | 527,890,000.00 USD | 527,890,000.00 USD | 345,650.00 USD | 178,560.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2042.60` | 527,330,000.00 USD | 527,330,000.00 USD | 626,840.00 USD | 0.00 USD | 20,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 2,420,000.00 USD | 182,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2045.10` | 936,930,000.00 USD | 936,930,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2045.20` | 526,690,000.00 USD | 526,690,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2047.80` | 526,660,000.00 USD | 526,660,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.40` | 525,830,000.00 USD | 525,830,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2051.70` | 936,630,000.00 USD | 936,630,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2053.00` | 524,720,000.00 USD | 524,720,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 19,180,000.00 USD | 180,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2055.60` | 524,700,000.00 USD | 524,700,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2058.20` | 524,370,000.00 USD | 524,370,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2058.30` | 934,120,000.00 USD | 934,120,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2060.80` | 523,610,000.00 USD | 523,610,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.60` | 933,780,000.00 USD | 933,780,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2063.40` | 523,530,000.00 USD | 523,530,000.00 USD | 643,750.00 USD | 555,980.00 USD | 600,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.90` | 928,520,000.00 USD | 928,520,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 1,620,000.00 USD | 160,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2066.00` | 521,730,000.00 USD | 521,730,000.00 USD | 808,950.00 USD | 100,330.00 USD | 53,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2068.20` | 925,990,000.00 USD | 925,990,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2068.60` | 520,770,000.00 USD | 520,770,000.00 USD | 57,300.00 USD | 1,270,000.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2071.20` | 519,410,000.00 USD | 519,410,000.00 USD | 1,040,000.00 USD | 534,600.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.50` | 921,500,000.00 USD | 921,500,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.80` | 517,400,000.00 USD | 517,400,000.00 USD | 419,970.00 USD | 62,630.00 USD | 926,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.80` | 915,040,000.00 USD | 915,040,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 4,050,000.00 USD | 159,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2076.40` | 515,990,000.00 USD | 515,990,000.00 USD | 2,580,000.00 USD | 1,020,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.10` | 903,340,000.00 USD | 903,340,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2079.00` | 510,390,000.00 USD | 510,390,000.00 USD | 1,320,000.00 USD | 1,010,000.00 USD | 436,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.40` | 891,050,000.00 USD | 891,050,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2081.60` | 507,620,000.00 USD | 507,620,000.00 USD | 1,430,000.00 USD | 1,260,000.00 USD | 227,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2084.20` | 504,700,000.00 USD | 504,700,000.00 USD | 2,090,000.00 USD | 1,290,000.00 USD | 753,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.70` | 880,410,000.00 USD | 880,410,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 12,710,000.00 USD | 155,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2086.80` | 500,570,000.00 USD | 500,570,000.00 USD | 1,600,000.00 USD | 1,650,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.00` | 871,620,000.00 USD | 871,620,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2089.40` | 495,720,000.00 USD | 495,720,000.00 USD | 1,080,000.00 USD | 220,540.00 USD | 92,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.30` | 863,190,000.00 USD | 863,190,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.00` | 494,330,000.00 USD | 494,330,000.00 USD | 1,130,000.00 USD | 514,440.00 USD | 955,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2094.60` | 491,720,000.00 USD | 491,720,000.00 USD | 2,040,000.00 USD | 1,120,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.60` | 850,240,000.00 USD | 850,240,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 2,470,000.00 USD | 142,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2097.20` | 487,130,000.00 USD | 487,130,000.00 USD | 617,040.00 USD | 1,010,000.00 USD | 984,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.90` | 840,020,000.00 USD | 840,020,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2099.80` | 484,520,000.00 USD | 484,520,000.00 USD | 172,210.00 USD | 403,100.00 USD | 11,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.20` | 833,180,000.00 USD | 833,180,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.40` | 483,930,000.00 USD | 483,930,000.00 USD | 507,510.00 USD | 289,160.00 USD | 466,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2104.50` | 826,580,000.00 USD | 826,580,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2105.00` | 482,670,000.00 USD | 482,670,000.00 USD | 612,280.00 USD | 671,930.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,760,000.00 USD | 140,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2107.60` | 481,350,000.00 USD | 481,350,000.00 USD | 603,300.00 USD | 0.00 USD | 488,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.80` | 821,140,000.00 USD | 821,140,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.20` | 480,260,000.00 USD | 480,260,000.00 USD | 61,010.00 USD | 31,550.00 USD | 196,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2111.10` | 816,650,000.00 USD | 816,650,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2112.80` | 479,970,000.00 USD | 479,970,000.00 USD | 911,810.00 USD | 643,210.00 USD | 224,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2114.40` | 808,610,000.00 USD | 808,610,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,260,000.00 USD | 138,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2115.40` | 478,190,000.00 USD | 478,190,000.00 USD | 0.00 USD | 13,230.00 USD | 426,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.70` | 801,880,000.00 USD | 801,880,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2118.00` | 477,750,000.00 USD | 477,750,000.00 USD | 202,840.00 USD | 14,580.00 USD | 472,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.60` | 477,060,000.00 USD | 477,060,000.00 USD | 744,340.00 USD | 215,530.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2121.00` | 793,040,000.00 USD | 793,040,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.20` | 475,050,000.00 USD | 475,050,000.00 USD | 757,170.00 USD | 1,210,000.00 USD | 917,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.30` | 786,240,000.00 USD | 786,240,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 122,980,000.00 USD | 137,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.80` | 472,170,000.00 USD | 472,170,000.00 USD | 68,480.00 USD | 554,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.60` | 782,920,000.00 USD | 782,920,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.40` | 471,540,000.00 USD | 471,540,000.00 USD | 107,010.00 USD | 475,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.90` | 774,620,000.00 USD | 774,620,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2131.00` | 470,960,000.00 USD | 470,960,000.00 USD | 0.00 USD | 18,610.00 USD | 331,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.20` | 768,200,000.00 USD | 768,200,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 2,160,000.00 USD | 14,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2136.20` | 470,610,000.00 USD | 470,610,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.50` | 765,170,000.00 USD | 765,170,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.80` | 763,210,000.00 USD | 763,210,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.10` | 759,270,000.00 USD | 759,270,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 4,980,000.00 USD | 11,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2147.40` | 757,430,000.00 USD | 757,430,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.70` | 756,350,000.00 USD | 756,350,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2151.80` | 470,330,000.00 USD | 470,330,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.00` | 755,390,000.00 USD | 755,390,000.00 USD | 128,430.00 USD | 311,060.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2154.40` | 469,680,000.00 USD | 469,680,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 4,010,000.00 USD | 6,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2157.30` | 754,920,000.00 USD | 754,920,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2159.60` | 468,290,000.00 USD | 468,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 37,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.60` | 752,430,000.00 USD | 752,430,000.00 USD | 613,630.00 USD | 1,900,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2162.20` | 465,960,000.00 USD | 465,960,000.00 USD | 0.00 USD | 932,730.00 USD | 100,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.90` | 747,910,000.00 USD | 747,910,000.00 USD | 566,120.00 USD | 2,950,000.00 USD | 540,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2164.80` | 464,930,000.00 USD | 464,930,000.00 USD | 217,960.00 USD | 408,000.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 1,880,000.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2167.20` | 743,850,000.00 USD | 743,850,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.40` | 464,190,000.00 USD | 464,190,000.00 USD | 3,220,000.00 USD | 0.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.00` | 459,950,000.00 USD | 459,950,000.00 USD | 5,210,000.00 USD | 5,170,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.50` | 740,150,000.00 USD | 740,150,000.00 USD | 3,500,000.00 USD | 3,730,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2172.60` | 446,820,000.00 USD | 446,820,000.00 USD | 63,650.00 USD | 1,290,000.00 USD | 581,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.80` | 727,710,000.00 USD | 727,710,000.00 USD | 4,370,000.00 USD | 363,040.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 1,080,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.20` | 444,890,000.00 USD | 444,890,000.00 USD | 1,970,000.00 USD | 111,190.00 USD | 894,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2177.10` | 721,850,000.00 USD | 721,850,000.00 USD | 1,750,000.00 USD | 1,330,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2177.80` | 441,920,000.00 USD | 441,920,000.00 USD | 2,320,000.00 USD | 1,770,000.00 USD | 99,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2180.40` | 437,720,000.00 USD | 437,720,000.00 USD | 2,080,000.00 USD | 267,450.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2180.40` | 715,950,000.00 USD | 715,950,000.00 USD | 0.00 USD | 373,740.00 USD | 431,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2183.00` | 433,960,000.00 USD | 433,960,000.00 USD | 2,960,000.00 USD | 1,140,000.00 USD | 425,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2183.70` | 715,150,000.00 USD | 715,150,000.00 USD | 1,760,000.00 USD | 1,310,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2185.60` | 429,440,000.00 USD | 429,440,000.00 USD | 566,020.00 USD | 1,960,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.00` | 708,140,000.00 USD | 708,140,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2188.20` | 424,220,000.00 USD | 424,220,000.00 USD | 0.00 USD | 42,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.30` | 707,530,000.00 USD | 707,530,000.00 USD | 2,730,000.00 USD | 0.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2190.80` | 424,180,000.00 USD | 424,180,000.00 USD | 0.00 USD | 222,200.00 USD | 764,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2193.40` | 423,190,000.00 USD | 423,190,000.00 USD | 605,210.00 USD | 0.00 USD | 39,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2196.00` | 422,550,000.00 USD | 422,550,000.00 USD | 416,500.00 USD | 881,070.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.90` | 700,600,000.00 USD | 700,600,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2198.60` | 419,370,000.00 USD | 419,370,000.00 USD | 0.00 USD | 2,940,000.00 USD | 50,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.20` | 695,500,000.00 USD | 695,500,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2201.20` | 416,370,000.00 USD | 416,370,000.00 USD | 1,690,000.00 USD | 1,450,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.50` | 684,230,000.00 USD | 684,230,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.80` | 411,730,000.00 USD | 411,730,000.00 USD | 2,130,000.00 USD | 314,310.00 USD | 830,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 12,820.00 USD | 12,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2206.40` | 408,450,000.00 USD | 408,450,000.00 USD | 755,060.00 USD | 10,820,000.00 USD | 945,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2206.80` | 675,120,000.00 USD | 675,120,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2209.00` | 395,930,000.00 USD | 395,930,000.00 USD | 2,720,000.00 USD | 2,140,000.00 USD | 3,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2210.10` | 654,750,000.00 USD | 654,750,000.00 USD | 12,800,000.00 USD | 20,410,000.00 USD | 6,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2211.60` | 388,020,000.00 USD | 388,020,000.00 USD | 6,110,000.00 USD | 2,320,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2213.40` | 615,070,000.00 USD | 615,070,000.00 USD | 10,920,000.00 USD | 14,590,000.00 USD | 19,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2214.20` | 374,490,000.00 USD | 374,490,000.00 USD | 15,370,000.00 USD | 11,020,000.00 USD | 7,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2216.70` | 569,600,000.00 USD | 569,600,000.00 USD | 25,710,000.00 USD | 17,030,000.00 USD | 9,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2216.80` | 341,080,000.00 USD | 341,080,000.00 USD | 10,700,000.00 USD | 9,030,000.00 USD | 6,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2219.40` | 315,030,000.00 USD | 315,030,000.00 USD | 9,410,000.00 USD | 8,320,000.00 USD | 3,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2220.00` | 517,470,000.00 USD | 517,470,000.00 USD | 27,820,000.00 USD | 14,950,000.00 USD | 16,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2222.00` | 294,290,000.00 USD | 294,290,000.00 USD | 9,930,000.00 USD | 12,880,000.00 USD | 2,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2223.30` | 458,700,000.00 USD | 458,700,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2224.60` | 269,390,000.00 USD | 269,390,000.00 USD | 9,460,000.00 USD | 4,680,000.00 USD | 5,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2225.00` | 18,300.00 USD | 18,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2226.60` | 428,420,000.00 USD | 428,420,000.00 USD | 16,350,000.00 USD | 11,030,000.00 USD | 10,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.20` | 249,870,000.00 USD | 249,870,000.00 USD | 5,120,000.00 USD | 13,730,000.00 USD | 5,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2229.80` | 225,310,000.00 USD | 225,310,000.00 USD | 10,100,000.00 USD | 7,120,000.00 USD | 4,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.90` | 390,570,000.00 USD | 390,570,000.00 USD | 12,730,000.00 USD | 11,790,000.00 USD | 28,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2232.40` | 204,000,000.00 USD | 204,000,000.00 USD | 4,620,000.00 USD | 6,200,000.00 USD | 7,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2233.20` | 337,500,000.00 USD | 337,500,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2235.00` | 185,910,000.00 USD | 185,910,000.00 USD | 19,080,000.00 USD | 85,110.00 USD | 11,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2235.00` | 7,840,000.00 USD | 7,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2236.50` | 286,180,000.00 USD | 286,180,000.00 USD | 16,050,000.00 USD | 7,430,000.00 USD | 27,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2237.60` | 155,300,000.00 USD | 155,300,000.00 USD | 23,860,000.00 USD | 7,390,000.00 USD | 12,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.80` | 234,940,000.00 USD | 234,940,000.00 USD | 16,720,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2240.20` | 111,600,000.00 USD | 111,600,000.00 USD | 1,100,000.00 USD | 1,380,000.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2242.80` | 106,890,000.00 USD | 106,890,000.00 USD | 9,030,000.00 USD | 3,760,000.00 USD | 9,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2243.10` | 197,880,000.00 USD | 197,880,000.00 USD | 29,940,000.00 USD | 5,310,000.00 USD | 24,810,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2245.00` | 2,480,000.00 USD | 10,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2245.40` | 84,870,000.00 USD | 84,870,000.00 USD | 11,210,000.00 USD | 6,190,000.00 USD | 501,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2246.40` | 137,820,000.00 USD | 137,820,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2248.00` | 66,970,000.00 USD | 66,970,000.00 USD | 12,490,000.00 USD | 1,070,000.00 USD | 7,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2249.70` | 109,560,000.00 USD | 109,560,000.00 USD | 25,030,000.00 USD | 0.00 USD | 19,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2250.60` | 46,290,000.00 USD | 46,290,000.00 USD | 4,450,000.00 USD | 4,540,000.00 USD | 5,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.00` | 65,090,000.00 USD | 65,090,000.00 USD | 26,890,000.00 USD | 0.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2253.20` | 31,680,000.00 USD | 31,680,000.00 USD | 13,840,000.00 USD | 4,440,000.00 USD | 8,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 4,890,000.00 USD | 15,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2255.80` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2256.30` | 26,160,000.00 USD | 26,160,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2258.40` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 170,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2259.60` | 10,940,000.00 USD | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2261.00` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 156,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 941,830.00 USD | 16,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2266.20` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2268.80` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2274.00` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 288,080.00 USD | 114,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 1,040,000.00 USD | 17,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2276.60` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 267,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2279.20` | 22,720,000.00 USD | 22,720,000.00 USD | 11,600,000.00 USD | 3,950,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2279.40` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 17,000,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2281.80` | 85,490,000.00 USD | 85,490,000.00 USD | 33,480,000.00 USD | 26,790,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.70` | 117,630,000.00 USD | 117,630,000.00 USD | 0.00 USD | 87,090,000.00 USD | 13,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2284.40` | 152,200,000.00 USD | 152,200,000.00 USD | 33,020,000.00 USD | 19,430,000.00 USD | 14,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 962,770.00 USD | 18,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2286.00` | 128,050,000.00 USD | 128,050,000.00 USD | 1,010,000.00 USD | 9,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2287.00` | 164,470,000.00 USD | 164,470,000.00 USD | 3,210,000.00 USD | 5,140,000.00 USD | 3,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2289.30` | 152,130,000.00 USD | 152,130,000.00 USD | 7,010,000.00 USD | 5,310,000.00 USD | 11,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2289.60` | 176,810,000.00 USD | 176,810,000.00 USD | 3,280,000.00 USD | 8,840,000.00 USD | 219,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2292.20` | 197,140,000.00 USD | 197,140,000.00 USD | 17,600,000.00 USD | 2,560,000.00 USD | 176,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2292.60` | 153,150,000.00 USD | 153,150,000.00 USD | 0.00 USD | 0.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2294.80` | 209,490,000.00 USD | 209,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 5,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 3,340,000.00 USD | 21,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2295.90` | 180,460,000.00 USD | 180,460,000.00 USD | 13,610,000.00 USD | 2,380,000.00 USD | 11,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2297.40` | 233,240,000.00 USD | 233,240,000.00 USD | 11,830,000.00 USD | 6,530,000.00 USD | 5,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.20` | 208,880,000.00 USD | 208,880,000.00 USD | 11,730,000.00 USD | 11,130,000.00 USD | 5,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2300.00` | 249,950,000.00 USD | 249,950,000.00 USD | 2,700,000.00 USD | 6,620,000.00 USD | 7,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.50` | 255,990,000.00 USD | 255,990,000.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.60` | 269,830,000.00 USD | 269,830,000.00 USD | 14,790,000.00 USD | 170,210.00 USD | 4,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 209,410.00 USD | 21,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.20` | 299,270,000.00 USD | 299,270,000.00 USD | 10,430,000.00 USD | 14,490,000.00 USD | 4,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.80` | 276,770,000.00 USD | 276,770,000.00 USD | 2,980,000.00 USD | 8,820,000.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2307.80` | 307,480,000.00 USD | 307,480,000.00 USD | 2,550,000.00 USD | 3,220,000.00 USD | 2,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2309.10` | 281,280,000.00 USD | 281,280,000.00 USD | 1,240,000.00 USD | 930,630.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2310.40` | 323,320,000.00 USD | 323,320,000.00 USD | 3,940,000.00 USD | 2,450,000.00 USD | 9,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2312.40` | 308,580,000.00 USD | 308,580,000.00 USD | 10,780,000.00 USD | 2,650,000.00 USD | 13,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2313.00` | 335,020,000.00 USD | 335,020,000.00 USD | 4,650,000.00 USD | 6,730,000.00 USD | 313,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 1,110,000.00 USD | 22,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2315.60` | 366,280,000.00 USD | 366,280,000.00 USD | 9,790,000.00 USD | 14,850,000.00 USD | 6,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2315.70` | 316,670,000.00 USD | 316,670,000.00 USD | 0.00 USD | 7,460,000.00 USD | 627,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2318.20` | 379,270,000.00 USD | 379,270,000.00 USD | 4,440,000.00 USD | 6,320,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.00` | 334,170,000.00 USD | 334,170,000.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 8,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.80` | 396,910,000.00 USD | 396,910,000.00 USD | 5,790,000.00 USD | 9,890,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.30` | 351,330,000.00 USD | 351,330,000.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 108,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2323.40` | 412,610,000.00 USD | 412,610,000.00 USD | 1,710,000.00 USD | 10,410,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,800,000.00 USD | 24,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.60` | 371,980,000.00 USD | 371,980,000.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2326.00` | 424,390,000.00 USD | 424,390,000.00 USD | 479,120.00 USD | 5,640,000.00 USD | 5,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2328.60` | 427,380,000.00 USD | 427,380,000.00 USD | 2,140,000.00 USD | 444,400.00 USD | 402,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.90` | 383,810,000.00 USD | 383,810,000.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2331.20` | 445,540,000.00 USD | 445,540,000.00 USD | 17,350,000.00 USD | 692,470.00 USD | 126,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2332.20` | 413,040,000.00 USD | 413,040,000.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2333.80` | 463,270,000.00 USD | 463,270,000.00 USD | 7,710,000.00 USD | 2,820,000.00 USD | 7,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 1,050,000.00 USD | 25,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2335.50` | 471,050,000.00 USD | 471,050,000.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 10,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2336.40` | 481,890,000.00 USD | 481,890,000.00 USD | 15,940,000.00 USD | 547,950.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.80` | 488,920,000.00 USD | 488,920,000.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2339.00` | 494,900,000.00 USD | 494,900,000.00 USD | 6,360,000.00 USD | 2,600,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2341.60` | 513,570,000.00 USD | 513,570,000.00 USD | 5,340,000.00 USD | 3,430,000.00 USD | 9,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2342.10` | 529,020,000.00 USD | 529,020,000.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2344.20` | 526,900,000.00 USD | 526,900,000.00 USD | 1,370,000.00 USD | 6,240,000.00 USD | 5,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 280,870.00 USD | 25,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2345.40` | 550,400,000.00 USD | 550,400,000.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2346.80` | 540,470,000.00 USD | 540,470,000.00 USD | 3,930,000.00 USD | 3,010,000.00 USD | 6,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.70` | 588,270,000.00 USD | 588,270,000.00 USD | 847,620.00 USD | 9,500,000.00 USD | 27,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2349.40` | 571,320,000.00 USD | 571,320,000.00 USD | 19,450,000.00 USD | 5,980,000.00 USD | 5,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2352.00` | 598,840,000.00 USD | 598,840,000.00 USD | 18,420,000.00 USD | 2,080,000.00 USD | 7,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2352.00` | 624,900,000.00 USD | 624,900,000.00 USD | 2,930,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2354.60` | 622,470,000.00 USD | 622,470,000.00 USD | 973,980.00 USD | 20,450,000.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,240,000.00 USD | 27,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2355.30` | 684,440,000.00 USD | 684,440,000.00 USD | 18,530,000.00 USD | 38,020,000.00 USD | 3,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.20` | 632,150,000.00 USD | 632,150,000.00 USD | 4,390,000.00 USD | 1,740,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.60` | 696,580,000.00 USD | 696,580,000.00 USD | 7,110,000.00 USD | 512,220.00 USD | 4,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2359.80` | 653,040,000.00 USD | 653,040,000.00 USD | 8,920,000.00 USD | 6,950,000.00 USD | 5,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.90` | 703,960,000.00 USD | 703,960,000.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 431,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.40` | 673,590,000.00 USD | 673,590,000.00 USD | 8,900,000.00 USD | 6,710,000.00 USD | 4,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2365.00` | 690,810,000.00 USD | 690,810,000.00 USD | 6,420,000.00 USD | 4,850,000.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 3,920,000.00 USD | 31,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2365.20` | 725,010,000.00 USD | 725,010,000.00 USD | 10,200,000.00 USD | 0.00 USD | 10,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.60` | 699,590,000.00 USD | 699,590,000.00 USD | 4,770,000.00 USD | 1,110,000.00 USD | 2,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.50` | 738,080,000.00 USD | 738,080,000.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 458,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.20` | 735,010,000.00 USD | 735,010,000.00 USD | 14,350,000.00 USD | 12,620,000.00 USD | 8,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.80` | 819,020,000.00 USD | 819,020,000.00 USD | 26,000,000.00 USD | 0.00 USD | 54,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.80` | 761,980,000.00 USD | 761,980,000.00 USD | 14,450,000.00 USD | 5,460,000.00 USD | 7,060,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 931,710.00 USD | 32,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2375.10` | 845,960,000.00 USD | 845,960,000.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2375.40` | 780,580,000.00 USD | 780,580,000.00 USD | 11,510,000.00 USD | 3,420,000.00 USD | 3,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.00` | 803,100,000.00 USD | 803,100,000.00 USD | 5,030,000.00 USD | 6,270,000.00 USD | 11,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.40` | 891,380,000.00 USD | 891,380,000.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.60` | 840,470,000.00 USD | 840,470,000.00 USD | 11,320,000.00 USD | 11,190,000.00 USD | 14,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.70` | 931,170,000.00 USD | 931,170,000.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 24,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.20` | 886,340,000.00 USD | 886,340,000.00 USD | 20,060,000.00 USD | 12,500,000.00 USD | 13,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2385.00` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 914,030.00 USD | 32,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.80` | 910,150,000.00 USD | 910,150,000.00 USD | 8,950,000.00 USD | 10,960,000.00 USD | 3,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.30` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2388.40` | 935,260,000.00 USD | 935,260,000.00 USD | 13,100,000.00 USD | 6,720,000.00 USD | 5,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2391.00` | 950,870,000.00 USD | 950,870,000.00 USD | 3,770,000.00 USD | 6,670,000.00 USD | 5,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2393.60` | 965,250,000.00 USD | 965,250,000.00 USD | 4,380,000.00 USD | 6,000,000.00 USD | 4,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.90` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 1,480,000.00 USD | 34,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2396.20` | 979,190,000.00 USD | 979,190,000.00 USD | 5,350,000.00 USD | 4,020,000.00 USD | 4,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2398.20` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.80` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 8,890,000.00 USD | 6,800,000.00 USD | 7,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2401.40` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 4,600,000.00 USD | 6,190,000.00 USD | 6,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.50` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2404.00` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 9,470,000.00 USD | 8,980,000.00 USD | 7,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.80` | 1,670,000,000.00 USD | 1,670,000,000.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 4,990,000.00 USD | 39,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2406.60` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 11,990,000.00 USD | 7,780,000.00 USD | 5,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2408.10` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2409.20` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 8,220,000.00 USD | 6,130,000.00 USD | 6,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.40` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2411.80` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 8,840,000.00 USD | 7,170,000.00 USD | 3,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2414.40` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 2,970,000.00 USD | 2,340,000.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.70` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 23,820,000.00 USD | 21,740,000.00 USD | 23,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 167,200.00 USD | 39,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2417.00` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 3,600,000.00 USD | 2,550,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.00` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2419.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 6,520,000.00 USD | 3,840,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.30` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 25,700,000.00 USD | 27,770,000.00 USD | 21,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.20` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 2,930,000.00 USD | 3,700,000.00 USD | 5,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.60` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 23,650,000.00 USD | 31,040,000.00 USD | 34,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2424.80` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 1,500,000.00 USD | 2,700,000.00 USD | 844,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 4,440,000.00 USD | 44,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2427.40` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 634,700.00 USD | 89,750.00 USD | 601,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.90` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 25,200,000.00 USD | 15,090,000.00 USD | 18,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.00` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,550,000.00 USD | 1,770,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.20` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 10,380,000.00 USD | 17,060,000.00 USD | 9,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 2,090,000.00 USD | 1,690,000.00 USD | 247,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.50` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 183,920.00 USD | 44,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.20` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,790,000.00 USD | 495,600.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2437.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 777,840.00 USD | 517,090.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.80` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 11,900,000.00 USD | 12,720,000.00 USD | 5,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 1,540,000.00 USD | 2,030,000.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.10` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2443.00` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 1,050,000.00 USD | 644,860.00 USD | 859,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.40` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 8,860,000.00 USD | 15,100,000.00 USD | 13,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 200,680.00 USD | 44,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 126,820.00 USD | 467,480.00 USD | 799,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.70` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 11,380,000.00 USD | 6,510,000.00 USD | 17,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2448.20` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 864,380.00 USD | 325,700.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.80` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 2,340,000.00 USD | 871,330.00 USD | 3,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.00` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 16,710,000.00 USD | 12,450,000.00 USD | 12,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2453.40` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 4,320,000.00 USD | 3,900,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2454.30` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 4,620,000.00 USD | 4,930,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 1,750,000.00 USD | 46,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2456.00` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 793,240.00 USD | 1,840,000.00 USD | 797,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.60` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2458.60` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 1,400,000.00 USD | 1,230,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.90` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2461.20` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 470,530.00 USD | 46,520.00 USD | 366,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2463.80` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 619,960.00 USD | 829,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.20` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 11,320,000.00 USD | 57,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2466.40` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.50` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2469.00` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 1,250,000.00 USD | 391,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.80` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.10` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 567,640.00 USD | 58,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2476.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.40` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2479.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 26,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.70` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2482.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 525,130.00 USD | 136,500.00 USD | 451,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.00` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2484.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 925,970.00 USD | 1,330,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 54,830,000.00 USD | 112,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2487.20` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2487.30` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2489.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 317,820.00 USD | 30,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.60` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 239,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2492.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 547,850.00 USD | 44,470.00 USD | 357,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.90` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 1,610,000.00 USD | 1,760,000.00 USD | 3,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2495.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 626,840.00 USD | 134,080.00 USD | 33,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 118,810.00 USD | 113,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.20` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 2,860,000.00 USD | 4,270,000.00 USD | 6,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2497.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2500.20` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.50` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 1,110,000.00 USD | 1,450,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2502.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.80` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 63,860.00 USD | 1,480,000.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 278,950.00 USD | 113,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2505.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2507.10` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2510.40` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2510.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2513.20` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.70` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 6,420,000.00 USD | 119,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2515.80` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2517.00` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2520.30` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2521.00` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 80,610.00 USD | 121,470.00 USD | 88,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2523.60` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 563,140.00 USD | 494,150.00 USD | 532,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.60` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 5,230,000.00 USD | 124,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2526.20` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 754,970.00 USD | 304,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2526.90` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.20` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.50` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 1,040,000.00 USD | 126,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2536.80` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2540.10` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2543.40` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 20,740.00 USD | 126,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2546.70` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.00` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.30` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 12,750,000.00 USD | 138,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2556.60` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.90` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2563.20` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 62,280.00 USD | 138,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2566.50` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.80` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2573.10` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 552,940.00 USD | 139,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2576.40` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2579.70` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2583.00` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,880,000.00 USD | 166,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.30` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.60` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.90` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 8,050,000.00 USD | 174,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2596.20` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2599.50` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2602.80` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 409,940.00 USD | 174,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.10` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.40` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.70` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 177,780.00 USD | 174,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2616.00` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2619.30` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2622.60` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2625.00` | 32,860,000.00 USD | 207,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2625.90` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2629.20` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 0.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2632.40` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2635.00` | 1,730,000.00 USD | 209,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 26,900.00 USD | 209,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 26,070,000.00 USD | 235,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 542,320.00 USD | 236,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 4,380,000.00 USD | 240,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 69,120.00 USD | 240,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 6,220,000.00 USD | 246,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 6,540,000.00 USD | 253,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 422,880.00 USD | 253,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 103,040.00 USD | 253,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 431,080.00 USD | 254,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 13,780,000.00 USD | 268,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 863,440.00 USD | 268,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 9,960,000.00 USD | 278,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 52,970.00 USD | 278,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 1,780,000.00 USD | 280,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 15,480,000.00 USD | 296,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 4,640,000.00 USD | 300,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 1,160,000.00 USD | 302,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 862,730.00 USD | 302,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 6,200,000.00 USD | 309,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 105,480.00 USD | 309,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 467,450.00 USD | 309,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 612,170.00 USD | 310,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 876,420.00 USD | 311,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 1,820,000.00 USD | 312,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 306,370.00 USD | 313,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 286,950.00 USD | 313,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 2,550,000.00 USD | 316,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 186,190.00 USD | 316,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 22,720.00 USD | 316,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 1,060,000.00 USD | 317,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 30,840,000.00 USD | 348,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 1,770,000.00 USD | 349,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 33,400.00 USD | 350,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 50,110.00 USD | 350,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 2,300,000.00 USD | 352,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 524,790.00 USD | 352,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 333,020.00 USD | 353,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 21,490,000.00 USD | 374,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 12,820,000.00 USD | 387,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 929,270.00 USD | 388,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 1,670,000.00 USD | 390,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 313,220.00 USD | 390,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 22,210.00 USD | 390,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 2,190,000.00 USD | 392,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 379,520.00 USD | 393,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 3,140,000.00 USD | 396,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 30,630,000.00 USD | 426,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 6,640,000.00 USD | 433,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 1,970,000.00 USD | 435,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 1,780,000.00 USD | 437,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 145,010.00 USD | 437,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 45,590.00 USD | 437,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 5,530,000.00 USD | 442,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 965,280.00 USD | 443,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 9,590,000.00 USD | 453,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 655,630.00 USD | 454,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 9,800,000.00 USD | 463,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 4,970,000.00 USD | 468,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 18,220,000.00 USD | 487,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 228,510.00 USD | 487,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 159,350.00 USD | 487,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 129,870.00 USD | 487,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 8,490,000.00 USD | 496,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 75,230.00 USD | 496,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 432,520.00 USD | 496,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 1,200,000.00 USD | 497,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 706,260.00 USD | 498,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 1,320,000.00 USD | 499,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 6,090.00 USD | 499,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 49,010.00 USD | 499,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 61,710.00 USD | 499,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 2,170,000.00 USD | 502,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 643,420.00 USD | 502,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 139,390.00 USD | 502,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 4,140,000.00 USD | 507,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 678,580.00 USD | 507,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 35,340.00 USD | 507,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 17,320,000.00 USD | 525,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 111,870.00 USD | 525,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 14,510.00 USD | 525,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 2,030,000.00 USD | 527,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 74,270.00 USD | 527,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 58,030,000.00 USD | 585,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 687,160.00 USD | 586,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 1,440,000.00 USD | 587,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 1,330,000.00 USD | 588,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 140,130.00 USD | 588,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 1,130,000.00 USD | 590,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 245,680.00 USD | 590,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 185,480.00 USD | 590,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 102,950.00 USD | 590,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 54,960.00 USD | 590,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 138,100.00 USD | 590,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 1,430,000.00 USD | 592,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 123,820.00 USD | 592,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 2,040.00 USD | 592,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 3,740,000.00 USD | 596,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 32,490,000.00 USD | 628,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 23,960,000.00 USD | 652,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 8,650.00 USD | 652,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 254,870.00 USD | 652,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 344,930.00 USD | 653,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 6,540,000.00 USD | 659,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 1,150,000.00 USD | 660,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 1,870,000.00 USD | 662,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 7,580.00 USD | 662,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 1,360.00 USD | 662,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 236,950.00 USD | 663,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 446,670.00 USD | 663,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 841,610.00 USD | 664,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 76,980.00 USD | 664,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 309,940.00 USD | 664,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 2,840,000.00 USD | 667,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 87,290.00 USD | 667,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 767,730.00 USD | 668,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 281,290.00 USD | 668,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 19,710.00 USD | 668,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 68,100.00 USD | 668,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 3,030,000.00 USD | 671,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 115,350.00 USD | 671,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 410,310,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 1,460,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3875.00` | 134,760.00 USD | 1,080,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 1,360,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 27,280.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 488,290.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 2,570,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 150,680.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 36,210,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 5,740,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 80,740.00 USD | 1,130,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 64,300,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 518,380.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 331,080.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 2,560,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 387,470.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 182,620.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 647,920.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 1,210.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 1,960,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 95,870.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 293,860.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 151,710.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 1,930,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 42,270.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 32,020.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 6,310.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 147,920.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 3,530,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 231,690.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 21,440.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 814,900.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 355,260.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 476,820.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 1,530,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 4,890,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 38,920.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4225.00` | 45,790.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 84,630,000.00 USD | 1,300,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 29,460,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 16,990.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 147,970.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 2,790.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 1,550,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 5,560.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 233,230.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 57,820.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 58,150.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 30,830.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 197,900.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 5,550,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 741,510.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 438,640.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 160,750.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 141,280.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 37,090.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 40,260.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `445.00` | 767,750,000.00 USD | 0.00 USD | 2,230.00 USD | `-79.85%` | `5.00` |
| `Live` | `Long` | `455.00` | 767,750,000.00 USD | 0.00 USD | 79,460.00 USD | `-79.40%` | `174.63` |
| `Live` | `Long` | `465.00` | 767,670,000.00 USD | 0.00 USD | 10,820.00 USD | `-78.94%` | `23.27` |
| `Live` | `Long` | `485.00` | 767,660,000.00 USD | 0.00 USD | 127,650.00 USD | `-78.04%` | `263.20` |
| `Live` | `Long` | `495.00` | 767,530,000.00 USD | 0.00 USD | 10,560.00 USD | `-77.58%` | `21.33` |
| `Live` | `Long` | `505.00` | 767,520,000.00 USD | 0.00 USD | 121,300.00 USD | `-77.13%` | `240.19` |
| `Live` | `Long` | `515.00` | 767,400,000.00 USD | 0.00 USD | 92,440.00 USD | `-76.68%` | `179.49` |
| `Live` | `Long` | `525.00` | 767,310,000.00 USD | 0.00 USD | 349,700.00 USD | `-76.23%` | `666.10` |
| `Live` | `Long` | `535.00` | 766,960,000.00 USD | 0.00 USD | 8,340.00 USD | `-75.77%` | `15.58` |
| `Live` | `Long` | `545.00` | 766,950,000.00 USD | 0.00 USD | 8,900.00 USD | `-75.32%` | `16.34` |
| `Live` | `Long` | `555.00` | 766,940,000.00 USD | 0.00 USD | 31,920.00 USD | `-74.87%` | `57.51` |
| `Live` | `Long` | `565.00` | 766,910,000.00 USD | 0.00 USD | 143,340.00 USD | `-74.41%` | `253.70` |
| `Live` | `Long` | `575.00` | 766,770,000.00 USD | 0.00 USD | 3,540,000.00 USD | `-73.96%` | `6,150.90` |
| `Live` | `Long` | `585.00` | 763,230,000.00 USD | 0.00 USD | 2,210,000.00 USD | `-73.51%` | `3,775.71` |
| `Live` | `Long` | `595.00` | 761,020,000.00 USD | 0.00 USD | 89,630.00 USD | `-73.06%` | `150.64` |
| `Live` | `Long` | `605.00` | 760,930,000.00 USD | 0.00 USD | 25,050.00 USD | `-72.60%` | `41.40` |
| `Live` | `Long` | `615.00` | 760,910,000.00 USD | 0.00 USD | 458,800.00 USD | `-72.15%` | `746.02` |
| `Live` | `Long` | `625.00` | 760,450,000.00 USD | 0.00 USD | 9,380.00 USD | `-71.70%` | `15.01` |
| `Live` | `Long` | `635.00` | 760,440,000.00 USD | 0.00 USD | 21,200.00 USD | `-71.24%` | `33.39` |
| `Live` | `Long` | `645.00` | 760,420,000.00 USD | 0.00 USD | 11,030.00 USD | `-70.79%` | `17.11` |
| `Live` | `Long` | `655.00` | 760,400,000.00 USD | 0.00 USD | 38,100.00 USD | `-70.34%` | `58.18` |
| `Live` | `Long` | `665.00` | 760,370,000.00 USD | 0.00 USD | 222,030.00 USD | `-69.89%` | `333.87` |
| `Live` | `Long` | `675.00` | 760,140,000.00 USD | 0.00 USD | 31,960.00 USD | `-69.43%` | `47.35` |
| `Live` | `Long` | `685.00` | 760,110,000.00 USD | 0.00 USD | 1,230,000.00 USD | `-68.98%` | `1,799.98` |
| `Live` | `Long` | `695.00` | 758,880,000.00 USD | 0.00 USD | 52,880.00 USD | `-68.53%` | `76.08` |
| `Live` | `Long` | `705.00` | 758,830,000.00 USD | 0.00 USD | 89,360.00 USD | `-68.07%` | `126.75` |
| `Live` | `Long` | `715.00` | 758,740,000.00 USD | 0.00 USD | 11,980.00 USD | `-67.62%` | `16.75` |
| `Live` | `Long` | `725.00` | 758,730,000.00 USD | 0.00 USD | 404,710.00 USD | `-67.17%` | `558.22` |
| `Live` | `Long` | `735.00` | 758,320,000.00 USD | 0.00 USD | 2,250,000.00 USD | `-66.72%` | `3,064.88` |
| `Live` | `Long` | `745.00` | 756,070,000.00 USD | 0.00 USD | 45,660.00 USD | `-66.26%` | `61.29` |
| `Live` | `Long` | `755.00` | 756,020,000.00 USD | 0.00 USD | 198,360.00 USD | `-65.81%` | `262.73` |
| `Live` | `Long` | `765.00` | 755,820,000.00 USD | 0.00 USD | 28,720.00 USD | `-65.36%` | `37.55` |
| `Live` | `Long` | `775.00` | 755,800,000.00 USD | 0.00 USD | 82,610.00 USD | `-64.91%` | `106.60` |
| `Live` | `Long` | `785.00` | 755,710,000.00 USD | 0.00 USD | 21,670.00 USD | `-64.45%` | `27.60` |
| `Live` | `Long` | `795.00` | 755,690,000.00 USD | 0.00 USD | 874.58 USD | `-64.00%` | `1.10` |
| `Live` | `Long` | `805.00` | 755,690,000.00 USD | 0.00 USD | 62,040.00 USD | `-63.55%` | `77.06` |
| `Live` | `Long` | `815.00` | 755,630,000.00 USD | 0.00 USD | 136,990.00 USD | `-63.09%` | `168.08` |
| `Live` | `Long` | `825.00` | 755,490,000.00 USD | 0.00 USD | 97,560.00 USD | `-62.64%` | `118.26` |
| `Live` | `Long` | `835.00` | 755,390,000.00 USD | 0.00 USD | 241,420.00 USD | `-62.19%` | `289.13` |
| `Live` | `Long` | `845.00` | 755,150,000.00 USD | 0.00 USD | 1,970,000.00 USD | `-61.74%` | `2,325.70` |
| `Live` | `Long` | `855.00` | 753,190,000.00 USD | 0.00 USD | 177,030.00 USD | `-61.28%` | `207.05` |
| `Live` | `Long` | `865.00` | 753,010,000.00 USD | 0.00 USD | 333,420.00 USD | `-60.83%` | `385.46` |
| `Live` | `Long` | `875.00` | 752,680,000.00 USD | 0.00 USD | 104,470.00 USD | `-60.38%` | `119.39` |
| `Live` | `Long` | `885.00` | 752,570,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-59.92%` | `1,587.84` |
| `Live` | `Long` | `895.00` | 751,170,000.00 USD | 0.00 USD | 101,170.00 USD | `-59.47%` | `113.04` |
| `Live` | `Long` | `905.00` | 751,070,000.00 USD | 0.00 USD | 89,430.00 USD | `-59.02%` | `98.81` |
| `Live` | `Long` | `915.00` | 750,980,000.00 USD | 0.00 USD | 247,230.00 USD | `-58.57%` | `270.19` |
| `Live` | `Long` | `925.00` | 750,730,000.00 USD | 0.00 USD | 53,670.00 USD | `-58.11%` | `58.02` |
| `Live` | `Long` | `935.00` | 750,680,000.00 USD | 0.00 USD | 218,180.00 USD | `-57.66%` | `233.35` |
| `Live` | `Long` | `945.00` | 750,460,000.00 USD | 0.00 USD | 59,380.00 USD | `-57.21%` | `62.83` |
| `Live` | `Long` | `955.00` | 750,400,000.00 USD | 0.00 USD | 105,390.00 USD | `-56.75%` | `110.35` |
| `Live` | `Long` | `965.00` | 750,290,000.00 USD | 0.00 USD | 309,900.00 USD | `-56.30%` | `321.14` |
| `Live` | `Long` | `975.00` | 749,980,000.00 USD | 0.00 USD | 170,350.00 USD | `-55.85%` | `174.72` |
| `Live` | `Long` | `985.00` | 749,810,000.00 USD | 0.00 USD | 354,530.00 USD | `-55.40%` | `359.93` |
| `Live` | `Long` | `995.00` | 749,460,000.00 USD | 0.00 USD | 158,580.00 USD | `-54.94%` | `159.38` |
| `Live` | `Long` | `1005.00` | 749,300,000.00 USD | 0.00 USD | 87,940.00 USD | `-54.49%` | `87.50` |
| `Live` | `Long` | `1015.00` | 749,210,000.00 USD | 0.00 USD | 47,530.00 USD | `-54.04%` | `46.82` |
| `Live` | `Long` | `1025.00` | 749,160,000.00 USD | 0.00 USD | 5,800,000.00 USD | `-53.58%` | `5,654.20` |
| `Live` | `Long` | `1035.00` | 743,370,000.00 USD | 0.00 USD | 147,410.00 USD | `-53.13%` | `142.42` |
| `Live` | `Long` | `1045.00` | 743,220,000.00 USD | 0.00 USD | 741,400.00 USD | `-52.68%` | `709.47` |
| `Live` | `Long` | `1055.00` | 742,480,000.00 USD | 0.00 USD | 163,840.00 USD | `-52.23%` | `155.30` |
| `Live` | `Long` | `1065.00` | 742,320,000.00 USD | 0.00 USD | 649,380.00 USD | `-51.77%` | `609.75` |
| `Live` | `Long` | `1075.00` | 741,670,000.00 USD | 0.00 USD | 10,480,000.00 USD | `-51.32%` | `9,750.87` |
| `Live` | `Long` | `1085.00` | 731,180,000.00 USD | 0.00 USD | 2,430,000.00 USD | `-50.87%` | `2,240.67` |
| `Live` | `Long` | `1095.00` | 728,750,000.00 USD | 0.00 USD | 78,960.00 USD | `-50.41%` | `72.11` |
| `Live` | `Long` | `1105.00` | 728,670,000.00 USD | 0.00 USD | 524,070.00 USD | `-49.96%` | `474.27` |
| `Live` | `Long` | `1115.00` | 728,150,000.00 USD | 0.00 USD | 307,080.00 USD | `-49.51%` | `275.40` |
| `Live` | `Long` | `1125.00` | 727,840,000.00 USD | 0.00 USD | 127,790.00 USD | `-49.06%` | `113.59` |
| `Live` | `Long` | `1135.00` | 727,710,000.00 USD | 0.00 USD | 123,790.00 USD | `-48.60%` | `109.06` |
| `Live` | `Long` | `1145.00` | 727,590,000.00 USD | 0.00 USD | 8,040,000.00 USD | `-48.15%` | `7,018.40` |
| `Live` | `Long` | `1155.00` | 719,560,000.00 USD | 0.00 USD | 449,180.00 USD | `-47.70%` | `388.90` |
| `Live` | `Long` | `1165.00` | 719,110,000.00 USD | 0.00 USD | 86,950.00 USD | `-47.24%` | `74.64` |
| `Live` | `Long` | `1175.00` | 719,020,000.00 USD | 0.00 USD | 41,190.00 USD | `-46.79%` | `35.05` |
| `Live` | `Long` | `1185.00` | 718,980,000.00 USD | 0.00 USD | 3,760,000.00 USD | `-46.34%` | `3,172.77` |
| `Live` | `Long` | `1195.00` | 715,220,000.00 USD | 0.00 USD | 214,060.00 USD | `-45.89%` | `179.13` |
| `Live` | `Long` | `1205.00` | 715,000,000.00 USD | 0.00 USD | 372,330.00 USD | `-45.43%` | `308.99` |
| `Live` | `Long` | `1215.00` | 714,630,000.00 USD | 0.00 USD | 175,330.00 USD | `-44.98%` | `144.31` |
| `Live` | `Long` | `1225.00` | 714,460,000.00 USD | 0.00 USD | 1,740,000.00 USD | `-44.53%` | `1,416.96` |
| `Live` | `Long` | `1235.00` | 712,720,000.00 USD | 0.00 USD | 268,910.00 USD | `-44.07%` | `217.74` |
| `Live` | `Long` | `1245.00` | 712,450,000.00 USD | 0.00 USD | 73,390.00 USD | `-43.62%` | `58.95` |
| `Live` | `Long` | `1255.00` | 712,380,000.00 USD | 0.00 USD | 1,080,000.00 USD | `-43.17%` | `859.21` |
| `Live` | `Long` | `1265.00` | 711,300,000.00 USD | 0.00 USD | 2,680,000.00 USD | `-42.72%` | `2,120.68` |
| `Live` | `Long` | `1275.00` | 708,620,000.00 USD | 0.00 USD | 15,380,000.00 USD | `-42.26%` | `12,066.63` |
| `Live` | `Long` | `1285.00` | 693,230,000.00 USD | 0.00 USD | 338,190.00 USD | `-41.81%` | `263.18` |
| `Live` | `Long` | `1295.00` | 692,890,000.00 USD | 0.00 USD | 261,100.00 USD | `-41.36%` | `201.62` |
| `Live` | `Long` | `1305.00` | 692,630,000.00 USD | 0.00 USD | 2,260,000.00 USD | `-40.90%` | `1,732.35` |
| `Live` | `Long` | `1315.00` | 690,370,000.00 USD | 0.00 USD | 109,150.00 USD | `-40.45%` | `83.00` |
| `Live` | `Long` | `1325.00` | 690,260,000.00 USD | 0.00 USD | 606,570.00 USD | `-40.00%` | `457.79` |
| `Live` | `Long` | `1335.00` | 689,660,000.00 USD | 0.00 USD | 815,430.00 USD | `-39.55%` | `610.81` |
| `Live` | `Long` | `1345.00` | 688,840,000.00 USD | 0.00 USD | 136,450.00 USD | `-39.09%` | `101.45` |
| `Live` | `Long` | `1355.00` | 688,700,000.00 USD | 0.00 USD | 5,290,000.00 USD | `-38.64%` | `3,906.40` |
| `Live` | `Long` | `1365.00` | 683,410,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-38.19%` | `816.74` |
| `Live` | `Long` | `1375.00` | 682,300,000.00 USD | 0.00 USD | 626,320.00 USD | `-37.73%` | `455.50` |
| `Live` | `Long` | `1385.00` | 681,670,000.00 USD | 0.00 USD | 1,910,000.00 USD | `-37.28%` | `1,375.47` |
| `Live` | `Long` | `1395.00` | 679,770,000.00 USD | 0.00 USD | 7,300,000.00 USD | `-36.83%` | `5,233.88` |
| `Live` | `Long` | `1405.00` | 672,460,000.00 USD | 0.00 USD | 10,050,000.00 USD | `-36.38%` | `7,149.98` |
| `Live` | `Long` | `1415.00` | 662,420,000.00 USD | 0.00 USD | 192,300.00 USD | `-35.92%` | `135.90` |
| `Live` | `Long` | `1425.00` | 662,230,000.00 USD | 0.00 USD | 13,530,000.00 USD | `-35.47%` | `9,491.69` |
| `Live` | `Long` | `1435.00` | 648,700,000.00 USD | 0.00 USD | 1,390,000.00 USD | `-35.02%` | `966.08` |
| `Live` | `Long` | `1445.00` | 647,310,000.00 USD | 0.00 USD | 212,560.00 USD | `-34.57%` | `147.10` |
| `Live` | `Long` | `1455.00` | 647,100,000.00 USD | 0.00 USD | 419,050.00 USD | `-34.11%` | `288.01` |
| `Live` | `Long` | `1465.00` | 646,680,000.00 USD | 0.00 USD | 4,800,000.00 USD | `-33.66%` | `3,276.47` |
| `Live` | `Long` | `1475.00` | 641,880,000.00 USD | 0.00 USD | 20,450,000.00 USD | `-33.21%` | `13,866.13` |
| `Live` | `Long` | `1485.00` | 621,430,000.00 USD | 0.00 USD | 201,640.00 USD | `-32.75%` | `135.78` |
| `Live` | `Long` | `1495.00` | 621,230,000.00 USD | 0.00 USD | 7,170,000.00 USD | `-32.30%` | `4,799.09` |
| `Live` | `Long` | `1505.00` | 614,050,000.00 USD | 0.00 USD | 250,500.00 USD | `-31.85%` | `166.44` |
| `Live` | `Long` | `1515.00` | 613,800,000.00 USD | 0.00 USD | 480,920.00 USD | `-31.40%` | `317.44` |
| `Live` | `Long` | `1525.00` | 613,320,000.00 USD | 0.00 USD | 28,140,000.00 USD | `-30.94%` | `18,451.66` |
| `Live` | `Long` | `1535.00` | 585,180,000.00 USD | 0.00 USD | 933,950.00 USD | `-30.49%` | `608.44` |
| `Live` | `Long` | `1545.00` | 584,250,000.00 USD | 0.00 USD | 4,900,000.00 USD | `-30.04%` | `3,171.11` |
| `Live` | `Long` | `1555.00` | 579,350,000.00 USD | 0.00 USD | 395,910.00 USD | `-29.58%` | `254.61` |
| `Live` | `Long` | `1565.00` | 578,950,000.00 USD | 0.00 USD | 2,870,000.00 USD | `-29.13%` | `1,836.17` |
| `Live` | `Long` | `1575.00` | 576,080,000.00 USD | 0.00 USD | 16,260,000.00 USD | `-28.68%` | `10,322.49` |
| `Live` | `Long` | `1585.00` | 559,820,000.00 USD | 0.00 USD | 986,150.00 USD | `-28.23%` | `622.17` |
| `Live` | `Long` | `1595.00` | 558,840,000.00 USD | 0.00 USD | 2,350,000.00 USD | `-27.77%` | `1,471.81` |
| `Live` | `Long` | `1605.00` | 556,490,000.00 USD | 0.00 USD | 19,480,000.00 USD | `-27.32%` | `12,136.08` |
| `Live` | `Long` | `1615.00` | 537,010,000.00 USD | 0.00 USD | 157,220.00 USD | `-26.87%` | `97.35` |
| `Live` | `Long` | `1625.00` | 536,850,000.00 USD | 0.00 USD | 413,480.00 USD | `-26.41%` | `254.45` |
| `Live` | `Long` | `1635.00` | 536,440,000.00 USD | 0.00 USD | 21,080,000.00 USD | `-25.96%` | `12,893.02` |
| `Live` | `Long` | `1645.00` | 515,360,000.00 USD | 0.00 USD | 37,270,000.00 USD | `-25.51%` | `22,654.06` |
| `Live` | `Long` | `1655.00` | 478,090,000.00 USD | 0.00 USD | 833,640.00 USD | `-25.06%` | `503.71` |
| `Live` | `Long` | `1665.00` | 477,260,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-24.60%` | `612.49` |
| `Live` | `Long` | `1675.00` | 476,240,000.00 USD | 0.00 USD | 11,970,000.00 USD | `-24.15%` | `7,146.81` |
| `Live` | `Long` | `1685.00` | 464,270,000.00 USD | 0.00 USD | 1,470,000.00 USD | `-23.70%` | `870.03` |
| `Live` | `Long` | `1695.00` | 462,800,000.00 USD | 0.00 USD | 17,980,000.00 USD | `-23.24%` | `10,609.63` |
| `Live` | `Long` | `1705.00` | 444,820,000.00 USD | 0.00 USD | 400,700.00 USD | `-22.79%` | `235.01` |
| `Live` | `Long` | `1715.00` | 444,420,000.00 USD | 0.00 USD | 555,170.00 USD | `-22.34%` | `323.71` |
| `Live` | `Long` | `1725.00` | 443,860,000.00 USD | 0.00 USD | 36,250,000.00 USD | `-21.89%` | `21,016.77` |
| `Live` | `Long` | `1735.00` | 407,610,000.00 USD | 0.00 USD | 224,960.00 USD | `-21.43%` | `129.66` |
| `Live` | `Long` | `1745.00` | 407,390,000.00 USD | 0.00 USD | 2,470,000.00 USD | `-20.98%` | `1,413.56` |
| `Live` | `Long` | `1755.00` | 404,920,000.00 USD | 0.00 USD | 389,290.00 USD | `-20.53%` | `221.82` |
| `Live` | `Long` | `1765.00` | 404,530,000.00 USD | 0.00 USD | 586,090.00 USD | `-20.07%` | `332.06` |
| `Live` | `Long` | `1775.00` | 403,940,000.00 USD | 0.00 USD | 829,730.00 USD | `-19.62%` | `467.45` |
| `Live` | `Long` | `1785.00` | 403,110,000.00 USD | 0.00 USD | 55,860,000.00 USD | `-19.17%` | `31,294.16` |
| `Live` | `Long` | `1795.00` | 347,250,000.00 USD | 0.00 USD | 29,700,000.00 USD | `-18.72%` | `16,546.15` |
| `Live` | `Long` | `1805.00` | 317,550,000.00 USD | 0.00 USD | 1,790,000.00 USD | `-18.26%` | `989.44` |
| `Live` | `Long` | `1815.00` | 315,770,000.00 USD | 0.00 USD | 3,990,000.00 USD | `-17.81%` | `2,198.33` |
| `Live` | `Long` | `1825.00` | 311,780,000.00 USD | 0.00 USD | 778,510.00 USD | `-17.36%` | `426.58` |
| `Live` | `Long` | `1835.00` | 311,000,000.00 USD | 0.00 USD | 626,710.00 USD | `-16.90%` | `341.53` |
| `Live` | `Long` | `1845.00` | 310,370,000.00 USD | 0.00 USD | 24,940,000.00 USD | `-16.45%` | `13,515.25` |
| `Live` | `Long` | `1855.00` | 285,440,000.00 USD | 0.00 USD | 1,950,000.00 USD | `-16.00%` | `1,053.04` |
| `Live` | `Long` | `1865.00` | 283,480,000.00 USD | 0.00 USD | 794,430.00 USD | `-15.55%` | `425.97` |
| `Live` | `Long` | `1875.00` | 282,690,000.00 USD | 0.00 USD | 8,480,000.00 USD | `-15.09%` | `4,522.89` |
| `Live` | `Long` | `1885.00` | 274,210,000.00 USD | 0.00 USD | 17,490,000.00 USD | `-14.64%` | `9,280.25` |
| `Live` | `Long` | `1895.00` | 256,720,000.00 USD | 0.00 USD | 1,050,000.00 USD | `-14.19%` | `556.02` |
| `Live` | `Long` | `1905.00` | 255,660,000.00 USD | 0.00 USD | 722,550.00 USD | `-13.73%` | `379.29` |
| `Live` | `Long` | `1915.00` | 254,940,000.00 USD | 0.00 USD | 18,350,000.00 USD | `-13.28%` | `9,584.56` |
| `Live` | `Long` | `1925.00` | 236,580,000.00 USD | 0.00 USD | 587,230.00 USD | `-12.83%` | `305.05` |
| `Live` | `Long` | `1935.00` | 236,000,000.00 USD | 0.00 USD | 16,280,000.00 USD | `-12.38%` | `8,412.56` |
| `Live` | `Long` | `1945.00` | 219,720,000.00 USD | 0.00 USD | 5,100,000.00 USD | `-11.92%` | `2,623.72` |
| `Live` | `Long` | `1955.00` | 214,620,000.00 USD | 0.00 USD | 4,220,000.00 USD | `-11.47%` | `2,157.38` |
| `Live` | `Long` | `1965.00` | 210,400,000.00 USD | 0.00 USD | 1,580,000.00 USD | `-11.02%` | `806.16` |
| `Live` | `Long` | `1975.00` | 208,810,000.00 USD | 0.00 USD | 1,280,000.00 USD | `-10.56%` | `648.27` |
| `Live` | `Long` | `1985.00` | 207,530,000.00 USD | 0.00 USD | 8,470,000.00 USD | `-10.11%` | `4,265.59` |
| `Live` | `Long` | `1995.00` | 199,070,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-9.66%` | `681.80` |
| `Live` | `Long` | `2005.00` | 197,710,000.00 USD | 0.00 USD | 2,270,000.00 USD | `-9.21%` | `1,131.41` |
| `Live` | `Long` | `2015.00` | 195,440,000.00 USD | 0.00 USD | 3,210,000.00 USD | `-8.75%` | `1,594.16` |
| `Live` | `Long` | `2025.00` | 192,230,000.00 USD | 0.00 USD | 5,640,000.00 USD | `-8.30%` | `2,783.96` |
| `Live` | `Long` | `2035.00` | 186,590,000.00 USD | 0.00 USD | 4,000,000.00 USD | `-7.85%` | `1,967.07` |
| `Live` | `Long` | `2045.00` | 182,580,000.00 USD | 0.00 USD | 2,420,000.00 USD | `-7.39%` | `1,183.40` |
| `Live` | `Long` | `2055.00` | 180,160,000.00 USD | 0.00 USD | 19,180,000.00 USD | `-6.94%` | `9,334.75` |
| `Live` | `Long` | `2065.00` | 160,980,000.00 USD | 0.00 USD | 1,620,000.00 USD | `-6.49%` | `783.25` |
| `Live` | `Long` | `2075.00` | 159,360,000.00 USD | 0.00 USD | 4,050,000.00 USD | `-6.04%` | `1,952.34` |
| `Live` | `Long` | `2085.00` | 155,310,000.00 USD | 0.00 USD | 12,710,000.00 USD | `-5.58%` | `6,096.47` |
| `Live` | `Long` | `2095.00` | 142,600,000.00 USD | 0.00 USD | 2,470,000.00 USD | `-5.13%` | `1,180.14` |
| `Live` | `Long` | `2105.00` | 140,130,000.00 USD | 0.00 USD | 1,760,000.00 USD | `-4.68%` | `837.85` |
| `Live` | `Long` | `2115.00` | 138,370,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-4.22%` | `594.04` |
| `Live` | `Long` | `2125.00` | 137,110,000.00 USD | 0.00 USD | 122,980,000.00 USD | `-3.77%` | `57,870.88` |
| `Live` | `Long` | `2135.00` | 14,130,000.00 USD | 0.00 USD | 2,160,000.00 USD | `-3.32%` | `1,013.52` |
| `Live` | `Long` | `2145.00` | 11,970,000.00 USD | 0.00 USD | 4,980,000.00 USD | `-2.87%` | `2,323.99` |
| `Live` | `Long` | `2155.00` | 6,990,000.00 USD | 0.00 USD | 4,010,000.00 USD | `-2.41%` | `1,860.23` |
| `Live` | `Long` | `2165.00` | 2,980,000.00 USD | 0.00 USD | 1,880,000.00 USD | `-1.96%` | `869.29` |
| `Live` | `Long` | `2175.00` | 1,090,000.00 USD | 0.00 USD | 1,080,000.00 USD | `-1.51%` | `497.41` |
| `Live` | `Long` | `2205.00` | 12,820.00 USD | 0.00 USD | 12,820.00 USD | `-0.15%` | `5.81` |
| `Live` | `Short` | `2225.00` | 18,300.00 USD | 18,300.00 USD | 0.00 USD | `+0.76%` | `8.22` |
| `Live` | `Short` | `2235.00` | 7,860,000.00 USD | 7,840,000.00 USD | 0.00 USD | `+1.21%` | `3,506.37` |
| `Live` | `Short` | `2245.00` | 10,330,000.00 USD | 2,480,000.00 USD | 0.00 USD | `+1.66%` | `1,104.27` |
| `Live` | `Short` | `2255.00` | 15,230,000.00 USD | 4,890,000.00 USD | 0.00 USD | `+2.11%` | `2,170.55` |
| `Live` | `Short` | `2265.00` | 16,170,000.00 USD | 941,830.00 USD | 0.00 USD | `+2.57%` | `415.82` |
| `Live` | `Short` | `2275.00` | 17,210,000.00 USD | 1,040,000.00 USD | 0.00 USD | `+3.02%` | `456.90` |
| `Live` | `Short` | `2285.00` | 18,170,000.00 USD | 962,770.00 USD | 0.00 USD | `+3.47%` | `421.34` |
| `Live` | `Short` | `2295.00` | 21,510,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+3.93%` | `1,453.46` |
| `Live` | `Short` | `2305.00` | 21,720,000.00 USD | 209,410.00 USD | 0.00 USD | `+4.38%` | `90.85` |
| `Live` | `Short` | `2315.00` | 22,830,000.00 USD | 1,110,000.00 USD | 0.00 USD | `+4.83%` | `479.07` |
| `Live` | `Short` | `2325.00` | 24,630,000.00 USD | 1,800,000.00 USD | 0.00 USD | `+5.28%` | `774.21` |
| `Live` | `Short` | `2335.00` | 25,680,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+5.74%` | `449.02` |
| `Live` | `Short` | `2345.00` | 25,960,000.00 USD | 280,870.00 USD | 0.00 USD | `+6.19%` | `119.78` |
| `Live` | `Short` | `2355.00` | 27,200,000.00 USD | 1,240,000.00 USD | 0.00 USD | `+6.64%` | `527.81` |
| `Live` | `Short` | `2365.00` | 31,120,000.00 USD | 3,920,000.00 USD | 0.00 USD | `+7.10%` | `1,659.00` |
| `Live` | `Short` | `2375.00` | 32,050,000.00 USD | 931,710.00 USD | 0.00 USD | `+7.55%` | `392.30` |
| `Live` | `Short` | `2385.00` | 32,970,000.00 USD | 914,030.00 USD | 0.00 USD | `+8.00%` | `383.24` |
| `Live` | `Short` | `2395.00` | 34,450,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+8.45%` | `619.63` |
| `Live` | `Short` | `2405.00` | 39,440,000.00 USD | 4,990,000.00 USD | 0.00 USD | `+8.91%` | `2,075.80` |
| `Live` | `Short` | `2415.00` | 39,610,000.00 USD | 167,200.00 USD | 0.00 USD | `+9.36%` | `69.23` |
| `Live` | `Short` | `2425.00` | 44,050,000.00 USD | 4,440,000.00 USD | 0.00 USD | `+9.81%` | `1,831.63` |
| `Live` | `Short` | `2435.00` | 44,240,000.00 USD | 183,920.00 USD | 0.00 USD | `+10.27%` | `75.53` |
| `Live` | `Short` | `2445.00` | 44,440,000.00 USD | 200,680.00 USD | 0.00 USD | `+10.72%` | `82.08` |
| `Live` | `Short` | `2455.00` | 46,190,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+11.17%` | `712.96` |
| `Live` | `Short` | `2465.00` | 57,510,000.00 USD | 11,320,000.00 USD | 0.00 USD | `+11.62%` | `4,593.80` |
| `Live` | `Short` | `2475.00` | 58,080,000.00 USD | 567,640.00 USD | 0.00 USD | `+12.08%` | `229.35` |
| `Live` | `Short` | `2485.00` | 112,910,000.00 USD | 54,830,000.00 USD | 0.00 USD | `+12.53%` | `22,065.50` |
| `Live` | `Short` | `2495.00` | 113,030,000.00 USD | 118,810.00 USD | 0.00 USD | `+12.98%` | `47.62` |
| `Live` | `Short` | `2505.00` | 113,310,000.00 USD | 278,950.00 USD | 0.00 USD | `+13.44%` | `111.36` |
| `Live` | `Short` | `2515.00` | 119,740,000.00 USD | 6,420,000.00 USD | 0.00 USD | `+13.89%` | `2,554.49` |
| `Live` | `Short` | `2525.00` | 124,970,000.00 USD | 5,230,000.00 USD | 0.00 USD | `+14.34%` | `2,072.53` |
| `Live` | `Short` | `2535.00` | 126,010,000.00 USD | 1,040,000.00 USD | 0.00 USD | `+14.79%` | `412.04` |
| `Live` | `Short` | `2545.00` | 126,030,000.00 USD | 20,740.00 USD | 0.00 USD | `+15.25%` | `8.15` |
| `Live` | `Short` | `2555.00` | 138,780,000.00 USD | 12,750,000.00 USD | 0.00 USD | `+15.70%` | `4,990.69` |
| `Live` | `Short` | `2565.00` | 138,850,000.00 USD | 62,280.00 USD | 0.00 USD | `+16.15%` | `24.28` |
| `Live` | `Short` | `2575.00` | 139,400,000.00 USD | 552,940.00 USD | 0.00 USD | `+16.61%` | `214.74` |
| `Live` | `Short` | `2585.00` | 166,280,000.00 USD | 26,880,000.00 USD | 0.00 USD | `+17.06%` | `10,396.70` |
| `Live` | `Short` | `2595.00` | 174,330,000.00 USD | 8,050,000.00 USD | 0.00 USD | `+17.51%` | `3,101.99` |
| `Live` | `Short` | `2605.00` | 174,740,000.00 USD | 409,940.00 USD | 0.00 USD | `+17.96%` | `157.37` |
| `Live` | `Short` | `2615.00` | 174,910,000.00 USD | 177,780.00 USD | 0.00 USD | `+18.42%` | `67.99` |
| `Live` | `Short` | `2625.00` | 207,770,000.00 USD | 32,860,000.00 USD | 0.00 USD | `+18.87%` | `12,517.79` |
| `Live` | `Short` | `2635.00` | 209,500,000.00 USD | 1,730,000.00 USD | 0.00 USD | `+19.32%` | `655.86` |
| `Live` | `Short` | `2645.00` | 209,530,000.00 USD | 26,900.00 USD | 0.00 USD | `+19.78%` | `10.17` |
| `Live` | `Short` | `2655.00` | 235,600,000.00 USD | 26,070,000.00 USD | 0.00 USD | `+20.23%` | `9,819.51` |
| `Live` | `Short` | `2665.00` | 236,140,000.00 USD | 542,320.00 USD | 0.00 USD | `+20.68%` | `203.50` |
| `Live` | `Short` | `2675.00` | 240,520,000.00 USD | 4,380,000.00 USD | 0.00 USD | `+21.13%` | `1,636.59` |
| `Live` | `Short` | `2685.00` | 240,590,000.00 USD | 69,120.00 USD | 0.00 USD | `+21.59%` | `25.74` |
| `Live` | `Short` | `2695.00` | 246,810,000.00 USD | 6,220,000.00 USD | 0.00 USD | `+22.04%` | `2,308.43` |
| `Live` | `Short` | `2705.00` | 253,350,000.00 USD | 6,540,000.00 USD | 0.00 USD | `+22.49%` | `2,416.72` |
| `Live` | `Short` | `2715.00` | 253,770,000.00 USD | 422,880.00 USD | 0.00 USD | `+22.95%` | `155.76` |
| `Live` | `Short` | `2725.00` | 253,870,000.00 USD | 103,040.00 USD | 0.00 USD | `+23.40%` | `37.81` |
| `Live` | `Short` | `2735.00` | 254,300,000.00 USD | 431,080.00 USD | 0.00 USD | `+23.85%` | `157.62` |
| `Live` | `Short` | `2745.00` | 268,080,000.00 USD | 13,780,000.00 USD | 0.00 USD | `+24.30%` | `5,019.61` |
| `Live` | `Short` | `2755.00` | 268,940,000.00 USD | 863,440.00 USD | 0.00 USD | `+24.76%` | `313.41` |
| `Live` | `Short` | `2765.00` | 278,900,000.00 USD | 9,960,000.00 USD | 0.00 USD | `+25.21%` | `3,601.58` |
| `Live` | `Short` | `2775.00` | 278,960,000.00 USD | 52,970.00 USD | 0.00 USD | `+25.66%` | `19.09` |
| `Live` | `Short` | `2785.00` | 280,740,000.00 USD | 1,780,000.00 USD | 0.00 USD | `+26.12%` | `639.11` |
| `Live` | `Short` | `2795.00` | 296,220,000.00 USD | 15,480,000.00 USD | 0.00 USD | `+26.57%` | `5,539.82` |
| `Live` | `Short` | `2805.00` | 300,860,000.00 USD | 4,640,000.00 USD | 0.00 USD | `+27.02%` | `1,655.93` |
| `Live` | `Short` | `2815.00` | 302,020,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+27.47%` | `410.62` |
| `Live` | `Short` | `2825.00` | 302,880,000.00 USD | 862,730.00 USD | 0.00 USD | `+27.93%` | `305.39` |
| `Live` | `Short` | `2835.00` | 309,090,000.00 USD | 6,200,000.00 USD | 0.00 USD | `+28.38%` | `2,187.80` |
| `Live` | `Short` | `2845.00` | 309,190,000.00 USD | 105,480.00 USD | 0.00 USD | `+28.83%` | `37.08` |
| `Live` | `Short` | `2855.00` | 309,660,000.00 USD | 467,450.00 USD | 0.00 USD | `+29.28%` | `163.73` |
| `Live` | `Short` | `2865.00` | 310,270,000.00 USD | 612,170.00 USD | 0.00 USD | `+29.74%` | `213.67` |
| `Live` | `Short` | `2875.00` | 311,150,000.00 USD | 876,420.00 USD | 0.00 USD | `+30.19%` | `304.84` |
| `Live` | `Short` | `2885.00` | 312,970,000.00 USD | 1,820,000.00 USD | 0.00 USD | `+30.64%` | `630.52` |
| `Live` | `Short` | `2895.00` | 313,270,000.00 USD | 306,370.00 USD | 0.00 USD | `+31.10%` | `105.83` |
| `Live` | `Short` | `2905.00` | 313,560,000.00 USD | 286,950.00 USD | 0.00 USD | `+31.55%` | `98.78` |
| `Live` | `Short` | `2915.00` | 316,110,000.00 USD | 2,550,000.00 USD | 0.00 USD | `+32.00%` | `875.27` |
| `Live` | `Short` | `2925.00` | 316,300,000.00 USD | 186,190.00 USD | 0.00 USD | `+32.45%` | `63.65` |
| `Live` | `Short` | `2935.00` | 316,320,000.00 USD | 22,720.00 USD | 0.00 USD | `+32.91%` | `7.74` |
| `Live` | `Short` | `2945.00` | 317,380,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+33.36%` | `360.11` |
| `Live` | `Short` | `2955.00` | 348,220,000.00 USD | 30,840,000.00 USD | 0.00 USD | `+33.81%` | `10,436.70` |
| `Live` | `Short` | `2965.00` | 349,990,000.00 USD | 1,770,000.00 USD | 0.00 USD | `+34.27%` | `597.48` |
| `Live` | `Short` | `2975.00` | 350,030,000.00 USD | 33,400.00 USD | 0.00 USD | `+34.72%` | `11.23` |
| `Live` | `Short` | `2985.00` | 350,080,000.00 USD | 50,110.00 USD | 0.00 USD | `+35.17%` | `16.79` |
| `Live` | `Short` | `2995.00` | 352,380,000.00 USD | 2,300,000.00 USD | 0.00 USD | `+35.62%` | `769.33` |
| `Live` | `Short` | `3005.00` | 352,910,000.00 USD | 524,790.00 USD | 0.00 USD | `+36.08%` | `174.64` |
| `Live` | `Short` | `3015.00` | 353,240,000.00 USD | 333,020.00 USD | 0.00 USD | `+36.53%` | `110.46` |
| `Live` | `Short` | `3025.00` | 374,730,000.00 USD | 21,490,000.00 USD | 0.00 USD | `+36.98%` | `7,104.33` |
| `Live` | `Short` | `3035.00` | 387,550,000.00 USD | 12,820,000.00 USD | 0.00 USD | `+37.44%` | `4,223.15` |
| `Live` | `Short` | `3045.00` | 388,480,000.00 USD | 929,270.00 USD | 0.00 USD | `+37.89%` | `305.18` |
| `Live` | `Short` | `3055.00` | 390,140,000.00 USD | 1,670,000.00 USD | 0.00 USD | `+38.34%` | `545.57` |
| `Live` | `Short` | `3065.00` | 390,460,000.00 USD | 313,220.00 USD | 0.00 USD | `+38.79%` | `102.19` |
| `Live` | `Short` | `3075.00` | 390,480,000.00 USD | 22,210.00 USD | 0.00 USD | `+39.25%` | `7.22` |
| `Live` | `Short` | `3085.00` | 392,670,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+39.70%` | `710.71` |
| `Live` | `Short` | `3095.00` | 393,050,000.00 USD | 379,520.00 USD | 0.00 USD | `+40.15%` | `122.62` |
| `Live` | `Short` | `3105.00` | 396,190,000.00 USD | 3,140,000.00 USD | 0.00 USD | `+40.61%` | `1,012.04` |
| `Live` | `Short` | `3115.00` | 426,820,000.00 USD | 30,630,000.00 USD | 0.00 USD | `+41.06%` | `9,832.77` |
| `Live` | `Short` | `3125.00` | 433,470,000.00 USD | 6,640,000.00 USD | 0.00 USD | `+41.51%` | `2,126.38` |
| `Live` | `Short` | `3135.00` | 435,430,000.00 USD | 1,970,000.00 USD | 0.00 USD | `+41.96%` | `627.68` |
| `Live` | `Short` | `3145.00` | 437,220,000.00 USD | 1,780,000.00 USD | 0.00 USD | `+42.42%` | `566.95` |
| `Live` | `Short` | `3155.00` | 437,360,000.00 USD | 145,010.00 USD | 0.00 USD | `+42.87%` | `45.96` |
| `Live` | `Short` | `3165.00` | 437,410,000.00 USD | 45,590.00 USD | 0.00 USD | `+43.32%` | `14.40` |
| `Live` | `Short` | `3175.00` | 442,930,000.00 USD | 5,530,000.00 USD | 0.00 USD | `+43.78%` | `1,740.71` |
| `Live` | `Short` | `3185.00` | 443,900,000.00 USD | 965,280.00 USD | 0.00 USD | `+44.23%` | `303.07` |
| `Live` | `Short` | `3195.00` | 453,490,000.00 USD | 9,590,000.00 USD | 0.00 USD | `+44.68%` | `3,001.27` |
| `Live` | `Short` | `3205.00` | 454,140,000.00 USD | 655,630.00 USD | 0.00 USD | `+45.13%` | `204.57` |
| `Live` | `Short` | `3215.00` | 463,940,000.00 USD | 9,800,000.00 USD | 0.00 USD | `+45.59%` | `3,047.72` |
| `Live` | `Short` | `3225.00` | 468,920,000.00 USD | 4,970,000.00 USD | 0.00 USD | `+46.04%` | `1,542.19` |
| `Live` | `Short` | `3235.00` | 487,130,000.00 USD | 18,220,000.00 USD | 0.00 USD | `+46.49%` | `5,631.13` |
| `Live` | `Short` | `3245.00` | 487,360,000.00 USD | 228,510.00 USD | 0.00 USD | `+46.95%` | `70.42` |
| `Live` | `Short` | `3255.00` | 487,520,000.00 USD | 159,350.00 USD | 0.00 USD | `+47.40%` | `48.96` |
| `Live` | `Short` | `3265.00` | 487,650,000.00 USD | 129,870.00 USD | 0.00 USD | `+47.85%` | `39.78` |
| `Live` | `Short` | `3275.00` | 496,140,000.00 USD | 8,490,000.00 USD | 0.00 USD | `+48.30%` | `2,593.30` |
| `Live` | `Short` | `3285.00` | 496,220,000.00 USD | 75,230.00 USD | 0.00 USD | `+48.76%` | `22.90` |
| `Live` | `Short` | `3295.00` | 496,650,000.00 USD | 432,520.00 USD | 0.00 USD | `+49.21%` | `131.27` |
| `Live` | `Short` | `3305.00` | 497,850,000.00 USD | 1,200,000.00 USD | 0.00 USD | `+49.66%` | `363.28` |
| `Live` | `Short` | `3315.00` | 498,560,000.00 USD | 706,260.00 USD | 0.00 USD | `+50.12%` | `213.05` |
| `Live` | `Short` | `3325.00` | 499,880,000.00 USD | 1,320,000.00 USD | 0.00 USD | `+50.57%` | `396.66` |
| `Live` | `Short` | `3335.00` | 499,880,000.00 USD | 6,090.00 USD | 0.00 USD | `+51.02%` | `1.83` |
| `Live` | `Short` | `3345.00` | 499,930,000.00 USD | 49,010.00 USD | 0.00 USD | `+51.47%` | `14.65` |
| `Live` | `Short` | `3355.00` | 499,990,000.00 USD | 61,710.00 USD | 0.00 USD | `+51.93%` | `18.39` |
| `Live` | `Short` | `3365.00` | 502,160,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+52.38%` | `644.05` |
| `Live` | `Short` | `3375.00` | 502,800,000.00 USD | 643,420.00 USD | 0.00 USD | `+52.83%` | `190.64` |
| `Live` | `Short` | `3385.00` | 502,940,000.00 USD | 139,390.00 USD | 0.00 USD | `+53.29%` | `41.18` |
| `Live` | `Short` | `3395.00` | 507,090,000.00 USD | 4,140,000.00 USD | 0.00 USD | `+53.74%` | `1,219.84` |
| `Live` | `Short` | `3405.00` | 507,760,000.00 USD | 678,580.00 USD | 0.00 USD | `+54.19%` | `199.29` |
| `Live` | `Short` | `3415.00` | 507,800,000.00 USD | 35,340.00 USD | 0.00 USD | `+54.64%` | `10.35` |
| `Live` | `Short` | `3425.00` | 525,120,000.00 USD | 17,320,000.00 USD | 0.00 USD | `+55.10%` | `5,058.00` |
| `Live` | `Short` | `3435.00` | 525,230,000.00 USD | 111,870.00 USD | 0.00 USD | `+55.55%` | `32.57` |
| `Live` | `Short` | `3445.00` | 525,250,000.00 USD | 14,510.00 USD | 0.00 USD | `+56.00%` | `4.21` |
| `Live` | `Short` | `3455.00` | 527,280,000.00 USD | 2,030,000.00 USD | 0.00 USD | `+56.46%` | `587.87` |
| `Live` | `Short` | `3465.00` | 527,350,000.00 USD | 74,270.00 USD | 0.00 USD | `+56.91%` | `21.43` |
| `Live` | `Short` | `3475.00` | 585,380,000.00 USD | 58,030,000.00 USD | 0.00 USD | `+57.36%` | `16,699.04` |
| `Live` | `Short` | `3485.00` | 586,070,000.00 USD | 687,160.00 USD | 0.00 USD | `+57.81%` | `197.18` |
| `Live` | `Short` | `3495.00` | 587,510,000.00 USD | 1,440,000.00 USD | 0.00 USD | `+58.27%` | `411.67` |
| `Live` | `Short` | `3505.00` | 588,840,000.00 USD | 1,330,000.00 USD | 0.00 USD | `+58.72%` | `380.72` |
| `Live` | `Short` | `3515.00` | 588,980,000.00 USD | 140,130.00 USD | 0.00 USD | `+59.17%` | `39.87` |
| `Live` | `Short` | `3525.00` | 590,110,000.00 USD | 1,130,000.00 USD | 0.00 USD | `+59.63%` | `320.60` |
| `Live` | `Short` | `3535.00` | 590,360,000.00 USD | 245,680.00 USD | 0.00 USD | `+60.08%` | `69.50` |
| `Live` | `Short` | `3545.00` | 590,550,000.00 USD | 185,480.00 USD | 0.00 USD | `+60.53%` | `52.32` |
| `Live` | `Short` | `3555.00` | 590,650,000.00 USD | 102,950.00 USD | 0.00 USD | `+60.98%` | `28.96` |
| `Live` | `Short` | `3565.00` | 590,700,000.00 USD | 54,960.00 USD | 0.00 USD | `+61.44%` | `15.42` |
| `Live` | `Short` | `3575.00` | 590,840,000.00 USD | 138,100.00 USD | 0.00 USD | `+61.89%` | `38.63` |
| `Live` | `Short` | `3585.00` | 592,280,000.00 USD | 1,430,000.00 USD | 0.00 USD | `+62.34%` | `400.20` |
| `Live` | `Short` | `3595.00` | 592,400,000.00 USD | 123,820.00 USD | 0.00 USD | `+62.79%` | `34.44` |
| `Live` | `Short` | `3605.00` | 592,400,000.00 USD | 2,040.00 USD | 0.00 USD | `+63.25%` | `0.56` |
| `Live` | `Short` | `3615.00` | 596,140,000.00 USD | 3,740,000.00 USD | 0.00 USD | `+63.70%` | `1,034.86` |
| `Live` | `Short` | `3625.00` | 628,630,000.00 USD | 32,490,000.00 USD | 0.00 USD | `+64.15%` | `8,963.08` |
| `Live` | `Short` | `3635.00` | 652,590,000.00 USD | 23,960,000.00 USD | 0.00 USD | `+64.61%` | `6,591.12` |
| `Live` | `Short` | `3645.00` | 652,600,000.00 USD | 8,650.00 USD | 0.00 USD | `+65.06%` | `2.37` |
| `Live` | `Short` | `3655.00` | 652,860,000.00 USD | 254,870.00 USD | 0.00 USD | `+65.51%` | `69.73` |
| `Live` | `Short` | `3665.00` | 653,200,000.00 USD | 344,930.00 USD | 0.00 USD | `+65.96%` | `94.11` |
| `Live` | `Short` | `3675.00` | 659,740,000.00 USD | 6,540,000.00 USD | 0.00 USD | `+66.42%` | `1,779.27` |
| `Live` | `Short` | `3685.00` | 660,890,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+66.87%` | `312.67` |
| `Live` | `Short` | `3695.00` | 662,770,000.00 USD | 1,870,000.00 USD | 0.00 USD | `+67.32%` | `507.26` |
| `Live` | `Short` | `3705.00` | 662,770,000.00 USD | 7,580.00 USD | 0.00 USD | `+67.78%` | `2.05` |
| `Live` | `Short` | `3715.00` | 662,780,000.00 USD | 1,360.00 USD | 0.00 USD | `+68.23%` | `0.37` |
| `Live` | `Short` | `3725.00` | 663,010,000.00 USD | 236,950.00 USD | 0.00 USD | `+68.68%` | `63.61` |
| `Live` | `Short` | `3735.00` | 663,460,000.00 USD | 446,670.00 USD | 0.00 USD | `+69.13%` | `119.59` |
| `Live` | `Short` | `3745.00` | 664,300,000.00 USD | 841,610.00 USD | 0.00 USD | `+69.59%` | `224.73` |
| `Live` | `Short` | `3755.00` | 664,380,000.00 USD | 76,980.00 USD | 0.00 USD | `+70.04%` | `20.50` |
| `Live` | `Short` | `3765.00` | 664,690,000.00 USD | 309,940.00 USD | 0.00 USD | `+70.49%` | `82.32` |
| `Live` | `Short` | `3775.00` | 667,530,000.00 USD | 2,840,000.00 USD | 0.00 USD | `+70.95%` | `753.60` |
| `Live` | `Short` | `3785.00` | 667,620,000.00 USD | 87,290.00 USD | 0.00 USD | `+71.40%` | `23.06` |
| `Live` | `Short` | `3795.00` | 668,390,000.00 USD | 767,730.00 USD | 0.00 USD | `+71.85%` | `202.30` |
| `Live` | `Short` | `3805.00` | 668,670,000.00 USD | 281,290.00 USD | 0.00 USD | `+72.30%` | `73.93` |
| `Live` | `Short` | `3815.00` | 668,690,000.00 USD | 19,710.00 USD | 0.00 USD | `+72.76%` | `5.17` |
| `Live` | `Short` | `3825.00` | 668,760,000.00 USD | 68,100.00 USD | 0.00 USD | `+73.21%` | `17.80` |
| `Live` | `Short` | `3835.00` | 671,790,000.00 USD | 3,030,000.00 USD | 0.00 USD | `+73.66%` | `791.12` |
| `Live` | `Short` | `3845.00` | 671,910,000.00 USD | 115,350.00 USD | 0.00 USD | `+74.12%` | `30.00` |
| `Live` | `Short` | `3855.00` | 1,080,000,000.00 USD | 410,310,000.00 USD | 0.00 USD | `+74.57%` | `106,435.76` |
| `Live` | `Short` | `3865.00` | 1,080,000,000.00 USD | 1,460,000.00 USD | 0.00 USD | `+75.02%` | `378.37` |
| `Live` | `Short` | `3875.00` | 1,080,000,000.00 USD | 134,760.00 USD | 0.00 USD | `+75.47%` | `34.78` |
| `Live` | `Short` | `3885.00` | 1,090,000,000.00 USD | 1,360,000.00 USD | 0.00 USD | `+75.93%` | `350.11` |
| `Live` | `Short` | `3895.00` | 1,090,000,000.00 USD | 27,280.00 USD | 0.00 USD | `+76.38%` | `7.00` |
| `Live` | `Short` | `3905.00` | 1,090,000,000.00 USD | 488,290.00 USD | 0.00 USD | `+76.83%` | `125.04` |
| `Live` | `Short` | `3915.00` | 1,090,000,000.00 USD | 2,570,000.00 USD | 0.00 USD | `+77.29%` | `655.19` |
| `Live` | `Short` | `3925.00` | 1,090,000,000.00 USD | 150,680.00 USD | 0.00 USD | `+77.74%` | `38.39` |
| `Live` | `Short` | `3935.00` | 1,120,000,000.00 USD | 36,210,000.00 USD | 0.00 USD | `+78.19%` | `9,201.56` |
| `Live` | `Short` | `3945.00` | 1,130,000,000.00 USD | 5,740,000.00 USD | 0.00 USD | `+78.64%` | `1,454.06` |
| `Live` | `Short` | `3955.00` | 1,130,000,000.00 USD | 80,740.00 USD | 0.00 USD | `+79.10%` | `20.41` |
| `Live` | `Short` | `3965.00` | 1,190,000,000.00 USD | 64,300,000.00 USD | 0.00 USD | `+79.55%` | `16,216.98` |
| `Live` | `Short` | `3975.00` | 1,200,000,000.00 USD | 518,380.00 USD | 0.00 USD | `+80.00%` | `130.41` |
| `Live` | `Short` | `3985.00` | 1,200,000,000.00 USD | 331,080.00 USD | 0.00 USD | `+80.46%` | `83.08` |
| `Live` | `Short` | `3995.00` | 1,200,000,000.00 USD | 2,560,000.00 USD | 0.00 USD | `+80.91%` | `641.69` |
| `Live` | `Short` | `4005.00` | 1,200,000,000.00 USD | 387,470.00 USD | 0.00 USD | `+81.36%` | `96.75` |
| `Live` | `Short` | `4015.00` | 1,200,000,000.00 USD | 182,620.00 USD | 0.00 USD | `+81.81%` | `45.48` |
| `Live` | `Short` | `4025.00` | 1,200,000,000.00 USD | 647,920.00 USD | 0.00 USD | `+82.27%` | `160.97` |
| `Live` | `Short` | `4035.00` | 1,200,000,000.00 USD | 1,210.00 USD | 0.00 USD | `+82.72%` | `0.30` |
| `Live` | `Short` | `4045.00` | 1,200,000,000.00 USD | 1,960,000.00 USD | 0.00 USD | `+83.17%` | `484.14` |
| `Live` | `Short` | `4055.00` | 1,200,000,000.00 USD | 95,870.00 USD | 0.00 USD | `+83.63%` | `23.64` |
| `Live` | `Short` | `4065.00` | 1,200,000,000.00 USD | 293,860.00 USD | 0.00 USD | `+84.08%` | `72.29` |
| `Live` | `Short` | `4075.00` | 1,200,000,000.00 USD | 151,710.00 USD | 0.00 USD | `+84.53%` | `37.23` |
| `Live` | `Short` | `4085.00` | 1,200,000,000.00 USD | 1,930,000.00 USD | 0.00 USD | `+84.98%` | `472.42` |
| `Live` | `Short` | `4095.00` | 1,200,000,000.00 USD | 42,270.00 USD | 0.00 USD | `+85.44%` | `10.32` |
| `Live` | `Short` | `4105.00` | 1,200,000,000.00 USD | 32,020.00 USD | 0.00 USD | `+85.89%` | `7.80` |
| `Live` | `Short` | `4115.00` | 1,200,000,000.00 USD | 6,310.00 USD | 0.00 USD | `+86.34%` | `1.53` |
| `Live` | `Short` | `4125.00` | 1,200,000,000.00 USD | 147,920.00 USD | 0.00 USD | `+86.80%` | `35.86` |
| `Live` | `Short` | `4135.00` | 1,210,000,000.00 USD | 3,530,000.00 USD | 0.00 USD | `+87.25%` | `852.54` |
| `Live` | `Short` | `4145.00` | 1,210,000,000.00 USD | 231,690.00 USD | 0.00 USD | `+87.70%` | `55.90` |
| `Live` | `Short` | `4155.00` | 1,210,000,000.00 USD | 21,440.00 USD | 0.00 USD | `+88.15%` | `5.16` |
| `Live` | `Short` | `4165.00` | 1,210,000,000.00 USD | 814,900.00 USD | 0.00 USD | `+88.61%` | `195.65` |
| `Live` | `Short` | `4175.00` | 1,210,000,000.00 USD | 355,260.00 USD | 0.00 USD | `+89.06%` | `85.09` |
| `Live` | `Short` | `4185.00` | 1,210,000,000.00 USD | 476,820.00 USD | 0.00 USD | `+89.51%` | `113.94` |
| `Live` | `Short` | `4195.00` | 1,210,000,000.00 USD | 1,530,000.00 USD | 0.00 USD | `+89.97%` | `364.89` |
| `Live` | `Short` | `4205.00` | 1,220,000,000.00 USD | 4,890,000.00 USD | 0.00 USD | `+90.42%` | `1,163.15` |
| `Live` | `Short` | `4215.00` | 1,220,000,000.00 USD | 38,920.00 USD | 0.00 USD | `+90.87%` | `9.23` |
| `Live` | `Short` | `4225.00` | 1,220,000,000.00 USD | 45,790.00 USD | 0.00 USD | `+91.32%` | `10.84` |
| `Live` | `Short` | `4235.00` | 1,300,000,000.00 USD | 84,630,000.00 USD | 0.00 USD | `+91.78%` | `19,983.66` |
| `Live` | `Short` | `4245.00` | 1,330,000,000.00 USD | 29,460,000.00 USD | 0.00 USD | `+92.23%` | `6,939.71` |
| `Live` | `Short` | `4255.00` | 1,330,000,000.00 USD | 16,990.00 USD | 0.00 USD | `+92.68%` | `3.99` |
| `Live` | `Short` | `4265.00` | 1,330,000,000.00 USD | 147,970.00 USD | 0.00 USD | `+93.13%` | `34.69` |
| `Live` | `Short` | `4275.00` | 1,330,000,000.00 USD | 2,790.00 USD | 0.00 USD | `+93.59%` | `0.65` |
| `Live` | `Short` | `4285.00` | 1,330,000,000.00 USD | 1,550,000.00 USD | 0.00 USD | `+94.04%` | `362.63` |
| `Live` | `Short` | `4295.00` | 1,330,000,000.00 USD | 5,560.00 USD | 0.00 USD | `+94.49%` | `1.29` |
| `Live` | `Short` | `4305.00` | 1,330,000,000.00 USD | 233,230.00 USD | 0.00 USD | `+94.95%` | `54.18` |
| `Live` | `Short` | `4315.00` | 1,330,000,000.00 USD | 57,820.00 USD | 0.00 USD | `+95.40%` | `13.40` |
| `Live` | `Short` | `4325.00` | 1,330,000,000.00 USD | 58,150.00 USD | 0.00 USD | `+95.85%` | `13.44` |
| `Live` | `Short` | `4335.00` | 1,330,000,000.00 USD | 30,830.00 USD | 0.00 USD | `+96.30%` | `7.11` |
| `Live` | `Short` | `4345.00` | 1,330,000,000.00 USD | 197,900.00 USD | 0.00 USD | `+96.76%` | `45.55` |
| `Live` | `Short` | `4355.00` | 1,340,000,000.00 USD | 5,550,000.00 USD | 0.00 USD | `+97.21%` | `1,273.65` |
| `Live` | `Short` | `4365.00` | 1,340,000,000.00 USD | 741,510.00 USD | 0.00 USD | `+97.66%` | `169.88` |
| `Live` | `Short` | `4375.00` | 1,340,000,000.00 USD | 438,640.00 USD | 0.00 USD | `+98.12%` | `100.26` |
| `Live` | `Short` | `4385.00` | 1,340,000,000.00 USD | 160,750.00 USD | 0.00 USD | `+98.57%` | `36.66` |
| `Live` | `Short` | `4395.00` | 1,340,000,000.00 USD | 141,280.00 USD | 0.00 USD | `+99.02%` | `32.15` |
| `Live` | `Short` | `4405.00` | 1,340,000,000.00 USD | 37,090.00 USD | 0.00 USD | `+99.47%` | `8.42` |
| `Live` | `Short` | `4415.00` | 1,340,000,000.00 USD | 40,260.00 USD | 0.00 USD | `+99.93%` | `9.12` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `485.00` | 67,940,000.00 USD | 0.00 USD | 278.83 USD | `-78.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `505.00` | 67,940,000.00 USD | 0.00 USD | 15,910.00 USD | `-77.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 67,920,000.00 USD | 0.00 USD | 563.16 USD | `-74.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.00` | 67,920,000.00 USD | 0.00 USD | 583.40 USD | `-70.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.00` | 67,920,000.00 USD | 0.00 USD | 16,690.00 USD | `-70.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.00` | 67,910,000.00 USD | 0.00 USD | 578.54 USD | `-69.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.00` | 67,900,000.00 USD | 0.00 USD | 242.21 USD | `-68.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 67,900,000.00 USD | 0.00 USD | 885.90 USD | `-68.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 67,900,000.00 USD | 0.00 USD | 177.27 USD | `-65.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `795.00` | 67,900,000.00 USD | 0.00 USD | 104.22 USD | `-64.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 67,900,000.00 USD | 0.00 USD | 2,090.00 USD | `-63.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 67,900,000.00 USD | 0.00 USD | 1,670.00 USD | `-62.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 67,900,000.00 USD | 0.00 USD | 139,430.00 USD | `-60.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `875.00` | 67,760,000.00 USD | 0.00 USD | 918.49 USD | `-60.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 67,760,000.00 USD | 0.00 USD | 3,130.00 USD | `-59.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 67,760,000.00 USD | 0.00 USD | 2,780.00 USD | `-59.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 67,750,000.00 USD | 0.00 USD | 516.34 USD | `-55.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 67,750,000.00 USD | 0.00 USD | 100.50 USD | `-54.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 67,750,000.00 USD | 0.00 USD | 223,740.00 USD | `-54.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 67,530,000.00 USD | 0.00 USD | 445.08 USD | `-54.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 67,530,000.00 USD | 0.00 USD | 112.03 USD | `-53.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1045.00` | 67,530,000.00 USD | 0.00 USD | 1,260.00 USD | `-52.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 67,530,000.00 USD | 0.00 USD | 1,060.00 USD | `-51.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 67,530,000.00 USD | 0.00 USD | 995.34 USD | `-51.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 67,530,000.00 USD | 0.00 USD | 1,610.00 USD | `-49.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 67,520,000.00 USD | 0.00 USD | 11,050.00 USD | `-49.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 67,510,000.00 USD | 0.00 USD | 1,320.00 USD | `-49.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 67,510,000.00 USD | 0.00 USD | 1,000.00 USD | `-47.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 67,510,000.00 USD | 0.00 USD | 476.46 USD | `-46.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 67,510,000.00 USD | 0.00 USD | 972.41 USD | `-46.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1195.00` | 67,510,000.00 USD | 0.00 USD | 221.55 USD | `-45.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 67,510,000.00 USD | 0.00 USD | 3,110.00 USD | `-45.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 67,510,000.00 USD | 0.00 USD | 995.93 USD | `-44.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 67,500,000.00 USD | 0.00 USD | 951.93 USD | `-43.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 67,500,000.00 USD | 0.00 USD | 2,290.00 USD | `-43.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 67,500,000.00 USD | 0.00 USD | 9,050.00 USD | `-41.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 67,490,000.00 USD | 0.00 USD | 7,030.00 USD | `-41.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 67,490,000.00 USD | 0.00 USD | 25,040.00 USD | `-40.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 67,460,000.00 USD | 0.00 USD | 1,440.00 USD | `-40.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 67,460,000.00 USD | 0.00 USD | 141,950.00 USD | `-39.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 67,320,000.00 USD | 0.00 USD | 128.86 USD | `-38.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 67,320,000.00 USD | 0.00 USD | 1,270.00 USD | `-38.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 67,320,000.00 USD | 0.00 USD | 4,160.00 USD | `-37.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1385.00` | 67,310,000.00 USD | 0.00 USD | 100,800.00 USD | `-37.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 67,210,000.00 USD | 0.00 USD | 535,600.00 USD | `-36.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 66,670,000.00 USD | 0.00 USD | 18,840.00 USD | `-36.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 66,660,000.00 USD | 0.00 USD | 6,450.00 USD | `-35.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 66,650,000.00 USD | 0.00 USD | 852.10 USD | `-35.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 66,650,000.00 USD | 0.00 USD | 1,610.00 USD | `-34.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 66,650,000.00 USD | 0.00 USD | 5,090.00 USD | `-34.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 66,640,000.00 USD | 0.00 USD | 19,730.00 USD | `-33.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 66,620,000.00 USD | 0.00 USD | 2,600.00 USD | `-33.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 66,620,000.00 USD | 0.00 USD | 18,710.00 USD | `-32.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 66,600,000.00 USD | 0.00 USD | 11,460.00 USD | `-32.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 66,590,000.00 USD | 0.00 USD | 84,170.00 USD | `-31.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 66,510,000.00 USD | 0.00 USD | 11,140.00 USD | `-31.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 66,490,000.00 USD | 0.00 USD | 31,900.00 USD | `-30.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 66,460,000.00 USD | 0.00 USD | 8,830.00 USD | `-30.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 66,450,000.00 USD | 0.00 USD | 960.99 USD | `-30.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 66,450,000.00 USD | 0.00 USD | 58,080.00 USD | `-29.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 66,390,000.00 USD | 0.00 USD | 6,260.00 USD | `-29.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 66,390,000.00 USD | 0.00 USD | 198,620.00 USD | `-28.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 66,190,000.00 USD | 0.00 USD | 9,350.00 USD | `-28.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 66,180,000.00 USD | 0.00 USD | 4,040.00 USD | `-27.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 66,180,000.00 USD | 0.00 USD | 431,660.00 USD | `-27.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 65,740,000.00 USD | 0.00 USD | 28,870.00 USD | `-26.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 65,720,000.00 USD | 0.00 USD | 13,590.00 USD | `-26.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 65,700,000.00 USD | 0.00 USD | 10,560.00 USD | `-25.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 65,690,000.00 USD | 0.00 USD | 326,230.00 USD | `-25.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 65,370,000.00 USD | 0.00 USD | 35,070.00 USD | `-25.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 65,330,000.00 USD | 0.00 USD | 744.09 USD | `-24.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 65,330,000.00 USD | 0.00 USD | 289.27 USD | `-24.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 65,330,000.00 USD | 0.00 USD | 35,440.00 USD | `-23.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 65,290,000.00 USD | 0.00 USD | 42,680.00 USD | `-23.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 65,250,000.00 USD | 0.00 USD | 84,490.00 USD | `-22.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 65,170,000.00 USD | 0.00 USD | 16,350.00 USD | `-22.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 65,150,000.00 USD | 0.00 USD | 47,500.00 USD | `-21.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 65,100,000.00 USD | 0.00 USD | 28,150.00 USD | `-21.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 65,070,000.00 USD | 0.00 USD | 3,180.00 USD | `-20.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 65,070,000.00 USD | 0.00 USD | 466,120.00 USD | `-20.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 64,610,000.00 USD | 0.00 USD | 76,990.00 USD | `-20.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 64,530,000.00 USD | 0.00 USD | 3,090.00 USD | `-19.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 64,530,000.00 USD | 0.00 USD | 8,500.00 USD | `-19.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 64,520,000.00 USD | 0.00 USD | 186,120.00 USD | `-18.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 64,330,000.00 USD | 0.00 USD | 660,000.00 USD | `-18.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 63,670,000.00 USD | 0.00 USD | 264,580.00 USD | `-17.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 63,410,000.00 USD | 0.00 USD | 27,250.00 USD | `-17.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 63,380,000.00 USD | 0.00 USD | 19,130.00 USD | `-16.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 63,360,000.00 USD | 0.00 USD | 31,580.00 USD | `-16.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 63,330,000.00 USD | 0.00 USD | 792,160.00 USD | `-16.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 62,540,000.00 USD | 0.00 USD | 33,750.00 USD | `-15.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 62,500,000.00 USD | 0.00 USD | 18,240,000.00 USD | `-15.09%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 44,260,000.00 USD | 0.00 USD | 22,350.00 USD | `-14.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 44,240,000.00 USD | 0.00 USD | 59,690.00 USD | `-14.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 44,180,000.00 USD | 0.00 USD | 160,070.00 USD | `-13.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 44,020,000.00 USD | 0.00 USD | 101,030.00 USD | `-13.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1925.00` | 43,920,000.00 USD | 0.00 USD | 19,300,000.00 USD | `-12.83%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 24,620,000.00 USD | 0.00 USD | 107,510.00 USD | `-12.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 24,510,000.00 USD | 0.00 USD | 63,470.00 USD | `-11.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 24,450,000.00 USD | 0.00 USD | 73,490.00 USD | `-11.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 24,370,000.00 USD | 0.00 USD | 139,850.00 USD | `-11.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 24,230,000.00 USD | 0.00 USD | 334,410.00 USD | `-10.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 23,900,000.00 USD | 0.00 USD | 100,060.00 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 23,800,000.00 USD | 0.00 USD | 249,090.00 USD | `-9.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 23,550,000.00 USD | 0.00 USD | 1,920,000.00 USD | `-9.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 21,630,000.00 USD | 0.00 USD | 483,180.00 USD | `-8.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 21,150,000.00 USD | 0.00 USD | 95,400.00 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 21,060,000.00 USD | 0.00 USD | 328,550.00 USD | `-7.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 20,730,000.00 USD | 0.00 USD | 702,690.00 USD | `-7.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 20,020,000.00 USD | 0.00 USD | 297,190.00 USD | `-6.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 19,730,000.00 USD | 0.00 USD | 128,420.00 USD | `-6.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 19,600,000.00 USD | 0.00 USD | 36,400.00 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 19,560,000.00 USD | 0.00 USD | 223,180.00 USD | `-5.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 19,340,000.00 USD | 0.00 USD | 28,900.00 USD | `-5.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 19,310,000.00 USD | 0.00 USD | 819,220.00 USD | `-4.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 18,490,000.00 USD | 0.00 USD | 876,600.00 USD | `-4.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 17,610,000.00 USD | 0.00 USD | 296,050.00 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 17,320,000.00 USD | 0.00 USD | 643,510.00 USD | `-3.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 16,670,000.00 USD | 0.00 USD | 377,670.00 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 16,300,000.00 USD | 0.00 USD | 5,280,000.00 USD | `-2.41%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2165.00` | 11,020,000.00 USD | 0.00 USD | 1,680,000.00 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 9,340,000.00 USD | 0.00 USD | 6,980,000.00 USD | `-1.51%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2185.00` | 2,360,000.00 USD | 0.00 USD | 1,530,000.00 USD | `-1.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 830,880.00 USD | 0.00 USD | 641,070.00 USD | `-0.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 189,810.00 USD | 0.00 USD | 189,810.00 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2215.00` | 13,280.00 USD | 13,280.00 USD | 0.00 USD | `+0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2225.00` | 1,820,000.00 USD | 1,810,000.00 USD | 0.00 USD | `+0.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2235.00` | 7,730,000.00 USD | 5,900,000.00 USD | 0.00 USD | `+1.21%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2245.00` | 8,180,000.00 USD | 449,460.00 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2255.00` | 9,370,000.00 USD | 1,190,000.00 USD | 0.00 USD | `+2.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2265.00` | 10,910,000.00 USD | 1,550,000.00 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 11,550,000.00 USD | 630,980.00 USD | 0.00 USD | `+3.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 12,450,000.00 USD | 908,340.00 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 12,740,000.00 USD | 285,280.00 USD | 0.00 USD | `+3.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 13,250,000.00 USD | 513,080.00 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2315.00` | 14,510,000.00 USD | 1,260,000.00 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 15,130,000.00 USD | 623,820.00 USD | 0.00 USD | `+5.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 15,380,000.00 USD | 246,920.00 USD | 0.00 USD | `+5.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 16,350,000.00 USD | 971,960.00 USD | 0.00 USD | `+6.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 17,800,000.00 USD | 1,450,000.00 USD | 0.00 USD | `+6.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 18,060,000.00 USD | 264,160.00 USD | 0.00 USD | `+7.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 18,210,000.00 USD | 143,260.00 USD | 0.00 USD | `+7.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 18,250,000.00 USD | 47,410.00 USD | 0.00 USD | `+8.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 19,410,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+8.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 20,890,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+8.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 21,130,000.00 USD | 238,600.00 USD | 0.00 USD | `+9.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 24,110,000.00 USD | 2,980,000.00 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 24,300,000.00 USD | 189,180.00 USD | 0.00 USD | `+10.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 24,870,000.00 USD | 566,880.00 USD | 0.00 USD | `+10.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2455.00` | 25,010,000.00 USD | 147,980.00 USD | 0.00 USD | `+11.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 27,110,000.00 USD | 2,100,000.00 USD | 0.00 USD | `+11.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 27,300,000.00 USD | 187,980.00 USD | 0.00 USD | `+12.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 29,410,000.00 USD | 2,110,000.00 USD | 0.00 USD | `+12.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 29,820,000.00 USD | 411,740.00 USD | 0.00 USD | `+12.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 34,690,000.00 USD | 4,870,000.00 USD | 0.00 USD | `+13.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2515.00` | 42,370,000.00 USD | 7,680,000.00 USD | 0.00 USD | `+13.89%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 45,420,000.00 USD | 3,050,000.00 USD | 0.00 USD | `+14.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 45,480,000.00 USD | 63,610.00 USD | 0.00 USD | `+14.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 47,750,000.00 USD | 2,270,000.00 USD | 0.00 USD | `+15.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 47,980,000.00 USD | 222,610.00 USD | 0.00 USD | `+15.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 50,320,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+16.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 50,390,000.00 USD | 78,680.00 USD | 0.00 USD | `+16.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 53,090,000.00 USD | 2,700,000.00 USD | 0.00 USD | `+17.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 53,100,000.00 USD | 11,010.00 USD | 0.00 USD | `+17.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 55,900,000.00 USD | 2,790,000.00 USD | 0.00 USD | `+17.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 56,040,000.00 USD | 145,730.00 USD | 0.00 USD | `+18.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 58,230,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+18.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 58,370,000.00 USD | 147,930.00 USD | 0.00 USD | `+19.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 60,500,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+19.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 60,750,000.00 USD | 251,610.00 USD | 0.00 USD | `+20.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 62,890,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+20.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 63,100,000.00 USD | 208,460.00 USD | 0.00 USD | `+21.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 65,280,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+21.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 65,360,000.00 USD | 76,240.00 USD | 0.00 USD | `+22.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 70,340,000.00 USD | 4,980,000.00 USD | 0.00 USD | `+22.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 70,410,000.00 USD | 76,900.00 USD | 0.00 USD | `+22.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 72,880,000.00 USD | 2,470,000.00 USD | 0.00 USD | `+23.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 72,920,000.00 USD | 43,050.00 USD | 0.00 USD | `+23.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 75,300,000.00 USD | 2,370,000.00 USD | 0.00 USD | `+24.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 75,980,000.00 USD | 684,550.00 USD | 0.00 USD | `+24.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 78,320,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+25.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 78,890,000.00 USD | 577,610.00 USD | 0.00 USD | `+25.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 81,160,000.00 USD | 2,260,000.00 USD | 0.00 USD | `+26.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 81,180,000.00 USD | 17,550.00 USD | 0.00 USD | `+26.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 84,310,000.00 USD | 3,130,000.00 USD | 0.00 USD | `+27.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 84,360,000.00 USD | 52,490.00 USD | 0.00 USD | `+27.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 84,400,000.00 USD | 43,930.00 USD | 0.00 USD | `+27.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 84,690,000.00 USD | 286,140.00 USD | 0.00 USD | `+28.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 85,690,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+28.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 86,960,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+29.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 86,980,000.00 USD | 14,570.00 USD | 0.00 USD | `+29.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 86,980,000.00 USD | 2,460.00 USD | 0.00 USD | `+30.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 87,290,000.00 USD | 305,820.00 USD | 0.00 USD | `+30.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 87,300,000.00 USD | 16,190.00 USD | 0.00 USD | `+31.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 88,790,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+31.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 88,800,000.00 USD | 10,340.00 USD | 0.00 USD | `+32.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 88,800,000.00 USD | 3,050.00 USD | 0.00 USD | `+32.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 88,850,000.00 USD | 52,370.00 USD | 0.00 USD | `+32.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 88,890,000.00 USD | 34,650.00 USD | 0.00 USD | `+33.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 88,930,000.00 USD | 43,400.00 USD | 0.00 USD | `+33.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 89,040,000.00 USD | 113,340.00 USD | 0.00 USD | `+34.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 89,190,000.00 USD | 145,510.00 USD | 0.00 USD | `+34.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 89,370,000.00 USD | 177,120.00 USD | 0.00 USD | `+35.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 91,290,000.00 USD | 1,920,000.00 USD | 0.00 USD | `+35.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 94,330,000.00 USD | 3,040,000.00 USD | 0.00 USD | `+36.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 94,340,000.00 USD | 6,950.00 USD | 0.00 USD | `+36.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 94,370,000.00 USD | 35,380.00 USD | 0.00 USD | `+36.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 94,450,000.00 USD | 74,910.00 USD | 0.00 USD | `+37.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 94,470,000.00 USD | 22,460.00 USD | 0.00 USD | `+37.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 95,240,000.00 USD | 771,720.00 USD | 0.00 USD | `+38.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 95,240,000.00 USD | 612.69 USD | 0.00 USD | `+38.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 95,290,000.00 USD | 49,500.00 USD | 0.00 USD | `+39.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 95,310,000.00 USD | 19,570.00 USD | 0.00 USD | `+39.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 95,310,000.00 USD | 928.50 USD | 0.00 USD | `+40.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 107,160,000.00 USD | 11,850,000.00 USD | 0.00 USD | `+40.61%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 107,290,000.00 USD | 128,280.00 USD | 0.00 USD | `+41.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 107,670,000.00 USD | 381,020.00 USD | 0.00 USD | `+41.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 107,670,000.00 USD | 2,660.00 USD | 0.00 USD | `+42.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 107,730,000.00 USD | 58,930.00 USD | 0.00 USD | `+42.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 107,740,000.00 USD | 9,860.00 USD | 0.00 USD | `+43.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 107,740,000.00 USD | 149.22 USD | 0.00 USD | `+43.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 107,740,000.00 USD | 1,330.00 USD | 0.00 USD | `+44.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 107,780,000.00 USD | 36,550.00 USD | 0.00 USD | `+44.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 108,430,000.00 USD | 653,320.00 USD | 0.00 USD | `+45.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 108,430,000.00 USD | 1,760.00 USD | 0.00 USD | `+45.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 108,440,000.00 USD | 3,740.00 USD | 0.00 USD | `+46.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 108,440,000.00 USD | 167.25 USD | 0.00 USD | `+46.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 108,490,000.00 USD | 56,110.00 USD | 0.00 USD | `+46.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 108,730,000.00 USD | 236,580.00 USD | 0.00 USD | `+47.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 108,750,000.00 USD | 15,710.00 USD | 0.00 USD | `+47.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 108,750,000.00 USD | 1,630.00 USD | 0.00 USD | `+48.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 108,890,000.00 USD | 141,980.00 USD | 0.00 USD | `+48.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 108,910,000.00 USD | 15,350.00 USD | 0.00 USD | `+49.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 110,320,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+49.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 110,710,000.00 USD | 389,970.00 USD | 0.00 USD | `+50.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 110,730,000.00 USD | 18,270.00 USD | 0.00 USD | `+50.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 110,730,000.00 USD | 4,350.00 USD | 0.00 USD | `+51.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 110,730,000.00 USD | 2,170.00 USD | 0.00 USD | `+51.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 110,730,000.00 USD | 837.74 USD | 0.00 USD | `+51.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 110,740,000.00 USD | 2,780.00 USD | 0.00 USD | `+52.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 110,760,000.00 USD | 21,260.00 USD | 0.00 USD | `+52.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 110,820,000.00 USD | 58,010.00 USD | 0.00 USD | `+53.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 111,140,000.00 USD | 322,160.00 USD | 0.00 USD | `+53.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 112,630,000.00 USD | 1,490,000.00 USD | 0.00 USD | `+54.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 112,640,000.00 USD | 5,700.00 USD | 0.00 USD | `+54.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 112,650,000.00 USD | 16,310.00 USD | 0.00 USD | `+55.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 112,670,000.00 USD | 15,030.00 USD | 0.00 USD | `+56.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 112,690,000.00 USD | 18,600.00 USD | 0.00 USD | `+56.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 112,690,000.00 USD | 495.50 USD | 0.00 USD | `+56.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 112,690,000.00 USD | 3,190.00 USD | 0.00 USD | `+57.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 112,730,000.00 USD | 43,610.00 USD | 0.00 USD | `+57.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 112,730,000.00 USD | 158.32 USD | 0.00 USD | `+58.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 113,180,000.00 USD | 444,280.00 USD | 0.00 USD | `+58.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 113,220,000.00 USD | 43,620.00 USD | 0.00 USD | `+59.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 113,230,000.00 USD | 3,690.00 USD | 0.00 USD | `+59.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 113,240,000.00 USD | 9,810.00 USD | 0.00 USD | `+60.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 113,330,000.00 USD | 90,810.00 USD | 0.00 USD | `+60.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 113,330,000.00 USD | 2,300.00 USD | 0.00 USD | `+61.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3575.00` | 113,330,000.00 USD | 2,870.00 USD | 0.00 USD | `+61.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 113,330,000.00 USD | 354.92 USD | 0.00 USD | `+62.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 113,340,000.00 USD | 13,160.00 USD | 0.00 USD | `+62.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 113,450,000.00 USD | 101,080.00 USD | 0.00 USD | `+63.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 113,460,000.00 USD | 10,210.00 USD | 0.00 USD | `+64.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 113,460,000.00 USD | 7,790.00 USD | 0.00 USD | `+64.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 113,470,000.00 USD | 3,860.00 USD | 0.00 USD | `+65.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 113,470,000.00 USD | 820.18 USD | 0.00 USD | `+65.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 113,480,000.00 USD | 8,130.00 USD | 0.00 USD | `+65.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 113,530,000.00 USD | 55,120.00 USD | 0.00 USD | `+66.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 113,530,000.00 USD | 1,410.00 USD | 0.00 USD | `+66.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 113,530,000.00 USD | 819.92 USD | 0.00 USD | `+67.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 113,530,000.00 USD | 323.58 USD | 0.00 USD | `+68.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 113,540,000.00 USD | 1,400.00 USD | 0.00 USD | `+68.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 113,540,000.00 USD | 6,490.00 USD | 0.00 USD | `+69.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3745.00` | 113,540,000.00 USD | 165.90 USD | 0.00 USD | `+69.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 113,540,000.00 USD | 751.00 USD | 0.00 USD | `+70.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 113,540,000.00 USD | 286.90 USD | 0.00 USD | `+71.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 113,540,000.00 USD | 1,560.00 USD | 0.00 USD | `+71.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 114,280,000.00 USD | 734,090.00 USD | 0.00 USD | `+72.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 114,300,000.00 USD | 20,930.00 USD | 0.00 USD | `+72.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 114,310,000.00 USD | 8,380.00 USD | 0.00 USD | `+73.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 114,310,000.00 USD | 711.78 USD | 0.00 USD | `+73.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 114,310,000.00 USD | 355.28 USD | 0.00 USD | `+74.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 114,310,000.00 USD | 5,170.00 USD | 0.00 USD | `+74.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 114,330,000.00 USD | 19,430.00 USD | 0.00 USD | `+75.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 114,350,000.00 USD | 12,120.00 USD | 0.00 USD | `+76.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 114,990,000.00 USD | 646,840.00 USD | 0.00 USD | `+77.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 115,040,000.00 USD | 42,570.00 USD | 0.00 USD | `+78.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 115,090,000.00 USD | 59,170.00 USD | 0.00 USD | `+78.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 115,100,000.00 USD | 1,380.00 USD | 0.00 USD | `+79.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 115,100,000.00 USD | 6,960.00 USD | 0.00 USD | `+80.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 115,120,000.00 USD | 14,610.00 USD | 0.00 USD | `+80.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 115,120,000.00 USD | 4,280.00 USD | 0.00 USD | `+80.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 117,870,000.00 USD | 2,750,000.00 USD | 0.00 USD | `+81.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 117,870,000.00 USD | 898.59 USD | 0.00 USD | `+82.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 117,870,000.00 USD | 811.00 USD | 0.00 USD | `+83.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 117,880,000.00 USD | 4,310.00 USD | 0.00 USD | `+84.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 117,880,000.00 USD | 3,050.00 USD | 0.00 USD | `+84.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 117,920,000.00 USD | 36,740.00 USD | 0.00 USD | `+85.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 117,920,000.00 USD | 5,990.00 USD | 0.00 USD | `+86.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 117,920,000.00 USD | 372.90 USD | 0.00 USD | `+86.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 117,920,000.00 USD | 395.43 USD | 0.00 USD | `+87.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 117,930,000.00 USD | 376.65 USD | 0.00 USD | `+89.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 117,970,000.00 USD | 42,260.00 USD | 0.00 USD | `+90.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 117,970,000.00 USD | 460.70 USD | 0.00 USD | `+90.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 117,970,000.00 USD | 1,270.00 USD | 0.00 USD | `+91.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 117,970,000.00 USD | 4,300.00 USD | 0.00 USD | `+92.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 117,970,000.00 USD | 437.16 USD | 0.00 USD | `+93.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 118,040,000.00 USD | 64,550.00 USD | 0.00 USD | `+93.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 118,040,000.00 USD | 1,610.00 USD | 0.00 USD | `+94.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 118,140,000.00 USD | 97,670.00 USD | 0.00 USD | `+94.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 118,140,000.00 USD | 1,070.00 USD | 0.00 USD | `+95.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 118,150,000.00 USD | 11,270.00 USD | 0.00 USD | `+96.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 118,150,000.00 USD | 2,400.00 USD | 0.00 USD | `+97.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 118,200,000.00 USD | 43,750.00 USD | 0.00 USD | `+98.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 118,260,000.00 USD | 64,570.00 USD | 0.00 USD | `+98.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 118,260,000.00 USD | 1,050.00 USD | 0.00 USD | `+99.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 118,310,000.00 USD | 46,920.00 USD | 0.00 USD | `+99.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 118,320,000.00 USD | 11,480.00 USD | 0.00 USD | `+99.93%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `2025.30` | 942,910,000.00 USD | 0.00 USD | 942,910,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2027.00` | 534,200,000.00 USD | 0.00 USD | 534,200,000.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD |
| `7D` | `2028.60` | 942,730,000.00 USD | 0.00 USD | 942,730,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD |
| `1D` | `2029.60` | 533,220,000.00 USD | 0.00 USD | 533,220,000.00 USD | 87,180.00 USD | 163,200.00 USD | 43,160.00 USD |
| `7D` | `2031.90` | 941,520,000.00 USD | 0.00 USD | 941,520,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD |
| `1D` | `2032.20` | 532,920,000.00 USD | 0.00 USD | 532,920,000.00 USD | 1,360,000.00 USD | 542,800.00 USD | 408,620.00 USD |
| `1D` | `2034.80` | 530,610,000.00 USD | 0.00 USD | 530,610,000.00 USD | 1,030,000.00 USD | 787,650.00 USD | 0.00 USD |
| `7D` | `2035.20` | 940,070,000.00 USD | 0.00 USD | 940,070,000.00 USD | 146,420.00 USD | 186,130.00 USD | 1,350,000.00 USD |
| `1D` | `2037.40` | 528,790,000.00 USD | 0.00 USD | 528,790,000.00 USD | 202,200.00 USD | 317,820.00 USD | 378,700.00 USD |
| `7D` | `2038.50` | 938,380,000.00 USD | 0.00 USD | 938,380,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2040.00` | 527,890,000.00 USD | 0.00 USD | 527,890,000.00 USD | 345,650.00 USD | 178,560.00 USD | 31,670.00 USD |
| `1D` | `2042.60` | 527,330,000.00 USD | 0.00 USD | 527,330,000.00 USD | 626,840.00 USD | 0.00 USD | 20,290.00 USD |
| `7D` | `2045.10` | 936,930,000.00 USD | 0.00 USD | 936,930,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD |
| `1D` | `2045.20` | 526,690,000.00 USD | 0.00 USD | 526,690,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD |
| `1D` | `2047.80` | 526,660,000.00 USD | 0.00 USD | 526,660,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD |
| `1D` | `2050.40` | 525,830,000.00 USD | 0.00 USD | 525,830,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2051.70` | 936,630,000.00 USD | 0.00 USD | 936,630,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2053.00` | 524,720,000.00 USD | 0.00 USD | 524,720,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD |
| `1D` | `2055.60` | 524,700,000.00 USD | 0.00 USD | 524,700,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD |
| `1D` | `2058.20` | 524,370,000.00 USD | 0.00 USD | 524,370,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2058.30` | 934,120,000.00 USD | 0.00 USD | 934,120,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `1D` | `2060.80` | 523,610,000.00 USD | 0.00 USD | 523,610,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD |
| `7D` | `2061.60` | 933,780,000.00 USD | 0.00 USD | 933,780,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `1D` | `2063.40` | 523,530,000.00 USD | 0.00 USD | 523,530,000.00 USD | 643,750.00 USD | 555,980.00 USD | 600,330.00 USD |
| `7D` | `2064.90` | 928,520,000.00 USD | 0.00 USD | 928,520,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD |
| `1D` | `2066.00` | 521,730,000.00 USD | 0.00 USD | 521,730,000.00 USD | 808,950.00 USD | 100,330.00 USD | 53,680.00 USD |
| `7D` | `2068.20` | 925,990,000.00 USD | 0.00 USD | 925,990,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD |
| `1D` | `2068.60` | 520,770,000.00 USD | 0.00 USD | 520,770,000.00 USD | 57,300.00 USD | 1,270,000.00 USD | 26,970.00 USD |
| `1D` | `2071.20` | 519,410,000.00 USD | 0.00 USD | 519,410,000.00 USD | 1,040,000.00 USD | 534,600.00 USD | 437,490.00 USD |
| `7D` | `2071.50` | 921,500,000.00 USD | 0.00 USD | 921,500,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD |
| `1D` | `2073.80` | 517,400,000.00 USD | 0.00 USD | 517,400,000.00 USD | 419,970.00 USD | 62,630.00 USD | 926,730.00 USD |
| `7D` | `2074.80` | 915,040,000.00 USD | 0.00 USD | 915,040,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD |
| `1D` | `2076.40` | 515,990,000.00 USD | 0.00 USD | 515,990,000.00 USD | 2,580,000.00 USD | 1,020,000.00 USD | 2,000,000.00 USD |
| `7D` | `2078.10` | 903,340,000.00 USD | 0.00 USD | 903,340,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD |
| `1D` | `2079.00` | 510,390,000.00 USD | 0.00 USD | 510,390,000.00 USD | 1,320,000.00 USD | 1,010,000.00 USD | 436,470.00 USD |
| `7D` | `2081.40` | 891,050,000.00 USD | 0.00 USD | 891,050,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD |
| `1D` | `2081.60` | 507,620,000.00 USD | 0.00 USD | 507,620,000.00 USD | 1,430,000.00 USD | 1,260,000.00 USD | 227,550.00 USD |
| `1D` | `2084.20` | 504,700,000.00 USD | 0.00 USD | 504,700,000.00 USD | 2,090,000.00 USD | 1,290,000.00 USD | 753,020.00 USD |
| `7D` | `2084.70` | 880,410,000.00 USD | 0.00 USD | 880,410,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD |
| `1D` | `2086.80` | 500,570,000.00 USD | 0.00 USD | 500,570,000.00 USD | 1,600,000.00 USD | 1,650,000.00 USD | 1,600,000.00 USD |
| `7D` | `2088.00` | 871,620,000.00 USD | 0.00 USD | 871,620,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD |
| `1D` | `2089.40` | 495,720,000.00 USD | 0.00 USD | 495,720,000.00 USD | 1,080,000.00 USD | 220,540.00 USD | 92,700.00 USD |
| `7D` | `2091.30` | 863,190,000.00 USD | 0.00 USD | 863,190,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD |
| `1D` | `2092.00` | 494,330,000.00 USD | 0.00 USD | 494,330,000.00 USD | 1,130,000.00 USD | 514,440.00 USD | 955,070.00 USD |
| `1D` | `2094.60` | 491,720,000.00 USD | 0.00 USD | 491,720,000.00 USD | 2,040,000.00 USD | 1,120,000.00 USD | 1,430,000.00 USD |
| `7D` | `2094.60` | 850,240,000.00 USD | 0.00 USD | 850,240,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD |
| `1D` | `2097.20` | 487,130,000.00 USD | 0.00 USD | 487,130,000.00 USD | 617,040.00 USD | 1,010,000.00 USD | 984,190.00 USD |
| `7D` | `2097.90` | 840,020,000.00 USD | 0.00 USD | 840,020,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD |
| `1D` | `2099.80` | 484,520,000.00 USD | 0.00 USD | 484,520,000.00 USD | 172,210.00 USD | 403,100.00 USD | 11,930.00 USD |
| `7D` | `2101.20` | 833,180,000.00 USD | 0.00 USD | 833,180,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD |
| `1D` | `2102.40` | 483,930,000.00 USD | 0.00 USD | 483,930,000.00 USD | 507,510.00 USD | 289,160.00 USD | 466,670.00 USD |
| `7D` | `2104.50` | 826,580,000.00 USD | 0.00 USD | 826,580,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD |
| `1D` | `2105.00` | 482,670,000.00 USD | 0.00 USD | 482,670,000.00 USD | 612,280.00 USD | 671,930.00 USD | 30,860.00 USD |
| `1D` | `2107.60` | 481,350,000.00 USD | 0.00 USD | 481,350,000.00 USD | 603,300.00 USD | 0.00 USD | 488,260.00 USD |
| `7D` | `2107.80` | 821,140,000.00 USD | 0.00 USD | 821,140,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD |
| `1D` | `2110.20` | 480,260,000.00 USD | 0.00 USD | 480,260,000.00 USD | 61,010.00 USD | 31,550.00 USD | 196,840.00 USD |
| `7D` | `2111.10` | 816,650,000.00 USD | 0.00 USD | 816,650,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD |
| `1D` | `2112.80` | 479,970,000.00 USD | 0.00 USD | 479,970,000.00 USD | 911,810.00 USD | 643,210.00 USD | 224,810.00 USD |
| `7D` | `2114.40` | 808,610,000.00 USD | 0.00 USD | 808,610,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD |
| `1D` | `2115.40` | 478,190,000.00 USD | 0.00 USD | 478,190,000.00 USD | 0.00 USD | 13,230.00 USD | 426,410.00 USD |
| `7D` | `2117.70` | 801,880,000.00 USD | 0.00 USD | 801,880,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD |
| `1D` | `2118.00` | 477,750,000.00 USD | 0.00 USD | 477,750,000.00 USD | 202,840.00 USD | 14,580.00 USD | 472,930.00 USD |
| `1D` | `2120.60` | 477,060,000.00 USD | 0.00 USD | 477,060,000.00 USD | 744,340.00 USD | 215,530.00 USD | 1,050,000.00 USD |
| `7D` | `2121.00` | 793,040,000.00 USD | 0.00 USD | 793,040,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD |
| `1D` | `2123.20` | 475,050,000.00 USD | 0.00 USD | 475,050,000.00 USD | 757,170.00 USD | 1,210,000.00 USD | 917,970.00 USD |
| `7D` | `2124.30` | 786,240,000.00 USD | 0.00 USD | 786,240,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD |
| `1D` | `2125.80` | 472,170,000.00 USD | 0.00 USD | 472,170,000.00 USD | 68,480.00 USD | 554,160.00 USD | 0.00 USD |
| `7D` | `2127.60` | 782,920,000.00 USD | 0.00 USD | 782,920,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD |
| `1D` | `2128.40` | 471,540,000.00 USD | 0.00 USD | 471,540,000.00 USD | 107,010.00 USD | 475,750.00 USD | 0.00 USD |
| `7D` | `2130.90` | 774,620,000.00 USD | 0.00 USD | 774,620,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD |
| `1D` | `2131.00` | 470,960,000.00 USD | 0.00 USD | 470,960,000.00 USD | 0.00 USD | 18,610.00 USD | 331,620.00 USD |
| `7D` | `2134.20` | 768,200,000.00 USD | 0.00 USD | 768,200,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD |
| `1D` | `2136.20` | 470,610,000.00 USD | 0.00 USD | 470,610,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD |
| `7D` | `2137.50` | 765,170,000.00 USD | 0.00 USD | 765,170,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD |
| `7D` | `2140.80` | 763,210,000.00 USD | 0.00 USD | 763,210,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2144.10` | 759,270,000.00 USD | 0.00 USD | 759,270,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD |
| `7D` | `2147.40` | 757,430,000.00 USD | 0.00 USD | 757,430,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD |
| `7D` | `2150.70` | 756,350,000.00 USD | 0.00 USD | 756,350,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD |
| `1D` | `2151.80` | 470,330,000.00 USD | 0.00 USD | 470,330,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD |
| `7D` | `2154.00` | 755,390,000.00 USD | 0.00 USD | 755,390,000.00 USD | 128,430.00 USD | 311,060.00 USD | 32,590.00 USD |
| `1D` | `2154.40` | 469,680,000.00 USD | 0.00 USD | 469,680,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD |
| `7D` | `2157.30` | 754,920,000.00 USD | 0.00 USD | 754,920,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD |
| `1D` | `2159.60` | 468,290,000.00 USD | 0.00 USD | 468,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 37,580.00 USD |
| `7D` | `2160.60` | 752,430,000.00 USD | 0.00 USD | 752,430,000.00 USD | 613,630.00 USD | 1,900,000.00 USD | 1,990,000.00 USD |
| `1D` | `2162.20` | 465,960,000.00 USD | 0.00 USD | 465,960,000.00 USD | 0.00 USD | 932,730.00 USD | 100,530.00 USD |
| `7D` | `2163.90` | 747,910,000.00 USD | 0.00 USD | 747,910,000.00 USD | 566,120.00 USD | 2,950,000.00 USD | 540,130.00 USD |
| `1D` | `2164.80` | 464,930,000.00 USD | 0.00 USD | 464,930,000.00 USD | 217,960.00 USD | 408,000.00 USD | 107,900.00 USD |
| `7D` | `2167.20` | 743,850,000.00 USD | 0.00 USD | 743,850,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD |
| `1D` | `2167.40` | 464,190,000.00 USD | 0.00 USD | 464,190,000.00 USD | 3,220,000.00 USD | 0.00 USD | 1,020,000.00 USD |
| `1D` | `2170.00` | 459,950,000.00 USD | 0.00 USD | 459,950,000.00 USD | 5,210,000.00 USD | 5,170,000.00 USD | 2,740,000.00 USD |
| `7D` | `2170.50` | 740,150,000.00 USD | 0.00 USD | 740,150,000.00 USD | 3,500,000.00 USD | 3,730,000.00 USD | 5,210,000.00 USD |
| `1D` | `2172.60` | 446,820,000.00 USD | 0.00 USD | 446,820,000.00 USD | 63,650.00 USD | 1,290,000.00 USD | 581,810.00 USD |
| `7D` | `2173.80` | 727,710,000.00 USD | 0.00 USD | 727,710,000.00 USD | 4,370,000.00 USD | 363,040.00 USD | 1,130,000.00 USD |
| `1D` | `2175.20` | 444,890,000.00 USD | 0.00 USD | 444,890,000.00 USD | 1,970,000.00 USD | 111,190.00 USD | 894,600.00 USD |
| `7D` | `2177.10` | 721,850,000.00 USD | 0.00 USD | 721,850,000.00 USD | 1,750,000.00 USD | 1,330,000.00 USD | 2,820,000.00 USD |
| `1D` | `2177.80` | 441,920,000.00 USD | 0.00 USD | 441,920,000.00 USD | 2,320,000.00 USD | 1,770,000.00 USD | 99,000.00 USD |
| `1D` | `2180.40` | 437,720,000.00 USD | 0.00 USD | 437,720,000.00 USD | 2,080,000.00 USD | 267,450.00 USD | 1,420,000.00 USD |
| `7D` | `2180.40` | 715,950,000.00 USD | 0.00 USD | 715,950,000.00 USD | 0.00 USD | 373,740.00 USD | 431,800.00 USD |
| `1D` | `2183.00` | 433,960,000.00 USD | 0.00 USD | 433,960,000.00 USD | 2,960,000.00 USD | 1,140,000.00 USD | 425,980.00 USD |
| `7D` | `2183.70` | 715,150,000.00 USD | 0.00 USD | 715,150,000.00 USD | 1,760,000.00 USD | 1,310,000.00 USD | 3,950,000.00 USD |
| `1D` | `2185.60` | 429,440,000.00 USD | 0.00 USD | 429,440,000.00 USD | 566,020.00 USD | 1,960,000.00 USD | 2,690,000.00 USD |
| `7D` | `2187.00` | 708,140,000.00 USD | 0.00 USD | 708,140,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD |
| `1D` | `2188.20` | 424,220,000.00 USD | 0.00 USD | 424,220,000.00 USD | 0.00 USD | 42,550.00 USD | 0.00 USD |
| `7D` | `2190.30` | 707,530,000.00 USD | 0.00 USD | 707,530,000.00 USD | 2,730,000.00 USD | 0.00 USD | 4,200,000.00 USD |
| `1D` | `2190.80` | 424,180,000.00 USD | 0.00 USD | 424,180,000.00 USD | 0.00 USD | 222,200.00 USD | 764,360.00 USD |
| `1D` | `2193.40` | 423,190,000.00 USD | 0.00 USD | 423,190,000.00 USD | 605,210.00 USD | 0.00 USD | 39,000.00 USD |
| `1D` | `2196.00` | 422,550,000.00 USD | 0.00 USD | 422,550,000.00 USD | 416,500.00 USD | 881,070.00 USD | 1,890,000.00 USD |
| `7D` | `2196.90` | 700,600,000.00 USD | 0.00 USD | 700,600,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 2,040,000.00 USD |
| `1D` | `2198.60` | 419,370,000.00 USD | 0.00 USD | 419,370,000.00 USD | 0.00 USD | 2,940,000.00 USD | 50,830.00 USD |
| `7D` | `2200.20` | 695,500,000.00 USD | 0.00 USD | 695,500,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD |
| `1D` | `2201.20` | 416,370,000.00 USD | 0.00 USD | 416,370,000.00 USD | 1,690,000.00 USD | 1,450,000.00 USD | 1,500,000.00 USD |
| `7D` | `2203.50` | 684,230,000.00 USD | 0.00 USD | 684,230,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD |
| `1D` | `2203.80` | 411,730,000.00 USD | 0.00 USD | 411,730,000.00 USD | 2,130,000.00 USD | 314,310.00 USD | 830,450.00 USD |
| `1D` | `2206.40` | 408,450,000.00 USD | 0.00 USD | 408,450,000.00 USD | 755,060.00 USD | 10,820,000.00 USD | 945,060.00 USD |
| `7D` | `2206.80` | 675,120,000.00 USD | 0.00 USD | 675,120,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD |
| `1D` | `2209.00` | 395,930,000.00 USD | 0.00 USD | 395,930,000.00 USD | 2,720,000.00 USD | 2,140,000.00 USD | 3,050,000.00 USD |
| `7D` | `2210.10` | 654,750,000.00 USD | 0.00 USD | 654,750,000.00 USD | 12,800,000.00 USD | 20,410,000.00 USD | 6,470,000.00 USD |
| `1D` | `2211.60` | 388,020,000.00 USD | 0.00 USD | 388,020,000.00 USD | 6,110,000.00 USD | 2,320,000.00 USD | 5,100,000.00 USD |
| `7D` | `2213.40` | 615,070,000.00 USD | 0.00 USD | 615,070,000.00 USD | 10,920,000.00 USD | 14,590,000.00 USD | 19,950,000.00 USD |
| `1D` | `2214.20` | 374,490,000.00 USD | 0.00 USD | 374,490,000.00 USD | 15,370,000.00 USD | 11,020,000.00 USD | 7,020,000.00 USD |
| `7D` | `2216.70` | 569,600,000.00 USD | 0.00 USD | 569,600,000.00 USD | 25,710,000.00 USD | 17,030,000.00 USD | 9,390,000.00 USD |
| `1D` | `2216.80` | 341,080,000.00 USD | 0.00 USD | 341,080,000.00 USD | 10,700,000.00 USD | 9,030,000.00 USD | 6,310,000.00 USD |
| `1D` | `2219.40` | 315,030,000.00 USD | 0.00 USD | 315,030,000.00 USD | 9,410,000.00 USD | 8,320,000.00 USD | 3,010,000.00 USD |
| `7D` | `2220.00` | 517,470,000.00 USD | 0.00 USD | 517,470,000.00 USD | 27,820,000.00 USD | 14,950,000.00 USD | 16,000,000.00 USD |
| `1D` | `2222.00` | 294,290,000.00 USD | 0.00 USD | 294,290,000.00 USD | 9,930,000.00 USD | 12,880,000.00 USD | 2,090,000.00 USD |
| `7D` | `2223.30` | 458,700,000.00 USD | 0.00 USD | 458,700,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD |
| `1D` | `2224.60` | 269,390,000.00 USD | 0.00 USD | 269,390,000.00 USD | 9,460,000.00 USD | 4,680,000.00 USD | 5,370,000.00 USD |
| `7D` | `2226.60` | 428,420,000.00 USD | 0.00 USD | 428,420,000.00 USD | 16,350,000.00 USD | 11,030,000.00 USD | 10,460,000.00 USD |
| `1D` | `2227.20` | 249,870,000.00 USD | 0.00 USD | 249,870,000.00 USD | 5,120,000.00 USD | 13,730,000.00 USD | 5,700,000.00 USD |
| `1D` | `2229.80` | 225,310,000.00 USD | 0.00 USD | 225,310,000.00 USD | 10,100,000.00 USD | 7,120,000.00 USD | 4,090,000.00 USD |
| `7D` | `2229.90` | 390,570,000.00 USD | 0.00 USD | 390,570,000.00 USD | 12,730,000.00 USD | 11,790,000.00 USD | 28,550,000.00 USD |
| `1D` | `2232.40` | 204,000,000.00 USD | 0.00 USD | 204,000,000.00 USD | 4,620,000.00 USD | 6,200,000.00 USD | 7,280,000.00 USD |
| `7D` | `2233.20` | 337,500,000.00 USD | 0.00 USD | 337,500,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD |
| `1D` | `2235.00` | 185,910,000.00 USD | 0.00 USD | 185,910,000.00 USD | 19,080,000.00 USD | 85,110.00 USD | 11,450,000.00 USD |
| `7D` | `2236.50` | 286,180,000.00 USD | 0.00 USD | 286,180,000.00 USD | 16,050,000.00 USD | 7,430,000.00 USD | 27,770,000.00 USD |
| `1D` | `2237.60` | 155,300,000.00 USD | 0.00 USD | 155,300,000.00 USD | 23,860,000.00 USD | 7,390,000.00 USD | 12,450,000.00 USD |
| `7D` | `2239.80` | 234,940,000.00 USD | 0.00 USD | 234,940,000.00 USD | 16,720,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD |
| `1D` | `2240.20` | 111,600,000.00 USD | 0.00 USD | 111,600,000.00 USD | 1,100,000.00 USD | 1,380,000.00 USD | 2,220,000.00 USD |
| `1D` | `2242.80` | 106,890,000.00 USD | 0.00 USD | 106,890,000.00 USD | 9,030,000.00 USD | 3,760,000.00 USD | 9,240,000.00 USD |
| `7D` | `2243.10` | 197,880,000.00 USD | 0.00 USD | 197,880,000.00 USD | 29,940,000.00 USD | 5,310,000.00 USD | 24,810,000.00 USD |
| `1D` | `2245.40` | 84,870,000.00 USD | 0.00 USD | 84,870,000.00 USD | 11,210,000.00 USD | 6,190,000.00 USD | 501,600.00 USD |
| `7D` | `2246.40` | 137,820,000.00 USD | 0.00 USD | 137,820,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD |
| `1D` | `2248.00` | 66,970,000.00 USD | 0.00 USD | 66,970,000.00 USD | 12,490,000.00 USD | 1,070,000.00 USD | 7,120,000.00 USD |
| `7D` | `2249.70` | 109,560,000.00 USD | 0.00 USD | 109,560,000.00 USD | 25,030,000.00 USD | 0.00 USD | 19,440,000.00 USD |
| `1D` | `2250.60` | 46,290,000.00 USD | 0.00 USD | 46,290,000.00 USD | 4,450,000.00 USD | 4,540,000.00 USD | 5,610,000.00 USD |
| `7D` | `2253.00` | 65,090,000.00 USD | 0.00 USD | 65,090,000.00 USD | 26,890,000.00 USD | 0.00 USD | 12,040,000.00 USD |
| `1D` | `2253.20` | 31,680,000.00 USD | 0.00 USD | 31,680,000.00 USD | 13,840,000.00 USD | 4,440,000.00 USD | 8,130,000.00 USD |
| `1D` | `2255.80` | 5,280,000.00 USD | 0.00 USD | 5,280,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD |
| `7D` | `2256.30` | 26,160,000.00 USD | 0.00 USD | 26,160,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2258.40` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 0.00 USD | 170,210.00 USD | 0.00 USD |
| `7D` | `2259.60` | 10,940,000.00 USD | 0.00 USD | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2261.00` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 156,010.00 USD |
| `1D` | `2266.20` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 1,560,000.00 USD |
| `7D` | `2266.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2266.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2268.80` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,980,000.00 USD |
| `1D` | `2274.00` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 288,080.00 USD | 114,460.00 USD |
| `1D` | `2276.60` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 267,040.00 USD | 0.00 USD |
| `1D` | `2279.20` | 22,720,000.00 USD | 22,720,000.00 USD | 0.00 USD | 11,600,000.00 USD | 3,950,000.00 USD | 4,520,000.00 USD |
| `7D` | `2279.40` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 0.00 USD | 17,000,000.00 USD | 0.00 USD |
| `1D` | `2281.80` | 85,490,000.00 USD | 85,490,000.00 USD | 0.00 USD | 33,480,000.00 USD | 26,790,000.00 USD | 2,500,000.00 USD |
| `7D` | `2282.70` | 117,630,000.00 USD | 117,630,000.00 USD | 0.00 USD | 0.00 USD | 87,090,000.00 USD | 13,550,000.00 USD |
| `1D` | `2284.40` | 152,200,000.00 USD | 152,200,000.00 USD | 0.00 USD | 33,020,000.00 USD | 19,430,000.00 USD | 14,270,000.00 USD |
| `7D` | `2286.00` | 128,050,000.00 USD | 128,050,000.00 USD | 0.00 USD | 1,010,000.00 USD | 9,400,000.00 USD | 0.00 USD |
| `1D` | `2287.00` | 164,470,000.00 USD | 164,470,000.00 USD | 0.00 USD | 3,210,000.00 USD | 5,140,000.00 USD | 3,920,000.00 USD |
| `7D` | `2289.30` | 152,130,000.00 USD | 152,130,000.00 USD | 0.00 USD | 7,010,000.00 USD | 5,310,000.00 USD | 11,760,000.00 USD |
| `1D` | `2289.60` | 176,810,000.00 USD | 176,810,000.00 USD | 0.00 USD | 3,280,000.00 USD | 8,840,000.00 USD | 219,440.00 USD |
| `1D` | `2292.20` | 197,140,000.00 USD | 197,140,000.00 USD | 0.00 USD | 17,600,000.00 USD | 2,560,000.00 USD | 176,580.00 USD |
| `7D` | `2292.60` | 153,150,000.00 USD | 153,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,020,000.00 USD |
| `1D` | `2294.80` | 209,490,000.00 USD | 209,490,000.00 USD | 0.00 USD | 0.00 USD | 6,490,000.00 USD | 5,860,000.00 USD |
| `7D` | `2295.90` | 180,460,000.00 USD | 180,460,000.00 USD | 0.00 USD | 13,610,000.00 USD | 2,380,000.00 USD | 11,320,000.00 USD |
| `1D` | `2297.40` | 233,240,000.00 USD | 233,240,000.00 USD | 0.00 USD | 11,830,000.00 USD | 6,530,000.00 USD | 5,390,000.00 USD |
| `7D` | `2299.20` | 208,880,000.00 USD | 208,880,000.00 USD | 0.00 USD | 11,730,000.00 USD | 11,130,000.00 USD | 5,560,000.00 USD |
| `1D` | `2300.00` | 249,950,000.00 USD | 249,950,000.00 USD | 0.00 USD | 2,700,000.00 USD | 6,620,000.00 USD | 7,390,000.00 USD |
| `7D` | `2302.50` | 255,990,000.00 USD | 255,990,000.00 USD | 0.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 16,850,000.00 USD |
| `1D` | `2302.60` | 269,830,000.00 USD | 269,830,000.00 USD | 0.00 USD | 14,790,000.00 USD | 170,210.00 USD | 4,910,000.00 USD |
| `1D` | `2305.20` | 299,270,000.00 USD | 299,270,000.00 USD | 0.00 USD | 10,430,000.00 USD | 14,490,000.00 USD | 4,530,000.00 USD |
| `7D` | `2305.80` | 276,770,000.00 USD | 276,770,000.00 USD | 0.00 USD | 2,980,000.00 USD | 8,820,000.00 USD | 8,970,000.00 USD |
| `1D` | `2307.80` | 307,480,000.00 USD | 307,480,000.00 USD | 0.00 USD | 2,550,000.00 USD | 3,220,000.00 USD | 2,440,000.00 USD |
| `7D` | `2309.10` | 281,280,000.00 USD | 281,280,000.00 USD | 0.00 USD | 1,240,000.00 USD | 930,630.00 USD | 2,350,000.00 USD |
| `1D` | `2310.40` | 323,320,000.00 USD | 323,320,000.00 USD | 0.00 USD | 3,940,000.00 USD | 2,450,000.00 USD | 9,450,000.00 USD |
| `7D` | `2312.40` | 308,580,000.00 USD | 308,580,000.00 USD | 0.00 USD | 10,780,000.00 USD | 2,650,000.00 USD | 13,870,000.00 USD |
| `1D` | `2313.00` | 335,020,000.00 USD | 335,020,000.00 USD | 0.00 USD | 4,650,000.00 USD | 6,730,000.00 USD | 313,050.00 USD |
| `1D` | `2315.60` | 366,280,000.00 USD | 366,280,000.00 USD | 0.00 USD | 9,790,000.00 USD | 14,850,000.00 USD | 6,630,000.00 USD |
| `7D` | `2315.70` | 316,670,000.00 USD | 316,670,000.00 USD | 0.00 USD | 0.00 USD | 7,460,000.00 USD | 627,210.00 USD |
| `1D` | `2318.20` | 379,270,000.00 USD | 379,270,000.00 USD | 0.00 USD | 4,440,000.00 USD | 6,320,000.00 USD | 2,230,000.00 USD |
| `7D` | `2319.00` | 334,170,000.00 USD | 334,170,000.00 USD | 0.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 8,420,000.00 USD |
| `1D` | `2320.80` | 396,910,000.00 USD | 396,910,000.00 USD | 0.00 USD | 5,790,000.00 USD | 9,890,000.00 USD | 1,960,000.00 USD |
| `7D` | `2322.30` | 351,330,000.00 USD | 351,330,000.00 USD | 0.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 108,040.00 USD |
| `1D` | `2323.40` | 412,610,000.00 USD | 412,610,000.00 USD | 0.00 USD | 1,710,000.00 USD | 10,410,000.00 USD | 3,590,000.00 USD |
| `7D` | `2325.60` | 371,980,000.00 USD | 371,980,000.00 USD | 0.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD |
| `1D` | `2326.00` | 424,390,000.00 USD | 424,390,000.00 USD | 0.00 USD | 479,120.00 USD | 5,640,000.00 USD | 5,660,000.00 USD |
| `1D` | `2328.60` | 427,380,000.00 USD | 427,380,000.00 USD | 0.00 USD | 2,140,000.00 USD | 444,400.00 USD | 402,280.00 USD |
| `7D` | `2328.90` | 383,810,000.00 USD | 383,810,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD |
| `1D` | `2331.20` | 445,540,000.00 USD | 445,540,000.00 USD | 0.00 USD | 17,350,000.00 USD | 692,470.00 USD | 126,990.00 USD |
| `7D` | `2332.20` | 413,040,000.00 USD | 413,040,000.00 USD | 0.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2333.80` | 463,270,000.00 USD | 463,270,000.00 USD | 0.00 USD | 7,710,000.00 USD | 2,820,000.00 USD | 7,200,000.00 USD |
| `7D` | `2335.50` | 471,050,000.00 USD | 471,050,000.00 USD | 0.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 10,600,000.00 USD |
| `1D` | `2336.40` | 481,890,000.00 USD | 481,890,000.00 USD | 0.00 USD | 15,940,000.00 USD | 547,950.00 USD | 2,140,000.00 USD |
| `7D` | `2338.80` | 488,920,000.00 USD | 488,920,000.00 USD | 0.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD |
| `1D` | `2339.00` | 494,900,000.00 USD | 494,900,000.00 USD | 0.00 USD | 6,360,000.00 USD | 2,600,000.00 USD | 4,050,000.00 USD |
| `1D` | `2341.60` | 513,570,000.00 USD | 513,570,000.00 USD | 0.00 USD | 5,340,000.00 USD | 3,430,000.00 USD | 9,900,000.00 USD |
| `7D` | `2342.10` | 529,020,000.00 USD | 529,020,000.00 USD | 0.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD |
| `1D` | `2344.20` | 526,900,000.00 USD | 526,900,000.00 USD | 0.00 USD | 1,370,000.00 USD | 6,240,000.00 USD | 5,710,000.00 USD |
| `7D` | `2345.40` | 550,400,000.00 USD | 550,400,000.00 USD | 0.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD |
| `1D` | `2346.80` | 540,470,000.00 USD | 540,470,000.00 USD | 0.00 USD | 3,930,000.00 USD | 3,010,000.00 USD | 6,620,000.00 USD |
| `7D` | `2348.70` | 588,270,000.00 USD | 588,270,000.00 USD | 0.00 USD | 847,620.00 USD | 9,500,000.00 USD | 27,530,000.00 USD |
| `1D` | `2349.40` | 571,320,000.00 USD | 571,320,000.00 USD | 0.00 USD | 19,450,000.00 USD | 5,980,000.00 USD | 5,420,000.00 USD |
| `1D` | `2352.00` | 598,840,000.00 USD | 598,840,000.00 USD | 0.00 USD | 18,420,000.00 USD | 2,080,000.00 USD | 7,020,000.00 USD |
| `7D` | `2352.00` | 624,900,000.00 USD | 624,900,000.00 USD | 0.00 USD | 2,930,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD |
| `1D` | `2354.60` | 622,470,000.00 USD | 622,470,000.00 USD | 0.00 USD | 973,980.00 USD | 20,450,000.00 USD | 2,200,000.00 USD |
| `7D` | `2355.30` | 684,440,000.00 USD | 684,440,000.00 USD | 0.00 USD | 18,530,000.00 USD | 38,020,000.00 USD | 3,000,000.00 USD |
| `1D` | `2357.20` | 632,150,000.00 USD | 632,150,000.00 USD | 0.00 USD | 4,390,000.00 USD | 1,740,000.00 USD | 3,550,000.00 USD |
| `7D` | `2358.60` | 696,580,000.00 USD | 696,580,000.00 USD | 0.00 USD | 7,110,000.00 USD | 512,220.00 USD | 4,510,000.00 USD |
| `1D` | `2359.80` | 653,040,000.00 USD | 653,040,000.00 USD | 0.00 USD | 8,920,000.00 USD | 6,950,000.00 USD | 5,030,000.00 USD |
| `7D` | `2361.90` | 703,960,000.00 USD | 703,960,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 431,800.00 USD |
| `1D` | `2362.40` | 673,590,000.00 USD | 673,590,000.00 USD | 0.00 USD | 8,900,000.00 USD | 6,710,000.00 USD | 4,940,000.00 USD |
| `1D` | `2365.00` | 690,810,000.00 USD | 690,810,000.00 USD | 0.00 USD | 6,420,000.00 USD | 4,850,000.00 USD | 5,940,000.00 USD |
| `7D` | `2365.20` | 725,010,000.00 USD | 725,010,000.00 USD | 0.00 USD | 10,200,000.00 USD | 0.00 USD | 10,860,000.00 USD |
| `1D` | `2367.60` | 699,590,000.00 USD | 699,590,000.00 USD | 0.00 USD | 4,770,000.00 USD | 1,110,000.00 USD | 2,910,000.00 USD |
| `7D` | `2368.50` | 738,080,000.00 USD | 738,080,000.00 USD | 0.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 458,400.00 USD |
| `1D` | `2370.20` | 735,010,000.00 USD | 735,010,000.00 USD | 0.00 USD | 14,350,000.00 USD | 12,620,000.00 USD | 8,450,000.00 USD |
| `7D` | `2371.80` | 819,020,000.00 USD | 819,020,000.00 USD | 0.00 USD | 26,000,000.00 USD | 0.00 USD | 54,940,000.00 USD |
| `1D` | `2372.80` | 761,980,000.00 USD | 761,980,000.00 USD | 0.00 USD | 14,450,000.00 USD | 5,460,000.00 USD | 7,060,000.00 USD |
| `7D` | `2375.10` | 845,960,000.00 USD | 845,960,000.00 USD | 0.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD |
| `1D` | `2375.40` | 780,580,000.00 USD | 780,580,000.00 USD | 0.00 USD | 11,510,000.00 USD | 3,420,000.00 USD | 3,670,000.00 USD |
| `1D` | `2378.00` | 803,100,000.00 USD | 803,100,000.00 USD | 0.00 USD | 5,030,000.00 USD | 6,270,000.00 USD | 11,220,000.00 USD |
| `7D` | `2378.40` | 891,380,000.00 USD | 891,380,000.00 USD | 0.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD |
| `1D` | `2380.60` | 840,470,000.00 USD | 840,470,000.00 USD | 0.00 USD | 11,320,000.00 USD | 11,190,000.00 USD | 14,860,000.00 USD |
| `7D` | `2381.70` | 931,170,000.00 USD | 931,170,000.00 USD | 0.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 24,530,000.00 USD |
| `1D` | `2383.20` | 886,340,000.00 USD | 886,340,000.00 USD | 0.00 USD | 20,060,000.00 USD | 12,500,000.00 USD | 13,320,000.00 USD |
| `7D` | `2385.00` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD |
| `1D` | `2385.80` | 910,150,000.00 USD | 910,150,000.00 USD | 0.00 USD | 8,950,000.00 USD | 10,960,000.00 USD | 3,910,000.00 USD |
| `7D` | `2388.30` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD |
| `1D` | `2388.40` | 935,260,000.00 USD | 935,260,000.00 USD | 0.00 USD | 13,100,000.00 USD | 6,720,000.00 USD | 5,290,000.00 USD |
| `1D` | `2391.00` | 950,870,000.00 USD | 950,870,000.00 USD | 0.00 USD | 3,770,000.00 USD | 6,670,000.00 USD | 5,160,000.00 USD |
| `7D` | `2391.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD |
| `1D` | `2393.60` | 965,250,000.00 USD | 965,250,000.00 USD | 0.00 USD | 4,380,000.00 USD | 6,000,000.00 USD | 4,000,000.00 USD |
| `7D` | `2394.90` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD |
| `1D` | `2396.20` | 979,190,000.00 USD | 979,190,000.00 USD | 0.00 USD | 5,350,000.00 USD | 4,020,000.00 USD | 4,560,000.00 USD |
| `7D` | `2398.20` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 0.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD |
| `1D` | `2398.80` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 8,890,000.00 USD | 6,800,000.00 USD | 7,690,000.00 USD |
| `1D` | `2401.40` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 4,600,000.00 USD | 6,190,000.00 USD | 6,540,000.00 USD |
| `7D` | `2401.50` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD |
| `1D` | `2404.00` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 9,470,000.00 USD | 8,980,000.00 USD | 7,870,000.00 USD |
| `7D` | `2404.80` | 1,670,000,000.00 USD | 1,670,000,000.00 USD | 0.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD |
| `1D` | `2406.60` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 11,990,000.00 USD | 7,780,000.00 USD | 5,990,000.00 USD |
| `7D` | `2408.10` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 0.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD |
| `1D` | `2409.20` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 8,220,000.00 USD | 6,130,000.00 USD | 6,800,000.00 USD |
| `7D` | `2411.40` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 0.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD |
| `1D` | `2411.80` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 8,840,000.00 USD | 7,170,000.00 USD | 3,340,000.00 USD |
| `1D` | `2414.40` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 2,970,000.00 USD | 2,340,000.00 USD | 2,320,000.00 USD |
| `7D` | `2414.70` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 0.00 USD | 23,820,000.00 USD | 21,740,000.00 USD | 23,130,000.00 USD |
| `1D` | `2417.00` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 3,600,000.00 USD | 2,550,000.00 USD | 3,160,000.00 USD |
| `7D` | `2418.00` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 0.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,450,000.00 USD |
| `1D` | `2419.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 6,520,000.00 USD | 3,840,000.00 USD | 3,660,000.00 USD |
| `7D` | `2421.30` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 0.00 USD | 25,700,000.00 USD | 27,770,000.00 USD | 21,590,000.00 USD |
| `1D` | `2422.20` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 2,930,000.00 USD | 3,700,000.00 USD | 5,020,000.00 USD |
| `7D` | `2424.60` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 23,650,000.00 USD | 31,040,000.00 USD | 34,520,000.00 USD |
| `1D` | `2424.80` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 1,500,000.00 USD | 2,700,000.00 USD | 844,590.00 USD |
| `1D` | `2427.40` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 634,700.00 USD | 89,750.00 USD | 601,200.00 USD |
| `7D` | `2427.90` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 25,200,000.00 USD | 15,090,000.00 USD | 18,920,000.00 USD |
| `1D` | `2430.00` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,550,000.00 USD | 1,770,000.00 USD | 1,220,000.00 USD |
| `7D` | `2431.20` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 10,380,000.00 USD | 17,060,000.00 USD | 9,300,000.00 USD |
| `1D` | `2432.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 2,090,000.00 USD | 1,690,000.00 USD | 247,270.00 USD |
| `7D` | `2434.50` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,160,000.00 USD |
| `1D` | `2435.20` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,790,000.00 USD | 495,600.00 USD | 1,540,000.00 USD |
| `1D` | `2437.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 777,840.00 USD | 517,090.00 USD | 21,360.00 USD |
| `7D` | `2437.80` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 11,900,000.00 USD | 12,720,000.00 USD | 5,470,000.00 USD |
| `1D` | `2440.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 1,540,000.00 USD | 2,030,000.00 USD | 1,030,000.00 USD |
| `7D` | `2441.10` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,640,000.00 USD |
| `1D` | `2443.00` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 644,860.00 USD | 859,130.00 USD |
| `7D` | `2444.40` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 0.00 USD | 8,860,000.00 USD | 15,100,000.00 USD | 13,960,000.00 USD |
| `1D` | `2445.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 126,820.00 USD | 467,480.00 USD | 799,060.00 USD |
| `7D` | `2447.70` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 0.00 USD | 11,380,000.00 USD | 6,510,000.00 USD | 17,330,000.00 USD |
| `1D` | `2448.20` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 864,380.00 USD | 325,700.00 USD | 1,840,000.00 USD |
| `1D` | `2450.80` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 2,340,000.00 USD | 871,330.00 USD | 3,150,000.00 USD |
| `7D` | `2451.00` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 0.00 USD | 16,710,000.00 USD | 12,450,000.00 USD | 12,710,000.00 USD |
| `1D` | `2453.40` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 4,320,000.00 USD | 3,900,000.00 USD | 2,950,000.00 USD |
| `7D` | `2454.30` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 0.00 USD | 4,620,000.00 USD | 4,930,000.00 USD | 3,880,000.00 USD |
| `1D` | `2456.00` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 793,240.00 USD | 1,840,000.00 USD | 797,640.00 USD |
| `7D` | `2457.60` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 0.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,600,000.00 USD |
| `1D` | `2458.60` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 1,400,000.00 USD | 1,230,000.00 USD | 0.00 USD |
| `7D` | `2460.90` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 0.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD |
| `1D` | `2461.20` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 470,530.00 USD | 46,520.00 USD | 366,800.00 USD |
| `1D` | `2463.80` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 619,960.00 USD | 829,050.00 USD |
| `7D` | `2464.20` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 0.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD |
| `1D` | `2466.40` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2467.50` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD |
| `1D` | `2469.00` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 1,250,000.00 USD | 391,890.00 USD |
| `7D` | `2470.80` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD |
| `7D` | `2474.10` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 0.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD |
| `1D` | `2476.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD |
| `7D` | `2477.40` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD |
| `1D` | `2479.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 26,700.00 USD | 0.00 USD |
| `7D` | `2480.70` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 0.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD |
| `1D` | `2482.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 525,130.00 USD | 136,500.00 USD | 451,780.00 USD |
| `7D` | `2484.00` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 1,430,000.00 USD |
| `1D` | `2484.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 925,970.00 USD | 1,330,000.00 USD | 0.00 USD |
| `1D` | `2487.20` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2487.30` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD |
| `1D` | `2489.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 317,820.00 USD | 30,580.00 USD |
| `7D` | `2490.60` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 239,380.00 USD |
| `1D` | `2492.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 547,850.00 USD | 44,470.00 USD | 357,840.00 USD |
| `7D` | `2493.90` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 1,610,000.00 USD | 1,760,000.00 USD | 3,940,000.00 USD |
| `1D` | `2495.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 626,840.00 USD | 134,080.00 USD | 33,960.00 USD |
| `7D` | `2497.20` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 0.00 USD | 2,860,000.00 USD | 4,270,000.00 USD | 6,460,000.00 USD |
| `1D` | `2497.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,270.00 USD |
| `1D` | `2500.20` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD |
| `7D` | `2500.50` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 1,450,000.00 USD | 1,130,000.00 USD |
| `1D` | `2502.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD |
| `7D` | `2503.80` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 63,860.00 USD | 1,480,000.00 USD | 125,600.00 USD |
| `1D` | `2505.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2507.10` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,180,000.00 USD |
| `7D` | `2510.40` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD |
| `1D` | `2510.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD |
| `1D` | `2513.20` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2513.70` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2515.80` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2517.00` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD |
| `7D` | `2520.30` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2521.00` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 80,610.00 USD | 121,470.00 USD | 88,290.00 USD |
| `1D` | `2523.60` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 563,140.00 USD | 494,150.00 USD | 532,370.00 USD |
| `7D` | `2523.60` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `1D` | `2526.20` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 754,970.00 USD | 304,560.00 USD | 0.00 USD |
| `7D` | `2526.90` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD |
| `7D` | `2530.20` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 0.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `7D` | `2533.50` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD |
| `7D` | `2536.80` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD |
| `7D` | `2540.10` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD |
| `7D` | `2543.40` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD |
| `7D` | `2546.70` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 0.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD |
| `7D` | `2550.00` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD |
| `7D` | `2553.30` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 0.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD |
| `7D` | `2556.60` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 0.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD |
| `7D` | `2559.90` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD |
| `7D` | `2563.20` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD |
| `7D` | `2566.50` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD |
| `7D` | `2569.80` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD |
| `7D` | `2573.10` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD |
| `7D` | `2576.40` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD |
| `7D` | `2579.70` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD |
| `7D` | `2583.00` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD |
| `7D` | `2586.30` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD |
| `7D` | `2589.60` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD |
| `7D` | `2592.90` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD |
| `7D` | `2596.20` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD |
| `7D` | `2599.50` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD |
| `7D` | `2602.80` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD |
| `7D` | `2606.10` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD |
| `7D` | `2609.40` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD |
| `7D` | `2612.70` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD |
| `7D` | `2616.00` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2619.30` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD |
| `7D` | `2622.60` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD |
| `7D` | `2625.90` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD |
| `7D` | `2629.20` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,040.00 USD |
| `7D` | `2632.40` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `28.88B` | Total OI Tokens: `13,031,467.2 ETH`
  * 1h OI Change: `+0.16%` | 4h OI Change: `-1.49%` | 24h OI Change: `-2.97%`
  * Exchange Breakdown: Binance=`8.38B` | Bybit=`2.09B` | OKX=`1.79B` | Hyperliquid=`2.34B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-579.76K` | Last 24h: `1.05M` | Last 3d: `6.29M` | Last 7d: `12.86M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0028%` | **USDT OKX** | `-0.0084%` |
| **USDT Bybit** | `-0.0176%` | **USDT KuCoin** | `-0.0143%` |
| **USDT MEXC** | `-0.0028%` | **USDT BingX** | `-0.0002%` |
| **USDT Gate** | `-0.0108%` | **USDT Bitget** | `-0.0004%` |
| **CoinM Binance** | `0.0051%` | **CoinM OKX** | `0.0015%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `49.14%` | `50.86%` | `0.97` | 507,700,000.00 USD |
| `15M` | `Binance` | `45.11%` | `54.89%` | `0.82` | 166,040,000.00 USD |
| `15M` | `OKX` | `54.01%` | `45.99%` | `1.17` | 60,710,000.00 USD |
| `15M` | `Bybit` | `57.68%` | `42.32%` | `1.36` | 60,300,000.00 USD |
| `15M` | `KuCoin` | `75.47%` | `24.53%` | `3.08` | 2,150,000.00 USD |
| `15M` | `Gate` | `38.93%` | `61.07%` | `0.64` | 59,440,000.00 USD |
| `15M` | `Bitget` | `48.75%` | `51.25%` | `0.95` | 27,740,000.00 USD |
| `15M` | `BingX` | `59.09%` | `40.91%` | `1.44` | 7,240,000.00 USD |
| `15M` | `MEXC` | `49.52%` | `50.48%` | `0.98` | 16,420,000.00 USD |
| `15M` | `Bitunix` | `62.35%` | `37.65%` | `1.66` | 22,920,000.00 USD |
| `15M` | `Hyperliquid` | `47.99%` | `52.01%` | `0.92` | 37,590,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `54.65%` | `45.35%` | `1.21` | 2,330,000.00 USD |
| `15M` | `Crypto.com` | `52.6%` | `47.4%` | `1.11` | 2,760,000.00 USD |
| `15M` | `WhiteBIT` | `99.4%` | `0.6%` | `165.67` | 520,350.00 USD |
| `15M` | `HTX` | `54.3%` | `45.7%` | `1.19` | 1,830,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `49.33%` | `50.67%` | `0.97` | 28,610,000.00 USD |
| `15M` | `Bitfinex` | `67.05%` | `32.95%` | `2.03` | 464,300.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `50.46%` | `49.54%` | `1.02` | 4,590,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `49.67%` | `50.33%` | `0.99` | 6,040,000.00 USD |
| `15M` | `Whale Positions` | `45.11%` | `54.89%` | `0.82` | 166,040,000.00 USD |
| `15M` | `Global Accounts` | `49.14%` | `50.86%` | `0.97` | 507,700,000.00 USD |
| `1H` | `ETH` | `49.06%` | `50.94%` | `0.96` | 2,000,000,000.00 USD |
| `1H` | `Binance` | `53.84%` | `46.16%` | `1.17` | 639,510,000.00 USD |
| `1H` | `OKX` | `52.95%` | `47.05%` | `1.13` | 348,170,000.00 USD |
| `1H` | `Bybit` | `54.64%` | `45.36%` | `1.20` | 135,960,000.00 USD |
| `1H` | `KuCoin` | `60.04%` | `39.96%` | `1.50` | 18,990,000.00 USD |
| `1H` | `Gate` | `51.62%` | `48.38%` | `1.07` | 302,270,000.00 USD |
| `1H` | `Bitget` | `50.87%` | `49.13%` | `1.04` | 78,830,000.00 USD |
| `1H` | `BingX` | `52.89%` | `47.11%` | `1.12` | 16,540,000.00 USD |
| `1H` | `MEXC` | `47.34%` | `52.66%` | `0.90` | 51,720,000.00 USD |
| `1H` | `Bitunix` | `54.49%` | `45.51%` | `1.20` | 68,610,000.00 USD |
| `1H` | `Hyperliquid` | `53.18%` | `46.82%` | `1.14` | 64,950,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.61%` | `46.39%` | `1.16` | 13,890,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `1.7%` | `98.3%` | `0.02` | 163,270,000.00 USD |
| `1H` | `HTX` | `69.4%` | `30.6%` | `2.27` | 29,470,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `43.83%` | `56.17%` | `0.78` | 19,940,000.00 USD |
| `1H` | `Bitfinex` | `31.47%` | `68.53%` | `0.46` | 1,470,000.00 USD |
| `1H` | `Kraken` | `72.66%` | `27.34%` | `2.66` | 1,000,000.00 USD |
| `1H` | `Aster` | `58.66%` | `41.34%` | `1.42` | 13,710,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `53.27%` | `46.73%` | `1.14` | 33,330,000.00 USD |
| `1H` | `Whale Positions` | `53.84%` | `46.16%` | `1.17` | 639,510,000.00 USD |
| `1H` | `Global Accounts` | `49.06%` | `50.94%` | `0.96` | 2,000,000,000.00 USD |
| `4H` | `ETH` | `49.08%` | `50.92%` | `0.96` | 18,970,000,000.00 USD |
| `4H` | `Binance` | `46.33%` | `53.67%` | `0.86` | 5,630,000,000.00 USD |
| `4H` | `OKX` | `46.77%` | `53.23%` | `0.88` | 3,330,000,000.00 USD |
| `4H` | `Bybit` | `48.99%` | `51.01%` | `0.96` | 1,270,000,000.00 USD |
| `4H` | `KuCoin` | `57.87%` | `42.13%` | `1.37` | 218,380,000.00 USD |
| `4H` | `Gate` | `47.8%` | `52.2%` | `0.92` | 1,830,000,000.00 USD |
| `4H` | `Bitget` | `49.49%` | `50.51%` | `0.98` | 715,500,000.00 USD |
| `4H` | `BingX` | `48.74%` | `51.26%` | `0.95` | 157,130,000.00 USD |
| `4H` | `MEXC` | `47.92%` | `52.08%` | `0.92` | 568,740,000.00 USD |
| `4H` | `Bitunix` | `49.67%` | `50.33%` | `0.99` | 630,530,000.00 USD |
| `4H` | `Hyperliquid` | `49.34%` | `50.66%` | `0.97` | 797,670,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `55.58%` | `44.42%` | `1.25` | 61,190,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `57.23%` | `42.77%` | `1.34` | 3,060,000,000.00 USD |
| `4H` | `HTX` | `51.06%` | `48.94%` | `1.04` | 149,930,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.08%` | `48.92%` | `1.04` | 123,150,000.00 USD |
| `4H` | `Bitfinex` | `25.71%` | `74.29%` | `0.35` | 12,550,000.00 USD |
| `4H` | `Kraken` | `39.3%` | `60.7%` | `0.65` | 60,220,000.00 USD |
| `4H` | `Aster` | `46.55%` | `53.45%` | `0.87` | 171,770,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `43.73%` | `56.27%` | `0.78` | 189,070,000.00 USD |
| `4H` | `Whale Positions` | `46.33%` | `53.67%` | `0.86` | 5,630,000,000.00 USD |
| `4H` | `Global Accounts` | `49.08%` | `50.92%` | `0.96` | 18,970,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `2214.25` | `2218.08` | `2214.25` | `2227.75` | `2210.25` | 141,329,048.77 USD | 65,222,449.86 USD | 76,106,598.91 USD | -10,884,149.05 USD | `-7.70%` | `2B / 1S` |
| `5:00 UTC` | `2205.25` | `2210.00` | `2205.25` | `2224.25` | `2202.75` | 274,097,559.83 USD | 122,676,431.99 USD | 151,421,127.83 USD | -28,744,695.84 USD | `-10.49%` | `1B / 6S` |
| `0:00 UTC` | `2180.25` | `2189.30` | `2180.25` | `2210.25` | `2172.75` | 713,753,253.85 USD | 330,298,360.51 USD | 383,454,893.33 USD | -53,156,532.82 USD | `-7.45%` | `1B / 5S` |
| `5:00 UTC` | `2192.25` | `2195.11` | `2192.25` | `2205.75` | `2188.75` | 213,150,561.59 USD | 86,554,765.83 USD | 126,595,795.76 USD | -40,041,029.93 USD | `-18.79%` | `1B / 5S` |
| `0:00 UTC` | `2190.25` | `2193.00` | `2190.25` | `2205.25` | `2181.25` | 206,705,717.00 USD | 113,660,029.38 USD | 93,045,687.62 USD | 20,614,341.75 USD | `+9.97%` | `2B / 2S` |
| `5:00 UTC` | `2214.75` | `2211.66` | `2214.75` | `2217.25` | `2204.25` | 218,308,818.86 USD | 130,467,599.52 USD | 87,841,219.34 USD | 42,626,380.18 USD | `+19.53%` | `6B / 1S` |
| `0:00 UTC` | `2217.25` | `2215.50` | `2217.25` | `2218.75` | `2209.75` | 102,137,358.80 USD | 50,758,296.06 USD | 51,379,062.74 USD | -620,766.68 USD | `-0.61%` | `0B / 3S` |
| `5:00 UTC` | `2208.25` | `2209.85` | `2208.25` | `2215.75` | `2207.25` | 69,365,754.50 USD | 25,046,876.87 USD | 44,318,877.64 USD | -19,272,000.77 USD | `-27.78%` | `0B / 4S` |
| `0:00 UTC` | `2215.25` | `2214.70` | `2215.25` | `2218.75` | `2208.25` | 100,318,327.91 USD | 51,517,721.13 USD | 48,800,606.78 USD | 2,717,114.35 USD | `+2.71%` | `2B / 2S` |
| `5:00 UTC` | `2210.75` | `2211.65` | `2210.75` | `2214.75` | `2210.25` | 27,077,749.29 USD | 16,340,466.45 USD | 10,737,282.84 USD | 5,603,183.61 USD | `+20.69%` | `2B / 0S` |

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
| `5m` | 846,480.00 USD | 8,470,000.00 USD | **`ACCUMULATION`** |
| `15m` | -1,100,000.00 USD | 7,870,000.00 USD | **`ACCUMULATION`** |
| `30m` | -2,710,000.00 USD | 20,560,000.00 USD | **`ACCUMULATION`** |
| `1h` | -3,960,000.00 USD | 15,600,000.00 USD | **`ACCUMULATION`** |
| `2h` | -29,850,000.00 USD | -207,050,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -63,790,000.00 USD | -670,050,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -73,790,000.00 USD | -740,460,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -167,890,000.00 USD | -1,910,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -161,280,000.00 USD | -2,190,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -137,540,000.00 USD | -2,010,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -203,030,000.00 USD | -3,230,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,170,000,000.00 USD | -9,770,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+846.48K` | 15m=`-1.10M` | 1h=`-3.96M` | 24h=`-137.54M`
* Futures Capital Netflows: 5m=`+8.47M` | 15m=`+7.87M` | 1h=`+15.60M` | 24h=`-2.01B`
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
  * `2026-10-30 08:33:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:00:58 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:48:58 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:49:58 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:49:58 IST`: [investinglive.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `2179.39` (Risk Distance: `27.56` pts)
  * +2.5R Take Profit: `2275.86`
  * Mathematical Lot Sizing: **`0.36 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2288.70` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2316.26` (Risk Distance: `27.56` pts)
  * +2.5R Take Profit: `2219.79`
  * Mathematical Lot Sizing: **`0.36 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2229.09`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
