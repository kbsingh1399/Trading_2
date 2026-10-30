# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 09:55:28 IST` (`2026-10-30 04:25:28 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2232.80` | **Live Ask Quote**: `2235.70` | **Mid Price**: `2234.25`
- **Spread Points**: `290.00` | **Spread BPS**: `12.98 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2234.25` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `5.59` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2249.89` | Lower -3.00σ Band: `2218.61`
  * Upper +2.51σ Band: `2246.54` | Lower -2.51σ Band: `2221.96`
  * Upper +2.01σ Band: `2243.63` | Lower -2.01σ Band: `2224.87`
  * Upper +2.00σ Band: `2243.19` | Lower -2.00σ Band: `2225.31`
  * Upper +1.28σ Band: `2240.51` | Lower -1.28σ Band: `2227.99`
  * Upper +1.00σ Band: `2238.72` | Lower -1.00σ Band: `2229.78`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2234.25` | EMA-20=`2234.25` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2234.25` (Slope: `+0.0000`) | EMA-100=`2234.25`
  * Institutional Anchors: EMA-144=`2234.25` | EMA-200=`2234.25` (Slope: `+0.0000`) | EMA-233=`2234.25`
- **Range Boundaries**: 24H High=`2256.59` | 24H Low=`2211.91` | Weekly High=`2278.93` | Weekly Low=`2189.57`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2280.60` (Distance: `-2.09%`)
  * Point of Control (POC) = `2264.42` (Distance: `-1.39%`)
  * Value Area Low (VAL) = `2206.95` (Distance: `+1.18%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2350.38` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2243.19` | Low=`2225.31`
  * New York Session (13:00-21:00 UTC): High=`2247.66` | Low=`2220.84`
  * Initial Balance (First Hour): IB High=`2240.95` | IB Low=`2227.55`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2225.31` - `2243.19`
  * Optimal Trade Entry (OTE 0.705): `2238.72`
  * Structural Invalidation Anchor (0.786): `2252.12`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2224.00` | `2231.45` | `2222.86` | `2229.01` | `34,491` | 76,816,733.47 USD | 11,297,559.05 USD | `+14.71%` | -997,630,994.20 USD | `+0.67` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `2229.01` | `2232.77` | `2228.16` | `2232.34` | `20,627` | 46,001,606.68 USD | -3,235.83 USD | `-0.01%` | -997,634,230.03 USD | `-0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `2232.33` | `2238.00` | `2230.12` | `2236.67` | `23,265` | 51,964,966.63 USD | 4,929,212.24 USD | `+9.49%` | -992,705,017.78 USD | `+0.15` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `2211.64` | `2221.32` | `2210.01` | `2220.90` | `36,553` | 81,002,689.38 USD | 13,736,922.17 USD | `+16.96%` | -1,015,815,574.10 USD | `+0.71` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `2220.91` | `2232.77` | `2219.65` | `2232.34` | `82,086` | 182,767,345.67 USD | 14,782,054.04 USD | `+8.09%` | -1,001,033,520.06 USD | `+0.69` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `2232.33` | `2238.00` | `2230.12` | `2237.22` | `24,472` | 54,665,284.79 USD | 7,008,586.02 USD | `+12.82%` | -994,024,934.04 USD | `+0.50` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2221.62` | `2227.62` | `2172.85` | `2194.70` | `610,884` | 1,342,330,424.04 USD | -132,826,407.64 USD | `-9.90%` | -1,075,617,565.11 USD | `-0.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2194.71` | `2218.96` | `2181.22` | `2209.27` | `270,460` | 596,517,649.16 USD | 43,347,954.49 USD | `+7.27%` | -1,032,269,610.63 USD | `+0.85` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2209.27` | `2238.00` | `2208.12` | `2236.67` | `187,202` | 416,053,329.58 USD | 36,165,302.81 USD | `+8.69%` | -996,104,307.82 USD | `+0.75` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -182,194,938.56 USD | `-1.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -736,432,507.87 USD | `-1.81` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.67` | `1,915,439` | 4,234,167,834.30 USD | -259,671,799.95 USD | `-6.13%` | -996,104,307.82 USD | `-0.45` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -84,078,993.86 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | 19,961,178.38 USD | `+1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -182,194,938.56 USD | `-1.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -736,432,507.87 USD | `-1.81` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.67` | `1,915,439` | 4,234,167,834.30 USD | -259,671,799.95 USD | `-6.13%` | -996,104,307.82 USD | `-0.45` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2234.25`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2235.30` | `385.7303` | 862,222.94 USD | 7,856,911.90 USD | `7 orders` | `-0.09%` | `-` |
| `BID` | `2235.40` | `172.0203` | 384,534.18 USD | 6,994,688.96 USD | `11 orders` | `-0.08%` | `-` |
| `BID` | `2235.50` | `83.1136` | 185,800.45 USD | 6,610,154.78 USD | `4 orders` | `-0.08%` | `-` |
| `BID` | `2235.60` | `153.0762` | 342,217.15 USD | 6,424,354.33 USD | `6 orders` | `-0.07%` | `-` |
| `BID` | `2235.70` | `99.0238` | 221,387.51 USD | 6,082,137.18 USD | `6 orders` | `-0.07%` | `-` |
| `BID` | `2235.80` | `155.7054` | 348,126.13 USD | 5,860,749.67 USD | `9 orders` | `-0.06%` | `-` |
| `BID` | `2235.90` | `306.2883` | 684,830.01 USD | 5,512,623.53 USD | `5 orders` | `-0.06%` | `-` |
| `BID` | `2236.00` | `141.6150` | 316,651.14 USD | 4,827,793.52 USD | `7 orders` | `-0.06%` | `-` |
| `BID` | `2236.10` | `167.0519` | 373,544.75 USD | 4,511,142.38 USD | `11 orders` | `-0.05%` | `-` |
| `BID` | `2236.20` | `159.4310` | 356,519.60 USD | 4,137,597.63 USD | `15 orders` | `-0.05%` | `-` |
| `BID` | `2236.30` | `181.4968` | 405,881.29 USD | 3,781,078.03 USD | `10 orders` | `-0.04%` | `-` |
| `BID` | `2236.40` | `157.4096` | 352,030.83 USD | 3,375,196.73 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `2236.50` | `442.4136` | 989,458.02 USD | 3,023,165.90 USD | `10 orders` | `-0.03%` | `-` |
| `BID` | `2236.60` | `255.4930` | 571,435.64 USD | 2,033,707.89 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `2236.70` | `212.4395` | 475,163.43 USD | 1,462,272.24 USD | `9 orders` | `-0.02%` | `-` |
| `BID` | `2236.80` | `80.3465` | 179,719.05 USD | 987,108.81 USD | `6 orders` | `-0.02%` | `-` |
| `BID` | `2236.90` | `78.2883` | 175,123.10 USD | 807,389.76 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `2237.00` | `7.3078` | 16,347.55 USD | 632,266.67 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `2237.10` | `77.7130` | 173,851.75 USD | 615,919.12 USD | `7 orders` | `-0.01%` | `-` |
| `BID` | `2237.20` | `197.5985` | 442,067.36 USD | 442,067.36 USD | `25 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2237.25` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,237.25` | `0.00%` | `-` |
| `ASK` | `2237.30` | `9.7026` | 21,707.63 USD | 21,707.63 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `2237.40` | `25.7250` | 57,557.12 USD | 79,264.74 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `2237.50` | `4.8612` | 10,876.94 USD | 90,141.68 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `2237.60` | `22.3215` | 49,946.59 USD | 140,088.27 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `2237.70` | `74.1995` | 166,036.22 USD | 306,124.49 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `2237.80` | `10.5994` | 23,719.34 USD | 329,843.82 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `2237.90` | `57.9929` | 129,782.31 USD | 459,626.13 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `2238.00` | `170.6105` | 381,826.30 USD | 841,452.43 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `2238.10` | `60.6297` | 135,695.33 USD | 977,147.77 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `2238.20` | `202.8507` | 454,020.44 USD | 1,431,168.20 USD | `11 orders` | `+0.04%` | `-` |
| `ASK` | `2238.30` | `106.9150` | 239,307.84 USD | 1,670,476.05 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `2238.40` | `259.9410` | 581,851.93 USD | 2,252,327.98 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `2238.50` | `77.0383` | 172,450.23 USD | 2,424,778.22 USD | `8 orders` | `+0.06%` | `-` |
| `ASK` | `2238.60` | `174.0273` | 389,577.51 USD | 2,814,355.73 USD | `8 orders` | `+0.06%` | `-` |
| `ASK` | `2238.70` | `55.9901` | 125,345.04 USD | 2,939,700.77 USD | `5 orders` | `+0.06%` | `-` |
| `ASK` | `2238.80` | `140.4035` | 314,335.36 USD | 3,254,036.12 USD | `6 orders` | `+0.07%` | `-` |
| `ASK` | `2238.90` | `456.4909` | 1,022,037.48 USD | 4,276,073.60 USD | `8 orders` | `+0.07%` | `-` |
| `ASK` | `2239.00` | `175.8993` | 393,838.53 USD | 4,669,912.13 USD | `10 orders` | `+0.08%` | `-` |
| `ASK` | `2239.10` | `303.9069` | 680,477.94 USD | 5,350,390.07 USD | `10 orders` | `+0.08%` | `-` |
| `ASK` | `2239.20` | `170.0298` | 380,730.73 USD | 5,731,120.80 USD | `9 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:47:56 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1844.27` | `7,964.66` | 14,688,972.62 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 09:47:56 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 09:47:56 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1913.52` | `6,500.22` | 12,438,334.12 USD | `AT_RISK_LIQ` | `0xf78c5d8d4b` | `2026-10-30 09:47:56 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `10,000.00` | 19,261,000.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 09:47:56 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1928.81` | `8,092.45` | 15,608,770.69 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 09:47:56 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2122.22` | `30,641.99` | 65,028,977.30 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 09:47:56 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.50` | `26,025.05` | 55,420,231.63 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 09:47:56 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,000.00` | 6,525,000.00 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2199.40` | `498.98` | 1,097,458.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2200.90` | `4,722.42` | 10,393,577.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.00` | `239.72` | 527,621.08 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9362ca4dfd` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2206.80` | `244.00` | 538,459.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x24fb652303` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2207.40` | `266.00` | 587,168.40 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x24fb652303` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2213.30` | `359.07` | 794,719.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2213.30` | `344.25` | 761,925.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2215.90` | `498.78` | 1,105,255.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2216.50` | `2,434.39` | 5,395,821.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2220.70` | `499.01` | 1,108,144.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2223.30` | `1,802.88` | 4,008,350.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2224.10` | `466.53` | 1,037,611.60 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2225.00` | `1,351.16` | 3,006,323.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2225.90` | `354.92` | 790,009.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.50` | `1,240.74` | 2,762,514.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2229.20` | `899.08` | 2,004,219.33 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2230.20` | `673.99` | 1,503,133.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2230.90` | `247.87` | 552,968.72 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2232.50` | `223.60` | 499,178.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2577367690` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2232.60` | `448.77` | 1,001,915.64 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2233.40` | `353.52` | 789,547.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.00` | `336.43` | 751,575.91 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.10` | `223.60` | 499,538.06 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2577367690` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.80` | `246.62` | 551,146.15 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2237.30` | `201.57` | 450,963.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2237.50` | `246.33` | 551,174.34 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2238.10` | `223.40` | 499,999.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2577367690` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2238.50` | `335.75` | 751,578.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2239.00` | `447.58` | 1,002,122.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2239.80` | `349.06` | 781,819.88 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2239.80` | `223.23` | 499,999.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2577367690` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2240.10` | `252.16` | 564,852.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2240.50` | `670.89` | 1,503,140.25 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2243.30` | `893.42` | 2,004,219.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.30` | `473.98` | 1,063,746.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.30` | `348.25` | 781,575.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.40` | `1,339.49` | 3,006,346.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.60` | `1,240.74` | 2,784,971.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.70` | `392.01` | 879,948.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x6798a1b850` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2246.60` | `1,784.22` | 4,008,420.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2247.50` | `507.05` | 1,139,594.88 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2249.60` | `2,434.39` | 5,476,399.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2250.30` | `507.62` | 1,142,306.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2257.10` | `352.10` | 794,719.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2259.60` | `337.19` | 761,925.60 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2262.90` | `4,722.42` | 10,686,367.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2266.50` | `507.32` | 1,149,836.25 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.70` | `620.97` | 1,409,408.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.20` | `2,200.51` | 4,999,999.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb1ec7febea` | `2026-10-30 09:47:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2278.00` | `240.63` | 548,166.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x81cb8a0a3b` | `2026-10-30 09:47:56 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2300.00` | `4,002.10` | 9,204,832.99 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 09:47:56 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2463.82` | `22,046.99` | 54,319,767.92 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 09:47:56 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `2,733.67` | 6,872,176.53 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 09:47:56 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2624.22` | `10,000.00` | 26,242,230.56 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 09:47:56 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.08` | `9,700.00` | 25,783,366.12 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 09:47:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 238,482,090.80 USD | `106,417.71` | `2322.74` | `2240.38` | `3782.48` | 8,698,921.35 USD | `+3.65%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 144,955,737.93 USD | `64,680.62` | `2375.30` | `2240.38` | `4323.93` | 8,680,559.57 USD | `+5.99%` | `5X Cross` |
| `10` | `0x77dd...e0e9` | `LONG` | 68,687,088.59 USD | `30,641.99` | `2610.31` | `2240.38` | `2122.13` | -11,298,086.44 USD | `-16.45%` | `10X Cross` |
| `11` | `0xde8d...9524` | `LONG` | 67,890,120.41 USD | `30,282.40` | `2134.45` | `2240.38` | `1786.39` | 3,253,789.83 USD | `+4.79%` | `20X Cross` |
| `17` | `0x0392...d7d9` | `LONG` | 58,348,164.57 USD | `26,025.05` | `2518.71` | `2240.38` | `2129.41` | -7,201,557.52 USD | `-12.34%` | `9X Cross` |
| `23` | `0x8add...7d2c` | `SHORT` | 49,266,201.17 USD | `22,046.99` | `2271.09` | `2240.38` | `2464.17` | 804,696.13 USD | `+1.63%` | `25X Cross` |
| `27` | `0xdf95...7d72` | `SHORT` | 44,790,024.47 USD | `19,981.27` | `2402.53` | `2240.38` | `4186.68` | 3,215,677.71 USD | `+7.18%` | `25X Cross` |
| `35` | `0xeced...6210` | `SHORT` | 37,358,477.06 USD | `16,687.58` | `2522.09` | `2240.38` | `3476.53` | 4,729,237.93 USD | `+12.66%` | `20X Cross` |
| `36` | `0xb695...a92d` | `SHORT` | 36,346,567.56 USD | `16,214.56` | `2557.74` | `2240.38` | `3914.55` | 5,126,161.27 USD | `+14.10%` | `20X Cross` |
| `37` | `0x6046...b21d` | `LONG` | 35,708,063.35 USD | `15,927.59` | `2410.19` | `2240.38` | `1756.68` | -2,680,556.30 USD | `-7.51%` | `6X Cross` |
| `41` | `0x45d2...4029` | `SHORT` | 31,270,320.00 USD | `13,950.00` | `2443.60` | `2240.38` | `5288.50` | 2,817,962.46 USD | `+9.01%` | `20X Cross` |
| `44` | `0xa61c...66b9` | `LONG` | 28,885,874.40 USD | `12,888.00` | `2369.69` | `2240.38` | `1430.05` | -1,654,780.14 USD | `-5.73%` | `10X Cross` |
| `47` | `0x2371...0883` | `LONG` | 26,893,200.00 USD | `12,000.00` | `2421.77` | `2240.38` | `1279.37` | -2,168,094.85 USD | `-8.06%` | `20X Cross` |
| `48` | `0xbd1c...ff0e` | `LONG` | 26,858,400.00 USD | `12,000.00` | `2419.91` | `2240.38` | `1520.27` | -2,180,632.39 USD | `-8.12%` | `20X Cross` |
| `55` | `0xa9de...e049` | `LONG` | 24,660,900.00 USD | `11,000.00` | `2481.81` | `2240.38` | `1644.01` | -2,639,079.46 USD | `-10.70%` | `20X Cross` |
| `56` | `0x0c5d...36b3` | `LONG` | 24,660,900.00 USD | `11,000.00` | `2482.20` | `2240.38` | `1644.34` | -2,643,353.24 USD | `-10.72%` | `20X Cross` |
| `57` | `0x6c93...59a4` | `LONG` | 24,657,600.00 USD | `11,000.00` | `2441.15` | `2240.38` | `1602.30` | -2,195,072.73 USD | `-8.90%` | `20X Cross` |
| `58` | `0x09dc...c094` | `LONG` | 24,646,600.00 USD | `11,000.00` | `2465.31` | `2240.38` | `1637.34` | -2,471,823.04 USD | `-10.03%` | `20X Cross` |
| `70` | `0x15a4...dfdb` | `LONG` | 22,419,000.00 USD | `10,000.00` | `1761.94` | `2240.38` | `269.18` | 4,799,518.97 USD | `+21.41%` | `20X Cross` |
| `71` | `0xb37f...66ca` | `SHORT` | 22,416,000.00 USD | `10,000.00` | `2290.69` | `2240.38` | `2624.14` | 490,991.85 USD | `+2.19%` | `25X Cross` |
| `72` | `0xec7f...df39` | `LONG` | 22,406,000.00 USD | `10,000.00` | `2719.35` | `2240.38` | `1720.86` | -4,787,548.52 USD | `-21.37%` | `20X Cross` |
| `73` | `0x6646...6de5` | `LONG` | 22,404,000.00 USD | `10,000.00` | `1765.80` | `2240.38` | `1726.42` | 4,745,942.55 USD | `+21.18%` | `25X Cross` |
| `74` | `0xa2ce...3126` | `LONG` | 22,377,699.20 USD | `10,016.88` | `2162.83` | `2240.38` | `1542.53` | 712,897.15 USD | `+3.19%` | `10X Cross` |
| `76` | `0x939f...04d2` | `LONG` | 22,021,059.00 USD | `9,823.81` | `2427.28` | `2240.38` | `1772.93` | -1,824,091.61 USD | `-8.28%` | `25X Cross` |
| `78` | `0xaeaa...2416` | `SHORT` | 21,738,670.00 USD | `9,700.00` | `2311.92` | `2240.38` | `2658.00` | 687,012.40 USD | `+3.16%` | `25X Cross` |
| `84` | `0xf517...c032` | `SHORT` | 20,893,815.41 USD | `9,326.35` | `2202.91` | `2240.38` | `3149.48` | -348,677.20 USD | `-1.67%` | `25X Cross` |
| `85` | `0xca49...53c8` | `SHORT` | 20,619,180.15 USD | `9,200.88` | `2549.39` | `2240.38` | `3865.81` | 2,837,527.38 USD | `+13.76%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 20,269,463.15 USD | `9,054.12` | `2493.89` | `2240.38` | `2918.67` | 2,310,544.11 USD | `+11.40%` | `20X Cross` |
| `88` | `0xea00...a918` | `LONG` | 20,186,578.56 USD | `9,003.83` | `2003.01` | `2240.38` | `1351.17` | 2,151,799.70 USD | `+10.66%` | `5X Cross` |
| `92` | `0xefe4...194b` | `SHORT` | 19,766,905.66 USD | `8,820.57` | `2267.42` | `2240.38` | `3606.46` | 233,108.73 USD | `+1.18%` | `20X Cross` |
| `114` | `0x9eec...daab` | `LONG` | 18,140,040.63 USD | `8,092.45` | `1658.44` | `2240.38` | `1927.92` | 4,719,176.10 USD | `+26.02%` | `15X Cross` |
| `115` | `0x5f91...65aa` | `LONG` | 17,855,962.06 USD | `7,964.66` | `1626.99` | `2240.38` | `1844.18` | 4,897,519.00 USD | `+27.43%` | `16X Cross` |
| `123` | `0xecb6...2b00` | `SHORT` | 15,848,569.73 USD | `7,070.20` | `2242.32` | `2240.38` | `6161.68` | 5,142.04 USD | `+0.03%` | `15X Cross` |
| `127` | `0xec0b...b078` | `LONG` | 15,695,367.20 USD | `7,007.80` | `2065.97` | `2240.38` | `1060.63` | 1,217,437.61 USD | `+7.76%` | `25X Cross` |
| `131` | `0xf02d...5eb3` | `LONG` | 15,368,377.10 USD | `6,855.99` | `2383.33` | `2240.38` | `1122.95` | -971,711.67 USD | `-6.32%` | `20X Cross` |
| `132` | `0xcf53...ee11` | `SHORT` | 15,243,528.31 USD | `6,803.63` | `1862.69` | `2240.38` | `4228.02` | -2,570,422.92 USD | `-16.86%` | `7X Cross` |
| `133` | `0x418a...8888` | `SHORT` | 15,066,652.10 USD | `6,724.38` | `2494.55` | `2240.38` | `3010.49` | 1,707,671.07 USD | `+11.33%` | `25X Cross` |
| `139` | `0x4ff9...38d3` | `LONG` | 14,667,478.55 USD | `6,564.10` | `2447.40` | `2240.38` | `1669.96` | -1,397,544.20 USD | `-9.53%` | `3X Isolated` |
| `140` | `0xf78c...c581` | `LONG` | 14,573,496.60 USD | `6,500.22` | `2521.53` | `2240.38` | `1913.44` | -1,817,044.34 USD | `-12.47%` | `20X Cross` |
| `141` | `0x1ee7...edf5` | `LONG` | 14,530,750.00 USD | `6,500.00` | `2301.55` | `2240.38` | `2069.17` | -429,343.66 USD | `-2.95%` | `25X Cross` |
| `144` | `0x799f...5f4c` | `LONG` | 14,147,151.93 USD | `6,310.90` | `2390.33` | `2240.38` | `1835.03` | -938,012.69 USD | `-6.63%` | `20X Cross` |
| `147` | `0x08bf...7872` | `SHORT` | 13,951,824.65 USD | `6,224.05` | `2258.00` | `2240.38` | `2585.23` | 102,091.46 USD | `+0.73%` | `20X Cross` |
| `153` | `0xd9e7...4aff` | `LONG` | 13,451,400.00 USD | `6,000.00` | `2480.18` | `2240.38` | `1407.73` | -1,429,724.33 USD | `-10.63%` | `20X Cross` |
| `162` | `0x0c4a...1b19` | `LONG` | 12,647,487.86 USD | `5,660.10` | `2373.06` | `2240.38` | `2081.78` | -784,270.27 USD | `-6.20%` | `25X Isolated` |
| `165` | `0xc179...e0c8` | `LONG` | 12,152,617.78 USD | `5,420.68` | `2306.49` | `2240.38` | `980.76` | -350,123.24 USD | `-2.88%` | `10X Cross` |
| `169` | `0x7fda...17d1` | `LONG` | 11,915,804.48 USD | `5,315.76` | `2211.05` | `2240.38` | `0.000000` | 162,362.23 USD | `+1.36%` | `25X Cross` |
| `177` | `0x218a...7da2` | `SHORT` | 11,709,148.22 USD | `5,222.87` | `2208.16` | `2240.38` | `2792.88` | -176,213.16 USD | `-1.50%` | `10X Cross` |
| `186` | `0x45ab...6cbc` | `LONG` | 11,032,305.16 USD | `4,920.96` | `2727.66` | `2240.38` | `1381.96` | -2,390,438.64 USD | `-21.67%` | `7X Cross` |
| `192` | `0x64b7...9da9` | `LONG` | 10,887,576.43 USD | `4,856.84` | `2604.61` | `2240.38` | `601.35` | -1,762,637.98 USD | `-16.19%` | `25X Cross` |
| `198` | `0xfb18...eb17` | `SHORT` | 10,685,498.33 USD | `4,768.18` | `2315.53` | `2240.38` | `2588.80` | 355,383.47 USD | `+3.33%` | `25X Cross` |
| `200` | `0x5559...d43b` | `SHORT` | 10,662,308.93 USD | `4,755.93` | `2262.69` | `2240.38` | `2779.46` | 98,896.95 USD | `+0.93%` | `25X Cross` |
| `211` | `0xe091...6705` | `SHORT` | 10,088,550.45 USD | `4,500.00` | `2467.33` | `2240.38` | `2463.35` | 1,014,458.06 USD | `+10.06%` | `20X Cross` |
| `220` | `0xb829...3a81` | `LONG` | 9,851,632.50 USD | `4,394.91` | `2398.60` | `2240.38` | `1469.71` | -690,009.45 USD | `-7.00%` | `20X Cross` |
| `237` | `0x28bb...fca6` | `SHORT` | 9,435,008.31 USD | `4,209.61` | `1896.10` | `2240.38` | `3036.50` | -1,453,125.74 USD | `-15.40%` | `20X Cross` |
| `239` | `0x6ea4...0ea7` | `SHORT` | 9,366,748.34 USD | `4,184.01` | `2602.13` | `2240.38` | `3425.29` | 1,520,598.33 USD | `+16.23%` | `20X Cross` |
| `250` | `0xfb94...0ddf` | `SHORT` | 8,972,310.90 USD | `4,002.10` | `2382.44` | `2240.38` | `5104.68` | 562,473.25 USD | `+6.27%` | `20X Cross` |
| `252` | `0x5e9e...35ee` | `SHORT` | 8,972,115.70 USD | `4,007.56` | `1796.39` | `2240.38` | `2585.78` | -1,772,965.61 USD | `-19.76%` | `20X Cross` |
| `253` | `0x3dc9...54b0` | `SHORT` | 8,967,305.43 USD | `3,999.69` | `2480.32` | `2240.38` | `6518.60` | 953,231.12 USD | `+10.63%` | `20X Cross` |
| `254` | `0x8cc9...2b6a` | `SHORT` | 8,966,400.00 USD | `4,000.00` | `1791.18` | `2240.38` | `3560.22` | -1,801,653.33 USD | `-20.09%` | `25X Cross` |
| `273` | `0x4b67...f4e7` | `LONG` | 8,565,945.46 USD | `3,820.84` | `2591.51` | `2240.38` | `1341.02` | -1,335,828.09 USD | `-15.59%` | `20X Cross` |
| `276` | `0x12d2...f97f` | `LONG` | 8,421,149.53 USD | `3,757.26` | `2446.50` | `2240.38` | `1776.59` | -771,016.86 USD | `-9.16%` | `20X Cross` |
| `286` | `0x0622...8088` | `LONG` | 8,196,792.41 USD | `3,658.63` | `2206.77` | `2240.38` | `0.000000` | 123,007.15 USD | `+1.50%` | `5X Cross` |
| `297` | `0x8ae4...3d60` | `LONG` | 7,965,738.53 USD | `3,558.20` | `2482.21` | `2240.38` | `501.69` | -866,459.50 USD | `-10.88%` | `10X Cross` |
| `337` | `0x4a20...3c26` | `LONG` | 6,724,800.00 USD | `3,000.00` | `2428.72` | `2240.38` | `551.47` | -561,360.28 USD | `-8.35%` | `20X Cross` |
| `338` | `0x007d...67a0` | `LONG` | 6,723,000.00 USD | `3,000.00` | `2400.00` | `2240.38` | `1472.03` | -477,000.00 USD | `-7.10%` | `25X Cross` |
| `340` | `0x469e...58a5` | `SHORT` | 6,704,100.00 USD | `3,000.00` | `2195.70` | `2240.38` | `3221.97` | -116,992.76 USD | `-1.75%` | `25X Cross` |
| `341` | `0xb823...9763` | `SHORT` | 6,703,200.00 USD | `3,000.00` | `2229.66` | `2240.38` | `3233.68` | -14,203.32 USD | `-0.21%` | `25X Cross` |
| `363` | `0x9c2a...f6a8` | `SHORT` | 6,330,084.77 USD | `2,823.41` | `2533.78` | `2240.38` | `2628.80` | 823,826.05 USD | `+13.01%` | `20X Cross` |
| `390` | `0x8328...f54a` | `SHORT` | 5,776,145.72 USD | `2,576.45` | `2292.01` | `2240.38` | `3279.52` | 129,125.57 USD | `+2.24%` | `25X Cross` |
| `392` | `0xed48...7c9b` | `SHORT` | 5,718,614.13 USD | `2,551.13` | `2460.02` | `2240.38` | `3244.26` | 557,232.28 USD | `+9.74%` | `20X Cross` |
| `396` | `0x1c98...7fc7` | `LONG` | 5,596,760.07 USD | `2,500.00` | `2452.60` | `2240.38` | `1916.93` | -534,761.49 USD | `-9.55%` | `10X Cross` |
| `398` | `0x970c...2a93` | `SHORT` | 5,591,500.00 USD | `2,500.00` | `2229.57` | `2240.38` | `5061.27` | -17,555.51 USD | `-0.31%` | `20X Cross` |
| `409` | `0xa445...329d` | `LONG` | 5,393,594.01 USD | `2,406.14` | `2354.86` | `2240.38` | `1706.82` | -272,521.27 USD | `-5.05%` | `25X Cross` |
| `412` | `0xfbe2...c8ea` | `SHORT` | 5,346,677.77 USD | `2,385.21` | `2041.57` | `2240.38` | `2623.16` | -477,111.11 USD | `-8.92%` | `20X Cross` |
| `414` | `0x6749...ce07` | `SHORT` | 5,345,978.84 USD | `2,384.89` | `2220.92` | `2240.38` | `3630.52` | -49,315.81 USD | `-0.92%` | `20X Cross` |
| `416` | `0x645b...87b8` | `SHORT` | 5,334,953.30 USD | `2,379.98` | `2421.64` | `2240.38` | `11310.62` | 428,493.65 USD | `+8.03%` | `10X Cross` |
| `427` | `0x77ee...2902` | `SHORT` | 5,118,549.49 USD | `2,290.69` | `2476.53` | `2240.38` | `5875.42` | 554,422.75 USD | `+10.83%` | `25X Cross` |
| `432` | `0xbcd4...0dd2` | `SHORT` | 5,073,634.58 USD | `2,263.50` | `2233.24` | `2240.38` | `2693.88` | -18,677.01 USD | `-0.37%` | `25X Cross` |
| `452` | `0xd507...c948` | `SHORT` | 4,864,628.18 USD | `2,172.00` | `2387.49` | `2240.38` | `2600.53` | 321,012.85 USD | `+6.60%` | `5X Isolated` |
| `459` | `0x382b...3e39` | `SHORT` | 4,773,580.45 USD | `2,129.54` | `2296.66` | `2240.38` | `4657.62` | 117,256.76 USD | `+2.46%` | `25X Cross` |
| `461` | `0x023a...2355` | `LONG` | 4,759,486.17 USD | `2,123.54` | `2330.15` | `2240.38` | `0.000000` | -188,687.65 USD | `-3.96%` | `25X Cross` |
| `495` | `0x3453...b323` | `SHORT` | 4,484,275.99 USD | `2,000.12` | `2322.47` | `2240.38` | `2382.30` | 160,959.85 USD | `+3.59%` | `25X Cross` |
| `496` | `0x7a6d...f79c` | `SHORT` | 4,483,800.00 USD | `2,000.00` | `2418.41` | `2240.38` | `2512.70` | 353,032.11 USD | `+7.87%` | `25X Cross` |
| `497` | `0xe02e...d78b` | `LONG` | 4,483,200.00 USD | `2,000.00` | `2228.11` | `2240.38` | `2171.88` | 26,976.53 USD | `+0.60%` | `25X Cross` |
| `504` | `0xf3dc...1672` | `SHORT` | 4,435,415.20 USD | `1,980.36` | `2240.44` | `2240.38` | `2776.80` | 1,472.35 USD | `+0.03%` | `20X Cross` |
| `508` | `0xac48...3201` | `SHORT` | 4,395,276.76 USD | `1,964.37` | `2272.04` | `2240.38` | `3140.55` | 67,865.54 USD | `+1.54%` | `20X Cross` |
| `518` | `0x8376...9a1e` | `SHORT` | 4,283,140.98 USD | `1,910.50` | `2477.72` | `2240.38` | `3180.64` | 450,547.19 USD | `+10.52%` | `20X Cross` |
| `552` | `0x7265...91a5` | `LONG` | 4,039,611.01 USD | `1,801.87` | `2533.96` | `2240.38` | `1987.40` | -526,255.45 USD | `-13.03%` | `20X Cross` |
| `553` | `0x739c...cfb2` | `SHORT` | 4,035,600.00 USD | `1,800.00` | `2427.60` | `2240.38` | `2507.33` | 334,096.38 USD | `+8.28%` | `25X Cross` |
| `567` | `0x91a9...3f70` | `SHORT` | 3,961,806.42 USD | `1,767.48` | `2156.23` | `2240.38` | `3656.80` | -150,702.34 USD | `-3.80%` | `4X Cross` |
| `573` | `0xbb34...1696` | `LONG` | 3,923,325.00 USD | `1,750.00` | `2315.81` | `2240.38` | `1945.21` | -129,343.23 USD | `-3.30%` | `25X Cross` |
| `574` | `0xc619...10f5` | `LONG` | 3,921,750.00 USD | `1,750.00` | `2315.39` | `2240.38` | `1773.95` | -130,195.83 USD | `-3.32%` | `25X Cross` |
| `595` | `0xfeec...4e9c` | `SHORT` | 3,792,527.79 USD | `1,691.81` | `2566.49` | `2240.38` | `2509.16` | 549,496.73 USD | `+14.49%` | `10X Cross` |
| `613` | `0xeee0...0b53` | `LONG` | 3,670,268.07 USD | `1,637.12` | `2468.64` | `2240.38` | `195.09` | -371,207.99 USD | `-10.11%` | `7X Cross` |
| `619` | `0x982b...4606` | `LONG` | 3,647,161.70 USD | `1,626.82` | `2575.24` | `2240.38` | `1547.68` | -542,291.37 USD | `-14.87%` | `5X Isolated` |
| `620` | `0x27b8...12fc` | `LONG` | 3,644,384.03 USD | `1,628.12` | `2468.73` | `2240.38` | `603.04` | -375,010.60 USD | `-10.29%` | `10X Cross` |
| `627` | `0x73d7...8be1` | `LONG` | 3,588,243.60 USD | `1,601.47` | `2410.40` | `2240.38` | `1761.38` | -271,935.32 USD | `-7.58%` | `25X Cross` |
| `630` | `0xad54...6203` | `LONG` | 3,572,860.47 USD | `1,597.45` | `2591.98` | `2240.38` | `2052.04` | -567,717.57 USD | `-15.89%` | `10X Isolated` |
| `634` | `0x880a...311c` | `LONG` | 3,536,562.37 USD | `1,578.40` | `2209.72` | `2240.38` | `0.000000` | 48,738.52 USD | `+1.38%` | `9X Cross` |
| `653` | `0xe170...9300` | `SHORT` | 3,436,349.40 USD | `1,533.40` | `2076.39` | `2240.38` | `3152.21` | -252,399.90 USD | `-7.35%` | `25X Cross` |
| `659` | `0x4b86...df9d` | `SHORT` | 3,409,950.00 USD | `1,524.00` | `2287.40` | `2240.38` | `2759.88` | 76,047.60 USD | `+2.23%` | `9X Isolated` |
| `663` | `0x2e2b...2fab` | `LONG` | 3,379,539.23 USD | `1,507.38` | `2245.53` | `2240.38` | `1214.32` | -5,333.87 USD | `-0.16%` | `25X Cross` |
| `666` | `0xf929...d1f9` | `SHORT` | 3,362,850.00 USD | `1,500.00` | `2423.37` | `2240.38` | `2677.92` | 272,205.26 USD | `+8.09%` | `25X Cross` |
| `667` | `0x251f...6e5d` | `LONG` | 3,360,450.00 USD | `1,500.00` | `2346.68` | `2240.38` | `1855.30` | -159,580.49 USD | `-4.75%` | `20X Cross` |
| `668` | `0xde6b...3361` | `LONG` | 3,358,050.00 USD | `1,500.00` | `2216.98` | `2240.38` | `2168.81` | 32,569.26 USD | `+0.97%` | `25X Cross` |
| `689` | `0xb885...3c54` | `LONG` | 3,248,874.93 USD | `1,450.00` | `2274.34` | `2240.38` | `32.53` | -48,933.21 USD | `-1.51%` | `20X Cross` |
| `690` | `0x3440...32c5` | `SHORT` | 3,248,166.36 USD | `1,448.97` | `2198.21` | `2240.38` | `3804.40` | -63,015.40 USD | `-1.94%` | `25X Cross` |
| `694` | `0xef70...a84c` | `SHORT` | 3,233,620.78 USD | `1,442.74` | `2424.73` | `2240.38` | `3263.95` | 264,650.04 USD | `+8.18%` | `25X Cross` |
| `700` | `0x4b5f...0dd8` | `LONG` | 3,209,731.17 USD | `1,431.96` | `2339.45` | `2240.38` | `2147.97` | -140,261.78 USD | `-4.37%` | `10X Cross` |
| `701` | `0xd911...961e` | `LONG` | 3,209,456.69 USD | `1,431.71` | `2210.48` | `2240.38` | `641.95` | 44,687.91 USD | `+1.39%` | `25X Cross` |
| `704` | `0xbadb...9ee6` | `LONG` | 3,201,791.90 USD | `1,428.16` | `1936.00` | `2240.38` | `1063.75` | 436,870.26 USD | `+13.64%` | `20X Cross` |
| `757` | `0x53f8...ceff` | `LONG` | 3,023,682.94 USD | `1,348.65` | `2276.73` | `2240.38` | `0.000000` | -46,841.53 USD | `-1.55%` | `20X Cross` |
| `777` | `0x0dd5...f6ee` | `LONG` | 2,946,915.00 USD | `1,315.00` | `2306.05` | `2240.38` | `1560.29` | -85,549.38 USD | `-2.90%` | `5X Cross` |
| `802` | `0x1f16...6d07` | `LONG` | 2,837,865.60 USD | `1,266.00` | `2261.43` | `2240.38` | `1379.09` | -25,105.63 USD | `-0.88%` | `7X Cross` |
| `813` | `0xc435...c905` | `SHORT` | 2,797,891.20 USD | `1,248.00` | `2704.38` | `2240.38` | `4236.25` | 577,179.15 USD | `+20.63%` | `20X Cross` |
| `820` | `0x6859...7e1e` | `SHORT` | 2,773,327.67 USD | `1,237.15` | `2200.39` | `2240.38` | `4675.62` | -51,100.52 USD | `-1.84%` | `25X Cross` |
| `830` | `0x7277...0b98` | `SHORT` | 2,733,527.86 USD | `1,219.45` | `2206.05` | `2240.38` | `3353.12` | -43,340.06 USD | `-1.59%` | `20X Cross` |
| `835` | `0x7178...0854` | `LONG` | 2,725,591.21 USD | `1,218.63` | `2461.81` | `2240.38` | `1169.47` | -274,455.19 USD | `-10.07%` | `10X Cross` |
| `846` | `0xaaa1...ab8c` | `SHORT` | 2,690,280.00 USD | `1,200.00` | `2276.29` | `2240.38` | `2365.50` | 41,277.58 USD | `+1.53%` | `25X Isolated` |
| `858` | `0x07fd...689d` | `LONG` | 2,659,703.15 USD | `1,186.89` | `2416.34` | `2240.38` | `0.000000` | -208,239.21 USD | `-7.83%` | `25X Cross` |
| `862` | `0xb8eb...1dd5` | `LONG` | 2,646,716.43 USD | `1,181.73` | `2226.79` | `2240.38` | `601.11` | 15,251.68 USD | `+0.58%` | `25X Cross` |
| `872` | `0xa70a...4be9` | `LONG` | 2,605,817.41 USD | `1,162.48` | `2259.47` | `2240.38` | `1016.36` | -20,779.48 USD | `-0.80%` | `20X Cross` |
| `873` | `0x0a97...347d` | `LONG` | 2,605,052.89 USD | `1,162.09` | `2267.88` | `2240.38` | `1531.94` | -30,425.89 USD | `-1.17%` | `20X Cross` |
| `877` | `0x6e6f...82a6` | `LONG` | 2,594,629.94 USD | `1,157.75` | `2266.47` | `2240.38` | `1394.07` | -29,377.63 USD | `-1.13%` | `20X Cross` |
| `925` | `0x2f80...f203` | `SHORT` | 2,437,485.76 USD | `1,088.94` | `1984.00` | `2240.38` | `2962.95` | -277,018.57 USD | `-11.36%` | `20X Cross` |
| `931` | `0x6f11...0389` | `SHORT` | 2,418,146.90 USD | `1,079.00` | `2333.39` | `2240.38` | `3198.98` | 99,582.01 USD | `+4.12%` | `25X Cross` |
| `932` | `0x8eb7...b90f` | `LONG` | 2,416,183.51 USD | `1,077.74` | `2396.38` | `2240.38` | `1881.22` | -166,494.53 USD | `-6.89%` | `5X Isolated` |
| `934` | `0x2b61...2f6c` | `SHORT` | 2,405,656.44 USD | `1,076.60` | `2681.75` | `2240.38` | `6429.62` | 481,516.30 USD | `+20.02%` | `10X Cross` |
| `958` | `0x30af...393e` | `SHORT` | 2,333,354.66 USD | `1,041.16` | `2252.26` | `2240.38` | `2297.19` | 11,627.67 USD | `+0.50%` | `25X Cross` |
| `971` | `0x1b2a...f7a6` | `LONG` | 2,298,772.52 USD | `1,025.37` | `2737.51` | `2240.38` | `882.35` | -508,187.42 USD | `-22.11%` | `10X Cross` |
| `978` | `0x001a...fef6` | `SHORT` | 2,256,206.54 USD | `1,007.33` | `2022.19` | `2240.38` | `3078.45` | -219,198.58 USD | `-9.72%` | `10X Cross` |
| `979` | `0x02aa...1806` | `SHORT` | 2,256,206.35 USD | `1,007.10` | `2654.68` | `2240.38` | `3612.98` | 417,325.75 USD | `+18.50%` | `20X Cross` |
| `982` | `0xb15b...dbae` | `SHORT` | 2,250,255.11 USD | `1,004.13` | `2290.80` | `2240.38` | `2247.27` | 50,006.35 USD | `+2.22%` | `25X Cross` |
| `984` | `0xdb3a...cf3b` | `LONG` | 2,248,506.00 USD | `1,003.22` | `2705.01` | `2240.38` | `0.000000` | -465,200.89 USD | `-20.69%` | `4X Cross` |
| `989` | `0x8c02...b73f` | `SHORT` | 2,242,000.00 USD | `1,000.00` | `2250.37` | `2240.38` | `8098.66` | 8,371.47 USD | `+0.37%` | `20X Cross` |
| `990` | `0x834c...dd93` | `SHORT` | 2,241,900.00 USD | `1,000.00` | `2191.89` | `2240.38` | `2262.27` | -50,007.36 USD | `-2.23%` | `25X Cross` |
| `991` | `0x5272...fcd9` | `SHORT` | 2,241,600.00 USD | `1,000.00` | `2241.82` | `2240.38` | `2831.03` | 224.49 USD | `+0.01%` | `5X Cross` |
| `994` | `0xd7b8...9f55` | `LONG` | 2,239,658.10 USD | `999.00` | `2195.00` | `2240.38` | `0.000000` | 46,853.10 USD | `+2.09%` | `15X Cross` |
| `1016` | `0xb002...ed8a` | `SHORT` | 2,158,465.45 USD | `962.78` | `2299.66` | `2240.38` | `4200.23` | 55,612.46 USD | `+2.58%` | `25X Cross` |
| `1033` | `0xb812...b5e0` | `LONG` | 2,106,585.36 USD | `940.99` | `2263.21` | `2240.38` | `1185.55` | -23,067.75 USD | `-1.10%` | `25X Cross` |
| `1041` | `0xb1ec...e86a` | `SHORT` | 2,092,843.84 USD | `933.64` | `2272.72` | `2240.38` | `12664.93` | 29,063.12 USD | `+1.39%` | `25X Cross` |
| `1059` | `0xef96...9383` | `LONG` | 2,056,835.90 USD | `917.57` | `2235.00` | `2240.38` | `0.000000` | 6,052.24 USD | `+0.29%` | `25X Cross` |
| `1068` | `0x9606...4e5d` | `SHORT` | 2,046,025.60 USD | `913.00` | `2478.70` | `2240.38` | `4304.33` | 217,028.00 USD | `+10.61%` | `20X Cross` |
| `1069` | `0xede2...f971` | `LONG` | 2,042,573.68 USD | `914.31` | `2208.16` | `2240.38` | `1463.26` | 23,616.69 USD | `+1.16%` | `5X Cross` |
| `1084` | `0x5f10...d49d` | `LONG` | 2,017,440.00 USD | `900.00` | `2249.83` | `2240.38` | `1800.71` | -7,413.47 USD | `-0.37%` | `25X Cross` |
| `1104` | `0x82f6...12ec` | `SHORT` | 1,988,603.41 USD | `887.02` | `2199.66` | `2240.38` | `2249.55` | -37,460.59 USD | `-1.88%` | `25X Cross` |
| `1144` | `0xa0fb...96be` | `LONG` | 1,943,710.61 USD | `868.35` | `2293.96` | `2240.38` | `1122.07` | -48,248.06 USD | `-2.48%` | `3X Cross` |
| `1170` | `0x24fb...ed0f` | `LONG` | 1,902,004.79 USD | `850.10` | `2199.85` | `2240.38` | `0.000000` | 31,917.92 USD | `+1.68%` | `15X Cross` |
| `1181` | `0xcd27...52a8` | `LONG` | 1,876,267.52 USD | `837.21` | `2553.56` | `2240.38` | `1403.49` | -261,597.25 USD | `-13.94%` | `2X Cross` |
| `1190` | `0xbef3...0d3e` | `LONG` | 1,854,784.40 USD | `827.33` | `2227.10` | `2240.38` | `2133.02` | 12,239.90 USD | `+0.66%` | `20X Cross` |
| `1202` | `0x6a41...a3b9` | `LONG` | 1,849,387.63 USD | `825.69` | `2226.70` | `2240.38` | `2136.78` | 10,815.18 USD | `+0.58%` | `20X Cross` |
| `1241` | `0x04a9...95aa` | `LONG` | 1,792,880.00 USD | `800.00` | `2595.13` | `2240.38` | `1865.00` | -283,226.74 USD | `-15.80%` | `5X Cross` |
| `1244` | `0x7737...bf66` | `SHORT` | 1,792,333.65 USD | `799.79` | `2494.83` | `2240.38` | `23928.36` | 203,012.38 USD | `+11.33%` | `15X Cross` |
| `1269` | `0x458d...ab3b` | `LONG` | 1,736,905.30 USD | `774.75` | `2740.41` | `2240.38` | `1887.25` | -386,223.88 USD | `-22.24%` | `3X Isolated` |
| `1288` | `0x2e30...4cb5` | `SHORT` | 1,697,265.72 USD | `757.37` | `2335.09` | `2240.38` | `8702.30` | 71,265.79 USD | `+4.20%` | `2X Cross` |
| `1331` | `0xaa53...9cb7` | `LONG` | 1,637,122.75 USD | `730.34` | `2389.70` | `2240.38` | `1960.73` | -108,166.89 USD | `-6.61%` | `20X Cross` |
| `1333` | `0x3fc5...c0c1` | `SHORT` | 1,636,490.06 USD | `729.92` | `2702.11` | `2240.38` | `4563.15` | 335,852.14 USD | `+20.52%` | `25X Cross` |
| `1339` | `0x6463...42f5` | `LONG` | 1,625,234.35 USD | `726.88` | `2214.40` | `2240.38` | `0.000000` | 15,623.68 USD | `+0.96%` | `1X Cross` |
| `1346` | `0xa189...94d7` | `SHORT` | 1,613,904.93 USD | `719.98` | `2691.84` | `2240.38` | `2915.10` | 324,167.73 USD | `+20.09%` | `25X Cross` |
| `1364` | `0x2f93...4404` | `LONG` | 1,580,349.84 USD | `707.47` | `1700.45` | `2240.38` | `1368.88` | 377,323.46 USD | `+23.88%` | `4X Isolated` |
| `1373` | `0x5605...fe0f` | `SHORT` | 1,571,678.23 USD | `702.14` | `2566.90` | `2240.38` | `3073.61` | 230,654.41 USD | `+14.68%` | `20X Cross` |
| `1374` | `0x7743...e4fe` | `SHORT` | 1,570,156.61 USD | `700.56` | `2298.56` | `2240.38` | `6178.19` | 40,118.48 USD | `+2.56%` | `25X Cross` |
| `1376` | `0x0deb...0bc5` | `LONG` | 1,569,120.00 USD | `700.00` | `2071.05` | `2240.38` | `1597.47` | 119,384.21 USD | `+7.61%` | `20X Cross` |
| `1408` | `0x51f6...2b39` | `LONG` | 1,549,800.10 USD | `691.38` | `2223.60` | `2240.38` | `385.94` | 12,439.07 USD | `+0.80%` | `25X Cross` |
| `1433` | `0x248e...6be2` | `SHORT` | 1,524,189.91 USD | `680.93` | `2282.89` | `2240.38` | `3450.80` | 30,295.76 USD | `+1.99%` | `20X Cross` |
| `1434` | `0xdbd1...29dd` | `SHORT` | 1,523,956.76 USD | `680.70` | `3030.57` | `2240.38` | `3775.29` | 538,964.37 USD | `+35.37%` | `6X Cross` |
| `1441` | `0x71e5...be04` | `LONG` | 1,519,057.90 USD | `677.67` | `2727.27` | `2240.38` | `1471.03` | -329,127.71 USD | `-21.67%` | `20X Cross` |
| `1449` | `0x0b23...f37b` | `LONG` | 1,511,122.50 USD | `675.00` | `2238.15` | `2240.38` | `594.68` | 365.86 USD | `+0.02%` | `5X Cross` |
| `1451` | `0x4487...c92d` | `LONG` | 1,505,798.38 USD | `672.11` | `2221.12` | `2240.38` | `1451.47` | 12,953.36 USD | `+0.86%` | `10X Cross` |
| `1476` | `0x0cac...6170` | `SHORT` | 1,473,457.50 USD | `657.50` | `2146.55` | `2240.38` | `2839.47` | -62,095.30 USD | `-4.21%` | `20X Cross` |
| `1503` | `0x9599...c60a` | `LONG` | 1,443,865.96 USD | `644.50` | `2231.08` | `2240.38` | `0.000000` | 5,942.10 USD | `+0.41%` | `20X Cross` |
| `1506` | `0xf00e...fe3d` | `SHORT` | 1,441,144.10 USD | `642.88` | `2333.21` | `2240.38` | `2489.63` | 58,833.87 USD | `+4.08%` | `20X Cross` |
| `1513` | `0xffb2...5ed6` | `SHORT` | 1,434,484.64 USD | `640.77` | `2672.96` | `2240.38` | `2504.05` | 278,263.71 USD | `+19.40%` | `20X Cross` |
| `1522` | `0x8505...1821` | `SHORT` | 1,416,584.29 USD | `633.96` | `2239.93` | `2240.38` | `3869.40` | 3,447.31 USD | `+0.24%` | `20X Cross` |
| `1524` | `0x31de...13f2` | `LONG` | 1,414,849.65 USD | `633.18` | `2252.34` | `2240.38` | `0.000000` | -11,299.11 USD | `-0.80%` | `20X Cross` |
| `1540` | `0xfce0...f4c0` | `SHORT` | 1,398,111.20 USD | `623.60` | `3129.61` | `2240.38` | `2798.02` | 553,515.39 USD | `+39.59%` | `20X Cross` |
| `1586` | `0xad02...eb65` | `LONG` | 1,346,170.05 USD | `600.62` | `2460.69` | `2240.38` | `1078.95` | -131,770.50 USD | `-9.79%` | `5X Cross` |
| `1587` | `0x26e6...6b28` | `LONG` | 1,345,200.00 USD | `600.00` | `1769.78` | `2240.38` | `2004.75` | 283,328.47 USD | `+21.06%` | `20X Cross` |
| `1589` | `0x7a76...b16d` | `LONG` | 1,344,660.00 USD | `600.00` | `2232.00` | `2240.38` | `2138.31` | 5,457.39 USD | `+0.41%` | `25X Cross` |
| `1590` | `0x638f...f5f0` | `LONG` | 1,344,600.00 USD | `600.00` | `4011.50` | `2240.38` | `349.16` | -1,062,303.53 USD | `-79.01%` | `25X Cross` |
| `1603` | `0x7c90...d129` | `LONG` | 1,331,122.41 USD | `594.17` | `2286.01` | `2240.38` | `1861.28` | -27,160.47 USD | `-2.04%` | `20X Cross` |
| `1665` | `0xfc66...ca06` | `SHORT` | 1,267,872.07 USD | `567.43` | `2275.19` | `2240.38` | `7323.53` | 23,151.14 USD | `+1.83%` | `20X Cross` |
| `1667` | `0xfb99...37f3` | `LONG` | 1,267,438.21 USD | `565.34` | `2362.35` | `2240.38` | `1245.30` | -68,098.14 USD | `-5.37%` | `3X Cross` |
| `1682` | `0x844b...7f42` | `SHORT` | 1,255,910.70 USD | `561.00` | `2026.17` | `2240.38` | `3030.73` | -119,227.29 USD | `-9.49%` | `25X Cross` |
| `1693` | `0xabe6...1d99` | `SHORT` | 1,245,282.16 USD | `556.00` | `2484.68` | `2240.38` | `3108.10` | 136,213.73 USD | `+10.94%` | `20X Cross` |
| `1696` | `0x2a76...9a53` | `LONG` | 1,244,010.08 USD | `554.99` | `2231.40` | `2240.38` | `0.000000` | 5,603.03 USD | `+0.45%` | `25X Cross` |
| `1706` | `0x936c...bb0f` | `LONG` | 1,233,078.61 USD | `550.09` | `2218.31` | `2240.38` | `0.000000` | 12,811.33 USD | `+1.04%` | `20X Cross` |
| `1707` | `0x825c...465e` | `LONG` | 1,231,835.00 USD | `550.00` | `2208.12` | `2240.38` | `1189.54` | 17,365.50 USD | `+1.41%` | `4X Cross` |
| `1714` | `0xad21...fb6a` | `LONG` | 1,226,728.83 USD | `547.26` | `2565.80` | `2240.38` | `1732.76` | -177,424.17 USD | `-14.46%` | `6X Cross` |
| `1817` | `0x0c7a...2f50` | `SHORT` | 1,141,524.26 USD | `509.25` | `2122.56` | `2240.38` | `4108.60` | -60,618.83 USD | `-5.31%` | `20X Cross` |
| `1824` | `0x0089...2410` | `SHORT` | 1,137,265.90 USD | `507.35` | `2308.88` | `2240.38` | `3398.45` | 34,134.36 USD | `+3.00%` | `20X Cross` |
| `1837` | `0x6936...9417` | `SHORT` | 1,121,000.00 USD | `500.00` | `2315.11` | `2240.38` | `2358.98` | 36,555.21 USD | `+3.26%` | `25X Isolated` |
| `1838` | `0xa559...ff95` | `LONG` | 1,120,950.00 USD | `500.00` | `2260.68` | `2240.38` | `1054.63` | -9,394.36 USD | `-0.84%` | `20X Cross` |
| `1839` | `0x4044...794c` | `LONG` | 1,120,950.00 USD | `500.00` | `2260.80` | `2240.38` | `0.000000` | -9,450.00 USD | `-0.84%` | `25X Cross` |
| `1840` | `0xe282...df29` | `LONG` | 1,120,650.00 USD | `500.00` | `2309.84` | `2240.38` | `2045.39` | -34,274.21 USD | `-3.06%` | `10X Isolated` |
| `1841` | `0xb322...d51f` | `SHORT` | 1,120,650.00 USD | `500.00` | `2268.03` | `2240.38` | `3764.24` | 13,366.32 USD | `+1.19%` | `20X Cross` |
| `1846` | `0x89b2...9ca6` | `LONG` | 1,119,300.00 USD | `500.00` | `2363.45` | `2240.38` | `1622.73` | -62,427.42 USD | `-5.58%` | `25X Cross` |
| `1852` | `0x7298...7d6c` | `SHORT` | 1,116,800.92 USD | `498.15` | `3426.75` | `2240.38` | `5421.69` | 590,234.91 USD | `+52.85%` | `20X Cross` |
| `1862` | `0x9c68...7783` | `SHORT` | 1,105,798.76 USD | `493.31` | `2273.58` | `2240.38` | `3901.99` | 15,780.48 USD | `+1.43%` | `25X Cross` |
| `1868` | `0x404c...5f03` | `SHORT` | 1,097,363.96 USD | `489.79` | `2671.94` | `2240.38` | `5012.53` | 211,315.59 USD | `+19.26%` | `20X Cross` |
| `1872` | `0x321f...1c84` | `SHORT` | 1,092,471.27 USD | `488.02` | `2370.09` | `2240.38` | `3051.74` | 64,173.33 USD | `+5.87%` | `10X Cross` |
| `1889` | `0x71d0...8c26` | `LONG` | 1,077,326.24 USD | `480.73` | `2225.97` | `2240.38` | `0.000000` | 7,221.48 USD | `+0.67%` | `25X Cross` |
| `1926` | `0xe86b...3664` | `LONG` | 1,047,696.94 USD | `467.39` | `2231.29` | `2240.38` | `0.000000` | 4,816.01 USD | `+0.46%` | `25X Cross` |
| `1942` | `0x94b6...e5b3` | `SHORT` | 1,039,320.23 USD | `463.86` | `2261.12` | `2240.38` | `2434.02` | 9,522.43 USD | `+0.92%` | `25X Cross` |
| `1949` | `0x82c6...fe42` | `LONG` | 1,036,925.00 USD | `462.50` | `2501.38` | `2240.38` | `2053.73` | -119,965.57 USD | `-11.57%` | `5X Isolated` |
| `1957` | `0xe330...77a1` | `SHORT` | 1,032,490.68 USD | `461.20` | `2206.97` | `2240.38` | `6431.83` | -14,633.31 USD | `-1.42%` | `20X Cross` |
| `1958` | `0x2de3...486d` | `LONG` | 1,032,032.64 USD | `460.40` | `2286.27` | `2240.38` | `1172.21` | -20,568.27 USD | `-1.99%` | `25X Cross` |
| `1972` | `0x617e...0f97` | `SHORT` | 1,025,502.29 USD | `457.85` | `2205.60` | `2240.38` | `3383.85` | -15,658.45 USD | `-1.53%` | `10X Cross` |
| `2000` | `0xae55...2236` | `LONG` | 1,008,450.00 USD | `450.00` | `2510.21` | `2240.38` | `0.000000` | -121,147.50 USD | `-12.01%` | `25X Cross` |
| `2001` | `0xc10f...23b3` | `LONG` | 1,008,405.00 USD | `450.00` | `2366.44` | `2240.38` | `2016.80` | -56,493.27 USD | `-5.60%` | `25X Cross` |
| `2003` | `0x0514...bdfe` | `SHORT` | 1,005,300.00 USD | `450.00` | `1988.74` | `2240.38` | `3877.38` | -110,363.16 USD | `-10.98%` | `25X Cross` |
| `2007` | `0xaa7a...af37` | `LONG` | 1,003,458.17 USD | `448.03` | `2212.37` | `2240.38` | `0.000000` | 12,241.93 USD | `+1.22%` | `20X Cross` |
| `2011` | `0xac26...a9c7` | `SHORT` | 1,000,058.23 USD | `446.14` | `2192.58` | `2240.38` | `8593.48` | -21,867.69 USD | `-2.19%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `2356.80` | 41,836.97 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 41.84K USD at 2356.8000 USD [API] | `2026-10-29 00:36:32` |
| `ANNOUNCEMENT` | `INFO` | `2343.30` | 46,866.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 46.87K USD at 2343.3000 USD [API] | `2026-10-29 01:10:12` |
| `ANNOUNCEMENT` | `INFO` | `2347.00` | 207,777.56 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 207.78K USD at 2347.0000 USD [API] | `2026-10-29 01:18:29` |
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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2240.09` (Vol: 38,100,000.00 USD, Dist: `+0.24%`) | Long MP=`2174.37` (Vol: 35,800,000.00 USD, Dist: `--2.70%`)
  * 48H Horizon: Short MP=`2238.88` (Vol: 26,900,000.00 USD, Dist: `+0.18%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--2.72%`)
  * 3D Horizon: Short MP=`2402.29` (Vol: 31,100,000.00 USD, Dist: `+7.49%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--2.72%`)
  * 7D Horizon: Short MP=`2401.80` (Vol: 50,700,000.00 USD, Dist: `+7.47%`) | Long MP=`2175.27` (Vol: 44,800,000.00 USD, Dist: `--2.66%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `455.00` | 72,310.00 USD | 759,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `465.00` | 2,230.00 USD | 759,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 198,670.00 USD | 759,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 98,630.00 USD | 759,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 88,680.00 USD | 759,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 45,950.00 USD | 759,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 1,880,000.00 USD | 759,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 26,700.00 USD | 757,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 2,660.00 USD | 757,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 16,450.00 USD | 757,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 190,490.00 USD | 757,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 666,590.00 USD | 756,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 44,270.00 USD | 756,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 1,790,000.00 USD | 756,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 541,190.00 USD | 754,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 2,990,000.00 USD | 753,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 1,020,000.00 USD | 750,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 20,060.00 USD | 749,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 7,980.00 USD | 749,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 54,890.00 USD | 749,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 117,840.00 USD | 749,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 165,010.00 USD | 749,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 147,900.00 USD | 749,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 35,730.00 USD | 749,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 66,640.00 USD | 749,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 7,860.00 USD | 749,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 1,140.00 USD | 749,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 397,250.00 USD | 749,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 189,130.00 USD | 748,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 63,060.00 USD | 748,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 28,770.00 USD | 748,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 12,370.00 USD | 748,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 11,490.00 USD | 748,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 91,840.00 USD | 748,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 66,420.00 USD | 748,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 136,320.00 USD | 748,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 436,890.00 USD | 748,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 79,450.00 USD | 747,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 121,540.00 USD | 747,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 96,220.00 USD | 747,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 135,540.00 USD | 747,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 521,630.00 USD | 747,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 53,500.00 USD | 746,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 1,100,000.00 USD | 746,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 14,900.00 USD | 745,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 352,150.00 USD | 745,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 161,430.00 USD | 745,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 218,380.00 USD | 745,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 47,430.00 USD | 744,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 227,350.00 USD | 744,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 117,540.00 USD | 744,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 113,520.00 USD | 744,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 81,320.00 USD | 744,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 152,820.00 USD | 744,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 5,740,000.00 USD | 744,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 56,100.00 USD | 738,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 232,420.00 USD | 738,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 187,160.00 USD | 738,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 1,410,000.00 USD | 737,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 401,740.00 USD | 736,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 2,120,000.00 USD | 736,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 7,740,000.00 USD | 734,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 660,160.00 USD | 726,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 354,200.00 USD | 725,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 54,230.00 USD | 725,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 172,280.00 USD | 725,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 7,920,000.00 USD | 725,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 158,830.00 USD | 717,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 475,040.00 USD | 717,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 196,970.00 USD | 716,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 1,370,000.00 USD | 716,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 72,300.00 USD | 714,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 1,510,000.00 USD | 714,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 2,110,000.00 USD | 713,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 218,050.00 USD | 711,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 185,340.00 USD | 711,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 2,090,000.00 USD | 710,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 556,370.00 USD | 708,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 80,420.00 USD | 708,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 819,550.00 USD | 708,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 438,130.00 USD | 707,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 1,690,000.00 USD | 706,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 15,440,000.00 USD | 705,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 279,440.00 USD | 689,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 371,250.00 USD | 689,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 268,590.00 USD | 689,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 221,150.00 USD | 688,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 506,670.00 USD | 688,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 291,100.00 USD | 688,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 5,390,000.00 USD | 687,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 12,260,000.00 USD | 682,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 1,910,000.00 USD | 670,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 638,470.00 USD | 668,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 9,170,000.00 USD | 667,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 360,520.00 USD | 658,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 9,980,000.00 USD | 658,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 227,570.00 USD | 648,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 2,650,000.00 USD | 647,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 1,130,000.00 USD | 645,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 18,850,000.00 USD | 644,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 335,310.00 USD | 625,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 1,780,000.00 USD | 624,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 12,160,000.00 USD | 623,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 185,340.00 USD | 610,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 158,690.00 USD | 610,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 281,240.00 USD | 610,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 729,610.00 USD | 610,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 19,520,000.00 USD | 609,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 989,140.00 USD | 590,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 20,230,000.00 USD | 589,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 410,620.00 USD | 568,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 3,430,000.00 USD | 568,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 267,000.00 USD | 565,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 861,320.00 USD | 564,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 1,620,000.00 USD | 563,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 21,750,000.00 USD | 562,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 173,560.00 USD | 540,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 1,730,000.00 USD | 540,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 18,480,000.00 USD | 538,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 38,040,000.00 USD | 520,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 925,200.00 USD | 482,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 1,380,000.00 USD | 481,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 12,260,000.00 USD | 479,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 606,650.00 USD | 467,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 417,600.00 USD | 466,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 1,230,000.00 USD | 466,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 575,210.00 USD | 465,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 36,130,000.00 USD | 464,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 1,540,000.00 USD | 428,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 1,310,000.00 USD | 427,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 1,140,000.00 USD | 425,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 49,080,000.00 USD | 424,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 734,410.00 USD | 375,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 61,370,000.00 USD | 374,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 495,870.00 USD | 313,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 3,280,000.00 USD | 312,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 805,460.00 USD | 309,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 831,850.00 USD | 308,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 1,130,000.00 USD | 308,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 27,870,000.00 USD | 306,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 1,680,000.00 USD | 279,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 3,380,000.00 USD | 277,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 8,890,000.00 USD | 273,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 5,830,000.00 USD | 265,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 775,090.00 USD | 259,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 490,530.00 USD | 258,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 18,290,000.00 USD | 257,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 16,340,000.00 USD | 239,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 4,460,000.00 USD | 223,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 1,690,000.00 USD | 218,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 1,290,000.00 USD | 217,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 2,730,000.00 USD | 215,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,950,000.00 USD | 213,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1985.00` | 5,060,000.00 USD | 211,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1995.00` | 1,560,000.00 USD | 206,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2005.00` | 2,090,000.00 USD | 204,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2015.00` | 5,730,000.00 USD | 202,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2025.00` | 2,100,000.00 USD | 196,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2025.30` | 942,910,000.00 USD | 942,910,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2027.00` | 534,200,000.00 USD | 534,200,000.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.60` | 942,730,000.00 USD | 942,730,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2029.60` | 533,220,000.00 USD | 533,220,000.00 USD | 87,180.00 USD | 163,200.00 USD | 43,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.90` | 941,520,000.00 USD | 941,520,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.20` | 532,920,000.00 USD | 532,920,000.00 USD | 1,360,000.00 USD | 542,800.00 USD | 408,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2034.80` | 530,610,000.00 USD | 530,610,000.00 USD | 1,030,000.00 USD | 787,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 1,080,000.00 USD | 194,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2035.20` | 940,070,000.00 USD | 940,070,000.00 USD | 146,420.00 USD | 186,130.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2037.40` | 528,790,000.00 USD | 528,790,000.00 USD | 202,200.00 USD | 317,820.00 USD | 378,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.50` | 938,380,000.00 USD | 938,380,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2040.00` | 527,890,000.00 USD | 527,890,000.00 USD | 345,650.00 USD | 178,560.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2042.60` | 527,330,000.00 USD | 527,330,000.00 USD | 626,840.00 USD | 0.00 USD | 20,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 2,000,000.00 USD | 193,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2045.10` | 936,930,000.00 USD | 936,930,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2045.20` | 526,690,000.00 USD | 526,690,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2047.80` | 526,660,000.00 USD | 526,660,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.40` | 525,830,000.00 USD | 525,830,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2051.70` | 936,630,000.00 USD | 936,630,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2053.00` | 524,720,000.00 USD | 524,720,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 5,940,000.00 USD | 191,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2055.60` | 524,700,000.00 USD | 524,700,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2058.20` | 524,370,000.00 USD | 524,370,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2058.30` | 934,120,000.00 USD | 934,120,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2060.80` | 523,610,000.00 USD | 523,610,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.60` | 933,780,000.00 USD | 933,780,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2063.40` | 523,530,000.00 USD | 523,530,000.00 USD | 643,750.00 USD | 555,980.00 USD | 600,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.90` | 928,520,000.00 USD | 928,520,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 13,860,000.00 USD | 185,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2066.00` | 521,730,000.00 USD | 521,730,000.00 USD | 808,950.00 USD | 100,330.00 USD | 53,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2068.20` | 925,990,000.00 USD | 925,990,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2068.60` | 520,770,000.00 USD | 520,770,000.00 USD | 57,300.00 USD | 1,270,000.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2071.20` | 519,410,000.00 USD | 519,410,000.00 USD | 1,040,000.00 USD | 534,600.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.50` | 921,500,000.00 USD | 921,500,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.80` | 517,400,000.00 USD | 517,400,000.00 USD | 419,970.00 USD | 62,630.00 USD | 926,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.80` | 915,040,000.00 USD | 915,040,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 2,720,000.00 USD | 171,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2076.40` | 515,990,000.00 USD | 515,990,000.00 USD | 2,580,000.00 USD | 1,020,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.10` | 903,340,000.00 USD | 903,340,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2079.00` | 510,390,000.00 USD | 510,390,000.00 USD | 1,320,000.00 USD | 1,010,000.00 USD | 436,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.40` | 891,050,000.00 USD | 891,050,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2081.60` | 507,620,000.00 USD | 507,620,000.00 USD | 1,430,000.00 USD | 1,260,000.00 USD | 227,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2084.20` | 504,700,000.00 USD | 504,700,000.00 USD | 2,090,000.00 USD | 1,290,000.00 USD | 753,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.70` | 880,410,000.00 USD | 880,410,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 13,600,000.00 USD | 169,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2086.80` | 500,570,000.00 USD | 500,570,000.00 USD | 1,600,000.00 USD | 1,650,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.00` | 871,620,000.00 USD | 871,620,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2089.40` | 495,720,000.00 USD | 495,720,000.00 USD | 1,080,000.00 USD | 220,540.00 USD | 92,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.30` | 863,190,000.00 USD | 863,190,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.00` | 494,330,000.00 USD | 494,330,000.00 USD | 1,130,000.00 USD | 514,440.00 USD | 955,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2094.60` | 491,720,000.00 USD | 491,720,000.00 USD | 2,040,000.00 USD | 1,120,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.60` | 850,240,000.00 USD | 850,240,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,380,000.00 USD | 155,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2097.20` | 487,130,000.00 USD | 487,130,000.00 USD | 617,040.00 USD | 1,010,000.00 USD | 984,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.90` | 840,020,000.00 USD | 840,020,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2099.80` | 484,520,000.00 USD | 484,520,000.00 USD | 172,210.00 USD | 403,100.00 USD | 11,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.20` | 833,180,000.00 USD | 833,180,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.40` | 483,930,000.00 USD | 483,930,000.00 USD | 507,510.00 USD | 289,160.00 USD | 466,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2104.50` | 826,580,000.00 USD | 826,580,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2105.00` | 482,670,000.00 USD | 482,670,000.00 USD | 612,280.00 USD | 671,930.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 2,280,000.00 USD | 154,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2107.60` | 481,350,000.00 USD | 481,350,000.00 USD | 603,300.00 USD | 0.00 USD | 488,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.80` | 821,140,000.00 USD | 821,140,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.20` | 480,260,000.00 USD | 480,260,000.00 USD | 61,010.00 USD | 31,550.00 USD | 196,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2111.10` | 816,650,000.00 USD | 816,650,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2112.80` | 479,970,000.00 USD | 479,970,000.00 USD | 911,810.00 USD | 643,210.00 USD | 224,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2114.40` | 808,610,000.00 USD | 808,610,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 2,910,000.00 USD | 151,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2115.40` | 478,190,000.00 USD | 478,190,000.00 USD | 0.00 USD | 13,230.00 USD | 426,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.70` | 801,880,000.00 USD | 801,880,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2118.00` | 477,750,000.00 USD | 477,750,000.00 USD | 202,840.00 USD | 14,580.00 USD | 472,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.60` | 477,060,000.00 USD | 477,060,000.00 USD | 744,340.00 USD | 215,530.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2121.00` | 793,040,000.00 USD | 793,040,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.20` | 475,050,000.00 USD | 475,050,000.00 USD | 757,170.00 USD | 1,210,000.00 USD | 917,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.30` | 786,240,000.00 USD | 786,240,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,240,000.00 USD | 148,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.80` | 472,170,000.00 USD | 472,170,000.00 USD | 68,480.00 USD | 554,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.60` | 782,920,000.00 USD | 782,920,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.40` | 471,540,000.00 USD | 471,540,000.00 USD | 107,010.00 USD | 475,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.90` | 774,620,000.00 USD | 774,620,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2131.00` | 470,960,000.00 USD | 470,960,000.00 USD | 0.00 USD | 18,610.00 USD | 331,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.20` | 768,200,000.00 USD | 768,200,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 4,840,000.00 USD | 25,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2136.20` | 470,610,000.00 USD | 470,610,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.50` | 765,170,000.00 USD | 765,170,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.80` | 763,210,000.00 USD | 763,210,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.10` | 759,270,000.00 USD | 759,270,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 5,020,000.00 USD | 20,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2147.40` | 757,430,000.00 USD | 757,430,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.70` | 756,350,000.00 USD | 756,350,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2151.80` | 470,330,000.00 USD | 470,330,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.00` | 755,390,000.00 USD | 755,390,000.00 USD | 128,430.00 USD | 311,060.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2154.40` | 469,680,000.00 USD | 469,680,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 3,970,000.00 USD | 15,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2157.30` | 754,920,000.00 USD | 754,920,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2159.60` | 468,290,000.00 USD | 468,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 37,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.60` | 752,430,000.00 USD | 752,430,000.00 USD | 613,630.00 USD | 1,900,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2162.20` | 465,960,000.00 USD | 465,960,000.00 USD | 0.00 USD | 932,730.00 USD | 100,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.90` | 747,910,000.00 USD | 747,910,000.00 USD | 566,120.00 USD | 2,950,000.00 USD | 540,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2164.80` | 464,930,000.00 USD | 464,930,000.00 USD | 217,960.00 USD | 408,000.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 5,390,000.00 USD | 11,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2167.20` | 743,850,000.00 USD | 743,850,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.40` | 464,190,000.00 USD | 464,190,000.00 USD | 3,220,000.00 USD | 0.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.00` | 459,950,000.00 USD | 459,950,000.00 USD | 5,210,000.00 USD | 5,170,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.50` | 740,150,000.00 USD | 740,150,000.00 USD | 3,500,000.00 USD | 3,730,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2172.60` | 446,820,000.00 USD | 446,820,000.00 USD | 63,650.00 USD | 1,290,000.00 USD | 581,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.80` | 727,710,000.00 USD | 727,710,000.00 USD | 4,370,000.00 USD | 363,040.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 5,680,000.00 USD | 6,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.20` | 444,890,000.00 USD | 444,890,000.00 USD | 1,970,000.00 USD | 111,190.00 USD | 894,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2177.10` | 721,850,000.00 USD | 721,850,000.00 USD | 1,750,000.00 USD | 1,330,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2177.80` | 441,920,000.00 USD | 441,920,000.00 USD | 2,320,000.00 USD | 1,770,000.00 USD | 99,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2180.40` | 437,720,000.00 USD | 437,720,000.00 USD | 2,080,000.00 USD | 267,450.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2180.40` | 715,950,000.00 USD | 715,950,000.00 USD | 0.00 USD | 373,740.00 USD | 431,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2183.00` | 433,960,000.00 USD | 433,960,000.00 USD | 2,960,000.00 USD | 1,140,000.00 USD | 425,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2183.70` | 715,150,000.00 USD | 715,150,000.00 USD | 1,760,000.00 USD | 1,310,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 618,490.00 USD | 731,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2185.60` | 429,440,000.00 USD | 429,440,000.00 USD | 566,020.00 USD | 1,960,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.00` | 708,140,000.00 USD | 708,140,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2188.20` | 424,220,000.00 USD | 424,220,000.00 USD | 0.00 USD | 42,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.30` | 707,530,000.00 USD | 707,530,000.00 USD | 2,730,000.00 USD | 0.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2190.80` | 424,180,000.00 USD | 424,180,000.00 USD | 0.00 USD | 222,200.00 USD | 764,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2193.40` | 423,190,000.00 USD | 423,190,000.00 USD | 605,210.00 USD | 0.00 USD | 39,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 107,420.00 USD | 112,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2196.00` | 422,550,000.00 USD | 422,550,000.00 USD | 416,500.00 USD | 881,070.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.90` | 700,600,000.00 USD | 700,600,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2198.60` | 419,370,000.00 USD | 419,370,000.00 USD | 0.00 USD | 2,940,000.00 USD | 50,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.20` | 695,500,000.00 USD | 695,500,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2201.20` | 416,370,000.00 USD | 416,370,000.00 USD | 1,690,000.00 USD | 1,450,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.50` | 684,230,000.00 USD | 684,230,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.80` | 411,730,000.00 USD | 411,730,000.00 USD | 2,130,000.00 USD | 314,310.00 USD | 830,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 5,310.00 USD | 5,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `7D` | `Long Liquidation` | `2226.60` | 428,420,000.00 USD | 428,420,000.00 USD | 16,350,000.00 USD | 11,030,000.00 USD | 10,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.20` | 249,870,000.00 USD | 249,870,000.00 USD | 5,120,000.00 USD | 13,730,000.00 USD | 5,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2229.80` | 225,310,000.00 USD | 225,310,000.00 USD | 10,100,000.00 USD | 7,120,000.00 USD | 4,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.90` | 390,570,000.00 USD | 390,570,000.00 USD | 12,730,000.00 USD | 11,790,000.00 USD | 28,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2232.40` | 204,000,000.00 USD | 204,000,000.00 USD | 4,620,000.00 USD | 6,200,000.00 USD | 7,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2233.20` | 337,500,000.00 USD | 337,500,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2235.00` | 185,910,000.00 USD | 185,910,000.00 USD | 19,080,000.00 USD | 85,110.00 USD | 11,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2235.00` | 14,960.00 USD | 14,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2236.50` | 286,180,000.00 USD | 286,180,000.00 USD | 16,050,000.00 USD | 7,430,000.00 USD | 27,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2237.60` | 155,300,000.00 USD | 155,300,000.00 USD | 23,860,000.00 USD | 7,390,000.00 USD | 12,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.80` | 234,940,000.00 USD | 234,940,000.00 USD | 16,720,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2240.20` | 111,600,000.00 USD | 111,600,000.00 USD | 1,100,000.00 USD | 1,380,000.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2242.80` | 106,890,000.00 USD | 106,890,000.00 USD | 9,030,000.00 USD | 3,760,000.00 USD | 9,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2243.10` | 197,880,000.00 USD | 197,880,000.00 USD | 29,940,000.00 USD | 5,310,000.00 USD | 24,810,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2245.00` | 1,800,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2245.40` | 84,870,000.00 USD | 84,870,000.00 USD | 11,210,000.00 USD | 6,190,000.00 USD | 501,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2246.40` | 137,820,000.00 USD | 137,820,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2248.00` | 66,970,000.00 USD | 66,970,000.00 USD | 12,490,000.00 USD | 1,070,000.00 USD | 7,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2249.70` | 109,560,000.00 USD | 109,560,000.00 USD | 25,030,000.00 USD | 0.00 USD | 19,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2250.60` | 46,290,000.00 USD | 46,290,000.00 USD | 4,450,000.00 USD | 4,540,000.00 USD | 5,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.00` | 65,090,000.00 USD | 65,090,000.00 USD | 26,890,000.00 USD | 0.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2253.20` | 31,680,000.00 USD | 31,680,000.00 USD | 13,840,000.00 USD | 4,440,000.00 USD | 8,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 2,970,000.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2255.80` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2256.30` | 26,160,000.00 USD | 26,160,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2258.40` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 170,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2259.60` | 10,940,000.00 USD | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2261.00` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 156,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 2,310,000.00 USD | 7,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2266.20` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2268.80` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2274.00` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 288,080.00 USD | 114,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 276,460.00 USD | 7,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2276.60` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 267,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2279.20` | 22,720,000.00 USD | 22,720,000.00 USD | 11,600,000.00 USD | 3,950,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2279.40` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 17,000,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2281.80` | 85,490,000.00 USD | 85,490,000.00 USD | 33,480,000.00 USD | 26,790,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.70` | 117,630,000.00 USD | 117,630,000.00 USD | 0.00 USD | 87,090,000.00 USD | 13,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2284.40` | 152,200,000.00 USD | 152,200,000.00 USD | 33,020,000.00 USD | 19,430,000.00 USD | 14,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 767,790.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2286.00` | 128,050,000.00 USD | 128,050,000.00 USD | 1,010,000.00 USD | 9,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2287.00` | 164,470,000.00 USD | 164,470,000.00 USD | 3,210,000.00 USD | 5,140,000.00 USD | 3,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2289.30` | 152,130,000.00 USD | 152,130,000.00 USD | 7,010,000.00 USD | 5,310,000.00 USD | 11,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2289.60` | 176,810,000.00 USD | 176,810,000.00 USD | 3,280,000.00 USD | 8,840,000.00 USD | 219,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2292.20` | 197,140,000.00 USD | 197,140,000.00 USD | 17,600,000.00 USD | 2,560,000.00 USD | 176,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2292.60` | 153,150,000.00 USD | 153,150,000.00 USD | 0.00 USD | 0.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2294.80` | 209,490,000.00 USD | 209,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 5,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 3,840,000.00 USD | 11,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2295.90` | 180,460,000.00 USD | 180,460,000.00 USD | 13,610,000.00 USD | 2,380,000.00 USD | 11,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2297.40` | 233,240,000.00 USD | 233,240,000.00 USD | 11,830,000.00 USD | 6,530,000.00 USD | 5,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.20` | 208,880,000.00 USD | 208,880,000.00 USD | 11,730,000.00 USD | 11,130,000.00 USD | 5,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2300.00` | 249,950,000.00 USD | 249,950,000.00 USD | 2,700,000.00 USD | 6,620,000.00 USD | 7,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.50` | 255,990,000.00 USD | 255,990,000.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.60` | 269,830,000.00 USD | 269,830,000.00 USD | 14,790,000.00 USD | 170,210.00 USD | 4,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 266,780.00 USD | 12,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.20` | 299,270,000.00 USD | 299,270,000.00 USD | 10,430,000.00 USD | 14,490,000.00 USD | 4,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.80` | 276,770,000.00 USD | 276,770,000.00 USD | 2,980,000.00 USD | 8,820,000.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2307.80` | 307,480,000.00 USD | 307,480,000.00 USD | 2,550,000.00 USD | 3,220,000.00 USD | 2,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2309.10` | 281,280,000.00 USD | 281,280,000.00 USD | 1,240,000.00 USD | 930,630.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2310.40` | 323,320,000.00 USD | 323,320,000.00 USD | 3,940,000.00 USD | 2,450,000.00 USD | 9,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2312.40` | 308,580,000.00 USD | 308,580,000.00 USD | 10,780,000.00 USD | 2,650,000.00 USD | 13,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2313.00` | 335,020,000.00 USD | 335,020,000.00 USD | 4,650,000.00 USD | 6,730,000.00 USD | 313,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 1,010,000.00 USD | 13,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2315.60` | 366,280,000.00 USD | 366,280,000.00 USD | 9,790,000.00 USD | 14,850,000.00 USD | 6,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2315.70` | 316,670,000.00 USD | 316,670,000.00 USD | 0.00 USD | 7,460,000.00 USD | 627,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2318.20` | 379,270,000.00 USD | 379,270,000.00 USD | 4,440,000.00 USD | 6,320,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.00` | 334,170,000.00 USD | 334,170,000.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 8,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.80` | 396,910,000.00 USD | 396,910,000.00 USD | 5,790,000.00 USD | 9,890,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.30` | 351,330,000.00 USD | 351,330,000.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 108,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2323.40` | 412,610,000.00 USD | 412,610,000.00 USD | 1,710,000.00 USD | 10,410,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,990,000.00 USD | 15,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.60` | 371,980,000.00 USD | 371,980,000.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2326.00` | 424,390,000.00 USD | 424,390,000.00 USD | 479,120.00 USD | 5,640,000.00 USD | 5,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2328.60` | 427,380,000.00 USD | 427,380,000.00 USD | 2,140,000.00 USD | 444,400.00 USD | 402,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.90` | 383,810,000.00 USD | 383,810,000.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2331.20` | 445,540,000.00 USD | 445,540,000.00 USD | 17,350,000.00 USD | 692,470.00 USD | 126,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2332.20` | 413,040,000.00 USD | 413,040,000.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2333.80` | 463,270,000.00 USD | 463,270,000.00 USD | 7,710,000.00 USD | 2,820,000.00 USD | 7,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 828,820.00 USD | 16,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2335.50` | 471,050,000.00 USD | 471,050,000.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 10,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2336.40` | 481,890,000.00 USD | 481,890,000.00 USD | 15,940,000.00 USD | 547,950.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.80` | 488,920,000.00 USD | 488,920,000.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2339.00` | 494,900,000.00 USD | 494,900,000.00 USD | 6,360,000.00 USD | 2,600,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2341.60` | 513,570,000.00 USD | 513,570,000.00 USD | 5,340,000.00 USD | 3,430,000.00 USD | 9,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2342.10` | 529,020,000.00 USD | 529,020,000.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2344.20` | 526,900,000.00 USD | 526,900,000.00 USD | 1,370,000.00 USD | 6,240,000.00 USD | 5,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 109,700.00 USD | 16,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2345.40` | 550,400,000.00 USD | 550,400,000.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2346.80` | 540,470,000.00 USD | 540,470,000.00 USD | 3,930,000.00 USD | 3,010,000.00 USD | 6,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.70` | 588,270,000.00 USD | 588,270,000.00 USD | 847,620.00 USD | 9,500,000.00 USD | 27,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2349.40` | 571,320,000.00 USD | 571,320,000.00 USD | 19,450,000.00 USD | 5,980,000.00 USD | 5,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2352.00` | 598,840,000.00 USD | 598,840,000.00 USD | 18,420,000.00 USD | 2,080,000.00 USD | 7,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2352.00` | 624,900,000.00 USD | 624,900,000.00 USD | 2,930,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2354.60` | 622,470,000.00 USD | 622,470,000.00 USD | 973,980.00 USD | 20,450,000.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,220,000.00 USD | 17,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2355.30` | 684,440,000.00 USD | 684,440,000.00 USD | 18,530,000.00 USD | 38,020,000.00 USD | 3,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.20` | 632,150,000.00 USD | 632,150,000.00 USD | 4,390,000.00 USD | 1,740,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.60` | 696,580,000.00 USD | 696,580,000.00 USD | 7,110,000.00 USD | 512,220.00 USD | 4,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2359.80` | 653,040,000.00 USD | 653,040,000.00 USD | 8,920,000.00 USD | 6,950,000.00 USD | 5,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.90` | 703,960,000.00 USD | 703,960,000.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 431,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.40` | 673,590,000.00 USD | 673,590,000.00 USD | 8,900,000.00 USD | 6,710,000.00 USD | 4,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2365.00` | 690,810,000.00 USD | 690,810,000.00 USD | 6,420,000.00 USD | 4,850,000.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 3,880,000.00 USD | 21,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2365.20` | 725,010,000.00 USD | 725,010,000.00 USD | 10,200,000.00 USD | 0.00 USD | 10,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.60` | 699,590,000.00 USD | 699,590,000.00 USD | 4,770,000.00 USD | 1,110,000.00 USD | 2,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.50` | 738,080,000.00 USD | 738,080,000.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 458,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.20` | 735,010,000.00 USD | 735,010,000.00 USD | 14,350,000.00 USD | 12,620,000.00 USD | 8,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.80` | 819,020,000.00 USD | 819,020,000.00 USD | 26,000,000.00 USD | 0.00 USD | 54,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.80` | 761,980,000.00 USD | 761,980,000.00 USD | 14,450,000.00 USD | 5,460,000.00 USD | 7,060,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 894,650.00 USD | 22,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2375.10` | 845,960,000.00 USD | 845,960,000.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2375.40` | 780,580,000.00 USD | 780,580,000.00 USD | 11,510,000.00 USD | 3,420,000.00 USD | 3,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.00` | 803,100,000.00 USD | 803,100,000.00 USD | 5,030,000.00 USD | 6,270,000.00 USD | 11,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.40` | 891,380,000.00 USD | 891,380,000.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.60` | 840,470,000.00 USD | 840,470,000.00 USD | 11,320,000.00 USD | 11,190,000.00 USD | 14,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.70` | 931,170,000.00 USD | 931,170,000.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 24,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.20` | 886,340,000.00 USD | 886,340,000.00 USD | 20,060,000.00 USD | 12,500,000.00 USD | 13,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2385.00` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 5,770,000.00 USD | 27,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.80` | 910,150,000.00 USD | 910,150,000.00 USD | 8,950,000.00 USD | 10,960,000.00 USD | 3,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.30` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2388.40` | 935,260,000.00 USD | 935,260,000.00 USD | 13,100,000.00 USD | 6,720,000.00 USD | 5,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2391.00` | 950,870,000.00 USD | 950,870,000.00 USD | 3,770,000.00 USD | 6,670,000.00 USD | 5,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2393.60` | 965,250,000.00 USD | 965,250,000.00 USD | 4,380,000.00 USD | 6,000,000.00 USD | 4,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.90` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 155,990.00 USD | 28,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2396.20` | 979,190,000.00 USD | 979,190,000.00 USD | 5,350,000.00 USD | 4,020,000.00 USD | 4,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2398.20` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.80` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 8,890,000.00 USD | 6,800,000.00 USD | 7,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2401.40` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 4,600,000.00 USD | 6,190,000.00 USD | 6,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.50` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2404.00` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 9,470,000.00 USD | 8,980,000.00 USD | 7,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.80` | 1,670,000,000.00 USD | 1,670,000,000.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 190,970.00 USD | 28,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2406.60` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 11,990,000.00 USD | 7,780,000.00 USD | 5,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2408.10` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2409.20` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 8,220,000.00 USD | 6,130,000.00 USD | 6,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.40` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2411.80` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 8,840,000.00 USD | 7,170,000.00 USD | 3,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2414.40` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 2,970,000.00 USD | 2,340,000.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.70` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 23,820,000.00 USD | 21,740,000.00 USD | 23,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 164,460.00 USD | 28,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2417.00` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 3,600,000.00 USD | 2,550,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.00` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2419.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 6,520,000.00 USD | 3,840,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.30` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 25,700,000.00 USD | 27,770,000.00 USD | 21,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.20` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 2,930,000.00 USD | 3,700,000.00 USD | 5,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.60` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 23,650,000.00 USD | 31,040,000.00 USD | 34,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2424.80` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 1,500,000.00 USD | 2,700,000.00 USD | 844,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 1,180,000.00 USD | 29,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2427.40` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 634,700.00 USD | 89,750.00 USD | 601,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.90` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 25,200,000.00 USD | 15,090,000.00 USD | 18,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.00` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,550,000.00 USD | 1,770,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.20` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 10,380,000.00 USD | 17,060,000.00 USD | 9,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 2,090,000.00 USD | 1,690,000.00 USD | 247,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.50` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 198,530.00 USD | 29,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.20` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,790,000.00 USD | 495,600.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2437.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 777,840.00 USD | 517,090.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.80` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 11,900,000.00 USD | 12,720,000.00 USD | 5,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 1,540,000.00 USD | 2,030,000.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.10` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2443.00` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 1,050,000.00 USD | 644,860.00 USD | 859,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.40` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 8,860,000.00 USD | 15,100,000.00 USD | 13,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 66,330.00 USD | 29,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 126,820.00 USD | 467,480.00 USD | 799,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.70` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 11,380,000.00 USD | 6,510,000.00 USD | 17,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2448.20` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 864,380.00 USD | 325,700.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.80` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 2,340,000.00 USD | 871,330.00 USD | 3,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.00` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 16,710,000.00 USD | 12,450,000.00 USD | 12,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2453.40` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 4,320,000.00 USD | 3,900,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2454.30` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 4,620,000.00 USD | 4,930,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 186,790.00 USD | 30,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2456.00` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 793,240.00 USD | 1,840,000.00 USD | 797,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.60` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2458.60` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 1,400,000.00 USD | 1,230,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.90` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2461.20` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 470,530.00 USD | 46,520.00 USD | 366,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2463.80` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 619,960.00 USD | 829,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.20` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 65,770,000.00 USD | 95,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2466.40` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.50` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2469.00` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 1,250,000.00 USD | 391,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.80` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.10` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 641,630.00 USD | 96,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2476.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.40` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2479.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 26,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.70` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2482.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 525,130.00 USD | 136,500.00 USD | 451,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.00` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2484.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 925,970.00 USD | 1,330,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 1,640,000.00 USD | 98,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2487.20` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2487.30` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2489.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 317,820.00 USD | 30,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.60` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 239,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2492.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 547,850.00 USD | 44,470.00 USD | 357,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.90` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 1,610,000.00 USD | 1,760,000.00 USD | 3,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2495.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 626,840.00 USD | 134,080.00 USD | 33,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 6,380,000.00 USD | 104,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.20` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 2,860,000.00 USD | 4,270,000.00 USD | 6,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2497.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2500.20` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.50` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 1,110,000.00 USD | 1,450,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2502.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.80` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 63,860.00 USD | 1,480,000.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 4,450,000.00 USD | 108,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2505.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2507.10` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2510.40` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2510.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2513.20` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.70` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 700,300.00 USD | 109,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2515.80` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2517.00` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2520.30` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2521.00` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 80,610.00 USD | 121,470.00 USD | 88,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2523.60` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 563,140.00 USD | 494,150.00 USD | 532,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.60` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 5,130,000.00 USD | 114,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2526.20` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 754,970.00 USD | 304,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2526.90` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.20` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.50` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 854,240.00 USD | 115,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2536.80` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2540.10` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2543.40` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 173,450.00 USD | 115,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2546.70` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.00` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.30` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 12,390,000.00 USD | 128,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2556.60` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.90` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2563.20` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 60,800.00 USD | 128,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2566.50` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.80` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2573.10` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 41,530.00 USD | 128,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2576.40` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2579.70` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2583.00` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,520,000.00 USD | 154,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.30` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.60` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.90` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 41,560.00 USD | 154,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2596.20` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2599.50` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2602.80` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 6,100,000.00 USD | 160,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.10` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.40` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.70` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 190,200.00 USD | 161,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2616.00` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2619.30` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2622.60` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2625.00` | 33,170,000.00 USD | 194,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2625.90` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2629.20` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 0.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2632.40` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2635.00` | 942,760.00 USD | 195,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 8,830,000.00 USD | 204,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 26,080,000.00 USD | 230,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 135,770.00 USD | 230,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 4,390,000.00 USD | 234,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 60,700.00 USD | 234,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 6,220,000.00 USD | 240,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 718,530.00 USD | 241,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 335,440.00 USD | 242,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 303,970.00 USD | 242,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 133,470.00 USD | 242,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 887,740.00 USD | 243,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 5,770,000.00 USD | 249,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 28,570.00 USD | 249,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 13,380,000.00 USD | 262,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 57,740.00 USD | 262,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 22,470,000.00 USD | 285,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 3,870,000.00 USD | 288,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 1,160,000.00 USD | 290,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 668,010.00 USD | 290,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 6,160,000.00 USD | 296,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 246,080.00 USD | 297,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 396,550.00 USD | 297,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 73,290.00 USD | 297,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 50,280.00 USD | 297,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 963,300.00 USD | 298,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 1,380,000.00 USD | 300,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 1,700,000.00 USD | 301,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 3,200,000.00 USD | 304,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 26,530,000.00 USD | 331,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 44,150.00 USD | 331,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 573,180.00 USD | 332,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 1,100,000.00 USD | 333,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 3,810,000.00 USD | 336,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 44,270.00 USD | 337,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 145,060.00 USD | 337,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 2,230,000.00 USD | 339,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 525,050.00 USD | 339,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 20,470,000.00 USD | 360,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 842,230.00 USD | 361,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 14,060,000.00 USD | 375,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 19,540.00 USD | 375,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 4,000,000.00 USD | 379,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 2,300,000.00 USD | 381,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 42,140.00 USD | 381,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 3,290,000.00 USD | 384,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 936,010.00 USD | 385,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 1,650,000.00 USD | 387,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 1,900,000.00 USD | 389,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 431,960.00 USD | 389,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 6,370,000.00 USD | 396,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 4,860,000.00 USD | 401,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 29,560,000.00 USD | 430,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 7,040.00 USD | 430,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 859,400.00 USD | 431,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 6,910,000.00 USD | 438,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 3,690,000.00 USD | 442,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 556,050.00 USD | 442,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 156,500.00 USD | 442,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 9,840,000.00 USD | 452,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 9,980,000.00 USD | 462,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 8,460,000.00 USD | 471,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 26,830.00 USD | 471,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 137,380.00 USD | 471,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 13,410,000.00 USD | 484,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 69,380.00 USD | 484,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 321,720.00 USD | 485,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 1,190,000.00 USD | 486,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 2,190,000.00 USD | 488,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 60,520.00 USD | 488,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 4,190,000.00 USD | 492,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 727,550.00 USD | 493,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 64,090.00 USD | 493,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 1,790,000.00 USD | 495,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 1,920.00 USD | 495,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 100,850.00 USD | 495,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 1,600,000.00 USD | 497,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 2,760,000.00 USD | 499,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 39,930.00 USD | 499,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 14,970,000.00 USD | 514,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 395,100.00 USD | 515,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 539,570.00 USD | 515,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 697,920.00 USD | 516,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 585,240.00 USD | 517,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 60,570,000.00 USD | 577,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 50,550.00 USD | 577,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 2,510,000.00 USD | 580,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 934,520.00 USD | 581,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 6,450.00 USD | 581,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 123,270.00 USD | 581,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 272,480.00 USD | 581,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 3,540.00 USD | 581,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 245,580.00 USD | 581,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 178,960.00 USD | 581,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 173,450.00 USD | 582,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 15,230,000.00 USD | 597,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 31,710.00 USD | 597,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 31,860,000.00 USD | 629,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 3,740,000.00 USD | 632,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 469,100.00 USD | 633,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 8,740,000.00 USD | 642,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 463,140.00 USD | 642,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 6,610,000.00 USD | 649,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 367,440.00 USD | 649,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 39,370.00 USD | 649,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 1,030,000.00 USD | 650,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 46,230.00 USD | 650,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 3,950.00 USD | 650,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 132,370.00 USD | 650,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 418,150.00 USD | 651,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 360,230.00 USD | 651,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 1,180,000.00 USD | 652,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 2,850,000.00 USD | 655,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 211,050.00 USD | 655,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 2,850,000.00 USD | 658,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 27,580.00 USD | 658,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 403,860,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 292,660.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 78,710.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 115,590.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 5,840,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 2,720,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 210,430.00 USD | 1,070,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 2,920,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3875.00` | 35,780,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 1,380,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 1,950,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 514,850.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 503,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 64,110,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 4,610.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 42,130.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 101,980.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 57,950.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 566,890.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 1,080,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 360,060.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 627,270.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 81,790.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 557,880.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 90,960.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 7,890.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 1,750,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 154.47 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 474,720.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 9,960.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 425.47 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 107,050.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 2,530,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 233,750.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 173,010.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 710,240.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 85,310.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 1,420,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 235,900.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 872,460.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 85,150,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 6,130,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 81,810.00 USD | 1,280,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 29,040,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 29,900.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 5,310,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 54,650.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 4,060.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 59,170.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 108,920.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 140,630.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 625,670.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 229,040.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 4,100,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 281,060,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 508,850.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 547,470.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 22,390.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 14,060.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 14,520.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 111,660.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 50,550.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 8,540.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4435.00` | 19,310.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4445.00` | 31,110.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4455.00` | 108,470.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4465.00` | 6,560.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4475.00` | 41,200.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `455.00` | 759,540,000.00 USD | 0.00 USD | 72,310.00 USD | `-79.59%` | `158.92` |
| `Live` | `Long` | `465.00` | 759,470,000.00 USD | 0.00 USD | 2,230.00 USD | `-79.14%` | `4.79` |
| `Live` | `Long` | `475.00` | 759,470,000.00 USD | 0.00 USD | 198,670.00 USD | `-78.70%` | `418.25` |
| `Live` | `Long` | `485.00` | 759,270,000.00 USD | 0.00 USD | 98,630.00 USD | `-78.25%` | `203.36` |
| `Live` | `Long` | `495.00` | 759,170,000.00 USD | 0.00 USD | 88,680.00 USD | `-77.80%` | `179.14` |
| `Live` | `Long` | `505.00` | 759,080,000.00 USD | 0.00 USD | 45,950.00 USD | `-77.35%` | `90.99` |
| `Live` | `Long` | `515.00` | 759,040,000.00 USD | 0.00 USD | 1,880,000.00 USD | `-76.90%` | `3,646.84` |
| `Live` | `Long` | `525.00` | 757,160,000.00 USD | 0.00 USD | 26,700.00 USD | `-76.45%` | `50.85` |
| `Live` | `Long` | `535.00` | 757,130,000.00 USD | 0.00 USD | 2,660.00 USD | `-76.00%` | `4.98` |
| `Live` | `Long` | `545.00` | 757,130,000.00 USD | 0.00 USD | 16,450.00 USD | `-75.56%` | `30.19` |
| `Live` | `Long` | `555.00` | 757,110,000.00 USD | 0.00 USD | 190,490.00 USD | `-75.11%` | `343.22` |
| `Live` | `Long` | `565.00` | 756,920,000.00 USD | 0.00 USD | 666,590.00 USD | `-74.66%` | `1,179.81` |
| `Live` | `Long` | `575.00` | 756,250,000.00 USD | 0.00 USD | 44,270.00 USD | `-74.21%` | `77.00` |
| `Live` | `Long` | `585.00` | 756,210,000.00 USD | 0.00 USD | 1,790,000.00 USD | `-73.76%` | `3,059.02` |
| `Live` | `Long` | `595.00` | 754,420,000.00 USD | 0.00 USD | 541,190.00 USD | `-73.31%` | `909.57` |
| `Live` | `Long` | `605.00` | 753,880,000.00 USD | 0.00 USD | 2,990,000.00 USD | `-72.87%` | `4,937.77` |
| `Live` | `Long` | `615.00` | 750,890,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-72.42%` | `1,663.55` |
| `Live` | `Long` | `625.00` | 749,870,000.00 USD | 0.00 USD | 20,060.00 USD | `-71.97%` | `32.10` |
| `Live` | `Long` | `635.00` | 749,850,000.00 USD | 0.00 USD | 7,980.00 USD | `-71.52%` | `12.56` |
| `Live` | `Long` | `645.00` | 749,840,000.00 USD | 0.00 USD | 54,890.00 USD | `-71.07%` | `85.10` |
| `Live` | `Long` | `655.00` | 749,790,000.00 USD | 0.00 USD | 117,840.00 USD | `-70.62%` | `179.90` |
| `Live` | `Long` | `665.00` | 749,670,000.00 USD | 0.00 USD | 165,010.00 USD | `-70.17%` | `248.13` |
| `Live` | `Long` | `675.00` | 749,500,000.00 USD | 0.00 USD | 147,900.00 USD | `-69.73%` | `219.11` |
| `Live` | `Long` | `685.00` | 749,360,000.00 USD | 0.00 USD | 35,730.00 USD | `-69.28%` | `52.16` |
| `Live` | `Long` | `695.00` | 749,320,000.00 USD | 0.00 USD | 66,640.00 USD | `-68.83%` | `95.88` |
| `Live` | `Long` | `705.00` | 749,250,000.00 USD | 0.00 USD | 7,860.00 USD | `-68.38%` | `11.15` |
| `Live` | `Long` | `715.00` | 749,250,000.00 USD | 0.00 USD | 1,140.00 USD | `-67.93%` | `1.60` |
| `Live` | `Long` | `725.00` | 749,240,000.00 USD | 0.00 USD | 397,250.00 USD | `-67.48%` | `547.94` |
| `Live` | `Long` | `735.00` | 748,850,000.00 USD | 0.00 USD | 189,130.00 USD | `-67.03%` | `257.32` |
| `Live` | `Long` | `745.00` | 748,660,000.00 USD | 0.00 USD | 63,060.00 USD | `-66.59%` | `84.64` |
| `Live` | `Long` | `755.00` | 748,590,000.00 USD | 0.00 USD | 28,770.00 USD | `-66.14%` | `38.11` |
| `Live` | `Long` | `765.00` | 748,570,000.00 USD | 0.00 USD | 12,370.00 USD | `-65.69%` | `16.16` |
| `Live` | `Long` | `775.00` | 748,550,000.00 USD | 0.00 USD | 11,490.00 USD | `-65.24%` | `14.83` |
| `Live` | `Long` | `785.00` | 748,540,000.00 USD | 0.00 USD | 91,840.00 USD | `-64.79%` | `117.00` |
| `Live` | `Long` | `795.00` | 748,450,000.00 USD | 0.00 USD | 66,420.00 USD | `-64.34%` | `83.54` |
| `Live` | `Long` | `805.00` | 748,380,000.00 USD | 0.00 USD | 136,320.00 USD | `-63.89%` | `169.35` |
| `Live` | `Long` | `815.00` | 748,250,000.00 USD | 0.00 USD | 436,890.00 USD | `-63.45%` | `536.06` |
| `Live` | `Long` | `825.00` | 747,810,000.00 USD | 0.00 USD | 79,450.00 USD | `-63.00%` | `96.31` |
| `Live` | `Long` | `835.00` | 747,730,000.00 USD | 0.00 USD | 121,540.00 USD | `-62.55%` | `145.55` |
| `Live` | `Long` | `845.00` | 747,610,000.00 USD | 0.00 USD | 96,220.00 USD | `-62.10%` | `113.86` |
| `Live` | `Long` | `855.00` | 747,510,000.00 USD | 0.00 USD | 135,540.00 USD | `-61.65%` | `158.53` |
| `Live` | `Long` | `865.00` | 747,380,000.00 USD | 0.00 USD | 521,630.00 USD | `-61.20%` | `603.04` |
| `Live` | `Long` | `875.00` | 746,860,000.00 USD | 0.00 USD | 53,500.00 USD | `-60.76%` | `61.15` |
| `Live` | `Long` | `885.00` | 746,800,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-60.31%` | `1,247.31` |
| `Live` | `Long` | `895.00` | 745,700,000.00 USD | 0.00 USD | 14,900.00 USD | `-59.86%` | `16.65` |
| `Live` | `Long` | `905.00` | 745,680,000.00 USD | 0.00 USD | 352,150.00 USD | `-59.41%` | `389.12` |
| `Live` | `Long` | `915.00` | 745,330,000.00 USD | 0.00 USD | 161,430.00 USD | `-58.96%` | `176.43` |
| `Live` | `Long` | `925.00` | 745,170,000.00 USD | 0.00 USD | 218,380.00 USD | `-58.51%` | `236.09` |
| `Live` | `Long` | `935.00` | 744,950,000.00 USD | 0.00 USD | 47,430.00 USD | `-58.06%` | `50.72` |
| `Live` | `Long` | `945.00` | 744,900,000.00 USD | 0.00 USD | 227,350.00 USD | `-57.62%` | `240.58` |
| `Live` | `Long` | `955.00` | 744,680,000.00 USD | 0.00 USD | 117,540.00 USD | `-57.17%` | `123.08` |
| `Live` | `Long` | `965.00` | 744,560,000.00 USD | 0.00 USD | 113,520.00 USD | `-56.72%` | `117.63` |
| `Live` | `Long` | `975.00` | 744,450,000.00 USD | 0.00 USD | 81,320.00 USD | `-56.27%` | `83.41` |
| `Live` | `Long` | `985.00` | 744,360,000.00 USD | 0.00 USD | 152,820.00 USD | `-55.82%` | `155.15` |
| `Live` | `Long` | `995.00` | 744,210,000.00 USD | 0.00 USD | 5,740,000.00 USD | `-55.37%` | `5,773.28` |
| `Live` | `Long` | `1005.00` | 738,470,000.00 USD | 0.00 USD | 56,100.00 USD | `-54.92%` | `55.82` |
| `Live` | `Long` | `1015.00` | 738,410,000.00 USD | 0.00 USD | 232,420.00 USD | `-54.48%` | `228.99` |
| `Live` | `Long` | `1025.00` | 738,180,000.00 USD | 0.00 USD | 187,160.00 USD | `-54.03%` | `182.59` |
| `Live` | `Long` | `1035.00` | 737,990,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-53.58%` | `1,365.55` |
| `Live` | `Long` | `1045.00` | 736,580,000.00 USD | 0.00 USD | 401,740.00 USD | `-53.13%` | `384.44` |
| `Live` | `Long` | `1055.00` | 736,180,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-52.68%` | `2,005.92` |
| `Live` | `Long` | `1065.00` | 734,060,000.00 USD | 0.00 USD | 7,740,000.00 USD | `-52.23%` | `7,265.03` |
| `Live` | `Long` | `1075.00` | 726,320,000.00 USD | 0.00 USD | 660,160.00 USD | `-51.79%` | `614.10` |
| `Live` | `Long` | `1085.00` | 725,660,000.00 USD | 0.00 USD | 354,200.00 USD | `-51.34%` | `326.45` |
| `Live` | `Long` | `1095.00` | 725,310,000.00 USD | 0.00 USD | 54,230.00 USD | `-50.89%` | `49.53` |
| `Live` | `Long` | `1105.00` | 725,250,000.00 USD | 0.00 USD | 172,280.00 USD | `-50.44%` | `155.91` |
| `Live` | `Long` | `1115.00` | 725,080,000.00 USD | 0.00 USD | 7,920,000.00 USD | `-49.99%` | `7,103.78` |
| `Live` | `Long` | `1125.00` | 717,160,000.00 USD | 0.00 USD | 158,830.00 USD | `-49.54%` | `141.18` |
| `Live` | `Long` | `1135.00` | 717,000,000.00 USD | 0.00 USD | 475,040.00 USD | `-49.09%` | `418.54` |
| `Live` | `Long` | `1145.00` | 716,530,000.00 USD | 0.00 USD | 196,970.00 USD | `-48.65%` | `172.02` |
| `Live` | `Long` | `1155.00` | 716,330,000.00 USD | 0.00 USD | 1,370,000.00 USD | `-48.20%` | `1,183.06` |
| `Live` | `Long` | `1165.00` | 714,960,000.00 USD | 0.00 USD | 72,300.00 USD | `-47.75%` | `62.06` |
| `Live` | `Long` | `1175.00` | 714,890,000.00 USD | 0.00 USD | 1,510,000.00 USD | `-47.30%` | `1,287.10` |
| `Live` | `Long` | `1185.00` | 713,380,000.00 USD | 0.00 USD | 2,110,000.00 USD | `-46.85%` | `1,782.41` |
| `Live` | `Long` | `1195.00` | 711,270,000.00 USD | 0.00 USD | 218,050.00 USD | `-46.40%` | `182.47` |
| `Live` | `Long` | `1205.00` | 711,050,000.00 USD | 0.00 USD | 185,340.00 USD | `-45.95%` | `153.81` |
| `Live` | `Long` | `1215.00` | 710,860,000.00 USD | 0.00 USD | 2,090,000.00 USD | `-45.51%` | `1,722.09` |
| `Live` | `Long` | `1225.00` | 708,770,000.00 USD | 0.00 USD | 556,370.00 USD | `-45.06%` | `454.18` |
| `Live` | `Long` | `1235.00` | 708,220,000.00 USD | 0.00 USD | 80,420.00 USD | `-44.61%` | `65.12` |
| `Live` | `Long` | `1245.00` | 708,140,000.00 USD | 0.00 USD | 819,550.00 USD | `-44.16%` | `658.27` |
| `Live` | `Long` | `1255.00` | 707,320,000.00 USD | 0.00 USD | 438,130.00 USD | `-43.71%` | `349.11` |
| `Live` | `Long` | `1265.00` | 706,880,000.00 USD | 0.00 USD | 1,690,000.00 USD | `-43.26%` | `1,333.36` |
| `Live` | `Long` | `1275.00` | 705,190,000.00 USD | 0.00 USD | 15,440,000.00 USD | `-42.81%` | `12,106.21` |
| `Live` | `Long` | `1285.00` | 689,760,000.00 USD | 0.00 USD | 279,440.00 USD | `-42.37%` | `217.46` |
| `Live` | `Long` | `1295.00` | 689,480,000.00 USD | 0.00 USD | 371,250.00 USD | `-41.92%` | `286.68` |
| `Live` | `Long` | `1305.00` | 689,100,000.00 USD | 0.00 USD | 268,590.00 USD | `-41.47%` | `205.82` |
| `Live` | `Long` | `1315.00` | 688,840,000.00 USD | 0.00 USD | 221,150.00 USD | `-41.02%` | `168.17` |
| `Live` | `Long` | `1325.00` | 688,610,000.00 USD | 0.00 USD | 506,670.00 USD | `-40.57%` | `382.39` |
| `Live` | `Long` | `1335.00` | 688,110,000.00 USD | 0.00 USD | 291,100.00 USD | `-40.12%` | `218.05` |
| `Live` | `Long` | `1345.00` | 687,820,000.00 USD | 0.00 USD | 5,390,000.00 USD | `-39.68%` | `4,007.93` |
| `Live` | `Long` | `1355.00` | 682,430,000.00 USD | 0.00 USD | 12,260,000.00 USD | `-39.23%` | `9,051.59` |
| `Live` | `Long` | `1365.00` | 670,160,000.00 USD | 0.00 USD | 1,910,000.00 USD | `-38.78%` | `1,400.32` |
| `Live` | `Long` | `1375.00` | 668,250,000.00 USD | 0.00 USD | 638,470.00 USD | `-38.33%` | `464.34` |
| `Live` | `Long` | `1385.00` | 667,610,000.00 USD | 0.00 USD | 9,170,000.00 USD | `-37.88%` | `6,620.74` |
| `Live` | `Long` | `1395.00` | 658,440,000.00 USD | 0.00 USD | 360,520.00 USD | `-37.43%` | `258.43` |
| `Live` | `Long` | `1405.00` | 658,080,000.00 USD | 0.00 USD | 9,980,000.00 USD | `-36.98%` | `7,106.18` |
| `Live` | `Long` | `1415.00` | 648,100,000.00 USD | 0.00 USD | 227,570.00 USD | `-36.54%` | `160.83` |
| `Live` | `Long` | `1425.00` | 647,870,000.00 USD | 0.00 USD | 2,650,000.00 USD | `-36.09%` | `1,861.05` |
| `Live` | `Long` | `1435.00` | 645,220,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-35.64%` | `788.81` |
| `Live` | `Long` | `1445.00` | 644,090,000.00 USD | 0.00 USD | 18,850,000.00 USD | `-35.19%` | `13,045.08` |
| `Live` | `Long` | `1455.00` | 625,240,000.00 USD | 0.00 USD | 335,310.00 USD | `-34.74%` | `230.46` |
| `Live` | `Long` | `1465.00` | 624,900,000.00 USD | 0.00 USD | 1,780,000.00 USD | `-34.29%` | `1,213.40` |
| `Live` | `Long` | `1475.00` | 623,120,000.00 USD | 0.00 USD | 12,160,000.00 USD | `-33.84%` | `8,245.10` |
| `Live` | `Long` | `1485.00` | 610,960,000.00 USD | 0.00 USD | 185,340.00 USD | `-33.40%` | `124.81` |
| `Live` | `Long` | `1495.00` | 610,780,000.00 USD | 0.00 USD | 158,690.00 USD | `-32.95%` | `106.15` |
| `Live` | `Long` | `1505.00` | 610,620,000.00 USD | 0.00 USD | 281,240.00 USD | `-32.50%` | `186.87` |
| `Live` | `Long` | `1515.00` | 610,340,000.00 USD | 0.00 USD | 729,610.00 USD | `-32.05%` | `481.59` |
| `Live` | `Long` | `1525.00` | 609,610,000.00 USD | 0.00 USD | 19,520,000.00 USD | `-31.60%` | `12,799.47` |
| `Live` | `Long` | `1535.00` | 590,090,000.00 USD | 0.00 USD | 989,140.00 USD | `-31.15%` | `644.39` |
| `Live` | `Long` | `1545.00` | 589,100,000.00 USD | 0.00 USD | 20,230,000.00 USD | `-30.71%` | `13,096.58` |
| `Live` | `Long` | `1555.00` | 568,860,000.00 USD | 0.00 USD | 410,620.00 USD | `-30.26%` | `264.07` |
| `Live` | `Long` | `1565.00` | 568,450,000.00 USD | 0.00 USD | 3,430,000.00 USD | `-29.81%` | `2,189.79` |
| `Live` | `Long` | `1575.00` | 565,030,000.00 USD | 0.00 USD | 267,000.00 USD | `-29.36%` | `169.52` |
| `Live` | `Long` | `1585.00` | 564,760,000.00 USD | 0.00 USD | 861,320.00 USD | `-28.91%` | `543.42` |
| `Live` | `Long` | `1595.00` | 563,900,000.00 USD | 0.00 USD | 1,620,000.00 USD | `-28.46%` | `1,016.02` |
| `Live` | `Long` | `1605.00` | 562,280,000.00 USD | 0.00 USD | 21,750,000.00 USD | `-28.01%` | `13,549.66` |
| `Live` | `Long` | `1615.00` | 540,530,000.00 USD | 0.00 USD | 173,560.00 USD | `-27.57%` | `107.47` |
| `Live` | `Long` | `1625.00` | 540,360,000.00 USD | 0.00 USD | 1,730,000.00 USD | `-27.12%` | `1,063.79` |
| `Live` | `Long` | `1635.00` | 538,630,000.00 USD | 0.00 USD | 18,480,000.00 USD | `-26.67%` | `11,302.69` |
| `Live` | `Long` | `1645.00` | 520,150,000.00 USD | 0.00 USD | 38,040,000.00 USD | `-26.22%` | `23,127.61` |
| `Live` | `Long` | `1655.00` | 482,100,000.00 USD | 0.00 USD | 925,200.00 USD | `-25.77%` | `559.04` |
| `Live` | `Long` | `1665.00` | 481,180,000.00 USD | 0.00 USD | 1,380,000.00 USD | `-25.32%` | `827.67` |
| `Live` | `Long` | `1675.00` | 479,800,000.00 USD | 0.00 USD | 12,260,000.00 USD | `-24.87%` | `7,317.76` |
| `Live` | `Long` | `1685.00` | 467,540,000.00 USD | 0.00 USD | 606,650.00 USD | `-24.43%` | `360.03` |
| `Live` | `Long` | `1695.00` | 466,940,000.00 USD | 0.00 USD | 417,600.00 USD | `-23.98%` | `246.37` |
| `Live` | `Long` | `1705.00` | 466,520,000.00 USD | 0.00 USD | 1,230,000.00 USD | `-23.53%` | `719.40` |
| `Live` | `Long` | `1715.00` | 465,290,000.00 USD | 0.00 USD | 575,210.00 USD | `-23.08%` | `335.40` |
| `Live` | `Long` | `1725.00` | 464,720,000.00 USD | 0.00 USD | 36,130,000.00 USD | `-22.63%` | `20,946.31` |
| `Live` | `Long` | `1735.00` | 428,580,000.00 USD | 0.00 USD | 1,540,000.00 USD | `-22.18%` | `884.90` |
| `Live` | `Long` | `1745.00` | 427,050,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-21.73%` | `748.72` |
| `Live` | `Long` | `1755.00` | 425,740,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-21.29%` | `652.04` |
| `Live` | `Long` | `1765.00` | 424,600,000.00 USD | 0.00 USD | 49,080,000.00 USD | `-20.84%` | `27,809.70` |
| `Live` | `Long` | `1775.00` | 375,510,000.00 USD | 0.00 USD | 734,410.00 USD | `-20.39%` | `413.75` |
| `Live` | `Long` | `1785.00` | 374,780,000.00 USD | 0.00 USD | 61,370,000.00 USD | `-19.94%` | `34,378.83` |
| `Live` | `Long` | `1795.00` | 313,410,000.00 USD | 0.00 USD | 495,870.00 USD | `-19.49%` | `276.25` |
| `Live` | `Long` | `1805.00` | 312,920,000.00 USD | 0.00 USD | 3,280,000.00 USD | `-19.04%` | `1,818.39` |
| `Live` | `Long` | `1815.00` | 309,630,000.00 USD | 0.00 USD | 805,460.00 USD | `-18.60%` | `443.78` |
| `Live` | `Long` | `1825.00` | 308,830,000.00 USD | 0.00 USD | 831,850.00 USD | `-18.15%` | `455.81` |
| `Live` | `Long` | `1835.00` | 308,000,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-17.70%` | `616.74` |
| `Live` | `Long` | `1845.00` | 306,870,000.00 USD | 0.00 USD | 27,870,000.00 USD | `-17.25%` | `15,105.40` |
| `Live` | `Long` | `1855.00` | 279,000,000.00 USD | 0.00 USD | 1,680,000.00 USD | `-16.80%` | `902.99` |
| `Live` | `Long` | `1865.00` | 277,320,000.00 USD | 0.00 USD | 3,380,000.00 USD | `-16.35%` | `1,812.38` |
| `Live` | `Long` | `1875.00` | 273,940,000.00 USD | 0.00 USD | 8,890,000.00 USD | `-15.90%` | `4,743.58` |
| `Live` | `Long` | `1885.00` | 265,050,000.00 USD | 0.00 USD | 5,830,000.00 USD | `-15.46%` | `3,091.11` |
| `Live` | `Long` | `1895.00` | 259,220,000.00 USD | 0.00 USD | 775,090.00 USD | `-15.01%` | `409.02` |
| `Live` | `Long` | `1905.00` | 258,450,000.00 USD | 0.00 USD | 490,530.00 USD | `-14.56%` | `257.49` |
| `Live` | `Long` | `1915.00` | 257,950,000.00 USD | 0.00 USD | 18,290,000.00 USD | `-14.11%` | `9,549.13` |
| `Live` | `Long` | `1925.00` | 239,670,000.00 USD | 0.00 USD | 16,340,000.00 USD | `-13.66%` | `8,487.98` |
| `Live` | `Long` | `1935.00` | 223,330,000.00 USD | 0.00 USD | 4,460,000.00 USD | `-13.21%` | `2,303.52` |
| `Live` | `Long` | `1945.00` | 218,870,000.00 USD | 0.00 USD | 1,690,000.00 USD | `-12.76%` | `868.61` |
| `Live` | `Long` | `1955.00` | 217,180,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-12.32%` | `658.39` |
| `Live` | `Long` | `1965.00` | 215,890,000.00 USD | 0.00 USD | 2,730,000.00 USD | `-11.87%` | `1,388.04` |
| `Live` | `Long` | `1975.00` | 213,170,000.00 USD | 0.00 USD | 1,950,000.00 USD | `-11.42%` | `988.92` |
| `Live` | `Long` | `1985.00` | 211,210,000.00 USD | 0.00 USD | 5,060,000.00 USD | `-10.97%` | `2,551.23` |
| `Live` | `Long` | `1995.00` | 206,150,000.00 USD | 0.00 USD | 1,560,000.00 USD | `-10.52%` | `784.10` |
| `Live` | `Long` | `2005.00` | 204,590,000.00 USD | 0.00 USD | 2,090,000.00 USD | `-10.07%` | `1,040.05` |
| `Live` | `Long` | `2015.00` | 202,500,000.00 USD | 0.00 USD | 5,730,000.00 USD | `-9.63%` | `2,845.12` |
| `Live` | `Long` | `2025.00` | 196,770,000.00 USD | 0.00 USD | 2,100,000.00 USD | `-9.18%` | `1,036.53` |
| `Live` | `Long` | `2035.00` | 194,670,000.00 USD | 0.00 USD | 1,080,000.00 USD | `-8.73%` | `529.82` |
| `Live` | `Long` | `2045.00` | 193,590,000.00 USD | 0.00 USD | 2,000,000.00 USD | `-8.28%` | `978.79` |
| `Live` | `Long` | `2055.00` | 191,590,000.00 USD | 0.00 USD | 5,940,000.00 USD | `-7.83%` | `2,892.90` |
| `Live` | `Long` | `2065.00` | 185,640,000.00 USD | 0.00 USD | 13,860,000.00 USD | `-7.38%` | `6,714.08` |
| `Live` | `Long` | `2075.00` | 171,780,000.00 USD | 0.00 USD | 2,720,000.00 USD | `-6.93%` | `1,312.25` |
| `Live` | `Long` | `2085.00` | 169,060,000.00 USD | 0.00 USD | 13,600,000.00 USD | `-6.49%` | `6,524.51` |
| `Live` | `Long` | `2095.00` | 155,450,000.00 USD | 0.00 USD | 1,380,000.00 USD | `-6.04%` | `657.96` |
| `Live` | `Long` | `2105.00` | 154,070,000.00 USD | 0.00 USD | 2,280,000.00 USD | `-5.59%` | `1,083.78` |
| `Live` | `Long` | `2115.00` | 151,790,000.00 USD | 0.00 USD | 2,910,000.00 USD | `-5.14%` | `1,375.04` |
| `Live` | `Long` | `2125.00` | 148,880,000.00 USD | 0.00 USD | 123,240,000.00 USD | `-4.69%` | `57,997.47` |
| `Live` | `Long` | `2135.00` | 25,640,000.00 USD | 0.00 USD | 4,840,000.00 USD | `-4.24%` | `2,266.48` |
| `Live` | `Long` | `2145.00` | 20,800,000.00 USD | 0.00 USD | 5,020,000.00 USD | `-3.79%` | `2,339.37` |
| `Live` | `Long` | `2155.00` | 15,780,000.00 USD | 0.00 USD | 3,970,000.00 USD | `-3.35%` | `1,844.11` |
| `Live` | `Long` | `2165.00` | 11,810,000.00 USD | 0.00 USD | 5,390,000.00 USD | `-2.90%` | `2,491.34` |
| `Live` | `Long` | `2175.00` | 6,420,000.00 USD | 0.00 USD | 5,680,000.00 USD | `-2.45%` | `2,613.45` |
| `Live` | `Long` | `2185.00` | 731,220.00 USD | 0.00 USD | 618,490.00 USD | `-2.00%` | `283.06` |
| `Live` | `Long` | `2195.00` | 112,730.00 USD | 0.00 USD | 107,420.00 USD | `-1.55%` | `48.94` |
| `Live` | `Long` | `2205.00` | 5,310.00 USD | 0.00 USD | 5,310.00 USD | `-1.10%` | `2.41` |
| `Live` | `Short` | `2235.00` | 14,960.00 USD | 14,960.00 USD | 0.00 USD | `+0.24%` | `6.69` |
| `Live` | `Short` | `2245.00` | 1,810,000.00 USD | 1,800,000.00 USD | 0.00 USD | `+0.69%` | `800.01` |
| `Live` | `Short` | `2255.00` | 4,780,000.00 USD | 2,970,000.00 USD | 0.00 USD | `+1.14%` | `1,316.55` |
| `Live` | `Short` | `2265.00` | 7,090,000.00 USD | 2,310,000.00 USD | 0.00 USD | `+1.59%` | `1,017.91` |
| `Live` | `Short` | `2275.00` | 7,360,000.00 USD | 276,460.00 USD | 0.00 USD | `+2.04%` | `121.52` |
| `Live` | `Short` | `2285.00` | 8,130,000.00 USD | 767,790.00 USD | 0.00 USD | `+2.48%` | `336.01` |
| `Live` | `Short` | `2295.00` | 11,970,000.00 USD | 3,840,000.00 USD | 0.00 USD | `+2.93%` | `1,671.21` |
| `Live` | `Short` | `2305.00` | 12,230,000.00 USD | 266,780.00 USD | 0.00 USD | `+3.38%` | `115.74` |
| `Live` | `Short` | `2315.00` | 13,240,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+3.83%` | `436.72` |
| `Live` | `Short` | `2325.00` | 15,240,000.00 USD | 1,990,000.00 USD | 0.00 USD | `+4.28%` | `857.57` |
| `Live` | `Short` | `2335.00` | 16,070,000.00 USD | 828,820.00 USD | 0.00 USD | `+4.73%` | `354.95` |
| `Live` | `Short` | `2345.00` | 16,180,000.00 USD | 109,700.00 USD | 0.00 USD | `+5.18%` | `46.78` |
| `Live` | `Short` | `2355.00` | 17,400,000.00 USD | 1,220,000.00 USD | 0.00 USD | `+5.62%` | `520.12` |
| `Live` | `Short` | `2365.00` | 21,280,000.00 USD | 3,880,000.00 USD | 0.00 USD | `+6.07%` | `1,640.01` |
| `Live` | `Short` | `2375.00` | 22,170,000.00 USD | 894,650.00 USD | 0.00 USD | `+6.52%` | `376.69` |
| `Live` | `Short` | `2385.00` | 27,940,000.00 USD | 5,770,000.00 USD | 0.00 USD | `+6.97%` | `2,419.12` |
| `Live` | `Short` | `2395.00` | 28,100,000.00 USD | 155,990.00 USD | 0.00 USD | `+7.42%` | `65.13` |
| `Live` | `Short` | `2405.00` | 28,290,000.00 USD | 190,970.00 USD | 0.00 USD | `+7.87%` | `79.41` |
| `Live` | `Short` | `2415.00` | 28,450,000.00 USD | 164,460.00 USD | 0.00 USD | `+8.32%` | `68.10` |
| `Live` | `Short` | `2425.00` | 29,630,000.00 USD | 1,180,000.00 USD | 0.00 USD | `+8.76%` | `485.23` |
| `Live` | `Short` | `2435.00` | 29,830,000.00 USD | 198,530.00 USD | 0.00 USD | `+9.21%` | `81.53` |
| `Live` | `Short` | `2445.00` | 29,900,000.00 USD | 66,330.00 USD | 0.00 USD | `+9.66%` | `27.13` |
| `Live` | `Short` | `2455.00` | 30,080,000.00 USD | 186,790.00 USD | 0.00 USD | `+10.11%` | `76.09` |
| `Live` | `Short` | `2465.00` | 95,850,000.00 USD | 65,770,000.00 USD | 0.00 USD | `+10.56%` | `26,680.74` |
| `Live` | `Short` | `2475.00` | 96,490,000.00 USD | 641,630.00 USD | 0.00 USD | `+11.01%` | `259.24` |
| `Live` | `Short` | `2485.00` | 98,130,000.00 USD | 1,640,000.00 USD | 0.00 USD | `+11.45%` | `659.67` |
| `Live` | `Short` | `2495.00` | 104,510,000.00 USD | 6,380,000.00 USD | 0.00 USD | `+11.90%` | `2,558.44` |
| `Live` | `Short` | `2505.00` | 108,960,000.00 USD | 4,450,000.00 USD | 0.00 USD | `+12.35%` | `1,774.79` |
| `Live` | `Short` | `2515.00` | 109,660,000.00 USD | 700,300.00 USD | 0.00 USD | `+12.80%` | `278.45` |
| `Live` | `Short` | `2525.00` | 114,790,000.00 USD | 5,130,000.00 USD | 0.00 USD | `+13.25%` | `2,030.53` |
| `Live` | `Short` | `2535.00` | 115,640,000.00 USD | 854,240.00 USD | 0.00 USD | `+13.70%` | `336.98` |
| `Live` | `Short` | `2545.00` | 115,820,000.00 USD | 173,450.00 USD | 0.00 USD | `+14.15%` | `68.15` |
| `Live` | `Short` | `2555.00` | 128,200,000.00 USD | 12,390,000.00 USD | 0.00 USD | `+14.59%` | `4,848.05` |
| `Live` | `Short` | `2565.00` | 128,260,000.00 USD | 60,800.00 USD | 0.00 USD | `+15.04%` | `23.70` |
| `Live` | `Short` | `2575.00` | 128,300,000.00 USD | 41,530.00 USD | 0.00 USD | `+15.49%` | `16.13` |
| `Live` | `Short` | `2585.00` | 154,820,000.00 USD | 26,520,000.00 USD | 0.00 USD | `+15.94%` | `10,257.58` |
| `Live` | `Short` | `2595.00` | 154,860,000.00 USD | 41,560.00 USD | 0.00 USD | `+16.39%` | `16.02` |
| `Live` | `Short` | `2605.00` | 160,960,000.00 USD | 6,100,000.00 USD | 0.00 USD | `+16.84%` | `2,339.77` |
| `Live` | `Short` | `2615.00` | 161,150,000.00 USD | 190,200.00 USD | 0.00 USD | `+17.29%` | `72.73` |
| `Live` | `Short` | `2625.00` | 194,320,000.00 USD | 33,170,000.00 USD | 0.00 USD | `+17.73%` | `12,636.25` |
| `Live` | `Short` | `2635.00` | 195,260,000.00 USD | 942,760.00 USD | 0.00 USD | `+18.18%` | `357.78` |
| `Live` | `Short` | `2645.00` | 204,090,000.00 USD | 8,830,000.00 USD | 0.00 USD | `+18.63%` | `3,339.12` |
| `Live` | `Short` | `2655.00` | 230,170,000.00 USD | 26,080,000.00 USD | 0.00 USD | `+19.08%` | `9,822.32` |
| `Live` | `Short` | `2665.00` | 230,310,000.00 USD | 135,770.00 USD | 0.00 USD | `+19.53%` | `50.95` |
| `Live` | `Short` | `2675.00` | 234,690,000.00 USD | 4,390,000.00 USD | 0.00 USD | `+19.98%` | `1,639.29` |
| `Live` | `Short` | `2685.00` | 234,750,000.00 USD | 60,700.00 USD | 0.00 USD | `+20.43%` | `22.61` |
| `Live` | `Short` | `2695.00` | 240,970,000.00 USD | 6,220,000.00 USD | 0.00 USD | `+20.87%` | `2,308.75` |
| `Live` | `Short` | `2705.00` | 241,690,000.00 USD | 718,530.00 USD | 0.00 USD | `+21.32%` | `265.63` |
| `Live` | `Short` | `2715.00` | 242,030,000.00 USD | 335,440.00 USD | 0.00 USD | `+21.77%` | `123.55` |
| `Live` | `Short` | `2725.00` | 242,330,000.00 USD | 303,970.00 USD | 0.00 USD | `+22.22%` | `111.55` |
| `Live` | `Short` | `2735.00` | 242,470,000.00 USD | 133,470.00 USD | 0.00 USD | `+22.67%` | `48.80` |
| `Live` | `Short` | `2745.00` | 243,350,000.00 USD | 887,740.00 USD | 0.00 USD | `+23.12%` | `323.40` |
| `Live` | `Short` | `2755.00` | 249,130,000.00 USD | 5,770,000.00 USD | 0.00 USD | `+23.56%` | `2,094.89` |
| `Live` | `Short` | `2765.00` | 249,150,000.00 USD | 28,570.00 USD | 0.00 USD | `+24.01%` | `10.33` |
| `Live` | `Short` | `2775.00` | 262,530,000.00 USD | 13,380,000.00 USD | 0.00 USD | `+24.46%` | `4,821.07` |
| `Live` | `Short` | `2785.00` | 262,590,000.00 USD | 57,740.00 USD | 0.00 USD | `+24.91%` | `20.73` |
| `Live` | `Short` | `2795.00` | 285,060,000.00 USD | 22,470,000.00 USD | 0.00 USD | `+25.36%` | `8,038.21` |
| `Live` | `Short` | `2805.00` | 288,920,000.00 USD | 3,870,000.00 USD | 0.00 USD | `+25.81%` | `1,378.27` |
| `Live` | `Short` | `2815.00` | 290,080,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+26.26%` | `412.30` |
| `Live` | `Short` | `2825.00` | 290,750,000.00 USD | 668,010.00 USD | 0.00 USD | `+26.70%` | `236.46` |
| `Live` | `Short` | `2835.00` | 296,920,000.00 USD | 6,160,000.00 USD | 0.00 USD | `+27.15%` | `2,174.33` |
| `Live` | `Short` | `2845.00` | 297,160,000.00 USD | 246,080.00 USD | 0.00 USD | `+27.60%` | `86.50` |
| `Live` | `Short` | `2855.00` | 297,560,000.00 USD | 396,550.00 USD | 0.00 USD | `+28.05%` | `138.90` |
| `Live` | `Short` | `2865.00` | 297,630,000.00 USD | 73,290.00 USD | 0.00 USD | `+28.50%` | `25.58` |
| `Live` | `Short` | `2875.00` | 297,680,000.00 USD | 50,280.00 USD | 0.00 USD | `+28.95%` | `17.49` |
| `Live` | `Short` | `2885.00` | 298,650,000.00 USD | 963,300.00 USD | 0.00 USD | `+29.40%` | `333.90` |
| `Live` | `Short` | `2895.00` | 300,020,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+29.84%` | `476.62` |
| `Live` | `Short` | `2905.00` | 301,730,000.00 USD | 1,700,000.00 USD | 0.00 USD | `+30.29%` | `585.57` |
| `Live` | `Short` | `2915.00` | 304,930,000.00 USD | 3,200,000.00 USD | 0.00 USD | `+30.74%` | `1,098.53` |
| `Live` | `Short` | `2925.00` | 331,460,000.00 USD | 26,530,000.00 USD | 0.00 USD | `+31.19%` | `9,070.32` |
| `Live` | `Short` | `2935.00` | 331,500,000.00 USD | 44,150.00 USD | 0.00 USD | `+31.64%` | `15.04` |
| `Live` | `Short` | `2945.00` | 332,080,000.00 USD | 573,180.00 USD | 0.00 USD | `+32.09%` | `194.63` |
| `Live` | `Short` | `2955.00` | 333,170,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+32.53%` | `371.35` |
| `Live` | `Short` | `2965.00` | 336,980,000.00 USD | 3,810,000.00 USD | 0.00 USD | `+32.98%` | `1,284.32` |
| `Live` | `Short` | `2975.00` | 337,030,000.00 USD | 44,270.00 USD | 0.00 USD | `+33.43%` | `14.88` |
| `Live` | `Short` | `2985.00` | 337,170,000.00 USD | 145,060.00 USD | 0.00 USD | `+33.88%` | `48.59` |
| `Live` | `Short` | `2995.00` | 339,400,000.00 USD | 2,230,000.00 USD | 0.00 USD | `+34.33%` | `745.91` |
| `Live` | `Short` | `3005.00` | 339,930,000.00 USD | 525,050.00 USD | 0.00 USD | `+34.78%` | `174.73` |
| `Live` | `Short` | `3015.00` | 360,400,000.00 USD | 20,470,000.00 USD | 0.00 USD | `+35.23%` | `6,790.86` |
| `Live` | `Short` | `3025.00` | 361,250,000.00 USD | 842,230.00 USD | 0.00 USD | `+35.67%` | `278.42` |
| `Live` | `Short` | `3035.00` | 375,300,000.00 USD | 14,060,000.00 USD | 0.00 USD | `+36.12%` | `4,631.24` |
| `Live` | `Short` | `3045.00` | 375,320,000.00 USD | 19,540.00 USD | 0.00 USD | `+36.57%` | `6.42` |
| `Live` | `Short` | `3055.00` | 379,330,000.00 USD | 4,000,000.00 USD | 0.00 USD | `+37.02%` | `1,310.70` |
| `Live` | `Short` | `3065.00` | 381,630,000.00 USD | 2,300,000.00 USD | 0.00 USD | `+37.47%` | `752.00` |
| `Live` | `Short` | `3075.00` | 381,670,000.00 USD | 42,140.00 USD | 0.00 USD | `+37.92%` | `13.70` |
| `Live` | `Short` | `3085.00` | 384,960,000.00 USD | 3,290,000.00 USD | 0.00 USD | `+38.37%` | `1,065.07` |
| `Live` | `Short` | `3095.00` | 385,890,000.00 USD | 936,010.00 USD | 0.00 USD | `+38.81%` | `302.43` |
| `Live` | `Short` | `3105.00` | 387,550,000.00 USD | 1,650,000.00 USD | 0.00 USD | `+39.26%` | `532.75` |
| `Live` | `Short` | `3115.00` | 389,450,000.00 USD | 1,900,000.00 USD | 0.00 USD | `+39.71%` | `609.45` |
| `Live` | `Short` | `3125.00` | 389,880,000.00 USD | 431,960.00 USD | 0.00 USD | `+40.16%` | `138.23` |
| `Live` | `Short` | `3135.00` | 396,250,000.00 USD | 6,370,000.00 USD | 0.00 USD | `+40.61%` | `2,031.12` |
| `Live` | `Short` | `3145.00` | 401,100,000.00 USD | 4,860,000.00 USD | 0.00 USD | `+41.06%` | `1,544.24` |
| `Live` | `Short` | `3155.00` | 430,670,000.00 USD | 29,560,000.00 USD | 0.00 USD | `+41.51%` | `9,370.55` |
| `Live` | `Short` | `3165.00` | 430,670,000.00 USD | 7,040.00 USD | 0.00 USD | `+41.95%` | `2.22` |
| `Live` | `Short` | `3175.00` | 431,530,000.00 USD | 859,400.00 USD | 0.00 USD | `+42.40%` | `270.68` |
| `Live` | `Short` | `3185.00` | 438,450,000.00 USD | 6,910,000.00 USD | 0.00 USD | `+42.85%` | `2,169.99` |
| `Live` | `Short` | `3195.00` | 442,140,000.00 USD | 3,690,000.00 USD | 0.00 USD | `+43.30%` | `1,156.01` |
| `Live` | `Short` | `3205.00` | 442,700,000.00 USD | 556,050.00 USD | 0.00 USD | `+43.75%` | `173.49` |
| `Live` | `Short` | `3215.00` | 442,850,000.00 USD | 156,500.00 USD | 0.00 USD | `+44.20%` | `48.68` |
| `Live` | `Short` | `3225.00` | 452,700,000.00 USD | 9,840,000.00 USD | 0.00 USD | `+44.64%` | `3,052.67` |
| `Live` | `Short` | `3235.00` | 462,680,000.00 USD | 9,980,000.00 USD | 0.00 USD | `+45.09%` | `3,086.34` |
| `Live` | `Short` | `3245.00` | 471,150,000.00 USD | 8,460,000.00 USD | 0.00 USD | `+45.54%` | `2,608.61` |
| `Live` | `Short` | `3255.00` | 471,170,000.00 USD | 26,830.00 USD | 0.00 USD | `+45.99%` | `8.24` |
| `Live` | `Short` | `3265.00` | 471,310,000.00 USD | 137,380.00 USD | 0.00 USD | `+46.44%` | `42.08` |
| `Live` | `Short` | `3275.00` | 484,720,000.00 USD | 13,410,000.00 USD | 0.00 USD | `+46.89%` | `4,095.83` |
| `Live` | `Short` | `3285.00` | 484,790,000.00 USD | 69,380.00 USD | 0.00 USD | `+47.34%` | `21.12` |
| `Live` | `Short` | `3295.00` | 485,110,000.00 USD | 321,720.00 USD | 0.00 USD | `+47.78%` | `97.64` |
| `Live` | `Short` | `3305.00` | 486,300,000.00 USD | 1,190,000.00 USD | 0.00 USD | `+48.23%` | `359.09` |
| `Live` | `Short` | `3315.00` | 488,490,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+48.68%` | `659.46` |
| `Live` | `Short` | `3325.00` | 488,550,000.00 USD | 60,520.00 USD | 0.00 USD | `+49.13%` | `18.20` |
| `Live` | `Short` | `3335.00` | 492,740,000.00 USD | 4,190,000.00 USD | 0.00 USD | `+49.58%` | `1,255.39` |
| `Live` | `Short` | `3345.00` | 493,460,000.00 USD | 727,550.00 USD | 0.00 USD | `+50.03%` | `217.50` |
| `Live` | `Short` | `3355.00` | 493,530,000.00 USD | 64,090.00 USD | 0.00 USD | `+50.48%` | `19.10` |
| `Live` | `Short` | `3365.00` | 495,320,000.00 USD | 1,790,000.00 USD | 0.00 USD | `+50.92%` | `531.66` |
| `Live` | `Short` | `3375.00` | 495,320,000.00 USD | 1,920.00 USD | 0.00 USD | `+51.37%` | `0.57` |
| `Live` | `Short` | `3385.00` | 495,420,000.00 USD | 100,850.00 USD | 0.00 USD | `+51.82%` | `29.79` |
| `Live` | `Short` | `3395.00` | 497,020,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+52.27%` | `472.54` |
| `Live` | `Short` | `3405.00` | 499,780,000.00 USD | 2,760,000.00 USD | 0.00 USD | `+52.72%` | `810.94` |
| `Live` | `Short` | `3415.00` | 499,820,000.00 USD | 39,930.00 USD | 0.00 USD | `+53.17%` | `11.69` |
| `Live` | `Short` | `3425.00` | 514,800,000.00 USD | 14,970,000.00 USD | 0.00 USD | `+53.61%` | `4,371.38` |
| `Live` | `Short` | `3435.00` | 515,190,000.00 USD | 395,100.00 USD | 0.00 USD | `+54.06%` | `115.02` |
| `Live` | `Short` | `3445.00` | 515,730,000.00 USD | 539,570.00 USD | 0.00 USD | `+54.51%` | `156.62` |
| `Live` | `Short` | `3455.00` | 516,430,000.00 USD | 697,920.00 USD | 0.00 USD | `+54.96%` | `202.00` |
| `Live` | `Short` | `3465.00` | 517,010,000.00 USD | 585,240.00 USD | 0.00 USD | `+55.41%` | `168.90` |
| `Live` | `Short` | `3475.00` | 577,590,000.00 USD | 60,570,000.00 USD | 0.00 USD | `+55.86%` | `17,431.48` |
| `Live` | `Short` | `3485.00` | 577,640,000.00 USD | 50,550.00 USD | 0.00 USD | `+56.31%` | `14.50` |
| `Live` | `Short` | `3495.00` | 580,140,000.00 USD | 2,510,000.00 USD | 0.00 USD | `+56.75%` | `716.87` |
| `Live` | `Short` | `3505.00` | 581,080,000.00 USD | 934,520.00 USD | 0.00 USD | `+57.20%` | `266.62` |
| `Live` | `Short` | `3515.00` | 581,090,000.00 USD | 6,450.00 USD | 0.00 USD | `+57.65%` | `1.84` |
| `Live` | `Short` | `3525.00` | 581,210,000.00 USD | 123,270.00 USD | 0.00 USD | `+58.10%` | `34.97` |
| `Live` | `Short` | `3535.00` | 581,480,000.00 USD | 272,480.00 USD | 0.00 USD | `+58.55%` | `77.08` |
| `Live` | `Short` | `3545.00` | 581,480,000.00 USD | 3,540.00 USD | 0.00 USD | `+59.00%` | `1.00` |
| `Live` | `Short` | `3555.00` | 581,730,000.00 USD | 245,580.00 USD | 0.00 USD | `+59.45%` | `69.08` |
| `Live` | `Short` | `3565.00` | 581,910,000.00 USD | 178,960.00 USD | 0.00 USD | `+59.89%` | `50.20` |
| `Live` | `Short` | `3575.00` | 582,080,000.00 USD | 173,450.00 USD | 0.00 USD | `+60.34%` | `48.52` |
| `Live` | `Short` | `3585.00` | 597,310,000.00 USD | 15,230,000.00 USD | 0.00 USD | `+60.79%` | `4,246.92` |
| `Live` | `Short` | `3595.00` | 597,340,000.00 USD | 31,710.00 USD | 0.00 USD | `+61.24%` | `8.82` |
| `Live` | `Short` | `3605.00` | 629,200,000.00 USD | 31,860,000.00 USD | 0.00 USD | `+61.69%` | `8,837.71` |
| `Live` | `Short` | `3615.00` | 632,940,000.00 USD | 3,740,000.00 USD | 0.00 USD | `+62.14%` | `1,034.22` |
| `Live` | `Short` | `3625.00` | 633,410,000.00 USD | 469,100.00 USD | 0.00 USD | `+62.59%` | `129.41` |
| `Live` | `Short` | `3635.00` | 642,150,000.00 USD | 8,740,000.00 USD | 0.00 USD | `+63.03%` | `2,405.67` |
| `Live` | `Short` | `3645.00` | 642,610,000.00 USD | 463,140.00 USD | 0.00 USD | `+63.48%` | `127.06` |
| `Live` | `Short` | `3655.00` | 649,230,000.00 USD | 6,610,000.00 USD | 0.00 USD | `+63.93%` | `1,808.73` |
| `Live` | `Short` | `3665.00` | 649,590,000.00 USD | 367,440.00 USD | 0.00 USD | `+64.38%` | `100.26` |
| `Live` | `Short` | `3675.00` | 649,630,000.00 USD | 39,370.00 USD | 0.00 USD | `+64.83%` | `10.71` |
| `Live` | `Short` | `3685.00` | 650,660,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+65.28%` | `280.18` |
| `Live` | `Short` | `3695.00` | 650,710,000.00 USD | 46,230.00 USD | 0.00 USD | `+65.72%` | `12.51` |
| `Live` | `Short` | `3705.00` | 650,720,000.00 USD | 3,950.00 USD | 0.00 USD | `+66.17%` | `1.07` |
| `Live` | `Short` | `3715.00` | 650,850,000.00 USD | 132,370.00 USD | 0.00 USD | `+66.62%` | `35.63` |
| `Live` | `Short` | `3725.00` | 651,270,000.00 USD | 418,150.00 USD | 0.00 USD | `+67.07%` | `112.25` |
| `Live` | `Short` | `3735.00` | 651,630,000.00 USD | 360,230.00 USD | 0.00 USD | `+67.52%` | `96.45` |
| `Live` | `Short` | `3745.00` | 652,800,000.00 USD | 1,180,000.00 USD | 0.00 USD | `+67.97%` | `314.41` |
| `Live` | `Short` | `3755.00` | 655,650,000.00 USD | 2,850,000.00 USD | 0.00 USD | `+68.42%` | `759.19` |
| `Live` | `Short` | `3765.00` | 655,870,000.00 USD | 211,050.00 USD | 0.00 USD | `+68.86%` | `56.06` |
| `Live` | `Short` | `3775.00` | 658,710,000.00 USD | 2,850,000.00 USD | 0.00 USD | `+69.31%` | `754.67` |
| `Live` | `Short` | `3785.00` | 658,740,000.00 USD | 27,580.00 USD | 0.00 USD | `+69.76%` | `7.29` |
| `Live` | `Short` | `3795.00` | 1,060,000,000.00 USD | 403,860,000.00 USD | 0.00 USD | `+70.21%` | `106,419.56` |
| `Live` | `Short` | `3805.00` | 1,060,000,000.00 USD | 292,660.00 USD | 0.00 USD | `+70.66%` | `76.92` |
| `Live` | `Short` | `3815.00` | 1,060,000,000.00 USD | 78,710.00 USD | 0.00 USD | `+71.11%` | `20.63` |
| `Live` | `Short` | `3825.00` | 1,060,000,000.00 USD | 115,590.00 USD | 0.00 USD | `+71.56%` | `30.22` |
| `Live` | `Short` | `3835.00` | 1,070,000,000.00 USD | 5,840,000.00 USD | 0.00 USD | `+72.00%` | `1,522.33` |
| `Live` | `Short` | `3845.00` | 1,070,000,000.00 USD | 2,720,000.00 USD | 0.00 USD | `+72.45%` | `708.00` |
| `Live` | `Short` | `3855.00` | 1,070,000,000.00 USD | 210,430.00 USD | 0.00 USD | `+72.90%` | `54.59` |
| `Live` | `Short` | `3865.00` | 1,070,000,000.00 USD | 2,920,000.00 USD | 0.00 USD | `+73.35%` | `756.35` |
| `Live` | `Short` | `3875.00` | 1,110,000,000.00 USD | 35,780,000.00 USD | 0.00 USD | `+73.80%` | `9,234.49` |
| `Live` | `Short` | `3885.00` | 1,110,000,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+74.25%` | `354.42` |
| `Live` | `Short` | `3895.00` | 1,110,000,000.00 USD | 1,950,000.00 USD | 0.00 USD | `+74.70%` | `499.88` |
| `Live` | `Short` | `3905.00` | 1,110,000,000.00 USD | 514,850.00 USD | 0.00 USD | `+75.14%` | `131.84` |
| `Live` | `Short` | `3915.00` | 1,110,000,000.00 USD | 503,000.00 USD | 0.00 USD | `+75.59%` | `128.48` |
| `Live` | `Short` | `3925.00` | 1,180,000,000.00 USD | 64,110,000.00 USD | 0.00 USD | `+76.04%` | `16,332.74` |
| `Live` | `Short` | `3935.00` | 1,180,000,000.00 USD | 4,610.00 USD | 0.00 USD | `+76.49%` | `1.17` |
| `Live` | `Short` | `3945.00` | 1,180,000,000.00 USD | 42,130.00 USD | 0.00 USD | `+76.94%` | `10.68` |
| `Live` | `Short` | `3955.00` | 1,180,000,000.00 USD | 101,980.00 USD | 0.00 USD | `+77.39%` | `25.79` |
| `Live` | `Short` | `3965.00` | 1,180,000,000.00 USD | 57,950.00 USD | 0.00 USD | `+77.83%` | `14.62` |
| `Live` | `Short` | `3975.00` | 1,180,000,000.00 USD | 566,890.00 USD | 0.00 USD | `+78.28%` | `142.61` |
| `Live` | `Short` | `3985.00` | 1,180,000,000.00 USD | 1,080,000.00 USD | 0.00 USD | `+78.73%` | `269.88` |
| `Live` | `Short` | `3995.00` | 1,180,000,000.00 USD | 360,060.00 USD | 0.00 USD | `+79.18%` | `90.13` |
| `Live` | `Short` | `4005.00` | 1,180,000,000.00 USD | 627,270.00 USD | 0.00 USD | `+79.63%` | `156.62` |
| `Live` | `Short` | `4015.00` | 1,180,000,000.00 USD | 81,790.00 USD | 0.00 USD | `+80.08%` | `20.37` |
| `Live` | `Short` | `4025.00` | 1,180,000,000.00 USD | 557,880.00 USD | 0.00 USD | `+80.53%` | `138.60` |
| `Live` | `Short` | `4035.00` | 1,180,000,000.00 USD | 90,960.00 USD | 0.00 USD | `+80.97%` | `22.54` |
| `Live` | `Short` | `4045.00` | 1,180,000,000.00 USD | 7,890.00 USD | 0.00 USD | `+81.42%` | `1.95` |
| `Live` | `Short` | `4055.00` | 1,180,000,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+81.87%` | `430.96` |
| `Live` | `Short` | `4065.00` | 1,180,000,000.00 USD | 154.47 USD | 0.00 USD | `+82.32%` | `0.04` |
| `Live` | `Short` | `4075.00` | 1,180,000,000.00 USD | 474,720.00 USD | 0.00 USD | `+82.77%` | `116.50` |
| `Live` | `Short` | `4085.00` | 1,180,000,000.00 USD | 9,960.00 USD | 0.00 USD | `+83.22%` | `2.44` |
| `Live` | `Short` | `4095.00` | 1,180,000,000.00 USD | 425.47 USD | 0.00 USD | `+83.67%` | `0.10` |
| `Live` | `Short` | `4105.00` | 1,180,000,000.00 USD | 107,050.00 USD | 0.00 USD | `+84.11%` | `26.08` |
| `Live` | `Short` | `4115.00` | 1,190,000,000.00 USD | 2,530,000.00 USD | 0.00 USD | `+84.56%` | `614.66` |
| `Live` | `Short` | `4125.00` | 1,190,000,000.00 USD | 233,750.00 USD | 0.00 USD | `+85.01%` | `56.67` |
| `Live` | `Short` | `4135.00` | 1,190,000,000.00 USD | 173,010.00 USD | 0.00 USD | `+85.46%` | `41.84` |
| `Live` | `Short` | `4145.00` | 1,190,000,000.00 USD | 710,240.00 USD | 0.00 USD | `+85.91%` | `171.35` |
| `Live` | `Short` | `4155.00` | 1,190,000,000.00 USD | 85,310.00 USD | 0.00 USD | `+86.36%` | `20.53` |
| `Live` | `Short` | `4165.00` | 1,190,000,000.00 USD | 1,420,000.00 USD | 0.00 USD | `+86.80%` | `340.64` |
| `Live` | `Short` | `4175.00` | 1,190,000,000.00 USD | 235,900.00 USD | 0.00 USD | `+87.25%` | `56.50` |
| `Live` | `Short` | `4185.00` | 1,190,000,000.00 USD | 872,460.00 USD | 0.00 USD | `+87.70%` | `208.47` |
| `Live` | `Short` | `4195.00` | 1,280,000,000.00 USD | 85,150,000.00 USD | 0.00 USD | `+88.15%` | `20,298.72` |
| `Live` | `Short` | `4205.00` | 1,280,000,000.00 USD | 6,130,000.00 USD | 0.00 USD | `+88.60%` | `1,458.02` |
| `Live` | `Short` | `4215.00` | 1,280,000,000.00 USD | 81,810.00 USD | 0.00 USD | `+89.05%` | `19.41` |
| `Live` | `Short` | `4235.00` | 1,310,000,000.00 USD | 29,040,000.00 USD | 0.00 USD | `+89.94%` | `6,856.86` |
| `Live` | `Short` | `4245.00` | 1,310,000,000.00 USD | 29,900.00 USD | 0.00 USD | `+90.39%` | `7.04` |
| `Live` | `Short` | `4255.00` | 1,320,000,000.00 USD | 5,310,000.00 USD | 0.00 USD | `+90.84%` | `1,248.54` |
| `Live` | `Short` | `4265.00` | 1,320,000,000.00 USD | 54,650.00 USD | 0.00 USD | `+91.29%` | `12.81` |
| `Live` | `Short` | `4275.00` | 1,320,000,000.00 USD | 4,060.00 USD | 0.00 USD | `+91.74%` | `0.95` |
| `Live` | `Short` | `4285.00` | 1,320,000,000.00 USD | 59,170.00 USD | 0.00 USD | `+92.19%` | `13.81` |
| `Live` | `Short` | `4295.00` | 1,320,000,000.00 USD | 108,920.00 USD | 0.00 USD | `+92.64%` | `25.36` |
| `Live` | `Short` | `4305.00` | 1,320,000,000.00 USD | 140,630.00 USD | 0.00 USD | `+93.08%` | `32.67` |
| `Live` | `Short` | `4315.00` | 1,320,000,000.00 USD | 625,670.00 USD | 0.00 USD | `+93.53%` | `145.00` |
| `Live` | `Short` | `4325.00` | 1,320,000,000.00 USD | 229,040.00 USD | 0.00 USD | `+93.98%` | `52.96` |
| `Live` | `Short` | `4335.00` | 1,320,000,000.00 USD | 4,100,000.00 USD | 0.00 USD | `+94.43%` | `946.60` |
| `Live` | `Short` | `4345.00` | 1,600,000,000.00 USD | 281,060,000.00 USD | 0.00 USD | `+94.88%` | `64,685.76` |
| `Live` | `Short` | `4355.00` | 1,600,000,000.00 USD | 508,850.00 USD | 0.00 USD | `+95.33%` | `116.84` |
| `Live` | `Short` | `4365.00` | 1,600,000,000.00 USD | 547,470.00 USD | 0.00 USD | `+95.78%` | `125.42` |
| `Live` | `Short` | `4375.00` | 1,600,000,000.00 USD | 22,390.00 USD | 0.00 USD | `+96.22%` | `5.12` |
| `Live` | `Short` | `4385.00` | 1,600,000,000.00 USD | 14,060.00 USD | 0.00 USD | `+96.67%` | `3.21` |
| `Live` | `Short` | `4395.00` | 1,600,000,000.00 USD | 14,520.00 USD | 0.00 USD | `+97.12%` | `3.30` |
| `Live` | `Short` | `4405.00` | 1,600,000,000.00 USD | 111,660.00 USD | 0.00 USD | `+97.57%` | `25.35` |
| `Live` | `Short` | `4415.00` | 1,600,000,000.00 USD | 50,550.00 USD | 0.00 USD | `+98.02%` | `11.45` |
| `Live` | `Short` | `4425.00` | 1,600,000,000.00 USD | 8,540.00 USD | 0.00 USD | `+98.47%` | `1.93` |
| `Live` | `Short` | `4435.00` | 1,600,000,000.00 USD | 19,310.00 USD | 0.00 USD | `+98.91%` | `4.35` |
| `Live` | `Short` | `4445.00` | 1,600,000,000.00 USD | 31,110.00 USD | 0.00 USD | `+99.36%` | `7.00` |
| `Live` | `Short` | `4455.00` | 1,600,000,000.00 USD | 108,470.00 USD | 0.00 USD | `+99.81%` | `24.35` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `485.00` | 68,900,000.00 USD | 0.00 USD | 278.83 USD | `-78.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `505.00` | 68,900,000.00 USD | 0.00 USD | 15,910.00 USD | `-77.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 68,890,000.00 USD | 0.00 USD | 563.16 USD | `-75.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.00` | 68,890,000.00 USD | 0.00 USD | 583.40 USD | `-71.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.00` | 68,880,000.00 USD | 0.00 USD | 16,690.00 USD | `-70.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.00` | 68,870,000.00 USD | 0.00 USD | 578.54 USD | `-69.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.00` | 68,870,000.00 USD | 0.00 USD | 242.21 USD | `-68.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 68,870,000.00 USD | 0.00 USD | 885.90 USD | `-68.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 68,870,000.00 USD | 0.00 USD | 177.27 USD | `-66.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 68,870,000.00 USD | 0.00 USD | 2,090.00 USD | `-63.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 68,860,000.00 USD | 0.00 USD | 1,670.00 USD | `-62.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 68,860,000.00 USD | 0.00 USD | 139,430.00 USD | `-61.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `875.00` | 68,720,000.00 USD | 0.00 USD | 918.49 USD | `-60.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 68,720,000.00 USD | 0.00 USD | 3,130.00 USD | `-60.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 68,720,000.00 USD | 0.00 USD | 2,780.00 USD | `-59.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 68,720,000.00 USD | 0.00 USD | 516.34 USD | `-55.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 68,720,000.00 USD | 0.00 USD | 100.50 USD | `-55.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 68,720,000.00 USD | 0.00 USD | 223,740.00 USD | `-54.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 68,490,000.00 USD | 0.00 USD | 445.08 USD | `-54.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 68,490,000.00 USD | 0.00 USD | 112.03 USD | `-54.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1045.00` | 68,490,000.00 USD | 0.00 USD | 1,260.00 USD | `-53.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 68,490,000.00 USD | 0.00 USD | 1,060.00 USD | `-52.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 68,490,000.00 USD | 0.00 USD | 995.34 USD | `-51.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 68,490,000.00 USD | 0.00 USD | 1,610.00 USD | `-50.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 68,490,000.00 USD | 0.00 USD | 11,050.00 USD | `-49.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 68,480,000.00 USD | 0.00 USD | 1,320.00 USD | `-49.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 68,470,000.00 USD | 0.00 USD | 1,000.00 USD | `-48.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 68,470,000.00 USD | 0.00 USD | 476.46 USD | `-47.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 68,470,000.00 USD | 0.00 USD | 972.41 USD | `-46.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1195.00` | 68,470,000.00 USD | 0.00 USD | 221.55 USD | `-46.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 68,470,000.00 USD | 0.00 USD | 3,110.00 USD | `-45.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 68,470,000.00 USD | 0.00 USD | 995.93 USD | `-45.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 68,470,000.00 USD | 0.00 USD | 951.93 USD | `-44.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 68,470,000.00 USD | 0.00 USD | 2,290.00 USD | `-43.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 68,460,000.00 USD | 0.00 USD | 9,050.00 USD | `-42.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 68,450,000.00 USD | 0.00 USD | 7,030.00 USD | `-41.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 68,450,000.00 USD | 0.00 USD | 25,040.00 USD | `-41.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 68,420,000.00 USD | 0.00 USD | 1,440.00 USD | `-41.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 68,420,000.00 USD | 0.00 USD | 141,950.00 USD | `-39.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 68,280,000.00 USD | 0.00 USD | 128.86 USD | `-39.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 68,280,000.00 USD | 0.00 USD | 1,270.00 USD | `-38.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 68,280,000.00 USD | 0.00 USD | 4,160.00 USD | `-38.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1385.00` | 68,270,000.00 USD | 0.00 USD | 100,800.00 USD | `-37.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 68,170,000.00 USD | 0.00 USD | 535,600.00 USD | `-37.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 67,640,000.00 USD | 0.00 USD | 18,840.00 USD | `-36.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 67,620,000.00 USD | 0.00 USD | 6,450.00 USD | `-36.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 67,610,000.00 USD | 0.00 USD | 852.10 USD | `-35.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 67,610,000.00 USD | 0.00 USD | 1,610.00 USD | `-35.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 67,610,000.00 USD | 0.00 USD | 5,090.00 USD | `-34.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 67,600,000.00 USD | 0.00 USD | 19,730.00 USD | `-34.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 67,580,000.00 USD | 0.00 USD | 2,600.00 USD | `-33.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 67,580,000.00 USD | 0.00 USD | 19,050.00 USD | `-33.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 67,560,000.00 USD | 0.00 USD | 11,460.00 USD | `-32.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 67,550,000.00 USD | 0.00 USD | 84,170.00 USD | `-32.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 67,470,000.00 USD | 0.00 USD | 11,140.00 USD | `-32.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 67,460,000.00 USD | 0.00 USD | 31,900.00 USD | `-31.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 67,420,000.00 USD | 0.00 USD | 2,090.00 USD | `-31.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 67,420,000.00 USD | 0.00 USD | 960.99 USD | `-30.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 67,420,000.00 USD | 0.00 USD | 58,080.00 USD | `-30.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 67,360,000.00 USD | 0.00 USD | 10,660.00 USD | `-29.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 67,350,000.00 USD | 0.00 USD | 198,620.00 USD | `-29.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 67,150,000.00 USD | 0.00 USD | 4,990.00 USD | `-28.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 67,150,000.00 USD | 0.00 USD | 7,240.00 USD | `-28.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 67,140,000.00 USD | 0.00 USD | 431,660.00 USD | `-28.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 66,710,000.00 USD | 0.00 USD | 25,700.00 USD | `-27.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 66,680,000.00 USD | 0.00 USD | 15,920.00 USD | `-27.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 66,670,000.00 USD | 0.00 USD | 10,560.00 USD | `-26.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 66,660,000.00 USD | 0.00 USD | 323,930.00 USD | `-26.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 66,330,000.00 USD | 0.00 USD | 80,080.00 USD | `-25.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 66,250,000.00 USD | 0.00 USD | 744.09 USD | `-25.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 66,250,000.00 USD | 0.00 USD | 289.27 USD | `-24.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 66,250,000.00 USD | 0.00 USD | 35,320.00 USD | `-24.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 66,220,000.00 USD | 0.00 USD | 42,680.00 USD | `-23.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 66,180,000.00 USD | 0.00 USD | 84,490.00 USD | `-23.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 66,090,000.00 USD | 0.00 USD | 16,350.00 USD | `-23.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 66,070,000.00 USD | 0.00 USD | 47,500.00 USD | `-22.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 66,030,000.00 USD | 0.00 USD | 28,150.00 USD | `-22.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 66,000,000.00 USD | 0.00 USD | 3,180.00 USD | `-21.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 66,000,000.00 USD | 0.00 USD | 466,520.00 USD | `-21.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 65,530,000.00 USD | 0.00 USD | 77,220.00 USD | `-20.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 65,450,000.00 USD | 0.00 USD | 8,070.00 USD | `-20.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 65,440,000.00 USD | 0.00 USD | 8,500.00 USD | `-19.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 65,440,000.00 USD | 0.00 USD | 189,720.00 USD | `-19.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 65,250,000.00 USD | 0.00 USD | 738,880.00 USD | `-19.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 64,510,000.00 USD | 0.00 USD | 262,190.00 USD | `-18.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 64,240,000.00 USD | 0.00 USD | 27,250.00 USD | `-18.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 64,220,000.00 USD | 0.00 USD | 17,460.00 USD | `-17.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 64,200,000.00 USD | 0.00 USD | 31,580.00 USD | `-17.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 64,170,000.00 USD | 0.00 USD | 790,920.00 USD | `-16.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 63,380,000.00 USD | 0.00 USD | 33,750.00 USD | `-16.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 63,340,000.00 USD | 0.00 USD | 18,240,000.00 USD | `-15.90%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 45,100,000.00 USD | 0.00 USD | 20,990.00 USD | `-15.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 45,080,000.00 USD | 0.00 USD | 64,600.00 USD | `-15.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 45,020,000.00 USD | 0.00 USD | 159,840.00 USD | `-14.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 44,860,000.00 USD | 0.00 USD | 98,060.00 USD | `-14.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1925.00` | 44,760,000.00 USD | 0.00 USD | 19,300,000.00 USD | `-13.66%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 25,460,000.00 USD | 0.00 USD | 107,510.00 USD | `-13.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 25,350,000.00 USD | 0.00 USD | 63,130.00 USD | `-12.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 25,290,000.00 USD | 0.00 USD | 63,530.00 USD | `-12.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 25,230,000.00 USD | 0.00 USD | 139,850.00 USD | `-11.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 25,090,000.00 USD | 0.00 USD | 334,160.00 USD | `-11.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 24,750,000.00 USD | 0.00 USD | 99,900.00 USD | `-10.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 24,650,000.00 USD | 0.00 USD | 248,710.00 USD | `-10.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 24,410,000.00 USD | 0.00 USD | 1,800,000.00 USD | `-10.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 22,600,000.00 USD | 0.00 USD | 481,780.00 USD | `-9.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 22,120,000.00 USD | 0.00 USD | 15,390.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 22,110,000.00 USD | 0.00 USD | 311,020.00 USD | `-8.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 21,790,000.00 USD | 0.00 USD | 801,210.00 USD | `-8.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 20,990,000.00 USD | 0.00 USD | 318,040.00 USD | `-7.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 20,670,000.00 USD | 0.00 USD | 134,110.00 USD | `-7.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 20,540,000.00 USD | 0.00 USD | 36,260.00 USD | `-6.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 20,500,000.00 USD | 0.00 USD | 143,690.00 USD | `-6.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 20,360,000.00 USD | 0.00 USD | 29,280.00 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 20,330,000.00 USD | 0.00 USD | 716,620.00 USD | `-5.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 19,610,000.00 USD | 0.00 USD | 165,900.00 USD | `-5.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 19,450,000.00 USD | 0.00 USD | 304,460.00 USD | `-4.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 19,140,000.00 USD | 0.00 USD | 608,350.00 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 18,540,000.00 USD | 0.00 USD | 248,440.00 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 18,290,000.00 USD | 0.00 USD | 4,740,000.00 USD | `-3.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 13,550,000.00 USD | 0.00 USD | 1,640,000.00 USD | `-2.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 11,910,000.00 USD | 0.00 USD | 8,050,000.00 USD | `-2.45%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2185.00` | 3,860,000.00 USD | 0.00 USD | 1,550,000.00 USD | `-2.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 2,300,000.00 USD | 0.00 USD | 808,730.00 USD | `-1.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 1,500,000.00 USD | 0.00 USD | 346,930.00 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 1,150,000.00 USD | 0.00 USD | 679,200.00 USD | `-0.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 469,250.00 USD | 0.00 USD | 469,250.00 USD | `-0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2235.00` | 238,580.00 USD | 238,580.00 USD | 0.00 USD | `+0.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2245.00` | 3,090,000.00 USD | 2,850,000.00 USD | 0.00 USD | `+0.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2255.00` | 5,680,000.00 USD | 2,590,000.00 USD | 0.00 USD | `+1.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2265.00` | 8,590,000.00 USD | 2,910,000.00 USD | 0.00 USD | `+1.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 9,240,000.00 USD | 650,100.00 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 10,380,000.00 USD | 1,140,000.00 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 10,630,000.00 USD | 249,730.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 20,150,000.00 USD | 9,520,000.00 USD | 0.00 USD | `+3.38%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2315.00` | 21,480,000.00 USD | 1,330,000.00 USD | 0.00 USD | `+3.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 21,880,000.00 USD | 399,800.00 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 22,080,000.00 USD | 201,930.00 USD | 0.00 USD | `+4.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 23,060,000.00 USD | 972,770.00 USD | 0.00 USD | `+5.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 24,480,000.00 USD | 1,430,000.00 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 24,780,000.00 USD | 292,460.00 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 24,940,000.00 USD | 161,070.00 USD | 0.00 USD | `+6.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 24,990,000.00 USD | 55,350.00 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 26,150,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 27,770,000.00 USD | 1,620,000.00 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 28,010,000.00 USD | 238,510.00 USD | 0.00 USD | `+8.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 30,950,000.00 USD | 2,940,000.00 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 31,140,000.00 USD | 188,860.00 USD | 0.00 USD | `+9.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 31,620,000.00 USD | 482,610.00 USD | 0.00 USD | `+9.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2455.00` | 31,770,000.00 USD | 148,310.00 USD | 0.00 USD | `+10.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 33,870,000.00 USD | 2,100,000.00 USD | 0.00 USD | `+10.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 34,060,000.00 USD | 188,440.00 USD | 0.00 USD | `+11.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 36,170,000.00 USD | 2,110,000.00 USD | 0.00 USD | `+11.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 36,580,000.00 USD | 411,640.00 USD | 0.00 USD | `+11.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 41,470,000.00 USD | 4,890,000.00 USD | 0.00 USD | `+12.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2515.00` | 48,390,000.00 USD | 6,920,000.00 USD | 0.00 USD | `+12.80%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 51,440,000.00 USD | 3,050,000.00 USD | 0.00 USD | `+13.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 51,500,000.00 USD | 64,370.00 USD | 0.00 USD | `+13.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 53,700,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+14.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 53,930,000.00 USD | 235,090.00 USD | 0.00 USD | `+14.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 57,040,000.00 USD | 3,110,000.00 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 57,120,000.00 USD | 80,760.00 USD | 0.00 USD | `+15.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 59,820,000.00 USD | 2,700,000.00 USD | 0.00 USD | `+15.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 59,830,000.00 USD | 10,500.00 USD | 0.00 USD | `+16.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 62,700,000.00 USD | 2,860,000.00 USD | 0.00 USD | `+16.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 62,790,000.00 USD | 93,420.00 USD | 0.00 USD | `+17.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 64,970,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+17.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 65,120,000.00 USD | 148,510.00 USD | 0.00 USD | `+18.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 67,250,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+18.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 67,570,000.00 USD | 318,690.00 USD | 0.00 USD | `+19.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 69,710,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+19.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 69,920,000.00 USD | 208,460.00 USD | 0.00 USD | `+19.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 72,090,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+20.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 72,170,000.00 USD | 76,240.00 USD | 0.00 USD | `+20.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 77,180,000.00 USD | 5,010,000.00 USD | 0.00 USD | `+21.32%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2715.00` | 77,250,000.00 USD | 76,900.00 USD | 0.00 USD | `+21.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 79,720,000.00 USD | 2,470,000.00 USD | 0.00 USD | `+22.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 79,760,000.00 USD | 43,050.00 USD | 0.00 USD | `+22.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 82,130,000.00 USD | 2,370,000.00 USD | 0.00 USD | `+23.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 82,820,000.00 USD | 684,550.00 USD | 0.00 USD | `+23.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 85,150,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+24.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 85,730,000.00 USD | 577,610.00 USD | 0.00 USD | `+24.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 88,000,000.00 USD | 2,260,000.00 USD | 0.00 USD | `+24.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 88,010,000.00 USD | 17,550.00 USD | 0.00 USD | `+25.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 91,140,000.00 USD | 3,130,000.00 USD | 0.00 USD | `+25.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 91,200,000.00 USD | 52,490.00 USD | 0.00 USD | `+26.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 91,240,000.00 USD | 43,930.00 USD | 0.00 USD | `+26.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 91,530,000.00 USD | 286,140.00 USD | 0.00 USD | `+27.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 92,530,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+27.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 93,800,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+28.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 93,810,000.00 USD | 10,470.00 USD | 0.00 USD | `+28.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 93,820,000.00 USD | 2,460.00 USD | 0.00 USD | `+28.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 94,120,000.00 USD | 305,820.00 USD | 0.00 USD | `+29.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 94,140,000.00 USD | 16,190.00 USD | 0.00 USD | `+29.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 95,620,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+30.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 95,630,000.00 USD | 10,340.00 USD | 0.00 USD | `+30.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 95,630,000.00 USD | 3,050.00 USD | 0.00 USD | `+31.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 95,690,000.00 USD | 52,370.00 USD | 0.00 USD | `+31.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 95,720,000.00 USD | 34,650.00 USD | 0.00 USD | `+32.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 95,770,000.00 USD | 43,460.00 USD | 0.00 USD | `+32.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 95,880,000.00 USD | 113,340.00 USD | 0.00 USD | `+32.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 96,020,000.00 USD | 145,510.00 USD | 0.00 USD | `+33.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 96,200,000.00 USD | 177,120.00 USD | 0.00 USD | `+33.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 101,120,000.00 USD | 4,920,000.00 USD | 0.00 USD | `+34.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 104,140,000.00 USD | 3,010,000.00 USD | 0.00 USD | `+34.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 104,140,000.00 USD | 6,950.00 USD | 0.00 USD | `+35.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 104,180,000.00 USD | 35,380.00 USD | 0.00 USD | `+35.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 104,250,000.00 USD | 74,910.00 USD | 0.00 USD | `+36.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 104,280,000.00 USD | 22,460.00 USD | 0.00 USD | `+36.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 105,050,000.00 USD | 771,720.00 USD | 0.00 USD | `+37.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 105,050,000.00 USD | 612.69 USD | 0.00 USD | `+37.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 105,100,000.00 USD | 49,500.00 USD | 0.00 USD | `+37.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 105,120,000.00 USD | 19,570.00 USD | 0.00 USD | `+38.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 105,120,000.00 USD | 928.50 USD | 0.00 USD | `+38.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 117,070,000.00 USD | 11,950,000.00 USD | 0.00 USD | `+39.26%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 117,180,000.00 USD | 111,160.00 USD | 0.00 USD | `+39.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 117,560,000.00 USD | 381,020.00 USD | 0.00 USD | `+40.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 117,570,000.00 USD | 2,660.00 USD | 0.00 USD | `+41.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 117,630,000.00 USD | 58,930.00 USD | 0.00 USD | `+41.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 117,640,000.00 USD | 9,860.00 USD | 0.00 USD | `+41.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 117,640,000.00 USD | 149.22 USD | 0.00 USD | `+42.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 117,640,000.00 USD | 1,330.00 USD | 0.00 USD | `+42.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 117,680,000.00 USD | 41,120.00 USD | 0.00 USD | `+43.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 118,340,000.00 USD | 661,330.00 USD | 0.00 USD | `+43.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 118,340,000.00 USD | 1,760.00 USD | 0.00 USD | `+44.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 118,350,000.00 USD | 3,740.00 USD | 0.00 USD | `+44.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 118,350,000.00 USD | 167.25 USD | 0.00 USD | `+45.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 118,400,000.00 USD | 56,110.00 USD | 0.00 USD | `+45.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 118,640,000.00 USD | 236,580.00 USD | 0.00 USD | `+45.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 118,650,000.00 USD | 15,710.00 USD | 0.00 USD | `+46.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 118,660,000.00 USD | 1,630.00 USD | 0.00 USD | `+46.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 118,800,000.00 USD | 141,980.00 USD | 0.00 USD | `+47.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 118,810,000.00 USD | 15,350.00 USD | 0.00 USD | `+47.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 120,230,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+48.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 120,620,000.00 USD | 389,970.00 USD | 0.00 USD | `+48.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 120,630,000.00 USD | 18,270.00 USD | 0.00 USD | `+49.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 120,640,000.00 USD | 4,350.00 USD | 0.00 USD | `+49.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 120,640,000.00 USD | 2,170.00 USD | 0.00 USD | `+50.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 120,640,000.00 USD | 837.74 USD | 0.00 USD | `+50.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 120,640,000.00 USD | 2,780.00 USD | 0.00 USD | `+50.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 120,670,000.00 USD | 21,260.00 USD | 0.00 USD | `+51.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 120,720,000.00 USD | 58,010.00 USD | 0.00 USD | `+51.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 121,050,000.00 USD | 322,160.00 USD | 0.00 USD | `+52.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 122,540,000.00 USD | 1,490,000.00 USD | 0.00 USD | `+52.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 122,540,000.00 USD | 5,700.00 USD | 0.00 USD | `+53.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 122,560,000.00 USD | 16,310.00 USD | 0.00 USD | `+53.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 122,580,000.00 USD | 15,030.00 USD | 0.00 USD | `+54.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 122,590,000.00 USD | 18,600.00 USD | 0.00 USD | `+54.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 122,590,000.00 USD | 495.50 USD | 0.00 USD | `+55.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 122,600,000.00 USD | 3,190.00 USD | 0.00 USD | `+55.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 122,640,000.00 USD | 43,610.00 USD | 0.00 USD | `+56.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 122,640,000.00 USD | 158.32 USD | 0.00 USD | `+56.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 123,090,000.00 USD | 444,280.00 USD | 0.00 USD | `+57.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 123,130,000.00 USD | 43,620.00 USD | 0.00 USD | `+57.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 123,130,000.00 USD | 3,690.00 USD | 0.00 USD | `+58.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 123,140,000.00 USD | 9,810.00 USD | 0.00 USD | `+58.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 123,230,000.00 USD | 90,810.00 USD | 0.00 USD | `+59.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 123,240,000.00 USD | 2,300.00 USD | 0.00 USD | `+59.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3575.00` | 123,240,000.00 USD | 2,870.00 USD | 0.00 USD | `+60.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 123,240,000.00 USD | 354.92 USD | 0.00 USD | `+60.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 123,250,000.00 USD | 13,160.00 USD | 0.00 USD | `+61.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 123,350,000.00 USD | 101,080.00 USD | 0.00 USD | `+61.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 123,360,000.00 USD | 10,210.00 USD | 0.00 USD | `+62.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 123,370,000.00 USD | 7,790.00 USD | 0.00 USD | `+63.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 123,380,000.00 USD | 3,860.00 USD | 0.00 USD | `+63.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 123,380,000.00 USD | 8,090.00 USD | 0.00 USD | `+63.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 123,390,000.00 USD | 8,130.00 USD | 0.00 USD | `+64.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 123,450,000.00 USD | 55,120.00 USD | 0.00 USD | `+64.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 123,450,000.00 USD | 1,410.00 USD | 0.00 USD | `+65.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 123,450,000.00 USD | 819.92 USD | 0.00 USD | `+66.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 123,450,000.00 USD | 323.58 USD | 0.00 USD | `+66.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 123,450,000.00 USD | 1,400.00 USD | 0.00 USD | `+67.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 123,460,000.00 USD | 6,490.00 USD | 0.00 USD | `+67.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3745.00` | 123,460,000.00 USD | 165.90 USD | 0.00 USD | `+67.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 123,460,000.00 USD | 751.00 USD | 0.00 USD | `+68.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 123,460,000.00 USD | 286.90 USD | 0.00 USD | `+69.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 123,460,000.00 USD | 1,560.00 USD | 0.00 USD | `+70.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 124,190,000.00 USD | 734,530.00 USD | 0.00 USD | `+70.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 124,220,000.00 USD | 20,930.00 USD | 0.00 USD | `+71.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 124,220,000.00 USD | 8,380.00 USD | 0.00 USD | `+71.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 124,220,000.00 USD | 711.78 USD | 0.00 USD | `+72.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 124,220,000.00 USD | 355.28 USD | 0.00 USD | `+72.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 124,230,000.00 USD | 5,170.00 USD | 0.00 USD | `+72.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 124,250,000.00 USD | 19,430.00 USD | 0.00 USD | `+74.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 124,260,000.00 USD | 12,120.00 USD | 0.00 USD | `+75.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 124,910,000.00 USD | 646,840.00 USD | 0.00 USD | `+75.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 124,950,000.00 USD | 42,570.00 USD | 0.00 USD | `+76.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 125,010,000.00 USD | 59,170.00 USD | 0.00 USD | `+76.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 125,010,000.00 USD | 1,380.00 USD | 0.00 USD | `+77.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 125,020,000.00 USD | 6,960.00 USD | 0.00 USD | `+78.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 125,030,000.00 USD | 14,610.00 USD | 0.00 USD | `+78.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 125,040,000.00 USD | 4,280.00 USD | 0.00 USD | `+79.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 127,790,000.00 USD | 2,750,000.00 USD | 0.00 USD | `+79.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 127,790,000.00 USD | 898.59 USD | 0.00 USD | `+80.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 127,790,000.00 USD | 811.00 USD | 0.00 USD | `+81.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 127,790,000.00 USD | 4,310.00 USD | 0.00 USD | `+82.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 127,800,000.00 USD | 3,050.00 USD | 0.00 USD | `+83.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 127,830,000.00 USD | 36,740.00 USD | 0.00 USD | `+84.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 127,840,000.00 USD | 5,990.00 USD | 0.00 USD | `+84.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 127,840,000.00 USD | 372.90 USD | 0.00 USD | `+85.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 127,840,000.00 USD | 395.43 USD | 0.00 USD | `+85.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 127,840,000.00 USD | 376.65 USD | 0.00 USD | `+87.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 127,880,000.00 USD | 42,260.00 USD | 0.00 USD | `+88.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 127,880,000.00 USD | 460.70 USD | 0.00 USD | `+89.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 127,880,000.00 USD | 1,270.00 USD | 0.00 USD | `+89.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 127,890,000.00 USD | 4,300.00 USD | 0.00 USD | `+90.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 127,890,000.00 USD | 437.16 USD | 0.00 USD | `+91.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 127,950,000.00 USD | 64,550.00 USD | 0.00 USD | `+91.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 127,960,000.00 USD | 1,610.00 USD | 0.00 USD | `+92.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 128,050,000.00 USD | 97,670.00 USD | 0.00 USD | `+93.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 128,050,000.00 USD | 1,070.00 USD | 0.00 USD | `+93.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 128,070,000.00 USD | 11,270.00 USD | 0.00 USD | `+94.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 128,070,000.00 USD | 2,400.00 USD | 0.00 USD | `+95.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 128,110,000.00 USD | 43,750.00 USD | 0.00 USD | `+96.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 128,180,000.00 USD | 64,570.00 USD | 0.00 USD | `+96.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 128,180,000.00 USD | 1,050.00 USD | 0.00 USD | `+97.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 128,450,000.00 USD | 269,710.00 USD | 0.00 USD | `+97.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 128,460,000.00 USD | 11,480.00 USD | 0.00 USD | `+98.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 128,460,000.00 USD | 2,510.00 USD | 0.00 USD | `+98.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 128,640,000.00 USD | 177,400.00 USD | 0.00 USD | `+98.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 128,640,000.00 USD | 2,040.00 USD | 0.00 USD | `+99.81%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `29.06B` | Total OI Tokens: `12,973,681.7 ETH`
  * 1h OI Change: `+0.79%` | 4h OI Change: `+0.69%` | 24h OI Change: `-2.76%`
  * Exchange Breakdown: Binance=`8.44B` | Bybit=`2.08B` | OKX=`1.80B` | Hyperliquid=`2.36B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-333.38K` | Last 24h: `1.05M` | Last 3d: `6.29M` | Last 7d: `12.86M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0001%` | **USDT OKX** | `-0.0086%` |
| **USDT Bybit** | `-0.0171%` | **USDT KuCoin** | `-0.0115%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `-0.0002%` |
| **USDT Gate** | `-0.0132%` | **USDT Bitget** | `-0.0004%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0050%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `54.38%` | `45.62%` | `1.19` | 839,390,000.00 USD |
| `15M` | `Binance` | `51.83%` | `48.17%` | `1.08` | 261,000,000.00 USD |
| `15M` | `OKX` | `58.26%` | `41.74%` | `1.40` | 112,930,000.00 USD |
| `15M` | `Bybit` | `59.57%` | `40.43%` | `1.47` | 88,670,000.00 USD |
| `15M` | `KuCoin` | `56.76%` | `43.24%` | `1.31` | 1,650,000.00 USD |
| `15M` | `Gate` | `46.37%` | `53.63%` | `0.86` | 80,420,000.00 USD |
| `15M` | `Bitget` | `56.86%` | `43.14%` | `1.32` | 56,160,000.00 USD |
| `15M` | `BingX` | `54.76%` | `45.24%` | `1.21` | 13,770,000.00 USD |
| `15M` | `MEXC` | `58.05%` | `41.95%` | `1.38` | 41,900,000.00 USD |
| `15M` | `Bitunix` | `49.83%` | `50.17%` | `0.99` | 42,000,000.00 USD |
| `15M` | `Hyperliquid` | `55.9%` | `44.1%` | `1.27` | 71,500,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `76.87%` | `23.13%` | `3.32` | 21,630,000.00 USD |
| `15M` | `Crypto.com` | `52.3%` | `47.7%` | `1.10` | 1,840,000.00 USD |
| `15M` | `WhiteBIT` | `72.43%` | `27.57%` | `2.63` | 4,460,000.00 USD |
| `15M` | `HTX` | `57.85%` | `42.15%` | `1.37` | 2,280,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `50.54%` | `49.46%` | `1.02` | 18,960,000.00 USD |
| `15M` | `Bitfinex` | `45.35%` | `54.65%` | `0.83` | 364,660.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `39.66%` | `60.34%` | `0.66` | 7,090,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `38.85%` | `61.15%` | `0.64` | 12,770,000.00 USD |
| `15M` | `Whale Positions` | `51.83%` | `48.17%` | `1.08` | 261,000,000.00 USD |
| `15M` | `Global Accounts` | `54.38%` | `45.62%` | `1.19` | 839,390,000.00 USD |
| `1H` | `ETH` | `56.49%` | `43.51%` | `1.30` | 3,830,000,000.00 USD |
| `1H` | `Binance` | `57.74%` | `42.26%` | `1.37` | 1,260,000,000.00 USD |
| `1H` | `OKX` | `55.19%` | `44.81%` | `1.23` | 538,350,000.00 USD |
| `1H` | `Bybit` | `61.7%` | `38.3%` | `1.61` | 397,550,000.00 USD |
| `1H` | `KuCoin` | `77.32%` | `22.68%` | `3.41` | 17,460,000.00 USD |
| `1H` | `Gate` | `47.59%` | `52.41%` | `0.91` | 428,520,000.00 USD |
| `1H` | `Bitget` | `52.32%` | `47.68%` | `1.10` | 215,660,000.00 USD |
| `1H` | `BingX` | `51.46%` | `48.54%` | `1.06` | 54,540,000.00 USD |
| `1H` | `MEXC` | `51.63%` | `48.37%` | `1.07` | 138,900,000.00 USD |
| `1H` | `Bitunix` | `51.35%` | `48.65%` | `1.06` | 152,940,000.00 USD |
| `1H` | `Hyperliquid` | `58.93%` | `41.07%` | `1.43` | 284,160,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `75.92%` | `24.08%` | `3.15` | 58,670,000.00 USD |
| `1H` | `Crypto.com` | `51.18%` | `48.82%` | `1.05` | 11,720,000.00 USD |
| `1H` | `WhiteBIT` | `91.44%` | `8.56%` | `10.68` | 48,360,000.00 USD |
| `1H` | `HTX` | `53.33%` | `46.67%` | `1.14` | 12,210,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `58.85%` | `41.15%` | `1.43` | 129,270,000.00 USD |
| `1H` | `Bitfinex` | `58.11%` | `41.89%` | `1.39` | 2,730,000.00 USD |
| `1H` | `Kraken` | `58.1%` | `41.9%` | `1.39` | 55,260.00 USD |
| `1H` | `Aster` | `50.22%` | `49.78%` | `1.01` | 37,650,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `48.15%` | `51.85%` | `0.93` | 42,090,000.00 USD |
| `1H` | `Whale Positions` | `57.74%` | `42.26%` | `1.37` | 1,260,000,000.00 USD |
| `1H` | `Global Accounts` | `56.49%` | `43.51%` | `1.30` | 3,830,000,000.00 USD |
| `4H` | `ETH` | `48.93%` | `51.07%` | `0.96` | 23,240,000,000.00 USD |
| `4H` | `Binance` | `50%` | `50%` | `1.00` | 6,740,000,000.00 USD |
| `4H` | `OKX` | `50.75%` | `49.25%` | `1.03` | 3,070,000,000.00 USD |
| `4H` | `Bybit` | `51.42%` | `48.58%` | `1.06` | 2,220,000,000.00 USD |
| `4H` | `KuCoin` | `52.65%` | `47.35%` | `1.11` | 83,260,000.00 USD |
| `4H` | `Gate` | `48.81%` | `51.19%` | `0.95` | 2,130,000,000.00 USD |
| `4H` | `Bitget` | `48.13%` | `51.87%` | `0.93` | 1,090,000,000.00 USD |
| `4H` | `BingX` | `50.35%` | `49.65%` | `1.01` | 311,530,000.00 USD |
| `4H` | `MEXC` | `47.39%` | `52.61%` | `0.90` | 918,630,000.00 USD |
| `4H` | `Bitunix` | `51.59%` | `48.41%` | `1.07` | 986,950,000.00 USD |
| `4H` | `Hyperliquid` | `55%` | `45%` | `1.22` | 1,590,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `64.71%` | `35.29%` | `1.83` | 129,840,000.00 USD |
| `4H` | `Crypto.com` | `50.04%` | `49.96%` | `1.00` | 72,810,000.00 USD |
| `4H` | `WhiteBIT` | `36.38%` | `63.62%` | `0.57` | 2,560,000,000.00 USD |
| `4H` | `HTX` | `49.83%` | `50.17%` | `0.99` | 86,850,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `50.35%` | `49.65%` | `1.01` | 739,060,000.00 USD |
| `4H` | `Bitfinex` | `48.79%` | `51.21%` | `0.95` | 17,630,000.00 USD |
| `4H` | `Kraken` | `47.74%` | `52.26%` | `0.91` | 64,320,000.00 USD |
| `4H` | `Aster` | `50.6%` | `49.4%` | `1.02` | 202,300,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.81%` | `52.19%` | `0.92` | 214,380,000.00 USD |
| `4H` | `Whale Positions` | `50%` | `50%` | `1.00` | 6,740,000,000.00 USD |
| `4H` | `Global Accounts` | `48.93%` | `51.07%` | `0.96` | 23,240,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2192.25` | `2195.11` | `2192.25` | `2205.75` | `2188.75` | 213,150,561.59 USD | 86,554,765.83 USD | 126,595,795.76 USD | -40,041,029.93 USD | `-18.79%` | `1B / 5S` |
| `0:00 UTC` | `2190.25` | `2193.00` | `2190.25` | `2205.25` | `2181.25` | 206,705,717.00 USD | 113,660,029.38 USD | 93,045,687.62 USD | 20,614,341.75 USD | `+9.97%` | `2B / 2S` |
| `5:00 UTC` | `2214.75` | `2211.66` | `2214.75` | `2217.25` | `2204.25` | 218,308,818.86 USD | 130,467,599.52 USD | 87,841,219.34 USD | 42,626,380.18 USD | `+19.53%` | `6B / 1S` |
| `0:00 UTC` | `2217.25` | `2215.50` | `2217.25` | `2218.75` | `2209.75` | 102,137,358.80 USD | 50,758,296.06 USD | 51,379,062.74 USD | -620,766.68 USD | `-0.61%` | `0B / 3S` |
| `5:00 UTC` | `2208.25` | `2209.85` | `2208.25` | `2215.75` | `2207.25` | 69,365,754.50 USD | 25,046,876.87 USD | 44,318,877.64 USD | -19,272,000.77 USD | `-27.78%` | `0B / 4S` |
| `0:00 UTC` | `2215.25` | `2214.70` | `2215.25` | `2218.75` | `2208.25` | 100,318,327.91 USD | 51,517,721.13 USD | 48,800,606.78 USD | 2,717,114.35 USD | `+2.71%` | `2B / 2S` |
| `5:00 UTC` | `2219.75` | `2216.05` | `2219.75` | `2221.25` | `2210.25` | 81,002,689.38 USD | 47,369,805.78 USD | 33,632,883.60 USD | 13,736,922.17 USD | `+16.96%` | `0B / 0S` |
| `0:00 UTC` | `2229.75` | `2226.55` | `2229.75` | `2232.75` | `2219.75` | 182,767,345.67 USD | 98,774,699.85 USD | 83,992,645.82 USD | 14,782,054.04 USD | `+8.09%` | `1B / 2S` |
| `5:00 UTC` | `2234.75` | `2234.69` | `2234.75` | `2238.25` | `2230.25` | 138,036,296.36 USD | 70,500,947.16 USD | 67,535,349.20 USD | 2,965,597.96 USD | `+2.15%` | `1B / 0S` |
| `0:00 UTC` | `2229.75` | `2230.44` | `2229.75` | `2236.75` | `2225.25` | 120,463,298.49 USD | 53,848,530.99 USD | 66,614,767.50 USD | -12,766,236.50 USD | `-10.60%` | `0B / 3S` |

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
| `5m` | -804,250.00 USD | 8,960,000.00 USD | **`ACCUMULATION`** |
| `15m` | -2,740,000.00 USD | -4,280,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -3,700,000.00 USD | 6,630,000.00 USD | **`ACCUMULATION`** |
| `1h` | 11,710,000.00 USD | 68,750,000.00 USD | **`ACCUMULATION`** |
| `2h` | 12,530,000.00 USD | 115,420,000.00 USD | **`ACCUMULATION`** |
| `4h` | -47,890,000.00 USD | -501,220,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -66,680,000.00 USD | -604,450,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -137,130,000.00 USD | -1,780,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -160,880,000.00 USD | -2,120,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -123,960,000.00 USD | -1,960,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -169,330,000.00 USD | -3,030,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,150,000,000.00 USD | -9,710,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-804.25K` | 15m=`-2.74M` | 1h=`+11.71M` | 24h=`-123.96M`
* Futures Capital Netflows: 5m=`+8.96M` | 15m=`-4.28M` | 1h=`+68.75M` | 24h=`-1.96B`
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
  * `2026-10-30 09:09:49 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:42:49 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:42:49 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:42:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:41:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:43:49 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `2195.90` (Risk Distance: `11.05` pts)
  * +2.5R Take Profit: `2234.58`
  * Mathematical Lot Sizing: **`0.90 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2280.60` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2291.65` (Risk Distance: `11.05` pts)
  * +2.5R Take Profit: `2252.97`
  * Mathematical Lot Sizing: **`0.90 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2252.12`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
