# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 08:18:38 IST` (`2026-10-30 02:48:38 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2210.10` | **Live Ask Quote**: `2213.10` | **Mid Price**: `2211.60`
- **Spread Points**: `300.00` | **Spread BPS**: `13.56 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2207.25` | VWAP Z-Score: `+0.05` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `20.85` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `34.09` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2250.10` | Lower -3.00σ Band: `2164.40`
  * Upper +2.51σ Band: `2243.10` | Lower -2.51σ Band: `2171.40`
  * Upper +2.01σ Band: `2235.96` | Lower -2.01σ Band: `2178.54`
  * Upper +2.00σ Band: `2235.82` | Lower -2.00σ Band: `2178.68`
  * Upper +1.28σ Band: `2225.53` | Lower -1.28σ Band: `2188.97`
  * Upper +1.00σ Band: `2221.53` | Lower -1.00σ Band: `2192.97`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2210.08` | EMA-20=`2232.43` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2270.11` (Slope: `+0.0000`) | EMA-100=`2294.71`
  * Institutional Anchors: EMA-144=`2304.13` | EMA-200=`2310.46` (Slope: `-0.5269`) | EMA-233=`2314.94`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2288.70` (Distance: `-3.36%`)
  * Point of Control (POC) = `2264.42` (Distance: `-2.33%`)
  * Value Area Low (VAL) = `2206.95` (Distance: `+0.22%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2350.38` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2220.45` | Low=`2202.75`
  * New York Session (13:00-21:00 UTC): High=`2224.87` | Low=`2198.33`
  * Initial Balance (First Hour): IB High=`2218.23` | IB Low=`2204.97`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2202.75` - `2220.45`
  * Optimal Trade Entry (OTE 0.705): `2216.02`
  * Structural Invalidation Anchor (0.786): `2229.29`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2213.76` | `2216.40` | `2209.66` | `2209.95` | `15,811` | 34,997,567.89 USD | -6,628,993.30 USD | `-18.94%` | -982,088,867.62 USD | `-0.16` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `2209.95` | `2218.96` | `2209.95` | `2215.53` | `20,290` | 44,974,290.22 USD | 9,326,794.05 USD | `+20.74%` | -972,762,073.57 USD | `+0.71` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `2215.53` | `2218.08` | `2215.05` | `2215.74` | `6,871` | 15,228,706.10 USD | -1,072,834.58 USD | `-7.04%` | -973,834,908.15 USD | `+0.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2194.71` | `2205.00` | `2181.22` | `2204.63` | `94,259` | 206,705,717.00 USD | 20,614,341.75 USD | `+9.97%` | -1,018,086,254.51 USD | `+1.03` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `2204.62` | `2217.04` | `2204.41` | `2213.76` | `98,709` | 218,308,818.86 USD | 42,626,380.18 USD | `+19.53%` | -975,459,874.32 USD | `+1.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `2213.76` | `2218.96` | `2209.66` | `2215.74` | `42,972` | 95,200,564.22 USD | 1,624,966.17 USD | `+1.71%` | -973,834,908.15 USD | `+0.44` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `2252.35` | `2256.50` | `2196.26` | `2221.62` | `846,893` | 1,879,266,431.52 USD | -206,358,649.60 USD | `-10.98%` | -935,096,395.02 USD | `-1.46` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2221.62` | `2227.62` | `2172.85` | `2194.70` | `610,884` | 1,342,330,424.04 USD | -132,826,407.64 USD | `-9.90%` | -1,067,922,802.66 USD | `-0.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2194.71` | `2218.96` | `2181.22` | `2215.74` | `235,940` | 520,215,100.08 USD | 64,865,688.11 USD | `+12.47%` | -1,003,057,114.55 USD | `+1.02` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -182,194,938.56 USD | `-1.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -736,432,507.87 USD | `-1.81` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2215.74` | `1,693,717` | 3,741,811,955.64 USD | -274,319,369.13 USD | `-7.33%` | -1,010,751,877.00 USD | `-0.50` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -84,078,993.86 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | 19,961,178.38 USD | `+1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -182,194,938.56 USD | `-1.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -736,432,507.87 USD | `-1.81` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2215.74` | `1,693,717` | 3,741,811,955.64 USD | -274,319,369.13 USD | `-7.33%` | -1,010,751,877.00 USD | `-0.50` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2211.60`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2213.50` | `129.7459` | 287,192.55 USD | 6,238,630.14 USD | `6 orders` | `-0.09%` | `-` |
| `BID` | `2213.60` | `15.3386` | 33,953.52 USD | 5,951,437.59 USD | `3 orders` | `-0.08%` | `-` |
| `BID` | `2213.70` | `370.3755` | 819,900.24 USD | 5,917,484.06 USD | `6 orders` | `-0.08%` | `-` |
| `BID` | `2213.80` | `153.1538` | 339,051.88 USD | 5,097,583.82 USD | `12 orders` | `-0.07%` | `-` |
| `BID` | `2213.90` | `238.7333` | 528,531.65 USD | 4,758,531.93 USD | `9 orders` | `-0.07%` | `-` |
| `BID` | `2214.00` | `230.7883` | 510,965.30 USD | 4,230,000.28 USD | `9 orders` | `-0.07%` | `-` |
| `BID` | `2214.10` | `540.9243` | 1,197,660.49 USD | 3,719,034.99 USD | `14 orders` | `-0.06%` | `-` |
| `BID` | `2214.20` | `91.1139` | 201,744.40 USD | 2,521,374.49 USD | `8 orders` | `-0.06%` | `-` |
| `BID` | `2214.30` | `97.1291` | 215,072.97 USD | 2,319,630.10 USD | `8 orders` | `-0.05%` | `-` |
| `BID` | `2214.40` | `389.1988` | 861,841.82 USD | 2,104,557.13 USD | `12 orders` | `-0.05%` | `-` |
| `BID` | `2214.50` | `105.0012` | 232,525.16 USD | 1,242,715.31 USD | `9 orders` | `-0.04%` | `-` |
| `BID` | `2214.60` | `93.0290` | 206,022.02 USD | 1,010,190.15 USD | `8 orders` | `-0.04%` | `-` |
| `BID` | `2214.70` | `50.6602` | 112,197.14 USD | 804,168.13 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `2214.80` | `61.5884` | 136,405.99 USD | 691,970.98 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `2214.90` | `20.0905` | 44,498.45 USD | 555,564.99 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `2215.00` | `132.2098` | 292,844.71 USD | 511,066.54 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `2215.10` | `18.4340` | 40,833.15 USD | 218,221.84 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `2215.20` | `20.5812` | 45,591.47 USD | 177,388.68 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `2215.30` | `38.0469` | 84,285.30 USD | 131,797.21 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `2215.40` | `21.4462` | 47,511.91 USD | 47,511.91 USD | `2 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2215.45` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,215.45` | `0.00%` | `-` |
| `ASK` | `2215.50` | `328.0212` | 726,730.97 USD | 726,730.97 USD | `31 orders` | `+0.00%` | `-` |
| `ASK` | `2215.60` | `49.7280` | 110,177.36 USD | 836,908.33 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `2215.70` | `278.0208` | 616,010.69 USD | 1,452,919.01 USD | `8 orders` | `+0.01%` | `-` |
| `ASK` | `2215.80` | `73.1138` | 162,005.56 USD | 1,614,924.57 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `2215.90` | `244.0739` | 540,843.36 USD | 2,155,767.93 USD | `7 orders` | `+0.02%` | `-` |
| `ASK` | `2216.00` | `146.5843` | 324,830.81 USD | 2,480,598.73 USD | `10 orders` | `+0.02%` | `-` |
| `ASK` | `2216.10` | `23.4081` | 51,874.69 USD | 2,532,473.42 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `2216.20` | `285.7364` | 633,249.01 USD | 3,165,722.43 USD | `8 orders` | `+0.03%` | `-` |
| `ASK` | `2216.30` | `72.4166` | 160,496.91 USD | 3,326,219.34 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `2216.40` | `558.1791` | 1,237,148.16 USD | 4,563,367.50 USD | `10 orders` | `+0.04%` | `-` |
| `ASK` | `2216.50` | `204.1121` | 452,414.47 USD | 5,015,781.97 USD | `8 orders` | `+0.05%` | `-` |
| `ASK` | `2216.60` | `67.1498` | 148,844.25 USD | 5,164,626.22 USD | `7 orders` | `+0.05%` | `-` |
| `ASK` | `2216.70` | `311.9049` | 691,399.59 USD | 5,856,025.81 USD | `10 orders` | `+0.06%` | `-` |
| `ASK` | `2216.80` | `175.8567` | 389,839.13 USD | 6,245,864.94 USD | `10 orders` | `+0.06%` | `-` |
| `ASK` | `2216.90` | `134.1425` | 297,380.51 USD | 6,543,245.45 USD | `10 orders` | `+0.07%` | `-` |
| `ASK` | `2217.00` | `152.6412` | 338,405.54 USD | 6,881,650.99 USD | `7 orders` | `+0.07%` | `-` |
| `ASK` | `2217.10` | `146.5896` | 325,003.80 USD | 7,206,654.79 USD | `9 orders` | `+0.07%` | `-` |
| `ASK` | `2217.20` | `171.3979` | 380,023.42 USD | 7,586,678.22 USD | `11 orders` | `+0.08%` | `-` |
| `ASK` | `2217.30` | `681.8846` | 1,511,942.72 USD | 9,098,620.94 USD | `11 orders` | `+0.08%` | `-` |
| `ASK` | `2217.40` | `182.5602` | 404,808.99 USD | 9,503,429.93 USD | `9 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:13:17 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1786.70` | `30,282.40` | 54,105,627.95 USD | `AT_RISK_LIQ` | `0xde8d9e530b` | `2026-10-30 08:13:17 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1820.38` | `15,927.59` | 28,994,215.19 USD | `AT_RISK_LIQ` | `0x60468ba274` | `2026-10-30 08:13:17 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 08:13:17 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `10,000.00` | 19,261,000.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 08:13:17 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1934.08` | `8,092.45` | 15,651,468.16 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 08:13:17 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2122.44` | `30,641.99` | 65,035,850.90 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 08:13:17 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.72` | `26,025.05` | 55,426,069.56 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 08:13:17 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2150.00` | `1,500.00` | 3,225,000.00 USD | `TRIGGER_STOP` | `0x834cae1ec1` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2178.90` | `2,126.12` | 4,632,600.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2179.30` | `3,689.44` | 8,040,388.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2181.90` | `462.67` | 1,009,488.76 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2189.00` | `1,387.39` | 3,036,998.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2195.60` | `361.95` | 794,706.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2196.90` | `346.82` | 761,918.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2197.40` | `984.76` | 2,163,901.08 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2197.40` | `462.69` | 1,016,706.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2197.50` | `1,898.59` | 4,172,143.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2198.60` | `370.42` | 814,401.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.40` | `462.79` | 1,018,794.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2203.10` | `1,818.99` | 4,007,412.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2204.60` | `358.61` | 790,583.45 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2205.90` | `687.65` | 1,516,877.21 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2206.40` | `344.01` | 759,023.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2206.80` | `1,362.03` | 3,005,723.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2207.60` | `967.41` | 2,135,651.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2208.00` | `907.50` | 2,003,753.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2208.70` | `476.91` | 1,053,342.72 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2209.80` | `680.05` | 1,502,782.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2212.20` | `452.76` | 1,001,596.78 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2212.20` | `357.49` | 790,834.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2213.40` | `339.47` | 751,378.91 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2218.00` | `338.78` | 751,411.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2218.50` | `451.65` | 1,001,992.62 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2218.60` | `353.81` | 784,970.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2219.50` | `254.22` | 564,243.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2220.20` | `676.91` | 1,502,870.92 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2221.30` | `262.67` | 583,477.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2221.40` | `479.66` | 1,065,518.06 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2222.50` | `901.57` | 2,003,728.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2222.50` | `478.17` | 1,062,741.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2223.20` | `968.51` | 2,153,190.54 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2223.70` | `352.92` | 784,794.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2224.60` | `1,351.12` | 3,005,699.55 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2224.60` | `344.01` | 765,284.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2225.90` | `1,800.40` | 4,007,506.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2225.90` | `695.92` | 1,549,038.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2226.80` | `511.35` | 1,138,678.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2230.40` | `1,898.59` | 4,234,607.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2232.40` | `430.01` | 959,959.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2232.80` | `511.53` | 1,142,150.88 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2232.90` | `1,032.59` | 2,305,676.91 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:13:17 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2235.00` | `2,107.13` | 4,709,425.49 USD | `TRIGGER_STOP` | `0x5b5f798b94` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2237.80` | `340.48` | 761,921.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2238.00` | `355.10` | 794,704.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2238.30` | `378.77` | 847,800.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x6798a1b850` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2241.00` | `1,415.67` | 3,172,520.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.90` | `3,684.29` | 8,270,867.34 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2248.50` | `511.30` | 1,149,651.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 08:13:17 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2252.60` | `2,069.95` | 4,662,762.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 08:13:17 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2500.24` | `22,046.99` | 55,122,800.44 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 08:13:17 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,037.41` | 7,635,751.54 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 08:13:17 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2624.43` | `10,000.00` | 26,244,321.52 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 08:13:17 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.29` | `9,700.00` | 25,785,414.21 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 08:13:17 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 235,779,080.93 USD | `106,417.71` | `2322.74` | `2215.48` | `3834.80` | 11,401,931.22 USD | `+4.84%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 143,306,382.12 USD | `64,680.62` | `2375.30` | `2215.48` | `4403.94` | 10,329,915.38 USD | `+7.21%` | `5X Cross` |
| `10` | `0x77dd...e0e9` | `LONG` | 67,905,717.81 USD | `30,641.99` | `2610.31` | `2215.48` | `2122.31` | -12,079,457.23 USD | `-17.79%` | `10X Cross` |
| `11` | `0xde8d...9524` | `LONG` | 67,096,115.79 USD | `30,282.40` | `2134.45` | `2215.48` | `1786.57` | 2,459,785.21 USD | `+3.67%` | `20X Cross` |
| `16` | `0x0392...d7d9` | `LONG` | 57,663,185.22 USD | `26,025.05` | `2518.71` | `2215.48` | `2129.59` | -7,886,536.87 USD | `-13.68%` | `9X Cross` |
| `23` | `0x8add...7d2c` | `SHORT` | 48,847,087.92 USD | `22,046.99` | `2271.09` | `2215.48` | `2480.36` | 1,223,809.39 USD | `+2.51%` | `25X Cross` |
| `26` | `0xdf95...7d72` | `SHORT` | 44,272,933.13 USD | `19,983.27` | `2402.53` | `2215.48` | `4225.99` | 3,737,562.11 USD | `+8.44%` | `25X Cross` |
| `34` | `0xeced...6210` | `SHORT` | 36,972,827.17 USD | `16,687.58` | `2522.09` | `2215.48` | `3473.35` | 5,114,887.82 USD | `+13.83%` | `20X Cross` |
| `35` | `0xb695...a92d` | `SHORT` | 35,933,096.17 USD | `16,214.56` | `2557.74` | `2215.48` | `3955.28` | 5,539,632.66 USD | `+15.42%` | `20X Cross` |
| `36` | `0x6046...b21d` | `LONG` | 35,290,282.67 USD | `15,927.59` | `2410.19` | `2215.48` | `1790.23` | -3,098,336.98 USD | `-8.78%` | `6X Cross` |
| `39` | `0x45d2...4029` | `SHORT` | 30,915,990.00 USD | `13,950.00` | `2443.60` | `2215.48` | `5406.22` | 3,172,292.46 USD | `+10.26%` | `20X Cross` |
| `43` | `0xa61c...66b9` | `LONG` | 28,553,364.00 USD | `12,888.00` | `2369.69` | `2215.48` | `1467.87` | -1,987,290.54 USD | `-6.96%` | `10X Cross` |
| `46` | `0x2371...0883` | `LONG` | 26,587,200.00 USD | `12,000.00` | `2421.77` | `2215.48` | `1279.55` | -2,474,094.85 USD | `-9.31%` | `20X Cross` |
| `47` | `0xbd1c...ff0e` | `LONG` | 26,584,800.00 USD | `12,000.00` | `2419.91` | `2215.48` | `1520.45` | -2,454,232.39 USD | `-9.23%` | `20X Cross` |
| `54` | `0x0c5d...36b3` | `LONG` | 24,372,370.00 USD | `11,000.00` | `2482.20` | `2215.48` | `1644.52` | -2,931,883.24 USD | `-12.03%` | `20X Cross` |
| `55` | `0xa9de...e049` | `LONG` | 24,371,600.00 USD | `11,000.00` | `2481.81` | `2215.48` | `1644.19` | -2,928,379.46 USD | `-12.02%` | `20X Cross` |
| `56` | `0x09dc...c094` | `LONG` | 24,370,500.00 USD | `11,000.00` | `2465.31` | `2215.48` | `1637.52` | -2,747,923.04 USD | `-11.28%` | `20X Cross` |
| `57` | `0x6c93...59a4` | `LONG` | 24,370,500.00 USD | `11,000.00` | `2441.15` | `2215.48` | `1602.48` | -2,482,172.73 USD | `-10.19%` | `20X Cross` |
| `70` | `0xa2ce...3126` | `LONG` | 22,191,385.32 USD | `10,016.88` | `2162.83` | `2215.48` | `1563.98` | 526,583.27 USD | `+2.37%` | `10X Cross` |
| `72` | `0x6646...6de5` | `LONG` | 22,161,000.00 USD | `10,000.00` | `1765.80` | `2215.48` | `1723.63` | 4,502,942.55 USD | `+20.32%` | `25X Cross` |
| `73` | `0x15a4...dfdb` | `LONG` | 22,156,000.00 USD | `10,000.00` | `1761.94` | `2215.48` | `348.56` | 4,536,518.97 USD | `+20.48%` | `20X Cross` |
| `74` | `0xec7f...df39` | `LONG` | 22,154,000.00 USD | `10,000.00` | `2719.35` | `2215.48` | `1721.04` | -5,039,548.52 USD | `-22.75%` | `20X Cross` |
| `75` | `0xb37f...66ca` | `SHORT` | 22,154,000.00 USD | `10,000.00` | `2290.69` | `2215.48` | `2624.31` | 752,991.85 USD | `+3.40%` | `25X Cross` |
| `76` | `0x939f...04d2` | `LONG` | 21,766,327.53 USD | `9,823.81` | `2427.28` | `2215.48` | `1717.06` | -2,078,823.07 USD | `-9.55%` | `25X Cross` |
| `77` | `0xaeaa...2416` | `SHORT` | 21,491,999.00 USD | `9,700.00` | `2311.92` | `2215.48` | `2658.17` | 933,683.40 USD | `+4.34%` | `25X Cross` |
| `83` | `0xf517...c032` | `SHORT` | 20,662,522.00 USD | `9,326.35` | `2202.91` | `2215.48` | `3132.75` | -117,383.79 USD | `-0.57%` | `25X Cross` |
| `84` | `0xca49...53c8` | `SHORT` | 20,394,181.03 USD | `9,202.74` | `2549.39` | `2215.48` | `3923.74` | 3,067,246.44 USD | `+15.04%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 20,060,222.38 USD | `9,054.12` | `2493.89` | `2215.48` | `2942.52` | 2,519,784.88 USD | `+12.56%` | `20X Cross` |
| `88` | `0xea00...a918` | `LONG` | 19,949,597.86 USD | `9,003.83` | `2003.01` | `2215.48` | `1408.81` | 1,914,818.99 USD | `+9.60%` | `5X Cross` |
| `92` | `0xefe4...194b` | `SHORT` | 19,541,981.03 USD | `8,820.57` | `2267.42` | `2215.48` | `3628.97` | 458,033.36 USD | `+2.34%` | `20X Cross` |
| `114` | `0x9eec...daab` | `LONG` | 17,930,446.12 USD | `8,092.45` | `1658.44` | `2215.48` | `1931.18` | 4,509,581.59 USD | `+25.15%` | `15X Cross` |
| `116` | `0x5f91...65aa` | `LONG` | 17,647,128.78 USD | `7,964.66` | `1626.99` | `2215.48` | `1844.36` | 4,688,685.72 USD | `+26.57%` | `16X Cross` |
| `129` | `0xec0b...b078` | `LONG` | 15,525,778.46 USD | `7,007.80` | `2065.97` | `2215.48` | `1064.66` | 1,047,848.87 USD | `+6.75%` | `25X Cross` |
| `132` | `0xf02d...5eb3` | `LONG` | 15,189,161.64 USD | `6,855.99` | `2383.33` | `2215.48` | `1142.30` | -1,150,927.13 USD | `-7.58%` | `20X Cross` |
| `133` | `0xcf53...ee11` | `SHORT` | 15,088,201.48 USD | `6,803.63` | `1862.69` | `2215.48` | `4236.37` | -2,415,096.10 USD | `-16.01%` | `7X Cross` |
| `136` | `0x418a...8888` | `SHORT` | 14,897,870.09 USD | `6,724.38` | `2494.55` | `2215.48` | `3022.00` | 1,876,453.08 USD | `+12.60%` | `25X Cross` |
| `140` | `0x4ff9...38d3` | `LONG` | 14,543,351.44 USD | `6,564.10` | `2447.40` | `2215.48` | `1670.14` | -1,521,671.31 USD | `-10.46%` | `3X Isolated` |
| `142` | `0xf78c...c581` | `LONG` | 14,401,890.76 USD | `6,500.22` | `2521.53` | `2215.48` | `1913.62` | -1,988,650.19 USD | `-13.81%` | `20X Cross` |
| `146` | `0x799f...5f4c` | `LONG` | 13,984,961.71 USD | `6,310.90` | `2390.33` | `2215.48` | `1875.52` | -1,100,202.90 USD | `-7.87%` | `20X Cross` |
| `150` | `0x08bf...7872` | `SHORT` | 13,789,128.05 USD | `6,224.05` | `2258.00` | `2215.48` | `2585.40` | 264,788.05 USD | `+1.92%` | `20X Cross` |
| `153` | `0x1ee7...edf5` | `LONG` | 13,294,080.00 USD | `6,000.00` | `2308.18` | `2215.48` | `2052.79` | -555,000.40 USD | `-4.17%` | `25X Cross` |
| `154` | `0xd9e7...4aff` | `LONG` | 13,294,020.00 USD | `6,000.00` | `2480.18` | `2215.48` | `1407.91` | -1,587,104.33 USD | `-11.94%` | `20X Cross` |
| `162` | `0x0622...8088` | `LONG` | 12,654,700.32 USD | `5,711.66` | `2201.21` | `2215.48` | `470.80` | 82,131.84 USD | `+0.65%` | `5X Cross` |
| `164` | `0x0c4a...1b19` | `LONG` | 12,540,455.42 USD | `5,660.10` | `2373.06` | `2215.48` | `2081.96` | -891,302.71 USD | `-7.11%` | `25X Isolated` |
| `167` | `0xc179...e0c8` | `LONG` | 12,135,305.76 USD | `5,477.46` | `2307.21` | `2215.48` | `995.50` | -502,361.91 USD | `-4.14%` | `10X Cross` |
| `170` | `0x7fda...17d1` | `LONG` | 11,777,063.18 USD | `5,315.76` | `2211.05` | `2215.48` | `0.000000` | 23,620.93 USD | `+0.20%` | `25X Cross` |
| `180` | `0x218a...7da2` | `SHORT` | 11,572,152.38 USD | `5,222.87` | `2208.16` | `2215.48` | `2793.05` | -39,217.32 USD | `-0.34%` | `10X Cross` |
| `189` | `0x45ab...6cbc` | `LONG` | 10,903,277.53 USD | `4,920.96` | `2727.66` | `2215.48` | `1393.48` | -2,519,466.27 USD | `-23.11%` | `7X Cross` |
| `192` | `0x64b7...9da9` | `LONG` | 10,760,327.25 USD | `4,856.84` | `2604.61` | `2215.48` | `1533.65` | -1,889,887.17 USD | `-17.56%` | `25X Cross` |
| `201` | `0xfb18...eb17` | `SHORT` | 10,564,863.29 USD | `4,768.18` | `2315.53` | `2215.48` | `2558.17` | 476,018.50 USD | `+4.51%` | `25X Cross` |
| `202` | `0x5559...d43b` | `SHORT` | 10,537,228.09 USD | `4,755.93` | `2262.69` | `2215.48` | `2748.04` | 223,977.78 USD | `+2.13%` | `25X Cross` |
| `211` | `0xe091...6705` | `SHORT` | 9,970,515.44 USD | `4,500.00` | `2467.33` | `2215.48` | `2463.52` | 1,132,493.07 USD | `+11.36%` | `20X Cross` |
| `217` | `0xecb6...2b00` | `SHORT` | 9,883,355.03 USD | `4,461.00` | `2254.00` | `2215.48` | `8702.74` | 171,751.82 USD | `+1.74%` | `15X Cross` |
| `224` | `0xb829...3a81` | `LONG` | 9,736,925.32 USD | `4,394.91` | `2398.60` | `2215.48` | `1495.42` | -804,716.63 USD | `-8.26%` | `20X Cross` |
| `243` | `0x28bb...fca6` | `SHORT` | 9,331,451.80 USD | `4,209.61` | `1896.10` | `2215.48` | `3035.60` | -1,349,569.23 USD | `-14.46%` | `20X Cross` |
| `245` | `0x6ea4...0ea7` | `SHORT` | 9,270,055.81 USD | `4,184.01` | `2602.13` | `2215.48` | `3425.46` | 1,617,290.86 USD | `+17.45%` | `20X Cross` |
| `257` | `0x5e9e...35ee` | `SHORT` | 8,881,144.19 USD | `4,007.56` | `1796.39` | `2215.48` | `2585.96` | -1,681,994.10 USD | `-18.94%` | `20X Cross` |
| `258` | `0xfb94...0ddf` | `SHORT` | 8,867,375.81 USD | `4,002.10` | `2382.44` | `2215.48` | `5104.85` | 667,408.34 USD | `+7.53%` | `20X Cross` |
| `260` | `0x8cc9...2b6a` | `SHORT` | 8,862,400.00 USD | `4,000.00` | `1791.18` | `2215.48` | `3615.34` | -1,697,653.33 USD | `-19.16%` | `25X Cross` |
| `261` | `0x3dc9...54b0` | `SHORT` | 8,862,033.58 USD | `3,999.69` | `2480.32` | `2215.48` | `6729.62` | 1,058,502.97 USD | `+11.94%` | `20X Cross` |
| `276` | `0x4b67...f4e7` | `LONG` | 8,465,762.98 USD | `3,820.84` | `2591.51` | `2215.48` | `1347.66` | -1,436,010.56 USD | `-16.96%` | `20X Cross` |
| `282` | `0x12d2...f97f` | `LONG` | 8,323,836.46 USD | `3,757.26` | `2446.50` | `2215.48` | `1831.06` | -868,329.93 USD | `-10.43%` | `20X Cross` |
| `299` | `0x8ae4...3d60` | `LONG` | 7,883,544.15 USD | `3,558.20` | `2482.21` | `2215.48` | `568.11` | -948,653.88 USD | `-12.03%` | `10X Cross` |
| `334` | `0x9c2a...f6a8` | `SHORT` | 6,729,691.36 USD | `3,037.41` | `2543.83` | `2215.48` | `2598.53` | 996,982.13 USD | `+14.81%` | `20X Cross` |
| `337` | `0x007d...67a0` | `LONG` | 6,649,800.00 USD | `3,000.00` | `2400.00` | `2215.48` | `1467.15` | -550,200.00 USD | `-8.27%` | `25X Cross` |
| `338` | `0x4a20...3c26` | `LONG` | 6,648,300.00 USD | `3,000.00` | `2428.72` | `2215.48` | `708.36` | -637,860.28 USD | `-9.59%` | `20X Cross` |
| `339` | `0x469e...58a5` | `SHORT` | 6,646,770.00 USD | `3,000.00` | `2195.70` | `2215.48` | `3217.00` | -59,662.76 USD | `-0.90%` | `25X Cross` |
| `340` | `0xb823...9763` | `SHORT` | 6,646,200.00 USD | `3,000.00` | `2229.66` | `2215.48` | `3233.85` | 42,796.68 USD | `+0.64%` | `25X Cross` |
| `362` | `0x24fb...ed0f` | `LONG` | 6,292,042.56 USD | `2,839.88` | `2199.85` | `2215.48` | `1345.21` | 44,717.50 USD | `+0.71%` | `15X Cross` |
| `392` | `0x8328...f54a` | `SHORT` | 5,708,565.41 USD | `2,576.45` | `2292.01` | `2215.48` | `3279.70` | 196,705.88 USD | `+3.45%` | `25X Cross` |
| `396` | `0xed48...7c9b` | `SHORT` | 5,652,539.85 USD | `2,551.13` | `2460.02` | `2215.48` | `3241.24` | 623,306.56 USD | `+11.03%` | `20X Cross` |
| `397` | `0x1c98...7fc7` | `LONG` | 5,538,984.97 USD | `2,500.00` | `2452.60` | `2215.48` | `1917.11` | -592,536.59 USD | `-10.70%` | `10X Cross` |
| `398` | `0x970c...2a93` | `SHORT` | 5,538,975.00 USD | `2,500.00` | `2229.57` | `2215.48` | `5079.44` | 34,969.49 USD | `+0.63%` | `20X Cross` |
| `412` | `0xfbe2...c8ea` | `SHORT` | 5,284,185.37 USD | `2,385.21` | `2041.57` | `2215.48` | `2620.67` | -414,618.72 USD | `-7.85%` | `20X Cross` |
| `413` | `0x6749...ce07` | `SHORT` | 5,283,637.70 USD | `2,384.89` | `2220.92` | `2215.48` | `3632.71` | 13,025.33 USD | `+0.25%` | `20X Cross` |
| `414` | `0x645b...87b8` | `SHORT` | 5,273,073.94 USD | `2,379.98` | `2421.64` | `2215.48` | `11602.07` | 490,373.02 USD | `+9.30%` | `10X Cross` |
| `425` | `0x77ee...2902` | `SHORT` | 5,075,232.52 USD | `2,290.69` | `2476.53` | `2215.48` | `5885.09` | 597,739.72 USD | `+11.78%` | `25X Cross` |
| `432` | `0xbcd4...0dd2` | `SHORT` | 5,015,009.94 USD | `2,263.50` | `2233.24` | `2215.48` | `2705.06` | 39,947.63 USD | `+0.80%` | `25X Cross` |
| `448` | `0xd507...c948` | `SHORT` | 4,813,151.78 USD | `2,172.00` | `2387.49` | `2215.48` | `2706.88` | 372,489.25 USD | `+7.74%` | `5X Isolated` |
| `460` | `0x382b...3e39` | `SHORT` | 4,717,999.41 USD | `2,129.54` | `2296.66` | `2215.48` | `4612.01` | 172,837.80 USD | `+3.66%` | `25X Cross` |
| `461` | `0x023a...2355` | `LONG` | 4,709,673.79 USD | `2,125.78` | `2330.15` | `2215.48` | `0.000000` | -243,732.39 USD | `-5.18%` | `25X Cross` |
| `466` | `0x5b5f...c052` | `SHORT` | 4,668,547.26 USD | `2,107.13` | `2237.36` | `2215.48` | `2254.20` | 45,856.15 USD | `+0.98%` | `25X Cross` |
| `495` | `0x3453...b323` | `SHORT` | 4,431,632.75 USD | `2,000.12` | `2322.47` | `2215.48` | `2397.38` | 213,603.09 USD | `+4.82%` | `25X Cross` |
| `496` | `0x7a6d...f79c` | `SHORT` | 4,431,000.00 USD | `2,000.00` | `2418.41` | `2215.48` | `2523.62` | 405,832.11 USD | `+9.16%` | `25X Cross` |
| `504` | `0xb8eb...1dd5` | `LONG` | 4,355,201.98 USD | `1,965.79` | `2227.42` | `2215.48` | `1263.91` | -23,437.14 USD | `-0.54%` | `25X Cross` |
| `507` | `0xac48...3201` | `SHORT` | 4,352,414.21 USD | `1,964.37` | `2272.04` | `2215.48` | `3130.83` | 110,728.09 USD | `+2.54%` | `20X Cross` |
| `508` | `0xb15b...dbae` | `SHORT` | 4,345,195.17 USD | `1,961.19` | `2290.80` | `2215.48` | `2220.62` | 147,502.50 USD | `+3.39%` | `25X Cross` |
| `522` | `0x8376...9a1e` | `SHORT` | 4,233,047.78 USD | `1,910.50` | `2477.72` | `2215.48` | `3189.33` | 500,640.39 USD | `+11.83%` | `20X Cross` |
| `530` | `0xf3dc...1672` | `SHORT` | 4,166,128.50 USD | `1,880.36` | `2240.73` | `2215.48` | `2776.83` | 47,261.74 USD | `+1.13%` | `20X Cross` |
| `542` | `0xd911...961e` | `LONG` | 4,089,289.02 USD | `1,844.76` | `2200.91` | `2215.48` | `1004.39` | 29,110.79 USD | `+0.71%` | `25X Cross` |
| `553` | `0x7265...91a5` | `LONG` | 3,992,221.84 USD | `1,801.87` | `2533.96` | `2215.48` | `1987.58` | -573,644.61 USD | `-14.37%` | `20X Cross` |
| `554` | `0x739c...cfb2` | `SHORT` | 3,988,080.00 USD | `1,800.00` | `2427.60` | `2215.48` | `2447.96` | 381,616.38 USD | `+9.57%` | `25X Cross` |
| `564` | `0xa445...329d` | `LONG` | 3,937,454.12 USD | `1,776.75` | `2398.85` | `2215.48` | `2019.33` | -324,715.23 USD | `-8.25%` | `25X Cross` |
| `568` | `0x91a9...3f70` | `SHORT` | 3,916,028.69 USD | `1,767.48` | `2156.23` | `2215.48` | `3664.60` | -104,924.61 USD | `-2.68%` | `4X Cross` |
| `577` | `0xbb34...1696` | `LONG` | 3,877,440.00 USD | `1,750.00` | `2315.81` | `2215.48` | `1965.65` | -175,228.23 USD | `-4.52%` | `25X Cross` |
| `579` | `0xc619...10f5` | `LONG` | 3,877,282.50 USD | `1,750.00` | `2315.39` | `2215.48` | `1796.73` | -174,663.33 USD | `-4.50%` | `25X Cross` |
| `599` | `0xfeec...4e9c` | `SHORT` | 3,748,134.72 USD | `1,691.81` | `2566.49` | `2215.48` | `2510.90` | 593,889.79 USD | `+15.84%` | `10X Cross` |
| `621` | `0xeee0...0b53` | `LONG` | 3,627,326.31 USD | `1,637.12` | `2468.64` | `2215.48` | `237.19` | -414,149.75 USD | `-11.42%` | `7X Cross` |
| `624` | `0x27b8...12fc` | `LONG` | 3,607,100.08 USD | `1,628.12` | `2468.73` | `2215.48` | `674.97` | -412,294.55 USD | `-11.43%` | `10X Cross` |
| `626` | `0x982b...4606` | `LONG` | 3,604,506.56 USD | `1,626.82` | `2575.24` | `2215.48` | `1547.86` | -584,946.52 USD | `-16.23%` | `5X Isolated` |
| `632` | `0x73d7...8be1` | `LONG` | 3,548,367.11 USD | `1,601.47` | `2410.40` | `2215.48` | `2035.76` | -311,811.81 USD | `-8.79%` | `25X Cross` |
| `634` | `0xad54...6203` | `LONG` | 3,539,313.99 USD | `1,597.45` | `2591.98` | `2215.48` | `2057.52` | -601,264.06 USD | `-16.99%` | `10X Isolated` |
| `642` | `0x880a...311c` | `LONG` | 3,497,086.59 USD | `1,578.40` | `2209.72` | `2215.48` | `0.000000` | 9,262.74 USD | `+0.26%` | `9X Cross` |
| `656` | `0xe170...9300` | `SHORT` | 3,397,401.04 USD | `1,533.40` | `2076.39` | `2215.48` | `3166.45` | -213,451.54 USD | `-6.28%` | `25X Cross` |
| `660` | `0x4b86...df9d` | `SHORT` | 3,376,574.40 USD | `1,524.00` | `2287.40` | `2215.48` | `2760.05` | 109,423.20 USD | `+3.24%` | `9X Isolated` |
| `665` | `0x2e2b...2fab` | `LONG` | 3,339,744.48 USD | `1,507.38` | `2245.53` | `2215.48` | `1283.70` | -45,128.62 USD | `-1.35%` | `25X Cross` |
| `668` | `0x251f...6e5d` | `LONG` | 3,324,000.00 USD | `1,500.00` | `2346.68` | `2215.48` | `1942.94` | -196,030.49 USD | `-5.90%` | `20X Cross` |
| `669` | `0xf929...d1f9` | `SHORT` | 3,323,400.00 USD | `1,500.00` | `2423.37` | `2215.48` | `2678.09` | 311,655.26 USD | `+9.38%` | `25X Cross` |
| `670` | `0x834c...dd93` | `SHORT` | 3,323,400.00 USD | `1,500.00` | `2191.89` | `2215.48` | `2238.03` | -35,561.05 USD | `-1.07%` | `25X Cross` |
| `690` | `0xb885...3c54` | `LONG` | 3,213,349.88 USD | `1,450.00` | `2274.34` | `2215.48` | `47.01` | -84,458.26 USD | `-2.63%` | `20X Cross` |
| `692` | `0x3440...32c5` | `SHORT` | 3,210,203.23 USD | `1,448.97` | `2198.21` | `2215.48` | `3921.22` | -25,052.26 USD | `-0.78%` | `25X Cross` |
| `696` | `0xef70...a84c` | `SHORT` | 3,196,398.00 USD | `1,442.74` | `2424.73` | `2215.48` | `3241.64` | 301,872.82 USD | `+9.44%` | `25X Cross` |
| `700` | `0x4b5f...0dd8` | `LONG` | 3,172,643.49 USD | `1,431.96` | `2339.45` | `2215.48` | `2148.15` | -177,349.46 USD | `-5.59%` | `10X Cross` |
| `706` | `0xbadb...9ee6` | `LONG` | 3,164,231.30 USD | `1,428.16` | `1936.00` | `2215.48` | `1075.76` | 399,309.65 USD | `+12.62%` | `20X Cross` |
| `747` | `0xa0fb...96be` | `LONG` | 3,049,089.85 USD | `1,376.25` | `2293.96` | `2215.48` | `1549.38` | -107,985.04 USD | `-3.54%` | `3X Cross` |
| `752` | `0x0a97...347d` | `LONG` | 3,016,917.94 USD | `1,361.76` | `2267.88` | `2215.48` | `1636.41` | -71,386.14 USD | `-2.37%` | `20X Cross` |
| `755` | `0x6e6f...82a6` | `LONG` | 3,007,223.20 USD | `1,357.25` | `2266.68` | `2215.48` | `1523.96` | -69,245.76 USD | `-2.30%` | `20X Cross` |
| `758` | `0xa70a...4be9` | `LONG` | 3,003,462.07 USD | `1,355.66` | `2259.47` | `2215.48` | `1187.65` | -59,615.91 USD | `-1.98%` | `20X Cross` |
| `763` | `0x53f8...ceff` | `LONG` | 2,988,078.47 USD | `1,348.65` | `2276.73` | `2215.48` | `0.000000` | -82,446.00 USD | `-2.76%` | `20X Cross` |
| `781` | `0x0dd5...f6ee` | `LONG` | 2,913,514.00 USD | `1,315.00` | `2306.05` | `2215.48` | `1560.42` | -118,950.38 USD | `-4.08%` | `5X Cross` |
| `810` | `0x1f16...6d07` | `LONG` | 2,804,772.36 USD | `1,266.00` | `2261.43` | `2215.48` | `1384.99` | -58,198.87 USD | `-2.07%` | `7X Cross` |
| `820` | `0xc435...c905` | `SHORT` | 2,765,156.16 USD | `1,248.00` | `2704.38` | `2215.48` | `4324.54` | 609,914.19 USD | `+22.06%` | `20X Cross` |
| `827` | `0x6859...7e1e` | `SHORT` | 2,740,914.24 USD | `1,237.15` | `2200.39` | `2215.48` | `4892.29` | -18,687.09 USD | `-0.68%` | `25X Cross` |
| `832` | `0x7277...0b98` | `SHORT` | 2,701,651.34 USD | `1,219.45` | `2206.05` | `2215.48` | `3381.00` | -11,463.53 USD | `-0.42%` | `20X Cross` |
| `834` | `0x7178...0854` | `LONG` | 2,699,987.77 USD | `1,218.63` | `2461.81` | `2215.48` | `1216.14` | -300,058.64 USD | `-11.11%` | `10X Cross` |
| `850` | `0xaaa1...ab8c` | `SHORT` | 2,658,816.00 USD | `1,200.00` | `2276.29` | `2215.48` | `2365.67` | 72,741.58 USD | `+2.74%` | `25X Isolated` |
| `859` | `0x07fd...689d` | `LONG` | 2,629,757.90 USD | `1,186.89` | `2416.34` | `2215.48` | `0.000000` | -238,184.46 USD | `-9.06%` | `25X Cross` |
| `927` | `0x2f80...f203` | `SHORT` | 2,412,549.01 USD | `1,088.94` | `1984.00` | `2215.48` | `2958.76` | -252,081.82 USD | `-10.45%` | `20X Cross` |
| `935` | `0x6f11...0389` | `SHORT` | 2,390,707.93 USD | `1,079.00` | `2333.39` | `2215.48` | `3199.15` | 127,020.98 USD | `+5.31%` | `25X Cross` |
| `936` | `0x8eb7...b90f` | `LONG` | 2,387,925.19 USD | `1,077.74` | `2396.38` | `2215.48` | `1881.39` | -194,752.85 USD | `-8.16%` | `5X Isolated` |
| `937` | `0x2b61...2f6c` | `SHORT` | 2,385,297.99 USD | `1,076.60` | `2681.75` | `2215.48` | `6478.15` | 501,874.75 USD | `+21.04%` | `10X Cross` |
| `958` | `0x30af...393e` | `SHORT` | 2,306,877.83 USD | `1,041.16` | `2252.26` | `2215.48` | `2297.36` | 38,104.49 USD | `+1.65%` | `25X Cross` |
| `967` | `0x2577...4897` | `LONG` | 2,292,559.74 USD | `1,034.78` | `2234.33` | `2215.48` | `0.000000` | -19,493.91 USD | `-0.85%` | `15X Cross` |
| `975` | `0x1b2a...f7a6` | `LONG` | 2,271,877.12 USD | `1,025.37` | `2737.51` | `2215.48` | `882.53` | -535,082.82 USD | `-23.55%` | `10X Cross` |
| `982` | `0x001a...fef6` | `SHORT` | 2,231,688.24 USD | `1,007.33` | `2022.19` | `2215.48` | `3095.82` | -194,680.29 USD | `-8.72%` | `10X Cross` |
| `983` | `0x02aa...1806` | `SHORT` | 2,231,230.27 USD | `1,007.10` | `2654.68` | `2215.48` | `3613.15` | 442,301.83 USD | `+19.82%` | `20X Cross` |
| `985` | `0xdb3a...cf3b` | `LONG` | 2,222,793.60 USD | `1,003.22` | `2705.01` | `2215.48` | `0.000000` | -490,913.29 USD | `-22.09%` | `4X Cross` |
| `987` | `0x816f...f299` | `LONG` | 2,216,200.00 USD | `1,000.00` | `2203.57` | `2215.48` | `2068.88` | 12,624.83 USD | `+0.57%` | `25X Cross` |
| `988` | `0x8c02...b73f` | `SHORT` | 2,215,680.00 USD | `1,000.00` | `2250.37` | `2215.48` | `8098.83` | 34,691.47 USD | `+1.57%` | `20X Cross` |
| `990` | `0x5272...fcd9` | `SHORT` | 2,215,500.00 USD | `1,000.00` | `2241.82` | `2215.48` | `2831.20` | 26,324.49 USD | `+1.19%` | `5X Cross` |
| `992` | `0xd7b8...9f55` | `LONG` | 2,213,384.40 USD | `999.00` | `2195.00` | `2215.48` | `0.000000` | 20,579.40 USD | `+0.93%` | `15X Cross` |
| `1021` | `0xb002...ed8a` | `SHORT` | 2,133,211.63 USD | `962.78` | `2299.66` | `2215.48` | `4200.76` | 80,866.28 USD | `+3.79%` | `25X Cross` |
| `1038` | `0xb812...b5e0` | `LONG` | 2,084,972.11 USD | `941.05` | `2263.21` | `2215.48` | `1188.27` | -44,816.79 USD | `-2.15%` | `25X Cross` |
| `1048` | `0xb1ec...e86a` | `SHORT` | 2,068,569.24 USD | `933.64` | `2272.72` | `2215.48` | `12748.82` | 53,337.72 USD | `+2.58%` | `25X Cross` |
| `1063` | `0xef96...9383` | `LONG` | 2,033,043.18 USD | `917.57` | `2235.00` | `2215.48` | `0.000000` | -17,740.47 USD | `-0.87%` | `25X Cross` |
| `1069` | `0x9606...4e5d` | `SHORT` | 2,022,826.36 USD | `913.00` | `2478.70` | `2215.48` | `4418.55` | 240,227.25 USD | `+11.88%` | `20X Cross` |
| `1090` | `0x5f10...d49d` | `LONG` | 1,993,914.00 USD | `900.00` | `2249.83` | `2215.48` | `1840.00` | -30,939.47 USD | `-1.55%` | `25X Cross` |
| `1109` | `0x82f6...12ec` | `SHORT` | 1,965,336.96 USD | `887.02` | `2199.66` | `2215.48` | `2249.72` | -14,194.13 USD | `-0.72%` | `25X Cross` |
| `1177` | `0xcd27...52a8` | `LONG` | 1,854,977.31 USD | `837.21` | `2553.56` | `2215.48` | `1403.67` | -282,887.46 USD | `-15.25%` | `2X Cross` |
| `1200` | `0x9599...c60a` | `LONG` | 1,827,291.67 USD | `824.78` | `2231.44` | `2215.48` | `0.000000` | -13,152.73 USD | `-0.72%` | `20X Cross` |
| `1222` | `0x2e30...4cb5` | `SHORT` | 1,790,234.83 USD | `808.09` | `2335.57` | `2215.48` | `8399.68` | 97,113.89 USD | `+5.42%` | `2X Cross` |
| `1237` | `0x04a9...95aa` | `LONG` | 1,772,536.00 USD | `800.00` | `2595.13` | `2215.48` | `1867.63` | -303,570.74 USD | `-17.13%` | `5X Cross` |
| `1238` | `0x7737...bf66` | `SHORT` | 1,772,010.94 USD | `799.79` | `2494.83` | `2215.48` | `23560.27` | 223,335.09 USD | `+12.60%` | `15X Cross` |
| `1267` | `0x458d...ab3b` | `LONG` | 1,716,583.69 USD | `774.75` | `2740.41` | `2215.48` | `1887.43` | -406,545.50 USD | `-23.68%` | `3X Isolated` |
| `1270` | `0x31de...13f2` | `LONG` | 1,711,365.58 USD | `772.42` | `2255.44` | `2215.48` | `0.000000` | -30,784.12 USD | `-1.80%` | `20X Cross` |
| `1323` | `0xf910...0a2d` | `LONG` | 1,625,085.64 USD | `733.51` | `2225.91` | `2215.48` | `0.000000` | -7,638.23 USD | `-0.47%` | `5X Cross` |
| `1327` | `0xaa53...9cb7` | `LONG` | 1,618,060.96 USD | `730.34` | `2389.70` | `2215.48` | `1958.57` | -127,228.68 USD | `-7.86%` | `20X Cross` |
| `1329` | `0x3fc5...c0c1` | `SHORT` | 1,617,220.06 USD | `729.92` | `2702.11` | `2215.48` | `4815.32` | 355,122.14 USD | `+21.96%` | `25X Cross` |
| `1338` | `0x6463...42f5` | `LONG` | 1,610,405.96 USD | `726.88` | `2214.40` | `2215.48` | `0.0050` | 795.30 USD | `+0.05%` | `1X Cross` |
| `1349` | `0x71d0...8c26` | `LONG` | 1,596,864.83 USD | `720.77` | `2225.97` | `2215.48` | `0.000000` | -7,552.40 USD | `-0.47%` | `25X Cross` |
| `1350` | `0xa189...94d7` | `SHORT` | 1,595,257.47 USD | `719.98` | `2691.84` | `2215.48` | `2915.26` | 342,815.19 USD | `+21.49%` | `25X Cross` |
| `1352` | `0xf71a...7215` | `LONG` | 1,593,056.28 USD | `719.02` | `2215.26` | `2215.48` | `1743.89` | 239.28 USD | `+0.02%` | `25X Cross` |
| `1367` | `0x2f93...4404` | `LONG` | 1,567,827.59 USD | `707.47` | `1700.45` | `2215.48` | `1369.06` | 364,801.22 USD | `+23.27%` | `4X Isolated` |
| `1380` | `0x5605...fe0f` | `SHORT` | 1,555,599.15 USD | `702.14` | `2566.90` | `2215.48` | `3079.99` | 246,733.50 USD | `+15.86%` | `20X Cross` |
| `1384` | `0x7743...e4fe` | `SHORT` | 1,552,082.26 USD | `700.56` | `2298.56` | `2215.48` | `6178.27` | 58,192.83 USD | `+3.75%` | `25X Cross` |
| `1395` | `0x0deb...0bc5` | `LONG` | 1,550,850.00 USD | `700.00` | `2071.05` | `2215.48` | `1597.65` | 101,114.21 USD | `+6.52%` | `20X Cross` |
| `1432` | `0x0c68...82d0` | `LONG` | 1,513,412.48 USD | `683.10` | `2207.13` | `2215.48` | `0.000000` | 5,715.85 USD | `+0.38%` | `6X Cross` |
| `1437` | `0xdbd1...29dd` | `SHORT` | 1,509,525.86 USD | `680.70` | `3030.57` | `2215.48` | `3778.82` | 553,395.26 USD | `+36.66%` | `6X Cross` |
| `1444` | `0x71e5...be04` | `LONG` | 1,501,343.69 USD | `677.67` | `2727.27` | `2215.48` | `1471.21` | -346,841.92 USD | `-23.10%` | `20X Cross` |
| `1446` | `0x0b23...f37b` | `LONG` | 1,495,523.25 USD | `675.00` | `2238.15` | `2215.48` | `608.21` | -15,233.39 USD | `-1.02%` | `5X Cross` |
| `1477` | `0x0cac...6170` | `SHORT` | 1,456,822.75 USD | `657.50` | `2146.55` | `2215.48` | `2839.64` | -45,460.55 USD | `-3.12%` | `20X Cross` |
| `1510` | `0xf00e...fe3d` | `SHORT` | 1,424,622.08 USD | `642.88` | `2333.21` | `2215.48` | `2502.52` | 75,355.89 USD | `+5.29%` | `20X Cross` |
| `1514` | `0xffb2...5ed6` | `SHORT` | 1,419,676.51 USD | `640.77` | `2672.96` | `2215.48` | `2461.73` | 293,071.83 USD | `+20.64%` | `20X Cross` |
| `1525` | `0x8505...1821` | `SHORT` | 1,404,475.65 USD | `633.96` | `2239.93` | `2215.48` | `3842.62` | 15,555.95 USD | `+1.11%` | `20X Cross` |
| `1545` | `0xfce0...f4c0` | `SHORT` | 1,381,698.05 USD | `623.60` | `3129.61` | `2215.48` | `2785.98` | 569,928.54 USD | `+41.25%` | `20X Cross` |
| `1583` | `0xad02...eb65` | `LONG` | 1,330,613.99 USD | `600.62` | `2460.69` | `2215.48` | `1079.13` | -147,326.57 USD | `-11.07%` | `5X Cross` |
| `1585` | `0x638f...f5f0` | `LONG` | 1,329,720.00 USD | `600.00` | `4011.50` | `2215.48` | `497.90` | -1,077,183.53 USD | `-81.01%` | `25X Cross` |
| `1586` | `0x26e6...6b28` | `LONG` | 1,329,408.00 USD | `600.00` | `1769.78` | `2215.48` | `2004.93` | 267,536.47 USD | `+20.12%` | `20X Cross` |
| `1596` | `0x7c90...d129` | `LONG` | 1,316,921.71 USD | `594.17` | `2286.01` | `2215.48` | `1867.61` | -41,361.17 USD | `-3.14%` | `20X Cross` |
| `1657` | `0xfc66...ca06` | `SHORT` | 1,257,147.59 USD | `567.43` | `2275.19` | `2215.48` | `7328.66` | 33,875.62 USD | `+2.69%` | `20X Cross` |
| `1662` | `0xfb99...37f3` | `LONG` | 1,252,614.97 USD | `565.34` | `2362.35` | `2215.48` | `1257.37` | -82,921.39 USD | `-6.62%` | `3X Cross` |
| `1675` | `0x844b...7f42` | `SHORT` | 1,242,945.99 USD | `561.00` | `2026.17` | `2215.48` | `3112.19` | -106,262.58 USD | `-8.55%` | `25X Cross` |
| `1687` | `0xabe6...1d99` | `SHORT` | 1,231,771.26 USD | `556.00` | `2484.68` | `2215.48` | `3137.31` | 149,724.63 USD | `+12.16%` | `20X Cross` |
| `1693` | `0x2a76...9a53` | `LONG` | 1,229,580.34 USD | `554.99` | `2231.40` | `2215.48` | `0.000000` | -8,826.71 USD | `-0.72%` | `25X Cross` |
| `1695` | `0xbef3...0d3e` | `LONG` | 1,223,774.36 USD | `552.33` | `2232.78` | `2215.48` | `2069.18` | -9,450.99 USD | `-0.77%` | `20X Cross` |
| `1699` | `0x6a41...a3b9` | `LONG` | 1,220,060.78 USD | `550.69` | `2232.16` | `2215.48` | `2074.61` | -9,178.90 USD | `-0.75%` | `20X Cross` |
| `1701` | `0x936c...bb0f` | `LONG` | 1,218,721.29 USD | `550.09` | `2218.31` | `2215.48` | `0.000000` | -1,545.98 USD | `-0.13%` | `20X Cross` |
| `1702` | `0x825c...465e` | `LONG` | 1,218,470.00 USD | `550.00` | `2208.12` | `2215.48` | `1189.72` | 4,000.50 USD | `+0.33%` | `4X Cross` |
| `1710` | `0xad21...fb6a` | `LONG` | 1,212,390.72 USD | `547.26` | `2565.80` | `2215.48` | `1746.45` | -191,762.28 USD | `-15.82%` | `6X Cross` |
| `1767` | `0x51f6...2b39` | `LONG` | 1,158,696.31 USD | `523.00` | `2226.44` | `2215.48` | `0.000000` | -5,726.78 USD | `-0.49%` | `25X Cross` |
| `1806` | `0x0c7a...2f50` | `SHORT` | 1,128,232.96 USD | `509.25` | `2122.56` | `2215.48` | `4128.81` | -47,327.53 USD | `-4.19%` | `20X Cross` |
| `1814` | `0x0089...2410` | `SHORT` | 1,124,003.88 USD | `507.35` | `2308.88` | `2215.48` | `3378.77` | 47,396.38 USD | `+4.22%` | `20X Cross` |
| `1819` | `0xfc27...9d9d` | `SHORT` | 1,119,489.27 USD | `505.14` | `2284.97` | `2215.48` | `40760.30` | 34,743.43 USD | `+3.10%` | `25X Cross` |
| `1828` | `0x89b2...9ca6` | `LONG` | 1,108,835.00 USD | `500.00` | `2363.45` | `2215.48` | `1941.75` | -72,892.42 USD | `-6.57%` | `25X Cross` |
| `1829` | `0xb322...d51f` | `SHORT` | 1,108,350.00 USD | `500.00` | `2268.03` | `2215.48` | `3700.84` | 25,666.32 USD | `+2.32%` | `20X Cross` |
| `1833` | `0x4044...794c` | `LONG` | 1,107,840.00 USD | `500.00` | `2260.80` | `2215.48` | `0.000000` | -22,560.00 USD | `-2.04%` | `25X Cross` |
| `1834` | `0xe282...df29` | `LONG` | 1,107,835.00 USD | `500.00` | `2309.84` | `2215.48` | `2045.57` | -47,089.21 USD | `-4.25%` | `10X Isolated` |
| `1835` | `0xa559...ff95` | `LONG` | 1,107,835.00 USD | `500.00` | `2260.68` | `2215.48` | `1069.33` | -22,509.36 USD | `-2.03%` | `20X Cross` |
| `1836` | `0x6936...9417` | `SHORT` | 1,107,800.00 USD | `500.00` | `2315.11` | `2215.48` | `2359.15` | 49,755.21 USD | `+4.49%` | `25X Isolated` |
| `1841` | `0x7298...7d6c` | `SHORT` | 1,103,739.44 USD | `498.15` | `3426.75` | `2215.48` | `5421.86` | 603,296.38 USD | `+54.66%` | `20X Cross` |
| `1852` | `0x9c68...7783` | `SHORT` | 1,092,923.43 USD | `493.31` | `2273.58` | `2215.48` | `3902.53` | 28,655.82 USD | `+2.62%` | `25X Cross` |
| `1857` | `0x404c...5f03` | `SHORT` | 1,085,902.99 USD | `489.79` | `2671.94` | `2215.48` | `5282.24` | 222,776.57 USD | `+20.52%` | `20X Cross` |
| `1864` | `0x321f...1c84` | `SHORT` | 1,081,242.04 USD | `488.02` | `2370.09` | `2215.48` | `3050.18` | 75,402.56 USD | `+6.97%` | `10X Cross` |
| `1911` | `0xe86b...3664` | `LONG` | 1,035,578.32 USD | `467.42` | `2231.40` | `2215.48` | `0.000000` | -7,436.70 USD | `-0.72%` | `25X Cross` |
| `1915` | `0xaa7a...af37` | `LONG` | 1,032,679.25 USD | `466.14` | `2212.37` | `2215.48` | `0.000000` | 1,409.49 USD | `+0.14%` | `20X Cross` |
| `1925` | `0x94b6...e5b3` | `SHORT` | 1,027,955.71 USD | `463.86` | `2261.12` | `2215.48` | `2403.35` | 20,886.95 USD | `+2.03%` | `25X Cross` |
| `1932` | `0x82c6...fe42` | `LONG` | 1,024,752.00 USD | `462.50` | `2501.38` | `2215.48` | `2053.91` | -132,138.57 USD | `-12.89%` | `5X Isolated` |
| `1934` | `0xe330...77a1` | `SHORT` | 1,021,832.32 USD | `461.20` | `2206.97` | `2215.48` | `6452.04` | -3,974.96 USD | `-0.39%` | `20X Cross` |
| `1938` | `0x2de3...486d` | `LONG` | 1,020,016.20 USD | `460.40` | `2286.27` | `2215.48` | `1092.91` | -32,584.71 USD | `-3.19%` | `25X Cross` |
| `1948` | `0x617e...0f97` | `SHORT` | 1,014,358.11 USD | `457.85` | `2205.60` | `2215.48` | `3432.03` | -4,514.27 USD | `-0.45%` | `10X Cross` |

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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2303.89` (Vol: 21,900,000.00 USD, Dist: `+1.64%`) | Long MP=`2242.01` (Vol: 36,100,000.00 USD, Dist: `--1.09%`)
  * 48H Horizon: Short MP=`2402.77` (Vol: 36,200,000.00 USD, Dist: `+6.00%`) | Long MP=`2242.90` (Vol: 36,100,000.00 USD, Dist: `--1.05%`)
  * 3D Horizon: Short MP=`2402.77` (Vol: 36,700,000.00 USD, Dist: `+6.00%`) | Long MP=`2242.90` (Vol: 36,100,000.00 USD, Dist: `--1.05%`)
  * 7D Horizon: Short MP=`2393.80` (Vol: 49,300,000.00 USD, Dist: `+5.60%`) | Long MP=`2241.80` (Vol: 29,100,000.00 USD, Dist: `--1.10%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `445.00` | 15,690.00 USD | 787,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `455.00` | 61,760.00 USD | 787,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `465.00` | 58,550.00 USD | 787,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 815.76 USD | 787,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 38,240.00 USD | 787,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 4,280.00 USD | 787,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 121,420.00 USD | 787,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 48,930.00 USD | 787,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 216,050.00 USD | 787,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 9,430.00 USD | 787,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 15,440.00 USD | 787,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 4,060.00 USD | 787,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 202,350.00 USD | 787,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 1,440.00 USD | 786,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 140,000.00 USD | 786,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 55,430.00 USD | 786,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 34,800.00 USD | 786,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 421,220.00 USD | 786,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 2,610,000.00 USD | 786,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 34,490.00 USD | 783,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 51,980.00 USD | 783,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 41,250.00 USD | 783,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 30,030.00 USD | 783,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 9,430.00 USD | 783,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 112,430.00 USD | 783,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 93,960.00 USD | 783,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 5,510.00 USD | 783,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 90,680.00 USD | 783,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 583,860.00 USD | 783,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 1,270,000.00 USD | 782,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 63,950.00 USD | 781,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 51,360.00 USD | 781,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 31,470.00 USD | 781,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 9,500.00 USD | 781,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 23,830.00 USD | 781,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 1,110.00 USD | 781,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 57,090.00 USD | 781,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 64,600.00 USD | 781,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 486,190.00 USD | 781,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 8,660.00 USD | 780,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 2,550,000.00 USD | 780,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 175,900.00 USD | 778,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 40,320.00 USD | 777,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 6,570,000.00 USD | 777,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 1,060,000.00 USD | 771,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 25,390.00 USD | 770,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 346,270.00 USD | 770,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 399,470.00 USD | 769,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 199,740.00 USD | 769,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 189,000.00 USD | 769,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 172,210.00 USD | 769,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 152,260.00 USD | 768,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 70,060.00 USD | 768,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 231,240.00 USD | 768,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 492,680.00 USD | 768,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 305,430.00 USD | 767,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 5,690,000.00 USD | 767,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 226,700.00 USD | 761,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 445,280.00 USD | 761,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 38,930.00 USD | 761,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 624,800.00 USD | 761,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 270,220.00 USD | 760,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 702,800.00 USD | 760,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 8,300,000.00 USD | 759,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 50,300.00 USD | 751,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 24,580.00 USD | 751,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 1,890,000.00 USD | 751,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 91,900.00 USD | 749,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 710,890.00 USD | 749,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 154,300.00 USD | 748,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 185,980.00 USD | 748,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 8,540,000.00 USD | 748,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 29,690.00 USD | 739,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 98,410.00 USD | 739,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 152,890.00 USD | 739,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 344,340.00 USD | 739,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 1,340,000.00 USD | 739,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 110,070.00 USD | 737,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 249,600.00 USD | 737,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 318,870.00 USD | 737,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 43,050.00 USD | 737,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 561,480.00 USD | 736,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 4,270,000.00 USD | 736,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 15,390,000.00 USD | 732,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 3,590,000.00 USD | 716,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 356,990.00 USD | 713,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 634,790.00 USD | 712,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 171,480.00 USD | 712,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 1,390,000.00 USD | 712,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 340,530.00 USD | 710,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 219,560.00 USD | 710,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 218,570.00 USD | 710,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 3,480,000.00 USD | 709,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 342,230.00 USD | 706,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 5,870,000.00 USD | 706,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 2,080,000.00 USD | 700,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 16,920,000.00 USD | 698,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 161,500.00 USD | 681,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 446,770.00 USD | 680,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 1,200,000.00 USD | 680,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 275,040.00 USD | 679,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 124,030.00 USD | 679,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 5,240,000.00 USD | 678,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 1,600,000.00 USD | 673,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 297,900.00 USD | 672,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 316,410.00 USD | 671,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 40,070,000.00 USD | 671,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 465,650.00 USD | 631,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 18,830,000.00 USD | 630,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 1,620,000.00 USD | 612,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 12,780,000.00 USD | 610,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 791,900.00 USD | 597,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 7,320,000.00 USD | 596,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 3,220,000.00 USD | 589,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 858,690.00 USD | 586,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 17,770,000.00 USD | 585,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 18,280,000.00 USD | 567,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 417,190.00 USD | 549,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 229,350.00 USD | 549,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 18,510,000.00 USD | 548,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 36,690,000.00 USD | 530,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 17,680,000.00 USD | 493,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 1,300,000.00 USD | 475,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 14,490,000.00 USD | 474,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 834,950.00 USD | 460,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 750,540.00 USD | 459,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 612,790.00 USD | 458,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 17,740,000.00 USD | 457,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 18,490,000.00 USD | 440,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 812,780.00 USD | 421,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 1,460,000.00 USD | 420,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 1,190,000.00 USD | 419,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 844,050.00 USD | 418,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 1,400,000.00 USD | 417,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 55,030,000.00 USD | 416,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 531,540.00 USD | 360,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 1,380,000.00 USD | 360,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 671,350.00 USD | 359,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 32,790,000.00 USD | 358,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 1,120,000.00 USD | 325,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 15,590,000.00 USD | 324,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 3,510,000.00 USD | 308,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 7,810,000.00 USD | 305,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 7,250,000.00 USD | 297,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 6,920,000.00 USD | 290,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 849,020.00 USD | 283,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 13,180,000.00 USD | 282,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 18,510,000.00 USD | 269,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 14,870,000.00 USD | 250,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 18,190,000.00 USD | 235,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 2,290,000.00 USD | 217,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 443,030.00 USD | 215,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 1,060,000.00 USD | 215,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,720,000.00 USD | 214,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1985.00` | 5,210,000.00 USD | 212,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1995.00` | 1,720,000.00 USD | 207,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2005.00` | 5,640,000.00 USD | 205,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2015.00` | 2,090,000.00 USD | 199,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,210,000.00 USD | 197,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2025.30` | 942,910,000.00 USD | 942,910,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2027.00` | 534,200,000.00 USD | 534,200,000.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.60` | 942,730,000.00 USD | 942,730,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2029.60` | 533,220,000.00 USD | 533,220,000.00 USD | 87,180.00 USD | 163,200.00 USD | 43,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.90` | 941,520,000.00 USD | 941,520,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.20` | 532,920,000.00 USD | 532,920,000.00 USD | 1,360,000.00 USD | 542,800.00 USD | 408,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2034.80` | 530,610,000.00 USD | 530,610,000.00 USD | 1,030,000.00 USD | 787,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 2,090,000.00 USD | 196,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2035.20` | 940,070,000.00 USD | 940,070,000.00 USD | 146,420.00 USD | 186,130.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2037.40` | 528,790,000.00 USD | 528,790,000.00 USD | 202,200.00 USD | 317,820.00 USD | 378,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.50` | 938,380,000.00 USD | 938,380,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2040.00` | 527,890,000.00 USD | 527,890,000.00 USD | 345,650.00 USD | 178,560.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2042.60` | 527,330,000.00 USD | 527,330,000.00 USD | 626,840.00 USD | 0.00 USD | 20,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 3,520,000.00 USD | 194,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2045.10` | 936,930,000.00 USD | 936,930,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2045.20` | 526,690,000.00 USD | 526,690,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2047.80` | 526,660,000.00 USD | 526,660,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.40` | 525,830,000.00 USD | 525,830,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2051.70` | 936,630,000.00 USD | 936,630,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2053.00` | 524,720,000.00 USD | 524,720,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 19,100,000.00 USD | 190,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2055.60` | 524,700,000.00 USD | 524,700,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2058.20` | 524,370,000.00 USD | 524,370,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2058.30` | 934,120,000.00 USD | 934,120,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2060.80` | 523,610,000.00 USD | 523,610,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.60` | 933,780,000.00 USD | 933,780,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2063.40` | 523,530,000.00 USD | 523,530,000.00 USD | 643,750.00 USD | 555,980.00 USD | 600,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.90` | 928,520,000.00 USD | 928,520,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 8,630,000.00 USD | 171,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2066.00` | 521,730,000.00 USD | 521,730,000.00 USD | 808,950.00 USD | 100,330.00 USD | 53,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2068.20` | 925,990,000.00 USD | 925,990,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2068.60` | 520,770,000.00 USD | 520,770,000.00 USD | 57,300.00 USD | 1,270,000.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2071.20` | 519,410,000.00 USD | 519,410,000.00 USD | 1,040,000.00 USD | 534,600.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.50` | 921,500,000.00 USD | 921,500,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.80` | 517,400,000.00 USD | 517,400,000.00 USD | 419,970.00 USD | 62,630.00 USD | 926,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.80` | 915,040,000.00 USD | 915,040,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 6,700,000.00 USD | 163,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2076.40` | 515,990,000.00 USD | 515,990,000.00 USD | 2,580,000.00 USD | 1,020,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.10` | 903,340,000.00 USD | 903,340,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2079.00` | 510,390,000.00 USD | 510,390,000.00 USD | 1,320,000.00 USD | 1,010,000.00 USD | 436,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.40` | 891,050,000.00 USD | 891,050,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2081.60` | 507,620,000.00 USD | 507,620,000.00 USD | 1,430,000.00 USD | 1,260,000.00 USD | 227,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2084.20` | 504,700,000.00 USD | 504,700,000.00 USD | 2,090,000.00 USD | 1,290,000.00 USD | 753,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.70` | 880,410,000.00 USD | 880,410,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 13,110,000.00 USD | 156,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2086.80` | 500,570,000.00 USD | 500,570,000.00 USD | 1,600,000.00 USD | 1,650,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.00` | 871,620,000.00 USD | 871,620,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2089.40` | 495,720,000.00 USD | 495,720,000.00 USD | 1,080,000.00 USD | 220,540.00 USD | 92,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.30` | 863,190,000.00 USD | 863,190,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.00` | 494,330,000.00 USD | 494,330,000.00 USD | 1,130,000.00 USD | 514,440.00 USD | 955,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2094.60` | 491,720,000.00 USD | 491,720,000.00 USD | 2,040,000.00 USD | 1,120,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.60` | 850,240,000.00 USD | 850,240,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,670,000.00 USD | 143,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2097.20` | 487,130,000.00 USD | 487,130,000.00 USD | 617,040.00 USD | 1,010,000.00 USD | 984,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.90` | 840,020,000.00 USD | 840,020,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2099.80` | 484,520,000.00 USD | 484,520,000.00 USD | 172,210.00 USD | 403,100.00 USD | 11,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.20` | 833,180,000.00 USD | 833,180,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.40` | 483,930,000.00 USD | 483,930,000.00 USD | 507,510.00 USD | 289,160.00 USD | 466,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2104.50` | 826,580,000.00 USD | 826,580,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2105.00` | 482,670,000.00 USD | 482,670,000.00 USD | 612,280.00 USD | 671,930.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,870,000.00 USD | 141,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2107.60` | 481,350,000.00 USD | 481,350,000.00 USD | 603,300.00 USD | 0.00 USD | 488,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.80` | 821,140,000.00 USD | 821,140,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.20` | 480,260,000.00 USD | 480,260,000.00 USD | 61,010.00 USD | 31,550.00 USD | 196,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2111.10` | 816,650,000.00 USD | 816,650,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2112.80` | 479,970,000.00 USD | 479,970,000.00 USD | 911,810.00 USD | 643,210.00 USD | 224,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2114.40` | 808,610,000.00 USD | 808,610,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,630,000.00 USD | 139,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2115.40` | 478,190,000.00 USD | 478,190,000.00 USD | 0.00 USD | 13,230.00 USD | 426,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.70` | 801,880,000.00 USD | 801,880,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2118.00` | 477,750,000.00 USD | 477,750,000.00 USD | 202,840.00 USD | 14,580.00 USD | 472,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.60` | 477,060,000.00 USD | 477,060,000.00 USD | 744,340.00 USD | 215,530.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2121.00` | 793,040,000.00 USD | 793,040,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.20` | 475,050,000.00 USD | 475,050,000.00 USD | 757,170.00 USD | 1,210,000.00 USD | 917,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.30` | 786,240,000.00 USD | 786,240,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,050,000.00 USD | 138,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.80` | 472,170,000.00 USD | 472,170,000.00 USD | 68,480.00 USD | 554,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.60` | 782,920,000.00 USD | 782,920,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.40` | 471,540,000.00 USD | 471,540,000.00 USD | 107,010.00 USD | 475,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.90` | 774,620,000.00 USD | 774,620,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2131.00` | 470,960,000.00 USD | 470,960,000.00 USD | 0.00 USD | 18,610.00 USD | 331,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.20` | 768,200,000.00 USD | 768,200,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 3,190,000.00 USD | 15,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2136.20` | 470,610,000.00 USD | 470,610,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.50` | 765,170,000.00 USD | 765,170,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.80` | 763,210,000.00 USD | 763,210,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.10` | 759,270,000.00 USD | 759,270,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 4,860,000.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2147.40` | 757,430,000.00 USD | 757,430,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.70` | 756,350,000.00 USD | 756,350,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2151.80` | 470,330,000.00 USD | 470,330,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.00` | 755,390,000.00 USD | 755,390,000.00 USD | 128,430.00 USD | 311,060.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2154.40` | 469,680,000.00 USD | 469,680,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 3,200,000.00 USD | 7,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2157.30` | 754,920,000.00 USD | 754,920,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2159.60` | 468,290,000.00 USD | 468,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 37,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.60` | 752,430,000.00 USD | 752,430,000.00 USD | 613,630.00 USD | 1,900,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2162.20` | 465,960,000.00 USD | 465,960,000.00 USD | 0.00 USD | 932,730.00 USD | 100,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.90` | 747,910,000.00 USD | 747,910,000.00 USD | 566,120.00 USD | 2,950,000.00 USD | 540,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2164.80` | 464,930,000.00 USD | 464,930,000.00 USD | 217,960.00 USD | 408,000.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 2,640,000.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2167.20` | 743,850,000.00 USD | 743,850,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.40` | 464,190,000.00 USD | 464,190,000.00 USD | 3,220,000.00 USD | 0.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.00` | 459,950,000.00 USD | 459,950,000.00 USD | 5,210,000.00 USD | 5,170,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.50` | 740,150,000.00 USD | 740,150,000.00 USD | 3,500,000.00 USD | 3,730,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2172.60` | 446,820,000.00 USD | 446,820,000.00 USD | 63,650.00 USD | 1,290,000.00 USD | 581,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.80` | 727,710,000.00 USD | 727,710,000.00 USD | 4,370,000.00 USD | 363,040.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 1,150,000.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.20` | 444,890,000.00 USD | 444,890,000.00 USD | 1,970,000.00 USD | 111,190.00 USD | 894,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2177.10` | 721,850,000.00 USD | 721,850,000.00 USD | 1,750,000.00 USD | 1,330,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2177.80` | 441,920,000.00 USD | 441,920,000.00 USD | 2,320,000.00 USD | 1,770,000.00 USD | 99,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2180.40` | 437,720,000.00 USD | 437,720,000.00 USD | 2,080,000.00 USD | 267,450.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2180.40` | 715,950,000.00 USD | 715,950,000.00 USD | 0.00 USD | 373,740.00 USD | 431,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2183.00` | 433,960,000.00 USD | 433,960,000.00 USD | 2,960,000.00 USD | 1,140,000.00 USD | 425,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2183.70` | 715,150,000.00 USD | 715,150,000.00 USD | 1,760,000.00 USD | 1,310,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 13,780.00 USD | 13,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2185.60` | 429,440,000.00 USD | 429,440,000.00 USD | 566,020.00 USD | 1,960,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.00` | 708,140,000.00 USD | 708,140,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2188.20` | 424,220,000.00 USD | 424,220,000.00 USD | 0.00 USD | 42,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.30` | 707,530,000.00 USD | 707,530,000.00 USD | 2,730,000.00 USD | 0.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2190.80` | 424,180,000.00 USD | 424,180,000.00 USD | 0.00 USD | 222,200.00 USD | 764,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2193.40` | 423,190,000.00 USD | 423,190,000.00 USD | 605,210.00 USD | 0.00 USD | 39,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2195.00` | 41,590.00 USD | 41,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2196.00` | 422,550,000.00 USD | 422,550,000.00 USD | 416,500.00 USD | 881,070.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.90` | 700,600,000.00 USD | 700,600,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2198.60` | 419,370,000.00 USD | 419,370,000.00 USD | 0.00 USD | 2,940,000.00 USD | 50,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.20` | 695,500,000.00 USD | 695,500,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2201.20` | 416,370,000.00 USD | 416,370,000.00 USD | 1,690,000.00 USD | 1,450,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.50` | 684,230,000.00 USD | 684,230,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.80` | 411,730,000.00 USD | 411,730,000.00 USD | 2,130,000.00 USD | 314,310.00 USD | 830,450.00 USD | `Tier 1 CEX` |
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
| `Live` | `Short Liquidation` | `2225.00` | 133,410.00 USD | 175,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2226.60` | 428,420,000.00 USD | 428,420,000.00 USD | 16,350,000.00 USD | 11,030,000.00 USD | 10,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.20` | 249,870,000.00 USD | 249,870,000.00 USD | 5,120,000.00 USD | 13,730,000.00 USD | 5,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2229.80` | 225,310,000.00 USD | 225,310,000.00 USD | 10,100,000.00 USD | 7,120,000.00 USD | 4,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.90` | 390,570,000.00 USD | 390,570,000.00 USD | 12,730,000.00 USD | 11,790,000.00 USD | 28,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2232.40` | 204,000,000.00 USD | 204,000,000.00 USD | 4,620,000.00 USD | 6,200,000.00 USD | 7,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2233.20` | 337,500,000.00 USD | 337,500,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2235.00` | 185,910,000.00 USD | 185,910,000.00 USD | 19,080,000.00 USD | 85,110.00 USD | 11,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2235.00` | 3,750,000.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2236.50` | 286,180,000.00 USD | 286,180,000.00 USD | 16,050,000.00 USD | 7,430,000.00 USD | 27,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2237.60` | 155,300,000.00 USD | 155,300,000.00 USD | 23,860,000.00 USD | 7,390,000.00 USD | 12,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.80` | 234,940,000.00 USD | 234,940,000.00 USD | 16,720,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2240.20` | 111,600,000.00 USD | 111,600,000.00 USD | 1,100,000.00 USD | 1,380,000.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2242.80` | 106,890,000.00 USD | 106,890,000.00 USD | 9,030,000.00 USD | 3,760,000.00 USD | 9,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2243.10` | 197,880,000.00 USD | 197,880,000.00 USD | 29,940,000.00 USD | 5,310,000.00 USD | 24,810,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2245.00` | 3,220,000.00 USD | 7,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2245.40` | 84,870,000.00 USD | 84,870,000.00 USD | 11,210,000.00 USD | 6,190,000.00 USD | 501,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2246.40` | 137,820,000.00 USD | 137,820,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2248.00` | 66,970,000.00 USD | 66,970,000.00 USD | 12,490,000.00 USD | 1,070,000.00 USD | 7,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2249.70` | 109,560,000.00 USD | 109,560,000.00 USD | 25,030,000.00 USD | 0.00 USD | 19,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2250.60` | 46,290,000.00 USD | 46,290,000.00 USD | 4,450,000.00 USD | 4,540,000.00 USD | 5,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.00` | 65,090,000.00 USD | 65,090,000.00 USD | 26,890,000.00 USD | 0.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2253.20` | 31,680,000.00 USD | 31,680,000.00 USD | 13,840,000.00 USD | 4,440,000.00 USD | 8,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 9,380,000.00 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2255.80` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2256.30` | 26,160,000.00 USD | 26,160,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2258.40` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 170,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2259.60` | 10,940,000.00 USD | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2261.00` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 156,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 660,570.00 USD | 17,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2266.20` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2268.80` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2274.00` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 288,080.00 USD | 114,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 291,560.00 USD | 17,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2276.60` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 267,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2279.20` | 22,720,000.00 USD | 22,720,000.00 USD | 11,600,000.00 USD | 3,950,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2279.40` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 17,000,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2281.80` | 85,490,000.00 USD | 85,490,000.00 USD | 33,480,000.00 USD | 26,790,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.70` | 117,630,000.00 USD | 117,630,000.00 USD | 0.00 USD | 87,090,000.00 USD | 13,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2284.40` | 152,200,000.00 USD | 152,200,000.00 USD | 33,020,000.00 USD | 19,430,000.00 USD | 14,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 51,650.00 USD | 17,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2286.00` | 128,050,000.00 USD | 128,050,000.00 USD | 1,010,000.00 USD | 9,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2287.00` | 164,470,000.00 USD | 164,470,000.00 USD | 3,210,000.00 USD | 5,140,000.00 USD | 3,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2289.30` | 152,130,000.00 USD | 152,130,000.00 USD | 7,010,000.00 USD | 5,310,000.00 USD | 11,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2289.60` | 176,810,000.00 USD | 176,810,000.00 USD | 3,280,000.00 USD | 8,840,000.00 USD | 219,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2292.20` | 197,140,000.00 USD | 197,140,000.00 USD | 17,600,000.00 USD | 2,560,000.00 USD | 176,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2292.60` | 153,150,000.00 USD | 153,150,000.00 USD | 0.00 USD | 0.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2294.80` | 209,490,000.00 USD | 209,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 5,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 3,360,000.00 USD | 20,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2295.90` | 180,460,000.00 USD | 180,460,000.00 USD | 13,610,000.00 USD | 2,380,000.00 USD | 11,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2297.40` | 233,240,000.00 USD | 233,240,000.00 USD | 11,830,000.00 USD | 6,530,000.00 USD | 5,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.20` | 208,880,000.00 USD | 208,880,000.00 USD | 11,730,000.00 USD | 11,130,000.00 USD | 5,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2300.00` | 249,950,000.00 USD | 249,950,000.00 USD | 2,700,000.00 USD | 6,620,000.00 USD | 7,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.50` | 255,990,000.00 USD | 255,990,000.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.60` | 269,830,000.00 USD | 269,830,000.00 USD | 14,790,000.00 USD | 170,210.00 USD | 4,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 252,880.00 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.20` | 299,270,000.00 USD | 299,270,000.00 USD | 10,430,000.00 USD | 14,490,000.00 USD | 4,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.80` | 276,770,000.00 USD | 276,770,000.00 USD | 2,980,000.00 USD | 8,820,000.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2307.80` | 307,480,000.00 USD | 307,480,000.00 USD | 2,550,000.00 USD | 3,220,000.00 USD | 2,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2309.10` | 281,280,000.00 USD | 281,280,000.00 USD | 1,240,000.00 USD | 930,630.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2310.40` | 323,320,000.00 USD | 323,320,000.00 USD | 3,940,000.00 USD | 2,450,000.00 USD | 9,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2312.40` | 308,580,000.00 USD | 308,580,000.00 USD | 10,780,000.00 USD | 2,650,000.00 USD | 13,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2313.00` | 335,020,000.00 USD | 335,020,000.00 USD | 4,650,000.00 USD | 6,730,000.00 USD | 313,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 1,410,000.00 USD | 22,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2315.60` | 366,280,000.00 USD | 366,280,000.00 USD | 9,790,000.00 USD | 14,850,000.00 USD | 6,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2315.70` | 316,670,000.00 USD | 316,670,000.00 USD | 0.00 USD | 7,460,000.00 USD | 627,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2318.20` | 379,270,000.00 USD | 379,270,000.00 USD | 4,440,000.00 USD | 6,320,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.00` | 334,170,000.00 USD | 334,170,000.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 8,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.80` | 396,910,000.00 USD | 396,910,000.00 USD | 5,790,000.00 USD | 9,890,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.30` | 351,330,000.00 USD | 351,330,000.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 108,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2323.40` | 412,610,000.00 USD | 412,610,000.00 USD | 1,710,000.00 USD | 10,410,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,660,000.00 USD | 24,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.60` | 371,980,000.00 USD | 371,980,000.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2326.00` | 424,390,000.00 USD | 424,390,000.00 USD | 479,120.00 USD | 5,640,000.00 USD | 5,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2328.60` | 427,380,000.00 USD | 427,380,000.00 USD | 2,140,000.00 USD | 444,400.00 USD | 402,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.90` | 383,810,000.00 USD | 383,810,000.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2331.20` | 445,540,000.00 USD | 445,540,000.00 USD | 17,350,000.00 USD | 692,470.00 USD | 126,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2332.20` | 413,040,000.00 USD | 413,040,000.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2333.80` | 463,270,000.00 USD | 463,270,000.00 USD | 7,710,000.00 USD | 2,820,000.00 USD | 7,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 1,090,000.00 USD | 25,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2335.50` | 471,050,000.00 USD | 471,050,000.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 10,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2336.40` | 481,890,000.00 USD | 481,890,000.00 USD | 15,940,000.00 USD | 547,950.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.80` | 488,920,000.00 USD | 488,920,000.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2339.00` | 494,900,000.00 USD | 494,900,000.00 USD | 6,360,000.00 USD | 2,600,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2341.60` | 513,570,000.00 USD | 513,570,000.00 USD | 5,340,000.00 USD | 3,430,000.00 USD | 9,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2342.10` | 529,020,000.00 USD | 529,020,000.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2344.20` | 526,900,000.00 USD | 526,900,000.00 USD | 1,370,000.00 USD | 6,240,000.00 USD | 5,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 230,280.00 USD | 25,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2345.40` | 550,400,000.00 USD | 550,400,000.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2346.80` | 540,470,000.00 USD | 540,470,000.00 USD | 3,930,000.00 USD | 3,010,000.00 USD | 6,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.70` | 588,270,000.00 USD | 588,270,000.00 USD | 847,620.00 USD | 9,500,000.00 USD | 27,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2349.40` | 571,320,000.00 USD | 571,320,000.00 USD | 19,450,000.00 USD | 5,980,000.00 USD | 5,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2352.00` | 598,840,000.00 USD | 598,840,000.00 USD | 18,420,000.00 USD | 2,080,000.00 USD | 7,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2352.00` | 624,900,000.00 USD | 624,900,000.00 USD | 2,930,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2354.60` | 622,470,000.00 USD | 622,470,000.00 USD | 973,980.00 USD | 20,450,000.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,670,000.00 USD | 27,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2355.30` | 684,440,000.00 USD | 684,440,000.00 USD | 18,530,000.00 USD | 38,020,000.00 USD | 3,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.20` | 632,150,000.00 USD | 632,150,000.00 USD | 4,390,000.00 USD | 1,740,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.60` | 696,580,000.00 USD | 696,580,000.00 USD | 7,110,000.00 USD | 512,220.00 USD | 4,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2359.80` | 653,040,000.00 USD | 653,040,000.00 USD | 8,920,000.00 USD | 6,950,000.00 USD | 5,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.90` | 703,960,000.00 USD | 703,960,000.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 431,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.40` | 673,590,000.00 USD | 673,590,000.00 USD | 8,900,000.00 USD | 6,710,000.00 USD | 4,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2365.00` | 690,810,000.00 USD | 690,810,000.00 USD | 6,420,000.00 USD | 4,850,000.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 4,000,000.00 USD | 31,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2365.20` | 725,010,000.00 USD | 725,010,000.00 USD | 10,200,000.00 USD | 0.00 USD | 10,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.60` | 699,590,000.00 USD | 699,590,000.00 USD | 4,770,000.00 USD | 1,110,000.00 USD | 2,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.50` | 738,080,000.00 USD | 738,080,000.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 458,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.20` | 735,010,000.00 USD | 735,010,000.00 USD | 14,350,000.00 USD | 12,620,000.00 USD | 8,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.80` | 819,020,000.00 USD | 819,020,000.00 USD | 26,000,000.00 USD | 0.00 USD | 54,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.80` | 761,980,000.00 USD | 761,980,000.00 USD | 14,450,000.00 USD | 5,460,000.00 USD | 7,060,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 1,590,000.00 USD | 32,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2375.10` | 845,960,000.00 USD | 845,960,000.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2375.40` | 780,580,000.00 USD | 780,580,000.00 USD | 11,510,000.00 USD | 3,420,000.00 USD | 3,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.00` | 803,100,000.00 USD | 803,100,000.00 USD | 5,030,000.00 USD | 6,270,000.00 USD | 11,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.40` | 891,380,000.00 USD | 891,380,000.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.60` | 840,470,000.00 USD | 840,470,000.00 USD | 11,320,000.00 USD | 11,190,000.00 USD | 14,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.70` | 931,170,000.00 USD | 931,170,000.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 24,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.20` | 886,340,000.00 USD | 886,340,000.00 USD | 20,060,000.00 USD | 12,500,000.00 USD | 13,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2385.00` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 5,690,000.00 USD | 38,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.80` | 910,150,000.00 USD | 910,150,000.00 USD | 8,950,000.00 USD | 10,960,000.00 USD | 3,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.30` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2388.40` | 935,260,000.00 USD | 935,260,000.00 USD | 13,100,000.00 USD | 6,720,000.00 USD | 5,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2391.00` | 950,870,000.00 USD | 950,870,000.00 USD | 3,770,000.00 USD | 6,670,000.00 USD | 5,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2393.60` | 965,250,000.00 USD | 965,250,000.00 USD | 4,380,000.00 USD | 6,000,000.00 USD | 4,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.90` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 5,040,000.00 USD | 43,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2396.20` | 979,190,000.00 USD | 979,190,000.00 USD | 5,350,000.00 USD | 4,020,000.00 USD | 4,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2398.20` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.80` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 8,890,000.00 USD | 6,800,000.00 USD | 7,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2401.40` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 4,600,000.00 USD | 6,190,000.00 USD | 6,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.50` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2404.00` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 9,470,000.00 USD | 8,980,000.00 USD | 7,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.80` | 1,670,000,000.00 USD | 1,670,000,000.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 207,600.00 USD | 43,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2406.60` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 11,990,000.00 USD | 7,780,000.00 USD | 5,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2408.10` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2409.20` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 8,220,000.00 USD | 6,130,000.00 USD | 6,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.40` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2411.80` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 8,840,000.00 USD | 7,170,000.00 USD | 3,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2414.40` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 2,970,000.00 USD | 2,340,000.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.70` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 23,820,000.00 USD | 21,740,000.00 USD | 23,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 159,090.00 USD | 43,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2417.00` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 3,600,000.00 USD | 2,550,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.00` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2419.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 6,520,000.00 USD | 3,840,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.30` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 25,700,000.00 USD | 27,770,000.00 USD | 21,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.20` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 2,930,000.00 USD | 3,700,000.00 USD | 5,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.60` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 23,650,000.00 USD | 31,040,000.00 USD | 34,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2424.80` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 1,500,000.00 USD | 2,700,000.00 USD | 844,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 1,600,000.00 USD | 45,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2427.40` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 634,700.00 USD | 89,750.00 USD | 601,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.90` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 25,200,000.00 USD | 15,090,000.00 USD | 18,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.00` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,550,000.00 USD | 1,770,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.20` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 10,380,000.00 USD | 17,060,000.00 USD | 9,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 2,090,000.00 USD | 1,690,000.00 USD | 247,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.50` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 207,040.00 USD | 45,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.20` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,790,000.00 USD | 495,600.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2437.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 777,840.00 USD | 517,090.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.80` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 11,900,000.00 USD | 12,720,000.00 USD | 5,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 1,540,000.00 USD | 2,030,000.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.10` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2443.00` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 1,050,000.00 USD | 644,860.00 USD | 859,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.40` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 8,860,000.00 USD | 15,100,000.00 USD | 13,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 334,460.00 USD | 46,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 126,820.00 USD | 467,480.00 USD | 799,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.70` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 11,380,000.00 USD | 6,510,000.00 USD | 17,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2448.20` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 864,380.00 USD | 325,700.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.80` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 2,340,000.00 USD | 871,330.00 USD | 3,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.00` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 16,710,000.00 USD | 12,450,000.00 USD | 12,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2453.40` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 4,320,000.00 USD | 3,900,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2454.30` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 4,620,000.00 USD | 4,930,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 223,610.00 USD | 46,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2456.00` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 793,240.00 USD | 1,840,000.00 USD | 797,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.60` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2458.60` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 1,400,000.00 USD | 1,230,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.90` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2461.20` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 470,530.00 USD | 46,520.00 USD | 366,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2463.80` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 619,960.00 USD | 829,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.20` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 11,960,000.00 USD | 58,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2466.40` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.50` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2469.00` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 1,250,000.00 USD | 391,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.80` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.10` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 615,790.00 USD | 58,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2476.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.40` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2479.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 26,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.70` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2482.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 525,130.00 USD | 136,500.00 USD | 451,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.00` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2484.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 925,970.00 USD | 1,330,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 36,830.00 USD | 58,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2487.20` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2487.30` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2489.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 317,820.00 USD | 30,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.60` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 239,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2492.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 547,850.00 USD | 44,470.00 USD | 357,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.90` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 1,610,000.00 USD | 1,760,000.00 USD | 3,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2495.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 626,840.00 USD | 134,080.00 USD | 33,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 118,030.00 USD | 58,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.20` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 2,860,000.00 USD | 4,270,000.00 USD | 6,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2497.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2500.20` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.50` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 1,110,000.00 USD | 1,450,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2502.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.80` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 63,860.00 USD | 1,480,000.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 55,380,000.00 USD | 114,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2505.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2507.10` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2510.40` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2510.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2513.20` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.70` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 6,510,000.00 USD | 120,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2515.80` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2517.00` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2520.30` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2521.00` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 80,610.00 USD | 121,470.00 USD | 88,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2523.60` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 563,140.00 USD | 494,150.00 USD | 532,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.60` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 18,050,000.00 USD | 138,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2526.20` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 754,970.00 USD | 304,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2526.90` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.20` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.50` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 889,170.00 USD | 139,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2536.80` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2540.10` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2543.40` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 193,650.00 USD | 140,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2546.70` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.00` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.30` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 834,430.00 USD | 140,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2556.60` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.90` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2563.20` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 1,840,000.00 USD | 142,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2566.50` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.80` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2573.10` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 552,900.00 USD | 143,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2576.40` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2579.70` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2583.00` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,530,000.00 USD | 169,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.30` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.60` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.90` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 8,140,000.00 USD | 177,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2596.20` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2599.50` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2602.80` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 339,670.00 USD | 178,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.10` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.40` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.70` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 226,630.00 USD | 178,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2616.00` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2619.30` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2622.60` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2625.00` | 32,790,000.00 USD | 211,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2625.90` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2629.20` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 0.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2632.40` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2635.00` | 1,600,000.00 USD | 212,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 639,970.00 USD | 213,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 26,060,000.00 USD | 239,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 438,080.00 USD | 240,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 4,490,000.00 USD | 244,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 59,830.00 USD | 244,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 6,390,000.00 USD | 250,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 6,470,000.00 USD | 257,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 4,640.00 USD | 257,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 13,010,000.00 USD | 270,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 238,930.00 USD | 270,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 5,900,000.00 USD | 276,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 1,380,000.00 USD | 277,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 4,430,000.00 USD | 282,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 355,030.00 USD | 282,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 1,920,000.00 USD | 284,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 15,060,000.00 USD | 299,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 3,790,000.00 USD | 303,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 1,160,000.00 USD | 304,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 224,370.00 USD | 304,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 7,760,000.00 USD | 312,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 139,770.00 USD | 312,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 402,980.00 USD | 313,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 846,340.00 USD | 314,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 130,270.00 USD | 314,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 2,010,000.00 USD | 316,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 306,810.00 USD | 316,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 286,270.00 USD | 316,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 2,320,000.00 USD | 319,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 1,190,000.00 USD | 320,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 145,500.00 USD | 320,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 394,070.00 USD | 320,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 3,380,000.00 USD | 324,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 27,970,000.00 USD | 352,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 115,120.00 USD | 352,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 379,670.00 USD | 352,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 1,010,000.00 USD | 353,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 1,740,000.00 USD | 355,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 320,320.00 USD | 355,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 6,270,000.00 USD | 362,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 33,550,000.00 USD | 395,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 648,220.00 USD | 396,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 1,500,000.00 USD | 397,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 19,360.00 USD | 397,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 153,180.00 USD | 397,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 28,800,000.00 USD | 426,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 464,560.00 USD | 427,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 8,330,000.00 USD | 435,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 4,510,000.00 USD | 440,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 718,050.00 USD | 440,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 1,900,000.00 USD | 442,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 157,660.00 USD | 442,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 1,020,000.00 USD | 443,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 1,800,000.00 USD | 445,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 3,880,000.00 USD | 449,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 1,490,000.00 USD | 450,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 16,370,000.00 USD | 467,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 389,500.00 USD | 467,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 5,020,000.00 USD | 472,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 31,890.00 USD | 472,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 18,130,000.00 USD | 490,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 586,260.00 USD | 491,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 35,060.00 USD | 491,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 135,990.00 USD | 491,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 8,680,000.00 USD | 500,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 107,110.00 USD | 500,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 319,520.00 USD | 500,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 1,190,000.00 USD | 501,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 710,580.00 USD | 502,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 1,720,000.00 USD | 504,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 107,510.00 USD | 504,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 75,350.00 USD | 504,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 384,020.00 USD | 504,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 445,620.00 USD | 505,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 38,140.00 USD | 505,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 115,930.00 USD | 505,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 899,730.00 USD | 506,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 202,720.00 USD | 506,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 16,170.00 USD | 506,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 14,710,000.00 USD | 521,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 984,440.00 USD | 522,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 4,220,000.00 USD | 526,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 373,990.00 USD | 526,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 62,090,000.00 USD | 589,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 276,220.00 USD | 589,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 186,940.00 USD | 589,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 1,090,000.00 USD | 590,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 586,670.00 USD | 591,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 2,770,000.00 USD | 593,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 342,840.00 USD | 594,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 323,920.00 USD | 594,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 1,190,000.00 USD | 595,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 265,280.00 USD | 596,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 1,950,000.00 USD | 598,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 79,950.00 USD | 598,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 758,690.00 USD | 598,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 469,720.00 USD | 599,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 4,520.00 USD | 599,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 12,280,000.00 USD | 611,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 469,000.00 USD | 612,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 178,520.00 USD | 612,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 2,700,000.00 USD | 614,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 32,260,000.00 USD | 647,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 1,350,000.00 USD | 648,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 194,720.00 USD | 648,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 366,020.00 USD | 649,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 6,550,000.00 USD | 655,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 270,770.00 USD | 655,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 20,630.00 USD | 655,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 308,960.00 USD | 656,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 398,880.00 USD | 656,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 840,530.00 USD | 657,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 15,110,000.00 USD | 672,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 99,760.00 USD | 672,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 310,260.00 USD | 673,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 2,580,000.00 USD | 675,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 200,410.00 USD | 675,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 2,420,000.00 USD | 678,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 42,930.00 USD | 678,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 91,090.00 USD | 678,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 282,790.00 USD | 678,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 189,850.00 USD | 678,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 363,360.00 USD | 679,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 1,260,000.00 USD | 680,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3875.00` | 1,150,000.00 USD | 681,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 1,470,000.00 USD | 683,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 25,030.00 USD | 683,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 490,460.00 USD | 683,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 75,750.00 USD | 683,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 636,770.00 USD | 684,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 521,140.00 USD | 684,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 6,330.00 USD | 684,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 618.17 USD | 684,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 24,530.00 USD | 684,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 38,970,000.00 USD | 723,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 321,680.00 USD | 724,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 64,980,000.00 USD | 789,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 609,150.00 USD | 789,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 42,810.00 USD | 789,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 315,140.00 USD | 790,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 56,910.00 USD | 790,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 2,150,000.00 USD | 792,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 63,060.00 USD | 792,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 3,080,000.00 USD | 795,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 433,770,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 16,500.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 528,780.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 108,450.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 1,990,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 299,080.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 63,620.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 2,190,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 166,330.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 141,870.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 2,780.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 828,320.00 USD | 1,240,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 4,440,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 1,890,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 92,620,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4225.00` | 1,380,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 115,220.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 29,030,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 420.39 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 54,480.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 301.39 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 223,960.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 19,590.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 13,080.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 6,660.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 1,610,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 15,410.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 197,540.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 670,800.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 505.31 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 104,290.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `445.00` | 787,780,000.00 USD | 0.00 USD | 15,690.00 USD | `-79.72%` | `35.26` |
| `Live` | `Long` | `455.00` | 787,760,000.00 USD | 0.00 USD | 61,760.00 USD | `-79.26%` | `135.74` |
| `Live` | `Long` | `465.00` | 787,700,000.00 USD | 0.00 USD | 58,550.00 USD | `-78.80%` | `125.91` |
| `Live` | `Long` | `475.00` | 787,640,000.00 USD | 0.00 USD | 815.76 USD | `-78.35%` | `1.72` |
| `Live` | `Long` | `485.00` | 787,640,000.00 USD | 0.00 USD | 38,240.00 USD | `-77.89%` | `78.84` |
| `Live` | `Long` | `495.00` | 787,600,000.00 USD | 0.00 USD | 4,280.00 USD | `-77.44%` | `8.65` |
| `Live` | `Long` | `505.00` | 787,600,000.00 USD | 0.00 USD | 121,420.00 USD | `-76.98%` | `240.44` |
| `Live` | `Long` | `515.00` | 787,480,000.00 USD | 0.00 USD | 48,930.00 USD | `-76.53%` | `95.01` |
| `Live` | `Long` | `525.00` | 787,430,000.00 USD | 0.00 USD | 216,050.00 USD | `-76.07%` | `411.53` |
| `Live` | `Long` | `535.00` | 787,210,000.00 USD | 0.00 USD | 9,430.00 USD | `-75.61%` | `17.62` |
| `Live` | `Long` | `545.00` | 787,200,000.00 USD | 0.00 USD | 15,440.00 USD | `-75.16%` | `28.34` |
| `Live` | `Long` | `555.00` | 787,190,000.00 USD | 0.00 USD | 4,060.00 USD | `-74.70%` | `7.32` |
| `Live` | `Long` | `565.00` | 787,180,000.00 USD | 0.00 USD | 202,350.00 USD | `-74.25%` | `358.15` |
| `Live` | `Long` | `575.00` | 786,980,000.00 USD | 0.00 USD | 1,440.00 USD | `-73.79%` | `2.50` |
| `Live` | `Long` | `585.00` | 786,980,000.00 USD | 0.00 USD | 140,000.00 USD | `-73.33%` | `239.31` |
| `Live` | `Long` | `595.00` | 786,840,000.00 USD | 0.00 USD | 55,430.00 USD | `-72.88%` | `93.15` |
| `Live` | `Long` | `605.00` | 786,780,000.00 USD | 0.00 USD | 34,800.00 USD | `-72.42%` | `57.52` |
| `Live` | `Long` | `615.00` | 786,750,000.00 USD | 0.00 USD | 421,220.00 USD | `-71.97%` | `684.92` |
| `Live` | `Long` | `625.00` | 786,330,000.00 USD | 0.00 USD | 2,610,000.00 USD | `-71.51%` | `4,175.73` |
| `Live` | `Long` | `635.00` | 783,720,000.00 USD | 0.00 USD | 34,490.00 USD | `-71.06%` | `54.31` |
| `Live` | `Long` | `645.00` | 783,680,000.00 USD | 0.00 USD | 51,980.00 USD | `-70.60%` | `80.58` |
| `Live` | `Long` | `655.00` | 783,630,000.00 USD | 0.00 USD | 41,250.00 USD | `-70.14%` | `62.98` |
| `Live` | `Long` | `665.00` | 783,590,000.00 USD | 0.00 USD | 30,030.00 USD | `-69.69%` | `45.16` |
| `Live` | `Long` | `675.00` | 783,560,000.00 USD | 0.00 USD | 9,430.00 USD | `-69.23%` | `13.97` |
| `Live` | `Long` | `685.00` | 783,550,000.00 USD | 0.00 USD | 112,430.00 USD | `-68.78%` | `164.13` |
| `Live` | `Long` | `695.00` | 783,440,000.00 USD | 0.00 USD | 93,960.00 USD | `-68.32%` | `135.20` |
| `Live` | `Long` | `705.00` | 783,340,000.00 USD | 0.00 USD | 5,510.00 USD | `-67.87%` | `7.81` |
| `Live` | `Long` | `715.00` | 783,340,000.00 USD | 0.00 USD | 90,680.00 USD | `-67.41%` | `126.83` |
| `Live` | `Long` | `725.00` | 783,250,000.00 USD | 0.00 USD | 583,860.00 USD | `-66.95%` | `805.32` |
| `Live` | `Long` | `735.00` | 782,660,000.00 USD | 0.00 USD | 1,270,000.00 USD | `-66.50%` | `1,725.21` |
| `Live` | `Long` | `745.00` | 781,390,000.00 USD | 0.00 USD | 63,950.00 USD | `-66.04%` | `85.84` |
| `Live` | `Long` | `755.00` | 781,330,000.00 USD | 0.00 USD | 51,360.00 USD | `-65.59%` | `68.03` |
| `Live` | `Long` | `765.00` | 781,280,000.00 USD | 0.00 USD | 31,470.00 USD | `-65.13%` | `41.13` |
| `Live` | `Long` | `775.00` | 781,250,000.00 USD | 0.00 USD | 9,500.00 USD | `-64.67%` | `12.26` |
| `Live` | `Long` | `785.00` | 781,240,000.00 USD | 0.00 USD | 23,830.00 USD | `-64.22%` | `30.36` |
| `Live` | `Long` | `795.00` | 781,210,000.00 USD | 0.00 USD | 1,110.00 USD | `-63.76%` | `1.39` |
| `Live` | `Long` | `805.00` | 781,210,000.00 USD | 0.00 USD | 57,090.00 USD | `-63.31%` | `70.92` |
| `Live` | `Long` | `815.00` | 781,160,000.00 USD | 0.00 USD | 64,600.00 USD | `-62.85%` | `79.26` |
| `Live` | `Long` | `825.00` | 781,090,000.00 USD | 0.00 USD | 486,190.00 USD | `-62.40%` | `589.32` |
| `Live` | `Long` | `835.00` | 780,610,000.00 USD | 0.00 USD | 8,660.00 USD | `-61.94%` | `10.37` |
| `Live` | `Long` | `845.00` | 780,600,000.00 USD | 0.00 USD | 2,550,000.00 USD | `-61.48%` | `3,013.79` |
| `Live` | `Long` | `855.00` | 778,050,000.00 USD | 0.00 USD | 175,900.00 USD | `-61.03%` | `205.73` |
| `Live` | `Long` | `865.00` | 777,870,000.00 USD | 0.00 USD | 40,320.00 USD | `-60.57%` | `46.62` |
| `Live` | `Long` | `875.00` | 777,830,000.00 USD | 0.00 USD | 6,570,000.00 USD | `-60.12%` | `7,512.08` |
| `Live` | `Long` | `885.00` | 771,260,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-59.66%` | `1,192.51` |
| `Live` | `Long` | `895.00` | 770,210,000.00 USD | 0.00 USD | 25,390.00 USD | `-59.20%` | `28.37` |
| `Live` | `Long` | `905.00` | 770,180,000.00 USD | 0.00 USD | 346,270.00 USD | `-58.75%` | `382.62` |
| `Live` | `Long` | `915.00` | 769,830,000.00 USD | 0.00 USD | 399,470.00 USD | `-58.29%` | `436.58` |
| `Live` | `Long` | `925.00` | 769,430,000.00 USD | 0.00 USD | 199,740.00 USD | `-57.84%` | `215.94` |
| `Live` | `Long` | `935.00` | 769,230,000.00 USD | 0.00 USD | 189,000.00 USD | `-57.38%` | `202.13` |
| `Live` | `Long` | `945.00` | 769,050,000.00 USD | 0.00 USD | 172,210.00 USD | `-56.93%` | `182.23` |
| `Live` | `Long` | `955.00` | 768,870,000.00 USD | 0.00 USD | 152,260.00 USD | `-56.47%` | `159.43` |
| `Live` | `Long` | `965.00` | 768,720,000.00 USD | 0.00 USD | 70,060.00 USD | `-56.01%` | `72.60` |
| `Live` | `Long` | `975.00` | 768,650,000.00 USD | 0.00 USD | 231,240.00 USD | `-55.56%` | `237.16` |
| `Live` | `Long` | `985.00` | 768,420,000.00 USD | 0.00 USD | 492,680.00 USD | `-55.10%` | `500.18` |
| `Live` | `Long` | `995.00` | 767,930,000.00 USD | 0.00 USD | 305,430.00 USD | `-54.65%` | `306.96` |
| `Live` | `Long` | `1005.00` | 767,620,000.00 USD | 0.00 USD | 5,690,000.00 USD | `-54.19%` | `5,665.20` |
| `Live` | `Long` | `1015.00` | 761,930,000.00 USD | 0.00 USD | 226,700.00 USD | `-53.73%` | `223.35` |
| `Live` | `Long` | `1025.00` | 761,700,000.00 USD | 0.00 USD | 445,280.00 USD | `-53.28%` | `434.42` |
| `Live` | `Long` | `1035.00` | 761,260,000.00 USD | 0.00 USD | 38,930.00 USD | `-52.82%` | `37.61` |
| `Live` | `Long` | `1045.00` | 761,220,000.00 USD | 0.00 USD | 624,800.00 USD | `-52.37%` | `597.89` |
| `Live` | `Long` | `1055.00` | 760,590,000.00 USD | 0.00 USD | 270,220.00 USD | `-51.91%` | `256.14` |
| `Live` | `Long` | `1065.00` | 760,320,000.00 USD | 0.00 USD | 702,800.00 USD | `-51.46%` | `659.91` |
| `Live` | `Long` | `1075.00` | 759,620,000.00 USD | 0.00 USD | 8,300,000.00 USD | `-51.00%` | `7,719.89` |
| `Live` | `Long` | `1085.00` | 751,320,000.00 USD | 0.00 USD | 50,300.00 USD | `-50.54%` | `46.36` |
| `Live` | `Long` | `1095.00` | 751,270,000.00 USD | 0.00 USD | 24,580.00 USD | `-50.09%` | `22.45` |
| `Live` | `Long` | `1105.00` | 751,250,000.00 USD | 0.00 USD | 1,890,000.00 USD | `-49.63%` | `1,712.91` |
| `Live` | `Long` | `1115.00` | 749,350,000.00 USD | 0.00 USD | 91,900.00 USD | `-49.18%` | `82.42` |
| `Live` | `Long` | `1125.00` | 749,260,000.00 USD | 0.00 USD | 710,890.00 USD | `-48.72%` | `631.90` |
| `Live` | `Long` | `1135.00` | 748,550,000.00 USD | 0.00 USD | 154,300.00 USD | `-48.27%` | `135.95` |
| `Live` | `Long` | `1145.00` | 748,400,000.00 USD | 0.00 USD | 185,980.00 USD | `-47.81%` | `162.43` |
| `Live` | `Long` | `1155.00` | 748,210,000.00 USD | 0.00 USD | 8,540,000.00 USD | `-47.35%` | `7,393.45` |
| `Live` | `Long` | `1165.00` | 739,670,000.00 USD | 0.00 USD | 29,690.00 USD | `-46.90%` | `25.48` |
| `Live` | `Long` | `1175.00` | 739,640,000.00 USD | 0.00 USD | 98,410.00 USD | `-46.44%` | `83.75` |
| `Live` | `Long` | `1185.00` | 739,540,000.00 USD | 0.00 USD | 152,890.00 USD | `-45.99%` | `129.02` |
| `Live` | `Long` | `1195.00` | 739,390,000.00 USD | 0.00 USD | 344,340.00 USD | `-45.53%` | `288.15` |
| `Live` | `Long` | `1205.00` | 739,050,000.00 USD | 0.00 USD | 1,340,000.00 USD | `-45.07%` | `1,113.52` |
| `Live` | `Long` | `1215.00` | 737,700,000.00 USD | 0.00 USD | 110,070.00 USD | `-44.62%` | `90.59` |
| `Live` | `Long` | `1225.00` | 737,590,000.00 USD | 0.00 USD | 249,600.00 USD | `-44.16%` | `203.76` |
| `Live` | `Long` | `1235.00` | 737,340,000.00 USD | 0.00 USD | 318,870.00 USD | `-43.71%` | `258.19` |
| `Live` | `Long` | `1245.00` | 737,020,000.00 USD | 0.00 USD | 43,050.00 USD | `-43.25%` | `34.58` |
| `Live` | `Long` | `1255.00` | 736,980,000.00 USD | 0.00 USD | 561,480.00 USD | `-42.80%` | `447.40` |
| `Live` | `Long` | `1265.00` | 736,420,000.00 USD | 0.00 USD | 4,270,000.00 USD | `-42.34%` | `3,376.06` |
| `Live` | `Long` | `1275.00` | 732,150,000.00 USD | 0.00 USD | 15,390,000.00 USD | `-41.88%` | `12,071.02` |
| `Live` | `Long` | `1285.00` | 716,760,000.00 USD | 0.00 USD | 3,590,000.00 USD | `-41.43%` | `2,796.51` |
| `Live` | `Long` | `1295.00` | 713,170,000.00 USD | 0.00 USD | 356,990.00 USD | `-40.97%` | `275.67` |
| `Live` | `Long` | `1305.00` | 712,810,000.00 USD | 0.00 USD | 634,790.00 USD | `-40.52%` | `486.43` |
| `Live` | `Long` | `1315.00` | 712,170,000.00 USD | 0.00 USD | 171,480.00 USD | `-40.06%` | `130.40` |
| `Live` | `Long` | `1325.00` | 712,000,000.00 USD | 0.00 USD | 1,390,000.00 USD | `-39.60%` | `1,049.02` |
| `Live` | `Long` | `1335.00` | 710,610,000.00 USD | 0.00 USD | 340,530.00 USD | `-39.15%` | `255.08` |
| `Live` | `Long` | `1345.00` | 710,270,000.00 USD | 0.00 USD | 219,560.00 USD | `-38.69%` | `163.24` |
| `Live` | `Long` | `1355.00` | 710,050,000.00 USD | 0.00 USD | 218,570.00 USD | `-38.24%` | `161.31` |
| `Live` | `Long` | `1365.00` | 709,830,000.00 USD | 0.00 USD | 3,480,000.00 USD | `-37.78%` | `2,552.96` |
| `Live` | `Long` | `1375.00` | 706,350,000.00 USD | 0.00 USD | 342,230.00 USD | `-37.33%` | `248.90` |
| `Live` | `Long` | `1385.00` | 706,010,000.00 USD | 0.00 USD | 5,870,000.00 USD | `-36.87%` | `4,237.17` |
| `Live` | `Long` | `1395.00` | 700,140,000.00 USD | 0.00 USD | 2,080,000.00 USD | `-36.41%` | `1,488.47` |
| `Live` | `Long` | `1405.00` | 698,060,000.00 USD | 0.00 USD | 16,920,000.00 USD | `-35.96%` | `12,043.32` |
| `Live` | `Long` | `1415.00` | 681,140,000.00 USD | 0.00 USD | 161,500.00 USD | `-35.50%` | `114.14` |
| `Live` | `Long` | `1425.00` | 680,980,000.00 USD | 0.00 USD | 446,770.00 USD | `-35.05%` | `313.52` |
| `Live` | `Long` | `1435.00` | 680,530,000.00 USD | 0.00 USD | 1,200,000.00 USD | `-34.59%` | `839.20` |
| `Live` | `Long` | `1445.00` | 679,330,000.00 USD | 0.00 USD | 275,040.00 USD | `-34.13%` | `190.34` |
| `Live` | `Long` | `1455.00` | 679,050,000.00 USD | 0.00 USD | 124,030.00 USD | `-33.68%` | `85.25` |
| `Live` | `Long` | `1465.00` | 678,930,000.00 USD | 0.00 USD | 5,240,000.00 USD | `-33.22%` | `3,577.47` |
| `Live` | `Long` | `1475.00` | 673,690,000.00 USD | 0.00 USD | 1,600,000.00 USD | `-32.77%` | `1,088.03` |
| `Live` | `Long` | `1485.00` | 672,080,000.00 USD | 0.00 USD | 297,900.00 USD | `-32.31%` | `200.61` |
| `Live` | `Long` | `1495.00` | 671,790,000.00 USD | 0.00 USD | 316,410.00 USD | `-31.86%` | `211.65` |
| `Live` | `Long` | `1505.00` | 671,470,000.00 USD | 0.00 USD | 40,070,000.00 USD | `-31.40%` | `26,621.97` |
| `Live` | `Long` | `1515.00` | 631,400,000.00 USD | 0.00 USD | 465,650.00 USD | `-30.94%` | `307.36` |
| `Live` | `Long` | `1525.00` | 630,940,000.00 USD | 0.00 USD | 18,830,000.00 USD | `-30.49%` | `12,349.12` |
| `Live` | `Long` | `1535.00` | 612,100,000.00 USD | 0.00 USD | 1,620,000.00 USD | `-30.03%` | `1,057.29` |
| `Live` | `Long` | `1545.00` | 610,480,000.00 USD | 0.00 USD | 12,780,000.00 USD | `-29.58%` | `8,271.65` |
| `Live` | `Long` | `1555.00` | 597,700,000.00 USD | 0.00 USD | 791,900.00 USD | `-29.12%` | `509.26` |
| `Live` | `Long` | `1565.00` | 596,910,000.00 USD | 0.00 USD | 7,320,000.00 USD | `-28.67%` | `4,674.95` |
| `Live` | `Long` | `1575.00` | 589,590,000.00 USD | 0.00 USD | 3,220,000.00 USD | `-28.21%` | `2,041.49` |
| `Live` | `Long` | `1585.00` | 586,380,000.00 USD | 0.00 USD | 858,690.00 USD | `-27.75%` | `541.76` |
| `Live` | `Long` | `1595.00` | 585,520,000.00 USD | 0.00 USD | 17,770,000.00 USD | `-27.30%` | `11,142.93` |
| `Live` | `Long` | `1605.00` | 567,750,000.00 USD | 0.00 USD | 18,280,000.00 USD | `-26.84%` | `11,392.18` |
| `Live` | `Long` | `1615.00` | 549,460,000.00 USD | 0.00 USD | 417,190.00 USD | `-26.39%` | `258.32` |
| `Live` | `Long` | `1625.00` | 549,050,000.00 USD | 0.00 USD | 229,350.00 USD | `-25.93%` | `141.14` |
| `Live` | `Long` | `1635.00` | 548,820,000.00 USD | 0.00 USD | 18,510,000.00 USD | `-25.47%` | `11,322.28` |
| `Live` | `Long` | `1645.00` | 530,300,000.00 USD | 0.00 USD | 36,690,000.00 USD | `-25.02%` | `22,304.44` |
| `Live` | `Long` | `1655.00` | 493,610,000.00 USD | 0.00 USD | 17,680,000.00 USD | `-24.56%` | `10,683.23` |
| `Live` | `Long` | `1665.00` | 475,930,000.00 USD | 0.00 USD | 1,300,000.00 USD | `-24.11%` | `780.74` |
| `Live` | `Long` | `1675.00` | 474,630,000.00 USD | 0.00 USD | 14,490,000.00 USD | `-23.65%` | `8,651.28` |
| `Live` | `Long` | `1685.00` | 460,140,000.00 USD | 0.00 USD | 834,950.00 USD | `-23.20%` | `495.52` |
| `Live` | `Long` | `1695.00` | 459,310,000.00 USD | 0.00 USD | 750,540.00 USD | `-22.74%` | `442.80` |
| `Live` | `Long` | `1705.00` | 458,560,000.00 USD | 0.00 USD | 612,790.00 USD | `-22.28%` | `359.41` |
| `Live` | `Long` | `1715.00` | 457,940,000.00 USD | 0.00 USD | 17,740,000.00 USD | `-21.83%` | `10,344.35` |
| `Live` | `Long` | `1725.00` | 440,200,000.00 USD | 0.00 USD | 18,490,000.00 USD | `-21.37%` | `10,719.82` |
| `Live` | `Long` | `1735.00` | 421,710,000.00 USD | 0.00 USD | 812,780.00 USD | `-20.92%` | `468.46` |
| `Live` | `Long` | `1745.00` | 420,900,000.00 USD | 0.00 USD | 1,460,000.00 USD | `-20.46%` | `836.09` |
| `Live` | `Long` | `1755.00` | 419,440,000.00 USD | 0.00 USD | 1,190,000.00 USD | `-20.00%` | `680.33` |
| `Live` | `Long` | `1765.00` | 418,250,000.00 USD | 0.00 USD | 844,050.00 USD | `-19.55%` | `478.21` |
| `Live` | `Long` | `1775.00` | 417,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | `-19.09%` | `790.66` |
| `Live` | `Long` | `1785.00` | 416,000,000.00 USD | 0.00 USD | 55,030,000.00 USD | `-18.64%` | `30,831.20` |
| `Live` | `Long` | `1795.00` | 360,960,000.00 USD | 0.00 USD | 531,540.00 USD | `-18.18%` | `296.12` |
| `Live` | `Long` | `1805.00` | 360,430,000.00 USD | 0.00 USD | 1,380,000.00 USD | `-17.73%` | `763.45` |
| `Live` | `Long` | `1815.00` | 359,050,000.00 USD | 0.00 USD | 671,350.00 USD | `-17.27%` | `369.89` |
| `Live` | `Long` | `1825.00` | 358,380,000.00 USD | 0.00 USD | 32,790,000.00 USD | `-16.81%` | `17,966.75` |
| `Live` | `Long` | `1835.00` | 325,590,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-16.36%` | `608.20` |
| `Live` | `Long` | `1845.00` | 324,480,000.00 USD | 0.00 USD | 15,590,000.00 USD | `-15.90%` | `8,449.44` |
| `Live` | `Long` | `1855.00` | 308,890,000.00 USD | 0.00 USD | 3,510,000.00 USD | `-15.45%` | `1,892.53` |
| `Live` | `Long` | `1865.00` | 305,380,000.00 USD | 0.00 USD | 7,810,000.00 USD | `-14.99%` | `4,187.16` |
| `Live` | `Long` | `1875.00` | 297,570,000.00 USD | 0.00 USD | 7,250,000.00 USD | `-14.53%` | `3,867.02` |
| `Live` | `Long` | `1885.00` | 290,320,000.00 USD | 0.00 USD | 6,920,000.00 USD | `-14.08%` | `3,671.37` |
| `Live` | `Long` | `1895.00` | 283,400,000.00 USD | 0.00 USD | 849,020.00 USD | `-13.62%` | `448.03` |
| `Live` | `Long` | `1905.00` | 282,550,000.00 USD | 0.00 USD | 13,180,000.00 USD | `-13.17%` | `6,921.17` |
| `Live` | `Long` | `1915.00` | 269,360,000.00 USD | 0.00 USD | 18,510,000.00 USD | `-12.71%` | `9,666.16` |
| `Live` | `Long` | `1925.00` | 250,850,000.00 USD | 0.00 USD | 14,870,000.00 USD | `-12.26%` | `7,725.90` |
| `Live` | `Long` | `1935.00` | 235,980,000.00 USD | 0.00 USD | 18,190,000.00 USD | `-11.80%` | `9,399.17` |
| `Live` | `Long` | `1945.00` | 217,790,000.00 USD | 0.00 USD | 2,290,000.00 USD | `-11.34%` | `1,175.32` |
| `Live` | `Long` | `1955.00` | 215,510,000.00 USD | 0.00 USD | 443,030.00 USD | `-10.89%` | `226.61` |
| `Live` | `Long` | `1965.00` | 215,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-10.43%` | `537.11` |
| `Live` | `Long` | `1975.00` | 214,010,000.00 USD | 0.00 USD | 1,720,000.00 USD | `-9.98%` | `870.14` |
| `Live` | `Long` | `1985.00` | 212,290,000.00 USD | 0.00 USD | 5,210,000.00 USD | `-9.52%` | `2,623.65` |
| `Live` | `Long` | `1995.00` | 207,080,000.00 USD | 0.00 USD | 1,720,000.00 USD | `-9.07%` | `860.98` |
| `Live` | `Long` | `2005.00` | 205,370,000.00 USD | 0.00 USD | 5,640,000.00 USD | `-8.61%` | `2,813.69` |
| `Live` | `Long` | `2015.00` | 199,720,000.00 USD | 0.00 USD | 2,090,000.00 USD | `-8.15%` | `1,036.24` |
| `Live` | `Long` | `2025.00` | 197,640,000.00 USD | 0.00 USD | 1,210,000.00 USD | `-7.70%` | `599.66` |
| `Live` | `Long` | `2035.00` | 196,420,000.00 USD | 0.00 USD | 2,090,000.00 USD | `-7.24%` | `1,025.54` |
| `Live` | `Long` | `2045.00` | 194,330,000.00 USD | 0.00 USD | 3,520,000.00 USD | `-6.79%` | `1,720.56` |
| `Live` | `Long` | `2055.00` | 190,820,000.00 USD | 0.00 USD | 19,100,000.00 USD | `-6.33%` | `9,295.02` |
| `Live` | `Long` | `2065.00` | 171,710,000.00 USD | 0.00 USD | 8,630,000.00 USD | `-5.87%` | `4,177.56` |
| `Live` | `Long` | `2075.00` | 163,090,000.00 USD | 0.00 USD | 6,700,000.00 USD | `-5.42%` | `3,228.61` |
| `Live` | `Long` | `2085.00` | 156,390,000.00 USD | 0.00 USD | 13,110,000.00 USD | `-4.96%` | `6,288.45` |
| `Live` | `Long` | `2095.00` | 143,280,000.00 USD | 0.00 USD | 1,670,000.00 USD | `-4.51%` | `797.84` |
| `Live` | `Long` | `2105.00` | 141,610,000.00 USD | 0.00 USD | 1,870,000.00 USD | `-4.05%` | `887.28` |
| `Live` | `Long` | `2115.00` | 139,740,000.00 USD | 0.00 USD | 1,630,000.00 USD | `-3.60%` | `772.83` |
| `Live` | `Long` | `2125.00` | 138,100,000.00 USD | 0.00 USD | 123,050,000.00 USD | `-3.14%` | `57,905.00` |
| `Live` | `Long` | `2135.00` | 15,060,000.00 USD | 0.00 USD | 3,190,000.00 USD | `-2.68%` | `1,494.07` |
| `Live` | `Long` | `2145.00` | 11,870,000.00 USD | 0.00 USD | 4,860,000.00 USD | `-2.23%` | `2,263.88` |
| `Live` | `Long` | `2155.00` | 7,010,000.00 USD | 0.00 USD | 3,200,000.00 USD | `-1.77%` | `1,485.68` |
| `Live` | `Long` | `2165.00` | 3,810,000.00 USD | 0.00 USD | 2,640,000.00 USD | `-1.32%` | `1,219.91` |
| `Live` | `Long` | `2175.00` | 1,170,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-0.86%` | `530.05` |
| `Live` | `Long` | `2185.00` | 13,780.00 USD | 0.00 USD | 13,780.00 USD | `-0.40%` | `6.31` |
| `Live` | `Short` | `2195.00` | 41,590.00 USD | 41,590.00 USD | 0.00 USD | `+0.05%` | `18.95` |
| `Live` | `Short` | `2225.00` | 175,000.00 USD | 133,410.00 USD | 0.00 USD | `+1.42%` | `59.96` |
| `Live` | `Short` | `2235.00` | 3,920,000.00 USD | 3,750,000.00 USD | 0.00 USD | `+1.87%` | `1,676.39` |
| `Live` | `Short` | `2245.00` | 7,140,000.00 USD | 3,220,000.00 USD | 0.00 USD | `+2.33%` | `1,432.76` |
| `Live` | `Short` | `2255.00` | 16,520,000.00 USD | 9,380,000.00 USD | 0.00 USD | `+2.79%` | `4,161.34` |
| `Live` | `Short` | `2265.00` | 17,180,000.00 USD | 660,570.00 USD | 0.00 USD | `+3.24%` | `291.64` |
| `Live` | `Short` | `2275.00` | 17,470,000.00 USD | 291,560.00 USD | 0.00 USD | `+3.70%` | `128.16` |
| `Live` | `Short` | `2285.00` | 17,530,000.00 USD | 51,650.00 USD | 0.00 USD | `+4.15%` | `22.61` |
| `Live` | `Short` | `2295.00` | 20,880,000.00 USD | 3,360,000.00 USD | 0.00 USD | `+4.61%` | `1,463.56` |
| `Live` | `Short` | `2305.00` | 21,140,000.00 USD | 252,880.00 USD | 0.00 USD | `+5.06%` | `109.71` |
| `Live` | `Short` | `2315.00` | 22,550,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+5.52%` | `610.63` |
| `Live` | `Short` | `2325.00` | 24,210,000.00 USD | 1,660,000.00 USD | 0.00 USD | `+5.98%` | `712.78` |
| `Live` | `Short` | `2335.00` | 25,300,000.00 USD | 1,090,000.00 USD | 0.00 USD | `+6.43%` | `466.65` |
| `Live` | `Short` | `2345.00` | 25,530,000.00 USD | 230,280.00 USD | 0.00 USD | `+6.89%` | `98.20` |
| `Live` | `Short` | `2355.00` | 27,200,000.00 USD | 1,670,000.00 USD | 0.00 USD | `+7.34%` | `708.86` |
| `Live` | `Short` | `2365.00` | 31,200,000.00 USD | 4,000,000.00 USD | 0.00 USD | `+7.80%` | `1,690.29` |
| `Live` | `Short` | `2375.00` | 32,780,000.00 USD | 1,590,000.00 USD | 0.00 USD | `+8.26%` | `669.01` |
| `Live` | `Short` | `2385.00` | 38,470,000.00 USD | 5,690,000.00 USD | 0.00 USD | `+8.71%` | `2,383.69` |
| `Live` | `Short` | `2395.00` | 43,510,000.00 USD | 5,040,000.00 USD | 0.00 USD | `+9.17%` | `2,106.23` |
| `Live` | `Short` | `2405.00` | 43,720,000.00 USD | 207,600.00 USD | 0.00 USD | `+9.62%` | `86.32` |
| `Live` | `Short` | `2415.00` | 43,880,000.00 USD | 159,090.00 USD | 0.00 USD | `+10.08%` | `65.88` |
| `Live` | `Short` | `2425.00` | 45,480,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+10.53%` | `661.27` |
| `Live` | `Short` | `2435.00` | 45,690,000.00 USD | 207,040.00 USD | 0.00 USD | `+10.99%` | `85.03` |
| `Live` | `Short` | `2445.00` | 46,030,000.00 USD | 334,460.00 USD | 0.00 USD | `+11.45%` | `136.79` |
| `Live` | `Short` | `2455.00` | 46,250,000.00 USD | 223,610.00 USD | 0.00 USD | `+11.90%` | `91.08` |
| `Live` | `Short` | `2465.00` | 58,210,000.00 USD | 11,960,000.00 USD | 0.00 USD | `+12.36%` | `4,853.01` |
| `Live` | `Short` | `2475.00` | 58,830,000.00 USD | 615,790.00 USD | 0.00 USD | `+12.81%` | `248.80` |
| `Live` | `Short` | `2485.00` | 58,860,000.00 USD | 36,830.00 USD | 0.00 USD | `+13.27%` | `14.82` |
| `Live` | `Short` | `2495.00` | 58,980,000.00 USD | 118,030.00 USD | 0.00 USD | `+13.73%` | `47.31` |
| `Live` | `Short` | `2505.00` | 114,360,000.00 USD | 55,380,000.00 USD | 0.00 USD | `+14.18%` | `22,107.22` |
| `Live` | `Short` | `2515.00` | 120,870,000.00 USD | 6,510,000.00 USD | 0.00 USD | `+14.64%` | `2,589.08` |
| `Live` | `Short` | `2525.00` | 138,920,000.00 USD | 18,050,000.00 USD | 0.00 USD | `+15.09%` | `7,148.91` |
| `Live` | `Short` | `2535.00` | 139,810,000.00 USD | 889,170.00 USD | 0.00 USD | `+15.55%` | `350.76` |
| `Live` | `Short` | `2545.00` | 140,010,000.00 USD | 193,650.00 USD | 0.00 USD | `+16.00%` | `76.09` |
| `Live` | `Short` | `2555.00` | 140,840,000.00 USD | 834,430.00 USD | 0.00 USD | `+16.46%` | `326.59` |
| `Live` | `Short` | `2565.00` | 142,680,000.00 USD | 1,840,000.00 USD | 0.00 USD | `+16.92%` | `717.61` |
| `Live` | `Short` | `2575.00` | 143,230,000.00 USD | 552,900.00 USD | 0.00 USD | `+17.37%` | `214.72` |
| `Live` | `Short` | `2585.00` | 169,760,000.00 USD | 26,530,000.00 USD | 0.00 USD | `+17.83%` | `10,262.86` |
| `Live` | `Short` | `2595.00` | 177,900,000.00 USD | 8,140,000.00 USD | 0.00 USD | `+18.28%` | `3,136.86` |
| `Live` | `Short` | `2605.00` | 178,240,000.00 USD | 339,670.00 USD | 0.00 USD | `+18.74%` | `130.39` |
| `Live` | `Short` | `2615.00` | 178,470,000.00 USD | 226,630.00 USD | 0.00 USD | `+19.20%` | `86.66` |
| `Live` | `Short` | `2625.00` | 211,260,000.00 USD | 32,790,000.00 USD | 0.00 USD | `+19.65%` | `12,491.82` |
| `Live` | `Short` | `2635.00` | 212,860,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+20.11%` | `608.25` |
| `Live` | `Short` | `2645.00` | 213,500,000.00 USD | 639,970.00 USD | 0.00 USD | `+20.56%` | `241.96` |
| `Live` | `Short` | `2655.00` | 239,570,000.00 USD | 26,060,000.00 USD | 0.00 USD | `+21.02%` | `9,816.66` |
| `Live` | `Short` | `2665.00` | 240,010,000.00 USD | 438,080.00 USD | 0.00 USD | `+21.47%` | `164.38` |
| `Live` | `Short` | `2675.00` | 244,500,000.00 USD | 4,490,000.00 USD | 0.00 USD | `+21.93%` | `1,679.89` |
| `Live` | `Short` | `2685.00` | 244,560,000.00 USD | 59,830.00 USD | 0.00 USD | `+22.39%` | `22.28` |
| `Live` | `Short` | `2695.00` | 250,950,000.00 USD | 6,390,000.00 USD | 0.00 USD | `+22.84%` | `2,369.82` |
| `Live` | `Short` | `2705.00` | 257,420,000.00 USD | 6,470,000.00 USD | 0.00 USD | `+23.30%` | `2,392.31` |
| `Live` | `Short` | `2715.00` | 257,420,000.00 USD | 4,640.00 USD | 0.00 USD | `+23.75%` | `1.71` |
| `Live` | `Short` | `2725.00` | 270,430,000.00 USD | 13,010,000.00 USD | 0.00 USD | `+24.21%` | `4,773.87` |
| `Live` | `Short` | `2735.00` | 270,670,000.00 USD | 238,930.00 USD | 0.00 USD | `+24.66%` | `87.36` |
| `Live` | `Short` | `2745.00` | 276,570,000.00 USD | 5,900,000.00 USD | 0.00 USD | `+25.12%` | `2,149.53` |
| `Live` | `Short` | `2755.00` | 277,950,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+25.58%` | `501.42` |
| `Live` | `Short` | `2765.00` | 282,380,000.00 USD | 4,430,000.00 USD | 0.00 USD | `+26.03%` | `1,601.06` |
| `Live` | `Short` | `2775.00` | 282,730,000.00 USD | 355,030.00 USD | 0.00 USD | `+26.49%` | `127.94` |
| `Live` | `Short` | `2785.00` | 284,660,000.00 USD | 1,920,000.00 USD | 0.00 USD | `+26.94%` | `690.41` |
| `Live` | `Short` | `2795.00` | 299,720,000.00 USD | 15,060,000.00 USD | 0.00 USD | `+27.40%` | `5,388.93` |
| `Live` | `Short` | `2805.00` | 303,510,000.00 USD | 3,790,000.00 USD | 0.00 USD | `+27.86%` | `1,351.06` |
| `Live` | `Short` | `2815.00` | 304,670,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+28.31%` | `412.62` |
| `Live` | `Short` | `2825.00` | 304,890,000.00 USD | 224,370.00 USD | 0.00 USD | `+28.77%` | `79.42` |
| `Live` | `Short` | `2835.00` | 312,660,000.00 USD | 7,760,000.00 USD | 0.00 USD | `+29.22%` | `2,738.66` |
| `Live` | `Short` | `2845.00` | 312,800,000.00 USD | 139,770.00 USD | 0.00 USD | `+29.68%` | `49.13` |
| `Live` | `Short` | `2855.00` | 313,200,000.00 USD | 402,980.00 USD | 0.00 USD | `+30.13%` | `141.15` |
| `Live` | `Short` | `2865.00` | 314,050,000.00 USD | 846,340.00 USD | 0.00 USD | `+30.59%` | `295.41` |
| `Live` | `Short` | `2875.00` | 314,180,000.00 USD | 130,270.00 USD | 0.00 USD | `+31.05%` | `45.31` |
| `Live` | `Short` | `2885.00` | 316,190,000.00 USD | 2,010,000.00 USD | 0.00 USD | `+31.50%` | `697.68` |
| `Live` | `Short` | `2895.00` | 316,500,000.00 USD | 306,810.00 USD | 0.00 USD | `+31.96%` | `105.98` |
| `Live` | `Short` | `2905.00` | 316,780,000.00 USD | 286,270.00 USD | 0.00 USD | `+32.41%` | `98.55` |
| `Live` | `Short` | `2915.00` | 319,100,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+32.87%` | `796.19` |
| `Live` | `Short` | `2925.00` | 320,300,000.00 USD | 1,190,000.00 USD | 0.00 USD | `+33.33%` | `408.25` |
| `Live` | `Short` | `2935.00` | 320,440,000.00 USD | 145,500.00 USD | 0.00 USD | `+33.78%` | `49.57` |
| `Live` | `Short` | `2945.00` | 320,840,000.00 USD | 394,070.00 USD | 0.00 USD | `+34.24%` | `133.81` |
| `Live` | `Short` | `2955.00` | 324,220,000.00 USD | 3,380,000.00 USD | 0.00 USD | `+34.69%` | `1,144.55` |
| `Live` | `Short` | `2965.00` | 352,190,000.00 USD | 27,970,000.00 USD | 0.00 USD | `+35.15%` | `9,432.56` |
| `Live` | `Short` | `2975.00` | 352,300,000.00 USD | 115,120.00 USD | 0.00 USD | `+35.60%` | `38.69` |
| `Live` | `Short` | `2985.00` | 352,680,000.00 USD | 379,670.00 USD | 0.00 USD | `+36.06%` | `127.19` |
| `Live` | `Short` | `2995.00` | 353,700,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+36.52%` | `338.63` |
| `Live` | `Short` | `3005.00` | 355,440,000.00 USD | 1,740,000.00 USD | 0.00 USD | `+36.97%` | `580.40` |
| `Live` | `Short` | `3015.00` | 355,760,000.00 USD | 320,320.00 USD | 0.00 USD | `+37.43%` | `106.24` |
| `Live` | `Short` | `3025.00` | 362,030,000.00 USD | 6,270,000.00 USD | 0.00 USD | `+37.88%` | `2,073.56` |
| `Live` | `Short` | `3035.00` | 395,580,000.00 USD | 33,550,000.00 USD | 0.00 USD | `+38.34%` | `11,053.61` |
| `Live` | `Short` | `3045.00` | 396,230,000.00 USD | 648,220.00 USD | 0.00 USD | `+38.80%` | `212.88` |
| `Live` | `Short` | `3055.00` | 397,730,000.00 USD | 1,500,000.00 USD | 0.00 USD | `+39.25%` | `490.32` |
| `Live` | `Short` | `3065.00` | 397,750,000.00 USD | 19,360.00 USD | 0.00 USD | `+39.71%` | `6.32` |
| `Live` | `Short` | `3075.00` | 397,900,000.00 USD | 153,180.00 USD | 0.00 USD | `+40.16%` | `49.82` |
| `Live` | `Short` | `3085.00` | 426,700,000.00 USD | 28,800,000.00 USD | 0.00 USD | `+40.62%` | `9,334.18` |
| `Live` | `Short` | `3095.00` | 427,160,000.00 USD | 464,560.00 USD | 0.00 USD | `+41.07%` | `150.10` |
| `Live` | `Short` | `3105.00` | 435,480,000.00 USD | 8,330,000.00 USD | 0.00 USD | `+41.53%` | `2,681.16` |
| `Live` | `Short` | `3115.00` | 440,000,000.00 USD | 4,510,000.00 USD | 0.00 USD | `+41.99%` | `1,449.23` |
| `Live` | `Short` | `3125.00` | 440,720,000.00 USD | 718,050.00 USD | 0.00 USD | `+42.44%` | `229.78` |
| `Live` | `Short` | `3135.00` | 442,620,000.00 USD | 1,900,000.00 USD | 0.00 USD | `+42.90%` | `605.81` |
| `Live` | `Short` | `3145.00` | 442,770,000.00 USD | 157,660.00 USD | 0.00 USD | `+43.35%` | `50.13` |
| `Live` | `Short` | `3155.00` | 443,790,000.00 USD | 1,020,000.00 USD | 0.00 USD | `+43.81%` | `322.05` |
| `Live` | `Short` | `3165.00` | 445,590,000.00 USD | 1,800,000.00 USD | 0.00 USD | `+44.26%` | `570.12` |
| `Live` | `Short` | `3175.00` | 449,470,000.00 USD | 3,880,000.00 USD | 0.00 USD | `+44.72%` | `1,221.91` |
| `Live` | `Short` | `3185.00` | 450,960,000.00 USD | 1,490,000.00 USD | 0.00 USD | `+45.18%` | `467.88` |
| `Live` | `Short` | `3195.00` | 467,330,000.00 USD | 16,370,000.00 USD | 0.00 USD | `+45.63%` | `5,122.29` |
| `Live` | `Short` | `3205.00` | 467,720,000.00 USD | 389,500.00 USD | 0.00 USD | `+46.09%` | `121.53` |
| `Live` | `Short` | `3215.00` | 472,740,000.00 USD | 5,020,000.00 USD | 0.00 USD | `+46.54%` | `1,561.86` |
| `Live` | `Short` | `3225.00` | 472,770,000.00 USD | 31,890.00 USD | 0.00 USD | `+47.00%` | `9.89` |
| `Live` | `Short` | `3235.00` | 490,900,000.00 USD | 18,130,000.00 USD | 0.00 USD | `+47.46%` | `5,603.70` |
| `Live` | `Short` | `3245.00` | 491,490,000.00 USD | 586,260.00 USD | 0.00 USD | `+47.91%` | `180.66` |
| `Live` | `Short` | `3255.00` | 491,520,000.00 USD | 35,060.00 USD | 0.00 USD | `+48.37%` | `10.77` |
| `Live` | `Short` | `3265.00` | 491,660,000.00 USD | 135,990.00 USD | 0.00 USD | `+48.82%` | `41.65` |
| `Live` | `Short` | `3275.00` | 500,330,000.00 USD | 8,680,000.00 USD | 0.00 USD | `+49.28%` | `2,649.21` |
| `Live` | `Short` | `3285.00` | 500,440,000.00 USD | 107,110.00 USD | 0.00 USD | `+49.73%` | `32.61` |
| `Live` | `Short` | `3295.00` | 500,760,000.00 USD | 319,520.00 USD | 0.00 USD | `+50.19%` | `96.97` |
| `Live` | `Short` | `3305.00` | 501,950,000.00 USD | 1,190,000.00 USD | 0.00 USD | `+50.65%` | `358.67` |
| `Live` | `Short` | `3315.00` | 502,660,000.00 USD | 710,580.00 USD | 0.00 USD | `+51.10%` | `214.35` |
| `Live` | `Short` | `3325.00` | 504,380,000.00 USD | 1,720,000.00 USD | 0.00 USD | `+51.56%` | `518.67` |
| `Live` | `Short` | `3335.00` | 504,490,000.00 USD | 107,510.00 USD | 0.00 USD | `+52.01%` | `32.24` |
| `Live` | `Short` | `3345.00` | 504,560,000.00 USD | 75,350.00 USD | 0.00 USD | `+52.47%` | `22.53` |
| `Live` | `Short` | `3355.00` | 504,950,000.00 USD | 384,020.00 USD | 0.00 USD | `+52.93%` | `114.46` |
| `Live` | `Short` | `3365.00` | 505,390,000.00 USD | 445,620.00 USD | 0.00 USD | `+53.38%` | `132.43` |
| `Live` | `Short` | `3375.00` | 505,430,000.00 USD | 38,140.00 USD | 0.00 USD | `+53.84%` | `11.30` |
| `Live` | `Short` | `3385.00` | 505,550,000.00 USD | 115,930.00 USD | 0.00 USD | `+54.29%` | `34.25` |
| `Live` | `Short` | `3395.00` | 506,450,000.00 USD | 899,730.00 USD | 0.00 USD | `+54.75%` | `265.02` |
| `Live` | `Short` | `3405.00` | 506,650,000.00 USD | 202,720.00 USD | 0.00 USD | `+55.20%` | `59.54` |
| `Live` | `Short` | `3415.00` | 506,670,000.00 USD | 16,170.00 USD | 0.00 USD | `+55.66%` | `4.73` |
| `Live` | `Short` | `3425.00` | 521,380,000.00 USD | 14,710,000.00 USD | 0.00 USD | `+56.12%` | `4,296.16` |
| `Live` | `Short` | `3435.00` | 522,370,000.00 USD | 984,440.00 USD | 0.00 USD | `+56.57%` | `286.59` |
| `Live` | `Short` | `3445.00` | 526,580,000.00 USD | 4,220,000.00 USD | 0.00 USD | `+57.03%` | `1,223.69` |
| `Live` | `Short` | `3455.00` | 526,960,000.00 USD | 373,990.00 USD | 0.00 USD | `+57.48%` | `108.25` |
| `Live` | `Short` | `3465.00` | 589,040,000.00 USD | 62,090,000.00 USD | 0.00 USD | `+57.94%` | `17,918.89` |
| `Live` | `Short` | `3475.00` | 589,320,000.00 USD | 276,220.00 USD | 0.00 USD | `+58.40%` | `79.49` |
| `Live` | `Short` | `3485.00` | 589,510,000.00 USD | 186,940.00 USD | 0.00 USD | `+58.85%` | `53.64` |
| `Live` | `Short` | `3495.00` | 590,600,000.00 USD | 1,090,000.00 USD | 0.00 USD | `+59.31%` | `312.02` |
| `Live` | `Short` | `3505.00` | 591,180,000.00 USD | 586,670.00 USD | 0.00 USD | `+59.76%` | `167.38` |
| `Live` | `Short` | `3515.00` | 593,960,000.00 USD | 2,770,000.00 USD | 0.00 USD | `+60.22%` | `789.36` |
| `Live` | `Short` | `3525.00` | 594,300,000.00 USD | 342,840.00 USD | 0.00 USD | `+60.67%` | `97.26` |
| `Live` | `Short` | `3535.00` | 594,630,000.00 USD | 323,920.00 USD | 0.00 USD | `+61.13%` | `91.63` |
| `Live` | `Short` | `3545.00` | 595,820,000.00 USD | 1,190,000.00 USD | 0.00 USD | `+61.59%` | `336.07` |
| `Live` | `Short` | `3555.00` | 596,080,000.00 USD | 265,280.00 USD | 0.00 USD | `+62.04%` | `74.62` |
| `Live` | `Short` | `3565.00` | 598,030,000.00 USD | 1,950,000.00 USD | 0.00 USD | `+62.50%` | `547.54` |
| `Live` | `Short` | `3575.00` | 598,110,000.00 USD | 79,950.00 USD | 0.00 USD | `+62.95%` | `22.36` |
| `Live` | `Short` | `3585.00` | 598,870,000.00 USD | 758,690.00 USD | 0.00 USD | `+63.41%` | `211.63` |
| `Live` | `Short` | `3595.00` | 599,340,000.00 USD | 469,720.00 USD | 0.00 USD | `+63.86%` | `130.66` |
| `Live` | `Short` | `3605.00` | 599,350,000.00 USD | 4,520.00 USD | 0.00 USD | `+64.32%` | `1.25` |
| `Live` | `Short` | `3615.00` | 611,630,000.00 USD | 12,280,000.00 USD | 0.00 USD | `+64.78%` | `3,398.34` |
| `Live` | `Short` | `3625.00` | 612,100,000.00 USD | 469,000.00 USD | 0.00 USD | `+65.23%` | `129.38` |
| `Live` | `Short` | `3635.00` | 612,280,000.00 USD | 178,520.00 USD | 0.00 USD | `+65.69%` | `49.11` |
| `Live` | `Short` | `3645.00` | 614,980,000.00 USD | 2,700,000.00 USD | 0.00 USD | `+66.14%` | `739.84` |
| `Live` | `Short` | `3655.00` | 647,240,000.00 USD | 32,260,000.00 USD | 0.00 USD | `+66.60%` | `8,827.17` |
| `Live` | `Short` | `3665.00` | 648,590,000.00 USD | 1,350,000.00 USD | 0.00 USD | `+67.06%` | `368.95` |
| `Live` | `Short` | `3675.00` | 648,790,000.00 USD | 194,720.00 USD | 0.00 USD | `+67.51%` | `52.98` |
| `Live` | `Short` | `3685.00` | 649,150,000.00 USD | 366,020.00 USD | 0.00 USD | `+67.97%` | `99.33` |
| `Live` | `Short` | `3695.00` | 655,700,000.00 USD | 6,550,000.00 USD | 0.00 USD | `+68.42%` | `1,771.50` |
| `Live` | `Short` | `3705.00` | 655,970,000.00 USD | 270,770.00 USD | 0.00 USD | `+68.88%` | `73.08` |
| `Live` | `Short` | `3715.00` | 655,990,000.00 USD | 20,630.00 USD | 0.00 USD | `+69.33%` | `5.55` |
| `Live` | `Short` | `3725.00` | 656,300,000.00 USD | 308,960.00 USD | 0.00 USD | `+69.79%` | `82.94` |
| `Live` | `Short` | `3735.00` | 656,700,000.00 USD | 398,880.00 USD | 0.00 USD | `+70.25%` | `106.80` |
| `Live` | `Short` | `3745.00` | 657,540,000.00 USD | 840,530.00 USD | 0.00 USD | `+70.70%` | `224.44` |
| `Live` | `Short` | `3755.00` | 672,650,000.00 USD | 15,110,000.00 USD | 0.00 USD | `+71.16%` | `4,023.85` |
| `Live` | `Short` | `3765.00` | 672,750,000.00 USD | 99,760.00 USD | 0.00 USD | `+71.61%` | `26.50` |
| `Live` | `Short` | `3775.00` | 673,060,000.00 USD | 310,260.00 USD | 0.00 USD | `+72.07%` | `82.19` |
| `Live` | `Short` | `3785.00` | 675,630,000.00 USD | 2,580,000.00 USD | 0.00 USD | `+72.53%` | `680.70` |
| `Live` | `Short` | `3795.00` | 675,830,000.00 USD | 200,410.00 USD | 0.00 USD | `+72.98%` | `52.81` |
| `Live` | `Short` | `3805.00` | 678,250,000.00 USD | 2,420,000.00 USD | 0.00 USD | `+73.44%` | `634.81` |
| `Live` | `Short` | `3815.00` | 678,290,000.00 USD | 42,930.00 USD | 0.00 USD | `+73.89%` | `11.25` |
| `Live` | `Short` | `3825.00` | 678,380,000.00 USD | 91,090.00 USD | 0.00 USD | `+74.35%` | `23.82` |
| `Live` | `Short` | `3835.00` | 678,670,000.00 USD | 282,790.00 USD | 0.00 USD | `+74.80%` | `73.74` |
| `Live` | `Short` | `3845.00` | 678,860,000.00 USD | 189,850.00 USD | 0.00 USD | `+75.26%` | `49.38` |
| `Live` | `Short` | `3855.00` | 679,220,000.00 USD | 363,360.00 USD | 0.00 USD | `+75.72%` | `94.26` |
| `Live` | `Short` | `3865.00` | 680,480,000.00 USD | 1,260,000.00 USD | 0.00 USD | `+76.17%` | `326.11` |
| `Live` | `Short` | `3875.00` | 681,630,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+76.63%` | `296.95` |
| `Live` | `Short` | `3885.00` | 683,110,000.00 USD | 1,470,000.00 USD | 0.00 USD | `+77.08%` | `379.41` |
| `Live` | `Short` | `3895.00` | 683,130,000.00 USD | 25,030.00 USD | 0.00 USD | `+77.54%` | `6.43` |
| `Live` | `Short` | `3905.00` | 683,620,000.00 USD | 490,460.00 USD | 0.00 USD | `+78.00%` | `125.60` |
| `Live` | `Short` | `3915.00` | 683,700,000.00 USD | 75,750.00 USD | 0.00 USD | `+78.45%` | `19.35` |
| `Live` | `Short` | `3925.00` | 684,330,000.00 USD | 636,770.00 USD | 0.00 USD | `+78.91%` | `162.24` |
| `Live` | `Short` | `3935.00` | 684,850,000.00 USD | 521,140.00 USD | 0.00 USD | `+79.36%` | `132.44` |
| `Live` | `Short` | `3945.00` | 684,860,000.00 USD | 6,330.00 USD | 0.00 USD | `+79.82%` | `1.60` |
| `Live` | `Short` | `3955.00` | 684,860,000.00 USD | 618.17 USD | 0.00 USD | `+80.27%` | `0.16` |
| `Live` | `Short` | `3965.00` | 684,890,000.00 USD | 24,530.00 USD | 0.00 USD | `+80.73%` | `6.19` |
| `Live` | `Short` | `3975.00` | 723,850,000.00 USD | 38,970,000.00 USD | 0.00 USD | `+81.19%` | `9,802.61` |
| `Live` | `Short` | `3985.00` | 724,170,000.00 USD | 321,680.00 USD | 0.00 USD | `+81.64%` | `80.72` |
| `Live` | `Short` | `3995.00` | 789,150,000.00 USD | 64,980,000.00 USD | 0.00 USD | `+82.10%` | `16,265.16` |
| `Live` | `Short` | `4005.00` | 789,760,000.00 USD | 609,150.00 USD | 0.00 USD | `+82.55%` | `152.10` |
| `Live` | `Short` | `4015.00` | 789,800,000.00 USD | 42,810.00 USD | 0.00 USD | `+83.01%` | `10.66` |
| `Live` | `Short` | `4025.00` | 790,120,000.00 USD | 315,140.00 USD | 0.00 USD | `+83.46%` | `78.30` |
| `Live` | `Short` | `4035.00` | 790,180,000.00 USD | 56,910.00 USD | 0.00 USD | `+83.92%` | `14.10` |
| `Live` | `Short` | `4045.00` | 792,320,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+84.38%` | `530.73` |
| `Live` | `Short` | `4055.00` | 792,390,000.00 USD | 63,060.00 USD | 0.00 USD | `+84.83%` | `15.55` |
| `Live` | `Short` | `4065.00` | 795,470,000.00 USD | 3,080,000.00 USD | 0.00 USD | `+85.29%` | `758.58` |
| `Live` | `Short` | `4075.00` | 1,230,000,000.00 USD | 433,770,000.00 USD | 0.00 USD | `+85.74%` | `106,445.69` |
| `Live` | `Short` | `4085.00` | 1,230,000,000.00 USD | 16,500.00 USD | 0.00 USD | `+86.20%` | `4.04` |
| `Live` | `Short` | `4095.00` | 1,230,000,000.00 USD | 528,780.00 USD | 0.00 USD | `+86.66%` | `129.13` |
| `Live` | `Short` | `4105.00` | 1,230,000,000.00 USD | 108,450.00 USD | 0.00 USD | `+87.11%` | `26.42` |
| `Live` | `Short` | `4115.00` | 1,230,000,000.00 USD | 1,990,000.00 USD | 0.00 USD | `+87.57%` | `483.50` |
| `Live` | `Short` | `4125.00` | 1,230,000,000.00 USD | 299,080.00 USD | 0.00 USD | `+88.02%` | `72.50` |
| `Live` | `Short` | `4135.00` | 1,230,000,000.00 USD | 63,620.00 USD | 0.00 USD | `+88.48%` | `15.39` |
| `Live` | `Short` | `4145.00` | 1,230,000,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+88.93%` | `528.30` |
| `Live` | `Short` | `4155.00` | 1,230,000,000.00 USD | 166,330.00 USD | 0.00 USD | `+89.39%` | `40.03` |
| `Live` | `Short` | `4165.00` | 1,230,000,000.00 USD | 141,870.00 USD | 0.00 USD | `+89.85%` | `34.06` |
| `Live` | `Short` | `4175.00` | 1,230,000,000.00 USD | 2,780.00 USD | 0.00 USD | `+90.30%` | `0.67` |
| `Live` | `Short` | `4185.00` | 1,240,000,000.00 USD | 828,320.00 USD | 0.00 USD | `+90.76%` | `197.93` |
| `Live` | `Short` | `4195.00` | 1,240,000,000.00 USD | 4,440,000.00 USD | 0.00 USD | `+91.21%` | `1,057.89` |
| `Live` | `Short` | `4205.00` | 1,240,000,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+91.67%` | `449.27` |
| `Live` | `Short` | `4215.00` | 1,330,000,000.00 USD | 92,620,000.00 USD | 0.00 USD | `+92.13%` | `21,974.74` |
| `Live` | `Short` | `4225.00` | 1,340,000,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+92.58%` | `327.25` |
| `Live` | `Short` | `4235.00` | 1,340,000,000.00 USD | 115,220.00 USD | 0.00 USD | `+93.04%` | `27.21` |
| `Live` | `Short` | `4245.00` | 1,370,000,000.00 USD | 29,030,000.00 USD | 0.00 USD | `+93.49%` | `6,837.68` |
| `Live` | `Short` | `4255.00` | 1,370,000,000.00 USD | 420.39 USD | 0.00 USD | `+93.95%` | `0.10` |
| `Live` | `Short` | `4265.00` | 1,370,000,000.00 USD | 54,480.00 USD | 0.00 USD | `+94.40%` | `12.77` |
| `Live` | `Short` | `4275.00` | 1,370,000,000.00 USD | 301.39 USD | 0.00 USD | `+94.86%` | `0.07` |
| `Live` | `Short` | `4285.00` | 1,370,000,000.00 USD | 223,960.00 USD | 0.00 USD | `+95.32%` | `52.27` |
| `Live` | `Short` | `4295.00` | 1,370,000,000.00 USD | 19,590.00 USD | 0.00 USD | `+95.77%` | `4.56` |
| `Live` | `Short` | `4305.00` | 1,370,000,000.00 USD | 13,080.00 USD | 0.00 USD | `+96.23%` | `3.04` |
| `Live` | `Short` | `4325.00` | 1,370,000,000.00 USD | 6,660.00 USD | 0.00 USD | `+97.14%` | `1.54` |
| `Live` | `Short` | `4335.00` | 1,370,000,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+97.60%` | `370.25` |
| `Live` | `Short` | `4345.00` | 1,370,000,000.00 USD | 15,410.00 USD | 0.00 USD | `+98.05%` | `3.55` |
| `Live` | `Short` | `4355.00` | 1,370,000,000.00 USD | 197,540.00 USD | 0.00 USD | `+98.51%` | `45.36` |
| `Live` | `Short` | `4365.00` | 1,370,000,000.00 USD | 670,800.00 USD | 0.00 USD | `+98.96%` | `153.68` |
| `Live` | `Short` | `4375.00` | 1,370,000,000.00 USD | 505.31 USD | 0.00 USD | `+99.42%` | `0.12` |
| `Live` | `Short` | `4385.00` | 1,370,000,000.00 USD | 104,290.00 USD | 0.00 USD | `+99.87%` | `23.78` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `485.00` | 58,630,000.00 USD | 0.00 USD | 278.83 USD | `-77.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `505.00` | 58,630,000.00 USD | 0.00 USD | 15,740.00 USD | `-76.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 58,610,000.00 USD | 0.00 USD | 563.16 USD | `-74.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.00` | 58,610,000.00 USD | 0.00 USD | 583.40 USD | `-70.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.00` | 58,610,000.00 USD | 0.00 USD | 16,690.00 USD | `-70.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.00` | 58,600,000.00 USD | 0.00 USD | 578.54 USD | `-69.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.00` | 58,600,000.00 USD | 0.00 USD | 242.21 USD | `-68.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 58,600,000.00 USD | 0.00 USD | 885.90 USD | `-67.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 58,590,000.00 USD | 0.00 USD | 177.27 USD | `-65.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `795.00` | 58,590,000.00 USD | 0.00 USD | 104.22 USD | `-63.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 58,590,000.00 USD | 0.00 USD | 2,090.00 USD | `-63.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 58,590,000.00 USD | 0.00 USD | 1,670.00 USD | `-61.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 58,590,000.00 USD | 0.00 USD | 139,430.00 USD | `-60.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `875.00` | 58,450,000.00 USD | 0.00 USD | 918.49 USD | `-60.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 58,450,000.00 USD | 0.00 USD | 3,130.00 USD | `-59.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 58,450,000.00 USD | 0.00 USD | 2,780.00 USD | `-58.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 58,440,000.00 USD | 0.00 USD | 516.34 USD | `-55.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 58,440,000.00 USD | 0.00 USD | 100.50 USD | `-54.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 58,440,000.00 USD | 0.00 USD | 223,740.00 USD | `-54.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 58,220,000.00 USD | 0.00 USD | 445.08 USD | `-53.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 58,220,000.00 USD | 0.00 USD | 112.03 USD | `-53.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1045.00` | 58,220,000.00 USD | 0.00 USD | 1,260.00 USD | `-52.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 58,220,000.00 USD | 0.00 USD | 1,060.00 USD | `-51.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 58,220,000.00 USD | 0.00 USD | 995.34 USD | `-51.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 58,220,000.00 USD | 0.00 USD | 1,610.00 USD | `-49.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 58,210,000.00 USD | 0.00 USD | 11,050.00 USD | `-49.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 58,200,000.00 USD | 0.00 USD | 1,320.00 USD | `-48.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 58,200,000.00 USD | 0.00 USD | 1,000.00 USD | `-47.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 58,200,000.00 USD | 0.00 USD | 464.71 USD | `-46.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 58,200,000.00 USD | 0.00 USD | 972.41 USD | `-45.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1195.00` | 58,200,000.00 USD | 0.00 USD | 199.92 USD | `-45.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 58,200,000.00 USD | 0.00 USD | 3,110.00 USD | `-45.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 58,200,000.00 USD | 0.00 USD | 995.93 USD | `-44.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 58,200,000.00 USD | 0.00 USD | 951.93 USD | `-43.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 58,190,000.00 USD | 0.00 USD | 2,290.00 USD | `-42.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 58,190,000.00 USD | 0.00 USD | 9,050.00 USD | `-41.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 58,180,000.00 USD | 0.00 USD | 7,030.00 USD | `-40.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 58,180,000.00 USD | 0.00 USD | 25,040.00 USD | `-40.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 58,150,000.00 USD | 0.00 USD | 1,440.00 USD | `-40.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 58,150,000.00 USD | 0.00 USD | 141,950.00 USD | `-38.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 58,010,000.00 USD | 0.00 USD | 128.86 USD | `-38.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 58,010,000.00 USD | 0.00 USD | 1,270.00 USD | `-37.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 58,010,000.00 USD | 0.00 USD | 4,160.00 USD | `-37.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1385.00` | 58,000,000.00 USD | 0.00 USD | 100,800.00 USD | `-36.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 57,900,000.00 USD | 0.00 USD | 535,600.00 USD | `-36.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 57,370,000.00 USD | 0.00 USD | 18,840.00 USD | `-35.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 57,350,000.00 USD | 0.00 USD | 6,450.00 USD | `-35.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 57,340,000.00 USD | 0.00 USD | 852.10 USD | `-34.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 57,340,000.00 USD | 0.00 USD | 1,610.00 USD | `-34.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 57,340,000.00 USD | 0.00 USD | 5,090.00 USD | `-33.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 57,330,000.00 USD | 0.00 USD | 19,730.00 USD | `-33.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 57,310,000.00 USD | 0.00 USD | 2,600.00 USD | `-32.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 57,310,000.00 USD | 0.00 USD | 18,710.00 USD | `-32.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 57,290,000.00 USD | 0.00 USD | 11,460.00 USD | `-31.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 57,280,000.00 USD | 0.00 USD | 84,170.00 USD | `-31.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 57,200,000.00 USD | 0.00 USD | 11,140.00 USD | `-30.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 57,190,000.00 USD | 0.00 USD | 31,900.00 USD | `-30.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 57,150,000.00 USD | 0.00 USD | 8,830.00 USD | `-30.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 57,140,000.00 USD | 0.00 USD | 960.99 USD | `-29.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 57,140,000.00 USD | 0.00 USD | 58,630.00 USD | `-29.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 57,080,000.00 USD | 0.00 USD | 6,260.00 USD | `-28.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 57,080,000.00 USD | 0.00 USD | 198,620.00 USD | `-28.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 56,880,000.00 USD | 0.00 USD | 7,750.00 USD | `-27.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 56,870,000.00 USD | 0.00 USD | 4,040.00 USD | `-27.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 56,870,000.00 USD | 0.00 USD | 432,070.00 USD | `-26.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 56,440,000.00 USD | 0.00 USD | 28,870.00 USD | `-26.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 56,410,000.00 USD | 0.00 USD | 13,590.00 USD | `-25.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 56,390,000.00 USD | 0.00 USD | 10,560.00 USD | `-25.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 56,380,000.00 USD | 0.00 USD | 326,230.00 USD | `-25.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 56,060,000.00 USD | 0.00 USD | 35,070.00 USD | `-24.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 56,020,000.00 USD | 0.00 USD | 744.09 USD | `-24.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 56,020,000.00 USD | 0.00 USD | 289.27 USD | `-23.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 56,020,000.00 USD | 0.00 USD | 35,440.00 USD | `-23.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 55,990,000.00 USD | 0.00 USD | 42,680.00 USD | `-22.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 55,940,000.00 USD | 0.00 USD | 84,490.00 USD | `-22.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 55,860,000.00 USD | 0.00 USD | 16,350.00 USD | `-21.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 55,840,000.00 USD | 0.00 USD | 47,500.00 USD | `-21.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 55,790,000.00 USD | 0.00 USD | 28,150.00 USD | `-20.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 55,770,000.00 USD | 0.00 USD | 3,180.00 USD | `-20.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 55,760,000.00 USD | 0.00 USD | 466,120.00 USD | `-20.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 55,300,000.00 USD | 0.00 USD | 76,690.00 USD | `-19.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 55,220,000.00 USD | 0.00 USD | 3,090.00 USD | `-19.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 55,220,000.00 USD | 0.00 USD | 8,500.00 USD | `-18.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 55,210,000.00 USD | 0.00 USD | 187,030.00 USD | `-18.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 55,020,000.00 USD | 0.00 USD | 660,140.00 USD | `-17.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 54,360,000.00 USD | 0.00 USD | 264,580.00 USD | `-17.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 54,100,000.00 USD | 0.00 USD | 27,520.00 USD | `-16.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 54,070,000.00 USD | 0.00 USD | 18,710.00 USD | `-16.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 54,050,000.00 USD | 0.00 USD | 26,170.00 USD | `-15.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 54,020,000.00 USD | 0.00 USD | 744,070.00 USD | `-15.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 53,280,000.00 USD | 0.00 USD | 34,010.00 USD | `-14.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 53,250,000.00 USD | 0.00 USD | 18,240,000.00 USD | `-14.53%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 35,000,000.00 USD | 0.00 USD | 22,130.00 USD | `-14.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 34,980,000.00 USD | 0.00 USD | 60,150.00 USD | `-13.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 34,920,000.00 USD | 0.00 USD | 160,340.00 USD | `-13.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 34,760,000.00 USD | 0.00 USD | 101,030.00 USD | `-12.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1925.00` | 34,660,000.00 USD | 0.00 USD | 19,300,000.00 USD | `-12.26%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 15,360,000.00 USD | 0.00 USD | 107,600.00 USD | `-11.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 15,260,000.00 USD | 0.00 USD | 45,240.00 USD | `-11.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 15,210,000.00 USD | 0.00 USD | 72,960.00 USD | `-10.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 15,140,000.00 USD | 0.00 USD | 139,530.00 USD | `-10.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 15,000,000.00 USD | 0.00 USD | 332,610.00 USD | `-9.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 14,660,000.00 USD | 0.00 USD | 117,480.00 USD | `-9.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 14,550,000.00 USD | 0.00 USD | 248,820.00 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 14,300,000.00 USD | 0.00 USD | 2,620,000.00 USD | `-8.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 11,680,000.00 USD | 0.00 USD | 524,480.00 USD | `-8.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 11,150,000.00 USD | 0.00 USD | 95,400.00 USD | `-7.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 11,060,000.00 USD | 0.00 USD | 328,340.00 USD | `-7.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 10,730,000.00 USD | 0.00 USD | 112,940.00 USD | `-6.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 10,610,000.00 USD | 0.00 USD | 1,040,000.00 USD | `-6.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 9,580,000.00 USD | 0.00 USD | 122,630.00 USD | `-5.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 9,460,000.00 USD | 0.00 USD | 42,490.00 USD | `-5.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 9,410,000.00 USD | 0.00 USD | 164,460.00 USD | `-4.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 9,250,000.00 USD | 0.00 USD | 25,570.00 USD | `-4.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 9,220,000.00 USD | 0.00 USD | 853,350.00 USD | `-4.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 8,370,000.00 USD | 0.00 USD | 207,430.00 USD | `-3.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 8,160,000.00 USD | 0.00 USD | 766,560.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 7,400,000.00 USD | 0.00 USD | 394,260.00 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 7,000,000.00 USD | 0.00 USD | 344,440.00 USD | `-2.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 6,660,000.00 USD | 0.00 USD | 4,960,000.00 USD | `-1.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 1,700,000.00 USD | 0.00 USD | 1,370,000.00 USD | `-1.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 324,820.00 USD | 0.00 USD | 259,810.00 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2185.00` | 65,010.00 USD | 0.00 USD | 65,010.00 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2195.00` | 83,110.00 USD | 83,110.00 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2205.00` | 118,290.00 USD | 35,180.00 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2215.00` | 1,540,000.00 USD | 1,420,000.00 USD | 0.00 USD | `+0.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2225.00` | 3,810,000.00 USD | 2,270,000.00 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2235.00` | 13,120,000.00 USD | 9,310,000.00 USD | 0.00 USD | `+1.87%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2245.00` | 13,640,000.00 USD | 518,480.00 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2255.00` | 15,060,000.00 USD | 1,420,000.00 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2265.00` | 15,780,000.00 USD | 723,590.00 USD | 0.00 USD | `+3.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 16,110,000.00 USD | 329,750.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 17,020,000.00 USD | 906,390.00 USD | 0.00 USD | `+4.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 17,300,000.00 USD | 277,970.00 USD | 0.00 USD | `+4.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 17,870,000.00 USD | 574,160.00 USD | 0.00 USD | `+5.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2315.00` | 19,560,000.00 USD | 1,690,000.00 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 20,010,000.00 USD | 445,660.00 USD | 0.00 USD | `+5.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 20,190,000.00 USD | 183,100.00 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 21,160,000.00 USD | 971,960.00 USD | 0.00 USD | `+6.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 22,480,000.00 USD | 1,310,000.00 USD | 0.00 USD | `+7.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 22,730,000.00 USD | 257,100.00 USD | 0.00 USD | `+7.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 22,850,000.00 USD | 119,580.00 USD | 0.00 USD | `+8.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 22,910,000.00 USD | 55,560.00 USD | 0.00 USD | `+8.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 24,200,000.00 USD | 1,290,000.00 USD | 0.00 USD | `+9.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 25,580,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 25,820,000.00 USD | 243,540.00 USD | 0.00 USD | `+10.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 28,750,000.00 USD | 2,930,000.00 USD | 0.00 USD | `+10.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 28,940,000.00 USD | 187,200.00 USD | 0.00 USD | `+10.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 29,520,000.00 USD | 575,140.00 USD | 0.00 USD | `+11.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2455.00` | 29,640,000.00 USD | 126,950.00 USD | 0.00 USD | `+11.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 31,830,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+12.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 32,020,000.00 USD | 186,860.00 USD | 0.00 USD | `+12.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 34,120,000.00 USD | 2,100,000.00 USD | 0.00 USD | `+13.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 34,530,000.00 USD | 411,740.00 USD | 0.00 USD | `+13.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 39,450,000.00 USD | 4,920,000.00 USD | 0.00 USD | `+14.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2515.00` | 47,130,000.00 USD | 7,680,000.00 USD | 0.00 USD | `+14.64%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 50,190,000.00 USD | 3,060,000.00 USD | 0.00 USD | `+15.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 50,260,000.00 USD | 63,610.00 USD | 0.00 USD | `+15.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 52,520,000.00 USD | 2,260,000.00 USD | 0.00 USD | `+16.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 52,740,000.00 USD | 222,610.00 USD | 0.00 USD | `+16.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 55,080,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+16.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 55,160,000.00 USD | 78,950.00 USD | 0.00 USD | `+17.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 57,860,000.00 USD | 2,700,000.00 USD | 0.00 USD | `+17.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 57,870,000.00 USD | 11,010.00 USD | 0.00 USD | `+18.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 60,670,000.00 USD | 2,800,000.00 USD | 0.00 USD | `+18.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 60,820,000.00 USD | 145,730.00 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 63,000,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+19.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 63,150,000.00 USD | 147,930.00 USD | 0.00 USD | `+20.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 65,270,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+20.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 65,520,000.00 USD | 251,610.00 USD | 0.00 USD | `+21.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 67,680,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+21.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 67,910,000.00 USD | 230,090.00 USD | 0.00 USD | `+21.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 70,090,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+22.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 70,160,000.00 USD | 76,240.00 USD | 0.00 USD | `+22.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 75,140,000.00 USD | 4,980,000.00 USD | 0.00 USD | `+23.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 75,220,000.00 USD | 76,590.00 USD | 0.00 USD | `+23.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 77,690,000.00 USD | 2,470,000.00 USD | 0.00 USD | `+24.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 77,730,000.00 USD | 43,050.00 USD | 0.00 USD | `+24.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 79,990,000.00 USD | 2,260,000.00 USD | 0.00 USD | `+25.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 80,680,000.00 USD | 685,070.00 USD | 0.00 USD | `+25.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 82,990,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+26.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 83,570,000.00 USD | 577,610.00 USD | 0.00 USD | `+26.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 85,830,000.00 USD | 2,260,000.00 USD | 0.00 USD | `+26.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 85,850,000.00 USD | 17,550.00 USD | 0.00 USD | `+27.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 88,980,000.00 USD | 3,130,000.00 USD | 0.00 USD | `+27.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 89,030,000.00 USD | 52,490.00 USD | 0.00 USD | `+28.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 89,080,000.00 USD | 43,930.00 USD | 0.00 USD | `+28.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 89,360,000.00 USD | 286,140.00 USD | 0.00 USD | `+29.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 90,370,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+29.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 91,750,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+30.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 91,770,000.00 USD | 10,290.00 USD | 0.00 USD | `+30.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 91,770,000.00 USD | 2,460.00 USD | 0.00 USD | `+31.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 92,070,000.00 USD | 305,820.00 USD | 0.00 USD | `+31.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 92,090,000.00 USD | 16,190.00 USD | 0.00 USD | `+31.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 93,570,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+32.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 93,580,000.00 USD | 10,340.00 USD | 0.00 USD | `+32.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 93,590,000.00 USD | 3,050.00 USD | 0.00 USD | `+33.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 93,640,000.00 USD | 52,370.00 USD | 0.00 USD | `+33.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 93,670,000.00 USD | 34,650.00 USD | 0.00 USD | `+34.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 93,710,000.00 USD | 40,710.00 USD | 0.00 USD | `+34.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 93,830,000.00 USD | 113,340.00 USD | 0.00 USD | `+35.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 93,970,000.00 USD | 145,510.00 USD | 0.00 USD | `+35.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 94,150,000.00 USD | 177,120.00 USD | 0.00 USD | `+36.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 96,090,000.00 USD | 1,940,000.00 USD | 0.00 USD | `+36.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 98,830,000.00 USD | 2,740,000.00 USD | 0.00 USD | `+36.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 98,840,000.00 USD | 6,950.00 USD | 0.00 USD | `+37.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 98,870,000.00 USD | 35,380.00 USD | 0.00 USD | `+37.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 98,950,000.00 USD | 74,910.00 USD | 0.00 USD | `+38.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 98,970,000.00 USD | 22,460.00 USD | 0.00 USD | `+38.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 99,740,000.00 USD | 771,720.00 USD | 0.00 USD | `+39.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 99,740,000.00 USD | 612.69 USD | 0.00 USD | `+39.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 99,790,000.00 USD | 49,500.00 USD | 0.00 USD | `+40.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 99,810,000.00 USD | 19,570.00 USD | 0.00 USD | `+40.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 99,810,000.00 USD | 928.50 USD | 0.00 USD | `+41.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 111,580,000.00 USD | 11,770,000.00 USD | 0.00 USD | `+41.53%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 111,710,000.00 USD | 128,280.00 USD | 0.00 USD | `+41.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 112,090,000.00 USD | 381,020.00 USD | 0.00 USD | `+42.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 112,090,000.00 USD | 2,660.00 USD | 0.00 USD | `+43.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 112,150,000.00 USD | 58,930.00 USD | 0.00 USD | `+43.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 112,160,000.00 USD | 9,860.00 USD | 0.00 USD | `+44.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 112,160,000.00 USD | 149.22 USD | 0.00 USD | `+44.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 112,160,000.00 USD | 1,330.00 USD | 0.00 USD | `+45.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 112,200,000.00 USD | 36,550.00 USD | 0.00 USD | `+45.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 112,850,000.00 USD | 653,320.00 USD | 0.00 USD | `+46.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 112,850,000.00 USD | 1,760.00 USD | 0.00 USD | `+46.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 112,860,000.00 USD | 3,740.00 USD | 0.00 USD | `+47.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 112,860,000.00 USD | 167.25 USD | 0.00 USD | `+47.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 112,910,000.00 USD | 56,110.00 USD | 0.00 USD | `+47.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 113,150,000.00 USD | 236,580.00 USD | 0.00 USD | `+48.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 113,170,000.00 USD | 15,710.00 USD | 0.00 USD | `+48.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 113,170,000.00 USD | 1,630.00 USD | 0.00 USD | `+49.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 113,310,000.00 USD | 141,980.00 USD | 0.00 USD | `+49.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 113,330,000.00 USD | 15,350.00 USD | 0.00 USD | `+50.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 114,740,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+50.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 115,130,000.00 USD | 389,970.00 USD | 0.00 USD | `+51.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 115,150,000.00 USD | 18,270.00 USD | 0.00 USD | `+51.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 115,150,000.00 USD | 4,350.00 USD | 0.00 USD | `+52.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 115,150,000.00 USD | 2,170.00 USD | 0.00 USD | `+52.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 115,150,000.00 USD | 837.74 USD | 0.00 USD | `+52.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 115,160,000.00 USD | 2,780.00 USD | 0.00 USD | `+53.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 115,180,000.00 USD | 21,260.00 USD | 0.00 USD | `+53.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 115,240,000.00 USD | 58,010.00 USD | 0.00 USD | `+54.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 115,560,000.00 USD | 322,160.00 USD | 0.00 USD | `+54.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 117,050,000.00 USD | 1,490,000.00 USD | 0.00 USD | `+55.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 117,060,000.00 USD | 5,700.00 USD | 0.00 USD | `+55.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 117,070,000.00 USD | 16,310.00 USD | 0.00 USD | `+56.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 117,090,000.00 USD | 15,030.00 USD | 0.00 USD | `+57.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 117,110,000.00 USD | 18,600.00 USD | 0.00 USD | `+57.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 117,110,000.00 USD | 495.50 USD | 0.00 USD | `+57.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 117,110,000.00 USD | 3,190.00 USD | 0.00 USD | `+58.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 117,150,000.00 USD | 43,610.00 USD | 0.00 USD | `+58.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 117,150,000.00 USD | 158.32 USD | 0.00 USD | `+59.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 117,600,000.00 USD | 444,280.00 USD | 0.00 USD | `+59.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 117,640,000.00 USD | 43,620.00 USD | 0.00 USD | `+60.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 117,650,000.00 USD | 3,690.00 USD | 0.00 USD | `+60.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 117,660,000.00 USD | 9,810.00 USD | 0.00 USD | `+61.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 117,750,000.00 USD | 90,810.00 USD | 0.00 USD | `+62.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 117,750,000.00 USD | 2,300.00 USD | 0.00 USD | `+62.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3575.00` | 117,750,000.00 USD | 2,870.00 USD | 0.00 USD | `+62.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 117,750,000.00 USD | 354.92 USD | 0.00 USD | `+63.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 117,760,000.00 USD | 13,160.00 USD | 0.00 USD | `+63.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 117,870,000.00 USD | 101,080.00 USD | 0.00 USD | `+64.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 117,880,000.00 USD | 10,210.00 USD | 0.00 USD | `+65.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 117,880,000.00 USD | 7,790.00 USD | 0.00 USD | `+65.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 117,890,000.00 USD | 3,860.00 USD | 0.00 USD | `+66.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 117,890,000.00 USD | 820.18 USD | 0.00 USD | `+66.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 117,900,000.00 USD | 8,130.00 USD | 0.00 USD | `+67.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 117,950,000.00 USD | 55,120.00 USD | 0.00 USD | `+67.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 117,950,000.00 USD | 1,410.00 USD | 0.00 USD | `+67.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 117,950,000.00 USD | 819.92 USD | 0.00 USD | `+68.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 117,950,000.00 USD | 323.58 USD | 0.00 USD | `+69.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 117,960,000.00 USD | 1,400.00 USD | 0.00 USD | `+69.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 117,960,000.00 USD | 6,490.00 USD | 0.00 USD | `+70.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3745.00` | 117,960,000.00 USD | 165.90 USD | 0.00 USD | `+70.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 117,960,000.00 USD | 751.00 USD | 0.00 USD | `+71.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 117,960,000.00 USD | 286.90 USD | 0.00 USD | `+72.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 117,960,000.00 USD | 1,560.00 USD | 0.00 USD | `+72.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 118,700,000.00 USD | 734,090.00 USD | 0.00 USD | `+73.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 118,720,000.00 USD | 20,930.00 USD | 0.00 USD | `+73.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 118,730,000.00 USD | 8,380.00 USD | 0.00 USD | `+74.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 118,730,000.00 USD | 711.78 USD | 0.00 USD | `+74.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 118,730,000.00 USD | 355.28 USD | 0.00 USD | `+75.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 118,730,000.00 USD | 5,170.00 USD | 0.00 USD | `+75.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 118,750,000.00 USD | 19,430.00 USD | 0.00 USD | `+77.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 118,770,000.00 USD | 12,120.00 USD | 0.00 USD | `+78.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 119,410,000.00 USD | 646,840.00 USD | 0.00 USD | `+78.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 119,460,000.00 USD | 42,570.00 USD | 0.00 USD | `+79.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 119,510,000.00 USD | 59,170.00 USD | 0.00 USD | `+79.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 119,520,000.00 USD | 1,380.00 USD | 0.00 USD | `+80.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 119,520,000.00 USD | 6,960.00 USD | 0.00 USD | `+81.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 119,540,000.00 USD | 14,610.00 USD | 0.00 USD | `+81.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 119,540,000.00 USD | 4,280.00 USD | 0.00 USD | `+82.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 122,210,000.00 USD | 2,670,000.00 USD | 0.00 USD | `+82.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 122,210,000.00 USD | 898.59 USD | 0.00 USD | `+83.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 122,210,000.00 USD | 811.00 USD | 0.00 USD | `+84.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 122,220,000.00 USD | 4,310.00 USD | 0.00 USD | `+85.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 122,220,000.00 USD | 3,050.00 USD | 0.00 USD | `+86.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 122,260,000.00 USD | 36,740.00 USD | 0.00 USD | `+87.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 122,260,000.00 USD | 5,990.00 USD | 0.00 USD | `+87.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 122,270,000.00 USD | 372.90 USD | 0.00 USD | `+88.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 122,270,000.00 USD | 395.43 USD | 0.00 USD | `+88.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 122,270,000.00 USD | 376.65 USD | 0.00 USD | `+90.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 122,310,000.00 USD | 41,200.00 USD | 0.00 USD | `+91.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 122,310,000.00 USD | 460.70 USD | 0.00 USD | `+92.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 122,310,000.00 USD | 1,270.00 USD | 0.00 USD | `+92.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 122,310,000.00 USD | 4,300.00 USD | 0.00 USD | `+93.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 122,310,000.00 USD | 437.16 USD | 0.00 USD | `+94.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 122,380,000.00 USD | 64,550.00 USD | 0.00 USD | `+94.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 122,380,000.00 USD | 1,610.00 USD | 0.00 USD | `+95.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 122,480,000.00 USD | 97,670.00 USD | 0.00 USD | `+96.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 122,480,000.00 USD | 1,070.00 USD | 0.00 USD | `+96.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 122,490,000.00 USD | 11,270.00 USD | 0.00 USD | `+98.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 122,490,000.00 USD | 2,400.00 USD | 0.00 USD | `+98.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 122,540,000.00 USD | 43,750.00 USD | 0.00 USD | `+99.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 122,600,000.00 USD | 64,570.00 USD | 0.00 USD | `+99.87%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `28.84B` | Total OI Tokens: `13,021,144.3 ETH`
  * 1h OI Change: `+0.38%` | 4h OI Change: `-1.53%` | 24h OI Change: `-2.59%`
  * Exchange Breakdown: Binance=`8.36B` | Bybit=`2.08B` | OKX=`1.78B` | Hyperliquid=`2.34B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-615.06K` | Last 24h: `1.05M` | Last 3d: `6.29M` | Last 7d: `12.86M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0031%` | **USDT OKX** | `-0.0079%` |
| **USDT Bybit** | `-0.0184%` | **USDT KuCoin** | `-0.0165%` |
| **USDT MEXC** | `-0.0032%` | **USDT BingX** | `0.0003%` |
| **USDT Gate** | `-0.0107%` | **USDT Bitget** | `0.0002%` |
| **CoinM Binance** | `0.0039%` | **CoinM OKX** | `-0.0002%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `61.80%` | `38.20%` | `1.62` | 1,260,000,000.00 USD |
| `15M` | `Binance` | `54.97%` | `45.03%` | `1.22` | 357,670,000.00 USD |
| `15M` | `OKX` | `54.27%` | `45.73%` | `1.19` | 144,460,000.00 USD |
| `15M` | `Bybit` | `63.86%` | `36.14%` | `1.77` | 125,740,000.00 USD |
| `15M` | `KuCoin` | `87.81%` | `12.19%` | `7.20` | 6,650,000.00 USD |
| `15M` | `Gate` | `45.89%` | `54.11%` | `0.85` | 110,460,000.00 USD |
| `15M` | `Bitget` | `52.17%` | `47.83%` | `1.09` | 47,620,000.00 USD |
| `15M` | `BingX` | `52.19%` | `47.81%` | `1.09` | 17,620,000.00 USD |
| `15M` | `MEXC` | `54.9%` | `45.1%` | `1.22` | 46,830,000.00 USD |
| `15M` | `Bitunix` | `51.99%` | `48.01%` | `1.08` | 45,150,000.00 USD |
| `15M` | `Hyperliquid` | `69.06%` | `30.94%` | `2.23` | 65,960,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `62.06%` | `37.94%` | `1.64` | 4,470,000.00 USD |
| `15M` | `Crypto.com` | `48.65%` | `51.35%` | `0.95` | 3,460,000.00 USD |
| `15M` | `WhiteBIT` | `98.65%` | `1.35%` | `73.07` | 196,430,000.00 USD |
| `15M` | `HTX` | `53.88%` | `46.12%` | `1.17` | 3,710,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `40.76%` | `59.24%` | `0.69` | 48,360,000.00 USD |
| `15M` | `Bitfinex` | `81.33%` | `18.67%` | `4.36` | 630,850.00 USD |
| `15M` | `Kraken` | `58.25%` | `41.75%` | `1.40` | 55,440.00 USD |
| `15M` | `Aster` | `52.16%` | `47.84%` | `1.09` | 17,830,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `46.05%` | `53.95%` | `0.85` | 14,030,000.00 USD |
| `15M` | `Whale Positions` | `54.97%` | `45.03%` | `1.22` | 357,670,000.00 USD |
| `15M` | `Global Accounts` | `61.80%` | `38.20%` | `1.62` | 1,260,000,000.00 USD |
| `1H` | `ETH` | `52.44%` | `47.56%` | `1.10` | 5,320,000,000.00 USD |
| `1H` | `Binance` | `51.22%` | `48.78%` | `1.05` | 1,610,000,000.00 USD |
| `1H` | `OKX` | `49.44%` | `50.56%` | `0.98` | 694,230,000.00 USD |
| `1H` | `Bybit` | `52.19%` | `47.81%` | `1.09` | 495,930,000.00 USD |
| `1H` | `KuCoin` | `59.96%` | `40.04%` | `1.50` | 16,450,000.00 USD |
| `1H` | `Gate` | `48.89%` | `51.11%` | `0.96` | 606,050,000.00 USD |
| `1H` | `Bitget` | `48.24%` | `51.76%` | `0.93` | 226,930,000.00 USD |
| `1H` | `BingX` | `47.71%` | `52.29%` | `0.91` | 70,710,000.00 USD |
| `1H` | `MEXC` | `51.3%` | `48.7%` | `1.05` | 210,340,000.00 USD |
| `1H` | `Bitunix` | `50.48%` | `49.52%` | `1.02` | 236,540,000.00 USD |
| `1H` | `Hyperliquid` | `57.46%` | `42.54%` | `1.35` | 357,600,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.03%` | `47.97%` | `1.08` | 22,490,000.00 USD |
| `1H` | `Crypto.com` | `49.7%` | `50.3%` | `0.99` | 17,300,000.00 USD |
| `1H` | `WhiteBIT` | `72.02%` | `27.98%` | `2.57` | 428,490,000.00 USD |
| `1H` | `HTX` | `48.5%` | `51.5%` | `0.94` | 22,890,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `45.48%` | `54.52%` | `0.83` | 181,570,000.00 USD |
| `1H` | `Bitfinex` | `58.2%` | `41.8%` | `1.39` | 4,620,000.00 USD |
| `1H` | `Kraken` | `49.86%` | `50.14%` | `0.99` | 15,560,000.00 USD |
| `1H` | `Aster` | `47.87%` | `52.13%` | `0.92` | 54,830,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `46.51%` | `53.49%` | `0.87` | 53,300,000.00 USD |
| `1H` | `Whale Positions` | `51.22%` | `48.78%` | `1.05` | 1,610,000,000.00 USD |
| `1H` | `Global Accounts` | `52.44%` | `47.56%` | `1.10` | 5,320,000,000.00 USD |
| `4H` | `ETH` | `49.06%` | `50.94%` | `0.96` | 19,380,000,000.00 USD |
| `4H` | `Binance` | `46.35%` | `53.65%` | `0.86` | 5,740,000,000.00 USD |
| `4H` | `OKX` | `46.97%` | `53.03%` | `0.89` | 3,380,000,000.00 USD |
| `4H` | `Bybit` | `48.73%` | `51.27%` | `0.95` | 1,290,000,000.00 USD |
| `4H` | `KuCoin` | `57.32%` | `42.68%` | `1.34` | 223,690,000.00 USD |
| `4H` | `Gate` | `47.38%` | `52.62%` | `0.90` | 1,900,000,000.00 USD |
| `4H` | `Bitget` | `49.36%` | `50.64%` | `0.97` | 722,980,000.00 USD |
| `4H` | `BingX` | `49.5%` | `50.5%` | `0.98` | 164,380,000.00 USD |
| `4H` | `MEXC` | `47.68%` | `52.32%` | `0.91` | 607,030,000.00 USD |
| `4H` | `Bitunix` | `49.68%` | `50.32%` | `0.99` | 643,820,000.00 USD |
| `4H` | `Hyperliquid` | `48.18%` | `51.82%` | `0.93` | 861,290,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `55.1%` | `44.9%` | `1.23` | 61,710,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `57.77%` | `42.23%` | `1.37` | 3,080,000,000.00 USD |
| `4H` | `HTX` | `52.39%` | `47.61%` | `1.10` | 151,830,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.33%` | `48.67%` | `1.05` | 123,930,000.00 USD |
| `4H` | `Bitfinex` | `26.96%` | `73.04%` | `0.37` | 13,770,000.00 USD |
| `4H` | `Kraken` | `38.72%` | `61.28%` | `0.63` | 62,950,000.00 USD |
| `4H` | `Aster` | `46.31%` | `53.69%` | `0.86` | 170,700,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `42.43%` | `57.57%` | `0.74` | 188,020,000.00 USD |
| `4H` | `Whale Positions` | `46.35%` | `53.65%` | `0.86` | 5,740,000,000.00 USD |
| `4H` | `Global Accounts` | `49.06%` | `50.94%` | `0.96` | 19,380,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2199.25` | `2214.79` | `2199.25` | `2247.25` | `2199.25` | 968,245,119.65 USD | 394,095,796.43 USD | 574,149,323.23 USD | -180,053,526.80 USD | `-18.60%` | `3B / 16S` |
| `0:00 UTC` | `2209.75` | `2208.25` | `2209.75` | `2219.25` | `2196.25` | 403,830,463.07 USD | 203,436,508.93 USD | 200,393,954.14 USD | 3,042,554.80 USD | `+0.75%` | `3B / 4S` |
| `5:00 UTC` | `2220.75` | `2216.89` | `2220.75` | `2225.75` | `2206.25` | 183,066,195.52 USD | 88,383,369.64 USD | 94,682,825.87 USD | -6,299,456.23 USD | `-3.44%` | `0B / 2S` |
| `0:00 UTC` | `2214.25` | `2218.08` | `2214.25` | `2227.75` | `2210.25` | 141,329,048.77 USD | 65,222,449.86 USD | 76,106,598.91 USD | -10,884,149.05 USD | `-7.70%` | `2B / 1S` |
| `5:00 UTC` | `2205.25` | `2210.00` | `2205.25` | `2224.25` | `2202.75` | 274,097,559.83 USD | 122,676,431.99 USD | 151,421,127.83 USD | -28,744,695.84 USD | `-10.49%` | `1B / 6S` |
| `0:00 UTC` | `2180.25` | `2189.30` | `2180.25` | `2210.25` | `2172.75` | 713,753,253.85 USD | 330,298,360.51 USD | 383,454,893.33 USD | -53,156,532.82 USD | `-7.45%` | `1B / 5S` |
| `5:00 UTC` | `2192.25` | `2195.11` | `2192.25` | `2205.75` | `2188.75` | 213,150,561.59 USD | 86,554,765.83 USD | 126,595,795.76 USD | -40,041,029.93 USD | `-18.79%` | `1B / 5S` |
| `0:00 UTC` | `2190.25` | `2193.00` | `2190.25` | `2205.25` | `2181.25` | 206,705,717.00 USD | 113,660,029.38 USD | 93,045,687.62 USD | 20,614,341.75 USD | `+9.97%` | `2B / 2S` |
| `5:00 UTC` | `2214.75` | `2211.66` | `2214.75` | `2217.25` | `2204.25` | 218,308,818.86 USD | 130,467,599.52 USD | 87,841,219.34 USD | 42,626,380.18 USD | `+19.53%` | `6B / 1S` |
| `0:00 UTC` | `2217.25` | `2215.26` | `2217.25` | `2218.75` | `2209.75` | 79,588,826.91 USD | 41,166,064.52 USD | 38,422,762.39 USD | 2,743,302.13 USD | `+3.45%` | `0B / 3S` |

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
| `5m` | -1,360,000.00 USD | 20,380,000.00 USD | **`ACCUMULATION`** |
| `15m` | -74,710.00 USD | 14,800,000.00 USD | **`ACCUMULATION`** |
| `30m` | 9,930,000.00 USD | 111,190,000.00 USD | **`ACCUMULATION`** |
| `1h` | 2,810,000.00 USD | 30,740,000.00 USD | **`ACCUMULATION`** |
| `2h` | -32,740,000.00 USD | -204,530,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -67,380,000.00 USD | -670,780,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -103,990,000.00 USD | -1,320,000,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -159,210,000.00 USD | -1,980,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -152,130,000.00 USD | -2,120,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -129,970,000.00 USD | -1,930,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -200,950,000.00 USD | -3,270,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,160,000,000.00 USD | -9,780,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.36M` | 15m=`-74.71K` | 1h=`+2.81M` | 24h=`-129.97M`
* Futures Capital Netflows: 5m=`+20.38M` | 15m=`+14.80M` | 1h=`+30.74M` | 24h=`-1.93B`
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
  * `2026-10-30 08:00:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:15:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:08:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:09:46 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [morningstar.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `2177.43` (Risk Distance: `29.52` pts)
  * +2.5R Take Profit: `2280.75`
  * Mathematical Lot Sizing: **`0.33 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2288.70` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2318.22` (Risk Distance: `29.52` pts)
  * +2.5R Take Profit: `2214.90`
  * Mathematical Lot Sizing: **`0.33 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2229.29`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
