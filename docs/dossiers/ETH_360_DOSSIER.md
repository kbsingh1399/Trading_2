# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 16:21:39 IST` (`2026-10-30 10:51:39 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2240.40` | **Live Ask Quote**: `2243.30` | **Mid Price**: `2241.85`
- **Spread Points**: `290.00` | **Spread BPS**: `12.94 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2219.98` | VWAP Z-Score: `+0.30` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `11.19` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `45.82` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2267.99` | Lower -3.00σ Band: `2171.96`
  * Upper +2.51σ Band: `2260.15` | Lower -2.51σ Band: `2179.80`
  * Upper +2.01σ Band: `2252.15` | Lower -2.01σ Band: `2187.81`
  * Upper +2.00σ Band: `2251.99` | Lower -2.00σ Band: `2187.97`
  * Upper +1.28σ Band: `2240.46` | Lower -1.28σ Band: `2199.49`
  * Upper +1.00σ Band: `2235.98` | Lower -1.00σ Band: `2203.97`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2224.56` | EMA-20=`2227.67` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2240.49` (Slope: `+0.0000`) | EMA-100=`2263.80`
  * Institutional Anchors: EMA-144=`2277.79` | EMA-200=`2290.81` (Slope: `-0.3716`) | EMA-233=`2295.89`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2251.47` (Distance: `-0.42%`)
  * Point of Control (POC) = `2221.52` (Distance: `+0.92%`)
  * Value Area Low (VAL) = `2196.43` (Distance: `+2.07%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2356.25` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2251.30` | Low=`2215.10`
  * New York Session (13:00-21:00 UTC): High=`2243.30` | Low=`2216.10`
  * Initial Balance (First Hour): IB High=`2246.50` | IB Low=`2230.60`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2232.88` - `2250.82`
  * Optimal Trade Entry (OTE 0.705): `2246.33`
  * Structural Invalidation Anchor (0.786): `2259.78`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2228.48` | `2243.54` | `2228.26` | `2238.30` | `39,932` | 89,344,493.85 USD | 16,887,442.70 USD | `+18.90%` | -939,172,411.99 USD | `+2.98` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `2238.31` | `2245.83` | `2237.68` | `2244.71` | `21,927` | 49,141,896.63 USD | 8,943,118.13 USD | `+18.20%` | -930,229,293.86 USD | `+1.35` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `2244.71` | `2247.55` | `2243.55` | `2244.95` | `15,618` | 35,073,876.04 USD | 8,145,983.41 USD | `+23.23%` | -922,083,310.44 USD | `+1.09` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `2228.43` | `2228.43` | `2221.66` | `2224.27` | `25,370` | 56,423,190.50 USD | -1,089,080.98 USD | `-1.93%` | -960,816,426.84 USD | `-0.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `2224.26` | `2230.72` | `2220.36` | `2228.47` | `27,286` | 60,731,653.97 USD | 4,756,572.15 USD | `+7.83%` | -956,059,854.69 USD | `+0.31` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `2228.48` | `2247.55` | `2228.26` | `2244.95` | `77,477` | 173,560,266.52 USD | 33,976,544.24 USD | `+19.58%` | -922,083,310.44 USD | `+1.85` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `2235.54` | `2236.80` | `2223.18` | `2227.93` | `164,265` | 366,023,334.59 USD | -37,825,356.97 USD | `-10.33%` | -969,069,546.97 USD | `+0.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2227.92` | `2231.18` | `2220.24` | `2228.42` | `122,419` | 272,434,813.90 USD | 5,581,746.93 USD | `+2.05%` | -963,487,800.04 USD | `+0.46` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `2228.43` | `2247.55` | `2220.36` | `2244.61` | `130,014` | 290,448,584.50 USD | 37,564,895.98 USD | `+12.93%` | -925,922,904.06 USD | `+0.73` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2247.55` | `2220.24` | `2245.01` | `416,974` | 929,525,854.50 USD | 5,569,697.98 USD | `+0.60%` | -882,296,370.47 USD | `+0.68` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -98,115,944.70 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -652,353,514.01 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2247.55` | `2220.24` | `2245.01` | `416,974` | 929,525,854.50 USD | 5,569,697.98 USD | `+0.60%` | -882,296,370.47 USD | `+0.68` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`2241.85`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2242.90` | `104.0192` | 233,304.66 USD | 13,407,288.59 USD | `5 orders` | `-0.09%` | `-` |
| `BID` | `2243.00` | `224.8527` | 504,344.61 USD | 13,173,983.93 USD | `5 orders` | `-0.08%` | `-` |
| `BID` | `2243.10` | `159.3215` | 357,374.06 USD | 12,669,639.32 USD | `8 orders` | `-0.08%` | `-` |
| `BID` | `2243.20` | `255.3465` | 572,793.27 USD | 12,312,265.26 USD | `7 orders` | `-0.07%` | `-` |
| `BID` | `2243.30` | `161.0514` | 361,286.61 USD | 11,739,472.00 USD | `9 orders` | `-0.07%` | `-` |
| `BID` | `2243.40` | `400.7380` | 899,015.63 USD | 11,378,185.39 USD | `11 orders` | `-0.06%` | `-` |
| `BID` | `2243.50` | `133.4104` | 299,306.23 USD | 10,479,169.76 USD | `11 orders` | `-0.06%` | `-` |
| `BID` | `2243.60` | `464.5465` | 1,042,256.53 USD | 10,179,863.53 USD | `6 orders` | `-0.06%` | `-` |
| `BID` | `2243.70` | `363.3277` | 815,198.36 USD | 9,137,607.00 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `2243.80` | `340.4615` | 763,927.51 USD | 8,322,408.64 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `2243.90` | `418.8859` | 939,938.07 USD | 7,558,481.13 USD | `9 orders` | `-0.04%` | `-` |
| `BID` | `2244.00` | `266.5863` | 598,219.66 USD | 6,618,543.06 USD | `8 orders` | `-0.04%` | `-` |
| `BID` | `2244.10` | `580.5702` | 1,302,857.59 USD | 6,020,323.40 USD | `10 orders` | `-0.03%` | `-` |
| `BID` | `2244.20` | `335.2674` | 752,407.10 USD | 4,717,465.81 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `2244.30` | `26.0481` | 58,459.75 USD | 3,965,058.71 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `2244.40` | `251.9242` | 565,418.67 USD | 3,906,598.96 USD | `6 orders` | `-0.02%` | `-` |
| `BID` | `2244.50` | `44.1988` | 99,204.21 USD | 3,341,180.29 USD | `8 orders` | `-0.02%` | `-` |
| `BID` | `2244.60` | `365.6269` | 820,686.14 USD | 3,241,976.08 USD | `10 orders` | `-0.01%` | `-` |
| `BID` | `2244.70` | `691.8950` | 1,553,096.71 USD | 2,421,289.94 USD | `11 orders` | `-0.01%` | `-` |
| `BID` | `2244.80` | `386.7575` | 868,193.24 USD | 868,193.24 USD | `35 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2244.85` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,244.85` | `0.00%` | `-` |
| `ASK` | `2244.90` | `7.9634` | 17,877.04 USD | 17,877.04 USD | `4 orders` | `+0.00%` | `-` |
| `ASK` | `2245.00` | `1.6724` | 3,754.54 USD | 21,631.57 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `2245.30` | `15.3802` | 34,533.16 USD | 56,164.74 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `2245.40` | `5.4027` | 12,131.22 USD | 68,295.96 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `2245.50` | `81.6329` | 183,306.68 USD | 251,602.64 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `2245.60` | `29.7589` | 66,826.59 USD | 318,429.22 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `2245.70` | `173.2653` | 389,101.88 USD | 707,531.11 USD | `9 orders` | `+0.04%` | `-` |
| `ASK` | `2245.80` | `349.6374` | 785,215.67 USD | 1,492,746.78 USD | `12 orders` | `+0.04%` | `-` |
| `ASK` | `2245.90` | `324.1678` | 728,048.46 USD | 2,220,795.24 USD | `13 orders` | `+0.05%` | `-` |
| `ASK` | `2246.00` | `87.8467` | 197,303.69 USD | 2,418,098.93 USD | `10 orders` | `+0.05%` | `-` |
| `ASK` | `2246.10` | `212.0080` | 476,191.17 USD | 2,894,290.10 USD | `11 orders` | `+0.06%` | `-` |
| `ASK` | `2246.20` | `523.6221` | 1,176,159.96 USD | 4,070,450.06 USD | `15 orders` | `+0.06%` | `-` |
| `ASK` | `2246.30` | `423.4026` | 951,089.26 USD | 5,021,539.32 USD | `8 orders` | `+0.06%` | `-` |
| `ASK` | `2246.40` | `650.1477` | 1,460,491.79 USD | 6,482,031.11 USD | `13 orders` | `+0.07%` | `-` |
| `ASK` | `2246.50` | `221.9056` | 498,510.93 USD | 6,980,542.04 USD | `16 orders` | `+0.07%` | `-` |
| `ASK` | `2246.60` | `233.3486` | 524,240.96 USD | 7,504,783.01 USD | `15 orders` | `+0.08%` | `-` |
| `ASK` | `2246.70` | `198.8991` | 446,866.61 USD | 7,951,649.62 USD | `7 orders` | `+0.08%` | `-` |
| `ASK` | `2246.80` | `170.1856` | 382,373.01 USD | 8,334,022.62 USD | `13 orders` | `+0.09%` | `-` |
| `ASK` | `2246.90` | `261.3091` | 587,135.42 USD | 8,921,158.04 USD | `18 orders` | `+0.09%` | `-` |
| `ASK` | `2247.00` | `110.9738` | 249,358.13 USD | 9,170,516.17 USD | `11 orders` | `+0.10%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:12:11 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1843.85` | `7,964.66` | 14,685,670.30 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 16:12:11 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 16:12:11 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1913.11` | `6,500.22` | 12,435,638.98 USD | `AT_RISK_LIQ` | `0xf78c5d8d4b` | `2026-10-30 16:12:11 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `10,000.00` | 19,261,000.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 16:12:11 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1930.52` | `8,092.45` | 15,622,633.76 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 16:12:11 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2121.80` | `30,641.99` | 65,016,272.46 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 16:12:11 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.08` | `26,025.05` | 55,409,441.07 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 16:12:11 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,533.33` | 7,684,999.71 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 16:12:11 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2195.00` | `839.60` | 1,842,926.39 USD | `TRIGGER_STOP` | `0x28280399d9` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.10` | `500.00` | 1,100,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2203.70` | `4,230.54` | 9,322,836.59 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2204.80` | `2,114.85` | 4,662,819.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2206.30` | `505.38` | 1,115,022.10 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.10` | `500.00` | 1,105,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2217.80` | `358.34` | 794,719.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2217.90` | `343.53` | 761,925.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 16:12:11 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2219.00` | `439.90` | 976,147.64 USD | `TRIGGER_STOP` | `0x369fd6445f` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2223.20` | `2,178.31` | 4,842,822.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2223.50` | `505.29` | 1,123,501.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2224.00` | `994.93` | 2,212,729.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.20` | `430.01` | 957,293.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2228.30` | `505.38` | 1,126,138.25 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2229.70` | `1,796.47` | 4,005,584.03 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2230.90` | `1,346.61` | 3,004,150.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2230.90` | `344.01` | 767,451.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2231.10` | `691.97` | 1,543,856.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2232.60` | `472.50` | 1,054,910.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2232.60` | `351.23` | 784,154.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2233.30` | `1,109.45` | 2,477,726.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.50` | `896.31` | 2,002,798.21 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2235.60` | `483.45` | 1,080,796.57 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2236.50` | `342.51` | 766,020.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2236.70` | `671.55` | 1,502,050.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2238.20` | `447.38` | 1,001,336.44 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2243.50` | `334.78` | 751,073.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.50` | `446.17` | 1,001,430.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2245.70` | `668.89` | 1,502,117.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2248.60` | `492.52` | 1,107,484.74 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2248.70` | `472.98` | 1,063,590.13 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2249.30` | `344.01` | 773,781.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2249.40` | `890.38` | 2,002,826.62 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2250.90` | `336.64` | 757,737.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2251.50` | `1,334.33` | 3,004,253.68 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2251.60` | `1,109.10` | 2,497,249.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2253.30` | `681.92` | 1,536,562.90 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2253.60` | `505.48` | 1,139,149.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2253.90` | `1,777.22` | 4,005,679.54 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2256.10` | `2,178.31` | 4,914,488.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2257.50` | `506.24` | 1,142,845.83 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2260.00` | `995.25` | 2,249,273.59 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2260.30` | `349.96` | 791,020.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2264.10` | `351.01` | 794,719.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2264.10` | `336.52` | 761,925.57 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2265.30` | `4,230.54` | 9,583,437.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2268.40` | `1,403.82` | 3,184,420.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.70` | `620.97` | 1,409,408.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.20` | `2,200.51` | 4,999,999.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb1ec7febea` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2274.90` | `505.20` | 1,149,277.21 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2279.90` | `2,039.99` | 4,650,973.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:12:11 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2283.60` | `4,133.45` | 9,439,135.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 16:12:11 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2300.00` | `4,002.10` | 9,204,832.99 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 16:12:11 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2478.67` | `22,046.99` | 54,647,122.27 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 16:12:11 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,002.39` | 7,547,704.95 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 16:12:11 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2623.84` | `10,000.00` | 26,238,434.09 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 16:12:11 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2657.69` | `9,700.00` | 25,779,622.97 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 16:12:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 230,498,256.20 USD | `102,676.40` | `2322.74` | `2244.80` | `3703.93` | 7,992,656.95 USD | `+3.47%` | `5X Cross` |
| `6` | `0xb83d...6e36` | `SHORT` | 100,173,249.72 USD | `44,580.89` | `2375.30` | `2244.80` | `4626.67` | 5,720,017.32 USD | `+5.71%` | `5X Cross` |
| `9` | `0x77dd...e0e9` | `LONG` | 68,794,335.57 USD | `30,641.99` | `2610.31` | `2244.80` | `2121.82` | -11,190,839.47 USD | `-16.27%` | `10X Cross` |
| `10` | `0xde8d...9524` | `LONG` | 67,980,967.62 USD | `30,282.40` | `2134.45` | `2244.80` | `1786.08` | 3,344,637.04 USD | `+4.92%` | `20X Cross` |
| `15` | `0x0392...d7d9` | `LONG` | 58,423,637.21 USD | `26,025.05` | `2518.71` | `2244.80` | `2129.10` | -7,126,084.87 USD | `-12.20%` | `9X Cross` |
| `22` | `0x8add...7d2c` | `SHORT` | 49,493,285.16 USD | `22,046.99` | `2271.09` | `2244.80` | `2476.31` | 577,612.14 USD | `+1.17%` | `25X Cross` |
| `25` | `0x15a4...dfdb` | `SHORT` | 44,898,000.00 USD | `20,000.00` | `2228.11` | `2244.80` | `3187.78` | -335,672.32 USD | `-0.75%` | `20X Cross` |
| `26` | `0xdf95...7d72` | `SHORT` | 44,265,219.14 USD | `19,716.37` | `2402.53` | `2244.80` | `4222.77` | 3,104,037.94 USD | `+7.01%` | `25X Cross` |
| `33` | `0x6046...b21d` | `LONG` | 35,776,551.98 USD | `15,927.59` | `2410.19` | `2244.80` | `1783.37` | -2,612,067.66 USD | `-7.30%` | `6X Cross` |
| `34` | `0xefe4...194b` | `SHORT` | 33,920,974.78 USD | `15,108.89` | `2250.33` | `2244.80` | `2894.53` | 79,041.97 USD | `+0.23%` | `20X Cross` |
| `37` | `0xb695...a92d` | `SHORT` | 33,217,895.67 USD | `14,795.73` | `2557.74` | `2244.80` | `3777.43` | 4,625,818.44 USD | `+13.93%` | `20X Cross` |
| `38` | `0xeced...6210` | `SHORT` | 32,970,671.28 USD | `14,687.58` | `2522.09` | `2244.80` | `3654.56` | 4,072,846.26 USD | `+12.35%` | `20X Cross` |
| `40` | `0x45d2...4029` | `SHORT` | 31,319,145.00 USD | `13,950.00` | `2443.60` | `2244.80` | `5289.49` | 2,769,137.46 USD | `+8.84%` | `20X Cross` |
| `42` | `0xa61c...66b9` | `LONG` | 28,934,848.80 USD | `12,888.00` | `2369.69` | `2244.80` | `1492.14` | -1,605,805.74 USD | `-5.55%` | `10X Cross` |
| `44` | `0x2371...0883` | `LONG` | 26,964,000.00 USD | `12,000.00` | `2421.77` | `2244.80` | `1279.06` | -2,097,294.85 USD | `-7.78%` | `20X Cross` |
| `45` | `0xbd1c...ff0e` | `LONG` | 26,941,200.00 USD | `12,000.00` | `2419.91` | `2244.80` | `1519.96` | -2,097,832.39 USD | `-7.79%` | `20X Cross` |
| `52` | `0x09dc...c094` | `LONG` | 24,700,500.00 USD | `11,000.00` | `2465.31` | `2244.80` | `1637.02` | -2,417,923.04 USD | `-9.79%` | `20X Cross` |
| `53` | `0x6c93...59a4` | `LONG` | 24,696,100.00 USD | `11,000.00` | `2441.15` | `2244.80` | `1601.99` | -2,156,572.73 USD | `-8.73%` | `20X Cross` |
| `54` | `0xa9de...e049` | `LONG` | 24,693,900.00 USD | `11,000.00` | `2481.81` | `2244.80` | `1643.70` | -2,606,079.46 USD | `-10.55%` | `20X Cross` |
| `55` | `0x0c5d...36b3` | `LONG` | 24,693,900.00 USD | `11,000.00` | `2482.20` | `2244.80` | `1644.03` | -2,610,353.24 USD | `-10.57%` | `20X Cross` |
| `58` | `0xecb6...2b00` | `SHORT` | 24,364,248.85 USD | `10,852.19` | `2238.55` | `2244.80` | `5231.34` | -70,977.09 USD | `-0.29%` | `15X Cross` |
| `71` | `0xa2ce...3126` | `LONG` | 22,488,886.51 USD | `10,016.88` | `2162.83` | `2244.80` | `1556.04` | 824,084.46 USD | `+3.66%` | `10X Cross` |
| `73` | `0xec7f...df39` | `LONG` | 22,456,000.00 USD | `10,000.00` | `2719.35` | `2244.80` | `1720.55` | -4,737,548.52 USD | `-21.10%` | `20X Cross` |
| `74` | `0x6646...6de5` | `LONG` | 22,451,000.00 USD | `10,000.00` | `1765.80` | `2244.80` | `1723.55` | 4,792,942.55 USD | `+21.35%` | `25X Cross` |
| `76` | `0x939f...04d2` | `LONG` | 22,053,477.58 USD | `9,823.81` | `2427.28` | `2244.80` | `1758.95` | -1,791,673.02 USD | `-8.12%` | `25X Cross` |
| `82` | `0xf517...c032` | `SHORT` | 20,938,581.87 USD | `9,326.35` | `2202.91` | `2244.80` | `3160.48` | -393,443.66 USD | `-1.88%` | `25X Cross` |
| `85` | `0xca49...53c8` | `SHORT` | 20,614,254.28 USD | `9,181.89` | `2549.39` | `2244.80` | `3892.15` | 2,794,023.11 USD | `+13.55%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 20,334,652.82 USD | `9,054.12` | `2493.89` | `2244.80` | `2761.28` | 2,245,354.43 USD | `+11.04%` | `20X Cross` |
| `88` | `0xea00...a918` | `LONG` | 20,222,593.87 USD | `9,003.83` | `2003.01` | `2244.80` | `1410.87` | 2,187,815.00 USD | `+10.82%` | `5X Cross` |
| `91` | `0x0622...8088` | `SHORT` | 19,874,099.84 USD | `8,849.85` | `2232.74` | `2244.80` | `3306.82` | -114,662.87 USD | `-0.58%` | `5X Cross` |
| `113` | `0x9eec...daab` | `LONG` | 18,168,364.21 USD | `8,092.45` | `1658.44` | `2244.80` | `1930.24` | 4,747,499.68 USD | `+26.13%` | `15X Cross` |
| `114` | `0x5f91...65aa` | `LONG` | 17,888,617.15 USD | `7,964.66` | `1626.99` | `2244.80` | `1843.87` | 4,930,174.09 USD | `+27.56%` | `16X Cross` |
| `121` | `0xec0b...b078` | `LONG` | 15,733,209.31 USD | `7,007.80` | `2065.97` | `2244.80` | `1059.27` | 1,255,279.72 USD | `+7.98%` | `25X Cross` |
| `129` | `0xf02d...5eb3` | `LONG` | 15,392,373.05 USD | `6,855.99` | `2383.33` | `2244.80` | `1115.58` | -947,715.72 USD | `-6.16%` | `20X Cross` |
| `131` | `0xcf53...ee11` | `SHORT` | 15,274,825.00 USD | `6,803.63` | `1862.69` | `2244.80` | `4194.05` | -2,601,719.61 USD | `-17.03%` | `7X Cross` |
| `135` | `0x4ff9...38d3` | `LONG` | 14,735,088.76 USD | `6,564.10` | `2447.40` | `2244.80` | `1669.64` | -1,329,933.98 USD | `-9.03%` | `3X Isolated` |
| `138` | `0xf78c...c581` | `LONG` | 14,599,497.49 USD | `6,500.22` | `2521.53` | `2244.80` | `1913.13` | -1,791,043.46 USD | `-12.27%` | `20X Cross` |
| `139` | `0x1ee7...edf5` | `LONG` | 14,599,000.00 USD | `6,500.00` | `2301.55` | `2244.80` | `2068.86` | -361,093.66 USD | `-2.47%` | `25X Cross` |
| `140` | `0x4e23...20c3` | `LONG` | 14,290,755.01 USD | `6,365.31` | `2228.10` | `2244.80` | `313.34` | 108,177.57 USD | `+0.76%` | `20X Cross` |
| `142` | `0x799f...5f4c` | `LONG` | 14,168,609.00 USD | `6,310.90` | `2390.33` | `2244.80` | `1867.59` | -916,555.62 USD | `-6.47%` | `20X Cross` |
| `145` | `0x08bf...7872` | `SHORT` | 13,973,608.82 USD | `6,224.05` | `2258.00` | `2244.80` | `2584.93` | 80,307.29 USD | `+0.57%` | `20X Cross` |
| `152` | `0xec4a...cf62` | `LONG` | 13,624,429.31 USD | `6,068.52` | `2223.80` | `2244.80` | `1961.03` | 129,213.99 USD | `+0.95%` | `25X Cross` |
| `153` | `0xd9e7...4aff` | `LONG` | 13,469,400.00 USD | `6,000.00` | `2480.18` | `2244.80` | `1407.42` | -1,411,724.33 USD | `-10.48%` | `20X Cross` |
| `154` | `0x524e...0de0` | `LONG` | 13,469,400.00 USD | `6,000.00` | `2246.48` | `2244.80` | `2002.83` | -9,485.04 USD | `-0.07%` | `10X Cross` |
| `156` | `0xc179...e0c8` | `LONG` | 13,144,455.67 USD | `5,854.73` | `2294.94` | `2244.80` | `1194.72` | -291,816.51 USD | `-2.22%` | `10X Cross` |
| `161` | `0x0c4a...1b19` | `LONG` | 12,705,786.87 USD | `5,660.10` | `2373.06` | `2244.80` | `2081.46` | -725,971.26 USD | `-5.71%` | `25X Isolated` |
| `184` | `0x45ab...6cbc` | `LONG` | 11,051,989.01 USD | `4,920.96` | `2727.66` | `2244.80` | `1373.18` | -2,370,754.79 USD | `-21.45%` | `7X Cross` |
| `187` | `0x64b7...9da9` | `LONG` | 10,904,089.69 USD | `4,856.84` | `2604.61` | `2244.80` | `589.58` | -1,746,124.73 USD | `-16.01%` | `25X Cross` |
| `193` | `0xfb18...eb17` | `SHORT` | 10,704,997.36 USD | `4,768.16` | `2315.53` | `2244.80` | `2615.45` | 335,832.33 USD | `+3.14%` | `25X Cross` |
| `196` | `0x7fda...17d1` | `LONG` | 10,684,916.96 USD | `4,759.22` | `2211.05` | `2244.80` | `0.000000` | 162,020.71 USD | `+1.52%` | `25X Cross` |
| `197` | `0x5559...d43b` | `SHORT` | 10,676,576.71 USD | `4,755.93` | `2262.69` | `2244.80` | `2741.25` | 84,629.17 USD | `+0.79%` | `25X Cross` |
| `210` | `0xe091...6705` | `SHORT` | 10,106,550.45 USD | `4,500.00` | `2467.33` | `2244.80` | `2463.05` | 996,458.06 USD | `+9.86%` | `20X Cross` |
| `211` | `0x418a...8888` | `SHORT` | 10,104,750.00 USD | `4,500.00` | `2494.55` | `2244.80` | `2992.71` | 1,120,734.41 USD | `+11.09%` | `25X Cross` |
| `219` | `0xb829...3a81` | `LONG` | 9,867,454.18 USD | `4,394.91` | `2398.60` | `2244.80` | `1460.25` | -674,187.77 USD | `-6.83%` | `20X Cross` |
| `235` | `0x28bb...fca6` | `SHORT` | 9,451,004.84 USD | `4,209.61` | `1896.10` | `2244.80` | `3033.77` | -1,469,122.28 USD | `-15.54%` | `20X Cross` |
| `237` | `0x6ea4...0ea7` | `SHORT` | 9,392,270.81 USD | `4,184.01` | `2602.13` | `2244.80` | `3424.99` | 1,495,075.86 USD | `+15.92%` | `20X Cross` |
| `250` | `0x5e9e...35ee` | `SHORT` | 8,997,363.30 USD | `4,007.56` | `1796.39` | `2244.80` | `2585.48` | -1,798,213.21 USD | `-19.99%` | `20X Cross` |
| `252` | `0xfb94...0ddf` | `SHORT` | 8,984,317.21 USD | `4,002.10` | `2382.44` | `2244.80` | `5104.38` | 550,466.94 USD | `+6.13%` | `20X Cross` |
| `253` | `0x3dc9...54b0` | `SHORT` | 8,983,304.19 USD | `3,999.69` | `2480.32` | `2244.80` | `6471.69` | 937,232.36 USD | `+10.43%` | `20X Cross` |
| `254` | `0x8cc9...2b6a` | `SHORT` | 8,982,800.00 USD | `4,000.00` | `1791.18` | `2244.80` | `3502.03` | -1,818,053.33 USD | `-20.24%` | `25X Cross` |
| `269` | `0x4b67...f4e7` | `LONG` | 8,577,407.98 USD | `3,820.84` | `2591.51` | `2244.80` | `1345.62` | -1,324,365.56 USD | `-15.44%` | `20X Cross` |
| `273` | `0x12d2...f97f` | `LONG` | 8,435,427.12 USD | `3,757.26` | `2446.50` | `2244.80` | `1785.56` | -756,739.27 USD | `-8.97%` | `20X Cross` |
| `292` | `0x8ae4...3d60` | `LONG` | 7,987,443.54 USD | `3,558.20` | `2482.21` | `2244.80` | `517.92` | -844,754.49 USD | `-10.58%` | `10X Cross` |
| `295` | `0x469e...58a5` | `SHORT` | 7,931,979.70 USD | `3,533.33` | `2203.63` | `2244.80` | `3070.26` | -145,816.61 USD | `-1.84%` | `25X Cross` |
| `301` | `0x218a...7da2` | `SHORT` | 7,778,731.60 USD | `3,465.07` | `2208.16` | `2244.80` | `3101.70` | -127,302.35 USD | `-1.64%` | `10X Cross` |
| `334` | `0x9c2a...f6a8` | `SHORT` | 6,743,365.02 USD | `3,002.39` | `2515.77` | `2244.80` | `2595.63` | 809,972.88 USD | `+12.01%` | `20X Cross` |
| `335` | `0xb823...9763` | `SHORT` | 6,736,500.00 USD | `3,000.00` | `2229.66` | `2244.80` | `3233.38` | -47,503.32 USD | `-0.71%` | `25X Cross` |
| `336` | `0x4a20...3c26` | `LONG` | 6,735,300.00 USD | `3,000.00` | `2428.72` | `2244.80` | `610.52` | -550,860.28 USD | `-8.18%` | `20X Cross` |
| `337` | `0x007d...67a0` | `LONG` | 6,735,300.00 USD | `3,000.00` | `2400.00` | `2244.80` | `1472.83` | -464,700.00 USD | `-6.90%` | `25X Cross` |
| `390` | `0x8328...f54a` | `SHORT` | 5,783,875.07 USD | `2,576.45` | `2292.01` | `2244.80` | `3279.22` | 121,396.21 USD | `+2.10%` | `25X Cross` |
| `396` | `0xed48...7c9b` | `SHORT` | 5,727,543.09 USD | `2,551.13` | `2460.02` | `2244.80` | `3237.73` | 548,303.32 USD | `+9.57%` | `20X Cross` |
| `399` | `0x970c...2a93` | `SHORT` | 5,612,250.00 USD | `2,500.00` | `2229.57` | `2244.80` | `5069.52` | -38,305.51 USD | `-0.68%` | `20X Cross` |
| `400` | `0x1c98...7fc7` | `LONG` | 5,612,010.10 USD | `2,500.00` | `2452.60` | `2244.80` | `1916.62` | -519,511.46 USD | `-9.26%` | `10X Cross` |
| `414` | `0xa445...329d` | `LONG` | 5,402,015.48 USD | `2,406.14` | `2354.86` | `2244.80` | `1766.81` | -264,099.80 USD | `-4.89%` | `25X Cross` |
| `416` | `0xfbe2...c8ea` | `SHORT` | 5,355,025.99 USD | `2,385.21` | `2041.57` | `2244.80` | `2623.12` | -485,459.33 USD | `-9.07%` | `20X Cross` |
| `417` | `0x6749...ce07` | `SHORT` | 5,354,325.97 USD | `2,384.89` | `2220.92` | `2244.80` | `3631.47` | -57,662.94 USD | `-1.08%` | `20X Cross` |
| `418` | `0x645b...87b8` | `SHORT` | 5,343,283.22 USD | `2,379.98` | `2421.64` | `2244.80` | `11290.77` | 420,163.74 USD | `+7.86%` | `10X Cross` |
| `424` | `0xd911...961e` | `SHORT` | 5,207,328.05 USD | `2,319.42` | `2231.05` | `2244.80` | `3154.73` | -32,575.28 USD | `-0.63%` | `25X Cross` |
| `429` | `0x77ee...2902` | `SHORT` | 5,133,668.05 USD | `2,290.69` | `2476.53` | `2244.80` | `6092.47` | 539,304.19 USD | `+10.51%` | `25X Cross` |
| `451` | `0xd507...c948` | `SHORT` | 4,876,356.98 USD | `2,172.00` | `2387.49` | `2244.80` | `2600.23` | 309,284.05 USD | `+6.34%` | `5X Isolated` |
| `457` | `0x023a...2355` | `LONG` | 4,810,849.67 USD | `2,142.82` | `2328.93` | `2244.80` | `0.000000` | -179,654.18 USD | `-3.73%` | `25X Cross` |
| `461` | `0x382b...3e39` | `SHORT` | 4,781,033.85 USD | `2,129.54` | `2296.66` | `2244.80` | `4605.84` | 109,803.37 USD | `+2.30%` | `25X Cross` |
| `497` | `0x3453...b323` | `SHORT` | 4,492,276.48 USD | `2,000.12` | `2322.47` | `2244.80` | `2392.40` | 152,959.36 USD | `+3.40%` | `25X Cross` |
| `498` | `0xe02e...d78b` | `LONG` | 4,490,200.00 USD | `2,000.00` | `2228.11` | `2244.80` | `2171.57` | 33,976.53 USD | `+0.76%` | `25X Cross` |
| `501` | `0xf3dc...1672` | `SHORT` | 4,447,891.48 USD | `1,980.36` | `2240.44` | `2244.80` | `2788.30` | -11,003.93 USD | `-0.25%` | `20X Cross` |
| `508` | `0x7a6d...f79c` | `SHORT` | 4,425,684.76 USD | `1,971.44` | `2418.41` | `2244.80` | `2547.08` | 342,076.42 USD | `+7.73%` | `25X Cross` |
| `511` | `0xac48...3201` | `SHORT` | 4,411,973.90 USD | `1,964.37` | `2272.04` | `2244.80` | `3096.48` | 51,168.40 USD | `+1.16%` | `20X Cross` |
| `519` | `0x8376...9a1e` | `SHORT` | 4,290,782.97 USD | `1,910.50` | `2477.72` | `2244.80` | `3185.44` | 442,905.20 USD | `+10.32%` | `20X Cross` |
| `521` | `0x739c...cfb2` | `SHORT` | 4,265,120.00 USD | `1,900.00` | `2418.12` | `2244.80` | `2459.08` | 329,326.38 USD | `+7.72%` | `25X Cross` |
| `546` | `0x7265...91a5` | `LONG` | 4,046,818.49 USD | `1,801.87` | `2533.96` | `2244.80` | `1987.09` | -519,047.97 USD | `-12.83%` | `20X Cross` |
| `548` | `0xbb34...1696` | `LONG` | 4,040,820.00 USD | `1,800.00` | `2313.95` | `2244.80` | `1956.23` | -124,298.23 USD | `-3.08%` | `25X Cross` |
| `549` | `0xc619...10f5` | `LONG` | 4,040,820.00 USD | `1,800.00` | `2313.55` | `2244.80` | `1789.35` | -123,575.83 USD | `-3.06%` | `25X Cross` |
| `560` | `0x91a9...3f70` | `SHORT` | 3,971,527.56 USD | `1,767.48` | `2156.23` | `2244.80` | `3649.05` | -160,423.48 USD | `-4.04%` | `4X Cross` |
| `568` | `0x020c...5872` | `LONG` | 3,928,925.00 USD | `1,750.00` | `2229.40` | `2244.80` | `2163.25` | 27,467.72 USD | `+0.70%` | `25X Cross` |
| `569` | `0xbcd4...0dd2` | `SHORT` | 3,925,463.84 USD | `1,747.52` | `2233.24` | `2244.80` | `2754.24` | -22,807.61 USD | `-0.58%` | `25X Cross` |
| `592` | `0xfeec...4e9c` | `SHORT` | 3,798,279.94 USD | `1,691.81` | `2566.49` | `2244.80` | `2509.14` | 543,744.58 USD | `+14.32%` | `10X Cross` |
| `597` | `0xb8eb...1dd5` | `SHORT` | 3,784,378.05 USD | `1,685.62` | `2232.60` | `2244.80` | `3311.68` | -21,053.77 USD | `-0.56%` | `25X Cross` |
| `615` | `0xeee0...0b53` | `LONG` | 3,676,816.57 USD | `1,637.12` | `2468.64` | `2244.80` | `163.53` | -364,659.49 USD | `-9.92%` | `7X Cross` |
| `620` | `0x27b8...12fc` | `LONG` | 3,655,455.25 USD | `1,628.12` | `2468.73` | `2244.80` | `633.08` | -363,939.39 USD | `-9.96%` | `10X Cross` |
| `621` | `0x982b...4606` | `LONG` | 3,652,042.16 USD | `1,626.82` | `2575.24` | `2244.80` | `1547.37` | -537,410.92 USD | `-14.72%` | `5X Isolated` |
| `627` | `0x73d7...8be1` | `LONG` | 3,595,450.19 USD | `1,601.47` | `2410.40` | `2244.80` | `1764.78` | -264,728.73 USD | `-7.36%` | `25X Cross` |
| `631` | `0xad54...6203` | `LONG` | 3,586,119.32 USD | `1,597.45` | `2591.98` | `2244.80` | `2043.77` | -554,458.72 USD | `-15.46%` | `10X Isolated` |
| `635` | `0x880a...311c` | `LONG` | 3,543,191.65 USD | `1,578.40` | `2209.72` | `2244.80` | `0.000000` | 55,367.79 USD | `+1.56%` | `9X Cross` |
| `641` | `0x936c...bb0f` | `LONG` | 3,512,783.37 USD | `1,564.64` | `2232.92` | `2244.80` | `0.000000` | 19,045.46 USD | `+0.54%` | `20X Cross` |
| `654` | `0xe170...9300` | `SHORT` | 3,444,323.08 USD | `1,533.40` | `2076.39` | `2244.80` | `3091.44` | -260,373.58 USD | `-7.56%` | `25X Cross` |
| `660` | `0x4b86...df9d` | `SHORT` | 3,423,208.80 USD | `1,524.00` | `2287.40` | `2244.80` | `2759.58` | 62,788.80 USD | `+1.83%` | `9X Isolated` |
| `663` | `0x2e2b...2fab` | `LONG` | 3,386,020.96 USD | `1,507.38` | `2245.53` | `2244.80` | `1212.21` | 1,147.86 USD | `+0.03%` | `25X Cross` |
| `665` | `0xde6b...3361` | `LONG` | 3,367,800.00 USD | `1,500.00` | `2216.98` | `2244.80` | `2168.50` | 42,319.26 USD | `+1.26%` | `25X Cross` |
| `666` | `0x251f...6e5d` | `LONG` | 3,367,650.00 USD | `1,500.00` | `2346.68` | `2244.80` | `1883.93` | -152,380.49 USD | `-4.52%` | `20X Cross` |
| `687` | `0xb885...3c54` | `LONG` | 3,255,399.94 USD | `1,450.00` | `2274.34` | `2244.80` | `41.99` | -42,408.20 USD | `-1.30%` | `20X Cross` |
| `690` | `0xef70...a84c` | `SHORT` | 3,239,103.21 USD | `1,442.74` | `2424.73` | `2244.80` | `3263.76` | 259,167.62 USD | `+8.00%` | `25X Cross` |
| `701` | `0xbadb...9ee6` | `LONG` | 3,200,935.01 USD | `1,428.16` | `1936.00` | `2244.80` | `1059.78` | 436,013.36 USD | `+13.62%` | `20X Cross` |
| `754` | `0x53f8...ceff` | `LONG` | 3,029,482.15 USD | `1,348.65` | `2276.73` | `2244.80` | `0.000000` | -41,042.31 USD | `-1.35%` | `20X Cross` |
| `767` | `0xa0fb...96be` | `LONG` | 2,980,000.30 USD | `1,327.28` | `2276.83` | `2244.80` | `1525.75` | -41,982.25 USD | `-1.41%` | `3X Cross` |
| `797` | `0x1f16...6d07` | `LONG` | 2,842,296.60 USD | `1,266.00` | `2261.43` | `2244.80` | `1378.82` | -20,674.63 USD | `-0.73%` | `7X Cross` |
| `807` | `0xc435...c905` | `SHORT` | 2,802,009.60 USD | `1,248.00` | `2704.38` | `2244.80` | `3763.04` | 573,060.75 USD | `+20.45%` | `20X Cross` |
| `814` | `0x6859...7e1e` | `SHORT` | 2,777,534.00 USD | `1,237.15` | `2200.39` | `2244.80` | `4811.71` | -55,306.84 USD | `-1.99%` | `25X Cross` |
| `821` | `0x7277...0b98` | `SHORT` | 2,737,795.95 USD | `1,219.45` | `2206.05` | `2244.80` | `3373.73` | -47,608.15 USD | `-1.74%` | `20X Cross` |
| `824` | `0x7178...0854` | `LONG` | 2,731,075.05 USD | `1,218.63` | `2461.81` | `2244.80` | `1183.83` | -268,971.35 USD | `-9.85%` | `10X Cross` |
| `836` | `0xaaa1...ab8c` | `SHORT` | 2,695,200.00 USD | `1,200.00` | `2276.29` | `2244.80` | `2365.20` | 36,357.58 USD | `+1.35%` | `25X Isolated` |
| `839` | `0x0dd5...f6ee` | `LONG` | 2,673,328.46 USD | `1,190.32` | `2286.90` | `2244.80` | `1483.12` | -48,802.97 USD | `-1.83%` | `5X Cross` |
| `849` | `0x07fd...689d` | `LONG` | 2,641,792.11 USD | `1,176.69` | `2416.34` | `2244.80` | `0.000000` | -201,507.83 USD | `-7.63%` | `25X Cross` |
| `909` | `0x2f80...f203` | `SHORT` | 2,445,435.03 USD | `1,088.94` | `1984.00` | `2244.80` | `2959.51` | -284,967.84 USD | `-11.65%` | `20X Cross` |
| `918` | `0x8eb7...b90f` | `LONG` | 2,420,494.47 USD | `1,077.74` | `2396.38` | `2244.80` | `1880.90` | -162,183.57 USD | `-6.70%` | `5X Isolated` |
| `920` | `0x2b61...2f6c` | `SHORT` | 2,416,745.39 USD | `1,076.60` | `2681.75` | `2244.80` | `6336.63` | 470,427.34 USD | `+19.47%` | `10X Cross` |
| `937` | `0x30af...393e` | `SHORT` | 2,339,497.53 USD | `1,041.16` | `2252.26` | `2244.80` | `2296.89` | 5,484.80 USD | `+0.23%` | `25X Cross` |
| `960` | `0x1b2a...f7a6` | `LONG` | 2,302,873.99 USD | `1,025.37` | `2737.51` | `2244.80` | `882.04` | -504,085.95 USD | `-21.89%` | `10X Cross` |
| `971` | `0xfc27...9d9d` | `LONG` | 2,272,133.92 USD | `1,012.04` | `2237.33` | `2244.80` | `0.000000` | 7,858.11 USD | `+0.35%` | `25X Cross` |
| `976` | `0x001a...fef6` | `SHORT` | 2,261,545.36 USD | `1,007.33` | `2022.19` | `2244.80` | `3084.39` | -224,537.40 USD | `-9.93%` | `10X Cross` |
| `977` | `0x02aa...1806` | `SHORT` | 2,260,939.72 USD | `1,007.10` | `2654.68` | `2244.80` | `3612.68` | 412,592.38 USD | `+18.25%` | `20X Cross` |
| `980` | `0xdb3a...cf3b` | `LONG` | 2,254,224.33 USD | `1,003.22` | `2705.01` | `2244.80` | `0.000000` | -459,482.56 USD | `-20.38%` | `4X Cross` |
| `983` | `0x8c02...b73f` | `SHORT` | 2,246,000.00 USD | `1,000.00` | `2250.37` | `2244.80` | `8098.36` | 4,371.47 USD | `+0.19%` | `20X Cross` |
| `984` | `0x6463...42f5` | `SHORT` | 2,245,600.00 USD | `1,000.00` | `2223.43` | `2244.80` | `3705.26` | -22,165.05 USD | `-0.99%` | `5X Cross` |
| `985` | `0x5272...fcd9` | `SHORT` | 2,245,100.00 USD | `1,000.00` | `2241.82` | `2244.80` | `2830.73` | -3,275.51 USD | `-0.15%` | `5X Cross` |
| `986` | `0xd7b8...9f55` | `LONG` | 2,243,953.80 USD | `999.00` | `2195.00` | `2244.80` | `0.000000` | 51,148.80 USD | `+2.28%` | `15X Cross` |
| `1007` | `0xb002...ed8a` | `SHORT` | 2,161,353.80 USD | `962.78` | `2299.66` | `2244.80` | `4197.32` | 52,724.11 USD | `+2.44%` | `25X Cross` |
| `1022` | `0xb1ec...e86a` | `SHORT` | 2,096,951.85 USD | `933.64` | `2272.72` | `2244.80` | `13143.27` | 24,955.11 USD | `+1.19%` | `25X Cross` |
| `1045` | `0xede2...f971` | `LONG` | 2,052,722.54 USD | `914.31` | `2208.16` | `2244.80` | `1462.95` | 33,765.56 USD | `+1.64%` | `5X Cross` |
| `1046` | `0xb812...b5e0` | `LONG` | 2,052,685.95 USD | `914.30` | `2263.21` | `2244.80` | `1148.74` | -16,561.96 USD | `-0.81%` | `25X Cross` |
| `1048` | `0x9606...4e5d` | `SHORT` | 2,050,225.39 USD | `913.00` | `2478.70` | `2244.80` | `3752.02` | 212,828.22 USD | `+10.38%` | `20X Cross` |
| `1073` | `0x5f10...d49d` | `LONG` | 2,020,590.00 USD | `900.00` | `2249.83` | `2244.80` | `1811.29` | -4,263.47 USD | `-0.21%` | `25X Cross` |
| `1083` | `0x51f6...2b39` | `LONG` | 1,998,470.15 USD | `890.15` | `2226.49` | `2244.80` | `788.86` | 16,563.26 USD | `+0.83%` | `25X Cross` |
| `1099` | `0x6f11...0389` | `SHORT` | 1,975,113.00 USD | `879.00` | `2333.39` | `2244.80` | `3150.78` | 75,937.71 USD | `+3.84%` | `25X Cross` |
| `1163` | `0x2828...93a0` | `LONG` | 1,884,822.53 USD | `839.60` | `2242.41` | `2244.80` | `2192.50` | 2,090.34 USD | `+0.11%` | `25X Cross` |
| `1166` | `0xcd27...52a8` | `LONG` | 1,879,448.91 USD | `837.21` | `2553.56` | `2244.80` | `1403.18` | -258,415.86 USD | `-13.75%` | `2X Cross` |
| `1225` | `0x04a9...95aa` | `LONG` | 1,797,600.00 USD | `800.00` | `2595.13` | `2244.80` | `1877.37` | -278,506.74 USD | `-15.49%` | `5X Cross` |
| `1226` | `0x7737...bf66` | `SHORT` | 1,795,452.84 USD | `799.79` | `2494.83` | `2244.80` | `24942.90` | 199,893.19 USD | `+11.13%` | `15X Cross` |
| `1261` | `0x458d...ab3b` | `LONG` | 1,739,229.54 USD | `774.75` | `2740.41` | `2244.80` | `1886.93` | -383,899.64 USD | `-22.07%` | `3X Isolated` |
| `1314` | `0xaa53...9cb7` | `LONG` | 1,639,678.93 USD | `730.34` | `2389.70` | `2244.80` | `1965.22` | -105,610.71 USD | `-6.44%` | `20X Cross` |
| `1315` | `0x3fc5...c0c1` | `SHORT` | 1,639,628.73 USD | `729.92` | `2702.11` | `2244.80` | `4601.76` | 332,713.47 USD | `+20.29%` | `25X Cross` |
| `1333` | `0xa189...94d7` | `SHORT` | 1,616,424.85 USD | `719.98` | `2691.84` | `2244.80` | `2914.83` | 321,647.81 USD | `+19.90%` | `25X Cross` |
| `1346` | `0x2f93...4404` | `LONG` | 1,588,344.26 USD | `707.47` | `1700.45` | `2244.80` | `1368.57` | 385,317.89 USD | `+24.26%` | `4X Isolated` |
| `1358` | `0x5605...fe0f` | `SHORT` | 1,576,803.88 USD | `702.14` | `2566.90` | `2244.80` | `3061.49` | 225,528.77 USD | `+14.30%` | `20X Cross` |
| `1364` | `0x0deb...0bc5` | `LONG` | 1,571,570.00 USD | `700.00` | `2071.05` | `2244.80` | `1597.16` | 121,834.21 USD | `+7.75%` | `20X Cross` |
| `1366` | `0x26e6...6b28` | `LONG` | 1,569,050.00 USD | `700.00` | `1835.24` | `2244.80` | `2043.00` | 284,378.47 USD | `+18.12%` | `20X Cross` |
| `1403` | `0x7b22...8a34` | `LONG` | 1,538,593.25 USD | `684.73` | `2228.49` | `2244.80` | `2181.56` | 12,669.68 USD | `+0.82%` | `25X Cross` |
| `1409` | `0x248e...6be2` | `SHORT` | 1,529,092.59 USD | `680.93` | `2282.89` | `2244.80` | `3445.64` | 25,393.07 USD | `+1.66%` | `20X Cross` |
| `1411` | `0xdbd1...29dd` | `SHORT` | 1,528,245.18 USD | `680.70` | `3030.57` | `2244.80` | `3770.09` | 534,675.94 USD | `+34.99%` | `6X Cross` |
| `1420` | `0x71e5...be04` | `LONG` | 1,521,429.73 USD | `677.67` | `2727.27` | `2244.80` | `1470.71` | -326,755.87 USD | `-21.48%` | `20X Cross` |
| `1428` | `0x0b23...f37b` | `LONG` | 1,515,847.50 USD | `675.00` | `2238.15` | `2244.80` | `592.61` | 5,090.86 USD | `+0.34%` | `5X Cross` |
| `1453` | `0x0cac...6170` | `SHORT` | 1,476,153.25 USD | `657.50` | `2146.55` | `2244.80` | `2839.17` | -64,791.05 USD | `-4.39%` | `20X Cross` |
| `1484` | `0xf00e...fe3d` | `SHORT` | 1,443,329.89 USD | `642.88` | `2333.21` | `2244.80` | `2461.13` | 56,648.08 USD | `+3.92%` | `20X Cross` |
| `1485` | `0xb15b...dbae` | `SHORT` | 1,443,312.36 USD | `642.64` | `2290.80` | `2244.80` | `2324.04` | 28,855.11 USD | `+2.00%` | `25X Cross` |
| `1489` | `0xffb2...5ed6` | `SHORT` | 1,436,022.48 USD | `640.77` | `2672.96` | `2244.80` | `2496.24` | 276,725.87 USD | `+19.27%` | `20X Cross` |
| `1505` | `0x8505...1821` | `SHORT` | 1,423,240.87 USD | `633.96` | `2239.93` | `2244.80` | `3897.67` | -3,209.27 USD | `-0.23%` | `20X Cross` |
| `1525` | `0xfce0...f4c0` | `SHORT` | 1,400,268.86 USD | `623.60` | `3129.61` | `2244.80` | `2807.77` | 551,357.73 USD | `+39.38%` | `20X Cross` |
| `1573` | `0x7050...5fff` | `SHORT` | 1,350,683.83 USD | `601.11` | `2245.52` | `2244.80` | `3284.23` | -883.72 USD | `-0.07%` | `25X Cross` |
| `1575` | `0xad02...eb65` | `LONG` | 1,348,392.35 USD | `600.62` | `2460.69` | `2244.80` | `1078.63` | -129,548.21 USD | `-9.61%` | `5X Cross` |
| `1576` | `0x24fb...ed0f` | `LONG` | 1,347,995.64 USD | `600.10` | `2205.72` | `2244.80` | `0.000000` | 24,351.80 USD | `+1.81%` | `15X Cross` |
| `1579` | `0x638f...f5f0` | `LONG` | 1,347,060.00 USD | `600.00` | `4011.50` | `2244.80` | `422.03` | -1,059,843.53 USD | `-78.68%` | `25X Cross` |
| `1651` | `0xfb99...37f3` | `LONG` | 1,269,756.11 USD | `565.34` | `2362.35` | `2244.80` | `1253.88` | -65,780.24 USD | `-5.18%` | `3X Cross` |
| `1664` | `0x844b...7f42` | `SHORT` | 1,259,949.90 USD | `561.00` | `2026.17` | `2244.80` | `3003.26` | -123,266.49 USD | `-9.78%` | `25X Cross` |
| `1679` | `0xabe6...1d99` | `SHORT` | 1,248,284.58 USD | `556.00` | `2484.68` | `2244.80` | `3120.88` | 133,211.31 USD | `+10.67%` | `20X Cross` |
| `1681` | `0x2a76...9a53` | `LONG` | 1,246,763.89 USD | `555.03` | `2231.40` | `2244.80` | `0.000000` | 8,267.79 USD | `+0.66%` | `25X Cross` |
| `1687` | `0xbef3...0d3e` | `LONG` | 1,240,250.28 USD | `552.33` | `2237.93` | `2244.80` | `2078.68` | 4,177.31 USD | `+0.34%` | `20X Cross` |
| `1691` | `0x6a41...a3b9` | `LONG` | 1,236,361.30 USD | `550.69` | `2237.64` | `2244.80` | `2084.03` | 4,103.30 USD | `+0.33%` | `20X Cross` |
| `1693` | `0x9599...c60a` | `SHORT` | 1,235,489.76 USD | `550.30` | `2241.99` | `2244.80` | `9391.95` | -1,709.24 USD | `-0.14%` | `20X Cross` |
| `1694` | `0x34fb...93de` | `SHORT` | 1,235,489.08 USD | `550.30` | `2234.27` | `2244.80` | `7022.50` | -5,956.14 USD | `-0.48%` | `20X Cross` |
| `1696` | `0x825c...465e` | `LONG` | 1,234,805.00 USD | `550.00` | `2208.12` | `2244.80` | `1189.22` | 20,335.50 USD | `+1.65%` | `4X Cross` |
| `1702` | `0xad21...fb6a` | `LONG` | 1,228,644.22 USD | `547.26` | `2565.80` | `2244.80` | `1732.95` | -175,508.78 USD | `-14.28%` | `6X Cross` |
| `1730` | `0xa70a...4be9` | `SHORT` | 1,200,194.54 USD | `534.58` | `2236.90` | `2244.80` | `4818.66` | -4,383.36 USD | `-0.37%` | `20X Cross` |
| `1741` | `0x2e30...4cb5` | `SHORT` | 1,187,480.54 USD | `528.92` | `2315.38` | `2244.80` | `11658.75` | 37,174.11 USD | `+3.13%` | `2X Cross` |
| `1754` | `0x6e6f...82a6` | `SHORT` | 1,177,360.10 USD | `524.27` | `2235.06` | `2244.80` | `4021.45` | -5,573.52 USD | `-0.47%` | `20X Cross` |
| `1767` | `0x0a97...347d` | `SHORT` | 1,165,770.20 USD | `519.25` | `2236.28` | `2244.80` | `3748.06` | -4,576.80 USD | `-0.39%` | `20X Cross` |
| `1780` | `0x6dae...90de` | `SHORT` | 1,161,251.13 USD | `517.05` | `2292.28` | `2244.80` | `3794.42` | 23,982.29 USD | `+2.07%` | `25X Cross` |
| `1801` | `0xfc66...ca06` | `SHORT` | 1,147,003.85 USD | `510.89` | `2275.19` | `2244.80` | `55340.98` | 15,377.74 USD | `+1.34%` | `20X Cross` |
| `1812` | `0x0089...2410` | `SHORT` | 1,139,041.61 USD | `507.35` | `2308.88` | `2244.80` | `3410.54` | 32,358.65 USD | `+2.84%` | `20X Cross` |
| `1829` | `0x6936...9417` | `SHORT` | 1,123,000.00 USD | `500.00` | `2315.11` | `2244.80` | `2358.68` | 34,555.21 USD | `+3.08%` | `25X Isolated` |
| `1830` | `0xa559...ff95` | `LONG` | 1,122,950.00 USD | `500.00` | `2260.68` | `2244.80` | `1062.07` | -7,394.36 USD | `-0.66%` | `20X Cross` |
| `1831` | `0x4044...794c` | `LONG` | 1,122,950.00 USD | `500.00` | `2260.80` | `2244.80` | `0.000000` | -7,450.00 USD | `-0.66%` | `25X Cross` |
| `1834` | `0x89b2...9ca6` | `LONG` | 1,122,550.00 USD | `500.00` | `2363.45` | `2244.80` | `1622.41` | -59,177.42 USD | `-5.27%` | `25X Cross` |
| `1835` | `0xb322...d51f` | `SHORT` | 1,122,550.00 USD | `500.00` | `2268.03` | `2244.80` | `3743.51` | 11,466.32 USD | `+1.02%` | `20X Cross` |
| `1836` | `0xe282...df29` | `LONG` | 1,122,450.00 USD | `500.00` | `2309.84` | `2244.80` | `2045.08` | -32,474.21 USD | `-2.89%` | `10X Isolated` |
| `1842` | `0x7298...7d6c` | `SHORT` | 1,118,295.36 USD | `498.15` | `3426.75` | `2244.80` | `5421.39` | 588,740.46 USD | `+52.65%` | `20X Cross` |
| `1855` | `0x9c68...7783` | `SHORT` | 1,107,722.66 USD | `493.31` | `2273.58` | `2244.80` | `3886.63` | 13,856.58 USD | `+1.25%` | `25X Cross` |
| `1866` | `0x404c...5f03` | `SHORT` | 1,099,616.98 USD | `489.79` | `2671.94` | `2244.80` | `4964.50` | 209,062.58 USD | `+19.01%` | `20X Cross` |
| `1870` | `0x321f...1c84` | `SHORT` | 1,093,691.31 USD | `488.02` | `2370.09` | `2244.80` | `3064.86` | 62,953.29 USD | `+5.76%` | `10X Cross` |
| `1872` | `0x94b6...e5b3` | `SHORT` | 1,091,232.20 USD | `486.05` | `2260.75` | `2244.80` | `2374.19` | 7,610.39 USD | `+0.70%` | `25X Cross` |
| `1930` | `0x82c6...fe42` | `LONG` | 1,038,775.00 USD | `462.50` | `2501.38` | `2244.80` | `2053.42` | -118,115.57 USD | `-11.37%` | `5X Isolated` |
| `1939` | `0xe330...77a1` | `SHORT` | 1,035,304.00 USD | `461.20` | `2206.97` | `2244.80` | `6447.97` | -17,446.64 USD | `-1.69%` | `20X Cross` |
| `1951` | `0x617e...0f97` | `SHORT` | 1,027,928.91 USD | `457.85` | `2205.60` | `2244.80` | `3313.55` | -18,085.08 USD | `-1.76%` | `10X Cross` |
| `1981` | `0xae55...2236` | `LONG` | 1,010,295.00 USD | `450.00` | `2510.21` | `2244.80` | `0.000000` | -119,302.50 USD | `-11.81%` | `25X Cross` |
| `1990` | `0xf71a...7215` | `LONG` | 1,006,459.16 USD | `447.91` | `2223.27` | `2244.80` | `1111.48` | 10,624.88 USD | `+1.06%` | `25X Cross` |
| `2001` | `0xac26...a9c7` | `SHORT` | 1,001,410.47 USD | `446.04` | `2192.58` | `2244.80` | `8655.00` | -23,424.27 USD | `-2.34%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `2553.00` | 4,921.42 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 4.92K USD at 2553.0000 USD [API] | `2026-10-07 13:39:04` |
| `ANNOUNCEMENT` | `INFO` | `2553.20` | 15,355.71 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 15.36K USD at 2553.2000 USD [API] | `2026-10-07 13:39:04` |
| `ANNOUNCEMENT` | `INFO` | `2338.40` | 43,486.99 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 43.49K USD at 2338.4000 USD [API] | `2026-10-29 17:41:19` |
| `ANNOUNCEMENT` | `INFO` | `2380.80` | 43.33 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.04K USD at 2380.8000 USD [API] | `2026-10-22 16:45:54` |
| `ANNOUNCEMENT` | `INFO` | `2330.90` | 40,043.93 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 40.04K USD at 2330.9000 USD [API] | `2026-10-29 18:31:28` |
| `ANNOUNCEMENT` | `INFO` | `2327.50` | 60,399.56 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 60.40K USD at 2327.5000 USD [API] | `2026-10-29 18:35:32` |
| `ANNOUNCEMENT` | `INFO` | `2430.50` | 11,757.54 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 11.76K USD at 2430.5000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2430.50` | 278.78 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.28K USD at 2430.5000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2430.50` | 23.58 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2430.5000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2430.60` | 11,151.59 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 11.15K USD at 2430.6000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2430.60` | 38,494.14 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 38.49K USD at 2430.6000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2430.70` | 607.67 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.61K USD at 2430.7000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2430.80` | 29.90 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.03K USD at 2430.8000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2430.90` | 25,158.11 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 25.16K USD at 2430.9000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2431.00` | 20.18 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2431.0000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2431.00` | 9,706.74 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 9.71K USD at 2431.0000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2323.80` | 24,580.23 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 24.58K USD at 2323.8000 USD [API] | `2026-10-29 18:31:51` |
| `ANNOUNCEMENT` | `INFO` | `2310.30` | 21,500.34 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 21.50K USD at 2310.3000 USD [API] | `2026-10-25 23:30:50` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2275.30` (Vol: 35,200,000.00 USD, Dist: `+1.52%`) | Long MP=`2174.37` (Vol: 35,800,000.00 USD, Dist: `--2.98%`)
  * 48H Horizon: Short MP=`2270.12` (Vol: 35,900,000.00 USD, Dist: `+1.29%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--3.00%`)
  * 3D Horizon: Short MP=`2270.12` (Vol: 35,900,000.00 USD, Dist: `+1.29%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--3.00%`)
  * 7D Horizon: Short MP=`2401.80` (Vol: 50,700,000.00 USD, Dist: `+7.17%`) | Long MP=`2175.27` (Vol: 44,800,000.00 USD, Dist: `--2.94%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `455.00` | 121,330.00 USD | 786,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `465.00` | 118,030.00 USD | 786,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 81,110.00 USD | 786,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 2,960.00 USD | 786,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 140,880.00 USD | 786,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 67,370.00 USD | 786,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 39,200.00 USD | 786,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 1,870,000.00 USD | 786,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 34,560.00 USD | 784,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 53,010.00 USD | 784,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 66,580.00 USD | 784,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 158,160.00 USD | 784,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 64,830.00 USD | 783,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 44,160.00 USD | 783,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 3,330,000.00 USD | 783,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 154,720.00 USD | 780,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 142,040.00 USD | 780,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 1,880,000.00 USD | 780,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 51,410.00 USD | 778,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 1,150,000.00 USD | 778,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 46,320.00 USD | 777,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 54,620.00 USD | 777,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 46,090.00 USD | 777,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 44,110.00 USD | 776,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 2,640.00 USD | 776,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 15,790.00 USD | 776,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 54,550.00 USD | 776,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 1,080,000.00 USD | 776,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 78,630.00 USD | 775,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 9,220.00 USD | 775,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 55,210.00 USD | 775,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 5,250.00 USD | 775,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 72,970.00 USD | 775,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 16,550.00 USD | 775,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 6,010.00 USD | 775,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 85,220.00 USD | 775,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 95,130.00 USD | 775,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 129,310.00 USD | 775,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 62,560.00 USD | 775,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 375,830.00 USD | 775,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 214,080.00 USD | 774,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 17,290.00 USD | 774,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 88,960.00 USD | 774,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 964,270.00 USD | 774,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 175,070.00 USD | 773,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 18,280.00 USD | 773,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 605,510.00 USD | 773,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 164,030.00 USD | 772,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 297,070.00 USD | 772,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 91,310.00 USD | 772,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 294,230.00 USD | 772,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 47,900.00 USD | 771,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 183,680.00 USD | 771,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 105,940.00 USD | 771,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 336,130.00 USD | 771,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 113,820.00 USD | 771,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 155,360.00 USD | 771,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 63,130.00 USD | 770,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 60,140.00 USD | 770,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 702,780.00 USD | 770,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 7,410,000.00 USD | 770,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 557,690.00 USD | 762,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 721,980.00 USD | 762,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 1,890,000.00 USD | 761,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 676,930.00 USD | 759,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 217,450.00 USD | 758,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 206,920.00 USD | 758,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 7,930,000.00 USD | 758,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 86,940.00 USD | 750,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 850,610.00 USD | 750,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 599,140.00 USD | 749,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 1,630,000.00 USD | 748,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 261,700.00 USD | 747,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 2,670,000.00 USD | 747,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 330,450.00 USD | 744,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 7,250,000.00 USD | 744,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 80,960.00 USD | 736,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 405,620.00 USD | 736,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 116,280.00 USD | 736,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 53,980.00 USD | 736,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 1,200,000.00 USD | 736,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 2,220,000.00 USD | 734,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 15,490,000.00 USD | 732,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 556,180.00 USD | 717,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 378,160.00 USD | 716,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 125,780.00 USD | 716,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 306,940.00 USD | 716,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 640,550.00 USD | 715,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 286,420.00 USD | 715,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 580,160.00 USD | 714,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 5,240,000.00 USD | 714,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 1,100,000.00 USD | 709,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 7,130,000.00 USD | 708,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 2,300,000.00 USD | 700,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 520,350.00 USD | 698,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 10,130,000.00 USD | 698,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 554,220.00 USD | 687,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 372,990.00 USD | 687,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 1,210,000.00 USD | 687,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 2,120,000.00 USD | 685,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 19,770,000.00 USD | 683,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 2,030,000.00 USD | 663,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 5,960,000.00 USD | 661,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 139,630.00 USD | 655,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 19,510,000.00 USD | 655,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 293,500.00 USD | 636,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 20,980,000.00 USD | 636,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 275,130.00 USD | 615,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 1,060,000.00 USD | 614,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 2,710,000.00 USD | 613,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 3,810,000.00 USD | 610,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 16,680,000.00 USD | 607,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 747,200.00 USD | 590,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 1,100,000.00 USD | 589,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 1,470,000.00 USD | 588,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 17,980,000.00 USD | 587,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 410,710.00 USD | 569,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 1,110,000.00 USD | 568,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 18,690,000.00 USD | 567,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 36,670,000.00 USD | 548,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 533,660.00 USD | 512,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 12,350,000.00 USD | 511,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 1,460,000.00 USD | 499,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 1,220,000.00 USD | 497,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 870,240.00 USD | 496,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 17,250,000.00 USD | 495,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 17,850,000.00 USD | 478,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 19,370,000.00 USD | 460,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 1,390,000.00 USD | 441,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 1,110,000.00 USD | 440,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 225,470.00 USD | 438,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 3,830,000.00 USD | 438,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 4,970,000.00 USD | 434,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 83,330,000.00 USD | 429,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 1,160,000.00 USD | 346,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 8,320,000.00 USD | 345,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 2,190,000.00 USD | 337,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 4,200,000.00 USD | 334,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 1,110,000.00 USD | 330,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 16,340,000.00 USD | 329,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 1,120,000.00 USD | 313,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 1,300,000.00 USD | 312,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 18,820,000.00 USD | 310,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 4,920,000.00 USD | 291,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 1,310,000.00 USD | 287,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 3,660,000.00 USD | 285,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 17,910,000.00 USD | 282,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 1,370,000.00 USD | 264,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 17,760,000.00 USD | 262,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 1,690,000.00 USD | 245,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 1,410,000.00 USD | 243,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 14,400,000.00 USD | 241,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1972.30` | 849,340,000.00 USD | 849,340,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,630,000.00 USD | 227,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1975.10` | 849,210,000.00 USD | 849,210,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1977.90` | 849,160,000.00 USD | 849,160,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1983.50` | 846,920,000.00 USD | 846,920,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1985.00` | 5,570,000.00 USD | 225,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1986.30` | 846,720,000.00 USD | 846,720,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1989.10` | 842,980,000.00 USD | 842,980,000.00 USD | 0.00 USD | 1,780,000.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1991.90` | 841,170,000.00 USD | 841,170,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1994.70` | 838,460,000.00 USD | 838,460,000.00 USD | 0.00 USD | 0.00 USD | 808,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1995.00` | 5,340,000.00 USD | 220,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1997.50` | 837,650,000.00 USD | 837,650,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1997.90` | 714,930,000.00 USD | 714,930,000.00 USD | 219,590.00 USD | 92,480.00 USD | 328,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2000.40` | 714,290,000.00 USD | 714,290,000.00 USD | 218,020.00 USD | 248,200.00 USD | 586,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2002.90` | 713,230,000.00 USD | 713,230,000.00 USD | 738,150.00 USD | 702,190.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2003.10` | 836,310,000.00 USD | 836,310,000.00 USD | 0.00 USD | 266,430.00 USD | 617,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2005.00` | 13,090,000.00 USD | 214,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2005.40` | 710,620,000.00 USD | 710,620,000.00 USD | 773,690.00 USD | 17,210.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2005.90` | 835,430,000.00 USD | 835,430,000.00 USD | 0.00 USD | 475,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2007.90` | 709,820,000.00 USD | 709,820,000.00 USD | 0.00 USD | 558,480.00 USD | 281,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2008.70` | 834,950,000.00 USD | 834,950,000.00 USD | 807,770.00 USD | 0.00 USD | 380,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2010.40` | 708,980,000.00 USD | 708,980,000.00 USD | 484,920.00 USD | 490,130.00 USD | 374,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2011.50` | 833,760,000.00 USD | 833,760,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2012.90` | 707,630,000.00 USD | 707,630,000.00 USD | 323,800.00 USD | 270,490.00 USD | 25,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2015.00` | 2,660,000.00 USD | 201,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2015.40` | 707,010,000.00 USD | 707,010,000.00 USD | 478,950.00 USD | 605,010.00 USD | 208,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2017.10` | 832,810,000.00 USD | 832,810,000.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2017.90` | 705,720,000.00 USD | 705,720,000.00 USD | 1,170,000.00 USD | 1,040,000.00 USD | 553,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2019.90` | 832,790,000.00 USD | 832,790,000.00 USD | 820,980.00 USD | 466,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2020.40` | 702,960,000.00 USD | 702,960,000.00 USD | 789,460.00 USD | 1,620,000.00 USD | 696,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2022.70` | 831,500,000.00 USD | 831,500,000.00 USD | 1,830,000.00 USD | 484,980.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2022.90` | 699,850,000.00 USD | 699,850,000.00 USD | 1,610,000.00 USD | 333,350.00 USD | 1,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,180,000.00 USD | 199,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2025.40` | 696,010,000.00 USD | 696,010,000.00 USD | 414,330.00 USD | 1,190,000.00 USD | 231,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2025.50` | 827,640,000.00 USD | 827,640,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2027.90` | 694,170,000.00 USD | 694,170,000.00 USD | 2,770,000.00 USD | 978,910.00 USD | 312,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.30` | 827,460,000.00 USD | 827,460,000.00 USD | 1,100,000.00 USD | 0.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2030.40` | 690,110,000.00 USD | 690,110,000.00 USD | 87,180.00 USD | 366,120.00 USD | 957,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.10` | 826,330,000.00 USD | 826,330,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.90` | 688,700,000.00 USD | 688,700,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2033.90` | 821,760,000.00 USD | 821,760,000.00 USD | 0.00 USD | 0.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 1,110,000.00 USD | 198,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2035.40` | 685,140,000.00 USD | 685,140,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2036.70` | 820,400,000.00 USD | 820,400,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2037.90` | 683,800,000.00 USD | 683,800,000.00 USD | 396,700.00 USD | 458,110.00 USD | 388,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2039.50` | 820,070,000.00 USD | 820,070,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2040.40` | 682,560,000.00 USD | 682,560,000.00 USD | 834,710.00 USD | 178,560.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2042.90` | 681,520,000.00 USD | 681,520,000.00 USD | 334,790.00 USD | 0.00 USD | 174,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 6,580,000.00 USD | 196,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2045.10` | 818,620,000.00 USD | 818,620,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2045.40` | 681,010,000.00 USD | 681,010,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2047.90` | 680,980,000.00 USD | 680,980,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.40` | 680,160,000.00 USD | 680,160,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2050.70` | 818,320,000.00 USD | 818,320,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2052.90` | 679,050,000.00 USD | 679,050,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2053.50` | 818,100,000.00 USD | 818,100,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 3,870,000.00 USD | 190,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2055.40` | 679,020,000.00 USD | 679,020,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2057.90` | 678,690,000.00 USD | 678,690,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2059.10` | 815,810,000.00 USD | 815,810,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.90` | 815,470,000.00 USD | 815,470,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2062.90` | 677,940,000.00 USD | 677,940,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.70` | 810,210,000.00 USD | 810,210,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 15,510,000.00 USD | 186,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2065.40` | 677,860,000.00 USD | 677,860,000.00 USD | 563,140.00 USD | 537,030.00 USD | 510,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2067.50` | 807,750,000.00 USD | 807,750,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2067.90` | 676,250,000.00 USD | 676,250,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2070.30` | 806,100,000.00 USD | 806,100,000.00 USD | 3,600,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2070.40` | 675,550,000.00 USD | 675,550,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2072.90` | 675,180,000.00 USD | 675,180,000.00 USD | 47,910.00 USD | 555,250.00 USD | 420,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2073.10` | 798,540,000.00 USD | 798,540,000.00 USD | 2,870,000.00 USD | 2,180,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 3,430,000.00 USD | 170,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2075.40` | 674,150,000.00 USD | 674,150,000.00 USD | 379,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2075.90` | 791,460,000.00 USD | 791,460,000.00 USD | 3,910,000.00 USD | 4,290,000.00 USD | 4,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2077.90` | 673,770,000.00 USD | 673,770,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.70` | 778,960,000.00 USD | 778,960,000.00 USD | 4,160,000.00 USD | 3,730,000.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2080.40` | 673,750,000.00 USD | 673,750,000.00 USD | 77,960.00 USD | 29,610.00 USD | 199,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.50` | 769,010,000.00 USD | 769,010,000.00 USD | 4,400,000.00 USD | 1,290,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2082.90` | 673,440,000.00 USD | 673,440,000.00 USD | 827,940.00 USD | 4,240.00 USD | 206,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.30` | 762,100,000.00 USD | 762,100,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 12,820,000.00 USD | 167,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2085.40` | 672,400,000.00 USD | 672,400,000.00 USD | 528,660.00 USD | 200,510.00 USD | 820,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2087.10` | 754,720,000.00 USD | 754,720,000.00 USD | 2,920,000.00 USD | 2,750,000.00 USD | 3,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2087.90` | 670,850,000.00 USD | 670,850,000.00 USD | 324,560.00 USD | 180,420.00 USD | 306,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2089.90` | 746,030,000.00 USD | 746,030,000.00 USD | 4,130,000.00 USD | 948,120.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2090.40` | 670,040,000.00 USD | 670,040,000.00 USD | 758,170.00 USD | 223,260.00 USD | 445,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2092.70` | 737,790,000.00 USD | 737,790,000.00 USD | 4,680,000.00 USD | 737,060.00 USD | 6,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.90` | 668,620,000.00 USD | 668,620,000.00 USD | 655,300.00 USD | 228,180.00 USD | 275,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,840,000.00 USD | 154,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2095.40` | 667,460,000.00 USD | 667,460,000.00 USD | 1,840,000.00 USD | 1,130,000.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2095.50` | 726,160,000.00 USD | 726,160,000.00 USD | 2,480,000.00 USD | 2,010,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2097.90` | 662,920,000.00 USD | 662,920,000.00 USD | 345,860.00 USD | 488,160.00 USD | 309,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2098.30` | 720,650,000.00 USD | 720,650,000.00 USD | 3,020,000.00 USD | 3,130,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2100.40` | 661,780,000.00 USD | 661,780,000.00 USD | 137,320.00 USD | 928,890.00 USD | 231,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.10` | 713,030,000.00 USD | 713,030,000.00 USD | 631,640.00 USD | 1,240,000.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.90` | 660,480,000.00 USD | 660,480,000.00 USD | 279,330.00 USD | 222,480.00 USD | 302,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2103.90` | 707,750,000.00 USD | 707,750,000.00 USD | 1,130,000.00 USD | 738,240.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 2,360,000.00 USD | 152,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2105.40` | 659,670,000.00 USD | 659,670,000.00 USD | 3,510,000.00 USD | 1,160,000.00 USD | 833,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2106.70` | 703,560,000.00 USD | 703,560,000.00 USD | 1,700,000.00 USD | 834,660.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2107.90` | 654,170,000.00 USD | 654,170,000.00 USD | 795,870.00 USD | 0.00 USD | 347,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2109.50` | 699,850,000.00 USD | 699,850,000.00 USD | 7,750,000.00 USD | 1,800,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.40` | 653,030,000.00 USD | 653,030,000.00 USD | 36,110.00 USD | 31,550.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2112.30` | 688,530,000.00 USD | 688,530,000.00 USD | 3,920,000.00 USD | 1,480,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2112.90` | 652,960,000.00 USD | 652,960,000.00 USD | 866,490.00 USD | 506,690.00 USD | 244,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 2,210,000.00 USD | 150,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2115.10` | 679,410,000.00 USD | 679,410,000.00 USD | 923,330.00 USD | 3,210,000.00 USD | 1,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2115.40` | 651,340,000.00 USD | 651,340,000.00 USD | 410,020.00 USD | 400,200.00 USD | 939,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2117.90` | 649,590,000.00 USD | 649,590,000.00 USD | 4,540,000.00 USD | 3,940,000.00 USD | 302,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.90` | 673,340,000.00 USD | 673,340,000.00 USD | 8,390,000.00 USD | 578,010.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.40` | 640,800,000.00 USD | 640,800,000.00 USD | 5,470,000.00 USD | 325,610.00 USD | 671,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2120.70` | 661,790,000.00 USD | 661,790,000.00 USD | 7,060,000.00 USD | 5,780,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2122.90` | 634,330,000.00 USD | 634,330,000.00 USD | 5,450,000.00 USD | 3,490,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2123.50` | 647,140,000.00 USD | 647,140,000.00 USD | 7,150,000.00 USD | 7,720,000.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,700,000.00 USD | 148,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.40` | 622,730,000.00 USD | 622,730,000.00 USD | 4,480,000.00 USD | 2,390,000.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2126.30` | 630,860,000.00 USD | 630,860,000.00 USD | 2,740,000.00 USD | 4,400,000.00 USD | 4,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2127.90` | 614,540,000.00 USD | 614,540,000.00 USD | 4,430,000.00 USD | 3,780,000.00 USD | 745,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2129.10` | 618,930,000.00 USD | 618,930,000.00 USD | 4,770,000.00 USD | 1,270,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2130.40` | 605,590,000.00 USD | 605,590,000.00 USD | 1,250,000.00 USD | 18,610.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2131.90` | 611,780,000.00 USD | 611,780,000.00 USD | 2,170,000.00 USD | 1,620,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2132.90` | 603,180,000.00 USD | 603,180,000.00 USD | 95,260.00 USD | 434,790.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.70` | 606,630,000.00 USD | 606,630,000.00 USD | 1,630,000.00 USD | 790,240.00 USD | 898,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 1,490,000.00 USD | 24,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2135.40` | 601,110,000.00 USD | 601,110,000.00 USD | 2,760,000.00 USD | 2,950,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.50` | 603,320,000.00 USD | 603,320,000.00 USD | 2,120,000.00 USD | 2,390,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2137.90` | 593,180,000.00 USD | 593,180,000.00 USD | 772,430.00 USD | 1,700,000.00 USD | 943,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.30` | 597,230,000.00 USD | 597,230,000.00 USD | 3,990,000.00 USD | 1,870,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2140.40` | 589,760,000.00 USD | 589,760,000.00 USD | 2,180,000.00 USD | 1,310,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2142.90` | 585,200,000.00 USD | 585,200,000.00 USD | 1,080,000.00 USD | 3,170,000.00 USD | 955,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2143.10` | 589,680,000.00 USD | 589,680,000.00 USD | 2,380,000.00 USD | 618,280.00 USD | 333,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 5,640,000.00 USD | 23,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2145.40` | 579,990,000.00 USD | 579,990,000.00 USD | 3,170,000.00 USD | 2,110,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2145.90` | 586,350,000.00 USD | 586,350,000.00 USD | 978,940.00 USD | 1,450,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2147.90` | 573,660,000.00 USD | 573,660,000.00 USD | 728,710.00 USD | 1,050,000.00 USD | 114,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2148.70` | 582,200,000.00 USD | 582,200,000.00 USD | 26,270.00 USD | 538,910.00 USD | 399,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2150.40` | 571,760,000.00 USD | 571,760,000.00 USD | 7,890,000.00 USD | 3,310,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2151.50` | 581,230,000.00 USD | 581,230,000.00 USD | 11,290,000.00 USD | 363,770.00 USD | 107,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2152.90` | 557,910,000.00 USD | 557,910,000.00 USD | 4,360,000.00 USD | 3,370,000.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.30` | 569,470,000.00 USD | 569,470,000.00 USD | 2,100,000.00 USD | 3,920,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 1,690,000.00 USD | 17,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2155.40` | 547,780,000.00 USD | 547,780,000.00 USD | 4,430,000.00 USD | 5,320,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2157.10` | 561,870,000.00 USD | 561,870,000.00 USD | 6,160,000.00 USD | 2,540,000.00 USD | 6,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2157.90` | 535,660,000.00 USD | 535,660,000.00 USD | 4,230,000.00 USD | 2,360,000.00 USD | 4,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2159.90` | 546,570,000.00 USD | 546,570,000.00 USD | 2,980,000.00 USD | 737,260.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2160.40` | 524,570,000.00 USD | 524,570,000.00 USD | 4,790,000.00 USD | 6,030,000.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2162.70` | 541,010,000.00 USD | 541,010,000.00 USD | 17,980,000.00 USD | 1,960,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2162.90` | 510,830,000.00 USD | 510,830,000.00 USD | 18,720,000.00 USD | 10,660,000.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 6,700,000.00 USD | 15,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2165.40` | 478,860,000.00 USD | 478,860,000.00 USD | 9,360,000.00 USD | 11,850,000.00 USD | 4,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2165.50` | 521,070,000.00 USD | 521,070,000.00 USD | 8,990,000.00 USD | 17,170,000.00 USD | 2,900,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.90` | 453,210,000.00 USD | 453,210,000.00 USD | 18,870,000.00 USD | 6,950,000.00 USD | 5,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2168.30` | 492,010,000.00 USD | 492,010,000.00 USD | 12,290,000.00 USD | 16,150,000.00 USD | 3,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.40` | 422,260,000.00 USD | 422,260,000.00 USD | 24,230,000.00 USD | 8,680,000.00 USD | 7,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2171.10` | 459,810,000.00 USD | 459,810,000.00 USD | 1,860,000.00 USD | 6,380,000.00 USD | 5,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2172.90` | 381,950,000.00 USD | 381,950,000.00 USD | 6,820,000.00 USD | 3,860,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.90` | 446,010,000.00 USD | 446,010,000.00 USD | 35,100,000.00 USD | 0.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 5,690,000.00 USD | 9,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.40` | 367,820,000.00 USD | 367,820,000.00 USD | 3,650,000.00 USD | 85,890.00 USD | 914,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2176.70` | 409,900,000.00 USD | 409,900,000.00 USD | 0.00 USD | 1,460,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2177.90` | 363,170,000.00 USD | 363,170,000.00 USD | 1,320,000.00 USD | 783,680.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2179.50` | 405,620,000.00 USD | 405,620,000.00 USD | 2,400,000.00 USD | 133,210.00 USD | 4,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2180.40` | 357,710,000.00 USD | 357,710,000.00 USD | 6,480,000.00 USD | 5,550,000.00 USD | 7,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2182.30` | 398,930,000.00 USD | 398,930,000.00 USD | 1,760,000.00 USD | 2,160,000.00 USD | 2,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2182.90` | 338,090,000.00 USD | 338,090,000.00 USD | 1,610,000.00 USD | 2,190,000.00 USD | 3,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 694,330.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2185.10` | 392,250,000.00 USD | 392,250,000.00 USD | 41,350,000.00 USD | 20,450,000.00 USD | 3,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2185.40` | 331,180,000.00 USD | 331,180,000.00 USD | 3,730,000.00 USD | 3,250,000.00 USD | 7,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2187.90` | 316,810,000.00 USD | 316,810,000.00 USD | 7,340,000.00 USD | 4,050,000.00 USD | 7,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.90` | 327,380,000.00 USD | 327,380,000.00 USD | 2,370,000.00 USD | 0.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2190.40` | 297,430,000.00 USD | 297,430,000.00 USD | 6,760,000.00 USD | 4,660,000.00 USD | 4,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.70` | 323,280,000.00 USD | 323,280,000.00 USD | 12,430,000.00 USD | 27,960,000.00 USD | 6,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2192.90` | 281,880,000.00 USD | 281,880,000.00 USD | 6,130,000.00 USD | 5,130,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2193.50` | 276,460,000.00 USD | 276,460,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 2,250,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2195.40` | 269,110,000.00 USD | 269,110,000.00 USD | 6,060,000.00 USD | 2,840,000.00 USD | 5,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.30` | 261,010,000.00 USD | 261,010,000.00 USD | 566,810.00 USD | 243,760.00 USD | 109,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2197.90` | 254,580,000.00 USD | 254,580,000.00 USD | 7,200,000.00 USD | 4,560,000.00 USD | 4,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2199.10` | 260,090,000.00 USD | 260,090,000.00 USD | 4,100,000.00 USD | 5,270,000.00 USD | 7,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.40` | 237,870,000.00 USD | 237,870,000.00 USD | 12,020,000.00 USD | 7,180,000.00 USD | 10,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2201.90` | 243,270,000.00 USD | 243,270,000.00 USD | 12,880,000.00 USD | 2,690,000.00 USD | 21,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2202.90` | 208,150,000.00 USD | 208,150,000.00 USD | 16,520,000.00 USD | 16,290,000.00 USD | 19,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2204.70` | 205,980,000.00 USD | 205,980,000.00 USD | 5,350,000.00 USD | 4,330,000.00 USD | 4,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 449,420.00 USD | 455,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.40` | 155,680,000.00 USD | 155,680,000.00 USD | 10,040,000.00 USD | 3,290,000.00 USD | 4,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2207.50` | 191,640,000.00 USD | 191,640,000.00 USD | 19,630,000.00 USD | 3,390,000.00 USD | 7,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2207.90` | 138,350,000.00 USD | 138,350,000.00 USD | 14,640,000.00 USD | 8,140,000.00 USD | 5,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2210.30` | 161,430,000.00 USD | 161,430,000.00 USD | 4,740,000.00 USD | 0.00 USD | 11,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.40` | 109,800,000.00 USD | 109,800,000.00 USD | 6,870,000.00 USD | 7,030,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.90` | 90,670,000.00 USD | 90,670,000.00 USD | 8,240,000.00 USD | 5,160,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2213.10` | 145,120,000.00 USD | 145,120,000.00 USD | 1,710,000.00 USD | 1,980,000.00 USD | 8,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 6,540.00 USD | 6,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2215.40` | 75,240,000.00 USD | 75,240,000.00 USD | 2,150,000.00 USD | 3,720,000.00 USD | 878,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2215.90` | 132,580,000.00 USD | 132,580,000.00 USD | 0.00 USD | 0.00 USD | 565,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2217.90` | 68,490,000.00 USD | 68,490,000.00 USD | 5,090,000.00 USD | 3,410,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2218.70` | 132,020,000.00 USD | 132,020,000.00 USD | 22,760,000.00 USD | 487,520.00 USD | 218,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2220.40` | 56,700,000.00 USD | 56,700,000.00 USD | 9,840,000.00 USD | 6,700,000.00 USD | 4,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2221.50` | 108,550,000.00 USD | 108,550,000.00 USD | 8,210,000.00 USD | 19,850,000.00 USD | 18,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2222.90` | 36,090,000.00 USD | 36,090,000.00 USD | 5,350,000.00 USD | 6,360,000.00 USD | 883,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2224.30` | 61,620,000.00 USD | 61,620,000.00 USD | 7,550,000.00 USD | 4,850,000.00 USD | 6,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2225.00` | 1,890.00 USD | 1,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2225.40` | 23,500,000.00 USD | 23,500,000.00 USD | 3,470,000.00 USD | 2,560,000.00 USD | 3,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2227.10` | 42,690,000.00 USD | 42,690,000.00 USD | 557,870.00 USD | 0.00 USD | 6,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.90` | 14,200,000.00 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 111,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.90` | 35,270,000.00 USD | 35,270,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.40` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 113,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2232.90` | 13,970,000.00 USD | 13,970,000.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2235.50` | 33,370,000.00 USD | 33,370,000.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2237.90` | 8,020,000.00 USD | 8,020,000.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2238.30` | 8,470,000.00 USD | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2240.40` | 21,970.00 USD | 21,970.00 USD | 0.00 USD | 0.00 USD | 21,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2242.90` | 22,480.00 USD | 22,480.00 USD | 0.00 USD | 0.00 USD | 22,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2243.90` | 268,650.00 USD | 268,650.00 USD | 0.00 USD | 268,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2245.00` | 2,570.00 USD | 4,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2245.40` | 84,720.00 USD | 84,720.00 USD | 0.00 USD | 0.00 USD | 62,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2246.70` | 3,480,000.00 USD | 3,480,000.00 USD | 1,210,000.00 USD | 1,300,000.00 USD | 709,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2247.90` | 828,620.00 USD | 828,620.00 USD | 158,150.00 USD | 286,090.00 USD | 299,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2249.50` | 9,970,000.00 USD | 9,970,000.00 USD | 2,960,000.00 USD | 2,660,000.00 USD | 867,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2250.40` | 10,940,000.00 USD | 10,940,000.00 USD | 7,970,000.00 USD | 458,980.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2252.30` | 35,240,000.00 USD | 35,240,000.00 USD | 10,050,000.00 USD | 11,670,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2252.90` | 19,050,000.00 USD | 19,050,000.00 USD | 1,390,000.00 USD | 3,240,000.00 USD | 3,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 20,070.00 USD | 24,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2255.10` | 52,660,000.00 USD | 52,660,000.00 USD | 10,050,000.00 USD | 6,600,000.00 USD | 774,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2255.40` | 47,360,000.00 USD | 47,360,000.00 USD | 15,660,000.00 USD | 6,830,000.00 USD | 5,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2257.90` | 82,170,000.00 USD | 82,170,000.00 USD | 19,650,000.00 USD | 9,290,000.00 USD | 5,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2257.90` | 92,360,000.00 USD | 92,360,000.00 USD | 20,510,000.00 USD | 12,290,000.00 USD | 6,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2260.40` | 102,520,000.00 USD | 102,520,000.00 USD | 8,330,000.00 USD | 9,340,000.00 USD | 2,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2260.70` | 96,680,000.00 USD | 96,680,000.00 USD | 0.00 USD | 0.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2262.90` | 138,380,000.00 USD | 138,380,000.00 USD | 18,250,000.00 USD | 11,340,000.00 USD | 6,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2263.50` | 105,440,000.00 USD | 105,440,000.00 USD | 7,080,000.00 USD | 1,460,000.00 USD | 218,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 93,510.00 USD | 118,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2265.40` | 172,930,000.00 USD | 172,930,000.00 USD | 8,910,000.00 USD | 12,680,000.00 USD | 12,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2266.30` | 135,770,000.00 USD | 135,770,000.00 USD | 8,210,000.00 USD | 15,790,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2267.90` | 225,940,000.00 USD | 225,940,000.00 USD | 24,280,000.00 USD | 15,840,000.00 USD | 12,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2269.10` | 183,640,000.00 USD | 183,640,000.00 USD | 18,560,000.00 USD | 4,980,000.00 USD | 24,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2270.40` | 273,190,000.00 USD | 273,190,000.00 USD | 14,990,000.00 USD | 12,470,000.00 USD | 19,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2271.90` | 212,540,000.00 USD | 212,540,000.00 USD | 18,240,000.00 USD | 3,640,000.00 USD | 7,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2272.90` | 300,520,000.00 USD | 300,520,000.00 USD | 16,290,000.00 USD | 4,810,000.00 USD | 6,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2274.70` | 240,840,000.00 USD | 240,840,000.00 USD | 19,630,000.00 USD | 6,900,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 828,610.00 USD | 946,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2275.40` | 354,760,000.00 USD | 354,760,000.00 USD | 30,720,000.00 USD | 18,900,000.00 USD | 4,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2277.50` | 267,230,000.00 USD | 267,230,000.00 USD | 6,890,000.00 USD | 8,890,000.00 USD | 10,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2277.90` | 387,640,000.00 USD | 387,640,000.00 USD | 6,870,000.00 USD | 10,770,000.00 USD | 15,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2280.30` | 311,550,000.00 USD | 311,550,000.00 USD | 854,200.00 USD | 39,830,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2280.40` | 443,160,000.00 USD | 443,160,000.00 USD | 31,180,000.00 USD | 15,520,000.00 USD | 8,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2282.90` | 501,680,000.00 USD | 501,680,000.00 USD | 27,530,000.00 USD | 21,080,000.00 USD | 9,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2283.10` | 403,360,000.00 USD | 403,360,000.00 USD | 5,600,000.00 USD | 72,520,000.00 USD | 13,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 490,730.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2285.40` | 524,400,000.00 USD | 524,400,000.00 USD | 8,500,000.00 USD | 9,370,000.00 USD | 4,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2285.90` | 407,250,000.00 USD | 407,250,000.00 USD | 1,190,000.00 USD | 2,590,000.00 USD | 109,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2287.90` | 557,680,000.00 USD | 557,680,000.00 USD | 14,760,000.00 USD | 9,890,000.00 USD | 8,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2288.70` | 447,800,000.00 USD | 447,800,000.00 USD | 12,490,000.00 USD | 13,140,000.00 USD | 14,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2290.40` | 603,580,000.00 USD | 603,580,000.00 USD | 20,500,000.00 USD | 16,540,000.00 USD | 8,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2291.50` | 468,970,000.00 USD | 468,970,000.00 USD | 8,080,000.00 USD | 2,940,000.00 USD | 10,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2292.90` | 633,960,000.00 USD | 633,960,000.00 USD | 14,730,000.00 USD | 6,010,000.00 USD | 9,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2294.30` | 490,300,000.00 USD | 490,300,000.00 USD | 14,670,000.00 USD | 1,490,000.00 USD | 5,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 2,920,000.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2295.40` | 666,300,000.00 USD | 666,300,000.00 USD | 11,190,000.00 USD | 13,180,000.00 USD | 7,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2297.10` | 540,050,000.00 USD | 540,050,000.00 USD | 25,900,000.00 USD | 8,070,000.00 USD | 15,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2297.90` | 715,530,000.00 USD | 715,530,000.00 USD | 30,590,000.00 USD | 12,660,000.00 USD | 5,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.90` | 582,970,000.00 USD | 582,970,000.00 USD | 16,200,000.00 USD | 20,940,000.00 USD | 5,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2300.40` | 756,080,000.00 USD | 756,080,000.00 USD | 12,140,000.00 USD | 13,230,000.00 USD | 15,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.70` | 637,640,000.00 USD | 637,640,000.00 USD | 26,960,000.00 USD | 10,860,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.90` | 782,960,000.00 USD | 782,960,000.00 USD | 16,590,000.00 USD | 3,050,000.00 USD | 7,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 448,140.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.40` | 820,930,000.00 USD | 820,930,000.00 USD | 12,570,000.00 USD | 18,050,000.00 USD | 7,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.50` | 663,650,000.00 USD | 663,650,000.00 USD | 6,340,000.00 USD | 8,820,000.00 USD | 10,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2307.90` | 830,210,000.00 USD | 830,210,000.00 USD | 4,390,000.00 USD | 2,880,000.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2308.30` | 665,950,000.00 USD | 665,950,000.00 USD | 1,240,000.00 USD | 930,630.00 USD | 134,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2310.40` | 849,590,000.00 USD | 849,590,000.00 USD | 5,980,000.00 USD | 2,740,000.00 USD | 10,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2311.10` | 696,450,000.00 USD | 696,450,000.00 USD | 11,560,000.00 USD | 2,790,000.00 USD | 16,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2312.90` | 866,610,000.00 USD | 866,610,000.00 USD | 6,580,000.00 USD | 8,640,000.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2313.90` | 707,270,000.00 USD | 707,270,000.00 USD | 1,100,000.00 USD | 7,460,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 824,210.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2315.40` | 893,480,000.00 USD | 893,480,000.00 USD | 6,000,000.00 USD | 12,910,000.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2316.70` | 713,030,000.00 USD | 713,030,000.00 USD | 1,020,000.00 USD | 3,640,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2317.90` | 916,370,000.00 USD | 916,370,000.00 USD | 7,580,000.00 USD | 11,210,000.00 USD | 4,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.50` | 743,190,000.00 USD | 743,190,000.00 USD | 5,530,000.00 USD | 15,850,000.00 USD | 8,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.40` | 941,600,000.00 USD | 941,600,000.00 USD | 10,170,000.00 USD | 11,790,000.00 USD | 3,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.30` | 749,110,000.00 USD | 749,110,000.00 USD | 2,300,000.00 USD | 3,450,000.00 USD | 172,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2322.90` | 959,930,000.00 USD | 959,930,000.00 USD | 4,360,000.00 USD | 9,300,000.00 USD | 4,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 3,250,000.00 USD | 8,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.10` | 772,140,000.00 USD | 772,140,000.00 USD | 10,150,000.00 USD | 2,770,000.00 USD | 10,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2325.40` | 973,050,000.00 USD | 973,050,000.00 USD | 2,050,000.00 USD | 9,550,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2327.90` | 979,360,000.00 USD | 979,360,000.00 USD | 494,310.00 USD | 1,240,000.00 USD | 4,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2327.90` | 784,030,000.00 USD | 784,030,000.00 USD | 3,860,000.00 USD | 0.00 USD | 8,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2330.40` | 997,900,000.00 USD | 997,900,000.00 USD | 13,500,000.00 USD | 3,350,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2330.70` | 800,350,000.00 USD | 800,350,000.00 USD | 15,890,000.00 USD | 363,770.00 USD | 54,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2332.90` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 4,140,000.00 USD | 4,150,000.00 USD | 9,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2333.50` | 845,400,000.00 USD | 845,400,000.00 USD | 22,320,000.00 USD | 14,770,000.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 437,940.00 USD | 9,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2335.40` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 13,620,000.00 USD | 5,030,000.00 USD | 5,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2336.30` | 887,300,000.00 USD | 887,300,000.00 USD | 26,200,000.00 USD | 8,780,000.00 USD | 6,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2337.90` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 8,210,000.00 USD | 1,950,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2339.10` | 913,700,000.00 USD | 913,700,000.00 USD | 14,040,000.00 USD | 0.00 USD | 12,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2340.40` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 10,960,000.00 USD | 6,230,000.00 USD | 12,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2341.90` | 954,130,000.00 USD | 954,130,000.00 USD | 8,610,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2342.90` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 9,530,000.00 USD | 6,510,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2344.70` | 982,050,000.00 USD | 982,050,000.00 USD | 2,480,000.00 USD | 16,920,000.00 USD | 8,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 415,460.00 USD | 9,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2345.40` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 4,570,000.00 USD | 5,870,000.00 USD | 9,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2347.50` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 8,220,000.00 USD | 18,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2347.90` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 3,940,000.00 USD | 3,280,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2350.30` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 1,630,000.00 USD | 20,110,000.00 USD | 15,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.40` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 26,860,000.00 USD | 7,910,000.00 USD | 10,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2352.90` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 3,960,000.00 USD | 2,870,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2353.10` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 2,710,000.00 USD | 35,770,000.00 USD | 4,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 2,440,000.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2355.40` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 3,190,000.00 USD | 3,280,000.00 USD | 951,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2355.90` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 18,560,000.00 USD | 10,720,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.90` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 3,680,000.00 USD | 4,660,000.00 USD | 3,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.70` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 6,870,000.00 USD | 512,220.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 10,760,000.00 USD | 3,880,000.00 USD | 5,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.50` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 3,150,000.00 USD | 3,430,000.00 USD | 374,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.90` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 6,270,000.00 USD | 9,060,000.00 USD | 7,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2364.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 3,860,000.00 USD | 373,740.00 USD | 10,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 4,860,000.00 USD | 17,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2365.40` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 4,890,000.00 USD | 658,050.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2367.10` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 307,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.90` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 2,980,000.00 USD | 3,580,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2369.90` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 24,940,000.00 USD | 475,460.00 USD | 18,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.40` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 14,770,000.00 USD | 5,230,000.00 USD | 5,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2372.70` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 15,600,000.00 USD | 0.00 USD | 39,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.90` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 11,560,000.00 USD | 2,680,000.00 USD | 6,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 893,040.00 USD | 17,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2375.40` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 8,180,000.00 USD | 1,830,000.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2375.50` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 9,700,000.00 USD | 1,050,000.00 USD | 11,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2377.90` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 1,460,000.00 USD | 1,920,000.00 USD | 3,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.30` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 11,180,000.00 USD | 7,020,000.00 USD | 23,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.40` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 6,310,000.00 USD | 5,360,000.00 USD | 5,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.10` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 4,540,000.00 USD | 2,390,000.00 USD | 16,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2382.90` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 15,730,000.00 USD | 10,890,000.00 USD | 11,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2383.90` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 8,840,000.00 USD | 21,750,000.00 USD | 30,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 722,850.00 USD | 18,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.40` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 7,510,000.00 USD | 10,280,000.00 USD | 4,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2386.70` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 17,720,000.00 USD | 32,140,000.00 USD | 42,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2387.90` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 9,900,000.00 USD | 5,870,000.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2389.50` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 5,670,000.00 USD | 35,860,000.00 USD | 28,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.40` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 4,300,000.00 USD | 3,360,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2392.30` | 1,690,000,000.00 USD | 1,690,000,000.00 USD | 26,840,000.00 USD | 45,530,000.00 USD | 39,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.90` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 2,700,000.00 USD | 3,990,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,850,000.00 USD | 23,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2395.10` | 1,780,000,000.00 USD | 1,780,000,000.00 USD | 39,180,000.00 USD | 24,870,000.00 USD | 29,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2395.40` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 2,060,000.00 USD | 1,450,000.00 USD | 2,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2397.90` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 64,150.00 USD | 3,720,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2397.90` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 34,290,000.00 USD | 36,430,000.00 USD | 23,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2400.40` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 2,150,000.00 USD | 637,690.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2400.70` | 1,960,000,000.00 USD | 1,960,000,000.00 USD | 42,030,000.00 USD | 25,390,000.00 USD | 24,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2402.90` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 1,140,000.00 USD | 467,060.00 USD | 552,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2403.50` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 51,300,000.00 USD | 24,760,000.00 USD | 30,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 115,180.00 USD | 23,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2405.40` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 6,760,000.00 USD | 3,300,000.00 USD | 5,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2406.30` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 29,700,000.00 USD | 33,710,000.00 USD | 14,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2407.90` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 6,010,000.00 USD | 3,490,000.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2409.10` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 25,090,000.00 USD | 21,480,000.00 USD | 27,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.40` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 4,520,000.00 USD | 3,650,000.00 USD | 3,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.90` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 15,970,000.00 USD | 21,640,000.00 USD | 13,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2412.90` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 4,850,000.00 USD | 2,870,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.70` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 22,250,000.00 USD | 19,630,000.00 USD | 21,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 236,460.00 USD | 23,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.40` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 3,020,000.00 USD | 2,080,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2417.50` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 22,310,000.00 USD | 8,700,000.00 USD | 21,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2417.90` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 2,330,000.00 USD | 1,820,000.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2420.30` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 29,980,000.00 USD | 18,780,000.00 USD | 9,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2420.40` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 6,230,000.00 USD | 2,900,000.00 USD | 4,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.90` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 1,070,000.00 USD | 2,790,000.00 USD | 3,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2423.10` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 17,920,000.00 USD | 17,260,000.00 USD | 17,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 289,470.00 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.40` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 1,280,000.00 USD | 623,850.00 USD | 621,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2425.90` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 12,980,000.00 USD | 15,010,000.00 USD | 17,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2427.90` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 1,610,000.00 USD | 1,520,000.00 USD | 609,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2428.70` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 12,800,000.00 USD | 7,090,000.00 USD | 8,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.40` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 1,330,000.00 USD | 1,550,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.50` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 9,420,000.00 USD | 12,660,000.00 USD | 8,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.90` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 2,680,000.00 USD | 2,230,000.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.30` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 8,200,000.00 USD | 3,830,000.00 USD | 3,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 197,400.00 USD | 24,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.40` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 2,480,000.00 USD | 572,900.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.10` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 7,130,000.00 USD | 7,440,000.00 USD | 6,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2437.90` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 1,380,000.00 USD | 1,040,000.00 USD | 15,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2439.90` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 12,730,000.00 USD | 4,970,000.00 USD | 3,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.40` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 1,230,000.00 USD | 1,190,000.00 USD | 863,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2442.70` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 5,050,000.00 USD | 5,320,000.00 USD | 7,900,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2442.90` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 1,040,000.00 USD | 42,810.00 USD | 751,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 4,800,000.00 USD | 29,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.40` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 218,020.00 USD | 703,990.00 USD | 755,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2445.50` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 9,990,000.00 USD | 7,470,000.00 USD | 10,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2447.90` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 1,210,000.00 USD | 989,540.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2448.30` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 10,750,000.00 USD | 3,620,000.00 USD | 13,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.40` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 1,990,000.00 USD | 73,380.00 USD | 35,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.10` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 8,450,000.00 USD | 7,240,000.00 USD | 7,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2452.90` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 2,460,000.00 USD | 1,840,000.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2453.90` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 4,220,000.00 USD | 2,980,000.00 USD | 3,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 214,400.00 USD | 29,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.40` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 1,640,000.00 USD | 2,130,000.00 USD | 916,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2456.70` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 5,900,000.00 USD | 7,380,000.00 USD | 7,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2457.90` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 1,770,000.00 USD | 1,840,000.00 USD | 845,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2459.50` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 3,220,000.00 USD | 4,870,000.00 USD | 6,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2460.40` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 1,560,000.00 USD | 1,410,000.00 USD | 388,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2462.30` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 6,600,000.00 USD | 5,990,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2462.90` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 330,880.00 USD | 618,870.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 11,550,000.00 USD | 40,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2465.10` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 4,900,000.00 USD | 3,130,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2465.40` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 1,090,000.00 USD | 1,030,000.00 USD | 345,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2467.90` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 732,440.00 USD | 1,550,000.00 USD | 377,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.90` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 3,720,000.00 USD | 2,330,000.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.40` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 1,650,000.00 USD | 1,590,000.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.70` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 4,710,000.00 USD | 2,530,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2472.90` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 219,870.00 USD | 92,950.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2473.50` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 5,300,000.00 USD | 2,920,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 54,770,000.00 USD | 95,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2475.40` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 339,190.00 USD | 1,100,000.00 USD | 103,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2476.30` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 232,420.00 USD | 0.00 USD | 156,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2476.30` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 2,070,000.00 USD | 1,710,000.00 USD | 872,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2479.10` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 3,070,000.00 USD | 4,130,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2481.90` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 601,420.00 USD | 3,680,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.70` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 1,650,000.00 USD | 97,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2487.50` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.30` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 338,890.00 USD | 286,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2491.80` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 2,580,000.00 USD | 733,870.00 USD | 445,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 2,150,000.00 USD | 99,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2505.00` | 4,470,000.00 USD | 103,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2515.00` | 1,590,000.00 USD | 105,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2525.00` | 46,400.00 USD | 105,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2535.00` | 1,060,000.00 USD | 106,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2545.00` | 5,040,000.00 USD | 111,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2555.00` | 238,660.00 USD | 111,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2565.00` | 89,050.00 USD | 112,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2575.00` | 559,600.00 USD | 112,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2585.00` | 34,310,000.00 USD | 146,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2595.00` | 359,640.00 USD | 147,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2605.00` | 5,810,000.00 USD | 153,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2615.00` | 732,830.00 USD | 153,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2625.00` | 45,410,000.00 USD | 199,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2635.00` | 1,030,000.00 USD | 200,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 626,810.00 USD | 200,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 26,820,000.00 USD | 227,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 51,540.00 USD | 227,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 1,100,000.00 USD | 228,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 23,200.00 USD | 228,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 468,980.00 USD | 229,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 698,920.00 USD | 230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 413,400.00 USD | 230,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 229,610.00 USD | 230,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 5,150,000.00 USD | 235,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 13,790,000.00 USD | 249,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 5,050,000.00 USD | 254,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 416,000.00 USD | 255,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 25,170,000.00 USD | 280,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 528,660.00 USD | 280,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 5,560,000.00 USD | 286,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 5,930,000.00 USD | 292,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 2,010,000.00 USD | 294,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 133,850.00 USD | 294,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 6,280,000.00 USD | 300,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 349,690.00 USD | 301,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 502,140.00 USD | 301,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 422,840.00 USD | 301,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 64,240.00 USD | 302,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 1,740,000.00 USD | 303,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 1,340,000.00 USD | 305,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 44,390,000.00 USD | 349,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 2,350,000.00 USD | 351,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 3,030,000.00 USD | 354,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 67,460.00 USD | 354,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 437,030.00 USD | 355,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 4,570,000.00 USD | 359,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 590,570.00 USD | 360,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 3,360,000.00 USD | 363,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 1,240,000.00 USD | 365,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 15,030,000.00 USD | 380,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 646,430.00 USD | 380,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 175,020.00 USD | 380,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 862,710.00 USD | 381,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 15,030,000.00 USD | 396,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 715,260.00 USD | 397,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 6,520.00 USD | 397,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 1,510,000.00 USD | 399,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 6,070,000.00 USD | 405,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 10,930,000.00 USD | 416,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 5,780,000.00 USD | 421,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 12,290,000.00 USD | 434,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 33,880,000.00 USD | 468,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 1,870,000.00 USD | 469,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 261,240.00 USD | 470,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 401,090.00 USD | 470,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 222,300.00 USD | 470,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 130,620.00 USD | 470,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 1,090,000.00 USD | 472,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 70,660,000.00 USD | 542,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 210,270.00 USD | 542,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 352,030.00 USD | 543,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 175,220.00 USD | 543,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 8,340,000.00 USD | 551,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 9,760,000.00 USD | 561,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 4,850,000.00 USD | 566,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 12,810.00 USD | 566,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 65,860.00 USD | 566,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 10,830,000.00 USD | 577,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 65,540.00 USD | 577,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 334,070.00 USD | 577,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 1,270,000.00 USD | 578,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 2,120,000.00 USD | 581,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 75,050.00 USD | 581,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 1,480,000.00 USD | 582,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 58,000.00 USD | 582,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 2,050,000.00 USD | 584,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 2,970,000.00 USD | 587,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 2,430,000.00 USD | 590,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 102,540.00 USD | 590,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 93,920.00 USD | 590,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 1,270,000.00 USD | 591,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 4,200,000.00 USD | 595,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 14,590,000.00 USD | 610,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 95,600.00 USD | 610,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 881,390.00 USD | 611,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 559,510.00 USD | 611,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 424,610.00 USD | 612,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 55,090.00 USD | 612,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 30,100.00 USD | 612,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 1,170,000.00 USD | 613,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 1,640,000.00 USD | 615,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 375,650.00 USD | 615,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 765,100.00 USD | 616,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 14,830,000.00 USD | 631,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 97,280.00 USD | 631,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 119,970.00 USD | 631,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 125,810.00 USD | 631,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 80,980.00 USD | 631,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 749,130.00 USD | 632,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 43,700.00 USD | 632,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 62,790.00 USD | 632,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 3,790,000.00 USD | 636,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 1,120,000.00 USD | 637,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 8,820,000.00 USD | 646,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 53,550,000.00 USD | 699,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 37,050.00 USD | 699,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 343,720.00 USD | 700,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 6,540,000.00 USD | 706,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 212,010.00 USD | 706,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 31,030.00 USD | 706,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 3,860,000.00 USD | 710,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 2,920.00 USD | 710,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 382,870,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 360,220.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 2,710,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 163,780.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 78,340.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 456,790.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 59,410,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 3,470,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 4,850,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 1,590.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 34,550.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 280,720.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 212,940.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 1,050,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 2,480,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3875.00` | 93,260.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 1,360,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 2,490,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 38,870,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 553,260.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 152,270.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 2,640.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 88,480.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 1,660.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 30,880.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 160,630.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 178,550.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 562,130.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 141,730.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 1,230,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 490,570.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 414,520.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 121,110.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 1,690,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 1,200,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 129,220.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 91,390.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 207,480.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 1,150,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 129,580.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 151,430.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 608,480.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 99,240.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 681,920.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 132,850.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 209,470.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 948,630.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 32,730,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 42,140.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 42,320.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4225.00` | 801,540.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 83,560,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 335,020.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 420.39 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 2,170,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 4,060.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 2,450.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 15,180.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 17,120.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 50,390.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 36,530.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 32,800.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 204,690.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 6,930.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 1,140,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 19,130.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 4,180.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 615,700.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 23,210.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 129,550.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 8,230.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4435.00` | 73,170.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4445.00` | 25,610.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `455.00` | 786,690,000.00 USD | 0.00 USD | 121,330.00 USD | `-79.54%` | `266.65` |
| `Live` | `Long` | `465.00` | 786,570,000.00 USD | 0.00 USD | 118,030.00 USD | `-79.09%` | `253.83` |
| `Live` | `Long` | `475.00` | 786,450,000.00 USD | 0.00 USD | 81,110.00 USD | `-78.64%` | `170.75` |
| `Live` | `Long` | `485.00` | 786,370,000.00 USD | 0.00 USD | 2,960.00 USD | `-78.20%` | `6.10` |
| `Live` | `Long` | `495.00` | 786,370,000.00 USD | 0.00 USD | 140,880.00 USD | `-77.75%` | `284.60` |
| `Live` | `Long` | `505.00` | 786,230,000.00 USD | 0.00 USD | 67,370.00 USD | `-77.30%` | `133.41` |
| `Live` | `Long` | `515.00` | 786,160,000.00 USD | 0.00 USD | 39,200.00 USD | `-76.85%` | `76.11` |
| `Live` | `Long` | `525.00` | 786,120,000.00 USD | 0.00 USD | 1,870,000.00 USD | `-76.40%` | `3,559.73` |
| `Live` | `Long` | `535.00` | 784,250,000.00 USD | 0.00 USD | 34,560.00 USD | `-75.95%` | `64.60` |
| `Live` | `Long` | `545.00` | 784,220,000.00 USD | 0.00 USD | 53,010.00 USD | `-75.50%` | `97.27` |
| `Live` | `Long` | `555.00` | 784,160,000.00 USD | 0.00 USD | 66,580.00 USD | `-75.05%` | `119.97` |
| `Live` | `Long` | `565.00` | 784,100,000.00 USD | 0.00 USD | 158,160.00 USD | `-74.60%` | `279.93` |
| `Live` | `Long` | `575.00` | 783,940,000.00 USD | 0.00 USD | 64,830.00 USD | `-74.15%` | `112.75` |
| `Live` | `Long` | `585.00` | 783,870,000.00 USD | 0.00 USD | 44,160.00 USD | `-73.70%` | `75.49` |
| `Live` | `Long` | `595.00` | 783,830,000.00 USD | 0.00 USD | 3,330,000.00 USD | `-73.25%` | `5,604.18` |
| `Live` | `Long` | `605.00` | 780,490,000.00 USD | 0.00 USD | 154,720.00 USD | `-72.80%` | `255.73` |
| `Live` | `Long` | `615.00` | 780,340,000.00 USD | 0.00 USD | 142,040.00 USD | `-72.35%` | `230.97` |
| `Live` | `Long` | `625.00` | 780,200,000.00 USD | 0.00 USD | 1,880,000.00 USD | `-71.90%` | `3,012.16` |
| `Live` | `Long` | `635.00` | 778,310,000.00 USD | 0.00 USD | 51,410.00 USD | `-71.45%` | `80.96` |
| `Live` | `Long` | `645.00` | 778,260,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-71.00%` | `1,776.04` |
| `Live` | `Long` | `655.00` | 777,120,000.00 USD | 0.00 USD | 46,320.00 USD | `-70.55%` | `70.72` |
| `Live` | `Long` | `665.00` | 777,070,000.00 USD | 0.00 USD | 54,620.00 USD | `-70.10%` | `82.13` |
| `Live` | `Long` | `675.00` | 777,020,000.00 USD | 0.00 USD | 46,090.00 USD | `-69.65%` | `68.28` |
| `Live` | `Long` | `685.00` | 776,970,000.00 USD | 0.00 USD | 44,110.00 USD | `-69.20%` | `64.39` |
| `Live` | `Long` | `695.00` | 776,930,000.00 USD | 0.00 USD | 2,640.00 USD | `-68.75%` | `3.80` |
| `Live` | `Long` | `705.00` | 776,920,000.00 USD | 0.00 USD | 15,790.00 USD | `-68.30%` | `22.40` |
| `Live` | `Long` | `715.00` | 776,910,000.00 USD | 0.00 USD | 54,550.00 USD | `-67.86%` | `76.30` |
| `Live` | `Long` | `725.00` | 776,850,000.00 USD | 0.00 USD | 1,080,000.00 USD | `-67.41%` | `1,484.42` |
| `Live` | `Long` | `735.00` | 775,780,000.00 USD | 0.00 USD | 78,630.00 USD | `-66.96%` | `106.98` |
| `Live` | `Long` | `745.00` | 775,700,000.00 USD | 0.00 USD | 9,220.00 USD | `-66.51%` | `12.38` |
| `Live` | `Long` | `755.00` | 775,690,000.00 USD | 0.00 USD | 55,210.00 USD | `-66.06%` | `73.12` |
| `Live` | `Long` | `765.00` | 775,630,000.00 USD | 0.00 USD | 5,250.00 USD | `-65.61%` | `6.87` |
| `Live` | `Long` | `775.00` | 775,630,000.00 USD | 0.00 USD | 72,970.00 USD | `-65.16%` | `94.15` |
| `Live` | `Long` | `785.00` | 775,560,000.00 USD | 0.00 USD | 16,550.00 USD | `-64.71%` | `21.08` |
| `Live` | `Long` | `795.00` | 775,540,000.00 USD | 0.00 USD | 6,010.00 USD | `-64.26%` | `7.56` |
| `Live` | `Long` | `805.00` | 775,530,000.00 USD | 0.00 USD | 85,220.00 USD | `-63.81%` | `105.86` |
| `Live` | `Long` | `815.00` | 775,450,000.00 USD | 0.00 USD | 95,130.00 USD | `-63.36%` | `116.72` |
| `Live` | `Long` | `825.00` | 775,350,000.00 USD | 0.00 USD | 129,310.00 USD | `-62.91%` | `156.74` |
| `Live` | `Long` | `835.00` | 775,220,000.00 USD | 0.00 USD | 62,560.00 USD | `-62.46%` | `74.92` |
| `Live` | `Long` | `845.00` | 775,160,000.00 USD | 0.00 USD | 375,830.00 USD | `-62.01%` | `444.77` |
| `Live` | `Long` | `855.00` | 774,790,000.00 USD | 0.00 USD | 214,080.00 USD | `-61.56%` | `250.39` |
| `Live` | `Long` | `865.00` | 774,570,000.00 USD | 0.00 USD | 17,290.00 USD | `-61.11%` | `19.99` |
| `Live` | `Long` | `875.00` | 774,550,000.00 USD | 0.00 USD | 88,960.00 USD | `-60.66%` | `101.67` |
| `Live` | `Long` | `885.00` | 774,470,000.00 USD | 0.00 USD | 964,270.00 USD | `-60.21%` | `1,089.58` |
| `Live` | `Long` | `895.00` | 773,500,000.00 USD | 0.00 USD | 175,070.00 USD | `-59.76%` | `195.60` |
| `Live` | `Long` | `905.00` | 773,330,000.00 USD | 0.00 USD | 18,280.00 USD | `-59.31%` | `20.20` |
| `Live` | `Long` | `915.00` | 773,310,000.00 USD | 0.00 USD | 605,510.00 USD | `-58.86%` | `661.76` |
| `Live` | `Long` | `925.00` | 772,700,000.00 USD | 0.00 USD | 164,030.00 USD | `-58.41%` | `177.33` |
| `Live` | `Long` | `935.00` | 772,540,000.00 USD | 0.00 USD | 297,070.00 USD | `-57.96%` | `317.72` |
| `Live` | `Long` | `945.00` | 772,240,000.00 USD | 0.00 USD | 91,310.00 USD | `-57.51%` | `96.63` |
| `Live` | `Long` | `955.00` | 772,150,000.00 USD | 0.00 USD | 294,230.00 USD | `-57.07%` | `308.09` |
| `Live` | `Long` | `965.00` | 771,860,000.00 USD | 0.00 USD | 47,900.00 USD | `-56.62%` | `49.64` |
| `Live` | `Long` | `975.00` | 771,810,000.00 USD | 0.00 USD | 183,680.00 USD | `-56.17%` | `188.39` |
| `Live` | `Long` | `985.00` | 771,620,000.00 USD | 0.00 USD | 105,940.00 USD | `-55.72%` | `107.55` |
| `Live` | `Long` | `995.00` | 771,520,000.00 USD | 0.00 USD | 336,130.00 USD | `-55.27%` | `337.82` |
| `Live` | `Long` | `1005.00` | 771,180,000.00 USD | 0.00 USD | 113,820.00 USD | `-54.82%` | `113.26` |
| `Live` | `Long` | `1015.00` | 771,070,000.00 USD | 0.00 USD | 155,360.00 USD | `-54.37%` | `153.07` |
| `Live` | `Long` | `1025.00` | 770,910,000.00 USD | 0.00 USD | 63,130.00 USD | `-53.92%` | `61.59` |
| `Live` | `Long` | `1035.00` | 770,850,000.00 USD | 0.00 USD | 60,140.00 USD | `-53.47%` | `58.10` |
| `Live` | `Long` | `1045.00` | 770,790,000.00 USD | 0.00 USD | 702,780.00 USD | `-53.02%` | `672.51` |
| `Live` | `Long` | `1055.00` | 770,090,000.00 USD | 0.00 USD | 7,410,000.00 USD | `-52.57%` | `7,023.20` |
| `Live` | `Long` | `1065.00` | 762,680,000.00 USD | 0.00 USD | 557,690.00 USD | `-52.12%` | `523.66` |
| `Live` | `Long` | `1075.00` | 762,120,000.00 USD | 0.00 USD | 721,980.00 USD | `-51.67%` | `671.61` |
| `Live` | `Long` | `1085.00` | 761,400,000.00 USD | 0.00 USD | 1,890,000.00 USD | `-51.22%` | `1,741.70` |
| `Live` | `Long` | `1095.00` | 759,510,000.00 USD | 0.00 USD | 676,930.00 USD | `-50.77%` | `618.20` |
| `Live` | `Long` | `1105.00` | 758,830,000.00 USD | 0.00 USD | 217,450.00 USD | `-50.32%` | `196.79` |
| `Live` | `Long` | `1115.00` | 758,610,000.00 USD | 0.00 USD | 206,920.00 USD | `-49.87%` | `185.58` |
| `Live` | `Long` | `1125.00` | 758,410,000.00 USD | 0.00 USD | 7,930,000.00 USD | `-49.42%` | `7,046.35` |
| `Live` | `Long` | `1135.00` | 750,480,000.00 USD | 0.00 USD | 86,940.00 USD | `-48.97%` | `76.60` |
| `Live` | `Long` | `1145.00` | 750,390,000.00 USD | 0.00 USD | 850,610.00 USD | `-48.52%` | `742.89` |
| `Live` | `Long` | `1155.00` | 749,540,000.00 USD | 0.00 USD | 599,140.00 USD | `-48.07%` | `518.73` |
| `Live` | `Long` | `1165.00` | 748,940,000.00 USD | 0.00 USD | 1,630,000.00 USD | `-47.62%` | `1,395.42` |
| `Live` | `Long` | `1175.00` | 747,320,000.00 USD | 0.00 USD | 261,700.00 USD | `-47.17%` | `222.73` |
| `Live` | `Long` | `1185.00` | 747,060,000.00 USD | 0.00 USD | 2,670,000.00 USD | `-46.72%` | `2,251.69` |
| `Live` | `Long` | `1195.00` | 744,390,000.00 USD | 0.00 USD | 330,450.00 USD | `-46.28%` | `276.53` |
| `Live` | `Long` | `1205.00` | 744,060,000.00 USD | 0.00 USD | 7,250,000.00 USD | `-45.83%` | `6,014.73` |
| `Live` | `Long` | `1215.00` | 736,810,000.00 USD | 0.00 USD | 80,960.00 USD | `-45.38%` | `66.64` |
| `Live` | `Long` | `1225.00` | 736,730,000.00 USD | 0.00 USD | 405,620.00 USD | `-44.93%` | `331.12` |
| `Live` | `Long` | `1235.00` | 736,320,000.00 USD | 0.00 USD | 116,280.00 USD | `-44.48%` | `94.15` |
| `Live` | `Long` | `1245.00` | 736,210,000.00 USD | 0.00 USD | 53,980.00 USD | `-44.03%` | `43.36` |
| `Live` | `Long` | `1255.00` | 736,150,000.00 USD | 0.00 USD | 1,200,000.00 USD | `-43.58%` | `952.40` |
| `Live` | `Long` | `1265.00` | 734,960,000.00 USD | 0.00 USD | 2,220,000.00 USD | `-43.13%` | `1,751.91` |
| `Live` | `Long` | `1275.00` | 732,740,000.00 USD | 0.00 USD | 15,490,000.00 USD | `-42.68%` | `12,147.81` |
| `Live` | `Long` | `1285.00` | 717,250,000.00 USD | 0.00 USD | 556,180.00 USD | `-42.23%` | `432.82` |
| `Live` | `Long` | `1295.00` | 716,700,000.00 USD | 0.00 USD | 378,160.00 USD | `-41.78%` | `292.01` |
| `Live` | `Long` | `1305.00` | 716,320,000.00 USD | 0.00 USD | 125,780.00 USD | `-41.33%` | `96.38` |
| `Live` | `Long` | `1315.00` | 716,190,000.00 USD | 0.00 USD | 306,940.00 USD | `-40.88%` | `233.41` |
| `Live` | `Long` | `1325.00` | 715,880,000.00 USD | 0.00 USD | 640,550.00 USD | `-40.43%` | `483.43` |
| `Live` | `Long` | `1335.00` | 715,240,000.00 USD | 0.00 USD | 286,420.00 USD | `-39.98%` | `214.55` |
| `Live` | `Long` | `1345.00` | 714,960,000.00 USD | 0.00 USD | 580,160.00 USD | `-39.53%` | `431.35` |
| `Live` | `Long` | `1355.00` | 714,380,000.00 USD | 0.00 USD | 5,240,000.00 USD | `-39.08%` | `3,868.53` |
| `Live` | `Long` | `1365.00` | 709,140,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-38.63%` | `806.90` |
| `Live` | `Long` | `1375.00` | 708,030,000.00 USD | 0.00 USD | 7,130,000.00 USD | `-38.18%` | `5,185.78` |
| `Live` | `Long` | `1385.00` | 700,900,000.00 USD | 0.00 USD | 2,300,000.00 USD | `-37.73%` | `1,660.38` |
| `Live` | `Long` | `1395.00` | 698,600,000.00 USD | 0.00 USD | 520,350.00 USD | `-37.28%` | `373.01` |
| `Live` | `Long` | `1405.00` | 698,080,000.00 USD | 0.00 USD | 10,130,000.00 USD | `-36.83%` | `7,211.33` |
| `Live` | `Long` | `1415.00` | 687,950,000.00 USD | 0.00 USD | 554,220.00 USD | `-36.38%` | `391.67` |
| `Live` | `Long` | `1425.00` | 687,400,000.00 USD | 0.00 USD | 372,990.00 USD | `-35.93%` | `261.75` |
| `Live` | `Long` | `1435.00` | 687,020,000.00 USD | 0.00 USD | 1,210,000.00 USD | `-35.49%` | `842.87` |
| `Live` | `Long` | `1445.00` | 685,820,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-35.04%` | `1,466.35` |
| `Live` | `Long` | `1455.00` | 683,700,000.00 USD | 0.00 USD | 19,770,000.00 USD | `-34.59%` | `13,585.18` |
| `Live` | `Long` | `1465.00` | 663,930,000.00 USD | 0.00 USD | 2,030,000.00 USD | `-34.14%` | `1,388.71` |
| `Live` | `Long` | `1475.00` | 661,900,000.00 USD | 0.00 USD | 5,960,000.00 USD | `-33.69%` | `4,037.91` |
| `Live` | `Long` | `1485.00` | 655,940,000.00 USD | 0.00 USD | 139,630.00 USD | `-33.24%` | `94.03` |
| `Live` | `Long` | `1495.00` | 655,800,000.00 USD | 0.00 USD | 19,510,000.00 USD | `-32.79%` | `13,050.56` |
| `Live` | `Long` | `1505.00` | 636,290,000.00 USD | 0.00 USD | 293,500.00 USD | `-32.34%` | `195.02` |
| `Live` | `Long` | `1515.00` | 636,000,000.00 USD | 0.00 USD | 20,980,000.00 USD | `-31.89%` | `13,846.62` |
| `Live` | `Long` | `1525.00` | 615,020,000.00 USD | 0.00 USD | 275,130.00 USD | `-31.44%` | `180.41` |
| `Live` | `Long` | `1535.00` | 614,740,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-30.99%` | `688.26` |
| `Live` | `Long` | `1545.00` | 613,690,000.00 USD | 0.00 USD | 2,710,000.00 USD | `-30.54%` | `1,753.80` |
| `Live` | `Long` | `1555.00` | 610,980,000.00 USD | 0.00 USD | 3,810,000.00 USD | `-30.09%` | `2,449.88` |
| `Live` | `Long` | `1565.00` | 607,170,000.00 USD | 0.00 USD | 16,680,000.00 USD | `-29.64%` | `10,659.10` |
| `Live` | `Long` | `1575.00` | 590,490,000.00 USD | 0.00 USD | 747,200.00 USD | `-29.19%` | `474.41` |
| `Live` | `Long` | `1585.00` | 589,740,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-28.74%` | `691.63` |
| `Live` | `Long` | `1595.00` | 588,640,000.00 USD | 0.00 USD | 1,470,000.00 USD | `-28.29%` | `923.48` |
| `Live` | `Long` | `1605.00` | 587,170,000.00 USD | 0.00 USD | 17,980,000.00 USD | `-27.84%` | `11,204.10` |
| `Live` | `Long` | `1615.00` | 569,190,000.00 USD | 0.00 USD | 410,710.00 USD | `-27.39%` | `254.31` |
| `Live` | `Long` | `1625.00` | 568,780,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-26.94%` | `684.53` |
| `Live` | `Long` | `1635.00` | 567,660,000.00 USD | 0.00 USD | 18,690,000.00 USD | `-26.49%` | `11,430.73` |
| `Live` | `Long` | `1645.00` | 548,970,000.00 USD | 0.00 USD | 36,670,000.00 USD | `-26.04%` | `22,293.51` |
| `Live` | `Long` | `1655.00` | 512,300,000.00 USD | 0.00 USD | 533,660.00 USD | `-25.59%` | `322.46` |
| `Live` | `Long` | `1665.00` | 511,770,000.00 USD | 0.00 USD | 12,350,000.00 USD | `-25.14%` | `7,418.57` |
| `Live` | `Long` | `1675.00` | 499,420,000.00 USD | 0.00 USD | 1,460,000.00 USD | `-24.70%` | `870.85` |
| `Live` | `Long` | `1685.00` | 497,960,000.00 USD | 0.00 USD | 1,220,000.00 USD | `-24.25%` | `723.34` |
| `Live` | `Long` | `1695.00` | 496,740,000.00 USD | 0.00 USD | 870,240.00 USD | `-23.80%` | `513.41` |
| `Live` | `Long` | `1705.00` | 495,870,000.00 USD | 0.00 USD | 17,250,000.00 USD | `-23.35%` | `10,116.29` |
| `Live` | `Long` | `1715.00` | 478,620,000.00 USD | 0.00 USD | 17,850,000.00 USD | `-22.90%` | `10,410.04` |
| `Live` | `Long` | `1725.00` | 460,770,000.00 USD | 0.00 USD | 19,370,000.00 USD | `-22.45%` | `11,228.05` |
| `Live` | `Long` | `1735.00` | 441,400,000.00 USD | 0.00 USD | 1,390,000.00 USD | `-22.00%` | `799.89` |
| `Live` | `Long` | `1745.00` | 440,010,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-21.55%` | `638.64` |
| `Live` | `Long` | `1755.00` | 438,900,000.00 USD | 0.00 USD | 225,470.00 USD | `-21.10%` | `128.48` |
| `Live` | `Long` | `1765.00` | 438,670,000.00 USD | 0.00 USD | 3,830,000.00 USD | `-20.65%` | `2,172.77` |
| `Live` | `Long` | `1775.00` | 434,840,000.00 USD | 0.00 USD | 4,970,000.00 USD | `-20.20%` | `2,802.36` |
| `Live` | `Long` | `1785.00` | 429,860,000.00 USD | 0.00 USD | 83,330,000.00 USD | `-19.75%` | `46,685.95` |
| `Live` | `Long` | `1795.00` | 346,530,000.00 USD | 0.00 USD | 1,160,000.00 USD | `-19.30%` | `647.64` |
| `Live` | `Long` | `1805.00` | 345,360,000.00 USD | 0.00 USD | 8,320,000.00 USD | `-18.85%` | `4,611.73` |
| `Live` | `Long` | `1815.00` | 337,040,000.00 USD | 0.00 USD | 2,190,000.00 USD | `-18.40%` | `1,206.49` |
| `Live` | `Long` | `1825.00` | 334,850,000.00 USD | 0.00 USD | 4,200,000.00 USD | `-17.95%` | `2,299.74` |
| `Live` | `Long` | `1835.00` | 330,650,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-17.50%` | `602.44` |
| `Live` | `Long` | `1845.00` | 329,550,000.00 USD | 0.00 USD | 16,340,000.00 USD | `-17.05%` | `8,857.35` |
| `Live` | `Long` | `1855.00` | 313,210,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-16.60%` | `605.09` |
| `Live` | `Long` | `1865.00` | 312,080,000.00 USD | 0.00 USD | 1,300,000.00 USD | `-16.15%` | `698.59` |
| `Live` | `Long` | `1875.00` | 310,780,000.00 USD | 0.00 USD | 18,820,000.00 USD | `-15.70%` | `10,039.91` |
| `Live` | `Long` | `1885.00` | 291,960,000.00 USD | 0.00 USD | 4,920,000.00 USD | `-15.25%` | `2,608.83` |
| `Live` | `Long` | `1895.00` | 287,040,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-14.80%` | `690.50` |
| `Live` | `Long` | `1905.00` | 285,730,000.00 USD | 0.00 USD | 3,660,000.00 USD | `-14.36%` | `1,920.54` |
| `Live` | `Long` | `1915.00` | 282,070,000.00 USD | 0.00 USD | 17,910,000.00 USD | `-13.91%` | `9,353.98` |
| `Live` | `Long` | `1925.00` | 264,160,000.00 USD | 0.00 USD | 1,370,000.00 USD | `-13.46%` | `713.08` |
| `Live` | `Long` | `1935.00` | 262,790,000.00 USD | 0.00 USD | 17,760,000.00 USD | `-13.01%` | `9,179.16` |
| `Live` | `Long` | `1945.00` | 245,020,000.00 USD | 0.00 USD | 1,690,000.00 USD | `-12.56%` | `870.97` |
| `Live` | `Long` | `1955.00` | 243,330,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-12.11%` | `722.16` |
| `Live` | `Long` | `1965.00` | 241,920,000.00 USD | 0.00 USD | 14,400,000.00 USD | `-11.66%` | `7,330.61` |
| `Live` | `Long` | `1975.00` | 227,510,000.00 USD | 0.00 USD | 1,630,000.00 USD | `-11.21%` | `824.00` |
| `Live` | `Long` | `1985.00` | 225,890,000.00 USD | 0.00 USD | 5,570,000.00 USD | `-10.76%` | `2,807.01` |
| `Live` | `Long` | `1995.00` | 220,310,000.00 USD | 0.00 USD | 5,340,000.00 USD | `-10.31%` | `2,676.76` |
| `Live` | `Long` | `2005.00` | 214,970,000.00 USD | 0.00 USD | 13,090,000.00 USD | `-9.86%` | `6,528.05` |
| `Live` | `Long` | `2015.00` | 201,890,000.00 USD | 0.00 USD | 2,660,000.00 USD | `-9.41%` | `1,322.22` |
| `Live` | `Long` | `2025.00` | 199,220,000.00 USD | 0.00 USD | 1,180,000.00 USD | `-8.96%` | `583.38` |
| `Live` | `Long` | `2035.00` | 198,040,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-8.51%` | `543.38` |
| `Live` | `Long` | `2045.00` | 196,930,000.00 USD | 0.00 USD | 6,580,000.00 USD | `-8.06%` | `3,219.86` |
| `Live` | `Long` | `2055.00` | 190,350,000.00 USD | 0.00 USD | 3,870,000.00 USD | `-7.61%` | `1,881.11` |
| `Live` | `Long` | `2065.00` | 186,480,000.00 USD | 0.00 USD | 15,510,000.00 USD | `-7.16%` | `7,509.62` |
| `Live` | `Long` | `2075.00` | 170,980,000.00 USD | 0.00 USD | 3,430,000.00 USD | `-6.71%` | `1,654.52` |
| `Live` | `Long` | `2085.00` | 167,540,000.00 USD | 0.00 USD | 12,820,000.00 USD | `-6.26%` | `6,147.10` |
| `Live` | `Long` | `2095.00` | 154,730,000.00 USD | 0.00 USD | 1,840,000.00 USD | `-5.81%` | `880.55` |
| `Live` | `Long` | `2105.00` | 152,880,000.00 USD | 0.00 USD | 2,360,000.00 USD | `-5.36%` | `1,121.90` |
| `Live` | `Long` | `2115.00` | 150,520,000.00 USD | 0.00 USD | 2,210,000.00 USD | `-4.91%` | `1,044.21` |
| `Live` | `Long` | `2125.00` | 148,310,000.00 USD | 0.00 USD | 123,700,000.00 USD | `-4.46%` | `58,213.47` |
| `Live` | `Long` | `2135.00` | 24,610,000.00 USD | 0.00 USD | 1,490,000.00 USD | `-4.01%` | `698.74` |
| `Live` | `Long` | `2145.00` | 23,120,000.00 USD | 0.00 USD | 5,640,000.00 USD | `-3.57%` | `2,627.08` |
| `Live` | `Long` | `2155.00` | 17,480,000.00 USD | 0.00 USD | 1,690,000.00 USD | `-3.12%` | `784.04` |
| `Live` | `Long` | `2165.00` | 15,790,000.00 USD | 0.00 USD | 6,700,000.00 USD | `-2.67%` | `3,094.58` |
| `Live` | `Long` | `2175.00` | 9,090,000.00 USD | 0.00 USD | 5,690,000.00 USD | `-2.22%` | `2,615.40` |
| `Live` | `Long` | `2185.00` | 3,400,000.00 USD | 0.00 USD | 694,330.00 USD | `-1.77%` | `317.77` |
| `Live` | `Long` | `2195.00` | 2,710,000.00 USD | 0.00 USD | 2,250,000.00 USD | `-1.32%` | `1,026.59` |
| `Live` | `Long` | `2205.00` | 455,960.00 USD | 0.00 USD | 449,420.00 USD | `-0.87%` | `203.82` |
| `Live` | `Long` | `2215.00` | 6,540.00 USD | 0.00 USD | 6,540.00 USD | `-0.42%` | `2.95` |
| `Live` | `Short` | `2225.00` | 1,890.00 USD | 1,890.00 USD | 0.00 USD | `+0.03%` | `0.85` |
| `Live` | `Short` | `2245.00` | 4,460.00 USD | 2,570.00 USD | 0.00 USD | `+0.93%` | `1.15` |
| `Live` | `Short` | `2255.00` | 24,530.00 USD | 20,070.00 USD | 0.00 USD | `+1.38%` | `8.90` |
| `Live` | `Short` | `2265.00` | 118,040.00 USD | 93,510.00 USD | 0.00 USD | `+1.83%` | `41.28` |
| `Live` | `Short` | `2275.00` | 946,650.00 USD | 828,610.00 USD | 0.00 USD | `+2.28%` | `364.22` |
| `Live` | `Short` | `2285.00` | 1,440,000.00 USD | 490,730.00 USD | 0.00 USD | `+2.73%` | `214.76` |
| `Live` | `Short` | `2295.00` | 4,360,000.00 USD | 2,920,000.00 USD | 0.00 USD | `+3.18%` | `1,272.76` |
| `Live` | `Short` | `2305.00` | 4,810,000.00 USD | 448,140.00 USD | 0.00 USD | `+3.63%` | `194.42` |
| `Live` | `Short` | `2315.00` | 5,630,000.00 USD | 824,210.00 USD | 0.00 USD | `+4.08%` | `356.03` |
| `Live` | `Short` | `2325.00` | 8,880,000.00 USD | 3,250,000.00 USD | 0.00 USD | `+4.53%` | `1,396.72` |
| `Live` | `Short` | `2335.00` | 9,320,000.00 USD | 437,940.00 USD | 0.00 USD | `+4.98%` | `187.55` |
| `Live` | `Short` | `2345.00` | 9,730,000.00 USD | 415,460.00 USD | 0.00 USD | `+5.43%` | `177.17` |
| `Live` | `Short` | `2355.00` | 12,170,000.00 USD | 2,440,000.00 USD | 0.00 USD | `+5.88%` | `1,034.09` |
| `Live` | `Short` | `2365.00` | 17,030,000.00 USD | 4,860,000.00 USD | 0.00 USD | `+6.33%` | `2,055.20` |
| `Live` | `Short` | `2375.00` | 17,920,000.00 USD | 893,040.00 USD | 0.00 USD | `+6.78%` | `376.02` |
| `Live` | `Short` | `2385.00` | 18,640,000.00 USD | 722,850.00 USD | 0.00 USD | `+7.22%` | `303.08` |
| `Live` | `Short` | `2395.00` | 23,500,000.00 USD | 4,850,000.00 USD | 0.00 USD | `+7.67%` | `2,026.67` |
| `Live` | `Short` | `2405.00` | 23,610,000.00 USD | 115,180.00 USD | 0.00 USD | `+8.12%` | `47.89` |
| `Live` | `Short` | `2415.00` | 23,850,000.00 USD | 236,460.00 USD | 0.00 USD | `+8.57%` | `97.91` |
| `Live` | `Short` | `2425.00` | 24,140,000.00 USD | 289,470.00 USD | 0.00 USD | `+9.02%` | `119.37` |
| `Live` | `Short` | `2435.00` | 24,340,000.00 USD | 197,400.00 USD | 0.00 USD | `+9.47%` | `81.07` |
| `Live` | `Short` | `2445.00` | 29,130,000.00 USD | 4,800,000.00 USD | 0.00 USD | `+9.92%` | `1,961.21` |
| `Live` | `Short` | `2455.00` | 29,350,000.00 USD | 214,400.00 USD | 0.00 USD | `+10.37%` | `87.33` |
| `Live` | `Short` | `2465.00` | 40,890,000.00 USD | 11,550,000.00 USD | 0.00 USD | `+10.82%` | `4,684.83` |
| `Live` | `Short` | `2475.00` | 95,670,000.00 USD | 54,770,000.00 USD | 0.00 USD | `+11.27%` | `22,131.28` |
| `Live` | `Short` | `2485.00` | 97,320,000.00 USD | 1,650,000.00 USD | 0.00 USD | `+11.72%` | `664.64` |
| `Live` | `Short` | `2495.00` | 99,470,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+12.17%` | `860.11` |
| `Live` | `Short` | `2505.00` | 103,930,000.00 USD | 4,470,000.00 USD | 0.00 USD | `+12.62%` | `1,783.82` |
| `Live` | `Short` | `2515.00` | 105,530,000.00 USD | 1,590,000.00 USD | 0.00 USD | `+13.07%` | `634.16` |
| `Live` | `Short` | `2525.00` | 105,580,000.00 USD | 46,400.00 USD | 0.00 USD | `+13.52%` | `18.38` |
| `Live` | `Short` | `2535.00` | 106,630,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+13.97%` | `416.76` |
| `Live` | `Short` | `2545.00` | 111,670,000.00 USD | 5,040,000.00 USD | 0.00 USD | `+14.42%` | `1,978.95` |
| `Live` | `Short` | `2555.00` | 111,910,000.00 USD | 238,660.00 USD | 0.00 USD | `+14.87%` | `93.41` |
| `Live` | `Short` | `2565.00` | 112,000,000.00 USD | 89,050.00 USD | 0.00 USD | `+15.32%` | `34.72` |
| `Live` | `Short` | `2575.00` | 112,560,000.00 USD | 559,600.00 USD | 0.00 USD | `+15.77%` | `217.32` |
| `Live` | `Short` | `2585.00` | 146,870,000.00 USD | 34,310,000.00 USD | 0.00 USD | `+16.22%` | `13,273.57` |
| `Live` | `Short` | `2595.00` | 147,230,000.00 USD | 359,640.00 USD | 0.00 USD | `+16.67%` | `138.59` |
| `Live` | `Short` | `2605.00` | 153,030,000.00 USD | 5,810,000.00 USD | 0.00 USD | `+17.12%` | `2,229.24` |
| `Live` | `Short` | `2615.00` | 153,770,000.00 USD | 732,830.00 USD | 0.00 USD | `+17.57%` | `280.24` |
| `Live` | `Short` | `2625.00` | 199,180,000.00 USD | 45,410,000.00 USD | 0.00 USD | `+18.01%` | `17,298.59` |
| `Live` | `Short` | `2635.00` | 200,210,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+18.46%` | `390.95` |
| `Live` | `Short` | `2645.00` | 200,830,000.00 USD | 626,810.00 USD | 0.00 USD | `+18.91%` | `236.98` |
| `Live` | `Short` | `2655.00` | 227,660,000.00 USD | 26,820,000.00 USD | 0.00 USD | `+19.36%` | `10,103.19` |
| `Live` | `Short` | `2665.00` | 227,710,000.00 USD | 51,540.00 USD | 0.00 USD | `+19.81%` | `19.34` |
| `Live` | `Short` | `2675.00` | 228,810,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+20.26%` | `410.36` |
| `Live` | `Short` | `2685.00` | 228,830,000.00 USD | 23,200.00 USD | 0.00 USD | `+20.71%` | `8.64` |
| `Live` | `Short` | `2695.00` | 229,300,000.00 USD | 468,980.00 USD | 0.00 USD | `+21.16%` | `174.02` |
| `Live` | `Short` | `2705.00` | 230,000,000.00 USD | 698,920.00 USD | 0.00 USD | `+21.61%` | `258.38` |
| `Live` | `Short` | `2715.00` | 230,410,000.00 USD | 413,400.00 USD | 0.00 USD | `+22.06%` | `152.27` |
| `Live` | `Short` | `2725.00` | 230,640,000.00 USD | 229,610.00 USD | 0.00 USD | `+22.51%` | `84.26` |
| `Live` | `Short` | `2735.00` | 235,790,000.00 USD | 5,150,000.00 USD | 0.00 USD | `+22.96%` | `1,882.22` |
| `Live` | `Short` | `2745.00` | 249,580,000.00 USD | 13,790,000.00 USD | 0.00 USD | `+23.41%` | `5,025.44` |
| `Live` | `Short` | `2755.00` | 254,630,000.00 USD | 5,050,000.00 USD | 0.00 USD | `+23.86%` | `1,833.58` |
| `Live` | `Short` | `2765.00` | 255,050,000.00 USD | 416,000.00 USD | 0.00 USD | `+24.31%` | `150.45` |
| `Live` | `Short` | `2775.00` | 280,230,000.00 USD | 25,170,000.00 USD | 0.00 USD | `+24.76%` | `9,071.78` |
| `Live` | `Short` | `2785.00` | 280,750,000.00 USD | 528,660.00 USD | 0.00 USD | `+25.21%` | `189.82` |
| `Live` | `Short` | `2795.00` | 286,310,000.00 USD | 5,560,000.00 USD | 0.00 USD | `+25.66%` | `1,988.20` |
| `Live` | `Short` | `2805.00` | 292,240,000.00 USD | 5,930,000.00 USD | 0.00 USD | `+26.11%` | `2,112.46` |
| `Live` | `Short` | `2815.00` | 294,240,000.00 USD | 2,010,000.00 USD | 0.00 USD | `+26.56%` | `712.55` |
| `Live` | `Short` | `2825.00` | 294,380,000.00 USD | 133,850.00 USD | 0.00 USD | `+27.01%` | `47.38` |
| `Live` | `Short` | `2835.00` | 300,660,000.00 USD | 6,280,000.00 USD | 0.00 USD | `+27.46%` | `2,215.71` |
| `Live` | `Short` | `2845.00` | 301,010,000.00 USD | 349,690.00 USD | 0.00 USD | `+27.91%` | `122.92` |
| `Live` | `Short` | `2855.00` | 301,510,000.00 USD | 502,140.00 USD | 0.00 USD | `+28.35%` | `175.88` |
| `Live` | `Short` | `2865.00` | 301,930,000.00 USD | 422,840.00 USD | 0.00 USD | `+28.80%` | `147.59` |
| `Live` | `Short` | `2875.00` | 302,000,000.00 USD | 64,240.00 USD | 0.00 USD | `+29.25%` | `22.34` |
| `Live` | `Short` | `2885.00` | 303,730,000.00 USD | 1,740,000.00 USD | 0.00 USD | `+29.70%` | `601.87` |
| `Live` | `Short` | `2895.00` | 305,070,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+30.15%` | `463.25` |
| `Live` | `Short` | `2905.00` | 349,470,000.00 USD | 44,390,000.00 USD | 0.00 USD | `+30.60%` | `15,282.00` |
| `Live` | `Short` | `2915.00` | 351,820,000.00 USD | 2,350,000.00 USD | 0.00 USD | `+31.05%` | `807.62` |
| `Live` | `Short` | `2925.00` | 354,850,000.00 USD | 3,030,000.00 USD | 0.00 USD | `+31.50%` | `1,035.76` |
| `Live` | `Short` | `2935.00` | 354,920,000.00 USD | 67,460.00 USD | 0.00 USD | `+31.95%` | `22.99` |
| `Live` | `Short` | `2945.00` | 355,360,000.00 USD | 437,030.00 USD | 0.00 USD | `+32.40%` | `148.40` |
| `Live` | `Short` | `2955.00` | 359,930,000.00 USD | 4,570,000.00 USD | 0.00 USD | `+32.85%` | `1,548.18` |
| `Live` | `Short` | `2965.00` | 360,520,000.00 USD | 590,570.00 USD | 0.00 USD | `+33.30%` | `199.18` |
| `Live` | `Short` | `2975.00` | 363,880,000.00 USD | 3,360,000.00 USD | 0.00 USD | `+33.75%` | `1,128.30` |
| `Live` | `Short` | `2985.00` | 365,120,000.00 USD | 1,240,000.00 USD | 0.00 USD | `+34.20%` | `416.92` |
| `Live` | `Short` | `2995.00` | 380,150,000.00 USD | 15,030,000.00 USD | 0.00 USD | `+34.65%` | `5,018.80` |
| `Live` | `Short` | `3005.00` | 380,800,000.00 USD | 646,430.00 USD | 0.00 USD | `+35.10%` | `215.12` |
| `Live` | `Short` | `3015.00` | 380,980,000.00 USD | 175,020.00 USD | 0.00 USD | `+35.55%` | `58.05` |
| `Live` | `Short` | `3025.00` | 381,840,000.00 USD | 862,710.00 USD | 0.00 USD | `+36.00%` | `285.19` |
| `Live` | `Short` | `3035.00` | 396,860,000.00 USD | 15,030,000.00 USD | 0.00 USD | `+36.45%` | `4,950.87` |
| `Live` | `Short` | `3045.00` | 397,580,000.00 USD | 715,260.00 USD | 0.00 USD | `+36.90%` | `234.90` |
| `Live` | `Short` | `3055.00` | 397,590,000.00 USD | 6,520.00 USD | 0.00 USD | `+37.35%` | `2.14` |
| `Live` | `Short` | `3065.00` | 399,100,000.00 USD | 1,510,000.00 USD | 0.00 USD | `+37.80%` | `492.46` |
| `Live` | `Short` | `3075.00` | 405,170,000.00 USD | 6,070,000.00 USD | 0.00 USD | `+38.25%` | `1,973.85` |
| `Live` | `Short` | `3085.00` | 416,100,000.00 USD | 10,930,000.00 USD | 0.00 USD | `+38.70%` | `3,543.92` |
| `Live` | `Short` | `3095.00` | 421,880,000.00 USD | 5,780,000.00 USD | 0.00 USD | `+39.14%` | `1,868.35` |
| `Live` | `Short` | `3105.00` | 434,170,000.00 USD | 12,290,000.00 USD | 0.00 USD | `+39.59%` | `3,956.62` |
| `Live` | `Short` | `3115.00` | 468,050,000.00 USD | 33,880,000.00 USD | 0.00 USD | `+40.04%` | `10,877.23` |
| `Live` | `Short` | `3125.00` | 469,910,000.00 USD | 1,870,000.00 USD | 0.00 USD | `+40.49%` | `597.23` |
| `Live` | `Short` | `3135.00` | 470,180,000.00 USD | 261,240.00 USD | 0.00 USD | `+40.94%` | `83.33` |
| `Live` | `Short` | `3145.00` | 470,580,000.00 USD | 401,090.00 USD | 0.00 USD | `+41.39%` | `127.53` |
| `Live` | `Short` | `3155.00` | 470,800,000.00 USD | 222,300.00 USD | 0.00 USD | `+41.84%` | `70.46` |
| `Live` | `Short` | `3165.00` | 470,930,000.00 USD | 130,620.00 USD | 0.00 USD | `+42.29%` | `41.27` |
| `Live` | `Short` | `3175.00` | 472,020,000.00 USD | 1,090,000.00 USD | 0.00 USD | `+42.74%` | `343.57` |
| `Live` | `Short` | `3185.00` | 542,680,000.00 USD | 70,660,000.00 USD | 0.00 USD | `+43.19%` | `22,183.97` |
| `Live` | `Short` | `3195.00` | 542,890,000.00 USD | 210,270.00 USD | 0.00 USD | `+43.64%` | `65.81` |
| `Live` | `Short` | `3205.00` | 543,240,000.00 USD | 352,030.00 USD | 0.00 USD | `+44.09%` | `109.84` |
| `Live` | `Short` | `3215.00` | 543,410,000.00 USD | 175,220.00 USD | 0.00 USD | `+44.54%` | `54.50` |
| `Live` | `Short` | `3225.00` | 551,750,000.00 USD | 8,340,000.00 USD | 0.00 USD | `+44.99%` | `2,584.90` |
| `Live` | `Short` | `3235.00` | 561,510,000.00 USD | 9,760,000.00 USD | 0.00 USD | `+45.44%` | `3,016.19` |
| `Live` | `Short` | `3245.00` | 566,360,000.00 USD | 4,850,000.00 USD | 0.00 USD | `+45.89%` | `1,496.04` |
| `Live` | `Short` | `3255.00` | 566,380,000.00 USD | 12,810.00 USD | 0.00 USD | `+46.34%` | `3.93` |
| `Live` | `Short` | `3265.00` | 566,440,000.00 USD | 65,860.00 USD | 0.00 USD | `+46.79%` | `20.17` |
| `Live` | `Short` | `3275.00` | 577,270,000.00 USD | 10,830,000.00 USD | 0.00 USD | `+47.24%` | `3,307.06` |
| `Live` | `Short` | `3285.00` | 577,340,000.00 USD | 65,540.00 USD | 0.00 USD | `+47.69%` | `19.95` |
| `Live` | `Short` | `3295.00` | 577,670,000.00 USD | 334,070.00 USD | 0.00 USD | `+48.14%` | `101.39` |
| `Live` | `Short` | `3305.00` | 578,940,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+48.59%` | `384.36` |
| `Live` | `Short` | `3315.00` | 581,060,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+49.04%` | `639.66` |
| `Live` | `Short` | `3325.00` | 581,140,000.00 USD | 75,050.00 USD | 0.00 USD | `+49.49%` | `22.57` |
| `Live` | `Short` | `3335.00` | 582,620,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+49.93%` | `443.70` |
| `Live` | `Short` | `3345.00` | 582,680,000.00 USD | 58,000.00 USD | 0.00 USD | `+50.38%` | `17.34` |
| `Live` | `Short` | `3355.00` | 584,720,000.00 USD | 2,050,000.00 USD | 0.00 USD | `+50.83%` | `609.89` |
| `Live` | `Short` | `3365.00` | 587,690,000.00 USD | 2,970,000.00 USD | 0.00 USD | `+51.28%` | `881.89` |
| `Live` | `Short` | `3375.00` | 590,120,000.00 USD | 2,430,000.00 USD | 0.00 USD | `+51.73%` | `718.89` |
| `Live` | `Short` | `3385.00` | 590,220,000.00 USD | 102,540.00 USD | 0.00 USD | `+52.18%` | `30.29` |
| `Live` | `Short` | `3395.00` | 590,310,000.00 USD | 93,920.00 USD | 0.00 USD | `+52.63%` | `27.66` |
| `Live` | `Short` | `3405.00` | 591,580,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+53.08%` | `372.47` |
| `Live` | `Short` | `3415.00` | 595,780,000.00 USD | 4,200,000.00 USD | 0.00 USD | `+53.53%` | `1,231.30` |
| `Live` | `Short` | `3425.00` | 610,370,000.00 USD | 14,590,000.00 USD | 0.00 USD | `+53.98%` | `4,258.75` |
| `Live` | `Short` | `3435.00` | 610,470,000.00 USD | 95,600.00 USD | 0.00 USD | `+54.43%` | `27.83` |
| `Live` | `Short` | `3445.00` | 611,350,000.00 USD | 881,390.00 USD | 0.00 USD | `+54.88%` | `255.85` |
| `Live` | `Short` | `3455.00` | 611,910,000.00 USD | 559,510.00 USD | 0.00 USD | `+55.33%` | `161.94` |
| `Live` | `Short` | `3465.00` | 612,330,000.00 USD | 424,610.00 USD | 0.00 USD | `+55.78%` | `122.54` |
| `Live` | `Short` | `3475.00` | 612,390,000.00 USD | 55,090.00 USD | 0.00 USD | `+56.23%` | `15.85` |
| `Live` | `Short` | `3485.00` | 612,420,000.00 USD | 30,100.00 USD | 0.00 USD | `+56.68%` | `8.64` |
| `Live` | `Short` | `3495.00` | 613,580,000.00 USD | 1,170,000.00 USD | 0.00 USD | `+57.13%` | `334.09` |
| `Live` | `Short` | `3505.00` | 615,230,000.00 USD | 1,640,000.00 USD | 0.00 USD | `+57.58%` | `469.01` |
| `Live` | `Short` | `3515.00` | 615,600,000.00 USD | 375,650.00 USD | 0.00 USD | `+58.03%` | `106.87` |
| `Live` | `Short` | `3525.00` | 616,370,000.00 USD | 765,100.00 USD | 0.00 USD | `+58.48%` | `217.05` |
| `Live` | `Short` | `3535.00` | 631,200,000.00 USD | 14,830,000.00 USD | 0.00 USD | `+58.93%` | `4,194.93` |
| `Live` | `Short` | `3545.00` | 631,300,000.00 USD | 97,280.00 USD | 0.00 USD | `+59.38%` | `27.44` |
| `Live` | `Short` | `3555.00` | 631,420,000.00 USD | 119,970.00 USD | 0.00 USD | `+59.83%` | `33.75` |
| `Live` | `Short` | `3565.00` | 631,540,000.00 USD | 125,810.00 USD | 0.00 USD | `+60.28%` | `35.29` |
| `Live` | `Short` | `3575.00` | 631,620,000.00 USD | 80,980.00 USD | 0.00 USD | `+60.72%` | `22.65` |
| `Live` | `Short` | `3585.00` | 632,370,000.00 USD | 749,130.00 USD | 0.00 USD | `+61.17%` | `208.96` |
| `Live` | `Short` | `3595.00` | 632,420,000.00 USD | 43,700.00 USD | 0.00 USD | `+61.62%` | `12.15` |
| `Live` | `Short` | `3605.00` | 632,480,000.00 USD | 62,790.00 USD | 0.00 USD | `+62.07%` | `17.42` |
| `Live` | `Short` | `3615.00` | 636,270,000.00 USD | 3,790,000.00 USD | 0.00 USD | `+62.52%` | `1,047.50` |
| `Live` | `Short` | `3625.00` | 637,390,000.00 USD | 1,120,000.00 USD | 0.00 USD | `+62.97%` | `309.01` |
| `Live` | `Short` | `3635.00` | 646,200,000.00 USD | 8,820,000.00 USD | 0.00 USD | `+63.42%` | `2,425.46` |
| `Live` | `Short` | `3645.00` | 699,750,000.00 USD | 53,550,000.00 USD | 0.00 USD | `+63.87%` | `14,690.08` |
| `Live` | `Short` | `3655.00` | 699,780,000.00 USD | 37,050.00 USD | 0.00 USD | `+64.32%` | `10.14` |
| `Live` | `Short` | `3665.00` | 700,130,000.00 USD | 343,720.00 USD | 0.00 USD | `+64.77%` | `93.78` |
| `Live` | `Short` | `3675.00` | 706,670,000.00 USD | 6,540,000.00 USD | 0.00 USD | `+65.22%` | `1,779.72` |
| `Live` | `Short` | `3685.00` | 706,880,000.00 USD | 212,010.00 USD | 0.00 USD | `+65.67%` | `57.53` |
| `Live` | `Short` | `3695.00` | 706,910,000.00 USD | 31,030.00 USD | 0.00 USD | `+66.12%` | `8.40` |
| `Live` | `Short` | `3705.00` | 710,770,000.00 USD | 3,860,000.00 USD | 0.00 USD | `+66.57%` | `1,041.70` |
| `Live` | `Short` | `3715.00` | 710,770,000.00 USD | 2,920.00 USD | 0.00 USD | `+67.02%` | `0.79` |
| `Live` | `Short` | `3725.00` | 1,090,000,000.00 USD | 382,870,000.00 USD | 0.00 USD | `+67.47%` | `102,784.23` |
| `Live` | `Short` | `3735.00` | 1,090,000,000.00 USD | 360,220.00 USD | 0.00 USD | `+67.92%` | `96.44` |
| `Live` | `Short` | `3745.00` | 1,100,000,000.00 USD | 2,710,000.00 USD | 0.00 USD | `+68.37%` | `724.56` |
| `Live` | `Short` | `3755.00` | 1,100,000,000.00 USD | 163,780.00 USD | 0.00 USD | `+68.82%` | `43.62` |
| `Live` | `Short` | `3765.00` | 1,100,000,000.00 USD | 78,340.00 USD | 0.00 USD | `+69.27%` | `20.81` |
| `Live` | `Short` | `3775.00` | 1,100,000,000.00 USD | 456,790.00 USD | 0.00 USD | `+69.72%` | `121.00` |
| `Live` | `Short` | `3785.00` | 1,160,000,000.00 USD | 59,410,000.00 USD | 0.00 USD | `+70.17%` | `15,696.92` |
| `Live` | `Short` | `3795.00` | 1,160,000,000.00 USD | 3,470,000.00 USD | 0.00 USD | `+70.62%` | `914.81` |
| `Live` | `Short` | `3805.00` | 1,170,000,000.00 USD | 4,850,000.00 USD | 0.00 USD | `+71.07%` | `1,273.85` |
| `Live` | `Short` | `3815.00` | 1,170,000,000.00 USD | 1,590.00 USD | 0.00 USD | `+71.51%` | `0.42` |
| `Live` | `Short` | `3825.00` | 1,170,000,000.00 USD | 34,550.00 USD | 0.00 USD | `+71.96%` | `9.03` |
| `Live` | `Short` | `3835.00` | 1,170,000,000.00 USD | 280,720.00 USD | 0.00 USD | `+72.41%` | `73.20` |
| `Live` | `Short` | `3845.00` | 1,170,000,000.00 USD | 212,940.00 USD | 0.00 USD | `+72.86%` | `55.38` |
| `Live` | `Short` | `3855.00` | 1,170,000,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+73.31%` | `273.48` |
| `Live` | `Short` | `3865.00` | 1,170,000,000.00 USD | 2,480,000.00 USD | 0.00 USD | `+73.76%` | `640.80` |
| `Live` | `Short` | `3875.00` | 1,170,000,000.00 USD | 93,260.00 USD | 0.00 USD | `+74.21%` | `24.07` |
| `Live` | `Short` | `3885.00` | 1,170,000,000.00 USD | 1,360,000.00 USD | 0.00 USD | `+74.66%` | `351.03` |
| `Live` | `Short` | `3895.00` | 1,170,000,000.00 USD | 2,490,000.00 USD | 0.00 USD | `+75.11%` | `640.54` |
| `Live` | `Short` | `3905.00` | 1,210,000,000.00 USD | 38,870,000.00 USD | 0.00 USD | `+75.56%` | `9,954.89` |
| `Live` | `Short` | `3915.00` | 1,210,000,000.00 USD | 553,260.00 USD | 0.00 USD | `+76.01%` | `141.32` |
| `Live` | `Short` | `3925.00` | 1,210,000,000.00 USD | 152,270.00 USD | 0.00 USD | `+76.46%` | `38.79` |
| `Live` | `Short` | `3935.00` | 1,210,000,000.00 USD | 2,640.00 USD | 0.00 USD | `+76.91%` | `0.67` |
| `Live` | `Short` | `3945.00` | 1,210,000,000.00 USD | 88,480.00 USD | 0.00 USD | `+77.36%` | `22.43` |
| `Live` | `Short` | `3955.00` | 1,210,000,000.00 USD | 1,660.00 USD | 0.00 USD | `+77.81%` | `0.42` |
| `Live` | `Short` | `3965.00` | 1,210,000,000.00 USD | 30,880.00 USD | 0.00 USD | `+78.26%` | `7.79` |
| `Live` | `Short` | `3975.00` | 1,210,000,000.00 USD | 160,630.00 USD | 0.00 USD | `+78.71%` | `40.41` |
| `Live` | `Short` | `3985.00` | 1,210,000,000.00 USD | 178,550.00 USD | 0.00 USD | `+79.16%` | `44.80` |
| `Live` | `Short` | `3995.00` | 1,210,000,000.00 USD | 562,130.00 USD | 0.00 USD | `+79.61%` | `140.71` |
| `Live` | `Short` | `4005.00` | 1,210,000,000.00 USD | 141,730.00 USD | 0.00 USD | `+80.06%` | `35.39` |
| `Live` | `Short` | `4015.00` | 1,220,000,000.00 USD | 1,230,000.00 USD | 0.00 USD | `+80.51%` | `305.37` |
| `Live` | `Short` | `4025.00` | 1,220,000,000.00 USD | 490,570.00 USD | 0.00 USD | `+80.96%` | `121.88` |
| `Live` | `Short` | `4035.00` | 1,220,000,000.00 USD | 414,520.00 USD | 0.00 USD | `+81.41%` | `102.73` |
| `Live` | `Short` | `4045.00` | 1,220,000,000.00 USD | 121,110.00 USD | 0.00 USD | `+81.85%` | `29.94` |
| `Live` | `Short` | `4055.00` | 1,220,000,000.00 USD | 1,690,000.00 USD | 0.00 USD | `+82.30%` | `416.77` |
| `Live` | `Short` | `4065.00` | 1,220,000,000.00 USD | 1,200,000.00 USD | 0.00 USD | `+82.75%` | `295.68` |
| `Live` | `Short` | `4075.00` | 1,220,000,000.00 USD | 129,220.00 USD | 0.00 USD | `+83.20%` | `31.71` |
| `Live` | `Short` | `4085.00` | 1,220,000,000.00 USD | 91,390.00 USD | 0.00 USD | `+83.65%` | `22.37` |
| `Live` | `Short` | `4095.00` | 1,220,000,000.00 USD | 207,480.00 USD | 0.00 USD | `+84.10%` | `50.67` |
| `Live` | `Short` | `4105.00` | 1,220,000,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+84.55%` | `279.04` |
| `Live` | `Short` | `4115.00` | 1,220,000,000.00 USD | 129,580.00 USD | 0.00 USD | `+85.00%` | `31.49` |
| `Live` | `Short` | `4125.00` | 1,220,000,000.00 USD | 151,430.00 USD | 0.00 USD | `+85.45%` | `36.71` |
| `Live` | `Short` | `4135.00` | 1,220,000,000.00 USD | 608,480.00 USD | 0.00 USD | `+85.90%` | `147.15` |
| `Live` | `Short` | `4145.00` | 1,220,000,000.00 USD | 99,240.00 USD | 0.00 USD | `+86.35%` | `23.94` |
| `Live` | `Short` | `4155.00` | 1,220,000,000.00 USD | 681,920.00 USD | 0.00 USD | `+86.80%` | `164.12` |
| `Live` | `Short` | `4165.00` | 1,220,000,000.00 USD | 132,850.00 USD | 0.00 USD | `+87.25%` | `31.90` |
| `Live` | `Short` | `4175.00` | 1,220,000,000.00 USD | 209,470.00 USD | 0.00 USD | `+87.70%` | `50.17` |
| `Live` | `Short` | `4185.00` | 1,220,000,000.00 USD | 948,630.00 USD | 0.00 USD | `+88.15%` | `226.67` |
| `Live` | `Short` | `4195.00` | 1,260,000,000.00 USD | 32,730,000.00 USD | 0.00 USD | `+88.60%` | `7,801.99` |
| `Live` | `Short` | `4205.00` | 1,260,000,000.00 USD | 42,140.00 USD | 0.00 USD | `+89.05%` | `10.02` |
| `Live` | `Short` | `4215.00` | 1,260,000,000.00 USD | 42,320.00 USD | 0.00 USD | `+89.50%` | `10.04` |
| `Live` | `Short` | `4225.00` | 1,260,000,000.00 USD | 801,540.00 USD | 0.00 USD | `+89.95%` | `189.71` |
| `Live` | `Short` | `4235.00` | 1,340,000,000.00 USD | 83,560,000.00 USD | 0.00 USD | `+90.40%` | `19,730.11` |
| `Live` | `Short` | `4245.00` | 1,340,000,000.00 USD | 335,020.00 USD | 0.00 USD | `+90.85%` | `78.92` |
| `Live` | `Short` | `4255.00` | 1,340,000,000.00 USD | 420.39 USD | 0.00 USD | `+91.30%` | `0.10` |
| `Live` | `Short` | `4265.00` | 1,340,000,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+91.75%` | `509.16` |
| `Live` | `Short` | `4275.00` | 1,340,000,000.00 USD | 4,060.00 USD | 0.00 USD | `+92.20%` | `0.95` |
| `Live` | `Short` | `4285.00` | 1,340,000,000.00 USD | 2,450.00 USD | 0.00 USD | `+92.64%` | `0.57` |
| `Live` | `Short` | `4295.00` | 1,340,000,000.00 USD | 15,180.00 USD | 0.00 USD | `+93.09%` | `3.54` |
| `Live` | `Short` | `4305.00` | 1,340,000,000.00 USD | 17,120.00 USD | 0.00 USD | `+93.54%` | `3.98` |
| `Live` | `Short` | `4315.00` | 1,340,000,000.00 USD | 50,390.00 USD | 0.00 USD | `+93.99%` | `11.68` |
| `Live` | `Short` | `4325.00` | 1,340,000,000.00 USD | 36,530.00 USD | 0.00 USD | `+94.44%` | `8.45` |
| `Live` | `Short` | `4335.00` | 1,340,000,000.00 USD | 32,800.00 USD | 0.00 USD | `+94.89%` | `7.57` |
| `Live` | `Short` | `4345.00` | 1,340,000,000.00 USD | 204,690.00 USD | 0.00 USD | `+95.34%` | `47.11` |
| `Live` | `Short` | `4355.00` | 1,340,000,000.00 USD | 6,930.00 USD | 0.00 USD | `+95.79%` | `1.59` |
| `Live` | `Short` | `4365.00` | 1,340,000,000.00 USD | 1,140,000.00 USD | 0.00 USD | `+96.24%` | `262.00` |
| `Live` | `Short` | `4375.00` | 1,340,000,000.00 USD | 19,130.00 USD | 0.00 USD | `+96.69%` | `4.37` |
| `Live` | `Short` | `4385.00` | 1,340,000,000.00 USD | 4,180.00 USD | 0.00 USD | `+97.14%` | `0.95` |
| `Live` | `Short` | `4395.00` | 1,350,000,000.00 USD | 615,700.00 USD | 0.00 USD | `+97.59%` | `140.09` |
| `Live` | `Short` | `4405.00` | 1,350,000,000.00 USD | 23,210.00 USD | 0.00 USD | `+98.04%` | `5.27` |
| `Live` | `Short` | `4415.00` | 1,350,000,000.00 USD | 129,550.00 USD | 0.00 USD | `+98.49%` | `29.34` |
| `Live` | `Short` | `4425.00` | 1,350,000,000.00 USD | 8,230.00 USD | 0.00 USD | `+98.94%` | `1.86` |
| `Live` | `Short` | `4435.00` | 1,350,000,000.00 USD | 73,170.00 USD | 0.00 USD | `+99.39%` | `16.50` |
| `Live` | `Short` | `4445.00` | 1,350,000,000.00 USD | 25,610.00 USD | 0.00 USD | `+99.84%` | `5.76` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `485.00` | 70,280,000.00 USD | 0.00 USD | 278.83 USD | `-78.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `505.00` | 70,280,000.00 USD | 0.00 USD | 16,100.00 USD | `-77.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 70,270,000.00 USD | 0.00 USD | 563.16 USD | `-75.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.00` | 70,270,000.00 USD | 0.00 USD | 170.14 USD | `-74.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.00` | 70,270,000.00 USD | 0.00 USD | 259.78 USD | `-72.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.00` | 70,270,000.00 USD | 0.00 USD | 583.40 USD | `-71.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.00` | 70,270,000.00 USD | 0.00 USD | 613.93 USD | `-70.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.00` | 70,270,000.00 USD | 0.00 USD | 578.54 USD | `-69.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.00` | 70,270,000.00 USD | 0.00 USD | 242.21 USD | `-68.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 70,260,000.00 USD | 0.00 USD | 885.90 USD | `-68.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `715.00` | 70,260,000.00 USD | 0.00 USD | 4,130.00 USD | `-67.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `725.00` | 70,260,000.00 USD | 0.00 USD | 15,090.00 USD | `-67.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 70,240,000.00 USD | 0.00 USD | 177.27 USD | `-66.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 70,240,000.00 USD | 0.00 USD | 2,400.00 USD | `-63.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 70,240,000.00 USD | 0.00 USD | 1,670.00 USD | `-62.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 70,240,000.00 USD | 0.00 USD | 139,430.00 USD | `-61.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `875.00` | 70,100,000.00 USD | 0.00 USD | 918.49 USD | `-60.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 70,100,000.00 USD | 0.00 USD | 3,130.00 USD | `-60.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 70,100,000.00 USD | 0.00 USD | 2,780.00 USD | `-59.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 70,090,000.00 USD | 0.00 USD | 516.34 USD | `-55.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 70,090,000.00 USD | 0.00 USD | 100.50 USD | `-55.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 70,090,000.00 USD | 0.00 USD | 223,740.00 USD | `-54.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 69,870,000.00 USD | 0.00 USD | 445.08 USD | `-54.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 69,870,000.00 USD | 0.00 USD | 112.03 USD | `-53.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1045.00` | 69,870,000.00 USD | 0.00 USD | 1,260.00 USD | `-53.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 69,870,000.00 USD | 0.00 USD | 1,060.00 USD | `-52.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 69,870,000.00 USD | 0.00 USD | 995.34 USD | `-51.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 69,870,000.00 USD | 0.00 USD | 1,610.00 USD | `-50.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 69,860,000.00 USD | 0.00 USD | 11,050.00 USD | `-49.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 69,850,000.00 USD | 0.00 USD | 1,320.00 USD | `-49.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 69,850,000.00 USD | 0.00 USD | 1,000.00 USD | `-48.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 69,850,000.00 USD | 0.00 USD | 476.46 USD | `-47.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 69,850,000.00 USD | 0.00 USD | 972.41 USD | `-46.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1195.00` | 69,850,000.00 USD | 0.00 USD | 221.55 USD | `-46.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 69,850,000.00 USD | 0.00 USD | 3,110.00 USD | `-45.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 69,850,000.00 USD | 0.00 USD | 995.93 USD | `-44.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 69,850,000.00 USD | 0.00 USD | 951.93 USD | `-44.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 69,840,000.00 USD | 0.00 USD | 2,290.00 USD | `-43.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 69,840,000.00 USD | 0.00 USD | 9,050.00 USD | `-42.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 69,830,000.00 USD | 0.00 USD | 7,030.00 USD | `-41.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 69,830,000.00 USD | 0.00 USD | 23,030.00 USD | `-41.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 69,800,000.00 USD | 0.00 USD | 1,440.00 USD | `-40.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1335.00` | 69,800,000.00 USD | 0.00 USD | 281.69 USD | `-39.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 69,800,000.00 USD | 0.00 USD | 144,020.00 USD | `-39.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 69,660,000.00 USD | 0.00 USD | 128.86 USD | `-39.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 69,660,000.00 USD | 0.00 USD | 1,270.00 USD | `-38.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 69,660,000.00 USD | 0.00 USD | 4,160.00 USD | `-38.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1385.00` | 69,650,000.00 USD | 0.00 USD | 100,800.00 USD | `-37.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 69,550,000.00 USD | 0.00 USD | 535,600.00 USD | `-37.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 69,020,000.00 USD | 0.00 USD | 18,840.00 USD | `-36.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 69,000,000.00 USD | 0.00 USD | 6,450.00 USD | `-35.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 68,990,000.00 USD | 0.00 USD | 852.10 USD | `-35.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 68,990,000.00 USD | 0.00 USD | 1,610.00 USD | `-35.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 68,990,000.00 USD | 0.00 USD | 5,090.00 USD | `-34.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 68,980,000.00 USD | 0.00 USD | 19,730.00 USD | `-34.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 68,960,000.00 USD | 0.00 USD | 2,600.00 USD | `-33.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 68,960,000.00 USD | 0.00 USD | 19,930.00 USD | `-33.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 68,940,000.00 USD | 0.00 USD | 11,460.00 USD | `-32.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 68,930,000.00 USD | 0.00 USD | 68,840.00 USD | `-32.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 68,860,000.00 USD | 0.00 USD | 11,140.00 USD | `-31.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 68,850,000.00 USD | 0.00 USD | 31,900.00 USD | `-31.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 68,820,000.00 USD | 0.00 USD | 2,090.00 USD | `-30.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 68,810,000.00 USD | 0.00 USD | 960.99 USD | `-30.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 68,810,000.00 USD | 0.00 USD | 32,880.00 USD | `-30.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 68,780,000.00 USD | 0.00 USD | 10,660.00 USD | `-29.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 68,770,000.00 USD | 0.00 USD | 198,620.00 USD | `-29.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 68,570,000.00 USD | 0.00 USD | 4,990.00 USD | `-28.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 68,570,000.00 USD | 0.00 USD | 9,090.00 USD | `-28.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 68,560,000.00 USD | 0.00 USD | 431,660.00 USD | `-27.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 68,130,000.00 USD | 0.00 USD | 25,700.00 USD | `-27.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 68,100,000.00 USD | 0.00 USD | 15,920.00 USD | `-26.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 68,080,000.00 USD | 0.00 USD | 10,560.00 USD | `-26.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 68,070,000.00 USD | 0.00 USD | 323,930.00 USD | `-26.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 67,750,000.00 USD | 0.00 USD | 114,830.00 USD | `-25.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 67,630,000.00 USD | 0.00 USD | 865.13 USD | `-25.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 67,630,000.00 USD | 0.00 USD | 289.27 USD | `-24.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 67,630,000.00 USD | 0.00 USD | 35,320.00 USD | `-24.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 67,600,000.00 USD | 0.00 USD | 42,420.00 USD | `-23.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 67,560,000.00 USD | 0.00 USD | 84,860.00 USD | `-23.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 67,470,000.00 USD | 0.00 USD | 16,350.00 USD | `-22.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 67,450,000.00 USD | 0.00 USD | 47,500.00 USD | `-22.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 67,410,000.00 USD | 0.00 USD | 28,150.00 USD | `-22.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 67,380,000.00 USD | 0.00 USD | 3,180.00 USD | `-21.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 67,380,000.00 USD | 0.00 USD | 466,520.00 USD | `-21.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 66,910,000.00 USD | 0.00 USD | 77,450.00 USD | `-20.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 66,830,000.00 USD | 0.00 USD | 3,090.00 USD | `-20.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 66,830,000.00 USD | 0.00 USD | 8,500.00 USD | `-19.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 66,820,000.00 USD | 0.00 USD | 191,050.00 USD | `-19.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 66,630,000.00 USD | 0.00 USD | 756,110.00 USD | `-18.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 65,870,000.00 USD | 0.00 USD | 264,490.00 USD | `-18.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 65,610,000.00 USD | 0.00 USD | 39,660.00 USD | `-17.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 65,570,000.00 USD | 0.00 USD | 5,260.00 USD | `-17.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 65,560,000.00 USD | 0.00 USD | 30,780.00 USD | `-17.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 65,530,000.00 USD | 0.00 USD | 789,490.00 USD | `-16.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 64,740,000.00 USD | 0.00 USD | 41,250.00 USD | `-16.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 64,700,000.00 USD | 0.00 USD | 18,200,000.00 USD | `-15.70%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 46,510,000.00 USD | 0.00 USD | 19,770.00 USD | `-15.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 46,490,000.00 USD | 0.00 USD | 61,630.00 USD | `-14.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 46,420,000.00 USD | 0.00 USD | 153,490.00 USD | `-14.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 46,270,000.00 USD | 0.00 USD | 104,860.00 USD | `-13.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1925.00` | 46,170,000.00 USD | 0.00 USD | 19,310,000.00 USD | `-13.46%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 26,860,000.00 USD | 0.00 USD | 117,650.00 USD | `-13.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 26,740,000.00 USD | 0.00 USD | 61,020.00 USD | `-12.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 26,680,000.00 USD | 0.00 USD | 65,650.00 USD | `-12.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 26,610,000.00 USD | 0.00 USD | 138,620.00 USD | `-11.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 26,480,000.00 USD | 0.00 USD | 69,900.00 USD | `-11.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 26,410,000.00 USD | 0.00 USD | 105,150.00 USD | `-10.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 26,300,000.00 USD | 0.00 USD | 125,080.00 USD | `-10.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 26,180,000.00 USD | 0.00 USD | 2,090,000.00 USD | `-9.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 24,090,000.00 USD | 0.00 USD | 48,350.00 USD | `-9.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 24,040,000.00 USD | 0.00 USD | 15,730.00 USD | `-8.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 24,030,000.00 USD | 0.00 USD | 177,870.00 USD | `-8.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 23,850,000.00 USD | 0.00 USD | 39,670.00 USD | `-8.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 23,810,000.00 USD | 0.00 USD | 273,990.00 USD | `-7.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 23,530,000.00 USD | 0.00 USD | 828,390.00 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 22,710,000.00 USD | 0.00 USD | 761,840.00 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 21,940,000.00 USD | 0.00 USD | 136,050.00 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 21,810,000.00 USD | 0.00 USD | 33,120.00 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 21,770,000.00 USD | 0.00 USD | 470,680.00 USD | `-5.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 21,300,000.00 USD | 0.00 USD | 176,680.00 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 21,130,000.00 USD | 0.00 USD | 210,460.00 USD | `-4.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 20,920,000.00 USD | 0.00 USD | 342,670.00 USD | `-4.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 20,570,000.00 USD | 0.00 USD | 526,510.00 USD | `-3.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 20,050,000.00 USD | 0.00 USD | 1,820,000.00 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 18,230,000.00 USD | 0.00 USD | 1,680,000.00 USD | `-2.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 16,540,000.00 USD | 0.00 USD | 9,750,000.00 USD | `-2.22%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2185.00` | 6,790,000.00 USD | 0.00 USD | 219,480.00 USD | `-1.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 6,570,000.00 USD | 0.00 USD | 3,040,000.00 USD | `-1.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 3,530,000.00 USD | 0.00 USD | 1,580,000.00 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2225.00` | 583,300.00 USD | 583,300.00 USD | 0.00 USD | `+0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2235.00` | 1,950,000.00 USD | 1,360,000.00 USD | 0.00 USD | `+0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2245.00` | 2,810,000.00 USD | 865,920.00 USD | 0.00 USD | `+0.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2255.00` | 3,360,000.00 USD | 549,610.00 USD | 0.00 USD | `+1.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2265.00` | 5,250,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 5,700,000.00 USD | 447,920.00 USD | 0.00 USD | `+2.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 6,540,000.00 USD | 840,590.00 USD | 0.00 USD | `+2.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 6,990,000.00 USD | 444,860.00 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 17,010,000.00 USD | 10,020,000.00 USD | 0.00 USD | `+3.63%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2315.00` | 18,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | `+4.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 18,690,000.00 USD | 231,970.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 18,860,000.00 USD | 168,630.00 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 20,430,000.00 USD | 1,570,000.00 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 21,680,000.00 USD | 1,260,000.00 USD | 0.00 USD | `+5.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 23,890,000.00 USD | 2,210,000.00 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 24,060,000.00 USD | 163,240.00 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 26,020,000.00 USD | 1,970,000.00 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 27,120,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+7.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 29,630,000.00 USD | 2,510,000.00 USD | 0.00 USD | `+8.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 29,920,000.00 USD | 286,440.00 USD | 0.00 USD | `+8.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 32,200,000.00 USD | 2,280,000.00 USD | 0.00 USD | `+9.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 32,390,000.00 USD | 189,700.00 USD | 0.00 USD | `+9.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 34,870,000.00 USD | 2,490,000.00 USD | 0.00 USD | `+9.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2455.00` | 35,020,000.00 USD | 141,470.00 USD | 0.00 USD | `+10.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 37,140,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+10.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 37,320,000.00 USD | 181,240.00 USD | 0.00 USD | `+11.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 39,420,000.00 USD | 2,100,000.00 USD | 0.00 USD | `+11.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 39,540,000.00 USD | 122,320.00 USD | 0.00 USD | `+12.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 44,600,000.00 USD | 5,060,000.00 USD | 0.00 USD | `+12.62%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2515.00` | 52,200,000.00 USD | 7,600,000.00 USD | 0.00 USD | `+13.07%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 54,820,000.00 USD | 2,610,000.00 USD | 0.00 USD | `+13.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 54,880,000.00 USD | 61,230.00 USD | 0.00 USD | `+13.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 57,060,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+14.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 57,260,000.00 USD | 199,370.00 USD | 0.00 USD | `+14.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 59,620,000.00 USD | 2,360,000.00 USD | 0.00 USD | `+15.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 59,710,000.00 USD | 93,110.00 USD | 0.00 USD | `+15.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 62,220,000.00 USD | 2,510,000.00 USD | 0.00 USD | `+16.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 62,240,000.00 USD | 10,500.00 USD | 0.00 USD | `+16.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 65,510,000.00 USD | 3,280,000.00 USD | 0.00 USD | `+17.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 65,590,000.00 USD | 79,040.00 USD | 0.00 USD | `+17.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 67,770,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+18.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 67,920,000.00 USD | 147,930.00 USD | 0.00 USD | `+18.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 70,040,000.00 USD | 2,130,000.00 USD | 0.00 USD | `+18.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 70,350,000.00 USD | 306,950.00 USD | 0.00 USD | `+19.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 72,490,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+19.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 72,750,000.00 USD | 261,420.00 USD | 0.00 USD | `+20.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 74,930,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 75,020,000.00 USD | 94,620.00 USD | 0.00 USD | `+21.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 77,860,000.00 USD | 2,840,000.00 USD | 0.00 USD | `+21.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 77,940,000.00 USD | 76,590.00 USD | 0.00 USD | `+22.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 78,230,000.00 USD | 286,910.00 USD | 0.00 USD | `+22.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 78,270,000.00 USD | 43,050.00 USD | 0.00 USD | `+22.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 78,450,000.00 USD | 178,210.00 USD | 0.00 USD | `+23.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 79,340,000.00 USD | 892,290.00 USD | 0.00 USD | `+23.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 79,440,000.00 USD | 103,020.00 USD | 0.00 USD | `+24.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 80,020,000.00 USD | 579,030.00 USD | 0.00 USD | `+24.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 80,060,000.00 USD | 35,580.00 USD | 0.00 USD | `+25.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 80,080,000.00 USD | 17,550.00 USD | 0.00 USD | `+25.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 80,980,000.00 USD | 905,020.00 USD | 0.00 USD | `+26.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 81,030,000.00 USD | 52,490.00 USD | 0.00 USD | `+26.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 81,080,000.00 USD | 43,930.00 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 81,360,000.00 USD | 286,140.00 USD | 0.00 USD | `+27.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 82,370,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+27.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 83,640,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+28.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 83,650,000.00 USD | 11,150.00 USD | 0.00 USD | `+28.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 83,650,000.00 USD | 2,460.00 USD | 0.00 USD | `+29.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 83,960,000.00 USD | 305,820.00 USD | 0.00 USD | `+29.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 83,980,000.00 USD | 16,190.00 USD | 0.00 USD | `+30.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 85,460,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+30.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 85,470,000.00 USD | 10,340.00 USD | 0.00 USD | `+31.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 85,470,000.00 USD | 3,050.00 USD | 0.00 USD | `+31.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 85,530,000.00 USD | 52,370.00 USD | 0.00 USD | `+31.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 85,560,000.00 USD | 34,650.00 USD | 0.00 USD | `+32.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 85,610,000.00 USD | 44,750.00 USD | 0.00 USD | `+32.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 85,720,000.00 USD | 113,340.00 USD | 0.00 USD | `+33.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 85,860,000.00 USD | 145,510.00 USD | 0.00 USD | `+33.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 86,800,000.00 USD | 931,470.00 USD | 0.00 USD | `+34.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 91,720,000.00 USD | 4,920,000.00 USD | 0.00 USD | `+34.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 93,800,000.00 USD | 2,080,000.00 USD | 0.00 USD | `+35.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 93,810,000.00 USD | 9,740.00 USD | 0.00 USD | `+35.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 93,840,000.00 USD | 35,380.00 USD | 0.00 USD | `+36.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 93,920,000.00 USD | 74,910.00 USD | 0.00 USD | `+36.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 93,940,000.00 USD | 22,460.00 USD | 0.00 USD | `+36.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 94,710,000.00 USD | 771,070.00 USD | 0.00 USD | `+37.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 94,710,000.00 USD | 612.69 USD | 0.00 USD | `+37.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 94,760,000.00 USD | 49,330.00 USD | 0.00 USD | `+38.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 94,780,000.00 USD | 19,570.00 USD | 0.00 USD | `+38.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 94,780,000.00 USD | 928.50 USD | 0.00 USD | `+39.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 106,660,000.00 USD | 11,880,000.00 USD | 0.00 USD | `+39.59%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 106,770,000.00 USD | 110,480.00 USD | 0.00 USD | `+40.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 107,150,000.00 USD | 381,020.00 USD | 0.00 USD | `+40.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3135.00` | 107,150,000.00 USD | 674.02 USD | 0.00 USD | `+40.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 107,150,000.00 USD | 2,660.00 USD | 0.00 USD | `+41.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 107,210,000.00 USD | 58,930.00 USD | 0.00 USD | `+41.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 107,220,000.00 USD | 9,860.00 USD | 0.00 USD | `+42.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 107,220,000.00 USD | 149.22 USD | 0.00 USD | `+42.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 107,230,000.00 USD | 1,330.00 USD | 0.00 USD | `+43.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 107,270,000.00 USD | 41,120.00 USD | 0.00 USD | `+43.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 107,930,000.00 USD | 660,240.00 USD | 0.00 USD | `+44.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 107,930,000.00 USD | 1,760.00 USD | 0.00 USD | `+44.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 108,080,000.00 USD | 156,230.00 USD | 0.00 USD | `+44.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 108,080,000.00 USD | 167.25 USD | 0.00 USD | `+45.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 108,140,000.00 USD | 57,500.00 USD | 0.00 USD | `+45.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 108,380,000.00 USD | 236,580.00 USD | 0.00 USD | `+46.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 108,390,000.00 USD | 15,710.00 USD | 0.00 USD | `+46.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 108,400,000.00 USD | 1,630.00 USD | 0.00 USD | `+47.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 108,540,000.00 USD | 141,980.00 USD | 0.00 USD | `+47.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 108,550,000.00 USD | 15,350.00 USD | 0.00 USD | `+48.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 109,970,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+48.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 110,360,000.00 USD | 389,970.00 USD | 0.00 USD | `+49.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 110,380,000.00 USD | 24,200.00 USD | 0.00 USD | `+49.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 110,380,000.00 USD | 4,350.00 USD | 0.00 USD | `+49.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 110,390,000.00 USD | 2,170.00 USD | 0.00 USD | `+50.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 110,390,000.00 USD | 334.49 USD | 0.00 USD | `+50.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 110,390,000.00 USD | 295.78 USD | 0.00 USD | `+51.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 110,410,000.00 USD | 21,260.00 USD | 0.00 USD | `+51.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 110,470,000.00 USD | 58,010.00 USD | 0.00 USD | `+52.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 110,790,000.00 USD | 321,800.00 USD | 0.00 USD | `+52.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 112,270,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+53.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 112,280,000.00 USD | 5,700.00 USD | 0.00 USD | `+53.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 112,290,000.00 USD | 16,310.00 USD | 0.00 USD | `+53.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 112,310,000.00 USD | 15,030.00 USD | 0.00 USD | `+54.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 112,330,000.00 USD | 18,600.00 USD | 0.00 USD | `+55.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 112,330,000.00 USD | 495.50 USD | 0.00 USD | `+55.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 112,330,000.00 USD | 3,190.00 USD | 0.00 USD | `+56.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 112,370,000.00 USD | 43,610.00 USD | 0.00 USD | `+56.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 112,370,000.00 USD | 158.32 USD | 0.00 USD | `+57.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 112,820,000.00 USD | 446,770.00 USD | 0.00 USD | `+57.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 112,860,000.00 USD | 43,510.00 USD | 0.00 USD | `+58.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 112,870,000.00 USD | 3,690.00 USD | 0.00 USD | `+58.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 112,880,000.00 USD | 9,810.00 USD | 0.00 USD | `+58.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 112,970,000.00 USD | 90,810.00 USD | 0.00 USD | `+59.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 112,970,000.00 USD | 2,300.00 USD | 0.00 USD | `+60.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3575.00` | 112,970,000.00 USD | 2,870.00 USD | 0.00 USD | `+60.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 112,970,000.00 USD | 354.92 USD | 0.00 USD | `+61.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 112,990,000.00 USD | 13,160.00 USD | 0.00 USD | `+61.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 113,090,000.00 USD | 101,080.00 USD | 0.00 USD | `+62.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3615.00` | 113,090,000.00 USD | 199.55 USD | 0.00 USD | `+62.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 113,100,000.00 USD | 10,210.00 USD | 0.00 USD | `+62.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 113,110,000.00 USD | 7,790.00 USD | 0.00 USD | `+63.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 113,110,000.00 USD | 3,860.00 USD | 0.00 USD | `+63.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 113,110,000.00 USD | 820.18 USD | 0.00 USD | `+64.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 113,120,000.00 USD | 8,130.00 USD | 0.00 USD | `+64.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 113,180,000.00 USD | 55,120.00 USD | 0.00 USD | `+65.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 113,180,000.00 USD | 1,410.00 USD | 0.00 USD | `+65.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 113,180,000.00 USD | 819.92 USD | 0.00 USD | `+66.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 113,180,000.00 USD | 323.58 USD | 0.00 USD | `+67.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 113,180,000.00 USD | 1,400.00 USD | 0.00 USD | `+67.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 113,190,000.00 USD | 6,490.00 USD | 0.00 USD | `+67.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3745.00` | 113,190,000.00 USD | 165.90 USD | 0.00 USD | `+68.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 113,190,000.00 USD | 751.00 USD | 0.00 USD | `+68.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 113,190,000.00 USD | 286.90 USD | 0.00 USD | `+70.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 113,190,000.00 USD | 1,560.00 USD | 0.00 USD | `+70.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 113,920,000.00 USD | 732,630.00 USD | 0.00 USD | `+71.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 113,940,000.00 USD | 20,930.00 USD | 0.00 USD | `+71.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 113,950,000.00 USD | 8,380.00 USD | 0.00 USD | `+71.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 113,950,000.00 USD | 711.78 USD | 0.00 USD | `+72.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 113,950,000.00 USD | 355.28 USD | 0.00 USD | `+72.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 113,960,000.00 USD | 5,170.00 USD | 0.00 USD | `+73.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 113,980,000.00 USD | 19,430.00 USD | 0.00 USD | `+74.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 113,990,000.00 USD | 12,120.00 USD | 0.00 USD | `+75.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 114,710,000.00 USD | 717,170.00 USD | 0.00 USD | `+76.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 114,750,000.00 USD | 42,570.00 USD | 0.00 USD | `+76.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 114,810,000.00 USD | 59,170.00 USD | 0.00 USD | `+77.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 114,810,000.00 USD | 1,380.00 USD | 0.00 USD | `+77.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 114,820,000.00 USD | 6,960.00 USD | 0.00 USD | `+78.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 114,830,000.00 USD | 14,610.00 USD | 0.00 USD | `+79.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 114,830,000.00 USD | 4,280.00 USD | 0.00 USD | `+79.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 117,470,000.00 USD | 2,640,000.00 USD | 0.00 USD | `+80.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 117,470,000.00 USD | 898.59 USD | 0.00 USD | `+81.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 117,470,000.00 USD | 811.00 USD | 0.00 USD | `+82.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 117,480,000.00 USD | 4,310.00 USD | 0.00 USD | `+83.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 117,480,000.00 USD | 3,050.00 USD | 0.00 USD | `+83.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 117,520,000.00 USD | 36,740.00 USD | 0.00 USD | `+84.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 117,520,000.00 USD | 5,990.00 USD | 0.00 USD | `+85.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 117,520,000.00 USD | 372.90 USD | 0.00 USD | `+85.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 117,520,000.00 USD | 395.43 USD | 0.00 USD | `+86.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 117,520,000.00 USD | 376.65 USD | 0.00 USD | `+88.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 117,570,000.00 USD | 42,260.00 USD | 0.00 USD | `+89.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 117,570,000.00 USD | 460.70 USD | 0.00 USD | `+89.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 117,570,000.00 USD | 1,270.00 USD | 0.00 USD | `+89.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 117,570,000.00 USD | 4,300.00 USD | 0.00 USD | `+91.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 117,570,000.00 USD | 437.16 USD | 0.00 USD | `+91.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 117,640,000.00 USD | 64,550.00 USD | 0.00 USD | `+92.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 117,640,000.00 USD | 1,610.00 USD | 0.00 USD | `+92.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 117,730,000.00 USD | 94,600.00 USD | 0.00 USD | `+93.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 117,730,000.00 USD | 1,070.00 USD | 0.00 USD | `+93.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 117,750,000.00 USD | 11,270.00 USD | 0.00 USD | `+95.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 117,750,000.00 USD | 2,400.00 USD | 0.00 USD | `+95.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 117,790,000.00 USD | 43,750.00 USD | 0.00 USD | `+96.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 117,860,000.00 USD | 64,570.00 USD | 0.00 USD | `+97.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 117,860,000.00 USD | 1,050.00 USD | 0.00 USD | `+97.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 117,910,000.00 USD | 56,760.00 USD | 0.00 USD | `+98.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 117,930,000.00 USD | 11,480.00 USD | 0.00 USD | `+98.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 117,930,000.00 USD | 2,510.00 USD | 0.00 USD | `+98.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 118,110,000.00 USD | 177,400.00 USD | 0.00 USD | `+99.39%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1972.30` | 849,340,000.00 USD | 0.00 USD | 849,340,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD |
| `7D` | `1975.10` | 849,210,000.00 USD | 0.00 USD | 849,210,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD |
| `7D` | `1977.90` | 849,160,000.00 USD | 0.00 USD | 849,160,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1983.50` | 846,920,000.00 USD | 0.00 USD | 846,920,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD |
| `7D` | `1986.30` | 846,720,000.00 USD | 0.00 USD | 846,720,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1989.10` | 842,980,000.00 USD | 0.00 USD | 842,980,000.00 USD | 0.00 USD | 1,780,000.00 USD | 38,060.00 USD |
| `7D` | `1991.90` | 841,170,000.00 USD | 0.00 USD | 841,170,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD |
| `7D` | `1994.70` | 838,460,000.00 USD | 0.00 USD | 838,460,000.00 USD | 0.00 USD | 0.00 USD | 808,380.00 USD |
| `7D` | `1997.50` | 837,650,000.00 USD | 0.00 USD | 837,650,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1997.90` | 714,930,000.00 USD | 0.00 USD | 714,930,000.00 USD | 219,590.00 USD | 92,480.00 USD | 328,290.00 USD |
| `1D` | `2000.40` | 714,290,000.00 USD | 0.00 USD | 714,290,000.00 USD | 218,020.00 USD | 248,200.00 USD | 586,930.00 USD |
| `1D` | `2002.90` | 713,230,000.00 USD | 0.00 USD | 713,230,000.00 USD | 738,150.00 USD | 702,190.00 USD | 1,180,000.00 USD |
| `7D` | `2003.10` | 836,310,000.00 USD | 0.00 USD | 836,310,000.00 USD | 0.00 USD | 266,430.00 USD | 617,240.00 USD |
| `1D` | `2005.40` | 710,620,000.00 USD | 0.00 USD | 710,620,000.00 USD | 773,690.00 USD | 17,210.00 USD | 9,210.00 USD |
| `7D` | `2005.90` | 835,430,000.00 USD | 0.00 USD | 835,430,000.00 USD | 0.00 USD | 475,660.00 USD | 0.00 USD |
| `1D` | `2007.90` | 709,820,000.00 USD | 0.00 USD | 709,820,000.00 USD | 0.00 USD | 558,480.00 USD | 281,160.00 USD |
| `7D` | `2008.70` | 834,950,000.00 USD | 0.00 USD | 834,950,000.00 USD | 807,770.00 USD | 0.00 USD | 380,820.00 USD |
| `1D` | `2010.40` | 708,980,000.00 USD | 0.00 USD | 708,980,000.00 USD | 484,920.00 USD | 490,130.00 USD | 374,070.00 USD |
| `7D` | `2011.50` | 833,760,000.00 USD | 0.00 USD | 833,760,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD |
| `1D` | `2012.90` | 707,630,000.00 USD | 0.00 USD | 707,630,000.00 USD | 323,800.00 USD | 270,490.00 USD | 25,520.00 USD |
| `1D` | `2015.40` | 707,010,000.00 USD | 0.00 USD | 707,010,000.00 USD | 478,950.00 USD | 605,010.00 USD | 208,350.00 USD |
| `7D` | `2017.10` | 832,810,000.00 USD | 0.00 USD | 832,810,000.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD |
| `1D` | `2017.90` | 705,720,000.00 USD | 0.00 USD | 705,720,000.00 USD | 1,170,000.00 USD | 1,040,000.00 USD | 553,080.00 USD |
| `7D` | `2019.90` | 832,790,000.00 USD | 0.00 USD | 832,790,000.00 USD | 820,980.00 USD | 466,180.00 USD | 0.00 USD |
| `1D` | `2020.40` | 702,960,000.00 USD | 0.00 USD | 702,960,000.00 USD | 789,460.00 USD | 1,620,000.00 USD | 696,790.00 USD |
| `7D` | `2022.70` | 831,500,000.00 USD | 0.00 USD | 831,500,000.00 USD | 1,830,000.00 USD | 484,980.00 USD | 1,550,000.00 USD |
| `1D` | `2022.90` | 699,850,000.00 USD | 0.00 USD | 699,850,000.00 USD | 1,610,000.00 USD | 333,350.00 USD | 1,900,000.00 USD |
| `1D` | `2025.40` | 696,010,000.00 USD | 0.00 USD | 696,010,000.00 USD | 414,330.00 USD | 1,190,000.00 USD | 231,680.00 USD |
| `7D` | `2025.50` | 827,640,000.00 USD | 0.00 USD | 827,640,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2027.90` | 694,170,000.00 USD | 0.00 USD | 694,170,000.00 USD | 2,770,000.00 USD | 978,910.00 USD | 312,840.00 USD |
| `7D` | `2028.30` | 827,460,000.00 USD | 0.00 USD | 827,460,000.00 USD | 1,100,000.00 USD | 0.00 USD | 35,180.00 USD |
| `1D` | `2030.40` | 690,110,000.00 USD | 0.00 USD | 690,110,000.00 USD | 87,180.00 USD | 366,120.00 USD | 957,140.00 USD |
| `7D` | `2031.10` | 826,330,000.00 USD | 0.00 USD | 826,330,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD |
| `1D` | `2032.90` | 688,700,000.00 USD | 0.00 USD | 688,700,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD |
| `7D` | `2033.90` | 821,760,000.00 USD | 0.00 USD | 821,760,000.00 USD | 0.00 USD | 0.00 USD | 1,350,000.00 USD |
| `1D` | `2035.40` | 685,140,000.00 USD | 0.00 USD | 685,140,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD |
| `7D` | `2036.70` | 820,400,000.00 USD | 0.00 USD | 820,400,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD |
| `1D` | `2037.90` | 683,800,000.00 USD | 0.00 USD | 683,800,000.00 USD | 396,700.00 USD | 458,110.00 USD | 388,420.00 USD |
| `7D` | `2039.50` | 820,070,000.00 USD | 0.00 USD | 820,070,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2040.40` | 682,560,000.00 USD | 0.00 USD | 682,560,000.00 USD | 834,710.00 USD | 178,560.00 USD | 21,940.00 USD |
| `1D` | `2042.90` | 681,520,000.00 USD | 0.00 USD | 681,520,000.00 USD | 334,790.00 USD | 0.00 USD | 174,920.00 USD |
| `7D` | `2045.10` | 818,620,000.00 USD | 0.00 USD | 818,620,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD |
| `1D` | `2045.40` | 681,010,000.00 USD | 0.00 USD | 681,010,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD |
| `1D` | `2047.90` | 680,980,000.00 USD | 0.00 USD | 680,980,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD |
| `1D` | `2050.40` | 680,160,000.00 USD | 0.00 USD | 680,160,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2050.70` | 818,320,000.00 USD | 0.00 USD | 818,320,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2052.90` | 679,050,000.00 USD | 0.00 USD | 679,050,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD |
| `7D` | `2053.50` | 818,100,000.00 USD | 0.00 USD | 818,100,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2055.40` | 679,020,000.00 USD | 0.00 USD | 679,020,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD |
| `1D` | `2057.90` | 678,690,000.00 USD | 0.00 USD | 678,690,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2059.10` | 815,810,000.00 USD | 0.00 USD | 815,810,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2061.90` | 815,470,000.00 USD | 0.00 USD | 815,470,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `1D` | `2062.90` | 677,940,000.00 USD | 0.00 USD | 677,940,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD |
| `7D` | `2064.70` | 810,210,000.00 USD | 0.00 USD | 810,210,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `1D` | `2065.40` | 677,860,000.00 USD | 0.00 USD | 677,860,000.00 USD | 563,140.00 USD | 537,030.00 USD | 510,200.00 USD |
| `7D` | `2067.50` | 807,750,000.00 USD | 0.00 USD | 807,750,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD |
| `1D` | `2067.90` | 676,250,000.00 USD | 0.00 USD | 676,250,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD |
| `7D` | `2070.30` | 806,100,000.00 USD | 0.00 USD | 806,100,000.00 USD | 3,600,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `1D` | `2070.40` | 675,550,000.00 USD | 0.00 USD | 675,550,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD |
| `1D` | `2072.90` | 675,180,000.00 USD | 0.00 USD | 675,180,000.00 USD | 47,910.00 USD | 555,250.00 USD | 420,170.00 USD |
| `7D` | `2073.10` | 798,540,000.00 USD | 0.00 USD | 798,540,000.00 USD | 2,870,000.00 USD | 2,180,000.00 USD | 2,030,000.00 USD |
| `1D` | `2075.40` | 674,150,000.00 USD | 0.00 USD | 674,150,000.00 USD | 379,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2075.90` | 791,460,000.00 USD | 0.00 USD | 791,460,000.00 USD | 3,910,000.00 USD | 4,290,000.00 USD | 4,300,000.00 USD |
| `1D` | `2077.90` | 673,770,000.00 USD | 0.00 USD | 673,770,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD |
| `7D` | `2078.70` | 778,960,000.00 USD | 0.00 USD | 778,960,000.00 USD | 4,160,000.00 USD | 3,730,000.00 USD | 2,060,000.00 USD |
| `1D` | `2080.40` | 673,750,000.00 USD | 0.00 USD | 673,750,000.00 USD | 77,960.00 USD | 29,610.00 USD | 199,420.00 USD |
| `7D` | `2081.50` | 769,010,000.00 USD | 0.00 USD | 769,010,000.00 USD | 4,400,000.00 USD | 1,290,000.00 USD | 1,220,000.00 USD |
| `1D` | `2082.90` | 673,440,000.00 USD | 0.00 USD | 673,440,000.00 USD | 827,940.00 USD | 4,240.00 USD | 206,010.00 USD |
| `7D` | `2084.30` | 762,100,000.00 USD | 0.00 USD | 762,100,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 3,500,000.00 USD |
| `1D` | `2085.40` | 672,400,000.00 USD | 0.00 USD | 672,400,000.00 USD | 528,660.00 USD | 200,510.00 USD | 820,410.00 USD |
| `7D` | `2087.10` | 754,720,000.00 USD | 0.00 USD | 754,720,000.00 USD | 2,920,000.00 USD | 2,750,000.00 USD | 3,020,000.00 USD |
| `1D` | `2087.90` | 670,850,000.00 USD | 0.00 USD | 670,850,000.00 USD | 324,560.00 USD | 180,420.00 USD | 306,130.00 USD |
| `7D` | `2089.90` | 746,030,000.00 USD | 0.00 USD | 746,030,000.00 USD | 4,130,000.00 USD | 948,120.00 USD | 3,160,000.00 USD |
| `1D` | `2090.40` | 670,040,000.00 USD | 0.00 USD | 670,040,000.00 USD | 758,170.00 USD | 223,260.00 USD | 445,500.00 USD |
| `7D` | `2092.70` | 737,790,000.00 USD | 0.00 USD | 737,790,000.00 USD | 4,680,000.00 USD | 737,060.00 USD | 6,220,000.00 USD |
| `1D` | `2092.90` | 668,620,000.00 USD | 0.00 USD | 668,620,000.00 USD | 655,300.00 USD | 228,180.00 USD | 275,040.00 USD |
| `1D` | `2095.40` | 667,460,000.00 USD | 0.00 USD | 667,460,000.00 USD | 1,840,000.00 USD | 1,130,000.00 USD | 1,560,000.00 USD |
| `7D` | `2095.50` | 726,160,000.00 USD | 0.00 USD | 726,160,000.00 USD | 2,480,000.00 USD | 2,010,000.00 USD | 1,020,000.00 USD |
| `1D` | `2097.90` | 662,920,000.00 USD | 0.00 USD | 662,920,000.00 USD | 345,860.00 USD | 488,160.00 USD | 309,770.00 USD |
| `7D` | `2098.30` | 720,650,000.00 USD | 0.00 USD | 720,650,000.00 USD | 3,020,000.00 USD | 3,130,000.00 USD | 1,480,000.00 USD |
| `1D` | `2100.40` | 661,780,000.00 USD | 0.00 USD | 661,780,000.00 USD | 137,320.00 USD | 928,890.00 USD | 231,410.00 USD |
| `7D` | `2101.10` | 713,030,000.00 USD | 0.00 USD | 713,030,000.00 USD | 631,640.00 USD | 1,240,000.00 USD | 3,400,000.00 USD |
| `1D` | `2102.90` | 660,480,000.00 USD | 0.00 USD | 660,480,000.00 USD | 279,330.00 USD | 222,480.00 USD | 302,840.00 USD |
| `7D` | `2103.90` | 707,750,000.00 USD | 0.00 USD | 707,750,000.00 USD | 1,130,000.00 USD | 738,240.00 USD | 2,320,000.00 USD |
| `1D` | `2105.40` | 659,670,000.00 USD | 0.00 USD | 659,670,000.00 USD | 3,510,000.00 USD | 1,160,000.00 USD | 833,200.00 USD |
| `7D` | `2106.70` | 703,560,000.00 USD | 0.00 USD | 703,560,000.00 USD | 1,700,000.00 USD | 834,660.00 USD | 1,180,000.00 USD |
| `1D` | `2107.90` | 654,170,000.00 USD | 0.00 USD | 654,170,000.00 USD | 795,870.00 USD | 0.00 USD | 347,020.00 USD |
| `7D` | `2109.50` | 699,850,000.00 USD | 0.00 USD | 699,850,000.00 USD | 7,750,000.00 USD | 1,800,000.00 USD | 1,770,000.00 USD |
| `1D` | `2110.40` | 653,030,000.00 USD | 0.00 USD | 653,030,000.00 USD | 36,110.00 USD | 31,550.00 USD | 6,190.00 USD |
| `7D` | `2112.30` | 688,530,000.00 USD | 0.00 USD | 688,530,000.00 USD | 3,920,000.00 USD | 1,480,000.00 USD | 3,710,000.00 USD |
| `1D` | `2112.90` | 652,960,000.00 USD | 0.00 USD | 652,960,000.00 USD | 866,490.00 USD | 506,690.00 USD | 244,160.00 USD |
| `7D` | `2115.10` | 679,410,000.00 USD | 0.00 USD | 679,410,000.00 USD | 923,330.00 USD | 3,210,000.00 USD | 1,930,000.00 USD |
| `1D` | `2115.40` | 651,340,000.00 USD | 0.00 USD | 651,340,000.00 USD | 410,020.00 USD | 400,200.00 USD | 939,960.00 USD |
| `1D` | `2117.90` | 649,590,000.00 USD | 0.00 USD | 649,590,000.00 USD | 4,540,000.00 USD | 3,940,000.00 USD | 302,800.00 USD |
| `7D` | `2117.90` | 673,340,000.00 USD | 0.00 USD | 673,340,000.00 USD | 8,390,000.00 USD | 578,010.00 USD | 2,580,000.00 USD |
| `1D` | `2120.40` | 640,800,000.00 USD | 0.00 USD | 640,800,000.00 USD | 5,470,000.00 USD | 325,610.00 USD | 671,270.00 USD |
| `7D` | `2120.70` | 661,790,000.00 USD | 0.00 USD | 661,790,000.00 USD | 7,060,000.00 USD | 5,780,000.00 USD | 1,820,000.00 USD |
| `1D` | `2122.90` | 634,330,000.00 USD | 0.00 USD | 634,330,000.00 USD | 5,450,000.00 USD | 3,490,000.00 USD | 2,660,000.00 USD |
| `7D` | `2123.50` | 647,140,000.00 USD | 0.00 USD | 647,140,000.00 USD | 7,150,000.00 USD | 7,720,000.00 USD | 1,410,000.00 USD |
| `1D` | `2125.40` | 622,730,000.00 USD | 0.00 USD | 622,730,000.00 USD | 4,480,000.00 USD | 2,390,000.00 USD | 1,320,000.00 USD |
| `7D` | `2126.30` | 630,860,000.00 USD | 0.00 USD | 630,860,000.00 USD | 2,740,000.00 USD | 4,400,000.00 USD | 4,790,000.00 USD |
| `1D` | `2127.90` | 614,540,000.00 USD | 0.00 USD | 614,540,000.00 USD | 4,430,000.00 USD | 3,780,000.00 USD | 745,430.00 USD |
| `7D` | `2129.10` | 618,930,000.00 USD | 0.00 USD | 618,930,000.00 USD | 4,770,000.00 USD | 1,270,000.00 USD | 1,100,000.00 USD |
| `1D` | `2130.40` | 605,590,000.00 USD | 0.00 USD | 605,590,000.00 USD | 1,250,000.00 USD | 18,610.00 USD | 1,140,000.00 USD |
| `7D` | `2131.90` | 611,780,000.00 USD | 0.00 USD | 611,780,000.00 USD | 2,170,000.00 USD | 1,620,000.00 USD | 1,360,000.00 USD |
| `1D` | `2132.90` | 603,180,000.00 USD | 0.00 USD | 603,180,000.00 USD | 95,260.00 USD | 434,790.00 USD | 1,550,000.00 USD |
| `7D` | `2134.70` | 606,630,000.00 USD | 0.00 USD | 606,630,000.00 USD | 1,630,000.00 USD | 790,240.00 USD | 898,290.00 USD |
| `1D` | `2135.40` | 601,110,000.00 USD | 0.00 USD | 601,110,000.00 USD | 2,760,000.00 USD | 2,950,000.00 USD | 2,210,000.00 USD |
| `7D` | `2137.50` | 603,320,000.00 USD | 0.00 USD | 603,320,000.00 USD | 2,120,000.00 USD | 2,390,000.00 USD | 1,590,000.00 USD |
| `1D` | `2137.90` | 593,180,000.00 USD | 0.00 USD | 593,180,000.00 USD | 772,430.00 USD | 1,700,000.00 USD | 943,360.00 USD |
| `7D` | `2140.30` | 597,230,000.00 USD | 0.00 USD | 597,230,000.00 USD | 3,990,000.00 USD | 1,870,000.00 USD | 1,690,000.00 USD |
| `1D` | `2140.40` | 589,760,000.00 USD | 0.00 USD | 589,760,000.00 USD | 2,180,000.00 USD | 1,310,000.00 USD | 1,080,000.00 USD |
| `1D` | `2142.90` | 585,200,000.00 USD | 0.00 USD | 585,200,000.00 USD | 1,080,000.00 USD | 3,170,000.00 USD | 955,950.00 USD |
| `7D` | `2143.10` | 589,680,000.00 USD | 0.00 USD | 589,680,000.00 USD | 2,380,000.00 USD | 618,280.00 USD | 333,410.00 USD |
| `1D` | `2145.40` | 579,990,000.00 USD | 0.00 USD | 579,990,000.00 USD | 3,170,000.00 USD | 2,110,000.00 USD | 1,050,000.00 USD |
| `7D` | `2145.90` | 586,350,000.00 USD | 0.00 USD | 586,350,000.00 USD | 978,940.00 USD | 1,450,000.00 USD | 1,720,000.00 USD |
| `1D` | `2147.90` | 573,660,000.00 USD | 0.00 USD | 573,660,000.00 USD | 728,710.00 USD | 1,050,000.00 USD | 114,470.00 USD |
| `7D` | `2148.70` | 582,200,000.00 USD | 0.00 USD | 582,200,000.00 USD | 26,270.00 USD | 538,910.00 USD | 399,680.00 USD |
| `1D` | `2150.40` | 571,760,000.00 USD | 0.00 USD | 571,760,000.00 USD | 7,890,000.00 USD | 3,310,000.00 USD | 2,660,000.00 USD |
| `7D` | `2151.50` | 581,230,000.00 USD | 0.00 USD | 581,230,000.00 USD | 11,290,000.00 USD | 363,770.00 USD | 107,200.00 USD |
| `1D` | `2152.90` | 557,910,000.00 USD | 0.00 USD | 557,910,000.00 USD | 4,360,000.00 USD | 3,370,000.00 USD | 2,390,000.00 USD |
| `7D` | `2154.30` | 569,470,000.00 USD | 0.00 USD | 569,470,000.00 USD | 2,100,000.00 USD | 3,920,000.00 USD | 1,580,000.00 USD |
| `1D` | `2155.40` | 547,780,000.00 USD | 0.00 USD | 547,780,000.00 USD | 4,430,000.00 USD | 5,320,000.00 USD | 2,380,000.00 USD |
| `7D` | `2157.10` | 561,870,000.00 USD | 0.00 USD | 561,870,000.00 USD | 6,160,000.00 USD | 2,540,000.00 USD | 6,600,000.00 USD |
| `1D` | `2157.90` | 535,660,000.00 USD | 0.00 USD | 535,660,000.00 USD | 4,230,000.00 USD | 2,360,000.00 USD | 4,500,000.00 USD |
| `7D` | `2159.90` | 546,570,000.00 USD | 0.00 USD | 546,570,000.00 USD | 2,980,000.00 USD | 737,260.00 USD | 1,830,000.00 USD |
| `1D` | `2160.40` | 524,570,000.00 USD | 0.00 USD | 524,570,000.00 USD | 4,790,000.00 USD | 6,030,000.00 USD | 2,920,000.00 USD |
| `7D` | `2162.70` | 541,010,000.00 USD | 0.00 USD | 541,010,000.00 USD | 17,980,000.00 USD | 1,960,000.00 USD | 0.00 USD |
| `1D` | `2162.90` | 510,830,000.00 USD | 0.00 USD | 510,830,000.00 USD | 18,720,000.00 USD | 10,660,000.00 USD | 2,590,000.00 USD |
| `1D` | `2165.40` | 478,860,000.00 USD | 0.00 USD | 478,860,000.00 USD | 9,360,000.00 USD | 11,850,000.00 USD | 4,440,000.00 USD |
| `7D` | `2165.50` | 521,070,000.00 USD | 0.00 USD | 521,070,000.00 USD | 8,990,000.00 USD | 17,170,000.00 USD | 2,900,000.00 USD |
| `1D` | `2167.90` | 453,210,000.00 USD | 0.00 USD | 453,210,000.00 USD | 18,870,000.00 USD | 6,950,000.00 USD | 5,130,000.00 USD |
| `7D` | `2168.30` | 492,010,000.00 USD | 0.00 USD | 492,010,000.00 USD | 12,290,000.00 USD | 16,150,000.00 USD | 3,760,000.00 USD |
| `1D` | `2170.40` | 422,260,000.00 USD | 0.00 USD | 422,260,000.00 USD | 24,230,000.00 USD | 8,680,000.00 USD | 7,400,000.00 USD |
| `7D` | `2171.10` | 459,810,000.00 USD | 0.00 USD | 459,810,000.00 USD | 1,860,000.00 USD | 6,380,000.00 USD | 5,570,000.00 USD |
| `1D` | `2172.90` | 381,950,000.00 USD | 0.00 USD | 381,950,000.00 USD | 6,820,000.00 USD | 3,860,000.00 USD | 3,470,000.00 USD |
| `7D` | `2173.90` | 446,010,000.00 USD | 0.00 USD | 446,010,000.00 USD | 35,100,000.00 USD | 0.00 USD | 1,010,000.00 USD |
| `1D` | `2175.40` | 367,820,000.00 USD | 0.00 USD | 367,820,000.00 USD | 3,650,000.00 USD | 85,890.00 USD | 914,480.00 USD |
| `7D` | `2176.70` | 409,900,000.00 USD | 0.00 USD | 409,900,000.00 USD | 0.00 USD | 1,460,000.00 USD | 2,820,000.00 USD |
| `1D` | `2177.90` | 363,170,000.00 USD | 0.00 USD | 363,170,000.00 USD | 1,320,000.00 USD | 783,680.00 USD | 3,350,000.00 USD |
| `7D` | `2179.50` | 405,620,000.00 USD | 0.00 USD | 405,620,000.00 USD | 2,400,000.00 USD | 133,210.00 USD | 4,150,000.00 USD |
| `1D` | `2180.40` | 357,710,000.00 USD | 0.00 USD | 357,710,000.00 USD | 6,480,000.00 USD | 5,550,000.00 USD | 7,600,000.00 USD |
| `7D` | `2182.30` | 398,930,000.00 USD | 0.00 USD | 398,930,000.00 USD | 1,760,000.00 USD | 2,160,000.00 USD | 2,770,000.00 USD |
| `1D` | `2182.90` | 338,090,000.00 USD | 0.00 USD | 338,090,000.00 USD | 1,610,000.00 USD | 2,190,000.00 USD | 3,110,000.00 USD |
| `7D` | `2185.10` | 392,250,000.00 USD | 0.00 USD | 392,250,000.00 USD | 41,350,000.00 USD | 20,450,000.00 USD | 3,070,000.00 USD |
| `1D` | `2185.40` | 331,180,000.00 USD | 0.00 USD | 331,180,000.00 USD | 3,730,000.00 USD | 3,250,000.00 USD | 7,400,000.00 USD |
| `1D` | `2187.90` | 316,810,000.00 USD | 0.00 USD | 316,810,000.00 USD | 7,340,000.00 USD | 4,050,000.00 USD | 7,990,000.00 USD |
| `7D` | `2187.90` | 327,380,000.00 USD | 0.00 USD | 327,380,000.00 USD | 2,370,000.00 USD | 0.00 USD | 1,730,000.00 USD |
| `1D` | `2190.40` | 297,430,000.00 USD | 0.00 USD | 297,430,000.00 USD | 6,760,000.00 USD | 4,660,000.00 USD | 4,130,000.00 USD |
| `7D` | `2190.70` | 323,280,000.00 USD | 0.00 USD | 323,280,000.00 USD | 12,430,000.00 USD | 27,960,000.00 USD | 6,420,000.00 USD |
| `1D` | `2192.90` | 281,880,000.00 USD | 0.00 USD | 281,880,000.00 USD | 6,130,000.00 USD | 5,130,000.00 USD | 1,520,000.00 USD |
| `7D` | `2193.50` | 276,460,000.00 USD | 0.00 USD | 276,460,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,120,000.00 USD |
| `1D` | `2195.40` | 269,110,000.00 USD | 0.00 USD | 269,110,000.00 USD | 6,060,000.00 USD | 2,840,000.00 USD | 5,630,000.00 USD |
| `7D` | `2196.30` | 261,010,000.00 USD | 0.00 USD | 261,010,000.00 USD | 566,810.00 USD | 243,760.00 USD | 109,160.00 USD |
| `1D` | `2197.90` | 254,580,000.00 USD | 0.00 USD | 254,580,000.00 USD | 7,200,000.00 USD | 4,560,000.00 USD | 4,950,000.00 USD |
| `7D` | `2199.10` | 260,090,000.00 USD | 0.00 USD | 260,090,000.00 USD | 4,100,000.00 USD | 5,270,000.00 USD | 7,440,000.00 USD |
| `1D` | `2200.40` | 237,870,000.00 USD | 0.00 USD | 237,870,000.00 USD | 12,020,000.00 USD | 7,180,000.00 USD | 10,520,000.00 USD |
| `7D` | `2201.90` | 243,270,000.00 USD | 0.00 USD | 243,270,000.00 USD | 12,880,000.00 USD | 2,690,000.00 USD | 21,720,000.00 USD |
| `1D` | `2202.90` | 208,150,000.00 USD | 0.00 USD | 208,150,000.00 USD | 16,520,000.00 USD | 16,290,000.00 USD | 19,660,000.00 USD |
| `7D` | `2204.70` | 205,980,000.00 USD | 0.00 USD | 205,980,000.00 USD | 5,350,000.00 USD | 4,330,000.00 USD | 4,660,000.00 USD |
| `1D` | `2205.40` | 155,680,000.00 USD | 0.00 USD | 155,680,000.00 USD | 10,040,000.00 USD | 3,290,000.00 USD | 4,010,000.00 USD |
| `7D` | `2207.50` | 191,640,000.00 USD | 0.00 USD | 191,640,000.00 USD | 19,630,000.00 USD | 3,390,000.00 USD | 7,200,000.00 USD |
| `1D` | `2207.90` | 138,350,000.00 USD | 0.00 USD | 138,350,000.00 USD | 14,640,000.00 USD | 8,140,000.00 USD | 5,770,000.00 USD |
| `7D` | `2210.30` | 161,430,000.00 USD | 0.00 USD | 161,430,000.00 USD | 4,740,000.00 USD | 0.00 USD | 11,560,000.00 USD |
| `1D` | `2210.40` | 109,800,000.00 USD | 0.00 USD | 109,800,000.00 USD | 6,870,000.00 USD | 7,030,000.00 USD | 5,210,000.00 USD |
| `1D` | `2212.90` | 90,670,000.00 USD | 0.00 USD | 90,670,000.00 USD | 8,240,000.00 USD | 5,160,000.00 USD | 2,030,000.00 USD |
| `7D` | `2213.10` | 145,120,000.00 USD | 0.00 USD | 145,120,000.00 USD | 1,710,000.00 USD | 1,980,000.00 USD | 8,850,000.00 USD |
| `1D` | `2215.40` | 75,240,000.00 USD | 0.00 USD | 75,240,000.00 USD | 2,150,000.00 USD | 3,720,000.00 USD | 878,020.00 USD |
| `7D` | `2215.90` | 132,580,000.00 USD | 0.00 USD | 132,580,000.00 USD | 0.00 USD | 0.00 USD | 565,690.00 USD |
| `1D` | `2217.90` | 68,490,000.00 USD | 0.00 USD | 68,490,000.00 USD | 5,090,000.00 USD | 3,410,000.00 USD | 3,300,000.00 USD |
| `7D` | `2218.70` | 132,020,000.00 USD | 0.00 USD | 132,020,000.00 USD | 22,760,000.00 USD | 487,520.00 USD | 218,310.00 USD |
| `1D` | `2220.40` | 56,700,000.00 USD | 0.00 USD | 56,700,000.00 USD | 9,840,000.00 USD | 6,700,000.00 USD | 4,070,000.00 USD |
| `7D` | `2221.50` | 108,550,000.00 USD | 0.00 USD | 108,550,000.00 USD | 8,210,000.00 USD | 19,850,000.00 USD | 18,870,000.00 USD |
| `1D` | `2222.90` | 36,090,000.00 USD | 0.00 USD | 36,090,000.00 USD | 5,350,000.00 USD | 6,360,000.00 USD | 883,270.00 USD |
| `7D` | `2224.30` | 61,620,000.00 USD | 0.00 USD | 61,620,000.00 USD | 7,550,000.00 USD | 4,850,000.00 USD | 6,530,000.00 USD |
| `1D` | `2225.40` | 23,500,000.00 USD | 0.00 USD | 23,500,000.00 USD | 3,470,000.00 USD | 2,560,000.00 USD | 3,260,000.00 USD |
| `7D` | `2227.10` | 42,690,000.00 USD | 0.00 USD | 42,690,000.00 USD | 557,870.00 USD | 0.00 USD | 6,860,000.00 USD |
| `1D` | `2227.90` | 14,200,000.00 USD | 0.00 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 111,560.00 USD |
| `7D` | `2229.90` | 35,270,000.00 USD | 0.00 USD | 35,270,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2230.40` | 14,090,000.00 USD | 0.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 113,200.00 USD |
| `1D` | `2232.90` | 13,970,000.00 USD | 0.00 USD | 13,970,000.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2235.50` | 33,370,000.00 USD | 0.00 USD | 33,370,000.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 0.00 USD |
| `1D` | `2237.90` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2238.30` | 8,470,000.00 USD | 0.00 USD | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2240.40` | 21,970.00 USD | 0.00 USD | 21,970.00 USD | 0.00 USD | 0.00 USD | 21,970.00 USD |
| `7D` | `2241.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2242.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2242.90` | 22,480.00 USD | 22,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,480.00 USD |
| `7D` | `2243.90` | 268,650.00 USD | 268,650.00 USD | 0.00 USD | 0.00 USD | 268,650.00 USD | 0.00 USD |
| `1D` | `2245.40` | 84,720.00 USD | 84,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 62,250.00 USD |
| `7D` | `2246.70` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,300,000.00 USD | 709,510.00 USD |
| `1D` | `2247.90` | 828,620.00 USD | 828,620.00 USD | 0.00 USD | 158,150.00 USD | 286,090.00 USD | 299,650.00 USD |
| `7D` | `2249.50` | 9,970,000.00 USD | 9,970,000.00 USD | 0.00 USD | 2,960,000.00 USD | 2,660,000.00 USD | 867,440.00 USD |
| `1D` | `2250.40` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 7,970,000.00 USD | 458,980.00 USD | 1,680,000.00 USD |
| `7D` | `2252.30` | 35,240,000.00 USD | 35,240,000.00 USD | 0.00 USD | 10,050,000.00 USD | 11,670,000.00 USD | 3,550,000.00 USD |
| `1D` | `2252.90` | 19,050,000.00 USD | 19,050,000.00 USD | 0.00 USD | 1,390,000.00 USD | 3,240,000.00 USD | 3,480,000.00 USD |
| `7D` | `2255.10` | 52,660,000.00 USD | 52,660,000.00 USD | 0.00 USD | 10,050,000.00 USD | 6,600,000.00 USD | 774,210.00 USD |
| `1D` | `2255.40` | 47,360,000.00 USD | 47,360,000.00 USD | 0.00 USD | 15,660,000.00 USD | 6,830,000.00 USD | 5,810,000.00 USD |
| `1D` | `2257.90` | 82,170,000.00 USD | 82,170,000.00 USD | 0.00 USD | 19,650,000.00 USD | 9,290,000.00 USD | 5,870,000.00 USD |
| `7D` | `2257.90` | 92,360,000.00 USD | 92,360,000.00 USD | 0.00 USD | 20,510,000.00 USD | 12,290,000.00 USD | 6,890,000.00 USD |
| `1D` | `2260.40` | 102,520,000.00 USD | 102,520,000.00 USD | 0.00 USD | 8,330,000.00 USD | 9,340,000.00 USD | 2,680,000.00 USD |
| `7D` | `2260.70` | 96,680,000.00 USD | 96,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,320,000.00 USD |
| `1D` | `2262.90` | 138,380,000.00 USD | 138,380,000.00 USD | 0.00 USD | 18,250,000.00 USD | 11,340,000.00 USD | 6,270,000.00 USD |
| `7D` | `2263.50` | 105,440,000.00 USD | 105,440,000.00 USD | 0.00 USD | 7,080,000.00 USD | 1,460,000.00 USD | 218,310.00 USD |
| `1D` | `2265.40` | 172,930,000.00 USD | 172,930,000.00 USD | 0.00 USD | 8,910,000.00 USD | 12,680,000.00 USD | 12,960,000.00 USD |
| `7D` | `2266.30` | 135,770,000.00 USD | 135,770,000.00 USD | 0.00 USD | 8,210,000.00 USD | 15,790,000.00 USD | 6,330,000.00 USD |
| `1D` | `2267.90` | 225,940,000.00 USD | 225,940,000.00 USD | 0.00 USD | 24,280,000.00 USD | 15,840,000.00 USD | 12,900,000.00 USD |
| `7D` | `2269.10` | 183,640,000.00 USD | 183,640,000.00 USD | 0.00 USD | 18,560,000.00 USD | 4,980,000.00 USD | 24,330,000.00 USD |
| `1D` | `2270.40` | 273,190,000.00 USD | 273,190,000.00 USD | 0.00 USD | 14,990,000.00 USD | 12,470,000.00 USD | 19,780,000.00 USD |
| `7D` | `2271.90` | 212,540,000.00 USD | 212,540,000.00 USD | 0.00 USD | 18,240,000.00 USD | 3,640,000.00 USD | 7,010,000.00 USD |
| `1D` | `2272.90` | 300,520,000.00 USD | 300,520,000.00 USD | 0.00 USD | 16,290,000.00 USD | 4,810,000.00 USD | 6,230,000.00 USD |
| `7D` | `2274.70` | 240,840,000.00 USD | 240,840,000.00 USD | 0.00 USD | 19,630,000.00 USD | 6,900,000.00 USD | 1,770,000.00 USD |
| `1D` | `2275.40` | 354,760,000.00 USD | 354,760,000.00 USD | 0.00 USD | 30,720,000.00 USD | 18,900,000.00 USD | 4,620,000.00 USD |
| `7D` | `2277.50` | 267,230,000.00 USD | 267,230,000.00 USD | 0.00 USD | 6,890,000.00 USD | 8,890,000.00 USD | 10,610,000.00 USD |
| `1D` | `2277.90` | 387,640,000.00 USD | 387,640,000.00 USD | 0.00 USD | 6,870,000.00 USD | 10,770,000.00 USD | 15,240,000.00 USD |
| `7D` | `2280.30` | 311,550,000.00 USD | 311,550,000.00 USD | 0.00 USD | 854,200.00 USD | 39,830,000.00 USD | 3,640,000.00 USD |
| `1D` | `2280.40` | 443,160,000.00 USD | 443,160,000.00 USD | 0.00 USD | 31,180,000.00 USD | 15,520,000.00 USD | 8,810,000.00 USD |
| `1D` | `2282.90` | 501,680,000.00 USD | 501,680,000.00 USD | 0.00 USD | 27,530,000.00 USD | 21,080,000.00 USD | 9,910,000.00 USD |
| `7D` | `2283.10` | 403,360,000.00 USD | 403,360,000.00 USD | 0.00 USD | 5,600,000.00 USD | 72,520,000.00 USD | 13,690,000.00 USD |
| `1D` | `2285.40` | 524,400,000.00 USD | 524,400,000.00 USD | 0.00 USD | 8,500,000.00 USD | 9,370,000.00 USD | 4,850,000.00 USD |
| `7D` | `2285.90` | 407,250,000.00 USD | 407,250,000.00 USD | 0.00 USD | 1,190,000.00 USD | 2,590,000.00 USD | 109,160.00 USD |
| `1D` | `2287.90` | 557,680,000.00 USD | 557,680,000.00 USD | 0.00 USD | 14,760,000.00 USD | 9,890,000.00 USD | 8,640,000.00 USD |
| `7D` | `2288.70` | 447,800,000.00 USD | 447,800,000.00 USD | 0.00 USD | 12,490,000.00 USD | 13,140,000.00 USD | 14,930,000.00 USD |
| `1D` | `2290.40` | 603,580,000.00 USD | 603,580,000.00 USD | 0.00 USD | 20,500,000.00 USD | 16,540,000.00 USD | 8,860,000.00 USD |
| `7D` | `2291.50` | 468,970,000.00 USD | 468,970,000.00 USD | 0.00 USD | 8,080,000.00 USD | 2,940,000.00 USD | 10,140,000.00 USD |
| `1D` | `2292.90` | 633,960,000.00 USD | 633,960,000.00 USD | 0.00 USD | 14,730,000.00 USD | 6,010,000.00 USD | 9,630,000.00 USD |
| `7D` | `2294.30` | 490,300,000.00 USD | 490,300,000.00 USD | 0.00 USD | 14,670,000.00 USD | 1,490,000.00 USD | 5,180,000.00 USD |
| `1D` | `2295.40` | 666,300,000.00 USD | 666,300,000.00 USD | 0.00 USD | 11,190,000.00 USD | 13,180,000.00 USD | 7,970,000.00 USD |
| `7D` | `2297.10` | 540,050,000.00 USD | 540,050,000.00 USD | 0.00 USD | 25,900,000.00 USD | 8,070,000.00 USD | 15,780,000.00 USD |
| `1D` | `2297.90` | 715,530,000.00 USD | 715,530,000.00 USD | 0.00 USD | 30,590,000.00 USD | 12,660,000.00 USD | 5,980,000.00 USD |
| `7D` | `2299.90` | 582,970,000.00 USD | 582,970,000.00 USD | 0.00 USD | 16,200,000.00 USD | 20,940,000.00 USD | 5,780,000.00 USD |
| `1D` | `2300.40` | 756,080,000.00 USD | 756,080,000.00 USD | 0.00 USD | 12,140,000.00 USD | 13,230,000.00 USD | 15,190,000.00 USD |
| `7D` | `2302.70` | 637,640,000.00 USD | 637,640,000.00 USD | 0.00 USD | 26,960,000.00 USD | 10,860,000.00 USD | 16,850,000.00 USD |
| `1D` | `2302.90` | 782,960,000.00 USD | 782,960,000.00 USD | 0.00 USD | 16,590,000.00 USD | 3,050,000.00 USD | 7,240,000.00 USD |
| `1D` | `2305.40` | 820,930,000.00 USD | 820,930,000.00 USD | 0.00 USD | 12,570,000.00 USD | 18,050,000.00 USD | 7,340,000.00 USD |
| `7D` | `2305.50` | 663,650,000.00 USD | 663,650,000.00 USD | 0.00 USD | 6,340,000.00 USD | 8,820,000.00 USD | 10,860,000.00 USD |
| `1D` | `2307.90` | 830,210,000.00 USD | 830,210,000.00 USD | 0.00 USD | 4,390,000.00 USD | 2,880,000.00 USD | 2,010,000.00 USD |
| `7D` | `2308.30` | 665,950,000.00 USD | 665,950,000.00 USD | 0.00 USD | 1,240,000.00 USD | 930,630.00 USD | 134,160.00 USD |
| `1D` | `2310.40` | 849,590,000.00 USD | 849,590,000.00 USD | 0.00 USD | 5,980,000.00 USD | 2,740,000.00 USD | 10,660,000.00 USD |
| `7D` | `2311.10` | 696,450,000.00 USD | 696,450,000.00 USD | 0.00 USD | 11,560,000.00 USD | 2,790,000.00 USD | 16,150,000.00 USD |
| `1D` | `2312.90` | 866,610,000.00 USD | 866,610,000.00 USD | 0.00 USD | 6,580,000.00 USD | 8,640,000.00 USD | 1,800,000.00 USD |
| `7D` | `2313.90` | 707,270,000.00 USD | 707,270,000.00 USD | 0.00 USD | 1,100,000.00 USD | 7,460,000.00 USD | 2,260,000.00 USD |
| `1D` | `2315.40` | 893,480,000.00 USD | 893,480,000.00 USD | 0.00 USD | 6,000,000.00 USD | 12,910,000.00 USD | 7,960,000.00 USD |
| `7D` | `2316.70` | 713,030,000.00 USD | 713,030,000.00 USD | 0.00 USD | 1,020,000.00 USD | 3,640,000.00 USD | 1,090,000.00 USD |
| `1D` | `2317.90` | 916,370,000.00 USD | 916,370,000.00 USD | 0.00 USD | 7,580,000.00 USD | 11,210,000.00 USD | 4,110,000.00 USD |
| `7D` | `2319.50` | 743,190,000.00 USD | 743,190,000.00 USD | 0.00 USD | 5,530,000.00 USD | 15,850,000.00 USD | 8,780,000.00 USD |
| `1D` | `2320.40` | 941,600,000.00 USD | 941,600,000.00 USD | 0.00 USD | 10,170,000.00 USD | 11,790,000.00 USD | 3,250,000.00 USD |
| `7D` | `2322.30` | 749,110,000.00 USD | 749,110,000.00 USD | 0.00 USD | 2,300,000.00 USD | 3,450,000.00 USD | 172,940.00 USD |
| `1D` | `2322.90` | 959,930,000.00 USD | 959,930,000.00 USD | 0.00 USD | 4,360,000.00 USD | 9,300,000.00 USD | 4,670,000.00 USD |
| `7D` | `2325.10` | 772,140,000.00 USD | 772,140,000.00 USD | 0.00 USD | 10,150,000.00 USD | 2,770,000.00 USD | 10,120,000.00 USD |
| `1D` | `2325.40` | 973,050,000.00 USD | 973,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 9,550,000.00 USD | 1,530,000.00 USD |
| `1D` | `2327.90` | 979,360,000.00 USD | 979,360,000.00 USD | 0.00 USD | 494,310.00 USD | 1,240,000.00 USD | 4,570,000.00 USD |
| `7D` | `2327.90` | 784,030,000.00 USD | 784,030,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 8,030,000.00 USD |
| `1D` | `2330.40` | 997,900,000.00 USD | 997,900,000.00 USD | 0.00 USD | 13,500,000.00 USD | 3,350,000.00 USD | 1,710,000.00 USD |
| `7D` | `2330.70` | 800,350,000.00 USD | 800,350,000.00 USD | 0.00 USD | 15,890,000.00 USD | 363,770.00 USD | 54,580.00 USD |
| `1D` | `2332.90` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 4,140,000.00 USD | 4,150,000.00 USD | 9,420,000.00 USD |
| `7D` | `2333.50` | 845,400,000.00 USD | 845,400,000.00 USD | 0.00 USD | 22,320,000.00 USD | 14,770,000.00 USD | 7,960,000.00 USD |
| `1D` | `2335.40` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 0.00 USD | 13,620,000.00 USD | 5,030,000.00 USD | 5,970,000.00 USD |
| `7D` | `2336.30` | 887,300,000.00 USD | 887,300,000.00 USD | 0.00 USD | 26,200,000.00 USD | 8,780,000.00 USD | 6,930,000.00 USD |
| `1D` | `2337.90` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 8,210,000.00 USD | 1,950,000.00 USD | 2,740,000.00 USD |
| `7D` | `2339.10` | 913,700,000.00 USD | 913,700,000.00 USD | 0.00 USD | 14,040,000.00 USD | 0.00 USD | 12,370,000.00 USD |
| `1D` | `2340.40` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 10,960,000.00 USD | 6,230,000.00 USD | 12,110,000.00 USD |
| `7D` | `2341.90` | 954,130,000.00 USD | 954,130,000.00 USD | 0.00 USD | 8,610,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD |
| `1D` | `2342.90` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 9,530,000.00 USD | 6,510,000.00 USD | 2,450,000.00 USD |
| `7D` | `2344.70` | 982,050,000.00 USD | 982,050,000.00 USD | 0.00 USD | 2,480,000.00 USD | 16,920,000.00 USD | 8,520,000.00 USD |
| `1D` | `2345.40` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 4,570,000.00 USD | 5,870,000.00 USD | 9,120,000.00 USD |
| `7D` | `2347.50` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 0.00 USD | 8,220,000.00 USD | 18,860,000.00 USD |
| `1D` | `2347.90` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 3,940,000.00 USD | 3,280,000.00 USD | 1,770,000.00 USD |
| `7D` | `2350.30` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 1,630,000.00 USD | 20,110,000.00 USD | 15,150,000.00 USD |
| `1D` | `2350.40` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 26,860,000.00 USD | 7,910,000.00 USD | 10,500,000.00 USD |
| `1D` | `2352.90` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 3,960,000.00 USD | 2,870,000.00 USD | 2,260,000.00 USD |
| `7D` | `2353.10` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 2,710,000.00 USD | 35,770,000.00 USD | 4,640,000.00 USD |
| `1D` | `2355.40` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 3,190,000.00 USD | 3,280,000.00 USD | 951,670.00 USD |
| `7D` | `2355.90` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 18,560,000.00 USD | 10,720,000.00 USD | 3,950,000.00 USD |
| `1D` | `2357.90` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 3,680,000.00 USD | 4,660,000.00 USD | 3,440,000.00 USD |
| `7D` | `2358.70` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 6,870,000.00 USD | 512,220.00 USD | 3,190,000.00 USD |
| `1D` | `2360.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 10,760,000.00 USD | 3,880,000.00 USD | 5,480,000.00 USD |
| `7D` | `2361.50` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,430,000.00 USD | 374,770.00 USD |
| `1D` | `2362.90` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 6,270,000.00 USD | 9,060,000.00 USD | 7,880,000.00 USD |
| `7D` | `2364.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 3,860,000.00 USD | 373,740.00 USD | 10,920,000.00 USD |
| `1D` | `2365.40` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 4,890,000.00 USD | 658,050.00 USD | 3,660,000.00 USD |
| `7D` | `2367.10` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 307,410.00 USD |
| `1D` | `2367.90` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 2,980,000.00 USD | 3,580,000.00 USD | 1,910,000.00 USD |
| `7D` | `2369.90` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 24,940,000.00 USD | 475,460.00 USD | 18,790,000.00 USD |
| `1D` | `2370.40` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 0.00 USD | 14,770,000.00 USD | 5,230,000.00 USD | 5,280,000.00 USD |
| `7D` | `2372.70` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 15,600,000.00 USD | 0.00 USD | 39,640,000.00 USD |
| `1D` | `2372.90` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 11,560,000.00 USD | 2,680,000.00 USD | 6,610,000.00 USD |
| `1D` | `2375.40` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 8,180,000.00 USD | 1,830,000.00 USD | 1,380,000.00 USD |
| `7D` | `2375.50` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 0.00 USD | 9,700,000.00 USD | 1,050,000.00 USD | 11,870,000.00 USD |
| `1D` | `2377.90` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 1,460,000.00 USD | 1,920,000.00 USD | 3,990,000.00 USD |
| `7D` | `2378.30` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 11,180,000.00 USD | 7,020,000.00 USD | 23,870,000.00 USD |
| `1D` | `2380.40` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 6,310,000.00 USD | 5,360,000.00 USD | 5,110,000.00 USD |
| `7D` | `2381.10` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 2,390,000.00 USD | 16,460,000.00 USD |
| `1D` | `2382.90` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 15,730,000.00 USD | 10,890,000.00 USD | 11,420,000.00 USD |
| `7D` | `2383.90` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 8,840,000.00 USD | 21,750,000.00 USD | 30,520,000.00 USD |
| `1D` | `2385.40` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 7,510,000.00 USD | 10,280,000.00 USD | 4,890,000.00 USD |
| `7D` | `2386.70` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 0.00 USD | 17,720,000.00 USD | 32,140,000.00 USD | 42,040,000.00 USD |
| `1D` | `2387.90` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 9,900,000.00 USD | 5,870,000.00 USD | 2,790,000.00 USD |
| `7D` | `2389.50` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 5,670,000.00 USD | 35,860,000.00 USD | 28,760,000.00 USD |
| `1D` | `2390.40` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 4,300,000.00 USD | 3,360,000.00 USD | 1,520,000.00 USD |
| `7D` | `2392.30` | 1,690,000,000.00 USD | 1,690,000,000.00 USD | 0.00 USD | 26,840,000.00 USD | 45,530,000.00 USD | 39,160,000.00 USD |
| `1D` | `2392.90` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 2,700,000.00 USD | 3,990,000.00 USD | 3,320,000.00 USD |
| `7D` | `2395.10` | 1,780,000,000.00 USD | 1,780,000,000.00 USD | 0.00 USD | 39,180,000.00 USD | 24,870,000.00 USD | 29,410,000.00 USD |
| `1D` | `2395.40` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 2,060,000.00 USD | 1,450,000.00 USD | 2,190,000.00 USD |
| `1D` | `2397.90` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 0.00 USD | 64,150.00 USD | 3,720,000.00 USD | 3,380,000.00 USD |
| `7D` | `2397.90` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 0.00 USD | 34,290,000.00 USD | 36,430,000.00 USD | 23,570,000.00 USD |
| `1D` | `2400.40` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 0.00 USD | 2,150,000.00 USD | 637,690.00 USD | 1,390,000.00 USD |
| `7D` | `2400.70` | 1,960,000,000.00 USD | 1,960,000,000.00 USD | 0.00 USD | 42,030,000.00 USD | 25,390,000.00 USD | 24,070,000.00 USD |
| `1D` | `2402.90` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 0.00 USD | 1,140,000.00 USD | 467,060.00 USD | 552,090.00 USD |
| `7D` | `2403.50` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 0.00 USD | 51,300,000.00 USD | 24,760,000.00 USD | 30,980,000.00 USD |
| `1D` | `2405.40` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 0.00 USD | 6,760,000.00 USD | 3,300,000.00 USD | 5,010,000.00 USD |
| `7D` | `2406.30` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 29,700,000.00 USD | 33,710,000.00 USD | 14,210,000.00 USD |
| `1D` | `2407.90` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 0.00 USD | 6,010,000.00 USD | 3,490,000.00 USD | 1,850,000.00 USD |
| `7D` | `2409.10` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 25,090,000.00 USD | 21,480,000.00 USD | 27,910,000.00 USD |
| `1D` | `2410.40` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 0.00 USD | 4,520,000.00 USD | 3,650,000.00 USD | 3,740,000.00 USD |
| `7D` | `2411.90` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 15,970,000.00 USD | 21,640,000.00 USD | 13,990,000.00 USD |
| `1D` | `2412.90` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 0.00 USD | 4,850,000.00 USD | 2,870,000.00 USD | 1,020,000.00 USD |
| `7D` | `2414.70` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 22,250,000.00 USD | 19,630,000.00 USD | 21,720,000.00 USD |
| `1D` | `2415.40` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 0.00 USD | 3,020,000.00 USD | 2,080,000.00 USD | 2,570,000.00 USD |
| `7D` | `2417.50` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 0.00 USD | 22,310,000.00 USD | 8,700,000.00 USD | 21,160,000.00 USD |
| `1D` | `2417.90` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 0.00 USD | 2,330,000.00 USD | 1,820,000.00 USD | 1,250,000.00 USD |
| `7D` | `2420.30` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 0.00 USD | 29,980,000.00 USD | 18,780,000.00 USD | 9,160,000.00 USD |
| `1D` | `2420.40` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 0.00 USD | 6,230,000.00 USD | 2,900,000.00 USD | 4,110,000.00 USD |
| `1D` | `2422.90` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 0.00 USD | 1,070,000.00 USD | 2,790,000.00 USD | 3,130,000.00 USD |
| `7D` | `2423.10` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 0.00 USD | 17,920,000.00 USD | 17,260,000.00 USD | 17,780,000.00 USD |
| `1D` | `2425.40` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 1,280,000.00 USD | 623,850.00 USD | 621,440.00 USD |
| `7D` | `2425.90` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 0.00 USD | 12,980,000.00 USD | 15,010,000.00 USD | 17,380,000.00 USD |
| `1D` | `2427.90` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 1,610,000.00 USD | 1,520,000.00 USD | 609,950.00 USD |
| `7D` | `2428.70` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 0.00 USD | 12,800,000.00 USD | 7,090,000.00 USD | 8,840,000.00 USD |
| `1D` | `2430.40` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 1,330,000.00 USD | 1,550,000.00 USD | 1,360,000.00 USD |
| `7D` | `2431.50` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 0.00 USD | 9,420,000.00 USD | 12,660,000.00 USD | 8,250,000.00 USD |
| `1D` | `2432.90` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 2,680,000.00 USD | 2,230,000.00 USD | 1,030,000.00 USD |
| `7D` | `2434.30` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 0.00 USD | 8,200,000.00 USD | 3,830,000.00 USD | 3,220,000.00 USD |
| `1D` | `2435.40` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 2,480,000.00 USD | 572,900.00 USD | 1,030,000.00 USD |
| `7D` | `2437.10` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 7,130,000.00 USD | 7,440,000.00 USD | 6,120,000.00 USD |
| `1D` | `2437.90` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 1,380,000.00 USD | 1,040,000.00 USD | 15,480.00 USD |
| `7D` | `2439.90` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 12,730,000.00 USD | 4,970,000.00 USD | 3,700,000.00 USD |
| `1D` | `2440.40` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,190,000.00 USD | 863,330.00 USD |
| `7D` | `2442.70` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 5,050,000.00 USD | 5,320,000.00 USD | 7,900,000.00 USD |
| `1D` | `2442.90` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 1,040,000.00 USD | 42,810.00 USD | 751,290.00 USD |
| `1D` | `2445.40` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 218,020.00 USD | 703,990.00 USD | 755,960.00 USD |
| `7D` | `2445.50` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 9,990,000.00 USD | 7,470,000.00 USD | 10,400,000.00 USD |
| `1D` | `2447.90` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 989,540.00 USD | 1,860,000.00 USD |
| `7D` | `2448.30` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 10,750,000.00 USD | 3,620,000.00 USD | 13,290,000.00 USD |
| `1D` | `2450.40` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 1,990,000.00 USD | 73,380.00 USD | 35,990.00 USD |
| `7D` | `2451.10` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 0.00 USD | 8,450,000.00 USD | 7,240,000.00 USD | 7,080,000.00 USD |
| `1D` | `2452.90` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 2,460,000.00 USD | 1,840,000.00 USD | 2,520,000.00 USD |
| `7D` | `2453.90` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 4,220,000.00 USD | 2,980,000.00 USD | 3,970,000.00 USD |
| `1D` | `2455.40` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 1,640,000.00 USD | 2,130,000.00 USD | 916,970.00 USD |
| `7D` | `2456.70` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 5,900,000.00 USD | 7,380,000.00 USD | 7,530,000.00 USD |
| `1D` | `2457.90` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 1,770,000.00 USD | 1,840,000.00 USD | 845,630.00 USD |
| `7D` | `2459.50` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 3,220,000.00 USD | 4,870,000.00 USD | 6,000,000.00 USD |
| `1D` | `2460.40` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 1,560,000.00 USD | 1,410,000.00 USD | 388,420.00 USD |
| `7D` | `2462.30` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 6,600,000.00 USD | 5,990,000.00 USD | 5,150,000.00 USD |
| `1D` | `2462.90` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 330,880.00 USD | 618,870.00 USD | 1,030,000.00 USD |
| `7D` | `2465.10` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 4,900,000.00 USD | 3,130,000.00 USD | 2,820,000.00 USD |
| `1D` | `2465.40` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 1,030,000.00 USD | 345,350.00 USD |
| `1D` | `2467.90` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 732,440.00 USD | 1,550,000.00 USD | 377,900.00 USD |
| `7D` | `2467.90` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 3,720,000.00 USD | 2,330,000.00 USD | 23,760.00 USD |
| `1D` | `2470.40` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 1,650,000.00 USD | 1,590,000.00 USD | 1,800,000.00 USD |
| `7D` | `2470.70` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 4,710,000.00 USD | 2,530,000.00 USD | 1,140,000.00 USD |
| `1D` | `2472.90` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 219,870.00 USD | 92,950.00 USD | 1,120,000.00 USD |
| `7D` | `2473.50` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 0.00 USD | 5,300,000.00 USD | 2,920,000.00 USD | 3,180,000.00 USD |
| `1D` | `2475.40` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 339,190.00 USD | 1,100,000.00 USD | 103,970.00 USD |
| `1D` | `2476.30` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 232,420.00 USD | 0.00 USD | 156,140.00 USD |
| `7D` | `2476.30` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 2,070,000.00 USD | 1,710,000.00 USD | 872,130.00 USD |
| `7D` | `2479.10` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 3,070,000.00 USD | 4,130,000.00 USD | 540,990.00 USD |
| `7D` | `2481.90` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 601,420.00 USD | 3,680,000.00 USD | 1,050,000.00 USD |
| `7D` | `2484.70` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD |
| `7D` | `2487.50` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD |
| `7D` | `2490.30` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 338,890.00 USD | 286,610.00 USD | 0.00 USD |
| `7D` | `2491.80` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 2,580,000.00 USD | 733,870.00 USD | 445,140.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `28.66B` | Total OI Tokens: `12,772,147.0 ETH`
  * 1h OI Change: `+0.59%` | 4h OI Change: `-1.09%` | 24h OI Change: `-5.33%`
  * Exchange Breakdown: Binance=`8.48B` | Bybit=`2.12B` | OKX=`1.75B` | Hyperliquid=`2.33B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `96.98K` | Last 24h: `195.10K` | Last 3d: `5.21M` | Last 7d: `11.81M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0007%` | **USDT OKX** | `0.0009%` |
| **USDT Bybit** | `0.0015%` | **USDT KuCoin** | `-0.0016%` |
| **USDT MEXC** | `0.0006%` | **USDT BingX** | `0.0041%` |
| **USDT Gate** | `0.0074%` | **USDT Bitget** | `0.0042%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0019%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `58.07%` | `41.93%` | `1.38` | 785,610,000.00 USD |
| `15M` | `Binance` | `57.05%` | `42.95%` | `1.33` | 247,260,000.00 USD |
| `15M` | `OKX` | `63.26%` | `36.74%` | `1.72` | 115,580,000.00 USD |
| `15M` | `Bybit` | `67.99%` | `32.01%` | `2.12` | 86,980,000.00 USD |
| `15M` | `KuCoin` | `83.89%` | `16.11%` | `5.21` | 732,310.00 USD |
| `15M` | `Gate` | `46.42%` | `53.58%` | `0.87` | 103,130,000.00 USD |
| `15M` | `Bitget` | `54.2%` | `45.8%` | `1.18` | 35,940,000.00 USD |
| `15M` | `BingX` | `63.1%` | `36.9%` | `1.71` | 17,850,000.00 USD |
| `15M` | `MEXC` | `62.12%` | `37.88%` | `1.64` | 48,550,000.00 USD |
| `15M` | `Bitunix` | `64.95%` | `35.05%` | `1.85` | 30,530,000.00 USD |
| `15M` | `Hyperliquid` | `68.52%` | `31.48%` | `2.18` | 25,010,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `65.65%` | `34.35%` | `1.91` | 5,100,000.00 USD |
| `15M` | `Crypto.com` | `49.03%` | `50.97%` | `0.96` | 2,670,000.00 USD |
| `15M` | `WhiteBIT` | `16.32%` | `83.68%` | `0.20` | 53,100.00 USD |
| `15M` | `HTX` | `72.3%` | `27.7%` | `2.61` | 2,010,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `45.23%` | `54.77%` | `0.83` | 35,120,000.00 USD |
| `15M` | `Bitfinex` | `70.34%` | `29.66%` | `2.37` | 647,180.00 USD |
| `15M` | `Kraken` | `49.63%` | `50.37%` | `0.99` | 7,880,000.00 USD |
| `15M` | `Aster` | `47.41%` | `52.59%` | `0.90` | 13,100,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `52.42%` | `47.58%` | `1.10` | 7,500,000.00 USD |
| `15M` | `Whale Positions` | `57.05%` | `42.95%` | `1.33` | 247,260,000.00 USD |
| `15M` | `Global Accounts` | `58.07%` | `41.93%` | `1.38` | 785,610,000.00 USD |
| `1H` | `ETH` | `50.22%` | `49.78%` | `1.01` | 2,550,000,000.00 USD |
| `1H` | `Binance` | `46.79%` | `53.21%` | `0.88` | 783,220,000.00 USD |
| `1H` | `OKX` | `57.29%` | `42.71%` | `1.34` | 354,980,000.00 USD |
| `1H` | `Bybit` | `48.53%` | `51.47%` | `0.94` | 265,370,000.00 USD |
| `1H` | `KuCoin` | `68.77%` | `31.23%` | `2.20` | 10,450,000.00 USD |
| `1H` | `Gate` | `49.36%` | `50.64%` | `0.97` | 285,790,000.00 USD |
| `1H` | `Bitget` | `44.7%` | `55.3%` | `0.81` | 128,470,000.00 USD |
| `1H` | `BingX` | `57.01%` | `42.99%` | `1.33` | 44,870,000.00 USD |
| `1H` | `MEXC` | `53.6%` | `46.4%` | `1.16` | 141,060,000.00 USD |
| `1H` | `Bitunix` | `51.77%` | `48.23%` | `1.07` | 125,430,000.00 USD |
| `1H` | `Hyperliquid` | `62.41%` | `37.59%` | `1.66` | 132,680,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.88%` | `50.12%` | `1.00` | 22,940,000.00 USD |
| `1H` | `Crypto.com` | `47.39%` | `52.61%` | `0.90` | 9,770,000.00 USD |
| `1H` | `WhiteBIT` | `11.38%` | `88.62%` | `0.13` | 11,050,000.00 USD |
| `1H` | `HTX` | `45.23%` | `54.77%` | `0.83` | 10,370,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `46.16%` | `53.84%` | `0.86` | 125,200,000.00 USD |
| `1H` | `Bitfinex` | `60.14%` | `39.86%` | `1.51` | 2,280,000.00 USD |
| `1H` | `Kraken` | `52.92%` | `47.08%` | `1.12` | 26,680,000.00 USD |
| `1H` | `Aster` | `39.65%` | `60.35%` | `0.66` | 37,430,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `55.53%` | `44.47%` | `1.25` | 24,950,000.00 USD |
| `1H` | `Whale Positions` | `46.79%` | `53.21%` | `0.88` | 783,220,000.00 USD |
| `1H` | `Global Accounts` | `50.22%` | `49.78%` | `1.01` | 2,550,000,000.00 USD |
| `4H` | `ETH` | `45.81%` | `54.19%` | `0.85` | 10,680,000,000.00 USD |
| `4H` | `Binance` | `44.32%` | `55.68%` | `0.80` | 3,120,000,000.00 USD |
| `4H` | `OKX` | `48.74%` | `51.26%` | `0.95` | 1,520,000,000.00 USD |
| `4H` | `Bybit` | `44.25%` | `55.75%` | `0.79` | 949,910,000.00 USD |
| `4H` | `KuCoin` | `54.02%` | `45.98%` | `1.17` | 28,700,000.00 USD |
| `4H` | `Gate` | `49.87%` | `50.13%` | `0.99` | 1,060,000,000.00 USD |
| `4H` | `Bitget` | `43.18%` | `56.82%` | `0.76` | 485,900,000.00 USD |
| `4H` | `BingX` | `45.87%` | `54.13%` | `0.85` | 214,440,000.00 USD |
| `4H` | `MEXC` | `46.06%` | `53.94%` | `0.85` | 509,020,000.00 USD |
| `4H` | `Bitunix` | `46.57%` | `53.43%` | `0.87` | 433,770,000.00 USD |
| `4H` | `Hyperliquid` | `40.18%` | `59.82%` | `0.67` | 604,760,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.75%` | `49.25%` | `1.03` | 704,930,000.00 USD |
| `4H` | `Crypto.com` | `45.14%` | `54.86%` | `0.82` | 34,650,000.00 USD |
| `4H` | `WhiteBIT` | `15.15%` | `84.85%` | `0.18` | 184,870,000.00 USD |
| `4H` | `HTX` | `44.73%` | `55.27%` | `0.81` | 36,720,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.54%` | `48.46%` | `1.06` | 508,980,000.00 USD |
| `4H` | `Bitfinex` | `46.99%` | `53.01%` | `0.89` | 6,020,000.00 USD |
| `4H` | `Kraken` | `47.18%` | `52.82%` | `0.89` | 56,020,000.00 USD |
| `4H` | `Aster` | `44.93%` | `55.07%` | `0.82` | 105,290,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.79%` | `48.21%` | `1.07` | 107,440,000.00 USD |
| `4H` | `Whale Positions` | `44.32%` | `55.68%` | `0.80` | 3,120,000,000.00 USD |
| `4H` | `Global Accounts` | `45.81%` | `54.19%` | `0.85` | 10,680,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `2224.25` | `2226.52` | `2224.25` | `2230.75` | `2223.25` | 103,679,050.63 USD | 41,811,152.44 USD | 61,867,898.19 USD | -20,056,745.75 USD | `-19.35%` | `0B / 2S` |
| `5:00 UTC` | `2223.75` | `2226.83` | `2223.75` | `2231.75` | `2223.25` | 59,922,094.97 USD | 29,249,984.51 USD | 30,672,110.46 USD | -1,422,125.96 USD | `-2.37%` | `1B / 1S` |
| `0:00 UTC` | `2222.75` | `2224.81` | `2222.75` | `2229.75` | `2221.25` | 65,855,959.19 USD | 30,261,207.11 USD | 35,594,752.09 USD | -5,333,544.98 USD | `-8.10%` | `0B / 4S` |
| `5:00 UTC` | `2221.75` | `2223.05` | `2221.75` | `2226.25` | `2220.25` | 71,858,619.15 USD | 38,686,757.89 USD | 33,171,861.26 USD | 5,514,896.63 USD | `+7.67%` | `0B / 0S` |
| `0:00 UTC` | `2229.25` | `2226.54` | `2229.25` | `2231.25` | `2220.25` | 81,297,282.61 USD | 40,950,851.56 USD | 40,346,431.05 USD | 604,420.51 USD | `+0.74%` | `0B / 2S` |
| `5:00 UTC` | `2227.25` | `2227.77` | `2227.25` | `2229.75` | `2226.25` | 53,422,952.94 USD | 29,109,463.85 USD | 24,313,489.09 USD | 4,795,974.76 USD | `+8.98%` | `1B / 0S` |
| `0:00 UTC` | `2223.75` | `2224.01` | `2223.75` | `2228.25` | `2221.75` | 56,423,190.50 USD | 27,667,054.76 USD | 28,756,135.74 USD | -1,089,080.98 USD | `-1.93%` | `0B / 3S` |
| `5:00 UTC` | `2222.25` | `2225.79` | `2222.25` | `2230.75` | `2220.25` | 60,731,653.97 USD | 32,744,113.06 USD | 27,987,540.91 USD | 4,756,572.15 USD | `+7.83%` | `4B / 1S` |
| `0:00 UTC` | `2245.25` | `2240.77` | `2245.25` | `2248.75` | `2228.25` | 194,501,635.59 USD | 112,910,472.81 USD | 81,591,162.78 USD | 31,319,310.03 USD | `+16.10%` | `7B / 0S` |
| `5:00 UTC` | `2241.25` | `2242.25` | `2241.25` | `2245.25` | `2240.75` | 27,837,807.63 USD | 7,410,954.01 USD | 20,426,853.62 USD | -13,015,899.61 USD | `-46.76%` | `0B / 5S` |

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
| `5m` | 4,610,000.00 USD | -4,110,000.00 USD | **`ACCUMULATION`** |
| `15m` | 11,710,000.00 USD | 71,040,000.00 USD | **`ACCUMULATION`** |
| `30m` | 7,030,000.00 USD | 72,140,000.00 USD | **`ACCUMULATION`** |
| `1h` | -385,260.00 USD | 73,210,000.00 USD | **`ACCUMULATION`** |
| `2h` | -16,580,000.00 USD | 44,730,000.00 USD | **`ACCUMULATION`** |
| `4h` | -15,920,000.00 USD | -51,670,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -4,520,000.00 USD | -19,170,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -4,070,000.00 USD | -153,190,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -69,450,000.00 USD | -615,430,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -148,290,000.00 USD | -1,890,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -220,180,000.00 USD | -3,010,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,180,000,000.00 USD | -9,750,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+4.61M` | 15m=`+11.71M` | 1h=`-385.26K` | 24h=`-148.29M`
* Futures Capital Netflows: 5m=`-4.11M` | 15m=`+71.04M` | 1h=`+73.21M` | 24h=`-1.89B`
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
  * `2026-10-30 15:50:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2196.43` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2178.66` (Risk Distance: `17.77` pts)
  * +2.5R Take Profit: `2240.86`
  * Mathematical Lot Sizing: **`0.56 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2251.47` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2269.24` (Risk Distance: `17.77` pts)
  * +2.5R Take Profit: `2207.04`
  * Mathematical Lot Sizing: **`0.56 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2259.78`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
