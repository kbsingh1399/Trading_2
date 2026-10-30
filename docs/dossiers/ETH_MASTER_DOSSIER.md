# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 14:59:56 IST` (`2026-10-30 09:29:56 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2219.00` | **Live Ask Quote**: `2222.40` | **Mid Price**: `2220.70`
- **Spread Points**: `340.00` | **Spread BPS**: `15.31 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2219.79` | VWAP Z-Score: `-0.05` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `12.29` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `40.08` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2269.80` | Lower -3.00σ Band: `2169.78`
  * Upper +2.51σ Band: `2261.64` | Lower -2.51σ Band: `2177.95`
  * Upper +2.01σ Band: `2253.30` | Lower -2.01σ Band: `2186.29`
  * Upper +2.00σ Band: `2253.13` | Lower -2.00σ Band: `2186.45`
  * Upper +1.28σ Band: `2241.13` | Lower -1.28σ Band: `2198.46`
  * Upper +1.00σ Band: `2236.46` | Lower -1.00σ Band: `2203.12`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2226.56` | EMA-20=`2230.33` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2244.23` (Slope: `+0.0000`) | EMA-100=`2268.02`
  * Institutional Anchors: EMA-144=`2281.60` | EMA-200=`2293.72` (Slope: `-0.3420`) | EMA-233=`2298.78`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2252.28` (Distance: `-1.41%`)
  * Point of Control (POC) = `2241.75` (Distance: `-0.94%`)
  * Value Area Low (VAL) = `2193.19` (Distance: `+1.25%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2354.78` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2251.30` | Low=`2215.90`
  * New York Session (13:00-21:00 UTC): High=`2234.02` | Low=`2207.38`
  * Initial Balance (First Hour): IB High=`2246.50` | IB Low=`2230.60`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2211.82` - `2229.58`
  * Optimal Trade Entry (OTE 0.705): `2225.14`
  * Structural Invalidation Anchor (0.786): `2238.47`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2222.81` | `2225.55` | `2222.05` | `2223.00` | `7,728` | 17,183,673.68 USD | 1,164,108.69 USD | `+6.77%` | -975,346,980.28 USD | `+0.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `2223.00` | `2226.00` | `2221.29` | `2223.83` | `12,077` | 26,852,890.50 USD | -2,382,073.02 USD | `-8.87%` | -977,729,053.29 USD | `-0.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `2223.83` | `2224.93` | `2223.30` | `2223.37` | `2,938` | 6,535,056.87 USD | -1,427,959.80 USD | `-21.85%` | -979,157,013.09 USD | `-0.12` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2224.68` | `2231.68` | `2223.30` | `2227.93` | `26,909` | 59,922,094.97 USD | -1,422,125.96 USD | `-2.37%` | -965,967,037.27 USD | `-0.05` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2227.92` | `2229.91` | `2221.24` | `2223.00` | `29,601` | 65,855,959.19 USD | -5,333,544.98 USD | `-8.10%` | -971,300,582.25 USD | `-0.30` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `2223.00` | `2226.00` | `2221.29` | `2223.30` | `14,988` | 33,326,459.49 USD | -3,870,480.16 USD | `-11.61%` | -975,171,062.41 USD | `-0.17` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2252.91` | `2253.96` | `2228.21` | `2235.54` | `253,701` | 568,308,333.87 USD | -3,920,812.04 USD | `-0.69%` | -926,664,438.18 USD | `+0.36` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `2235.54` | `2236.80` | `2223.18` | `2227.93` | `164,265` | 366,023,334.59 USD | -37,825,356.97 USD | `-10.33%` | -964,489,795.15 USD | `+0.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2227.92` | `2229.91` | `2221.24` | `2223.37` | `44,617` | 99,243,906.56 USD | -9,143,577.79 USD | `-9.21%` | -973,633,372.94 USD | `+0.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2236.80` | `2221.24` | `2223.37` | `208,881` | 465,266,825.38 USD | -46,968,621.26 USD | `-10.09%` | -934,834,689.71 USD | `+0.50` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -98,115,944.70 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -652,353,514.01 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2236.80` | `2221.24` | `2223.37` | `208,881` | 465,266,825.38 USD | -46,968,621.26 USD | `-10.09%` | -934,834,689.71 USD | `+0.50` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2220.70`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2221.10` | `566.2893` | 1,257,785.16 USD | 11,183,335.50 USD | `4 orders` | `-0.09%` | `-` |
| `BID` | `2221.20` | `488.0250` | 1,084,001.13 USD | 9,925,550.34 USD | `14 orders` | `-0.08%` | `-` |
| `BID` | `2221.30` | `170.7893` | 379,374.27 USD | 8,841,549.21 USD | `5 orders` | `-0.08%` | `-` |
| `BID` | `2221.40` | `391.8997` | 870,565.99 USD | 8,462,174.94 USD | `11 orders` | `-0.07%` | `-` |
| `BID` | `2221.50` | `119.5606` | 265,603.87 USD | 7,591,608.94 USD | `7 orders` | `-0.07%` | `-` |
| `BID` | `2221.60` | `373.8296` | 830,499.84 USD | 7,326,005.07 USD | `10 orders` | `-0.07%` | `-` |
| `BID` | `2221.70` | `121.1783` | 269,221.83 USD | 6,495,505.23 USD | `9 orders` | `-0.06%` | `-` |
| `BID` | `2221.80` | `200.3356` | 445,105.64 USD | 6,226,283.40 USD | `5 orders` | `-0.06%` | `-` |
| `BID` | `2221.90` | `246.6297` | 547,986.53 USD | 5,781,177.76 USD | `12 orders` | `-0.05%` | `-` |
| `BID` | `2222.00` | `269.0498` | 597,828.66 USD | 5,233,191.23 USD | `9 orders` | `-0.05%` | `-` |
| `BID` | `2222.10` | `418.9155` | 930,872.13 USD | 4,635,362.58 USD | `13 orders` | `-0.04%` | `-` |
| `BID` | `2222.20` | `246.2015` | 547,108.97 USD | 3,704,490.45 USD | `9 orders` | `-0.04%` | `-` |
| `BID` | `2222.30` | `404.1521` | 898,147.21 USD | 3,157,381.47 USD | `10 orders` | `-0.03%` | `-` |
| `BID` | `2222.40` | `179.1605` | 398,166.30 USD | 2,259,234.26 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `2222.50` | `78.9741` | 175,519.94 USD | 1,861,067.97 USD | `9 orders` | `-0.02%` | `-` |
| `BID` | `2222.60` | `181.3906` | 403,158.75 USD | 1,685,548.03 USD | `9 orders` | `-0.02%` | `-` |
| `BID` | `2222.70` | `195.8295` | 435,270.23 USD | 1,282,389.28 USD | `9 orders` | `-0.02%` | `-` |
| `BID` | `2222.80` | `175.3871` | 389,850.45 USD | 847,119.05 USD | `12 orders` | `-0.01%` | `-` |
| `BID` | `2222.90` | `42.7330` | 94,991.19 USD | 457,268.61 USD | `7 orders` | `-0.01%` | `-` |
| `BID` | `2223.00` | `162.9678` | 362,277.42 USD | 362,277.42 USD | `25 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2223.05` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,223.05` | `0.00%` | `-` |
| `ASK` | `2223.10` | `3.9650` | 8,814.59 USD | 8,814.59 USD | `6 orders` | `+0.00%` | `-` |
| `ASK` | `2223.30` | `1.2668` | 2,816.48 USD | 11,631.07 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `2223.40` | `24.1449` | 53,683.77 USD | 65,314.84 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `2223.50` | `331.6171` | 737,350.62 USD | 802,665.46 USD | `12 orders` | `+0.02%` | `-` |
| `ASK` | `2223.60` | `111.0495` | 246,929.67 USD | 1,049,595.13 USD | `7 orders` | `+0.02%` | `-` |
| `ASK` | `2223.70` | `404.0284` | 898,437.95 USD | 1,948,033.08 USD | `11 orders` | `+0.03%` | `-` |
| `ASK` | `2223.80` | `346.5557` | 770,670.57 USD | 2,718,703.65 USD | `9 orders` | `+0.03%` | `-` |
| `ASK` | `2223.90` | `243.9721` | 542,569.55 USD | 3,261,273.20 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `2224.00` | `110.3812` | 245,487.79 USD | 3,506,760.99 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `2224.10` | `135.8424` | 302,127.08 USD | 3,808,888.07 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `2224.20` | `375.8948` | 836,065.21 USD | 4,644,953.29 USD | `8 orders` | `+0.05%` | `-` |
| `ASK` | `2224.30` | `452.4270` | 1,006,333.38 USD | 5,651,286.66 USD | `11 orders` | `+0.06%` | `-` |
| `ASK` | `2224.40` | `522.0298` | 1,161,203.09 USD | 6,812,489.75 USD | `12 orders` | `+0.06%` | `-` |
| `ASK` | `2224.50` | `245.0989` | 545,222.50 USD | 7,357,712.25 USD | `6 orders` | `+0.07%` | `-` |
| `ASK` | `2224.60` | `98.8485` | 219,898.37 USD | 7,577,610.62 USD | `9 orders` | `+0.07%` | `-` |
| `ASK` | `2224.70` | `118.1025` | 262,742.63 USD | 7,840,353.26 USD | `11 orders` | `+0.07%` | `-` |
| `ASK` | `2224.80` | `302.7196` | 673,490.57 USD | 8,513,843.82 USD | `11 orders` | `+0.08%` | `-` |
| `ASK` | `2224.90` | `53.4372` | 118,892.43 USD | 8,632,736.25 USD | `9 orders` | `+0.08%` | `-` |
| `ASK` | `2225.00` | `137.6028` | 306,166.23 USD | 8,938,902.48 USD | `5 orders` | `+0.09%` | `-` |
| `ASK` | `2225.10` | `83.6562` | 186,143.41 USD | 9,125,045.89 USD | `5 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:52:21 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1786.14` | `30,282.40` | 54,088,732.77 USD | `AT_RISK_LIQ` | `0xde8d9e530b` | `2026-10-30 14:52:21 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1843.94` | `7,964.66` | 14,686,315.60 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 14:52:21 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 14:52:21 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `10,000.00` | 19,261,000.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 14:52:21 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1929.22` | `8,092.45` | 15,612,143.31 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 14:52:21 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2121.88` | `30,641.99` | 65,018,755.10 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 14:52:21 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.16` | `26,025.05` | 55,411,549.64 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 14:52:21 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,533.33` | 7,684,999.71 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2186.40` | `2,173.42` | 4,751,960.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2191.10` | `500.00` | 1,095,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2193.90` | `4,250.16` | 9,324,427.12 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 14:52:21 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2195.00` | `839.60` | 1,842,926.39 USD | `TRIGGER_STOP` | `0x28280399d9` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2198.30` | `1,438.76` | 3,162,824.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2200.20` | `361.20` | 794,719.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2200.30` | `346.28` | 761,925.60 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.00` | `566.99` | 1,247,952.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9362ca4dfd` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.10` | `500.00` | 1,100,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2203.10` | `500.00` | 1,101,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xf929122994` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2206.10` | `1,008.10` | 2,223,970.95 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2206.80` | `244.00` | 538,459.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x24fb652303` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2207.40` | `266.00` | 587,168.40 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x24fb652303` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2208.20` | `2,192.19` | 4,840,789.10 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2208.60` | `430.01` | 949,724.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.10` | `500.00` | 1,105,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.10` | `500.00` | 1,105,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xf929122994` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2212.40` | `705.64` | 1,561,159.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2212.70` | `1,810.43` | 4,005,935.36 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2212.70` | `344.01` | 761,190.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2214.90` | `354.26` | 784,647.37 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2215.00` | `1,356.47` | 3,004,579.06 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2215.70` | `1,118.46` | 2,478,179.36 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2217.50` | `903.29` | 2,003,040.03 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2218.00` | `492.78` | 1,092,985.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:52:21 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2219.00` | `439.90` | 976,147.64 USD | `TRIGGER_STOP` | `0x369fd6445f` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2219.80` | `676.74` | 1,502,223.90 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2220.70` | `353.43` | 784,859.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.10` | `500.00` | 1,110,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.30` | `450.84` | 1,001,456.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2222.00` | `338.03` | 751,092.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2222.60` | `247.82` | 550,801.62 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2225.40` | `247.52` | 550,828.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2226.00` | `337.43` | 751,126.75 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2226.60` | `346.31` | 771,094.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2227.50` | `449.61` | 1,001,507.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2229.50` | `673.81` | 1,502,260.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2230.90` | `344.01` | 767,451.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2231.00` | `897.80` | 2,003,002.06 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2232.20` | `1,118.46` | 2,496,634.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2232.70` | `343.75` | 767,501.34 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2234.10` | `1,344.86` | 3,004,549.05 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2235.10` | `686.12` | 1,533,548.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2235.50` | `1,792.08` | 4,006,191.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2239.70` | `2,192.19` | 4,909,843.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2241.70` | `1,027.78` | 2,303,974.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2242.30` | `430.01` | 964,216.36 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.10` | `339.52` | 761,925.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.20` | `354.12` | 794,719.92 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2249.80` | `1,425.74` | 3,207,632.55 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2254.00` | `4,250.16` | 9,579,861.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 14:52:21 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2261.40` | `2,039.79` | 4,612,772.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:52:21 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2300.00` | `4,002.10` | 9,204,832.99 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 14:52:21 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2468.87` | `22,046.99` | 54,431,199.08 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 14:52:21 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,002.39` | 7,547,704.95 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 14:52:21 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2623.92` | `10,000.00` | 26,239,195.38 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 14:52:21 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2657.77` | `9,700.00` | 25,780,366.97 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 14:52:21 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 228,277,365.61 USD | `102,676.40` | `2322.74` | `2222.30` | `3719.27` | 10,213,547.54 USD | `+4.47%` | `5X Cross` |
| `5` | `0xb83d...6e36` | `SHORT` | 111,372,291.07 USD | `50,093.91` | `2375.30` | `2222.30` | `4593.51` | 7,616,102.94 USD | `+6.84%` | `5X Cross` |
| `9` | `0x77dd...e0e9` | `LONG` | 68,117,147.55 USD | `30,641.99` | `2610.31` | `2222.30` | `2121.80` | -11,868,027.49 USD | `-17.42%` | `10X Cross` |
| `11` | `0xde8d...9524` | `LONG` | 67,372,291.31 USD | `30,282.40` | `2134.45` | `2222.30` | `1786.06` | 2,735,960.73 USD | `+4.06%` | `20X Cross` |
| `15` | `0x0392...d7d9` | `LONG` | 57,890,123.67 USD | `26,025.05` | `2518.71` | `2222.30` | `2129.08` | -7,659,598.42 USD | `-13.23%` | `9X Cross` |
| `22` | `0x8add...7d2c` | `SHORT` | 49,023,684.30 USD | `22,046.99` | `2271.09` | `2222.30` | `2476.65` | 1,047,213.01 USD | `+2.14%` | `25X Cross` |
| `25` | `0x15a4...dfdb` | `SHORT` | 44,490,000.00 USD | `20,000.00` | `2228.11` | `2222.30` | `3187.77` | 72,327.68 USD | `+0.16%` | `20X Cross` |
| `27` | `0xdf95...7d72` | `SHORT` | 43,835,007.98 USD | `19,716.37` | `2402.53` | `2222.30` | `4234.73` | 3,534,249.10 USD | `+8.06%` | `25X Cross` |
| `33` | `0x6046...b21d` | `LONG` | 35,430,923.29 USD | `15,927.59` | `2410.19` | `2222.30` | `1783.78` | -2,957,696.36 USD | `-8.35%` | `6X Cross` |
| `36` | `0xefe4...194b` | `SHORT` | 33,000,650.47 USD | `14,843.29` | `2250.83` | `2222.30` | `2949.38` | 409,210.36 USD | `+1.24%` | `20X Cross` |
| `37` | `0xb695...a92d` | `SHORT` | 32,859,838.98 USD | `14,795.73` | `2557.74` | `2222.30` | `3782.46` | 4,983,875.13 USD | `+15.17%` | `20X Cross` |
| `38` | `0xeced...6210` | `SHORT` | 32,656,357.15 USD | `14,687.58` | `2522.09` | `2222.30` | `3647.96` | 4,387,160.39 USD | `+13.43%` | `20X Cross` |
| `40` | `0x45d2...4029` | `SHORT` | 31,014,616.50 USD | `13,950.00` | `2443.60` | `2222.30` | `5370.34` | 3,073,665.96 USD | `+9.91%` | `20X Cross` |
| `42` | `0xa61c...66b9` | `LONG` | 28,622,959.20 USD | `12,888.00` | `2369.69` | `2222.30` | `1482.03` | -1,917,695.34 USD | `-6.70%` | `10X Cross` |
| `45` | `0x2371...0883` | `LONG` | 26,688,480.00 USD | `12,000.00` | `2421.77` | `2222.30` | `1279.04` | -2,372,814.85 USD | `-8.89%` | `20X Cross` |
| `46` | `0xbd1c...ff0e` | `LONG` | 26,679,240.00 USD | `12,000.00` | `2419.91` | `2222.30` | `1519.94` | -2,359,792.39 USD | `-8.85%` | `20X Cross` |
| `52` | `0xa9de...e049` | `LONG` | 24,469,500.00 USD | `11,000.00` | `2481.81` | `2222.30` | `1643.68` | -2,830,479.46 USD | `-11.57%` | `20X Cross` |
| `53` | `0x0c5d...36b3` | `LONG` | 24,469,500.00 USD | `11,000.00` | `2482.20` | `2222.30` | `1644.01` | -2,834,753.24 USD | `-11.58%` | `20X Cross` |
| `54` | `0x09dc...c094` | `LONG` | 24,467,300.00 USD | `11,000.00` | `2465.31` | `2222.30` | `1637.01` | -2,651,123.04 USD | `-10.84%` | `20X Cross` |
| `55` | `0x6c93...59a4` | `LONG` | 24,431,000.00 USD | `11,000.00` | `2441.15` | `2222.30` | `1601.97` | -2,421,672.73 USD | `-9.91%` | `20X Cross` |
| `69` | `0xa2ce...3126` | `LONG` | 22,252,488.26 USD | `10,016.88` | `2162.83` | `2222.30` | `1559.68` | 587,686.21 USD | `+2.64%` | `10X Cross` |
| `70` | `0xec7f...df39` | `LONG` | 22,243,000.00 USD | `10,000.00` | `2719.35` | `2222.30` | `1720.53` | -4,950,548.52 USD | `-22.26%` | `20X Cross` |
| `71` | `0x6646...6de5` | `LONG` | 22,232,800.00 USD | `10,000.00` | `1765.80` | `2222.30` | `1719.46` | 4,574,742.55 USD | `+20.58%` | `25X Cross` |
| `72` | `0xb37f...66ca` | `SHORT` | 22,209,000.00 USD | `10,000.00` | `2290.69` | `2222.30` | `2623.84` | 697,991.85 USD | `+3.14%` | `25X Cross` |
| `75` | `0x939f...04d2` | `LONG` | 21,856,018.94 USD | `9,823.81` | `2427.28` | `2222.30` | `1717.29` | -1,989,131.66 USD | `-9.10%` | `25X Cross` |
| `77` | `0xaeaa...2416` | `SHORT` | 21,572,800.00 USD | `9,700.00` | `2311.92` | `2222.30` | `2657.69` | 852,882.40 USD | `+3.95%` | `25X Cross` |
| `80` | `0xecb6...2b00` | `SHORT` | 21,138,091.02 USD | `9,507.66` | `2240.81` | `2222.30` | `5547.95` | 166,846.60 USD | `+0.79%` | `15X Cross` |
| `85` | `0xf517...c032` | `SHORT` | 20,734,987.72 USD | `9,326.35` | `2202.91` | `2222.30` | `3115.61` | -189,849.50 USD | `-0.92%` | `25X Cross` |
| `86` | `0xca49...53c8` | `SHORT` | 20,413,813.69 USD | `9,181.89` | `2549.39` | `2222.30` | `3895.66` | 2,994,463.70 USD | `+14.67%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 20,132,745.90 USD | `9,054.12` | `2493.89` | `2222.30` | `2771.52` | 2,447,261.36 USD | `+12.16%` | `20X Cross` |
| `89` | `0xea00...a918` | `LONG` | 20,028,111.22 USD | `9,003.83` | `2003.01` | `2222.30` | `1428.57` | 1,993,332.36 USD | `+9.95%` | `5X Cross` |
| `114` | `0x9eec...daab` | `LONG` | 17,989,521.02 USD | `8,092.45` | `1658.44` | `2222.30` | `1930.27` | 4,568,656.49 USD | `+25.40%` | `15X Cross` |
| `115` | `0x5f91...65aa` | `LONG` | 17,719,766.45 USD | `7,964.66` | `1626.99` | `2222.30` | `1843.86` | 4,761,323.38 USD | `+26.87%` | `16X Cross` |
| `126` | `0xec0b...b078` | `LONG` | 15,563,620.58 USD | `7,007.80` | `2065.97` | `2222.30` | `1056.42` | 1,085,690.99 USD | `+6.98%` | `25X Cross` |
| `130` | `0xf02d...5eb3` | `LONG` | 15,227,143.80 USD | `6,855.99` | `2383.33` | `2222.30` | `1129.81` | -1,112,944.97 USD | `-7.31%` | `20X Cross` |
| `132` | `0xcf53...ee11` | `SHORT` | 15,126,369.84 USD | `6,803.63` | `1862.69` | `2222.30` | `4196.89` | -2,453,264.45 USD | `-16.22%` | `7X Cross` |
| `136` | `0x4ff9...38d3` | `LONG` | 14,595,929.87 USD | `6,564.10` | `2447.40` | `2222.30` | `1669.63` | -1,469,092.88 USD | `-10.07%` | `3X Isolated` |
| `138` | `0x1ee7...edf5` | `LONG` | 14,461,200.00 USD | `6,500.00` | `2301.55` | `2222.30` | `2068.84` | -498,893.66 USD | `-3.45%` | `25X Cross` |
| `139` | `0xf78c...c581` | `LONG` | 14,459,092.70 USD | `6,500.22` | `2521.53` | `2222.30` | `1913.11` | -1,931,448.24 USD | `-13.36%` | `20X Cross` |
| `143` | `0x799f...5f4c` | `LONG` | 14,016,516.23 USD | `6,310.90` | `2390.33` | `2222.30` | `1870.36` | -1,068,648.39 USD | `-7.62%` | `20X Cross` |
| `148` | `0x08bf...7872` | `SHORT` | 13,823,609.28 USD | `6,224.05` | `2258.00` | `2222.30` | `2584.91` | 230,306.83 USD | `+1.67%` | `20X Cross` |
| `150` | `0xec4a...cf62` | `LONG` | 13,695,471.01 USD | `6,166.63` | `2225.41` | `2222.30` | `1961.48` | -27,848.43 USD | `-0.20%` | `25X Cross` |
| `152` | `0xd9e7...4aff` | `LONG` | 13,347,000.00 USD | `6,000.00` | `2480.18` | `2222.30` | `1407.40` | -1,534,124.33 USD | `-11.49%` | `20X Cross` |
| `153` | `0x524e...0de0` | `LONG` | 13,325,400.00 USD | `6,000.00` | `2246.48` | `2222.30` | `2002.81` | -153,485.04 USD | `-1.15%` | `10X Cross` |
| `155` | `0xc179...e0c8` | `LONG` | 13,016,705.45 USD | `5,854.73` | `2294.94` | `2222.30` | `1159.53` | -419,566.73 USD | `-3.22%` | `10X Cross` |
| `162` | `0x0c4a...1b19` | `LONG` | 12,584,660.78 USD | `5,660.10` | `2373.06` | `2222.30` | `2081.45` | -847,097.35 USD | `-6.73%` | `25X Isolated` |
| `168` | `0x7fda...17d1` | `LONG` | 11,818,419.78 USD | `5,315.76` | `2211.05` | `2222.30` | `0.000000` | 64,977.54 USD | `+0.55%` | `25X Cross` |
| `185` | `0x45ab...6cbc` | `LONG` | 10,948,156.70 USD | `4,920.96` | `2727.66` | `2222.30` | `1380.05` | -2,474,587.09 USD | `-22.60%` | `7X Cross` |
| `189` | `0x64b7...9da9` | `LONG` | 10,786,554.18 USD | `4,856.84` | `2604.61` | `2222.30` | `600.58` | -1,863,660.24 USD | `-17.28%` | `25X Cross` |
| `197` | `0xfb18...eb17` | `SHORT` | 10,600,908.42 USD | `4,768.16` | `2315.53` | `2222.30` | `2624.21` | 439,921.28 USD | `+4.15%` | `25X Cross` |
| `198` | `0x5559...d43b` | `SHORT` | 10,579,555.83 USD | `4,755.93` | `2262.69` | `2222.30` | `2747.48` | 181,650.05 USD | `+1.72%` | `25X Cross` |
| `210` | `0xe091...6705` | `SHORT` | 10,010,250.44 USD | `4,500.00` | `2467.33` | `2222.30` | `2463.03` | 1,092,758.06 USD | `+10.92%` | `20X Cross` |
| `212` | `0x418a...8888` | `SHORT` | 9,994,050.00 USD | `4,500.00` | `2494.55` | `2222.30` | `2994.21` | 1,231,434.41 USD | `+12.32%` | `25X Cross` |
| `218` | `0xb829...3a81` | `LONG` | 9,770,766.14 USD | `4,394.91` | `2398.60` | `2222.30` | `1456.38` | -770,875.81 USD | `-7.89%` | `20X Cross` |
| `238` | `0x28bb...fca6` | `SHORT` | 9,349,132.18 USD | `4,209.61` | `1896.10` | `2222.30` | `3034.75` | -1,367,249.61 USD | `-14.62%` | `20X Cross` |
| `240` | `0x6ea4...0ea7` | `SHORT` | 9,302,732.95 USD | `4,184.01` | `2602.13` | `2222.30` | `3424.97` | 1,584,613.72 USD | `+17.03%` | `20X Cross` |
| `251` | `0x5e9e...35ee` | `SHORT` | 8,909,878.36 USD | `4,007.56` | `1796.39` | `2222.30` | `2585.47` | -1,710,728.27 USD | `-19.20%` | `20X Cross` |
| `253` | `0xfb94...0ddf` | `SHORT` | 8,903,874.97 USD | `4,002.10` | `2382.44` | `2222.30` | `5104.36` | 630,909.18 USD | `+7.09%` | `20X Cross` |
| `254` | `0x3dc9...54b0` | `SHORT` | 8,896,910.88 USD | `3,999.69` | `2480.32` | `2222.30` | `6586.52` | 1,023,625.67 USD | `+11.51%` | `20X Cross` |
| `255` | `0x8cc9...2b6a` | `SHORT` | 8,893,200.00 USD | `4,000.00` | `1791.18` | `2222.30` | `3533.57` | -1,728,453.33 USD | `-19.44%` | `25X Cross` |
| `275` | `0x4b67...f4e7` | `LONG` | 8,498,698.64 USD | `3,820.84` | `2591.51` | `2222.30` | `1347.48` | -1,403,074.90 USD | `-16.51%` | `20X Cross` |
| `282` | `0x12d2...f97f` | `LONG` | 8,344,501.40 USD | `3,757.26` | `2446.50` | `2222.30` | `1803.57` | -847,664.99 USD | `-10.16%` | `20X Cross` |
| `299` | `0x8ae4...3d60` | `LONG` | 7,914,500.48 USD | `3,558.20` | `2482.21` | `2222.30` | `518.03` | -917,697.56 USD | `-11.60%` | `10X Cross` |
| `301` | `0x469e...58a5` | `SHORT` | 7,856,719.70 USD | `3,533.33` | `2203.63` | `2222.30` | `3086.55` | -70,556.61 USD | `-0.90%` | `25X Cross` |
| `311` | `0x218a...7da2` | `SHORT` | 7,709,083.73 USD | `3,465.07` | `2208.16` | `2222.30` | `3101.69` | -57,654.48 USD | `-0.75%` | `10X Cross` |
| `337` | `0x9c2a...f6a8` | `SHORT` | 6,678,213.19 USD | `3,002.39` | `2515.77` | `2222.30` | `2588.93` | 875,124.71 USD | `+13.10%` | `20X Cross` |
| `338` | `0xb823...9763` | `SHORT` | 6,672,900.00 USD | `3,000.00` | `2229.66` | `2222.30` | `3233.36` | 16,096.68 USD | `+0.24%` | `25X Cross` |
| `339` | `0x4a20...3c26` | `LONG` | 6,669,000.00 USD | `3,000.00` | `2428.72` | `2222.30` | `617.20` | -617,160.28 USD | `-9.25%` | `20X Cross` |
| `341` | `0x007d...67a0` | `LONG` | 6,662,700.00 USD | `3,000.00` | `2400.00` | `2222.30` | `1469.19` | -537,300.00 USD | `-8.06%` | `25X Cross` |
| `394` | `0x8328...f54a` | `SHORT` | 5,732,088.41 USD | `2,576.45` | `2292.01` | `2222.30` | `3279.21` | 173,182.88 USD | `+3.02%` | `25X Cross` |
| `396` | `0xed48...7c9b` | `SHORT` | 5,671,163.10 USD | `2,551.13` | `2460.02` | `2222.30` | `3226.02` | 604,683.31 USD | `+10.66%` | `20X Cross` |
| `400` | `0x970c...2a93` | `SHORT` | 5,559,000.00 USD | `2,500.00` | `2229.57` | `2222.30` | `5077.82` | 14,944.49 USD | `+0.27%` | `20X Cross` |
| `401` | `0x1c98...7fc7` | `LONG` | 5,558,510.01 USD | `2,500.00` | `2452.60` | `2222.30` | `1916.60` | -573,011.56 USD | `-10.31%` | `10X Cross` |
| `417` | `0xa445...329d` | `LONG` | 5,348,839.88 USD | `2,406.14` | `2354.86` | `2222.30` | `1767.01` | -317,275.40 USD | `-5.93%` | `25X Cross` |
| `418` | `0xfbe2...c8ea` | `SHORT` | 5,302,312.94 USD | `2,385.21` | `2041.57` | `2222.30` | `2622.48` | -432,746.28 USD | `-8.16%` | `20X Cross` |
| `419` | `0x6749...ce07` | `SHORT` | 5,296,850.02 USD | `2,384.89` | `2220.92` | `2222.30` | `3630.85` | -186.99 USD | `-0.00%` | `20X Cross` |
| `420` | `0x645b...87b8` | `SHORT` | 5,291,399.75 USD | `2,379.98` | `2421.64` | `2222.30` | `11548.89` | 472,047.20 USD | `+8.92%` | `10X Cross` |
| `428` | `0x0622...8088` | `LONG` | 5,165,320.51 USD | `2,322.95` | `2228.94` | `2222.30` | `0.000000` | -12,405.19 USD | `-0.24%` | `5X Cross` |
| `431` | `0x77ee...2902` | `SHORT` | 5,093,122.81 USD | `2,290.69` | `2476.53` | `2222.30` | `6113.65` | 579,849.42 USD | `+11.38%` | `25X Cross` |
| `455` | `0xd507...c948` | `SHORT` | 4,823,794.58 USD | `2,172.00` | `2387.49` | `2222.30` | `2600.21` | 361,846.45 USD | `+7.50%` | `5X Isolated` |
| `462` | `0x023a...2355` | `LONG` | 4,758,993.38 USD | `2,142.82` | `2328.93` | `2222.30` | `0.000000` | -231,510.47 USD | `-4.86%` | `25X Cross` |
| `465` | `0x382b...3e39` | `SHORT` | 4,734,545.95 USD | `2,129.54` | `2296.66` | `2222.30` | `4553.38` | 156,291.26 USD | `+3.30%` | `25X Cross` |
| `502` | `0x3453...b323` | `SHORT` | 4,449,073.82 USD | `2,000.12` | `2322.47` | `2222.30` | `2397.68` | 196,162.02 USD | `+4.41%` | `25X Cross` |
| `503` | `0xe02e...d78b` | `LONG` | 4,442,000.00 USD | `2,000.00` | `2228.11` | `2222.30` | `2171.55` | -14,223.47 USD | `-0.32%` | `25X Cross` |
| `507` | `0xf3dc...1672` | `SHORT` | 4,405,115.68 USD | `1,980.36` | `2240.44` | `2222.30` | `2789.84` | 31,771.88 USD | `+0.72%` | `20X Cross` |
| `509` | `0x7a6d...f79c` | `SHORT` | 4,385,467.39 USD | `1,971.44` | `2418.41` | `2222.30` | `2543.58` | 382,293.79 USD | `+8.72%` | `25X Cross` |
| `512` | `0xac48...3201` | `SHORT` | 4,369,543.52 USD | `1,964.37` | `2272.04` | `2222.30` | `3091.31` | 93,598.78 USD | `+2.14%` | `20X Cross` |
| `525` | `0x8376...9a1e` | `SHORT` | 4,248,561.00 USD | `1,910.50` | `2477.72` | `2222.30` | `3186.04` | 485,127.17 USD | `+11.42%` | `20X Cross` |
| `529` | `0x739c...cfb2` | `SHORT` | 4,226,360.00 USD | `1,900.00` | `2418.12` | `2222.30` | `2448.91` | 368,086.38 USD | `+8.71%` | `25X Cross` |
| `541` | `0xbcd4...0dd2` | `SHORT` | 4,135,926.68 USD | `1,861.64` | `2233.24` | `2222.30` | `2739.62` | 21,573.80 USD | `+0.52%` | `25X Cross` |
| `546` | `0x4487...c92d` | `LONG` | 4,093,501.84 USD | `1,841.21` | `2232.11` | `2222.30` | `1604.57` | -16,277.68 USD | `-0.40%` | `10X Cross` |
| `558` | `0x7265...91a5` | `LONG` | 4,008,258.48 USD | `1,801.87` | `2533.96` | `2222.30` | `1987.07` | -557,607.98 USD | `-13.91%` | `20X Cross` |
| `559` | `0xbb34...1696` | `LONG` | 4,004,640.00 USD | `1,800.00` | `2313.95` | `2222.30` | `1984.20` | -160,478.23 USD | `-4.01%` | `25X Cross` |
| `560` | `0xc619...10f5` | `LONG` | 4,002,480.00 USD | `1,800.00` | `2313.55` | `2222.30` | `1821.08` | -161,915.83 USD | `-4.05%` | `25X Cross` |
| `572` | `0x91a9...3f70` | `SHORT` | 3,931,936.01 USD | `1,767.48` | `2156.23` | `2222.30` | `3670.77` | -120,831.93 USD | `-3.07%` | `4X Cross` |
| `608` | `0xfeec...4e9c` | `SHORT` | 3,757,507.34 USD | `1,691.81` | `2566.49` | `2222.30` | `2509.64` | 584,517.17 USD | `+15.56%` | `10X Cross` |
| `628` | `0xeee0...0b53` | `LONG` | 3,642,273.25 USD | `1,637.12` | `2468.64` | `2222.30` | `191.36` | -399,202.81 USD | `-10.96%` | `7X Cross` |
| `630` | `0x27b8...12fc` | `LONG` | 3,621,427.54 USD | `1,628.12` | `2468.73` | `2222.30` | `632.58` | -397,967.10 USD | `-10.99%` | `10X Cross` |
| `631` | `0x982b...4606` | `LONG` | 3,619,343.13 USD | `1,626.82` | `2575.24` | `2222.30` | `1547.35` | -570,109.95 USD | `-15.75%` | `5X Isolated` |
| `638` | `0x73d7...8be1` | `LONG` | 3,560,490.20 USD | `1,601.47` | `2410.40` | `2222.30` | `1766.47` | -299,688.72 USD | `-8.42%` | `25X Cross` |
| `639` | `0xad54...6203` | `LONG` | 3,553,531.31 USD | `1,597.45` | `2591.98` | `2222.30` | `2046.41` | -587,046.74 USD | `-16.52%` | `10X Isolated` |
| `645` | `0x880a...311c` | `LONG` | 3,509,224.48 USD | `1,578.40` | `2209.72` | `2222.30` | `0.000000` | 21,400.63 USD | `+0.61%` | `9X Cross` |
| `651` | `0x936c...bb0f` | `LONG` | 3,487,096.72 USD | `1,568.64` | `2232.92` | `2222.30` | `0.000000` | -15,572.89 USD | `-0.45%` | `20X Cross` |
| `662` | `0xe170...9300` | `SHORT` | 3,409,974.92 USD | `1,533.40` | `2076.39` | `2222.30` | `3107.38` | -226,025.42 USD | `-6.63%` | `25X Cross` |
| `667` | `0x4b86...df9d` | `SHORT` | 3,390,138.00 USD | `1,524.00` | `2287.40` | `2222.30` | `2759.56` | 95,859.60 USD | `+2.83%` | `9X Isolated` |
| `673` | `0x2e2b...2fab` | `LONG` | 3,353,009.40 USD | `1,507.38` | `2245.53` | `2222.30` | `1248.80` | -31,863.70 USD | `-0.95%` | `25X Cross` |
| `677` | `0xde6b...3361` | `LONG` | 3,336,450.00 USD | `1,500.00` | `2216.98` | `2222.30` | `2168.48` | 10,969.26 USD | `+0.33%` | `25X Cross` |
| `679` | `0x251f...6e5d` | `LONG` | 3,331,350.00 USD | `1,500.00` | `2346.68` | `2222.30` | `1900.05` | -188,680.49 USD | `-5.66%` | `20X Cross` |
| `697` | `0xb885...3c54` | `LONG` | 3,223,746.39 USD | `1,450.00` | `2274.34` | `2222.30` | `30.94` | -74,061.75 USD | `-2.30%` | `20X Cross` |
| `700` | `0xef70...a84c` | `SHORT` | 3,208,661.32 USD | `1,442.74` | `2424.73` | `2222.30` | `3256.57` | 289,609.50 USD | `+9.03%` | `25X Cross` |
| `705` | `0xe668...b5ca` | `SHORT` | 3,190,289.20 USD | `1,434.22` | `2241.90` | `2222.30` | `2319.00` | 25,111.09 USD | `+0.79%` | `25X Cross` |
| `708` | `0xbadb...9ee6` | `LONG` | 3,176,941.92 USD | `1,428.16` | `1936.00` | `2222.30` | `1078.14` | 412,020.27 USD | `+12.97%` | `20X Cross` |
| `761` | `0x53f8...ceff` | `LONG` | 2,999,946.62 USD | `1,348.65` | `2276.73` | `2222.30` | `0.000000` | -70,577.84 USD | `-2.35%` | `20X Cross` |
| `774` | `0x020c...5872` | `LONG` | 2,956,962.40 USD | `1,330.00` | `2226.24` | `2222.30` | `2135.69` | -3,945.03 USD | `-0.13%` | `25X Cross` |
| `781` | `0xa0fb...96be` | `LONG` | 2,928,159.82 USD | `1,317.09` | `2277.10` | `2222.30` | `1519.85` | -71,002.46 USD | `-2.42%` | `3X Cross` |
| `785` | `0x0dd5...f6ee` | `LONG` | 2,890,034.64 USD | `1,300.84` | `2290.95` | `2222.30` | `1551.66` | -90,147.08 USD | `-3.12%` | `5X Cross` |
| `794` | `0x039c...0ebd` | `LONG` | 2,864,525.70 USD | `1,289.80` | `2226.24` | `2222.30` | `0.000000` | -6,888.23 USD | `-0.24%` | `25X Cross` |
| `803` | `0xb8eb...1dd5` | `LONG` | 2,835,240.25 USD | `1,276.62` | `2232.77` | `2222.30` | `726.68` | -15,159.19 USD | `-0.53%` | `25X Cross` |
| `812` | `0x1f16...6d07` | `LONG` | 2,811,912.60 USD | `1,266.00` | `2261.43` | `2222.30` | `1383.30` | -51,058.63 USD | `-1.82%` | `7X Cross` |
| `820` | `0xc435...c905` | `SHORT` | 2,776,176.00 USD | `1,248.00` | `2704.38` | `2222.30` | `3786.81` | 598,894.35 USD | `+21.57%` | `20X Cross` |
| `825` | `0x6859...7e1e` | `SHORT` | 2,751,430.05 USD | `1,237.15` | `2200.39` | `2222.30` | `4863.01` | -29,202.89 USD | `-1.06%` | `25X Cross` |
| `835` | `0x7178...0854` | `LONG` | 2,709,992.73 USD | `1,218.63` | `2461.81` | `2222.30` | `1185.00` | -290,053.67 USD | `-10.70%` | `10X Cross` |
| `836` | `0x7277...0b98` | `SHORT` | 2,708,407.11 USD | `1,219.45` | `2206.05` | `2222.30` | `3414.31` | -18,219.31 USD | `-0.67%` | `20X Cross` |
| `848` | `0xaaa1...ab8c` | `SHORT` | 2,669,160.00 USD | `1,200.00` | `2276.29` | `2222.30` | `2365.18` | 62,397.58 USD | `+2.34%` | `25X Isolated` |
| `860` | `0xfc27...9d9d` | `LONG` | 2,628,595.69 USD | `1,182.31` | `2237.33` | `2222.30` | `0.000000` | -16,629.65 USD | `-0.63%` | `25X Cross` |
| `863` | `0x07fd...689d` | `LONG` | 2,613,316.15 USD | `1,176.69` | `2416.34` | `2222.30` | `0.000000` | -229,983.79 USD | `-8.80%` | `25X Cross` |
| `919` | `0x2f80...f203` | `SHORT` | 2,420,933.85 USD | `1,088.94` | `1984.00` | `2222.30` | `2959.41` | -260,466.66 USD | `-10.76%` | `20X Cross` |
| `923` | `0x6f11...0389` | `SHORT` | 2,399,696.00 USD | `1,079.00` | `2333.39` | `2222.30` | `2971.51` | 118,032.91 USD | `+4.92%` | `25X Cross` |
| `924` | `0x8eb7...b90f` | `LONG` | 2,397,215.30 USD | `1,077.74` | `2396.38` | `2222.30` | `1880.88` | -185,462.74 USD | `-7.74%` | `5X Isolated` |
| `927` | `0x2b61...2f6c` | `SHORT` | 2,394,675.15 USD | `1,076.60` | `2681.75` | `2222.30` | `6286.63` | 492,497.59 USD | `+20.57%` | `10X Cross` |
| `929` | `0x2577...4897` | `LONG` | 2,389,884.60 USD | `1,074.94` | `2232.09` | `2222.30` | `0.000000` | -9,473.52 USD | `-0.40%` | `15X Cross` |
| `939` | `0xef96...9383` | `LONG` | 2,363,644.34 USD | `1,063.13` | `2234.39` | `2222.30` | `0.000000` | -11,812.19 USD | `-0.50%` | `25X Cross` |
| `962` | `0x30af...393e` | `SHORT` | 2,315,550.74 USD | `1,041.16` | `2252.26` | `2222.30` | `2296.87` | 29,431.59 USD | `+1.27%` | `25X Cross` |
| `974` | `0x1b2a...f7a6` | `LONG` | 2,281,238.73 USD | `1,025.37` | `2737.51` | `2222.30` | `882.02` | -525,721.21 USD | `-23.05%` | `10X Cross` |
| `986` | `0x001a...fef6` | `SHORT` | 2,237,268.83 USD | `1,007.33` | `2022.19` | `2222.30` | `3090.45` | -200,260.87 USD | `-8.95%` | `10X Cross` |
| `988` | `0x02aa...1806` | `SHORT` | 2,236,668.61 USD | `1,007.10` | `2654.68` | `2222.30` | `3612.66` | 436,863.49 USD | `+19.53%` | `20X Cross` |
| `990` | `0xdb3a...cf3b` | `LONG` | 2,231,150.38 USD | `1,003.22` | `2705.01` | `2222.30` | `0.000000` | -482,556.51 USD | `-21.63%` | `4X Cross` |
| `991` | `0xf929...d1f9` | `SHORT` | 2,224,500.00 USD | `1,000.00` | `2423.37` | `2222.30` | `2926.09` | 198,870.17 USD | `+8.94%` | `25X Cross` |
| `992` | `0x6463...42f5` | `SHORT` | 2,224,300.00 USD | `1,000.00` | `2223.43` | `2222.30` | `3703.25` | -865.05 USD | `-0.04%` | `5X Cross` |
| `993` | `0x8c02...b73f` | `SHORT` | 2,223,900.00 USD | `1,000.00` | `2250.37` | `2222.30` | `8098.34` | 26,471.47 USD | `+1.19%` | `20X Cross` |
| `994` | `0xd7b8...9f55` | `LONG` | 2,222,275.50 USD | `999.00` | `2195.00` | `2222.30` | `0.000000` | 29,470.50 USD | `+1.33%` | `15X Cross` |
| `996` | `0x5272...fcd9` | `SHORT` | 2,221,000.00 USD | `1,000.00` | `2241.82` | `2222.30` | `2830.71` | 20,824.49 USD | `+0.94%` | `5X Cross` |
| `1000` | `0x9599...c60a` | `LONG` | 2,211,122.71 USD | `995.60` | `2233.08` | `2222.30` | `0.000000` | -12,127.50 USD | `-0.55%` | `20X Cross` |
| `1029` | `0xb002...ed8a` | `SHORT` | 2,141,135.34 USD | `962.78` | `2299.66` | `2222.30` | `4199.33` | 72,942.57 USD | `+3.41%` | `25X Cross` |
| `1048` | `0xb1ec...e86a` | `SHORT` | 2,076,785.26 USD | `933.64` | `2272.72` | `2222.30` | `12603.09` | 45,121.70 USD | `+2.17%` | `25X Cross` |
| `1055` | `0xb812...b5e0` | `LONG` | 2,059,963.05 USD | `927.24` | `2263.21` | `2222.30` | `1165.89` | -38,586.70 USD | `-1.87%` | `25X Cross` |
| `1072` | `0xede2...f971` | `LONG` | 2,032,772.25 USD | `914.31` | `2208.16` | `2222.30` | `1462.93` | 13,815.26 USD | `+0.68%` | `5X Cross` |
| `1074` | `0x9606...4e5d` | `SHORT` | 2,030,322.06 USD | `913.00` | `2478.70` | `2222.30` | `4319.94` | 232,731.54 USD | `+11.46%` | `20X Cross` |
| `1097` | `0x5f10...d49d` | `LONG` | 1,998,900.00 USD | `900.00` | `2249.83` | `2222.30` | `1817.63` | -25,953.47 USD | `-1.30%` | `25X Cross` |
| `1108` | `0x51f6...2b39` | `LONG` | 1,979,047.13 USD | `890.15` | `2226.49` | `2222.30` | `747.45` | -2,859.76 USD | `-0.14%` | `25X Cross` |
| `1183` | `0x2828...93a0` | `LONG` | 1,867,694.65 USD | `839.60` | `2242.41` | `2222.30` | `2192.48` | -15,037.54 USD | `-0.81%` | `25X Cross` |
| `1187` | `0xcd27...52a8` | `LONG` | 1,859,355.91 USD | `837.21` | `2553.56` | `2222.30` | `1403.16` | -278,508.86 USD | `-14.98%` | `2X Cross` |
| `1246` | `0x04a9...95aa` | `LONG` | 1,779,200.00 USD | `800.00` | `2595.13` | `2222.30` | `1871.98` | -296,906.74 USD | `-16.69%` | `5X Cross` |
| `1250` | `0x7737...bf66` | `SHORT` | 1,778,577.23 USD | `799.79` | `2494.83` | `2222.30` | `24846.55` | 216,768.80 USD | `+12.19%` | `15X Cross` |
| `1276` | `0x458d...ab3b` | `LONG` | 1,722,959.85 USD | `774.75` | `2740.41` | `2222.30` | `1886.92` | -400,169.33 USD | `-23.23%` | `3X Isolated` |
| `1332` | `0x3fc5...c0c1` | `SHORT` | 1,623,643.39 USD | `729.92` | `2702.11` | `2222.30` | `4697.26` | 348,698.81 USD | `+21.48%` | `25X Cross` |
| `1333` | `0xaa53...9cb7` | `LONG` | 1,622,077.81 USD | `730.34` | `2389.70` | `2222.30` | `1930.07` | -123,211.83 USD | `-7.60%` | `20X Cross` |
| `1348` | `0xa189...94d7` | `SHORT` | 1,599,001.36 USD | `719.98` | `2691.84` | `2222.30` | `2914.81` | 339,071.30 USD | `+21.21%` | `25X Cross` |
| `1365` | `0x2f93...4404` | `LONG` | 1,572,907.24 USD | `707.47` | `1700.45` | `2222.30` | `1368.55` | 369,880.86 USD | `+23.52%` | `4X Isolated` |
| `1375` | `0x5605...fe0f` | `SHORT` | 1,561,778.01 USD | `702.14` | `2566.90` | `2222.30` | `3091.14` | 240,554.64 USD | `+15.40%` | `20X Cross` |
| `1382` | `0x26e6...6b28` | `LONG` | 1,557,080.00 USD | `700.00` | `1835.24` | `2222.30` | `2042.98` | 272,408.47 USD | `+17.49%` | `20X Cross` |
| `1385` | `0x0deb...0bc5` | `LONG` | 1,554,700.00 USD | `700.00` | `2071.05` | `2222.30` | `1597.14` | 104,964.21 USD | `+6.75%` | `20X Cross` |
| `1438` | `0x248e...6be2` | `SHORT` | 1,513,839.80 USD | `680.93` | `2282.89` | `2222.30` | `3385.50` | 40,645.87 USD | `+2.68%` | `20X Cross` |
| `1439` | `0xdbd1...29dd` | `SHORT` | 1,513,392.25 USD | `680.70` | `3030.57` | `2222.30` | `3787.60` | 549,528.87 USD | `+36.31%` | `6X Cross` |
| `1447` | `0x71e5...be04` | `LONG` | 1,505,097.96 USD | `677.67` | `2727.27` | `2222.30` | `1470.70` | -343,087.64 USD | `-22.80%` | `20X Cross` |
| `1452` | `0x0b23...f37b` | `LONG` | 1,500,795.00 USD | `675.00` | `2238.15` | `2222.30` | `592.14` | -9,961.64 USD | `-0.66%` | `5X Cross` |
| `1458` | `0x4e23...20c3` | `SHORT` | 1,493,610.73 USD | `672.49` | `2230.51` | `2222.30` | `20303.58` | 6,402.05 USD | `+0.43%` | `20X Cross` |
| `1464` | `0xd911...961e` | `LONG` | 1,476,927.59 USD | `665.01` | `2231.50` | `2222.30` | `0.000000` | -7,055.45 USD | `-0.48%` | `25X Cross` |
| `1470` | `0xa70a...4be9` | `LONG` | 1,466,009.56 USD | `659.39` | `2251.37` | `2222.30` | `45.13` | -18,533.05 USD | `-1.26%` | `20X Cross` |
| `1474` | `0x0cac...6170` | `SHORT` | 1,461,800.02 USD | `657.50` | `2146.55` | `2222.30` | `2839.16` | -50,437.82 USD | `-3.45%` | `20X Cross` |
| `1504` | `0xb15b...dbae` | `SHORT` | 1,429,109.95 USD | `642.64` | `2290.80` | `2222.30` | `2325.09` | 43,057.53 USD | `+3.01%` | `25X Cross` |
| `1508` | `0xf00e...fe3d` | `SHORT` | 1,427,836.48 USD | `642.88` | `2333.21` | `2222.30` | `2486.02` | 72,141.49 USD | `+5.05%` | `20X Cross` |
| `1513` | `0xffb2...5ed6` | `SHORT` | 1,424,809.06 USD | `640.77` | `2672.96` | `2222.30` | `2493.89` | 287,939.29 USD | `+20.21%` | `20X Cross` |
| `1523` | `0x0a97...347d` | `LONG` | 1,412,048.73 USD | `635.11` | `2259.32` | `2222.30` | `942.74` | -22,880.10 USD | `-1.62%` | `20X Cross` |
| `1524` | `0x6e6f...82a6` | `LONG` | 1,411,765.93 USD | `635.47` | `2257.18` | `2222.30` | `697.59` | -22,614.66 USD | `-1.60%` | `20X Cross` |
| `1527` | `0x8505...1821` | `SHORT` | 1,407,962.43 USD | `633.96` | `2239.93` | `2222.30` | `3884.79` | 12,069.17 USD | `+0.86%` | `20X Cross` |
| `1549` | `0xfce0...f4c0` | `SHORT` | 1,387,135.84 USD | `623.60` | `3129.61` | `2222.30` | `2807.76` | 564,490.74 USD | `+40.69%` | `20X Cross` |
| `1598` | `0x7050...5fff` | `SHORT` | 1,336,882.45 USD | `601.11` | `2245.52` | `2222.30` | `3271.72` | 12,917.66 USD | `+0.97%` | `25X Cross` |
| `1600` | `0x24fb...ed0f` | `LONG` | 1,334,973.56 USD | `600.10` | `2199.85` | `2222.30` | `0.000000` | 14,850.13 USD | `+1.11%` | `15X Cross` |
| `1601` | `0x638f...f5f0` | `LONG` | 1,333,962.00 USD | `600.00` | `4011.50` | `2222.30` | `429.17` | -1,072,941.53 USD | `-80.43%` | `25X Cross` |
| `1602` | `0xad02...eb65` | `LONG` | 1,333,917.40 USD | `600.62` | `2460.69` | `2222.30` | `1078.62` | -144,023.16 USD | `-10.80%` | `5X Cross` |
| `1681` | `0x9362...7d7c` | `SHORT` | 1,260,766.75 USD | `566.99` | `2226.19` | `2222.30` | `2518.61` | 1,469.07 USD | `+0.12%` | `20X Cross` |
| `1684` | `0xfb99...37f3` | `LONG` | 1,257,770.88 USD | `565.34` | `2362.35` | `2222.30` | `1253.71` | -77,765.48 USD | `-6.18%` | `3X Cross` |
| `1693` | `0x844b...7f42` | `SHORT` | 1,247,439.60 USD | `561.00` | `2026.17` | `2222.30` | `3037.37` | -110,756.19 USD | `-8.88%` | `25X Cross` |
| `1711` | `0xabe6...1d99` | `SHORT` | 1,234,829.28 USD | `556.00` | `2484.68` | `2222.30` | `3126.50` | 146,666.61 USD | `+11.88%` | `20X Cross` |
| `1712` | `0x2a76...9a53` | `LONG` | 1,234,331.22 USD | `555.03` | `2231.40` | `2222.30` | `0.000000` | -4,164.88 USD | `-0.34%` | `25X Cross` |
| `1718` | `0xbef3...0d3e` | `LONG` | 1,228,817.11 USD | `552.33` | `2233.44` | `2222.30` | `2068.58` | -4,773.71 USD | `-0.39%` | `20X Cross` |
| `1722` | `0x825c...465e` | `LONG` | 1,223,475.00 USD | `550.00` | `2208.12` | `2222.30` | `1189.21` | 9,005.50 USD | `+0.74%` | `4X Cross` |
| `1724` | `0x6a41...a3b9` | `LONG` | 1,223,089.60 USD | `550.69` | `2233.05` | `2222.30` | `2074.03` | -6,636.76 USD | `-0.54%` | `20X Cross` |
| `1730` | `0xad21...fb6a` | `LONG` | 1,216,549.87 USD | `547.26` | `2565.80` | `2222.30` | `1734.50` | -187,603.13 USD | `-15.42%` | `6X Cross` |
| `1768` | `0xfc66...ca06` | `SHORT` | 1,173,174.94 USD | `527.67` | `2275.19` | `2222.30` | `16999.08` | 27,386.10 USD | `+2.33%` | `20X Cross` |
| `1791` | `0x2e30...4cb5` | `SHORT` | 1,160,006.24 USD | `521.76` | `2316.81` | `2222.30` | `11915.02` | 48,808.46 USD | `+4.21%` | `2X Cross` |
| `1803` | `0x6dae...90de` | `SHORT` | 1,150,341.29 USD | `517.05` | `2292.28` | `2222.30` | `3858.20` | 34,892.12 USD | `+3.03%` | `25X Cross` |
| `1837` | `0x0089...2410` | `SHORT` | 1,126,814.58 USD | `507.35` | `2308.88` | `2222.30` | `3364.67` | 44,585.68 USD | `+3.96%` | `20X Cross` |
| `1854` | `0xa559...ff95` | `LONG` | 1,112,400.00 USD | `500.00` | `2260.68` | `2222.30` | `1051.99` | -17,944.36 USD | `-1.61%` | `20X Cross` |
| `1855` | `0x4044...794c` | `LONG` | 1,112,400.00 USD | `500.00` | `2260.80` | `2222.30` | `0.000000` | -18,000.00 USD | `-1.62%` | `25X Cross` |
| `1856` | `0x6936...9417` | `SHORT` | 1,112,200.00 USD | `500.00` | `2315.11` | `2222.30` | `2358.66` | 45,355.21 USD | `+4.08%` | `25X Isolated` |
| `1857` | `0xe282...df29` | `LONG` | 1,111,950.00 USD | `500.00` | `2309.84` | `2222.30` | `2045.06` | -42,974.21 USD | `-3.86%` | `10X Isolated` |
| `1858` | `0x89b2...9ca6` | `LONG` | 1,111,640.00 USD | `500.00` | `2363.45` | `2222.30` | `1622.40` | -70,087.42 USD | `-6.30%` | `25X Cross` |
| `1859` | `0xb322...d51f` | `SHORT` | 1,110,450.00 USD | `500.00` | `2268.03` | `2222.30` | `3743.04` | 23,566.32 USD | `+2.12%` | `20X Cross` |
| `1861` | `0x7298...7d6c` | `SHORT` | 1,108,282.56 USD | `498.15` | `3426.75` | `2222.30` | `5421.37` | 598,753.26 USD | `+54.03%` | `20X Cross` |
| `1869` | `0x9c68...7783` | `SHORT` | 1,097,511.19 USD | `493.31` | `2273.58` | `2222.30` | `3910.58` | 24,068.06 USD | `+2.19%` | `25X Cross` |
| `1881` | `0x404c...5f03` | `SHORT` | 1,088,058.04 USD | `489.79` | `2671.94` | `2222.30` | `5042.23` | 220,621.51 USD | `+20.28%` | `20X Cross` |
| `1885` | `0x321f...1c84` | `SHORT` | 1,085,248.65 USD | `488.02` | `2370.09` | `2222.30` | `3058.17` | 71,395.95 USD | `+6.58%` | `10X Cross` |
| `1892` | `0x94b6...e5b3` | `SHORT` | 1,079,469.78 USD | `486.05` | `2260.75` | `2222.30` | `2351.03` | 19,372.82 USD | `+1.79%` | `25X Cross` |
| `1917` | `0xd4c1...3d1d` | `LONG` | 1,052,325.49 USD | `473.32` | `2242.01` | `2222.30` | `0.000000` | -8,873.43 USD | `-0.84%` | `12X Cross` |
| `1930` | `0xe86b...3664` | `LONG` | 1,043,034.52 USD | `469.14` | `2230.96` | `2222.30` | `0.000000` | -3,594.44 USD | `-0.34%` | `25X Cross` |
| `1954` | `0x82c6...fe42` | `LONG` | 1,028,785.00 USD | `462.50` | `2501.38` | `2222.30` | `2053.40` | -128,105.57 USD | `-12.45%` | `5X Isolated` |
| `1963` | `0xe330...77a1` | `SHORT` | 1,025,434.30 USD | `461.20` | `2206.97` | `2222.30` | `6448.47` | -7,576.94 USD | `-0.74%` | `20X Cross` |
| `1967` | `0x2de3...486d` | `LONG` | 1,022,548.40 USD | `460.40` | `2286.27` | `2222.30` | `1123.25` | -30,052.51 USD | `-2.94%` | `25X Cross` |
| `1968` | `0x7a76...b16d` | `LONG` | 1,021,943.93 USD | `459.50` | `2228.08` | `2222.30` | `2032.95` | -1,860.55 USD | `-0.18%` | `25X Cross` |
| `1970` | `0xd6e1...f256` | `LONG` | 1,019,677.66 USD | `458.64` | `2213.70` | `2222.30` | `918.00` | 4,386.78 USD | `+0.43%` | `25X Cross` |
| `1976` | `0x617e...0f97` | `SHORT` | 1,016,894.62 USD | `457.85` | `2205.60` | `2222.30` | `3371.72` | -7,050.79 USD | `-0.69%` | `10X Cross` |
| `2009` | `0xae55...2236` | `LONG` | 1,000,471.50 USD | `450.00` | `2510.21` | `2222.30` | `0.000000` | -129,126.00 USD | `-12.91%` | `25X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `2320.30` | 86,616.33 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 86.62K USD at 2320.3000 USD [API] | `2026-10-29 09:28:28` |
| `ANNOUNCEMENT` | `INFO` | `2318.30` | 115,915.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 115.92K USD at 2318.3000 USD [API] | `2026-10-29 09:30:17` |
| `ANNOUNCEMENT` | `INFO` | `2319.20` | 55,554.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 55.55K USD at 2319.2000 USD [API] | `2026-10-29 09:42:18` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 53.78 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.05K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 32,997.80 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 33.00K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 261.77 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.26K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 19.66 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 1,287.31 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.29K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 1,810.63 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.81K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 12,309.32 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 12.31K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 76.52 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.08K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 50,088.24 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 50.09K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 12.32 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.01K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 34.35 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.03K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2317.30` | 81,784.24 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 81.78K USD at 2317.3000 USD [API] | `2026-10-29 10:14:21` |
| `ANNOUNCEMENT` | `INFO` | `2317.30` | 67,469.12 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 67.47K USD at 2317.3000 USD [API] | `2026-10-29 10:14:21` |
| `ANNOUNCEMENT` | `INFO` | `2296.60` | 65.68 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.07K USD at 2296.6000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `2296.60` | 31,280.61 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 31.28K USD at 2296.6000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 407.52 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.41K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 171.01 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.17K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 413.73 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.41K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 191.01 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.19K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 23.21 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 841.25 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.84K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 6,367.30 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 6.37K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 111.48 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.11K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 122.28 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.12K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 140.21 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.14K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 621.28 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.62K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 30.57 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.03K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 1,627.80 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.63K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 2,332.06 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.33K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 61.14 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.06K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 11.72 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.01K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 29.88 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.03K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 123.45 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.12K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 24,696.02 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 24.70K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 25,605.64 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 25.61K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 70,134.15 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 70.13K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 245.29 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.25K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 11,537.50 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 11.54K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 24.46 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 30,133.18 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 30.13K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 244.59 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.24K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 70,479.82 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 70.48K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 13,103.83 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 13.10K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2381.50` | 2,944.96 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 2.94K USD at 2381.5000 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `2381.50` | 49.77 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.05K USD at 2381.5000 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `2381.50` | 1,188.84 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.19K USD at 2381.5000 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `2381.10` | 143.34 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.14K USD at 2381.1000 USD [API] | `2026-10-28 20:01:02` |
| `ANNOUNCEMENT` | `INFO` | `2381.10` | 51.91 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.05K USD at 2381.1000 USD [API] | `2026-10-28 20:01:02` |
| `ANNOUNCEMENT` | `INFO` | `2381.10` | 356.69 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.36K USD at 2381.1000 USD [API] | `2026-10-28 20:01:02` |
| `ANNOUNCEMENT` | `INFO` | `2377.80` | 15,458.79 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 15.46K USD at 2377.8000 USD [API] | `2026-10-28 20:00:18` |
| `ANNOUNCEMENT` | `INFO` | `2377.80` | 104,644.60 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 104.64K USD at 2377.8000 USD [API] | `2026-10-28 20:00:18` |
| `ANNOUNCEMENT` | `INFO` | `2318.80` | 154,404.02 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 154.40K USD at 2318.8000 USD [API] | `2026-10-29 10:26:53` |
| `ANNOUNCEMENT` | `INFO` | `2323.90` | 66,792.84 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 66.79K USD at 2323.9000 USD [API] | `2026-10-29 10:39:31` |
| `ANNOUNCEMENT` | `INFO` | `2323.00` | 106,844.06 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 106.84K USD at 2323.0000 USD [API] | `2026-10-29 10:44:22` |
| `ANNOUNCEMENT` | `INFO` | `2324.50` | 1,412.13 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.41K USD at 2324.5000 USD [API] | `2026-10-29 10:45:49` |
| `ANNOUNCEMENT` | `INFO` | `2325.00` | 69,594.92 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 69.59K USD at 2325.0000 USD [API] | `2026-10-29 11:36:03` |
| `ANNOUNCEMENT` | `INFO` | `2325.00` | 99,895.72 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 99.90K USD at 2325.0000 USD [API] | `2026-10-29 11:36:03` |
| `ANNOUNCEMENT` | `INFO` | `2325.00` | 63,009.36 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 63.01K USD at 2325.0000 USD [API] | `2026-10-29 11:36:03` |
| `ANNOUNCEMENT` | `INFO` | `2325.90` | 70,001.45 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 70.00K USD at 2325.9000 USD [API] | `2026-10-29 11:53:41` |
| `ANNOUNCEMENT` | `INFO` | `2322.00` | 41,043.44 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 41.04K USD at 2322.0000 USD [API] | `2026-10-29 12:27:06` |
| `ANNOUNCEMENT` | `INFO` | `2322.60` | 40,051.38 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.05K USD at 2322.6000 USD [API] | `2026-10-29 12:52:25` |
| `ANNOUNCEMENT` | `INFO` | `2316.70` | 73,303.86 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 73.30K USD at 2316.7000 USD [API] | `2026-10-29 13:39:20` |
| `ANNOUNCEMENT` | `INFO` | `2514.40` | 294.44 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.29K USD at 2514.4000 USD [API] | `2026-09-14 23:37:58` |
| `ANNOUNCEMENT` | `INFO` | `2357.20` | 29,188.03 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 29.19K USD at 2357.2000 USD [API] | `2026-10-29 16:29:53` |
| `ANNOUNCEMENT` | `INFO` | `2429.60` | 82,377.29 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 82.38K USD at 2429.6000 USD [API] | `2026-10-08 15:56:54` |
| `ANNOUNCEMENT` | `INFO` | `2441.60` | 20,695.98 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 20.70K USD at 2441.6000 USD [API] | `2026-10-08 15:35:34` |
| `ANNOUNCEMENT` | `INFO` | `2453.30` | 5,820.21 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 5.82K USD at 2453.3000 USD [API] | `2026-10-08 15:34:56` |
| `ANNOUNCEMENT` | `INFO` | `2453.30` | 431.78 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.43K USD at 2453.3000 USD [API] | `2026-10-08 15:34:56` |
| `ANNOUNCEMENT` | `INFO` | `2453.30` | 1,497.74 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.50K USD at 2453.3000 USD [API] | `2026-10-08 15:34:56` |
| `ANNOUNCEMENT` | `INFO` | `2453.40` | 18,244.95 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 18.24K USD at 2453.4000 USD [API] | `2026-10-08 15:34:56` |
| `ANNOUNCEMENT` | `INFO` | `2478.30` | 6,609.38 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 6.61K USD at 2478.3000 USD [API] | `2026-10-08 15:20:45` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2275.30` (Vol: 35,200,000.00 USD, Dist: `+2.28%`) | Long MP=`2174.37` (Vol: 35,800,000.00 USD, Dist: `--2.25%`)
  * 48H Horizon: Short MP=`2270.12` (Vol: 33,600,000.00 USD, Dist: `+2.05%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--2.27%`)
  * 3D Horizon: Short MP=`2270.12` (Vol: 33,600,000.00 USD, Dist: `+2.05%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--2.27%`)
  * 7D Horizon: Short MP=`2401.80` (Vol: 50,700,000.00 USD, Dist: `+7.97%`) | Long MP=`2175.27` (Vol: 44,800,000.00 USD, Dist: `--2.21%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `445.00` | 41,360.00 USD | 790,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `455.00` | 60,900.00 USD | 790,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `465.00` | 67,840.00 USD | 790,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 2,360.00 USD | 790,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 1,520.00 USD | 790,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 112,860.00 USD | 790,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 1,810,000.00 USD | 790,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 187,930.00 USD | 788,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 38,890.00 USD | 788,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 13,170.00 USD | 788,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 50,920.00 USD | 788,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 54,970.00 USD | 788,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 142,380.00 USD | 788,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 76,910.00 USD | 788,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 28,140.00 USD | 788,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 2,260,000.00 USD | 788,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 3,130,000.00 USD | 785,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 27,520.00 USD | 782,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 1,040,000.00 USD | 782,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 24,300.00 USD | 781,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 240,790.00 USD | 781,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 89,020.00 USD | 781,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 18,990.00 USD | 781,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 117,890.00 USD | 781,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 35,230.00 USD | 781,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 41,100.00 USD | 781,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 1,200.00 USD | 781,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 29,860.00 USD | 781,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 458,180.00 USD | 781,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 57,510.00 USD | 780,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 681,760.00 USD | 780,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 80,370.00 USD | 779,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 71,910.00 USD | 779,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 12,170.00 USD | 779,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 21,030.00 USD | 779,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 72,450.00 USD | 779,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 24,700.00 USD | 779,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 88,450.00 USD | 779,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 126,790.00 USD | 779,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 58,450.00 USD | 779,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 537,240.00 USD | 779,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 49,220.00 USD | 778,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 77,430.00 USD | 778,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 64,490.00 USD | 778,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 2,480,000.00 USD | 778,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 175,800.00 USD | 776,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 97,060.00 USD | 776,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 631,470.00 USD | 775,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 403,040.00 USD | 775,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 37,320.00 USD | 774,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 50,530.00 USD | 774,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 37,250.00 USD | 774,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 1,130,000.00 USD | 774,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 284,510.00 USD | 773,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 396,560.00 USD | 773,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 131,720.00 USD | 772,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 26,870.00 USD | 772,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 152,990.00 USD | 772,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 78,740.00 USD | 772,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 20,800.00 USD | 772,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 472,760.00 USD | 772,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 7,710,000.00 USD | 772,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 621,550.00 USD | 764,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 2,230,000.00 USD | 763,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 360,780.00 USD | 761,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 403,250.00 USD | 761,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 158,750.00 USD | 760,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 277,530.00 USD | 760,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 8,020,000.00 USD | 760,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 143,520.00 USD | 752,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 821,960.00 USD | 752,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 570,210.00 USD | 751,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 7,910,000.00 USD | 750,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 1,550,000.00 USD | 742,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 902,780.00 USD | 741,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 333,510.00 USD | 740,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 204,340.00 USD | 740,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 409,170.00 USD | 739,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 432,120.00 USD | 739,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 168,290.00 USD | 739,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 2,620,000.00 USD | 738,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 420,820.00 USD | 736,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 388,390.00 USD | 735,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 15,580,000.00 USD | 735,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 264,450.00 USD | 719,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 576,590.00 USD | 719,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 208,950.00 USD | 719,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 154,430.00 USD | 718,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 3,280,000.00 USD | 718,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 347,920.00 USD | 715,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 1,440,000.00 USD | 715,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 5,550,000.00 USD | 713,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 1,260,000.00 USD | 708,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 8,890,000.00 USD | 706,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 2,110,000.00 USD | 697,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 606,080.00 USD | 695,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 10,000,000.00 USD | 695,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 570,410.00 USD | 685,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 13,190,000.00 USD | 684,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 1,150,000.00 USD | 671,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 98,390.00 USD | 670,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 406,230.00 USD | 670,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 12,870,000.00 USD | 669,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 20,280,000.00 USD | 656,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 268,120.00 USD | 636,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 289,110.00 USD | 636,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 430,380.00 USD | 636,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 2,620,000.00 USD | 635,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 18,590,000.00 USD | 632,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 1,630,000.00 USD | 614,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 18,280,000.00 USD | 612,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 2,590,000.00 USD | 594,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 865,240.00 USD | 591,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 1,210,000.00 USD | 591,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 765,690.00 USD | 589,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 1,820,000.00 USD | 589,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 18,010,000.00 USD | 587,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 279,300.00 USD | 569,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 1,500,000.00 USD | 568,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 18,720,000.00 USD | 567,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 37,010,000.00 USD | 548,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 989,550.00 USD | 511,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 12,280,000.00 USD | 510,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 4,560,000.00 USD | 498,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 1,120,000.00 USD | 493,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 322,170.00 USD | 492,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 1,180,000.00 USD | 492,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 17,800,000.00 USD | 491,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 35,810,000.00 USD | 473,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 1,410,000.00 USD | 437,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 5,350,000.00 USD | 436,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 392,750.00 USD | 430,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 4,190,000.00 USD | 430,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 28,960,000.00 USD | 426,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 54,520,000.00 USD | 397,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 7,580,000.00 USD | 342,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 1,490,000.00 USD | 335,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 5,540,000.00 USD | 333,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 1,270,000.00 USD | 328,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 988,340.00 USD | 326,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 16,240,000.00 USD | 325,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 12,840,000.00 USD | 309,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 1,250,000.00 USD | 296,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 10,250,000.00 USD | 295,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 5,350,000.00 USD | 285,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 636,770.00 USD | 280,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 1,340,000.00 USD | 279,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 17,670,000.00 USD | 278,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 16,410,000.00 USD | 260,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 13,940,000.00 USD | 243,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 1,990,000.00 USD | 230,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 1,800,000.00 USD | 228,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 1,680,000.00 USD | 226,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1971.80` | 726,620,000.00 USD | 726,620,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1974.70` | 726,490,000.00 USD | 726,490,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,950,000.00 USD | 224,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1977.60` | 726,440,000.00 USD | 726,440,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1983.40` | 724,200,000.00 USD | 724,200,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1985.00` | 8,110,000.00 USD | 222,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1986.30` | 723,990,000.00 USD | 723,990,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1989.20` | 720,260,000.00 USD | 720,260,000.00 USD | 0.00 USD | 3,100,000.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1992.10` | 717,130,000.00 USD | 717,130,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1995.00` | 715,740,000.00 USD | 715,740,000.00 USD | 1,340,000.00 USD | 0.00 USD | 808,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1995.00` | 1,720,000.00 USD | 214,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1998.10` | 595,580,000.00 USD | 595,580,000.00 USD | 219,590.00 USD | 92,480.00 USD | 319,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2000.60` | 594,950,000.00 USD | 594,950,000.00 USD | 13,780.00 USD | 236,510.00 USD | 586,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2003.10` | 594,110,000.00 USD | 594,110,000.00 USD | 379,460.00 USD | 601,340.00 USD | 308,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2003.70` | 713,590,000.00 USD | 713,590,000.00 USD | 0.00 USD | 699,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2005.00` | 12,670,000.00 USD | 212,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2005.60` | 592,820,000.00 USD | 592,820,000.00 USD | 493,990.00 USD | 13,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2006.60` | 712,890,000.00 USD | 712,890,000.00 USD | 807,770.00 USD | 42,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2008.10` | 592,310,000.00 USD | 592,310,000.00 USD | 0.00 USD | 570,100.00 USD | 126,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2010.60` | 591,620,000.00 USD | 591,620,000.00 USD | 484,920.00 USD | 478,500.00 USD | 366,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2012.40` | 712,040,000.00 USD | 712,040,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2013.10` | 590,290,000.00 USD | 590,290,000.00 USD | 348,720.00 USD | 270,490.00 USD | 21,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2015.00` | 5,010,000.00 USD | 200,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2015.60` | 589,650,000.00 USD | 589,650,000.00 USD | 330,880.00 USD | 605,010.00 USD | 197,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2018.10` | 588,510,000.00 USD | 588,510,000.00 USD | 537,580.00 USD | 885,870.00 USD | 550,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2018.20` | 711,080,000.00 USD | 711,080,000.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2020.60` | 586,540,000.00 USD | 586,540,000.00 USD | 911,610.00 USD | 1,280,000.00 USD | 837,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2023.10` | 583,510,000.00 USD | 583,510,000.00 USD | 792,850.00 USD | 271,500.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2024.00` | 711,060,000.00 USD | 711,060,000.00 USD | 1,070,000.00 USD | 0.00 USD | 934,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,440,000.00 USD | 195,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2025.60` | 581,010,000.00 USD | 581,010,000.00 USD | 414,330.00 USD | 1,100,000.00 USD | 231,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2026.90` | 709,060,000.00 USD | 709,060,000.00 USD | 1,100,000.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2028.10` | 579,260,000.00 USD | 579,260,000.00 USD | 2,770,000.00 USD | 978,910.00 USD | 615,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2029.80` | 707,780,000.00 USD | 707,780,000.00 USD | 0.00 USD | 3,320,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2030.60` | 574,900,000.00 USD | 574,900,000.00 USD | 525,130.00 USD | 366,120.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2032.70` | 703,380,000.00 USD | 703,380,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2033.10` | 572,950,000.00 USD | 572,950,000.00 USD | 1,090,000.00 USD | 1,490,000.00 USD | 298,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 423,740.00 USD | 193,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2035.60` | 570,070,000.00 USD | 570,070,000.00 USD | 985,830.00 USD | 19,490.00 USD | 165,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2035.60` | 701,820,000.00 USD | 701,820,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2038.10` | 568,900,000.00 USD | 568,900,000.00 USD | 603,980.00 USD | 458,110.00 USD | 388,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.50` | 701,490,000.00 USD | 701,490,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2040.60` | 567,450,000.00 USD | 567,450,000.00 USD | 962,230.00 USD | 178,560.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2043.10` | 566,280,000.00 USD | 566,280,000.00 USD | 0.00 USD | 0.00 USD | 174,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2044.30` | 700,030,000.00 USD | 700,030,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 6,640,000.00 USD | 193,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2045.60` | 566,110,000.00 USD | 566,110,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2048.10` | 566,080,000.00 USD | 566,080,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2050.10` | 699,740,000.00 USD | 699,740,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.60` | 565,260,000.00 USD | 565,260,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2053.00` | 699,510,000.00 USD | 699,510,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2053.10` | 564,150,000.00 USD | 564,150,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 3,920,000.00 USD | 186,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2055.60` | 564,120,000.00 USD | 564,120,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2058.10` | 563,790,000.00 USD | 563,790,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2058.80` | 697,230,000.00 USD | 697,230,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.70` | 696,880,000.00 USD | 696,880,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2063.10` | 563,030,000.00 USD | 563,030,000.00 USD | 0.00 USD | 111,540.00 USD | 530,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.60` | 691,630,000.00 USD | 691,630,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 15,310,000.00 USD | 182,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2065.60` | 562,390,000.00 USD | 562,390,000.00 USD | 950,540.00 USD | 485,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2067.50` | 689,160,000.00 USD | 689,160,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2068.10` | 560,960,000.00 USD | 560,960,000.00 USD | 0.00 USD | 304,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2070.40` | 687,520,000.00 USD | 687,520,000.00 USD | 3,600,000.00 USD | 2,730,000.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2070.60` | 560,650,000.00 USD | 560,650,000.00 USD | 105,210.00 USD | 319,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.10` | 560,230,000.00 USD | 560,230,000.00 USD | 0.00 USD | 555,250.00 USD | 420,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2073.30` | 679,320,000.00 USD | 679,320,000.00 USD | 3,200,000.00 USD | 2,180,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 2,710,000.00 USD | 167,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2075.60` | 559,250,000.00 USD | 559,250,000.00 USD | 379,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2076.20` | 672,250,000.00 USD | 672,250,000.00 USD | 4,520,000.00 USD | 5,030,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2078.10` | 558,870,000.00 USD | 558,870,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2079.10` | 658,690,000.00 USD | 658,690,000.00 USD | 3,560,000.00 USD | 3,000,000.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2080.60` | 558,850,000.00 USD | 558,850,000.00 USD | 77,960.00 USD | 29,610.00 USD | 199,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2082.00` | 650,070,000.00 USD | 650,070,000.00 USD | 4,050,000.00 USD | 1,860,000.00 USD | 2,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2083.10` | 558,540,000.00 USD | 558,540,000.00 USD | 827,940.00 USD | 4,240.00 USD | 211,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.90` | 641,700,000.00 USD | 641,700,000.00 USD | 3,070,000.00 USD | 1,460,000.00 USD | 4,380,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 13,760,000.00 USD | 164,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2085.60` | 557,500,000.00 USD | 557,500,000.00 USD | 691,080.00 USD | 249,220.00 USD | 817,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2087.80` | 632,790,000.00 USD | 632,790,000.00 USD | 3,310,000.00 USD | 2,260,000.00 USD | 924,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2088.10` | 555,740,000.00 USD | 555,740,000.00 USD | 525,540.00 USD | 343,300.00 USD | 442,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2090.60` | 554,430,000.00 USD | 554,430,000.00 USD | 761,770.00 USD | 224,660.00 USD | 446,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2090.70` | 626,300,000.00 USD | 626,300,000.00 USD | 4,340,000.00 USD | 952,210.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2093.10` | 552,990,000.00 USD | 552,990,000.00 USD | 752,390.00 USD | 334,060.00 USD | 673,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2093.60` | 614,030,000.00 USD | 614,030,000.00 USD | 3,930,000.00 USD | 1,640,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,710,000.00 USD | 150,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2095.60` | 551,230,000.00 USD | 551,230,000.00 USD | 1,840,000.00 USD | 1,130,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2096.50` | 605,510,000.00 USD | 605,510,000.00 USD | 3,210,000.00 USD | 1,980,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2098.10` | 546,960,000.00 USD | 546,960,000.00 USD | 345,860.00 USD | 488,160.00 USD | 309,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2099.40` | 599,030,000.00 USD | 599,030,000.00 USD | 2,320,000.00 USD | 3,020,000.00 USD | 2,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2100.60` | 545,820,000.00 USD | 545,820,000.00 USD | 137,320.00 USD | 1,030,000.00 USD | 231,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2102.30` | 591,620,000.00 USD | 591,620,000.00 USD | 125,250.00 USD | 739,480.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2103.10` | 544,420,000.00 USD | 544,420,000.00 USD | 315,200.00 USD | 119,690.00 USD | 306,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 2,380,000.00 USD | 149,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2105.20` | 588,750,000.00 USD | 588,750,000.00 USD | 2,000,000.00 USD | 1,250,000.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2105.60` | 543,680,000.00 USD | 543,680,000.00 USD | 3,610,000.00 USD | 1,160,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2108.10` | 537,830,000.00 USD | 537,830,000.00 USD | 656,240.00 USD | 9,120.00 USD | 96,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2108.10` | 583,100,000.00 USD | 583,100,000.00 USD | 8,000,000.00 USD | 930,280.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.60` | 537,070,000.00 USD | 537,070,000.00 USD | 36,110.00 USD | 22,440.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2111.00` | 572,530,000.00 USD | 572,530,000.00 USD | 3,450,000.00 USD | 1,780,000.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2113.10` | 537,000,000.00 USD | 537,000,000.00 USD | 866,490.00 USD | 506,690.00 USD | 244,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2113.90` | 565,140,000.00 USD | 565,140,000.00 USD | 1,080,000.00 USD | 1,810,000.00 USD | 3,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,330,000.00 USD | 146,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2115.60` | 535,380,000.00 USD | 535,380,000.00 USD | 722,960.00 USD | 400,200.00 USD | 939,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2116.80` | 558,870,000.00 USD | 558,870,000.00 USD | 2,360,000.00 USD | 2,350,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2118.10` | 533,320,000.00 USD | 533,320,000.00 USD | 4,580,000.00 USD | 3,940,000.00 USD | 302,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2119.70` | 552,180,000.00 USD | 552,180,000.00 USD | 12,310,000.00 USD | 5,090,000.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.60` | 524,500,000.00 USD | 524,500,000.00 USD | 5,670,000.00 USD | 1,980,000.00 USD | 671,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2122.60` | 532,200,000.00 USD | 532,200,000.00 USD | 4,890,000.00 USD | 4,260,000.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.10` | 516,180,000.00 USD | 516,180,000.00 USD | 5,450,000.00 USD | 2,370,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,770,000.00 USD | 145,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2125.50` | 521,070,000.00 USD | 521,070,000.00 USD | 6,630,000.00 USD | 7,840,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2125.60` | 505,220,000.00 USD | 505,220,000.00 USD | 5,170,000.00 USD | 3,160,000.00 USD | 837,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.10` | 496,050,000.00 USD | 496,050,000.00 USD | 3,180,000.00 USD | 2,480,000.00 USD | 745,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2128.40` | 504,160,000.00 USD | 504,160,000.00 USD | 4,290,000.00 USD | 1,960,000.00 USD | 3,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2130.60` | 489,630,000.00 USD | 489,630,000.00 USD | 1,250,000.00 USD | 18,610.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2131.30` | 493,930,000.00 USD | 493,930,000.00 USD | 1,980,000.00 USD | 1,850,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2133.10` | 487,260,000.00 USD | 487,260,000.00 USD | 95,260.00 USD | 255,590.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.20` | 488,740,000.00 USD | 488,740,000.00 USD | 2,270,000.00 USD | 577,880.00 USD | 308,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 2,100,000.00 USD | 21,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2135.60` | 485,380,000.00 USD | 485,380,000.00 USD | 1,460,000.00 USD | 2,490,000.00 USD | 771,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.10` | 485,590,000.00 USD | 485,590,000.00 USD | 792,450.00 USD | 2,590,000.00 USD | 633,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2138.10` | 480,650,000.00 USD | 480,650,000.00 USD | 84,550.00 USD | 1,090,000.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.00` | 481,570,000.00 USD | 481,570,000.00 USD | 3,470,000.00 USD | 1,700,000.00 USD | 635,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2140.60` | 479,420,000.00 USD | 479,420,000.00 USD | 1,530,000.00 USD | 898,980.00 USD | 317,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2142.90` | 475,760,000.00 USD | 475,760,000.00 USD | 1,960,000.00 USD | 804,740.00 USD | 434,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2143.10` | 476,670,000.00 USD | 476,670,000.00 USD | 1,080,000.00 USD | 3,170,000.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 1,020,000.00 USD | 19,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2145.60` | 471,250,000.00 USD | 471,250,000.00 USD | 3,170,000.00 USD | 2,360,000.00 USD | 615,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2145.80` | 472,560,000.00 USD | 472,560,000.00 USD | 2,160,000.00 USD | 1,460,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2148.10` | 465,110,000.00 USD | 465,110,000.00 USD | 728,710.00 USD | 2,080,000.00 USD | 69,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2148.70` | 467,210,000.00 USD | 467,210,000.00 USD | 26,270.00 USD | 538,910.00 USD | 399,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2150.60` | 462,230,000.00 USD | 462,230,000.00 USD | 7,990,000.00 USD | 1,820,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2151.60` | 466,250,000.00 USD | 466,250,000.00 USD | 11,200,000.00 USD | 363,770.00 USD | 107,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2153.10` | 449,770,000.00 USD | 449,770,000.00 USD | 2,300,000.00 USD | 3,300,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.50` | 454,580,000.00 USD | 454,580,000.00 USD | 48,150.00 USD | 2,020,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,970,000.00 USD | 18,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2155.60` | 441,930,000.00 USD | 441,930,000.00 USD | 4,060,000.00 USD | 3,710,000.00 USD | 3,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2157.40` | 450,930,000.00 USD | 450,930,000.00 USD | 6,950,000.00 USD | 1,330,000.00 USD | 5,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2158.10` | 431,130,000.00 USD | 431,130,000.00 USD | 2,480,000.00 USD | 1,730,000.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.30` | 437,600,000.00 USD | 437,600,000.00 USD | 309,460.00 USD | 767,490.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2160.60` | 423,880,000.00 USD | 423,880,000.00 USD | 4,790,000.00 USD | 6,270,000.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2163.10` | 409,890,000.00 USD | 409,890,000.00 USD | 18,720,000.00 USD | 10,400,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.20` | 434,690,000.00 USD | 434,690,000.00 USD | 26,080,000.00 USD | 10,840,000.00 USD | 87,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 6,050,000.00 USD | 15,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2165.60` | 377,960,000.00 USD | 377,960,000.00 USD | 12,300,000.00 USD | 11,850,000.00 USD | 4,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2166.10` | 397,680,000.00 USD | 397,680,000.00 USD | 885,200.00 USD | 14,900,000.00 USD | 2,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2168.10` | 349,600,000.00 USD | 349,600,000.00 USD | 15,930,000.00 USD | 6,950,000.00 USD | 5,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2169.00` | 379,040,000.00 USD | 379,040,000.00 USD | 12,770,000.00 USD | 14,280,000.00 USD | 3,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.60` | 321,590,000.00 USD | 321,590,000.00 USD | 24,230,000.00 USD | 8,680,000.00 USD | 7,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2171.90` | 348,220,000.00 USD | 348,220,000.00 USD | 2,110,000.00 USD | 1,650,000.00 USD | 5,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2173.10` | 280,780,000.00 USD | 280,780,000.00 USD | 6,820,000.00 USD | 3,860,000.00 USD | 3,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2174.80` | 338,890,000.00 USD | 338,890,000.00 USD | 34,840,000.00 USD | 1,330,000.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 6,220,000.00 USD | 9,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.60` | 266,300,000.00 USD | 266,300,000.00 USD | 3,680,000.00 USD | 511,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2177.70` | 298,890,000.00 USD | 298,890,000.00 USD | 196,330.00 USD | 267,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2178.10` | 262,120,000.00 USD | 262,120,000.00 USD | 1,290,000.00 USD | 94,350.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2180.60` | 257,410,000.00 USD | 257,410,000.00 USD | 3,270,000.00 USD | 4,110,000.00 USD | 5,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2180.60` | 298,430,000.00 USD | 298,430,000.00 USD | 0.00 USD | 0.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2183.10` | 244,440,000.00 USD | 244,440,000.00 USD | 637,950.00 USD | 1,320,000.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2183.50` | 297,250,000.00 USD | 297,250,000.00 USD | 1,760,000.00 USD | 3,680,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 661,930.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2185.60` | 241,230,000.00 USD | 241,230,000.00 USD | 2,650,000.00 USD | 2,480,000.00 USD | 4,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2186.40` | 287,860,000.00 USD | 287,860,000.00 USD | 41,350,000.00 USD | 18,930,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2188.10` | 231,370,000.00 USD | 231,370,000.00 USD | 7,340,000.00 USD | 4,820,000.00 USD | 7,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2189.30` | 227,580,000.00 USD | 227,580,000.00 USD | 14,800,000.00 USD | 13,670,000.00 USD | 8,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2190.60` | 211,280,000.00 USD | 211,280,000.00 USD | 6,880,000.00 USD | 3,890,000.00 USD | 4,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2192.20` | 191,100,000.00 USD | 191,100,000.00 USD | 0.00 USD | 21,640,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2193.10` | 196,400,000.00 USD | 196,400,000.00 USD | 6,010,000.00 USD | 6,260,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 2,240,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2195.10` | 169,460,000.00 USD | 169,460,000.00 USD | 141,070.00 USD | 243,760.00 USD | 8,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2195.60` | 182,690,000.00 USD | 182,690,000.00 USD | 8,230,000.00 USD | 1,230,000.00 USD | 5,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2198.00` | 160,950,000.00 USD | 160,950,000.00 USD | 242,610.00 USD | 1,460,000.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2198.10` | 167,590,000.00 USD | 167,590,000.00 USD | 1,110,000.00 USD | 3,160,000.00 USD | 5,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.60` | 158,270,000.00 USD | 158,270,000.00 USD | 9,250,000.00 USD | 5,850,000.00 USD | 11,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.90` | 157,110,000.00 USD | 157,110,000.00 USD | 4,700,000.00 USD | 266,430.00 USD | 8,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.10` | 131,210,000.00 USD | 131,210,000.00 USD | 8,650,000.00 USD | 11,510,000.00 USD | 7,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.80` | 143,450,000.00 USD | 143,450,000.00 USD | 5,350,000.00 USD | 4,330,000.00 USD | 12,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 455,190.00 USD | 455,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.60` | 103,980,000.00 USD | 103,980,000.00 USD | 11,830,000.00 USD | 1,530,000.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2206.70` | 121,380,000.00 USD | 121,380,000.00 USD | 15,070,000.00 USD | 3,390,000.00 USD | 5,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2208.10` | 88,240,000.00 USD | 88,240,000.00 USD | 8,730,000.00 USD | 6,100,000.00 USD | 3,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2209.60` | 97,830,000.00 USD | 97,830,000.00 USD | 4,550,000.00 USD | 0.00 USD | 9,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.60` | 69,710,000.00 USD | 69,710,000.00 USD | 6,870,000.00 USD | 7,030,000.00 USD | 4,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2212.50` | 84,120,000.00 USD | 84,120,000.00 USD | 6,450,000.00 USD | 1,980,000.00 USD | 11,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2213.10` | 51,150,000.00 USD | 51,150,000.00 USD | 9,690,000.00 USD | 6,160,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 412.88 USD | 412.88 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2215.40` | 64,690,000.00 USD | 64,690,000.00 USD | 0.00 USD | 0.00 USD | 565,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2215.60` | 33,310,000.00 USD | 33,310,000.00 USD | 968,510.00 USD | 2,730,000.00 USD | 736,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2218.10` | 28,880,000.00 USD | 28,880,000.00 USD | 6,820,000.00 USD | 3,040,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2218.30` | 64,130,000.00 USD | 64,130,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2220.60` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 3,570,000.00 USD | 4,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2221.20` | 41,240,000.00 USD | 41,240,000.00 USD | 0.00 USD | 11,780,000.00 USD | 18,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2223.10` | 7,720,000.00 USD | 7,720,000.00 USD | 0.00 USD | 2,150,000.00 USD | 5,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2224.10` | 11,220,000.00 USD | 11,220,000.00 USD | 8,610,000.00 USD | 446,880.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2225.00` | 778.75 USD | 778.75 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2225.60` | 1,660,000.00 USD | 1,660,000.00 USD | 374,450.00 USD | 1,140,000.00 USD | 147,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2227.00` | 8,230,000.00 USD | 8,230,000.00 USD | 524,820.00 USD | 0.00 USD | 7,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2228.10` | 27,020,000.00 USD | 27,020,000.00 USD | 2,770,000.00 USD | 17,080,000.00 USD | 5,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2229.90` | 29,250,000.00 USD | 29,250,000.00 USD | 1,940,000.00 USD | 0.00 USD | 19,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2230.60` | 67,690,000.00 USD | 67,690,000.00 USD | 40,330,000.00 USD | 0.00 USD | 344,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2232.80` | 30,210,000.00 USD | 30,210,000.00 USD | 0.00 USD | 0.00 USD | 959,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2233.10` | 67,960,000.00 USD | 67,960,000.00 USD | 89,990.00 USD | 0.00 USD | 180,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2235.00` | 2,120.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2235.70` | 55,460,000.00 USD | 55,460,000.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 350,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2238.10` | 79,920,000.00 USD | 79,920,000.00 USD | 11,960,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2238.60` | 69,520,000.00 USD | 69,520,000.00 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2240.60` | 83,180,000.00 USD | 83,180,000.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2241.50` | 101,890,000.00 USD | 101,890,000.00 USD | 32,370,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2243.10` | 83,950,000.00 USD | 83,950,000.00 USD | 271,140.00 USD | 452,920.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2244.40` | 104,290,000.00 USD | 104,290,000.00 USD | 1,860,000.00 USD | 535,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2245.60` | 92,740,000.00 USD | 92,740,000.00 USD | 3,390,000.00 USD | 4,370,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2247.30` | 110,470,000.00 USD | 110,470,000.00 USD | 1,670,000.00 USD | 1,030,000.00 USD | 3,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2248.10` | 101,900,000.00 USD | 101,900,000.00 USD | 2,560,000.00 USD | 3,510,000.00 USD | 3,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2250.20` | 121,280,000.00 USD | 121,280,000.00 USD | 3,160,000.00 USD | 7,420,000.00 USD | 228,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2250.60` | 108,860,000.00 USD | 108,860,000.00 USD | 6,430,000.00 USD | 475,410.00 USD | 55,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2253.10` | 114,720,000.00 USD | 114,720,000.00 USD | 943,690.00 USD | 3,480,000.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2253.10` | 143,340,000.00 USD | 143,340,000.00 USD | 10,600,000.00 USD | 11,240,000.00 USD | 216,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 20,070.00 USD | 22,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2255.60` | 146,550,000.00 USD | 146,550,000.00 USD | 16,490,000.00 USD | 6,560,000.00 USD | 8,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2256.00` | 178,870,000.00 USD | 178,870,000.00 USD | 17,810,000.00 USD | 10,520,000.00 USD | 7,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2258.10` | 175,540,000.00 USD | 175,540,000.00 USD | 18,480,000.00 USD | 7,740,000.00 USD | 2,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2258.90` | 203,150,000.00 USD | 203,150,000.00 USD | 11,860,000.00 USD | 8,380,000.00 USD | 4,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2260.60` | 196,990,000.00 USD | 196,990,000.00 USD | 9,590,000.00 USD | 9,340,000.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2261.80` | 211,600,000.00 USD | 211,600,000.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 280,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2263.10` | 229,550,000.00 USD | 229,550,000.00 USD | 14,130,000.00 USD | 10,400,000.00 USD | 8,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2264.70` | 214,330,000.00 USD | 214,330,000.00 USD | 0.00 USD | 2,510,000.00 USD | 218,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 13,280.00 USD | 36,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2265.60` | 252,640,000.00 USD | 252,640,000.00 USD | 3,490,000.00 USD | 9,120,000.00 USD | 10,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2267.60` | 226,640,000.00 USD | 226,640,000.00 USD | 196,330.00 USD | 5,790,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2268.10` | 298,000,000.00 USD | 298,000,000.00 USD | 19,910,000.00 USD | 11,870,000.00 USD | 13,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2270.50` | 275,830,000.00 USD | 275,830,000.00 USD | 26,480,000.00 USD | 3,500,000.00 USD | 19,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2270.60` | 326,950,000.00 USD | 326,950,000.00 USD | 7,630,000.00 USD | 9,260,000.00 USD | 12,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2273.10` | 351,660,000.00 USD | 351,660,000.00 USD | 14,930,000.00 USD | 5,280,000.00 USD | 4,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2273.40` | 279,440,000.00 USD | 279,440,000.00 USD | 373,530.00 USD | 362,150.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 1,610,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2275.60` | 408,680,000.00 USD | 408,680,000.00 USD | 33,630,000.00 USD | 17,390,000.00 USD | 6,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2276.30` | 310,270,000.00 USD | 310,270,000.00 USD | 24,150,000.00 USD | 6,680,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2278.10` | 437,070,000.00 USD | 437,070,000.00 USD | 4,240,000.00 USD | 10,420,000.00 USD | 13,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2279.20` | 352,090,000.00 USD | 352,090,000.00 USD | 3,230,000.00 USD | 24,610,000.00 USD | 13,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2280.60` | 492,350,000.00 USD | 492,350,000.00 USD | 31,330,000.00 USD | 16,100,000.00 USD | 7,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.10` | 435,140,000.00 USD | 435,140,000.00 USD | 0.00 USD | 69,380,000.00 USD | 13,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2283.10` | 549,200,000.00 USD | 549,200,000.00 USD | 26,480,000.00 USD | 20,540,000.00 USD | 9,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2285.00` | 471,740,000.00 USD | 471,740,000.00 USD | 6,610,000.00 USD | 29,850,000.00 USD | 140,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 183,890.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2285.60` | 574,720,000.00 USD | 574,720,000.00 USD | 7,480,000.00 USD | 12,460,000.00 USD | 5,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2287.90` | 498,490,000.00 USD | 498,490,000.00 USD | 8,380,000.00 USD | 6,500,000.00 USD | 11,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2288.10` | 598,270,000.00 USD | 598,270,000.00 USD | 11,850,000.00 USD | 4,100,000.00 USD | 7,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2290.60` | 640,110,000.00 USD | 640,110,000.00 USD | 18,820,000.00 USD | 15,090,000.00 USD | 7,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2290.80` | 511,690,000.00 USD | 511,690,000.00 USD | 4,310,000.00 USD | 3,340,000.00 USD | 5,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2293.10` | 668,750,000.00 USD | 668,750,000.00 USD | 14,100,000.00 USD | 5,110,000.00 USD | 9,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2293.70` | 529,040,000.00 USD | 529,040,000.00 USD | 8,930,000.00 USD | 0.00 USD | 8,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 3,010,000.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2295.60` | 699,580,000.00 USD | 699,580,000.00 USD | 10,130,000.00 USD | 13,170,000.00 USD | 7,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2296.60` | 584,710,000.00 USD | 584,710,000.00 USD | 28,890,000.00 USD | 9,570,000.00 USD | 17,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2298.10` | 754,870,000.00 USD | 754,870,000.00 USD | 32,970,000.00 USD | 15,200,000.00 USD | 7,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.50` | 630,090,000.00 USD | 630,090,000.00 USD | 18,930,000.00 USD | 20,670,000.00 USD | 5,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2300.60` | 787,960,000.00 USD | 787,960,000.00 USD | 8,900,000.00 USD | 10,180,000.00 USD | 14,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.40` | 685,030,000.00 USD | 685,030,000.00 USD | 26,960,000.00 USD | 11,130,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2303.10` | 818,890,000.00 USD | 818,890,000.00 USD | 17,940,000.00 USD | 5,770,000.00 USD | 7,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 670,610.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2305.30` | 709,190,000.00 USD | 709,190,000.00 USD | 6,340,000.00 USD | 6,960,000.00 USD | 10,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2305.60` | 853,920,000.00 USD | 853,920,000.00 USD | 12,190,000.00 USD | 15,330,000.00 USD | 7,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2308.10` | 863,640,000.00 USD | 863,640,000.00 USD | 4,390,000.00 USD | 3,450,000.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2308.20` | 713,350,000.00 USD | 713,350,000.00 USD | 1,240,000.00 USD | 2,780,000.00 USD | 134,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2310.60` | 882,360,000.00 USD | 882,360,000.00 USD | 5,990,000.00 USD | 2,140,000.00 USD | 10,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2311.10` | 743,840,000.00 USD | 743,840,000.00 USD | 11,560,000.00 USD | 2,790,000.00 USD | 16,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2313.10` | 899,160,000.00 USD | 899,160,000.00 USD | 6,090,000.00 USD | 8,970,000.00 USD | 1,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2314.00` | 752,080,000.00 USD | 752,080,000.00 USD | 0.00 USD | 7,460,000.00 USD | 778,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 5,890,000.00 USD | 11,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2315.60` | 931,740,000.00 USD | 931,740,000.00 USD | 9,820,000.00 USD | 15,740,000.00 USD | 7,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2316.90` | 760,550,000.00 USD | 760,550,000.00 USD | 1,020,000.00 USD | 6,410,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2318.10` | 946,570,000.00 USD | 946,570,000.00 USD | 5,910,000.00 USD | 6,680,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.80` | 787,050,000.00 USD | 787,050,000.00 USD | 5,530,000.00 USD | 13,080,000.00 USD | 7,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.60` | 966,780,000.00 USD | 966,780,000.00 USD | 5,860,000.00 USD | 11,510,000.00 USD | 2,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.70` | 799,910,000.00 USD | 799,910,000.00 USD | 5,850,000.00 USD | 5,180,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2323.10` | 987,880,000.00 USD | 987,880,000.00 USD | 4,360,000.00 USD | 12,060,000.00 USD | 4,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,780,000.00 USD | 13,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2325.60` | 998,240,000.00 USD | 998,240,000.00 USD | 2,050,000.00 USD | 6,790,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2325.60` | 815,940,000.00 USD | 815,940,000.00 USD | 6,590,000.00 USD | 1,040,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2328.10` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 1,250,000.00 USD | 1,240,000.00 USD | 4,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.50` | 828,190,000.00 USD | 828,190,000.00 USD | 3,860,000.00 USD | 363,770.00 USD | 8,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2330.60` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 11,680,000.00 USD | 3,110,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2331.40` | 851,870,000.00 USD | 851,870,000.00 USD | 23,030,000.00 USD | 593,900.00 USD | 54,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2333.10` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 2,710,000.00 USD | 3,760,000.00 USD | 8,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2334.30` | 895,910,000.00 USD | 895,910,000.00 USD | 16,820,000.00 USD | 15,180,000.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 427,950.00 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2335.60` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 13,920,000.00 USD | 3,880,000.00 USD | 5,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2337.20` | 934,100,000.00 USD | 934,100,000.00 USD | 28,890,000.00 USD | 4,650,000.00 USD | 4,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2338.10` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 6,320,000.00 USD | 1,830,000.00 USD | 5,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2340.10` | 974,710,000.00 USD | 974,710,000.00 USD | 10,400,000.00 USD | 10,610,000.00 USD | 19,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2340.60` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 10,960,000.00 USD | 5,840,000.00 USD | 9,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2343.00` | 995,730,000.00 USD | 995,730,000.00 USD | 5,030,000.00 USD | 12,160,000.00 USD | 3,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2343.10` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 10,420,000.00 USD | 8,840,000.00 USD | 3,740,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 417,120.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2345.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 3,680,000.00 USD | 3,280,000.00 USD | 8,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2345.90` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 1,350,000.00 USD | 16,220,000.00 USD | 15,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2348.10` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 4,920,000.00 USD | 4,640,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.80` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 1,060,000.00 USD | 9,500,000.00 USD | 20,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 25,880,000.00 USD | 6,920,000.00 USD | 10,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2351.70` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 2,430,000.00 USD | 19,600,000.00 USD | 10,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2353.10` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 3,960,000.00 USD | 2,550,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2354.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 10,390,000.00 USD | 34,750,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,790,000.00 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2355.60` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 3,840,000.00 USD | 3,430,000.00 USD | 951,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2357.50` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 13,850,000.00 USD | 7,240,000.00 USD | 6,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2358.10` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 4,740,000.00 USD | 4,470,000.00 USD | 5,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2360.40` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 4,470,000.00 USD | 3,430,000.00 USD | 254,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.60` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 9,930,000.00 USD | 3,880,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2363.10` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 5,580,000.00 USD | 9,200,000.00 USD | 7,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2363.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 4,570,000.00 USD | 373,740.00 USD | 6,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 5,520,000.00 USD | 21,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2365.60` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 4,890,000.00 USD | 1,170,000.00 USD | 3,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2366.20` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 4,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2368.10` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 4,190,000.00 USD | 3,330,000.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2369.10` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 21,280,000.00 USD | 475,460.00 USD | 4,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.60` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 13,960,000.00 USD | 5,840,000.00 USD | 5,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2372.00` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 15,540,000.00 USD | 0.00 USD | 51,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2373.10` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 12,450,000.00 USD | 2,600,000.00 USD | 6,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2374.90` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 885,750.00 USD | 22,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2375.60` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 7,590,000.00 USD | 1,830,000.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2377.80` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 11,180,000.00 USD | 6,190,000.00 USD | 18,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.10` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 1,650,000.00 USD | 1,990,000.00 USD | 5,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.60` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 6,120,000.00 USD | 6,700,000.00 USD | 5,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2380.70` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 4,420,000.00 USD | 2,590,000.00 USD | 19,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.10` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 15,730,000.00 USD | 9,480,000.00 USD | 10,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2383.60` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 8,840,000.00 USD | 17,490,000.00 USD | 35,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 726,570.00 USD | 22,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.60` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 7,510,000.00 USD | 10,450,000.00 USD | 3,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2386.50` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 17,480,000.00 USD | 37,880,000.00 USD | 38,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2388.10` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 12,620,000.00 USD | 5,690,000.00 USD | 4,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2389.40` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 6,030,000.00 USD | 35,920,000.00 USD | 31,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.60` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 1,700,000.00 USD | 5,130,000.00 USD | 52,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2392.30` | 1,720,000,000.00 USD | 1,720,000,000.00 USD | 26,840,000.00 USD | 45,530,000.00 USD | 39,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2393.10` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 2,570,000.00 USD | 2,220,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,840,000.00 USD | 27,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2395.20` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 41,200,000.00 USD | 24,950,000.00 USD | 29,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2395.60` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 2,120,000.00 USD | 1,450,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.10` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 1,210,000.00 USD | 3,720,000.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2398.10` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 35,750,000.00 USD | 38,130,000.00 USD | 23,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2400.60` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 944,200.00 USD | 637,690.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.00` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 40,240,000.00 USD | 25,000,000.00 USD | 25,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2403.10` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 1,200,000.00 USD | 467,060.00 USD | 564,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2403.90` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 57,170,000.00 USD | 25,580,000.00 USD | 30,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 156,110.00 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2405.60` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 7,730,000.00 USD | 3,300,000.00 USD | 5,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2406.80` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 25,430,000.00 USD | 33,580,000.00 USD | 16,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2408.10` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 5,840,000.00 USD | 3,520,000.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2409.70` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 27,030,000.00 USD | 27,370,000.00 USD | 25,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.60` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 4,650,000.00 USD | 4,210,000.00 USD | 4,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2412.60` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 16,670,000.00 USD | 15,260,000.00 USD | 15,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.10` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 5,150,000.00 USD | 3,250,000.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 143,210.00 USD | 28,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2415.50` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 23,150,000.00 USD | 19,800,000.00 USD | 26,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2415.60` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 2,990,000.00 USD | 2,210,000.00 USD | 3,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2418.10` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 2,660,000.00 USD | 2,070,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.40` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 27,090,000.00 USD | 11,140,000.00 USD | 17,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2420.60` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 6,490,000.00 USD | 4,150,000.00 USD | 4,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.30` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 21,290,000.00 USD | 20,900,000.00 USD | 12,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2423.10` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 770,750.00 USD | 1,540,000.00 USD | 3,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.20` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 19,140,000.00 USD | 18,390,000.00 USD | 23,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 243,520.00 USD | 28,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.60` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 1,280,000.00 USD | 694,550.00 USD | 11,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.10` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 18,590,000.00 USD | 9,810,000.00 USD | 13,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.10` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 1,610,000.00 USD | 1,450,000.00 USD | 738,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2430.00` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 7,100,000.00 USD | 14,510,000.00 USD | 7,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 1,330,000.00 USD | 2,120,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2432.90` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 16,380,000.00 USD | 5,350,000.00 USD | 5,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2433.10` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 3,570,000.00 USD | 2,130,000.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 187,830.00 USD | 28,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.60` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 1,920,000.00 USD | 623,860.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2435.80` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 6,050,000.00 USD | 3,000,000.00 USD | 5,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2438.10` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 1,050,000.00 USD | 517,090.00 USD | 15,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2438.70` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 10,300,000.00 USD | 9,480,000.00 USD | 6,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.60` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 1,230,000.00 USD | 1,190,000.00 USD | 858,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.60` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 9,610,000.00 USD | 3,820,000.00 USD | 8,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2443.10` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 1,060,000.00 USD | 31,110.00 USD | 747,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.50` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 7,520,000.00 USD | 10,650,000.00 USD | 8,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 135,670.00 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.60` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 234,410.00 USD | 703,990.00 USD | 755,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.40` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 11,080,000.00 USD | 3,020,000.00 USD | 12,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2448.10` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 938,360.00 USD | 888,690.00 USD | 995,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2450.30` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 8,460,000.00 USD | 6,720,000.00 USD | 10,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.60` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 1,860,000.00 USD | 69,580.00 USD | 371,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2453.10` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 2,000,000.00 USD | 2,000,000.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2453.20` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 7,290,000.00 USD | 3,760,000.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 5,180,000.00 USD | 33,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 2,260,000.00 USD | 1,970,000.00 USD | 489,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2456.10` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 5,780,000.00 USD | 5,730,000.00 USD | 6,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2458.10` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 1,180,000.00 USD | 1,850,000.00 USD | 674,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2459.00` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 5,530,000.00 USD | 6,340,000.00 USD | 6,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2460.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 1,530,000.00 USD | 1,390,000.00 USD | 388,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2461.90` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 5,190,000.00 USD | 6,700,000.00 USD | 6,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2463.10` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 330,880.00 USD | 618,870.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.80` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 6,130,000.00 USD | 2,500,000.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 67,480,000.00 USD | 101,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2465.60` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 537,580.00 USD | 1,100,000.00 USD | 339,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.70` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 3,400,000.00 USD | 2,500,000.00 USD | 45,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2468.10` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 326,370.00 USD | 1,950,000.00 USD | 377,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.60` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 1,380,000.00 USD | 475,680.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.60` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 3,960,000.00 USD | 2,050,000.00 USD | 522,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2473.10` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 92,950.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2473.50` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 5,300,000.00 USD | 2,920,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 197,560.00 USD | 101,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2475.60` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 339,190.00 USD | 1,100,000.00 USD | 103,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2476.40` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 232,420.00 USD | 0.00 USD | 156,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2476.40` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 2,070,000.00 USD | 2,410,000.00 USD | 872,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2479.30` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 3,070,000.00 USD | 4,940,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2482.20` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 601,420.00 USD | 2,170,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 52,650.00 USD | 101,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2485.10` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2488.00` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.90` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 2,180,000.00 USD | 301,010.00 USD | 137,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.80` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 1,200,000.00 USD | 733,870.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 2,220,000.00 USD | 103,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2496.70` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 773,650.00 USD | 812,060.00 USD | 4,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2499.60` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 752,070.00 USD | 92,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2502.50` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 55,050.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 4,470,000.00 USD | 108,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2505.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2508.30` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 1,520,000.00 USD | 109,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2525.00` | 198,500.00 USD | 109,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2535.00` | 907,780.00 USD | 110,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2545.00` | 5,090,000.00 USD | 115,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2555.00` | 273,390.00 USD | 116,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2565.00` | 146,840.00 USD | 116,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2575.00` | 98,920.00 USD | 116,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2585.00` | 27,070,000.00 USD | 143,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2595.00` | 8,170,000.00 USD | 151,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2605.00` | 5,820,000.00 USD | 157,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2615.00` | 326,670.00 USD | 157,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2625.00` | 45,390,000.00 USD | 203,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2635.00` | 1,580,000.00 USD | 204,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 638,950.00 USD | 205,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 26,680,000.00 USD | 232,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 456,980.00 USD | 232,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 4,380,000.00 USD | 237,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 120,480.00 USD | 237,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 83,170.00 USD | 237,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 5,940,000.00 USD | 243,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 296,820.00 USD | 243,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 315,000.00 USD | 243,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 188,530.00 USD | 243,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 739,840.00 USD | 244,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 18,300,000.00 USD | 262,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 25,510,000.00 USD | 288,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 534,220.00 USD | 289,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 5,530,000.00 USD | 294,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 24,130.00 USD | 294,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 5,290,000.00 USD | 299,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 2,530,000.00 USD | 302,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 115,850.00 USD | 302,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 6,000,000.00 USD | 308,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 453,890.00 USD | 308,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 524,990.00 USD | 309,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 35,400.00 USD | 309,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 64,880.00 USD | 309,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 2,050,000.00 USD | 311,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 405,610.00 USD | 312,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 15,730,000.00 USD | 327,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 2,420,000.00 USD | 330,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 15,390.00 USD | 330,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 48,280.00 USD | 330,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 402,540.00 USD | 330,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 232,250.00 USD | 330,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 5,170,000.00 USD | 336,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 212,550.00 USD | 336,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 1,030,000.00 USD | 337,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 1,610,000.00 USD | 338,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 526,020.00 USD | 339,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 436,400.00 USD | 339,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 884,050.00 USD | 340,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 14,540,000.00 USD | 355,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 19,380.00 USD | 355,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 2,450,000.00 USD | 357,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 17,500.00 USD | 357,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 21,130.00 USD | 357,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 5,460,000.00 USD | 363,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 17,470,000.00 USD | 380,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 16,930,000.00 USD | 397,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 1,780,000.00 USD | 399,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 29,290,000.00 USD | 428,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 209,490.00 USD | 428,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 691,720.00 USD | 429,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 37,010,000.00 USD | 466,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 157,220.00 USD | 466,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 918,150.00 USD | 467,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 70,770,000.00 USD | 538,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 3,650,000.00 USD | 542,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 129,060.00 USD | 542,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 176,300.00 USD | 542,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 8,270,000.00 USD | 550,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 9,750,000.00 USD | 560,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 171,870.00 USD | 560,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 4,750,000.00 USD | 565,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 2,200,000.00 USD | 567,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 8,450,000.00 USD | 576,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 296,110.00 USD | 576,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 102,300.00 USD | 576,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 1,190,000.00 USD | 577,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 714,800.00 USD | 578,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 2,940,000.00 USD | 581,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 233,210.00 USD | 581,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 504,080.00 USD | 582,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 1,060,000.00 USD | 583,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 1,670,000.00 USD | 584,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 1,900,000.00 USD | 586,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 101,820.00 USD | 586,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 3,210,000.00 USD | 590,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 4,730,000.00 USD | 594,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 39,630.00 USD | 594,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 14,870,000.00 USD | 609,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 193,830.00 USD | 609,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 661,810.00 USD | 610,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 569,080.00 USD | 611,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 799,730.00 USD | 611,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 268,290.00 USD | 612,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 214,060.00 USD | 612,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 1,530,000.00 USD | 613,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 925,810.00 USD | 614,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 673,280.00 USD | 615,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 97,210.00 USD | 615,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 14,540,000.00 USD | 630,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 13,710.00 USD | 630,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 705,630.00 USD | 630,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 71,060.00 USD | 630,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 80,920.00 USD | 631,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 749,070.00 USD | 631,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 103,870.00 USD | 631,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 54,800,000.00 USD | 686,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 3,760,000.00 USD | 690,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 1,120,000.00 USD | 691,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 8,740,000.00 USD | 700,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 22,760.00 USD | 700,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 22,630.00 USD | 700,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 6,820,000.00 USD | 707,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 4,750.00 USD | 707,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 207,200.00 USD | 707,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 42,780.00 USD | 707,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 3,950.00 USD | 707,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 315,680.00 USD | 707,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 234,460.00 USD | 707,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 448,050.00 USD | 708,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 5,330,000.00 USD | 713,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 1,960,000.00 USD | 715,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 394,330,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 275,200.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 7,380,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 57,450,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 3,240.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 2,960.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 97,310.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 289,260.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 1,990,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 1,130,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 473,710.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3875.00` | 93,650.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 39,800,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 46,120.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 516,720.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 740,390.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 147,220.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 2,040,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 4,310.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 67,490.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 6,960.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 236,270.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 80,870.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 1,260,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 975,110.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 483,440.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 65,250.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 396,110.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 7,590.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 1,690,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 283,580.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 1,530,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 58,190.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 5,620.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 26,460.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 58,200.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 487,770.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 95,470.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 1,010,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 62,880.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 123,920.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 242,040.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 859,990.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 32,590,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 774,870.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 42,320.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4225.00` | 84,890,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 61,210.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 18,700.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 59,020.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 682,840.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 14,040.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 1,520.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 13,140.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 3,990,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 285,720.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 236,730.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 22,710.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 6,750.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 1,010,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 699,700.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 456,580.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 9,790.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 335,480.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 40,260.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 145,290.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4435.00` | 34,160.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4445.00` | 394,410.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `445.00` | 790,910,000.00 USD | 0.00 USD | 41,360.00 USD | `-79.98%` | `92.95` |
| `Live` | `Long` | `455.00` | 790,870,000.00 USD | 0.00 USD | 60,900.00 USD | `-79.53%` | `133.85` |
| `Live` | `Long` | `465.00` | 790,810,000.00 USD | 0.00 USD | 67,840.00 USD | `-79.08%` | `145.88` |
| `Live` | `Long` | `475.00` | 790,740,000.00 USD | 0.00 USD | 2,360.00 USD | `-78.63%` | `4.96` |
| `Live` | `Long` | `485.00` | 790,740,000.00 USD | 0.00 USD | 1,520.00 USD | `-78.18%` | `3.14` |
| `Live` | `Long` | `495.00` | 790,740,000.00 USD | 0.00 USD | 112,860.00 USD | `-77.73%` | `227.99` |
| `Live` | `Long` | `505.00` | 790,620,000.00 USD | 0.00 USD | 1,810,000.00 USD | `-77.28%` | `3,592.88` |
| `Live` | `Long` | `515.00` | 788,810,000.00 USD | 0.00 USD | 187,930.00 USD | `-76.83%` | `364.91` |
| `Live` | `Long` | `525.00` | 788,620,000.00 USD | 0.00 USD | 38,890.00 USD | `-76.38%` | `74.08` |
| `Live` | `Long` | `535.00` | 788,580,000.00 USD | 0.00 USD | 13,170.00 USD | `-75.93%` | `24.62` |
| `Live` | `Long` | `545.00` | 788,570,000.00 USD | 0.00 USD | 50,920.00 USD | `-75.48%` | `93.43` |
| `Live` | `Long` | `555.00` | 788,520,000.00 USD | 0.00 USD | 54,970.00 USD | `-75.03%` | `99.04` |
| `Live` | `Long` | `565.00` | 788,460,000.00 USD | 0.00 USD | 142,380.00 USD | `-74.58%` | `252.00` |
| `Live` | `Long` | `575.00` | 788,320,000.00 USD | 0.00 USD | 76,910.00 USD | `-74.13%` | `133.76` |
| `Live` | `Long` | `585.00` | 788,240,000.00 USD | 0.00 USD | 28,140.00 USD | `-73.68%` | `48.11` |
| `Live` | `Long` | `595.00` | 788,220,000.00 USD | 0.00 USD | 2,260,000.00 USD | `-73.23%` | `3,796.57` |
| `Live` | `Long` | `605.00` | 785,960,000.00 USD | 0.00 USD | 3,130,000.00 USD | `-72.78%` | `5,167.63` |
| `Live` | `Long` | `615.00` | 782,830,000.00 USD | 0.00 USD | 27,520.00 USD | `-72.33%` | `44.74` |
| `Live` | `Long` | `625.00` | 782,800,000.00 USD | 0.00 USD | 1,040,000.00 USD | `-71.88%` | `1,669.51` |
| `Live` | `Long` | `635.00` | 781,760,000.00 USD | 0.00 USD | 24,300.00 USD | `-71.43%` | `38.27` |
| `Live` | `Long` | `645.00` | 781,730,000.00 USD | 0.00 USD | 240,790.00 USD | `-70.98%` | `373.31` |
| `Live` | `Long` | `655.00` | 781,490,000.00 USD | 0.00 USD | 89,020.00 USD | `-70.53%` | `135.90` |
| `Live` | `Long` | `665.00` | 781,410,000.00 USD | 0.00 USD | 18,990.00 USD | `-70.08%` | `28.55` |
| `Live` | `Long` | `675.00` | 781,390,000.00 USD | 0.00 USD | 117,890.00 USD | `-69.63%` | `174.65` |
| `Live` | `Long` | `685.00` | 781,270,000.00 USD | 0.00 USD | 35,230.00 USD | `-69.18%` | `51.43` |
| `Live` | `Long` | `695.00` | 781,230,000.00 USD | 0.00 USD | 41,100.00 USD | `-68.73%` | `59.13` |
| `Live` | `Long` | `705.00` | 781,190,000.00 USD | 0.00 USD | 1,200.00 USD | `-68.28%` | `1.70` |
| `Live` | `Long` | `715.00` | 781,190,000.00 USD | 0.00 USD | 29,860.00 USD | `-67.83%` | `41.76` |
| `Live` | `Long` | `725.00` | 781,160,000.00 USD | 0.00 USD | 458,180.00 USD | `-67.38%` | `631.98` |
| `Live` | `Long` | `735.00` | 780,700,000.00 USD | 0.00 USD | 57,510.00 USD | `-66.93%` | `78.24` |
| `Live` | `Long` | `745.00` | 780,650,000.00 USD | 0.00 USD | 681,760.00 USD | `-66.48%` | `915.12` |
| `Live` | `Long` | `755.00` | 779,960,000.00 USD | 0.00 USD | 80,370.00 USD | `-66.03%` | `106.45` |
| `Live` | `Long` | `765.00` | 779,880,000.00 USD | 0.00 USD | 71,910.00 USD | `-65.58%` | `94.00` |
| `Live` | `Long` | `775.00` | 779,810,000.00 USD | 0.00 USD | 12,170.00 USD | `-65.13%` | `15.70` |
| `Live` | `Long` | `785.00` | 779,800,000.00 USD | 0.00 USD | 21,030.00 USD | `-64.68%` | `26.79` |
| `Live` | `Long` | `795.00` | 779,780,000.00 USD | 0.00 USD | 72,450.00 USD | `-64.23%` | `91.13` |
| `Live` | `Long` | `805.00` | 779,710,000.00 USD | 0.00 USD | 24,700.00 USD | `-63.78%` | `30.69` |
| `Live` | `Long` | `815.00` | 779,680,000.00 USD | 0.00 USD | 88,450.00 USD | `-63.33%` | `108.52` |
| `Live` | `Long` | `825.00` | 779,590,000.00 USD | 0.00 USD | 126,790.00 USD | `-62.88%` | `153.68` |
| `Live` | `Long` | `835.00` | 779,470,000.00 USD | 0.00 USD | 58,450.00 USD | `-62.43%` | `70.00` |
| `Live` | `Long` | `845.00` | 779,410,000.00 USD | 0.00 USD | 537,240.00 USD | `-61.98%` | `635.79` |
| `Live` | `Long` | `855.00` | 778,870,000.00 USD | 0.00 USD | 49,220.00 USD | `-61.53%` | `57.57` |
| `Live` | `Long` | `865.00` | 778,820,000.00 USD | 0.00 USD | 77,430.00 USD | `-61.08%` | `89.52` |
| `Live` | `Long` | `875.00` | 778,740,000.00 USD | 0.00 USD | 64,490.00 USD | `-60.63%` | `73.70` |
| `Live` | `Long` | `885.00` | 778,680,000.00 USD | 0.00 USD | 2,480,000.00 USD | `-60.18%` | `2,796.91` |
| `Live` | `Long` | `895.00` | 776,200,000.00 USD | 0.00 USD | 175,800.00 USD | `-59.73%` | `196.43` |
| `Live` | `Long` | `905.00` | 776,030,000.00 USD | 0.00 USD | 97,060.00 USD | `-59.28%` | `107.24` |
| `Live` | `Long` | `915.00` | 775,930,000.00 USD | 0.00 USD | 631,470.00 USD | `-58.83%` | `690.13` |
| `Live` | `Long` | `925.00` | 775,300,000.00 USD | 0.00 USD | 403,040.00 USD | `-58.38%` | `435.72` |
| `Live` | `Long` | `935.00` | 774,900,000.00 USD | 0.00 USD | 37,320.00 USD | `-57.93%` | `39.92` |
| `Live` | `Long` | `945.00` | 774,860,000.00 USD | 0.00 USD | 50,530.00 USD | `-57.48%` | `53.48` |
| `Live` | `Long` | `955.00` | 774,810,000.00 USD | 0.00 USD | 37,250.00 USD | `-57.04%` | `39.00` |
| `Live` | `Long` | `965.00` | 774,770,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-56.59%` | `1,169.40` |
| `Live` | `Long` | `975.00` | 773,640,000.00 USD | 0.00 USD | 284,510.00 USD | `-56.14%` | `291.80` |
| `Live` | `Long` | `985.00` | 773,360,000.00 USD | 0.00 USD | 396,560.00 USD | `-55.69%` | `402.60` |
| `Live` | `Long` | `995.00` | 772,960,000.00 USD | 0.00 USD | 131,720.00 USD | `-55.24%` | `132.38` |
| `Live` | `Long` | `1005.00` | 772,830,000.00 USD | 0.00 USD | 26,870.00 USD | `-54.79%` | `26.73` |
| `Live` | `Long` | `1015.00` | 772,800,000.00 USD | 0.00 USD | 152,990.00 USD | `-54.34%` | `150.73` |
| `Live` | `Long` | `1025.00` | 772,650,000.00 USD | 0.00 USD | 78,740.00 USD | `-53.89%` | `76.82` |
| `Live` | `Long` | `1035.00` | 772,570,000.00 USD | 0.00 USD | 20,800.00 USD | `-53.44%` | `20.09` |
| `Live` | `Long` | `1045.00` | 772,550,000.00 USD | 0.00 USD | 472,760.00 USD | `-52.99%` | `452.41` |
| `Live` | `Long` | `1055.00` | 772,080,000.00 USD | 0.00 USD | 7,710,000.00 USD | `-52.54%` | `7,308.85` |
| `Live` | `Long` | `1065.00` | 764,370,000.00 USD | 0.00 USD | 621,550.00 USD | `-52.09%` | `583.61` |
| `Live` | `Long` | `1075.00` | 763,750,000.00 USD | 0.00 USD | 2,230,000.00 USD | `-51.64%` | `2,076.74` |
| `Live` | `Long` | `1085.00` | 761,510,000.00 USD | 0.00 USD | 360,780.00 USD | `-51.19%` | `332.52` |
| `Live` | `Long` | `1095.00` | 761,150,000.00 USD | 0.00 USD | 403,250.00 USD | `-50.74%` | `368.26` |
| `Live` | `Long` | `1105.00` | 760,750,000.00 USD | 0.00 USD | 158,750.00 USD | `-50.29%` | `143.66` |
| `Live` | `Long` | `1115.00` | 760,590,000.00 USD | 0.00 USD | 277,530.00 USD | `-49.84%` | `248.91` |
| `Live` | `Long` | `1125.00` | 760,310,000.00 USD | 0.00 USD | 8,020,000.00 USD | `-49.39%` | `7,128.81` |
| `Live` | `Long` | `1135.00` | 752,290,000.00 USD | 0.00 USD | 143,520.00 USD | `-48.94%` | `126.45` |
| `Live` | `Long` | `1145.00` | 752,150,000.00 USD | 0.00 USD | 821,960.00 USD | `-48.49%` | `717.87` |
| `Live` | `Long` | `1155.00` | 751,330,000.00 USD | 0.00 USD | 570,210.00 USD | `-48.04%` | `493.68` |
| `Live` | `Long` | `1165.00` | 750,760,000.00 USD | 0.00 USD | 7,910,000.00 USD | `-47.59%` | `6,792.23` |
| `Live` | `Long` | `1175.00` | 742,840,000.00 USD | 0.00 USD | 1,550,000.00 USD | `-47.14%` | `1,315.93` |
| `Live` | `Long` | `1185.00` | 741,300,000.00 USD | 0.00 USD | 902,780.00 USD | `-46.69%` | `761.84` |
| `Live` | `Long` | `1195.00` | 740,390,000.00 USD | 0.00 USD | 333,510.00 USD | `-46.24%` | `279.08` |
| `Live` | `Long` | `1205.00` | 740,060,000.00 USD | 0.00 USD | 204,340.00 USD | `-45.79%` | `169.58` |
| `Live` | `Long` | `1215.00` | 739,860,000.00 USD | 0.00 USD | 409,170.00 USD | `-45.34%` | `336.76` |
| `Live` | `Long` | `1225.00` | 739,450,000.00 USD | 0.00 USD | 432,120.00 USD | `-44.89%` | `352.75` |
| `Live` | `Long` | `1235.00` | 739,020,000.00 USD | 0.00 USD | 168,290.00 USD | `-44.44%` | `136.27` |
| `Live` | `Long` | `1245.00` | 738,850,000.00 USD | 0.00 USD | 2,620,000.00 USD | `-43.99%` | `2,105.64` |
| `Live` | `Long` | `1255.00` | 736,230,000.00 USD | 0.00 USD | 420,820.00 USD | `-43.54%` | `335.31` |
| `Live` | `Long` | `1265.00` | 735,800,000.00 USD | 0.00 USD | 388,390.00 USD | `-43.09%` | `307.03` |
| `Live` | `Long` | `1275.00` | 735,420,000.00 USD | 0.00 USD | 15,580,000.00 USD | `-42.64%` | `12,216.46` |
| `Live` | `Long` | `1285.00` | 719,840,000.00 USD | 0.00 USD | 264,450.00 USD | `-42.19%` | `205.80` |
| `Live` | `Long` | `1295.00` | 719,580,000.00 USD | 0.00 USD | 576,590.00 USD | `-41.74%` | `445.24` |
| `Live` | `Long` | `1305.00` | 719,000,000.00 USD | 0.00 USD | 208,950.00 USD | `-41.29%` | `160.11` |
| `Live` | `Long` | `1315.00` | 718,790,000.00 USD | 0.00 USD | 154,430.00 USD | `-40.84%` | `117.44` |
| `Live` | `Long` | `1325.00` | 718,640,000.00 USD | 0.00 USD | 3,280,000.00 USD | `-40.39%` | `2,478.76` |
| `Live` | `Long` | `1335.00` | 715,350,000.00 USD | 0.00 USD | 347,920.00 USD | `-39.94%` | `260.62` |
| `Live` | `Long` | `1345.00` | 715,000,000.00 USD | 0.00 USD | 1,440,000.00 USD | `-39.49%` | `1,071.50` |
| `Live` | `Long` | `1355.00` | 713,560,000.00 USD | 0.00 USD | 5,550,000.00 USD | `-39.04%` | `4,095.49` |
| `Live` | `Long` | `1365.00` | 708,010,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-38.59%` | `923.84` |
| `Live` | `Long` | `1375.00` | 706,750,000.00 USD | 0.00 USD | 8,890,000.00 USD | `-38.14%` | `6,462.14` |
| `Live` | `Long` | `1385.00` | 697,870,000.00 USD | 0.00 USD | 2,110,000.00 USD | `-37.69%` | `1,523.24` |
| `Live` | `Long` | `1395.00` | 695,760,000.00 USD | 0.00 USD | 606,080.00 USD | `-37.24%` | `434.47` |
| `Live` | `Long` | `1405.00` | 695,150,000.00 USD | 0.00 USD | 10,000,000.00 USD | `-36.79%` | `7,114.46` |
| `Live` | `Long` | `1415.00` | 685,160,000.00 USD | 0.00 USD | 570,410.00 USD | `-36.34%` | `403.11` |
| `Live` | `Long` | `1425.00` | 684,580,000.00 USD | 0.00 USD | 13,190,000.00 USD | `-35.89%` | `9,254.84` |
| `Live` | `Long` | `1435.00` | 671,400,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-35.44%` | `803.47` |
| `Live` | `Long` | `1445.00` | 670,240,000.00 USD | 0.00 USD | 98,390.00 USD | `-34.99%` | `68.09` |
| `Live` | `Long` | `1455.00` | 670,150,000.00 USD | 0.00 USD | 406,230.00 USD | `-34.54%` | `279.19` |
| `Live` | `Long` | `1465.00` | 669,740,000.00 USD | 0.00 USD | 12,870,000.00 USD | `-34.09%` | `8,781.86` |
| `Live` | `Long` | `1475.00` | 656,870,000.00 USD | 0.00 USD | 20,280,000.00 USD | `-33.64%` | `13,748.74` |
| `Live` | `Long` | `1485.00` | 636,590,000.00 USD | 0.00 USD | 268,120.00 USD | `-33.19%` | `180.55` |
| `Live` | `Long` | `1495.00` | 636,330,000.00 USD | 0.00 USD | 289,110.00 USD | `-32.74%` | `193.39` |
| `Live` | `Long` | `1505.00` | 636,040,000.00 USD | 0.00 USD | 430,380.00 USD | `-32.29%` | `285.97` |
| `Live` | `Long` | `1515.00` | 635,610,000.00 USD | 0.00 USD | 2,620,000.00 USD | `-31.84%` | `1,726.72` |
| `Live` | `Long` | `1525.00` | 632,990,000.00 USD | 0.00 USD | 18,590,000.00 USD | `-31.39%` | `12,192.92` |
| `Live` | `Long` | `1535.00` | 614,400,000.00 USD | 0.00 USD | 1,630,000.00 USD | `-30.94%` | `1,063.25` |
| `Live` | `Long` | `1545.00` | 612,760,000.00 USD | 0.00 USD | 18,280,000.00 USD | `-30.49%` | `11,834.68` |
| `Live` | `Long` | `1555.00` | 594,480,000.00 USD | 0.00 USD | 2,590,000.00 USD | `-30.04%` | `1,665.99` |
| `Live` | `Long` | `1565.00` | 591,890,000.00 USD | 0.00 USD | 865,240.00 USD | `-29.59%` | `552.87` |
| `Live` | `Long` | `1575.00` | 591,020,000.00 USD | 0.00 USD | 1,210,000.00 USD | `-29.14%` | `769.55` |
| `Live` | `Long` | `1585.00` | 589,810,000.00 USD | 0.00 USD | 765,690.00 USD | `-28.69%` | `483.08` |
| `Live` | `Long` | `1595.00` | 589,050,000.00 USD | 0.00 USD | 1,820,000.00 USD | `-28.24%` | `1,142.58` |
| `Live` | `Long` | `1605.00` | 587,220,000.00 USD | 0.00 USD | 18,010,000.00 USD | `-27.79%` | `11,221.03` |
| `Live` | `Long` | `1615.00` | 569,210,000.00 USD | 0.00 USD | 279,300.00 USD | `-27.34%` | `172.94` |
| `Live` | `Long` | `1625.00` | 568,930,000.00 USD | 0.00 USD | 1,500,000.00 USD | `-26.89%` | `924.24` |
| `Live` | `Long` | `1635.00` | 567,430,000.00 USD | 0.00 USD | 18,720,000.00 USD | `-26.44%` | `11,451.10` |
| `Live` | `Long` | `1645.00` | 548,710,000.00 USD | 0.00 USD | 37,010,000.00 USD | `-25.99%` | `22,496.16` |
| `Live` | `Long` | `1655.00` | 511,700,000.00 USD | 0.00 USD | 989,550.00 USD | `-25.54%` | `597.91` |
| `Live` | `Long` | `1665.00` | 510,710,000.00 USD | 0.00 USD | 12,280,000.00 USD | `-25.09%` | `7,376.32` |
| `Live` | `Long` | `1675.00` | 498,430,000.00 USD | 0.00 USD | 4,560,000.00 USD | `-24.64%` | `2,721.40` |
| `Live` | `Long` | `1685.00` | 493,870,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-24.19%` | `661.73` |
| `Live` | `Long` | `1695.00` | 492,760,000.00 USD | 0.00 USD | 322,170.00 USD | `-23.74%` | `190.07` |
| `Live` | `Long` | `1705.00` | 492,440,000.00 USD | 0.00 USD | 1,180,000.00 USD | `-23.29%` | `692.02` |
| `Live` | `Long` | `1715.00` | 491,260,000.00 USD | 0.00 USD | 17,800,000.00 USD | `-22.84%` | `10,379.10` |
| `Live` | `Long` | `1725.00` | 473,460,000.00 USD | 0.00 USD | 35,810,000.00 USD | `-22.39%` | `20,761.47` |
| `Live` | `Long` | `1735.00` | 437,640,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-21.94%` | `811.90` |
| `Live` | `Long` | `1745.00` | 436,240,000.00 USD | 0.00 USD | 5,350,000.00 USD | `-21.49%` | `3,067.49` |
| `Live` | `Long` | `1755.00` | 430,880,000.00 USD | 0.00 USD | 392,750.00 USD | `-21.04%` | `223.79` |
| `Live` | `Long` | `1765.00` | 430,490,000.00 USD | 0.00 USD | 4,190,000.00 USD | `-20.59%` | `2,373.41` |
| `Live` | `Long` | `1775.00` | 426,300,000.00 USD | 0.00 USD | 28,960,000.00 USD | `-20.14%` | `16,314.59` |
| `Live` | `Long` | `1785.00` | 397,340,000.00 USD | 0.00 USD | 54,520,000.00 USD | `-19.69%` | `30,544.38` |
| `Live` | `Long` | `1795.00` | 342,820,000.00 USD | 0.00 USD | 7,580,000.00 USD | `-19.24%` | `4,223.28` |
| `Live` | `Long` | `1805.00` | 335,240,000.00 USD | 0.00 USD | 1,490,000.00 USD | `-18.79%` | `822.82` |
| `Live` | `Long` | `1815.00` | 333,750,000.00 USD | 0.00 USD | 5,540,000.00 USD | `-18.34%` | `3,052.62` |
| `Live` | `Long` | `1825.00` | 328,210,000.00 USD | 0.00 USD | 1,270,000.00 USD | `-17.89%` | `694.70` |
| `Live` | `Long` | `1835.00` | 326,950,000.00 USD | 0.00 USD | 988,340.00 USD | `-17.44%` | `538.61` |
| `Live` | `Long` | `1845.00` | 325,960,000.00 USD | 0.00 USD | 16,240,000.00 USD | `-16.99%` | `8,800.52` |
| `Live` | `Long` | `1855.00` | 309,720,000.00 USD | 0.00 USD | 12,840,000.00 USD | `-16.54%` | `6,921.29` |
| `Live` | `Long` | `1865.00` | 296,880,000.00 USD | 0.00 USD | 1,250,000.00 USD | `-16.09%` | `669.54` |
| `Live` | `Long` | `1875.00` | 295,630,000.00 USD | 0.00 USD | 10,250,000.00 USD | `-15.64%` | `5,464.07` |
| `Live` | `Long` | `1885.00` | 285,390,000.00 USD | 0.00 USD | 5,350,000.00 USD | `-15.19%` | `2,835.94` |
| `Live` | `Long` | `1895.00` | 280,040,000.00 USD | 0.00 USD | 636,770.00 USD | `-14.74%` | `336.03` |
| `Live` | `Long` | `1905.00` | 279,410,000.00 USD | 0.00 USD | 1,340,000.00 USD | `-14.29%` | `702.31` |
| `Live` | `Long` | `1915.00` | 278,070,000.00 USD | 0.00 USD | 17,670,000.00 USD | `-13.85%` | `9,229.33` |
| `Live` | `Long` | `1925.00` | 260,390,000.00 USD | 0.00 USD | 16,410,000.00 USD | `-13.40%` | `8,523.17` |
| `Live` | `Long` | `1935.00` | 243,990,000.00 USD | 0.00 USD | 13,940,000.00 USD | `-12.95%` | `7,203.45` |
| `Live` | `Long` | `1945.00` | 230,050,000.00 USD | 0.00 USD | 1,990,000.00 USD | `-12.50%` | `1,020.71` |
| `Live` | `Long` | `1955.00` | 228,060,000.00 USD | 0.00 USD | 1,800,000.00 USD | `-12.05%` | `920.75` |
| `Live` | `Long` | `1965.00` | 226,260,000.00 USD | 0.00 USD | 1,680,000.00 USD | `-11.60%` | `853.05` |
| `Live` | `Long` | `1975.00` | 224,590,000.00 USD | 0.00 USD | 1,950,000.00 USD | `-11.15%` | `986.56` |
| `Live` | `Long` | `1985.00` | 222,640,000.00 USD | 0.00 USD | 8,110,000.00 USD | `-10.70%` | `4,083.38` |
| `Live` | `Long` | `1995.00` | 214,530,000.00 USD | 0.00 USD | 1,720,000.00 USD | `-10.25%` | `863.07` |
| `Live` | `Long` | `2005.00` | 212,810,000.00 USD | 0.00 USD | 12,670,000.00 USD | `-9.80%` | `6,318.58` |
| `Live` | `Long` | `2015.00` | 200,140,000.00 USD | 0.00 USD | 5,010,000.00 USD | `-9.35%` | `2,486.63` |
| `Live` | `Long` | `2025.00` | 195,130,000.00 USD | 0.00 USD | 1,440,000.00 USD | `-8.90%` | `713.24` |
| `Live` | `Long` | `2035.00` | 193,690,000.00 USD | 0.00 USD | 423,740.00 USD | `-8.45%` | `208.23` |
| `Live` | `Long` | `2045.00` | 193,260,000.00 USD | 0.00 USD | 6,640,000.00 USD | `-8.00%` | `3,248.83` |
| `Live` | `Long` | `2055.00` | 186,620,000.00 USD | 0.00 USD | 3,920,000.00 USD | `-7.55%` | `1,908.19` |
| `Live` | `Long` | `2065.00` | 182,700,000.00 USD | 0.00 USD | 15,310,000.00 USD | `-7.10%` | `7,415.10` |
| `Live` | `Long` | `2075.00` | 167,390,000.00 USD | 0.00 USD | 2,710,000.00 USD | `-6.65%` | `1,304.62` |
| `Live` | `Long` | `2085.00` | 164,680,000.00 USD | 0.00 USD | 13,760,000.00 USD | `-6.20%` | `6,601.52` |
| `Live` | `Long` | `2095.00` | 150,910,000.00 USD | 0.00 USD | 1,710,000.00 USD | `-5.75%` | `816.16` |
| `Live` | `Long` | `2105.00` | 149,200,000.00 USD | 0.00 USD | 2,380,000.00 USD | `-5.30%` | `1,128.57` |
| `Live` | `Long` | `2115.00` | 146,830,000.00 USD | 0.00 USD | 1,330,000.00 USD | `-4.85%` | `631.08` |
| `Live` | `Long` | `2125.00` | 145,490,000.00 USD | 0.00 USD | 123,770,000.00 USD | `-4.40%` | `58,243.94` |
| `Live` | `Long` | `2135.00` | 21,730,000.00 USD | 0.00 USD | 2,100,000.00 USD | `-3.95%` | `983.24` |
| `Live` | `Long` | `2145.00` | 19,630,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-3.50%` | `476.52` |
| `Live` | `Long` | `2155.00` | 18,600,000.00 USD | 0.00 USD | 2,970,000.00 USD | `-3.05%` | `1,377.74` |
| `Live` | `Long` | `2165.00` | 15,640,000.00 USD | 0.00 USD | 6,050,000.00 USD | `-2.60%` | `2,796.38` |
| `Live` | `Long` | `2175.00` | 9,580,000.00 USD | 0.00 USD | 6,220,000.00 USD | `-2.15%` | `2,859.48` |
| `Live` | `Long` | `2185.00` | 3,360,000.00 USD | 0.00 USD | 661,930.00 USD | `-1.70%` | `302.94` |
| `Live` | `Long` | `2195.00` | 2,700,000.00 USD | 0.00 USD | 2,240,000.00 USD | `-1.25%` | `1,022.47` |
| `Live` | `Long` | `2205.00` | 455,600.00 USD | 0.00 USD | 455,190.00 USD | `-0.80%` | `206.43` |
| `Live` | `Long` | `2215.00` | 412.88 USD | 0.00 USD | 412.88 USD | `-0.35%` | `0.19` |
| `Live` | `Short` | `2225.00` | 778.75 USD | 778.75 USD | 0.00 USD | `+0.10%` | `0.35` |
| `Live` | `Short` | `2235.00` | 2,900.00 USD | 2,120.00 USD | 0.00 USD | `+0.55%` | `0.95` |
| `Live` | `Short` | `2255.00` | 22,970.00 USD | 20,070.00 USD | 0.00 USD | `+1.45%` | `8.90` |
| `Live` | `Short` | `2265.00` | 36,240.00 USD | 13,280.00 USD | 0.00 USD | `+1.90%` | `5.86` |
| `Live` | `Short` | `2275.00` | 1,650,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+2.35%` | `709.88` |
| `Live` | `Short` | `2285.00` | 1,840,000.00 USD | 183,890.00 USD | 0.00 USD | `+2.80%` | `80.48` |
| `Live` | `Short` | `2295.00` | 4,850,000.00 USD | 3,010,000.00 USD | 0.00 USD | `+3.25%` | `1,313.15` |
| `Live` | `Short` | `2305.00` | 5,520,000.00 USD | 670,610.00 USD | 0.00 USD | `+3.70%` | `290.94` |
| `Live` | `Short` | `2315.00` | 11,410,000.00 USD | 5,890,000.00 USD | 0.00 USD | `+4.15%` | `2,545.88` |
| `Live` | `Short` | `2325.00` | 13,190,000.00 USD | 1,780,000.00 USD | 0.00 USD | `+4.60%` | `765.30` |
| `Live` | `Short` | `2335.00` | 13,620,000.00 USD | 427,950.00 USD | 0.00 USD | `+5.05%` | `183.27` |
| `Live` | `Short` | `2345.00` | 14,040,000.00 USD | 417,120.00 USD | 0.00 USD | `+5.50%` | `177.88` |
| `Live` | `Short` | `2355.00` | 15,820,000.00 USD | 1,790,000.00 USD | 0.00 USD | `+5.95%` | `758.77` |
| `Live` | `Short` | `2365.00` | 21,340,000.00 USD | 5,520,000.00 USD | 0.00 USD | `+6.40%` | `2,333.69` |
| `Live` | `Short` | `2375.00` | 22,230,000.00 USD | 885,750.00 USD | 0.00 USD | `+6.85%` | `372.95` |
| `Live` | `Short` | `2385.00` | 22,960,000.00 USD | 726,570.00 USD | 0.00 USD | `+7.30%` | `304.64` |
| `Live` | `Short` | `2395.00` | 27,790,000.00 USD | 4,840,000.00 USD | 0.00 USD | `+7.75%` | `2,019.89` |
| `Live` | `Short` | `2405.00` | 27,950,000.00 USD | 156,110.00 USD | 0.00 USD | `+8.20%` | `64.91` |
| `Live` | `Short` | `2415.00` | 28,090,000.00 USD | 143,210.00 USD | 0.00 USD | `+8.65%` | `59.30` |
| `Live` | `Short` | `2425.00` | 28,340,000.00 USD | 243,520.00 USD | 0.00 USD | `+9.10%` | `100.42` |
| `Live` | `Short` | `2435.00` | 28,520,000.00 USD | 187,830.00 USD | 0.00 USD | `+9.55%` | `77.14` |
| `Live` | `Short` | `2445.00` | 28,660,000.00 USD | 135,670.00 USD | 0.00 USD | `+10.00%` | `55.49` |
| `Live` | `Short` | `2455.00` | 33,840,000.00 USD | 5,180,000.00 USD | 0.00 USD | `+10.45%` | `2,109.28` |
| `Live` | `Short` | `2465.00` | 101,310,000.00 USD | 67,480,000.00 USD | 0.00 USD | `+10.90%` | `27,373.71` |
| `Live` | `Short` | `2475.00` | 101,510,000.00 USD | 197,560.00 USD | 0.00 USD | `+11.35%` | `79.82` |
| `Live` | `Short` | `2485.00` | 101,560,000.00 USD | 52,650.00 USD | 0.00 USD | `+11.80%` | `21.19` |
| `Live` | `Short` | `2495.00` | 103,790,000.00 USD | 2,220,000.00 USD | 0.00 USD | `+12.25%` | `890.36` |
| `Live` | `Short` | `2505.00` | 108,260,000.00 USD | 4,470,000.00 USD | 0.00 USD | `+12.70%` | `1,784.79` |
| `Live` | `Short` | `2515.00` | 109,780,000.00 USD | 1,520,000.00 USD | 0.00 USD | `+13.15%` | `606.00` |
| `Live` | `Short` | `2525.00` | 109,980,000.00 USD | 198,500.00 USD | 0.00 USD | `+13.60%` | `78.61` |
| `Live` | `Short` | `2535.00` | 110,890,000.00 USD | 907,780.00 USD | 0.00 USD | `+14.05%` | `358.10` |
| `Live` | `Short` | `2545.00` | 115,970,000.00 USD | 5,090,000.00 USD | 0.00 USD | `+14.50%` | `1,998.11` |
| `Live` | `Short` | `2555.00` | 116,250,000.00 USD | 273,390.00 USD | 0.00 USD | `+14.95%` | `107.00` |
| `Live` | `Short` | `2565.00` | 116,390,000.00 USD | 146,840.00 USD | 0.00 USD | `+15.40%` | `57.25` |
| `Live` | `Short` | `2575.00` | 116,490,000.00 USD | 98,920.00 USD | 0.00 USD | `+15.85%` | `38.42` |
| `Live` | `Short` | `2585.00` | 143,560,000.00 USD | 27,070,000.00 USD | 0.00 USD | `+16.30%` | `10,472.53` |
| `Live` | `Short` | `2595.00` | 151,730,000.00 USD | 8,170,000.00 USD | 0.00 USD | `+16.75%` | `3,147.05` |
| `Live` | `Short` | `2605.00` | 157,550,000.00 USD | 5,820,000.00 USD | 0.00 USD | `+17.20%` | `2,234.18` |
| `Live` | `Short` | `2615.00` | 157,880,000.00 USD | 326,670.00 USD | 0.00 USD | `+17.65%` | `124.92` |
| `Live` | `Short` | `2625.00` | 203,270,000.00 USD | 45,390,000.00 USD | 0.00 USD | `+18.10%` | `17,292.58` |
| `Live` | `Short` | `2635.00` | 204,850,000.00 USD | 1,580,000.00 USD | 0.00 USD | `+18.55%` | `599.63` |
| `Live` | `Short` | `2645.00` | 205,490,000.00 USD | 638,950.00 USD | 0.00 USD | `+19.00%` | `241.57` |
| `Live` | `Short` | `2655.00` | 232,170,000.00 USD | 26,680,000.00 USD | 0.00 USD | `+19.45%` | `10,049.47` |
| `Live` | `Short` | `2665.00` | 232,630,000.00 USD | 456,980.00 USD | 0.00 USD | `+19.90%` | `171.47` |
| `Live` | `Short` | `2675.00` | 237,000,000.00 USD | 4,380,000.00 USD | 0.00 USD | `+20.35%` | `1,635.94` |
| `Live` | `Short` | `2685.00` | 237,120,000.00 USD | 120,480.00 USD | 0.00 USD | `+20.80%` | `44.87` |
| `Live` | `Short` | `2695.00` | 237,210,000.00 USD | 83,170.00 USD | 0.00 USD | `+21.25%` | `30.86` |
| `Live` | `Short` | `2705.00` | 243,150,000.00 USD | 5,940,000.00 USD | 0.00 USD | `+21.70%` | `2,196.09` |
| `Live` | `Short` | `2715.00` | 243,440,000.00 USD | 296,820.00 USD | 0.00 USD | `+22.15%` | `109.33` |
| `Live` | `Short` | `2725.00` | 243,760,000.00 USD | 315,000.00 USD | 0.00 USD | `+22.60%` | `115.60` |
| `Live` | `Short` | `2735.00` | 243,950,000.00 USD | 188,530.00 USD | 0.00 USD | `+23.05%` | `68.93` |
| `Live` | `Short` | `2745.00` | 244,690,000.00 USD | 739,840.00 USD | 0.00 USD | `+23.50%` | `269.52` |
| `Live` | `Short` | `2755.00` | 262,990,000.00 USD | 18,300,000.00 USD | 0.00 USD | `+23.95%` | `6,644.24` |
| `Live` | `Short` | `2765.00` | 288,500,000.00 USD | 25,510,000.00 USD | 0.00 USD | `+24.40%` | `9,226.40` |
| `Live` | `Short` | `2775.00` | 289,040,000.00 USD | 534,220.00 USD | 0.00 USD | `+24.85%` | `192.51` |
| `Live` | `Short` | `2785.00` | 294,570,000.00 USD | 5,530,000.00 USD | 0.00 USD | `+25.30%` | `1,987.23` |
| `Live` | `Short` | `2795.00` | 294,600,000.00 USD | 24,130.00 USD | 0.00 USD | `+25.75%` | `8.63` |
| `Live` | `Short` | `2805.00` | 299,880,000.00 USD | 5,290,000.00 USD | 0.00 USD | `+26.20%` | `1,884.36` |
| `Live` | `Short` | `2815.00` | 302,410,000.00 USD | 2,530,000.00 USD | 0.00 USD | `+26.65%` | `899.08` |
| `Live` | `Short` | `2825.00` | 302,530,000.00 USD | 115,850.00 USD | 0.00 USD | `+27.10%` | `41.01` |
| `Live` | `Short` | `2835.00` | 308,530,000.00 USD | 6,000,000.00 USD | 0.00 USD | `+27.55%` | `2,116.70` |
| `Live` | `Short` | `2845.00` | 308,980,000.00 USD | 453,890.00 USD | 0.00 USD | `+28.00%` | `159.54` |
| `Live` | `Short` | `2855.00` | 309,510,000.00 USD | 524,990.00 USD | 0.00 USD | `+28.45%` | `183.89` |
| `Live` | `Short` | `2865.00` | 309,540,000.00 USD | 35,400.00 USD | 0.00 USD | `+28.89%` | `12.35` |
| `Live` | `Short` | `2875.00` | 309,610,000.00 USD | 64,880.00 USD | 0.00 USD | `+29.34%` | `22.57` |
| `Live` | `Short` | `2885.00` | 311,660,000.00 USD | 2,050,000.00 USD | 0.00 USD | `+29.79%` | `709.52` |
| `Live` | `Short` | `2895.00` | 312,060,000.00 USD | 405,610.00 USD | 0.00 USD | `+30.24%` | `140.11` |
| `Live` | `Short` | `2905.00` | 327,790,000.00 USD | 15,730,000.00 USD | 0.00 USD | `+30.69%` | `5,414.54` |
| `Live` | `Short` | `2915.00` | 330,210,000.00 USD | 2,420,000.00 USD | 0.00 USD | `+31.14%` | `831.85` |
| `Live` | `Short` | `2925.00` | 330,230,000.00 USD | 15,390.00 USD | 0.00 USD | `+31.59%` | `5.26` |
| `Live` | `Short` | `2935.00` | 330,280,000.00 USD | 48,280.00 USD | 0.00 USD | `+32.04%` | `16.45` |
| `Live` | `Short` | `2945.00` | 330,680,000.00 USD | 402,540.00 USD | 0.00 USD | `+32.49%` | `136.69` |
| `Live` | `Short` | `2955.00` | 330,910,000.00 USD | 232,250.00 USD | 0.00 USD | `+32.94%` | `78.60` |
| `Live` | `Short` | `2965.00` | 336,090,000.00 USD | 5,170,000.00 USD | 0.00 USD | `+33.39%` | `1,744.62` |
| `Live` | `Short` | `2975.00` | 336,300,000.00 USD | 212,550.00 USD | 0.00 USD | `+33.84%` | `71.45` |
| `Live` | `Short` | `2985.00` | 337,330,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+34.29%` | `345.87` |
| `Live` | `Short` | `2995.00` | 338,940,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+34.74%` | `537.86` |
| `Live` | `Short` | `3005.00` | 339,470,000.00 USD | 526,020.00 USD | 0.00 USD | `+35.19%` | `175.05` |
| `Live` | `Short` | `3015.00` | 339,900,000.00 USD | 436,400.00 USD | 0.00 USD | `+35.64%` | `144.74` |
| `Live` | `Short` | `3025.00` | 340,790,000.00 USD | 884,050.00 USD | 0.00 USD | `+36.09%` | `292.25` |
| `Live` | `Short` | `3035.00` | 355,330,000.00 USD | 14,540,000.00 USD | 0.00 USD | `+36.54%` | `4,789.70` |
| `Live` | `Short` | `3045.00` | 355,340,000.00 USD | 19,380.00 USD | 0.00 USD | `+36.99%` | `6.37` |
| `Live` | `Short` | `3055.00` | 357,800,000.00 USD | 2,450,000.00 USD | 0.00 USD | `+37.44%` | `802.63` |
| `Live` | `Short` | `3065.00` | 357,810,000.00 USD | 17,500.00 USD | 0.00 USD | `+37.89%` | `5.71` |
| `Live` | `Short` | `3075.00` | 357,840,000.00 USD | 21,130.00 USD | 0.00 USD | `+38.34%` | `6.87` |
| `Live` | `Short` | `3085.00` | 363,300,000.00 USD | 5,460,000.00 USD | 0.00 USD | `+38.79%` | `1,770.66` |
| `Live` | `Short` | `3095.00` | 380,770,000.00 USD | 17,470,000.00 USD | 0.00 USD | `+39.24%` | `5,645.70` |
| `Live` | `Short` | `3105.00` | 397,700,000.00 USD | 16,930,000.00 USD | 0.00 USD | `+39.69%` | `5,453.01` |
| `Live` | `Short` | `3115.00` | 399,480,000.00 USD | 1,780,000.00 USD | 0.00 USD | `+40.14%` | `572.01` |
| `Live` | `Short` | `3125.00` | 428,770,000.00 USD | 29,290,000.00 USD | 0.00 USD | `+40.59%` | `9,371.88` |
| `Live` | `Short` | `3135.00` | 428,980,000.00 USD | 209,490.00 USD | 0.00 USD | `+41.04%` | `66.82` |
| `Live` | `Short` | `3145.00` | 429,670,000.00 USD | 691,720.00 USD | 0.00 USD | `+41.49%` | `219.94` |
| `Live` | `Short` | `3155.00` | 466,680,000.00 USD | 37,010,000.00 USD | 0.00 USD | `+41.94%` | `11,730.97` |
| `Live` | `Short` | `3165.00` | 466,840,000.00 USD | 157,220.00 USD | 0.00 USD | `+42.39%` | `49.67` |
| `Live` | `Short` | `3175.00` | 467,760,000.00 USD | 918,150.00 USD | 0.00 USD | `+42.84%` | `289.18` |
| `Live` | `Short` | `3185.00` | 538,530,000.00 USD | 70,770,000.00 USD | 0.00 USD | `+43.29%` | `22,220.34` |
| `Live` | `Short` | `3195.00` | 542,190,000.00 USD | 3,650,000.00 USD | 0.00 USD | `+43.74%` | `1,143.79` |
| `Live` | `Short` | `3205.00` | 542,310,000.00 USD | 129,060.00 USD | 0.00 USD | `+44.19%` | `40.27` |
| `Live` | `Short` | `3215.00` | 542,490,000.00 USD | 176,300.00 USD | 0.00 USD | `+44.64%` | `54.84` |
| `Live` | `Short` | `3225.00` | 550,760,000.00 USD | 8,270,000.00 USD | 0.00 USD | `+45.09%` | `2,564.19` |
| `Live` | `Short` | `3235.00` | 560,510,000.00 USD | 9,750,000.00 USD | 0.00 USD | `+45.54%` | `3,013.29` |
| `Live` | `Short` | `3245.00` | 560,680,000.00 USD | 171,870.00 USD | 0.00 USD | `+45.99%` | `52.96` |
| `Live` | `Short` | `3255.00` | 565,430,000.00 USD | 4,750,000.00 USD | 0.00 USD | `+46.44%` | `1,459.94` |
| `Live` | `Short` | `3265.00` | 567,630,000.00 USD | 2,200,000.00 USD | 0.00 USD | `+46.89%` | `674.18` |
| `Live` | `Short` | `3275.00` | 576,090,000.00 USD | 8,450,000.00 USD | 0.00 USD | `+47.34%` | `2,581.36` |
| `Live` | `Short` | `3285.00` | 576,380,000.00 USD | 296,110.00 USD | 0.00 USD | `+47.79%` | `90.14` |
| `Live` | `Short` | `3295.00` | 576,490,000.00 USD | 102,300.00 USD | 0.00 USD | `+48.24%` | `31.05` |
| `Live` | `Short` | `3305.00` | 577,680,000.00 USD | 1,190,000.00 USD | 0.00 USD | `+48.69%` | `361.23` |
| `Live` | `Short` | `3315.00` | 578,390,000.00 USD | 714,800.00 USD | 0.00 USD | `+49.14%` | `215.63` |
| `Live` | `Short` | `3325.00` | 581,340,000.00 USD | 2,940,000.00 USD | 0.00 USD | `+49.59%` | `884.68` |
| `Live` | `Short` | `3335.00` | 581,570,000.00 USD | 233,210.00 USD | 0.00 USD | `+50.04%` | `69.93` |
| `Live` | `Short` | `3345.00` | 582,070,000.00 USD | 504,080.00 USD | 0.00 USD | `+50.49%` | `150.70` |
| `Live` | `Short` | `3355.00` | 583,140,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+50.94%` | `317.13` |
| `Live` | `Short` | `3365.00` | 584,810,000.00 USD | 1,670,000.00 USD | 0.00 USD | `+51.39%` | `497.36` |
| `Live` | `Short` | `3375.00` | 586,710,000.00 USD | 1,900,000.00 USD | 0.00 USD | `+51.84%` | `561.93` |
| `Live` | `Short` | `3385.00` | 586,810,000.00 USD | 101,820.00 USD | 0.00 USD | `+52.29%` | `30.08` |
| `Live` | `Short` | `3395.00` | 590,020,000.00 USD | 3,210,000.00 USD | 0.00 USD | `+52.74%` | `946.81` |
| `Live` | `Short` | `3405.00` | 594,750,000.00 USD | 4,730,000.00 USD | 0.00 USD | `+53.19%` | `1,389.23` |
| `Live` | `Short` | `3415.00` | 594,790,000.00 USD | 39,630.00 USD | 0.00 USD | `+53.64%` | `11.60` |
| `Live` | `Short` | `3425.00` | 609,660,000.00 USD | 14,870,000.00 USD | 0.00 USD | `+54.09%` | `4,340.85` |
| `Live` | `Short` | `3435.00` | 609,860,000.00 USD | 193,830.00 USD | 0.00 USD | `+54.54%` | `56.43` |
| `Live` | `Short` | `3445.00` | 610,520,000.00 USD | 661,810.00 USD | 0.00 USD | `+54.99%` | `192.11` |
| `Live` | `Short` | `3455.00` | 611,090,000.00 USD | 569,080.00 USD | 0.00 USD | `+55.44%` | `164.71` |
| `Live` | `Short` | `3465.00` | 611,890,000.00 USD | 799,730.00 USD | 0.00 USD | `+55.89%` | `230.80` |
| `Live` | `Short` | `3475.00` | 612,150,000.00 USD | 268,290.00 USD | 0.00 USD | `+56.34%` | `77.21` |
| `Live` | `Short` | `3485.00` | 612,370,000.00 USD | 214,060.00 USD | 0.00 USD | `+56.79%` | `61.42` |
| `Live` | `Short` | `3495.00` | 613,900,000.00 USD | 1,530,000.00 USD | 0.00 USD | `+57.24%` | `437.92` |
| `Live` | `Short` | `3505.00` | 614,820,000.00 USD | 925,810.00 USD | 0.00 USD | `+57.69%` | `264.14` |
| `Live` | `Short` | `3515.00` | 615,500,000.00 USD | 673,280.00 USD | 0.00 USD | `+58.14%` | `191.55` |
| `Live` | `Short` | `3525.00` | 615,600,000.00 USD | 97,210.00 USD | 0.00 USD | `+58.59%` | `27.58` |
| `Live` | `Short` | `3535.00` | 630,140,000.00 USD | 14,540,000.00 USD | 0.00 USD | `+59.04%` | `4,113.36` |
| `Live` | `Short` | `3545.00` | 630,150,000.00 USD | 13,710.00 USD | 0.00 USD | `+59.49%` | `3.87` |
| `Live` | `Short` | `3555.00` | 630,860,000.00 USD | 705,630.00 USD | 0.00 USD | `+59.94%` | `198.49` |
| `Live` | `Short` | `3565.00` | 630,930,000.00 USD | 71,060.00 USD | 0.00 USD | `+60.39%` | `19.93` |
| `Live` | `Short` | `3575.00` | 631,010,000.00 USD | 80,920.00 USD | 0.00 USD | `+60.84%` | `22.63` |
| `Live` | `Short` | `3585.00` | 631,760,000.00 USD | 749,070.00 USD | 0.00 USD | `+61.29%` | `208.95` |
| `Live` | `Short` | `3595.00` | 631,860,000.00 USD | 103,870.00 USD | 0.00 USD | `+61.74%` | `28.89` |
| `Live` | `Short` | `3605.00` | 686,660,000.00 USD | 54,800,000.00 USD | 0.00 USD | `+62.19%` | `15,200.79` |
| `Live` | `Short` | `3615.00` | 690,420,000.00 USD | 3,760,000.00 USD | 0.00 USD | `+62.64%` | `1,039.20` |
| `Live` | `Short` | `3625.00` | 691,540,000.00 USD | 1,120,000.00 USD | 0.00 USD | `+63.09%` | `309.53` |
| `Live` | `Short` | `3635.00` | 700,280,000.00 USD | 8,740,000.00 USD | 0.00 USD | `+63.54%` | `2,405.69` |
| `Live` | `Short` | `3645.00` | 700,310,000.00 USD | 22,760.00 USD | 0.00 USD | `+63.99%` | `6.24` |
| `Live` | `Short` | `3655.00` | 700,330,000.00 USD | 22,630.00 USD | 0.00 USD | `+64.44%` | `6.19` |
| `Live` | `Short` | `3665.00` | 707,150,000.00 USD | 6,820,000.00 USD | 0.00 USD | `+64.89%` | `1,861.23` |
| `Live` | `Short` | `3675.00` | 707,150,000.00 USD | 4,750.00 USD | 0.00 USD | `+65.34%` | `1.29` |
| `Live` | `Short` | `3685.00` | 707,360,000.00 USD | 207,200.00 USD | 0.00 USD | `+65.79%` | `56.23` |
| `Live` | `Short` | `3695.00` | 707,400,000.00 USD | 42,780.00 USD | 0.00 USD | `+66.24%` | `11.58` |
| `Live` | `Short` | `3705.00` | 707,410,000.00 USD | 3,950.00 USD | 0.00 USD | `+66.69%` | `1.07` |
| `Live` | `Short` | `3715.00` | 707,720,000.00 USD | 315,680.00 USD | 0.00 USD | `+67.14%` | `84.97` |
| `Live` | `Short` | `3725.00` | 707,960,000.00 USD | 234,460.00 USD | 0.00 USD | `+67.59%` | `62.94` |
| `Live` | `Short` | `3735.00` | 708,410,000.00 USD | 448,050.00 USD | 0.00 USD | `+68.04%` | `119.96` |
| `Live` | `Short` | `3745.00` | 713,740,000.00 USD | 5,330,000.00 USD | 0.00 USD | `+68.49%` | `1,424.46` |
| `Live` | `Short` | `3755.00` | 715,700,000.00 USD | 1,960,000.00 USD | 0.00 USD | `+68.94%` | `520.69` |
| `Live` | `Short` | `3765.00` | 1,110,000,000.00 USD | 394,330,000.00 USD | 0.00 USD | `+69.39%` | `104,735.02` |
| `Live` | `Short` | `3775.00` | 1,110,000,000.00 USD | 275,200.00 USD | 0.00 USD | `+69.84%` | `72.90` |
| `Live` | `Short` | `3785.00` | 1,120,000,000.00 USD | 7,380,000.00 USD | 0.00 USD | `+70.29%` | `1,950.49` |
| `Live` | `Short` | `3795.00` | 1,180,000,000.00 USD | 57,450,000.00 USD | 0.00 USD | `+70.74%` | `15,137.11` |
| `Live` | `Short` | `3805.00` | 1,180,000,000.00 USD | 3,240.00 USD | 0.00 USD | `+71.19%` | `0.85` |
| `Live` | `Short` | `3815.00` | 1,180,000,000.00 USD | 2,960.00 USD | 0.00 USD | `+71.64%` | `0.78` |
| `Live` | `Short` | `3825.00` | 1,180,000,000.00 USD | 97,310.00 USD | 0.00 USD | `+72.08%` | `25.44` |
| `Live` | `Short` | `3835.00` | 1,180,000,000.00 USD | 289,260.00 USD | 0.00 USD | `+72.53%` | `75.43` |
| `Live` | `Short` | `3845.00` | 1,180,000,000.00 USD | 1,990,000.00 USD | 0.00 USD | `+72.98%` | `517.25` |
| `Live` | `Short` | `3855.00` | 1,180,000,000.00 USD | 1,130,000.00 USD | 0.00 USD | `+73.43%` | `293.48` |
| `Live` | `Short` | `3865.00` | 1,180,000,000.00 USD | 473,710.00 USD | 0.00 USD | `+73.88%` | `122.56` |
| `Live` | `Short` | `3875.00` | 1,180,000,000.00 USD | 93,650.00 USD | 0.00 USD | `+74.33%` | `24.17` |
| `Live` | `Short` | `3885.00` | 1,220,000,000.00 USD | 39,800,000.00 USD | 0.00 USD | `+74.78%` | `10,244.59` |
| `Live` | `Short` | `3895.00` | 1,220,000,000.00 USD | 46,120.00 USD | 0.00 USD | `+75.23%` | `11.84` |
| `Live` | `Short` | `3905.00` | 1,220,000,000.00 USD | 516,720.00 USD | 0.00 USD | `+75.68%` | `132.32` |
| `Live` | `Short` | `3915.00` | 1,220,000,000.00 USD | 740,390.00 USD | 0.00 USD | `+76.13%` | `189.12` |
| `Live` | `Short` | `3925.00` | 1,220,000,000.00 USD | 147,220.00 USD | 0.00 USD | `+76.58%` | `37.51` |
| `Live` | `Short` | `3935.00` | 1,220,000,000.00 USD | 2,040,000.00 USD | 0.00 USD | `+77.03%` | `518.11` |
| `Live` | `Short` | `3945.00` | 1,220,000,000.00 USD | 4,310.00 USD | 0.00 USD | `+77.48%` | `1.09` |
| `Live` | `Short` | `3955.00` | 1,220,000,000.00 USD | 67,490.00 USD | 0.00 USD | `+77.93%` | `17.06` |
| `Live` | `Short` | `3965.00` | 1,220,000,000.00 USD | 6,960.00 USD | 0.00 USD | `+78.38%` | `1.76` |
| `Live` | `Short` | `3975.00` | 1,220,000,000.00 USD | 236,270.00 USD | 0.00 USD | `+78.83%` | `59.44` |
| `Live` | `Short` | `3985.00` | 1,220,000,000.00 USD | 80,870.00 USD | 0.00 USD | `+79.28%` | `20.29` |
| `Live` | `Short` | `3995.00` | 1,220,000,000.00 USD | 1,260,000.00 USD | 0.00 USD | `+79.73%` | `316.29` |
| `Live` | `Short` | `4005.00` | 1,230,000,000.00 USD | 975,110.00 USD | 0.00 USD | `+80.18%` | `243.47` |
| `Live` | `Short` | `4015.00` | 1,230,000,000.00 USD | 483,440.00 USD | 0.00 USD | `+80.63%` | `120.41` |
| `Live` | `Short` | `4025.00` | 1,230,000,000.00 USD | 65,250.00 USD | 0.00 USD | `+81.08%` | `16.21` |
| `Live` | `Short` | `4035.00` | 1,230,000,000.00 USD | 396,110.00 USD | 0.00 USD | `+81.53%` | `98.17` |
| `Live` | `Short` | `4045.00` | 1,230,000,000.00 USD | 7,590.00 USD | 0.00 USD | `+81.98%` | `1.88` |
| `Live` | `Short` | `4055.00` | 1,230,000,000.00 USD | 1,690,000.00 USD | 0.00 USD | `+82.43%` | `416.76` |
| `Live` | `Short` | `4065.00` | 1,230,000,000.00 USD | 283,580.00 USD | 0.00 USD | `+82.88%` | `69.76` |
| `Live` | `Short` | `4075.00` | 1,230,000,000.00 USD | 1,530,000.00 USD | 0.00 USD | `+83.33%` | `374.98` |
| `Live` | `Short` | `4085.00` | 1,230,000,000.00 USD | 58,190.00 USD | 0.00 USD | `+83.78%` | `14.25` |
| `Live` | `Short` | `4095.00` | 1,230,000,000.00 USD | 5,620.00 USD | 0.00 USD | `+84.23%` | `1.37` |
| `Live` | `Short` | `4105.00` | 1,230,000,000.00 USD | 26,460.00 USD | 0.00 USD | `+84.68%` | `6.45` |
| `Live` | `Short` | `4115.00` | 1,230,000,000.00 USD | 58,200.00 USD | 0.00 USD | `+85.13%` | `14.14` |
| `Live` | `Short` | `4125.00` | 1,230,000,000.00 USD | 487,770.00 USD | 0.00 USD | `+85.58%` | `118.25` |
| `Live` | `Short` | `4135.00` | 1,230,000,000.00 USD | 95,470.00 USD | 0.00 USD | `+86.03%` | `23.09` |
| `Live` | `Short` | `4145.00` | 1,230,000,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+86.48%` | `243.86` |
| `Live` | `Short` | `4155.00` | 1,230,000,000.00 USD | 62,880.00 USD | 0.00 USD | `+86.93%` | `15.13` |
| `Live` | `Short` | `4165.00` | 1,230,000,000.00 USD | 123,920.00 USD | 0.00 USD | `+87.38%` | `29.75` |
| `Live` | `Short` | `4175.00` | 1,230,000,000.00 USD | 242,040.00 USD | 0.00 USD | `+87.83%` | `57.97` |
| `Live` | `Short` | `4185.00` | 1,230,000,000.00 USD | 859,990.00 USD | 0.00 USD | `+88.28%` | `205.49` |
| `Live` | `Short` | `4195.00` | 1,270,000,000.00 USD | 32,590,000.00 USD | 0.00 USD | `+88.73%` | `7,767.60` |
| `Live` | `Short` | `4205.00` | 1,270,000,000.00 USD | 774,870.00 USD | 0.00 USD | `+89.18%` | `184.27` |
| `Live` | `Short` | `4215.00` | 1,270,000,000.00 USD | 42,320.00 USD | 0.00 USD | `+89.63%` | `10.04` |
| `Live` | `Short` | `4225.00` | 1,350,000,000.00 USD | 84,890,000.00 USD | 0.00 USD | `+90.08%` | `20,091.31` |
| `Live` | `Short` | `4235.00` | 1,350,000,000.00 USD | 61,210.00 USD | 0.00 USD | `+90.53%` | `14.45` |
| `Live` | `Short` | `4255.00` | 1,350,000,000.00 USD | 18,700.00 USD | 0.00 USD | `+91.43%` | `4.40` |
| `Live` | `Short` | `4265.00` | 1,350,000,000.00 USD | 59,020.00 USD | 0.00 USD | `+91.88%` | `13.84` |
| `Live` | `Short` | `4275.00` | 1,350,000,000.00 USD | 682,840.00 USD | 0.00 USD | `+92.33%` | `159.73` |
| `Live` | `Short` | `4285.00` | 1,350,000,000.00 USD | 14,040.00 USD | 0.00 USD | `+92.78%` | `3.28` |
| `Live` | `Short` | `4295.00` | 1,350,000,000.00 USD | 1,520.00 USD | 0.00 USD | `+93.23%` | `0.35` |
| `Live` | `Short` | `4305.00` | 1,350,000,000.00 USD | 13,140.00 USD | 0.00 USD | `+93.68%` | `3.05` |
| `Live` | `Short` | `4315.00` | 1,360,000,000.00 USD | 3,990,000.00 USD | 0.00 USD | `+94.13%` | `923.61` |
| `Live` | `Short` | `4325.00` | 1,360,000,000.00 USD | 285,720.00 USD | 0.00 USD | `+94.58%` | `66.06` |
| `Live` | `Short` | `4335.00` | 1,360,000,000.00 USD | 236,730.00 USD | 0.00 USD | `+95.03%` | `54.61` |
| `Live` | `Short` | `4345.00` | 1,360,000,000.00 USD | 22,710.00 USD | 0.00 USD | `+95.48%` | `5.23` |
| `Live` | `Short` | `4355.00` | 1,360,000,000.00 USD | 6,750.00 USD | 0.00 USD | `+95.93%` | `1.55` |
| `Live` | `Short` | `4365.00` | 1,360,000,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+96.38%` | `232.17` |
| `Live` | `Short` | `4375.00` | 1,360,000,000.00 USD | 699,700.00 USD | 0.00 USD | `+96.83%` | `159.93` |
| `Live` | `Short` | `4385.00` | 1,360,000,000.00 USD | 456,580.00 USD | 0.00 USD | `+97.28%` | `104.12` |
| `Live` | `Short` | `4395.00` | 1,360,000,000.00 USD | 9,790.00 USD | 0.00 USD | `+97.73%` | `2.23` |
| `Live` | `Short` | `4405.00` | 1,360,000,000.00 USD | 335,480.00 USD | 0.00 USD | `+98.18%` | `76.16` |
| `Live` | `Short` | `4415.00` | 1,360,000,000.00 USD | 40,260.00 USD | 0.00 USD | `+98.63%` | `9.12` |
| `Live` | `Short` | `4425.00` | 1,360,000,000.00 USD | 145,290.00 USD | 0.00 USD | `+99.08%` | `32.83` |
| `Live` | `Short` | `4435.00` | 1,360,000,000.00 USD | 34,160.00 USD | 0.00 USD | `+99.53%` | `7.70` |
| `Live` | `Short` | `4445.00` | 1,360,000,000.00 USD | 394,410.00 USD | 0.00 USD | `+99.98%` | `88.73` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `485.00` | 77,030,000.00 USD | 0.00 USD | 278.83 USD | `-78.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `505.00` | 77,030,000.00 USD | 0.00 USD | 16,120.00 USD | `-77.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 77,020,000.00 USD | 0.00 USD | 563.16 USD | `-75.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.00` | 77,020,000.00 USD | 0.00 USD | 583.40 USD | `-70.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.00` | 77,020,000.00 USD | 0.00 USD | 16,690.00 USD | `-70.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.00` | 77,000,000.00 USD | 0.00 USD | 578.54 USD | `-69.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.00` | 77,000,000.00 USD | 0.00 USD | 242.21 USD | `-68.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 77,000,000.00 USD | 0.00 USD | 885.90 USD | `-68.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 77,000,000.00 USD | 0.00 USD | 177.27 USD | `-66.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 77,000,000.00 USD | 0.00 USD | 2,400.00 USD | `-63.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 77,000,000.00 USD | 0.00 USD | 1,670.00 USD | `-62.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 76,990,000.00 USD | 0.00 USD | 139,430.00 USD | `-61.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `875.00` | 76,860,000.00 USD | 0.00 USD | 918.49 USD | `-60.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 76,850,000.00 USD | 0.00 USD | 3,130.00 USD | `-60.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 76,850,000.00 USD | 0.00 USD | 2,780.00 USD | `-59.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 76,850,000.00 USD | 0.00 USD | 516.34 USD | `-55.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 76,850,000.00 USD | 0.00 USD | 100.50 USD | `-55.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 76,850,000.00 USD | 0.00 USD | 223,740.00 USD | `-54.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 76,620,000.00 USD | 0.00 USD | 445.08 USD | `-54.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 76,620,000.00 USD | 0.00 USD | 112.03 USD | `-53.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1045.00` | 76,620,000.00 USD | 0.00 USD | 1,260.00 USD | `-52.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 76,620,000.00 USD | 0.00 USD | 1,060.00 USD | `-52.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 76,620,000.00 USD | 0.00 USD | 995.34 USD | `-51.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 76,620,000.00 USD | 0.00 USD | 1,610.00 USD | `-50.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 76,620,000.00 USD | 0.00 USD | 11,050.00 USD | `-49.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 76,610,000.00 USD | 0.00 USD | 1,320.00 USD | `-49.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 76,610,000.00 USD | 0.00 USD | 1,000.00 USD | `-48.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 76,610,000.00 USD | 0.00 USD | 476.46 USD | `-47.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 76,600,000.00 USD | 0.00 USD | 972.41 USD | `-46.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1195.00` | 76,600,000.00 USD | 0.00 USD | 221.55 USD | `-46.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 76,600,000.00 USD | 0.00 USD | 3,110.00 USD | `-45.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 76,600,000.00 USD | 0.00 USD | 995.93 USD | `-44.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 76,600,000.00 USD | 0.00 USD | 951.93 USD | `-43.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 76,600,000.00 USD | 0.00 USD | 2,290.00 USD | `-43.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 76,600,000.00 USD | 0.00 USD | 9,050.00 USD | `-42.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 76,590,000.00 USD | 0.00 USD | 7,030.00 USD | `-41.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 76,580,000.00 USD | 0.00 USD | 25,040.00 USD | `-41.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 76,560,000.00 USD | 0.00 USD | 1,440.00 USD | `-40.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1335.00` | 76,550,000.00 USD | 0.00 USD | 281.69 USD | `-39.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 76,550,000.00 USD | 0.00 USD | 141,950.00 USD | `-39.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 76,410,000.00 USD | 0.00 USD | 128.86 USD | `-39.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 76,410,000.00 USD | 0.00 USD | 1,270.00 USD | `-38.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 76,410,000.00 USD | 0.00 USD | 4,160.00 USD | `-38.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1385.00` | 76,410,000.00 USD | 0.00 USD | 100,800.00 USD | `-37.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 76,310,000.00 USD | 0.00 USD | 535,600.00 USD | `-37.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 75,770,000.00 USD | 0.00 USD | 18,840.00 USD | `-36.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 75,750,000.00 USD | 0.00 USD | 6,450.00 USD | `-35.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 75,740,000.00 USD | 0.00 USD | 852.10 USD | `-35.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 75,740,000.00 USD | 0.00 USD | 1,610.00 USD | `-34.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 75,740,000.00 USD | 0.00 USD | 5,090.00 USD | `-34.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 75,740,000.00 USD | 0.00 USD | 19,730.00 USD | `-34.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 75,720,000.00 USD | 0.00 USD | 2,600.00 USD | `-33.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 75,710,000.00 USD | 0.00 USD | 19,930.00 USD | `-33.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 75,690,000.00 USD | 0.00 USD | 11,460.00 USD | `-32.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 75,680,000.00 USD | 0.00 USD | 70,590.00 USD | `-32.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 75,610,000.00 USD | 0.00 USD | 11,140.00 USD | `-31.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 75,600,000.00 USD | 0.00 USD | 31,900.00 USD | `-31.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 75,570,000.00 USD | 0.00 USD | 2,090.00 USD | `-30.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 75,570,000.00 USD | 0.00 USD | 960.99 USD | `-30.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 75,570,000.00 USD | 0.00 USD | 32,880.00 USD | `-30.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 75,530,000.00 USD | 0.00 USD | 10,660.00 USD | `-29.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 75,520,000.00 USD | 0.00 USD | 198,620.00 USD | `-29.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 75,320,000.00 USD | 0.00 USD | 4,990.00 USD | `-28.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 75,320,000.00 USD | 0.00 USD | 7,240.00 USD | `-28.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 75,310,000.00 USD | 0.00 USD | 431,660.00 USD | `-27.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 74,880,000.00 USD | 0.00 USD | 25,700.00 USD | `-27.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 74,850,000.00 USD | 0.00 USD | 16,400.00 USD | `-26.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 74,840,000.00 USD | 0.00 USD | 10,560.00 USD | `-26.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 74,830,000.00 USD | 0.00 USD | 323,930.00 USD | `-25.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 74,500,000.00 USD | 0.00 USD | 114,830.00 USD | `-25.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 74,390,000.00 USD | 0.00 USD | 865.13 USD | `-25.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 74,390,000.00 USD | 0.00 USD | 289.27 USD | `-24.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 74,390,000.00 USD | 0.00 USD | 35,320.00 USD | `-24.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 74,350,000.00 USD | 0.00 USD | 42,420.00 USD | `-23.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 74,310,000.00 USD | 0.00 USD | 274,290.00 USD | `-23.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 74,040,000.00 USD | 0.00 USD | 195,960.00 USD | `-22.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 73,840,000.00 USD | 0.00 USD | 217,800.00 USD | `-22.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 73,620,000.00 USD | 0.00 USD | 189,590.00 USD | `-21.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 73,430,000.00 USD | 0.00 USD | 156,220.00 USD | `-21.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 73,280,000.00 USD | 0.00 USD | 611,610.00 USD | `-21.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 72,660,000.00 USD | 0.00 USD | 215,000.00 USD | `-20.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 72,450,000.00 USD | 0.00 USD | 133,460.00 USD | `-20.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 72,320,000.00 USD | 0.00 USD | 132,090.00 USD | `-19.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 72,180,000.00 USD | 0.00 USD | 308,190.00 USD | `-19.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 71,880,000.00 USD | 0.00 USD | 850,390.00 USD | `-18.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 71,030,000.00 USD | 0.00 USD | 369,730.00 USD | `-18.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 70,660,000.00 USD | 0.00 USD | 141,220.00 USD | `-17.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 70,510,000.00 USD | 0.00 USD | 99,800.00 USD | `-17.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 70,410,000.00 USD | 0.00 USD | 120,370.00 USD | `-16.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 70,290,000.00 USD | 0.00 USD | 874,400.00 USD | `-16.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 69,420,000.00 USD | 0.00 USD | 121,710.00 USD | `-16.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 69,300,000.00 USD | 0.00 USD | 18,270,000.00 USD | `-15.64%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 51,020,000.00 USD | 0.00 USD | 89,480.00 USD | `-15.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 50,940,000.00 USD | 0.00 USD | 130,100.00 USD | `-14.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 50,810,000.00 USD | 0.00 USD | 213,850.00 USD | `-14.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 50,590,000.00 USD | 0.00 USD | 166,350.00 USD | `-13.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1925.00` | 50,430,000.00 USD | 0.00 USD | 19,360,000.00 USD | `-13.40%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 31,060,000.00 USD | 0.00 USD | 165,340.00 USD | `-12.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 30,900,000.00 USD | 0.00 USD | 113,320.00 USD | `-12.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 30,780,000.00 USD | 0.00 USD | 115,190.00 USD | `-12.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 30,670,000.00 USD | 0.00 USD | 185,560.00 USD | `-11.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 30,480,000.00 USD | 0.00 USD | 118,800.00 USD | `-11.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 30,360,000.00 USD | 0.00 USD | 147,290.00 USD | `-10.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 30,210,000.00 USD | 0.00 USD | 165,000.00 USD | `-10.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 30,050,000.00 USD | 0.00 USD | 2,130,000.00 USD | `-9.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 27,920,000.00 USD | 0.00 USD | 84,180.00 USD | `-9.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 27,840,000.00 USD | 0.00 USD | 49,650.00 USD | `-8.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 27,790,000.00 USD | 0.00 USD | 209,680.00 USD | `-8.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 27,580,000.00 USD | 0.00 USD | 44,510.00 USD | `-8.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 27,530,000.00 USD | 0.00 USD | 302,590.00 USD | `-7.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 27,230,000.00 USD | 0.00 USD | 841,530.00 USD | `-7.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 26,390,000.00 USD | 0.00 USD | 187,050.00 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 26,200,000.00 USD | 0.00 USD | 160,610.00 USD | `-6.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 26,040,000.00 USD | 0.00 USD | 56,980.00 USD | `-5.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 25,990,000.00 USD | 0.00 USD | 1,050,000.00 USD | `-5.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 24,940,000.00 USD | 0.00 USD | 190,820.00 USD | `-4.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 24,750,000.00 USD | 0.00 USD | 224,320.00 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 24,520,000.00 USD | 0.00 USD | 378,420.00 USD | `-3.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 24,140,000.00 USD | 0.00 USD | 1,010,000.00 USD | `-3.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 23,130,000.00 USD | 0.00 USD | 1,810,000.00 USD | `-3.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 21,320,000.00 USD | 0.00 USD | 4,710,000.00 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 16,620,000.00 USD | 0.00 USD | 9,650,000.00 USD | `-2.15%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2185.00` | 6,960,000.00 USD | 0.00 USD | 204,500.00 USD | `-1.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 6,760,000.00 USD | 0.00 USD | 3,240,000.00 USD | `-1.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 3,510,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-0.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | `-0.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2225.00` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2235.00` | 2,460,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+0.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2245.00` | 2,610,000.00 USD | 146,470.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2255.00` | 3,130,000.00 USD | 523,500.00 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2265.00` | 5,030,000.00 USD | 1,900,000.00 USD | 0.00 USD | `+1.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 5,420,000.00 USD | 393,080.00 USD | 0.00 USD | `+2.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 6,260,000.00 USD | 838,420.00 USD | 0.00 USD | `+2.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 6,610,000.00 USD | 353,970.00 USD | 0.00 USD | `+3.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 16,520,000.00 USD | 9,900,000.00 USD | 0.00 USD | `+3.70%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2315.00` | 18,040,000.00 USD | 1,520,000.00 USD | 0.00 USD | `+4.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 18,240,000.00 USD | 200,450.00 USD | 0.00 USD | `+4.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 18,410,000.00 USD | 174,570.00 USD | 0.00 USD | `+5.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 19,970,000.00 USD | 1,560,000.00 USD | 0.00 USD | `+5.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 21,290,000.00 USD | 1,310,000.00 USD | 0.00 USD | `+5.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 23,500,000.00 USD | 2,210,000.00 USD | 0.00 USD | `+6.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 23,660,000.00 USD | 163,010.00 USD | 0.00 USD | `+6.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 25,620,000.00 USD | 1,960,000.00 USD | 0.00 USD | `+7.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 26,730,000.00 USD | 1,110,000.00 USD | 0.00 USD | `+7.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 29,230,000.00 USD | 2,500,000.00 USD | 0.00 USD | `+8.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 29,480,000.00 USD | 248,140.00 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 31,760,000.00 USD | 2,290,000.00 USD | 0.00 USD | `+9.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 31,950,000.00 USD | 184,920.00 USD | 0.00 USD | `+9.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 34,440,000.00 USD | 2,490,000.00 USD | 0.00 USD | `+10.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2455.00` | 34,580,000.00 USD | 141,470.00 USD | 0.00 USD | `+10.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 36,700,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+10.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 36,880,000.00 USD | 183,840.00 USD | 0.00 USD | `+11.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 38,990,000.00 USD | 2,100,000.00 USD | 0.00 USD | `+11.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 39,110,000.00 USD | 122,320.00 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 44,170,000.00 USD | 5,060,000.00 USD | 0.00 USD | `+12.70%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2515.00` | 51,760,000.00 USD | 7,600,000.00 USD | 0.00 USD | `+13.15%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 54,380,000.00 USD | 2,620,000.00 USD | 0.00 USD | `+13.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 54,440,000.00 USD | 61,230.00 USD | 0.00 USD | `+14.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 56,620,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+14.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 56,840,000.00 USD | 221,640.00 USD | 0.00 USD | `+14.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 59,200,000.00 USD | 2,360,000.00 USD | 0.00 USD | `+15.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 59,290,000.00 USD | 93,110.00 USD | 0.00 USD | `+15.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 61,800,000.00 USD | 2,510,000.00 USD | 0.00 USD | `+16.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 61,810,000.00 USD | 10,500.00 USD | 0.00 USD | `+16.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 65,090,000.00 USD | 3,280,000.00 USD | 0.00 USD | `+17.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 65,170,000.00 USD | 79,030.00 USD | 0.00 USD | `+17.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 67,350,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+18.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 67,500,000.00 USD | 147,930.00 USD | 0.00 USD | `+18.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 69,620,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+19.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 69,930,000.00 USD | 306,950.00 USD | 0.00 USD | `+19.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 72,070,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+19.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 72,330,000.00 USD | 261,420.00 USD | 0.00 USD | `+20.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 74,510,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+20.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 74,600,000.00 USD | 94,620.00 USD | 0.00 USD | `+21.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 77,450,000.00 USD | 2,840,000.00 USD | 0.00 USD | `+21.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 77,530,000.00 USD | 78,290.00 USD | 0.00 USD | `+22.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 77,810,000.00 USD | 286,910.00 USD | 0.00 USD | `+22.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 77,860,000.00 USD | 43,050.00 USD | 0.00 USD | `+23.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 78,030,000.00 USD | 178,210.00 USD | 0.00 USD | `+23.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 78,930,000.00 USD | 892,290.00 USD | 0.00 USD | `+23.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 79,030,000.00 USD | 103,020.00 USD | 0.00 USD | `+24.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 79,610,000.00 USD | 577,610.00 USD | 0.00 USD | `+24.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 79,640,000.00 USD | 35,580.00 USD | 0.00 USD | `+25.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 79,660,000.00 USD | 18,360.00 USD | 0.00 USD | `+25.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 80,570,000.00 USD | 905,020.00 USD | 0.00 USD | `+26.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 80,620,000.00 USD | 52,490.00 USD | 0.00 USD | `+26.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 80,660,000.00 USD | 43,930.00 USD | 0.00 USD | `+27.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 80,950,000.00 USD | 286,140.00 USD | 0.00 USD | `+27.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 81,950,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+28.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 83,220,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+28.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 83,230,000.00 USD | 11,150.00 USD | 0.00 USD | `+28.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 83,240,000.00 USD | 2,460.00 USD | 0.00 USD | `+29.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 83,540,000.00 USD | 305,820.00 USD | 0.00 USD | `+29.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 83,560,000.00 USD | 16,190.00 USD | 0.00 USD | `+30.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 85,040,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+30.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 85,050,000.00 USD | 10,340.00 USD | 0.00 USD | `+31.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 85,060,000.00 USD | 3,050.00 USD | 0.00 USD | `+31.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 85,110,000.00 USD | 52,370.00 USD | 0.00 USD | `+32.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 85,140,000.00 USD | 34,650.00 USD | 0.00 USD | `+32.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 85,190,000.00 USD | 44,750.00 USD | 0.00 USD | `+32.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 85,300,000.00 USD | 113,340.00 USD | 0.00 USD | `+33.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 85,450,000.00 USD | 145,510.00 USD | 0.00 USD | `+33.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 86,380,000.00 USD | 931,470.00 USD | 0.00 USD | `+34.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 91,300,000.00 USD | 4,920,000.00 USD | 0.00 USD | `+34.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 93,380,000.00 USD | 2,080,000.00 USD | 0.00 USD | `+35.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 93,390,000.00 USD | 9,740.00 USD | 0.00 USD | `+35.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 93,430,000.00 USD | 35,380.00 USD | 0.00 USD | `+36.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 93,500,000.00 USD | 74,910.00 USD | 0.00 USD | `+36.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 93,520,000.00 USD | 22,460.00 USD | 0.00 USD | `+36.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 94,290,000.00 USD | 771,070.00 USD | 0.00 USD | `+37.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 94,290,000.00 USD | 612.69 USD | 0.00 USD | `+37.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 94,340,000.00 USD | 49,330.00 USD | 0.00 USD | `+38.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 94,360,000.00 USD | 19,570.00 USD | 0.00 USD | `+38.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 94,360,000.00 USD | 928.50 USD | 0.00 USD | `+39.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 106,320,000.00 USD | 11,960,000.00 USD | 0.00 USD | `+39.69%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 106,430,000.00 USD | 110,480.00 USD | 0.00 USD | `+40.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 106,810,000.00 USD | 381,020.00 USD | 0.00 USD | `+40.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3135.00` | 106,810,000.00 USD | 674.02 USD | 0.00 USD | `+41.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 106,820,000.00 USD | 2,660.00 USD | 0.00 USD | `+41.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 106,870,000.00 USD | 58,930.00 USD | 0.00 USD | `+41.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 106,880,000.00 USD | 9,860.00 USD | 0.00 USD | `+42.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 106,880,000.00 USD | 149.22 USD | 0.00 USD | `+42.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 106,890,000.00 USD | 1,330.00 USD | 0.00 USD | `+43.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 106,930,000.00 USD | 41,120.00 USD | 0.00 USD | `+43.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 107,590,000.00 USD | 660,240.00 USD | 0.00 USD | `+44.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 107,590,000.00 USD | 1,760.00 USD | 0.00 USD | `+44.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 107,750,000.00 USD | 156,230.00 USD | 0.00 USD | `+45.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 107,750,000.00 USD | 167.25 USD | 0.00 USD | `+45.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 107,800,000.00 USD | 57,500.00 USD | 0.00 USD | `+45.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 108,040,000.00 USD | 236,580.00 USD | 0.00 USD | `+46.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 108,060,000.00 USD | 15,710.00 USD | 0.00 USD | `+46.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 108,060,000.00 USD | 1,630.00 USD | 0.00 USD | `+47.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 108,200,000.00 USD | 141,980.00 USD | 0.00 USD | `+47.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 108,210,000.00 USD | 15,350.00 USD | 0.00 USD | `+48.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 109,630,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+48.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 110,020,000.00 USD | 389,970.00 USD | 0.00 USD | `+49.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 110,040,000.00 USD | 24,200.00 USD | 0.00 USD | `+49.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 110,040,000.00 USD | 4,350.00 USD | 0.00 USD | `+50.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 110,050,000.00 USD | 2,170.00 USD | 0.00 USD | `+50.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 110,050,000.00 USD | 334.49 USD | 0.00 USD | `+50.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 110,050,000.00 USD | 238.58 USD | 0.00 USD | `+51.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 110,070,000.00 USD | 21,260.00 USD | 0.00 USD | `+51.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 110,130,000.00 USD | 58,010.00 USD | 0.00 USD | `+52.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 110,450,000.00 USD | 321,800.00 USD | 0.00 USD | `+52.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 111,950,000.00 USD | 1,500,000.00 USD | 0.00 USD | `+53.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 111,950,000.00 USD | 5,700.00 USD | 0.00 USD | `+53.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 111,970,000.00 USD | 16,310.00 USD | 0.00 USD | `+54.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 111,980,000.00 USD | 15,030.00 USD | 0.00 USD | `+54.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 112,000,000.00 USD | 18,600.00 USD | 0.00 USD | `+55.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 112,000,000.00 USD | 495.50 USD | 0.00 USD | `+55.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 112,010,000.00 USD | 3,190.00 USD | 0.00 USD | `+56.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 112,050,000.00 USD | 43,610.00 USD | 0.00 USD | `+56.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 112,050,000.00 USD | 158.32 USD | 0.00 USD | `+57.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 112,500,000.00 USD | 446,770.00 USD | 0.00 USD | `+57.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 112,540,000.00 USD | 43,510.00 USD | 0.00 USD | `+58.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 112,540,000.00 USD | 3,690.00 USD | 0.00 USD | `+58.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 112,550,000.00 USD | 9,810.00 USD | 0.00 USD | `+59.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 112,640,000.00 USD | 90,810.00 USD | 0.00 USD | `+59.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 112,650,000.00 USD | 2,300.00 USD | 0.00 USD | `+60.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3575.00` | 112,650,000.00 USD | 2,870.00 USD | 0.00 USD | `+60.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 112,650,000.00 USD | 354.92 USD | 0.00 USD | `+61.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 112,660,000.00 USD | 13,160.00 USD | 0.00 USD | `+61.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 112,760,000.00 USD | 101,080.00 USD | 0.00 USD | `+62.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3615.00` | 112,760,000.00 USD | 199.55 USD | 0.00 USD | `+62.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 112,770,000.00 USD | 10,210.00 USD | 0.00 USD | `+63.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 112,780,000.00 USD | 7,790.00 USD | 0.00 USD | `+63.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 112,790,000.00 USD | 3,860.00 USD | 0.00 USD | `+63.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 112,790,000.00 USD | 8,090.00 USD | 0.00 USD | `+64.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 112,800,000.00 USD | 8,130.00 USD | 0.00 USD | `+64.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 112,860,000.00 USD | 55,120.00 USD | 0.00 USD | `+65.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 112,860,000.00 USD | 1,410.00 USD | 0.00 USD | `+65.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 112,860,000.00 USD | 819.92 USD | 0.00 USD | `+66.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 112,860,000.00 USD | 323.58 USD | 0.00 USD | `+67.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 112,860,000.00 USD | 1,400.00 USD | 0.00 USD | `+67.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 112,870,000.00 USD | 6,490.00 USD | 0.00 USD | `+68.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3745.00` | 112,870,000.00 USD | 165.90 USD | 0.00 USD | `+68.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 112,870,000.00 USD | 751.00 USD | 0.00 USD | `+68.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 112,870,000.00 USD | 286.90 USD | 0.00 USD | `+70.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 112,870,000.00 USD | 1,560.00 USD | 0.00 USD | `+70.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 113,600,000.00 USD | 732,630.00 USD | 0.00 USD | `+71.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 113,620,000.00 USD | 20,930.00 USD | 0.00 USD | `+71.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 113,630,000.00 USD | 8,380.00 USD | 0.00 USD | `+72.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 113,630,000.00 USD | 711.78 USD | 0.00 USD | `+72.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 113,630,000.00 USD | 355.28 USD | 0.00 USD | `+72.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 113,640,000.00 USD | 5,170.00 USD | 0.00 USD | `+73.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 113,660,000.00 USD | 19,430.00 USD | 0.00 USD | `+74.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 113,670,000.00 USD | 12,120.00 USD | 0.00 USD | `+75.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 114,390,000.00 USD | 717,170.00 USD | 0.00 USD | `+76.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 114,430,000.00 USD | 42,570.00 USD | 0.00 USD | `+77.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 114,490,000.00 USD | 59,170.00 USD | 0.00 USD | `+77.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 114,490,000.00 USD | 1,380.00 USD | 0.00 USD | `+77.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 114,500,000.00 USD | 6,960.00 USD | 0.00 USD | `+78.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 114,510,000.00 USD | 14,610.00 USD | 0.00 USD | `+79.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 114,520,000.00 USD | 4,280.00 USD | 0.00 USD | `+79.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 117,150,000.00 USD | 2,640,000.00 USD | 0.00 USD | `+80.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 117,150,000.00 USD | 898.59 USD | 0.00 USD | `+81.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 117,150,000.00 USD | 811.00 USD | 0.00 USD | `+82.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 117,160,000.00 USD | 4,310.00 USD | 0.00 USD | `+83.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 117,160,000.00 USD | 3,050.00 USD | 0.00 USD | `+83.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 117,200,000.00 USD | 36,740.00 USD | 0.00 USD | `+84.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 117,200,000.00 USD | 5,990.00 USD | 0.00 USD | `+85.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 117,210,000.00 USD | 372.90 USD | 0.00 USD | `+85.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 117,210,000.00 USD | 395.43 USD | 0.00 USD | `+86.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 117,210,000.00 USD | 376.65 USD | 0.00 USD | `+88.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 117,250,000.00 USD | 42,260.00 USD | 0.00 USD | `+89.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 117,250,000.00 USD | 460.70 USD | 0.00 USD | `+89.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 117,250,000.00 USD | 1,270.00 USD | 0.00 USD | `+90.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 117,250,000.00 USD | 4,300.00 USD | 0.00 USD | `+91.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 117,250,000.00 USD | 437.16 USD | 0.00 USD | `+91.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 117,320,000.00 USD | 64,550.00 USD | 0.00 USD | `+92.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 117,320,000.00 USD | 1,610.00 USD | 0.00 USD | `+92.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 117,420,000.00 USD | 94,600.00 USD | 0.00 USD | `+93.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 117,420,000.00 USD | 1,070.00 USD | 0.00 USD | `+94.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 117,430,000.00 USD | 11,270.00 USD | 0.00 USD | `+95.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 117,430,000.00 USD | 2,400.00 USD | 0.00 USD | `+95.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 117,470,000.00 USD | 43,750.00 USD | 0.00 USD | `+96.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 117,540,000.00 USD | 64,570.00 USD | 0.00 USD | `+97.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 117,540,000.00 USD | 1,050.00 USD | 0.00 USD | `+97.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 117,850,000.00 USD | 306,600.00 USD | 0.00 USD | `+98.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 117,860,000.00 USD | 11,480.00 USD | 0.00 USD | `+98.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 117,860,000.00 USD | 2,510.00 USD | 0.00 USD | `+99.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 118,040,000.00 USD | 177,400.00 USD | 0.00 USD | `+99.53%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1971.80` | 726,620,000.00 USD | 0.00 USD | 726,620,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD |
| `7D` | `1974.70` | 726,490,000.00 USD | 0.00 USD | 726,490,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD |
| `7D` | `1977.60` | 726,440,000.00 USD | 0.00 USD | 726,440,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1983.40` | 724,200,000.00 USD | 0.00 USD | 724,200,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD |
| `7D` | `1986.30` | 723,990,000.00 USD | 0.00 USD | 723,990,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1989.20` | 720,260,000.00 USD | 0.00 USD | 720,260,000.00 USD | 0.00 USD | 3,100,000.00 USD | 38,060.00 USD |
| `7D` | `1992.10` | 717,130,000.00 USD | 0.00 USD | 717,130,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1995.00` | 715,740,000.00 USD | 0.00 USD | 715,740,000.00 USD | 1,340,000.00 USD | 0.00 USD | 808,380.00 USD |
| `1D` | `1998.10` | 595,580,000.00 USD | 0.00 USD | 595,580,000.00 USD | 219,590.00 USD | 92,480.00 USD | 319,590.00 USD |
| `1D` | `2000.60` | 594,950,000.00 USD | 0.00 USD | 594,950,000.00 USD | 13,780.00 USD | 236,510.00 USD | 586,930.00 USD |
| `1D` | `2003.10` | 594,110,000.00 USD | 0.00 USD | 594,110,000.00 USD | 379,460.00 USD | 601,340.00 USD | 308,610.00 USD |
| `7D` | `2003.70` | 713,590,000.00 USD | 0.00 USD | 713,590,000.00 USD | 0.00 USD | 699,110.00 USD | 0.00 USD |
| `1D` | `2005.60` | 592,820,000.00 USD | 0.00 USD | 592,820,000.00 USD | 493,990.00 USD | 13,410.00 USD | 0.00 USD |
| `7D` | `2006.60` | 712,890,000.00 USD | 0.00 USD | 712,890,000.00 USD | 807,770.00 USD | 42,980.00 USD | 0.00 USD |
| `1D` | `2008.10` | 592,310,000.00 USD | 0.00 USD | 592,310,000.00 USD | 0.00 USD | 570,100.00 USD | 126,940.00 USD |
| `1D` | `2010.60` | 591,620,000.00 USD | 0.00 USD | 591,620,000.00 USD | 484,920.00 USD | 478,500.00 USD | 366,100.00 USD |
| `7D` | `2012.40` | 712,040,000.00 USD | 0.00 USD | 712,040,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD |
| `1D` | `2013.10` | 590,290,000.00 USD | 0.00 USD | 590,290,000.00 USD | 348,720.00 USD | 270,490.00 USD | 21,620.00 USD |
| `1D` | `2015.60` | 589,650,000.00 USD | 0.00 USD | 589,650,000.00 USD | 330,880.00 USD | 605,010.00 USD | 197,000.00 USD |
| `1D` | `2018.10` | 588,510,000.00 USD | 0.00 USD | 588,510,000.00 USD | 537,580.00 USD | 885,870.00 USD | 550,280.00 USD |
| `7D` | `2018.20` | 711,080,000.00 USD | 0.00 USD | 711,080,000.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD |
| `1D` | `2020.60` | 586,540,000.00 USD | 0.00 USD | 586,540,000.00 USD | 911,610.00 USD | 1,280,000.00 USD | 837,150.00 USD |
| `1D` | `2023.10` | 583,510,000.00 USD | 0.00 USD | 583,510,000.00 USD | 792,850.00 USD | 271,500.00 USD | 1,430,000.00 USD |
| `7D` | `2024.00` | 711,060,000.00 USD | 0.00 USD | 711,060,000.00 USD | 1,070,000.00 USD | 0.00 USD | 934,340.00 USD |
| `1D` | `2025.60` | 581,010,000.00 USD | 0.00 USD | 581,010,000.00 USD | 414,330.00 USD | 1,100,000.00 USD | 231,680.00 USD |
| `7D` | `2026.90` | 709,060,000.00 USD | 0.00 USD | 709,060,000.00 USD | 1,100,000.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2028.10` | 579,260,000.00 USD | 0.00 USD | 579,260,000.00 USD | 2,770,000.00 USD | 978,910.00 USD | 615,730.00 USD |
| `7D` | `2029.80` | 707,780,000.00 USD | 0.00 USD | 707,780,000.00 USD | 0.00 USD | 3,320,000.00 USD | 1,080,000.00 USD |
| `1D` | `2030.60` | 574,900,000.00 USD | 0.00 USD | 574,900,000.00 USD | 525,130.00 USD | 366,120.00 USD | 1,060,000.00 USD |
| `7D` | `2032.70` | 703,380,000.00 USD | 0.00 USD | 703,380,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD |
| `1D` | `2033.10` | 572,950,000.00 USD | 0.00 USD | 572,950,000.00 USD | 1,090,000.00 USD | 1,490,000.00 USD | 298,550.00 USD |
| `1D` | `2035.60` | 570,070,000.00 USD | 0.00 USD | 570,070,000.00 USD | 985,830.00 USD | 19,490.00 USD | 165,760.00 USD |
| `7D` | `2035.60` | 701,820,000.00 USD | 0.00 USD | 701,820,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD |
| `1D` | `2038.10` | 568,900,000.00 USD | 0.00 USD | 568,900,000.00 USD | 603,980.00 USD | 458,110.00 USD | 388,420.00 USD |
| `7D` | `2038.50` | 701,490,000.00 USD | 0.00 USD | 701,490,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2040.60` | 567,450,000.00 USD | 0.00 USD | 567,450,000.00 USD | 962,230.00 USD | 178,560.00 USD | 21,940.00 USD |
| `1D` | `2043.10` | 566,280,000.00 USD | 0.00 USD | 566,280,000.00 USD | 0.00 USD | 0.00 USD | 174,920.00 USD |
| `7D` | `2044.30` | 700,030,000.00 USD | 0.00 USD | 700,030,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD |
| `1D` | `2045.60` | 566,110,000.00 USD | 0.00 USD | 566,110,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD |
| `1D` | `2048.10` | 566,080,000.00 USD | 0.00 USD | 566,080,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD |
| `7D` | `2050.10` | 699,740,000.00 USD | 0.00 USD | 699,740,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2050.60` | 565,260,000.00 USD | 0.00 USD | 565,260,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2053.00` | 699,510,000.00 USD | 0.00 USD | 699,510,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2053.10` | 564,150,000.00 USD | 0.00 USD | 564,150,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD |
| `1D` | `2055.60` | 564,120,000.00 USD | 0.00 USD | 564,120,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD |
| `1D` | `2058.10` | 563,790,000.00 USD | 0.00 USD | 563,790,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2058.80` | 697,230,000.00 USD | 0.00 USD | 697,230,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2061.70` | 696,880,000.00 USD | 0.00 USD | 696,880,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `1D` | `2063.10` | 563,030,000.00 USD | 0.00 USD | 563,030,000.00 USD | 0.00 USD | 111,540.00 USD | 530,530.00 USD |
| `7D` | `2064.60` | 691,630,000.00 USD | 0.00 USD | 691,630,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `1D` | `2065.60` | 562,390,000.00 USD | 0.00 USD | 562,390,000.00 USD | 950,540.00 USD | 485,130.00 USD | 0.00 USD |
| `7D` | `2067.50` | 689,160,000.00 USD | 0.00 USD | 689,160,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD |
| `1D` | `2068.10` | 560,960,000.00 USD | 0.00 USD | 560,960,000.00 USD | 0.00 USD | 304,560.00 USD | 0.00 USD |
| `7D` | `2070.40` | 687,520,000.00 USD | 0.00 USD | 687,520,000.00 USD | 3,600,000.00 USD | 2,730,000.00 USD | 1,880,000.00 USD |
| `1D` | `2070.60` | 560,650,000.00 USD | 0.00 USD | 560,650,000.00 USD | 105,210.00 USD | 319,490.00 USD | 0.00 USD |
| `1D` | `2073.10` | 560,230,000.00 USD | 0.00 USD | 560,230,000.00 USD | 0.00 USD | 555,250.00 USD | 420,170.00 USD |
| `7D` | `2073.30` | 679,320,000.00 USD | 0.00 USD | 679,320,000.00 USD | 3,200,000.00 USD | 2,180,000.00 USD | 1,690,000.00 USD |
| `1D` | `2075.60` | 559,250,000.00 USD | 0.00 USD | 559,250,000.00 USD | 379,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2076.20` | 672,250,000.00 USD | 0.00 USD | 672,250,000.00 USD | 4,520,000.00 USD | 5,030,000.00 USD | 4,020,000.00 USD |
| `1D` | `2078.10` | 558,870,000.00 USD | 0.00 USD | 558,870,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD |
| `7D` | `2079.10` | 658,690,000.00 USD | 0.00 USD | 658,690,000.00 USD | 3,560,000.00 USD | 3,000,000.00 USD | 2,060,000.00 USD |
| `1D` | `2080.60` | 558,850,000.00 USD | 0.00 USD | 558,850,000.00 USD | 77,960.00 USD | 29,610.00 USD | 199,420.00 USD |
| `7D` | `2082.00` | 650,070,000.00 USD | 0.00 USD | 650,070,000.00 USD | 4,050,000.00 USD | 1,860,000.00 USD | 2,460,000.00 USD |
| `1D` | `2083.10` | 558,540,000.00 USD | 0.00 USD | 558,540,000.00 USD | 827,940.00 USD | 4,240.00 USD | 211,750.00 USD |
| `7D` | `2084.90` | 641,700,000.00 USD | 0.00 USD | 641,700,000.00 USD | 3,070,000.00 USD | 1,460,000.00 USD | 4,380,000.00 USD |
| `1D` | `2085.60` | 557,500,000.00 USD | 0.00 USD | 557,500,000.00 USD | 691,080.00 USD | 249,220.00 USD | 817,510.00 USD |
| `7D` | `2087.80` | 632,790,000.00 USD | 0.00 USD | 632,790,000.00 USD | 3,310,000.00 USD | 2,260,000.00 USD | 924,970.00 USD |
| `1D` | `2088.10` | 555,740,000.00 USD | 0.00 USD | 555,740,000.00 USD | 525,540.00 USD | 343,300.00 USD | 442,590.00 USD |
| `1D` | `2090.60` | 554,430,000.00 USD | 0.00 USD | 554,430,000.00 USD | 761,770.00 USD | 224,660.00 USD | 446,120.00 USD |
| `7D` | `2090.70` | 626,300,000.00 USD | 0.00 USD | 626,300,000.00 USD | 4,340,000.00 USD | 952,210.00 USD | 6,980,000.00 USD |
| `1D` | `2093.10` | 552,990,000.00 USD | 0.00 USD | 552,990,000.00 USD | 752,390.00 USD | 334,060.00 USD | 673,020.00 USD |
| `7D` | `2093.60` | 614,030,000.00 USD | 0.00 USD | 614,030,000.00 USD | 3,930,000.00 USD | 1,640,000.00 USD | 2,950,000.00 USD |
| `1D` | `2095.60` | 551,230,000.00 USD | 0.00 USD | 551,230,000.00 USD | 1,840,000.00 USD | 1,130,000.00 USD | 1,300,000.00 USD |
| `7D` | `2096.50` | 605,510,000.00 USD | 0.00 USD | 605,510,000.00 USD | 3,210,000.00 USD | 1,980,000.00 USD | 1,290,000.00 USD |
| `1D` | `2098.10` | 546,960,000.00 USD | 0.00 USD | 546,960,000.00 USD | 345,860.00 USD | 488,160.00 USD | 309,770.00 USD |
| `7D` | `2099.40` | 599,030,000.00 USD | 0.00 USD | 599,030,000.00 USD | 2,320,000.00 USD | 3,020,000.00 USD | 2,070,000.00 USD |
| `1D` | `2100.60` | 545,820,000.00 USD | 0.00 USD | 545,820,000.00 USD | 137,320.00 USD | 1,030,000.00 USD | 231,410.00 USD |
| `7D` | `2102.30` | 591,620,000.00 USD | 0.00 USD | 591,620,000.00 USD | 125,250.00 USD | 739,480.00 USD | 2,010,000.00 USD |
| `1D` | `2103.10` | 544,420,000.00 USD | 0.00 USD | 544,420,000.00 USD | 315,200.00 USD | 119,690.00 USD | 306,410.00 USD |
| `7D` | `2105.20` | 588,750,000.00 USD | 0.00 USD | 588,750,000.00 USD | 2,000,000.00 USD | 1,250,000.00 USD | 2,400,000.00 USD |
| `1D` | `2105.60` | 543,680,000.00 USD | 0.00 USD | 543,680,000.00 USD | 3,610,000.00 USD | 1,160,000.00 USD | 1,080,000.00 USD |
| `1D` | `2108.10` | 537,830,000.00 USD | 0.00 USD | 537,830,000.00 USD | 656,240.00 USD | 9,120.00 USD | 96,180.00 USD |
| `7D` | `2108.10` | 583,100,000.00 USD | 0.00 USD | 583,100,000.00 USD | 8,000,000.00 USD | 930,280.00 USD | 1,640,000.00 USD |
| `1D` | `2110.60` | 537,070,000.00 USD | 0.00 USD | 537,070,000.00 USD | 36,110.00 USD | 22,440.00 USD | 6,190.00 USD |
| `7D` | `2111.00` | 572,530,000.00 USD | 0.00 USD | 572,530,000.00 USD | 3,450,000.00 USD | 1,780,000.00 USD | 2,160,000.00 USD |
| `1D` | `2113.10` | 537,000,000.00 USD | 0.00 USD | 537,000,000.00 USD | 866,490.00 USD | 506,690.00 USD | 244,160.00 USD |
| `7D` | `2113.90` | 565,140,000.00 USD | 0.00 USD | 565,140,000.00 USD | 1,080,000.00 USD | 1,810,000.00 USD | 3,370,000.00 USD |
| `1D` | `2115.60` | 535,380,000.00 USD | 0.00 USD | 535,380,000.00 USD | 722,960.00 USD | 400,200.00 USD | 939,960.00 USD |
| `7D` | `2116.80` | 558,870,000.00 USD | 0.00 USD | 558,870,000.00 USD | 2,360,000.00 USD | 2,350,000.00 USD | 1,990,000.00 USD |
| `1D` | `2118.10` | 533,320,000.00 USD | 0.00 USD | 533,320,000.00 USD | 4,580,000.00 USD | 3,940,000.00 USD | 302,800.00 USD |
| `7D` | `2119.70` | 552,180,000.00 USD | 0.00 USD | 552,180,000.00 USD | 12,310,000.00 USD | 5,090,000.00 USD | 2,590,000.00 USD |
| `1D` | `2120.60` | 524,500,000.00 USD | 0.00 USD | 524,500,000.00 USD | 5,670,000.00 USD | 1,980,000.00 USD | 671,270.00 USD |
| `7D` | `2122.60` | 532,200,000.00 USD | 0.00 USD | 532,200,000.00 USD | 4,890,000.00 USD | 4,260,000.00 USD | 1,980,000.00 USD |
| `1D` | `2123.10` | 516,180,000.00 USD | 0.00 USD | 516,180,000.00 USD | 5,450,000.00 USD | 2,370,000.00 USD | 3,140,000.00 USD |
| `7D` | `2125.50` | 521,070,000.00 USD | 0.00 USD | 521,070,000.00 USD | 6,630,000.00 USD | 7,840,000.00 USD | 2,450,000.00 USD |
| `1D` | `2125.60` | 505,220,000.00 USD | 0.00 USD | 505,220,000.00 USD | 5,170,000.00 USD | 3,160,000.00 USD | 837,670.00 USD |
| `1D` | `2128.10` | 496,050,000.00 USD | 0.00 USD | 496,050,000.00 USD | 3,180,000.00 USD | 2,480,000.00 USD | 745,430.00 USD |
| `7D` | `2128.40` | 504,160,000.00 USD | 0.00 USD | 504,160,000.00 USD | 4,290,000.00 USD | 1,960,000.00 USD | 3,980,000.00 USD |
| `1D` | `2130.60` | 489,630,000.00 USD | 0.00 USD | 489,630,000.00 USD | 1,250,000.00 USD | 18,610.00 USD | 1,110,000.00 USD |
| `7D` | `2131.30` | 493,930,000.00 USD | 0.00 USD | 493,930,000.00 USD | 1,980,000.00 USD | 1,850,000.00 USD | 1,360,000.00 USD |
| `1D` | `2133.10` | 487,260,000.00 USD | 0.00 USD | 487,260,000.00 USD | 95,260.00 USD | 255,590.00 USD | 1,530,000.00 USD |
| `7D` | `2134.20` | 488,740,000.00 USD | 0.00 USD | 488,740,000.00 USD | 2,270,000.00 USD | 577,880.00 USD | 308,060.00 USD |
| `1D` | `2135.60` | 485,380,000.00 USD | 0.00 USD | 485,380,000.00 USD | 1,460,000.00 USD | 2,490,000.00 USD | 771,530.00 USD |
| `7D` | `2137.10` | 485,590,000.00 USD | 0.00 USD | 485,590,000.00 USD | 792,450.00 USD | 2,590,000.00 USD | 633,790.00 USD |
| `1D` | `2138.10` | 480,650,000.00 USD | 0.00 USD | 480,650,000.00 USD | 84,550.00 USD | 1,090,000.00 USD | 64,360.00 USD |
| `7D` | `2140.00` | 481,570,000.00 USD | 0.00 USD | 481,570,000.00 USD | 3,470,000.00 USD | 1,700,000.00 USD | 635,670.00 USD |
| `1D` | `2140.60` | 479,420,000.00 USD | 0.00 USD | 479,420,000.00 USD | 1,530,000.00 USD | 898,980.00 USD | 317,350.00 USD |
| `7D` | `2142.90` | 475,760,000.00 USD | 0.00 USD | 475,760,000.00 USD | 1,960,000.00 USD | 804,740.00 USD | 434,750.00 USD |
| `1D` | `2143.10` | 476,670,000.00 USD | 0.00 USD | 476,670,000.00 USD | 1,080,000.00 USD | 3,170,000.00 USD | 1,160,000.00 USD |
| `1D` | `2145.60` | 471,250,000.00 USD | 0.00 USD | 471,250,000.00 USD | 3,170,000.00 USD | 2,360,000.00 USD | 615,080.00 USD |
| `7D` | `2145.80` | 472,560,000.00 USD | 0.00 USD | 472,560,000.00 USD | 2,160,000.00 USD | 1,460,000.00 USD | 1,720,000.00 USD |
| `1D` | `2148.10` | 465,110,000.00 USD | 0.00 USD | 465,110,000.00 USD | 728,710.00 USD | 2,080,000.00 USD | 69,300.00 USD |
| `7D` | `2148.70` | 467,210,000.00 USD | 0.00 USD | 467,210,000.00 USD | 26,270.00 USD | 538,910.00 USD | 399,680.00 USD |
| `1D` | `2150.60` | 462,230,000.00 USD | 0.00 USD | 462,230,000.00 USD | 7,990,000.00 USD | 1,820,000.00 USD | 2,660,000.00 USD |
| `7D` | `2151.60` | 466,250,000.00 USD | 0.00 USD | 466,250,000.00 USD | 11,200,000.00 USD | 363,770.00 USD | 107,200.00 USD |
| `1D` | `2153.10` | 449,770,000.00 USD | 0.00 USD | 449,770,000.00 USD | 2,300,000.00 USD | 3,300,000.00 USD | 2,240,000.00 USD |
| `7D` | `2154.50` | 454,580,000.00 USD | 0.00 USD | 454,580,000.00 USD | 48,150.00 USD | 2,020,000.00 USD | 1,580,000.00 USD |
| `1D` | `2155.60` | 441,930,000.00 USD | 0.00 USD | 441,930,000.00 USD | 4,060,000.00 USD | 3,710,000.00 USD | 3,020,000.00 USD |
| `7D` | `2157.40` | 450,930,000.00 USD | 0.00 USD | 450,930,000.00 USD | 6,950,000.00 USD | 1,330,000.00 USD | 5,050,000.00 USD |
| `1D` | `2158.10` | 431,130,000.00 USD | 0.00 USD | 431,130,000.00 USD | 2,480,000.00 USD | 1,730,000.00 USD | 3,040,000.00 USD |
| `7D` | `2160.30` | 437,600,000.00 USD | 0.00 USD | 437,600,000.00 USD | 309,460.00 USD | 767,490.00 USD | 1,830,000.00 USD |
| `1D` | `2160.60` | 423,880,000.00 USD | 0.00 USD | 423,880,000.00 USD | 4,790,000.00 USD | 6,270,000.00 USD | 2,920,000.00 USD |
| `1D` | `2163.10` | 409,890,000.00 USD | 0.00 USD | 409,890,000.00 USD | 18,720,000.00 USD | 10,400,000.00 USD | 2,810,000.00 USD |
| `7D` | `2163.20` | 434,690,000.00 USD | 0.00 USD | 434,690,000.00 USD | 26,080,000.00 USD | 10,840,000.00 USD | 87,960.00 USD |
| `1D` | `2165.60` | 377,960,000.00 USD | 0.00 USD | 377,960,000.00 USD | 12,300,000.00 USD | 11,850,000.00 USD | 4,210,000.00 USD |
| `7D` | `2166.10` | 397,680,000.00 USD | 0.00 USD | 397,680,000.00 USD | 885,200.00 USD | 14,900,000.00 USD | 2,860,000.00 USD |
| `1D` | `2168.10` | 349,600,000.00 USD | 0.00 USD | 349,600,000.00 USD | 15,930,000.00 USD | 6,950,000.00 USD | 5,130,000.00 USD |
| `7D` | `2169.00` | 379,040,000.00 USD | 0.00 USD | 379,040,000.00 USD | 12,770,000.00 USD | 14,280,000.00 USD | 3,760,000.00 USD |
| `1D` | `2170.60` | 321,590,000.00 USD | 0.00 USD | 321,590,000.00 USD | 24,230,000.00 USD | 8,680,000.00 USD | 7,900,000.00 USD |
| `7D` | `2171.90` | 348,220,000.00 USD | 0.00 USD | 348,220,000.00 USD | 2,110,000.00 USD | 1,650,000.00 USD | 5,570,000.00 USD |
| `1D` | `2173.10` | 280,780,000.00 USD | 0.00 USD | 280,780,000.00 USD | 6,820,000.00 USD | 3,860,000.00 USD | 3,800,000.00 USD |
| `7D` | `2174.80` | 338,890,000.00 USD | 0.00 USD | 338,890,000.00 USD | 34,840,000.00 USD | 1,330,000.00 USD | 3,830,000.00 USD |
| `1D` | `2175.60` | 266,300,000.00 USD | 0.00 USD | 266,300,000.00 USD | 3,680,000.00 USD | 511,180.00 USD | 0.00 USD |
| `7D` | `2177.70` | 298,890,000.00 USD | 0.00 USD | 298,890,000.00 USD | 196,330.00 USD | 267,540.00 USD | 0.00 USD |
| `1D` | `2178.10` | 262,120,000.00 USD | 0.00 USD | 262,120,000.00 USD | 1,290,000.00 USD | 94,350.00 USD | 3,320,000.00 USD |
| `1D` | `2180.60` | 257,410,000.00 USD | 0.00 USD | 257,410,000.00 USD | 3,270,000.00 USD | 4,110,000.00 USD | 5,590,000.00 USD |
| `7D` | `2180.60` | 298,430,000.00 USD | 0.00 USD | 298,430,000.00 USD | 0.00 USD | 0.00 USD | 1,180,000.00 USD |
| `1D` | `2183.10` | 244,440,000.00 USD | 0.00 USD | 244,440,000.00 USD | 637,950.00 USD | 1,320,000.00 USD | 1,260,000.00 USD |
| `7D` | `2183.50` | 297,250,000.00 USD | 0.00 USD | 297,250,000.00 USD | 1,760,000.00 USD | 3,680,000.00 USD | 3,950,000.00 USD |
| `1D` | `2185.60` | 241,230,000.00 USD | 0.00 USD | 241,230,000.00 USD | 2,650,000.00 USD | 2,480,000.00 USD | 4,730,000.00 USD |
| `7D` | `2186.40` | 287,860,000.00 USD | 0.00 USD | 287,860,000.00 USD | 41,350,000.00 USD | 18,930,000.00 USD | 0.00 USD |
| `1D` | `2188.10` | 231,370,000.00 USD | 0.00 USD | 231,370,000.00 USD | 7,340,000.00 USD | 4,820,000.00 USD | 7,930,000.00 USD |
| `7D` | `2189.30` | 227,580,000.00 USD | 0.00 USD | 227,580,000.00 USD | 14,800,000.00 USD | 13,670,000.00 USD | 8,020,000.00 USD |
| `1D` | `2190.60` | 211,280,000.00 USD | 0.00 USD | 211,280,000.00 USD | 6,880,000.00 USD | 3,890,000.00 USD | 4,110,000.00 USD |
| `7D` | `2192.20` | 191,100,000.00 USD | 0.00 USD | 191,100,000.00 USD | 0.00 USD | 21,640,000.00 USD | 0.00 USD |
| `1D` | `2193.10` | 196,400,000.00 USD | 0.00 USD | 196,400,000.00 USD | 6,010,000.00 USD | 6,260,000.00 USD | 1,450,000.00 USD |
| `7D` | `2195.10` | 169,460,000.00 USD | 0.00 USD | 169,460,000.00 USD | 141,070.00 USD | 243,760.00 USD | 8,120,000.00 USD |
| `1D` | `2195.60` | 182,690,000.00 USD | 0.00 USD | 182,690,000.00 USD | 8,230,000.00 USD | 1,230,000.00 USD | 5,630,000.00 USD |
| `7D` | `2198.00` | 160,950,000.00 USD | 0.00 USD | 160,950,000.00 USD | 242,610.00 USD | 1,460,000.00 USD | 2,150,000.00 USD |
| `1D` | `2198.10` | 167,590,000.00 USD | 0.00 USD | 167,590,000.00 USD | 1,110,000.00 USD | 3,160,000.00 USD | 5,050,000.00 USD |
| `1D` | `2200.60` | 158,270,000.00 USD | 0.00 USD | 158,270,000.00 USD | 9,250,000.00 USD | 5,850,000.00 USD | 11,970,000.00 USD |
| `7D` | `2200.90` | 157,110,000.00 USD | 0.00 USD | 157,110,000.00 USD | 4,700,000.00 USD | 266,430.00 USD | 8,690,000.00 USD |
| `1D` | `2203.10` | 131,210,000.00 USD | 0.00 USD | 131,210,000.00 USD | 8,650,000.00 USD | 11,510,000.00 USD | 7,070,000.00 USD |
| `7D` | `2203.80` | 143,450,000.00 USD | 0.00 USD | 143,450,000.00 USD | 5,350,000.00 USD | 4,330,000.00 USD | 12,400,000.00 USD |
| `1D` | `2205.60` | 103,980,000.00 USD | 0.00 USD | 103,980,000.00 USD | 11,830,000.00 USD | 1,530,000.00 USD | 2,370,000.00 USD |
| `7D` | `2206.70` | 121,380,000.00 USD | 0.00 USD | 121,380,000.00 USD | 15,070,000.00 USD | 3,390,000.00 USD | 5,090,000.00 USD |
| `1D` | `2208.10` | 88,240,000.00 USD | 0.00 USD | 88,240,000.00 USD | 8,730,000.00 USD | 6,100,000.00 USD | 3,690,000.00 USD |
| `7D` | `2209.60` | 97,830,000.00 USD | 0.00 USD | 97,830,000.00 USD | 4,550,000.00 USD | 0.00 USD | 9,150,000.00 USD |
| `1D` | `2210.60` | 69,710,000.00 USD | 0.00 USD | 69,710,000.00 USD | 6,870,000.00 USD | 7,030,000.00 USD | 4,650,000.00 USD |
| `7D` | `2212.50` | 84,120,000.00 USD | 0.00 USD | 84,120,000.00 USD | 6,450,000.00 USD | 1,980,000.00 USD | 11,000,000.00 USD |
| `1D` | `2213.10` | 51,150,000.00 USD | 0.00 USD | 51,150,000.00 USD | 9,690,000.00 USD | 6,160,000.00 USD | 1,990,000.00 USD |
| `7D` | `2215.40` | 64,690,000.00 USD | 0.00 USD | 64,690,000.00 USD | 0.00 USD | 0.00 USD | 565,690.00 USD |
| `1D` | `2215.60` | 33,310,000.00 USD | 0.00 USD | 33,310,000.00 USD | 968,510.00 USD | 2,730,000.00 USD | 736,470.00 USD |
| `1D` | `2218.10` | 28,880,000.00 USD | 0.00 USD | 28,880,000.00 USD | 6,820,000.00 USD | 3,040,000.00 USD | 3,320,000.00 USD |
| `7D` | `2218.30` | 64,130,000.00 USD | 0.00 USD | 64,130,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 0.00 USD |
| `1D` | `2220.60` | 15,700,000.00 USD | 0.00 USD | 15,700,000.00 USD | 0.00 USD | 3,570,000.00 USD | 4,410,000.00 USD |
| `7D` | `2221.20` | 41,240,000.00 USD | 0.00 USD | 41,240,000.00 USD | 0.00 USD | 11,780,000.00 USD | 18,240,000.00 USD |
| `1D` | `2223.10` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 0.00 USD | 2,150,000.00 USD | 5,570,000.00 USD |
| `1D` | `2224.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2224.10` | 11,220,000.00 USD | 0.00 USD | 11,220,000.00 USD | 8,610,000.00 USD | 446,880.00 USD | 2,160,000.00 USD |
| `7D` | `2225.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2225.60` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 374,450.00 USD | 1,140,000.00 USD | 147,770.00 USD |
| `7D` | `2227.00` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 524,820.00 USD | 0.00 USD | 7,710,000.00 USD |
| `1D` | `2228.10` | 27,020,000.00 USD | 27,020,000.00 USD | 0.00 USD | 2,770,000.00 USD | 17,080,000.00 USD | 5,500,000.00 USD |
| `7D` | `2229.90` | 29,250,000.00 USD | 29,250,000.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD | 19,080,000.00 USD |
| `1D` | `2230.60` | 67,690,000.00 USD | 67,690,000.00 USD | 0.00 USD | 40,330,000.00 USD | 0.00 USD | 344,090.00 USD |
| `7D` | `2232.80` | 30,210,000.00 USD | 30,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 959,630.00 USD |
| `1D` | `2233.10` | 67,960,000.00 USD | 67,960,000.00 USD | 0.00 USD | 89,990.00 USD | 0.00 USD | 180,290.00 USD |
| `7D` | `2235.70` | 55,460,000.00 USD | 55,460,000.00 USD | 0.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 350,840.00 USD |
| `1D` | `2238.10` | 79,920,000.00 USD | 79,920,000.00 USD | 0.00 USD | 11,960,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2238.60` | 69,520,000.00 USD | 69,520,000.00 USD | 0.00 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2240.60` | 83,180,000.00 USD | 83,180,000.00 USD | 0.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2241.50` | 101,890,000.00 USD | 101,890,000.00 USD | 0.00 USD | 32,370,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2243.10` | 83,950,000.00 USD | 83,950,000.00 USD | 0.00 USD | 271,140.00 USD | 452,920.00 USD | 50,930.00 USD |
| `7D` | `2244.40` | 104,290,000.00 USD | 104,290,000.00 USD | 0.00 USD | 1,860,000.00 USD | 535,080.00 USD | 0.00 USD |
| `1D` | `2245.60` | 92,740,000.00 USD | 92,740,000.00 USD | 0.00 USD | 3,390,000.00 USD | 4,370,000.00 USD | 1,040,000.00 USD |
| `7D` | `2247.30` | 110,470,000.00 USD | 110,470,000.00 USD | 0.00 USD | 1,670,000.00 USD | 1,030,000.00 USD | 3,480,000.00 USD |
| `1D` | `2248.10` | 101,900,000.00 USD | 101,900,000.00 USD | 0.00 USD | 2,560,000.00 USD | 3,510,000.00 USD | 3,090,000.00 USD |
| `7D` | `2250.20` | 121,280,000.00 USD | 121,280,000.00 USD | 0.00 USD | 3,160,000.00 USD | 7,420,000.00 USD | 228,120.00 USD |
| `1D` | `2250.60` | 108,860,000.00 USD | 108,860,000.00 USD | 0.00 USD | 6,430,000.00 USD | 475,410.00 USD | 55,780.00 USD |
| `1D` | `2253.10` | 114,720,000.00 USD | 114,720,000.00 USD | 0.00 USD | 943,690.00 USD | 3,480,000.00 USD | 1,440,000.00 USD |
| `7D` | `2253.10` | 143,340,000.00 USD | 143,340,000.00 USD | 0.00 USD | 10,600,000.00 USD | 11,240,000.00 USD | 216,090.00 USD |
| `1D` | `2255.60` | 146,550,000.00 USD | 146,550,000.00 USD | 0.00 USD | 16,490,000.00 USD | 6,560,000.00 USD | 8,780,000.00 USD |
| `7D` | `2256.00` | 178,870,000.00 USD | 178,870,000.00 USD | 0.00 USD | 17,810,000.00 USD | 10,520,000.00 USD | 7,190,000.00 USD |
| `1D` | `2258.10` | 175,540,000.00 USD | 175,540,000.00 USD | 0.00 USD | 18,480,000.00 USD | 7,740,000.00 USD | 2,770,000.00 USD |
| `7D` | `2258.90` | 203,150,000.00 USD | 203,150,000.00 USD | 0.00 USD | 11,860,000.00 USD | 8,380,000.00 USD | 4,040,000.00 USD |
| `1D` | `2260.60` | 196,990,000.00 USD | 196,990,000.00 USD | 0.00 USD | 9,590,000.00 USD | 9,340,000.00 USD | 2,510,000.00 USD |
| `7D` | `2261.80` | 211,600,000.00 USD | 211,600,000.00 USD | 0.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 280,820.00 USD |
| `1D` | `2263.10` | 229,550,000.00 USD | 229,550,000.00 USD | 0.00 USD | 14,130,000.00 USD | 10,400,000.00 USD | 8,040,000.00 USD |
| `7D` | `2264.70` | 214,330,000.00 USD | 214,330,000.00 USD | 0.00 USD | 0.00 USD | 2,510,000.00 USD | 218,310.00 USD |
| `1D` | `2265.60` | 252,640,000.00 USD | 252,640,000.00 USD | 0.00 USD | 3,490,000.00 USD | 9,120,000.00 USD | 10,480,000.00 USD |
| `7D` | `2267.60` | 226,640,000.00 USD | 226,640,000.00 USD | 0.00 USD | 196,330.00 USD | 5,790,000.00 USD | 6,330,000.00 USD |
| `1D` | `2268.10` | 298,000,000.00 USD | 298,000,000.00 USD | 0.00 USD | 19,910,000.00 USD | 11,870,000.00 USD | 13,590,000.00 USD |
| `7D` | `2270.50` | 275,830,000.00 USD | 275,830,000.00 USD | 0.00 USD | 26,480,000.00 USD | 3,500,000.00 USD | 19,220,000.00 USD |
| `1D` | `2270.60` | 326,950,000.00 USD | 326,950,000.00 USD | 0.00 USD | 7,630,000.00 USD | 9,260,000.00 USD | 12,050,000.00 USD |
| `1D` | `2273.10` | 351,660,000.00 USD | 351,660,000.00 USD | 0.00 USD | 14,930,000.00 USD | 5,280,000.00 USD | 4,490,000.00 USD |
| `7D` | `2273.40` | 279,440,000.00 USD | 279,440,000.00 USD | 0.00 USD | 373,530.00 USD | 362,150.00 USD | 2,870,000.00 USD |
| `1D` | `2275.60` | 408,680,000.00 USD | 408,680,000.00 USD | 0.00 USD | 33,630,000.00 USD | 17,390,000.00 USD | 6,000,000.00 USD |
| `7D` | `2276.30` | 310,270,000.00 USD | 310,270,000.00 USD | 0.00 USD | 24,150,000.00 USD | 6,680,000.00 USD | 0.00 USD |
| `1D` | `2278.10` | 437,070,000.00 USD | 437,070,000.00 USD | 0.00 USD | 4,240,000.00 USD | 10,420,000.00 USD | 13,740,000.00 USD |
| `7D` | `2279.20` | 352,090,000.00 USD | 352,090,000.00 USD | 0.00 USD | 3,230,000.00 USD | 24,610,000.00 USD | 13,990,000.00 USD |
| `1D` | `2280.60` | 492,350,000.00 USD | 492,350,000.00 USD | 0.00 USD | 31,330,000.00 USD | 16,100,000.00 USD | 7,850,000.00 USD |
| `7D` | `2282.10` | 435,140,000.00 USD | 435,140,000.00 USD | 0.00 USD | 0.00 USD | 69,380,000.00 USD | 13,670,000.00 USD |
| `1D` | `2283.10` | 549,200,000.00 USD | 549,200,000.00 USD | 0.00 USD | 26,480,000.00 USD | 20,540,000.00 USD | 9,830,000.00 USD |
| `7D` | `2285.00` | 471,740,000.00 USD | 471,740,000.00 USD | 0.00 USD | 6,610,000.00 USD | 29,850,000.00 USD | 140,410.00 USD |
| `1D` | `2285.60` | 574,720,000.00 USD | 574,720,000.00 USD | 0.00 USD | 7,480,000.00 USD | 12,460,000.00 USD | 5,580,000.00 USD |
| `7D` | `2287.90` | 498,490,000.00 USD | 498,490,000.00 USD | 0.00 USD | 8,380,000.00 USD | 6,500,000.00 USD | 11,870,000.00 USD |
| `1D` | `2288.10` | 598,270,000.00 USD | 598,270,000.00 USD | 0.00 USD | 11,850,000.00 USD | 4,100,000.00 USD | 7,600,000.00 USD |
| `1D` | `2290.60` | 640,110,000.00 USD | 640,110,000.00 USD | 0.00 USD | 18,820,000.00 USD | 15,090,000.00 USD | 7,930,000.00 USD |
| `7D` | `2290.80` | 511,690,000.00 USD | 511,690,000.00 USD | 0.00 USD | 4,310,000.00 USD | 3,340,000.00 USD | 5,550,000.00 USD |
| `1D` | `2293.10` | 668,750,000.00 USD | 668,750,000.00 USD | 0.00 USD | 14,100,000.00 USD | 5,110,000.00 USD | 9,430,000.00 USD |
| `7D` | `2293.70` | 529,040,000.00 USD | 529,040,000.00 USD | 0.00 USD | 8,930,000.00 USD | 0.00 USD | 8,410,000.00 USD |
| `1D` | `2295.60` | 699,580,000.00 USD | 699,580,000.00 USD | 0.00 USD | 10,130,000.00 USD | 13,170,000.00 USD | 7,530,000.00 USD |
| `7D` | `2296.60` | 584,710,000.00 USD | 584,710,000.00 USD | 0.00 USD | 28,890,000.00 USD | 9,570,000.00 USD | 17,210,000.00 USD |
| `1D` | `2298.10` | 754,870,000.00 USD | 754,870,000.00 USD | 0.00 USD | 32,970,000.00 USD | 15,200,000.00 USD | 7,120,000.00 USD |
| `7D` | `2299.50` | 630,090,000.00 USD | 630,090,000.00 USD | 0.00 USD | 18,930,000.00 USD | 20,670,000.00 USD | 5,780,000.00 USD |
| `1D` | `2300.60` | 787,960,000.00 USD | 787,960,000.00 USD | 0.00 USD | 8,900,000.00 USD | 10,180,000.00 USD | 14,010,000.00 USD |
| `7D` | `2302.40` | 685,030,000.00 USD | 685,030,000.00 USD | 0.00 USD | 26,960,000.00 USD | 11,130,000.00 USD | 16,850,000.00 USD |
| `1D` | `2303.10` | 818,890,000.00 USD | 818,890,000.00 USD | 0.00 USD | 17,940,000.00 USD | 5,770,000.00 USD | 7,220,000.00 USD |
| `7D` | `2305.30` | 709,190,000.00 USD | 709,190,000.00 USD | 0.00 USD | 6,340,000.00 USD | 6,960,000.00 USD | 10,860,000.00 USD |
| `1D` | `2305.60` | 853,920,000.00 USD | 853,920,000.00 USD | 0.00 USD | 12,190,000.00 USD | 15,330,000.00 USD | 7,500,000.00 USD |
| `1D` | `2308.10` | 863,640,000.00 USD | 863,640,000.00 USD | 0.00 USD | 4,390,000.00 USD | 3,450,000.00 USD | 1,890,000.00 USD |
| `7D` | `2308.20` | 713,350,000.00 USD | 713,350,000.00 USD | 0.00 USD | 1,240,000.00 USD | 2,780,000.00 USD | 134,160.00 USD |
| `1D` | `2310.60` | 882,360,000.00 USD | 882,360,000.00 USD | 0.00 USD | 5,990,000.00 USD | 2,140,000.00 USD | 10,590,000.00 USD |
| `7D` | `2311.10` | 743,840,000.00 USD | 743,840,000.00 USD | 0.00 USD | 11,560,000.00 USD | 2,790,000.00 USD | 16,150,000.00 USD |
| `1D` | `2313.10` | 899,160,000.00 USD | 899,160,000.00 USD | 0.00 USD | 6,090,000.00 USD | 8,970,000.00 USD | 1,740,000.00 USD |
| `7D` | `2314.00` | 752,080,000.00 USD | 752,080,000.00 USD | 0.00 USD | 0.00 USD | 7,460,000.00 USD | 778,500.00 USD |
| `1D` | `2315.60` | 931,740,000.00 USD | 931,740,000.00 USD | 0.00 USD | 9,820,000.00 USD | 15,740,000.00 USD | 7,020,000.00 USD |
| `7D` | `2316.90` | 760,550,000.00 USD | 760,550,000.00 USD | 0.00 USD | 1,020,000.00 USD | 6,410,000.00 USD | 1,040,000.00 USD |
| `1D` | `2318.10` | 946,570,000.00 USD | 946,570,000.00 USD | 0.00 USD | 5,910,000.00 USD | 6,680,000.00 USD | 2,230,000.00 USD |
| `7D` | `2319.80` | 787,050,000.00 USD | 787,050,000.00 USD | 0.00 USD | 5,530,000.00 USD | 13,080,000.00 USD | 7,890,000.00 USD |
| `1D` | `2320.60` | 966,780,000.00 USD | 966,780,000.00 USD | 0.00 USD | 5,860,000.00 USD | 11,510,000.00 USD | 2,840,000.00 USD |
| `7D` | `2322.70` | 799,910,000.00 USD | 799,910,000.00 USD | 0.00 USD | 5,850,000.00 USD | 5,180,000.00 USD | 1,830,000.00 USD |
| `1D` | `2323.10` | 987,880,000.00 USD | 987,880,000.00 USD | 0.00 USD | 4,360,000.00 USD | 12,060,000.00 USD | 4,670,000.00 USD |
| `1D` | `2325.60` | 998,240,000.00 USD | 998,240,000.00 USD | 0.00 USD | 2,050,000.00 USD | 6,790,000.00 USD | 1,530,000.00 USD |
| `7D` | `2325.60` | 815,940,000.00 USD | 815,940,000.00 USD | 0.00 USD | 6,590,000.00 USD | 1,040,000.00 USD | 8,390,000.00 USD |
| `1D` | `2328.10` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 1,250,000.00 USD | 1,240,000.00 USD | 4,510,000.00 USD |
| `7D` | `2328.50` | 828,190,000.00 USD | 828,190,000.00 USD | 0.00 USD | 3,860,000.00 USD | 363,770.00 USD | 8,030,000.00 USD |
| `1D` | `2330.60` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 11,680,000.00 USD | 3,110,000.00 USD | 2,550,000.00 USD |
| `7D` | `2331.40` | 851,870,000.00 USD | 851,870,000.00 USD | 0.00 USD | 23,030,000.00 USD | 593,900.00 USD | 54,580.00 USD |
| `1D` | `2333.10` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 0.00 USD | 2,710,000.00 USD | 3,760,000.00 USD | 8,420,000.00 USD |
| `7D` | `2334.30` | 895,910,000.00 USD | 895,910,000.00 USD | 0.00 USD | 16,820,000.00 USD | 15,180,000.00 USD | 12,040,000.00 USD |
| `1D` | `2335.60` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 13,920,000.00 USD | 3,880,000.00 USD | 5,250,000.00 USD |
| `7D` | `2337.20` | 934,100,000.00 USD | 934,100,000.00 USD | 0.00 USD | 28,890,000.00 USD | 4,650,000.00 USD | 4,650,000.00 USD |
| `1D` | `2338.10` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 6,320,000.00 USD | 1,830,000.00 USD | 5,440,000.00 USD |
| `7D` | `2340.10` | 974,710,000.00 USD | 974,710,000.00 USD | 0.00 USD | 10,400,000.00 USD | 10,610,000.00 USD | 19,610,000.00 USD |
| `1D` | `2340.60` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 10,960,000.00 USD | 5,840,000.00 USD | 9,310,000.00 USD |
| `7D` | `2343.00` | 995,730,000.00 USD | 995,730,000.00 USD | 0.00 USD | 5,030,000.00 USD | 12,160,000.00 USD | 3,840,000.00 USD |
| `1D` | `2343.10` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 10,420,000.00 USD | 8,840,000.00 USD | 3,740,000.00 USD |
| `1D` | `2345.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 3,680,000.00 USD | 3,280,000.00 USD | 8,910,000.00 USD |
| `7D` | `2345.90` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 1,350,000.00 USD | 16,220,000.00 USD | 15,530,000.00 USD |
| `1D` | `2348.10` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 4,920,000.00 USD | 4,640,000.00 USD | 2,760,000.00 USD |
| `7D` | `2348.80` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 1,060,000.00 USD | 9,500,000.00 USD | 20,210,000.00 USD |
| `1D` | `2350.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 25,880,000.00 USD | 6,920,000.00 USD | 10,130,000.00 USD |
| `7D` | `2351.70` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 2,430,000.00 USD | 19,600,000.00 USD | 10,630,000.00 USD |
| `1D` | `2353.10` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 3,960,000.00 USD | 2,550,000.00 USD | 1,640,000.00 USD |
| `7D` | `2354.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 10,390,000.00 USD | 34,750,000.00 USD | 1,500,000.00 USD |
| `1D` | `2355.60` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 3,840,000.00 USD | 3,430,000.00 USD | 951,670.00 USD |
| `7D` | `2357.50` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 13,850,000.00 USD | 7,240,000.00 USD | 6,010,000.00 USD |
| `1D` | `2358.10` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 4,740,000.00 USD | 4,470,000.00 USD | 5,290,000.00 USD |
| `7D` | `2360.40` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 4,470,000.00 USD | 3,430,000.00 USD | 254,850.00 USD |
| `1D` | `2360.60` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 9,930,000.00 USD | 3,880,000.00 USD | 3,640,000.00 USD |
| `1D` | `2363.10` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 5,580,000.00 USD | 9,200,000.00 USD | 7,890,000.00 USD |
| `7D` | `2363.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 4,570,000.00 USD | 373,740.00 USD | 6,830,000.00 USD |
| `1D` | `2365.60` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 4,890,000.00 USD | 1,170,000.00 USD | 3,680,000.00 USD |
| `7D` | `2366.20` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 4,210,000.00 USD |
| `1D` | `2368.10` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 4,190,000.00 USD | 3,330,000.00 USD | 2,220,000.00 USD |
| `7D` | `2369.10` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 21,280,000.00 USD | 475,460.00 USD | 4,120,000.00 USD |
| `1D` | `2370.60` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 13,960,000.00 USD | 5,840,000.00 USD | 5,740,000.00 USD |
| `7D` | `2372.00` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 0.00 USD | 15,540,000.00 USD | 0.00 USD | 51,280,000.00 USD |
| `1D` | `2373.10` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 12,450,000.00 USD | 2,600,000.00 USD | 6,690,000.00 USD |
| `7D` | `2374.90` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD |
| `1D` | `2375.60` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 7,590,000.00 USD | 1,830,000.00 USD | 1,380,000.00 USD |
| `7D` | `2377.80` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 11,180,000.00 USD | 6,190,000.00 USD | 18,380,000.00 USD |
| `1D` | `2378.10` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 1,650,000.00 USD | 1,990,000.00 USD | 5,990,000.00 USD |
| `1D` | `2380.60` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 6,120,000.00 USD | 6,700,000.00 USD | 5,230,000.00 USD |
| `7D` | `2380.70` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 4,420,000.00 USD | 2,590,000.00 USD | 19,130,000.00 USD |
| `1D` | `2383.10` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 15,730,000.00 USD | 9,480,000.00 USD | 10,570,000.00 USD |
| `7D` | `2383.60` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 8,840,000.00 USD | 17,490,000.00 USD | 35,140,000.00 USD |
| `1D` | `2385.60` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 7,510,000.00 USD | 10,450,000.00 USD | 3,690,000.00 USD |
| `7D` | `2386.50` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 17,480,000.00 USD | 37,880,000.00 USD | 38,780,000.00 USD |
| `1D` | `2388.10` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 12,620,000.00 USD | 5,690,000.00 USD | 4,190,000.00 USD |
| `7D` | `2389.40` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 6,030,000.00 USD | 35,920,000.00 USD | 31,990,000.00 USD |
| `1D` | `2390.60` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 0.00 USD | 1,700,000.00 USD | 5,130,000.00 USD | 52,390.00 USD |
| `7D` | `2392.30` | 1,720,000,000.00 USD | 1,720,000,000.00 USD | 0.00 USD | 26,840,000.00 USD | 45,530,000.00 USD | 39,190,000.00 USD |
| `1D` | `2393.10` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 2,570,000.00 USD | 2,220,000.00 USD | 3,320,000.00 USD |
| `7D` | `2395.20` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 0.00 USD | 41,200,000.00 USD | 24,950,000.00 USD | 29,410,000.00 USD |
| `1D` | `2395.60` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 2,120,000.00 USD | 1,450,000.00 USD | 2,700,000.00 USD |
| `1D` | `2398.10` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 3,720,000.00 USD | 2,870,000.00 USD |
| `7D` | `2398.10` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 0.00 USD | 35,750,000.00 USD | 38,130,000.00 USD | 23,590,000.00 USD |
| `1D` | `2400.60` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 0.00 USD | 944,200.00 USD | 637,690.00 USD | 1,390,000.00 USD |
| `7D` | `2401.00` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 0.00 USD | 40,240,000.00 USD | 25,000,000.00 USD | 25,750,000.00 USD |
| `1D` | `2403.10` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 0.00 USD | 1,200,000.00 USD | 467,060.00 USD | 564,470.00 USD |
| `7D` | `2403.90` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 0.00 USD | 57,170,000.00 USD | 25,580,000.00 USD | 30,410,000.00 USD |
| `1D` | `2405.60` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 0.00 USD | 7,730,000.00 USD | 3,300,000.00 USD | 5,000,000.00 USD |
| `7D` | `2406.80` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 25,430,000.00 USD | 33,580,000.00 USD | 16,510,000.00 USD |
| `1D` | `2408.10` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 0.00 USD | 5,840,000.00 USD | 3,520,000.00 USD | 1,850,000.00 USD |
| `7D` | `2409.70` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 27,030,000.00 USD | 27,370,000.00 USD | 25,790,000.00 USD |
| `1D` | `2410.60` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 4,650,000.00 USD | 4,210,000.00 USD | 4,180,000.00 USD |
| `7D` | `2412.60` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 16,670,000.00 USD | 15,260,000.00 USD | 15,070,000.00 USD |
| `1D` | `2413.10` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 5,150,000.00 USD | 3,250,000.00 USD | 1,280,000.00 USD |
| `7D` | `2415.50` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 0.00 USD | 23,150,000.00 USD | 19,800,000.00 USD | 26,990,000.00 USD |
| `1D` | `2415.60` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 0.00 USD | 2,990,000.00 USD | 2,210,000.00 USD | 3,210,000.00 USD |
| `1D` | `2418.10` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 2,660,000.00 USD | 2,070,000.00 USD | 1,390,000.00 USD |
| `7D` | `2418.40` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 0.00 USD | 27,090,000.00 USD | 11,140,000.00 USD | 17,450,000.00 USD |
| `1D` | `2420.60` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 6,490,000.00 USD | 4,150,000.00 USD | 4,100,000.00 USD |
| `7D` | `2421.30` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 0.00 USD | 21,290,000.00 USD | 20,900,000.00 USD | 12,200,000.00 USD |
| `1D` | `2423.10` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 770,750.00 USD | 1,540,000.00 USD | 3,520,000.00 USD |
| `7D` | `2424.20` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 0.00 USD | 19,140,000.00 USD | 18,390,000.00 USD | 23,330,000.00 USD |
| `1D` | `2425.60` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 1,280,000.00 USD | 694,550.00 USD | 11,160.00 USD |
| `7D` | `2427.10` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 18,590,000.00 USD | 9,810,000.00 USD | 13,000,000.00 USD |
| `1D` | `2428.10` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 1,610,000.00 USD | 1,450,000.00 USD | 738,520.00 USD |
| `7D` | `2430.00` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 7,100,000.00 USD | 14,510,000.00 USD | 7,560,000.00 USD |
| `1D` | `2430.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 1,330,000.00 USD | 2,120,000.00 USD | 1,220,000.00 USD |
| `7D` | `2432.90` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 16,380,000.00 USD | 5,350,000.00 USD | 5,450,000.00 USD |
| `1D` | `2433.10` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 3,570,000.00 USD | 2,130,000.00 USD | 1,030,000.00 USD |
| `1D` | `2435.60` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 1,920,000.00 USD | 623,860.00 USD | 1,030,000.00 USD |
| `7D` | `2435.80` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 6,050,000.00 USD | 3,000,000.00 USD | 5,020,000.00 USD |
| `1D` | `2438.10` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 517,090.00 USD | 15,480.00 USD |
| `7D` | `2438.70` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 10,300,000.00 USD | 9,480,000.00 USD | 6,740,000.00 USD |
| `1D` | `2440.60` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,190,000.00 USD | 858,540.00 USD |
| `7D` | `2441.60` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 0.00 USD | 9,610,000.00 USD | 3,820,000.00 USD | 8,990,000.00 USD |
| `1D` | `2443.10` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 1,060,000.00 USD | 31,110.00 USD | 747,370.00 USD |
| `7D` | `2444.50` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 0.00 USD | 7,520,000.00 USD | 10,650,000.00 USD | 8,800,000.00 USD |
| `1D` | `2445.60` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 234,410.00 USD | 703,990.00 USD | 755,960.00 USD |
| `7D` | `2447.40` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 11,080,000.00 USD | 3,020,000.00 USD | 12,010,000.00 USD |
| `1D` | `2448.10` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 938,360.00 USD | 888,690.00 USD | 995,880.00 USD |
| `7D` | `2450.30` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 8,460,000.00 USD | 6,720,000.00 USD | 10,020,000.00 USD |
| `1D` | `2450.60` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 1,860,000.00 USD | 69,580.00 USD | 371,600.00 USD |
| `1D` | `2453.10` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 2,000,000.00 USD | 2,610,000.00 USD |
| `7D` | `2453.20` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 7,290,000.00 USD | 3,760,000.00 USD | 3,580,000.00 USD |
| `1D` | `2455.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 2,260,000.00 USD | 1,970,000.00 USD | 489,590.00 USD |
| `7D` | `2456.10` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 5,780,000.00 USD | 5,730,000.00 USD | 6,720,000.00 USD |
| `1D` | `2458.10` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 1,180,000.00 USD | 1,850,000.00 USD | 674,150.00 USD |
| `7D` | `2459.00` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 5,530,000.00 USD | 6,340,000.00 USD | 6,940,000.00 USD |
| `1D` | `2460.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 1,530,000.00 USD | 1,390,000.00 USD | 388,420.00 USD |
| `7D` | `2461.90` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 5,190,000.00 USD | 6,700,000.00 USD | 6,560,000.00 USD |
| `1D` | `2463.10` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 330,880.00 USD | 618,870.00 USD | 1,020,000.00 USD |
| `7D` | `2464.80` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 6,130,000.00 USD | 2,500,000.00 USD | 2,800,000.00 USD |
| `1D` | `2465.60` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 537,580.00 USD | 1,100,000.00 USD | 339,180.00 USD |
| `7D` | `2467.70` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 3,400,000.00 USD | 2,500,000.00 USD | 45,590.00 USD |
| `1D` | `2468.10` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 326,370.00 USD | 1,950,000.00 USD | 377,900.00 USD |
| `1D` | `2470.60` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 1,380,000.00 USD | 475,680.00 USD | 1,480,000.00 USD |
| `7D` | `2470.60` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 3,960,000.00 USD | 2,050,000.00 USD | 522,210.00 USD |
| `1D` | `2473.10` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 0.00 USD | 92,950.00 USD | 1,110,000.00 USD |
| `7D` | `2473.50` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 5,300,000.00 USD | 2,920,000.00 USD | 3,180,000.00 USD |
| `1D` | `2475.60` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 0.00 USD | 339,190.00 USD | 1,100,000.00 USD | 103,970.00 USD |
| `1D` | `2476.40` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 0.00 USD | 232,420.00 USD | 0.00 USD | 156,140.00 USD |
| `7D` | `2476.40` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 2,070,000.00 USD | 2,410,000.00 USD | 872,130.00 USD |
| `7D` | `2479.30` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 3,070,000.00 USD | 4,940,000.00 USD | 540,990.00 USD |
| `7D` | `2482.20` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 601,420.00 USD | 2,170,000.00 USD | 1,050,000.00 USD |
| `7D` | `2485.10` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD |
| `7D` | `2488.00` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 0.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD |
| `7D` | `2490.90` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 0.00 USD | 2,180,000.00 USD | 301,010.00 USD | 137,010.00 USD |
| `7D` | `2493.80` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 0.00 USD | 1,200,000.00 USD | 733,870.00 USD | 1,840,000.00 USD |
| `7D` | `2496.70` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 773,650.00 USD | 812,060.00 USD | 4,160,000.00 USD |
| `7D` | `2499.60` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 0.00 USD | 752,070.00 USD | 92,150.00 USD |
| `7D` | `2502.50` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 0.00 USD | 55,050.00 USD | 125,600.00 USD |
| `7D` | `2505.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2508.30` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `28.37B` | Total OI Tokens: `12,766,428.0 ETH`
  * 1h OI Change: `-0.65%` | 4h OI Change: `-2.49%` | 24h OI Change: `-6.05%`
  * Exchange Breakdown: Binance=`8.38B` | Bybit=`2.08B` | OKX=`1.75B` | Hyperliquid=`2.34B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-145.73K` | Last 24h: `195.10K` | Last 3d: `5.21M` | Last 7d: `11.81M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0035%` | **USDT OKX** | `-0.0045%` |
| **USDT Bybit** | `0.0006%` | **USDT KuCoin** | `-0.0052%` |
| **USDT MEXC** | `-0.0036%` | **USDT BingX** | `0.0006%` |
| **USDT Gate** | `0.0095%` | **USDT Bitget** | `0.0003%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0014%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `40.26%` | `59.74%` | `0.67` | 713,110,000.00 USD |
| `15M` | `Binance` | `46.72%` | `53.28%` | `0.88` | 185,390,000.00 USD |
| `15M` | `OKX` | `39.29%` | `60.71%` | `0.65` | 93,770,000.00 USD |
| `15M` | `Bybit` | `35.57%` | `64.43%` | `0.55` | 48,780,000.00 USD |
| `15M` | `KuCoin` | `26.97%` | `73.03%` | `0.37` | 1,820,000.00 USD |
| `15M` | `Gate` | `47.18%` | `52.82%` | `0.89` | 73,580,000.00 USD |
| `15M` | `Bitget` | `42.27%` | `57.73%` | `0.73` | 36,600,000.00 USD |
| `15M` | `BingX` | `51.54%` | `48.46%` | `1.06` | 14,320,000.00 USD |
| `15M` | `MEXC` | `42.57%` | `57.43%` | `0.74` | 34,550,000.00 USD |
| `15M` | `Bitunix` | `47.54%` | `52.46%` | `0.91` | 29,610,000.00 USD |
| `15M` | `Hyperliquid` | `66.04%` | `33.96%` | `1.94` | 44,370,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `81.24%` | `18.76%` | `4.33` | 6,740,000.00 USD |
| `15M` | `Crypto.com` | `46.51%` | `53.49%` | `0.87` | 2,800,000.00 USD |
| `15M` | `WhiteBIT` | `0.51%` | `99.49%` | `0.01` | 88,330,000.00 USD |
| `15M` | `HTX` | `35.9%` | `64.1%` | `0.56` | 2,170,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `47.09%` | `52.91%` | `0.89` | 32,110,000.00 USD |
| `15M` | `Bitfinex` | `24.6%` | `75.4%` | `0.33` | 478,530.00 USD |
| `15M` | `Kraken` | `24.7%` | `75.3%` | `0.33` | 4,700,000.00 USD |
| `15M` | `Aster` | `24.55%` | `75.45%` | `0.33` | 4,120,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `53.81%` | `46.19%` | `1.16` | 8,880,000.00 USD |
| `15M` | `Whale Positions` | `46.72%` | `53.28%` | `0.88` | 185,390,000.00 USD |
| `15M` | `Global Accounts` | `40.26%` | `59.74%` | `0.67` | 713,110,000.00 USD |
| `1H` | `ETH` | `41.94%` | `58.06%` | `0.72` | 2,360,000,000.00 USD |
| `1H` | `Binance` | `41.19%` | `58.81%` | `0.70` | 645,320,000.00 USD |
| `1H` | `OKX` | `43.54%` | `56.46%` | `0.77` | 344,640,000.00 USD |
| `1H` | `Bybit` | `42.91%` | `57.09%` | `0.75` | 223,650,000.00 USD |
| `1H` | `KuCoin` | `45.42%` | `54.58%` | `0.83` | 7,930,000.00 USD |
| `1H` | `Gate` | `50.52%` | `49.48%` | `1.02` | 230,130,000.00 USD |
| `1H` | `Bitget` | `43.7%` | `56.3%` | `0.78` | 121,560,000.00 USD |
| `1H` | `BingX` | `49.61%` | `50.39%` | `0.98` | 47,490,000.00 USD |
| `1H` | `MEXC` | `37.68%` | `62.32%` | `0.60` | 131,640,000.00 USD |
| `1H` | `Bitunix` | `51.12%` | `48.88%` | `1.05` | 107,470,000.00 USD |
| `1H` | `Hyperliquid` | `34.26%` | `65.74%` | `0.52` | 176,690,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.7%` | `46.3%` | `1.16` | 46,480,000.00 USD |
| `1H` | `Crypto.com` | `44.72%` | `55.28%` | `0.81` | 7,710,000.00 USD |
| `1H` | `WhiteBIT` | `6.59%` | `93.41%` | `0.07` | 94,730,000.00 USD |
| `1H` | `HTX` | `49.82%` | `50.18%` | `0.99` | 7,970,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `50.36%` | `49.64%` | `1.01` | 111,830,000.00 USD |
| `1H` | `Bitfinex` | `32.88%` | `67.12%` | `0.49` | 1,280,000.00 USD |
| `1H` | `Kraken` | `27.29%` | `72.71%` | `0.38` | 17,630,000.00 USD |
| `1H` | `Aster` | `32.34%` | `67.66%` | `0.48` | 16,110,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `53.21%` | `46.79%` | `1.14` | 23,310,000.00 USD |
| `1H` | `Whale Positions` | `41.19%` | `58.81%` | `0.70` | 645,320,000.00 USD |
| `1H` | `Global Accounts` | `41.94%` | `58.06%` | `0.72` | 2,360,000,000.00 USD |
| `4H` | `ETH` | `44.14%` | `55.86%` | `0.79` | 9,810,000,000.00 USD |
| `4H` | `Binance` | `43.16%` | `56.84%` | `0.76` | 2,940,000,000.00 USD |
| `4H` | `OKX` | `45.07%` | `54.93%` | `0.82` | 1,410,000,000.00 USD |
| `4H` | `Bybit` | `41.28%` | `58.72%` | `0.70` | 843,220,000.00 USD |
| `4H` | `KuCoin` | `43.77%` | `56.23%` | `0.78` | 23,190,000.00 USD |
| `4H` | `Gate` | `48.79%` | `51.21%` | `0.95` | 960,900,000.00 USD |
| `4H` | `Bitget` | `43.41%` | `56.59%` | `0.77` | 451,130,000.00 USD |
| `4H` | `BingX` | `41.24%` | `58.76%` | `0.70` | 188,620,000.00 USD |
| `4H` | `MEXC` | `41.6%` | `58.4%` | `0.71` | 429,100,000.00 USD |
| `4H` | `Bitunix` | `43.94%` | `56.06%` | `0.78` | 374,830,000.00 USD |
| `4H` | `Hyperliquid` | `36.71%` | `63.29%` | `0.58` | 547,690,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.75%` | `49.25%` | `1.03` | 696,280,000.00 USD |
| `4H` | `Crypto.com` | `45.74%` | `54.26%` | `0.84` | 30,240,000.00 USD |
| `4H` | `WhiteBIT` | `27.13%` | `72.87%` | `0.37` | 203,450,000.00 USD |
| `4H` | `HTX` | `44.47%` | `55.53%` | `0.80` | 35,140,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.41%` | `48.59%` | `1.06` | 449,090,000.00 USD |
| `4H` | `Bitfinex` | `31.3%` | `68.7%` | `0.46` | 5,210,000.00 USD |
| `4H` | `Kraken` | `39.11%` | `60.89%` | `0.64` | 24,300,000.00 USD |
| `4H` | `Aster` | `48.4%` | `51.6%` | `0.94` | 83,550,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.08%` | `46.92%` | `1.13` | 115,900,000.00 USD |
| `4H` | `Whale Positions` | `43.16%` | `56.84%` | `0.76` | 2,940,000,000.00 USD |
| `4H` | `Global Accounts` | `44.14%` | `55.86%` | `0.79` | 9,810,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `2252.25` | `2251.61` | `2252.25` | `2253.75` | `2247.75` | 100,086,564.92 USD | 38,681,627.31 USD | 61,404,937.61 USD | -22,723,310.29 USD | `-22.70%` | `0B / 5S` |
| `5:00 UTC` | `2244.75` | `2247.34` | `2244.75` | `2250.75` | `2244.25` | 75,332,127.88 USD | 44,642,781.21 USD | 30,689,346.67 USD | 13,953,434.54 USD | `+18.52%` | `1B / 0S` |
| `0:00 UTC` | `2230.25` | `2237.42` | `2230.25` | `2248.75` | `2228.25` | 239,005,598.88 USD | 101,154,920.14 USD | 137,850,678.73 USD | -36,695,758.59 USD | `-15.35%` | `0B / 8S` |
| `5:00 UTC` | `2232.75` | `2233.33` | `2232.75` | `2238.25` | `2228.25` | 153,884,513.89 USD | 97,714,432.25 USD | 56,170,081.64 USD | 41,544,350.61 USD | `+27.00%` | `5B / 1S` |
| `0:00 UTC` | `2227.75` | `2228.98` | `2227.75` | `2236.75` | `2223.25` | 107,078,982.08 USD | 47,873,893.40 USD | 59,205,088.68 USD | -11,331,195.28 USD | `-10.58%` | `0B / 1S` |
| `5:00 UTC` | `2233.25` | `2230.29` | `2233.25` | `2234.75` | `2224.25` | 95,342,735.21 USD | 45,163,958.47 USD | 50,178,776.75 USD | -5,014,818.28 USD | `-5.26%` | `0B / 3S` |
| `0:00 UTC` | `2224.25` | `2226.52` | `2224.25` | `2230.75` | `2223.25` | 103,679,050.63 USD | 41,811,152.44 USD | 61,867,898.19 USD | -20,056,745.75 USD | `-19.35%` | `0B / 2S` |
| `5:00 UTC` | `2223.75` | `2226.83` | `2223.75` | `2231.75` | `2223.25` | 59,922,094.97 USD | 29,249,984.51 USD | 30,672,110.46 USD | -1,422,125.96 USD | `-2.37%` | `1B / 1S` |
| `0:00 UTC` | `2222.75` | `2224.81` | `2222.75` | `2229.75` | `2221.25` | 65,855,959.19 USD | 30,261,207.11 USD | 35,594,752.09 USD | -5,333,544.98 USD | `-8.10%` | `0B / 4S` |
| `5:00 UTC` | `2221.75` | `2222.97` | `2221.75` | `2226.25` | `2220.25` | 68,537,963.80 USD | 36,206,475.87 USD | 32,331,487.93 USD | 3,874,987.93 USD | `+5.65%` | `0B / 0S` |

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
| `5m` | -1,190,000.00 USD | -598,180.00 USD | **`DISTRIBUTION`** |
| `15m` | -6,890,000.00 USD | -29,380,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -12,740,000.00 USD | -22,700,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -30,300,000.00 USD | -57,590,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -23,040,000.00 USD | -115,820,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -9,070,000.00 USD | -123,420,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 85,070.00 USD | -16,570,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -34,260,000.00 USD | -628,860,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -72,010,000.00 USD | -800,060,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -152,160,000.00 USD | -1,990,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -228,320,000.00 USD | -3,100,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,170,000,000.00 USD | -9,810,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.19M` | 15m=`-6.89M` | 1h=`-30.30M` | 24h=`-152.16M`
* Futures Capital Netflows: 5m=`-598.18K` | 15m=`-29.38M` | 1h=`-57.59M` | 24h=`-1.99B`
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
  * `2026-10-30 14:41:20 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:20 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:20 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:20 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:09:20 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:56:20 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:56:20 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:56:20 IST`: [destatis.de] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2193.19` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2173.35` (Risk Distance: `19.84` pts)
  * +2.5R Take Profit: `2242.80`
  * Mathematical Lot Sizing: **`0.50 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2252.28` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2272.12` (Risk Distance: `19.84` pts)
  * +2.5R Take Profit: `2202.67`
  * Mathematical Lot Sizing: **`0.50 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2238.47`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
