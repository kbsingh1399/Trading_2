# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 11:32:22 IST` (`2026-10-30 06:02:22 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2237.00` | **Live Ask Quote**: `2239.80` | **Mid Price**: `2238.40`
- **Spread Points**: `280.00` | **Spread BPS**: `12.51 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2215.12` | VWAP Z-Score: `+1.68` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `14.66` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `55.17` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2266.18` | Lower -3.00σ Band: `2164.06`
  * Upper +2.51σ Band: `2257.84` | Lower -2.51σ Band: `2172.40`
  * Upper +2.01σ Band: `2249.33` | Lower -2.01σ Band: `2180.91`
  * Upper +2.00σ Band: `2249.16` | Lower -2.00σ Band: `2181.08`
  * Upper +1.28σ Band: `2236.90` | Lower -1.28σ Band: `2193.33`
  * Upper +1.00σ Band: `2232.14` | Lower -1.00σ Band: `2198.10`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2235.03` | EMA-20=`2232.28` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2253.67` (Slope: `+0.0000`) | EMA-100=`2279.54`
  * Institutional Anchors: EMA-144=`2291.73` | EMA-200=`2301.48` (Slope: `-0.3967`) | EMA-233=`2306.59`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2275.75` (Distance: `-1.62%`)
  * Point of Control (POC) = `2264.42` (Distance: `-1.13%`)
  * Value Area Low (VAL) = `2208.57` (Distance: `+1.37%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2351.85` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2246.50` | Low=`2235.00`
  * New York Session (13:00-21:00 UTC): High=`2251.83` | Low=`2224.97`
  * Initial Balance (First Hour): IB High=`2246.50` | IB Low=`2235.00`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2229.45` - `2247.35`
  * Optimal Trade Entry (OTE 0.705): `2242.88`
  * Structural Invalidation Anchor (0.786): `2256.31`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2247.98` | `2251.99` | `2246.50` | `2247.92` | `10,589` | 23,815,158.93 USD | 3,318,622.96 USD | `+13.93%` | -1,034,376,302.91 USD | `+0.54` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `2247.92` | `2249.65` | `2246.50` | `2246.50` | `11,502` | 25,860,147.12 USD | -1,455,252.58 USD | `-5.63%` | -1,035,831,555.49 USD | `-0.29` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `2246.50` | `2249.31` | `2245.66` | `2248.59` | `5,989` | 13,457,752.33 USD | -861,768.86 USD | `-6.40%` | -1,036,693,324.35 USD | `-0.35` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2242.81` | `2252.87` | `2241.55` | `2247.18` | `47,793` | 107,425,896.61 USD | 12,910,248.16 USD | `+12.02%` | -1,028,545,310.50 USD | `+0.55` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `2247.18` | `2249.00` | `2244.60` | `2247.98` | `26,763` | 60,142,096.16 USD | -9,149,615.36 USD | `-15.21%` | -1,037,694,925.86 USD | `-0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2247.98` | `2251.99` | `2245.66` | `2248.12` | `28,130` | 63,246,030.10 USD | 891,201.89 USD | `+1.41%` | -1,036,803,723.98 USD | `+0.18` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `2209.27` | `2238.00` | `2208.12` | `2236.82` | `225,707` | 502,124,659.31 USD | 34,201,688.52 USD | `+6.81%` | -1,027,139,167.10 USD | `+0.73` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2236.81` | `2246.94` | `2225.47` | `2242.81` | `206,764` | 463,074,415.24 USD | -1,345,167.52 USD | `-0.29%` | -1,028,484,334.62 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2242.81` | `2252.87` | `2241.55` | `2248.12` | `102,687` | 230,814,022.87 USD | 4,651,834.68 USD | `+2.02%` | -1,023,832,499.94 USD | `+0.46` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -701,515,761.74 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -963,151,175.97 USD | `-0.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2252.87` | `2225.47` | `2248.82` | `309,631` | 694,292,101.52 USD | 3,690,407.35 USD | `+0.53%` | -959,460,768.62 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | 54,877,924.52 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -147,278,192.42 USD | `-1.22` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -701,515,761.74 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -963,151,175.97 USD | `-0.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2252.87` | `2225.47` | `2243.03` | `331,736` | 743,931,542.43 USD | -1,857,413.51 USD | `-0.25%` | -965,008,589.48 USD | `+0.74` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`2238.40`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2240.00` | `117.9463` | 264,199.71 USD | 9,326,572.89 USD | `9 orders` | `-0.09%` | `-` |
| `BID` | `2240.10` | `606.1244` | 1,357,779.27 USD | 9,062,373.17 USD | `11 orders` | `-0.08%` | `-` |
| `BID` | `2240.20` | `169.7429` | 380,258.04 USD | 7,704,593.91 USD | `9 orders` | `-0.08%` | `-` |
| `BID` | `2240.30` | `208.1831` | 466,392.60 USD | 7,324,335.86 USD | `5 orders` | `-0.07%` | `-` |
| `BID` | `2240.40` | `66.9015` | 149,886.12 USD | 6,857,943.26 USD | `6 orders` | `-0.07%` | `-` |
| `BID` | `2240.50` | `297.1358` | 665,732.76 USD | 6,708,057.14 USD | `7 orders` | `-0.06%` | `-` |
| `BID` | `2240.60` | `264.2886` | 592,165.04 USD | 6,042,324.38 USD | `14 orders` | `-0.06%` | `-` |
| `BID` | `2240.70` | `48.1312` | 107,847.58 USD | 5,450,159.34 USD | `6 orders` | `-0.06%` | `-` |
| `BID` | `2240.80` | `85.3987` | 191,361.41 USD | 5,342,311.76 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `2240.90` | `125.9035` | 282,137.15 USD | 5,150,950.36 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `2241.00` | `59.5024` | 133,344.88 USD | 4,868,813.20 USD | `13 orders` | `-0.04%` | `-` |
| `BID` | `2241.10` | `565.1911` | 1,266,649.77 USD | 4,735,468.33 USD | `8 orders` | `-0.04%` | `-` |
| `BID` | `2241.20` | `528.2204` | 1,183,847.56 USD | 3,468,818.55 USD | `10 orders` | `-0.03%` | `-` |
| `BID` | `2241.30` | `51.1027` | 114,536.48 USD | 2,284,970.99 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `2241.40` | `389.4356` | 872,880.95 USD | 2,170,434.51 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `2241.50` | `117.8150` | 264,082.32 USD | 1,297,553.56 USD | `13 orders` | `-0.02%` | `-` |
| `BID` | `2241.60` | `190.2114` | 426,377.87 USD | 1,033,471.23 USD | `9 orders` | `-0.02%` | `-` |
| `BID` | `2241.70` | `42.3530` | 94,942.72 USD | 607,093.36 USD | `7 orders` | `-0.01%` | `-` |
| `BID` | `2241.80` | `24.4872` | 54,895.40 USD | 512,150.64 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `2241.90` | `203.9588` | 457,255.23 USD | 457,255.23 USD | `22 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2241.95` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,241.95` | `0.00%` | `-` |
| `ASK` | `2242.00` | `19.9315` | 44,686.42 USD | 44,686.42 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `2242.10` | `15.7874` | 35,396.93 USD | 80,083.35 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `2242.20` | `15.7874` | 35,398.51 USD | 115,481.86 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `2242.30` | `15.7874` | 35,400.09 USD | 150,881.95 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `2242.40` | `19.1724` | 42,992.19 USD | 193,874.14 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `2242.50` | `150.4356` | 337,351.83 USD | 531,225.97 USD | `11 orders` | `+0.02%` | `-` |
| `ASK` | `2242.60` | `37.6083` | 84,340.37 USD | 615,566.34 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `2242.70` | `80.3632` | 180,230.55 USD | 795,796.89 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `2242.80` | `145.8369` | 327,083.00 USD | 1,122,879.89 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `2242.90` | `180.2963` | 404,386.57 USD | 1,527,266.46 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `2243.00` | `89.5464` | 200,852.58 USD | 1,728,119.04 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `2243.10` | `83.0256` | 186,234.72 USD | 1,914,353.76 USD | `9 orders` | `+0.05%` | `-` |
| `ASK` | `2243.20` | `421.5162` | 945,545.14 USD | 2,859,898.90 USD | `7 orders` | `+0.06%` | `-` |
| `ASK` | `2243.30` | `206.7123` | 463,717.70 USD | 3,323,616.60 USD | `5 orders` | `+0.06%` | `-` |
| `ASK` | `2243.40` | `198.0813` | 444,375.59 USD | 3,767,992.19 USD | `7 orders` | `+0.06%` | `-` |
| `ASK` | `2243.50` | `251.0944` | 563,330.29 USD | 4,331,322.48 USD | `7 orders` | `+0.07%` | `-` |
| `ASK` | `2243.60` | `181.4747` | 407,156.64 USD | 4,738,479.12 USD | `12 orders` | `+0.07%` | `-` |
| `ASK` | `2243.70` | `403.8244` | 906,060.81 USD | 5,644,539.92 USD | `6 orders` | `+0.08%` | `-` |
| `ASK` | `2243.80` | `98.7011` | 221,465.53 USD | 5,866,005.45 USD | `11 orders` | `+0.08%` | `-` |
| `ASK` | `2243.90` | `188.0501` | 421,965.62 USD | 6,287,971.07 USD | `13 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:24:14 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1844.19` | `7,964.66` | 14,688,299.29 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 11:24:14 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 11:24:14 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1913.44` | `6,500.22` | 12,437,784.60 USD | `AT_RISK_LIQ` | `0xf78c5d8d4b` | `2026-10-30 11:24:14 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `10,000.00` | 19,261,000.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 11:24:14 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1927.82` | `8,092.45` | 15,600,828.40 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 11:24:14 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2122.13` | `30,641.99` | 65,026,386.86 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 11:24:14 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.41` | `26,025.05` | 55,418,031.50 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 11:24:14 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,000.00` | 6,525,000.00 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2210.00` | `2,000.69` | 4,421,518.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.10` | `500.00` | 1,105,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.20` | `504.57` | 1,115,705.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2218.80` | `401.99` | 891,943.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc86781f990` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2220.20` | `4,681.76` | 10,394,435.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.00` | `458.19` | 1,017,637.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9362ca4dfd` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.10` | `1,408.25` | 3,127,870.74 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.10` | `500.00` | 1,110,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.00` | `357.02` | 794,719.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.00` | `342.28` | 761,925.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2228.20` | `504.24` | 1,123,556.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2229.30` | `993.60` | 2,215,041.40 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2231.10` | `500.00` | 1,115,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2232.00` | `2,417.43` | 5,395,711.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.60` | `504.24` | 1,126,774.70 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2235.90` | `690.08` | 1,542,939.36 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2236.40` | `1,792.05` | 4,007,743.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2238.30` | `1,342.85` | 3,005,704.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2238.80` | `471.40` | 1,055,377.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2239.10` | `1,233.53` | 2,761,995.68 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2239.30` | `348.99` | 781,495.10 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2240.80` | `894.23` | 2,003,780.28 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2240.80` | `480.11` | 1,075,839.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2241.10` | `500.00` | 1,120,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2242.40` | `670.14` | 1,502,732.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2244.00` | `348.15` | 781,251.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2244.10` | `446.40` | 1,001,772.75 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2250.80` | `445.14` | 1,001,913.68 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2250.90` | `339.17` | 763,430.78 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2251.70` | `667.42` | 1,502,824.44 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2253.80` | `889.04` | 2,003,708.44 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2254.10` | `492.58` | 1,110,315.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2255.20` | `471.37` | 1,063,035.88 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2257.70` | `336.82` | 760,449.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2258.00` | `1,233.18` | 2,784,522.25 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2258.10` | `1,331.14` | 3,005,854.91 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2258.60` | `694.57` | 1,568,751.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2259.50` | `504.19` | 1,139,217.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2259.90` | `1,773.42` | 4,007,757.28 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2262.20` | `2,420.23` | 5,475,034.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2264.80` | `504.05` | 1,141,581.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2265.50` | `995.74` | 2,255,854.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.70` | `620.97` | 1,409,408.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.70` | `335.69` | 761,925.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.80` | `350.13` | 794,719.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.20` | `2,200.51` | 4,999,999.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb1ec7febea` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2274.10` | `1,418.47` | 3,225,753.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2275.70` | `4,696.65` | 10,688,176.87 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2279.30` | `504.41` | 1,149,697.15 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:24:14 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2285.30` | `1,960.43` | 4,480,161.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:24:14 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2300.00` | `4,002.10` | 9,204,832.99 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 11:24:14 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2457.31` | `22,046.99` | 54,176,241.78 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 11:24:14 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `2,733.67` | 6,872,176.53 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 11:24:14 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2624.15` | `10,000.00` | 26,241,459.22 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 11:24:14 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.00` | `9,700.00` | 25,782,604.68 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 11:24:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 238,641,717.37 USD | `106,417.71` | `2322.74` | `2240.20` | `3776.04` | 8,539,294.79 USD | `+3.58%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 144,910,461.50 USD | `64,680.62` | `2375.30` | `2240.20` | `4321.72` | 8,725,836.00 USD | `+6.02%` | `5X Cross` |
| `10` | `0x77dd...e0e9` | `LONG` | 68,674,831.80 USD | `30,641.99` | `2610.31` | `2240.20` | `2122.05` | -11,310,343.24 USD | `-16.47%` | `10X Cross` |
| `12` | `0xde8d...9524` | `LONG` | 67,905,261.61 USD | `30,282.40` | `2134.45` | `2240.20` | `1786.31` | 3,268,931.03 USD | `+4.81%` | `20X Cross` |
| `17` | `0x0392...d7d9` | `LONG` | 58,315,112.75 USD | `26,025.05` | `2518.71` | `2240.20` | `2129.33` | -7,234,609.34 USD | `-12.41%` | `9X Cross` |
| `23` | `0x8add...7d2c` | `SHORT` | 49,438,167.69 USD | `22,046.99` | `2271.09` | `2240.20` | `2452.05` | 632,729.62 USD | `+1.28%` | `25X Cross` |
| `27` | `0xdf95...7d72` | `SHORT` | 44,750,382.72 USD | `19,971.61` | `2402.53` | `2240.20` | `4180.32` | 3,232,096.57 USD | `+7.22%` | `25X Cross` |
| `34` | `0xeced...6210` | `SHORT` | 37,417,884.83 USD | `16,687.58` | `2522.09` | `2240.20` | `3477.01` | 4,669,830.16 USD | `+12.48%` | `20X Cross` |
| `35` | `0x6046...b21d` | `LONG` | 35,713,797.28 USD | `15,927.59` | `2410.19` | `2240.20` | `1746.96` | -2,674,822.37 USD | `-7.49%` | `6X Cross` |
| `36` | `0xb695...a92d` | `SHORT` | 35,108,382.13 USD | `15,668.28` | `2557.74` | `2240.20` | `3962.97` | 4,967,086.92 USD | `+14.15%` | `20X Cross` |
| `39` | `0x45d2...4029` | `SHORT` | 31,264,740.00 USD | `13,950.00` | `2443.60` | `2240.20` | `5275.88` | 2,823,542.46 USD | `+9.03%` | `20X Cross` |
| `43` | `0xa61c...66b9` | `LONG` | 28,874,275.20 USD | `12,888.00` | `2369.69` | `2240.20` | `1443.24` | -1,666,379.34 USD | `-5.77%` | `10X Cross` |
| `46` | `0xbd1c...ff0e` | `LONG` | 26,899,200.00 USD | `12,000.00` | `2419.91` | `2240.20` | `1520.19` | -2,139,832.39 USD | `-7.96%` | `20X Cross` |
| `47` | `0x2371...0883` | `LONG` | 26,883,600.00 USD | `12,000.00` | `2421.77` | `2240.20` | `1279.29` | -2,177,694.85 USD | `-8.10%` | `20X Cross` |
| `54` | `0xa9de...e049` | `LONG` | 24,667,500.00 USD | `11,000.00` | `2481.81` | `2240.20` | `1643.93` | -2,632,479.46 USD | `-10.67%` | `20X Cross` |
| `55` | `0x0c5d...36b3` | `LONG` | 24,667,500.00 USD | `11,000.00` | `2482.20` | `2240.20` | `1644.26` | -2,636,753.24 USD | `-10.69%` | `20X Cross` |
| `56` | `0x09dc...c094` | `LONG` | 24,667,500.00 USD | `11,000.00` | `2465.31` | `2240.20` | `1637.26` | -2,450,923.04 USD | `-9.94%` | `20X Cross` |
| `57` | `0x6c93...59a4` | `LONG` | 24,644,400.00 USD | `11,000.00` | `2441.15` | `2240.20` | `1602.22` | -2,208,272.73 USD | `-8.96%` | `20X Cross` |
| `70` | `0xa2ce...3126` | `LONG` | 22,456,331.67 USD | `10,016.88` | `2162.83` | `2240.20` | `1525.82` | 791,529.62 USD | `+3.52%` | `10X Cross` |
| `71` | `0x15a4...dfdb` | `LONG` | 22,425,000.00 USD | `10,000.00` | `1761.94` | `2240.20` | `247.33` | 4,805,518.97 USD | `+21.43%` | `20X Cross` |
| `72` | `0xec7f...df39` | `LONG` | 22,425,000.00 USD | `10,000.00` | `2719.35` | `2240.20` | `1720.78` | -4,768,548.52 USD | `-21.26%` | `20X Cross` |
| `73` | `0x6646...6de5` | `LONG` | 22,412,000.00 USD | `10,000.00` | `1765.80` | `2240.20` | `1723.54` | 4,753,942.55 USD | `+21.21%` | `25X Cross` |
| `74` | `0xb37f...66ca` | `SHORT` | 22,412,000.00 USD | `10,000.00` | `2290.69` | `2240.20` | `2624.08` | 494,991.85 USD | `+2.21%` | `25X Cross` |
| `76` | `0x939f...04d2` | `LONG` | 22,029,900.43 USD | `9,823.81` | `2427.28` | `2240.20` | `1780.77` | -1,815,250.17 USD | `-8.24%` | `25X Cross` |
| `78` | `0xaeaa...2416` | `SHORT` | 21,731,880.00 USD | `9,700.00` | `2311.92` | `2240.20` | `2657.93` | 693,802.40 USD | `+3.19%` | `25X Cross` |
| `84` | `0xf517...c032` | `SHORT` | 20,894,748.04 USD | `9,326.35` | `2202.91` | `2240.20` | `3163.71` | -349,609.83 USD | `-1.67%` | `25X Cross` |
| `85` | `0xca49...53c8` | `SHORT` | 20,607,551.98 USD | `9,188.31` | `2549.39` | `2240.20` | `3854.61` | 2,817,112.16 USD | `+13.67%` | `25X Cross` |
| `88` | `0xba5d...a352` | `SHORT` | 20,302,963.40 USD | `9,054.12` | `2493.89` | `2240.20` | `2908.89` | 2,277,043.86 USD | `+11.22%` | `20X Cross` |
| `89` | `0xea00...a918` | `LONG` | 20,190,180.10 USD | `9,003.83` | `2003.01` | `2240.20` | `1363.47` | 2,155,401.23 USD | `+10.68%` | `5X Cross` |
| `92` | `0xefe4...194b` | `SHORT` | 19,764,524.11 USD | `8,820.57` | `2267.42` | `2240.20` | `3555.05` | 235,490.29 USD | `+1.19%` | `20X Cross` |
| `93` | `0xecb6...2b00` | `SHORT` | 19,694,373.12 USD | `8,789.27` | `2243.08` | `2240.20` | `5759.91` | 20,691.44 USD | `+0.11%` | `15X Cross` |
| `115` | `0x9eec...daab` | `LONG` | 18,136,803.65 USD | `8,092.45` | `1658.44` | `2240.20` | `1927.03` | 4,715,939.12 USD | `+26.00%` | `15X Cross` |
| `116` | `0x5f91...65aa` | `LONG` | 17,859,944.39 USD | `7,964.66` | `1626.99` | `2240.20` | `1844.11` | 4,901,501.33 USD | `+27.44%` | `16X Cross` |
| `129` | `0xec0b...b078` | `LONG` | 15,700,272.66 USD | `7,007.80` | `2065.97` | `2240.20` | `1058.06` | 1,222,343.07 USD | `+7.79%` | `25X Cross` |
| `130` | `0xf02d...5eb3` | `LONG` | 15,360,149.91 USD | `6,855.99` | `2383.33` | `2240.20` | `1120.03` | -979,938.85 USD | `-6.38%` | `20X Cross` |
| `132` | `0xcf53...ee11` | `SHORT` | 15,252,713.21 USD | `6,803.63` | `1862.69` | `2240.20` | `4206.43` | -2,579,607.82 USD | `-16.91%` | `7X Cross` |
| `137` | `0x4ff9...38d3` | `LONG` | 14,719,334.92 USD | `6,564.10` | `2447.40` | `2240.20` | `1669.88` | -1,345,687.82 USD | `-9.14%` | `3X Isolated` |
| `140` | `0xf78c...c581` | `LONG` | 14,565,241.32 USD | `6,500.22` | `2521.53` | `2240.20` | `1913.36` | -1,825,299.62 USD | `-12.53%` | `20X Cross` |
| `141` | `0x1ee7...edf5` | `LONG` | 14,564,745.00 USD | `6,500.00` | `2301.55` | `2240.20` | `2069.10` | -395,348.66 USD | `-2.71%` | `25X Cross` |
| `144` | `0x799f...5f4c` | `LONG` | 14,138,947.75 USD | `6,310.90` | `2390.33` | `2240.20` | `1825.38` | -946,216.86 USD | `-6.69%` | `20X Cross` |
| `148` | `0x08bf...7872` | `SHORT` | 13,949,335.03 USD | `6,224.05` | `2258.00` | `2240.20` | `2585.15` | 104,581.07 USD | `+0.75%` | `20X Cross` |
| `149` | `0xc179...e0c8` | `LONG` | 13,943,488.53 USD | `6,223.94` | `2294.94` | `2240.20` | `1221.63` | -340,093.77 USD | `-2.44%` | `10X Cross` |
| `154` | `0xd9e7...4aff` | `LONG` | 13,453,560.00 USD | `6,000.00` | `2480.18` | `2240.20` | `1407.65` | -1,427,564.33 USD | `-10.61%` | `20X Cross` |
| `164` | `0x0c4a...1b19` | `LONG` | 12,692,768.64 USD | `5,660.10` | `2373.06` | `2240.20` | `2081.70` | -738,989.49 USD | `-5.82%` | `25X Isolated` |
| `167` | `0x418a...8888` | `SHORT` | 12,324,015.00 USD | `5,500.00` | `2494.55` | `2240.20` | `2830.00` | 1,396,021.50 USD | `+11.33%` | `25X Cross` |
| `171` | `0x7fda...17d1` | `LONG` | 11,908,893.99 USD | `5,315.76` | `2211.05` | `2240.20` | `0.000000` | 155,451.75 USD | `+1.31%` | `25X Cross` |
| `177` | `0x218a...7da2` | `SHORT` | 11,711,028.45 USD | `5,222.87` | `2208.16` | `2240.20` | `2792.80` | -178,093.39 USD | `-1.52%` | `10X Cross` |
| `189` | `0x45ab...6cbc` | `LONG` | 11,032,797.25 USD | `4,920.96` | `2727.66` | `2240.20` | `1373.94` | -2,389,946.54 USD | `-21.66%` | `7X Cross` |
| `193` | `0x64b7...9da9` | `LONG` | 10,881,262.54 USD | `4,856.84` | `2604.61` | `2240.20` | `588.56` | -1,768,951.87 USD | `-16.26%` | `25X Cross` |
| `200` | `0xfb18...eb17` | `SHORT` | 10,686,451.96 USD | `4,768.18` | `2315.53` | `2240.20` | `2590.28` | 354,429.83 USD | `+3.32%` | `25X Cross` |
| `202` | `0x5559...d43b` | `SHORT` | 10,665,162.49 USD | `4,755.93` | `2262.69` | `2240.20` | `2784.78` | 96,043.39 USD | `+0.90%` | `25X Cross` |
| `213` | `0xe091...6705` | `SHORT` | 10,090,170.45 USD | `4,500.00` | `2467.33` | `2240.20` | `2463.27` | 1,012,838.06 USD | `+10.04%` | `20X Cross` |
| `222` | `0xb829...3a81` | `LONG` | 9,847,808.93 USD | `4,394.91` | `2398.60` | `2240.20` | `1476.86` | -693,833.02 USD | `-7.05%` | `20X Cross` |
| `237` | `0x28bb...fca6` | `SHORT` | 9,431,219.65 USD | `4,209.61` | `1896.10` | `2240.20` | `3036.42` | -1,449,337.09 USD | `-15.37%` | `20X Cross` |
| `240` | `0x6ea4...0ea7` | `SHORT` | 9,382,229.18 USD | `4,184.01` | `2602.13` | `2240.20` | `3425.22` | 1,505,117.49 USD | `+16.04%` | `20X Cross` |
| `251` | `0x5e9e...35ee` | `SHORT` | 8,982,134.59 USD | `4,007.56` | `1796.39` | `2240.20` | `2585.71` | -1,782,984.50 USD | `-19.85%` | `20X Cross` |
| `253` | `0xfb94...0ddf` | `SHORT` | 8,972,711.11 USD | `4,002.10` | `2382.44` | `2240.20` | `5104.61` | 562,073.04 USD | `+6.26%` | `20X Cross` |
| `255` | `0x8cc9...2b6a` | `SHORT` | 8,962,920.00 USD | `4,000.00` | `1791.18` | `2240.20` | `3540.34` | -1,798,173.33 USD | `-20.06%` | `25X Cross` |
| `256` | `0x3dc9...54b0` | `SHORT` | 8,962,225.82 USD | `3,999.69` | `2480.32` | `2240.20` | `6428.14` | 958,310.73 USD | `+10.69%` | `20X Cross` |
| `273` | `0x4b67...f4e7` | `LONG` | 8,566,327.54 USD | `3,820.84` | `2591.51` | `2240.20` | `1336.84` | -1,335,446.00 USD | `-15.59%` | `20X Cross` |
| `277` | `0x12d2...f97f` | `LONG` | 8,417,767.99 USD | `3,757.26` | `2446.50` | `2240.20` | `1770.88` | -774,398.40 USD | `-9.20%` | `20X Cross` |
| `295` | `0x8ae4...3d60` | `LONG` | 7,978,405.72 USD | `3,558.20` | `2482.21` | `2240.20` | `478.87` | -853,792.31 USD | `-10.70%` | `10X Cross` |
| `326` | `0x469e...58a5` | `SHORT` | 7,025,747.93 USD | `3,133.33` | `2197.67` | `2240.20` | `3202.95` | -139,691.28 USD | `-1.99%` | `25X Cross` |
| `334` | `0xb823...9763` | `SHORT` | 6,727,500.00 USD | `3,000.00` | `2229.66` | `2240.20` | `3233.61` | -38,503.32 USD | `-0.57%` | `25X Cross` |
| `335` | `0x4a20...3c26` | `LONG` | 6,723,600.00 USD | `3,000.00` | `2428.72` | `2240.20` | `514.07` | -562,560.28 USD | `-8.37%` | `20X Cross` |
| `336` | `0x007d...67a0` | `LONG` | 6,723,600.00 USD | `3,000.00` | `2400.00` | `2240.20` | `1472.06` | -476,400.00 USD | `-7.09%` | `25X Cross` |
| `364` | `0x9c2a...f6a8` | `SHORT` | 6,326,499.04 USD | `2,823.41` | `2533.78` | `2240.20` | `2626.93` | 827,411.78 USD | `+13.08%` | `20X Cross` |
| `391` | `0x8328...f54a` | `SHORT` | 5,777,691.59 USD | `2,576.45` | `2292.01` | `2240.20` | `3279.45` | 127,579.70 USD | `+2.21%` | `25X Cross` |
| `394` | `0xed48...7c9b` | `SHORT` | 5,717,593.68 USD | `2,551.13` | `2460.02` | `2240.20` | `3244.13` | 558,252.73 USD | `+9.76%` | `20X Cross` |
| `399` | `0x1c98...7fc7` | `LONG` | 5,605,660.09 USD | `2,500.00` | `2452.60` | `2240.20` | `1916.85` | -525,861.47 USD | `-9.38%` | `10X Cross` |
| `400` | `0x970c...2a93` | `SHORT` | 5,605,650.00 USD | `2,500.00` | `2229.57` | `2240.20` | `5050.46` | -31,705.51 USD | `-0.57%` | `20X Cross` |
| `412` | `0xa445...329d` | `LONG` | 5,392,631.55 USD | `2,406.14` | `2354.86` | `2240.20` | `1699.94` | -273,483.73 USD | `-5.07%` | `25X Cross` |
| `415` | `0xfbe2...c8ea` | `SHORT` | 5,345,723.69 USD | `2,385.21` | `2041.57` | `2240.20` | `2622.06` | -476,157.03 USD | `-8.91%` | `20X Cross` |
| `416` | `0x6749...ce07` | `SHORT` | 5,343,116.97 USD | `2,384.89` | `2220.92` | `2240.20` | `3630.85` | -46,453.93 USD | `-0.87%` | `20X Cross` |
| `417` | `0x645b...87b8` | `SHORT` | 5,332,882.73 USD | `2,379.98` | `2421.64` | `2240.20` | `11338.68` | 430,564.23 USD | `+8.07%` | `10X Cross` |
| `428` | `0x77ee...2902` | `SHORT` | 5,136,645.95 USD | `2,290.69` | `2476.53` | `2240.20` | `5907.65` | 536,326.29 USD | `+10.44%` | `25X Cross` |
| `434` | `0xbcd4...0dd2` | `SHORT` | 5,070,918.38 USD | `2,263.50` | `2233.24` | `2240.20` | `2638.80` | -15,960.81 USD | `-0.31%` | `25X Cross` |
| `450` | `0xd507...c948` | `SHORT` | 4,866,148.58 USD | `2,172.00` | `2387.49` | `2240.20` | `2600.45` | 319,492.45 USD | `+6.57%` | `5X Isolated` |
| `461` | `0x382b...3e39` | `SHORT` | 4,771,727.75 USD | `2,129.54` | `2296.66` | `2240.20` | `4634.84` | 119,109.47 USD | `+2.50%` | `25X Cross` |
| `462` | `0x023a...2355` | `LONG` | 4,758,275.75 USD | `2,123.54` | `2330.15` | `2240.20` | `0.000000` | -189,898.06 USD | `-3.99%` | `25X Cross` |
| `493` | `0x3453...b323` | `SHORT` | 4,485,876.09 USD | `2,000.12` | `2322.47` | `2240.20` | `2374.41` | 159,359.75 USD | `+3.55%` | `25X Cross` |
| `494` | `0x7a6d...f79c` | `SHORT` | 4,485,000.00 USD | `2,000.00` | `2418.41` | `2240.20` | `2542.66` | 351,832.11 USD | `+7.84%` | `25X Cross` |
| `495` | `0xe02e...d78b` | `LONG` | 4,481,000.00 USD | `2,000.00` | `2228.11` | `2240.20` | `2171.80` | 24,776.53 USD | `+0.55%` | `25X Cross` |
| `503` | `0xf3dc...1672` | `SHORT` | 4,437,454.98 USD | `1,980.36` | `2240.44` | `2240.20` | `2768.37` | -567.42 USD | `-0.01%` | `20X Cross` |
| `508` | `0xac48...3201` | `SHORT` | 4,405,687.91 USD | `1,964.37` | `2272.04` | `2240.20` | `3104.71` | 57,454.39 USD | `+1.30%` | `20X Cross` |
| `512` | `0x0622...8088` | `LONG` | 4,345,865.14 USD | `1,939.49` | `2214.59` | `2240.20` | `0.000000` | 50,692.15 USD | `+1.17%` | `5X Cross` |
| `519` | `0x8376...9a1e` | `SHORT` | 4,284,096.23 USD | `1,910.50` | `2477.72` | `2240.20` | `3178.20` | 449,591.94 USD | `+10.49%` | `20X Cross` |
| `521` | `0x739c...cfb2` | `SHORT` | 4,257,387.00 USD | `1,900.00` | `2418.12` | `2240.20` | `2501.87` | 337,059.38 USD | `+7.92%` | `25X Cross` |
| `552` | `0x7265...91a5` | `LONG` | 4,040,692.13 USD | `1,801.87` | `2533.96` | `2240.20` | `1987.33` | -525,174.33 USD | `-13.00%` | `20X Cross` |
| `554` | `0xbb34...1696` | `LONG` | 4,036,320.00 USD | `1,800.00` | `2313.95` | `2240.20` | `1950.90` | -128,798.23 USD | `-3.19%` | `25X Cross` |
| `555` | `0xc619...10f5` | `LONG` | 4,036,140.00 USD | `1,800.00` | `2313.55` | `2240.20` | `1783.43` | -128,255.83 USD | `-3.18%` | `25X Cross` |
| `566` | `0x91a9...3f70` | `SHORT` | 3,959,685.44 USD | `1,767.48` | `2156.23` | `2240.20` | `3656.13` | -148,581.36 USD | `-3.75%` | `4X Cross` |
| `600` | `0xfeec...4e9c` | `SHORT` | 3,790,328.44 USD | `1,691.81` | `2566.49` | `2240.20` | `2508.78` | 551,696.08 USD | `+14.56%` | `10X Cross` |
| `615` | `0xeee0...0b53` | `LONG` | 3,670,431.78 USD | `1,637.12` | `2468.64` | `2240.20` | `166.63` | -371,044.28 USD | `-10.11%` | `7X Cross` |
| `618` | `0x27b8...12fc` | `LONG` | 3,651,059.32 USD | `1,628.12` | `2468.73` | `2240.20` | `578.14` | -368,335.31 USD | `-10.09%` | `10X Cross` |
| `621` | `0x982b...4606` | `LONG` | 3,647,324.39 USD | `1,626.82` | `2575.24` | `2240.20` | `1547.61` | -542,128.69 USD | `-14.86%` | `5X Isolated` |
| `628` | `0x73d7...8be1` | `LONG` | 3,589,364.63 USD | `1,601.47` | `2410.40` | `2240.20` | `1757.17` | -270,814.30 USD | `-7.54%` | `25X Cross` |
| `631` | `0xad54...6203` | `LONG` | 3,581,902.05 USD | `1,597.45` | `2591.98` | `2240.20` | `2051.96` | -558,676.00 USD | `-15.60%` | `10X Isolated` |
| `635` | `0x880a...311c` | `LONG` | 3,537,982.93 USD | `1,578.40` | `2209.72` | `2240.20` | `0.000000` | 50,159.08 USD | `+1.42%` | `9X Cross` |
| `654` | `0xe170...9300` | `SHORT` | 3,438,342.82 USD | `1,533.40` | `2076.39` | `2240.20` | `3149.59` | -254,393.32 USD | `-7.40%` | `25X Cross` |
| `655` | `0x4b86...df9d` | `SHORT` | 3,417,570.00 USD | `1,524.00` | `2287.40` | `2240.20` | `2759.80` | 68,427.60 USD | `+2.00%` | `9X Isolated` |
| `664` | `0x2e2b...2fab` | `LONG` | 3,376,976.69 USD | `1,507.38` | `2245.53` | `2240.20` | `1201.85` | -7,896.41 USD | `-0.23%` | `25X Cross` |
| `667` | `0xf929...d1f9` | `SHORT` | 3,363,750.00 USD | `1,500.00` | `2423.37` | `2240.20` | `2677.84` | 271,305.26 USD | `+8.07%` | `25X Cross` |
| `668` | `0xde6b...3361` | `LONG` | 3,363,390.00 USD | `1,500.00` | `2216.98` | `2240.20` | `2168.73` | 37,909.26 USD | `+1.13%` | `25X Cross` |
| `669` | `0x251f...6e5d` | `LONG` | 3,360,600.00 USD | `1,500.00` | `2346.68` | `2240.20` | `1823.56` | -159,430.49 USD | `-4.74%` | `20X Cross` |
| `690` | `0xb885...3c54` | `LONG` | 3,249,889.93 USD | `1,450.00` | `2274.34` | `2240.20` | `17.12` | -47,918.21 USD | `-1.47%` | `20X Cross` |
| `691` | `0x3440...32c5` | `SHORT` | 3,246,282.69 USD | `1,448.97` | `2198.21` | `2240.20` | `3776.10` | -61,131.73 USD | `-1.88%` | `25X Cross` |
| `694` | `0xef70...a84c` | `SHORT` | 3,232,322.31 USD | `1,442.74` | `2424.73` | `2240.20` | `3296.63` | 265,948.51 USD | `+8.23%` | `25X Cross` |
| `702` | `0x4b5f...0dd8` | `LONG` | 3,208,012.82 USD | `1,431.96` | `2339.45` | `2240.20` | `2147.89` | -141,980.13 USD | `-4.43%` | `10X Cross` |
| `704` | `0xbadb...9ee6` | `LONG` | 3,202,648.80 USD | `1,428.16` | `1936.00` | `2240.20` | `1062.44` | 437,727.15 USD | `+13.67%` | `20X Cross` |
| `762` | `0x53f8...ceff` | `LONG` | 3,021,390.23 USD | `1,348.65` | `2276.73` | `2240.20` | `0.000000` | -49,134.24 USD | `-1.63%` | `20X Cross` |
| `777` | `0x0dd5...f6ee` | `LONG` | 2,948,571.90 USD | `1,315.00` | `2306.05` | `2240.20` | `1560.23` | -83,892.48 USD | `-2.85%` | `5X Cross` |
| `804` | `0x1f16...6d07` | `LONG` | 2,837,359.20 USD | `1,266.00` | `2261.43` | `2240.20` | `1392.17` | -25,612.03 USD | `-0.90%` | `7X Cross` |
| `811` | `0xc435...c905` | `SHORT` | 2,798,640.00 USD | `1,248.00` | `2704.38` | `2240.20` | `4224.45` | 576,430.35 USD | `+20.60%` | `20X Cross` |
| `818` | `0x6859...7e1e` | `SHORT` | 2,771,719.37 USD | `1,237.15` | `2200.39` | `2240.20` | `4664.57` | -49,492.22 USD | `-1.79%` | `25X Cross` |
| `828` | `0x7178...0854` | `LONG` | 2,732,537.41 USD | `1,218.63` | `2461.81` | `2240.20` | `1147.65` | -267,508.99 USD | `-9.79%` | `10X Cross` |
| `829` | `0x7277...0b98` | `SHORT` | 2,732,186.46 USD | `1,219.45` | `2206.05` | `2240.20` | `3353.81` | -41,998.66 USD | `-1.54%` | `20X Cross` |
| `840` | `0xaaa1...ab8c` | `SHORT` | 2,690,880.00 USD | `1,200.00` | `2276.29` | `2240.20` | `2365.42` | 40,677.58 USD | `+1.51%` | `25X Isolated` |
| `856` | `0x07fd...689d` | `LONG` | 2,636,143.98 USD | `1,176.69` | `2416.34` | `2240.20` | `0.000000` | -207,155.95 USD | `-7.86%` | `25X Cross` |
| `859` | `0x4487...c92d` | `LONG` | 2,620,767.39 USD | `1,169.36` | `2231.29` | `2240.20` | `1569.41` | 11,577.89 USD | `+0.44%` | `10X Cross` |
| `909` | `0xbef3...0d3e` | `LONG` | 2,471,417.13 USD | `1,102.33` | `2233.44` | `2240.20` | `2174.44` | 9,432.72 USD | `+0.38%` | `20X Cross` |
| `912` | `0x6a41...a3b9` | `LONG` | 2,465,993.05 USD | `1,100.69` | `2233.05` | `2240.20` | `2177.22` | 8,088.29 USD | `+0.33%` | `20X Cross` |
| `920` | `0x2f80...f203` | `SHORT` | 2,441,950.42 USD | `1,088.94` | `1984.00` | `2240.20` | `2964.88` | -281,483.23 USD | `-11.53%` | `20X Cross` |
| `921` | `0x6e6f...82a6` | `LONG` | 2,433,883.86 USD | `1,086.36` | `2266.07` | `2240.20` | `1329.29` | -27,897.73 USD | `-1.15%` | `20X Cross` |
| `925` | `0x6f11...0389` | `SHORT` | 2,417,391.60 USD | `1,079.00` | `2333.39` | `2240.20` | `3198.91` | 100,337.31 USD | `+4.15%` | `25X Cross` |
| `926` | `0x8eb7...b90f` | `LONG` | 2,416,291.29 USD | `1,077.74` | `2396.38` | `2240.20` | `1881.14` | -166,386.76 USD | `-6.89%` | `5X Isolated` |
| `927` | `0x2b61...2f6c` | `SHORT` | 2,414,161.56 USD | `1,076.60` | `2681.75` | `2240.20` | `6351.45` | 473,011.18 USD | `+19.59%` | `10X Cross` |
| `939` | `0x0a97...347d` | `LONG` | 2,370,502.72 USD | `1,058.07` | `2267.88` | `2240.20` | `1452.23` | -29,078.00 USD | `-1.23%` | `20X Cross` |
| `956` | `0x30af...393e` | `SHORT` | 2,332,625.84 USD | `1,041.16` | `2252.26` | `2240.20` | `2297.11` | 12,356.48 USD | `+0.53%` | `25X Cross` |
| `962` | `0xa70a...4be9` | `LONG` | 2,318,361.73 USD | `1,034.15` | `2259.47` | `2240.20` | `840.57` | -18,278.75 USD | `-0.79%` | `20X Cross` |
| `972` | `0x1b2a...f7a6` | `LONG` | 2,299,285.20 USD | `1,025.37` | `2737.51` | `2240.20` | `882.27` | -507,674.74 USD | `-22.08%` | `10X Cross` |
| `979` | `0x001a...fef6` | `SHORT` | 2,256,911.66 USD | `1,007.33` | `2022.19` | `2240.20` | `3073.76` | -219,903.71 USD | `-9.74%` | `10X Cross` |
| `980` | `0x02aa...1806` | `SHORT` | 2,256,307.06 USD | `1,007.10` | `2654.68` | `2240.20` | `3612.90` | 417,225.04 USD | `+18.49%` | `20X Cross` |
| `982` | `0xdb3a...cf3b` | `LONG` | 2,247,502.79 USD | `1,003.22` | `2705.01` | `2240.20` | `0.000000` | -466,204.11 USD | `-20.74%` | `4X Cross` |
| `988` | `0x8c02...b73f` | `SHORT` | 2,240,730.00 USD | `1,000.00` | `2250.37` | `2240.20` | `8098.58` | 9,641.47 USD | `+0.43%` | `20X Cross` |
| `989` | `0x5272...fcd9` | `SHORT` | 2,240,400.00 USD | `1,000.00` | `2241.82` | `2240.20` | `2830.96` | 1,424.49 USD | `+0.06%` | `5X Cross` |
| `990` | `0xd7b8...9f55` | `LONG` | 2,240,257.50 USD | `999.00` | `2195.00` | `2240.20` | `0.000000` | 47,452.50 USD | `+2.12%` | `15X Cross` |
| `1016` | `0xb002...ed8a` | `SHORT` | 2,158,561.73 USD | `962.78` | `2299.66` | `2240.20` | `4199.14` | 55,516.18 USD | `+2.57%` | `25X Cross` |
| `1025` | `0xb812...b5e0` | `LONG` | 2,109,297.86 USD | `940.64` | `2263.21` | `2240.20` | `1184.74` | -19,578.96 USD | `-0.93%` | `25X Cross` |
| `1037` | `0xb1ec...e86a` | `SHORT` | 2,092,003.56 USD | `933.64` | `2272.72` | `2240.20` | `12596.60` | 29,903.39 USD | `+1.43%` | `25X Cross` |
| `1057` | `0xef96...9383` | `LONG` | 2,056,037.61 USD | `917.57` | `2235.00` | `2240.20` | `0.000000` | 5,253.95 USD | `+0.26%` | `25X Cross` |
| `1063` | `0xede2...f971` | `LONG` | 2,049,431.02 USD | `914.31` | `2208.16` | `2240.20` | `1463.18` | 30,474.03 USD | `+1.49%` | `5X Cross` |
| `1064` | `0x9606...4e5d` | `SHORT` | 2,047,175.98 USD | `913.00` | `2478.70` | `2240.20` | `4284.86` | 215,877.62 USD | `+10.55%` | `20X Cross` |
| `1083` | `0x5f10...d49d` | `LONG` | 2,017,080.00 USD | `900.00` | `2249.83` | `2240.20` | `1794.11` | -7,773.47 USD | `-0.39%` | `25X Cross` |
| `1087` | `0xa0fb...96be` | `LONG` | 2,006,367.67 USD | `894.70` | `2292.43` | `2240.20` | `1156.34` | -44,680.27 USD | `-2.23%` | `3X Cross` |
| `1173` | `0x2828...93a0` | `LONG` | 1,881,799.96 USD | `839.60` | `2242.41` | `2240.20` | `2192.73` | -932.23 USD | `-0.05%` | `25X Cross` |
| `1176` | `0xcd27...52a8` | `LONG` | 1,875,681.48 USD | `837.21` | `2553.56` | `2240.20` | `1403.42` | -262,183.30 USD | `-13.98%` | `2X Cross` |
| `1181` | `0xb8eb...1dd5` | `LONG` | 1,868,869.99 USD | `834.17` | `2234.28` | `2240.20` | `0.000000` | 5,099.03 USD | `+0.27%` | `25X Cross` |
| `1230` | `0xd911...961e` | `LONG` | 1,801,110.43 USD | `803.92` | `2220.31` | `2240.20` | `0.000000` | 16,144.00 USD | `+0.90%` | `25X Cross` |
| `1234` | `0x7737...bf66` | `SHORT` | 1,793,373.38 USD | `799.79` | `2494.83` | `2240.20` | `24047.40` | 201,972.65 USD | `+11.26%` | `15X Cross` |
| `1235` | `0x04a9...95aa` | `LONG` | 1,792,320.00 USD | `800.00` | `2595.13` | `2240.20` | `1866.99` | -283,786.74 USD | `-15.83%` | `5X Cross` |
| `1271` | `0x458d...ab3b` | `LONG` | 1,737,184.21 USD | `774.75` | `2740.41` | `2240.20` | `1887.17` | -385,944.98 USD | `-22.22%` | `3X Isolated` |
| `1325` | `0xaa53...9cb7` | `LONG` | 1,636,319.38 USD | `730.34` | `2389.70` | `2240.20` | `1960.10` | -108,970.26 USD | `-6.66%` | `20X Cross` |
| `1326` | `0x3fc5...c0c1` | `SHORT` | 1,635,541.15 USD | `729.92` | `2702.11` | `2240.20` | `4496.15` | 336,801.04 USD | `+20.59%` | `25X Cross` |
| `1336` | `0xa189...94d7` | `SHORT` | 1,613,616.93 USD | `719.98` | `2691.84` | `2240.20` | `2915.03` | 324,455.73 USD | `+20.11%` | `25X Cross` |
| `1352` | `0x51f6...2b39` | `LONG` | 1,593,293.03 USD | `711.06` | `2224.11` | `2240.20` | `359.73` | 11,811.54 USD | `+0.74%` | `25X Cross` |
| `1354` | `0x2e30...4cb5` | `SHORT` | 1,588,956.34 USD | `708.98` | `2334.41` | `2240.20` | `9218.51` | 66,089.00 USD | `+4.16%` | `2X Cross` |
| `1355` | `0x2f93...4404` | `LONG` | 1,585,868.11 USD | `707.47` | `1700.45` | `2240.20` | `1368.80` | 382,841.74 USD | `+24.14%` | `4X Isolated` |
| `1363` | `0x5605...fe0f` | `SHORT` | 1,574,557.02 USD | `702.14` | `2566.90` | `2240.20` | `3073.41` | 227,775.63 USD | `+14.47%` | `20X Cross` |
| `1385` | `0x7743...e4fe` | `SHORT` | 1,569,526.11 USD | `700.56` | `2298.56` | `2240.20` | `6178.21` | 40,748.98 USD | `+2.60%` | `25X Cross` |
| `1387` | `0x0deb...0bc5` | `LONG` | 1,568,280.00 USD | `700.00` | `2071.05` | `2240.20` | `1597.39` | 118,544.21 USD | `+7.56%` | `20X Cross` |
| `1420` | `0x248e...6be2` | `SHORT` | 1,526,981.71 USD | `680.93` | `2282.89` | `2240.20` | `3444.03` | 27,503.95 USD | `+1.80%` | `20X Cross` |
| `1421` | `0xdbd1...29dd` | `SHORT` | 1,525,794.65 USD | `680.70` | `3030.57` | `2240.20` | `3775.79` | 537,126.47 USD | `+35.20%` | `6X Cross` |
| `1431` | `0x71e5...be04` | `LONG` | 1,518,244.70 USD | `677.67` | `2727.27` | `2240.20` | `1470.95` | -329,940.91 USD | `-21.73%` | `20X Cross` |
| `1435` | `0x0b23...f37b` | `LONG` | 1,513,620.00 USD | `675.00` | `2238.15` | `2240.20` | `591.81` | 2,863.36 USD | `+0.19%` | `5X Cross` |
| `1463` | `0x0cac...6170` | `SHORT` | 1,473,589.00 USD | `657.50` | `2146.55` | `2240.20` | `2839.40` | -62,226.80 USD | `-4.22%` | `20X Cross` |
| `1499` | `0xb15b...dbae` | `SHORT` | 1,440,998.85 USD | `642.64` | `2290.80` | `2240.20` | `2280.53` | 31,168.63 USD | `+2.16%` | `25X Cross` |
| `1500` | `0xf00e...fe3d` | `SHORT` | 1,440,308.35 USD | `642.88` | `2333.21` | `2240.20` | `2485.03` | 59,669.62 USD | `+4.14%` | `20X Cross` |
| `1505` | `0xffb2...5ed6` | `SHORT` | 1,436,855.47 USD | `640.77` | `2672.96` | `2240.20` | `2516.40` | 275,892.88 USD | `+19.20%` | `20X Cross` |
| `1516` | `0x8505...1821` | `SHORT` | 1,420,324.66 USD | `633.96` | `2239.93` | `2240.20` | `3889.04` | -293.06 USD | `-0.02%` | `20X Cross` |
| `1532` | `0xfce0...f4c0` | `SHORT` | 1,397,319.23 USD | `623.60` | `3129.61` | `2240.20` | `2801.14` | 554,307.36 USD | `+39.67%` | `20X Cross` |
| `1581` | `0xad02...eb65` | `LONG` | 1,345,629.50 USD | `600.62` | `2460.69` | `2240.20` | `1078.87` | -132,311.06 USD | `-9.83%` | `5X Cross` |
| `1582` | `0x638f...f5f0` | `LONG` | 1,344,720.00 USD | `600.00` | `4011.50` | `2240.20` | `314.13` | -1,062,183.53 USD | `-78.99%` | `25X Cross` |
| `1584` | `0x26e6...6b28` | `LONG` | 1,344,438.00 USD | `600.00` | `1769.78` | `2240.20` | `2004.67` | 282,566.47 USD | `+21.02%` | `20X Cross` |
| `1585` | `0x24fb...ed0f` | `LONG` | 1,344,395.07 USD | `600.10` | `2199.85` | `2240.20` | `0.000000` | 24,271.63 USD | `+1.81%` | `15X Cross` |
| `1637` | `0xfc27...9d9d` | `LONG` | 1,288,700.51 USD | `575.13` | `2243.19` | `2240.20` | `0.000000` | -1,433.69 USD | `-0.11%` | `25X Cross` |
| `1652` | `0xfc66...ca06` | `SHORT` | 1,273,035.71 USD | `567.43` | `2275.19` | `2240.20` | `7319.62` | 17,987.50 USD | `+1.41%` | `20X Cross` |
| `1654` | `0x9362...7d7c` | `SHORT` | 1,271,426.22 USD | `566.99` | `2226.19` | `2240.20` | `2518.85` | -9,190.41 USD | `-0.72%` | `20X Cross` |
| `1662` | `0xfb99...37f3` | `LONG` | 1,267,720.88 USD | `565.34` | `2362.35` | `2240.20` | `1241.40` | -67,815.47 USD | `-5.35%` | `3X Cross` |
| `1673` | `0x844b...7f42` | `SHORT` | 1,257,986.40 USD | `561.00` | `2026.17` | `2240.20` | `3005.86` | -121,302.99 USD | `-9.64%` | `25X Cross` |
| `1687` | `0xabe6...1d99` | `SHORT` | 1,245,671.36 USD | `556.00` | `2484.68` | `2240.20` | `3097.26` | 135,824.53 USD | `+10.90%` | `20X Cross` |
| `1689` | `0x2a76...9a53` | `LONG` | 1,243,344.10 USD | `554.99` | `2231.40` | `2240.20` | `0.000000` | 4,937.04 USD | `+0.40%` | `25X Cross` |
| `1702` | `0x936c...bb0f` | `LONG` | 1,232,600.03 USD | `550.09` | `2218.31` | `2240.20` | `0.000000` | 12,332.75 USD | `+1.00%` | `20X Cross` |
| `1705` | `0x825c...465e` | `LONG` | 1,232,220.00 USD | `550.00` | `2208.12` | `2240.20` | `1189.46` | 17,750.50 USD | `+1.44%` | `4X Cross` |
| `1710` | `0xad21...fb6a` | `LONG` | 1,226,509.92 USD | `547.26` | `2565.80` | `2240.20` | `1724.87` | -177,643.08 USD | `-14.48%` | `6X Cross` |
| `1813` | `0x0c7a...2f50` | `SHORT` | 1,140,964.09 USD | `509.25` | `2122.56` | `2240.20` | `4103.87` | -60,058.66 USD | `-5.26%` | `20X Cross` |
| `1817` | `0x0089...2410` | `SHORT` | 1,136,707.82 USD | `507.35` | `2308.88` | `2240.20` | `3399.47` | 34,692.44 USD | `+3.05%` | `20X Cross` |
| `1833` | `0xa559...ff95` | `LONG` | 1,121,000.00 USD | `500.00` | `2260.68` | `2240.20` | `1046.04` | -9,344.36 USD | `-0.83%` | `20X Cross` |
| `1834` | `0x4044...794c` | `LONG` | 1,121,000.00 USD | `500.00` | `2260.80` | `2240.20` | `0.000000` | -9,400.00 USD | `-0.84%` | `25X Cross` |
| `1835` | `0x89b2...9ca6` | `LONG` | 1,120,750.00 USD | `500.00` | `2363.45` | `2240.20` | `1622.65` | -60,977.42 USD | `-5.44%` | `25X Cross` |
| `1838` | `0x6936...9417` | `SHORT` | 1,120,365.00 USD | `500.00` | `2315.11` | `2240.20` | `2358.91` | 37,190.21 USD | `+3.32%` | `25X Isolated` |
| `1839` | `0xe282...df29` | `LONG` | 1,120,200.00 USD | `500.00` | `2309.84` | `2240.20` | `2045.31` | -34,724.21 USD | `-3.10%` | `10X Isolated` |
| `1840` | `0xb322...d51f` | `SHORT` | 1,120,200.00 USD | `500.00` | `2268.03` | `2240.20` | `3779.66` | 13,816.32 USD | `+1.23%` | `20X Cross` |
| `1845` | `0x7298...7d6c` | `SHORT` | 1,117,049.99 USD | `498.15` | `3426.75` | `2240.20` | `5421.61` | 589,985.83 USD | `+52.82%` | `20X Cross` |
| `1856` | `0x9c68...7783` | `SHORT` | 1,106,193.41 USD | `493.31` | `2273.58` | `2240.20` | `3961.44` | 15,385.84 USD | `+1.39%` | `25X Cross` |
| `1864` | `0x404c...5f03` | `SHORT` | 1,098,833.32 USD | `489.79` | `2671.94` | `2240.20` | `4966.25` | 209,846.24 USD | `+19.10%` | `20X Cross` |
| `1866` | `0x321f...1c84` | `SHORT` | 1,094,276.93 USD | `488.02` | `2370.09` | `2240.20` | `3050.82` | 62,367.67 USD | `+5.70%` | `10X Cross` |
| `1874` | `0x31de...13f2` | `LONG` | 1,089,442.21 USD | `486.29` | `2251.70` | `2240.20` | `0.000000` | -5,545.93 USD | `-0.51%` | `20X Cross` |
| `1918` | `0xe86b...3664` | `LONG` | 1,048,070.85 USD | `467.39` | `2231.29` | `2240.20` | `0.000000` | 5,189.92 USD | `+0.50%` | `25X Cross` |
| `1933` | `0x94b6...e5b3` | `SHORT` | 1,039,784.09 USD | `463.86` | `2261.12` | `2240.20` | `2396.65` | 9,058.58 USD | `+0.87%` | `25X Cross` |
| `1939` | `0x82c6...fe42` | `LONG` | 1,036,337.62 USD | `462.50` | `2501.38` | `2240.20` | `2053.65` | -120,552.94 USD | `-11.63%` | `5X Isolated` |
| `1943` | `0x71d0...8c26` | `LONG` | 1,034,719.74 USD | `461.87` | `2225.97` | `2240.20` | `0.000000` | 6,614.74 USD | `+0.64%` | `25X Cross` |
| `1944` | `0xe330...77a1` | `SHORT` | 1,034,197.12 USD | `461.20` | `2206.97` | `2240.20` | `6423.18` | -16,339.76 USD | `-1.58%` | `20X Cross` |
| `1949` | `0x2de3...486d` | `LONG` | 1,031,480.16 USD | `460.40` | `2286.27` | `2240.20` | `1179.06` | -21,120.75 USD | `-2.05%` | `25X Cross` |
| `1956` | `0x617e...0f97` | `SHORT` | 1,025,822.78 USD | `457.85` | `2205.60` | `2240.20` | `3365.10` | -15,978.95 USD | `-1.56%` | `10X Cross` |
| `1958` | `0x34fb...93de` | `LONG` | 1,024,907.21 USD | `457.40` | `2219.83` | `2240.20` | `0.000000` | 9,557.46 USD | `+0.93%` | `20X Cross` |
| `1996` | `0x0514...bdfe` | `SHORT` | 1,010,160.00 USD | `450.00` | `1988.74` | `2240.20` | `3735.05` | -115,223.16 USD | `-11.41%` | `25X Cross` |
| `1998` | `0xc10f...23b3` | `LONG` | 1,009,017.00 USD | `450.00` | `2366.44` | `2240.20` | `2016.72` | -55,881.27 USD | `-5.54%` | `25X Cross` |
| `1999` | `0xae55...2236` | `LONG` | 1,008,540.00 USD | `450.00` | `2510.21` | `2240.20` | `0.000000` | -121,057.50 USD | `-12.00%` | `25X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `2739.00` | 83,040.45 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 83.04K USD at 2739.0000 USD [API] | `2026-09-29 12:15:35` |
| `ANNOUNCEMENT` | `INFO` | `2308.40` | 41,987.26 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 41.99K USD at 2308.4000 USD [API] | `2026-10-29 03:43:57` |
| `ANNOUNCEMENT` | `INFO` | `2308.40` | 40,056.74 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.06K USD at 2308.4000 USD [API] | `2026-10-29 03:43:57` |
| `ANNOUNCEMENT` | `INFO` | `2308.40` | 115,537.73 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 115.54K USD at 2308.4000 USD [API] | `2026-10-29 03:43:57` |
| `ANNOUNCEMENT` | `INFO` | `2308.40` | 136,902.43 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 136.90K USD at 2308.4000 USD [API] | `2026-10-29 03:43:57` |
| `ANNOUNCEMENT` | `INFO` | `2362.70` | 42.29 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.04K USD at 2362.7000 USD [API] | `2026-10-27 21:33:33` |
| `ANNOUNCEMENT` | `INFO` | `2362.70` | 36.62 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.04K USD at 2362.7000 USD [API] | `2026-10-27 21:33:33` |
| `ANNOUNCEMENT` | `INFO` | `1592.40` | 11,956.69 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 11.96K USD at 1592.4000 USD [API] | `2026-06-24 16:51:42` |
| `ANNOUNCEMENT` | `INFO` | `2375.40` | 17,545.42 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 17.55K USD at 2375.4000 USD [API] | `2026-10-28 08:26:36` |
| `ANNOUNCEMENT` | `INFO` | `2309.50` | 46,190.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 46.19K USD at 2309.5000 USD [API] | `2026-10-29 04:24:02` |
| `ANNOUNCEMENT` | `INFO` | `2325.50` | 145,724.90 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 145.72K USD at 2325.5000 USD [API] | `2026-10-29 05:05:15` |
| `ANNOUNCEMENT` | `INFO` | `2325.50` | 59,066.77 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 59.07K USD at 2325.5000 USD [API] | `2026-10-29 05:05:15` |
| `ANNOUNCEMENT` | `INFO` | `2325.50` | 94,775.52 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 94.78K USD at 2325.5000 USD [API] | `2026-10-29 05:05:15` |
| `ANNOUNCEMENT` | `INFO` | `2292.40` | 14,347.44 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 14.35K USD at 2292.4000 USD [API] | `2026-10-29 02:36:05` |
| `ANNOUNCEMENT` | `INFO` | `2292.40` | 4,279.91 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 4.28K USD at 2292.4000 USD [API] | `2026-10-29 02:36:05` |
| `ANNOUNCEMENT` | `INFO` | `2292.40` | 1,975.13 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.98K USD at 2292.4000 USD [API] | `2026-10-29 02:36:05` |
| `ANNOUNCEMENT` | `INFO` | `2293.50` | 22.93 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2293.5000 USD [API] | `2026-10-29 02:36:02` |
| `ANNOUNCEMENT` | `INFO` | `2295.60` | 18,364.34 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 18.36K USD at 2295.6000 USD [API] | `2026-10-29 02:31:00` |
| `ANNOUNCEMENT` | `INFO` | `2295.60` | 5,870.54 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 5.87K USD at 2295.6000 USD [API] | `2026-10-29 02:31:00` |
| `ANNOUNCEMENT` | `INFO` | `2296.60` | 18,298.85 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 18.30K USD at 2296.6000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `2296.60` | 3,147.95 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 3.15K USD at 2296.6000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `2296.60` | 189.47 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.19K USD at 2296.6000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `2296.60` | 1,020.38 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.02K USD at 2296.6000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `2296.60` | 755.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.76K USD at 2296.6000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `2324.10` | 1,329.62 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.33K USD at 2324.1000 USD [API] | `2026-10-29 01:48:08` |
| `ANNOUNCEMENT` | `INFO` | `2325.70` | 22,155.32 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 22.16K USD at 2325.7000 USD [API] | `2026-10-29 01:48:04` |
| `ANNOUNCEMENT` | `INFO` | `2328.20` | 15.37 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2328.2000 USD [API] | `2026-10-29 01:45:39` |
| `ANNOUNCEMENT` | `INFO` | `2326.40` | 45,946.40 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 45.95K USD at 2326.4000 USD [API] | `2026-10-29 05:07:16` |
| `ANNOUNCEMENT` | `INFO` | `2326.20` | 73,539.56 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 73.54K USD at 2326.2000 USD [API] | `2026-10-29 05:07:10` |
| `ANNOUNCEMENT` | `INFO` | `2974.40` | 2,185.89 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.19K USD at 2974.4000 USD [API] | `2025-11-25 22:58:18` |
| `ANNOUNCEMENT` | `INFO` | `2974.40` | 184.41 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.18K USD at 2974.4000 USD [API] | `2025-11-25 22:58:18` |
| `ANNOUNCEMENT` | `INFO` | `2920.50` | 4,440.91 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 4.44K USD at 2920.5000 USD [API] | `2025-11-25 01:57:27` |
| `ANNOUNCEMENT` | `INFO` | `2328.30` | 46,566.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 46.57K USD at 2328.3000 USD [API] | `2026-10-29 05:11:13` |
| `ANNOUNCEMENT` | `INFO` | `2330.20` | 40,000.21 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.00K USD at 2330.2000 USD [API] | `2026-10-29 05:15:56` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2296.42` (Vol: 23,400,000.00 USD, Dist: `+2.12%`) | Long MP=`2174.37` (Vol: 35,800,000.00 USD, Dist: `--3.31%`)
  * 48H Horizon: Short MP=`2402.29` (Vol: 24,100,000.00 USD, Dist: `+6.83%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--3.32%`)
  * 3D Horizon: Short MP=`2402.29` (Vol: 29,900,000.00 USD, Dist: `+6.83%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--3.32%`)
  * 7D Horizon: Short MP=`2401.80` (Vol: 50,700,000.00 USD, Dist: `+6.81%`) | Long MP=`2175.27` (Vol: 44,800,000.00 USD, Dist: `--3.27%`)
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
| `7D` | `Long Liquidation` | `1972.30` | 960,310,000.00 USD | 960,310,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,810,000.00 USD | 209,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1975.60` | 960,180,000.00 USD | 960,180,000.00 USD | 2,240,000.00 USD | 0.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1982.20` | 957,890,000.00 USD | 957,890,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1985.00` | 5,620,000.00 USD | 208,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1985.50` | 957,680,000.00 USD | 957,680,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1988.80` | 955,390,000.00 USD | 955,390,000.00 USD | 1,440,000.00 USD | 1,780,000.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1992.10` | 952,140,000.00 USD | 952,140,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1995.00` | 1,490,000.00 USD | 202,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1995.40` | 949,430,000.00 USD | 949,430,000.00 USD | 1,340,000.00 USD | 0.00 USD | 808,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2002.70` | 676,840,000.00 USD | 676,840,000.00 USD | 0.00 USD | 217,070.00 USD | 10,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2005.00` | 2,050,000.00 USD | 200,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2005.20` | 676,620,000.00 USD | 676,620,000.00 USD | 14,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2005.30` | 947,280,000.00 USD | 947,280,000.00 USD | 0.00 USD | 266,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2007.70` | 676,600,000.00 USD | 676,600,000.00 USD | 0.00 USD | 224,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2010.20` | 676,380,000.00 USD | 676,380,000.00 USD | 0.00 USD | 308,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2011.90` | 947,010,000.00 USD | 947,010,000.00 USD | 170,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2012.70` | 676,070,000.00 USD | 676,070,000.00 USD | 299,090.00 USD | 210,450.00 USD | 21,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2015.00` | 2,810,000.00 USD | 198,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2015.20` | 675,540,000.00 USD | 675,540,000.00 USD | 355,800.00 USD | 51,960.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2017.70` | 675,130,000.00 USD | 675,130,000.00 USD | 483,920.00 USD | 1,350,000.00 USD | 553,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2020.20` | 672,740,000.00 USD | 672,740,000.00 USD | 548,260.00 USD | 1,010,000.00 USD | 403,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2022.70` | 670,780,000.00 USD | 670,780,000.00 USD | 751,210.00 USD | 178,550.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 834,860.00 USD | 196,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2025.10` | 946,840,000.00 USD | 946,840,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2025.20` | 668,370,000.00 USD | 668,370,000.00 USD | 122,610.00 USD | 914,780.00 USD | 28,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2027.70` | 667,300,000.00 USD | 667,300,000.00 USD | 1,430,000.00 USD | 1,160,000.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.40` | 946,660,000.00 USD | 946,660,000.00 USD | 0.00 USD | 0.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2030.20` | 664,700,000.00 USD | 664,700,000.00 USD | 87,180.00 USD | 366,120.00 USD | 957,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.70` | 946,630,000.00 USD | 946,630,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.70` | 663,290,000.00 USD | 663,290,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2035.00` | 942,060,000.00 USD | 942,060,000.00 USD | 146,420.00 USD | 186,130.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 588,290.00 USD | 195,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2035.20` | 659,730,000.00 USD | 659,730,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2037.70` | 658,390,000.00 USD | 658,390,000.00 USD | 396,700.00 USD | 458,110.00 USD | 388,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.30` | 940,370,000.00 USD | 940,370,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2040.20` | 657,150,000.00 USD | 657,150,000.00 USD | 542,670.00 USD | 178,560.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2042.70` | 656,400,000.00 USD | 656,400,000.00 USD | 626,840.00 USD | 0.00 USD | 174,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2044.90` | 938,920,000.00 USD | 938,920,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 1,980,000.00 USD | 194,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2045.20` | 655,600,000.00 USD | 655,600,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2047.70` | 655,570,000.00 USD | 655,570,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.20` | 654,750,000.00 USD | 654,750,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2051.50` | 938,620,000.00 USD | 938,620,000.00 USD | 222,640.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2054.80` | 937,210,000.00 USD | 937,210,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 7,180,000.00 USD | 192,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2055.20` | 653,640,000.00 USD | 653,640,000.00 USD | 242,080.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2058.10` | 936,110,000.00 USD | 936,110,000.00 USD | 56,430.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2060.20` | 653,280,000.00 USD | 653,280,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.40` | 935,870,000.00 USD | 935,870,000.00 USD | 1,700,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2062.70` | 652,530,000.00 USD | 652,530,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.70` | 930,510,000.00 USD | 930,510,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 14,780,000.00 USD | 185,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2065.20` | 652,450,000.00 USD | 652,450,000.00 USD | 563,140.00 USD | 537,030.00 USD | 510,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2067.70` | 650,840,000.00 USD | 650,840,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2068.00` | 928,050,000.00 USD | 928,050,000.00 USD | 1,740,000.00 USD | 1,920,000.00 USD | 893,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2070.20` | 650,140,000.00 USD | 650,140,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.30` | 923,490,000.00 USD | 923,490,000.00 USD | 2,780,000.00 USD | 2,310,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2072.70` | 649,770,000.00 USD | 649,770,000.00 USD | 67,060.00 USD | 555,250.00 USD | 428,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.60` | 917,170,000.00 USD | 917,170,000.00 USD | 4,000,000.00 USD | 3,180,000.00 USD | 3,740,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 1,590,000.00 USD | 170,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2075.20` | 648,720,000.00 USD | 648,720,000.00 USD | 421,860.00 USD | 224,070.00 USD | 91,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2077.70` | 647,980,000.00 USD | 647,980,000.00 USD | 1,190,000.00 USD | 765,660.00 USD | 422,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2077.90` | 906,260,000.00 USD | 906,260,000.00 USD | 5,570,000.00 USD | 4,500,000.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2080.20` | 645,600,000.00 USD | 645,600,000.00 USD | 586,070.00 USD | 932,020.00 USD | 206,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.20` | 893,460,000.00 USD | 893,460,000.00 USD | 5,010,000.00 USD | 2,990,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2082.70` | 643,880,000.00 USD | 643,880,000.00 USD | 858,220.00 USD | 305,810.00 USD | 215,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.50` | 882,970,000.00 USD | 882,970,000.00 USD | 2,500,000.00 USD | 1,960,000.00 USD | 4,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 13,710,000.00 USD | 169,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2085.20` | 642,500,000.00 USD | 642,500,000.00 USD | 1,380,000.00 USD | 785,030.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2087.70` | 639,070,000.00 USD | 639,070,000.00 USD | 1,460,000.00 USD | 573,160.00 USD | 682,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2087.80` | 874,320,000.00 USD | 874,320,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2090.20` | 636,350,000.00 USD | 636,350,000.00 USD | 1,030,000.00 USD | 214,870.00 USD | 258,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.10` | 865,190,000.00 USD | 865,190,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.70` | 634,850,000.00 USD | 634,850,000.00 USD | 768,770.00 USD | 345,550.00 USD | 588,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.40` | 852,230,000.00 USD | 852,230,000.00 USD | 5,720,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,700,000.00 USD | 155,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2095.20` | 633,150,000.00 USD | 633,150,000.00 USD | 1,840,000.00 USD | 1,130,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2097.70` | 628,690,000.00 USD | 628,690,000.00 USD | 175,830.00 USD | 488,160.00 USD | 517,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.70` | 842,510,000.00 USD | 842,510,000.00 USD | 1,850,000.00 USD | 3,860,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2100.20` | 627,510,000.00 USD | 627,510,000.00 USD | 307,340.00 USD | 928,890.00 USD | 50,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.00` | 835,520,000.00 USD | 835,520,000.00 USD | 1,810,000.00 USD | 1,580,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.70` | 626,220,000.00 USD | 626,220,000.00 USD | 211,840.00 USD | 222,480.00 USD | 483,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2104.30` | 828,110,000.00 USD | 828,110,000.00 USD | 1,440,000.00 USD | 738,240.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 2,250,000.00 USD | 153,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2105.20` | 625,300,000.00 USD | 625,300,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 691,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.60` | 823,610,000.00 USD | 823,610,000.00 USD | 8,610,000.00 USD | 1,150,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2107.70` | 619,880,000.00 USD | 619,880,000.00 USD | 734,860.00 USD | 0.00 USD | 488,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.20` | 618,660,000.00 USD | 618,660,000.00 USD | 61,010.00 USD | 31,550.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2110.90` | 812,630,000.00 USD | 812,630,000.00 USD | 3,480,000.00 USD | 2,360,000.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2112.70` | 618,560,000.00 USD | 618,560,000.00 USD | 902,600.00 USD | 506,690.00 USD | 244,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2114.20` | 804,070,000.00 USD | 804,070,000.00 USD | 1,130,000.00 USD | 2,040,000.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,830,000.00 USD | 151,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2115.20` | 616,900,000.00 USD | 616,900,000.00 USD | 410,020.00 USD | 400,200.00 USD | 939,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.50` | 797,080,000.00 USD | 797,080,000.00 USD | 2,410,000.00 USD | 2,350,000.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2117.70` | 615,150,000.00 USD | 615,150,000.00 USD | 4,540,000.00 USD | 3,940,000.00 USD | 302,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.20` | 606,370,000.00 USD | 606,370,000.00 USD | 5,430,000.00 USD | 22,470.00 USD | 671,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2120.80` | 788,920,000.00 USD | 788,920,000.00 USD | 13,880,000.00 USD | 5,780,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2122.70` | 600,240,000.00 USD | 600,240,000.00 USD | 3,690,000.00 USD | 3,800,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.10` | 767,440,000.00 USD | 767,440,000.00 USD | 7,990,000.00 USD | 7,760,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,520,000.00 USD | 149,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.20` | 590,910,000.00 USD | 590,910,000.00 USD | 6,280,000.00 USD | 1,830,000.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.40` | 750,020,000.00 USD | 750,020,000.00 USD | 2,400,000.00 USD | 4,820,000.00 USD | 5,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2127.70` | 580,700,000.00 USD | 580,700,000.00 USD | 4,430,000.00 USD | 4,180,000.00 USD | 782,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2130.20` | 571,310,000.00 USD | 571,310,000.00 USD | 1,230,000.00 USD | 172,040.00 USD | 774,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.70` | 737,510,000.00 USD | 737,510,000.00 USD | 5,390,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2132.70` | 569,130,000.00 USD | 569,130,000.00 USD | 0.00 USD | 177,810.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.00` | 728,120,000.00 USD | 728,120,000.00 USD | 2,550,000.00 USD | 550,450.00 USD | 316,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 4,970,000.00 USD | 26,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2135.20` | 567,430,000.00 USD | 567,430,000.00 USD | 20,600.00 USD | 1,170,000.00 USD | 86,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.30` | 724,700,000.00 USD | 724,700,000.00 USD | 1,040,000.00 USD | 1,510,000.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2137.70` | 566,150,000.00 USD | 566,150,000.00 USD | 21,090.00 USD | 379,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2140.20` | 565,750,000.00 USD | 565,750,000.00 USD | 36,740.00 USD | 265,280.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.60` | 722,110,000.00 USD | 722,110,000.00 USD | 2,710,000.00 USD | 1,500,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2142.70` | 565,390,000.00 USD | 565,390,000.00 USD | 670,350.00 USD | 2,130,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2143.90` | 717,100,000.00 USD | 717,100,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 4,040,000.00 USD | 21,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2145.20` | 562,580,000.00 USD | 562,580,000.00 USD | 121,400.00 USD | 1,720,000.00 USD | 118,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2147.20` | 715,250,000.00 USD | 715,250,000.00 USD | 1,080,000.00 USD | 949,370.00 USD | 134,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2147.70` | 560,620,000.00 USD | 560,620,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 69,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2150.20` | 557,970,000.00 USD | 557,970,000.00 USD | 7,450,000.00 USD | 2,570,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.50` | 713,080,000.00 USD | 713,080,000.00 USD | 459,630.00 USD | 827,410.00 USD | 331,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2152.70` | 546,250,000.00 USD | 546,250,000.00 USD | 2,710,000.00 USD | 2,400,000.00 USD | 2,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2153.80` | 711,460,000.00 USD | 711,460,000.00 USD | 11,310,000.00 USD | 1,720,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 4,230,000.00 USD | 17,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2155.20` | 539,040,000.00 USD | 539,040,000.00 USD | 2,450,000.00 USD | 3,070,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2157.10` | 696,840,000.00 USD | 696,840,000.00 USD | 4,350,000.00 USD | 1,640,000.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2157.70` | 532,010,000.00 USD | 532,010,000.00 USD | 1,980,000.00 USD | 1,460,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2160.20` | 525,100,000.00 USD | 525,100,000.00 USD | 3,090,000.00 USD | 5,170,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.40` | 688,130,000.00 USD | 688,130,000.00 USD | 546,010.00 USD | 1,510,000.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2162.70` | 515,010,000.00 USD | 515,010,000.00 USD | 14,200,000.00 USD | 10,130,000.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.70` | 684,900,000.00 USD | 684,900,000.00 USD | 21,060,000.00 USD | 14,080,000.00 USD | 518,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 5,990,000.00 USD | 12,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2165.20` | 489,120,000.00 USD | 489,120,000.00 USD | 9,520,000.00 USD | 9,640,000.00 USD | 4,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2167.00` | 649,250,000.00 USD | 649,250,000.00 USD | 5,300,000.00 USD | 13,000,000.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.70` | 465,720,000.00 USD | 465,720,000.00 USD | 18,870,000.00 USD | 7,820,000.00 USD | 5,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.20` | 433,890,000.00 USD | 433,890,000.00 USD | 23,930,000.00 USD | 9,410,000.00 USD | 7,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.30` | 627,980,000.00 USD | 627,980,000.00 USD | 10,280,000.00 USD | 14,770,000.00 USD | 9,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2172.70` | 393,150,000.00 USD | 393,150,000.00 USD | 6,810,000.00 USD | 5,090,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.60` | 593,400,000.00 USD | 593,400,000.00 USD | 34,190,000.00 USD | 828,350.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 5,790,000.00 USD | 6,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.20` | 377,780,000.00 USD | 377,780,000.00 USD | 3,840,000.00 USD | 0.00 USD | 836,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2176.90` | 556,880,000.00 USD | 556,880,000.00 USD | 1,750,000.00 USD | 1,330,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2177.70` | 373,100,000.00 USD | 373,100,000.00 USD | 730,100.00 USD | 355,620.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2180.20` | 369,190,000.00 USD | 369,190,000.00 USD | 894,580.00 USD | 1,460,000.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2182.70` | 365,460,000.00 USD | 365,460,000.00 USD | 73,470.00 USD | 26,540.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2183.50` | 550,980,000.00 USD | 550,980,000.00 USD | 1,760,000.00 USD | 1,310,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 800,690.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2185.20` | 362,330,000.00 USD | 362,330,000.00 USD | 310,640.00 USD | 1,660,000.00 USD | 4,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2186.80` | 543,980,000.00 USD | 543,980,000.00 USD | 37,310,000.00 USD | 17,750,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2187.70` | 355,370,000.00 USD | 355,370,000.00 USD | 3,960,000.00 USD | 1,250,000.00 USD | 3,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.10` | 488,920,000.00 USD | 488,920,000.00 USD | 12,430,000.00 USD | 27,500,000.00 USD | 4,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2190.20` | 346,590,000.00 USD | 346,590,000.00 USD | 4,530,000.00 USD | 4,030,000.00 USD | 5,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2192.70` | 332,960,000.00 USD | 332,960,000.00 USD | 4,930,000.00 USD | 4,710,000.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2193.40` | 444,410,000.00 USD | 444,410,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,080,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 152,660.00 USD | 292,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2195.20` | 322,100,000.00 USD | 322,100,000.00 USD | 5,560,000.00 USD | 1,880,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.70` | 428,990,000.00 USD | 428,990,000.00 USD | 383,690.00 USD | 243,760.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2197.70` | 310,640,000.00 USD | 310,640,000.00 USD | 4,440,000.00 USD | 1,140,000.00 USD | 4,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.00` | 426,320,000.00 USD | 426,320,000.00 USD | 0.00 USD | 0.00 USD | 5,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.20` | 300,850,000.00 USD | 300,850,000.00 USD | 4,980,000.00 USD | 2,340,000.00 USD | 7,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2202.70` | 285,770,000.00 USD | 285,770,000.00 USD | 3,630,000.00 USD | 4,690,000.00 USD | 5,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.30` | 420,920,000.00 USD | 420,920,000.00 USD | 4,310,000.00 USD | 0.00 USD | 7,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 140,270.00 USD | 140,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.20` | 272,330,000.00 USD | 272,330,000.00 USD | 1,810,000.00 USD | 574,970.00 USD | 681,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2206.60` | 408,950,000.00 USD | 408,950,000.00 USD | 1,490,000.00 USD | 588,950.00 USD | 4,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2207.70` | 269,260,000.00 USD | 269,260,000.00 USD | 0.00 USD | 4,250,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2209.90` | 402,220,000.00 USD | 402,220,000.00 USD | 0.00 USD | 0.00 USD | 11,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.20` | 265,010,000.00 USD | 265,010,000.00 USD | 104,760.00 USD | 399,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.70` | 264,500,000.00 USD | 264,500,000.00 USD | 3,780,000.00 USD | 5,190,000.00 USD | 39,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2213.20` | 390,930,000.00 USD | 390,930,000.00 USD | 1,710,000.00 USD | 1,060,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2215.20` | 255,490,000.00 USD | 255,490,000.00 USD | 2,150,000.00 USD | 2,640,000.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2216.50` | 386,200,000.00 USD | 386,200,000.00 USD | 0.00 USD | 487,520.00 USD | 495,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2217.70` | 250,600,000.00 USD | 250,600,000.00 USD | 2,100,000.00 USD | 1,490,000.00 USD | 92,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2219.80` | 385,220,000.00 USD | 385,220,000.00 USD | 22,400,000.00 USD | 1,200,000.00 USD | 3,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2220.20` | 246,920,000.00 USD | 246,920,000.00 USD | 6,760,000.00 USD | 865,980.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2222.70` | 236,330,000.00 USD | 236,330,000.00 USD | 9,870,000.00 USD | 6,090,000.00 USD | 5,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2223.10` | 357,920,000.00 USD | 357,920,000.00 USD | 9,430,000.00 USD | 13,660,000.00 USD | 25,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2225.20` | 214,850,000.00 USD | 214,850,000.00 USD | 14,150,000.00 USD | 2,980,000.00 USD | 13,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2226.40` | 309,250,000.00 USD | 309,250,000.00 USD | 969,390.00 USD | 12,680,000.00 USD | 14,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.70` | 184,710,000.00 USD | 184,710,000.00 USD | 20,040,000.00 USD | 17,080,000.00 USD | 2,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.70` | 281,220,000.00 USD | 281,220,000.00 USD | 48,530,000.00 USD | 33,560,000.00 USD | 23,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.20` | 145,470,000.00 USD | 145,470,000.00 USD | 29,540,000.00 USD | 1,030,000.00 USD | 7,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2232.70` | 107,430,000.00 USD | 107,430,000.00 USD | 26,430,000.00 USD | 6,600,000.00 USD | 21,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2233.00` | 175,340,000.00 USD | 175,340,000.00 USD | 23,810,000.00 USD | 46,390,000.00 USD | 25,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2235.20` | 53,230,000.00 USD | 53,230,000.00 USD | 22,090,000.00 USD | 0.00 USD | 20,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2236.30` | 79,680,000.00 USD | 79,680,000.00 USD | 30,150,000.00 USD | 23,260,000.00 USD | 26,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2237.70` | 10,730,000.00 USD | 10,730,000.00 USD | 8,000,000.00 USD | 0.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2239.60` | 49,490,000.00 USD | 49,490,000.00 USD | 41,160,000.00 USD | 0.00 USD | 8,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2240.20` | 12,140,000.00 USD | 12,140,000.00 USD | 7,220,000.00 USD | 0.00 USD | 4,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2242.70` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 141,810.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2242.90` | 54,320,000.00 USD | 54,320,000.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2245.00` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2245.20` | 14,030,000.00 USD | 14,030,000.00 USD | 0.00 USD | 1,650,000.00 USD | 45,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2246.20` | 57,500,000.00 USD | 57,500,000.00 USD | 2,040,000.00 USD | 1,030,000.00 USD | 102,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2247.70` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 16,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2249.50` | 64,920,000.00 USD | 64,920,000.00 USD | 3,510,000.00 USD | 2,660,000.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2250.20` | 20,200,000.00 USD | 20,200,000.00 USD | 5,930,000.00 USD | 166,850.00 USD | 55,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2252.70` | 32,510,000.00 USD | 32,510,000.00 USD | 10,870,000.00 USD | 122,810.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2252.80` | 95,300,000.00 USD | 95,300,000.00 USD | 21,510,000.00 USD | 8,880,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 202,140.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2255.20` | 49,270,000.00 USD | 49,270,000.00 USD | 5,590,000.00 USD | 8,490,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2256.10` | 119,400,000.00 USD | 119,400,000.00 USD | 13,070,000.00 USD | 10,520,000.00 USD | 514,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2257.70` | 76,780,000.00 USD | 76,780,000.00 USD | 16,850,000.00 USD | 6,780,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2259.40` | 142,760,000.00 USD | 142,760,000.00 USD | 11,860,000.00 USD | 7,450,000.00 USD | 4,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2260.20` | 97,650,000.00 USD | 97,650,000.00 USD | 9,700,000.00 USD | 9,260,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2262.70` | 120,560,000.00 USD | 120,560,000.00 USD | 11,070,000.00 USD | 8,850,000.00 USD | 2,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2262.70` | 151,140,000.00 USD | 151,140,000.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 210,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 4,500,000.00 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2265.20` | 147,460,000.00 USD | 147,460,000.00 USD | 7,780,000.00 USD | 8,270,000.00 USD | 10,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2266.00` | 163,120,000.00 USD | 163,120,000.00 USD | 0.00 USD | 5,650,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2267.70` | 169,160,000.00 USD | 169,160,000.00 USD | 9,840,000.00 USD | 6,210,000.00 USD | 5,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2269.30` | 176,400,000.00 USD | 176,400,000.00 USD | 8,610,000.00 USD | 0.00 USD | 4,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2270.20` | 194,590,000.00 USD | 194,590,000.00 USD | 7,970,000.00 USD | 3,900,000.00 USD | 13,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2272.60` | 189,450,000.00 USD | 189,450,000.00 USD | 7,540,000.00 USD | 1,480,000.00 USD | 4,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2272.70` | 200,610,000.00 USD | 200,610,000.00 USD | 3,630,000.00 USD | 1,290,000.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 79,460.00 USD | 6,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2275.20` | 229,610,000.00 USD | 229,610,000.00 USD | 12,590,000.00 USD | 15,020,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2275.90` | 194,950,000.00 USD | 194,950,000.00 USD | 0.00 USD | 5,500,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2277.70` | 252,930,000.00 USD | 252,930,000.00 USD | 3,520,000.00 USD | 10,200,000.00 USD | 9,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2279.20` | 230,490,000.00 USD | 230,490,000.00 USD | 854,200.00 USD | 24,150,000.00 USD | 10,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2280.20` | 297,840,000.00 USD | 297,840,000.00 USD | 27,000,000.00 USD | 10,110,000.00 USD | 7,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.50` | 326,340,000.00 USD | 326,340,000.00 USD | 0.00 USD | 82,170,000.00 USD | 13,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2282.70` | 363,520,000.00 USD | 363,520,000.00 USD | 28,520,000.00 USD | 26,750,000.00 USD | 10,420,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 167,510.00 USD | 6,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2285.20` | 384,430,000.00 USD | 384,430,000.00 USD | 9,620,000.00 USD | 8,450,000.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2285.80` | 350,110,000.00 USD | 350,110,000.00 USD | 6,610,000.00 USD | 17,060,000.00 USD | 105,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2287.70` | 414,060,000.00 USD | 414,060,000.00 USD | 12,690,000.00 USD | 8,930,000.00 USD | 8,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2289.10` | 382,120,000.00 USD | 382,120,000.00 USD | 8,380,000.00 USD | 8,650,000.00 USD | 14,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2290.20` | 444,690,000.00 USD | 444,690,000.00 USD | 14,400,000.00 USD | 13,200,000.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2292.40` | 395,380,000.00 USD | 395,380,000.00 USD | 7,890,000.00 USD | 0.00 USD | 5,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2292.70` | 470,720,000.00 USD | 470,720,000.00 USD | 13,200,000.00 USD | 3,480,000.00 USD | 9,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 2,440,000.00 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2295.20` | 497,460,000.00 USD | 497,460,000.00 USD | 6,720,000.00 USD | 11,490,000.00 USD | 8,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2295.70` | 436,900,000.00 USD | 436,900,000.00 USD | 23,390,000.00 USD | 6,820,000.00 USD | 11,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2297.70` | 537,150,000.00 USD | 537,150,000.00 USD | 22,140,000.00 USD | 12,350,000.00 USD | 5,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.00` | 463,950,000.00 USD | 463,950,000.00 USD | 4,220,000.00 USD | 17,180,000.00 USD | 5,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2300.20` | 573,300,000.00 USD | 573,300,000.00 USD | 9,490,000.00 USD | 13,100,000.00 USD | 13,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.30` | 540,590,000.00 USD | 540,590,000.00 USD | 37,120,000.00 USD | 17,380,000.00 USD | 22,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.70` | 601,900,000.00 USD | 601,900,000.00 USD | 18,950,000.00 USD | 2,400,000.00 USD | 7,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 158,470.00 USD | 9,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.20` | 640,960,000.00 USD | 640,960,000.00 USD | 14,750,000.00 USD | 18,210,000.00 USD | 6,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.60` | 566,610,000.00 USD | 566,610,000.00 USD | 6,340,000.00 USD | 8,820,000.00 USD | 10,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2307.70` | 652,460,000.00 USD | 652,460,000.00 USD | 4,370,000.00 USD | 3,930,000.00 USD | 3,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2308.90` | 569,930,000.00 USD | 569,930,000.00 USD | 1,920,000.00 USD | 930,630.00 USD | 472,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2310.20` | 671,730,000.00 USD | 671,730,000.00 USD | 5,900,000.00 USD | 2,720,000.00 USD | 10,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2312.20` | 599,240,000.00 USD | 599,240,000.00 USD | 10,780,000.00 USD | 2,650,000.00 USD | 15,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2312.70` | 683,930,000.00 USD | 683,930,000.00 USD | 4,670,000.00 USD | 7,190,000.00 USD | 338,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 1,160,000.00 USD | 10,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2315.20` | 705,230,000.00 USD | 705,230,000.00 USD | 4,180,000.00 USD | 11,100,000.00 USD | 6,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2315.50` | 607,990,000.00 USD | 607,990,000.00 USD | 0.00 USD | 8,120,000.00 USD | 627,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2317.70` | 724,440,000.00 USD | 724,440,000.00 USD | 6,110,000.00 USD | 10,220,000.00 USD | 2,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2318.80` | 625,500,000.00 USD | 625,500,000.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 8,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.20` | 748,200,000.00 USD | 748,200,000.00 USD | 9,790,000.00 USD | 11,280,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.10` | 642,660,000.00 USD | 642,660,000.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 108,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2322.70` | 762,000,000.00 USD | 762,000,000.00 USD | 1,730,000.00 USD | 8,480,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,790,000.00 USD | 12,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2325.20` | 774,420,000.00 USD | 774,420,000.00 USD | 1,950,000.00 USD | 8,990,000.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2325.40` | 663,730,000.00 USD | 663,730,000.00 USD | 10,150,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2327.70` | 780,450,000.00 USD | 780,450,000.00 USD | 494,310.00 USD | 1,140,000.00 USD | 4,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.70` | 675,970,000.00 USD | 675,970,000.00 USD | 3,860,000.00 USD | 363,770.00 USD | 8,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2330.20` | 796,480,000.00 USD | 796,480,000.00 USD | 12,730,000.00 USD | 2,830,000.00 USD | 479,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2332.00` | 705,210,000.00 USD | 705,210,000.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2332.70` | 822,160,000.00 USD | 822,160,000.00 USD | 14,210,000.00 USD | 1,980,000.00 USD | 9,490,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 1,390,000.00 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2335.20` | 842,720,000.00 USD | 842,720,000.00 USD | 14,300,000.00 USD | 4,300,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2335.30` | 763,710,000.00 USD | 763,710,000.00 USD | 26,630,000.00 USD | 19,830,000.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2337.70` | 855,540,000.00 USD | 855,540,000.00 USD | 6,870,000.00 USD | 999,990.00 USD | 4,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.60` | 790,210,000.00 USD | 790,210,000.00 USD | 15,880,000.00 USD | 0.00 USD | 10,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2340.20` | 880,800,000.00 USD | 880,800,000.00 USD | 8,850,000.00 USD | 5,380,000.00 USD | 11,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2341.90` | 826,740,000.00 USD | 826,740,000.00 USD | 4,720,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2342.70` | 895,080,000.00 USD | 895,080,000.00 USD | 5,180,000.00 USD | 6,350,000.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 416,450.00 USD | 14,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2345.20` | 914,460,000.00 USD | 914,460,000.00 USD | 4,550,000.00 USD | 6,130,000.00 USD | 8,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2345.20` | 857,900,000.00 USD | 857,900,000.00 USD | 1,350,000.00 USD | 21,160,000.00 USD | 8,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2347.70` | 924,030,000.00 USD | 924,030,000.00 USD | 3,700,000.00 USD | 3,280,000.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.50` | 895,770,000.00 USD | 895,770,000.00 USD | 847,620.00 USD | 9,500,000.00 USD | 27,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.20` | 970,560,000.00 USD | 970,560,000.00 USD | 28,240,000.00 USD | 7,790,000.00 USD | 10,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2351.80` | 928,640,000.00 USD | 928,640,000.00 USD | 2,640,000.00 USD | 19,600,000.00 USD | 10,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2352.70` | 979,880,000.00 USD | 979,880,000.00 USD | 4,190,000.00 USD | 2,860,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,230,000.00 USD | 15,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2355.10` | 989,170,000.00 USD | 989,170,000.00 USD | 18,880,000.00 USD | 40,150,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2355.20` | 992,110,000.00 USD | 992,110,000.00 USD | 2,930,000.00 USD | 7,680,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.70` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 4,070,000.00 USD | 4,660,000.00 USD | 3,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.40` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 7,400,000.00 USD | 1,840,000.00 USD | 6,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.20` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 10,050,000.00 USD | 3,880,000.00 USD | 5,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.70` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 3,150,000.00 USD | 3,430,000.00 USD | 431,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.70` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 7,480,000.00 USD | 6,710,000.00 USD | 7,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2365.00` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 10,200,000.00 USD | 373,740.00 USD | 10,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 4,040,000.00 USD | 19,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2365.20` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 4,830,000.00 USD | 3,140,000.00 USD | 3,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.70` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 3,130,000.00 USD | 1,110,000.00 USD | 1,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.30` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 424,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.20` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 12,570,000.00 USD | 8,560,000.00 USD | 6,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.60` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 26,000,000.00 USD | 0.00 USD | 54,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.70` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 14,240,000.00 USD | 2,610,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2374.90` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 5,640,000.00 USD | 25,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2375.20` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 10,840,000.00 USD | 757,510.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2377.70` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 1,460,000.00 USD | 3,270,000.00 USD | 4,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.20` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 11,180,000.00 USD | 7,790,000.00 USD | 25,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.20` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 6,310,000.00 USD | 389,290.00 USD | 4,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.50` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 4,540,000.00 USD | 5,450,000.00 USD | 22,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2382.70` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 15,650,000.00 USD | 14,510,000.00 USD | 11,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2384.80` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 22,770,000.00 USD | 34,830,000.00 USD | 48,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 1,180,000.00 USD | 26,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.20` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 7,590,000.00 USD | 11,630,000.00 USD | 4,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2387.70` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 9,800,000.00 USD | 5,870,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.10` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 5,480,000.00 USD | 41,600,000.00 USD | 41,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.20` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 4,390,000.00 USD | 3,310,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.40` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 6,340,000.00 USD | 50,800,000.00 USD | 39,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.70` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 2,500,000.00 USD | 2,710,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.70` | 1,650,000,000.00 USD | 1,650,000,000.00 USD | 59,730,000.00 USD | 28,250,000.00 USD | 39,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 17,990.00 USD | 26,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2395.20` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 2,360,000.00 USD | 2,790,000.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2397.70` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 118,120.00 USD | 4,290,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2398.00` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 41,690,000.00 USD | 43,490,000.00 USD | 26,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2400.20` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 3,740,000.00 USD | 1,820,000.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.30` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 47,780,000.00 USD | 25,630,000.00 USD | 30,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2402.70` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 3,450,000.00 USD | 2,620,000.00 USD | 825,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.60` | 1,980,000,000.00 USD | 1,980,000,000.00 USD | 55,440,000.00 USD | 32,120,000.00 USD | 26,380,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 190,150.00 USD | 26,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2405.20` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 7,770,000.00 USD | 6,760,000.00 USD | 5,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2407.70` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 10,200,000.00 USD | 5,620,000.00 USD | 3,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2407.90` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 28,480,000.00 USD | 32,330,000.00 USD | 19,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.20` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 5,140,000.00 USD | 4,430,000.00 USD | 4,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.20` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 25,300,000.00 USD | 29,110,000.00 USD | 31,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2412.70` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 7,660,000.00 USD | 3,820,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.50` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 23,240,000.00 USD | 25,170,000.00 USD | 23,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 220,420.00 USD | 26,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.20` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 2,930,000.00 USD | 2,640,000.00 USD | 2,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2417.70` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 3,410,000.00 USD | 1,770,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2417.80` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 33,470,000.00 USD | 11,710,000.00 USD | 24,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2420.20` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 6,550,000.00 USD | 3,030,000.00 USD | 3,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.10` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 29,160,000.00 USD | 25,680,000.00 USD | 13,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.70` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 1,380,000.00 USD | 2,970,000.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.40` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 22,950,000.00 USD | 26,480,000.00 USD | 25,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 69,910.00 USD | 26,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.20` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 510,650.00 USD | 623,850.00 USD | 888,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2427.70` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 2,250,000.00 USD | 1,520,000.00 USD | 609,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.70` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 20,520,000.00 USD | 17,260,000.00 USD | 19,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.20` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 1,370,000.00 USD | 1,550,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.00` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 10,160,000.00 USD | 15,690,000.00 USD | 8,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.70` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 2,770,000.00 USD | 2,230,000.00 USD | 682,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.30` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 20,500,000.00 USD | 11,740,000.00 USD | 12,080,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 1,310,000.00 USD | 28,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.20` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 2,480,000.00 USD | 572,900.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.60` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 12,730,000.00 USD | 16,640,000.00 USD | 6,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2437.70` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 1,360,000.00 USD | 1,040,000.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.20` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 1,240,000.00 USD | 515,920.00 USD | 304,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2440.90` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 16,130,000.00 USD | 8,010,000.00 USD | 10,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2442.70` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 1,030,000.00 USD | 673,960.00 USD | 819,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.20` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 8,460,000.00 USD | 12,330,000.00 USD | 7,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 40,510.00 USD | 28,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.20` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 486,350.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.50` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 11,990,000.00 USD | 5,380,000.00 USD | 14,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2447.70` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 472,100.00 USD | 485,550.00 USD | 687,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.20` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 335,910.00 USD | 56,170.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2450.80` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 12,910,000.00 USD | 12,800,000.00 USD | 13,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2452.70` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 2,730,000.00 USD | 1,820,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2454.10` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 3,980,000.00 USD | 2,980,000.00 USD | 3,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 54,300,000.00 USD | 82,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.20` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 2,270,000.00 USD | 1,660,000.00 USD | 905,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.40` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 9,530,000.00 USD | 8,940,000.00 USD | 8,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2457.70` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 1,290,000.00 USD | 1,810,000.00 USD | 479,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2460.20` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 1,510,000.00 USD | 1,350,000.00 USD | 388,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.70` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 7,770,000.00 USD | 8,630,000.00 USD | 8,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2462.70` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 355,800.00 USD | 542,230.00 USD | 832,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.00` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 8,640,000.00 USD | 7,740,000.00 USD | 6,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 11,530,000.00 USD | 94,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2465.20` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 483,920.00 USD | 876,630.00 USD | 339,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.30` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 3,880,000.00 USD | 3,710,000.00 USD | 586,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2467.70` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 288,920.00 USD | 966,930.00 USD | 377,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.20` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 1,010,000.00 USD | 1,360,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.60` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 4,690,000.00 USD | 2,290,000.00 USD | 522,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2472.70` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 27,630.00 USD | 933,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2473.90` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 4,230,000.00 USD | 2,920,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 249,030.00 USD | 94,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2475.20` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 122,610.00 USD | 914,780.00 USD | 28,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.20` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 2,660,000.00 USD | 4,420,000.00 USD | 872,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2477.70` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 1,080,000.00 USD | 376,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2480.20` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 346,950.00 USD | 943,540.00 USD | 586,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.50` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 2,110,000.00 USD | 5,060,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2480.90` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 0.00 USD | 327,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2483.80` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 63,020.00 USD | 94,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2487.10` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 251,080.00 USD | 211,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.40` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 1,400,000.00 USD | 1,080,000.00 USD | 167,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.70` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 3,000,000.00 USD | 1,540,000.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 2,080,000.00 USD | 96,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.00` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 1,370,000.00 USD | 3,410,000.00 USD | 4,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.30` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 358,770.00 USD | 1,980,000.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.60` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 27,220.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 16,160,000.00 USD | 112,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2506.90` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 2,540,000.00 USD | 1,790,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2510.20` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 148,280.00 USD | 112,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2516.80` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 153,480.00 USD | 189,640.00 USD | 815,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2520.10` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.40` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 77,380.00 USD | 112,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2526.70` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.00` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 2,170,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.30` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 3,800,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 961,350.00 USD | 113,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2536.60` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 4,080,000.00 USD | 3,180,000.00 USD | 3,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2539.90` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 4,150,000.00 USD | 3,040,000.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2543.20` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 3,830,000.00 USD | 2,970,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 12,650.00 USD | 113,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2546.50` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2549.80` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 4,830,000.00 USD | 3,510,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.10` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 2,290,000.00 USD | 835,760.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 197,130.00 USD | 114,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2556.40` | 2,990,000,000.00 USD | 2,990,000,000.00 USD | 3,290,000.00 USD | 255,750.00 USD | 6,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.70` | 3,000,000,000.00 USD | 3,000,000,000.00 USD | 5,720,000.00 USD | 1,660,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2563.00` | 3,000,000,000.00 USD | 3,000,000,000.00 USD | 1,410,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 60,800.00 USD | 114,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2566.30` | 3,010,000,000.00 USD | 3,010,000,000.00 USD | 1,880,000.00 USD | 1,920,000.00 USD | 3,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.60` | 3,010,000,000.00 USD | 3,010,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2572.90` | 3,020,000,000.00 USD | 3,020,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 50,100.00 USD | 114,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2576.20` | 3,020,000,000.00 USD | 3,020,000,000.00 USD | 2,320,000.00 USD | 356,360.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2579.50` | 3,030,000,000.00 USD | 3,030,000,000.00 USD | 2,800,000.00 USD | 2,350,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2582.80` | 3,030,000,000.00 USD | 3,030,000,000.00 USD | 1,760,000.00 USD | 1,280,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,510,000.00 USD | 140,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.10` | 3,040,000,000.00 USD | 3,040,000,000.00 USD | 1,400,000.00 USD | 1,980,000.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2587.00` | 3,040,000,000.00 USD | 3,040,000,000.00 USD | 924,990.00 USD | 344,190.00 USD | 695,470.00 USD | `Tier 1 CEX` |
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
| `7D` | `1972.30` | 960,310,000.00 USD | 0.00 USD | 960,310,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD |
| `7D` | `1975.60` | 960,180,000.00 USD | 0.00 USD | 960,180,000.00 USD | 2,240,000.00 USD | 0.00 USD | 49,530.00 USD |
| `7D` | `1982.20` | 957,890,000.00 USD | 0.00 USD | 957,890,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD |
| `7D` | `1985.50` | 957,680,000.00 USD | 0.00 USD | 957,680,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1988.80` | 955,390,000.00 USD | 0.00 USD | 955,390,000.00 USD | 1,440,000.00 USD | 1,780,000.00 USD | 38,060.00 USD |
| `7D` | `1992.10` | 952,140,000.00 USD | 0.00 USD | 952,140,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD |
| `7D` | `1995.40` | 949,430,000.00 USD | 0.00 USD | 949,430,000.00 USD | 1,340,000.00 USD | 0.00 USD | 808,380.00 USD |
| `1D` | `2002.70` | 676,840,000.00 USD | 0.00 USD | 676,840,000.00 USD | 0.00 USD | 217,070.00 USD | 10,310.00 USD |
| `1D` | `2005.20` | 676,620,000.00 USD | 0.00 USD | 676,620,000.00 USD | 14,690.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2005.30` | 947,280,000.00 USD | 0.00 USD | 947,280,000.00 USD | 0.00 USD | 266,430.00 USD | 0.00 USD |
| `1D` | `2007.70` | 676,600,000.00 USD | 0.00 USD | 676,600,000.00 USD | 0.00 USD | 224,500.00 USD | 0.00 USD |
| `1D` | `2010.20` | 676,380,000.00 USD | 0.00 USD | 676,380,000.00 USD | 0.00 USD | 308,260.00 USD | 0.00 USD |
| `7D` | `2011.90` | 947,010,000.00 USD | 0.00 USD | 947,010,000.00 USD | 170,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2012.70` | 676,070,000.00 USD | 0.00 USD | 676,070,000.00 USD | 299,090.00 USD | 210,450.00 USD | 21,620.00 USD |
| `1D` | `2015.20` | 675,540,000.00 USD | 0.00 USD | 675,540,000.00 USD | 355,800.00 USD | 51,960.00 USD | 3,700.00 USD |
| `1D` | `2017.70` | 675,130,000.00 USD | 0.00 USD | 675,130,000.00 USD | 483,920.00 USD | 1,350,000.00 USD | 553,080.00 USD |
| `1D` | `2020.20` | 672,740,000.00 USD | 0.00 USD | 672,740,000.00 USD | 548,260.00 USD | 1,010,000.00 USD | 403,900.00 USD |
| `1D` | `2022.70` | 670,780,000.00 USD | 0.00 USD | 670,780,000.00 USD | 751,210.00 USD | 178,550.00 USD | 1,490,000.00 USD |
| `7D` | `2025.10` | 946,840,000.00 USD | 0.00 USD | 946,840,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2025.20` | 668,370,000.00 USD | 0.00 USD | 668,370,000.00 USD | 122,610.00 USD | 914,780.00 USD | 28,770.00 USD |
| `1D` | `2027.70` | 667,300,000.00 USD | 0.00 USD | 667,300,000.00 USD | 1,430,000.00 USD | 1,160,000.00 USD | 11,450.00 USD |
| `7D` | `2028.40` | 946,660,000.00 USD | 0.00 USD | 946,660,000.00 USD | 0.00 USD | 0.00 USD | 35,180.00 USD |
| `1D` | `2030.20` | 664,700,000.00 USD | 0.00 USD | 664,700,000.00 USD | 87,180.00 USD | 366,120.00 USD | 957,140.00 USD |
| `7D` | `2031.70` | 946,630,000.00 USD | 0.00 USD | 946,630,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD |
| `1D` | `2032.70` | 663,290,000.00 USD | 0.00 USD | 663,290,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD |
| `7D` | `2035.00` | 942,060,000.00 USD | 0.00 USD | 942,060,000.00 USD | 146,420.00 USD | 186,130.00 USD | 1,350,000.00 USD |
| `1D` | `2035.20` | 659,730,000.00 USD | 0.00 USD | 659,730,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD |
| `1D` | `2037.70` | 658,390,000.00 USD | 0.00 USD | 658,390,000.00 USD | 396,700.00 USD | 458,110.00 USD | 388,420.00 USD |
| `7D` | `2038.30` | 940,370,000.00 USD | 0.00 USD | 940,370,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2040.20` | 657,150,000.00 USD | 0.00 USD | 657,150,000.00 USD | 542,670.00 USD | 178,560.00 USD | 21,940.00 USD |
| `1D` | `2042.70` | 656,400,000.00 USD | 0.00 USD | 656,400,000.00 USD | 626,840.00 USD | 0.00 USD | 174,920.00 USD |
| `7D` | `2044.90` | 938,920,000.00 USD | 0.00 USD | 938,920,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD |
| `1D` | `2045.20` | 655,600,000.00 USD | 0.00 USD | 655,600,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD |
| `1D` | `2047.70` | 655,570,000.00 USD | 0.00 USD | 655,570,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD |
| `1D` | `2050.20` | 654,750,000.00 USD | 0.00 USD | 654,750,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2051.50` | 938,620,000.00 USD | 0.00 USD | 938,620,000.00 USD | 222,640.00 USD | 0.00 USD | 1,190,000.00 USD |
| `7D` | `2054.80` | 937,210,000.00 USD | 0.00 USD | 937,210,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2055.20` | 653,640,000.00 USD | 0.00 USD | 653,640,000.00 USD | 242,080.00 USD | 88,880.00 USD | 28,160.00 USD |
| `7D` | `2058.10` | 936,110,000.00 USD | 0.00 USD | 936,110,000.00 USD | 56,430.00 USD | 189,640.00 USD | 0.00 USD |
| `1D` | `2060.20` | 653,280,000.00 USD | 0.00 USD | 653,280,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2061.40` | 935,870,000.00 USD | 0.00 USD | 935,870,000.00 USD | 1,700,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `1D` | `2062.70` | 652,530,000.00 USD | 0.00 USD | 652,530,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD |
| `7D` | `2064.70` | 930,510,000.00 USD | 0.00 USD | 930,510,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `1D` | `2065.20` | 652,450,000.00 USD | 0.00 USD | 652,450,000.00 USD | 563,140.00 USD | 537,030.00 USD | 510,200.00 USD |
| `1D` | `2067.70` | 650,840,000.00 USD | 0.00 USD | 650,840,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD |
| `7D` | `2068.00` | 928,050,000.00 USD | 0.00 USD | 928,050,000.00 USD | 1,740,000.00 USD | 1,920,000.00 USD | 893,570.00 USD |
| `1D` | `2070.20` | 650,140,000.00 USD | 0.00 USD | 650,140,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD |
| `7D` | `2071.30` | 923,490,000.00 USD | 0.00 USD | 923,490,000.00 USD | 2,780,000.00 USD | 2,310,000.00 USD | 1,230,000.00 USD |
| `1D` | `2072.70` | 649,770,000.00 USD | 0.00 USD | 649,770,000.00 USD | 67,060.00 USD | 555,250.00 USD | 428,640.00 USD |
| `7D` | `2074.60` | 917,170,000.00 USD | 0.00 USD | 917,170,000.00 USD | 4,000,000.00 USD | 3,180,000.00 USD | 3,740,000.00 USD |
| `1D` | `2075.20` | 648,720,000.00 USD | 0.00 USD | 648,720,000.00 USD | 421,860.00 USD | 224,070.00 USD | 91,320.00 USD |
| `1D` | `2077.70` | 647,980,000.00 USD | 0.00 USD | 647,980,000.00 USD | 1,190,000.00 USD | 765,660.00 USD | 422,950.00 USD |
| `7D` | `2077.90` | 906,260,000.00 USD | 0.00 USD | 906,260,000.00 USD | 5,570,000.00 USD | 4,500,000.00 USD | 2,730,000.00 USD |
| `1D` | `2080.20` | 645,600,000.00 USD | 0.00 USD | 645,600,000.00 USD | 586,070.00 USD | 932,020.00 USD | 206,930.00 USD |
| `7D` | `2081.20` | 893,460,000.00 USD | 0.00 USD | 893,460,000.00 USD | 5,010,000.00 USD | 2,990,000.00 USD | 2,500,000.00 USD |
| `1D` | `2082.70` | 643,880,000.00 USD | 0.00 USD | 643,880,000.00 USD | 858,220.00 USD | 305,810.00 USD | 215,500.00 USD |
| `7D` | `2084.50` | 882,970,000.00 USD | 0.00 USD | 882,970,000.00 USD | 2,500,000.00 USD | 1,960,000.00 USD | 4,190,000.00 USD |
| `1D` | `2085.20` | 642,500,000.00 USD | 0.00 USD | 642,500,000.00 USD | 1,380,000.00 USD | 785,030.00 USD | 1,260,000.00 USD |
| `1D` | `2087.70` | 639,070,000.00 USD | 0.00 USD | 639,070,000.00 USD | 1,460,000.00 USD | 573,160.00 USD | 682,400.00 USD |
| `7D` | `2087.80` | 874,320,000.00 USD | 0.00 USD | 874,320,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 2,370,000.00 USD |
| `1D` | `2090.20` | 636,350,000.00 USD | 0.00 USD | 636,350,000.00 USD | 1,030,000.00 USD | 214,870.00 USD | 258,380.00 USD |
| `7D` | `2091.10` | 865,190,000.00 USD | 0.00 USD | 865,190,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD |
| `1D` | `2092.70` | 634,850,000.00 USD | 0.00 USD | 634,850,000.00 USD | 768,770.00 USD | 345,550.00 USD | 588,550.00 USD |
| `7D` | `2094.40` | 852,230,000.00 USD | 0.00 USD | 852,230,000.00 USD | 5,720,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD |
| `1D` | `2095.20` | 633,150,000.00 USD | 0.00 USD | 633,150,000.00 USD | 1,840,000.00 USD | 1,130,000.00 USD | 1,480,000.00 USD |
| `1D` | `2097.70` | 628,690,000.00 USD | 0.00 USD | 628,690,000.00 USD | 175,830.00 USD | 488,160.00 USD | 517,910.00 USD |
| `7D` | `2097.70` | 842,510,000.00 USD | 0.00 USD | 842,510,000.00 USD | 1,850,000.00 USD | 3,860,000.00 USD | 1,290,000.00 USD |
| `1D` | `2100.20` | 627,510,000.00 USD | 0.00 USD | 627,510,000.00 USD | 307,340.00 USD | 928,890.00 USD | 50,560.00 USD |
| `7D` | `2101.00` | 835,520,000.00 USD | 0.00 USD | 835,520,000.00 USD | 1,810,000.00 USD | 1,580,000.00 USD | 4,020,000.00 USD |
| `1D` | `2102.70` | 626,220,000.00 USD | 0.00 USD | 626,220,000.00 USD | 211,840.00 USD | 222,480.00 USD | 483,690.00 USD |
| `7D` | `2104.30` | 828,110,000.00 USD | 0.00 USD | 828,110,000.00 USD | 1,440,000.00 USD | 738,240.00 USD | 2,320,000.00 USD |
| `1D` | `2105.20` | 625,300,000.00 USD | 0.00 USD | 625,300,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 691,960.00 USD |
| `7D` | `2107.60` | 823,610,000.00 USD | 0.00 USD | 823,610,000.00 USD | 8,610,000.00 USD | 1,150,000.00 USD | 1,220,000.00 USD |
| `1D` | `2107.70` | 619,880,000.00 USD | 0.00 USD | 619,880,000.00 USD | 734,860.00 USD | 0.00 USD | 488,260.00 USD |
| `1D` | `2110.20` | 618,660,000.00 USD | 0.00 USD | 618,660,000.00 USD | 61,010.00 USD | 31,550.00 USD | 6,190.00 USD |
| `7D` | `2110.90` | 812,630,000.00 USD | 0.00 USD | 812,630,000.00 USD | 3,480,000.00 USD | 2,360,000.00 USD | 2,720,000.00 USD |
| `1D` | `2112.70` | 618,560,000.00 USD | 0.00 USD | 618,560,000.00 USD | 902,600.00 USD | 506,690.00 USD | 244,160.00 USD |
| `7D` | `2114.20` | 804,070,000.00 USD | 0.00 USD | 804,070,000.00 USD | 1,130,000.00 USD | 2,040,000.00 USD | 3,830,000.00 USD |
| `1D` | `2115.20` | 616,900,000.00 USD | 0.00 USD | 616,900,000.00 USD | 410,020.00 USD | 400,200.00 USD | 939,960.00 USD |
| `7D` | `2117.50` | 797,080,000.00 USD | 0.00 USD | 797,080,000.00 USD | 2,410,000.00 USD | 2,350,000.00 USD | 3,400,000.00 USD |
| `1D` | `2117.70` | 615,150,000.00 USD | 0.00 USD | 615,150,000.00 USD | 4,540,000.00 USD | 3,940,000.00 USD | 302,800.00 USD |
| `1D` | `2120.20` | 606,370,000.00 USD | 0.00 USD | 606,370,000.00 USD | 5,430,000.00 USD | 22,470.00 USD | 671,270.00 USD |
| `7D` | `2120.80` | 788,920,000.00 USD | 0.00 USD | 788,920,000.00 USD | 13,880,000.00 USD | 5,780,000.00 USD | 1,820,000.00 USD |
| `1D` | `2122.70` | 600,240,000.00 USD | 0.00 USD | 600,240,000.00 USD | 3,690,000.00 USD | 3,800,000.00 USD | 1,830,000.00 USD |
| `7D` | `2124.10` | 767,440,000.00 USD | 0.00 USD | 767,440,000.00 USD | 7,990,000.00 USD | 7,760,000.00 USD | 1,660,000.00 USD |
| `1D` | `2125.20` | 590,910,000.00 USD | 0.00 USD | 590,910,000.00 USD | 6,280,000.00 USD | 1,830,000.00 USD | 2,110,000.00 USD |
| `7D` | `2127.40` | 750,020,000.00 USD | 0.00 USD | 750,020,000.00 USD | 2,400,000.00 USD | 4,820,000.00 USD | 5,290,000.00 USD |
| `1D` | `2127.70` | 580,700,000.00 USD | 0.00 USD | 580,700,000.00 USD | 4,430,000.00 USD | 4,180,000.00 USD | 782,350.00 USD |
| `1D` | `2130.20` | 571,310,000.00 USD | 0.00 USD | 571,310,000.00 USD | 1,230,000.00 USD | 172,040.00 USD | 774,790.00 USD |
| `7D` | `2130.70` | 737,510,000.00 USD | 0.00 USD | 737,510,000.00 USD | 5,390,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD |
| `1D` | `2132.70` | 569,130,000.00 USD | 0.00 USD | 569,130,000.00 USD | 0.00 USD | 177,810.00 USD | 1,530,000.00 USD |
| `7D` | `2134.00` | 728,120,000.00 USD | 0.00 USD | 728,120,000.00 USD | 2,550,000.00 USD | 550,450.00 USD | 316,050.00 USD |
| `1D` | `2135.20` | 567,430,000.00 USD | 0.00 USD | 567,430,000.00 USD | 20,600.00 USD | 1,170,000.00 USD | 86,940.00 USD |
| `7D` | `2137.30` | 724,700,000.00 USD | 0.00 USD | 724,700,000.00 USD | 1,040,000.00 USD | 1,510,000.00 USD | 43,560.00 USD |
| `1D` | `2137.70` | 566,150,000.00 USD | 0.00 USD | 566,150,000.00 USD | 21,090.00 USD | 379,920.00 USD | 0.00 USD |
| `1D` | `2140.20` | 565,750,000.00 USD | 0.00 USD | 565,750,000.00 USD | 36,740.00 USD | 265,280.00 USD | 64,360.00 USD |
| `7D` | `2140.60` | 722,110,000.00 USD | 0.00 USD | 722,110,000.00 USD | 2,710,000.00 USD | 1,500,000.00 USD | 801,910.00 USD |
| `1D` | `2142.70` | 565,390,000.00 USD | 0.00 USD | 565,390,000.00 USD | 670,350.00 USD | 2,130,000.00 USD | 0.00 USD |
| `7D` | `2143.90` | 717,100,000.00 USD | 0.00 USD | 717,100,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD |
| `1D` | `2145.20` | 562,580,000.00 USD | 0.00 USD | 562,580,000.00 USD | 121,400.00 USD | 1,720,000.00 USD | 118,750.00 USD |
| `7D` | `2147.20` | 715,250,000.00 USD | 0.00 USD | 715,250,000.00 USD | 1,080,000.00 USD | 949,370.00 USD | 134,420.00 USD |
| `1D` | `2147.70` | 560,620,000.00 USD | 0.00 USD | 560,620,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 69,830.00 USD |
| `1D` | `2150.20` | 557,970,000.00 USD | 0.00 USD | 557,970,000.00 USD | 7,450,000.00 USD | 2,570,000.00 USD | 1,700,000.00 USD |
| `7D` | `2150.50` | 713,080,000.00 USD | 0.00 USD | 713,080,000.00 USD | 459,630.00 USD | 827,410.00 USD | 331,330.00 USD |
| `1D` | `2152.70` | 546,250,000.00 USD | 0.00 USD | 546,250,000.00 USD | 2,710,000.00 USD | 2,400,000.00 USD | 2,100,000.00 USD |
| `7D` | `2153.80` | 711,460,000.00 USD | 0.00 USD | 711,460,000.00 USD | 11,310,000.00 USD | 1,720,000.00 USD | 1,590,000.00 USD |
| `1D` | `2155.20` | 539,040,000.00 USD | 0.00 USD | 539,040,000.00 USD | 2,450,000.00 USD | 3,070,000.00 USD | 1,520,000.00 USD |
| `7D` | `2157.10` | 696,840,000.00 USD | 0.00 USD | 696,840,000.00 USD | 4,350,000.00 USD | 1,640,000.00 USD | 2,720,000.00 USD |
| `1D` | `2157.70` | 532,010,000.00 USD | 0.00 USD | 532,010,000.00 USD | 1,980,000.00 USD | 1,460,000.00 USD | 3,470,000.00 USD |
| `1D` | `2160.20` | 525,100,000.00 USD | 0.00 USD | 525,100,000.00 USD | 3,090,000.00 USD | 5,170,000.00 USD | 1,830,000.00 USD |
| `7D` | `2160.40` | 688,130,000.00 USD | 0.00 USD | 688,130,000.00 USD | 546,010.00 USD | 1,510,000.00 USD | 1,170,000.00 USD |
| `1D` | `2162.70` | 515,010,000.00 USD | 0.00 USD | 515,010,000.00 USD | 14,200,000.00 USD | 10,130,000.00 USD | 1,560,000.00 USD |
| `7D` | `2163.70` | 684,900,000.00 USD | 0.00 USD | 684,900,000.00 USD | 21,060,000.00 USD | 14,080,000.00 USD | 518,640.00 USD |
| `1D` | `2165.20` | 489,120,000.00 USD | 0.00 USD | 489,120,000.00 USD | 9,520,000.00 USD | 9,640,000.00 USD | 4,250,000.00 USD |
| `7D` | `2167.00` | 649,250,000.00 USD | 0.00 USD | 649,250,000.00 USD | 5,300,000.00 USD | 13,000,000.00 USD | 2,970,000.00 USD |
| `1D` | `2167.70` | 465,720,000.00 USD | 0.00 USD | 465,720,000.00 USD | 18,870,000.00 USD | 7,820,000.00 USD | 5,130,000.00 USD |
| `1D` | `2170.20` | 433,890,000.00 USD | 0.00 USD | 433,890,000.00 USD | 23,930,000.00 USD | 9,410,000.00 USD | 7,400,000.00 USD |
| `7D` | `2170.30` | 627,980,000.00 USD | 0.00 USD | 627,980,000.00 USD | 10,280,000.00 USD | 14,770,000.00 USD | 9,520,000.00 USD |
| `1D` | `2172.70` | 393,150,000.00 USD | 0.00 USD | 393,150,000.00 USD | 6,810,000.00 USD | 5,090,000.00 USD | 3,470,000.00 USD |
| `7D` | `2173.60` | 593,400,000.00 USD | 0.00 USD | 593,400,000.00 USD | 34,190,000.00 USD | 828,350.00 USD | 1,500,000.00 USD |
| `1D` | `2175.20` | 377,780,000.00 USD | 0.00 USD | 377,780,000.00 USD | 3,840,000.00 USD | 0.00 USD | 836,880.00 USD |
| `7D` | `2176.90` | 556,880,000.00 USD | 0.00 USD | 556,880,000.00 USD | 1,750,000.00 USD | 1,330,000.00 USD | 2,820,000.00 USD |
| `1D` | `2177.70` | 373,100,000.00 USD | 0.00 USD | 373,100,000.00 USD | 730,100.00 USD | 355,620.00 USD | 2,830,000.00 USD |
| `1D` | `2180.20` | 369,190,000.00 USD | 0.00 USD | 369,190,000.00 USD | 894,580.00 USD | 1,460,000.00 USD | 1,370,000.00 USD |
| `1D` | `2182.70` | 365,460,000.00 USD | 0.00 USD | 365,460,000.00 USD | 73,470.00 USD | 26,540.00 USD | 3,040,000.00 USD |
| `7D` | `2183.50` | 550,980,000.00 USD | 0.00 USD | 550,980,000.00 USD | 1,760,000.00 USD | 1,310,000.00 USD | 3,950,000.00 USD |
| `1D` | `2185.20` | 362,330,000.00 USD | 0.00 USD | 362,330,000.00 USD | 310,640.00 USD | 1,660,000.00 USD | 4,990,000.00 USD |
| `7D` | `2186.80` | 543,980,000.00 USD | 0.00 USD | 543,980,000.00 USD | 37,310,000.00 USD | 17,750,000.00 USD | 0.00 USD |
| `1D` | `2187.70` | 355,370,000.00 USD | 0.00 USD | 355,370,000.00 USD | 3,960,000.00 USD | 1,250,000.00 USD | 3,570,000.00 USD |
| `7D` | `2190.10` | 488,920,000.00 USD | 0.00 USD | 488,920,000.00 USD | 12,430,000.00 USD | 27,500,000.00 USD | 4,580,000.00 USD |
| `1D` | `2190.20` | 346,590,000.00 USD | 0.00 USD | 346,590,000.00 USD | 4,530,000.00 USD | 4,030,000.00 USD | 5,080,000.00 USD |
| `1D` | `2192.70` | 332,960,000.00 USD | 0.00 USD | 332,960,000.00 USD | 4,930,000.00 USD | 4,710,000.00 USD | 1,210,000.00 USD |
| `7D` | `2193.40` | 444,410,000.00 USD | 0.00 USD | 444,410,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,080,000.00 USD |
| `1D` | `2195.20` | 322,100,000.00 USD | 0.00 USD | 322,100,000.00 USD | 5,560,000.00 USD | 1,880,000.00 USD | 4,020,000.00 USD |
| `7D` | `2196.70` | 428,990,000.00 USD | 0.00 USD | 428,990,000.00 USD | 383,690.00 USD | 243,760.00 USD | 2,040,000.00 USD |
| `1D` | `2197.70` | 310,640,000.00 USD | 0.00 USD | 310,640,000.00 USD | 4,440,000.00 USD | 1,140,000.00 USD | 4,210,000.00 USD |
| `7D` | `2200.00` | 426,320,000.00 USD | 0.00 USD | 426,320,000.00 USD | 0.00 USD | 0.00 USD | 5,400,000.00 USD |
| `1D` | `2200.20` | 300,850,000.00 USD | 0.00 USD | 300,850,000.00 USD | 4,980,000.00 USD | 2,340,000.00 USD | 7,760,000.00 USD |
| `1D` | `2202.70` | 285,770,000.00 USD | 0.00 USD | 285,770,000.00 USD | 3,630,000.00 USD | 4,690,000.00 USD | 5,120,000.00 USD |
| `7D` | `2203.30` | 420,920,000.00 USD | 0.00 USD | 420,920,000.00 USD | 4,310,000.00 USD | 0.00 USD | 7,670,000.00 USD |
| `1D` | `2205.20` | 272,330,000.00 USD | 0.00 USD | 272,330,000.00 USD | 1,810,000.00 USD | 574,970.00 USD | 681,760.00 USD |
| `7D` | `2206.60` | 408,950,000.00 USD | 0.00 USD | 408,950,000.00 USD | 1,490,000.00 USD | 588,950.00 USD | 4,640,000.00 USD |
| `1D` | `2207.70` | 269,260,000.00 USD | 0.00 USD | 269,260,000.00 USD | 0.00 USD | 4,250,000.00 USD | 0.00 USD |
| `7D` | `2209.90` | 402,220,000.00 USD | 0.00 USD | 402,220,000.00 USD | 0.00 USD | 0.00 USD | 11,300,000.00 USD |
| `1D` | `2210.20` | 265,010,000.00 USD | 0.00 USD | 265,010,000.00 USD | 104,760.00 USD | 399,720.00 USD | 0.00 USD |
| `1D` | `2212.70` | 264,500,000.00 USD | 0.00 USD | 264,500,000.00 USD | 3,780,000.00 USD | 5,190,000.00 USD | 39,150.00 USD |
| `7D` | `2213.20` | 390,930,000.00 USD | 0.00 USD | 390,930,000.00 USD | 1,710,000.00 USD | 1,060,000.00 USD | 1,960,000.00 USD |
| `1D` | `2215.20` | 255,490,000.00 USD | 0.00 USD | 255,490,000.00 USD | 2,150,000.00 USD | 2,640,000.00 USD | 100,120.00 USD |
| `7D` | `2216.50` | 386,200,000.00 USD | 0.00 USD | 386,200,000.00 USD | 0.00 USD | 487,520.00 USD | 495,340.00 USD |
| `1D` | `2217.70` | 250,600,000.00 USD | 0.00 USD | 250,600,000.00 USD | 2,100,000.00 USD | 1,490,000.00 USD | 92,370.00 USD |
| `7D` | `2219.80` | 385,220,000.00 USD | 0.00 USD | 385,220,000.00 USD | 22,400,000.00 USD | 1,200,000.00 USD | 3,700,000.00 USD |
| `1D` | `2220.20` | 246,920,000.00 USD | 0.00 USD | 246,920,000.00 USD | 6,760,000.00 USD | 865,980.00 USD | 2,970,000.00 USD |
| `1D` | `2222.70` | 236,330,000.00 USD | 0.00 USD | 236,330,000.00 USD | 9,870,000.00 USD | 6,090,000.00 USD | 5,520,000.00 USD |
| `7D` | `2223.10` | 357,920,000.00 USD | 0.00 USD | 357,920,000.00 USD | 9,430,000.00 USD | 13,660,000.00 USD | 25,580,000.00 USD |
| `1D` | `2225.20` | 214,850,000.00 USD | 0.00 USD | 214,850,000.00 USD | 14,150,000.00 USD | 2,980,000.00 USD | 13,020,000.00 USD |
| `7D` | `2226.40` | 309,250,000.00 USD | 0.00 USD | 309,250,000.00 USD | 969,390.00 USD | 12,680,000.00 USD | 14,390,000.00 USD |
| `1D` | `2227.70` | 184,710,000.00 USD | 0.00 USD | 184,710,000.00 USD | 20,040,000.00 USD | 17,080,000.00 USD | 2,120,000.00 USD |
| `7D` | `2229.70` | 281,220,000.00 USD | 0.00 USD | 281,220,000.00 USD | 48,530,000.00 USD | 33,560,000.00 USD | 23,780,000.00 USD |
| `1D` | `2230.20` | 145,470,000.00 USD | 0.00 USD | 145,470,000.00 USD | 29,540,000.00 USD | 1,030,000.00 USD | 7,470,000.00 USD |
| `1D` | `2232.70` | 107,430,000.00 USD | 0.00 USD | 107,430,000.00 USD | 26,430,000.00 USD | 6,600,000.00 USD | 21,170,000.00 USD |
| `7D` | `2233.00` | 175,340,000.00 USD | 0.00 USD | 175,340,000.00 USD | 23,810,000.00 USD | 46,390,000.00 USD | 25,460,000.00 USD |
| `1D` | `2235.20` | 53,230,000.00 USD | 0.00 USD | 53,230,000.00 USD | 22,090,000.00 USD | 0.00 USD | 20,410,000.00 USD |
| `7D` | `2236.30` | 79,680,000.00 USD | 0.00 USD | 79,680,000.00 USD | 30,150,000.00 USD | 23,260,000.00 USD | 26,260,000.00 USD |
| `1D` | `2237.70` | 10,730,000.00 USD | 0.00 USD | 10,730,000.00 USD | 8,000,000.00 USD | 0.00 USD | 2,730,000.00 USD |
| `7D` | `2238.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2238.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2239.60` | 49,490,000.00 USD | 49,490,000.00 USD | 0.00 USD | 41,160,000.00 USD | 0.00 USD | 8,330,000.00 USD |
| `1D` | `2240.20` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 7,220,000.00 USD | 0.00 USD | 4,920,000.00 USD |
| `1D` | `2242.70` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 0.00 USD | 141,810.00 USD | 50,930.00 USD |
| `7D` | `2242.90` | 54,320,000.00 USD | 54,320,000.00 USD | 0.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2245.20` | 14,030,000.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 1,650,000.00 USD | 45,350.00 USD |
| `7D` | `2246.20` | 57,500,000.00 USD | 57,500,000.00 USD | 0.00 USD | 2,040,000.00 USD | 1,030,000.00 USD | 102,060.00 USD |
| `1D` | `2247.70` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,950.00 USD |
| `7D` | `2249.50` | 64,920,000.00 USD | 64,920,000.00 USD | 0.00 USD | 3,510,000.00 USD | 2,660,000.00 USD | 1,250,000.00 USD |
| `1D` | `2250.20` | 20,200,000.00 USD | 20,200,000.00 USD | 0.00 USD | 5,930,000.00 USD | 166,850.00 USD | 55,780.00 USD |
| `1D` | `2252.70` | 32,510,000.00 USD | 32,510,000.00 USD | 0.00 USD | 10,870,000.00 USD | 122,810.00 USD | 1,320,000.00 USD |
| `7D` | `2252.80` | 95,300,000.00 USD | 95,300,000.00 USD | 0.00 USD | 21,510,000.00 USD | 8,880,000.00 USD | 0.00 USD |
| `1D` | `2255.20` | 49,270,000.00 USD | 49,270,000.00 USD | 0.00 USD | 5,590,000.00 USD | 8,490,000.00 USD | 2,690,000.00 USD |
| `7D` | `2256.10` | 119,400,000.00 USD | 119,400,000.00 USD | 0.00 USD | 13,070,000.00 USD | 10,520,000.00 USD | 514,610.00 USD |
| `1D` | `2257.70` | 76,780,000.00 USD | 76,780,000.00 USD | 0.00 USD | 16,850,000.00 USD | 6,780,000.00 USD | 3,880,000.00 USD |
| `7D` | `2259.40` | 142,760,000.00 USD | 142,760,000.00 USD | 0.00 USD | 11,860,000.00 USD | 7,450,000.00 USD | 4,040,000.00 USD |
| `1D` | `2260.20` | 97,650,000.00 USD | 97,650,000.00 USD | 0.00 USD | 9,700,000.00 USD | 9,260,000.00 USD | 1,910,000.00 USD |
| `1D` | `2262.70` | 120,560,000.00 USD | 120,560,000.00 USD | 0.00 USD | 11,070,000.00 USD | 8,850,000.00 USD | 2,990,000.00 USD |
| `7D` | `2262.70` | 151,140,000.00 USD | 151,140,000.00 USD | 0.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 210,470.00 USD |
| `1D` | `2265.20` | 147,460,000.00 USD | 147,460,000.00 USD | 0.00 USD | 7,780,000.00 USD | 8,270,000.00 USD | 10,850,000.00 USD |
| `7D` | `2266.00` | 163,120,000.00 USD | 163,120,000.00 USD | 0.00 USD | 0.00 USD | 5,650,000.00 USD | 6,330,000.00 USD |
| `1D` | `2267.70` | 169,160,000.00 USD | 169,160,000.00 USD | 0.00 USD | 9,840,000.00 USD | 6,210,000.00 USD | 5,650,000.00 USD |
| `7D` | `2269.30` | 176,400,000.00 USD | 176,400,000.00 USD | 0.00 USD | 8,610,000.00 USD | 0.00 USD | 4,660,000.00 USD |
| `1D` | `2270.20` | 194,590,000.00 USD | 194,590,000.00 USD | 0.00 USD | 7,970,000.00 USD | 3,900,000.00 USD | 13,570,000.00 USD |
| `7D` | `2272.60` | 189,450,000.00 USD | 189,450,000.00 USD | 0.00 USD | 7,540,000.00 USD | 1,480,000.00 USD | 4,030,000.00 USD |
| `1D` | `2272.70` | 200,610,000.00 USD | 200,610,000.00 USD | 0.00 USD | 3,630,000.00 USD | 1,290,000.00 USD | 1,110,000.00 USD |
| `1D` | `2275.20` | 229,610,000.00 USD | 229,610,000.00 USD | 0.00 USD | 12,590,000.00 USD | 15,020,000.00 USD | 1,390,000.00 USD |
| `7D` | `2275.90` | 194,950,000.00 USD | 194,950,000.00 USD | 0.00 USD | 0.00 USD | 5,500,000.00 USD | 0.00 USD |
| `1D` | `2277.70` | 252,930,000.00 USD | 252,930,000.00 USD | 0.00 USD | 3,520,000.00 USD | 10,200,000.00 USD | 9,590,000.00 USD |
| `7D` | `2279.20` | 230,490,000.00 USD | 230,490,000.00 USD | 0.00 USD | 854,200.00 USD | 24,150,000.00 USD | 10,540,000.00 USD |
| `1D` | `2280.20` | 297,840,000.00 USD | 297,840,000.00 USD | 0.00 USD | 27,000,000.00 USD | 10,110,000.00 USD | 7,800,000.00 USD |
| `7D` | `2282.50` | 326,340,000.00 USD | 326,340,000.00 USD | 0.00 USD | 0.00 USD | 82,170,000.00 USD | 13,670,000.00 USD |
| `1D` | `2282.70` | 363,520,000.00 USD | 363,520,000.00 USD | 0.00 USD | 28,520,000.00 USD | 26,750,000.00 USD | 10,420,000.00 USD |
| `1D` | `2285.20` | 384,430,000.00 USD | 384,430,000.00 USD | 0.00 USD | 9,620,000.00 USD | 8,450,000.00 USD | 2,830,000.00 USD |
| `7D` | `2285.80` | 350,110,000.00 USD | 350,110,000.00 USD | 0.00 USD | 6,610,000.00 USD | 17,060,000.00 USD | 105,230.00 USD |
| `1D` | `2287.70` | 414,060,000.00 USD | 414,060,000.00 USD | 0.00 USD | 12,690,000.00 USD | 8,930,000.00 USD | 8,010,000.00 USD |
| `7D` | `2289.10` | 382,120,000.00 USD | 382,120,000.00 USD | 0.00 USD | 8,380,000.00 USD | 8,650,000.00 USD | 14,980,000.00 USD |
| `1D` | `2290.20` | 444,690,000.00 USD | 444,690,000.00 USD | 0.00 USD | 14,400,000.00 USD | 13,200,000.00 USD | 3,040,000.00 USD |
| `7D` | `2292.40` | 395,380,000.00 USD | 395,380,000.00 USD | 0.00 USD | 7,890,000.00 USD | 0.00 USD | 5,370,000.00 USD |
| `1D` | `2292.70` | 470,720,000.00 USD | 470,720,000.00 USD | 0.00 USD | 13,200,000.00 USD | 3,480,000.00 USD | 9,350,000.00 USD |
| `1D` | `2295.20` | 497,460,000.00 USD | 497,460,000.00 USD | 0.00 USD | 6,720,000.00 USD | 11,490,000.00 USD | 8,540,000.00 USD |
| `7D` | `2295.70` | 436,900,000.00 USD | 436,900,000.00 USD | 0.00 USD | 23,390,000.00 USD | 6,820,000.00 USD | 11,320,000.00 USD |
| `1D` | `2297.70` | 537,150,000.00 USD | 537,150,000.00 USD | 0.00 USD | 22,140,000.00 USD | 12,350,000.00 USD | 5,200,000.00 USD |
| `7D` | `2299.00` | 463,950,000.00 USD | 463,950,000.00 USD | 0.00 USD | 4,220,000.00 USD | 17,180,000.00 USD | 5,650,000.00 USD |
| `1D` | `2300.20` | 573,300,000.00 USD | 573,300,000.00 USD | 0.00 USD | 9,490,000.00 USD | 13,100,000.00 USD | 13,560,000.00 USD |
| `7D` | `2302.30` | 540,590,000.00 USD | 540,590,000.00 USD | 0.00 USD | 37,120,000.00 USD | 17,380,000.00 USD | 22,140,000.00 USD |
| `1D` | `2302.70` | 601,900,000.00 USD | 601,900,000.00 USD | 0.00 USD | 18,950,000.00 USD | 2,400,000.00 USD | 7,240,000.00 USD |
| `1D` | `2305.20` | 640,960,000.00 USD | 640,960,000.00 USD | 0.00 USD | 14,750,000.00 USD | 18,210,000.00 USD | 6,110,000.00 USD |
| `7D` | `2305.60` | 566,610,000.00 USD | 566,610,000.00 USD | 0.00 USD | 6,340,000.00 USD | 8,820,000.00 USD | 10,860,000.00 USD |
| `1D` | `2307.70` | 652,460,000.00 USD | 652,460,000.00 USD | 0.00 USD | 4,370,000.00 USD | 3,930,000.00 USD | 3,210,000.00 USD |
| `7D` | `2308.90` | 569,930,000.00 USD | 569,930,000.00 USD | 0.00 USD | 1,920,000.00 USD | 930,630.00 USD | 472,960.00 USD |
| `1D` | `2310.20` | 671,730,000.00 USD | 671,730,000.00 USD | 0.00 USD | 5,900,000.00 USD | 2,720,000.00 USD | 10,660,000.00 USD |
| `7D` | `2312.20` | 599,240,000.00 USD | 599,240,000.00 USD | 0.00 USD | 10,780,000.00 USD | 2,650,000.00 USD | 15,880,000.00 USD |
| `1D` | `2312.70` | 683,930,000.00 USD | 683,930,000.00 USD | 0.00 USD | 4,670,000.00 USD | 7,190,000.00 USD | 338,820.00 USD |
| `1D` | `2315.20` | 705,230,000.00 USD | 705,230,000.00 USD | 0.00 USD | 4,180,000.00 USD | 11,100,000.00 USD | 6,020,000.00 USD |
| `7D` | `2315.50` | 607,990,000.00 USD | 607,990,000.00 USD | 0.00 USD | 0.00 USD | 8,120,000.00 USD | 627,210.00 USD |
| `1D` | `2317.70` | 724,440,000.00 USD | 724,440,000.00 USD | 0.00 USD | 6,110,000.00 USD | 10,220,000.00 USD | 2,880,000.00 USD |
| `7D` | `2318.80` | 625,500,000.00 USD | 625,500,000.00 USD | 0.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 8,420,000.00 USD |
| `1D` | `2320.20` | 748,200,000.00 USD | 748,200,000.00 USD | 0.00 USD | 9,790,000.00 USD | 11,280,000.00 USD | 2,690,000.00 USD |
| `7D` | `2322.10` | 642,660,000.00 USD | 642,660,000.00 USD | 0.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 108,040.00 USD |
| `1D` | `2322.70` | 762,000,000.00 USD | 762,000,000.00 USD | 0.00 USD | 1,730,000.00 USD | 8,480,000.00 USD | 3,590,000.00 USD |
| `1D` | `2325.20` | 774,420,000.00 USD | 774,420,000.00 USD | 0.00 USD | 1,950,000.00 USD | 8,990,000.00 USD | 1,490,000.00 USD |
| `7D` | `2325.40` | 663,730,000.00 USD | 663,730,000.00 USD | 0.00 USD | 10,150,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD |
| `1D` | `2327.70` | 780,450,000.00 USD | 780,450,000.00 USD | 0.00 USD | 494,310.00 USD | 1,140,000.00 USD | 4,390,000.00 USD |
| `7D` | `2328.70` | 675,970,000.00 USD | 675,970,000.00 USD | 0.00 USD | 3,860,000.00 USD | 363,770.00 USD | 8,020,000.00 USD |
| `1D` | `2330.20` | 796,480,000.00 USD | 796,480,000.00 USD | 0.00 USD | 12,730,000.00 USD | 2,830,000.00 USD | 479,030.00 USD |
| `7D` | `2332.00` | 705,210,000.00 USD | 705,210,000.00 USD | 0.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2332.70` | 822,160,000.00 USD | 822,160,000.00 USD | 0.00 USD | 14,210,000.00 USD | 1,980,000.00 USD | 9,490,000.00 USD |
| `1D` | `2335.20` | 842,720,000.00 USD | 842,720,000.00 USD | 0.00 USD | 14,300,000.00 USD | 4,300,000.00 USD | 1,960,000.00 USD |
| `7D` | `2335.30` | 763,710,000.00 USD | 763,710,000.00 USD | 0.00 USD | 26,630,000.00 USD | 19,830,000.00 USD | 12,040,000.00 USD |
| `1D` | `2337.70` | 855,540,000.00 USD | 855,540,000.00 USD | 0.00 USD | 6,870,000.00 USD | 999,990.00 USD | 4,950,000.00 USD |
| `7D` | `2338.60` | 790,210,000.00 USD | 790,210,000.00 USD | 0.00 USD | 15,880,000.00 USD | 0.00 USD | 10,620,000.00 USD |
| `1D` | `2340.20` | 880,800,000.00 USD | 880,800,000.00 USD | 0.00 USD | 8,850,000.00 USD | 5,380,000.00 USD | 11,020,000.00 USD |
| `7D` | `2341.90` | 826,740,000.00 USD | 826,740,000.00 USD | 0.00 USD | 4,720,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD |
| `1D` | `2342.70` | 895,080,000.00 USD | 895,080,000.00 USD | 0.00 USD | 5,180,000.00 USD | 6,350,000.00 USD | 2,750,000.00 USD |
| `1D` | `2345.20` | 914,460,000.00 USD | 914,460,000.00 USD | 0.00 USD | 4,550,000.00 USD | 6,130,000.00 USD | 8,700,000.00 USD |
| `7D` | `2345.20` | 857,900,000.00 USD | 857,900,000.00 USD | 0.00 USD | 1,350,000.00 USD | 21,160,000.00 USD | 8,640,000.00 USD |
| `1D` | `2347.70` | 924,030,000.00 USD | 924,030,000.00 USD | 0.00 USD | 3,700,000.00 USD | 3,280,000.00 USD | 2,590,000.00 USD |
| `7D` | `2348.50` | 895,770,000.00 USD | 895,770,000.00 USD | 0.00 USD | 847,620.00 USD | 9,500,000.00 USD | 27,530,000.00 USD |
| `1D` | `2350.20` | 970,560,000.00 USD | 970,560,000.00 USD | 0.00 USD | 28,240,000.00 USD | 7,790,000.00 USD | 10,500,000.00 USD |
| `7D` | `2351.80` | 928,640,000.00 USD | 928,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 19,600,000.00 USD | 10,630,000.00 USD |
| `1D` | `2352.70` | 979,880,000.00 USD | 979,880,000.00 USD | 0.00 USD | 4,190,000.00 USD | 2,860,000.00 USD | 2,270,000.00 USD |
| `7D` | `2355.10` | 989,170,000.00 USD | 989,170,000.00 USD | 0.00 USD | 18,880,000.00 USD | 40,150,000.00 USD | 1,500,000.00 USD |
| `1D` | `2355.20` | 992,110,000.00 USD | 992,110,000.00 USD | 0.00 USD | 2,930,000.00 USD | 7,680,000.00 USD | 1,620,000.00 USD |
| `1D` | `2357.70` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 4,070,000.00 USD | 4,660,000.00 USD | 3,480,000.00 USD |
| `7D` | `2358.40` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 7,400,000.00 USD | 1,840,000.00 USD | 6,010,000.00 USD |
| `1D` | `2360.20` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 10,050,000.00 USD | 3,880,000.00 USD | 5,480,000.00 USD |
| `7D` | `2361.70` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,430,000.00 USD | 431,800.00 USD |
| `1D` | `2362.70` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 7,480,000.00 USD | 6,710,000.00 USD | 7,950,000.00 USD |
| `7D` | `2365.00` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 10,200,000.00 USD | 373,740.00 USD | 10,860,000.00 USD |
| `1D` | `2365.20` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 4,830,000.00 USD | 3,140,000.00 USD | 3,680,000.00 USD |
| `1D` | `2367.70` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 3,130,000.00 USD | 1,110,000.00 USD | 1,920,000.00 USD |
| `7D` | `2368.30` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 424,830.00 USD |
| `1D` | `2370.20` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 12,570,000.00 USD | 8,560,000.00 USD | 6,540,000.00 USD |
| `7D` | `2371.60` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 26,000,000.00 USD | 0.00 USD | 54,970,000.00 USD |
| `1D` | `2372.70` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 14,240,000.00 USD | 2,610,000.00 USD | 6,290,000.00 USD |
| `7D` | `2374.90` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD |
| `1D` | `2375.20` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 10,840,000.00 USD | 757,510.00 USD | 2,320,000.00 USD |
| `1D` | `2377.70` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 1,460,000.00 USD | 3,270,000.00 USD | 4,330,000.00 USD |
| `7D` | `2378.20` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 11,180,000.00 USD | 7,790,000.00 USD | 25,670,000.00 USD |
| `1D` | `2380.20` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 6,310,000.00 USD | 389,290.00 USD | 4,780,000.00 USD |
| `7D` | `2381.50` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 5,450,000.00 USD | 22,290,000.00 USD |
| `1D` | `2382.70` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 15,650,000.00 USD | 14,510,000.00 USD | 11,740,000.00 USD |
| `7D` | `2384.80` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 22,770,000.00 USD | 34,830,000.00 USD | 48,450,000.00 USD |
| `1D` | `2385.20` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 7,590,000.00 USD | 11,630,000.00 USD | 4,560,000.00 USD |
| `1D` | `2387.70` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 9,800,000.00 USD | 5,870,000.00 USD | 3,120,000.00 USD |
| `7D` | `2388.10` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 5,480,000.00 USD | 41,600,000.00 USD | 41,180,000.00 USD |
| `1D` | `2390.20` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 4,390,000.00 USD | 3,310,000.00 USD | 1,520,000.00 USD |
| `7D` | `2391.40` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 0.00 USD | 6,340,000.00 USD | 50,800,000.00 USD | 39,790,000.00 USD |
| `1D` | `2392.70` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 2,500,000.00 USD | 2,710,000.00 USD | 3,320,000.00 USD |
| `7D` | `2394.70` | 1,650,000,000.00 USD | 1,650,000,000.00 USD | 0.00 USD | 59,730,000.00 USD | 28,250,000.00 USD | 39,900,000.00 USD |
| `1D` | `2395.20` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 2,360,000.00 USD | 2,790,000.00 USD | 2,220,000.00 USD |
| `1D` | `2397.70` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 118,120.00 USD | 4,290,000.00 USD | 3,380,000.00 USD |
| `7D` | `2398.00` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 0.00 USD | 41,690,000.00 USD | 43,490,000.00 USD | 26,250,000.00 USD |
| `1D` | `2400.20` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 3,740,000.00 USD | 1,820,000.00 USD | 2,600,000.00 USD |
| `7D` | `2401.30` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 0.00 USD | 47,780,000.00 USD | 25,630,000.00 USD | 30,910,000.00 USD |
| `1D` | `2402.70` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 3,450,000.00 USD | 2,620,000.00 USD | 825,510.00 USD |
| `7D` | `2404.60` | 1,980,000,000.00 USD | 1,980,000,000.00 USD | 0.00 USD | 55,440,000.00 USD | 32,120,000.00 USD | 26,380,000.00 USD |
| `1D` | `2405.20` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 0.00 USD | 7,770,000.00 USD | 6,760,000.00 USD | 5,320,000.00 USD |
| `1D` | `2407.70` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 10,200,000.00 USD | 5,620,000.00 USD | 3,210,000.00 USD |
| `7D` | `2407.90` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 0.00 USD | 28,480,000.00 USD | 32,330,000.00 USD | 19,910,000.00 USD |
| `1D` | `2410.20` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 5,140,000.00 USD | 4,430,000.00 USD | 4,630,000.00 USD |
| `7D` | `2411.20` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 25,300,000.00 USD | 29,110,000.00 USD | 31,630,000.00 USD |
| `1D` | `2412.70` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 7,660,000.00 USD | 3,820,000.00 USD | 2,420,000.00 USD |
| `7D` | `2414.50` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 23,240,000.00 USD | 25,170,000.00 USD | 23,620,000.00 USD |
| `1D` | `2415.20` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 2,930,000.00 USD | 2,640,000.00 USD | 2,980,000.00 USD |
| `1D` | `2417.70` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 3,410,000.00 USD | 1,770,000.00 USD | 1,770,000.00 USD |
| `7D` | `2417.80` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 33,470,000.00 USD | 11,710,000.00 USD | 24,570,000.00 USD |
| `1D` | `2420.20` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 6,550,000.00 USD | 3,030,000.00 USD | 3,680,000.00 USD |
| `7D` | `2421.10` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 29,160,000.00 USD | 25,680,000.00 USD | 13,470,000.00 USD |
| `1D` | `2422.70` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 1,380,000.00 USD | 2,970,000.00 USD | 3,790,000.00 USD |
| `7D` | `2424.40` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 0.00 USD | 22,950,000.00 USD | 26,480,000.00 USD | 25,470,000.00 USD |
| `1D` | `2425.20` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 510,650.00 USD | 623,850.00 USD | 888,640.00 USD |
| `1D` | `2427.70` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 2,250,000.00 USD | 1,520,000.00 USD | 609,950.00 USD |
| `7D` | `2427.70` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 0.00 USD | 20,520,000.00 USD | 17,260,000.00 USD | 19,450,000.00 USD |
| `1D` | `2430.20` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,550,000.00 USD | 1,350,000.00 USD |
| `7D` | `2431.00` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 0.00 USD | 10,160,000.00 USD | 15,690,000.00 USD | 8,420,000.00 USD |
| `1D` | `2432.70` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 2,770,000.00 USD | 2,230,000.00 USD | 682,860.00 USD |
| `7D` | `2434.30` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 0.00 USD | 20,500,000.00 USD | 11,740,000.00 USD | 12,080,000.00 USD |
| `1D` | `2435.20` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 2,480,000.00 USD | 572,900.00 USD | 1,370,000.00 USD |
| `7D` | `2437.60` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 12,730,000.00 USD | 16,640,000.00 USD | 6,270,000.00 USD |
| `1D` | `2437.70` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 1,360,000.00 USD | 1,040,000.00 USD | 30,250.00 USD |
| `1D` | `2440.20` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 1,240,000.00 USD | 515,920.00 USD | 304,820.00 USD |
| `7D` | `2440.90` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 16,130,000.00 USD | 8,010,000.00 USD | 10,540,000.00 USD |
| `1D` | `2442.70` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 1,030,000.00 USD | 673,960.00 USD | 819,120.00 USD |
| `7D` | `2444.20` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 8,460,000.00 USD | 12,330,000.00 USD | 7,710,000.00 USD |
| `1D` | `2445.20` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 0.00 USD | 486,350.00 USD | 1,140,000.00 USD |
| `7D` | `2447.50` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 11,990,000.00 USD | 5,380,000.00 USD | 14,540,000.00 USD |
| `1D` | `2447.70` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 472,100.00 USD | 485,550.00 USD | 687,270.00 USD |
| `1D` | `2450.20` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 335,910.00 USD | 56,170.00 USD | 26,770.00 USD |
| `7D` | `2450.80` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 12,910,000.00 USD | 12,800,000.00 USD | 13,220,000.00 USD |
| `1D` | `2452.70` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 2,730,000.00 USD | 1,820,000.00 USD | 2,240,000.00 USD |
| `7D` | `2454.10` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 0.00 USD | 3,980,000.00 USD | 2,980,000.00 USD | 3,870,000.00 USD |
| `1D` | `2455.20` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 2,270,000.00 USD | 1,660,000.00 USD | 905,110.00 USD |
| `7D` | `2457.40` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 9,530,000.00 USD | 8,940,000.00 USD | 8,640,000.00 USD |
| `1D` | `2457.70` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 1,290,000.00 USD | 1,810,000.00 USD | 479,530.00 USD |
| `1D` | `2460.20` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,350,000.00 USD | 388,420.00 USD |
| `7D` | `2460.70` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 7,770,000.00 USD | 8,630,000.00 USD | 8,640,000.00 USD |
| `1D` | `2462.70` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 355,800.00 USD | 542,230.00 USD | 832,760.00 USD |
| `7D` | `2464.00` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 8,640,000.00 USD | 7,740,000.00 USD | 6,900,000.00 USD |
| `1D` | `2465.20` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 483,920.00 USD | 876,630.00 USD | 339,180.00 USD |
| `7D` | `2467.30` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 3,880,000.00 USD | 3,710,000.00 USD | 586,780.00 USD |
| `1D` | `2467.70` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 288,920.00 USD | 966,930.00 USD | 377,900.00 USD |
| `1D` | `2470.20` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 1,010,000.00 USD | 1,360,000.00 USD | 1,190,000.00 USD |
| `7D` | `2470.60` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 4,690,000.00 USD | 2,290,000.00 USD | 522,210.00 USD |
| `1D` | `2472.70` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 0.00 USD | 27,630.00 USD | 933,760.00 USD |
| `7D` | `2473.90` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 4,230,000.00 USD | 2,920,000.00 USD | 2,240,000.00 USD |
| `1D` | `2475.20` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 122,610.00 USD | 914,780.00 USD | 28,770.00 USD |
| `7D` | `2477.20` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 0.00 USD | 2,660,000.00 USD | 4,420,000.00 USD | 872,130.00 USD |
| `1D` | `2477.70` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 1,080,000.00 USD | 376,610.00 USD | 0.00 USD |
| `1D` | `2480.20` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 346,950.00 USD | 943,540.00 USD | 586,640.00 USD |
| `7D` | `2480.50` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 0.00 USD | 2,110,000.00 USD | 5,060,000.00 USD | 1,590,000.00 USD |
| `1D` | `2480.90` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 327,340.00 USD |
| `7D` | `2483.80` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 1,430,000.00 USD |
| `7D` | `2487.10` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 251,080.00 USD | 211,130.00 USD | 0.00 USD |
| `7D` | `2490.40` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 1,400,000.00 USD | 1,080,000.00 USD | 167,620.00 USD |
| `7D` | `2493.70` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 1,540,000.00 USD | 1,840,000.00 USD |
| `7D` | `2497.00` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 1,370,000.00 USD | 3,410,000.00 USD | 4,400,000.00 USD |
| `7D` | `2500.30` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 358,770.00 USD | 1,980,000.00 USD | 1,060,000.00 USD |
| `7D` | `2503.60` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 0.00 USD | 27,220.00 USD | 125,600.00 USD |
| `7D` | `2506.90` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 2,540,000.00 USD | 1,790,000.00 USD | 1,990,000.00 USD |
| `7D` | `2510.20` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 1,190,000.00 USD |
| `7D` | `2516.80` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 153,480.00 USD | 189,640.00 USD | 815,620.00 USD |
| `7D` | `2520.10` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `7D` | `2523.40` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `7D` | `2526.70` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD |
| `7D` | `2530.00` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 2,170,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `7D` | `2533.30` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 0.00 USD | 3,800,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD |
| `7D` | `2536.60` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 4,080,000.00 USD | 3,180,000.00 USD | 3,530,000.00 USD |
| `7D` | `2539.90` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 3,040,000.00 USD | 1,560,000.00 USD |
| `7D` | `2543.20` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 0.00 USD | 3,830,000.00 USD | 2,970,000.00 USD | 2,480,000.00 USD |
| `7D` | `2546.50` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 2,300,000.00 USD |
| `7D` | `2549.80` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 0.00 USD | 4,830,000.00 USD | 3,510,000.00 USD | 3,710,000.00 USD |
| `7D` | `2553.10` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 0.00 USD | 2,290,000.00 USD | 835,760.00 USD | 1,680,000.00 USD |
| `7D` | `2556.40` | 2,990,000,000.00 USD | 2,990,000,000.00 USD | 0.00 USD | 3,290,000.00 USD | 255,750.00 USD | 6,520,000.00 USD |
| `7D` | `2559.70` | 3,000,000,000.00 USD | 3,000,000,000.00 USD | 0.00 USD | 5,720,000.00 USD | 1,660,000.00 USD | 2,300,000.00 USD |
| `7D` | `2563.00` | 3,000,000,000.00 USD | 3,000,000,000.00 USD | 0.00 USD | 1,410,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD |
| `7D` | `2566.30` | 3,010,000,000.00 USD | 3,010,000,000.00 USD | 0.00 USD | 1,880,000.00 USD | 1,920,000.00 USD | 3,000,000.00 USD |
| `7D` | `2569.60` | 3,010,000,000.00 USD | 3,010,000,000.00 USD | 0.00 USD | 125,250.00 USD | 341,900.00 USD | 1,480,000.00 USD |
| `7D` | `2572.90` | 3,020,000,000.00 USD | 3,020,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,800,000.00 USD |
| `7D` | `2576.20` | 3,020,000,000.00 USD | 3,020,000,000.00 USD | 0.00 USD | 2,320,000.00 USD | 356,360.00 USD | 1,640,000.00 USD |
| `7D` | `2579.50` | 3,030,000,000.00 USD | 3,030,000,000.00 USD | 0.00 USD | 2,800,000.00 USD | 2,350,000.00 USD | 1,950,000.00 USD |
| `7D` | `2582.80` | 3,030,000,000.00 USD | 3,030,000,000.00 USD | 0.00 USD | 1,760,000.00 USD | 1,280,000.00 USD | 2,950,000.00 USD |
| `7D` | `2586.10` | 3,040,000,000.00 USD | 3,040,000,000.00 USD | 0.00 USD | 1,400,000.00 USD | 1,980,000.00 USD | 1,850,000.00 USD |
| `7D` | `2587.00` | 3,040,000,000.00 USD | 3,040,000,000.00 USD | 0.00 USD | 924,990.00 USD | 344,190.00 USD | 695,470.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `28.97B` | Total OI Tokens: `12,932,382.8 ETH`
  * 1h OI Change: `-0.53%` | 4h OI Change: `+0.82%` | 24h OI Change: `-3.13%`
  * Exchange Breakdown: Binance=`8.45B` | Bybit=`2.10B` | OKX=`1.79B` | Hyperliquid=`2.35B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-75.37K` | Last 24h: `1.05M` | Last 3d: `6.29M` | Last 7d: `12.86M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0027%` | **USDT OKX** | `-0.0078%` |
| **USDT Bybit** | `-0.0145%` | **USDT KuCoin** | `-0.0098%` |
| **USDT MEXC** | `0.0026%` | **USDT BingX** | `0.0028%` |
| **USDT Gate** | `-0.0113%` | **USDT Bitget** | `0.0010%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0078%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `35.64%` | `64.36%` | `0.55` | 508,510,000.00 USD |
| `15M` | `Binance` | `31.13%` | `68.87%` | `0.45` | 205,360,000.00 USD |
| `15M` | `OKX` | `37.24%` | `62.76%` | `0.59` | 63,460,000.00 USD |
| `15M` | `Bybit` | `35.08%` | `64.92%` | `0.54` | 36,210,000.00 USD |
| `15M` | `KuCoin` | `21.72%` | `78.28%` | `0.28` | 2,150,000.00 USD |
| `15M` | `Gate` | `39.3%` | `60.7%` | `0.65` | 48,570,000.00 USD |
| `15M` | `Bitget` | `42.54%` | `57.46%` | `0.74` | 27,060,000.00 USD |
| `15M` | `BingX` | `27.5%` | `72.5%` | `0.38` | 8,980,000.00 USD |
| `15M` | `MEXC` | `39.18%` | `60.82%` | `0.64` | 15,370,000.00 USD |
| `15M` | `Bitunix` | `25.54%` | `74.46%` | `0.34` | 25,990,000.00 USD |
| `15M` | `Hyperliquid` | `32.07%` | `67.93%` | `0.47` | 23,680,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `28.81%` | `71.19%` | `0.40` | 3,130,000.00 USD |
| `15M` | `Crypto.com` | `53.48%` | `46.52%` | `1.15` | 1,360,000.00 USD |
| `15M` | `WhiteBIT` | `99.42%` | `0.58%` | `171.41` | 6,820,000.00 USD |
| `15M` | `HTX` | `39.32%` | `60.68%` | `0.65` | 2,800,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `44.39%` | `55.61%` | `0.80` | 26,520,000.00 USD |
| `15M` | `Bitfinex` | `64.34%` | `35.66%` | `1.80` | 144,820.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `54.72%` | `45.28%` | `1.21` | 4,460,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `52.21%` | `47.79%` | `1.09` | 6,470,000.00 USD |
| `15M` | `Whale Positions` | `31.13%` | `68.87%` | `0.45` | 205,360,000.00 USD |
| `15M` | `Global Accounts` | `35.64%` | `64.36%` | `0.55` | 508,510,000.00 USD |
| `1H` | `ETH` | `51.94%` | `48.06%` | `1.08` | 2,600,000,000.00 USD |
| `1H` | `Binance` | `47.4%` | `52.6%` | `0.90` | 858,170,000.00 USD |
| `1H` | `OKX` | `51.51%` | `48.49%` | `1.06` | 392,700,000.00 USD |
| `1H` | `Bybit` | `57.43%` | `42.57%` | `1.35` | 239,240,000.00 USD |
| `1H` | `KuCoin` | `59.84%` | `40.16%` | `1.49` | 8,060,000.00 USD |
| `1H` | `Gate` | `49.69%` | `50.31%` | `0.99` | 283,740,000.00 USD |
| `1H` | `Bitget` | `52.09%` | `47.91%` | `1.09` | 153,260,000.00 USD |
| `1H` | `BingX` | `42.47%` | `57.53%` | `0.74` | 38,350,000.00 USD |
| `1H` | `MEXC` | `45.85%` | `54.15%` | `0.85` | 110,530,000.00 USD |
| `1H` | `Bitunix` | `48.49%` | `51.51%` | `0.94` | 105,680,000.00 USD |
| `1H` | `Hyperliquid` | `58.99%` | `41.01%` | `1.44` | 141,860,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `43.59%` | `56.41%` | `0.77` | 13,650,000.00 USD |
| `1H` | `Crypto.com` | `50%` | `50%` | `1.00` | 6,020,000.00 USD |
| `1H` | `WhiteBIT` | `90.59%` | `9.41%` | `9.63` | 95,380,000.00 USD |
| `1H` | `HTX` | `50.54%` | `49.46%` | `1.02` | 8,030,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `49.48%` | `50.52%` | `0.98` | 93,820,000.00 USD |
| `1H` | `Bitfinex` | `52.05%` | `47.95%` | `1.09` | 1,800,000.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `64.56%` | `35.44%` | `1.82` | 28,250,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.67%` | `47.33%` | `1.11` | 29,390,000.00 USD |
| `1H` | `Whale Positions` | `47.4%` | `52.6%` | `0.90` | 858,170,000.00 USD |
| `1H` | `Global Accounts` | `51.94%` | `48.06%` | `1.08` | 2,600,000,000.00 USD |
| `4H` | `ETH` | `49.27%` | `50.73%` | `0.97` | 8,970,000,000.00 USD |
| `4H` | `Binance` | `51.07%` | `48.93%` | `1.04` | 2,570,000,000.00 USD |
| `4H` | `OKX` | `50.73%` | `49.27%` | `1.03` | 1,470,000,000.00 USD |
| `4H` | `Bybit` | `52.38%` | `47.62%` | `1.10` | 569,820,000.00 USD |
| `4H` | `KuCoin` | `57.46%` | `42.54%` | `1.35` | 62,340,000.00 USD |
| `4H` | `Gate` | `50.33%` | `49.67%` | `1.01` | 1,220,000,000.00 USD |
| `4H` | `Bitget` | `51.73%` | `48.27%` | `1.07` | 383,040,000.00 USD |
| `4H` | `BingX` | `52.19%` | `47.81%` | `1.09` | 72,670,000.00 USD |
| `4H` | `MEXC` | `49.81%` | `50.19%` | `0.99` | 216,670,000.00 USD |
| `4H` | `Bitunix` | `51.43%` | `48.57%` | `1.06` | 287,700,000.00 USD |
| `4H` | `Hyperliquid` | `53.59%` | `46.41%` | `1.15` | 223,840,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `57.28%` | `42.72%` | `1.34` | 42,390,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `36.45%` | `63.55%` | `0.57` | 1,460,000,000.00 USD |
| `4H` | `HTX` | `77.49%` | `22.51%` | `3.44` | 174,070,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `47.94%` | `52.06%` | `0.92` | 48,350,000.00 USD |
| `4H` | `Bitfinex` | `27.35%` | `72.65%` | `0.38` | 4,640,000.00 USD |
| `4H` | `Kraken` | `58.11%` | `41.89%` | `1.39` | 3,580,000.00 USD |
| `4H` | `Aster` | `52.42%` | `47.58%` | `1.10` | 62,990,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.09%` | `48.91%` | `1.04` | 99,460,000.00 USD |
| `4H` | `Whale Positions` | `51.07%` | `48.93%` | `1.04` | 2,570,000,000.00 USD |
| `4H` | `Global Accounts` | `49.27%` | `50.73%` | `0.97` | 8,970,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2234.75` | `2234.69` | `2234.75` | `2238.25` | `2230.25` | 138,036,296.36 USD | 70,500,947.16 USD | 67,535,349.20 USD | 2,965,597.96 USD | `+2.15%` | `1B / 0S` |
| `0:00 UTC` | `2229.75` | `2230.64` | `2229.75` | `2236.75` | `2225.25` | 125,588,915.24 USD | 57,499,740.21 USD | 68,089,175.03 USD | -10,589,434.83 USD | `-8.43%` | `0B / 2S` |
| `5:00 UTC` | `2241.25` | `2240.18` | `2241.25` | `2243.25` | `2233.75` | 123,392,803.54 USD | 67,738,859.18 USD | 55,653,944.36 USD | 12,084,914.83 USD | `+9.79%` | `1B / 2S` |
| `0:00 UTC` | `2245.25` | `2244.67` | `2245.25` | `2246.25` | `2242.75` | 130,536,562.11 USD | 61,753,972.34 USD | 68,782,589.78 USD | -7,028,617.44 USD | `-5.38%` | `0B / 0S` |
| `5:00 UTC` | `2246.25` | `2244.65` | `2246.25` | `2246.75` | `2241.25` | 83,556,134.35 USD | 43,872,052.14 USD | 39,684,082.21 USD | 4,187,969.92 USD | `+5.01%` | `0B / 0S` |
| `0:00 UTC` | `2250.25` | `2247.75` | `2250.25` | `2252.75` | `2241.75` | 107,425,896.61 USD | 60,168,072.38 USD | 47,257,824.22 USD | 12,910,248.16 USD | `+12.02%` | `3B / 0S` |
| `5:00 UTC` | `2247.75` | `2247.16` | `2247.75` | `2249.25` | `2244.75` | 60,142,096.16 USD | 25,496,240.40 USD | 34,645,855.76 USD | -9,149,615.36 USD | `-15.21%` | `0B / 0S` |
| `0:00 UTC` | `2248.25` | `2248.34` | `2248.25` | `2251.75` | `2245.75` | 66,196,194.89 USD | 33,643,736.92 USD | 32,552,457.97 USD | 1,091,278.95 USD | `+1.65%` | `2B / 0S` |
| `5:00 UTC` | `2239.25` | `2242.30` | `2239.25` | `2250.25` | `2237.25` | 119,524,398.16 USD | 59,440,954.02 USD | 60,083,444.14 USD | -642,490.12 USD | `-0.54%` | `0B / 3S` |
| `0:00 UTC` | `2239.25` | `2238.89` | `2239.25` | `2239.25` | `2238.25` | 1,135,513.85 USD | 1,033,101.92 USD | 102,411.93 USD | 930,689.99 USD | `+81.96%` | `3B / 0S` |

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
| `5m` | -1,970,000.00 USD | -6,110,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,630,000.00 USD | -17,730,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 887,150.00 USD | -23,960,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 2,150,000.00 USD | -6,570,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -6,680,000.00 USD | -8,780,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 7,050,000.00 USD | 136,460,000.00 USD | **`ACCUMULATION`** |
| `6h` | -50,160,000.00 USD | -547,370,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -67,030,000.00 USD | -1,530,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -151,720,000.00 USD | -1,810,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -131,430,000.00 USD | -1,970,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -152,240,000.00 USD | -3,070,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,160,000,000.00 USD | -9,650,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.97M` | 15m=`-1.63M` | 1h=`+2.15M` | 24h=`-131.43M`
* Futures Capital Netflows: 5m=`-6.11M` | 15m=`-17.73M` | 1h=`-6.57M` | 24h=`-1.97B`
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
  * `2026-10-30 11:03:56 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:28:56 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:29:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2208.57` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2186.78` (Risk Distance: `21.79` pts)
  * +2.5R Take Profit: `2263.04`
  * Mathematical Lot Sizing: **`0.45 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2275.75` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2297.54` (Risk Distance: `21.79` pts)
  * +2.5R Take Profit: `2221.28`
  * Mathematical Lot Sizing: **`0.45 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2256.31`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
