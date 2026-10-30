# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 09:43:23 IST` (`2026-10-30 04:13:23 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2223.40` | **Live Ask Quote**: `2226.60` | **Mid Price**: `2225.00`
- **Spread Points**: `320.00` | **Spread BPS**: `14.38 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2208.50` | VWAP Z-Score: `+1.59` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `18.60` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `47.84` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2249.00` | Lower -3.00σ Band: `2168.00`
  * Upper +2.51σ Band: `2242.39` | Lower -2.51σ Band: `2174.61`
  * Upper +2.01σ Band: `2235.64` | Lower -2.01σ Band: `2181.36`
  * Upper +2.00σ Band: `2235.50` | Lower -2.00σ Band: `2181.50`
  * Upper +1.28σ Band: `2225.78` | Lower -1.28σ Band: `2191.22`
  * Upper +1.00σ Band: `2222.00` | Lower -1.00σ Band: `2195.00`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2216.29` | EMA-20=`2225.30` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2258.50` (Slope: `+0.0000`) | EMA-100=`2285.73`
  * Institutional Anchors: EMA-144=`2297.04` | EMA-200=`2305.41` (Slope: `-0.5313`) | EMA-233=`2310.31`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2280.60` (Distance: `-2.45%`)
  * Point of Control (POC) = `2264.42` (Distance: `-1.75%`)
  * Value Area Low (VAL) = `2206.14` (Distance: `+0.84%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2350.38` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2233.90` | Low=`2216.10`
  * New York Session (13:00-21:00 UTC): High=`2238.35` | Low=`2211.65`
  * Initial Balance (First Hour): IB High=`2231.67` | IB Low=`2218.32`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2216.10` - `2233.90`
  * Optimal Trade Entry (OTE 0.705): `2229.45`
  * Structural Invalidation Anchor (0.786): `2242.80`

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
| --- | **`2225.00`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2227.50` | `279.2451` | 622,018.46 USD | 8,416,437.23 USD | `8 orders` | `-0.09%` | `-` |
| `BID` | `2227.60` | `709.9279` | 1,581,435.39 USD | 7,794,418.77 USD | `11 orders` | `-0.08%` | `-` |
| `BID` | `2227.70` | `158.4014` | 352,870.80 USD | 6,212,983.38 USD | `8 orders` | `-0.08%` | `-` |
| `BID` | `2227.80` | `142.9442` | 318,451.09 USD | 5,860,112.58 USD | `5 orders` | `-0.07%` | `-` |
| `BID` | `2227.90` | `99.8067` | 222,359.35 USD | 5,541,661.49 USD | `8 orders` | `-0.07%` | `-` |
| `BID` | `2228.00` | `114.6900` | 255,529.32 USD | 5,319,302.15 USD | `16 orders` | `-0.07%` | `-` |
| `BID` | `2228.10` | `212.9738` | 474,526.92 USD | 5,063,772.83 USD | `12 orders` | `-0.06%` | `-` |
| `BID` | `2228.20` | `259.3529` | 577,890.13 USD | 4,589,245.90 USD | `6 orders` | `-0.06%` | `-` |
| `BID` | `2228.30` | `373.2265` | 831,660.61 USD | 4,011,355.77 USD | `8 orders` | `-0.05%` | `-` |
| `BID` | `2228.40` | `136.2400` | 303,597.22 USD | 3,179,695.16 USD | `11 orders` | `-0.05%` | `-` |
| `BID` | `2228.50` | `114.0827` | 254,233.30 USD | 2,876,097.94 USD | `31 orders` | `-0.04%` | `-` |
| `BID` | `2228.60` | `67.1934` | 149,747.21 USD | 2,621,864.65 USD | `8 orders` | `-0.04%` | `-` |
| `BID` | `2228.70` | `96.1991` | 214,398.93 USD | 2,472,117.44 USD | `7 orders` | `-0.03%` | `-` |
| `BID` | `2228.80` | `375.2429` | 836,341.38 USD | 2,257,718.50 USD | `7 orders` | `-0.03%` | `-` |
| `BID` | `2228.90` | `145.8462` | 325,076.60 USD | 1,421,377.13 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `2229.00` | `185.6042` | 413,711.76 USD | 1,096,300.53 USD | `12 orders` | `-0.02%` | `-` |
| `BID` | `2229.10` | `11.2140` | 24,997.13 USD | 682,588.77 USD | `8 orders` | `-0.02%` | `-` |
| `BID` | `2229.20` | `131.9783` | 294,206.03 USD | 657,591.64 USD | `8 orders` | `-0.01%` | `-` |
| `BID` | `2229.30` | `45.7832` | 102,064.49 USD | 363,385.62 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `2229.40` | `117.2159` | 261,321.13 USD | 261,321.13 USD | `22 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2229.45` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,229.45` | `0.00%` | `-` |
| `ASK` | `2229.50` | `92.1430` | 205,432.82 USD | 205,432.82 USD | `16 orders` | `+0.00%` | `-` |
| `ASK` | `2229.70` | `20.6094` | 45,952.78 USD | 251,385.60 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `2229.80` | `81.3804` | 181,462.02 USD | 432,847.61 USD | `11 orders` | `+0.02%` | `-` |
| `ASK` | `2229.90` | `39.1679` | 87,340.50 USD | 520,188.11 USD | `10 orders` | `+0.02%` | `-` |
| `ASK` | `2230.00` | `86.5437` | 192,992.45 USD | 713,180.56 USD | `7 orders` | `+0.02%` | `-` |
| `ASK` | `2230.10` | `20.7783` | 46,337.69 USD | 759,518.25 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `2230.20` | `57.2046` | 127,577.70 USD | 887,095.95 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `2230.30` | `232.4583` | 518,451.75 USD | 1,405,547.70 USD | `10 orders` | `+0.04%` | `-` |
| `ASK` | `2230.40` | `30.7212` | 68,520.56 USD | 1,474,068.26 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `2230.50` | `194.6520` | 434,171.29 USD | 1,908,239.55 USD | `8 orders` | `+0.05%` | `-` |
| `ASK` | `2230.60` | `207.7486` | 463,404.03 USD | 2,371,643.57 USD | `7 orders` | `+0.05%` | `-` |
| `ASK` | `2230.70` | `163.2716` | 364,209.96 USD | 2,735,853.53 USD | `9 orders` | `+0.06%` | `-` |
| `ASK` | `2230.80` | `159.7556` | 356,382.79 USD | 3,092,236.33 USD | `7 orders` | `+0.06%` | `-` |
| `ASK` | `2230.90` | `310.1743` | 691,967.85 USD | 3,784,204.17 USD | `9 orders` | `+0.07%` | `-` |
| `ASK` | `2231.00` | `102.2802` | 228,187.13 USD | 4,012,391.30 USD | `11 orders` | `+0.07%` | `-` |
| `ASK` | `2231.10` | `286.2197` | 638,584.77 USD | 4,650,976.07 USD | `8 orders` | `+0.07%` | `-` |
| `ASK` | `2231.20` | `176.9232` | 394,751.04 USD | 5,045,727.11 USD | `11 orders` | `+0.08%` | `-` |
| `ASK` | `2231.30` | `381.9024` | 852,138.83 USD | 5,897,865.94 USD | `14 orders` | `+0.08%` | `-` |
| `ASK` | `2231.40` | `88.2347` | 196,886.91 USD | 6,094,752.85 USD | `11 orders` | `+0.09%` | `-` |
| `ASK` | `2231.50` | `336.3985` | 750,673.25 USD | 6,845,426.10 USD | `13 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1786.48` | `30,282.40` | 54,098,835.01 USD | `AT_RISK_LIQ` | `0xde8d9e530b` | `2026-10-30 09:33:32 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1844.27` | `7,964.66` | 14,688,972.62 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 09:33:32 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 09:33:32 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `10,000.00` | 19,261,000.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 09:33:32 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1928.81` | `8,092.45` | 15,608,770.69 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 09:33:32 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2122.22` | `30,641.99` | 65,028,977.30 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 09:33:32 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.50` | `26,025.05` | 55,420,231.63 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 09:33:32 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2150.00` | `1,500.00` | 3,225,000.00 USD | `TRIGGER_STOP` | `0x834cae1ec1` | `2026-10-30 09:33:32 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,000.00` | 6,525,000.00 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2198.00` | `2,068.13` | 4,545,755.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2199.60` | `491.76` | 1,081,681.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2200.90` | `4,722.42` | 10,393,577.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2207.40` | `266.00` | 587,168.40 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x24fb652303` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2209.10` | `1,481.65` | 3,273,114.78 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2215.40` | `358.73` | 794,719.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2215.40` | `343.92` | 761,925.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2217.00` | `498.40` | 1,104,946.15 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2217.50` | `1,034.97` | 2,295,037.10 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2218.80` | `2,431.87` | 5,395,832.05 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2222.60` | `498.47` | 1,107,899.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2224.20` | `707.55` | 1,573,726.70 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2224.70` | `1,801.86` | 4,008,588.60 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2225.20` | `349.48` | 777,661.34 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.30` | `1,240.75` | 2,762,281.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.60` | `466.08` | 1,037,767.05 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.70` | `1,350.15` | 3,006,369.21 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2228.60` | `495.00` | 1,103,162.57 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2229.70` | `898.89` | 2,004,261.28 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2230.90` | `247.79` | 552,790.25 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2231.10` | `673.72` | 1,503,136.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2232.70` | `448.83` | 1,002,106.76 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2232.80` | `349.33` | 779,994.74 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.60` | `336.34` | 751,588.49 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2238.70` | `335.73` | 751,607.03 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2239.40` | `339.72` | 760,777.25 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2239.60` | `447.49` | 1,002,200.17 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2240.70` | `252.03` | 564,730.34 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2241.00` | `670.77` | 1,503,189.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2243.10` | `511.32` | 1,146,931.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2243.20` | `893.48` | 2,004,253.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.30` | `473.83` | 1,063,423.40 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.40` | `1,240.75` | 2,784,739.08 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.70` | `1,339.33` | 3,006,393.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.70` | `337.95` | 758,595.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2246.30` | `506.99` | 1,138,853.88 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2246.50` | `674.24` | 1,514,671.17 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2247.40` | `1,783.59` | 4,008,431.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2251.10` | `507.18` | 1,141,710.65 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2252.00` | `2,431.87` | 5,476,570.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2252.50` | `392.01` | 883,006.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x6798a1b850` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2253.20` | `1,009.29` | 2,274,130.65 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2257.80` | `351.99` | 794,719.86 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2260.00` | `337.14` | 761,925.55 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2261.80` | `1,430.39` | 3,235,262.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2262.90` | `4,722.42` | 10,686,367.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2265.90` | `507.49` | 1,149,917.06 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.70` | `620.97` | 1,409,408.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.20` | `2,200.51` | 4,999,999.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb1ec7febea` | `2026-10-30 09:33:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2273.10` | `2,093.74` | 4,759,290.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 09:33:32 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2463.82` | `22,046.99` | 54,319,767.92 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 09:33:32 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,037.41` | 7,635,751.54 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 09:33:32 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2624.22` | `10,000.00` | 26,242,230.56 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 09:33:32 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.08` | `9,700.00` | 25,783,366.12 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 09:33:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 237,045,451.70 USD | `106,417.71` | `2322.74` | `2228.70` | `3810.98` | 10,135,560.46 USD | `+4.28%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 144,121,357.93 USD | `64,680.62` | `2375.30` | `2228.70` | `4370.04` | 9,514,939.57 USD | `+6.60%` | `5X Cross` |
| `10` | `0x77dd...e0e9` | `LONG` | 68,294,871.10 USD | `30,641.99` | `2610.31` | `2228.70` | `2122.13` | -11,690,303.94 USD | `-17.12%` | `10X Cross` |
| `11` | `0xde8d...9524` | `LONG` | 67,469,195.00 USD | `30,282.40` | `2134.45` | `2228.70` | `1786.39` | 2,832,864.42 USD | `+4.20%` | `20X Cross` |
| `17` | `0x0392...d7d9` | `LONG` | 57,983,813.85 USD | `26,025.05` | `2518.71` | `2228.70` | `2129.41` | -7,565,908.24 USD | `-13.05%` | `9X Cross` |
| `23` | `0x8add...7d2c` | `SHORT` | 49,109,667.55 USD | `22,046.99` | `2271.09` | `2228.70` | `2468.64` | 961,229.75 USD | `+1.96%` | `25X Cross` |
| `27` | `0xdf95...7d72` | `SHORT` | 44,535,492.23 USD | `19,981.83` | `2402.53` | `2228.70` | `4207.30` | 3,471,533.75 USD | `+7.79%` | `25X Cross` |
| `35` | `0xeced...6210` | `SHORT` | 37,195,773.19 USD | `16,687.58` | `2522.09` | `2228.70` | `3475.18` | 4,891,941.80 USD | `+13.15%` | `20X Cross` |
| `36` | `0xb695...a92d` | `SHORT` | 36,148,749.87 USD | `16,214.56` | `2557.74` | `2228.70` | `3933.57` | 5,323,978.96 USD | `+14.73%` | `20X Cross` |
| `37` | `0x6046...b21d` | `LONG` | 35,485,077.09 USD | `15,927.59` | `2410.19` | `2228.70` | `1772.05` | -2,903,542.56 USD | `-8.18%` | `6X Cross` |
| `41` | `0x45d2...4029` | `SHORT` | 31,091,760.00 USD | `13,950.00` | `2443.60` | `2228.70` | `5359.08` | 2,996,522.46 USD | `+9.64%` | `20X Cross` |
| `44` | `0xa61c...66b9` | `LONG` | 28,727,352.00 USD | `12,888.00` | `2369.69` | `2228.70` | `1455.11` | -1,813,302.54 USD | `-6.31%` | `10X Cross` |
| `47` | `0x2371...0883` | `LONG` | 26,738,400.00 USD | `12,000.00` | `2421.77` | `2228.70` | `1279.37` | -2,322,894.85 USD | `-8.69%` | `20X Cross` |
| `48` | `0xbd1c...ff0e` | `LONG` | 26,731,200.00 USD | `12,000.00` | `2419.91` | `2228.70` | `1520.27` | -2,307,832.39 USD | `-8.63%` | `20X Cross` |
| `55` | `0xa9de...e049` | `LONG` | 24,506,900.00 USD | `11,000.00` | `2481.81` | `2228.70` | `1644.01` | -2,793,079.46 USD | `-11.40%` | `20X Cross` |
| `56` | `0x0c5d...36b3` | `LONG` | 24,506,900.00 USD | `11,000.00` | `2482.20` | `2228.70` | `1644.34` | -2,797,353.24 USD | `-11.41%` | `20X Cross` |
| `57` | `0x6c93...59a4` | `LONG` | 24,505,800.00 USD | `11,000.00` | `2441.15` | `2228.70` | `1602.30` | -2,346,872.73 USD | `-9.58%` | `20X Cross` |
| `58` | `0x09dc...c094` | `LONG` | 24,500,300.00 USD | `11,000.00` | `2465.31` | `2228.70` | `1637.34` | -2,618,123.04 USD | `-10.69%` | `20X Cross` |
| `70` | `0xa2ce...3126` | `LONG` | 22,312,589.51 USD | `10,016.88` | `2162.83` | `2228.70` | `1549.27` | 647,787.46 USD | `+2.90%` | `10X Cross` |
| `71` | `0xec7f...df39` | `LONG` | 22,311,000.00 USD | `10,000.00` | `2719.35` | `2228.70` | `1720.86` | -4,882,548.52 USD | `-21.88%` | `20X Cross` |
| `72` | `0x15a4...dfdb` | `LONG` | 22,290,000.00 USD | `10,000.00` | `1761.94` | `2228.70` | `305.56` | 4,670,518.97 USD | `+20.95%` | `20X Cross` |
| `73` | `0xb37f...66ca` | `SHORT` | 22,288,000.00 USD | `10,000.00` | `2290.69` | `2228.70` | `2624.14` | 618,991.85 USD | `+2.78%` | `25X Cross` |
| `74` | `0x6646...6de5` | `LONG` | 22,276,000.00 USD | `10,000.00` | `1765.80` | `2228.70` | `1723.35` | 4,617,942.55 USD | `+20.73%` | `25X Cross` |
| `76` | `0x939f...04d2` | `LONG` | 21,901,208.48 USD | `9,823.81` | `2427.28` | `2228.70` | `1744.49` | -1,943,942.12 USD | `-8.88%` | `25X Cross` |
| `77` | `0xaeaa...2416` | `SHORT` | 21,613,540.00 USD | `9,700.00` | `2311.92` | `2228.70` | `2658.00` | 812,142.40 USD | `+3.76%` | `25X Cross` |
| `84` | `0xf517...c032` | `SHORT` | 20,780,966.61 USD | `9,326.35` | `2202.91` | `2228.70` | `3140.75` | -235,828.40 USD | `-1.13%` | `25X Cross` |
| `85` | `0xca49...53c8` | `SHORT` | 20,494,968.22 USD | `9,200.88` | `2549.39` | `2228.70` | `3890.56` | 2,961,739.31 USD | `+14.45%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 20,168,056.98 USD | `9,054.12` | `2493.89` | `2228.70` | `2932.00` | 2,411,950.28 USD | `+11.96%` | `20X Cross` |
| `88` | `0xea00...a918` | `LONG` | 20,060,525.00 USD | `9,003.83` | `2003.01` | `2228.70` | `1383.26` | 2,025,746.13 USD | `+10.10%` | `5X Cross` |
| `92` | `0xefe4...194b` | `SHORT` | 19,661,940.83 USD | `8,820.57` | `2267.42` | `2228.70` | `3604.72` | 338,073.56 USD | `+1.72%` | `20X Cross` |
| `113` | `0x9eec...daab` | `LONG` | 18,036,457.24 USD | `8,092.45` | `1658.44` | `2228.70` | `1929.42` | 4,615,592.71 USD | `+25.59%` | `15X Cross` |
| `114` | `0x5f91...65aa` | `LONG` | 17,745,253.35 USD | `7,964.66` | `1626.99` | `2228.70` | `1844.18` | 4,786,810.28 USD | `+26.98%` | `16X Cross` |
| `126` | `0xec0b...b078` | `LONG` | 15,614,777.51 USD | `7,007.80` | `2065.97` | `2228.70` | `1066.97` | 1,136,847.92 USD | `+7.28%` | `25X Cross` |
| `130` | `0xf02d...5eb3` | `LONG` | 15,284,734.07 USD | `6,855.99` | `2383.33` | `2228.70` | `1127.55` | -1,055,354.69 USD | `-6.90%` | `20X Cross` |
| `131` | `0xcf53...ee11` | `SHORT` | 15,153,720.42 USD | `6,803.63` | `1862.69` | `2228.70` | `4233.44` | -2,480,615.03 USD | `-16.37%` | `7X Cross` |
| `132` | `0x418a...8888` | `SHORT` | 14,987,304.38 USD | `6,724.38` | `2494.55` | `2228.70` | `3015.63` | 1,787,018.79 USD | `+11.92%` | `25X Cross` |
| `137` | `0x4ff9...38d3` | `LONG` | 14,621,529.85 USD | `6,564.10` | `2447.40` | `2228.70` | `1669.96` | -1,443,492.89 USD | `-9.87%` | `3X Isolated` |
| `139` | `0x1ee7...edf5` | `LONG` | 14,489,150.00 USD | `6,500.00` | `2301.55` | `2228.70` | `2069.17` | -470,943.66 USD | `-3.25%` | `25X Cross` |
| `140` | `0xf78c...c581` | `LONG` | 14,482,493.50 USD | `6,500.22` | `2521.53` | `2228.70` | `1913.44` | -1,908,047.44 USD | `-13.17%` | `20X Cross` |
| `141` | `0xecb6...2b00` | `SHORT` | 14,475,675.23 USD | `6,493.08` | `2242.98` | `2228.70` | `6335.18` | 88,224.47 USD | `+0.61%` | `15X Cross` |
| `144` | `0x799f...5f4c` | `LONG` | 14,069,527.82 USD | `6,310.90` | `2390.33` | `2228.70` | `1853.17` | -1,015,636.80 USD | `-7.22%` | `20X Cross` |
| `148` | `0x08bf...7872` | `SHORT` | 13,874,024.06 USD | `6,224.05` | `2258.00` | `2228.70` | `2585.23` | 179,892.05 USD | `+1.30%` | `20X Cross` |
| `151` | `0xd9e7...4aff` | `LONG` | 13,374,000.00 USD | `6,000.00` | `2480.18` | `2228.70` | `1407.73` | -1,507,124.33 USD | `-11.27%` | `20X Cross` |
| `162` | `0x0c4a...1b19` | `LONG` | 12,606,735.16 USD | `5,660.10` | `2373.06` | `2228.70` | `2081.78` | -825,022.97 USD | `-6.54%` | `25X Isolated` |
| `165` | `0xc179...e0c8` | `LONG` | 12,109,798.27 USD | `5,431.86` | `2306.65` | `2228.70` | `1018.09` | -419,645.59 USD | `-3.47%` | `10X Cross` |
| `168` | `0x7fda...17d1` | `LONG` | 11,850,952.22 USD | `5,315.76` | `2211.05` | `2228.70` | `0.000000` | 97,509.98 USD | `+0.82%` | `25X Cross` |
| `178` | `0x218a...7da2` | `SHORT` | 11,641,773.22 USD | `5,222.87` | `2208.16` | `2228.70` | `2792.88` | -108,838.16 USD | `-0.93%` | `10X Cross` |
| `187` | `0x45ab...6cbc` | `LONG` | 10,969,316.84 USD | `4,920.96` | `2727.66` | `2228.70` | `1385.75` | -2,453,426.96 USD | `-22.37%` | `7X Cross` |
| `191` | `0x64b7...9da9` | `LONG` | 10,828,808.68 USD | `4,856.84` | `2604.61` | `2228.70` | `610.09` | -1,821,405.73 USD | `-16.82%` | `25X Cross` |
| `198` | `0xfb18...eb17` | `SHORT` | 10,626,849.68 USD | `4,768.18` | `2315.53` | `2228.70` | `2580.15` | 414,032.12 USD | `+3.90%` | `25X Cross` |
| `199` | `0x5559...d43b` | `SHORT` | 10,600,957.49 USD | `4,755.93` | `2262.69` | `2228.70` | `2766.37` | 160,248.38 USD | `+1.51%` | `25X Cross` |
| `211` | `0xe091...6705` | `SHORT` | 10,025,550.45 USD | `4,500.00` | `2467.33` | `2228.70` | `2463.35` | 1,077,458.06 USD | `+10.75%` | `20X Cross` |
| `220` | `0xb829...3a81` | `LONG` | 9,796,696.11 USD | `4,394.91` | `2398.60` | `2228.70` | `1473.60` | -744,945.84 USD | `-7.60%` | `20X Cross` |
| `237` | `0x28bb...fca6` | `SHORT` | 9,379,862.36 USD | `4,209.61` | `1896.10` | `2228.70` | `3035.72` | -1,397,979.80 USD | `-14.90%` | `20X Cross` |
| `239` | `0x6ea4...0ea7` | `SHORT` | 9,325,954.22 USD | `4,184.01` | `2602.13` | `2228.70` | `3425.29` | 1,561,392.45 USD | `+16.74%` | `20X Cross` |
| `251` | `0x5e9e...35ee` | `SHORT` | 8,927,231.08 USD | `4,007.56` | `1796.39` | `2228.70` | `2585.78` | -1,728,080.99 USD | `-19.36%` | `20X Cross` |
| `252` | `0x8cc9...2b6a` | `SHORT` | 8,917,600.00 USD | `4,000.00` | `1791.18` | `2228.70` | `3593.98` | -1,752,853.33 USD | `-19.66%` | `25X Cross` |
| `253` | `0xfb94...0ddf` | `SHORT` | 8,916,681.70 USD | `4,002.10` | `2382.44` | `2228.70` | `5104.68` | 618,102.45 USD | `+6.93%` | `20X Cross` |
| `255` | `0x3dc9...54b0` | `SHORT` | 8,911,309.77 USD | `3,999.69` | `2480.32` | `2228.70` | `6608.62` | 1,009,226.79 USD | `+11.33%` | `20X Cross` |
| `274` | `0x4b67...f4e7` | `LONG` | 8,517,038.68 USD | `3,820.84` | `2591.51` | `2228.70` | `1347.54` | -1,384,734.86 USD | `-16.26%` | `20X Cross` |
| `277` | `0x12d2...f97f` | `LONG` | 8,371,929.41 USD | `3,757.26` | `2446.50` | `2228.70` | `1799.72` | -820,236.98 USD | `-9.80%` | `20X Cross` |
| `294` | `0x8ae4...3d60` | `LONG` | 7,941,542.79 USD | `3,558.20` | `2482.21` | `2228.70` | `518.43` | -890,655.25 USD | `-11.22%` | `10X Cross` |
| `298` | `0x0622...8088` | `LONG` | 7,883,720.61 USD | `3,536.73` | `2204.83` | `2228.70` | `0.000000` | 85,822.46 USD | `+1.09%` | `5X Cross` |
| `334` | `0x469e...58a5` | `SHORT` | 6,696,300.00 USD | `3,000.00` | `2195.70` | `2228.70` | `3222.40` | -109,192.76 USD | `-1.63%` | `25X Cross` |
| `335` | `0xb823...9763` | `SHORT` | 6,693,300.00 USD | `3,000.00` | `2229.66` | `2228.70` | `3233.68` | -4,303.32 USD | `-0.06%` | `25X Cross` |
| `336` | `0x4a20...3c26` | `LONG` | 6,686,400.00 USD | `3,000.00` | `2428.72` | `2228.70` | `613.84` | -599,760.28 USD | `-8.97%` | `20X Cross` |
| `338` | `0x007d...67a0` | `LONG` | 6,682,500.00 USD | `3,000.00` | `2400.00` | `2228.70` | `1469.98` | -517,500.00 USD | `-7.74%` | `25X Cross` |
| `362` | `0x9c2a...f6a8` | `SHORT` | 6,291,121.72 USD | `2,823.41` | `2533.78` | `2228.70` | `2629.81` | 862,789.10 USD | `+13.71%` | `20X Cross` |
| `390` | `0x8328...f54a` | `SHORT` | 5,742,909.50 USD | `2,576.45` | `2292.01` | `2228.70` | `3279.52` | 162,361.79 USD | `+2.83%` | `25X Cross` |
| `392` | `0xed48...7c9b` | `SHORT` | 5,686,725.00 USD | `2,551.13` | `2460.02` | `2228.70` | `3243.43` | 589,121.41 USD | `+10.36%` | `20X Cross` |
| `395` | `0x1c98...7fc7` | `LONG` | 5,568,760.02 USD | `2,500.00` | `2452.60` | `2228.70` | `1916.93` | -562,761.54 USD | `-10.11%` | `10X Cross` |
| `396` | `0x970c...2a93` | `SHORT` | 5,568,750.00 USD | `2,500.00` | `2229.57` | `2228.70` | `5067.30` | 5,194.49 USD | `+0.09%` | `20X Cross` |
| `411` | `0xa445...329d` | `LONG` | 5,362,795.47 USD | `2,406.14` | `2354.86` | `2228.70` | `1731.91` | -303,319.81 USD | `-5.66%` | `25X Cross` |
| `414` | `0x6749...ce07` | `SHORT` | 5,316,883.13 USD | `2,384.89` | `2220.92` | `2228.70` | `3632.24` | -20,220.10 USD | `-0.38%` | `20X Cross` |
| `415` | `0xfbe2...c8ea` | `SHORT` | 5,316,862.69 USD | `2,385.21` | `2041.57` | `2228.70` | `2622.30` | -447,296.04 USD | `-8.41%` | `20X Cross` |
| `417` | `0x645b...87b8` | `SHORT` | 5,305,917.60 USD | `2,379.98` | `2421.64` | `2228.70` | `11488.31` | 457,529.35 USD | `+8.62%` | `10X Cross` |
| `426` | `0x77ee...2902` | `SHORT` | 5,105,836.15 USD | `2,290.69` | `2476.53` | `2228.70` | `5880.13` | 567,136.09 USD | `+11.11%` | `25X Cross` |
| `432` | `0xbcd4...0dd2` | `SHORT` | 5,043,530.03 USD | `2,263.50` | `2233.24` | `2228.70` | `2674.17` | 11,427.54 USD | `+0.23%` | `25X Cross` |
| `451` | `0xd507...c948` | `SHORT` | 4,839,650.18 USD | `2,172.00` | `2387.49` | `2228.70` | `2600.53` | 345,990.85 USD | `+7.15%` | `5X Isolated` |
| `459` | `0x382b...3e39` | `SHORT` | 4,747,600.04 USD | `2,129.54` | `2296.66` | `2228.70` | `4627.74` | 143,237.17 USD | `+3.02%` | `25X Cross` |
| `461` | `0x023a...2355` | `LONG` | 4,733,579.00 USD | `2,123.54` | `2330.15` | `2228.70` | `0.000000` | -214,594.81 USD | `-4.53%` | `25X Cross` |
| `493` | `0x3453...b323` | `SHORT` | 4,456,274.27 USD | `2,000.12` | `2322.47` | `2228.70` | `2387.97` | 188,961.57 USD | `+4.24%` | `25X Cross` |
| `494` | `0x7a6d...f79c` | `SHORT` | 4,455,800.00 USD | `2,000.00` | `2418.41` | `2228.70` | `2518.14` | 381,032.11 USD | `+8.55%` | `25X Cross` |
| `495` | `0xe02e...d78b` | `LONG` | 4,455,740.00 USD | `2,000.00` | `2228.11` | `2228.70` | `2171.88` | -483.47 USD | `-0.01%` | `25X Cross` |
| `502` | `0xf3dc...1672` | `SHORT` | 4,414,621.41 USD | `1,980.36` | `2240.44` | `2228.70` | `2765.34` | 22,266.14 USD | `+0.50%` | `20X Cross` |
| `507` | `0xac48...3201` | `SHORT` | 4,378,972.49 USD | `1,964.37` | `2272.04` | `2228.70` | `3125.87` | 84,169.81 USD | `+1.92%` | `20X Cross` |
| `521` | `0x8376...9a1e` | `SHORT` | 4,256,585.09 USD | `1,910.50` | `2477.72` | `2228.70` | `3184.37` | 477,103.08 USD | `+11.21%` | `20X Cross` |
| `551` | `0x7265...91a5` | `LONG` | 4,013,664.09 USD | `1,801.87` | `2533.96` | `2228.70` | `1987.40` | -552,202.37 USD | `-13.76%` | `20X Cross` |
| `553` | `0x739c...cfb2` | `SHORT` | 4,010,400.00 USD | `1,800.00` | `2427.60` | `2228.70` | `2480.98` | 359,296.38 USD | `+8.96%` | `25X Cross` |
| `567` | `0x91a9...3f70` | `SHORT` | 3,938,298.94 USD | `1,767.48` | `2156.23` | `2228.70` | `3661.55` | -127,194.86 USD | `-3.23%` | `4X Cross` |
| `574` | `0xbb34...1696` | `LONG` | 3,899,000.00 USD | `1,750.00` | `2315.81` | `2228.70` | `1957.00` | -153,668.23 USD | `-3.94%` | `25X Cross` |
| `576` | `0xc619...10f5` | `LONG` | 3,898,125.00 USD | `1,750.00` | `2315.39` | `2228.70` | `1785.80` | -153,820.83 USD | `-3.95%` | `25X Cross` |
| `595` | `0xfeec...4e9c` | `SHORT` | 3,771,718.54 USD | `1,691.81` | `2566.49` | `2228.70` | `2509.97` | 570,305.98 USD | `+15.12%` | `10X Cross` |
| `617` | `0xeee0...0b53` | `LONG` | 3,647,512.05 USD | `1,637.12` | `2468.64` | `2228.70` | `209.18` | -393,964.01 USD | `-10.80%` | `7X Cross` |
| `619` | `0x27b8...12fc` | `LONG` | 3,628,998.30 USD | `1,628.12` | `2468.73` | `2228.70` | `626.39` | -390,396.34 USD | `-10.76%` | `10X Cross` |
| `620` | `0x982b...4606` | `LONG` | 3,624,548.94 USD | `1,626.82` | `2575.24` | `2228.70` | `1547.68` | -564,904.13 USD | `-15.59%` | `5X Isolated` |
| `627` | `0x73d7...8be1` | `LONG` | 3,567,424.55 USD | `1,601.47` | `2410.40` | `2228.70` | `1768.46` | -292,754.37 USD | `-8.21%` | `25X Cross` |
| `629` | `0xad54...6203` | `LONG` | 3,558,323.66 USD | `1,597.45` | `2591.98` | `2228.70` | `2052.04` | -582,254.38 USD | `-16.36%` | `10X Isolated` |
| `631` | `0x880a...311c` | `LONG` | 3,518,410.77 USD | `1,578.40` | `2209.72` | `2228.70` | `0.000000` | 30,586.92 USD | `+0.87%` | `9X Cross` |
| `651` | `0xe170...9300` | `SHORT` | 3,415,648.50 USD | `1,533.40` | `2076.39` | `2228.70` | `3159.26` | -231,699.00 USD | `-6.78%` | `25X Cross` |
| `656` | `0x4b86...df9d` | `SHORT` | 3,394,710.00 USD | `1,524.00` | `2287.40` | `2228.70` | `2759.88` | 91,287.60 USD | `+2.69%` | `9X Isolated` |
| `660` | `0x2e2b...2fab` | `LONG` | 3,358,435.96 USD | `1,507.38` | `2245.53` | `2228.70` | `1242.39` | -26,437.14 USD | `-0.79%` | `25X Cross` |
| `661` | `0xde6b...3361` | `LONG` | 3,343,425.00 USD | `1,500.00` | `2216.98` | `2228.70` | `2168.81` | 17,944.26 USD | `+0.54%` | `25X Cross` |
| `663` | `0x251f...6e5d` | `LONG` | 3,342,300.00 USD | `1,500.00` | `2346.68` | `2228.70` | `1888.49` | -177,730.49 USD | `-5.32%` | `20X Cross` |
| `664` | `0xf929...d1f9` | `SHORT` | 3,341,250.00 USD | `1,500.00` | `2423.37` | `2228.70` | `2677.92` | 293,805.26 USD | `+8.79%` | `25X Cross` |
| `683` | `0x3440...32c5` | `SHORT` | 3,230,343.97 USD | `1,448.97` | `2198.21` | `2228.70` | `3852.19` | -45,193.01 USD | `-1.40%` | `25X Cross` |
| `684` | `0xb885...3c54` | `LONG` | 3,230,024.90 USD | `1,450.00` | `2274.34` | `2228.70` | `34.31` | -67,783.24 USD | `-2.10%` | `20X Cross` |
| `692` | `0xef70...a84c` | `SHORT` | 3,214,720.84 USD | `1,442.74` | `2424.73` | `2228.70` | `3251.40` | 283,549.98 USD | `+8.82%` | `25X Cross` |
| `698` | `0x4b5f...0dd8` | `LONG` | 3,192,261.29 USD | `1,431.96` | `2339.45` | `2228.70` | `2147.97` | -157,731.65 USD | `-4.94%` | `10X Cross` |
| `701` | `0xbadb...9ee6` | `LONG` | 3,181,226.40 USD | `1,428.16` | `1936.00` | `2228.70` | `1070.30` | 416,304.75 USD | `+13.09%` | `20X Cross` |
| `713` | `0xd911...961e` | `LONG` | 3,139,187.31 USD | `1,408.84` | `2209.82` | `2228.70` | `615.65` | 25,880.47 USD | `+0.82%` | `25X Cross` |
| `754` | `0x53f8...ceff` | `LONG` | 3,006,420.17 USD | `1,348.65` | `2276.73` | `2228.70` | `0.000000` | -64,104.30 USD | `-2.13%` | `20X Cross` |
| `778` | `0x0dd5...f6ee` | `LONG` | 2,929,162.50 USD | `1,315.00` | `2306.05` | `2228.70` | `1560.27` | -103,301.88 USD | `-3.53%` | `5X Cross` |
| `803` | `0x1f16...6d07` | `LONG` | 2,822,040.60 USD | `1,266.00` | `2261.43` | `2228.70` | `1382.59` | -40,930.63 USD | `-1.45%` | `7X Cross` |
| `813` | `0xc435...c905` | `SHORT` | 2,780,419.20 USD | `1,248.00` | `2704.38` | `2228.70` | `4288.83` | 594,651.15 USD | `+21.39%` | `20X Cross` |
| `822` | `0x6859...7e1e` | `SHORT` | 2,756,626.10 USD | `1,237.15` | `2200.39` | `2228.70` | `4771.13` | -34,398.94 USD | `-1.25%` | `25X Cross` |
| `828` | `0x7277...0b98` | `SHORT` | 2,718,650.52 USD | `1,219.45` | `2206.05` | `2228.70` | `3390.37` | -28,462.72 USD | `-1.05%` | `20X Cross` |
| `830` | `0x7178...0854` | `LONG` | 2,716,329.61 USD | `1,218.63` | `2461.81` | `2228.70` | `1181.12` | -283,716.79 USD | `-10.44%` | `10X Cross` |
| `845` | `0xaaa1...ab8c` | `SHORT` | 2,674,920.00 USD | `1,200.00` | `2276.29` | `2228.70` | `2365.50` | 56,637.58 USD | `+2.12%` | `25X Isolated` |
| `852` | `0x0a97...347d` | `LONG` | 2,650,563.98 USD | `1,188.91` | `2267.88` | `2228.70` | `1547.29` | -45,751.87 USD | `-1.73%` | `20X Cross` |
| `853` | `0x07fd...689d` | `LONG` | 2,645,223.08 USD | `1,186.89` | `2416.34` | `2228.70` | `0.000000` | -222,719.27 USD | `-8.42%` | `25X Cross` |
| `858` | `0xa70a...4be9` | `LONG` | 2,639,394.14 USD | `1,184.86` | `2259.47` | `2228.70` | `1029.93` | -37,767.55 USD | `-1.43%` | `20X Cross` |
| `860` | `0xb8eb...1dd5` | `LONG` | 2,634,544.63 USD | `1,181.73` | `2226.79` | `2228.70` | `601.11` | 3,079.88 USD | `+0.12%` | `25X Cross` |
| `862` | `0x6e6f...82a6` | `LONG` | 2,634,236.86 USD | `1,182.23` | `2266.47` | `2228.70` | `1411.67` | -45,249.47 USD | `-1.72%` | `20X Cross` |
| `923` | `0x2f80...f203` | `SHORT` | 2,425,398.51 USD | `1,088.94` | `1984.00` | `2228.70` | `2961.09` | -264,931.32 USD | `-10.92%` | `20X Cross` |
| `931` | `0x6f11...0389` | `SHORT` | 2,405,544.18 USD | `1,079.00` | `2333.39` | `2228.70` | `3198.98` | 112,184.73 USD | `+4.66%` | `25X Cross` |
| `932` | `0x8eb7...b90f` | `LONG` | 2,401,202.94 USD | `1,077.74` | `2396.38` | `2228.70` | `1881.22` | -181,475.11 USD | `-7.56%` | `5X Isolated` |
| `933` | `0x2b61...2f6c` | `SHORT` | 2,398,120.26 USD | `1,076.60` | `2681.75` | `2228.70` | `6418.35` | 489,052.48 USD | `+20.39%` | `10X Cross` |
| `956` | `0x30af...393e` | `SHORT` | 2,319,923.63 USD | `1,041.16` | `2252.26` | `2228.70` | `2297.19` | 25,058.70 USD | `+1.08%` | `25X Cross` |
| `972` | `0x1b2a...f7a6` | `LONG` | 2,284,519.90 USD | `1,025.37` | `2737.51` | `2228.70` | `882.35` | -522,440.03 USD | `-22.87%` | `10X Cross` |
| `977` | `0x001a...fef6` | `SHORT` | 2,245,730.35 USD | `1,007.33` | `2022.19` | `2228.70` | `3085.26` | -208,722.40 USD | `-9.29%` | `10X Cross` |
| `978` | `0x02aa...1806` | `SHORT` | 2,244,020.44 USD | `1,007.10` | `2654.68` | `2228.70` | `3612.98` | 429,511.66 USD | `+19.14%` | `20X Cross` |
| `983` | `0xb15b...dbae` | `SHORT` | 2,236,699.35 USD | `1,004.13` | `2290.80` | `2228.70` | `2265.46` | 63,562.10 USD | `+2.84%` | `25X Cross` |
| `984` | `0xdb3a...cf3b` | `LONG` | 2,235,363.89 USD | `1,003.22` | `2705.01` | `2228.70` | `0.000000` | -478,343.01 USD | `-21.40%` | `4X Cross` |
| `986` | `0x5272...fcd9` | `SHORT` | 2,229,400.00 USD | `1,000.00` | `2241.82` | `2228.70` | `2831.03` | 12,424.49 USD | `+0.56%` | `5X Cross` |
| `987` | `0x8c02...b73f` | `SHORT` | 2,228,000.00 USD | `1,000.00` | `2250.37` | `2228.70` | `8098.66` | 22,371.47 USD | `+1.00%` | `20X Cross` |
| `988` | `0x834c...dd93` | `SHORT` | 2,227,900.00 USD | `1,000.00` | `2191.89` | `2228.70` | `2262.27` | -36,007.36 USD | `-1.62%` | `25X Cross` |
| `990` | `0xd7b8...9f55` | `LONG` | 2,225,672.10 USD | `999.00` | `2195.00` | `2228.70` | `0.000000` | 32,867.10 USD | `+1.48%` | `15X Cross` |
| `1015` | `0xb002...ed8a` | `SHORT` | 2,145,082.75 USD | `962.78` | `2299.66` | `2228.70` | `4201.25` | 68,995.16 USD | `+3.22%` | `25X Cross` |
| `1029` | `0xb812...b5e0` | `LONG` | 2,099,594.90 USD | `941.02` | `2263.21` | `2228.70` | `1186.72` | -30,126.10 USD | `-1.43%` | `25X Cross` |
| `1041` | `0xb1ec...e86a` | `SHORT` | 2,080,146.36 USD | `933.64` | `2272.72` | `2228.70` | `12619.11` | 41,760.60 USD | `+2.01%` | `25X Cross` |
| `1057` | `0xef96...9383` | `LONG` | 2,045,090.94 USD | `917.57` | `2235.00` | `2228.70` | `0.000000` | -5,692.71 USD | `-0.28%` | `25X Cross` |
| `1061` | `0xede2...f971` | `LONG` | 2,036,447.79 USD | `914.31` | `2208.16` | `2228.70` | `1463.26` | 17,490.80 USD | `+0.86%` | `5X Cross` |
| `1063` | `0x9606...4e5d` | `SHORT` | 2,033,700.15 USD | `913.00` | `2478.70` | `2228.70` | `4368.41` | 229,353.46 USD | `+11.28%` | `20X Cross` |
| `1088` | `0x5f10...d49d` | `LONG` | 2,006,190.00 USD | `900.00` | `2249.83` | `2228.70` | `1815.74` | -18,663.47 USD | `-0.93%` | `25X Cross` |
| `1107` | `0x82f6...12ec` | `SHORT` | 1,976,185.17 USD | `887.02` | `2199.66` | `2228.70` | `2249.55` | -25,042.35 USD | `-1.27%` | `25X Cross` |
| `1142` | `0xa0fb...96be` | `LONG` | 1,935,591.56 USD | `868.35` | `2293.96` | `2228.70` | `1122.07` | -56,367.12 USD | `-2.91%` | `3X Cross` |
| `1170` | `0x24fb...ed0f` | `LONG` | 1,894,183.91 USD | `850.10` | `2199.85` | `2228.70` | `0.000000` | 24,097.04 USD | `+1.27%` | `15X Cross` |
| `1181` | `0xcd27...52a8` | `LONG` | 1,865,467.53 USD | `837.21` | `2553.56` | `2228.70` | `1403.49` | -272,397.24 USD | `-14.60%` | `2X Cross` |
| `1190` | `0xbef3...0d3e` | `LONG` | 1,843,284.56 USD | `827.33` | `2227.10` | `2228.70` | `2133.02` | 740.06 USD | `+0.04%` | `20X Cross` |
| `1195` | `0x6a41...a3b9` | `LONG` | 1,840,800.42 USD | `825.69` | `2226.70` | `2228.70` | `2136.78` | 2,227.98 USD | `+0.12%` | `20X Cross` |
| `1237` | `0x04a9...95aa` | `LONG` | 1,783,520.00 USD | `800.00` | `2595.13` | `2228.70` | `1866.67` | -292,586.74 USD | `-16.41%` | `5X Cross` |
| `1238` | `0x7737...bf66` | `SHORT` | 1,781,536.46 USD | `799.79` | `2494.83` | `2228.70` | `23694.29` | 213,809.57 USD | `+12.00%` | `15X Cross` |
| `1269` | `0x458d...ab3b` | `LONG` | 1,726,911.06 USD | `774.75` | `2740.41` | `2228.70` | `1887.25` | -396,218.12 USD | `-22.94%` | `3X Isolated` |
| `1286` | `0x2e30...4cb5` | `SHORT` | 1,688,711.77 USD | `757.58` | `2335.09` | `2228.70` | `8798.14` | 80,301.29 USD | `+4.76%` | `2X Cross` |
| `1328` | `0xaa53...9cb7` | `LONG` | 1,627,095.22 USD | `730.34` | `2389.70` | `2228.70` | `1958.05` | -118,194.41 USD | `-7.26%` | `20X Cross` |
| `1329` | `0x3fc5...c0c1` | `SHORT` | 1,626,782.06 USD | `729.92` | `2702.11` | `2228.70` | `4695.99` | 345,560.13 USD | `+21.24%` | `25X Cross` |
| `1336` | `0x6463...42f5` | `LONG` | 1,620,255.21 USD | `726.88` | `2214.40` | `2228.70` | `0.000000` | 10,644.54 USD | `+0.66%` | `1X Cross` |
| `1347` | `0xa189...94d7` | `SHORT` | 1,604,689.20 USD | `719.98` | `2691.84` | `2228.70` | `2915.09` | 333,383.47 USD | `+20.78%` | `25X Cross` |
| `1364` | `0x2f93...4404` | `LONG` | 1,575,892.77 USD | `707.47` | `1700.45` | `2228.70` | `1368.88` | 372,866.39 USD | `+23.66%` | `4X Isolated` |
| `1371` | `0x5605...fe0f` | `SHORT` | 1,565,113.19 USD | `702.14` | `2566.90` | `2228.70` | `3076.96` | 237,219.46 USD | `+15.16%` | `20X Cross` |
| `1375` | `0x7743...e4fe` | `SHORT` | 1,560,979.32 USD | `700.56` | `2298.56` | `2228.70` | `6178.18` | 49,295.76 USD | `+3.16%` | `25X Cross` |
| `1381` | `0x0deb...0bc5` | `LONG` | 1,559,460.00 USD | `700.00` | `2071.05` | `2228.70` | `1597.47` | 109,724.21 USD | `+7.04%` | `20X Cross` |
| `1409` | `0x51f6...2b39` | `LONG` | 1,540,171.85 USD | `690.85` | `2223.60` | `2228.70` | `299.20` | 4,003.75 USD | `+0.26%` | `25X Cross` |
| `1429` | `0x248e...6be2` | `SHORT` | 1,516,631.60 USD | `680.93` | `2282.89` | `2228.70` | `3448.25` | 37,854.06 USD | `+2.50%` | `20X Cross` |
| `1430` | `0xdbd1...29dd` | `SHORT` | 1,516,264.82 USD | `680.70` | `3030.57` | `2228.70` | `3774.81` | 546,656.31 USD | `+36.05%` | `6X Cross` |
| `1439` | `0x71e5...be04` | `LONG` | 1,510,790.36 USD | `677.67` | `2727.27` | `2228.70` | `1471.03` | -337,395.24 USD | `-22.33%` | `20X Cross` |
| `1444` | `0x0b23...f37b` | `LONG` | 1,504,541.25 USD | `675.00` | `2238.15` | `2228.70` | `598.92` | -6,215.39 USD | `-0.41%` | `5X Cross` |
| `1470` | `0x0cac...6170` | `SHORT` | 1,465,370.25 USD | `657.50` | `2146.55` | `2228.70` | `2839.47` | -54,008.05 USD | `-3.69%` | `20X Cross` |
| `1501` | `0x9599...c60a` | `LONG` | 1,436,067.55 USD | `644.50` | `2231.08` | `2228.70` | `0.000000` | -1,856.31 USD | `-0.13%` | `20X Cross` |
| `1505` | `0xf00e...fe3d` | `SHORT` | 1,432,208.06 USD | `642.88` | `2333.21` | `2228.70` | `2495.25` | 67,769.91 USD | `+4.73%` | `20X Cross` |
| `1507` | `0x31de...13f2` | `LONG` | 1,427,731.61 USD | `640.41` | `2252.34` | `2228.70` | `0.000000` | -14,694.16 USD | `-1.03%` | `20X Cross` |
| `1508` | `0xffb2...5ed6` | `SHORT` | 1,427,308.05 USD | `640.77` | `2672.96` | `2228.70` | `2490.40` | 285,440.30 USD | `+20.00%` | `20X Cross` |
| `1510` | `0x4487...c92d` | `LONG` | 1,424,910.94 USD | `639.23` | `2220.28` | `2228.70` | `1545.43` | 5,636.14 USD | `+0.40%` | `10X Cross` |
| `1521` | `0x8505...1821` | `SHORT` | 1,412,590.34 USD | `633.96` | `2239.93` | `2228.70` | `3857.27` | 7,441.26 USD | `+0.53%` | `20X Cross` |
| `1543` | `0xfce0...f4c0` | `SHORT` | 1,390,129.12 USD | `623.60` | `3129.61` | `2228.70` | `2792.46` | 561,497.46 USD | `+40.39%` | `20X Cross` |
| `1584` | `0xad02...eb65` | `LONG` | 1,338,301.93 USD | `600.62` | `2460.69` | `2228.70` | `1078.95` | -139,638.63 USD | `-10.43%` | `5X Cross` |
| `1586` | `0x26e6...6b28` | `LONG` | 1,337,460.00 USD | `600.00` | `1769.78` | `2228.70` | `2004.75` | 275,588.47 USD | `+20.61%` | `20X Cross` |
| `1587` | `0x638f...f5f0` | `LONG` | 1,337,220.00 USD | `600.00` | `4011.50` | `2228.70` | `411.02` | -1,069,683.53 USD | `-79.99%` | `25X Cross` |
| `1600` | `0x7c90...d129` | `LONG` | 1,324,705.36 USD | `594.17` | `2286.01` | `2228.70` | `1866.47` | -33,577.52 USD | `-2.53%` | `20X Cross` |
| `1660` | `0xfc66...ca06` | `SHORT` | 1,264,836.31 USD | `567.43` | `2275.19` | `2228.70` | `7321.89` | 26,186.90 USD | `+2.07%` | `20X Cross` |
| `1668` | `0xfb99...37f3` | `LONG` | 1,260,201.85 USD | `565.34` | `2362.35` | `2228.70` | `1250.59` | -75,334.51 USD | `-5.98%` | `3X Cross` |
| `1677` | `0x0c68...82d0` | `LONG` | 1,250,668.30 USD | `561.10` | `2207.13` | `2228.70` | `0.000000` | 12,241.84 USD | `+0.98%` | `6X Cross` |
| `1678` | `0x844b...7f42` | `SHORT` | 1,249,627.50 USD | `561.00` | `2026.17` | `2228.70` | `3069.31` | -112,944.09 USD | `-9.04%` | `25X Cross` |
| `1692` | `0xabe6...1d99` | `SHORT` | 1,238,888.11 USD | `556.00` | `2484.68` | `2228.70` | `3119.68` | 142,607.78 USD | `+11.51%` | `20X Cross` |
| `1698` | `0x2a76...9a53` | `LONG` | 1,236,240.23 USD | `554.99` | `2231.40` | `2228.70` | `0.000000` | -2,166.83 USD | `-0.18%` | `25X Cross` |
| `1706` | `0x936c...bb0f` | `LONG` | 1,226,367.52 USD | `550.09` | `2218.31` | `2228.70` | `0.000000` | 6,100.25 USD | `+0.50%` | `20X Cross` |
| `1707` | `0x825c...465e` | `LONG` | 1,225,510.00 USD | `550.00` | `2208.12` | `2228.70` | `1189.54` | 11,040.50 USD | `+0.90%` | `4X Cross` |
| `1714` | `0xad21...fb6a` | `LONG` | 1,219,888.13 USD | `547.26` | `2565.80` | `2228.70` | `1738.69` | -184,264.87 USD | `-15.11%` | `6X Cross` |
| `1747` | `0x71d0...8c26` | `LONG` | 1,182,748.42 USD | `530.59` | `2225.97` | `2228.70` | `0.000000` | 1,656.39 USD | `+0.14%` | `25X Cross` |
| `1815` | `0x0c7a...2f50` | `SHORT` | 1,134,532.33 USD | `509.25` | `2122.56` | `2228.70` | `4116.43` | -53,626.90 USD | `-4.73%` | `20X Cross` |
| `1819` | `0x0089...2410` | `SHORT` | 1,131,076.28 USD | `507.35` | `2308.88` | `2228.70` | `3385.77` | 40,323.98 USD | `+3.57%` | `20X Cross` |
| `1838` | `0xe282...df29` | `LONG` | 1,114,100.00 USD | `500.00` | `2309.84` | `2228.70` | `2045.39` | -40,824.21 USD | `-3.66%` | `10X Isolated` |
| `1839` | `0xb322...d51f` | `SHORT` | 1,114,100.00 USD | `500.00` | `2268.03` | `2228.70` | `3743.15` | 19,916.32 USD | `+1.79%` | `20X Cross` |
| `1840` | `0xa559...ff95` | `LONG` | 1,114,000.00 USD | `500.00` | `2260.68` | `2228.70` | `1064.10` | -16,344.36 USD | `-1.47%` | `20X Cross` |
| `1841` | `0x6936...9417` | `SHORT` | 1,114,000.00 USD | `500.00` | `2315.11` | `2228.70` | `2358.98` | 43,555.21 USD | `+3.91%` | `25X Isolated` |
| `1842` | `0x4044...794c` | `LONG` | 1,114,000.00 USD | `500.00` | `2260.80` | `2228.70` | `0.000000` | -16,400.00 USD | `-1.47%` | `25X Cross` |
| `1843` | `0x89b2...9ca6` | `LONG` | 1,113,650.00 USD | `500.00` | `2363.45` | `2228.70` | `1622.73` | -68,077.42 USD | `-6.11%` | `25X Cross` |
| `1849` | `0x7298...7d6c` | `SHORT` | 1,110,424.60 USD | `498.15` | `3426.75` | `2228.70` | `5421.69` | 596,611.22 USD | `+53.73%` | `20X Cross` |
| `1862` | `0x9c68...7783` | `SHORT` | 1,099,484.42 USD | `493.31` | `2273.58` | `2228.70` | `3898.04` | 22,094.82 USD | `+2.01%` | `25X Cross` |
| `1868` | `0x404c...5f03` | `SHORT` | 1,090,996.76 USD | `489.79` | `2671.94` | `2228.70` | `5182.25` | 217,682.80 USD | `+19.95%` | `20X Cross` |
| `1871` | `0x321f...1c84` | `SHORT` | 1,087,054.30 USD | `488.02` | `2370.09` | `2228.70` | `3053.85` | 69,590.30 USD | `+6.40%` | `10X Cross` |
| `1894` | `0x2577...4897` | `LONG` | 1,062,781.96 USD | `476.71` | `2233.03` | `2228.70` | `0.000000` | -1,733.86 USD | `-0.16%` | `15X Cross` |
| `1920` | `0xe86b...3664` | `LONG` | 1,041,714.37 USD | `467.39` | `2231.29` | `2228.70` | `0.000000` | -1,166.56 USD | `-0.11%` | `25X Cross` |
| `1937` | `0x94b6...e5b3` | `SHORT` | 1,033,290.08 USD | `463.86` | `2261.12` | `2228.70` | `2411.00` | 15,552.59 USD | `+1.51%` | `25X Cross` |
| `1943` | `0x82c6...fe42` | `LONG` | 1,030,450.00 USD | `462.50` | `2501.38` | `2228.70` | `2053.73` | -126,440.57 USD | `-12.27%` | `5X Isolated` |
| `1948` | `0xe330...77a1` | `SHORT` | 1,027,325.23 USD | `461.20` | `2206.97` | `2228.70` | `6440.09` | -9,467.86 USD | `-0.92%` | `20X Cross` |
| `1950` | `0x2de3...486d` | `LONG` | 1,025,711.35 USD | `460.40` | `2286.27` | `2228.70` | `1130.98` | -26,889.56 USD | `-2.62%` | `25X Cross` |
| `1960` | `0x617e...0f97` | `SHORT` | 1,020,040.08 USD | `457.85` | `2205.60` | `2228.70` | `3410.12` | -10,196.25 USD | `-1.00%` | `10X Cross` |
| `1997` | `0xae55...2236` | `LONG` | 1,002,960.00 USD | `450.00` | `2510.21` | `2228.70` | `0.000000` | -126,637.50 USD | `-12.63%` | `25X Cross` |
| `1999` | `0x0514...bdfe` | `SHORT` | 1,002,375.00 USD | `450.00` | `1988.74` | `2228.70` | `3919.45` | -107,438.16 USD | `-10.72%` | `25X Cross` |

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
| `Live` | `Long` | `445.00` | 759,540,000.00 USD | 0.00 USD | 719.03 USD | `-80.09%` | `1.62` |
| `Live` | `Long` | `455.00` | 759,540,000.00 USD | 0.00 USD | 72,310.00 USD | `-79.65%` | `158.92` |
| `Live` | `Long` | `465.00` | 759,470,000.00 USD | 0.00 USD | 2,230.00 USD | `-79.20%` | `4.79` |
| `Live` | `Long` | `475.00` | 759,470,000.00 USD | 0.00 USD | 198,670.00 USD | `-78.75%` | `418.25` |
| `Live` | `Long` | `485.00` | 759,270,000.00 USD | 0.00 USD | 98,630.00 USD | `-78.31%` | `203.36` |
| `Live` | `Long` | `495.00` | 759,170,000.00 USD | 0.00 USD | 88,680.00 USD | `-77.86%` | `179.14` |
| `Live` | `Long` | `505.00` | 759,080,000.00 USD | 0.00 USD | 45,950.00 USD | `-77.41%` | `90.99` |
| `Live` | `Long` | `515.00` | 759,040,000.00 USD | 0.00 USD | 1,880,000.00 USD | `-76.96%` | `3,646.84` |
| `Live` | `Long` | `525.00` | 757,160,000.00 USD | 0.00 USD | 26,700.00 USD | `-76.52%` | `50.85` |
| `Live` | `Long` | `535.00` | 757,130,000.00 USD | 0.00 USD | 2,660.00 USD | `-76.07%` | `4.98` |
| `Live` | `Long` | `545.00` | 757,130,000.00 USD | 0.00 USD | 16,450.00 USD | `-75.62%` | `30.19` |
| `Live` | `Long` | `555.00` | 757,110,000.00 USD | 0.00 USD | 190,490.00 USD | `-75.17%` | `343.22` |
| `Live` | `Long` | `565.00` | 756,920,000.00 USD | 0.00 USD | 666,590.00 USD | `-74.73%` | `1,179.81` |
| `Live` | `Long` | `575.00` | 756,250,000.00 USD | 0.00 USD | 44,270.00 USD | `-74.28%` | `77.00` |
| `Live` | `Long` | `585.00` | 756,210,000.00 USD | 0.00 USD | 1,790,000.00 USD | `-73.83%` | `3,059.02` |
| `Live` | `Long` | `595.00` | 754,420,000.00 USD | 0.00 USD | 541,190.00 USD | `-73.39%` | `909.57` |
| `Live` | `Long` | `605.00` | 753,880,000.00 USD | 0.00 USD | 2,990,000.00 USD | `-72.94%` | `4,937.77` |
| `Live` | `Long` | `615.00` | 750,890,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-72.49%` | `1,663.55` |
| `Live` | `Long` | `625.00` | 749,870,000.00 USD | 0.00 USD | 20,060.00 USD | `-72.04%` | `32.10` |
| `Live` | `Long` | `635.00` | 749,850,000.00 USD | 0.00 USD | 7,980.00 USD | `-71.60%` | `12.56` |
| `Live` | `Long` | `645.00` | 749,840,000.00 USD | 0.00 USD | 54,890.00 USD | `-71.15%` | `85.10` |
| `Live` | `Long` | `655.00` | 749,790,000.00 USD | 0.00 USD | 117,840.00 USD | `-70.70%` | `179.90` |
| `Live` | `Long` | `665.00` | 749,670,000.00 USD | 0.00 USD | 165,010.00 USD | `-70.25%` | `248.13` |
| `Live` | `Long` | `675.00` | 749,500,000.00 USD | 0.00 USD | 147,900.00 USD | `-69.81%` | `219.11` |
| `Live` | `Long` | `685.00` | 749,360,000.00 USD | 0.00 USD | 35,730.00 USD | `-69.36%` | `52.16` |
| `Live` | `Long` | `695.00` | 749,320,000.00 USD | 0.00 USD | 66,640.00 USD | `-68.91%` | `95.88` |
| `Live` | `Long` | `705.00` | 749,250,000.00 USD | 0.00 USD | 7,860.00 USD | `-68.46%` | `11.15` |
| `Live` | `Long` | `715.00` | 749,250,000.00 USD | 0.00 USD | 1,140.00 USD | `-68.02%` | `1.60` |
| `Live` | `Long` | `725.00` | 749,240,000.00 USD | 0.00 USD | 397,250.00 USD | `-67.57%` | `547.94` |
| `Live` | `Long` | `735.00` | 748,850,000.00 USD | 0.00 USD | 189,130.00 USD | `-67.12%` | `257.32` |
| `Live` | `Long` | `745.00` | 748,660,000.00 USD | 0.00 USD | 63,060.00 USD | `-66.68%` | `84.64` |
| `Live` | `Long` | `755.00` | 748,590,000.00 USD | 0.00 USD | 28,770.00 USD | `-66.23%` | `38.11` |
| `Live` | `Long` | `765.00` | 748,570,000.00 USD | 0.00 USD | 12,370.00 USD | `-65.78%` | `16.16` |
| `Live` | `Long` | `775.00` | 748,550,000.00 USD | 0.00 USD | 11,490.00 USD | `-65.33%` | `14.83` |
| `Live` | `Long` | `785.00` | 748,540,000.00 USD | 0.00 USD | 91,840.00 USD | `-64.89%` | `117.00` |
| `Live` | `Long` | `795.00` | 748,450,000.00 USD | 0.00 USD | 66,420.00 USD | `-64.44%` | `83.54` |
| `Live` | `Long` | `805.00` | 748,380,000.00 USD | 0.00 USD | 136,320.00 USD | `-63.99%` | `169.35` |
| `Live` | `Long` | `815.00` | 748,250,000.00 USD | 0.00 USD | 436,890.00 USD | `-63.54%` | `536.06` |
| `Live` | `Long` | `825.00` | 747,810,000.00 USD | 0.00 USD | 79,450.00 USD | `-63.10%` | `96.31` |
| `Live` | `Long` | `835.00` | 747,730,000.00 USD | 0.00 USD | 121,540.00 USD | `-62.65%` | `145.55` |
| `Live` | `Long` | `845.00` | 747,610,000.00 USD | 0.00 USD | 96,220.00 USD | `-62.20%` | `113.86` |
| `Live` | `Long` | `855.00` | 747,510,000.00 USD | 0.00 USD | 135,540.00 USD | `-61.76%` | `158.53` |
| `Live` | `Long` | `865.00` | 747,380,000.00 USD | 0.00 USD | 521,630.00 USD | `-61.31%` | `603.04` |
| `Live` | `Long` | `875.00` | 746,860,000.00 USD | 0.00 USD | 53,500.00 USD | `-60.86%` | `61.15` |
| `Live` | `Long` | `885.00` | 746,800,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-60.41%` | `1,247.31` |
| `Live` | `Long` | `895.00` | 745,700,000.00 USD | 0.00 USD | 14,900.00 USD | `-59.97%` | `16.65` |
| `Live` | `Long` | `905.00` | 745,680,000.00 USD | 0.00 USD | 352,150.00 USD | `-59.52%` | `389.12` |
| `Live` | `Long` | `915.00` | 745,330,000.00 USD | 0.00 USD | 161,430.00 USD | `-59.07%` | `176.43` |
| `Live` | `Long` | `925.00` | 745,170,000.00 USD | 0.00 USD | 218,380.00 USD | `-58.62%` | `236.09` |
| `Live` | `Long` | `935.00` | 744,950,000.00 USD | 0.00 USD | 47,430.00 USD | `-58.18%` | `50.72` |
| `Live` | `Long` | `945.00` | 744,900,000.00 USD | 0.00 USD | 227,350.00 USD | `-57.73%` | `240.58` |
| `Live` | `Long` | `955.00` | 744,680,000.00 USD | 0.00 USD | 117,540.00 USD | `-57.28%` | `123.08` |
| `Live` | `Long` | `965.00` | 744,560,000.00 USD | 0.00 USD | 113,520.00 USD | `-56.83%` | `117.63` |
| `Live` | `Long` | `975.00` | 744,450,000.00 USD | 0.00 USD | 81,320.00 USD | `-56.39%` | `83.41` |
| `Live` | `Long` | `985.00` | 744,360,000.00 USD | 0.00 USD | 152,820.00 USD | `-55.94%` | `155.15` |
| `Live` | `Long` | `995.00` | 744,210,000.00 USD | 0.00 USD | 5,740,000.00 USD | `-55.49%` | `5,773.28` |
| `Live` | `Long` | `1005.00` | 738,470,000.00 USD | 0.00 USD | 56,100.00 USD | `-55.05%` | `55.82` |
| `Live` | `Long` | `1015.00` | 738,410,000.00 USD | 0.00 USD | 232,420.00 USD | `-54.60%` | `228.99` |
| `Live` | `Long` | `1025.00` | 738,180,000.00 USD | 0.00 USD | 187,160.00 USD | `-54.15%` | `182.59` |
| `Live` | `Long` | `1035.00` | 737,990,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-53.70%` | `1,365.55` |
| `Live` | `Long` | `1045.00` | 736,580,000.00 USD | 0.00 USD | 401,740.00 USD | `-53.26%` | `384.44` |
| `Live` | `Long` | `1055.00` | 736,180,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-52.81%` | `2,005.92` |
| `Live` | `Long` | `1065.00` | 734,060,000.00 USD | 0.00 USD | 7,740,000.00 USD | `-52.36%` | `7,265.03` |
| `Live` | `Long` | `1075.00` | 726,320,000.00 USD | 0.00 USD | 660,160.00 USD | `-51.91%` | `614.10` |
| `Live` | `Long` | `1085.00` | 725,660,000.00 USD | 0.00 USD | 354,200.00 USD | `-51.47%` | `326.45` |
| `Live` | `Long` | `1095.00` | 725,310,000.00 USD | 0.00 USD | 54,230.00 USD | `-51.02%` | `49.53` |
| `Live` | `Long` | `1105.00` | 725,250,000.00 USD | 0.00 USD | 172,280.00 USD | `-50.57%` | `155.91` |
| `Live` | `Long` | `1115.00` | 725,080,000.00 USD | 0.00 USD | 7,920,000.00 USD | `-50.13%` | `7,103.78` |
| `Live` | `Long` | `1125.00` | 717,160,000.00 USD | 0.00 USD | 158,830.00 USD | `-49.68%` | `141.18` |
| `Live` | `Long` | `1135.00` | 717,000,000.00 USD | 0.00 USD | 475,040.00 USD | `-49.23%` | `418.54` |
| `Live` | `Long` | `1145.00` | 716,530,000.00 USD | 0.00 USD | 196,970.00 USD | `-48.78%` | `172.02` |
| `Live` | `Long` | `1155.00` | 716,330,000.00 USD | 0.00 USD | 1,370,000.00 USD | `-48.34%` | `1,183.06` |
| `Live` | `Long` | `1165.00` | 714,960,000.00 USD | 0.00 USD | 72,300.00 USD | `-47.89%` | `62.06` |
| `Live` | `Long` | `1175.00` | 714,890,000.00 USD | 0.00 USD | 1,510,000.00 USD | `-47.44%` | `1,287.10` |
| `Live` | `Long` | `1185.00` | 713,380,000.00 USD | 0.00 USD | 2,110,000.00 USD | `-46.99%` | `1,782.41` |
| `Live` | `Long` | `1195.00` | 711,270,000.00 USD | 0.00 USD | 218,050.00 USD | `-46.55%` | `182.47` |
| `Live` | `Long` | `1205.00` | 711,050,000.00 USD | 0.00 USD | 185,340.00 USD | `-46.10%` | `153.81` |
| `Live` | `Long` | `1215.00` | 710,860,000.00 USD | 0.00 USD | 2,090,000.00 USD | `-45.65%` | `1,722.09` |
| `Live` | `Long` | `1225.00` | 708,770,000.00 USD | 0.00 USD | 556,370.00 USD | `-45.20%` | `454.18` |
| `Live` | `Long` | `1235.00` | 708,220,000.00 USD | 0.00 USD | 80,420.00 USD | `-44.76%` | `65.12` |
| `Live` | `Long` | `1245.00` | 708,140,000.00 USD | 0.00 USD | 819,550.00 USD | `-44.31%` | `658.27` |
| `Live` | `Long` | `1255.00` | 707,320,000.00 USD | 0.00 USD | 438,130.00 USD | `-43.86%` | `349.11` |
| `Live` | `Long` | `1265.00` | 706,880,000.00 USD | 0.00 USD | 1,690,000.00 USD | `-43.42%` | `1,333.36` |
| `Live` | `Long` | `1275.00` | 705,190,000.00 USD | 0.00 USD | 15,440,000.00 USD | `-42.97%` | `12,106.21` |
| `Live` | `Long` | `1285.00` | 689,760,000.00 USD | 0.00 USD | 279,440.00 USD | `-42.52%` | `217.46` |
| `Live` | `Long` | `1295.00` | 689,480,000.00 USD | 0.00 USD | 371,250.00 USD | `-42.07%` | `286.68` |
| `Live` | `Long` | `1305.00` | 689,100,000.00 USD | 0.00 USD | 268,590.00 USD | `-41.63%` | `205.82` |
| `Live` | `Long` | `1315.00` | 688,840,000.00 USD | 0.00 USD | 221,150.00 USD | `-41.18%` | `168.17` |
| `Live` | `Long` | `1325.00` | 688,610,000.00 USD | 0.00 USD | 506,670.00 USD | `-40.73%` | `382.39` |
| `Live` | `Long` | `1335.00` | 688,110,000.00 USD | 0.00 USD | 291,100.00 USD | `-40.28%` | `218.05` |
| `Live` | `Long` | `1345.00` | 687,820,000.00 USD | 0.00 USD | 5,390,000.00 USD | `-39.84%` | `4,007.93` |
| `Live` | `Long` | `1355.00` | 682,430,000.00 USD | 0.00 USD | 12,260,000.00 USD | `-39.39%` | `9,051.59` |
| `Live` | `Long` | `1365.00` | 670,160,000.00 USD | 0.00 USD | 1,910,000.00 USD | `-38.94%` | `1,400.32` |
| `Live` | `Long` | `1375.00` | 668,250,000.00 USD | 0.00 USD | 638,470.00 USD | `-38.50%` | `464.34` |
| `Live` | `Long` | `1385.00` | 667,610,000.00 USD | 0.00 USD | 9,170,000.00 USD | `-38.05%` | `6,620.74` |
| `Live` | `Long` | `1395.00` | 658,440,000.00 USD | 0.00 USD | 360,520.00 USD | `-37.60%` | `258.43` |
| `Live` | `Long` | `1405.00` | 658,080,000.00 USD | 0.00 USD | 9,980,000.00 USD | `-37.15%` | `7,106.18` |
| `Live` | `Long` | `1415.00` | 648,100,000.00 USD | 0.00 USD | 227,570.00 USD | `-36.71%` | `160.83` |
| `Live` | `Long` | `1425.00` | 647,870,000.00 USD | 0.00 USD | 2,650,000.00 USD | `-36.26%` | `1,861.05` |
| `Live` | `Long` | `1435.00` | 645,220,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-35.81%` | `788.81` |
| `Live` | `Long` | `1445.00` | 644,090,000.00 USD | 0.00 USD | 18,850,000.00 USD | `-35.36%` | `13,045.08` |
| `Live` | `Long` | `1455.00` | 625,240,000.00 USD | 0.00 USD | 335,310.00 USD | `-34.92%` | `230.46` |
| `Live` | `Long` | `1465.00` | 624,900,000.00 USD | 0.00 USD | 1,780,000.00 USD | `-34.47%` | `1,213.40` |
| `Live` | `Long` | `1475.00` | 623,120,000.00 USD | 0.00 USD | 12,160,000.00 USD | `-34.02%` | `8,245.10` |
| `Live` | `Long` | `1485.00` | 610,960,000.00 USD | 0.00 USD | 185,340.00 USD | `-33.57%` | `124.81` |
| `Live` | `Long` | `1495.00` | 610,780,000.00 USD | 0.00 USD | 158,690.00 USD | `-33.13%` | `106.15` |
| `Live` | `Long` | `1505.00` | 610,620,000.00 USD | 0.00 USD | 281,240.00 USD | `-32.68%` | `186.87` |
| `Live` | `Long` | `1515.00` | 610,340,000.00 USD | 0.00 USD | 729,610.00 USD | `-32.23%` | `481.59` |
| `Live` | `Long` | `1525.00` | 609,610,000.00 USD | 0.00 USD | 19,520,000.00 USD | `-31.79%` | `12,799.47` |
| `Live` | `Long` | `1535.00` | 590,090,000.00 USD | 0.00 USD | 989,140.00 USD | `-31.34%` | `644.39` |
| `Live` | `Long` | `1545.00` | 589,100,000.00 USD | 0.00 USD | 20,230,000.00 USD | `-30.89%` | `13,096.58` |
| `Live` | `Long` | `1555.00` | 568,860,000.00 USD | 0.00 USD | 410,620.00 USD | `-30.44%` | `264.07` |
| `Live` | `Long` | `1565.00` | 568,450,000.00 USD | 0.00 USD | 3,430,000.00 USD | `-30.00%` | `2,189.79` |
| `Live` | `Long` | `1575.00` | 565,030,000.00 USD | 0.00 USD | 267,000.00 USD | `-29.55%` | `169.52` |
| `Live` | `Long` | `1585.00` | 564,760,000.00 USD | 0.00 USD | 861,320.00 USD | `-29.10%` | `543.42` |
| `Live` | `Long` | `1595.00` | 563,900,000.00 USD | 0.00 USD | 1,620,000.00 USD | `-28.65%` | `1,016.02` |
| `Live` | `Long` | `1605.00` | 562,280,000.00 USD | 0.00 USD | 21,750,000.00 USD | `-28.21%` | `13,549.66` |
| `Live` | `Long` | `1615.00` | 540,530,000.00 USD | 0.00 USD | 173,560.00 USD | `-27.76%` | `107.47` |
| `Live` | `Long` | `1625.00` | 540,360,000.00 USD | 0.00 USD | 1,730,000.00 USD | `-27.31%` | `1,063.79` |
| `Live` | `Long` | `1635.00` | 538,630,000.00 USD | 0.00 USD | 18,480,000.00 USD | `-26.87%` | `11,302.69` |
| `Live` | `Long` | `1645.00` | 520,150,000.00 USD | 0.00 USD | 38,040,000.00 USD | `-26.42%` | `23,127.61` |
| `Live` | `Long` | `1655.00` | 482,100,000.00 USD | 0.00 USD | 925,200.00 USD | `-25.97%` | `559.04` |
| `Live` | `Long` | `1665.00` | 481,180,000.00 USD | 0.00 USD | 1,380,000.00 USD | `-25.52%` | `827.67` |
| `Live` | `Long` | `1675.00` | 479,800,000.00 USD | 0.00 USD | 12,260,000.00 USD | `-25.08%` | `7,317.76` |
| `Live` | `Long` | `1685.00` | 467,540,000.00 USD | 0.00 USD | 606,650.00 USD | `-24.63%` | `360.03` |
| `Live` | `Long` | `1695.00` | 466,940,000.00 USD | 0.00 USD | 417,600.00 USD | `-24.18%` | `246.37` |
| `Live` | `Long` | `1705.00` | 466,520,000.00 USD | 0.00 USD | 1,230,000.00 USD | `-23.73%` | `719.40` |
| `Live` | `Long` | `1715.00` | 465,290,000.00 USD | 0.00 USD | 575,210.00 USD | `-23.29%` | `335.40` |
| `Live` | `Long` | `1725.00` | 464,720,000.00 USD | 0.00 USD | 36,130,000.00 USD | `-22.84%` | `20,946.31` |
| `Live` | `Long` | `1735.00` | 428,580,000.00 USD | 0.00 USD | 1,540,000.00 USD | `-22.39%` | `884.90` |
| `Live` | `Long` | `1745.00` | 427,050,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-21.94%` | `748.72` |
| `Live` | `Long` | `1755.00` | 425,740,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-21.50%` | `652.04` |
| `Live` | `Long` | `1765.00` | 424,600,000.00 USD | 0.00 USD | 49,080,000.00 USD | `-21.05%` | `27,809.70` |
| `Live` | `Long` | `1775.00` | 375,510,000.00 USD | 0.00 USD | 734,410.00 USD | `-20.60%` | `413.75` |
| `Live` | `Long` | `1785.00` | 374,780,000.00 USD | 0.00 USD | 61,370,000.00 USD | `-20.16%` | `34,378.83` |
| `Live` | `Long` | `1795.00` | 313,410,000.00 USD | 0.00 USD | 495,870.00 USD | `-19.71%` | `276.25` |
| `Live` | `Long` | `1805.00` | 312,920,000.00 USD | 0.00 USD | 3,280,000.00 USD | `-19.26%` | `1,818.39` |
| `Live` | `Long` | `1815.00` | 309,630,000.00 USD | 0.00 USD | 805,460.00 USD | `-18.81%` | `443.78` |
| `Live` | `Long` | `1825.00` | 308,830,000.00 USD | 0.00 USD | 831,850.00 USD | `-18.37%` | `455.81` |
| `Live` | `Long` | `1835.00` | 308,000,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-17.92%` | `616.74` |
| `Live` | `Long` | `1845.00` | 306,870,000.00 USD | 0.00 USD | 27,870,000.00 USD | `-17.47%` | `15,105.40` |
| `Live` | `Long` | `1855.00` | 279,000,000.00 USD | 0.00 USD | 1,680,000.00 USD | `-17.02%` | `902.99` |
| `Live` | `Long` | `1865.00` | 277,320,000.00 USD | 0.00 USD | 3,380,000.00 USD | `-16.58%` | `1,812.38` |
| `Live` | `Long` | `1875.00` | 273,940,000.00 USD | 0.00 USD | 8,890,000.00 USD | `-16.13%` | `4,743.58` |
| `Live` | `Long` | `1885.00` | 265,050,000.00 USD | 0.00 USD | 5,830,000.00 USD | `-15.68%` | `3,091.11` |
| `Live` | `Long` | `1895.00` | 259,220,000.00 USD | 0.00 USD | 775,090.00 USD | `-15.24%` | `409.02` |
| `Live` | `Long` | `1905.00` | 258,450,000.00 USD | 0.00 USD | 490,530.00 USD | `-14.79%` | `257.49` |
| `Live` | `Long` | `1915.00` | 257,950,000.00 USD | 0.00 USD | 18,290,000.00 USD | `-14.34%` | `9,549.13` |
| `Live` | `Long` | `1925.00` | 239,670,000.00 USD | 0.00 USD | 16,340,000.00 USD | `-13.89%` | `8,487.98` |
| `Live` | `Long` | `1935.00` | 223,330,000.00 USD | 0.00 USD | 4,460,000.00 USD | `-13.45%` | `2,303.52` |
| `Live` | `Long` | `1945.00` | 218,870,000.00 USD | 0.00 USD | 1,690,000.00 USD | `-13.00%` | `868.61` |
| `Live` | `Long` | `1955.00` | 217,180,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-12.55%` | `658.39` |
| `Live` | `Long` | `1965.00` | 215,890,000.00 USD | 0.00 USD | 2,730,000.00 USD | `-12.10%` | `1,388.04` |
| `Live` | `Long` | `1975.00` | 213,170,000.00 USD | 0.00 USD | 1,950,000.00 USD | `-11.66%` | `988.92` |
| `Live` | `Long` | `1985.00` | 211,210,000.00 USD | 0.00 USD | 5,060,000.00 USD | `-11.21%` | `2,551.23` |
| `Live` | `Long` | `1995.00` | 206,150,000.00 USD | 0.00 USD | 1,560,000.00 USD | `-10.76%` | `784.10` |
| `Live` | `Long` | `2005.00` | 204,590,000.00 USD | 0.00 USD | 2,090,000.00 USD | `-10.31%` | `1,040.05` |
| `Live` | `Long` | `2015.00` | 202,500,000.00 USD | 0.00 USD | 5,730,000.00 USD | `-9.87%` | `2,845.12` |
| `Live` | `Long` | `2025.00` | 196,770,000.00 USD | 0.00 USD | 2,100,000.00 USD | `-9.42%` | `1,036.53` |
| `Live` | `Long` | `2035.00` | 194,670,000.00 USD | 0.00 USD | 1,080,000.00 USD | `-8.97%` | `529.82` |
| `Live` | `Long` | `2045.00` | 193,590,000.00 USD | 0.00 USD | 2,000,000.00 USD | `-8.53%` | `978.79` |
| `Live` | `Long` | `2055.00` | 191,590,000.00 USD | 0.00 USD | 5,940,000.00 USD | `-8.08%` | `2,892.90` |
| `Live` | `Long` | `2065.00` | 185,640,000.00 USD | 0.00 USD | 13,860,000.00 USD | `-7.63%` | `6,714.08` |
| `Live` | `Long` | `2075.00` | 171,780,000.00 USD | 0.00 USD | 2,720,000.00 USD | `-7.18%` | `1,312.25` |
| `Live` | `Long` | `2085.00` | 169,060,000.00 USD | 0.00 USD | 13,600,000.00 USD | `-6.74%` | `6,524.51` |
| `Live` | `Long` | `2095.00` | 155,450,000.00 USD | 0.00 USD | 1,380,000.00 USD | `-6.29%` | `657.96` |
| `Live` | `Long` | `2105.00` | 154,070,000.00 USD | 0.00 USD | 2,280,000.00 USD | `-5.84%` | `1,083.78` |
| `Live` | `Long` | `2115.00` | 151,790,000.00 USD | 0.00 USD | 2,910,000.00 USD | `-5.39%` | `1,375.04` |
| `Live` | `Long` | `2125.00` | 148,880,000.00 USD | 0.00 USD | 123,240,000.00 USD | `-4.95%` | `57,997.47` |
| `Live` | `Long` | `2135.00` | 25,640,000.00 USD | 0.00 USD | 4,840,000.00 USD | `-4.50%` | `2,266.48` |
| `Live` | `Long` | `2145.00` | 20,800,000.00 USD | 0.00 USD | 5,020,000.00 USD | `-4.05%` | `2,339.37` |
| `Live` | `Long` | `2155.00` | 15,780,000.00 USD | 0.00 USD | 3,970,000.00 USD | `-3.61%` | `1,844.11` |
| `Live` | `Long` | `2165.00` | 11,810,000.00 USD | 0.00 USD | 5,390,000.00 USD | `-3.16%` | `2,491.34` |
| `Live` | `Long` | `2175.00` | 6,420,000.00 USD | 0.00 USD | 5,680,000.00 USD | `-2.71%` | `2,613.45` |
| `Live` | `Long` | `2185.00` | 731,220.00 USD | 0.00 USD | 618,490.00 USD | `-2.26%` | `283.06` |
| `Live` | `Long` | `2195.00` | 112,730.00 USD | 0.00 USD | 107,420.00 USD | `-1.82%` | `48.94` |
| `Live` | `Long` | `2205.00` | 5,310.00 USD | 0.00 USD | 5,310.00 USD | `-1.37%` | `2.41` |
| `Live` | `Short` | `2235.00` | 14,960.00 USD | 14,960.00 USD | 0.00 USD | `-0.03%` | `6.69` |
| `Live` | `Short` | `2245.00` | 1,810,000.00 USD | 1,800,000.00 USD | 0.00 USD | `+0.42%` | `800.01` |
| `Live` | `Short` | `2255.00` | 4,780,000.00 USD | 2,970,000.00 USD | 0.00 USD | `+0.87%` | `1,316.55` |
| `Live` | `Short` | `2265.00` | 7,090,000.00 USD | 2,310,000.00 USD | 0.00 USD | `+1.32%` | `1,017.91` |
| `Live` | `Short` | `2275.00` | 7,360,000.00 USD | 276,460.00 USD | 0.00 USD | `+1.76%` | `121.52` |
| `Live` | `Short` | `2285.00` | 8,130,000.00 USD | 767,790.00 USD | 0.00 USD | `+2.21%` | `336.01` |
| `Live` | `Short` | `2295.00` | 11,970,000.00 USD | 3,840,000.00 USD | 0.00 USD | `+2.66%` | `1,671.21` |
| `Live` | `Short` | `2305.00` | 12,230,000.00 USD | 266,780.00 USD | 0.00 USD | `+3.10%` | `115.74` |
| `Live` | `Short` | `2315.00` | 13,240,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+3.55%` | `436.72` |
| `Live` | `Short` | `2325.00` | 15,240,000.00 USD | 1,990,000.00 USD | 0.00 USD | `+4.00%` | `857.57` |
| `Live` | `Short` | `2335.00` | 16,070,000.00 USD | 828,820.00 USD | 0.00 USD | `+4.45%` | `354.95` |
| `Live` | `Short` | `2345.00` | 16,180,000.00 USD | 109,700.00 USD | 0.00 USD | `+4.89%` | `46.78` |
| `Live` | `Short` | `2355.00` | 17,400,000.00 USD | 1,220,000.00 USD | 0.00 USD | `+5.34%` | `520.12` |
| `Live` | `Short` | `2365.00` | 21,280,000.00 USD | 3,880,000.00 USD | 0.00 USD | `+5.79%` | `1,640.01` |
| `Live` | `Short` | `2375.00` | 22,170,000.00 USD | 894,650.00 USD | 0.00 USD | `+6.24%` | `376.69` |
| `Live` | `Short` | `2385.00` | 27,940,000.00 USD | 5,770,000.00 USD | 0.00 USD | `+6.68%` | `2,419.12` |
| `Live` | `Short` | `2395.00` | 28,100,000.00 USD | 155,990.00 USD | 0.00 USD | `+7.13%` | `65.13` |
| `Live` | `Short` | `2405.00` | 28,290,000.00 USD | 190,970.00 USD | 0.00 USD | `+7.58%` | `79.41` |
| `Live` | `Short` | `2415.00` | 28,450,000.00 USD | 164,460.00 USD | 0.00 USD | `+8.02%` | `68.10` |
| `Live` | `Short` | `2425.00` | 29,630,000.00 USD | 1,180,000.00 USD | 0.00 USD | `+8.47%` | `485.23` |
| `Live` | `Short` | `2435.00` | 29,830,000.00 USD | 198,530.00 USD | 0.00 USD | `+8.92%` | `81.53` |
| `Live` | `Short` | `2445.00` | 29,900,000.00 USD | 66,330.00 USD | 0.00 USD | `+9.37%` | `27.13` |
| `Live` | `Short` | `2455.00` | 30,080,000.00 USD | 186,790.00 USD | 0.00 USD | `+9.81%` | `76.09` |
| `Live` | `Short` | `2465.00` | 95,850,000.00 USD | 65,770,000.00 USD | 0.00 USD | `+10.26%` | `26,680.74` |
| `Live` | `Short` | `2475.00` | 96,490,000.00 USD | 641,630.00 USD | 0.00 USD | `+10.71%` | `259.24` |
| `Live` | `Short` | `2485.00` | 98,130,000.00 USD | 1,640,000.00 USD | 0.00 USD | `+11.16%` | `659.67` |
| `Live` | `Short` | `2495.00` | 104,510,000.00 USD | 6,380,000.00 USD | 0.00 USD | `+11.60%` | `2,558.44` |
| `Live` | `Short` | `2505.00` | 108,960,000.00 USD | 4,450,000.00 USD | 0.00 USD | `+12.05%` | `1,774.79` |
| `Live` | `Short` | `2515.00` | 109,660,000.00 USD | 700,300.00 USD | 0.00 USD | `+12.50%` | `278.45` |
| `Live` | `Short` | `2525.00` | 114,790,000.00 USD | 5,130,000.00 USD | 0.00 USD | `+12.95%` | `2,030.53` |
| `Live` | `Short` | `2535.00` | 115,640,000.00 USD | 854,240.00 USD | 0.00 USD | `+13.39%` | `336.98` |
| `Live` | `Short` | `2545.00` | 115,820,000.00 USD | 173,450.00 USD | 0.00 USD | `+13.84%` | `68.15` |
| `Live` | `Short` | `2555.00` | 128,200,000.00 USD | 12,390,000.00 USD | 0.00 USD | `+14.29%` | `4,848.05` |
| `Live` | `Short` | `2565.00` | 128,260,000.00 USD | 60,800.00 USD | 0.00 USD | `+14.73%` | `23.70` |
| `Live` | `Short` | `2575.00` | 128,300,000.00 USD | 41,530.00 USD | 0.00 USD | `+15.18%` | `16.13` |
| `Live` | `Short` | `2585.00` | 154,820,000.00 USD | 26,520,000.00 USD | 0.00 USD | `+15.63%` | `10,257.58` |
| `Live` | `Short` | `2595.00` | 154,860,000.00 USD | 41,560.00 USD | 0.00 USD | `+16.08%` | `16.02` |
| `Live` | `Short` | `2605.00` | 160,960,000.00 USD | 6,100,000.00 USD | 0.00 USD | `+16.52%` | `2,339.77` |
| `Live` | `Short` | `2615.00` | 161,150,000.00 USD | 190,200.00 USD | 0.00 USD | `+16.97%` | `72.73` |
| `Live` | `Short` | `2625.00` | 194,320,000.00 USD | 33,170,000.00 USD | 0.00 USD | `+17.42%` | `12,636.25` |
| `Live` | `Short` | `2635.00` | 195,260,000.00 USD | 942,760.00 USD | 0.00 USD | `+17.87%` | `357.78` |
| `Live` | `Short` | `2645.00` | 204,090,000.00 USD | 8,830,000.00 USD | 0.00 USD | `+18.31%` | `3,339.12` |
| `Live` | `Short` | `2655.00` | 230,170,000.00 USD | 26,080,000.00 USD | 0.00 USD | `+18.76%` | `9,822.32` |
| `Live` | `Short` | `2665.00` | 230,310,000.00 USD | 135,770.00 USD | 0.00 USD | `+19.21%` | `50.95` |
| `Live` | `Short` | `2675.00` | 234,690,000.00 USD | 4,390,000.00 USD | 0.00 USD | `+19.65%` | `1,639.29` |
| `Live` | `Short` | `2685.00` | 234,750,000.00 USD | 60,700.00 USD | 0.00 USD | `+20.10%` | `22.61` |
| `Live` | `Short` | `2695.00` | 240,970,000.00 USD | 6,220,000.00 USD | 0.00 USD | `+20.55%` | `2,308.75` |
| `Live` | `Short` | `2705.00` | 241,690,000.00 USD | 718,530.00 USD | 0.00 USD | `+21.00%` | `265.63` |
| `Live` | `Short` | `2715.00` | 242,030,000.00 USD | 335,440.00 USD | 0.00 USD | `+21.44%` | `123.55` |
| `Live` | `Short` | `2725.00` | 242,330,000.00 USD | 303,970.00 USD | 0.00 USD | `+21.89%` | `111.55` |
| `Live` | `Short` | `2735.00` | 242,470,000.00 USD | 133,470.00 USD | 0.00 USD | `+22.34%` | `48.80` |
| `Live` | `Short` | `2745.00` | 243,350,000.00 USD | 887,740.00 USD | 0.00 USD | `+22.79%` | `323.40` |
| `Live` | `Short` | `2755.00` | 249,130,000.00 USD | 5,770,000.00 USD | 0.00 USD | `+23.23%` | `2,094.89` |
| `Live` | `Short` | `2765.00` | 249,150,000.00 USD | 28,570.00 USD | 0.00 USD | `+23.68%` | `10.33` |
| `Live` | `Short` | `2775.00` | 262,530,000.00 USD | 13,380,000.00 USD | 0.00 USD | `+24.13%` | `4,821.07` |
| `Live` | `Short` | `2785.00` | 262,590,000.00 USD | 57,740.00 USD | 0.00 USD | `+24.58%` | `20.73` |
| `Live` | `Short` | `2795.00` | 285,060,000.00 USD | 22,470,000.00 USD | 0.00 USD | `+25.02%` | `8,038.21` |
| `Live` | `Short` | `2805.00` | 288,920,000.00 USD | 3,870,000.00 USD | 0.00 USD | `+25.47%` | `1,378.27` |
| `Live` | `Short` | `2815.00` | 290,080,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+25.92%` | `412.30` |
| `Live` | `Short` | `2825.00` | 290,750,000.00 USD | 668,010.00 USD | 0.00 USD | `+26.36%` | `236.46` |
| `Live` | `Short` | `2835.00` | 296,920,000.00 USD | 6,160,000.00 USD | 0.00 USD | `+26.81%` | `2,174.33` |
| `Live` | `Short` | `2845.00` | 297,160,000.00 USD | 246,080.00 USD | 0.00 USD | `+27.26%` | `86.50` |
| `Live` | `Short` | `2855.00` | 297,560,000.00 USD | 396,550.00 USD | 0.00 USD | `+27.71%` | `138.90` |
| `Live` | `Short` | `2865.00` | 297,630,000.00 USD | 73,290.00 USD | 0.00 USD | `+28.15%` | `25.58` |
| `Live` | `Short` | `2875.00` | 297,680,000.00 USD | 50,280.00 USD | 0.00 USD | `+28.60%` | `17.49` |
| `Live` | `Short` | `2885.00` | 298,650,000.00 USD | 963,300.00 USD | 0.00 USD | `+29.05%` | `333.90` |
| `Live` | `Short` | `2895.00` | 300,020,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+29.50%` | `476.62` |
| `Live` | `Short` | `2905.00` | 301,730,000.00 USD | 1,700,000.00 USD | 0.00 USD | `+29.94%` | `585.57` |
| `Live` | `Short` | `2915.00` | 304,930,000.00 USD | 3,200,000.00 USD | 0.00 USD | `+30.39%` | `1,098.53` |
| `Live` | `Short` | `2925.00` | 331,460,000.00 USD | 26,530,000.00 USD | 0.00 USD | `+30.84%` | `9,070.32` |
| `Live` | `Short` | `2935.00` | 331,500,000.00 USD | 44,150.00 USD | 0.00 USD | `+31.28%` | `15.04` |
| `Live` | `Short` | `2945.00` | 332,080,000.00 USD | 573,180.00 USD | 0.00 USD | `+31.73%` | `194.63` |
| `Live` | `Short` | `2955.00` | 333,170,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+32.18%` | `371.35` |
| `Live` | `Short` | `2965.00` | 336,980,000.00 USD | 3,810,000.00 USD | 0.00 USD | `+32.63%` | `1,284.32` |
| `Live` | `Short` | `2975.00` | 337,030,000.00 USD | 44,270.00 USD | 0.00 USD | `+33.07%` | `14.88` |
| `Live` | `Short` | `2985.00` | 337,170,000.00 USD | 145,060.00 USD | 0.00 USD | `+33.52%` | `48.59` |
| `Live` | `Short` | `2995.00` | 339,400,000.00 USD | 2,230,000.00 USD | 0.00 USD | `+33.97%` | `745.91` |
| `Live` | `Short` | `3005.00` | 339,930,000.00 USD | 525,050.00 USD | 0.00 USD | `+34.42%` | `174.73` |
| `Live` | `Short` | `3015.00` | 360,400,000.00 USD | 20,470,000.00 USD | 0.00 USD | `+34.86%` | `6,790.86` |
| `Live` | `Short` | `3025.00` | 361,250,000.00 USD | 842,230.00 USD | 0.00 USD | `+35.31%` | `278.42` |
| `Live` | `Short` | `3035.00` | 375,300,000.00 USD | 14,060,000.00 USD | 0.00 USD | `+35.76%` | `4,631.24` |
| `Live` | `Short` | `3045.00` | 375,320,000.00 USD | 19,540.00 USD | 0.00 USD | `+36.21%` | `6.42` |
| `Live` | `Short` | `3055.00` | 379,330,000.00 USD | 4,000,000.00 USD | 0.00 USD | `+36.65%` | `1,310.70` |
| `Live` | `Short` | `3065.00` | 381,630,000.00 USD | 2,300,000.00 USD | 0.00 USD | `+37.10%` | `752.00` |
| `Live` | `Short` | `3075.00` | 381,670,000.00 USD | 42,140.00 USD | 0.00 USD | `+37.55%` | `13.70` |
| `Live` | `Short` | `3085.00` | 384,960,000.00 USD | 3,290,000.00 USD | 0.00 USD | `+37.99%` | `1,065.07` |
| `Live` | `Short` | `3095.00` | 385,890,000.00 USD | 936,010.00 USD | 0.00 USD | `+38.44%` | `302.43` |
| `Live` | `Short` | `3105.00` | 387,550,000.00 USD | 1,650,000.00 USD | 0.00 USD | `+38.89%` | `532.75` |
| `Live` | `Short` | `3115.00` | 389,450,000.00 USD | 1,900,000.00 USD | 0.00 USD | `+39.34%` | `609.45` |
| `Live` | `Short` | `3125.00` | 389,880,000.00 USD | 431,960.00 USD | 0.00 USD | `+39.78%` | `138.23` |
| `Live` | `Short` | `3135.00` | 396,250,000.00 USD | 6,370,000.00 USD | 0.00 USD | `+40.23%` | `2,031.12` |
| `Live` | `Short` | `3145.00` | 401,100,000.00 USD | 4,860,000.00 USD | 0.00 USD | `+40.68%` | `1,544.24` |
| `Live` | `Short` | `3155.00` | 430,670,000.00 USD | 29,560,000.00 USD | 0.00 USD | `+41.13%` | `9,370.55` |
| `Live` | `Short` | `3165.00` | 430,670,000.00 USD | 7,040.00 USD | 0.00 USD | `+41.57%` | `2.22` |
| `Live` | `Short` | `3175.00` | 431,530,000.00 USD | 859,400.00 USD | 0.00 USD | `+42.02%` | `270.68` |
| `Live` | `Short` | `3185.00` | 438,450,000.00 USD | 6,910,000.00 USD | 0.00 USD | `+42.47%` | `2,169.99` |
| `Live` | `Short` | `3195.00` | 442,140,000.00 USD | 3,690,000.00 USD | 0.00 USD | `+42.91%` | `1,156.01` |
| `Live` | `Short` | `3205.00` | 442,700,000.00 USD | 556,050.00 USD | 0.00 USD | `+43.36%` | `173.49` |
| `Live` | `Short` | `3215.00` | 442,850,000.00 USD | 156,500.00 USD | 0.00 USD | `+43.81%` | `48.68` |
| `Live` | `Short` | `3225.00` | 452,700,000.00 USD | 9,840,000.00 USD | 0.00 USD | `+44.26%` | `3,052.67` |
| `Live` | `Short` | `3235.00` | 462,680,000.00 USD | 9,980,000.00 USD | 0.00 USD | `+44.70%` | `3,086.34` |
| `Live` | `Short` | `3245.00` | 471,150,000.00 USD | 8,460,000.00 USD | 0.00 USD | `+45.15%` | `2,608.61` |
| `Live` | `Short` | `3255.00` | 471,170,000.00 USD | 26,830.00 USD | 0.00 USD | `+45.60%` | `8.24` |
| `Live` | `Short` | `3265.00` | 471,310,000.00 USD | 137,380.00 USD | 0.00 USD | `+46.05%` | `42.08` |
| `Live` | `Short` | `3275.00` | 484,720,000.00 USD | 13,410,000.00 USD | 0.00 USD | `+46.49%` | `4,095.83` |
| `Live` | `Short` | `3285.00` | 484,790,000.00 USD | 69,380.00 USD | 0.00 USD | `+46.94%` | `21.12` |
| `Live` | `Short` | `3295.00` | 485,110,000.00 USD | 321,720.00 USD | 0.00 USD | `+47.39%` | `97.64` |
| `Live` | `Short` | `3305.00` | 486,300,000.00 USD | 1,190,000.00 USD | 0.00 USD | `+47.84%` | `359.09` |
| `Live` | `Short` | `3315.00` | 488,490,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+48.28%` | `659.46` |
| `Live` | `Short` | `3325.00` | 488,550,000.00 USD | 60,520.00 USD | 0.00 USD | `+48.73%` | `18.20` |
| `Live` | `Short` | `3335.00` | 492,740,000.00 USD | 4,190,000.00 USD | 0.00 USD | `+49.18%` | `1,255.39` |
| `Live` | `Short` | `3345.00` | 493,460,000.00 USD | 727,550.00 USD | 0.00 USD | `+49.62%` | `217.50` |
| `Live` | `Short` | `3355.00` | 493,530,000.00 USD | 64,090.00 USD | 0.00 USD | `+50.07%` | `19.10` |
| `Live` | `Short` | `3365.00` | 495,320,000.00 USD | 1,790,000.00 USD | 0.00 USD | `+50.52%` | `531.66` |
| `Live` | `Short` | `3375.00` | 495,320,000.00 USD | 1,920.00 USD | 0.00 USD | `+50.97%` | `0.57` |
| `Live` | `Short` | `3385.00` | 495,420,000.00 USD | 100,850.00 USD | 0.00 USD | `+51.41%` | `29.79` |
| `Live` | `Short` | `3395.00` | 497,020,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+51.86%` | `472.54` |
| `Live` | `Short` | `3405.00` | 499,780,000.00 USD | 2,760,000.00 USD | 0.00 USD | `+52.31%` | `810.94` |
| `Live` | `Short` | `3415.00` | 499,820,000.00 USD | 39,930.00 USD | 0.00 USD | `+52.76%` | `11.69` |
| `Live` | `Short` | `3425.00` | 514,800,000.00 USD | 14,970,000.00 USD | 0.00 USD | `+53.20%` | `4,371.38` |
| `Live` | `Short` | `3435.00` | 515,190,000.00 USD | 395,100.00 USD | 0.00 USD | `+53.65%` | `115.02` |
| `Live` | `Short` | `3445.00` | 515,730,000.00 USD | 539,570.00 USD | 0.00 USD | `+54.10%` | `156.62` |
| `Live` | `Short` | `3455.00` | 516,430,000.00 USD | 697,920.00 USD | 0.00 USD | `+54.54%` | `202.00` |
| `Live` | `Short` | `3465.00` | 517,010,000.00 USD | 585,240.00 USD | 0.00 USD | `+54.99%` | `168.90` |
| `Live` | `Short` | `3475.00` | 577,590,000.00 USD | 60,570,000.00 USD | 0.00 USD | `+55.44%` | `17,431.48` |
| `Live` | `Short` | `3485.00` | 577,640,000.00 USD | 50,550.00 USD | 0.00 USD | `+55.89%` | `14.50` |
| `Live` | `Short` | `3495.00` | 580,140,000.00 USD | 2,510,000.00 USD | 0.00 USD | `+56.33%` | `716.87` |
| `Live` | `Short` | `3505.00` | 581,080,000.00 USD | 934,520.00 USD | 0.00 USD | `+56.78%` | `266.62` |
| `Live` | `Short` | `3515.00` | 581,090,000.00 USD | 6,450.00 USD | 0.00 USD | `+57.23%` | `1.84` |
| `Live` | `Short` | `3525.00` | 581,210,000.00 USD | 123,270.00 USD | 0.00 USD | `+57.68%` | `34.97` |
| `Live` | `Short` | `3535.00` | 581,480,000.00 USD | 272,480.00 USD | 0.00 USD | `+58.12%` | `77.08` |
| `Live` | `Short` | `3545.00` | 581,480,000.00 USD | 3,540.00 USD | 0.00 USD | `+58.57%` | `1.00` |
| `Live` | `Short` | `3555.00` | 581,730,000.00 USD | 245,580.00 USD | 0.00 USD | `+59.02%` | `69.08` |
| `Live` | `Short` | `3565.00` | 581,910,000.00 USD | 178,960.00 USD | 0.00 USD | `+59.47%` | `50.20` |
| `Live` | `Short` | `3575.00` | 582,080,000.00 USD | 173,450.00 USD | 0.00 USD | `+59.91%` | `48.52` |
| `Live` | `Short` | `3585.00` | 597,310,000.00 USD | 15,230,000.00 USD | 0.00 USD | `+60.36%` | `4,246.92` |
| `Live` | `Short` | `3595.00` | 597,340,000.00 USD | 31,710.00 USD | 0.00 USD | `+60.81%` | `8.82` |
| `Live` | `Short` | `3605.00` | 629,200,000.00 USD | 31,860,000.00 USD | 0.00 USD | `+61.25%` | `8,837.71` |
| `Live` | `Short` | `3615.00` | 632,940,000.00 USD | 3,740,000.00 USD | 0.00 USD | `+61.70%` | `1,034.22` |
| `Live` | `Short` | `3625.00` | 633,410,000.00 USD | 469,100.00 USD | 0.00 USD | `+62.15%` | `129.41` |
| `Live` | `Short` | `3635.00` | 642,150,000.00 USD | 8,740,000.00 USD | 0.00 USD | `+62.60%` | `2,405.67` |
| `Live` | `Short` | `3645.00` | 642,610,000.00 USD | 463,140.00 USD | 0.00 USD | `+63.04%` | `127.06` |
| `Live` | `Short` | `3655.00` | 649,230,000.00 USD | 6,610,000.00 USD | 0.00 USD | `+63.49%` | `1,808.73` |
| `Live` | `Short` | `3665.00` | 649,590,000.00 USD | 367,440.00 USD | 0.00 USD | `+63.94%` | `100.26` |
| `Live` | `Short` | `3675.00` | 649,630,000.00 USD | 39,370.00 USD | 0.00 USD | `+64.39%` | `10.71` |
| `Live` | `Short` | `3685.00` | 650,660,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+64.83%` | `280.18` |
| `Live` | `Short` | `3695.00` | 650,710,000.00 USD | 46,230.00 USD | 0.00 USD | `+65.28%` | `12.51` |
| `Live` | `Short` | `3705.00` | 650,720,000.00 USD | 3,950.00 USD | 0.00 USD | `+65.73%` | `1.07` |
| `Live` | `Short` | `3715.00` | 650,850,000.00 USD | 132,370.00 USD | 0.00 USD | `+66.17%` | `35.63` |
| `Live` | `Short` | `3725.00` | 651,270,000.00 USD | 418,150.00 USD | 0.00 USD | `+66.62%` | `112.25` |
| `Live` | `Short` | `3735.00` | 651,630,000.00 USD | 360,230.00 USD | 0.00 USD | `+67.07%` | `96.45` |
| `Live` | `Short` | `3745.00` | 652,800,000.00 USD | 1,180,000.00 USD | 0.00 USD | `+67.52%` | `314.41` |
| `Live` | `Short` | `3755.00` | 655,650,000.00 USD | 2,850,000.00 USD | 0.00 USD | `+67.96%` | `759.19` |
| `Live` | `Short` | `3765.00` | 655,870,000.00 USD | 211,050.00 USD | 0.00 USD | `+68.41%` | `56.06` |
| `Live` | `Short` | `3775.00` | 658,710,000.00 USD | 2,850,000.00 USD | 0.00 USD | `+68.86%` | `754.67` |
| `Live` | `Short` | `3785.00` | 658,740,000.00 USD | 27,580.00 USD | 0.00 USD | `+69.31%` | `7.29` |
| `Live` | `Short` | `3795.00` | 1,060,000,000.00 USD | 403,860,000.00 USD | 0.00 USD | `+69.75%` | `106,419.56` |
| `Live` | `Short` | `3805.00` | 1,060,000,000.00 USD | 292,660.00 USD | 0.00 USD | `+70.20%` | `76.92` |
| `Live` | `Short` | `3815.00` | 1,060,000,000.00 USD | 78,710.00 USD | 0.00 USD | `+70.65%` | `20.63` |
| `Live` | `Short` | `3825.00` | 1,060,000,000.00 USD | 115,590.00 USD | 0.00 USD | `+71.10%` | `30.22` |
| `Live` | `Short` | `3835.00` | 1,070,000,000.00 USD | 5,840,000.00 USD | 0.00 USD | `+71.54%` | `1,522.33` |
| `Live` | `Short` | `3845.00` | 1,070,000,000.00 USD | 2,720,000.00 USD | 0.00 USD | `+71.99%` | `708.00` |
| `Live` | `Short` | `3855.00` | 1,070,000,000.00 USD | 210,430.00 USD | 0.00 USD | `+72.44%` | `54.59` |
| `Live` | `Short` | `3865.00` | 1,070,000,000.00 USD | 2,920,000.00 USD | 0.00 USD | `+72.88%` | `756.35` |
| `Live` | `Short` | `3875.00` | 1,110,000,000.00 USD | 35,780,000.00 USD | 0.00 USD | `+73.33%` | `9,234.49` |
| `Live` | `Short` | `3885.00` | 1,110,000,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+73.78%` | `354.42` |
| `Live` | `Short` | `3895.00` | 1,110,000,000.00 USD | 1,950,000.00 USD | 0.00 USD | `+74.23%` | `499.88` |
| `Live` | `Short` | `3905.00` | 1,110,000,000.00 USD | 514,850.00 USD | 0.00 USD | `+74.67%` | `131.84` |
| `Live` | `Short` | `3915.00` | 1,110,000,000.00 USD | 503,000.00 USD | 0.00 USD | `+75.12%` | `128.48` |
| `Live` | `Short` | `3925.00` | 1,180,000,000.00 USD | 64,110,000.00 USD | 0.00 USD | `+75.57%` | `16,332.74` |
| `Live` | `Short` | `3935.00` | 1,180,000,000.00 USD | 4,610.00 USD | 0.00 USD | `+76.02%` | `1.17` |
| `Live` | `Short` | `3945.00` | 1,180,000,000.00 USD | 42,130.00 USD | 0.00 USD | `+76.46%` | `10.68` |
| `Live` | `Short` | `3955.00` | 1,180,000,000.00 USD | 101,980.00 USD | 0.00 USD | `+76.91%` | `25.79` |
| `Live` | `Short` | `3965.00` | 1,180,000,000.00 USD | 57,950.00 USD | 0.00 USD | `+77.36%` | `14.62` |
| `Live` | `Short` | `3975.00` | 1,180,000,000.00 USD | 566,890.00 USD | 0.00 USD | `+77.80%` | `142.61` |
| `Live` | `Short` | `3985.00` | 1,180,000,000.00 USD | 1,080,000.00 USD | 0.00 USD | `+78.25%` | `269.88` |
| `Live` | `Short` | `3995.00` | 1,180,000,000.00 USD | 360,060.00 USD | 0.00 USD | `+78.70%` | `90.13` |
| `Live` | `Short` | `4005.00` | 1,180,000,000.00 USD | 627,270.00 USD | 0.00 USD | `+79.15%` | `156.62` |
| `Live` | `Short` | `4015.00` | 1,180,000,000.00 USD | 81,790.00 USD | 0.00 USD | `+79.59%` | `20.37` |
| `Live` | `Short` | `4025.00` | 1,180,000,000.00 USD | 557,880.00 USD | 0.00 USD | `+80.04%` | `138.60` |
| `Live` | `Short` | `4035.00` | 1,180,000,000.00 USD | 90,960.00 USD | 0.00 USD | `+80.49%` | `22.54` |
| `Live` | `Short` | `4045.00` | 1,180,000,000.00 USD | 7,890.00 USD | 0.00 USD | `+80.94%` | `1.95` |
| `Live` | `Short` | `4055.00` | 1,180,000,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+81.38%` | `430.96` |
| `Live` | `Short` | `4065.00` | 1,180,000,000.00 USD | 154.47 USD | 0.00 USD | `+81.83%` | `0.04` |
| `Live` | `Short` | `4075.00` | 1,180,000,000.00 USD | 474,720.00 USD | 0.00 USD | `+82.28%` | `116.50` |
| `Live` | `Short` | `4085.00` | 1,180,000,000.00 USD | 9,960.00 USD | 0.00 USD | `+82.72%` | `2.44` |
| `Live` | `Short` | `4095.00` | 1,180,000,000.00 USD | 425.47 USD | 0.00 USD | `+83.17%` | `0.10` |
| `Live` | `Short` | `4105.00` | 1,180,000,000.00 USD | 107,050.00 USD | 0.00 USD | `+83.62%` | `26.08` |
| `Live` | `Short` | `4115.00` | 1,190,000,000.00 USD | 2,530,000.00 USD | 0.00 USD | `+84.07%` | `614.66` |
| `Live` | `Short` | `4125.00` | 1,190,000,000.00 USD | 233,750.00 USD | 0.00 USD | `+84.51%` | `56.67` |
| `Live` | `Short` | `4135.00` | 1,190,000,000.00 USD | 173,010.00 USD | 0.00 USD | `+84.96%` | `41.84` |
| `Live` | `Short` | `4145.00` | 1,190,000,000.00 USD | 710,240.00 USD | 0.00 USD | `+85.41%` | `171.35` |
| `Live` | `Short` | `4155.00` | 1,190,000,000.00 USD | 85,310.00 USD | 0.00 USD | `+85.86%` | `20.53` |
| `Live` | `Short` | `4165.00` | 1,190,000,000.00 USD | 1,420,000.00 USD | 0.00 USD | `+86.30%` | `340.64` |
| `Live` | `Short` | `4175.00` | 1,190,000,000.00 USD | 235,900.00 USD | 0.00 USD | `+86.75%` | `56.50` |
| `Live` | `Short` | `4185.00` | 1,190,000,000.00 USD | 872,460.00 USD | 0.00 USD | `+87.20%` | `208.47` |
| `Live` | `Short` | `4195.00` | 1,280,000,000.00 USD | 85,150,000.00 USD | 0.00 USD | `+87.65%` | `20,298.72` |
| `Live` | `Short` | `4205.00` | 1,280,000,000.00 USD | 6,130,000.00 USD | 0.00 USD | `+88.09%` | `1,458.02` |
| `Live` | `Short` | `4215.00` | 1,280,000,000.00 USD | 81,810.00 USD | 0.00 USD | `+88.54%` | `19.41` |
| `Live` | `Short` | `4235.00` | 1,310,000,000.00 USD | 29,040,000.00 USD | 0.00 USD | `+89.43%` | `6,856.86` |
| `Live` | `Short` | `4245.00` | 1,310,000,000.00 USD | 29,900.00 USD | 0.00 USD | `+89.88%` | `7.04` |
| `Live` | `Short` | `4255.00` | 1,320,000,000.00 USD | 5,310,000.00 USD | 0.00 USD | `+90.33%` | `1,248.54` |
| `Live` | `Short` | `4265.00` | 1,320,000,000.00 USD | 54,650.00 USD | 0.00 USD | `+90.78%` | `12.81` |
| `Live` | `Short` | `4275.00` | 1,320,000,000.00 USD | 4,060.00 USD | 0.00 USD | `+91.22%` | `0.95` |
| `Live` | `Short` | `4285.00` | 1,320,000,000.00 USD | 59,170.00 USD | 0.00 USD | `+91.67%` | `13.81` |
| `Live` | `Short` | `4295.00` | 1,320,000,000.00 USD | 108,920.00 USD | 0.00 USD | `+92.12%` | `25.36` |
| `Live` | `Short` | `4305.00` | 1,320,000,000.00 USD | 140,630.00 USD | 0.00 USD | `+92.57%` | `32.67` |
| `Live` | `Short` | `4315.00` | 1,320,000,000.00 USD | 625,670.00 USD | 0.00 USD | `+93.01%` | `145.00` |
| `Live` | `Short` | `4325.00` | 1,320,000,000.00 USD | 229,040.00 USD | 0.00 USD | `+93.46%` | `52.96` |
| `Live` | `Short` | `4335.00` | 1,320,000,000.00 USD | 4,100,000.00 USD | 0.00 USD | `+93.91%` | `946.60` |
| `Live` | `Short` | `4345.00` | 1,600,000,000.00 USD | 281,060,000.00 USD | 0.00 USD | `+94.35%` | `64,685.76` |
| `Live` | `Short` | `4355.00` | 1,600,000,000.00 USD | 508,850.00 USD | 0.00 USD | `+94.80%` | `116.84` |
| `Live` | `Short` | `4365.00` | 1,600,000,000.00 USD | 547,470.00 USD | 0.00 USD | `+95.25%` | `125.42` |
| `Live` | `Short` | `4375.00` | 1,600,000,000.00 USD | 22,390.00 USD | 0.00 USD | `+95.70%` | `5.12` |
| `Live` | `Short` | `4385.00` | 1,600,000,000.00 USD | 14,060.00 USD | 0.00 USD | `+96.14%` | `3.21` |
| `Live` | `Short` | `4395.00` | 1,600,000,000.00 USD | 14,520.00 USD | 0.00 USD | `+96.59%` | `3.30` |
| `Live` | `Short` | `4405.00` | 1,600,000,000.00 USD | 111,660.00 USD | 0.00 USD | `+97.04%` | `25.35` |
| `Live` | `Short` | `4415.00` | 1,600,000,000.00 USD | 50,550.00 USD | 0.00 USD | `+97.49%` | `11.45` |
| `Live` | `Short` | `4425.00` | 1,600,000,000.00 USD | 8,540.00 USD | 0.00 USD | `+97.93%` | `1.93` |
| `Live` | `Short` | `4435.00` | 1,600,000,000.00 USD | 19,310.00 USD | 0.00 USD | `+98.38%` | `4.35` |
| `Live` | `Short` | `4445.00` | 1,600,000,000.00 USD | 31,110.00 USD | 0.00 USD | `+98.83%` | `7.00` |
| `Live` | `Short` | `4455.00` | 1,600,000,000.00 USD | 108,470.00 USD | 0.00 USD | `+99.28%` | `24.35` |
| `Live` | `Short` | `4465.00` | 1,600,000,000.00 USD | 6,560.00 USD | 0.00 USD | `+99.72%` | `1.47` |
| `Live` | `Short` | `4475.00` | 1,600,000,000.00 USD | 41,200.00 USD | 0.00 USD | `+100.17%` | `9.21` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `485.00` | 75,670,000.00 USD | 0.00 USD | 278.83 USD | `-78.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `505.00` | 75,670,000.00 USD | 0.00 USD | 15,910.00 USD | `-77.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 75,650,000.00 USD | 0.00 USD | 563.16 USD | `-75.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.00` | 75,650,000.00 USD | 0.00 USD | 583.40 USD | `-71.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.00` | 75,650,000.00 USD | 0.00 USD | 16,690.00 USD | `-70.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.00` | 75,630,000.00 USD | 0.00 USD | 578.54 USD | `-69.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.00` | 75,630,000.00 USD | 0.00 USD | 242.21 USD | `-68.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 75,630,000.00 USD | 0.00 USD | 885.90 USD | `-68.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 75,630,000.00 USD | 0.00 USD | 177.27 USD | `-66.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 75,630,000.00 USD | 0.00 USD | 2,090.00 USD | `-63.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 75,630,000.00 USD | 0.00 USD | 1,670.00 USD | `-62.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 75,630,000.00 USD | 0.00 USD | 139,430.00 USD | `-61.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `875.00` | 75,490,000.00 USD | 0.00 USD | 918.49 USD | `-60.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 75,490,000.00 USD | 0.00 USD | 3,130.00 USD | `-60.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 75,480,000.00 USD | 0.00 USD | 2,780.00 USD | `-59.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 75,480,000.00 USD | 0.00 USD | 516.34 USD | `-55.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 75,480,000.00 USD | 0.00 USD | 100.50 USD | `-55.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 75,480,000.00 USD | 0.00 USD | 223,740.00 USD | `-55.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 75,260,000.00 USD | 0.00 USD | 445.08 USD | `-54.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 75,260,000.00 USD | 0.00 USD | 112.03 USD | `-54.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1045.00` | 75,250,000.00 USD | 0.00 USD | 1,260.00 USD | `-53.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 75,250,000.00 USD | 0.00 USD | 1,060.00 USD | `-52.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 75,250,000.00 USD | 0.00 USD | 995.34 USD | `-51.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 75,250,000.00 USD | 0.00 USD | 1,610.00 USD | `-50.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 75,250,000.00 USD | 0.00 USD | 11,050.00 USD | `-50.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 75,240,000.00 USD | 0.00 USD | 1,320.00 USD | `-49.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 75,240,000.00 USD | 0.00 USD | 1,000.00 USD | `-48.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 75,240,000.00 USD | 0.00 USD | 476.46 USD | `-47.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 75,240,000.00 USD | 0.00 USD | 972.41 USD | `-46.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1195.00` | 75,240,000.00 USD | 0.00 USD | 221.55 USD | `-46.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 75,240,000.00 USD | 0.00 USD | 3,110.00 USD | `-46.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 75,230,000.00 USD | 0.00 USD | 995.93 USD | `-45.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 75,230,000.00 USD | 0.00 USD | 951.93 USD | `-44.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 75,230,000.00 USD | 0.00 USD | 2,290.00 USD | `-43.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 75,230,000.00 USD | 0.00 USD | 9,050.00 USD | `-42.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 75,220,000.00 USD | 0.00 USD | 7,030.00 USD | `-42.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 75,210,000.00 USD | 0.00 USD | 25,040.00 USD | `-41.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 75,190,000.00 USD | 0.00 USD | 1,440.00 USD | `-41.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 75,190,000.00 USD | 0.00 USD | 141,950.00 USD | `-39.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 75,040,000.00 USD | 0.00 USD | 128.86 USD | `-39.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 75,040,000.00 USD | 0.00 USD | 1,270.00 USD | `-38.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 75,040,000.00 USD | 0.00 USD | 4,160.00 USD | `-38.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1385.00` | 75,040,000.00 USD | 0.00 USD | 100,800.00 USD | `-38.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 74,940,000.00 USD | 0.00 USD | 535,600.00 USD | `-37.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 74,400,000.00 USD | 0.00 USD | 18,840.00 USD | `-37.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 74,380,000.00 USD | 0.00 USD | 6,450.00 USD | `-36.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 74,380,000.00 USD | 0.00 USD | 852.10 USD | `-35.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 74,380,000.00 USD | 0.00 USD | 1,610.00 USD | `-35.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 74,370,000.00 USD | 0.00 USD | 5,090.00 USD | `-34.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 74,370,000.00 USD | 0.00 USD | 19,730.00 USD | `-34.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 74,350,000.00 USD | 0.00 USD | 2,600.00 USD | `-34.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 74,350,000.00 USD | 0.00 USD | 18,710.00 USD | `-33.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 74,330,000.00 USD | 0.00 USD | 11,460.00 USD | `-33.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 74,320,000.00 USD | 0.00 USD | 84,170.00 USD | `-32.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 74,230,000.00 USD | 0.00 USD | 11,140.00 USD | `-32.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 74,220,000.00 USD | 0.00 USD | 31,900.00 USD | `-31.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 74,190,000.00 USD | 0.00 USD | 8,830.00 USD | `-31.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 74,180,000.00 USD | 0.00 USD | 960.99 USD | `-30.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 74,180,000.00 USD | 0.00 USD | 58,080.00 USD | `-30.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 74,120,000.00 USD | 0.00 USD | 6,260.00 USD | `-30.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 74,110,000.00 USD | 0.00 USD | 198,620.00 USD | `-29.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 73,920,000.00 USD | 0.00 USD | 9,350.00 USD | `-29.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 73,910,000.00 USD | 0.00 USD | 4,040.00 USD | `-28.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 73,900,000.00 USD | 0.00 USD | 431,660.00 USD | `-28.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 73,470,000.00 USD | 0.00 USD | 28,870.00 USD | `-27.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 73,440,000.00 USD | 0.00 USD | 13,590.00 USD | `-27.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 73,430,000.00 USD | 0.00 USD | 10,560.00 USD | `-26.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 73,420,000.00 USD | 0.00 USD | 326,230.00 USD | `-26.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 73,090,000.00 USD | 0.00 USD | 35,070.00 USD | `-25.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 73,060,000.00 USD | 0.00 USD | 744.09 USD | `-25.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 73,060,000.00 USD | 0.00 USD | 289.27 USD | `-25.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 73,060,000.00 USD | 0.00 USD | 35,440.00 USD | `-24.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 73,020,000.00 USD | 0.00 USD | 42,680.00 USD | `-24.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 72,980,000.00 USD | 0.00 USD | 84,490.00 USD | `-23.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 72,890,000.00 USD | 0.00 USD | 16,350.00 USD | `-23.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 72,880,000.00 USD | 0.00 USD | 47,500.00 USD | `-22.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 72,830,000.00 USD | 0.00 USD | 28,150.00 USD | `-22.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 72,800,000.00 USD | 0.00 USD | 3,180.00 USD | `-21.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 72,800,000.00 USD | 0.00 USD | 466,120.00 USD | `-21.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 72,330,000.00 USD | 0.00 USD | 76,990.00 USD | `-21.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 72,250,000.00 USD | 0.00 USD | 3,090.00 USD | `-20.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 72,250,000.00 USD | 0.00 USD | 8,500.00 USD | `-20.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 72,240,000.00 USD | 0.00 USD | 186,120.00 USD | `-19.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 72,060,000.00 USD | 0.00 USD | 660,000.00 USD | `-19.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 71,400,000.00 USD | 0.00 USD | 264,580.00 USD | `-18.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 71,130,000.00 USD | 0.00 USD | 27,250.00 USD | `-18.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 71,110,000.00 USD | 0.00 USD | 19,130.00 USD | `-17.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 71,090,000.00 USD | 0.00 USD | 31,580.00 USD | `-17.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 71,050,000.00 USD | 0.00 USD | 792,160.00 USD | `-17.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 70,260,000.00 USD | 0.00 USD | 33,750.00 USD | `-16.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 70,230,000.00 USD | 0.00 USD | 18,240,000.00 USD | `-16.13%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 51,990,000.00 USD | 0.00 USD | 22,350.00 USD | `-15.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 51,960,000.00 USD | 0.00 USD | 59,690.00 USD | `-15.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 51,900,000.00 USD | 0.00 USD | 160,070.00 USD | `-14.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 51,740,000.00 USD | 0.00 USD | 101,030.00 USD | `-14.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1925.00` | 51,640,000.00 USD | 0.00 USD | 19,300,000.00 USD | `-13.89%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 32,350,000.00 USD | 0.00 USD | 107,510.00 USD | `-13.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 32,240,000.00 USD | 0.00 USD | 63,470.00 USD | `-13.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 32,170,000.00 USD | 0.00 USD | 73,490.00 USD | `-12.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 32,100,000.00 USD | 0.00 USD | 139,850.00 USD | `-12.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 31,960,000.00 USD | 0.00 USD | 334,410.00 USD | `-11.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 31,630,000.00 USD | 0.00 USD | 100,060.00 USD | `-11.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 31,530,000.00 USD | 0.00 USD | 249,090.00 USD | `-10.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 31,280,000.00 USD | 0.00 USD | 1,920,000.00 USD | `-10.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 29,360,000.00 USD | 0.00 USD | 483,180.00 USD | `-9.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 28,880,000.00 USD | 0.00 USD | 95,400.00 USD | `-9.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 28,780,000.00 USD | 0.00 USD | 328,550.00 USD | `-8.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 28,450,000.00 USD | 0.00 USD | 702,690.00 USD | `-8.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 27,750,000.00 USD | 0.00 USD | 297,190.00 USD | `-8.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 27,450,000.00 USD | 0.00 USD | 128,420.00 USD | `-7.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 27,320,000.00 USD | 0.00 USD | 36,400.00 USD | `-7.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 27,290,000.00 USD | 0.00 USD | 223,180.00 USD | `-6.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 27,070,000.00 USD | 0.00 USD | 28,900.00 USD | `-6.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 27,040,000.00 USD | 0.00 USD | 819,220.00 USD | `-5.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 26,220,000.00 USD | 0.00 USD | 876,600.00 USD | `-5.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 25,340,000.00 USD | 0.00 USD | 296,050.00 USD | `-4.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 25,040,000.00 USD | 0.00 USD | 643,510.00 USD | `-4.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 24,400,000.00 USD | 0.00 USD | 377,670.00 USD | `-4.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 24,020,000.00 USD | 0.00 USD | 5,280,000.00 USD | `-3.61%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2165.00` | 18,740,000.00 USD | 0.00 USD | 1,680,000.00 USD | `-3.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 17,060,000.00 USD | 0.00 USD | 6,980,000.00 USD | `-2.71%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2185.00` | 10,090,000.00 USD | 0.00 USD | 1,530,000.00 USD | `-2.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 8,560,000.00 USD | 0.00 USD | 641,070.00 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 7,920,000.00 USD | 0.00 USD | 189,810.00 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 7,730,000.00 USD | 0.00 USD | 13,280.00 USD | `-0.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 7,710,000.00 USD | 0.00 USD | 1,810,000.00 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2235.00` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | `-0.03%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2245.00` | 449,460.00 USD | 449,460.00 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2255.00` | 1,640,000.00 USD | 1,190,000.00 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2265.00` | 3,190,000.00 USD | 1,550,000.00 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 3,820,000.00 USD | 630,980.00 USD | 0.00 USD | `+1.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 4,730,000.00 USD | 908,340.00 USD | 0.00 USD | `+2.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 5,010,000.00 USD | 285,280.00 USD | 0.00 USD | `+2.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 5,530,000.00 USD | 513,080.00 USD | 0.00 USD | `+3.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2315.00` | 6,780,000.00 USD | 1,260,000.00 USD | 0.00 USD | `+3.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 7,410,000.00 USD | 623,820.00 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 7,650,000.00 USD | 246,920.00 USD | 0.00 USD | `+4.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 8,630,000.00 USD | 971,960.00 USD | 0.00 USD | `+4.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 10,070,000.00 USD | 1,450,000.00 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 10,340,000.00 USD | 264,160.00 USD | 0.00 USD | `+5.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 10,480,000.00 USD | 143,260.00 USD | 0.00 USD | `+6.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 10,530,000.00 USD | 47,410.00 USD | 0.00 USD | `+6.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 11,680,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+7.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 13,160,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+7.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 13,400,000.00 USD | 238,600.00 USD | 0.00 USD | `+8.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 16,380,000.00 USD | 2,980,000.00 USD | 0.00 USD | `+8.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 16,570,000.00 USD | 189,180.00 USD | 0.00 USD | `+8.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 17,140,000.00 USD | 566,880.00 USD | 0.00 USD | `+9.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2455.00` | 17,290,000.00 USD | 147,980.00 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 19,380,000.00 USD | 2,100,000.00 USD | 0.00 USD | `+10.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 19,570,000.00 USD | 187,980.00 USD | 0.00 USD | `+10.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 21,680,000.00 USD | 2,110,000.00 USD | 0.00 USD | `+11.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 22,090,000.00 USD | 411,740.00 USD | 0.00 USD | `+11.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 26,960,000.00 USD | 4,870,000.00 USD | 0.00 USD | `+12.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2515.00` | 34,650,000.00 USD | 7,680,000.00 USD | 0.00 USD | `+12.50%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 37,690,000.00 USD | 3,050,000.00 USD | 0.00 USD | `+12.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 37,760,000.00 USD | 63,610.00 USD | 0.00 USD | `+13.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 40,030,000.00 USD | 2,270,000.00 USD | 0.00 USD | `+13.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 40,250,000.00 USD | 222,610.00 USD | 0.00 USD | `+14.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 42,590,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+14.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 42,670,000.00 USD | 78,680.00 USD | 0.00 USD | `+15.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 45,370,000.00 USD | 2,700,000.00 USD | 0.00 USD | `+15.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 45,380,000.00 USD | 11,010.00 USD | 0.00 USD | `+16.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 48,170,000.00 USD | 2,790,000.00 USD | 0.00 USD | `+16.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 48,320,000.00 USD | 145,730.00 USD | 0.00 USD | `+16.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 50,500,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+17.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 50,650,000.00 USD | 147,930.00 USD | 0.00 USD | `+17.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 52,770,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+18.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 53,020,000.00 USD | 251,610.00 USD | 0.00 USD | `+18.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 55,170,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+19.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 55,380,000.00 USD | 208,460.00 USD | 0.00 USD | `+19.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 57,550,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+20.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 57,630,000.00 USD | 76,240.00 USD | 0.00 USD | `+20.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 62,610,000.00 USD | 4,980,000.00 USD | 0.00 USD | `+21.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 62,690,000.00 USD | 76,900.00 USD | 0.00 USD | `+21.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 65,150,000.00 USD | 2,470,000.00 USD | 0.00 USD | `+21.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 65,200,000.00 USD | 43,050.00 USD | 0.00 USD | `+22.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 67,570,000.00 USD | 2,370,000.00 USD | 0.00 USD | `+22.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 68,250,000.00 USD | 684,550.00 USD | 0.00 USD | `+23.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 70,590,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+23.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 71,170,000.00 USD | 577,610.00 USD | 0.00 USD | `+24.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 73,430,000.00 USD | 2,260,000.00 USD | 0.00 USD | `+24.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 73,450,000.00 USD | 17,550.00 USD | 0.00 USD | `+25.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 76,580,000.00 USD | 3,130,000.00 USD | 0.00 USD | `+25.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 76,630,000.00 USD | 52,490.00 USD | 0.00 USD | `+25.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 76,680,000.00 USD | 43,930.00 USD | 0.00 USD | `+26.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 76,960,000.00 USD | 286,140.00 USD | 0.00 USD | `+26.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 77,970,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+27.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 79,240,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+27.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 79,250,000.00 USD | 14,570.00 USD | 0.00 USD | `+28.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 79,250,000.00 USD | 2,460.00 USD | 0.00 USD | `+28.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 79,560,000.00 USD | 305,820.00 USD | 0.00 USD | `+29.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 79,580,000.00 USD | 16,190.00 USD | 0.00 USD | `+29.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 81,060,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+29.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 81,070,000.00 USD | 10,340.00 USD | 0.00 USD | `+30.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 81,070,000.00 USD | 3,050.00 USD | 0.00 USD | `+30.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 81,130,000.00 USD | 52,370.00 USD | 0.00 USD | `+31.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 81,160,000.00 USD | 34,650.00 USD | 0.00 USD | `+31.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 81,200,000.00 USD | 43,400.00 USD | 0.00 USD | `+32.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 81,320,000.00 USD | 113,340.00 USD | 0.00 USD | `+32.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 81,460,000.00 USD | 145,510.00 USD | 0.00 USD | `+33.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 81,640,000.00 USD | 177,120.00 USD | 0.00 USD | `+33.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 83,570,000.00 USD | 1,920,000.00 USD | 0.00 USD | `+33.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 86,600,000.00 USD | 3,040,000.00 USD | 0.00 USD | `+34.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 86,610,000.00 USD | 6,950.00 USD | 0.00 USD | `+34.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 86,650,000.00 USD | 35,380.00 USD | 0.00 USD | `+35.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 86,720,000.00 USD | 74,910.00 USD | 0.00 USD | `+35.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 86,740,000.00 USD | 22,460.00 USD | 0.00 USD | `+36.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 87,510,000.00 USD | 771,720.00 USD | 0.00 USD | `+36.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 87,520,000.00 USD | 612.69 USD | 0.00 USD | `+37.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 87,560,000.00 USD | 49,500.00 USD | 0.00 USD | `+37.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 87,580,000.00 USD | 19,570.00 USD | 0.00 USD | `+37.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 87,590,000.00 USD | 928.50 USD | 0.00 USD | `+38.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 99,430,000.00 USD | 11,850,000.00 USD | 0.00 USD | `+38.89%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 99,560,000.00 USD | 128,280.00 USD | 0.00 USD | `+39.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 99,940,000.00 USD | 381,020.00 USD | 0.00 USD | `+39.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 99,950,000.00 USD | 2,660.00 USD | 0.00 USD | `+40.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 100,000,000.00 USD | 58,930.00 USD | 0.00 USD | `+41.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 100,010,000.00 USD | 9,860.00 USD | 0.00 USD | `+41.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 100,010,000.00 USD | 149.22 USD | 0.00 USD | `+42.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 100,020,000.00 USD | 1,330.00 USD | 0.00 USD | `+42.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 100,050,000.00 USD | 36,550.00 USD | 0.00 USD | `+42.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 100,710,000.00 USD | 653,320.00 USD | 0.00 USD | `+43.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 100,710,000.00 USD | 1,760.00 USD | 0.00 USD | `+43.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 100,710,000.00 USD | 3,740.00 USD | 0.00 USD | `+44.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 100,710,000.00 USD | 167.25 USD | 0.00 USD | `+44.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 100,770,000.00 USD | 56,110.00 USD | 0.00 USD | `+45.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 101,000,000.00 USD | 236,580.00 USD | 0.00 USD | `+45.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 101,020,000.00 USD | 15,710.00 USD | 0.00 USD | `+46.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 101,020,000.00 USD | 1,630.00 USD | 0.00 USD | `+46.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 101,160,000.00 USD | 141,980.00 USD | 0.00 USD | `+46.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 101,180,000.00 USD | 15,350.00 USD | 0.00 USD | `+47.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 102,590,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+47.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 102,980,000.00 USD | 389,970.00 USD | 0.00 USD | `+48.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 103,000,000.00 USD | 18,270.00 USD | 0.00 USD | `+48.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 103,000,000.00 USD | 4,350.00 USD | 0.00 USD | `+49.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 103,010,000.00 USD | 2,170.00 USD | 0.00 USD | `+49.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 103,010,000.00 USD | 837.74 USD | 0.00 USD | `+50.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 103,010,000.00 USD | 2,780.00 USD | 0.00 USD | `+50.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 103,030,000.00 USD | 21,260.00 USD | 0.00 USD | `+50.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 103,090,000.00 USD | 58,010.00 USD | 0.00 USD | `+51.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 103,410,000.00 USD | 322,160.00 USD | 0.00 USD | `+51.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 104,900,000.00 USD | 1,490,000.00 USD | 0.00 USD | `+52.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 104,910,000.00 USD | 5,700.00 USD | 0.00 USD | `+52.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 104,930,000.00 USD | 16,310.00 USD | 0.00 USD | `+53.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 104,940,000.00 USD | 15,030.00 USD | 0.00 USD | `+54.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 104,960,000.00 USD | 18,600.00 USD | 0.00 USD | `+54.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 104,960,000.00 USD | 495.50 USD | 0.00 USD | `+54.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 104,960,000.00 USD | 3,190.00 USD | 0.00 USD | `+55.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 105,010,000.00 USD | 43,610.00 USD | 0.00 USD | `+55.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 105,010,000.00 USD | 158.32 USD | 0.00 USD | `+56.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 105,450,000.00 USD | 444,280.00 USD | 0.00 USD | `+56.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 105,500,000.00 USD | 43,620.00 USD | 0.00 USD | `+57.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 105,500,000.00 USD | 3,690.00 USD | 0.00 USD | `+57.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 105,510,000.00 USD | 9,810.00 USD | 0.00 USD | `+58.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 105,600,000.00 USD | 90,810.00 USD | 0.00 USD | `+59.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 105,600,000.00 USD | 2,300.00 USD | 0.00 USD | `+59.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3575.00` | 105,600,000.00 USD | 2,870.00 USD | 0.00 USD | `+59.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 105,600,000.00 USD | 354.92 USD | 0.00 USD | `+60.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 105,620,000.00 USD | 13,160.00 USD | 0.00 USD | `+60.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 105,720,000.00 USD | 101,080.00 USD | 0.00 USD | `+61.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 105,730,000.00 USD | 10,210.00 USD | 0.00 USD | `+62.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 105,740,000.00 USD | 7,790.00 USD | 0.00 USD | `+62.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 105,740,000.00 USD | 3,860.00 USD | 0.00 USD | `+63.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 105,740,000.00 USD | 820.18 USD | 0.00 USD | `+63.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 105,750,000.00 USD | 8,130.00 USD | 0.00 USD | `+63.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 105,810,000.00 USD | 55,120.00 USD | 0.00 USD | `+64.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 105,810,000.00 USD | 1,410.00 USD | 0.00 USD | `+64.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 105,810,000.00 USD | 819.92 USD | 0.00 USD | `+65.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 105,810,000.00 USD | 323.58 USD | 0.00 USD | `+66.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 105,810,000.00 USD | 1,400.00 USD | 0.00 USD | `+66.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 105,820,000.00 USD | 6,490.00 USD | 0.00 USD | `+67.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3745.00` | 105,820,000.00 USD | 165.90 USD | 0.00 USD | `+67.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 105,820,000.00 USD | 751.00 USD | 0.00 USD | `+67.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 105,820,000.00 USD | 286.90 USD | 0.00 USD | `+69.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 105,820,000.00 USD | 1,560.00 USD | 0.00 USD | `+69.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 106,550,000.00 USD | 734,090.00 USD | 0.00 USD | `+70.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 106,570,000.00 USD | 20,930.00 USD | 0.00 USD | `+70.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 106,580,000.00 USD | 8,380.00 USD | 0.00 USD | `+71.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 106,580,000.00 USD | 711.78 USD | 0.00 USD | `+71.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 106,580,000.00 USD | 355.28 USD | 0.00 USD | `+71.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 106,590,000.00 USD | 5,170.00 USD | 0.00 USD | `+72.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 106,610,000.00 USD | 19,430.00 USD | 0.00 USD | `+73.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 106,620,000.00 USD | 12,120.00 USD | 0.00 USD | `+74.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 107,270,000.00 USD | 646,840.00 USD | 0.00 USD | `+75.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 107,310,000.00 USD | 42,570.00 USD | 0.00 USD | `+76.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 107,370,000.00 USD | 59,170.00 USD | 0.00 USD | `+76.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 107,370,000.00 USD | 1,380.00 USD | 0.00 USD | `+76.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 107,380,000.00 USD | 6,960.00 USD | 0.00 USD | `+77.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 107,390,000.00 USD | 14,610.00 USD | 0.00 USD | `+78.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 107,400,000.00 USD | 4,280.00 USD | 0.00 USD | `+78.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 110,150,000.00 USD | 2,750,000.00 USD | 0.00 USD | `+79.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 110,150,000.00 USD | 898.59 USD | 0.00 USD | `+80.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 110,150,000.00 USD | 811.00 USD | 0.00 USD | `+81.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 110,150,000.00 USD | 4,310.00 USD | 0.00 USD | `+82.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 110,150,000.00 USD | 3,050.00 USD | 0.00 USD | `+82.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 110,190,000.00 USD | 36,740.00 USD | 0.00 USD | `+83.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 110,200,000.00 USD | 5,990.00 USD | 0.00 USD | `+84.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 110,200,000.00 USD | 372.90 USD | 0.00 USD | `+84.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 110,200,000.00 USD | 395.43 USD | 0.00 USD | `+85.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 110,200,000.00 USD | 376.65 USD | 0.00 USD | `+87.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 110,240,000.00 USD | 42,260.00 USD | 0.00 USD | `+88.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 110,240,000.00 USD | 460.70 USD | 0.00 USD | `+88.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 110,240,000.00 USD | 1,270.00 USD | 0.00 USD | `+88.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 110,250,000.00 USD | 4,300.00 USD | 0.00 USD | `+90.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 110,250,000.00 USD | 437.16 USD | 0.00 USD | `+90.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 110,310,000.00 USD | 64,550.00 USD | 0.00 USD | `+91.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 110,310,000.00 USD | 1,610.00 USD | 0.00 USD | `+91.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 110,410,000.00 USD | 97,670.00 USD | 0.00 USD | `+92.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 110,410,000.00 USD | 1,070.00 USD | 0.00 USD | `+93.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 110,420,000.00 USD | 11,270.00 USD | 0.00 USD | `+94.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 110,430,000.00 USD | 2,400.00 USD | 0.00 USD | `+94.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 110,470,000.00 USD | 43,750.00 USD | 0.00 USD | `+95.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 110,530,000.00 USD | 64,570.00 USD | 0.00 USD | `+96.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 110,540,000.00 USD | 1,050.00 USD | 0.00 USD | `+96.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 110,580,000.00 USD | 46,920.00 USD | 0.00 USD | `+97.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 110,590,000.00 USD | 11,480.00 USD | 0.00 USD | `+97.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 110,600,000.00 USD | 2,510.00 USD | 0.00 USD | `+97.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 110,770,000.00 USD | 177,400.00 USD | 0.00 USD | `+98.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 110,770,000.00 USD | 959.61 USD | 0.00 USD | `+99.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4465.00` | 110,780,000.00 USD | 1,030.00 USD | 0.00 USD | `+99.72%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `28.93B` | Total OI Tokens: `12,983,589.7 ETH`
  * 1h OI Change: `+0.38%` | 4h OI Change: `-1.22%` | 24h OI Change: `-3.02%`
  * Exchange Breakdown: Binance=`8.41B` | Bybit=`2.08B` | OKX=`1.79B` | Hyperliquid=`2.34B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-408.07K` | Last 24h: `1.05M` | Last 3d: `6.29M` | Last 7d: `12.86M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0007%` | **USDT OKX** | `-0.0087%` |
| **USDT Bybit** | `-0.0184%` | **USDT KuCoin** | `-0.0122%` |
| **USDT MEXC** | `-0.0005%` | **USDT BingX** | `-0.0004%` |
| **USDT Gate** | `-0.0135%` | **USDT Bitget** | `-0.0005%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0045%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `51.09%` | `48.91%` | `1.04` | 985,690,000.00 USD |
| `15M` | `Binance` | `53.24%` | `46.76%` | `1.14` | 326,730,000.00 USD |
| `15M` | `OKX` | `49.58%` | `50.42%` | `0.98` | 137,210,000.00 USD |
| `15M` | `Bybit` | `55.17%` | `44.83%` | `1.23` | 103,140,000.00 USD |
| `15M` | `KuCoin` | `69.4%` | `30.6%` | `2.27` | 3,160,000.00 USD |
| `15M` | `Gate` | `47.92%` | `52.08%` | `0.92` | 103,630,000.00 USD |
| `15M` | `Bitget` | `46.9%` | `53.1%` | `0.88` | 57,670,000.00 USD |
| `15M` | `BingX` | `46.41%` | `53.59%` | `0.87` | 13,770,000.00 USD |
| `15M` | `MEXC` | `45.71%` | `54.29%` | `0.84` | 37,910,000.00 USD |
| `15M` | `Bitunix` | `45.72%` | `54.28%` | `0.84` | 50,460,000.00 USD |
| `15M` | `Hyperliquid` | `38.88%` | `61.12%` | `0.64` | 69,480,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `78.21%` | `21.79%` | `3.59` | 23,010,000.00 USD |
| `15M` | `Crypto.com` | `50.27%` | `49.73%` | `1.01` | 3,480,000.00 USD |
| `15M` | `WhiteBIT` | `99.73%` | `0.27%` | `369.37` | 5,150,000.00 USD |
| `15M` | `HTX` | `48.99%` | `51.01%` | `0.96` | 3,800,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `51.26%` | `48.74%` | `1.05` | 24,910,000.00 USD |
| `15M` | `Bitfinex` | `68.94%` | `31.06%` | `2.22` | 324,990.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `60.21%` | `39.79%` | `1.51` | 11,080,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `52.2%` | `47.8%` | `1.09` | 10,790,000.00 USD |
| `15M` | `Whale Positions` | `53.24%` | `46.76%` | `1.14` | 326,730,000.00 USD |
| `15M` | `Global Accounts` | `51.09%` | `48.91%` | `1.04` | 985,690,000.00 USD |
| `1H` | `ETH` | `55.87%` | `44.13%` | `1.27` | 3,610,000,000.00 USD |
| `1H` | `Binance` | `57.41%` | `42.59%` | `1.35` | 1,200,000,000.00 USD |
| `1H` | `OKX` | `54.32%` | `45.68%` | `1.19` | 492,070,000.00 USD |
| `1H` | `Bybit` | `61.67%` | `38.33%` | `1.61` | 383,600,000.00 USD |
| `1H` | `KuCoin` | `76.77%` | `23.23%` | `3.30` | 17,150,000.00 USD |
| `1H` | `Gate` | `46.81%` | `53.19%` | `0.88` | 416,750,000.00 USD |
| `1H` | `Bitget` | `52.03%` | `47.97%` | `1.08` | 199,070,000.00 USD |
| `1H` | `BingX` | `50.29%` | `49.71%` | `1.01` | 49,040,000.00 USD |
| `1H` | `MEXC` | `48.22%` | `51.78%` | `0.93` | 120,850,000.00 USD |
| `1H` | `Bitunix` | `53.24%` | `46.76%` | `1.14` | 142,700,000.00 USD |
| `1H` | `Hyperliquid` | `56.16%` | `43.84%` | `1.28` | 261,360,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `75.14%` | `24.86%` | `3.02` | 43,350,000.00 USD |
| `1H` | `Crypto.com` | `51.58%` | `48.42%` | `1.07` | 12,120,000.00 USD |
| `1H` | `WhiteBIT` | `93.66%` | `6.34%` | `14.77` | 45,650,000.00 USD |
| `1H` | `HTX` | `51.79%` | `48.21%` | `1.07` | 12,380,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `57.92%` | `42.08%` | `1.38` | 137,590,000.00 USD |
| `1H` | `Bitfinex` | `61.17%` | `38.83%` | `1.58` | 2,740,000.00 USD |
| `1H` | `Kraken` | `58.25%` | `41.75%` | `1.40` | 55,440.00 USD |
| `1H` | `Aster` | `50.66%` | `49.34%` | `1.03` | 36,100,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50%` | `50%` | `1.00` | 34,520,000.00 USD |
| `1H` | `Whale Positions` | `57.41%` | `42.59%` | `1.35` | 1,200,000,000.00 USD |
| `1H` | `Global Accounts` | `55.87%` | `44.13%` | `1.27` | 3,610,000,000.00 USD |
| `4H` | `ETH` | `48.10%` | `51.90%` | `0.93` | 26,530,000,000.00 USD |
| `4H` | `Binance` | `49.12%` | `50.88%` | `0.97` | 7,880,000,000.00 USD |
| `4H` | `OKX` | `49.58%` | `50.42%` | `0.98` | 3,530,000,000.00 USD |
| `4H` | `Bybit` | `50.22%` | `49.78%` | `1.01` | 2,670,000,000.00 USD |
| `4H` | `KuCoin` | `50.71%` | `49.29%` | `1.03` | 99,070,000.00 USD |
| `4H` | `Gate` | `48.32%` | `51.68%` | `0.93` | 2,440,000,000.00 USD |
| `4H` | `Bitget` | `46.76%` | `53.24%` | `0.88` | 1,270,000,000.00 USD |
| `4H` | `BingX` | `48.95%` | `51.05%` | `0.96` | 352,620,000.00 USD |
| `4H` | `MEXC` | `46.29%` | `53.71%` | `0.86` | 1,010,000,000.00 USD |
| `4H` | `Bitunix` | `50.6%` | `49.4%` | `1.02` | 1,130,000,000.00 USD |
| `4H` | `Hyperliquid` | `51.68%` | `48.32%` | `1.07` | 1,710,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `60.37%` | `39.63%` | `1.52` | 119,800,000.00 USD |
| `4H` | `Crypto.com` | `50.11%` | `49.89%` | `1.00` | 82,450,000.00 USD |
| `4H` | `WhiteBIT` | `37.51%` | `62.49%` | `0.60` | 2,770,000,000.00 USD |
| `4H` | `HTX` | `48.49%` | `51.51%` | `0.94` | 97,020,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `50.2%` | `49.8%` | `1.01` | 798,290,000.00 USD |
| `4H` | `Bitfinex` | `45.87%` | `54.13%` | `0.85` | 27,510,000.00 USD |
| `4H` | `Kraken` | `50.01%` | `49.99%` | `1.00` | 86,250,000.00 USD |
| `4H` | `Aster` | `49.62%` | `50.38%` | `0.98` | 233,970,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.23%` | `51.77%` | `0.93` | 232,490,000.00 USD |
| `4H` | `Whale Positions` | `49.12%` | `50.88%` | `0.97` | 7,880,000,000.00 USD |
| `4H` | `Global Accounts` | `48.10%` | `51.90%` | `0.93` | 26,530,000,000.00 USD |


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
| `0:00 UTC` | `2236.75` | `2236.37` | `2236.75` | `2236.75` | `2235.75` | 994,649.95 USD | 295,815.67 USD | 698,834.27 USD | -403,018.60 USD | `-40.52%` | `0B / 1S` |

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
| `5m` | -3,730,000.00 USD | 3,400,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -2,570,000.00 USD | 24,450,000.00 USD | **`ACCUMULATION`** |
| `30m` | 8,880,000.00 USD | 51,510,000.00 USD | **`ACCUMULATION`** |
| `1h` | 12,170,000.00 USD | 105,920,000.00 USD | **`ACCUMULATION`** |
| `2h` | 15,490,000.00 USD | 178,250,000.00 USD | **`ACCUMULATION`** |
| `4h` | -46,110,000.00 USD | -528,100,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -64,440,000.00 USD | -595,470,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -144,270,000.00 USD | -1,700,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -160,510,000.00 USD | -2,160,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -122,080,000.00 USD | -1,930,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -170,970,000.00 USD | -3,010,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,160,000,000.00 USD | -9,690,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-3.73M` | 15m=`-2.57M` | 1h=`+12.17M` | 24h=`-122.08M`
* Futures Capital Netflows: 5m=`+3.40M` | 15m=`+24.45M` | 1h=`+105.92M` | 24h=`-1.93B`
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
  * `2026-10-30 09:09:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:28:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:29:56 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2206.14` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2179.02` (Risk Distance: `27.12` pts)
  * +2.5R Take Profit: `2273.95`
  * Mathematical Lot Sizing: **`0.36 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2280.60` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2307.72` (Risk Distance: `27.12` pts)
  * +2.5R Take Profit: `2212.79`
  * Mathematical Lot Sizing: **`0.36 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2242.80`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
