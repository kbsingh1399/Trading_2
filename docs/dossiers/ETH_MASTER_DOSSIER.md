# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 17:22:13 IST` (`2026-10-30 11:52:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2230.00` | **Live Ask Quote**: `2233.60` | **Mid Price**: `2231.80`
- **Spread Points**: `360.00` | **Spread BPS**: `16.13 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2221.20` | VWAP Z-Score: `+0.79` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `11.31` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.64` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2269.74` | Lower -3.00σ Band: `2172.66`
  * Upper +2.51σ Band: `2261.81` | Lower -2.51σ Band: `2180.58`
  * Upper +2.01σ Band: `2253.72` | Lower -2.01σ Band: `2188.67`
  * Upper +2.00σ Band: `2253.56` | Lower -2.00σ Band: `2188.84`
  * Upper +1.28σ Band: `2241.91` | Lower -1.28σ Band: `2200.48`
  * Upper +1.00σ Band: `2237.38` | Lower -1.00σ Band: `2205.02`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2234.93` | EMA-20=`2232.68` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2240.51` (Slope: `+0.0000`) | EMA-100=`2261.60`
  * Institutional Anchors: EMA-144=`2275.36` | EMA-200=`2288.81` (Slope: `-0.3233`) | EMA-233=`2293.98`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2249.85` (Distance: `-0.80%`)
  * Point of Control (POC) = `2241.75` (Distance: `-0.44%`)
  * Value Area Low (VAL) = `2196.43` (Distance: `+1.61%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2356.25` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2251.30` | Low=`2215.10`
  * New York Session (13:00-21:00 UTC): High=`2247.90` | Low=`2216.10`
  * Initial Balance (First Hour): IB High=`2246.50` | IB Low=`2230.60`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2222.87` - `2240.73`
  * Optimal Trade Entry (OTE 0.705): `2236.26`
  * Structural Invalidation Anchor (0.786): `2249.65`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2241.94` | `2242.57` | `2237.22` | `2237.79` | `13,794` | 30,894,263.10 USD | -8,403,842.73 USD | `-27.20%` | -933,363,863.61 USD | `-1.27` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `2237.79` | `2239.90` | `2233.10` | `2233.21` | `22,059` | 49,318,576.85 USD | -7,105,136.45 USD | `-14.41%` | -940,469,000.06 USD | `-0.99` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `2233.20` | `2234.21` | `2233.19` | `2234.09` | `1,307` | 2,919,813.77 USD | -368,291.16 USD | `-12.61%` | -940,837,291.22 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2244.15` | `2248.38` | `2240.99` | `2247.53` | `19,635` | 44,075,480.00 USD | -5,110,460.93 USD | `-11.59%` | -906,344,981.73 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2247.53` | `2248.81` | `2237.22` | `2237.79` | `29,120` | 65,303,286.98 USD | -17,885,225.63 USD | `-27.39%` | -924,230,207.36 USD | `-0.92` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2237.79` | `2239.90` | `2233.10` | `2234.09` | `23,366` | 52,238,390.61 USD | -7,473,427.61 USD | `-14.31%` | -931,703,634.97 USD | `-0.30` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2227.92` | `2231.18` | `2220.24` | `2228.42` | `122,419` | 272,434,813.90 USD | 5,581,746.93 USD | `+2.05%` | -920,109,678.48 USD | `+0.46` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `2228.43` | `2248.56` | `2220.36` | `2248.40` | `178,179` | 398,534,292.30 USD | 25,797,692.56 USD | `+6.47%` | -894,311,985.92 USD | `+0.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2248.40` | `2251.73` | `2233.10` | `2234.09` | `104,329` | 233,984,971.32 USD | -37,391,649.05 USD | `-15.98%` | -931,703,634.97 USD | `+0.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2251.73` | `2220.24` | `2234.10` | `569,154` | 1,270,893,041.62 USD | -43,793,307.05 USD | `-3.45%` | -931,659,375.50 USD | `+0.51` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -98,115,944.70 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -652,353,514.01 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2251.73` | `2220.24` | `2234.10` | `569,154` | 1,270,893,041.62 USD | -43,793,307.05 USD | `-3.45%` | -931,659,375.50 USD | `+0.51` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`2231.80`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2232.10` | `297.2119` | 663,406.68 USD | 12,159,655.31 USD | `6 orders` | `-0.09%` | `-` |
