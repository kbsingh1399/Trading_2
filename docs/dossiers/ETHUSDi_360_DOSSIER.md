# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 15:09:00 IST` (`2026-10-30 09:39:00 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2219.90` | **Live Ask Quote**: `2222.90` | **Mid Price**: `2221.40`
- **Spread Points**: `300.00` | **Spread BPS**: `13.50 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2219.79` | VWAP Z-Score: `+0.13` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `11.89` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `42.59` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2269.36` | Lower -3.00σ Band: `2170.22`
  * Upper +2.51σ Band: `2261.27` | Lower -2.51σ Band: `2178.32`
  * Upper +2.01σ Band: `2253.00` | Lower -2.01σ Band: `2186.58`
  * Upper +2.00σ Band: `2252.84` | Lower -2.00σ Band: `2186.74`
  * Upper +1.28σ Band: `2240.94` | Lower -1.28σ Band: `2198.64`
  * Upper +1.00σ Band: `2236.31` | Lower -1.00σ Band: `2203.27`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2225.63` | EMA-20=`2229.53` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2243.36` (Slope: `+0.0000`) | EMA-100=`2267.11`
  * Institutional Anchors: EMA-144=`2280.79` | EMA-200=`2293.11` (Slope: `-0.3492`) | EMA-233=`2298.15`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2252.28` (Distance: `-1.38%`)
  * Point of Control (POC) = `2241.75` (Distance: `-0.92%`)
  * Value Area Low (VAL) = `2194.00` (Distance: `+1.24%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2354.78` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2251.30` | Low=`2215.10`
  * New York Session (13:00-21:00 UTC): High=`2234.73` | Low=`2208.07`
  * Initial Balance (First Hour): IB High=`2246.50` | IB Low=`2230.60`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2212.51` - `2230.29`
  * Optimal Trade Entry (OTE 0.705): `2225.84`
  * Structural Invalidation Anchor (0.786): `2239.17`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2223.83` | `2224.93` | `2220.44` | `2221.91` | `9,846` | 21,882,945.47 USD | -3,443,250.75 USD | `-15.73%` | -974,819,379.15 USD | `-0.32` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `2221.90` | `2225.85` | `2221.90` | `2225.84` | `10,401` | 23,122,783.18 USD | 11,340,220.40 USD | `+49.04%` | -963,479,158.74 USD | `+1.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `2225.85` | `2225.86` | `2223.84` | `2223.86` | `1,831` | 4,074,437.19 USD | 1,158,506.71 USD | `+28.43%` | -962,320,652.03 USD | `+0.25` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `2227.92` | `2229.91` | `2221.24` | `2223.00` | `29,601` | 65,855,959.19 USD | -5,333,544.98 USD | `-8.10%` | -969,562,933.12 USD | `-0.30` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `2223.00` | `2226.00` | `2220.44` | `2225.84` | `32,324` | 71,858,619.15 USD | 5,514,896.63 USD | `+7.67%` | -964,048,036.48 USD | `+0.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `2225.85` | `2225.86` | `2223.84` | `2223.85` | `1,775` | 3,950,192.41 USD | 1,056,331.42 USD | `+26.74%` | -962,991,705.07 USD | `+0.08` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `2252.91` | `2253.96` | `2228.21` | `2235.54` | `253,701` | 568,308,333.87 USD | -3,920,812.04 USD | `-0.69%` | -926,664,438.18 USD | `+0.36` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `2235.54` | `2236.80` | `2223.18` | `2227.93` | `164,265` | 366,023,334.59 USD | -37,825,356.97 USD | `-10.33%` | -964,489,795.15 USD | `+0.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2227.92` | `2229.91` | `2220.44` | `2223.86` | `63,702` | 141,667,497.21 USD | 1,240,409.53 USD | `+0.88%` | -963,249,385.62 USD | `+0.42` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2236.80` | `2220.44` | `2223.86` | `227,972` | 507,703,062.98 USD | -36,594,683.45 USD | `-7.21%` | -924,460,751.90 USD | `+0.54` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -98,115,944.70 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -652,353,514.01 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2236.80` | `2220.44` | `2223.86` | `227,972` | 507,703,062.98 USD | -36,594,683.45 USD | `-7.21%` | -924,460,751.90 USD | `+0.54` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2221.40`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2221.90` | `442.8967` | 984,072.18 USD | 8,079,877.56 USD | `11 orders` | `-0.09%` | `-` |
| `BID` | `2222.00` | `186.7010` | 414,849.62 USD | 7,095,805.39 USD | `12 orders` | `-0.08%` | `-` |
| `BID` | `2222.10` | `388.1781` | 862,570.56 USD | 6,680,955.76 USD | `9 orders` | `-0.08%` | `-` |
| `BID` | `2222.20` | `53.1311` | 118,067.93 USD | 5,818,385.21 USD | `5 orders` | `-0.07%` | `-` |
| `BID` | `2222.30` | `331.5299` | 736,758.90 USD | 5,700,317.28 USD | `13 orders` | `-0.07%` | `-` |
| `BID` | `2222.40` | `86.0335` | 191,200.85 USD | 4,963,558.38 USD | `9 orders` | `-0.07%` | `-` |
| `BID` | `2222.50` | `272.1395` | 604,830.04 USD | 4,772,357.53 USD | `10 orders` | `-0.06%` | `-` |
| `BID` | `2222.60` | `325.2423` | 722,883.54 USD | 4,167,527.49 USD | `9 orders` | `-0.06%` | `-` |
| `BID` | `2222.70` | `496.1039` | 1,102,690.14 USD | 3,444,643.96 USD | `15 orders` | `-0.05%` | `-` |
| `BID` | `2222.80` | `310.5426` | 690,274.09 USD | 2,341,953.82 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `2222.90` | `73.8211` | 164,096.92 USD | 1,651,679.73 USD | `12 orders` | `-0.04%` | `-` |
| `BID` | `2223.00` | `48.7013` | 108,262.99 USD | 1,487,582.80 USD | `8 orders` | `-0.04%` | `-` |
| `BID` | `2223.10` | `148.7509` | 330,688.13 USD | 1,379,319.81 USD | `13 orders` | `-0.03%` | `-` |
| `BID` | `2223.20` | `100.4208` | 223,255.52 USD | 1,048,631.69 USD | `7 orders` | `-0.03%` | `-` |
| `BID` | `2223.30` | `123.5738` | 274,741.63 USD | 825,376.16 USD | `9 orders` | `-0.02%` | `-` |
| `BID` | `2223.40` | `54.2797` | 120,685.48 USD | 550,634.54 USD | `8 orders` | `-0.02%` | `-` |
| `BID` | `2223.50` | `48.8368` | 108,588.62 USD | 429,949.05 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `2223.60` | `59.9326` | 133,266.13 USD | 321,360.43 USD | `7 orders` | `-0.01%` | `-` |
| `BID` | `2223.70` | `36.0300` | 80,119.91 USD | 188,094.30 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `2223.80` | `48.5540` | 107,974.39 USD | 107,974.39 USD | `8 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2223.85` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,223.85` | `0.00%` | `-` |
| `ASK` | `2223.90` | `433.8099` | 964,749.84 USD | 964,749.84 USD | `21 orders` | `+0.00%` | `-` |
| `ASK` | `2224.00` | `66.7297` | 148,406.85 USD | 1,113,156.69 USD | `10 orders` | `+0.01%` | `-` |
| `ASK` | `2224.10` | `312.8411` | 695,789.89 USD | 1,808,946.58 USD | `13 orders` | `+0.01%` | `-` |
| `ASK` | `2224.20` | `67.2316` | 149,536.52 USD | 1,958,483.10 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `2224.30` | `174.9503` | 389,141.95 USD | 2,347,625.06 USD | `12 orders` | `+0.02%` | `-` |
| `ASK` | `2224.40` | `283.4320` | 630,466.14 USD | 2,978,091.20 USD | `9 orders` | `+0.02%` | `-` |
| `ASK` | `2224.50` | `273.4062` | 608,192.09 USD | 3,586,283.29 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `2224.60` | `260.6150` | 579,764.13 USD | 4,166,047.42 USD | `8 orders` | `+0.03%` | `-` |
| `ASK` | `2224.70` | `381.0203` | 847,655.86 USD | 5,013,703.28 USD | `14 orders` | `+0.04%` | `-` |
| `ASK` | `2224.80` | `284.3543` | 632,631.45 USD | 5,646,334.73 USD | `10 orders` | `+0.04%` | `-` |
| `ASK` | `2224.90` | `81.2524` | 180,778.46 USD | 5,827,113.19 USD | `10 orders` | `+0.05%` | `-` |
| `ASK` | `2225.00` | `206.3595` | 459,149.89 USD | 6,286,263.08 USD | `13 orders` | `+0.05%` | `-` |
| `ASK` | `2225.10` | `126.7353` | 281,998.72 USD | 6,568,261.79 USD | `18 orders` | `+0.06%` | `-` |
| `ASK` | `2225.20` | `134.9157` | 300,214.42 USD | 6,868,476.21 USD | `10 orders` | `+0.06%` | `-` |
| `ASK` | `2225.30` | `240.3598` | 534,872.66 USD | 7,403,348.87 USD | `15 orders` | `+0.07%` | `-` |
| `ASK` | `2225.40` | `416.7081` | 927,342.21 USD | 8,330,691.08 USD | `20 orders` | `+0.07%` | `-` |
| `ASK` | `2225.50` | `113.3946` | 252,359.68 USD | 8,583,050.76 USD | `12 orders` | `+0.07%` | `-` |
| `ASK` | `2225.60` | `124.9405` | 278,067.58 USD | 8,861,118.34 USD | `13 orders` | `+0.08%` | `-` |
| `ASK` | `2225.70` | `480.4809` | 1,069,406.34 USD | 9,930,524.68 USD | `10 orders` | `+0.08%` | `-` |
| `ASK` | `2225.80` | `85.6298` | 190,594.81 USD | 10,121,119.49 USD | `8 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:01:34 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1786.14` | `30,282.40` | 54,088,732.77 USD | `AT_RISK_LIQ` | `0xde8d9e530b` | `2026-10-30 15:01:34 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1843.94` | `7,964.66` | 14,686,315.60 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 15:01:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 15:01:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `10,000.00` | 19,261,000.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 15:01:34 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1929.22` | `8,092.45` | 15,612,143.31 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 15:01:34 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2121.88` | `30,641.99` | 65,018,755.10 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 15:01:34 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.16` | `26,025.05` | 55,411,549.64 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 15:01:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,533.33` | 7,684,999.71 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2186.30` | `2,062.67` | 4,509,624.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2191.10` | `500.00` | 1,095,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2193.90` | `4,250.16` | 9,324,427.12 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:01:34 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2195.00` | `839.60` | 1,842,926.39 USD | `TRIGGER_STOP` | `0x28280399d9` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2196.90` | `1,466.77` | 3,222,355.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2200.20` | `361.20` | 794,719.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2200.30` | `346.28` | 761,925.60 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.00` | `566.99` | 1,247,952.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9362ca4dfd` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.10` | `500.00` | 1,100,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2203.10` | `500.00` | 1,101,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xf929122994` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2205.00` | `430.01` | 948,176.90 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2205.80` | `1,004.51` | 2,215,742.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2206.80` | `244.00` | 538,459.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x24fb652303` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2207.40` | `266.00` | 587,168.40 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x24fb652303` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2208.20` | `2,192.19` | 4,840,789.10 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.10` | `500.00` | 1,105,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.10` | `500.00` | 1,105,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xf929122994` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2212.30` | `708.71` | 1,567,870.95 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2212.40` | `1,810.78` | 4,006,161.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2212.70` | `344.01` | 761,190.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2213.90` | `351.79` | 778,829.21 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2214.10` | `1,356.98` | 3,004,484.10 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2215.10` | `1,118.61` | 2,477,830.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2215.90` | `903.91` | 2,002,984.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2217.80` | `475.96` | 1,055,587.19 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2218.60` | `677.06` | 1,502,127.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:01:34 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2219.00` | `439.90` | 976,147.64 USD | `TRIGGER_STOP` | `0x369fd6445f` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2219.40` | `350.80` | 778,573.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2219.70` | `451.16` | 1,001,441.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2220.70` | `338.22` | 751,088.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.40` | `247.95` | 550,803.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2224.10` | `247.67` | 550,833.95 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2225.00` | `337.59` | 751,129.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2225.60` | `345.07` | 767,989.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2226.20` | `449.88` | 1,001,528.87 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2228.20` | `674.20` | 1,502,259.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2230.10` | `898.18` | 2,003,032.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2230.70` | `471.15` | 1,050,986.05 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2231.30` | `344.01` | 767,589.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2231.50` | `341.93` | 763,018.36 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2232.20` | `1,118.46` | 2,496,634.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2233.70` | `1,345.12` | 3,004,599.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2235.20` | `691.64` | 1,545,955.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2236.00` | `1,791.66` | 4,006,141.25 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2239.10` | `430.01` | 962,840.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2239.70` | `2,192.19` | 4,909,843.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2241.20` | `1,029.66` | 2,307,674.44 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.10` | `339.52` | 761,925.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.20` | `354.12` | 794,719.92 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2249.80` | `1,366.81` | 3,075,043.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2254.00` | `4,250.16` | 9,579,861.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:01:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2261.20` | `2,114.32` | 4,780,897.44 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:01:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2300.00` | `4,002.10` | 9,204,832.99 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 15:01:34 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2468.87` | `22,046.99` | 54,431,199.08 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 15:01:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,002.39` | 7,547,704.95 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 15:01:34 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2623.92` | `10,000.00` | 26,239,195.38 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 15:01:34 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2657.77` | `9,700.00` | 25,780,366.97 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 15:01:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 228,188,037.14 USD | `102,676.40` | `2322.74` | `2221.50` | `3723.65` | 10,302,876.01 USD | `+4.52%` | `5X Cross` |
| `5` | `0xb83d...6e36` | `SHORT` | 110,188,740.62 USD | `49,580.97` | `2375.30` | `2221.50` | `4630.76` | 7,581,252.03 USD | `+6.88%` | `5X Cross` |
| `9` | `0x77dd...e0e9` | `LONG` | 68,114,083.35 USD | `30,641.99` | `2610.31` | `2221.50` | `2121.80` | -11,871,091.69 USD | `-17.43%` | `10X Cross` |
| `11` | `0xde8d...9524` | `LONG` | 67,341,100.43 USD | `30,282.40` | `2134.45` | `2221.50` | `1786.06` | 2,704,769.86 USD | `+4.02%` | `20X Cross` |
| `15` | `0x0392...d7d9` | `LONG` | 57,871,906.13 USD | `26,025.05` | `2518.71` | `2221.50` | `2129.08` | -7,677,815.96 USD | `-13.27%` | `9X Cross` |
| `22` | `0x8add...7d2c` | `SHORT` | 49,030,298.39 USD | `22,046.99` | `2271.09` | `2221.50` | `2476.32` | 1,040,598.91 USD | `+2.12%` | `25X Cross` |
| `25` | `0x15a4...dfdb` | `SHORT` | 44,506,000.00 USD | `20,000.00` | `2228.11` | `2221.50` | `3187.77` | 56,327.68 USD | `+0.13%` | `20X Cross` |
| `27` | `0xdf95...7d72` | `SHORT` | 43,817,657.58 USD | `19,716.37` | `2402.53` | `2221.50` | `4237.53` | 3,551,599.51 USD | `+8.11%` | `25X Cross` |
| `33` | `0x6046...b21d` | `LONG` | 35,419,773.97 USD | `15,927.59` | `2410.19` | `2221.50` | `1785.44` | -2,968,845.67 USD | `-8.38%` | `6X Cross` |
| `35` | `0xefe4...194b` | `SHORT` | 33,578,002.91 USD | `15,108.89` | `2250.33` | `2221.50` | `2927.63` | 422,013.84 USD | `+1.26%` | `20X Cross` |
| `37` | `0xb695...a92d` | `SHORT` | 32,889,430.44 USD | `14,795.73` | `2557.74` | `2221.50` | `3782.80` | 4,954,283.67 USD | `+15.06%` | `20X Cross` |
| `38` | `0xeced...6210` | `SHORT` | 32,641,669.57 USD | `14,687.58` | `2522.09` | `2221.50` | `3647.64` | 4,401,847.97 USD | `+13.49%` | `20X Cross` |
| `40` | `0x45d2...4029` | `SHORT` | 31,009,455.00 USD | `13,950.00` | `2443.60` | `2221.50` | `5377.68` | 3,078,827.46 USD | `+9.93%` | `20X Cross` |
| `42` | `0xa61c...66b9` | `LONG` | 28,660,334.40 USD | `12,888.00` | `2369.69` | `2221.50` | `1478.06` | -1,880,320.14 USD | `-6.56%` | `10X Cross` |
| `45` | `0x2371...0883` | `LONG` | 26,667,600.00 USD | `12,000.00` | `2421.77` | `2221.50` | `1279.04` | -2,393,694.85 USD | `-8.98%` | `20X Cross` |
| `46` | `0xbd1c...ff0e` | `LONG` | 26,644,800.00 USD | `12,000.00` | `2419.91` | `2221.50` | `1519.94` | -2,394,232.39 USD | `-8.99%` | `20X Cross` |
| `52` | `0x6c93...59a4` | `LONG` | 24,462,900.00 USD | `11,000.00` | `2441.15` | `2221.50` | `1601.97` | -2,389,772.73 USD | `-9.77%` | `20X Cross` |
| `53` | `0x0c5d...36b3` | `LONG` | 24,460,700.00 USD | `11,000.00` | `2482.20` | `2221.50` | `1644.01` | -2,843,553.24 USD | `-11.62%` | `20X Cross` |
| `54` | `0x09dc...c094` | `LONG` | 24,448,600.00 USD | `11,000.00` | `2465.31` | `2221.50` | `1637.01` | -2,669,823.04 USD | `-10.92%` | `20X Cross` |
| `55` | `0xa9de...e049` | `LONG` | 24,445,300.00 USD | `11,000.00` | `2481.81` | `2221.50` | `1643.68` | -2,854,679.46 USD | `-11.68%` | `20X Cross` |
| `69` | `0xa2ce...3126` | `LONG` | 22,244,474.76 USD | `10,016.88` | `2162.83` | `2221.50` | `1563.11` | 579,672.71 USD | `+2.61%` | `10X Cross` |
| `70` | `0xec7f...df39` | `LONG` | 22,239,000.00 USD | `10,000.00` | `2719.35` | `2221.50` | `1720.53` | -4,954,548.52 USD | `-22.28%` | `20X Cross` |
| `71` | `0xb37f...66ca` | `SHORT` | 22,224,000.00 USD | `10,000.00` | `2290.69` | `2221.50` | `2623.84` | 682,991.85 USD | `+3.07%` | `25X Cross` |
| `72` | `0x6646...6de5` | `LONG` | 22,204,000.00 USD | `10,000.00` | `1765.80` | `2221.50` | `1718.87` | 4,545,942.55 USD | `+20.47%` | `25X Cross` |
| `74` | `0x939f...04d2` | `LONG` | 21,831,459.41 USD | `9,823.81` | `2427.28` | `2221.50` | `1706.86` | -2,013,691.19 USD | `-9.22%` | `25X Cross` |
| `77` | `0xaeaa...2416` | `SHORT` | 21,570,860.00 USD | `9,700.00` | `2311.92` | `2221.50` | `2657.69` | 854,822.40 USD | `+3.96%` | `25X Cross` |
| `80` | `0xecb6...2b00` | `SHORT` | 21,253,040.11 USD | `9,563.10` | `2240.66` | `2221.50` | `5536.12` | 174,680.32 USD | `+0.82%` | `15X Cross` |
| `85` | `0xf517...c032` | `SHORT` | 20,725,941.16 USD | `9,326.35` | `2202.91` | `2221.50` | `3111.82` | -180,802.95 USD | `-0.87%` | `25X Cross` |
| `86` | `0xca49...53c8` | `SHORT` | 20,387,461.67 USD | `9,181.89` | `2549.39` | `2221.50` | `3903.16` | 3,020,815.72 USD | `+14.82%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 20,134,556.73 USD | `9,054.12` | `2493.89` | `2221.50` | `2775.66` | 2,445,450.53 USD | `+12.15%` | `20X Cross` |
| `89` | `0xea00...a918` | `LONG` | 20,022,438.81 USD | `9,003.83` | `2003.01` | `2221.50` | `1434.15` | 1,987,659.95 USD | `+9.93%` | `5X Cross` |
| `114` | `0x9eec...daab` | `LONG` | 17,984,665.55 USD | `8,092.45` | `1658.44` | `2221.50` | `1930.43` | 4,563,801.02 USD | `+25.38%` | `15X Cross` |
| `115` | `0x5f91...65aa` | `LONG` | 17,711,562.85 USD | `7,964.66` | `1626.99` | `2221.50` | `1843.86` | 4,753,119.79 USD | `+26.84%` | `16X Cross` |
| `125` | `0xec0b...b078` | `LONG` | 15,584,643.97 USD | `7,007.80` | `2065.97` | `2221.50` | `1057.68` | 1,106,714.38 USD | `+7.10%` | `25X Cross` |
| `130` | `0xf02d...5eb3` | `LONG` | 15,247,026.15 USD | `6,855.99` | `2383.33` | `2221.50` | `1129.63` | -1,093,062.61 USD | `-7.17%` | `20X Cross` |
| `132` | `0xcf53...ee11` | `SHORT` | 15,108,816.48 USD | `6,803.63` | `1862.69` | `2221.50` | `4198.99` | -2,435,711.09 USD | `-16.12%` | `7X Cross` |
| `136` | `0x4ff9...38d3` | `LONG` | 14,588,052.95 USD | `6,564.10` | `2447.40` | `2221.50` | `1669.63` | -1,476,969.79 USD | `-10.12%` | `3X Isolated` |
| `138` | `0x1ee7...edf5` | `LONG` | 14,454,505.00 USD | `6,500.00` | `2301.55` | `2221.50` | `2068.84` | -505,588.66 USD | `-3.50%` | `25X Cross` |
| `139` | `0xf78c...c581` | `LONG` | 14,445,442.24 USD | `6,500.22` | `2521.53` | `2221.50` | `1913.11` | -1,945,098.71 USD | `-13.47%` | `20X Cross` |
| `143` | `0x799f...5f4c` | `LONG` | 14,024,720.40 USD | `6,310.90` | `2390.33` | `2221.50` | `1870.61` | -1,060,444.21 USD | `-7.56%` | `20X Cross` |
| `148` | `0x08bf...7872` | `SHORT` | 13,831,700.54 USD | `6,224.05` | `2258.00` | `2221.50` | `2584.91` | 222,215.57 USD | `+1.61%` | `20X Cross` |
| `150` | `0xec4a...cf62` | `LONG` | 13,713,970.90 USD | `6,166.63` | `2225.41` | `2221.50` | `1959.60` | -9,348.53 USD | `-0.07%` | `25X Cross` |
| `152` | `0x524e...0de0` | `LONG` | 13,342,800.00 USD | `6,000.00` | `2246.48` | `2221.50` | `2002.81` | -136,085.04 USD | `-1.02%` | `10X Cross` |
| `153` | `0xd9e7...4aff` | `LONG` | 13,333,800.00 USD | `6,000.00` | `2480.18` | `2221.50` | `1407.40` | -1,547,324.33 USD | `-11.60%` | `20X Cross` |
| `155` | `0xc179...e0c8` | `LONG` | 13,011,553.29 USD | `5,854.73` | `2294.94` | `2221.50` | `1178.39` | -424,718.89 USD | `-3.26%` | `10X Cross` |
| `163` | `0x0c4a...1b19` | `LONG` | 12,580,132.70 USD | `5,660.10` | `2373.06` | `2221.50` | `2081.45` | -851,625.43 USD | `-6.77%` | `25X Isolated` |
| `168` | `0x7fda...17d1` | `LONG` | 11,813,741.91 USD | `5,315.76` | `2211.05` | `2221.50` | `0.000000` | 60,299.67 USD | `+0.51%` | `25X Cross` |
| `186` | `0x45ab...6cbc` | `LONG` | 10,943,088.11 USD | `4,920.96` | `2727.66` | `2221.50` | `1381.28` | -2,479,655.69 USD | `-22.66%` | `7X Cross` |
| `190` | `0x64b7...9da9` | `LONG` | 10,800,639.01 USD | `4,856.84` | `2604.61` | `2221.50` | `601.65` | -1,849,575.40 USD | `-17.12%` | `25X Cross` |
| `197` | `0xfb18...eb17` | `SHORT` | 10,587,223.80 USD | `4,768.16` | `2315.53` | `2221.50` | `2625.12` | 453,605.90 USD | `+4.28%` | `25X Cross` |
| `198` | `0x5559...d43b` | `SHORT` | 10,569,092.79 USD | `4,755.93` | `2262.69` | `2221.50` | `2743.97` | 192,113.08 USD | `+1.82%` | `25X Cross` |
| `210` | `0xe091...6705` | `SHORT` | 10,006,650.44 USD | `4,500.00` | `2467.33` | `2221.50` | `2463.03` | 1,096,358.06 USD | `+10.96%` | `20X Cross` |
| `211` | `0x418a...8888` | `SHORT` | 10,001,700.00 USD | `4,500.00` | `2494.55` | `2221.50` | `2994.12` | 1,223,784.41 USD | `+12.24%` | `25X Cross` |
| `218` | `0xb829...3a81` | `LONG` | 9,768,129.19 USD | `4,394.91` | `2398.60` | `2221.50` | `1455.16` | -773,512.76 USD | `-7.92%` | `20X Cross` |
| `236` | `0x28bb...fca6` | `SHORT` | 9,355,025.64 USD | `4,209.61` | `1896.10` | `2221.50` | `3035.08` | -1,373,143.07 USD | `-14.68%` | `20X Cross` |
| `238` | `0x6ea4...0ea7` | `SHORT` | 9,298,548.94 USD | `4,184.01` | `2602.13` | `2221.50` | `3424.97` | 1,588,797.73 USD | `+17.09%` | `20X Cross` |
| `250` | `0x5e9e...35ee` | `SHORT` | 8,898,376.68 USD | `4,007.56` | `1796.39` | `2221.50` | `2585.47` | -1,699,226.59 USD | `-19.10%` | `20X Cross` |
| `251` | `0x8cc9...2b6a` | `SHORT` | 8,894,800.00 USD | `4,000.00` | `1791.18` | `2221.50` | `3539.91` | -1,730,053.33 USD | `-19.45%` | `25X Cross` |
| `252` | `0x3dc9...54b0` | `SHORT` | 8,894,111.10 USD | `3,999.69` | `2480.32` | `2221.50` | `6626.75` | 1,026,425.45 USD | `+11.54%` | `20X Cross` |
| `253` | `0xfb94...0ddf` | `SHORT` | 8,893,869.72 USD | `4,002.10` | `2382.44` | `2221.50` | `5104.36` | 640,914.43 USD | `+7.21%` | `20X Cross` |
| `270` | `0x4b67...f4e7` | `LONG` | 8,496,788.22 USD | `3,820.84` | `2591.51` | `2221.50` | `1351.56` | -1,404,985.33 USD | `-16.54%` | `20X Cross` |
| `279` | `0x12d2...f97f` | `LONG` | 8,355,397.46 USD | `3,757.26` | `2446.50` | `2221.50` | `1801.56` | -836,768.93 USD | `-10.01%` | `20X Cross` |
| `297` | `0x8ae4...3d60` | `LONG` | 7,912,721.38 USD | `3,558.20` | `2482.21` | `2221.50` | `525.62` | -919,476.65 USD | `-11.62%` | `10X Cross` |
| `300` | `0x469e...58a5` | `SHORT` | 7,852,479.70 USD | `3,533.33` | `2203.63` | `2221.50` | `3084.35` | -66,316.61 USD | `-0.84%` | `25X Cross` |
| `309` | `0x218a...7da2` | `SHORT` | 7,705,618.66 USD | `3,465.07` | `2208.16` | `2221.50` | `3101.69` | -54,189.41 USD | `-0.70%` | `10X Cross` |
| `337` | `0x9c2a...f6a8` | `SHORT` | 6,672,208.41 USD | `3,002.39` | `2515.77` | `2221.50` | `2589.61` | 881,129.49 USD | `+13.21%` | `20X Cross` |
| `339` | `0x4a20...3c26` | `LONG` | 6,668,700.00 USD | `3,000.00` | `2428.72` | `2221.50` | `626.84` | -617,460.28 USD | `-9.26%` | `20X Cross` |
| `340` | `0xb823...9763` | `SHORT` | 6,667,800.00 USD | `3,000.00` | `2229.66` | `2221.50` | `3233.36` | 21,196.68 USD | `+0.32%` | `25X Cross` |
| `342` | `0x007d...67a0` | `LONG` | 6,661,200.00 USD | `3,000.00` | `2400.00` | `2221.50` | `1469.39` | -538,800.00 USD | `-8.09%` | `25X Cross` |
| `393` | `0x8328...f54a` | `SHORT` | 5,725,647.28 USD | `2,576.45` | `2292.01` | `2221.50` | `3279.21` | 179,624.01 USD | `+3.14%` | `25X Cross` |
| `395` | `0xed48...7c9b` | `SHORT` | 5,669,632.42 USD | `2,551.13` | `2460.02` | `2221.50` | `3225.27` | 606,213.99 USD | `+10.69%` | `20X Cross` |
| `399` | `0x970c...2a93` | `SHORT` | 5,559,500.00 USD | `2,500.00` | `2229.57` | `2221.50` | `5078.59` | 14,444.49 USD | `+0.26%` | `20X Cross` |
| `400` | `0x1c98...7fc7` | `LONG` | 5,556,010.00 USD | `2,500.00` | `2452.60` | `2221.50` | `1916.60` | -575,511.56 USD | `-10.36%` | `10X Cross` |
| `414` | `0xa445...329d` | `LONG` | 5,348,599.27 USD | `2,406.14` | `2354.86` | `2221.50` | `1768.40` | -317,516.01 USD | `-5.94%` | `25X Cross` |
| `416` | `0xfbe2...c8ea` | `SHORT` | 5,300,881.81 USD | `2,385.21` | `2041.57` | `2221.50` | `2622.12` | -431,315.16 USD | `-8.14%` | `20X Cross` |
| `417` | `0x6749...ce07` | `SHORT` | 5,299,950.38 USD | `2,384.89` | `2220.92` | `2221.50` | `3630.49` | -3,287.35 USD | `-0.06%` | `20X Cross` |
| `418` | `0x645b...87b8` | `SHORT` | 5,289,257.77 USD | `2,379.98` | `2421.64` | `2221.50` | `11573.56` | 474,189.18 USD | `+8.97%` | `10X Cross` |
| `427` | `0x77ee...2902` | `SHORT` | 5,094,039.09 USD | `2,290.69` | `2476.53` | `2221.50` | `6103.26` | 578,933.15 USD | `+11.36%` | `25X Cross` |
| `451` | `0xd507...c948` | `SHORT` | 4,830,310.58 USD | `2,172.00` | `2387.49` | `2221.50` | `2600.21` | 355,330.45 USD | `+7.36%` | `5X Isolated` |
| `457` | `0x023a...2355` | `LONG` | 4,765,207.56 USD | `2,142.82` | `2328.93` | `2221.50` | `0.000000` | -225,296.29 USD | `-4.73%` | `25X Cross` |
| `462` | `0x382b...3e39` | `SHORT` | 4,735,674.61 USD | `2,129.54` | `2296.66` | `2221.50` | `4551.16` | 155,162.61 USD | `+3.28%` | `25X Cross` |
| `499` | `0x3453...b323` | `SHORT` | 4,444,873.57 USD | `2,000.12` | `2322.47` | `2221.50` | `2398.71` | 200,362.28 USD | `+4.51%` | `25X Cross` |
| `500` | `0xe02e...d78b` | `LONG` | 4,444,600.00 USD | `2,000.00` | `2228.11` | `2221.50` | `2171.55` | -11,623.47 USD | `-0.26%` | `25X Cross` |
| `505` | `0xf3dc...1672` | `SHORT` | 4,403,709.62 USD | `1,980.36` | `2240.44` | `2221.50` | `2787.86` | 33,177.94 USD | `+0.75%` | `20X Cross` |
| `506` | `0x0622...8088` | `LONG` | 4,403,603.15 USD | `1,981.28` | `2228.49` | `2221.50` | `0.000000` | -11,679.07 USD | `-0.27%` | `5X Cross` |
| `510` | `0x7a6d...f79c` | `SHORT` | 4,383,890.24 USD | `1,971.44` | `2418.41` | `2221.50` | `2545.05` | 383,870.94 USD | `+8.76%` | `25X Cross` |
| `511` | `0xac48...3201` | `SHORT` | 4,365,418.34 USD | `1,964.37` | `2272.04` | `2221.50` | `3083.15` | 97,723.96 USD | `+2.24%` | `20X Cross` |
| `524` | `0x8376...9a1e` | `SHORT` | 4,245,695.26 USD | `1,910.50` | `2477.72` | `2221.50` | `3186.88` | 487,992.91 USD | `+11.49%` | `20X Cross` |
| `525` | `0x739c...cfb2` | `SHORT` | 4,225,030.00 USD | `1,900.00` | `2418.12` | `2221.50` | `2443.57` | 369,416.38 USD | `+8.74%` | `25X Cross` |
| `546` | `0xbcd4...0dd2` | `SHORT` | 4,065,036.29 USD | `1,829.12` | `2233.24` | `2221.50` | `2742.58` | 19,843.42 USD | `+0.49%` | `25X Cross` |
| `549` | `0x4487...c92d` | `LONG` | 4,053,692.36 USD | `1,825.66` | `2232.11` | `2221.50` | `1607.64` | -21,379.86 USD | `-0.53%` | `10X Cross` |
| `557` | `0x7265...91a5` | `LONG` | 4,006,816.98 USD | `1,801.87` | `2533.96` | `2221.50` | `1987.07` | -559,049.47 USD | `-13.95%` | `20X Cross` |
| `558` | `0xc619...10f5` | `LONG` | 4,002,840.00 USD | `1,800.00` | `2313.55` | `2221.50` | `1822.96` | -161,555.83 USD | `-4.04%` | `25X Cross` |
| `559` | `0xbb34...1696` | `LONG` | 4,000,140.00 USD | `1,800.00` | `2313.95` | `2221.50` | `1990.87` | -164,978.23 USD | `-4.12%` | `25X Cross` |
| `571` | `0x91a9...3f70` | `SHORT` | 3,927,870.80 USD | `1,767.48` | `2156.23` | `2221.50` | `3672.62` | -116,766.72 USD | `-2.97%` | `4X Cross` |
| `604` | `0xfeec...4e9c` | `SHORT` | 3,762,413.59 USD | `1,691.81` | `2566.49` | `2221.50` | `2509.62` | 579,610.92 USD | `+15.41%` | `10X Cross` |
| `627` | `0xeee0...0b53` | `LONG` | 3,640,636.13 USD | `1,637.12` | `2468.64` | `2221.50` | `196.39` | -400,839.93 USD | `-11.01%` | `7X Cross` |
| `629` | `0x27b8...12fc` | `LONG` | 3,620,776.29 USD | `1,628.12` | `2468.73` | `2221.50` | `638.36` | -398,618.34 USD | `-11.01%` | `10X Cross` |
| `630` | `0x982b...4606` | `LONG` | 3,615,276.09 USD | `1,626.82` | `2575.24` | `2221.50` | `1547.35` | -574,176.99 USD | `-15.88%` | `5X Isolated` |
| `637` | `0x73d7...8be1` | `LONG` | 3,555,894.00 USD | `1,601.47` | `2410.40` | `2221.50` | `1768.78` | -304,284.92 USD | `-8.56%` | `25X Cross` |
| `638` | `0xad54...6203` | `LONG` | 3,550,016.91 USD | `1,597.45` | `2591.98` | `2221.50` | `2043.76` | -590,561.13 USD | `-16.64%` | `10X Isolated` |
| `645` | `0x880a...311c` | `LONG` | 3,507,677.65 USD | `1,578.40` | `2209.72` | `2221.50` | `0.000000` | 19,853.80 USD | `+0.57%` | `9X Cross` |
| `652` | `0x936c...bb0f` | `LONG` | 3,486,155.54 USD | `1,568.64` | `2232.92` | `2221.50` | `0.000000` | -16,514.08 USD | `-0.47%` | `20X Cross` |
| `663` | `0xe170...9300` | `SHORT` | 3,407,828.16 USD | `1,533.40` | `2076.39` | `2221.50` | `3110.12` | -223,878.66 USD | `-6.57%` | `25X Cross` |
| `667` | `0x4b86...df9d` | `SHORT` | 3,388,918.80 USD | `1,524.00` | `2287.40` | `2221.50` | `2759.56` | 97,078.80 USD | `+2.86%` | `9X Isolated` |
| `672` | `0x2e2b...2fab` | `LONG` | 3,351,939.16 USD | `1,507.38` | `2245.53` | `2221.50` | `1260.04` | -32,933.94 USD | `-0.98%` | `25X Cross` |
| `676` | `0xde6b...3361` | `LONG` | 3,333,900.00 USD | `1,500.00` | `2216.98` | `2221.50` | `2168.48` | 8,419.26 USD | `+0.25%` | `25X Cross` |
| `678` | `0x251f...6e5d` | `LONG` | 3,333,450.00 USD | `1,500.00` | `2346.68` | `2221.50` | `1902.26` | -186,580.49 USD | `-5.60%` | `20X Cross` |
| `697` | `0xb885...3c54` | `LONG` | 3,219,584.88 USD | `1,450.00` | `2274.34` | `2221.50` | `33.21` | -78,223.25 USD | `-2.43%` | `20X Cross` |
| `701` | `0xef70...a84c` | `SHORT` | 3,206,208.66 USD | `1,442.74` | `2424.73` | `2221.50` | `3251.53` | 292,062.17 USD | `+9.11%` | `25X Cross` |
| `706` | `0xe668...b5ca` | `SHORT` | 3,187,277.33 USD | `1,434.22` | `2241.90` | `2221.50` | `2320.79` | 28,122.96 USD | `+0.88%` | `25X Cross` |
| `708` | `0xbadb...9ee6` | `LONG` | 3,173,799.97 USD | `1,428.16` | `1936.00` | `2221.50` | `1081.50` | 408,878.32 USD | `+12.88%` | `20X Cross` |
| `762` | `0x53f8...ceff` | `LONG` | 2,997,114.45 USD | `1,348.65` | `2276.73` | `2221.50` | `0.000000` | -73,410.02 USD | `-2.45%` | `20X Cross` |
| `775` | `0x020c...5872` | `LONG` | 2,953,531.00 USD | `1,330.00` | `2226.24` | `2221.50` | `2138.23` | -7,376.43 USD | `-0.25%` | `25X Cross` |
| `779` | `0xa0fb...96be` | `LONG` | 2,929,081.79 USD | `1,317.09` | `2277.10` | `2221.50` | `1519.85` | -70,080.49 USD | `-2.39%` | `3X Cross` |
| `787` | `0x0dd5...f6ee` | `LONG` | 2,884,860.55 USD | `1,298.08` | `2290.07` | `2221.50` | `1550.12` | -87,852.03 USD | `-3.05%` | `5X Cross` |
| `795` | `0x039c...0ebd` | `LONG` | 2,868,227.44 USD | `1,289.80` | `2226.24` | `2221.50` | `0.000000` | -3,186.50 USD | `-0.11%` | `25X Cross` |
| `812` | `0x1f16...6d07` | `LONG` | 2,813,431.80 USD | `1,266.00` | `2261.43` | `2221.50` | `1385.24` | -49,539.43 USD | `-1.76%` | `7X Cross` |
| `813` | `0xb8eb...1dd5` | `LONG` | 2,809,237.43 USD | `1,264.11` | `2232.77` | `2221.50` | `711.44` | -13,240.94 USD | `-0.47%` | `25X Cross` |
| `820` | `0xc435...c905` | `SHORT` | 2,773,555.20 USD | `1,248.00` | `2704.38` | `2221.50` | `3802.79` | 601,515.15 USD | `+21.69%` | `20X Cross` |
| `824` | `0x6859...7e1e` | `SHORT` | 2,751,306.34 USD | `1,237.15` | `2200.39` | `2221.50` | `4867.89` | -29,079.18 USD | `-1.06%` | `25X Cross` |
| `835` | `0x7178...0854` | `LONG` | 2,709,992.73 USD | `1,218.63` | `2461.81` | `2221.50` | `1188.37` | -290,053.67 USD | `-10.70%` | `10X Cross` |
| `836` | `0x7277...0b98` | `SHORT` | 2,709,992.40 USD | `1,219.45` | `2206.05` | `2221.50` | `3412.65` | -19,804.60 USD | `-0.73%` | `20X Cross` |
| `848` | `0xaaa1...ab8c` | `SHORT` | 2,668,524.00 USD | `1,200.00` | `2276.29` | `2221.50` | `2365.18` | 63,033.58 USD | `+2.36%` | `25X Isolated` |
| `860` | `0xfc27...9d9d` | `LONG` | 2,628,158.23 USD | `1,182.31` | `2237.33` | `2221.50` | `0.000000` | -17,067.10 USD | `-0.65%` | `25X Cross` |
| `862` | `0x07fd...689d` | `LONG` | 2,614,963.52 USD | `1,176.69` | `2416.34` | `2221.50` | `0.000000` | -228,336.42 USD | `-8.73%` | `25X Cross` |
| `916` | `0x2577...4897` | `LONG` | 2,424,490.61 USD | `1,090.93` | `2231.96` | `2221.50` | `0.000000` | -10,439.25 USD | `-0.43%` | `15X Cross` |
| `918` | `0x2f80...f203` | `SHORT` | 2,423,329.52 USD | `1,088.94` | `1984.00` | `2221.50` | `2959.74` | -262,862.34 USD | `-10.85%` | `20X Cross` |
| `923` | `0x6f11...0389` | `SHORT` | 2,397,861.70 USD | `1,079.00` | `2333.39` | `2221.50` | `2971.51` | 119,867.21 USD | `+5.00%` | `25X Cross` |
| `925` | `0x8eb7...b90f` | `LONG` | 2,396,644.10 USD | `1,077.74` | `2396.38` | `2221.50` | `1880.88` | -186,033.94 USD | `-7.76%` | `5X Isolated` |
| `928` | `0x2b61...2f6c` | `SHORT` | 2,394,136.85 USD | `1,076.60` | `2681.75` | `2221.50` | `6282.24` | 493,035.89 USD | `+20.59%` | `10X Cross` |
| `938` | `0xef96...9383` | `LONG` | 2,364,197.17 USD | `1,063.13` | `2234.39` | `2221.50` | `0.000000` | -11,259.36 USD | `-0.48%` | `25X Cross` |
| `961` | `0x30af...393e` | `SHORT` | 2,315,134.27 USD | `1,041.16` | `2252.26` | `2221.50` | `2296.87` | 29,848.05 USD | `+1.29%` | `25X Cross` |
| `973` | `0x1b2a...f7a6` | `LONG` | 2,278,675.31 USD | `1,025.37` | `2737.51` | `2221.50` | `882.02` | -528,284.63 USD | `-23.18%` | `10X Cross` |
| `985` | `0x001a...fef6` | `SHORT` | 2,240,190.07 USD | `1,007.33` | `2022.19` | `2221.50` | `3090.03` | -203,182.11 USD | `-9.07%` | `10X Cross` |
| `986` | `0x02aa...1806` | `SHORT` | 2,239,589.20 USD | `1,007.10` | `2654.68` | `2221.50` | `3612.66` | 433,942.90 USD | `+19.38%` | `20X Cross` |
| `989` | `0xdb3a...cf3b` | `LONG` | 2,230,949.74 USD | `1,003.22` | `2705.01` | `2221.50` | `0.000000` | -482,757.15 USD | `-21.64%` | `4X Cross` |
| `992` | `0x5272...fcd9` | `SHORT` | 2,223,900.00 USD | `1,000.00` | `2241.82` | `2221.50` | `2830.71` | 17,924.49 USD | `+0.81%` | `5X Cross` |
| `993` | `0x6463...42f5` | `SHORT` | 2,223,900.00 USD | `1,000.00` | `2223.43` | `2221.50` | `3705.96` | -465.05 USD | `-0.02%` | `5X Cross` |
| `994` | `0x8c02...b73f` | `SHORT` | 2,223,700.00 USD | `1,000.00` | `2250.37` | `2221.50` | `8098.34` | 26,671.47 USD | `+1.20%` | `20X Cross` |
| `995` | `0xf929...d1f9` | `SHORT` | 2,222,300.00 USD | `1,000.00` | `2423.37` | `2221.50` | `2926.09` | 201,070.17 USD | `+9.05%` | `25X Cross` |
| `996` | `0xd7b8...9f55` | `LONG` | 2,220,077.70 USD | `999.00` | `2195.00` | `2221.50` | `0.000000` | 27,272.70 USD | `+1.23%` | `15X Cross` |
| `1000` | `0x9599...c60a` | `LONG` | 2,212,815.23 USD | `995.60` | `2233.08` | `2221.50` | `0.000000` | -10,434.98 USD | `-0.47%` | `20X Cross` |
| `1027` | `0xb002...ed8a` | `SHORT` | 2,139,594.88 USD | `962.78` | `2299.66` | `2221.50` | `4198.56` | 74,483.02 USD | `+3.48%` | `25X Cross` |
| `1048` | `0xb1ec...e86a` | `SHORT` | 2,074,824.62 USD | `933.64` | `2272.72` | `2221.50` | `12533.03` | 47,082.34 USD | `+2.27%` | `25X Cross` |
| `1053` | `0xb812...b5e0` | `LONG` | 2,060,571.50 USD | `927.18` | `2263.21` | `2221.50` | `1165.38` | -37,842.46 USD | `-1.84%` | `25X Cross` |
| `1071` | `0xede2...f971` | `LONG` | 2,030,413.32 USD | `914.31` | `2208.16` | `2221.50` | `1462.93` | 11,456.34 USD | `+0.56%` | `5X Cross` |
| `1073` | `0x9606...4e5d` | `SHORT` | 2,029,043.87 USD | `913.00` | `2478.70` | `2221.50` | `4330.86` | 234,009.74 USD | `+11.53%` | `20X Cross` |
| `1096` | `0x5f10...d49d` | `LONG` | 2,001,510.00 USD | `900.00` | `2249.83` | `2221.50` | `1817.66` | -23,343.47 USD | `-1.17%` | `25X Cross` |
| `1108` | `0x51f6...2b39` | `LONG` | 1,978,263.80 USD | `890.15` | `2226.49` | `2221.50` | `732.15` | -3,643.09 USD | `-0.18%` | `25X Cross` |
| `1183` | `0x2828...93a0` | `LONG` | 1,865,847.52 USD | `839.60` | `2242.41` | `2221.50` | `2192.48` | -16,884.67 USD | `-0.90%` | `25X Cross` |
| `1184` | `0xcd27...52a8` | `LONG` | 1,861,783.82 USD | `837.21` | `2553.56` | `2221.50` | `1403.16` | -276,080.96 USD | `-14.83%` | `2X Cross` |
| `1246` | `0x04a9...95aa` | `LONG` | 1,779,040.00 USD | `800.00` | `2595.13` | `2221.50` | `1873.20` | -297,066.74 USD | `-16.70%` | `5X Cross` |
| `1248` | `0x7737...bf66` | `SHORT` | 1,778,577.23 USD | `799.79` | `2494.83` | `2221.50` | `24774.40` | 216,768.80 USD | `+12.19%` | `15X Cross` |
| `1273` | `0x458d...ab3b` | `LONG` | 1,722,882.38 USD | `774.75` | `2740.41` | `2221.50` | `1886.92` | -400,246.80 USD | `-23.23%` | `3X Isolated` |
| `1331` | `0xaa53...9cb7` | `LONG` | 1,623,027.25 USD | `730.34` | `2389.70` | `2221.50` | `1928.80` | -122,262.39 USD | `-7.53%` | `20X Cross` |
| `1333` | `0x3fc5...c0c1` | `SHORT` | 1,622,110.55 USD | `729.92` | `2702.11` | `2221.50` | `4730.86` | 350,231.65 USD | `+21.59%` | `25X Cross` |
| `1350` | `0xa189...94d7` | `SHORT` | 1,600,441.32 USD | `719.98` | `2691.84` | `2221.50` | `2914.81` | 337,631.34 USD | `+21.10%` | `25X Cross` |
| `1365` | `0x2f93...4404` | `LONG` | 1,570,869.72 USD | `707.47` | `1700.45` | `2221.50` | `1368.55` | 367,843.34 USD | `+23.42%` | `4X Isolated` |
| `1375` | `0x5605...fe0f` | `SHORT` | 1,561,497.15 USD | `702.14` | `2566.90` | `2221.50` | `3093.49` | 240,835.50 USD | `+15.42%` | `20X Cross` |
| `1381` | `0x0deb...0bc5` | `LONG` | 1,555,610.00 USD | `700.00` | `2071.05` | `2221.50` | `1597.14` | 105,874.21 USD | `+6.81%` | `20X Cross` |
| `1382` | `0x26e6...6b28` | `LONG` | 1,555,610.00 USD | `700.00` | `1835.24` | `2221.50` | `2042.98` | 270,938.47 USD | `+17.42%` | `20X Cross` |
| `1435` | `0x248e...6be2` | `SHORT` | 1,514,316.45 USD | `680.93` | `2282.89` | `2221.50` | `3385.92` | 40,169.22 USD | `+2.65%` | `20X Cross` |
| `1440` | `0xdbd1...29dd` | `SHORT` | 1,511,431.83 USD | `680.70` | `3030.57` | `2221.50` | `3793.07` | 551,489.29 USD | `+36.49%` | `6X Cross` |
| `1443` | `0x71e5...be04` | `LONG` | 1,507,063.20 USD | `677.67` | `2727.27` | `2221.50` | `1470.70` | -341,122.41 USD | `-22.63%` | `20X Cross` |
| `1452` | `0x0b23...f37b` | `LONG` | 1,500,120.00 USD | `675.00` | `2238.15` | `2221.50` | `592.27` | -10,636.64 USD | `-0.71%` | `5X Cross` |
| `1454` | `0x4e23...20c3` | `SHORT` | 1,495,560.96 USD | `672.49` | `2230.51` | `2221.50` | `20215.94` | 4,451.82 USD | `+0.30%` | `20X Cross` |
| `1464` | `0xd911...961e` | `LONG` | 1,478,922.63 USD | `665.01` | `2231.50` | `2221.50` | `0.000000` | -5,060.41 USD | `-0.34%` | `25X Cross` |
| `1472` | `0x0cac...6170` | `SHORT` | 1,462,214.25 USD | `657.50` | `2146.55` | `2221.50` | `2839.16` | -50,852.05 USD | `-3.48%` | `20X Cross` |
| `1503` | `0xf00e...fe3d` | `SHORT` | 1,429,700.83 USD | `642.88` | `2333.21` | `2221.50` | `2486.37` | 70,277.14 USD | `+4.92%` | `20X Cross` |
| `1505` | `0xb15b...dbae` | `SHORT` | 1,428,210.25 USD | `642.64` | `2290.80` | `2221.50` | `2327.83` | 43,957.23 USD | `+3.08%` | `25X Cross` |
| `1512` | `0xffb2...5ed6` | `SHORT` | 1,424,040.14 USD | `640.77` | `2672.96` | `2221.50` | `2491.23` | 288,708.21 USD | `+20.27%` | `20X Cross` |
| `1525` | `0x8505...1821` | `SHORT` | 1,408,849.97 USD | `633.96` | `2239.93` | `2221.50` | `3885.06` | 11,181.63 USD | `+0.79%` | `20X Cross` |
| `1546` | `0x0a97...347d` | `LONG` | 1,388,190.40 USD | `624.21` | `2259.32` | `2221.50` | `919.00` | -22,112.92 USD | `-1.59%` | `20X Cross` |
| `1548` | `0xfce0...f4c0` | `SHORT` | 1,385,826.28 USD | `623.60` | `3129.61` | `2221.50` | `2807.76` | 565,800.31 USD | `+40.83%` | `20X Cross` |
| `1587` | `0xa70a...4be9` | `LONG` | 1,344,205.74 USD | `605.39` | `2251.37` | `2221.50` | `0.000000` | -18,752.66 USD | `-1.40%` | `20X Cross` |
| `1594` | `0x7050...5fff` | `SHORT` | 1,336,617.97 USD | `601.11` | `2245.52` | `2221.50` | `3266.06` | 13,182.14 USD | `+0.99%` | `25X Cross` |
| `1595` | `0xad02...eb65` | `LONG` | 1,335,659.20 USD | `600.62` | `2460.69` | `2221.50` | `1078.62` | -142,281.36 USD | `-10.65%` | `5X Cross` |
| `1596` | `0x24fb...ed0f` | `LONG` | 1,334,427.47 USD | `600.10` | `2199.85` | `2221.50` | `0.000000` | 14,304.04 USD | `+1.07%` | `15X Cross` |
| `1597` | `0x638f...f5f0` | `LONG` | 1,334,340.00 USD | `600.00` | `4011.50` | `2221.50` | `433.63` | -1,072,563.53 USD | `-80.38%` | `25X Cross` |
| `1607` | `0x6e6f...82a6` | `LONG` | 1,322,279.61 USD | `595.00` | `2257.18` | `2221.50` | `590.83` | -20,758.03 USD | `-1.57%` | `20X Cross` |
| `1676` | `0x9362...7d7c` | `SHORT` | 1,260,086.35 USD | `566.99` | `2226.19` | `2221.50` | `2518.61` | 2,149.46 USD | `+0.17%` | `20X Cross` |
| `1679` | `0xfb99...37f3` | `LONG` | 1,257,188.58 USD | `565.34` | `2362.35` | `2221.50` | `1254.36` | -78,347.78 USD | `-6.23%` | `3X Cross` |
| `1688` | `0x844b...7f42` | `SHORT` | 1,247,551.80 USD | `561.00` | `2026.17` | `2221.50` | `3042.73` | -110,868.39 USD | `-8.89%` | `25X Cross` |
| `1707` | `0xabe6...1d99` | `SHORT` | 1,236,497.30 USD | `556.00` | `2484.68` | `2221.50` | `3125.37` | 144,998.59 USD | `+11.73%` | `20X Cross` |
| `1709` | `0x2a76...9a53` | `LONG` | 1,233,443.17 USD | `555.03` | `2231.40` | `2221.50` | `0.000000` | -5,052.93 USD | `-0.41%` | `25X Cross` |
| `1715` | `0xbef3...0d3e` | `LONG` | 1,228,264.78 USD | `552.33` | `2233.44` | `2221.50` | `2068.58` | -5,326.04 USD | `-0.43%` | `20X Cross` |
| `1720` | `0x6a41...a3b9` | `LONG` | 1,224,686.61 USD | `550.69` | `2233.05` | `2221.50` | `2074.03` | -5,039.75 USD | `-0.41%` | `20X Cross` |
| `1722` | `0x825c...465e` | `LONG` | 1,222,265.00 USD | `550.00` | `2208.12` | `2221.50` | `1189.21` | 7,795.50 USD | `+0.64%` | `4X Cross` |
| `1726` | `0xad21...fb6a` | `LONG` | 1,216,166.79 USD | `547.26` | `2565.80` | `2221.50` | `1735.16` | -187,986.21 USD | `-15.46%` | `6X Cross` |
| `1767` | `0xfc66...ca06` | `SHORT` | 1,171,930.97 USD | `527.28` | `2275.19` | `2221.50` | `17009.52` | 27,734.78 USD | `+2.37%` | `20X Cross` |
| `1794` | `0x2e30...4cb5` | `SHORT` | 1,157,893.30 USD | `521.48` | `2316.81` | `2221.50` | `11952.76` | 50,279.17 USD | `+4.34%` | `2X Cross` |
| `1806` | `0x6dae...90de` | `SHORT` | 1,149,048.66 USD | `517.05` | `2292.28` | `2221.50` | `3866.61` | 36,184.76 USD | `+3.15%` | `25X Cross` |
| `1837` | `0x0089...2410` | `SHORT` | 1,128,285.88 USD | `507.35` | `2308.88` | `2221.50` | `3364.53` | 43,114.38 USD | `+3.82%` | `20X Cross` |
| `1852` | `0xe282...df29` | `LONG` | 1,111,900.00 USD | `500.00` | `2309.84` | `2221.50` | `2045.06` | -43,024.21 USD | `-3.87%` | `10X Isolated` |
| `1853` | `0xa559...ff95` | `LONG` | 1,111,900.00 USD | `500.00` | `2260.68` | `2221.50` | `1057.91` | -18,444.36 USD | `-1.66%` | `20X Cross` |
| `1854` | `0xb322...d51f` | `SHORT` | 1,111,900.00 USD | `500.00` | `2268.03` | `2221.50` | `3741.66` | 22,116.32 USD | `+1.99%` | `20X Cross` |
| `1855` | `0x6936...9417` | `SHORT` | 1,111,850.00 USD | `500.00` | `2315.11` | `2221.50` | `2358.66` | 45,705.21 USD | `+4.11%` | `25X Isolated` |
| `1856` | `0x4044...794c` | `LONG` | 1,111,150.00 USD | `500.00` | `2260.80` | `2221.50` | `0.000000` | -19,250.00 USD | `-1.73%` | `25X Cross` |
| `1858` | `0x89b2...9ca6` | `LONG` | 1,110,350.00 USD | `500.00` | `2363.45` | `2221.50` | `1622.40` | -71,377.42 USD | `-6.43%` | `25X Cross` |
| `1863` | `0x7298...7d6c` | `SHORT` | 1,107,769.47 USD | `498.15` | `3426.75` | `2221.50` | `5421.37` | 599,266.35 USD | `+54.10%` | `20X Cross` |
| `1874` | `0x9c68...7783` | `SHORT` | 1,096,277.92 USD | `493.31` | `2273.58` | `2221.50` | `3907.91` | 25,301.32 USD | `+2.31%` | `25X Cross` |
| `1882` | `0x404c...5f03` | `SHORT` | 1,087,666.22 USD | `489.79` | `2671.94` | `2221.50` | `5061.79` | 221,013.34 USD | `+20.32%` | `20X Cross` |
| `1887` | `0x321f...1c84` | `SHORT` | 1,084,565.43 USD | `488.02` | `2370.09` | `2221.50` | `3058.31` | 72,079.18 USD | `+6.65%` | `10X Cross` |
| `1893` | `0x94b6...e5b3` | `SHORT` | 1,079,226.75 USD | `486.05` | `2260.75` | `2221.50` | `2346.30` | 19,615.84 USD | `+1.82%` | `25X Cross` |
| `1940` | `0xd4c1...3d1d` | `LONG` | 1,033,267.40 USD | `464.89` | `2242.01` | `2221.50` | `0.000000` | -9,026.83 USD | `-0.87%` | `12X Cross` |
| `1951` | `0x82c6...fe42` | `LONG` | 1,028,461.25 USD | `462.50` | `2501.38` | `2221.50` | `2053.40` | -128,429.32 USD | `-12.49%` | `5X Isolated` |
| `1962` | `0xe330...77a1` | `SHORT` | 1,025,618.78 USD | `461.20` | `2206.97` | `2221.50` | `6448.70` | -7,761.42 USD | `-0.76%` | `20X Cross` |
| `1967` | `0x2de3...486d` | `LONG` | 1,023,146.92 USD | `460.40` | `2286.27` | `2221.50` | `1130.80` | -29,453.99 USD | `-2.88%` | `25X Cross` |
| `1969` | `0x7a76...b16d` | `LONG` | 1,021,741.75 USD | `459.50` | `2228.08` | `2221.50` | `2046.78` | -2,062.73 USD | `-0.20%` | `25X Cross` |
| `1971` | `0xd6e1...f256` | `LONG` | 1,019,507.97 USD | `458.64` | `2213.70` | `2221.50` | `918.74` | 4,217.08 USD | `+0.41%` | `25X Cross` |
| `1975` | `0x617e...0f97` | `SHORT` | 1,017,489.83 USD | `457.85` | `2205.60` | `2221.50` | `3367.38` | -7,646.00 USD | `-0.75%` | `10X Cross` |
| `1981` | `0xe86b...3664` | `LONG` | 1,013,694.37 USD | `456.15` | `2230.96` | `2221.50` | `0.000000` | -3,951.04 USD | `-0.39%` | `25X Cross` |
| `2006` | `0xae55...2236` | `LONG` | 1,000,305.00 USD | `450.00` | `2510.21` | `2221.50` | `0.000000` | -129,292.50 USD | `-12.93%` | `25X Cross` |

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
| `ANNOUNCEMENT` | `INFO` | `2478.30` | 218.34 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.22K USD at 2478.3000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2478.30` | 12.14 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.01K USD at 2478.3000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2478.30` | 72.61 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.07K USD at 2478.3000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2478.40` | 545.25 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.55K USD at 2478.4000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2478.50` | 282.30 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.28K USD at 2478.5000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2478.50` | 925.97 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.93K USD at 2478.5000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2478.50` | 24,159.43 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 24.16K USD at 2478.5000 USD [API] | `2026-10-08 15:20:45` |


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
| `7D` | `Long Liquidation` | `1971.60` | 735,760,000.00 USD | 735,760,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1974.40` | 735,630,000.00 USD | 735,630,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,950,000.00 USD | 224,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1977.20` | 735,580,000.00 USD | 735,580,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1982.80` | 733,340,000.00 USD | 733,340,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1985.00` | 8,110,000.00 USD | 222,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1985.60` | 733,130,000.00 USD | 733,130,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1988.40` | 730,840,000.00 USD | 730,840,000.00 USD | 1,440,000.00 USD | 1,780,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1991.20` | 727,630,000.00 USD | 727,630,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1994.00` | 724,880,000.00 USD | 724,880,000.00 USD | 0.00 USD | 0.00 USD | 808,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1995.00` | 1,720,000.00 USD | 214,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1996.80` | 724,070,000.00 USD | 724,070,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1998.20` | 600,230,000.00 USD | 600,230,000.00 USD | 219,590.00 USD | 104,180.00 USD | 24,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2000.60` | 599,880,000.00 USD | 599,880,000.00 USD | 13,780.00 USD | 236,510.00 USD | 586,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2002.40` | 722,730,000.00 USD | 722,730,000.00 USD | 0.00 USD | 0.00 USD | 594,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2003.00` | 599,040,000.00 USD | 599,040,000.00 USD | 616,980.00 USD | 601,340.00 USD | 478,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2005.00` | 12,670,000.00 USD | 212,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2005.20` | 722,140,000.00 USD | 722,140,000.00 USD | 0.00 USD | 742,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2005.40` | 597,340,000.00 USD | 597,340,000.00 USD | 493,990.00 USD | 13,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2007.80` | 596,840,000.00 USD | 596,840,000.00 USD | 0.00 USD | 558,480.00 USD | 126,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2008.00` | 721,390,000.00 USD | 721,390,000.00 USD | 807,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2010.20` | 596,150,000.00 USD | 596,150,000.00 USD | 484,920.00 USD | 463,210.00 USD | 362,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2010.80` | 720,590,000.00 USD | 720,590,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2012.60` | 594,840,000.00 USD | 594,840,000.00 USD | 323,800.00 USD | 266,130.00 USD | 25,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2015.00` | 594,220,000.00 USD | 594,220,000.00 USD | 355,800.00 USD | 159,880.00 USD | 188,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2015.00` | 5,010,000.00 USD | 200,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2017.40` | 593,520,000.00 USD | 593,520,000.00 USD | 537,580.00 USD | 1,350,000.00 USD | 559,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2019.20` | 719,630,000.00 USD | 719,630,000.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2019.80` | 591,080,000.00 USD | 591,080,000.00 USD | 326,370.00 USD | 1,140,000.00 USD | 166,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2022.00` | 719,610,000.00 USD | 719,610,000.00 USD | 0.00 USD | 0.00 USD | 934,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2022.20` | 589,440,000.00 USD | 589,440,000.00 USD | 1,380,000.00 USD | 333,050.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2024.60` | 586,240,000.00 USD | 586,240,000.00 USD | 197,740.00 USD | 1,010,000.00 USD | 822,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2024.80` | 718,680,000.00 USD | 718,680,000.00 USD | 1,070,000.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,440,000.00 USD | 195,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2027.00` | 584,220,000.00 USD | 584,220,000.00 USD | 1,390,000.00 USD | 233,420.00 USD | 196,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2027.60` | 717,430,000.00 USD | 717,430,000.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2029.40` | 582,400,000.00 USD | 582,400,000.00 USD | 1,680,000.00 USD | 1,300,000.00 USD | 775,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2030.40` | 716,330,000.00 USD | 716,330,000.00 USD | 0.00 USD | 3,320,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2031.80` | 578,640,000.00 USD | 578,640,000.00 USD | 1,290,000.00 USD | 156,850.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2033.20` | 711,930,000.00 USD | 711,930,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2034.20` | 576,160,000.00 USD | 576,160,000.00 USD | 1,110,000.00 USD | 1,330,000.00 USD | 165,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 423,740.00 USD | 193,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2036.00` | 710,370,000.00 USD | 710,370,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2036.60` | 573,560,000.00 USD | 573,560,000.00 USD | 119,600.00 USD | 177,360.00 USD | 30,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.80` | 710,040,000.00 USD | 710,040,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2039.00` | 573,230,000.00 USD | 573,230,000.00 USD | 939,380.00 USD | 300,240.00 USD | 357,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2041.40` | 571,630,000.00 USD | 571,630,000.00 USD | 626,840.00 USD | 178,560.00 USD | 188,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2043.80` | 570,640,000.00 USD | 570,640,000.00 USD | 0.00 USD | 0.00 USD | 16,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2044.40` | 708,590,000.00 USD | 708,590,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 6,640,000.00 USD | 193,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2046.20` | 570,620,000.00 USD | 570,620,000.00 USD | 467,370.00 USD | 0.00 USD | 19,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2048.60` | 570,130,000.00 USD | 570,130,000.00 USD | 51,070.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2050.00` | 708,290,000.00 USD | 708,290,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2051.00` | 569,730,000.00 USD | 569,730,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2052.80` | 708,060,000.00 USD | 708,060,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2053.40` | 568,670,000.00 USD | 568,670,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 3,920,000.00 USD | 186,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2055.80` | 568,550,000.00 USD | 568,550,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2058.20` | 568,310,000.00 USD | 568,310,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2058.40` | 705,780,000.00 USD | 705,780,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.20` | 705,440,000.00 USD | 705,440,000.00 USD | 1,600,000.00 USD | 1,120,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2063.00` | 567,550,000.00 USD | 567,550,000.00 USD | 0.00 USD | 111,540.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.00` | 701,010,000.00 USD | 701,010,000.00 USD | 1,050,000.00 USD | 826,260.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 15,310,000.00 USD | 182,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2065.40` | 567,420,000.00 USD | 567,420,000.00 USD | 563,140.00 USD | 485,130.00 USD | 510,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2066.80` | 698,180,000.00 USD | 698,180,000.00 USD | 476,480.00 USD | 1,340,000.00 USD | 200,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2067.80` | 565,860,000.00 USD | 565,860,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2069.60` | 696,170,000.00 USD | 696,170,000.00 USD | 1,510,000.00 USD | 2,770,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2070.20` | 565,170,000.00 USD | 565,170,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2072.40` | 690,590,000.00 USD | 690,590,000.00 USD | 4,460,000.00 USD | 1,850,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2072.60` | 564,800,000.00 USD | 564,800,000.00 USD | 47,910.00 USD | 555,250.00 USD | 420,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2075.00` | 563,770,000.00 USD | 563,770,000.00 USD | 25,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 2,710,000.00 USD | 167,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2075.20` | 682,740,000.00 USD | 682,740,000.00 USD | 4,080,000.00 USD | 3,180,000.00 USD | 4,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2077.40` | 563,750,000.00 USD | 563,750,000.00 USD | 354,080.00 USD | 25,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.00` | 671,470,000.00 USD | 671,470,000.00 USD | 3,750,000.00 USD | 3,040,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2079.80` | 563,370,000.00 USD | 563,370,000.00 USD | 55,820.00 USD | 15,600.00 USD | 199,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2080.80` | 663,110,000.00 USD | 663,110,000.00 USD | 4,230,000.00 USD | 2,970,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2082.20` | 563,100,000.00 USD | 563,100,000.00 USD | 850,080.00 USD | 18,240.00 USD | 208,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2083.60` | 653,430,000.00 USD | 653,430,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2084.60` | 562,020,000.00 USD | 562,020,000.00 USD | 528,660.00 USD | 207,610.00 USD | 486,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 13,760,000.00 USD | 164,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2086.40` | 648,770,000.00 USD | 648,770,000.00 USD | 4,830,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2087.00` | 560,800,000.00 USD | 560,800,000.00 USD | 551,330.00 USD | 370,040.00 USD | 639,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2089.20` | 636,670,000.00 USD | 636,670,000.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2089.40` | 559,240,000.00 USD | 559,240,000.00 USD | 152,210.00 USD | 218,010.00 USD | 108,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2091.80` | 558,760,000.00 USD | 558,760,000.00 USD | 1,010,000.00 USD | 338,870.00 USD | 450,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2092.00` | 630,460,000.00 USD | 630,460,000.00 USD | 3,470,000.00 USD | 293,650.00 USD | 6,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2094.20` | 556,950,000.00 USD | 556,950,000.00 USD | 1,920,000.00 USD | 881,690.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.80` | 620,200,000.00 USD | 620,200,000.00 USD | 5,040,000.00 USD | 2,120,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,710,000.00 USD | 150,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2096.60` | 553,080,000.00 USD | 553,080,000.00 USD | 516,470.00 USD | 465,510.00 USD | 828,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.60` | 611,650,000.00 USD | 611,650,000.00 USD | 1,830,000.00 USD | 3,350,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2099.00` | 551,270,000.00 USD | 551,270,000.00 USD | 330,040.00 USD | 989,450.00 USD | 248,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2100.40` | 605,180,000.00 USD | 605,180,000.00 USD | 1,810,000.00 USD | 1,580,000.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2101.40` | 549,710,000.00 USD | 549,710,000.00 USD | 46,810.00 USD | 334,210.00 USD | 534,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2103.20` | 598,490,000.00 USD | 598,490,000.00 USD | 679,880.00 USD | 554,710.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2103.80` | 548,790,000.00 USD | 548,790,000.00 USD | 753,840.00 USD | 391,570.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 2,380,000.00 USD | 149,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2106.00` | 595,000,000.00 USD | 595,000,000.00 USD | 1,560,000.00 USD | 986,590.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2106.20` | 547,640,000.00 USD | 547,640,000.00 USD | 3,130,000.00 USD | 886,560.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2108.60` | 542,450,000.00 USD | 542,450,000.00 USD | 656,240.00 USD | 21,400.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2108.80` | 590,890,000.00 USD | 590,890,000.00 USD | 8,350,000.00 USD | 1,600,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2111.00` | 541,770,000.00 USD | 541,770,000.00 USD | 450,470.00 USD | 81,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2111.60` | 579,120,000.00 USD | 579,120,000.00 USD | 2,990,000.00 USD | 1,140,000.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2113.40` | 541,240,000.00 USD | 541,240,000.00 USD | 452,130.00 USD | 520,660.00 USD | 249,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2114.40` | 573,650,000.00 USD | 573,650,000.00 USD | 1,080,000.00 USD | 2,330,000.00 USD | 3,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,330,000.00 USD | 146,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2115.80` | 540,020,000.00 USD | 540,020,000.00 USD | 722,960.00 USD | 315,330.00 USD | 935,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.20` | 566,390,000.00 USD | 566,390,000.00 USD | 2,410,000.00 USD | 1,830,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2118.20` | 538,040,000.00 USD | 538,040,000.00 USD | 4,580,000.00 USD | 3,940,000.00 USD | 302,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2120.00` | 560,160,000.00 USD | 560,160,000.00 USD | 13,440,000.00 USD | 5,380,000.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.60` | 529,220,000.00 USD | 529,220,000.00 USD | 5,670,000.00 USD | 1,980,000.00 USD | 671,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2122.80` | 539,230,000.00 USD | 539,230,000.00 USD | 4,100,000.00 USD | 4,620,000.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.00` | 520,900,000.00 USD | 520,900,000.00 USD | 5,450,000.00 USD | 1,840,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,770,000.00 USD | 145,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.40` | 510,950,000.00 USD | 510,950,000.00 USD | 3,930,000.00 USD | 2,390,000.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2125.60` | 528,520,000.00 USD | 528,520,000.00 USD | 6,230,000.00 USD | 7,150,000.00 USD | 2,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2127.80` | 503,310,000.00 USD | 503,310,000.00 USD | 4,430,000.00 USD | 3,780,000.00 USD | 745,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2128.40` | 512,710,000.00 USD | 512,710,000.00 USD | 4,290,000.00 USD | 1,960,000.00 USD | 3,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2130.20` | 494,350,000.00 USD | 494,350,000.00 USD | 1,250,000.00 USD | 18,610.00 USD | 774,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2131.20` | 502,480,000.00 USD | 502,480,000.00 USD | 1,980,000.00 USD | 1,810,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2132.60` | 492,310,000.00 USD | 492,310,000.00 USD | 81,820.00 USD | 284,820.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.00` | 497,330,000.00 USD | 497,330,000.00 USD | 2,270,000.00 USD | 617,060.00 USD | 308,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2135.00` | 490,420,000.00 USD | 490,420,000.00 USD | 1,430,000.00 USD | 2,070,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 2,100,000.00 USD | 21,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2136.80` | 494,140,000.00 USD | 494,140,000.00 USD | 1,850,000.00 USD | 1,510,000.00 USD | 2,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2137.40` | 485,780,000.00 USD | 485,780,000.00 USD | 660,230.00 USD | 1,670,000.00 USD | 560,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2139.60` | 488,660,000.00 USD | 488,660,000.00 USD | 1,110,000.00 USD | 2,190,000.00 USD | 635,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2139.80` | 482,890,000.00 USD | 482,890,000.00 USD | 1,470,000.00 USD | 367,550.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2142.20` | 480,990,000.00 USD | 480,990,000.00 USD | 522,990.00 USD | 3,160,000.00 USD | 876,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2142.40` | 484,720,000.00 USD | 484,720,000.00 USD | 4,320,000.00 USD | 1,100,000.00 USD | 434,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2144.60` | 476,430,000.00 USD | 476,430,000.00 USD | 2,860,000.00 USD | 2,330,000.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 1,020,000.00 USD | 19,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2145.20` | 478,870,000.00 USD | 478,870,000.00 USD | 2,210,000.00 USD | 1,760,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2147.00` | 470,030,000.00 USD | 470,030,000.00 USD | 1,570,000.00 USD | 1,340,000.00 USD | 69,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2148.00` | 473,180,000.00 USD | 473,180,000.00 USD | 26,270.00 USD | 538,910.00 USD | 134,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2149.40` | 467,050,000.00 USD | 467,050,000.00 USD | 7,120,000.00 USD | 1,670,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.80` | 472,480,000.00 USD | 472,480,000.00 USD | 0.00 USD | 363,770.00 USD | 317,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2151.80` | 456,300,000.00 USD | 456,300,000.00 USD | 2,620,000.00 USD | 3,960,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2153.60` | 471,790,000.00 USD | 471,790,000.00 USD | 11,230,000.00 USD | 603,900.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2154.20` | 447,190,000.00 USD | 447,190,000.00 USD | 1,160,000.00 USD | 3,480,000.00 USD | 853,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,970,000.00 USD | 18,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2156.40` | 458,330,000.00 USD | 458,330,000.00 USD | 2,500,000.00 USD | 1,710,000.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2156.60` | 441,700,000.00 USD | 441,700,000.00 USD | 5,700,000.00 USD | 1,610,000.00 USD | 2,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2159.00` | 431,390,000.00 USD | 431,390,000.00 USD | 1,820,000.00 USD | 2,320,000.00 USD | 4,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2159.20` | 452,920,000.00 USD | 452,920,000.00 USD | 4,780,000.00 USD | 1,330,000.00 USD | 5,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2161.40` | 422,670,000.00 USD | 422,670,000.00 USD | 8,470,000.00 USD | 9,400,000.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2162.00` | 441,640,000.00 USD | 441,640,000.00 USD | 15,360,000.00 USD | 1,850,000.00 USD | 514,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2163.80` | 403,360,000.00 USD | 403,360,000.00 USD | 15,960,000.00 USD | 7,660,000.00 USD | 3,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2164.80` | 423,920,000.00 USD | 423,920,000.00 USD | 11,610,000.00 USD | 17,760,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 6,050,000.00 USD | 15,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2166.20` | 375,860,000.00 USD | 375,860,000.00 USD | 11,060,000.00 USD | 11,460,000.00 USD | 5,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2167.60` | 391,790,000.00 USD | 391,790,000.00 USD | 11,850,000.00 USD | 11,020,000.00 USD | 298,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2168.60` | 347,670,000.00 USD | 347,670,000.00 USD | 17,790,000.00 USD | 6,160,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.40` | 368,620,000.00 USD | 368,620,000.00 USD | 2,420,000.00 USD | 11,510,000.00 USD | 8,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2171.00` | 319,980,000.00 USD | 319,980,000.00 USD | 21,940,000.00 USD | 10,800,000.00 USD | 6,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.20` | 345,970,000.00 USD | 345,970,000.00 USD | 30,070,000.00 USD | 0.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2173.40` | 280,940,000.00 USD | 280,940,000.00 USD | 7,740,000.00 USD | 1,390,000.00 USD | 3,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 6,220,000.00 USD | 9,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.80` | 268,010,000.00 USD | 268,010,000.00 USD | 2,090,000.00 USD | 569,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2176.00` | 314,390,000.00 USD | 314,390,000.00 USD | 5,390,000.00 USD | 1,460,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2178.20` | 265,350,000.00 USD | 265,350,000.00 USD | 1,290,000.00 USD | 1,180,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2178.80` | 304,720,000.00 USD | 304,720,000.00 USD | 196,330.00 USD | 133,210.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2180.60` | 259,550,000.00 USD | 259,550,000.00 USD | 4,460,000.00 USD | 3,440,000.00 USD | 6,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2181.60` | 303,210,000.00 USD | 303,210,000.00 USD | 3,960,000.00 USD | 2,160,000.00 USD | 4,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2183.00` | 244,870,000.00 USD | 244,870,000.00 USD | 637,950.00 USD | 1,320,000.00 USD | 365,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2184.40` | 292,710,000.00 USD | 292,710,000.00 USD | 26,960,000.00 USD | 2,700,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 661,930.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2185.40` | 242,560,000.00 USD | 242,560,000.00 USD | 2,650,000.00 USD | 2,480,000.00 USD | 5,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.20` | 260,500,000.00 USD | 260,500,000.00 USD | 14,380,000.00 USD | 17,750,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2187.80` | 231,800,000.00 USD | 231,800,000.00 USD | 5,040,000.00 USD | 4,050,000.00 USD | 7,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.00` | 228,370,000.00 USD | 228,370,000.00 USD | 14,800,000.00 USD | 27,960,000.00 USD | 8,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2190.20` | 214,780,000.00 USD | 214,780,000.00 USD | 8,990,000.00 USD | 4,390,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2192.60` | 197,390,000.00 USD | 197,390,000.00 USD | 5,000,000.00 USD | 4,860,000.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2192.80` | 177,580,000.00 USD | 177,580,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2195.00` | 186,320,000.00 USD | 186,320,000.00 USD | 5,700,000.00 USD | 2,910,000.00 USD | 5,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 2,240,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2195.60` | 162,160,000.00 USD | 162,160,000.00 USD | 383,690.00 USD | 243,760.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2197.40` | 171,760,000.00 USD | 171,760,000.00 USD | 4,650,000.00 USD | 1,240,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2198.40` | 161,500,000.00 USD | 161,500,000.00 USD | 0.00 USD | 1,460,000.00 USD | 7,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2199.80` | 162,210,000.00 USD | 162,210,000.00 USD | 4,040,000.00 USD | 4,100,000.00 USD | 10,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2201.20` | 152,490,000.00 USD | 152,490,000.00 USD | 4,700,000.00 USD | 266,430.00 USD | 8,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2202.20` | 143,490,000.00 USD | 143,490,000.00 USD | 16,430,000.00 USD | 10,590,000.00 USD | 10,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2204.00` | 139,510,000.00 USD | 139,510,000.00 USD | 9,760,000.00 USD | 4,330,000.00 USD | 15,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2204.60` | 106,340,000.00 USD | 106,340,000.00 USD | 4,280,000.00 USD | 6,370,000.00 USD | 4,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 455,190.00 USD | 455,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2206.80` | 110,370,000.00 USD | 110,370,000.00 USD | 17,370,000.00 USD | 3,390,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2207.00` | 91,210,000.00 USD | 91,210,000.00 USD | 9,400,000.00 USD | 2,400,000.00 USD | 780,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2209.40` | 78,620,000.00 USD | 78,620,000.00 USD | 7,190,000.00 USD | 8,460,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2209.60` | 85,960,000.00 USD | 85,960,000.00 USD | 2,260,000.00 USD | 0.00 USD | 9,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2211.80` | 57,830,000.00 USD | 57,830,000.00 USD | 10,640,000.00 USD | 5,740,000.00 USD | 4,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2212.40` | 74,550,000.00 USD | 74,550,000.00 USD | 6,450,000.00 USD | 1,980,000.00 USD | 11,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2214.20` | 37,090,000.00 USD | 37,090,000.00 USD | 6,070,000.00 USD | 5,040,000.00 USD | 102,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 412.88 USD | 412.88 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2215.20` | 55,120,000.00 USD | 55,120,000.00 USD | 0.00 USD | 0.00 USD | 495,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2216.60` | 25,880,000.00 USD | 25,880,000.00 USD | 522,020.00 USD | 2,260,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2218.00` | 54,630,000.00 USD | 54,630,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 70,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2219.00` | 20,540,000.00 USD | 20,540,000.00 USD | 6,820,000.00 USD | 2,420,000.00 USD | 3,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2220.80` | 31,670,000.00 USD | 31,670,000.00 USD | 0.00 USD | 6,120,000.00 USD | 10,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2221.40` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 4,950,000.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2223.60` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 6,100,000.00 USD | 8,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2223.80` | 494,970.00 USD | 494,970.00 USD | 168,380.00 USD | 300,160.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2225.00` | 778.75 USD | 778.75 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2226.20` | 6,600,000.00 USD | 6,600,000.00 USD | 2,980,000.00 USD | 3,480,000.00 USD | 147,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2226.40` | 5,430,000.00 USD | 5,430,000.00 USD | 324,830.00 USD | 0.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2228.60` | 25,150,000.00 USD | 25,150,000.00 USD | 0.00 USD | 13,040,000.00 USD | 5,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2229.20` | 26,580,000.00 USD | 26,580,000.00 USD | 2,140,000.00 USD | 0.00 USD | 19,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2231.00` | 65,930,000.00 USD | 65,930,000.00 USD | 40,420,000.00 USD | 0.00 USD | 361,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2232.00` | 30,520,000.00 USD | 30,520,000.00 USD | 0.00 USD | 0.00 USD | 3,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2233.40` | 66,090,000.00 USD | 66,090,000.00 USD | 0.00 USD | 0.00 USD | 162,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2234.80` | 45,160,000.00 USD | 45,160,000.00 USD | 0.00 USD | 14,300,000.00 USD | 350,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2235.00` | 2,120.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2237.60` | 64,230,000.00 USD | 64,230,000.00 USD | 11,730,000.00 USD | 7,340,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2238.20` | 78,050,000.00 USD | 78,050,000.00 USD | 11,960,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2240.40` | 99,700,000.00 USD | 99,700,000.00 USD | 35,470,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2240.60` | 81,310,000.00 USD | 81,310,000.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2243.00` | 82,200,000.00 USD | 82,200,000.00 USD | 271,140.00 USD | 569,860.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2243.20` | 102,880,000.00 USD | 102,880,000.00 USD | 2,910,000.00 USD | 268,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2245.40` | 87,190,000.00 USD | 87,190,000.00 USD | 1,040,000.00 USD | 2,910,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2246.00` | 114,880,000.00 USD | 114,880,000.00 USD | 2,290,000.00 USD | 1,300,000.00 USD | 8,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2247.80` | 105,680,000.00 USD | 105,680,000.00 USD | 7,200,000.00 USD | 5,800,000.00 USD | 5,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2248.80` | 130,720,000.00 USD | 130,720,000.00 USD | 7,600,000.00 USD | 6,990,000.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2250.20` | 111,900,000.00 USD | 111,900,000.00 USD | 5,800,000.00 USD | 365,980.00 USD | 55,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2251.60` | 152,900,000.00 USD | 152,900,000.00 USD | 10,510,000.00 USD | 11,670,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2252.60` | 115,910,000.00 USD | 115,910,000.00 USD | 850,700.00 USD | 1,770,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2254.40` | 160,790,000.00 USD | 160,790,000.00 USD | 885,200.00 USD | 6,600,000.00 USD | 406,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2255.00` | 140,850,000.00 USD | 140,850,000.00 USD | 12,360,000.00 USD | 6,830,000.00 USD | 5,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 20,070.00 USD | 22,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2257.20` | 206,090,000.00 USD | 206,090,000.00 USD | 29,680,000.00 USD | 8,620,000.00 USD | 7,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2257.40` | 174,380,000.00 USD | 174,380,000.00 USD | 19,840,000.00 USD | 7,960,000.00 USD | 5,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2259.80` | 194,020,000.00 USD | 194,020,000.00 USD | 9,190,000.00 USD | 9,590,000.00 USD | 859,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2260.00` | 213,800,000.00 USD | 213,800,000.00 USD | 0.00 USD | 3,670,000.00 USD | 4,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2262.20` | 220,620,000.00 USD | 220,620,000.00 USD | 11,700,000.00 USD | 6,910,000.00 USD | 7,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2262.80` | 222,260,000.00 USD | 222,260,000.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 280,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2264.60` | 246,340,000.00 USD | 246,340,000.00 USD | 6,910,000.00 USD | 11,430,000.00 USD | 7,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 13,280.00 USD | 36,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2265.60` | 224,990,000.00 USD | 224,990,000.00 USD | 0.00 USD | 2,510,000.00 USD | 218,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2267.00` | 276,860,000.00 USD | 276,860,000.00 USD | 9,850,000.00 USD | 9,000,000.00 USD | 11,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2268.40` | 256,930,000.00 USD | 256,930,000.00 USD | 11,010,000.00 USD | 5,790,000.00 USD | 15,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2269.40` | 321,340,000.00 USD | 321,340,000.00 USD | 21,800,000.00 USD | 9,800,000.00 USD | 12,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2271.20` | 291,670,000.00 USD | 291,670,000.00 USD | 17,870,000.00 USD | 3,500,000.00 USD | 13,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2271.80` | 346,060,000.00 USD | 346,060,000.00 USD | 7,280,000.00 USD | 6,790,000.00 USD | 10,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2274.00` | 317,000,000.00 USD | 317,000,000.00 USD | 15,420,000.00 USD | 7,040,000.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2274.20` | 367,800,000.00 USD | 367,800,000.00 USD | 11,490,000.00 USD | 6,900,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 1,610,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2276.60` | 429,040,000.00 USD | 429,040,000.00 USD | 29,880,000.00 USD | 19,450,000.00 USD | 11,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2276.80` | 326,100,000.00 USD | 326,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2279.00` | 458,010,000.00 USD | 458,010,000.00 USD | 11,040,000.00 USD | 5,320,000.00 USD | 12,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2279.60` | 373,620,000.00 USD | 373,620,000.00 USD | 3,230,000.00 USD | 30,300,000.00 USD | 13,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2281.40` | 515,600,000.00 USD | 515,600,000.00 USD | 31,660,000.00 USD | 25,130,000.00 USD | 800,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.40` | 453,880,000.00 USD | 453,880,000.00 USD | 0.00 USD | 66,580,000.00 USD | 13,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2283.80` | 562,150,000.00 USD | 562,150,000.00 USD | 22,270,000.00 USD | 11,570,000.00 USD | 12,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 183,890.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2285.20` | 487,570,000.00 USD | 487,570,000.00 USD | 6,610,000.00 USD | 26,950,000.00 USD | 140,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2286.20` | 587,700,000.00 USD | 587,700,000.00 USD | 4,520,000.00 USD | 13,210,000.00 USD | 7,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2288.00` | 514,330,000.00 USD | 514,330,000.00 USD | 8,380,000.00 USD | 6,500,000.00 USD | 11,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2288.60` | 610,630,000.00 USD | 610,630,000.00 USD | 12,720,000.00 USD | 7,200,000.00 USD | 3,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2290.80` | 527,520,000.00 USD | 527,520,000.00 USD | 4,310,000.00 USD | 3,340,000.00 USD | 5,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2291.00` | 650,700,000.00 USD | 650,700,000.00 USD | 20,070,000.00 USD | 11,790,000.00 USD | 8,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2293.40` | 677,980,000.00 USD | 677,980,000.00 USD | 13,490,000.00 USD | 5,110,000.00 USD | 8,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2293.60` | 544,870,000.00 USD | 544,870,000.00 USD | 8,930,000.00 USD | 0.00 USD | 8,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 3,010,000.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2295.80` | 709,020,000.00 USD | 709,020,000.00 USD | 9,310,000.00 USD | 13,540,000.00 USD | 8,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2296.40` | 600,540,000.00 USD | 600,540,000.00 USD | 28,890,000.00 USD | 9,570,000.00 USD | 17,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2298.20` | 761,590,000.00 USD | 761,590,000.00 USD | 32,280,000.00 USD | 13,940,000.00 USD | 6,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.20` | 634,390,000.00 USD | 634,390,000.00 USD | 18,930,000.00 USD | 14,430,000.00 USD | 487,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2300.60` | 794,670,000.00 USD | 794,670,000.00 USD | 8,900,000.00 USD | 10,170,000.00 USD | 14,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.00` | 689,860,000.00 USD | 689,860,000.00 USD | 16,020,000.00 USD | 17,380,000.00 USD | 22,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2303.00` | 825,600,000.00 USD | 825,600,000.00 USD | 17,940,000.00 USD | 5,770,000.00 USD | 7,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2304.80` | 714,260,000.00 USD | 714,260,000.00 USD | 10,940,000.00 USD | 4,600,000.00 USD | 8,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 670,610.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.40` | 860,460,000.00 USD | 860,460,000.00 USD | 12,190,000.00 USD | 15,330,000.00 USD | 7,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2307.60` | 729,180,000.00 USD | 729,180,000.00 USD | 7,580,000.00 USD | 5,150,000.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2307.80` | 869,720,000.00 USD | 869,720,000.00 USD | 4,390,000.00 USD | 2,880,000.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2310.20` | 889,080,000.00 USD | 889,080,000.00 USD | 5,980,000.00 USD | 2,740,000.00 USD | 10,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2310.40` | 748,720,000.00 USD | 748,720,000.00 USD | 11,460,000.00 USD | 2,720,000.00 USD | 5,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2312.60` | 903,410,000.00 USD | 903,410,000.00 USD | 5,450,000.00 USD | 7,690,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2313.20` | 766,470,000.00 USD | 766,470,000.00 USD | 1,200,000.00 USD | 3,490,000.00 USD | 13,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2315.00` | 922,820,000.00 USD | 922,820,000.00 USD | 5,440,000.00 USD | 12,280,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 5,890,000.00 USD | 11,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2316.00` | 773,000,000.00 USD | 773,000,000.00 USD | 0.00 USD | 5,780,000.00 USD | 749,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2317.40` | 948,840,000.00 USD | 948,840,000.00 USD | 7,540,000.00 USD | 10,540,000.00 USD | 7,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2318.80` | 792,990,000.00 USD | 792,990,000.00 USD | 6,560,000.00 USD | 5,250,000.00 USD | 8,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2319.80` | 972,460,000.00 USD | 972,460,000.00 USD | 9,790,000.00 USD | 10,770,000.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2321.60` | 810,210,000.00 USD | 810,210,000.00 USD | 1,190,000.00 USD | 15,930,000.00 USD | 108,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2322.20` | 991,140,000.00 USD | 991,140,000.00 USD | 3,420,000.00 USD | 10,510,000.00 USD | 4,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2324.40` | 818,570,000.00 USD | 818,570,000.00 USD | 4,670,000.00 USD | 1,970,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2324.60` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 2,540,000.00 USD | 9,500,000.00 USD | 519,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,780,000.00 USD | 13,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2327.00` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 949,090.00 USD | 945,500.00 USD | 5,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2327.20` | 834,490,000.00 USD | 834,490,000.00 USD | 6,590,000.00 USD | 805,740.00 USD | 8,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2329.40` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 9,320,000.00 USD | 2,530,000.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2330.00` | 855,990,000.00 USD | 855,990,000.00 USD | 13,230,000.00 USD | 363,770.00 USD | 7,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2331.80` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 3,190,000.00 USD | 2,970,000.00 USD | 1,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2332.80` | 883,900,000.00 USD | 883,900,000.00 USD | 19,860,000.00 USD | 8,000,000.00 USD | 54,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2334.20` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 7,690,000.00 USD | 4,790,000.00 USD | 8,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 427,950.00 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2335.60` | 940,830,000.00 USD | 940,830,000.00 USD | 31,150,000.00 USD | 12,430,000.00 USD | 13,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2336.60` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 13,510,000.00 USD | 1,880,000.00 USD | 4,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.40` | 966,510,000.00 USD | 966,510,000.00 USD | 14,040,000.00 USD | 0.00 USD | 11,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2339.00` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 7,770,000.00 USD | 3,990,000.00 USD | 5,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2341.20` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 4,720,000.00 USD | 17,820,000.00 USD | 14,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2341.40` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 7,800,000.00 USD | 4,080,000.00 USD | 11,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2343.80` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 7,550,000.00 USD | 8,510,000.00 USD | 6,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2344.00` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 6,380,000.00 USD | 4,940,000.00 USD | 5,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 417,120.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2346.20` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 3,850,000.00 USD | 2,750,000.00 USD | 3,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2346.80` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 19,690,000.00 USD | 19,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2348.60` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 7,490,000.00 USD | 6,650,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2349.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 1,320,000.00 USD | 15,110,000.00 USD | 16,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2351.00` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 24,320,000.00 USD | 4,950,000.00 USD | 11,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2352.40` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 2,710,000.00 USD | 22,900,000.00 USD | 5,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2353.40` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 3,010,000.00 USD | 2,970,000.00 USD | 652,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,790,000.00 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2355.20` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 18,340,000.00 USD | 27,760,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2355.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 4,450,000.00 USD | 2,950,000.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.00` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 5,360,000.00 USD | 1,840,000.00 USD | 4,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2358.20` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 3,900,000.00 USD | 4,470,000.00 USD | 6,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.60` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 9,930,000.00 USD | 3,880,000.00 USD | 1,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2360.80` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 4,470,000.00 USD | 3,430,000.00 USD | 254,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2363.00` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 5,390,000.00 USD | 9,200,000.00 USD | 7,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2363.60` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 4,570,000.00 USD | 373,740.00 USD | 6,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 5,520,000.00 USD | 21,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2365.40` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 4,890,000.00 USD | 658,050.00 USD | 3,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2366.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 4,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.80` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 3,010,000.00 USD | 2,080,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2369.20` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 21,280,000.00 USD | 475,460.00 USD | 13,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.20` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 10,560,000.00 USD | 7,300,000.00 USD | 5,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2372.00` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 15,540,000.00 USD | 0.00 USD | 41,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.60` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 13,770,000.00 USD | 2,610,000.00 USD | 5,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2374.80` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2375.00` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 8,510,000.00 USD | 557,400.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 885,750.00 USD | 22,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2377.40` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 3,730,000.00 USD | 3,470,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2377.60` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 8,770,000.00 USD | 6,190,000.00 USD | 15,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2379.80` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 6,370,000.00 USD | 389,290.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2380.40` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 6,830,000.00 USD | 2,590,000.00 USD | 22,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2382.20` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 8,260,000.00 USD | 8,360,000.00 USD | 11,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2383.20` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 8,610,000.00 USD | 15,780,000.00 USD | 24,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2384.60` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 11,820,000.00 USD | 12,030,000.00 USD | 5,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 726,570.00 USD | 22,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2386.00` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 15,430,000.00 USD | 37,810,000.00 USD | 43,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2387.00` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 7,590,000.00 USD | 7,070,000.00 USD | 4,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.80` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 5,490,000.00 USD | 26,450,000.00 USD | 31,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2389.40` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 9,610,000.00 USD | 6,800,000.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.60` | 1,700,000,000.00 USD | 1,700,000,000.00 USD | 7,580,000.00 USD | 49,400,000.00 USD | 36,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2391.80` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 451,370.00 USD | 3,710,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2394.20` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 4,450,000.00 USD | 2,780,000.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.40` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 57,060,000.00 USD | 26,270,000.00 USD | 35,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,840,000.00 USD | 27,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2396.60` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 64,150.00 USD | 1,150,000.00 USD | 2,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2397.20` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 25,000,000.00 USD | 39,300,000.00 USD | 21,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2399.00` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 2,150,000.00 USD | 3,200,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2400.00` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 48,240,000.00 USD | 26,850,000.00 USD | 22,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2401.40` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 642,440.00 USD | 62,980.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2402.80` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 53,160,000.00 USD | 21,040,000.00 USD | 27,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2403.80` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 3,400,000.00 USD | 3,030,000.00 USD | 1,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 156,110.00 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2405.60` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 26,730,000.00 USD | 29,760,000.00 USD | 16,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2406.20` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 9,420,000.00 USD | 3,430,000.00 USD | 4,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2408.40` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 27,050,000.00 USD | 26,540,000.00 USD | 26,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2408.60` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 2,450,000.00 USD | 1,330,000.00 USD | 673,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2411.00` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 3,410,000.00 USD | 4,350,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.20` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 17,990,000.00 USD | 19,900,000.00 USD | 20,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.40` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 5,430,000.00 USD | 2,470,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.00` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 19,190,000.00 USD | 22,460,000.00 USD | 20,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 143,210.00 USD | 28,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.80` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 2,710,000.00 USD | 2,310,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2416.80` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 23,820,000.00 USD | 6,390,000.00 USD | 21,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2418.20` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 3,310,000.00 USD | 2,000,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2419.60` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 27,160,000.00 USD | 17,310,000.00 USD | 10,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2420.60` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 5,840,000.00 USD | 4,110,000.00 USD | 4,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2422.40` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 21,450,000.00 USD | 20,430,000.00 USD | 13,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2423.00` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 770,750.00 USD | 1,540,000.00 USD | 2,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 243,520.00 USD | 28,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2425.20` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 11,030,000.00 USD | 13,240,000.00 USD | 22,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2425.40` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 1,280,000.00 USD | 623,850.00 USD | 621,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2427.80` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 1,490,000.00 USD | 1,520,000.00 USD | 609,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2428.00` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 19,050,000.00 USD | 10,460,000.00 USD | 12,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.20` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 1,370,000.00 USD | 1,550,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2430.80` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 7,240,000.00 USD | 12,690,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.60` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 2,770,000.00 USD | 2,230,000.00 USD | 682,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2433.60` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 14,430,000.00 USD | 5,270,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2435.00` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 2,480,000.00 USD | 545,610.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 187,830.00 USD | 28,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2436.40` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 6,380,000.00 USD | 5,300,000.00 USD | 5,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2437.40` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 967,690.00 USD | 1,050,000.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2439.20` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 13,780,000.00 USD | 7,040,000.00 USD | 5,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2439.80` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 1,640,000.00 USD | 502,040.00 USD | 304,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2442.00` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 5,970,000.00 USD | 4,860,000.00 USD | 7,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2442.20` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 1,040,000.00 USD | 743,640.00 USD | 565,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2444.60` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 13,780.00 USD | 486,350.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.80` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 9,830,000.00 USD | 8,980,000.00 USD | 8,630,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 135,670.00 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2447.00` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 1,090,000.00 USD | 848,560.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.60` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 8,340,000.00 USD | 3,080,000.00 USD | 12,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2449.40` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 321,220.00 USD | 257,760.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2450.40` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 8,460,000.00 USD | 6,640,000.00 USD | 9,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2451.80` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 2,860,000.00 USD | 1,690,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2453.20` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 7,290,000.00 USD | 3,760,000.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2454.20` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 2,640,000.00 USD | 2,210,000.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 5,180,000.00 USD | 33,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2456.00` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 5,780,000.00 USD | 5,730,000.00 USD | 6,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2456.60` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 1,080,000.00 USD | 1,900,000.00 USD | 841,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2458.80` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 4,440,000.00 USD | 5,910,000.00 USD | 6,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2459.00` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 1,710,000.00 USD | 1,290,000.00 USD | 16,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2461.40` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 540,100.00 USD | 350,490.00 USD | 379,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2461.60` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 6,280,000.00 USD | 6,710,000.00 USD | 6,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2463.80` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 358,460.00 USD | 940,830.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.40` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 4,990,000.00 USD | 2,040,000.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 67,480,000.00 USD | 101,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2466.20` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 510,000.00 USD | 885,870.00 USD | 550,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.20` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 3,670,000.00 USD | 3,120,000.00 USD | 608,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2468.60` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 288,920.00 USD | 1,810,000.00 USD | 555,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.00` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 3,190,000.00 USD | 2,290,000.00 USD | 408,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2471.00` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 1,380,000.00 USD | 284,850.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2472.80` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 4,410,000.00 USD | 2,420,000.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 197,560.00 USD | 101,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2475.60` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 4,390,000.00 USD | 1,420,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2478.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 3,140,000.00 USD | 4,910,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2481.20` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 729,480.00 USD | 3,680,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.00` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 52,650.00 USD | 101,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2486.80` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 30,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2489.60` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 630,050.00 USD | 225,530.00 USD | 52,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2492.40` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 3,000,000.00 USD | 1,020,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 2,220,000.00 USD | 103,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2495.20` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 773,650.00 USD | 736,470.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2498.00` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 602,570.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 4,470,000.00 USD | 108,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `7D` | `1971.60` | 735,760,000.00 USD | 0.00 USD | 735,760,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD |
| `7D` | `1974.40` | 735,630,000.00 USD | 0.00 USD | 735,630,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD |
| `7D` | `1977.20` | 735,580,000.00 USD | 0.00 USD | 735,580,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1982.80` | 733,340,000.00 USD | 0.00 USD | 733,340,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD |
| `7D` | `1985.60` | 733,130,000.00 USD | 0.00 USD | 733,130,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1988.40` | 730,840,000.00 USD | 0.00 USD | 730,840,000.00 USD | 1,440,000.00 USD | 1,780,000.00 USD | 0.00 USD |
| `7D` | `1991.20` | 727,630,000.00 USD | 0.00 USD | 727,630,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 38,060.00 USD |
| `7D` | `1994.00` | 724,880,000.00 USD | 0.00 USD | 724,880,000.00 USD | 0.00 USD | 0.00 USD | 808,380.00 USD |
| `7D` | `1996.80` | 724,070,000.00 USD | 0.00 USD | 724,070,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1998.20` | 600,230,000.00 USD | 0.00 USD | 600,230,000.00 USD | 219,590.00 USD | 104,180.00 USD | 24,170.00 USD |
| `1D` | `2000.60` | 599,880,000.00 USD | 0.00 USD | 599,880,000.00 USD | 13,780.00 USD | 236,510.00 USD | 586,930.00 USD |
| `7D` | `2002.40` | 722,730,000.00 USD | 0.00 USD | 722,730,000.00 USD | 0.00 USD | 0.00 USD | 594,510.00 USD |
| `1D` | `2003.00` | 599,040,000.00 USD | 0.00 USD | 599,040,000.00 USD | 616,980.00 USD | 601,340.00 USD | 478,890.00 USD |
| `7D` | `2005.20` | 722,140,000.00 USD | 0.00 USD | 722,140,000.00 USD | 0.00 USD | 742,090.00 USD | 0.00 USD |
| `1D` | `2005.40` | 597,340,000.00 USD | 0.00 USD | 597,340,000.00 USD | 493,990.00 USD | 13,410.00 USD | 0.00 USD |
| `1D` | `2007.80` | 596,840,000.00 USD | 0.00 USD | 596,840,000.00 USD | 0.00 USD | 558,480.00 USD | 126,940.00 USD |
| `7D` | `2008.00` | 721,390,000.00 USD | 0.00 USD | 721,390,000.00 USD | 807,770.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2010.20` | 596,150,000.00 USD | 0.00 USD | 596,150,000.00 USD | 484,920.00 USD | 463,210.00 USD | 362,200.00 USD |
| `7D` | `2010.80` | 720,590,000.00 USD | 0.00 USD | 720,590,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD |
| `1D` | `2012.60` | 594,840,000.00 USD | 0.00 USD | 594,840,000.00 USD | 323,800.00 USD | 266,130.00 USD | 25,520.00 USD |
| `1D` | `2015.00` | 594,220,000.00 USD | 0.00 USD | 594,220,000.00 USD | 355,800.00 USD | 159,880.00 USD | 188,020.00 USD |
| `1D` | `2017.40` | 593,520,000.00 USD | 0.00 USD | 593,520,000.00 USD | 537,580.00 USD | 1,350,000.00 USD | 559,250.00 USD |
| `7D` | `2019.20` | 719,630,000.00 USD | 0.00 USD | 719,630,000.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD |
| `1D` | `2019.80` | 591,080,000.00 USD | 0.00 USD | 591,080,000.00 USD | 326,370.00 USD | 1,140,000.00 USD | 166,650.00 USD |
| `7D` | `2022.00` | 719,610,000.00 USD | 0.00 USD | 719,610,000.00 USD | 0.00 USD | 0.00 USD | 934,340.00 USD |
| `1D` | `2022.20` | 589,440,000.00 USD | 0.00 USD | 589,440,000.00 USD | 1,380,000.00 USD | 333,050.00 USD | 1,490,000.00 USD |
| `1D` | `2024.60` | 586,240,000.00 USD | 0.00 USD | 586,240,000.00 USD | 197,740.00 USD | 1,010,000.00 USD | 822,450.00 USD |
| `7D` | `2024.80` | 718,680,000.00 USD | 0.00 USD | 718,680,000.00 USD | 1,070,000.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2027.00` | 584,220,000.00 USD | 0.00 USD | 584,220,000.00 USD | 1,390,000.00 USD | 233,420.00 USD | 196,350.00 USD |
| `7D` | `2027.60` | 717,430,000.00 USD | 0.00 USD | 717,430,000.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2029.40` | 582,400,000.00 USD | 0.00 USD | 582,400,000.00 USD | 1,680,000.00 USD | 1,300,000.00 USD | 775,050.00 USD |
| `7D` | `2030.40` | 716,330,000.00 USD | 0.00 USD | 716,330,000.00 USD | 0.00 USD | 3,320,000.00 USD | 1,080,000.00 USD |
| `1D` | `2031.80` | 578,640,000.00 USD | 0.00 USD | 578,640,000.00 USD | 1,290,000.00 USD | 156,850.00 USD | 1,030,000.00 USD |
| `7D` | `2033.20` | 711,930,000.00 USD | 0.00 USD | 711,930,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD |
| `1D` | `2034.20` | 576,160,000.00 USD | 0.00 USD | 576,160,000.00 USD | 1,110,000.00 USD | 1,330,000.00 USD | 165,760.00 USD |
| `7D` | `2036.00` | 710,370,000.00 USD | 0.00 USD | 710,370,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD |
| `1D` | `2036.60` | 573,560,000.00 USD | 0.00 USD | 573,560,000.00 USD | 119,600.00 USD | 177,360.00 USD | 30,580.00 USD |
| `7D` | `2038.80` | 710,040,000.00 USD | 0.00 USD | 710,040,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2039.00` | 573,230,000.00 USD | 0.00 USD | 573,230,000.00 USD | 939,380.00 USD | 300,240.00 USD | 357,840.00 USD |
| `1D` | `2041.40` | 571,630,000.00 USD | 0.00 USD | 571,630,000.00 USD | 626,840.00 USD | 178,560.00 USD | 188,590.00 USD |
| `1D` | `2043.80` | 570,640,000.00 USD | 0.00 USD | 570,640,000.00 USD | 0.00 USD | 0.00 USD | 16,940.00 USD |
| `7D` | `2044.40` | 708,590,000.00 USD | 0.00 USD | 708,590,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD |
| `1D` | `2046.20` | 570,620,000.00 USD | 0.00 USD | 570,620,000.00 USD | 467,370.00 USD | 0.00 USD | 19,040.00 USD |
| `1D` | `2048.60` | 570,130,000.00 USD | 0.00 USD | 570,130,000.00 USD | 51,070.00 USD | 0.00 USD | 357,950.00 USD |
| `7D` | `2050.00` | 708,290,000.00 USD | 0.00 USD | 708,290,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2051.00` | 569,730,000.00 USD | 0.00 USD | 569,730,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2052.80` | 708,060,000.00 USD | 0.00 USD | 708,060,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2053.40` | 568,670,000.00 USD | 0.00 USD | 568,670,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD |
| `1D` | `2055.80` | 568,550,000.00 USD | 0.00 USD | 568,550,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2058.20` | 568,310,000.00 USD | 0.00 USD | 568,310,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2058.40` | 705,780,000.00 USD | 0.00 USD | 705,780,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2061.20` | 705,440,000.00 USD | 0.00 USD | 705,440,000.00 USD | 1,600,000.00 USD | 1,120,000.00 USD | 1,710,000.00 USD |
| `1D` | `2063.00` | 567,550,000.00 USD | 0.00 USD | 567,550,000.00 USD | 0.00 USD | 111,540.00 USD | 20,330.00 USD |
| `7D` | `2064.00` | 701,010,000.00 USD | 0.00 USD | 701,010,000.00 USD | 1,050,000.00 USD | 826,260.00 USD | 945,860.00 USD |
| `1D` | `2065.40` | 567,420,000.00 USD | 0.00 USD | 567,420,000.00 USD | 563,140.00 USD | 485,130.00 USD | 510,200.00 USD |
| `7D` | `2066.80` | 698,180,000.00 USD | 0.00 USD | 698,180,000.00 USD | 476,480.00 USD | 1,340,000.00 USD | 200,040.00 USD |
| `1D` | `2067.80` | 565,860,000.00 USD | 0.00 USD | 565,860,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD |
| `7D` | `2069.60` | 696,170,000.00 USD | 0.00 USD | 696,170,000.00 USD | 1,510,000.00 USD | 2,770,000.00 USD | 1,300,000.00 USD |
| `1D` | `2070.20` | 565,170,000.00 USD | 0.00 USD | 565,170,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD |
| `7D` | `2072.40` | 690,590,000.00 USD | 0.00 USD | 690,590,000.00 USD | 4,460,000.00 USD | 1,850,000.00 USD | 1,550,000.00 USD |
| `1D` | `2072.60` | 564,800,000.00 USD | 0.00 USD | 564,800,000.00 USD | 47,910.00 USD | 555,250.00 USD | 420,170.00 USD |
| `1D` | `2075.00` | 563,770,000.00 USD | 0.00 USD | 563,770,000.00 USD | 25,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2075.20` | 682,740,000.00 USD | 0.00 USD | 682,740,000.00 USD | 4,080,000.00 USD | 3,180,000.00 USD | 4,010,000.00 USD |
| `1D` | `2077.40` | 563,750,000.00 USD | 0.00 USD | 563,750,000.00 USD | 354,080.00 USD | 25,190.00 USD | 0.00 USD |
| `7D` | `2078.00` | 671,470,000.00 USD | 0.00 USD | 671,470,000.00 USD | 3,750,000.00 USD | 3,040,000.00 USD | 1,570,000.00 USD |
| `1D` | `2079.80` | 563,370,000.00 USD | 0.00 USD | 563,370,000.00 USD | 55,820.00 USD | 15,600.00 USD | 199,420.00 USD |
| `7D` | `2080.80` | 663,110,000.00 USD | 0.00 USD | 663,110,000.00 USD | 4,230,000.00 USD | 2,970,000.00 USD | 2,480,000.00 USD |
| `1D` | `2082.20` | 563,100,000.00 USD | 0.00 USD | 563,100,000.00 USD | 850,080.00 USD | 18,240.00 USD | 208,160.00 USD |
| `7D` | `2083.60` | 653,430,000.00 USD | 0.00 USD | 653,430,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 2,300,000.00 USD |
| `1D` | `2084.60` | 562,020,000.00 USD | 0.00 USD | 562,020,000.00 USD | 528,660.00 USD | 207,610.00 USD | 486,720.00 USD |
| `7D` | `2086.40` | 648,770,000.00 USD | 0.00 USD | 648,770,000.00 USD | 4,830,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD |
| `1D` | `2087.00` | 560,800,000.00 USD | 0.00 USD | 560,800,000.00 USD | 551,330.00 USD | 370,040.00 USD | 639,240.00 USD |
| `7D` | `2089.20` | 636,670,000.00 USD | 0.00 USD | 636,670,000.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD |
| `1D` | `2089.40` | 559,240,000.00 USD | 0.00 USD | 559,240,000.00 USD | 152,210.00 USD | 218,010.00 USD | 108,650.00 USD |
| `1D` | `2091.80` | 558,760,000.00 USD | 0.00 USD | 558,760,000.00 USD | 1,010,000.00 USD | 338,870.00 USD | 450,880.00 USD |
| `7D` | `2092.00` | 630,460,000.00 USD | 0.00 USD | 630,460,000.00 USD | 3,470,000.00 USD | 293,650.00 USD | 6,500,000.00 USD |
| `1D` | `2094.20` | 556,950,000.00 USD | 0.00 USD | 556,950,000.00 USD | 1,920,000.00 USD | 881,690.00 USD | 1,060,000.00 USD |
| `7D` | `2094.80` | 620,200,000.00 USD | 0.00 USD | 620,200,000.00 USD | 5,040,000.00 USD | 2,120,000.00 USD | 1,390,000.00 USD |
| `1D` | `2096.60` | 553,080,000.00 USD | 0.00 USD | 553,080,000.00 USD | 516,470.00 USD | 465,510.00 USD | 828,360.00 USD |
| `7D` | `2097.60` | 611,650,000.00 USD | 0.00 USD | 611,650,000.00 USD | 1,830,000.00 USD | 3,350,000.00 USD | 1,290,000.00 USD |
| `1D` | `2099.00` | 551,270,000.00 USD | 0.00 USD | 551,270,000.00 USD | 330,040.00 USD | 989,450.00 USD | 248,570.00 USD |
| `7D` | `2100.40` | 605,180,000.00 USD | 0.00 USD | 605,180,000.00 USD | 1,810,000.00 USD | 1,580,000.00 USD | 3,310,000.00 USD |
| `1D` | `2101.40` | 549,710,000.00 USD | 0.00 USD | 549,710,000.00 USD | 46,810.00 USD | 334,210.00 USD | 534,250.00 USD |
| `7D` | `2103.20` | 598,490,000.00 USD | 0.00 USD | 598,490,000.00 USD | 679,880.00 USD | 554,710.00 USD | 2,250,000.00 USD |
| `1D` | `2103.80` | 548,790,000.00 USD | 0.00 USD | 548,790,000.00 USD | 753,840.00 USD | 391,570.00 USD | 8,780.00 USD |
| `7D` | `2106.00` | 595,000,000.00 USD | 0.00 USD | 595,000,000.00 USD | 1,560,000.00 USD | 986,590.00 USD | 1,560,000.00 USD |
| `1D` | `2106.20` | 547,640,000.00 USD | 0.00 USD | 547,640,000.00 USD | 3,130,000.00 USD | 886,560.00 USD | 1,170,000.00 USD |
| `1D` | `2108.60` | 542,450,000.00 USD | 0.00 USD | 542,450,000.00 USD | 656,240.00 USD | 21,400.00 USD | 6,190.00 USD |
| `7D` | `2108.80` | 590,890,000.00 USD | 0.00 USD | 590,890,000.00 USD | 8,350,000.00 USD | 1,600,000.00 USD | 1,820,000.00 USD |
| `1D` | `2111.00` | 541,770,000.00 USD | 0.00 USD | 541,770,000.00 USD | 450,470.00 USD | 81,050.00 USD | 0.00 USD |
| `7D` | `2111.60` | 579,120,000.00 USD | 0.00 USD | 579,120,000.00 USD | 2,990,000.00 USD | 1,140,000.00 USD | 1,340,000.00 USD |
| `1D` | `2113.40` | 541,240,000.00 USD | 0.00 USD | 541,240,000.00 USD | 452,130.00 USD | 520,660.00 USD | 249,040.00 USD |
| `7D` | `2114.40` | 573,650,000.00 USD | 0.00 USD | 573,650,000.00 USD | 1,080,000.00 USD | 2,330,000.00 USD | 3,840,000.00 USD |
| `1D` | `2115.80` | 540,020,000.00 USD | 0.00 USD | 540,020,000.00 USD | 722,960.00 USD | 315,330.00 USD | 935,080.00 USD |
| `7D` | `2117.20` | 566,390,000.00 USD | 0.00 USD | 566,390,000.00 USD | 2,410,000.00 USD | 1,830,000.00 USD | 2,000,000.00 USD |
| `1D` | `2118.20` | 538,040,000.00 USD | 0.00 USD | 538,040,000.00 USD | 4,580,000.00 USD | 3,940,000.00 USD | 302,800.00 USD |
| `7D` | `2120.00` | 560,160,000.00 USD | 0.00 USD | 560,160,000.00 USD | 13,440,000.00 USD | 5,380,000.00 USD | 2,110,000.00 USD |
| `1D` | `2120.60` | 529,220,000.00 USD | 0.00 USD | 529,220,000.00 USD | 5,670,000.00 USD | 1,980,000.00 USD | 671,270.00 USD |
| `7D` | `2122.80` | 539,230,000.00 USD | 0.00 USD | 539,230,000.00 USD | 4,100,000.00 USD | 4,620,000.00 USD | 1,980,000.00 USD |
| `1D` | `2123.00` | 520,900,000.00 USD | 0.00 USD | 520,900,000.00 USD | 5,450,000.00 USD | 1,840,000.00 USD | 2,660,000.00 USD |
| `1D` | `2125.40` | 510,950,000.00 USD | 0.00 USD | 510,950,000.00 USD | 3,930,000.00 USD | 2,390,000.00 USD | 1,320,000.00 USD |
| `7D` | `2125.60` | 528,520,000.00 USD | 0.00 USD | 528,520,000.00 USD | 6,230,000.00 USD | 7,150,000.00 USD | 2,430,000.00 USD |
| `1D` | `2127.80` | 503,310,000.00 USD | 0.00 USD | 503,310,000.00 USD | 4,430,000.00 USD | 3,780,000.00 USD | 745,430.00 USD |
| `7D` | `2128.40` | 512,710,000.00 USD | 0.00 USD | 512,710,000.00 USD | 4,290,000.00 USD | 1,960,000.00 USD | 3,980,000.00 USD |
| `1D` | `2130.20` | 494,350,000.00 USD | 0.00 USD | 494,350,000.00 USD | 1,250,000.00 USD | 18,610.00 USD | 774,790.00 USD |
| `7D` | `2131.20` | 502,480,000.00 USD | 0.00 USD | 502,480,000.00 USD | 1,980,000.00 USD | 1,810,000.00 USD | 1,360,000.00 USD |
| `1D` | `2132.60` | 492,310,000.00 USD | 0.00 USD | 492,310,000.00 USD | 81,820.00 USD | 284,820.00 USD | 1,530,000.00 USD |
| `7D` | `2134.00` | 497,330,000.00 USD | 0.00 USD | 497,330,000.00 USD | 2,270,000.00 USD | 617,060.00 USD | 308,060.00 USD |
| `1D` | `2135.00` | 490,420,000.00 USD | 0.00 USD | 490,420,000.00 USD | 1,430,000.00 USD | 2,070,000.00 USD | 1,140,000.00 USD |
| `7D` | `2136.80` | 494,140,000.00 USD | 0.00 USD | 494,140,000.00 USD | 1,850,000.00 USD | 1,510,000.00 USD | 2,120,000.00 USD |
| `1D` | `2137.40` | 485,780,000.00 USD | 0.00 USD | 485,780,000.00 USD | 660,230.00 USD | 1,670,000.00 USD | 560,020.00 USD |
| `7D` | `2139.60` | 488,660,000.00 USD | 0.00 USD | 488,660,000.00 USD | 1,110,000.00 USD | 2,190,000.00 USD | 635,670.00 USD |
| `1D` | `2139.80` | 482,890,000.00 USD | 0.00 USD | 482,890,000.00 USD | 1,470,000.00 USD | 367,550.00 USD | 64,360.00 USD |
| `1D` | `2142.20` | 480,990,000.00 USD | 0.00 USD | 480,990,000.00 USD | 522,990.00 USD | 3,160,000.00 USD | 876,300.00 USD |
| `7D` | `2142.40` | 484,720,000.00 USD | 0.00 USD | 484,720,000.00 USD | 4,320,000.00 USD | 1,100,000.00 USD | 434,750.00 USD |
| `1D` | `2144.60` | 476,430,000.00 USD | 0.00 USD | 476,430,000.00 USD | 2,860,000.00 USD | 2,330,000.00 USD | 1,210,000.00 USD |
| `7D` | `2145.20` | 478,870,000.00 USD | 0.00 USD | 478,870,000.00 USD | 2,210,000.00 USD | 1,760,000.00 USD | 1,720,000.00 USD |
| `1D` | `2147.00` | 470,030,000.00 USD | 0.00 USD | 470,030,000.00 USD | 1,570,000.00 USD | 1,340,000.00 USD | 69,830.00 USD |
| `7D` | `2148.00` | 473,180,000.00 USD | 0.00 USD | 473,180,000.00 USD | 26,270.00 USD | 538,910.00 USD | 134,420.00 USD |
| `1D` | `2149.40` | 467,050,000.00 USD | 0.00 USD | 467,050,000.00 USD | 7,120,000.00 USD | 1,670,000.00 USD | 1,960,000.00 USD |
| `7D` | `2150.80` | 472,480,000.00 USD | 0.00 USD | 472,480,000.00 USD | 0.00 USD | 363,770.00 USD | 317,870.00 USD |
| `1D` | `2151.80` | 456,300,000.00 USD | 0.00 USD | 456,300,000.00 USD | 2,620,000.00 USD | 3,960,000.00 USD | 2,530,000.00 USD |
| `7D` | `2153.60` | 471,790,000.00 USD | 0.00 USD | 471,790,000.00 USD | 11,230,000.00 USD | 603,900.00 USD | 1,640,000.00 USD |
| `1D` | `2154.20` | 447,190,000.00 USD | 0.00 USD | 447,190,000.00 USD | 1,160,000.00 USD | 3,480,000.00 USD | 853,190.00 USD |
| `7D` | `2156.40` | 458,330,000.00 USD | 0.00 USD | 458,330,000.00 USD | 2,500,000.00 USD | 1,710,000.00 USD | 1,200,000.00 USD |
| `1D` | `2156.60` | 441,700,000.00 USD | 0.00 USD | 441,700,000.00 USD | 5,700,000.00 USD | 1,610,000.00 USD | 2,990,000.00 USD |
| `1D` | `2159.00` | 431,390,000.00 USD | 0.00 USD | 431,390,000.00 USD | 1,820,000.00 USD | 2,320,000.00 USD | 4,580,000.00 USD |
| `7D` | `2159.20` | 452,920,000.00 USD | 0.00 USD | 452,920,000.00 USD | 4,780,000.00 USD | 1,330,000.00 USD | 5,170,000.00 USD |
| `1D` | `2161.40` | 422,670,000.00 USD | 0.00 USD | 422,670,000.00 USD | 8,470,000.00 USD | 9,400,000.00 USD | 1,440,000.00 USD |
| `7D` | `2162.00` | 441,640,000.00 USD | 0.00 USD | 441,640,000.00 USD | 15,360,000.00 USD | 1,850,000.00 USD | 514,130.00 USD |
| `1D` | `2163.80` | 403,360,000.00 USD | 0.00 USD | 403,360,000.00 USD | 15,960,000.00 USD | 7,660,000.00 USD | 3,870,000.00 USD |
| `7D` | `2164.80` | 423,920,000.00 USD | 0.00 USD | 423,920,000.00 USD | 11,610,000.00 USD | 17,760,000.00 USD | 2,760,000.00 USD |
| `1D` | `2166.20` | 375,860,000.00 USD | 0.00 USD | 375,860,000.00 USD | 11,060,000.00 USD | 11,460,000.00 USD | 5,670,000.00 USD |
| `7D` | `2167.60` | 391,790,000.00 USD | 0.00 USD | 391,790,000.00 USD | 11,850,000.00 USD | 11,020,000.00 USD | 298,520.00 USD |
| `1D` | `2168.60` | 347,670,000.00 USD | 0.00 USD | 347,670,000.00 USD | 17,790,000.00 USD | 6,160,000.00 USD | 3,750,000.00 USD |
| `7D` | `2170.40` | 368,620,000.00 USD | 0.00 USD | 368,620,000.00 USD | 2,420,000.00 USD | 11,510,000.00 USD | 8,730,000.00 USD |
| `1D` | `2171.00` | 319,980,000.00 USD | 0.00 USD | 319,980,000.00 USD | 21,940,000.00 USD | 10,800,000.00 USD | 6,300,000.00 USD |
| `7D` | `2173.20` | 345,970,000.00 USD | 0.00 USD | 345,970,000.00 USD | 30,070,000.00 USD | 0.00 USD | 1,500,000.00 USD |
| `1D` | `2173.40` | 280,940,000.00 USD | 0.00 USD | 280,940,000.00 USD | 7,740,000.00 USD | 1,390,000.00 USD | 3,800,000.00 USD |
| `1D` | `2175.80` | 268,010,000.00 USD | 0.00 USD | 268,010,000.00 USD | 2,090,000.00 USD | 569,650.00 USD | 0.00 USD |
| `7D` | `2176.00` | 314,390,000.00 USD | 0.00 USD | 314,390,000.00 USD | 5,390,000.00 USD | 1,460,000.00 USD | 2,820,000.00 USD |
| `1D` | `2178.20` | 265,350,000.00 USD | 0.00 USD | 265,350,000.00 USD | 1,290,000.00 USD | 1,180,000.00 USD | 3,320,000.00 USD |
| `7D` | `2178.80` | 304,720,000.00 USD | 0.00 USD | 304,720,000.00 USD | 196,330.00 USD | 133,210.00 USD | 1,180,000.00 USD |
| `1D` | `2180.60` | 259,550,000.00 USD | 0.00 USD | 259,550,000.00 USD | 4,460,000.00 USD | 3,440,000.00 USD | 6,780,000.00 USD |
| `7D` | `2181.60` | 303,210,000.00 USD | 0.00 USD | 303,210,000.00 USD | 3,960,000.00 USD | 2,160,000.00 USD | 4,370,000.00 USD |
| `1D` | `2183.00` | 244,870,000.00 USD | 0.00 USD | 244,870,000.00 USD | 637,950.00 USD | 1,320,000.00 USD | 365,370.00 USD |
| `7D` | `2184.40` | 292,710,000.00 USD | 0.00 USD | 292,710,000.00 USD | 26,960,000.00 USD | 2,700,000.00 USD | 2,550,000.00 USD |
| `1D` | `2185.40` | 242,560,000.00 USD | 0.00 USD | 242,560,000.00 USD | 2,650,000.00 USD | 2,480,000.00 USD | 5,620,000.00 USD |
| `7D` | `2187.20` | 260,500,000.00 USD | 0.00 USD | 260,500,000.00 USD | 14,380,000.00 USD | 17,750,000.00 USD | 0.00 USD |
| `1D` | `2187.80` | 231,800,000.00 USD | 0.00 USD | 231,800,000.00 USD | 5,040,000.00 USD | 4,050,000.00 USD | 7,930,000.00 USD |
| `7D` | `2190.00` | 228,370,000.00 USD | 0.00 USD | 228,370,000.00 USD | 14,800,000.00 USD | 27,960,000.00 USD | 8,020,000.00 USD |
| `1D` | `2190.20` | 214,780,000.00 USD | 0.00 USD | 214,780,000.00 USD | 8,990,000.00 USD | 4,390,000.00 USD | 4,020,000.00 USD |
| `1D` | `2192.60` | 197,390,000.00 USD | 0.00 USD | 197,390,000.00 USD | 5,000,000.00 USD | 4,860,000.00 USD | 1,210,000.00 USD |
| `7D` | `2192.80` | 177,580,000.00 USD | 0.00 USD | 177,580,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,080,000.00 USD |
| `1D` | `2195.00` | 186,320,000.00 USD | 0.00 USD | 186,320,000.00 USD | 5,700,000.00 USD | 2,910,000.00 USD | 5,950,000.00 USD |
| `7D` | `2195.60` | 162,160,000.00 USD | 0.00 USD | 162,160,000.00 USD | 383,690.00 USD | 243,760.00 USD | 35,180.00 USD |
| `1D` | `2197.40` | 171,760,000.00 USD | 0.00 USD | 171,760,000.00 USD | 4,650,000.00 USD | 1,240,000.00 USD | 3,660,000.00 USD |
| `7D` | `2198.40` | 161,500,000.00 USD | 0.00 USD | 161,500,000.00 USD | 0.00 USD | 1,460,000.00 USD | 7,550,000.00 USD |
| `1D` | `2199.80` | 162,210,000.00 USD | 0.00 USD | 162,210,000.00 USD | 4,040,000.00 USD | 4,100,000.00 USD | 10,580,000.00 USD |
| `7D` | `2201.20` | 152,490,000.00 USD | 0.00 USD | 152,490,000.00 USD | 4,700,000.00 USD | 266,430.00 USD | 8,020,000.00 USD |
| `1D` | `2202.20` | 143,490,000.00 USD | 0.00 USD | 143,490,000.00 USD | 16,430,000.00 USD | 10,590,000.00 USD | 10,120,000.00 USD |
| `7D` | `2204.00` | 139,510,000.00 USD | 0.00 USD | 139,510,000.00 USD | 9,760,000.00 USD | 4,330,000.00 USD | 15,050,000.00 USD |
| `1D` | `2204.60` | 106,340,000.00 USD | 0.00 USD | 106,340,000.00 USD | 4,280,000.00 USD | 6,370,000.00 USD | 4,480,000.00 USD |
| `7D` | `2206.80` | 110,370,000.00 USD | 0.00 USD | 110,370,000.00 USD | 17,370,000.00 USD | 3,390,000.00 USD | 3,660,000.00 USD |
| `1D` | `2207.00` | 91,210,000.00 USD | 0.00 USD | 91,210,000.00 USD | 9,400,000.00 USD | 2,400,000.00 USD | 780,680.00 USD |
| `1D` | `2209.40` | 78,620,000.00 USD | 0.00 USD | 78,620,000.00 USD | 7,190,000.00 USD | 8,460,000.00 USD | 5,150,000.00 USD |
| `7D` | `2209.60` | 85,960,000.00 USD | 0.00 USD | 85,960,000.00 USD | 2,260,000.00 USD | 0.00 USD | 9,150,000.00 USD |
| `1D` | `2211.80` | 57,830,000.00 USD | 0.00 USD | 57,830,000.00 USD | 10,640,000.00 USD | 5,740,000.00 USD | 4,360,000.00 USD |
| `7D` | `2212.40` | 74,550,000.00 USD | 0.00 USD | 74,550,000.00 USD | 6,450,000.00 USD | 1,980,000.00 USD | 11,000,000.00 USD |
| `1D` | `2214.20` | 37,090,000.00 USD | 0.00 USD | 37,090,000.00 USD | 6,070,000.00 USD | 5,040,000.00 USD | 102,250.00 USD |
| `7D` | `2215.20` | 55,120,000.00 USD | 0.00 USD | 55,120,000.00 USD | 0.00 USD | 0.00 USD | 495,340.00 USD |
| `1D` | `2216.60` | 25,880,000.00 USD | 0.00 USD | 25,880,000.00 USD | 522,020.00 USD | 2,260,000.00 USD | 2,550,000.00 USD |
| `7D` | `2218.00` | 54,630,000.00 USD | 0.00 USD | 54,630,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 70,350.00 USD |
| `1D` | `2219.00` | 20,540,000.00 USD | 0.00 USD | 20,540,000.00 USD | 6,820,000.00 USD | 2,420,000.00 USD | 3,260,000.00 USD |
| `7D` | `2220.80` | 31,670,000.00 USD | 0.00 USD | 31,670,000.00 USD | 0.00 USD | 6,120,000.00 USD | 10,510,000.00 USD |
| `1D` | `2221.40` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 0.00 USD | 4,950,000.00 USD | 2,590,000.00 USD |
| `7D` | `2223.60` | 15,040,000.00 USD | 0.00 USD | 15,040,000.00 USD | 0.00 USD | 6,100,000.00 USD | 8,940,000.00 USD |
| `1D` | `2223.80` | 494,970.00 USD | 0.00 USD | 494,970.00 USD | 168,380.00 USD | 300,160.00 USD | 26,430.00 USD |
| `7D` | `2225.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2225.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2226.20` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 2,980,000.00 USD | 3,480,000.00 USD | 147,770.00 USD |
| `7D` | `2226.40` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 324,830.00 USD | 0.00 USD | 5,100,000.00 USD |
| `1D` | `2228.60` | 25,150,000.00 USD | 25,150,000.00 USD | 0.00 USD | 0.00 USD | 13,040,000.00 USD | 5,500,000.00 USD |
| `7D` | `2229.20` | 26,580,000.00 USD | 26,580,000.00 USD | 0.00 USD | 2,140,000.00 USD | 0.00 USD | 19,010,000.00 USD |
| `1D` | `2231.00` | 65,930,000.00 USD | 65,930,000.00 USD | 0.00 USD | 40,420,000.00 USD | 0.00 USD | 361,580.00 USD |
| `7D` | `2232.00` | 30,520,000.00 USD | 30,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,940,000.00 USD |
| `1D` | `2233.40` | 66,090,000.00 USD | 66,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 162,790.00 USD |
| `7D` | `2234.80` | 45,160,000.00 USD | 45,160,000.00 USD | 0.00 USD | 0.00 USD | 14,300,000.00 USD | 350,840.00 USD |
| `7D` | `2237.60` | 64,230,000.00 USD | 64,230,000.00 USD | 0.00 USD | 11,730,000.00 USD | 7,340,000.00 USD | 0.00 USD |
| `1D` | `2238.20` | 78,050,000.00 USD | 78,050,000.00 USD | 0.00 USD | 11,960,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2240.40` | 99,700,000.00 USD | 99,700,000.00 USD | 0.00 USD | 35,470,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2240.60` | 81,310,000.00 USD | 81,310,000.00 USD | 0.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2243.00` | 82,200,000.00 USD | 82,200,000.00 USD | 0.00 USD | 271,140.00 USD | 569,860.00 USD | 50,930.00 USD |
| `7D` | `2243.20` | 102,880,000.00 USD | 102,880,000.00 USD | 0.00 USD | 2,910,000.00 USD | 268,650.00 USD | 0.00 USD |
| `1D` | `2245.40` | 87,190,000.00 USD | 87,190,000.00 USD | 0.00 USD | 1,040,000.00 USD | 2,910,000.00 USD | 1,040,000.00 USD |
| `7D` | `2246.00` | 114,880,000.00 USD | 114,880,000.00 USD | 0.00 USD | 2,290,000.00 USD | 1,300,000.00 USD | 8,410,000.00 USD |
| `1D` | `2247.80` | 105,680,000.00 USD | 105,680,000.00 USD | 0.00 USD | 7,200,000.00 USD | 5,800,000.00 USD | 5,480,000.00 USD |
| `7D` | `2248.80` | 130,720,000.00 USD | 130,720,000.00 USD | 0.00 USD | 7,600,000.00 USD | 6,990,000.00 USD | 1,250,000.00 USD |
| `1D` | `2250.20` | 111,900,000.00 USD | 111,900,000.00 USD | 0.00 USD | 5,800,000.00 USD | 365,980.00 USD | 55,780.00 USD |
| `7D` | `2251.60` | 152,900,000.00 USD | 152,900,000.00 USD | 0.00 USD | 10,510,000.00 USD | 11,670,000.00 USD | 0.00 USD |
| `1D` | `2252.60` | 115,910,000.00 USD | 115,910,000.00 USD | 0.00 USD | 850,700.00 USD | 1,770,000.00 USD | 1,390,000.00 USD |
| `7D` | `2254.40` | 160,790,000.00 USD | 160,790,000.00 USD | 0.00 USD | 885,200.00 USD | 6,600,000.00 USD | 406,400.00 USD |
| `1D` | `2255.00` | 140,850,000.00 USD | 140,850,000.00 USD | 0.00 USD | 12,360,000.00 USD | 6,830,000.00 USD | 5,750,000.00 USD |
| `7D` | `2257.20` | 206,090,000.00 USD | 206,090,000.00 USD | 0.00 USD | 29,680,000.00 USD | 8,620,000.00 USD | 7,000,000.00 USD |
| `1D` | `2257.40` | 174,380,000.00 USD | 174,380,000.00 USD | 0.00 USD | 19,840,000.00 USD | 7,960,000.00 USD | 5,730,000.00 USD |
| `1D` | `2259.80` | 194,020,000.00 USD | 194,020,000.00 USD | 0.00 USD | 9,190,000.00 USD | 9,590,000.00 USD | 859,300.00 USD |
| `7D` | `2260.00` | 213,800,000.00 USD | 213,800,000.00 USD | 0.00 USD | 0.00 USD | 3,670,000.00 USD | 4,040,000.00 USD |
| `1D` | `2262.20` | 220,620,000.00 USD | 220,620,000.00 USD | 0.00 USD | 11,700,000.00 USD | 6,910,000.00 USD | 7,990,000.00 USD |
| `7D` | `2262.80` | 222,260,000.00 USD | 222,260,000.00 USD | 0.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 280,820.00 USD |
| `1D` | `2264.60` | 246,340,000.00 USD | 246,340,000.00 USD | 0.00 USD | 6,910,000.00 USD | 11,430,000.00 USD | 7,370,000.00 USD |
| `7D` | `2265.60` | 224,990,000.00 USD | 224,990,000.00 USD | 0.00 USD | 0.00 USD | 2,510,000.00 USD | 218,310.00 USD |
| `1D` | `2267.00` | 276,860,000.00 USD | 276,860,000.00 USD | 0.00 USD | 9,850,000.00 USD | 9,000,000.00 USD | 11,680,000.00 USD |
| `7D` | `2268.40` | 256,930,000.00 USD | 256,930,000.00 USD | 0.00 USD | 11,010,000.00 USD | 5,790,000.00 USD | 15,150,000.00 USD |
| `1D` | `2269.40` | 321,340,000.00 USD | 321,340,000.00 USD | 0.00 USD | 21,800,000.00 USD | 9,800,000.00 USD | 12,870,000.00 USD |
| `7D` | `2271.20` | 291,670,000.00 USD | 291,670,000.00 USD | 0.00 USD | 17,870,000.00 USD | 3,500,000.00 USD | 13,370,000.00 USD |
| `1D` | `2271.80` | 346,060,000.00 USD | 346,060,000.00 USD | 0.00 USD | 7,280,000.00 USD | 6,790,000.00 USD | 10,660,000.00 USD |
| `7D` | `2274.00` | 317,000,000.00 USD | 317,000,000.00 USD | 0.00 USD | 15,420,000.00 USD | 7,040,000.00 USD | 2,870,000.00 USD |
| `1D` | `2274.20` | 367,800,000.00 USD | 367,800,000.00 USD | 0.00 USD | 11,490,000.00 USD | 6,900,000.00 USD | 3,350,000.00 USD |
| `1D` | `2276.60` | 429,040,000.00 USD | 429,040,000.00 USD | 0.00 USD | 29,880,000.00 USD | 19,450,000.00 USD | 11,910,000.00 USD |
| `7D` | `2276.80` | 326,100,000.00 USD | 326,100,000.00 USD | 0.00 USD | 9,100,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2279.00` | 458,010,000.00 USD | 458,010,000.00 USD | 0.00 USD | 11,040,000.00 USD | 5,320,000.00 USD | 12,610,000.00 USD |
| `7D` | `2279.60` | 373,620,000.00 USD | 373,620,000.00 USD | 0.00 USD | 3,230,000.00 USD | 30,300,000.00 USD | 13,990,000.00 USD |
| `1D` | `2281.40` | 515,600,000.00 USD | 515,600,000.00 USD | 0.00 USD | 31,660,000.00 USD | 25,130,000.00 USD | 800,750.00 USD |
| `7D` | `2282.40` | 453,880,000.00 USD | 453,880,000.00 USD | 0.00 USD | 0.00 USD | 66,580,000.00 USD | 13,670,000.00 USD |
| `1D` | `2283.80` | 562,150,000.00 USD | 562,150,000.00 USD | 0.00 USD | 22,270,000.00 USD | 11,570,000.00 USD | 12,710,000.00 USD |
| `7D` | `2285.20` | 487,570,000.00 USD | 487,570,000.00 USD | 0.00 USD | 6,610,000.00 USD | 26,950,000.00 USD | 140,410.00 USD |
| `1D` | `2286.20` | 587,700,000.00 USD | 587,700,000.00 USD | 0.00 USD | 4,520,000.00 USD | 13,210,000.00 USD | 7,820,000.00 USD |
| `7D` | `2288.00` | 514,330,000.00 USD | 514,330,000.00 USD | 0.00 USD | 8,380,000.00 USD | 6,500,000.00 USD | 11,870,000.00 USD |
| `1D` | `2288.60` | 610,630,000.00 USD | 610,630,000.00 USD | 0.00 USD | 12,720,000.00 USD | 7,200,000.00 USD | 3,020,000.00 USD |
| `7D` | `2290.80` | 527,520,000.00 USD | 527,520,000.00 USD | 0.00 USD | 4,310,000.00 USD | 3,340,000.00 USD | 5,550,000.00 USD |
| `1D` | `2291.00` | 650,700,000.00 USD | 650,700,000.00 USD | 0.00 USD | 20,070,000.00 USD | 11,790,000.00 USD | 8,210,000.00 USD |
| `1D` | `2293.40` | 677,980,000.00 USD | 677,980,000.00 USD | 0.00 USD | 13,490,000.00 USD | 5,110,000.00 USD | 8,680,000.00 USD |
| `7D` | `2293.60` | 544,870,000.00 USD | 544,870,000.00 USD | 0.00 USD | 8,930,000.00 USD | 0.00 USD | 8,410,000.00 USD |
| `1D` | `2295.80` | 709,020,000.00 USD | 709,020,000.00 USD | 0.00 USD | 9,310,000.00 USD | 13,540,000.00 USD | 8,200,000.00 USD |
| `7D` | `2296.40` | 600,540,000.00 USD | 600,540,000.00 USD | 0.00 USD | 28,890,000.00 USD | 9,570,000.00 USD | 17,210,000.00 USD |
| `1D` | `2298.20` | 761,590,000.00 USD | 761,590,000.00 USD | 0.00 USD | 32,280,000.00 USD | 13,940,000.00 USD | 6,340,000.00 USD |
| `7D` | `2299.20` | 634,390,000.00 USD | 634,390,000.00 USD | 0.00 USD | 18,930,000.00 USD | 14,430,000.00 USD | 487,160.00 USD |
| `1D` | `2300.60` | 794,670,000.00 USD | 794,670,000.00 USD | 0.00 USD | 8,900,000.00 USD | 10,170,000.00 USD | 14,010,000.00 USD |
| `7D` | `2302.00` | 689,860,000.00 USD | 689,860,000.00 USD | 0.00 USD | 16,020,000.00 USD | 17,380,000.00 USD | 22,080,000.00 USD |
| `1D` | `2303.00` | 825,600,000.00 USD | 825,600,000.00 USD | 0.00 USD | 17,940,000.00 USD | 5,770,000.00 USD | 7,220,000.00 USD |
| `7D` | `2304.80` | 714,260,000.00 USD | 714,260,000.00 USD | 0.00 USD | 10,940,000.00 USD | 4,600,000.00 USD | 8,860,000.00 USD |
| `1D` | `2305.40` | 860,460,000.00 USD | 860,460,000.00 USD | 0.00 USD | 12,190,000.00 USD | 15,330,000.00 USD | 7,340,000.00 USD |
| `7D` | `2307.60` | 729,180,000.00 USD | 729,180,000.00 USD | 0.00 USD | 7,580,000.00 USD | 5,150,000.00 USD | 2,200,000.00 USD |
| `1D` | `2307.80` | 869,720,000.00 USD | 869,720,000.00 USD | 0.00 USD | 4,390,000.00 USD | 2,880,000.00 USD | 1,980,000.00 USD |
| `1D` | `2310.20` | 889,080,000.00 USD | 889,080,000.00 USD | 0.00 USD | 5,980,000.00 USD | 2,740,000.00 USD | 10,650,000.00 USD |
| `7D` | `2310.40` | 748,720,000.00 USD | 748,720,000.00 USD | 0.00 USD | 11,460,000.00 USD | 2,720,000.00 USD | 5,350,000.00 USD |
| `1D` | `2312.60` | 903,410,000.00 USD | 903,410,000.00 USD | 0.00 USD | 5,450,000.00 USD | 7,690,000.00 USD | 1,190,000.00 USD |
| `7D` | `2313.20` | 766,470,000.00 USD | 766,470,000.00 USD | 0.00 USD | 1,200,000.00 USD | 3,490,000.00 USD | 13,060,000.00 USD |
| `1D` | `2315.00` | 922,820,000.00 USD | 922,820,000.00 USD | 0.00 USD | 5,440,000.00 USD | 12,280,000.00 USD | 1,680,000.00 USD |
| `7D` | `2316.00` | 773,000,000.00 USD | 773,000,000.00 USD | 0.00 USD | 0.00 USD | 5,780,000.00 USD | 749,540.00 USD |
| `1D` | `2317.40` | 948,840,000.00 USD | 948,840,000.00 USD | 0.00 USD | 7,540,000.00 USD | 10,540,000.00 USD | 7,940,000.00 USD |
| `7D` | `2318.80` | 792,990,000.00 USD | 792,990,000.00 USD | 0.00 USD | 6,560,000.00 USD | 5,250,000.00 USD | 8,180,000.00 USD |
| `1D` | `2319.80` | 972,460,000.00 USD | 972,460,000.00 USD | 0.00 USD | 9,790,000.00 USD | 10,770,000.00 USD | 3,060,000.00 USD |
| `7D` | `2321.60` | 810,210,000.00 USD | 810,210,000.00 USD | 0.00 USD | 1,190,000.00 USD | 15,930,000.00 USD | 108,040.00 USD |
| `1D` | `2322.20` | 991,140,000.00 USD | 991,140,000.00 USD | 0.00 USD | 3,420,000.00 USD | 10,510,000.00 USD | 4,750,000.00 USD |
| `7D` | `2324.40` | 818,570,000.00 USD | 818,570,000.00 USD | 0.00 USD | 4,670,000.00 USD | 1,970,000.00 USD | 1,720,000.00 USD |
| `1D` | `2324.60` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 2,540,000.00 USD | 9,500,000.00 USD | 519,140.00 USD |
| `1D` | `2327.00` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 949,090.00 USD | 945,500.00 USD | 5,840,000.00 USD |
| `7D` | `2327.20` | 834,490,000.00 USD | 834,490,000.00 USD | 0.00 USD | 6,590,000.00 USD | 805,740.00 USD | 8,520,000.00 USD |
| `1D` | `2329.40` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 9,320,000.00 USD | 2,530,000.00 USD | 1,410,000.00 USD |
| `7D` | `2330.00` | 855,990,000.00 USD | 855,990,000.00 USD | 0.00 USD | 13,230,000.00 USD | 363,770.00 USD | 7,910,000.00 USD |
| `1D` | `2331.80` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 3,190,000.00 USD | 2,970,000.00 USD | 1,940,000.00 USD |
| `7D` | `2332.80` | 883,900,000.00 USD | 883,900,000.00 USD | 0.00 USD | 19,860,000.00 USD | 8,000,000.00 USD | 54,580.00 USD |
| `1D` | `2334.20` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 7,690,000.00 USD | 4,790,000.00 USD | 8,640,000.00 USD |
| `7D` | `2335.60` | 940,830,000.00 USD | 940,830,000.00 USD | 0.00 USD | 31,150,000.00 USD | 12,430,000.00 USD | 13,350,000.00 USD |
| `1D` | `2336.60` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 13,510,000.00 USD | 1,880,000.00 USD | 4,420,000.00 USD |
| `7D` | `2338.40` | 966,510,000.00 USD | 966,510,000.00 USD | 0.00 USD | 14,040,000.00 USD | 0.00 USD | 11,650,000.00 USD |
| `1D` | `2339.00` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 7,770,000.00 USD | 3,990,000.00 USD | 5,770,000.00 USD |
| `7D` | `2341.20` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 4,720,000.00 USD | 17,820,000.00 USD | 14,630,000.00 USD |
| `1D` | `2341.40` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 7,800,000.00 USD | 4,080,000.00 USD | 11,030,000.00 USD |
| `1D` | `2343.80` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 7,550,000.00 USD | 8,510,000.00 USD | 6,680,000.00 USD |
| `7D` | `2344.00` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 6,380,000.00 USD | 4,940,000.00 USD | 5,980,000.00 USD |
| `1D` | `2346.20` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 3,850,000.00 USD | 2,750,000.00 USD | 3,900,000.00 USD |
| `7D` | `2346.80` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 19,690,000.00 USD | 19,370,000.00 USD |
| `1D` | `2348.60` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 7,490,000.00 USD | 6,650,000.00 USD | 2,760,000.00 USD |
| `7D` | `2349.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 1,320,000.00 USD | 15,110,000.00 USD | 16,240,000.00 USD |
| `1D` | `2351.00` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 24,320,000.00 USD | 4,950,000.00 USD | 11,170,000.00 USD |
| `7D` | `2352.40` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 2,710,000.00 USD | 22,900,000.00 USD | 5,540,000.00 USD |
| `1D` | `2353.40` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 3,010,000.00 USD | 2,970,000.00 USD | 652,430.00 USD |
| `7D` | `2355.20` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 18,340,000.00 USD | 27,760,000.00 USD | 2,760,000.00 USD |
| `1D` | `2355.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 4,450,000.00 USD | 2,950,000.00 USD | 1,850,000.00 USD |
| `7D` | `2358.00` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 5,360,000.00 USD | 1,840,000.00 USD | 4,510,000.00 USD |
| `1D` | `2358.20` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 3,900,000.00 USD | 4,470,000.00 USD | 6,080,000.00 USD |
| `1D` | `2360.60` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 9,930,000.00 USD | 3,880,000.00 USD | 1,900,000.00 USD |
| `7D` | `2360.80` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 4,470,000.00 USD | 3,430,000.00 USD | 254,850.00 USD |
| `1D` | `2363.00` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 5,390,000.00 USD | 9,200,000.00 USD | 7,890,000.00 USD |
| `7D` | `2363.60` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 4,570,000.00 USD | 373,740.00 USD | 6,830,000.00 USD |
| `1D` | `2365.40` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 4,890,000.00 USD | 658,050.00 USD | 3,680,000.00 USD |
| `7D` | `2366.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 4,210,000.00 USD |
| `1D` | `2367.80` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 0.00 USD | 3,010,000.00 USD | 2,080,000.00 USD | 1,910,000.00 USD |
| `7D` | `2369.20` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 21,280,000.00 USD | 475,460.00 USD | 13,880,000.00 USD |
| `1D` | `2370.20` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 10,560,000.00 USD | 7,300,000.00 USD | 5,290,000.00 USD |
| `7D` | `2372.00` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 15,540,000.00 USD | 0.00 USD | 41,520,000.00 USD |
| `1D` | `2372.60` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 13,770,000.00 USD | 2,610,000.00 USD | 5,690,000.00 USD |
| `7D` | `2374.80` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD |
| `1D` | `2375.00` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 8,510,000.00 USD | 557,400.00 USD | 1,840,000.00 USD |
| `1D` | `2377.40` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 3,730,000.00 USD | 3,470,000.00 USD | 4,820,000.00 USD |
| `7D` | `2377.60` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 8,770,000.00 USD | 6,190,000.00 USD | 15,370,000.00 USD |
| `1D` | `2379.80` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 6,370,000.00 USD | 389,290.00 USD | 2,050,000.00 USD |
| `7D` | `2380.40` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 6,830,000.00 USD | 2,590,000.00 USD | 22,140,000.00 USD |
| `1D` | `2382.20` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 8,260,000.00 USD | 8,360,000.00 USD | 11,930,000.00 USD |
| `7D` | `2383.20` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 8,610,000.00 USD | 15,780,000.00 USD | 24,790,000.00 USD |
| `1D` | `2384.60` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 11,820,000.00 USD | 12,030,000.00 USD | 5,140,000.00 USD |
| `7D` | `2386.00` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 0.00 USD | 15,430,000.00 USD | 37,810,000.00 USD | 43,230,000.00 USD |
| `1D` | `2387.00` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 7,590,000.00 USD | 7,070,000.00 USD | 4,800,000.00 USD |
| `7D` | `2388.80` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 5,490,000.00 USD | 26,450,000.00 USD | 31,790,000.00 USD |
| `1D` | `2389.40` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 0.00 USD | 9,610,000.00 USD | 6,800,000.00 USD | 1,800,000.00 USD |
| `7D` | `2391.60` | 1,700,000,000.00 USD | 1,700,000,000.00 USD | 0.00 USD | 7,580,000.00 USD | 49,400,000.00 USD | 36,080,000.00 USD |
| `1D` | `2391.80` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 451,370.00 USD | 3,710,000.00 USD | 3,320,000.00 USD |
| `1D` | `2394.20` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 0.00 USD | 4,450,000.00 USD | 2,780,000.00 USD | 1,120,000.00 USD |
| `7D` | `2394.40` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 0.00 USD | 57,060,000.00 USD | 26,270,000.00 USD | 35,940,000.00 USD |
| `1D` | `2396.60` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 0.00 USD | 64,150.00 USD | 1,150,000.00 USD | 2,880,000.00 USD |
| `7D` | `2397.20` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 0.00 USD | 25,000,000.00 USD | 39,300,000.00 USD | 21,770,000.00 USD |
| `1D` | `2399.00` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 0.00 USD | 2,150,000.00 USD | 3,200,000.00 USD | 1,570,000.00 USD |
| `7D` | `2400.00` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 0.00 USD | 48,240,000.00 USD | 26,850,000.00 USD | 22,380,000.00 USD |
| `1D` | `2401.40` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 0.00 USD | 642,440.00 USD | 62,980.00 USD | 1,390,000.00 USD |
| `7D` | `2402.80` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 0.00 USD | 53,160,000.00 USD | 21,040,000.00 USD | 27,270,000.00 USD |
| `1D` | `2403.80` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 0.00 USD | 3,400,000.00 USD | 3,030,000.00 USD | 1,930,000.00 USD |
| `7D` | `2405.60` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 0.00 USD | 26,730,000.00 USD | 29,760,000.00 USD | 16,500,000.00 USD |
| `1D` | `2406.20` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 0.00 USD | 9,420,000.00 USD | 3,430,000.00 USD | 4,810,000.00 USD |
| `7D` | `2408.40` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 27,050,000.00 USD | 26,540,000.00 USD | 26,780,000.00 USD |
| `1D` | `2408.60` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 0.00 USD | 2,450,000.00 USD | 1,330,000.00 USD | 673,910.00 USD |
| `1D` | `2411.00` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 3,410,000.00 USD | 4,350,000.00 USD | 4,020,000.00 USD |
| `7D` | `2411.20` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 17,990,000.00 USD | 19,900,000.00 USD | 20,380,000.00 USD |
| `1D` | `2413.40` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 0.00 USD | 5,430,000.00 USD | 2,470,000.00 USD | 1,290,000.00 USD |
| `7D` | `2414.00` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 0.00 USD | 19,190,000.00 USD | 22,460,000.00 USD | 20,110,000.00 USD |
| `1D` | `2415.80` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 2,710,000.00 USD | 2,310,000.00 USD | 3,200,000.00 USD |
| `7D` | `2416.80` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 0.00 USD | 23,820,000.00 USD | 6,390,000.00 USD | 21,560,000.00 USD |
| `1D` | `2418.20` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 3,310,000.00 USD | 2,000,000.00 USD | 1,140,000.00 USD |
| `7D` | `2419.60` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 0.00 USD | 27,160,000.00 USD | 17,310,000.00 USD | 10,160,000.00 USD |
| `1D` | `2420.60` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 5,840,000.00 USD | 4,110,000.00 USD | 4,100,000.00 USD |
| `7D` | `2422.40` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 0.00 USD | 21,450,000.00 USD | 20,430,000.00 USD | 13,750,000.00 USD |
| `1D` | `2423.00` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 770,750.00 USD | 1,540,000.00 USD | 2,890,000.00 USD |
| `7D` | `2425.20` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 0.00 USD | 11,030,000.00 USD | 13,240,000.00 USD | 22,920,000.00 USD |
| `1D` | `2425.40` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 1,280,000.00 USD | 623,850.00 USD | 621,440.00 USD |
| `1D` | `2427.80` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 1,490,000.00 USD | 1,520,000.00 USD | 609,950.00 USD |
| `7D` | `2428.00` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 19,050,000.00 USD | 10,460,000.00 USD | 12,860,000.00 USD |
| `1D` | `2430.20` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,550,000.00 USD | 1,350,000.00 USD |
| `7D` | `2430.80` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 7,240,000.00 USD | 12,690,000.00 USD | 8,390,000.00 USD |
| `1D` | `2432.60` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 2,770,000.00 USD | 2,230,000.00 USD | 682,860.00 USD |
| `7D` | `2433.60` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 14,430,000.00 USD | 5,270,000.00 USD | 3,140,000.00 USD |
| `1D` | `2435.00` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 2,480,000.00 USD | 545,610.00 USD | 1,370,000.00 USD |
| `7D` | `2436.40` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 6,380,000.00 USD | 5,300,000.00 USD | 5,010,000.00 USD |
| `1D` | `2437.40` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 967,690.00 USD | 1,050,000.00 USD | 30,250.00 USD |
| `7D` | `2439.20` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 0.00 USD | 13,780,000.00 USD | 7,040,000.00 USD | 5,790,000.00 USD |
| `1D` | `2439.80` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 1,640,000.00 USD | 502,040.00 USD | 304,820.00 USD |
| `7D` | `2442.00` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 5,970,000.00 USD | 4,860,000.00 USD | 7,930,000.00 USD |
| `1D` | `2442.20` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 1,040,000.00 USD | 743,640.00 USD | 565,910.00 USD |
| `1D` | `2444.60` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 13,780.00 USD | 486,350.00 USD | 1,490,000.00 USD |
| `7D` | `2444.80` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 9,830,000.00 USD | 8,980,000.00 USD | 8,630,000.00 USD |
| `1D` | `2447.00` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 848,560.00 USD | 1,170,000.00 USD |
| `7D` | `2447.60` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 8,340,000.00 USD | 3,080,000.00 USD | 12,830,000.00 USD |
| `1D` | `2449.40` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 321,220.00 USD | 257,760.00 USD | 26,770.00 USD |
| `7D` | `2450.40` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 8,460,000.00 USD | 6,640,000.00 USD | 9,800,000.00 USD |
| `1D` | `2451.80` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 2,860,000.00 USD | 1,690,000.00 USD | 2,210,000.00 USD |
| `7D` | `2453.20` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 7,290,000.00 USD | 3,760,000.00 USD | 3,580,000.00 USD |
| `1D` | `2454.20` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 2,640,000.00 USD | 2,210,000.00 USD | 1,060,000.00 USD |
| `7D` | `2456.00` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 5,780,000.00 USD | 5,730,000.00 USD | 6,710,000.00 USD |
| `1D` | `2456.60` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 1,080,000.00 USD | 1,900,000.00 USD | 841,740.00 USD |
| `7D` | `2458.80` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 4,440,000.00 USD | 5,910,000.00 USD | 6,680,000.00 USD |
| `1D` | `2459.00` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 1,710,000.00 USD | 1,290,000.00 USD | 16,930.00 USD |
| `1D` | `2461.40` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 540,100.00 USD | 350,490.00 USD | 379,080.00 USD |
| `7D` | `2461.60` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 6,280,000.00 USD | 6,710,000.00 USD | 6,480,000.00 USD |
| `1D` | `2463.80` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 358,460.00 USD | 940,830.00 USD | 1,020,000.00 USD |
| `7D` | `2464.40` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 4,990,000.00 USD | 2,040,000.00 USD | 2,590,000.00 USD |
| `1D` | `2466.20` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 510,000.00 USD | 885,870.00 USD | 550,280.00 USD |
| `7D` | `2467.20` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 3,670,000.00 USD | 3,120,000.00 USD | 608,610.00 USD |
| `1D` | `2468.60` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 0.00 USD | 288,920.00 USD | 1,810,000.00 USD | 555,890.00 USD |
| `7D` | `2470.00` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 3,190,000.00 USD | 2,290,000.00 USD | 408,300.00 USD |
| `1D` | `2471.00` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 0.00 USD | 1,380,000.00 USD | 284,850.00 USD | 1,080,000.00 USD |
| `7D` | `2472.80` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 4,410,000.00 USD | 2,420,000.00 USD | 2,870,000.00 USD |
| `7D` | `2475.60` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 0.00 USD | 4,390,000.00 USD | 1,420,000.00 USD | 1,290,000.00 USD |
| `7D` | `2478.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 3,140,000.00 USD | 4,910,000.00 USD | 540,990.00 USD |
| `7D` | `2481.20` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 729,480.00 USD | 3,680,000.00 USD | 1,050,000.00 USD |
| `7D` | `2484.00` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD |
| `7D` | `2486.80` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 30,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2489.60` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 630,050.00 USD | 225,530.00 USD | 52,670.00 USD |
| `7D` | `2492.40` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 1,020,000.00 USD | 1,550,000.00 USD |
| `7D` | `2495.20` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 0.00 USD | 773,650.00 USD | 736,470.00 USD | 2,760,000.00 USD |
| `7D` | `2498.00` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 0.00 USD | 602,570.00 USD | 1,660,000.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `28.37B` | Total OI Tokens: `12,772,992.1 ETH`
  * 1h OI Change: `-0.51%` | 4h OI Change: `-2.59%` | 24h OI Change: `-6.02%`
  * Exchange Breakdown: Binance=`8.38B` | Bybit=`2.09B` | OKX=`1.75B` | Hyperliquid=`2.34B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-142.98K` | Last 24h: `195.10K` | Last 3d: `5.21M` | Last 7d: `11.81M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0030%` | **USDT OKX** | `-0.0039%` |
| **USDT Bybit** | `-0.0009%` | **USDT KuCoin** | `-0.0049%` |
| **USDT MEXC** | `-0.0030%` | **USDT BingX** | `0.0007%` |
| **USDT Gate** | `0.0079%` | **USDT Bitget** | `0.0008%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0016%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `68.42%` | `31.58%` | `2.17` | 433,200,000.00 USD |
| `15M` | `Binance` | `55.93%` | `44.07%` | `1.27` | 84,880,000.00 USD |
| `15M` | `OKX` | `48.97%` | `51.03%` | `0.96` | 38,860,000.00 USD |
| `15M` | `Bybit` | `50.69%` | `49.31%` | `1.03` | 16,200,000.00 USD |
| `15M` | `KuCoin` | `49.95%` | `50.05%` | `1.00` | 910,820.00 USD |
| `15M` | `Gate` | `48.98%` | `51.02%` | `0.96` | 42,160,000.00 USD |
| `15M` | `Bitget` | `56.05%` | `43.95%` | `1.28` | 7,910,000.00 USD |
| `15M` | `BingX` | `45.32%` | `54.68%` | `0.83` | 2,420,000.00 USD |
| `15M` | `MEXC` | `55.98%` | `44.02%` | `1.27` | 8,110,000.00 USD |
| `15M` | `Bitunix` | `48.33%` | `51.67%` | `0.94` | 7,960,000.00 USD |
| `15M` | `Hyperliquid` | `46.39%` | `53.61%` | `0.87` | 9,780,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.53%` | `53.47%` | `0.87` | 1,930,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `87.51%` | `12.49%` | `7.01` | 202,620,000.00 USD |
| `15M` | `HTX` | `43.16%` | `56.84%` | `0.76` | 3,500,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `43.11%` | `56.89%` | `0.76` | 1,950,000.00 USD |
| `15M` | `Bitfinex` | `51.94%` | `48.06%` | `1.08` | 27,090.00 USD |
| `15M` | `Kraken` | `21.89%` | `78.11%` | `0.28` | 1,190,000.00 USD |
| `15M` | `Aster` | `47.23%` | `52.77%` | `0.90` | 1,040,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.82%` | `55.18%` | `0.81` | 1,770,000.00 USD |
| `15M` | `Whale Positions` | `55.93%` | `44.07%` | `1.27` | 84,880,000.00 USD |
| `15M` | `Global Accounts` | `68.42%` | `31.58%` | `2.17` | 433,200,000.00 USD |
| `1H` | `ETH` | `53.64%` | `46.36%` | `1.16` | 1,350,000,000.00 USD |
| `1H` | `Binance` | `46.92%` | `53.08%` | `0.88` | 373,480,000.00 USD |
| `1H` | `OKX` | `44.7%` | `55.3%` | `0.81` | 226,140,000.00 USD |
| `1H` | `Bybit` | `50.3%` | `49.7%` | `1.01` | 70,650,000.00 USD |
| `1H` | `KuCoin` | `46.98%` | `53.02%` | `0.89` | 4,930,000.00 USD |
| `1H` | `Gate` | `48.85%` | `51.15%` | `0.96` | 187,940,000.00 USD |
| `1H` | `Bitget` | `50.83%` | `49.17%` | `1.03` | 42,220,000.00 USD |
| `1H` | `BingX` | `57.84%` | `42.16%` | `1.37` | 14,230,000.00 USD |
| `1H` | `MEXC` | `45.13%` | `54.87%` | `0.82` | 34,860,000.00 USD |
| `1H` | `Bitunix` | `44.53%` | `55.47%` | `0.80` | 39,730,000.00 USD |
| `1H` | `Hyperliquid` | `63.07%` | `36.93%` | `1.71` | 82,560,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.76%` | `51.24%` | `0.95` | 4,060,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `86.86%` | `13.14%` | `6.61` | 205,540,000.00 USD |
| `1H` | `HTX` | `18.61%` | `81.39%` | `0.23` | 25,510,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `48.85%` | `51.15%` | `0.96` | 12,410,000.00 USD |
| `1H` | `Bitfinex` | `57.01%` | `42.99%` | `1.33` | 828,930.00 USD |
| `1H` | `Kraken` | `40%` | `60%` | `0.67` | 4,610,000.00 USD |
| `1H` | `Aster` | `37.31%` | `62.69%` | `0.60` | 8,090,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `51.52%` | `48.48%` | `1.06` | 11,940,000.00 USD |
| `1H` | `Whale Positions` | `46.92%` | `53.08%` | `0.88` | 373,480,000.00 USD |
| `1H` | `Global Accounts` | `53.64%` | `46.36%` | `1.16` | 1,350,000,000.00 USD |
| `4H` | `ETH` | `49.66%` | `50.34%` | `0.99` | 6,340,000,000.00 USD |
| `4H` | `Binance` | `49.45%` | `50.55%` | `0.98` | 2,080,000,000.00 USD |
| `4H` | `OKX` | `48.17%` | `51.83%` | `0.93` | 1,130,000,000.00 USD |
| `4H` | `Bybit` | `44.85%` | `55.15%` | `0.81` | 377,050,000.00 USD |
| `4H` | `KuCoin` | `46.9%` | `53.1%` | `0.88` | 19,920,000.00 USD |
| `4H` | `Gate` | `50.1%` | `49.9%` | `1.00` | 934,400,000.00 USD |
| `4H` | `Bitget` | `47.56%` | `52.44%` | `0.91` | 223,020,000.00 USD |
| `4H` | `BingX` | `46.42%` | `53.58%` | `0.87` | 66,610,000.00 USD |
| `4H` | `MEXC` | `52.37%` | `47.63%` | `1.10` | 248,960,000.00 USD |
| `4H` | `Bitunix` | `49.85%` | `50.15%` | `0.99` | 206,500,000.00 USD |
| `4H` | `Hyperliquid` | `40.89%` | `59.11%` | `0.69` | 260,690,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.44%` | `49.56%` | `1.02` | 36,520,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `63.42%` | `36.58%` | `1.73` | 482,680,000.00 USD |
| `4H` | `HTX` | `45.1%` | `54.9%` | `0.82` | 82,400,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `43.16%` | `56.84%` | `0.76` | 66,720,000.00 USD |
| `4H` | `Bitfinex` | `34.28%` | `65.72%` | `0.52` | 2,010,000.00 USD |
| `4H` | `Kraken` | `45.65%` | `54.35%` | `0.84` | 9,140,000.00 USD |
| `4H` | `Aster` | `48.5%` | `51.5%` | `0.94` | 51,630,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.96%` | `49.04%` | `1.04` | 74,960,000.00 USD |
| `4H` | `Whale Positions` | `49.45%` | `50.55%` | `0.98` | 2,080,000,000.00 USD |
| `4H` | `Global Accounts` | `49.66%` | `50.34%` | `0.99` | 6,340,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2244.75` | `2247.34` | `2244.75` | `2250.75` | `2244.25` | 75,332,127.88 USD | 44,642,781.21 USD | 30,689,346.67 USD | 13,953,434.54 USD | `+18.52%` | `1B / 0S` |
| `0:00 UTC` | `2230.25` | `2237.42` | `2230.25` | `2248.75` | `2228.25` | 239,005,598.88 USD | 101,154,920.14 USD | 137,850,678.73 USD | -36,695,758.59 USD | `-15.35%` | `0B / 8S` |
| `5:00 UTC` | `2232.75` | `2233.33` | `2232.75` | `2238.25` | `2228.25` | 153,884,513.89 USD | 97,714,432.25 USD | 56,170,081.64 USD | 41,544,350.61 USD | `+27.00%` | `5B / 1S` |
| `0:00 UTC` | `2227.75` | `2228.98` | `2227.75` | `2236.75` | `2223.25` | 107,078,982.08 USD | 47,873,893.40 USD | 59,205,088.68 USD | -11,331,195.28 USD | `-10.58%` | `0B / 1S` |
| `5:00 UTC` | `2233.25` | `2230.29` | `2233.25` | `2234.75` | `2224.25` | 95,342,735.21 USD | 45,163,958.47 USD | 50,178,776.75 USD | -5,014,818.28 USD | `-5.26%` | `0B / 3S` |
| `0:00 UTC` | `2224.25` | `2226.52` | `2224.25` | `2230.75` | `2223.25` | 103,679,050.63 USD | 41,811,152.44 USD | 61,867,898.19 USD | -20,056,745.75 USD | `-19.35%` | `0B / 2S` |
| `5:00 UTC` | `2223.75` | `2226.83` | `2223.75` | `2231.75` | `2223.25` | 59,922,094.97 USD | 29,249,984.51 USD | 30,672,110.46 USD | -1,422,125.96 USD | `-2.37%` | `1B / 1S` |
| `0:00 UTC` | `2222.75` | `2224.81` | `2222.75` | `2229.75` | `2221.25` | 65,855,959.19 USD | 30,261,207.11 USD | 35,594,752.09 USD | -5,333,544.98 USD | `-8.10%` | `0B / 4S` |
| `5:00 UTC` | `2221.75` | `2223.05` | `2221.75` | `2226.25` | `2220.25` | 71,858,619.15 USD | 38,686,757.89 USD | 33,171,861.26 USD | 5,514,896.63 USD | `+7.67%` | `0B / 0S` |
| `0:00 UTC` | `2225.25` | `2223.77` | `2225.25` | `2226.25` | `2220.25` | 33,967,611.58 USD | 16,340,040.50 USD | 17,627,571.08 USD | -1,287,530.58 USD | `-3.79%` | `0B / 1S` |

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
| `5m` | 371,690.00 USD | 7,650,000.00 USD | **`ACCUMULATION`** |
| `15m` | -3,380,000.00 USD | -5,610,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -10,550,000.00 USD | -31,890,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -28,720,000.00 USD | -42,930,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -25,470,000.00 USD | -111,790,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -11,340,000.00 USD | -111,190,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -5,480,000.00 USD | -42,980,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -7,570,000.00 USD | -649,910,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -75,740,000.00 USD | -712,740,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -152,960,000.00 USD | -1,990,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -221,150,000.00 USD | -3,100,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,180,000,000.00 USD | -9,810,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+371.69K` | 15m=`-3.38M` | 1h=`-28.72M` | 24h=`-152.96M`
* Futures Capital Netflows: 5m=`+7.65M` | 15m=`-5.61M` | 1h=`-42.93M` | 24h=`-1.99B`
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
  * `2026-10-30 14:41:27 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:27 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:27 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:27 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:09:27 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:05:27 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:05:27 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:05:27 IST`: [destatis.de] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2194.00` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2175.23` (Risk Distance: `18.77` pts)
  * +2.5R Take Profit: `2240.93`
  * Mathematical Lot Sizing: **`0.53 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2252.28` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2271.05` (Risk Distance: `18.77` pts)
  * +2.5R Take Profit: `2205.35`
  * Mathematical Lot Sizing: **`0.53 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2239.17`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