| `BID` | `2232.20` | `451.3982` | 1,007,611.06 USD | 11,496,248.63 USD | `11 orders` | `-0.08%` | `-` |
| `BID` | `2232.30` | `154.3405` | 344,534.30 USD | 10,488,637.56 USD | `9 orders` | `-0.08%` | `-` |
| `BID` | `2232.40` | `131.4758` | 293,506.58 USD | 10,144,103.27 USD | `8 orders` | `-0.07%` | `-` |
| `BID` | `2232.50` | `529.7486` | 1,182,663.75 USD | 9,850,596.69 USD | `10 orders` | `-0.07%` | `-` |
| `BID` | `2232.60` | `123.5864` | 275,919.00 USD | 8,667,932.94 USD | `7 orders` | `-0.06%` | `-` |
| `BID` | `2232.70` | `103.2500` | 230,526.27 USD | 8,392,013.94 USD | `10 orders` | `-0.06%` | `-` |
| `BID` | `2232.80` | `100.1354` | 223,582.32 USD | 8,161,487.67 USD | `10 orders` | `-0.06%` | `-` |
| `BID` | `2232.90` | `189.0148` | 422,051.15 USD | 7,937,905.35 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `2233.00` | `472.9024` | 1,055,991.06 USD | 7,515,854.20 USD | `15 orders` | `-0.05%` | `-` |
| `BID` | `2233.10` | `472.6814` | 1,055,544.83 USD | 6,459,863.14 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `2233.20` | `181.6220` | 405,598.25 USD | 5,404,318.31 USD | `10 orders` | `-0.04%` | `-` |
| `BID` | `2233.30` | `145.7238` | 325,444.96 USD | 4,998,720.06 USD | `9 orders` | `-0.03%` | `-` |
| `BID` | `2233.40` | `378.3809` | 845,075.90 USD | 4,673,275.09 USD | `10 orders` | `-0.03%` | `-` |
| `BID` | `2233.50` | `280.6095` | 626,741.32 USD | 3,828,199.19 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `2233.60` | `305.0512` | 681,362.36 USD | 3,201,457.87 USD | `10 orders` | `-0.02%` | `-` |
| `BID` | `2233.70` | `279.6331` | 624,616.46 USD | 2,520,095.51 USD | `10 orders` | `-0.02%` | `-` |
| `BID` | `2233.80` | `378.1868` | 844,793.67 USD | 1,895,479.06 USD | `10 orders` | `-0.01%` | `-` |
| `BID` | `2233.90` | `251.3382` | 561,464.40 USD | 1,050,685.38 USD | `7 orders` | `-0.01%` | `-` |
| `BID` | `2234.00` | `218.9888` | 489,220.98 USD | 489,220.98 USD | `25 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2234.05` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,234.05` | `0.00%` | `-` |
| `ASK` | `2234.10` | `17.3700` | 38,806.32 USD | 38,806.32 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `2234.20` | `4.0246` | 8,991.76 USD | 47,798.08 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `2234.30` | `29.2777` | 65,415.17 USD | 113,213.24 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `2234.40` | `82.9877` | 185,427.72 USD | 298,640.96 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `2234.50` | `84.8115` | 189,511.30 USD | 488,152.26 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `2234.60` | `102.7039` | 229,502.13 USD | 717,654.39 USD | `8 orders` | `+0.02%` | `-` |
| `ASK` | `2234.70` | `122.6536` | 274,094.00 USD | 991,748.39 USD | `10 orders` | `+0.03%` | `-` |
| `ASK` | `2234.80` | `194.5152` | 434,702.57 USD | 1,426,450.96 USD | `12 orders` | `+0.03%` | `-` |
| `ASK` | `2234.90` | `247.3433` | 552,787.54 USD | 1,979,238.50 USD | `11 orders` | `+0.04%` | `-` |
| `ASK` | `2235.00` | `276.3248` | 617,585.93 USD | 2,596,824.43 USD | `20 orders` | `+0.04%` | `-` |
| `ASK` | `2235.10` | `548.5638` | 1,226,094.95 USD | 3,822,919.38 USD | `11 orders` | `+0.05%` | `-` |
| `ASK` | `2235.20` | `632.2311` | 1,413,162.95 USD | 5,236,082.33 USD | `13 orders` | `+0.05%` | `-` |
| `ASK` | `2235.30` | `312.0510` | 697,527.60 USD | 5,933,609.93 USD | `21 orders` | `+0.06%` | `-` |
| `ASK` | `2235.40` | `131.0604` | 292,972.42 USD | 6,226,582.35 USD | `15 orders` | `+0.06%` | `-` |
| `ASK` | `2235.50` | `346.7062` | 775,061.71 USD | 7,001,644.06 USD | `14 orders` | `+0.06%` | `-` |
| `ASK` | `2235.60` | `339.1861` | 758,284.45 USD | 7,759,928.51 USD | `11 orders` | `+0.07%` | `-` |
| `ASK` | `2235.70` | `609.8711` | 1,363,488.82 USD | 9,123,417.33 USD | `9 orders` | `+0.07%` | `-` |
| `ASK` | `2235.80` | `198.9195` | 444,744.22 USD | 9,568,161.54 USD | `9 orders` | `+0.08%` | `-` |
| `ASK` | `2235.90` | `17.0802` | 38,189.62 USD | 9,606,351.16 USD | `6 orders` | `+0.08%` | `-` |
| `ASK` | `2236.00` | `704.0517` | 1,574,259.60 USD | 11,180,610.76 USD | `13 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 17:20:49 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1843.87` | `7,964.66` | 14,685,805.43 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 17:20:49 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1913.13` | `6,500.22` | 12,435,749.27 USD | `AT_RISK_LIQ` | `0xf78c5d8d4b` | `2026-10-30 17:20:49 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1929.89` | `8,092.45` | 15,617,516.47 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 17:20:49 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2121.82` | `30,641.99` | 65,016,792.34 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 17:20:49 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.10` | `26,025.05` | 55,409,882.62 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 17:20:49 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,533.33` | 7,684,999.71 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2191.10` | `500.00` | 1,095,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 17:20:49 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2195.00` | `839.60` | 1,842,926.39 USD | `TRIGGER_STOP` | `0x28280399d9` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2196.60` | `2,114.57` | 4,644,866.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.00` | `506.76` | 1,115,374.36 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.10` | `500.00` | 1,100,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2202.50` | `4,231.56` | 9,320,008.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2207.60` | `1,502.54` | 3,317,013.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2210.30` | `344.72` | 761,925.55 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2210.80` | `359.47` | 794,719.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.10` | `500.00` | 1,105,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2215.60` | `430.01` | 952,735.03 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2216.50` | `506.17` | 1,121,934.67 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2216.90` | `2,182.59` | 4,838,591.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2218.50` | `981.70` | 2,177,905.44 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 17:20:49 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2219.00` | `439.90` | 976,147.64 USD | `TRIGGER_STOP` | `0x369fd6445f` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2222.00` | `1,802.68` | 4,005,565.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2222.10` | `732.26` | 1,627,157.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2222.60` | `506.68` | 1,126,146.97 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2223.50` | `341.54` | 759,417.97 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2224.20` | `474.07` | 1,054,424.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2224.40` | `1,350.52` | 3,004,099.13 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2225.00` | `689.77` | 1,534,730.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2225.00` | `344.01` | 765,421.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.40` | `899.53` | 2,002,722.72 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.80` | `1,112.20` | 2,476,640.72 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2228.20` | `334.73` | 745,836.92 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2228.60` | `674.01` | 1,502,089.10 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2231.20` | `448.80` | 1,001,361.67 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 17:20:49 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2234.00` | `465.08` | 1,038,983.58 USD | `TRIGGER_STOP` | `0x0903f51b01` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2236.30` | `335.86` | 751,082.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2237.00` | `447.65` | 1,001,383.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2238.40` | `671.05` | 1,502,080.78 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2240.60` | `491.95` | 1,102,265.19 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2241.80` | `893.36` | 2,002,742.74 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2242.00` | `1,113.57` | 2,496,619.90 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2243.30` | `473.80` | 1,062,864.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.30` | `1,338.57` | 3,004,144.57 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2245.10` | `344.01` | 772,336.40 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2245.30` | `689.79` | 1,548,792.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2246.00` | `1,783.40` | 4,005,506.74 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2246.20` | `506.82` | 1,138,410.10 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2252.20` | `430.01` | 968,473.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2252.30` | `2,179.91` | 4,909,802.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2252.50` | `506.76` | 1,141,488.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2253.30` | `980.88` | 2,210,217.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2257.00` | `352.11` | 794,719.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2257.00` | `337.58` | 761,925.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2262.40` | `1,475.11` | 3,337,293.62 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2263.90` | `4,231.56` | 9,579,825.97 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2268.30` | `506.67` | 1,149,277.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.70` | `620.97` | 1,409,408.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.10` | `2,003.63` | 4,552,449.31 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 17:20:49 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.20` | `2,200.51` | 4,999,999.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb1ec7febea` | `2026-10-30 17:20:49 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2300.00` | `4,002.10` | 9,204,832.99 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 17:20:49 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2474.03` | `22,046.99` | 54,544,867.42 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 17:20:49 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,002.39` | 7,547,704.95 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 17:20:49 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2541.00` | `400.00` | 1,016,400.00 USD | `TRIGGER_STOP` | `0xbef32b1382` | `2026-10-30 17:20:49 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2584.93` | `6,224.05` | 16,088,712.55 USD | `AT_RISK_LIQ` | `0x08bf75d170` | `2026-10-30 17:20:49 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2601.00` | `400.00` | 1,040,400.00 USD | `TRIGGER_STOP` | `0xbef32b1382` | `2026-10-30 17:20:49 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 230,477,720.92 USD | `102,676.40` | `2322.74` | `2244.80` | `3709.78` | 8,013,192.23 USD | `+3.48%` | `5X Cross` |
| `6` | `0xb83d...6e36` | `SHORT` | 100,061,797.50 USD | `44,580.89` | `2375.30` | `2244.80` | `4647.10` | 5,831,469.54 USD | `+5.83%` | `5X Cross` |
| `9` | `0x77dd...e0e9` | `LONG` | 68,782,078.77 USD | `30,641.99` | `2610.31` | `2244.80` | `2121.85` | -11,203,096.27 USD | `-16.29%` | `10X Cross` |
| `10` | `0xde8d...9524` | `LONG` | 67,974,911.14 USD | `30,282.40` | `2134.45` | `2244.80` | `1786.11` | 3,338,580.56 USD | `+4.91%` | `20X Cross` |
| `15` | `0x0392...d7d9` | `LONG` | 58,418,432.20 USD | `26,025.05` | `2518.71` | `2244.80` | `2129.13` | -7,131,289.88 USD | `-12.21%` | `9X Cross` |
| `22` | `0x8add...7d2c` | `SHORT` | 49,485,127.77 USD | `22,046.99` | `2271.09` | `2244.80` | `2476.44` | 585,769.53 USD | `+1.18%` | `25X Cross` |
| `25` | `0x15a4...dfdb` | `SHORT` | 44,900,000.00 USD | `20,000.00` | `2228.11` | `2244.80` | `3187.81` | -337,672.32 USD | `-0.75%` | `20X Cross` |
| `26` | `0xdf95...7d72` | `SHORT` | 44,248,921.71 USD | `19,712.62` | `2402.53` | `2244.80` | `4223.34` | 3,111,333.08 USD | `+7.03%` | `25X Cross` |
| `33` | `0x6046...b21d` | `LONG` | 35,754,253.36 USD | `15,927.59` | `2410.19` | `2244.80` | `1784.33` | -2,634,366.29 USD | `-7.37%` | `6X Cross` |
| `34` | `0xefe4...194b` | `SHORT` | 33,917,953.00 USD | `15,108.89` | `2250.33` | `2244.80` | `2886.54` | 82,063.75 USD | `+0.24%` | `20X Cross` |
| `37` | `0xb695...a92d` | `SHORT` | 33,211,977.38 USD | `14,795.73` | `2557.74` | `2244.80` | `3777.95` | 4,631,736.74 USD | `+13.95%` | `20X Cross` |
| `38` | `0xeced...6210` | `SHORT` | 32,966,705.63 USD | `14,687.58` | `2522.09` | `2244.80` | `3655.48` | 4,076,811.90 USD | `+12.37%` | `20X Cross` |
| `40` | `0x45d2...4029` | `SHORT` | 31,313,565.00 USD | `13,950.00` | `2443.60` | `2244.80` | `5286.36` | 2,774,717.46 USD | `+8.86%` | `20X Cross` |
| `42` | `0xa61c...66b9` | `LONG` | 28,932,271.20 USD | `12,888.00` | `2369.69` | `2244.80` | `1509.87` | -1,608,383.34 USD | `-5.56%` | `10X Cross` |
| `44` | `0xbd1c...ff0e` | `LONG` | 26,936,400.00 USD | `12,000.00` | `2419.91` | `2244.80` | `1519.99` | -2,102,632.39 USD | `-7.81%` | `20X Cross` |
| `45` | `0x2371...0883` | `LONG` | 26,934,000.00 USD | `12,000.00` | `2421.77` | `2244.80` | `1279.08` | -2,127,294.85 USD | `-7.90%` | `20X Cross` |
| `52` | `0x0c5d...36b3` | `LONG` | 24,698,300.00 USD | `11,000.00` | `2482.20` | `2244.80` | `1644.06` | -2,605,953.24 USD | `-10.55%` | `20X Cross` |
| `53` | `0xa9de...e049` | `LONG` | 24,695,000.00 USD | `11,000.00` | `2481.81` | `2244.80` | `1643.73` | -2,604,979.46 USD | `-10.55%` | `20X Cross` |
| `54` | `0x6c93...59a4` | `LONG` | 24,692,800.00 USD | `11,000.00` | `2441.15` | `2244.80` | `1602.02` | -2,159,872.73 USD | `-8.75%` | `20X Cross` |
| `55` | `0x09dc...c094` | `LONG` | 24,689,500.00 USD | `11,000.00` | `2465.31` | `2244.80` | `1637.05` | -2,428,923.04 USD | `-9.84%` | `20X Cross` |
| `60` | `0xecb6...2b00` | `SHORT` | 23,791,639.67 USD | `10,598.08` | `2238.88` | `2244.80` | `5472.96` | -63,778.82 USD | `-0.27%` | `15X Cross` |
| `72` | `0xa2ce...3126` | `LONG` | 22,482,876.39 USD | `10,016.88` | `2162.83` | `2244.80` | `1556.97` | 818,074.34 USD | `+3.64%` | `10X Cross` |
| `73` | `0x6646...6de5` | `LONG` | 22,445,000.00 USD | `10,000.00` | `1765.80` | `2244.80` | `1722.35` | 4,786,942.55 USD | `+21.33%` | `25X Cross` |
| `74` | `0xec7f...df39` | `LONG` | 22,445,000.00 USD | `10,000.00` | `2719.35` | `2244.80` | `1720.58` | -4,748,548.52 USD | `-21.16%` | `20X Cross` |
| `76` | `0x939f...04d2` | `LONG` | 22,052,495.20 USD | `9,823.81` | `2427.28` | `2244.80` | `1765.57` | -1,792,655.40 USD | `-8.13%` | `25X Cross` |
| `83` | `0xf517...c032` | `SHORT` | 20,936,716.60 USD | `9,326.35` | `2202.91` | `2244.80` | `3168.14` | -391,578.39 USD | `-1.87%` | `25X Cross` |
| `85` | `0xca49...53c8` | `SHORT` | 20,610,581.52 USD | `9,181.89` | `2549.39` | `2244.80` | `3898.17` | 2,797,695.86 USD | `+13.57%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 20,322,248.68 USD | `9,054.12` | `2493.89` | `2244.80` | `2764.10` | 2,257,758.58 USD | `+11.11%` | `20X Cross` |
| `88` | `0xea00...a918` | `LONG` | 20,210,888.90 USD | `9,003.83` | `2003.01` | `2244.80` | `1416.30` | 2,176,110.03 USD | `+10.77%` | `5X Cross` |
| `106` | `0x0622...8088` | `SHORT` | 18,690,447.44 USD | `8,325.74` | `2233.13` | `2244.80` | `3376.52` | -97,944.11 USD | `-0.52%` | `5X Cross` |
| `114` | `0x9eec...daab` | `LONG` | 18,165,127.23 USD | `8,092.45` | `1658.44` | `2244.80` | `1930.23` | 4,744,262.70 USD | `+26.12%` | `15X Cross` |
| `115` | `0x5f91...65aa` | `LONG` | 17,878,263.10 USD | `7,964.66` | `1626.99` | `2244.80` | `1843.90` | 4,919,820.03 USD | `+27.52%` | `16X Cross` |
| `122` | `0xec0b...b078` | `LONG` | 15,731,807.75 USD | `7,007.80` | `2065.97` | `2244.80` | `1068.50` | 1,253,878.16 USD | `+7.97%` | `25X Cross` |
| `130` | `0xf02d...5eb3` | `LONG` | 15,391,001.85 USD | `6,855.99` | `2383.33` | `2244.80` | `1114.19` | -949,086.92 USD | `-6.17%` | `20X Cross` |
| `132` | `0xcf53...ee11` | `SHORT` | 15,270,742.82 USD | `6,803.63` | `1862.69` | `2244.80` | `4195.84` | -2,597,637.43 USD | `-17.01%` | `7X Cross` |
| `137` | `0x4ff9...38d3` | `LONG` | 14,733,316.46 USD | `6,564.10` | `2447.40` | `2244.80` | `1669.67` | -1,331,706.29 USD | `-9.04%` | `3X Isolated` |
| `139` | `0xf78c...c581` | `LONG` | 14,592,477.25 USD | `6,500.22` | `2521.53` | `2244.80` | `1913.16` | -1,798,063.70 USD | `-12.32%` | `20X Cross` |
| `140` | `0x1ee7...edf5` | `LONG` | 14,591,980.00 USD | `6,500.00` | `2301.55` | `2244.80` | `2068.89` | -368,113.66 USD | `-2.52%` | `25X Cross` |
| `143` | `0x4e23...20c3` | `LONG` | 14,289,481.95 USD | `6,365.31` | `2228.10` | `2244.80` | `284.30` | 106,904.51 USD | `+0.75%` | `20X Cross` |
| `144` | `0x799f...5f4c` | `LONG` | 14,167,346.82 USD | `6,310.90` | `2390.33` | `2244.80` | `1866.78` | -917,817.80 USD | `-6.48%` | `20X Cross` |
| `148` | `0x08bf...7872` | `SHORT` | 13,971,741.60 USD | `6,224.05` | `2258.00` | `2244.80` | `2584.96` | 82,174.50 USD | `+0.59%` | `20X Cross` |
| `154` | `0xec4a...cf62` | `LONG` | 13,623,215.61 USD | `6,068.52` | `2223.80` | `2244.80` | `1960.61` | 128,000.29 USD | `+0.94%` | `25X Cross` |
| `155` | `0x524e...0de0` | `LONG` | 13,469,400.00 USD | `6,000.00` | `2246.48` | `2244.80` | `2002.86` | -9,485.04 USD | `-0.07%` | `10X Cross` |
| `156` | `0xd9e7...4aff` | `LONG` | 13,468,800.00 USD | `6,000.00` | `2480.18` | `2244.80` | `1407.44` | -1,412,324.33 USD | `-10.49%` | `20X Cross` |
| `157` | `0xc179...e0c8` | `LONG` | 13,143,284.72 USD | `5,854.73` | `2294.94` | `2244.80` | `1203.76` | -292,987.45 USD | `-2.23%` | `10X Cross` |
| `161` | `0x0c4a...1b19` | `LONG` | 12,704,258.64 USD | `5,660.10` | `2373.06` | `2244.80` | `2081.49` | -727,499.49 USD | `-5.73%` | `25X Isolated` |
| `185` | `0x45ab...6cbc` | `LONG` | 11,051,989.01 USD | `4,920.96` | `2727.66` | `2244.80` | `1376.22` | -2,370,754.79 USD | `-21.45%` | `7X Cross` |
| `189` | `0x64b7...9da9` | `LONG` | 10,903,118.32 USD | `4,856.84` | `2604.61` | `2244.80` | `595.29` | -1,747,096.09 USD | `-16.02%` | `25X Cross` |
| `195` | `0xfb18...eb17` | `SHORT` | 10,704,043.73 USD | `4,768.16` | `2315.53` | `2244.80` | `2613.75` | 336,785.97 USD | `+3.15%` | `25X Cross` |
| `197` | `0x5559...d43b` | `SHORT` | 10,677,052.30 USD | `4,755.93` | `2262.69` | `2244.80` | `2739.21` | 84,153.58 USD | `+0.79%` | `25X Cross` |
| `201` | `0x7fda...17d1` | `LONG` | 10,372,664.39 USD | `4,620.55` | `2211.05` | `2244.80` | `0.000000` | 156,375.77 USD | `+1.51%` | `25X Cross` |
| `209` | `0xe091...6705` | `SHORT` | 10,103,850.45 USD | `4,500.00` | `2467.33` | `2244.80` | `2463.07` | 999,158.06 USD | `+9.89%` | `20X Cross` |
| `210` | `0x418a...8888` | `SHORT` | 10,100,250.00 USD | `4,500.00` | `2494.55` | `2244.80` | `2992.44` | 1,125,234.41 USD | `+11.14%` | `25X Cross` |
| `221` | `0xb829...3a81` | `LONG` | 9,864,377.74 USD | `4,394.91` | `2398.60` | `2244.80` | `1461.90` | -677,264.21 USD | `-6.87%` | `20X Cross` |
| `239` | `0x28bb...fca6` | `SHORT` | 9,450,162.92 USD | `4,209.61` | `1896.10` | `2244.80` | `3033.43` | -1,468,280.35 USD | `-15.54%` | `20X Cross` |
| `241` | `0x6ea4...0ea7` | `SHORT` | 9,391,141.13 USD | `4,184.01` | `2602.13` | `2244.80` | `3425.02` | 1,496,205.54 USD | `+15.93%` | `20X Cross` |
| `257` | `0x5e9e...35ee` | `SHORT` | 8,995,760.28 USD | `4,007.56` | `1796.39` | `2244.80` | `2585.51` | -1,796,610.19 USD | `-19.97%` | `20X Cross` |
| `258` | `0xfb94...0ddf` | `SHORT` | 8,984,397.25 USD | `4,002.10` | `2382.44` | `2244.80` | `5104.41` | 550,386.90 USD | `+6.13%` | `20X Cross` |
| `259` | `0x8cc9...2b6a` | `SHORT` | 8,978,800.00 USD | `4,000.00` | `1791.18` | `2244.80` | `3505.14` | -1,814,053.33 USD | `-20.20%` | `25X Cross` |
| `260` | `0x3dc9...54b0` | `SHORT` | 8,978,104.59 USD | `3,999.69` | `2480.32` | `2244.80` | `6499.76` | 942,431.96 USD | `+10.50%` | `20X Cross` |
| `274` | `0x4b67...f4e7` | `LONG` | 8,577,484.40 USD | `3,820.84` | `2591.51` | `2244.80` | `1346.82` | -1,324,289.14 USD | `-15.44%` | `20X Cross` |
| `279` | `0x12d2...f97f` | `LONG` | 8,434,675.67 USD | `3,757.26` | `2446.50` | `2244.80` | `1777.74` | -757,490.72 USD | `-8.98%` | `20X Cross` |
| `300` | `0x8ae4...3d60` | `LONG` | 7,986,482.83 USD | `3,558.20` | `2482.21` | `2244.80` | `523.57` | -845,715.20 USD | `-10.59%` | `10X Cross` |
| `302` | `0x469e...58a5` | `SHORT` | 7,930,672.37 USD | `3,533.33` | `2203.63` | `2244.80` | `3082.21` | -144,509.28 USD | `-1.82%` | `25X Cross` |
| `309` | `0x218a...7da2` | `SHORT` | 7,778,385.10 USD | `3,465.07` | `2208.16` | `2244.80` | `3101.73` | -126,955.84 USD | `-1.63%` | `10X Cross` |
| `343` | `0x9c2a...f6a8` | `SHORT` | 6,739,461.91 USD | `3,002.39` | `2515.77` | `2244.80` | `2597.67` | 813,875.98 USD | `+12.08%` | `20X Cross` |
| `344` | `0x4a20...3c26` | `LONG` | 6,734,100.00 USD | `3,000.00` | `2428.72` | `2244.80` | `628.28` | -552,060.28 USD | `-8.20%` | `20X Cross` |
| `345` | `0x007d...67a0` | `LONG` | 6,734,100.00 USD | `3,000.00` | `2400.00` | `2244.80` | `1472.52` | -465,900.00 USD | `-6.92%` | `25X Cross` |
| `346` | `0xb823...9763` | `SHORT` | 6,733,500.00 USD | `3,000.00` | `2229.66` | `2244.80` | `3233.41` | -44,503.32 USD | `-0.66%` | `25X Cross` |
| `390` | `0x8328...f54a` | `SHORT` | 5,783,617.43 USD | `2,576.45` | `2292.01` | `2244.80` | `3279.25` | 121,653.86 USD | `+2.10%` | `25X Cross` |
| `397` | `0xed48...7c9b` | `SHORT` | 5,726,777.75 USD | `2,551.13` | `2460.02` | `2244.80` | `3239.74` | 549,068.66 USD | `+9.59%` | `20X Cross` |
| `401` | `0x970c...2a93` | `SHORT` | 5,611,500.00 USD | `2,500.00` | `2229.57` | `2244.80` | `5068.31` | -37,555.51 USD | `-0.67%` | `20X Cross` |
| `402` | `0x1c98...7fc7` | `LONG` | 5,611,335.10 USD | `2,500.00` | `2452.60` | `2244.80` | `1916.65` | -520,186.46 USD | `-9.27%` | `10X Cross` |
| `416` | `0xa445...329d` | `LONG` | 5,401,053.03 USD | `2,406.14` | `2354.86` | `2244.80` | `1762.28` | -265,062.25 USD | `-4.91%` | `25X Cross` |
| `418` | `0xfbe2...c8ea` | `SHORT` | 5,354,310.43 USD | `2,385.21` | `2041.57` | `2244.80` | `2620.95` | -484,743.77 USD | `-9.05%` | `20X Cross` |
| `419` | `0x6749...ce07` | `SHORT` | 5,353,610.50 USD | `2,384.89` | `2220.92` | `2244.80` | `3616.67` | -56,947.47 USD | `-1.06%` | `20X Cross` |
| `420` | `0x645b...87b8` | `SHORT` | 5,342,331.23 USD | `2,379.98` | `2421.64` | `2244.80` | `11281.03` | 421,115.73 USD | `+7.88%` | `10X Cross` |
| `433` | `0x77ee...2902` | `SHORT` | 5,141,525.12 USD | `2,290.69` | `2476.53` | `2244.80` | `6103.79` | 531,447.12 USD | `+10.34%` | `25X Cross` |
| `453` | `0xd507...c948` | `SHORT` | 4,875,922.58 USD | `2,172.00` | `2387.49` | `2244.80` | `2600.25` | 309,718.45 USD | `+6.35%` | `5X Isolated` |
| `462` | `0x023a...2355` | `LONG` | 4,801,096.92 USD | `2,138.67` | `2328.93` | `2244.80` | `0.000000` | -179,733.68 USD | `-3.74%` | `25X Cross` |
| `466` | `0x382b...3e39` | `SHORT` | 4,780,607.94 USD | `2,129.54` | `2296.66` | `2244.80` | `4617.52` | 110,229.28 USD | `+2.31%` | `25X Cross` |
| `490` | `0xd911...961e` | `SHORT` | 4,570,107.03 USD | `2,035.77` | `2231.45` | `2244.80` | `3287.37` | -27,378.25 USD | `-0.60%` | `25X Cross` |
| `500` | `0x3453...b323` | `SHORT` | 4,489,676.32 USD | `2,000.12` | `2322.47` | `2244.80` | `2395.91` | 155,559.52 USD | `+3.46%` | `25X Cross` |
| `501` | `0xe02e...d78b` | `LONG` | 4,489,600.00 USD | `2,000.00` | `2228.11` | `2244.80` | `2171.60` | 33,376.53 USD | `+0.74%` | `25X Cross` |
| `505` | `0xf3dc...1672` | `SHORT` | 4,445,317.01 USD | `1,980.36` | `2240.44` | `2244.80` | `2784.85` | -8,429.46 USD | `-0.19%` | `20X Cross` |
| `509` | `0x7a6d...f79c` | `SHORT` | 4,426,473.33 USD | `1,971.44` | `2418.41` | `2244.80` | `2546.47` | 341,287.84 USD | `+7.71%` | `25X Cross` |
| `515` | `0xac48...3201` | `SHORT` | 4,409,420.22 USD | `1,964.37` | `2272.04` | `2244.80` | `3085.87` | 53,722.08 USD | `+1.22%` | `20X Cross` |
| `521` | `0x8376...9a1e` | `SHORT` | 4,288,490.37 USD | `1,910.50` | `2477.72` | `2244.80` | `3185.63` | 445,197.80 USD | `+10.38%` | `20X Cross` |
| `523` | `0x739c...cfb2` | `SHORT` | 4,265,348.00 USD | `1,900.00` | `2418.12` | `2244.80` | `2456.26` | 329,098.38 USD | `+7.72%` | `25X Cross` |
| `529` | `0x020c...5872` | `LONG` | 4,208,437.50 USD | `1,875.00` | `2230.70` | `2244.80` | `2171.40` | 25,864.23 USD | `+0.61%` | `25X Cross` |
| `551` | `0x7265...91a5` | `LONG` | 4,046,638.30 USD | `1,801.87` | `2533.96` | `2244.80` | `1987.12` | -519,228.16 USD | `-12.83%` | `20X Cross` |
| `552` | `0xbb34...1696` | `LONG` | 4,040,460.00 USD | `1,800.00` | `2313.95` | `2244.80` | `1951.96` | -124,658.23 USD | `-3.09%` | `25X Cross` |
| `553` | `0xc619...10f5` | `LONG` | 4,040,280.00 USD | `1,800.00` | `2313.55` | `2244.80` | `1784.47` | -124,115.83 USD | `-3.07%` | `25X Cross` |
| `566` | `0x91a9...3f70` | `SHORT` | 3,967,108.86 USD | `1,767.48` | `2156.23` | `2244.80` | `3649.00` | -156,004.78 USD | `-3.93%` | `4X Cross` |
| `573` | `0xbcd4...0dd2` | `SHORT` | 3,922,667.80 USD | `1,747.52` | `2233.24` | `2244.80` | `2760.28` | -20,011.58 USD | `-0.51%` | `25X Cross` |
| `576` | `0xb8eb...1dd5` | `SHORT` | 3,906,905.20 USD | `1,740.35` | `2233.05` | `2244.80` | `3276.83` | -20,618.13 USD | `-0.53%` | `25X Cross` |
| `598` | `0xfeec...4e9c` | `SHORT` | 3,797,941.58 USD | `1,691.81` | `2566.49` | `2244.80` | `2509.30` | 544,082.94 USD | `+14.33%` | `10X Cross` |
| `619` | `0xeee0...0b53` | `LONG` | 3,675,015.73 USD | `1,637.12` | `2468.64` | `2244.80` | `172.42` | -366,460.33 USD | `-9.97%` | `7X Cross` |
| `622` | `0x27b8...12fc` | `LONG` | 3,654,364.41 USD | `1,628.12` | `2468.73` | `2244.80` | `638.51` | -365,030.23 USD | `-9.99%` | `10X Cross` |
| `623` | `0x982b...4606` | `LONG` | 3,651,716.79 USD | `1,626.82` | `2575.24` | `2244.80` | `1547.40` | -537,736.28 USD | `-14.73%` | `5X Isolated` |
| `629` | `0x73d7...8be1` | `LONG` | 3,594,809.61 USD | `1,601.47` | `2410.40` | `2244.80` | `1767.46` | -265,369.31 USD | `-7.38%` | `25X Cross` |
| `631` | `0xad54...6203` | `LONG` | 3,586,279.07 USD | `1,597.45` | `2591.98` | `2244.80` | `2043.80` | -554,298.98 USD | `-15.46%` | `10X Isolated` |
| `638` | `0x880a...311c` | `LONG` | 3,542,765.48 USD | `1,578.40` | `2209.72` | `2244.80` | `0.000000` | 54,941.63 USD | `+1.55%` | `9X Cross` |
| `650` | `0x936c...bb0f` | `LONG` | 3,490,293.52 USD | `1,554.77` | `2232.92` | `2244.80` | `0.000000` | 18,614.26 USD | `+0.53%` | `20X Cross` |
| `657` | `0xe170...9300` | `SHORT` | 3,442,329.66 USD | `1,533.40` | `2076.39` | `2244.80` | `3091.04` | -258,380.16 USD | `-7.51%` | `25X Cross` |
| `662` | `0x4b86...df9d` | `SHORT` | 3,421,380.00 USD | `1,524.00` | `2287.40` | `2244.80` | `2759.61` | 64,617.60 USD | `+1.89%` | `9X Isolated` |
| `668` | `0x2e2b...2fab` | `LONG` | 3,383,609.15 USD | `1,507.38` | `2245.53` | `2244.80` | `1220.52` | -1,263.95 USD | `-0.04%` | `25X Cross` |
| `670` | `0x251f...6e5d` | `LONG` | 3,367,350.00 USD | `1,500.00` | `2346.68` | `2244.80` | `1879.71` | -152,680.49 USD | `-4.53%` | `20X Cross` |
| `671` | `0xde6b...3361` | `LONG` | 3,366,795.00 USD | `1,500.00` | `2216.98` | `2244.80` | `2168.53` | 41,314.26 USD | `+1.23%` | `25X Cross` |
| `691` | `0xb885...3c54` | `LONG` | 3,254,819.94 USD | `1,450.00` | `2274.34` | `2244.80` | `37.56` | -42,988.20 USD | `-1.32%` | `20X Cross` |
| `695` | `0xef70...a84c` | `SHORT` | 3,238,814.66 USD | `1,442.74` | `2424.73` | `2244.80` | `3251.51` | 259,456.17 USD | `+8.01%` | `25X Cross` |
| `699` | `0xbadb...9ee6` | `LONG` | 3,206,219.20 USD | `1,428.16` | `1936.00` | `2244.80` | `1054.92` | 441,297.55 USD | `+13.76%` | `20X Cross` |
| `759` | `0x53f8...ceff` | `LONG` | 3,027,324.31 USD | `1,348.65` | `2276.73` | `2244.80` | `0.000000` | -43,200.16 USD | `-1.43%` | `20X Cross` |
| `767` | `0xa0fb...96be` | `LONG` | 2,993,829.69 USD | `1,333.85` | `2276.68` | `2244.80` | `1529.56` | -42,933.76 USD | `-1.43%` | `3X Cross` |
| `804` | `0x1f16...6d07` | `LONG` | 2,841,916.80 USD | `1,266.00` | `2261.43` | `2244.80` | `1368.43` | -21,054.43 USD | `-0.74%` | `7X Cross` |
| `815` | `0xc435...c905` | `SHORT` | 2,801,173.44 USD | `1,248.00` | `2704.38` | `2244.80` | `3776.49` | 573,896.91 USD | `+20.49%` | `20X Cross` |
| `824` | `0x6859...7e1e` | `SHORT` | 2,777,286.57 USD | `1,237.15` | `2200.39` | `2244.80` | `4804.79` | -55,059.41 USD | `-1.98%` | `25X Cross` |
| `830` | `0x7277...0b98` | `SHORT` | 2,737,430.11 USD | `1,219.45` | `2206.05` | `2244.80` | `3387.13` | -47,242.31 USD | `-1.73%` | `20X Cross` |
| `831` | `0x7178...0854` | `LONG` | 2,735,340.26 USD | `1,218.63` | `2461.81` | `2244.80` | `1187.48` | -264,706.14 USD | `-9.68%` | `10X Cross` |
| `840` | `0xaaa1...ab8c` | `SHORT` | 2,693,640.00 USD | `1,200.00` | `2276.29` | `2244.80` | `2365.23` | 37,917.58 USD | `+1.41%` | `25X Isolated` |
| `857` | `0x07fd...689d` | `LONG` | 2,641,556.77 USD | `1,176.69` | `2416.34` | `2244.80` | `0.000000` | -201,743.17 USD | `-7.64%` | `25X Cross` |
| `875` | `0x0dd5...f6ee` | `LONG` | 2,561,423.27 USD | `1,141.00` | `2286.43` | `2244.80` | `1448.23` | -47,388.34 USD | `-1.85%` | `5X Cross` |
| `912` | `0x2f80...f203` | `SHORT` | 2,444,160.97 USD | `1,088.94` | `1984.00` | `2244.80` | `2959.43` | -283,693.78 USD | `-11.61%` | `20X Cross` |
| `922` | `0x8eb7...b90f` | `LONG` | 2,419,438.28 USD | `1,077.74` | `2396.38` | `2244.80` | `1880.93` | -163,239.76 USD | `-6.75%` | `5X Isolated` |
| `924` | `0x2b61...2f6c` | `SHORT` | 2,416,454.71 USD | `1,076.60` | `2681.75` | `2244.80` | `6247.70` | 470,718.03 USD | `+19.48%` | `10X Cross` |
| `941` | `0x30af...393e` | `SHORT` | 2,336,925.85 USD | `1,041.16` | `2252.26` | `2244.80` | `2296.91` | 8,056.47 USD | `+0.34%` | `25X Cross` |
| `965` | `0x1b2a...f7a6` | `LONG` | 2,301,746.09 USD | `1,025.37` | `2737.51` | `2244.80` | `882.07` | -505,213.85 USD | `-21.95%` | `10X Cross` |
| `978` | `0xfc27...9d9d` | `LONG` | 2,266,172.58 USD | `1,009.57` | `2237.33` | `2244.80` | `0.000000` | 7,435.07 USD | `+0.33%` | `25X Cross` |
| `981` | `0x001a...fef6` | `SHORT` | 2,261,243.16 USD | `1,007.33` | `2022.19` | `2244.80` | `3085.18` | -224,235.20 USD | `-9.92%` | `10X Cross` |
| `982` | `0x02aa...1806` | `SHORT` | 2,260,839.01 USD | `1,007.10` | `2654.68` | `2244.80` | `3612.70` | 412,693.09 USD | `+18.25%` | `20X Cross` |
| `984` | `0xdb3a...cf3b` | `LONG` | 2,252,117.58 USD | `1,003.22` | `2705.01` | `2244.80` | `0.000000` | -461,589.32 USD | `-20.50%` | `4X Cross` |
| `986` | `0x5272...fcd9` | `SHORT` | 2,244,800.00 USD | `1,000.00` | `2241.82` | `2244.80` | `2830.76` | -2,975.51 USD | `-0.13%` | `5X Cross` |
| `987` | `0x8c02...b73f` | `SHORT` | 2,244,700.00 USD | `1,000.00` | `2250.37` | `2244.80` | `8098.39` | 5,671.47 USD | `+0.25%` | `20X Cross` |
| `988` | `0x6463...42f5` | `SHORT` | 2,244,500.00 USD | `1,000.00` | `2223.43` | `2244.80` | `3709.97` | -21,065.05 USD | `-0.94%` | `5X Cross` |
| `990` | `0xd7b8...9f55` | `LONG` | 2,242,455.30 USD | `999.00` | `2195.00` | `2244.80` | `0.000000` | 49,650.30 USD | `+2.21%` | `15X Cross` |
| `1012` | `0xb002...ed8a` | `SHORT` | 2,161,257.52 USD | `962.78` | `2299.66` | `2244.80` | `4198.09` | 52,820.38 USD | `+2.44%` | `25X Cross` |
| `1028` | `0xb1ec...e86a` | `SHORT` | 2,095,738.12 USD | `933.64` | `2272.72` | `2244.80` | `13225.01` | 26,168.84 USD | `+1.25%` | `25X Cross` |
| `1055` | `0xede2...f971` | `LONG` | 2,052,173.96 USD | `914.31` | `2208.16` | `2244.80` | `1462.97` | 33,216.97 USD | `+1.62%` | `5X Cross` |
| `1057` | `0x9606...4e5d` | `SHORT` | 2,049,586.29 USD | `913.00` | `2478.70` | `2244.80` | `3545.30` | 213,467.31 USD | `+10.42%` | `20X Cross` |
| `1074` | `0x5f10...d49d` | `LONG` | 2,020,320.00 USD | `900.00` | `2249.83` | `2244.80` | `1815.30` | -4,533.47 USD | `-0.22%` | `25X Cross` |
| `1089` | `0x51f6...2b39` | `LONG` | 1,998,114.09 USD | `890.15` | `2226.49` | `2244.80` | `803.04` | 16,207.20 USD | `+0.81%` | `25X Cross` |
| `1094` | `0xb812...b5e0` | `LONG` | 1,988,752.34 USD | `886.04` | `2263.21` | `2244.80` | `1111.88` | -16,555.24 USD | `-0.83%` | `25X Cross` |
| `1165` | `0x2828...93a0` | `LONG` | 1,884,906.49 USD | `839.60` | `2242.41` | `2244.80` | `2192.53` | 2,174.30 USD | `+0.12%` | `25X Cross` |
| `1170` | `0xcd27...52a8` | `LONG` | 1,879,448.91 USD | `837.21` | `2553.56` | `2244.80` | `1403.21` | -258,415.86 USD | `-13.75%` | `2X Cross` |
| `1225` | `0x04a9...95aa` | `LONG` | 1,795,920.00 USD | `800.00` | `2595.13` | `2244.80` | `1877.49` | -280,186.74 USD | `-15.60%` | `5X Cross` |
| `1226` | `0x7737...bf66` | `SHORT` | 1,795,452.84 USD | `799.79` | `2494.83` | `2244.80` | `24838.63` | 199,893.19 USD | `+11.13%` | `15X Cross` |
| `1258` | `0x6f11...0389` | `SHORT` | 1,748,488.87 USD | `779.00` | `2333.39` | `2244.80` | `3021.03` | 69,222.73 USD | `+3.96%` | `25X Cross` |
| `1264` | `0x458d...ab3b` | `LONG` | 1,739,152.07 USD | `774.75` | `2740.41` | `2244.80` | `1886.96` | -383,977.12 USD | `-22.08%` | `3X Isolated` |
| `1317` | `0xaa53...9cb7` | `LONG` | 1,639,459.82 USD | `730.34` | `2389.70` | `2244.80` | `1972.44` | -105,829.81 USD | `-6.46%` | `20X Cross` |
| `1320` | `0x3fc5...c0c1` | `SHORT` | 1,638,387.86 USD | `729.92` | `2702.11` | `2244.80` | `4638.46` | 333,954.34 USD | `+20.38%` | `25X Cross` |
| `1340` | `0xa189...94d7` | `SHORT` | 1,616,136.86 USD | `719.98` | `2691.84` | `2244.80` | `2914.86` | 321,935.80 USD | `+19.92%` | `25X Cross` |
| `1354` | `0x2f93...4404` | `LONG` | 1,587,919.78 USD | `707.47` | `1700.45` | `2244.80` | `1368.60` | 384,893.41 USD | `+24.24%` | `4X Isolated` |
| `1363` | `0x5605...fe0f` | `SHORT` | 1,575,961.31 USD | `702.14` | `2566.90` | `2244.80` | `3059.15` | 226,371.34 USD | `+14.36%` | `20X Cross` |
| `1364` | `0x0a97...347d` | `SHORT` | 1,575,922.49 USD | `702.00` | `2238.76` | `2244.80` | `3351.75` | -4,305.14 USD | `-0.27%` | `20X Cross` |
| `1368` | `0x0deb...0bc5` | `LONG` | 1,571,360.00 USD | `700.00` | `2071.05` | `2244.80` | `1597.19` | 121,624.21 USD | `+7.74%` | `20X Cross` |
| `1369` | `0x26e6...6b28` | `LONG` | 1,571,290.00 USD | `700.00` | `1835.24` | `2244.80` | `2043.03` | 286,618.47 USD | `+18.24%` | `20X Cross` |
| `1376` | `0xa70a...4be9` | `SHORT` | 1,563,375.64 USD | `696.47` | `2239.13` | `2244.80` | `4218.53` | -3,873.51 USD | `-0.25%` | `20X Cross` |
| `1400` | `0x6e6f...82a6` | `SHORT` | 1,551,585.76 USD | `691.16` | `2237.53` | `2244.80` | `3587.36` | -5,091.02 USD | `-0.33%` | `20X Cross` |
| `1405` | `0x7b22...8a34` | `LONG` | 1,537,155.32 USD | `684.73` | `2228.49` | `2244.80` | `2181.59` | 11,231.75 USD | `+0.73%` | `25X Cross` |
| `1416` | `0x248e...6be2` | `SHORT` | 1,528,343.57 USD | `680.93` | `2282.89` | `2244.80` | `3448.11` | 26,142.09 USD | `+1.71%` | `20X Cross` |
| `1417` | `0xdbd1...29dd` | `SHORT` | 1,527,836.76 USD | `680.70` | `3030.57` | `2244.80` | `3774.76` | 535,084.36 USD | `+35.02%` | `6X Cross` |
| `1424` | `0x71e5...be04` | `LONG` | 1,521,226.43 USD | `677.67` | `2727.27` | `2244.80` | `1470.74` | -326,959.17 USD | `-21.49%` | `20X Cross` |
| `1430` | `0x0b23...f37b` | `LONG` | 1,515,057.75 USD | `675.00` | `2238.15` | `2244.80` | `596.81` | 4,301.11 USD | `+0.28%` | `5X Cross` |
| `1462` | `0x0cac...6170` | `SHORT` | 1,475,890.25 USD | `657.50` | `2146.55` | `2244.80` | `2839.20` | -64,528.05 USD | `-4.37%` | `20X Cross` |
| `1494` | `0xf00e...fe3d` | `SHORT` | 1,443,201.31 USD | `642.88` | `2333.21` | `2244.80` | `2487.01` | 56,776.66 USD | `+3.93%` | `20X Cross` |
| `1497` | `0xb15b...dbae` | `SHORT` | 1,442,476.93 USD | `642.64` | `2290.80` | `2244.80` | `2324.77` | 29,690.55 USD | `+2.06%` | `25X Cross` |
| `1501` | `0xffb2...5ed6` | `SHORT` | 1,438,220.31 USD | `640.77` | `2672.96` | `2244.80` | `2490.94` | 274,528.04 USD | `+19.09%` | `20X Cross` |
| `1512` | `0x8505...1821` | `SHORT` | 1,423,177.48 USD | `633.96` | `2239.93` | `2244.80` | `3904.03` | -3,145.88 USD | `-0.22%` | `20X Cross` |
| `1542` | `0xfce0...f4c0` | `SHORT` | 1,399,932.11 USD | `623.60` | `3129.61` | `2244.80` | `2807.80` | 551,694.47 USD | `+39.41%` | `20X Cross` |
| `1589` | `0x7050...5fff` | `SHORT` | 1,349,181.07 USD | `601.11` | `2245.52` | `2244.80` | `3289.87` | 619.04 USD | `+0.05%` | `25X Cross` |
| `1590` | `0xad02...eb65` | `LONG` | 1,348,332.29 USD | `600.62` | `2460.69` | `2244.80` | `1078.66` | -129,608.27 USD | `-9.61%` | `5X Cross` |
| `1591` | `0x638f...f5f0` | `LONG` | 1,346,820.00 USD | `600.00` | `4011.50` | `2244.80` | `431.36` | -1,060,083.53 USD | `-78.71%` | `25X Cross` |
| `1667` | `0xfb99...37f3` | `LONG` | 1,269,145.54 USD | `565.34` | `2362.35` | `2244.80` | `1254.29` | -66,390.81 USD | `-5.23%` | `3X Cross` |
| `1678` | `0x844b...7f42` | `SHORT` | 1,259,181.33 USD | `561.00` | `2026.17` | `2244.80` | `2997.26` | -122,497.92 USD | `-9.73%` | `25X Cross` |
| `1691` | `0xabe6...1d99` | `SHORT` | 1,248,173.38 USD | `556.00` | `2484.68` | `2244.80` | `3121.46` | 133,322.51 USD | `+10.68%` | `20X Cross` |
| `1705` | `0xbef3...0d3e` | `LONG` | 1,239,863.65 USD | `552.33` | `2237.93` | `2244.80` | `2078.71` | 3,790.68 USD | `+0.31%` | `20X Cross` |
| `1708` | `0x6a41...a3b9` | `LONG` | 1,236,196.10 USD | `550.69` | `2237.64` | `2244.80` | `2084.06` | 3,938.09 USD | `+0.32%` | `20X Cross` |
| `1709` | `0x9599...c60a` | `SHORT` | 1,235,379.69 USD | `550.30` | `2241.99` | `2244.80` | `9409.59` | -1,599.18 USD | `-0.13%` | `20X Cross` |
| `1710` | `0x825c...465e` | `LONG` | 1,234,695.00 USD | `550.00` | `2208.12` | `2244.80` | `1189.25` | 20,225.50 USD | `+1.64%` | `4X Cross` |
| `1715` | `0xad21...fb6a` | `LONG` | 1,228,480.04 USD | `547.26` | `2565.80` | `2244.80` | `1732.84` | -175,672.95 USD | `-14.30%` | `6X Cross` |
| `1753` | `0x2e30...4cb5` | `SHORT` | 1,187,387.94 USD | `528.97` | `2315.37` | `2244.80` | `11698.92` | 37,385.73 USD | `+3.15%` | `2X Cross` |
| `1788` | `0x6dae...90de` | `SHORT` | 1,160,630.66 USD | `517.05` | `2292.28` | `2244.80` | `3815.43` | 24,602.75 USD | `+2.12%` | `25X Cross` |
| `1808` | `0xfc66...ca06` | `SHORT` | 1,146,901.68 USD | `510.89` | `2275.19` | `2244.80` | `54779.18` | 15,479.92 USD | `+1.35%` | `20X Cross` |
| `1817` | `0x0089...2410` | `SHORT` | 1,138,889.40 USD | `507.35` | `2308.88` | `2244.80` | `3412.17` | 32,510.86 USD | `+2.85%` | `20X Cross` |
| `1839` | `0xe282...df29` | `LONG` | 1,122,450.00 USD | `500.00` | `2309.84` | `2244.80` | `2045.11` | -32,474.21 USD | `-2.89%` | `10X Isolated` |
| `1840` | `0xb322...d51f` | `SHORT` | 1,122,450.00 USD | `500.00` | `2268.03` | `2244.80` | `3736.18` | 11,566.32 USD | `+1.03%` | `20X Cross` |
| `1841` | `0xa559...ff95` | `LONG` | 1,122,400.00 USD | `500.00` | `2260.68` | `2244.80` | `1066.52` | -7,944.36 USD | `-0.71%` | `20X Cross` |
| `1842` | `0x6936...9417` | `SHORT` | 1,122,350.00 USD | `500.00` | `2315.11` | `2244.80` | `2358.71` | 35,205.21 USD | `+3.14%` | `25X Isolated` |
| `1843` | `0x4044...794c` | `LONG` | 1,122,350.00 USD | `500.00` | `2260.80` | `2244.80` | `0.000000` | -8,050.00 USD | `-0.72%` | `25X Cross` |
| `1844` | `0x89b2...9ca6` | `LONG` | 1,122,250.00 USD | `500.00` | `2363.45` | `2244.80` | `1622.44` | -59,477.42 USD | `-5.30%` | `25X Cross` |
| `1850` | `0x7298...7d6c` | `SHORT` | 1,118,195.73 USD | `498.15` | `3426.75` | `2244.80` | `5421.42` | 588,840.09 USD | `+52.66%` | `20X Cross` |
| `1863` | `0x9c68...7783` | `SHORT` | 1,107,377.35 USD | `493.31` | `2273.58` | `2244.80` | `3884.98` | 14,201.90 USD | `+1.28%` | `25X Cross` |
| `1872` | `0x404c...5f03` | `SHORT` | 1,099,323.11 USD | `489.79` | `2671.94` | `2244.80` | `4948.82` | 209,356.45 USD | `+19.04%` | `20X Cross` |
| `1879` | `0x321f...1c84` | `SHORT` | 1,095,399.37 USD | `488.02` | `2370.09` | `2244.80` | `3047.32` | 61,245.23 USD | `+5.59%` | `10X Cross` |
| `1881` | `0x94b6...e5b3` | `SHORT` | 1,091,037.78 USD | `486.05` | `2260.75` | `2244.80` | `2366.08` | 7,804.81 USD | `+0.72%` | `25X Cross` |
| `1926` | `0x0903...6f81` | `LONG` | 1,044,052.93 USD | `465.08` | `2236.70` | `2244.80` | `1923.16` | 3,812.27 USD | `+0.37%` | `25X Cross` |
| `1933` | `0x82c6...fe42` | `LONG` | 1,038,275.50 USD | `462.50` | `2501.38` | `2244.80` | `2053.45` | -118,615.07 USD | `-11.42%` | `5X Isolated` |
| `1940` | `0xe330...77a1` | `SHORT` | 1,035,179.48 USD | `461.20` | `2206.97` | `2244.80` | `6448.05` | -17,322.11 USD | `-1.67%` | `20X Cross` |
| `1989` | `0xae55...2236` | `LONG` | 1,010,115.00 USD | `450.00` | `2510.21` | `2244.80` | `0.000000` | -119,482.50 USD | `-11.83%` | `25X Cross` |
| `1999` | `0xf71a...7215` | `LONG` | 1,005,339.38 USD | `447.91` | `2223.27` | `2244.80` | `1081.10` | 9,505.10 USD | `+0.95%` | `25X Cross` |
| `2002` | `0x617e...0f97` | `SHORT` | 1,004,650.36 USD | `447.55` | `2205.60` | `2244.80` | `3344.56` | -17,543.62 USD | `-1.75%` | `10X Cross` |
| `2012` | `0xac26...a9c7` | `SHORT` | 1,001,232.05 USD | `446.04` | `2192.58` | `2244.80` | `8667.07` | -23,245.85 USD | `-2.32%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `2328.00` | 11,998.98 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 12.00K USD at 2328.0000 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `2335.30` | 96,002.78 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 96.00K USD at 2335.3000 USD [API] | `2026-10-29 19:59:25` |
| `ANNOUNCEMENT` | `INFO` | `2308.50` | 1,079.69 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.08K USD at 2308.5000 USD [API] | `2026-10-29 20:05:12` |
| `ANNOUNCEMENT` | `INFO` | `2310.50` | 48.98 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.05K USD at 2310.5000 USD [API] | `2026-10-29 20:05:00` |
| `ANNOUNCEMENT` | `INFO` | `2310.50` | 1,351.87 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.35K USD at 2310.5000 USD [API] | `2026-10-29 20:05:00` |
| `ANNOUNCEMENT` | `INFO` | `2310.50` | 1,093.33 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.09K USD at 2310.5000 USD [API] | `2026-10-29 20:05:00` |
| `ANNOUNCEMENT` | `INFO` | `2388.20` | 89,007.98 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 89.01K USD at 2388.2000 USD [API] | `2026-10-28 20:01:45` |
| `ANNOUNCEMENT` | `INFO` | `2295.00` | 118,879.39 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 118.88K USD at 2295.0000 USD [API] | `2026-10-29 20:36:25` |
| `ANNOUNCEMENT` | `INFO` | `2295.00` | 44,561.56 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 44.56K USD at 2295.0000 USD [API] | `2026-10-29 20:36:25` |
| `ANNOUNCEMENT` | `INFO` | `2301.40` | 17,890.85 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 17.89K USD at 2301.4000 USD [API] | `2026-10-29 20:33:43` |
| `ANNOUNCEMENT` | `INFO` | `2301.40` | 34,671.28 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 34.67K USD at 2301.4000 USD [API] | `2026-10-29 20:33:43` |
| `ANNOUNCEMENT` | `INFO` | `2301.40` | 4,473.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 4.47K USD at 2301.4000 USD [API] | `2026-10-29 20:33:43` |
| `ANNOUNCEMENT` | `INFO` | `2301.40` | 18,156.44 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 18.16K USD at 2301.4000 USD [API] | `2026-10-29 20:33:43` |
| `ANNOUNCEMENT` | `INFO` | `2313.50` | 16,143.37 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 16.14K USD at 2313.5000 USD [API] | `2026-10-29 20:04:17` |
| `ANNOUNCEMENT` | `INFO` | `2316.30` | 9,807.91 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 9.81K USD at 2316.3000 USD [API] | `2026-10-29 20:03:59` |
| `ANNOUNCEMENT` | `INFO` | `2316.30` | 2,479.60 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.48K USD at 2316.3000 USD [API] | `2026-10-29 20:03:59` |
| `ANNOUNCEMENT` | `INFO` | `2293.40` | 41,216.76 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 41.22K USD at 2293.4000 USD [API] | `2026-10-29 20:40:55` |
| `ANNOUNCEMENT` | `INFO` | `2254.50` | 4,063.06 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 4.06K USD at 2254.5000 USD [API] | `2026-10-29 20:42:30` |
| `ANNOUNCEMENT` | `INFO` | `2271.40` | 1,107.76 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.11K USD at 2271.4000 USD [API] | `2026-10-29 20:41:40` |


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
| `Live` | `Long Liquidation` | `455.00` | 80,660.00 USD | 784,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `465.00` | 6,190.00 USD | 784,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 70,920.00 USD | 784,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 108,780.00 USD | 784,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 19,900.00 USD | 784,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 65,690.00 USD | 784,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 1,830,000.00 USD | 784,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 38,160.00 USD | 782,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 8,790.00 USD | 782,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 13,630.00 USD | 782,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 106,590.00 USD | 782,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 150,140.00 USD | 782,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 12,360.00 USD | 782,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 2,850,000.00 USD | 782,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 554,380.00 USD | 779,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 1,830,000.00 USD | 778,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 57,360.00 USD | 776,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 1,080,000.00 USD | 776,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 15,580.00 USD | 775,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 339,590.00 USD | 775,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 51,390.00 USD | 775,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 105,210.00 USD | 775,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 15,070.00 USD | 775,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 32,820.00 USD | 775,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 11,490.00 USD | 775,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 51,810.00 USD | 775,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 1,810.00 USD | 775,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 405,280.00 USD | 775,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 66,120.00 USD | 774,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 7,820.00 USD | 774,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 38,260.00 USD | 774,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 7,720.00 USD | 774,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 4,390.00 USD | 774,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 20,660.00 USD | 774,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 84,530.00 USD | 774,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 47,650.00 USD | 774,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 98,180.00 USD | 774,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 845,300.00 USD | 774,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 88,670.00 USD | 773,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 92,370.00 USD | 773,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 95,080.00 USD | 773,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 85,930.00 USD | 773,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 404,280.00 USD | 773,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 1,200,000.00 USD | 772,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 115,430.00 USD | 771,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 131,400.00 USD | 771,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 166,190.00 USD | 771,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 168,790.00 USD | 771,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 84,000.00 USD | 770,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 62,450.00 USD | 770,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 27,560.00 USD | 770,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 483,050.00 USD | 770,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 144,850.00 USD | 770,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 215,460.00 USD | 770,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 72,670.00 USD | 769,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 21,150.00 USD | 769,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 345,840.00 USD | 769,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 54,250.00 USD | 769,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 275,540.00 USD | 769,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 396,790.00 USD | 769,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 9,530,000.00 USD | 768,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 127,940.00 USD | 759,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 671,120.00 USD | 759,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 868,060.00 USD | 758,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 38,740.00 USD | 757,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 137,420.00 USD | 757,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 7,860,000.00 USD | 757,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 176,230.00 USD | 749,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 1,740,000.00 USD | 749,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 214,200.00 USD | 747,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 537,840.00 USD | 747,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 51,500.00 USD | 746,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 1,560,000.00 USD | 746,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 1,270,000.00 USD | 745,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 7,200,000.00 USD | 743,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 2,020,000.00 USD | 736,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 78,020.00 USD | 734,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 432,140.00 USD | 734,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 138,120.00 USD | 734,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 56,730.00 USD | 734,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 1,260,000.00 USD | 733,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 289,300.00 USD | 732,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 15,490,000.00 USD | 732,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 474,130.00 USD | 716,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 339,640.00 USD | 716,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 114,060.00 USD | 716,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 186,060.00 USD | 716,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 492,940.00 USD | 715,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 5,500,000.00 USD | 715,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 188,030.00 USD | 709,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 106,050.00 USD | 709,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 1,260,000.00 USD | 709,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 8,980,000.00 USD | 708,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 485,050.00 USD | 699,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 913,010.00 USD | 698,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 22,730,000.00 USD | 697,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 229,690.00 USD | 675,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 561,450.00 USD | 674,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 782,000.00 USD | 674,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 1,730,000.00 USD | 673,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 661,960.00 USD | 671,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 8,450,000.00 USD | 671,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 5,730,000.00 USD | 662,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 318,770.00 USD | 657,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 19,400,000.00 USD | 656,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 498,390.00 USD | 637,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 18,790,000.00 USD | 636,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 2,460,000.00 USD | 618,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 902,770.00 USD | 615,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 4,110,000.00 USD | 614,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 16,090,000.00 USD | 610,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 576,720.00 USD | 594,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 949,290.00 USD | 593,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 667,450.00 USD | 592,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 2,010,000.00 USD | 592,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 18,080,000.00 USD | 590,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 1,080,000.00 USD | 572,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 1,720,000.00 USD | 571,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 18,670,000.00 USD | 569,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 37,490,000.00 USD | 550,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 859,690.00 USD | 513,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 11,660,000.00 USD | 512,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 1,030,000.00 USD | 500,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 573,580.00 USD | 499,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 756,150.00 USD | 499,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 1,020,000.00 USD | 498,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 511,390.00 USD | 497,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 36,690,000.00 USD | 496,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 1,580,000.00 USD | 460,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 837,560.00 USD | 458,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 480,300.00 USD | 457,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 7,660,000.00 USD | 457,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 24,770,000.00 USD | 449,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 86,890,000.00 USD | 424,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 482,950.00 USD | 337,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 3,030,000.00 USD | 337,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 507,190.00 USD | 334,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 1,320,000.00 USD | 333,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 1,060,000.00 USD | 332,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 16,200,000.00 USD | 331,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 1,050,000.00 USD | 315,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 15,820,000.00 USD | 314,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 7,240,000.00 USD | 298,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 5,540,000.00 USD | 291,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 538,030.00 USD | 285,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 1,420,000.00 USD | 285,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 18,440,000.00 USD | 283,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 17,280,000.00 USD | 265,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 876,330.00 USD | 247,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 5,430,000.00 USD | 247,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 13,680,000.00 USD | 241,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 2,720,000.00 USD | 227,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1972.30` | 871,060,000.00 USD | 871,060,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1975.00` | 3,020,000.00 USD | 225,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1975.10` | 870,930,000.00 USD | 870,930,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1977.90` | 870,880,000.00 USD | 870,880,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1983.50` | 868,640,000.00 USD | 868,640,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1985.00` | 5,560,000.00 USD | 222,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1986.30` | 868,430,000.00 USD | 868,430,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1989.10` | 864,700,000.00 USD | 864,700,000.00 USD | 0.00 USD | 1,780,000.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1991.90` | 862,890,000.00 USD | 862,890,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1994.70` | 860,180,000.00 USD | 860,180,000.00 USD | 0.00 USD | 0.00 USD | 808,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1995.00` | 645,300.00 USD | 216,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1997.50` | 859,370,000.00 USD | 859,370,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1997.60` | 755,360,000.00 USD | 755,360,000.00 USD | 206,020.00 USD | 86,340.00 USD | 328,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2000.10` | 754,740,000.00 USD | 754,740,000.00 USD | 27,360.00 USD | 25,630.00 USD | 586,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2002.60` | 754,100,000.00 USD | 754,100,000.00 USD | 942,390.00 USD | 700,600.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2003.10` | 858,030,000.00 USD | 858,030,000.00 USD | 0.00 USD | 266,430.00 USD | 617,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2005.00` | 13,400,000.00 USD | 216,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2005.10` | 751,280,000.00 USD | 751,280,000.00 USD | 773,690.00 USD | 255,310.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2005.90` | 857,140,000.00 USD | 857,140,000.00 USD | 0.00 USD | 475,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2007.60` | 750,240,000.00 USD | 750,240,000.00 USD | 0.00 USD | 383,650.00 USD | 281,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2008.70` | 856,670,000.00 USD | 856,670,000.00 USD | 807,770.00 USD | 0.00 USD | 380,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2010.10` | 749,580,000.00 USD | 749,580,000.00 USD | 460,200.00 USD | 638,030.00 USD | 374,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2011.50` | 855,480,000.00 USD | 855,480,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2012.60` | 748,100,000.00 USD | 748,100,000.00 USD | 348,530.00 USD | 266,130.00 USD | 25,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2015.00` | 2,050,000.00 USD | 202,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2015.10` | 747,460,000.00 USD | 747,460,000.00 USD | 413,060.00 USD | 159,880.00 USD | 202,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2017.10` | 854,520,000.00 USD | 854,520,000.00 USD | 62,110.00 USD | 0.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2017.60` | 746,690,000.00 USD | 746,690,000.00 USD | 1,140,000.00 USD | 1,500,000.00 USD | 573,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2019.90` | 854,440,000.00 USD | 854,440,000.00 USD | 1,020,000.00 USD | 466,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2020.10` | 743,480,000.00 USD | 743,480,000.00 USD | 1,340,000.00 USD | 2,190,000.00 USD | 696,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2022.60` | 739,250,000.00 USD | 739,250,000.00 USD | 1,840,000.00 USD | 628,480.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2022.70` | 852,960,000.00 USD | 852,960,000.00 USD | 1,890,000.00 USD | 957,590.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,010,000.00 USD | 200,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2025.10` | 734,890,000.00 USD | 734,890,000.00 USD | 595,510.00 USD | 1,010,000.00 USD | 240,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2025.50` | 848,560,000.00 USD | 848,560,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2027.60` | 733,050,000.00 USD | 733,050,000.00 USD | 2,550,000.00 USD | 1,160,000.00 USD | 167,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.30` | 848,380,000.00 USD | 848,380,000.00 USD | 1,100,000.00 USD | 0.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2030.10` | 729,170,000.00 USD | 729,170,000.00 USD | 307,680.00 USD | 366,120.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.10` | 847,250,000.00 USD | 847,250,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.60` | 727,390,000.00 USD | 727,390,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2033.90` | 842,680,000.00 USD | 842,680,000.00 USD | 0.00 USD | 0.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 598,780.00 USD | 199,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2035.10` | 723,840,000.00 USD | 723,840,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2036.70` | 841,320,000.00 USD | 841,320,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2037.60` | 722,500,000.00 USD | 722,500,000.00 USD | 396,700.00 USD | 458,110.00 USD | 378,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2039.50` | 840,990,000.00 USD | 840,990,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2040.10` | 721,260,000.00 USD | 721,260,000.00 USD | 542,670.00 USD | 178,560.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2042.60` | 720,510,000.00 USD | 720,510,000.00 USD | 626,840.00 USD | 0.00 USD | 174,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 6,820,000.00 USD | 198,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2045.10` | 719,710,000.00 USD | 719,710,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2045.10` | 839,540,000.00 USD | 839,540,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2047.60` | 719,680,000.00 USD | 719,680,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.10` | 718,860,000.00 USD | 718,860,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2050.70` | 839,240,000.00 USD | 839,240,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2053.50` | 839,020,000.00 USD | 839,020,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 3,880,000.00 USD | 192,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2055.10` | 717,750,000.00 USD | 717,750,000.00 USD | 242,080.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2059.10` | 836,730,000.00 USD | 836,730,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2060.10` | 717,390,000.00 USD | 717,390,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.90` | 836,390,000.00 USD | 836,390,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2062.60` | 716,630,000.00 USD | 716,630,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.70` | 831,130,000.00 USD | 831,130,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 14,120,000.00 USD | 188,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2065.10` | 716,550,000.00 USD | 716,550,000.00 USD | 563,140.00 USD | 537,030.00 USD | 510,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2067.50` | 828,670,000.00 USD | 828,670,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2067.60` | 714,940,000.00 USD | 714,940,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2070.10` | 714,250,000.00 USD | 714,250,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2070.30` | 827,020,000.00 USD | 827,020,000.00 USD | 3,600,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2072.60` | 713,870,000.00 USD | 713,870,000.00 USD | 47,910.00 USD | 555,250.00 USD | 420,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2073.10` | 819,460,000.00 USD | 819,460,000.00 USD | 2,870,000.00 USD | 2,180,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 3,520,000.00 USD | 174,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2075.10` | 712,850,000.00 USD | 712,850,000.00 USD | 25,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2075.90` | 812,380,000.00 USD | 812,380,000.00 USD | 3,910,000.00 USD | 4,290,000.00 USD | 4,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2077.60` | 712,830,000.00 USD | 712,830,000.00 USD | 354,080.00 USD | 25,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.70` | 799,880,000.00 USD | 799,880,000.00 USD | 4,160,000.00 USD | 3,730,000.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2080.10` | 712,450,000.00 USD | 712,450,000.00 USD | 77,960.00 USD | 29,610.00 USD | 199,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.50` | 789,930,000.00 USD | 789,930,000.00 USD | 4,400,000.00 USD | 1,290,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2082.60` | 712,140,000.00 USD | 712,140,000.00 USD | 827,940.00 USD | 4,240.00 USD | 206,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.30` | 783,020,000.00 USD | 783,020,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 13,940,000.00 USD | 170,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2085.10` | 711,100,000.00 USD | 711,100,000.00 USD | 528,660.00 USD | 200,510.00 USD | 820,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2087.10` | 775,630,000.00 USD | 775,630,000.00 USD | 2,920,000.00 USD | 2,750,000.00 USD | 3,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2087.60` | 709,550,000.00 USD | 709,550,000.00 USD | 324,560.00 USD | 170,940.00 USD | 302,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2089.90` | 766,950,000.00 USD | 766,950,000.00 USD | 4,130,000.00 USD | 948,120.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2090.10` | 708,750,000.00 USD | 708,750,000.00 USD | 461,140.00 USD | 207,680.00 USD | 251,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.60` | 707,830,000.00 USD | 707,830,000.00 USD | 587,740.00 USD | 226,930.00 USD | 199,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2092.70` | 758,710,000.00 USD | 758,710,000.00 USD | 4,680,000.00 USD | 737,060.00 USD | 6,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,740,000.00 USD | 156,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2095.10` | 706,820,000.00 USD | 706,820,000.00 USD | 1,370,000.00 USD | 838,640.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2095.50` | 747,080,000.00 USD | 747,080,000.00 USD | 2,480,000.00 USD | 2,010,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2097.60` | 703,530,000.00 USD | 703,530,000.00 USD | 87,950.00 USD | 672,980.00 USD | 555,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2098.30` | 741,570,000.00 USD | 741,570,000.00 USD | 3,020,000.00 USD | 3,130,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2100.10` | 702,210,000.00 USD | 702,210,000.00 USD | 307,340.00 USD | 928,890.00 USD | 50,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.10` | 733,950,000.00 USD | 733,950,000.00 USD | 631,640.00 USD | 1,240,000.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.60` | 700,930,000.00 USD | 700,930,000.00 USD | 211,840.00 USD | 222,480.00 USD | 483,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2103.90` | 728,670,000.00 USD | 728,670,000.00 USD | 1,130,000.00 USD | 738,240.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 2,400,000.00 USD | 154,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2105.10` | 700,010,000.00 USD | 700,010,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 691,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2106.70` | 724,480,000.00 USD | 724,480,000.00 USD | 1,700,000.00 USD | 834,660.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2107.60` | 694,580,000.00 USD | 694,580,000.00 USD | 734,860.00 USD | 0.00 USD | 488,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2109.50` | 720,760,000.00 USD | 720,760,000.00 USD | 7,750,000.00 USD | 1,800,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.10` | 693,360,000.00 USD | 693,360,000.00 USD | 61,010.00 USD | 31,550.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2112.30` | 709,450,000.00 USD | 709,450,000.00 USD | 3,920,000.00 USD | 1,480,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2112.60` | 693,260,000.00 USD | 693,260,000.00 USD | 902,600.00 USD | 360,140.00 USD | 221,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,120,000.00 USD | 152,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2115.10` | 691,780,000.00 USD | 691,780,000.00 USD | 202,800.00 USD | 411,610.00 USD | 962,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2115.10` | 700,330,000.00 USD | 700,330,000.00 USD | 923,330.00 USD | 3,210,000.00 USD | 1,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2117.60` | 690,200,000.00 USD | 690,200,000.00 USD | 4,750,000.00 USD | 4,080,000.00 USD | 302,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.90` | 694,260,000.00 USD | 694,260,000.00 USD | 8,390,000.00 USD | 578,010.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.10` | 681,070,000.00 USD | 681,070,000.00 USD | 3,950,000.00 USD | 22,470.00 USD | 645,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2120.70` | 682,710,000.00 USD | 682,710,000.00 USD | 7,060,000.00 USD | 5,780,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2122.60` | 676,460,000.00 USD | 676,460,000.00 USD | 4,520,000.00 USD | 3,800,000.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2123.50` | 668,060,000.00 USD | 668,060,000.00 USD | 7,150,000.00 USD | 7,720,000.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,840,000.00 USD | 151,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.10` | 666,280,000.00 USD | 666,280,000.00 USD | 6,940,000.00 USD | 1,830,000.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2126.30` | 651,780,000.00 USD | 651,780,000.00 USD | 2,740,000.00 USD | 4,400,000.00 USD | 4,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2127.60` | 655,400,000.00 USD | 655,400,000.00 USD | 4,430,000.00 USD | 4,180,000.00 USD | 782,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2129.10` | 639,850,000.00 USD | 639,850,000.00 USD | 4,770,000.00 USD | 1,270,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2130.10` | 646,010,000.00 USD | 646,010,000.00 USD | 1,250,000.00 USD | 172,040.00 USD | 794,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2131.90` | 632,700,000.00 USD | 632,700,000.00 USD | 2,170,000.00 USD | 1,620,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2132.60` | 643,800,000.00 USD | 643,800,000.00 USD | 81,820.00 USD | 284,820.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.70` | 627,550,000.00 USD | 627,550,000.00 USD | 1,630,000.00 USD | 790,240.00 USD | 898,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 1,620,000.00 USD | 27,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2135.10` | 641,880,000.00 USD | 641,880,000.00 USD | 2,560,000.00 USD | 2,610,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.50` | 624,240,000.00 USD | 624,240,000.00 USD | 2,120,000.00 USD | 2,390,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2137.60` | 635,160,000.00 USD | 635,160,000.00 USD | 889,780.00 USD | 2,180,000.00 USD | 1,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2140.10` | 630,150,000.00 USD | 630,150,000.00 USD | 1,990,000.00 USD | 749,480.00 USD | 758,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.30` | 618,140,000.00 USD | 618,140,000.00 USD | 3,990,000.00 USD | 1,870,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2142.60` | 626,650,000.00 USD | 626,650,000.00 USD | 873,550.00 USD | 3,390,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2143.10` | 610,600,000.00 USD | 610,600,000.00 USD | 2,380,000.00 USD | 618,280.00 USD | 333,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 1,990,000.00 USD | 25,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2145.10` | 621,280,000.00 USD | 621,280,000.00 USD | 2,780,000.00 USD | 2,360,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2145.90` | 607,270,000.00 USD | 607,270,000.00 USD | 978,940.00 USD | 1,450,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2147.60` | 614,920,000.00 USD | 614,920,000.00 USD | 1,610,000.00 USD | 1,170,000.00 USD | 105,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2148.70` | 603,120,000.00 USD | 603,120,000.00 USD | 26,270.00 USD | 538,910.00 USD | 399,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2150.10` | 612,040,000.00 USD | 612,040,000.00 USD | 7,520,000.00 USD | 3,310,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2151.50` | 602,150,000.00 USD | 602,150,000.00 USD | 11,350,000.00 USD | 363,770.00 USD | 107,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2152.60` | 598,540,000.00 USD | 598,540,000.00 USD | 5,270,000.00 USD | 3,330,000.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.30` | 590,330,000.00 USD | 590,330,000.00 USD | 2,590,000.00 USD | 4,660,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,440,000.00 USD | 23,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2155.10` | 587,920,000.00 USD | 587,920,000.00 USD | 4,130,000.00 USD | 7,120,000.00 USD | 2,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2157.10` | 581,470,000.00 USD | 581,470,000.00 USD | 6,320,000.00 USD | 3,720,000.00 USD | 6,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2157.60` | 574,050,000.00 USD | 574,050,000.00 USD | 6,160,000.00 USD | 2,080,000.00 USD | 4,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2159.90` | 564,820,000.00 USD | 564,820,000.00 USD | 2,980,000.00 USD | 737,260.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2160.10` | 560,960,000.00 USD | 560,960,000.00 USD | 5,100,000.00 USD | 6,230,000.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2162.60` | 546,710,000.00 USD | 546,710,000.00 USD | 17,620,000.00 USD | 10,310,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2162.70` | 559,270,000.00 USD | 559,270,000.00 USD | 17,980,000.00 USD | 1,960,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 9,880,000.00 USD | 21,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2165.10` | 516,820,000.00 USD | 516,820,000.00 USD | 11,270,000.00 USD | 9,810,000.00 USD | 5,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2165.50` | 539,320,000.00 USD | 539,320,000.00 USD | 8,990,000.00 USD | 17,170,000.00 USD | 2,900,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.60` | 490,730,000.00 USD | 490,730,000.00 USD | 17,280,000.00 USD | 7,820,000.00 USD | 5,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2168.30` | 510,270,000.00 USD | 510,270,000.00 USD | 12,290,000.00 USD | 16,150,000.00 USD | 3,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.10` | 460,430,000.00 USD | 460,430,000.00 USD | 13,580,000.00 USD | 9,360,000.00 USD | 4,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2171.10` | 478,060,000.00 USD | 478,060,000.00 USD | 1,860,000.00 USD | 6,380,000.00 USD | 5,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2172.60` | 432,730,000.00 USD | 432,730,000.00 USD | 16,900,000.00 USD | 5,140,000.00 USD | 4,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.90` | 464,260,000.00 USD | 464,260,000.00 USD | 35,100,000.00 USD | 0.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 6,190,000.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.10` | 406,060,000.00 USD | 406,060,000.00 USD | 5,740,000.00 USD | 0.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2176.70` | 428,160,000.00 USD | 428,160,000.00 USD | 0.00 USD | 1,460,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2177.60` | 397,940,000.00 USD | 397,940,000.00 USD | 920,620.00 USD | 869,570.00 USD | 3,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2179.50` | 423,880,000.00 USD | 423,880,000.00 USD | 2,400,000.00 USD | 133,210.00 USD | 4,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2180.10` | 392,790,000.00 USD | 392,790,000.00 USD | 6,340,000.00 USD | 5,030,000.00 USD | 6,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2182.30` | 417,190,000.00 USD | 417,190,000.00 USD | 1,760,000.00 USD | 2,160,000.00 USD | 2,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2182.60` | 374,760,000.00 USD | 374,760,000.00 USD | 2,210,000.00 USD | 2,710,000.00 USD | 4,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 2,700,000.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2185.10` | 365,790,000.00 USD | 365,790,000.00 USD | 3,730,000.00 USD | 2,560,000.00 USD | 5,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2185.10` | 410,500,000.00 USD | 410,500,000.00 USD | 41,350,000.00 USD | 20,450,000.00 USD | 3,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2187.60` | 353,890,000.00 USD | 353,890,000.00 USD | 5,040,000.00 USD | 4,480,000.00 USD | 6,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.90` | 345,640,000.00 USD | 345,640,000.00 USD | 2,370,000.00 USD | 0.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2190.10` | 337,480,000.00 USD | 337,480,000.00 USD | 8,990,000.00 USD | 4,160,000.00 USD | 6,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.70` | 341,540,000.00 USD | 341,540,000.00 USD | 12,430,000.00 USD | 27,960,000.00 USD | 6,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2192.60` | 317,400,000.00 USD | 317,400,000.00 USD | 5,000,000.00 USD | 5,340,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2193.50` | 294,720,000.00 USD | 294,720,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 2,300,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2195.10` | 305,770,000.00 USD | 305,770,000.00 USD | 6,730,000.00 USD | 3,350,000.00 USD | 5,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.30` | 279,260,000.00 USD | 279,260,000.00 USD | 694,220.00 USD | 243,760.00 USD | 109,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2197.60` | 289,740,000.00 USD | 289,740,000.00 USD | 10,200,000.00 USD | 3,830,000.00 USD | 5,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2199.10` | 278,210,000.00 USD | 278,210,000.00 USD | 5,090,000.00 USD | 5,270,000.00 USD | 7,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.10` | 270,690,000.00 USD | 270,690,000.00 USD | 10,980,000.00 USD | 10,470,000.00 USD | 10,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2201.90` | 260,350,000.00 USD | 260,350,000.00 USD | 13,210,000.00 USD | 6,520,000.00 USD | 21,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2202.60` | 238,330,000.00 USD | 238,330,000.00 USD | 19,040,000.00 USD | 14,300,000.00 USD | 17,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2204.70` | 218,910,000.00 USD | 218,910,000.00 USD | 5,350,000.00 USD | 4,330,000.00 USD | 4,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 432,930.00 USD | 460,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.10` | 187,220,000.00 USD | 187,220,000.00 USD | 11,730,000.00 USD | 7,020,000.00 USD | 4,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2207.50` | 204,570,000.00 USD | 204,570,000.00 USD | 19,630,000.00 USD | 3,390,000.00 USD | 7,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2207.60` | 163,590,000.00 USD | 163,590,000.00 USD | 13,820,000.00 USD | 6,420,000.00 USD | 5,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.10` | 137,760,000.00 USD | 137,760,000.00 USD | 4,040,000.00 USD | 7,220,000.00 USD | 6,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2210.30` | 174,360,000.00 USD | 174,360,000.00 USD | 4,740,000.00 USD | 0.00 USD | 11,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.60` | 120,100,000.00 USD | 120,100,000.00 USD | 12,700,000.00 USD | 6,410,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2213.10` | 158,050,000.00 USD | 158,050,000.00 USD | 1,710,000.00 USD | 1,980,000.00 USD | 8,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 27,590.00 USD | 27,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2215.10` | 98,990,000.00 USD | 98,990,000.00 USD | 2,300,000.00 USD | 2,930,000.00 USD | 280,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2215.90` | 145,510,000.00 USD | 145,510,000.00 USD | 0.00 USD | 0.00 USD | 565,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2217.60` | 93,480,000.00 USD | 93,480,000.00 USD | 2,810,000.00 USD | 4,440,000.00 USD | 3,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2218.70` | 144,950,000.00 USD | 144,950,000.00 USD | 23,020,000.00 USD | 487,520.00 USD | 218,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2220.10` | 82,300,000.00 USD | 82,300,000.00 USD | 17,480,000.00 USD | 7,250,000.00 USD | 4,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2221.50` | 121,220,000.00 USD | 121,220,000.00 USD | 10,170,000.00 USD | 19,850,000.00 USD | 19,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2222.60` | 53,360,000.00 USD | 53,360,000.00 USD | 8,350,000.00 USD | 14,430,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2224.30` | 72,200,000.00 USD | 72,200,000.00 USD | 8,200,000.00 USD | 12,510,000.00 USD | 6,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2225.10` | 28,940,000.00 USD | 28,940,000.00 USD | 5,440,000.00 USD | 2,560,000.00 USD | 3,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2227.10` | 44,970,000.00 USD | 44,970,000.00 USD | 557,870.00 USD | 0.00 USD | 6,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.60` | 17,670,000.00 USD | 17,670,000.00 USD | 2,850,000.00 USD | 0.00 USD | 111,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.90` | 37,550,000.00 USD | 37,550,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.10` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 0.00 USD | 113,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2232.60` | 14,600,000.00 USD | 14,600,000.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2235.50` | 35,640,000.00 USD | 35,640,000.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2237.60` | 8,650,000.00 USD | 8,650,000.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2238.30` | 10,750,000.00 USD | 10,750,000.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2240.10` | 649,520.00 USD | 649,520.00 USD | 0.00 USD | 0.00 USD | 21,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2242.60` | 627,550.00 USD | 627,550.00 USD | 0.00 USD | 0.00 USD | 22,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2243.90` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 268,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2245.10` | 605,070.00 USD | 605,070.00 USD | 0.00 USD | 0.00 USD | 62,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2246.70` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 1,300,000.00 USD | 709,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2247.60` | 542,830.00 USD | 542,830.00 USD | 0.00 USD | 243,170.00 USD | 299,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2249.50` | 4,390,000.00 USD | 4,390,000.00 USD | 861,640.00 USD | 2,660,000.00 USD | 867,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2250.10` | 2,390,000.00 USD | 2,390,000.00 USD | 255,300.00 USD | 446,930.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2252.30` | 29,660,000.00 USD | 29,660,000.00 USD | 10,050,000.00 USD | 11,670,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2252.60` | 10,580,000.00 USD | 10,580,000.00 USD | 1,470,000.00 USD | 3,300,000.00 USD | 3,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 20,070.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2255.10` | 35,630,000.00 USD | 35,630,000.00 USD | 12,360,000.00 USD | 6,830,000.00 USD | 5,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2255.10` | 47,080,000.00 USD | 47,080,000.00 USD | 10,050,000.00 USD | 6,600,000.00 USD | 774,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2257.60` | 69,780,000.00 USD | 69,780,000.00 USD | 19,980,000.00 USD | 8,290,000.00 USD | 5,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2257.90` | 86,780,000.00 USD | 86,780,000.00 USD | 20,510,000.00 USD | 12,290,000.00 USD | 6,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2260.10` | 91,850,000.00 USD | 91,850,000.00 USD | 9,050,000.00 USD | 10,340,000.00 USD | 2,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2260.70` | 91,100,000.00 USD | 91,100,000.00 USD | 0.00 USD | 0.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2262.60` | 120,240,000.00 USD | 120,240,000.00 USD | 15,390,000.00 USD | 6,760,000.00 USD | 6,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2263.50` | 100,120,000.00 USD | 100,120,000.00 USD | 7,340,000.00 USD | 1,460,000.00 USD | 218,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 34,370.00 USD | 54,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2265.10` | 166,340,000.00 USD | 166,340,000.00 USD | 19,500,000.00 USD | 16,750,000.00 USD | 9,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2266.30` | 132,540,000.00 USD | 132,540,000.00 USD | 10,170,000.00 USD | 15,790,000.00 USD | 6,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2267.60` | 222,280,000.00 USD | 222,280,000.00 USD | 20,700,000.00 USD | 22,510,000.00 USD | 12,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2269.10` | 188,720,000.00 USD | 188,720,000.00 USD | 19,210,000.00 USD | 12,640,000.00 USD | 24,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2270.10` | 281,760,000.00 USD | 281,760,000.00 USD | 23,390,000.00 USD | 12,160,000.00 USD | 23,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2271.90` | 217,620,000.00 USD | 217,620,000.00 USD | 18,240,000.00 USD | 3,640,000.00 USD | 7,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2272.60` | 312,680,000.00 USD | 312,680,000.00 USD | 19,020,000.00 USD | 5,610,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2274.70` | 245,920,000.00 USD | 245,920,000.00 USD | 19,630,000.00 USD | 6,900,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 791,770.00 USD | 846,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2275.10` | 360,200,000.00 USD | 360,200,000.00 USD | 27,310,000.00 USD | 15,610,000.00 USD | 4,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2277.50` | 272,300,000.00 USD | 272,300,000.00 USD | 6,890,000.00 USD | 8,890,000.00 USD | 10,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2277.60` | 397,830,000.00 USD | 397,830,000.00 USD | 10,430,000.00 USD | 15,200,000.00 USD | 11,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2280.10` | 446,320,000.00 USD | 446,320,000.00 USD | 26,670,000.00 USD | 9,750,000.00 USD | 12,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2280.30` | 316,620,000.00 USD | 316,620,000.00 USD | 854,200.00 USD | 39,830,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2282.60` | 500,850,000.00 USD | 500,850,000.00 USD | 22,560,000.00 USD | 24,830,000.00 USD | 7,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2283.10` | 408,440,000.00 USD | 408,440,000.00 USD | 5,600,000.00 USD | 72,520,000.00 USD | 13,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 235,710.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2285.10` | 528,700,000.00 USD | 528,700,000.00 USD | 11,520,000.00 USD | 9,410,000.00 USD | 6,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2285.90` | 412,450,000.00 USD | 412,450,000.00 USD | 1,320,000.00 USD | 2,590,000.00 USD | 109,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2287.60` | 567,910,000.00 USD | 567,910,000.00 USD | 19,470,000.00 USD | 11,060,000.00 USD | 8,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2288.70` | 454,050,000.00 USD | 454,050,000.00 USD | 13,470,000.00 USD | 13,140,000.00 USD | 15,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2290.10` | 613,830,000.00 USD | 613,830,000.00 USD | 19,770,000.00 USD | 21,020,000.00 USD | 5,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2291.50` | 479,370,000.00 USD | 479,370,000.00 USD | 8,400,000.00 USD | 6,770,000.00 USD | 10,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2292.60` | 647,810,000.00 USD | 647,810,000.00 USD | 17,860,000.00 USD | 4,710,000.00 USD | 11,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2294.30` | 500,700,000.00 USD | 500,700,000.00 USD | 14,670,000.00 USD | 1,490,000.00 USD | 5,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 3,490,000.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2295.10` | 684,420,000.00 USD | 684,420,000.00 USD | 12,280,000.00 USD | 13,600,000.00 USD | 10,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2297.10` | 550,450,000.00 USD | 550,450,000.00 USD | 25,900,000.00 USD | 8,070,000.00 USD | 15,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2297.60` | 730,750,000.00 USD | 730,750,000.00 USD | 29,190,000.00 USD | 11,160,000.00 USD | 5,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.90` | 593,370,000.00 USD | 593,370,000.00 USD | 16,200,000.00 USD | 20,940,000.00 USD | 5,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2300.10` | 770,270,000.00 USD | 770,270,000.00 USD | 11,250,000.00 USD | 14,710,000.00 USD | 13,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.60` | 797,870,000.00 USD | 797,870,000.00 USD | 16,060,000.00 USD | 2,700,000.00 USD | 8,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.70` | 648,040,000.00 USD | 648,040,000.00 USD | 26,960,000.00 USD | 10,860,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 310,530.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.10` | 836,610,000.00 USD | 836,610,000.00 USD | 14,970,000.00 USD | 17,660,000.00 USD | 6,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.50` | 674,050,000.00 USD | 674,050,000.00 USD | 6,340,000.00 USD | 8,820,000.00 USD | 10,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2307.60` | 847,900,000.00 USD | 847,900,000.00 USD | 4,390,000.00 USD | 3,680,000.00 USD | 3,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2308.30` | 676,350,000.00 USD | 676,350,000.00 USD | 1,240,000.00 USD | 930,630.00 USD | 134,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2310.10` | 866,410,000.00 USD | 866,410,000.00 USD | 4,990,000.00 USD | 2,820,000.00 USD | 10,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2311.10` | 706,850,000.00 USD | 706,850,000.00 USD | 11,560,000.00 USD | 2,790,000.00 USD | 16,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2312.60` | 882,980,000.00 USD | 882,980,000.00 USD | 6,950,000.00 USD | 8,040,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2313.90` | 717,670,000.00 USD | 717,670,000.00 USD | 1,100,000.00 USD | 7,460,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 1,030,000.00 USD | 5,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2315.10` | 905,530,000.00 USD | 905,530,000.00 USD | 5,980,000.00 USD | 13,500,000.00 USD | 3,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2316.70` | 723,430,000.00 USD | 723,430,000.00 USD | 1,020,000.00 USD | 3,640,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2317.60` | 932,690,000.00 USD | 932,690,000.00 USD | 8,220,000.00 USD | 10,500,000.00 USD | 8,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.50` | 753,590,000.00 USD | 753,590,000.00 USD | 5,530,000.00 USD | 15,850,000.00 USD | 8,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.10` | 958,540,000.00 USD | 958,540,000.00 USD | 10,150,000.00 USD | 12,260,000.00 USD | 3,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.30` | 759,510,000.00 USD | 759,510,000.00 USD | 2,300,000.00 USD | 3,450,000.00 USD | 172,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2322.60` | 976,490,000.00 USD | 976,490,000.00 USD | 3,370,000.00 USD | 9,320,000.00 USD | 5,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 3,580,000.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2325.10` | 990,410,000.00 USD | 990,410,000.00 USD | 3,060,000.00 USD | 9,360,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2325.10` | 782,540,000.00 USD | 782,540,000.00 USD | 10,150,000.00 USD | 2,770,000.00 USD | 10,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2327.60` | 996,970,000.00 USD | 996,970,000.00 USD | 553,100.00 USD | 1,410,000.00 USD | 4,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2327.90` | 794,430,000.00 USD | 794,430,000.00 USD | 3,860,000.00 USD | 0.00 USD | 8,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2330.10` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 11,750,000.00 USD | 3,450,000.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2330.70` | 810,810,000.00 USD | 810,810,000.00 USD | 15,960,000.00 USD | 363,770.00 USD | 54,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2332.60` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 5,020,000.00 USD | 3,500,000.00 USD | 6,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2333.50` | 856,150,000.00 USD | 856,150,000.00 USD | 22,570,000.00 USD | 14,770,000.00 USD | 7,990,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 79,270.00 USD | 9,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2335.10` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 11,180,000.00 USD | 7,590,000.00 USD | 5,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2336.30` | 900,360,000.00 USD | 900,360,000.00 USD | 26,590,000.00 USD | 10,690,000.00 USD | 6,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2337.60` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 14,050,000.00 USD | 1,830,000.00 USD | 6,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2339.10` | 926,760,000.00 USD | 926,760,000.00 USD | 14,040,000.00 USD | 0.00 USD | 12,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2340.10` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 11,670,000.00 USD | 6,260,000.00 USD | 12,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2341.90` | 967,190,000.00 USD | 967,190,000.00 USD | 8,610,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2342.60` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 8,670,000.00 USD | 4,470,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2344.70` | 995,110,000.00 USD | 995,110,000.00 USD | 2,480,000.00 USD | 16,920,000.00 USD | 8,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 550,680.00 USD | 10,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2345.10` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 5,430,000.00 USD | 8,130,000.00 USD | 8,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2347.50` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 8,220,000.00 USD | 18,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2347.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 1,960,000.00 USD | 3,520,000.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.10` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 23,260,000.00 USD | 6,880,000.00 USD | 10,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2350.30` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 1,630,000.00 USD | 20,110,000.00 USD | 15,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2352.60` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 5,150,000.00 USD | 3,400,000.00 USD | 2,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2353.10` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 2,710,000.00 USD | 35,770,000.00 USD | 4,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,280,000.00 USD | 11,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2355.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 2,320,000.00 USD | 3,770,000.00 USD | 951,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2355.90` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 18,560,000.00 USD | 10,720,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 3,780,000.00 USD | 4,290,000.00 USD | 3,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.70` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 6,870,000.00 USD | 512,220.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.10` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 9,090,000.00 USD | 4,260,000.00 USD | 5,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.50` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 3,150,000.00 USD | 3,430,000.00 USD | 374,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.60` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 8,700,000.00 USD | 6,710,000.00 USD | 7,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2364.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 3,860,000.00 USD | 373,740.00 USD | 10,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 3,970,000.00 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2365.10` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 4,830,000.00 USD | 3,010,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2367.10` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 307,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.60` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 2,910,000.00 USD | 1,110,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2369.90` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 24,940,000.00 USD | 475,460.00 USD | 18,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.10` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 10,250,000.00 USD | 7,700,000.00 USD | 4,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.60` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 11,280,000.00 USD | 1,790,000.00 USD | 4,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2372.70` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 15,600,000.00 USD | 0.00 USD | 39,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 1,760,000.00 USD | 17,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2375.10` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 5,700,000.00 USD | 557,400.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2375.50` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 9,700,000.00 USD | 1,050,000.00 USD | 11,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2377.60` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 3,340,000.00 USD | 3,070,000.00 USD | 4,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.30` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 11,180,000.00 USD | 7,020,000.00 USD | 23,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.10` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 6,310,000.00 USD | 389,290.00 USD | 4,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.10` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 4,540,000.00 USD | 2,390,000.00 USD | 16,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2382.60` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 15,650,000.00 USD | 14,510,000.00 USD | 11,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2383.90` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 8,840,000.00 USD | 21,750,000.00 USD | 30,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 1,890,000.00 USD | 19,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.10` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 7,540,000.00 USD | 11,520,000.00 USD | 4,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2386.70` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 17,720,000.00 USD | 32,140,000.00 USD | 42,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2387.60` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 9,850,000.00 USD | 5,970,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2389.50` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 5,670,000.00 USD | 35,860,000.00 USD | 28,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.10` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 4,390,000.00 USD | 3,310,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2392.30` | 1,700,000,000.00 USD | 1,700,000,000.00 USD | 26,840,000.00 USD | 45,530,000.00 USD | 39,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.60` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 2,380,000.00 USD | 2,660,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,870,000.00 USD | 23,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2395.10` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 2,380,000.00 USD | 2,830,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2395.10` | 1,790,000,000.00 USD | 1,790,000,000.00 USD | 39,180,000.00 USD | 24,870,000.00 USD | 29,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2397.60` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 64,150.00 USD | 3,720,000.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2397.90` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 34,290,000.00 USD | 36,430,000.00 USD | 23,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2400.10` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 2,150,000.00 USD | 637,690.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2400.70` | 1,980,000,000.00 USD | 1,980,000,000.00 USD | 42,030,000.00 USD | 25,390,000.00 USD | 24,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2402.60` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 1,140,000.00 USD | 315,710.00 USD | 552,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2403.50` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 51,300,000.00 USD | 24,760,000.00 USD | 30,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 225,400.00 USD | 24,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2405.10` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 5,960,000.00 USD | 3,440,000.00 USD | 4,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2406.30` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 29,700,000.00 USD | 33,710,000.00 USD | 14,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2407.60` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 6,810,000.00 USD | 3,500,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2409.10` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 25,090,000.00 USD | 21,480,000.00 USD | 27,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.10` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 4,520,000.00 USD | 3,540,000.00 USD | 3,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.90` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 15,970,000.00 USD | 21,640,000.00 USD | 13,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2412.60` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 4,850,000.00 USD | 2,970,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.70` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 22,250,000.00 USD | 19,630,000.00 USD | 21,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 116,740.00 USD | 24,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.10` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 2,080,000.00 USD | 1,890,000.00 USD | 2,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2417.50` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 22,310,000.00 USD | 8,700,000.00 USD | 21,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2417.60` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 2,060,000.00 USD | 1,260,000.00 USD | 599,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2420.10` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 5,060,000.00 USD | 2,860,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2420.30` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 29,980,000.00 USD | 18,780,000.00 USD | 9,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.60` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 693,410.00 USD | 2,620,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2423.10` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 17,920,000.00 USD | 17,260,000.00 USD | 17,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 435,780.00 USD | 24,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.10` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 510,650.00 USD | 623,850.00 USD | 888,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2425.90` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 12,980,000.00 USD | 15,010,000.00 USD | 17,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2427.60` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 2,250,000.00 USD | 1,520,000.00 USD | 603,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2428.70` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 12,800,000.00 USD | 7,090,000.00 USD | 8,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.10` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 1,370,000.00 USD | 1,550,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.50` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 9,420,000.00 USD | 12,660,000.00 USD | 8,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.60` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 2,770,000.00 USD | 2,230,000.00 USD | 691,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.30` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 8,200,000.00 USD | 3,830,000.00 USD | 3,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 532,800.00 USD | 25,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.10` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 2,480,000.00 USD | 559,660.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.10` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 7,130,000.00 USD | 7,440,000.00 USD | 6,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2437.60` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 1,360,000.00 USD | 1,040,000.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2439.90` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 12,730,000.00 USD | 4,970,000.00 USD | 3,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.10` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 1,240,000.00 USD | 502,040.00 USD | 304,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2442.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 1,040,000.00 USD | 743,640.00 USD | 827,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2442.70` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 5,050,000.00 USD | 5,320,000.00 USD | 7,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 1,630,000.00 USD | 26,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.10` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 218,020.00 USD | 703,990.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2445.50` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 9,990,000.00 USD | 7,470,000.00 USD | 10,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2447.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 1,210,000.00 USD | 751,450.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2448.30` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 10,750,000.00 USD | 3,620,000.00 USD | 13,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.10` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 627,630.00 USD | 311,480.00 USD | 35,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.10` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 8,450,000.00 USD | 7,240,000.00 USD | 7,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2452.60` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 3,200,000.00 USD | 1,840,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2453.90` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 4,220,000.00 USD | 2,980,000.00 USD | 3,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 194,210.00 USD | 27,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.10` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 2,270,000.00 USD | 1,990,000.00 USD | 994,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2456.70` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 5,900,000.00 USD | 7,380,000.00 USD | 7,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2457.60` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 1,770,000.00 USD | 1,980,000.00 USD | 845,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2459.50` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 3,220,000.00 USD | 4,870,000.00 USD | 6,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2460.10` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 1,530,000.00 USD | 1,370,000.00 USD | 388,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2462.30` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 6,600,000.00 USD | 5,990,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2462.60` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 413,060.00 USD | 629,460.00 USD | 851,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 16,250,000.00 USD | 43,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2465.10` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 1,090,000.00 USD | 1,050,000.00 USD | 525,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2465.10` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 4,960,000.00 USD | 3,130,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2467.60` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 1,140,000.00 USD | 1,580,000.00 USD | 391,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.90` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 3,830,000.00 USD | 2,330,000.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.10` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 1,440,000.00 USD | 2,220,000.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.70` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 4,870,000.00 USD | 3,000,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2472.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 653,960.00 USD | 275,370.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2473.50` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 5,300,000.00 USD | 2,920,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 54,870,000.00 USD | 98,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2475.10` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 595,510.00 USD | 914,780.00 USD | 231,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2476.30` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 2,070,000.00 USD | 1,710,000.00 USD | 872,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2477.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 2,200,000.00 USD | 405,410.00 USD | 156,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2479.10` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 3,070,000.00 USD | 4,130,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2480.10` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 567,450.00 USD | 943,540.00 USD | 731,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2481.90` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 601,420.00 USD | 3,680,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.70` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 41,090.00 USD | 98,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2487.50` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.30` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 338,890.00 USD | 286,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2491.80` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 2,580,000.00 USD | 733,870.00 USD | 445,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 1,740,000.00 USD | 99,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2505.00` | 4,900,000.00 USD | 104,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2515.00` | 60,730.00 USD | 104,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2525.00` | 79,800.00 USD | 104,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2535.00` | 1,060,000.00 USD | 106,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2545.00` | 5,080,000.00 USD | 111,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2555.00` | 262,820.00 USD | 111,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2565.00` | 38,980.00 USD | 111,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2575.00` | 45,990.00 USD | 111,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,690,000.00 USD | 138,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2595.00` | 8,000,000.00 USD | 146,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2605.00` | 5,810,000.00 USD | 151,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2615.00` | 12,770,000.00 USD | 164,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2625.00` | 6,640,000.00 USD | 171,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2635.00` | 1,480,000.00 USD | 172,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 860,740.00 USD | 173,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 398,020.00 USD | 174,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 462,390.00 USD | 174,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 1,590,000.00 USD | 176,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 17,400.00 USD | 176,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 275,120.00 USD | 176,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 1,270,000.00 USD | 177,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 533,790.00 USD | 178,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 409,700.00 USD | 178,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 435,040.00 USD | 179,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 13,800,000.00 USD | 192,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 35,320,000.00 USD | 228,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 376,890.00 USD | 228,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 405,060.00 USD | 229,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 5,570,000.00 USD | 234,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 22,260.00 USD | 234,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 5,280,000.00 USD | 239,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 1,890,000.00 USD | 241,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 106,590.00 USD | 241,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 6,290,000.00 USD | 248,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 121,050.00 USD | 248,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 1,090,000.00 USD | 249,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 50,400.00 USD | 249,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 43,550,000.00 USD | 292,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 2,080,000.00 USD | 295,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 533,420.00 USD | 295,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 1,200,000.00 USD | 296,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 2,750,000.00 USD | 299,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 24,140.00 USD | 299,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 182,240.00 USD | 299,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 412,780.00 USD | 300,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 280,690.00 USD | 300,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 3,890,000.00 USD | 304,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 18,050.00 USD | 304,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 2,370,000.00 USD | 306,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 14,980,000.00 USD | 321,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 559,150.00 USD | 322,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 163,470.00 USD | 322,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 2,090,000.00 USD | 324,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 12,810,000.00 USD | 337,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 947,940.00 USD | 338,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 2,180,000.00 USD | 340,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 1,510,000.00 USD | 341,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 11,210,000.00 USD | 353,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 7,870,000.00 USD | 361,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 6,890,000.00 USD | 367,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 12,140,000.00 USD | 380,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 1,750,000.00 USD | 381,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 116,140.00 USD | 381,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 600,340.00 USD | 382,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 35,850.00 USD | 382,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 3,250,000.00 USD | 385,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 29,530,000.00 USD | 415,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 9,000,000.00 USD | 424,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 70,710,000.00 USD | 495,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 230,850.00 USD | 495,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 106,300.00 USD | 495,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 335,380.00 USD | 495,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 35,870.00 USD | 495,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 18,000,000.00 USD | 513,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 182,250.00 USD | 513,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 1,530,000.00 USD | 515,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 4,780,000.00 USD | 520,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 8,450,000.00 USD | 528,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 118,750.00 USD | 528,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 2,080,000.00 USD | 530,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 2,850,000.00 USD | 533,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 6,270,000.00 USD | 540,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 260,460.00 USD | 540,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 29,130,000.00 USD | 569,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 372,490.00 USD | 569,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 2,510,000.00 USD | 572,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 4,340,000.00 USD | 576,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 3,250.00 USD | 576,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 102,400.00 USD | 576,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 1,130,000.00 USD | 577,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 402,390.00 USD | 578,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 1,850,000.00 USD | 580,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 15,090,000.00 USD | 595,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 739,940.00 USD | 595,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 2,740,000.00 USD | 598,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 473,740.00 USD | 599,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 65,160.00 USD | 599,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 57,870.00 USD | 599,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 14,200,000.00 USD | 613,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 1,300,000.00 USD | 614,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 1,390,000.00 USD | 616,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 691,460.00 USD | 616,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 167,320.00 USD | 617,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 244,270.00 USD | 617,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 30,420.00 USD | 617,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 178,820.00 USD | 617,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 55,400.00 USD | 617,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 80,150.00 USD | 617,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 2,840,000.00 USD | 620,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 118,080.00 USD | 620,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 1,010.00 USD | 620,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 3,790,000.00 USD | 624,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 9,700,000.00 USD | 634,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 73,410.00 USD | 634,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 6,560,000.00 USD | 640,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 54,100,000.00 USD | 694,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 12,160.00 USD | 694,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 347,420.00 USD | 695,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 222,990.00 USD | 695,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 383,100,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 102,260.00 USD | 1,080,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 2,100.00 USD | 1,080,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 234,460.00 USD | 1,080,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 3,780,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 7,650,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 80,890.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 2,640,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 57,020,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 3,170,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 1,250,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 8,090.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 27,530.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 115,860.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 281,470.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 3,430,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 67,010.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 817,060.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 39,470,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 266,110.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 971,390.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 2,580,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 197,460.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 5,050.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 24,650.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 1,760.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 5,480.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 241,590.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 600,020.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 607,880.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 52,680.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 1,810,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 702,730.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 1,120,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 48,020.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 1,620,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 70,150.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 271,220.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 451,090.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 9,770.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 535,670.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 3,810.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 64,130.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 196,720.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 774,090.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 40,030.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 123,950.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 92,210.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 854,050.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 32,940,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 82,260.00 USD | 1,250,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 83,090,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 16,670.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 1,530,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 420.39 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 58,530.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 766,900.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 5,810.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 5,560.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 153,740.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 248,420.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 116,150.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 152,480.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 598,750.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 1,010,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 448,590.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 178,700.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 81,540.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 42,140.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 116,160.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 22,970.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4455.00` | 390,430.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4465.00` | 75,710.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4475.00` | 37,040.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4485.00` | 18,450.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4495.00` | 138,480.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `455.00` | 784,540,000.00 USD | 0.00 USD | 80,660.00 USD | `-79.77%` | `177.28` |
| `Live` | `Long` | `465.00` | 784,460,000.00 USD | 0.00 USD | 6,190.00 USD | `-79.32%` | `13.30` |
| `Live` | `Long` | `475.00` | 784,460,000.00 USD | 0.00 USD | 70,920.00 USD | `-78.88%` | `149.30` |
| `Live` | `Long` | `485.00` | 784,390,000.00 USD | 0.00 USD | 108,780.00 USD | `-78.43%` | `224.30` |
| `Live` | `Long` | `495.00` | 784,280,000.00 USD | 0.00 USD | 19,900.00 USD | `-77.99%` | `40.21` |
| `Live` | `Long` | `505.00` | 784,260,000.00 USD | 0.00 USD | 65,690.00 USD | `-77.55%` | `130.08` |
| `Live` | `Long` | `515.00` | 784,190,000.00 USD | 0.00 USD | 1,830,000.00 USD | `-77.10%` | `3,561.68` |
| `Live` | `Long` | `525.00` | 782,360,000.00 USD | 0.00 USD | 38,160.00 USD | `-76.66%` | `72.69` |
| `Live` | `Long` | `535.00` | 782,320,000.00 USD | 0.00 USD | 8,790.00 USD | `-76.21%` | `16.42` |
| `Live` | `Long` | `545.00` | 782,310,000.00 USD | 0.00 USD | 13,630.00 USD | `-75.77%` | `25.01` |
| `Live` | `Long` | `555.00` | 782,300,000.00 USD | 0.00 USD | 106,590.00 USD | `-75.32%` | `192.05` |
| `Live` | `Long` | `565.00` | 782,190,000.00 USD | 0.00 USD | 150,140.00 USD | `-74.88%` | `265.74` |
| `Live` | `Long` | `575.00` | 782,040,000.00 USD | 0.00 USD | 12,360.00 USD | `-74.43%` | `21.49` |
| `Live` | `Long` | `585.00` | 782,030,000.00 USD | 0.00 USD | 2,850,000.00 USD | `-73.99%` | `4,867.66` |
| `Live` | `Long` | `595.00` | 779,180,000.00 USD | 0.00 USD | 554,380.00 USD | `-73.54%` | `931.73` |
| `Live` | `Long` | `605.00` | 778,630,000.00 USD | 0.00 USD | 1,830,000.00 USD | `-73.10%` | `3,017.99` |
| `Live` | `Long` | `615.00` | 776,800,000.00 USD | 0.00 USD | 57,360.00 USD | `-72.65%` | `93.26` |
| `Live` | `Long` | `625.00` | 776,740,000.00 USD | 0.00 USD | 1,080,000.00 USD | `-72.21%` | `1,732.80` |
| `Live` | `Long` | `635.00` | 775,660,000.00 USD | 0.00 USD | 15,580.00 USD | `-71.77%` | `24.54` |
| `Live` | `Long` | `645.00` | 775,640,000.00 USD | 0.00 USD | 339,590.00 USD | `-71.32%` | `526.49` |
| `Live` | `Long` | `655.00` | 775,310,000.00 USD | 0.00 USD | 51,390.00 USD | `-70.88%` | `78.45` |
| `Live` | `Long` | `665.00` | 775,250,000.00 USD | 0.00 USD | 105,210.00 USD | `-70.43%` | `158.21` |
| `Live` | `Long` | `675.00` | 775,150,000.00 USD | 0.00 USD | 15,070.00 USD | `-69.99%` | `22.33` |
| `Live` | `Long` | `685.00` | 775,130,000.00 USD | 0.00 USD | 32,820.00 USD | `-69.54%` | `47.91` |
| `Live` | `Long` | `695.00` | 775,100,000.00 USD | 0.00 USD | 11,490.00 USD | `-69.10%` | `16.53` |
| `Live` | `Long` | `705.00` | 775,090,000.00 USD | 0.00 USD | 51,810.00 USD | `-68.65%` | `73.49` |
| `Live` | `Long` | `715.00` | 775,040,000.00 USD | 0.00 USD | 1,810.00 USD | `-68.21%` | `2.53` |
| `Live` | `Long` | `725.00` | 775,040,000.00 USD | 0.00 USD | 405,280.00 USD | `-67.76%` | `559.01` |
| `Live` | `Long` | `735.00` | 774,630,000.00 USD | 0.00 USD | 66,120.00 USD | `-67.32%` | `89.96` |
| `Live` | `Long` | `745.00` | 774,560,000.00 USD | 0.00 USD | 7,820.00 USD | `-66.87%` | `10.50` |
| `Live` | `Long` | `755.00` | 774,560,000.00 USD | 0.00 USD | 38,260.00 USD | `-66.43%` | `50.68` |
| `Live` | `Long` | `765.00` | 774,520,000.00 USD | 0.00 USD | 7,720.00 USD | `-65.98%` | `10.09` |
| `Live` | `Long` | `775.00` | 774,510,000.00 USD | 0.00 USD | 4,390.00 USD | `-65.54%` | `5.66` |
| `Live` | `Long` | `785.00` | 774,510,000.00 USD | 0.00 USD | 20,660.00 USD | `-65.10%` | `26.32` |
| `Live` | `Long` | `795.00` | 774,490,000.00 USD | 0.00 USD | 84,530.00 USD | `-64.65%` | `106.32` |
| `Live` | `Long` | `805.00` | 774,400,000.00 USD | 0.00 USD | 47,650.00 USD | `-64.21%` | `59.19` |
| `Live` | `Long` | `815.00` | 774,350,000.00 USD | 0.00 USD | 98,180.00 USD | `-63.76%` | `120.46` |
| `Live` | `Long` | `825.00` | 774,260,000.00 USD | 0.00 USD | 845,300.00 USD | `-63.32%` | `1,024.60` |
| `Live` | `Long` | `835.00` | 773,410,000.00 USD | 0.00 USD | 88,670.00 USD | `-62.87%` | `106.19` |
| `Live` | `Long` | `845.00` | 773,320,000.00 USD | 0.00 USD | 92,370.00 USD | `-62.43%` | `109.31` |
| `Live` | `Long` | `855.00` | 773,230,000.00 USD | 0.00 USD | 95,080.00 USD | `-61.98%` | `111.21` |
| `Live` | `Long` | `865.00` | 773,130,000.00 USD | 0.00 USD | 85,930.00 USD | `-61.54%` | `99.34` |
| `Live` | `Long` | `875.00` | 773,050,000.00 USD | 0.00 USD | 404,280.00 USD | `-61.09%` | `462.03` |
| `Live` | `Long` | `885.00` | 772,640,000.00 USD | 0.00 USD | 1,200,000.00 USD | `-60.65%` | `1,360.87` |
| `Live` | `Long` | `895.00` | 771,440,000.00 USD | 0.00 USD | 115,430.00 USD | `-60.20%` | `128.98` |
| `Live` | `Long` | `905.00` | 771,320,000.00 USD | 0.00 USD | 131,400.00 USD | `-59.76%` | `145.19` |
| `Live` | `Long` | `915.00` | 771,190,000.00 USD | 0.00 USD | 166,190.00 USD | `-59.32%` | `181.63` |
| `Live` | `Long` | `925.00` | 771,030,000.00 USD | 0.00 USD | 168,790.00 USD | `-58.87%` | `182.48` |
| `Live` | `Long` | `935.00` | 770,860,000.00 USD | 0.00 USD | 84,000.00 USD | `-58.43%` | `89.84` |
| `Live` | `Long` | `945.00` | 770,770,000.00 USD | 0.00 USD | 62,450.00 USD | `-57.98%` | `66.08` |
| `Live` | `Long` | `955.00` | 770,710,000.00 USD | 0.00 USD | 27,560.00 USD | `-57.54%` | `28.86` |
| `Live` | `Long` | `965.00` | 770,680,000.00 USD | 0.00 USD | 483,050.00 USD | `-57.09%` | `500.57` |
| `Live` | `Long` | `975.00` | 770,200,000.00 USD | 0.00 USD | 144,850.00 USD | `-56.65%` | `148.57` |
| `Live` | `Long` | `985.00` | 770,060,000.00 USD | 0.00 USD | 215,460.00 USD | `-56.20%` | `218.74` |
| `Live` | `Long` | `995.00` | 769,840,000.00 USD | 0.00 USD | 72,670.00 USD | `-55.76%` | `73.03` |
| `Live` | `Long` | `1005.00` | 769,770,000.00 USD | 0.00 USD | 21,150.00 USD | `-55.31%` | `21.04` |
| `Live` | `Long` | `1015.00` | 769,750,000.00 USD | 0.00 USD | 345,840.00 USD | `-54.87%` | `340.73` |
| `Live` | `Long` | `1025.00` | 769,400,000.00 USD | 0.00 USD | 54,250.00 USD | `-54.42%` | `52.93` |
| `Live` | `Long` | `1035.00` | 769,350,000.00 USD | 0.00 USD | 275,540.00 USD | `-53.98%` | `266.23` |
| `Live` | `Long` | `1045.00` | 769,070,000.00 USD | 0.00 USD | 396,790.00 USD | `-53.53%` | `379.70` |
| `Live` | `Long` | `1055.00` | 768,670,000.00 USD | 0.00 USD | 9,530,000.00 USD | `-53.09%` | `9,034.88` |
| `Live` | `Long` | `1065.00` | 759,140,000.00 USD | 0.00 USD | 127,940.00 USD | `-52.65%` | `120.13` |
| `Live` | `Long` | `1075.00` | 759,010,000.00 USD | 0.00 USD | 671,120.00 USD | `-52.20%` | `624.30` |
| `Live` | `Long` | `1085.00` | 758,340,000.00 USD | 0.00 USD | 868,060.00 USD | `-51.76%` | `800.05` |
| `Live` | `Long` | `1095.00` | 757,470,000.00 USD | 0.00 USD | 38,740.00 USD | `-51.31%` | `35.38` |
| `Live` | `Long` | `1105.00` | 757,440,000.00 USD | 0.00 USD | 137,420.00 USD | `-50.87%` | `124.36` |
| `Live` | `Long` | `1115.00` | 757,300,000.00 USD | 0.00 USD | 7,860,000.00 USD | `-50.42%` | `7,051.32` |
| `Live` | `Long` | `1125.00` | 749,440,000.00 USD | 0.00 USD | 176,230.00 USD | `-49.98%` | `156.64` |
| `Live` | `Long` | `1135.00` | 749,260,000.00 USD | 0.00 USD | 1,740,000.00 USD | `-49.53%` | `1,536.04` |
| `Live` | `Long` | `1145.00` | 747,520,000.00 USD | 0.00 USD | 214,200.00 USD | `-49.09%` | `187.07` |
| `Live` | `Long` | `1155.00` | 747,300,000.00 USD | 0.00 USD | 537,840.00 USD | `-48.64%` | `465.66` |
| `Live` | `Long` | `1165.00` | 746,760,000.00 USD | 0.00 USD | 51,500.00 USD | `-48.20%` | `44.20` |
| `Live` | `Long` | `1175.00` | 746,710,000.00 USD | 0.00 USD | 1,560,000.00 USD | `-47.75%` | `1,328.41` |
| `Live` | `Long` | `1185.00` | 745,150,000.00 USD | 0.00 USD | 1,270,000.00 USD | `-47.31%` | `1,067.75` |
| `Live` | `Long` | `1195.00` | 743,890,000.00 USD | 0.00 USD | 7,200,000.00 USD | `-46.87%` | `6,024.50` |
| `Live` | `Long` | `1205.00` | 736,690,000.00 USD | 0.00 USD | 2,020,000.00 USD | `-46.42%` | `1,673.31` |
| `Live` | `Long` | `1215.00` | 734,670,000.00 USD | 0.00 USD | 78,020.00 USD | `-45.98%` | `64.21` |
| `Live` | `Long` | `1225.00` | 734,590,000.00 USD | 0.00 USD | 432,140.00 USD | `-45.53%` | `352.77` |
| `Live` | `Long` | `1235.00` | 734,160,000.00 USD | 0.00 USD | 138,120.00 USD | `-45.09%` | `111.84` |
| `Live` | `Long` | `1245.00` | 734,020,000.00 USD | 0.00 USD | 56,730.00 USD | `-44.64%` | `45.57` |
| `Live` | `Long` | `1255.00` | 733,970,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-44.20%` | `1,002.44` |
| `Live` | `Long` | `1265.00` | 732,710,000.00 USD | 0.00 USD | 289,300.00 USD | `-43.75%` | `228.69` |
| `Live` | `Long` | `1275.00` | 732,420,000.00 USD | 0.00 USD | 15,490,000.00 USD | `-43.31%` | `12,145.72` |
| `Live` | `Long` | `1285.00` | 716,930,000.00 USD | 0.00 USD | 474,130.00 USD | `-42.86%` | `368.98` |
| `Live` | `Long` | `1295.00` | 716,460,000.00 USD | 0.00 USD | 339,640.00 USD | `-42.42%` | `262.27` |
| `Live` | `Long` | `1305.00` | 716,120,000.00 USD | 0.00 USD | 114,060.00 USD | `-41.97%` | `87.41` |
| `Live` | `Long` | `1315.00` | 716,010,000.00 USD | 0.00 USD | 186,060.00 USD | `-41.53%` | `141.49` |
| `Live` | `Long` | `1325.00` | 715,820,000.00 USD | 0.00 USD | 492,940.00 USD | `-41.08%` | `372.03` |
| `Live` | `Long` | `1335.00` | 715,330,000.00 USD | 0.00 USD | 5,500,000.00 USD | `-40.64%` | `4,118.27` |
| `Live` | `Long` | `1345.00` | 709,830,000.00 USD | 0.00 USD | 188,030.00 USD | `-40.20%` | `139.80` |
| `Live` | `Long` | `1355.00` | 709,640,000.00 USD | 0.00 USD | 106,050.00 USD | `-39.75%` | `78.27` |
| `Live` | `Long` | `1365.00` | 709,530,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-39.31%` | `921.62` |
| `Live` | `Long` | `1375.00` | 708,280,000.00 USD | 0.00 USD | 8,980,000.00 USD | `-38.86%` | `6,531.06` |
| `Live` | `Long` | `1385.00` | 699,300,000.00 USD | 0.00 USD | 485,050.00 USD | `-38.42%` | `350.21` |
| `Live` | `Long` | `1395.00` | 698,810,000.00 USD | 0.00 USD | 913,010.00 USD | `-37.97%` | `654.49` |
| `Live` | `Long` | `1405.00` | 697,900,000.00 USD | 0.00 USD | 22,730,000.00 USD | `-37.53%` | `16,181.47` |
| `Live` | `Long` | `1415.00` | 675,160,000.00 USD | 0.00 USD | 229,690.00 USD | `-37.08%` | `162.32` |
| `Live` | `Long` | `1425.00` | 674,930,000.00 USD | 0.00 USD | 561,450.00 USD | `-36.64%` | `394.00` |
| `Live` | `Long` | `1435.00` | 674,370,000.00 USD | 0.00 USD | 782,000.00 USD | `-36.19%` | `544.95` |
| `Live` | `Long` | `1445.00` | 673,590,000.00 USD | 0.00 USD | 1,730,000.00 USD | `-35.75%` | `1,195.74` |
| `Live` | `Long` | `1455.00` | 671,860,000.00 USD | 0.00 USD | 661,960.00 USD | `-35.30%` | `454.95` |
| `Live` | `Long` | `1465.00` | 671,200,000.00 USD | 0.00 USD | 8,450,000.00 USD | `-34.86%` | `5,767.16` |
| `Live` | `Long` | `1475.00` | 662,750,000.00 USD | 0.00 USD | 5,730,000.00 USD | `-34.42%` | `3,887.69` |
| `Live` | `Long` | `1485.00` | 657,020,000.00 USD | 0.00 USD | 318,770.00 USD | `-33.97%` | `214.66` |
| `Live` | `Long` | `1495.00` | 656,700,000.00 USD | 0.00 USD | 19,400,000.00 USD | `-33.53%` | `12,976.71` |
| `Live` | `Long` | `1505.00` | 637,300,000.00 USD | 0.00 USD | 498,390.00 USD | `-33.08%` | `331.16` |
| `Live` | `Long` | `1515.00` | 636,800,000.00 USD | 0.00 USD | 18,790,000.00 USD | `-32.64%` | `12,405.12` |
| `Live` | `Long` | `1525.00` | 618,010,000.00 USD | 0.00 USD | 2,460,000.00 USD | `-32.19%` | `1,615.56` |
| `Live` | `Long` | `1535.00` | 615,540,000.00 USD | 0.00 USD | 902,770.00 USD | `-31.75%` | `588.12` |
| `Live` | `Long` | `1545.00` | 614,640,000.00 USD | 0.00 USD | 4,110,000.00 USD | `-31.30%` | `2,657.58` |
| `Live` | `Long` | `1555.00` | 610,530,000.00 USD | 0.00 USD | 16,090,000.00 USD | `-30.86%` | `10,347.34` |
| `Live` | `Long` | `1565.00` | 594,440,000.00 USD | 0.00 USD | 576,720.00 USD | `-30.41%` | `368.51` |
| `Live` | `Long` | `1575.00` | 593,870,000.00 USD | 0.00 USD | 949,290.00 USD | `-29.97%` | `602.72` |
| `Live` | `Long` | `1585.00` | 592,920,000.00 USD | 0.00 USD | 667,450.00 USD | `-29.52%` | `421.11` |
| `Live` | `Long` | `1595.00` | 592,250,000.00 USD | 0.00 USD | 2,010,000.00 USD | `-29.08%` | `1,263.08` |
| `Live` | `Long` | `1605.00` | 590,240,000.00 USD | 0.00 USD | 18,080,000.00 USD | `-28.63%` | `11,265.82` |
| `Live` | `Long` | `1615.00` | 572,150,000.00 USD | 0.00 USD | 1,080,000.00 USD | `-28.19%` | `669.83` |
| `Live` | `Long` | `1625.00` | 571,070,000.00 USD | 0.00 USD | 1,720,000.00 USD | `-27.75%` | `1,058.91` |
| `Live` | `Long` | `1635.00` | 569,350,000.00 USD | 0.00 USD | 18,670,000.00 USD | `-27.30%` | `11,419.54` |
| `Live` | `Long` | `1645.00` | 550,680,000.00 USD | 0.00 USD | 37,490,000.00 USD | `-26.86%` | `22,788.26` |
| `Live` | `Long` | `1655.00` | 513,190,000.00 USD | 0.00 USD | 859,690.00 USD | `-26.41%` | `519.45` |
| `Live` | `Long` | `1665.00` | 512,330,000.00 USD | 0.00 USD | 11,660,000.00 USD | `-25.97%` | `7,003.36` |
| `Live` | `Long` | `1675.00` | 500,670,000.00 USD | 0.00 USD | 1,030,000.00 USD | `-25.52%` | `612.33` |
| `Live` | `Long` | `1685.00` | 499,650,000.00 USD | 0.00 USD | 573,580.00 USD | `-25.08%` | `340.40` |
| `Live` | `Long` | `1695.00` | 499,070,000.00 USD | 0.00 USD | 756,150.00 USD | `-24.63%` | `446.11` |
| `Live` | `Long` | `1705.00` | 498,320,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-24.19%` | `597.96` |
| `Live` | `Long` | `1715.00` | 497,300,000.00 USD | 0.00 USD | 511,390.00 USD | `-23.74%` | `298.19` |
| `Live` | `Long` | `1725.00` | 496,790,000.00 USD | 0.00 USD | 36,690,000.00 USD | `-23.30%` | `21,269.24` |
| `Live` | `Long` | `1735.00` | 460,100,000.00 USD | 0.00 USD | 1,580,000.00 USD | `-22.85%` | `911.34` |
| `Live` | `Long` | `1745.00` | 458,520,000.00 USD | 0.00 USD | 837,560.00 USD | `-22.41%` | `479.97` |
| `Live` | `Long` | `1755.00` | 457,680,000.00 USD | 0.00 USD | 480,300.00 USD | `-21.97%` | `273.67` |
| `Live` | `Long` | `1765.00` | 457,200,000.00 USD | 0.00 USD | 7,660,000.00 USD | `-21.52%` | `4,339.39` |
| `Live` | `Long` | `1775.00` | 449,540,000.00 USD | 0.00 USD | 24,770,000.00 USD | `-21.08%` | `13,955.49` |
| `Live` | `Long` | `1785.00` | 424,770,000.00 USD | 0.00 USD | 86,890,000.00 USD | `-20.63%` | `48,679.38` |
| `Live` | `Long` | `1795.00` | 337,880,000.00 USD | 0.00 USD | 482,950.00 USD | `-20.19%` | `269.05` |
| `Live` | `Long` | `1805.00` | 337,390,000.00 USD | 0.00 USD | 3,030,000.00 USD | `-19.74%` | `1,676.85` |
| `Live` | `Long` | `1815.00` | 334,370,000.00 USD | 0.00 USD | 507,190.00 USD | `-19.30%` | `279.44` |
| `Live` | `Long` | `1825.00` | 333,860,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-18.85%` | `724.95` |
| `Live` | `Long` | `1835.00` | 332,540,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-18.41%` | `579.27` |
| `Live` | `Long` | `1845.00` | 331,470,000.00 USD | 0.00 USD | 16,200,000.00 USD | `-17.96%` | `8,780.67` |
| `Live` | `Long` | `1855.00` | 315,270,000.00 USD | 0.00 USD | 1,050,000.00 USD | `-17.52%` | `567.03` |
| `Live` | `Long` | `1865.00` | 314,220,000.00 USD | 0.00 USD | 15,820,000.00 USD | `-17.07%` | `8,484.98` |
| `Live` | `Long` | `1875.00` | 298,400,000.00 USD | 0.00 USD | 7,240,000.00 USD | `-16.63%` | `3,862.29` |
| `Live` | `Long` | `1885.00` | 291,150,000.00 USD | 0.00 USD | 5,540,000.00 USD | `-16.18%` | `2,938.71` |
| `Live` | `Long` | `1895.00` | 285,620,000.00 USD | 0.00 USD | 538,030.00 USD | `-15.74%` | `283.92` |
| `Live` | `Long` | `1905.00` | 285,080,000.00 USD | 0.00 USD | 1,420,000.00 USD | `-15.30%` | `743.27` |
| `Live` | `Long` | `1915.00` | 283,660,000.00 USD | 0.00 USD | 18,440,000.00 USD | `-14.85%` | `9,629.63` |
| `Live` | `Long` | `1925.00` | 265,220,000.00 USD | 0.00 USD | 17,280,000.00 USD | `-14.41%` | `8,976.41` |
| `Live` | `Long` | `1935.00` | 247,940,000.00 USD | 0.00 USD | 876,330.00 USD | `-13.96%` | `452.88` |
| `Live` | `Long` | `1945.00` | 247,060,000.00 USD | 0.00 USD | 5,430,000.00 USD | `-13.52%` | `2,792.78` |
| `Live` | `Long` | `1955.00` | 241,630,000.00 USD | 0.00 USD | 13,680,000.00 USD | `-13.07%` | `6,998.40` |
| `Live` | `Long` | `1965.00` | 227,950,000.00 USD | 0.00 USD | 2,720,000.00 USD | `-12.63%` | `1,385.08` |
| `Live` | `Long` | `1975.00` | 225,230,000.00 USD | 0.00 USD | 3,020,000.00 USD | `-12.18%` | `1,528.88` |
| `Live` | `Long` | `1985.00` | 222,210,000.00 USD | 0.00 USD | 5,560,000.00 USD | `-11.74%` | `2,799.84` |
| `Live` | `Long` | `1995.00` | 216,650,000.00 USD | 0.00 USD | 645,300.00 USD | `-11.29%` | `323.46` |
| `Live` | `Long` | `2005.00` | 216,010,000.00 USD | 0.00 USD | 13,400,000.00 USD | `-10.85%` | `6,680.97` |
| `Live` | `Long` | `2015.00` | 202,610,000.00 USD | 0.00 USD | 2,050,000.00 USD | `-10.40%` | `1,016.65` |
| `Live` | `Long` | `2025.00` | 200,560,000.00 USD | 0.00 USD | 1,010,000.00 USD | `-9.96%` | `499.16` |
| `Live` | `Long` | `2035.00` | 199,550,000.00 USD | 0.00 USD | 598,780.00 USD | `-9.52%` | `294.24` |
| `Live` | `Long` | `2045.00` | 198,950,000.00 USD | 0.00 USD | 6,820,000.00 USD | `-9.07%` | `3,337.16` |
| `Live` | `Long` | `2055.00` | 192,130,000.00 USD | 0.00 USD | 3,880,000.00 USD | `-8.63%` | `1,890.30` |
| `Live` | `Long` | `2065.00` | 188,240,000.00 USD | 0.00 USD | 14,120,000.00 USD | `-8.18%` | `6,836.44` |
| `Live` | `Long` | `2075.00` | 174,130,000.00 USD | 0.00 USD | 3,520,000.00 USD | `-7.74%` | `1,695.99` |
| `Live` | `Long` | `2085.00` | 170,610,000.00 USD | 0.00 USD | 13,940,000.00 USD | `-7.29%` | `6,685.99` |
| `Live` | `Long` | `2095.00` | 156,670,000.00 USD | 0.00 USD | 1,740,000.00 USD | `-6.85%` | `830.54` |
| `Live` | `Long` | `2105.00` | 154,930,000.00 USD | 0.00 USD | 2,400,000.00 USD | `-6.40%` | `1,140.76` |
| `Live` | `Long` | `2115.00` | 152,530,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-5.96%` | `527.87` |
| `Live` | `Long` | `2125.00` | 151,410,000.00 USD | 0.00 USD | 123,840,000.00 USD | `-5.51%` | `58,278.99` |
| `Live` | `Long` | `2135.00` | 27,570,000.00 USD | 0.00 USD | 1,620,000.00 USD | `-5.07%` | `757.55` |
| `Live` | `Long` | `2145.00` | 25,950,000.00 USD | 0.00 USD | 1,990,000.00 USD | `-4.62%` | `926.54` |
| `Live` | `Long` | `2155.00` | 23,960,000.00 USD | 0.00 USD | 2,440,000.00 USD | `-4.18%` | `1,132.31` |
| `Live` | `Long` | `2165.00` | 21,520,000.00 USD | 0.00 USD | 9,880,000.00 USD | `-3.73%` | `4,561.89` |
| `Live` | `Long` | `2175.00` | 11,650,000.00 USD | 0.00 USD | 6,190,000.00 USD | `-3.29%` | `2,844.22` |
| `Live` | `Long` | `2185.00` | 5,460,000.00 USD | 0.00 USD | 2,700,000.00 USD | `-2.85%` | `1,236.31` |
| `Live` | `Long` | `2195.00` | 2,760,000.00 USD | 0.00 USD | 2,300,000.00 USD | `-2.40%` | `1,046.52` |
| `Live` | `Long` | `2205.00` | 460,520.00 USD | 0.00 USD | 432,930.00 USD | `-1.96%` | `196.34` |
| `Live` | `Long` | `2215.00` | 27,590.00 USD | 0.00 USD | 27,590.00 USD | `-1.51%` | `12.46` |
| `Live` | `Short` | `2255.00` | 20,070.00 USD | 20,070.00 USD | 0.00 USD | `+0.27%` | `8.90` |
| `Live` | `Short` | `2265.00` | 54,440.00 USD | 34,370.00 USD | 0.00 USD | `+0.71%` | `15.17` |
| `Live` | `Short` | `2275.00` | 846,210.00 USD | 791,770.00 USD | 0.00 USD | `+1.16%` | `348.03` |
| `Live` | `Short` | `2285.00` | 1,080,000.00 USD | 235,710.00 USD | 0.00 USD | `+1.60%` | `103.15` |
| `Live` | `Short` | `2295.00` | 4,580,000.00 USD | 3,490,000.00 USD | 0.00 USD | `+2.05%` | `1,522.56` |
| `Live` | `Short` | `2305.00` | 4,890,000.00 USD | 310,530.00 USD | 0.00 USD | `+2.49%` | `134.72` |
| `Live` | `Short` | `2315.00` | 5,910,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+2.93%` | `442.89` |
| `Live` | `Short` | `2325.00` | 9,490,000.00 USD | 3,580,000.00 USD | 0.00 USD | `+3.38%` | `1,539.99` |
| `Live` | `Short` | `2335.00` | 9,570,000.00 USD | 79,270.00 USD | 0.00 USD | `+3.82%` | `33.95` |
| `Live` | `Short` | `2345.00` | 10,120,000.00 USD | 550,680.00 USD | 0.00 USD | `+4.27%` | `234.83` |
| `Live` | `Short` | `2355.00` | 11,400,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+4.71%` | `541.83` |
| `Live` | `Short` | `2365.00` | 15,370,000.00 USD | 3,970,000.00 USD | 0.00 USD | `+5.16%` | `1,680.06` |
| `Live` | `Short` | `2375.00` | 17,130,000.00 USD | 1,760,000.00 USD | 0.00 USD | `+5.60%` | `741.88` |
| `Live` | `Short` | `2385.00` | 19,020,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+6.05%` | `792.28` |
| `Live` | `Short` | `2395.00` | 23,900,000.00 USD | 4,870,000.00 USD | 0.00 USD | `+6.49%` | `2,035.38` |
| `Live` | `Short` | `2405.00` | 24,120,000.00 USD | 225,400.00 USD | 0.00 USD | `+6.94%` | `93.72` |
| `Live` | `Short` | `2415.00` | 24,240,000.00 USD | 116,740.00 USD | 0.00 USD | `+7.38%` | `48.34` |
| `Live` | `Short` | `2425.00` | 24,680,000.00 USD | 435,780.00 USD | 0.00 USD | `+7.83%` | `179.70` |
| `Live` | `Short` | `2435.00` | 25,210,000.00 USD | 532,800.00 USD | 0.00 USD | `+8.27%` | `218.81` |
| `Live` | `Short` | `2445.00` | 26,840,000.00 USD | 1,630,000.00 USD | 0.00 USD | `+8.71%` | `665.94` |
| `Live` | `Short` | `2455.00` | 27,030,000.00 USD | 194,210.00 USD | 0.00 USD | `+9.16%` | `79.11` |
| `Live` | `Short` | `2465.00` | 43,280,000.00 USD | 16,250,000.00 USD | 0.00 USD | `+9.60%` | `6,593.36` |
| `Live` | `Short` | `2475.00` | 98,150,000.00 USD | 54,870,000.00 USD | 0.00 USD | `+10.05%` | `22,170.01` |
| `Live` | `Short` | `2485.00` | 98,200,000.00 USD | 41,090.00 USD | 0.00 USD | `+10.49%` | `16.53` |
| `Live` | `Short` | `2495.00` | 99,940,000.00 USD | 1,740,000.00 USD | 0.00 USD | `+10.94%` | `699.14` |
| `Live` | `Short` | `2505.00` | 104,840,000.00 USD | 4,900,000.00 USD | 0.00 USD | `+11.38%` | `1,957.96` |
| `Live` | `Short` | `2515.00` | 104,910,000.00 USD | 60,730.00 USD | 0.00 USD | `+11.83%` | `24.15` |
| `Live` | `Short` | `2525.00` | 104,990,000.00 USD | 79,800.00 USD | 0.00 USD | `+12.27%` | `31.60` |
| `Live` | `Short` | `2535.00` | 106,050,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+12.72%` | `418.95` |
| `Live` | `Short` | `2545.00` | 111,130,000.00 USD | 5,080,000.00 USD | 0.00 USD | `+13.16%` | `1,996.90` |
| `Live` | `Short` | `2555.00` | 111,390,000.00 USD | 262,820.00 USD | 0.00 USD | `+13.61%` | `102.87` |
| `Live` | `Short` | `2565.00` | 111,430,000.00 USD | 38,980.00 USD | 0.00 USD | `+14.05%` | `15.20` |
| `Live` | `Short` | `2575.00` | 111,480,000.00 USD | 45,990.00 USD | 0.00 USD | `+14.50%` | `17.86` |
| `Live` | `Short` | `2585.00` | 138,170,000.00 USD | 26,690,000.00 USD | 0.00 USD | `+14.94%` | `10,325.23` |
| `Live` | `Short` | `2595.00` | 146,160,000.00 USD | 8,000,000.00 USD | 0.00 USD | `+15.38%` | `3,081.17` |
| `Live` | `Short` | `2605.00` | 151,980,000.00 USD | 5,810,000.00 USD | 0.00 USD | `+15.83%` | `2,231.80` |
| `Live` | `Short` | `2615.00` | 164,750,000.00 USD | 12,770,000.00 USD | 0.00 USD | `+16.27%` | `4,884.95` |
| `Live` | `Short` | `2625.00` | 171,390,000.00 USD | 6,640,000.00 USD | 0.00 USD | `+16.72%` | `2,529.33` |
| `Live` | `Short` | `2635.00` | 172,870,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+17.16%` | `561.57` |
| `Live` | `Short` | `2645.00` | 173,730,000.00 USD | 860,740.00 USD | 0.00 USD | `+17.61%` | `325.42` |
| `Live` | `Short` | `2655.00` | 174,130,000.00 USD | 398,020.00 USD | 0.00 USD | `+18.05%` | `149.91` |
| `Live` | `Short` | `2665.00` | 174,590,000.00 USD | 462,390.00 USD | 0.00 USD | `+18.50%` | `173.51` |
| `Live` | `Short` | `2675.00` | 176,180,000.00 USD | 1,590,000.00 USD | 0.00 USD | `+18.94%` | `594.35` |
| `Live` | `Short` | `2685.00` | 176,200,000.00 USD | 17,400.00 USD | 0.00 USD | `+19.39%` | `6.48` |
| `Live` | `Short` | `2695.00` | 176,470,000.00 USD | 275,120.00 USD | 0.00 USD | `+19.83%` | `102.09` |
| `Live` | `Short` | `2705.00` | 177,740,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+20.28%` | `468.81` |
| `Live` | `Short` | `2715.00` | 178,280,000.00 USD | 533,790.00 USD | 0.00 USD | `+20.72%` | `196.61` |
| `Live` | `Short` | `2725.00` | 178,690,000.00 USD | 409,700.00 USD | 0.00 USD | `+21.16%` | `150.35` |
| `Live` | `Short` | `2735.00` | 179,120,000.00 USD | 435,040.00 USD | 0.00 USD | `+21.61%` | `159.06` |
| `Live` | `Short` | `2745.00` | 192,920,000.00 USD | 13,800,000.00 USD | 0.00 USD | `+22.05%` | `5,028.25` |
| `Live` | `Short` | `2755.00` | 228,240,000.00 USD | 35,320,000.00 USD | 0.00 USD | `+22.50%` | `12,818.65` |
| `Live` | `Short` | `2765.00` | 228,620,000.00 USD | 376,890.00 USD | 0.00 USD | `+22.94%` | `136.31` |
| `Live` | `Short` | `2775.00` | 229,020,000.00 USD | 405,060.00 USD | 0.00 USD | `+23.39%` | `145.97` |
| `Live` | `Short` | `2785.00` | 234,590,000.00 USD | 5,570,000.00 USD | 0.00 USD | `+23.83%` | `1,999.72` |
| `Live` | `Short` | `2795.00` | 234,610,000.00 USD | 22,260.00 USD | 0.00 USD | `+24.28%` | `7.96` |
| `Live` | `Short` | `2805.00` | 239,890,000.00 USD | 5,280,000.00 USD | 0.00 USD | `+24.72%` | `1,881.35` |
| `Live` | `Short` | `2815.00` | 241,780,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+25.17%` | `671.39` |
| `Live` | `Short` | `2825.00` | 241,890,000.00 USD | 106,590.00 USD | 0.00 USD | `+25.61%` | `37.73` |
| `Live` | `Short` | `2835.00` | 248,170,000.00 USD | 6,290,000.00 USD | 0.00 USD | `+26.06%` | `2,217.87` |
| `Live` | `Short` | `2845.00` | 248,290,000.00 USD | 121,050.00 USD | 0.00 USD | `+26.50%` | `42.55` |
| `Live` | `Short` | `2855.00` | 249,390,000.00 USD | 1,090,000.00 USD | 0.00 USD | `+26.95%` | `382.61` |
| `Live` | `Short` | `2865.00` | 249,440,000.00 USD | 50,400.00 USD | 0.00 USD | `+27.39%` | `17.59` |
| `Live` | `Short` | `2875.00` | 292,990,000.00 USD | 43,550,000.00 USD | 0.00 USD | `+27.83%` | `15,148.69` |
| `Live` | `Short` | `2885.00` | 295,070,000.00 USD | 2,080,000.00 USD | 0.00 USD | `+28.28%` | `720.01` |
| `Live` | `Short` | `2895.00` | 295,600,000.00 USD | 533,420.00 USD | 0.00 USD | `+28.72%` | `184.26` |
| `Live` | `Short` | `2905.00` | 296,800,000.00 USD | 1,200,000.00 USD | 0.00 USD | `+29.17%` | `412.89` |
| `Live` | `Short` | `2915.00` | 299,550,000.00 USD | 2,750,000.00 USD | 0.00 USD | `+29.61%` | `943.09` |
| `Live` | `Short` | `2925.00` | 299,570,000.00 USD | 24,140.00 USD | 0.00 USD | `+30.06%` | `8.25` |
| `Live` | `Short` | `2935.00` | 299,760,000.00 USD | 182,240.00 USD | 0.00 USD | `+30.50%` | `62.09` |
| `Live` | `Short` | `2945.00` | 300,170,000.00 USD | 412,780.00 USD | 0.00 USD | `+30.95%` | `140.16` |
| `Live` | `Short` | `2955.00` | 300,450,000.00 USD | 280,690.00 USD | 0.00 USD | `+31.39%` | `94.99` |
| `Live` | `Short` | `2965.00` | 304,340,000.00 USD | 3,890,000.00 USD | 0.00 USD | `+31.84%` | `1,312.86` |
| `Live` | `Short` | `2975.00` | 304,360,000.00 USD | 18,050.00 USD | 0.00 USD | `+32.28%` | `6.07` |
| `Live` | `Short` | `2985.00` | 306,730,000.00 USD | 2,370,000.00 USD | 0.00 USD | `+32.73%` | `792.44` |
| `Live` | `Short` | `2995.00` | 321,710,000.00 USD | 14,980,000.00 USD | 0.00 USD | `+33.17%` | `5,002.66` |
| `Live` | `Short` | `3005.00` | 322,270,000.00 USD | 559,150.00 USD | 0.00 USD | `+33.61%` | `186.07` |
| `Live` | `Short` | `3015.00` | 322,430,000.00 USD | 163,470.00 USD | 0.00 USD | `+34.06%` | `54.22` |
| `Live` | `Short` | `3025.00` | 324,530,000.00 USD | 2,090,000.00 USD | 0.00 USD | `+34.50%` | `692.34` |
| `Live` | `Short` | `3035.00` | 337,340,000.00 USD | 12,810,000.00 USD | 0.00 USD | `+34.95%` | `4,222.29` |
| `Live` | `Short` | `3045.00` | 338,290,000.00 USD | 947,940.00 USD | 0.00 USD | `+35.39%` | `311.31` |
| `Live` | `Short` | `3055.00` | 340,470,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+35.84%` | `713.85` |
| `Live` | `Short` | `3065.00` | 341,980,000.00 USD | 1,510,000.00 USD | 0.00 USD | `+36.28%` | `493.82` |
| `Live` | `Short` | `3075.00` | 353,200,000.00 USD | 11,210,000.00 USD | 0.00 USD | `+36.73%` | `3,646.97` |
| `Live` | `Short` | `3085.00` | 361,070,000.00 USD | 7,870,000.00 USD | 0.00 USD | `+37.17%` | `2,550.82` |
| `Live` | `Short` | `3095.00` | 367,960,000.00 USD | 6,890,000.00 USD | 0.00 USD | `+37.62%` | `2,227.56` |
| `Live` | `Short` | `3105.00` | 380,100,000.00 USD | 12,140,000.00 USD | 0.00 USD | `+38.06%` | `3,908.62` |
| `Live` | `Short` | `3115.00` | 381,850,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+38.51%` | `561.85` |
| `Live` | `Short` | `3125.00` | 381,960,000.00 USD | 116,140.00 USD | 0.00 USD | `+38.95%` | `37.16` |
| `Live` | `Short` | `3135.00` | 382,560,000.00 USD | 600,340.00 USD | 0.00 USD | `+39.40%` | `191.49` |
| `Live` | `Short` | `3145.00` | 382,600,000.00 USD | 35,850.00 USD | 0.00 USD | `+39.84%` | `11.40` |
| `Live` | `Short` | `3155.00` | 385,850,000.00 USD | 3,250,000.00 USD | 0.00 USD | `+40.28%` | `1,030.96` |
| `Live` | `Short` | `3165.00` | 415,380,000.00 USD | 29,530,000.00 USD | 0.00 USD | `+40.73%` | `9,329.08` |
| `Live` | `Short` | `3175.00` | 424,380,000.00 USD | 9,000,000.00 USD | 0.00 USD | `+41.17%` | `2,835.46` |
| `Live` | `Short` | `3185.00` | 495,090,000.00 USD | 70,710,000.00 USD | 0.00 USD | `+41.62%` | `22,199.66` |
| `Live` | `Short` | `3195.00` | 495,320,000.00 USD | 230,850.00 USD | 0.00 USD | `+42.06%` | `72.25` |
| `Live` | `Short` | `3205.00` | 495,420,000.00 USD | 106,300.00 USD | 0.00 USD | `+42.51%` | `33.17` |
| `Live` | `Short` | `3215.00` | 495,760,000.00 USD | 335,380.00 USD | 0.00 USD | `+42.95%` | `104.32` |
| `Live` | `Short` | `3225.00` | 495,800,000.00 USD | 35,870.00 USD | 0.00 USD | `+43.40%` | `11.12` |
| `Live` | `Short` | `3235.00` | 513,800,000.00 USD | 18,000,000.00 USD | 0.00 USD | `+43.84%` | `5,564.83` |
| `Live` | `Short` | `3245.00` | 513,980,000.00 USD | 182,250.00 USD | 0.00 USD | `+44.29%` | `56.16` |
| `Live` | `Short` | `3255.00` | 515,510,000.00 USD | 1,530,000.00 USD | 0.00 USD | `+44.73%` | `469.41` |
| `Live` | `Short` | `3265.00` | 520,280,000.00 USD | 4,780,000.00 USD | 0.00 USD | `+45.18%` | `1,463.10` |
| `Live` | `Short` | `3275.00` | 528,740,000.00 USD | 8,450,000.00 USD | 0.00 USD | `+45.62%` | `2,580.89` |
| `Live` | `Short` | `3285.00` | 528,860,000.00 USD | 118,750.00 USD | 0.00 USD | `+46.06%` | `36.15` |
| `Live` | `Short` | `3295.00` | 530,940,000.00 USD | 2,080,000.00 USD | 0.00 USD | `+46.51%` | `632.07` |
| `Live` | `Short` | `3305.00` | 533,790,000.00 USD | 2,850,000.00 USD | 0.00 USD | `+46.95%` | `861.87` |
| `Live` | `Short` | `3315.00` | 540,060,000.00 USD | 6,270,000.00 USD | 0.00 USD | `+47.40%` | `1,890.92` |
| `Live` | `Short` | `3325.00` | 540,320,000.00 USD | 260,460.00 USD | 0.00 USD | `+47.84%` | `78.33` |
| `Live` | `Short` | `3335.00` | 569,450,000.00 USD | 29,130,000.00 USD | 0.00 USD | `+48.29%` | `8,735.57` |
| `Live` | `Short` | `3345.00` | 569,820,000.00 USD | 372,490.00 USD | 0.00 USD | `+48.73%` | `111.36` |
| `Live` | `Short` | `3355.00` | 572,330,000.00 USD | 2,510,000.00 USD | 0.00 USD | `+49.18%` | `748.01` |
| `Live` | `Short` | `3365.00` | 576,670,000.00 USD | 4,340,000.00 USD | 0.00 USD | `+49.62%` | `1,290.43` |
| `Live` | `Short` | `3375.00` | 576,680,000.00 USD | 3,250.00 USD | 0.00 USD | `+50.07%` | `0.96` |
| `Live` | `Short` | `3385.00` | 576,780,000.00 USD | 102,400.00 USD | 0.00 USD | `+50.51%` | `30.25` |
| `Live` | `Short` | `3395.00` | 577,910,000.00 USD | 1,130,000.00 USD | 0.00 USD | `+50.96%` | `332.09` |
| `Live` | `Short` | `3405.00` | 578,310,000.00 USD | 402,390.00 USD | 0.00 USD | `+51.40%` | `118.18` |
| `Live` | `Short` | `3415.00` | 580,150,000.00 USD | 1,850,000.00 USD | 0.00 USD | `+51.85%` | `540.56` |
| `Live` | `Short` | `3425.00` | 595,240,000.00 USD | 15,090,000.00 USD | 0.00 USD | `+52.29%` | `4,405.35` |
| `Live` | `Short` | `3435.00` | 595,980,000.00 USD | 739,940.00 USD | 0.00 USD | `+52.73%` | `215.41` |
| `Live` | `Short` | `3445.00` | 598,720,000.00 USD | 2,740,000.00 USD | 0.00 USD | `+53.18%` | `794.99` |
| `Live` | `Short` | `3455.00` | 599,200,000.00 USD | 473,740.00 USD | 0.00 USD | `+53.62%` | `137.12` |
| `Live` | `Short` | `3465.00` | 599,260,000.00 USD | 65,160.00 USD | 0.00 USD | `+54.07%` | `18.80` |
| `Live` | `Short` | `3475.00` | 599,320,000.00 USD | 57,870.00 USD | 0.00 USD | `+54.51%` | `16.65` |
| `Live` | `Short` | `3485.00` | 613,520,000.00 USD | 14,200,000.00 USD | 0.00 USD | `+54.96%` | `4,074.89` |
| `Live` | `Short` | `3495.00` | 614,820,000.00 USD | 1,300,000.00 USD | 0.00 USD | `+55.40%` | `372.11` |
| `Live` | `Short` | `3505.00` | 616,210,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+55.85%` | `396.32` |
| `Live` | `Short` | `3515.00` | 616,900,000.00 USD | 691,460.00 USD | 0.00 USD | `+56.29%` | `196.72` |
| `Live` | `Short` | `3525.00` | 617,070,000.00 USD | 167,320.00 USD | 0.00 USD | `+56.74%` | `47.47` |
| `Live` | `Short` | `3535.00` | 617,310,000.00 USD | 244,270.00 USD | 0.00 USD | `+57.18%` | `69.10` |
| `Live` | `Short` | `3545.00` | 617,340,000.00 USD | 30,420.00 USD | 0.00 USD | `+57.63%` | `8.58` |
| `Live` | `Short` | `3555.00` | 617,520,000.00 USD | 178,820.00 USD | 0.00 USD | `+58.07%` | `50.30` |
| `Live` | `Short` | `3565.00` | 617,580,000.00 USD | 55,400.00 USD | 0.00 USD | `+58.51%` | `15.54` |
| `Live` | `Short` | `3575.00` | 617,660,000.00 USD | 80,150.00 USD | 0.00 USD | `+58.96%` | `22.42` |
| `Live` | `Short` | `3585.00` | 620,500,000.00 USD | 2,840,000.00 USD | 0.00 USD | `+59.40%` | `793.14` |
| `Live` | `Short` | `3595.00` | 620,620,000.00 USD | 118,080.00 USD | 0.00 USD | `+59.85%` | `32.85` |
| `Live` | `Short` | `3605.00` | 620,620,000.00 USD | 1,010.00 USD | 0.00 USD | `+60.29%` | `0.28` |
| `Live` | `Short` | `3615.00` | 624,410,000.00 USD | 3,790,000.00 USD | 0.00 USD | `+60.74%` | `1,047.40` |
| `Live` | `Short` | `3625.00` | 634,100,000.00 USD | 9,700,000.00 USD | 0.00 USD | `+61.18%` | `2,674.72` |
| `Live` | `Short` | `3635.00` | 634,180,000.00 USD | 73,410.00 USD | 0.00 USD | `+61.63%` | `20.20` |
| `Live` | `Short` | `3645.00` | 640,740,000.00 USD | 6,560,000.00 USD | 0.00 USD | `+62.07%` | `1,800.61` |
| `Live` | `Short` | `3655.00` | 694,840,000.00 USD | 54,100,000.00 USD | 0.00 USD | `+62.52%` | `14,800.93` |
| `Live` | `Short` | `3665.00` | 694,850,000.00 USD | 12,160.00 USD | 0.00 USD | `+62.96%` | `3.32` |
| `Live` | `Short` | `3675.00` | 695,200,000.00 USD | 347,420.00 USD | 0.00 USD | `+63.41%` | `94.54` |
| `Live` | `Short` | `3685.00` | 695,420,000.00 USD | 222,990.00 USD | 0.00 USD | `+63.85%` | `60.51` |
| `Live` | `Short` | `3695.00` | 1,080,000,000.00 USD | 383,100,000.00 USD | 0.00 USD | `+64.30%` | `103,681.40` |
| `Live` | `Short` | `3705.00` | 1,080,000,000.00 USD | 102,260.00 USD | 0.00 USD | `+64.74%` | `27.60` |
| `Live` | `Short` | `3715.00` | 1,080,000,000.00 USD | 2,100.00 USD | 0.00 USD | `+65.18%` | `0.57` |
| `Live` | `Short` | `3725.00` | 1,080,000,000.00 USD | 234,460.00 USD | 0.00 USD | `+65.63%` | `62.94` |
| `Live` | `Short` | `3735.00` | 1,080,000,000.00 USD | 3,780,000.00 USD | 0.00 USD | `+66.07%` | `1,011.11` |
| `Live` | `Short` | `3745.00` | 1,090,000,000.00 USD | 7,650,000.00 USD | 0.00 USD | `+66.52%` | `2,042.32` |
| `Live` | `Short` | `3755.00` | 1,090,000,000.00 USD | 80,890.00 USD | 0.00 USD | `+66.96%` | `21.54` |
| `Live` | `Short` | `3765.00` | 1,090,000,000.00 USD | 2,640,000.00 USD | 0.00 USD | `+67.41%` | `701.06` |
| `Live` | `Short` | `3775.00` | 1,150,000,000.00 USD | 57,020,000.00 USD | 0.00 USD | `+67.85%` | `15,105.86` |
| `Live` | `Short` | `3785.00` | 1,150,000,000.00 USD | 3,170,000.00 USD | 0.00 USD | `+68.30%` | `837.62` |
| `Live` | `Short` | `3795.00` | 1,150,000,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+68.74%` | `328.72` |
| `Live` | `Short` | `3805.00` | 1,150,000,000.00 USD | 8,090.00 USD | 0.00 USD | `+69.19%` | `2.13` |
| `Live` | `Short` | `3815.00` | 1,150,000,000.00 USD | 27,530.00 USD | 0.00 USD | `+69.63%` | `7.22` |
| `Live` | `Short` | `3825.00` | 1,150,000,000.00 USD | 115,860.00 USD | 0.00 USD | `+70.08%` | `30.29` |
| `Live` | `Short` | `3835.00` | 1,150,000,000.00 USD | 281,470.00 USD | 0.00 USD | `+70.52%` | `73.40` |
| `Live` | `Short` | `3845.00` | 1,160,000,000.00 USD | 3,430,000.00 USD | 0.00 USD | `+70.96%` | `892.78` |
| `Live` | `Short` | `3855.00` | 1,160,000,000.00 USD | 67,010.00 USD | 0.00 USD | `+71.41%` | `17.38` |
| `Live` | `Short` | `3865.00` | 1,160,000,000.00 USD | 817,060.00 USD | 0.00 USD | `+71.85%` | `211.40` |
| `Live` | `Short` | `3885.00` | 1,200,000,000.00 USD | 39,470,000.00 USD | 0.00 USD | `+72.74%` | `10,160.83` |
| `Live` | `Short` | `3895.00` | 1,200,000,000.00 USD | 266,110.00 USD | 0.00 USD | `+73.19%` | `68.32` |
| `Live` | `Short` | `3905.00` | 1,200,000,000.00 USD | 971,390.00 USD | 0.00 USD | `+73.63%` | `248.76` |
| `Live` | `Short` | `3915.00` | 1,200,000,000.00 USD | 2,580,000.00 USD | 0.00 USD | `+74.08%` | `658.45` |
| `Live` | `Short` | `3925.00` | 1,200,000,000.00 USD | 197,460.00 USD | 0.00 USD | `+74.52%` | `50.31` |
| `Live` | `Short` | `3935.00` | 1,200,000,000.00 USD | 5,050.00 USD | 0.00 USD | `+74.97%` | `1.28` |
| `Live` | `Short` | `3945.00` | 1,200,000,000.00 USD | 24,650.00 USD | 0.00 USD | `+75.41%` | `6.25` |
| `Live` | `Short` | `3955.00` | 1,200,000,000.00 USD | 1,760.00 USD | 0.00 USD | `+75.86%` | `0.44` |
| `Live` | `Short` | `3965.00` | 1,200,000,000.00 USD | 5,480.00 USD | 0.00 USD | `+76.30%` | `1.38` |
| `Live` | `Short` | `3975.00` | 1,200,000,000.00 USD | 241,590.00 USD | 0.00 USD | `+76.75%` | `60.78` |
| `Live` | `Short` | `3985.00` | 1,200,000,000.00 USD | 600,020.00 USD | 0.00 USD | `+77.19%` | `150.57` |
| `Live` | `Short` | `3995.00` | 1,200,000,000.00 USD | 607,880.00 USD | 0.00 USD | `+77.63%` | `152.16` |
| `Live` | `Short` | `4005.00` | 1,200,000,000.00 USD | 52,680.00 USD | 0.00 USD | `+78.08%` | `13.15` |
| `Live` | `Short` | `4015.00` | 1,210,000,000.00 USD | 1,810,000.00 USD | 0.00 USD | `+78.52%` | `450.27` |
| `Live` | `Short` | `4025.00` | 1,210,000,000.00 USD | 702,730.00 USD | 0.00 USD | `+78.97%` | `174.59` |
| `Live` | `Short` | `4035.00` | 1,210,000,000.00 USD | 1,120,000.00 USD | 0.00 USD | `+79.41%` | `276.69` |
| `Live` | `Short` | `4045.00` | 1,210,000,000.00 USD | 48,020.00 USD | 0.00 USD | `+79.86%` | `11.87` |
| `Live` | `Short` | `4055.00` | 1,210,000,000.00 USD | 1,620,000.00 USD | 0.00 USD | `+80.30%` | `399.95` |
| `Live` | `Short` | `4065.00` | 1,210,000,000.00 USD | 70,150.00 USD | 0.00 USD | `+80.75%` | `17.26` |
| `Live` | `Short` | `4075.00` | 1,210,000,000.00 USD | 271,220.00 USD | 0.00 USD | `+81.19%` | `66.56` |
| `Live` | `Short` | `4085.00` | 1,210,000,000.00 USD | 451,090.00 USD | 0.00 USD | `+81.64%` | `110.43` |
| `Live` | `Short` | `4095.00` | 1,210,000,000.00 USD | 9,770.00 USD | 0.00 USD | `+82.08%` | `2.39` |
| `Live` | `Short` | `4105.00` | 1,210,000,000.00 USD | 535,670.00 USD | 0.00 USD | `+82.53%` | `130.49` |
| `Live` | `Short` | `4115.00` | 1,210,000,000.00 USD | 3,810.00 USD | 0.00 USD | `+82.97%` | `0.93` |
| `Live` | `Short` | `4125.00` | 1,210,000,000.00 USD | 64,130.00 USD | 0.00 USD | `+83.41%` | `15.55` |
| `Live` | `Short` | `4135.00` | 1,210,000,000.00 USD | 196,720.00 USD | 0.00 USD | `+83.86%` | `47.57` |
| `Live` | `Short` | `4145.00` | 1,210,000,000.00 USD | 774,090.00 USD | 0.00 USD | `+84.30%` | `186.75` |
| `Live` | `Short` | `4155.00` | 1,210,000,000.00 USD | 40,030.00 USD | 0.00 USD | `+84.75%` | `9.63` |
| `Live` | `Short` | `4165.00` | 1,210,000,000.00 USD | 123,950.00 USD | 0.00 USD | `+85.19%` | `29.76` |
| `Live` | `Short` | `4175.00` | 1,210,000,000.00 USD | 92,210.00 USD | 0.00 USD | `+85.64%` | `22.09` |
| `Live` | `Short` | `4185.00` | 1,210,000,000.00 USD | 854,050.00 USD | 0.00 USD | `+86.08%` | `204.07` |
| `Live` | `Short` | `4195.00` | 1,250,000,000.00 USD | 32,940,000.00 USD | 0.00 USD | `+86.53%` | `7,851.08` |
| `Live` | `Short` | `4205.00` | 1,250,000,000.00 USD | 82,260.00 USD | 0.00 USD | `+86.97%` | `19.56` |
| `Live` | `Short` | `4215.00` | 1,330,000,000.00 USD | 83,090,000.00 USD | 0.00 USD | `+87.42%` | `19,712.87` |
| `Live` | `Short` | `4235.00` | 1,330,000,000.00 USD | 16,670.00 USD | 0.00 USD | `+88.31%` | `3.94` |
| `Live` | `Short` | `4245.00` | 1,330,000,000.00 USD | 1,530,000.00 USD | 0.00 USD | `+88.75%` | `361.45` |
| `Live` | `Short` | `4255.00` | 1,330,000,000.00 USD | 420.39 USD | 0.00 USD | `+89.20%` | `0.10` |
| `Live` | `Short` | `4265.00` | 1,330,000,000.00 USD | 58,530.00 USD | 0.00 USD | `+89.64%` | `13.72` |
| `Live` | `Short` | `4285.00` | 1,330,000,000.00 USD | 766,900.00 USD | 0.00 USD | `+90.53%` | `178.97` |
| `Live` | `Short` | `4295.00` | 1,330,000,000.00 USD | 5,810.00 USD | 0.00 USD | `+90.97%` | `1.35` |
| `Live` | `Short` | `4305.00` | 1,330,000,000.00 USD | 5,560.00 USD | 0.00 USD | `+91.42%` | `1.29` |
| `Live` | `Short` | `4315.00` | 1,330,000,000.00 USD | 153,740.00 USD | 0.00 USD | `+91.86%` | `35.63` |
| `Live` | `Short` | `4325.00` | 1,330,000,000.00 USD | 248,420.00 USD | 0.00 USD | `+92.31%` | `57.44` |
| `Live` | `Short` | `4335.00` | 1,330,000,000.00 USD | 116,150.00 USD | 0.00 USD | `+92.75%` | `26.79` |
| `Live` | `Short` | `4345.00` | 1,330,000,000.00 USD | 152,480.00 USD | 0.00 USD | `+93.20%` | `35.09` |
| `Live` | `Short` | `4355.00` | 1,330,000,000.00 USD | 598,750.00 USD | 0.00 USD | `+93.64%` | `137.49` |
| `Live` | `Short` | `4365.00` | 1,330,000,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+94.09%` | `231.76` |
| `Live` | `Short` | `4375.00` | 1,330,000,000.00 USD | 448,590.00 USD | 0.00 USD | `+94.53%` | `102.54` |
| `Live` | `Short` | `4385.00` | 1,330,000,000.00 USD | 178,700.00 USD | 0.00 USD | `+94.98%` | `40.75` |
| `Live` | `Short` | `4395.00` | 1,330,000,000.00 USD | 81,540.00 USD | 0.00 USD | `+95.42%` | `18.55` |
| `Live` | `Short` | `4405.00` | 1,330,000,000.00 USD | 42,140.00 USD | 0.00 USD | `+95.86%` | `9.57` |
| `Live` | `Short` | `4415.00` | 1,330,000,000.00 USD | 116,160.00 USD | 0.00 USD | `+96.31%` | `26.31` |
| `Live` | `Short` | `4425.00` | 1,330,000,000.00 USD | 22,970.00 USD | 0.00 USD | `+96.75%` | `5.19` |
| `Live` | `Short` | `4455.00` | 1,340,000,000.00 USD | 390,430.00 USD | 0.00 USD | `+98.09%` | `87.64` |
| `Live` | `Short` | `4465.00` | 1,340,000,000.00 USD | 75,710.00 USD | 0.00 USD | `+98.53%` | `16.96` |
| `Live` | `Short` | `4475.00` | 1,340,000,000.00 USD | 37,040.00 USD | 0.00 USD | `+98.98%` | `8.28` |
| `Live` | `Short` | `4485.00` | 1,340,000,000.00 USD | 18,450.00 USD | 0.00 USD | `+99.42%` | `4.11` |
| `Live` | `Short` | `4495.00` | 1,340,000,000.00 USD | 138,480.00 USD | 0.00 USD | `+99.87%` | `30.81` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `485.00` | 34,130,000.00 USD | 0.00 USD | 278.83 USD | `-78.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `505.00` | 34,130,000.00 USD | 0.00 USD | 16,100.00 USD | `-77.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.00` | 34,110,000.00 USD | 0.00 USD | 300.66 USD | `-77.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 34,110,000.00 USD | 0.00 USD | 563.16 USD | `-75.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.00` | 34,110,000.00 USD | 0.00 USD | 170.14 USD | `-74.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.00` | 34,110,000.00 USD | 0.00 USD | 259.78 USD | `-72.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.00` | 34,110,000.00 USD | 0.00 USD | 583.40 USD | `-71.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.00` | 34,110,000.00 USD | 0.00 USD | 613.93 USD | `-70.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.00` | 34,110,000.00 USD | 0.00 USD | 578.54 USD | `-69.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.00` | 34,110,000.00 USD | 0.00 USD | 242.21 USD | `-69.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 34,110,000.00 USD | 0.00 USD | 885.90 USD | `-68.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `715.00` | 34,110,000.00 USD | 0.00 USD | 4,130.00 USD | `-68.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `725.00` | 34,110,000.00 USD | 0.00 USD | 15,090.00 USD | `-67.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 34,090,000.00 USD | 0.00 USD | 177.27 USD | `-66.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 34,090,000.00 USD | 0.00 USD | 2,400.00 USD | `-64.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 34,090,000.00 USD | 0.00 USD | 1,670.00 USD | `-62.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 34,090,000.00 USD | 0.00 USD | 139,430.00 USD | `-61.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `875.00` | 33,950,000.00 USD | 0.00 USD | 918.49 USD | `-61.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 33,950,000.00 USD | 0.00 USD | 3,130.00 USD | `-60.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 33,940,000.00 USD | 0.00 USD | 2,780.00 USD | `-59.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 33,940,000.00 USD | 0.00 USD | 516.34 USD | `-56.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 33,940,000.00 USD | 0.00 USD | 100.50 USD | `-55.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 33,940,000.00 USD | 0.00 USD | 223,740.00 USD | `-55.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 33,720,000.00 USD | 0.00 USD | 445.08 USD | `-54.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 33,720,000.00 USD | 0.00 USD | 112.03 USD | `-54.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1045.00` | 33,720,000.00 USD | 0.00 USD | 1,260.00 USD | `-53.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 33,710,000.00 USD | 0.00 USD | 1,060.00 USD | `-52.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 33,710,000.00 USD | 0.00 USD | 995.34 USD | `-52.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 33,710,000.00 USD | 0.00 USD | 1,610.00 USD | `-50.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 33,710,000.00 USD | 0.00 USD | 11,050.00 USD | `-50.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 33,700,000.00 USD | 0.00 USD | 1,320.00 USD | `-49.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 33,700,000.00 USD | 0.00 USD | 1,000.00 USD | `-48.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 33,700,000.00 USD | 0.00 USD | 476.46 USD | `-47.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 33,700,000.00 USD | 0.00 USD | 228.47 USD | `-47.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1195.00` | 33,700,000.00 USD | 0.00 USD | 221.55 USD | `-46.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 33,700,000.00 USD | 0.00 USD | 3,880.00 USD | `-46.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 33,690,000.00 USD | 0.00 USD | 995.93 USD | `-45.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 33,690,000.00 USD | 0.00 USD | 951.93 USD | `-44.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 33,690,000.00 USD | 0.00 USD | 2,290.00 USD | `-44.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 33,690,000.00 USD | 0.00 USD | 9,050.00 USD | `-42.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 33,680,000.00 USD | 0.00 USD | 7,030.00 USD | `-42.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 33,670,000.00 USD | 0.00 USD | 23,030.00 USD | `-41.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 33,650,000.00 USD | 0.00 USD | 1,440.00 USD | `-41.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1335.00` | 33,650,000.00 USD | 0.00 USD | 281.69 USD | `-40.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 33,650,000.00 USD | 0.00 USD | 144,020.00 USD | `-40.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 33,500,000.00 USD | 0.00 USD | 128.86 USD | `-39.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 33,500,000.00 USD | 0.00 USD | 1,270.00 USD | `-39.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 33,500,000.00 USD | 0.00 USD | 4,160.00 USD | `-38.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1385.00` | 33,500,000.00 USD | 0.00 USD | 100,800.00 USD | `-38.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 33,400,000.00 USD | 0.00 USD | 535,600.00 USD | `-37.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 32,860,000.00 USD | 0.00 USD | 18,840.00 USD | `-37.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 32,840,000.00 USD | 0.00 USD | 6,450.00 USD | `-36.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 32,840,000.00 USD | 0.00 USD | 852.10 USD | `-36.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 32,830,000.00 USD | 0.00 USD | 1,610.00 USD | `-35.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 32,830,000.00 USD | 0.00 USD | 5,090.00 USD | `-35.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 32,830,000.00 USD | 0.00 USD | 19,730.00 USD | `-34.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 32,810,000.00 USD | 0.00 USD | 2,600.00 USD | `-34.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 32,810,000.00 USD | 0.00 USD | 19,930.00 USD | `-33.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 32,790,000.00 USD | 0.00 USD | 11,460.00 USD | `-33.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 32,770,000.00 USD | 0.00 USD | 68,840.00 USD | `-33.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 32,710,000.00 USD | 0.00 USD | 11,140.00 USD | `-32.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 32,690,000.00 USD | 0.00 USD | 31,900.00 USD | `-32.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 32,660,000.00 USD | 0.00 USD | 983.78 USD | `-31.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 32,660,000.00 USD | 0.00 USD | 2,090.00 USD | `-31.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 32,660,000.00 USD | 0.00 USD | 32,880.00 USD | `-30.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 32,630,000.00 USD | 0.00 USD | 10,660.00 USD | `-30.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 32,620,000.00 USD | 0.00 USD | 198,620.00 USD | `-29.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 32,420,000.00 USD | 0.00 USD | 4,990.00 USD | `-29.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 32,410,000.00 USD | 0.00 USD | 9,090.00 USD | `-29.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 32,400,000.00 USD | 0.00 USD | 431,660.00 USD | `-28.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 31,970,000.00 USD | 0.00 USD | 25,700.00 USD | `-28.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 31,950,000.00 USD | 0.00 USD | 15,920.00 USD | `-27.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 31,930,000.00 USD | 0.00 USD | 10,560.00 USD | `-27.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 31,920,000.00 USD | 0.00 USD | 323,930.00 USD | `-26.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 31,600,000.00 USD | 0.00 USD | 114,830.00 USD | `-26.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 31,480,000.00 USD | 0.00 USD | 999.83 USD | `-25.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 31,480,000.00 USD | 0.00 USD | 289.27 USD | `-25.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 31,480,000.00 USD | 0.00 USD | 35,320.00 USD | `-25.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 31,440,000.00 USD | 0.00 USD | 42,420.00 USD | `-24.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 31,400,000.00 USD | 0.00 USD | 84,860.00 USD | `-24.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 31,320,000.00 USD | 0.00 USD | 16,350.00 USD | `-23.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 31,300,000.00 USD | 0.00 USD | 47,500.00 USD | `-23.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 31,250,000.00 USD | 0.00 USD | 28,150.00 USD | `-22.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 31,220,000.00 USD | 0.00 USD | 3,180.00 USD | `-22.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 31,220,000.00 USD | 0.00 USD | 466,520.00 USD | `-21.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 30,750,000.00 USD | 0.00 USD | 77,450.00 USD | `-21.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 30,680,000.00 USD | 0.00 USD | 3,090.00 USD | `-21.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 30,670,000.00 USD | 0.00 USD | 8,500.00 USD | `-20.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 30,670,000.00 USD | 0.00 USD | 191,070.00 USD | `-20.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 30,470,000.00 USD | 0.00 USD | 744,540.00 USD | `-19.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 29,730,000.00 USD | 0.00 USD | 259,710.00 USD | `-19.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 29,470,000.00 USD | 0.00 USD | 45,060.00 USD | `-18.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 29,430,000.00 USD | 0.00 USD | 5,380.00 USD | `-18.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 29,420,000.00 USD | 0.00 USD | 30,780.00 USD | `-17.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 29,390,000.00 USD | 0.00 USD | 485,090.00 USD | `-17.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 28,900,000.00 USD | 0.00 USD | 41,250.00 USD | `-17.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 28,860,000.00 USD | 0.00 USD | 9,620.00 USD | `-16.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1885.00` | 28,850,000.00 USD | 0.00 USD | 19,770.00 USD | `-16.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 28,830,000.00 USD | 0.00 USD | 61,630.00 USD | `-15.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 28,770,000.00 USD | 0.00 USD | 152,510.00 USD | `-15.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 28,620,000.00 USD | 0.00 USD | 105,830.00 USD | `-14.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1925.00` | 28,510,000.00 USD | 0.00 USD | 56,430.00 USD | `-14.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1935.00` | 28,460,000.00 USD | 0.00 USD | 117,650.00 USD | `-13.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 28,340,000.00 USD | 0.00 USD | 61,020.00 USD | `-13.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 28,280,000.00 USD | 0.00 USD | 81,030.00 USD | `-13.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 28,200,000.00 USD | 0.00 USD | 138,620.00 USD | `-12.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 28,060,000.00 USD | 0.00 USD | 69,900.00 USD | `-12.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 27,990,000.00 USD | 0.00 USD | 105,150.00 USD | `-11.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 27,880,000.00 USD | 0.00 USD | 122,280.00 USD | `-11.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 27,760,000.00 USD | 0.00 USD | 2,080,000.00 USD | `-10.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 25,680,000.00 USD | 0.00 USD | 48,350.00 USD | `-10.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 25,630,000.00 USD | 0.00 USD | 15,730.00 USD | `-9.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 25,620,000.00 USD | 0.00 USD | 175,420.00 USD | `-9.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 25,440,000.00 USD | 0.00 USD | 50,140.00 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 25,390,000.00 USD | 0.00 USD | 269,160.00 USD | `-8.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 25,120,000.00 USD | 0.00 USD | 825,500.00 USD | `-8.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 24,300,000.00 USD | 0.00 USD | 148,720.00 USD | `-7.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 24,150,000.00 USD | 0.00 USD | 153,080.00 USD | `-7.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 24,000,000.00 USD | 0.00 USD | 33,690.00 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 23,960,000.00 USD | 0.00 USD | 470,900.00 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 23,490,000.00 USD | 0.00 USD | 191,710.00 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 23,300,000.00 USD | 0.00 USD | 462,910.00 USD | `-5.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 22,840,000.00 USD | 0.00 USD | 311,950.00 USD | `-5.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 22,530,000.00 USD | 0.00 USD | 492,720.00 USD | `-4.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 22,030,000.00 USD | 0.00 USD | 638,630.00 USD | `-4.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 21,390,000.00 USD | 0.00 USD | 1,710,000.00 USD | `-3.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 19,690,000.00 USD | 0.00 USD | 9,700,000.00 USD | `-3.29%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2185.00` | 9,980,000.00 USD | 0.00 USD | 271,670.00 USD | `-2.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 9,710,000.00 USD | 0.00 USD | 2,990,000.00 USD | `-2.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 6,720,000.00 USD | 0.00 USD | 1,610,000.00 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 5,120,000.00 USD | 0.00 USD | 3,070,000.00 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 2,050,000.00 USD | 0.00 USD | 584,790.00 USD | `-1.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2235.00` | 1,460,000.00 USD | 0.00 USD | 1,450,000.00 USD | `-0.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2245.00` | 15,080.00 USD | 0.00 USD | 15,080.00 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2255.00` | 573,280.00 USD | 573,280.00 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2265.00` | 2,540,000.00 USD | 1,970,000.00 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 3,000,000.00 USD | 455,570.00 USD | 0.00 USD | `+1.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 5,020,000.00 USD | 2,030,000.00 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 5,830,000.00 USD | 812,750.00 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 15,740,000.00 USD | 9,900,000.00 USD | 0.00 USD | `+2.49%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2315.00` | 16,860,000.00 USD | 1,120,000.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 17,090,000.00 USD | 229,720.00 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 17,250,000.00 USD | 164,580.00 USD | 0.00 USD | `+3.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 18,840,000.00 USD | 1,590,000.00 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 20,130,000.00 USD | 1,290,000.00 USD | 0.00 USD | `+4.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 22,350,000.00 USD | 2,210,000.00 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 22,510,000.00 USD | 166,390.00 USD | 0.00 USD | `+5.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 24,850,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 25,950,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 28,490,000.00 USD | 2,540,000.00 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 28,820,000.00 USD | 321,000.00 USD | 0.00 USD | `+7.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 31,090,000.00 USD | 2,280,000.00 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 31,280,000.00 USD | 192,130.00 USD | 0.00 USD | `+8.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 33,770,000.00 USD | 2,490,000.00 USD | 0.00 USD | `+8.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2455.00` | 33,920,000.00 USD | 148,840.00 USD | 0.00 USD | `+9.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 36,040,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+9.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 36,220,000.00 USD | 181,240.00 USD | 0.00 USD | `+10.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 38,330,000.00 USD | 2,100,000.00 USD | 0.00 USD | `+10.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 38,450,000.00 USD | 122,320.00 USD | 0.00 USD | `+10.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 41,000,000.00 USD | 2,550,000.00 USD | 0.00 USD | `+11.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2515.00` | 48,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | `+11.83%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 51,210,000.00 USD | 2,610,000.00 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 51,280,000.00 USD | 61,230.00 USD | 0.00 USD | `+12.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 53,450,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+13.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 53,650,000.00 USD | 200,490.00 USD | 0.00 USD | `+13.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 56,010,000.00 USD | 2,360,000.00 USD | 0.00 USD | `+14.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 56,100,000.00 USD | 93,110.00 USD | 0.00 USD | `+14.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 58,620,000.00 USD | 2,510,000.00 USD | 0.00 USD | `+14.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 58,630,000.00 USD | 10,500.00 USD | 0.00 USD | `+15.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 61,900,000.00 USD | 3,270,000.00 USD | 0.00 USD | `+15.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 61,980,000.00 USD | 79,040.00 USD | 0.00 USD | `+16.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 64,160,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+16.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 64,300,000.00 USD | 147,930.00 USD | 0.00 USD | `+17.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 66,430,000.00 USD | 2,130,000.00 USD | 0.00 USD | `+17.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 66,740,000.00 USD | 306,950.00 USD | 0.00 USD | `+18.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 68,880,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+18.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 69,150,000.00 USD | 265,610.00 USD | 0.00 USD | `+18.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 71,320,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+19.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 71,420,000.00 USD | 94,620.00 USD | 0.00 USD | `+19.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 74,270,000.00 USD | 2,850,000.00 USD | 0.00 USD | `+20.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 74,340,000.00 USD | 76,590.00 USD | 0.00 USD | `+20.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 74,630,000.00 USD | 286,910.00 USD | 0.00 USD | `+21.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 74,670,000.00 USD | 43,050.00 USD | 0.00 USD | `+21.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 74,850,000.00 USD | 180,060.00 USD | 0.00 USD | `+22.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 75,750,000.00 USD | 892,350.00 USD | 0.00 USD | `+22.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 75,850,000.00 USD | 103,020.00 USD | 0.00 USD | `+22.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 76,430,000.00 USD | 577,610.00 USD | 0.00 USD | `+23.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 76,460,000.00 USD | 35,580.00 USD | 0.00 USD | `+23.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 76,480,000.00 USD | 17,550.00 USD | 0.00 USD | `+24.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 77,380,000.00 USD | 905,020.00 USD | 0.00 USD | `+24.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 77,440,000.00 USD | 52,490.00 USD | 0.00 USD | `+25.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 77,480,000.00 USD | 43,930.00 USD | 0.00 USD | `+25.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 77,770,000.00 USD | 286,140.00 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 78,770,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+26.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 80,040,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+26.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 80,050,000.00 USD | 11,150.00 USD | 0.00 USD | `+27.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 80,060,000.00 USD | 2,460.00 USD | 0.00 USD | `+27.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 80,360,000.00 USD | 305,820.00 USD | 0.00 USD | `+28.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 80,380,000.00 USD | 16,190.00 USD | 0.00 USD | `+28.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 81,860,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+29.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 81,870,000.00 USD | 10,340.00 USD | 0.00 USD | `+29.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 81,880,000.00 USD | 3,050.00 USD | 0.00 USD | `+30.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 81,930,000.00 USD | 52,370.00 USD | 0.00 USD | `+30.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 81,960,000.00 USD | 34,650.00 USD | 0.00 USD | `+30.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 82,010,000.00 USD | 44,750.00 USD | 0.00 USD | `+31.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 82,120,000.00 USD | 113,340.00 USD | 0.00 USD | `+31.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 82,270,000.00 USD | 145,510.00 USD | 0.00 USD | `+32.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 83,200,000.00 USD | 931,470.00 USD | 0.00 USD | `+32.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 88,120,000.00 USD | 4,920,000.00 USD | 0.00 USD | `+33.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 90,200,000.00 USD | 2,080,000.00 USD | 0.00 USD | `+33.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 90,210,000.00 USD | 9,740.00 USD | 0.00 USD | `+34.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 90,240,000.00 USD | 35,380.00 USD | 0.00 USD | `+34.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 90,320,000.00 USD | 74,910.00 USD | 0.00 USD | `+34.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 90,340,000.00 USD | 22,460.00 USD | 0.00 USD | `+35.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 91,110,000.00 USD | 771,070.00 USD | 0.00 USD | `+35.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 91,110,000.00 USD | 612.69 USD | 0.00 USD | `+36.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 91,160,000.00 USD | 49,330.00 USD | 0.00 USD | `+36.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 91,180,000.00 USD | 19,570.00 USD | 0.00 USD | `+37.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 91,180,000.00 USD | 928.50 USD | 0.00 USD | `+37.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 103,060,000.00 USD | 11,880,000.00 USD | 0.00 USD | `+38.06%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 103,170,000.00 USD | 110,480.00 USD | 0.00 USD | `+38.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 103,550,000.00 USD | 381,020.00 USD | 0.00 USD | `+38.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3135.00` | 103,550,000.00 USD | 674.02 USD | 0.00 USD | `+39.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 103,560,000.00 USD | 2,660.00 USD | 0.00 USD | `+39.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 103,620,000.00 USD | 58,930.00 USD | 0.00 USD | `+40.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 103,630,000.00 USD | 9,860.00 USD | 0.00 USD | `+40.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 103,630,000.00 USD | 149.22 USD | 0.00 USD | `+41.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 103,630,000.00 USD | 1,920.00 USD | 0.00 USD | `+41.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 103,670,000.00 USD | 41,120.00 USD | 0.00 USD | `+42.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 104,330,000.00 USD | 663,130.00 USD | 0.00 USD | `+42.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 104,330,000.00 USD | 1,760.00 USD | 0.00 USD | `+42.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 104,490,000.00 USD | 156,230.00 USD | 0.00 USD | `+43.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 104,490,000.00 USD | 167.25 USD | 0.00 USD | `+43.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 104,550,000.00 USD | 57,500.00 USD | 0.00 USD | `+44.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 104,780,000.00 USD | 236,580.00 USD | 0.00 USD | `+44.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 104,800,000.00 USD | 15,710.00 USD | 0.00 USD | `+45.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 104,800,000.00 USD | 1,630.00 USD | 0.00 USD | `+45.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 104,940,000.00 USD | 141,980.00 USD | 0.00 USD | `+46.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 104,960,000.00 USD | 15,350.00 USD | 0.00 USD | `+46.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 106,370,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+46.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 106,760,000.00 USD | 389,970.00 USD | 0.00 USD | `+47.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 106,790,000.00 USD | 24,200.00 USD | 0.00 USD | `+47.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 106,790,000.00 USD | 4,350.00 USD | 0.00 USD | `+48.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 106,790,000.00 USD | 2,170.00 USD | 0.00 USD | `+48.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 106,800,000.00 USD | 2,520.00 USD | 0.00 USD | `+49.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 106,800,000.00 USD | 295.78 USD | 0.00 USD | `+49.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 106,820,000.00 USD | 21,260.00 USD | 0.00 USD | `+50.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 106,870,000.00 USD | 58,010.00 USD | 0.00 USD | `+50.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 107,200,000.00 USD | 321,800.00 USD | 0.00 USD | `+50.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 108,680,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+51.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 108,690,000.00 USD | 5,700.00 USD | 0.00 USD | `+51.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 108,700,000.00 USD | 16,310.00 USD | 0.00 USD | `+52.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 108,720,000.00 USD | 15,030.00 USD | 0.00 USD | `+53.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 108,740,000.00 USD | 18,600.00 USD | 0.00 USD | `+53.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 108,740,000.00 USD | 495.50 USD | 0.00 USD | `+54.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 108,740,000.00 USD | 3,190.00 USD | 0.00 USD | `+54.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 108,780,000.00 USD | 43,610.00 USD | 0.00 USD | `+54.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 108,780,000.00 USD | 158.32 USD | 0.00 USD | `+55.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 109,230,000.00 USD | 446,770.00 USD | 0.00 USD | `+55.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 109,270,000.00 USD | 43,460.00 USD | 0.00 USD | `+56.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 109,280,000.00 USD | 3,690.00 USD | 0.00 USD | `+56.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 109,290,000.00 USD | 9,810.00 USD | 0.00 USD | `+57.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 109,380,000.00 USD | 90,810.00 USD | 0.00 USD | `+58.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 109,380,000.00 USD | 2,300.00 USD | 0.00 USD | `+58.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3575.00` | 109,380,000.00 USD | 2,870.00 USD | 0.00 USD | `+58.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 109,380,000.00 USD | 354.92 USD | 0.00 USD | `+59.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 109,400,000.00 USD | 13,160.00 USD | 0.00 USD | `+59.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 109,500,000.00 USD | 105,150.00 USD | 0.00 USD | `+60.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3615.00` | 109,500,000.00 USD | 199.55 USD | 0.00 USD | `+60.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 109,510,000.00 USD | 10,210.00 USD | 0.00 USD | `+61.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 109,520,000.00 USD | 7,790.00 USD | 0.00 USD | `+61.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 109,520,000.00 USD | 3,860.00 USD | 0.00 USD | `+62.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 109,530,000.00 USD | 8,100.00 USD | 0.00 USD | `+62.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 109,540,000.00 USD | 8,130.00 USD | 0.00 USD | `+62.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 109,590,000.00 USD | 55,120.00 USD | 0.00 USD | `+63.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 109,600,000.00 USD | 1,410.00 USD | 0.00 USD | `+63.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 109,600,000.00 USD | 819.92 USD | 0.00 USD | `+64.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 109,600,000.00 USD | 323.58 USD | 0.00 USD | `+65.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 109,600,000.00 USD | 1,400.00 USD | 0.00 USD | `+65.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 109,610,000.00 USD | 6,490.00 USD | 0.00 USD | `+66.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3745.00` | 109,610,000.00 USD | 165.90 USD | 0.00 USD | `+66.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 109,610,000.00 USD | 751.00 USD | 0.00 USD | `+66.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 109,610,000.00 USD | 286.90 USD | 0.00 USD | `+68.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 109,610,000.00 USD | 1,560.00 USD | 0.00 USD | `+68.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 110,340,000.00 USD | 732,630.00 USD | 0.00 USD | `+69.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 110,360,000.00 USD | 20,930.00 USD | 0.00 USD | `+69.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 110,370,000.00 USD | 8,380.00 USD | 0.00 USD | `+70.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 110,370,000.00 USD | 711.78 USD | 0.00 USD | `+70.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 110,370,000.00 USD | 355.28 USD | 0.00 USD | `+70.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 110,380,000.00 USD | 5,170.00 USD | 0.00 USD | `+71.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 110,400,000.00 USD | 19,430.00 USD | 0.00 USD | `+72.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 110,410,000.00 USD | 12,120.00 USD | 0.00 USD | `+73.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 111,120,000.00 USD | 717,170.00 USD | 0.00 USD | `+74.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 111,170,000.00 USD | 42,570.00 USD | 0.00 USD | `+74.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 111,230,000.00 USD | 59,170.00 USD | 0.00 USD | `+75.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 111,230,000.00 USD | 1,380.00 USD | 0.00 USD | `+75.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 111,230,000.00 USD | 6,960.00 USD | 0.00 USD | `+76.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 111,250,000.00 USD | 14,610.00 USD | 0.00 USD | `+77.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 111,250,000.00 USD | 4,280.00 USD | 0.00 USD | `+77.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 113,890,000.00 USD | 2,640,000.00 USD | 0.00 USD | `+78.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 113,890,000.00 USD | 898.59 USD | 0.00 USD | `+79.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 113,890,000.00 USD | 811.00 USD | 0.00 USD | `+80.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 113,900,000.00 USD | 4,310.00 USD | 0.00 USD | `+81.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 113,900,000.00 USD | 3,050.00 USD | 0.00 USD | `+81.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 113,940,000.00 USD | 36,740.00 USD | 0.00 USD | `+82.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 113,940,000.00 USD | 5,990.00 USD | 0.00 USD | `+82.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 113,940,000.00 USD | 372.90 USD | 0.00 USD | `+83.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 113,940,000.00 USD | 395.43 USD | 0.00 USD | `+84.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 113,940,000.00 USD | 376.65 USD | 0.00 USD | `+86.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 113,990,000.00 USD | 42,260.00 USD | 0.00 USD | `+86.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 113,990,000.00 USD | 460.70 USD | 0.00 USD | `+87.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 113,990,000.00 USD | 1,270.00 USD | 0.00 USD | `+87.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 113,990,000.00 USD | 4,300.00 USD | 0.00 USD | `+89.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 113,990,000.00 USD | 437.16 USD | 0.00 USD | `+89.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 114,060,000.00 USD | 64,550.00 USD | 0.00 USD | `+90.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 114,060,000.00 USD | 1,610.00 USD | 0.00 USD | `+90.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 114,150,000.00 USD | 94,600.00 USD | 0.00 USD | `+91.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 114,150,000.00 USD | 1,070.00 USD | 0.00 USD | `+91.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 114,170,000.00 USD | 11,270.00 USD | 0.00 USD | `+93.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 114,170,000.00 USD | 2,400.00 USD | 0.00 USD | `+93.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 114,210,000.00 USD | 43,750.00 USD | 0.00 USD | `+94.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 114,280,000.00 USD | 64,570.00 USD | 0.00 USD | `+94.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 114,280,000.00 USD | 1,050.00 USD | 0.00 USD | `+95.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 114,330,000.00 USD | 57,640.00 USD | 0.00 USD | `+95.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 114,350,000.00 USD | 11,480.00 USD | 0.00 USD | `+96.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 114,350,000.00 USD | 2,510.00 USD | 0.00 USD | `+96.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 114,530,000.00 USD | 177,400.00 USD | 0.00 USD | `+97.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 114,530,000.00 USD | 2,040.00 USD | 0.00 USD | `+98.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4465.00` | 114,530,000.00 USD | 1,030.00 USD | 0.00 USD | `+98.53%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1972.30` | 871,060,000.00 USD | 0.00 USD | 871,060,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD |
| `7D` | `1975.10` | 870,930,000.00 USD | 0.00 USD | 870,930,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD |
| `7D` | `1977.90` | 870,880,000.00 USD | 0.00 USD | 870,880,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1983.50` | 868,640,000.00 USD | 0.00 USD | 868,640,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD |
| `7D` | `1986.30` | 868,430,000.00 USD | 0.00 USD | 868,430,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1989.10` | 864,700,000.00 USD | 0.00 USD | 864,700,000.00 USD | 0.00 USD | 1,780,000.00 USD | 38,060.00 USD |
| `7D` | `1991.90` | 862,890,000.00 USD | 0.00 USD | 862,890,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD |
| `7D` | `1994.70` | 860,180,000.00 USD | 0.00 USD | 860,180,000.00 USD | 0.00 USD | 0.00 USD | 808,380.00 USD |
| `7D` | `1997.50` | 859,370,000.00 USD | 0.00 USD | 859,370,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1997.60` | 755,360,000.00 USD | 0.00 USD | 755,360,000.00 USD | 206,020.00 USD | 86,340.00 USD | 328,290.00 USD |
| `1D` | `2000.10` | 754,740,000.00 USD | 0.00 USD | 754,740,000.00 USD | 27,360.00 USD | 25,630.00 USD | 586,930.00 USD |
| `1D` | `2002.60` | 754,100,000.00 USD | 0.00 USD | 754,100,000.00 USD | 942,390.00 USD | 700,600.00 USD | 1,180,000.00 USD |
| `7D` | `2003.10` | 858,030,000.00 USD | 0.00 USD | 858,030,000.00 USD | 0.00 USD | 266,430.00 USD | 617,240.00 USD |
| `1D` | `2005.10` | 751,280,000.00 USD | 0.00 USD | 751,280,000.00 USD | 773,690.00 USD | 255,310.00 USD | 9,210.00 USD |
| `7D` | `2005.90` | 857,140,000.00 USD | 0.00 USD | 857,140,000.00 USD | 0.00 USD | 475,660.00 USD | 0.00 USD |
| `1D` | `2007.60` | 750,240,000.00 USD | 0.00 USD | 750,240,000.00 USD | 0.00 USD | 383,650.00 USD | 281,160.00 USD |
| `7D` | `2008.70` | 856,670,000.00 USD | 0.00 USD | 856,670,000.00 USD | 807,770.00 USD | 0.00 USD | 380,820.00 USD |
| `1D` | `2010.10` | 749,580,000.00 USD | 0.00 USD | 749,580,000.00 USD | 460,200.00 USD | 638,030.00 USD | 374,070.00 USD |
| `7D` | `2011.50` | 855,480,000.00 USD | 0.00 USD | 855,480,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD |
| `1D` | `2012.60` | 748,100,000.00 USD | 0.00 USD | 748,100,000.00 USD | 348,530.00 USD | 266,130.00 USD | 25,520.00 USD |
| `1D` | `2015.10` | 747,460,000.00 USD | 0.00 USD | 747,460,000.00 USD | 413,060.00 USD | 159,880.00 USD | 202,180.00 USD |
| `7D` | `2017.10` | 854,520,000.00 USD | 0.00 USD | 854,520,000.00 USD | 62,110.00 USD | 0.00 USD | 21,830.00 USD |
| `1D` | `2017.60` | 746,690,000.00 USD | 0.00 USD | 746,690,000.00 USD | 1,140,000.00 USD | 1,500,000.00 USD | 573,330.00 USD |
| `7D` | `2019.90` | 854,440,000.00 USD | 0.00 USD | 854,440,000.00 USD | 1,020,000.00 USD | 466,180.00 USD | 0.00 USD |
| `1D` | `2020.10` | 743,480,000.00 USD | 0.00 USD | 743,480,000.00 USD | 1,340,000.00 USD | 2,190,000.00 USD | 696,790.00 USD |
| `1D` | `2022.60` | 739,250,000.00 USD | 0.00 USD | 739,250,000.00 USD | 1,840,000.00 USD | 628,480.00 USD | 1,890,000.00 USD |
| `7D` | `2022.70` | 852,960,000.00 USD | 0.00 USD | 852,960,000.00 USD | 1,890,000.00 USD | 957,590.00 USD | 1,550,000.00 USD |
| `1D` | `2025.10` | 734,890,000.00 USD | 0.00 USD | 734,890,000.00 USD | 595,510.00 USD | 1,010,000.00 USD | 240,540.00 USD |
| `7D` | `2025.50` | 848,560,000.00 USD | 0.00 USD | 848,560,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2027.60` | 733,050,000.00 USD | 0.00 USD | 733,050,000.00 USD | 2,550,000.00 USD | 1,160,000.00 USD | 167,580.00 USD |
| `7D` | `2028.30` | 848,380,000.00 USD | 0.00 USD | 848,380,000.00 USD | 1,100,000.00 USD | 0.00 USD | 35,180.00 USD |
| `1D` | `2030.10` | 729,170,000.00 USD | 0.00 USD | 729,170,000.00 USD | 307,680.00 USD | 366,120.00 USD | 1,100,000.00 USD |
| `7D` | `2031.10` | 847,250,000.00 USD | 0.00 USD | 847,250,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD |
| `1D` | `2032.60` | 727,390,000.00 USD | 0.00 USD | 727,390,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD |
| `7D` | `2033.90` | 842,680,000.00 USD | 0.00 USD | 842,680,000.00 USD | 0.00 USD | 0.00 USD | 1,350,000.00 USD |
| `1D` | `2035.10` | 723,840,000.00 USD | 0.00 USD | 723,840,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD |
| `7D` | `2036.70` | 841,320,000.00 USD | 0.00 USD | 841,320,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD |
| `1D` | `2037.60` | 722,500,000.00 USD | 0.00 USD | 722,500,000.00 USD | 396,700.00 USD | 458,110.00 USD | 378,700.00 USD |
| `7D` | `2039.50` | 840,990,000.00 USD | 0.00 USD | 840,990,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2040.10` | 721,260,000.00 USD | 0.00 USD | 721,260,000.00 USD | 542,670.00 USD | 178,560.00 USD | 31,670.00 USD |
| `1D` | `2042.60` | 720,510,000.00 USD | 0.00 USD | 720,510,000.00 USD | 626,840.00 USD | 0.00 USD | 174,920.00 USD |
| `1D` | `2045.10` | 719,710,000.00 USD | 0.00 USD | 719,710,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD |
| `7D` | `2045.10` | 839,540,000.00 USD | 0.00 USD | 839,540,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD |
| `1D` | `2047.60` | 719,680,000.00 USD | 0.00 USD | 719,680,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD |
| `1D` | `2050.10` | 718,860,000.00 USD | 0.00 USD | 718,860,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2050.70` | 839,240,000.00 USD | 0.00 USD | 839,240,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2053.50` | 839,020,000.00 USD | 0.00 USD | 839,020,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2055.10` | 717,750,000.00 USD | 0.00 USD | 717,750,000.00 USD | 242,080.00 USD | 88,880.00 USD | 28,160.00 USD |
| `7D` | `2059.10` | 836,730,000.00 USD | 0.00 USD | 836,730,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `1D` | `2060.10` | 717,390,000.00 USD | 0.00 USD | 717,390,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2061.90` | 836,390,000.00 USD | 0.00 USD | 836,390,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `1D` | `2062.60` | 716,630,000.00 USD | 0.00 USD | 716,630,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD |
| `7D` | `2064.70` | 831,130,000.00 USD | 0.00 USD | 831,130,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `1D` | `2065.10` | 716,550,000.00 USD | 0.00 USD | 716,550,000.00 USD | 563,140.00 USD | 537,030.00 USD | 510,200.00 USD |
| `7D` | `2067.50` | 828,670,000.00 USD | 0.00 USD | 828,670,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD |
| `1D` | `2067.60` | 714,940,000.00 USD | 0.00 USD | 714,940,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD |
| `1D` | `2070.10` | 714,250,000.00 USD | 0.00 USD | 714,250,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD |
| `7D` | `2070.30` | 827,020,000.00 USD | 0.00 USD | 827,020,000.00 USD | 3,600,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `1D` | `2072.60` | 713,870,000.00 USD | 0.00 USD | 713,870,000.00 USD | 47,910.00 USD | 555,250.00 USD | 420,170.00 USD |
| `7D` | `2073.10` | 819,460,000.00 USD | 0.00 USD | 819,460,000.00 USD | 2,870,000.00 USD | 2,180,000.00 USD | 2,030,000.00 USD |
| `1D` | `2075.10` | 712,850,000.00 USD | 0.00 USD | 712,850,000.00 USD | 25,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2075.90` | 812,380,000.00 USD | 0.00 USD | 812,380,000.00 USD | 3,910,000.00 USD | 4,290,000.00 USD | 4,300,000.00 USD |
| `1D` | `2077.60` | 712,830,000.00 USD | 0.00 USD | 712,830,000.00 USD | 354,080.00 USD | 25,190.00 USD | 0.00 USD |
| `7D` | `2078.70` | 799,880,000.00 USD | 0.00 USD | 799,880,000.00 USD | 4,160,000.00 USD | 3,730,000.00 USD | 2,060,000.00 USD |
| `1D` | `2080.10` | 712,450,000.00 USD | 0.00 USD | 712,450,000.00 USD | 77,960.00 USD | 29,610.00 USD | 199,420.00 USD |
| `7D` | `2081.50` | 789,930,000.00 USD | 0.00 USD | 789,930,000.00 USD | 4,400,000.00 USD | 1,290,000.00 USD | 1,220,000.00 USD |
| `1D` | `2082.60` | 712,140,000.00 USD | 0.00 USD | 712,140,000.00 USD | 827,940.00 USD | 4,240.00 USD | 206,010.00 USD |
| `7D` | `2084.30` | 783,020,000.00 USD | 0.00 USD | 783,020,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 3,500,000.00 USD |
| `1D` | `2085.10` | 711,100,000.00 USD | 0.00 USD | 711,100,000.00 USD | 528,660.00 USD | 200,510.00 USD | 820,410.00 USD |
| `7D` | `2087.10` | 775,630,000.00 USD | 0.00 USD | 775,630,000.00 USD | 2,920,000.00 USD | 2,750,000.00 USD | 3,020,000.00 USD |
| `1D` | `2087.60` | 709,550,000.00 USD | 0.00 USD | 709,550,000.00 USD | 324,560.00 USD | 170,940.00 USD | 302,640.00 USD |
| `7D` | `2089.90` | 766,950,000.00 USD | 0.00 USD | 766,950,000.00 USD | 4,130,000.00 USD | 948,120.00 USD | 3,160,000.00 USD |
| `1D` | `2090.10` | 708,750,000.00 USD | 0.00 USD | 708,750,000.00 USD | 461,140.00 USD | 207,680.00 USD | 251,600.00 USD |
| `1D` | `2092.60` | 707,830,000.00 USD | 0.00 USD | 707,830,000.00 USD | 587,740.00 USD | 226,930.00 USD | 199,290.00 USD |
| `7D` | `2092.70` | 758,710,000.00 USD | 0.00 USD | 758,710,000.00 USD | 4,680,000.00 USD | 737,060.00 USD | 6,220,000.00 USD |
| `1D` | `2095.10` | 706,820,000.00 USD | 0.00 USD | 706,820,000.00 USD | 1,370,000.00 USD | 838,640.00 USD | 1,080,000.00 USD |
| `7D` | `2095.50` | 747,080,000.00 USD | 0.00 USD | 747,080,000.00 USD | 2,480,000.00 USD | 2,010,000.00 USD | 1,020,000.00 USD |
| `1D` | `2097.60` | 703,530,000.00 USD | 0.00 USD | 703,530,000.00 USD | 87,950.00 USD | 672,980.00 USD | 555,060.00 USD |
| `7D` | `2098.30` | 741,570,000.00 USD | 0.00 USD | 741,570,000.00 USD | 3,020,000.00 USD | 3,130,000.00 USD | 1,480,000.00 USD |
| `1D` | `2100.10` | 702,210,000.00 USD | 0.00 USD | 702,210,000.00 USD | 307,340.00 USD | 928,890.00 USD | 50,560.00 USD |
| `7D` | `2101.10` | 733,950,000.00 USD | 0.00 USD | 733,950,000.00 USD | 631,640.00 USD | 1,240,000.00 USD | 3,400,000.00 USD |
| `1D` | `2102.60` | 700,930,000.00 USD | 0.00 USD | 700,930,000.00 USD | 211,840.00 USD | 222,480.00 USD | 483,690.00 USD |
| `7D` | `2103.90` | 728,670,000.00 USD | 0.00 USD | 728,670,000.00 USD | 1,130,000.00 USD | 738,240.00 USD | 2,320,000.00 USD |
| `1D` | `2105.10` | 700,010,000.00 USD | 0.00 USD | 700,010,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 691,960.00 USD |
| `7D` | `2106.70` | 724,480,000.00 USD | 0.00 USD | 724,480,000.00 USD | 1,700,000.00 USD | 834,660.00 USD | 1,180,000.00 USD |
| `1D` | `2107.60` | 694,580,000.00 USD | 0.00 USD | 694,580,000.00 USD | 734,860.00 USD | 0.00 USD | 488,260.00 USD |
| `7D` | `2109.50` | 720,760,000.00 USD | 0.00 USD | 720,760,000.00 USD | 7,750,000.00 USD | 1,800,000.00 USD | 1,770,000.00 USD |
| `1D` | `2110.10` | 693,360,000.00 USD | 0.00 USD | 693,360,000.00 USD | 61,010.00 USD | 31,550.00 USD | 6,190.00 USD |
| `7D` | `2112.30` | 709,450,000.00 USD | 0.00 USD | 709,450,000.00 USD | 3,920,000.00 USD | 1,480,000.00 USD | 3,710,000.00 USD |
| `1D` | `2112.60` | 693,260,000.00 USD | 0.00 USD | 693,260,000.00 USD | 902,600.00 USD | 360,140.00 USD | 221,490.00 USD |
| `1D` | `2115.10` | 691,780,000.00 USD | 0.00 USD | 691,780,000.00 USD | 202,800.00 USD | 411,610.00 USD | 962,630.00 USD |
| `7D` | `2115.10` | 700,330,000.00 USD | 0.00 USD | 700,330,000.00 USD | 923,330.00 USD | 3,210,000.00 USD | 1,930,000.00 USD |
| `1D` | `2117.60` | 690,200,000.00 USD | 0.00 USD | 690,200,000.00 USD | 4,750,000.00 USD | 4,080,000.00 USD | 302,800.00 USD |
| `7D` | `2117.90` | 694,260,000.00 USD | 0.00 USD | 694,260,000.00 USD | 8,390,000.00 USD | 578,010.00 USD | 2,580,000.00 USD |
| `1D` | `2120.10` | 681,070,000.00 USD | 0.00 USD | 681,070,000.00 USD | 3,950,000.00 USD | 22,470.00 USD | 645,650.00 USD |
| `7D` | `2120.70` | 682,710,000.00 USD | 0.00 USD | 682,710,000.00 USD | 7,060,000.00 USD | 5,780,000.00 USD | 1,820,000.00 USD |
| `1D` | `2122.60` | 676,460,000.00 USD | 0.00 USD | 676,460,000.00 USD | 4,520,000.00 USD | 3,800,000.00 USD | 1,860,000.00 USD |
| `7D` | `2123.50` | 668,060,000.00 USD | 0.00 USD | 668,060,000.00 USD | 7,150,000.00 USD | 7,720,000.00 USD | 1,410,000.00 USD |
| `1D` | `2125.10` | 666,280,000.00 USD | 0.00 USD | 666,280,000.00 USD | 6,940,000.00 USD | 1,830,000.00 USD | 2,110,000.00 USD |
| `7D` | `2126.30` | 651,780,000.00 USD | 0.00 USD | 651,780,000.00 USD | 2,740,000.00 USD | 4,400,000.00 USD | 4,790,000.00 USD |
| `1D` | `2127.60` | 655,400,000.00 USD | 0.00 USD | 655,400,000.00 USD | 4,430,000.00 USD | 4,180,000.00 USD | 782,350.00 USD |
| `7D` | `2129.10` | 639,850,000.00 USD | 0.00 USD | 639,850,000.00 USD | 4,770,000.00 USD | 1,270,000.00 USD | 1,100,000.00 USD |
| `1D` | `2130.10` | 646,010,000.00 USD | 0.00 USD | 646,010,000.00 USD | 1,250,000.00 USD | 172,040.00 USD | 794,920.00 USD |
| `7D` | `2131.90` | 632,700,000.00 USD | 0.00 USD | 632,700,000.00 USD | 2,170,000.00 USD | 1,620,000.00 USD | 1,360,000.00 USD |
| `1D` | `2132.60` | 643,800,000.00 USD | 0.00 USD | 643,800,000.00 USD | 81,820.00 USD | 284,820.00 USD | 1,550,000.00 USD |
| `7D` | `2134.70` | 627,550,000.00 USD | 0.00 USD | 627,550,000.00 USD | 1,630,000.00 USD | 790,240.00 USD | 898,290.00 USD |
| `1D` | `2135.10` | 641,880,000.00 USD | 0.00 USD | 641,880,000.00 USD | 2,560,000.00 USD | 2,610,000.00 USD | 1,540,000.00 USD |
| `7D` | `2137.50` | 624,240,000.00 USD | 0.00 USD | 624,240,000.00 USD | 2,120,000.00 USD | 2,390,000.00 USD | 1,590,000.00 USD |
| `1D` | `2137.60` | 635,160,000.00 USD | 0.00 USD | 635,160,000.00 USD | 889,780.00 USD | 2,180,000.00 USD | 1,940,000.00 USD |
| `1D` | `2140.10` | 630,150,000.00 USD | 0.00 USD | 630,150,000.00 USD | 1,990,000.00 USD | 749,480.00 USD | 758,120.00 USD |
| `7D` | `2140.30` | 618,140,000.00 USD | 0.00 USD | 618,140,000.00 USD | 3,990,000.00 USD | 1,870,000.00 USD | 1,690,000.00 USD |
| `1D` | `2142.60` | 626,650,000.00 USD | 0.00 USD | 626,650,000.00 USD | 873,550.00 USD | 3,390,000.00 USD | 1,100,000.00 USD |
| `7D` | `2143.10` | 610,600,000.00 USD | 0.00 USD | 610,600,000.00 USD | 2,380,000.00 USD | 618,280.00 USD | 333,410.00 USD |
| `1D` | `2145.10` | 621,280,000.00 USD | 0.00 USD | 621,280,000.00 USD | 2,780,000.00 USD | 2,360,000.00 USD | 1,220,000.00 USD |
| `7D` | `2145.90` | 607,270,000.00 USD | 0.00 USD | 607,270,000.00 USD | 978,940.00 USD | 1,450,000.00 USD | 1,720,000.00 USD |
| `1D` | `2147.60` | 614,920,000.00 USD | 0.00 USD | 614,920,000.00 USD | 1,610,000.00 USD | 1,170,000.00 USD | 105,220.00 USD |
| `7D` | `2148.70` | 603,120,000.00 USD | 0.00 USD | 603,120,000.00 USD | 26,270.00 USD | 538,910.00 USD | 399,680.00 USD |
| `1D` | `2150.10` | 612,040,000.00 USD | 0.00 USD | 612,040,000.00 USD | 7,520,000.00 USD | 3,310,000.00 USD | 2,660,000.00 USD |
| `7D` | `2151.50` | 602,150,000.00 USD | 0.00 USD | 602,150,000.00 USD | 11,350,000.00 USD | 363,770.00 USD | 107,200.00 USD |
| `1D` | `2152.60` | 598,540,000.00 USD | 0.00 USD | 598,540,000.00 USD | 5,270,000.00 USD | 3,330,000.00 USD | 2,020,000.00 USD |
| `7D` | `2154.30` | 590,330,000.00 USD | 0.00 USD | 590,330,000.00 USD | 2,590,000.00 USD | 4,660,000.00 USD | 1,620,000.00 USD |
| `1D` | `2155.10` | 587,920,000.00 USD | 0.00 USD | 587,920,000.00 USD | 4,130,000.00 USD | 7,120,000.00 USD | 2,620,000.00 USD |
| `7D` | `2157.10` | 581,470,000.00 USD | 0.00 USD | 581,470,000.00 USD | 6,320,000.00 USD | 3,720,000.00 USD | 6,600,000.00 USD |
| `1D` | `2157.60` | 574,050,000.00 USD | 0.00 USD | 574,050,000.00 USD | 6,160,000.00 USD | 2,080,000.00 USD | 4,850,000.00 USD |
| `7D` | `2159.90` | 564,820,000.00 USD | 0.00 USD | 564,820,000.00 USD | 2,980,000.00 USD | 737,260.00 USD | 1,830,000.00 USD |
| `1D` | `2160.10` | 560,960,000.00 USD | 0.00 USD | 560,960,000.00 USD | 5,100,000.00 USD | 6,230,000.00 USD | 2,930,000.00 USD |
| `1D` | `2162.60` | 546,710,000.00 USD | 0.00 USD | 546,710,000.00 USD | 17,620,000.00 USD | 10,310,000.00 USD | 1,950,000.00 USD |
| `7D` | `2162.70` | 559,270,000.00 USD | 0.00 USD | 559,270,000.00 USD | 17,980,000.00 USD | 1,960,000.00 USD | 0.00 USD |
| `1D` | `2165.10` | 516,820,000.00 USD | 0.00 USD | 516,820,000.00 USD | 11,270,000.00 USD | 9,810,000.00 USD | 5,000,000.00 USD |
| `7D` | `2165.50` | 539,320,000.00 USD | 0.00 USD | 539,320,000.00 USD | 8,990,000.00 USD | 17,170,000.00 USD | 2,900,000.00 USD |
| `1D` | `2167.60` | 490,730,000.00 USD | 0.00 USD | 490,730,000.00 USD | 17,280,000.00 USD | 7,820,000.00 USD | 5,200,000.00 USD |
| `7D` | `2168.30` | 510,270,000.00 USD | 0.00 USD | 510,270,000.00 USD | 12,290,000.00 USD | 16,150,000.00 USD | 3,760,000.00 USD |
| `1D` | `2170.10` | 460,430,000.00 USD | 0.00 USD | 460,430,000.00 USD | 13,580,000.00 USD | 9,360,000.00 USD | 4,760,000.00 USD |
| `7D` | `2171.10` | 478,060,000.00 USD | 0.00 USD | 478,060,000.00 USD | 1,860,000.00 USD | 6,380,000.00 USD | 5,570,000.00 USD |
| `1D` | `2172.60` | 432,730,000.00 USD | 0.00 USD | 432,730,000.00 USD | 16,900,000.00 USD | 5,140,000.00 USD | 4,630,000.00 USD |
| `7D` | `2173.90` | 464,260,000.00 USD | 0.00 USD | 464,260,000.00 USD | 35,100,000.00 USD | 0.00 USD | 1,010,000.00 USD |
| `1D` | `2175.10` | 406,060,000.00 USD | 0.00 USD | 406,060,000.00 USD | 5,740,000.00 USD | 0.00 USD | 2,380,000.00 USD |
| `7D` | `2176.70` | 428,160,000.00 USD | 0.00 USD | 428,160,000.00 USD | 0.00 USD | 1,460,000.00 USD | 2,820,000.00 USD |
| `1D` | `2177.60` | 397,940,000.00 USD | 0.00 USD | 397,940,000.00 USD | 920,620.00 USD | 869,570.00 USD | 3,360,000.00 USD |
| `7D` | `2179.50` | 423,880,000.00 USD | 0.00 USD | 423,880,000.00 USD | 2,400,000.00 USD | 133,210.00 USD | 4,150,000.00 USD |
| `1D` | `2180.10` | 392,790,000.00 USD | 0.00 USD | 392,790,000.00 USD | 6,340,000.00 USD | 5,030,000.00 USD | 6,660,000.00 USD |
| `7D` | `2182.30` | 417,190,000.00 USD | 0.00 USD | 417,190,000.00 USD | 1,760,000.00 USD | 2,160,000.00 USD | 2,770,000.00 USD |
| `1D` | `2182.60` | 374,760,000.00 USD | 0.00 USD | 374,760,000.00 USD | 2,210,000.00 USD | 2,710,000.00 USD | 4,040,000.00 USD |
| `1D` | `2185.10` | 365,790,000.00 USD | 0.00 USD | 365,790,000.00 USD | 3,730,000.00 USD | 2,560,000.00 USD | 5,600,000.00 USD |
| `7D` | `2185.10` | 410,500,000.00 USD | 0.00 USD | 410,500,000.00 USD | 41,350,000.00 USD | 20,450,000.00 USD | 3,070,000.00 USD |
| `1D` | `2187.60` | 353,890,000.00 USD | 0.00 USD | 353,890,000.00 USD | 5,040,000.00 USD | 4,480,000.00 USD | 6,890,000.00 USD |
| `7D` | `2187.90` | 345,640,000.00 USD | 0.00 USD | 345,640,000.00 USD | 2,370,000.00 USD | 0.00 USD | 1,730,000.00 USD |
| `1D` | `2190.10` | 337,480,000.00 USD | 0.00 USD | 337,480,000.00 USD | 8,990,000.00 USD | 4,160,000.00 USD | 6,930,000.00 USD |
| `7D` | `2190.70` | 341,540,000.00 USD | 0.00 USD | 341,540,000.00 USD | 12,430,000.00 USD | 27,960,000.00 USD | 6,420,000.00 USD |
| `1D` | `2192.60` | 317,400,000.00 USD | 0.00 USD | 317,400,000.00 USD | 5,000,000.00 USD | 5,340,000.00 USD | 1,290,000.00 USD |
| `7D` | `2193.50` | 294,720,000.00 USD | 0.00 USD | 294,720,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,120,000.00 USD |
| `1D` | `2195.10` | 305,770,000.00 USD | 0.00 USD | 305,770,000.00 USD | 6,730,000.00 USD | 3,350,000.00 USD | 5,950,000.00 USD |
| `7D` | `2196.30` | 279,260,000.00 USD | 0.00 USD | 279,260,000.00 USD | 694,220.00 USD | 243,760.00 USD | 109,160.00 USD |
| `1D` | `2197.60` | 289,740,000.00 USD | 0.00 USD | 289,740,000.00 USD | 10,200,000.00 USD | 3,830,000.00 USD | 5,010,000.00 USD |
| `7D` | `2199.10` | 278,210,000.00 USD | 0.00 USD | 278,210,000.00 USD | 5,090,000.00 USD | 5,270,000.00 USD | 7,510,000.00 USD |
| `1D` | `2200.10` | 270,690,000.00 USD | 0.00 USD | 270,690,000.00 USD | 10,980,000.00 USD | 10,470,000.00 USD | 10,900,000.00 USD |
| `7D` | `2201.90` | 260,350,000.00 USD | 0.00 USD | 260,350,000.00 USD | 13,210,000.00 USD | 6,520,000.00 USD | 21,720,000.00 USD |
| `1D` | `2202.60` | 238,330,000.00 USD | 0.00 USD | 238,330,000.00 USD | 19,040,000.00 USD | 14,300,000.00 USD | 17,770,000.00 USD |
| `7D` | `2204.70` | 218,910,000.00 USD | 0.00 USD | 218,910,000.00 USD | 5,350,000.00 USD | 4,330,000.00 USD | 4,660,000.00 USD |
| `1D` | `2205.10` | 187,220,000.00 USD | 0.00 USD | 187,220,000.00 USD | 11,730,000.00 USD | 7,020,000.00 USD | 4,880,000.00 USD |
| `7D` | `2207.50` | 204,570,000.00 USD | 0.00 USD | 204,570,000.00 USD | 19,630,000.00 USD | 3,390,000.00 USD | 7,200,000.00 USD |
| `1D` | `2207.60` | 163,590,000.00 USD | 0.00 USD | 163,590,000.00 USD | 13,820,000.00 USD | 6,420,000.00 USD | 5,600,000.00 USD |
| `1D` | `2210.10` | 137,760,000.00 USD | 0.00 USD | 137,760,000.00 USD | 4,040,000.00 USD | 7,220,000.00 USD | 6,410,000.00 USD |
| `7D` | `2210.30` | 174,360,000.00 USD | 0.00 USD | 174,360,000.00 USD | 4,740,000.00 USD | 0.00 USD | 11,560,000.00 USD |
| `1D` | `2212.60` | 120,100,000.00 USD | 0.00 USD | 120,100,000.00 USD | 12,700,000.00 USD | 6,410,000.00 USD | 1,990,000.00 USD |
| `7D` | `2213.10` | 158,050,000.00 USD | 0.00 USD | 158,050,000.00 USD | 1,710,000.00 USD | 1,980,000.00 USD | 8,850,000.00 USD |
| `1D` | `2215.10` | 98,990,000.00 USD | 0.00 USD | 98,990,000.00 USD | 2,300,000.00 USD | 2,930,000.00 USD | 280,820.00 USD |
| `7D` | `2215.90` | 145,510,000.00 USD | 0.00 USD | 145,510,000.00 USD | 0.00 USD | 0.00 USD | 565,690.00 USD |
| `1D` | `2217.60` | 93,480,000.00 USD | 0.00 USD | 93,480,000.00 USD | 2,810,000.00 USD | 4,440,000.00 USD | 3,930,000.00 USD |
| `7D` | `2218.70` | 144,950,000.00 USD | 0.00 USD | 144,950,000.00 USD | 23,020,000.00 USD | 487,520.00 USD | 218,310.00 USD |
| `1D` | `2220.10` | 82,300,000.00 USD | 0.00 USD | 82,300,000.00 USD | 17,480,000.00 USD | 7,250,000.00 USD | 4,210,000.00 USD |
| `7D` | `2221.50` | 121,220,000.00 USD | 0.00 USD | 121,220,000.00 USD | 10,170,000.00 USD | 19,850,000.00 USD | 19,000,000.00 USD |
| `1D` | `2222.60` | 53,360,000.00 USD | 0.00 USD | 53,360,000.00 USD | 8,350,000.00 USD | 14,430,000.00 USD | 1,640,000.00 USD |
| `7D` | `2224.30` | 72,200,000.00 USD | 0.00 USD | 72,200,000.00 USD | 8,200,000.00 USD | 12,510,000.00 USD | 6,530,000.00 USD |
| `1D` | `2225.10` | 28,940,000.00 USD | 0.00 USD | 28,940,000.00 USD | 5,440,000.00 USD | 2,560,000.00 USD | 3,260,000.00 USD |
| `7D` | `2227.10` | 44,970,000.00 USD | 0.00 USD | 44,970,000.00 USD | 557,870.00 USD | 0.00 USD | 6,860,000.00 USD |
| `1D` | `2227.60` | 17,670,000.00 USD | 0.00 USD | 17,670,000.00 USD | 2,850,000.00 USD | 0.00 USD | 111,560.00 USD |
| `7D` | `2229.90` | 37,550,000.00 USD | 0.00 USD | 37,550,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2230.10` | 14,720,000.00 USD | 0.00 USD | 14,720,000.00 USD | 0.00 USD | 0.00 USD | 113,200.00 USD |
| `1D` | `2232.60` | 14,600,000.00 USD | 0.00 USD | 14,600,000.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2235.50` | 35,640,000.00 USD | 0.00 USD | 35,640,000.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 0.00 USD |
| `1D` | `2237.60` | 8,650,000.00 USD | 0.00 USD | 8,650,000.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2238.30` | 10,750,000.00 USD | 0.00 USD | 10,750,000.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2240.10` | 649,520.00 USD | 0.00 USD | 649,520.00 USD | 0.00 USD | 0.00 USD | 21,970.00 USD |
| `1D` | `2242.60` | 627,550.00 USD | 0.00 USD | 627,550.00 USD | 0.00 USD | 0.00 USD | 22,480.00 USD |
| `7D` | `2243.90` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 0.00 USD | 268,650.00 USD | 0.00 USD |
| `1D` | `2245.10` | 605,070.00 USD | 0.00 USD | 605,070.00 USD | 0.00 USD | 0.00 USD | 62,250.00 USD |
| `7D` | `2246.70` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 0.00 USD | 1,300,000.00 USD | 709,510.00 USD |
| `7D` | `2247.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2247.60` | 542,830.00 USD | 0.00 USD | 542,830.00 USD | 0.00 USD | 243,170.00 USD | 299,650.00 USD |
| `1D` | `2248.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2249.50` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 861,640.00 USD | 2,660,000.00 USD | 867,440.00 USD |
| `1D` | `2250.10` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 255,300.00 USD | 446,930.00 USD | 1,680,000.00 USD |
| `7D` | `2252.30` | 29,660,000.00 USD | 29,660,000.00 USD | 0.00 USD | 10,050,000.00 USD | 11,670,000.00 USD | 3,550,000.00 USD |
| `1D` | `2252.60` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 1,470,000.00 USD | 3,300,000.00 USD | 3,430,000.00 USD |
| `1D` | `2255.10` | 35,630,000.00 USD | 35,630,000.00 USD | 0.00 USD | 12,360,000.00 USD | 6,830,000.00 USD | 5,870,000.00 USD |
| `7D` | `2255.10` | 47,080,000.00 USD | 47,080,000.00 USD | 0.00 USD | 10,050,000.00 USD | 6,600,000.00 USD | 774,210.00 USD |
| `1D` | `2257.60` | 69,780,000.00 USD | 69,780,000.00 USD | 0.00 USD | 19,980,000.00 USD | 8,290,000.00 USD | 5,870,000.00 USD |
| `7D` | `2257.90` | 86,780,000.00 USD | 86,780,000.00 USD | 0.00 USD | 20,510,000.00 USD | 12,290,000.00 USD | 6,890,000.00 USD |
| `1D` | `2260.10` | 91,850,000.00 USD | 91,850,000.00 USD | 0.00 USD | 9,050,000.00 USD | 10,340,000.00 USD | 2,680,000.00 USD |
| `7D` | `2260.70` | 91,100,000.00 USD | 91,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,320,000.00 USD |
| `1D` | `2262.60` | 120,240,000.00 USD | 120,240,000.00 USD | 0.00 USD | 15,390,000.00 USD | 6,760,000.00 USD | 6,230,000.00 USD |
| `7D` | `2263.50` | 100,120,000.00 USD | 100,120,000.00 USD | 0.00 USD | 7,340,000.00 USD | 1,460,000.00 USD | 218,310.00 USD |
| `1D` | `2265.10` | 166,340,000.00 USD | 166,340,000.00 USD | 0.00 USD | 19,500,000.00 USD | 16,750,000.00 USD | 9,850,000.00 USD |
| `7D` | `2266.30` | 132,540,000.00 USD | 132,540,000.00 USD | 0.00 USD | 10,170,000.00 USD | 15,790,000.00 USD | 6,460,000.00 USD |
| `1D` | `2267.60` | 222,280,000.00 USD | 222,280,000.00 USD | 0.00 USD | 20,700,000.00 USD | 22,510,000.00 USD | 12,730,000.00 USD |
| `7D` | `2269.10` | 188,720,000.00 USD | 188,720,000.00 USD | 0.00 USD | 19,210,000.00 USD | 12,640,000.00 USD | 24,330,000.00 USD |
| `1D` | `2270.10` | 281,760,000.00 USD | 281,760,000.00 USD | 0.00 USD | 23,390,000.00 USD | 12,160,000.00 USD | 23,930,000.00 USD |
| `7D` | `2271.90` | 217,620,000.00 USD | 217,620,000.00 USD | 0.00 USD | 18,240,000.00 USD | 3,640,000.00 USD | 7,010,000.00 USD |
| `1D` | `2272.60` | 312,680,000.00 USD | 312,680,000.00 USD | 0.00 USD | 19,020,000.00 USD | 5,610,000.00 USD | 6,290,000.00 USD |
| `7D` | `2274.70` | 245,920,000.00 USD | 245,920,000.00 USD | 0.00 USD | 19,630,000.00 USD | 6,900,000.00 USD | 1,770,000.00 USD |
| `1D` | `2275.10` | 360,200,000.00 USD | 360,200,000.00 USD | 0.00 USD | 27,310,000.00 USD | 15,610,000.00 USD | 4,600,000.00 USD |
| `7D` | `2277.50` | 272,300,000.00 USD | 272,300,000.00 USD | 0.00 USD | 6,890,000.00 USD | 8,890,000.00 USD | 10,610,000.00 USD |
| `1D` | `2277.60` | 397,830,000.00 USD | 397,830,000.00 USD | 0.00 USD | 10,430,000.00 USD | 15,200,000.00 USD | 11,990,000.00 USD |
| `1D` | `2280.10` | 446,320,000.00 USD | 446,320,000.00 USD | 0.00 USD | 26,670,000.00 USD | 9,750,000.00 USD | 12,070,000.00 USD |
| `7D` | `2280.30` | 316,620,000.00 USD | 316,620,000.00 USD | 0.00 USD | 854,200.00 USD | 39,830,000.00 USD | 3,640,000.00 USD |
| `1D` | `2282.60` | 500,850,000.00 USD | 500,850,000.00 USD | 0.00 USD | 22,560,000.00 USD | 24,830,000.00 USD | 7,150,000.00 USD |
| `7D` | `2283.10` | 408,440,000.00 USD | 408,440,000.00 USD | 0.00 USD | 5,600,000.00 USD | 72,520,000.00 USD | 13,690,000.00 USD |
| `1D` | `2285.10` | 528,700,000.00 USD | 528,700,000.00 USD | 0.00 USD | 11,520,000.00 USD | 9,410,000.00 USD | 6,920,000.00 USD |
| `7D` | `2285.90` | 412,450,000.00 USD | 412,450,000.00 USD | 0.00 USD | 1,320,000.00 USD | 2,590,000.00 USD | 109,160.00 USD |
| `1D` | `2287.60` | 567,910,000.00 USD | 567,910,000.00 USD | 0.00 USD | 19,470,000.00 USD | 11,060,000.00 USD | 8,670,000.00 USD |
| `7D` | `2288.70` | 454,050,000.00 USD | 454,050,000.00 USD | 0.00 USD | 13,470,000.00 USD | 13,140,000.00 USD | 15,000,000.00 USD |
| `1D` | `2290.10` | 613,830,000.00 USD | 613,830,000.00 USD | 0.00 USD | 19,770,000.00 USD | 21,020,000.00 USD | 5,130,000.00 USD |
| `7D` | `2291.50` | 479,370,000.00 USD | 479,370,000.00 USD | 0.00 USD | 8,400,000.00 USD | 6,770,000.00 USD | 10,140,000.00 USD |
| `1D` | `2292.60` | 647,810,000.00 USD | 647,810,000.00 USD | 0.00 USD | 17,860,000.00 USD | 4,710,000.00 USD | 11,420,000.00 USD |
| `7D` | `2294.30` | 500,700,000.00 USD | 500,700,000.00 USD | 0.00 USD | 14,670,000.00 USD | 1,490,000.00 USD | 5,180,000.00 USD |
| `1D` | `2295.10` | 684,420,000.00 USD | 684,420,000.00 USD | 0.00 USD | 12,280,000.00 USD | 13,600,000.00 USD | 10,720,000.00 USD |
| `7D` | `2297.10` | 550,450,000.00 USD | 550,450,000.00 USD | 0.00 USD | 25,900,000.00 USD | 8,070,000.00 USD | 15,780,000.00 USD |
| `1D` | `2297.60` | 730,750,000.00 USD | 730,750,000.00 USD | 0.00 USD | 29,190,000.00 USD | 11,160,000.00 USD | 5,980,000.00 USD |
| `7D` | `2299.90` | 593,370,000.00 USD | 593,370,000.00 USD | 0.00 USD | 16,200,000.00 USD | 20,940,000.00 USD | 5,780,000.00 USD |
| `1D` | `2300.10` | 770,270,000.00 USD | 770,270,000.00 USD | 0.00 USD | 11,250,000.00 USD | 14,710,000.00 USD | 13,570,000.00 USD |
| `1D` | `2302.60` | 797,870,000.00 USD | 797,870,000.00 USD | 0.00 USD | 16,060,000.00 USD | 2,700,000.00 USD | 8,840,000.00 USD |
| `7D` | `2302.70` | 648,040,000.00 USD | 648,040,000.00 USD | 0.00 USD | 26,960,000.00 USD | 10,860,000.00 USD | 16,850,000.00 USD |
| `1D` | `2305.10` | 836,610,000.00 USD | 836,610,000.00 USD | 0.00 USD | 14,970,000.00 USD | 17,660,000.00 USD | 6,110,000.00 USD |
| `7D` | `2305.50` | 674,050,000.00 USD | 674,050,000.00 USD | 0.00 USD | 6,340,000.00 USD | 8,820,000.00 USD | 10,860,000.00 USD |
| `1D` | `2307.60` | 847,900,000.00 USD | 847,900,000.00 USD | 0.00 USD | 4,390,000.00 USD | 3,680,000.00 USD | 3,230,000.00 USD |
| `7D` | `2308.30` | 676,350,000.00 USD | 676,350,000.00 USD | 0.00 USD | 1,240,000.00 USD | 930,630.00 USD | 134,160.00 USD |
| `1D` | `2310.10` | 866,410,000.00 USD | 866,410,000.00 USD | 0.00 USD | 4,990,000.00 USD | 2,820,000.00 USD | 10,690,000.00 USD |
| `7D` | `2311.10` | 706,850,000.00 USD | 706,850,000.00 USD | 0.00 USD | 11,560,000.00 USD | 2,790,000.00 USD | 16,150,000.00 USD |
| `1D` | `2312.60` | 882,980,000.00 USD | 882,980,000.00 USD | 0.00 USD | 6,950,000.00 USD | 8,040,000.00 USD | 1,590,000.00 USD |
| `7D` | `2313.90` | 717,670,000.00 USD | 717,670,000.00 USD | 0.00 USD | 1,100,000.00 USD | 7,460,000.00 USD | 2,260,000.00 USD |
| `1D` | `2315.10` | 905,530,000.00 USD | 905,530,000.00 USD | 0.00 USD | 5,980,000.00 USD | 13,500,000.00 USD | 3,070,000.00 USD |
| `7D` | `2316.70` | 723,430,000.00 USD | 723,430,000.00 USD | 0.00 USD | 1,020,000.00 USD | 3,640,000.00 USD | 1,090,000.00 USD |
| `1D` | `2317.60` | 932,690,000.00 USD | 932,690,000.00 USD | 0.00 USD | 8,220,000.00 USD | 10,500,000.00 USD | 8,440,000.00 USD |
| `7D` | `2319.50` | 753,590,000.00 USD | 753,590,000.00 USD | 0.00 USD | 5,530,000.00 USD | 15,850,000.00 USD | 8,780,000.00 USD |
| `1D` | `2320.10` | 958,540,000.00 USD | 958,540,000.00 USD | 0.00 USD | 10,150,000.00 USD | 12,260,000.00 USD | 3,450,000.00 USD |
| `7D` | `2322.30` | 759,510,000.00 USD | 759,510,000.00 USD | 0.00 USD | 2,300,000.00 USD | 3,450,000.00 USD | 172,940.00 USD |
| `1D` | `2322.60` | 976,490,000.00 USD | 976,490,000.00 USD | 0.00 USD | 3,370,000.00 USD | 9,320,000.00 USD | 5,260,000.00 USD |
| `1D` | `2325.10` | 990,410,000.00 USD | 990,410,000.00 USD | 0.00 USD | 3,060,000.00 USD | 9,360,000.00 USD | 1,500,000.00 USD |
| `7D` | `2325.10` | 782,540,000.00 USD | 782,540,000.00 USD | 0.00 USD | 10,150,000.00 USD | 2,770,000.00 USD | 10,120,000.00 USD |
| `1D` | `2327.60` | 996,970,000.00 USD | 996,970,000.00 USD | 0.00 USD | 553,100.00 USD | 1,410,000.00 USD | 4,590,000.00 USD |
| `7D` | `2327.90` | 794,430,000.00 USD | 794,430,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 8,030,000.00 USD |
| `1D` | `2330.10` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 11,750,000.00 USD | 3,450,000.00 USD | 1,250,000.00 USD |
| `7D` | `2330.70` | 810,810,000.00 USD | 810,810,000.00 USD | 0.00 USD | 15,960,000.00 USD | 363,770.00 USD | 54,580.00 USD |
| `1D` | `2332.60` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 5,020,000.00 USD | 3,500,000.00 USD | 6,310,000.00 USD |
| `7D` | `2333.50` | 856,150,000.00 USD | 856,150,000.00 USD | 0.00 USD | 22,570,000.00 USD | 14,770,000.00 USD | 7,990,000.00 USD |
| `1D` | `2335.10` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 11,180,000.00 USD | 7,590,000.00 USD | 5,870,000.00 USD |
| `7D` | `2336.30` | 900,360,000.00 USD | 900,360,000.00 USD | 0.00 USD | 26,590,000.00 USD | 10,690,000.00 USD | 6,930,000.00 USD |
| `1D` | `2337.60` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 14,050,000.00 USD | 1,830,000.00 USD | 6,590,000.00 USD |
| `7D` | `2339.10` | 926,760,000.00 USD | 926,760,000.00 USD | 0.00 USD | 14,040,000.00 USD | 0.00 USD | 12,370,000.00 USD |
| `1D` | `2340.10` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 11,670,000.00 USD | 6,260,000.00 USD | 12,150,000.00 USD |
| `7D` | `2341.90` | 967,190,000.00 USD | 967,190,000.00 USD | 0.00 USD | 8,610,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD |
| `1D` | `2342.60` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 8,670,000.00 USD | 4,470,000.00 USD | 2,450,000.00 USD |
| `7D` | `2344.70` | 995,110,000.00 USD | 995,110,000.00 USD | 0.00 USD | 2,480,000.00 USD | 16,920,000.00 USD | 8,520,000.00 USD |
| `1D` | `2345.10` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 5,430,000.00 USD | 8,130,000.00 USD | 8,300,000.00 USD |
| `7D` | `2347.50` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 0.00 USD | 8,220,000.00 USD | 18,860,000.00 USD |
| `1D` | `2347.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 1,960,000.00 USD | 3,520,000.00 USD | 2,590,000.00 USD |
| `1D` | `2350.10` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 23,260,000.00 USD | 6,880,000.00 USD | 10,080,000.00 USD |
| `7D` | `2350.30` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 1,630,000.00 USD | 20,110,000.00 USD | 15,150,000.00 USD |
| `1D` | `2352.60` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 5,150,000.00 USD | 3,400,000.00 USD | 2,670,000.00 USD |
| `7D` | `2353.10` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 2,710,000.00 USD | 35,770,000.00 USD | 4,640,000.00 USD |
| `1D` | `2355.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 2,320,000.00 USD | 3,770,000.00 USD | 951,670.00 USD |
| `7D` | `2355.90` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 18,560,000.00 USD | 10,720,000.00 USD | 3,950,000.00 USD |
| `1D` | `2357.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 3,780,000.00 USD | 4,290,000.00 USD | 3,440,000.00 USD |
| `7D` | `2358.70` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 6,870,000.00 USD | 512,220.00 USD | 3,190,000.00 USD |
| `1D` | `2360.10` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 9,090,000.00 USD | 4,260,000.00 USD | 5,450,000.00 USD |
| `7D` | `2361.50` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,430,000.00 USD | 374,770.00 USD |
| `1D` | `2362.60` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 8,700,000.00 USD | 6,710,000.00 USD | 7,910,000.00 USD |
| `7D` | `2364.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 3,860,000.00 USD | 373,740.00 USD | 10,920,000.00 USD |
| `1D` | `2365.10` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 4,830,000.00 USD | 3,010,000.00 USD | 3,660,000.00 USD |
| `7D` | `2367.10` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 307,410.00 USD |
| `1D` | `2367.60` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 2,910,000.00 USD | 1,110,000.00 USD | 1,910,000.00 USD |
| `7D` | `2369.90` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 24,940,000.00 USD | 475,460.00 USD | 18,790,000.00 USD |
| `1D` | `2370.10` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 0.00 USD | 10,250,000.00 USD | 7,700,000.00 USD | 4,930,000.00 USD |
| `1D` | `2372.60` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 11,280,000.00 USD | 1,790,000.00 USD | 4,460,000.00 USD |
| `7D` | `2372.70` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 15,600,000.00 USD | 0.00 USD | 39,640,000.00 USD |
| `1D` | `2375.10` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 5,700,000.00 USD | 557,400.00 USD | 1,840,000.00 USD |
| `7D` | `2375.50` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 0.00 USD | 9,700,000.00 USD | 1,050,000.00 USD | 11,870,000.00 USD |
| `1D` | `2377.60` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 3,340,000.00 USD | 3,070,000.00 USD | 4,510,000.00 USD |
| `7D` | `2378.30` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 11,180,000.00 USD | 7,020,000.00 USD | 23,870,000.00 USD |
| `1D` | `2380.10` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 6,310,000.00 USD | 389,290.00 USD | 4,780,000.00 USD |
| `7D` | `2381.10` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 2,390,000.00 USD | 16,460,000.00 USD |
| `1D` | `2382.60` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 15,650,000.00 USD | 14,510,000.00 USD | 11,550,000.00 USD |
| `7D` | `2383.90` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 8,840,000.00 USD | 21,750,000.00 USD | 30,520,000.00 USD |
| `1D` | `2385.10` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 7,540,000.00 USD | 11,520,000.00 USD | 4,750,000.00 USD |
| `7D` | `2386.70` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 0.00 USD | 17,720,000.00 USD | 32,140,000.00 USD | 42,040,000.00 USD |
| `1D` | `2387.60` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 9,850,000.00 USD | 5,970,000.00 USD | 3,120,000.00 USD |
| `7D` | `2389.50` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 5,670,000.00 USD | 35,860,000.00 USD | 28,760,000.00 USD |
| `1D` | `2390.10` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 4,390,000.00 USD | 3,310,000.00 USD | 1,520,000.00 USD |
| `7D` | `2392.30` | 1,700,000,000.00 USD | 1,700,000,000.00 USD | 0.00 USD | 26,840,000.00 USD | 45,530,000.00 USD | 39,160,000.00 USD |
| `1D` | `2392.60` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,660,000.00 USD | 3,320,000.00 USD |
| `1D` | `2395.10` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,830,000.00 USD | 2,170,000.00 USD |
| `7D` | `2395.10` | 1,790,000,000.00 USD | 1,790,000,000.00 USD | 0.00 USD | 39,180,000.00 USD | 24,870,000.00 USD | 29,410,000.00 USD |
| `1D` | `2397.60` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 64,150.00 USD | 3,720,000.00 USD | 3,400,000.00 USD |
| `7D` | `2397.90` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 0.00 USD | 34,290,000.00 USD | 36,430,000.00 USD | 23,570,000.00 USD |
| `1D` | `2400.10` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 2,150,000.00 USD | 637,690.00 USD | 1,390,000.00 USD |
| `7D` | `2400.70` | 1,980,000,000.00 USD | 1,980,000,000.00 USD | 0.00 USD | 42,030,000.00 USD | 25,390,000.00 USD | 24,070,000.00 USD |
| `1D` | `2402.60` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 1,140,000.00 USD | 315,710.00 USD | 552,090.00 USD |
| `7D` | `2403.50` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 0.00 USD | 51,300,000.00 USD | 24,760,000.00 USD | 30,980,000.00 USD |
| `1D` | `2405.10` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 0.00 USD | 5,960,000.00 USD | 3,440,000.00 USD | 4,950,000.00 USD |
| `7D` | `2406.30` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 29,700,000.00 USD | 33,710,000.00 USD | 14,210,000.00 USD |
| `1D` | `2407.60` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 0.00 USD | 6,810,000.00 USD | 3,500,000.00 USD | 1,910,000.00 USD |
| `7D` | `2409.10` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 25,090,000.00 USD | 21,480,000.00 USD | 27,910,000.00 USD |
| `1D` | `2410.10` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 0.00 USD | 4,520,000.00 USD | 3,540,000.00 USD | 3,330,000.00 USD |
| `7D` | `2411.90` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 15,970,000.00 USD | 21,640,000.00 USD | 13,990,000.00 USD |
| `1D` | `2412.60` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 0.00 USD | 4,850,000.00 USD | 2,970,000.00 USD | 1,430,000.00 USD |
| `7D` | `2414.70` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 22,250,000.00 USD | 19,630,000.00 USD | 21,720,000.00 USD |
| `1D` | `2415.10` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 2,080,000.00 USD | 1,890,000.00 USD | 2,560,000.00 USD |
| `7D` | `2417.50` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 0.00 USD | 22,310,000.00 USD | 8,700,000.00 USD | 21,160,000.00 USD |
| `1D` | `2417.60` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 2,060,000.00 USD | 1,260,000.00 USD | 599,960.00 USD |
| `1D` | `2420.10` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 0.00 USD | 5,060,000.00 USD | 2,860,000.00 USD | 2,950,000.00 USD |
| `7D` | `2420.30` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 0.00 USD | 29,980,000.00 USD | 18,780,000.00 USD | 9,160,000.00 USD |
| `1D` | `2422.60` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 693,410.00 USD | 2,620,000.00 USD | 3,180,000.00 USD |
| `7D` | `2423.10` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 0.00 USD | 17,920,000.00 USD | 17,260,000.00 USD | 17,780,000.00 USD |
| `1D` | `2425.10` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 510,650.00 USD | 623,850.00 USD | 888,640.00 USD |
| `7D` | `2425.90` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 0.00 USD | 12,980,000.00 USD | 15,010,000.00 USD | 17,380,000.00 USD |
| `1D` | `2427.60` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 2,250,000.00 USD | 1,520,000.00 USD | 603,040.00 USD |
| `7D` | `2428.70` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 0.00 USD | 12,800,000.00 USD | 7,090,000.00 USD | 8,840,000.00 USD |
| `1D` | `2430.10` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,550,000.00 USD | 1,350,000.00 USD |
| `7D` | `2431.50` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 0.00 USD | 9,420,000.00 USD | 12,660,000.00 USD | 8,250,000.00 USD |
| `1D` | `2432.60` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 2,770,000.00 USD | 2,230,000.00 USD | 691,800.00 USD |
| `7D` | `2434.30` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 8,200,000.00 USD | 3,830,000.00 USD | 3,220,000.00 USD |
| `1D` | `2435.10` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 2,480,000.00 USD | 559,660.00 USD | 1,370,000.00 USD |
| `7D` | `2437.10` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 7,130,000.00 USD | 7,440,000.00 USD | 6,120,000.00 USD |
| `1D` | `2437.60` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 1,360,000.00 USD | 1,040,000.00 USD | 30,250.00 USD |
| `7D` | `2439.90` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 12,730,000.00 USD | 4,970,000.00 USD | 3,700,000.00 USD |
| `1D` | `2440.10` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 1,240,000.00 USD | 502,040.00 USD | 304,820.00 USD |
| `1D` | `2442.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 1,040,000.00 USD | 743,640.00 USD | 827,820.00 USD |
| `7D` | `2442.70` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 5,050,000.00 USD | 5,320,000.00 USD | 7,900,000.00 USD |
| `1D` | `2445.10` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 218,020.00 USD | 703,990.00 USD | 1,240,000.00 USD |
| `7D` | `2445.50` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 0.00 USD | 9,990,000.00 USD | 7,470,000.00 USD | 10,400,000.00 USD |
| `1D` | `2447.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 751,450.00 USD | 1,860,000.00 USD |
| `7D` | `2448.30` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 0.00 USD | 10,750,000.00 USD | 3,620,000.00 USD | 13,290,000.00 USD |
| `1D` | `2450.10` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 627,630.00 USD | 311,480.00 USD | 35,990.00 USD |
| `7D` | `2451.10` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 8,450,000.00 USD | 7,240,000.00 USD | 7,080,000.00 USD |
| `1D` | `2452.60` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 3,200,000.00 USD | 1,840,000.00 USD | 2,450,000.00 USD |
| `7D` | `2453.90` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 4,220,000.00 USD | 2,980,000.00 USD | 3,970,000.00 USD |
| `1D` | `2455.10` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 2,270,000.00 USD | 1,990,000.00 USD | 994,080.00 USD |
| `7D` | `2456.70` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 5,900,000.00 USD | 7,380,000.00 USD | 7,530,000.00 USD |
| `1D` | `2457.60` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 1,770,000.00 USD | 1,980,000.00 USD | 845,630.00 USD |
| `7D` | `2459.50` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 3,220,000.00 USD | 4,870,000.00 USD | 6,000,000.00 USD |
| `1D` | `2460.10` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 1,530,000.00 USD | 1,370,000.00 USD | 388,420.00 USD |
| `7D` | `2462.30` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 6,600,000.00 USD | 5,990,000.00 USD | 5,150,000.00 USD |
| `1D` | `2462.60` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 413,060.00 USD | 629,460.00 USD | 851,570.00 USD |
| `1D` | `2465.10` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 1,050,000.00 USD | 525,020.00 USD |
| `7D` | `2465.10` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 4,960,000.00 USD | 3,130,000.00 USD | 2,820,000.00 USD |
| `1D` | `2467.60` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 1,140,000.00 USD | 1,580,000.00 USD | 391,980.00 USD |
| `7D` | `2467.90` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 3,830,000.00 USD | 2,330,000.00 USD | 23,760.00 USD |
| `1D` | `2470.10` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 1,440,000.00 USD | 2,220,000.00 USD | 1,670,000.00 USD |
| `7D` | `2470.70` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 0.00 USD | 4,870,000.00 USD | 3,000,000.00 USD | 1,140,000.00 USD |
| `1D` | `2472.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 653,960.00 USD | 275,370.00 USD | 1,160,000.00 USD |
| `7D` | `2473.50` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 5,300,000.00 USD | 2,920,000.00 USD | 3,180,000.00 USD |
| `1D` | `2475.10` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 595,510.00 USD | 914,780.00 USD | 231,680.00 USD |
| `7D` | `2476.30` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 2,070,000.00 USD | 1,710,000.00 USD | 872,130.00 USD |
| `1D` | `2477.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 2,200,000.00 USD | 405,410.00 USD | 156,140.00 USD |
| `7D` | `2479.10` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 3,070,000.00 USD | 4,130,000.00 USD | 540,990.00 USD |
| `1D` | `2480.10` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 567,450.00 USD | 943,540.00 USD | 731,890.00 USD |
| `7D` | `2481.90` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 601,420.00 USD | 3,680,000.00 USD | 1,050,000.00 USD |
| `7D` | `2484.70` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD |
| `7D` | `2487.50` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD |
| `7D` | `2490.30` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 338,890.00 USD | 286,610.00 USD | 0.00 USD |
| `7D` | `2491.80` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 2,580,000.00 USD | 733,870.00 USD | 445,140.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `28.68B` | Total OI Tokens: `12,782,394.1 ETH`
  * 1h OI Change: `+0.78%` | 4h OI Change: `-0.10%` | 24h OI Change: `-5.06%`
  * Exchange Breakdown: Binance=`8.49B` | Bybit=`2.11B` | OKX=`1.76B` | Hyperliquid=`2.32B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `99.81K` | Last 24h: `195.10K` | Last 3d: `5.21M` | Last 7d: `11.81M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0015%` | **USDT OKX** | `0.0015%` |
| **USDT Bybit** | `0.0018%` | **USDT KuCoin** | `-0.0023%` |
| **USDT MEXC** | `-0.0015%` | **USDT BingX** | `0.0052%` |
| **USDT Gate** | `0.0063%` | **USDT Bitget** | `0.0052%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0030%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `43.69%` | `56.31%` | `0.78` | 369,900,000.00 USD |
| `15M` | `Binance` | `39.66%` | `60.34%` | `0.66` | 117,690,000.00 USD |
| `15M` | `OKX` | `45.16%` | `54.84%` | `0.82` | 48,650,000.00 USD |
| `15M` | `Bybit` | `47.94%` | `52.06%` | `0.92` | 43,720,000.00 USD |
| `15M` | `KuCoin` | `27.83%` | `72.17%` | `0.39` | 3,230,000.00 USD |
| `15M` | `Gate` | `44.54%` | `55.46%` | `0.80` | 37,920,000.00 USD |
| `15M` | `Bitget` | `44.67%` | `55.33%` | `0.81` | 16,680,000.00 USD |
| `15M` | `BingX` | `39.66%` | `60.34%` | `0.66` | 6,250,000.00 USD |
| `15M` | `MEXC` | `44.9%` | `55.1%` | `0.81` | 19,050,000.00 USD |
| `15M` | `Bitunix` | `43.94%` | `56.06%` | `0.78` | 15,450,000.00 USD |
| `15M` | `Hyperliquid` | `67.77%` | `32.23%` | `2.10` | 11,020,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.77%` | `49.23%` | `1.03` | 5,200,000.00 USD |
| `15M` | `Crypto.com` | `60.6%` | `39.4%` | `1.54` | 1,910,000.00 USD |
| `15M` | `WhiteBIT` | `0.08%` | `99.92%` | `0.00` | 4,220,000.00 USD |
| `15M` | `HTX` | `42.72%` | `57.28%` | `0.75` | 1,780,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `49.39%` | `50.61%` | `0.98` | 21,020,000.00 USD |
| `15M` | `Bitfinex` | `48.18%` | `51.82%` | `0.93` | 611,040.00 USD |
| `15M` | `Kraken` | `39.13%` | `60.87%` | `0.64` | 3,810,000.00 USD |
| `15M` | `Aster` | `33.84%` | `66.16%` | `0.51` | 7,620,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `53.41%` | `46.59%` | `1.15` | 4,080,000.00 USD |
| `15M` | `Whale Positions` | `39.66%` | `60.34%` | `0.66` | 117,690,000.00 USD |
| `15M` | `Global Accounts` | `43.69%` | `56.31%` | `0.78` | 369,900,000.00 USD |
| `1H` | `ETH` | `52.85%` | `47.15%` | `1.12` | 2,350,000,000.00 USD |
| `1H` | `Binance` | `50.09%` | `49.91%` | `1.00` | 769,630,000.00 USD |
| `1H` | `OKX` | `57.28%` | `42.72%` | `1.34` | 315,020,000.00 USD |
| `1H` | `Bybit` | `54.95%` | `45.05%` | `1.22` | 252,410,000.00 USD |
| `1H` | `KuCoin` | `43.95%` | `56.05%` | `0.78` | 5,190,000.00 USD |
| `1H` | `Gate` | `49.05%` | `50.95%` | `0.96` | 281,920,000.00 USD |
| `1H` | `Bitget` | `52.27%` | `47.73%` | `1.10` | 98,380,000.00 USD |
| `1H` | `BingX` | `58.49%` | `41.51%` | `1.41` | 46,420,000.00 USD |
| `1H` | `MEXC` | `55.85%` | `44.15%` | `1.27` | 134,600,000.00 USD |
| `1H` | `Bitunix` | `56.51%` | `43.49%` | `1.30` | 97,340,000.00 USD |
| `1H` | `Hyperliquid` | `71.61%` | `28.39%` | `2.52` | 96,450,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `58.59%` | `41.41%` | `1.41` | 17,410,000.00 USD |
| `1H` | `Crypto.com` | `52.25%` | `47.75%` | `1.09` | 9,610,000.00 USD |
| `1H` | `WhiteBIT` | `38.84%` | `61.16%` | `0.64` | 9,890,000.00 USD |
| `1H` | `HTX` | `56.78%` | `43.22%` | `1.31` | 7,290,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `45.28%` | `54.72%` | `0.83` | 108,430,000.00 USD |
| `1H` | `Bitfinex` | `59.31%` | `40.69%` | `1.46` | 3,860,000.00 USD |
| `1H` | `Kraken` | `49.17%` | `50.83%` | `0.97` | 24,530,000.00 USD |
| `1H` | `Aster` | `44.1%` | `55.9%` | `0.79` | 40,330,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `45.47%` | `54.53%` | `0.83` | 25,800,000.00 USD |
| `1H` | `Whale Positions` | `50.09%` | `49.91%` | `1.00` | 769,630,000.00 USD |
| `1H` | `Global Accounts` | `52.85%` | `47.15%` | `1.12` | 2,350,000,000.00 USD |
| `4H` | `ETH` | `46.48%` | `53.52%` | `0.87` | 10,770,000,000.00 USD |
| `4H` | `Binance` | `44.28%` | `55.72%` | `0.79` | 3,140,000,000.00 USD |
| `4H` | `OKX` | `49.27%` | `50.73%` | `0.97` | 1,510,000,000.00 USD |
| `4H` | `Bybit` | `45.96%` | `54.04%` | `0.85` | 961,110,000.00 USD |
| `4H` | `KuCoin` | `51.59%` | `48.41%` | `1.07` | 29,620,000.00 USD |
| `4H` | `Gate` | `50.56%` | `49.44%` | `1.02` | 1,080,000,000.00 USD |
| `4H` | `Bitget` | `44.16%` | `55.84%` | `0.79` | 487,570,000.00 USD |
| `4H` | `BingX` | `49.63%` | `50.37%` | `0.99` | 203,000,000.00 USD |
| `4H` | `MEXC` | `46.77%` | `53.23%` | `0.88` | 515,790,000.00 USD |
| `4H` | `Bitunix` | `48.49%` | `51.51%` | `0.94` | 436,620,000.00 USD |
| `4H` | `Hyperliquid` | `43.64%` | `56.36%` | `0.77` | 619,770,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.38%` | `49.62%` | `1.02` | 693,970,000.00 USD |
| `4H` | `Crypto.com` | `47.15%` | `52.85%` | `0.89` | 37,350,000.00 USD |
| `4H` | `WhiteBIT` | `16.18%` | `83.82%` | `0.19` | 193,410,000.00 USD |
| `4H` | `HTX` | `44.94%` | `55.06%` | `0.82` | 36,960,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.43%` | `48.57%` | `1.06` | 515,160,000.00 USD |
| `4H` | `Bitfinex` | `50.22%` | `49.78%` | `1.01` | 8,360,000.00 USD |
| `4H` | `Kraken` | `47.61%` | `52.39%` | `0.91` | 71,120,000.00 USD |
| `4H` | `Aster` | `45.14%` | `54.86%` | `0.82` | 116,140,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.46%` | `48.54%` | `1.06` | 99,410,000.00 USD |
| `4H` | `Whale Positions` | `44.28%` | `55.72%` | `0.79` | 3,140,000,000.00 USD |
| `4H` | `Global Accounts` | `46.48%` | `53.52%` | `0.87` | 10,770,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `2222.75` | `2224.81` | `2222.75` | `2229.75` | `2221.25` | 65,855,959.19 USD | 30,261,207.11 USD | 35,594,752.09 USD | -5,333,544.98 USD | `-8.10%` | `0B / 4S` |
| `5:00 UTC` | `2221.75` | `2223.05` | `2221.75` | `2226.25` | `2220.25` | 71,858,619.15 USD | 38,686,757.89 USD | 33,171,861.26 USD | 5,514,896.63 USD | `+7.67%` | `0B / 0S` |
| `0:00 UTC` | `2229.25` | `2226.54` | `2229.25` | `2231.25` | `2220.25` | 81,297,282.61 USD | 40,950,851.56 USD | 40,346,431.05 USD | 604,420.51 USD | `+0.74%` | `0B / 2S` |
| `5:00 UTC` | `2227.25` | `2227.77` | `2227.25` | `2229.75` | `2226.25` | 53,422,952.94 USD | 29,109,463.85 USD | 24,313,489.09 USD | 4,795,974.76 USD | `+8.98%` | `1B / 0S` |
| `0:00 UTC` | `2223.75` | `2224.01` | `2223.75` | `2228.25` | `2221.75` | 56,423,190.50 USD | 27,667,054.76 USD | 28,756,135.74 USD | -1,089,080.98 USD | `-1.93%` | `0B / 3S` |
| `5:00 UTC` | `2222.25` | `2225.79` | `2222.25` | `2230.75` | `2220.25` | 60,731,653.97 USD | 32,744,113.06 USD | 27,987,540.91 USD | 4,756,572.15 USD | `+7.83%` | `4B / 1S` |
| `0:00 UTC` | `2245.25` | `2240.77` | `2245.25` | `2248.75` | `2228.25` | 194,501,635.59 USD | 112,910,472.81 USD | 81,591,162.78 USD | 31,319,310.03 USD | `+16.10%` | `7B / 0S` |
| `5:00 UTC` | `2241.25` | `2243.75` | `2241.25` | `2248.75` | `2240.25` | 86,877,812.25 USD | 38,844,351.80 USD | 48,033,460.45 USD | -9,189,108.64 USD | `-10.58%` | `1B / 1S` |
| `0:00 UTC` | `2245.75` | `2246.97` | `2245.75` | `2251.75` | `2242.75` | 72,367,813.73 USD | 32,722,639.42 USD | 39,645,174.31 USD | -6,922,534.89 USD | `-9.57%` | `2B / 1S` |
| `5:00 UTC` | `2242.75` | `2242.41` | `2242.75` | `2244.25` | `2240.75` | 15,895,607.30 USD | 5,986,338.35 USD | 9,909,268.95 USD | -3,922,930.60 USD | `-24.68%` | `0B / 2S` |

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
| `5m` | 112,350.00 USD | -17,890,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -2,220,000.00 USD | -36,640,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 1,990,000.00 USD | -33,620,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 15,490,000.00 USD | 63,240,000.00 USD | **`ACCUMULATION`** |
| `2h` | 5,050,000.00 USD | 79,150,000.00 USD | **`ACCUMULATION`** |
| `4h` | -17,530,000.00 USD | -33,830,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -3,570,000.00 USD | -52,110,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 5,590,000.00 USD | 120,980,000.00 USD | **`ACCUMULATION`** |
| `12h` | -58,000,000.00 USD | -616,230,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -143,360,000.00 USD | -1,870,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -219,440,000.00 USD | -3,020,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,180,000,000.00 USD | -9,720,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+112.35K` | 15m=`-2.22M` | 1h=`+15.49M` | 24h=`-143.36M`
* Futures Capital Netflows: 5m=`-17.89M` | 15m=`-36.64M` | 1h=`+63.24M` | 24h=`-1.87B`
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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `2177.46` (Risk Distance: `18.97` pts)
  * +2.5R Take Profit: `2243.85`
  * Mathematical Lot Sizing: **`0.52 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2249.85` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2268.82` (Risk Distance: `18.97` pts)
  * +2.5R Take Profit: `2202.43`
  * Mathematical Lot Sizing: **`0.52 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2249.65`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
